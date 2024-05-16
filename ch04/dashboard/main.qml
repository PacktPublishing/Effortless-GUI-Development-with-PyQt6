import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

ApplicationWindow {
  visible: true
  width: 320
  height: 480
  title: qsTr("Smart Home Dashboard")

  readonly property string degreeSign: "\u00B0"
  readonly property string playSign:   "\u23F5"
  readonly property string pauseSign:  "\u23F8"
  readonly property string nextSign:   "\u23ED"

  property bool isPlaying: false
  property string currentSong: "Pink Floyd -- Echoes"

  ColumnLayout {
    anchors.fill: parent
    anchors.margins: 20

    Label { // Header
      text: qsTr("Smart Home Dashboard")
      font.pointSize: 24
      font.bold: true
    }

    Label {
      text: qsTr("Lights")
      font.pointSize: 18
    }

    Switch {
      id: lightSwitch

      onCheckedChanged: {
        if (checked) {
          controller.turnLightsOn()
        } else {
          controller.turnLightsOff()
        }
      }
    }

    // Thermostat
    Label {
      text: qsTr("Thermostat")
      font.pointSize: 18
    }

    Slider {
      id: thermostatSlider
      Layout.fillWidth: true
      from: 15; to: 30; stepSize: 0.5
      value: 22
      onValueChanged: {
        console.log("thermostatSlider moved. New value: ", thermostatSlider.value)
      }
    }

    Label {
      text: `Temperature: ${thermostatSlider.value.toFixed(1)} ${degreeSign}C`
      font.pointSize: 18
    }

    // Home Entertainment
    ColumnLayout {
      spacing: 10

      Label {
        text: qsTr("Home Entertainment")
        font.pointSize: 18
      }

      Label {
        id: mediaStatusText
        text: isPlaying ? qsTr("[ Now playing ]") : qsTr("[ Paused ]")
        opacity: isPlaying ? 1.0 : 0
        font.pointSize: 14

        OpacityAnimator {
          target: mediaStatusText
          from: 0; to: 1; duration: 1000;
          loops: Animation.Infinite
          running: !isPlaying
          easing.type: Easing.InOutExpo
        }
      }

      Label {
        text: currentSong
        font.italic: true
        font.pointSize: 14
      }

      component MultimediaButton: Button {
        implicitWidth: 50
        font.pixelSize: 24
      }

      RowLayout {
        spacing: 10

        MultimediaButton {
          text: isPlaying ? pauseSign : playSign

          onClicked: {
            console.log("[Play/Pause] clicked")
            isPlaying = !isPlaying
          }
        }

        MultimediaButton {
          text: nextSign
          onClicked: console.log("[Next song] clicked")
        }
      }
    }
  }
}
