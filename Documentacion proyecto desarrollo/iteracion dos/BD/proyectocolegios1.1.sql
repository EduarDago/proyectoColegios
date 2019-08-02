
--
-- Volcado de datos para la tabla `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pedroperez1', NULL, 0, 'pedroperez', 'pedro', 'perez', '', 0, 0, '0000-00-00 00:00:00.000000'),
(2, 'andresarcila1', NULL, 0, 'andresarcila', 'andres', 'arcila', '', 0, 0, '0000-00-00 00:00:00.000000'),
(3, 'jaimejaramillo1', NULL, 0, 'jaimejaramillo', 'jaime', 'jaramillo', '', 0, 0, '0000-00-00 00:00:00.000000'),
(4, 'valeriavalencia1', NULL, 0, 'valeriavalencia', 'valeria', 'valencia', '', 0, 0, '0000-00-00 00:00:00.000000'),
(5, 'luisaleguizamon1', NULL, 0, 'luisaleguizamon', 'luisa', 'leguizamon', '', 0, 0, '0000-00-00 00:00:00.000000'),
(6, 'gianpierre1', NULL, 0, 'gianpierre', 'gian', 'pierre', '', 0, 0, '0000-00-00 00:00:00.000000'),
(7, 'oscarosorio1', NULL, 0, 'oscarosorio', 'oscar', 'osorio', '', 0, 0, '0000-00-00 00:00:00.000000');

-- --------------------------------------------------------


--
-- Volcado de datos para la tabla `profesor_profesor`
--

INSERT INTO `profesor_profesor` (`cedula`, `profesion`, `telefono`, `codigoprofesor`, `usuario_id`) VALUES
(10236111, 'licenciado en lenguas modernas', 2147483647, 1, 1),
(10236222, 'licenciado en biología y química', 2147483647, 2, 2),
(10236333, 'sociologo', 2147483647, 3, 3),
(10236555, 'licenciada en biología y química', 2147483647, 5, 5),
(10236666, 'matematico', 2147483647, 6, 6);

--
-- Volcado de datos para la tabla `grado_grado`
--

INSERT INTO `grado_grado` (`idGrado`) VALUES
('10'),
('11'),
('6'),
('7'),
('8'),
('9');

-- --------------------------------------------------------


--
-- Volcado de datos para la tabla `grupo_grupo`
--

INSERT INTO `grupo_grupo` (`idGrupo`, `foraneaGrado_id`) VALUES
('10_1', '10'),
('10_2', '10'),
('10_3', '10'),
('10_4', '10'),
('11_1', '11'),
('11_2', '11'),
('11_3', '11'),
('11_4', '11'),
('6_1', '6'),
('6_2', '6'),
('6_3', '6'),
('6_4', '6'),
('7_1', '7'),
('7_2', '7'),
('7_3', '7'),
('7_4', '7'),
('8_1', '8'),
('8_2', '8'),
('8_3', '8'),
('8_4', '8'),
('9_1', '9'),
('9_2', '9'),
('9_3', '9'),
('9_4', '9');


--
-- Volcado de datos para la tabla `estudiante_estudiante`
--

INSERT INTO `estudiante_estudiante` (`codigo`, `sexo`, `edad`, `email`, `direccion`, `usuarioEstudiante_id`, `foraneaGrupo_id`) VALUES
('1', 'f', 21, 'valeria_v@uc.edu.co', 'cra17#14-42', 4, '10_2'),
('2', 'm', 28, 'oscar_o@uc.edu.co', 'cra71#41-24', 7, '10_2');




-- --------------------------------------------------------

--
-- Volcado de datos para la tabla `materiagrado_materiagrado`
--

INSERT INTO `materiagrado_materiagrado` (`idMateriaGrado`, `nombreMateria`, `foraneaGrado_id`) VALUES
('1', 'Ciencias naturales', '6'),
('101', 'fisica', '11'),
('105', 'quimica', '11'),
('109', 'calculo basico', '11'),
('113', 'literatura', '11'),
('117', 'filosofia', '11'),
('13', 'matematicas', '6'),
('17', 'literatura', '6'),
('21', 'Ciencias naturales', '7'),
('25', 'geografia de america', '7'),
('29', 'historia de america', '7'),
('33', 'matematicas', '7'),
('37', 'literatura', '7'),
('41', 'ingles', '7'),
('45', 'biologia', '8'),
('49', 'geografia universal', '8'),
('5', 'geografia de colombia', '6'),
('53', 'historia universal', '8'),
('57', 'algebra', '8'),
('61', 'literatura', '8'),
('65', 'biologia', '9'),
('69', 'geografia de colombia', '9'),
('73', 'historia de colombia', '9'),
('77', 'algebra', '9'),
('81', 'literatura', '9'),
('85', 'fisica', '10'),
('89', 'quimica', '10'),
('9', 'historia de colombia', '6'),
('93', 'trigonometria', '10'),
('97', 'filosofia', '10');

-- --------------------------------------------------------

--
-- Volcado de datos para la tabla `curso_curso`
--

INSERT INTO `curso_curso` (`idCurso`, `foraneaProfesor_id`, `foraneaGrupo_id`, `foraneaMateriaGrado_id`) VALUES
('1', 2, '8_1', '45'),
('10', 2, '8_3', '49'),
('11', 6, '6_1', '13'),
('12', 6, '6_2', '13'),
('2', 2, '8_2', '45'),
('3', 6, '9_1', '77'),
('4', 6, '9_2', '77'),
('5', 5, '10_3', '89'),
('6', 5, '10_4', '89'),
('7', 3, '11_3', '117'),
('8', 3, '11_4', '117'),
('9', 2, '9_1', '49');

-- --------------------------------------------------------


--
-- Volcado de datos para la tabla `tema_tema`
--

INSERT INTO `tema_tema` (`idTema`, `nombreTema`, `descripcionTema`, `foraneaMateriaGrado_id`) VALUES
('1', 'Pensamiento Númerico', 'Distingue entre números racionales e irracionales.', '13'),
('2', 'Sistemas númericos', 'Realiza operaciones aritméticas con números enteros y fraccionarios', '13'),
('3', 'MRU', 'El movimiento rectilíneo uniforme se designa frecuentemente con el acrónimo MRU. El MRU se caracteriza por:\r\nMovimiento que se realiza sobre una línea recta.\r\nVelocidad constante; implica magnitud y dirección constantes.\r\nLa magnitud de la velocidad recibe el nombre de celeridad o rapidez.\r\nSin aceleración\r\nPara este tipo de movimiento, la distancia recorrida se calcula multiplicando la magnitud de la velocidad por el tiempo transcurrido. Esta relación también es aplicable si la trayectoria no es rectilínea, con tal que la rapidez o módulo de la velocidad sea constante. Por lo tanto, el movimiento puede considerarse en dos sentidos; una velocidad negativa representa un movimiento en dirección contraria al sentido que convencionalmente hayamos adoptado como positivo.', '101');




------------


--
-- Volcado de datos para la tabla `tarea_tarea`
--

INSERT INTO `tarea_tarea` (`idTarea`, `tituloTarea`, `descripcionTarea`, `fechaLimite`, `rutaArchivo`, `logrosTarea`, `foraneaCurso_id`,`foraneaTema_id`) VALUES
(1, 'definiciones basicas sobre biologia', 'defina que son los enlaces de vander walls, cuales son las funciones de los lisosomas y cuales son las funciones del glucocalix en la membrana', '2018-06-25 00:00:00.000000', NULL, 'comprender los conceptos basicos de biologia, identificar conceptos claves sobre procesos biologicos', '2','1'),
(2, 'definiciones algebraicas', 'defina los siguientes terminos: lenguaje algebraico y sus tipos, operaciones con monomios, polinomios y ejemplos representativos', '2018-06-25 00:00:00.000000', NULL, 'identificar las diferencias entre monomios y polinomios', '4','1'),
(3, 'hexeno y sus definiciones', 'formula semidesarrollada de los isomeros del hexeno y sus nombres', '2018-06-25 00:00:00.000000', NULL, 'entender lo que es el hexeno y las partes que lo componen', '5','1'),
(4, 'preguntas sobre logica y conductismo', 'Desarrollar  qué estudia la lógica formal, cómo y para qué (con ejemplos), Explicar cómo se justifican las hipótesis científicas para el inductivismo (neopositivismo) y el falsacionismo.', '2018-06-25 00:00:00.000000', NULL, 'identificar y relacionar las diferentes corrientes del pensamiento cientifico en la filosofia', '7','1');

-- --------------------------------------------------------

INSERT INTO `estudiante_estudiante_tareasestudiante` (`id`, `estudiante_id`, `tarea_id`) VALUES ('1', '1', '1'), ('2', '1', '2');

