## AssetMetrics

> `/System/Library/ExtensionKit/Extensions/AssetMetrics.appex/Contents/MacOS/AssetMetrics`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_entry`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift5_protos`

```diff

-3600.6.1.0.0
-  __TEXT.__text: 0x3868
-  __TEXT.__auth_stubs: 0x530
-  __TEXT.__const: 0x3ca
+3605.12.1.0.0
+  __TEXT.__text: 0x4bf4
+  __TEXT.__auth_stubs: 0x700
+  __TEXT.__objc_stubs: 0xa0
+  __TEXT.__const: 0x52a
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__swift5_typeref: 0x142
-  __TEXT.__constg_swiftt: 0xd0
-  __TEXT.__swift5_reflstr: 0x68
-  __TEXT.__swift5_fieldmd: 0xb0
-  __TEXT.__swift5_assocty: 0x18
-  __TEXT.__cstring: 0xa2
-  __TEXT.__swift5_capture: 0x2c
-  __TEXT.__oslogstring: 0xea
-  __TEXT.__swift5_proto: 0x2c
-  __TEXT.__swift5_types: 0x10
+  __TEXT.__objc_classname: 0x7e
+  __TEXT.__objc_methname: 0x53
+  __TEXT.__objc_methtype: 0xa
+  __TEXT.__constg_swiftt: 0x130
+  __TEXT.__swift5_typeref: 0x1a0
+  __TEXT.__swift5_reflstr: 0xa6
+  __TEXT.__swift5_fieldmd: 0xf4
+  __TEXT.__swift5_assocty: 0x30
+  __TEXT.__cstring: 0xfd
+  __TEXT.__swift5_capture: 0x4c
+  __TEXT.__oslogstring: 0x205
+  __TEXT.__swift5_proto: 0x40
+  __TEXT.__swift5_types: 0x18
   __TEXT.__swift_as_entry: 0x20
-  __TEXT.__swift_as_ret: 0x1c
-  __TEXT.__swift_as_cont: 0x18
-  __TEXT.__objc_classname: 0x2e
+  __TEXT.__swift_as_ret: 0x20
+  __TEXT.__swift_as_cont: 0x20
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0x230
-  __TEXT.__eh_frame: 0x298
-  __DATA_CONST.__const: 0x258
-  __DATA_CONST.__objc_classlist: 0x8
+  __TEXT.__unwind_info: 0x2d0
+  __TEXT.__eh_frame: 0x378
+  __DATA_CONST.__const: 0x370
+  __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__auth_got: 0x298
-  __DATA_CONST.__got: 0x70
-  __DATA_CONST.__auth_ptr: 0x190
-  __DATA.__objc_const: 0x90
-  __DATA.__data: 0x1d8
+  __DATA_CONST.__auth_got: 0x388
+  __DATA_CONST.__got: 0xa0
+  __DATA_CONST.__auth_ptr: 0x1e8
+  __DATA.__objc_const: 0x168
+  __DATA.__objc_selrefs: 0x28
+  __DATA.__data: 0x2a8
   - /System/Library/Frameworks/ExtensionFoundation.framework/Versions/A/ExtensionFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/PrivateFrameworks/AssetMetricsCoreV2.framework/Versions/A/AssetMetricsCoreV2
+  - /System/Library/PrivateFrameworks/AssistantServices.framework/Versions/A/AssistantServices
   - /System/Library/PrivateFrameworks/DeepThought.framework/Versions/A/DeepThought
   - /System/Library/PrivateFrameworks/DeepThoughtBiomeFoundation.framework/Versions/A/DeepThoughtBiomeFoundation
   - /System/Library/PrivateFrameworks/LighthouseBackground.framework/Versions/A/LighthouseBackground

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 126
-  Symbols:   83
-  CStrings:  13
+  Functions: 180
+  Symbols:   95
+  CStrings:  27
 
Symbols:
+ _AFIsHorseman
+ _OBJC_CLASS_$_NSLock
+ _OBJC_CLASS_$_NSProcessInfo
+ __Block_copy
+ __Block_release
+ __NSConcreteStackBlock
+ __swift_stdlib_bridgeErrorToNSError
+ _dispatch_semaphore_create
+ _objc_msgSend
+ _objc_retainAutoreleasedReturnValue
+ _swift_allocBox
+ _swift_retain
CStrings:
+ "#AssetMetricsEntry: RunningBoard is expiring the AssetMetrics activity"
+ "AssetMetrics AND Assistant/dictation are enabled. Continuing."
+ "Hourly task running on HomePod. Not continuing for resource reasons."
+ "Siri Assistant or Dictation disabled. Not continuing."
+ "_TtC12AssetMetricsP33_CFE025F5F3C0D62108C1EA1F858D47D911RunOnceGate"
+ "claimed"
+ "com.apple.siri.AssetMetrics metrics run"
+ "dependenciesUnavailableError"
+ "init"
+ "lock"
+ "performExpiringActivityWithReason:usingBlock:"
+ "processInfo"
+ "unexpected error throws: %@"
+ "unlock"
+ "v12@?0B8"
- "AssetMetrics are disabled"
```
