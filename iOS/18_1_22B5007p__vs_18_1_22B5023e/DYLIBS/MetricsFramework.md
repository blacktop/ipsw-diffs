## MetricsFramework

> `/System/Library/PrivateFrameworks/MetricsFramework.framework/MetricsFramework`

```diff

-3400.46.4.0.0
-  __TEXT.__text: 0x8742c
-  __TEXT.__auth_stubs: 0x1530
-  __TEXT.__const: 0x5020
-  __TEXT.__cstring: 0x319e
-  __TEXT.__constg_swiftt: 0x25ac
-  __TEXT.__swift5_typeref: 0x15ac
+3401.5.1.0.0
+  __TEXT.__text: 0x87030
+  __TEXT.__auth_stubs: 0x14e0
+  __TEXT.__const: 0x5070
+  __TEXT.__cstring: 0x31d1
+  __TEXT.__constg_swiftt: 0x2610
+  __TEXT.__swift5_typeref: 0x15e8
   __TEXT.__swift5_builtin: 0xdc
-  __TEXT.__swift5_reflstr: 0x1ff9
+  __TEXT.__swift5_reflstr: 0x201c
   __TEXT.__swift5_assocty: 0x5b0
-  __TEXT.__swift5_proto: 0x3a8
+  __TEXT.__swift5_proto: 0x3ac
   __TEXT.__swift5_types: 0x228
-  __TEXT.__swift5_fieldmd: 0x2094
-  __TEXT.__oslogstring: 0x1c4a
-  __TEXT.__swift5_capture: 0x2bc
-  __TEXT.__swift5_protos: 0x20
+  __TEXT.__swift5_fieldmd: 0x20d4
+  __TEXT.__oslogstring: 0x1bfa
+  __TEXT.__swift5_capture: 0x2cc
+  __TEXT.__swift5_protos: 0x24
   __TEXT.__unwind_info: 0x1e48
   __TEXT.__eh_frame: 0x3620
-  __TEXT.__objc_methname: 0x15c0
+  __TEXT.__objc_methname: 0x1640
   __TEXT.__objc_stubs: 0x20
   __DATA_CONST.__got: 0x4a0
-  __DATA_CONST.__const: 0x158
+  __DATA_CONST.__const: 0x1a0
   __DATA_CONST.__objc_classlist: 0x190
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5b0
-  __AUTH_CONST.__auth_got: 0xaa0
-  __AUTH_CONST.__auth_ptr: 0x6e8
-  __AUTH_CONST.__const: 0x3708
+  __DATA_CONST.__objc_selrefs: 0x5c0
+  __AUTH_CONST.__auth_got: 0xa78
+  __AUTH_CONST.__auth_ptr: 0x6f0
+  __AUTH_CONST.__const: 0x3750
   __AUTH_CONST.__cfstring: 0x1b00
-  __AUTH_CONST.__objc_const: 0x26d8
+  __AUTH_CONST.__objc_const: 0x26f8
   __AUTH.__objc_data: 0xaf0
-  __AUTH.__data: 0x31f0
-  __DATA.__data: 0x1a38
+  __AUTH.__data: 0x3220
+  __DATA.__data: 0x1a40
   __DATA.__bss: 0x7180
   __DATA.__common: 0x28
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
-  - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/PrivateFrameworks/AssistantServices.framework/AssistantServices
   - /System/Library/PrivateFrameworks/BiomeLibrary.framework/BiomeLibrary
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics

   - /System/Library/PrivateFrameworks/Trial.framework/Trial
   - /System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore
   - /System/Library/PrivateFrameworks/lighthouse_runtime.framework/lighthouse_runtime
-  - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAVFoundation.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
+  - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib

   - /usr/lib/swift/libswiftSpatial.dylib
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
-  Functions: 2344
-  Symbols:   276
-  CStrings:  840
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
+  Functions: 2347
+  Symbols:   281
+  CStrings:  843
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftCompression
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_math
+ __swift_FORCE_LOAD_$_swift_signal
+ __swift_FORCE_LOAD_$_swift_stdio
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swiftsys_time
+ __swift_FORCE_LOAD_$_swiftunistd
- _IOPSCopyPowerSourcesInfo
- _IOPSGetProvidingPowerSourceType
- _MobileGestalt_get_current_device
- _MobileGestalt_get_iPadCapability
CStrings:
+ "asrMode"
+ "initWithEventMetadata:deviceType:programCode:productId:systemBuild:dataSharingOptInStatus:viewInterface:audioInterfaceVendorId:audioInterfaceProductId:asrLocation:nlLocation:siriInputLocale:dictationLocale:subDomain:totalTurnCount:validTurnCount:siriTasksStarted:siriTasksCompleted:flowTasksStarted:flowTasksCompleted:reliabilityRequestCount:reliabilityTurnCount:clientErrorCount:undesiredResponseCount:fatalResponseCount:failureResponseCount:siriUnavailableResponseCount:asrTurnCount:siriResponseId:responseCategory:isIntelligenceEngineRequest:intelligenceEngineRouting:"
+ "isIntelligenceEngineRequest"
+ "is_assistant_engine_request"
+ "nlMode"
+ "setDaysWithTwoValidAssistantTurnsPerWeek:"
+ "setIsIntelligenceEngineRequest:"
- "Power source: %!s(MISSING)"
- "Unable to retrieve current power source"
- "initWithEventMetadata:deviceType:programCode:productId:systemBuild:dataSharingOptInStatus:viewInterface:audioInterfaceVendorId:audioInterfaceProductId:asrLocation:nlLocation:siriInputLocale:dictationLocale:subDomain:totalTurnCount:validTurnCount:siriTasksStarted:siriTasksCompleted:flowTasksStarted:flowTasksCompleted:reliabilityRequestCount:reliabilityTurnCount:clientErrorCount:undesiredResponseCount:fatalResponseCount:failureResponseCount:siriUnavailableResponseCount:asrTurnCount:siriResponseId:responseCategory:"
- "uodMode"

```
