## Bom

> `/System/Library/PrivateFrameworks/Bom.framework/Versions/A/Bom`

```diff

-265.0.0.0.0
-  __TEXT.__text: 0x5c580
+269.0.0.0.0
+  __TEXT.__text: 0x5d078
   __TEXT.__auth_stubs: 0x1980
-  __TEXT.__cstring: 0x12b8d
-  __TEXT.__const: 0x1508
-  __TEXT.__oslogstring: 0x1036
-  __TEXT.__unwind_info: 0xb28
+  __TEXT.__cstring: 0x13027
+  __TEXT.__const: 0x14f8
+  __TEXT.__oslogstring: 0x108c
+  __TEXT.__unwind_info: 0xb30
   __DATA_CONST.__got: 0x70
   __DATA_CONST.__const: 0x958
   __AUTH_CONST.__auth_got: 0xcc0
   __AUTH_CONST.__auth_ptr: 0x30
   __AUTH_CONST.__const: 0x1e0
-  __AUTH_CONST.__cfstring: 0x13c0
+  __AUTH_CONST.__cfstring: 0x13e0
   __AUTH.__data: 0x160
-  __DATA.__data: 0x20
+  __DATA.__data: 0x168
   __DATA.__bss: 0x8dc
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/PrivateFrameworks/AppleFSCompression.framework/Versions/A/AppleFSCompression

   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libbz2.1.0.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 1074
-  Symbols:   1559
-  CStrings:  2374
+  Functions: 1075
+  Symbols:   1562
+  CStrings:  2402
 
Symbols:
+ _BOMFilePreallocate
+ _inject_apple_double_bytes
CStrings:
+ "%s/._%s"
+ "/AppleInternal/Library/BuildRoots/1d1afd2a-039a-11f0-91c4-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/Bom/Bom/BOMBom.c"
+ "/AppleInternal/Library/BuildRoots/1d1afd2a-039a-11f0-91c4-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/Bom/Bom/BOMBomEnumerator.c"
+ "/AppleInternal/Library/BuildRoots/1d1afd2a-039a-11f0-91c4-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/Bom/Bom/BOMFSEnumerator.c"
+ "/AppleInternal/Library/BuildRoots/1d1afd2a-039a-11f0-91c4-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/Bom/Common/BOMBufferManager.c"
+ "/AppleInternal/Library/BuildRoots/1d1afd2a-039a-11f0-91c4-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/Bom/Common/BOMCRC32.c"
+ "/AppleInternal/Library/BuildRoots/1d1afd2a-039a-11f0-91c4-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/Bom/Common/BOMFile.c"
+ "/AppleInternal/Library/BuildRoots/1d1afd2a-039a-11f0-91c4-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/Bom/Common/BOMPatternList.c"
+ "/AppleInternal/Library/BuildRoots/1d1afd2a-039a-11f0-91c4-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/Bom/Common/BOMSystemCmds.c"
+ "/AppleInternal/Library/BuildRoots/1d1afd2a-039a-11f0-91c4-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/Bom/Copier/BOMCopier2.c"
+ "/AppleInternal/Library/BuildRoots/1d1afd2a-039a-11f0-91c4-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/Bom/Copier/BOMCopierDataAnalyzer.c"
+ "/AppleInternal/Library/BuildRoots/1d1afd2a-039a-11f0-91c4-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/Bom/Copier/BOMCopierDestination.c"
+ "/AppleInternal/Library/BuildRoots/1d1afd2a-039a-11f0-91c4-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/Bom/Copier/BOMCopierMatchRecord.c"
+ "/AppleInternal/Library/BuildRoots/1d1afd2a-039a-11f0-91c4-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/Bom/Copier/BOMCopierSource.c"
+ "/AppleInternal/Library/BuildRoots/1d1afd2a-039a-11f0-91c4-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/Bom/Copier/BOMCopierSourceEntry.c"
+ "/AppleInternal/Library/BuildRoots/1d1afd2a-039a-11f0-91c4-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/Bom/Copier/data_archive/data_archive.c"
+ "/AppleInternal/Library/BuildRoots/1d1afd2a-039a-11f0-91c4-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/Bom/Copier/data_archive/data_archive_decoder.c"
+ "/AppleInternal/Library/BuildRoots/1d1afd2a-039a-11f0-91c4-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/Bom/Copier/data_archive/data_archive_entry.c"
+ "/AppleInternal/Library/BuildRoots/1d1afd2a-039a-11f0-91c4-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/Bom/FSObject/BOMFSOArchInfo.c"
+ "/AppleInternal/Library/BuildRoots/1d1afd2a-039a-11f0-91c4-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/Bom/FSObject/BOMFSOTypeInfo.c"
+ "/AppleInternal/Library/BuildRoots/1d1afd2a-039a-11f0-91c4-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/Bom/Storage/BOMStorage.c"
+ "/AppleInternal/Library/BuildRoots/1d1afd2a-039a-11f0-91c4-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/Bom/Storage/BOMStream.c"
+ "/AppleInternal/Library/BuildRoots/1d1afd2a-039a-11f0-91c4-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/Bom/Storage/BOMTree.c"
+ "Could not allocate last path component buffer: %s\n"
+ "Could not allocate parent path buffer: %s\n"
+ "Could not construct insert entry path: %s\n"
+ "Could not convert kBOMCopierSourceOptionSegmentFileSizeKey to kCFNumberLongLongType"
+ "Could not create AppleDouble injection entry"
+ "Could not create insert entry path"
+ "Could not create last path component"
+ "Could not create parent path"
+ "Could not get basename of %s: %s\n"
+ "Could not get dirname of %s: %s\n"
+ "Could not get last path component"
+ "Could not get parent path"
+ "Could not preallocate regular file at %s for %llu: %s"
+ "Could not push source entry onto the preempty stack"
+ "Could not read from source entry\n"
+ "Could not set insert entry path"
+ "Injecting AppleDouble between segmented files"
+ "Mar 18 2025"
+ "Previous split file path is NULL"
+ "Read 0 bytes from deterministic source."
+ "injectAppleDouble requires creating a CPIO"
+ "injectAppleDouble requires segment large files"
+ "injectAppleDoubleBetweenSegmentedFiles"
+ "kBOMCopierOptionInjectAppleDoubleBetweenSegmentedFilesKey is not a CFBooleanRef"
+ "kBOMCopierOptionInjectAppleDoubleBetweenSegmentedFilesKey must be a CFBooleanRef"
+ "kBOMCopierSourceOptionInjectAppleDoubleBetweenSegmentedFilesKey must be a CFBooleanRef"
+ "kBOMCopierSourceOptionSegmentFileSizeKey must be a CFNumberRef"
+ "synthesize_inject_apple_double"
- "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Bom/Bom/BOMBom.c"
- "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Bom/Bom/BOMBomEnumerator.c"
- "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Bom/Bom/BOMFSEnumerator.c"
- "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Bom/Common/BOMBufferManager.c"
- "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Bom/Common/BOMCRC32.c"
- "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Bom/Common/BOMFile.c"
- "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Bom/Common/BOMPatternList.c"
- "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Bom/Common/BOMSystemCmds.c"
- "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Bom/Copier/BOMCopier2.c"
- "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Bom/Copier/BOMCopierDataAnalyzer.c"
- "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Bom/Copier/BOMCopierDestination.c"
- "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Bom/Copier/BOMCopierMatchRecord.c"
- "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Bom/Copier/BOMCopierSource.c"
- "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Bom/Copier/BOMCopierSourceEntry.c"
- "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Bom/Copier/data_archive/data_archive.c"
- "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Bom/Copier/data_archive/data_archive_decoder.c"
- "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Bom/Copier/data_archive/data_archive_entry.c"
- "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Bom/FSObject/BOMFSOArchInfo.c"
- "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Bom/FSObject/BOMFSOTypeInfo.c"
- "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Bom/Storage/BOMStorage.c"
- "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Bom/Storage/BOMStream.c"
- "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Bom/Storage/BOMTree.c"
- "Mar  7 2025"

```
