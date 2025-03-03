## ANECompiler

> `/System/Library/PrivateFrameworks/ANECompiler.framework/ANECompiler`

```diff

-8.4.2.0.0
-  __TEXT.__text: 0x125dba4
-  __TEXT.__auth_stubs: 0x2140
+8.5.2.0.0
+  __TEXT.__text: 0x11c11ec
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
+  __TEXT.__const: 0x78a3c
+  __TEXT.__cstring: 0x92084
+  __TEXT.__gcc_except_tab: 0x6f64c
+  __TEXT.__oslogstring: 0x1630f
+  __TEXT.__unwind_info: 0x38478
+  __TEXT.__eh_frame: 0x2560
+  __DATA_CONST.__got: 0x1e0
+  __DATA_CONST.__const: 0x3628
+  __AUTH_CONST.__auth_got: 0x10a0
   __AUTH_CONST.__auth_ptr: 0x80
-  __AUTH_CONST.__const: 0x71ec8
+  __AUTH_CONST.__const: 0x72090
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
+  Functions: 74033
+  Symbols:   95446
+  CStrings:  15758
 
Symbols:
+ __ZNSt3__117bad_function_callD1Ev
+ __ZTINSt3__117bad_function_callE
+ __ZTVNSt3__117bad_function_callE
+ ___mulsc3
- __ZNKSt9exception4whatEv
- _logb
- _scalbn
CStrings:
+ "/Library/Caches/com.apple.xbs/Sources/ANECompiler/libs/inference/compiler/ZinIrSchedule/src/ZinIrExecutionBehavior.cpp"
+ "/Library/Caches/com.apple.xbs/Sources/ANECompiler/libs/inference/compiler/ZinMirPrepare/src/ZinMirActiveNE.cpp"
+ "ANE internal failure: MirInfo transfer error"
+ "API should be called for root tensor only"
+ "Allocation decision must be L2-dep"
+ "Allocation decision must be chain"
+ "Allocation decision must exist"
+ "Both tasks must exist to perform promotion"
+ "Computing temporary mir-info must succeed"
+ "Config : "
+ "Error: Splitting NEConv with kernel tensor in batch, %s"
+ "Execution behavior must exist"
+ "Failure to enumerate tile height candidates."
+ "Failure to enumerate wu candidates."
+ "Forking node and its outgoing layer must be connected."
+ "GQA must start with dual input matmul"
+ "Info: Optimized WAW between TID=%zi -> TID=%zi"
+ "Internal Execution Behavior Error"
+ "Invalid basic block schedule with missing layers"
+ "Invalid liverange"
+ "Invalid memory pressure analyzer while resident/inplace to l2-dep update in %s"
+ "Invalid resident/inplace to l2-dep update in %s"
+ "Invalid schedule for L2-dep"
+ "Invalid schedule set during parallel execution update"
+ "Layer schedule must be set"
+ "Layers cannot be null"
+ "Layers must have valid schedule"
+ "MHA must start with single input view"
+ "MIR Prepare Layers: Collapse Transposes Around Concat failed!\n"
+ "Memory pressure analyzer has DMA with invalid live range"
+ "Memory pressure analyzer has tensor with invalid live range"
+ "Must be either MHA or GQA"
+ "ShouldSkipFurtherCompression, "
+ "Single outgoing transpose is allowed"
+ "Task must exist to perform promotion"
+ "Tensor family util must be initialized to use this API."
+ "Tensor family util must be set for memory pressure tracking in scheduler"
+ "TrySplitByBatch"
+ "[MirOpt::CollapseSymmetricTransposeAroundConcat] Failed to collapse transposes around concat: %s"
+ "[MirOpt::CollapseSymmetricTransposeAroundConcat] Successfully collapsed transposes around concat: %s"
+ "_to_goc"
+ "after_collapse_transposes_around_concat"
+ "initialize set must be successful"
+ "n301"
- " \t\r"
- ">>"
- "Allocation decision must exist."
- "Error: Invalid NE cateogy given.\n"
- "Incorrect config"
- "Internal CP Allocation Error"
- "Invalid inplaceable tensor"
- "It is not a qualifying attention branch"
- "Liverange must exist."
- "Missing handling of options in ZinIrCompilerParameters"
- "Producer must be engine layer."

```
