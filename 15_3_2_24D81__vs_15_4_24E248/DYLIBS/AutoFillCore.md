## AutoFillCore

> `/System/Library/PrivateFrameworks/AutoFillCore.framework/Versions/A/AutoFillCore`

```diff

 35.0.0.0.0
-  __TEXT.__text: 0xb0e8
+  __TEXT.__text: 0xb0a0
   __TEXT.__auth_stubs: 0x330
-  __TEXT.__objc_methlist: 0x3bc
+  __TEXT.__objc_methlist: 0x4f4
   __TEXT.__const: 0x78
   __TEXT.__cstring: 0x18c3
-  __TEXT.__gcc_except_tab: 0x5e4
+  __TEXT.__gcc_except_tab: 0x5ec
   __TEXT.__oslogstring: 0x3
   __TEXT.__dlopen_cstrs: 0x2da
-  __TEXT.__unwind_info: 0x350
+  __TEXT.__unwind_info: 0x368
   __TEXT.__objc_classname: 0xa4
   __TEXT.__objc_methname: 0x1a11
   __TEXT.__objc_methtype: 0x3ae

   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x578
+  __DATA_CONST.__objc_selrefs: 0x618
   __DATA_CONST.__objc_superrefs: 0x20
   __AUTH_CONST.__auth_got: 0x1a8
   __AUTH_CONST.__const: 0x520
   __AUTH_CONST.__cfstring: 0x10a0
-  __AUTH_CONST.__objc_const: 0xa58
+  __AUTH_CONST.__objc_const: 0x828
   __AUTH_CONST.__objc_intobj: 0xc0
   __AUTH.__objc_data: 0x190
   __DATA.__objc_ivar: 0x54

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 7C64DF9E-EDAB-395A-8E18-0F31086421DE
-  Functions: 229
-  Symbols:   725
+  UUID: FA8FC7ED-01BB-3C6C-9363-2A92B80E0C0D
+  Functions: 237
+  Symbols:   733
   CStrings:  624
 
Symbols:
+ +[AFCredentialManager sharedInstance].cold.1
+ +[AFInsertionManager preferredInsertionOrder].cold.1
+ +[AFSuggestionGenerationManager sharedInstance].cold.1
+ -[AFCredentialManager generateLoginAutoFillWithDocumentTraits:].cold.1
+ AFCredentialManagerOSLogFacility.cold.1
+ AFDispatchAsync.cold.1
+ AFLocalizationManagerOSLogFacility.cold.1
+ AFSuggestionGenerationManagerOSLogFacility.cold.1
+ GCC_except_table109
+ GCC_except_table110
+ GCC_except_table115
+ GCC_except_table116
+ GCC_except_table56
+ GCC_except_table57
+ __AFDispatchAsync_block_invoke.cold.1
- GCC_except_table106
- GCC_except_table107
- GCC_except_table112
- GCC_except_table113
- GCC_except_table53
- GCC_except_table54
- _OUTLINED_FUNCTION_4

```
