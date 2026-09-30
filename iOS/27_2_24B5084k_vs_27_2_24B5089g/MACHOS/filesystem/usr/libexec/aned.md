## aned

> `/usr/libexec/aned`

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
-  __TEXT.__text: 0x7c790
-  __TEXT.__auth_stubs: 0xf80
+382.101.0.0.0
+  __TEXT.__text: 0x7ca48
+  __TEXT.__auth_stubs: 0xf90
   __TEXT.__objc_stubs: 0x3480
   __TEXT.__objc_methlist: 0x117c
   __TEXT.__const: 0x60ec
-  __TEXT.__gcc_except_tab: 0x61a0
+  __TEXT.__gcc_except_tab: 0x61b4
   __TEXT.__cstring: 0x5cfc
-  __TEXT.__oslogstring: 0x6ce5
+  __TEXT.__oslogstring: 0x6d61
   __TEXT.__objc_classname: 0x247
   __TEXT.__objc_methname: 0x3e6b
   __TEXT.__objc_methtype: 0xeaf
-  __TEXT.__unwind_info: 0x2c58
+  __TEXT.__unwind_info: 0x2c60
   __DATA_CONST.__const: 0x2b68
   __DATA_CONST.__cfstring: 0xb00
   __DATA_CONST.__objc_classlist: 0x90

   __DATA_CONST.__objc_arraydata: 0x8
   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA_CONST.__objc_intobj: 0x18
-  __DATA_CONST.__auth_got: 0x7d8
+  __DATA_CONST.__auth_got: 0x7e0
   __DATA_CONST.__got: 0x3c8
-  __DATA_CONST.__auth_ptr: 0x18
+  __DATA_CONST.__auth_ptr: 0x20
   __DATA.__objc_const: 0x1c98
   __DATA.__objc_selrefs: 0xfb8
   __DATA.__objc_ivar: 0xe4

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2787
-  Symbols:   4176
-  CStrings:  1755
+  Functions: 2789
+  Symbols:   4178
+  CStrings:  1757
 
Symbols:
+ __ANEStorageProbeFileIsReadable
+ _pread
CStrings:
+ "%@: %@ failed readability probe. Returning nil"
+ "%@: perTdStats Model patching is not enabled"
+ "%@: pread(%@, offset=%zu, want=%zu) failed. got=%zd errno=%d : %s"
- "%@: Model patching is not enabled"
```
