## DeviceAccess

> `/System/Library/PrivateFrameworks/DeviceAccess.framework/DeviceAccess`

```diff

-315.1.0.0.0
-  __TEXT.__text: 0x244d0
+320.33.1.4.0
+  __TEXT.__text: 0x274ac
   __TEXT.__auth_stubs: 0xe30
-  __TEXT.__objc_methlist: 0x2014
-  __TEXT.__cstring: 0x49c7
-  __TEXT.__gcc_except_tab: 0x6cc
-  __TEXT.__const: 0x22a
+  __TEXT.__objc_methlist: 0x249c
+  __TEXT.__cstring: 0x5197
+  __TEXT.__gcc_except_tab: 0x75c
+  __TEXT.__const: 0x24a
   __TEXT.__swift5_typeref: 0x119
   __TEXT.__oslogstring: 0x17d
   __TEXT.__swift5_capture: 0x1c

   __TEXT.__swift5_protos: 0x4
   __TEXT.__swift5_proto: 0x8
   __TEXT.__swift5_types: 0x8
-  __TEXT.__unwind_info: 0x8e0
-  __TEXT.__objc_classname: 0x309
-  __TEXT.__objc_methname: 0x4532
-  __TEXT.__objc_methtype: 0x72e
-  __TEXT.__objc_stubs: 0x2800
-  __DATA_CONST.__got: 0x298
+  __TEXT.__unwind_info: 0x938
+  __TEXT.__objc_classname: 0x362
+  __TEXT.__objc_methname: 0x5177
+  __TEXT.__objc_methtype: 0x790
+  __TEXT.__objc_stubs: 0x2ae0
+  __DATA_CONST.__got: 0x2b8
   __DATA_CONST.__const: 0x8b0
-  __DATA_CONST.__objc_classlist: 0xf0
+  __DATA_CONST.__objc_classlist: 0x108
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1078
+  __DATA_CONST.__objc_selrefs: 0x12a0
   __DATA_CONST.__objc_protorefs: 0x28
-  __DATA_CONST.__objc_superrefs: 0xb8
+  __DATA_CONST.__objc_superrefs: 0xd0
   __AUTH_CONST.__auth_got: 0x728
-  __AUTH_CONST.__const: 0x3d8
-  __AUTH_CONST.__cfstring: 0x1aa0
-  __AUTH_CONST.__objc_const: 0x3ac8
-  __AUTH_CONST.__objc_intobj: 0x78
-  __AUTH.__objc_data: 0x1e0
-  __DATA.__objc_ivar: 0x340
+  __AUTH_CONST.__const: 0x438
+  __AUTH_CONST.__cfstring: 0x2100
+  __AUTH_CONST.__objc_const: 0x4340
+  __AUTH_CONST.__objc_intobj: 0x90
+  __AUTH.__objc_data: 0x2d0
+  __DATA.__objc_ivar: 0x3c0
   __DATA.__data: 0x738
   __DATA.__bss: 0x140
   __DATA_DIRTY.__objc_data: 0x780

   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/CoreUtils.framework/CoreUtils
   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
+  - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
+  - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib
+  - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  - /usr/lib/swift/libswift_errno.dylib
-  - /usr/lib/swift/libswift_math.dylib
-  - /usr/lib/swift/libswift_signal.dylib
-  - /usr/lib/swift/libswift_stdio.dylib
-  - /usr/lib/swift/libswift_time.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
-  - /usr/lib/swift/libswiftsys_time.dylib
-  - /usr/lib/swift/libswiftunistd.dylib
-  UUID: F58FC6B3-FC06-36CF-A89E-0AE25938347E
-  Functions: 1020
-  Symbols:   3183
-  CStrings:  1893
+  - /usr/lib/swift/libswiftsimd.dylib
+  UUID: D405B6A9-829E-3EA6-AFD2-407BC008D43E
+  Functions: 1130
+  Symbols:   3479
+  CStrings:  2177
 
Symbols:
+ +[DAPropertyCompareString supportsSecureCoding]
+ +[DAUserAlert accessoryUnpairAlert:appName:]
+ -[DADevice bluetoothSetupFinished]
+ -[DADevice bluetoothSetupInProgress]
+ -[DADevice networkUnsecured]
+ -[DADevice requiresBluetoothSetup]
+ -[DADevice requiresWiFiAwareSetup]
+ -[DADevice requiresWiFiSoftAPSetup]
+ -[DADevice setBluetoothOnboardingFinished:]
+ -[DADevice setBluetoothSetupFinished:]
+ -[DADevice setBluetoothSetupInProgress:]
+ -[DADevice setDeviceUpgradeFinished:inProgress:failed:]
+ -[DADevice setNetworkUnsecured:]
+ -[DADevice setSignature:]
+ -[DADevice setUpgradeFailed:]
+ -[DADevice setUpgradeFinished:]
+ -[DADevice setUpgradeInProgress:]
+ -[DADevice setWiFiAwareOnboardingFinished:]
+ -[DADevice setWifiAwareDevicePairingID:]
+ -[DADevice setWifiAwareModelName:]
+ -[DADevice setWifiAwareOTAName:]
+ -[DADevice setWifiAwareSetupFinished:]
+ -[DADevice setWifiAwareSetupInProgress:]
+ -[DADevice setWifiAwareVendorName:]
+ -[DADevice signature]
+ -[DADevice stillTrackableWhenUnpaired]
+ -[DADevice upgradeFailed]
+ -[DADevice upgradeFinished]
+ -[DADevice upgradeInProgress]
+ -[DADevice wifiAwareDevicePairingID]
+ -[DADevice wifiAwareModelName]
+ -[DADevice wifiAwareOTAName]
+ -[DADevice wifiAwareSetupFinished]
+ -[DADevice wifiAwareSetupInProgress]
+ -[DADevice wifiAwareVendorName]
+ -[DADeviceAppAccessInfo endTime]
+ -[DADeviceAppAccessInfo setBundleIdentifier:]
+ -[DADeviceAppAccessInfo setEndTime:]
+ -[DADeviceAppAccessInfo setWifiAwarePairingID:]
+ -[DADeviceAppAccessInfo wifiAwarePairingID]
+ -[DADiscovery deviceOTANameToBroadcast]
+ -[DADiscovery respondToWiFiAwarePairingRequest:completionHandler:]
+ -[DADiscovery runOtherDiscovery]
+ -[DADiscovery setDeviceOTANameToBroadcast:]
+ -[DADiscoveryConfiguration bonjourServiceName]
+ -[DADiscoveryConfiguration bonjourTXTRecordData]
+ -[DADiscoveryConfiguration existingDeviceIdentifier]
+ -[DADiscoveryConfiguration setBonjourServiceName:]
+ -[DADiscoveryConfiguration setBonjourTXTRecordData:]
+ -[DADiscoveryConfiguration setExistingDeviceIdentifier:]
+ -[DADiscoveryConfiguration setWifiAwareModelNameMatch:]
+ -[DADiscoveryConfiguration setWifiAwarePairingID:]
+ -[DADiscoveryConfiguration setWifiAwareServiceName:]
+ -[DADiscoveryConfiguration setWifiAwareServiceType:]
+ -[DADiscoveryConfiguration setWifiAwareVendorNameMatch:]
+ -[DADiscoveryConfiguration wifiAwareModelNameMatch]
+ -[DADiscoveryConfiguration wifiAwarePairingID]
+ -[DADiscoveryConfiguration wifiAwareServiceName]
+ -[DADiscoveryConfiguration wifiAwareServiceType]
+ -[DADiscoveryConfiguration wifiAwareVendorNameMatch]
+ -[DAEventDeviceWiFiAwarePairingRequest .cxx_destruct]
+ -[DAEventDeviceWiFiAwarePairingRequest descriptionWithLevel:]
+ -[DAEventDeviceWiFiAwarePairingRequest encodeWithXPCObject:]
+ -[DAEventDeviceWiFiAwarePairingRequest initWithEventType:pairingInfo:]
+ -[DAEventDeviceWiFiAwarePairingRequest initWithXPCObject:error:]
+ -[DAEventDeviceWiFiAwarePairingRequest pairingInfo]
+ -[DAEventDeviceWiFiAwarePairingRequest setPairingInfo:]
+ -[DAPropertyCompareString .cxx_destruct]
+ -[DAPropertyCompareString compareOptions]
+ -[DAPropertyCompareString copyWithZone:]
+ -[DAPropertyCompareString descriptionWithLevel:]
+ -[DAPropertyCompareString description]
+ -[DAPropertyCompareString encodeWithCoder:]
+ -[DAPropertyCompareString encodeWithXPCObject:]
+ -[DAPropertyCompareString hash]
+ -[DAPropertyCompareString initWithCoder:]
+ -[DAPropertyCompareString initWithCoder:].cold.1
+ -[DAPropertyCompareString initWithString:compareOptions:]
+ -[DAPropertyCompareString initWithXPCObject:error:]
+ -[DAPropertyCompareString isEqual:]
+ -[DAPropertyCompareString string]
+ -[DASession appIsUsingDeviceAccess].cold.2
+ -[DASession appIsUsingDeviceAccess].cold.3
+ -[DASession appIsUsingDeviceAccess].cold.4
+ -[DASession currentDeviceCapabilities]
+ -[DASession setCurrentDeviceCapabilities:]
+ -[DAWiFiAwarePairingInfo .cxx_destruct]
+ -[DAWiFiAwarePairingInfo accept]
+ -[DAWiFiAwarePairingInfo descriptionWithLevel:]
+ -[DAWiFiAwarePairingInfo description]
+ -[DAWiFiAwarePairingInfo encodeWithXPCObject:]
+ -[DAWiFiAwarePairingInfo initWithWiFiAwareIdentifier:pairingType:]
+ -[DAWiFiAwarePairingInfo initWithXPCObject:error:]
+ -[DAWiFiAwarePairingInfo pairingType]
+ -[DAWiFiAwarePairingInfo passkey]
+ -[DAWiFiAwarePairingInfo setAccept:]
+ -[DAWiFiAwarePairingInfo setPasskey:]
+ -[DAWiFiAwarePairingInfo wifiAwareIdentifier]
+ GCC_except_table111
+ GCC_except_table140
+ GCC_except_table92
+ _DACurrentDeviceCapabilitiesToString
+ _MGGetBoolAnswer
+ _OBJC_CLASS_$_DAEventDeviceWiFiAwarePairingRequest
+ _OBJC_CLASS_$_DAPropertyCompareString
+ _OBJC_CLASS_$_DAWiFiAwarePairingInfo
+ _OBJC_IVAR_$_DADevice._bluetoothSetupFinished
+ _OBJC_IVAR_$_DADevice._bluetoothSetupInProgress
+ _OBJC_IVAR_$_DADevice._networkUnsecured
+ _OBJC_IVAR_$_DADevice._signature
+ _OBJC_IVAR_$_DADevice._upgradeFailed
+ _OBJC_IVAR_$_DADevice._upgradeFinished
+ _OBJC_IVAR_$_DADevice._upgradeInProgress
+ _OBJC_IVAR_$_DADevice._wifiAwareDevicePairingID
+ _OBJC_IVAR_$_DADevice._wifiAwareModelName
+ _OBJC_IVAR_$_DADevice._wifiAwareOTAName
+ _OBJC_IVAR_$_DADevice._wifiAwareSetupFinished
+ _OBJC_IVAR_$_DADevice._wifiAwareSetupInProgress
+ _OBJC_IVAR_$_DADevice._wifiAwareVendorName
+ _OBJC_IVAR_$_DADeviceAppAccessInfo._endTime
+ _OBJC_IVAR_$_DADeviceAppAccessInfo._wifiAwarePairingID
+ _OBJC_IVAR_$_DADiscovery._deviceOTANameToBroadcast
+ _OBJC_IVAR_$_DADiscoveryConfiguration._bonjourServiceName
+ _OBJC_IVAR_$_DADiscoveryConfiguration._bonjourTXTRecordData
+ _OBJC_IVAR_$_DADiscoveryConfiguration._existingDeviceIdentifier
+ _OBJC_IVAR_$_DADiscoveryConfiguration._wifiAwareModelNameMatch
+ _OBJC_IVAR_$_DADiscoveryConfiguration._wifiAwarePairingID
+ _OBJC_IVAR_$_DADiscoveryConfiguration._wifiAwareServiceName
+ _OBJC_IVAR_$_DADiscoveryConfiguration._wifiAwareServiceType
+ _OBJC_IVAR_$_DADiscoveryConfiguration._wifiAwareVendorNameMatch
+ _OBJC_IVAR_$_DAEventDeviceWiFiAwarePairingRequest._pairingInfo
+ _OBJC_IVAR_$_DAPropertyCompareString._compareOptions
+ _OBJC_IVAR_$_DAPropertyCompareString._string
+ _OBJC_IVAR_$_DASession._currentDeviceCapabilities
+ _OBJC_IVAR_$_DAWiFiAwarePairingInfo._accept
+ _OBJC_IVAR_$_DAWiFiAwarePairingInfo._pairingType
+ _OBJC_IVAR_$_DAWiFiAwarePairingInfo._passkey
+ _OBJC_IVAR_$_DAWiFiAwarePairingInfo._wifiAwareIdentifier
+ _OBJC_METACLASS_$_DAEventDeviceWiFiAwarePairingRequest
+ _OBJC_METACLASS_$_DAPropertyCompareString
+ _OBJC_METACLASS_$_DAWiFiAwarePairingInfo
+ _OUTLINED_FUNCTION_10
+ _OUTLINED_FUNCTION_11
+ _OUTLINED_FUNCTION_8
+ _OUTLINED_FUNCTION_9
+ __OBJC_$_CLASS_METHODS_DAPropertyCompareString
+ __OBJC_$_CLASS_PROP_LIST_DAPropertyCompareString
+ __OBJC_$_INSTANCE_METHODS_DAEventDeviceWiFiAwarePairingRequest
+ __OBJC_$_INSTANCE_METHODS_DAPropertyCompareString
+ __OBJC_$_INSTANCE_METHODS_DAWiFiAwarePairingInfo
+ __OBJC_$_INSTANCE_VARIABLES_DAEventDeviceWiFiAwarePairingRequest
+ __OBJC_$_INSTANCE_VARIABLES_DAPropertyCompareString
+ __OBJC_$_INSTANCE_VARIABLES_DAWiFiAwarePairingInfo
+ __OBJC_$_PROP_LIST_DAEventDeviceWiFiAwarePairingRequest
+ __OBJC_$_PROP_LIST_DAPropertyCompareString
+ __OBJC_$_PROP_LIST_DAWiFiAwarePairingInfo
+ __OBJC_CLASS_PROTOCOLS_$_DAPropertyCompareString
+ __OBJC_CLASS_PROTOCOLS_$_DAWiFiAwarePairingInfo
+ __OBJC_CLASS_RO_$_DAEventDeviceWiFiAwarePairingRequest
+ __OBJC_CLASS_RO_$_DAPropertyCompareString
+ __OBJC_CLASS_RO_$_DAWiFiAwarePairingInfo
+ __OBJC_METACLASS_RO_$_DAEventDeviceWiFiAwarePairingRequest
+ __OBJC_METACLASS_RO_$_DAPropertyCompareString
+ __OBJC_METACLASS_RO_$_DAWiFiAwarePairingInfo
+ ___35-[DASession appIsUsingDeviceAccess]_block_invoke
+ ___66-[DADiscovery respondToWiFiAwarePairingRequest:completionHandler:]_block_invoke
+ ___66-[DADiscovery respondToWiFiAwarePairingRequest:completionHandler:]_block_invoke.cold.1
+ ___66-[DADiscovery respondToWiFiAwarePairingRequest:completionHandler:]_block_invoke_2
+ ___66-[DADiscovery respondToWiFiAwarePairingRequest:completionHandler:]_block_invoke_2.cold.1
+ ___96+[DADeviceAccessAnalytics markState:deviceID:shared:discovery:flags:sourceApp:atTime:errorCode:]_block_invoke.171
+ ___96+[DADeviceAccessAnalytics markState:deviceID:shared:discovery:flags:sourceApp:atTime:errorCode:]_block_invoke_2.175
+ ___96+[DADeviceAccessAnalytics markState:deviceID:shared:discovery:flags:sourceApp:atTime:errorCode:]_block_invoke_6
+ ___96+[DADeviceAccessAnalytics markState:deviceID:shared:discovery:flags:sourceApp:atTime:errorCode:]_block_invoke_7
+ ___block_descriptor_168_e8_32s40s48s56s64s72s80s88s96s104s112s120s128s136s_e19_"NSDictionary"8?0ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8s96l8s104l8s112l8s120l8s128l8s136l8
+ ___block_literal_global.108
+ ___block_literal_global.119
+ ___block_literal_global.177
+ ___block_literal_global.179
+ ___block_literal_global.181
+ ___block_literal_global.183
+ ___block_literal_global.185
+ ___block_literal_global.60
+ ___block_literal_global.63
+ ___block_literal_global.76
+ ___block_literal_global.85
+ ___unnamed_2
+ ___unnamed_7
+ __swift_FORCE_LOAD_$_swiftAccelerate
+ __swift_FORCE_LOAD_$_swiftAccelerate_$_DeviceAccess
+ __swift_FORCE_LOAD_$_swiftCoreImage
+ __swift_FORCE_LOAD_$_swiftCoreImage_$_DeviceAccess
+ __swift_FORCE_LOAD_$_swiftOSLog
+ __swift_FORCE_LOAD_$_swiftOSLog_$_DeviceAccess
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_DeviceAccess
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_DeviceAccess
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_DeviceAccess
+ __swift_FORCE_LOAD_$_swiftsimd
+ __swift_FORCE_LOAD_$_swiftsimd_$_DeviceAccess
+ _objc_msgSend$bluetoothCompanyPayloadMask
+ _objc_msgSend$bluetoothServicePayloadMask
+ _objc_msgSend$bundleRecordWithBundleIdentifier:allowPlaceholder:error:
+ _objc_msgSend$compareOptions
+ _objc_msgSend$copyWithZone:
+ _objc_msgSend$decodeInt64ForKey:
+ _objc_msgSend$encodeInt64:forKey:
+ _objc_msgSend$hash
+ _objc_msgSend$infoDictionary
+ _objc_msgSend$numberWithUnsignedLongLong:
+ _objc_msgSend$objectForKey:ofClass:
+ _objc_msgSend$requiresWiFiAwareSetup
+ _objc_msgSend$runOtherDiscovery
+ _objc_msgSend$runUpgradeWithDiscovery:
+ _objc_msgSend$setWifiAwareModelNameMatch:
+ _objc_msgSend$setWifiAwareServiceName:
+ _objc_msgSend$setWifiAwareServiceType:
+ _objc_msgSend$setWifiAwareVendorNameMatch:
+ _objc_msgSend$string
+ _objc_msgSend$wifiAwareDevicePairingID
+ _objc_msgSend$wifiAwareModelNameMatch
+ _objc_msgSend$wifiAwareServiceName
+ _objc_msgSend$wifiAwareServiceType
+ _objc_msgSend$wifiAwareVendorNameMatch
+ _swift_coroFrameAlloc
- -[DADiscovery _activateDirect].cold.3
- GCC_except_table1
- GCC_except_table120
- GCC_except_table75
- GCC_except_table94
- _CUGestaltDeviceClassToString
- _GestaltGetDeviceClass
- ___96+[DADeviceAccessAnalytics markState:deviceID:shared:discovery:flags:sourceApp:atTime:errorCode:]_block_invoke.168
- ___96+[DADeviceAccessAnalytics markState:deviceID:shared:discovery:flags:sourceApp:atTime:errorCode:]_block_invoke_2.172
- ___block_descriptor_136_e8_32s40s48s56s64s72s80s88s96s104s_e19_"NSDictionary"8?0ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8s96l8s104l8
- ___block_literal_global.103
- ___block_literal_global.114
- ___block_literal_global.171
- ___block_literal_global.176
- ___block_literal_global.178
- ___block_literal_global.59
- ___block_literal_global.62
- ___block_literal_global.78
- ___unnamed_1
- ___unnamed_6
- __swift_FORCE_LOAD_$_swift_errno
- __swift_FORCE_LOAD_$_swift_errno_$_DeviceAccess
- __swift_FORCE_LOAD_$_swift_math
- __swift_FORCE_LOAD_$_swift_math_$_DeviceAccess
- __swift_FORCE_LOAD_$_swift_signal
- __swift_FORCE_LOAD_$_swift_signal_$_DeviceAccess
- __swift_FORCE_LOAD_$_swift_stdio
- __swift_FORCE_LOAD_$_swift_stdio_$_DeviceAccess
- __swift_FORCE_LOAD_$_swift_time
- __swift_FORCE_LOAD_$_swift_time_$_DeviceAccess
- __swift_FORCE_LOAD_$_swiftsys_time
- __swift_FORCE_LOAD_$_swiftsys_time_$_DeviceAccess
- __swift_FORCE_LOAD_$_swiftunistd
- __swift_FORCE_LOAD_$_swiftunistd_$_DeviceAccess
- _objc_msgSend$executeQuery:
CStrings:
+ "%@, CID 0x%X %@, DeviceOTAName:%@"
+ "%lu"
+ "-[DADiscovery respondToWiFiAwarePairingRequest:completionHandler:]_block_invoke"
+ "-[DADiscovery respondToWiFiAwarePairingRequest:completionHandler:]_block_invoke_2"
+ "1"
+ "@\"DAPropertyCompareString\""
+ "@\"DAWiFiAwarePairingInfo\""
+ "@32@0:8@16Q24"
+ "@32@0:8Q16q24"
+ "AccessorySetupUpgradeFailed"
+ "AccessorySetupUpgraded"
+ "AppSession"
+ "AppSessionPaired"
+ "Archived"
+ "DAEventDeviceWiFiAwarePairingRequest"
+ "DAEventTypeWiFiAwarePairingRequest"
+ "DAPropertyCompareString"
+ "DASession-CheckMDD"
+ "DAWiFiAwarePairingInfo"
+ "DAWiFiAwarePairingTypeInvalid"
+ "DAWiFiAwarePairingTypeJustWorks"
+ "DAWiFiAwarePairingTypeNumericComparison"
+ "DAWiFiAwarePairingTypePasskeyDisplay"
+ "DAWiFiAwarePairingTypePasskeyEntry"
+ "Device discovery configurations not provided for %@"
+ "DeviceUnpairAlertMessageKeyWLAN"
+ "DeviceUnpairAlertMessageKeyWiFi"
+ "DeviceUnpairAlertPrimaryKey"
+ "DeviceUnpairAlertSecondaryKey"
+ "DeviceUnpairAlertTitleKey"
+ "Discovery: Device missing accessory setup flag"
+ "HasBluetoothLEHID"
+ "HasWiFiAwarePublishableServices"
+ "HasWiFiAwareSubscribableServices"
+ "MDDEx"
+ "Mnm %@"
+ "NetworkUnsecured '%s'"
+ "Session: Device missing accessory setup flag"
+ "T@\"DAPropertyCompareString\",C,N,V_wifiAwareModelNameMatch"
+ "T@\"DAPropertyCompareString\",C,N,V_wifiAwareVendorNameMatch"
+ "T@\"DAWiFiAwarePairingInfo\",C,N,V_pairingInfo"
+ "T@\"NSData\",C,N,V_bonjourTXTRecordData"
+ "T@\"NSString\",&,N,V_passkey"
+ "T@\"NSString\",C,N,V_bonjourServiceName"
+ "T@\"NSString\",C,N,V_deviceOTANameToBroadcast"
+ "T@\"NSString\",C,N,V_existingDeviceIdentifier"
+ "T@\"NSString\",C,N,V_wifiAwareModelName"
+ "T@\"NSString\",C,N,V_wifiAwareOTAName"
+ "T@\"NSString\",C,N,V_wifiAwareServiceName"
+ "T@\"NSString\",C,N,V_wifiAwareVendorName"
+ "T@\"NSString\",R,C,N,V_string"
+ "T@\"NSUUID\",C,N,V_wifiAwareDevicePairingID"
+ "TB,N,V_bluetoothSetupFinished"
+ "TB,N,V_bluetoothSetupInProgress"
+ "TB,N,V_networkUnsecured"
+ "TB,N,V_upgradeFailed"
+ "TB,N,V_upgradeFinished"
+ "TB,N,V_upgradeInProgress"
+ "TB,N,V_wifiAwareSetupFinished"
+ "TB,N,V_wifiAwareSetupInProgress"
+ "TQ,N,V_currentDeviceCapabilities"
+ "TQ,N,V_wifiAwarePairingID"
+ "TQ,N,V_wifiAwareServiceType"
+ "TQ,R,N,V_compareOptions"
+ "TQ,R,N,V_wifiAwareIdentifier"
+ "Td,N,V_endTime"
+ "Tq,N,V_signature"
+ "UpgradeFailed %s"
+ "UpgradeFinished %s"
+ "UpgradeInProgress %s"
+ "Vidm %@"
+ "WF-ID %llu"
+ "WF-Sn %@"
+ "Wi-Fi Aware"
+ "Wi-Fi Aware Device already authorized"
+ "WiFiAware identifier %llu"
+ "WiFiAwarePublishableServices"
+ "WiFiAwareSubscribableServices"
+ "_bluetoothSetupFinished"
+ "_bluetoothSetupInProgress"
+ "_bonjourServiceName"
+ "_bonjourTXTRecordData"
+ "_compareOptions"
+ "_currentDeviceCapabilities"
+ "_deviceOTANameToBroadcast"
+ "_endTime"
+ "_existingDeviceIdentifier"
+ "_networkUnsecured"
+ "_signature"
+ "_string"
+ "_upgradeFailed"
+ "_upgradeFinished"
+ "_upgradeInProgress"
+ "_wifiAwareDevicePairingID"
+ "_wifiAwareIdentifier"
+ "_wifiAwareModelName"
+ "_wifiAwareModelNameMatch"
+ "_wifiAwareOTAName"
+ "_wifiAwarePairingID"
+ "_wifiAwareServiceName"
+ "_wifiAwareServiceType"
+ "_wifiAwareSetupFinished"
+ "_wifiAwareSetupInProgress"
+ "_wifiAwareVendorName"
+ "_wifiAwareVendorNameMatch"
+ "accessoryUnpairAlert:appName:"
+ "asdID"
+ "bjSn"
+ "bjSn %@"
+ "bjTx %@"
+ "bluetoothSetupFinished"
+ "bluetoothSetupFinished %s"
+ "bluetoothSetupInProgress"
+ "bluetoothSetupInProgress %s"
+ "bonjourServiceName"
+ "bonjourTXTRecordData"
+ "btSetupFinished"
+ "btSetupInProgress"
+ "bundleRecordWithBundleIdentifier:allowPlaceholder:error:"
+ "cdcS"
+ "check appIsUsingDeviceAccess completed with result: %s"
+ "check appIsUsingDeviceAccess failed with error: %@"
+ "check appIsUsingDeviceAccess failed: no reply from daemon"
+ "check appIsUsingDeviceAccess: %@"
+ "compareOptions"
+ "currentDeviceCapabilities"
+ "decodeInt64ForKey:"
+ "deviceOTANameToBroadcast"
+ "deviceWiFiAwarePairingID"
+ "dvID %@"
+ "dwFPi"
+ "encodeInt64:forKey:"
+ "endTime"
+ "endTime %@"
+ "epT"
+ "existingDeviceIdentifier"
+ "infoDictionary"
+ "initWithString:compareOptions:"
+ "initWithWiFiAwareIdentifier:pairingType:"
+ "isWiFiAwarePublisher"
+ "ldNm"
+ "mddExt"
+ "networkUnsecured"
+ "numberWithUnsignedLongLong:"
+ "nwUnsecured"
+ "nwUsec"
+ "objectForKey:ofClass:"
+ "pCs"
+ "pCso"
+ "requiresBluetoothSetup"
+ "requiresWiFiAwareSetup"
+ "requiresWiFiSoftAPSetup"
+ "respondToWiFiAwarePairingRequest %@"
+ "respondToWiFiAwarePairingRequest completed: %@"
+ "respondToWiFiAwarePairingRequest:completionHandler:"
+ "runOtherDiscovery"
+ "runUpgradeWithDiscovery:"
+ "setBluetoothOnboardingFinished:"
+ "setBluetoothSetupFinished:"
+ "setBluetoothSetupInProgress:"
+ "setBonjourServiceName:"
+ "setBonjourTXTRecordData:"
+ "setCurrentDeviceCapabilities:"
+ "setDeviceOTANameToBroadcast:"
+ "setDeviceUpgradeFinished:inProgress:failed:"
+ "setEndTime:"
+ "setExistingDeviceIdentifier:"
+ "setNetworkUnsecured:"
+ "setSignature:"
+ "setUpgradeFailed:"
+ "setUpgradeFinished:"
+ "setUpgradeInProgress:"
+ "setWiFiAwareOnboardingFinished:"
+ "setWifiAwareDevicePairingID:"
+ "setWifiAwareModelName:"
+ "setWifiAwareModelNameMatch:"
+ "setWifiAwareOTAName:"
+ "setWifiAwarePairingID:"
+ "setWifiAwareServiceName:"
+ "setWifiAwareServiceType:"
+ "setWifiAwareSetupFinished:"
+ "setWifiAwareSetupInProgress:"
+ "setWifiAwareVendorName:"
+ "setWifiAwareVendorNameMatch:"
+ "sig"
+ "signature"
+ "stillTrackableWhenUnpaired"
+ "string"
+ "ty %lu"
+ "upgradeFailed"
+ "upgradeFinished"
+ "upgradeInProgress"
+ "v28@0:8B16B20B24"
+ "wFID %llu"
+ "wFMn"
+ "wFMnm"
+ "wFPA"
+ "wFPI"
+ "wFPM"
+ "wFPT"
+ "wFPi"
+ "wFPk"
+ "wFSn"
+ "wFSt"
+ "wFVim"
+ "wFVn"
+ "wapi"
+ "wfMdNm %@"
+ "wfOTANm %@"
+ "wfVdNm %@"
+ "wfaDevicePairingID %@"
+ "wfaNm"
+ "wfaSignature %ld"
+ "wifiAwareDevicePairingID"
+ "wifiAwareIdentifier"
+ "wifiAwareModelName"
+ "wifiAwareModelNameMatch"
+ "wifiAwareOTAName"
+ "wifiAwarePairingID"
+ "wifiAwareServiceName"
+ "wifiAwareServiceType"
+ "wifiAwareSetupFinished"
+ "wifiAwareSetupFinished %s"
+ "wifiAwareSetupInProgress"
+ "wifiAwareSetupInProgress %s"
+ "wifiAwareSignature"
+ "wifiAwareVendorName"
+ "wifiAwareVendorNameMatch"
- "%@, CID 0x%X %@"
- "Device missing accessory setup flag"
- "T@\"NSString\",R,C,N,V_bundleIdentifier"
- "executeQuery:"

```
