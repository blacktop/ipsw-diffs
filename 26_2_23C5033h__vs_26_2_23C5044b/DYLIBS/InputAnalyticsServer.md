## InputAnalyticsServer

> `/System/Library/PrivateFrameworks/InputAnalyticsServer.framework/InputAnalyticsServer`

```diff

-111.3.101.0.0
-  __TEXT.__text: 0x55528
-  __TEXT.__auth_stubs: 0xec0
-  __TEXT.__objc_methlist: 0x4634
+111.3.103.0.0
+  __TEXT.__text: 0x56a24
+  __TEXT.__auth_stubs: 0xed0
+  __TEXT.__objc_methlist: 0x47ac
   __TEXT.__const: 0x440
-  __TEXT.__cstring: 0x4199
-  __TEXT.__oslogstring: 0x5a43
-  __TEXT.__gcc_except_tab: 0x98c
+  __TEXT.__cstring: 0x42d9
+  __TEXT.__oslogstring: 0x5ab3
+  __TEXT.__gcc_except_tab: 0xb38
   __TEXT.__swift5_typeref: 0x10d
   __TEXT.__swift5_capture: 0x98
   __TEXT.__constg_swiftt: 0x4c

   __TEXT.__swift5_types: 0x8
   __TEXT.__swift_as_entry: 0x1c
   __TEXT.__swift_as_ret: 0x1c
-  __TEXT.__unwind_info: 0x1028
+  __TEXT.__unwind_info: 0x10b8
   __TEXT.__eh_frame: 0x310
-  __TEXT.__objc_classname: 0xa82
-  __TEXT.__objc_methname: 0xa066
-  __TEXT.__objc_methtype: 0xe5a
-  __TEXT.__objc_stubs: 0x8080
+  __TEXT.__objc_classname: 0xab7
+  __TEXT.__objc_methname: 0xa3e4
+  __TEXT.__objc_methtype: 0xeac
+  __TEXT.__objc_stubs: 0x8320
   __DATA_CONST.__got: 0x1028
-  __DATA_CONST.__const: 0x1070
-  __DATA_CONST.__objc_classlist: 0x2d8
-  __DATA_CONST.__objc_protolist: 0x38
+  __DATA_CONST.__const: 0x10b8
+  __DATA_CONST.__objc_classlist: 0x2e0
+  __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2320
+  __DATA_CONST.__objc_selrefs: 0x23e8
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x1c0
+  __DATA_CONST.__objc_superrefs: 0x1c8
   __DATA_CONST.__objc_arraydata: 0x1b8
-  __AUTH_CONST.__auth_got: 0x770
-  __AUTH_CONST.__const: 0xf18
-  __AUTH_CONST.__cfstring: 0x4a40
-  __AUTH_CONST.__objc_const: 0x7a48
+  __AUTH_CONST.__auth_got: 0x778
+  __AUTH_CONST.__const: 0xf38
+  __AUTH_CONST.__cfstring: 0x4b00
+  __AUTH_CONST.__objc_const: 0x7cc0
   __AUTH_CONST.__objc_intobj: 0xe40
   __AUTH_CONST.__objc_arrayobj: 0x1b0
-  __AUTH.__objc_data: 0xce8
+  __AUTH.__objc_data: 0xd38
   __AUTH.__data: 0x28
-  __DATA.__objc_ivar: 0x548
-  __DATA.__data: 0x430
+  __DATA.__objc_ivar: 0x564
+  __DATA.__data: 0x490
   __DATA.__bss: 0x208
   __DATA_DIRTY.__objc_data: 0xfc8
   __DATA_DIRTY.__data: 0x28

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: A7A51022-7C89-30A7-BD4A-86D007FB97BE
-  Functions: 1936
-  Symbols:   673
-  CStrings:  3590
+  UUID: 8B72DB73-8663-3359-A3DB-1435BFEDDEF5
+  Functions: 1969
+  Symbols:   674
+  CStrings:  3647
 
Symbols:
+ _objc_copyWeak
CStrings:
+ "@\"<IASAnalyticsServerDelegateProtocol>\""
+ "@\"<IASAnalyticsTestingDelegateProtocol>\""
+ "@\"IASPriorityQueue\""
+ "Did not find session manager class %@ to restart."
+ "ERROR: Tried to schedule a new timer when one already exists."
+ "IASAnalyticsServer.m"
+ "IASAnalyticsServerDelegateProtocol"
+ "IASPriorityQueue"
+ "Processing action %{private}@ from buffer"
+ "Running buffer processing loop with finalFlush: %{private}d"
+ "T@\"<IASAnalyticsServerDelegateProtocol>\",W,N,V_serverDelegate"
+ "T@\"<IASAnalyticsTestingDelegateProtocol>\",W,N,V_testingDelegate"
+ "T@\"IASPriorityQueue\",&,N,V_signalBuffer"
+ "T@\"NSDate\",C,N,V_lastConsumedSignalTimestamp"
+ "T@\"NSMutableArray\",&,N,V_storage"
+ "T@\"NSObject<OS_dispatch_source>\",&,N,V_bufferTimer"
+ "T@?,C,N,V_comparator"
+ "TB,N,V_didReceiveSafariSignal"
+ "Td,N,V_signalProcessingInterval"
+ "To use createTimerWithDelay, queue must be set on the session manager"
+ "_bufferTimer"
+ "_comparator"
+ "_didReceiveSafariSignal"
+ "_lastConsumedSignalTimestamp"
+ "_signalBuffer"
+ "_signalProcessingInterval"
+ "_storage"
+ "_testingDelegate"
+ "bufferAction:"
+ "bufferTimer"
+ "com.apple.inputAnalytics.server.IASCandidateBarAnalyzer"
+ "com.apple.inputAnalytics.server.IASSafariAnalyzer"
+ "com.apple.mobilesafari"
+ "comparator"
+ "didReceiveSafariSignal"
+ "exchangeObjectAtIndex:withObjectAtIndex:"
+ "handleSessionManagerException:forSessionManager:"
+ "handleSessionManagerException:forSessionManagerClass:"
+ "initWithComparator:"
+ "initWithEventHandler:testingDelegate:isInternalBuild:"
+ "initWithQueue:serverDelegate:testingDelegate:eventHandler:"
+ "lastConsumedSignalTimestamp"
+ "peek"
+ "pop"
+ "processBufferWithFinalFlush:"
+ "push:"
+ "q24@?0@\"IAXPCObject\"8@\"IAXPCObject\"16"
+ "removeLastObject"
+ "scheduleSignalProcessing"
+ "setBufferTimer:"
+ "setComparator:"
+ "setDidReceiveSafariSignal:"
+ "setLastConsumedSignalTimestamp:"
+ "setSignalBuffer:"
+ "setSignalProcessingInterval:"
+ "setStorage:"
+ "setTestingDelegate:"
+ "siftDownFromIndex:"
+ "siftUpFromIndex:"
+ "signalBuffer"
+ "signalProcessingInterval"
+ "storage"
+ "testingDelegate"
+ "v32@0:8@\"NSException\"16@\"IASSessionManager\"24"
- "@\"<IASServerAnalyticsDelegate>\""
- "@\"IAXPCObject\""
- "@40@0:8@16@24@?32"
- "T@\"<IASServerAnalyticsDelegate>\",W,N,V_serverDelegate"
- "T@\"IAXPCObject\",&,N,V_lastConsumedAsyncSignal"
- "_lastConsumedAsyncSignal"
- "com.apple.inputanalytics.server.IASCandidateBarAnalyzer"
- "com.apple.inputanalytics.server.IASSafariAnalyzer"
- "creationTimestamp"
- "initWithEventHandler:serverDelegate:isInternalBuild:"
- "initWithQueue:serverDelegate:eventHandler:"
- "lastConsumedAsyncSignal"
- "setLastConsumedAsyncSignal:"

```
