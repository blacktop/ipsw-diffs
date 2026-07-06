## libParallelCompression.dylib

> `/usr/lib/libParallelCompression.dylib`

```diff

-  __TEXT.__text: 0x55fa4
+  __TEXT.__text: 0x55fac
   __TEXT.__cstring: 0xffb7
   __TEXT.__const: 0x830
   __TEXT.__oslogstring: 0x31
Sections:
~ __TEXT.__cstring : content changed
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__const : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__cfstring : content changed
Functions:
~ _processEntryThreadProc : 5836 -> 5816
~ _resizeStream : 960 -> 976
~ _RawImageDiff : 6824 -> 6832
~ _archiveTreeFromIndexBeginProc : 788 -> 796
~ _OArchiveFileStreamWrite : 788 -> 768
~ _BXPatch5StreamWithFlags : 2940 -> 2936
~ _BXPatch5InPlace : 2908 -> 2904
~ _pc_zero_coder_decode : 344 -> 332
~ _pc_zero_coder_encode : 312 -> 324
~ _bomBeginProc : 2672 -> 2640
~ _ParallelCompressionFileOpen : 3952 -> 3976
~ _rawimg_get_digests : 3188 -> 3168
~ _ParallelArchiveCombine : 2300 -> 2304
~ _loadDirectory : 1316 -> 1328
~ _updateOps : 2180 -> 2216
CStrings:
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.UZIGUO/Sources/ParallelCompression/AppleArchive/AAByteStream.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.UZIGUO/Sources/ParallelCompression/AppleArchive/AACacheStream.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.UZIGUO/Sources/ParallelCompression/AppleArchive/AACompressionStream.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.UZIGUO/Sources/ParallelCompression/AppleArchive/AAJSONStreams.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.UZIGUO/Sources/ParallelCompression/AppleArchive/AAMemoryStream.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.UZIGUO/Sources/ParallelCompression/AppleArchive/AASequentialDecompressionStream.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.UZIGUO/Sources/ParallelCompression/AppleArchive/AATempStream.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.UZIGUO/Sources/ParallelCompression/Common/BlobBuffer.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.UZIGUO/Sources/ParallelCompression/Common/ErrorCorrection.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.UZIGUO/Sources/ParallelCompression/Common/ErrorCorrection_ECC65537.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.UZIGUO/Sources/ParallelCompression/Common/IOBasicStreams.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.UZIGUO/Sources/ParallelCompression/Common/IOBuffers.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.UZIGUO/Sources/ParallelCompression/Common/IOCompressedStreams.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.UZIGUO/Sources/ParallelCompression/Common/ParallelCompressionAFSCStream.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.UZIGUO/Sources/ParallelCompression/Common/SharedArray.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.UZIGUO/Sources/ParallelCompression/Common/SharedBuffer.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.UZIGUO/Sources/ParallelCompression/Common/StringTable.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.UZIGUO/Sources/ParallelCompression/Common/ThreadPipeline.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.UZIGUO/Sources/ParallelCompression/Common/ThreadPool.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.UZIGUO/Sources/ParallelCompression/Common/Threads.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.UZIGUO/Sources/ParallelCompression/Common/Utils.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.UZIGUO/Sources/ParallelCompression/ParallelArchive/../ParallelCompression/../Common/SharedArray.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.UZIGUO/Sources/ParallelCompression/ParallelArchive/ArchiveDatabase.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.UZIGUO/Sources/ParallelCompression/ParallelArchive/ArchiveDatabasePlugins/ArchiveDatabaseFilePlugin.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.UZIGUO/Sources/ParallelCompression/ParallelArchive/ArchiveTree.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.UZIGUO/Sources/ParallelCompression/ParallelArchive/CheckAndFix.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.UZIGUO/Sources/ParallelCompression/ParallelArchive/Combine.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.UZIGUO/Sources/ParallelCompression/ParallelArchive/Convert.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.UZIGUO/Sources/ParallelCompression/ParallelArchive/Extract.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.UZIGUO/Sources/ParallelCompression/ParallelArchive/ExtractClones.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.UZIGUO/Sources/ParallelCompression/ParallelArchive/ExtractSubtree.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.UZIGUO/Sources/ParallelCompression/ParallelArchive/GenerateBOM.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.UZIGUO/Sources/ParallelCompression/ParallelArchive/ISparseArchiveStream.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.UZIGUO/Sources/ParallelCompression/ParallelArchive/MSUArchive.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.UZIGUO/Sources/ParallelCompression/ParallelArchive/Read.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.UZIGUO/Sources/ParallelCompression/ParallelArchive/Search.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.UZIGUO/Sources/ParallelCompression/ParallelArchive/Sort.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.UZIGUO/Sources/ParallelCompression/ParallelArchive/VerifyDir.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.UZIGUO/Sources/ParallelCompression/ParallelArchive/Write.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.UZIGUO/Sources/ParallelCompression/ParallelArchive/WriteDirContents.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.UZIGUO/Sources/ParallelCompression/ParallelArchive/YAACommon.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.UZIGUO/Sources/ParallelCompression/ParallelCompression/File.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.UZIGUO/Sources/ParallelCompression/ParallelCompression/Filter.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.UZIGUO/Sources/ParallelCompression/ParallelCompression/Streams.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.UZIGUO/Sources/ParallelCompression/ParallelDiff/BXDiff5.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.UZIGUO/Sources/ParallelCompression/ParallelDiff/BXDiffBase.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.UZIGUO/Sources/ParallelCompression/ParallelDiff/BXDiffControls.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.UZIGUO/Sources/ParallelCompression/ParallelDiff/BXDiffMatches.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.UZIGUO/Sources/ParallelCompression/ParallelDiff/BXDiffWithCache.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.UZIGUO/Sources/ParallelCompression/ParallelDiff/DirectoryDiff.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.UZIGUO/Sources/ParallelCompression/ParallelDiff/FilePatchCache.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.UZIGUO/Sources/ParallelCompression/ParallelDiff/ImageDiff/APFS/APFS.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.UZIGUO/Sources/ParallelCompression/ParallelDiff/ImageDiff/GenericArray.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.UZIGUO/Sources/ParallelCompression/ParallelDiff/ImageDiff/ImageDiff.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.UZIGUO/Sources/ParallelCompression/ParallelDiff/ImageDiff/ImageDiffInPlace.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.UZIGUO/Sources/ParallelCompression/ParallelDiff/ImageDiff/ImageOutputStream.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.UZIGUO/Sources/ParallelCompression/ParallelDiff/ImageDiff/ImagePatch.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.UZIGUO/Sources/ParallelCompression/ParallelDiff/ImageDiff/ImageStreams.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.UZIGUO/Sources/ParallelCompression/ParallelDiff/ImageDiff/InSituStream.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.UZIGUO/Sources/ParallelCompression/ParallelDiff/ImageDiff/RawImage.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.UZIGUO/Sources/ParallelCompression/ParallelDiff/LargeFile.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.UZIGUO/Sources/ParallelCompression/ParallelDiff/PatchCache.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.UZIGUO/Sources/ParallelCompression/ParallelPatch/BXPatch4.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.UZIGUO/Sources/ParallelCompression/ParallelPatch/BXPatch5.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.UZIGUO/Sources/ParallelCompression/ParallelPatch/BXPatchFile.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.UZIGUO/Sources/ParallelCompression/ParallelPatch/DirectoryPatch.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.UZIGUO/Sources/ParallelCompression/ParallelPatch/PagedFile.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.NTXlDi/Sources/ParallelCompression/AppleArchive/AAByteStream.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.NTXlDi/Sources/ParallelCompression/AppleArchive/AACacheStream.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.NTXlDi/Sources/ParallelCompression/AppleArchive/AACompressionStream.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.NTXlDi/Sources/ParallelCompression/AppleArchive/AAJSONStreams.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.NTXlDi/Sources/ParallelCompression/AppleArchive/AAMemoryStream.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.NTXlDi/Sources/ParallelCompression/AppleArchive/AASequentialDecompressionStream.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.NTXlDi/Sources/ParallelCompression/AppleArchive/AATempStream.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.NTXlDi/Sources/ParallelCompression/Common/BlobBuffer.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.NTXlDi/Sources/ParallelCompression/Common/ErrorCorrection.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.NTXlDi/Sources/ParallelCompression/Common/ErrorCorrection_ECC65537.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.NTXlDi/Sources/ParallelCompression/Common/IOBasicStreams.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.NTXlDi/Sources/ParallelCompression/Common/IOBuffers.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.NTXlDi/Sources/ParallelCompression/Common/IOCompressedStreams.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.NTXlDi/Sources/ParallelCompression/Common/ParallelCompressionAFSCStream.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.NTXlDi/Sources/ParallelCompression/Common/SharedArray.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.NTXlDi/Sources/ParallelCompression/Common/SharedBuffer.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.NTXlDi/Sources/ParallelCompression/Common/StringTable.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.NTXlDi/Sources/ParallelCompression/Common/ThreadPipeline.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.NTXlDi/Sources/ParallelCompression/Common/ThreadPool.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.NTXlDi/Sources/ParallelCompression/Common/Threads.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.NTXlDi/Sources/ParallelCompression/Common/Utils.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.NTXlDi/Sources/ParallelCompression/ParallelArchive/../ParallelCompression/../Common/SharedArray.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.NTXlDi/Sources/ParallelCompression/ParallelArchive/ArchiveDatabase.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.NTXlDi/Sources/ParallelCompression/ParallelArchive/ArchiveDatabasePlugins/ArchiveDatabaseFilePlugin.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.NTXlDi/Sources/ParallelCompression/ParallelArchive/ArchiveTree.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.NTXlDi/Sources/ParallelCompression/ParallelArchive/CheckAndFix.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.NTXlDi/Sources/ParallelCompression/ParallelArchive/Combine.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.NTXlDi/Sources/ParallelCompression/ParallelArchive/Convert.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.NTXlDi/Sources/ParallelCompression/ParallelArchive/Extract.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.NTXlDi/Sources/ParallelCompression/ParallelArchive/ExtractClones.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.NTXlDi/Sources/ParallelCompression/ParallelArchive/ExtractSubtree.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.NTXlDi/Sources/ParallelCompression/ParallelArchive/GenerateBOM.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.NTXlDi/Sources/ParallelCompression/ParallelArchive/ISparseArchiveStream.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.NTXlDi/Sources/ParallelCompression/ParallelArchive/MSUArchive.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.NTXlDi/Sources/ParallelCompression/ParallelArchive/Read.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.NTXlDi/Sources/ParallelCompression/ParallelArchive/Search.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.NTXlDi/Sources/ParallelCompression/ParallelArchive/Sort.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.NTXlDi/Sources/ParallelCompression/ParallelArchive/VerifyDir.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.NTXlDi/Sources/ParallelCompression/ParallelArchive/Write.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.NTXlDi/Sources/ParallelCompression/ParallelArchive/WriteDirContents.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.NTXlDi/Sources/ParallelCompression/ParallelArchive/YAACommon.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.NTXlDi/Sources/ParallelCompression/ParallelCompression/File.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.NTXlDi/Sources/ParallelCompression/ParallelCompression/Filter.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.NTXlDi/Sources/ParallelCompression/ParallelCompression/Streams.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.NTXlDi/Sources/ParallelCompression/ParallelDiff/BXDiff5.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.NTXlDi/Sources/ParallelCompression/ParallelDiff/BXDiffBase.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.NTXlDi/Sources/ParallelCompression/ParallelDiff/BXDiffControls.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.NTXlDi/Sources/ParallelCompression/ParallelDiff/BXDiffMatches.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.NTXlDi/Sources/ParallelCompression/ParallelDiff/BXDiffWithCache.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.NTXlDi/Sources/ParallelCompression/ParallelDiff/DirectoryDiff.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.NTXlDi/Sources/ParallelCompression/ParallelDiff/FilePatchCache.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.NTXlDi/Sources/ParallelCompression/ParallelDiff/ImageDiff/APFS/APFS.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.NTXlDi/Sources/ParallelCompression/ParallelDiff/ImageDiff/GenericArray.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.NTXlDi/Sources/ParallelCompression/ParallelDiff/ImageDiff/ImageDiff.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.NTXlDi/Sources/ParallelCompression/ParallelDiff/ImageDiff/ImageDiffInPlace.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.NTXlDi/Sources/ParallelCompression/ParallelDiff/ImageDiff/ImageOutputStream.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.NTXlDi/Sources/ParallelCompression/ParallelDiff/ImageDiff/ImagePatch.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.NTXlDi/Sources/ParallelCompression/ParallelDiff/ImageDiff/ImageStreams.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.NTXlDi/Sources/ParallelCompression/ParallelDiff/ImageDiff/InSituStream.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.NTXlDi/Sources/ParallelCompression/ParallelDiff/ImageDiff/RawImage.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.NTXlDi/Sources/ParallelCompression/ParallelDiff/LargeFile.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.NTXlDi/Sources/ParallelCompression/ParallelDiff/PatchCache.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.NTXlDi/Sources/ParallelCompression/ParallelPatch/BXPatch4.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.NTXlDi/Sources/ParallelCompression/ParallelPatch/BXPatch5.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.NTXlDi/Sources/ParallelCompression/ParallelPatch/BXPatchFile.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.NTXlDi/Sources/ParallelCompression/ParallelPatch/DirectoryPatch.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.NTXlDi/Sources/ParallelCompression/ParallelPatch/PagedFile.c"

```
