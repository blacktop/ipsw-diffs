## libAppleArchive.dylib

> `/usr/lib/libAppleArchive.dylib`

```diff

 450.160.2.0.0
-  __TEXT.__text: 0x82d0c
-  __TEXT.__auth_stubs: 0xf20
-  __TEXT.__cstring: 0x13278
+  __TEXT.__text: 0x83004
+  __TEXT.__auth_stubs: 0xf30
+  __TEXT.__cstring: 0x13333
   __TEXT.__const: 0x960
   __TEXT.__oslogstring: 0x31
   __TEXT.__unwind_info: 0xd38
   __TEXT.__eh_frame: 0x48
   __DATA_CONST.__got: 0xa0
   __DATA_CONST.__const: 0x158
-  __AUTH_CONST.__auth_got: 0x790
+  __AUTH_CONST.__auth_got: 0x798
   __AUTH_CONST.__const: 0x80
   __AUTH_CONST.__cfstring: 0x40
   __DATA_DIRTY.__data: 0x10

   - /usr/lib/libcompression.dylib
   - /usr/lib/liblzma.5.dylib
   Functions: 1067
-  Symbols:   1303
-  CStrings:  2887
+  Symbols:   1304
+  CStrings:  2893
 
Symbols:
+ _linkat
Functions:
~ _aeaInputStreamDecryptSegment : 1348 -> 1408
~ _aeaInputStreamLoadSegment : 1848 -> 1920
~ _aeaContainerCreateExisting : 4104 -> 4236
~ _copyFileWithAttributes : 796 -> 836
~ _removeFile : 140 -> 176
~ _aaEntryAttributesInitWithPath : 952 -> 1036
~ _aaEntryAttributesApplyToPath : 1604 -> 1636
~ _aaEntryAttributesApplyToFD : 1344 -> 1408
~ _aaCheckAndFixWithPath : 2096 -> 1968
~ _AARandomAccessDecodeAndExtract : 5316 -> 5292
~ _workerProc : 8264 -> 8272
~ _extractStreamClose : 3120 -> 3376
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
