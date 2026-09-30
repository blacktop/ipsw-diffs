## ANEStorageMaintainer

> `/System/Library/PrivateFrameworks/AppleNeuralEngine.framework/XPCServices/ANEStorageMaintainer.xpc/ANEStorageMaintainer`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-382.100.2.0.0
-  __TEXT.__text: 0x8308
-  __TEXT.__auth_stubs: 0x580
+382.101.0.0.0
+  __TEXT.__text: 0x85dc
+  __TEXT.__auth_stubs: 0x590
   __TEXT.__objc_stubs: 0xfa0
   __TEXT.__objc_methlist: 0x3dc
-  __TEXT.__const: 0xc8
-  __TEXT.__oslogstring: 0x1009
+  __TEXT.__const: 0xd0
+  __TEXT.__oslogstring: 0x107a
   __TEXT.__objc_classname: 0x86
   __TEXT.__objc_methname: 0x1075
   __TEXT.__objc_methtype: 0x26b
-  __TEXT.__gcc_except_tab: 0x154
+  __TEXT.__gcc_except_tab: 0x168
   __TEXT.__cstring: 0x1ee
-  __TEXT.__unwind_info: 0x208
+  __TEXT.__unwind_info: 0x210
   __DATA_CONST.__const: 0x118
   __DATA_CONST.__cfstring: 0x320
   __DATA_CONST.__objc_classlist: 0x20

   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__objc_intobj: 0x18
-  __DATA_CONST.__auth_got: 0x2d0
+  __DATA_CONST.__auth_got: 0x2d8
   __DATA_CONST.__got: 0xd0
+  __DATA_CONST.__auth_ptr: 0x8
   __DATA.__objc_const: 0x450
   __DATA.__objc_selrefs: 0x520
   __DATA.__objc_ivar: 0x8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 110
-  Symbols:   402
-  CStrings:  341
+  Functions: 115
+  Symbols:   405
+  CStrings:  343
 
Symbols:
+ GCC_except_table11
+ __ANEStorageProbeFileIsReadable
+ ___chkstk_darwin
+ _pread
- GCC_except_table10
CStrings:
+ "%@: %@ failed readability probe. Returning nil"
+ "%@: pread(%@, offset=%zu, want=%zu) failed. got=%zd errno=%d : %s"
```
