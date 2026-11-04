## PebblePlayDaemon

> `/System/Library/PrivateFrameworks/PebblePlayDaemon.framework/PebblePlayDaemon`

```diff

-164.2.4.0.0
-  __TEXT.__text: 0x2ee4c
-  __TEXT.__objc_methlist: 0x7cc
-  __TEXT.__const: 0xf18
+178.0.0.0.0
+  __TEXT.__text: 0x30ee0
+  __TEXT.__objc_methlist: 0x82c
+  __TEXT.__const: 0xf48
   __TEXT.__constg_swiftt: 0x628
-  __TEXT.__swift5_typeref: 0xb32
-  __TEXT.__swift5_reflstr: 0x680
-  __TEXT.__swift5_fieldmd: 0x60c
+  __TEXT.__swift5_typeref: 0xbcc
+  __TEXT.__swift5_reflstr: 0x6b0
+  __TEXT.__swift5_fieldmd: 0x630
   __TEXT.__swift5_assocty: 0x60
-  __TEXT.__oslogstring: 0xda7
-  __TEXT.__cstring: 0xe75
-  __TEXT.__swift5_capture: 0x3e8
+  __TEXT.__oslogstring: 0xe87
+  __TEXT.__cstring: 0x10a5
+  __TEXT.__swift5_capture: 0x41c
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_proto: 0x50
   __TEXT.__swift5_types: 0x48
   __TEXT.__swift_as_entry: 0xf0
-  __TEXT.__swift_as_ret: 0xcc
-  __TEXT.__swift_as_cont: 0x174
+  __TEXT.__swift_as_ret: 0xc4
+  __TEXT.__swift_as_cont: 0x170
   __TEXT.__swift5_protos: 0x1c
-  __TEXT.__unwind_info: 0xc48
-  __TEXT.__eh_frame: 0x1cdc
+  __TEXT.__unwind_info: 0xc58
+  __TEXT.__eh_frame: 0x1c14
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xb8
+  __DATA_CONST.__const: 0xc8
   __DATA_CONST.__objc_classlist: 0x60
   __DATA_CONST.__objc_protolist: 0xd8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6c8
+  __DATA_CONST.__objc_selrefs: 0x6e8
   __DATA_CONST.__objc_protorefs: 0x70
   __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__const: 0xd58
-  __AUTH_CONST.__objc_const: 0x1450
-  __AUTH_CONST.__auth_got: 0xb80
+  __AUTH_CONST.__const: 0xe18
+  __AUTH_CONST.__objc_const: 0x14d0
+  __AUTH_CONST.__auth_got: 0xbb0
   __AUTH.__objc_data: 0x3d0
-  __AUTH.__data: 0x8c8
-  __DATA.__data: 0xbd8
+  __AUTH.__data: 0x8d8
+  __DATA.__data: 0xc48
   __DATA.__common: 0x10
   - /System/Library/Frameworks/CarPlay.framework/CarPlay
   - /System/Library/Frameworks/Combine.framework/Combine

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
+  - /usr/lib/swift/libswiftAVFoundation.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftCarPlay.dylib
   - /usr/lib/swift/libswiftCompression.dylib

   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
+  - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMLCompute.dylib

   - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 673
-  Symbols:   612
-  CStrings:  152
+  Functions: 683
+  Symbols:   628
+  CStrings:  167
 
Symbols:
+ _FBSActivateForEventOptionTypeBackgroundContentFetching
+ _FBSOpenApplicationOptionKeyActivateForEvent
+ ___swift_closure_destructor.88Tm
+ __swift_FORCE_LOAD_$_swiftAVFoundation
+ __swift_FORCE_LOAD_$_swiftAVFoundation_$_PebblePlayDaemon
+ __swift_FORCE_LOAD_$_swiftCoreMIDI
+ __swift_FORCE_LOAD_$_swiftCoreMIDI_$_PebblePlayDaemon
+ _symbolic SDySSSDySSypGG
+ _symbolic SS_SDySSypGt
+ _symbolic _____ 14PebblePlayCore13AppExitReasonO
+ _symbolic _____XMT 16PebblePlayDaemon18ApplicationLibraryC
+ _symbolic _____ySSSgG 2os21OSAllocatedUnfairLockV
+ _symbolic _____ySSSg_____G s13ManagedBufferCsRi__rlE So16os_unfair_lock_sV
+ _symbolic _____ySS_SDySSypGtG s23_ContiguousArrayStorageC
+ _symbolic _____ySbG 2os21OSAllocatedUnfairLockV
+ _symbolic _____ySb_____G s13ManagedBufferCsRi__rlE So16os_unfair_lock_sV
+ _symbolic _____y_____G 2os21OSAllocatedUnfairLockV 14PebblePlayCore13SessionMetricC0H17TerminationReasonO
+ _symbolic _____y__________G s13ManagedBufferCsRi__rlE 14PebblePlayCore13SessionMetricC0F17TerminationReasonO So16os_unfair_lock_sV
- _FBSOpenApplicationOptionKeyActivateSuspended
- ___swift_closure_destructor.77Tm
CStrings:
+ " - target will fall back to legacy placeholder (no entitlements)"
+ ") requested but no active session/provider to notify"
+ "CarPlay connected — ending session (Ended due to CarPlay connecting)"
+ "Current route left built-in but no conversational app connected — ignoring"
+ "Failed to send appExited ("
+ "No serialized placeholder data for "
+ "Remote device control not allowed — ending session"
+ "ai.perplexity.app"
+ "appExited (%s) ignored — session exit already in progress"
+ "com.apple.internal."
+ "com.apple.internal.CarDJ"
+ "com.apple.internal.CarLandmarks"
+ "fetchApplicationInfo(bundleIDs:details:features:)"
+ "remoteDeviceControlDisallowed()"
+ "sendAppExitedAndInvalidate(reason:)"
```
