## ParavirtualizedANE

> `/System/Library/PrivateFrameworks/ParavirtualizedANE.framework/ParavirtualizedANE`

```diff

-370.56.0.0.0
-  __TEXT.__text: 0x132f8
-  __TEXT.__auth_stubs: 0x5a0
-  __TEXT.__objc_methlist: 0x53c
-  __TEXT.__const: 0x198
-  __TEXT.__cstring: 0xc25
-  __TEXT.__oslogstring: 0x35f8
-  __TEXT.__gcc_except_tab: 0x2640
-  __TEXT.__unwind_info: 0x4e0
+380.7.0.0.0
+  __TEXT.__text: 0x1a180
+  __TEXT.__auth_stubs: 0x5e0
+  __TEXT.__objc_methlist: 0x638
+  __TEXT.__const: 0x190
+  __TEXT.__cstring: 0xe00
+  __TEXT.__oslogstring: 0x4e5f
+  __TEXT.__gcc_except_tab: 0x36e0
+  __TEXT.__unwind_info: 0x5c8
   __TEXT.__objc_classname: 0x2f
-  __TEXT.__objc_methname: 0x16d2
-  __TEXT.__objc_methtype: 0x7ab
-  __TEXT.__objc_stubs: 0x17c0
-  __DATA_CONST.__got: 0x140
+  __TEXT.__objc_methname: 0x1eb7
+  __TEXT.__objc_methtype: 0x902
+  __TEXT.__objc_stubs: 0x1f20
+  __DATA_CONST.__got: 0x170
   __DATA_CONST.__const: 0x50
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x690
+  __DATA_CONST.__objc_selrefs: 0x868
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0x2e0
+  __AUTH_CONST.__auth_got: 0x300
   __AUTH_CONST.__const: 0x50
-  __AUTH_CONST.__cfstring: 0xc80
-  __AUTH_CONST.__objc_const: 0x320
+  __AUTH_CONST.__cfstring: 0xfc0
+  __AUTH_CONST.__objc_const: 0x380
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH.__objc_data: 0xa0
-  __DATA.__objc_ivar: 0x28
+  __DATA.__objc_ivar: 0x30
   __DATA.__data: 0x10
   __DATA.__bss: 0x20
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F8F331B5-7C62-366C-B820-F8336E5CD38C
-  Functions: 321
-  Symbols:   1114
-  CStrings:  719
+  UUID: 4D41AD7F-14DA-35CC-B29A-D8765AD3CDAE
+  Functions: 429
+  Symbols:   1418
+  CStrings:  953
 
Symbols:
+ +[_ANEVirtualModel objectWithModel:tmpModelFilesPath:tmpWeightFilesPath:]
+ +[_ANEVirtualPlatformClient generateExpectedBaseDirectoryWith:withCSIdentity:withVMID:fileSubDirectory:]
+ +[_ANEVirtualPlatformClient generateExpectedPathForFileName:withANEBaseDirectory:withCSIdentity:withVMID:fileSubDirectory:]
+ +[_ANEVirtualPlatformClient getDataFromIOSurface:withSize:]
+ +[_ANEVirtualPlatformClient getDataFromIOSurface:withSize:].cold.1
+ +[_ANEVirtualPlatformClient getDataFromIOSurface:withSize:].cold.2
+ +[_ANEVirtualPlatformClient getDataFromIOSurface:withSize:].cold.3
+ -[_ANEVirtualModel initWithModel:tmpModelFilesPath:tmpWeightFilesPath:]
+ -[_ANEVirtualModel initWithModel:tmpModelFilesPath:tmpWeightFilesPath:].cold.1
+ -[_ANEVirtualModel setTmpModelFilesPath:]
+ -[_ANEVirtualModel setTmpWeightFilesPath:]
+ -[_ANEVirtualModel tmpModelFilesPath]
+ -[_ANEVirtualModel tmpWeightFilesPath]
+ -[_ANEVirtualModel updateTmpWeightFilesPath:]
+ -[_ANEVirtualPlatformClient chunkedDataReceived:]
+ -[_ANEVirtualPlatformClient chunkedDataReceived:].cold.1
+ -[_ANEVirtualPlatformClient chunkedDataReceived:].cold.2
+ -[_ANEVirtualPlatformClient chunkedDataReceived:].cold.3
+ -[_ANEVirtualPlatformClient chunkedDataReceived:].cold.4
+ -[_ANEVirtualPlatformClient chunkedDataReceived:].cold.5
+ -[_ANEVirtualPlatformClient chunkedDataReceived:].cold.6
+ -[_ANEVirtualPlatformClient chunkedDataReceived:].cold.7
+ -[_ANEVirtualPlatformClient chunkedDataReceived:].cold.8
+ -[_ANEVirtualPlatformClient chunkedDataReceived:].cold.9
+ -[_ANEVirtualPlatformClient compileModelDictionary:].cold.4
+ -[_ANEVirtualPlatformClient constructANEModel:modelDirectory:].cold.6
+ -[_ANEVirtualPlatformClient copyDictionaryUsingJSONSerialization:toIOSurfaceWithID:withMaxSize:outWrittentDataSize:]
+ -[_ANEVirtualPlatformClient copyDictionaryUsingJSONSerialization:toIOSurfaceWithID:withMaxSize:outWrittentDataSize:].cold.1
+ -[_ANEVirtualPlatformClient copyDictionaryUsingJSONSerialization:toIOSurfaceWithID:withMaxSize:outWrittentDataSize:].cold.2
+ -[_ANEVirtualPlatformClient copyDictionaryUsingJSONSerialization:toIOSurfaceWithID:withMaxSize:outWrittentDataSize:].cold.3
+ -[_ANEVirtualPlatformClient copyDictionaryUsingJSONSerialization:toIOSurfaceWithID:withMaxSize:outWrittentDataSize:].cold.4
+ -[_ANEVirtualPlatformClient copyDictionaryUsingJSONSerialization:toIOSurfaceWithID:withMaxSize:outWrittentDataSize:].cold.5
+ -[_ANEVirtualPlatformClient copyDictionaryUsingJSONSerialization:toIOSurfaceWithID:withMaxSize:outWrittentDataSize:].cold.6
+ -[_ANEVirtualPlatformClient createANEModelInstanceParameters:modelUUID:].cold.2
+ -[_ANEVirtualPlatformClient createAllModelFilesOnHost:].cold.12
+ -[_ANEVirtualPlatformClient createLLIRBundleOnDiskFromIOSurfaceWithID:destDirectory:llirDataSize:]
+ -[_ANEVirtualPlatformClient createLLIRBundleOnDiskFromIOSurfaceWithID:destDirectory:llirDataSize:].cold.1
+ -[_ANEVirtualPlatformClient createLLIRBundleOnDiskFromIOSurfaceWithID:destDirectory:llirDataSize:].cold.10
+ -[_ANEVirtualPlatformClient createLLIRBundleOnDiskFromIOSurfaceWithID:destDirectory:llirDataSize:].cold.11
+ -[_ANEVirtualPlatformClient createLLIRBundleOnDiskFromIOSurfaceWithID:destDirectory:llirDataSize:].cold.12
+ -[_ANEVirtualPlatformClient createLLIRBundleOnDiskFromIOSurfaceWithID:destDirectory:llirDataSize:].cold.13
+ -[_ANEVirtualPlatformClient createLLIRBundleOnDiskFromIOSurfaceWithID:destDirectory:llirDataSize:].cold.14
+ -[_ANEVirtualPlatformClient createLLIRBundleOnDiskFromIOSurfaceWithID:destDirectory:llirDataSize:].cold.15
+ -[_ANEVirtualPlatformClient createLLIRBundleOnDiskFromIOSurfaceWithID:destDirectory:llirDataSize:].cold.2
+ -[_ANEVirtualPlatformClient createLLIRBundleOnDiskFromIOSurfaceWithID:destDirectory:llirDataSize:].cold.3
+ -[_ANEVirtualPlatformClient createLLIRBundleOnDiskFromIOSurfaceWithID:destDirectory:llirDataSize:].cold.4
+ -[_ANEVirtualPlatformClient createLLIRBundleOnDiskFromIOSurfaceWithID:destDirectory:llirDataSize:].cold.5
+ -[_ANEVirtualPlatformClient createLLIRBundleOnDiskFromIOSurfaceWithID:destDirectory:llirDataSize:].cold.6
+ -[_ANEVirtualPlatformClient createLLIRBundleOnDiskFromIOSurfaceWithID:destDirectory:llirDataSize:].cold.7
+ -[_ANEVirtualPlatformClient createLLIRBundleOnDiskFromIOSurfaceWithID:destDirectory:llirDataSize:].cold.8
+ -[_ANEVirtualPlatformClient createLLIRBundleOnDiskFromIOSurfaceWithID:destDirectory:llirDataSize:].cold.9
+ -[_ANEVirtualPlatformClient createModelFileAtPath:fromIOSID:withDataLength:shouldAppend:]
+ -[_ANEVirtualPlatformClient createModelFileAtPath:fromIOSID:withDataLength:shouldAppend:].cold.1
+ -[_ANEVirtualPlatformClient createModelFileAtPath:fromIOSID:withDataLength:shouldAppend:].cold.2
+ -[_ANEVirtualPlatformClient createModelFileAtPath:fromIOSID:withDataLength:shouldAppend:].cold.3
+ -[_ANEVirtualPlatformClient createModelFileAtPath:fromIOSID:withDataLength:shouldAppend:].cold.4
+ -[_ANEVirtualPlatformClient createModelFileAtPath:fromIOSID:withDataLength:shouldAppend:].cold.5
+ -[_ANEVirtualPlatformClient createModelFileAtPath:fromIOSID:withDataLength:shouldAppend:].cold.6
+ -[_ANEVirtualPlatformClient createModelFileAtPath:fromIOSID:withDataLength:shouldAppend:].cold.7
+ -[_ANEVirtualPlatformClient doCreateModelFile:aneModelKey:].cold.19
+ -[_ANEVirtualPlatformClient echo:].cold.1
+ -[_ANEVirtualPlatformClient evaluateWithModelDictionary:].cold.6
+ -[_ANEVirtualPlatformClient evaluateWithModelDictionary:].cold.7
+ -[_ANEVirtualPlatformClient evaluateWithModelDictionary:].cold.8
+ -[_ANEVirtualPlatformClient generateExpectedModelFilePathFromDictionary:error:]
+ -[_ANEVirtualPlatformClient generateExpectedModelFilePathFromDictionary:withFileType:error:]
+ -[_ANEVirtualPlatformClient generateExpectedPathForFileName:withFileType:withInputDictionary:]
+ -[_ANEVirtualPlatformClient generatedExpectedBaseDirectoryWithFileType:withInputDictionary:]
+ -[_ANEVirtualPlatformClient generatedExpectedBaseDirectoryWithFileType:withInputDictionary:].cold.1
+ -[_ANEVirtualPlatformClient generatedExpectedBaseDirectoryWithFileType:withInputDictionary:].cold.2
+ -[_ANEVirtualPlatformClient generatedExpectedBaseDirectoryWithFileType:withInputDictionary:].cold.3
+ -[_ANEVirtualPlatformClient generatedExpectedBaseDirectoryWithFileType:withInputDictionary:].cold.4
+ -[_ANEVirtualPlatformClient generatedExpectedBaseDirectoryWithFileType:withInputDictionary:].cold.5
+ -[_ANEVirtualPlatformClient generatedExpectedBaseDirectoryWithFileType:withInputDictionary:].cold.6
+ -[_ANEVirtualPlatformClient loadModelNewInstance:]
+ -[_ANEVirtualPlatformClient loadModelNewInstance:].cold.1
+ -[_ANEVirtualPlatformClient loadModelNewInstance:].cold.10
+ -[_ANEVirtualPlatformClient loadModelNewInstance:].cold.11
+ -[_ANEVirtualPlatformClient loadModelNewInstance:].cold.12
+ -[_ANEVirtualPlatformClient loadModelNewInstance:].cold.13
+ -[_ANEVirtualPlatformClient loadModelNewInstance:].cold.14
+ -[_ANEVirtualPlatformClient loadModelNewInstance:].cold.15
+ -[_ANEVirtualPlatformClient loadModelNewInstance:].cold.16
+ -[_ANEVirtualPlatformClient loadModelNewInstance:].cold.2
+ -[_ANEVirtualPlatformClient loadModelNewInstance:].cold.3
+ -[_ANEVirtualPlatformClient loadModelNewInstance:].cold.4
+ -[_ANEVirtualPlatformClient loadModelNewInstance:].cold.5
+ -[_ANEVirtualPlatformClient loadModelNewInstance:].cold.6
+ -[_ANEVirtualPlatformClient loadModelNewInstance:].cold.7
+ -[_ANEVirtualPlatformClient loadModelNewInstance:].cold.8
+ -[_ANEVirtualPlatformClient loadModelNewInstance:].cold.9
+ -[_ANEVirtualPlatformClient loadModelNewInstanceLegacy:]
+ -[_ANEVirtualPlatformClient loadModelNewInstanceLegacy:].cold.1
+ -[_ANEVirtualPlatformClient loadModelNewInstanceLegacy:].cold.2
+ -[_ANEVirtualPlatformClient loadModelNewInstanceLegacy:].cold.3
+ -[_ANEVirtualPlatformClient sessionHintWithModel:]
+ -[_ANEVirtualPlatformClient sessionHintWithModel:].cold.1
+ -[_ANEVirtualPlatformClient sessionHintWithModel:].cold.2
+ -[_ANEVirtualPlatformClient updateErrorValueForIOSID:error:dictToUpdate:maxIOSurfaceSize:]
+ -[_ANEVirtualPlatformClient updateErrorValueForIOSID:error:dictToUpdate:maxIOSurfaceSize:].cold.1
+ -[_ANEVirtualPlatformClient updateErrorValueForIOSID:error:dictToUpdate:maxIOSurfaceSize:].cold.2
+ -[_ANEVirtualPlatformClient updatePerformanceStatsDictionary:aneRequest:].cold.1
+ -[_ANEVirtualPlatformClient validateNetworkCreateMLIR:]
+ -[_ANEVirtualPlatformClient validateNetworkCreateMLIR:].cold.1
+ -[_ANEVirtualPlatformClient validateNetworkCreateMLIR:].cold.2
+ -[_ANEVirtualPlatformClient validateNetworkCreateMLIR:].cold.3
+ -[_ANEVirtualPlatformClient writeDictionaryToIOSurfaceID:dict:writtenDataLength:ioSurfaceMaxSize:]
+ -[_ANEVirtualPlatformClient writeDictionaryToIOSurfaceID:dict:writtenDataLength:ioSurfaceMaxSize:].cold.1
+ -[_ANEVirtualPlatformClient writeDictionaryToIOSurfaceID:dict:writtenDataLength:ioSurfaceMaxSize:].cold.2
+ -[_ANEVirtualPlatformClient writeDictionaryToIOSurfaceID:dict:writtenDataLength:ioSurfaceMaxSize:].cold.3
+ -[_ANEVirtualPlatformClient writeDictionaryToIOSurfaceID:dict:writtenDataLength:ioSurfaceMaxSize:].cold.4
+ -[_ANEVirtualPlatformClient writeObjectToIOSurfaceID:obj:writtenDataLength:ioSurfaceMaxSize:]
+ -[_ANEVirtualPlatformClient writeObjectToIOSurfaceID:obj:writtenDataLength:ioSurfaceMaxSize:].cold.1
+ -[_ANEVirtualPlatformClient writeObjectToIOSurfaceID:obj:writtenDataLength:ioSurfaceMaxSize:].cold.2
+ -[_ANEVirtualPlatformClient writeObjectToIOSurfaceID:obj:writtenDataLength:ioSurfaceMaxSize:].cold.3
+ -[_ANEVirtualPlatformClient writeObjectToIOSurfaceID:obj:writtenDataLength:ioSurfaceMaxSize:].cold.4
+ GCC_except_table100
+ GCC_except_table102
+ GCC_except_table117
+ GCC_except_table124
+ GCC_except_table125
+ GCC_except_table126
+ GCC_except_table130
+ GCC_except_table31
+ GCC_except_table42
+ GCC_except_table47
+ GCC_except_table49
+ GCC_except_table50
+ GCC_except_table53
+ GCC_except_table58
+ GCC_except_table61
+ GCC_except_table74
+ GCC_except_table79
+ GCC_except_table80
+ GCC_except_table87
+ GCC_except_table88
+ GCC_except_table91
+ GCC_except_table92
+ GCC_except_table93
+ GCC_except_table94
+ GCC_except_table95
+ GCC_except_table96
+ GCC_except_table97
+ GCC_except_table98
+ GCC_except_table99
+ _ANEValidateNetworkCreate
+ _OBJC_CLASS_$_NSCharacterSet
+ _OBJC_CLASS_$_NSDate
+ _OBJC_CLASS_$_NSDateFormatter
+ _OBJC_CLASS_$_NSFileHandle
+ _OBJC_CLASS_$_NSUUID
+ _OBJC_CLASS_$__ANEStrings
+ _OBJC_IVAR_$__ANEVirtualModel._tmpModelFilesPath
+ _OBJC_IVAR_$__ANEVirtualModel._tmpWeightFilesPath
+ _OUTLINED_FUNCTION_30
+ _OUTLINED_FUNCTION_31
+ __ZN14aneserializers17anemodelparams_v137_ANEModelParamsSerializerDeserializerC2EPNS0_29_ANEModelParamsSerializedDataE
+ __ZNSt3__115allocate_sharedB8ne200100I17_IOSurfaceWrapperNS_9allocatorIS1_EEJRjRU8__strongPU19objcproto9OS_os_log8NSObjectELi0EEENS_10shared_ptrIT_EERKT0_DpOT1_
+ __ZNSt3__115allocate_sharedB8ne200100I17_IOSurfaceWrapperNS_9allocatorIS1_EEJRjU8__strongPU19objcproto9OS_os_log8NSObjectELi0EEENS_10shared_ptrIT_EERKT0_DpOT1_
+ __ZNSt3__119__shared_weak_count16__release_sharedB8ne200100Ev
+ __os_log_impl
+ _objc_alloc_init
+ _objc_msgSend$UUID
+ _objc_msgSend$UUIDString
+ _objc_msgSend$characterSetWithCharactersInString:
+ _objc_msgSend$chunkedDataReceived:
+ _objc_msgSend$closeAndReturnError:
+ _objc_msgSend$controllerWithProgramHandle:
+ _objc_msgSend$copyDictionaryUsingJSONSerialization:toIOSurfaceWithID:withMaxSize:outWrittentDataSize:
+ _objc_msgSend$createLLIRBundleOnDiskFromIOSurfaceWithID:destDirectory:llirDataSize:
+ _objc_msgSend$createModelFileAtPath:fromIOSID:withDataLength:shouldAppend:
+ _objc_msgSend$date
+ _objc_msgSend$description
+ _objc_msgSend$fileHandleForWritingAtPath:
+ _objc_msgSend$fileURLWithPath:
+ _objc_msgSend$generateExpectedBaseDirectoryWith:withCSIdentity:withVMID:fileSubDirectory:
+ _objc_msgSend$generateExpectedModelFilePathFromDictionary:error:
+ _objc_msgSend$generateExpectedModelFilePathFromDictionary:withFileType:error:
+ _objc_msgSend$generateExpectedPathForFileName:withFileType:withInputDictionary:
+ _objc_msgSend$generatedExpectedBaseDirectoryWithFileType:withInputDictionary:
+ _objc_msgSend$getBytes:range:
+ _objc_msgSend$getDataFromIOSurface:withSize:
+ _objc_msgSend$initWithModel:tmpModelFilesPath:tmpWeightFilesPath:
+ _objc_msgSend$initWithUUIDString:
+ _objc_msgSend$invertedSet
+ _objc_msgSend$isBoolBootArgSetTrue:
+ _objc_msgSend$loadModelNewInstance:
+ _objc_msgSend$loadModelNewInstanceLegacy:
+ _objc_msgSend$modelAtURLWithSourceURL:sourceURL:key:identifierSource:cacheURLIdentifier:UUID:
+ _objc_msgSend$modelWithCacheURLIdentifier:UUID:
+ _objc_msgSend$numberWithInt:
+ _objc_msgSend$objectWithModel:tmpModelFilesPath:tmpWeightFilesPath:
+ _objc_msgSend$pStatsRawData
+ _objc_msgSend$path
+ _objc_msgSend$procedureArray
+ _objc_msgSend$rangeOfString:
+ _objc_msgSend$rangeOfString:options:range:
+ _objc_msgSend$seekToEndReturningOffset:error:
+ _objc_msgSend$sessionHintWithModel:
+ _objc_msgSend$sessionHintWithModel:hint:options:report:error:
+ _objc_msgSend$setDateFormat:
+ _objc_msgSend$setObject:forKey:
+ _objc_msgSend$setTmpModelFilesPath:
+ _objc_msgSend$setTmpWeightFilesPath:
+ _objc_msgSend$setValue:forKey:
+ _objc_msgSend$stringByDeletingLastPathComponent
+ _objc_msgSend$stringByTrimmingCharactersInSet:
+ _objc_msgSend$stringFromDate:
+ _objc_msgSend$subdataWithRange:
+ _objc_msgSend$tmpModelFilesPath
+ _objc_msgSend$tmpWeightFilesPath
+ _objc_msgSend$unarchivedObjectOfClass:fromData:error:
+ _objc_msgSend$updateErrorValueForIOSID:error:dictToUpdate:maxIOSurfaceSize:
+ _objc_msgSend$updateTmpWeightFilesPath:
+ _objc_msgSend$updateWeightURL:
+ _objc_msgSend$validateNetworkCreateMLIR:
+ _objc_msgSend$virtualizationHostError:
+ _objc_msgSend$vm_debugDumpBootArg
+ _objc_msgSend$weightArray
+ _objc_msgSend$weightURL
+ _objc_msgSend$writeData:error:
+ _objc_msgSend$writeDictionaryToIOSurfaceID:dict:writtenDataLength:ioSurfaceMaxSize:
+ _objc_msgSend$writeObjectToIOSurfaceID:obj:writtenDataLength:ioSurfaceMaxSize:
+ _objc_msgSend$writeToFile:atomically:
+ _objc_msgSend$writeToFile:atomically:encoding:error:
+ _objc_retain_x25
+ _objc_retain_x4
- -[_ANEVirtualModel initWithModel:]
- -[_ANEVirtualModel initWithModel:].cold.1
- -[_ANEVirtualPlatformClient copyToIOSurface:ioSID:]
- -[_ANEVirtualPlatformClient copyToIOSurface:ioSID:].cold.1
- -[_ANEVirtualPlatformClient copyToIOSurface:ioSID:].cold.2
- -[_ANEVirtualPlatformClient createModelFile:path:ioSID:length:].cold.1
- -[_ANEVirtualPlatformClient createModelFile:path:ioSID:length:].cold.2
- -[_ANEVirtualPlatformClient createModelFile:path:ioSID:length:].cold.3
- -[_ANEVirtualPlatformClient loadModelDictionary:].cold.3
- -[_ANEVirtualPlatformClient loadModelNewInstanceDictionary:]
- -[_ANEVirtualPlatformClient loadModelNewInstanceDictionary:].cold.1
- -[_ANEVirtualPlatformClient loadModelNewInstanceDictionary:].cold.2
- -[_ANEVirtualPlatformClient loadModelNewInstanceDictionary:].cold.3
- GCC_except_table107
- GCC_except_table108
- GCC_except_table109
- GCC_except_table32
- GCC_except_table44
- GCC_except_table51
- GCC_except_table54
- GCC_except_table55
- GCC_except_table62
- GCC_except_table71
- GCC_except_table77
- GCC_except_table85
- __ZNSt3__119__shared_weak_count16__release_sharedB8ne190102Ev
- __Znwm
- _objc_msgSend$initWithModel:
- _objc_msgSend$loadModelNewInstanceDictionary:
- _objc_msgSend$localizedDescription
- _objc_msgSend$modelAtURLWithSourceURL:sourceURL:key:identifierSource:cacheURLIdentifier:
CStrings:
+ "%@: ANEVirtualPlatformClient skipping invalid espresso ref filename"
+ "%@: BEGIN clientCall loadModelNewInstance model=%@!"
+ "%@: CREATED EMPTY DIRECTORY at path=%@"
+ "%@: Could not remove file or directory at path=%@ with error=%@"
+ "%@: END clientCall loadModelNewInstance updatedModel=%@!"
+ "%@: ERROR : BAD_ARGUMENT : destDirectory is nil! cannot create LLIR bundle"
+ "%@: ERROR : BAD_ARGUMENT : dict is nil!"
+ "%@: ERROR : BAD_ARGUMENT : errorIOSurface is nil! cannot update"
+ "%@: ERROR : BAD_ARGUMENT : ioSID is 0!"
+ "%@: ERROR : BAD_ARGUMENT : ioSID is 0! could not find LLIR bundle ioSurface"
+ "%@: ERROR : BAD_ARGUMENT : ioSurfaceMaxSize is 0!"
+ "%@: ERROR : BAD_ARGUMENT : llirDataSize is 0! No data to parse"
+ "%@: ERROR : BAD_ARGUMENT : obj is nil!"
+ "%@: ERROR : BAD_ARGUMENT : passed in dictionary is nil!"
+ "%@: ERROR : BAD_ARGUMENT : passed in ioSID is 0!"
+ "%@: ERROR : BAD_ARGUMENT : passed in ioSurfaceMaxSize is 0!"
+ "%@: ERROR : BAD_ARGUMENT passed in dataSize is nil!"
+ "%@: ERROR : BAD_ARGUMENT passed in ioSurfaceRef is nil!"
+ "%@: ERROR : FAILED to create bundle directory at %@"
+ "%@: ERROR : FAILED to create directory %@ at path %@"
+ "%@: ERROR : FAILED to get NSFileManager object"
+ "%@: ERROR : FAILED to get dataBuffer from surface with ioSID=%u"
+ "%@: ERROR : FAILED to get ioSurfaceRef for ioSID=%u"
+ "%@: ERROR : FAILED to get relativePath for pathData at offset=%llu"
+ "%@: ERROR : FAILED to remove files at existing path=%@"
+ "%@: ERROR : Failed to create dataArchive for object!"
+ "%@: ERROR : Failed to get ioSurfaceRef for ioSID=%u!"
+ "%@: ERROR : Failed to write data, ioSurface too small : dataSize=%llu ioSurfaceMaxSize=%llu"
+ "%@: ERROR : bundleNameData is nil!"
+ "%@: ERROR : bundleNameDataLength is 0!"
+ "%@: ERROR : failed to copy data, dictionaryDataArchive.length %lu > ioSurfaceMaxSize=%llu!"
+ "%@: ERROR : failed to get dataBaseAddress for ioSurface with ioSID=%u!"
+ "%@: ERROR : failed to get ioSurfaceRef for ioSID=%u!"
+ "%@: ERROR : failed to serialize dict"
+ "%@: ERROR : failed to serialize dictionary to NSData with err=%@!"
+ "%@: ERROR : failed to write error data to IOSurface"
+ "%@: ERROR : fileData is nil! at offset=%llu"
+ "%@: ERROR : pathData at offset=%llu is nil!"
+ "%@: ERROR : pathDataLength at offset=%llu is 0!"
+ "%@: ERROR BAD_ARGUMENT passed in dataLength is 0!"
+ "%@: ERROR BAD_ARGUMENT passed in filePathComplete is nil!"
+ "%@: ERROR BAD_ARGUMENT passed in ioSID is 0!"
+ "%@: ERROR No validationParamsIOSID found!"
+ "%@: ERROR aneClient call for loadModelNewInstance failed with error=%@!"
+ "%@: ERROR could not get IOSurface to return model!"
+ "%@: ERROR could not serialize and write modelAttributes to output ioSurface!"
+ "%@: ERROR evaluateWithModel failed with error=%@ model=%@"
+ "%@: ERROR evaluateWithModel failed with request=%@"
+ "%@: ERROR extracted NSData is nil!"
+ "%@: ERROR failed to URLs for weight file paths!"
+ "%@: ERROR failed to close file with error=%@ at path=%@"
+ "%@: ERROR failed to convert uuidString to NSUUID, model data location unknown!"
+ "%@: ERROR failed to create _ANEModel object with cacheURLIdentifier=%@ uuid=%@!"
+ "%@: ERROR failed to create directory at path=%@ with error=%@"
+ "%@: ERROR failed to create model file at path=%@ with error=%@"
+ "%@: ERROR failed to create model file at path=%@! Passed in dataLength exceeds surface alloc size %llu > %zu"
+ "%@: ERROR failed to create model file at path=%@! ioSurface is nil for ioSID=%u"
+ "%@: ERROR failed to create outputDictionary!"
+ "%@: ERROR failed to extract UUID, generating new UUID"
+ "%@: ERROR failed to extract options dictionary from IOSurface with optionsIOSID=%u optionsDataSize=%llu!"
+ "%@: ERROR failed to generate cacheURLIdentifier from cacheURLIdentifierData!"
+ "%@: ERROR failed to generate expected model file path, could not get srcHashDirectory from modelInputPathIOSID!"
+ "%@: ERROR failed to generate expected model file path, could not get uuidString from input dictionary!"
+ "%@: ERROR failed to generate expected model file path, csIdentity needed but data not found in input dictionary!"
+ "%@: ERROR failed to generate expected model file path, modelInputPathDataSize is 0!"
+ "%@: ERROR failed to generate expected model file path, modelInputPathIOSID is 0!"
+ "%@: ERROR failed to generate expected model file path, unknown file type=%u!"
+ "%@: ERROR failed to get cacheURLIdentifierData!"
+ "%@: ERROR failed to get data from ioSID=%u"
+ "%@: ERROR failed to get input validationParams!"
+ "%@: ERROR failed to get modelInstParamsData with error=%@!"
+ "%@: ERROR failed to get modelInstParamsData!"
+ "%@: ERROR failed to open file at path=%@"
+ "%@: ERROR failed to read uuidString, model data location unknown!"
+ "%@: ERROR failed to remove existing file with the same name at path=%@ with error=%@"
+ "%@: ERROR failed to seekToEnd of file with error=%@ at path=%@"
+ "%@: ERROR failed to update modelInstParams, could not generate file url!"
+ "%@: ERROR failed to write data to path=%@"
+ "%@: ERROR failed to write data, dataIOSID is 0!"
+ "%@: ERROR failed to write data, dataSize is 0!"
+ "%@: ERROR failed to write data, unable to extract destination directoryPath!"
+ "%@: ERROR failed to write data, unable to generate a destination filePath from inDictionary data!"
+ "%@: ERROR failed to writeData to file with error=%@ at path=%@"
+ "%@: ERROR loadModelNewInstance failed, could not find .asset directory in path=%@!"
+ "%@: ERROR loadModelNewInstance failed, could not get complete name of .asset directory in path=%@!"
+ "%@: ERROR loadModelNewInstance failed, get overWriteFileName from path=%@!"
+ "%@: ERROR validationParamsDataSize is 0 for validationParamsIOSID=%u"
+ "%@: ERROR value for key kVirtANEModelAttributeLength not found, cannot determine available space!"
+ "%@: FAILED to create LLIR bundle on disk with ioSID=%u"
+ "%@: FAILED to create model files on host"
+ "%@: File NOT found at path=%@, creating directory at path=%@"
+ "%@: File found at path=%@"
+ "%@: Generated expected model file path=%@"
+ "%@: Removed files at existing path=%@"
+ "%@: Removing existing file with the same name at path=%@"
+ "%@: Successfully appended data chunk with chunkSeq=%u at path=%@"
+ "%@: Successfully appended data to file at path=%@"
+ "%@: Successfully created file with data at path=%@"
+ "%@: Update _ANEWeight URL from %@ to %@"
+ "%@: WROTE ALL LLIR FILES"
+ "%@: clientCall success=%lld modelAttributes=%@!"
+ "%@: creating directory at path=%@"
+ "%@: error value is nil, nothing to update"
+ "%@: fileCount=%u"
+ "%@: fileCount=0, kVirtANENumModelFiles is not set (expecting a hwx or llir bundle) sent with a specific identifier!"
+ "%@: invalid IOSID=0 for LLIR IOSurface!"
+ "%@: kVirtANEIOSIDErrorValue not found, cannot update"
+ "%@: model and request data dumped to tmpDir=%@"
+ "%@: no ioSIDPerformanceStatsRaw found"
+ "%@: success=%llu model=%@"
+ "%@: wasModelFileAlreadyAvailable=%d modelPath=%@"
+ "%@: write file to path=%@"
+ "%@_%@.txt"
+ "%s: FAILED to read data, passed in length %llu exceeds IOSurfaceAllocSize %llu"
+ "-[_ANEVirtualPlatformClient echo:]"
+ ".asset"
+ "@28@0:8I16^{__CFDictionary=}20"
+ "@32@0:8^{__CFDictionary=}16^@24"
+ "@32@0:8^{__IOSurface=}16Q24"
+ "@36@0:8@16I24^{__CFDictionary=}28"
+ "@36@0:8^{__CFDictionary=}16I24^@28"
+ "@40@0:8@16@24@32"
+ "@48@0:8@16@24@32@40"
+ "@56@0:8@16@24@32@40@48"
+ "B36@0:8I16@20Q28"
+ "B40@0:8@16I24Q28B36"
+ "B44@0:8@16I24Q28^Q36"
+ "B44@0:8I16@20^Q28Q36"
+ "B44@0:8I16^{__CFDictionary=}20^Q28Q36"
+ "T@\"NSString\",&,N,V_tmpModelFilesPath"
+ "T@\"NSString\",&,N,V_tmpWeightFilesPath"
+ "UUID"
+ "UUIDString"
+ "_tmpModelFilesPath"
+ "_tmpWeightFilesPath"
+ "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_"
+ "cacheURLIdentifierDataSize"
+ "characterSetWithCharactersInString:"
+ "chunkSequence"
+ "chunkedDataReceived:"
+ "closeAndReturnError:"
+ "controllerWithProgramHandle:"
+ "copyDictionaryUsingJSONSerialization:toIOSurfaceWithID:withMaxSize:outWrittentDataSize:"
+ "createLLIRBundleOnDiskFromIOSurfaceWithID:destDirectory:llirDataSize:"
+ "createModelFileAtPath:fromIOSID:withDataLength:shouldAppend:"
+ "date"
+ "description"
+ "dump"
+ "fileDataAlreadySent"
+ "fileHandleForWritingAtPath:"
+ "fileType"
+ "fileURLWithPath:"
+ "generateExpectedBaseDirectoryWith:withCSIdentity:withVMID:fileSubDirectory:"
+ "generateExpectedModelFilePathFromDictionary:error:"
+ "generateExpectedModelFilePathFromDictionary:withFileType:error:"
+ "generateExpectedPathForFileName:withANEBaseDirectory:withCSIdentity:withVMID:fileSubDirectory:"
+ "generateExpectedPathForFileName:withFileType:withInputDictionary:"
+ "generatedExpectedBaseDirectoryWithFileType:withInputDictionary:"
+ "genericDataSize"
+ "genericFileName"
+ "getBytes:range:"
+ "getDataFromIOSurface:withSize:"
+ "initWithModel:tmpModelFilesPath:tmpWeightFilesPath:"
+ "initWithUUIDString:"
+ "invertedSet"
+ "ioSIDCacheURLIdentifierData"
+ "ioSIDGenericData"
+ "ioSIDLLIRBundle"
+ "ioSIDModelInstParamsData"
+ "ioSIDPerformanceStatsRaw"
+ "ioSIDReportData"
+ "ioSIDValidationParams"
+ "isBoolBootArgSetTrue:"
+ "llirDataSize"
+ "loadModelNewInstance:"
+ "loadModelNewInstanceLegacy:"
+ "modelAtURLWithSourceURL:sourceURL:key:identifierSource:cacheURLIdentifier:UUID:"
+ "modelInstParamsDataSize"
+ "modelWithCacheURLIdentifier:UUID:"
+ "model_dump.txt"
+ "numberWithInt:"
+ "objectWithModel:tmpModelFilesPath:tmpWeightFilesPath:"
+ "pStatsRawData"
+ "path"
+ "performanceStatsRawLength"
+ "procedureArray"
+ "rangeOfString:"
+ "rangeOfString:options:range:"
+ "reportDataLength"
+ "request_dump.txt"
+ "seekToEndReturningOffset:error:"
+ "sessionHint"
+ "sessionHintWithModel:"
+ "sessionHintWithModel:hint:options:report:error:"
+ "setDateFormat:"
+ "setObject:forKey:"
+ "setTmpModelFilesPath:"
+ "setTmpWeightFilesPath:"
+ "setValue:forKey:"
+ "stringByDeletingLastPathComponent"
+ "stringByTrimmingCharactersInSet:"
+ "stringFromDate:"
+ "subdataWithRange:"
+ "tmpModelFilesPath"
+ "tmpWeightFilesPath"
+ "unarchivedObjectOfClass:fromData:error:"
+ "updateErrorValueForIOSID:error:dictToUpdate:maxIOSurfaceSize:"
+ "updateTmpWeightFilesPath:"
+ "updateWeightURL:"
+ "v44@0:8I16@20@28Q36"
+ "validateNetworkCreateMLIR:"
+ "validationParamsDataSize"
+ "virtualizationHostError:"
+ "vm_debugDumpBootArg"
+ "weightArray"
+ "weightURL"
+ "writeData:error:"
+ "writeDictionaryToIOSurfaceID:dict:writtenDataLength:ioSurfaceMaxSize:"
+ "writeObjectToIOSurfaceID:obj:writtenDataLength:ioSurfaceMaxSize:"
+ "writeToFile:atomically:"
+ "writeToFile:atomically:encoding:error:"
+ "yyyyMMdd_HHmmss"
- "%@: ANEVirtualPlatformClient fileCount=%u"
- "%@: ANEVirtualPlatformClient fileCount=0, no files to create!"
- "%@: kVirtANENumModelFiles is not set!"
- "%s:ANEVirtualPlatformClient Write model file %@ returned error: %@"
- "%s:ANEVirtualPlatformClient filepath:%@ Length %llu"
- "%s:ANEVirtualPlatformClient iosurface empty modeFileName=%@ path=%@ ioSID=%u length=%lld"
- "%s:ANEVirtualPlatformClient modeFileName=%@ path=%@ ioSID=%u length=%lld"
- "-[_ANEVirtualPlatformClient createModelFile:path:ioSID:length:]"
- "copyToIOSurface:ioSID:"
- "initWithModel:"
- "loadModelNewInstanceDictionary:"
- "localizedDescription"
- "modelAtURLWithSourceURL:sourceURL:key:identifierSource:cacheURLIdentifier:"
- "v28@0:8@16I24"

```
