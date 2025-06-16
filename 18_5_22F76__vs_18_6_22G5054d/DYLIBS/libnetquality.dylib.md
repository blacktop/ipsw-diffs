## libnetquality.dylib

> `/usr/lib/libnetquality.dylib`

```diff

-147.120.6.0.0
-  __TEXT.__text: 0x187f0
-  __TEXT.__auth_stubs: 0xb70
-  __TEXT.__objc_methlist: 0x169c
+147.140.5.0.0
+  __TEXT.__text: 0x188e8
+  __TEXT.__auth_stubs: 0xb80
+  __TEXT.__objc_methlist: 0x16a4
   __TEXT.__const: 0x190
-  __TEXT.__gcc_except_tab: 0x52c
-  __TEXT.__cstring: 0x23ec
-  __TEXT.__oslogstring: 0x162a
+  __TEXT.__gcc_except_tab: 0x538
+  __TEXT.__cstring: 0x2409
+  __TEXT.__oslogstring: 0x1656
   __TEXT.__unwind_info: 0x4d0
   __TEXT.__objc_classname: 0x315
-  __TEXT.__objc_methname: 0x3e46
+  __TEXT.__objc_methname: 0x3e60
   __TEXT.__objc_methtype: 0xc57
-  __TEXT.__objc_stubs: 0x3280
+  __TEXT.__objc_stubs: 0x32a0
   __DATA_CONST.__got: 0x178
   __DATA_CONST.__const: 0x5d8
   __DATA_CONST.__objc_classlist: 0xc0
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xf00
+  __DATA_CONST.__objc_selrefs: 0xf08
   __DATA_CONST.__objc_superrefs: 0xa0
   __DATA_CONST.__objc_arraydata: 0x58
-  __AUTH_CONST.__auth_got: 0x5c8
+  __AUTH_CONST.__auth_got: 0x5d0
   __AUTH_CONST.__const: 0x40
   __AUTH_CONST.__cfstring: 0x1940
   __AUTH_CONST.__objc_const: 0x36b0

   - /System/Library/PrivateFrameworks/Rapport.framework/Rapport
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: D423B61B-F44B-3916-9BFB-A89A50E1890E
-  Functions: 555
-  Symbols:   2282
-  CStrings:  1591
+  UUID: 15C478DA-88F3-35C2-964B-DC8DAC0098AB
+  Functions: 556
+  Symbols:   2286
+  CStrings:  1594
 
Symbols:
+ -[NetworkQualityConfiguration hasCustomConfigurationSet]
+ ___56-[NetworkQualityExecutions execDLWithCompletionHandler:]_block_invoke.175
+ ___56-[NetworkQualityExecutions execDLWithCompletionHandler:]_block_invoke.175.cold.1
+ ___56-[NetworkQualityExecutions execULWithCompletionHandler:]_block_invoke.181
+ ___56-[NetworkQualityExecutions execULWithCompletionHandler:]_block_invoke.181.cold.1
+ ___62-[NetworkQualityExecutions execParallelWithCompletionHandler:]_block_invoke.188.cold.1
+ ___62-[NetworkQualityExecutions execParallelWithCompletionHandler:]_block_invoke.190
+ ___62-[NetworkQualityExecutions execParallelWithCompletionHandler:]_block_invoke.190.cold.1
+ _network_config_get_l4s_enabled
+ _objc_msgSend$hasCustomConfigurationSet
- ___56-[NetworkQualityExecutions execDLWithCompletionHandler:]_block_invoke.174
- ___56-[NetworkQualityExecutions execDLWithCompletionHandler:]_block_invoke.174.cold.1
- ___56-[NetworkQualityExecutions execULWithCompletionHandler:]_block_invoke.180
- ___56-[NetworkQualityExecutions execULWithCompletionHandler:]_block_invoke.180.cold.1
- ___62-[NetworkQualityExecutions execParallelWithCompletionHandler:]_block_invoke.187
- ___62-[NetworkQualityExecutions execParallelWithCompletionHandler:]_block_invoke.187.cold.1
- ___62-[NetworkQualityExecutions execParallelWithCompletionHandler:]_block_invoke.189.cold.1
Functions:
~ ___53-[NetworkQualityExecutions runWithCompletionHandler:]_block_invoke : 2392 -> 2608
+ -[NetworkQualityConfiguration hasCustomConfigurationSet]
CStrings:
+ "%s:%u - Using L4S Server pool for test run."
+ "hasCustomConfigurationSet"
+ "mensura-l4s.networking.apple"

```
