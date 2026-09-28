import os
import tkinter as tk
from tkinter import Menu, messagebox, scrolledtext, ttk
from dotenv import load_dotenv
import psycopg2

load_dotenv()

DB_HOST = os.getenv("DB_HOST", "127.0.0.1")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("DB_NAME", "guidb")
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD", "")

def get_connection():
    return psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )

def _quit():
    win.quit()
    win.destroy()
    exit()

def _msg_box():
    messagebox.showinfo("About", "Python GUI with PostgreSQL Database\nLab 5")

def insert_quote():
    title = entry_title_crud.get().strip()
    page = entry_page_crud.get().strip()
    quote = scr.get("1.0", tk.END).strip()

    if not title or not quote:
        messagebox.showwarning("Cảnh báo", "Vui lòng nhập Book Title và Book Quotation ở hàng CRUD!")
        return

    try:
        page_val = int(page) if page else None
        conn = get_connection()
        cur = conn.cursor()

        cur.execute(
            'INSERT INTO books ("Book_Title", "Book_Page") VALUES (%s, %s) RETURNING "Book_ID"',
            (title, page_val)
        )
        book_id = cur.fetchone()[0]

        cur.execute(
            'INSERT INTO quotations ("Quotation", "Books_Book_ID") VALUES (%s, %s)',
            (quote, book_id)
        )

        conn.commit()
        cur.close()
        conn.close()

        # Hiển thị kết quả vừa tạo lên hàng Return (Read-only)
        entry_title_ro.configure(state='normal')
        entry_page_ro.configure(state='normal')
        entry_title_ro.delete(0, tk.END)
        entry_page_ro.delete(0, tk.END)
        entry_title_ro.insert(0, f"[{book_id}] {title}")
        entry_page_ro.insert(0, str(page_val if page_val is not None else ""))
        entry_title_ro.configure(state='readonly')
        entry_page_ro.configure(state='readonly')

        messagebox.showinfo("Thành công", f"Đã thêm thành công Book ID: {book_id}")
        get_quotes()
    except Exception as e:
        messagebox.showerror("Database Error", str(e))

def get_quotes():
    try:
        conn = get_connection()
        cur = conn.cursor()

        query = """
            SELECT q."Quotation", b."Book_ID", b."Book_Title", b."Book_Page"
            FROM quotations q
            JOIN books b ON q."Books_Book_ID" = b."Book_ID"
            ORDER BY q."Quote_ID" ASC
        """
        cur.execute(query)
        rows = cur.fetchall()

        scr.delete("1.0", tk.END)
        for quote, book_id, title, page in rows:
            scr.insert(tk.END, f"{quote}...{{{book_id}  {{{title}}}  {page}}}\n")

        # Cập nhật bản ghi mới nhất lên hàng Return (Read-only)
        if rows:
            last_quote, last_id, last_title, last_page = rows[-1]
            entry_title_ro.configure(state='normal')
            entry_page_ro.configure(state='normal')
            entry_title_ro.delete(0, tk.END)
            entry_page_ro.delete(0, tk.END)
            entry_title_ro.insert(0, f"[{last_id}] {last_title}")
            entry_page_ro.insert(0, str(last_page if last_page is not None else ""))
            entry_title_ro.configure(state='readonly')
            entry_page_ro.configure(state='readonly')

        cur.close()
        conn.close()
    except Exception as e:
        messagebox.showerror("Database Error", str(e))

def modify_quote():
    title = entry_title_crud.get().strip()
    new_quote = scr.get("1.0", tk.END).strip()

    if not title or not new_quote:
        messagebox.showwarning("Cảnh báo", "Vui lòng nhập Book Title cần sửa (hàng CRUD) và nội dung mới trong ô Quotation!")
        return

    try:
        conn = get_connection()
        cur = conn.cursor()

        cur.execute('SELECT "Book_ID" FROM books WHERE "Book_Title" = %s', (title,))
        row = cur.fetchone()

        if not row:
            messagebox.showwarning("Không tìm thấy", f"Không tìm thấy sách có tên: {title}")
            cur.close()
            conn.close()
            return

        book_id = row[0]
        cur.execute(
            'UPDATE quotations SET "Quotation" = %s WHERE "Books_Book_ID" = %s',
            (new_quote, book_id)
        )

        conn.commit()
        cur.close()
        conn.close()

        messagebox.showinfo("Thành công", f"Đã cập nhật câu trích dẫn cho Book ID: {book_id}")
        get_quotes()
    except Exception as e:
        messagebox.showerror("Database Error", str(e))

