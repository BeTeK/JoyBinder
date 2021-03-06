@echo off
echo "Generating MainWindow.ui"
call pyuic5 ui\MainDialog.ui > src\ui\MainWindowUI.py

echo "Generating ButtonForm.ui"
call pyuic5 ui\ButtonForm.ui > src\ui\ButtonFormUI.py

echo "Generating JoystickWidget.ui"
call pyuic5 ui\JoystickWidget.ui > src\ui\JoystickWidgetUI.py

echo "Generating AxisWidget.ui"
call pyuic5 ui\AxisWidget.ui > src\ui\AxisWidgetUI.py

echo "Generating JoyMappingsDialog.ui"
call pyuic5 ui\JoyMappingsDialog.ui > src\ui\JoyMappingsDialogUI.py

echo "Generating ProfileOptions.ui"
call pyuic5 ui\ProfileOptions.ui > src\ui\ProfileOptionsUI.py

echo "Generating ExpertEditor.ui"
call pyuic5 ui\ExpertEditor.ui > src\ui\ExpertEditorUI.py

