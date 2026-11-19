document.getElementById("predictionForm").addEventListener("submit",function(e){

e.preventDefault()

let data={

age:age.value,
bp:bp.value,
sg:sg.value,
al:al.value,
su:su.value,

rbc:rbc.value,
pc:pc.value,
pcc:pcc.value,
ba:ba.value,

bgr:bgr.value,
bu:bu.value,
sc:sc.value,

sod:sod.value,
pot:pot.value,

hemo:hemo.value,
pcv:pcv.value,
wc:wc.value,
rc:rc.value,

htn:htn.value,
dm:dm.value,
cad:cad.value,
appet:appet.value,
pe:pe.value,
ane:ane.value

}

fetch("/predict",{

method:"POST",
headers:{"Content-Type":"application/json"},
body:JSON.stringify(data)

})

.then(res=>res.json())

.then(result=>{

document.getElementById("result").innerHTML=result.prediction

})

})