def delete_quote():
    title = entry_title_crud.get().strip()
    if not title:
        messagebox.showwarning("Cảnh báo", "Vui lòng nhập Book Title cần xóa tại hàng CRUD!")
        return

    try:
        conn = get_connection()
        cur = conn.cursor()

        cur.execute('DELETE FROM books WHERE "Book_Title" = %s RETURNING "Book_ID"', (title,))
        deleted_row = cur.fetchone()

        if not deleted_row:
            messagebox.showwarning("Không tìm thấy", f"Không tìm thấy sách: {title}")
            cur.close()
            conn.close()
            return

        conn.commit()
        cur.close()
        conn.close()

        # Dọn sạch hàng Read-only nếu xóa đúng sách đó
        entry_title_ro.configure(state='normal')
        entry_page_ro.configure(state='normal')
        entry_title_ro.delete(0, tk.END)
        entry_page_ro.delete(0, tk.END)
        entry_title_ro.configure(state='readonly')
        entry_page_ro.configure(state='readonly')

        messagebox.showinfo("Thành công", f"Đã xóa sách ID: {deleted_row[0]}")
        get_quotes()
    except Exception as e:
        messagebox.showerror("Database Error", str(e))

win = tk.Tk()
win.title("Python GUI")
win.geometry("540x380")
win.resizable(False, False)

# Menu Bar
menu_bar = Menu(win)
win.config(menu=menu_bar)

file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Exit", command=_quit)
menu_bar.add_cascade(label="File", menu=file_menu)

help_menu = Menu(menu_bar, tearoff=0)
help_menu.add_command(label="About", command=_msg_box)
menu_bar.add_cascade(label="Help", menu=help_menu)

# Notebook Tabs
tab_control = ttk.Notebook(win)
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab_control.add(tab1, text="PostgreSQL")
tab_control.add(tab2, text="Widgets")
tab_control.pack(expand=1, fill="both")

# Style cho tiêu đề LabelFrame
style = ttk.Style()
style.configure("BlueTitle.TLabelframe.Label", foreground="#1d4ed8")

db_frame = ttk.LabelFrame(tab1, text=" Python Database ", style="BlueTitle.TLabelframe")
db_frame.pack(fill="x", padx=10, pady=6)

# Tiêu đề cột
ttk.Label(db_frame, text="Book Title:").grid(row=0, column=0, sticky="w", padx=6, pady=2)
ttk.Label(db_frame, text="Page:").grid(row=0, column=1, sticky="w", padx=6, pady=2)

# --- HÀNG 1: HÀNG CRUD (NHẬP ĐƯỢC ĐỂ THAO TÁC C/R/U/D) ---
entry_title_crud = ttk.Entry(db_frame, width=38)
entry_title_crud.grid(row=1, column=0, padx=6, pady=3, sticky="w")
entry_title_crud.insert(0, "The Meaning of Life")

entry_page_crud = ttk.Entry(db_frame, width=8)
entry_page_crud.grid(row=1, column=1, padx=6, pady=3, sticky="w")
entry_page_crud.insert(0, "42")

btn_insert = ttk.Button(db_frame, text="Insert Quote", width=14, command=insert_quote)
btn_insert.grid(row=1, column=2, padx=8, pady=3)

# --- HÀNG 2: HÀNG RETURN (READ-ONLY / KHÔNG NHẬP ĐƯỢC) ---
entry_title_ro = ttk.Entry(db_frame, width=38, state='readonly')
entry_title_ro.grid(row=2, column=0, padx=6, pady=3, sticky="w")

entry_page_ro = ttk.Entry(db_frame, width=8, state='readonly')
entry_page_ro.grid(row=2, column=1, padx=6, pady=3, sticky="w")

btn_get = ttk.Button(db_frame, text="Get Quotes", width=14, command=get_quotes)
btn_get.grid(row=2, column=2, padx=8, pady=3)

# --- HÀNG 3: NÚT MODIFY & DELETE CHO CRUD ---
btn_modify = ttk.Button(db_frame, text="Modify Quote", width=14, command=modify_quote)
btn_modify.grid(row=3, column=2, padx=8, pady=3)

btn_delete = ttk.Button(db_frame, text="Delete Quote", width=14, command=delete_quote)
btn_delete.grid(row=3, column=0, sticky="w", padx=6, pady=3)

# Khung ScrolledText trích dẫn
quote_frame = ttk.LabelFrame(tab1, text=" Book Quotation ", style="BlueTitle.TLabelframe")
quote_frame.pack(fill="both", expand=True, padx=10, pady=(2, 8))

scr = scrolledtext.ScrolledText(quote_frame, wrap=tk.WORD, height=6)
scr.pack(fill="both", expand=True, padx=6, pady=6)
scr.insert(tk.END, "The Life of Brian...{1  {The Meaning of Life}  42}")

win.mainloop()