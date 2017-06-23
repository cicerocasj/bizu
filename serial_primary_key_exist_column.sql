
/*
cria serial primary key para coluna existente
*/
create sequence aneel.subestacoes_id_seq;
alter table aneel.subestacoes alter column id set default nextval('aneel.subestacoes_id_seq');
alter table aneel.subestacoes alter column id set not null;
alter table aneel.subestacoes add constraint subestacoes_id_pk primary key(id);
