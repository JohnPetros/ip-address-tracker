from flask import request, render_template, flash, redirect

from controllers import home_page_controller


def home_page_view():
    try:
        ip_address = ""

        if request.method == "POST":
            ip_address = request.form.get("ip-address")

        data = home_page_controller.execute(ip_address)

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
    except Exception as exception:
        flash(str(exception))
        return redirect("/")
