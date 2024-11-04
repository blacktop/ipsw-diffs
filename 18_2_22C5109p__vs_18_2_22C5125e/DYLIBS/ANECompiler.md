## ANECompiler

> `/System/Library/PrivateFrameworks/ANECompiler.framework/ANECompiler`

```diff

-8.3.8.0.0
-  __TEXT.__text: 0x125a4f0
+8.3.15.0.0
+  __TEXT.__text: 0x125cf40
   __TEXT.__auth_stubs: 0x2140
   __TEXT.__init_offsets: 0x4
-  __TEXT.__const: 0x77e6c
-  __TEXT.__cstring: 0x915bf
-  __TEXT.__gcc_except_tab: 0x6e1e4
-  __TEXT.__oslogstring: 0x1611d
-  __TEXT.__unwind_info: 0x39338
+  __TEXT.__const: 0x7842c
+  __TEXT.__cstring: 0x91a8c
+  __TEXT.__gcc_except_tab: 0x6e084
+  __TEXT.__oslogstring: 0x161fd
+  __TEXT.__unwind_info: 0x394b8
   __TEXT.__eh_frame: 0x2488
   __DATA_CONST.__got: 0x1c8
-  __DATA_CONST.__const: 0x3630
+  __DATA_CONST.__const: 0x3640
   __AUTH_CONST.__auth_got: 0x10a8
   __AUTH_CONST.__auth_ptr: 0x80
-  __AUTH_CONST.__const: 0x71c88
-  __AUTH_CONST.__cfstring: 0x7f60
+  __AUTH_CONST.__const: 0x71e98
+  __AUTH_CONST.__cfstring: 0x7f80
   __AUTH.__data: 0x3618
   __AUTH.__thread_vars: 0xf0
   __AUTH.__thread_bss: 0x16c
   __DATA.__data: 0x6890
-  __DATA.__bss: 0xad60
+  __DATA.__bss: 0xb5c0
   __DATA.__common: 0x1558
   __DATA_DIRTY.__data: 0x80
   __DATA_DIRTY.__bss: 0xee0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libncurses.5.4.dylib
-  Functions: 72874
-  Symbols:   85357
-  CStrings:  15689
+  Functions: 72950
+  Symbols:   85416
+  CStrings:  15722
 
CStrings:
+ ".CpAllocationBeforePromotion.debug."
+ "Codegen Error: CropBatchSplit is not supported on this arch"
+ "CropBatchSplit is only used for Crop mode"
+ "Enforced per-TD latency violation.  Current latency: (%!f(MISSING) us).  Upper bound: (%!f(MISSING) us).  Related OpLayers: %!s(MISSING).  Compilation will FAIL.\n"
+ "Error in getting tensor format size in bits"
+ "Error: Dequant layer must have int8, uint8, int4 or e4m3 input format."
+ "Error: Not a valid format for LiveIO."
+ "Error: Palette data is empty."
+ "Error: Tensor Dimension Legalization failure.\n"
+ "Error: This weight does not have palette info."
+ "Error: Unsupported tensor format."
+ "Error: cannot get bit size of tensor format."
+ "Error: int4 kernel input is not a livein or a view."
+ "Error: palette info has empty palette data"
+ "GetDMASrcIndex failed."
+ "GetHWDMAMemoryFormat failed"
+ "Inconsistent texture information"
+ "Int4 Per-Cout Dequant is not supported"
+ "Invalid production of sx, sy, sz = %!z(MISSING)d for output channel. It should be in [%!d(MISSING), %!z(MISSING)u]"
+ "Latency for some tasks (%!f(MISSING) us) is too large (>%!f(MISSING) us) "
+ "NE-PE chain not supported due to hw errata rdar://118381021."
+ "No ANE layer can have more than 3 incoming layers."
+ "Only PE layers can be ternary."
+ "Palette vector size cannot be zero"
+ "Tensor Dimension Legalization failure"
+ "Tensor Dimension Legalizer works for ANE Layer only."
+ "Tensor dimension legalizer for layer %!s(MISSING) failed!\n"
+ "Tensor format is not supported by Hardware DMA."
+ "Tensor format should be valid"
+ "Tensor with the int4 format must have an interleave factor of 8"
+ "TensorDimensionLegalizationFailure"
+ "Transpose must have only 1 input"
+ "Validation after tensor dimension legalization result failed!\n"
+ "ZinMirActivationPreV7::GetLut() failed\n"
+ "ZinMirPETransposeFusion failure"
+ "ZinTensorFormatGetSizeInBytes cannot support less than 1 byte formats."
+ "after_tensor_dimension_legalization"
+ "h16c"
+ "int4:t23=r1;-8;7"
+ "internal error"
+ "t6041"
+ "unsupported C stride: %!d(MISSING) (in elements), or %!l(MISSING)d (in bytes) is not %!z(MISSING)d bytes aligned."
+ "unsupported D stride: %!d(MISSING) (in elements), or %!l(MISSING)d (in bytes) is not %!z(MISSING)d bytes aligned."
+ "unsupported H stride: %!d(MISSING) (in elements), or %!l(MISSING)d (in bytes) is not %!z(MISSING)d bytes aligned."
+ "unsupported N stride: %!d(MISSING) (in elements), or %!l(MISSING)d (in bytes) is not %!z(MISSING)d bytes aligned."
- "Error: Dequant layer must have int8, uint8 or e4m3 input format."
- "Invalid information for palettized kernels."
- "Invalid input tensor dimension in IR\n"
- "Invalid output tensor dimension in IR\n"
- "Promotion from resident to inplace must succeed"
- "The dim (=%!z(MISSING)d) at axis %!s(MISSING) exceeds the upper_bound %!z(MISSING)d"
- "The dim (=%!z(MISSING)d) at axis %!s(MISSING) is below the lower_bound %!z(MISSING)d"
- "Unknown axis"
- "unsupported C stride: %!d(MISSING) (in elements), or %!l(MISSING)d (in bytes) is not 64 bytes aligned."
- "unsupported D stride: %!d(MISSING) (in elements), or %!l(MISSING)d (in bytes) is not 64 bytes aligned."
- "unsupported H stride: %!d(MISSING) (in elements), or %!l(MISSING)d (in bytes) is not 64 bytes aligned."
- "unsupported N stride: %!d(MISSING) (in elements), or %!l(MISSING)d (in bytes) is not 64 bytes aligned."

```
