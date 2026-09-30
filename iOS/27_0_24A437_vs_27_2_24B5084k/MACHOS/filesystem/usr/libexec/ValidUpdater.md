## ValidUpdater

> `/usr/libexec/ValidUpdater`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_entry`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_types`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`

```diff

-134.0.21.0.0
-  __TEXT.__text: 0x61cc
-  __TEXT.__auth_stubs: 0x900
+134.40.15.0.0
+  __TEXT.__text: 0x6220
+  __TEXT.__auth_stubs: 0x920
   __TEXT.__objc_stubs: 0x180
   __TEXT.__objc_methlist: 0x104
   __TEXT.__const: 0x1d4

   __TEXT.__constg_swiftt: 0x74
   __TEXT.__swift5_fieldmd: 0x2c
   __TEXT.__objc_methtype: 0xdd
-  __TEXT.__oslogstring: 0x200
+  __TEXT.__oslogstring: 0x218
   __TEXT.__cstring: 0x107
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_reflstr: 0x9

   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__auth_got: 0x488
+  __DATA_CONST.__auth_got: 0x498
   __DATA_CONST.__got: 0x100
   __DATA_CONST.__auth_ptr: 0x48
   __DATA.__objc_const: 0x190
   __DATA.__objc_selrefs: 0x100
-  __DATA.__data: 0x1f0
-  __DATA.__common: 0x8
+  __DATA.__data: 0x1e0
+  __DATA.__common: 0x18
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/BackgroundSystemTasks.framework/BackgroundSystemTasks

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 132
-  Symbols:   195
+  Functions: 133
+  Symbols:   197
   CStrings:  75
 
Symbols:
+ _$s11SwiftCRLite22ValidInitialRetryDelaySivg
+ _$s11SwiftCRLite25ValidInitialRetryAttemptsSivg
CStrings:
+ "daemon startup failed with: %{public}@"
+ "validDownload scheduled update: %{public}@"
+ "validDownloadTask completed: %{public}@"
- "daemon startup failed with: %@"
- "validDownload scheduled update: %@"
- "validDownloadTask completed: %@"
```
