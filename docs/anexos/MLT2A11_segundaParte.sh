#!/bin/bash
rutaAbsoluta="/home/<user>/Desktop"
carpeta="MLT2A11_Varibles2"
archivo="denunciaMetro.txt"
pasosDenuncia="Pasos para denunciar acoso"
numerosDenuncia="11-22-33-44"

cd ${rutaAbsoluta}
mkdir ${carpeta}
cd ${carpeta}
touch ${archivo}
echo ${pasosDenuncia}>>${archivo}
echo ${numerosDenuncia} >> ${archivo}
ls ${rutaAbsoluta}
cat ${archivo}
