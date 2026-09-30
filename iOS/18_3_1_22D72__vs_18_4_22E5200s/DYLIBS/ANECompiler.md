## ANECompiler

> `/System/Library/PrivateFrameworks/ANECompiler.framework/ANECompiler`

```diff

-8.4.2.0.0
-  __TEXT.__text: 0x125dba4
-  __TEXT.__auth_stubs: 0x2140
+8.5.1.0.0
+  __TEXT.__text: 0x11bd7c0
+  __TEXT.__auth_stubs: 0x2130
   __TEXT.__init_offsets: 0x4
-  __TEXT.__const: 0x7852c
-  __TEXT.__cstring: 0x91af7
-  __TEXT.__gcc_except_tab: 0x6e114
-  __TEXT.__oslogstring: 0x161fd
-  __TEXT.__unwind_info: 0x394e0
-  __TEXT.__eh_frame: 0x2488
-  __DATA_CONST.__got: 0x1c8
-  __DATA_CONST.__const: 0x3640
-  __AUTH_CONST.__auth_got: 0x10a8
+  __TEXT.__const: 0x7871c
+  __TEXT.__cstring: 0x91c93
+  __TEXT.__gcc_except_tab: 0x6f330
+  __TEXT.__oslogstring: 0x162e0
+  __TEXT.__unwind_info: 0x38330
+  __TEXT.__eh_frame: 0x2560
+  __DATA_CONST.__got: 0x1e0
+  __DATA_CONST.__const: 0x3628
+  __AUTH_CONST.__auth_got: 0x10a0
   __AUTH_CONST.__auth_ptr: 0x80
-  __AUTH_CONST.__const: 0x71ec8
+  __AUTH_CONST.__const: 0x71ee0
   __AUTH_CONST.__cfstring: 0x7f80
   __AUTH.__data: 0x3618
   __AUTH.__thread_vars: 0xf0
-  __AUTH.__thread_bss: 0x16c
+  __AUTH.__thread_bss: 0x170
   __DATA.__data: 0x6890
-  __DATA.__bss: 0xb5c0
+  __DATA.__bss: 0xb4b8
   __DATA.__common: 0x1558
   __DATA_DIRTY.__data: 0x80
-  __DATA_DIRTY.__bss: 0xee0
+  __DATA_DIRTY.__bss: 0xff0
   __DATA_DIRTY.__common: 0x30
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libncurses.5.4.dylib
-  Functions: 72962
-  Symbols:   85427
-  CStrings:  15725
+  Functions: 73969
+  Symbols:   95365
+  CStrings:  15735
 
Symbols:
+ __ZNSt3__117bad_function_callD1Ev
+ __ZTINSt3__117bad_function_callE
+ __ZTVNSt3__117bad_function_callE
+ ___mulsc3
- __ZNKSt9exception4whatEv
- _logb
- _scalbn
CStrings:
+ "ANE internal failure: MirInfo transfer error"
+ "API should be called for root tensor only"
+ "Allocation decision must be L2-dep"
+ "Allocation decision must be chain"
+ "Allocation decision must exist"
+ "Invalid memory pressure analyzer while resident/inplace to l2-dep update in %s"
+ "Invalid resident/inplace to l2-dep update in %s"
+ "Invalid schedule for L2-dep"
+ "Layers cannot be null"
+ "Layers must have valid schedule"
+ "MIR Prepare Layers: Collapse Transposes Around Concat failed!\n"
+ "Memory pressure analyzer has DMA with invalid live range"
+ "Memory pressure analyzer has tensor with invalid live range"
+ "Single outgoing transpose is allowed"
+ "[MirOpt::CollapseSymmetricTransposeAroundConcat] Failed to collapse transposes around concat: %s"
+ "[MirOpt::CollapseSymmetricTransposeAroundConcat] Successfully collapsed transposes around concat: %s"
+ "_to_goc"
+ "after_collapse_transposes_around_concat"
+ "n301"
- " \t\r"
- ">>"
- "Allocation decision must exist."
- "Error: Invalid NE cateogy given.\n"
- "Incorrect config"
- "Invalid inplaceable tensor"
- "Liverange must exist."
- "Missing handling of options in ZinIrCompilerParameters"
- "Producer must be engine layer."

```
