
  $(document).ready(function(){

    var form = $('.form-nuevo')
    var deletebtn = $(".delete")

    form.submit(function(e){
      e.preventDefault();
      e.stopPropagation();
      console.log('si delete')
      // $('#createModal').modal('toggle');
      $('.modal').modal('hide');
      console.log('Not submited');

      var thisForm = $(this);
      var formAction = thisForm.attr("data-endpoint");
      var httpMethod = thisForm.attr("method");
      var formData = thisForm.serialize();
      console.log(formAction)

    $.ajax({
      url: formAction,
      method: httpMethod,
      data: formData,
      success: function(data){
        console.log('success')
        $('.lista-productos').html(data.lista)
        thisForm.trigger('reset');
        refreshList();
        rate();
      },
      error: function(errorData){
        console.log('error')
        console.log(errorData)
      }
    })
    })

    $(".del").click(function(){
      console.log('sii vaina');
    })

    refreshList();

    function refreshList(){
      var deletebtn = $(".delete")
      $(".lista-productos").on('click', '.delete', function(){
        var thisbtn = $(this)
        $.ajax({
          url: thisbtn.attr("data-url"),
          method: 'GET',
          data: {},
          beforeSend: function(){
            $('#modal-list').modal('show');
          },
          success: function(data){
            console.log('success');
            // $('.lista-productos').html(data.lista)
            $('#modal-list .modal-content').html(data.delete);
          },
          error: function(errorData){
            console.log('error');
            console.log(errorData);
          }
        })
      })
      var form = $('.form-delete')
      $('#modal-list').on('submit', '.form-delete', function(e){
        e.preventDefault();
        e.stopPropagation();
        $('.modal').modal('hide');

        var thisForm = $(this);
        var formAction = thisForm.attr("data-endpoint");
        var httpMethod = thisForm.attr("method");
        var formData = thisForm.serialize();

      $.ajax({
        url: formAction,
        method: httpMethod,
        data: formData,
        success: function(data){
          console.log('success')
          $('.lista-productos').html(data.lista)
          thisForm.trigger('reset');
          refreshList();
          rate();
        },
        error: function(errorData){
          console.log('error')
          console.log(errorData)
        }
      })
      })
    }

    function rate(){
      var ratings = {
      }

      $('#table-list > tbody > tr').each(function(index, value){
        var rating = $(this).find('span').text();
        var name = $(this).find('.name').text();
        ratings[name] = rating;
      });

    	var starsTotal = 5;
    	$(document).ready(function(){
    		$.each(ratings, function(index, value){
    			console.log(index + value);
    			var starPercentage = (value / starsTotal) * 100;

    			var starPercentageRounded = (Math.round(starPercentage /10 ) * 10)+"%"
    			console.log(starPercentageRounded)

    			$('.'+index + ' .stars-inner').css("width",starPercentageRounded);
    		});
    	})
    }


  })
