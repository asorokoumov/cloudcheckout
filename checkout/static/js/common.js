$(document).ready(function($) {

  document.ontouchmove = function(event) {
    event.preventDefault();
  };

  if (window.innerHeight < window.innerWidth) {
    document.ontouchmove = function(event) {
      return true;
    };
  }

  $(window).on('orientationchange', function() {
    viewportUnitsBuggyfill.refresh();

    if (window.innerHeight < window.innerWidth) {
      document.ontouchmove = function(event) {
        return true;
      };
    } else {
      document.ontouchmove = function(event) {
        event.preventDefault();
      };
    }
  });

  $('#delivery').change(function() {
    $('.delivery-fields').hide();
    $('.content').removeClass('content--without-center');
    $('button[type="submit"]').attr('disabled', false);

    if ($(this).val() === 'courier') {
      $('.courier').show();
    }

    if ($(this).val() === 'pochta') {
      $('.pochta').show();
    }

    if ($(this).val() === 'self') {
      $('.self').show();
    }
  });

  $('.tooltip-char').click(function() {
    $('.tooltip').hide();
    $('.tooltip').removeClass('tooltip--visible');
    var popup = $(this).data('popup');
    $('#' + popup).show();
    $('#' + popup).addClass('tooltip--visible');
  });

  $('.tooltip-close').click(function() {
    $(this).parent().removeClass('tooltip--visible');
  });
});
