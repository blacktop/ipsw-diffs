## GenerativeFunctionsInstrumentation

> `/System/Library/PrivateFrameworks/GenerativeFunctionsInstrumentation.framework/Versions/A/GenerativeFunctionsInstrumentation`

```diff

-119.0.0.0.0
-  __TEXT.__text: 0x5ec88
-  __TEXT.__auth_stubs: 0x2200
-  __TEXT.__objc_methlist: 0x9c
-  __TEXT.__const: 0x2350
-  __TEXT.__cstring: 0x3508
-  __TEXT.__swift5_typeref: 0xf56
-  __TEXT.__oslogstring: 0x1cdc
-  __TEXT.__constg_swiftt: 0xf3c
-  __TEXT.__swift5_reflstr: 0x1403
-  __TEXT.__swift5_fieldmd: 0xf1c
-  __TEXT.__swift5_builtin: 0x3c
-  __TEXT.__swift5_proto: 0x1ac
+128.100.0.0.0
+  __TEXT.__text: 0x616d0
+  __TEXT.__auth_stubs: 0x2490
+  __TEXT.__objc_methlist: 0x64
+  __TEXT.__const: 0x23f8
+  __TEXT.__cstring: 0x3528
+  __TEXT.__swift5_typeref: 0xf3a
+  __TEXT.__oslogstring: 0x1f01
+  __TEXT.__constg_swiftt: 0xf30
+  __TEXT.__swift5_reflstr: 0x1422
+  __TEXT.__swift5_fieldmd: 0xf6c
+  __TEXT.__swift5_builtin: 0x14
+  __TEXT.__swift5_proto: 0x1b8
   __TEXT.__swift5_types: 0xd4
-  __TEXT.__swift5_capture: 0x140
+  __TEXT.__swift5_capture: 0x100
   __TEXT.__swift5_protos: 0x20
   __TEXT.__swift5_assocty: 0x1a8
-  __TEXT.__unwind_info: 0x1500
-  __TEXT.__eh_frame: 0x25c8
+  __TEXT.__unwind_info: 0x1588
+  __TEXT.__eh_frame: 0x2628
   __TEXT.__objc_classname: 0x1f
-  __TEXT.__objc_methname: 0x409
+  __TEXT.__objc_methname: 0x30a
   __TEXT.__objc_methtype: 0x2e
   __TEXT.__objc_stubs: 0x20
-  __DATA_CONST.__got: 0x7e0
-  __DATA_CONST.__const: 0x60
+  __DATA_CONST.__got: 0x850
+  __DATA_CONST.__const: 0x88
   __DATA_CONST.__objc_classlist: 0xa8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x180
+  __DATA_CONST.__objc_selrefs: 0x110
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x1108
-  __AUTH_CONST.__auth_ptr: 0x600
-  __AUTH_CONST.__const: 0xdf8
-  __AUTH_CONST.__objc_const: 0x1d38
+  __AUTH_CONST.__auth_got: 0x1250
+  __AUTH_CONST.__auth_ptr: 0x620
+  __AUTH_CONST.__const: 0xe90
+  __AUTH_CONST.__objc_const: 0x1c98
   __AUTH.__objc_data: 0x1e0
-  __AUTH.__data: 0x1a08
+  __AUTH.__data: 0x19e8
   __DATA.__objc_ivar: 0x10
-  __DATA.__data: 0xd28
-  __DATA.__bss: 0x2d90
-  __DATA.__common: 0x388
+  __DATA.__data: 0xdc8
+  __DATA.__bss: 0x2f10
+  __DATA.__common: 0x3a0
   - /System/Library/Frameworks/Combine.framework/Versions/A/Combine
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CryptoKit.framework/Versions/A/CryptoKit
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/Frameworks/Security.framework/Versions/A/Security
-  - /System/Library/PrivateFrameworks/BiomeLibrary.framework/Versions/A/BiomeLibrary
   - /System/Library/PrivateFrameworks/BiomeStreams.framework/Versions/A/BiomeStreams
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/Versions/A/CoreAnalytics
   - /System/Library/PrivateFrameworks/GenerativeFunctionsFoundation.framework/Versions/A/GenerativeFunctionsFoundation
   - /System/Library/PrivateFrameworks/IntelligencePlatformLibrary.framework/Versions/A/IntelligencePlatformLibrary
   - /System/Library/PrivateFrameworks/InternalSwiftProtobuf.framework/Versions/A/InternalSwiftProtobuf
+  - /System/Library/PrivateFrameworks/ModelManagerServices.framework/Versions/A/ModelManagerServices
   - /System/Library/PrivateFrameworks/PowerLog.framework/Versions/A/PowerLog
   - /System/Library/PrivateFrameworks/ProactiveEventTracker.framework/Versions/A/ProactiveEventTracker
   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/Versions/A/RunningBoardServices

   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIOKit.dylib
+  - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
+  - /usr/lib/swift/libswiftQuartzCore.dylib
   - /usr/lib/swift/libswiftRegexBuilder.dylib
+  - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 2110
-  Symbols:   147
-  CStrings:  392
+  Functions: 2161
+  Symbols:   142
+  CStrings:  387
 
Symbols:
+ _OBJC_CLASS_$_NSOutputStream
+ __swift_FORCE_LOAD_$_swiftMetal
+ __swift_FORCE_LOAD_$_swiftQuartzCore
+ __swift_FORCE_LOAD_$_swiftUniformTypeIdentifiers
- _BiomeLibrary
- _CFPreferencesCopyValue
- _CFPreferencesSetValue
- _OBJC_CLASS_$_NSJSONSerialization
- _getpwuid
- _kCFPreferencesCurrentHost
- _kCFPreferencesCurrentUser
- _objc_autorelease
- _swift_isEscapingClosureAtFileLocation
CStrings:
+ ",\n\"privateCloudComputeRequests\": ["
+ "AppleIntelligenceReportExport"
+ "Failed to create UserDefaults for TransparencyReport"
+ "GenerativeFunctionsInstrumentation/TransparencyReportUserDefaults.swift"
+ "_TtC34GenerativeFunctionsInstrumentation18TransparencyReport"
+ "attachmentsLength"
+ "cli"
+ "com.apple.AppleIntelligenceReport"
+ "inputHasAttachment"
+ "inputHasUnsupportedEmoji"
+ "other"
+ "recipientsLength"
+ "report-settings-changed"
+ "testing"
+ "{\n\"modelRequests\": ["
- "\n\"modelRequests\": ["
- "\n\"privateCloudComputeRequests\": ["
- "$__lazy_storage_$_requestLogSource"
- "$__lazy_storage_$_transparencyLogSource"
- "$__lazy_storage_$_userName"
- "@24@0:8^@16"
- "B16@0:8"
- "B24@?0@8^B16"
- "B32@0:8q16^@24"
- "TB,N"
- "TransparencyLogging"
- "_TtC34GenerativeFunctionsInstrumentation15TransparencyLog"
- "com.apple.tokengeneration"
- "enabled"
- "settings.TransparencyLogReport"
- "transparency-logging-disabled"
- "user"
- "v16@?0@\"BPSCompletion\"8"
- "v16@?0@8"
- "v20@0:8B16"

```
