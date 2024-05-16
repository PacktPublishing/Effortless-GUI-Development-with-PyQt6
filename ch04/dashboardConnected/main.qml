import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

ApplicationWindow {
  visible: true
  width: 480
  height: 480
  title: qsTr("Smart Home Dashboard")

  readonly property string degreeSign: "\u00B0"
  readonly property string playSign:   "\u23F5"
  readonly property string pauseSign:  "\u23F8"
  readonly property string nextSign:   "\u23ED"

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
      checked: smartHomeController.lightsOn

      onClicked: {
        smartHomeController.toggleLights()
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
      value: smartHomeController.temperature
      onValueChanged: {
        smartHomeController.temperature = thermostatSlider.value
      }
    }

    Label {
      text: `Temperature: ${smartHomeController.temperature.toFixed(1)} ${degreeSign}C`
      font.pointSize: 18
      color: smartHomeController.temperatureColor
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
        text: mediaController.isPlaying ? qsTr("[ Now playing ]") : qsTr("[ Paused ]")
        opacity: mediaController.isPlaying ? 1.0 : 0
        font.pointSize: 14

        OpacityAnimator {
          target: mediaStatusText
          from: 0; to: 1; duration: 1000;
          loops: Animation.Infinite
          running: !mediaController.isPlaying
          easing.type: Easing.InOutExpo
        }
      }

      Label {
        text: mediaController.currentSong
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
          text: mediaController.isPlaying ? pauseSign : playSign

          onClicked: {
            if (mediaController.isPlaying) {
              mediaController.pause()
            } else {
              mediaController.play()
            }
          }
        }

        MultimediaButton {
          text: nextSign
          onClicked: mediaController.nextSong()
        }
      }
    }
  }
}
