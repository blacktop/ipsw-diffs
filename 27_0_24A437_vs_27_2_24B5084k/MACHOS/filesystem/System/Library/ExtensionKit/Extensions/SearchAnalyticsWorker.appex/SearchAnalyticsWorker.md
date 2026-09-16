## SearchAnalyticsWorker

> `/System/Library/ExtensionKit/Extensions/SearchAnalyticsWorker.appex/SearchAnalyticsWorker`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_entry`
- `__DATA.__objc_selrefs`

```diff

-3600.56.26.11.2
-  __TEXT.__text: 0x3bdc
-  __TEXT.__auth_stubs: 0x630
+3605.21.1.1.1
+  __TEXT.__text: 0x335c
+  __TEXT.__auth_stubs: 0x590
   __TEXT.__objc_stubs: 0x60
-  __TEXT.__const: 0x210
-  __TEXT.__objc_classname: 0x24
-  __TEXT.__objc_methname: 0x47
-  __TEXT.__objc_methtype: 0x1
-  __TEXT.__constg_swiftt: 0x7c
-  __TEXT.__swift5_typeref: 0xd6
-  __TEXT.__swift5_reflstr: 0x21
-  __TEXT.__swift5_fieldmd: 0x38
-  __TEXT.__swift5_capture: 0x3c
-  __TEXT.__oslogstring: 0x168
-  __TEXT.__swift5_types: 0x8
-  __TEXT.__swift_as_entry: 0x2c
-  __TEXT.__swift_as_ret: 0x2c
-  __TEXT.__swift_as_cont: 0x28
+  __TEXT.__const: 0x2e2
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__swift5_assocty: 0x18
-  __TEXT.__cstring: 0x44
-  __TEXT.__swift5_proto: 0x8
-  __TEXT.__unwind_info: 0x208
-  __TEXT.__eh_frame: 0x3a0
-  __DATA_CONST.__const: 0x138
-  __DATA_CONST.__objc_classlist: 0x8
+  __TEXT.__constg_swiftt: 0x28
+  __TEXT.__swift5_typeref: 0x11e
+  __TEXT.__swift5_fieldmd: 0x10
+  __TEXT.__swift5_reflstr: 0xa3
+  __TEXT.__swift5_assocty: 0x58
+  __TEXT.__oslogstring: 0x128
+  __TEXT.__cstring: 0x64
+  __TEXT.__swift5_proto: 0xc
+  __TEXT.__swift5_types: 0x4
+  __TEXT.__swift_as_entry: 0x50
+  __TEXT.__swift_as_ret: 0x3c
+  __TEXT.__swift_as_cont: 0x20
+  __TEXT.__objc_methname: 0x34
+  __TEXT.__unwind_info: 0x1f0
+  __TEXT.__eh_frame: 0x390
+  __DATA_CONST.__const: 0xc0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__auth_got: 0x320
-  __DATA_CONST.__got: 0x70
-  __DATA_CONST.__auth_ptr: 0xb0
-  __DATA.__objc_const: 0xd8
+  __DATA_CONST.__auth_got: 0x2d0
+  __DATA_CONST.__got: 0x100
+  __DATA_CONST.__auth_ptr: 0x1b0
   __DATA.__objc_selrefs: 0x18
-  __DATA.__data: 0x138
+  __DATA.__data: 0xc8
   __DATA.__common: 0x40
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/ExtensionFoundation.framework/ExtensionFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/LighthouseBackground.framework/LighthouseBackground
   - /System/Library/PrivateFrameworks/PegasusConfiguration.framework/PegasusConfiguration
+  - /System/Library/PrivateFrameworks/PoirotAnalytics.framework/PoirotAnalytics
   - /System/Library/PrivateFrameworks/PoirotBlocks.framework/PoirotBlocks
+  - /System/Library/PrivateFrameworks/PoirotSchematizer.framework/PoirotSchematizer
   - /System/Library/PrivateFrameworks/SearchOnDeviceAnalytics.framework/SearchOnDeviceAnalytics
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 108
-  Symbols:   89
-  CStrings:  18
+  Functions: 113
+  Symbols:   64
+  CStrings:  12
 
Symbols:
+ _objc_release_x24
+ _swift_allocError
+ _swift_willThrow
- _OBJC_CLASS_$__TtCs12_SwiftObject
- _OBJC_METACLASS_$__TtCs12_SwiftObject
- __objc_empty_cache
- __swift_stdlib_bridgeErrorToNSError
- _objc_release_x23
- _objc_release_x26
- _objc_release_x8
- _objc_retain_x21
- _objc_retain_x8
- _swift_beginAccess
- _swift_deallocClassInstance
- _swift_deallocObject
- _swift_deletedMethodError
- _swift_dynamicCast
- _swift_getTypeByMangledNameInContextInMetadataState2
- _swift_release_x19
- _swift_release_x23
- _swift_release_x24
- _swift_release_x25
- _swift_release_x27
- _swift_release_x28
- _swift_release_x8
- _swift_retain_x19
- _swift_retain_x23
- _swift_retain_x24
- _swift_retain_x25
- _swift_retain_x26
- _swift_retain_x27
CStrings:
+ "Failed to subscribe to known recipes: %s"
+ "SAW mainDatabaseConfig: FAILED to load feedback manifest: %s"
+ "SAW mainDatabaseConfig: loaded manifest with %ld messages, %ld enums"
+ "com.apple.poirot"
- "Config found. Task params: %s"
- "No valid config found"
- "On-demand task completed %ld iteration(s): %@"
- "On-demand task is finished: %@"
- "On-demand task is interrupted: %@"
- "On-demand task started: %@"
- "Unexpected error: %@"
- "_TtC21SearchAnalyticsWorker7SAWTask"
- "context"
- "identifier"
```
