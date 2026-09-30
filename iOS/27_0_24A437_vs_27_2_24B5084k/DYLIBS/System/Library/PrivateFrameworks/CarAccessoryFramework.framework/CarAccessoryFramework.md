## CarAccessoryFramework

> `/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`

```diff

-542.7.0.0.0
-  __TEXT.__text: 0x106c9c
-  __TEXT.__objc_methlist: 0x1930c
+552.3.0.0.0
+  __TEXT.__text: 0x109cf0
+  __TEXT.__objc_methlist: 0x19694
   __TEXT.__const: 0x1b8
   __TEXT.__gcc_except_tab: 0x53c
-  __TEXT.__oslogstring: 0x3d35
-  __TEXT.__cstring: 0x7f7f
+  __TEXT.__oslogstring: 0x3e3a
+  __TEXT.__cstring: 0x80cb
   __TEXT.__ustring: 0x38
-  __TEXT.__unwind_info: 0x6630
+  __TEXT.__unwind_info: 0x6740
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x2740
-  __DATA_CONST.__objc_classlist: 0xde0
+  __DATA_CONST.__const: 0x27f0
+  __DATA_CONST.__objc_classlist: 0xe08
   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0x630
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x7e50
+  __DATA_CONST.__objc_selrefs: 0x7fa8
   __DATA_CONST.__objc_protorefs: 0x5d0
-  __DATA_CONST.__objc_superrefs: 0x800
-  __DATA_CONST.__objc_arraydata: 0xc4c8
-  __DATA_CONST.__got: 0xf20
-  __AUTH_CONST.__const: 0xac0
-  __AUTH_CONST.__cfstring: 0xe020
-  __AUTH_CONST.__objc_const: 0x50bf0
+  __DATA_CONST.__objc_superrefs: 0x810
+  __DATA_CONST.__objc_arraydata: 0xc578
+  __DATA_CONST.__got: 0xf40
+  __AUTH_CONST.__const: 0xae0
+  __AUTH_CONST.__cfstring: 0xe220
+  __AUTH_CONST.__objc_const: 0x51288
   __AUTH_CONST.__objc_arrayobj: 0x120
-  __AUTH_CONST.__objc_floatobj: 0x20
-  __AUTH_CONST.__objc_intobj: 0x690
-  __AUTH_CONST.__objc_doubleobj: 0x30
   __AUTH_CONST.__objc_dictobj: 0x6860
+  __AUTH_CONST.__objc_intobj: 0x690
+  __AUTH_CONST.__objc_floatobj: 0x20
+  __AUTH_CONST.__objc_doubleobj: 0x30
   __AUTH_CONST.__auth_got: 0x0
-  __AUTH.__objc_data: 0x190
-  __DATA.__objc_ivar: 0x684
+  __AUTH.__objc_data: 0x320
+  __DATA.__objc_ivar: 0x6a4
   __DATA.__data: 0x4a60
   __DATA_DIRTY.__objc_data: 0x8930
   __DATA_DIRTY.__bss: 0x128

   - /System/Library/PrivateFrameworks/GraphicsServices.framework/GraphicsServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 7815
-  Symbols:   15981
-  CStrings:  2196
+  Functions: 7890
+  Symbols:   16135
+  CStrings:  2217
 
Symbols:
+ +[CAFAccessoryTypes handlerPriorityForType:]
+ +[CAFPresetEntryCharacteristic primaryCharacteristicFormat]
+ +[CAFPresetEntryCharacteristic secondaryCharacteristicFormats]
+ +[CAFPresetEntryList presetEntryListWithArray:]
+ +[CAFPresetEntryList presetEntryListWithPresetEntrys:]
+ +[CAFPresetEntryListCharacteristic primaryCharacteristicFormat]
+ +[CAFPresetEntryListCharacteristic secondaryCharacteristicFormats]
+ +[CAFSeekToPositionControl controlIdentifier]
+ -[CAFCar accessoriesForCategory:sortedByHandlerPriority:]
+ -[CAFCar accessoryForCategory:withHandlerPriority:]
+ -[CAFDimensionManager displayUnitsService]
+ -[CAFDimensionManager setDisplayUnitsService:]
+ -[CAFDriveMode hasUserVisibleLabels]
+ -[CAFDriveMode registeredForUserVisibleLabels]
+ -[CAFDriveMode userVisibleLabelsCharacteristic]
+ -[CAFDriveMode userVisibleLabels]
+ -[CAFEqualizer valueDisabled]
+ -[CAFEqualizer valueHidden]
+ -[CAFEqualizerPresets presetEntryListCharacteristic]
+ -[CAFEqualizerPresets presetEntryList]
+ -[CAFEqualizerPresets registeredForPresetEntryList]
+ -[CAFEqualizerPresets registeredForSelectedPresetEntryIndex]
+ -[CAFEqualizerPresets selectedPresetEntryIndexCharacteristic]
+ -[CAFEqualizerPresets selectedPresetEntryIndexRange]
+ -[CAFEqualizerPresets selectedPresetEntryIndex]
+ -[CAFEqualizerPresets setSelectedPresetEntryIndex:]
+ -[CAFNowPlaying durationCharacteristic]
+ -[CAFNowPlaying durationInvalid]
+ -[CAFNowPlaying durationMeasurementRange]
+ -[CAFNowPlaying durationRange]
+ -[CAFNowPlaying duration]
+ -[CAFNowPlaying elapsedTimeCharacteristic]
+ -[CAFNowPlaying elapsedTimeInvalid]
+ -[CAFNowPlaying elapsedTimeMeasurementRange]
+ -[CAFNowPlaying elapsedTimeRange]
+ -[CAFNowPlaying elapsedTime]
+ -[CAFNowPlaying hasDuration]
+ -[CAFNowPlaying hasElapsedTime]
+ -[CAFNowPlaying hasPlaybackRate]
+ -[CAFNowPlaying hasSeekToPosition]
+ -[CAFNowPlaying playbackRateCharacteristic]
+ -[CAFNowPlaying playbackRateInvalid]
+ -[CAFNowPlaying playbackRateRange]
+ -[CAFNowPlaying playbackRate]
+ -[CAFNowPlaying registeredForDuration]
+ -[CAFNowPlaying registeredForElapsedTime]
+ -[CAFNowPlaying registeredForPlaybackRate]
+ -[CAFNowPlaying registeredForSeekToPosition]
+ -[CAFNowPlaying seekToPosition:completion:]
+ -[CAFNowPlaying seekToPositionControl]
+ -[CAFNowPlaying seekToPositionDisabled]
+ -[CAFPresetEntry .cxx_destruct]
+ -[CAFPresetEntry description]
+ -[CAFPresetEntry dictionaryRepresentation]
+ -[CAFPresetEntry disabled]
+ -[CAFPresetEntry imageIdentifier]
+ -[CAFPresetEntry initWithDictionary:]
+ -[CAFPresetEntry initWithDisabled:imageIdentifier:symbolName:userVisibleDescription:userVisibleLabel:]
+ -[CAFPresetEntry symbolName]
+ -[CAFPresetEntry userVisibleDescription]
+ -[CAFPresetEntry userVisibleLabel]
+ -[CAFPresetEntryCharacteristic formattedValue]
+ -[CAFPresetEntryCharacteristic presetEntryValue]
+ -[CAFPresetEntryCharacteristic setPresetEntryValue:]
+ -[CAFPresetEntryList .cxx_destruct]
+ -[CAFPresetEntryList arrayRepresentation]
+ -[CAFPresetEntryList countByEnumeratingWithState:objects:count:]
+ -[CAFPresetEntryList formattedValue]
+ -[CAFPresetEntryList initWithArray:]
+ -[CAFPresetEntryList initWithPresetEntrys:]
+ -[CAFPresetEntryList objectAtIndex:]
+ -[CAFPresetEntryList objectAtIndexedSubscript:]
+ -[CAFPresetEntryList parseError]
+ -[CAFPresetEntryList presetEntrys]
+ -[CAFPresetEntryListCharacteristic formattedValue]
+ -[CAFPresetEntryListCharacteristic presetEntryListValue]
+ -[CAFPresetEntryListCharacteristic setPresetEntryListValue:]
+ -[CAFSeekToPositionControl seekToPosition:completion:]
+ -[CAFSoundDistribution balanceDisabled]
+ -[CAFSoundDistribution balanceHidden]
+ -[CAFSoundDistribution fadeDisabled]
+ -[CAFSoundDistribution fadeHidden]
+ -[CAFSoundDistributionPresets presetEntryListCharacteristic]
+ -[CAFSoundDistributionPresets presetEntryList]
+ -[CAFSoundDistributionPresets registeredForPresetEntryList]
+ -[CAFSoundDistributionPresets registeredForSelectedPresetEntryIndex]
+ -[CAFSoundDistributionPresets selectedPresetEntryIndexCharacteristic]
+ -[CAFSoundDistributionPresets selectedPresetEntryIndexRange]
+ -[CAFSoundDistributionPresets selectedPresetEntryIndex]
+ -[CAFSoundDistributionPresets setSelectedPresetEntryIndex:]
+ _CAFCharacteristicTypePlaybackRate
+ _CAFCharacteristicTypePresetEntryList
+ _CAFCharacteristicTypeSelectedPresetEntryIndex
+ _CAFCharacteristicTypeUserVisibleLabels
+ _CAFControlTypeSeekToPosition
+ _CARPKeyPresetEntryDisabled
+ _CARPKeyPresetEntryImageIdentifier
+ _CARPKeyPresetEntrySymbolName
+ _CARPKeyPresetEntryUserVisibleDescription
+ _CARPKeyPresetEntryUserVisibleLabel
+ _CARPKeySeekToPositionPosition
+ _OBJC_CLASS_$_CAFPresetEntry
+ _OBJC_CLASS_$_CAFPresetEntryCharacteristic
+ _OBJC_CLASS_$_CAFPresetEntryList
+ _OBJC_CLASS_$_CAFPresetEntryListCharacteristic
+ _OBJC_CLASS_$_CAFSeekToPositionControl
+ _OBJC_IVAR_$_CAFDimensionManager._displayUnitsService
+ _OBJC_IVAR_$_CAFPresetEntry._disabled
+ _OBJC_IVAR_$_CAFPresetEntry._imageIdentifier
+ _OBJC_IVAR_$_CAFPresetEntry._symbolName
+ _OBJC_IVAR_$_CAFPresetEntry._userVisibleDescription
+ _OBJC_IVAR_$_CAFPresetEntry._userVisibleLabel
+ _OBJC_IVAR_$_CAFPresetEntryList._parseError
+ _OBJC_IVAR_$_CAFPresetEntryList._presetEntrys
+ _OBJC_METACLASS_$_CAFPresetEntry
+ _OBJC_METACLASS_$_CAFPresetEntryCharacteristic
+ _OBJC_METACLASS_$_CAFPresetEntryList
+ _OBJC_METACLASS_$_CAFPresetEntryListCharacteristic
+ _OBJC_METACLASS_$_CAFSeekToPositionControl
+ __OBJC_$_CLASS_METHODS_CAFPresetEntryCharacteristic
+ __OBJC_$_CLASS_METHODS_CAFPresetEntryList
+ __OBJC_$_CLASS_METHODS_CAFPresetEntryListCharacteristic
+ __OBJC_$_CLASS_METHODS_CAFSeekToPositionControl
+ __OBJC_$_INSTANCE_METHODS_CAFCar(Accessories|CAFNowPlaying)
+ __OBJC_$_INSTANCE_METHODS_CAFPresetEntry
+ __OBJC_$_INSTANCE_METHODS_CAFPresetEntryCharacteristic
+ __OBJC_$_INSTANCE_METHODS_CAFPresetEntryList
+ __OBJC_$_INSTANCE_METHODS_CAFPresetEntryListCharacteristic
+ __OBJC_$_INSTANCE_METHODS_CAFSeekToPositionControl
+ __OBJC_$_INSTANCE_VARIABLES_CAFPresetEntry
+ __OBJC_$_INSTANCE_VARIABLES_CAFPresetEntryList
+ __OBJC_$_PROP_LIST_CAFPresetEntry
+ __OBJC_$_PROP_LIST_CAFPresetEntryCharacteristic
+ __OBJC_$_PROP_LIST_CAFPresetEntryList
+ __OBJC_$_PROP_LIST_CAFPresetEntryListCharacteristic
+ __OBJC_CLASS_PROTOCOLS_$_CAFPresetEntryList
+ __OBJC_CLASS_RO_$_CAFPresetEntry
+ __OBJC_CLASS_RO_$_CAFPresetEntryCharacteristic
+ __OBJC_CLASS_RO_$_CAFPresetEntryList
+ __OBJC_CLASS_RO_$_CAFPresetEntryListCharacteristic
+ __OBJC_CLASS_RO_$_CAFSeekToPositionControl
+ __OBJC_METACLASS_RO_$_CAFPresetEntry
+ __OBJC_METACLASS_RO_$_CAFPresetEntryCharacteristic
+ __OBJC_METACLASS_RO_$_CAFPresetEntryList
+ __OBJC_METACLASS_RO_$_CAFPresetEntryListCharacteristic
+ __OBJC_METACLASS_RO_$_CAFSeekToPositionControl
+ ___36-[CAFPresetEntryList initWithArray:]_block_invoke
+ ___43-[CAFNowPlaying seekToPosition:completion:]_block_invoke
+ ___44+[CAFAccessoryTypes handlerPriorityForType:]_block_invoke
+ ___54-[CAFSeekToPositionControl seekToPosition:completion:]_block_invoke
+ ___57-[CAFCar accessoriesForCategory:sortedByHandlerPriority:]_block_invoke
+ ___block_descriptor_40_e8_32s_e39_q24?0"CAFAccessory"8"CAFAccessory"16ls32l8
+ _handlerPriorityForType:._handlerPriorityForType
+ _handlerPriorityForType:.onceToken
+ _kCarDataProtocolHandlerNameCenterDP
+ _kCarDataProtocolHandlerNameClusterDP
+ _kCarDataProtocolHandlerNameCommunicationPlugin
+ _kCarDataProtocolHandlerNamePassengerDP
+ _kCarDataProtocolHandlerNameSecondaryClusterDP
+ _objc_msgSend$accessoriesForCategory:sortedByHandlerPriority:
+ _objc_msgSend$accessoryForCategory:withHandlerPriority:
+ _objc_msgSend$driveModeService:didUpdateUserVisibleLabels:
+ _objc_msgSend$equalizerPresetsService:didUpdatePresetEntryList:
+ _objc_msgSend$equalizerPresetsService:didUpdateSelectedPresetEntryIndex:
+ _objc_msgSend$handlerPriorityForType:
+ _objc_msgSend$hasUserVisibleLabels
+ _objc_msgSend$imageIdentifier
+ _objc_msgSend$initWithPresetEntrys:
+ _objc_msgSend$nowPlayingService:didUpdateDuration:
+ _objc_msgSend$nowPlayingService:didUpdateElapsedTime:
+ _objc_msgSend$nowPlayingService:didUpdatePlaybackRate:
+ _objc_msgSend$nowPlayingServiceDidUpdateSeekToPosition:
+ _objc_msgSend$playbackRate
+ _objc_msgSend$playbackRateCharacteristic
+ _objc_msgSend$presetEntryList
+ _objc_msgSend$presetEntryListCharacteristic
+ _objc_msgSend$presetEntryListValue
+ _objc_msgSend$presetEntryListWithArray:
+ _objc_msgSend$presetEntryValue
+ _objc_msgSend$presetEntrys
+ _objc_msgSend$seekToPosition:completion:
+ _objc_msgSend$seekToPositionControl
+ _objc_msgSend$selectedPresetEntryIndex
+ _objc_msgSend$selectedPresetEntryIndexCharacteristic
+ _objc_msgSend$setDisplayUnitsService:
+ _objc_msgSend$sortedArrayWithOptions:usingComparator:
+ _objc_msgSend$soundDistributionPresetsService:didUpdatePresetEntryList:
+ _objc_msgSend$soundDistributionPresetsService:didUpdateSelectedPresetEntryIndex:
+ _objc_msgSend$userVisibleLabels
+ _objc_msgSend$userVisibleLabelsCharacteristic
- -[CAFEqualizerPresets hasPresetLabel]
- -[CAFEqualizerPresets presetLabelCharacteristic]
- -[CAFEqualizerPresets presetLabel]
- -[CAFEqualizerPresets registeredForPresetLabel]
- -[CAFEqualizerPresets registeredForSelectSettingEntryList]
- -[CAFEqualizerPresets registeredForSelectedEntryIndex]
- -[CAFEqualizerPresets selectSettingEntryListCharacteristic]
- -[CAFEqualizerPresets selectSettingEntryList]
- -[CAFEqualizerPresets selectedEntryIndexCharacteristic]
- -[CAFEqualizerPresets selectedEntryIndexRange]
- -[CAFEqualizerPresets selectedEntryIndex]
- -[CAFEqualizerPresets setSelectedEntryIndex:]
- -[CAFSoundDistributionPresets hasPresetLabel]
- -[CAFSoundDistributionPresets presetLabelCharacteristic]
- -[CAFSoundDistributionPresets presetLabel]
- -[CAFSoundDistributionPresets registeredForPresetLabel]
- -[CAFSoundDistributionPresets registeredForSelectSettingEntryList]
- -[CAFSoundDistributionPresets registeredForSelectedEntryIndex]
- -[CAFSoundDistributionPresets selectSettingEntryListCharacteristic]
- -[CAFSoundDistributionPresets selectSettingEntryList]
- -[CAFSoundDistributionPresets selectedEntryIndexCharacteristic]
- -[CAFSoundDistributionPresets selectedEntryIndexRange]
- -[CAFSoundDistributionPresets selectedEntryIndex]
- -[CAFSoundDistributionPresets setSelectedEntryIndex:]
- GCC_except_table16
- _CAFCharacteristicTypePresetLabel
- __OBJC_$_INSTANCE_METHODS_CAFCar(CAFNowPlaying|Accessories)
- _objc_msgSend$equalizerPresetsService:didUpdatePresetLabel:
- _objc_msgSend$equalizerPresetsService:didUpdateSelectSettingEntryList:
- _objc_msgSend$equalizerPresetsService:didUpdateSelectedEntryIndex:
- _objc_msgSend$hasPresetLabel
- _objc_msgSend$presetLabel
- _objc_msgSend$presetLabelCharacteristic
- _objc_msgSend$soundDistributionPresetsService:didUpdatePresetLabel:
- _objc_msgSend$soundDistributionPresetsService:didUpdateSelectSettingEntryList:
- _objc_msgSend$soundDistributionPresetsService:didUpdateSelectedEntryIndex:
CStrings:
+ "!1"
+ "%{public}@ %s observing DisplayUnits on %{public}@ (%{public}@)"
+ "%{public}@ has no %{public}@ accessory on any preferred handler %{public}@, falling back to the accessory on %{public}@"
+ "%{public}@: Error parsing dictionary from PresetEntryList array - %{public}@"
+ "0x000000000F00004F"
+ "0x0000000032000036"
+ "0x0000000033000012"
+ "0x0000000033000013"
+ "0x0000000041000026"
+ "<%@: %p { %@: %d, %@: %@, %@: %@, %@: %@, %@: %@ }>"
+ "Center_Display"
+ "Homescreen"
+ "Passenger_Display"
+ "PlaybackRate"
+ "PresetEntry"
+ "PresetEntryList"
+ "SeekToPosition"
+ "SelectedPresetEntryIndex"
+ "Siri"
+ "UserVisibleLabels"
+ "imageIdentifier"
+ "position"
+ "q24@?0@\"CAFAccessory\"8@\"CAFAccessory\"16"
- "0x0000000033000010"
- "PresetLabel"
```
