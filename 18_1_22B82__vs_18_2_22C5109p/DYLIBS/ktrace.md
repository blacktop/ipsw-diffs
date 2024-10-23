## ktrace

> `/System/Library/PrivateFrameworks/ktrace.framework/ktrace`

```diff

-629.40.2.0.0
-  __TEXT.__text: 0xbb990
-  __TEXT.__auth_stubs: 0x30b0
+629.60.5.0.0
+  __TEXT.__text: 0xc8030
+  __TEXT.__auth_stubs: 0x32b0
   __TEXT.__objc_methlist: 0x160
-  __TEXT.__const: 0x32d1
-  __TEXT.__cstring: 0x63d6
+  __TEXT.__const: 0x3d81
+  __TEXT.__cstring: 0x6986
   __TEXT.__oslogstring: 0x5215
   __TEXT.__gcc_except_tab: 0x10d0
-  __TEXT.__swift5_typeref: 0x1042
-  __TEXT.__swift5_reflstr: 0x22b1
-  __TEXT.__swift5_assocty: 0x230
-  __TEXT.__constg_swiftt: 0x101c
-  __TEXT.__swift5_fieldmd: 0x2610
-  __TEXT.__swift5_proto: 0x2ac
-  __TEXT.__swift5_types: 0x1e0
-  __TEXT.__swift5_builtin: 0x208
-  __TEXT.__swift5_mpenum: 0x50
-  __TEXT.__swift5_capture: 0x308
-  __TEXT.__swift5_protos: 0x8
-  __TEXT.__unwind_info: 0x2a48
-  __TEXT.__eh_frame: 0x26f8
+  __TEXT.__swift5_typeref: 0x1390
+  __TEXT.__swift5_reflstr: 0x28b1
+  __TEXT.__swift5_assocty: 0x2a8
+  __TEXT.__constg_swiftt: 0x134c
+  __TEXT.__swift5_fieldmd: 0x2ca4
+  __TEXT.__swift5_proto: 0x358
+  __TEXT.__swift5_types: 0x21c
+  __TEXT.__swift5_builtin: 0x258
+  __TEXT.__swift5_mpenum: 0x78
+  __TEXT.__swift5_capture: 0x3b0
+  __TEXT.__swift5_protos: 0xc
+  __TEXT.__unwind_info: 0x2d38
+  __TEXT.__eh_frame: 0x28c0
   __TEXT.__objc_classname: 0x9b
-  __TEXT.__objc_methname: 0xc13
+  __TEXT.__objc_methname: 0xc46
   __TEXT.__objc_methtype: 0xfea
   __TEXT.__objc_stubs: 0x7e0
-  __DATA_CONST.__got: 0x508
+  __DATA_CONST.__got: 0x590
   __DATA_CONST.__const: 0x1bf0
-  __DATA_CONST.__objc_classlist: 0x50
+  __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x348
+  __DATA_CONST.__objc_selrefs: 0x358
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__objc_arraydata: 0x30
-  __AUTH_CONST.__auth_got: 0x1870
-  __AUTH_CONST.__auth_ptr: 0x470
-  __AUTH_CONST.__const: 0x3f70
+  __AUTH_CONST.__auth_got: 0x1970
+  __AUTH_CONST.__auth_ptr: 0x4e8
+  __AUTH_CONST.__const: 0x48d8
   __AUTH_CONST.__cfstring: 0x1280
-  __AUTH_CONST.__objc_const: 0x10a8
+  __AUTH_CONST.__objc_const: 0x12c0
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH.__objc_data: 0x190
-  __AUTH.__data: 0xe50
+  __AUTH.__data: 0x1060
   __DATA.__objc_ivar: 0x10
-  __DATA.__data: 0xb00
+  __DATA.__data: 0xc58
   __DATA.__crash_info: 0x40
-  __DATA.__bss: 0x5300
-  __DATA.__common: 0x100
+  __DATA.__bss: 0x6800
+  __DATA.__common: 0x110
   __DATA_DIRTY.__objc_data: 0x28
   __DATA_DIRTY.__data: 0x70
   __DATA_DIRTY.__bss: 0xa0

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/Frameworks/Security.framework/Security
+  - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/CoreSymbolication.framework/CoreSymbolication
   - /System/Library/PrivateFrameworks/LoggingSupport.framework/LoggingSupport
   - /System/Library/PrivateFrameworks/kperf.framework/kperf

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 3716
-  Symbols:   3492
-  CStrings:  1572
+  Functions: 3987
+  Symbols:   3511
+  CStrings:  1627
 
Symbols:
+ _AnalyticsSendEventLazy
+ _NSFileSize
+ _NSURLCreationDateKey
+ _NSURLFileSizeKey
+ _NSURLNameKey
+ _objc_autoreleaseReturnValue
+ _objc_retain_x27
+ _objc_retain_x9
+ _proc_pid_rusage
CStrings:
+ " of lost events; only the first "
+ " previous in-progress trace files using "
+ " seconds will be usable by analysis tools.\n\n"
+ "@\"NSDictionary\"8@?0"
+ "InstructionsPerSecond"
+ "TRACE_NO_ANALYTICS"
+ "_TtC6ktrace10RecordInfo"
+ "attributesOfItemAtPath:error:"
+ "collectionPriority"
+ "com.apple.trace.record.analytics"
+ "com.apple.trace.recording.v"
+ "currentSpan"
+ "endAfterDurationSeconds"
+ "endOnKdebugEvent"
+ "endOnNotification"
+ "endedAfterDurationExtraPercent"
+ "endedAfterDurationExtraSeconds"
+ "endedAtKdebugEventsSizeExtraBytes"
+ "endedAtKdebugEventsSizeExtraPercent"
+ "endedOnKdebugEvent"
+ "error"
+ "experimentalPlan"
+ "experimentalUsed"
+ "fileSize"
+ "in-process file not available during clean up"
+ "initial"
+ "initialSpan"
+ "kdebug event quota reached"
+ "kdebug-events-size"
+ "kdebugEventCount"
+ "kdebugEventsSize"
+ "kdebugEventsUntilLoss"
+ "kdebugFilterInclude"
+ "ktrace/Recording.swift"
+ "lostEvents"
+ "lostKdebugEvents"
+ "no in-process file at start of recording"
+ "note: file may contain sensitive data like file paths or hostnames"
+ "pendingExtension"
+ "phaseThroughputs"
+ "phases"
+ "postProcess"
+ "postProcessBytesAdded"
+ "postProcessChunksAdded"
+ "primaryEndReason"
+ "profilingIntervalSeconds"
+ "recording with providers: "
+ "requestedKdebugBufferSize"
+ "retrogradeEvents"
+ "secondsUntilLostKdebugEvents"
+ "setup"
+ "starting"
+ "stringFromByteCount:"
+ "teardown"
+ "total"
+ "trace-record-pending"
+ "trailingDurationSeconds"
+ "usage"
+ "waitingToStart"
- " of lost events; the file will not be usable by analysis tools.\n\n"
- " signal received"
- "note: trace files may contain sensitive user data, like file paths"
- "recording with names: "

```
