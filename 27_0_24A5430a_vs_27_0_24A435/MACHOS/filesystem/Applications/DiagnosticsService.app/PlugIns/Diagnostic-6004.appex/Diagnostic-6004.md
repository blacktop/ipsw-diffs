## Diagnostic-6004

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-6004.appex/Diagnostic-6004`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__oslogstring`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_proto`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

 1374.2.2.0.0
-  __TEXT.__text: 0x14868
+  __TEXT.__text: 0x149a4
   __TEXT.__auth_stubs: 0xf50
-  __TEXT.__objc_stubs: 0xde0
+  __TEXT.__objc_stubs: 0xe20
   __TEXT.__objc_methlist: 0x504
-  __TEXT.__cstring: 0xa4c
+  __TEXT.__cstring: 0xa5c
   __TEXT.__objc_classname: 0x31e
   __TEXT.__const: 0xb98
   __TEXT.__oslogstring: 0x22e
-  __TEXT.__objc_methname: 0x1310
+  __TEXT.__objc_methname: 0x1330
   __TEXT.__objc_methtype: 0x50b
   __TEXT.__swift5_typeref: 0x14f2
   __TEXT.__constg_swiftt: 0x6fc

   __TEXT.__unwind_info: 0x4b0
   __TEXT.__eh_frame: 0x88
   __DATA_CONST.__const: 0xc38
-  __DATA_CONST.__cfstring: 0x380
+  __DATA_CONST.__cfstring: 0x3a0
   __DATA_CONST.__objc_classlist: 0x60
   __DATA_CONST.__objc_protolist: 0xc8
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__objc_intobj: 0x48
   __DATA_CONST.__auth_got: 0x7b0
-  __DATA_CONST.__got: 0x2c0
+  __DATA_CONST.__got: 0x2c8
   __DATA_CONST.__auth_ptr: 0x2e0
   __DATA.__objc_const: 0xdb0
-  __DATA.__objc_selrefs: 0x500
+  __DATA.__objc_selrefs: 0x510
   __DATA.__objc_ivar: 0xc
   __DATA.__objc_data: 0x7f8
   __DATA.__data: 0x1120

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 478
-  Symbols:   216
-  CStrings:  383
+  Functions: 476
+  Symbols:   217
+  CStrings:  387
 
Symbols:
+ _EXDisplayPipeOpenDisplay
+ _OBJC_CLASS_$_NSMutableArray
- _EXDisplayPipeOpen
CStrings:
+ "Returning %ld stat sets"
+ "Stats found on index %u."
+ "addObject:"
+ "displayIndex"
+ "numberWithUnsignedInt:"
- "Failed to open ExDisplayPipe client for status!"
```
