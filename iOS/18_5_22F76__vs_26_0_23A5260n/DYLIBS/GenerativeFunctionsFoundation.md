## GenerativeFunctionsFoundation

> `/System/Library/PrivateFrameworks/GenerativeFunctionsFoundation.framework/GenerativeFunctionsFoundation`

```diff

-154.762.0.0.0
-  __TEXT.__text: 0x71a70
-  __TEXT.__auth_stubs: 0x10d0
-  __TEXT.__cstring: 0x2114
-  __TEXT.__swift5_typeref: 0x387c
-  __TEXT.__swift5_fieldmd: 0x3284
-  __TEXT.__const: 0x110d0
-  __TEXT.__constg_swiftt: 0x2e74
-  __TEXT.__swift5_builtin: 0xf0
-  __TEXT.__swift5_reflstr: 0x11b5
+198.1.102.0.0
+  __TEXT.__text: 0x83fe4
+  __TEXT.__auth_stubs: 0x11c0
+  __TEXT.__cstring: 0x249d
+  __TEXT.__const: 0x14c74
+  __TEXT.__swift5_typeref: 0x4348
+  __TEXT.__constg_swiftt: 0x3694
+  __TEXT.__swift5_reflstr: 0x141b
+  __TEXT.__swift5_fieldmd: 0x3bb0
+  __TEXT.__swift5_builtin: 0x118
   __TEXT.__swift5_assocty: 0x210
+  __TEXT.__swift5_proto: 0x1400
+  __TEXT.__swift5_types: 0x58c
   __TEXT.__swift5_protos: 0x90
-  __TEXT.__swift5_proto: 0x101c
-  __TEXT.__swift5_types: 0x494
-  __TEXT.__swift5_capture: 0x730
-  __TEXT.__oslogstring: 0x245
-  __TEXT.__swift5_mpenum: 0x84
   __TEXT.__swift_as_entry: 0x10
   __TEXT.__swift_as_ret: 0x10
-  __TEXT.__unwind_info: 0x3178
-  __TEXT.__eh_frame: 0x3598
+  __TEXT.__swift5_capture: 0x760
+  __TEXT.__swift5_mpenum: 0x94
+  __TEXT.__oslogstring: 0x25f
+  __TEXT.__unwind_info: 0x36a8
+  __TEXT.__eh_frame: 0x3c98
   __TEXT.__objc_methname: 0x80
-  __DATA_CONST.__got: 0x260
-  __DATA_CONST.__const: 0xb8
+  __DATA_CONST.__got: 0x318
+  __DATA_CONST.__const: 0xa0
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x38
-  __AUTH_CONST.__auth_got: 0x868
-  __AUTH_CONST.__const: 0x8e00
+  __AUTH_CONST.__auth_got: 0x8e0
+  __AUTH_CONST.__const: 0xa840
   __AUTH_CONST.__objc_const: 0x118
-  __AUTH.__data: 0x2e8
-  __DATA.__data: 0x2950
-  __DATA.__bss: 0x1ff00
-  __DATA.__common: 0x48
-  __DATA_DIRTY.__data: 0xe90
+  __AUTH.__data: 0x348
+  __DATA.__data: 0x3198
+  __DATA.__bss: 0x27b80
+  __DATA.__common: 0x30
+  __DATA_DIRTY.__data: 0xee8
   __DATA_DIRTY.__bss: 0x80
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/PrivateFrameworks/AppleIntelligenceReporting.framework/AppleIntelligenceReporting
   - /System/Library/PrivateFrameworks/FeatureFlags.framework/FeatureFlags
   - /System/Library/PrivateFrameworks/PromptKit.framework/PromptKit
   - /usr/lib/libSystem.B.dylib

   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
+  - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
-  - /usr/lib/swift/libswift_errno.dylib
-  - /usr/lib/swift/libswift_math.dylib
-  - /usr/lib/swift/libswift_signal.dylib
-  - /usr/lib/swift/libswift_stdio.dylib
-  - /usr/lib/swift/libswift_time.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
+  - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
-  - /usr/lib/swift/libswiftsys_time.dylib
-  - /usr/lib/swift/libswiftunistd.dylib
-  UUID: E2561CA4-90F2-3265-81BE-3145B293A87B
-  Functions: 5364
-  Symbols:   126
-  CStrings:  211
+  UUID: 2F2ED715-3126-3422-8233-C484C0DD8E1E
+  Functions: 6285
+  Symbols:   124
+  CStrings:  228
 
Symbols:
+ _OBJC_CLASS_$_NSNull
+ __swiftEmptySetSingleton
+ __swift_FORCE_LOAD_$_swiftMetal
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3
+ _swift_coroFrameAlloc
+ _swift_dynamicCastClass
- __swift_FORCE_LOAD_$_swift_errno
- __swift_FORCE_LOAD_$_swift_math
- __swift_FORCE_LOAD_$_swift_signal
- __swift_FORCE_LOAD_$_swift_stdio
- __swift_FORCE_LOAD_$_swift_time
- __swift_FORCE_LOAD_$_swiftsys_time
- __swift_FORCE_LOAD_$_swiftunistd
- _objc_release_x25
- _objc_release_x26
- _swift_release_n
CStrings:
+ "A generation guide with an unsupported pattern was used."
+ "An error explaining that the developer has used a generation guide with an unsupported pattern."
+ "An error explaining that the failure happened because finalize operation was called before the streaming operation began."
+ "An error explaining that the model produced malformed output."
+ "Cannot call finalize operation before streaming the output first."
+ "GenerativeConfigurationKey.Instrumentation.userRequestIdentifier"
+ "MoveSafetyToInferenceProvider"
+ "Underlying model produced malformed output with the failure: "
+ "VMHostAvailability"
+ "allowsMultipleBoundValues"
+ "definitionOverride"
+ "expandableOptions"
+ "fileGenerationTool"
+ "finalizeOperation"
+ "illegalOperation"
+ "imageGenerationTool"
+ "osEligibility unable to be accessed. Status code: %d"
+ "unsupportedGuide"
- "Invoking tool: %s with arguments: %s"

```
