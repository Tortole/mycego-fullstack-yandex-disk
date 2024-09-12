"""
Module with views for manipulating Yandex Disk files
"""

from django.views import View
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse, StreamingHttpResponse

import json
import requests
from datetime import datetime
from urllib.parse import urlencode, unquote


YANDEX_API = "https://cloud-api.yandex.net/v1/disk/public/resources"
YANDEX_API_DOWNLOAD = "https://cloud-api.yandex.net/v1/disk/public/resources/download"


def get_dir_link(base_link: str, public_key: str, path: str) -> str:
    """
    Makes an internal link to browse the directory

    Arguments:
        base_link - str - main part of the link to which other parameters will be added
        public_key - str - public link to Yandex Disk root directory
        path - str - path to the browsing subdirectory in the root directory on Yandex Disk

    Return:
        str - internal link to browse the directory
    """

    return (
        base_link
        + "?"
        + urlencode(
            {
                "public_key": public_key,
                "path": path,
            }
        )
    )


def get_dir_download_link(public_key: str, path: str) -> str:
    """
    Makes an external link to download the directory

    Arguments:
        public_key - str - public link to Yandex Disk root directory
        path - str - path to the selected subdirectory in the root directory on Yandex Disk

    Return:
        str - external link to download the directory
    """

    dir_link = (
        YANDEX_API_DOWNLOAD
        + "/?"
        + urlencode(
            {
                "public_key": public_key,
                "path": path,
            }
        )
    )
    dir_response = requests.get(dir_link)
    dir_response_data = json.loads(dir_response.text)
    return dir_response_data["href"]


class YandexFilesView(LoginRequiredMixin, View):
    """
    View for read and downloading files from Yandex Disk
    """

    login_url = reverse_lazy("login")
    template_name = "yandex_disk_interface/files_table.html"

    def get(self, request: HttpRequest) -> HttpResponse:
        """
        Collects a files list if a public_key was passed and redirects the user to a page with
        a files table

        Accept parameters for Yandex Disk API
        """

        # If parameters was passed
        if request.GET:
            response = requests.get(YANDEX_API, params=request.GET)
            response_data = json.loads(response.text)

            # If error on requests
            if "error" in response_data:
                return render(
                    request,
                    self.template_name,
                    context={"error": response_data["message"]},
                )

            # Making a list of files with attributes
            files = []
            for item in response_data["_embedded"]["items"]:
                files.append(
                    {
                        "name": item["name"],
                        "type": item.get("mime_type", item["type"]).split("/")[0],
                        "created_date": datetime.fromisoformat(item["created"]),
                        "download_link": (
                            item.get("file")
                            if item["type"] == "file"
                            else get_dir_download_link(
                                request.GET.get("public_key"),
                                item["path"],
                            )
                        ),
                    }
                )

                # If a directory, then add a link to browse that directory
                if item["type"] == "dir":
                    files[-1]["dir_link"] = get_dir_link(
                        reverse("yandex_files"),
                        request.GET.get("public_key"),
                        item["path"],
                    )

            # Link to download the current browsing directory
            current_dir_download_link = get_dir_download_link(
                request.GET.get("public_key"),
                response_data["path"],
            )

            context = {
                "files": files,
                "current_dir_download_link": current_dir_download_link,
            }

            # If the current browsing directory not root, then add link to upper directory
            if "path" in request.GET and len(request.GET.get("path")) > 0:
                context["back_dir_link"] = get_dir_link(
                    reverse("yandex_files"),
                    request.GET.get("public_key"),
                    request.GET.get("path").rsplit("/", 1)[0],
                )

            return render(request, self.template_name, context=context)
        else:
            return render(request, self.template_name)

    def post(self, request: HttpRequest) -> HttpResponse:
        """
        Downloads the file from the passed external link and passes it to the user
        """

        # Request download file stream
        response = requests.get(request.POST.get("download_link"), stream=True)
        if response.status_code == 200:
            # Create a StreamingHttpResponse to pass the file to the user
            view_response = StreamingHttpResponse(
                response.iter_content(chunk_size=8192),
                content_type=response.headers.get("content-type"),
            )

            # Set a filename for download
            view_response["Content-Disposition"] = unquote(
                response.headers.get("Content-Disposition").replace("*=UTF-8''", "=")
            )

            return view_response
        else:
            return HttpResponse("File could not be downloaded", status=404)
