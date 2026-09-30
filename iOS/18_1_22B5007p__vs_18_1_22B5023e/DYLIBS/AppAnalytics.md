## AppAnalytics

> `/System/Library/PrivateFrameworks/AppAnalytics.framework/AppAnalytics`

```diff

-344.0.0.0.0
-  __TEXT.__text: 0xca6ec
-  __TEXT.__auth_stubs: 0x1dd0
+349.0.0.0.0
+  __TEXT.__text: 0xca7b0
+  __TEXT.__auth_stubs: 0x1d80
   __TEXT.__objc_methlist: 0x11ec
-  __TEXT.__const: 0x6670
-  __TEXT.__cstring: 0x6925
-  __TEXT.__constg_swiftt: 0x3614
-  __TEXT.__swift5_typeref: 0x1a1f
-  __TEXT.__swift5_reflstr: 0x1b27
+  __TEXT.__const: 0x66a0
+  __TEXT.__cstring: 0x69c5
+  __TEXT.__constg_swiftt: 0x3634
+  __TEXT.__swift5_typeref: 0x19d3
+  __TEXT.__swift5_reflstr: 0x1b17
   __TEXT.__swift5_fieldmd: 0x2940
   __TEXT.__swift5_builtin: 0x1b8
   __TEXT.__swift5_assocty: 0x2d0
   __TEXT.__swift5_proto: 0x48c
-  __TEXT.__swift5_types: 0x344
-  __TEXT.__swift5_capture: 0x13c4
-  __TEXT.__swift5_protos: 0x90
-  __TEXT.__oslogstring: 0xe3a
+  __TEXT.__swift5_types: 0x348
+  __TEXT.__swift5_capture: 0x13f8
+  __TEXT.__swift5_protos: 0x8c
+  __TEXT.__oslogstring: 0xe4a
   __TEXT.__swift5_mpenum: 0x78
-  __TEXT.__unwind_info: 0x2fb0
-  __TEXT.__eh_frame: 0x2660
+  __TEXT.__unwind_info: 0x3008
+  __TEXT.__eh_frame: 0x2658
   __TEXT.__objc_classname: 0x7b
   __TEXT.__objc_methname: 0x1c9e
   __TEXT.__objc_methtype: 0x4e5
   __TEXT.__objc_stubs: 0xa0
-  __DATA_CONST.__got: 0x498
-  __DATA_CONST.__const: 0x228
-  __DATA_CONST.__objc_classlist: 0x288
+  __DATA_CONST.__got: 0x4a0
+  __DATA_CONST.__const: 0x268
+  __DATA_CONST.__objc_classlist: 0x290
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x90
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x8a0
   __DATA_CONST.__objc_protorefs: 0x68
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0xef0
-  __AUTH_CONST.__auth_ptr: 0x950
-  __AUTH_CONST.__const: 0x6320
+  __AUTH_CONST.__auth_got: 0xec8
+  __AUTH_CONST.__auth_ptr: 0x970
+  __AUTH_CONST.__const: 0x6388
   __AUTH_CONST.__cfstring: 0x140
-  __AUTH_CONST.__objc_const: 0x5a70
-  __AUTH.__objc_data: 0xeb8
-  __AUTH.__data: 0x358
+  __AUTH_CONST.__objc_const: 0x5ae0
+  __AUTH.__objc_data: 0xe68
+  __AUTH.__data: 0x2e8
   __DATA.__objc_ivar: 0x4
-  __DATA.__data: 0xe28
-  __DATA.__bss: 0x5530
-  __DATA.__common: 0x48
-  __DATA_DIRTY.__objc_data: 0x1748
-  __DATA_DIRTY.__data: 0x4630
-  __DATA_DIRTY.__bss: 0x2380
-  __DATA_DIRTY.__common: 0xd0
+  __DATA.__data: 0xd90
+  __DATA.__bss: 0x53b0
+  __DATA.__common: 0x18
+  __DATA_DIRTY.__objc_data: 0x1798
+  __DATA_DIRTY.__data: 0x47e8
+  __DATA_DIRTY.__bss: 0x2500
+  __DATA_DIRTY.__common: 0xf8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/AppleMediaServices.framework/AppleMediaServices

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib
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
-  Functions: 4563
-  Symbols:   477
-  CStrings:  1080
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
+  Functions: 4573
+  Symbols:   480
+  CStrings:  1082
 
Symbols:
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_math
+ __swift_FORCE_LOAD_$_swift_signal
+ __swift_FORCE_LOAD_$_swift_stdio
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swiftsys_time
+ __swift_FORCE_LOAD_$_swiftunistd
- _swift_continuation_await
- _swift_continuation_init
- _swift_unownedRelease
- _swift_unownedRetain
- _swift_unownedRetainStrong
CStrings:
+ "/Library/Caches/com.apple.xbs/Sources/AppAnalytics/AppAnalytics/SummaryEvent/SummaryEventManager.swift"
+ "About to determine if it's time to submit our summary events..."
+ "Checking for possibility of saving summary events now..."
+ "Enough time has elapsed. It's time to submit. timeIntervalSinceLastFlush=%!f(MISSING), timeIntervalBetweenFlushes=%!f(MISSING)"
+ "It's not yet time to persist summary events ... skipping."
+ "It's not yet time to submit. timeIntervalSinceLastFlush=%!f(MISSING), timeIntervalBetweenFlushes=%!f(MISSING)"
+ "Successfully wrote summary events!"
+ "Time threshold reached, generating summary event data ..."
+ "Undetermined summary event time interval, feature like has a .disabled configuration"
+ "We have an override; force returning true for time to submit."
+ "Writing summary events to disk..."
+ "_TtC12AppAnalytics27DisabledSummaryEventManager"
+ "databaseManager"
+ "firstRecordedDate"
+ "lastSubmittedDate"
+ "lazyClient"
- "$__lazy_storage_$_lazyClient"
- "About to determine if it's time to flush our summary events..."
- "Checking for possibility of a flush now..."
- "Enough time has elapsed. It's time to flush. timeIntervalSinceLastFlush=%!f(MISSING), timeInvervalBetweenFlushes=%!f(MISSING)"
- "It's not yet time to flush ... skipping."
- "It's not yet time to flush. timeIntervalSinceLastFlush=%!f(MISSING), timeInvervalBetweenFlushes=%!f(MISSING)"
- "Now flushing our local database to clear the events that were just uploaded..."
- "Okay to flush, so generating summary event data for uploading ..."
- "Successfully flushed!"
- "We don't have a object for submitting events, so we cannot flush ... skipping."
- "We have an override; force returning true for time to flush."
- "dataseManager"
- "firstRecorded"
- "lastFlushed"

```
