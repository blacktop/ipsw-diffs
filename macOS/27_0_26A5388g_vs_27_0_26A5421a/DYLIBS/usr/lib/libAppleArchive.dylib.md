## libAppleArchive.dylib

> `/usr/lib/libAppleArchive.dylib`

```diff

 469.0.0.0.0
-  __TEXT.__text: 0x837f8
-  __TEXT.__cstring: 0x143b0
+  __TEXT.__text: 0x83b28
+  __TEXT.__cstring: 0x1446b
   __TEXT.__const: 0x920
   __TEXT.__oslogstring: 0x31
   __TEXT.__unwind_info: 0xd60

   __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x80
   __AUTH_CONST.__cfstring: 0x40
-  __AUTH_CONST.__auth_got: 0x7c8
+  __AUTH_CONST.__auth_got: 0x7d0
   __DATA_DIRTY.__data: 0x10
   __DATA_DIRTY.__bss: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/libcompression.dylib
   - /usr/lib/liblzma.5.dylib
   Functions: 1074
-  Symbols:   1320
-  CStrings:  2911
+  Symbols:   1321
+  CStrings:  2917
 
Symbols:
+ _linkat
Functions:
~ _aeaInputStreamDecryptSegment : 1348 -> 1408
~ _aeaInputStreamLoadSegment : 1856 -> 1928
~ _aeaContainerCreateExisting : 4140 -> 4272
~ _copyFileWithAttributes : 920 -> 956
~ _removeFile : 140 -> 176
~ _aaEntryAttributesInitWithPath : 952 -> 1036
~ _aaEntryAttributesApplyToPath : 1608 -> 1640
~ _aaEntryAttributesApplyToFD : 1344 -> 1408
~ _aaCheckAndFixWithPath : 2012 -> 1956
~ _AARandomAccessDecodeAndExtract : 5356 -> 5324
~ _workerProc : 8192 -> 8200
~ _extractStreamClose : 3116 -> 3372
~ _extractThreadProc : 3588 -> 3508
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
