## libAppleArchive.dylib

> `/usr/lib/libAppleArchive.dylib`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`

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
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wyL0Dk/Sources/ParallelCompression/AppleArchive/../Common/SharedArray.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wyL0Dk/Sources/ParallelCompression/AppleArchive/AAAFSCStream.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wyL0Dk/Sources/ParallelCompression/AppleArchive/AAArchiveFileStream.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wyL0Dk/Sources/ParallelCompression/AppleArchive/AAArchiveStream.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wyL0Dk/Sources/ParallelCompression/AppleArchive/AAArchiveStreamProcess.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wyL0Dk/Sources/ParallelCompression/AppleArchive/AAAssetBuilder.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wyL0Dk/Sources/ParallelCompression/AppleArchive/AAAssetDecodeStream.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wyL0Dk/Sources/ParallelCompression/AppleArchive/AAAssetDecompressionStream.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wyL0Dk/Sources/ParallelCompression/AppleArchive/AAAssetDecryptionStream.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wyL0Dk/Sources/ParallelCompression/AppleArchive/AAAssetExtractStream.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wyL0Dk/Sources/ParallelCompression/AppleArchive/AAAssetExtractor.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wyL0Dk/Sources/ParallelCompression/AppleArchive/AAAssetGenerate.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wyL0Dk/Sources/ParallelCompression/AppleArchive/AAAsyncByteStream.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wyL0Dk/Sources/ParallelCompression/AppleArchive/AAAsyncByteStreamProcessAllRanges.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wyL0Dk/Sources/ParallelCompression/AppleArchive/AAByteRange.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wyL0Dk/Sources/ParallelCompression/AppleArchive/AAByteStream.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wyL0Dk/Sources/ParallelCompression/AppleArchive/AAByteStreamProcess.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wyL0Dk/Sources/ParallelCompression/AppleArchive/AACacheStream.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wyL0Dk/Sources/ParallelCompression/AppleArchive/AAChunkAsyncStream.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wyL0Dk/Sources/ParallelCompression/AppleArchive/AAChunkInputStream.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wyL0Dk/Sources/ParallelCompression/AppleArchive/AAChunkOutputStream.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wyL0Dk/Sources/ParallelCompression/AppleArchive/AACompositeChunkAsyncStream.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wyL0Dk/Sources/ParallelCompression/AppleArchive/AACompressionStream.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wyL0Dk/Sources/ParallelCompression/AppleArchive/AAConvertArchiveOutputStream.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wyL0Dk/Sources/ParallelCompression/AppleArchive/AADecodeArchiveInputStream.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wyL0Dk/Sources/ParallelCompression/AppleArchive/AADecodeArchiveInputStreamCPIO.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wyL0Dk/Sources/ParallelCompression/AppleArchive/AADecodeArchiveInputStreamTar.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wyL0Dk/Sources/ParallelCompression/AppleArchive/AAEncodeArchiveOutputStream.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wyL0Dk/Sources/ParallelCompression/AppleArchive/AAExtractArchiveOutputStream.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wyL0Dk/Sources/ParallelCompression/AppleArchive/AAFieldACL.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wyL0Dk/Sources/ParallelCompression/AppleArchive/AAFieldKeys.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wyL0Dk/Sources/ParallelCompression/AppleArchive/AAFieldMCO.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wyL0Dk/Sources/ParallelCompression/AppleArchive/AAFieldXAT.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wyL0Dk/Sources/ParallelCompression/AppleArchive/AAFieldYEC.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wyL0Dk/Sources/ParallelCompression/AppleArchive/AAFieldYFP.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wyL0Dk/Sources/ParallelCompression/AppleArchive/AAGenericRandomAccessInputStream.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wyL0Dk/Sources/ParallelCompression/AppleArchive/AAHeader.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wyL0Dk/Sources/ParallelCompression/AppleArchive/AAInPlaceStream.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wyL0Dk/Sources/ParallelCompression/AppleArchive/AAJSONStreams.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wyL0Dk/Sources/ParallelCompression/AppleArchive/AAMemoryStream.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wyL0Dk/Sources/ParallelCompression/AppleArchive/AAPathFilter.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wyL0Dk/Sources/ParallelCompression/AppleArchive/AAPathList.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wyL0Dk/Sources/ParallelCompression/AppleArchive/AARandomAccessByteStreamProcess.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wyL0Dk/Sources/ParallelCompression/AppleArchive/AARandomAccessDecodeAndExtract.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wyL0Dk/Sources/ParallelCompression/AppleArchive/AARandomAccessDecompressionStream.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wyL0Dk/Sources/ParallelCompression/AppleArchive/AARangeInputStream.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wyL0Dk/Sources/ParallelCompression/AppleArchive/AARemoveArchiveOutputStream.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wyL0Dk/Sources/ParallelCompression/AppleArchive/AASequentialDecompressionStream.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wyL0Dk/Sources/ParallelCompression/AppleArchive/AATempStream.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wyL0Dk/Sources/ParallelCompression/AppleArchive/AAUtils.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wyL0Dk/Sources/ParallelCompression/AppleArchive/AAVerifyDirectoryArchiveOutputStream.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wyL0Dk/Sources/ParallelCompression/AppleEncryptedArchive/../AppleArchive/../Common/SharedArray.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wyL0Dk/Sources/ParallelCompression/AppleEncryptedArchive/AEAAuthData.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wyL0Dk/Sources/ParallelCompression/AppleEncryptedArchive/AEACommon.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wyL0Dk/Sources/ParallelCompression/AppleEncryptedArchive/AEAContainer.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wyL0Dk/Sources/ParallelCompression/AppleEncryptedArchive/AEAContext.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wyL0Dk/Sources/ParallelCompression/AppleEncryptedArchive/AEAContextValidate.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wyL0Dk/Sources/ParallelCompression/AppleEncryptedArchive/AEACrypto.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wyL0Dk/Sources/ParallelCompression/AppleEncryptedArchive/AEADecryptAndExtract.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wyL0Dk/Sources/ParallelCompression/AppleEncryptedArchive/AEADecryptAndExtractAsyncStream.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wyL0Dk/Sources/ParallelCompression/AppleEncryptedArchive/AEADecryptAsyncStream.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wyL0Dk/Sources/ParallelCompression/AppleEncryptedArchive/AEADecryptToFile.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wyL0Dk/Sources/ParallelCompression/AppleEncryptedArchive/AEADecryptToFileAsyncStream.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wyL0Dk/Sources/ParallelCompression/AppleEncryptedArchive/AEADecryptToStream.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wyL0Dk/Sources/ParallelCompression/AppleEncryptedArchive/AEADirectRandomAccessDecryptionStream.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wyL0Dk/Sources/ParallelCompression/AppleEncryptedArchive/AEAEncryptionStream.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wyL0Dk/Sources/ParallelCompression/AppleEncryptedArchive/AEAInplace.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wyL0Dk/Sources/ParallelCompression/AppleEncryptedArchive/AEAKeychain.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wyL0Dk/Sources/ParallelCompression/AppleEncryptedArchive/AEARandomAccessDecryptionStream.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wyL0Dk/Sources/ParallelCompression/AppleEncryptedArchive/AEASequentialDecryptionStream.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wyL0Dk/Sources/ParallelCompression/Common/BlobBuffer.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wyL0Dk/Sources/ParallelCompression/Common/ErrorCorrection.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wyL0Dk/Sources/ParallelCompression/Common/ErrorCorrection_ECC65537.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wyL0Dk/Sources/ParallelCompression/Common/IOBasicStreams.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wyL0Dk/Sources/ParallelCompression/Common/IOBuffers.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wyL0Dk/Sources/ParallelCompression/Common/IOCompressedStreams.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wyL0Dk/Sources/ParallelCompression/Common/ParallelCompressionAFSCStream.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wyL0Dk/Sources/ParallelCompression/Common/SharedArray.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wyL0Dk/Sources/ParallelCompression/Common/SharedBuffer.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wyL0Dk/Sources/ParallelCompression/Common/StringTable.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wyL0Dk/Sources/ParallelCompression/Common/ThreadPipeline.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wyL0Dk/Sources/ParallelCompression/Common/ThreadPool.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wyL0Dk/Sources/ParallelCompression/Common/Threads.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wyL0Dk/Sources/ParallelCompression/Common/Utils.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wyL0Dk/Sources/ParallelCompression/ParallelCompression/Filter.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wyL0Dk/Sources/ParallelCompression/ParallelDiff/BXDiff5.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wyL0Dk/Sources/ParallelCompression/ParallelDiff/BXDiffBase.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wyL0Dk/Sources/ParallelCompression/ParallelDiff/BXDiffControls.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wyL0Dk/Sources/ParallelCompression/ParallelDiff/BXDiffMatches.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wyL0Dk/Sources/ParallelCompression/ParallelDiff/ImageDiff/APFS/APFS.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wyL0Dk/Sources/ParallelCompression/ParallelDiff/ImageDiff/GenericArray.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wyL0Dk/Sources/ParallelCompression/ParallelDiff/ImageDiff/ImageDiff.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wyL0Dk/Sources/ParallelCompression/ParallelDiff/ImageDiff/ImageDiffInPlace.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wyL0Dk/Sources/ParallelCompression/ParallelDiff/ImageDiff/ImageOutputStream.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wyL0Dk/Sources/ParallelCompression/ParallelDiff/ImageDiff/ImagePatch.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wyL0Dk/Sources/ParallelCompression/ParallelDiff/ImageDiff/ImageStreams.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wyL0Dk/Sources/ParallelCompression/ParallelDiff/ImageDiff/InSituStream.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wyL0Dk/Sources/ParallelCompression/ParallelDiff/ImageDiff/RawImage.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wyL0Dk/Sources/ParallelCompression/ParallelDiff/LargeFile.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wyL0Dk/Sources/ParallelCompression/ParallelPatch/BXPatch5.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wyL0Dk/Sources/ParallelCompression/ParallelPatch/PagedFile.c"
+ "Invalid segment size in cluster header"
+ "bad donor for: %s"
+ "blob field size too large"
+ "cluster_id out of range"
+ "donor is not a regular file: %s"
+ "header payload too large"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.hd5tMA/Sources/ParallelCompression/AppleArchive/../Common/SharedArray.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.hd5tMA/Sources/ParallelCompression/AppleArchive/AAAFSCStream.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.hd5tMA/Sources/ParallelCompression/AppleArchive/AAArchiveFileStream.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.hd5tMA/Sources/ParallelCompression/AppleArchive/AAArchiveStream.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.hd5tMA/Sources/ParallelCompression/AppleArchive/AAArchiveStreamProcess.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.hd5tMA/Sources/ParallelCompression/AppleArchive/AAAssetBuilder.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.hd5tMA/Sources/ParallelCompression/AppleArchive/AAAssetDecodeStream.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.hd5tMA/Sources/ParallelCompression/AppleArchive/AAAssetDecompressionStream.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.hd5tMA/Sources/ParallelCompression/AppleArchive/AAAssetDecryptionStream.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.hd5tMA/Sources/ParallelCompression/AppleArchive/AAAssetExtractStream.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.hd5tMA/Sources/ParallelCompression/AppleArchive/AAAssetExtractor.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.hd5tMA/Sources/ParallelCompression/AppleArchive/AAAssetGenerate.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.hd5tMA/Sources/ParallelCompression/AppleArchive/AAAsyncByteStream.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.hd5tMA/Sources/ParallelCompression/AppleArchive/AAAsyncByteStreamProcessAllRanges.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.hd5tMA/Sources/ParallelCompression/AppleArchive/AAByteRange.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.hd5tMA/Sources/ParallelCompression/AppleArchive/AAByteStream.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.hd5tMA/Sources/ParallelCompression/AppleArchive/AAByteStreamProcess.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.hd5tMA/Sources/ParallelCompression/AppleArchive/AACacheStream.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.hd5tMA/Sources/ParallelCompression/AppleArchive/AAChunkAsyncStream.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.hd5tMA/Sources/ParallelCompression/AppleArchive/AAChunkInputStream.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.hd5tMA/Sources/ParallelCompression/AppleArchive/AAChunkOutputStream.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.hd5tMA/Sources/ParallelCompression/AppleArchive/AACompositeChunkAsyncStream.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.hd5tMA/Sources/ParallelCompression/AppleArchive/AACompressionStream.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.hd5tMA/Sources/ParallelCompression/AppleArchive/AAConvertArchiveOutputStream.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.hd5tMA/Sources/ParallelCompression/AppleArchive/AADecodeArchiveInputStream.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.hd5tMA/Sources/ParallelCompression/AppleArchive/AADecodeArchiveInputStreamCPIO.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.hd5tMA/Sources/ParallelCompression/AppleArchive/AADecodeArchiveInputStreamTar.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.hd5tMA/Sources/ParallelCompression/AppleArchive/AAEncodeArchiveOutputStream.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.hd5tMA/Sources/ParallelCompression/AppleArchive/AAExtractArchiveOutputStream.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.hd5tMA/Sources/ParallelCompression/AppleArchive/AAFieldACL.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.hd5tMA/Sources/ParallelCompression/AppleArchive/AAFieldKeys.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.hd5tMA/Sources/ParallelCompression/AppleArchive/AAFieldMCO.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.hd5tMA/Sources/ParallelCompression/AppleArchive/AAFieldXAT.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.hd5tMA/Sources/ParallelCompression/AppleArchive/AAFieldYEC.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.hd5tMA/Sources/ParallelCompression/AppleArchive/AAFieldYFP.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.hd5tMA/Sources/ParallelCompression/AppleArchive/AAGenericRandomAccessInputStream.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.hd5tMA/Sources/ParallelCompression/AppleArchive/AAHeader.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.hd5tMA/Sources/ParallelCompression/AppleArchive/AAInPlaceStream.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.hd5tMA/Sources/ParallelCompression/AppleArchive/AAJSONStreams.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.hd5tMA/Sources/ParallelCompression/AppleArchive/AAMemoryStream.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.hd5tMA/Sources/ParallelCompression/AppleArchive/AAPathFilter.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.hd5tMA/Sources/ParallelCompression/AppleArchive/AAPathList.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.hd5tMA/Sources/ParallelCompression/AppleArchive/AARandomAccessByteStreamProcess.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.hd5tMA/Sources/ParallelCompression/AppleArchive/AARandomAccessDecodeAndExtract.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.hd5tMA/Sources/ParallelCompression/AppleArchive/AARandomAccessDecompressionStream.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.hd5tMA/Sources/ParallelCompression/AppleArchive/AARangeInputStream.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.hd5tMA/Sources/ParallelCompression/AppleArchive/AARemoveArchiveOutputStream.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.hd5tMA/Sources/ParallelCompression/AppleArchive/AASequentialDecompressionStream.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.hd5tMA/Sources/ParallelCompression/AppleArchive/AATempStream.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.hd5tMA/Sources/ParallelCompression/AppleArchive/AAUtils.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.hd5tMA/Sources/ParallelCompression/AppleArchive/AAVerifyDirectoryArchiveOutputStream.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.hd5tMA/Sources/ParallelCompression/AppleEncryptedArchive/../AppleArchive/../Common/SharedArray.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.hd5tMA/Sources/ParallelCompression/AppleEncryptedArchive/AEAAuthData.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.hd5tMA/Sources/ParallelCompression/AppleEncryptedArchive/AEACommon.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.hd5tMA/Sources/ParallelCompression/AppleEncryptedArchive/AEAContainer.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.hd5tMA/Sources/ParallelCompression/AppleEncryptedArchive/AEAContext.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.hd5tMA/Sources/ParallelCompression/AppleEncryptedArchive/AEAContextValidate.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.hd5tMA/Sources/ParallelCompression/AppleEncryptedArchive/AEACrypto.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.hd5tMA/Sources/ParallelCompression/AppleEncryptedArchive/AEADecryptAndExtract.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.hd5tMA/Sources/ParallelCompression/AppleEncryptedArchive/AEADecryptAndExtractAsyncStream.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.hd5tMA/Sources/ParallelCompression/AppleEncryptedArchive/AEADecryptAsyncStream.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.hd5tMA/Sources/ParallelCompression/AppleEncryptedArchive/AEADecryptToFile.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.hd5tMA/Sources/ParallelCompression/AppleEncryptedArchive/AEADecryptToFileAsyncStream.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.hd5tMA/Sources/ParallelCompression/AppleEncryptedArchive/AEADecryptToStream.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.hd5tMA/Sources/ParallelCompression/AppleEncryptedArchive/AEADirectRandomAccessDecryptionStream.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.hd5tMA/Sources/ParallelCompression/AppleEncryptedArchive/AEAEncryptionStream.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.hd5tMA/Sources/ParallelCompression/AppleEncryptedArchive/AEAInplace.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.hd5tMA/Sources/ParallelCompression/AppleEncryptedArchive/AEAKeychain.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.hd5tMA/Sources/ParallelCompression/AppleEncryptedArchive/AEARandomAccessDecryptionStream.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.hd5tMA/Sources/ParallelCompression/AppleEncryptedArchive/AEASequentialDecryptionStream.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.hd5tMA/Sources/ParallelCompression/Common/BlobBuffer.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.hd5tMA/Sources/ParallelCompression/Common/ErrorCorrection.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.hd5tMA/Sources/ParallelCompression/Common/ErrorCorrection_ECC65537.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.hd5tMA/Sources/ParallelCompression/Common/IOBasicStreams.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.hd5tMA/Sources/ParallelCompression/Common/IOBuffers.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.hd5tMA/Sources/ParallelCompression/Common/IOCompressedStreams.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.hd5tMA/Sources/ParallelCompression/Common/ParallelCompressionAFSCStream.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.hd5tMA/Sources/ParallelCompression/Common/SharedArray.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.hd5tMA/Sources/ParallelCompression/Common/SharedBuffer.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.hd5tMA/Sources/ParallelCompression/Common/StringTable.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.hd5tMA/Sources/ParallelCompression/Common/ThreadPipeline.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.hd5tMA/Sources/ParallelCompression/Common/ThreadPool.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.hd5tMA/Sources/ParallelCompression/Common/Threads.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.hd5tMA/Sources/ParallelCompression/Common/Utils.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.hd5tMA/Sources/ParallelCompression/ParallelCompression/Filter.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.hd5tMA/Sources/ParallelCompression/ParallelDiff/BXDiff5.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.hd5tMA/Sources/ParallelCompression/ParallelDiff/BXDiffBase.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.hd5tMA/Sources/ParallelCompression/ParallelDiff/BXDiffControls.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.hd5tMA/Sources/ParallelCompression/ParallelDiff/BXDiffMatches.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.hd5tMA/Sources/ParallelCompression/ParallelDiff/ImageDiff/APFS/APFS.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.hd5tMA/Sources/ParallelCompression/ParallelDiff/ImageDiff/GenericArray.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.hd5tMA/Sources/ParallelCompression/ParallelDiff/ImageDiff/ImageDiff.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.hd5tMA/Sources/ParallelCompression/ParallelDiff/ImageDiff/ImageDiffInPlace.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.hd5tMA/Sources/ParallelCompression/ParallelDiff/ImageDiff/ImageOutputStream.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.hd5tMA/Sources/ParallelCompression/ParallelDiff/ImageDiff/ImagePatch.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.hd5tMA/Sources/ParallelCompression/ParallelDiff/ImageDiff/ImageStreams.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.hd5tMA/Sources/ParallelCompression/ParallelDiff/ImageDiff/InSituStream.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.hd5tMA/Sources/ParallelCompression/ParallelDiff/ImageDiff/RawImage.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.hd5tMA/Sources/ParallelCompression/ParallelDiff/LargeFile.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.hd5tMA/Sources/ParallelCompression/ParallelPatch/BXPatch5.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.hd5tMA/Sources/ParallelCompression/ParallelPatch/PagedFile.c"
- "link %s"
```
