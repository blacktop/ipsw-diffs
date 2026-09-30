## DistributedTimersDaemon

> `/System/Library/PrivateFrameworks/DistributedTimersDaemon.framework/DistributedTimersDaemon`

```diff

-98.0.24.0.0
-  __TEXT.__text: 0x84420
-  __TEXT.__auth_stubs: 0x1fa0
-  __TEXT.__objc_methlist: 0x8c
-  __TEXT.__const: 0x1e30
-  __TEXT.__cstring: 0x14b9
-  __TEXT.__swift5_typeref: 0xe16
-  __TEXT.__oslogstring: 0x1a21
-  __TEXT.__swift5_reflstr: 0x769
+98.10.6.0.0
+  __TEXT.__text: 0x8ab98
+  __TEXT.__auth_stubs: 0x2020
+  __TEXT.__objc_methlist: 0xb0
+  __TEXT.__const: 0x1e60
+  __TEXT.__cstring: 0x1729
+  __TEXT.__swift5_typeref: 0xe76
+  __TEXT.__oslogstring: 0x1d71
+  __TEXT.__swift5_reflstr: 0x829
   __TEXT.__swift5_assocty: 0x138
-  __TEXT.__constg_swiftt: 0x770
-  __TEXT.__swift5_fieldmd: 0x958
+  __TEXT.__constg_swiftt: 0x7d4
+  __TEXT.__swift5_fieldmd: 0x9e0
   __TEXT.__swift5_protos: 0x8
   __TEXT.__swift5_proto: 0x1ac
-  __TEXT.__swift5_types: 0x84
-  __TEXT.__swift5_capture: 0x874
+  __TEXT.__swift5_types: 0x88
+  __TEXT.__swift5_capture: 0x8d4
   __TEXT.__swift5_builtin: 0x3c
-  __TEXT.__unwind_info: 0x1960
-  __TEXT.__eh_frame: 0x43c0
-  __TEXT.__objc_classname: 0xbb
-  __TEXT.__objc_methname: 0x1911
-  __TEXT.__objc_methtype: 0x6a3
-  __DATA_CONST.__got: 0x678
-  __DATA_CONST.__const: 0x128
-  __DATA_CONST.__objc_classlist: 0x50
-  __DATA_CONST.__objc_protolist: 0xa0
+  __TEXT.__unwind_info: 0x1978
+  __TEXT.__eh_frame: 0x44b8
+  __TEXT.__objc_classname: 0xd9
+  __TEXT.__objc_methname: 0x1aec
+  __TEXT.__objc_methtype: 0x7bc
+  __DATA_CONST.__got: 0x690
+  __DATA_CONST.__const: 0x170
+  __DATA_CONST.__objc_classlist: 0x58
+  __DATA_CONST.__objc_protolist: 0xb0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3e0
-  __DATA_CONST.__objc_protorefs: 0x50
-  __AUTH_CONST.__auth_got: 0xfd0
+  __DATA_CONST.__objc_selrefs: 0x3f8
+  __DATA_CONST.__objc_protorefs: 0x58
+  __AUTH_CONST.__auth_got: 0x1010
   __AUTH_CONST.__auth_ptr: 0x4c8
-  __AUTH_CONST.__const: 0x20f0
-  __AUTH_CONST.__objc_const: 0x2038
-  __AUTH.__objc_data: 0x350
-  __AUTH.__data: 0xa80
-  __DATA.__data: 0x10b8
-  __DATA.__bss: 0x3a50
-  __DATA.__common: 0x40
+  __AUTH_CONST.__const: 0x2118
+  __AUTH_CONST.__objc_const: 0x2380
+  __AUTH.__objc_data: 0x378
+  __AUTH.__data: 0xb70
+  __DATA.__data: 0x1198
+  __DATA.__bss: 0x3a90
+  __DATA.__common: 0x48
   - /System/Library/Frameworks/CloudKit.framework/CloudKit
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswiftQuartzCore.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
+  - /usr/lib/swift/libswift_errno.dylib
+  - /usr/lib/swift/libswift_math.dylib
+  - /usr/lib/swift/libswift_signal.dylib
+  - /usr/lib/swift/libswift_stdio.dylib
+  - /usr/lib/swift/libswift_time.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1752
-  Symbols:   320
-  CStrings:  670
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
+  Functions: 1786
+  Symbols:   321
+  CStrings:  723
 
Symbols:
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_math
+ __swift_FORCE_LOAD_$_swift_signal
+ __swift_FORCE_LOAD_$_swift_stdio
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swiftsys_time
+ __swift_FORCE_LOAD_$_swiftunistd
+ _xpc_connection_get_peer_instance
- _swift_continuation_await
- _swift_continuation_init
CStrings:
+ "### Monitor start failed: no xpc connection, accessory=%!s(MISSING)"
+ "### Report event failed: %!s(MISSING), error=%!s(MISSING)"
+ "HMMM register retry"
+ "HMSiriEndpointProfileDelegate"
+ "HomeKit didUpdateHomes: %!{(MISSING)public}s"
+ "HomeKit didUpdateSessionHubIdentifier: id=%!s(MISSING), name=%!s(MISSING)"
+ "HomeKit ready"
+ "MT no future: addAlarm"
+ "MT no future: addTimer"
+ "MT no future: dismissAlarm"
+ "MT no future: dismissTimer"
+ "MT no future: removeAlarm"
+ "MT no future: removeTimer"
+ "MT no future: snoozeAlarm"
+ "MT no future: updateAlarm"
+ "MT no future: updateTimer"
+ "Monitor Incoming: monitorID="
+ "Monitor Local: clientID="
+ "Monitor Outgoing: monitorID="
+ "Monitor start local: monitorID=%!l(MISSING)lu, targets=[%!s(MISSING)]"
+ "Monitor start outgoing: monitorID=%!l(MISSING)lu, targets=[%!s(MISSING)]"
+ "Monitor stop outgoing: monitorID=%!l(MISSING)lu"
+ "Report event: %!s(MISSING), client=%!s(MISSING)"
+ "Report event: event=%!s(MISSING), filteredTimers=%!s(MISSING), timers=%!s(MISSING), targets=[%!s(MISSING)], local"
+ "Report event: event=%!s(MISSING), filteredTimers=%!s(MISSING), timers=%!s(MISSING), targets=[%!s(MISSING)], outgoing"
+ "Report event: event=%!s(MISSING), filteredTimers=%!s(MISSING), timers=%!s(MISSING), targets=[%!s(MISSING)], peer=%!s(MISSING), incoming"
+ "RequestForSelf: request=%!s(MISSING), %!s(MISSING)"
+ "Server deletion extant: alarm=%!s(MISSING)"
+ "Server deletion gone: id=%!s(MISSING)"
+ "Server deletion: extant, timer=%!s(MISSING)"
+ "XPC connection started: client=%!s(MISSING), instanceID=%!s(MISSING)"
+ "_TtCC23DistributedTimersDaemon17DTTransportDaemonP33_D0772C63A9128FD93A891935DD2DF83A27DTTransportMonitorInfoLocal"
+ "_homeKitPollDeadline"
+ "_homeKitPollTask"
+ "_homeSiriEndpointMap"
+ "_homeSiriEndpointsReady"
+ "_monitorContext"
+ "_monitorSessionsLocal"
+ "didUpdateDataSyncInProgress: %!{(MISSING)public}s"
+ "didUpdateStatus: %!{(MISSING)public}s"
+ "dismissAlarm: %!s(MISSING)"
+ "dismissAlarm: not found, %!s(MISSING)"
+ "dismissTimer: %!s(MISSING)"
+ "dismissTimer: not found, %!s(MISSING)"
+ "home:didUpdateDismissedWalletKeyUWBUnlockOnboarding:"
+ "monitor start incoming: monitorID=%!s(MISSING), targets=[%!s(MISSING)]"
+ "monitor stop incoming: monitorID=%!s(MISSING)"
+ "siriEndpointProfile:didUpdateAssistants:"
+ "siriEndpointProfile:didUpdateCurrentAssistant:"
+ "siriEndpointProfile:didUpdateManuallyDisabled:"
+ "siriEndpointProfile:didUpdateMultifunctionButton:"
+ "siriEndpointProfile:didUpdateNeedsOnboarding:"
+ "siriEndpointProfile:didUpdateSessionHubIdentifier:"
+ "siriEndpointProfile:didUpdateSessionState:"
+ "siriEndpointProfile:didUpdateSiriEngineVersion:"
+ "siriEndpointProfile:didUpdateSupportsOnboarding:"
+ "targets"
+ "v28@0:8@\"HMSiriEndpointProfile\"16B24"
+ "v32@0:8@\"HMSiriEndpointProfile\"16@\"HMSiriEndpointProfileAssistant\"24"
+ "v32@0:8@\"HMSiriEndpointProfile\"16@\"NSArray\"24"
+ "v32@0:8@\"HMSiriEndpointProfile\"16@\"NSString\"24"
+ "v32@0:8@\"HMSiriEndpointProfile\"16@\"NSUUID\"24"
+ "v32@0:8@\"HMSiriEndpointProfile\"16q24"
+ "xpcInstanceID"
- "### Monitor start failed: no ids, monitorID=%!l(MISSING)lu, accessory=%!s(MISSING)"
- "### Report client event failed: event=%!s(MISSING), error=%!s(MISSING)"
- "DistributedTimersDaemon/DTDaemon.swift"
- "HomeKit didUpdateHomes: dataSyncState=%!s(MISSING), status=%!s(MISSING)"
- "Monitor Incoming: id="
- "Monitor Outgoing: id="
- "Monitor start: monitorID=%!l(MISSING)lu, accessory=%!s(MISSING)"
- "Monitor stop: monitorID=%!l(MISSING)lu"
- "Report client event: event=%!s(MISSING), timers=%!s(MISSING), client=%!s(MISSING)"
- "Report client event: event=%!s(MISSING), timers=%!s(MISSING), peer=%!s(MISSING)"
- "RequestForSelf: request=%!s(MISSING)"

```
