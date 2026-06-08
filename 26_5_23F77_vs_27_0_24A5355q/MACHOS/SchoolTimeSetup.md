## SchoolTimeSetup

> `/System/Library/NanoPreferenceBundles/SetupBundles/SchoolTimeSetup.bundle/SchoolTimeSetup`

```diff

-39.0.5.0.0
-  __TEXT.__text: 0x24a8
-  __TEXT.__auth_stubs: 0x2c0
-  __TEXT.__objc_stubs: 0x920
-  __TEXT.__objc_methlist: 0x4b0
+39.0.6.0.0
+  __TEXT.__text: 0x1ebc
+  __TEXT.__auth_stubs: 0x300
+  __TEXT.__objc_stubs: 0x8c0
+  __TEXT.__objc_methlist: 0x490
   __TEXT.__const: 0x58
-  __TEXT.__cstring: 0x120
-  __TEXT.__gcc_except_tab: 0x90
-  __TEXT.__objc_methname: 0xd0b
-  __TEXT.__oslogstring: 0x2f9
-  __TEXT.__objc_classname: 0xd3
+  __TEXT.__cstring: 0x12a
+  __TEXT.__gcc_except_tab: 0x60
+  __TEXT.__objc_methname: 0xc97
+  __TEXT.__oslogstring: 0x2e0
+  __TEXT.__objc_classname: 0xc9
   __TEXT.__objc_methtype: 0x304
-  __TEXT.__unwind_info: 0x180
-  __DATA_CONST.__auth_got: 0x170
-  __DATA_CONST.__got: 0xd0
-  __DATA_CONST.__const: 0xe0
+  __TEXT.__unwind_info: 0x140
+  __DATA_CONST.__const: 0xb8
   __DATA_CONST.__cfstring: 0x120
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x20
-  __DATA.__objc_const: 0x778
-  __DATA.__objc_selrefs: 0x3f8
-  __DATA.__objc_ivar: 0x34
+  __DATA_CONST.__auth_got: 0x190
+  __DATA_CONST.__got: 0xc8
+  __DATA.__objc_const: 0x748
+  __DATA.__objc_selrefs: 0x3e0
+  __DATA.__objc_ivar: 0x30
   __DATA.__objc_data: 0x140
   __DATA.__data: 0x188
   __DATA.__bss: 0x10

   - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/PrivateFrameworks/BridgePreferences.framework/BridgePreferences
   - /System/Library/PrivateFrameworks/FamilyCircle.framework/FamilyCircle
-  - /System/Library/PrivateFrameworks/NanoRegistry.framework/NanoRegistry
   - /System/Library/PrivateFrameworks/OnBoardingKit.framework/OnBoardingKit
+  - /System/Library/PrivateFrameworks/PairedDeviceRegistry.framework/PairedDeviceRegistry
   - /System/Library/PrivateFrameworks/Preferences.framework/Preferences
   - /System/Library/PrivateFrameworks/SchoolTime.framework/SchoolTime
   - /System/Library/PrivateFrameworks/SchoolTimeSettingsUI.framework/SchoolTimeSettingsUI
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 2913F535-2021-3348-9DD7-095CE670FF4D
-  Functions: 87
-  Symbols:   96
-  CStrings:  246
+  UUID: BFBDF365-D49E-373E-AE3E-858433361096
+  Functions: 79
+  Symbols:   99
+  CStrings:  240
 
Symbols:
+ _PDRDidPairNotification
+ _PDRNotificationKeyDevice
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x23
- _NRPairedDeviceRegistryDevice
- _NRPairedDeviceRegistryDeviceDidFailToPairNotification
- _NRPairedDeviceRegistryDeviceDidPairNotification
- _objc_retainAutoreleasedReturnValue
- _scl_framework_log
CStrings:
- "Failed to pair device %@"
- "T@,&,V_pairingDidFailToken"
- "_pairingDidFailToken"
- "_pairingFailedToDevice:"
- "pairingDidFailToken"
- "setPairingDidFailToken:"

```
