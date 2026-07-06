## hangreporter

> `/usr/libexec/hangreporter`

```diff

-  __TEXT.__text: 0x23978
-  __TEXT.__auth_stubs: 0xef0
-  __TEXT.__objc_stubs: 0x30a0
-  __TEXT.__objc_methlist: 0x1144
+  __TEXT.__text: 0x25e20
+  __TEXT.__auth_stubs: 0xf20
+  __TEXT.__objc_stubs: 0x3460
+  __TEXT.__objc_methlist: 0x136c
   __TEXT.__const: 0x2b0
-  __TEXT.__cstring: 0x4132
-  __TEXT.__oslogstring: 0x4d39
-  __TEXT.__objc_classname: 0x160
-  __TEXT.__objc_methname: 0x5751
-  __TEXT.__objc_methtype: 0x89d
-  __TEXT.__gcc_except_tab: 0xbb4
-  __TEXT.__unwind_info: 0x578
-  __DATA_CONST.__const: 0x1530
-  __DATA_CONST.__cfstring: 0x5200
-  __DATA_CONST.__objc_classlist: 0x78
+  __TEXT.__cstring: 0x42bf
+  __TEXT.__oslogstring: 0x4d4f
+  __TEXT.__objc_classname: 0x183
+  __TEXT.__objc_methname: 0x5c78
+  __TEXT.__objc_methtype: 0x8ef
+  __TEXT.__gcc_except_tab: 0xc7c
+  __TEXT.__unwind_info: 0x608
+  __DATA_CONST.__const: 0x1640
+  __DATA_CONST.__cfstring: 0x52a0
+  __DATA_CONST.__objc_classlist: 0x88
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_superrefs: 0x60
+  __DATA_CONST.__objc_superrefs: 0x70
   __DATA_CONST.__objc_intobj: 0xc0
   __DATA_CONST.__objc_doubleobj: 0x20
-  __DATA_CONST.__auth_got: 0x788
-  __DATA_CONST.__got: 0x288
+  __DATA_CONST.__auth_got: 0x7a0
+  __DATA_CONST.__got: 0x2c8
   __DATA_CONST.__auth_ptr: 0x10
-  __DATA.__objc_const: 0x2a10
-  __DATA.__objc_selrefs: 0x1178
-  __DATA.__objc_ivar: 0x28c
-  __DATA.__objc_data: 0x4b0
-  __DATA.__data: 0x750
-  __DATA.__bss: 0x208
-  __DATA.__common: 0x10
+  __DATA.__objc_const: 0x2eb8
+  __DATA.__objc_selrefs: 0x1298
+  __DATA.__objc_ivar: 0x2e0
+  __DATA.__objc_data: 0x550
+  __DATA.__data: 0x758
+  __DATA.__bss: 0x218
+  __DATA.__common: 0x18
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 684
-  Symbols:   331
-  CStrings:  2721
+  Functions: 757
+  Symbols:   334
+  CStrings:  2819
 
Sections:
~ __TEXT.__const : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_intobj : content changed
~ __DATA_CONST.__auth_ptr : content changed
Symbols:
+ _dispatch_sync
+ _os_signpost_id_generate
+ _xpc_dictionary_set_bool
CStrings:
+ "@\"HTTailspinWorkItem\""
+ "@\"NSMutableSet\""
+ "@\"NSSet\""
+ "@?"
+ "@?16@0:8"
+ "Boost hangUUID %@ - %s"
+ "Boost request for hangUUID: %@"
+ "Boost request missing hangUUID"
+ "Discovered task: %@"
+ "Failed to parse reason dictionary from tailspin at %@: %@"
+ "HTTailspinQueue"
+ "HTTailspinWorkItem"
+ "Idle-exit timer fired, calling xpc_transaction_exit_clean."
+ "Ignoring non tailspin file or leftover .tailspin: %@"
+ "Scan finish, wait conversion to complete..."
+ "ShouldMonitorCPURoleForAppExtensions"
+ "T@\"NSArray\",C,N,V_infoDictArray"
+ "T@\"NSDate\",&,N,V_startTime"
+ "T@\"NSObject<OS_os_transaction>\",&,N,V_transaction"
+ "T@\"NSSet\",C,N,V_hangUUIDs"
+ "T@\"NSString\",C,N,V_filePath"
+ "T@\"NSString\",C,N,V_tailspinFileName"
+ "T@?,C,N,V_workBlock"
+ "TB,N,V_isBoosted"
+ "TB,N,V_isPriority"
+ "TB,R,V_shouldMonitorCPURoleForAppExtensions"
+ "TQ,N,V_taskSignpostID"
+ "TaskProcessing"
+ "Td,N,V_processingDurationMs"
+ "Td,N,V_totalHangDurationMs"
+ "_accessQueue"
+ "_currentProcessingItem"
+ "_hangUUIDs"
+ "_idleExitTimeoutMsec"
+ "_idleExitTimer"
+ "_inFlightPaths"
+ "_infoDictArray"
+ "_isBoosted"
+ "_isPriority"
+ "_normalQueue"
+ "_priorityQueue"
+ "_processingDurationMs"
+ "_shouldMonitorCPURoleForAppExtensions"
+ "_startTime"
+ "_tailspinFileName"
+ "_taskSignpostID"
+ "_totalHangDurationMs"
+ "_workBlock"
+ "_workerQueue"
+ "addInFlightPath:"
+ "beginProcessingItem:"
+ "boost-task"
+ "com.apple.hangreporter.doneProcessingTailspin"
+ "com.apple.hangreporter.httailspinqueue.work-available"
+ "com.apple.hangreporter.tailspinqueue"
+ "com.apple.hangreporter.taskregistry.changed"
+ "com.apple.hangreporter.worker"
+ "com.apple.hangtracer.processAllAvailableTailspins"
+ "completeProcessingItem:"
+ "dequeueNonBlocking"
+ "enqueueNormal:"
+ "enqueuePriority:"
+ "getProcessingHangEntries"
+ "hangUUIDs"
+ "hangreporter_tailspin_processing"
+ "hangtracer.tailspin_path"
+ "hasItems"
+ "hasPriorityItems"
+ "infoDictArray"
+ "isBoosted"
+ "isPathInFlight:"
+ "isPriority"
+ "nil"
+ "not found in pending queue"
+ "postDidSaveTailspinNotification()"
+ "postDoneProcessingTailspinNotification"
+ "processingDurationMs"
+ "promoteItemWithHangUUID:"
+ "promoted/boosted"
+ "removeInFlightPath:"
+ "removeObject:"
+ "set"
+ "setHangUUIDs:"
+ "setInfoDictArray:"
+ "setIsBoosted:"
+ "setIsPriority:"
+ "setProcessingDurationMs:"
+ "setStartTime:"
+ "setTailspinFileName:"
+ "setTaskSignpostID:"
+ "setTotalHangDurationMs:"
+ "setWorkBlock:"
+ "sharedQueue"
+ "shouldMonitorCPURoleForAppExtensions"
+ "startDispatcherWithNotifyToken:"
+ "success"
+ "tailspinFile=%{public}@"
+ "tailspinFile=%{public}@ durationMs=%.1f"
+ "tailspinFileName"
+ "taskSignpostID"
+ "totalHangDurationMs"
+ "v24@0:8@?16"
+ "v24@0:8d16"
+ "workBlock"
- "Calling xpc_transaction_exit_clean() now"
- "Done..."
- "Encountered error trying to procesxs %@"
- "File=%@, Bytes=%{signpost.telemetry:number1}llu, Symbolicate=%{signpost.telemetry:string1}s enableTelemetry=YES "
- "Ignoring non tailspin file: %@"
- "NumSuccessfulReports=%{signpost.telemetry:number2}d enableTelemetry=YES "
- "Post-Processing Tailspin file: %@\n"
- "Posting com.apple.hangreporter.processing notification"
- "Sentry tailspin detected."
- "TailspinConversionInterval"
- "hangreporter_tailspin_conversion"

```
