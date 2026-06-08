## ANEStorageMaintainer

> `/System/Library/PrivateFrameworks/AppleNeuralEngine.framework/XPCServices/ANEStorageMaintainer.xpc/ANEStorageMaintainer`

```diff

-380.601.0.0.0
-  __TEXT.__text: 0x48e0
-  __TEXT.__auth_stubs: 0x3c0
-  __TEXT.__objc_stubs: 0x8e0
-  __TEXT.__objc_methlist: 0x274
-  __TEXT.__const: 0xb8
-  __TEXT.__oslogstring: 0x765
-  __TEXT.__objc_classname: 0x76
-  __TEXT.__objc_methname: 0x910
-  __TEXT.__objc_methtype: 0x1a3
-  __TEXT.__gcc_except_tab: 0x1dc
-  __TEXT.__cstring: 0x78
-  __TEXT.__unwind_info: 0x130
-  __DATA_CONST.__auth_got: 0x1f0
-  __DATA_CONST.__got: 0xa0
-  __DATA_CONST.__const: 0xd0
-  __DATA_CONST.__cfstring: 0x80
-  __DATA_CONST.__objc_classlist: 0x18
+382.7.4.0.0
+  __TEXT.__text: 0x7818
+  __TEXT.__auth_stubs: 0x4d0
+  __TEXT.__objc_stubs: 0xec0
+  __TEXT.__objc_methlist: 0x3b4
+  __TEXT.__const: 0xc8
+  __TEXT.__oslogstring: 0xd7d
+  __TEXT.__objc_classname: 0x86
+  __TEXT.__objc_methname: 0xf94
+  __TEXT.__objc_methtype: 0x26b
+  __TEXT.__gcc_except_tab: 0x154
+  __TEXT.__cstring: 0x1e3
+  __TEXT.__unwind_info: 0x190
+  __DATA_CONST.__const: 0x118
+  __DATA_CONST.__cfstring: 0x2c0
+  __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
+  __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__objc_intobj: 0x18
-  __DATA.__objc_const: 0x360
-  __DATA.__objc_selrefs: 0x330
-  __DATA.__objc_data: 0xf0
+  __DATA_CONST.__auth_got: 0x278
+  __DATA_CONST.__got: 0xd0
+  __DATA.__objc_const: 0x450
+  __DATA.__objc_selrefs: 0x4d8
+  __DATA.__objc_ivar: 0x8
+  __DATA.__objc_data: 0x140
   __DATA.__data: 0x130
-  __DATA.__bss: 0x20
+  __DATA.__bss: 0x38
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOSurface.framework/IOSurface

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 3333BFFF-66AC-3293-8019-E22F896425B6
-  Functions: 50
-  Symbols:   101
-  CStrings:  202
+  UUID: 7E0885BC-BA55-3C6E-84D2-782CD0778D58
+  Functions: 96
+  Symbols:   854
+  CStrings:  339
 
Symbols:
+ 
+ +[_ANEPatchManager initialize]
+ +[_ANEPatchManager sharedManager]
+ +[_ANEStorageHelper _markPurgeablePath:error:]
+ +[_ANEStorageHelper _markPurgeablePath:withFlags:error:]
+ +[_ANEStorageHelper _markPurgeablePath:withFlags:error:].cold.1
+ +[_ANEStorageHelper _markPurgeablePath:withFlags:error:].cold.2
+ +[_ANEStorageHelper addSubdirectoryDetails:directoryPath:size:]
+ +[_ANEStorageHelper createModelCacheDictionary]
+ +[_ANEStorageHelper enableApfsPurging]
+ +[_ANEStorageHelper garbageCollectDanglingModelsAtPath:]
+ +[_ANEStorageHelper garbageCollectDanglingModelsAtPath:].cold.1
+ +[_ANEStorageHelper getAccessTimeForFilePath:]
+ +[_ANEStorageHelper initialize]
+ +[_ANEStorageHelper initialize].cold.1
+ +[_ANEStorageHelper markPathAndDirectParentPurgeable:error:]
+ +[_ANEStorageHelper memoryMapModelAtPath:isPrecompiled:modelAttributes:]
+ +[_ANEStorageHelper memoryMapModelAtPath:isPrecompiled:modelAttributes:].cold.1
+ +[_ANEStorageHelper memoryMapModelAtPath:isPrecompiled:modelAttributes:].cold.2
+ +[_ANEStorageHelper memoryMapModelAtPath:modelAttributes:]
+ +[_ANEStorageHelper memoryMapWeightAtPath:]
+ +[_ANEStorageHelper memoryMapWeightAtPath:].cold.1
+ +[_ANEStorageHelper mergeModelCacheStorageInformation:with:]
+ +[_ANEStorageHelper removeDirectoryAtPath:]
+ +[_ANEStorageHelper removeFilePath:ifDate:olderThanSecond:]
+ +[_ANEStorageHelper removeFilePath:ifDate:olderThanSecond:].cold.1
+ +[_ANEStorageHelper removeShapesDirectoryAtPath:]
+ +[_ANEStorageHelper setAccessTime:forModelFilePath:]
+ +[_ANEStorageHelper sizeOfDirectoryAtPath:recursionLevel:]
+ +[_ANEStorageHelper sizeOfModelCacheAtPath:purgeSubdirectories:]
+ +[_ANEStorageHelper uniqueFirstLevelSubdirectories:]
+ +[_ANEStorageHelper updateAccessTimeForFilePath:]
+ +[_ANEStorageHelper updateAccessTimeForFilePath:].cold.1
+ +[_ANEStorageHelper updateAccessTimeForFilePath:].cold.2
+ +[_ANEStorageHelper updateAccessTimeForFilePath:].cold.3
+ +[_ANEStorageHelper updatePurgeabilityForPath:to:error:]
+ +[_ANEStorageMaintainer initialize]
+ -[ServiceDelegate listener:shouldAcceptNewConnection:]
+ -[_ANEPatchManager .cxx_destruct]
+ -[_ANEPatchManager configurationIdentifierForConfiguration:]
+ -[_ANEPatchManager createDirectoryForPatchedURL:error:]
+ -[_ANEPatchManager dataVaultBaseURL]
+ -[_ANEPatchManager defaultPatchFromURL:toDestination:withConfiguration:error:]
+ -[_ANEPatchManager defaultPatchFromURL:toDestination:withConfiguration:error:].cold.1
+ -[_ANEPatchManager defaultPatchFromURL:toDestination:withConfiguration:error:].cold.2
+ -[_ANEPatchManager defaultPatchFromURL:toDestination:withConfiguration:error:].cold.3
+ -[_ANEPatchManager deletePatchedModelsInDirectory:forModelURL:onlyIfOrphaned:error:]
+ -[_ANEPatchManager deletePatchedModelsInDirectory:forModelURL:onlyIfOrphaned:error:].cold.1
+ -[_ANEPatchManager garbageCollectOrphanedPatchedModelsAtPath:error:]
+ -[_ANEPatchManager initPrivate]
+ -[_ANEPatchManager isPatchedURL:]
+ -[_ANEPatchManager isPatchedURL:].cold.1
+ -[_ANEPatchManager isURLInDataVault:]
+ -[_ANEPatchManager metadataURLForPatchedURL:]
+ -[_ANEPatchManager modelURLForPatchedURL:]
+ -[_ANEPatchManager parentHashForModelURL:]
+ -[_ANEPatchManager parentHashForModelURL:].cold.1
+ -[_ANEPatchManager patchModelAtURL:csIdentity:withConfiguration:usingPatcher:error:]
+ -[_ANEPatchManager patchModelAtURL:toPatchedURL:withConfiguration:usingPatcher:error:]
+ -[_ANEPatchManager patchedModelExistsForURL:csIdentity:configuration:]
+ -[_ANEPatchManager patchedModelsDirectoryForModelURL:csIdentity:]
+ -[_ANEPatchManager patchedModelsDirectoryForModelURL:csIdentity:].cold.1
+ -[_ANEPatchManager patchedURLForModelURL:csIdentity:configuration:]
+ -[_ANEPatchManager patchedURLForModelURL:csIdentity:configuration:].cold.1
+ -[_ANEPatchManager patchedURLForModelURL:csIdentity:configuration:].cold.2
+ -[_ANEPatchManager purgeAllPatchedModelsForModelURL:csIdentity:error:]
+ -[_ANEPatchManager purgeAllPatchedModelsForModelURL:csIdentity:error:].cold.1
+ -[_ANEPatchManager sanitizedOriginalName:]
+ -[_ANEPatchManager sanitizedOriginalName:].cold.1
+ -[_ANEPatchManager saveModelURLForPatchedURL:modelURL:configuration:]
+ -[_ANEPatchManager saveModelURLForPatchedURL:modelURL:configuration:].cold.1
+ -[_ANEPatchManager saveModelURLForPatchedURL:modelURL:configuration:].cold.2
+ -[_ANEStorageMaintainer purgeDanglingModelsAt:withReply:]
+ -[_ANEStorageMaintainer purgeDanglingModelsAt:withReply:].cold.1
+ /Library/Caches/com.apple.xbs/01273E70-6169-4366-936B-5D7E907FCA58/TemporaryDirectory.QWwnZm/Binaries/AppleNeuralEngine_CompilerService/install/TempContent/Objects/AppleNeuralEngine.build/ANEStorageMaintainer.build/DerivedSources/
+ /Library/Caches/com.apple.xbs/01273E70-6169-4366-936B-5D7E907FCA58/TemporaryDirectory.QWwnZm/Binaries/AppleNeuralEngine_CompilerService/install/TempContent/Objects/AppleNeuralEngine.build/ANEStorageMaintainer.build/Objects-normal/arm64e/ANEStorageMaintainer_vers.o
+ /Library/Caches/com.apple.xbs/01273E70-6169-4366-936B-5D7E907FCA58/TemporaryDirectory.QWwnZm/Binaries/AppleNeuralEngine_CompilerService/install/TempContent/Objects/AppleNeuralEngine.build/ANEStorageMaintainer.build/Objects-normal/arm64e/_ANEPatchManager.o
+ /Library/Caches/com.apple.xbs/01273E70-6169-4366-936B-5D7E907FCA58/TemporaryDirectory.QWwnZm/Binaries/AppleNeuralEngine_CompilerService/install/TempContent/Objects/AppleNeuralEngine.build/ANEStorageMaintainer.build/Objects-normal/arm64e/_ANEStorageHelper.o
+ /Library/Caches/com.apple.xbs/01273E70-6169-4366-936B-5D7E907FCA58/TemporaryDirectory.QWwnZm/Binaries/AppleNeuralEngine_CompilerService/install/TempContent/Objects/AppleNeuralEngine.build/ANEStorageMaintainer.build/Objects-normal/arm64e/_ANEStorageMaintainer.o
+ /Library/Caches/com.apple.xbs/01273E70-6169-4366-936B-5D7E907FCA58/TemporaryDirectory.QWwnZm/Binaries/AppleNeuralEngine_CompilerService/install/TempContent/Objects/AppleNeuralEngine.build/ANEStorageMaintainer.build/Objects-normal/arm64e/main.o
+ /Library/Caches/com.apple.xbs/01273E70-6169-4366-936B-5D7E907FCA58/TemporaryDirectory.QWwnZm/Sources/AppleNeuralEngine_CompilerService/ANEStorageMaintainer/
+ /Library/Caches/com.apple.xbs/01273E70-6169-4366-936B-5D7E907FCA58/TemporaryDirectory.QWwnZm/Sources/AppleNeuralEngine_CompilerService/Common/
+ /Library/Caches/com.apple.xbs/01273E70-6169-4366-936B-5D7E907FCA58/TemporaryDirectory.QWwnZm/Sources/AppleNeuralEngine_CompilerService/aned/
+ ANEPatchManager.m
+ ANEStorageHelper.m
+ ANEStorageMaintainer.m
+ ANEStorageMaintainer_vers.c
+ GCC_except_table5
+ GCC_except_table9
+ OBJC_IVAR_$__ANEPatchManager._dataVaultBaseURL
+ OBJC_IVAR_$__ANEPatchManager._serialQueue
+ _CC_SHA256
+ _NSCocoaErrorDomain
+ _NSLocalizedDescriptionKey
+ _OBJC_CLASS_$_NSCharacterSet
+ _OBJC_CLASS_$_NSMutableString
+ _OBJC_CLASS_$_NSPropertyListSerialization
+ _OBJC_CLASS_$_NSURL
+ _OBJC_CLASS_$__ANEPatchManager
+ _OBJC_METACLASS_$__ANEPatchManager
+ _OUTLINED_FUNCTION_0
+ _OUTLINED_FUNCTION_1
+ _OUTLINED_FUNCTION_2
+ _OUTLINED_FUNCTION_3
+ _OUTLINED_FUNCTION_4
+ _OUTLINED_FUNCTION_5
+ _OUTLINED_FUNCTION_6
+ _OUTLINED_FUNCTION_7
+ _OUTLINED_FUNCTION_8
+ __43+[_ANEStorageHelper memoryMapWeightAtPath:]_block_invoke.7
+ __43+[_ANEStorageHelper memoryMapWeightAtPath:]_block_invoke.8
+ __72+[_ANEStorageHelper memoryMapModelAtPath:isPrecompiled:modelAttributes:]_block_invoke.4
+ __72+[_ANEStorageHelper memoryMapModelAtPath:isPrecompiled:modelAttributes:]_block_invoke.6
+ __86-[_ANEPatchManager patchModelAtURL:toPatchedURL:withConfiguration:usingPatcher:error:]_block_invoke.cold.1
+ __OBJC_$_CLASS_METHODS__ANEPatchManager
+ __OBJC_$_CLASS_METHODS__ANEStorageHelper
+ __OBJC_$_CLASS_METHODS__ANEStorageMaintainer
+ __OBJC_$_INSTANCE_METHODS_ServiceDelegate
+ __OBJC_$_INSTANCE_METHODS__ANEPatchManager
+ __OBJC_$_INSTANCE_METHODS__ANEStorageMaintainer
+ __OBJC_$_INSTANCE_VARIABLES__ANEPatchManager
+ __OBJC_$_PROP_LIST_NSObject
+ __OBJC_$_PROP_LIST_ServiceDelegate
+ __OBJC_$_PROP_LIST__ANEPatchManager
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSXPCListenerDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS__ANEStorageMaintainerProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSXPCListenerDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES__ANEStorageMaintainerProtocol
+ __OBJC_$_PROTOCOL_REFS_NSXPCListenerDelegate
+ __OBJC_CLASS_PROTOCOLS_$_ServiceDelegate
+ __OBJC_CLASS_PROTOCOLS_$__ANEStorageMaintainer
+ __OBJC_CLASS_RO_$_ServiceDelegate
+ __OBJC_CLASS_RO_$__ANEPatchManager
+ __OBJC_CLASS_RO_$__ANEStorageHelper
+ __OBJC_CLASS_RO_$__ANEStorageMaintainer
+ __OBJC_LABEL_PROTOCOL_$_NSObject
+ __OBJC_LABEL_PROTOCOL_$_NSXPCListenerDelegate
+ __OBJC_LABEL_PROTOCOL_$__ANEStorageMaintainerProtocol
+ __OBJC_METACLASS_RO_$_ServiceDelegate
+ __OBJC_METACLASS_RO_$__ANEPatchManager
+ __OBJC_METACLASS_RO_$__ANEStorageHelper
+ __OBJC_METACLASS_RO_$__ANEStorageMaintainer
+ __OBJC_PROTOCOL_$_NSObject
+ __OBJC_PROTOCOL_$_NSXPCListenerDelegate
+ __OBJC_PROTOCOL_$__ANEStorageMaintainerProtocol
+ __OBJC_PROTOCOL_REFERENCE_$__ANEStorageMaintainerProtocol
+ ___31+[_ANEStorageHelper initialize]_block_invoke
+ ___33+[_ANEPatchManager sharedManager]_block_invoke
+ ___43+[_ANEStorageHelper memoryMapWeightAtPath:]_block_invoke
+ ___56+[_ANEStorageHelper garbageCollectDanglingModelsAtPath:]_block_invoke
+ ___72+[_ANEStorageHelper memoryMapModelAtPath:isPrecompiled:modelAttributes:]_block_invoke
+ ___84-[_ANEPatchManager deletePatchedModelsInDirectory:forModelURL:onlyIfOrphaned:error:]_block_invoke
+ ___86-[_ANEPatchManager patchModelAtURL:toPatchedURL:withConfiguration:usingPatcher:error:]_block_invoke
+ ___Block_byref_object_copy_
+ ___Block_byref_object_dispose_
+ ___block_descriptor_192_e8_32r_e5_v8?0lr32l8
+ ___block_descriptor_32_e5_v8?0l
+ ___block_descriptor_40_e27_B24?0"NSURL"8"NSError"16l
+ ___block_descriptor_40_e5_v8?0l
+ ___block_descriptor_40_e8_32r_e5_v8?0lr32l8
+ ___block_descriptor_48_e12_v24?0^v8Q16l
+ ___block_descriptor_96_e8_32s40s48s56s64s72r80r_e5_v8?0ls32l8s40l8r72l8r80l8s48l8s56l8s64l8
+ ___block_literal_global
+ __gAsyncIOq
+ __gLogger
+ _dispatch_sync
+ _fclose
+ _fopen
+ _fwrite
+ _gLogger
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$URLByAppendingPathComponent:
+ _objc_msgSend$URLByAppendingPathExtension:
+ _objc_msgSend$URLByDeletingLastPathComponent
+ _objc_msgSend$URLByStandardizingPath
+ _objc_msgSend$UTF8String
+ _objc_msgSend$_markPurgeablePath:error:
+ _objc_msgSend$_markPurgeablePath:withFlags:error:
+ _objc_msgSend$addEntriesFromDictionary:
+ _objc_msgSend$addObject:
+ _objc_msgSend$addSubdirectoryDetails:directoryPath:size:
+ _objc_msgSend$allKeys
+ _objc_msgSend$appendFormat:
+ _objc_msgSend$arrayWithObjects:count:
+ _objc_msgSend$attributesOfItemAtPath:error:
+ _objc_msgSend$boolValue
+ _objc_msgSend$buildSpecificModelDataVaultDirectory
+ _objc_msgSend$bytes
+ _objc_msgSend$characterAtIndex:
+ _objc_msgSend$characterIsMember:
+ _objc_msgSend$characterSetWithCharactersInString:
+ _objc_msgSend$code
+ _objc_msgSend$compare:
+ _objc_msgSend$configurationIdentifierForConfiguration:
+ _objc_msgSend$copy
+ _objc_msgSend$countByEnumeratingWithState:objects:count:
+ _objc_msgSend$createDirectoryAtPath:withIntermediateDirectories:attributes:error:
+ _objc_msgSend$createDirectoryForPatchedURL:error:
+ _objc_msgSend$createModelCacheDictionary
+ _objc_msgSend$daemon
+ _objc_msgSend$dataVaultBaseURL
+ _objc_msgSend$dataWithContentsOfURL:options:error:
+ _objc_msgSend$dataWithPropertyList:format:options:error:
+ _objc_msgSend$dateWithTimeIntervalSince1970:
+ _objc_msgSend$dateWithTimeIntervalSinceNow:
+ _objc_msgSend$defaultManager
+ _objc_msgSend$defaultPatchFromURL:toDestination:withConfiguration:error:
+ _objc_msgSend$deletePatchedModelsInDirectory:forModelURL:onlyIfOrphaned:error:
+ _objc_msgSend$dictionaryWithContentsOfURL:error:
+ _objc_msgSend$dictionaryWithObjects:forKeys:count:
+ _objc_msgSend$enumeratorAtURL:includingPropertiesForKeys:options:errorHandler:
+ _objc_msgSend$errorWithDomain:code:userInfo:
+ _objc_msgSend$fileExistsAtPath:
+ _objc_msgSend$fileExistsAtPath:isDirectory:
+ _objc_msgSend$fileSize
+ _objc_msgSend$fileURLWithPath:
+ _objc_msgSend$fileURLWithPath:isDirectory:
+ _objc_msgSend$firstObject
+ _objc_msgSend$framework
+ _objc_msgSend$garbageCollectDanglingModelsAtPath:
+ _objc_msgSend$garbageCollectOrphanedPatchedModelsAtPath:error:
+ _objc_msgSend$getAccessTimeForFilePath:
+ _objc_msgSend$hasPrefix:
+ _objc_msgSend$initPrivate
+ _objc_msgSend$initWithBytesNoCopy:length:deallocator:
+ _objc_msgSend$interfaceWithProtocol:
+ _objc_msgSend$invalidate
+ _objc_msgSend$isEqualToString:
+ _objc_msgSend$isPatchedURL:
+ _objc_msgSend$isURLInDataVault:
+ _objc_msgSend$lastPathComponent
+ _objc_msgSend$length
+ _objc_msgSend$localizedDescription
+ _objc_msgSend$maintenance
+ _objc_msgSend$memoryMapModelAtPath:isPrecompiled:modelAttributes:
+ _objc_msgSend$metadataURLForPatchedURL:
+ _objc_msgSend$modelAssetsCacheName
+ _objc_msgSend$modelBinaryName
+ _objc_msgSend$modelCacheRetainName
+ _objc_msgSend$modelSourceStoreName
+ _objc_msgSend$modelURLForPatchedURL:
+ _objc_msgSend$mutableCopy
+ _objc_msgSend$numberWithUnsignedInteger:
+ _objc_msgSend$numberWithUnsignedLongLong:
+ _objc_msgSend$objectForKeyedSubscript:
+ _objc_msgSend$parentHashForModelURL:
+ _objc_msgSend$patchModelAtURL:toPatchedURL:withConfiguration:usingPatcher:error:
+ _objc_msgSend$patchModelFromURL:toDestination:withConfiguration:error:
+ _objc_msgSend$patchedModelsDirectoryForModelURL:csIdentity:
+ _objc_msgSend$patchedURLForModelURL:csIdentity:configuration:
+ _objc_msgSend$path
+ _objc_msgSend$pathComponents
+ _objc_msgSend$perfStatsMask
+ _objc_msgSend$processIdentifier
+ _objc_msgSend$removeDirectoryAtPath:
+ _objc_msgSend$removeItemAtPath:error:
+ _objc_msgSend$removeItemAtURL:error:
+ _objc_msgSend$replaceCharactersInRange:withString:
+ _objc_msgSend$resume
+ _objc_msgSend$sanitizedOriginalName:
+ _objc_msgSend$saveModelURLForPatchedURL:modelURL:configuration:
+ _objc_msgSend$serviceListener
+ _objc_msgSend$set
+ _objc_msgSend$setAccessTime:forModelFilePath:
+ _objc_msgSend$setByAddingObjectsFromArray:
+ _objc_msgSend$setDelegate:
+ _objc_msgSend$setExportedInterface:
+ _objc_msgSend$setExportedObject:
+ _objc_msgSend$setObject:forKeyedSubscript:
+ _objc_msgSend$setWithArray:
+ _objc_msgSend$sharedManager
+ _objc_msgSend$sizeOfDirectoryAtPath:recursionLevel:
+ _objc_msgSend$storageMaintainerAccessEntitlement
+ _objc_msgSend$stringByAppendingPathComponent:
+ _objc_msgSend$stringByDeletingLastPathComponent
+ _objc_msgSend$stringByDeletingPathExtension
+ _objc_msgSend$stringValue
+ _objc_msgSend$stringWithCapacity:
+ _objc_msgSend$stringWithContentsOfURL:encoding:error:
+ _objc_msgSend$stringWithFormat:
+ _objc_msgSend$stringWithString:
+ _objc_msgSend$subpathsOfDirectoryAtPath:error:
+ _objc_msgSend$substringToIndex:
+ _objc_msgSend$timeIntervalSince1970
+ _objc_msgSend$uniqueFirstLevelSubdirectories:
+ _objc_msgSend$unsignedIntegerValue
+ _objc_msgSend$unsignedLongLongValue
+ _objc_msgSend$updateAccessTimeForFilePath:
+ _objc_msgSend$valueForEntitlement:
+ _objc_msgSendSuper2
+ _objc_release
+ _objc_release_x27
+ _objc_retain
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x27
+ _objc_retain_x3
+ _objc_retain_x5
+ _objc_retain_x8
+ _objc_storeStrong
+ _strlen
+ initialize.onceToken
+ main.m
+ sharedManager.onceToken
+ sharedManager.shared
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x28
- radr://5614542
CStrings:
+ ""
+ "%02x"
+ "%@: %@"
+ "%@: Completed - TotalFiles=%lu, Deleted=%lu"
+ "%@: Directory %@ does not exist, nothing to delete"
+ "%@: Enumeration error at %{public}@: %{public}@"
+ "%@: Failed to delete %{public}@: %{public}@"
+ "%@: Failed to delete metadata for %{public}@: %{public}@"
+ "%@: Failed to open metadata file for writing at %@: %s"
+ "%@: Failed to read metadata for %@: %@"
+ "%@: Failed to read metadata for patched URL %@: %@"
+ "%@: Failed to read source model at %@: %@"
+ "%@: Failed to remove existing file at %@: %@"
+ "%@: Failed to remove patched file at %@: %@"
+ "%@: Failed to serialize metadata: %@"
+ "%@: Failed to write metadata (wrote %zu/%lu bytes)"
+ "%@: Garbage collecting orphaned patched models at: %@"
+ "%@: Metadata missing patchedURL for %@"
+ "%@: Model %@ dataVault, modelURL: %@, patchedURL: %@"
+ "%@: Patched model GC failed: %@"
+ "%@: Patching succeeded but metadata save failed. Cleaning up patched file at %@"
+ "%@: Path mismatch - URL: %@ (normalized: %@), Metadata: %@ (normalized: %@)"
+ "%@: Purging patched models for modelURL: %@ in directory: %@"
+ "%@: Read source model: %lu bytes from %@"
+ "%@: Scanning directory: %@, onlyIfOrphaned=%d"
+ "%@: Skipping %{public}@: already deleted (concurrent cleanup)"
+ "%@: Skipping %{public}@: metadata unavailable (possibly already cleaned up)"
+ "%@: Skipping metadata for %{public}@: already deleted (concurrent cleanup)"
+ "%@: Successfully saved metadata: %lu bytes to %@"
+ "%@: Successfully wrote patched model: %zu bytes to %@"
+ "%@: Warning: fclose returned %d"
+ "%@: nil filename"
+ "%@: nil modelURL"
+ "%@: nil parentHash for modelURL=%@"
+ "%@: nil sanitizedOriginalName for modelURL=%@"
+ "%@_patched.hwx"
+ "%@_patched_%@.hwx"
+ ".cxx_destruct"
+ "0"
+ "@\"NSObject<OS_dispatch_queue>\""
+ "@\"NSURL\""
+ "@40@0:8@16@24@32"
+ "@56@0:8@16@24@32@40^@48"
+ "B40@0:8@16@24@32"
+ "B40@0:8@16@24^@32"
+ "B40@0:8@16Q24^@32"
+ "B44@0:8@16@24B32^@36"
+ "B48@0:8@16@24@32^@40"
+ "B56@0:8@16@24@32@40^@48"
+ "Failed to open destination file for writing: %s"
+ "Failed to save metadata for patched model"
+ "Patched_%@"
+ "Size mismatch: wrote %zu bytes, expected %lu bytes"
+ "T@\"NSURL\",R,N,V_dataVaultBaseURL"
+ "URLByAppendingPathExtension:"
+ "URLByStandardizingPath"
+ "_"
+ "_ANEPatchManager"
+ "_dataVaultBaseURL"
+ "_markPurgeablePath:withFlags:error:"
+ "_serialQueue"
+ "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_"
+ "appendFormat:"
+ "buildSpecificModelDataVaultDirectory"
+ "characterAtIndex:"
+ "characterIsMember:"
+ "characterSetWithCharactersInString:"
+ "code"
+ "com.apple.ane.patcher"
+ "com.apple.ane.patching"
+ "configurationIdentifierForConfiguration:"
+ "createDirectoryAtPath:withIntermediateDirectories:attributes:error:"
+ "createDirectoryForPatchedURL:error:"
+ "dataVaultBaseURL"
+ "dataWithContentsOfURL:options:error:"
+ "dataWithPropertyList:format:options:error:"
+ "defaultPatchFromURL:toDestination:withConfiguration:error:"
+ "deletePatchedModelsInDirectory:forModelURL:onlyIfOrphaned:error:"
+ "dictionaryWithContentsOfURL:error:"
+ "fileExistsAtPath:"
+ "fileURLWithPath:"
+ "fileURLWithPath:isDirectory:"
+ "framework"
+ "garbageCollectOrphanedPatchedModelsAtPath:error:"
+ "hasPrefix:"
+ "in"
+ "init"
+ "initPrivate"
+ "isPatchedURL:"
+ "isURLInDataVault:"
+ "localizedDescription"
+ "metadataURLForPatchedURL:"
+ "modelAssetsCacheName"
+ "modelURL"
+ "modelURLForPatchedURL:"
+ "outside"
+ "parentHashForModelURL:"
+ "patchModelAtURL:csIdentity:withConfiguration:usingPatcher:error:"
+ "patchModelAtURL:toPatchedURL:withConfiguration:usingPatcher:error:"
+ "patchModelFromURL:toDestination:withConfiguration:error:"
+ "patchedModelExistsForURL:csIdentity:configuration:"
+ "patchedModelsDirectoryForModelURL:csIdentity:"
+ "patchedURL"
+ "patchedURLForModelURL:csIdentity:configuration:"
+ "perfStatsMask"
+ "perfStatsMask%@"
+ "plist"
+ "purgeAllPatchedModelsForModelURL:csIdentity:error:"
+ "replaceCharactersInRange:withString:"
+ "sanitizedOriginalName:"
+ "saveModelURLForPatchedURL:modelURL:configuration:"
+ "sharedManager"
+ "stringByDeletingPathExtension"
+ "stringValue"
+ "stringWithCapacity:"
+ "stringWithFormat:"
+ "stringWithString:"
+ "substringToIndex:"
+ "updatePurgeabilityForPath:to:error:"
+ "wb"

```
