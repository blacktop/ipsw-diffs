## ParavirtualizedANE

> `/System/Library/PrivateFrameworks/ParavirtualizedANE.framework/ParavirtualizedANE`

```diff

-382.102.2.0.0
-  __TEXT.__text: 0x20234
-  __TEXT.__objc_methlist: 0x814
-  __TEXT.__const: 0x190
-  __TEXT.__cstring: 0xf6e
-  __TEXT.__oslogstring: 0x6600
-  __TEXT.__gcc_except_tab: 0x3d50
-  __TEXT.__unwind_info: 0xb50
+382.200.2.0.0
+  __TEXT.__text: 0x23454
+  __TEXT.__objc_methlist: 0x978
+  __TEXT.__const: 0x1a0
+  __TEXT.__cstring: 0x107b
+  __TEXT.__oslogstring: 0x6db0
+  __TEXT.__gcc_except_tab: 0x44a8
+  __TEXT.__unwind_info: 0xc20
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x70
-  __DATA_CONST.__objc_classlist: 0x18
+  __DATA_CONST.__const: 0xc0
+  __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xa68
-  __DATA_CONST.__objc_superrefs: 0x10
-  __DATA_CONST.__got: 0x1b8
-  __AUTH_CONST.__const: 0xd0
-  __AUTH_CONST.__cfstring: 0x11c0
-  __AUTH_CONST.__objc_const: 0x570
+  __DATA_CONST.__objc_selrefs: 0xbc8
+  __DATA_CONST.__objc_superrefs: 0x18
+  __DATA_CONST.__got: 0x1e0
+  __AUTH_CONST.__const: 0xf0
+  __AUTH_CONST.__cfstring: 0x1320
+  __AUTH_CONST.__objc_const: 0x810
   __AUTH_CONST.__weak_auth_got: 0x28
   __AUTH_CONST.__objc_intobj: 0x18
-  __AUTH_CONST.__auth_got: 0x328
-  __AUTH.__objc_data: 0xf0
-  __DATA.__objc_ivar: 0x4c
+  __AUTH_CONST.__auth_got: 0x358
+  __AUTH.__objc_data: 0x140
+  __DATA.__objc_ivar: 0x74
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 545
-  Symbols:   564
-  CStrings:  563
+  Functions: 596
+  Symbols:   641
+  CStrings:  609
 
Symbols:
+ +[_ANEVirtualPlatformClient assetUUIDFromLookupKey:]
+ +[_ANEVirtualPlatformClient prepareSharedCacheDirectory:]
+ -[_ANEAssetStagingState .cxx_destruct]
+ -[_ANEAssetStagingState contentDigest]
+ -[_ANEAssetStagingState emptyDirectories]
+ -[_ANEAssetStagingState expectedFileSizes]
+ -[_ANEAssetStagingState fileDigests]
+ -[_ANEAssetStagingState init]
+ -[_ANEAssetStagingState isComplete]
+ -[_ANEAssetStagingState publishedDirectory]
+ -[_ANEAssetStagingState receivedByteCounts]
+ -[_ANEAssetStagingState setEmptyDirectories:]
+ -[_ANEAssetStagingState setExpectedFileSizes:]
+ -[_ANEAssetStagingState setFileDigests:]
+ -[_ANEAssetStagingState setPublishedDirectory:]
+ -[_ANEAssetStagingState setReceivedByteCounts:]
+ -[_ANEAssetStagingState setStagingDirectory:]
+ -[_ANEAssetStagingState stagingDirectory]
+ -[_ANEVirtualPlatformClient assetStagingStates]
+ -[_ANEVirtualPlatformClient beginStagedTransferWithManifest:publishedDirectory:uuid:]
+ -[_ANEVirtualPlatformClient createAssetOnHost:dataSize:dataIOSID:filePathComplete:directoryPath:hashingInto:]
+ -[_ANEVirtualPlatformClient createModelFileAtPath:fromIOSID:withDataLength:shouldAppend:hashingInto:]
+ -[_ANEVirtualPlatformClient lastSharedAssetSweepDate]
+ -[_ANEVirtualPlatformClient maintenanceQueue]
+ -[_ANEVirtualPlatformClient publishStagedAssetForUUID:]
+ -[_ANEVirtualPlatformClient publishedDirectoryForLookupKey:]
+ -[_ANEVirtualPlatformClient setAssetStagingStates:]
+ -[_ANEVirtualPlatformClient setLastSharedAssetSweepDate:]
+ -[_ANEVirtualPlatformClient setSharedANEBaseDirectory:]
+ -[_ANEVirtualPlatformClient setSharedCachePath:]
+ -[_ANEVirtualPlatformClient sharedANEBaseDirectory]
+ GCC_except_table1
+ GCC_except_table106
+ GCC_except_table107
+ GCC_except_table112
+ GCC_except_table113
+ GCC_except_table128
+ GCC_except_table129
+ GCC_except_table130
+ GCC_except_table131
+ GCC_except_table134
+ GCC_except_table135
+ GCC_except_table136
+ GCC_except_table137
+ GCC_except_table140
+ GCC_except_table141
+ GCC_except_table142
+ GCC_except_table144
+ GCC_except_table145
+ GCC_except_table146
+ GCC_except_table147
+ GCC_except_table148
+ GCC_except_table149
+ GCC_except_table153
+ GCC_except_table176
+ GCC_except_table183
+ GCC_except_table184
+ GCC_except_table185
+ GCC_except_table189
+ GCC_except_table2
+ GCC_except_table3
+ GCC_except_table46
+ GCC_except_table59
+ GCC_except_table60
+ GCC_except_table66
+ GCC_except_table69
+ GCC_except_table72
+ GCC_except_table73
+ GCC_except_table77
+ GCC_except_table82
+ GCC_except_table92
+ _OBJC_CLASS_$_NSProcessInfo
+ _OBJC_CLASS_$__ANEAssetStagingState
+ _OBJC_CLASS_$__ANEAtomicPublish
+ _OBJC_CLASS_$__ANECacheMaintenance
+ _OBJC_CLASS_$__ANEIncrementalHash
+ _OBJC_IVAR_$__ANEAssetStagingState._emptyDirectories
+ _OBJC_IVAR_$__ANEAssetStagingState._expectedFileSizes
+ _OBJC_IVAR_$__ANEAssetStagingState._fileDigests
+ _OBJC_IVAR_$__ANEAssetStagingState._publishedDirectory
+ _OBJC_IVAR_$__ANEAssetStagingState._receivedByteCounts
+ _OBJC_IVAR_$__ANEAssetStagingState._stagingDirectory
+ _OBJC_IVAR_$__ANEVirtualPlatformClient._assetStagingStates
+ _OBJC_IVAR_$__ANEVirtualPlatformClient._lastSharedAssetSweepDate
+ _OBJC_IVAR_$__ANEVirtualPlatformClient._maintenanceQueue
+ _OBJC_IVAR_$__ANEVirtualPlatformClient._sharedANEBaseDirectory
+ _OBJC_METACLASS_$__ANEAssetStagingState
+ _OUTLINED_FUNCTION_35
+ _OUTLINED_FUNCTION_36
+ __OBJC_$_INSTANCE_METHODS__ANEAssetStagingState
+ __OBJC_$_INSTANCE_VARIABLES__ANEAssetStagingState
+ __OBJC_$_PROP_LIST__ANEAssetStagingState
+ __OBJC_CLASS_RO_$__ANEAssetStagingState
+ __OBJC_METACLASS_RO_$__ANEAssetStagingState
+ __ZZ52-[_ANEVirtualPlatformClient assetReceivedFromGuest:]E15manifestClasses
+ __ZZ52-[_ANEVirtualPlatformClient assetReceivedFromGuest:]E9onceToken
+ ___48-[_ANEVirtualPlatformClient setSharedCachePath:]_block_invoke
+ ___52-[_ANEVirtualPlatformClient assetReceivedFromGuest:]_block_invoke
+ ___55-[_ANEVirtualPlatformClient publishStagedAssetForUUID:]_block_invoke
+ ___85-[_ANEVirtualPlatformClient beginStagedTransferWithManifest:publishedDirectory:uuid:]_block_invoke
+ ___block_descriptor_40_ea8_32s_e5_v8?0ls32l8
+ ___block_descriptor_56_ea8_32s40s_e5_v8?0ls32l8s40l8
+ _dispatch_async
+ _dispatch_queue_attr_make_with_qos_class
+ _objc_getProperty
+ _objc_retain_x1
+ _objc_setProperty_atomic_copy
+ _objc_setProperty_nonatomic_copy
- -[_ANEVirtualPlatformClient createAssetOnHost:dataSize:dataIOSID:filePathComplete:directoryPath:]
- -[_ANEVirtualPlatformClient createModelFileAtPath:fromIOSID:withDataLength:shouldAppend:]
- GCC_except_table10
- GCC_except_table103
- GCC_except_table108
- GCC_except_table11
- GCC_except_table118
- GCC_except_table124
- GCC_except_table13
- GCC_except_table14
- GCC_except_table156
- GCC_except_table18
- GCC_except_table20
- GCC_except_table23
- GCC_except_table27
- GCC_except_table28
- GCC_except_table31
- GCC_except_table34
- GCC_except_table35
- GCC_except_table36
- GCC_except_table38
- GCC_except_table5
- GCC_except_table6
- GCC_except_table67
- GCC_except_table80
- GCC_except_table81
- GCC_except_table87
- GCC_except_table91
- GCC_except_table94
- GCC_except_table95
- GCC_except_table99
CStrings:
+ "%@ (no host model for programHandle=%llu)"
+ "%@/%@-%@/"
+ "%@: ANEVirtualPlatformClient evaluate model does not exist programHandle=%llu!"
+ "%@: ANEVirtualPlatformClient shared cache disabled"
+ "%@: ANEVirtualPlatformClient shared cache enabled, filepath:%@"
+ "%@: Cannot create shared cache directory %@: %@"
+ "%@: Cannot write to shared cache directory %@: %@"
+ "%@: ERROR : BAD_ARGUMENT : manifest, publishedDirectory or uuid missing!"
+ "%@: ERROR asset manifest is missing a UUID!"
+ "%@: ERROR could not clear stale staging directory=%@ with error=%@"
+ "%@: ERROR could not create empty directory=%@ with error=%@"
+ "%@: ERROR could not create parent directory=%@ with error=%@"
+ "%@: ERROR could not create staging directory=%@ with error=%@"
+ "%@: ERROR could not derive a content digest for uuid=%@, not publishing"
+ "%@: ERROR could not resolve a parent directory for uuid=%@ (shared=%d)"
+ "%@: ERROR failed to get asset manifest from IOSurface with ID %u!"
+ "%@: ERROR failed to handle asset manifest, unable to generate a destination baseDirectory from inDictionary data!"
+ "%@: ERROR malformed published directory=%@ for uuid=%@"
+ "%@: ERROR manifest entryCount=%lu out of range"
+ "%@: ERROR manifest is missing its file or directory list"
+ "%@: ERROR no staged transfer for uuid=%@"
+ "%@: ERROR staged chunk for uuid=%@ has no file name!"
+ "%@: ERROR staged chunk for uuid=%@ names path=%@ which the manifest did not declare!"
+ "%@: ERROR staged chunk path=%@ escapes staging directory=%@"
+ "%@: Opened staged transfer uuid=%@ fileCount=%lu staging=%@"
+ "%@: Published asset uuid=%@ at %@"
+ "%@: could not remove staging directory=%@ with error=%@"
+ "%@: dropping stale mapping for uuid=%@ (path=%@ is gone)"
+ "%@: found published asset for key=%@ at %@"
+ "%@: leaving shared asset in place for uuid=%@ at %@"
+ "%@: manifest empty directory escapes staging directory: %@"
+ "%@: manifest empty directory rejected: %@"
+ "%@: manifest file rejected: %@"
+ "%@: no asset held for uuid=%@; caller will transfer it"
+ "%@: shared cache path rejected (not absolute): %@"
+ "%@: shared cache stays disabled, %@ is not usable"
+ ".staging"
+ ".write-probe.%d"
+ "0123456789ABCDEFabcdef"
+ "assetContentDigest"
+ "assetManifestEmptyDirectories"
+ "assetManifestFiles"
+ "com.apple.appleneuralengine"
+ "com.apple.avp.ane.maintenance"
+ "inputIndexArrayCount"
+ "outputIndexArrayCount"
```
