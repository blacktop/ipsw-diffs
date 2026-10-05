## Diagnostic-6009

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-6009.appex/Diagnostic-6009`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift_as_ret`
- `__DATA_CONST.__const`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-369.1.0.0.0
-  __TEXT.__text: 0x1ea90
+370.0.0.0.0
+  __TEXT.__text: 0x1eb18
   __TEXT.__auth_stubs: 0x1470
   __TEXT.__objc_stubs: 0x520
   __TEXT.__objc_methlist: 0x2e4

   __TEXT.__swift_as_ret: 0x8
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x920
-  __TEXT.__eh_frame: 0x6f4
+  __TEXT.__unwind_info: 0x928
+  __TEXT.__eh_frame: 0x724
   __DATA_CONST.__const: 0x1550
   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_protolist: 0x30

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 689
+  Functions: 690
   Symbols:   193
   CStrings:  246
 
Functions:
~ sub_100009ca0 : 352 -> 380
- sub_10000b4d8
+ sub_10000b55c
+ sub_10000ba4c
```
