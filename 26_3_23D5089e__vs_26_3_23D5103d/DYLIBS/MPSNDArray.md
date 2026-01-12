## MPSNDArray

> `/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSNDArray.framework/MPSNDArray`

```diff

-129.3.2.0.0
-  __TEXT.__text: 0x10c4a8
+129.3.5.0.0
+  __TEXT.__text: 0x10cfb0
   __TEXT.__auth_stubs: 0xb10
   __TEXT.__objc_methlist: 0x6aa4
   __TEXT.__const: 0x895e8
-  __TEXT.__gcc_except_tab: 0x4154
-  __TEXT.__cstring: 0xe2e2
+  __TEXT.__gcc_except_tab: 0x41a4
+  __TEXT.__cstring: 0xe474
   __TEXT.__unwind_info: 0x1878
   __TEXT.__eh_frame: 0x68
   __TEXT.__objc_classname: 0x1c59

   __TEXT.__objc_methtype: 0x1ed4
   __TEXT.__objc_stubs: 0x3360
   __DATA_CONST.__got: 0x338
-  __DATA_CONST.__const: 0xedd0
+  __DATA_CONST.__const: 0xf050
   __DATA_CONST.__objc_classlist: 0x848
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x820
   __AUTH_CONST.__auth_got: 0x598
-  __AUTH_CONST.__const: 0x4080
-  __AUTH_CONST.__cfstring: 0x6f80
-  __AUTH_CONST.__objc_const: 0xe8d8
+  __AUTH_CONST.__const: 0x4060
+  __AUTH_CONST.__cfstring: 0x7020
+  __AUTH_CONST.__objc_const: 0xe918
   __AUTH.__objc_data: 0x50
-  __DATA.__objc_ivar: 0x6b0
+  __DATA.__objc_ivar: 0x6b8
   __DATA.__data: 0x9c4
-  __DATA.__bss: 0x608
+  __DATA.__bss: 0x600
   __DATA_DIRTY.__objc_data: 0x5280
   __DATA_DIRTY.__bss: 0x78
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: CA3D151C-4BD7-32C7-8D71-0FB3E2EA2891
+  UUID: 6A717907-3F80-3099-A330-DCD30C74B73A
   Functions: 2244
-  Symbols:   7571
-  CStrings:  3745
+  Symbols:   7570
+  CStrings:  3757
 
Symbols:
+ GCC_except_table15
+ __ZL27getWinogradA18PrecisionModeP9MPSKernel11MPSDataTypeS1_S1_
+ ___block_literal_global.205
+ ___block_literal_global.208
+ ___block_literal_global.211
+ ___block_literal_global.253
+ ___block_literal_global.284
+ ___block_literal_global.316
+ ___block_literal_global.319
+ ___block_literal_global.343
+ ___block_literal_global.404
- GCC_except_table14
- ____ZL22MPSSDPAForceMatrixUnitv_block_invoke
- ___block_literal_global.190
- ___block_literal_global.193
- ___block_literal_global.196
- ___block_literal_global.238
- ___block_literal_global.269
- ___block_literal_global.272
- ___block_literal_global.315
- ___block_literal_global.318
- ___block_literal_global.342
- ___block_literal_global.407
CStrings:
+ "A14 Encoder: Failed, fall back to vector based SDPA kernel\n"
+ "A18 Encoder: Failed, fall back to A14 Encoder\n"
+ "AllowConvertingOperandsFromFP32ToFP19 flag is set. Running A18 MXU Winograd using fp19 precision.\n"
+ "per_tensor_quantized_sdpa_tile_fwd_a20_16x16x16_doEdgeCheck"
+ "per_tensor_quantized_sdpa_tile_fwd_a20_16x16x16_noEdgeCheck"
+ "sdpa_tile_fwd_a20_16x16x16_doEdgeCheck"
+ "sdpa_tile_fwd_a20_16x16x16_noEdgeCheck"
+ "sdpa_tile_fwd_reduction"
- "MPSNDARRAY_SDPA_FORCE_MXU"

```
