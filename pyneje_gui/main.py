import Tkinter
import tkFileDialog
import ttk

import ImageTk
import PIL


class GUI:
    def __init__(self, tk, port):
        self.engraver = port
        self.tk = tk
        self.engraveImage = None
        self.previewImage = None

        # Gui start here
        root = self.tk
        root.title("pyNeje/PyBeam")

        # tabs"
        # import ttk
        notebook = ttk.Notebook(root)
        self.image_tab = ttk.Frame(notebook)
        jog_tab = ttk.Frame(notebook)
        prefs_tab = ttk.Frame(notebook)
        notebook.add(self.image_tab, text='Image')
        notebook.add(jog_tab, text='jog')
        notebook.add(prefs_tab, text='Prefs')
        notebook.pack()

        # frames
        image_frame_button = ttk.Frame(self.image_tab)

        # entrys
        # entry_usb_port = Entry(prefs_tab, textvariable=usb_port)

        # Sliders
        speed_slider = ttk.Scale(prefs_tab, from_=0, to=255, orient=Tkinter.HORIZONTAL)
        burn_time_slider = ttk.Scale(prefs_tab, from_=0, to=255, orient=Tkinter.HORIZONTAL)

        # labels
        # image preview

        im = PIL.Image.open("default.png").resize((512, 512)).convert("1")

        self.previewImage = ImageTk.PhotoImage(im)

        self.label_image = ttk.Label(self.image_tab, image=self.previewImage)
        # info
        self.label_info = ttk.Label(root, text="Welcome to PyNeje/PyBeam")
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
        self.label_image.grid(row=0, column=0)

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
        self.label_info.configure(text=value)

    def about():
        about = about(root)
        donation_img = PIL.Image.open(bitcoin-donation.png)
        about.title("pyNeje " + version)
        label_about = ttk.Label(about, image="donation_img")
        about.mainloop()

    def open_image(self):
        file_name = tkFileDialog.askopenfilename(parent=self.tk, title='Choose a file')
        self.engraveImage = PIL.Image.open(file_name).resize((512, 512)).convert("1")
        self.previewImage = ImageTk.PhotoImage(self.engraveImage)
        self.label_image.configure(image=self.previewImage)

    def engrave_memory(self):
        self.update_status("Engraving from EPROM...")
        # set 60 ms
        self.engraver.adjust_burntime(60)
        # engrave
        self.engraver.start()

    def engrave_pause(self):
        self.update_status("Pause")
        self.engraver.pause()

    def engrave_preview(self):
        self.update_status("Visualizing preview")
        self.engraver.preview()

    def reset(self):
        self.update_status("Reset")
        self.engraver.reset()

    def move_home(self):
        self.update_status("Move home")
        self.engraver.move_home()

    def move_center(self):
        self.update_status("Move center")
        self.engraver.move_center()

    def send_image(self):
        # upload to eeprom
        self.update_status("Uploading to EEPROM. please wait...")
        from PIL.Image import FLIP_TOP_BOTTOM
        self.engraver.load_image(self.engraveImage.transpose(FLIP_TOP_BOTTOM).getdata())
        self.update_status("Uploading to EEPROM. Done")

    def run(self):
        # tk main loop
        self.tk.mainloop()
