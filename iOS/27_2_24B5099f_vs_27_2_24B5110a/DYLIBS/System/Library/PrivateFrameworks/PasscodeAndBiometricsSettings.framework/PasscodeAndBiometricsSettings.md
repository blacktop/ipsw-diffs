## PasscodeAndBiometricsSettings

> `/System/Library/PrivateFrameworks/PasscodeAndBiometricsSettings.framework/PasscodeAndBiometricsSettings`

```diff

-40.2.1.0.0
-  __TEXT.__text: 0x3ad9c
+40.2.3.100.0
+  __TEXT.__text: 0x3b2b0
   __TEXT.__delay_stubs: 0x40
   __TEXT.__delay_helper: 0xdc
-  __TEXT.__objc_methlist: 0x2184
-  __TEXT.__const: 0xc74
+  __TEXT.__objc_methlist: 0x21c4
+  __TEXT.__const: 0xc84
   __TEXT.__gcc_except_tab: 0x8a4
-  __TEXT.__cstring: 0x36a8
-  __TEXT.__oslogstring: 0x50f5
+  __TEXT.__cstring: 0x3718
+  __TEXT.__oslogstring: 0x51f5
   __TEXT.__dlopen_cstrs: 0x333
   __TEXT.__ustring: 0x4e
   __TEXT.__swift5_typeref: 0x6c8

   __TEXT.__swift5_assocty: 0xc8
   __TEXT.__swift5_proto: 0x4c
   __TEXT.__swift5_builtin: 0x14
-  __TEXT.__unwind_info: 0x1520
+  __TEXT.__unwind_info: 0x1548
   __TEXT.__eh_frame: 0x7b8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x90
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1e48
+  __DATA_CONST.__objc_selrefs: 0x1e68
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x80
   __DATA_CONST.__objc_arraydata: 0x8
-  __DATA_CONST.__got: 0x720
+  __DATA_CONST.__got: 0x740
   __AUTH_CONST.__const: 0xa68
-  __AUTH_CONST.__cfstring: 0x2f00
-  __AUTH_CONST.__objc_const: 0x2188
+  __AUTH_CONST.__cfstring: 0x2f40
+  __AUTH_CONST.__objc_const: 0x21c0
   __AUTH_CONST.__objc_intobj: 0x150
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__auth_got: 0xaa0
   __AUTH.__objc_data: 0x5b8
   __AUTH.__data: 0x110
-  __DATA.__objc_ivar: 0xe0
-  __DATA.__data: 0x694
+  __DATA.__objc_ivar: 0xe4
+  __DATA.__data: 0x6c4
   __DATA.__common: 0x1
   __DATA_DIRTY.__objc_data: 0x578
-  __DATA_DIRTY.__data: 0x648
+  __DATA_DIRTY.__data: 0x650
   __DATA_DIRTY.__bss: 0x3e0
   __DATA_DIRTY.__common: 0x20
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1324
-  Symbols:   1851
-  CStrings:  884
+  Functions: 1335
+  Symbols:   1857
+  CStrings:  889
 
Symbols:
+ -[PABSPasscodeLockController viewDidLayoutSubviews]
+ -[PABSTouchIDPasscodeController enrollFlowTornDownByResult]
+ -[PABSTouchIDPasscodeController enrollmentNavigationControllerDidDismiss:]
+ -[PABSTouchIDPasscodeController enrollmentNavigationControllerWillDismiss:]
+ -[PABSTouchIDPasscodeController setEnrollFlowTornDownByResult:]
+ GCC_except_table117
+ GCC_except_table119
+ GCC_except_table121
+ GCC_except_table130
+ GCC_except_table151
+ GCC_except_table27
+ GCC_except_table30
+ GCC_except_table38
+ GCC_except_table47
+ GCC_except_table53
+ GCC_except_table55
+ GCC_except_table72
+ GCC_except_table86
+ _OBJC_IVAR_$_PABSTouchIDPasscodeController._enrollFlowTornDownByResult
- GCC_except_table116
- GCC_except_table118
- GCC_except_table120
- GCC_except_table129
- GCC_except_table150
- GCC_except_table31
- GCC_except_table44
- GCC_except_table46
- GCC_except_table51
- GCC_except_table52
- GCC_except_table67
- GCC_except_table74
- GCC_except_table85
CStrings:
+ "DTO_SECURITY_DELAY_OPTIONS_GROUP_FOOTER_DESCRIPTION_ALWAYS_FACE_ID"
+ "DTO_SECURITY_DELAY_OPTIONS_GROUP_FOOTER_DESCRIPTION_ALWAYS_TOUCH_ID"
+ "DTO_SECURITY_DELAY_OPTIONS_GROUP_HEADER_DESCRIPTION_FACE_ID"
+ "DTO_SECURITY_DELAY_OPTIONS_GROUP_HEADER_DESCRIPTION_TOUCH_ID"
+ "PHONE_NEARBY_DEVICE_AUTO_UNLOCK_FOOTER"
+ "PHONE_VISION_PRO_AUTO_UNLOCK_ALERT_BODY_DEFAULT"
+ "Touch ID: No enrollment controller from BiometricKitUI, not starting enrollment"
+ "Touch ID: enrollment navigation controller dismissed without an enroll result"
+ "Touch ID: enrollment navigation controller dismissed, already handled by enroll result"
- "DTO_SECURITY_DELAY_OPTIONS_GROUP_FOOTER_DESCRIPTION_ALWAYS"
- "DTO_SECURITY_DELAY_OPTIONS_GROUP_HEADER_DESCRIPTION"
- "PHONE_NEARBY_DEVICE_AUTO_UNLOCK_FOOTER_ASSISTANT_DISABLED"
- "PHONE_NEARBY_DEVICE_AUTO_UNLOCK_FOOTER_ASSISTANT_ENABLED"
```
