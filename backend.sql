CREATE DATABASE videostore;
USE videostore;

CREATE TABLE Movies (
    MovieID INT PRIMARY KEY,
    Title VARCHAR(60),
    Director VARCHAR(60),
    Genre VARCHAR(30),
    RentalPrice INT,
    RentalCount INT
);

INSERT INTO Movies VALUES 
(101, 'Eternal Sunshine of the Spotless Mind', 'Michel Gondry', 'Drama', 250, 480),
(102, 'Dead Poets Society', 'Peter Weir', 'Drama', 190, 420),
(103, 'The Virgin Suicides', 'Sofia Coppola', 'Drama', 220, 310),
(104, 'Mulholland Drive', 'David Lynch', 'Thriller', 290, 390),
(105, 'Amelie', 'Jean-Pierre Jeunet', 'Comedy', 230, 440),
(106, 'Kill Bill: Vol. 1', 'Quentin Tarantino', 'Action', 260, 510),
(107, '10 Things I Hate About You', 'Gil Junger', 'Comedy', 180, 470),
(108, 'Lost in Translation', 'Sofia Coppola', 'Drama', 240, 350),
(109, 'Blue Velvet', 'David Lynch', 'Thriller', 250, 280),
(110, 'La La Land', 'Damien Chazelle', 'Musical', 220, 450),
(111, 'Before Sunrise', 'Richard Linklater', 'Romance', 180, 400),
(112, 'Twin Peaks: Fire Walk with Me', 'David Lynch', 'Thriller', 270, 260),
(113, 'Fight Club', 'David Fincher', 'Thriller', 190, 490),
(114, 'Lady Bird', 'Greta Gerwig', 'Drama', 200, 370),
(115, 'Marie Antoinette', 'Sofia Coppola', 'Drama', 260, 290);

SELECT * FROM Movies;
