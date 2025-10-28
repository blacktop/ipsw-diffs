## KeyboardSettings

> `/System/Library/PrivateFrameworks/KeyboardSettings.framework/KeyboardSettings`

```diff

 123.0.0.0.0
-  __TEXT.__text: 0x28d9c
+  __TEXT.__text: 0x28e3c
   __TEXT.__auth_stubs: 0xad0
   __TEXT.__objc_methlist: 0x2998
   __TEXT.__const: 0x78
   __TEXT.__gcc_except_tab: 0x2fc
-  __TEXT.__cstring: 0x3617
+  __TEXT.__cstring: 0x3645
   __TEXT.__oslogstring: 0x3
   __TEXT.__dlopen_cstrs: 0x117
   __TEXT.__ustring: 0x52
-  __TEXT.__unwind_info: 0x8f8
+  __TEXT.__unwind_info: 0x900
   __TEXT.__objc_classname: 0x5c7
-  __TEXT.__objc_methname: 0x8a33
+  __TEXT.__objc_methname: 0x8a3f
   __TEXT.__objc_methtype: 0x17f1
-  __TEXT.__objc_stubs: 0x6660
+  __TEXT.__objc_stubs: 0x6680
   __DATA_CONST.__got: 0x740
   __DATA_CONST.__const: 0x798
   __DATA_CONST.__objc_classlist: 0x118
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x22f0
+  __DATA_CONST.__objc_selrefs: 0x22f8
   __DATA_CONST.__objc_superrefs: 0x110
   __DATA_CONST.__objc_arraydata: 0x2b8
   __AUTH_CONST.__auth_got: 0x578
-  __AUTH_CONST.__const: 0x2e0
-  __AUTH_CONST.__cfstring: 0x3360
+  __AUTH_CONST.__const: 0x300
+  __AUTH_CONST.__cfstring: 0x33a0
   __AUTH_CONST.__objc_const: 0x3458
   __AUTH_CONST.__objc_arrayobj: 0x270
   __AUTH_CONST.__objc_intobj: 0x2e8

   __AUTH.__objc_data: 0xaa0
   __DATA.__objc_ivar: 0x1d4
   __DATA.__data: 0x540
-  __DATA.__bss: 0xc8
+  __DATA.__bss: 0xd8
   __DATA_DIRTY.__objc_data: 0x50
   __DATA_DIRTY.__bss: 0x38
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: D3074B0F-D320-3DBE-952A-0E58229E64C5
-  Functions: 853
-  Symbols:   3455
-  CStrings:  2484
+  UUID: BAB1B0C4-25FF-3603-A633-1C92081F0D6D
+  Functions: 855
+  Symbols:   3463
+  CStrings:  2489
 
Symbols:
+ -[KSKeyboardController feedbackFeatureEnabled].cold.2
+ GCC_except_table69
+ ___46-[KSKeyboardController feedbackFeatureEnabled]_block_invoke
+ ___block_literal_global.237
+ ___block_literal_global.401
+ ___block_literal_global.741
+ _feedbackFeatureEnabled.is_internal_install
+ _feedbackFeatureEnabled.once_token
+ _objc_msgSend$boolForKey:
- GCC_except_table68
- ___block_literal_global.389
- ___block_literal_global.729
Functions:
~ -[KSKeyboardController feedbackFeatureEnabled] : 76 -> 172
+ ___46-[KSKeyboardController feedbackFeatureEnabled]_block_invoke
~ -[KSKeyboardController feedbackFeatureEnabled].cold.1 : 184 -> 20
+ -[KSKeyboardController feedbackFeatureEnabled].cold.2
CStrings:
+ "%s Feedback %@: RC_SEED_BUILD: 0 enabled: %d"
+ "apple-internal-install"
+ "boolForKey:"
- "%s Feedback %@: RC_SEED_BUILD: 1 enabled: %d"

```
