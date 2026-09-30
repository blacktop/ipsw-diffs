## com.apple.fskit.msdos

> `/System/Library/ExtensionKit/Extensions/com.apple.fskit.msdos.appex/com.apple.fskit.msdos`

```diff

-720.40.1.0.0
-  __TEXT.__text: 0x32490
-  __TEXT.__auth_stubs: 0x850
-  __TEXT.__objc_stubs: 0x39e0
-  __TEXT.__objc_methlist: 0x1a60
-  __TEXT.__const: 0x4d85
-  __TEXT.__cstring: 0x3a49
-  __TEXT.__gcc_except_tab: 0x1acc
-  __TEXT.__objc_methname: 0x4345
-  __TEXT.__oslogstring: 0x2654
-  __TEXT.__objc_classname: 0x268
-  __TEXT.__objc_methtype: 0x178b
-  __TEXT.__unwind_info: 0x9c8
-  __DATA_CONST.__auth_got: 0x438
+720.60.14.0.0
+  __TEXT.__text: 0x320e0
+  __TEXT.__auth_stubs: 0x890
+  __TEXT.__objc_stubs: 0x3960
+  __TEXT.__objc_methlist: 0x1a28
+  __TEXT.__const: 0x4d95
+  __TEXT.__cstring: 0x3976
+  __TEXT.__gcc_except_tab: 0x1bd0
+  __TEXT.__objc_methname: 0x427d
+  __TEXT.__oslogstring: 0x28a2
+  __TEXT.__objc_classname: 0x273
+  __TEXT.__objc_methtype: 0x1746
+  __TEXT.__unwind_info: 0x968
+  __DATA_CONST.__auth_got: 0x458
   __DATA_CONST.__got: 0xf0
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0xdf8
+  __DATA_CONST.__const: 0xdb8
   __DATA_CONST.__cfstring: 0x600
   __DATA_CONST.__objc_classlist: 0xc8
   __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_superrefs: 0xa0
-  __DATA_CONST.__objc_arraydata: 0x8
-  __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA.__objc_const: 0x3e88
-  __DATA.__objc_selrefs: 0x1170
-  __DATA.__objc_ivar: 0x1bc
+  __DATA_CONST.__objc_superrefs: 0x98
+  __DATA.__objc_const: 0x3ee0
+  __DATA.__objc_selrefs: 0x1148
+  __DATA.__objc_ivar: 0x1b8
   __DATA.__objc_data: 0x7d0
   __DATA.__data: 0xa88
   __DATA.__common: 0x8c

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libutil.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 1064
-  Symbols:   338
-  CStrings:  1720
+  Functions: 1047
+  Symbols:   341
+  CStrings:  1721
 
Symbols:
+ _OBJC_CLASS_$_FSContainerIdentifier
+ ___snprintf_chk
+ _dispatch_async
+ _dispatch_get_global_queue
+ _objc_autorelease
- _OBJC_CLASS_$_NSConstantArray
- _OBJC_CLASS_$_NSMutableIndexSet
CStrings:
+ "%!s(MISSING): (allowPartial = %!d(MISSING)) %!u(MISSING) clusters requested,but only %!l(MISSING)lu are available. Returning ENOSPC."
+ "%!s(MISSING): (allowPartial = true) %!u(MISSING) clusters requested,but only %!l(MISSING)lu are available. Will try to allocate %!l(MISSING)lu clusters."
+ "%!s(MISSING): (offset = %!l(MISSING)lu) Failed to parse long-name entry's characters. Skipping entry."
+ "%!s(MISSING): (offset = %!l(MISSING)lu) First long-name entry doesn't have the WIN_LAST mask. Skipping entry."
+ "%!s(MISSING): (offset = %!l(MISSING)lu) Reached a short-name entry while we still have long-name entries left. Skipping entry."
+ "%!s(MISSING): (offset = %!l(MISSING)lu) long-name entry has an invalid checksum value. Skipping entry."
+ "%!s(MISSING): Got NULL dir entry from dir block"
+ "%!s(MISSING): Metadata flush failed (%!d(MISSING)), flags 0x%!l(MISSING)x"
+ "%!s(MISSING): This method should not be called after metaRW is enabled."
+ "%!s(MISSING): unexpected offset in dir block (%!l(MISSING)lu), dir block size %!z(MISSING)u"
+ "%!s(MISSING):done:error(%!@(MISSING))"
+ "+[Utilities syncMetaClearToDevice:rangesToClear:]"
+ "+[Utilities syncMetaPurgeToDevice:rangesToPurge:]"
+ "+[Utilities syncReadFromDevice:into:startingAt:length:]"
+ "-[DirBlock getBytesAtOffset:]"
+ "-[FATManager allocateClusters:searchFromCluster:allowPartial:zeroFill:mustBeContig:replyHandler:]_block_invoke_2"
+ "-[FATVolume enumerateDirectory:startingAtCookie:verifier:providingAttributes:usingPacker:replyHandler:]"
+ "-[FATVolume enumerateDirectory:startingAtCookie:verifier:providingAttributes:usingPacker:replyHandler:]_block_invoke"
+ "-[FATVolume preallocateSpaceForItem:offset:length:flags:usingPacker:replyHandler:]"
+ "-[FATVolume preallocateSpaceForItem:offset:length:flags:usingPacker:replyHandler:]_block_invoke"
+ "-[FATVolume synchronizeWithFlags:replyHandler:]"
+ "-[FileItem fetchFileExtentsFrom:to:usingBlocks:replyHandler:]"
+ "-[MsdosDirItem iterateFromOffset:options:replyHandler:]_block_invoke"
+ "-[msdosFileSystem startCheckWithTask:parameters:error:]"
+ "-[msdosFileSystem startFormatWithTask:parameters:error:]"
+ "-[msdosFileSystem startFormatWithTask:parameters:error:]_block_invoke"
+ "-[msdosFileSystem syncRead:into:startingAt:length:]"
+ "@\"NSProgress\"40@0:8@\"FSTask\"16@\"NSArray\"24^@32"
+ "@40@0:8@16@24^@32"
+ "FSVolumeKernelOffloadedIOOperations"
+ "TB,?,GareXattrOperationsInhibited"
+ "TB,?,GisPreallocateInhibited"
+ "TB,?,GisVolumeRenameInhibited"
+ "TB,R"
+ "Tq,?,R"
+ "Tq,R"
+ "areXattrOperationsInhibited"
+ "asynchronousMetadataFlush"
+ "didCompleteWithError:"
+ "enumerateDirectory:startingAtCookie:verifier:providingAttributes:usingPacker:replyHandler:"
+ "fetchFileExtentsFrom:to:usingBlocks:replyHandler:"
+ "fs_posixCode"
+ "getXattrNamed:ofItem:replyHandler:"
+ "isAttributeWanted:"
+ "isPreallocateInhibited"
+ "isVolumeRenameInhibited"
+ "maximumFileSize"
+ "maximumFileSizeInBits"
+ "maximumLinkCount"
+ "maximumNameLength"
+ "maximumXattrSize"
+ "maximumXattrSizeInBits"
+ "metadataClear:wait:"
+ "metadataFlush"
+ "metadataPurge:"
+ "metadataReadInto:startingAt:length:"
+ "metadataWriteFrom:startingAt:length:"
+ "preallocateInhibited"
+ "preallocateSpaceForItem:offset:length:flags:usingPacker:replyHandler:"
+ "readInto:startingAt:length:error:"
+ "setCaseSensitivity:"
+ "setFileSystemSubType:"
+ "setInhibitKernelOffloadedIO:"
+ "setPreallocateInhibited:"
+ "setVolumeRenameInhibited:"
+ "startCheckWithTask:parameters:error:"
+ "startFormatWithTask:parameters:error:"
+ "synchronizeWithFlags:replyHandler:"
+ "truncatesLongNames"
+ "v48@0:8Q16Q24@?32@?40"
+ "volumeRenameInhibited"
+ "wipeResource:completionHandler:"
+ "writeFrom:startingAt:length:error:"
- "\x03"
- "%!s(MISSING): Failed to flush meta cache, error %!@(MISSING)"
- "%!s(MISSING): Finished launching"
- "%!s(MISSING): Finished loading"
- "%!s(MISSING): No probeResult cached, probe to find volumeID"
- "%!s(MISSING): uNeedToAllocClusters %!u(MISSING), uAmountOfAllocatedClusters %!u(MISSING) iErr %!@(MISSING)"
- "+[Utilities metaWriteToDevice:from:startingAt:length:]_block_invoke"
- "+[Utilities metaWriteToDevice:from:startingAt:length:]_block_invoke_2"
- "+[Utilities syncMetaClearToDevice:rangesToClear:]_block_invoke"
- "+[Utilities syncMetaPurgeToDevice:rangesToPurge:]_block_invoke"
- "+[Utilities syncMetaReadFromDevice:into:startingAt:length:]_block_invoke"
- "+[Utilities syncReadFromDevice:into:startingAt:length:]_block_invoke"
- "-[FATVolume enumerateDirectory:startingAtCookie:verifier:providingAttributes:usingBlock:replyHandler:]"
- "-[FATVolume enumerateDirectory:startingAtCookie:verifier:providingAttributes:usingBlock:replyHandler:]_block_invoke"
- "-[FATVolume preallocate:offset:length:flags:usingPacker:replyHandler:]"
- "-[FATVolume preallocate:offset:length:flags:usingPacker:replyHandler:]_block_invoke"
- "-[FATVolume synchronizeWithReplyHandler:]"
- "-[FATVolume synchronizeWithReplyHandler:]_block_invoke_2"
- "-[FileItem fetchFileExtentsFrom:to:lastValidOffset:usingBlocks:replyHandler:]"
- "-[FileItem preallocate:allowPartial:mustBeContig:replyHandler:]"
- "-[msdosFileSystem checkWithParameters:connection:taskID:replyHandler:]"
- "-[msdosFileSystem didFinishLaunching]"
- "-[msdosFileSystem didFinishLoading]"
- "-[msdosFileSystem formatWithParameters:connection:taskID:replyHandler:]"
- "-[msdosFileSystem syncRead:into:startingAt:length:]_block_invoke"
- "@\"FSProbeResult\""
- "FSVolumeKOIOOperations"
- "T@\"FSProbeResult\",&,V_probeResult"
- "TB,?"
- "TB,R,GisLongNameTruncated"
- "Ti,R"
- "_probeResult"
- "addIndexesInRange:"
- "checkWithParameters:connection:taskID:replyHandler:"
- "didCompleteWithError:completionHandler:"
- "didFinishLaunching"
- "enumerateDirectory:startingAtCookie:verifier:providingAttributes:usingBlock:replyHandler:"
- "fetchFileExtentsFrom:to:lastValidOffset:usingBlocks:replyHandler:"
- "formatWithParameters:connection:taskID:replyHandler:"
- "fs_containerIdentifier"
- "indexSet"
- "initWithBlockDevice:"
- "isLongNameTruncated"
- "isWanted:"
- "islongNameTruncated"
- "longNameTruncated"
- "maxXattrSizeInBits"
- "preallocate:offset:length:flags:usingPacker:replyHandler:"
- "preallocateOperationsInhibited"
- "probeResult"
- "setFilesystemSubType:"
- "setInhibitKOIO:"
- "setPreallocateOperationsInhibited:"
- "setProbeResult:"
- "setSupportsCasePreservingNames:"
- "setVolumeRenameOperationsInhibited:"
- "synchronizeWithReplyHandler:"
- "synchronousMetadataClear:wait:replyHandler:"
- "synchronousMetadataFlushWithReplyHandler:"
- "synchronousMetadataPurge:replyHandler:"
- "synchronousMetadataReadInto:startingAt:length:replyHandler:"
- "synchronousMetadataWriteFrom:startingAt:length:replyHandler:"
- "synchronousReadInto:startingAt:length:replyHandler:"
- "synchronousWriteFrom:startingAt:length:replyHandler:"
- "v24@0:8@?<v@?@\"NSError\">16"
- "v24@?0Q8@\"NSError\"16"
- "v48@0:8@\"NSArray\"16@\"FSMessageConnection\"24@\"NSUUID\"32@?<v@?@\"NSProgress\"@\"NSError\">40"
- "v56@0:8Q16Q24Q32@?40@?48"
- "volumeRenameOperationsInhibited"
- "wasConsumed:"
- "wipeResource:includingRanges:excludingRanges:completionHandler:"
- "xattrNamed:ofItem:replyHandler:"

```
