## DeviceSharing

> `/System/Library/PrivateFrameworks/DeviceSharing.framework/DeviceSharing`

```diff

-27.60.27.0.1
-  __TEXT.__text: 0x59cc0
-  __TEXT.__auth_stubs: 0x1ac0
-  __TEXT.__objc_methlist: 0x154
-  __TEXT.__const: 0x14c8
-  __TEXT.__cstring: 0x2078
-  __TEXT.__swift5_typeref: 0xeb3
-  __TEXT.__swift5_fieldmd: 0x714
-  __TEXT.__constg_swiftt: 0x1178
+27.60.30.0.1
+  __TEXT.__text: 0x58ecc
+  __TEXT.__auth_stubs: 0x1b10
+  __TEXT.__objc_methlist: 0x170
+  __TEXT.__const: 0x1508
+  __TEXT.__cstring: 0x1f38
+  __TEXT.__swift5_typeref: 0xe71
+  __TEXT.__swift5_fieldmd: 0x720
+  __TEXT.__constg_swiftt: 0x1118
   __TEXT.__swift5_builtin: 0x3c
-  __TEXT.__swift5_reflstr: 0x5f2
+  __TEXT.__swift5_reflstr: 0x602
   __TEXT.__swift5_assocty: 0xf0
-  __TEXT.__swift5_protos: 0x3c
-  __TEXT.__swift5_proto: 0xec
-  __TEXT.__swift5_types: 0x98
-  __TEXT.__swift5_capture: 0x620
-  __TEXT.__oslogstring: 0x1229
+  __TEXT.__swift5_protos: 0x40
+  __TEXT.__swift5_proto: 0xf0
+  __TEXT.__swift5_types: 0x94
+  __TEXT.__oslogstring: 0x14b9
+  __TEXT.__swift5_capture: 0x520
   __TEXT.__swift5_mpenum: 0x10
-  __TEXT.__unwind_info: 0x1918
-  __TEXT.__eh_frame: 0x44b8
+  __TEXT.__unwind_info: 0x1788
+  __TEXT.__eh_frame: 0x3e38
   __TEXT.__objc_classname: 0x93
-  __TEXT.__objc_methname: 0x816
+  __TEXT.__objc_methname: 0x81c
   __TEXT.__objc_methtype: 0x25d
   __TEXT.__objc_stubs: 0xc0
-  __DATA_CONST.__got: 0x5e0
-  __DATA_CONST.__const: 0x218
+  __DATA_CONST.__got: 0x560
+  __DATA_CONST.__const: 0x230
   __DATA_CONST.__objc_classlist: 0x70
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1f8
+  __DATA_CONST.__objc_selrefs: 0x200
   __DATA_CONST.__objc_protorefs: 0x30
-  __AUTH_CONST.__auth_got: 0xd68
+  __AUTH_CONST.__auth_got: 0xd90
   __AUTH_CONST.__auth_ptr: 0x530
-  __AUTH_CONST.__const: 0x1880
+  __AUTH_CONST.__const: 0x16c8
   __AUTH_CONST.__cfstring: 0x80
-  __AUTH_CONST.__objc_const: 0x12e0
-  __AUTH.__objc_data: 0x4f0
-  __AUTH.__data: 0xa08
-  __DATA.__data: 0x1928
+  __AUTH_CONST.__objc_const: 0x1310
+  __AUTH.__objc_data: 0x448
+  __AUTH.__data: 0xa38
+  __DATA.__data: 0x1790
   __DATA.__bss: 0x1580
-  __DATA.__common: 0xf0
+  __DATA.__common: 0x108
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 1604
-  Symbols:   275
-  CStrings:  431
+  Functions: 1519
+  Symbols:   269
+  CStrings:  436
 
Symbols:
+ _objc_retain_x1
+ _swift_continuation_resume
+ _swift_task_isCurrentExecutor
- _OBJC_CLASS_$_AVOutputContextDestinationChange
- _dispatch_sync
CStrings:
+ " %!s(MISSING) !!! PEER LISTENER FAILED !!!"
+ "%!s(MISSING)"
+ "%!s(MISSING) %!s(MISSING): observerCount:%!l(MISSING)d"
+ "%!s(MISSING) Invalidating peer connection."
+ "%!s(MISSING) [%!s(MISSING)] resuming activate(), connection is ready"
+ "%!s(MISSING): Performed authentication manager request with ID %!s(MISSING)"
+ "%!s(MISSING): Performing authentication manager request"
+ "%!s(MISSING): Resuming authentication manager request for %!s(MISSING)"
+ "%!s(MISSING): Resuming authentication manager request for %!s(MISSING) with error %!@(MISSING)"
+ "DeviceSharing/SharingInteractionController.swift"
+ "Incorrect actor executor assumption; Expected same executor as "
+ "LiveActivityCoordinator"
+ "Peer Connection Service sending heartbeat"
+ "Received heartbeat."
+ "[%!s(MISSING)] %!s(MISSING) Sending guest user access response: %!s(MISSING)"
+ "[%!s(MISSING)] Clearing previous browsing state and results"
+ "[%!s(MISSING)] Error sending heartbeat: %!@(MISSING)"
+ "[%!s(MISSING)] Heartbeat cancelled"
+ "[%!s(MISSING)] Peer Connection failed. Stopping Live activity and invalidating the prox card."
+ "[%!s(MISSING)] Unable to start Live Activity - %!@(MISSING)"
+ "[%!s(MISSING)] Waiting to send heartbeat..."
+ "[UserDefaults: com.apple.devicesharingd]"
+ "dictionaryRepresentation"
+ "ds_log"
+ "heartBeatTask"
+ "liveActivityCoordinator"
+ "readyContinuation"
+ "startHeartBeat()"
+ "startLiveActivity()"
- "%!s(MISSING) received %!l(MISSING)d"
- "%!s(MISSING) received %!s(MISSING)"
- "%!s(MISSING) sending update"
- "%!s(MISSING) sending updated optional %!s(MISSING)"
- "%!s(MISSING) sending updated value %!l(MISSING)d"
- "/Library/Caches/com.apple.xbs/Sources/DeviceSharing/DeviceSharing/Daemon/Peer/PeerListener.swift"
- "/Library/Caches/com.apple.xbs/Sources/DeviceSharing/DeviceSharing/Daemon/Servers/TestServer.swift"
- "XPCServer<TestTransportItem>"
- "[%!s(MISSING)] %!s(MISSING) !!!Sending guest user access response!!!!"
- "[%!s(MISSING)] Starting Live Activity"
- "[%!s(MISSING)] Stopping Live Activity"
- "peerConnectionDidCancel()"
- "peerConnectionDidFail(error:)"
- "setOutputDevice(_:)"
- "sharedSystemScreenContext"
- "testAddObserver()"
- "testOptionalToOptional(optional:)"
- "testOptionalToValue(optional:)"
- "testRemoveObserver()"
- "testValueToOptional(value:)"
- "testValueToValue(value:)"
- "testVoidToOptional()"
- "testVoidToValue()"
- "testVoidToVoid()"

```
