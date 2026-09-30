## libboringssl.dylib

> `/usr/lib/libboringssl.dylib`

```diff

-532.0.7.0.0
-  __TEXT.__text: 0x9f9d8
+532.0.10.0.0
+  __TEXT.__text: 0x9fb0c
   __TEXT.__auth_stubs: 0x1e20
   __TEXT.__objc_methlist: 0x1dc
   __TEXT.__cstring: 0x106bd
   __TEXT.__const: 0xfef8
   __TEXT.__oslogstring: 0x5be2
   __TEXT.__gcc_except_tab: 0x2940
-  __TEXT.__unwind_info: 0x2488
+  __TEXT.__unwind_info: 0x2490
   __TEXT.__eh_frame: 0x130
   __TEXT.__objc_classname: 0x240
   __TEXT.__objc_methname: 0xe4d

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: D9D192BE-BC14-3DCE-9FE3-F05AC28B62BE
-  Functions: 3129
-  Symbols:   7396
+  UUID: 76FFE13B-78D5-3721-B99D-5F8EE1051931
+  Functions: 3131
+  Symbols:   7400
   CStrings:  3638
 
Symbols:
+ GCC_except_table120
+ GCC_except_table153
+ _SSL_renegotiate_pending
+ ___boringssl_context_certificate_request_callback_block_invoke.211
+ ___boringssl_context_new_session_handler_block_invoke.236
+ ___boringssl_context_update_encryption_level_block_invoke.215
+ ___boringssl_context_update_encryption_level_block_invoke.217
- GCC_except_table119
- GCC_except_table152
- ___boringssl_context_new_session_handler_block_invoke.234
- ___boringssl_context_update_encryption_level_block_invoke.212
- ___boringssl_context_update_encryption_level_block_invoke.214
Functions:
- ___boringssl_context_update_encryption_level_block_invoke.214
+ _SSL_renegotiate_pending
~ _boringssl_context_certificate_request_callback : 1128 -> 1316
~ ___boringssl_context_certificate_request_callback_block_invoke : 196 -> 80
+ ___boringssl_context_certificate_request_callback_block_invoke.211
+ ___boringssl_context_update_encryption_level_block_invoke.217

```
