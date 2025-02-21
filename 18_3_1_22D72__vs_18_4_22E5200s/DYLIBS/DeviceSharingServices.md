## DeviceSharingServices

> `/System/Library/PrivateFrameworks/DeviceSharingServices.framework/DeviceSharingServices`

```diff

-27.60.30.0.1
-  __TEXT.__text: 0x1ed40
-  __TEXT.__auth_stubs: 0x1030
-  __TEXT.__objc_methlist: 0x480
-  __TEXT.__const: 0x2d2c
-  __TEXT.__cstring: 0x1543
-  __TEXT.__oslogstring: 0x859
-  __TEXT.__swift5_typeref: 0x8b1
+27.100.7.502.1
+  __TEXT.__text: 0x1cb14
+  __TEXT.__auth_stubs: 0xfb0
+  __TEXT.__objc_methlist: 0x614
+  __TEXT.__const: 0x2edc
+  __TEXT.__cstring: 0x1253
+  __TEXT.__oslogstring: 0xaa1
+  __TEXT.__swift5_typeref: 0x8db
   __TEXT.__constg_swiftt: 0x840
   __TEXT.__swift5_reflstr: 0x86c
   __TEXT.__swift5_fieldmd: 0x7c8
   __TEXT.__swift5_builtin: 0x64
-  __TEXT.__swift5_assocty: 0x128
-  __TEXT.__swift5_proto: 0x2cc
+  __TEXT.__swift5_assocty: 0x140
+  __TEXT.__swift5_proto: 0x2d0
   __TEXT.__swift5_types: 0xd4
   __TEXT.__swift5_capture: 0x34
   __TEXT.__swift5_protos: 0xc
-  __TEXT.__unwind_info: 0xcb0
-  __TEXT.__eh_frame: 0x14f8
+  __TEXT.__swift_as_entry: 0x3c
+  __TEXT.__swift_as_ret: 0x34
+  __TEXT.__unwind_info: 0xbf0
+  __TEXT.__eh_frame: 0x14b0
   __TEXT.__objc_classname: 0x11a
-  __TEXT.__objc_methname: 0xd63
+  __TEXT.__objc_methname: 0xd4d
   __TEXT.__objc_methtype: 0x223
   __TEXT.__objc_stubs: 0x680
   __DATA_CONST.__got: 0x1f8
-  __DATA_CONST.__const: 0x2e8
+  __DATA_CONST.__const: 0x2c8
   __DATA_CONST.__objc_classlist: 0x70
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x378
+  __DATA_CONST.__objc_selrefs: 0x418
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x38
-  __AUTH_CONST.__auth_got: 0x820
+  __AUTH_CONST.__auth_got: 0x7e0
   __AUTH_CONST.__auth_ptr: 0x358
-  __AUTH_CONST.__const: 0x1308
-  __AUTH_CONST.__cfstring: 0xb80
-  __AUTH_CONST.__objc_const: 0x1358
+  __AUTH_CONST.__const: 0x1330
+  __AUTH_CONST.__cfstring: 0xba0
+  __AUTH_CONST.__objc_const: 0x1070
   __AUTH.__objc_data: 0x3e0
   __AUTH.__data: 0x3c0
   __DATA.__objc_ivar: 0x64
-  __DATA.__data: 0xa30
-  __DATA.__bss: 0x59b0
+  __DATA.__data: 0xa18
+  __DATA.__bss: 0x5a30
   __DATA.__common: 0x90
   - /System/Library/Frameworks/ActivityKit.framework/ActivityKit
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox

   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
-  - /usr/lib/swift/libswiftFileProvider.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 1043
-  Symbols:   361
-  CStrings:  473
+  Functions: 980
+  Symbols:   368
+  CStrings:  456
 
Symbols:
+ _swift_enumFn_getEnumTag
+ _swift_generic_assignWithCopy
+ _swift_generic_assignWithTake
+ _swift_generic_destroy
+ _swift_generic_initWithCopy
+ _swift_generic_initWithTake
+ _swift_generic_initializeBufferWithCopyOfBuffer
- __swift_FORCE_LOAD_$_swiftFileProvider
- _objc_retain_x25
- _swift_unknownObjectWeakCopyAssign
- _swift_unknownObjectWeakCopyInit
- _swift_unknownObjectWeakDestroy
- _swift_unknownObjectWeakTakeAssign
- _swift_unknownObjectWeakTakeInit
CStrings:
+ "%{public}s decoding image for %{public}s"
+ "%{public}s failed to launch AirPlayReceiver with error %{public}@"
+ "%{public}s failed to launch AirPlayReceiver; unable to create FBSOpenApplicationService"
+ "%{public}s missing icon data for %{public}s"
+ "%{public}s successfully disabled AirPlayReceiver"
+ "%{public}s successfully enabled AirPlayReceiver"
+ "%{public}s successfully launched AirPlayReceiver"
+ "%{public}s unable to decode icon image for %{public}s with error: %{public}@"
+ "ApplicationLibraryIdentifier"
+ "Invalidating alert handler: %{public}@"
+ "Metrics at end of the session: %{public}@ %{public}@ %{public}@ %{public}f %{public}@ %{public}@ %{public}lu %{public}d %{public}d %{public}d %{public}d %{public}d %{public}lu"
+ "Metrics at start of the session: %{public}@ %{public}@ %{public}@ %{public}lu %{public}d, %{public}d, %{public}d, %{public}d, %{public}d, %{public}lu"
+ "Peer Connection Failed"
+ "Remote Unlock Authentication Failed"
+ "Reset the metrics to: %{public}@ %{public}@ %{public}@ %{public}lu %{public}d, %{public}d, %{public}d, %{public}d, %{public}d, %{public}lu"
+ "[%{public}s] %{public}s Remote Alert Deactivated."
+ "[%{public}s] %{public}s isRetrigger: %{bool,public}d."
+ "[%{public}s] %{public}s — %{public}s"
+ "[%{public}s] Failed to start Live Activity: %{public}@"
+ "[%{public}s] Invalidated assertion %{public}@; error %{public}@"
+ "[%{public}s] Live Activity is already active"
+ "[%{public}s] Received response for notification: %{public}lu"
+ "[%{public}s] Started Live Activity %{public}s; assertion %{public}@"
+ "[%{public}s] Starting Live Activity"
+ "[%{public}s] Stopping Live Activity"
+ "[%{public}s] Waiting for response for notification: %{public}lu"
- "%s decoding image for %s"
- "%s failed to launch AirPlayReceiver with error %@"
- "%s failed to launch AirPlayReceiver; unable to create FBSOpenApplicationService"
- "%s missing icon data for %s"
- "%s successfully disabled AirPlayReceiver"
- "%s successfully enabled AirPlayReceiver"
- "%s successfully launched AirPlayReceiver"
- "%s unable to decode icon image for %s with error: %@"
- "Can't construct Array with count < 0"
- "Fatal error"
- "GuestUserSelectedApps"
- "Insufficient space allocated to copy string contents"
- "Invalidating alert handler: %@"
- "Metrics at end of the session: %@ %@ %@ %f %@ %@ %lu %d %d %d %d %d %lu"
- "Metrics at start of the session: %@ %@ %@ %lu %d, %d, %d, %d, %d, %lu"
- "Peer connection invalidated"
- "Reset the metrics to: %@ %@ %@ %lu %d, %d, %d, %d, %d, %lu"
- "Swift/Array.swift"
- "Swift/ContiguousArrayBuffer.swift"
- "Swift/StringTesting.swift"
- "Swift/StringUTF8View.swift"
- "Swift/UnsafeBufferPointer.swift"
- "Swift/UnsafePointer.swift"
- "Swift/UnsafeRawPointer.swift"
- "Unexpectedly found nil while unwrapping an Optional value"
- "UnsafeMutableBufferPointer with negative count"
- "UnsafeMutablePointer.initialize overlapping range"
- "UnsafeMutablePointer.initialize with negative count"
- "UnsafeMutablePointer.moveInitialize with negative count"
- "UnsafeMutableRawPointer.initializeMemory overlapping range"
- "[%s] %s Remote Alert Deactivated."
- "[%s] %s isRetrigger: %{bool}d."
- "[%s] %s — %s"
- "[%s] Failed to start Live Activity: %@"
- "[%s] Invalidated assertion %@; error %@"
- "[%s] Live Activity is already active"
- "[%s] Received response for notification: %lu"
- "[%s] Started Live Activity %s; assertion %@"
- "[%s] Starting Live Activity"
- "[%s] Stopping Live Activity"
- "[%s] Waiting for response for notification: %lu"
- "invalid Collection: less than 'count' elements in collection"
- "isSelectedAppsEnabled"

```
