class Leaflet {
  constructor() {
    const data = document.querySelector("[data-leaflet='data']")

    if (!data) return

    const [latitude, longitude] = data.value.split(":").map(Number)

    this.addMap(latitude, longitude)
  }

  addMap(latitude, longitude) {
    this.map = L.map('map').setView([latitude, longitude], 14)

    this.addLayer()
    this.addMarker(latitude, longitude)
  }

  addLayer() {
    L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
      maxZoom: 20,
      attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
    }).addTo(this.map)
  }

  addMarker(latitude, longitude) {
    L.marker([latitude, longitude]).addTo(this.map)
  }
}

window.addEventListener("load", () => new Leaflet())