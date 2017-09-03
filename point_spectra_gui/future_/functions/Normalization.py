from point_spectra_gui.future_.util.BasicFunctionality import Basics
from point_spectra_gui.ui.Normalization import Ui_Form


class Ui_Form(Ui_Form, Basics):
    def setupUi(self, Form):
        super().setupUi(Form)
        self.connectWidgets()

    def get_widget(self):
        return self.groupBox

    def connectWidgets(self):
        pass

    def getGuiParams(self):
        return super().getGuiParams()

    def setDisabled(self, bool):
        self.get_widget().setDisabled(bool)
