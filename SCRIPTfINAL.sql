#PARA A DISCIPLINA (APENAS UMA VEZ)!!!!!!

#pegar o nome de tds os q responderam os 4 foruns da disciplina
CREATE TABLE info_qmrespondeu_4forum_informaticaaplicada
SELECT f.discussion, f.userid, f.subject, f. message,
u.id, u.firstname
FROM basepesq.mdl_forum_posts as f
INNER JOIN 
mdl_user as u on f.userid = u.id
where discussion = 25 or discussion = 26 or discussion = 27 or discussion = 28 
group by userid;

#PARA CADA FORUM!!!!!!!!
#escolher disciplina e pegar o id do forum
SELECT * FROM basepesq.discbiologia;

#saber ql o iddiscussion do forum 
SELECT * FROM basepesq.mdl_forum_discussions where forum = 58;

#ver a interaçao no forum
#pegar nome de qm interagiu no forum
create table interacao_forum58
SELECT f.discussion, f.userid, f.subject, f.message, u.id, u.firstname
FROM basepesq.mdl_forum_posts as f, mdl_user as u 
where discussion = 28
and f.userid = u.id
group by userid;

#pegar o g.itemig
SELECT * FROM basepesq.mdl_grade_items where courseid = 54;


#informaçao (nota e nome) qm respondeu ao forum 44
create table informacao_qmrespondeu_forum58
SELECT i.discussion, i.subject, i.message,
i.userid, u.firstname, u.lastname, g.itemid, g.rawgrade
FROM interacao_forum58 as i, mdl_user as u, mdl_grade_grades as g
where i.userid = u.id
and i.userid = g.userid
and g.itemid = 169;


#interação no forum qm respondeu ao forum mandou e recebeu mensagem p qm?
#qm respondeu ao forum (idfrom) c qm ele mandou mensagem (idto)
#ou qm respondeu ao forum (idto) recebeu mensagem de qm (idfrom)
#tabelas usadas seraõ qmRespondeuDiscElemntosGeologia e mdl_message
CREATE TABLE interacao_messagem_forum_58
SELECT d.discussion, d.userid, d.subject, d.message,
m.useridto, m.useridfrom, m.fullmessage
FROM interacao_forum58 as d, mdl_message m
#o userid da disciplina é useridto de mensagem
#quem respondeu ao forum (idto) recebeu mesnsagem de (idfrom)
where d.userid = m.useridto
#qm respondeu ao forum (idfrom) enviou mensagem p quem ((idto)
or d.userid = m.useridfrom;


#PARA PEGAR AS NOTAS DAS ATIVIDADES WEBQUEST E AVALIAÇAO PRESENCIAL
#DE QUEM RESPONDEU OS 4 FORUNS

#1 PASSO : procurar o itemid da atividade procurando pelo id do curso
SELECT * FROM basepesq.mdl_grade_items WHERE COURSEID = 54;


#nota de qm respondeu os 4 foruns em cada avaliação (webquest, presencial)
CREATE TABLE nota2ava_pres_informaticaAplicada
SELECT  d.discussion, d.subject, d. message, d.id, d.firstname,
g.rawgrade, g.userid, g.itemid
FROM basepesq.info_qmrespondeu_4forum_informaticaaplicada as d
INNER JOIN 
mdl_grade_grades as g on g.userid = d.userid
where g.itemid = 174; #MUDAR DE ACORDO A ATIVIDADE