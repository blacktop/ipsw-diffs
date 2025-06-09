## libRPAC.dylib

> `/usr/lib/libRPAC.dylib`

```diff

-88.0.0.0.0
-  __TEXT.__text: 0x92424
-  __TEXT.__auth_stubs: 0xac0
+95.0.0.0.0
+  __TEXT.__text: 0x927f8
+  __TEXT.__auth_stubs: 0xb20
   __TEXT.__objc_stubs: 0x1a0
   __TEXT.__init_offsets: 0x4
-  __TEXT.__cstring: 0x5140
-  __TEXT.__gcc_except_tab: 0x5c
+  __TEXT.__cstring: 0x51ef
+  __TEXT.__gcc_except_tab: 0xd4
   __TEXT.__const: 0x1d58
   __TEXT.__objc_methname: 0x13b
   __TEXT.__oslogstring: 0x1d
   __TEXT.__objc_classname: 0x1
-  __TEXT.__unwind_info: 0x330
-  __DATA_CONST.__auth_got: 0x578
-  __DATA_CONST.__got: 0x140
+  __TEXT.__unwind_info: 0x358
+  __DATA_CONST.__auth_got: 0x5a8
+  __DATA_CONST.__got: 0x148
   __DATA_CONST.__auth_ptr: 0x10
   __DATA_CONST.__const: 0x3f0
   __DATA_CONST.__cfstring: 0x260

   __DATA_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__interpose: 0x220
   __DATA.__objc_selrefs: 0x88
-  __DATA.__data: 0x7c4
-  __DATA.__common: 0x800e8
-  __DATA.__bss: 0x5807d8
+  __DATA.__data: 0x7cc
+  __DATA.__common: 0x80168
+  __DATA.__bss: 0x5806e0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/ImageIO.framework/ImageIO

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 9B38C7C0-72C5-38E8-8FFC-8D177FD80591
-  Functions: 279
-  Symbols:   730
-  CStrings:  652
+  UUID: 88FE7B5C-8C2E-31DD-AE29-A98B4DE0BF86
+  Functions: 280
+  Symbols:   744
+  CStrings:  657
 
Symbols:
+ GCC_except_table14
+ GCC_except_table2
+ GCC_except_table3
+ __ZSt28__throw_bad_array_new_lengthB8ne200100v
+ __ZTISt9exception
+ __ZZ22initializePrimitiveMapvE22initialization_success
+ ___cxa_begin_catch
+ ___cxa_end_catch
+ __block_descriptor_tmp.31
+ __block_descriptor_tmp.36
+ __block_descriptor_tmp.39
+ __block_literal_global.33
+ __block_literal_global.38
+ __block_literal_global.41
+ _atoll
+ _dispatch_queue_attr_make_with_qos_class
+ _dispatch_queue_create
+ _dispatch_sync
+ _envDisableXPCChecks
+ _envPriorityInversionDetectionOnMainThreadOnly
+ _envXPCWaitThreshold
+ _objc_retain_x2
+ _strnstr
+ generateCulledBacktrace.issueQueueOrWorkloop
+ qosWaiterSignallerInvariantCheck.cold.2
- __ZSt28__throw_bad_array_new_lengthB8ne190102v
- __Znwm
- __block_descriptor_tmp.30
- __block_descriptor_tmp.35
- __block_descriptor_tmp.38
- __block_literal_global.32
- __block_literal_global.37
- __block_literal_global.40
- _dispatch_async_and_wait
- generateCulledBacktrace.issueWorkloop
Functions:
~ __replacement_NSURLConnection_sendSynchronousRequest_returningResponse_error : 84 -> 180
~ __ZNSt3__112__hash_tableINS_17__hash_value_typeIl15sqliteDBState_tEENS_22__unordered_map_hasherIlS3_NS_4hashIlEENS_8equal_toIlEELb1EEENS_21__unordered_map_equalIlS3_S8_S6_Lb1EEENS_9allocatorIS3_EEE25__emplace_unique_key_argsIlJRKNS_21piecewise_construct_tENS_5tupleIJRKlEEENSJ_IJEEEEEENS_4pairINS_15__hash_iteratorIPNS_11__hash_nodeIS3_PvEEEEbEERKT_DpOT0_ : 636 -> 652
~ __ZNSt3__112__hash_tableINS_17__hash_value_typeIl15sqliteDBState_tEENS_22__unordered_map_hasherIlS3_NS_4hashIlEENS_8equal_toIlEELb1EEENS_21__unordered_map_equalIlS3_S8_S6_Lb1EEENS_9allocatorIS3_EEE11__do_rehashILb1EEEvm : 348 -> 356
~ __ZNSt3__112__hash_tableINS_17__hash_value_typeIl15sqliteDBState_tEENS_22__unordered_map_hasherIlS3_NS_4hashIlEENS_8equal_toIlEELb1EEENS_21__unordered_map_equalIlS3_S8_S6_Lb1EEENS_9allocatorIS3_EEE6removeENS_21__hash_const_iteratorIPNS_11__hash_nodeIS3_PvEEEE : 308 -> 316
~ _GetThreadLocalData : 164 -> 168
~ ___library_initializer : 2116 -> 2368
~ _interposed_dispatch_group_wait : 336 -> 364
~ _shouldFlag : 256 -> 272
~ _isSystemFrame : 128 -> 160
~ ___simpleFlaggingPolicy_block_invoke : 56 -> 68
~ __ZNSt3__112__hash_tableINS_17__hash_value_typeIl13hashed_addr_tEENS_22__unordered_map_hasherIlS3_NS_4hashIlEENS_8equal_toIlEELb1EEENS_21__unordered_map_equalIlS3_S8_S6_Lb1EEENS_9allocatorIS3_EEE25__emplace_unique_key_argsIlJRKNS_21piecewise_construct_tENS_5tupleIJRKlEEENSJ_IJEEEEEENS_4pairINS_15__hash_iteratorIPNS_11__hash_nodeIS3_PvEEEEbEERKT_DpOT0_ : 560 -> 576
~ _custom_xpc_connection_send_message_with_reply_sync : 228 -> 248
~ __replacement_NSCondition_wait : 372 -> 396
~ __replacement_NSCondition_waitUntilDate : 400 -> 416
~ _initializeNSConditionSwizzling : 240 -> 256
~ __Z22initializePrimitiveMapv : 52 -> 64
~ ____Z22initializePrimitiveMapv_block_invoke : 112 -> 168
~ _createPrimitiveEntry : 180 -> 224
~ _findPrimitiveInfoNoAssert : 164 -> 184
~ _qosWaiterSignallerInvariantCheck : 2296 -> 2436
~ __ZNSt3__112__hash_tableINS_17__hash_value_typeIl10qos_info_tEENS_22__unordered_map_hasherIlS3_NS_4hashIlEENS_8equal_toIlEELb1EEENS_21__unordered_map_equalIlS3_S8_S6_Lb1EEENS_9allocatorIS3_EEE25__emplace_unique_key_argsIlJRKNS_21piecewise_construct_tENS_5tupleIJRKlEEENSJ_IJEEEEEENS_4pairINS_15__hash_iteratorIPNS_11__hash_nodeIS3_PvEEEEbEERKT_DpOT0_ : 564 -> 580
~ _checkAndGenerateBT : 368 -> 372
~ ___generateCulledBacktrace_block_invoke : 212 -> 280
~ _checkUnconditionally : 284 -> 288
~ qosWaiterSignallerInvariantCheck.cold.1 : 44 -> 52
+ generateCulledBacktrace.cold.1
CStrings:
+ "Exception generated in qosWaiterSignallerInvariantCheck. Catching it\n"
+ "PERFC_DISABLE_XPC_CHECKS"
+ "PERFC_ENABLE_PRIORITY_INVERSION_DETECTION_MAIN_THREAD_ONLY"
+ "PERFC_XPC_WAIT_THRESHOLD"
+ "TPC issue queue"
+ "XCTestCore"
- "RPAC issue generation workloop"

```
