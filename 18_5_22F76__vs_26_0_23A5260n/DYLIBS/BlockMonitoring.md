## BlockMonitoring

> `/System/Library/PrivateFrameworks/BlockMonitoring.framework/BlockMonitoring`

```diff

-385.14.0.0.0
-  __TEXT.__text: 0x3a74
-  __TEXT.__auth_stubs: 0x750
-  __TEXT.__objc_methlist: 0x230
+410.0.0.0.0
+  __TEXT.__text: 0x4b9c
+  __TEXT.__auth_stubs: 0x850
+  __TEXT.__objc_methlist: 0x1e8
   __TEXT.__const: 0xc8
-  __TEXT.__gcc_except_tab: 0xe8
-  __TEXT.__cstring: 0x511
-  __TEXT.__oslogstring: 0x659
+  __TEXT.__gcc_except_tab: 0x190
+  __TEXT.__cstring: 0x566
+  __TEXT.__oslogstring: 0xf37
   __TEXT.__dlopen_cstrs: 0x5a
-  __TEXT.__unwind_info: 0x158
-  __TEXT.__objc_classname: 0x21
-  __TEXT.__objc_methname: 0x85f
-  __TEXT.__objc_methtype: 0x185
-  __TEXT.__objc_stubs: 0x6c0
+  __TEXT.__unwind_info: 0x148
+  __TEXT.__objc_classname: 0x22
+  __TEXT.__objc_methname: 0x87f
+  __TEXT.__objc_methtype: 0x158
+  __TEXT.__objc_stubs: 0x5a0
   __DATA_CONST.__got: 0xb0
-  __DATA_CONST.__const: 0x168
+  __DATA_CONST.__const: 0x190
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x288
+  __DATA_CONST.__objc_selrefs: 0x258
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x3b8
+  __AUTH_CONST.__auth_got: 0x438
   __AUTH_CONST.__const: 0x40
-  __AUTH_CONST.__cfstring: 0x340
-  __AUTH_CONST.__objc_const: 0x398
-  __DATA.__objc_ivar: 0x60
+  __AUTH_CONST.__cfstring: 0x380
+  __AUTH_CONST.__objc_const: 0x438
+  __DATA.__objc_ivar: 0x74
   __DATA.__bss: 0x10
   __DATA_DIRTY.__objc_data: 0x50
   __DATA_DIRTY.__data: 0x8

   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Security.framework/Security
+  - /System/Library/PrivateFrameworks/LoggingSupport.framework/LoggingSupport
   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: D5141E9D-C909-3DBB-968F-77290109FE98
-  Functions: 90
-  Symbols:   446
-  CStrings:  245
+  UUID: 64FAAB79-AEFB-356B-AA13-E95636BD870C
+  Functions: 114
+  Symbols:   502
+  CStrings:  286
 
Symbols:
+ -[BMBlockMonitoring executeBlockWithSignature:timeout:options:diagnosticCollectionBlock:block:]
+ -[BMBlockMonitoring executeBlockWithSignature:timeout:options:diagnosticCollectionBlock:block:].cold.1
+ -[BMBlockMonitoring executeBlockWithSignature:timeout:options:diagnosticCollectionBlock:block:].cold.2
+ -[BMBlockMonitoring logFault:thread_id:reason:]
+ -[BMBlockMonitoring logPanicDeny:thread_id:reason:demoted:]
+ -[BMBlockMonitoring lookForDeviceReadiness].cold.3
+ -[BMBlockMonitoring takeActionIfRelevant:thread_id:timeout:options:recovered:diagnosticCollectionBlock:]
+ -[BMBlockMonitoring(Testing) _test_setActionDoneCallback:]
+ -[BMBlockMonitoring(Testing) _test_setLogFlushSleep:]
+ -[BMBlockMonitoring(Testing) _test_setPostPersistenceSleep:]
+ GCC_except_table14
+ GCC_except_table23
+ GCC_except_table7
+ _BMMonitorBlockExecutionWithExtraDiagnostics
+ _OBJC_IVAR_$_BMBlockMonitoring._bootArgsBMFlags
+ _OBJC_IVAR_$_BMBlockMonitoring._bootArgsDebugFlags
+ _OBJC_IVAR_$_BMBlockMonitoring._entitledToFlushOSLogs
+ _OBJC_IVAR_$_BMBlockMonitoring._test_actionDoneCallback
+ _OBJC_IVAR_$_BMBlockMonitoring._test_logFlushSleep
+ _OBJC_IVAR_$_BMBlockMonitoring._test_postPersistenceSleep
+ _OSLogFlushBuffers
+ _OUTLINED_FUNCTION_10
+ _OUTLINED_FUNCTION_11
+ _OUTLINED_FUNCTION_12
+ _OUTLINED_FUNCTION_13
+ _OUTLINED_FUNCTION_14
+ _OUTLINED_FUNCTION_15
+ _OUTLINED_FUNCTION_16
+ _OUTLINED_FUNCTION_17
+ _OUTLINED_FUNCTION_18
+ _OUTLINED_FUNCTION_19
+ _OUTLINED_FUNCTION_20
+ _OUTLINED_FUNCTION_21
+ _OUTLINED_FUNCTION_22
+ _OUTLINED_FUNCTION_23
+ _OUTLINED_FUNCTION_24
+ _OUTLINED_FUNCTION_25
+ _OUTLINED_FUNCTION_26
+ _OUTLINED_FUNCTION_6
+ _OUTLINED_FUNCTION_7
+ _OUTLINED_FUNCTION_8
+ _OUTLINED_FUNCTION_9
+ ___104-[BMBlockMonitoring takeActionIfRelevant:thread_id:timeout:options:recovered:diagnosticCollectionBlock:]_block_invoke
+ ___43-[BMBlockMonitoring lookForDeviceReadiness]_block_invoke.54
+ ___43-[BMBlockMonitoring lookForDeviceReadiness]_block_invoke.56
+ ___43-[BMBlockMonitoring lookForDeviceReadiness]_block_invoke.56.cold.1
+ ___45-[BMBlockMonitoring initForTesting:bootArgs:]_block_invoke.46
+ ___45-[BMBlockMonitoring initForTesting:bootArgs:]_block_invoke.46.cold.1
+ ___45-[BMBlockMonitoring initForTesting:bootArgs:]_block_invoke.46.cold.2
+ ___45-[BMBlockMonitoring initForTesting:bootArgs:]_block_invoke.46.cold.3
+ ___45-[BMBlockMonitoring initForTesting:bootArgs:]_block_invoke.47
+ ___95-[BMBlockMonitoring executeBlockWithSignature:timeout:options:diagnosticCollectionBlock:block:]_block_invoke
+ ___95-[BMBlockMonitoring executeBlockWithSignature:timeout:options:diagnosticCollectionBlock:block:]_block_invoke_2
+ ___block_descriptor_68_e8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
+ ___block_descriptor_84_e8_32s40bs_e5_v8?0ls32l8s40l8
+ __os_log_debug_impl
+ _dispatch_queue_attr_make_with_autorelease_frequency
+ _dispatch_queue_attr_make_with_overcommit
+ _dispatch_semaphore_create
+ _dispatch_semaphore_signal
+ _dispatch_semaphore_wait
+ _objc_begin_catch
+ _objc_end_catch
+ _objc_exception_rethrow
+ _objc_msgSend$executeBlockWithSignature:timeout:options:diagnosticCollectionBlock:block:
+ _objc_release_x28
+ _objc_retainBlock
+ _objc_retain_x22
+ _objc_retain_x25
+ _objc_retain_x27
+ _objc_retain_x4
+ _objc_terminate
+ _sync
- -[BMBlockMonitoring executeBlockWithSignature:timeout:options:block:].cold.1
- -[BMBlockMonitoring executeBlockWithSignature:timeout:options:block:].cold.2
- -[BMBlockMonitoring logFault:reason:]
- -[BMBlockMonitoring logFault:reason:].cold.1
- -[BMBlockMonitoring logFault:reason:].cold.2
- -[BMBlockMonitoring logPanicDeny:reason:demoted:]
- -[BMBlockMonitoring logPanicDeny:reason:demoted:].cold.1
- -[BMBlockMonitoring takeActionIfRelevant:thread_id:timeout:options:recovered:]
- -[BMBlockMonitoring takeActionIfRelevant:thread_id:timeout:options:recovered:].cold.1
- -[BMBlockMonitoring takeActionIfRelevant:thread_id:timeout:options:recovered:].cold.2
- -[BMBlockMonitoring takeActionIfRelevant:thread_id:timeout:options:recovered:].cold.3
- -[BMBlockMonitoring takeActionIfRelevant:thread_id:timeout:options:recovered:].cold.4
- -[BMBlockMonitoring takeActionIfRelevant:thread_id:timeout:options:recovered:].cold.5
- -[BMBlockMonitoring takeActionIfRelevant:thread_id:timeout:options:recovered:].cold.6
- -[BMBlockMonitoring takeActionIfRelevant:thread_id:timeout:options:recovered:].cold.7
- GCC_except_table12
- GCC_except_table68
- GCC_except_table9
- _OBJC_IVAR_$_BMBlockMonitoring._bootDebugFlags
- ___43-[BMBlockMonitoring lookForDeviceReadiness]_block_invoke.50
- ___43-[BMBlockMonitoring lookForDeviceReadiness]_block_invoke.52
- ___43-[BMBlockMonitoring lookForDeviceReadiness]_block_invoke.52.cold.1
- ___45-[BMBlockMonitoring initForTesting:bootArgs:]_block_invoke.43
- ___69-[BMBlockMonitoring executeBlockWithSignature:timeout:options:block:]_block_invoke
- ___69-[BMBlockMonitoring executeBlockWithSignature:timeout:options:block:]_block_invoke_2
- ___block_descriptor_76_e8_32s_e5_v8?0ls32l8
- _objc_msgSend$alertPath
- _objc_msgSend$cleanup
- _objc_msgSend$initForTesting:bootArgs:
- _objc_msgSend$logFault:reason:
- _objc_msgSend$logPanicDeny:reason:demoted:
- _objc_msgSend$lookForDeviceReadiness
- _objc_msgSend$parseBootArgInt:where:
- _objc_msgSend$showBootArgsAlertWithCheckingFirst:
- _objc_msgSend$signaturePath
- _objc_msgSend$takeActionIfRelevant:thread_id:timeout:options:recovered:
- _objc_retain_x23
- _objc_retain_x28
CStrings:
+ "%@ (%u:%llu) calling diagnostic collection block"
+ "%@ (%u:%llu) calling diagnostic collection block for fault"
+ "%@ (%u:%llu) client requested no log flushing"
+ "%@ (%u:%llu) flushed logs"
+ "%@ (%u:%llu) flushing logs"
+ "%@ (%u:%llu) not entitled, cannot flush logs"
+ "%@ (%u:%llu) recovered after timer fired but before timer handler ran (fault) - ignoring via boot-arg"
+ "%@ (%u:%llu) recovered after timer fired but before timer handler ran - ignoring via boot-arg"
+ "%@ (%u:%llu) recovered after timer fired but before timer handler ran - skipping panic"
+ "%@ (%u:%llu) recovered during diagnostic gathering (fault) - ignoring via boot-arg"
+ "%@ (%u:%llu) recovered during diagnostic gathering - ignoring via boot-arg"
+ "%@ (%u:%llu) recovered during diagnostic gathering - skipping fault"
+ "%@ (%u:%llu) recovered during diagnostic gathering - skipping panic"
+ "%@ (%u:%llu) recovered during log flush - ignoring via boot-arg"
+ "%@ (%u:%llu) recovered during log flush - skipping panic"
+ "%@ (%u:%llu) recovered while persisting state - ignoring via boot-arg"
+ "%@ (%u:%llu) recovered while persisting state - skipping panic"
+ "%@ (%u:%llu) sleeping after persistence for recovery testing for %us"
+ "%@ (%u:%llu) sleeping for log flush recovery testing for %us"
+ "%@ (%u:%llu) timed out waiting for log flushing"
+ "%@ (%u:%llu) would trigger a panic - boot-arg prevents panic, so faulting instead"
+ "%@ cannot panic, last panic was within 24 hours at: %@"
+ "%@ has already panic on %@ - ignoring via boot-arg"
+ "%@ persisting or flushing failed: %{errno}d - ignoring via boot-arg"
+ "%@ serialization failed: %@ - ignoring via boot-arg"
+ "???"
+ "@?"
+ "Allowing BlockMonitoring in any process via boot-arg"
+ "Allowing customer machine via boot-arg"
+ "Allowing panics without core dumps via boot-arg"
+ "Allowing reporting process being debugged via boot-arg"
+ "Allowing virtual device via boot-arg"
+ "Container not found: %@ - ignoring via boot-arg"
+ "Detected boot-arg flags 0x%llx"
+ "Disabling feature - BlockMonitoring disabled via boot-arg"
+ "Disabling feature - customer machine"
+ "Entitled for log flushing"
+ "Failed allocating IO buffer: %{errno}d - ignoring via boot-arg"
+ "Failed gathering entitlement for flushing logs: %@"
+ "Failed opening %@: %{errno}d - ignoring via boot-arg"
+ "Ignoring failure to gather os version: %{errno}d - ignoring via boot-arg"
+ "Ignoring watchdog disablement via boot-arg"
+ "Not entitled for log flushing: %@"
+ "Process is properly entitled for panic with data"
+ "_bootArgsBMFlags"
+ "_bootArgsDebugFlags"
+ "_entitledToFlushOSLogs"
+ "_test_actionDoneCallback"
+ "_test_logFlushSleep"
+ "_test_postPersistenceSleep"
+ "_test_setActionDoneCallback:"
+ "_test_setLogFlushSleep:"
+ "_test_setPostPersistenceSleep:"
+ "com.apple.BlockMonitoring.FlushLogsQueue"
+ "com.apple.private.logging.flush-buffers"
+ "executeBlockWithSignature:timeout:options:diagnosticCollectionBlock:block:"
+ "last panic was within 24 hours at: %@ - ignoring via boot-arg"
+ "v24@0:8@?16"
+ "v52@0:8r*16Q24i32@?36@?44"
- "%@ (%u:%llu) recovered - skipping panic"
- "%@ cannot panic, last panic was at: %@"
- "@28@0:8B16@20"
- "B32@0:8@16^q24"
- "Disabling feature - BlockMonitoring disabled: %llx"
- "Process is properly entitled"
- "_bootDebugFlags"
- "alertPath"
- "cleanup"
- "initForTesting:bootArgs:"
- "logFault:reason:"
- "logPanicDeny:reason:demoted:"
- "lookForDeviceReadiness"
- "parseBootArgInt:where:"
- "showBootArgsAlertWithCheckingFirst:"
- "signaturePath"
- "takeActionIfRelevant:thread_id:timeout:options:recovered:"
- "v32@0:8@16C24B28"
- "v32@0:8@16r*24"
- "v52@0:8@16Q24Q32i40^AB44"

```
