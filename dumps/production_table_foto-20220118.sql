--
-- PostgreSQL database dump
--

-- Dumped from database version 12.9 (Ubuntu 12.9-0ubuntu0.20.04.1)
-- Dumped by pg_dump version 12.9 (Ubuntu 12.9-0ubuntu0.20.04.1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: watermarks_foto; Type: TABLE; Schema: public; Owner: vvf
--

CREATE TABLE public.watermarks_foto (
    id integer NOT NULL,
    date timestamp with time zone NOT NULL,
    image character varying(100),
    image_thumbails character varying(100),
    image_watermarks character varying(100),
    description character varying(1000) NOT NULL,
    created_date timestamp with time zone NOT NULL,
    last_modified timestamp with time zone NOT NULL,
    category_id integer,
    user_id integer,
    title character varying(255) NOT NULL
);


ALTER TABLE public.watermarks_foto OWNER TO vvf;

--
-- Name: watermarks_foto_id_seq; Type: SEQUENCE; Schema: public; Owner: vvf
--

CREATE SEQUENCE public.watermarks_foto_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.watermarks_foto_id_seq OWNER TO vvf;

--
-- Name: watermarks_foto_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vvf
--

ALTER SEQUENCE public.watermarks_foto_id_seq OWNED BY public.watermarks_foto.id;


--
-- Name: watermarks_foto id; Type: DEFAULT; Schema: public; Owner: vvf
--

ALTER TABLE ONLY public.watermarks_foto ALTER COLUMN id SET DEFAULT nextval('public.watermarks_foto_id_seq'::regclass);


--
-- Data for Name: watermarks_foto; Type: TABLE DATA; Schema: public; Owner: vvf
--

COPY public.watermarks_foto (id, date, image, image_thumbails, image_watermarks, description, created_date, last_modified, category_id, user_id, title) FROM stdin;
57	2022-01-11 01:00:00+01	galleria/originale/C0021T01.JPG	galleria/thumbails/C0021T01.png	galleria/watermarks/C0021T01.JPG	Esercitazione Montelibretti, SFO 2021	2022-01-11 12:16:36.126408+01	2022-01-11 12:16:36.126426+01	8	11	incendio autovettura
60	2022-01-13 01:00:00+01	galleria/originale/DSC_1115.JPG	galleria/thumbails/DSC_1115.jpeg	galleria/watermarks/DSC_1115.JPG	Recupero con elicottero di un sommozzatore con infortunato in mare.	2022-01-13 10:55:20.733034+01	2022-01-13 10:55:20.733055+01	7	15	Salvataggio in mare
62	2022-01-13 01:00:00+01	galleria/originale/IMG_7697_XQOJJXN.JPG	galleria/thumbails/IMG_7697_XQOJJXN.jpeg	galleria/watermarks/IMG_7697_XQOJJXN.JPG	Simulazione presso le scuole di formazione operative di Montelibretti di un incendio tetto.	2022-01-13 11:13:38.020946+01	2022-01-13 11:13:38.020964+01	8	15	Incendio Tetto
80	2022-01-13 01:00:00+01	galleria/originale/IMG_0312.JPG	galleria/thumbails/IMG_0312.jpeg	galleria/watermarks/IMG_0312.JPG	Naufragio Costa Concordia, operazioni dei Vigili del Fuoco	2022-01-13 18:02:28.675907+01	2022-01-14 00:26:02.629484+01	9	1	CONCORDIA
78	2022-01-13 01:00:00+01	galleria/originale/_MG_5120.JPG	galleria/thumbails/_MG_5120.jpeg	galleria/watermarks/_MG_5120.JPG	Naufragio Costa Concordia, operazioni dei Vigili del Fuoco	2022-01-13 18:02:28.635588+01	2022-01-14 00:26:47.914969+01	9	1	CONCORDIA
82	2022-01-13 01:00:00+01	galleria/originale/IMG_4071.JPG	galleria/thumbails/IMG_4071.jpeg	galleria/watermarks/IMG_4071.JPG	Naufragio Costa Concordia, operazioni dei Vigili del Fuoco	2022-01-13 18:02:28.715781+01	2022-01-14 00:27:35.64711+01	9	1	CONCORDIA
81	2022-01-13 01:00:00+01	galleria/originale/IMG_3541.JPG	galleria/thumbails/IMG_3541.jpeg	galleria/watermarks/IMG_3541.JPG	Naufragio Costa Concordia, operazioni dei Vigili del Fuoco	2022-01-13 18:02:28.695558+01	2022-01-14 00:29:49.981034+01	9	1	CONCORDIA
77	2022-01-13 01:00:00+01	galleria/originale/_MG_4764.JPG	galleria/thumbails/_MG_4764.jpeg	galleria/watermarks/_MG_4764.JPG	Naufragio Costa Concordia, operazioni dei Vigili del Fuoco	2022-01-13 18:02:28.615297+01	2022-01-14 00:28:27.72715+01	9	1	CONCORDIA
73	2022-01-13 01:00:00+01	galleria/originale/IMG_3871_FlWT0j4.jpg	galleria/thumbails/IMG_3871_FlWT0j4.jpeg	galleria/watermarks/IMG_3871_FlWT0j4.jpg	messa in sicurezza	2022-01-13 16:56:02.114241+01	2022-01-14 00:15:48.613761+01	2	1	Demolizione
84	2022-01-13 01:00:00+01	galleria/originale/IMG_9691.JPG	galleria/thumbails/IMG_9691.jpeg	galleria/watermarks/IMG_9691.JPG	Naufragio Costa Concordia, operazioni dei Vigili del Fuoco	2022-01-13 18:02:28.754948+01	2022-01-14 00:28:44.779528+01	9	1	CONCORDIA
61	2022-01-13 01:00:00+01	galleria/originale/DSC03112.JPG	galleria/thumbails/DSC03112.jpeg	galleria/watermarks/DSC03112.JPG	Momento del giuramento degli allievi vigili del fuoco.	2022-01-13 11:00:48.506041+01	2022-01-14 00:17:03.389174+01	5	1	Giuramento allievi vigili del fuoco
76	2022-01-13 01:00:00+01	galleria/originale/_MG_4544.JPG	galleria/thumbails/_MG_4544.jpeg	galleria/watermarks/_MG_4544.JPG	Naufragio Costa Concordia, operazioni dei Vigili del Fuoco	2022-01-13 18:02:28.579717+01	2022-01-14 00:30:05.708172+01	9	1	CONCORDIA
89	2022-01-14 01:00:00+01	galleria/originale/IMG_8636.JPG	galleria/thumbails/IMG_8636.jpeg	galleria/watermarks/IMG_8636.JPG	Capo del Corpo dei Vigili del Fuoco.	2022-01-14 10:48:32.837451+01	2022-01-14 10:48:32.837465+01	5	15	Capo del Corpo
85	2022-01-13 01:00:00+01	galleria/originale/SAM_3834.JPG	galleria/thumbails/SAM_3834.jpeg	galleria/watermarks/SAM_3834.JPG	Naufragio Costa Concordia, operazioni dei Vigili del Fuoco	2022-01-13 18:02:28.774221+01	2022-01-14 00:24:44.266054+01	9	1	CONCORDIA
90	2022-01-14 01:00:00+01	galleria/originale/N70_8068.JPG	galleria/thumbails/N70_8068.jpeg	galleria/watermarks/N70_8068.JPG	Capo del Corpo dei Vigili del Fuoco.	2022-01-14 10:48:34.008938+01	2022-01-14 10:48:34.00895+01	5	15	Capo del Corpo
91	2022-01-14 01:00:00+01	galleria/originale/N70_8140.JPG	galleria/thumbails/N70_8140.jpeg	galleria/watermarks/N70_8140.JPG	Capo del Corpo dei Vigili del Fuoco.	2022-01-14 10:48:35.127693+01	2022-01-14 10:48:35.127705+01	5	15	Capo del Corpo
93	2022-01-14 01:00:00+01	galleria/originale/IMG_3933.jpg	galleria/thumbails/IMG_3933.jpeg	galleria/watermarks/IMG_3933.jpg	Istruzione sull'uso del mototroncatore presso le scuole centrali VVF.	2022-01-14 11:09:58.161399+01	2022-01-14 11:09:58.161417+01	10	15	Mototroncatore
83	2022-01-13 01:00:00+01	galleria/originale/IMG_6238.JPG	galleria/thumbails/IMG_6238.jpeg	galleria/watermarks/IMG_6238.JPG	Naufragio Costa Concordia, operazioni dei Vigili del Fuoco	2022-01-13 18:02:28.735255+01	2022-01-14 00:30:22.609219+01	9	1	CONCORDIA
75	2022-01-13 01:00:00+01	galleria/originale/IMG_1468.JPG	galleria/thumbails/IMG_1468.jpeg	galleria/watermarks/IMG_1468.JPG	Naufragio Costa Concordia, operazioni dei Vigili del Fuoco	2022-01-13 18:02:28.451771+01	2022-01-14 00:29:06.157827+01	9	1	CONCORDIA
79	2022-01-13 01:00:00+01	galleria/originale/IMG_0152.JPG	galleria/thumbails/IMG_0152.jpeg	galleria/watermarks/IMG_0152.JPG	Naufragio Costa Concordia, operazioni dei Vigili del Fuoco	2022-01-13 18:02:28.655317+01	2022-01-14 00:29:24.628207+01	9	1	CONCORDIA
94	2022-01-14 01:00:00+01	galleria/originale/IMG_3925.jpg	galleria/thumbails/IMG_3925.jpeg	galleria/watermarks/IMG_3925.jpg	Istruzione sull'uso del mototroncatore presso le scuole centrali VVF.	2022-01-14 11:09:59.417701+01	2022-01-14 11:09:59.417716+01	10	15	Mototroncatore
87	2022-01-14 01:00:00+01	galleria/originale/Guido_Parisi.JPG	galleria/thumbails/Guido_Parisi.jpeg	galleria/watermarks/Guido_Parisi.JPG	Capo del Corpo dei Vigili del Fuoco.	2022-01-14 10:48:30.287981+01	2022-01-14 10:48:30.287998+01	5	15	Capo del Corpo
88	2022-01-14 01:00:00+01	galleria/originale/IMG_8624.JPG	galleria/thumbails/IMG_8624.jpeg	galleria/watermarks/IMG_8624.JPG	Capo del Corpo dei Vigili del Fuoco.	2022-01-14 10:48:31.740728+01	2022-01-14 10:48:31.740741+01	5	15	Capo del Corpo
86	2022-01-14 01:00:00+01	galleria/originale/CDV_6775.JPG	galleria/thumbails/CDV_6775.jpeg	galleria/watermarks/CDV_6775.JPG	Capo del Corpo dei Vigili del Fuoco.	2022-01-14 10:48:28.913965+01	2022-01-14 10:49:40.532805+01	5	15	Capo del Corpo
92	2022-01-14 01:00:00+01	galleria/originale/DSC_3059.jpg	galleria/thumbails/DSC_3059.jpeg	galleria/watermarks/DSC_3059.jpg	Fabio Dattilo Capo del Corpo Vigili del Fuoco 2019-2021.	2022-01-14 10:55:44.16967+01	2022-01-14 10:55:44.16969+01	5	15	Dattilo
96	2022-01-14 01:00:00+01	galleria/originale/IMG_20191026_154700.jpg	galleria/thumbails/IMG_20191026_154700.jpeg	galleria/watermarks/IMG_20191026_154700.jpg	Drago 65 Elicottero della flotta nazionale Vigili del fuoco.	2022-01-14 11:16:58.964339+01	2022-01-14 11:16:58.964351+01	11	15	Drago 65
98	2022-01-14 01:00:00+01	galleria/originale/IMG_20191026_160803-01.jpeg	galleria/thumbails/IMG_20191026_160803-01.jpeg	galleria/watermarks/IMG_20191026_160803-01.jpeg	Drago 65 Elicottero della flotta nazionale Vigili del fuoco.	2022-01-14 11:17:01.24537+01	2022-01-14 11:17:01.245383+01	11	15	Drago 65
99	2022-01-14 01:00:00+01	galleria/originale/IMG_20191026_160856.jpg	galleria/thumbails/IMG_20191026_160856.jpeg	galleria/watermarks/IMG_20191026_160856.jpg	Drago 65 Elicottero della flotta nazionale Vigili del fuoco.	2022-01-14 11:17:02.457243+01	2022-01-14 11:17:02.457258+01	11	15	Drago 65
101	2022-01-14 01:00:00+01	galleria/originale/IMG_20191026_161839.jpg	galleria/thumbails/IMG_20191026_161839.jpeg	galleria/watermarks/IMG_20191026_161839.jpg	Drago 65 Elicottero della flotta nazionale Vigili del fuoco.	2022-01-14 11:17:04.714754+01	2022-01-14 11:17:04.714766+01	11	15	Drago 65
102	2022-01-14 01:00:00+01	galleria/originale/IMG_20191026_161841.jpg	galleria/thumbails/IMG_20191026_161841.jpeg	galleria/watermarks/IMG_20191026_161841.jpg	Drago 65 Elicottero della flotta nazionale Vigili del fuoco.	2022-01-14 11:17:05.831753+01	2022-01-14 11:17:05.831765+01	11	15	Drago 65
95	2022-01-14 01:00:00+01	galleria/originale/IMG_20191026_212522_267.jpg	galleria/thumbails/IMG_20191026_212522_267.jpeg	galleria/watermarks/IMG_20191026_212522_267.jpg	Drago 65 Elicottero della flotta nazionale Vigili del fuoco.	2022-01-14 11:16:57.726912+01	2022-01-14 11:16:57.726923+01	11	15	Drago 65
97	2022-01-14 01:00:00+01	galleria/originale/IMG_20191026_160759-01.jpeg	galleria/thumbails/IMG_20191026_160759-01.jpeg	galleria/watermarks/IMG_20191026_160759-01.jpeg	Drago 65 Elicottero della flotta nazionale Vigili del fuoco.	2022-01-14 11:17:00.092632+01	2022-01-14 11:17:00.092644+01	11	15	Drago 65
100	2022-01-14 01:00:00+01	galleria/originale/IMG_20191026_161711.jpg	galleria/thumbails/IMG_20191026_161711.jpeg	galleria/watermarks/IMG_20191026_161711.jpg	Drago 65 Elicottero della flotta nazionale Vigili del fuoco.	2022-01-14 11:17:03.595897+01	2022-01-14 11:17:03.59591+01	11	15	Drago 65
103	2022-01-14 01:00:00+01	galleria/originale/IMG_20191026_170923-01.jpeg	galleria/thumbails/IMG_20191026_170923-01.jpeg	galleria/watermarks/IMG_20191026_170923-01.jpeg	Drago 65 Elicottero della flotta nazionale Vigili del fuoco.	2022-01-14 11:17:07.081682+01	2022-01-14 11:17:07.081694+01	11	15	Drago 65
104	2022-01-14 01:00:00+01	galleria/originale/IMG_20191026_171030-01.jpeg	galleria/thumbails/IMG_20191026_171030-01.jpeg	galleria/watermarks/IMG_20191026_171030-01.jpeg	Drago 65 Elicottero della flotta nazionale Vigili del fuoco.	2022-01-14 11:17:08.225804+01	2022-01-14 11:17:08.225816+01	11	15	Drago 65
105	2022-01-14 01:00:00+01	galleria/originale/IMG_0127.JPG	galleria/thumbails/IMG_0127.jpeg	galleria/watermarks/IMG_0127.JPG	Canadair aereo antincendio della flotta aerea Vigili del Fuoco.	2022-01-14 11:30:21.478798+01	2022-01-14 11:30:21.478816+01	11	15	Canadair
106	2022-01-14 01:00:00+01	galleria/originale/IMG_20200908_113431_435-01.jpeg	galleria/thumbails/IMG_20200908_113431_435-01.jpeg	galleria/watermarks/IMG_20200908_113431_435-01.jpeg	Canadair aereo antincendio della flotta aerea Vigili del Fuoco.	2022-01-14 11:30:22.837932+01	2022-01-14 11:30:22.837947+01	11	15	Canadair
107	2022-01-14 01:00:00+01	galleria/originale/RFA_0555.jpg	galleria/thumbails/RFA_0555.jpeg	galleria/watermarks/RFA_0555.jpg	Canadair aereo antincendio della flotta aerea Vigili del Fuoco.	2022-01-14 11:30:24.029929+01	2022-01-14 11:30:24.029941+01	11	15	Canadair
108	2022-01-14 01:00:00+01	galleria/originale/RFA_0563.jpg	galleria/thumbails/RFA_0563.jpeg	galleria/watermarks/RFA_0563.jpg	Canadair aereo antincendio della flotta aerea Vigili del Fuoco.	2022-01-14 11:30:25.193605+01	2022-01-14 11:30:25.193616+01	11	15	Canadair
109	2022-01-14 01:00:00+01	galleria/originale/RFA_0852.jpg	galleria/thumbails/RFA_0852.jpeg	galleria/watermarks/RFA_0852.jpg	Canadair aereo antincendio della flotta aerea Vigili del Fuoco.	2022-01-14 11:30:26.354925+01	2022-01-14 11:30:26.354937+01	11	15	Canadair
110	2022-01-14 01:00:00+01	galleria/originale/RFA_0886.jpg	galleria/thumbails/RFA_0886.jpeg	galleria/watermarks/RFA_0886.jpg	Canadair aereo antincendio della flotta aerea Vigili del Fuoco.	2022-01-14 11:30:27.564632+01	2022-01-14 11:30:27.564644+01	11	15	Canadair
111	2022-01-14 01:00:00+01	galleria/originale/ST3_7873.jpg	galleria/thumbails/ST3_7873.jpeg	galleria/watermarks/ST3_7873.jpg	Canadair aereo antincendio della flotta aerea Vigili del Fuoco.	2022-01-14 11:30:28.664808+01	2022-01-14 11:30:28.66482+01	11	15	Canadair
112	2022-01-14 01:00:00+01	galleria/originale/ST3_7874.jpg	galleria/thumbails/ST3_7874.jpeg	galleria/watermarks/ST3_7874.jpg	Canadair aereo antincendio della flotta aerea Vigili del Fuoco.	2022-01-14 11:30:29.816353+01	2022-01-14 11:30:29.816365+01	11	15	Canadair
113	2022-01-14 01:00:00+01	galleria/originale/ST3_7882.jpg	galleria/thumbails/ST3_7882.jpeg	galleria/watermarks/ST3_7882.jpg	Canadair aereo antincendio della flotta aerea Vigili del Fuoco.	2022-01-14 11:30:30.9569+01	2022-01-14 11:30:30.956911+01	11	15	Canadair
114	2022-01-14 01:00:00+01	galleria/originale/ST3_7893.jpg	galleria/thumbails/ST3_7893.jpeg	galleria/watermarks/ST3_7893.jpg	Canadair aereo antincendio della flotta aerea Vigili del Fuoco.	2022-01-14 11:30:32.055967+01	2022-01-14 11:30:32.055983+01	11	15	Canadair
115	2022-01-14 01:00:00+01	galleria/originale/ST3_7904.jpg	galleria/thumbails/ST3_7904.jpeg	galleria/watermarks/ST3_7904.jpg	Canadair aereo antincendio della flotta aerea Vigili del Fuoco.	2022-01-14 11:30:33.222501+01	2022-01-14 11:30:33.222529+01	11	15	Canadair
116	2022-01-14 01:00:00+01	galleria/originale/WhatsApp_Image_2020-02-12_at_16.12.34.jpeg	galleria/thumbails/WhatsApp_Image_2020-02-12_at_16.12.34.jpeg	galleria/watermarks/WhatsApp_Image_2020-02-12_at_16.12.34.jpeg	Canadair aereo antincendio della flotta aerea Vigili del Fuoco.	2022-01-14 11:30:34.382163+01	2022-01-14 11:30:34.382175+01	11	15	Canadair
122	2022-01-14 01:00:00+01	galleria/originale/1_19.JPG	galleria/thumbails/1_19.jpeg	galleria/watermarks/1_19.JPG	Personale di bordo elicottero drago VVF.	2022-01-14 12:26:56.474318+01	2022-01-14 12:26:56.47433+01	3	15	Elicotteristi
117	2022-01-14 01:00:00+01	galleria/originale/ST3_7895.jpg	galleria/thumbails/ST3_7895.jpeg	galleria/watermarks/ST3_7895.jpg	Canadair della Flotta aerea dei Vigili del Fuoco.	2022-01-14 11:35:21.001308+01	2022-01-14 11:36:00.914226+01	11	15	Canadair
118	2022-01-14 01:00:00+01	galleria/originale/P4012734.JPG	galleria/thumbails/P4012734.jpeg	galleria/watermarks/P4012734.JPG	Intervento con mezzi nautici e aerei VVF sul lago.	2022-01-14 12:23:57.835719+01	2022-01-14 12:23:57.835737+01	11	15	Mezzi VVF
123	2022-01-14 01:00:00+01	galleria/originale/P4012612_2.JPG	galleria/thumbails/P4012612_2.jpeg	galleria/watermarks/P4012612_2.JPG	Personale di bordo elicottero drago VVF.	2022-01-14 12:26:57.592172+01	2022-01-14 12:35:02.0903+01	3	15	Elicotteristi
125	2022-01-14 01:00:00+01	galleria/originale/IMG_6997.jpg	galleria/thumbails/IMG_6997.jpeg	galleria/watermarks/IMG_6997.jpg	Bimodale APS dotata di ruote gommate e ruote ferroviarie, per andare su rotaie.	2022-01-14 12:53:32.540293+01	2022-01-14 12:53:32.540312+01	11	15	Bimodale
126	2022-01-14 01:00:00+01	galleria/originale/IMG_3601.JPG	galleria/thumbails/IMG_3601.jpeg	galleria/watermarks/IMG_3601.JPG	Bimodale APS dotata di ruote gommate e ruote ferroviarie, per andare su rotaie.	2022-01-14 12:53:33.93964+01	2022-01-14 12:53:33.939655+01	11	15	Bimodale
120	2022-01-14 01:00:00+01	galleria/originale/1_13.JPG	galleria/thumbails/1_13.jpeg	galleria/watermarks/1_13.JPG	Personale di bordo elicottero drago VVF.	2022-01-14 12:26:54.214054+01	2022-01-14 12:28:12.908747+01	3	15	Elicotteristi
121	2022-01-14 01:00:00+01	galleria/originale/1_18.JPG	galleria/thumbails/1_18.jpeg	galleria/watermarks/1_18.JPG	Personale di bordo elicottero drago VVF.	2022-01-14 12:26:55.377452+01	2022-01-14 12:35:43.006365+01	3	15	Elicotteristi
119	2022-01-14 01:00:00+01	galleria/originale/1_11.JPG	galleria/thumbails/1_11.jpeg	galleria/watermarks/1_11.JPG	Personale di bordo elicottero drago VVF.	2022-01-14 12:26:52.917761+01	2022-01-14 12:31:24.60887+01	3	15	Elicotteristi
124	2022-01-14 01:00:00+01	galleria/originale/IMG_0051.JPG	galleria/thumbails/IMG_0051.jpeg	galleria/watermarks/IMG_0051.JPG	Personale VVF schierati per intervento aeroportuale con mezzo sullo sfondo.	2022-01-14 12:45:01.765659+01	2022-01-17 15:54:16.176482+01	12	15	Aereoportuali
259	2022-01-14 01:00:00+01	galleria/originale/NAD_2733.jpg	galleria/thumbails/NAD_2733.jpg	galleria/watermarks/NAD_2733.jpg	Frangenti del corso di addestramento allievi Vigili del Fuoco	2022-01-14 16:29:52.471571+01	2022-01-14 16:29:52.471584+01	8	15	Corso allievi VVF
260	2022-01-14 01:00:00+01	galleria/originale/NAD_2739.jpg	galleria/thumbails/NAD_2739.jpg	galleria/watermarks/NAD_2739.jpg	Frangenti del corso di addestramento allievi Vigili del Fuoco	2022-01-14 16:29:53.691242+01	2022-01-14 16:29:53.691258+01	8	15	Corso allievi VVF
262	2022-01-14 01:00:00+01	galleria/originale/NAD_2750.jpg	galleria/thumbails/NAD_2750.jpg	galleria/watermarks/NAD_2750.jpg	Frangenti del corso di addestramento allievi Vigili del Fuoco	2022-01-14 16:29:56.02592+01	2022-01-14 16:29:56.025933+01	8	15	Corso allievi VVF
263	2022-01-14 01:00:00+01	galleria/originale/NAD_2757.jpg	galleria/thumbails/NAD_2757.jpg	galleria/watermarks/NAD_2757.jpg	Frangenti del corso di addestramento allievi Vigili del Fuoco	2022-01-14 16:29:57.145485+01	2022-01-14 16:29:57.145497+01	8	15	Corso allievi VVF
264	2022-01-14 01:00:00+01	galleria/originale/NAD_2774.jpg	galleria/thumbails/NAD_2774.jpg	galleria/watermarks/NAD_2774.jpg	Frangenti del corso di addestramento allievi Vigili del Fuoco	2022-01-14 16:29:58.267996+01	2022-01-14 16:29:58.268008+01	8	15	Corso allievi VVF
265	2022-01-14 01:00:00+01	galleria/originale/NAD_2780.jpg	galleria/thumbails/NAD_2780.jpg	galleria/watermarks/NAD_2780.jpg	Frangenti del corso di addestramento allievi Vigili del Fuoco	2022-01-14 16:29:59.382084+01	2022-01-14 16:29:59.382097+01	8	15	Corso allievi VVF
266	2022-01-14 01:00:00+01	galleria/originale/NAD_2782.jpg	galleria/thumbails/NAD_2782.jpg	galleria/watermarks/NAD_2782.jpg	Frangenti del corso di addestramento allievi Vigili del Fuoco	2022-01-14 16:30:00.521226+01	2022-01-14 16:30:00.521263+01	8	15	Corso allievi VVF
267	2022-01-14 01:00:00+01	galleria/originale/NAD_2789.jpg	galleria/thumbails/NAD_2789.jpg	galleria/watermarks/NAD_2789.jpg	Frangenti del corso di addestramento allievi Vigili del Fuoco	2022-01-14 16:30:01.622576+01	2022-01-14 16:30:01.62259+01	8	15	Corso allievi VVF
268	2022-01-14 01:00:00+01	galleria/originale/NAD_2792.jpg	galleria/thumbails/NAD_2792.jpg	galleria/watermarks/NAD_2792.jpg	Frangenti del corso di addestramento allievi Vigili del Fuoco	2022-01-14 16:30:02.782812+01	2022-01-14 16:30:02.782825+01	8	15	Corso allievi VVF
269	2022-01-14 01:00:00+01	galleria/originale/NAD_2831.jpg	galleria/thumbails/NAD_2831.jpg	galleria/watermarks/NAD_2831.jpg	Frangenti del corso di addestramento allievi Vigili del Fuoco	2022-01-14 16:30:03.986083+01	2022-01-14 16:30:03.986095+01	8	15	Corso allievi VVF
270	2022-01-14 01:00:00+01	galleria/originale/NAD_2842.jpg	galleria/thumbails/NAD_2842.jpg	galleria/watermarks/NAD_2842.jpg	Frangenti del corso di addestramento allievi Vigili del Fuoco	2022-01-14 16:30:05.08595+01	2022-01-14 16:30:05.085962+01	8	15	Corso allievi VVF
271	2022-01-14 01:00:00+01	galleria/originale/NAD_2848.jpg	galleria/thumbails/NAD_2848.jpg	galleria/watermarks/NAD_2848.jpg	Frangenti del corso di addestramento allievi Vigili del Fuoco	2022-01-14 16:30:06.202476+01	2022-01-14 16:30:06.202488+01	8	15	Corso allievi VVF
272	2022-01-14 01:00:00+01	galleria/originale/NAD_2853.jpg	galleria/thumbails/NAD_2853.jpg	galleria/watermarks/NAD_2853.jpg	Frangenti del corso di addestramento allievi Vigili del Fuoco	2022-01-14 16:30:07.336278+01	2022-01-14 16:30:07.336291+01	8	15	Corso allievi VVF
275	2022-01-14 01:00:00+01	galleria/originale/NAD_2896.jpg	galleria/thumbails/NAD_2896.jpg	galleria/watermarks/NAD_2896.jpg	Frangenti del corso di addestramento allievi Vigili del Fuoco	2022-01-14 16:30:10.829185+01	2022-01-14 16:30:10.829198+01	8	15	Corso allievi VVF
276	2022-01-14 01:00:00+01	galleria/originale/NAD_2925.jpg	galleria/thumbails/NAD_2925.jpg	galleria/watermarks/NAD_2925.jpg	Frangenti del corso di addestramento allievi Vigili del Fuoco	2022-01-14 16:30:12.120281+01	2022-01-14 16:30:12.120293+01	8	15	Corso allievi VVF
277	2022-01-14 01:00:00+01	galleria/originale/NAD_2928.jpg	galleria/thumbails/NAD_2928.jpg	galleria/watermarks/NAD_2928.jpg	Frangenti del corso di addestramento allievi Vigili del Fuoco	2022-01-14 16:30:13.337258+01	2022-01-14 16:30:13.337271+01	8	15	Corso allievi VVF
278	2022-01-14 01:00:00+01	galleria/originale/NAD_2961.jpg	galleria/thumbails/NAD_2961.jpg	galleria/watermarks/NAD_2961.jpg	Frangenti del corso di addestramento allievi Vigili del Fuoco	2022-01-14 16:30:14.641706+01	2022-01-14 16:30:14.641719+01	8	15	Corso allievi VVF
279	2022-01-14 01:00:00+01	galleria/originale/NAD_2968.jpg	galleria/thumbails/NAD_2968.jpg	galleria/watermarks/NAD_2968.jpg	Frangenti del corso di addestramento allievi Vigili del Fuoco	2022-01-14 16:30:15.833169+01	2022-01-14 16:30:15.833182+01	8	15	Corso allievi VVF
281	2022-01-14 01:00:00+01	galleria/originale/NAD_3041.jpg	galleria/thumbails/NAD_3041.jpg	galleria/watermarks/NAD_3041.jpg	Frangenti del corso di addestramento allievi Vigili del Fuoco	2022-01-14 16:30:18.127557+01	2022-01-14 16:30:18.127569+01	8	15	Corso allievi VVF
312	2022-01-15 01:00:00+01	galleria/originale/DSC_9127.jpg	galleria/thumbails/DSC_9127.jpeg	galleria/watermarks/DSC_9127.jpg	Manovre di montaggio scala italiana al castello durante il corso allievi VVF presso le SCA.	2022-01-15 17:12:09.144734+01	2022-01-15 17:12:09.144747+01	8	15	Allievi VVF
282	2022-01-14 01:00:00+01	galleria/originale/NAD_3065.jpg	galleria/thumbails/NAD_3065.jpeg	galleria/watermarks/NAD_3065.jpg	Frangenti del corso di addestramento allievi Vigili del Fuoco	2022-01-14 16:30:19.273747+01	2022-01-14 17:19:02.57031+01	8	15	Corso allievi VVF
313	2022-01-15 01:00:00+01	galleria/originale/DSC_9133.jpg	galleria/thumbails/DSC_9133.jpeg	galleria/watermarks/DSC_9133.jpg	Manovre di montaggio scala italiana al castello durante il corso allievi VVF presso le SCA.	2022-01-15 17:12:09.915245+01	2022-01-15 17:12:09.91526+01	8	15	Allievi VVF
273	2022-01-14 01:00:00+01	galleria/originale/NAD_2868.jpg	galleria/thumbails/NAD_2868.jpeg	galleria/watermarks/NAD_2868.jpg	Frangenti del corso di addestramento allievi Vigili del Fuoco	2022-01-14 16:30:08.574768+01	2022-01-15 17:05:30.337141+01	8	15	Corso allievi VVF
314	2022-01-15 01:00:00+01	galleria/originale/DSC_9135.jpg	galleria/thumbails/DSC_9135.jpeg	galleria/watermarks/DSC_9135.jpg	Manovre di montaggio scala italiana al castello durante il corso allievi VVF presso le SCA.	2022-01-15 17:12:10.424465+01	2022-01-15 17:12:10.424477+01	8	15	Allievi VVF
274	2022-01-14 01:00:00+01	galleria/originale/NAD_2880.jpg	galleria/thumbails/NAD_2880.jpeg	galleria/watermarks/NAD_2880.jpg	Frangenti del corso di addestramento allievi Vigili del Fuoco	2022-01-14 16:30:09.702543+01	2022-01-15 17:07:03.211701+01	8	15	Corso allievi VVF
315	2022-01-15 01:00:00+01	galleria/originale/DSC_9140.jpg	galleria/thumbails/DSC_9140.jpeg	galleria/watermarks/DSC_9140.jpg	Manovre di montaggio scala italiana al castello durante il corso allievi VVF presso le SCA.	2022-01-15 17:12:11.211982+01	2022-01-15 17:12:11.211994+01	8	15	Allievi VVF
316	2022-01-15 01:00:00+01	galleria/originale/DSC_9143.jpg	galleria/thumbails/DSC_9143.jpeg	galleria/watermarks/DSC_9143.jpg	Manovre di montaggio scala italiana al castello durante il corso allievi VVF presso le SCA.	2022-01-15 17:12:12.475679+01	2022-01-15 17:12:12.475691+01	8	15	Allievi VVF
317	2022-01-15 01:00:00+01	galleria/originale/DSC_9144.jpg	galleria/thumbails/DSC_9144.jpeg	galleria/watermarks/DSC_9144.jpg	Manovre di montaggio scala italiana al castello durante il corso allievi VVF presso le SCA.	2022-01-15 17:12:12.942141+01	2022-01-15 17:12:12.942153+01	8	15	Allievi VVF
352	2022-01-16 01:00:00+01	galleria/originale/4_5951618413511051203-01.jpeg	galleria/thumbails/4_5951618413511051203-01.jpeg	galleria/watermarks/4_5951618413511051203-01.jpeg	Operazioni di raffreddamento della carcassa di un'auto a seguito di un incendio.	2022-01-16 17:20:37.375374+01	2022-01-16 17:20:37.375392+01	8	15	Raffreddamento
318	2022-01-15 01:00:00+01	galleria/originale/DSC_9145.jpg	galleria/thumbails/DSC_9145.jpeg	galleria/watermarks/DSC_9145.jpg	Manovre di montaggio scala italiana al castello durante il corso allievi VVF presso le SCA.	2022-01-15 17:12:13.49449+01	2022-01-15 17:13:20.406064+01	8	15	Allievi VVF
357	2022-01-16 01:00:00+01	galleria/originale/20082009-DSC_5570.jpg	galleria/thumbails/20082009-DSC_5570.jpeg	galleria/watermarks/20082009-DSC_5570.jpg	Momento della calata in mare di due sommozzatori da elicottero VVF.	2022-01-16 17:33:14.576612+01	2022-01-16 17:33:14.57663+01	17	15	soccorso in mare
361	2022-01-16 01:00:00+01	galleria/originale/IMG_20201110_190815-01.jpeg	galleria/thumbails/IMG_20201110_190815-01.jpeg	galleria/watermarks/IMG_20201110_190815-01.jpeg	Consolle radio VHF in sala operativa VVF.	2022-01-16 17:40:33.161801+01	2022-01-16 17:40:33.161813+01	10	15	Radio VVF
261	2022-01-14 01:00:00+01	galleria/originale/NAD_2747.jpg	galleria/thumbails/NAD_2747.jpg	galleria/watermarks/NAD_2747.jpg	Frangenti del corso di addestramento allievi Vigili del Fuoco	2022-01-14 16:29:54.857779+01	2022-01-14 16:29:54.857791+01	8	15	Corso allievi VVF
258	2022-01-14 01:00:00+01	galleria/originale/NAD_2724.jpg	galleria/thumbails/NAD_2724.jpeg	galleria/watermarks/NAD_2724.jpg	Frangenti del corso di addestramento allievi Vigili del Fuoco	2022-01-14 16:29:50.976434+01	2022-01-14 17:05:47.839195+01	8	1	Corso allievi VVF
358	2022-01-16 01:00:00+01	galleria/originale/23122006-DSC_1200.jpg	galleria/thumbails/23122006-DSC_1200.jpeg	galleria/watermarks/23122006-DSC_1200.jpg	Taglio di un palo con mototroncatrice durante un intervento.	2022-01-16 17:35:27.32183+01	2022-01-16 17:35:27.321847+01	10	15	Mototroncatrice
257	2022-01-14 01:00:00+01	galleria/originale/NAD_2718.jpg	galleria/thumbails/NAD_2718.jpeg	galleria/watermarks/NAD_2718.jpg	Frangenti del corso di addestramento allievi Vigili del Fuoco	2022-01-14 16:29:49.530294+01	2022-01-15 17:03:23.87688+01	8	15	Corso allievi VVF
319	2022-01-15 01:00:00+01	galleria/originale/DSC_9146.jpg	galleria/thumbails/DSC_9146.jpeg	galleria/watermarks/DSC_9146.jpg	Manovre di montaggio scala italiana al castello durante il corso allievi VVF presso le SCA.	2022-01-15 17:18:11.452134+01	2022-01-15 17:18:11.452157+01	8	15	Corso Allievi VVF
320	2022-01-15 01:00:00+01	galleria/originale/DSC_9152.jpg	galleria/thumbails/DSC_9152.jpeg	galleria/watermarks/DSC_9152.jpg	Manovre di montaggio scala italiana al castello durante il corso allievi VVF presso le SCA.	2022-01-15 17:18:13.703651+01	2022-01-15 17:18:13.703663+01	8	15	Corso Allievi VVF
321	2022-01-15 01:00:00+01	galleria/originale/DSC_9154.jpg	galleria/thumbails/DSC_9154.jpeg	galleria/watermarks/DSC_9154.jpg	Manovre di montaggio scala italiana al castello durante il corso allievi VVF presso le SCA.	2022-01-15 17:18:13.892392+01	2022-01-15 17:18:13.892405+01	8	15	Corso Allievi VVF
322	2022-01-15 01:00:00+01	galleria/originale/DSC_9157.jpg	galleria/thumbails/DSC_9157.jpeg	galleria/watermarks/DSC_9157.jpg	Manovre di montaggio scala italiana al castello durante il corso allievi VVF presso le SCA.	2022-01-15 17:18:14.308689+01	2022-01-15 17:18:14.308701+01	8	15	Corso Allievi VVF
323	2022-01-15 01:00:00+01	galleria/originale/DSC_9162.jpg	galleria/thumbails/DSC_9162.jpeg	galleria/watermarks/DSC_9162.jpg	Manovre di montaggio scala italiana al castello durante il corso allievi VVF presso le SCA.	2022-01-15 17:18:14.829194+01	2022-01-15 17:18:14.829217+01	8	15	Corso Allievi VVF
324	2022-01-15 01:00:00+01	galleria/originale/DSC_9166.jpg	galleria/thumbails/DSC_9166.jpeg	galleria/watermarks/DSC_9166.jpg	Manovre di montaggio scala italiana al castello durante il corso allievi VVF presso le SCA.	2022-01-15 17:18:15.317983+01	2022-01-15 17:18:15.317995+01	8	15	Corso Allievi VVF
325	2022-01-15 01:00:00+01	galleria/originale/DSC_9168.jpg	galleria/thumbails/DSC_9168.jpeg	galleria/watermarks/DSC_9168.jpg	Manovre di montaggio scala italiana al castello durante il corso allievi VVF presso le SCA.	2022-01-15 17:18:15.47638+01	2022-01-15 17:18:15.476392+01	8	15	Corso Allievi VVF
326	2022-01-15 01:00:00+01	galleria/originale/DSC_9171.jpg	galleria/thumbails/DSC_9171.jpeg	galleria/watermarks/DSC_9171.jpg	Manovre di montaggio scala italiana al castello durante il corso allievi VVF presso le SCA.	2022-01-15 17:18:16.074606+01	2022-01-15 17:18:16.074617+01	8	15	Corso Allievi VVF
353	2022-01-16 01:00:00+01	galleria/originale/02022018-_DSC4731.jpg	galleria/thumbails/02022018-_DSC4731.jpeg	galleria/watermarks/02022018-_DSC4731.jpg	Controlli di fine intervento a seguito di un incendio di una autocisterna.	2022-01-16 17:23:08.063429+01	2022-01-16 17:23:08.063453+01	17	15	Incendio cistena
362	2022-01-16 01:00:00+01	galleria/originale/PSX_20201110_191455.jpg	galleria/thumbails/PSX_20201110_191455.jpeg	galleria/watermarks/PSX_20201110_191455.jpg	Consolle radio VHF in sala operativa VVF.	2022-01-16 17:40:33.286875+01	2022-01-16 17:40:33.286888+01	10	15	Radio VVF
365	2022-01-16 01:00:00+01	galleria/originale/PSX_20201214_084939.jpg	galleria/thumbails/PSX_20201214_084939.jpeg	galleria/watermarks/PSX_20201214_084939.jpg	Montaggio scala italiana al castello di manovra durante un corso allievi Vigili del Fuoco.	2022-01-16 17:47:20.307142+01	2022-01-16 17:47:20.307161+01	8	15	Corso Allievi
368	2022-01-17 01:00:00+01	galleria/originale/photo5854859247534323256_1.jpg	galleria/thumbails/photo5854859247534323256_1.jpeg	galleria/watermarks/photo5854859247534323256_1.jpg	Personale SAPR in fase di preparazione per il decollo del drone.	2022-01-17 13:19:50.701395+01	2022-01-17 13:19:50.701414+01	15	15	Decollo drone
375	2022-01-17 01:00:00+01	galleria/originale/DSCF2905.jpg	galleria/thumbails/DSCF2905.jpeg	galleria/watermarks/DSCF2905.jpg	Il lavoro dei TAS dei VVF Topografia applicata al soccorso per delimitare o bonificare zone di ricerca in caso di persone scomparse.	2022-01-17 16:11:39.917625+01	2022-01-17 16:11:39.917642+01	14	15	Topografia applicata al soccorso
377	2022-01-17 01:00:00+01	galleria/originale/20180522_esercitazione_NBCR_Oristano_Desogus.jpg	galleria/thumbails/20180522_esercitazione_NBCR_Oristano_Desogus.jpeg	galleria/watermarks/20180522_esercitazione_NBCR_Oristano_Desogus.jpg	Il nucleo NBCR per interventi in luoghi contaminati da sostanze pericolose	2022-01-17 16:32:59.645288+01	2022-01-17 16:32:59.645305+01	18	15	Nucleo Biologico Chimico Radiologico
378	2022-01-17 01:00:00+01	galleria/originale/IMG_8554.JPG	galleria/thumbails/IMG_8554.jpeg	galleria/watermarks/IMG_8554.JPG	Il nucleo NBCR per interventi in luoghi contaminati da sostanze pericolose	2022-01-17 16:33:00.027203+01	2022-01-17 16:33:00.027214+01	18	15	Nucleo Biologico Chimico Radiologico
379	2022-01-17 01:00:00+01	galleria/originale/IMG_8579.JPG	galleria/thumbails/IMG_8579.jpeg	galleria/watermarks/IMG_8579.JPG	Il nucleo NBCR per interventi in luoghi contaminati da sostanze pericolose	2022-01-17 16:33:00.516772+01	2022-01-17 16:33:00.516784+01	18	15	Nucleo Biologico Chimico Radiologico
380	2022-01-17 01:00:00+01	galleria/originale/IMG_8592.JPG	galleria/thumbails/IMG_8592.jpeg	galleria/watermarks/IMG_8592.JPG	Il nucleo NBCR per interventi in luoghi contaminati da sostanze pericolose	2022-01-17 16:33:00.973871+01	2022-01-17 16:33:00.973883+01	18	15	Nucleo Biologico Chimico Radiologico
381	2022-01-17 01:00:00+01	galleria/originale/IMG_8636_WH4qkfF.JPG	galleria/thumbails/IMG_8636_WH4qkfF.jpeg	galleria/watermarks/IMG_8636_WH4qkfF.JPG	Il nucleo NBCR per interventi in luoghi contaminati da sostanze pericolose	2022-01-17 16:33:01.794227+01	2022-01-17 16:33:01.794243+01	18	15	Nucleo Biologico Chimico Radiologico
382	2022-01-17 01:00:00+01	galleria/originale/N.B.C.R..jpg	galleria/thumbails/N.B.C.R..jpeg	galleria/watermarks/N.B.C.R..jpg	Il nucleo NBCR per interventi in luoghi contaminati da sostanze pericolose	2022-01-17 16:33:02.935566+01	2022-01-17 16:33:02.935582+01	18	15	Nucleo Biologico Chimico Radiologico
388	2022-01-17 01:00:00+01	galleria/originale/IMG_0699.JPG	galleria/thumbails/IMG_0699.jpeg	galleria/watermarks/IMG_0699.JPG	Capo Dipartimento VVF con il Capo del Corpo e il Responsabile dell'emergenza durante una Videoconferenza al Centro Operativo Nazionale.	2022-01-17 17:11:53.024813+01	2022-01-17 17:11:53.02483+01	5	15	Dirigenti Nazionali
389	2022-01-17 01:00:00+01	galleria/originale/IMG_0706.JPG	galleria/thumbails/IMG_0706.jpeg	galleria/watermarks/IMG_0706.JPG	Capo Dipartimento VVF con il Capo del Corpo e il Responsabile dell'emergenza durante una Videoconferenza al Centro Operativo Nazionale.	2022-01-17 17:11:53.22685+01	2022-01-17 17:11:53.226862+01	5	15	Dirigenti Nazionali
393	2022-01-17 01:00:00+01	galleria/originale/IMG_9715_v1.jpg	galleria/thumbails/IMG_9715_v1.jpeg	galleria/watermarks/IMG_9715_v1.jpg	Estensione massima per risolvere un'intervento con l'autoscala sulla cupola	2022-01-17 18:44:27.447652+01	2022-01-17 18:44:27.447681+01	17	15	Estensione massima
404	2022-01-18 01:00:00+01	galleria/originale/IMG_2458.JPG			Il lavoro dei cinofili con il proprio cane durante un'esecitazione di ricerca persona.	2022-01-18 10:32:57.127286+01	2022-01-18 10:32:57.127301+01	16	15	Esercitazione gruppo cinofili liguria
283	2022-01-14 01:00:00+01	galleria/originale/DSC_0283.JPG	galleria/thumbails/DSC_0283.jpeg	galleria/watermarks/DSC_0283.JPG	Interventi squadre GOS.	2022-01-14 17:29:32.963608+01	2022-01-14 17:29:32.96362+01	2	15	Movimento terra
284	2022-01-14 01:00:00+01	galleria/originale/DSC_0289.JPG	galleria/thumbails/DSC_0289.jpeg	galleria/watermarks/DSC_0289.JPG	Interventi squadre GOS.	2022-01-14 17:29:34.269624+01	2022-01-14 17:29:34.269636+01	2	15	Movimento terra
285	2022-01-14 01:00:00+01	galleria/originale/DSC00323.JPG	galleria/thumbails/DSC00323.jpeg	galleria/watermarks/DSC00323.JPG	Interventi squadre GOS.	2022-01-14 17:29:35.381991+01	2022-01-14 17:29:35.382002+01	2	15	Movimento terra
286	2022-01-14 01:00:00+01	galleria/originale/DSC00328.JPG	galleria/thumbails/DSC00328.jpeg	galleria/watermarks/DSC00328.JPG	Interventi squadre GOS.	2022-01-14 17:29:36.724809+01	2022-01-14 17:29:36.724821+01	2	15	Movimento terra
287	2022-01-14 01:00:00+01	galleria/originale/DSC00330.JPG	galleria/thumbails/DSC00330.jpeg	galleria/watermarks/DSC00330.JPG	Interventi squadre GOS.	2022-01-14 17:29:37.963657+01	2022-01-14 17:29:37.963669+01	2	15	Movimento terra
288	2022-01-14 01:00:00+01	galleria/originale/DSC00335.JPG	galleria/thumbails/DSC00335.jpeg	galleria/watermarks/DSC00335.JPG	Interventi squadre GOS.	2022-01-14 17:29:39.132094+01	2022-01-14 17:29:39.132106+01	2	15	Movimento terra
289	2022-01-14 01:00:00+01	galleria/originale/DSC00340.JPG	galleria/thumbails/DSC00340.jpeg	galleria/watermarks/DSC00340.JPG	Interventi squadre GOS.	2022-01-14 17:29:40.371787+01	2022-01-14 17:29:40.371803+01	2	15	Movimento terra
290	2022-01-14 01:00:00+01	galleria/originale/DSC00347.JPG	galleria/thumbails/DSC00347.jpeg	galleria/watermarks/DSC00347.JPG	Interventi squadre GOS.	2022-01-14 17:29:41.591217+01	2022-01-14 17:29:41.591229+01	2	15	Movimento terra
291	2022-01-14 01:00:00+01	galleria/originale/DSC00355_1.jpg	galleria/thumbails/DSC00355_1.jpeg	galleria/watermarks/DSC00355_1.jpg	Interventi squadre GOS.	2022-01-14 17:29:42.72327+01	2022-01-14 17:29:42.723282+01	2	15	Movimento terra
292	2022-01-14 01:00:00+01	galleria/originale/IMG_20191025_154900.jpg	galleria/thumbails/IMG_20191025_154900.jpeg	galleria/watermarks/IMG_20191025_154900.jpg	Interventi squadre GOS.	2022-01-14 17:29:43.877376+01	2022-01-14 17:29:43.877389+01	2	15	Movimento terra
327	2022-01-15 01:00:00+01	galleria/originale/DSC_9175.jpg	galleria/thumbails/DSC_9175.jpeg	galleria/watermarks/DSC_9175.jpg	Manovre di montaggio scala italiana al castello durante il corso allievi VVF presso le SCA.	2022-01-15 17:23:03.564256+01	2022-01-15 17:23:03.564268+01	8	15	Corso allievi VVF
328	2022-01-15 01:00:00+01	galleria/originale/DSC_9178.jpg	galleria/thumbails/DSC_9178.jpeg	galleria/watermarks/DSC_9178.jpg	Manovre di montaggio scala italiana al castello durante il corso allievi VVF presso le SCA.	2022-01-15 17:23:04.108198+01	2022-01-15 17:23:04.10821+01	8	15	Corso allievi VVF
329	2022-01-15 01:00:00+01	galleria/originale/DSC_9179.jpg	galleria/thumbails/DSC_9179.jpeg	galleria/watermarks/DSC_9179.jpg	Manovre di montaggio scala italiana al castello durante il corso allievi VVF presso le SCA.	2022-01-15 17:23:04.898409+01	2022-01-15 17:23:04.898421+01	8	15	Corso allievi VVF
330	2022-01-15 01:00:00+01	galleria/originale/DSC_9184.jpg	galleria/thumbails/DSC_9184.jpeg	galleria/watermarks/DSC_9184.jpg	Manovre di montaggio scala italiana al castello durante il corso allievi VVF presso le SCA.	2022-01-15 17:23:05.515248+01	2022-01-15 17:23:05.51526+01	8	15	Corso allievi VVF
331	2022-01-15 01:00:00+01	galleria/originale/DSC_9186.jpg	galleria/thumbails/DSC_9186.jpeg	galleria/watermarks/DSC_9186.jpg	Manovre di montaggio scala italiana al castello durante il corso allievi VVF presso le SCA.	2022-01-15 17:23:06.078139+01	2022-01-15 17:23:06.078151+01	8	15	Corso allievi VVF
332	2022-01-15 01:00:00+01	galleria/originale/DSC_9188.jpg	galleria/thumbails/DSC_9188.jpeg	galleria/watermarks/DSC_9188.jpg	Manovre di montaggio scala italiana al castello durante il corso allievi VVF presso le SCA.	2022-01-15 17:23:07.120021+01	2022-01-15 17:23:07.120033+01	8	15	Corso allievi VVF
333	2022-01-15 01:00:00+01	galleria/originale/DSC_9189.jpg	galleria/thumbails/DSC_9189.jpeg	galleria/watermarks/DSC_9189.jpg	Manovre di montaggio scala italiana al castello durante il corso allievi VVF presso le SCA.	2022-01-15 17:23:07.996641+01	2022-01-15 17:23:07.996653+01	8	15	Corso allievi VVF
334	2022-01-15 01:00:00+01	galleria/originale/DSC_9190.jpg	galleria/thumbails/DSC_9190.jpeg	galleria/watermarks/DSC_9190.jpg	Manovre di montaggio scala italiana al castello durante il corso allievi VVF presso le SCA.	2022-01-15 17:23:08.453971+01	2022-01-15 17:23:08.453986+01	8	15	Corso allievi VVF
335	2022-01-15 01:00:00+01	galleria/originale/DSC_9195.jpg	galleria/thumbails/DSC_9195.jpeg	galleria/watermarks/DSC_9195.jpg	Manovre di montaggio scala italiana al castello durante il corso allievi VVF presso le SCA.	2022-01-15 17:23:08.745467+01	2022-01-15 17:23:08.745478+01	8	15	Corso allievi VVF
336	2022-01-15 01:00:00+01	galleria/originale/DSC_9203.jpg	galleria/thumbails/DSC_9203.jpeg	galleria/watermarks/DSC_9203.jpg	Manovre di montaggio scala italiana al castello durante il corso allievi VVF presso le SCA.	2022-01-15 17:23:09.711986+01	2022-01-15 17:23:09.711998+01	8	15	Corso allievi VVF
337	2022-01-15 01:00:00+01	galleria/originale/DSC_9209.jpg	galleria/thumbails/DSC_9209.jpeg	galleria/watermarks/DSC_9209.jpg	Manovre di montaggio scala italiana al castello durante il corso allievi VVF presso le SCA.	2022-01-15 17:23:09.951981+01	2022-01-15 17:23:09.951993+01	8	15	Corso allievi VVF
338	2022-01-15 01:00:00+01	galleria/originale/DSC_9226.jpg	galleria/thumbails/DSC_9226.jpeg	galleria/watermarks/DSC_9226.jpg	Manovre di montaggio scala italiana al castello durante il corso allievi VVF presso le SCA.	2022-01-15 17:23:10.380742+01	2022-01-15 17:23:10.380754+01	8	15	Corso allievi VVF
339	2022-01-15 01:00:00+01	galleria/originale/DSC_9231.jpg	galleria/thumbails/DSC_9231.jpeg	galleria/watermarks/DSC_9231.jpg	Manovre di montaggio scala italiana al castello durante il corso allievi VVF presso le SCA.	2022-01-15 17:23:10.886791+01	2022-01-15 17:23:10.886803+01	8	15	Corso allievi VVF
340	2022-01-15 01:00:00+01	galleria/originale/DSC_9233.jpg	galleria/thumbails/DSC_9233.jpeg	galleria/watermarks/DSC_9233.jpg	Manovre di montaggio scala italiana al castello durante il corso allievi VVF presso le SCA.	2022-01-15 17:23:11.364814+01	2022-01-15 17:23:11.364825+01	8	15	Corso allievi VVF
341	2022-01-15 01:00:00+01	galleria/originale/DSC_9238.jpg	galleria/thumbails/DSC_9238.jpeg	galleria/watermarks/DSC_9238.jpg	Manovre di montaggio scala italiana al castello durante il corso allievi VVF presso le SCA.	2022-01-15 17:23:11.921111+01	2022-01-15 17:23:11.921123+01	8	15	Corso allievi VVF
342	2022-01-15 01:00:00+01	galleria/originale/DSC_9245.jpg	galleria/thumbails/DSC_9245.jpeg	galleria/watermarks/DSC_9245.jpg	Manovre di montaggio scala italiana al castello durante il corso allievi VVF presso le SCA.	2022-01-15 17:23:12.143803+01	2022-01-15 17:23:12.143815+01	8	15	Corso allievi VVF
343	2022-01-15 01:00:00+01	galleria/originale/DSC_9246.jpg	galleria/thumbails/DSC_9246.jpeg	galleria/watermarks/DSC_9246.jpg	Manovre di montaggio scala italiana al castello durante il corso allievi VVF presso le SCA.	2022-01-15 17:23:12.504042+01	2022-01-15 17:23:12.504055+01	8	15	Corso allievi VVF
344	2022-01-15 01:00:00+01	galleria/originale/DSC_9254.jpg	galleria/thumbails/DSC_9254.jpeg	galleria/watermarks/DSC_9254.jpg	Manovre di montaggio scala italiana al castello durante il corso allievi VVF presso le SCA.	2022-01-15 17:23:12.968146+01	2022-01-15 17:23:12.968158+01	8	15	Corso allievi VVF
345	2022-01-15 01:00:00+01	galleria/originale/DSC_9259.jpg	galleria/thumbails/DSC_9259.jpeg	galleria/watermarks/DSC_9259.jpg	Manovre di montaggio scala italiana al castello durante il corso allievi VVF presso le SCA.	2022-01-15 17:23:13.084908+01	2022-01-15 17:23:13.08492+01	8	15	Corso allievi VVF
354	2022-01-16 01:00:00+01	galleria/originale/04032013-DSC_0313.jpg	galleria/thumbails/04032013-DSC_0313.jpeg	galleria/watermarks/04032013-DSC_0313.jpg	Spegnimento fiamme di un incendio fabbrica con ausilio autoscala.	2022-01-16 17:25:57.091202+01	2022-01-16 17:25:57.091221+01	17	15	Incendio Fabbrica
293	2022-01-15 01:00:00+01	galleria/originale/DSC00095	galleria/thumbails/DSC00095.jpeg	galleria/watermarks/DSC00095	Il lavoro degli USAR VVF nelle ricerche sotto le macerie.	2022-01-15 13:54:49.241656+01	2022-01-15 13:54:49.241673+01	1	15	USAR VVF
294	2022-01-15 01:00:00+01	galleria/originale/IMG_1057	galleria/thumbails/IMG_1057.jpeg	galleria/watermarks/IMG_1057	Il lavoro degli USAR VVF nelle ricerche sotto le macerie.	2022-01-15 13:54:49.394661+01	2022-01-15 13:54:49.394673+01	1	15	USAR VVF
349	2022-01-16 01:00:00+01	galleria/originale/IMG_20210215_214904-02.jpeg	galleria/thumbails/IMG_20210215_214904-02.jpeg	galleria/watermarks/IMG_20210215_214904-02.jpeg	I mezzi dei vigili del fuoco hanno parecchi scomparti nei quali ci sono attrezzature fondamentali per gli interventi, bisogna controllare il caricamento tutti i giorni.	2022-01-16 17:12:51.348352+01	2022-01-16 17:12:51.348364+01	10	15	Caricamento Mezzi
350	2022-01-16 01:00:00+01	galleria/originale/PSX_20201019_102007.jpg	galleria/thumbails/PSX_20201019_102007.jpeg	galleria/watermarks/PSX_20201019_102007.jpg	I mezzi dei vigili del fuoco hanno parecchi scomparti nei quali ci sono attrezzature fondamentali per gli interventi, bisogna controllare il caricamento tutti i giorni.	2022-01-16 17:12:52.293907+01	2022-01-16 17:12:52.293919+01	10	15	Caricamento Mezzi
295	2022-01-15 01:00:00+01	galleria/originale/IMG_1058	galleria/thumbails/IMG_1058.jpeg	galleria/watermarks/IMG_1058	Il lavoro degli USAR VVF nelle ricerche sotto le macerie.	2022-01-15 13:54:49.624785+01	2022-01-15 13:54:49.624798+01	1	15	USAR VVF
296	2022-01-15 01:00:00+01	galleria/originale/IMG_7039.JPG	galleria/thumbails/IMG_7039.jpeg	galleria/watermarks/IMG_7039.JPG	Il lavoro degli USAR VVF nelle ricerche sotto le macerie.	2022-01-15 13:54:49.748565+01	2022-01-15 13:54:49.748577+01	1	15	USAR VVF
355	2022-01-16 01:00:00+01	galleria/originale/12092015-_DSC3056.jpg	galleria/thumbails/12092015-_DSC3056.jpeg	galleria/watermarks/12092015-_DSC3056.jpg	Fasi di smantellamento e bonifica di un incendio tetto.	2022-01-16 17:28:33.279176+01	2022-01-16 17:28:33.279188+01	17	15	Incendio tetto
297	2022-01-15 01:00:00+01	galleria/originale/IMG_7056.JPG	galleria/thumbails/IMG_7056.jpeg	galleria/watermarks/IMG_7056.JPG	Il lavoro degli USAR VVF nelle ricerche sotto le macerie.	2022-01-15 13:54:50.017093+01	2022-01-15 13:54:50.017105+01	1	15	USAR VVF
299	2022-01-15 01:00:00+01	galleria/originale/IMG_7832.JPG	galleria/thumbails/IMG_7832.jpeg	galleria/watermarks/IMG_7832.JPG	Il lavoro degli USAR VVF nelle ricerche sotto le macerie.	2022-01-15 13:54:50.410007+01	2022-01-15 13:54:50.410019+01	1	15	USAR VVF
360	2022-01-16 01:00:00+01	galleria/originale/PSX_20201205_010233-02-01.jpeg	galleria/thumbails/PSX_20201205_010233-02-01.jpeg	galleria/watermarks/PSX_20201205_010233-02-01.jpeg	Mezzi VVF in autorimessa Caserma VVF.	2022-01-16 17:38:11.776003+01	2022-01-16 17:38:11.776019+01	11	15	Mezzi VVF
298	2022-01-15 01:00:00+01	galleria/originale/IMG_7657.JPG	galleria/thumbails/IMG_7657.jpeg	galleria/watermarks/IMG_7657.JPG	Il lavoro degli USAR VVF nelle ricerche sotto le macerie.	2022-01-15 13:54:50.102355+01	2022-01-15 13:56:25.5706+01	1	15	USAR VVF
346	2022-01-16 01:00:00+01	galleria/originale/4_5771891478330608132-01_0E0OUZX.jpeg	galleria/thumbails/4_5771891478330608132-01_0E0OUZX.jpeg	galleria/watermarks/4_5771891478330608132-01_0E0OUZX.jpeg	I mezzi dei vigili del fuoco hanno parecchi scomparti nei quali ci sono attrezzature fondamentali per gli interventi, bisogna controllare il caricamento tutti i giorni.	2022-01-16 17:12:45.509561+01	2022-01-16 17:12:45.509579+01	10	15	Caricamento Mezzi
347	2022-01-16 01:00:00+01	galleria/originale/IMG_20201019_101433-01.jpeg	galleria/thumbails/IMG_20201019_101433-01.jpeg	galleria/watermarks/IMG_20201019_101433-01.jpeg	I mezzi dei vigili del fuoco hanno parecchi scomparti nei quali ci sono attrezzature fondamentali per gli interventi, bisogna controllare il caricamento tutti i giorni.	2022-01-16 17:12:48.058978+01	2022-01-16 17:12:48.05899+01	10	15	Caricamento Mezzi
348	2022-01-16 01:00:00+01	galleria/originale/IMG_20210215_214904-01.jpeg	galleria/thumbails/IMG_20210215_214904-01.jpeg	galleria/watermarks/IMG_20210215_214904-01.jpeg	I mezzi dei vigili del fuoco hanno parecchi scomparti nei quali ci sono attrezzature fondamentali per gli interventi, bisogna controllare il caricamento tutti i giorni.	2022-01-16 17:12:49.869614+01	2022-01-16 17:12:49.869626+01	10	15	Caricamento Mezzi
363	2022-01-16 01:00:00+01	galleria/originale/IMG_20191214_135815.jpeg	galleria/thumbails/IMG_20191214_135815.jpeg	galleria/watermarks/IMG_20191214_135815.jpeg	Trasferimento Sommozzatore con gommone su lago.	2022-01-16 17:42:49.033267+01	2022-01-16 17:42:49.033285+01	7	15	Sommozzatore su Gommone
366	2022-01-16 01:00:00+01	galleria/originale/PSX_20210217_135350.jpg	galleria/thumbails/PSX_20210217_135350.jpeg	galleria/watermarks/PSX_20210217_135350.jpg	Prova lancio acqua da lancia montata direttamente su cestello autoscala.	2022-01-16 17:49:36.705528+01	2022-01-16 17:49:36.705546+01	11	15	Manovra con autoscala
369	2022-01-17 01:00:00+01	galleria/originale/IMG_8398.jpg	galleria/thumbails/IMG_8398.jpeg	galleria/watermarks/IMG_8398.jpg	Cani da ricerca impegnati con i cinofili in intervento di soccorso.	2022-01-17 13:24:41.641155+01	2022-01-17 13:24:41.641171+01	16	15	Cinofili VVF
370	2022-01-17 01:00:00+01	galleria/originale/_DSC5598.JPG	galleria/thumbails/_DSC5598.jpeg	galleria/watermarks/_DSC5598.JPG	Cani da ricerca impegnati con i cinofili in intervento di soccorso.	2022-01-17 13:24:41.784418+01	2022-01-17 13:24:41.784429+01	16	15	Cinofili VVF
371	2022-01-17 01:00:00+01	galleria/originale/IMG_8359.jpg	galleria/thumbails/IMG_8359.jpeg	galleria/watermarks/IMG_8359.jpg	Cani da ricerca impegnati con i cinofili in intervento di soccorso.	2022-01-17 13:24:41.933256+01	2022-01-17 13:24:41.933268+01	16	15	Cinofili VVF
374	2022-01-17 01:00:00+01	galleria/originale/15032017-_DSC0479.jpg	galleria/thumbails/15032017-_DSC0479.jpeg	galleria/watermarks/15032017-_DSC0479.jpg	Il lavoro dei TAS dei VVF Topografia applicata al soccorso per delimitare o bonificare zone di ricerca in caso di persone scomparse.	2022-01-17 16:11:38.364009+01	2022-01-17 16:11:38.364026+01	14	15	Topografia applicata al soccorso
383	2022-01-17 01:00:00+01	galleria/originale/IMG_0652.JPG	galleria/thumbails/IMG_0652.jpeg	galleria/watermarks/IMG_0652.JPG	Il CON durante l'esercitazione Nazionale "Bottone Rosso"	2022-01-17 16:55:32.697037+01	2022-01-17 16:55:32.697053+01	8	15	BOTTONE ROSSO
384	2022-01-17 01:00:00+01	galleria/originale/IMG_0614.JPG	galleria/thumbails/IMG_0614.jpeg	galleria/watermarks/IMG_0614.JPG	Il CON durante l'esercitazione Nazionale "Bottone Rosso"	2022-01-17 16:55:33.281638+01	2022-01-17 16:55:33.28165+01	8	15	BOTTONE ROSSO
385	2022-01-17 01:00:00+01	galleria/originale/IMG_0565.JPG	galleria/thumbails/IMG_0565.jpeg	galleria/watermarks/IMG_0565.JPG	Il CON durante l'esercitazione Nazionale "Bottone Rosso"	2022-01-17 16:55:33.814429+01	2022-01-17 16:55:33.814441+01	8	15	BOTTONE ROSSO
386	2022-01-17 01:00:00+01	galleria/originale/IMG_0561.JPG	galleria/thumbails/IMG_0561.jpeg	galleria/watermarks/IMG_0561.JPG	Il CON durante l'esercitazione Nazionale "Bottone Rosso"	2022-01-17 16:55:34.36515+01	2022-01-17 16:55:34.365162+01	8	15	BOTTONE ROSSO
390	2022-01-17 01:00:00+01	galleria/originale/IMG_0094.JPG	galleria/thumbails/IMG_0094.jpeg	galleria/watermarks/IMG_0094.JPG	Carro regia durante l'esercitazione nazionale alle SFO per le nuove tecnologie.	2022-01-17 17:18:49.319118+01	2022-01-17 17:18:49.319135+01	8	15	COEM
394	2022-01-18 01:00:00+01	galleria/originale/IMG_1303.JPG	galleria/thumbails/IMG_1303.jpeg	galleria/watermarks/IMG_1303.JPG	La motobarca VVF mezzo indispensabili per i distaccamenti nautici per effettuare interventi in mare aperto.	2022-01-18 07:55:45.409614+01	2022-01-18 07:55:45.409631+01	13	15	Motobarca VVF
405	2022-01-18 01:00:00+01	galleria/originale/IMG_2529.JPG			Il lavoro dei cinofili con il proprio cane durante un'esecitazione di ricerca persona.	2022-01-18 10:32:58.957365+01	2022-01-18 10:32:58.957381+01	16	15	Esercitazione gruppo cinofili liguria
406	2022-01-18 01:00:00+01	galleria/originale/IMG_2538.JPG			Il lavoro dei cinofili con il proprio cane durante un'esecitazione di ricerca persona.	2022-01-18 10:33:01.66636+01	2022-01-18 10:33:01.666372+01	16	15	Esercitazione gruppo cinofili liguria
300	2022-01-15 01:00:00+01	galleria/originale/36.JPG	galleria/thumbails/36.jpeg	galleria/watermarks/36.JPG	Le manovre dei SAF VVF per soccorso o recupero.	2022-01-15 14:10:21.240292+01	2022-01-15 14:10:21.240303+01	4	15	SAF VVF
301	2022-01-15 01:00:00+01	galleria/originale/DSC_2063.JPG	galleria/thumbails/DSC_2063.jpeg	galleria/watermarks/DSC_2063.JPG	Le manovre dei SAF VVF per soccorso o recupero.	2022-01-15 14:10:21.591652+01	2022-01-15 14:10:21.591667+01	4	15	SAF VVF
302	2022-01-15 01:00:00+01	galleria/originale/DSC_8355.JPG	galleria/thumbails/DSC_8355.jpeg	galleria/watermarks/DSC_8355.JPG	Le manovre dei SAF VVF per soccorso o recupero.	2022-01-15 14:10:21.839392+01	2022-01-15 14:10:21.839404+01	4	15	SAF VVF
303	2022-01-15 01:00:00+01	galleria/originale/IMG_3255.jpg	galleria/thumbails/IMG_3255.jpeg	galleria/watermarks/IMG_3255.jpg	Le manovre dei SAF VVF per soccorso o recupero.	2022-01-15 14:10:22.060615+01	2022-01-15 14:10:22.060628+01	4	15	SAF VVF
304	2022-01-15 01:00:00+01	galleria/originale/IMG_3276.jpg	galleria/thumbails/IMG_3276.jpeg	galleria/watermarks/IMG_3276.jpg	Le manovre dei SAF VVF per soccorso o recupero.	2022-01-15 14:10:22.265274+01	2022-01-15 14:10:22.265288+01	4	15	SAF VVF
305	2022-01-15 01:00:00+01	galleria/originale/IMG_6789.jpg	galleria/thumbails/IMG_6789.jpeg	galleria/watermarks/IMG_6789.jpg	Le manovre dei SAF VVF per soccorso o recupero.	2022-01-15 14:10:22.456962+01	2022-01-15 14:10:22.456973+01	4	15	SAF VVF
306	2022-01-15 01:00:00+01	galleria/originale/IMG_6790.jpg	galleria/thumbails/IMG_6790.jpeg	galleria/watermarks/IMG_6790.jpg	Le manovre dei SAF VVF per soccorso o recupero.	2022-01-15 14:10:22.665595+01	2022-01-15 14:10:22.665607+01	4	15	SAF VVF
307	2022-01-15 01:00:00+01	galleria/originale/IMG_6802.jpg	galleria/thumbails/IMG_6802.jpeg	galleria/watermarks/IMG_6802.jpg	Le manovre dei SAF VVF per soccorso o recupero.	2022-01-15 14:10:22.810937+01	2022-01-15 14:10:22.810953+01	4	15	SAF VVF
308	2022-01-15 01:00:00+01	galleria/originale/IMG_7297.jpg	galleria/thumbails/IMG_7297.jpeg	galleria/watermarks/IMG_7297.jpg	Le manovre dei SAF VVF per soccorso o recupero.	2022-01-15 14:10:23.010694+01	2022-01-15 14:10:23.010706+01	4	15	SAF VVF
309	2022-01-15 01:00:00+01	galleria/originale/IMG-20170902-WA0010.jpg	galleria/thumbails/IMG-20170902-WA0010.jpeg	galleria/watermarks/IMG-20170902-WA0010.jpg	Le manovre dei SAF VVF per soccorso o recupero.	2022-01-15 14:10:23.12586+01	2022-01-15 14:10:23.125872+01	4	15	SAF VVF
376	2022-01-17 01:00:00+01	galleria/originale/mareggiata_giugno_6.JPG	galleria/thumbails/mareggiata_giugno_6.jpeg	galleria/watermarks/mareggiata_giugno_6.JPG	Le motobarche VVF mezzi usati dai nautici per effettuare interventi in mare aperto.	2022-01-17 16:15:14.703946+01	2022-01-17 16:15:14.703966+01	13	15	Imbarcazione VVF
310	2022-01-15 01:00:00+01	galleria/originale/vlcsnap-2020-03-04-21h51m53s030.png	galleria/thumbails/vlcsnap-2020-03-04-21h51m53s030.jpeg	galleria/watermarks/vlcsnap-2020-03-04-21h51m53s030.png	Le manovre dei SAF VVF per soccorso o recupero.	2022-01-15 14:10:23.464499+01	2022-01-15 14:11:30.911098+01	4	15	SAF VVF
387	2022-01-17 01:00:00+01	galleria/originale/IMG_0651.JPG	galleria/thumbails/IMG_0651.jpeg	galleria/watermarks/IMG_0651.JPG	Il logo del Centro operativo nazionale.	2022-01-17 17:03:58.577373+01	2022-01-17 17:03:58.577391+01	5	15	CON
311	2022-01-15 01:00:00+01	galleria/originale/vlcsnap-2020-03-04-21h52m34s044.png	galleria/thumbails/vlcsnap-2020-03-04-21h52m34s044.jpeg	galleria/watermarks/vlcsnap-2020-03-04-21h52m34s044.png	Le manovre dei SAF VVF per soccorso o recupero.	2022-01-15 14:10:23.63914+01	2022-01-15 14:12:03.762405+01	4	15	SAF VVF
351	2022-01-16 01:00:00+01	galleria/originale/4_5771891478330608276-01.jpeg	galleria/thumbails/4_5771891478330608276-01.jpeg	galleria/watermarks/4_5771891478330608276-01.jpeg	Operazioni di spegnimento e bonifica incendio boschivo	2022-01-16 17:16:55.675405+01	2022-01-16 17:16:55.675435+01	17	15	Incendio boschivo
356	2022-01-16 01:00:00+01	galleria/originale/17022012-11.jpg	galleria/thumbails/17022012-11.jpeg	galleria/watermarks/17022012-11.jpg	La fresa VVF al lavoro per liberare una strada dalla neve.	2022-01-16 17:31:08.188072+01	2022-01-16 17:31:08.188091+01	17	15	Emergenza neve
359	2022-01-16 01:00:00+01	galleria/originale/DSC00523-01.jpeg	galleria/thumbails/DSC00523-01.jpeg	galleria/watermarks/DSC00523-01.jpeg	Mezzi VVF in autorimessa Caserma VVF.	2022-01-16 17:38:11.411341+01	2022-01-16 17:38:11.411359+01	11	15	Mezzi VVF
364	2022-01-16 01:00:00+01	galleria/originale/PSX_20201004_165008.jpg	galleria/thumbails/PSX_20201004_165008.jpeg	galleria/watermarks/PSX_20201004_165008.jpg	Dettaglio di un GriGri attrezzo utilizzato per le manovre SAF	2022-01-16 17:44:57.244221+01	2022-01-16 17:44:57.244239+01	10	15	GriGri
367	2022-01-16 01:00:00+01	galleria/originale/screenshot_2021-02-20-00-15-02.png	galleria/thumbails/screenshot_2021-02-20-00-15-02.jpeg	galleria/watermarks/screenshot_2021-02-20-00-15-02.png	Manovra di salvataggio con corda durante una esercitazione dei soccorritori acquatici Vigili del fuoco.	2022-01-16 17:51:59.896322+01	2022-01-16 17:51:59.896339+01	8	15	Addestramento SA
372	2022-01-17 01:00:00+01	galleria/originale/02022017-IMG_6316.jpg	galleria/thumbails/02022017-IMG_6316.jpeg	galleria/watermarks/02022017-IMG_6316.jpg	Il lavoro dei puntellatori per stabilizzare strutture lesionate o inagibili.	2022-01-17 16:09:04.273503+01	2022-01-17 16:09:04.273519+01	6	15	Opere di stabilizzazione
373	2022-01-17 01:00:00+01	galleria/originale/02022017-IMG_6312.jpg	galleria/thumbails/02022017-IMG_6312.jpeg	galleria/watermarks/02022017-IMG_6312.jpg	Il lavoro dei puntellatori per stabilizzare strutture lesionate o inagibili.	2022-01-17 16:09:06.003333+01	2022-01-17 16:09:06.003348+01	6	15	Opere di stabilizzazione
391	2022-01-17 01:00:00+01	galleria/originale/IMG_0138.JPG	galleria/thumbails/IMG_0138.jpeg	galleria/watermarks/IMG_0138.JPG	Riflessa in una pozza d'acqua l'autoscala VVF	2022-01-17 18:39:56.818763+01	2022-01-17 18:39:56.81878+01	11	15	Riflessi
392	2022-01-17 01:00:00+01	galleria/originale/IMG_0139.JPG	galleria/thumbails/IMG_0139.jpeg	galleria/watermarks/IMG_0139.JPG	Riflessa in una pozza d'acqua l'autoscala VVF	2022-01-17 18:39:56.954513+01	2022-01-17 18:39:56.954525+01	11	15	Riflessi
397	2022-01-18 01:00:00+01	galleria/originale/IMG_1781.JPG	galleria/thumbails/IMG_1781.JPG	galleria/watermarks/IMG_1781.JPG	Il lavoro dei cinofili con il proprio cane durante un'esecitazione di ricerca persona.	2022-01-18 10:32:42.039853+01	2022-01-18 10:32:42.039865+01	16	15	Esercitazione gruppo cinofili liguria
398	2022-01-18 01:00:00+01	galleria/originale/IMG_1784.JPG	galleria/thumbails/IMG_1784.JPG	galleria/watermarks/IMG_1784.JPG	Il lavoro dei cinofili con il proprio cane durante un'esecitazione di ricerca persona.	2022-01-18 10:32:44.134209+01	2022-01-18 10:32:44.134221+01	16	15	Esercitazione gruppo cinofili liguria
399	2022-01-18 01:00:00+01	galleria/originale/IMG_1831.JPG	galleria/thumbails/IMG_1831.JPG	galleria/watermarks/IMG_1831.JPG	Il lavoro dei cinofili con il proprio cane durante un'esecitazione di ricerca persona.	2022-01-18 10:32:45.535495+01	2022-01-18 10:32:45.535507+01	16	15	Esercitazione gruppo cinofili liguria
400	2022-01-18 01:00:00+01	galleria/originale/IMG_1832.JPG	galleria/thumbails/IMG_1832.JPG	galleria/watermarks/IMG_1832.JPG	Il lavoro dei cinofili con il proprio cane durante un'esecitazione di ricerca persona.	2022-01-18 10:32:47.209357+01	2022-01-18 10:32:47.209369+01	16	15	Esercitazione gruppo cinofili liguria
402	2022-01-18 01:00:00+01	galleria/originale/IMG_1845.JPG	galleria/thumbails/IMG_1845.JPG	galleria/watermarks/IMG_1845.JPG	Il lavoro dei cinofili con il proprio cane durante un'esecitazione di ricerca persona.	2022-01-18 10:32:52.342133+01	2022-01-18 10:32:52.342145+01	16	15	Esercitazione gruppo cinofili liguria
403	2022-01-18 01:00:00+01	galleria/originale/IMG_1853.JPG	galleria/thumbails/IMG_1853.JPG	galleria/watermarks/IMG_1853.JPG	Il lavoro dei cinofili con il proprio cane durante un'esecitazione di ricerca persona.	2022-01-18 10:32:54.681734+01	2022-01-18 10:32:54.681746+01	16	15	Esercitazione gruppo cinofili liguria
395	2022-01-18 01:00:00+01	galleria/originale/IMG_1712.JPG	galleria/thumbails/IMG_1712.JPG	galleria/watermarks/IMG_1712.JPG	Il lavoro dei cinofili con il proprio cane durante un'esecitazione di ricerca persona.	2022-01-18 10:32:36.957252+01	2022-01-18 10:32:36.95727+01	16	15	Esercitazione gruppo cinofili liguria
396	2022-01-18 01:00:00+01	galleria/originale/IMG_1777.JPG	galleria/thumbails/IMG_1777.JPG	galleria/watermarks/IMG_1777.JPG	Il lavoro dei cinofili con il proprio cane durante un'esecitazione di ricerca persona.	2022-01-18 10:32:39.715942+01	2022-01-18 10:32:39.715954+01	16	15	Esercitazione gruppo cinofili liguria
401	2022-01-18 01:00:00+01	galleria/originale/IMG_1839.JPG	galleria/thumbails/IMG_1839.JPG	galleria/watermarks/IMG_1839.JPG	Il lavoro dei cinofili con il proprio cane durante un'esecitazione di ricerca persona.	2022-01-18 10:32:49.710772+01	2022-01-18 10:32:49.710784+01	16	15	Esercitazione gruppo cinofili liguria
407	2022-01-18 01:00:00+01	galleria/originale/IMG_2579.JPG	galleria/thumbails/IMG_2579.JPG	galleria/watermarks/IMG_2579.JPG	Il lavoro dei cinofili con il proprio cane durante un'esecitazione di ricerca persona.	2022-01-18 10:33:04.539443+01	2022-01-18 10:33:04.539455+01	16	15	Esercitazione gruppo cinofili liguria
\.


--
-- Name: watermarks_foto_id_seq; Type: SEQUENCE SET; Schema: public; Owner: vvf
--

SELECT pg_catalog.setval('public.watermarks_foto_id_seq', 407, true);


--
-- Name: watermarks_foto watermarks_foto_pkey; Type: CONSTRAINT; Schema: public; Owner: vvf
--

ALTER TABLE ONLY public.watermarks_foto
    ADD CONSTRAINT watermarks_foto_pkey PRIMARY KEY (id);


--
-- Name: watermarks_foto_category_id_64ded64d; Type: INDEX; Schema: public; Owner: vvf
--

CREATE INDEX watermarks_foto_category_id_64ded64d ON public.watermarks_foto USING btree (category_id);


--
-- Name: watermarks_foto_user_id_cb25f6b0; Type: INDEX; Schema: public; Owner: vvf
--

CREATE INDEX watermarks_foto_user_id_cb25f6b0 ON public.watermarks_foto USING btree (user_id);


--
-- Name: watermarks_foto watermarks_foto_category_id_64ded64d_fk_watermarks_category_id; Type: FK CONSTRAINT; Schema: public; Owner: vvf
--

ALTER TABLE ONLY public.watermarks_foto
    ADD CONSTRAINT watermarks_foto_category_id_64ded64d_fk_watermarks_category_id FOREIGN KEY (category_id) REFERENCES public.watermarks_category(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: watermarks_foto watermarks_foto_user_id_cb25f6b0_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: vvf
--

ALTER TABLE ONLY public.watermarks_foto
    ADD CONSTRAINT watermarks_foto_user_id_cb25f6b0_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- PostgreSQL database dump complete
--

