## com.apple.filesystems.udf

> `com.apple.filesystems.udf`

### Sections with Same Size but Changed Content

- `__DATA.__data`
- `__DATA_CONST.__auth_got`
- `__DATA_CONST.__got`
- `__DATA_CONST.__const`
- `__DATA_CONST.__kalloc_type`
- `__DATA_CONST.__kalloc_var`

```diff

-324.0.0.0.0
+324.160.3.0.0
   __TEXT.__const: 0x1b08
-  __TEXT.__cstring: 0x302a
-  __TEXT_EXEC.__text: 0x2f3c4
+  __TEXT.__cstring: 0x308d
+  __TEXT_EXEC.__text: 0x2f400
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x4f8
   __DATA.__common: 0x4d8

   __DATA_CONST.__kalloc_var: 0xa0
   Functions: 855
   Symbols:   1173
-  CStrings:  347
+  CStrings:  349
 
Functions:
~ __ZN20UDFAllocDescIterator18GetADFinishByteOffEPhb : 284 -> 308
~ __ZN16UDFStagingBuffer17PatchFileMetadataEP13UDFExtentListPj : 3012 -> 3048
CStrings:
+ "FE/EFE (%u, %u) L_EA+L_AD exceeds sector size"
+ "FE/EFE (partRef %u, lbn %u) L_EA exceeds sector size"
```
