## com.apple.filesystems.udf

> `com.apple.filesystems.udf`

```diff

   __TEXT.__const: 0x1b08
-  __TEXT.__cstring: 0x302a
-  __TEXT_EXEC.__text: 0x2f588
+  __TEXT.__cstring: 0x308d
+  __TEXT_EXEC.__text: 0x2f5a0
   __TEXT_EXEC.__auth_stubs: 0xa40
   __DATA.__data: 0x4f8
   __DATA.__common: 0x4d8

   __DATA_CONST.__got: 0x20
   Functions: 855
   Symbols:   1175
-  CStrings:  347
+  CStrings:  349
 
Sections:
~ __DATA.__data : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__kalloc_type : content changed
~ __DATA_CONST.__kalloc_var : content changed
~ __DATA_CONST.__auth_got : content changed
~ __DATA_CONST.__got : content changed
Functions:
~ _localsub : 1476 -> 1472
~ __ZN20UDFAllocDescIterator18GetADFinishByteOffEPhb : 276 -> 300
~ __Z16UDFUtf8ToDstringPKcmPhm : 280 -> 292
~ __Z13UDFIsValidTagPKhjb : 92 -> 88
~ __Z15UDFCalcTagCkSumPvj : 108 -> 104
~ __ZN14UDFDirIterator21CurEntryHeaderIsValidEv : 204 -> 200
~ __ZN14UDFDirIterator15CurEntryIsValidEv : 276 -> 272
~ __ZN18UDFExtAttrIterator4InitEP9UDFStreamx : 364 -> 360
~ __Z31UDFKernelStringToDiskStringListPKhmP12UDFStringBufPmbb : 1372 -> 1344
~ __ZN8UDFMount12RenameVolumeEPKc : 500 -> 508
~ __ZN11UDFFileNode9WriteLinkEPh : 432 -> 420
~ __ZN16UDFStagingBuffer17PatchFileMetadataEP13UDFExtentListPj : 2972 -> 3016
CStrings:
+ "FE/EFE (%u, %u) L_EA+L_AD exceeds sector size"
+ "FE/EFE (partRef %u, lbn %u) L_EA exceeds sector size"

```
