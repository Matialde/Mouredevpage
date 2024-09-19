. .\venv\Scripts\Activate.ps1 #activa el entorno virtual
pip install --upgrade pip #actualiza al último pip
pip install -r requirements.txt #instala lo que figure en el archivo requirements.txt
reflex init #inicia reflex
reflex export --frontend-only #exporta solo el frontend
Remove-Item -Recurse -Force "public" #elimina la carpeta public y su contenido
Expand-Archive -Path "frontend.zip" -DestinationPath ".\public" -Force #descomprime la el frontend.zip en la carpeta public.
Remove-Item frontend.zip #elimina el archivo frontend.zip
deactivate #desactiva el entorno virtual

