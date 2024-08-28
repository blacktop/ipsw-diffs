## ANECompiler

> `/System/Library/PrivateFrameworks/ANECompiler.framework/ANECompiler`

```diff

-8.2.16.0.0
-  __TEXT.__text: 0x11c39e8
-  __TEXT.__auth_stubs: 0x20d0
+8.3.2.0.0
+  __TEXT.__text: 0x11c70cc
+  __TEXT.__auth_stubs: 0x20f0
   __TEXT.__init_offsets: 0x8
-  __TEXT.__const: 0x750ec
-  __TEXT.__cstring: 0x8c5e7
-  __TEXT.__gcc_except_tab: 0x6c414
-  __TEXT.__oslogstring: 0x15e07
-  __TEXT.__unwind_info: 0x38360
+  __TEXT.__const: 0x7577c
+  __TEXT.__cstring: 0x8c7fe
+  __TEXT.__gcc_except_tab: 0x6c74c
+  __TEXT.__oslogstring: 0x15e6e
+  __TEXT.__unwind_info: 0x38410
   __TEXT.__eh_frame: 0x11b4
   __DATA_CONST.__got: 0x1c8
-  __DATA_CONST.__const: 0x3610
-  __AUTH_CONST.__auth_got: 0x1070
+  __DATA_CONST.__const: 0x3618
+  __AUTH_CONST.__auth_got: 0x1080
   __AUTH_CONST.__auth_ptr: 0x80
-  __AUTH_CONST.__const: 0x71350
-  __AUTH_CONST.__cfstring: 0x7f00
+  __AUTH_CONST.__const: 0x71650
+  __AUTH_CONST.__cfstring: 0x7f20
   __AUTH.__data: 0x3618
   __AUTH.__thread_vars: 0xf0
   __AUTH.__thread_bss: 0x16c
-  __DATA.__data: 0x6540
-  __DATA.__bss: 0x9ca0
+  __DATA.__data: 0x6548
+  __DATA.__bss: 0x9cc8
   __DATA.__common: 0x1558
   __DATA_DIRTY.__data: 0x80
   __DATA_DIRTY.__common: 0x38

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libncurses.5.4.dylib
-  Functions: 71285
-  Symbols:   83456
-  CStrings:  15467
+  Functions: 71346
+  Symbols:   83517
+  CStrings:  15481
 
Symbols:
+ __ZNSt3__14__fs10filesystem8__statusERKNS1_4pathEPNS_10error_codeE
+ __ZNSt3__14__fs10filesystem11__file_sizeERKNS1_4pathEPNS_10error_codeE
CStrings:
+ "concat_1"
+ "EnableNoiseReductionTiling"
+ "Error: Unable to chop PEEW (name:%!s(MISSING)) for chaining canonicalization\n"
+ " bytes)"
+ "regular_conv"
+ "enable-noise-reduction-tiling"
+ "Error: provided tile sizes cannot cover all Couts of neconv\n"
+ " bytes) exceeds the maximum ("
+ "Enable noise reduction tiling: %!d(MISSING)\n"
+ "Weight file size ("
+ "peew"
+ "NEConv has per-cout-palette-lut, cannot split the kernel of this conv under specified tile sizes in chaining canonicalization."
+ "NEConv kind is not normal, cannot split the kernel of this conv under specified tile sizes in chaining canonicalization."
+ "NEConv don't have enough channels to make the kernel split based on given tile size."

```
