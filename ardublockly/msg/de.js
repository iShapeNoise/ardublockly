var Ardublockly = Ardublockly || {};
Ardublockly.LOCALISED_TEXT = {
  translationLanguage: "Deutsch",
  title: "Ardublockly",
  blocks: "Blöcke",
  /* Menu */
  open: "Öffnen",
  save: "Speichern",
  deleteAll: "Alles löschen",
  settings: "Einstellungen",
  documentation: "Dokumentation",
  reportBug: "Report Bug",
  examples: "Beispiele",
  /* Settings */
  compilerLocation: "Arduino Verzeichnis",
  compilerLocationDefault: "Arduino Verzeichnis unbekannt",
  sketchFolder: "Sketch Verzeichnis",
  sketchFolderDefault: "Sketch Verzeichnis unbekannt",
  arduinoBoard: "Arduino Board",
  arduinoBoardDefault: "Arduino Board unbekannt",
  comPort: "COM Port",
  comPortDefault: "COM Port unbekannt",
  defaultIdeButton: "Default IDE Taste",
  defaultIdeButtonDefault: "IDE Optionen unbekannt",
  language: "Sprache",
  languageDefault: "Sprache unbekannt",
  sketchName: "Sketch Name",
  /* Arduino console output */
  arduinoOpMainTitle: "Arduino IDE Code",
  arduinoOpWaiting: "Warte auf den Arduino Code...",
  arduinoOpUploadedTitle: "Sketch erfolgreich geladen",
  arduinoOpVerifiedTitle: "Sketch erfolgreich verifiziert",
  arduinoOpOpenedTitle: "Sketch in Arduino IDE geöffnet",
  arduinoOpOpenedBody: "Der Sketch sollte in der Arduino IDE geladen sein.",
  arduinoOpErrorTitle: "Es ist ein Fehler aufgetreten",
  arduinoOpErrorIdContext_0: "Keine Fehler.",
  arduinoOpErrorIdContext_1: "Kompilieren oder Hochladen fehlgeschlagen.",
  arduinoOpErrorIdContext_2: "Sketch nicht gefunden.",
  arduinoOpErrorIdContext_3: "Ungültiges Argument.",
  arduinoOpErrorIdContext_4: "Präferenz weitergegen zu 'get-pref' existiert nicht.",
  arduinoOpErrorIdContext_5: "Nicht klar, aber Arduino IDE zeigt manchmal Fehler.",
  arduinoOpErrorIdContext_50: "Unerwarteter Fehler von Arduino IDE",
  arduinoOpErrorIdContext_51: "Konnte Sketch Datei nicht erzeugen",
  arduinoOpErrorIdContext_52: "Ungültiger Pfad um Sketch Datei intern zu erzeugen",
  arduinoOpErrorIdContext_53: "Unable to find Arduino IDE<br>" +
                              "The compiler directory has not been set correctly.<br>" +
                              "Please ensure the path is correct in the Settings.",
  arduinoOpErrorIdContext_54: "What should we do with the Sketch?<br>" +
                              "The launch IDE option has not been set.<br>" +
                              "Please select an IDE option in the Settings.",
  arduinoOpErrorIdContext_55: "Serial Port unavailable<br>" +
                              "The Serial Port is not accessible.<br>" +
                              "Please check if the Arduino is correctly connected to the PC and select the Serial Port in the Settings.",
  arduinoOpErrorIdContext_56: "Unknown Arduino Board<br>" +
                              "The Arduino Board has not been set.<br>" +
                              "Please select the appropriate Arduino Board from the settings.",
  arduinoOpErrorIdContext_52: "Unexpected server error.",
  arduinoOpErrorIdContext_64: "Unable to parse sent JSON.",
  arduinoOpErrorUnknown: "Unexpected error",
  /* Modals */
  noServerTitle: "Ardublockly app not running",
  noServerTitleBody: "<p>For all the Ardublockly features to be enabled, the Ardublockly desktop application must be running locally on your computer.</p>" +
                     "<p>If you are using an online version you will not be able to configure the settings nor load the blocks code into an Arduino.</p>" +
                     "<p>Installation instruction can be found in the <a href=\"https://github.com/carlosperate/ardublockly\">Ardublockly repository</a>.</p>" +
                     "<p>Wenn Ardublockly bereits installiert ist, lese die Installationsdokumentation.</p>",
  noServerNoLangBody: "Wenn die Ardublockly Applikation nicht läuft, kann die Sprache nicht vollständig geändert werden.",
  addBlocksTitle: "Zusätzliche Blöcke",
  /* Alerts */
  loadNewBlocksTitle: "Neue Blöcke laden?",
  loadNewBlocksBody: "Laden einer neuen XML Datei wird die momentanen Blöcke von der Arbeitsfläche entfernen.<br>" +
                     "Möchtest du fortfahren?",
  discardBlocksTitle: "Blöcke löschen?",
  discardBlocksBody: "%1 Blöcke auf der Arbeitsfläche.<br>" +
                     "Bist du sicher dies zu löschen?",
  invalidXmlTitle: "Ungültiger XML",
  invalidXmlBody: "Die XML Datei wurde nicht erfolgreich in Blöcke analysiert. Bitte überprüfe den XML code und versuche es erneut.",
  /* Tooltips */
  uploadingSketch: "Lade Sketch in den Arduino...",
  uploadSketch: "Lade Sketch zum Arduino",
  verifyingSketch: "Verifiziere Sketch...",
  verifySketch: "Verifiziere den Sketch",
  openingSketch: "Öffne Sketch in der Arduino IDE...",
  openSketch: "Öffne Sketch in IDE",
  notImplemented: "Function not yet implemented",
  /* Prompts */
  ok: "OK",
  okay: "Okay",
  cancel: "Abbruch",
  return: "Rückgabe",
  /* Cards */
  arduinoSourceCode: "Arduino Source Code",
  blocksXml: "Blocks XML",
  /* Toolbox Categories*/
  catLogic: "Logik",
  catLoops: "Schleife",
  catMath: "Mathe",
  catText: "Text",
  catVariables: "Variable",
  catFunctions: "FunKtion",
  catInputOutput: "Eingang/Ausgang",
  catTime: "Zeit",
  catAudio: "Audio",
  catMotors: "Motor",
  catComms: "Kommunikation",
  catSensors: "Sensor",
  catDiplays: "Bildschirm",
  catVarious: "Verschieden",
};
