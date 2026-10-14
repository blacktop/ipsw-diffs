## Diagnostic-9008

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-9008.appex/Diagnostic-9008`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`

```diff

-1307.40.64.0.0
-  __TEXT.__text: 0xb834
+1307.40.66.0.0
+  __TEXT.__text: 0xb888
   __TEXT.__auth_stubs: 0x840
   __TEXT.__objc_stubs: 0x1ec0
   __TEXT.__objc_methlist: 0x8d8

   __TEXT.__swift5_fieldmd: 0x78
   __TEXT.__swift5_proto: 0x28
   __TEXT.__swift5_types: 0xc
-  __TEXT.__unwind_info: 0x448
+  __TEXT.__unwind_info: 0x450
   __TEXT.__eh_frame: 0x74
   __DATA_CONST.__const: 0x4f0
   __DATA_CONST.__cfstring: 0x7a0

   __DATA_CONST.__objc_arraydata: 0x70
   __DATA_CONST.__objc_arrayobj: 0x90
   __DATA_CONST.__auth_got: 0x430
-  __DATA_CONST.__got: 0x1e0
+  __DATA_CONST.__got: 0x1e8
   __DATA_CONST.__auth_ptr: 0x1d8
   __DATA.__objc_const: 0xdf0
   __DATA.__objc_selrefs: 0xa18
   __DATA.__objc_ivar: 0x70
   __DATA.__objc_data: 0x230
-  __DATA.__data: 0x400
+  __DATA.__data: 0x408
   __DATA.__common: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 301
+  Functions: 302
   Symbols:   193
   CStrings:  661
 
Functions:
~ sub_10000b864 : 140 -> 84
+ sub_10000b8b8
```
