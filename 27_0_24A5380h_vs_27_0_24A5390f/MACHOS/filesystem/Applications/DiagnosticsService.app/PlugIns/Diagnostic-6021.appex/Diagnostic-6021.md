## Diagnostic-6021

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-6021.appex/Diagnostic-6021`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_reflstr`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__swift5_capture`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`
- `__DATA.__bss`
- `__DATA.__common`

```diff

-1374.0.5.0.0
-  __TEXT.__text: 0x2e0a4
-  __TEXT.__auth_stubs: 0x12b0
-  __TEXT.__objc_stubs: 0x140
+1374.0.27.0.0
+  __TEXT.__text: 0x2e5a8
+  __TEXT.__auth_stubs: 0x12c0
+  __TEXT.__objc_stubs: 0x160
   __TEXT.__objc_methlist: 0x304
   __TEXT.__const: 0x2300
   __TEXT.__objc_classname: 0x25a
-  __TEXT.__objc_methname: 0x79f
+  __TEXT.__objc_methname: 0x78f
   __TEXT.__objc_methtype: 0x40f
   __TEXT.__constg_swiftt: 0x868
   __TEXT.__swift5_typeref: 0x77c

   __TEXT.__swift5_fieldmd: 0x760
   __TEXT.__swift5_assocty: 0x150
   __TEXT.__cstring: 0x711
-  __TEXT.__oslogstring: 0x57b
+  __TEXT.__oslogstring: 0x5bb
   __TEXT.__swift5_proto: 0x158
   __TEXT.__swift5_types: 0xa0
   __TEXT.__swift5_capture: 0x294

   __TEXT.__swift_as_entry: 0x7c
   __TEXT.__swift_as_ret: 0x9c
   __TEXT.__swift_as_cont: 0x148
-  __TEXT.__unwind_info: 0xcc0
+  __TEXT.__unwind_info: 0xcc8
   __TEXT.__eh_frame: 0x24d8
   __DATA_CONST.__const: 0x1388
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0xc0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x60
-  __DATA_CONST.__auth_got: 0x960
+  __DATA_CONST.__auth_got: 0x968
   __DATA_CONST.__got: 0x2b0
   __DATA_CONST.__auth_ptr: 0x808
   __DATA.__objc_const: 0x950

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 981
+  Functions: 982
   Symbols:   168
-  CStrings:  207
+  CStrings:  208
 
CStrings:
+ "Received a broadcast message id %u, replying to everything"
```
