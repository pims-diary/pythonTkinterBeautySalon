from Resources.Common.Root import root


def destroy_child_view(master):
    """ Destroys all child widgets of master """
    for i in master.winfo_children():
        i.destroy()


def exit_app():
    """ Terminate the App """
    root.destroy()
