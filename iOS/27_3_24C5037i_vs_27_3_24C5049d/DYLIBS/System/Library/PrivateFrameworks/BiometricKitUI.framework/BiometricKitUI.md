## BiometricKitUI

> `/System/Library/PrivateFrameworks/BiometricKitUI.framework/BiometricKitUI`

```diff

-685.2.2.0.0
-  __TEXT.__text: 0x67d7c
-  __TEXT.__objc_methlist: 0x74f0
+685.2.3.0.0
+  __TEXT.__text: 0x680b4
+  __TEXT.__objc_methlist: 0x7510
   __TEXT.__const: 0xa84
   __TEXT.__gcc_except_tab: 0xd20
-  __TEXT.__cstring: 0x3066
-  __TEXT.__oslogstring: 0x6c3b
+  __TEXT.__cstring: 0x3086
+  __TEXT.__oslogstring: 0x6ce8
   __TEXT.__dlopen_cstrs: 0x292
   __TEXT.__swift5_typeref: 0xae
   __TEXT.__swift5_capture: 0x44

   __TEXT.__swift5_assocty: 0x18
   __TEXT.__swift5_proto: 0x8
   __TEXT.__swift5_types: 0xc
-  __TEXT.__unwind_info: 0x1fc0
+  __TEXT.__unwind_info: 0x1fd0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_protolist: 0x150
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0x48a0
+  __DATA_CONST.__objc_selrefs: 0x48d0
   __DATA_CONST.__objc_superrefs: 0x1b0
   __DATA_CONST.__objc_arraydata: 0x1c8
   __DATA_CONST.__got: 0x850
   __AUTH_CONST.__const: 0x318
-  __AUTH_CONST.__cfstring: 0x3660
-  __AUTH_CONST.__objc_const: 0x10860
+  __AUTH_CONST.__cfstring: 0x3680
+  __AUTH_CONST.__objc_const: 0x108b0
   __AUTH_CONST.__weak_auth_got: 0x10
   __AUTH_CONST.__objc_arrayobj: 0xc0
   __AUTH_CONST.__objc_floatobj: 0x80

   __AUTH_CONST.__auth_got: 0x790
   __AUTH.__objc_data: 0x11f0
   __AUTH.__data: 0xe0
-  __DATA.__objc_ivar: 0xa60
+  __DATA.__objc_ivar: 0xa68
   __DATA.__data: 0x1078
   __DATA.__common: 0x300
   __DATA_DIRTY.__objc_data: 0x550

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 2741
-  Symbols:   4590
-  CStrings:  1091
+  Functions: 2744
+  Symbols:   4595
+  CStrings:  1096
 
Symbols:
+ -[BKUIDevice isCloseToLockTurnedOn]
+ -[BKUIFingerprintEnrollViewController _disableCloseToLock]
+ -[BKUIFingerprintEnrollViewController _enableCloseToLock]
+ _OBJC_IVAR_$_BKUIFingerprintEnrollViewController._closeToLockDisabled
+ _OBJC_IVAR_$_BKUIFingerprintEnrollViewController._closeToLockDisabledWindowScene
CStrings:
+ "Disabled Close to Lock for the enrollment flow (scene present=%d)"
+ "Not touching Close to Lock, it is already turned off"
+ "Re-enabled Close to Lock, the enrollment flow is over"
+ "SBLockOnFoldClosed"
+ "\xf0\xf1"
```
