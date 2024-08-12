## FitnessAwards

> `/System/Library/PrivateFrameworks/FitnessAwards.framework/FitnessAwards`

```diff

-980.0.0.0.0
-  __TEXT.__text: 0x9c9dc
+993.0.0.0.0
+  __TEXT.__text: 0x9328c
   __TEXT.__auth_stubs: 0x14a0
-  __TEXT.__const: 0xc108
-  __TEXT.__cstring: 0xdab
-  __TEXT.__constg_swiftt: 0x2054
-  __TEXT.__swift5_typeref: 0x3db5
-  __TEXT.__swift5_builtin: 0xf0
-  __TEXT.__swift5_reflstr: 0x1785
-  __TEXT.__swift5_fieldmd: 0x24c4
-  __TEXT.__swift5_types: 0x370
-  __TEXT.__swift5_proto: 0xbd0
-  __TEXT.__swift5_capture: 0x494
+  __TEXT.__const: 0xb518
+  __TEXT.__cstring: 0xd0b
+  __TEXT.__constg_swiftt: 0x1ea0
+  __TEXT.__swift5_typeref: 0x3b5f
+  __TEXT.__swift5_builtin: 0xc8
+  __TEXT.__swift5_reflstr: 0x165a
+  __TEXT.__swift5_fieldmd: 0x22cc
+  __TEXT.__swift5_types: 0x340
+  __TEXT.__swift5_proto: 0xb14
+  __TEXT.__swift5_capture: 0x438
   __TEXT.__swift5_assocty: 0x258
-  __TEXT.__oslogstring: 0x169b
-  __TEXT.__swift5_mpenum: 0x70
-  __TEXT.__unwind_info: 0x2cb8
-  __TEXT.__eh_frame: 0x3598
+  __TEXT.__oslogstring: 0x1242
+  __TEXT.__swift5_mpenum: 0x50
+  __TEXT.__unwind_info: 0x2af8
+  __TEXT.__eh_frame: 0x3408
   __TEXT.__objc_methname: 0x36
-  __DATA_CONST.__got: 0x4c8
-  __DATA_CONST.__const: 0x110
+  __DATA_CONST.__got: 0x4e0
+  __DATA_CONST.__const: 0x150
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x18
   __AUTH_CONST.__auth_got: 0xa50
-  __AUTH_CONST.__auth_ptr: 0x880
-  __AUTH_CONST.__const: 0x5dc0
+  __AUTH_CONST.__auth_ptr: 0x888
+  __AUTH_CONST.__const: 0x58b8
   __AUTH_CONST.__objc_const: 0x90
-  __AUTH.__data: 0xc48
-  __DATA.__data: 0x2860
-  __DATA.__bss: 0x17b60
+  __AUTH.__data: 0xbb8
+  __DATA.__data: 0x2650
+  __DATA.__bss: 0x163c0
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/SwiftUI.framework/SwiftUI
   - /System/Library/PrivateFrameworks/DataFlow.framework/DataFlow
   - /System/Library/PrivateFrameworks/FitnessCanvasUI.framework/FitnessCanvasUI
+  - /System/Library/PrivateFrameworks/FitnessUtilities.framework/FitnessUtilities
   - /System/Library/PrivateFrameworks/SeymourCore.framework/SeymourCore
   - /System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore
   - /usr/lib/libSystem.B.dylib

   - /usr/lib/swift/libswiftSpatial.dylib
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
-  Functions: 3883
-  Symbols:   161
-  CStrings:  178
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
+  Functions: 3723
+  Symbols:   164
+  CStrings:  160
 
Symbols:
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_math
+ __swift_FORCE_LOAD_$_swift_signal
+ __swift_FORCE_LOAD_$_swift_stdio
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swiftsys_time
+ __swift_FORCE_LOAD_$_swiftunistd
- _objc_release_x21
- _objc_release_x8
- _objc_retain_x19
- _objc_retain_x21
- _objc_retain_x25
- _objc_retain_x26
CStrings:
+ "Awards eligible to present %!s(MISSING)"
+ "Earnable awards %!s(MISSING)"
+ "Toast eligibility query for %!s(MISSING) failed with error %!s(MISSING)"
+ "[AwardHeaderFeature] Resolving award description state on viewAppeared for %!s(MISSING)"
+ "[AwardToastPresentationFeature] Award candidates: %!s(MISSING)"
+ "[AwardToastPresentationFeature] Fetching candidates"
+ "fetchCandidateIdentifiers"
+ "suggestedWorkoutsLoadStates"
- "Query for award toast eligibility of %!s(MISSING) failed with error %!s(MISSING)"
- "[AchievementEnvironmentCacheMonitor] Clearing previous description load states %!s(MISSING)"
- "[AwardHeaderFeature] (%!s(MISSING)) Setting load state %!s(MISSING)"
- "[AwardHeaderFeature] Description fetch failed for %!s(MISSING), error %!s(MISSING)"
- "[AwardHeaderFeature] Sending .awardDescriptionFetched(%!s(MISSING) action for %!s(MISSING)"
- "[AwardHeaderFeature] Sending .fetchAwardDescription(%!s(MISSING)) action on state reset"
- "[AwardHeaderFeature] Sending .fetchAwardDescription(%!s(MISSING)) action on view appeared"
- "[AwardHeaderFeature] View appeared for award %!s(MISSING) but load state was %!s(MISSING), returning"
- "[AwardHeaderView] Load state was reset to idle for  %!s(MISSING)"
- "[AwardLockupFeature] (%!s(MISSING)) Description fetched: %!s(MISSING)"
- "[AwardLockupFeature] Current state is %!s(MISSING), skipping .fetched update"
- "[AwardLockupFeature] Failed to fetch description for %!s(MISSING), error %!s(MISSING)"
- "[AwardLockupFeature] Sending .descriptionFetched(%!s(MISSING) action for %!s(MISSING)"
- "[AwardLockupFeature] Sending .fetchDescription(%!s(MISSING)) action for viewAppeared"
- "[AwardLockupFeature] View appeared for award %!s(MISSING) but load state was %!s(MISSING), returning"
- "[AwardLockupView] Load state was reset to idle for  %!s(MISSING)"
- "[AwardToastPresentationFeature] Awards eligible to present %!s(MISSING)"
- "[AwardToastPresentationFeature] Earnable awards %!s(MISSING)"
- "[RemoteBrowsingIdentityUpdatedMonitor] Clearing previous description load states %!s(MISSING)"
- "awardDescriptionFetched"
- "descriptionFetchFailed"
- "descriptionFetched"
- "descriptionLoadState"
- "descriptionLoadStates"
- "fetchAwardDescription"
- "fetchDescription"

```
