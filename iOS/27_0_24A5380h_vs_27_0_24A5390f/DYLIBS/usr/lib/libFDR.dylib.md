## libFDR.dylib

> `/usr/lib/libFDR.dylib`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_selrefs`
- `__AUTH_CONST.__const`
- `__DATA.__data`

```diff

-1636.0.12.0.0
-  __TEXT.__text: 0x8b6dc
+1636.0.16.0.0
+  __TEXT.__text: 0x8b7d0
   __TEXT.__const: 0x2000
-  __TEXT.__cstring: 0x23549
+  __TEXT.__cstring: 0x2359d
   __TEXT.__gcc_except_tab: 0x34
   __TEXT.__dlopen_cstrs: 0x56
   __TEXT.__ustring: 0x38
-  __TEXT.__unwind_info: 0x1220
+  __TEXT.__unwind_info: 0x1228
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_methname: 0x0

   __DATA_CONST.__objc_selrefs: 0x28
   __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x9b8
-  __AUTH_CONST.__cfstring: 0xfaa0
+  __AUTH_CONST.__cfstring: 0xfac0
   __AUTH_CONST.__auth_got: 0xa08
   __DATA.__data: 0x160
   __DATA.__bss: 0xb8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libamsupport.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 4632
-  Symbols:   1730
-  CStrings:  4190
+  Functions: 4634
+  Symbols:   1731
+  CStrings:  4191
 
Symbols:
+ _AMFDRSealingMapCopyMultiInstanceForClassWithOptions
CStrings:
+ "AMFDRSealingMapCopyMultiInstanceForClassWithOptions"
+ "there's something wrong with subCC digest for %@:%@, subCC check failing"
- "AMFDRSealingMapCopyMultiInstanceForClass"
```
