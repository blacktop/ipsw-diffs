## libAppleArchive.dylib

> `/usr/lib/libAppleArchive.dylib`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`

```diff

 469.0.0.0.0
-  __TEXT.__text: 0x83430
-  __TEXT.__cstring: 0x133db
+  __TEXT.__text: 0x83724
+  __TEXT.__cstring: 0x13496
   __TEXT.__const: 0x920
   __TEXT.__oslogstring: 0x31
   __TEXT.__unwind_info: 0xd78

   __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x80
   __AUTH_CONST.__cfstring: 0x40
-  __AUTH_CONST.__auth_got: 0x790
+  __AUTH_CONST.__auth_got: 0x798
   __DATA_DIRTY.__data: 0x10
   __DATA_DIRTY.__bss: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libcompression.dylib
   - /usr/lib/liblzma.5.dylib
   Functions: 1072
-  Symbols:   1310
-  CStrings:  2905
+  Symbols:   1311
+  CStrings:  2911
 
Symbols:
+ _linkat
Functions:
~ _extractThreadProc : 3588 -> 3508
~ _aeaInputStreamDecryptSegment : 1348 -> 1408
~ _aeaInputStreamLoadSegment : 1856 -> 1928
~ _aeaContainerCreateExisting : 4140 -> 4272
~ _copyFileWithAttributes : 796 -> 836
~ _removeFile : 140 -> 176
~ _aaEntryAttributesInitWithPath : 952 -> 1036
~ _aaEntryAttributesApplyToPath : 1608 -> 1640
~ _aaEntryAttributesApplyToFD : 1344 -> 1408
~ _aaCheckAndFixWithPath : 2096 -> 1968
~ _AARandomAccessDecodeAndExtract : 5360 -> 5328
~ _workerProc : 8160 -> 8176
~ _extractStreamClose : 3100 -> 3356
~ _clusterEntryUpdateDAT : 464 -> 476
~ _aaHeaderInitWithEncodedData : 1204 -> 1308
~ _update_field_sizes : 672 -> 760
CStrings:
+ "'H' LNK not a regular file: %s"
+ "Invalid segment size in cluster header"
+ "bad donor for: %s"
+ "blob field size too large"
+ "cluster_id out of range"
+ "donor is not a regular file: %s"
+ "header payload too large"
- "link %s"
```
