document.addEventListener("DOMContentLoaded", () => {
  const curtain = document.getElementById("pageCurtain");
  const links = document.querySelectorAll("a.nav-link");

  links.forEach(link => {
    link.addEventListener("click", function (e) {

      // Only internal navigation
      const url = link.getAttribute("href");
      if (!url.startsWith("/")) return;

      e.preventDefault();

      // Activate curtain
      curtain.classList.add("is-active");

      // Wait for animation then redirect
      setTimeout(() => {
        window.location.href = url;
      }, 450); // matches animation midpoint
    });
  });
});
