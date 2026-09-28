
CREATE TABLE IF NOT EXISTS books (
    "Book_ID" SERIAL PRIMARY KEY,
    "Book_Title" VARCHAR(250) NOT NULL,
    "Book_Page" INTEGER
);

CREATE TABLE IF NOT EXISTS quotations (
    "Quote_ID" SERIAL PRIMARY KEY,
    "Quotation" VARCHAR(250) NOT NULL,
    "Books_Book_ID" INTEGER REFERENCES books("Book_ID") ON DELETE CASCADE
);

INSERT INTO books ("Book_Title", "Book_Page") 
VALUES 
    ('Design Patterns', 7),
    ('xUnit Test Patterns', 31)
ON CONFLICT DO NOTHING;

INSERT INTO quotations ("Quotation", "Books_Book_ID") 
VALUES 
    ('Programming to an Interface, not an Implementation', 1),
    ('Philosophy of Test Automation', 2)
ON CONFLICT DO NOTHING;