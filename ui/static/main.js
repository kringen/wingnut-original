// custom javascript

$( document ).ready(() => {
  console.log('Sanity Check!');
});

$('.btn').on('click', function() {
  $.ajax({
    url: '/tasks',
    data: { "queue": $(this).data('queue'), "qualifier": $(this).data('qualifier') },
    method: 'POST'
  })
  .done((res) => {
    //getStatus(res.data.task_id);
    console.log(res.data.task_id)
    getConfiguration();
    getDiagnostics();
  })
  .fail((err) => {
    console.log(err);
  });
});

function getStatus(taskID) {
  $.ajax({
    url: `/tasks/${taskID}`,
    method: 'GET'
  })
  .done((res) => {
    const html = `
      <tr>
        <td>${res.data.task_id}</td>
        <td>${res.data.task_status}</td>
        <td>${res.data.task_result}</td>
      </tr>`
    $('#tasks').prepend(html);
    const taskStatus = res.data.task_status;
    if (taskStatus === 'finished' || taskStatus === 'failed') return false;
    setTimeout(function() {
      getStatus(res.data.task_id);
    }, 1000);
  })
  .fail((err) => {
    console.log(err);
  });
}

function getConfiguration() {
  $.ajax({
    url: `/configuration`,
    method: 'GET'
  })
  .done((res) => {
    console.log(res.data)
    $.each(res.data.configuration.gpio_pins, function(key, value){
      $("#configuration").append('<div class="col-xs-4"> \
        <div class="font-s12 text-white-op">'+key+'</div> \
        <div class="font-s18 text-success">'+value+'</div> \
        </div>')
    })
  });
}

function getDiagnostics() {
  $.ajax({
    url: `/diagnostics`,
    method: 'GET'
  })
  .done((res) => {
    console.log(res.data)
    $.each(res.data.diagnostics, function(key, value){
      $("#diagnostics").append('<div class="row items-push overflow-hidden"> \
      <div class="col-xs-8" data-toggle="appear" data-class="animated fadeInRight" data-timeout="400"> \
          <div class="text-uppercase font-w600 text-white-op">'+key+'</div> \
          <div class="font-s36 font-w300">'+value+'</div> \
      </div> \
  </div>');
    })
  });
}