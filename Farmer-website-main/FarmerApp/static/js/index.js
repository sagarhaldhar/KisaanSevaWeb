
function toggleMenu() {
  var x = document.getElementsByClassName("nav-bar")[0];
  if (x.style.display === "block") {
    x.style.display = "none";
  } else {
    x.style.display = "block";
  }
}


function showDropdown() {
  var dropdownOptions = document.querySelector(
    ".action_container .dropdown_options"
  );
  dropdownOptions.style.display = "block";
}

function hideDropdown() {
  var dropdownOptions = document.querySelector(
    ".action_container .dropdown_options"
  );
  dropdownOptions.style.display = "none";
}

// Function to hide dropdown options when clicking outside of it
function hideDropdownOnClickOutside(event) {
  var dropdownOptions = document.querySelector(
    ".action_container .dropdown_options"
  );
  var isClickInside = dropdownOptions.contains(event.target);
  if (!isClickInside) {
    hideDropdown();
  }
}

// Add event listener to hide dropdown options when clicking outside of it
document.addEventListener("click", hideDropdownOnClickOutside);

// Add event listener to hide dropdown options when clicking anywhere on the entire page
document.body.addEventListener("click", function (event) {
  // Check if the clicked element is part of the dropdown
  if (!event.target.closest(".action_container")) {
    hideDropdown();
  }
});

function rate(score) {
  var stars = document.querySelectorAll(".rating span");
  for (var i = 0; i < stars.length; i++) {
    if (i < score) {
      stars[i].classList.add("active");
    } else {
      stars[i].classList.remove("active");
    }
  }

  var ratingEmoji = document.getElementById("rating-emoji");
  switch (score) {
    case 1:
      ratingEmoji.innerHTML = "😡";
      break;
    case 2:
      ratingEmoji.innerHTML = "😐";
      break;
    case 3:
      ratingEmoji.innerHTML = "😊";
      break;
    case 4:
      ratingEmoji.innerHTML = "😄";
      break;
    case 5:
      ratingEmoji.innerHTML = "😍";
      break;
    default:
      ratingEmoji.innerHTML = "";
  }
}
