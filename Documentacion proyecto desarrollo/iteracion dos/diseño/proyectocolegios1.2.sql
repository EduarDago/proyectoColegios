
INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(123, '123', NULL, 0, 'Eduar', 'Eduar', 'Ortega', 'eduar@gmail.com', 0, 0, '0000-00-00 00:00:00.000000'),
(456, '456', NULL, 0, 'Luisda', 'Luis', 'Montoya', 'Luis@gmail.com', 0, 0, '0000-00-00 00:00:00.000000'),
(789, '789', '2018-06-22 00:00:00.000000', 0, 'estudiante1', 'Juan', 'perez', 'estudiante1@gmail.com', 0, 0, '0000-00-00 00:00:00.000000'),
(987, '987', '2018-06-22 00:00:00.000000', 0, 'estudiante2', 'Pepito', 'Lopez', 'estudiante2@gmail.com', 0, 0, '0000-00-00 00:00:00.000000');

INSERT INTO `profesor_profesor` (`cedula`, `profesion`, `telefono`, `codigoprofesor`, `usuario_id`) VALUES
(123, 'profesor Matematicas', 316123456, 71, 123),
(456, 'Profesor Quimica\r\n', 316123456, 72, 456);

--
-- Volcado de datos para la tabla `tema_tema`
--

INSERT INTO `tema_tema` (`idTema`, `nombreTema`, `descripcionTema`) VALUES
('1', 'Pensamiento Númerico', 'Distingue entre nÃºmeros racionales e irracionales.'),
('2', 'Sistemas numericos', 'Realiza operaciones aritmÃ©ticas con nÃºmeros enteros y fraccionarios');


INSERT INTO `curso_curso` (`idCurso`, `nombreMateria`, `foraneaGrado_id`, `foraneaProfesor_id`) VALUES
('1', 'Matemáticas', '61', 71),
('2', 'Fásica', '61', 71),
('3', 'Matemáticas', '62', 71),
('4', 'Quí­mica', '61', 72),
('5', 'Quí­mica ', '62', 72);


INSERT INTO `curso_curso_tema` (`id`, `curso_id`, `tema_id`) VALUES
(1, '1', '1'),
(2, '2', '2');

-- --------------------------------------------------------

INSERT INTO `estudiante_estudiante` (`codigo`, `sexo`, `edad`, `email`, `direccion`, `foraneaGrado_id`, `usuarioEstudiante_id`) VALUES
('20181', 'M', 18, 'estudiante', 'calle falsa 123', '61', 987),
('20182', 'M', 17, 'estudiante2@gmail.com', 'calle falsa 456', '61', 789);

-- --------------------------------------------------------


INSERT INTO `grado_grado` (`idGrado`, `nombre`) VALUES
('61', '6_1'),
('62', '6_2'),
('63', '6_3'),
('71', '7_1'),
('72', '7_2');

-- --------------------------------------------------------

--
-- Volcado de datos para la tabla `materia_materia`
--

INSERT INTO `materia_materia` (`id`, `nombre`, `intensidad`) VALUES
('121', 'Matemáticas', 4),
('122', 'Fisica', 4);

-- --------------------------------------------------------

--
-- Volcado de datos para la tabla `profesor_profesor`
--


-- --------------------------------------------------------

--
-- Volcado de datos para la tabla `tarea_tarea`
--

INSERT INTO `tarea_tarea` (`idTarea`, `tituloTarea`, `descripcionTarea`, `fechaLimite`, `rutaArchivo`, `logrosTarea`, `foraneaCurso_id`, `foraneaTema_id`) VALUES
(4, 'Sumas', 'sumar 3 y 5', '2018-06-02 09:00:00.000000', '', 'sumar', '1', '1'),
(5, 'sumas', 'sumar 5 y 0', '2018-06-02 09:00:00.000000', '', 'sumar', '1', '1'),
(6, 's', 'qwwqwq', '2018-06-03 07:54:00.000000', '', 'wwd', '1', '1'),
(7, 'hola 4', '<p>en los a&ntilde;os mil seicientos&nbsp;</p>', '2018-06-10 07:58:00.000000', '', 'wweew', '1', '1');

-- --------------------------------------------------------


