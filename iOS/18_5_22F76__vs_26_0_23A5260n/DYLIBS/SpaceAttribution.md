## SpaceAttribution

> `/System/Library/PrivateFrameworks/SpaceAttribution.framework/SpaceAttribution`

```diff

-322.120.5.0.0
-  __TEXT.__text: 0xf100
-  __TEXT.__auth_stubs: 0x4e0
-  __TEXT.__objc_methlist: 0x1138
-  __TEXT.__const: 0xc0
-  __TEXT.__cstring: 0xd78
-  __TEXT.__gcc_except_tab: 0x638
-  __TEXT.__oslogstring: 0xa1d
-  __TEXT.__unwind_info: 0x510
-  __TEXT.__objc_classname: 0x162
-  __TEXT.__objc_methname: 0x2882
-  __TEXT.__objc_methtype: 0x6ce
-  __TEXT.__objc_stubs: 0x1aa0
-  __DATA_CONST.__got: 0x118
+428.0.0.0.1
+  __TEXT.__text: 0xfbb0
+  __TEXT.__auth_stubs: 0x530
+  __TEXT.__objc_methlist: 0x11c8
+  __TEXT.__const: 0xd0
+  __TEXT.__cstring: 0xe4b
+  __TEXT.__gcc_except_tab: 0x6b0
+  __TEXT.__oslogstring: 0xb9b
+  __TEXT.__unwind_info: 0x540
+  __TEXT.__objc_classname: 0x165
+  __TEXT.__objc_methname: 0x2967
+  __TEXT.__objc_methtype: 0x6df
+  __TEXT.__objc_stubs: 0x1a40
+  __DATA_CONST.__got: 0x108
   __DATA_CONST.__const: 0x400
   __DATA_CONST.__objc_classlist: 0x98
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xb10
+  __DATA_CONST.__objc_selrefs: 0xb18
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x68
   __DATA_CONST.__objc_arraydata: 0xd0
-  __AUTH_CONST.__auth_got: 0x280
+  __AUTH_CONST.__auth_got: 0x2a8
   __AUTH_CONST.__const: 0x60
-  __AUTH_CONST.__cfstring: 0xfc0
-  __AUTH_CONST.__objc_const: 0x1be8
+  __AUTH_CONST.__cfstring: 0x1080
+  __AUTH_CONST.__objc_const: 0x1c88
   __AUTH_CONST.__objc_arrayobj: 0x78
-  __AUTH.__objc_data: 0x410
-  __DATA.__objc_ivar: 0x128
+  __AUTH.__objc_data: 0x320
+  __DATA.__objc_ivar: 0x134
   __DATA.__data: 0x180
-  __DATA_DIRTY.__objc_data: 0x1e0
+  __DATA_DIRTY.__objc_data: 0x2d0
   __DATA_DIRTY.__bss: 0x20
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
-  - /System/Library/PrivateFrameworks/DiskImages2.framework/DiskImages2
-  - /System/Library/PrivateFrameworks/StorageKit.framework/StorageKit
+  - /System/Library/PrivateFrameworks/APFS.framework/APFS
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: FC3FAD2D-804E-3C29-8A2A-AA72626C06E8
-  Functions: 455
-  Symbols:   1555
-  CStrings:  950
+  UUID: E20E8E1E-5455-3D64-9780-1E9C190BAA0A
+  Functions: 475
+  Symbols:   1601
+  CStrings:  980
 
Symbols:
+ +[SAAppSize newWithFixedSize:dataSize:cloneSize:purgeableSize:cloneFixUpSize:physicalSize:appCacheSize:CDPluginSize:]
+ +[SAInternalAPI setAppPathListPathOnDisk:reply:]
+ +[SAInternalAPI setAppPathListPathOnDisktoDefaultWithReply:]
+ -[SAAppSize cacheIsPurgeable]
+ -[SAAppSize cloneFixUpSize]
+ -[SAAppSize initWithFixedSize:dataSize:cloneSize:purgeableSize:cloneFixUpSize:physicalSize:appCacheSize:CDPluginSize:]
+ -[SAAppSize setCacheIsPurgeable:]
+ -[SAAppSize setCloneFixUpSize:]
+ -[SAAppSizeBreakdownList addPath:fixedPath:size:bundleIDs:]
+ -[SAAppSizeBreakdownList addPluginSize:bundleIDs:]
+ -[SAAppSizeBreakdownList addTagSize:bundleIDs:]
+ -[SAAppSizeBreakdownList mergeBundleIDs:withBundleIDs:newBundleIDs:]
+ -[SAAppSizeBreakdownList removeBundleIDs:]
+ -[SAAppSizeBreakdownList updateBundleIDs:newIDs:]
+ -[SAAppSizeBreakdownList updatePath:cacheSize:bundleIDs:]
+ -[SAAppSizeBreakdownList updatePath:cloneSize:bundleIDs:]
+ -[SAAppSizeBreakdownList updateTagsWithCloneSize:bundleIDs:]
+ -[SAAppSizerResults APFSDiskUsed]
+ -[SAAppSizerResults accountPurgeableTagsFor:purgeableTagsSize:]
+ -[SAAppSizerResults addToSystemDetails:key:]
+ -[SAAppSizerResults initDiskUsedAndCapacity].cold.10
+ -[SAAppSizerResults initDiskUsedAndCapacity].cold.11
+ -[SAAppSizerResults initDiskUsedAndCapacity].cold.12
+ -[SAAppSizerResults initDiskUsedAndCapacity].cold.6
+ -[SAAppSizerResults initDiskUsedAndCapacity].cold.7
+ -[SAAppSizerResults initDiskUsedAndCapacity].cold.8
+ -[SAAppSizerResults initDiskUsedAndCapacity].cold.9
+ -[SAAppSizerResults internalFlags]
+ -[SAAppSizerResults removeBundleIDs:]
+ -[SAAppSizerResults setAPFSDiskUsed:]
+ -[SAAppSizerResults setBundleIDs:vendorName:]
+ -[SAAppSizerResults setBundleIDs:vendorName:].cold.1
+ -[SAAppSizerResults setInternalFlags:]
+ -[SAAppSizerResults updateBundleIDs:fixedSize:dataSize:cloneSize:purgeableSize:cloneFixUpSize:physicalSize:appCacheSize:CDPluginSize:]
+ -[SAAppSizerResults updateBundleIDs:withAppSize:]
+ -[SAAppSizerResults updateBundleIDs:withDataSize:]
+ -[SAAppSizerResults updateBundleIDs:withDataSize:].cold.1
+ -[SAAppSizerResults updateBundleIDs:withDataSize:].cold.2
+ -[SAAppSizerResults updateCacheSize:cacheIsPurgeable:bundleIDs:]
+ -[SAAppSizerResults updateCacheSize:cacheIsPurgeable:bundleIDs:].cold.1
+ -[SAAppSizerResults updateCacheSize:cacheIsPurgeable:bundleIDs:].cold.2
+ -[SAAppSizerResults updateHiddenApp:withPurgeableTagsSize:]
+ -[SAAppSizerResults updateHiddenApp:withPurgeableTagsSize:].cold.1
+ GCC_except_table100
+ GCC_except_table62
+ GCC_except_table65
+ GCC_except_table80
+ GCC_except_table86
+ GCC_except_table89
+ GCC_except_table93
+ _APFSContainerGetBootDevice
+ _IOObjectConformsTo
+ _IORegistryEntryCreateCFProperty
+ _IORegistryEntryCreateIterator
+ _IOServiceGetMatchingService
+ _OBJC_IVAR_$_SAAppSize._cacheIsPurgeable
+ _OBJC_IVAR_$_SAAppSize._cloneFixUpSize
+ _OBJC_IVAR_$_SAAppSizerResults._APFSDiskUsed
+ _OBJC_IVAR_$_SAAppSizerResults._internalFlags
+ ___38-[SADaemonXPC setInvalidationHandler:]_block_invoke.112
+ ___38-[SADaemonXPC setInvalidationHandler:]_block_invoke.112.cold.1
+ ___48+[SAInternalAPI setAppPathListPathOnDisk:reply:]_block_invoke
+ ___48+[SAInternalAPI setAppPathListPathOnDisk:reply:]_block_invoke_2
+ ___51-[SAPathManager unregisterPaths:completionHandler:]_block_invoke.180
+ ___51-[SAPathManager unregisterPaths:completionHandler:]_block_invoke.180.cold.1
+ ___60+[SAInternalAPI setAppPathListPathOnDisktoDefaultWithReply:]_block_invoke
+ ___60+[SAInternalAPI setAppPathListPathOnDisktoDefaultWithReply:]_block_invoke_2
+ ___68+[SAVolumeSizer computeSizeOfVolumeAtURL:options:completionHandler:]_block_invoke.68
+ ___68+[SAVolumeSizer computeSizeOfVolumeAtURL:options:completionHandler:]_block_invoke.68.cold.1
+ ___68+[SAVolumeSizer computeSizeOfVolumeAtURL:options:completionHandler:]_block_invoke.69
+ ___block_descriptor_40_e8_32bs_e36_v32?0"NSString"8"SAAppSize"16^B24ls32l8
+ ___block_descriptor_40_e8_32s_e45_v32?0"NSString"8"SAAppSizeBreakdown"16^B24ls32l8
+ ___block_descriptor_48_e8_32s40r_e32_v24?0"NSString"8"SAAppSize"16ls32l8r40l8
+ ___block_literal_global.114
+ _objc_msgSend$cloneFixUpSize
+ _objc_msgSend$initWithFixedSize:dataSize:cloneSize:purgeableSize:cloneFixUpSize:physicalSize:appCacheSize:CDPluginSize:
+ _objc_msgSend$internalFlags
+ _objc_msgSend$mergeBundleIDs:withBundleIDs:newBundleIDs:
+ _objc_msgSend$newWithFixedSize:dataSize:cloneSize:purgeableSize:cloneFixUpSize:physicalSize:appCacheSize:CDPluginSize:
+ _objc_msgSend$removeBundleIDs:
+ _objc_msgSend$setAppPathListPathOnDisk:reply:
+ _objc_msgSend$setAppPathListPathOnDisktoDefaultWithReply:
+ _objc_msgSend$setCacheIsPurgeable:
+ _objc_msgSend$setCloneFixUpSize:
+ _objc_msgSend$updateBundleIDs:newIDs:
+ _objc_msgSend$updateBundleIDs:withAppSize:
+ _objc_msgSend$updateHiddenApp:withPurgeableTagsSize:
- +[SAAppSize newWithFixedSize:dataSize:cloneSize:purgeableSize:FSPurgeableSize:physicalSize:appCacheSize:CDPluginSize:]
- -[SAAppSize FSPurgeableSize]
- -[SAAppSize initWithFixedSize:dataSize:cloneSize:purgeableSize:FSPurgeableSize:physicalSize:appCacheSize:CDPluginSize:]
- -[SAAppSize setFSPurgeableSize:]
- -[SAAppSizeBreakdownList addPath:fixedPath:size:bundleId:]
- -[SAAppSizeBreakdownList addPluginSize:bundleId:]
- -[SAAppSizeBreakdownList addTagSize:bundleId:]
- -[SAAppSizeBreakdownList mergeBundleId:withBundleId:newBundleId:]
- -[SAAppSizeBreakdownList removeBundleId:]
- -[SAAppSizeBreakdownList updateBundleId:newId:]
- -[SAAppSizeBreakdownList updatePath:cacheSize:bundleId:]
- -[SAAppSizeBreakdownList updatePath:cloneSize:bundleId:]
- -[SAAppSizeBreakdownList updateTagsWithCloneSize:bundleId:]
- -[SAAppSizerResults removeBundleSet:]
- -[SAAppSizerResults setAppSet:vendorName:]
- -[SAAppSizerResults setAppSet:vendorName:].cold.1
- -[SAAppSizerResults setAppSet:withAppSize:]
- -[SAAppSizerResults updateAppSet:fixedSize:dataSize:cloneSize:purgeableSize:FSPurgeableSize:physicalSize:appCacheSize:CDPluginSize:]
- -[SAAppSizerResults updateAppSet:withAppSize:]
- -[SAAppSizerResults updateBundleID:WithCloneSize:]
- -[SAAppSizerResults updateBundleID:WithCloneSize:].cold.1
- -[SAAppSizerResults updateBundleID:WithCloneSize:].cold.2
- -[SAAppSizerResults updateBundleID:withDataSize:]
- -[SAAppSizerResults updateBundleID:withDataSize:].cold.1
- -[SAAppSizerResults updateBundleID:withDataSize:].cold.2
- GCC_except_table73
- GCC_except_table76
- GCC_except_table83
- GCC_except_table96
- _OBJC_CLASS_$_DIIOMedia
- _OBJC_CLASS_$_SKManager
- _OBJC_IVAR_$_SAAppSize._FSPurgeableSize
- _OUTLINED_FUNCTION_4
- ___38-[SADaemonXPC setInvalidationHandler:]_block_invoke.104
- ___38-[SADaemonXPC setInvalidationHandler:]_block_invoke.104.cold.1
- ___51-[SAPathManager unregisterPaths:completionHandler:]_block_invoke.174
- ___51-[SAPathManager unregisterPaths:completionHandler:]_block_invoke.174.cold.1
- ___68+[SAVolumeSizer computeSizeOfVolumeAtURL:options:completionHandler:]_block_invoke.62
- ___68+[SAVolumeSizer computeSizeOfVolumeAtURL:options:completionHandler:]_block_invoke.62.cold.1
- ___68+[SAVolumeSizer computeSizeOfVolumeAtURL:options:completionHandler:]_block_invoke.63
- ___block_descriptor_40_e8_32r_e29_v24?0"NSSet"8"SAAppSize"16lr32l8
- ___block_descriptor_40_e8_32s_e42_v32?0"NSSet"8"SAAppSizeBreakdown"16^B24ls32l8
- ___block_descriptor_48_e8_32s40bs_e36_v32?0"NSString"8"SAAppSize"16^B24ls32l8s40l8
- ___block_literal_global.106
- _objc_msgSend$FSPurgeableSize
- _objc_msgSend$container
- _objc_msgSend$copyPropertyWithClass:key:
- _objc_msgSend$designatedPhysicalStore
- _objc_msgSend$diskForPath:
- _objc_msgSend$diskIdentifier
- _objc_msgSend$initWithDevName:error:
- _objc_msgSend$initWithFixedSize:dataSize:cloneSize:purgeableSize:FSPurgeableSize:physicalSize:appCacheSize:CDPluginSize:
- _objc_msgSend$mergeBundleId:withBundleId:newBundleId:
- _objc_msgSend$newWithFixedSize:dataSize:cloneSize:purgeableSize:FSPurgeableSize:physicalSize:appCacheSize:CDPluginSize:
- _objc_msgSend$removeBundleId:
- _objc_msgSend$setFSPurgeableSize:
- _objc_msgSend$syncSharedManager
- _objc_msgSend$updateAppSet:withAppSize:
- _objc_msgSend$updateBundleId:newId:
- _objc_msgSend$wholeDiskForDisk:
CStrings:
+ "%s: Failed to find root disk size"
+ "-[SAAppSizerResults setBundleIDs:vendorName:]"
+ "-[SAAppSizerResults updateHiddenApp:withPurgeableTagsSize:]"
+ "@80@0:8Q16Q24Q32Q40q48Q56Q64Q72"
+ "APFSDiskUsed"
+ "CacheIsPurgeable"
+ "CloneFixUpSize"
+ "Exceeded the number of max iterations (%d) while iterating %@ parents in the IO registry"
+ "Exceeded the number of max iterations (%d) while searching for the IO media device in the IO registry"
+ "Failed to create IO iterator with error code %d"
+ "Failed to find %@ entry is the IO registry"
+ "Failed to get boot device with error %d"
+ "Failed to get boot disk IO media object in registry"
+ "Failed to get containing block device for disk %@"
+ "Failed to split array (count: %lu) to %d parts. Bailing out"
+ "IOBlockStorageDevice"
+ "IOMedia"
+ "Internal Flags"
+ "TB,V_cacheIsPurgeable"
+ "TQ,V_APFSDiskUsed"
+ "TQ,V_internalFlags"
+ "Tq,V_cloneFixUpSize"
+ "_APFSDiskUsed"
+ "_cacheIsPurgeable"
+ "_cloneFixUpSize"
+ "_internalFlags"
+ "accountPurgeableTagsFor:purgeableTagsSize:"
+ "addPath:fixedPath:size:bundleIDs:"
+ "addPluginSize:bundleIDs:"
+ "addTagSize:bundleIDs:"
+ "addToSystemDetails:key:"
+ "bundleID %@ adding to cacheSize %llu"
+ "bundleID %@ not found, creating with cacheSize %llu"
+ "cacheIsPurgeable"
+ "cfBootDisk: %@"
+ "cloneFixUpSize"
+ "com.apple.fakeapp.SoftwareUpdateReserve"
+ "initWithFixedSize:dataSize:cloneSize:purgeableSize:cloneFixUpSize:physicalSize:appCacheSize:CDPluginSize:"
+ "internalFlags"
+ "mergeBundleIDs:withBundleIDs:newBundleIDs:"
+ "newWithFixedSize:dataSize:cloneSize:purgeableSize:cloneFixUpSize:physicalSize:appCacheSize:CDPluginSize:"
+ "removeBundleIDs:"
+ "setAPFSDiskUsed:"
+ "setAppPathListPathOnDisk:reply:"
+ "setAppPathListPathOnDisktoDefaultWithReply:"
+ "setBundleIDs:vendorName:"
+ "setCacheIsPurgeable:"
+ "setCloneFixUpSize:"
+ "setInternalFlags:"
+ "updateBundleIDs:fixedSize:dataSize:cloneSize:purgeableSize:cloneFixUpSize:physicalSize:appCacheSize:CDPluginSize:"
+ "updateBundleIDs:newIDs:"
+ "updateBundleIDs:withAppSize:"
+ "updateBundleIDs:withDataSize:"
+ "updateCacheSize:cacheIsPurgeable:bundleIDs:"
+ "updateHiddenApp:withPurgeableTagsSize:"
+ "updatePath:cacheSize:bundleIDs:"
+ "updatePath:cloneSize:bundleIDs:"
+ "updateTagsWithCloneSize:bundleIDs:"
+ "v24@?0@\"NSString\"8@\"SAAppSize\"16"
+ "v32@?0@\"NSString\"8@\"SAAppSizeBreakdown\"16^B24"
+ "v36@0:8Q16B24@28"
- "%s:%s: Failed to find %@ in the registry: %@"
- "%s:%s: Failed to find size of disk0"
- "'System Data' not found, creating"
- "-[SAAppSizerResults setAppSet:vendorName:]"
- "@80@0:8Q16Q24Q32Q40Q48Q56Q64Q72"
- "FSPurgeableSize"
- "Failed to split array (count: %ld) to %d parts. Bailing out"
- "Root volume disk: %@"
- "TQ,V_FSPurgeableSize"
- "_FSPurgeableSize"
- "addPath:fixedPath:size:bundleId:"
- "addPluginSize:bundleId:"
- "addTagSize:bundleId:"
- "bundleID %@ not found, add to 'System Data'"
- "container"
- "copyPropertyWithClass:key:"
- "designatedPhysicalStore"
- "diskForPath:"
- "diskIdentifier"
- "initWithDevName:error:"
- "initWithFixedSize:dataSize:cloneSize:purgeableSize:FSPurgeableSize:physicalSize:appCacheSize:CDPluginSize:"
- "mergeBundleId:withBundleId:newBundleId:"
- "newWithFixedSize:dataSize:cloneSize:purgeableSize:FSPurgeableSize:physicalSize:appCacheSize:CDPluginSize:"
- "removeBundleId:"
- "removeBundleSet:"
- "setAppSet:vendorName:"
- "setAppSet:withAppSize:"
- "setFSPurgeableSize:"
- "syncSharedManager"
- "updateAppSet:fixedSize:dataSize:cloneSize:purgeableSize:FSPurgeableSize:physicalSize:appCacheSize:CDPluginSize:"
- "updateAppSet:withAppSize:"
- "updateBundleID:WithCloneSize:"
- "updateBundleID:withDataSize:"
- "updateBundleId:newId:"
- "updatePath:cacheSize:bundleId:"
- "updatePath:cloneSize:bundleId:"
- "updateTagsWithCloneSize:bundleId:"
- "v24@?0@\"NSSet\"8@\"SAAppSize\"16"
- "v32@?0@\"NSSet\"8@\"SAAppSizeBreakdown\"16^B24"
- "wholeDiskForDisk:"

```
