## UserNotificationsCore

> `/System/Library/PrivateFrameworks/UserNotificationsCore.framework/UserNotificationsCore`

```diff

-579.3.12.0.0
-  __TEXT.__text: 0x1a49e8
-  __TEXT.__auth_stubs: 0x31e0
+579.3.16.0.0
+  __TEXT.__text: 0x1a58b8
+  __TEXT.__auth_stubs: 0x31f0
   __TEXT.__objc_methlist: 0x62e0
-  __TEXT.__const: 0xba50
-  __TEXT.__cstring: 0xcd57
+  __TEXT.__const: 0xbbc8
+  __TEXT.__cstring: 0xcc03
   __TEXT.__gcc_except_tab: 0x6f0
-  __TEXT.__oslogstring: 0xc5e8
+  __TEXT.__oslogstring: 0xca38
   __TEXT.__dlopen_cstrs: 0xf4
-  __TEXT.__constg_swiftt: 0x5530
-  __TEXT.__swift5_typeref: 0x5010
-  __TEXT.__swift5_reflstr: 0x2ef4
-  __TEXT.__swift5_fieldmd: 0x3a0c
-  __TEXT.__swift5_builtin: 0x118
-  __TEXT.__swift5_assocty: 0x3d8
-  __TEXT.__swift5_capture: 0x1520
-  __TEXT.__swift5_protos: 0xf4
-  __TEXT.__swift5_proto: 0x964
+  __TEXT.__constg_swiftt: 0x555c
+  __TEXT.__swift5_typeref: 0x4fd6
+  __TEXT.__swift5_reflstr: 0x30ca
+  __TEXT.__swift5_fieldmd: 0x3ae4
+  __TEXT.__swift5_builtin: 0x104
+  __TEXT.__swift5_assocty: 0x3f0
+  __TEXT.__swift5_capture: 0x15b4
+  __TEXT.__swift5_protos: 0xf0
+  __TEXT.__swift5_proto: 0x984
   __TEXT.__swift5_types: 0x454
-  __TEXT.__swift5_mpenum: 0x48
-  __TEXT.__unwind_info: 0x5630
-  __TEXT.__eh_frame: 0x4eb8
+  __TEXT.__swift5_mpenum: 0x40
+  __TEXT.__unwind_info: 0x5738
+  __TEXT.__eh_frame: 0x52b0
   __TEXT.__objc_classname: 0xe30
   __TEXT.__objc_methname: 0x159b0
   __TEXT.__objc_methtype: 0x3107
   __TEXT.__objc_stubs: 0xca80
-  __DATA_CONST.__got: 0xf98
+  __DATA_CONST.__got: 0xf70
   __DATA_CONST.__const: 0x1510
-  __DATA_CONST.__objc_classlist: 0x5f0
+  __DATA_CONST.__objc_classlist: 0x5e0
   __DATA_CONST.__objc_catlist: 0x80
   __DATA_CONST.__objc_protolist: 0x2b8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x4068
   __DATA_CONST.__objc_protorefs: 0x160
   __DATA_CONST.__objc_superrefs: 0x1e8
-  __AUTH_CONST.__auth_got: 0x1900
+  __AUTH_CONST.__auth_got: 0x1908
   __AUTH_CONST.__auth_ptr: 0x1398
-  __AUTH_CONST.__const: 0x96e0
+  __AUTH_CONST.__const: 0x9870
   __AUTH_CONST.__cfstring: 0x5640
-  __AUTH_CONST.__objc_const: 0x239f8
+  __AUTH_CONST.__objc_const: 0x238c8
   __AUTH_CONST.__objc_intobj: 0x108
-  __AUTH.__objc_data: 0xb8
-  __AUTH.__data: 0x530
+  __AUTH.__objc_data: 0x158
+  __AUTH.__data: 0x768
   __DATA.__objc_ivar: 0x858
-  __DATA.__data: 0x3610
-  __DATA.__bss: 0xc880
-  __DATA.__common: 0x150
-  __DATA_DIRTY.__objc_data: 0x3430
-  __DATA_DIRTY.__data: 0x74c0
+  __DATA.__data: 0x3740
+  __DATA.__bss: 0xcd00
+  __DATA.__common: 0x178
+  __DATA_DIRTY.__objc_data: 0x3390
+  __DATA_DIRTY.__data: 0x71b0
   __DATA_DIRTY.__bss: 0x3e80
   __DATA_DIRTY.__common: 0x2b0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswiftObservation.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib
   - /usr/lib/swift/libswiftRegexBuilder.dylib
+  - /usr/lib/swift/libswiftSynchronization.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 8485
-  Symbols:   3557
-  CStrings:  5958
+  Functions: 8512
+  Symbols:   3547
+  CStrings:  5968
 
Symbols:
+ _swift_runtimeSupportsNoncopyableTypes
CStrings:
+ "%{public}s Error while indexing %@"
+ "%{public}s Failed to remove index, error=%{public}@"
+ "%{public}s Got inference %{public}s"
+ "%{public}s Indexing but not waiting for result because device is class C locked"
+ "%{public}s Notification inference failed with error: %@"
+ "%{public}s Overwriting summary: %s,  priority: %{bool}d."
+ "%{public}s Removing index"
+ "%{public}s Skip indexing, reason=%s"
+ ", priorityStatus: "
+ ", summaryStatus: "
+ "Dropping %ld inferences, notificationInferenceClient isn't set up"
+ "Failed to get redacted bundleId. %@"
+ "NotificationInference(summaryLength: "
+ "[id=%s] %ld Observers waiting on inferences for %ld spotlightIdentifiers"
+ "[id=%s] Cancelling observer before waiting for result"
+ "[id=%s] Error: %ld observers. Only 1 observer expected. Copying inference to all observers %s"
+ "[id=%s] Error: No observers, dropping inference %s"
+ "[id=%s] Error: Received %ld inferences for the same spotlightIdentifier. Keeping first inference, dropping rest. %s"
+ "[id=%s] Found observer that's older than %f seconds. Likely abandonded."
+ "[id=%s] Observer cancelled, unable to wait for inference"
+ "[id=%s] Observer received inference %s"
+ "[id=%s] Observer received inference %s but hasn't started waiting for result yet"
+ "[id=%s] Observing"
+ "[id=%s] Programming Error: Cancelling already cancelled observer"
+ "[id=%s] Programming Error: Missing inferences"
+ "[id=%s] Programming Error: Observer cancelled, can't receive inference: %s"
+ "[id=%s] Programming Error: Receive called multiple times for same observer"
+ "[id=%s] Waiting for inference"
+ "_TtC21UserNotificationsCore27NotificationInferenceClient"
+ "_TtCC21UserNotificationsCore27NotificationInferenceClientP33_B3E86FDDC0F0F128881A9BB8C4FF2FA98Observer"
+ "bundleId"
+ "cancelObserversAfterSeconds"
+ "cancelled"
+ "createdDate"
+ "indexedButNoWaitClassCLocked"
+ "indexingInterval"
+ "inference"
+ "inference(for:analytics:)"
+ "notificationInferenceClient"
+ "observers"
+ "waitingForResultInterval"
- "Failed to get inference: %{public}s, error=%{public}@"
- "Failed to get redacted bundleId. "
- "Failed to index: %{public}s, error=%{public}@"
- "Failed to remove index: %{public}s, error=%{public}@"
- "Got inference: %{public}s, %{public}s"
- "Handling notification results: %ld"
- "No observers for notification results"
- "Overwriting summary: %s,  priority: %{bool}d."
- "Received unknown result for %s"
- "Removing index: %{public}s"
- "Skip indexing: %{public}s, reason=%s"
- "Waiting for inference: %{public}s"
- "_TtC21UserNotificationsCore34NotificationInferenceObserverEntry"
- "_TtC21UserNotificationsCore47SpotlightNotificationInferenceBufferingObserver"
- "_TtCC21UserNotificationsCore28IntelligenceServiceAnalytics16WaitingForResult"
- "_TtCC21UserNotificationsCore28IntelligenceServiceAnalytics8Indexing"
- "cancelBlock"
- "com.apple.UserNotifications.SpotlightNotificationInferenceBufferingObserver"
- "com.apple.UserNotifications.SpotlightNotificationInferenceBufferingObserver.callOut"
- "indexing"
- "inference(_:observer:)"
- "isHighlight: nil"
- "objectIdentifier"
- "queue_notificationInferenceObservers"
- "queue_results"
- "queue_resultsBlock"
- "redacted-summarization-pipeline-client-unavailable"
- "serviceError"
- "topLineSummary: nil"
- "topLineSummaryLength: "
- "waitingForResult"

```
