## SiriSignals

> `/System/Library/PrivateFrameworks/SiriSignals.framework/SiriSignals`

```diff

-3400.145.2.0.0
-  __TEXT.__text: 0xfcc14
-  __TEXT.__auth_stubs: 0x2100
+3401.2.1.0.0
+  __TEXT.__text: 0xfc68c
+  __TEXT.__auth_stubs: 0x2110
   __TEXT.__objc_methlist: 0xf0
-  __TEXT.__const: 0x6528
-  __TEXT.__cstring: 0x4224
-  __TEXT.__constg_swiftt: 0x34a4
-  __TEXT.__swift5_typeref: 0x26f0
-  __TEXT.__swift5_reflstr: 0x1ba7
-  __TEXT.__swift5_fieldmd: 0x2940
+  __TEXT.__const: 0x65e8
+  __TEXT.__cstring: 0x4344
+  __TEXT.__constg_swiftt: 0x35d0
+  __TEXT.__swift5_typeref: 0x26fc
+  __TEXT.__swift5_reflstr: 0x1c67
+  __TEXT.__swift5_fieldmd: 0x2a00
   __TEXT.__swift5_builtin: 0xc8
   __TEXT.__swift5_assocty: 0x2b0
-  __TEXT.__oslogstring: 0x4967
+  __TEXT.__oslogstring: 0x4ab7
   __TEXT.__swift5_protos: 0xb0
-  __TEXT.__swift5_proto: 0x60c
-  __TEXT.__swift5_types: 0x340
+  __TEXT.__swift5_proto: 0x614
+  __TEXT.__swift5_types: 0x34c
   __TEXT.__swift5_capture: 0x1228
   __TEXT.__swift5_mpenum: 0x38
-  __TEXT.__unwind_info: 0x43c8
-  __TEXT.__eh_frame: 0x36f0
+  __TEXT.__unwind_info: 0x4438
+  __TEXT.__eh_frame: 0x3660
   __TEXT.__objc_classname: 0x49
   __TEXT.__objc_methname: 0x16cd
   __TEXT.__objc_methtype: 0x186
-  __DATA_CONST.__got: 0x5e8
-  __DATA_CONST.__const: 0x150
-  __DATA_CONST.__objc_classlist: 0x198
+  __DATA_CONST.__got: 0x5f8
+  __DATA_CONST.__const: 0x190
+  __DATA_CONST.__objc_classlist: 0x1a8
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x7e0
   __DATA_CONST.__objc_protorefs: 0x38
-  __AUTH_CONST.__auth_got: 0x1080
-  __AUTH_CONST.__auth_ptr: 0xb18
-  __AUTH_CONST.__const: 0xca58
-  __AUTH_CONST.__objc_const: 0x3218
+  __AUTH_CONST.__auth_got: 0x1088
+  __AUTH_CONST.__auth_ptr: 0xab8
+  __AUTH_CONST.__const: 0xca98
+  __AUTH_CONST.__objc_const: 0x3400
   __AUTH.__objc_data: 0x1e0
-  __AUTH.__data: 0x1d50
-  __DATA.__data: 0x12d8
-  __DATA.__bss: 0x4580
-  __DATA.__common: 0x58
+  __AUTH.__data: 0x1cf0
+  __DATA.__data: 0x1268
+  __DATA.__bss: 0x4480
+  __DATA.__common: 0x78
   __DATA_DIRTY.__objc_data: 0x190
-  __DATA_DIRTY.__data: 0x3490
+  __DATA_DIRTY.__data: 0x36f8
   __DATA_DIRTY.__common: 0xe8
-  __DATA_DIRTY.__bss: 0x1700
+  __DATA_DIRTY.__bss: 0x1880
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreML.framework/CoreML
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/swift/libswiftRegexBuilder.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswift_StringProcessing.dylib
+  - /usr/lib/swift/libswift_errno.dylib
+  - /usr/lib/swift/libswift_math.dylib
+  - /usr/lib/swift/libswift_signal.dylib
+  - /usr/lib/swift/libswift_stdio.dylib
+  - /usr/lib/swift/libswift_time.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 7153
-  Symbols:   1630
-  CStrings:  1086
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
+  Functions: 7201
+  Symbols:   1642
+  CStrings:  1102
 
Symbols:
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_math
+ __swift_FORCE_LOAD_$_swift_signal
+ __swift_FORCE_LOAD_$_swift_stdio
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swiftsys_time
+ __swift_FORCE_LOAD_$_swiftunistd
CStrings:
+ "\" ORDER BY eventTimestamp DESC LIMIT "
+ "AudioMegamodelFeatureTransform AudioMegamodelPredictor: (async) signal %!s(MISSING) value %!f(MISSING) is outside of Float16 range: %!f(MISSING)"
+ "ExtractedNowPlaying: incorrect SignalValue"
+ "ExtractedNowPlaying: incorrect event type"
+ "ExtractedNowPlaying: nil bundleID"
+ "NowPlayingSignal: Invalid input"
+ "NowPlayingSignal: updated %!s(MISSING) to %!s(MISSING)"
+ "SELECT sharedUserId, eventTimestamp FROM \""
+ "SignalRepository: %!s(MISSING)"
+ "SignalRepository: Started with %!l(MISSING)d signals, %!s(MISSING)"
+ "Siri.RecognizedUser"
+ "_TtCC11SiriSignals16SignalRepository17ProcessingTimeout"
+ "_TtCC11SiriSignals16SignalRepositoryP33_E1E840CA38E2F29538B8F1258CADFF4218LastRecognizedUser"
+ "idFilter"
+ "lastRecognizedUser"
+ "successes"
+ "timeoutsConsecutive"
+ "timeoutsTotal"
- "SELECT sharedUserId, eventTimestamp FROM \"Siri.RecognizedUser\" ORDER BY eventTimestamp DESC LIMIT "
- "SignalRepository: Started with %!l(MISSING)d signals"
- "SignalRepository: Timed out during processing"

```
