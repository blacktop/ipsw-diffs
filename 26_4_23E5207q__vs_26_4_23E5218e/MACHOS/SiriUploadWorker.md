## SiriUploadWorker

> `/System/Library/ExtensionKit/Extensions/SiriUploadWorker.appex/SiriUploadWorker`

```diff

-3520.48.1.0.0
-  __TEXT.__text: 0x42f4
-  __TEXT.__auth_stubs: 0x5f0
+3520.49.1.0.0
+  __TEXT.__text: 0x5328
+  __TEXT.__auth_stubs: 0x6f0
   __TEXT.__objc_stubs: 0x20
-  __TEXT.__const: 0x292
-  __TEXT.__cstring: 0xd4
+  __TEXT.__const: 0x2c8
+  __TEXT.__cstring: 0x19f
   __TEXT.__objc_classname: 0x2a
-  __TEXT.__objc_methname: 0x2e
+  __TEXT.__objc_methname: 0x59
   __TEXT.__objc_methtype: 0x1
   __TEXT.__constg_swiftt: 0x64
-  __TEXT.__swift5_typeref: 0xa8
-  __TEXT.__swift5_reflstr: 0x3f
-  __TEXT.__swift5_fieldmd: 0x50
-  __TEXT.__oslogstring: 0x22f
+  __TEXT.__swift5_typeref: 0xc4
+  __TEXT.__swift5_reflstr: 0x58
+  __TEXT.__swift5_fieldmd: 0x5c
+  __TEXT.__oslogstring: 0x2b3
   __TEXT.__swift5_proto: 0x10
   __TEXT.__swift5_types: 0x8
   __TEXT.__swift_as_entry: 0x34

   __TEXT.__swift5_entry: 0x8
   __TEXT.__swift5_assocty: 0x18
   __TEXT.__unwind_info: 0x1c8
-  __TEXT.__eh_frame: 0x3c0
-  __DATA_CONST.__auth_got: 0x300
-  __DATA_CONST.__got: 0xc0
-  __DATA_CONST.__auth_ptr: 0xe0
+  __TEXT.__eh_frame: 0x3e8
+  __DATA_CONST.__auth_got: 0x380
+  __DATA_CONST.__got: 0x108
+  __DATA_CONST.__auth_ptr: 0xf0
   __DATA_CONST.__const: 0x110
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA.__objc_const: 0xd8
+  __DATA.__objc_const: 0xf8
   __DATA.__objc_selrefs: 0x8
-  __DATA.__data: 0x120
+  __DATA.__data: 0x160
   __DATA.__common: 0x18
   __DATA.__bss: 0x200
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/ExtensionFoundation.framework/ExtensionFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/DataCollector.framework/DataCollector
+  - /System/Library/PrivateFrameworks/Dendrite.framework/Dendrite
   - /System/Library/PrivateFrameworks/IntelligencePlatformLibrary.framework/IntelligencePlatformLibrary
   - /System/Library/PrivateFrameworks/LighthouseBackground.framework/LighthouseBackground
+  - /System/Library/PrivateFrameworks/UnilogCommonLibrary.framework/UnilogCommonLibrary
+  - /System/Library/PrivateFrameworks/UnilogPlatformLibrary.framework/UnilogPlatformLibrary
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: C7AAEF86-57D0-364F-AD5A-36D0D66CEEF7
-  Functions: 109
-  Symbols:   71
-  CStrings:  15
+  UUID: C1D9631E-9BD9-368E-990C-571BD0C4A553
+  Functions: 121
+  Symbols:   72
+  CStrings:  23
 
Symbols:
+ _objc_release_x22
CStrings:
+ "About to upload, bookmark timestamp is: %s"
+ "Event client is %d"
+ "Summary stream event is malformatted- skipping to next event"
+ "UnilogSiri.Telemetry"
+ "apple.unilog.telemetry.HealthAggregatedSummary"
+ "com.apple.aiml.unilog.healthTelemetry"
+ "com.apple.unilog.SiriUploadWorker.dailyTelemetry"
+ "telemetryBookmarkManager"

```
