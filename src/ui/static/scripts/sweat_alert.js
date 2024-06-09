class SweatAlert {
  constructor() {
    const message = document.querySelector("[data-sweat-alert='message']")

    if (!message) return

    this.show(message.value)
  }

  show(text) {
    Swal.fire({
      icon: "error",
      title: text,
    })
  }
}

window.addEventListener("load", () => new SweatAlert())
