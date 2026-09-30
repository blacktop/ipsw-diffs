## DualSenseHIDServicePlugin

> `/System/Library/HIDPlugins/ServicePlugins/DualSenseHIDServicePlugin.plugin/DualSenseHIDServicePlugin`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_ivar`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-14.0.24.0.0
-  __TEXT.__text: 0x73e8
+14.1.2.0.0
+  __TEXT.__text: 0xa5ac
   __TEXT.__auth_stubs: 0x400
   __TEXT.__objc_stubs: 0x900
-  __TEXT.__objc_methlist: 0x494
+  __TEXT.__objc_methlist: 0x464
   __TEXT.__const: 0x4e0
-  __TEXT.__gcc_except_tab: 0x16c
-  __TEXT.__cstring: 0x553
-  __TEXT.__objc_methname: 0xf4c
-  __TEXT.__oslogstring: 0x9ef
+  __TEXT.__gcc_except_tab: 0x2d4
+  __TEXT.__cstring: 0x6e3
+  __TEXT.__objc_methname: 0xf2d
+  __TEXT.__oslogstring: 0x11ac
   __TEXT.__objc_classname: 0x9a
-  __TEXT.__objc_methtype: 0xb15
-  __TEXT.__unwind_info: 0x2b0
-  __DATA_CONST.__const: 0x308
-  __DATA_CONST.__cfstring: 0x880
+  __TEXT.__objc_methtype: 0x1002
+  __TEXT.__unwind_info: 0x3e8
+  __DATA_CONST.__const: 0xad8
+  __DATA_CONST.__cfstring: 0xc40
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x10
   __DATA_CONST.__auth_got: 0x210
-  __DATA_CONST.__got: 0x80
+  __DATA_CONST.__got: 0x90
   __DATA.__objc_const: 0x740
   __DATA.__objc_selrefs: 0x3e8
   __DATA.__objc_ivar: 0x8c

   - /System/Library/PrivateFrameworks/HID.framework/HID
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 128
-  Symbols:   90
-  CStrings:  380
+  Functions: 208
+  Symbols:   92
+  CStrings:  448
 
Symbols:
+ _OBJC_CLASS_$_NSMutableDictionary
+ _OBJC_CLASS_$_NSNull
+ _objc_retain_x5
- _memcpy
CStrings:
+ "."
+ "@\"NSNumber\"16@?0@\"DualSenseHIDServicePlugin\"8"
+ "Apply Audio '\"eac1\"' override {\n\tenableAudioControl = %{public}@\n}."
+ "Apply Audio '\"eac2\"' override {\n\tenableAudio2Control = %{public}@\n}."
+ "Apply Audio '\"ebf\"' override {\n\tbeamformingEnable = %{public}@\n}."
+ "Apply Audio '\"eec\"' override {\n\techoCancelEnable = %{public}@\n}."
+ "Apply Audio '\"ehvc\"' override {\n\tenableHeadphoneVolumeControl = %{public}@\n}."
+ "Apply Audio '\"emvc\"' override {\n\tenableMicrophoneVolumeControl = %{public}@\n}."
+ "Apply Audio '\"enc\"' override {\n\tnoiseCancelEnable = %{public}@\n}."
+ "Apply Audio '\"esvc\"' override {\n\tenableSpeakerVolumeControl = %{public}@\n}."
+ "Apply Audio '\"hm\"' override {\n\theadphoneMute = %{public}@\n}."
+ "Apply Audio '\"hv\"' override {\n\theadphoneVolume = %{public}@\n}."
+ "Apply Audio '\"is\"' override {\n\tinputPathSelection = %{public}@\n}."
+ "Apply Audio '\"mm\"' override {\n\tmicrophoneMute = %{public}@\n}."
+ "Apply Audio '\"ms\"' override {\n\tmicrophoneSelection = %{public}@\n}."
+ "Apply Audio '\"mv\"' override {\n\tmicrophoneVolume = %{public}@\n}."
+ "Apply Audio '\"os\"' override {\n\toutputPathSelection = %{public}@\n}."
+ "Apply Audio '\"ps\"' override {\n\taudioPowerSave = %{public}@\n}."
+ "Apply Audio '\"sm\"' override {\n\tspeakerMute = %{public}@\n}."
+ "Apply Audio '\"spg\"' override {\n\tspeakerCompressorPreGain = %{public}@\n}."
+ "Apply Audio '\"sv\"' override {\n\tspeakerVolume = %{public}@\n}."
+ "Apply Haptic '\"compatibleVibration1\"' override {\n\tcompatibleVibration1Enable = %{public}@\n}."
+ "Apply Haptic '\"compatibleVibration2\"' override {\n\tcompatibleVibration2Enable = %{public}@\n}."
+ "Apply Haptic '\"compatibleVibrationL\"' override {\n\tcompatibleVibrationLeft = %{public}@\n}."
+ "Apply Haptic '\"compatibleVibrationR\"' override {\n\tcompatibleVibrationRight = %{public}@\n}."
+ "Apply Haptic '\"hapticGain\"' override {\n\thapticGain = %{public}@\n}."
+ "Apply Haptic '\"hapticMute\"' override {\n\thapticMute = %{public}@\n}."
+ "Apply Haptic '\"hapticSelection\"' override {\n\thapticSelection = %{public}@\n}."
+ "Apply Haptic '\"hapticVolumeControl\"' override {\n\tenableHapticVolumeControl = %{public}@\n}."
+ "Apply Haptic '\"powerSave\"' override {\n\thapticPowerSave = %{public}@\n}."
+ "B24@?0@\"DualSenseHIDServicePlugin\"8@16"
+ "Failed to retrieve firmware info. %{public}@"
+ "Failed to retrieve sensor calibration info. %{public}@"
+ "Refresh Firmware Info"
+ "Refresh Sensor Calibration Info"
+ "Request Firmware Info"
+ "Request Firmware Info Error: %{public}@"
+ "Request Sensor Calibration Info"
+ "Request Sensor Calibration Info Error: %{public}@"
+ "Unable to send output report to DualSense - error %d"
+ "_audio"
+ "_haptic"
+ "audio"
+ "audio."
+ "compatibleVibration1"
+ "compatibleVibration2"
+ "compatibleVibrationL"
+ "compatibleVibrationR"
+ "componentsSeparatedByString:"
+ "eac1"
+ "eac2"
+ "ebf"
+ "eec"
+ "ehvc"
+ "emvc"
+ "enc"
+ "esvc"
+ "haptic"
+ "haptic."
+ "hapticGain"
+ "hapticMute"
+ "hapticSelection"
+ "hapticVolumeControl"
+ "hasPrefix:"
+ "hm"
+ "hv"
+ "is"
+ "lastObject"
+ "mm"
+ "ms"
+ "mv"
+ "os"
+ "powerSave"
+ "ps"
+ "setObject:forKey:"
+ "sm"
+ "spg"
+ "sv"
+ "unsignedIntValue"
+ "v12@?0i8"
+ "v24@0:8^{?=(?=[2C]{?=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1})CCCCC{?=b2b1b1b2b2}C{?=b1b1b1b1b1b1b1b1}{?=(AdaptiveTriggerCommandData={?=C[10C]}{?=Cb10b6b3b3b3b3b3b3b3b3b3b3b2[4C]}{?=Cb10b6b3b3b2[7C]}{?=Cb10b6b3b5[7C]}{?=Cb10b6b3b3b3b3b3b3b3b3b3b3b2[2C]C[1C]})(AdaptiveTriggerCommandData={?=C[10C]}{?=Cb10b6b3b3b3b3b3b3b3b3b3b3b2[4C]}{?=Cb10b6b3b3b2[7C]}{?=Cb10b6b3b5[7C]}{?=Cb10b6b3b3b3b3b3b3b3b3b3b3b2[2C]C[1C]})}[4C]{?=b3b1b4}{?=b3b1b4}{?=b1b1b1b5}CC{?=b2b6}{?=b2b6}{?=b1b1b1b1b1b1b2}{?=CCC}}16"
+ "v24@?0r^{?=[11c][8c]SSII[3I]SC[5C]II}8@\"NSError\"16"
+ "v24@?0r^{?=sssssssssssssssssS}8@\"NSError\"16"
+ "{?=\"buildDate\"[11c]\"buildTime\"[8c]\"firmwareType\"S\"softwareSeries\"S\"hardwareInfo\"I\"mainFirmwareVersion\"I\"deviceInfo\"[3I]\"updateVersion\"S\"updateCapabilityInfo\"C\"reserved\"[5C]\"audioSigProcFWVersion\"I\"audioCodecFWVersion\"I}"
+ "{?=\"gyroPitchBias\"s\"gyroYawBias\"s\"gyroRollBias\"s\"gyroRefPitchPlus\"s\"gyroRefPitchMinus\"s\"gyroRefYawPlus\"s\"gyroRefYawMinus\"s\"gyroRefRollPlus\"s\"gyroRefRollMinus\"s\"gyroRefSpeedPlus\"s\"gyroRefSpeedMinus\"s\"accelRefXPlus\"s\"accelRefXMinus\"s\"accelRefYPlus\"s\"accelRefYMinus\"s\"accelRefZPlus\"s\"accelRefZMinus\"s\"calibrationTemp\"S}"
+ "{?=\"overrides\"{?=\"hasAudioControl\"B\"hasAudio2Control\"B\"hasHeadphoneVolumeControl\"B\"hasSpeakerVolumeControl\"B\"hasMicrophoneVolumeControl\"B\"hasMicrophoneMute\"B\"hasSpeakerMute\"B\"hasHeadphoneMute\"B\"hasHeadphoneVolume\"B\"hasSpeakerVolume\"B\"hasMicrophoneVolume\"B\"hasOutputPathSelection\"B\"hasInputPathSelection\"B\"hasMicrophoneSelection\"B\"hasSpeakerCompressorPreGain\"B\"hasEchoCancelEnable\"B\"hasNoiseCancelEnable\"B\"hasBeamformingEnable\"B\"hasAudioPowerSave\"B\"enableAudioControl\"B\"enableAudio2Control\"B\"enableHeadphoneVolumeControl\"B\"enableSpeakerVolumeControl\"B\"enableMicrophoneVolumeControl\"B\"microphoneMute\"B\"speakerMute\"B\"headphoneMute\"B\"headphoneVolume\"C\"speakerVolume\"C\"microphoneVolume\"C\"outputPathSelection\"C\"inputPathSelection\"C\"microphoneSelection\"C\"speakerCompressorPreGain\"C\"echoCancelEnable\"B\"noiseCancelEnable\"B\"beamformingEnable\"B\"audioPowerSave\"B}}"
+ "{?=\"overrides\"{?=\"hasCompatibleVibration1Enable\"B\"hasCompatibleVibration2Enable\"B\"hasHapticVolumeControl\"B\"hasHapticMute\"B\"hasHapticSelection\"B\"hasHapticGain\"B\"hasCompatibleVibrationRight\"B\"hasCompatibleVibrationLeft\"B\"hasHapticPowerSave\"B\"compatibleVibration1Enable\"B\"compatibleVibration2Enable\"B\"enableHapticVolumeControl\"B\"hapticMute\"B\"hapticSelection\"C\"hapticGain\"C\"compatibleVibrationRight\"C\"compatibleVibrationLeft\"C\"hapticPowerSave\"B}}"
- "(Async) Unable to retrieve firmware info from DualSense - error %d"
- "(Async) Unable to retrieve sensor calibration info from DualSense - error %d"
- "CRC 32"
- "ReportID"
- "Unable to retrieve firmware info from DualSense - error %@"
- "Unable to retrieve sensor calibration info from DualSense - error %@"
- "Unable to send output report to DualSense - error %@"
- "_flashOffDuration"
- "_flashOnDuration"
- "dictionary"
- "dispatchOutputReport"
- "isVirtualDevice"
- "requestFirmwareInfo"
- "requestFirmwareInfo: %p"
- "requestSensorCalibrationInfo"
- "requestSensorCalibrationInfo: %p"
- "v24@0:8^{?={?=b1b1b1b1b1b1b1b1}{?=b1b1b1b1b1b1b1b1}CCCCC{?=b2b1b1b2b2}C{?=b1b1b1b1b1b1b1b1}{?=(AdaptiveTriggerCommandData={?=C[10C]}{?=Cb10b6b3b3b3b3b3b3b3b3b3b3b2[4C]}{?=Cb10b6b3b3b2[7C]}{?=Cb10b6b3b5[7C]}{?=Cb10b6b3b3b3b3b3b3b3b3b3b3b2[2C]C[1C]})(AdaptiveTriggerCommandData={?=C[10C]}{?=Cb10b6b3b3b3b3b3b3b3b3b3b3b2[4C]}{?=Cb10b6b3b3b2[7C]}{?=Cb10b6b3b5[7C]}{?=Cb10b6b3b3b3b3b3b3b3b3b3b3b2[2C]C[1C]})}[4C]{?=b3b1b4}C{?=b1b1b1b5}CC{?=b2b6}{?=b2b6}{?=b1b1b1b1b1b1b2}{?=CCC}[16C][8C]I}16"
- "{?=\"reportID\"C\"buildDate\"[11c]\"buildTime\"[8c]\"firmwareType\"S\"softwareSeries\"S\"hardwareInfo\"I\"mainFirmwareVersion\"I\"deviceInfo\"[3I]\"updateVersion\"S\"updateCapabilityInfo\"C\"reserved\"[5C]\"audioSigProcFWVersion\"I\"audioCodecFWVersion\"I\"crc32\"I}"
- "{?=\"reportID\"C\"gyroPitchBias\"s\"gyroYawBias\"s\"gyroRollBias\"s\"gyroRefPitchPlus\"s\"gyroRefPitchMinus\"s\"gyroRefYawPlus\"s\"gyroRefYawMinus\"s\"gyroRefRollPlus\"s\"gyroRefRollMinus\"s\"gyroRefSpeedPlus\"s\"gyroRefSpeedMinus\"s\"accelRefXPlus\"s\"accelRefXMinus\"s\"accelRefYPlus\"s\"accelRefYMinus\"s\"accelRefZPlus\"s\"accelRefZMinus\"s\"calibrationTemp\"S\"crc32\"I}"
```
