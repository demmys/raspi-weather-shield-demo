$(() => {
  $htu21dT = $('#htu21d-t');
  $htu21dH = $('#htu21d-h');
  $ms5637T = $('#ms5637-t');
  $ms5637P = $('#ms5637-p');
  $tsys01T = $('#tsys01-t');
  $tsd305T = $('#tsd305-t');
  $tsd305O = $('#tsd305-o');

  let load = () => {
    $.getJSON('/api', null, (data) => {
      console.log(data);
      $htu21dT.text(data.HTU21D.temperature);
      $htu21dH.text(data.HTU21D.humidity);
      $ms5637T.text(data.MS5637.temperature);
      $ms5637P.text(data.MS5637.pressure);
      $tsys01T.text(data.TSYS01.temperature);
      $tsd305T.text(data.TSD305.temperature);
      $tsd305O.text(data.TSD305.object_temperature);
    });
  };

  load();
  setInterval(load, 3000);
});
