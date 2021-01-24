-- Table: public.hrds_train_features

-- DROP TABLE public.hrds_train_features;

CREATE TABLE public.hrds_train_features
(
    enrollee_id integer NOT NULL,
    city character varying(30)[] COLLATE pg_catalog."default",
    city_development_index numeric,
    gender character varying(10) COLLATE pg_catalog."default",
    relevent_experience character varying(30) COLLATE pg_catalog."default",
    enrolled_university character varying(30) COLLATE pg_catalog."default",
    education_level character varying(30) COLLATE pg_catalog."default",
    major_discipline character varying(30) COLLATE pg_catalog."default",
    experience character varying(30) COLLATE pg_catalog."default",
    company_size character varying(30) COLLATE pg_catalog."default",
    company_type character varying(30) COLLATE pg_catalog."default",
    last_new_job character varying(30) COLLATE pg_catalog."default",
    training_hours integer,
    CONSTRAINT hrds_train_features_pkey PRIMARY KEY (enrollee_id)
)

TABLESPACE pg_default;

ALTER TABLE public.hrds_train_features
    OWNER to postgres;

COMMENT ON TABLE public.hrds_train_features
    IS 'This table is for training and testing the model';

-- Table: public.hrds_test_labels

-- DROP TABLE public.hrds_test_labels;

CREATE TABLE public.hrds_test_labels
(
    enrollee_id integer NOT NULL,
    city character varying(30)[] COLLATE pg_catalog."default",
    city_development_index numeric,
    gender character varying(10) COLLATE pg_catalog."default",
    relevent_experience character varying(30) COLLATE pg_catalog."default",
    enrolled_university character varying(30) COLLATE pg_catalog."default",
    education_level character varying(30) COLLATE pg_catalog."default",
    major_discipline character varying(30) COLLATE pg_catalog."default",
    experience character varying(30) COLLATE pg_catalog."default",
    company_size character varying(30) COLLATE pg_catalog."default",
    company_type character varying(30) COLLATE pg_catalog."default",
    last_new_job character varying(30) COLLATE pg_catalog."default",
    training_hours integer,
    CONSTRAINT hrds_test_labels_pkey PRIMARY KEY (enrollee_id)
)

TABLESPACE pg_default;

ALTER TABLE public.hrds_test_labels
    OWNER to postgres;

COMMENT ON TABLE public.hrds_test_labels
    IS 'This table is for creating predictions with the model';

-- Table: public.hrds_train_labels

-- DROP TABLE public.hrds_train_labels;
create table public.hrds_train_labels (
    enrollee_id integer NOT NULL,
    target integer,
    constraint hrds_train_labels_pk primary key (enrollee_id),
    CONSTRAINT hrds_train_labels_fk foreign key (enrollee_id) references hrds_train_features(enrollee_id)
)

TABLESPACE pg_default;

ALTER TABLE public.hrds_train_labels
    OWNER to postgres;

COMMENT ON TABLE public.hrds_train_labels
    IS 'This table contains labels related to hrds_train_features';