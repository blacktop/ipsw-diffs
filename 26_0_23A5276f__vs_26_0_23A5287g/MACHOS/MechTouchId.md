## MechTouchId

> `/System/Library/Frameworks/LocalAuthentication.framework/Support/MechanismPlugins/MechTouchId.bundle/MechTouchId`

```diff

-2005.0.31.0.0
-  __TEXT.__text: 0x27fc
+2005.0.40.0.0
+  __TEXT.__text: 0x2834
   __TEXT.__auth_stubs: 0x270
-  __TEXT.__objc_stubs: 0xd40
+  __TEXT.__objc_stubs: 0xd80
   __TEXT.__objc_methlist: 0x314
   __TEXT.__const: 0x80
   __TEXT.__gcc_except_tab: 0x50
   __TEXT.__cstring: 0xdf
-  __TEXT.__objc_methname: 0xce9
+  __TEXT.__objc_methname: 0xd1c
   __TEXT.__oslogstring: 0x23c
   __TEXT.__objc_classname: 0x92
   __TEXT.__objc_methtype: 0x238
   __TEXT.__unwind_info: 0x120
   __DATA_CONST.__auth_got: 0x148
-  __DATA_CONST.__got: 0x68
+  __DATA_CONST.__got: 0x70
   __DATA_CONST.__const: 0x168
   __DATA_CONST.__cfstring: 0x1a0
   __DATA_CONST.__objc_classlist: 0x8

   __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__objc_intobj: 0x1c8
   __DATA.__objc_const: 0x3e0
-  __DATA.__objc_selrefs: 0x478
+  __DATA.__objc_selrefs: 0x488
   __DATA.__objc_ivar: 0x28
   __DATA.__objc_data: 0x50
   __DATA.__data: 0x1e0

   - /System/Library/Frameworks/LocalAuthentication.framework/Support/DaemonUtils.framework/DaemonUtils
   - /System/Library/Frameworks/LocalAuthentication.framework/Support/MechanismBase.framework/MechanismBase
   - /System/Library/Frameworks/LocalAuthentication.framework/Support/SharedUtils.framework/SharedUtils
+  - /System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 2BB69A85-B1F5-31B4-A197-FDF30C5DC5B8
+  UUID: E723BEF7-2C93-30F9-AF0B-54DB522B87D3
   Functions: 44
-  Symbols:   62
-  CStrings:  245
+  Symbols:   63
+  CStrings:  247
 
Symbols:
+ _LACEventTouchID
Functions:
~ sub_13d8 -> sub_1450 : 2284 -> 2340
CStrings:
+ "analyticsData"
+ "authenticationAttemptFailedForEvent:"

```
