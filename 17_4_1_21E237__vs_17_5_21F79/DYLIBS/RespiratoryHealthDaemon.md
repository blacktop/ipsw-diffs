## RespiratoryHealthDaemon

> `/System/Library/PrivateFrameworks/RespiratoryHealthDaemon.framework/RespiratoryHealthDaemon`

```diff

-4146.4.18.0.0
+4146.5.13.0.0
   __TEXT.__text: 0x541c
   __TEXT.__auth_stubs: 0x450
   __TEXT.__objc_methlist: 0x624
   __TEXT.__const: 0x88
-  __TEXT.__oslogstring: 0x845
+  __TEXT.__oslogstring: 0x840
   __TEXT.__cstring: 0x501
-  __TEXT.__unwind_info: 0x1c4
+  __TEXT.__unwind_info: 0x1bc
   __TEXT.__objc_classname: 0x233
-  __TEXT.__objc_methname: 0x240a
+  __TEXT.__objc_methname: 0x2400
   __TEXT.__objc_methtype: 0x678
   __TEXT.__objc_stubs: 0x1540
   __DATA_CONST.__got: 0xb0
Symbols:
+ -[HDRespiratoryProfileExtension _updateBackgroundRecordingSettings]
+ -[HDRespiratoryProfileExtension _updateBackgroundRecordingSettings].cold.1
+ _objc_msgSend$_updateBackgroundRecordingSettings
+ _objc_msgSend$backgroundRecordingsDuringSleepMode
+ _objc_msgSend$backgroundRecordingsDuringTheaterMode
+ _objc_msgSend$backgroundRecordingsEnabled
+ _objc_msgSend$setBackgroundRecordingsEnabled:
- -[HDRespiratoryProfileExtension _updateBackgroundMeasurmentsSettings]
- -[HDRespiratoryProfileExtension _updateBackgroundMeasurmentsSettings].cold.1
- _objc_msgSend$_updateBackgroundMeasurmentsSettings
- _objc_msgSend$backgroundMeasurementsDuringSleepMode
- _objc_msgSend$backgroundMeasurementsDuringTheaterMode
- _objc_msgSend$backgroundMeasurementsEnabled
- _objc_msgSend$setBackgroundMeasurementsEnabled:
CStrings:
+ "[%{public}@] No updates to background recordings"
+ "[%{public}@] Updating background recordings setting from %{BOOL}d to %{BOOL}d, isSupported = %@, isOxygenSaturationDisabled = %@ isBloodOxygenAgeGated = %{BOOL}d"
+ "_updateBackgroundRecordingSettings"
+ "backgroundRecordingsDuringSleepMode"
+ "backgroundRecordingsDuringTheaterMode"
+ "backgroundRecordingsEnabled"
+ "setBackgroundRecordingsEnabled:"
- "[%{public}@] No updates to background measuremments"
- "[%{public}@] Updating background measurements setting from %{BOOL}d to %{BOOL}d, isSupported = %@, isOxygenSaturationDisabled = %@ isBloodOxygenAgeGated = %{BOOL}d"
- "_updateBackgroundMeasurmentsSettings"
- "backgroundMeasurementsDuringSleepMode"
- "backgroundMeasurementsDuringTheaterMode"
- "backgroundMeasurementsEnabled"
- "setBackgroundMeasurementsEnabled:"

```
