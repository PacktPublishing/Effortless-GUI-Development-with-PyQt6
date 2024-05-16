import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

ApplicationWindow {
  visible: true
  width: 320
  height: 150
  title: qsTr("Login Screen in QML")

  ColumnLayout {
    anchors.fill: parent
    anchors.margins: 10

    RowLayout {
      spacing: 10

      Label { text: qsTr("Username:") }

      TextField { Layout.fillWidth: true }
    }

    RowLayout {
      spacing: 10

      Label { text: qsTr("Password:") }

      TextField {
        echoMode: TextInput.Password
        Layout.fillWidth: true
      }
    }

    Button {
      text: qsTr("Login")
      Layout.columnSpan: 2
      Layout.fillWidth: true
    }
  }
}
