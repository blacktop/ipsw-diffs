## libboringssl.dylib

> `/usr/lib/libboringssl.dylib`

```diff

-532.0.11.0.0
-  __TEXT.__text: 0x9fca4
-  __TEXT.__auth_stubs: 0x1e40
+532.0.13.0.0
+  __TEXT.__text: 0x9fdec
+  __TEXT.__auth_stubs: 0x1e50
   __TEXT.__objc_methlist: 0x1dc
   __TEXT.__cstring: 0x106e0
   __TEXT.__const: 0xfef8

   __TEXT.__unwind_info: 0x24a8
   __TEXT.__eh_frame: 0x130
   __TEXT.__objc_classname: 0x240
-  __TEXT.__objc_methname: 0xe63
+  __TEXT.__objc_methname: 0xe83
   __TEXT.__objc_methtype: 0x62b
   __TEXT.__objc_stubs: 0xa0
   __DATA_CONST.__got: 0xd0
-  __DATA_CONST.__const: 0xb890
+  __DATA_CONST.__const: 0xb898
   __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0xe0
   __DATA_CONST.__objc_superrefs: 0x20
-  __AUTH_CONST.__auth_got: 0xf38
+  __AUTH_CONST.__auth_got: 0xf40
   __AUTH_CONST.__const: 0x18c8
   __AUTH_CONST.__cfstring: 0xe0
-  __AUTH_CONST.__objc_const: 0x2108
+  __AUTH_CONST.__objc_const: 0x2148
   __AUTH.__objc_data: 0x140
   __AUTH.__data: 0x28
-  __DATA.__objc_ivar: 0x2f4
+  __DATA.__objc_ivar: 0x2fc
   __DATA.__data: 0xd00
-  __DATA.__bss: 0x548
+  __DATA.__bss: 0x540
   __DATA_DIRTY.__objc_data: 0x140
   __DATA_DIRTY.__data: 0x210
-  __DATA_DIRTY.__bss: 0xcb0
+  __DATA_DIRTY.__bss: 0xcb8
   __DATA_DIRTY.__common: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 219F9520-2140-364D-A2C0-EC885651F035
+  UUID: 9786D53A-15AE-30A8-92D6-BABA2AE82DD3
   Functions: 3133
-  Symbols:   7407
-  CStrings:  3641
+  Symbols:   7410
+  CStrings:  3643
 
Symbols:
+ GCC_except_table96
+ _OBJC_IVAR_$_boringssl_concrete_boringssl_ctx.pake_offered
+ _OBJC_IVAR_$_boringssl_concrete_boringssl_ctx.tls13_epsk_offered
+ ___block_descriptor_60_e8_32s_e9_B16?0^v8lu40l8s32l8
+ ___boringssl_context_certificate_request_callback_block_invoke.213
+ ___boringssl_context_evaluate_trust_async_external_block_invoke.204
+ ___boringssl_context_evaluate_trust_async_internal_block_invoke.196
+ ___boringssl_context_evaluate_trust_async_internal_block_invoke.200
+ ___boringssl_context_new_session_handler_block_invoke.238
+ ___boringssl_context_update_encryption_level_block_invoke.219
+ _nw_settings_get_pqtls_enabled_for_endpoint
+ _objc_retainAutoreleasedReturnValue
- GCC_except_table93
- ___block_descriptor_52_e9_B16?0^v8lu32l8
- ___boringssl_context_certificate_request_callback_block_invoke.211
- ___boringssl_context_evaluate_trust_async_external_block_invoke.202
- ___boringssl_context_evaluate_trust_async_internal_block_invoke.194
- ___boringssl_context_evaluate_trust_async_internal_block_invoke.198
- ___boringssl_context_new_session_handler_block_invoke.236
- ___boringssl_context_update_encryption_level_block_invoke.215
- _nw_settings_get_pqtls_enabled
CStrings:
+ "pake_offered"
+ "tls13_epsk_offered"

```
