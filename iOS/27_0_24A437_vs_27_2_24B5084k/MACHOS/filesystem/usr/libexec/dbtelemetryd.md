## dbtelemetryd

> `/usr/libexec/dbtelemetryd`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_entry`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_capture`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_selrefs`

```diff

-6.0.0.0.0
-  __TEXT.__text: 0x5f04
-  __TEXT.__auth_stubs: 0xa10
+7.0.0.0.0
+  __TEXT.__text: 0x6594
+  __TEXT.__auth_stubs: 0xa30
   __TEXT.__objc_stubs: 0x2e0
-  __TEXT.__const: 0x2f2
+  __TEXT.__const: 0x302
   __TEXT.__swift5_entry: 0x8
   __TEXT.__swift5_typeref: 0x1cc
   __TEXT.__constg_swiftt: 0x84
   __TEXT.__swift5_reflstr: 0x33
   __TEXT.__swift5_fieldmd: 0x6c
-  __TEXT.__cstring: 0x167
+  __TEXT.__cstring: 0x1d1
   __TEXT.__objc_methtype: 0x38
   __TEXT.__swift5_capture: 0x3c
   __TEXT.__oslogstring: 0x1dd

   __TEXT.__eh_frame: 0x130
   __DATA_CONST.__const: 0x288
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__auth_got: 0x510
+  __DATA_CONST.__auth_got: 0x520
   __DATA_CONST.__got: 0x160
   __DATA_CONST.__auth_ptr: 0x170
   __DATA.__objc_selrefs: 0xb8
-  __DATA.__data: 0x200
+  __DATA.__data: 0x210
   __DATA.__common: 0x18
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 115
-  Symbols:   263
-  CStrings:  47
+  Functions: 116
+  Symbols:   265
+  CStrings:  49
 
Symbols:
+ _objc_retain
+ _os_variant_has_internal_content
CStrings:
+ "com.apple.libsqlite3.firstparty.sqltelemetry.sqlerrors.fullinternal"
+ "com.apple.sqlite"
```
