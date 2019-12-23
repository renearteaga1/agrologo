
$(document).ready(function(){

  $(".product-rate-select").change(function(){
    // alert($(".product-rate-select").val())
    $.ajax({
      url: $("#form-rate-product").attr("data-endpoint"),
      method: $("#form-rate-product").attr("method"),
      data: $("#form-rate-product").serialize(),
      success: function(data){
        console.log('success')
        console.log( data.rate )
        var ratingCount = data.count
        var ratingStar = data.rate
        if (ratingStar == null) {
          ratingStar = 0;
        }

        //count div
        $('.cant-votes').text("(" + ratingCount + ")")

        // RATEYO
          $(function () {
            $("#rateYo").rateYo({
              rating: 0,
              halfStar: true,
              starSvg: '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"><path d="M12 .587l3.668 7.568 8.332 1.151-6.064 5.828 1.48 8.279-7.416-3.967-7.417 3.967 1.481-8.279-6.064-5.828 8.332-1.151z"/></svg>'
            });

            // Getter
          var normalFill = 0
          var normalFill = $("#rateYo").rateYo("option", "rating"); //returns true

          // Setter
          $("#rateYo").rateYo("option", "rating", ratingStar);

          //input rate igual al valor seleccionado en estrellas
          $("#rateYo").click(function(){
            var rating = $("#rateYo").rateYo("rating")
              console.log(rating);
              $("#id_rate").val(rating)
          })

          });
        // $('.lista-productos').html(data.lista)
        // thisForm.trigger('reset');
        // refreshList();
        // rate();
      },
      error: function(errorData){
        console.log('error')
        console.log(errorData)
      }
    });
  });

// RATEYO
  $(function () {
    $("#rateYo").rateYo({
      rating: 0,
      halfStar: true,
      starSvg: '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"><path d="M12 .587l3.668 7.568 8.332 1.151-6.064 5.828 1.48 8.279-7.416-3.967-7.417 3.967 1.481-8.279-6.064-5.828 8.332-1.151z"/></svg>'


    });
    // Getter
  var normalFill = 0
  var normalFill = $("#rateYo").rateYo("option", "rating"); //returns true

  // Setter
  //$("#rateYo").rateYo("option", "rating", ratingStar);

  //input rate igual al valor seleccionado en estrellas
  $("#rateYo").click(function(){
    var rating = $("#rateYo").rateYo("rating")
      console.log(rating);
      $("#id_rate").val(rating)
  })

  });



  function rate(){
    var ratings = {
    }

    $('#table-list > tbody > tr').each(function(index, value){
      var rating = $(this).find('.number-rating').text();
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

  			$('.'+index.replace(/\s/g,'') + ' .stars-inner').css("width",starPercentageRounded);

  		});
  	})
  }

  rate();

})
