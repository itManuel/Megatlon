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

_day_ se completa con el día que quiero reserver, como está escrito en la página, ejemplo: "lun" "mar" "mié"

_class_name_ se completa con la clase que quiero reservar, ejemplo: "MegaCross" "Boxeo" "Zumba Outdoor"

_timing_ es el horario en que quiero tomar la clase, ejemplo "19:00"

_user_mail_ es tu usuario en la página

_user_password_ es tu password en la página

Y se ejecuta:

<code>
  phyton3 test.py
</code>
