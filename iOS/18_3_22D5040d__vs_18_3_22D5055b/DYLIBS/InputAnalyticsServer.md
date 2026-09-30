## InputAnalyticsServer

> `/System/Library/PrivateFrameworks/InputAnalyticsServer.framework/InputAnalyticsServer`

```diff

-64.223.0.0.0
-  __TEXT.__text: 0x2b544
-  __TEXT.__auth_stubs: 0xa70
-  __TEXT.__objc_methlist: 0x20e4
-  __TEXT.__const: 0x1b0
-  __TEXT.__cstring: 0x2439
-  __TEXT.__oslogstring: 0x36c6
+64.224.100.0.0
+  __TEXT.__text: 0x2c12c
+  __TEXT.__auth_stubs: 0xad0
+  __TEXT.__objc_methlist: 0x219c
+  __TEXT.__const: 0x1c0
+  __TEXT.__cstring: 0x2449
+  __TEXT.__oslogstring: 0x3896
   __TEXT.__gcc_except_tab: 0x2a8
   __TEXT.__swift5_typeref: 0xa7
   __TEXT.__swift5_capture: 0x88
   __TEXT.__constg_swiftt: 0x4c
   __TEXT.__swift5_builtin: 0x28
   __TEXT.__swift5_types: 0x8
-  __TEXT.__unwind_info: 0x858
+  __TEXT.__unwind_info: 0x878
   __TEXT.__eh_frame: 0x2e8
-  __TEXT.__objc_classname: 0x498
-  __TEXT.__objc_methname: 0x568c
-  __TEXT.__objc_methtype: 0x747
-  __TEXT.__objc_stubs: 0x4300
-  __DATA_CONST.__got: 0x9e0
-  __DATA_CONST.__const: 0x960
+  __TEXT.__objc_classname: 0x49c
+  __TEXT.__objc_methname: 0x5973
+  __TEXT.__objc_methtype: 0x81a
+  __TEXT.__objc_stubs: 0x44c0
+  __DATA_CONST.__got: 0x9f0
+  __DATA_CONST.__const: 0x968
   __DATA_CONST.__objc_classlist: 0x148
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1280
+  __DATA_CONST.__objc_selrefs: 0x12f0
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0xe0
   __DATA_CONST.__objc_arraydata: 0x68
-  __AUTH_CONST.__auth_got: 0x548
+  __AUTH_CONST.__auth_got: 0x578
   __AUTH_CONST.__auth_ptr: 0x90
   __AUTH_CONST.__const: 0x7a8
-  __AUTH_CONST.__cfstring: 0x2500
-  __AUTH_CONST.__objc_const: 0x4388
+  __AUTH_CONST.__cfstring: 0x2580
+  __AUTH_CONST.__objc_const: 0x44f8
   __AUTH_CONST.__objc_intobj: 0x570
   __AUTH_CONST.__objc_arrayobj: 0x90
   __AUTH.__objc_data: 0x590
   __AUTH.__data: 0x50
-  __DATA.__objc_ivar: 0x2f0
+  __DATA.__objc_ivar: 0x308
   __DATA.__data: 0x350
   __DATA.__bss: 0x120
   __DATA_DIRTY.__objc_data: 0x780

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 996
-  Symbols:   436
-  CStrings:  1667
+  Functions: 1019
+  Symbols:   444
+  CStrings:  1713
 
Symbols:
+ _IAPayloadKeyGenmojiCreationBundleID
+ _IAPayloadKeyGenmojiCreationQueryUUID
+ _IASignalGenmojiCreationBeginGeneration
+ _IASignalGenmojiCreationMessagesSendMenuButtonPressed
+ __dispatch_source_type_timer
+ _dispatch_resume
+ _dispatch_source_cancel
+ _dispatch_source_create
+ _dispatch_source_set_event_handler
+ _dispatch_source_set_timer
+ _dispatch_time
- _IAPayloadValueGenmojiCreationFailReasonPolicyViolationNonPersonalizedGeneratedImageCaptionPolicy
- _IASignalGenmojiCreationPhotoPicked
- _IASignalGenmojiCreationPillSelected
CStrings:
+ "\x01\x11"
+ "\x02\x12"
+ "\x06"
+ "\x11\x12\x11\x11\x13A1"
+ "!\x13"
+ "%@,%@,%@,%@,%@,%lu"
+ "@\"NSObject<OS_dispatch_queue>\"16@0:8"
+ "@\"NSObject<OS_dispatch_source>\""
+ "@32@0:8d16@?24"
+ "@40@0:8@\"NSUUID\"16@\"IASSessionManager\"24@\"NSObject<OS_dispatch_queue>\"32"
+ "@40@0:8@16@24@32"
+ "@48@0:8@\"NSUUID\"16@\"IASSessionManager\"24@\"NSObject<OS_dispatch_queue>\"32@?<v@?@\"NSDictionary\">40"
+ "@48@0:8@16@24@32@?40"
+ "A"
+ "Active session in state %@ interrupted"
+ "BeginGeneration"
+ "Bundle ID changed unexpectedly"
+ "Creating analyzer on %{private}@"
+ "IASAnalyzer.m"
+ "PendingTermination"
+ "Stray session without an entry point"
+ "T@\"NSDate\",&,N,V_creationSheetEntryTime"
+ "T@\"NSObject<OS_dispatch_queue>\",&,N"
+ "T@\"NSObject<OS_dispatch_queue>\",&,N,Vqueue"
+ "T@\"NSObject<OS_dispatch_queue>\",R,N,V_queue"
+ "T@\"NSObject<OS_dispatch_source>\",&,N,V_pendingTerminationTimer"
+ "T@\"NSString\",C,N,V_queryUUIDString"
+ "Td,N,V_pendingTerminationTimerDuration"
+ "To use createTimerWithDelay, queue must be set on the analyzer"
+ "[%{private}@] Cached bundle ID %{private}@"
+ "[%{private}@] Clearing grace period. Time since bringup %f"
+ "[%{private}@] Deep reset on start of new panel session"
+ "[%{private}@] Enumerating and invalidating timer"
+ "[%{private}@] Ignored %{private}@"
+ "[%{private}@] Ignoring signal due to grace period. Time since bringup %f"
+ "[%{private}@] Initial image personalization type after %{private}@ %lu"
+ "[%{private}@] Noted creation sheet entry point timestamp %{private}@"
+ "[%{private}@] PendingTermination - Publishing and resetting on %@"
+ "[%{private}@] PendingTermination timer expired"
+ "[%{private}@] Publishing previous session and starting new one on BeginGeneration, from state %{private}@ with signal %{private}@"
+ "[%{private}@] Reset"
+ "[%{private}@] Stopping timers before publish on %{private}@ in %{private}@"
+ "[%{private}@] Waiting for opportunity to still receive ImageInserted"
+ "[%{private}@] handleBeginGenerationSignal: Incremented numPrompts due to BeginGeneration"
+ "_creationSheetEntryTime"
+ "_pendingTerminationTimer"
+ "_pendingTerminationTimerDuration"
+ "_queryUUIDString"
+ "createTimerWithDelay:handler:"
+ "creationSheetEntryTime"
+ "deepReset"
+ "handleBeginGenerationSignal:"
+ "initWithAnalyzerSessionId:sessionManagerDelegate:queue:"
+ "initWithAnalyzerSessionId:sessionManagerDelegate:queue:eventHandler:"
+ "initWithQueue:"
+ "initWithQueue:serverDelegate:eventHandler:"
+ "isSessionStartSignal:"
+ "pendingTerminationTimer"
+ "pendingTerminationTimerDuration"
+ "pendingTerminationTimerExpired"
+ "queryUUIDString"
+ "resetPendingTerminationTimer"
+ "setCreationSheetEntryTime:"
+ "setPendingTerminationTimer:"
+ "setPendingTerminationTimerDuration:"
+ "setQueryUUIDString:"
+ "v24@0:8@\"NSObject<OS_dispatch_queue>\"16"
- "\x02\x11"
- "\x05"
- "\x11\x11\x11\x11\x13A1"
- "@32@0:8@\"NSUUID\"16@\"IASSessionManager\"24"
- "@32@0:8@?16@24"
- "@40@0:8@\"NSUUID\"16@\"IASSessionManager\"24@?<v@?@\"NSDictionary\">32"
- "Creating analyzer on PersonIdentificationStarted"
- "Generation times not well-defined due to restart occurring in a subsequent image generation"
- "Inconsistent prompt"
- "Initial generation time not well-defined due to restart occurring in a subsequent image"
- "N"
- "PendingForcedPersonalization"
- "[%{private}@] In AmbiguousPersonFound for %f. Low confidence"
- "[%{private}@] Incremented numPrompts due to NonPersonalizedGeneratedImageCaptionPolicy"
- "[%{private}@] Publishing previous session and starting new one on PersonIdentificationStarted, from state %{private}@ with signal %{private}@"
- "[%{private}@] verifyConsistencyOfPromptAndCacheIfNecessary: Incremented numPrompts due to mismatch in state %{private}@ (%{sensitive}@ -> %{sensitive}@) on signal %{privnate}@"
- "initWithAnalyzerSessionId:sessionManagerDelegate:"
- "initWithAnalyzerSessionId:sessionManagerDelegate:eventHandler:"
- "initWithEventHandler:serverDelegate:"
- "verifyConsistencyOfPromptAndCacheIfNecessary:"

```
