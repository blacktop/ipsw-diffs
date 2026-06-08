## ANECompilerService

> `/System/Library/PrivateFrameworks/AppleNeuralEngine.framework/XPCServices/ANECompilerService.xpc/ANECompilerService`

```diff

-380.601.0.0.0
-  __TEXT.__text: 0x119c0
-  __TEXT.__auth_stubs: 0x6d0
-  __TEXT.__objc_stubs: 0x1860
-  __TEXT.__objc_methlist: 0x79c
-  __TEXT.__const: 0xf8
-  __TEXT.__cstring: 0xa2c
-  __TEXT.__gcc_except_tab: 0xe40
-  __TEXT.__objc_methname: 0x1b77
-  __TEXT.__oslogstring: 0x1595
-  __TEXT.__objc_classname: 0x183
-  __TEXT.__objc_methtype: 0x52b
-  __TEXT.__unwind_info: 0x3a8
-  __DATA_CONST.__auth_got: 0x380
-  __DATA_CONST.__got: 0x150
-  __DATA_CONST.__const: 0x250
-  __DATA_CONST.__cfstring: 0xc80
-  __DATA_CONST.__objc_classlist: 0x70
+382.7.4.0.0
+  __TEXT.__text: 0x16158
+  __TEXT.__auth_stubs: 0x790
+  __TEXT.__objc_stubs: 0x1fc0
+  __TEXT.__objc_methlist: 0x944
+  __TEXT.__const: 0x100
+  __TEXT.__cstring: 0xe77
+  __TEXT.__oslogstring: 0x1fef
+  __TEXT.__objc_classname: 0x19e
+  __TEXT.__objc_methname: 0x2332
+  __TEXT.__objc_methtype: 0x601
+  __TEXT.__gcc_except_tab: 0xee8
+  __TEXT.__unwind_info: 0x420
+  __DATA_CONST.__const: 0x300
+  __DATA_CONST.__cfstring: 0x12c0
+  __DATA_CONST.__objc_classlist: 0x80
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x18
+  __DATA_CONST.__objc_superrefs: 0x20
   __DATA_CONST.__objc_intobj: 0x60
-  __DATA.__objc_const: 0xb78
-  __DATA.__objc_selrefs: 0x7c0
-  __DATA.__objc_ivar: 0x1c
-  __DATA.__objc_data: 0x460
-  __DATA.__data: 0x358
-  __DATA.__bss: 0x50
+  __DATA_CONST.__auth_got: 0x3e0
+  __DATA_CONST.__got: 0x188
+  __DATA.__objc_const: 0xd20
+  __DATA.__objc_selrefs: 0x9d0
+  __DATA.__objc_ivar: 0x24
+  __DATA.__objc_data: 0x500
+  __DATA.__data: 0x3c8
+  __DATA.__bss: 0x88
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsandbox.1.dylib
-  UUID: 273F5818-95B6-3CFB-B26C-3B45B5A6AA9C
-  Functions: 210
-  Symbols:   240
-  CStrings:  694
+  UUID: F88DEFC4-623C-3856-8BEC-B89CBD6AF0CF
+  Functions: 285
+  Symbols:   2400
+  CStrings:  929
 
Symbols:
+ 
+ +[NSFileManager(ANE) ane_addWriteModeForPath:]
+ +[NSFileManager(ANE) ane_addWriteModeForPath:].cold.1
+ +[NSFileManager(ANE) ane_addWriteModeIfMissing:originalMode:]
+ +[NSFileManager(ANE) sizeOfDirectoryOrFileAtPath:]
+ +[NSFileManager(ANE) sizeOfDirectoryOrFileAtPath:].cold.1
+ +[_ANECVAIRCompiler compileModelAt:csIdentity:plistFilename:optionsFilename:outputURL:saveSourceURL:aotModelBinaryPath:isEncryptedModel:options:ok:error:]
+ +[_ANECVAIRCompiler compileModelAt:csIdentity:plistFilename:optionsFilename:outputURL:saveSourceURL:aotModelBinaryPath:isEncryptedModel:options:ok:error:].cold.1
+ +[_ANECompiler applyDebugOptions:toCompilerOptions:]
+ +[_ANECompiler applyDebugOptions:toCompilerOptions:].cold.1
+ +[_ANECompiler applyDebugOptions:toCompilerOptions:].cold.2
+ +[_ANECompiler compileModel:options:ok:error:]
+ +[_ANECompiler compileModel:options:ok:error:].cold.1
+ +[_ANECompiler compileModel:options:ok:error:].cold.10
+ +[_ANECompiler compileModel:options:ok:error:].cold.11
+ +[_ANECompiler compileModel:options:ok:error:].cold.12
+ +[_ANECompiler compileModel:options:ok:error:].cold.13
+ +[_ANECompiler compileModel:options:ok:error:].cold.2
+ +[_ANECompiler compileModel:options:ok:error:].cold.3
+ +[_ANECompiler compileModel:options:ok:error:].cold.4
+ +[_ANECompiler compileModel:options:ok:error:].cold.5
+ +[_ANECompiler compileModel:options:ok:error:].cold.6
+ +[_ANECompiler compileModel:options:ok:error:].cold.7
+ +[_ANECompiler compileModel:options:ok:error:].cold.8
+ +[_ANECompiler compileModel:options:ok:error:].cold.9
+ +[_ANECompiler compileModelJIT:ok:error:]
+ +[_ANECompiler compileModelJIT:ok:error:].cold.1
+ +[_ANECompiler compileModelJIT:ok:error:].cold.2
+ +[_ANECompiler compileModelJIT:ok:error:].cold.3
+ +[_ANECompiler compileModelJIT:ok:error:].cold.4
+ +[_ANECompiler compileModelJIT:ok:error:].cold.5
+ +[_ANECompiler compileModelJIT:ok:error:].cold.6
+ +[_ANECompiler createErrorWithUnderlyingError:]
+ +[_ANECompiler createErrorWithUnderlyingError:].cold.1
+ +[_ANECompiler createExternConstants:]
+ +[_ANECompiler createExternConstants:].cold.1
+ +[_ANECompiler createExternConstants:].cold.2
+ +[_ANECompiler createExternConstants:].cold.3
+ +[_ANECompiler createInMemoryConstants:]
+ +[_ANECompiler createInMemoryConstants:].cold.1
+ +[_ANECompiler createInMemoryConstants:].cold.2
+ +[_ANECompiler createInMemoryConstants:].cold.3
+ +[_ANECompiler createInMemoryConstants:].cold.4
+ +[_ANECompiler createJITNetworkFromModelAtPath:modelFilename:aotModelAtPath:aotModelFilename:]
+ +[_ANECompiler createNetworkFromModelAtPath:modelFilename:]
+ +[_ANECompiler initialize]
+ +[_ANECompilerService initialize]
+ +[_ANECoreMLModelCompiler compileModelAt:csIdentity:key:optionsFilename:tempDirectory:outputURL:saveSourceModelPath:aotModelBinaryPath:isEncryptedModel:options:ok:error:]
+ +[_ANECoreMLModelCompiler compileModelAt:csIdentity:key:optionsFilename:tempDirectory:outputURL:saveSourceModelPath:aotModelBinaryPath:isEncryptedModel:options:ok:error:].cold.1
+ +[_ANECoreMLModelCompiler compileModelAt:csIdentity:key:optionsFilename:tempDirectory:outputURL:saveSourceModelPath:aotModelBinaryPath:isEncryptedModel:options:ok:error:].cold.2
+ +[_ANECoreMLModelCompiler createErrorWithString:]
+ +[_ANECoreMLModelCompiler createErrorWithString:].cold.1
+ +[_ANECoreMLModelCompiler initialize]
+ +[_ANECoreMLModelCompiler pathsForModelURL:]
+ +[_ANEDebugUtils applyDebugEnvToOptions:]
+ +[_ANEDebugUtils applyDebugEnvToOptions:].cold.1
+ +[_ANEDebugUtils applyDebugEnvToOptions:].cold.2
+ +[_ANEDebugUtils applyDebugEnvToOptions:].cold.3
+ +[_ANEDebugUtils parseDebugEnvVar]
+ +[_ANEDebugUtils parseDebugString:]
+ +[_ANEEspressoIRTranslator createErrorForPlan:status:]
+ +[_ANEEspressoIRTranslator createErrorForPlan:status:].cold.1
+ +[_ANEEspressoIRTranslator destroyEspresso:ctx:]
+ +[_ANEEspressoIRTranslator translateModelAt:key:outputPath:isEncryptedModel:translationOptions:error:]
+ +[_ANEInMemoryModelCacheManager new]
+ +[_ANEInMemoryModelCacheManager notRecentlyUsedSecondsThreshold]
+ +[_ANEInMemoryModelCacheManager removeFilesFromDirectory:notAccessedInSeconds:]
+ +[_ANEInMemoryModelCacheManager removeStaleModelsAtPath:]
+ +[_ANEMILCompiler compileModelAt:modelName:csIdentity:optionsFilename:outputURL:saveSourceURL:aotModelBinaryPath:isEncryptedModel:options:maxModelMemorySize:ok:error:]
+ +[_ANEMILCompiler compileModelAt:modelName:csIdentity:optionsFilename:outputURL:saveSourceURL:aotModelBinaryPath:isEncryptedModel:options:maxModelMemorySize:ok:error:].cold.1
+ +[_ANEMLIRCompiler compileModelAt:modelName:csIdentity:optionsFilename:outputURL:saveSourceURL:aotModelBinaryPath:isEncryptedModel:options:mpsConstants:externConstants:maxModelMemorySize:ok:error:]
+ +[_ANEMLIRCompiler compileModelAt:modelName:csIdentity:optionsFilename:outputURL:saveSourceURL:aotModelBinaryPath:isEncryptedModel:options:mpsConstants:externConstants:maxModelMemorySize:ok:error:].cold.1
+ +[_ANEModelCacheManager cachedModelRetainNameFor:]
+ +[_ANEModelCacheManager cachedSourceModelStoreNameFor:]
+ +[_ANEModelCacheManager createModelCacheRetain:]
+ +[_ANEModelCacheManager createModelCacheRetain:].cold.1
+ +[_ANEModelCacheManager initialize]
+ +[_ANEModelCacheManager initialize].cold.1
+ +[_ANEModelCacheManager isSystemModelPath:]
+ +[_ANEModelCacheManager new]
+ +[_ANEModelCacheManager removeIfStaleBinary:forModelPath:]
+ +[_ANEModelCacheManager saveSourceModelPath:outputModelDirectory:]
+ +[_ANEPatchManager initialize]
+ +[_ANEPatchManager sharedManager]
+ +[_ANESandboxingHelper canAccessPathAt:methodName:error:]
+ +[_ANESandboxingHelper consumeSandboxExtension:forModel:error:]
+ +[_ANESandboxingHelper consumeSandboxExtension:forPath:error:]
+ +[_ANESandboxingHelper consumeSandboxExtension:forPath:error:].cold.1
+ +[_ANESandboxingHelper consumeSandboxExtension:forPath:error:].cold.2
+ +[_ANESandboxingHelper initialize]
+ +[_ANESandboxingHelper issueSandboxExtensionForModel:error:]
+ +[_ANESandboxingHelper issueSandboxExtensionForPath:error:]
+ +[_ANESandboxingHelper issueSandboxExtensionForPath:error:].cold.1
+ +[_ANESandboxingHelper releaseSandboxExtension:handle:]
+ +[_ANESandboxingHelper sandboxExtensionPathForModelURL:]
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
+ +[_ANETask new]
+ +[_ANETask taskWithName:period:handler:]
+ +[_ANETaskManager registerTask:]
+ +[_ANETaskManager unregisterTask:]
+ -[ServiceDelegate listener:shouldAcceptNewConnection:]
+ -[_ANECompilerService compileModelAt:csIdentity:sandboxExtension:options:tempDirectory:cloneDirectory:outputURL:aotModelBinaryPath:maxModelMemorySize:withReply:]
+ -[_ANECompilerService updateSourcePathAt:to:withReply:]
+ -[_ANEInMemoryModelCacheManager .cxx_destruct]
+ -[_ANEInMemoryModelCacheManager URLForBundleID:]
+ -[_ANEInMemoryModelCacheManager URLForBundleID:].cold.1
+ -[_ANEInMemoryModelCacheManager URLForModelHash:bundleID:]
+ -[_ANEInMemoryModelCacheManager URLForModelHash:bundleID:].cold.1
+ -[_ANEInMemoryModelCacheManager cacheDir]
+ -[_ANEInMemoryModelCacheManager cachedModelPathMatchingHash:csIdentity:]
+ -[_ANEInMemoryModelCacheManager getDiskSpaceForBundleID:]
+ -[_ANEInMemoryModelCacheManager getDiskSpaceItemizedByBundleIDAndPurge:]
+ -[_ANEInMemoryModelCacheManager initWithURL:]
+ -[_ANEInMemoryModelCacheManager initWithURL:createDirectory:]
+ -[_ANEInMemoryModelCacheManager init]
+ -[_ANEInMemoryModelCacheManager removeAllModelsForBundleID:]
+ -[_ANEInMemoryModelCacheManager removeStaleModels]
+ -[_ANEInMemoryModelCacheManager scheduleMaintenanceWithName:directoryPaths:]
+ -[_ANEInMemoryModelCacheManager shouldEnforceSizeLimits]
+ -[_ANEModelCacheManager .cxx_destruct]
+ -[_ANEModelCacheManager URLForBundleID:]
+ -[_ANEModelCacheManager URLForBundleID:].cold.1
+ -[_ANEModelCacheManager URLForModel:bundleID:]
+ -[_ANEModelCacheManager URLForModel:bundleID:aotCacheUrlIdentifier:]
+ -[_ANEModelCacheManager URLForModel:bundleID:forAllSegments:]
+ -[_ANEModelCacheManager URLForModel:bundleID:forAllSegments:aotCacheUrlIdentifier:]
+ -[_ANEModelCacheManager URLForModel:bundleID:useSourceURL:]
+ -[_ANEModelCacheManager URLForModel:bundleID:useSourceURL:aotCacheUrlIdentifier:]
+ -[_ANEModelCacheManager URLForModel:bundleID:useSourceURL:forAllSegments:aotCacheUrlIdentifier:]
+ -[_ANEModelCacheManager URLForModel:bundleID:useSourceURL:forAllSegments:aotCacheUrlIdentifier:].cold.1
+ -[_ANEModelCacheManager URLForModel:bundleID:useSourceURL:forAllSegments:aotCacheUrlIdentifier:].cold.2
+ -[_ANEModelCacheManager cacheDir]
+ -[_ANEModelCacheManager cacheURLIdentifierForModel:useSourceURL:withReply:]
+ -[_ANEModelCacheManager cachedModelAllSegmentsPathFor:csIdentity:]
+ -[_ANEModelCacheManager cachedModelPathFor:csIdentity:]
+ -[_ANEModelCacheManager cachedModelPathFor:csIdentity:useSourceURL:]
+ -[_ANEModelCacheManager cachedModelRetainNameFor:csIdentity:]
+ -[_ANEModelCacheManager cachedSourceModelStoreNameFor:csIdentity:]
+ -[_ANEModelCacheManager filePathForModel:bundleID:]
+ -[_ANEModelCacheManager garbageCollectDanglingModels]
+ -[_ANEModelCacheManager getDiskSpaceForBundleID:]
+ -[_ANEModelCacheManager getDiskSpaceItemizedByBundleIDAndPurge:]
+ -[_ANEModelCacheManager getModelBinaryPathFromURLIdentifier:bundleID:]
+ -[_ANEModelCacheManager initWithURL:]
+ -[_ANEModelCacheManager initWithURL:createDirectory:]
+ -[_ANEModelCacheManager init]
+ -[_ANEModelCacheManager removeAllModelsForBundleID:]
+ -[_ANEModelCacheManager scanAllPartitionsForModel:csIdentity:expunge:]
+ -[_ANEModelCacheManager scheduleMaintenanceWithName:directoryPaths:]
+ -[_ANEModelCacheManager shouldEnforceSizeLimits]
+ -[_ANEModelCacheManager startDanglingModelGC]
+ -[_ANEModelCacheManager startDanglingModelGC].cold.1
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
+ -[_ANETask .cxx_destruct]
+ -[_ANETask executionCriteria]
+ -[_ANETask handler]
+ -[_ANETask initWithName:period:handler:]
+ -[_ANETask init]
+ -[_ANETask name]
+ -[_ANETask periodSeconds]
+ -[_ANETask queue]
+ /Library/Caches/com.apple.xbs/01273E70-6169-4366-936B-5D7E907FCA58/TemporaryDirectory.QWwnZm/Binaries/AppleNeuralEngine_CompilerService/install/TempContent/Objects/AppleNeuralEngine.build/ANECompilerService.build/DerivedSources/
+ /Library/Caches/com.apple.xbs/01273E70-6169-4366-936B-5D7E907FCA58/TemporaryDirectory.QWwnZm/Binaries/AppleNeuralEngine_CompilerService/install/TempContent/Objects/AppleNeuralEngine.build/ANECompilerService.build/Objects-normal/arm64e/ANECompilerService_vers.o
+ /Library/Caches/com.apple.xbs/01273E70-6169-4366-936B-5D7E907FCA58/TemporaryDirectory.QWwnZm/Binaries/AppleNeuralEngine_CompilerService/install/TempContent/Objects/AppleNeuralEngine.build/ANECompilerService.build/Objects-normal/arm64e/NSFileManager+ANE.o
+ /Library/Caches/com.apple.xbs/01273E70-6169-4366-936B-5D7E907FCA58/TemporaryDirectory.QWwnZm/Binaries/AppleNeuralEngine_CompilerService/install/TempContent/Objects/AppleNeuralEngine.build/ANECompilerService.build/Objects-normal/arm64e/_ANECVAIRCompiler.o
+ /Library/Caches/com.apple.xbs/01273E70-6169-4366-936B-5D7E907FCA58/TemporaryDirectory.QWwnZm/Binaries/AppleNeuralEngine_CompilerService/install/TempContent/Objects/AppleNeuralEngine.build/ANECompilerService.build/Objects-normal/arm64e/_ANECompiler.o
+ /Library/Caches/com.apple.xbs/01273E70-6169-4366-936B-5D7E907FCA58/TemporaryDirectory.QWwnZm/Binaries/AppleNeuralEngine_CompilerService/install/TempContent/Objects/AppleNeuralEngine.build/ANECompilerService.build/Objects-normal/arm64e/_ANECompilerService.o
+ /Library/Caches/com.apple.xbs/01273E70-6169-4366-936B-5D7E907FCA58/TemporaryDirectory.QWwnZm/Binaries/AppleNeuralEngine_CompilerService/install/TempContent/Objects/AppleNeuralEngine.build/ANECompilerService.build/Objects-normal/arm64e/_ANECoreMLModelCompiler.o
+ /Library/Caches/com.apple.xbs/01273E70-6169-4366-936B-5D7E907FCA58/TemporaryDirectory.QWwnZm/Binaries/AppleNeuralEngine_CompilerService/install/TempContent/Objects/AppleNeuralEngine.build/ANECompilerService.build/Objects-normal/arm64e/_ANEDebugUtils.o
+ /Library/Caches/com.apple.xbs/01273E70-6169-4366-936B-5D7E907FCA58/TemporaryDirectory.QWwnZm/Binaries/AppleNeuralEngine_CompilerService/install/TempContent/Objects/AppleNeuralEngine.build/ANECompilerService.build/Objects-normal/arm64e/_ANEEspressoIRTranslator.o
+ /Library/Caches/com.apple.xbs/01273E70-6169-4366-936B-5D7E907FCA58/TemporaryDirectory.QWwnZm/Binaries/AppleNeuralEngine_CompilerService/install/TempContent/Objects/AppleNeuralEngine.build/ANECompilerService.build/Objects-normal/arm64e/_ANEInMemoryModelCacheManager.o
+ /Library/Caches/com.apple.xbs/01273E70-6169-4366-936B-5D7E907FCA58/TemporaryDirectory.QWwnZm/Binaries/AppleNeuralEngine_CompilerService/install/TempContent/Objects/AppleNeuralEngine.build/ANECompilerService.build/Objects-normal/arm64e/_ANEMILCompiler.o
+ /Library/Caches/com.apple.xbs/01273E70-6169-4366-936B-5D7E907FCA58/TemporaryDirectory.QWwnZm/Binaries/AppleNeuralEngine_CompilerService/install/TempContent/Objects/AppleNeuralEngine.build/ANECompilerService.build/Objects-normal/arm64e/_ANEMLIRCompiler.o
+ /Library/Caches/com.apple.xbs/01273E70-6169-4366-936B-5D7E907FCA58/TemporaryDirectory.QWwnZm/Binaries/AppleNeuralEngine_CompilerService/install/TempContent/Objects/AppleNeuralEngine.build/ANECompilerService.build/Objects-normal/arm64e/_ANEModelCacheManager.o
+ /Library/Caches/com.apple.xbs/01273E70-6169-4366-936B-5D7E907FCA58/TemporaryDirectory.QWwnZm/Binaries/AppleNeuralEngine_CompilerService/install/TempContent/Objects/AppleNeuralEngine.build/ANECompilerService.build/Objects-normal/arm64e/_ANEOptionKeys.o
+ /Library/Caches/com.apple.xbs/01273E70-6169-4366-936B-5D7E907FCA58/TemporaryDirectory.QWwnZm/Binaries/AppleNeuralEngine_CompilerService/install/TempContent/Objects/AppleNeuralEngine.build/ANECompilerService.build/Objects-normal/arm64e/_ANEPatchManager.o
+ /Library/Caches/com.apple.xbs/01273E70-6169-4366-936B-5D7E907FCA58/TemporaryDirectory.QWwnZm/Binaries/AppleNeuralEngine_CompilerService/install/TempContent/Objects/AppleNeuralEngine.build/ANECompilerService.build/Objects-normal/arm64e/_ANESandboxingHelper.o
+ /Library/Caches/com.apple.xbs/01273E70-6169-4366-936B-5D7E907FCA58/TemporaryDirectory.QWwnZm/Binaries/AppleNeuralEngine_CompilerService/install/TempContent/Objects/AppleNeuralEngine.build/ANECompilerService.build/Objects-normal/arm64e/_ANEStorageHelper.o
+ /Library/Caches/com.apple.xbs/01273E70-6169-4366-936B-5D7E907FCA58/TemporaryDirectory.QWwnZm/Binaries/AppleNeuralEngine_CompilerService/install/TempContent/Objects/AppleNeuralEngine.build/ANECompilerService.build/Objects-normal/arm64e/_ANETask.o
+ /Library/Caches/com.apple.xbs/01273E70-6169-4366-936B-5D7E907FCA58/TemporaryDirectory.QWwnZm/Binaries/AppleNeuralEngine_CompilerService/install/TempContent/Objects/AppleNeuralEngine.build/ANECompilerService.build/Objects-normal/arm64e/main.o
+ /Library/Caches/com.apple.xbs/01273E70-6169-4366-936B-5D7E907FCA58/TemporaryDirectory.QWwnZm/Sources/AppleNeuralEngine_CompilerService/ANECompilerService/
+ /Library/Caches/com.apple.xbs/01273E70-6169-4366-936B-5D7E907FCA58/TemporaryDirectory.QWwnZm/Sources/AppleNeuralEngine_CompilerService/Common/
+ /Library/Caches/com.apple.xbs/01273E70-6169-4366-936B-5D7E907FCA58/TemporaryDirectory.QWwnZm/Sources/AppleNeuralEngine_CompilerService/aned/
+ ANECVAIRCompiler.m
+ ANECompiler.mm
+ ANECompilerService.m
+ ANECompilerService_vers.c
+ ANECoreMLModelCompiler.m
+ ANEDebugUtils.m
+ ANEEspressoIRTranslator.m
+ ANEInMemoryModelCacheManager.m
+ ANEMILCompiler.m
+ ANEMLIRCompiler.m
+ ANEModelCacheManager.m
+ ANEOptionKeys.m
+ ANEPatchManager.m
+ ANESandboxingHelper.m
+ ANEStorageHelper.m
+ ANETask.m
+ GCC_except_table0
+ GCC_except_table1
+ GCC_except_table10
+ GCC_except_table11
+ GCC_except_table12
+ GCC_except_table13
+ GCC_except_table14
+ GCC_except_table2
+ GCC_except_table3
+ GCC_except_table5
+ GCC_except_table6
+ GCC_except_table9
+ NSFileManager+ANE.m
+ OBJC_IVAR_$__ANEInMemoryModelCacheManager._cacheDir
+ OBJC_IVAR_$__ANEModelCacheManager._cacheDir
+ OBJC_IVAR_$__ANEPatchManager._dataVaultBaseURL
+ OBJC_IVAR_$__ANEPatchManager._serialQueue
+ OBJC_IVAR_$__ANETask._executionCriteria
+ OBJC_IVAR_$__ANETask._handler
+ OBJC_IVAR_$__ANETask._name
+ OBJC_IVAR_$__ANETask._periodSeconds
+ OBJC_IVAR_$__ANETask._queue
+ _APP_SANDBOX_READ_WRITE
+ _CC_SHA256
+ _NSCocoaErrorDomain
+ _NSTemporaryDirectory
+ _NSURLFileSizeKey
+ _OBJC_CLASS_$_NSCharacterSet
+ _OBJC_CLASS_$_NSMutableDictionary
+ _OBJC_CLASS_$_NSMutableString
+ _OBJC_CLASS_$_NSPropertyListSerialization
+ _OBJC_CLASS_$__ANEDebugUtils
+ _OBJC_CLASS_$__ANEPatchManager
+ _OBJC_METACLASS_$__ANEDebugUtils
+ _OBJC_METACLASS_$__ANEPatchManager
+ _OUTLINED_FUNCTION_0
+ _OUTLINED_FUNCTION_1
+ _OUTLINED_FUNCTION_10
+ _OUTLINED_FUNCTION_11
+ _OUTLINED_FUNCTION_12
+ _OUTLINED_FUNCTION_2
+ _OUTLINED_FUNCTION_3
+ _OUTLINED_FUNCTION_4
+ _OUTLINED_FUNCTION_5
+ _OUTLINED_FUNCTION_6
+ _OUTLINED_FUNCTION_7
+ _OUTLINED_FUNCTION_8
+ _OUTLINED_FUNCTION_9
+ __161-[_ANECompilerService compileModelAt:csIdentity:sandboxExtension:options:tempDirectory:cloneDirectory:outputURL:aotModelBinaryPath:maxModelMemorySize:withReply:]_block_invoke.cold.1
+ __161-[_ANECompilerService compileModelAt:csIdentity:sandboxExtension:options:tempDirectory:cloneDirectory:outputURL:aotModelBinaryPath:maxModelMemorySize:withReply:]_block_invoke.cold.2
+ __161-[_ANECompilerService compileModelAt:csIdentity:sandboxExtension:options:tempDirectory:cloneDirectory:outputURL:aotModelBinaryPath:maxModelMemorySize:withReply:]_block_invoke.cold.3
+ __161-[_ANECompilerService compileModelAt:csIdentity:sandboxExtension:options:tempDirectory:cloneDirectory:outputURL:aotModelBinaryPath:maxModelMemorySize:withReply:]_block_invoke.cold.4
+ __161-[_ANECompilerService compileModelAt:csIdentity:sandboxExtension:options:tempDirectory:cloneDirectory:outputURL:aotModelBinaryPath:maxModelMemorySize:withReply:]_block_invoke.cold.5
+ __161-[_ANECompilerService compileModelAt:csIdentity:sandboxExtension:options:tempDirectory:cloneDirectory:outputURL:aotModelBinaryPath:maxModelMemorySize:withReply:]_block_invoke.cold.6
+ __161-[_ANECompilerService compileModelAt:csIdentity:sandboxExtension:options:tempDirectory:cloneDirectory:outputURL:aotModelBinaryPath:maxModelMemorySize:withReply:]_block_invoke.cold.7
+ __43+[_ANEStorageHelper memoryMapWeightAtPath:]_block_invoke.7
+ __43+[_ANEStorageHelper memoryMapWeightAtPath:]_block_invoke.8
+ __45-[_ANEModelCacheManager startDanglingModelGC]_block_invoke.27
+ __45-[_ANEModelCacheManager startDanglingModelGC]_block_invoke.cold.1
+ __72+[_ANEStorageHelper memoryMapModelAtPath:isPrecompiled:modelAttributes:]_block_invoke.4
+ __72+[_ANEStorageHelper memoryMapModelAtPath:isPrecompiled:modelAttributes:]_block_invoke.6
+ __86-[_ANEPatchManager patchModelAtURL:toPatchedURL:withConfiguration:usingPatcher:error:]_block_invoke.cold.1
+ __OBJC_$_CATEGORY_CLASS_METHODS_NSFileManager_$_ANE
+ __OBJC_$_CATEGORY_NSFileManager_$_ANE
+ __OBJC_$_CLASS_METHODS__ANECVAIRCompiler
+ __OBJC_$_CLASS_METHODS__ANECompiler
+ __OBJC_$_CLASS_METHODS__ANECompilerService
+ __OBJC_$_CLASS_METHODS__ANECoreMLModelCompiler
+ __OBJC_$_CLASS_METHODS__ANEDebugUtils
+ __OBJC_$_CLASS_METHODS__ANEEspressoIRTranslator
+ __OBJC_$_CLASS_METHODS__ANEInMemoryModelCacheManager
+ __OBJC_$_CLASS_METHODS__ANEMILCompiler
+ __OBJC_$_CLASS_METHODS__ANEMLIRCompiler
+ __OBJC_$_CLASS_METHODS__ANEModelCacheManager
+ __OBJC_$_CLASS_METHODS__ANEPatchManager
+ __OBJC_$_CLASS_METHODS__ANESandboxingHelper
+ __OBJC_$_CLASS_METHODS__ANEStorageHelper
+ __OBJC_$_CLASS_METHODS__ANETask
+ __OBJC_$_CLASS_METHODS__ANETaskManager
+ __OBJC_$_INSTANCE_METHODS_ServiceDelegate
+ __OBJC_$_INSTANCE_METHODS__ANECompilerService
+ __OBJC_$_INSTANCE_METHODS__ANEInMemoryModelCacheManager
+ __OBJC_$_INSTANCE_METHODS__ANEModelCacheManager
+ __OBJC_$_INSTANCE_METHODS__ANEPatchManager
+ __OBJC_$_INSTANCE_METHODS__ANETask
+ __OBJC_$_INSTANCE_VARIABLES__ANEInMemoryModelCacheManager
+ __OBJC_$_INSTANCE_VARIABLES__ANEModelCacheManager
+ __OBJC_$_INSTANCE_VARIABLES__ANEPatchManager
+ __OBJC_$_INSTANCE_VARIABLES__ANETask
+ __OBJC_$_PROP_LIST_NSObject
+ __OBJC_$_PROP_LIST_ServiceDelegate
+ __OBJC_$_PROP_LIST__ANEInMemoryModelCacheManager
+ __OBJC_$_PROP_LIST__ANEModelCacheManager
+ __OBJC_$_PROP_LIST__ANEPatchManager
+ __OBJC_$_PROP_LIST__ANETask
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSXPCListenerDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS__ANECompilerServiceProtocol
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS__ANEMaintenanceProtocol
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS__ANEStorageMaintainerProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSXPCListenerDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES__ANECompilerServiceProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES__ANEMaintenanceProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES__ANEStorageMaintainerProtocol
+ __OBJC_$_PROTOCOL_REFS_NSXPCListenerDelegate
+ __OBJC_CLASS_PROTOCOLS_$_ServiceDelegate
+ __OBJC_CLASS_PROTOCOLS_$__ANECompilerService
+ __OBJC_CLASS_PROTOCOLS_$__ANEModelCacheManager
+ __OBJC_CLASS_RO_$_ServiceDelegate
+ __OBJC_CLASS_RO_$__ANECVAIRCompiler
+ __OBJC_CLASS_RO_$__ANECompiler
+ __OBJC_CLASS_RO_$__ANECompilerService
+ __OBJC_CLASS_RO_$__ANECoreMLModelCompiler
+ __OBJC_CLASS_RO_$__ANEDebugUtils
+ __OBJC_CLASS_RO_$__ANEEspressoIRTranslator
+ __OBJC_CLASS_RO_$__ANEInMemoryModelCacheManager
+ __OBJC_CLASS_RO_$__ANEMILCompiler
+ __OBJC_CLASS_RO_$__ANEMLIRCompiler
+ __OBJC_CLASS_RO_$__ANEModelCacheManager
+ __OBJC_CLASS_RO_$__ANEPatchManager
+ __OBJC_CLASS_RO_$__ANESandboxingHelper
+ __OBJC_CLASS_RO_$__ANEStorageHelper
+ __OBJC_CLASS_RO_$__ANETask
+ __OBJC_CLASS_RO_$__ANETaskManager
+ __OBJC_LABEL_PROTOCOL_$_NSObject
+ __OBJC_LABEL_PROTOCOL_$_NSXPCListenerDelegate
+ __OBJC_LABEL_PROTOCOL_$__ANECompilerServiceProtocol
+ __OBJC_LABEL_PROTOCOL_$__ANEMaintenanceProtocol
+ __OBJC_LABEL_PROTOCOL_$__ANEStorageMaintainerProtocol
+ __OBJC_METACLASS_RO_$_ServiceDelegate
+ __OBJC_METACLASS_RO_$__ANECVAIRCompiler
+ __OBJC_METACLASS_RO_$__ANECompiler
+ __OBJC_METACLASS_RO_$__ANECompilerService
+ __OBJC_METACLASS_RO_$__ANECoreMLModelCompiler
+ __OBJC_METACLASS_RO_$__ANEDebugUtils
+ __OBJC_METACLASS_RO_$__ANEEspressoIRTranslator
+ __OBJC_METACLASS_RO_$__ANEInMemoryModelCacheManager
+ __OBJC_METACLASS_RO_$__ANEMILCompiler
+ __OBJC_METACLASS_RO_$__ANEMLIRCompiler
+ __OBJC_METACLASS_RO_$__ANEModelCacheManager
+ __OBJC_METACLASS_RO_$__ANEPatchManager
+ __OBJC_METACLASS_RO_$__ANESandboxingHelper
+ __OBJC_METACLASS_RO_$__ANEStorageHelper
+ __OBJC_METACLASS_RO_$__ANETask
+ __OBJC_METACLASS_RO_$__ANETaskManager
+ __OBJC_PROTOCOL_$_NSObject
+ __OBJC_PROTOCOL_$_NSXPCListenerDelegate
+ __OBJC_PROTOCOL_$__ANECompilerServiceProtocol
+ __OBJC_PROTOCOL_$__ANEMaintenanceProtocol
+ __OBJC_PROTOCOL_$__ANEStorageMaintainerProtocol
+ __OBJC_PROTOCOL_REFERENCE_$__ANECompilerServiceProtocol
+ __OBJC_PROTOCOL_REFERENCE_$__ANEStorageMaintainerProtocol
+ __ZL7gLogger
+ __ZZ52+[_ANECompiler applyDebugOptions:toCompilerOptions:]E14anefToANECKeys
+ __ZZ52+[_ANECompiler applyDebugOptions:toCompilerOptions:]E9onceToken
+ ___161-[_ANECompilerService compileModelAt:csIdentity:sandboxExtension:options:tempDirectory:cloneDirectory:outputURL:aotModelBinaryPath:maxModelMemorySize:withReply:]_block_invoke
+ ___31+[_ANEStorageHelper initialize]_block_invoke
+ ___32+[_ANETaskManager registerTask:]_block_invoke
+ ___32+[_ANETaskManager registerTask:]_block_invoke_2
+ ___33+[_ANEPatchManager sharedManager]_block_invoke
+ ___35+[_ANEModelCacheManager initialize]_block_invoke
+ ___41+[_ANECompiler compileModelJIT:ok:error:]_block_invoke
+ ___41+[_ANEDebugUtils applyDebugEnvToOptions:]_block_invoke
+ ___43+[_ANEStorageHelper memoryMapWeightAtPath:]_block_invoke
+ ___45-[_ANEModelCacheManager startDanglingModelGC]_block_invoke
+ ___46+[_ANECompiler compileModel:options:ok:error:]_block_invoke
+ ___46+[_ANECompiler compileModel:options:ok:error:]_block_invoke_2
+ ___52+[_ANECompiler applyDebugOptions:toCompilerOptions:]_block_invoke
+ ___55-[_ANECompilerService updateSourcePathAt:to:withReply:]_block_invoke
+ ___56+[_ANEStorageHelper garbageCollectDanglingModelsAtPath:]_block_invoke
+ ___68-[_ANEModelCacheManager scheduleMaintenanceWithName:directoryPaths:]_block_invoke
+ ___70-[_ANEModelCacheManager scanAllPartitionsForModel:csIdentity:expunge:]_block_invoke
+ ___72+[_ANEStorageHelper memoryMapModelAtPath:isPrecompiled:modelAttributes:]_block_invoke
+ ___76-[_ANEInMemoryModelCacheManager scheduleMaintenanceWithName:directoryPaths:]_block_invoke
+ ___84-[_ANEPatchManager deletePatchedModelsInDirectory:forModelURL:onlyIfOrphaned:error:]_block_invoke
+ ___86-[_ANEPatchManager patchModelAtURL:toPatchedURL:withConfiguration:usingPatcher:error:]_block_invoke
+ ___96-[_ANEModelCacheManager URLForModel:bundleID:useSourceURL:forAllSegments:aotCacheUrlIdentifier:]_block_invoke
+ ___Block_byref_object_copy_
+ ___Block_byref_object_dispose_
+ ___block_descriptor_136_e8_32s40s48s56s64s72s80s88s96bs104r_e5_v8?0ls32l8s96l8s40l8s48l8r104l8s56l8s64l8s72l8s80l8s88l8
+ ___block_descriptor_192_e8_32r_e5_v8?0lr32l8
+ ___block_descriptor_32_e5_v8?0l
+ ___block_descriptor_40_e27_B24?0"NSURL"8"NSError"16l
+ ___block_descriptor_40_e5_v8?0l
+ ___block_descriptor_40_e8_32r_e5_v8?0lr32l8
+ ___block_descriptor_40_e8_32s_e33_v16?0"NSObject<OS_xpc_object>"8ls32l8
+ ___block_descriptor_40_e8_v12?0B8l
+ ___block_descriptor_48_e12_v24?0^v8Q16l
+ ___block_descriptor_48_e8_32r40r_e31_v24?0"NSString"8"NSString"16lr32l8r40l8
+ ___block_descriptor_48_e8_32s40s_e5_v8?0ls32l8s40l8
+ ___block_descriptor_48_e8_32s_e17_v16?0"NSError"8ls32l8
+ ___block_descriptor_48_ea8_32r40r_e28_v20?0i8^{__CFDictionary=}12lr32l8r40l8
+ ___block_descriptor_56_e8_32s40s48r_e5_v8?0ls32l8s40l8r48l8
+ ___block_descriptor_60_ea8_32r40r_e28_v20?0i8^{__CFDictionary=}12lr32l8r40l8
+ ___block_descriptor_64_e8_32s40s48bs_e5_v8?0ls32l8s40l8s48l8
+ ___block_descriptor_96_e8_32s40s48s56s64s72r80r_e5_v8?0ls32l8s40l8r72l8r80l8s48l8s56l8s64l8
+ ___block_literal_global
+ ___destructor_8_s0_s8_s16_s24_s32_s40_s48_s64_s72
+ __gAsyncIOq
+ __gLogger
+ _fclose
+ _fopen
+ _fwrite
+ _gANECompilerServiceQueue
+ _gLogger
+ _getenv
+ _kANEFAneInstanceHint
+ _kANEFDebugCaptureBytecodeKey
+ _kANEFDebugCaptureElideResourcesKey
+ _kANEFDebugCaptureFolderKey
+ _kANEFDebugCaptureFolderSandboxExtensionKey
+ _kANEFDebugCaptureIncludeLocationsKey
+ _kANEFDebugOptionsKey
+ _kANEFInMemoryModelIdentifierKey
+ _kANEFInMemoryModelIsCachedKey
+ _kANEFIntermediateBufferSizeHint
+ _kANEFIntermediateTensorDescriptorKey
+ _kANEFModelMutableWeightBufferInfoKey
+ _kANEFProcedureVariantHint
+ _kANEFTargetArchitectureKey
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$URLByAppendingPathComponent:
+ _objc_msgSend$URLByAppendingPathComponent:isDirectory:
+ _objc_msgSend$URLByAppendingPathExtension:
+ _objc_msgSend$URLByDeletingLastPathComponent
+ _objc_msgSend$URLByStandardizingPath
+ _objc_msgSend$URLForBundleID:
+ _objc_msgSend$URLForModel:bundleID:
+ _objc_msgSend$URLForModel:bundleID:forAllSegments:aotCacheUrlIdentifier:
+ _objc_msgSend$URLForModel:bundleID:useSourceURL:
+ _objc_msgSend$URLForModel:bundleID:useSourceURL:forAllSegments:aotCacheUrlIdentifier:
+ _objc_msgSend$URLForModelHash:bundleID:
+ _objc_msgSend$UTF8String
+ _objc_msgSend$_markPurgeablePath:error:
+ _objc_msgSend$_markPurgeablePath:withFlags:error:
+ _objc_msgSend$addEntriesFromDictionary:
+ _objc_msgSend$addObject:
+ _objc_msgSend$addSubdirectoryDetails:directoryPath:size:
+ _objc_msgSend$addValue:forScalarKey:
+ _objc_msgSend$allKeys
+ _objc_msgSend$aneSubType
+ _objc_msgSend$aneSubTypeAndVariant
+ _objc_msgSend$aneSubTypeProductVariant
+ _objc_msgSend$aneSubTypeVariant
+ _objc_msgSend$ane_addWriteModeIfMissing:originalMode:
+ _objc_msgSend$appendFormat:
+ _objc_msgSend$applyDebugOptions:toCompilerOptions:
+ _objc_msgSend$arrayWithObjects:count:
+ _objc_msgSend$attributesOfItemAtPath:error:
+ _objc_msgSend$boolValue
+ _objc_msgSend$buildSpecificModelDataVaultDirectory
+ _objc_msgSend$bytes
+ _objc_msgSend$cacheDir
+ _objc_msgSend$cacheURLIdentifierForModel:useSourceURL:withReply:
+ _objc_msgSend$cachedModelPathFor:csIdentity:useSourceURL:
+ _objc_msgSend$cachedModelRetainNameFor:
+ _objc_msgSend$cachedSourceModelStoreNameFor:
+ _objc_msgSend$canAccessPathAt:methodName:error:
+ _objc_msgSend$characterAtIndex:
+ _objc_msgSend$characterIsMember:
+ _objc_msgSend$characterSetWithCharactersInString:
+ _objc_msgSend$cloneIfWritable:isEncryptedModel:cloneDirectory:
+ _objc_msgSend$code
+ _objc_msgSend$common
+ _objc_msgSend$compare:
+ _objc_msgSend$compileModel:options:ok:error:
+ _objc_msgSend$compileModelAt:csIdentity:key:optionsFilename:tempDirectory:outputURL:saveSourceModelPath:aotModelBinaryPath:isEncryptedModel:options:ok:error:
+ _objc_msgSend$compileModelAt:csIdentity:plistFilename:optionsFilename:outputURL:saveSourceURL:aotModelBinaryPath:isEncryptedModel:options:ok:error:
+ _objc_msgSend$compileModelAt:modelName:csIdentity:optionsFilename:outputURL:saveSourceURL:aotModelBinaryPath:isEncryptedModel:options:maxModelMemorySize:ok:error:
+ _objc_msgSend$compileModelAt:modelName:csIdentity:optionsFilename:outputURL:saveSourceURL:aotModelBinaryPath:isEncryptedModel:options:mpsConstants:externConstants:maxModelMemorySize:ok:error:
+ _objc_msgSend$compileModelJIT:ok:error:
+ _objc_msgSend$compiler
+ _objc_msgSend$compilerServiceAccessEntitlement
+ _objc_msgSend$componentsSeparatedByString:
+ _objc_msgSend$configurationIdentifierForConfiguration:
+ _objc_msgSend$consumeSandboxExtension:forModel:error:
+ _objc_msgSend$consumeSandboxExtension:forPath:error:
+ _objc_msgSend$containsString:
+ _objc_msgSend$copy
+ _objc_msgSend$count
+ _objc_msgSend$countByEnumeratingWithState:objects:count:
+ _objc_msgSend$createDirectoryAtPath:withIntermediateDirectories:attributes:error:
+ _objc_msgSend$createDirectoryForPatchedURL:error:
+ _objc_msgSend$createErrorForPlan:status:
+ _objc_msgSend$createErrorWithString:
+ _objc_msgSend$createErrorWithUnderlyingError:
+ _objc_msgSend$createExternConstants:
+ _objc_msgSend$createFileAtPath:contents:attributes:
+ _objc_msgSend$createInMemoryConstants:
+ _objc_msgSend$createJITNetworkFromModelAtPath:modelFilename:aotModelAtPath:aotModelFilename:
+ _objc_msgSend$createModelCacheDictionary
+ _objc_msgSend$createModelCacheRetain:
+ _objc_msgSend$createNetworkFromModelAtPath:modelFilename:
+ _objc_msgSend$currentConnection
+ _objc_msgSend$currentDirectoryPath
+ _objc_msgSend$daemon
+ _objc_msgSend$dataVaultBaseURL
+ _objc_msgSend$dataWithBytesNoCopy:length:freeWhenDone:
+ _objc_msgSend$dataWithContentsOfURL:options:error:
+ _objc_msgSend$dataWithPropertyList:format:options:error:
+ _objc_msgSend$date
+ _objc_msgSend$dateWithTimeIntervalSince1970:
+ _objc_msgSend$dateWithTimeIntervalSinceNow:
+ _objc_msgSend$defaultANECIRFileName
+ _objc_msgSend$defaultCompilerOptionsFilename
+ _objc_msgSend$defaultLLIRBundleName
+ _objc_msgSend$defaultMILFileName
+ _objc_msgSend$defaultMLIRFileName
+ _objc_msgSend$defaultManager
+ _objc_msgSend$defaultPatchFromURL:toDestination:withConfiguration:error:
+ _objc_msgSend$deletePatchedModelsInDirectory:forModelURL:onlyIfOrphaned:error:
+ _objc_msgSend$destroyEspresso:ctx:
+ _objc_msgSend$dictionary
+ _objc_msgSend$dictionaryWithContentsOfURL:error:
+ _objc_msgSend$dictionaryWithObjects:forKeys:count:
+ _objc_msgSend$enableApfsPurging
+ _objc_msgSend$enumeratorAtPath:
+ _objc_msgSend$enumeratorAtURL:includingPropertiesForKeys:options:errorHandler:
+ _objc_msgSend$errorDomainCompiler
+ _objc_msgSend$errorDomainEspresso
+ _objc_msgSend$errorWithDomain:code:userInfo:
+ _objc_msgSend$executionCriteria
+ _objc_msgSend$externConstants
+ _objc_msgSend$fileAccessErrorForMethod:
+ _objc_msgSend$fileAttributes
+ _objc_msgSend$fileExistsAtPath:
+ _objc_msgSend$fileExistsAtPath:isDirectory:
+ _objc_msgSend$fileSize
+ _objc_msgSend$fileSystemRepresentation
+ _objc_msgSend$fileURLWithPath:
+ _objc_msgSend$fileURLWithPath:isDirectory:
+ _objc_msgSend$firstObject
+ _objc_msgSend$framework
+ _objc_msgSend$garbageCollectDanglingModelsAtPath:
+ _objc_msgSend$garbageCollectOrphanedPatchedModelsAtPath:error:
+ _objc_msgSend$getAccessTimeForFilePath:
+ _objc_msgSend$getCacheURLIdentifier
+ _objc_msgSend$getResourceValue:forKey:error:
+ _objc_msgSend$handler
+ _objc_msgSend$hasDirectoryPath
+ _objc_msgSend$hasPrefix:
+ _objc_msgSend$hasSuffix:
+ _objc_msgSend$hexStringForString:
+ _objc_msgSend$identifierSource
+ _objc_msgSend$initPrivate
+ _objc_msgSend$initWithBytesNoCopy:length:deallocator:
+ _objc_msgSend$initWithName:period:handler:
+ _objc_msgSend$initWithServiceName:
+ _objc_msgSend$initWithURL:createDirectory:
+ _objc_msgSend$intValue
+ _objc_msgSend$interfaceWithProtocol:
+ _objc_msgSend$internalLibraryPath
+ _objc_msgSend$invalidate
+ _objc_msgSend$ioSurface
+ _objc_msgSend$isAbsolutePath
+ _objc_msgSend$isEqualToString:
+ _objc_msgSend$isInternalBuild
+ _objc_msgSend$isPatchedURL:
+ _objc_msgSend$isSystemModelPath:
+ _objc_msgSend$isURLInDataVault:
+ _objc_msgSend$issueSandboxExtensionForPath:error:
+ _objc_msgSend$key
+ _objc_msgSend$lastPathComponent
+ _objc_msgSend$length
+ _objc_msgSend$llirBundleExtension
+ _objc_msgSend$localizedDescription
+ _objc_msgSend$markPathAndDirectParentPurgeable:error:
+ _objc_msgSend$memoryMapModelAtPath:isPrecompiled:modelAttributes:
+ _objc_msgSend$metadataURLForPatchedURL:
+ _objc_msgSend$mlirExtension
+ _objc_msgSend$modelAssetsCacheName
+ _objc_msgSend$modelBinaryName
+ _objc_msgSend$modelCacheRetainName
+ _objc_msgSend$modelSourceStoreName
+ _objc_msgSend$modelURL
+ _objc_msgSend$modelURLForPatchedURL:
+ _objc_msgSend$moveItemAtPath:toPath:error:
+ _objc_msgSend$mpsConstants
+ _objc_msgSend$mutableCopy
+ _objc_msgSend$name
+ _objc_msgSend$nextObject
+ _objc_msgSend$noSandboxExtension
+ _objc_msgSend$notRecentlyUsedSecondsThreshold
+ _objc_msgSend$numberWithBool:
+ _objc_msgSend$numberWithDouble:
+ _objc_msgSend$numberWithInteger:
+ _objc_msgSend$numberWithUnsignedInteger:
+ _objc_msgSend$numberWithUnsignedLongLong:
+ _objc_msgSend$objectAtIndex:
+ _objc_msgSend$objectForKey:
+ _objc_msgSend$objectForKeyedSubscript:
+ _objc_msgSend$parentHashForModelURL:
+ _objc_msgSend$parseDebugEnvVar
+ _objc_msgSend$parseDebugString:
+ _objc_msgSend$patchModelAtURL:toPatchedURL:withConfiguration:usingPatcher:error:
+ _objc_msgSend$patchModelFromURL:toDestination:withConfiguration:error:
+ _objc_msgSend$patchedModelsDirectoryForModelURL:csIdentity:
+ _objc_msgSend$patchedURLForModelURL:csIdentity:configuration:
+ _objc_msgSend$path
+ _objc_msgSend$pathComponents
+ _objc_msgSend$pathExtension
+ _objc_msgSend$pathsForModelURL:
+ _objc_msgSend$perfStatsMask
+ _objc_msgSend$processIdentifier
+ _objc_msgSend$processModelShareAccessEntitlement
+ _objc_msgSend$purgeDanglingModelsAt:withReply:
+ _objc_msgSend$queue
+ _objc_msgSend$rangeOfString:
+ _objc_msgSend$registerTask:
+ _objc_msgSend$releaseSandboxExtension:handle:
+ _objc_msgSend$removeDirectoryAtPath:
+ _objc_msgSend$removeFilePath:ifDate:olderThanSecond:
+ _objc_msgSend$removeFilesFromDirectory:notAccessedInSeconds:
+ _objc_msgSend$removeItemAtPath:error:
+ _objc_msgSend$removeItemAtURL:error:
+ _objc_msgSend$removeObjectForKey:
+ _objc_msgSend$removeStaleModels
+ _objc_msgSend$removeStaleModelsAtPath:
+ _objc_msgSend$replaceCharactersInRange:withString:
+ _objc_msgSend$reportTelemetryToPPS:playload:
+ _objc_msgSend$resume
+ _objc_msgSend$sandboxExtensionPathForModelURL:
+ _objc_msgSend$sanitizedOriginalName:
+ _objc_msgSend$saveModelURLForPatchedURL:modelURL:configuration:
+ _objc_msgSend$saveSourceModelPath:outputModelDirectory:
+ _objc_msgSend$serviceListener
+ _objc_msgSend$set
+ _objc_msgSend$setAccessTime:forModelFilePath:
+ _objc_msgSend$setAttributes:ofItemAtPath:error:
+ _objc_msgSend$setByAddingObjectsFromArray:
+ _objc_msgSend$setDelegate:
+ _objc_msgSend$setExportedInterface:
+ _objc_msgSend$setExportedObject:
+ _objc_msgSend$setObject:forKey:
+ _objc_msgSend$setObject:forKeyedSubscript:
+ _objc_msgSend$setRemoteObjectInterface:
+ _objc_msgSend$setWithArray:
+ _objc_msgSend$sharedManager
+ _objc_msgSend$sizeOfDirectoryAtPath:recursionLevel:
+ _objc_msgSend$sizeOfModelCacheAtPath:purgeSubdirectories:
+ _objc_msgSend$sourceURL
+ _objc_msgSend$startDanglingModelGC
+ _objc_msgSend$stringByAppendingPathComponent:
+ _objc_msgSend$stringByAppendingString:
+ _objc_msgSend$stringByDeletingLastPathComponent
+ _objc_msgSend$stringByDeletingPathExtension
+ _objc_msgSend$stringByReplacingOccurrencesOfString:withString:
+ _objc_msgSend$stringByTrimmingCharactersInSet:
+ _objc_msgSend$stringValue
+ _objc_msgSend$stringWithCapacity:
+ _objc_msgSend$stringWithContentsOfURL:encoding:error:
+ _objc_msgSend$stringWithFormat:
+ _objc_msgSend$stringWithString:
+ _objc_msgSend$stringWithUTF8String:
+ _objc_msgSend$string_id
+ _objc_msgSend$subpathsOfDirectoryAtPath:error:
+ _objc_msgSend$substringFromIndex:
+ _objc_msgSend$substringToIndex:
+ _objc_msgSend$substringWithRange:
+ _objc_msgSend$synchronousRemoteObjectProxyWithErrorHandler:
+ _objc_msgSend$systemLibraryPath
+ _objc_msgSend$systemModelsCacheDirectory
+ _objc_msgSend$taskWithName:period:handler:
+ _objc_msgSend$timeIntervalSince1970
+ _objc_msgSend$timeIntervalSinceDate:
+ _objc_msgSend$translateModelAt:key:outputPath:isEncryptedModel:translationOptions:error:
+ _objc_msgSend$trimmedModelPath:trimmedPathOut:
+ _objc_msgSend$uniqueFirstLevelSubdirectories:
+ _objc_msgSend$unsignedIntegerValue
+ _objc_msgSend$unsignedLongLongValue
+ _objc_msgSend$unsignedShortValue
+ _objc_msgSend$updateAccessTimeForFilePath:
+ _objc_msgSend$valueForEntitlement:
+ _objc_msgSend$whitespaceCharacterSet
+ _objc_msgSend$writeToFile:atomically:encoding:error:
+ _objc_retain
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x4
+ _objc_retain_x5
+ _strlen
+ applyDebugEnvToOptions:.knownBoolKeys
+ applyDebugEnvToOptions:.onceToken
+ initialize.onceToken
+ main.cold.1
+ main.m
+ sharedManager.onceToken
+ sharedManager.shared
- _objc_retainAutoreleasedReturnValue
- radr://5614542
CStrings:
+ "\""
+ "%02x"
+ "%@: ANE_DEBUG=%@"
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
+ "%@: Using externConstants"
+ "%@: Using mpsConstants"
+ "%@: Warning: fclose returned %d"
+ "%@: bundleID rejected (nil, path separator, or traversal): %@"
+ "%@: compilerRequest externConstants=%@"
+ "%@: compilerRequest fields - modelFilename=%@ inputModelPath=%@ optionsFilePath=%@ outputFilename=%@ outputModelPath=%@ aotModelBinaryPath=%@ sourceModelPath=%@ isJITModel=%d isEncryptedModel=%d isMILModel=%d mpsConstants=%@ maxModelMemorySize=0x%llx"
+ "%@: error getting attributes for file (%@): %@"
+ "%@: error getting size for file (%@): %@"
+ "%@: failed to issue write sandbox extension for capture folder: %@"
+ "%@: failed to resolve CWD for relative capture_folder path; skipping capture_folder"
+ "%@: model(%@) using client-supplied targetArchitecture=%@"
+ "%@: nil filename"
+ "%@: nil modelURL"
+ "%@: nil parentHash for modelURL=%@"
+ "%@: nil sanitizedOriginalName for modelURL=%@"
+ "%@: path does not exist (%@)"
+ "%@_patched.hwx"
+ "%@_patched_%@.hwx"
+ "%s: extra debug compiler options: %@"
+ "%s: failed to create capture directory %@: %@"
+ "%s: kANECCaptureFolder=%@"
+ "'"
+ "(null)"
+ "+[_ANECompiler applyDebugOptions:toCompilerOptions:]"
+ ".."
+ "0"
+ ";"
+ "="
+ "@124@0:8@16@24@32@40@48@56@64B72@76@84@92Q100^B108^@116"
+ "@40@0:8^{?=@@@@@@@BBB@@Q}16^B24^@32"
+ "@48@0:8^{?=@@@@@@@BBB@@Q}16@24^B32^@40"
+ "@56@0:8@16@24@32@40^@48"
+ "ANEFModelMutableWeightBufferInfo"
+ "ANE_DEBUG"
+ "Alignment"
+ "B40@0:8@16@24@32"
+ "B40@0:8@16Q24^@32"
+ "B44@0:8@16@24B32^@36"
+ "B48@0:8@16@24@32^@40"
+ "B56@0:8@16@24@32@40^@48"
+ "CaptureBytecode"
+ "CaptureElideResources"
+ "CaptureFolder"
+ "CaptureIncludeLocations"
+ "DataRef"
+ "ExternConstants"
+ "Failed to get alignment for key: %@ from extern constants dict"
+ "Failed to get surface for key: %@ from extern constants dict"
+ "Failed to open destination file for writing: %s"
+ "Failed to save metadata for patched model"
+ "FileConstants"
+ "InMemoryConstants"
+ "Offset"
+ "Patched_%@"
+ "Q24@0:8@16"
+ "Size mismatch: wrote %zu bytes, expected %lu bytes"
+ "T@\"NSURL\",R,N,V_dataVaultBaseURL"
+ "URLByAppendingPathExtension:"
+ "_ANEDebugUtils"
+ "_ANEPatchManager"
+ "_dataVaultBaseURL"
+ "_markPurgeablePath:withFlags:error:"
+ "_serialQueue"
+ "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_"
+ "appendFormat:"
+ "applyDebugEnvToOptions:"
+ "applyDebugOptions:toCompilerOptions:"
+ "buildSpecificModelDataVaultDirectory"
+ "capture_bytecode"
+ "capture_elide_resources"
+ "capture_folder"
+ "capture_include_locations"
+ "characterAtIndex:"
+ "characterIsMember:"
+ "characterSetWithCharactersInString:"
+ "code"
+ "com.apple.ane.patcher"
+ "com.apple.ane.patching"
+ "compileModelAt:modelName:csIdentity:optionsFilename:outputURL:saveSourceURL:aotModelBinaryPath:isEncryptedModel:options:mpsConstants:externConstants:maxModelMemorySize:ok:error:"
+ "componentsSeparatedByString:"
+ "configurationIdentifierForConfiguration:"
+ "consumeSandboxExtension(captureFolder) failed: %@"
+ "count"
+ "createDirectoryForPatchedURL:error:"
+ "createExternConstants:"
+ "currentDirectoryPath"
+ "dataVaultBaseURL"
+ "dataWithContentsOfURL:options:error:"
+ "dataWithPropertyList:format:options:error:"
+ "defaultPatchFromURL:toDestination:withConfiguration:error:"
+ "deletePatchedModelsInDirectory:forModelURL:onlyIfOrphaned:error:"
+ "dictionary"
+ "dictionaryWithContentsOfURL:error:"
+ "externConstants"
+ "false"
+ "fileURLWithPath:isDirectory:"
+ "framework"
+ "garbageCollectOrphanedPatchedModelsAtPath:error:"
+ "getResourceValue:forKey:error:"
+ "in"
+ "initPrivate"
+ "isAbsolutePath"
+ "isPatchedURL:"
+ "isURLInDataVault:"
+ "kANEFAneInstanceHint"
+ "kANEFDebugCaptureBytecodeKey"
+ "kANEFDebugCaptureElideResourcesKey"
+ "kANEFDebugCaptureFolderKey"
+ "kANEFDebugCaptureFolderSandboxExtensionKey"
+ "kANEFDebugCaptureIncludeLocationsKey"
+ "kANEFDebugOptionsKey"
+ "kANEFInMemoryModelIsCachedKey"
+ "kANEFIntermediateBufferSizeHint"
+ "kANEFIntermediateTensorDescriptorKey"
+ "kANEFIsInMemoryModelTypeKey"
+ "kANEFProcedureVariantHint"
+ "kANEFTargetArchitectureKey"
+ "localizedDescription"
+ "metadataURLForPatchedURL:"
+ "modelAssetsCacheName"
+ "modelURLForPatchedURL:"
+ "outside"
+ "parentHashForModelURL:"
+ "parseDebugEnvVar"
+ "parseDebugString:"
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
+ "rangeOfString:"
+ "releaseSandboxExtension(captureFolder):(%@) handle:(%lld) failed (%d)"
+ "removeObjectForKey:"
+ "replaceCharactersInRange:withString:"
+ "sanitizedOriginalName:"
+ "saveModelURLForPatchedURL:modelURL:configuration:"
+ "sharedManager"
+ "sizeOfDirectoryOrFileAtPath:"
+ "stringByAppendingString:"
+ "stringByDeletingPathExtension"
+ "stringByTrimmingCharactersInSet:"
+ "stringValue"
+ "stringWithCapacity:"
+ "stringWithString:"
+ "substringFromIndex:"
+ "substringToIndex:"
+ "substringWithRange:"
+ "trimmedModelPath:trimmedPathOut:"
+ "updatePurgeabilityForPath:to:error:"
+ "updateSourcePathAt:to:withReply:"
+ "v40@0:8@\"NSString\"16@\"NSString\"24@?<v@?B@\"NSError\">32"
+ "v40@0:8@16@24@?32"
+ "wb"
+ "whitespaceCharacterSet"
- "@116@0:8@16@24@32@40@48@56@64B72@76@84Q92^B100^@108"
- "@40@0:8^{?=@@@@@@@BBB@Q}16^B24^@32"
- "@48@0:8^{?=@@@@@@@BBB@Q}16@24^B32^@40"
- "compileModelAt:modelName:csIdentity:optionsFilename:outputURL:saveSourceURL:aotModelBinaryPath:isEncryptedModel:options:mpsConstants:maxModelMemorySize:ok:error:"
- "trimmedModelPath:trimmedPath:"

```
