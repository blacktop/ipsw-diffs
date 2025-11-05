## com.apple.fskit.msdos

> `/System/Library/ExtensionKit/Extensions/com.apple.fskit.msdos.appex/Contents/MacOS/com.apple.fskit.msdos`

```diff

-720.80.2.0.0
-  __TEXT.__text: 0x363e8
-  __TEXT.__auth_stubs: 0x6b0
-  __TEXT.__objc_stubs: 0x3960
-  __TEXT.__objc_methlist: 0x1a28
-  __TEXT.__const: 0x4da0
-  __TEXT.__cstring: 0x38d5
-  __TEXT.__gcc_except_tab: 0x1bd8
-  __TEXT.__objc_methname: 0x4284
-  __TEXT.__oslogstring: 0x28d5
-  __TEXT.__objc_classname: 0x273
-  __TEXT.__objc_methtype: 0x1746
-  __TEXT.__unwind_info: 0x9c0
-  __DATA_CONST.__auth_got: 0x368
-  __DATA_CONST.__got: 0xf0
+747.100.27.0.0
+  __TEXT.__text: 0x3846c
+  __TEXT.__auth_stubs: 0x6d0
+  __TEXT.__objc_stubs: 0x3ae0
+  __TEXT.__objc_methlist: 0x1fa4
+  __TEXT.__const: 0x4e15
+  __TEXT.__cstring: 0x3c24
+  __TEXT.__gcc_except_tab: 0x1634
+  __TEXT.__objc_methname: 0x448d
+  __TEXT.__oslogstring: 0x290f
+  __TEXT.__objc_classname: 0x274
+  __TEXT.__objc_methtype: 0x1760
+  __TEXT.__unwind_info: 0x9e8
+  __DATA_CONST.__auth_got: 0x378
+  __DATA_CONST.__got: 0x108
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0xfe0
-  __DATA_CONST.__cfstring: 0x600
+  __DATA_CONST.__const: 0x1210
+  __DATA_CONST.__cfstring: 0x5e0
   __DATA_CONST.__objc_classlist: 0xc8
   __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x98
-  __DATA.__objc_const: 0x3ee0
-  __DATA.__objc_selrefs: 0x1148
-  __DATA.__objc_ivar: 0x1b8
+  __DATA.__objc_const: 0x36d8
+  __DATA.__objc_selrefs: 0x1280
+  __DATA.__objc_ivar: 0x1cc
   __DATA.__objc_data: 0x7d0
   __DATA.__data: 0xa88
   __DATA.__common: 0x8c

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libutil.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 7A1895FA-41B9-3476-82AB-182B7E2DC3A0
-  Functions: 1094
-  Symbols:   311
-  CStrings:  1764
+  UUID: 91BDEBAD-0AD1-3DBD-BF2C-D2FCE1B35E3E
+  Functions: 1134
+  Symbols:   316
+  CStrings:  1800
 
Symbols:
+ _FSKitErrorDomain
+ _FSOperationIDUnspecified
+ _OBJC_CLASS_$_FSContainerStatus
+ _OBJC_CLASS_$_FSItem
+ _OBJC_CLASS_$_FSMetadataRange
+ _OBJC_METACLASS_$_FSItem
+ __os_log_default
+ _asprintf
+ _ftruncate
+ _pwrite
- _FSVolumeErrorDomain
- _OBJC_CLASS_$_FSMetadataBlockRange
- _OBJC_CLASS_$_FSUnaryItem
- _OBJC_METACLASS_$_FSUnaryItem
- _fskit_std_log
CStrings:
+ ""
+ "%s-%d"
+ "%s/shadow-%d"
+ "%s/shadow-r%s"
+ "%s: Couldn't allocate all clusters for wanted offset and length. Length to write = %llu (instead of %zu).\n"
+ "%s: Couldn't fetch extents in range [%llu, %llu]. Error = %@."
+ "%s: Couldn't find blockmap request (%lu) in dictionary."
+ "%s: offset: %llu, length: %zu, flags: %lu, operationID: %lu.\n"
+ "%s: offset: %lu, length: %lu, status: %d, flags: %lu, operationID: %lu."
+ "%s: victim item and its directory can't be the same item"
+ "-[FATItem reclaim:]"
+ "-[FATItem reclaim:]_block_invoke"
+ "-[FATVolume blockmapFile:offset:length:flags:operationID:packer:replyHandler:]"
+ "-[FATVolume blockmapFile:offset:length:flags:operationID:packer:replyHandler:]_block_invoke_2"
+ "-[FATVolume completeIOForFile:offset:length:status:flags:operationID:replyHandler:]"
+ "-[FATVolume deactivateItem:replyHandler:]"
+ "-[FATVolume lookupItemNamed:inDirectory:packer:replyHandler:]_block_invoke_2"
+ "-[FATVolume preallocateSpaceForFile:atOffset:length:flags:packer:replyHandler:]_block_invoke_2"
+ "-[FATVolume preallocateSpaceForItem:atOffset:length:flags:replyHandler:]"
+ "-[FATVolume preallocateSpaceForItem:atOffset:length:flags:replyHandler:]_block_invoke_2"
+ "-[FATVolume removeItem:named:fromDirectory:replyHandler:]_block_invoke_2"
+ "-[FATVolume renameItem:inDirectory:named:toNewName:inDirectory:overItem:replyHandler:]_block_invoke_2"
+ "-[FATVolume renameItem:inDirectory:named:toNewName:inDirectory:overItem:replyHandler:]_block_invoke_3"
+ "-[FATVolume setAttributes:onItem:replyHandler:]_block_invoke_2"
+ "-[FATVolume synchronizeWithFlags:replyHandler:]_block_invoke"
+ "-[FATVolume synchronizeWithFlags:replyHandler:]_block_invoke_2"
+ "-[FileItem blockmapOffset:length:flags:operationID:packer:replyHandler:]"
+ "-[FileItem blockmapOffset:length:flags:operationID:packer:replyHandler:]_block_invoke"
+ "-[FileItem completeIOAtOffset:length:status:flags:operationID:]"
+ "-[FileItem completeIOAtOffset:length:status:flags:operationID:]_block_invoke"
+ "-[msdosFileSystem startCheckWithTask:options:error:]"
+ "-[msdosFileSystem startFormatWithTask:options:error:]"
+ "-[msdosFileSystem startFormatWithTask:options:error:]_block_invoke"
+ "5"
+ "@\"DirItem\"48@0:8@\"FATItem\"16I24@\"DirEntryData\"28@\"FSFileName\"36B44"
+ "@\"FSFileName\""
+ "@\"FileItem\"44@0:8@\"FATItem\"16I24@\"DirEntryData\"28@\"FSFileName\"36"
+ "@\"NSProgress\"40@0:8@\"FSTask\"16@\"FSTaskOptions\"24^@32"
+ "@\"SymLinkItem\"48@0:8@\"FATItem\"16I24@\"DirEntryData\"28@\"FSFileName\"36S44"
+ "@20@0:8B16"
+ "@52@0:8q16Q24i32Q36Q44"
+ "AQ"
+ "Can't open\n"
+ "FSVolumeItemDeactivation"
+ "Failed to open shadow file at %s (%d)\n"
+ "Failed to shadow at offset 0x%llx, length 0x%x (errno %d)"
+ "Failed to shadow at offset 0x%llx, length 0x%zx (errno %d)"
+ "Failed to shadow offset 0, length 0x%x (errno: %d)"
+ "Failed to shadow offset 0x%x, length 0x%x (errno %d)"
+ "Failed to truncate shadow file to size 0x%x (errno %d)"
+ "T@\"FSFileName\",&,V_name"
+ "T@\"NSNumber\",&,V_fileIDSyncObject"
+ "T@\"NSObject<OS_dispatch_queue>\",&,N,V_queue"
+ "T@\"NSObject<OS_dispatch_queue>\",&,V_globalWorkQueue"
+ "TB,?"
+ "TB,V_includedInVolumeOUFiles"
+ "TQ,?,R"
+ "TQ,V_itemDeactivationPolicy"
+ "Warning: (NO WRITE)\n"
+ "X"
+ "_fileIDSyncObject"
+ "_globalWorkQueue"
+ "_includedInVolumeOUFiles"
+ "_itemDeactivationPolicy"
+ "_queue"
+ "asynchronousMetadataFlushWithError:"
+ "blockmapFile:offset:length:flags:operationID:packer:replyHandler:"
+ "blockmapOffset:length:flags:operationID:packer:replyHandler:"
+ "com.apple.fskit.msdos.itemQueue"
+ "completeIOAtOffset:length:status:flags:operationID:"
+ "completeIOForFile:offset:length:status:flags:operationID:replyHandler:"
+ "createFileNamed:inDirectory:attributes:packer:replyHandler:"
+ "deactivateItem:replyHandler:"
+ "decNumberOfOpenUnlinkedFiles"
+ "decNumberOfPreallocatedFiles"
+ "delayedMetadataWriteFrom:startingAt:length:error:"
+ "fileIDSyncObject"
+ "getNumberOfOpenUnlinkedFiles"
+ "getNumberOfPreallocatedFiles"
+ "globalWorkQueue"
+ "incNumberOfOpenUnlinkedFiles"
+ "incNumberOfPreallocatedFiles"
+ "includedInVolumeOUFiles"
+ "initWithCString:"
+ "initWithFileSystemTypeName:"
+ "itemDeactivationPolicy"
+ "lookupItemNamed:inDirectory:packer:replyHandler:"
+ "metadataClear:withDelayedWrites:error:"
+ "metadataFlushWithError:"
+ "metadataPurge:error:"
+ "metadataReadInto:startingAt:length:error:"
+ "notReadyWithStatus:"
+ "notRecognizedProbeResult"
+ "objectForKeyedSubscript:"
+ "packEntryWithName:itemType:itemID:nextCookie:attributes:"
+ "packExtentWithResource:type:logicalOffset:physicalOffset:length:"
+ "preallocateSpaceForFile:atOffset:length:flags:packer:replyHandler:"
+ "preallocateSpaceForItem:atOffset:length:flags:replyHandler:"
+ "queue"
+ "rangeWithOffset:segmentLength:segmentCount:"
+ "ready"
+ "reclaim:"
+ "restrictsOwnershipChanges"
+ "segmentLength"
+ "setCaseFormat:"
+ "setContainerStatus:"
+ "setFileIDSyncObject:"
+ "setGlobalWorkQueue:"
+ "setIncludedInVolumeOUFiles:"
+ "setItemDeactivationPolicy:"
+ "setQueue:"
+ "startCheckWithTask:options:error:"
+ "startFormatWithTask:options:error:"
+ "taskOptions"
+ "unloadResource:options:replyHandler:"
+ "usableProbeResultWithName:containerID:"
+ "v24@?0Q8@\"NSError\"16"
+ "v32@0:8@\"FSTaskOptions\"16@?<v@?@\"FSItem\"@\"NSError\">24"
+ "v32@0:8@\"FSTaskOptions\"16@?<v@?@\"NSError\">24"
+ "v36@0:8@\"FSFileName\"16I24@?<v@?@\"NSError\"{unistr255=S[255S]}>28"
+ "v40@0:8@\"FSResource\"16@\"FSTaskOptions\"24@?<v@?@\"FSVolume\"@\"NSError\">32"
+ "v40@0:8@\"FSResource\"16@\"FSTaskOptions\"24@?<v@?@\"NSError\">32"
+ "v48@0:8@\"FSFileName\"16@\"FSItem\"24@\"FSExtentPacker\"32@?<v@?@\"FSItem\"@\"FSFileName\"@\"NSError\">40"
+ "v48@0:8Q16Q24@32@?40"
+ "v56@0:8@\"FSFileName\"16@\"FSItem\"24@\"FSItemSetAttributesRequest\"32@\"FSExtentPacker\"40@?<v@?@\"FSItem\"@\"FSFileName\"@\"NSError\">48"
+ "v56@0:8@\"FSItem\"16q24Q32Q40@?<v@?Q@\"NSError\">48"
+ "v56@0:8@16q24Q32Q40@?48"
+ "v64@0:8@\"FSItem\"16Q24Q32@\"FSItemGetAttributesRequest\"40@\"FSDirectoryEntryPacker\"48@?<v@?Q@\"NSError\">56"
+ "v64@0:8@\"FSItem\"16q24Q32Q40@\"FSExtentPacker\"48@?<v@?Q@\"NSError\">56"
+ "v64@0:8@16Q24Q32@40@48@?56"
+ "v64@0:8@16q24Q32Q40@48@?56"
+ "v64@0:8q16Q24Q32Q40@48@?56"
+ "v72@0:8@\"FSItem\"16q24Q32@\"NSError\"40Q48Q56@?<v@?@\"NSError\">64"
+ "v72@0:8@\"FSItem\"16q24Q32Q40Q48@\"FSExtentPacker\"56@?<v@?@\"NSError\">64"
+ "v72@0:8@16q24Q32@40Q48Q56@?64"
+ "v72@0:8@16q24Q32Q40Q48@56@?64"
- "%s: Couldn't allocate all clusters for wanted offset and length. Length to write = %llu (instead of %llu).\n"
- "%s: Couldn't find blockmap request (%llu) in dictionary."
- "%s: Not supporting FSPreallocateFromVol mode"
- "%s: offset: %llu, length: %llu, startIO: %d, flags: %u, operationID: %llu.\n"
- "%s: offset: %lu, length: %lu, status: %d, flags: %u, operationID: %llu."
- "-[FATItem reclaim]"
- "-[FATItem reclaim]_block_invoke"
- "-[FATVolume blockmapFile:range:startIO:flags:operationID:usingPacker:replyHandler:]"
- "-[FATVolume blockmapFile:range:startIO:flags:operationID:usingPacker:replyHandler:]_block_invoke"
- "-[FATVolume endIO:range:status:flags:operationID:replyHandler:]"
- "-[FATVolume lookupItemNamed:inDirectory:usingPacker:replyHandler:]_block_invoke_2"
- "-[FATVolume preallocateSpaceForItem:offset:length:flags:usingPacker:replyHandler:]"
- "-[FATVolume preallocateSpaceForItem:offset:length:flags:usingPacker:replyHandler:]_block_invoke"
- "-[FATVolume setAttributes:onItem:replyHandler:]_block_invoke"
- "-[FATVolume synchronizeWithFlags:replyHandler:]"
- "-[FATVolume unmountWithReplyHandler:]"
- "-[FileItem blockmapRange:startIO:flags:operationID:usingBlocks:replyHandler:]"
- "-[FileItem blockmapRange:startIO:flags:operationID:usingBlocks:replyHandler:]_block_invoke"
- "-[FileItem endIOOfRange:status:flags:operationID:]"
- "-[FileItem endIOOfRange:status:flags:operationID:]_block_invoke"
- "-[msdosFileSystem startCheckWithTask:parameters:error:]"
- "-[msdosFileSystem startFormatWithTask:parameters:error:]"
- "-[msdosFileSystem startFormatWithTask:parameters:error:]_block_invoke"
- "12"
- "16"
- "4"
- "@\"DirItem\"48@0:8@\"FATItem\"16I24@\"DirEntryData\"28@\"NSString\"36B44"
- "@\"FileItem\"44@0:8@\"FATItem\"16I24@\"DirEntryData\"28@\"NSString\"36"
- "@\"NSProgress\"40@0:8@\"FSTask\"16@\"NSArray\"24^@32"
- "@\"SymLinkItem\"48@0:8@\"FATItem\"16I24@\"DirEntryData\"28@\"NSString\"36S44"
- "@48@0:8{_NSRange=QQ}16i32I36Q40"
- "Can't open"
- "FSBlockDeviceOperations"
- "PC_CASE_PRESERVING"
- "PC_CASE_SENSITIVE"
- "T@\"NSMutableArray\",&,V_nextAvailableFileID"
- "T@\"NSMutableArray\",&,V_openUnlinkedFiles"
- "T@\"NSMutableArray\",&,V_preAllocatedOpenFiles"
- "T@\"NSString\",&,V_name"
- "TB,?,GareXattrOperationsInhibited"
- "TB,R,GisChownRestricted"
- "Warning:  (NO WRITE)\n"
- "areXattrOperationsInhibited"
- "asynchronousMetadataFlush"
- "blockLength"
- "blockmapFile:range:startIO:flags:operationID:usingPacker:replyHandler:"
- "blockmapRange:startIO:flags:operationID:usingBlocks:replyHandler:"
- "chownRestricted"
- "createFileNamed:inDirectory:attributes:usingPacker:replyHandler:"
- "delayedMetadataWriteFrom:startingAt:length:"
- "endIO:range:status:flags:operationID:replyHandler:"
- "endIOOfRange:status:flags:operationID:"
- "initWithFSTypeName:"
- "initWithObjects:"
- "isChownRestricted"
- "lookupItemNamed:inDirectory:usingPacker:replyHandler:"
- "maxFileSizeInBits"
- "maxLinkCount"
- "maxNameLength"
- "metadataClear:wait:"
- "metadataFlush"
- "metadataPurge:"
- "metadataReadInto:startingAt:length:"
- "nextAvailableFileID"
- "numberWithUnsignedLongLong:"
- "objectAtIndex:"
- "openUnlinkedFiles"
- "preAllocatedOpenFiles"
- "preallocateSpaceForItem:offset:length:flags:usingPacker:replyHandler:"
- "rangeWithOffset:blockLength:numberOfBlocks:"
- "reclaim"
- "replaceObjectAtIndex:withObject:"
- "resultWithResult:name:containerID:"
- "setCaseSensitivity:"
- "setInhibitKernelOffloadedIO:"
- "setNextAvailableFileID:"
- "setOpenUnlinkedFiles:"
- "setPreAllocatedOpenFiles:"
- "startCheckWithTask:parameters:error:"
- "startFormatWithTask:parameters:error:"
- "unsignedLongLongValue"
- "v32@0:8@\"NSArray\"16@?<v@?@\"FSItem\"@\"NSError\">24"
- "v36@0:8@\"NSString\"16I24@?<v@?@\"NSError\"{unistr255=S[255S]}>28"
- "v40@0:8@\"FSResource\"16@\"NSArray\"24@?<v@?@\"FSVolume\"@\"NSError\">32"
- "v48@0:8@\"FSFileName\"16@\"FSItem\"24@?<B@?@\"FSBlockDeviceResource\"iQQI>32@?<v@?@\"FSItem\"@\"FSFileName\"@\"NSError\">40"
- "v48@0:8@16@24@?32@?40"
- "v48@0:8Q16Q24@?32@?40"
- "v56@0:8@\"FSFileName\"16@\"FSItem\"24@\"FSItemSetAttributesRequest\"32@?<B@?@\"FSBlockDeviceResource\"iQQI>40@?<v@?@\"FSItem\"@\"FSFileName\"@\"NSError\">48"
- "v56@0:8@16@24@32@?40@?48"
- "v60@0:8@\"FSItem\"16Q24Q32I40@?<B@?@\"FSBlockDeviceResource\"iQQI>44@?<v@?Q@\"NSError\">52"
- "v60@0:8@16Q24Q32I40@?44@?52"
- "v64@0:8@\"FSItem\"16Q24Q32@\"FSItemGetAttributesRequest\"40@?<B@?@\"FSFileName\"qQQ@\"FSItemAttributes\"B>48@?<v@?Q@\"NSError\">56"
- "v64@0:8@16Q24Q32@40@?48@?56"
- "v64@0:8{_NSRange=QQ}16B32I36Q40@?48@?56"
- "v68@0:8@\"FSItem\"16{_NSRange=QQ}24@\"NSError\"40I48Q52@?<v@?@\"NSError\">60"
- "v68@0:8@16{_NSRange=QQ}24@40I48Q52@?60"
- "v72@0:8@\"FSItem\"16{_NSRange=QQ}24B40I44Q48@?<B@?@\"FSBlockDeviceResource\"iQQI>56@?<v@?@\"NSError\">64"
- "v72@0:8@16{_NSRange=QQ}24B40I44Q48@?56@?64"

```
