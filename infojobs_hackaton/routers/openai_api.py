import openai
import os
from fastapi import APIRouter

from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.environ["OPENAI_API_KEY"]

router = APIRouter(
    prefix="/openai",
    tags=["openai"],
)

offer = {
    "title": "TECNICO EN CONTABILIDAD Y FINANZAS",
    "id": "ad2e4aaebf48f686fe5714d3619c7a",
    "state": 1,
    "creationDate": "2023-04-30T07:22:33.000+0000",
    "updateDate": "2023-05-21T08:30:02.000+0000",
    "city": "Madrid",
    "externalUrlForm": "",
    "blocked": False,
    "applications": 61,
    "province": {"id": 33, "value": "Madrid"},
    "experienceMin": {"id": 3, "value": "Al menos 3 años"},
    "category": {"id": 10, "value": "Administración de empresas"},
    "subcategory": {"id": 3005, "value": "Finanzas y contabilidad"},
    "studiesMin": {"id": 110, "value": "Diplomatura"},
    "residence": {"id": 1, "value": "No Requerido"},
    "country": {"id": 17, "value": "España"},
    "teleworking": {"id": 3, "value": "Híbrido"},
    "contractType": {"id": 1, "value": "Indefinido"},
    "journey": {"id": 1, "value": "Completa"},
    "subSegment": 22,
    "profile": {
        "id": "66565152575356671111101006284563014736",
        "name": "Conciliat",
        "description": "Especialistas en Selección de personal en  el campo financiero y de recursos humanos\r\n\r\nEstamos presentes en seis países europeos, habiendo abierto nuestra primera oficina en España a principios del 2002. \r\n \r\nUn trabajo de especialistas. \r\n\r\nLa formación de todos los consultores de Conciliat proviene del área financiera y de los recursos humanos y con ello ponen al servicio de sus clientes y candidatos su experiencia en ambas áreas de empresa.\r\n\r\nCONCILIAT Y EL CANDIDATO\r\n\r\nNuestra experiencia en el campo de la contabilidad, las finanzas y los recursos humanos nos permita asesorar al candidato en la búsqueda de un nuevo reto profesional y en la planificación de su carrera. \r\n\r\nNuestros clientes son empresas españolas y multinacionales que ofrecen nuevas oportunidades de carrera en el campo de las finanzas y de los recursos humanos\r\nPonemos a disposición de nuestros candidatos no sólo una descripción detallada de los puestos a los que se presenta sino también amplia información sobre la empresa, su entorno y cultura",
        "province": {"id": 33, "value": "Madrid"},
        "web": "http://www.conciliat.es",
        "numberWorkers": 10,
        "logoUrl": "https://multimedia.infojobs.net/api/v1/tenants/c7e2b9c1-8480-43b0-ad9e-000c17aa2cbb/domains/718302b6-5343-43d3-a8a3-829dc3da0893/buckets/6f3ab1cc-5920-4f4e-b131-46a4587a0e1f/images/d3/d3afd86e-7719-43e1-a542-473ac973ab0d?jwt=eyJhbGciOiJSUzI1NiJ9.eyJpYXQiOjE1NDE0OTUwMDAsInJxcyI6IkdFVFxcL3RlbmFudHMvYzdlMmI5YzEtODQ4MC00M2IwLWFkOWUtMDAwYzE3YWEyY2JiL2RvbWFpbnMvNzE4MzAyYjYtNTM0My00M2QzLWE4YTMtODI5ZGMzZGEwODkzL2J1Y2tldHMvNmYzYWIxY2MtNTkyMC00ZjRlLWIxMzEtNDZhNDU4N2EwZTFmL2ltYWdlcy9kMy9kM2FmZDg2ZS03NzE5LTQzZTEtYTU0Mi00NzNhYzk3M2FiMGQiLCJtZXRhZGF0YSI6eyJydWxlIjp7InZlcnNpb24iOiIyMDE2LTEwIiwiYWN0aW9ucyI6W119fX0.SGcJX4LA6rMklqzMvksluZvi663zvLFtilo-Wb0btrpP_lheZeYEAwU6VV-Sr1ARrc30Bza5tCwTIcXf0Wm4l4A8lj-rhqulsI8DpKKtsSCz7Qh3lF_KbBuxrFuUR3rsdXQNHN1AWADnmV4ITYsK--mUk4K6j3AddTUxi77INnJvCSFsgOBz6oJl9iGU01tYDaruJuvHs896LvnLyTQxeUbxcK-IM3BVI6lO1J24IyVT0_CCRaplhuxBN6O4M-E60-zoYSXYaCbLx80vaspcY9z8F2y7QhxtaVs4LDvrFNtTNNKHKktwv2xZ6Gc6zo8uGuQEPJRvtC3lWoYO-PW7dQ&AccessKeyId=d724d9a53d95a810",
        "url": "http://www.conciliat.es",
        "corporateWebsiteUrl": "/conciliat/em-i66565152575356671111101006284563014736",
        "websiteUrl": "",
        "hidden": False,
        "typeIndustry": {"id": 27, "value": "Servicios de RRHH"},
        "country": {"id": 17, "value": "España"},
        "corporateResponsive": False,
        "showCorporativeHeader": False,
        "clientId": 8603956006,
        "withoutAds": False,
        "followable": True,
    },
    "cityPD": 3533,
    "zipCode": "28033",
    "latitude": 0,
    "longitude": 0,
    "exactLocation": False,
    "department": "FINANCIERO",
    "vacancies": 1,
    "minRequirements": "PERFIL DESEADO:\r\n\r\nDiplomatura/Licenciatura en ADE o similar, se valorará master en auditoría. \r\n\r\nExperiencia de 3 a 4 años en departamento administración de compañía con gran volumen de transacciones. Se valorará experiencia previa en auditoría o en consultoría BPO, o haber realizado un programa master en auditoria.\r\n\r\nAcostumbrado a trabajar en entornos con elevado volumen de datos y procesos de facturación de clientes y aprovisionamientos complejos\r\n\r\nCapaz de obtener la visión global de los procesos en los que está involucrado. Acostumbrado a realizar propuestas de mejoras sobre los procedimientos, participando en la revisión de procesos y proponiendo la elaboración de controles sobre el ciclo de cuentas por cobrar, cuentas a pagar, tesorería e impuestos. \r\n\r\nHabilidades analíticas, acostumbrado a trabajar con información procedente de distintas fuentes \r\n\r\nRigurosidad y atención al detalle en los trabajos que realiza\r\n\r\nPerfil orientado a la digitalización y automatización de procesos\r\n\r\nSerá un plus el aportar experiencia y conocimiento del sector eléctrico será un plus\r\n\r\nSe valorará conocimiento de Microsoft Axapta, Navision o similar. Usuario avanzado del Paquete Office, en especial Excel.\r\n\r\nBuen nivel de inglés (B2)\r\n\r\nCapacidad de trabajo en equipo",
    "description": "Nuestro cliente, importante empresa nacional del sector de la energía, busca completar su equipo financiero con la figura de un:\r\n\r\nTECNICO SENIOR EN CONTABILIDAD Y FINANZAS\r\n\r\nMISION DEL PUESTO: En dependencia del Responsable de Administración y Contabilidad, la persona seleccionada se responsabilizará de tareas de contabilidad general, fiscalidad (impuestos y tasas), facturación y control de clientes y proveedores, conciliación bancaria, además de la elaboración de tareas necesarias para los Estados financieros de la compañía. \r\n\r\nFUNCIONES:\r\n\r\nContabilidad General:\r\n-\tRegistro diario de movimientos contables. \r\n-\tControl, liquidación y cobro de facturas clientes.\r\n-\tControl, facturación y pago proveedores / acreedores. \r\n-\tControl, conciliación y presentación tasa municipal mensual, y resto de impuestos (IA, Impuesto Electricidad, etc.).\r\n-\tControl y ejecución del ciclo de pagos de la compañía. Registro y conciliación diaria movimientos bancarios.\r\n-\tArchivo y documentación.\r\nMejora de procesos y automatización de tareas\r\n-\tBúsqueda de mejora continua de los procesos y procedimientos del Área, para lograr una mayor eficiencia y eficacia.\r\n-\tParticipación activa aportando mejoras en los procesos y mejora del Área\r\n-\tSistematización y automatización de tareas\r\n-\tControl financiero y estados financieros\r\n-\tAnálisis, conciliación y control de cuentas contables.\r\n-\tControl y seguimiento de provisiones contables de ingresos conciliación de facturas pendientes de emitir y \r\n-\tControl y seguimiento de provisiones contables de aprovisionamiento y gestión y conciliación de facturas pendientes de recibir \r\n-\tElaborar informes periódicos de gestión internos \r\n-\tDocumentar y aportar información necesaria que sea requerida en cada momento para el análisis financiero de la empresa",
    "desiredRequirements": "PERSONALIDAD:\r\n\r\nHabilidades de comunicación, trabajo en equipo compartiendo responsabilidades y siempre tendente a echar una mano\r\n\r\nLiderazgo en las tareas y/o áreas de responsabilidad asignadas\r\n\r\nCapacidad e independencia en la realización de sus funciones\r\nBuscamos a una persona con iniciativa, proactiva, que proponga mejoras en procesos y procedimientos dentro del área y que busquen ir más allá de lo encomendado y que se divierten con el trabajo. Visión global e involucración en la cultura y en la visión y misión de la empresa formando parte integrante de la misma \r\n\r\nSE OFRECE: Contrato indefinido con período de prueba. Incorporación a una empresa líder en su sector, en crecimiento y en el seno de un equipo joven. Posibilidad de progresión y revisión en un futuro. \r\n\r\nSALARIO: En función de la experiencia aportada por el candidato. \r\nOrientativo en el entorno de los 28-32.000 euros brutos anuales más un bono aproximado en función del rendimiento de 1.500 euros más seguro médico y vida y tickets restaurant. \r\n\r\nTeletrabajo un día a la semana o alternativamente las tardes de lunes a jueves (ambos en función de la organización del departamento)\r\n\r\nHorario flexible entre 8 y 9 de la mañana con salida por la tarde entre 17.30 y 18.30. Viernes jornada continuada. Julio y Agosto y el periodo de navidad (día 22 hasta reyes) jornada intensiva. 24 días laborables de vacaciones y no se trabaja ni el 24 ni el 31.\r\n\r\nZONA DE TRABAJO: Madrid Ciudad",
    "commissions": "",
    "contractDuration": "",
    "referenceId": "",
    "detailedStudiesId": 78,
    "studying": False,
    "showPay": True,
    "maxPay": {
        "amount": 33000,
        "amountId": 285,
        "periodId": 3,
        "periodValue": "Bruto/año",
        "amountValue": "33.000 €",
    },
    "minPay": {
        "amount": 27000,
        "amountId": 275,
        "periodId": 3,
        "periodValue": "Bruto/año",
        "amountValue": "27.000 €",
    },
    "schedule": "",
    "languages": [{"name": "Inglés", "level": "Intermedio"}],
    "jobLevel": {"id": 2, "value": "Empleado/a"},
    "staffInCharge": {"id": 1, "value": "0"},
    "hasKillerQuestions": 1,
    "hasOpenQuestions": 1,
    "epreselec": False,
    "fiscalAddress": "c/ Aleixandre nº8 3ºD, 08033 Madrid, MADRID, España",
    "shouldAskExportConsent": True,
    "exportConsentName": "::8603956006",
    "link": "https://www.infojobs.net/madrid/tecnico-contabilidad-finanzas/of-iad2e4aaebf48f686fe5714d3619c7a",
    "active": True,
    "archived": False,
    "deleted": False,
    "disponibleForFullVisualization": True,
    "availableForVisualization": True,
    "multiProvince": False,
    "skillsList": [
        {"skill": "Tesorería"},
        {"skill": "Contabilidad"},
        {"skill": "IRPF"},
        {"skill": "IVA"},
        {"skill": "Conciliación bancaria"},
        {"skill": "Mejora de Procesos"},
        {"skill": "Impuestos"},
        {"skill": "Facturación"},
        {"skill": "Estados financieros"},
        {"skill": "Microsoft Dynamics NAV (Navision)"},
    ],
    "salaryDescription": "27.000€ - 33.000€ Bruto/año",
    "upsellingsList": [
        {
            "productId": 475,
            "productName": "Subir a las primeras posiciones cada semana",
            "startDate": "2023-04-29T22:00:00.000Z",
            "endDate": "2023-05-29T22:00:00.000Z",
        }
    ],
}


@router.post("/summary/")
def get_completion(job_offer, model="gpt-3.5-turbo"):
    prompt = f"""
    Tu trabajo es generar un resumen de una oferta de trabajo obtenida \
    de un portal de trabajos llamado Infojobs.

    Te voy a proporcionar los datos de la oferta en formato JSON entre backpicks más abajo. Tu debes resumir la oferta de trabajo y devolver el resultado texto plano. Debes transformar los números a texto. Por ejemplo: 5 -> cinco, 9 -> Nueve, 20 -> veinte. 
     
    El resumen no debe ocupar más de 100 palabras y debe incluir una breve descripción de la oferta, el nombre de la empresa,
    la ciudad, los requerimientos del puesto de trabajo y el sueldo si lo hubiera.

    Oferta: ```{job_offer}```
    """

    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,  # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]
