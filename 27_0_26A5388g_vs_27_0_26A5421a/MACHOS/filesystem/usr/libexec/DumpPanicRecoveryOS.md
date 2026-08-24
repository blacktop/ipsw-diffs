## DumpPanicRecoveryOS

> `/usr/libexec/DumpPanicRecoveryOS`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-37.0.0.0.0
-  __TEXT.__text: 0x28390
+37.0.1.0.0
+  __TEXT.__text: 0x28410
   __TEXT.__auth_stubs: 0xbb0
-  __TEXT.__objc_stubs: 0x20a0
+  __TEXT.__objc_stubs: 0x20c0
   __TEXT.__objc_methlist: 0x76c
   __TEXT.__const: 0x250
-  __TEXT.__objc_methname: 0x1b83
+  __TEXT.__objc_methname: 0x1b9a
   __TEXT.__cstring: 0x26cf
   __TEXT.__oslogstring: 0x4a67
   __TEXT.__objc_classname: 0xe9
   __TEXT.__objc_methtype: 0x540
-  __TEXT.__gcc_except_tab: 0xb14
-  __TEXT.__unwind_info: 0x840
+  __TEXT.__gcc_except_tab: 0xb38
+  __TEXT.__unwind_info: 0x850
   __DATA_CONST.__const: 0x690
   __DATA_CONST.__cfstring: 0x2140
   __DATA_CONST.__objc_classlist: 0x60

   __DATA_CONST.__got: 0x1e0
   __DATA_CONST.__auth_ptr: 0x28
   __DATA.__objc_const: 0xdd8
-  __DATA.__objc_selrefs: 0x990
+  __DATA.__objc_selrefs: 0x998
   __DATA.__objc_ivar: 0x80
   __DATA.__objc_data: 0x3c0
   __DATA.__data: 0x228

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 828
+  Functions: 829
   Symbols:   266
-  CStrings:  1243
+  CStrings:  1244
 
CStrings:
+ "useCrashlogContainers:"
```
