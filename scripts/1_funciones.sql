-- Crear la secuencia id_contact
CREATE SEQUENCE id_contact START 1;
-- Crear la tabla contact
CREATE TABLE IF NOT EXISTS public.contact
(
    id integer NOT NULL DEFAULT nextval('id_contact'),
    fullname character varying(100) COLLATE pg_catalog."default",
    email character varying(100) COLLATE pg_catalog."default",
    phone character varying(100) COLLATE pg_catalog."default",
    CONSTRAINT contact_pkey PRIMARY KEY (id)
);

-- Definición de la función get_contact
CREATE OR REPLACE FUNCTION public.get_contact()
    RETURNS TABLE(c_id integer, c_fullname character varying, c_email character varying, c_phone character varying) 
    LANGUAGE 'plpgsql'
AS $BODY$
BEGIN
    RETURN QUERY
    SELECT c.id, c.fullname, c.email, c.phone 
    FROM contact c order by c.id asc;
END;
$BODY$;

-- Definición de la función get_contact_id
CREATE OR REPLACE FUNCTION public.get_contact_id(p_id integer)
    RETURNS TABLE(c_id integer, c_fullname character varying, c_email character varying, c_phone character varying) 
    LANGUAGE 'plpgsql'
AS $BODY$
BEGIN
    RETURN QUERY
    SELECT c.id, c.fullname, c.email, c.phone 
    FROM contact c WHERE c.id = p_id;
END;
$BODY$;

-- Definición de la función ins_contact
CREATE OR REPLACE FUNCTION public.ins_contact(p_fullname character varying, p_email character varying, p_phone character varying)
    RETURNS void
    LANGUAGE 'plpgsql'
AS $BODY$
BEGIN
    INSERT INTO contact (fullname, email, phone) 
    VALUES (p_fullname, p_email, p_phone);
END;
$BODY$;

-- Definición de la función upd_contact
CREATE OR REPLACE FUNCTION public.upd_contact(p_fullname character varying, p_email character varying, p_phone character varying, p_id integer)
    RETURNS void
    LANGUAGE 'plpgsql'
AS $BODY$
BEGIN
    UPDATE contact SET fullname = p_fullname, 
    email = p_email, phone = p_phone WHERE id = p_id;
END;
$BODY$;

-- Definición de la función del_contact
CREATE OR REPLACE FUNCTION public.del_contact(p_id integer)
    RETURNS void
    LANGUAGE 'plpgsql'
AS $BODY$
BEGIN
    DELETE FROM contact WHERE id = p_id;
END;
$BODY$;
