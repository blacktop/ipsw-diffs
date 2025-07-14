## SharedUtils

> `/System/Library/Frameworks/LocalAuthentication.framework/Support/SharedUtils.framework/SharedUtils`

```diff

-1394.40.33.0.0
-  __TEXT.__text: 0x1d8dc
-  __TEXT.__auth_stubs: 0x690
-  __TEXT.__objc_methlist: 0xc98
-  __TEXT.__const: 0x248
-  __TEXT.__cstring: 0x2598
+1394.62.1.0.0
+  __TEXT.__text: 0x1da40
+  __TEXT.__auth_stubs: 0x680
+  __TEXT.__objc_methlist: 0xcd0
+  __TEXT.__const: 0x190
+  __TEXT.__cstring: 0x251d
   __TEXT.__gcc_except_tab: 0x1d0
-  __TEXT.__oslogstring: 0xa49
-  __TEXT.__unwind_info: 0x760
-  __TEXT.__objc_classname: 0x3d7
-  __TEXT.__objc_methname: 0x282b
-  __TEXT.__objc_methtype: 0xf94
-  __TEXT.__objc_stubs: 0x17a0
+  __TEXT.__oslogstring: 0xa82
+  __TEXT.__unwind_info: 0x780
+  __TEXT.__objc_classname: 0x41c
+  __TEXT.__objc_methname: 0x28ed
+  __TEXT.__objc_methtype: 0xff3
+  __TEXT.__objc_stubs: 0x17c0
   __DATA_CONST.__got: 0x90
-  __DATA_CONST.__const: 0x5c0
-  __DATA_CONST.__objc_classlist: 0xc0
-  __DATA_CONST.__objc_protolist: 0xd0
+  __DATA_CONST.__const: 0x5b8
+  __DATA_CONST.__objc_classlist: 0xc8
+  __DATA_CONST.__objc_protolist: 0xd8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x1e08
-  __DATA_CONST.__objc_selrefs: 0x9b8
-  __AUTH_CONST.__cfstring: 0xe00
-  __AUTH_CONST.__objc_const: 0x0
-  __AUTH_CONST.__objc_intobj: 0x750
-  __AUTH_CONST.__const: 0x40
-  __AUTH_CONST.__auth_got: 0x358
+  __DATA_CONST.__objc_const: 0x1f60
+  __DATA_CONST.__objc_selrefs: 0x9d8
+  __AUTH_CONST.__cfstring: 0xd80
+  __AUTH_CONST.__objc_const: 0x90
+  __AUTH_CONST.__const: 0x120
+  __AUTH_CONST.__objc_intobj: 0x768
+  __AUTH_CONST.__auth_got: 0x350
+  __AUTH.__objc_data: 0xa0
   __DATA.__objc_protorefs: 0x78
-  __DATA.__objc_classrefs: 0x158
-  __DATA.__objc_superrefs: 0x68
-  __DATA.__objc_ivar: 0xac
-  __DATA.__data: 0x9e1
-  __DATA.__bss: 0xe0
+  __DATA.__objc_classrefs: 0x160
+  __DATA.__objc_superrefs: 0x70
+  __DATA.__objc_ivar: 0xb8
+  __DATA.__data: 0xa41
+  __DATA.__bss: 0xd0
   __DATA.__common: 0x0
-  __DATA_DIRTY.__const: 0x320
-  __DATA_DIRTY.__objc_const: 0x900
-  __DATA_DIRTY.__objc_data: 0x780
+  __DATA_DIRTY.__const: 0x220
+  __DATA_DIRTY.__objc_const: 0x8b8
+  __DATA_DIRTY.__objc_data: 0x730
   __DATA_DIRTY.__data: 0x4
   __DATA_DIRTY.__bss: 0xb0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CryptoTokenKit.framework/CryptoTokenKit
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
+  - /System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore
   - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration
   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
+  - /usr/lib/libAccessibility.dylib
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 8AE54CBB-5587-3390-A13F-9C7F4B8F14BF
-  Functions: 618
-  Symbols:   1824
-  CStrings:  1177
+  UUID: 9A63A432-C598-3D2B-A380-1C881216531F
+  Functions: 623
+  Symbols:   1846
+  CStrings:  1178
 
Symbols:
+ +[LAACMHelper notifyBiometricMatchOperationStartAttempted]
+ +[LAUtils isClarityBoardRunning]
+ +[LAUtils isPolicyAcceptingEmptyPassword:]
+ +[LAUtils usesFrontBoardServicesForRemoteUI]
+ -[LAACMBiometricAttemptNotifier notificationCenter:didReceiveNotification:]
+ -[LABaseService exportedInterface]
+ -[LABaseService exportedInterface].cold.1
+ -[LABaseService exportedObject]
+ -[LABaseServiceManager exportedInterface]
+ -[LAServiceAdapter .cxx_destruct]
+ -[LAServiceAdapter exportedInterface]
+ -[LAServiceAdapter exportedObject]
+ -[LAServiceAdapter initWithExportedInterface:exportedObject:queue:]
+ -[LAServiceAdapter queue]
+ GCC_except_table7
+ _OBJC_CLASS_$_LAACMBiometricAttemptNotifier
+ _OBJC_CLASS_$_LAServiceAdapter
+ _OBJC_CLASS_$_NSURL
+ _OBJC_IVAR_$_LAServiceAdapter._exportedInterface
+ _OBJC_IVAR_$_LAServiceAdapter._exportedObject
+ _OBJC_IVAR_$_LAServiceAdapter._queue
+ _OBJC_METACLASS_$_LAACMBiometricAttemptNotifier
+ _OBJC_METACLASS_$_LAServiceAdapter
+ __AXSClarityBoardEnabled
+ __OBJC_$_INSTANCE_METHODS_LAACMBiometricAttemptNotifier
+ __OBJC_$_INSTANCE_METHODS_LAServiceAdapter
+ __OBJC_$_INSTANCE_VARIABLES_LAServiceAdapter
+ __OBJC_$_PROP_LIST_LAACMBiometricAttemptNotifier
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_LACDarwinNotificationCenterObserver
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_LARemoteUI
+ __OBJC_$_PROTOCOL_METHOD_TYPES_LACDarwinNotificationCenterObserver
+ __OBJC_$_PROTOCOL_REFS_LACDarwinNotificationCenterObserver
+ __OBJC_CLASS_PROTOCOLS_$_LAACMBiometricAttemptNotifier
+ __OBJC_CLASS_RO_$_LAACMBiometricAttemptNotifier
+ __OBJC_CLASS_RO_$_LAServiceAdapter
+ __OBJC_LABEL_PROTOCOL_$_LACDarwinNotificationCenterObserver
+ __OBJC_METACLASS_RO_$_LAACMBiometricAttemptNotifier
+ __OBJC_METACLASS_RO_$_LAServiceAdapter
+ __OBJC_PROTOCOL_$_LACDarwinNotificationCenterObserver
+ ___31+[LAParamChecker checkOptions:]_block_invoke.126
+ ___block_literal_global.129
+ ___block_literal_global.137
+ ___block_literal_global.144
+ ___block_literal_global.159
+ ___block_literal_global.177
+ ___block_literal_global.194
+ ___block_literal_global.32
+ _objc_msgSend$exportedObject
+ _objc_msgSend$isClarityBoardRunning
- +[LABaseService exportedInterface]
- +[LABaseService exportedInterface].cold.1
- +[LABaseServiceManager exportedInterface]
- +[LAMobileGestalt _deviceClass]
- +[LAMobileGestalt currentDeviceScreenSize]
- +[LAMobileGestalt isIdiomPad]
- +[LAMobileGestalt isIdiomPhone]
- +[LAMobileGestalt isVirtualMachine]
- GCC_except_table6
- _MGGetBoolAnswer
- _MGGetSInt32Answer
- _OBJC_CLASS_$_LAMobileGestalt
- _OBJC_METACLASS_$_LAMobileGestalt
- __OBJC_$_CLASS_METHODS_LABaseService
- __OBJC_$_CLASS_METHODS_LABaseServiceManager
- __OBJC_$_CLASS_METHODS_LAMobileGestalt
- __OBJC_CLASS_RO_$_LAMobileGestalt
- __OBJC_METACLASS_RO_$_LAMobileGestalt
- ___31+[LAMobileGestalt _deviceClass]_block_invoke
- ___31+[LAParamChecker checkOptions:]_block_invoke.124
- ___block_literal_global.127
- ___block_literal_global.135
- ___block_literal_global.142
- ___block_literal_global.157
- ___block_literal_global.175
- ___block_literal_global.192
- ___block_literal_global.29
- __deviceClass.deviceClass
- __deviceClass.onceToken
- _kLAServiceTypeSecureStorage
- _objc_msgSend$_deviceClass
CStrings:
+ "\x03"
+ "@\"NSXPCInterface\""
+ "Biometric attempt notification finished with status (%d)"
+ "LAACMBiometricAttemptNotifier"
+ "LACDarwinNotificationCenterObserver"
+ "LAServiceAdapter"
+ "_exportedInterface"
+ "_exportedObject"
+ "exportedObject"
+ "initWithExportedInterface:exportedObject:queue:"
+ "isClarityBoardRunning"
+ "isPolicyAcceptingEmptyPassword:"
+ "notificationCenter:didReceiveNotification:"
+ "notifyBiometricMatchOperationStartAttempted"
+ "usesFrontBoardServicesForRemoteUI"
+ "v32@0:8@\"<LACDarwinNotificationCenter>\"16^{__CFString=}24"
+ "v32@0:8@16^{__CFString=}24"
- "ACMRequirement - ACMRequirementDataRatchet"
- "DeviceClassNumber"
- "IsVirtualDevice"
- "LAMobileGestalt"
- "_deviceClass"
- "currentDeviceScreenSize"
- "i16@0:8"
- "isIdiomPad"
- "isIdiomPhone"
- "isVirtualMachine"
- "kLAServiceTypeSecureStorage"
- "main-screen-class"

```
