// custom javascript

$( document ).ready(() => {
  console.log('Sanity Check!');
});

$('.btn').on('click', function() {
  $.ajax({
    url: '/mode',
    data: { type: $(this).data('type') },
    method: 'POST'
  })
  .done((res) => {
    //getStatus(res.data.task_id);
    console.log("button clicked")
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
    $.each(res.data, function(key, value){
      $("#configuration").append('<tr><td>'+key+'</td><td>'+value+'</td></tr>');
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
      $("#diagnostics").append('<tr><td>'+key+'</td><td>'+value+'</td></tr>');
    })
  });
}