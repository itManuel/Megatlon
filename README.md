# Megatlon
intento de automatizar la turnería de megatlon

Cómo se usa?

Necesias tener phyton3, pip, selenium y el chromedriver (si querés usar navegador chrome) o geckodriver (si querés usar firefox)

<code>
  sudo apt install python3-pip ;  
  sudo apt-get install chromium-chromedriver ;
  pip install selenium
</code>

Se completa en el código los datos necesarios:

_location_ se completa con el nombre de la sede tal cual está en la página de megatlón, ejemplo: "Devoto" "Alcorta" "Caballito II"

_day_ se completa con el día que quiero reservar, como está escrito en la página, ejemplo: "lun" "mar" "mié"

_class_name_ se completa con la clase que quiero reservar, ejemplo: "MegaCross" "Boxeo" "Zumba Outdoor"

_timing_ es el horario en que quiero tomar la clase, ejemplo "19:00"

_user_mail_ es tu usuario en la página

_user_password_ es tu password en la página

O como alternativa, se pueden pasar datos en el command line:
"h:u:p:t:c:d:",["help","user_mail","user_password","timming","class_name","day"]

Y se ejecuta:

<code>
  phyton3 test.py [-u user -p password -t timming -c clase -d dia]
</code>

Ah, que lindo, y cómo se automatiza esto? bueno, podés intentar con cron, para eso vas a precisar algo como <a href="https://ivanderevianko.com/2020/02/xvfb-run-selenium-in-headless-mode-with-any-browser">xvfb</a> y un poco de imaginación para armar en el crontab.

Como ejemplo:
52	18	*	*	6	/usr/bin/xvfb-run /usr/bin/python3 /path/to/Megatlon/test.py -t '19:00' -c 'Boxeo' -d lun >> /path/to/Megatlon/log.log 2>&1
