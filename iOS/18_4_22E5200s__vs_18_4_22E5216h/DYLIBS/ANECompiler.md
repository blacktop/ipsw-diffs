## ANECompiler

> `/System/Library/PrivateFrameworks/ANECompiler.framework/ANECompiler`

```diff

-8.5.1.0.0
-  __TEXT.__text: 0x11bd7c0
+8.5.2.0.0
+  __TEXT.__text: 0x11c11ec
   __TEXT.__auth_stubs: 0x2130
   __TEXT.__init_offsets: 0x4
-  __TEXT.__const: 0x7871c
-  __TEXT.__cstring: 0x91c93
-  __TEXT.__gcc_except_tab: 0x6f330
-  __TEXT.__oslogstring: 0x162e0
-  __TEXT.__unwind_info: 0x38330
+  __TEXT.__const: 0x78a3c
+  __TEXT.__cstring: 0x92084
+  __TEXT.__gcc_except_tab: 0x6f64c
+  __TEXT.__oslogstring: 0x1630f
+  __TEXT.__unwind_info: 0x38478
   __TEXT.__eh_frame: 0x2560
   __DATA_CONST.__got: 0x1e0
   __DATA_CONST.__const: 0x3628
   __AUTH_CONST.__auth_got: 0x10a0
   __AUTH_CONST.__auth_ptr: 0x80
-  __AUTH_CONST.__const: 0x71ee0
+  __AUTH_CONST.__const: 0x72090
   __AUTH_CONST.__cfstring: 0x7f80
   __AUTH.__data: 0x3618
   __AUTH.__thread_vars: 0xf0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libncurses.5.4.dylib
-  Functions: 73969
-  Symbols:   95365
-  CStrings:  15735
+  Functions: 74033
+  Symbols:   95446
+  CStrings:  15758
 
CStrings:
+ "/Library/Caches/com.apple.xbs/Sources/ANECompiler/libs/inference/compiler/ZinIrSchedule/src/ZinIrExecutionBehavior.cpp"
+ "/Library/Caches/com.apple.xbs/Sources/ANECompiler/libs/inference/compiler/ZinMirPrepare/src/ZinMirActiveNE.cpp"
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
+ "Invalid schedule set during parallel execution update"
+ "Layer schedule must be set"
+ "MHA must start with single input view"
+ "Must be either MHA or GQA"
+ "ShouldSkipFurtherCompression, "
+ "Task must exist to perform promotion"
+ "Tensor family util must be initialized to use this API."
+ "Tensor family util must be set for memory pressure tracking in scheduler"
+ "TrySplitByBatch"
+ "initialize set must be successful"
- "Internal CP Allocation Error"
- "It is not a qualifying attention branch"

```
