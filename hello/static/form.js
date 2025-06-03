document.addEventListener('DOMContentLoaded', () => {
  const form = document.getElementById('registrationForm');
  const firstNameInput = document.getElementById('firstName');
  const lastNameInput = document.getElementById('lastName');
  const phoneInput = document.getElementById('phone');
  const tokenNoInput = document.getElementById('tokenNo');
  const ageInput = document.getElementById('age');
  const diseaseInfoInput = document.getElementById('diseaseInfo');

  const firstNameError = document.getElementById('firstNameError');
  const lastNameError = document.getElementById('lastNameError');
  const phoneError = document.getElementById('phoneError');
  const tokenNoError = document.getElementById('tokenNoError');
  const ageError = document.getElementById('ageError');
  const diseaseInfoError = document.getElementById('diseaseInfoError');

  form.addEventListener('submit', (e) => {
    e.preventDefault();

    let isValid = true;

    // Validate first name
    if (firstNameInput.value.trim() === '') {
      firstNameError.textContent = 'First name is required.';
      isValid = false;
    } else {
      firstNameError.textContent = '';
    }

    // Validate last name
    if (lastNameInput.value.trim() === '') {
      lastNameError.textContent = 'Last name is required.';
      isValid = false;
    } else {
      lastNameError.textContent = '';
    }

    // Validate phone
    if (phoneInput.value.trim() === '') {
      phoneError.textContent = 'Phone is required.';
      isValid = false;
    } else if (!validatePhone(phoneInput.value)) {
      phoneError.textContent = 'Invalid phone format.';
      isValid = false;
    } else {
      phoneError.textContent = '';
    }

    // Validate token no.
    if (tokenNoInput.value.trim() === '') {
      tokenNoError.textContent = 'Token No. is required.';
      isValid = false;
    } else {
      tokenNoError.textContent = '';
    }

    // Validate age
    if (ageInput.value.trim() === '') {
      ageError.textContent = 'Age is required.';
      isValid = false;
    } else {
      ageError.textContent = '';
    }

    // Validate disease information
    if (diseaseInfoInput.value.trim() === '') {
      diseaseInfoError.textContent = 'Disease information is required.';
      isValid = false;
    } else {
      diseaseInfoError.textContent = '';
    }

    if (isValid) {
      form.submit();
    }
  });

  function validatePhone(phone) {
    const re = /^\d{10}$/;
    return re.test(String(phone));
  }
});
