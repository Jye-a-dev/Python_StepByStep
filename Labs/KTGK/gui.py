import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox
from database import Database


class QuanLyThietBiApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quản lý thiết bị học tập")
        self.root.geometry("800x600")

        # Khởi tạo kết nối DB từ module database
        try:
            self.db = Database()
        except Exception as e:
            messagebox.showerror("Lỗi kết nối", f"Không thể kết nối cơ sở dữ liệu: {e}")

        # Khai báo biến giao diện
        self.ma_var = tk.StringVar()
        self.ten_var = tk.StringVar()
        self.loai_var = tk.StringVar()
        self.so_luong_var = tk.StringVar()
        self.tinh_trang_var = tk.StringVar()

        self.setup_gui()
        self.load_data()

    def setup_gui(self):
        # Frame Nhập liệu
        input_frame = tk.LabelFrame(self.root, text="Thông tin thiết bị")
        input_frame.pack(fill="x", padx=10, pady=5)

        tk.Label(input_frame, text="Mã thiết bị:").grid(
            row=0, column=0, padx=5, pady=5, sticky="e"
        )
        tk.Entry(input_frame, textvariable=self.ma_var).grid(
            row=0, column=1, padx=5, pady=5
        )

        tk.Label(input_frame, text="Tên thiết bị:").grid(
            row=0, column=2, padx=5, pady=5, sticky="e"
        )
        tk.Entry(input_frame, textvariable=self.ten_var).grid(
            row=0, column=3, padx=5, pady=5
        )

        tk.Label(input_frame, text="Loại:").grid(
            row=1, column=0, padx=5, pady=5, sticky="e"
        )
        tk.Entry(input_frame, textvariable=self.loai_var).grid(
            row=1, column=1, padx=5, pady=5
        )

        tk.Label(input_frame, text="Số lượng:").grid(
            row=1, column=2, padx=5, pady=5, sticky="e"
        )
        tk.Entry(input_frame, textvariable=self.so_luong_var).grid(
            row=1, column=3, padx=5, pady=5
        )

        tk.Label(input_frame, text="Tình trạng:").grid(
            row=2, column=0, padx=5, pady=5, sticky="e"
        )
        tinh_trang_cb = ttk.Combobox(
            input_frame,
            textvariable=self.tinh_trang_var,
            values=["Đang sử dụng", "Đang bảo trì", "Ngừng sử dụng"],
        )
        tinh_trang_cb.grid(row=2, column=1, padx=5, pady=5)

        # Frame Nút chức năng
        btn_frame = tk.Frame(self.root)
        btn_frame.pack(fill="x", padx=10, pady=5)

        tk.Button(btn_frame, text="Thêm", command=self.add_record).pack(
            side="left", padx=5
        )
        tk.Button(btn_frame, text="Cập nhật", command=self.update_record).pack(
            side="left", padx=5
        )
        tk.Button(btn_frame, text="Xóa", command=self.delete_record).pack(
            side="left", padx=5
        )
        tk.Button(btn_frame, text="Làm mới", command=self.load_data).pack(
            side="left", padx=5
        )
        tk.Button(btn_frame, text="Tìm kiếm", command=self.search_record).pack(
            side="left", padx=5
        )

        # Treeview hiển thị dữ liệu
        columns = ("ma", "ten", "loai", "sl", "tinh_trang")
        self.tree = ttk.Treeview(self.root, columns=columns, show="headings")
        self.tree.heading("ma", text="Mã TB")
        self.tree.heading("ten", text="Tên TB")
        self.tree.heading("loai", text="Loại")
        self.tree.heading("sl", text="Số lượng")
        self.tree.heading("tinh_trang", text="Tình trạng")
        self.tree.pack(fill="both", expand=True, padx=10, pady=5)
        self.tree.bind("<ButtonRelease-1>", self.select_record)

    def validate_data(self):
        ma = self.ma_var.get().strip()
        ten = self.ten_var.get().strip()
        sl = self.so_luong_var.get()
        tt = self.tinh_trang_var.get()

        if not ma or not ten:
            messagebox.showwarning("Cảnh báo", "Mã và tên không được để trống!")
            return False
        try:
            if int(sl) < 0:
                raise ValueError
        except ValueError:
            messagebox.showwarning("Cảnh báo", "Số lượng phải là số nguyên không âm!")
            return False

        if tt not in ["Đang sử dụng", "Đang bảo trì", "Ngừng sử dụng"]:
            messagebox.showwarning("Cảnh báo", "Tình trạng không hợp lệ!")
            return False
        return True

    def populate_treeview(self, rows):
        for row in self.tree.get_children():
            self.tree.delete(row)
        for row in rows:
            self.tree.insert("", "end", values=row)

    def load_data(self):
        try:
            rows = self.db.fetch_all()
            self.populate_treeview(rows)
            self.clear_entries()
        except Exception as e:
            messagebox.showerror("Lỗi", f"Lỗi tải dữ liệu: {e}")

    def clear_entries(self):
        self.ma_var.set("")
        self.ten_var.set("")
        self.loai_var.set("")
        self.so_luong_var.set("")
        self.tinh_trang_var.set("")

    def add_record(self):
        if self.validate_data():
            try:
                self.db.insert(
                    self.ma_var.get(),
                    self.ten_var.get(),
                    self.loai_var.get(),
                    int(self.so_luong_var.get()),
                    self.tinh_trang_var.get(),
                )
                messagebox.showinfo("Thành công", "Thêm thiết bị thành công!")
                self.load_data()
            except sqlite3.IntegrityError:
                messagebox.showerror("Lỗi", "Mã thiết bị đã tồn tại!")
            except Exception as e:
                messagebox.showerror("Lỗi", str(e))

    def select_record(self, event):
        selected = self.tree.focus()
        if selected:
            values = self.tree.item(selected, "values")
            # Lưu lại mã thiết bị ban đầu vào một biến tạm
            self.ma_goc = values[0]

            self.ma_var.set(values[0])
            self.ten_var.set(values[1])
            self.loai_var.set(values[2])
            self.so_luong_var.set(values[3])
            self.tinh_trang_var.set(values[4])

    def update_record(self):
        if not hasattr(self, "ma_goc") or not self.ma_goc:
            messagebox.showwarning(
                "Cảnh báo", "Vui lòng chọn một thiết bị từ danh sách để cập nhật!"
            )
            return

        if self.validate_data():
            try:
                self.db.update(
                    self.ma_goc,
                    self.ten_var.get(),
                    self.loai_var.get(),
                    int(self.so_luong_var.get()),
                    self.tinh_trang_var.get(),
                )
                messagebox.showinfo("Thành công", "Cập nhật thành công!")
                self.ma_goc = None
                self.load_data()
            except Exception as e:
                messagebox.showerror("Lỗi", str(e))

    def delete_record(self):
        ma = self.ma_var.get()
        if not ma:
            messagebox.showwarning("Cảnh báo", "Vui lòng chọn bản ghi để xóa!")
            return
        if messagebox.askyesno("Xác nhận", f"Bạn có chắc muốn xóa thiết bị mã {ma}?"):
            try:
                self.db.delete(ma)
                messagebox.showinfo("Thành công", "Đã xóa bản ghi!")
                self.load_data()
            except Exception as e:
                messagebox.showerror("Lỗi", str(e))

    def search_record(self):
        tu_khoa = self.ma_var.get() or self.ten_var.get()
        try:
            rows = self.db.search(tu_khoa)
            self.populate_treeview(rows)
        except Exception as e:
            messagebox.showerror("Lỗi", str(e))
