const counter = document.getElementById('visitor-count');
const storageKey = 'resume-challenge-visitor-count';

let count = Number(localStorage.getItem(storageKey) || 0);
count += 1;
localStorage.setItem(storageKey, count);

if (counter) {
  counter.textContent = count;
}
