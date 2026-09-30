## DiagnosticsKit

> `/System/Library/PrivateFrameworks/DiagnosticsKit.framework/DiagnosticsKit`

```diff

-72.100.4.0.0
-  __TEXT.__text: 0x21580
-  __TEXT.__auth_stubs: 0x5b0
-  __TEXT.__objc_methlist: 0x2f94
-  __TEXT.__const: 0xe0
-  __TEXT.__cstring: 0x1b07
-  __TEXT.__oslogstring: 0x185f
-  __TEXT.__gcc_except_tab: 0xadc
-  __TEXT.__unwind_info: 0xae8
+72.120.2.0.0
+  __TEXT.__text: 0x226d8
+  __TEXT.__auth_stubs: 0x600
+  __TEXT.__objc_methlist: 0x2fac
+  __TEXT.__const: 0xf8
+  __TEXT.__cstring: 0x1b5d
+  __TEXT.__oslogstring: 0x1b24
+  __TEXT.__gcc_except_tab: 0xb20
+  __TEXT.__unwind_info: 0xb10
   __TEXT.__objc_classname: 0x6c9
-  __TEXT.__objc_methname: 0x5b6b
+  __TEXT.__objc_methname: 0x5c4d
   __TEXT.__objc_methtype: 0x110f
-  __TEXT.__objc_stubs: 0x4680
-  __DATA_CONST.__got: 0x2d0
-  __DATA_CONST.__const: 0x658
+  __TEXT.__objc_stubs: 0x47a0
+  __DATA_CONST.__got: 0x2f0
+  __DATA_CONST.__const: 0x720
   __DATA_CONST.__objc_classlist: 0x160
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x128
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1590
+  __DATA_CONST.__objc_selrefs: 0x15d0
   __DATA_CONST.__objc_protorefs: 0x80
   __DATA_CONST.__objc_superrefs: 0x110
   __DATA_CONST.__objc_arraydata: 0x60
-  __AUTH_CONST.__auth_got: 0x2e8
+  __AUTH_CONST.__auth_got: 0x310
   __AUTH_CONST.__const: 0x420
-  __AUTH_CONST.__cfstring: 0xee0
+  __AUTH_CONST.__cfstring: 0xf00
   __AUTH_CONST.__objc_const: 0x5220
   __AUTH_CONST.__objc_intobj: 0xf0
   __AUTH_CONST.__objc_doubleobj: 0x30

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 36D16917-60A2-3A75-A6F1-C9F982532045
-  Functions: 946
-  Symbols:   3553
-  CStrings:  1697
+  UUID: 4089E7C2-40A1-32B4-BFFC-2D022F641770
+  Functions: 956
+  Symbols:   3602
+  CStrings:  1718
 
Symbols:
+ -[DKReportManager retryFailedComponentsWithReport:error:startTime:completion:]
+ -[DKReportManager waitForSystemReportProcessCleanupWithCompletion:]
+ GCC_except_table35
+ GCC_except_table38
+ GCC_except_table39
+ _OBJC_CLASS_$_NSDate
+ _OBJC_CLASS_$_RBSProcessHandle
+ _OBJC_CLASS_$_RBSProcessPredicate
+ ___67-[DKReportManager reportWithComponentPredicateManifest:completion:]_block_invoke.73
+ ___67-[DKReportManager reportWithComponentPredicateManifest:completion:]_block_invoke.76
+ ___67-[DKReportManager reportWithComponentPredicateManifest:completion:]_block_invoke_2
+ ___67-[DKReportManager waitForSystemReportProcessCleanupWithCompletion:]_block_invoke
+ ___67-[DKReportManager waitForSystemReportProcessCleanupWithCompletion:]_block_invoke.71
+ ___70-[DKReportManager sendRequests:serialRequests:failOnError:completion:]_block_invoke.90
+ ___70-[DKReportManager sendRequests:serialRequests:failOnError:completion:]_block_invoke.cold.1
+ ___70-[DKReportManager sendRequests:serialRequests:failOnError:completion:]_block_invoke.cold.2
+ ___78-[DKReportManager retryFailedComponentsWithReport:error:startTime:completion:]_block_invoke
+ ___78-[DKReportManager retryFailedComponentsWithReport:error:startTime:completion:]_block_invoke_2
+ ___block_descriptor_40_e8_32bs_e30_v24?0"DKReport"8"NSError"16ls32l8
+ ___block_descriptor_56_e8_32bs40r48r_e5_v8?0lr40l8r48l8s32l8
+ ___block_descriptor_64_e8_32s40bs48r56r_e5_v8?0lr48l8s32l8r56l8s40l8
+ ___block_descriptor_64_e8_32s40s48bs56r_e30_v24?0"DKReport"8"NSError"16ls32l8r56l8s48l8s40l8
+ ___block_descriptor_72_e8_32s40s48s56s64bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8
+ __dispatch_source_type_timer
+ _dispatch_resume
+ _dispatch_source_cancel
+ _dispatch_source_create
+ _dispatch_source_set_event_handler
+ _dispatch_source_set_timer
+ _kill
+ _objc_msgSend$date
+ _objc_msgSend$handleForPredicate:error:
+ _objc_msgSend$numberWithUnsignedInteger:
+ _objc_msgSend$pid
+ _objc_msgSend$predicateMatchingBundleIdentifier:
+ _objc_msgSend$reportByMergingReport:
+ _objc_msgSend$retryFailedComponentsWithReport:error:startTime:completion:
+ _objc_msgSend$setObject:atIndexedSubscript:
+ _objc_msgSend$timeIntervalSinceNow
+ _objc_msgSend$waitForSystemReportProcessCleanupWithCompletion:
- GCC_except_table23
- GCC_except_table27
- GCC_except_table30
- ___67-[DKReportManager reportWithComponentPredicateManifest:completion:]_block_invoke.64
- ___70-[DKReportManager sendRequests:serialRequests:failOnError:completion:]_block_invoke.81
- _objc_msgSend$arrayByAddingObjectsFromArray:
- _objc_retain_x27
CStrings:
+ "%.1fs elapsed, %.1fs remaining — not enough time to retry %lu components."
+ "%.1fs elapsed, %.1fs remaining. Waiting %.1fs before retrying %lu components..."
+ "Retrying %lu incompleted SystemReport components..."
+ "SystemReport process (pid %d) still tracked by RunningBoard. Sending SIGKILL and polling async..."
+ "SystemReport process already cleaned up by RunningBoard."
+ "SystemReport process exited before SIGKILL could be sent."
+ "SystemReport process fully cleaned up by RunningBoard."
+ "Timed out waiting for RunningBoard to clean up SystemReport process."
+ "[RID: %@] Component %@ received nil payload — kept in retry list"
+ "[RID: %@] Retryable failure for component %@: error code=%ld — kept in retry list: %@"
+ "[RIDs: %@] Finished; count: %d; Report: %@, component: %@, error: %@; request: %@"
+ "com.apple.DiagnosticsKit.processCleanupWait"
+ "com.apple.DiagnosticsService.SystemReport"
+ "date"
+ "handleForPredicate:error:"
+ "kill() returned error %d (errno %d) for SystemReport pid %d."
+ "numberWithUnsignedInteger:"
+ "pid"
+ "predicateMatchingBundleIdentifier:"
+ "retryFailedComponentsWithReport:error:startTime:completion:"
+ "setObject:atIndexedSubscript:"
+ "timeIntervalSinceNow"
+ "waitForSystemReportProcessCleanupWithCompletion:"
- "Retrying %lu incompleted SystemReport components in serial order..."
- "[RID: %@] Finished; count: %d; Report: %@, error: %@; request: %@"
- "arrayByAddingObjectsFromArray:"

```
