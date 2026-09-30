## DiagnosticExtensionsDaemon

> `/System/Library/PrivateFrameworks/DiagnosticExtensionsDaemon.framework/DiagnosticExtensionsDaemon`

```diff

-189.0.0.0.0
-  __TEXT.__text: 0x6e590
+196.0.0.0.0
+  __TEXT.__text: 0x6f540
   __TEXT.__auth_stubs: 0x950
-  __TEXT.__objc_methlist: 0x690c
-  __TEXT.__const: 0x1e0
-  __TEXT.__cstring: 0x5116
+  __TEXT.__objc_methlist: 0x69e4
+  __TEXT.__const: 0x278
+  __TEXT.__cstring: 0x518c
   __TEXT.__gcc_except_tab: 0x1da8
-  __TEXT.__oslogstring: 0x84f9
+  __TEXT.__oslogstring: 0x8566
   __TEXT.__ustring: 0xc
-  __TEXT.__unwind_info: 0x1a58
-  __TEXT.__objc_classname: 0x873
-  __TEXT.__objc_methname: 0xeb73
-  __TEXT.__objc_methtype: 0x2316
-  __TEXT.__objc_stubs: 0xbae0
-  __DATA_CONST.__got: 0x6c8
-  __DATA_CONST.__const: 0x1c60
-  __DATA_CONST.__objc_classlist: 0x258
+  __TEXT.__unwind_info: 0x1a80
+  __TEXT.__objc_classname: 0x88f
+  __TEXT.__objc_methname: 0xedc2
+  __TEXT.__objc_methtype: 0x235b
+  __TEXT.__objc_stubs: 0xbd00
+  __DATA_CONST.__got: 0x6b8
+  __DATA_CONST.__const: 0x2020
+  __DATA_CONST.__objc_classlist: 0x260
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0xd8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3878
+  __DATA_CONST.__objc_selrefs: 0x3908
   __DATA_CONST.__objc_protorefs: 0x28
-  __DATA_CONST.__objc_superrefs: 0x1a0
+  __DATA_CONST.__objc_superrefs: 0x1a8
   __DATA_CONST.__objc_arraydata: 0x48
   __AUTH_CONST.__auth_got: 0x4b8
-  __AUTH_CONST.__const: 0xbe0
-  __AUTH_CONST.__cfstring: 0x4ba0
-  __AUTH_CONST.__objc_const: 0x122d8
+  __AUTH_CONST.__const: 0xc00
+  __AUTH_CONST.__cfstring: 0x4c20
+  __AUTH_CONST.__objc_const: 0x12830
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__objc_intobj: 0x330
   __AUTH_CONST.__objc_dictobj: 0x50
-  __AUTH.__objc_data: 0xeb0
-  __DATA.__objc_ivar: 0x5a0
+  __AUTH.__objc_data: 0xf00
+  __DATA.__objc_ivar: 0x5ac
   __DATA.__data: 0xa40
-  __DATA.__bss: 0x178
+  __DATA.__bss: 0x188
   __DATA_DIRTY.__objc_data: 0x8c0
   __DATA_DIRTY.__bss: 0x228
   - /System/Library/Frameworks/CloudKit.framework/CloudKit

   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/CoreFollowUp.framework/CoreFollowUp
   - /System/Library/PrivateFrameworks/DiagnosticExtensions.framework/DiagnosticExtensions
+  - /System/Library/PrivateFrameworks/EnhancedLogging.framework/EnhancedLogging
   - /System/Library/PrivateFrameworks/EnhancedLoggingState.framework/EnhancedLoggingState
   - /System/Library/PrivateFrameworks/IDS.framework/IDS
   - /System/Library/PrivateFrameworks/IDSFoundation.framework/IDSFoundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 2B3F8743-550F-3A4B-AE11-02F6808AAF42
-  Functions: 2693
-  Symbols:   9406
-  CStrings:  5044
+  UUID: EB201520-68DD-3BA4-AA4E-B9779FE04427
+  Functions: 2711
+  Symbols:   9468
+  CStrings:  5087
 
Symbols:
+ +[DEDDevice deviceTypeFromIDSDeviceType:]
+ +[DEDDevice deviceTypeFromPlatform:deviceClass:]
+ +[DEDDevice deviceWithIDSDevice:address:]
+ +[DEDEnhancedLoggingNotifier archivedClasses]
+ +[DEDNotifierConfiguration enhancedLoggingConfiguration]
+ +[DEDUtils deviceType]
+ +[DEDUtils unauthenticatedDeviceSpecifierFormResponseID:device:]
+ -[DEDBugSessionConfiguration isUnauthenticatedSession]
+ -[DEDBugSessionConfiguration setIsUnauthenticatedSession:]
+ -[DEDDevice deviceType]
+ -[DEDDevice setDeviceType:]
+ -[DEDEnhancedLoggingNotifier .cxx_destruct]
+ -[DEDEnhancedLoggingNotifier init]
+ -[DEDEnhancedLoggingNotifier presentNotificationForSession:]
+ -[DEDEnhancedLoggingNotifier removeNotificationForSession:]
+ -[DEDEnhancedLoggingNotifier setStatusProvider:]
+ -[DEDEnhancedLoggingNotifier statusProvider]
+ _DEDDeviceKeyDeviceType
+ _DEDKeyIsUnauthenticatedSession
+ _LogEnhancedLoggingNotifier
+ _LogEnhancedLoggingNotifier.cold.1
+ _LogEnhancedLoggingNotifier.log
+ _LogEnhancedLoggingNotifier.onceToken
+ _OBJC_CLASS_$_DEDEnhancedLoggingNotifier
+ _OBJC_CLASS_$_ELBugSessionStatusProvider
+ _OBJC_IVAR_$_DEDBugSessionConfiguration._isUnauthenticatedSession
+ _OBJC_IVAR_$_DEDDevice._deviceType
+ _OBJC_IVAR_$_DEDEnhancedLoggingNotifier._statusProvider
+ _OBJC_METACLASS_$_DEDEnhancedLoggingNotifier
+ __OBJC_$_CLASS_METHODS_DEDEnhancedLoggingNotifier
+ __OBJC_$_INSTANCE_METHODS_DEDEnhancedLoggingNotifier
+ __OBJC_$_INSTANCE_VARIABLES_DEDEnhancedLoggingNotifier
+ __OBJC_$_PROP_LIST_DEDEnhancedLoggingNotifier
+ __OBJC_CLASS_PROTOCOLS_$_DEDEnhancedLoggingNotifier
+ __OBJC_CLASS_RO_$_DEDEnhancedLoggingNotifier
+ __OBJC_METACLASS_RO_$_DEDEnhancedLoggingNotifier
+ ___47-[DEDController purgeStaleSessions:completion:]_block_invoke.113
+ ___47-[DEDController purgeStaleSessions:completion:]_block_invoke.113.cold.1
+ ___54-[DEDController idsInbound_devicesChanged:completion:]_block_invoke.54
+ ___56-[DEDController xpcInbound_discoverAllAvailableDevices:]_block_invoke.42
+ ___56-[DEDController xpcInbound_discoverAllAvailableDevices:]_block_invoke.44
+ ___56-[DEDController xpcInbound_discoverAllAvailableDevices:]_block_invoke.46
+ ___56-[DEDController xpcInbound_discoverAllAvailableDevices:]_block_invoke_2.45
+ ___87-[DEDController startBugSessionWithIdentifier:configuration:caller:target:fromInbound:]_block_invoke.64
+ ___87-[DEDController startBugSessionWithIdentifier:configuration:caller:target:fromInbound:]_block_invoke.64.cold.1
+ ___87-[DEDController startBugSessionWithIdentifier:configuration:caller:target:fromInbound:]_block_invoke.79
+ ___87-[DEDController startBugSessionWithIdentifier:configuration:caller:target:fromInbound:]_block_invoke.79.cold.1
+ ___87-[DEDController startBugSessionWithIdentifier:configuration:caller:target:fromInbound:]_block_invoke.82
+ ___87-[DEDController startBugSessionWithIdentifier:configuration:caller:target:fromInbound:]_block_invoke.85.cold.1
+ ___87-[DEDController startBugSessionWithIdentifier:configuration:caller:target:fromInbound:]_block_invoke.86
+ ___87-[DEDController startBugSessionWithIdentifier:configuration:caller:target:fromInbound:]_block_invoke.89
+ ___87-[DEDController startBugSessionWithIdentifier:configuration:caller:target:fromInbound:]_block_invoke_2.87
+ ___87-[DEDController startBugSessionWithIdentifier:configuration:caller:target:fromInbound:]_block_invoke_3.88
+ ___LogEnhancedLoggingNotifier_block_invoke
+ ___block_literal_global.103
+ ___block_literal_global.199
+ ___block_literal_global.231
+ _objc_msgSend$_setError
+ _objc_msgSend$arrayWithObjects:
+ _objc_msgSend$collectionDidCompleteWithSessionIdentifier:
+ _objc_msgSend$containerURLForSecurityApplicationGroupIdentifier:
+ _objc_msgSend$deviceType
+ _objc_msgSend$deviceTypeFromIDSDeviceType:
+ _objc_msgSend$deviceTypeFromPlatform:deviceClass:
+ _objc_msgSend$deviceWithIDSDevice:address:
+ _objc_msgSend$getBytes:range:
+ _objc_msgSend$hasError
+ _objc_msgSend$initWithHostAppIdentifier:localizedNotificationTitle:localizedNotificationBody:
+ _objc_msgSend$isUnauthenticatedSession
+ _objc_msgSend$position
+ _objc_msgSend$setDeviceType:
+ _objc_msgSend$setPosition:
+ _objc_msgSend$statusProvider
+ _objc_msgSend$unauthenticatedDeviceSpecifierFormResponseID:device:
+ _objc_msgSend$underlyingErrors
- +[DEDDevice idsDeviceWithDevice:address:]
- OBJC_IVAR_$_PBDataReader._bytes
- OBJC_IVAR_$_PBDataReader._error
- OBJC_IVAR_$_PBDataReader._length
- OBJC_IVAR_$_PBDataReader._pos
- ___47-[DEDController purgeStaleSessions:completion:]_block_invoke.112
- ___47-[DEDController purgeStaleSessions:completion:]_block_invoke.112.cold.1
- ___54-[DEDController idsInbound_devicesChanged:completion:]_block_invoke.53
- ___56-[DEDController xpcInbound_discoverAllAvailableDevices:]_block_invoke.41
- ___56-[DEDController xpcInbound_discoverAllAvailableDevices:]_block_invoke.43
- ___56-[DEDController xpcInbound_discoverAllAvailableDevices:]_block_invoke.45
- ___56-[DEDController xpcInbound_discoverAllAvailableDevices:]_block_invoke_2.44
- ___87-[DEDController startBugSessionWithIdentifier:configuration:caller:target:fromInbound:]_block_invoke.63
- ___87-[DEDController startBugSessionWithIdentifier:configuration:caller:target:fromInbound:]_block_invoke.63.cold.1
- ___87-[DEDController startBugSessionWithIdentifier:configuration:caller:target:fromInbound:]_block_invoke.78
- ___87-[DEDController startBugSessionWithIdentifier:configuration:caller:target:fromInbound:]_block_invoke.78.cold.1
- ___87-[DEDController startBugSessionWithIdentifier:configuration:caller:target:fromInbound:]_block_invoke.80
- ___87-[DEDController startBugSessionWithIdentifier:configuration:caller:target:fromInbound:]_block_invoke.84
- ___87-[DEDController startBugSessionWithIdentifier:configuration:caller:target:fromInbound:]_block_invoke.84.cold.1
- ___87-[DEDController startBugSessionWithIdentifier:configuration:caller:target:fromInbound:]_block_invoke.88
- ___87-[DEDController startBugSessionWithIdentifier:configuration:caller:target:fromInbound:]_block_invoke_2.86
- ___87-[DEDController startBugSessionWithIdentifier:configuration:caller:target:fromInbound:]_block_invoke_3.87
- ___block_literal_global.102
- ___block_literal_global.198
- ___block_literal_global.220
- _objc_msgSend$idsDeviceWithDevice:address:
CStrings:
+ "\nDEDDevice: %@ %s %@ (%@) -- %s"
+ "-"
+ "@\"ELBugSessionStatusProvider\""
+ "@32@0:8q16@24"
+ "DEDEnhancedLoggingNotifier"
+ "Device ready:\nidentifier: %{public}@\nidsIdentifier: %{public}@\naddress: %{private}@\nmodel: %{public}@\nname: %{private}@\nplatform: %{public}@\ndeviceType: %{public}s\nbuild: %{public}@\nremoteTransport: %{public}s\ntransport: %{public}s\nstatus: %{public}s\ndeviceClass: %{public}@\nproductType: %{public}@\ncolor: %{public}@\nenclosureColor: %{public}@\nhomeButtonType: %li\nisHomeKitResident: %d\nmediaSystemRole: %li\ncapabilities: %{public}@\n"
+ "EnhancedLogging"
+ "Notifying enhancedloggingd for bug session [%{public}@]"
+ "Reality"
+ "T@\"ELBugSessionStatusProvider\",&,N,V_statusProvider"
+ "TB,V_isUnauthenticatedSession"
+ "Tq,V_deviceType"
+ "Unauthenticated-FR%li-%lu"
+ "Will try to add device:\n%{private}@ - %{public}s %{public}@ (%{public}@) -- %{public}s \n%{public}s (%{public}@) \n%{public}s Remote: (%{private}@ - %{public}@)"
+ "_deviceType"
+ "_isUnauthenticatedSession"
+ "_setError"
+ "_statusProvider"
+ "arrayWithObjects:"
+ "collectionDidCompleteWithSessionIdentifier:"
+ "containerURLForSecurityApplicationGroupIdentifier:"
+ "ded-el-notifier"
+ "deviceType"
+ "deviceTypeFromIDSDeviceType:"
+ "deviceTypeFromPlatform:deviceClass:"
+ "deviceWithIDSDevice:address:"
+ "dovePeace2"
+ "enhancedLoggingConfiguration"
+ "getBytes:range:"
+ "isUnauthenticatedSession"
+ "position"
+ "q24@0:8q16"
+ "q32@0:8@16@24"
+ "setDeviceType:"
+ "setIsUnauthenticatedSession:"
+ "setPosition:"
+ "setStatusProvider:"
+ "statusProvider"
+ "unauthenticatedDeviceSpecifierFormResponseID:device:"
+ "underlyingErrors"
+ "uniquingString un-hashed [%@]"
- "\nDEDDevice: %@ %@ (%@) -- %s"
- "Device ready:\nidentifier: %{public}@\nidsIdentifier: %{public}@\naddress: %{private}@\nmodel: %{public}@\nname: %{private}@\nplatform: %{public}@\nbuild: %{public}@\nremoteTransport: %{public}s\ntransport: %{public}s\nstatus: %{public}s\ndeviceClass: %{public}@\nproductType: %{public}@\ncolor: %{public}@\nenclosureColor: %{public}@\nhomeButtonType: %li\nisHomeKitResident: %d\nmediaSystemRole: %li\ncapabilities: %{public}@\n"
- "Will try to add device:\n%{private}@ - %{public}@ %{public}@ (%{public}@) -- %{public}s \n%{public}s (%{public}@) \n%{public}s Remote: (%{private}@ - %{public}@)"
- "idsDeviceWithDevice:address:"

```
