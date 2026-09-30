## AppIntentsServices

> `/System/Library/PrivateFrameworks/AppIntentsServices.framework/AppIntentsServices`

```diff

-31.17.2.0.0
-  __TEXT.__text: 0x1daa40
-  __TEXT.__auth_stubs: 0x2750
+31.21.0.0.0
+  __TEXT.__text: 0x1f59e4
+  __TEXT.__auth_stubs: 0x2720
   __TEXT.__objc_methlist: 0x184
-  __TEXT.__cstring: 0x5311
-  __TEXT.__swift5_typeref: 0x4dda
-  __TEXT.__swift5_capture: 0x15f4
-  __TEXT.__const: 0xec08
-  __TEXT.__constg_swiftt: 0x414c
-  __TEXT.__swift5_reflstr: 0x2b0c
-  __TEXT.__swift5_fieldmd: 0x3e64
-  __TEXT.__swift5_builtin: 0x2bc
-  __TEXT.__swift5_assocty: 0x660
+  __TEXT.__cstring: 0x5381
+  __TEXT.__swift5_typeref: 0x510c
+  __TEXT.__swift5_capture: 0x1590
+  __TEXT.__const: 0x100b8
+  __TEXT.__constg_swiftt: 0x42c8
+  __TEXT.__swift5_reflstr: 0x2b8c
+  __TEXT.__swift5_fieldmd: 0x414c
+  __TEXT.__swift5_builtin: 0x2a8
+  __TEXT.__swift5_assocty: 0x6a8
   __TEXT.__swift5_protos: 0xec
-  __TEXT.__swift5_proto: 0xdcc
-  __TEXT.__swift5_types: 0x490
-  __TEXT.__oslogstring: 0x245e
+  __TEXT.__swift5_proto: 0xed8
+  __TEXT.__swift5_types: 0x4bc
+  __TEXT.__oslogstring: 0x210e
   __TEXT.__swift5_mpenum: 0xf0
-  __TEXT.__swift5_acfuncs: 0x154
-  __TEXT.__unwind_info: 0x84a8
-  __TEXT.__eh_frame: 0x136e0
+  __TEXT.__swift5_acfuncs: 0x1a4
+  __TEXT.__unwind_info: 0x8d50
+  __TEXT.__eh_frame: 0x15030
   __TEXT.__objc_classname: 0x4a
-  __TEXT.__objc_methname: 0x1a9a
+  __TEXT.__objc_methname: 0x1a65
   __TEXT.__objc_methtype: 0x36a
-  __DATA_CONST.__got: 0xa70
+  __DATA_CONST.__got: 0xb00
   __DATA_CONST.__const: 0x268
   __DATA_CONST.__objc_classlist: 0x100
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x838
+  __DATA_CONST.__objc_selrefs: 0x828
   __DATA_CONST.__objc_protorefs: 0x18
-  __AUTH_CONST.__auth_got: 0x13a8
-  __AUTH_CONST.__auth_ptr: 0xf88
-  __AUTH_CONST.__const: 0x8ab8
-  __AUTH_CONST.__objc_const: 0x2820
+  __AUTH_CONST.__auth_got: 0x1390
+  __AUTH_CONST.__auth_ptr: 0x10b0
+  __AUTH_CONST.__const: 0x8ae0
+  __AUTH_CONST.__objc_const: 0x28a0
   __AUTH.__objc_data: 0x158
-  __AUTH.__data: 0x19d8
-  __DATA.__data: 0x4bb0
-  __DATA.__bss: 0x168f0
-  __DATA.__common: 0xa58
+  __AUTH.__data: 0x1ed8
+  __DATA.__data: 0x4f48
+  __DATA.__bss: 0x18b00
+  __DATA.__common: 0x10b0
   __DATA_DIRTY.__objc_data: 0x438
   __DATA_DIRTY.__data: 0x3238
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/Frameworks/Intents.framework/Intents
   - /System/Library/Frameworks/Network.framework/Network
   - /System/Library/PrivateFrameworks/BackgroundSystemTasks.framework/BackgroundSystemTasks
+  - /System/Library/PrivateFrameworks/DiagnosticRequest.framework/DiagnosticRequest
   - /System/Library/PrivateFrameworks/FeatureFlags.framework/FeatureFlags
   - /System/Library/PrivateFrameworks/InternalSwiftProtobuf.framework/InternalSwiftProtobuf
   - /System/Library/PrivateFrameworks/LinkMetadata.framework/LinkMetadata
   - /System/Library/PrivateFrameworks/LinkServices.framework/LinkServices
+  - /System/Library/PrivateFrameworks/PowerLog.framework/PowerLog
   - /System/Library/PrivateFrameworks/UserManagement.framework/UserManagement
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 11188
-  Symbols:   3143
-  CStrings:  1136
+  Functions: 11974
+  Symbols:   3378
+  CStrings:  1134
 
Symbols:
+ _BGSystemTaskSchedulerErrorDomain
+ _DRTailspinRequest
+ _PPSCreateTelemetryIdentifier
+ _PPSSendTelemetry
- _OBJC_CLASS_$_LNFeatureFlags
- _OBJC_CLASS_$_NSDistributedNotificationCenter
- _notify_post
- _notify_register_dispatch
- _notify_set_state
CStrings:
+ ".FetchFileChunkRequest"
+ ".RestartObservingEventRequest"
+ ".StartObservingEventRequest"
+ ".StartObservingEventResponse"
+ ".StopObservingEventRequest"
+ "Closing the fileHandle"
+ "Could not close fileHandle: %!s(MISSING)"
+ "Failed to emit tailspin: %!s(MISSING)"
+ "Incorrect listener"
+ "No valid instances for %!s(MISSING)"
+ "Personal content access is disabled."
+ "Released cached entry for %!s(MISSING)"
+ "Requesting tailspin: %!s(MISSING)"
+ "TailspinThreshold"
+ "Unable to create PPSCreateTelemetryIdentifier"
+ "Unable to parse URL"
+ "_TtCO18AppIntentsServices8PowerLog10DataStream"
+ "closeAndReturnError:"
+ "emitTailspinThreshold"
+ "fileHandleForReadingAtPath:"
+ "length"
+ "metrics"
+ "offset"
+ "powerLogId"
+ "seekToFileOffset:"
+ "start"
+ "stream"
+ "took longer than "
- "%!s(MISSING)Attempting to submit metrics with no underlying NWActivity"
- "ActorCall %!s(MISSING) completed with invalidation error: %!@(MISSING)"
- "Feature not enabled"
- "NotificationCenter: Cannot start listener for %!s(MISSING), already started"
- "NotificationCenter: Cannot stop listener for %!s(MISSING), already stopped"
- "NotificationCenter: Expected notification name: %!s(MISSING), expected %!s(MISSING)"
- "NotificationCenter: Failed to register to set isObserved state"
- "NotificationCenter: Failed to set isObserved state for %!s(MISSING)"
- "NotificationCenter: Failed to set observed state for %!s(MISSING)"
- "NotificationCenter: Incorrect encoded data %!s(MISSING): %!s(MISSING)"
- "NotificationCenter: Incorrect event data format for %!s(MISSING)"
- "NotificationCenter: Notification Center not allocated"
- "NotificationCenter: Setting isObserved state as %!l(MISSING)lu for %!s(MISSING)"
- "NotificationCenter: Starting to observe %!s(MISSING), topic: %!s(MISSING)"
- "NotificationCenter: Stopped observing %!s(MISSING)"
- "_TtCC18AppIntentsServices28AppNotificationEventRegistry31DistributedNotificationListener"
- "addObserverForName:object:queue:usingBlock:"
- "appintents.appevent"
- "appintents.observability-state"
- "asyncSequenceRetrofit"
- "defaultCenter"
- "fileExistsAtPath:"
- "isProductionAppEventEnabled"
- "notificationCenter"
- "notificationObservers"
- "productionAppEvent feature flag enabled - switching to XPC interface with linkd"
- "productionAppEvent feature flag not enabled - falling back to notification center logic"
- "queriesIncludeFirstElementPage"
- "removeObserver:"
- "v12@?0i8"
- "v16@?0@\"NSNotification\"8"

```
