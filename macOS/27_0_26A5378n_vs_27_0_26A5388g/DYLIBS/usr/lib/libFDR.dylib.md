## libFDR.dylib

> `/usr/lib/libFDR.dylib`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_selrefs`
- `__AUTH_CONST.__const`
- `__DATA.__objc_classrefs`
- `__DATA.__data`

```diff

-1636.0.12.0.0
-  __TEXT.__text: 0x8b2d8
+1636.0.16.0.0
+  __TEXT.__text: 0x8b3cc
   __TEXT.__const: 0x2008
-  __TEXT.__cstring: 0x23641
+  __TEXT.__cstring: 0x23695
   __TEXT.__gcc_except_tab: 0x34
   __TEXT.__dlopen_cstrs: 0x56
   __TEXT.__ustring: 0x38

   __DATA_CONST.__objc_selrefs: 0x28
   __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0xad8
-  __AUTH_CONST.__cfstring: 0xfac0
+  __AUTH_CONST.__cfstring: 0xfae0
   __AUTH_CONST.__auth_got: 0xa10
   __DATA.__objc_classrefs: 0x10
   __DATA.__data: 0x160

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libamsupport.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 4631
-  Symbols:   2190
-  CStrings:  4193
+  Functions: 4633
+  Symbols:   2191
+  CStrings:  4194
 
Symbols:
+ AMFDRSealingMapCopyMultiInstanceForClassWithOptions
+ _AMFDRSealingMapCopyMultiInstanceForClassWithOptions
- AMFDRSealingMapCopyMultiInstanceForClass
CStrings:
+ "AMFDRSealingMapCopyMultiInstanceForClassWithOptions"
+ "there's something wrong with subCC digest for %@:%@, subCC check failing"
- "AMFDRSealingMapCopyMultiInstanceForClass"
```
