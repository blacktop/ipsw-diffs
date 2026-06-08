## libpartition2_dynamic.dylib

> `/usr/lib/libpartition2_dynamic.dylib`

```diff

-3476.120.8.0.2
-  __TEXT.__text: 0xb668
-  __TEXT.__auth_stubs: 0x6e0
+3689.0.0.0.1
+  __TEXT.__text: 0xb628
   __TEXT.__objc_methlist: 0x584
   __TEXT.__const: 0xc8
   __TEXT.__oslogstring: 0x115f
-  __TEXT.__cstring: 0xc86
+  __TEXT.__cstring: 0xc8e
   __TEXT.__gcc_except_tab: 0x90
-  __TEXT.__unwind_info: 0x260
-  __TEXT.__objc_classname: 0x52
-  __TEXT.__objc_methname: 0xc41
-  __TEXT.__objc_methtype: 0x146
-  __TEXT.__objc_stubs: 0xd60
-  __DATA_CONST.__got: 0x118
+  __TEXT.__unwind_info: 0x258
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x3d0
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x4c0
   __DATA_CONST.__objc_superrefs: 0x20
   __DATA_CONST.__objc_arraydata: 0x58
-  __AUTH_CONST.__auth_got: 0x380
+  __DATA_CONST.__got: 0x118
   __AUTH_CONST.__const: 0x1c0
   __AUTH_CONST.__cfstring: 0xac0
   __AUTH_CONST.__objc_const: 0x3c0
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__objc_arrayobj: 0x18
+  __AUTH_CONST.__auth_got: 0x390
   __DATA.__objc_ivar: 0x4
   __DATA.__data: 0xac
   __DATA.__bss: 0x30

   - /System/Library/PrivateFrameworks/APFS.framework/APFS
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 8DF60E46-E15F-3552-B41A-BC1D97DB4D81
+  UUID: 5E687544-FF2C-3DE9-8CFC-7DA91089891D
   Functions: 144
-  Symbols:   647
-  CStrings:  537
+  Symbols:   649
+  CStrings:  346
 
Symbols:
+ _objc_retainAutoreleaseReturnValue
+ _objc_storeStrong
Functions:
~ +[LPAPFSContainer allAPFSContainers] : 408 -> 412
~ -[LPAPFSContainer addVolumeWithName:role:caseSensitive:reserveSize:quotaSize:pairedVolume:error:] : 2756 -> 2636
~ -[LPAPFSContainer volumesWithRole:group:] : 496 -> 500
~ -[LPAPFSContainer volumeWithRole:group:] : 164 -> 168
~ -[LPAPFSPhysicalStore parent] : 704 -> 708
~ -[LPAPFSPhysicalStore container] : 460 -> 464
~ ___43+[LPAPFSVolume defaultVolumeNameGivenRole:]_block_invoke : 100 -> 52
~ -[LPAPFSVolume role] : 636 -> 640
~ -[LPAPFSVolume container] : 276 -> 288
~ -[LPAPFSVolume _pathIsTemporaryMount:] : 236 -> 232
~ -[LPAPFSVolume _createTemporaryMountPointWithError:] : 448 -> 444
~ -[LPAPFSVolume mountAtPath:options:error:] : 2504 -> 2516
~ -[LPAPFSVolume snapshotsWithError:] : 368 -> 380
~ -[LPAPFSVolume snapshotInfoWithError:] : 1772 -> 1784
~ -[LPAPFSVolume deleteSnapshots:waitForDeletionFor:error:] : 1492 -> 1532
~ -[LPAPFSVolume renameSnapshot:to:error:] : 1152 -> 1156
~ -[LPAPFSVolume revertToSnapshot:options:error:] : 1472 -> 1476
~ __LPLogObject : 88 -> 68
~ +[LPMedia snapshotNameForMediaForPath:] : 1640 -> 1672
~ +[LPMedia liveMediaForSnapshotAtPath:] : 876 -> 872
~ +[LPMedia mediaForBSDNameOrDeviceNode:] : 292 -> 288
~ -[LPMedia wholeMediaForMedia] : 544 -> 548
~ -[LPMedia deviceModel] : 192 -> 196
~ -[LPMedia isEqual:] : 156 -> 160
~ +[LPMedia(Private) contentTypeToSubclassMap] : 88 -> 68
~ +[LPMedia(Private) waitForIOMediaWithDevNode:] : 524 -> 516
~ _iterateSafely : 424 -> 428
CStrings:
+ "/var/mnt/"
+ "/var/mnt//tmp-mount-XXXXXX"
- "/tmp/"
- "/tmp//tmp-mount-XXXXXX"
- "@16@0:8"
- "@20@0:8I16"
- "@20@0:8i16"
- "@24@0:8@16"
- "@24@0:8^@16"
- "@28@0:8i16@20"
- "@32@0:8@16^@24"
- "@32@0:8@16^B24"
- "@64@0:8@16i24B28q32q40@48^@56"
- "B16@0:8"
- "B24@0:8@16"
- "B24@0:8^@16"
- "B28@0:8i16^@20"
- "B32@0:8@16^@24"
- "B40@0:8@16@24^@32"
- "B40@0:8@16d24^@32"
- "BSDName"
- "I"
- "I16@0:8"
- "I24@0:8@16"
- "IOMainPort"
- "LPAPFSContainer"
- "LPAPFSPhysicalStore"
- "LPAPFSVolume"
- "LPMedia"
- "LPPartitionMedia"
- "Private"
- "T@\"LPAPFSVolume\",R"
- "T@\"NSArray\",R"
- "T@\"NSDictionary\",R"
- "TB,R"
- "TI,R"
- "TI,V_ioMedia"
- "UTF8String"
- "VMVolume"
- "_containerWithPhysticalStoreRole:"
- "_copyIOMediaForDiskWithPath:"
- "_copyLiveFilesystemIOMediaForRootedSnapshot"
- "_createTemporaryMountPointWithError:"
- "_deviceCharacteristicStringForKey:"
- "_ioMedia"
- "_loadMountPointTableForMode:"
- "_matchVolumesWithRole:group:"
- "_pathIsTemporaryMount:"
- "addObject:"
- "addVolumeWithName:role:caseSensitive:reserveSize:quotaSize:pairedVolume:error:"
- "allAPFSContainers"
- "allMedia"
- "arrayWithArray:"
- "arrayWithCapacity:"
- "arrayWithObjects:count:"
- "boolValue"
- "caseInsensitiveCompare:"
- "children"
- "compare:"
- "componentsSeparatedByString:"
- "container"
- "containsString:"
- "content"
- "contentTypeToSubclassMap"
- "contentTypesForPartitionMedia"
- "copy"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "createSnapshot:error:"
- "dealloc"
- "defaultMountPointGivenRole:"
- "defaultVolumeNameGivenRole:"
- "deleteSnapshots:waitForDeletionFor:error:"
- "deleteVolumeWithError:"
- "description"
- "devNodePath"
- "diagsContainer"
- "dictionary"
- "dictionaryWithCapacity:"
- "dictionaryWithDictionary:"
- "dictionaryWithObjects:forKeys:count:"
- "enumerateRoleMetadataUsingBlock:"
- "eraseVolumeWithError:"
- "errorWithDomain:code:userInfo:"
- "fileSystemRepresentation"
- "getBoolPropertyWithName:"
- "getCString:maxLength:encoding:"
- "getPropertyWithName:"
- "getStringPropertyWithName:"
- "hardwareVolume"
- "hasEmbeddedDeviceTypeRoot"
- "hasPrefix:"
- "hasSuffix:"
- "i16@0:8"
- "init"
- "initWithBytes:length:encoding:"
- "initWithFormat:arguments:"
- "initWithIOMediaObject:"
- "initialize"
- "intValue"
- "ioMedia"
- "isCaseSenstive"
- "isEmbeddedDeviceTypeRoot"
- "isEncrypted"
- "isEqual:"
- "isEqualToString:"
- "isFilevaultEncrypted"
- "isInternal"
- "isJournaled"
- "isMounted"
- "isPrimaryMedia"
- "isReadOnly"
- "isWhole"
- "lastObject"
- "length"
- "liveMediaForSnapshotAtPath:"
- "mediaForBSDNameOrDeviceNode:"
- "mediaForPath:"
- "mediaForPath:isSnapshot:"
- "mediaForPath:snapshotName:"
- "mediaForUUID:"
- "mediaOfCorrectTypeGivenIOMedia:"
- "mediaUUID"
- "mountAtPath:error:"
- "mountAtPath:options:error:"
- "mountAtTemporaryPathWithError:"
- "mountAtTemporaryPathWithOptions:error:"
- "mountPoint"
- "mountWithError:"
- "name"
- "numberWithInt:"
- "numberWithLongLong:"
- "numberWithUnsignedLongLong:"
- "numberWithUnsignedShort:"
- "objectAtIndex:"
- "objectAtIndexedSubscript:"
- "objectForKey:"
- "objectForKeyedSubscript:"
- "pairedVolume"
- "pairedVolumeWithRole:"
- "parent"
- "physicalStores"
- "prebootVolume"
- "primaryMedia"
- "r^{?=iS@@}20@0:8i16"
- "rangeOfString:options:"
- "recoveryContainer"
- "recoveryVolume"
- "removeAllObjects"
- "renameSnapshot:to:error:"
- "revertToSnapshot:error:"
- "revertToSnapshot:options:error:"
- "role"
- "roleMetadataForRole:"
- "rootToSnapshot:error:"
- "setIoMedia:"
- "setName:withError:"
- "setObject:forKey:"
- "setObject:forKeyedSubscript:"
- "setRole:withError:"
- "snapshotInfoWithError:"
- "snapshotMountPoints"
- "snapshotNameForMediaForPath:"
- "snapshotsWithError:"
- "sortUsingComparator:"
- "sortedArrayUsingComparator:"
- "storageMedium"
- "stringByDeletingLastPathComponent"
- "stringByResolvingSymlinksInPath"
- "stringWithCString:encoding:"
- "stringWithFormat:"
- "stringWithUTF8String:"
- "substringFromIndex:"
- "substringToIndex:"
- "supportedContentTypes"
- "unmountAllWithError:"
- "unmountWithError:"
- "unmountWithOptions:error:"
- "updateVolume"
- "v16@0:8"
- "v20@0:8I16"
- "v20@0:8i16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "vendorName"
- "volumeGroupUUID"
- "volumeWithRole:group:"
- "volumes"
- "volumesWithRole:"
- "volumesWithRole:group:"
- "waitForBlockStorage"
- "waitForIOMediaWithDevNode:"
- "wholeMediaForMedia"
- "xARTVolume"

```
