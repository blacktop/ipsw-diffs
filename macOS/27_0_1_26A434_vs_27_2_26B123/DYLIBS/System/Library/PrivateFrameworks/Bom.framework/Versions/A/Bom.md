## Bom

> `/System/Library/PrivateFrameworks/Bom.framework/Versions/A/Bom`

```diff

-279.2.0.0.0
-  __TEXT.__text: 0x62190
-  __TEXT.__cstring: 0x13da8
+280.0.0.0.0
+  __TEXT.__text: 0x62810
+  __TEXT.__cstring: 0x13dd6
   __TEXT.__const: 0x1738
   __TEXT.__oslogstring: 0x10b9
   __TEXT.__unwind_info: 0xb78

   __AUTH_CONST.__cfstring: 0x13e0
   __AUTH_CONST.__auth_got: 0xd10
   __AUTH_CONST.__auth_ptr: 0x0
-  __AUTH.__data: 0x160
   __DATA.__data: 0x168
   __DATA.__bss: 0x8dc
+  __DATA_DIRTY.__data: 0x160
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/PrivateFrameworks/AppleFSCompression.framework/Versions/A/AppleFSCompression
   - /usr/lib/libAppleArchive.dylib

   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libbz2.1.0.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 1122
-  Symbols:   1605
-  CStrings:  2501
+  Functions: 1123
+  Symbols:   1606
+  CStrings:  2502
 
Symbols:
+ _BOMStreamWriteUInt64
+ __BOMCopierSanitizePath
- __copyDataFork
Functions:
~ __sanitizePath : 716 -> 4
~ __copyFile : 2792 -> 9708
~ _BOMPKZipFree : 192 -> 208
~ _BOMCopierDestinationNew : 9256 -> 9264
~ __resetCopier : 804 -> 808
~ __prepareCopierState : 692 -> 724
~ __copyFromDirToDir : 2956 -> 3164
~ __copyExtendedAttributes : 940 -> 944
- __copyDataFork
~ __copyFromCPIO : 1908 -> 1888
~ __mergeAppleDouble : 868 -> 924
~ _BOMStorageOpenWithSys : 1276 -> 1292
~ __ReadBlockTable : 348 -> 404
+ _BOMStreamWriteUInt16
~ _BOMPKZipWriteLocalHeader : 944 -> 1072
~ __squirrelAwayInfo : 344 -> 364
~ _BOMPKZipWriteDataDescriptor : 272 -> 340
~ _BOMPKZipWriteCentralDirectory : 768 -> 1488
+ __BOMCopierSanitizePath
~ _BOMCopierCopyWithOptions2 : 6640 -> 6632
CStrings:
+ "Could not re-apply quarantine state to %s: %d"
+ "Oct  3 2026"
- "Aug  8 2026"
```
