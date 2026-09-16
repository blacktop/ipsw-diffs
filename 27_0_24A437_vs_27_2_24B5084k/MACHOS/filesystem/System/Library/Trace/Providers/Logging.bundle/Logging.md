## Logging

> `/System/Library/Trace/Providers/Logging.bundle/Logging`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__swift5_capture`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__swift5_protos`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_data`

```diff

-206.0.0.0.0
-  __TEXT.__text: 0xaa00
-  __TEXT.__auth_stubs: 0xa80
-  __TEXT.__objc_stubs: 0x320
+210.0.0.0.0
+  __TEXT.__text: 0xad40
+  __TEXT.__auth_stubs: 0xad0
+  __TEXT.__objc_stubs: 0x380
   __TEXT.__objc_methlist: 0x618
-  __TEXT.__const: 0x95e
-  __TEXT.__cstring: 0x1c75
-  __TEXT.__swift5_typeref: 0x338
+  __TEXT.__const: 0x94e
+  __TEXT.__gcc_except_tab: 0x30
+  __TEXT.__cstring: 0x1cb5
+  __TEXT.__swift5_typeref: 0x34e
   __TEXT.__swift5_capture: 0x88
   __TEXT.__objc_methtype: 0x42b
-  __TEXT.__objc_methname: 0x61c
+  __TEXT.__objc_methname: 0x64c
   __TEXT.__constg_swiftt: 0x394
   __TEXT.__swift5_builtin: 0x28
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__swift5_reflstr: 0x2b0
-  __TEXT.__swift5_fieldmd: 0x2fc
+  __TEXT.__swift5_reflstr: 0x2d0
+  __TEXT.__swift5_fieldmd: 0x308
   __TEXT.__objc_classname: 0x25b
   __TEXT.__swift5_assocty: 0xc0
   __TEXT.__swift5_proto: 0x64
   __TEXT.__swift5_types: 0x40
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0x518
-  __TEXT.__eh_frame: 0x190
+  __TEXT.__unwind_info: 0x540
+  __TEXT.__eh_frame: 0x188
   __DATA_CONST.__const: 0x5c0
   __DATA_CONST.__objc_classlist: 0x60
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x20
-  __DATA_CONST.__auth_got: 0x548
-  __DATA_CONST.__got: 0xd8
+  __DATA_CONST.__auth_got: 0x578
+  __DATA_CONST.__got: 0xe0
   __DATA_CONST.__auth_ptr: 0x1d8
   __DATA.__objc_const: 0x9b0
-  __DATA.__objc_selrefs: 0x188
+  __DATA.__objc_selrefs: 0x1a0
   __DATA.__objc_data: 0x950
-  __DATA.__data: 0x4e8
+  __DATA.__data: 0x4e0
   __DATA.__common: 0x8
+  - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/LoggingSupport.framework/LoggingSupport
   - /System/Library/PrivateFrameworks/SignpostSupport.framework/SignpostSupport

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 388
-  Symbols:   129
-  CStrings:  209
+  Functions: 389
+  Symbols:   138
+  CStrings:  214
 
Symbols:
+ _ATSPredicateFromFormatString
+ _OBJC_EHTYPE_$_NSException
+ __Unwind_Resume
+ ___objc_personality_v0
+ _objc_begin_catch
+ _objc_claimAutoreleasedReturnValue
+ _objc_end_catch
+ _objc_retainAutorelease
+ _swift_release_x23
CStrings:
+ ". Logging will be disabled."
+ "Invalid predicate '"
+ "description"
+ "predicateWithFormat:"
+ "reason"
```
