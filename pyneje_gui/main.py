import Tkinter
import tkFileDialog
import ttk

import ImageTk
import PIL


class GUI:
    def __init__(self, tk, port):
        self.engraver = port
        self.tk = tk

        # Gui start here
        root = self.tk
        root.title("pyNeje")

        # tabs"
        # import ttk
        notebook = ttk.Notebook(root)
        image_tab = ttk.Frame(notebook)
        jog_tab = ttk.Frame(notebook)
        prefs_tab = ttk.Frame(notebook)
        notebook.add(image_tab, text='Image')
        notebook.add(jog_tab, text='jog')
        notebook.add(prefs_tab, text='Prefs')
        notebook.pack()

        # frames
        image_frame_button = ttk.Frame(image_tab)

        # entrys
        # entry_usb_port = Entry(prefs_tab, textvariable=usb_port)

        # Sliders
        speed_slider = ttk.Scale(prefs_tab, from_=0, to=255, orient=Tkinter.HORIZONTAL)
        burn_time_slider = ttk.Scale(prefs_tab, from_=0, to=255, orient=Tkinter.HORIZONTAL)

        # labels
        # image preview
        im = PIL.Image.open("default.png").convert("1").resize((512, 512))

        tk_image = ImageTk.PhotoImage(im)

        label_image = ttk.Label(image_tab, image=tk_image)
        # info
        self.label_info = ttk.Label(root, text=(im.format, im.size, im.mode))
        # entry_label
        serial_label = ttk.Label(prefs_tab, text="serial ")
        # speed_label
        speed_label = ttk.Label(prefs_tab, text="speed jog")
        # speed_label
        burn_time_label = ttk.Label(prefs_tab, text="burn time")

        # buttons
        # image_frame_button
        engrave_memory_bt = ttk.Button(image_frame_button, text="engrave", command=self.engrave_memory)
        engrave_pause_bt = ttk.Button(image_frame_button, text="pause", command=self.engrave_pause)
        engrave_preview_bt = ttk.Button(image_frame_button, text="preview", command=self.engrave_preview)
        send_image_bt = ttk.Button(image_frame_button, text="upload", command=self.send_image)
        open_image_bt = ttk.Button(image_frame_button, text='open', command=self.open_image)

        # jog_tab
        reset_bt = ttk.Button(jog_tab, text="reset", command=self.reset)
        home_bt = ttk.Button(jog_tab, text="home", command=self.move_home)
        center_bt = ttk.Button(jog_tab, text="center", command=self.move_center)

        # grid root
        self.label_info.pack()
        # grid frame
        image_frame_button.grid(row=1, column=0)

        # grid image_tab
        label_image.grid(row=0, column=0)

        open_image_bt.grid(row=0, column=0)
        send_image_bt.grid(row=0, column=1)
        engrave_preview_bt.grid(row=0, column=2)
        engrave_memory_bt.grid(row=0, column=3)
        engrave_pause_bt.grid(row=0, column=4)
        # grid jog_tab
        reset_bt.pack()
        home_bt.pack()
        center_bt.pack()
        # grid prefs_tab
        serial_label.grid(row=0, column=0)
        # entry_usb_port.grid(row=0, column=1)
        speed_label.grid(row=1, column=0)
        speed_slider.grid(row=1, column=1)
        burn_time_label.grid(row=2, column=0)
        burn_time_slider.grid(row=2, column=1)

        # menu
        menu = Tkinter.Menu(root)
        root.config(menu=menu)
        filemenu = Tkinter.Menu(menu)
        menu.add_cascade(label="File", menu=filemenu)
        filemenu.add_command(label="Open...", command=self.open_image)
        filemenu.add_separator()
        filemenu.add_command(label="Quit", command=root.quit)

        helpmenu = Tkinter.Menu(menu)
        menu.add_cascade(label="Help", menu=helpmenu)
        helpmenu.add_command(label="About...", command=self.about)
        root.update()
        pass

    def update_status(self, value):
        self.label_info.config(text=value)

    def about():
        about = about(root)
        donation_img = PIL.Image.open(bitcoin - donation.png)
        about.title("pyNeje " + version)
        label_about = ttk.Label(about, image="donation_img")
        about.mainloop()

    def open_image():
        fileName = tkFileDialog.askopenfilename(parent=root, title='Choose a file')
        im = PIL.Image.open(fileName).convert("1").resize((512, 512))

        label_image.config = ttk.Label(image_tab, image=input)
        # print(im)
        # im = Image.open(name_image)

    def convert_image():
        im = PIL.Image.open(name_image).convert("1")
        # im = Image.open(name_image)
        im = im.resize((512, 512))
        print((im.format, im.size, im.mode))

    def engrave_memory(self):
        # set 60 ms
        ser.write("3c".decode("hex"))
        # engrave
        self.label_info.config(text="Engraving Memory...")
        ser.write("f1".decode("hex"))
        self.label_info.config(text="Engraving Memory done")

    def engrave_pause(self):
        self.engraver.pause()
        self.update_status("Pause")

    def engrave_preview(self):
        self.engraver.preview()
        self.update_status("Visualizing preview")

    def reset(self):
        self.engraver.reset()
        self.update_status("Reset")

    def move_home(self):
        self.engraver.move_home()
        self.update_status("Move home")

    def move_center(self):
        self.engraver.move_center()
        self.update_status("Move center")

    def send_image():
        a = 0
        while a < 8:
            a = a + 1
            print(("Erase EEPROM 8/" + str(a)))
            # erase eeprom
            ser.write("fe".decode("hex"))
        # upload to eeprom
        label_info.config(text="Uploading to EEPROM. please wait...")
        ser.write(im.getdata())
        label_info.config(text="Uploading to EEPROM. Done")

    def run(self):
        # tk main loop
        self.tk.mainloop()
