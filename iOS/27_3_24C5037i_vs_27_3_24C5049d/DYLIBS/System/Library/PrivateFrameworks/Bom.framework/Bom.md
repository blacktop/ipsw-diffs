## Bom

> `/System/Library/PrivateFrameworks/Bom.framework/Bom`

```diff

-280.0.0.0.0
-  __TEXT.__text: 0x5b05c
-  __TEXT.__cstring: 0x129e3
+282.0.0.0.0
+  __TEXT.__text: 0x5b098
+  __TEXT.__cstring: 0x12a6b
   __TEXT.__const: 0x1728
   __TEXT.__oslogstring: 0x103e
   __TEXT.__unwind_info: 0xf48

   - /usr/lib/libz.1.dylib
   Functions: 1101
   Symbols:   1562
-  CStrings:  2392
+  CStrings:  2394
 
Functions:
~ _create_entry_filesystem : 6900 -> 6916
~ _BOMCopierCopySourceEntryToDestinationSet : 4060 -> 3996
~ __copyFile : 9060 -> 9072
~ _BOMStorageCopyFromBlock : 228 -> 276
~ _BOMStorageCopyFromBlockRange : 664 -> 712
CStrings:
+ "BOMStorageCopyFromBlock: bid >= storage->blockTableCount"
+ "BOMStorageCopyRangeFromBlockRange: bad block (bid >= storage->blockTableCount)"
```
