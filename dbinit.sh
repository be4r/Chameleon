#!/bin/bash
############### INITIATE DATABASE INITIALISATION ###############
mysql -e 'create user usser@localhost identified by "P4$sW0rD!1"; select user from mysql.user; create database reqs; use reqs; create table reqs (id INT(30) UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY, req VARCHAR(32), cont VARCHAR(255)); create table urls (id INT(32) UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY, url VARCHAR(2048)); grant all privileges on *.* to "usser"@"localhost";'
############### DATABASE INITIALISATION INITIALISED ###############
