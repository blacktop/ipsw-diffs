## MessagesPairingRegistration

> `/System/Library/NanoPreferenceBundles/SetupBundles/MessagesPairingRegistration.bundle/MessagesPairingRegistration`

```diff

-1445.100.6.2.4
-  __TEXT.__text: 0xe90
+1447.100.7.2.3
+  __TEXT.__text: 0xe64
   __TEXT.__auth_stubs: 0x250
-  __TEXT.__objc_stubs: 0x3e0
+  __TEXT.__objc_stubs: 0x3c0
   __TEXT.__objc_methlist: 0x2ec
-  __TEXT.__objc_methname: 0x638
+  __TEXT.__objc_methname: 0x629
   __TEXT.__objc_classname: 0xbe
   __TEXT.__objc_methtype: 0x1db
   __TEXT.__const: 0x18

   __TEXT.__oslogstring: 0x106
   __TEXT.__unwind_info: 0xb8
   __DATA_CONST.__auth_got: 0x138
-  __DATA_CONST.__got: 0x60
+  __DATA_CONST.__got: 0x58
   __DATA_CONST.__const: 0x8
   __DATA_CONST.__cfstring: 0x260
   __DATA_CONST.__objc_classlist: 0x18

   __DATA_CONST.__objc_arraydata: 0x8
   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA.__objc_const: 0x460
-  __DATA.__objc_selrefs: 0x218
+  __DATA.__objc_selrefs: 0x210
   __DATA.__objc_ivar: 0x10
   __DATA.__objc_data: 0xf0
   __DATA.__data: 0x128

   - /System/Library/PrivateFrameworks/IDS.framework/IDS
   - /System/Library/PrivateFrameworks/IMFoundation.framework/IMFoundation
   - /System/Library/PrivateFrameworks/Marco.framework/Marco
-  - /System/Library/PrivateFrameworks/NanoRegistry.framework/NanoRegistry
   - /System/Library/PrivateFrameworks/OnBoardingKit.framework/OnBoardingKit
+  - /System/Library/PrivateFrameworks/PairedDeviceRegistry.framework/PairedDeviceRegistry
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 7ED4E30F-7B1D-3E98-BE36-348F2FD5EC03
+  UUID: 018CE6F3-30A2-3FBE-88E1-7E509BD56D4E
   Functions: 32
-  Symbols:   68
-  CStrings:  152
+  Symbols:   67
+  CStrings:  151
 
Symbols:
+ _OBJC_CLASS_$_PDRRegistry
- _NRDevicePropertyIsAltAccount
- _OBJC_CLASS_$_NRPairedDeviceRegistry
Functions:
~ sub_18bc -> sub_18cc : 256 -> 212
CStrings:
+ "isAltAccount"
- "boolValue"
- "valueForProperty:"

```
