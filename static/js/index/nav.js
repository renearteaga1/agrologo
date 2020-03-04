$(document).ready(function(){

  //Select width nav categorias
  console.log($("#width_tmp_select").width()-2)
  $("#categoria_select").change(function(){
    $("#width_tmp_option").html($("#categoria_select option:selected").text());
    $(this).width($("#width_tmp_select").width()-20);

    console.log($("#width_tmp_select").width())

    $(".buscar").focus()
  });
  console.log('hola');
})

document.querySelectorAll('.navbar-toggler').addEventListener('click', function(event){
  console.log(event);
});

console.log('hola');
