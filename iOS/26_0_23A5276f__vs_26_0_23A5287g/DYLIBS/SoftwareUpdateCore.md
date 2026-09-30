## SoftwareUpdateCore

> `/System/Library/PrivateFrameworks/SoftwareUpdateCore.framework/SoftwareUpdateCore`

```diff

-2422.0.31.502.1
-  __TEXT.__text: 0xa41b4
+2422.0.56.0.2
+  __TEXT.__text: 0xa497c
   __TEXT.__auth_stubs: 0x910
-  __TEXT.__objc_methlist: 0x7974
-  __TEXT.__const: 0x130
-  __TEXT.__cstring: 0x150de
-  __TEXT.__oslogstring: 0xc4a1
+  __TEXT.__objc_methlist: 0x79bc
+  __TEXT.__const: 0x138
+  __TEXT.__cstring: 0x1521f
+  __TEXT.__oslogstring: 0xc548
   __TEXT.__gcc_except_tab: 0x758
   __TEXT.__dlopen_cstrs: 0x41
   __TEXT.__unwind_info: 0x1770
-  __TEXT.__objc_classname: 0x703
-  __TEXT.__objc_methname: 0x1574e
-  __TEXT.__objc_methtype: 0xfbc
-  __TEXT.__objc_stubs: 0xe860
+  __TEXT.__objc_classname: 0x71c
+  __TEXT.__objc_methname: 0x15846
+  __TEXT.__objc_methtype: 0xfcc
+  __TEXT.__objc_stubs: 0xe920
   __DATA_CONST.__got: 0x890
-  __DATA_CONST.__const: 0x22e8
-  __DATA_CONST.__objc_classlist: 0x1d8
+  __DATA_CONST.__const: 0x2308
+  __DATA_CONST.__objc_classlist: 0x1e0
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x43e8
-  __DATA_CONST.__objc_superrefs: 0x1c0
+  __DATA_CONST.__objc_selrefs: 0x4418
+  __DATA_CONST.__objc_superrefs: 0x1c8
   __DATA_CONST.__objc_arraydata: 0xe8
   __AUTH_CONST.__auth_got: 0x498
   __AUTH_CONST.__const: 0x4c0
-  __AUTH_CONST.__cfstring: 0x12a20
-  __AUTH_CONST.__objc_const: 0xa5b0
+  __AUTH_CONST.__cfstring: 0x12ac0
+  __AUTH_CONST.__objc_const: 0xa6e0
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__objc_arrayobj: 0xa8
   __AUTH_CONST.__objc_intobj: 0xa8
-  __AUTH.__objc_data: 0x5a0
-  __DATA.__objc_ivar: 0x998
+  __AUTH.__objc_data: 0x5f0
+  __DATA.__objc_ivar: 0x9a4
   __DATA.__data: 0x360
   __DATA.__bss: 0x58
   __DATA_DIRTY.__objc_data: 0xcd0

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F1689F75-C371-36D4-A38C-04F7801F4BDF
-  Functions: 3011
-  Symbols:   10175
-  CStrings:  8954
+  UUID: A28F9EA5-0826-3997-9ADE-80CE46394286
+  Functions: 3018
+  Symbols:   10206
+  CStrings:  8983
 
Symbols:
+ -[SUCoreAnalyticsEventSubmitter _queue_submitEvent:].cold.2
+ -[SUCoreDownloadCheckpoint downloadedBytes]
+ -[SUCoreDownloadCheckpoint initWithTimestamp:downloadedBytes:]
+ -[SUCoreDownloadCheckpoint timestamp]
+ -[SUCoreUpdateDownloader progressHistory]
+ -[SUCoreUpdateDownloader setProgressHistory:]
+ _OBJC_CLASS_$_SUCoreDownloadCheckpoint
+ _OBJC_IVAR_$_SUCoreDownloadCheckpoint._downloadedBytes
+ _OBJC_IVAR_$_SUCoreDownloadCheckpoint._timestamp
+ _OBJC_IVAR_$_SUCoreUpdateDownloader._progressHistory
+ _OBJC_METACLASS_$_SUCoreDownloadCheckpoint
+ __OBJC_$_INSTANCE_METHODS_SUCoreDownloadCheckpoint
+ __OBJC_$_INSTANCE_VARIABLES_SUCoreDownloadCheckpoint
+ __OBJC_$_PROP_LIST_SUCoreDownloadCheckpoint
+ __OBJC_CLASS_RO_$_SUCoreDownloadCheckpoint
+ __OBJC_METACLASS_RO_$_SUCoreDownloadCheckpoint
+ ___51-[SUCoreUpdateDownloader actionRemoveUpdate:error:]_block_invoke.554
+ ___51-[SUCoreUpdateDownloader actionRemoveUpdate:error:]_block_invoke_2.555
+ ___57-[SUCoreUpdateDownloader actionDownloadPSUSAssets:error:]_block_invoke.463
+ ___61-[SUCoreUpdateDownloader actionReportDownloadProgress:error:]_block_invoke.517
+ ___block_descriptor_40_e51_B24?0"SUCoreDownloadCheckpoint"8"NSDictionary"16l
+ _objc_msgSend$downloadedBytes
+ _objc_msgSend$filterUsingPredicate:
+ _objc_msgSend$initWithTimestamp:downloadedBytes:
+ _objc_msgSend$progressHistory
+ _objc_msgSend$setProgressHistory:
+ _objc_msgSend$timeIntervalSince1970
+ _objc_msgSend$timestamp
- ___51-[SUCoreUpdateDownloader actionRemoveUpdate:error:]_block_invoke.519
- ___51-[SUCoreUpdateDownloader actionRemoveUpdate:error:]_block_invoke_2.520
- ___57-[SUCoreUpdateDownloader actionDownloadPSUSAssets:error:]_block_invoke.449
- _objc_msgSend$estimatedTimeRemaining
CStrings:
+ "1.0.5"
+ "@32@0:8d16q24"
+ "B24@?0@\"SUCoreDownloadCheckpoint\"8@\"NSDictionary\"16"
+ "SUBMIT: failed to send event: %{public}@"
+ "SUBMIT_EVENTS_WITH_NAME: Failed to send event: %{public}@"
+ "SUCoreDownloadCheckpoint"
+ "T@\"NSMutableArray\",&,N,V_progressHistory"
+ "Td,R,N,V_timestamp"
+ "Tq,R,N,V_downloadedBytes"
+ "[CoreAnalytics]: SUBMIT_ALL_EVENT: Failed to send event: %{public}@"
+ "[PROGRESS]"
+ "[Progress] %lld/%lld bytes downloaded; estimated speed: %.2lf MBps; estimated time remaining = %.2lf secs"
+ "[Progress] Too few progress records to report"
+ "_downloadedBytes"
+ "_progressHistory"
+ "_timestamp"
+ "d"
+ "downloadedBytes"
+ "filterUsingPredicate:"
+ "initWithTimestamp:downloadedBytes:"
+ "progressHistory"
+ "setProgressHistory:"
+ "timeIntervalSince1970"
+ "unexpected written bytes (%lld) > expected bytes (%lld)"
+ "unexpected written bytes decreased (delta = %lld)"
- "1.0.4"
- "estimatedTimeRemaining"

```
