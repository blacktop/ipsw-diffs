## libusrtcp.dylib

> `/usr/lib/libusrtcp.dylib`

```diff

-5569.40.91.0.0
-  __TEXT.__text: 0x5c824
+5569.40.106.0.1
+  __TEXT.__text: 0x5ca8c
   __TEXT.__auth_stubs: 0x1020
   __TEXT.__const: 0x244
-  __TEXT.__oslogstring: 0xe6c3
-  __TEXT.__cstring: 0x1a22
+  __TEXT.__oslogstring: 0xe713
+  __TEXT.__cstring: 0x1a37
   __TEXT.__unwind_info: 0x458
   __DATA_CONST.__got: 0xa0
   __DATA_CONST.__const: 0x3e8

   __AUTH_CONST.__const: 0x1a8
   __AUTH.__data: 0x220
   __DATA.__data: 0x10
-  __DATA.__bss: 0x6c0
+  __DATA.__bss: 0x6d0
   __DATA_DIRTY.__data: 0x184
   __DATA_DIRTY.__bss: 0x170
   - /System/Library/Frameworks/Network.framework/Network
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 8454F464-64EA-31A7-BDD2-166FD42E6923
-  Functions: 326
-  Symbols:   1007
-  CStrings:  1116
+  UUID: 0343EF9B-0139-3466-BFA7-66F91C5B9E50
+  Functions: 327
+  Symbols:   1009
+  CStrings:  1118
 
Symbols:
+ _____nw_frame_array_finalize_block_invoke.586
+ _____nw_signpost_is_enabled_block_invoke.495
+ ___block_descriptor_tmp.487
+ ___block_descriptor_tmp.8.489
+ ___block_descriptor_tmp.800
+ ___block_literal_global.488
+ ___block_literal_global.798
+ _tcp_rst_rlc_compress
- _____nw_frame_array_finalize_block_invoke.594
- _____nw_signpost_is_enabled_block_invoke.503
- ___block_descriptor_tmp.495
- ___block_descriptor_tmp.8.497
- ___block_descriptor_tmp.808
- ___block_literal_global.496
- ___block_literal_global.806
Functions:
~ _tcp_output : 32860 -> 32864
+ _tcp_rst_rlc_compress
CStrings:
+ "%{public}s %{public}s RST RLC compression: compressed %u RST segments [%hu:%hu]"
+ "tcp_rst_rlc_compress"

```
