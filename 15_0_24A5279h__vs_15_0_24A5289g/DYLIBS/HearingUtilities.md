## HearingUtilities

> `/System/Library/PrivateFrameworks/HearingUtilities.framework/Versions/A/HearingUtilities`

```diff

-442.1.0.0.0
-  __TEXT.__text: 0x6e260
+444.2.0.0.0
+  __TEXT.__text: 0x6fc50
   __TEXT.__auth_stubs: 0x940
-  __TEXT.__objc_methlist: 0x4578
+  __TEXT.__objc_methlist: 0x45e0
   __TEXT.__const: 0x1f8
-  __TEXT.__gcc_except_tab: 0x1d00
-  __TEXT.__cstring: 0x8782
+  __TEXT.__gcc_except_tab: 0x1e54
+  __TEXT.__cstring: 0x88d6
   __TEXT.__oslogstring: 0x15da
   __TEXT.__dlopen_cstrs: 0x1b2
-  __TEXT.__unwind_info: 0x1678
-  __TEXT.__objc_classname: 0x50f
-  __TEXT.__objc_methname: 0xc0ea
+  __TEXT.__unwind_info: 0x1700
+  __TEXT.__objc_classname: 0x514
+  __TEXT.__objc_methname: 0xc19b
   __TEXT.__objc_methtype: 0x188d
-  __TEXT.__objc_stubs: 0x8f60
-  __DATA_CONST.__got: 0x408
-  __DATA_CONST.__const: 0x728
+  __TEXT.__objc_stubs: 0x8fc0
+  __DATA_CONST.__got: 0x3f0
+  __DATA_CONST.__const: 0x780
   __DATA_CONST.__objc_classlist: 0x120
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2b28
+  __DATA_CONST.__objc_selrefs: 0x2b60
   __DATA_CONST.__objc_superrefs: 0xf8
   __DATA_CONST.__objc_arraydata: 0x218
   __AUTH_CONST.__auth_got: 0x4b0
-  __AUTH_CONST.__const: 0x27f0
-  __AUTH_CONST.__cfstring: 0x5e20
-  __AUTH_CONST.__objc_const: 0x7f98
+  __AUTH_CONST.__const: 0x29a0
+  __AUTH_CONST.__cfstring: 0x5ea0
+  __AUTH_CONST.__objc_const: 0x7fc8
   __AUTH_CONST.__objc_intobj: 0x4b0
   __AUTH_CONST.__objc_dictobj: 0x208
   __AUTH_CONST.__objc_arrayobj: 0xf0
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH.__objc_data: 0xb40
-  __DATA.__objc_ivar: 0x5dc
+  __DATA.__objc_ivar: 0x5e0
   __DATA.__data: 0x778
   __DATA.__bss: 0x230
   - /System/Library/Frameworks/AVFAudio.framework/Versions/A/AVFAudio

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2099
-  Symbols:   4815
-  CStrings:  1071
+  Functions: 2139
+  Symbols:   4870
+  CStrings:  1083
 
Symbols:
+ -[HUAccessoryHearingSyncManager deviceTypesForAvailableAddresses:]
+ -[HUAccessoryHearingSyncManager getDeviceTypesWithCompletion:]
+ -[HUAccessoryManager bluetoothController]
+ -[HUAccessoryManager bluetoothStateUpdates]
+ -[HUAccessoryManager getAddressesFromIdentifiers:withCompletion:]
+ -[HUAccessoryManager getAvailableAddressesSupportingCharacteristic:withCompletion:]
+ -[HUAccessoryManager getBluetoothState:]
+ -[HUAccessoryManager getIdentifiersFromAddresses:withCompletion:]
+ -[HUAccessoryManager registerBluetoothStateBlock:withListener:]
+ -[HUAccessoryManager setBluetoothController:]
+ -[HUAccessoryManager setBluetoothStateUpdates:]
+ -[HUAccessoryManager setupBluetoothController]
+ -[HURoutesManager setSubscribeTimer:]
+ -[HURoutesManager subscribeTimer]
+ GCC_except_table102
+ GCC_except_table108
+ GCC_except_table11
+ GCC_except_table117
+ GCC_except_table127
+ GCC_except_table129
+ GCC_except_table24
+ GCC_except_table79
+ GCC_except_table95
+ OBJC_IVAR_$_HUAccessoryManager._bluetoothController
+ OBJC_IVAR_$_HUAccessoryManager._bluetoothStateUpdates
+ OBJC_IVAR_$_HURoutesManager._subscribeTimer
+ __33-[HUAccessoryManager logMessage:]_block_invoke.25
+ __46-[HUAccessoryManager setupBluetoothController]_block_invoke.100
+ __46-[HUAccessoryManager setupBluetoothController]_block_invoke.113
+ __46-[HUAccessoryManager setupBluetoothController]_block_invoke.114
+ __46-[HUAccessoryManager setupBluetoothController]_block_invoke_2.101
+ __55-[HUAccessoryManager setNotify:forCharacteristicUUIDs:]_block_invoke.42
+ __56-[HUAccessoryHearingSyncManager listeningModeDidChange:]_block_invoke.130
+ __60-[HUAccessoryHearingSyncManager listeningModesChangedState:]_block_invoke.181
+ __60-[HUAccessoryHearingSyncManager listeningModesChangedState:]_block_invoke.188
+ __67-[HUAccessoryHearingSyncManager _registerForAccessoryManagerUpdate]_block_invoke.50
+ __67-[HUAccessoryHearingSyncManager _registerForAccessoryManagerUpdate]_block_invoke.63
+ __67-[HUAccessoryHearingSyncManager _registerForAccessoryManagerUpdate]_block_invoke.66
+ __67-[HUAccessoryHearingSyncManager _registerForAccessoryManagerUpdate]_block_invoke.74
+ __67-[HUAccessoryHearingSyncManager _registerForNearbyControllerUpdate]_block_invoke.104
+ __67-[HUAccessoryHearingSyncManager _registerForNearbyControllerUpdate]_block_invoke.112
+ __67-[HUAccessoryHearingSyncManager _registerForNearbyControllerUpdate]_block_invoke.124
+ __67-[HUAccessoryHearingSyncManager _registerForNearbyControllerUpdate]_block_invoke_2.105
+ __67-[HUAccessoryHearingSyncManager _registerForNearbyControllerUpdate]_block_invoke_2.116
+ __67-[HUAccessoryManager centralManager:didDisconnectPeripheral:error:]_block_invoke.148
+ ___26-[HUAccessoryManager init]_block_invoke
+ ___37-[HUAccessoryHearingSyncManager init]_block_invoke_2
+ ___40-[HUAccessoryManager getBluetoothState:]_block_invoke
+ ___46-[HUAccessoryManager setupBluetoothController]_block_invoke
+ ___46-[HUAccessoryManager setupBluetoothController]_block_invoke_2
+ ___46-[HUAccessoryManager setupBluetoothController]_block_invoke_3
+ ___46-[HUAccessoryManager setupBluetoothController]_block_invoke_4
+ ___46-[HUAccessoryManager setupBluetoothController]_block_invoke_5
+ ___46-[HUAccessoryManager setupBluetoothController]_block_invoke_6
+ ___49-[HUAccessoryManager removeDiscoveredAccessories]_block_invoke_3
+ ___49-[HUAccessoryManager removeDiscoveredAccessories]_block_invoke_4
+ ___49-[HUAccessoryManager updateBluetoothAvailability]_block_invoke_2
+ ___53-[HUAccessoryManager readValueForCharacteristicUUID:]_block_invoke_4
+ ___54-[HUAccessoryHearingSyncManager sendUpdateToAccessory]_block_invoke_2
+ ___56-[HUAccessoryHearingSyncManager listeningModeDidChange:]_block_invoke_2
+ ___58-[HUAccessoryManager centralManager:didConnectPeripheral:]_block_invoke
+ ___62-[HUAccessoryHearingSyncManager getDeviceTypesWithCompletion:]_block_invoke
+ ___63-[HUAccessoryManager registerBluetoothStateBlock:withListener:]_block_invoke
+ ___65-[HUAccessoryManager getAddressesFromIdentifiers:withCompletion:]_block_invoke
+ ___65-[HUAccessoryManager getAddressesFromIdentifiers:withCompletion:]_block_invoke_2
+ ___65-[HUAccessoryManager getAddressesFromIdentifiers:withCompletion:]_block_invoke_3
+ ___65-[HUAccessoryManager getIdentifiersFromAddresses:withCompletion:]_block_invoke
+ ___65-[HUAccessoryManager getIdentifiersFromAddresses:withCompletion:]_block_invoke_2
+ ___65-[HUAccessoryManager getIdentifiersFromAddresses:withCompletion:]_block_invoke_3
+ ___66-[HUAccessoryHearingSyncManager deviceTypesForAvailableAddresses:]_block_invoke
+ ___67-[HUAccessoryHearingSyncManager _registerForAccessoryManagerUpdate]_block_invoke_2
+ ___67-[HUAccessoryManager centralManager:didDisconnectPeripheral:error:]_block_invoke_3
+ ___71-[HUAccessoryManager peripheral:didUpdateValueForCharacteristic:error:]_block_invoke_3
+ ___76-[HUAccessoryManager peripheral:didDiscoverCharacteristicsForService:error:]_block_invoke_3
+ ___83-[HUAccessoryManager getAvailableAddressesSupportingCharacteristic:withCompletion:]_block_invoke
+ ___83-[HUAccessoryManager getAvailableAddressesSupportingCharacteristic:withCompletion:]_block_invoke_2
+ ___block_descriptor_40_e8_32r_e17_v16?0"NSArray"8l
+ ___block_descriptor_40_e8_32s_e22_v32?08?<v?B>16^B24l
+ ___block_descriptor_40_e8_32w_e17_v16?0"NSError"8l
+ ___block_descriptor_48_e8_32s40bs_e17_v16?0"NSArray"8l
+ ___block_descriptor_48_e8_32s40r_e17_v16?0"NSArray"8l
+ ___block_descriptor_48_e8_32s40s_e15_v32?0816^B24l
+ ___block_descriptor_48_e8_32s40s_e17_v16?0"NSArray"8l
+ ___block_descriptor_48_e8_32s40s_e22_v16?0"NSDictionary"8l
+ ___block_descriptor_48_e8_32s40s_e25_v32?0"CBDevice"8Q16^B24l
+ ___block_descriptor_48_e8_32s40w_e18_v16?0"CBDevice"8l
+ ___block_descriptor_48_e8_32s40w_e38_v24?0"CBControllerInfo"8"NSError"16l
+ ___block_descriptor_56_e8_32s40s48r_e17_v16?0"NSArray"8l
+ ___block_descriptor_56_e8_32s40s48s_e25_v32?0"NSString"8Q16^B24l
+ ___block_descriptor_56_e8_32s40s48w_e17_v16?0"NSArray"8l
+ ___block_descriptor_64_e8_32s40s48s56bs_e29_v24?0"NSArray"8"NSError"16l
+ ___block_descriptor_64_e8_32s40s48s56s_e17_v16?0"NSArray"8l
+ ___block_descriptor_64_e8_32s40s48s56w_e17_v16?0"NSArray"8l
+ ___block_descriptor_72_e8_32s40s48s56s64w_e25_v32?0"CBDevice"8Q16^B24l
+ ___copy_helper_block_e8_32s40s48s56s64w
+ ___copy_helper_block_e8_32s40s48s56w
+ ___destroy_helper_block_e8_32s40s48s56s64w
+ ___destroy_helper_block_e8_32s40s48s56w
+ __block_literal_global.115
+ __block_literal_global.53
+ __block_literal_global.77
+ __block_literal_global.85
+ _objc_msgSend$bluetoothController
+ _objc_msgSend$deviceTypesForAvailableAddresses:
+ _objc_msgSend$getAddressesFromIdentifiers:withCompletion:
+ _objc_msgSend$getAvailableAddressesSupportingCharacteristic:withCompletion:
+ _objc_msgSend$getDeviceTypesWithCompletion:
+ _objc_msgSend$getDevicesWithFlags:completionHandler:
+ _objc_msgSend$getIdentifiersFromAddresses:withCompletion:
+ _objc_msgSend$registerBluetoothStateBlock:withListener:
+ _objc_msgSend$setBluetoothStateChangedHandler:
+ _objc_msgSend$setBluetoothStateUpdates:
+ _objc_msgSend$setupBluetoothController
+ _objc_msgSend$subscribeTimer
- -[HUAccessoryHearingSyncManager deviceTypes]
- -[HUAccessoryManager bluetoothAvailabilityDidChange:]
- -[HUAccessoryManager setTipiController:]
- -[HUAccessoryManager setUuidToAddress:]
- -[HUAccessoryManager tipiController]
- -[HUAccessoryManager uuidToAddress]
- GCC_except_table21
- GCC_except_table61
- GCC_except_table89
- OBJC_IVAR_$_HUAccessoryManager._tipiController
- OBJC_IVAR_$_HUAccessoryManager._uuidToAddress
- _BluetoothDenylistStateChangedNotification
- _BluetoothDeviceConnectSuccessNotification
- _BluetoothPowerChangedNotification
- __33-[HUAccessoryManager logMessage:]_block_invoke.29
- __41-[HUAccessoryManager discoverAccessories]_block_invoke.108
- __41-[HUAccessoryManager discoverAccessories]_block_invoke.115
- __41-[HUAccessoryManager discoverAccessories]_block_invoke.96
- __49-[HUAccessoryManager updateBluetoothAvailability]_block_invoke.84
- __55-[HUAccessoryManager setNotify:forCharacteristicUUIDs:]_block_invoke.44
- __56-[HUAccessoryHearingSyncManager listeningModeDidChange:]_block_invoke.124
- __60-[HUAccessoryHearingSyncManager listeningModesChangedState:]_block_invoke.172
- __60-[HUAccessoryHearingSyncManager listeningModesChangedState:]_block_invoke.179
- __67-[HUAccessoryHearingSyncManager _registerForAccessoryManagerUpdate]_block_invoke.47
- __67-[HUAccessoryHearingSyncManager _registerForAccessoryManagerUpdate]_block_invoke.57
- __67-[HUAccessoryHearingSyncManager _registerForAccessoryManagerUpdate]_block_invoke.62
- __67-[HUAccessoryHearingSyncManager _registerForAccessoryManagerUpdate]_block_invoke.70
- __67-[HUAccessoryHearingSyncManager _registerForNearbyControllerUpdate]_block_invoke.100
- __67-[HUAccessoryHearingSyncManager _registerForNearbyControllerUpdate]_block_invoke.107
- __67-[HUAccessoryHearingSyncManager _registerForNearbyControllerUpdate]_block_invoke.118
- __67-[HUAccessoryHearingSyncManager _registerForNearbyControllerUpdate]_block_invoke_2.111
- __67-[HUAccessoryManager centralManager:didDisconnectPeripheral:error:]_block_invoke.144
- ___40-[HUAccessoryManager availableAddresses]_block_invoke
- ___41-[HUAccessoryManager discoverAccessories]_block_invoke_2
- ___44-[HUAccessoryHearingSyncManager deviceTypes]_block_invoke
- ___66-[HUAccessoryManager writeValue:forCharacteristicUUID:andAddress:]_block_invoke_3
- ___block_descriptor_40_e8_32s_e17_v16?0"NSError"8l
- ___block_descriptor_40_e8_32w_e18_v16?0"CBDevice"8l
- ___block_descriptor_40_e8_32w_e38_v24?0"CBControllerInfo"8"NSError"16l
- ___block_descriptor_48_e8_32s40r_e35_v32?0"NSString"8"NSString"16^B24l
- ___block_descriptor_48_e8_32s40s_e29_v32?0"CBPeripheral"8Q16^B24l
- ___block_descriptor_56_e8_32s40s48s_e29_v32?0"CBPeripheral"8Q16^B24l
- ___block_descriptor_56_e8_32s40s48w_e25_v32?0"CBDevice"8Q16^B24l
- ___block_descriptor_64_e8_32s40s48s56s_e26_v32?0"CBService"8Q16^B24l
- ___block_descriptor_64_e8_32s40s48s56s_e33_v32?0"CBCharacteristic"8Q16^B24l
- __block_literal_global.110
- __block_literal_global.120
- __block_literal_global.50
- __block_literal_global.73
- __block_literal_global.81
- _objc_msgSend$available
- _objc_msgSend$availableAddresses
- _objc_msgSend$denylistEnabled
- _objc_msgSend$deviceFromIdentifier:
- _objc_msgSend$deviceTypes
- _objc_msgSend$identifierFromBluetoothAddress:
- _objc_msgSend$powered
- _objc_msgSend$setUuidToAddress:
- _objc_msgSend$uuidToAddress
CStrings:
+ "-[HUAccessoryHearingSyncManager _registerForAccessoryManagerUpdate]_block_invoke_2"
+ "-[HUAccessoryHearingSyncManager _registerForNearbyControllerUpdate]_block_invoke_2"
+ "-[HUAccessoryHearingSyncManager sendUpdateToAccessory]_block_invoke_2"
+ "-[HURoutesManager mediaServerDied]_block_invoke"
+ "?"
+ "Activated bluetooth controller with error %!@(MISSING)"
+ "Found addresses %!@(MISSING)"
+ "Found identifiers %!@(MISSING)"
+ "HUAccessoryManagerBluetoothStateKey"
+ "Listening state changed %!@(MISSING)"
+ "Media server died. Register on media notifications."
+ "PoweredOff"
+ "PoweredOn"
+ "Resetting"
+ "Restricted"
+ "Skipping tipi update. Address is nil %!@(MISSING) - %!@(MISSING)"
+ "Skipping write request. Missing value %!@(MISSING), %!@(MISSING) = %!@(MISSING)"
+ "Skipping write request. No identifier found for %!@(MISSING)"
+ "Unauthorized"
+ "Unsupported"
+ "Updating BT state %!s(MISSING)"
+ "v32@?0@8@?<v@?B>16^B24"
- "-[HUAccessoryHearingSyncManager sendUpdateToAccessory]_block_invoke"
- "-[HUAccessoryManager discoverAccessories]_block_invoke"
- "-[HURoutesManager mediaServerDied]"
- "Activated tipi controller with error %!@(MISSING)"
- "Checking %!d(MISSING), %!@(MISSING) = %!@(MISSING)"
- "Listening state changed %!@(MISSING) - %!@(MISSING)"
- "Removing discovered accessories when BT turned off %!@(MISSING)"
- "Skipping tipi update. Identifier is nil %!@(MISSING) - %!@(MISSING)"
- "Writing to %!@(MISSING)"
- "v32@?0@\"NSString\"8@\"NSString\"16^B24"

```
