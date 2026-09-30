## AppManagedFeaturesDemoExtension

> `/System/Library/ExtensionKit/Extensions/AppManagedFeaturesDemoExtension.appex/AppManagedFeaturesDemoExtension`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_entry`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`

```diff

-46.0.7.0.0
-  __TEXT.__text: 0x1514
-  __TEXT.__auth_stubs: 0x2d0
-  __TEXT.__const: 0x11a
+46.0.15.0.0
+  __TEXT.__text: 0x3bb4
+  __TEXT.__auth_stubs: 0x4f0
+  __TEXT.__objc_stubs: 0xc0
+  __TEXT.__const: 0x1aa
   __TEXT.__swift5_entry: 0x8
   __TEXT.__constg_swiftt: 0x34
-  __TEXT.__swift5_typeref: 0x69
+  __TEXT.__swift5_typeref: 0x9f
   __TEXT.__swift5_reflstr: 0x15
   __TEXT.__swift5_fieldmd: 0x1c
   __TEXT.__swift5_assocty: 0x18
-  __TEXT.__cstring: 0x90
-  __TEXT.__oslogstring: 0x7e
+  __TEXT.__cstring: 0x130
+  __TEXT.__oslogstring: 0x1ae
+  __TEXT.__swift5_capture: 0x30
   __TEXT.__swift5_proto: 0x8
   __TEXT.__swift5_types: 0x4
-  __TEXT.__swift_as_entry: 0x18
-  __TEXT.__swift_as_ret: 0xc
-  __TEXT.__swift_as_cont: 0xc
-  __TEXT.__unwind_info: 0xe8
-  __TEXT.__eh_frame: 0xf8
-  __DATA_CONST.__const: 0x90
+  __TEXT.__swift_as_entry: 0x30
+  __TEXT.__swift_as_ret: 0x28
+  __TEXT.__swift_as_cont: 0x38
+  __TEXT.__objc_methname: 0x6e
+  __TEXT.__unwind_info: 0x1b0
+  __TEXT.__eh_frame: 0x388
+  __DATA_CONST.__const: 0xe0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__auth_got: 0x168
-  __DATA_CONST.__got: 0x20
-  __DATA_CONST.__auth_ptr: 0x78
-  __DATA.__data: 0xa0
+  __DATA_CONST.__auth_got: 0x280
+  __DATA_CONST.__got: 0x68
+  __DATA_CONST.__auth_ptr: 0x90
+  __DATA.__objc_selrefs: 0x30
+  __DATA.__data: 0xb8
   __DATA.__bss: 0x110
   - /System/Library/Frameworks/AppManagedFeatures.framework/AppManagedFeatures
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 37
-  Symbols:   58
-  CStrings:  6
+  Functions: 73
+  Symbols:   79
+  CStrings:  23
 
Symbols:
+ _OBJC_CLASS_$_NSJSONSerialization
+ _OBJC_CLASS_$_NSURLSession
+ _OBJC_CLASS_$_NSUserDefaults
+ ___chkstk_darwin
+ ___stack_chk_fail
+ ___stack_chk_guard
+ __swift_stdlib_bridgeErrorToNSError
+ _objc_msgSend
+ _objc_opt_self
+ _objc_release
+ _objc_release_x25
+ _objc_release_x26
+ _objc_retain_x8
+ _swift_deallocObject
+ _swift_errorRelease
+ _swift_errorRetain
+ _swift_release_x8
+ _swift_retain
+ _swift_task_create
+ _swift_unknownObjectRelease
+ _swift_willThrow
CStrings:
+ "Invalid workload URL: %{public}s"
+ "JSONObjectWithData:options:error:"
+ "Network request failed (round=%ld, task=%ld): %{public}@"
+ "Network workload complete: totalBytesDownloaded=%{public}ld"
+ "Network workload starting: url=%{public}s, iterations=%ld, concurrency=%ld"
+ "NetworkWorkloadConcurrency"
+ "NetworkWorkloadEnabled"
+ "NetworkWorkloadIterations"
+ "NetworkWorkloadURL"
+ "Workload round %ld/%ld"
+ "boolForKey:"
+ "hash sentinel"
+ "https://apple.com"
+ "integerForKey:"
+ "sharedSession"
+ "standardUserDefaults"
+ "stringForKey:"
```
