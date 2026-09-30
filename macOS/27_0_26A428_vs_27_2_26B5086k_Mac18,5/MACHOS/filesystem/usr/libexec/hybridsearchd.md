## hybridsearchd

> `/usr/libexec/hybridsearchd`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_entry`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_selrefs`

```diff

-67.0.0.0.0
-  __TEXT.__text: 0x3580
-  __TEXT.__auth_stubs: 0x610
+73.2.0.0.0
+  __TEXT.__text: 0x3b7c
+  __TEXT.__auth_stubs: 0x630
   __TEXT.__objc_stubs: 0x20
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__const: 0x152
+  __TEXT.__const: 0x17a
   __TEXT.__constg_swiftt: 0x28
-  __TEXT.__swift5_typeref: 0xa6
+  __TEXT.__swift5_typeref: 0xb6
   __TEXT.__swift5_fieldmd: 0x10
   __TEXT.__cstring: 0x98
-  __TEXT.__swift5_capture: 0xec
-  __TEXT.__oslogstring: 0x81
+  __TEXT.__swift5_capture: 0x120
+  __TEXT.__oslogstring: 0xf1
   __TEXT.__objc_methtype: 0x6
   __TEXT.__swift5_proto: 0x4
   __TEXT.__swift5_types: 0x4
-  __TEXT.__swift_as_entry: 0x14
-  __TEXT.__swift_as_ret: 0x10
-  __TEXT.__swift_as_cont: 0x1c
+  __TEXT.__swift_as_entry: 0x18
+  __TEXT.__swift_as_ret: 0x14
+  __TEXT.__swift_as_cont: 0x20
   __TEXT.__objc_methname: 0x21
-  __TEXT.__unwind_info: 0x1b8
-  __TEXT.__eh_frame: 0x240
-  __DATA_CONST.__const: 0x2e0
+  __TEXT.__unwind_info: 0x1e0
+  __TEXT.__eh_frame: 0x2c0
+  __DATA_CONST.__const: 0x358
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__auth_got: 0x310
-  __DATA_CONST.__got: 0xb0
+  __DATA_CONST.__auth_got: 0x320
+  __DATA_CONST.__got: 0x98
   __DATA_CONST.__auth_ptr: 0x70
   __DATA.__objc_selrefs: 0x8
-  __DATA.__data: 0x78
+  __DATA.__data: 0x70
   __DATA.__common: 0x8
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/PrivateFrameworks/HybridSearch.framework/Versions/A/HybridSearch

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 105
-  Symbols:   53
-  CStrings:  10
+  Functions: 115
+  Symbols:   58
+  CStrings:  12
 
Symbols:
+ __swift_stdlib_bridgeErrorToNSError
+ _geteuid
+ _swift_errorRetain
+ _swift_task_immediate
+ _swift_task_isCurrentExecutorWithFlags
CStrings:
+ "XPCDistributed server failed: %@"
+ "hybridsearchd does not run as the macOS setup user; exiting"
```
