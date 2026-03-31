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
-- Name: watermarks_category; Type: TABLE; Schema: public; Owner: vvf
--

CREATE TABLE public.watermarks_category (
    id integer NOT NULL,
    name character varying(100) NOT NULL,
    user_id integer
);


ALTER TABLE public.watermarks_category OWNER TO vvf;

--
-- Name: watermarks_category_id_seq; Type: SEQUENCE; Schema: public; Owner: vvf
--

CREATE SEQUENCE public.watermarks_category_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.watermarks_category_id_seq OWNER TO vvf;

--
-- Name: watermarks_category_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vvf
--

ALTER SEQUENCE public.watermarks_category_id_seq OWNED BY public.watermarks_category.id;


--
-- Name: watermarks_category id; Type: DEFAULT; Schema: public; Owner: vvf
--

ALTER TABLE ONLY public.watermarks_category ALTER COLUMN id SET DEFAULT nextval('public.watermarks_category_id_seq'::regclass);


--
-- Data for Name: watermarks_category; Type: TABLE DATA; Schema: public; Owner: vvf
--

COPY public.watermarks_category (id, name, user_id) FROM stdin;
1	USAR	1
2	GOS	1
3	ELICOTERRISTI	1
4	SAF	1
5	ISTITUZIONALE	\N
6	PUNTELLATORI	1
7	SOMMOZZATORI	1
8	ESERCITAZIONE	1
9	CONCORDIA	\N
10	ATTREZZATURE	7
11	MEZZI	1
12	AEROPORTUALI	1
13	NAUTICI	1
14	TAS	1
15	SAPR	1
16	CINOFILI	\N
17	SOCCORSI	1
18	NBCR	1
19	CON	1
\.


--
-- Name: watermarks_category_id_seq; Type: SEQUENCE SET; Schema: public; Owner: vvf
--

SELECT pg_catalog.setval('public.watermarks_category_id_seq', 19, true);


--
-- Name: watermarks_category watermarks_category_pkey; Type: CONSTRAINT; Schema: public; Owner: vvf
--

ALTER TABLE ONLY public.watermarks_category
    ADD CONSTRAINT watermarks_category_pkey PRIMARY KEY (id);


--
-- Name: watermarks_category_user_id_fa373b47; Type: INDEX; Schema: public; Owner: vvf
--

CREATE INDEX watermarks_category_user_id_fa373b47 ON public.watermarks_category USING btree (user_id);


--
-- Name: watermarks_category watermarks_category_user_id_fa373b47_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: vvf
--

ALTER TABLE ONLY public.watermarks_category
    ADD CONSTRAINT watermarks_category_user_id_fa373b47_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- PostgreSQL database dump complete
--

