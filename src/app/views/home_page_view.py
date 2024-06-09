from flask import render_template

from controllers import home_page_controller


def home_page_view():
    data = home_page_controller.execute()

    ip_address = data["ip_address"]
    address = data["address"]
    time = data["time"]
    isp = data["isp"]
    latitude = data["latitude"]
    longitue = data["longitue"]

    return render_template(
        "pages/home.html",
        ip_address=ip_address,
        address=address,
        time=time,
        isp=isp,
        latitude=latitude,
        longitue=longitue,
    )
