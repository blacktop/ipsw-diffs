## AppIntentsServices

> `/System/Library/PrivateFrameworks/AppIntentsServices.framework/AppIntentsServices`

```diff

-33.19.0.0.0
-  __TEXT.__text: 0x1cf838
-  __TEXT.__auth_stubs: 0x2820
+34.5.0.0.0
+  __TEXT.__text: 0x1d315c
+  __TEXT.__auth_stubs: 0x29c0
   __TEXT.__objc_methlist: 0x614
-  __TEXT.__cstring: 0x5a11
-  __TEXT.__swift5_typeref: 0x5702
-  __TEXT.__swift5_capture: 0x17b4
-  __TEXT.__const: 0x142d8
-  __TEXT.__constg_swiftt: 0x4aa8
-  __TEXT.__swift5_reflstr: 0x2f4c
-  __TEXT.__swift5_fieldmd: 0x48a8
-  __TEXT.__swift5_builtin: 0x2d0
+  __TEXT.__const: 0x14be0
+  __TEXT.__cstring: 0x5e81
+  __TEXT.__constg_swiftt: 0x4fcc
+  __TEXT.__swift5_typeref: 0x5990
+  __TEXT.__swift5_reflstr: 0x32cc
+  __TEXT.__swift5_fieldmd: 0x4cec
+  __TEXT.__swift5_builtin: 0x2f8
   __TEXT.__swift5_assocty: 0x710
-  __TEXT.__swift5_protos: 0xf0
-  __TEXT.__swift5_proto: 0xfc8
-  __TEXT.__swift5_types: 0x530
-  __TEXT.__swift_as_entry: 0x568
-  __TEXT.__swift_as_ret: 0x5cc
-  __TEXT.__oslogstring: 0x287e
-  __TEXT.__swift5_mpenum: 0x12c
+  __TEXT.__oslogstring: 0x28ce
+  __TEXT.__swift5_capture: 0x1934
+  __TEXT.__swift5_mpenum: 0x150
+  __TEXT.__swift5_proto: 0xfe8
+  __TEXT.__swift5_types: 0x588
+  __TEXT.__swift5_types2: 0x8
+  __TEXT.__swift_as_entry: 0x60c
+  __TEXT.__swift_as_ret: 0x648
+  __TEXT.__swift5_protos: 0xec
   __TEXT.__swift5_acfuncs: 0x168
-  __TEXT.__unwind_info: 0x8cd8
-  __TEXT.__eh_frame: 0x16d28
+  __TEXT.__unwind_info: 0x9238
+  __TEXT.__eh_frame: 0x17c98
   __TEXT.__objc_classname: 0x59
-  __TEXT.__objc_methname: 0x1f72
+  __TEXT.__objc_methname: 0x1fa0
   __TEXT.__objc_methtype: 0x3f6
-  __DATA_CONST.__got: 0xbe8
-  __DATA_CONST.__const: 0x158
-  __DATA_CONST.__objc_classlist: 0x128
+  __DATA_CONST.__got: 0xc08
+  __DATA_CONST.__const: 0x168
+  __DATA_CONST.__objc_classlist: 0x140
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xa88
+  __DATA_CONST.__objc_selrefs: 0xaa0
   __DATA_CONST.__objc_protorefs: 0x20
-  __AUTH_CONST.__auth_got: 0x1410
-  __AUTH_CONST.__auth_ptr: 0x1218
-  __AUTH_CONST.__const: 0x9650
-  __AUTH_CONST.__objc_const: 0x2e80
-  __AUTH.__objc_data: 0x3b8
-  __AUTH.__data: 0x2bb0
-  __DATA.__data: 0x5b10
-  __DATA.__bss: 0x1a990
-  __DATA.__common: 0x11e0
+  __AUTH_CONST.__auth_got: 0x14e0
+  __AUTH_CONST.__auth_ptr: 0x1160
+  __AUTH_CONST.__const: 0xa1b0
+  __AUTH_CONST.__objc_const: 0x3250
+  __AUTH.__objc_data: 0x408
+  __AUTH.__data: 0x3040
+  __DATA.__data: 0x6358
+  __DATA.__bss: 0x1ae10
+  __DATA.__common: 0x11f8
   __DATA_DIRTY.__objc_data: 0x458
-  __DATA_DIRTY.__data: 0x33a0
+  __DATA_DIRTY.__data: 0x3378
   __DATA_DIRTY.__common: 0x30
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreSpotlight.framework/CoreSpotlight

   - /System/Library/Frameworks/Intents.framework/Intents
   - /System/Library/Frameworks/Network.framework/Network
   - /System/Library/PrivateFrameworks/BackgroundSystemTasks.framework/BackgroundSystemTasks
+  - /System/Library/PrivateFrameworks/BiometricKit.framework/BiometricKit
   - /System/Library/PrivateFrameworks/DiagnosticRequest.framework/DiagnosticRequest
   - /System/Library/PrivateFrameworks/FeatureFlags.framework/FeatureFlags
   - /System/Library/PrivateFrameworks/InternalSwiftProtobuf.framework/InternalSwiftProtobuf

   - /System/Library/PrivateFrameworks/LinkServices.framework/LinkServices
   - /System/Library/PrivateFrameworks/PowerLog.framework/PowerLog
   - /System/Library/PrivateFrameworks/UserManagement.framework/UserManagement
+  - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftCore.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 11800
-  Symbols:   3531
-  CStrings:  1274
+  Functions: 12067
+  Symbols:   3478
+  CStrings:  1328
 
Symbols:
+ _MobileGestalt_copy_deviceClass_obj
+ _MobileGestalt_get_current_device
+ _OBJC_CLASS_$_BiometricKit
+ _OBJC_CLASS_$_LNSystemContext
+ _notify_cancel
+ _notify_get_state
+ _notify_register_dispatch
+ _swift_getFunctionTypeMetadata0
+ _swift_initStructMetadata
+ _swift_setDeallocating
+ _swift_unownedRelease
+ _swift_unownedRetain
+ _swift_unownedRetainStrong
- _objc_release_x9
CStrings:
+ "%s failed to register for %s"
+ "%s listening for: %s"
+ "%s received notification for %s"
+ "%s stopping for: %s"
+ "%s unable to get current state for %s"
+ "%s%s %s"
+ "%s: device lock state changed"
+ "%s: isBiometricAuthenticationLocked took %fms"
+ "%sNo endpoint available"
+ "%sNo supported device found, falling back to first result"
+ "%sSelected %s"
+ "%sSeveral eligible endpoints found, arbitrarily selecting the first one:\n%s"
+ "<%s#%ld> ERROR: failed waiting to retry: %@"
+ "<%s#%ld> Error is immediately retryable"
+ "<%s#%ld> Error is not retryable"
+ "<%s#%ld> Error is transient, retrying when ready"
+ "<%s#%ld> Ready to retry"
+ "<%s#%ld> Retry attempt cancelled"
+ "<%s#%ld> completed"
+ "<%s#%ld> executing closure on %s"
+ "<%s#%ld> threw %@"
+ "<%s#%ld> was cancelled"
+ "<%s> cannot yield progress"
+ "<%s> fail invoked"
+ "<%s> yielding progress"
+ "> (parent cancelled)"
+ "> from active calls"
+ "AppIntentsServices/RemoteAppNotificationStream.swift"
+ "Applying state %s to %s"
+ "AsyncSequenceElementPage(complete: "
+ "BiometricKitHelper<"
+ "CallManager not initialized"
+ "CallManager update stream completed"
+ "Cancelling <%s> (parent cancelled)"
+ "DistributedActorManager not initialized"
+ "ERROR: evaluateRetries called while retry task already pending"
+ "Enqueuing call <%s> to active calls"
+ "INVALID STATE: RemoteAppNotificationStream wrappedStream should never be nil"
+ "Removing <%s> from active calls"
+ "Stream %s stopped listening for actor updates"
+ "The device is locked."
+ "USAGE ERROR: ActorCall executeOn called after completion for <%s>"
+ "_TtC18AppIntentsServices18BiometricKitHelper"
+ "_TtC18AppIntentsServices26DarwinNotificationObserver"
+ "_TtCC18AppIntentsServices18BiometricKitHelper35DeviceLockStateNotificationObserver"
+ "_TtCVV18AppIntentsServices33AppIntentsProtobuf_ClientMessages20PerformActionRequestP33_15D8ACD6F9A04B79071F668CEE455EA313_StorageClass"
+ "_actionIdentifier"
+ "_bundleIdentifier"
+ "_currentState"
+ "_environment"
+ "_options"
+ "_parameters"
+ "_streams"
+ "_systemContext"
+ "actorChangeListener"
+ "actorManager"
+ "actorProvider"
+ "airPods"
+ "callManager"
+ "canceled"
+ "carPlay"
+ "closure"
+ "com.apple.locationd.effective_bundle"
+ "com.apple.locationd.usage_oracle"
+ "com.apple.mobile.keybagd.lock_status"
+ "deviceLockStateObserver"
+ "deviceState"
+ "eyesFree"
+ "getBioLockoutState"
+ "homePod"
+ "init(_:onConnected:onDisconnected:onInvalidated:)"
+ "interfaceIdiom"
+ "invocation"
+ "isBiometricAuthenticationLockedCache"
+ "mac"
+ "manager"
+ "notificationName"
+ "onComplete"
+ "onNotify"
+ "pad"
+ "perform(intent:options:environment:systemContext:)"
+ "phone"
+ "progressUpdater"
+ "retryHandler"
+ "retryStrategy"
+ "setInterfaceIdiom:"
+ "systemContext"
+ "token"
+ "tv"
+ "v12@?0i8"
+ "vision"
+ "watch"
+ "withActor(progressUpdater:_:)"
- "%s%s Device: %s, NWEndpoint: %s, txtRecord: %s"
- "%sDequeued ActorCall %s"
- "%sEnqueuing ActorCall %s"
- "ActorCall %s already completed, no retry on: %@"
- "ActorCall %s cannot fail, it has already completed"
- "ActorCall %s completed returning result"
- "ActorCall %s completed throwing error: %@"
- "ActorCall %s completed with activeError: %@"
- "ActorCall %s does not have a ProgressTask, ignoring: %s"
- "ActorCall %s execution cancelled"
- "ActorCall %s failed at canMakeRemoteCalls with error: %@"
- "ActorCall %s failed with error: %@"
- "ActorCall %s retrying on: %@, remaining attempts: %ld"
- "ActorCall %s waiting on actor instance"
- "ActorCall %s waiting on closure execution"
- "ActorCall %s was already completed when the closure returned"
- "ActorCall %s was already completed when the closure threw: %@"
- "ActorCall %s yielding activeError: %@"
- "AsyncSequenceElementBatch(complete: "
- "No actor for topic %s with identifier %s"
- "Restarting observation for %s with identifier %s"
- "[%s] Dispatcher init completed with remoteDevice: %s"
- "[%s] Dispatcher init waiting with error: %s"
- "[%s] Failed to update actor: %@"
- "[%s] Remote actor updated with endpoint: %s"
- "[%s] updateActor called with existing endpoint, returning early"
- "_TtCC18AppIntentsServices26RemoteAppIntentsDispatcherP33_B5708ECC7F6A26C5132D2814E197AF3B9ActorCall"
- "actor"
- "actorCalls"
- "actorError"
- "com.apple.locationd.effective-bundle"
- "com.apple.locationd.usage-oracle"
- "delegateReferences"
- "onFail"
- "onProgress"
- "perform(intent:options:environment:payloadPrivacy:)"
- "sink"
- "withActor(activity:yieldProgress:_:)"
- "wrappedStream"

```
