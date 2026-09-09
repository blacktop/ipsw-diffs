## Diagnostic-8389

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8389.appex/Diagnostic-8389`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
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
-  __TEXT.__text: 0x1deb0
+  __TEXT.__text: 0x1dffc
   __TEXT.__auth_stubs: 0xf80
-  __TEXT.__objc_stubs: 0xb20
+  __TEXT.__objc_stubs: 0xb60
   __TEXT.__objc_methlist: 0x5d4
   __TEXT.__const: 0x36e0
-  __TEXT.__cstring: 0x11bd
-  __TEXT.__oslogstring: 0x18f
+  __TEXT.__cstring: 0x11cd
+  __TEXT.__oslogstring: 0x190
   __TEXT.__objc_classname: 0x1f4
-  __TEXT.__objc_methname: 0x15fd
+  __TEXT.__objc_methname: 0x161d
   __TEXT.__objc_methtype: 0x86b
   __TEXT.__constg_swiftt: 0xda0
   __TEXT.__swift5_typeref: 0xbd9

   __TEXT.__unwind_info: 0x8e8
   __TEXT.__eh_frame: 0x7b0
   __DATA_CONST.__const: 0x2128
-  __DATA_CONST.__cfstring: 0x360
+  __DATA_CONST.__cfstring: 0x380
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_protolist: 0xf0
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__objc_intobj: 0x48
   __DATA_CONST.__auth_got: 0x7c8
-  __DATA_CONST.__got: 0x230
+  __DATA_CONST.__got: 0x238
   __DATA_CONST.__auth_ptr: 0x198
   __DATA.__objc_const: 0xbf0
-  __DATA.__objc_selrefs: 0x4f0
+  __DATA.__objc_selrefs: 0x500
   __DATA.__objc_ivar: 0xc
   __DATA.__objc_data: 0x7e8
   __DATA.__data: 0x11f0

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 857
-  Symbols:   197
-  CStrings:  447
+  Functions: 855
+  Symbols:   198
+  CStrings:  451
 
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
