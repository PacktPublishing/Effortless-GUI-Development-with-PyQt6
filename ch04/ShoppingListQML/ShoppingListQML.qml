import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

ApplicationWindow {
  visible: true
  width: 280
  height: 180
  title: qsTr("Shopping List App in QML")

  ColumnLayout {
    anchors.fill: parent
    anchors.margins: 10

    Label { text: qsTr("Items:") }

    RowLayout {
      Layout.margins: 5

      ColumnLayout {
        CheckBox { text: qsTr("Apples") }
        CheckBox { text: qsTr("Bread") }
        CheckBox { text: qsTr("Milk") }
      }

      ColumnLayout {
        RadioButton { text: qsTr("Cake") }
        RadioButton { text: qsTr("Ice cream") }
        RadioButton { text: qsTr("Pack of donuts") }
      }
    }

    RowLayout {
      Label { text: qsTr("Buy at: ") }
      ComboBox {
        model: [
          qsTr("Local store"),
          qsTr("Supermarket"),
          qsTr("23/7"),
          qsTr("Order delivery")
        ]
      }
    }
  }
}
