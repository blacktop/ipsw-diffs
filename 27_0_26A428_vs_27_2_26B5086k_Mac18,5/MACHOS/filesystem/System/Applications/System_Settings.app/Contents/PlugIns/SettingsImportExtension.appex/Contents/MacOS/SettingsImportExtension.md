## SettingsImportExtension

> `/System/Applications/System Settings.app/Contents/PlugIns/SettingsImportExtension.appex/Contents/MacOS/SettingsImportExtension`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift5_types`
- `__DATA_CONST.__objc_classlist`
- `__DATA.__objc_const`
- `__DATA.__objc_data`

```diff

-2027.0.10.401.0
-  __TEXT.__text: 0x23cc
-  __TEXT.__auth_stubs: 0x410
-  __TEXT.__objc_stubs: 0x40
+2027.1.4.400.0
+  __TEXT.__text: 0x1100
+  __TEXT.__auth_stubs: 0x290
   __TEXT.__objc_methlist: 0x20
-  __TEXT.__const: 0xba
-  __TEXT.__cstring: 0xf3
+  __TEXT.__const: 0x82
+  __TEXT.__cstring: 0xd8
   __TEXT.__objc_classname: 0x37
-  __TEXT.__objc_methname: 0x6a
+  __TEXT.__objc_methname: 0x52
   __TEXT.__objc_methtype: 0x17
   __TEXT.__constg_swiftt: 0x38
-  __TEXT.__swift5_typeref: 0x7c
+  __TEXT.__swift5_typeref: 0x37
   __TEXT.__swift5_fieldmd: 0x10
-  __TEXT.__swift5_capture: 0x20
-  __TEXT.__oslogstring: 0x130
+  __TEXT.__oslogstring: 0x107
   __TEXT.__swift5_types: 0x4
-  __TEXT.__swift_as_entry: 0x8
-  __TEXT.__swift_as_ret: 0x8
-  __TEXT.__swift_as_cont: 0xc
-  __TEXT.__unwind_info: 0x110
-  __TEXT.__eh_frame: 0x130
-  __DATA_CONST.__const: 0x140
+  __TEXT.__unwind_info: 0xc8
+  __DATA_CONST.__const: 0x70
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__auth_got: 0x210
-  __DATA_CONST.__got: 0x58
-  __DATA_CONST.__auth_ptr: 0x30
+  __DATA_CONST.__auth_got: 0x148
+  __DATA_CONST.__got: 0x28
+  __DATA_CONST.__auth_ptr: 0x20
   __DATA.__objc_const: 0x48
-  __DATA.__objc_selrefs: 0x28
+  __DATA.__objc_selrefs: 0x18
   __DATA.__objc_data: 0xb0
-  __DATA.__data: 0x58
-  __DATA.__common: 0x18
+  __DATA.__data: 0x40
+  __DATA.__common: 0x30
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreSpotlight.framework/Versions/A/CoreSpotlight
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
-  - /System/Library/PrivateFrameworks/SettingsHost.framework/Versions/A/SettingsHost
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftCore.dylib
-  - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
-  - /usr/lib/swift/libswiftCoreImage.dylib
-  - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIOKit.dylib
-  - /usr/lib/swift/libswiftIntents.dylib
-  - /usr/lib/swift/libswiftMetal.dylib
-  - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
-  - /usr/lib/swift/libswiftQuartzCore.dylib
-  - /usr/lib/swift/libswiftSpatial.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 35
-  Symbols:   70
-  CStrings:  21
+  Functions: 25
+  Symbols:   48
+  CStrings:  14
 
Symbols:
+ _notify_post
+ _objc_retain
- _OBJC_CLASS_$_NSProcessInfo
- __swiftEmptySetSingleton
- __swift_FORCE_LOAD_$_swiftAccelerate
- __swift_FORCE_LOAD_$_swiftCoreAudio
- __swift_FORCE_LOAD_$_swiftCoreImage
- __swift_FORCE_LOAD_$_swiftCoreLocation
- __swift_FORCE_LOAD_$_swiftIntents
- __swift_FORCE_LOAD_$_swiftMetal
- __swift_FORCE_LOAD_$_swiftOSLog
- __swift_FORCE_LOAD_$_swiftQuartzCore
- __swift_FORCE_LOAD_$_swiftSpatial
- __swift_FORCE_LOAD_$_swiftsimd
- _objc_msgSend
- _objc_retainAutoreleasedReturnValue
- _swift_deallocObject
- _swift_errorRelease
- _swift_errorRetain
- _swift_getErrorValue
- _swift_getWitnessTable
- _swift_task_alloc
- _swift_task_create
- _swift_task_dealloc
- _swift_task_switch
- _swift_unknownObjectRelease
CStrings:
+ "PendingFullReindexToken"
+ "Wrote reindex token '%{public}s' and posted '%{public}s'. Whether a pass runs is up to systemsettingsagent."
+ "com.apple.Settings.SearchReindexRequest"
+ "com.apple.systemsettings.search.reindexAll"
+ "notify_post('%{public}s') failed with status %{public}u; relying on the durable token."
- "-indexing completed time"
- "-indexing start time"
- "-indexing status"
- "Error Indexing via Intents: '%s'"
- "Indexing for Intents…"
- "Resetting indexing preferences in domain '%{public}s' for process '%{public}s'."
- "Wrote indexing completion state to preferences."
- "com.apple.Settings"
- "com.apple.systempreferences"
- "processInfo"
- "processName"
- "…Indexing Intents completed."
```
