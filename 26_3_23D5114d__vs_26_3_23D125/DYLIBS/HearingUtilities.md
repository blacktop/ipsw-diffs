## HearingUtilities

> `/System/Library/PrivateFrameworks/HearingUtilities.framework/HearingUtilities`

```diff

 496.4.8.0.0
-  __TEXT.__text: 0x9a2ec
+  __TEXT.__text: 0x94c24
   __TEXT.__auth_stubs: 0x1140
-  __TEXT.__objc_methlist: 0x7dac
-  __TEXT.__const: 0x422
-  __TEXT.__gcc_except_tab: 0x2930
-  __TEXT.__cstring: 0x4e8b
-  __TEXT.__oslogstring: 0xa3d8
+  __TEXT.__objc_methlist: 0x7b9c
+  __TEXT.__const: 0x412
+  __TEXT.__gcc_except_tab: 0x27e8
+  __TEXT.__cstring: 0x4c7b
+  __TEXT.__oslogstring: 0x8fc5
   __TEXT.__dlopen_cstrs: 0x7a7
   __TEXT.__swift5_typeref: 0x46
   __TEXT.__swift5_capture: 0x30

   __TEXT.__swift5_reflstr: 0xb
   __TEXT.__swift5_fieldmd: 0x38
   __TEXT.__swift5_types: 0x8
-  __TEXT.__unwind_info: 0x25e8
+  __TEXT.__unwind_info: 0x24e0
   __TEXT.__eh_frame: 0x48
-  __TEXT.__objc_classname: 0x843
-  __TEXT.__objc_methname: 0x14348
-  __TEXT.__objc_methtype: 0x2246
-  __TEXT.__objc_stubs: 0xeda0
-  __DATA_CONST.__got: 0x620
-  __DATA_CONST.__const: 0x3470
-  __DATA_CONST.__objc_classlist: 0x1c0
+  __TEXT.__objc_classname: 0x829
+  __TEXT.__objc_methname: 0x13f77
+  __TEXT.__objc_methtype: 0x2212
+  __TEXT.__objc_stubs: 0xe960
+  __DATA_CONST.__got: 0x618
+  __DATA_CONST.__const: 0x3378
+  __DATA_CONST.__objc_classlist: 0x1b8
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0xe8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x49a0
-  __DATA_CONST.__objc_superrefs: 0x180
-  __DATA_CONST.__objc_arraydata: 0x430
+  __DATA_CONST.__objc_selrefs: 0x48a8
+  __DATA_CONST.__objc_superrefs: 0x178
+  __DATA_CONST.__objc_arraydata: 0x3d0
   __AUTH_CONST.__auth_got: 0x8b0
-  __AUTH_CONST.__const: 0xd98
-  __AUTH_CONST.__cfstring: 0x51c0
-  __AUTH_CONST.__objc_const: 0xa618
-  __AUTH_CONST.__objc_intobj: 0xa80
-  __AUTH_CONST.__objc_arrayobj: 0x1f8
+  __AUTH_CONST.__const: 0xd38
+  __AUTH_CONST.__cfstring: 0x5180
+  __AUTH_CONST.__objc_const: 0xa418
+  __AUTH_CONST.__objc_intobj: 0x960
   __AUTH_CONST.__objc_dictobj: 0x410
+  __AUTH_CONST.__objc_arrayobj: 0x1e0
   __AUTH_CONST.__objc_doubleobj: 0x1290
-  __AUTH.__objc_data: 0xfa8
+  __AUTH.__objc_data: 0xf58
   __AUTH.__data: 0x50
-  __DATA.__objc_ivar: 0x8fc
+  __DATA.__objc_ivar: 0x8e8
   __DATA.__data: 0xc20
-  __DATA.__bss: 0x408
+  __DATA.__bss: 0x3f8
   __DATA_DIRTY.__objc_data: 0x2d0
   __DATA_DIRTY.__bss: 0x168
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: D05FF454-B909-3A33-8985-32D810BF4F9D
-  Functions: 3592
-  Symbols:   11562
-  CStrings:  6071
+  UUID: 3DFCF42E-2B9B-30E1-AB76-DCD39F348355
+  Functions: 3514
+  Symbols:   11334
+  CStrings:  5906
 
Symbols:
+ GCC_except_table47
+ GCC_except_table58
+ GCC_except_table64
+ GCC_except_table66
+ ___44-[AXHearingAidDevice loadRequiredProperties]_block_invoke.167
+ ___46-[AXHearingAidDevice updateInputTagsAndReset:]_block_invoke.241
+ ___52-[AXHearingAidDeviceController connectToPeripheral:]_block_invoke.32
+ ___56-[AXHearingAidDeviceController cancelPendingConnections]_block_invoke.34
+ ___57-[AXHearingAidDevice peripheral:didUpdateCharacteristic:]_block_invoke.282
+ ___57-[AXHearingAidDevice peripheral:didUpdateCharacteristic:]_block_invoke.283
+ ___57-[AXHearingAidDevice peripheral:didUpdateCharacteristic:]_block_invoke.289
+ ___57-[AXHearingAidDevice peripheral:didUpdateCharacteristic:]_block_invoke.297
+ ___57-[AXHearingAidDevice peripheral:didUpdateCharacteristic:]_block_invoke_2.290
+ ___58-[AXHearingAidDeviceController pairedHearingAidsDidChange]_block_invoke.100
+ ___58-[AXHearingAidDeviceController pairedHearingAidsDidChange]_block_invoke.101
+ ___67-[AXHearingAidDevice loadProperties:forPeripheral:withRetryPeriod:]_block_invoke.165
+ ___block_descriptor_57_e8_32s40s48r_e23_v32?0"CBUUID"8Q16^B24ls32l8r48l8s40l8
+ ___block_literal_global.243
+ ___block_literal_global.248
+ ___block_literal_global.344
+ ___block_literal_global.36
+ ___block_literal_global.74
+ ___block_literal_global.89
- -[AXHearingAidDeviceController addPeripheral:toDevice:]
- -[AXHearingAidDeviceController centralManager:didDiscoverPeripheral:advertisementData:RSSI:].cold.1
- -[AXHearingAidDeviceController isLEAudioServiceInServiceUUIDs:]
- -[AXHearingAidDeviceController processConnectedIdentifiers:andLocations:]
- -[AXHearingAidDeviceController processConnectedIdentifiers:andLocations:].cold.1
- -[AXHearingAidDeviceController setupCentralManagerForLEAudio]
- -[AXHearingAidLEAudioDevice _initCharacteristicsForPeripheral:]
- -[AXHearingAidLEAudioDevice addPeripheral:]
- -[AXHearingAidLEAudioDevice addPeripheral:asLeft:]
- -[AXHearingAidLEAudioDevice availablePropertiesForPeripheral:]
- -[AXHearingAidLEAudioDevice availablePropertiesForPeripheral:].cold.1
- -[AXHearingAidLEAudioDevice availablePropertiesFromDISForPeripheral:]
- -[AXHearingAidLEAudioDevice connect]
- -[AXHearingAidLEAudioDevice connectionDidChange]
- -[AXHearingAidLEAudioDevice dealloc]
- -[AXHearingAidLEAudioDevice delayWriteProperty:forPeripheral:]
- -[AXHearingAidLEAudioDevice descriptiveProperties]
- -[AXHearingAidLEAudioDevice deviceProtocol]
- -[AXHearingAidLEAudioDevice didAddPeripheral:]
- -[AXHearingAidLEAudioDevice didLoadPersistentProperties]
- -[AXHearingAidLEAudioDevice didLoadPersistentProperties].cold.1
- -[AXHearingAidLEAudioDevice disconnectAndUnpair:]
- -[AXHearingAidLEAudioDevice discoveringServiceUUIDs]
- -[AXHearingAidLEAudioDevice discoveringServiceUUIDs].cold.1
- -[AXHearingAidLEAudioDevice earForPeripheral:]
- -[AXHearingAidLEAudioDevice earForPeripheral:].cold.1
- -[AXHearingAidLEAudioDevice isLeftEventHandlerSet]
- -[AXHearingAidLEAudioDevice isRightEventHandlerSet]
- -[AXHearingAidLEAudioDevice leftLoadedProperties]
- -[AXHearingAidLEAudioDevice loadBasicProperties]
- -[AXHearingAidLEAudioDevice loadProperties:forPeripheral:withRetryPeriod:]
- -[AXHearingAidLEAudioDevice loadProperties:forPeripheral:withRetryPeriod:].cold.1
- -[AXHearingAidLEAudioDevice loadRequiredProperties]
- -[AXHearingAidLEAudioDevice peripheral:characteristicForUUID:]
- -[AXHearingAidLEAudioDevice peripheral:characteristicForUUID:].cold.1
- -[AXHearingAidLEAudioDevice peripheralDidUpdateDeviceInfo]
- -[AXHearingAidLEAudioDevice processBTPresetsUpdate:activePreset:forEar:]
- -[AXHearingAidLEAudioDevice rightLoadedProperties]
- -[AXHearingAidLEAudioDevice sessionDidUpdateLocations:]
- -[AXHearingAidLEAudioDevice sessionDidUpdateValue:forProperty:]
- -[AXHearingAidLEAudioDevice sessionDidUpdateValue:forProperty:].cold.1
- -[AXHearingAidLEAudioDevice setBasicPropertiesLoaded]
- -[AXHearingAidLEAudioDevice setIsLeftEventHandlerSet:]
- -[AXHearingAidLEAudioDevice setIsRightEventHandlerSet:]
- -[AXHearingAidLEAudioDevice setLeftLoadedProperties:]
- -[AXHearingAidLEAudioDevice setNotify:forPeripheral:]
- -[AXHearingAidLEAudioDevice setNotify:forPeripheral:].cold.1
- -[AXHearingAidLEAudioDevice setRightLoadedProperties:]
- -[AXHearingAidLEAudioDevice setValue:forProperty:]
- -[AXHearingAidLEAudioDevice setupLoadingProperties]
- -[AXHearingAidLEAudioDevice setupUpdatesHandlerForLEAudioPeripheral:]
- -[AXHearingAidLEAudioDevice setupUpdatesHandlerForLEAudioPeripheral:].cold.1
- -[AXHearingAidLEAudioDevice updateName]
- -[AXHearingAidLEAudioDevice updateName].cold.1
- -[AXHearingAidLEAudioDevice writeValueForProperty:]
- -[AXHearingAidLEAudioDevice writeValueForProperty:].cold.1
- GCC_except_table33
- GCC_except_table59
- GCC_except_table94
- _AXLEAudioServiceUUIDString
- _OBJC_CLASS_$_AXHearingAidLEAudioDevice
- _OBJC_IVAR_$_AXHearingAidDeviceController._leAudioSessionInfo
- _OBJC_IVAR_$_AXHearingAidLEAudioDevice._isLeftEventHandlerSet
- _OBJC_IVAR_$_AXHearingAidLEAudioDevice._isRightEventHandlerSet
- _OBJC_IVAR_$_AXHearingAidLEAudioDevice._leftLoadedProperties
- _OBJC_IVAR_$_AXHearingAidLEAudioDevice._rightLoadedProperties
- _OBJC_METACLASS_$_AXHearingAidLEAudioDevice
- _OUTLINED_FUNCTION_4
- __OBJC_$_INSTANCE_METHODS_AXHearingAidLEAudioDevice
- __OBJC_$_INSTANCE_VARIABLES_AXHearingAidLEAudioDevice
- __OBJC_$_PROP_LIST_AXHearingAidLEAudioDevice
- __OBJC_CLASS_RO_$_AXHearingAidLEAudioDevice
- __OBJC_METACLASS_RO_$_AXHearingAidLEAudioDevice
- ___44-[AXHearingAidDevice loadRequiredProperties]_block_invoke.170
- ___46-[AXHearingAidDevice updateInputTagsAndReset:]_block_invoke.244
- ___52-[AXHearingAidDeviceController connectToPeripheral:]_block_invoke.35
- ___52-[AXHearingAidLEAudioDevice discoveringServiceUUIDs]_block_invoke
- ___53-[AXHearingAidLEAudioDevice setNotify:forPeripheral:]_block_invoke
- ___55-[AXHearingAidLEAudioDevice sessionDidUpdateLocations:]_block_invoke
- ___55-[AXHearingAidLEAudioDevice sessionDidUpdateLocations:]_block_invoke.cold.1
- ___55-[AXHearingAidLEAudioDevice sessionDidUpdateLocations:]_block_invoke.cold.2
- ___56-[AXHearingAidDeviceController cancelPendingConnections]_block_invoke.37
- ___57-[AXHearingAidDevice peripheral:didUpdateCharacteristic:]_block_invoke.285
- ___57-[AXHearingAidDevice peripheral:didUpdateCharacteristic:]_block_invoke.286
- ___57-[AXHearingAidDevice peripheral:didUpdateCharacteristic:]_block_invoke.295
- ___57-[AXHearingAidDevice peripheral:didUpdateCharacteristic:]_block_invoke.300
- ___57-[AXHearingAidDevice peripheral:didUpdateCharacteristic:]_block_invoke_2.296
- ___58-[AXHearingAidDeviceController pairedHearingAidsDidChange]_block_invoke.102
- ___58-[AXHearingAidDeviceController pairedHearingAidsDidChange]_block_invoke.103
- ___61-[AXHearingAidDeviceController setupCentralManagerForLEAudio]_block_invoke
- ___61-[AXHearingAidDeviceController setupCentralManagerForLEAudio]_block_invoke.cold.1
- ___62-[AXHearingAidLEAudioDevice delayWriteProperty:forPeripheral:]_block_invoke
- ___62-[AXHearingAidLEAudioDevice delayWriteProperty:forPeripheral:]_block_invoke.50
- ___62-[AXHearingAidLEAudioDevice delayWriteProperty:forPeripheral:]_block_invoke.50.cold.1
- ___62-[AXHearingAidLEAudioDevice delayWriteProperty:forPeripheral:]_block_invoke.cold.1
- ___63-[AXHearingAidDeviceController isLEAudioServiceInServiceUUIDs:]_block_invoke
- ___67-[AXHearingAidDevice loadProperties:forPeripheral:withRetryPeriod:]_block_invoke.168
- ___69-[AXHearingAidLEAudioDevice availablePropertiesFromDISForPeripheral:]_block_invoke
- ___69-[AXHearingAidLEAudioDevice availablePropertiesFromDISForPeripheral:]_block_invoke_2
- ___69-[AXHearingAidLEAudioDevice setupUpdatesHandlerForLEAudioPeripheral:]_block_invoke
- ___73-[AXHearingAidDeviceController processConnectedIdentifiers:andLocations:]_block_invoke
- ___73-[AXHearingAidDeviceController processConnectedIdentifiers:andLocations:]_block_invoke.cold.1
- ___73-[AXHearingAidDeviceController processConnectedIdentifiers:andLocations:]_block_invoke.cold.2
- ___73-[AXHearingAidDeviceController processConnectedIdentifiers:andLocations:]_block_invoke.cold.3
- ___73-[AXHearingAidDeviceController processConnectedIdentifiers:andLocations:]_block_invoke.cold.4
- ___block_descriptor_40_e8_32s_e33_v32?0"NSUUID"8"NSNumber"16^B24ls32l8
- ___block_descriptor_48_e8_32s40r_e23_v32?0"CBUUID"8Q16^B24ls32l8r40l8
- ___block_descriptor_48_e8_32s40r_e33_v32?0"CBCharacteristic"8Q16^B24lr40l8s32l8
- ___block_descriptor_48_e8_32s40w_e31_v16?0"CBLEAudioSessionEvent"8ls32l8w40l8
- ___block_descriptor_48_e8_32s40w_e57_v24?0"CBPeripheral"8"CBLEAudioPeripheralUpdateEvent"16ls32l8w40l8
- ___block_descriptor_56_e8_32s40s48r_e26_v32?0"CBService"8Q16^B24ls32l8r48l8s40l8
- ___block_descriptor_65_e8_32s40s48s56r_e23_v32?0"CBUUID"8Q16^B24ls32l8r56l8s40l8s48l8
- ___block_literal_global.237
- ___block_literal_global.246
- ___block_literal_global.251
- ___block_literal_global.347
- ___block_literal_global.49
- ___block_literal_global.52
- ___block_literal_global.61
- ___block_literal_global.91
- _objc_msgSend$activePreset
- _objc_msgSend$addPeripheral:toDevice:
- _objc_msgSend$audioSessionIdentifier
- _objc_msgSend$connectedIdentifiers
- _objc_msgSend$earForPeripheral:
- _objc_msgSend$error
- _objc_msgSend$eventType
- _objc_msgSend$isAvailable
- _objc_msgSend$isLEAudioEnabled
- _objc_msgSend$isLEAudioServiceInServiceUUIDs:
- _objc_msgSend$isLeftEventHandlerSet
- _objc_msgSend$isRightEventHandlerSet
- _objc_msgSend$isWritable
- _objc_msgSend$locations
- _objc_msgSend$presetIndex
- _objc_msgSend$presetName
- _objc_msgSend$presetResults
- _objc_msgSend$processBTPresetsUpdate:activePreset:forEar:
- _objc_msgSend$processConnectedIdentifiers:andLocations:
- _objc_msgSend$sessionDidUpdateLocations:
- _objc_msgSend$sessionDidUpdateValue:forProperty:
- _objc_msgSend$sessionInfo
- _objc_msgSend$sessionState
- _objc_msgSend$setActivePreset:OptionalPresetIndex:withResponse:
- _objc_msgSend$setBasicPropertiesLoaded
- _objc_msgSend$setIsLeftEventHandlerSet:
- _objc_msgSend$setIsRightEventHandlerSet:
- _objc_msgSend$setLeAudioEventHandler:
- _objc_msgSend$setUpdateHandler:
- _objc_msgSend$setVolume:withResponse:
- _objc_msgSend$setupCentralManagerForLEAudio
- _objc_msgSend$setupLoadingProperties
- _objc_msgSend$setupUpdatesHandlerForLEAudioPeripheral:
- _objc_msgSend$updatedValue
CStrings:
- "1854"
- "@\"CBLEAudioSessionInfo\""
- "AXHearingAidLEAudioDevice"
- "BackCenter"
- "BackLeft"
- "BackRight"
- "BottomFrontCenter"
- "BottomFrontLeft"
- "BottomFrontRight"
- "CentralManager LEA 3: session connected peripherals %@"
- "FrontCenter"
- "FrontLeft"
- "FrontLeftOfCenter"
- "FrontLeftWide"
- "FrontRight"
- "FrontRightOfCenter"
- "FrontRightWide"
- "HearingAidDeviceController LEA 3: didDiscoverPeripheral %@, Created Hearing Aids device %@"
- "HearingAidDeviceController LEA 3: session added the second peripheral %@ to %@"
- "HearingAidDeviceController LEA 3: session setup"
- "HearingAidDeviceController LEA 3: session update - ID %@, state %@"
- "HearingAidDeviceController LEA 3: session update - event %@ error %@"
- "HearingAidDeviceController LEA 3: session update - eventType %@, connectedIdentifiers %@, locations %@"
- "HearingAidDeviceController: Scanning LEA 3"
- "HearingAidLEA3Device LEA 3: Connect to %@"
- "HearingAidLEA3Device LEA 3: addPeripheral %@ %@ didAdd: %d to device:\n%@"
- "HearingAidLEA3Device LEA 3: addPeripheral: %@, didAdd: %d\n%@"
- "HearingAidLEA3Device LEA 3: availablePropertiesForPeripheral SKIP for %@"
- "HearingAidLEA3Device LEA 3: characteristicForUUID SKIP for %@"
- "HearingAidLEA3Device LEA 3: connectionDidChange, isConnecting %d %@"
- "HearingAidLEA3Device LEA 3: delayWriteProperty %@ ear %@ peripheral %@ device name %@"
- "HearingAidLEA3Device LEA 3: didLoadPersistentProperties %d %@, Left %@, Right %@"
- "HearingAidLEA3Device LEA 3: disconnectAndUnpair(%d) from \n%@"
- "HearingAidLEA3Device LEA 3: disconnectAndUnpair(%d), SKIP disconnecting/unpairing from %@ %@\n%@"
- "HearingAidLEA3Device LEA 3: loadBasicProperties SKIP for %@"
- "HearingAidLEA3Device LEA 3: loadProperties SKIP for %@ %@"
- "HearingAidLEA3Device LEA 3: loadRequiredProperties SKIP for %@"
- "HearingAidLEA3Device LEA 3: peripheral is unknown - %@"
- "HearingAidLEA3Device LEA 3: peripheral setting notify %d for peripheral: %@ - %@"
- "HearingAidLEA3Device LEA 3: peripheral setup update handler fail, device has no such peripheral - %@"
- "HearingAidLEA3Device LEA 3: peripheralDidUpdateDeviceInfo, (paired: %d %d) device info updated: %p %@, left: %@, right: %@"
- "HearingAidLEA3Device LEA 3: sessionDidUpdateLocations, session location %@ %@ %s"
- "HearingAidLEA3Device LEA 3: sessionDidUpdateLocations, session location for unknown peripheral identifier %@"
- "HearingAidLEA3Device LEA 3: sessionDidUpdateLocations, session unknown location %@ for %@"
- "HearingAidLEA3Device LEA 3: sessionDidUpdateValue %@ for property %@, wrong format error, device %@"
- "HearingAidLEA3Device LEA 3: setBasicPropertiesLoaded for %@"
- "HearingAidLEA3Device LEA 3: setNotify SKIP for %@"
- "HearingAidLEA3Device LEA 3: setValue, %@ %@ %@"
- "HearingAidLEA3Device LEA 3: setup update handler for peripheral %@, device: %@"
- "HearingAidLEA3Device LEA 3: setupLoadingProperties for %@"
- "HearingAidLEA3Device LEA 3: updateName, (paired: %d %d) name: %p %@, left: %@, right: %@"
- "HearingAidLEA3Device LEA 3: updated name %@"
- "HearingAidLEA3Device LEA 3: updated name %@, saving persistent representation - %@"
- "HearingAidLEA3Device LEA 3: writeValueForProperty SKIP for %@"
- "HearingAidLEA3Device peripheral LEA 3: LeftPrograms %@"
- "HearingAidLEA3Device peripheral LEA 3: RightPrograms %@"
- "HearingAidLEA3Device peripheral LEA 3: availablePropertiesFromDIS %@ for Peripheral %@"
- "HearingAidLEA3Device peripheral LEA 3: leftSelectedProgram %@"
- "HearingAidLEA3Device peripheral LEA 3: preset - %@ "
- "HearingAidLEA3Device peripheral LEA 3: preset available %d"
- "HearingAidLEA3Device peripheral LEA 3: preset index: %d"
- "HearingAidLEA3Device peripheral LEA 3: preset name: %s"
- "HearingAidLEA3Device peripheral LEA 3: preset writable: %d"
- "HearingAidLEA3Device peripheral LEA 3: rightSelectedProgram %@"
- "HearingAidLEA3Device peripheral LEA 3: setActivePreset %@"
- "HearingAidLEA3Device peripheral LEA 3: setActivePreset error %@"
- "HearingAidLEA3Device peripheral LEA 3: setVolume %@ adjusted %@"
- "HearingAidLEA3Device peripheral LEA 3: setVolume error %@"
- "HearingAidLEA3Device peripheral LEA 3: update %@, HA features %@"
- "HearingAidLEA3Device peripheral LEA 3: update %@, active preset %@"
- "HearingAidLEA3Device peripheral LEA 3: update %@, name preset at index: %@"
- "HearingAidLEA3Device peripheral LEA 3: update %@, presets %@, active preset index %@"
- "HearingAidLEA3Device peripheral LEA 3: update %@, volume %@"
- "HearingAidLEA3Device peripheral LEA 3: updateHandler %@ deviceType: %@, event type: %@, event: %@\n %@device: %@"
- "LEA 3"
- "LEA 3: peripheral DIS"
- "LEA 3: peripheral discovered %@\n device: %@"
- "LEA 3: session DeviceIdentifier - %@"
- "LEA 3: session device %@"
- "LEA 3: session device already has both peripherals %@"
- "LEA 3: session device is not found"
- "LEA 3: session left %@ connection requested %d"
- "LEA 3: session no connected identifiers"
- "LEA 3: session no peripherals for identifiers %@"
- "LEA 3: session not all peripherals retrieved for identifiers %@"
- "LEA 3: session peripheral1 %@\n found device %@"
- "LEA 3: session peripheral2 %@\n found device %@"
- "LEA 3: session right %@ connection requested %d"
- "LEA 3: session update - ID %@, new state %@"
- "LEA 3: session update - connected, connectedIdentifiers %@, locations %@"
- "LEA 3: session update - mic gain %@, paired HearingDevice: %@"
- "LEA 3: session update - mic mute %@"
- "LEA 3: session update - peripheral ready, connectedIdentifiers %@"
- "LEA 3: session update - unknown event %@"
- "LEA 3: session update - volume %@, paired HearingDevice: %@"
- "LEA 3: session update - volume mute %@"
- "LEA 3: session update - volume offset %@"
- "LEA 3: session updating persistent representation - %@"
- "LeftSurround"
- "LowFrequencyEffects1"
- "LowFrequencyEffects2"
- "NotAllowed"
- "RightSurround"
- "SideLeft"
- "SideRight"
- "T@\"AXHearingAidMode\",&,D"
- "T@\"NSArray\",C,D"
- "T@\"NSString\",&,D"
- "TB,N,V_isLeftEventHandlerSet"
- "TB,N,V_isRightEventHandlerSet"
- "TQ,N,V_leftLoadedProperties"
- "TQ,N,V_rightLoadedProperties"
- "Ti,D,N"
- "TopBackCenter"
- "TopBackLeft"
- "TopBackRight"
- "TopCenter"
- "TopFrontCenter"
- "TopFrontLeft"
- "TopFrontRight"
- "TopSideLeft"
- "TopSideRight"
- "_isLeftEventHandlerSet"
- "_isRightEventHandlerSet"
- "_leAudioSessionInfo"
- "_leftLoadedProperties"
- "_rightLoadedProperties"
- "activePreset"
- "addPeripheral:toDevice:"
- "audioSessionIdentifier"
- "availablePropertiesFromDISForPeripheral:"
- "connectedIdentifiers"
- "earForPeripheral:"
- "error"
- "eventType"
- "i24@0:8@16"
- "isAvailable"
- "isLEAudioEnabled"
- "isLEAudioServiceInServiceUUIDs:"
- "isLeftEventHandlerSet"
- "isRightEventHandlerSet"
- "isWritable"
- "locations"
- "presetIndex"
- "presetName"
- "presetResults"
- "processBTPresetsUpdate:activePreset:forEar:"
- "processConnectedIdentifiers:andLocations:"
- "sessionInfo"
- "sessionState"
- "setActivePreset:OptionalPresetIndex:withResponse:"
- "setIsLeftEventHandlerSet:"
- "setIsRightEventHandlerSet:"
- "setLeAudioEventHandler:"
- "setUpdateHandler:"
- "setVolume:withResponse:"
- "setupCentralManagerForLEAudio"
- "setupUpdatesHandlerForLEAudioPeripheral:"
- "updatedValue"
- "v16@?0@\"CBLEAudioSessionEvent\"8"
- "v24@?0@\"CBPeripheral\"8@\"CBLEAudioPeripheralUpdateEvent\"16"
- "v32@?0@\"NSUUID\"8@\"NSNumber\"16^B24"
- "v36@0:8@16@24i32"

```
