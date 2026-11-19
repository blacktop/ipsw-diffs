## DumpPanicRecoveryOS

> `/usr/libexec/DumpPanicRecoveryOS`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__objc_intobj`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__data`

```diff

-37.0.1.0.0
-  __TEXT.__text: 0x28050
+41.40.7.0.0
+  __TEXT.__text: 0x2821c
   __TEXT.__auth_stubs: 0xbb0
   __TEXT.__objc_stubs: 0x20c0
   __TEXT.__objc_methlist: 0x76c
   __TEXT.__const: 0x250
   __TEXT.__objc_methname: 0x1b9a
   __TEXT.__cstring: 0x26cf
-  __TEXT.__oslogstring: 0x4a67
+  __TEXT.__oslogstring: 0x4ac4
   __TEXT.__objc_classname: 0xe9
   __TEXT.__objc_methtype: 0x540
   __TEXT.__gcc_except_tab: 0xb38
-  __TEXT.__unwind_info: 0xce8
-  __DATA_CONST.__const: 0x690
+  __TEXT.__unwind_info: 0xce0
+  __DATA_CONST.__const: 0x6a0
   __DATA_CONST.__cfstring: 0x2140
   __DATA_CONST.__objc_classlist: 0x60
   __DATA_CONST.__objc_protolist: 0x10

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 830
+  Functions: 829
   Symbols:   266
-  CStrings:  1244
+  CStrings:  1246
 
CStrings:
+ "failed to fchmod file at path %s to mode 0666 with error : %s"
+ "fd identity mismatch for %s — possible TOCTOU, skipping"
+ "lstat failed for %s: %s"
+ "refusing to chown/chmod suspect file %s (uid=%u nlink=%u mode=0%o)"
- "failed to fchmod group for file at path %s to %d with error : %s"
- "skipping fchmod/fchown for suspect file at path : %s"
```
