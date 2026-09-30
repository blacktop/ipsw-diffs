## libAppleArchive.dylib

> `/usr/lib/libAppleArchive.dylib`

```diff

 450.160.2.0.0
-  __TEXT.__text: 0x830c4
-  __TEXT.__auth_stubs: 0xf90
-  __TEXT.__cstring: 0x1424d
+  __TEXT.__text: 0x833b8
+  __TEXT.__auth_stubs: 0xfa0
+  __TEXT.__cstring: 0x14308
   __TEXT.__const: 0x960
   __TEXT.__oslogstring: 0x31
   __TEXT.__unwind_info: 0xd40
   __TEXT.__eh_frame: 0x48
   __DATA_CONST.__got: 0xa0
   __DATA_CONST.__const: 0x158
-  __AUTH_CONST.__auth_got: 0x7c8
+  __AUTH_CONST.__auth_got: 0x7d0
   __AUTH_CONST.__const: 0x80
   __AUTH_CONST.__cfstring: 0x40
   __DATA_DIRTY.__data: 0x10

   - /usr/lib/libcompression.dylib
   - /usr/lib/liblzma.5.dylib
   Functions: 1069
-  Symbols:   1313
-  CStrings:  2893
+  Symbols:   1314
+  CStrings:  2899
 
Symbols:
+ _linkat
Functions:
~ _aeaInputStreamDecryptSegment : 1348 -> 1408
~ _aeaInputStreamLoadSegment : 1848 -> 1920
~ _aeaContainerCreateExisting : 4104 -> 4236
~ _copyFileWithAttributes : 920 -> 956
~ _removeFile : 140 -> 176
~ _aaEntryAttributesInitWithPath : 952 -> 1036
~ _aaEntryAttributesApplyToPath : 1604 -> 1636
~ _aaEntryAttributesApplyToFD : 1344 -> 1408
~ _aaCheckAndFixWithPath : 2096 -> 1968
~ _AARandomAccessDecodeAndExtract : 5316 -> 5292
~ _workerProc : 8264 -> 8272
~ _extractStreamClose : 3136 -> 3392
~ _extractThreadProc : 3588 -> 3508
~ _clusterEntryUpdateDAT : 472 -> 488
~ _aaHeaderInitWithEncodedData : 1208 -> 1312
~ _update_field_sizes : 656 -> 744
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
