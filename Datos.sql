INSERT INTO BiblioUd.Libro (nombreLibro,descripcion,autor,disponibilidad,numCopias) VALUES 
('Estaba La Pajara Pinta Sentada En El Verde Limon','Retrata la vida de una familia de clase media mientras ocurria el bogotazo','Albalucia Angel',1,4)
,('Cabaret Provenza','poesia','Luis Felipe Fabre',1,2)
,('La Resistencia','Una reflexion contra la globalizacion, la clonacion, la masificaion ','Ernesto Sabato',0,1)
;

INSERT INTO BiblioUd.Prestamo (fechaPrestamo,fechaEntrega,multa,cedula_Usuario,id_libro) VALUES 
('2020-08-01','2020-08-25',0,40979866,2)
,('2020-08-10','2020-09-04',0,40979866,1)
,('2020-07-20','2020-08-13',1000,1234567890,1)
;

INSERT INTO BiblioUd.Usuario (Cedula,Nombre,Apellido,edad,Direccion,Passwod,celular) VALUES 
(40979866,'Maria','Naranjo',17,'carrera 68 N 12 7','cba213',987456)
,(1047258369,'Pablo','Jaramillo',16,'carrere 35 N 20 50','acb321',654321)
,(1234567890,'Pedro','Leon',20,'carrera 167 N 50 4','abc123',123456)
;
