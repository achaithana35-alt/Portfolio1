-- ==========================================
-- CREATE DATABASE
-- ==========================================

CREATE DATABASE IF NOT EXISTS portfolio_db;

USE portfolio_db;


-- ==========================================
-- CONTACT TABLE
-- ==========================================

CREATE TABLE IF NOT EXISTS contact_messages (

    id INT AUTO_INCREMENT PRIMARY KEY,

    name VARCHAR(100) NOT NULL,

    email VARCHAR(150) NOT NULL,

    subject VARCHAR(200),

    message TEXT NOT NULL,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

);



-- ==========================================
-- PROJECTS TABLE
-- ==========================================

CREATE TABLE IF NOT EXISTS projects (

    id INT AUTO_INCREMENT PRIMARY KEY,

    title VARCHAR(200) NOT NULL,

    description TEXT,

    tech_stack VARCHAR(300),

    github_link VARCHAR(300),

    image VARCHAR(255),

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

);



-- ==========================================
-- SKILLS TABLE
-- ==========================================

CREATE TABLE IF NOT EXISTS skills (

    id INT AUTO_INCREMENT PRIMARY KEY,

    skill_name VARCHAR(100) NOT NULL,

    percentage INT NOT NULL

);



-- ==========================================
-- INSERT SKILLS DATA
-- ==========================================

INSERT INTO skills(skill_name,percentage)

VALUES

('Python',90),
('Java',85),
('SQL',85),
('HTML & CSS',90),
('JavaScript',80),
('Machine Learning',85);



-- ==========================================
-- INSERT PROJECT DATA
-- ==========================================

INSERT INTO projects
(title,description,tech_stack,github_link,image)

VALUES


(
'AI Career Guidance System',

'AI based career recommendation system using machine learning models.',

'Python, Scikit-learn, XGBoost, MongoDB',

'https://github.com/',

'career.png'

),


(
'Farm Management System',

'Web application for farmers to manage products and farming details.',

'Python Flask, MySQL, HTML, CSS',

'https://github.com/',

'farm.png'

);