import gdb

#https://www.wzdftpd.net/blog/python-scripts-in-gdb.html
class AydinCommand (gdb.Command):
  """template for further commands"""

  def __init__ (self):
    super (AydinCommand, self).__init__ ("aydin",
                         gdb.COMMAND_SUPPORT,
                         gdb.COMPLETE_NONE, True)

  def invoke(self, arg, from_tty):
    print ("hello from aydin")

class AydinCommand2 (gdb.Command):
  """template for further commands"""

  def __init__ (self):
    super (AydinCommand2, self).__init__ ("aydin2",
                         gdb.COMMAND_SUPPORT,
                         gdb.COMPLETE_NONE, True)

  def invoke(self, arg, from_tty):
    arg_list = gdb.string_to_argv(arg)
    if len(arg_list) < 2:
      print("usage: wzd_print_glist list objecttype")
    return

    l = gdb.parse_and_eval(arg_list[0])

    if l.type.code != gdb.lookup_type('GList').pointer().code:
      print ("%s is not a GList*" % arg_list[0])
      return

    # iterate list and print value
    while l:
      self._print_node(l, t)
      l = l['next']

AydinCommand()
AydinCommand2()


