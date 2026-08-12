## PasscodeAndBiometricsSettings

> `/System/Library/PrivateFrameworks/PasscodeAndBiometricsSettings.framework/PasscodeAndBiometricsSettings`

```diff

-34.0.0.0.0
-  __TEXT.__text: 0x3b8c0
+35.3.0.0.0
+  __TEXT.__text: 0x3bd70
   __TEXT.__delay_stubs: 0x40
   __TEXT.__delay_helper: 0xdc
-  __TEXT.__objc_methlist: 0x212c
+  __TEXT.__objc_methlist: 0x2144
   __TEXT.__const: 0xc34
-  __TEXT.__gcc_except_tab: 0x8c8
+  __TEXT.__gcc_except_tab: 0x8c4
   __TEXT.__cstring: 0x3698
-  __TEXT.__oslogstring: 0x5115
+  __TEXT.__oslogstring: 0x5165
   __TEXT.__dlopen_cstrs: 0x333
   __TEXT.__ustring: 0x4e
   __TEXT.__swift5_typeref: 0x6b0

   __TEXT.__swift5_assocty: 0xc8
   __TEXT.__swift5_proto: 0x4c
   __TEXT.__swift5_builtin: 0x14
-  __TEXT.__unwind_info: 0x1090
+  __TEXT.__unwind_info: 0x1098
   __TEXT.__eh_frame: 0x7b8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x90
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1e30
+  __DATA_CONST.__objc_selrefs: 0x1e40
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x80
   __DATA_CONST.__objc_arraydata: 0x8

   __AUTH_CONST.__objc_const: 0x2128
   __AUTH_CONST.__objc_intobj: 0x150
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH_CONST.__auth_got: 0xa70
+  __AUTH_CONST.__auth_got: 0xa68
   __AUTH.__objc_data: 0x508
   __AUTH.__data: 0xe8
   __DATA.__objc_ivar: 0xe0

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1317
-  Symbols:   2629
-  CStrings:  884
+  Functions: 1320
+  Symbols:   2632
+  CStrings:  885
 
Symbols:
+ -[PABSBiometrics isEnrolledInAnyBiometric]
+ -[PABSBiometrics removeAllIdentities]
+ _objc_msgSend$control
+ _objc_msgSend$isEnrolledInAnyBiometric
+ _objc_msgSend$removeAllIdentities
+ _objc_msgSend$setAccessibilityIdentifier:
- _PSPointImageOfColor
- _objc_msgSend$_setHidesShadow:
- _objc_msgSend$setBackgroundImage:forBarMetrics:
CStrings:
+ "Biometrics enrolled with no passcode set — removing all identities"
```
