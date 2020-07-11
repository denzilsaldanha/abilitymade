document.getElementById('orthotist').addEventListener('click',loadOrthotist);

function loadOrthotist(){
    var xhttp =new XMLHttpRequest();
    xhttp.open('GET', 'http://127.0.0.1:5000/orthotist', true);
      var count = 1;

      xhttp.onload = function(){
        if(this.status == 200){
          var orthotist = JSON.parse(this.responseText);


          var output = '<h1>Orthotist</h1>';
          for(var i in orthotist){
            output +=
              '<div ">' +
              '<h3>Orthotist'+count+'</h3>'+
              '<ul>' +
              '<li>Practice Name: '+orthotist[i].p_name+'</li>' +
              '<li>Address: '+orthotist[i].address+'</li>' +
              '<li>Phone Number: '+orthotist[i].ph+'</li>' +
              '<li>Orthotist Name: '+orthotist[i].o_name+'</li>' +
              '</ul>' +
              '</div>';
             count ++;
          }
          else if (this.status == 404){
          console.log('Error 404: NotFound')
          }

          document.getElementById('users').innerHTML = output;
        }
      }
}