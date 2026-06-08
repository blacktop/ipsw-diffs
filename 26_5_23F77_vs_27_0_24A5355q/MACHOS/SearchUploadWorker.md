## SearchUploadWorker

> `/System/Library/ExtensionKit/Extensions/SearchUploadWorker.appex/SearchUploadWorker`

```diff

-3525.2.2.0.0
-  __TEXT.__text: 0x45f8
-  __TEXT.__auth_stubs: 0x700
+3600.13.1.0.0
+  __TEXT.__text: 0x804c
+  __TEXT.__auth_stubs: 0xa50
   __TEXT.__objc_stubs: 0x20
-  __TEXT.__const: 0x3a8
-  __TEXT.__cstring: 0x1cb
-  __TEXT.__constg_swiftt: 0x9c
-  __TEXT.__swift5_typeref: 0xf3
-  __TEXT.__swift5_reflstr: 0x7e
-  __TEXT.__swift5_fieldmd: 0xa0
+  __TEXT.__const: 0x458
+  __TEXT.__constg_swiftt: 0xb8
+  __TEXT.__swift5_typeref: 0x144
+  __TEXT.__swift5_reflstr: 0xcc
+  __TEXT.__swift5_fieldmd: 0xe0
   __TEXT.__swift5_assocty: 0x30
-  __TEXT.__swift5_proto: 0x1c
-  __TEXT.__swift5_types: 0x10
+  __TEXT.__cstring: 0xd1
+  __TEXT.__swift5_proto: 0x20
+  __TEXT.__swift5_types: 0x14
   __TEXT.__objc_classname: 0x2e
   __TEXT.__objc_methname: 0x3d
   __TEXT.__objc_methtype: 0x1
-  __TEXT.__oslogstring: 0x374
-  __TEXT.__swift_as_entry: 0x34
-  __TEXT.__swift_as_ret: 0x20
+  __TEXT.__oslogstring: 0x482
+  __TEXT.__swift_as_entry: 0x38
+  __TEXT.__swift_as_ret: 0x3c
+  __TEXT.__swift_as_cont: 0x44
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__unwind_info: 0x1b0
-  __TEXT.__eh_frame: 0x240
-  __DATA_CONST.__auth_got: 0x388
-  __DATA_CONST.__got: 0xd0
-  __DATA_CONST.__auth_ptr: 0x140
-  __DATA_CONST.__const: 0x2e8
+  __TEXT.__unwind_info: 0x270
+  __TEXT.__eh_frame: 0x590
+  __DATA_CONST.__const: 0x250
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__auth_got: 0x530
+  __DATA_CONST.__got: 0x180
+  __DATA_CONST.__auth_ptr: 0x190
   __DATA.__objc_const: 0xd8
   __DATA.__objc_selrefs: 0x8
-  __DATA.__data: 0x148
+  __DATA.__data: 0x190
   __DATA.__common: 0x20
-  __DATA.__bss: 0x380
+  __DATA.__bss: 0x400
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/ExtensionFoundation.framework/ExtensionFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/DataCollector.framework/DataCollector
+  - /System/Library/PrivateFrameworks/Dendrite.framework/Dendrite
   - /System/Library/PrivateFrameworks/LighthouseBackground.framework/LighthouseBackground
   - /System/Library/PrivateFrameworks/UnilogCommonLibrary.framework/UnilogCommonLibrary
+  - /System/Library/PrivateFrameworks/UnilogConfig.framework/UnilogConfig
   - /System/Library/PrivateFrameworks/UnilogPlatformLibrary.framework/UnilogPlatformLibrary
   - /System/Library/PrivateFrameworks/UnilogTelemetry.framework/UnilogTelemetry
   - /usr/lib/libSystem.B.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: CAD0E272-A71A-37F8-AA22-442473CAD21D
-  Functions: 125
-  Symbols:   78
-  CStrings:  27
+  UUID: B6955620-99F0-3339-9556-8556114CC9D3
+  Functions: 178
+  Symbols:   89
+  CStrings:  28
 
Symbols:
+ _objc_retain_x23
+ _swift_getEnumCaseMultiPayload
+ _swift_getErrorValue
+ _swift_release_x19
+ _swift_release_x21
+ _swift_release_x22
+ _swift_release_x23
+ _swift_release_x24
+ _swift_release_x25
+ _swift_release_x26
+ _swift_release_x8
+ _swift_retain_x19
+ _swift_retain_x21
+ _swift_retain_x24
+ _swift_storeEnumTagMultiPayload
+ _swift_willThrow
- _objc_release_x22
- _objc_release_x23
- _objc_retain_x21
- _swift_bridgeObjectRelease_n
- _swift_retain_n
CStrings:
+ "Exit due to context not available: %@"
+ "Extension Exited On: (%@), didAdvance:%{bool}d"
+ "Failed to build context: %@"
+ "Failed to get LastMileRedactionConfig: %s"
+ "Failed to get UploaderConfig: %s"
+ "Fatal error"
+ "Running task type: %s with stream %s"
+ "SearchUploadWorker/UnilogLastMileRedactor.swift"
+ "Successfully retrieved LastMileRedactionConfig version: %s"
+ "Successfully retrieved UploaderConfig version: %s"
+ "Unknown SchemaRedactionConfig case encountered: "
+ "telemetry"
- "Exit due to context not available"
- "Exit due to no upload queue set for tenant - %s on current platform"
- "UnilogMailSearchProcessed"
- "UnilogUploaderSessionStart"
- "apple.trace.Session"
- "com.apple.unilog.SearchUploadWorker.mail.daily"
- "com.apple.unilog.SearchUploadWorker.mail.hourly"
- "https://carry-chickadee.smoot.apple.com"
- "https://chickadee.smoot.apple.com"
- "https://dev-chickadee.smoot.apple.com"
- "https://seed-chickadee.smoot.apple.com"

```
