## MediaControl

> `/System/Library/PrivateFrameworks/MediaControl.framework/MediaControl`

```diff

-4024.100.95.0.0
-  __TEXT.__text: 0x58954
-  __TEXT.__auth_stubs: 0x10d0
+4024.200.3.0.0
+  __TEXT.__text: 0x5b230
+  __TEXT.__auth_stubs: 0x10e0
   __TEXT.__objc_methlist: 0x2c
-  __TEXT.__const: 0xa704
-  __TEXT.__cstring: 0xf21
-  __TEXT.__oslogstring: 0x815
-  __TEXT.__swift5_typeref: 0x14f7
+  __TEXT.__const: 0xaca4
+  __TEXT.__cstring: 0xfa1
+  __TEXT.__oslogstring: 0x955
+  __TEXT.__swift5_typeref: 0x1583
   __TEXT.__swift5_capture: 0x1d4
-  __TEXT.__constg_swiftt: 0x1ee4
-  __TEXT.__swift5_reflstr: 0x99a
-  __TEXT.__swift5_fieldmd: 0x1d30
+  __TEXT.__constg_swiftt: 0x210c
+  __TEXT.__swift5_reflstr: 0xa5a
+  __TEXT.__swift5_fieldmd: 0x1e5c
   __TEXT.__swift5_builtin: 0xc8
-  __TEXT.__swift5_proto: 0xbc8
-  __TEXT.__swift5_types: 0x2e0
+  __TEXT.__swift5_proto: 0xc28
+  __TEXT.__swift5_types: 0x2f8
   __TEXT.__swift5_assocty: 0xa8
   __TEXT.__swift5_mpenum: 0x54
   __TEXT.__swift5_protos: 0x14
-  __TEXT.__unwind_info: 0x2490
-  __TEXT.__eh_frame: 0x1bb0
+  __TEXT.__unwind_info: 0x2570
+  __TEXT.__eh_frame: 0x1bcc
   __TEXT.__objc_methname: 0x332
-  __DATA_CONST.__got: 0x2e0
-  __DATA_CONST.__const: 0xd8
+  __DATA_CONST.__got: 0x2f8
+  __DATA_CONST.__const: 0x138
   __DATA_CONST.__objc_classlist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x148
-  __AUTH_CONST.__auth_got: 0x868
+  __AUTH_CONST.__auth_got: 0x870
   __AUTH_CONST.__auth_ptr: 0x330
-  __AUTH_CONST.__const: 0x5948
-  __AUTH_CONST.__objc_const: 0x8c0
+  __AUTH_CONST.__const: 0x5c90
+  __AUTH_CONST.__objc_const: 0x940
   __AUTH.__objc_data: 0xb0
-  __AUTH.__data: 0x968
-  __DATA.__data: 0x1d88
+  __AUTH.__data: 0xa88
+  __DATA.__data: 0x1de0
   __DATA.__common: 0x68
-  __DATA.__bss: 0x17680
-  __DATA_DIRTY.__data: 0x8
-  __DATA_DIRTY.__bss: 0x80
+  __DATA.__bss: 0x17b80
+  __DATA_DIRTY.__data: 0xa0
+  __DATA_DIRTY.__bss: 0x780
   - /System/Library/Frameworks/ActivityKit.framework/ActivityKit
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
-  Functions: 3889
-  Symbols:   742
-  CStrings:  195
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
+  Functions: 4037
+  Symbols:   767
+  CStrings:  205
 
Symbols:
+ __swiftEmptySetSingleton
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_math
+ __swift_FORCE_LOAD_$_swift_signal
+ __swift_FORCE_LOAD_$_swift_stdio
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swiftsys_time
+ __swift_FORCE_LOAD_$_swiftunistd
+ _objc_retain_x28
+ _os_unfair_lock_assert_owner
- _swift_continuation_await
- _swift_continuation_init
CStrings:
+ ".setExpandedSessionIdentifiers"
+ "[%!s(MISSING)] Error setting UI presented to: %!{(MISSING)bool}d"
+ "[%!s(MISSING)] Error setting expanded sessions to: %!s(MISSING)"
+ "[%!s(MISSING)] Error setting routing mode to: %!s(MISSING)"
+ "[%!s(MISSING)] loadForToken<%!s(MISSING)> - No data artwork in item: %!s(MISSING)"
+ "[%!s(MISSING)] loadForToken<%!s(MISSING)> - formatting error: %!@(MISSING)"
+ "[%!s(MISSING)] loadForToken<%!s(MISSING)> - no remote artwork in item: %!s(MISSING)"
+ "[%!s(MISSING)] loadForToken<%!s(MISSING)> - received data artwork"
+ "[%!s(MISSING)] loadForToken<%!s(MISSING)> - received remote artwork representation"
+ "[%!s(MISSING)] loadForToken<%!s(MISSING)> - request data artwork"
+ "[%!s(MISSING)] loadForToken<%!s(MISSING)> - request remote artwork"
+ "[%!s(MISSING)] loadForToken<%!s(MISSING)> - token: %!s(MISSING)"
+ "[%!s(MISSING)] loadImageData - finished with error: %!@(MISSING)"
+ "[%!s(MISSING)] loadRemoteArtwork<%!s(MISSING)> - Store artwork catalog failed with error: %!@(MISSING) for token: %!s(MISSING)"
+ "[%!s(MISSING)] loadRemoteArtwork<%!s(MISSING)> - could not retrieve source data from image"
+ "[%!s(MISSING)] loadRemoteArtwork<%!s(MISSING)> - formatting error: %!@(MISSING)"
+ "[%!s(MISSING)] loadRemoteArtwork<%!s(MISSING)> - received image from catalog"
+ "[%!s(MISSING)] loadRemoteArtwork<%!s(MISSING)> - request image from catalog: %!@(MISSING)"
+ "[%!s(MISSING)] updateToken - error: %!@(MISSING) loading image data for token: %!s(MISSING)"
+ "[%!s(MISSING)]<%!s(MISSING)> deinit"
+ "[%!s(MISSING)]<%!s(MISSING)> init"
+ "[%!s(MISSING)]<%!s(MISSING)> updateToken - load image data for token: %!s(MISSING)"
+ "_expandedSessionIdentifiers"
+ "_isPresentingUI"
+ "_routingMode"
+ "_snapshot"
+ "alwaysWantsLocalSession"
+ "expandedSessionIdentifiers"
+ "setExpandedSessionIdentifiers"
- "%!s(MISSING) loadImageData finished with error: %!@(MISSING)"
- "[%!s(MISSING)] Error setting routing mode to %!s(MISSING)"
- "[%!s(MISSING)] Load<%!s(MISSING)> No data artwork in item: %!s(MISSING)"
- "[%!s(MISSING)] Load<%!s(MISSING)> could not retrieve source data from image"
- "[%!s(MISSING)] Load<%!s(MISSING)> for token: %!s(MISSING)"
- "[%!s(MISSING)] Load<%!s(MISSING)> formatting error: %!@(MISSING)"
- "[%!s(MISSING)] Load<%!s(MISSING)> no remote artwork in item: %!s(MISSING)"
- "[%!s(MISSING)] Load<%!s(MISSING)> received data artwork"
- "[%!s(MISSING)] Load<%!s(MISSING)> received image from catalog"
- "[%!s(MISSING)] Load<%!s(MISSING)> received remote artwork representation"
- "[%!s(MISSING)] Load<%!s(MISSING)> request data artwork"
- "[%!s(MISSING)] Load<%!s(MISSING)> request image from catalog: %!@(MISSING)"
- "[%!s(MISSING)] Load<%!s(MISSING)> request remote artwork"
- "[%!s(MISSING)] Store artwork catalog failed with error: %!@(MISSING) for token: %!s(MISSING)"
- "[%!s(MISSING)] TODO willTransitionFrom: %!s(MISSING), to: %!s(MISSING)"
- "[%!s(MISSING)] error: %!@(MISSING) loading token: %!s(MISSING)"
- "[%!s(MISSING)] loading token: %!s(MISSING)"
- "cayenne_optimistic_engine"
- "routingMode"

```
