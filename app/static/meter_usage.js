function meter_usage(url) {
  var req = new XMLHttpRequest();
  req.responseType = 'json';
  req.open('GET', url, true);
  req.onload  = function() {
    var data_points = req.response;
    var text = "<table><tr><th>Timestamp</th><th>Meter usage</th></tr>";
    var x;
    for (x of data_points) {
      text += "<tr><td>" + x.time + "</td><td>" + x.meterusage + "</td></tr>";
    }
    text += "</table>";
    document.getElementById("meter_usage_table").innerHTML = text;
    document.getElementById("meter_usage_status").innerHTML = "Loading compete.";
  };
req.send(null);
};
