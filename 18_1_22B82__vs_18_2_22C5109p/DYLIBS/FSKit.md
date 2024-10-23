## FSKit

> `/System/Library/PrivateFrameworks/FSKit.framework/FSKit`

```diff

-470.40.4.0.0
-  __TEXT.__text: 0x38cb4
-  __TEXT.__auth_stubs: 0xb40
-  __TEXT.__objc_methlist: 0x3444
-  __TEXT.__const: 0x388
-  __TEXT.__gcc_except_tab: 0xf00
-  __TEXT.__cstring: 0x3e52
-  __TEXT.__oslogstring: 0x26a6
+474.60.39.0.0
+  __TEXT.__text: 0x39940
+  __TEXT.__auth_stubs: 0xb70
+  __TEXT.__objc_methlist: 0x360c
+  __TEXT.__const: 0x368
+  __TEXT.__gcc_except_tab: 0xd94
+  __TEXT.__cstring: 0x3de5
+  __TEXT.__oslogstring: 0x294b
   __TEXT.__swift5_typeref: 0x16c
   __TEXT.__swift5_reflstr: 0x16
   __TEXT.__swift5_assocty: 0x48

   __TEXT.__constg_swiftt: 0x210
   __TEXT.__swift5_protos: 0x8
   __TEXT.__swift5_types: 0x8
-  __TEXT.__unwind_info: 0x1168
-  __TEXT.__objc_classname: 0x7f9
-  __TEXT.__objc_methname: 0x8b05
-  __TEXT.__objc_methtype: 0x30cc
-  __TEXT.__objc_stubs: 0x4f00
-  __DATA_CONST.__got: 0x3b8
-  __DATA_CONST.__const: 0x1358
-  __DATA_CONST.__objc_classlist: 0x1f0
-  __DATA_CONST.__objc_catlist: 0x20
+  __TEXT.__unwind_info: 0x1100
+  __TEXT.__objc_classname: 0x81c
+  __TEXT.__objc_methname: 0x8cf8
+  __TEXT.__objc_methtype: 0x3197
+  __TEXT.__objc_stubs: 0x50e0
+  __DATA_CONST.__got: 0x3c0
+  __DATA_CONST.__const: 0x1378
+  __DATA_CONST.__objc_classlist: 0x200
+  __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x140
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1f20
+  __DATA_CONST.__objc_selrefs: 0x1fd0
   __DATA_CONST.__objc_protorefs: 0xe8
-  __DATA_CONST.__objc_superrefs: 0x158
+  __DATA_CONST.__objc_superrefs: 0x168
   __DATA_CONST.__objc_arraydata: 0x30
-  __AUTH_CONST.__auth_got: 0x5b0
+  __AUTH_CONST.__auth_got: 0x5c8
   __AUTH_CONST.__auth_ptr: 0x60
-  __AUTH_CONST.__const: 0x528
-  __AUTH_CONST.__cfstring: 0x1ca0
-  __AUTH_CONST.__objc_const: 0x7c78
+  __AUTH_CONST.__const: 0x450
+  __AUTH_CONST.__cfstring: 0x1ce0
+  __AUTH_CONST.__objc_const: 0x7ff0
   __AUTH_CONST.__objc_arrayobj: 0x30
-  __AUTH.__objc_data: 0x1090
+  __AUTH.__objc_data: 0x1130
   __AUTH.__data: 0x80
-  __DATA.__objc_ivar: 0x3c4
+  __DATA.__objc_ivar: 0x3d4
   __DATA.__data: 0xf60
   __DATA.__bss: 0x320
   __DATA_DIRTY.__objc_data: 0x410

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 1696
-  Symbols:   2091
-  CStrings:  2654
+  Functions: 1719
+  Symbols:   2123
+  CStrings:  2716
 
Symbols:
+ _OBJC_CLASS_$_FSFileHandle
+ _OBJC_CLASS_$_FSTask
+ _OBJC_METACLASS_$_FSFileHandle
+ _OBJC_METACLASS_$_FSTask
+ ___memcpy_chk
+ _log2
+ _swift_willThrow
CStrings:
+ "\x17"
+ "%!s(MISSING): Given fromDirectory item is not a directory (type = %!l(MISSING)u). Error = %!d(MISSING)."
+ "%!s(MISSING): Given fromItem is a directory, but toItem is not a directory. Error = %!d(MISSING)."
+ "%!s(MISSING): Given fromItem is not a directory, but toItem is a directory. Error = %!d(MISSING)."
+ "%!s(MISSING): Given item is not a directory (type = %!l(MISSING)u). Error = %!d(MISSING)."
+ "%!s(MISSING): Given item is not a file (type = %!l(MISSING)u). Error = %!d(MISSING)."
+ "%!s(MISSING): Given item is not a symlink (type = %!l(MISSING)u). Error = %!d(MISSING)."
+ "%!s(MISSING): Given parent item is not a directory (type = %!l(MISSING)u). Error = %!d(MISSING)."
+ "%!s(MISSING): Given toDirectory item is not a directory (type = %!l(MISSING)u). Error = %!d(MISSING)."
+ "%!s(MISSING): Volume does not implement both maxFileSizeInBits and maxFileSize, while one of them must be implemented."
+ "%!s(MISSING): Volume does not implement both maxXattrSizeInBits and maxXattrSize, while one of them must be implemented."
+ "%!s(MISSING): delegate doesn't have startCheckWithTask:parameters:error: method, try checkResource"
+ "%!s(MISSING): delegate doesn't have startFormatWithTask:parameters:error: method, try formatResource"
+ "%!s(MISSING): flushMeta failed, status: %!d(MISSING)"
+ "%!s(MISSING):EINVAL: readAheadExtentsCount is 0, returning EINVAL"
+ "+[FSFileSystemBasis wipeResource:extension:completionHandler:]"
+ "-[FSBlockDeviceResource asynchronousMetadataFlush]"
+ "-[FSBlockDeviceResource metadataClear:wait:]"
+ "-[FSBlockDeviceResource metadataFlush]"
+ "-[FSBlockDeviceResource metadataPurge:]"
+ "-[FSBlockDeviceResource metadataReadInto:startingAt:length:readAheadExtents:readAheadCount:]"
+ "-[FSModuleConnector sendWipeResource:replyHandler:]"
+ "-[FSModuleConnector sendWipeResource:replyHandler:]_block_invoke"
+ "-[FSModuleExtension(Project) sendWipeResource:replyHandler:]"
+ "-[FSModuleVolume fetchAndSetTypeForItem:]_block_invoke"
+ "-[FSModuleVolume getMaxFileSizeInBits]"
+ "-[FSModuleVolume getMaxXattrSizeInBits]"
+ "@\"FSFileHandle\""
+ "@\"FSMessageConnection\""
+ "@\"NSProgress\"40@0:8@\"FSTask\"16@\"NSArray\"24^@32"
+ "@16@?0@\"FSFileName\"8"
+ "@24@0:8q16"
+ "@40@0:8^v16q24Q32"
+ "@56@0:8^v16q24Q32r^{?=qQ}40q48"
+ "Delegate class %!@(MISSING) doesn't support probeResource:replyHandler:"
+ "FSFileHandle"
+ "FSFileHandle.value"
+ "FSKit._FSKitFileSystemExtensionConfiguration"
+ "FSKit._FSKitUnaryFileSystemExtensionConfiguration"
+ "FSKitStatFSResult:totalBytes(%!l(MISSING)d):availableBytes(%!l(MISSING)d):freeBytes(%!l(MISSING)d):totalFiles(%!l(MISSING)d):freeFiles(%!l(MISSING)d)"
+ "FSTask"
+ "FSTask.MessageConnection"
+ "FSTask.TaskID"
+ "FSVolumeKernelOffloadedIOOperations"
+ "Initial enumeration of file system modules"
+ "Q48@0:8^v16q24Q32^@40"
+ "T@\"FSFileHandle\",&,V_fileHandle"
+ "T@\"FSFileHandle\",R,C,N"
+ "T@\"FSMessageConnection\",R"
+ "T@\"FSMessageConnection\",R,V_connection"
+ "T@\"NSData\",C,V_qualifier"
+ "T@\"NSString\",R,C,N"
+ "T@\"NSString\",R,C,V_fileSystemTypeName"
+ "T@\"NSUUID\",C,V_uuid"
+ "T@\"NSUUID\",R"
+ "T@\"NSUUID\",R,V_taskID"
+ "T@?,C,V_lateCompletedBlock"
+ "TB,?,GareXattrOperationsInhibited"
+ "TB,?,GisAccessCheckInhibited"
+ "TB,?,GisOpenCloseInhibited"
+ "TB,?,GisPreallocateInhibited"
+ "TB,?,GisVolumeRenameInhibited"
+ "TQ,N,V_caseSensitivity"
+ "TQ,N,V_value"
+ "Tq,N,V_type"
+ "Tq,V_availableBlocks"
+ "Tq,V_availableBytes"
+ "Tq,V_blockSize"
+ "Tq,V_fileSystemSubType"
+ "Tq,V_freeBlocks"
+ "Tq,V_freeBytes"
+ "Tq,V_freeFiles"
+ "Tq,V_ioSize"
+ "Tq,V_totalBlocks"
+ "Tq,V_totalBytes"
+ "Tq,V_totalFiles"
+ "Tq,V_usedBlocks"
+ "Tq,V_usedBytes"
+ "_TtC5FSKit38_FSKitFileSystemExtensionConfiguration"
+ "_TtC5FSKit43_FSKitUnaryFileSystemExtensionConfiguration"
+ "_caseSensitivity"
+ "_fileSystemSubType"
+ "_fileSystemTypeName"
+ "_lateCompletedBlock"
+ "_type"
+ "_value"
+ "accessCheckInhibited"
+ "areXattrOperationsInhibited"
+ "asynchronousMetadataFlush"
+ "base64EncodedStringWithOptions:"
+ "base64String"
+ "caseSensitivity"
+ "delayedMetadataWriteFrom:startingAt:length:"
+ "didCompleteWithError:"
+ "enumerateDirectory:startingAtCookie:verifier:providingAttributes:usingPacker:replyHandler:"
+ "fetchAndSetTypeForItem:"
+ "file system extension backpointer loaded"
+ "fileSystemSubType"
+ "fileSystemTypeName"
+ "fsFileHandle"
+ "fs_posixCode"
+ "getMaxFileSizeInBits"
+ "getMaxXattrSizeInBits"
+ "getStandardItemAttributesDataForNewItem:"
+ "getXattrNamed:ofItem:replyHandler:"
+ "inhibitKernelOffloadedIO"
+ "initWithBase64:"
+ "initWithBase64EncodedString:options:"
+ "initWithBase64Encoding:"
+ "initWithMessageConnection:taskID:"
+ "initWithValue:"
+ "isAccessCheckInhibited"
+ "isAttributeWanted:"
+ "isOpenCloseInhibited"
+ "isPreallocateInhibited"
+ "isVolumeRenameInhibited"
+ "lateCompletedBlock"
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
+ "metadataReadInto:startingAt:length:readAheadExtents:readAheadCount:"
+ "metadataWriteFrom:startingAt:length:"
+ "metadataWriteFrom:startingAt:length:completionHandler:"
+ "openCloseInhibited"
+ "preallocateInhibited"
+ "preallocateSpaceForItem:offset:length:flags:usingPacker:replyHandler:"
+ "readInto:startingAt:length:completionHandler:"
+ "readInto:startingAt:length:error:"
+ "sendWipeResource:replyHandler:"
+ "setAccessCheckInhibited:"
+ "setCaseSensitivity:"
+ "setFileSystemSubType:"
+ "setInhibitKernelOffloadedIO:"
+ "setLateCompletedBlock:"
+ "setOpenCloseInhibited:"
+ "setPreallocateInhibited:"
+ "setValue:"
+ "setVolumeRenameInhibited:"
+ "startCheckWithTask:parameters:error:"
+ "startFormatWithTask:parameters:error:"
+ "synchronize:replyHandler:"
+ "synchronizeWithFlags:replyHandler:"
+ "truncatesLongNames"
+ "v24@0:8@?<v@?@\"FSFileHandle\"@\"NSError\">16"
+ "v28@0:8I16@?20"
+ "v28@0:8I16@?<v@?@\"NSError\">20"
+ "v40@0:8@\"FSFileHandle\"16Q24@?<v@?i@\"FSStatFSResult\">32"
+ "v40@0:8@\"FSFileHandle\"16Q24@?<v@?i@\"NSArray\">32"
+ "v40@0:8@\"FSFileHandle\"16Q24@?<v@?i@\"NSData\">32"
+ "v40@0:8@\"FSFileHandle\"16Q24@?<v@?i@\"NSData\"@\"NSData\">32"
+ "v44@0:8@\"FSFileHandle\"16B24Q28@?<v@?@\"NSError\">36"
+ "v44@0:8@\"FSFileHandle\"16i24Q28@?<v@?i>36"
+ "v44@0:8@\"FSFileHandle\"16i24Q28@?<v@?ii>36"
+ "v48@0:8@\"FSFileHandle\"16@\"FSFileName\"24Q32@?<v@?i@\"NSData\">40"
+ "v48@0:8@\"FSFileHandle\"16@\"NSData\"24Q32@?<v@?i@\"NSData\"Q@\"NSData\">40"
+ "v48@0:8@\"FSFileHandle\"16Q24Q32@?<v@?i>40"
+ "v48@0:8@\"FSFileHandle\"16Q24Q32@?<v@?i@\"NSData\">40"
+ "v48@0:8@\"NSData\"16@\"FSItem\"24q32@?<v@?Q@\"NSError\">40"
+ "v48@0:8@16@24q32@?40"
+ "v52@0:8@\"FSFileHandle\"16@\"FSFileName\"24I32Q36@?<v@?ii@\"FSFileHandle\"@\"NSData\"@\"FSFileHandle\"@\"NSData\"@\"NSString\"@\"NSData\"@\"NSData\">44"
+ "v56@0:8@\"FSFileHandle\"16@\"FSFileName\"24@\"FSFileHandle\"32Q40@?<v@?i@\"NSData\"@\"NSData\"@\"NSData\">48"
+ "v56@0:8@\"FSFileHandle\"16@\"FSFileName\"24@\"NSData\"32Q40@?<v@?i@\"NSData\"@\"NSData\">48"
+ "v56@0:8@\"FSFileHandle\"16Q24@\"FSMutableFileDataBuffer\"32Q40@?<v@?iQ>48"
+ "v56@0:8@\"FSFileHandle\"16Q24@\"NSData\"32Q40@?<v@?iQ@\"NSData\">48"
+ "v56@0:8@\"FSItem\"16q24Q32@\"NSMutableData\"40@?<v@?Q@\"NSError\">48"
+ "v56@0:8@16q24Q32@40@?48"
+ "v60@0:8@\"FSFileHandle\"16@\"FSFileHandle\"24@\"FSFileName\"32i40Q44@?<v@?i@\"NSData\"@\"NSData\">52"
+ "v60@0:8@\"FSFileHandle\"16@\"FSFileHandle\"24@\"FSFileName\"32i40Q44@?<v@?i@\"NSData\"@\"NSData\"@\"NSData\">52"
+ "v64@0:8@\"FSFileHandle\"16@\"FSFileName\"24@\"NSData\"32@\"NSData\"40Q48@?<v@?i@\"NSData\"@\"FSFileHandle\"@\"NSData\"@\"NSData\">56"
+ "v64@0:8@\"FSFileHandle\"16@\"FSFileName\"24@\"NSData\"32Q40Q48@?<v@?i>56"
+ "v64@0:8@\"FSFileHandle\"16@\"FSFileName\"24q32@\"NSData\"40Q48@?<v@?i@\"NSData\"@\"FSFileHandle\"@\"NSData\"@\"NSData\">56"
+ "v64@0:8@\"FSFileHandle\"16@\"FSMutableFileDataBuffer\"24Q32Q40Q48@?<v@?iqQ>56"
+ "v64@0:8@\"FSFileHandle\"16{_NSRange=QQ}24i40I44Q48@?<v@?i>56"
+ "v64@0:8@\"FSFileHandle\"16{_NSRange=QQ}24i40I44Q48@?<v@?i@\"NSData\"@\"NSData\">56"
+ "v68@0:8@\"FSFileHandle\"16@\"FSFileName\"24@\"FSFileHandle\"32@\"NSData\"40I48Q52@?<v@?i@\"NSData\"@\"FSFileHandle\"@\"NSData\"@\"NSData\">60"
+ "v72@0:8@\"FSFileHandle\"16Q24@\"FSMutableFileDataBuffer\"32Q40Q48Q56@?<v@?iqQ>64"
+ "v80@0:8@\"FSFileHandle\"16@\"NSString\"24@\"NSDictionary\"32@\"NSString\"40I48d52I60Q64@?<v@?i>72"
+ "v84@0:8@\"FSFileHandle\"16@\"FSFileName\"24@\"FSFileHandle\"32@\"FSFileHandle\"40@\"FSFileName\"48@\"FSFileHandle\"56I64Q68@?<v@?i@\"NSData\"@\"NSData\"@\"NSData\"@\"NSData\"@\"NSData\">76"
+ "value"
+ "volumeRenameInhibited"
+ "wasAttributeConsumed:"
+ "wipeFS:replyHandler:"
+ "wipeResource:completionHandler:"
+ "wipeResource:extension:completionHandler:"
+ "wipeResource:reply:"
+ "wipeResource:replyHandler:"
+ "writeFrom:startingAt:length:completionHandler:"
+ "writeFrom:startingAt:length:error:"
- "%!l(MISSING)lu"
- "%!s(MISSING): Volume doesn't implement maxXattrBits"
- "%!s(MISSING): delegate doesn't have checkWithOptions method, try checkResource"
- "%!s(MISSING): delegate doesn't have formatWithParameters method, try formatResource"
- "%!s(MISSING):reply:EINVAL: readAheadExtentsCount is 0, returning EINVAL"
- "+[FSFileSystemBasis wipeResource:includingRanges:excludingRanges:extension:completionHandler:]"
- "-[FSBlockDeviceResource synchronousMetadataClear:wait:replyHandler:]"
- "-[FSBlockDeviceResource synchronousMetadataFlushWithReplyHandler:]"
- "-[FSBlockDeviceResource synchronousMetadataPurge:replyHandler:]"
- "-[FSBlockDeviceResource synchronousMetadataReadInto:startingAt:length:readAheadExtents:readAheadCount:replyHandler:]"
- "-[FSModuleConnector sendWipeResource:includingBlockRanges:excludingBlockRanges:replyHandler:]"
- "-[FSModuleConnector sendWipeResource:includingBlockRanges:excludingBlockRanges:replyHandler:]_block_invoke"
- "-[FSModuleExtension(Project) sendWipeResource:includingBlockRanges:excludingBlockRanges:replyHandler:]"
- "-[FSVolumeConnector listXattrsOf:requestID:replyHandler:]_block_invoke"
- "Delegate class %!@(MISSING) doesn't surpport probeResource:replyHandler:"
- "FSKit._FSKitFilesystemExtensionConfiguration"
- "FSKit._FSKitUnaryFilesystemExtensionConfiguration"
- "FSKitStatFSResult:totalBytes(%!l(MISSING)lu):availableBytes(%!l(MISSING)lu):freeBytes(%!l(MISSING)lu):totalFiles(%!l(MISSING)lu):freeFiles(%!l(MISSING)lu)"
- "FSModule %!{(MISSING)public}@ checkWithOptions: did NOT call reply()"
- "FSModule %!{(MISSING)public}@ format: did NOT call reply()"
- "FSVolumeKOIOOperations"
- "FileHandleForFileID:"
- "Initial enumeration of filesystem modules"
- "T@\"FSVolumeIdentifier\",R"
- "T@\"NSData\",&,V_fileHandle"
- "T@\"NSData\",&,V_qualifier"
- "T@\"NSString\",R,C,V_filesystemTypeName"
- "T@\"NSUUID\",&,V_uuid"
- "TB,?"
- "TB,N,V_supportsCasePreservingNames"
- "TB,N,V_supportsCaseSensitiveNames"
- "TI,V_filesystemSubType"
- "TQ,V_availableBlocks"
- "TQ,V_availableBytes"
- "TQ,V_blockSize"
- "TQ,V_freeBlocks"
- "TQ,V_freeBytes"
- "TQ,V_freeFiles"
- "TQ,V_ioSize"
- "TQ,V_totalBlocks"
- "TQ,V_totalBytes"
- "TQ,V_totalFiles"
- "TQ,V_usedBlocks"
- "TQ,V_usedBytes"
- "_TtC5FSKit38_FSKitFilesystemExtensionConfiguration"
- "_TtC5FSKit43_FSKitUnaryFilesystemExtensionConfiguration"
- "_filesystemSubType"
- "_filesystemTypeName"
- "_supportsCasePreservingNames"
- "_supportsCaseSensitiveNames"
- "accessCheckOperationsInhibited"
- "checkWithParameters:connection:taskID:replyHandler:"
- "delayedMetadataWriteFrom:startingAt:length:replyHandler:"
- "enumerateDirectory:startingAtCookie:verifier:providingAttributes:usingBlock:replyHandler:"
- "filesystem extension backpointer loaded"
- "filesystemSubType"
- "filesystemTypeName"
- "formatWithParameters:connection:taskID:replyHandler:"
- "inhibitKOIO"
- "isLongNameTruncated"
- "isWanted:"
- "maxFileSizeInBits"
- "maxLinkCount"
- "maxNameLength"
- "maxXattrSizeInBits"
- "metadataWriteFrom:startingAt:length:replyHandler:"
- "preallocate:offset:length:flags:usingPacker:replyHandler:"
- "preallocateOperationsInhibited"
- "readInto:startingAt:length:replyHandler:"
- "sendWipeResource:includingBlockRanges:excludingBlockRanges:replyHandler:"
- "setAccessCheckOperationsInhibited:"
- "setFilesystemSubType:"
- "setInhibitKOIO:"
- "setPreallocateOperationsInhibited:"
- "setSupportsCasePreservingNames:"
- "setSupportsCaseSensitiveNames:"
- "setVolumeRenameOperationsInhibited:"
- "supportsCasePreservingNames"
- "supportsCaseSensitiveNames"
- "synchronize:"
- "synchronizeWithReplyHandler:"
- "synchronousMetadataClear:wait:replyHandler:"
- "synchronousMetadataFlushWithReplyHandler:"
- "synchronousMetadataPurge:replyHandler:"
- "synchronousMetadataReadInto:startingAt:length:readAheadExtents:readAheadCount:replyHandler:"
- "synchronousMetadataReadInto:startingAt:length:replyHandler:"
- "synchronousMetadataWriteFrom:startingAt:length:replyHandler:"
- "synchronousWriteFrom:startingAt:length:replyHandler:"
- "v24@0:8@?<v@?@\"NSData\"@\"NSError\">16"
- "v24@?0@\"NSProgress\"8@\"NSError\"16"
- "v40@0:8@\"NSData\"16Q24@?<v@?i@\"FSStatFSResult\">32"
- "v40@0:8@\"NSData\"16Q24@?<v@?i@\"NSArray\">32"
- "v40@0:8@\"NSData\"16Q24@?<v@?i@\"NSData\">32"
- "v40@0:8@\"NSData\"16Q24@?<v@?i@\"NSData\"@\"NSData\">32"
- "v44@0:8@\"NSData\"16B24Q28@?<v@?@\"NSError\">36"
- "v44@0:8@\"NSData\"16i24Q28@?<v@?i>36"
- "v44@0:8@\"NSData\"16i24Q28@?<v@?ii>36"
- "v48@0:8@\"FSBlockDeviceResource\"16@\"NSIndexSet\"24@\"NSIndexSet\"32@?<v@?@\"NSError\">40"
- "v48@0:8@\"FSResource\"16@\"NSIndexSet\"24@\"NSIndexSet\"32@?<v@?@\"NSError\">40"
- "v48@0:8@\"NSArray\"16@\"FSMessageConnection\"24@\"NSUUID\"32@?<v@?@\"NSProgress\"@\"NSError\">40"
- "v48@0:8@\"NSData\"16@\"FSFileName\"24Q32@?<v@?i@\"NSData\">40"
- "v48@0:8@\"NSData\"16@\"FSItem\"24Q32@?<v@?Q@\"NSError\">40"
- "v48@0:8@\"NSData\"16@\"NSData\"24Q32@?<v@?i@\"NSData\"Q@\"NSData\">40"
- "v48@0:8@\"NSData\"16Q24Q32@?<v@?i>40"
- "v48@0:8@\"NSData\"16Q24Q32@?<v@?i@\"NSData\">40"
- "v52@0:8@\"NSData\"16@\"FSFileName\"24I32Q36@?<v@?ii@\"NSData\"@\"NSData\"@\"NSData\"@\"NSData\"@\"NSString\"@\"NSData\"@\"NSData\">44"
- "v56@0:8@\"FSItem\"16Q24Q32@\"NSMutableData\"40@?<v@?Q@\"NSError\">48"
- "v56@0:8@\"NSData\"16@\"FSFileName\"24@\"NSData\"32Q40@?<v@?i@\"NSData\"@\"NSData\">48"
- "v56@0:8@\"NSData\"16@\"FSFileName\"24@\"NSData\"32Q40@?<v@?i@\"NSData\"@\"NSData\"@\"NSData\">48"
- "v56@0:8@\"NSData\"16Q24@\"FSMutableFileDataBuffer\"32Q40@?<v@?iQ>48"
- "v56@0:8@\"NSData\"16Q24@\"NSData\"32Q40@?<v@?iQ@\"NSData\">48"
- "v56@0:8@16Q24Q32@40@?48"
- "v60@0:8@\"NSData\"16@\"NSData\"24@\"FSFileName\"32i40Q44@?<v@?i@\"NSData\"@\"NSData\">52"
- "v60@0:8@\"NSData\"16@\"NSData\"24@\"FSFileName\"32i40Q44@?<v@?i@\"NSData\"@\"NSData\"@\"NSData\">52"
- "v64@0:8@\"NSData\"16@\"FSFileName\"24@\"NSData\"32@\"NSData\"40Q48@?<v@?i@\"NSData\"@\"NSData\"@\"NSData\"@\"NSData\">56"
- "v64@0:8@\"NSData\"16@\"FSFileName\"24@\"NSData\"32Q40Q48@?<v@?i>56"
- "v64@0:8@\"NSData\"16@\"FSFileName\"24q32@\"NSData\"40Q48@?<v@?i@\"NSData\"@\"NSData\"@\"NSData\"@\"NSData\">56"
- "v64@0:8@\"NSData\"16@\"FSMutableFileDataBuffer\"24Q32Q40Q48@?<v@?iqQ>56"
- "v64@0:8@\"NSData\"16{_NSRange=QQ}24i40I44Q48@?<v@?i>56"
- "v64@0:8@\"NSData\"16{_NSRange=QQ}24i40I44Q48@?<v@?i@\"NSData\"@\"NSData\">56"
- "v64@0:8^v16q24Q32r^{?=qQ}40q48@?56"
- "v68@0:8@\"NSData\"16@\"FSFileName\"24@\"NSData\"32@\"NSData\"40I48Q52@?<v@?i@\"NSData\"@\"NSData\"@\"NSData\"@\"NSData\">60"
- "v72@0:8@\"NSData\"16Q24@\"FSMutableFileDataBuffer\"32Q40Q48Q56@?<v@?iqQ>64"
- "v80@0:8@\"NSData\"16@\"NSString\"24@\"NSDictionary\"32@\"NSString\"40I48d52I60Q64@?<v@?i>72"
- "v84@0:8@\"NSData\"16@\"FSFileName\"24@\"NSData\"32@\"NSData\"40@\"FSFileName\"48@\"NSData\"56I64Q68@?<v@?i@\"NSData\"@\"NSData\"@\"NSData\"@\"NSData\"@\"NSData\">76"
- "volumeRenameOperationsInhibited"
- "wasConsumed:"
- "wipeFS:includingRanges:excludingRanges:replyHandler:"
- "wipeResource:includingRanges:excludingRanges:completionHandler:"
- "wipeResource:includingRanges:excludingRanges:extension:completionHandler:"
- "wipeResource:includingRanges:excludingRanges:reply:"
- "writeFrom:startingAt:length:replyHandler:"
- "xattrNamed:ofItem:replyHandler:"

```
