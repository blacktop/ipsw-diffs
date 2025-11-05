## FSKit

> `/System/Library/Frameworks/FSKit.framework/Versions/A/FSKit`

```diff

-474.60.43.0.0
-  __TEXT.__text: 0x3f948
-  __TEXT.__auth_stubs: 0x960
-  __TEXT.__objc_methlist: 0x360c
-  __TEXT.__const: 0x368
-  __TEXT.__gcc_except_tab: 0xda8
-  __TEXT.__cstring: 0x3de5
-  __TEXT.__oslogstring: 0x28ea
-  __TEXT.__swift5_typeref: 0x16c
+531.101.1.0.0
+  __TEXT.__text: 0x422f0
+  __TEXT.__auth_stubs: 0xaa0
+  __TEXT.__objc_methlist: 0x4324
+  __TEXT.__const: 0x380
+  __TEXT.__gcc_except_tab: 0xe5c
+  __TEXT.__cstring: 0x3e5f
+  __TEXT.__oslogstring: 0x2bf5
+  __TEXT.__swift5_typeref: 0x1d1
+  __TEXT.__swift5_capture: 0x58
   __TEXT.__swift5_reflstr: 0x16
   __TEXT.__swift5_assocty: 0x48
   __TEXT.__swift5_proto: 0x14

   __TEXT.__constg_swiftt: 0x210
   __TEXT.__swift5_protos: 0x8
   __TEXT.__swift5_types: 0x8
-  __TEXT.__unwind_info: 0x1178
-  __TEXT.__objc_classname: 0x81c
-  __TEXT.__objc_methname: 0x8d08
-  __TEXT.__objc_methtype: 0x3197
-  __TEXT.__objc_stubs: 0x5120
-  __DATA_CONST.__got: 0x3c0
-  __DATA_CONST.__const: 0x2a8
-  __DATA_CONST.__objc_classlist: 0x200
+  __TEXT.__swift_as_entry: 0x8
+  __TEXT.__swift_as_ret: 0x8
+  __TEXT.__unwind_info: 0x1228
+  __TEXT.__eh_frame: 0x138
+  __TEXT.__objc_classname: 0x825
+  __TEXT.__objc_methname: 0x9398
+  __TEXT.__objc_methtype: 0x325e
+  __TEXT.__objc_stubs: 0x5480
+  __DATA_CONST.__got: 0x3e8
+  __DATA_CONST.__const: 0x2c8
+  __DATA_CONST.__objc_classlist: 0x208
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x140
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1fd0
+  __DATA_CONST.__objc_selrefs: 0x22b0
   __DATA_CONST.__objc_protorefs: 0xe8
-  __DATA_CONST.__objc_superrefs: 0x168
+  __DATA_CONST.__objc_superrefs: 0x190
   __DATA_CONST.__objc_arraydata: 0x30
-  __AUTH_CONST.__auth_got: 0x4c0
-  __AUTH_CONST.__const: 0x16b0
-  __AUTH_CONST.__cfstring: 0x1ca0
-  __AUTH_CONST.__objc_const: 0x7ff0
+  __AUTH_CONST.__auth_got: 0x560
+  __AUTH_CONST.__const: 0x15c8
+  __AUTH_CONST.__cfstring: 0x1e40
+  __AUTH_CONST.__objc_const: 0x7018
   __AUTH_CONST.__objc_arrayobj: 0x30
-  __AUTH.__objc_data: 0x1540
+  __AUTH.__objc_data: 0x1590
   __AUTH.__data: 0x80
-  __DATA.__objc_ivar: 0x3d4
-  __DATA.__data: 0xf60
-  __DATA.__bss: 0x350
+  __DATA.__objc_ivar: 0x3f4
+  __DATA.__data: 0xf88
+  __DATA.__bss: 0x360
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/Versions/A/CoreServices
   - /System/Library/Frameworks/ExtensionFoundation.framework/Versions/A/ExtensionFoundation

   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswift_errno.dylib
   - /usr/lib/swift/libswift_math.dylib
   - /usr/lib/swift/libswift_signal.dylib

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 0A16DE15-8A1F-3566-A29F-6D6F7FDE7A4B
-  Functions: 1792
-  Symbols:   3957
-  CStrings:  2926
+  UUID: AB107FD7-7BF7-3E6D-8029-C08C0FDF5487
+  Functions: 1884
+  Symbols:   4102
+  CStrings:  3059
 
Symbols:
+ +[FSAuditToken getOurToken].cold.1
+ +[FSBlockDeviceBufferResource dynamicCast:]
+ +[FSBlockDeviceResource(Private) proxyResourceForBSDName:isWritable:]
+ +[FSClient sharedInstance]
+ +[FSClient sharedInstance].cold.1
+ +[FSClient(Private) new]
+ +[FSContainerStatus activeWithStatus:]
+ +[FSContainerStatus active]
+ +[FSContainerStatus blockedWithStatus:]
+ +[FSContainerStatus notReadyWithStatus:]
+ +[FSContainerStatus readyWithStatus:]
+ +[FSContainerStatus ready]
+ +[FSKitConstants(project) errorTypes].cold.1
+ +[FSKitConstants(project) plistTypes].cold.1
+ +[FSMetadataRange rangeWithOffset:segmentLength:segmentCount:]
+ +[FSModuleVolume(Project) volumeWithName:resource:]
+ +[FSProbeResult notRecognizedProbeResult]
+ +[FSProbeResult recognizedProbeResultWithName:containerID:]
+ +[FSProbeResult usableButLimitedProbeResultWithName:containerID:]
+ +[FSProbeResult usableButLimitedProbeResult]
+ +[FSProbeResult usableProbeResultWithName:containerID:]
+ +[FSProbeResult(Private) cantReadContainerID]
+ +[FSProbeResult(Private) newResult:name:containerID:]
+ +[FSProbeResult(Private) resultWithResult:name:containerID:]
+ +[FSTaskOptions supportsSecureCoding]
+ +[NSError(FSKitAdditions) fskit_initLocalizationStrings].cold.1
+ -[FSBlockDeviceBufferResource initBufferFromResource:].cold.3
+ -[FSBlockDeviceBufferResource initBufferFromResource:].cold.4
+ -[FSBlockDeviceResource asynchronousMetadataFlushWithError:]
+ -[FSBlockDeviceResource asynchronousMetadataFlushWithError:].cold.1
+ -[FSBlockDeviceResource delayedMetadataWriteFrom:startingAt:length:error:]
+ -[FSBlockDeviceResource limited]
+ -[FSBlockDeviceResource metadataClear:withDelayedWrites:error:]
+ -[FSBlockDeviceResource metadataClear:withDelayedWrites:error:].cold.1
+ -[FSBlockDeviceResource metadataClear:withDelayedWrites:error:].cold.2
+ -[FSBlockDeviceResource metadataFlushWithError:]
+ -[FSBlockDeviceResource metadataFlushWithError:].cold.1
+ -[FSBlockDeviceResource metadataPurge:error:]
+ -[FSBlockDeviceResource metadataPurge:error:].cold.1
+ -[FSBlockDeviceResource metadataPurge:error:].cold.2
+ -[FSBlockDeviceResource metadataReadInto:startingAt:length:error:]
+ -[FSBlockDeviceResource metadataWriteFrom:startingAt:length:error:]
+ -[FSBlockDeviceResource setLimited:]
+ -[FSBlockDeviceResource(Private) metadataReadInto:startingAt:length:readAheadExtents:readAheadCount:error:]
+ -[FSBlockDeviceResource(Private) metadataReadInto:startingAt:length:readAheadExtents:readAheadCount:error:].cold.1
+ -[FSBlockDeviceResource(Private) terminate]
+ -[FSBlockDeviceResource(Private) terminated]
+ -[FSClient fetchInstalledExtensionsWithCompletionHandler:]
+ -[FSClient initClient]
+ -[FSClient remoteObjectProxyWithErrorHandler:]
+ -[FSClient setupConnection]
+ -[FSClient setupConnection].cold.1
+ -[FSClient setupConnection].cold.2
+ -[FSClient synchronousRemoteObjectProxyWithErrorHandler:]
+ -[FSClient(Private) installedExtensionWithBundleID:synchronous:replyHandler:]
+ -[FSContainerStatus .cxx_destruct]
+ -[FSContainerStatus copyWithZone:]
+ -[FSContainerStatus initWithState:status:]
+ -[FSContainerStatus state]
+ -[FSContainerStatus status]
+ -[FSDirectoryEntryPacker .cxx_destruct]
+ -[FSDirectoryEntryPacker buffer]
+ -[FSDirectoryEntryPacker bytesPacked]
+ -[FSDirectoryEntryPacker outOfSpace]
+ -[FSDirectoryEntryPacker packEntryWithName:itemType:itemID:nextCookie:attributes:]
+ -[FSDirectoryEntryPacker packEntryWithName:itemType:itemID:nextCookie:attributes:].cold.1
+ -[FSDirectoryEntryPacker packEntryWithName:itemType:itemID:nextCookie:attributes:].cold.2
+ -[FSDirectoryEntryPacker packEntryWithName:itemType:itemID:nextCookie:attributes:].cold.3
+ -[FSDirectoryEntryPacker setBuffer:]
+ -[FSDirectoryEntryPacker setBytesPacked:]
+ -[FSDirectoryEntryPacker setOutOfSpace:]
+ -[FSDirectoryEntryPacker setWithAttributes:]
+ -[FSDirectoryEntryPacker withAttributes]
+ -[FSDirectoryEntryPacker(Project) initWithBuffer:withAttributes:]
+ -[FSDirectoryEntryPacker(Project) setLastEntryAsEOF]
+ -[FSEntityIdentifier initWithUUID:qualifier:]
+ -[FSExtentPacker .cxx_destruct]
+ -[FSExtentPacker buffer]
+ -[FSExtentPacker bytesPacked]
+ -[FSExtentPacker extentsPacked]
+ -[FSExtentPacker outOfSpace]
+ -[FSExtentPacker packExtentWithResource:type:logicalOffset:physicalOffset:length:]
+ -[FSExtentPacker setBuffer:]
+ -[FSExtentPacker setBytesPacked:]
+ -[FSExtentPacker setExtentsPacked:]
+ -[FSExtentPacker setOutOfSpace:]
+ -[FSExtentPacker(Project) extentDataByExtentsPacked]
+ -[FSExtentPacker(Project) extentData]
+ -[FSExtentPacker(Project) initWithBlockmapFlags:]
+ -[FSExtentPacker(Project) initWithExtentCount:]
+ -[FSExtentPacker(Project) initWithLength:]
+ -[FSFileSystem containerStatus]
+ -[FSFileSystem init]
+ -[FSFileSystem setContainerStatus:]
+ -[FSGenericURLResource(Private) initAsSecureURL:readonly:]
+ -[FSGenericURLResource(Private) initWithURL:]
+ -[FSMetadataRange initWithOffset:segmentLength:segmentCount:]
+ -[FSMetadataRange segmentCount]
+ -[FSMetadataRange segmentLength]
+ -[FSMetadataRange startOffset]
+ -[FSModuleConnector probeResource:replyHandler:].cold.2
+ -[FSModuleHost moduleOrder]
+ -[FSModuleHost setModuleOrder:]
+ -[FSModuleVolume supportsItemDeactivation]
+ -[FSModuleVolume(Project) fetchAndSetTypeForItem:replyHandler:]
+ -[FSModuleVolume(Project) getAndRemoveItemForFH:]
+ -[FSModuleVolume(Project) getItemForFH:]
+ -[FSModuleVolume(Project) getMaxFileSizeInBits]
+ -[FSModuleVolume(Project) getMaxFileSizeInBits].cold.1
+ -[FSModuleVolume(Project) getMaxXattrSizeInBits]
+ -[FSModuleVolume(Project) getMaxXattrSizeInBits].cold.1
+ -[FSModuleVolume(Project) initWithVolume:resource:]
+ -[FSModuleVolume(Project) insertIntoFHCache:]
+ -[FSModuleVolume(Project) listener:shouldAcceptNewConnection:]
+ -[FSModuleVolume(Project) listener:shouldAcceptNewConnection:].cold.1
+ -[FSModuleVolume(Project) newConnectionID:]
+ -[FSModuleVolume(Project) removeConnectionByID:]
+ -[FSModuleVolume(Project) removeFromFHCache:]
+ -[FSModuleVolume(Project) stopUsingVolume]
+ -[FSModuleVolume(Project) updateRootItem:replyHandler:]
+ -[FSMutableFileDataBuffer dealloc]
+ -[FSMutableFileDataBuffer dealloc].cold.1
+ -[FSMutableFileDataBuffer ensureMappedMB:]
+ -[FSMutableFileDataBuffer ensureMappedMB:].cold.1
+ -[FSMutableFileDataBuffer ensureMapped]
+ -[FSMutableFileDataBuffer initWithCapacity:andLength:]
+ -[FSMutableFileDataBuffer initWithCapacity:andLength:].cold.1
+ -[FSMutableFileDataBuffer initWithCapacity:andLength:].cold.2
+ -[FSMutableFileDataBuffer initWithCapacity:andLength:].cold.3
+ -[FSMutableFileDataBuffer initWithCoder:].cold.1
+ -[FSMutableFileDataBuffer initWithCoder:].cold.2
+ -[FSMutableFileDataBuffer initWithLength:]
+ -[FSMutableFileDataBuffer length]
+ -[FSResource(Private) initResource]
+ -[FSSettings settingsContainer].cold.1
+ -[FSStatFSResult _fixUpValues]
+ -[FSStatFSResult _fixUpValues].cold.1
+ -[FSStatFSResult initWithFileSystemTypeName:]
+ -[FSTaskOptions .cxx_destruct]
+ -[FSTaskOptions encodeWithCoder:]
+ -[FSTaskOptions extras]
+ -[FSTaskOptions initWithCoder:]
+ -[FSTaskOptions setExtras:]
+ -[FSTaskOptions setTaskOptions:]
+ -[FSTaskOptions taskOptions]
+ -[FSTaskOptions urlForOption:]
+ -[FSTaskOptions(Project) initWithOptions:]
+ -[FSTaskOptions(Project) initWithOptions:extras:]
+ -[FSTaskOptions(Project) setSecureURL:forKey:]
+ -[FSTaskOptions(Project) setSecureURL:forKey:].cold.1
+ -[FSTaskOptions(Project) setURL:forKey:]
+ -[FSTaskOptions(Project) setURL:forKey:].cold.1
+ -[FSTaskOptionsBundle enumerateOptionsUsingBlock:]
+ -[FSTaskOptionsBundle extras]
+ -[FSTaskOptionsBundle initWithOptionString:count:optionDictionary:errorHandler:]
+ -[FSTaskOptionsBundle mapStringToKind:]
+ -[FSTaskOptionsBundle setExtras:]
+ -[FSTaskOptionsBundle taskOptions]
+ -[FSUnaryFileSystem containerStatus]
+ -[FSUnaryFileSystem init]
+ -[FSUnaryFileSystem setContainerStatus:]
+ -[FSVolumeConnector blockmapFile:range:flags:operationID:replyHandler:]
+ -[FSVolumeConnector blockmapFile:range:flags:operationID:replyHandler:].cold.1
+ -[FSVolumeConnector blockmapFile:range:flags:operationID:replyHandler:].cold.2
+ -[FSVolumeConnector getStandardItemAttributesDataForItem:replyHandler:]
+ -[FSVolumeConnector getStandardItemAttributesDataForNewItem:replyHandler:]
+ -[FSVolumeConnector getStandardItemAttributesForItem:replyHandler:]
+ -[FSVolumeSupportedCapabilities caseFormat]
+ -[FSVolumeSupportedCapabilities setCaseFormat:]
+ GCC_except_table102
+ GCC_except_table105
+ GCC_except_table109
+ GCC_except_table111
+ GCC_except_table12
+ GCC_except_table13
+ GCC_except_table139
+ GCC_except_table18
+ GCC_except_table29
+ GCC_except_table35
+ GCC_except_table36
+ GCC_except_table39
+ GCC_except_table57
+ GCC_except_table61
+ GCC_except_table70
+ GCC_except_table77
+ GCC_except_table81
+ GCC_except_table88
+ GCC_except_table90
+ GCC_except_table93
+ GCC_except_table95
+ OBJC_IVAR_$_FSBlockDeviceResource._limited
+ OBJC_IVAR_$_FSContainerStatus._state
+ OBJC_IVAR_$_FSContainerStatus._status
+ OBJC_IVAR_$_FSDirectoryEntryPacker._buffer
+ OBJC_IVAR_$_FSDirectoryEntryPacker._bytesPacked
+ OBJC_IVAR_$_FSDirectoryEntryPacker._lastEntry
+ OBJC_IVAR_$_FSDirectoryEntryPacker._outOfSpace
+ OBJC_IVAR_$_FSDirectoryEntryPacker._withAttributes
+ OBJC_IVAR_$_FSExtentPacker._buffer
+ OBJC_IVAR_$_FSExtentPacker._bytesPacked
+ OBJC_IVAR_$_FSExtentPacker._extentsPacked
+ OBJC_IVAR_$_FSExtentPacker._outOfSpace
+ OBJC_IVAR_$_FSFileSystem._containerStatus
+ OBJC_IVAR_$_FSMetadataRange._segmentCount
+ OBJC_IVAR_$_FSMetadataRange._segmentLength
+ OBJC_IVAR_$_FSMetadataRange._startOffset
+ OBJC_IVAR_$_FSModuleVolume._supportsItemDeactivation
+ OBJC_IVAR_$_FSMutableFileDataBuffer._internalCapacity
+ OBJC_IVAR_$_FSMutableFileDataBuffer._length
+ OBJC_IVAR_$_FSMutableFileDataBuffer._mp
+ OBJC_IVAR_$_FSMutableFileDataBuffer._vma
+ OBJC_IVAR_$_FSResource._revoked
+ OBJC_IVAR_$_FSTaskOptions._extras
+ OBJC_IVAR_$_FSTaskOptions._taskOptions
+ OBJC_IVAR_$_FSTaskOptionsBundle._extras
+ OBJC_IVAR_$_FSUnaryFileSystem._containerStatus
+ OBJC_IVAR_$_FSVolumeSupportedCapabilities._caseFormat
+ _FSKitErrorVariantKey
+ _FSModuleIdentityAttributeSupportsGenericURLs
+ _FSModuleIdentityAttributeSupportsKOIO_OLD
+ _FSModuleIdentityAttributeSupportsPathURLs
+ _FSOperationIDUnspecified
+ _OBJC_CLASS_$_FSContainerStatus
+ _OBJC_CLASS_$_FSDirectoryEntryPacker
+ _OBJC_CLASS_$_FSExtentPacker
+ _OBJC_CLASS_$_FSMetadataRange
+ _OBJC_CLASS_$_FSTaskOptions
+ _OBJC_METACLASS_$_FSContainerStatus
+ _OBJC_METACLASS_$_FSDirectoryEntryPacker
+ _OBJC_METACLASS_$_FSExtentPacker
+ _OBJC_METACLASS_$_FSMetadataRange
+ _OBJC_METACLASS_$_FSTaskOptions
+ __106-[FSVolumeConnector renameItemIn:named:item:toDirectory:newName:toItem:usingFlags:requestID:replyHandler:]_block_invoke.453
+ __106-[FSVolumeConnector renameItemIn:named:item:toDirectory:newName:toItem:usingFlags:requestID:replyHandler:]_block_invoke.cold.1
+ __114-[FSVolumeConnector readDirectory:withAttr:requestedAttributes:intoBuffer:cookie:verifier:requestID:replyHandler:]_block_invoke.cold.1
+ __114-[FSVolumeConnector readDirectory:withAttr:requestedAttributes:intoBuffer:cookie:verifier:requestID:replyHandler:]_block_invoke.cold.2
+ __114-[FSVolumeConnector readDirectory:withAttr:requestedAttributes:intoBuffer:cookie:verifier:requestID:replyHandler:]_block_invoke.cold.3
+ __25-[FSClient setupHandlers]_block_invoke.56
+ __25-[FSClient setupHandlers]_block_invoke_2.57
+ __27-[FSClient setupConnection]_block_invoke.52
+ __29-[FSVolumeConnector unmount:]_block_invoke.cold.1
+ __39-[FSModuleConnector sendCloseResource:]_block_invoke.234
+ __39-[FSModuleConnector sendCloseResource:]_block_invoke.234.cold.1
+ __40-[FSModuleConnector sendRevokeResource:]_block_invoke.229
+ __40-[FSModuleConnector sendRevokeResource:]_block_invoke.229.cold.1
+ __40-[FSVolumeConnector mount:replyHandler:]_block_invoke.cold.1
+ __41-[FSClient(Private) installedExtensions:]_block_invoke.92
+ __48-[FSModuleConnector probeResource:replyHandler:]_block_invoke.cold.1
+ __48-[FSModuleConnector probeResource:replyHandler:]_block_invoke.cold.2
+ __51-[FSModuleConnector sendWipeResource:replyHandler:]_block_invoke.237
+ __51-[FSModuleConnector sendWipeResource:replyHandler:]_block_invoke.237.cold.1
+ __51-[FSModuleConnector sendWipeResource:replyHandler:]_block_invoke.237.cold.2
+ __52-[FSVolumeConnector reclaim:requestID:replyHandler:]_block_invoke.cold.1
+ __55-[FSModuleConnector loadResource:options:replyHandler:]_block_invoke.273
+ __55-[FSModuleConnector loadResource:options:replyHandler:]_block_invoke.278
+ __55-[FSModuleConnector loadResource:options:replyHandler:]_block_invoke.278.cold.1
+ __55-[FSModuleConnector loadResource:options:replyHandler:]_block_invoke.278.cold.2
+ __55-[FSModuleConnector loadResource:options:replyHandler:]_block_invoke.281
+ __55-[FSModuleConnector loadResource:options:replyHandler:]_block_invoke.cold.3
+ __55-[FSModuleConnector loadResource:options:replyHandler:]_block_invoke.cold.4
+ __55-[FSModuleConnector loadResource:options:replyHandler:]_block_invoke_2.282
+ __55-[FSModuleConnector loadResource:options:replyHandler:]_block_invoke_2.cold.1
+ __55-[FSModuleConnector loadResource:options:replyHandler:]_block_invoke_2.cold.2
+ __57-[FSModuleConnector unloadResource:options:replyHandler:]_block_invoke.292
+ __57-[FSVolumeConnector listXattrsOf:requestID:replyHandler:]_block_invoke.438
+ __57-[FSVolumeConnector listXattrsOf:requestID:replyHandler:]_block_invoke.cold.1
+ __57-[FSVolumeConnector listXattrsOf:requestID:replyHandler:]_block_invoke.cold.2
+ __57-[FSVolumeConnector listXattrsOf:requestID:replyHandler:]_block_invoke.cold.3
+ __58-[FSVolumeConnector open:withMode:requestID:replyHandler:]_block_invoke.cold.1
+ __58-[FSVolumeConnector open:withMode:requestID:replyHandler:]_block_invoke.cold.2
+ __58-[FSVolumeConnector xattrOf:named:requestID:replyHandler:]_block_invoke.cold.1
+ __58-[FSVolumeConnector xattrOf:named:requestID:replyHandler:]_block_invoke.cold.2
+ __58-[FSVolumeConnector xattrOf:named:requestID:replyHandler:]_block_invoke.cold.3
+ __62-[FSVolumeConnector close:keepingMode:requestID:replyHandler:]_block_invoke.cold.1
+ __62-[FSVolumeConnector close:keepingMode:requestID:replyHandler:]_block_invoke.cold.2
+ __63-[FSModuleVolume(Project) fetchAndSetTypeForItem:replyHandler:]_block_invoke.cold.1
+ __63-[FSModuleVolume(Project) fetchAndSetTypeForItem:replyHandler:]_block_invoke.cold.2
+ __63-[FSVolumeConnector readSymbolicLinkOf:requestID:replyHandler:]_block_invoke.428
+ __63-[FSVolumeConnector readSymbolicLinkOf:requestID:replyHandler:]_block_invoke.cold.1
+ __63-[FSVolumeConnector readSymbolicLinkOf:requestID:replyHandler:]_block_invoke.cold.2
+ __64-[FSVolumeConnector lookupIn:name:flags:requestID:replyHandler:]_block_invoke.396
+ __64-[FSVolumeConnector lookupIn:name:flags:requestID:replyHandler:]_block_invoke.400
+ __64-[FSVolumeConnector lookupIn:name:flags:requestID:replyHandler:]_block_invoke.cold.1
+ __64-[FSVolumeConnector lookupIn:name:flags:requestID:replyHandler:]_block_invoke_2.401
+ __64-[FSVolumeConnector lookupIn:name:flags:requestID:replyHandler:]_block_invoke_3.cold.1
+ __66-[FSModuleConnector activateVolume:resource:options:replyHandler:]_block_invoke.296
+ __66-[FSModuleConnector activateVolume:resource:options:replyHandler:]_block_invoke_2.299
+ __66-[FSModuleConnector activateVolume:resource:options:replyHandler:]_block_invoke_2.299.cold.1
+ __66-[FSModuleConnector activateVolume:resource:options:replyHandler:]_block_invoke_2.cold.3
+ __67-[FSVolumeConnector getStandardItemAttributesForItem:replyHandler:]_block_invoke.cold.1
+ __67-[FSVolumeConnector getStandardItemAttributesForItem:replyHandler:]_block_invoke.cold.2
+ __67-[FSVolumeConnector setFileAttributesOf:to:requestID:replyHandler:]_block_invoke.cold.1
+ __67-[FSVolumeConnector setFileAttributesOf:to:requestID:replyHandler:]_block_invoke.cold.2
+ __69-[FSModuleConnector checkWithOptions:connection:taskID:replyHandler:]_block_invoke.257
+ __69-[FSModuleConnector checkWithOptions:connection:taskID:replyHandler:]_block_invoke.259
+ __69-[FSModuleConnector checkWithOptions:connection:taskID:replyHandler:]_block_invoke_2.260
+ __70-[FSModuleConnector formatWithOptions:connection:taskID:replyHandler:]_block_invoke.269
+ __70-[FSModuleConnector formatWithOptions:connection:taskID:replyHandler:]_block_invoke_2.270
+ __71-[FSVolumeConnector blockmapFile:range:flags:operationID:replyHandler:]_block_invoke.cold.1
+ __71-[FSVolumeConnector endIO:range:status:flags:operationID:replyHandler:]_block_invoke.cold.1
+ __71-[FSVolumeConnector setXattrOf:named:value:how:requestID:replyHandler:]_block_invoke.cold.1
+ __72-[FSVolumeConnector writeTo:atOffset:fromBuffer:requestID:replyHandler:]_block_invoke.cold.1
+ __72-[FSVolumeConnector writeTo:atOffset:fromBuffer:requestID:replyHandler:]_block_invoke.cold.2
+ __73-[FSModuleHost(Project) _updateProviderListForFilteredFSModileInstances:]_block_invoke.187
+ __73-[FSModuleHost(Project) _updateProviderListForFilteredFSModileInstances:]_block_invoke_2.189
+ __73-[FSVolumeConnector makeLinkOf:named:inDirectory:requestID:replyHandler:]_block_invoke.432
+ __73-[FSVolumeConnector makeLinkOf:named:inDirectory:requestID:replyHandler:]_block_invoke.cold.2
+ __73-[FSVolumeConnector readFrom:atOffset:intoBuffer:requestID:replyHandler:]_block_invoke.cold.1
+ __73-[FSVolumeConnector readFrom:atOffset:intoBuffer:requestID:replyHandler:]_block_invoke.cold.2
+ __74-[FSClient(Private) validateVolumeName:usingBundle:volumeID:replyHandler:]_block_invoke.cold.1
+ __74-[FSModuleConnector checkResource:options:connection:taskID:replyHandler:]_block_invoke.244
+ __74-[FSModuleConnector checkResource:options:connection:taskID:replyHandler:]_block_invoke.247
+ __74-[FSModuleConnector checkResource:options:connection:taskID:replyHandler:]_block_invoke.247.cold.1
+ __74-[FSModuleConnector checkResource:options:connection:taskID:replyHandler:]_block_invoke.248
+ __74-[FSVolumeConnector checkAccessTo:requestedAccess:requestID:replyHandler:]_block_invoke.cold.1
+ __75-[FSModuleConnector formatResource:options:connection:taskID:replyHandler:]_block_invoke.263
+ __75-[FSModuleConnector formatResource:options:connection:taskID:replyHandler:]_block_invoke.263.cold.1
+ __75-[FSModuleConnector formatResource:options:connection:taskID:replyHandler:]_block_invoke_2.264
+ __75-[FSVolumeConnector createIn:named:type:attributes:requestID:replyHandler:]_block_invoke.393
+ __75-[FSVolumeConnector createIn:named:type:attributes:requestID:replyHandler:]_block_invoke.cold.1
+ __75-[FSVolumeConnector createIn:named:type:attributes:requestID:replyHandler:]_block_invoke.cold.2
+ __75-[FSVolumeConnector createIn:named:type:attributes:requestID:replyHandler:]_block_invoke_3.cold.1
+ __76-[FSVolumeConnector setOtherAttributeOf:named:value:requestID:replyHandler:]_block_invoke.384
+ __76-[FSVolumeConnector setOtherAttributeOf:named:value:requestID:replyHandler:]_block_invoke.384.cold.1
+ __76-[FSVolumeConnector setOtherAttributeOf:named:value:requestID:replyHandler:]_block_invoke.391
+ __77-[FSVolumeConnector removeItem:from:named:usingFlags:requestID:replyHandler:]_block_invoke.411
+ __79-[FSVolumeConnector fileAttributes:requestedAttributes:requestID:replyHandler:]_block_invoke.cold.1
+ __82-[FSVolumeConnector removeDirectory:from:named:usingFlags:requestID:replyHandler:]_block_invoke.406
+ __83+[FSBlockDeviceResource(Project) openWithBSDName:writable:auditToken:replyHandler:]_block_invoke.200
+ __83+[FSBlockDeviceResource(Project) openWithBSDName:writable:auditToken:replyHandler:]_block_invoke.200.cold.1
+ __84-[FSVolumeConnector makeSymlinkIn:named:contents:attributes:requestID:replyHandler:]_block_invoke.431
+ __84-[FSVolumeConnector makeSymlinkIn:named:contents:attributes:requestID:replyHandler:]_block_invoke.cold.1
+ __84-[FSVolumeConnector makeSymlinkIn:named:contents:attributes:requestID:replyHandler:]_block_invoke.cold.2
+ __87+[FSKitDiskArbHelper DAMountFSKitVolume:deviceName:mountPoint:volumeName:mountOptions:]_block_invoke.31
+ __87+[FSKitDiskArbHelper DAMountFSKitVolume:deviceName:mountPoint:volumeName:mountOptions:]_block_invoke.31.cold.1
+ __87+[FSKitDiskArbHelper DAMountFSKitVolume:deviceName:mountPoint:volumeName:mountOptions:]_block_invoke.31.cold.2
+ __87+[FSKitDiskArbHelper DAMountFSKitVolume:deviceName:mountPoint:volumeName:mountOptions:]_block_invoke.31.cold.3
+ __87+[FSKitDiskArbHelper DAMountFSKitVolume:deviceName:mountPoint:volumeName:mountOptions:]_block_invoke.37
+ __87+[FSKitDiskArbHelper DAMountFSKitVolume:deviceName:mountPoint:volumeName:mountOptions:]_block_invoke.37.cold.1
+ __87+[FSKitDiskArbHelper DAMountFSKitVolume:deviceName:mountPoint:volumeName:mountOptions:]_block_invoke.37.cold.2
+ __87+[FSKitDiskArbHelper DAMountFSKitVolume:deviceName:mountPoint:volumeName:mountOptions:]_block_invoke.39
+ __87+[FSKitDiskArbHelper DAMountFSKitVolume:deviceName:mountPoint:volumeName:mountOptions:]_block_invoke.39.cold.1
+ __96-[FSVolumeConnector makeCloneOf:named:inDirectory:attributes:usingFlags:requestID:replyHandler:]_block_invoke.446
+ __OBJC_$_CLASS_METHODS_FSClient(Private|Project)
+ __OBJC_$_CLASS_METHODS_FSContainerStatus
+ __OBJC_$_CLASS_METHODS_FSEntityIdentifier(FSEntityIdentifier_project)
+ __OBJC_$_CLASS_METHODS_FSMetadataRange
+ __OBJC_$_CLASS_METHODS_FSModuleVolume(Project)
+ __OBJC_$_CLASS_METHODS_FSProbeResult(Private)
+ __OBJC_$_CLASS_METHODS_FSTaskOptions
+ __OBJC_$_CLASS_METHODS_FSVolume(FSKit_private)
+ __OBJC_$_CLASS_PROP_LIST_FSClient
+ __OBJC_$_CLASS_PROP_LIST_FSContainerStatus
+ __OBJC_$_CLASS_PROP_LIST_FSMutableFileDataBuffer
+ __OBJC_$_CLASS_PROP_LIST_FSTaskOptions
+ __OBJC_$_INSTANCE_METHODS_FSContainerStatus
+ __OBJC_$_INSTANCE_METHODS_FSDirectoryEntryPacker(Project)
+ __OBJC_$_INSTANCE_METHODS_FSEntityIdentifier(FSEntityIdentifier_project)
+ __OBJC_$_INSTANCE_METHODS_FSExtentPacker(Project)
+ __OBJC_$_INSTANCE_METHODS_FSGenericURLResource(Private)
+ __OBJC_$_INSTANCE_METHODS_FSMetadataRange
+ __OBJC_$_INSTANCE_METHODS_FSModuleVolume(Project)
+ __OBJC_$_INSTANCE_METHODS_FSTaskOptions(Project)
+ __OBJC_$_INSTANCE_METHODS_FSVolume
+ __OBJC_$_INSTANCE_VARIABLES_FSContainerStatus
+ __OBJC_$_INSTANCE_VARIABLES_FSDirectoryEntryPacker
+ __OBJC_$_INSTANCE_VARIABLES_FSExtentPacker
+ __OBJC_$_INSTANCE_VARIABLES_FSMetadataRange
+ __OBJC_$_INSTANCE_VARIABLES_FSMutableFileDataBuffer
+ __OBJC_$_INSTANCE_VARIABLES_FSTaskOptions
+ __OBJC_$_PROP_LIST_FSContainerStatus
+ __OBJC_$_PROP_LIST_FSExtentPacker
+ __OBJC_$_PROP_LIST_FSMetadataRange
+ __OBJC_$_PROP_LIST_FSMutableFileDataBuffer
+ __OBJC_$_PROP_LIST_FSTaskOptions
+ __OBJC_$_PROP_LIST_FSVolumeItemDeactivation
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_FSFileSystemOperations
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_FSManageableResourceMaintenanceOperations
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_FSVolumeItemDeactivation
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_FSVolumeKernelOffloadedIOOperations
+ __OBJC_$_PROTOCOL_METHOD_TYPES_FSVolumeItemDeactivation
+ __OBJC_$_PROTOCOL_REFS_FSVolumeItemDeactivation
+ __OBJC_CLASS_PROTOCOLS_$_FSContainerStatus
+ __OBJC_CLASS_PROTOCOLS_$_FSModuleVolume(Project)
+ __OBJC_CLASS_PROTOCOLS_$_FSMutableFileDataBuffer
+ __OBJC_CLASS_PROTOCOLS_$_FSTaskOptions
+ __OBJC_CLASS_RO_$_FSContainerStatus
+ __OBJC_CLASS_RO_$_FSDirectoryEntryPacker
+ __OBJC_CLASS_RO_$_FSExtentPacker
+ __OBJC_CLASS_RO_$_FSMetadataRange
+ __OBJC_CLASS_RO_$_FSTaskOptions
+ __OBJC_LABEL_PROTOCOL_$_FSVolumeItemDeactivation
+ __OBJC_METACLASS_RO_$_FSContainerStatus
+ __OBJC_METACLASS_RO_$_FSDirectoryEntryPacker
+ __OBJC_METACLASS_RO_$_FSExtentPacker
+ __OBJC_METACLASS_RO_$_FSMetadataRange
+ __OBJC_METACLASS_RO_$_FSTaskOptions
+ __OBJC_PROTOCOL_$_FSVolumeItemDeactivation
+ __OBJC_PROTOCOL_REFERENCE_$_FSVolumeItemDeactivation
+ ___106-[FSVolumeConnector renameItemIn:named:item:toDirectory:newName:toItem:usingFlags:requestID:replyHandler:]_block_invoke_4
+ ___106-[FSVolumeConnector renameItemIn:named:item:toDirectory:newName:toItem:usingFlags:requestID:replyHandler:]_block_invoke_5
+ ___106-[FSVolumeConnector renameItemIn:named:item:toDirectory:newName:toItem:usingFlags:requestID:replyHandler:]_block_invoke_6
+ ___106-[FSVolumeConnector renameItemIn:named:item:toDirectory:newName:toItem:usingFlags:requestID:replyHandler:]_block_invoke_7
+ ___106-[FSVolumeConnector renameItemIn:named:item:toDirectory:newName:toItem:usingFlags:requestID:replyHandler:]_block_invoke_8
+ ___26+[FSClient sharedInstance]_block_invoke
+ ___27-[FSClient setupConnection]_block_invoke
+ ___40-[FSModuleVolume(Project) getItemForFH:]_block_invoke
+ ___45-[FSModuleVolume(Project) insertIntoFHCache:]_block_invoke
+ ___45-[FSModuleVolume(Project) removeFromFHCache:]_block_invoke
+ ___49-[FSModuleVolume(Project) getAndRemoveItemForFH:]_block_invoke
+ ___55-[FSModuleVolume(Project) updateRootItem:replyHandler:]_block_invoke
+ ___62-[FSModuleVolume(Project) listener:shouldAcceptNewConnection:]_block_invoke
+ ___63-[FSModuleVolume(Project) fetchAndSetTypeForItem:replyHandler:]_block_invoke
+ ___67-[FSVolumeConnector getStandardItemAttributesForItem:replyHandler:]_block_invoke
+ ___70-[FSModuleConnector formatWithOptions:connection:taskID:replyHandler:]_block_invoke_3
+ ___71-[FSVolumeConnector blockmapFile:range:flags:operationID:replyHandler:]_block_invoke
+ ___71-[FSVolumeConnector getStandardItemAttributesDataForItem:replyHandler:]_block_invoke
+ ___73-[FSVolumeConnector makeLinkOf:named:inDirectory:requestID:replyHandler:]_block_invoke_3
+ ___73-[FSVolumeConnector makeLinkOf:named:inDirectory:requestID:replyHandler:]_block_invoke_4
+ ___74-[FSClient(Private) validateVolumeName:usingBundle:volumeID:replyHandler:]_block_invoke
+ ___74-[FSVolumeConnector getStandardItemAttributesDataForNewItem:replyHandler:]_block_invoke
+ ___75-[FSVolumeConnector createIn:named:type:attributes:requestID:replyHandler:]_block_invoke_3
+ ___77-[FSClient(Private) installedExtensionWithBundleID:synchronous:replyHandler:]_block_invoke
+ ___77-[FSClient(Private) installedExtensionWithBundleID:synchronous:replyHandler:]_block_invoke_2
+ ___77-[FSClient(Private) installedExtensionWithBundleID:synchronous:replyHandler:]_block_invoke_3
+ ___77-[FSVolumeConnector removeItem:from:named:usingFlags:requestID:replyHandler:]_block_invoke_3
+ ___77-[FSVolumeConnector removeItem:from:named:usingFlags:requestID:replyHandler:]_block_invoke_4
+ ___84-[FSVolumeConnector makeSymlinkIn:named:contents:attributes:requestID:replyHandler:]_block_invoke_3
+ ___84-[FSVolumeConnector makeSymlinkIn:named:contents:attributes:requestID:replyHandler:]_block_invoke_4
+ ___96-[FSVolumeConnector makeCloneOf:named:inDirectory:attributes:usingFlags:requestID:replyHandler:]_block_invoke_3
+ ___96-[FSVolumeConnector makeCloneOf:named:inDirectory:attributes:usingFlags:requestID:replyHandler:]_block_invoke_4
+ ___block_descriptor_108_e8_32s40s48s56s64s72s80s88bs96r_e5_v8?0l
+ ___block_descriptor_116_e8_32s40s48s56s64s72s80s88s96r104r_e36_v32?0"FSVolumeDescription"8Q16^B24l
+ ___block_descriptor_40_e8_32bs_e26_v16?0"FSItemAttributes"8l
+ ___block_descriptor_40_e8_32bs_e30_v24?0"FSVolume"8"NSError"16l
+ ___block_descriptor_40_e8_32r_e38_v24?0"FSModuleIdentity"8"NSError"16l
+ ___block_descriptor_41_e8_32w_e5_v8?0l
+ ___block_descriptor_48_e8_32s40bs_e16_v16?0"NSData"8l
+ ___block_descriptor_48_e8_32s40bs_e26_v16?0"FSItemAttributes"8l
+ ___block_descriptor_48_e8_32s40bs_e38_v24?0"FSItemAttributes"8"NSError"16l
+ ___block_descriptor_56_e8_32s40s48bs_e16_v16?0"NSData"8l
+ ___block_descriptor_64_e8_32s40s48s56bs_e16_v16?0"NSData"8l
+ ___block_descriptor_64_e8_32s40s48s56bs_e35_v24?0"FSProbeResult"8"NSError"16l
+ ___block_descriptor_72_e8_32s40s48bs56r_e20_v24?0Q8"NSError"16l
+ ___block_descriptor_72_e8_32s40s48s56bs64bs_e5_v8?0l
+ ___block_descriptor_72_e8_32s40s48s56r64r_e25_v32?0"FSVolume"8Q16^B24l
+ ___block_descriptor_72_e8_32s40s48s56s64bs_e16_v16?0"NSData"8l
+ ___block_descriptor_80_e8_32s40s48s56bs64r72r_e5_v8?0l
+ ___block_descriptor_80_e8_32s40s48s56s64s72bs_e16_v16?0"NSData"8l
+ ___block_descriptor_84_e8_32s40s48s56s64bs72r_e43_v32?0"FSItem"8"FSFileName"16"NSError"24l
+ ___block_descriptor_88_e8_32s40s48s56s64bs72r80r_e29_v24?0"NSArray"8"NSError"16l
+ ___block_descriptor_88_e8_32s40s48s56s64s72r80r_e20_v20?0B8"NSError"12l
+ ___block_descriptor_88_e8_32s40s48s56s64s72s80bs_e16_v16?0"NSData"8l
+ ___block_descriptor_88_e8_32s40s48s56s64s72s80bs_e43_v32?0"FSItem"8"FSFileName"16"NSError"24l
+ ___block_descriptor_92_e8_32s40s48s56s64s72bs80r_e16_v16?0"NSData"8l
+ ___copy_helper_block_e8_32s40s48s56b64b
+ ___copy_helper_block_e8_32s40s48s56r64r
+ ___copy_helper_block_e8_32s40s48s56s64b72r
+ ___copy_helper_block_e8_32s40s48s56s64s72b80r
+ ___copy_helper_block_e8_32s40s48s56s64s72r80r
+ ___copy_helper_block_e8_32s40s48s56s64s72s80s88b96r
+ ___copy_helper_block_e8_32s40s48s56s64s72s80s88s96r104r
+ ___destroy_helper_block_e8_32s40s48s56r64r
+ ___destroy_helper_block_e8_32s40s48s56s64s72r
+ ___destroy_helper_block_e8_32s40s48s56s64s72s80r
+ ___destroy_helper_block_e8_32s40s48s56s64s72s80s88s96r
+ ___destroy_helper_block_e8_32s40s48s56s64s72s80s88s96r104r
+ ___swift_async_entry_functlets
+ ___swift_async_ret_functlets
+ __block_literal_global.157
+ __block_literal_global.181
+ __block_literal_global.183
+ __block_literal_global.231
+ __block_literal_global.233
+ __block_literal_global.252
+ __block_literal_global.262
+ __block_literal_global.266
+ __block_literal_global.272
+ __block_literal_global.298
+ __block_literal_global.316
+ _dispatch_group_notify
+ _objc_msgSend$_fixUpValues
+ _objc_msgSend$blockmapFile:offset:length:flags:operationID:packer:replyHandler:
+ _objc_msgSend$bufferFromResource:
+ _objc_msgSend$bytesPacked
+ _objc_msgSend$cantReadContainerID
+ _objc_msgSend$caseFormat
+ _objc_msgSend$completeIOForFile:offset:length:status:flags:operationID:replyHandler:
+ _objc_msgSend$containerStatus
+ _objc_msgSend$deactivateItem:replyHandler:
+ _objc_msgSend$decodeArrayOfObjectsOfClass:forKey:
+ _objc_msgSend$decodeDictionaryWithKeysOfClass:objectsOfClass:forKey:
+ _objc_msgSend$extentData
+ _objc_msgSend$extentDataByExtentsPacked
+ _objc_msgSend$extentsPacked
+ _objc_msgSend$fetchAndSetTypeForItem:replyHandler:
+ _objc_msgSend$getStandardItemAttributesDataForItem:replyHandler:
+ _objc_msgSend$getStandardItemAttributesDataForNewItem:replyHandler:
+ _objc_msgSend$getStandardItemAttributesForItem:replyHandler:
+ _objc_msgSend$initClient
+ _objc_msgSend$initFileURLWithPath:isDirectory:
+ _objc_msgSend$initWithBlockmapFlags:
+ _objc_msgSend$initWithBuffer:withAttributes:
+ _objc_msgSend$initWithDictionary:
+ _objc_msgSend$initWithExtentCount:
+ _objc_msgSend$initWithOffset:segmentLength:segmentCount:
+ _objc_msgSend$initWithOptionString:count:optionDictionary:errorHandler:
+ _objc_msgSend$initWithOptions:extras:
+ _objc_msgSend$initWithState:status:
+ _objc_msgSend$initWithUTF8String:
+ _objc_msgSend$initWithUUID:qualifier:
+ _objc_msgSend$installedExtensionWithBundleID:replyHandler:
+ _objc_msgSend$installedExtensionWithBundleID:synchronous:replyHandler:
+ _objc_msgSend$itemDeactivationPolicy
+ _objc_msgSend$limited
+ _objc_msgSend$lookupItemNamed:inDirectory:packer:replyHandler:
+ _objc_msgSend$mapStringToKind:
+ _objc_msgSend$notReadyWithStatus:
+ _objc_msgSend$outOfSpace
+ _objc_msgSend$preallocateSpaceForFile:atOffset:length:flags:packer:replyHandler:
+ _objc_msgSend$preallocateSpaceForItem:atOffset:length:flags:replyHandler:
+ _objc_msgSend$restrictsOwnershipChanges
+ _objc_msgSend$segmentCount
+ _objc_msgSend$segmentLength
+ _objc_msgSend$setInhibitKernelOffloadedIO:
+ _objc_msgSend$setLastEntryAsEOF
+ _objc_msgSend$setupConnection
+ _objc_msgSend$sharedInstance
+ _objc_msgSend$startCheckWithTask:options:error:
+ _objc_msgSend$startFormatWithTask:options:error:
+ _objc_msgSend$startOffset
+ _objc_msgSend$status
+ _objc_msgSend$supportsItemDeactivation
+ _objc_msgSend$taskOptions
+ _objc_msgSend$terminated
+ _objc_msgSend$updateRootItem:replyHandler:
+ _objc_msgSend$usedBlocks
+ _objc_msgSend$usedBytes
+ _objc_msgSend$wantedAttributes
+ _objc_msgSend$xattrOperationsInhibited
+ _objectdestroyTm
+ _swift_allocError
+ _swift_deallocObject
+ _swift_dynamicCast
+ _swift_errorRetain
+ _swift_getEnumCaseMultiPayload
+ _swift_isEscapingClosureAtFileLocation
+ _swift_storeEnumTagMultiPayload
+ _swift_task_alloc
+ _swift_task_dealloc
+ _swift_task_switch
+ _swift_willThrowTypedImpl
+ _symbolic B0
+ _symbolic B1
+ _symbolic ScCySi______pG s5ErrorP
+ _symbolic So23FSMutableFileDataBufferC
+ _symbolic SvIgy_
+ _symbolic Swxq_Igyrzr_
+ _symbolic ______p s5ErrorP
+ _symbolic _____yxq_GSg s6ResultOsRi_zrlE
+ _symbolic q_
+ block_copy_helper.14
+ block_copy_helper.5
+ block_copy_helper.8
+ block_descriptor.10
+ block_descriptor.16
+ block_descriptor.7
+ block_destroy_helper.15
+ block_destroy_helper.6
+ block_destroy_helper.9
+ fskitLocalizationBundle.cold.1
+ fskit_std_log.cold.1
+ sharedInstance.onceToken
+ sharedInstance.sharedInstance
- +[FSBlockDeviceResource proxyResourceForBSDName:isWritable:]
- +[FSClient fetchInstalledExtensionsWithCompletionHandler:]
- +[FSEntityIdentifier identifierWithUUID:]
- +[FSEntityIdentifier identifierWithUUID:byteQualifier:]
- +[FSEntityIdentifier identifierWithUUID:data:]
- +[FSEntityIdentifier identifierWithUUID:longByteQualifier:]
- +[FSEntityIdentifier identifier]
- +[FSFileDataBuffer dataWithLength:]
- +[FSFileDataBuffer supportsSecureCoding]
- +[FSMetadataBlockRange rangeWithOffset:blockLength:numberOfBlocks:]
- +[FSModuleVolume volumeWithName:resource:]
- +[FSProbeResult newResult:name:containerID:]
- +[FSProbeResult resultWithResult:name:containerID:]
- +[FSVolume(Project) extentPackerForBuffer:bufLen:extentCount:]
- +[FSVolume(Project) newDirEntryPacker:bufLen:bytesPacked:withAttr:]
- -[FSBlockDeviceResource asynchronousMetadataFlush]
- -[FSBlockDeviceResource asynchronousMetadataFlush].cold.1
- -[FSBlockDeviceResource delayedMetadataWriteFrom:startingAt:length:]
- -[FSBlockDeviceResource isTerminated]
- -[FSBlockDeviceResource metadataClear:wait:]
- -[FSBlockDeviceResource metadataClear:wait:].cold.1
- -[FSBlockDeviceResource metadataClear:wait:].cold.2
- -[FSBlockDeviceResource metadataFlush]
- -[FSBlockDeviceResource metadataFlush].cold.1
- -[FSBlockDeviceResource metadataPurge:]
- -[FSBlockDeviceResource metadataPurge:].cold.1
- -[FSBlockDeviceResource metadataPurge:].cold.2
- -[FSBlockDeviceResource metadataReadInto:startingAt:length:]
- -[FSBlockDeviceResource metadataReadInto:startingAt:length:readAheadExtents:readAheadCount:]
- -[FSBlockDeviceResource metadataReadInto:startingAt:length:readAheadExtents:readAheadCount:].cold.1
- -[FSBlockDeviceResource metadataWriteFrom:startingAt:length:]
- -[FSBlockDeviceResource terminate]
- -[FSBlockDeviceResource terminated]
- -[FSClient conn]
- -[FSClient init]
- -[FSClient init].cold.1
- -[FSClient setConn:]
- -[FSEntityIdentifier initWithUUID:byteQualifier:]
- -[FSEntityIdentifier initWithUUID:longByteQualifier:]
- -[FSEntityIdentifier(Private) initWithBytes:length:]
- -[FSFileDataBuffer bytes]
- -[FSFileDataBuffer classForCoder]
- -[FSFileDataBuffer dealloc]
- -[FSFileDataBuffer dealloc].cold.1
- -[FSFileDataBuffer encodeWithCoder:]
- -[FSFileDataBuffer ensureMappedMB:]
- -[FSFileDataBuffer ensureMappedMB:].cold.1
- -[FSFileDataBuffer ensureMapped]
- -[FSFileDataBuffer initWithCapacity:andLength:]
- -[FSFileDataBuffer initWithCapacity:andLength:].cold.1
- -[FSFileDataBuffer initWithCapacity:andLength:].cold.2
- -[FSFileDataBuffer initWithCapacity:andLength:].cold.3
- -[FSFileDataBuffer initWithCoder:]
- -[FSFileDataBuffer initWithCoder:].cold.1
- -[FSFileDataBuffer initWithCoder:].cold.2
- -[FSFileDataBuffer initWithLength:]
- -[FSFileDataBuffer internalCapacity]
- -[FSFileDataBuffer length]
- -[FSFileDataBuffer setLength:]
- -[FSFileDataBuffer withBytes:]
- -[FSFileSystem containerState]
- -[FSFileSystem errorState]
- -[FSFileSystem setContainerState:]
- -[FSFileSystem setErrorState:]
- -[FSGenericURLResource initAsSecureURL:readonly:]
- -[FSGenericURLResource initWithURL:]
- -[FSIOKitNotificationHandler .cxx_destruct]
- -[FSIOKitNotificationHandler resource]
- -[FSIOKitNotificationHandler setResource:]
- -[FSMetadataBlockRange blockLength]
- -[FSMetadataBlockRange initWithOffset:blockLength:numberOfBlocks:]
- -[FSMetadataBlockRange numberOfBlocks]
- -[FSMetadataBlockRange startBlockOffset]
- -[FSModuleConnector formatWithOptions:connection:taskID:replyHandler:].cold.1
- -[FSModuleExtension supportsBlockOps]
- -[FSModuleVolume fetchAndSetTypeForItem:]
- -[FSModuleVolume getAndRemoveItemForFH:]
- -[FSModuleVolume getItemForFH:]
- -[FSModuleVolume getMaxFileSizeInBits]
- -[FSModuleVolume getMaxFileSizeInBits].cold.1
- -[FSModuleVolume getMaxXattrSizeInBits]
- -[FSModuleVolume getMaxXattrSizeInBits].cold.1
- -[FSModuleVolume initWithVolume:resource:]
- -[FSModuleVolume insertIntoFHCache:]
- -[FSModuleVolume listener:shouldAcceptNewConnection:]
- -[FSModuleVolume listener:shouldAcceptNewConnection:].cold.1
- -[FSModuleVolume newConnectionID:]
- -[FSModuleVolume removeConnectionByID:]
- -[FSModuleVolume removeFromFHCache:]
- -[FSModuleVolume setFileHandleQueue:]
- -[FSModuleVolume stopUsingVolume]
- -[FSModuleVolume updateRootItem:]
- -[FSMutableFileDataBuffer capacity]
- -[FSStatFSResult initWithFSTypeName:]
- -[FSTaskOptionsBundle initWithOptionString:count:optionString:errorHandler:]
- -[FSUnaryFileSystem containerState]
- -[FSUnaryFileSystem errorState]
- -[FSUnaryFileSystem setContainerState:]
- -[FSUnaryFileSystem setErrorState:]
- -[FSUnaryItem .cxx_destruct]
- -[FSUnaryItem dealloc]
- -[FSUnaryItem init]
- -[FSUnaryItem queue]
- -[FSVolume globalWorkQueue]
- -[FSVolume setGlobalWorkQueue:]
- -[FSVolume(Project) queueForItem:]
- -[FSVolumeConnector blockmapFile:range:startIO:flags:operationID:replyHandler:]
- -[FSVolumeConnector blockmapFile:range:startIO:flags:operationID:replyHandler:].cold.1
- -[FSVolumeConnector blockmapFile:range:startIO:flags:operationID:replyHandler:].cold.2
- -[FSVolumeConnector getStandardItemAttributes:]
- -[FSVolumeConnector getStandardItemAttributesData:]
- -[FSVolumeConnector getStandardItemAttributesDataForNewItem:]
- -[FSVolumeConnector renameItemIn:item:oldName:toDirectory:newName:toItem:usingFlags:replyHandler:]
- -[FSVolumeConnector renameItemIn:item:oldName:toDirectory:overItem:newName:replyHandler:]
- -[FSVolumeSupportedCapabilities caseSensitivity]
- -[FSVolumeSupportedCapabilities setCaseSensitivity:]
- GCC_except_table101
- GCC_except_table104
- GCC_except_table113
- GCC_except_table115
- GCC_except_table118
- GCC_except_table126
- GCC_except_table131
- GCC_except_table136
- GCC_except_table138
- GCC_except_table143
- GCC_except_table15
- GCC_except_table150
- GCC_except_table21
- GCC_except_table24
- GCC_except_table5
- GCC_except_table59
- GCC_except_table6
- GCC_except_table60
- GCC_except_table67
- GCC_except_table71
- GCC_except_table78
- GCC_except_table82
- GCC_except_table86
- GCC_except_table87
- GCC_except_table9
- GCC_except_table91
- GCC_except_table97
- OBJC_IVAR_$_FSFileDataBuffer._internalCapacity
- OBJC_IVAR_$_FSFileDataBuffer._length
- OBJC_IVAR_$_FSFileDataBuffer._mp
- OBJC_IVAR_$_FSFileDataBuffer._vma
- OBJC_IVAR_$_FSFileSystem.containerState
- OBJC_IVAR_$_FSFileSystem.errorState
- OBJC_IVAR_$_FSIOKitNotificationHandler._resource
- OBJC_IVAR_$_FSItemGetAttributesRequest.attrsWanted
- OBJC_IVAR_$_FSItemSetAttributesRequest.attrsConsumed
- OBJC_IVAR_$_FSMetadataBlockRange._blockLength
- OBJC_IVAR_$_FSMetadataBlockRange._numberOfBlocks
- OBJC_IVAR_$_FSMetadataBlockRange._startBlockOffset
- OBJC_IVAR_$_FSModuleExtension._supportsBlockOps
- OBJC_IVAR_$_FSResource._isRevoked
- OBJC_IVAR_$_FSUnaryFileSystem.containerState
- OBJC_IVAR_$_FSUnaryFileSystem.errorState
- OBJC_IVAR_$_FSUnaryItem._queue
- OBJC_IVAR_$_FSVolume._globalWorkQueue
- OBJC_IVAR_$_FSVolumeSupportedCapabilities._caseSensitivity
- _FSVolumeErrorDomain
- _OBJC_CLASS_$_FSFileDataBuffer
- _OBJC_CLASS_$_FSIOKitNotificationHandler
- _OBJC_CLASS_$_FSMetadataBlockRange
- _OBJC_CLASS_$_FSUnaryItem
- _OBJC_METACLASS_$_FSFileDataBuffer
- _OBJC_METACLASS_$_FSIOKitNotificationHandler
- _OBJC_METACLASS_$_FSMetadataBlockRange
- _OBJC_METACLASS_$_FSUnaryItem
- _OUTLINED_FUNCTION_18
- __114-[FSVolumeConnector readDirectory:withAttr:requestedAttributes:intoBuffer:cookie:verifier:requestID:replyHandler:]_block_invoke_2.cold.1
- __114-[FSVolumeConnector readDirectory:withAttr:requestedAttributes:intoBuffer:cookie:verifier:requestID:replyHandler:]_block_invoke_2.cold.2
- __16-[FSClient init]_block_invoke.57
- __25-[FSClient setupHandlers]_block_invoke.14
- __25-[FSClient setupHandlers]_block_invoke_2.15
- __29-[FSVolumeConnector unmount:]_block_invoke_2.cold.1
- __39-[FSModuleConnector sendCloseResource:]_block_invoke.237
- __39-[FSModuleConnector sendCloseResource:]_block_invoke.237.cold.1
- __40-[FSModuleConnector sendRevokeResource:]_block_invoke.232
- __40-[FSModuleConnector sendRevokeResource:]_block_invoke.232.cold.1
- __40-[FSVolumeConnector mount:replyHandler:]_block_invoke_2.cold.1
- __40-[FSVolumeConnector mount:replyHandler:]_block_invoke_2.cold.2
- __41-[FSClient(Private) installedExtensions:]_block_invoke.88
- __41-[FSModuleVolume fetchAndSetTypeForItem:]_block_invoke.cold.1
- __47-[FSVolumeConnector getStandardItemAttributes:]_block_invoke.cold.1
- __51-[FSModuleConnector sendWipeResource:replyHandler:]_block_invoke.240
- __51-[FSModuleConnector sendWipeResource:replyHandler:]_block_invoke.240.cold.1
- __51-[FSModuleConnector sendWipeResource:replyHandler:]_block_invoke.240.cold.2
- __52-[FSVolumeConnector reclaim:requestID:replyHandler:]_block_invoke_2.cold.1
- __55-[FSModuleConnector loadResource:options:replyHandler:]_block_invoke.276
- __55-[FSModuleConnector loadResource:options:replyHandler:]_block_invoke.276.cold.1
- __55-[FSModuleConnector loadResource:options:replyHandler:]_block_invoke.285
- __55-[FSModuleConnector loadResource:options:replyHandler:]_block_invoke_2.277
- __55-[FSModuleConnector loadResource:options:replyHandler:]_block_invoke_2.277.cold.1
- __57-[FSModuleConnector unloadResource:options:replyHandler:]_block_invoke.cold.2
- __57-[FSVolumeConnector listXattrsOf:requestID:replyHandler:]_block_invoke.422
- __57-[FSVolumeConnector listXattrsOf:requestID:replyHandler:]_block_invoke_2.cold.1
- __57-[FSVolumeConnector listXattrsOf:requestID:replyHandler:]_block_invoke_2.cold.2
- __58-[FSVolumeConnector open:withMode:requestID:replyHandler:]_block_invoke_2.cold.1
- __58-[FSVolumeConnector open:withMode:requestID:replyHandler:]_block_invoke_2.cold.2
- __58-[FSVolumeConnector xattrOf:named:requestID:replyHandler:]_block_invoke_2.cold.1
- __58-[FSVolumeConnector xattrOf:named:requestID:replyHandler:]_block_invoke_2.cold.2
- __62-[FSVolumeConnector close:keepingMode:requestID:replyHandler:]_block_invoke_2.cold.1
- __62-[FSVolumeConnector close:keepingMode:requestID:replyHandler:]_block_invoke_2.cold.2
- __63-[FSVolumeConnector readSymbolicLinkOf:requestID:replyHandler:]_block_invoke_2.cold.2
- __64-[FSVolumeConnector lookupIn:name:flags:requestID:replyHandler:]_block_invoke.380
- __67-[FSVolumeConnector setFileAttributesOf:to:requestID:replyHandler:]_block_invoke_2.cold.1
- __69-[FSModuleConnector checkWithOptions:connection:taskID:replyHandler:]_block_invoke.258
- __69-[FSModuleConnector checkWithOptions:connection:taskID:replyHandler:]_block_invoke.261
- __69-[FSModuleConnector checkWithOptions:connection:taskID:replyHandler:]_block_invoke_2.259
- __69-[FSModuleConnector checkWithOptions:connection:taskID:replyHandler:]_block_invoke_2.262
- __70-[FSModuleConnector formatWithOptions:connection:taskID:replyHandler:]_block_invoke.270
- __70-[FSModuleConnector formatWithOptions:connection:taskID:replyHandler:]_block_invoke.272
- __70-[FSModuleConnector formatWithOptions:connection:taskID:replyHandler:]_block_invoke_2.271
- __70-[FSModuleConnector formatWithOptions:connection:taskID:replyHandler:]_block_invoke_2.273
- __71-[FSVolumeConnector endIO:range:status:flags:operationID:replyHandler:]_block_invoke_2.cold.1
- __71-[FSVolumeConnector setXattrOf:named:value:how:requestID:replyHandler:]_block_invoke_2.cold.1
- __72-[FSVolumeConnector writeTo:atOffset:fromBuffer:requestID:replyHandler:]_block_invoke_2.cold.1
- __72-[FSVolumeConnector writeTo:atOffset:fromBuffer:requestID:replyHandler:]_block_invoke_2.cold.2
- __73-[FSModuleHost(Project) _updateProviderListForFilteredFSModileInstances:]_block_invoke.183
- __73-[FSModuleHost(Project) _updateProviderListForFilteredFSModileInstances:]_block_invoke_2.185
- __73-[FSVolumeConnector makeLinkOf:named:inDirectory:requestID:replyHandler:]_block_invoke.415
- __73-[FSVolumeConnector makeLinkOf:named:inDirectory:requestID:replyHandler:]_block_invoke_2.cold.1
- __73-[FSVolumeConnector readFrom:atOffset:intoBuffer:requestID:replyHandler:]_block_invoke_2.cold.1
- __73-[FSVolumeConnector readFrom:atOffset:intoBuffer:requestID:replyHandler:]_block_invoke_2.cold.2
- __74-[FSModuleConnector checkResource:options:connection:taskID:replyHandler:]_block_invoke.246
- __74-[FSModuleConnector checkResource:options:connection:taskID:replyHandler:]_block_invoke.249.cold.1
- __74-[FSModuleConnector checkResource:options:connection:taskID:replyHandler:]_block_invoke.250
- __74-[FSModuleConnector checkResource:options:connection:taskID:replyHandler:]_block_invoke.251
- __74-[FSVolumeConnector checkAccessTo:requestedAccess:requestID:replyHandler:]_block_invoke_2.cold.1
- __75-[FSModuleConnector formatResource:options:connection:taskID:replyHandler:]_block_invoke.265
- __75-[FSModuleConnector formatResource:options:connection:taskID:replyHandler:]_block_invoke.265.cold.1
- __75-[FSModuleConnector formatResource:options:connection:taskID:replyHandler:]_block_invoke_2.266
- __75-[FSVolumeConnector createIn:named:type:attributes:requestID:replyHandler:]_block_invoke.371
- __75-[FSVolumeConnector createIn:named:type:attributes:requestID:replyHandler:]_block_invoke.371.cold.1
- __75-[FSVolumeConnector createIn:named:type:attributes:requestID:replyHandler:]_block_invoke_2.cold.1
- __75-[FSVolumeConnector createIn:named:type:attributes:requestID:replyHandler:]_block_invoke_2.cold.2
- __76-[FSVolumeConnector setOtherAttributeOf:named:value:requestID:replyHandler:]_block_invoke.362
- __76-[FSVolumeConnector setOtherAttributeOf:named:value:requestID:replyHandler:]_block_invoke_2.364
- __77-[FSVolumeConnector removeItem:from:named:usingFlags:requestID:replyHandler:]_block_invoke.386
- __77-[FSVolumeConnector removeItem:from:named:usingFlags:requestID:replyHandler:]_block_invoke_2.cold.1
- __79-[FSVolumeConnector blockmapFile:range:startIO:flags:operationID:replyHandler:]_block_invoke_2.cold.1
- __82-[FSVolumeConnector removeDirectory:from:named:usingFlags:requestID:replyHandler:]_block_invoke.383
- __82-[FSVolumeConnector removeDirectory:from:named:usingFlags:requestID:replyHandler:]_block_invoke_2.cold.1
- __83+[FSBlockDeviceResource(Project) openWithBSDName:writable:auditToken:replyHandler:]_block_invoke.196
- __83+[FSBlockDeviceResource(Project) openWithBSDName:writable:auditToken:replyHandler:]_block_invoke.196.cold.1
- __84-[FSVolumeConnector makeSymlinkIn:named:contents:attributes:requestID:replyHandler:]_block_invoke_2.cold.1
- __87+[FSKitDiskArbHelper DAMountFSKitVolume:deviceName:mountPoint:volumeName:mountOptions:]_block_invoke.34
- __87+[FSKitDiskArbHelper DAMountFSKitVolume:deviceName:mountPoint:volumeName:mountOptions:]_block_invoke.34.cold.1
- __87+[FSKitDiskArbHelper DAMountFSKitVolume:deviceName:mountPoint:volumeName:mountOptions:]_block_invoke.34.cold.2
- __87+[FSKitDiskArbHelper DAMountFSKitVolume:deviceName:mountPoint:volumeName:mountOptions:]_block_invoke.34.cold.3
- __87+[FSKitDiskArbHelper DAMountFSKitVolume:deviceName:mountPoint:volumeName:mountOptions:]_block_invoke.35
- __87+[FSKitDiskArbHelper DAMountFSKitVolume:deviceName:mountPoint:volumeName:mountOptions:]_block_invoke.35.cold.1
- __87+[FSKitDiskArbHelper DAMountFSKitVolume:deviceName:mountPoint:volumeName:mountOptions:]_block_invoke.35.cold.2
- __87+[FSKitDiskArbHelper DAMountFSKitVolume:deviceName:mountPoint:volumeName:mountOptions:]_block_invoke.38
- __87+[FSKitDiskArbHelper DAMountFSKitVolume:deviceName:mountPoint:volumeName:mountOptions:]_block_invoke.38.cold.1
- __96-[FSVolumeConnector makeCloneOf:named:inDirectory:attributes:usingFlags:requestID:replyHandler:]_block_invoke.437
- __96-[FSVolumeConnector makeCloneOf:named:inDirectory:attributes:usingFlags:requestID:replyHandler:]_block_invoke_2.cold.1
- __OBJC_$_CLASS_METHODS_FSClient
- __OBJC_$_CLASS_METHODS_FSEntityIdentifier(Private|FSEntityIdentifier_project)
- __OBJC_$_CLASS_METHODS_FSFileDataBuffer
- __OBJC_$_CLASS_METHODS_FSMetadataBlockRange
- __OBJC_$_CLASS_METHODS_FSModuleVolume
- __OBJC_$_CLASS_METHODS_FSProbeResult
- __OBJC_$_CLASS_METHODS_FSVolume(Project|FSKit_private)
- __OBJC_$_CLASS_PROP_LIST_FSFileDataBuffer
- __OBJC_$_CLASS_PROP_LIST_FSProbeResult
- __OBJC_$_INSTANCE_METHODS_FSEntityIdentifier(Private|FSEntityIdentifier_project)
- __OBJC_$_INSTANCE_METHODS_FSFileDataBuffer
- __OBJC_$_INSTANCE_METHODS_FSGenericURLResource
- __OBJC_$_INSTANCE_METHODS_FSIOKitNotificationHandler
- __OBJC_$_INSTANCE_METHODS_FSMetadataBlockRange
- __OBJC_$_INSTANCE_METHODS_FSModuleVolume
- __OBJC_$_INSTANCE_METHODS_FSUnaryItem
- __OBJC_$_INSTANCE_METHODS_FSVolume(Project|FSKit_private)
- __OBJC_$_INSTANCE_VARIABLES_FSFileDataBuffer
- __OBJC_$_INSTANCE_VARIABLES_FSIOKitNotificationHandler
- __OBJC_$_INSTANCE_VARIABLES_FSMetadataBlockRange
- __OBJC_$_INSTANCE_VARIABLES_FSUnaryItem
- __OBJC_$_PROP_LIST_FSFileDataBuffer
- __OBJC_$_PROP_LIST_FSIOKitNotificationHandler
- __OBJC_$_PROP_LIST_FSMetadataBlockRange
- __OBJC_$_PROP_LIST_FSModuleVolume
- __OBJC_$_PROP_LIST_FSUnaryItem
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_FSBlockDeviceOperations
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_FSManageableResourceMaintenanceOperations
- __OBJC_$_PROTOCOL_METHOD_TYPES_FSBlockDeviceOperations
- __OBJC_$_PROTOCOL_REFS_FSBlockDeviceOperations
- __OBJC_CLASS_PROTOCOLS_$_FSFileDataBuffer
- __OBJC_CLASS_PROTOCOLS_$_FSModuleVolume
- __OBJC_CLASS_RO_$_FSFileDataBuffer
- __OBJC_CLASS_RO_$_FSIOKitNotificationHandler
- __OBJC_CLASS_RO_$_FSMetadataBlockRange
- __OBJC_CLASS_RO_$_FSUnaryItem
- __OBJC_LABEL_PROTOCOL_$_FSBlockDeviceOperations
- __OBJC_METACLASS_RO_$_FSFileDataBuffer
- __OBJC_METACLASS_RO_$_FSIOKitNotificationHandler
- __OBJC_METACLASS_RO_$_FSMetadataBlockRange
- __OBJC_METACLASS_RO_$_FSUnaryItem
- __OBJC_PROTOCOL_$_FSBlockDeviceOperations
- __OBJC_PROTOCOL_REFERENCE_$_FSBlockDeviceOperations
- ___114-[FSVolumeConnector readDirectory:withAttr:requestedAttributes:intoBuffer:cookie:verifier:requestID:replyHandler:]_block_invoke_2
- ___16-[FSClient init]_block_invoke
- ___29-[FSVolumeConnector unmount:]_block_invoke_2
- ___31-[FSModuleVolume getItemForFH:]_block_invoke
- ___36-[FSModuleVolume insertIntoFHCache:]_block_invoke
- ___36-[FSModuleVolume removeFromFHCache:]_block_invoke
- ___40-[FSModuleVolume getAndRemoveItemForFH:]_block_invoke
- ___40-[FSVolumeConnector mount:replyHandler:]_block_invoke_2
- ___41-[FSModuleVolume fetchAndSetTypeForItem:]_block_invoke
- ___46-[FSVolumeConnector synchronize:replyHandler:]_block_invoke_2
- ___47-[FSVolumeConnector getStandardItemAttributes:]_block_invoke
- ___52-[FSVolumeConnector reclaim:requestID:replyHandler:]_block_invoke_2
- ___53-[FSModuleVolume listener:shouldAcceptNewConnection:]_block_invoke
- ___55-[FSModuleConnector loadResource:options:replyHandler:]_block_invoke_3
- ___57-[FSModuleConnector unloadResource:options:replyHandler:]_block_invoke_2
- ___57-[FSVolumeConnector listXattrsOf:requestID:replyHandler:]_block_invoke_2
- ___58-[FSVolumeConnector open:withMode:requestID:replyHandler:]_block_invoke_2
- ___58-[FSVolumeConnector xattrOf:named:requestID:replyHandler:]_block_invoke_2
- ___62+[FSVolume(Project) extentPackerForBuffer:bufLen:extentCount:]_block_invoke
- ___62-[FSVolumeConnector close:keepingMode:requestID:replyHandler:]_block_invoke_2
- ___67+[FSVolume(Project) newDirEntryPacker:bufLen:bytesPacked:withAttr:]_block_invoke
- ___67-[FSVolumeConnector setFileAttributesOf:to:requestID:replyHandler:]_block_invoke_2
- ___71-[FSVolumeConnector endIO:range:status:flags:operationID:replyHandler:]_block_invoke_2
- ___71-[FSVolumeConnector setXattrOf:named:value:how:requestID:replyHandler:]_block_invoke_2
- ___72-[FSVolumeConnector writeTo:atOffset:fromBuffer:requestID:replyHandler:]_block_invoke_2
- ___73-[FSVolumeConnector readFrom:atOffset:intoBuffer:requestID:replyHandler:]_block_invoke_2
- ___74-[FSVolumeConnector checkAccessTo:requestedAccess:requestID:replyHandler:]_block_invoke_2
- ___76-[FSVolumeConnector setOtherAttributeOf:named:value:requestID:replyHandler:]_block_invoke_3
- ___79-[FSVolumeConnector blockmapFile:range:startIO:flags:operationID:replyHandler:]_block_invoke
- ___79-[FSVolumeConnector blockmapFile:range:startIO:flags:operationID:replyHandler:]_block_invoke_2
- ___79-[FSVolumeConnector fileAttributes:requestedAttributes:requestID:replyHandler:]_block_invoke_2
- ___89-[FSVolumeConnector renameItemIn:item:oldName:toDirectory:overItem:newName:replyHandler:]_block_invoke
- ___89-[FSVolumeConnector renameItemIn:item:oldName:toDirectory:overItem:newName:replyHandler:]_block_invoke_2
- ___98-[FSVolumeConnector renameItemIn:item:oldName:toDirectory:newName:toItem:usingFlags:replyHandler:]_block_invoke
- ___block_descriptor_100_e8_32s40s48s56s64s72s80s88bs_e5_v8?0l
- ___block_descriptor_104_e8_32s40s48s56s64s72s80s88s96bs_e5_v8?0l
- ___block_descriptor_108_e8_32s40s48s56s64s72s80s88s96bs_e5_v8?0l
- ___block_descriptor_124_e8_32s40s48s56s64s72s80s88s96s104r112r_e36_v32?0"FSVolumeDescription"8Q16^B24l
- ___block_descriptor_40_e8_32bs_e20_v24?0Q8"NSError"16l
- ___block_descriptor_41_e8_32s_e5_v8?0l
- ___block_descriptor_48_e8_32bs40r_e20_v24?0Q8"NSError"16l
- ___block_descriptor_48_e8_32r40r_e20_v20?0B8"NSError"12l
- ___block_descriptor_48_e8_32s40bs_e28_v24?0"FSItem"8"NSError"16l
- ___block_descriptor_48_e8_32s40s_e38_v24?0"FSItemAttributes"8"NSError"16l
- ___block_descriptor_52_e8_32s40bs_e5_v8?0l
- ___block_descriptor_56_e8_32s40r48w_e38_v24?0"FSItemAttributes"8"NSError"16l
- ___block_descriptor_56_e8_32s40s48bs_e28_v24?0"FSItem"8"NSError"16l
- ___block_descriptor_56_e8_32s40s48bs_e35_v24?0"FSProbeResult"8"NSError"16l
- ___block_descriptor_60_e8_32s40s48bs_e5_v8?0l
- ___block_descriptor_64_e8_32r40r48r_e43_B40?0"FSBlockDeviceResource"8i16Q20Q28I36l
- ___block_descriptor_64_e8_32s40s48bs56r_e17_v16?0"NSError"8l
- ___block_descriptor_64_e8_32s40s48bs_e20_v24?0Q8"NSError"16l
- ___block_descriptor_64_e8_32s40s48bs_e5_v8?0l
- ___block_descriptor_64_e8_32s40s48s56r_e25_v32?0"FSVolume"8Q16^B24l
- ___block_descriptor_72_e8_32r40r48r56r64r_e53_B52?0"FSFileName"8q16Q24Q32"FSItemAttributes"40B48l
- ___block_descriptor_72_e8_32s40s48bs56w_e5_v8?0l
- ___block_descriptor_72_e8_32s40s48r56r64r_e43_v32?0"FSItem"8"FSFileName"16"NSError"24l
- ___block_descriptor_72_e8_32s40s48s56bs_e5_v8?0l
- ___block_descriptor_76_e8_32s40s48s56s64bs_e5_v8?0l
- ___block_descriptor_80_e8_32s40s48s56bs64r72r_e17_v16?0"NSError"8l
- ___block_descriptor_80_e8_32s40s48s56bs64r72r_e29_v24?0"NSArray"8"NSError"16l
- ___block_descriptor_80_e8_32s40s48s56bs64r72r_e30_v24?0"FSVolume"8"NSError"16l
- ___block_descriptor_80_e8_32s40s48s56s64bs72w_e5_v8?0l
- ___block_descriptor_80_e8_32s40s48s56s64bs_e5_v8?0l
- ___block_descriptor_88_e8_32s40s48bs_e5_v8?0l
- ___block_descriptor_88_e8_32s40s48s56bs64r72r80r_e5_v8?0l
- ___block_descriptor_88_e8_32s40s48s56s64s72bs_e5_v8?0l
- ___block_descriptor_89_e8_32s40s48s56s64bs_e5_v8?0l
- ___block_descriptor_92_e8_32s40s48s56s64bs72r80r_e43_v32?0"FSItem"8"FSFileName"16"NSError"24l
- ___block_descriptor_96_e8_32s40s48s56bs_e5_v8?0l
- ___copy_helper_block_e8_32r40r48r
- ___copy_helper_block_e8_32r40r48r56r64r
- ___copy_helper_block_e8_32s40r48w
- ___copy_helper_block_e8_32s40s48b56w
- ___copy_helper_block_e8_32s40s48r56r64r
- ___copy_helper_block_e8_32s40s48s56b64r72r80r
- ___copy_helper_block_e8_32s40s48s56r
- ___copy_helper_block_e8_32s40s48s56s64b72w
- ___copy_helper_block_e8_32s40s48s56s64s72s80s88s96b
- ___copy_helper_block_e8_32s40s48s56s64s72s80s88s96s104r112r
- ___destroy_helper_block_e8_32r40r48r
- ___destroy_helper_block_e8_32r40r48r56r64r
- ___destroy_helper_block_e8_32s40r48w
- ___destroy_helper_block_e8_32s40s48r56r64r
- ___destroy_helper_block_e8_32s40s48s56s64r72r80r
- ___destroy_helper_block_e8_32s40s48s56s64s72s80s88s96s
- ___destroy_helper_block_e8_32s40s48s56s64s72s80s88s96s104r112r
- ___destroy_helper_block_e8_32s40s48s56s64s72w
- ___destroy_helper_block_e8_32s40s48s56w
- __block_literal_global.153
- __block_literal_global.177
- __block_literal_global.179
- __block_literal_global.234
- __block_literal_global.239
- __block_literal_global.254
- __block_literal_global.264
- __block_literal_global.268
- __block_literal_global.275
- __block_literal_global.314
- _objc_msgSend$areXattrOperationsInhibited
- _objc_msgSend$blockLength
- _objc_msgSend$blockmapFile:range:startIO:flags:operationID:usingPacker:replyHandler:
- _objc_msgSend$caseSensitivity
- _objc_msgSend$dataWithLength:
- _objc_msgSend$endIO:range:status:flags:operationID:replyHandler:
- _objc_msgSend$extentPackerForBuffer:bufLen:extentCount:
- _objc_msgSend$fetchAndSetTypeForItem:
- _objc_msgSend$getStandardItemAttributes:
- _objc_msgSend$getStandardItemAttributesData:
- _objc_msgSend$getStandardItemAttributesDataForNewItem:
- _objc_msgSend$globalWorkQueue
- _objc_msgSend$initWithOffset:blockLength:numberOfBlocks:
- _objc_msgSend$initWithOptionString:count:optionString:errorHandler:
- _objc_msgSend$initWithUUID:byteQualifier:
- _objc_msgSend$initWithUUID:longByteQualifier:
- _objc_msgSend$isChownRestricted
- _objc_msgSend$isTerminated
- _objc_msgSend$lookupItemNamed:inDirectory:usingPacker:replyHandler:
- _objc_msgSend$newDirEntryPacker:bufLen:bytesPacked:withAttr:
- _objc_msgSend$numberOfBlocks
- _objc_msgSend$parameters
- _objc_msgSend$preallocateSpaceForItem:offset:length:flags:usingPacker:replyHandler:
- _objc_msgSend$queue
- _objc_msgSend$queueForItem:
- _objc_msgSend$renameItemIn:item:oldName:toDirectory:newName:toItem:usingFlags:replyHandler:
- _objc_msgSend$renameItemIn:item:oldName:toDirectory:overItem:newName:replyHandler:
- _objc_msgSend$startBlockOffset
- _objc_msgSend$startCheckWithTask:parameters:error:
- _objc_msgSend$startFormatWithTask:parameters:error:
- _objc_msgSend$supportsBlockOps
- _objc_msgSend$updateRootItem:
- block_copy_helper.1
- block_descriptor.3
- block_destroy_helper.2
CStrings:
+ "%s: Activating volumeName (%@) volumeID (%@) with activateOptions (%@)"
+ "%s: Can't read the whole footer of the resource, could only read (%zu) instead of (%ld)"
+ "%s: Can't read the whole header of the resource, could only read (%zu) instead of (%ld)"
+ "%s: Couldn't create a new XPC connection to com.apple.filesystems.fskitd"
+ "%s: Packer is out of space, bytes packed (%ld)"
+ "%s: Packer out of space"
+ "%s: Volume '%@' did not return a valid object for volumeStatistics."
+ "%s: activate volume (%@) reply(%@)"
+ "%s: delegate has checkResource:options:connection:taskID:replyHandler: method, try that"
+ "%s: forced-load error %@, container status %@"
+ "%s: linkName is nil"
+ "%s: load reply(nil,nil), container status %@"
+ "%s: newItem:%@"
+ "%s: non forced-load error %@, container status %@"
+ "%s: unexpected container error %@"
+ "%s: unexpected container state %@,%@"
+ "%s:error: Invalid entry name"
+ "%s:error: Invalid entry name (%@)"
+ "%s:error: No attributes found, while we were requeste to pack with attributes"
+ "%s:installedExtensionWithBundleID:%@"
+ "%s:nil attributes"
+ "%s:nil contents"
+ "%s:nil innerNewName"
+ "%s:nil newName"
+ "%s:nil value"
+ "%s:start:theFile:%@:originalRangeLocation:%lu:originalRangeLength:%lu:ioStatus:%d:flags:%lu:operationID:%llu"
+ "%s:start:theFile:%@:theRangeLocation:%lu:theRangeLength:%lu:flags:%lu:operationID:%llu"
+ "%s:theADItem:%@"
+ "%s:theItem:%@"
+ "-[FSBlockDeviceResource asynchronousMetadataFlushWithError:]"
+ "-[FSBlockDeviceResource metadataClear:withDelayedWrites:error:]"
+ "-[FSBlockDeviceResource metadataFlushWithError:]"
+ "-[FSBlockDeviceResource metadataPurge:error:]"
+ "-[FSBlockDeviceResource(Private) metadataReadInto:startingAt:length:readAheadExtents:readAheadCount:error:]"
+ "-[FSClient setupConnection]"
+ "-[FSClient(Private) validateVolumeName:usingBundle:volumeID:replyHandler:]_block_invoke"
+ "-[FSDirectoryEntryPacker packEntryWithName:itemType:itemID:nextCookie:attributes:]"
+ "-[FSExtentPacker packExtentWithResource:type:logicalOffset:physicalOffset:length:]"
+ "-[FSModuleVolume(Project) fetchAndSetTypeForItem:replyHandler:]_block_invoke"
+ "-[FSModuleVolume(Project) getMaxFileSizeInBits]"
+ "-[FSModuleVolume(Project) getMaxXattrSizeInBits]"
+ "-[FSModuleVolume(Project) listener:shouldAcceptNewConnection:]"
+ "-[FSMutableFileDataBuffer ensureMappedMB:]"
+ "-[FSMutableFileDataBuffer initWithCapacity:andLength:]"
+ "-[FSMutableFileDataBuffer initWithCoder:]"
+ "-[FSVolumeConnector blockmapFile:range:flags:operationID:replyHandler:]"
+ "-[FSVolumeConnector blockmapFile:range:flags:operationID:replyHandler:]_block_invoke"
+ "-[FSVolumeConnector checkAccessTo:requestedAccess:requestID:replyHandler:]_block_invoke"
+ "-[FSVolumeConnector createIn:named:type:attributes:requestID:replyHandler:]_block_invoke_3"
+ "-[FSVolumeConnector endIO:range:status:flags:operationID:replyHandler:]_block_invoke"
+ "-[FSVolumeConnector fileAttributes:requestedAttributes:requestID:replyHandler:]_block_invoke"
+ "-[FSVolumeConnector getStandardItemAttributesForItem:replyHandler:]_block_invoke"
+ "-[FSVolumeConnector listXattrsOf:requestID:replyHandler:]_block_invoke"
+ "-[FSVolumeConnector lookupIn:name:flags:requestID:replyHandler:]_block_invoke"
+ "-[FSVolumeConnector lookupIn:name:flags:requestID:replyHandler:]_block_invoke_3"
+ "-[FSVolumeConnector makeSymlinkIn:named:contents:attributes:requestID:replyHandler:]_block_invoke_4"
+ "-[FSVolumeConnector reclaim:requestID:replyHandler:]_block_invoke"
+ "-[FSVolumeConnector renameItemIn:named:item:toDirectory:newName:toItem:usingFlags:requestID:replyHandler:]_block_invoke"
+ "-[FSVolumeConnector setFileAttributesOf:to:requestID:replyHandler:]_block_invoke"
+ "-[FSVolumeConnector setOtherAttributeOf:named:value:requestID:replyHandler:]_block_invoke"
+ "-[FSVolumeConnector setXattrOf:named:value:how:requestID:replyHandler:]_block_invoke"
+ "-[FSVolumeConnector unmount:]_block_invoke"
+ "@\"FSContainerStatus\""
+ "@\"FSContainerStatus\"16@0:8"
+ "@\"FSMutableFileDataBuffer\""
+ "@\"NSProgress\"40@0:8@\"FSTask\"16@\"FSTaskOptions\"24^@32"
+ "@32@0:8@16Q24"
+ "@32@0:8q16@24"
+ "@40@0:8q16Q24Q32"
+ "B24@0:8^@16"
+ "B32@0:8@16^@24"
+ "B36@0:8@16B24^@28"
+ "B48@0:8^v16q24Q32^@40"
+ "B56@0:8@16q24Q32Q40@48"
+ "B56@0:8@16q24q32q40Q48"
+ "B64@0:8^v16q24Q32r^{?=qQ}40q48^@56"
+ "Directory"
+ "FSClient connection to fskitd was invalidated"
+ "FSClient setting up connection to fskitd"
+ "FSContainerStatus"
+ "FSDirectoryEntryPacker"
+ "FSExtentPacker"
+ "FSKitStatFSResult:totalBytes(%llu):availableBytes(%llu):freeBytes(%llu):totalFiles(%llu):freeFiles(%llu)"
+ "FSMetadataRange"
+ "FSModule %{public}@ activateVolume: returned nil result"
+ "FSModule %{public}@ probe: returned %@"
+ "FSModule %{public}@ probe: returned nil result"
+ "FSResource.Limited"
+ "FSStatFSResult with block size set to zero, which is invalid. Setting to 4096"
+ "FSSupportsGenericURLResources"
+ "FSSupportsKernelOffloadedIO"
+ "FSSupportsPathURLs"
+ "FSTB.e"
+ "FSTB.o"
+ "FSTB.p"
+ "FSTO.o"
+ "FSTO.x"
+ "FSTaskOptions"
+ "FSVolumeItemDeactivation"
+ "Got delegate '%@' conformance N %d S %d Maintenance %d URL %d isConformantFS %d"
+ "InvalidDirectoryCookie"
+ "Path"
+ "T@\"FSClient\",R"
+ "T@\"FSContainerIdentifier\",R"
+ "T@\"FSContainerStatus\",C"
+ "T@\"FSContainerStatus\",C,V_containerStatus"
+ "T@\"FSContainerStatus\",R"
+ "T@\"FSItem\",&"
+ "T@\"FSMutableFileDataBuffer\",&,V_buffer"
+ "T@\"FSProbeResult\",R"
+ "T@\"FSResource\",&"
+ "T@\"FSTaskOptions\",R,C"
+ "T@\"FSVolume<FSVolumeOperations>\",&"
+ "T@\"NSArray\",&,V_moduleOrder"
+ "T@\"NSError\",R,C,V_status"
+ "T@\"NSMutableArray\",C,V_taskOptions"
+ "T@\"NSMutableData\",&,V_buffer"
+ "T@\"NSMutableDictionary\",&"
+ "T@\"NSMutableDictionary\",&,V_extras"
+ "T@\"NSObject<OS_dispatch_queue>\",R"
+ "T@\"NSObject<OS_dispatch_queue>\",R,V_fileHandleQueue"
+ "T@\"NSXPCListener\",R"
+ "TB,?"
+ "TB,R,N,GisRevoked,V_revoked"
+ "TB,R,V_supportsItemDeactivation"
+ "TB,V_limited"
+ "TB,V_outOfSpace"
+ "TB,V_withAttributes"
+ "TI,V_bytesPacked"
+ "TQ,R,V_length"
+ "TQ,R,V_segmentCount"
+ "TQ,R,V_segmentLength"
+ "TQ,V_availableBlocks"
+ "TQ,V_availableBytes"
+ "TQ,V_freeBlocks"
+ "TQ,V_freeBytes"
+ "TQ,V_freeFiles"
+ "TQ,V_totalBlocks"
+ "TQ,V_totalBytes"
+ "TQ,V_totalFiles"
+ "TQ,V_usedBlocks"
+ "TQ,V_usedBytes"
+ "Tq,N,V_caseFormat"
+ "Tq,R"
+ "Tq,R,V_startOffset"
+ "Tq,R,V_state"
+ "Tq,V_bytesPacked"
+ "Tq,V_extentsPacked"
+ "Unable to allocate URL wrapper for '%@'"
+ "^v"
+ "_N_INACTIVE"
+ "_bytesPacked"
+ "_caseFormat"
+ "_containerStatus"
+ "_extentsPacked"
+ "_extras"
+ "_fixUpValues"
+ "_lastEntry"
+ "_limited"
+ "_outOfSpace"
+ "_revoked"
+ "_segmentCount"
+ "_segmentLength"
+ "_startOffset"
+ "_status"
+ "_supportsItemDeactivation"
+ "_taskOptions"
+ "_withAttributes"
+ "active"
+ "activeWithStatus:"
+ "asynchronousMetadataFlushWithError:"
+ "blockedWithStatus:"
+ "blockmapFile:offset:length:flags:operationID:packer:replyHandler:"
+ "blockmapFile:range:flags:operationID:replyHandler:"
+ "bytesPacked"
+ "cantReadContainerID"
+ "caseFormat"
+ "com.apple.fskitd"
+ "completeIOForFile:offset:length:status:flags:operationID:replyHandler:"
+ "containerStatus"
+ "createFileNamed:inDirectory:attributes:packer:replyHandler:"
+ "deactivateItem:replyHandler:"
+ "decodeArrayOfObjectsOfClass:forKey:"
+ "decodeDictionaryWithKeysOfClass:objectsOfClass:forKey:"
+ "delayedMetadataWriteFrom:startingAt:length:error:"
+ "enumerateOptionsUsingBlock:"
+ "extentData"
+ "extentDataByExtentsPacked"
+ "extentsPacked"
+ "extras"
+ "fetchAndSetTypeForItem:replyHandler:"
+ "getStandardItemAttributesDataForItem:replyHandler:"
+ "getStandardItemAttributesDataForNewItem:replyHandler:"
+ "getStandardItemAttributesForItem:replyHandler:"
+ "initClient"
+ "initFileURLWithPath:isDirectory:"
+ "initResource"
+ "initWithBlockmapFlags:"
+ "initWithBuffer:withAttributes:"
+ "initWithDictionary:"
+ "initWithExtentCount:"
+ "initWithFileSystemTypeName:"
+ "initWithOffset:segmentLength:segmentCount:"
+ "initWithOptionString:count:optionDictionary:errorHandler:"
+ "initWithOptions:"
+ "initWithOptions:extras:"
+ "initWithState:status:"
+ "initWithUTF8String:"
+ "initWithUUID:qualifier:"
+ "installedExtensionWithBundleID:replyHandler:"
+ "installedExtensionWithBundleID:synchronous:replyHandler:"
+ "itemDeactivationPolicy"
+ "limited"
+ "lookupItemNamed:inDirectory:packer:replyHandler:"
+ "mapStringToKind:"
+ "metadataClear:withDelayedWrites:error:"
+ "metadataFlushWithError:"
+ "metadataPurge:error:"
+ "metadataReadInto:startingAt:length:error:"
+ "metadataReadInto:startingAt:length:readAheadExtents:readAheadCount:error:"
+ "metadataWriteFrom:startingAt:length:error:"
+ "moduleOrder"
+ "new"
+ "notReadyWithStatus:"
+ "notRecognizedProbeResult"
+ "o"
+ "outOfSpace"
+ "packEntryWithName:itemType:itemID:nextCookie:attributes:"
+ "packExtentWithResource:type:logicalOffset:physicalOffset:length:"
+ "pathOptions"
+ "preallocateSpaceForFile:atOffset:length:flags:packer:replyHandler:"
+ "preallocateSpaceForItem:atOffset:length:flags:replyHandler:"
+ "rangeWithOffset:segmentLength:segmentCount:"
+ "read(into:startingAt:length:)"
+ "ready"
+ "readyWithStatus:"
+ "recognizedProbeResultWithName:containerID:"
+ "restrictsOwnershipChanges"
+ "revoked"
+ "segmentCount"
+ "segmentLength"
+ "setBuffer:"
+ "setBytesPacked:"
+ "setCaseFormat:"
+ "setContainerStatus:"
+ "setExtentsPacked:"
+ "setExtras:"
+ "setLastEntryAsEOF"
+ "setLimited:"
+ "setModuleOrder:"
+ "setOutOfSpace:"
+ "setSecureURL:forKey:"
+ "setTaskOptions:"
+ "setURL:forKey:"
+ "setWithAttributes:"
+ "setupConnection"
+ "sharedInstance"
+ "startCheckWithTask:options:error:"
+ "startFormatWithTask:options:error:"
+ "startOffset"
+ "status"
+ "supportsItemDeactivation"
+ "taskOptions"
+ "updateRootItem:replyHandler:"
+ "urlForOption:"
+ "usableButLimitedProbeResult"
+ "usableButLimitedProbeResultWithName:containerID:"
+ "usableProbeResultWithName:containerID:"
+ "v16@?0@\"FSItemAttributes\"8"
+ "v16@?0@\"NSData\"8"
+ "v16@?0^v8"
+ "v24@0:8@\"FSContainerStatus\"16"
+ "v32@0:8@\"FSItem\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@\"FSTaskOptionsBundle\"16@?<v@?@\"NSError\">24"
+ "v40@0:8@\"FSResource\"16@\"FSTaskOptions\"24@?<v@?@\"FSVolume\"@\"NSError\">32"
+ "v40@0:8@\"FSResource\"16@\"FSTaskOptions\"24@?<v@?@\"NSArray\"@\"NSError\">32"
+ "v40@0:8@\"FSResource\"16@\"FSTaskOptions\"24@?<v@?@\"NSError\">32"
+ "v48@0:8@\"FSFileName\"16@\"FSItem\"24@\"FSExtentPacker\"32@?<v@?@\"FSItem\"@\"FSFileName\"@\"NSError\">40"
+ "v56@0:8@\"FSFileName\"16@\"FSItem\"24@\"FSItemSetAttributesRequest\"32@\"FSExtentPacker\"40@?<v@?@\"FSItem\"@\"FSFileName\"@\"NSError\">48"
+ "v56@0:8@\"FSItem\"16q24Q32@\"FSMutableFileDataBuffer\"40@?<v@?Q@\"NSError\">48"
+ "v56@0:8@\"FSItem\"16q24Q32Q40@?<v@?Q@\"NSError\">48"
+ "v56@0:8@16q24Q32Q40@?48"
+ "v64@0:8@\"FSFileHandle\"16{_NSRange=QQ}24Q40Q48@?<v@?i@\"NSData\"@\"NSData\">56"
+ "v64@0:8@\"FSItem\"16q24Q32Q40@\"FSExtentPacker\"48@?<v@?Q@\"NSError\">56"
+ "v64@0:8@16q24Q32Q40@48@?56"
+ "v64@0:8@16{_NSRange=QQ}24Q40Q48@?56"
+ "v68@0:8@\"FSFileHandle\"16{_NSRange=QQ}24i40Q44Q52@?<v@?i>60"
+ "v68@0:8@16{_NSRange=QQ}24i40Q44Q52@?60"
+ "v72@0:8@\"FSItem\"16q24Q32@\"NSError\"40Q48Q56@?<v@?@\"NSError\">64"
+ "v72@0:8@\"FSItem\"16q24Q32Q40Q48@\"FSExtentPacker\"56@?<v@?@\"NSError\">64"
+ "v72@0:8@16q24Q32@40Q48Q56@?64"
+ "v72@0:8@16q24Q32Q40Q48@56@?64"
+ "withAttributes"
+ "write(from:startingAt:length:)"
- "%s: Activating volumeName (%@) volumeID (%@)"
- "%s: Received a volumeID (%@) of resource (%@) that is already being used by a different container, so we are modifying the volume ID to (%@) to avoid collision."
- "%s: activate volume (%@) reply(nil)"
- "%s: delegate doesn't have startCheckWithTask:parameters:error: method, try checkResource"
- "%s: delegate doesn't have startFormatWithTask:parameters:error: method, try formatResource"
- "%s: newItem is nil"
- "%s:dirQ==fileQ:error:%d"
- "%s:dirQ==itemQ:error:%d"
- "%s:dirQ==parentQ:error:%d"
- "%s:start:theFile:%@:originalRangeLocation:%lu:originalRangeLength:%lu:ioStatus:%d:flags:%d:operationID:%llu"
- "%s:start:theFile:%@:theRangeLocation:%lu:theRangeLength:%lu:startIO:%d:flags:%d:operationID:%llu"
- "-[FSBlockDeviceResource asynchronousMetadataFlush]"
- "-[FSBlockDeviceResource metadataClear:wait:]"
- "-[FSBlockDeviceResource metadataFlush]"
- "-[FSBlockDeviceResource metadataPurge:]"
- "-[FSBlockDeviceResource metadataReadInto:startingAt:length:readAheadExtents:readAheadCount:]"
- "-[FSFileDataBuffer ensureMappedMB:]"
- "-[FSFileDataBuffer initWithCapacity:andLength:]"
- "-[FSFileDataBuffer initWithCoder:]"
- "-[FSModuleVolume fetchAndSetTypeForItem:]_block_invoke"
- "-[FSModuleVolume getMaxFileSizeInBits]"
- "-[FSModuleVolume getMaxXattrSizeInBits]"
- "-[FSModuleVolume listener:shouldAcceptNewConnection:]"
- "-[FSVolumeConnector blockmapFile:range:startIO:flags:operationID:replyHandler:]"
- "-[FSVolumeConnector blockmapFile:range:startIO:flags:operationID:replyHandler:]_block_invoke_2"
- "-[FSVolumeConnector checkAccessTo:requestedAccess:requestID:replyHandler:]_block_invoke_2"
- "-[FSVolumeConnector close:keepingMode:requestID:replyHandler:]_block_invoke_2"
- "-[FSVolumeConnector createIn:named:type:attributes:requestID:replyHandler:]_block_invoke_2"
- "-[FSVolumeConnector endIO:range:status:flags:operationID:replyHandler:]_block_invoke_2"
- "-[FSVolumeConnector getStandardItemAttributes:]_block_invoke"
- "-[FSVolumeConnector makeCloneOf:named:inDirectory:attributes:usingFlags:requestID:replyHandler:]_block_invoke_2"
- "-[FSVolumeConnector makeLinkOf:named:inDirectory:requestID:replyHandler:]_block_invoke_2"
- "-[FSVolumeConnector makeSymlinkIn:named:contents:attributes:requestID:replyHandler:]_block_invoke_2"
- "-[FSVolumeConnector mount:replyHandler:]_block_invoke_2"
- "-[FSVolumeConnector open:withMode:requestID:replyHandler:]_block_invoke_2"
- "-[FSVolumeConnector readDirectory:withAttr:requestedAttributes:intoBuffer:cookie:verifier:requestID:replyHandler:]_block_invoke_2"
- "-[FSVolumeConnector readFrom:atOffset:intoBuffer:requestID:replyHandler:]_block_invoke_2"
- "-[FSVolumeConnector reclaim:requestID:replyHandler:]_block_invoke_2"
- "-[FSVolumeConnector removeDirectory:from:named:usingFlags:requestID:replyHandler:]_block_invoke_2"
- "-[FSVolumeConnector removeItem:from:named:usingFlags:requestID:replyHandler:]_block_invoke_2"
- "-[FSVolumeConnector setFileAttributesOf:to:requestID:replyHandler:]_block_invoke_2"
- "-[FSVolumeConnector setXattrOf:named:value:how:requestID:replyHandler:]_block_invoke_2"
- "-[FSVolumeConnector unmount:]_block_invoke_2"
- "-[FSVolumeConnector writeTo:atOffset:fromBuffer:requestID:replyHandler:]_block_invoke_2"
- "-[FSVolumeConnector xattrOf:named:requestID:replyHandler:]_block_invoke_2"
- "@\"FSBlockDeviceResource\""
- "@\"NSError\"16@0:8"
- "@\"NSProgress\"40@0:8@\"FSTask\"16@\"NSArray\"24^@32"
- "@28@0:8r*16i24"
- "@32@0:8@16r*24"
- "@32@0:8q16I24I28"
- "@?40@0:8^v16Q24^I32"
- "@?44@0:8^v16Q24^Q32B40"
- "B40@?0@\"FSBlockDeviceResource\"8i16Q20Q28I36"
- "B52@?0@\"FSFileName\"8q16Q24Q32@\"FSItemAttributes\"40B48"
- "FSBlockDeviceOperations"
- "FSFileDataBuffer"
- "FSIOKitNotificationHandler"
- "FSKitStatFSResult:totalBytes(%ld):availableBytes(%ld):freeBytes(%ld):totalFiles(%ld):freeFiles(%ld)"
- "FSMetadataBlockRange"
- "FSModule %{public}@ loadResource: did NOT call reply()"
- "FSModule %{public}@ unloadResource: did NOT call reply()"
- "FSTaskOption.options"
- "FSTaskOption.properties"
- "FSUnaryItem"
- "FSVolumeErrorDomain"
- "Got delegate '%@' conformance N %d S %d Block %d Maintenance %d URL %d isConformantFS %d"
- "T@\"FSBlockDeviceResource\",W,V_resource"
- "T@\"NSError\",&"
- "T@\"NSError\",&,VerrorState"
- "T@\"NSObject<OS_dispatch_queue>\",&"
- "T@\"NSObject<OS_dispatch_queue>\",&,V_fileHandleQueue"
- "T@\"NSObject<OS_dispatch_queue>\",&,V_globalWorkQueue"
- "T@\"NSObject<OS_dispatch_queue>\",R,&,N"
- "TB,?,GareXattrOperationsInhibited"
- "TB,R,N,GisTerminated,V_terminated"
- "TB,R,N,V_isRevoked"
- "TB,R,V_supportsBlockOps"
- "TI,R,V_blockLength"
- "TI,R,V_numberOfBlocks"
- "TQ,N,V_caseSensitivity"
- "TQ,V_length"
- "Tq"
- "Tq,R,V_startBlockOffset"
- "Tq,V_availableBlocks"
- "Tq,V_availableBytes"
- "Tq,V_freeBlocks"
- "Tq,V_freeBytes"
- "Tq,V_freeFiles"
- "Tq,V_totalBlocks"
- "Tq,V_totalBytes"
- "Tq,V_totalFiles"
- "Tq,V_usedBlocks"
- "Tq,V_usedBytes"
- "Tq,VcontainerState"
- "_blockLength"
- "_caseSensitivity"
- "_globalWorkQueue"
- "_isRevoked"
- "_numberOfBlocks"
- "_startBlockOffset"
- "_supportsBlockOps"
- "areXattrOperationsInhibited"
- "asynchronousMetadataFlush"
- "attrsConsumed"
- "attrsWanted"
- "blockLength"
- "blockmapFile:range:startIO:flags:operationID:replyHandler:"
- "blockmapFile:range:startIO:flags:operationID:usingPacker:replyHandler:"
- "capacity"
- "caseSensitivity"
- "com.apple.fskit.fsitem.queue"
- "containerState"
- "createFileNamed:inDirectory:attributes:usingPacker:replyHandler:"
- "errorState"
- "extentPackerForBuffer:bufLen:extentCount:"
- "fetchAndSetTypeForItem:"
- "getStandardItemAttributes:"
- "getStandardItemAttributesData:"
- "getStandardItemAttributesDataForNewItem:"
- "globalWorkQueue"
- "identifierWithUUID:"
- "identifierWithUUID:byteQualifier:"
- "identifierWithUUID:data:"
- "identifierWithUUID:longByteQualifier:"
- "initWithFSTypeName:"
- "initWithOffset:blockLength:numberOfBlocks:"
- "initWithOptionString:count:optionString:errorHandler:"
- "initWithUUID:byteQualifier:"
- "initWithUUID:longByteQualifier:"
- "internalCapacity"
- "isChownRestricted"
- "isTerminated"
- "loadResource returned vol %@ and error %@"
- "lookupItemNamed:inDirectory:usingPacker:replyHandler:"
- "newDirEntryPacker:bufLen:bytesPacked:withAttr:"
- "numberOfBlocks"
- "preallocateSpaceForItem:offset:length:flags:usingPacker:replyHandler:"
- "queueForItem:"
- "r^v16@0:8"
- "rangeWithOffset:blockLength:numberOfBlocks:"
- "renameItemIn:item:oldName:toDirectory:newName:toItem:usingFlags:replyHandler:"
- "renameItemIn:item:oldName:toDirectory:overItem:newName:replyHandler:"
- "setCaseSensitivity:"
- "setContainerState:"
- "setErrorState:"
- "setFileHandleQueue:"
- "setGlobalWorkQueue:"
- "setLength:"
- "startBlockOffset"
- "startCheckWithTask:parameters:error:"
- "startFormatWithTask:parameters:error:"
- "supportsBlockOps"
- "updateRootItem:"
- "v24@0:8@\"NSError\"16"
- "v32@0:8@\"FSTaskOptionsBundle\"16@?<v@?@\"FSItem\"@\"NSError\">24"
- "v40@0:8@\"FSResource\"16@\"NSArray\"24@?<v@?@\"FSVolume\"@\"NSError\">32"
- "v48@0:8@\"FSFileName\"16@\"FSItem\"24@?<B@?@\"FSBlockDeviceResource\"iQQI>32@?<v@?@\"FSItem\"@\"FSFileName\"@\"NSError\">40"
- "v48@0:8@16@24@?32@?40"
- "v56@0:8@\"FSFileName\"16@\"FSItem\"24@\"FSItemSetAttributesRequest\"32@?<B@?@\"FSBlockDeviceResource\"iQQI>40@?<v@?@\"FSItem\"@\"FSFileName\"@\"NSError\">48"
- "v56@0:8@\"FSItem\"16q24Q32@\"NSMutableData\"40@?<v@?Q@\"NSError\">48"
- "v56@0:8@16@24@32@?40@?48"
- "v60@0:8@\"FSItem\"16Q24Q32I40@?<B@?@\"FSBlockDeviceResource\"iQQI>44@?<v@?Q@\"NSError\">52"
- "v60@0:8@16Q24Q32I40@?44@?52"
- "v64@0:8@\"FSFileHandle\"16{_NSRange=QQ}24i40I44Q48@?<v@?i>56"
- "v64@0:8@\"FSFileHandle\"16{_NSRange=QQ}24i40I44Q48@?<v@?i@\"NSData\"@\"NSData\">56"
- "v64@0:8@16{_NSRange=QQ}24i40I44Q48@?56"
- "v68@0:8@\"FSItem\"16{_NSRange=QQ}24@\"NSError\"40I48Q52@?<v@?@\"NSError\">60"
- "v68@0:8@16{_NSRange=QQ}24@40I48Q52@?60"
- "v72@0:8@\"FSItem\"16{_NSRange=QQ}24B40I44Q48@?<B@?@\"FSBlockDeviceResource\"iQQI>56@?<v@?@\"NSError\">64"
- "v72@0:8@16@24@32@40@48@56@?64"
- "v72@0:8@16{_NSRange=QQ}24B40I44Q48@?56@?64"
- "v76@0:8@16@24@32@40@48@56I64@?68"
- "withBytes:"

```
