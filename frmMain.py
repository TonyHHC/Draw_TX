# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.9.0 Jan  9 2020)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class frmMain
###########################################################################

class frmMain ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"TX Research", pos = wx.DefaultPosition, size = wx.Size( 1024,713 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.m_panelSub0 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer1.Add( self.m_panelSub0, 2, wx.EXPAND|wx.ALL, 5 )

		self.m_panelSub1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer1.Add( self.m_panelSub1, 1, wx.EXPAND|wx.ALL, 5 )

		self.m_panelSub2 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer1.Add( self.m_panelSub2, 1, wx.EXPAND|wx.ALL, 5 )

		self.m_scrollBarDate = wx.ScrollBar( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.SB_HORIZONTAL )
		bSizer1.Add( self.m_scrollBarDate, 0, wx.ALIGN_BOTTOM|wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()
		self.m_toolBar2 = self.CreateToolBar( wx.TB_HORIZONTAL, wx.ID_ANY )
		self.m_txtDrawInterval = wx.StaticText( self.m_toolBar2, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_txtDrawInterval.Wrap( -1 )

		self.m_toolBar2.AddControl( self.m_txtDrawInterval )
		self.m_toolBar2.Realize()


		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_PAINT, self.OnPaint )
		self.Bind( wx.EVT_SIZE, self.OnSize )
		self.m_scrollBarDate.Bind( wx.EVT_SCROLL_CHANGED, self.OnScrollChanged )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def OnPaint( self, event ):
		event.Skip()

	def OnSize( self, event ):
		event.Skip()

	def OnScrollChanged( self, event ):
		event.Skip()


