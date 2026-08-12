## CarAccessoryFramework

> `/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`

```diff

-540.1.0.0.0
-  __TEXT.__text: 0x10cc10
-  __TEXT.__objc_methlist: 0x1901c
+542.7.0.0.0
+  __TEXT.__text: 0x10ec40
+  __TEXT.__objc_methlist: 0x1930c
   __TEXT.__const: 0x1b8
   __TEXT.__gcc_except_tab: 0x53c
   __TEXT.__oslogstring: 0x3d35
-  __TEXT.__cstring: 0x7ef1
+  __TEXT.__cstring: 0x7f7f
   __TEXT.__ustring: 0x38
-  __TEXT.__unwind_info: 0x3bd0
+  __TEXT.__unwind_info: 0x3c30
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x2738
-  __DATA_CONST.__objc_classlist: 0xdd0
+  __DATA_CONST.__const: 0x2740
+  __DATA_CONST.__objc_classlist: 0xde0
   __DATA_CONST.__objc_catlist: 0x40
-  __DATA_CONST.__objc_protolist: 0x620
+  __DATA_CONST.__objc_protolist: 0x630
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x7da0
-  __DATA_CONST.__objc_protorefs: 0x5c0
-  __DATA_CONST.__objc_superrefs: 0x7f0
-  __DATA_CONST.__objc_arraydata: 0xc218
-  __DATA_CONST.__got: 0xf10
+  __DATA_CONST.__objc_selrefs: 0x7e50
+  __DATA_CONST.__objc_protorefs: 0x5d0
+  __DATA_CONST.__objc_superrefs: 0x800
+  __DATA_CONST.__objc_arraydata: 0xc4c8
+  __DATA_CONST.__got: 0xf20
   __AUTH_CONST.__const: 0xac0
-  __AUTH_CONST.__cfstring: 0xdf20
-  __AUTH_CONST.__objc_const: 0x50188
+  __AUTH_CONST.__cfstring: 0xe020
+  __AUTH_CONST.__objc_const: 0x50bf0
   __AUTH_CONST.__objc_arrayobj: 0x120
   __AUTH_CONST.__objc_floatobj: 0x20
   __AUTH_CONST.__objc_intobj: 0x690
   __AUTH_CONST.__objc_doubleobj: 0x30
-  __AUTH_CONST.__objc_dictobj: 0x66d0
+  __AUTH_CONST.__objc_dictobj: 0x6860
   __AUTH_CONST.__auth_got: 0x0
-  __AUTH.__objc_data: 0xf0
+  __AUTH.__objc_data: 0x190
   __DATA.__objc_ivar: 0x684
-  __DATA.__data: 0x49a0
+  __DATA.__data: 0x4a60
   __DATA.__bss: 0x3d0
   __DATA_DIRTY.__objc_data: 0x8930
   __DATA_DIRTY.__bss: 0x128

   - /System/Library/PrivateFrameworks/GraphicsServices.framework/GraphicsServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 7764
-  Symbols:   15883
-  CStrings:  2188
+  Functions: 7815
+  Symbols:   15981
+  CStrings:  2196
 
Symbols:
+ +[CAFEqualizerPresets observerProtocol]
+ +[CAFEqualizerPresets serviceIdentifier]
+ +[CAFSoundDistributionPresets observerProtocol]
+ +[CAFSoundDistributionPresets serviceIdentifier]
+ -[CAFAudioSettings equalizerPresetsService]
+ -[CAFAudioSettings equalizerPresets]
+ -[CAFAudioSettings soundDistributionPresetsService]
+ -[CAFAudioSettings soundDistributionPresets]
+ -[CAFChargingTime elapsedTimeCharacteristic]
+ -[CAFChargingTime elapsedTimeInvalid]
+ -[CAFChargingTime elapsedTimeMeasurementRange]
+ -[CAFChargingTime elapsedTimeRange]
+ -[CAFChargingTime elapsedTime]
+ -[CAFChargingTime hasElapsedTime]
+ -[CAFChargingTime registeredForElapsedTime]
+ -[CAFEqualizerPresets _characteristicDidUpdate:fromGroupUpdate:]
+ -[CAFEqualizerPresets addObserver:]
+ -[CAFEqualizerPresets hasPresetLabel]
+ -[CAFEqualizerPresets name]
+ -[CAFEqualizerPresets presetLabelCharacteristic]
+ -[CAFEqualizerPresets presetLabel]
+ -[CAFEqualizerPresets registerObserver:]
+ -[CAFEqualizerPresets registeredForPresetLabel]
+ -[CAFEqualizerPresets registeredForSelectSettingEntryList]
+ -[CAFEqualizerPresets registeredForSelectedEntryIndex]
+ -[CAFEqualizerPresets removeObserver:]
+ -[CAFEqualizerPresets selectSettingEntryListCharacteristic]
+ -[CAFEqualizerPresets selectSettingEntryList]
+ -[CAFEqualizerPresets selectedEntryIndexCharacteristic]
+ -[CAFEqualizerPresets selectedEntryIndexRange]
+ -[CAFEqualizerPresets selectedEntryIndex]
+ -[CAFEqualizerPresets setSelectedEntryIndex:]
+ -[CAFEqualizerPresets unregisterObserver:]
+ -[CAFSoundDistributionPresets _characteristicDidUpdate:fromGroupUpdate:]
+ -[CAFSoundDistributionPresets addObserver:]
+ -[CAFSoundDistributionPresets hasPresetLabel]
+ -[CAFSoundDistributionPresets name]
+ -[CAFSoundDistributionPresets presetLabelCharacteristic]
+ -[CAFSoundDistributionPresets presetLabel]
+ -[CAFSoundDistributionPresets registerObserver:]
+ -[CAFSoundDistributionPresets registeredForPresetLabel]
+ -[CAFSoundDistributionPresets registeredForSelectSettingEntryList]
+ -[CAFSoundDistributionPresets registeredForSelectedEntryIndex]
+ -[CAFSoundDistributionPresets removeObserver:]
+ -[CAFSoundDistributionPresets selectSettingEntryListCharacteristic]
+ -[CAFSoundDistributionPresets selectSettingEntryList]
+ -[CAFSoundDistributionPresets selectedEntryIndexCharacteristic]
+ -[CAFSoundDistributionPresets selectedEntryIndexRange]
+ -[CAFSoundDistributionPresets selectedEntryIndex]
+ -[CAFSoundDistributionPresets setSelectedEntryIndex:]
+ -[CAFSoundDistributionPresets unregisterObserver:]
+ _CAFCharacteristicTypeElapsedTime
+ _CAFCharacteristicTypePresetLabel
+ _CAFServiceTypeEqualizerPresets
+ _CAFServiceTypeSoundDistributionPresets
+ _OBJC_CLASS_$_CAFEqualizerPresets
+ _OBJC_CLASS_$_CAFSoundDistributionPresets
+ _OBJC_METACLASS_$_CAFEqualizerPresets
+ _OBJC_METACLASS_$_CAFSoundDistributionPresets
+ __OBJC_$_CLASS_METHODS_CAFEqualizerPresets
+ __OBJC_$_CLASS_METHODS_CAFSoundDistributionPresets
+ __OBJC_$_INSTANCE_METHODS_CAFEqualizerPresets
+ __OBJC_$_INSTANCE_METHODS_CAFSoundDistributionPresets
+ __OBJC_$_PROP_LIST_CAFEqualizerPresets
+ __OBJC_$_PROP_LIST_CAFSoundDistributionPresets
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CAFEqualizerPresetsObserver
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CAFSoundDistributionPresetsObserver
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CAFEqualizerPresetsObserver
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CAFSoundDistributionPresetsObserver
+ __OBJC_$_PROTOCOL_REFS_CAFEqualizerPresetsObserver
+ __OBJC_$_PROTOCOL_REFS_CAFSoundDistributionPresetsObserver
+ __OBJC_CLASS_RO_$_CAFEqualizerPresets
+ __OBJC_CLASS_RO_$_CAFSoundDistributionPresets
+ __OBJC_LABEL_PROTOCOL_$_CAFEqualizerPresetsObserver
+ __OBJC_LABEL_PROTOCOL_$_CAFSoundDistributionPresetsObserver
+ __OBJC_METACLASS_RO_$_CAFEqualizerPresets
+ __OBJC_METACLASS_RO_$_CAFSoundDistributionPresets
+ __OBJC_PROTOCOL_$_CAFEqualizerPresetsObserver
+ __OBJC_PROTOCOL_$_CAFSoundDistributionPresetsObserver
+ __OBJC_PROTOCOL_REFERENCE_$_CAFEqualizerPresetsObserver
+ __OBJC_PROTOCOL_REFERENCE_$_CAFSoundDistributionPresetsObserver
+ _objc_msgSend$chargingTimeService:didUpdateElapsedTime:
+ _objc_msgSend$elapsedTime
+ _objc_msgSend$elapsedTimeCharacteristic
+ _objc_msgSend$elapsedTimeInvalid
+ _objc_msgSend$elapsedTimeRange
+ _objc_msgSend$equalizerPresetsService
+ _objc_msgSend$equalizerPresetsService:didUpdatePresetLabel:
+ _objc_msgSend$equalizerPresetsService:didUpdateSelectSettingEntryList:
+ _objc_msgSend$equalizerPresetsService:didUpdateSelectedEntryIndex:
+ _objc_msgSend$hasElapsedTime
+ _objc_msgSend$hasPresetLabel
+ _objc_msgSend$presetLabel
+ _objc_msgSend$presetLabelCharacteristic
+ _objc_msgSend$soundDistributionPresetsService
+ _objc_msgSend$soundDistributionPresetsService:didUpdatePresetLabel:
+ _objc_msgSend$soundDistributionPresetsService:didUpdateSelectSettingEntryList:
+ _objc_msgSend$soundDistributionPresetsService:didUpdateSelectedEntryIndex:
CStrings:
+ "0x0000000013000006"
+ "0x0000000013000007"
+ "0x0000000030000029"
+ "0x0000000033000010"
+ "ElapsedTime"
+ "EqualizerPresets"
+ "PresetLabel"
+ "SoundDistributionPresets"
```
