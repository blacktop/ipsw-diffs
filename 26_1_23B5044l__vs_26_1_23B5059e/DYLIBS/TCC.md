## TCC

> `/System/Library/PrivateFrameworks/TCC.framework/TCC`

```diff

-857.0.7.0.0
-  __TEXT.__text: 0x1306c
-  __TEXT.__auth_stubs: 0xae0
+858.0.1.0.0
+  __TEXT.__text: 0x13690
+  __TEXT.__auth_stubs: 0xaf0
   __TEXT.__objc_methlist: 0x11c
-  __TEXT.__cstring: 0x2b7e
-  __TEXT.__oslogstring: 0x101b
+  __TEXT.__cstring: 0x2bb2
+  __TEXT.__oslogstring: 0x10cd
   __TEXT.__const: 0x398
-  __TEXT.__unwind_info: 0x530
+  __TEXT.__unwind_info: 0x550
   __TEXT.__objc_classname: 0x120
   __TEXT.__objc_methname: 0x147
   __TEXT.__objc_methtype: 0xb5
   __DATA_CONST.__got: 0xc8
-  __DATA_CONST.__const: 0x1538
+  __DATA_CONST.__const: 0x1588
   __DATA_CONST.__objc_classlist: 0x68
   __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0xa8
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x570
+  __AUTH_CONST.__auth_got: 0x578
   __AUTH_CONST.__const: 0x298
   __AUTH_CONST.__cfstring: 0x1420
   __AUTH_CONST.__objc_const: 0xe50

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 6645B72D-B372-3059-88BF-FE3706921F2C
-  Functions: 488
-  Symbols:   1516
-  CStrings:  742
+  UUID: 2DA7C40A-CB8E-3E0C-AEB9-12B50ADED1B2
+  Functions: 496
+  Symbols:   1541
+  CStrings:  749
 
Symbols:
+ _TCCIntegrityFlagCheck
+ _TCCIntegrityFlagReset
+ ___TCCIntegrityFlagCheck_block_invoke
+ ___TCCIntegrityFlagCheck_block_invoke.cold.1
+ ___TCCIntegrityFlagCheck_block_invoke.cold.2
+ ___TCCIntegrityFlagCheck_block_invoke.cold.3
+ ___TCCIntegrityFlagCheck_block_invoke.cold.4
+ ___TCCIntegrityFlagReset_block_invoke
+ ___TCCIntegrityFlagReset_block_invoke.cold.1
+ ___TCCIntegrityFlagReset_block_invoke.cold.2
+ ___TCCIntegrityFlagReset_block_invoke.cold.3
+ ___TCCIntegrityFlagReset_block_invoke.cold.4
+ ___block_descriptor_tmp.476
+ ___block_descriptor_tmp.477
+ ___block_descriptor_tmp.483
+ ___block_descriptor_tmp.500
+ ___block_descriptor_tmp.505
+ ___block_descriptor_tmp.506
+ ___block_descriptor_tmp.510
+ ___block_descriptor_tmp.514
+ ___block_descriptor_tmp.515
+ ___block_literal_global.502
+ _xpc_dictionary_create_empty
- ___block_descriptor_tmp.480
- ___block_descriptor_tmp.494
- ___block_descriptor_tmp.502
- ___block_descriptor_tmp.503
- ___block_descriptor_tmp.507
- ___block_descriptor_tmp.508
- ___block_descriptor_tmp.512
- ___block_literal_global.496
CStrings:
+ "Failed to check system flag status: %{public}s"
+ "Failed to reset system flag status: %{public}s"
+ "TCCIntegrityFlagCheck"
+ "TCCIntegrityFlagReset"
+ "success"
+ "tccd declined to check system flag status"
+ "tccd declined to reset system flag status"

```
