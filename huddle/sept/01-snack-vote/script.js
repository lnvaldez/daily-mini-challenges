document.addEventListener("DOMContentLoaded", function () {
  const pollForm = document.getElementById("poll-form");
  const doritoCount = document.getElementById("dorito-count");
  const oreoCount = document.getElementById("oreo-count");
  const pringleCount = document.getElementById("pringle-count");

  let doritoVotes = 0;
  let oreoVotes = 0;
  let pringleVotes = 0;

  pollForm.addEventListener("submit", function (e) {
    e.preventDefault();
    const formData = new FormData(pollForm);
    const userVote = formData.get("vote");

    if (userVote === "doritos") {
      doritoVotes++;
    } else if (userVote === "oreos") {
      oreoVotes++;
    } else {
      pringleVotes++;
    }
    updateResults();
  });

  function updateResults() {
    doritoCount.textContent = doritoVotes;
    oreoCount.textContent = oreoVotes;
    pringleCount.textContent = pringleVotes;
  }
});
