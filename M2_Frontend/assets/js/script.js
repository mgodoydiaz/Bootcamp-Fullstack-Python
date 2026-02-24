$(document).ready(function () {

  // Evento 1: Modo Claro/Oscuro (Click)
  $('#theme-toggle').click(function () {
    $('body').toggleClass('dark-mode');

    if ($('body').hasClass('dark-mode')) {
      $(this).html('<i class="fas fa-sun"></i> Día');
      $(this).removeClass('btn-outline-primary').addClass('btn-outline-light');
    } else {
      $(this).html('<i class="fas fa-moon"></i> Noche');
      $(this).removeClass('btn-outline-light').addClass('btn-outline-primary');
    }
  });

  // Evento 2: Animación al hacer Scroll
  function reveal() {
    var windowHeight = $(window).height();
    var scrollTop = $(window).scrollTop();

    $('.reveal').each(function () {
      var elementOffset = $(this).offset().top;
      // Si el elemento entra en la vista de la ventana
      if (elementOffset < (scrollTop + windowHeight - 50)) {
        $(this).addClass('active');
      }
    });
  }

  // Ejecutar al cargar y al hacer scroll
  reveal();
  $(window).scroll(function () {
    reveal();
  });

  // Evento 3: Validación de Formulario en tiempo real (Input/Change)
  function validarFormulario() {
    let nombreValido = $('#nombre').val().trim().length > 0;
    let email = $('#email').val().trim();
    let emailValido = /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);

    // Mostrar/Ocultar error nombre
    if (!nombreValido && $('#nombre').val().length > 0) {
      $('#errorNombre').removeClass('d-none');
    } else {
      $('#errorNombre').addClass('d-none');
    }

    // Mostrar/Ocultar error email
    if (!emailValido && email.length > 0) {
      $('#errorEmail').removeClass('d-none');
    } else {
      $('#errorEmail').addClass('d-none');
    }

    // Habilitar botón si todo es válido
    if (nombreValido && emailValido) {
      $('#btnSubmit').prop('disabled', false);
    } else {
      $('#btnSubmit').prop('disabled', true);
    }
  }

  // Escuchar cambios en los inputs
  $('#nombre, #email').on('input', validarFormulario);

  // Simular envío de formulario
  $('#contactForm').submit(function (e) {
    e.preventDefault(); // Evitar recarga
    $('#btnSubmit').html('<i class="fas fa-spinner fa-spin"></i> Enviando...').prop('disabled', true);

    // Simular delay de servidor
    setTimeout(function () {
      $('#successMsg').removeClass('d-none');
      $('#btnSubmit').html('Enviar Mensaje');
      $('#contactForm')[0].reset();
      validarFormulario(); // re-deshabilitar botón

      // Ocultar mensaje de éxito después de 3 segundos
      setTimeout(() => $('#successMsg').addClass('d-none'), 3000);
    }, 1500);
  });
});
