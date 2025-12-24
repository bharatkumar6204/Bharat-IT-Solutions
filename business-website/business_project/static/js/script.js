// home
const counters = document.querySelectorAll('.counter');

counters.forEach(counter => {
  let start = 0;
  const target = +counter.dataset.target;
  const speed = 200;

  const updateCounter = () => {
    const inc = target / speed;
    if (start < target) {
      start += inc;
      counter.innerText = Math.ceil(start);
      setTimeout(updateCounter, 15);
    } else {
      counter.innerText = target;
    }
  };

  updateCounter();
});

// about
const aboutSection = document.querySelector(".about");

window.addEventListener("scroll", () => {
  const sectionTop = aboutSection.getBoundingClientRect().top;
  const screenHeight = window.innerHeight;

  if (sectionTop < screenHeight - 100) {
    aboutSection.classList.add("show");
  }
});
// service
const cards = document.querySelectorAll(".service-card");

window.addEventListener("scroll", () => {
  cards.forEach(card => {
    const cardTop = card.getBoundingClientRect().top;
    const screenHeight = window.innerHeight;

    if (cardTop < screenHeight - 100) {
      card.classList.add("show");
    }
  });
});
// projection section
const projects = document.querySelectorAll(".project-card");

window.addEventListener("scroll", () => {
  projects.forEach(card => {
    const top = card.getBoundingClientRect().top;
    const height = window.innerHeight;

    if (top < height - 100) {
      card.classList.add("show");
    }
  });
});


// Wait for DOM to load
window.addEventListener('DOMContentLoaded', () => {
  setTimeout(() => {
    document.querySelectorAll('.success-msg').forEach(msg => {
      msg.style.display = 'none';
    });
  }, 4000); // 4 seconds
});
