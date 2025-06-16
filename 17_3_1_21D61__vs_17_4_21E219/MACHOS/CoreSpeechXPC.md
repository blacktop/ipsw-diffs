## CoreSpeechXPC

> `/System/Library/PrivateFrameworks/CoreSpeech.framework/XPCServices/CoreSpeechXPC.xpc/CoreSpeechXPC`

```diff

-3303.7.1.0.0
-  __TEXT.__text: 0x1367c
-  __TEXT.__auth_stubs: 0x660
-  __TEXT.__objc_stubs: 0x29c0
-  __TEXT.__objc_methlist: 0xe78
+3304.82.8.1.2
+  __TEXT.__text: 0x12684
+  __TEXT.__auth_stubs: 0x5a0
+  __TEXT.__objc_stubs: 0x2900
+  __TEXT.__objc_methlist: 0xf58
   __TEXT.__const: 0x20
-  __TEXT.__gcc_except_tab: 0x2e4
-  __TEXT.__cstring: 0x2953
-  __TEXT.__objc_methname: 0x334c
-  __TEXT.__oslogstring: 0x1beb
-  __TEXT.__objc_classname: 0x31a
-  __TEXT.__objc_methtype: 0x636
-  __TEXT.__unwind_info: 0x4cc
-  __TEXT.__eh_frame: 0x38
-  __DATA_CONST.__auth_got: 0x348
-  __DATA_CONST.__got: 0x60
-  __DATA_CONST.__const: 0x870
-  __DATA_CONST.__cfstring: 0x14a0
-  __DATA_CONST.__objc_classlist: 0xa8
+  __TEXT.__gcc_except_tab: 0x48
+  __TEXT.__cstring: 0x27f7
+  __TEXT.__objc_methname: 0x3396
+  __TEXT.__oslogstring: 0x1832
+  __TEXT.__objc_classname: 0x319
+  __TEXT.__objc_methtype: 0x65e
+  __TEXT.__unwind_info: 0x458
+  __DATA_CONST.__auth_got: 0x2e0
+  __DATA_CONST.__got: 0x58
+  __DATA_CONST.__const: 0x800
+  __DATA_CONST.__cfstring: 0x16e0
+  __DATA_CONST.__objc_classlist: 0xb0
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_arraydata: 0x1f8
-  __DATA_CONST.__objc_arrayobj: 0x108
+  __DATA_CONST.__objc_protorefs: 0x8
+  __DATA_CONST.__objc_classrefs: 0x1d0
+  __DATA_CONST.__objc_superrefs: 0x88
+  __DATA_CONST.__objc_arraydata: 0x210
+  __DATA_CONST.__objc_arrayobj: 0x120
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA_CONST.__objc_intobj: 0x150
-  __DATA.__objc_const: 0x21d0
-  __DATA.__objc_selrefs: 0xc78
-  __DATA.__objc_protorefs: 0x8
-  __DATA.__objc_classrefs: 0x1d8
-  __DATA.__objc_superrefs: 0x80
-  __DATA.__objc_ivar: 0xc4
-  __DATA.__objc_data: 0x690
+  __DATA_CONST.__objc_intobj: 0x168
+  __DATA.__objc_const: 0x2310
+  __DATA.__objc_selrefs: 0xce0
+  __DATA.__objc_ivar: 0xcc
+  __DATA.__objc_data: 0x6e0
   __DATA.__data: 0x300
-  __DATA.__bss: 0xb0
+  __DATA.__bss: 0x90
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/PrivateFrameworks/AppSupport.framework/AppSupport
   - /System/Library/PrivateFrameworks/AssistantServices.framework/AssistantServices
-  - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/CoreSpeechFoundation.framework/CoreSpeechFoundation
   - /System/Library/PrivateFrameworks/EmbeddedAcousticRecognition.framework/EmbeddedAcousticRecognition
   - /System/Library/PrivateFrameworks/MobileAsset.framework/MobileAsset

   - /System/Library/PrivateFrameworks/VoiceTrigger.framework/VoiceTrigger
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
-  - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 45970AF4-54BA-3BD4-8AB5-1C661FDEEC2F
-  Functions: 362
-  Symbols:   169
-  CStrings:  1221
+  UUID: EFAE8C52-7A73-3B8F-BF20-CF73741E1EBE
+  Functions: 376
+  Symbols:   153
+  CStrings:  1250
 
Symbols:
+ _CSBnnsIrSuffix
+ _NSLog
+ _OBJC_CLASS_$_NSMutableSet
+ _OBJC_CLASS_$_UAFAssetSetManager
- _AFPreferencesMobileUserSessionLanguage
- _AnalyticsSendEventLazy
- _NSFilePosixPermissions
- _OBJC_CLASS_$_CSOSTransaction
- _OBJC_CLASS_$_NSDate
- _OBJC_CLASS_$_UAFAssetSet
- _OBJC_CLASS_$__EARmil2BnnsCompiler
- _QuasarC_setComputeEngineCacheLookupHandler
- __ZSt9terminatev
- __ZTISt9exception
- ___cxa_begin_catch
- ___cxa_end_catch
- ___gxx_personality_v0
- __os_log_fault_impl
- _bzero
- _objc_autorelease
- _os_unfair_lock_lock
- _os_unfair_lock_unlock
- _strlen
- _strncpy
CStrings:
+ "\x02"
+ "%@"
+ "%s Does not support model type: %lu"
+ "%s Incoming Major version:%@, Incoming Minor version:%@"
+ "%s progCheckerReocgnizerConfigFiles: %@"
+ "+[CSAsset(RTModel) supportsMultiPhraseVoiceTriggerForEngineVersion:engineMinorVersion:accessoryRTModelType:]"
+ "+[CSOnDeviceCompilationUtils getModelCompiledDirWithModelType:basePath:]"
+ "+[CSOnDeviceCompilationUtils getModelConfigsWithAsset:modelType:]"
+ "-[CoreSpeechXPC supportsMultiPhraseVoiceTriggerForEngineVersion:engineMinorVersion:accessoryRTModelType:completion:]"
+ "@32@0:8@16^@24"
+ "@32@0:8@16q24"
+ "@32@0:8q16@24"
+ "@48@0:8@16q24@32@40"
+ "B24@0:8Q16"
+ "B40@0:8@16@24@32"
+ "BnnsIrWeightFile"
+ "CSTempModel"
+ "Decoded config at path: %@"
+ "ERR: metaData is nil, defaulting to NO for %{public}@"
+ "ERR: read metafile %{public}@ failed with %{public}@ - defaulting to NO"
+ "InputOpsMap"
+ "Missing config for Ures %@"
+ "Missing config for regex matcher %@"
+ "ModelFile"
+ "OutputMap"
+ "PostITN"
+ "PreITN"
+ "SLODLDConfigDecoder"
+ "SLUresMitigatorConfigDecoder"
+ "SLUtils"
+ "SecondPassChecker"
+ "SupportedInputOrigins"
+ "T@\"NSDictionary\",&,N,V_dictionary"
+ "T@\"NSString\",&,N,V_resourcePath"
+ "T@\"NSString\",?,R,C"
+ "Version"
+ "_configDict"
+ "_dictionary"
+ "_getCachedIrsFromConfigFile:modelType:CSAsset:cachedIrDir:"
+ "_getValueForKey:categoryKey:"
+ "_resourcePath"
+ "addObjectsFromArray:"
+ "aftm"
+ "allObjects"
+ "assetNamed:"
+ "boolValue"
+ "com.apple.sl"
+ "contConvRecognizerConfigFiles"
+ "createErrorWithMsg:code:"
+ "decodeJsonFromFile:"
+ "enumerateKeysAndObjectsUsingBlock:"
+ "getAllMitigationConfigFiles"
+ "getAllNldaConfigFiles"
+ "getBertModelFile"
+ "getBertModelOutputNodes"
+ "getBnnsIrWeightFile"
+ "getConfigVersion"
+ "getInputOpsMap"
+ "getInputType"
+ "getModelCompiledDirWithModelType:basePath:"
+ "getModelConfigsWithAsset:modelType:"
+ "getModelFile"
+ "getOdldModelBnnsIrWeightFile"
+ "getOutputMap"
+ "getOutputSpecs"
+ "getPreProcessorType"
+ "getRegexMapConfig"
+ "getSPMEncoderOptions"
+ "getSPMModelFile"
+ "getSupportedInputOrigins"
+ "getTokenizerType"
+ "getVersion"
+ "initWithConfigFile:"
+ "initWithConfigFile:errOut:"
+ "inputType"
+ "isSPMModelMmapable"
+ "mmapModel"
+ "model"
+ "modelFile"
+ "neuralCombiner"
+ "odld"
+ "outputNodeName"
+ "outputSpecs"
+ "pipeline"
+ "preprocessing"
+ "progCheckerRecognizerConfigFiles"
+ "readMilFilePathFromConfig:modelType:"
+ "regexMapConfig"
+ "retrieveAssetSet:usages:"
+ "setDictionary:"
+ "setResourcePath:"
+ "sharedManager"
+ "shouldCompileForAssetType:"
+ "spmEncodeOptions"
+ "spmModel"
+ "supportsMultiPhraseVoiceTriggerForEngineVersion:engineMinorVersion:accessoryRTModelType:"
+ "supportsMultiPhraseVoiceTriggerForEngineVersion:engineMinorVersion:accessoryRTModelType:completion:"
+ "tokenizer"
+ "v32@?0@8@16^B24"
+ "v48@0:8@\"NSNumber\"16@\"NSNumber\"24@\"NSNumber\"32@?<v@?B>40"
- "\x03"
- "%s Caching bnnsIr %s to mil path %s"
- "%s Compilation done for modelFile: %@, output cacheIrPath: %@ with error: %@"
- "%s Compile MIL: %@ to BNNS IR: %@"
- "%s Creating model directory not success %@"
- "%s Error setting file permissions: %@"
- "%s Failed to query language code with endpointId %@, trying legacy query"
- "%s No Valid backend for compilation is found for model file: %@ from config: %@"
- "%s Not implemented"
- "%s Only mil2Bnns is supported for prewarm"
- "%s Siri language is nil, falling back to %@"
- "%s bnnsIr already existed, touch file but skipping compilation for: %@"
- "%s bnnsIr cache path: %@ file does not exist"
- "%s checking modelMilBnnsIrCacheMap: %@"
- "%s compute Engine caching Input Mil path invalid or empty"
- "%s endpointUUID not provided, fallback to legacy query"
- "%s invalid for milPath: %@"
- "%s mil2Bnns compilation error for modelFilePath: %@ to bnnsIrCachePath: %@ with error: %@"
- "%s mil2Bnns compilation failed for modelFile: %@ with error: %@"
- "%s no bnnsIR is found for milFile: %@"
- "%s removing milBnns model file path from cacheMap :%@"
- "%s second pass model compilation finished with error %@: "
- "+[CSMil2BnnsUtils _changePermissionOfBnnsIr:]"
- "+[CSMil2BnnsUtils _compileWithExceptionHandlingUsingModelFilePath:bnnsIrPath:milConfigPath:error:]"
- "+[CSMil2BnnsUtils compileModelWithMilFile:bnnsIrCachePath:]"
- "+[CSMil2BnnsUtils mmapModelWithConfig:mappedSizeOut:]"
- "+[CSMil2BnnsUtils removeConfigFromQuasarComputeEngineCacheWithMilBnnsPath:bnnsIrPath:]"
- "+[CSUtils(LanguageCode) getSiriLanguageWithEndpointId:fallbackLanguage:]"
- "+[CSUtils(LanguageCode) getSiriLanguageWithFallback:]"
- "-[CSOnDeviceCompilationHandler _compileModelAndAddToCacheWithConfigFiles:compileDirectoryPath:locale:assetVersion:hashToUse:]"
- "-[CSOnDeviceCompilationHandler compileAndUpdateDeviceCachesWithAsset:assetType:deviceId:currentLocale:compileDirectory:errOut:]_block_invoke"
- "-[CSOnDeviceCompilationHandler compileUsingConfig:locale:compileDirectory:errOut:]_block_invoke"
- "@\"NSDictionary\"8@?0"
- "@56@0:8@16@24@32@40@48"
- "CSMil2BnnsUtils"
- "CSModelEngineCacheLookUpHandler"
- "CSOnDeviceCompilationHandler"
- "CSOnDeviceCompilationHanlder"
- "Hub"
- "LanguageCode"
- "Mil2Bnns compilation"
- "MissingIrFileCount"
- "MissingIrFileForMilFileName"
- "^v32@0:8@16^@24"
- "_changePermissionOfBnnsIr:"
- "_compileModelAndAddToCacheWithConfigFiles:compileDirectoryPath:locale:assetVersion:hashToUse:"
- "_compileWithExceptionHandlingUsingModelFilePath:bnnsIrPath:milConfigPath:error:"
- "_locale"
- "com.apple.corespeech.mil2bnns"
- "compileAndUpdateDeviceCachesWithAsset:assetType:deviceId:currentLocale:compileDirectory:errOut:"
- "compileAndUpdateDeviceCachesWithAsset:assetType:endpointId:errOut:"
- "compileModelWithMilFile:bnnsIrCachePath:"
- "compileUsingConfig:locale:compileDirectory:errOut:"
- "compileWithModelMilPath:bnnsIrOutPath:milConfigPath:errorOut:"
- "config files passed in for compilation is nil"
- "configPathRecognizer"
- "configfileNil"
- "createDirectoryAtPath:withIntermediateDirectories:attributes:error:"
- "date"
- "decodeConfigFrom:forFirstPassSource:"
- "defaultHash"
- "deviceId specified as nil"
- "getAsset:"
- "getSiriLanguageWithEndpointId:fallbackLanguage:"
- "initWithAssetSet:usages:"
- "initWithDescription:"
- "isBridgeOS"
- "languageCodeDarwin"
- "mil"
- "mil2Bnns compilation Failed with exception : %s"
- "mil2Bnns compilation unkown failure from EAR"
- "mmapModelWithConfig:mappedSizeOut:"
- "mmapWithFile:mappedSizeOut:"
- "not avaiable for E5ML"
- "override"
- "pathExtension"
- "readBnnsIrFromCacheMapWithMilFile:"
- "readMilFilePathFromConfig:"
- "removeBnnsIrFromCacheMapWithMilFile:"
- "removeConfigFromQuasarComputeEngineCacheWithMilBnnsPath:bnnsIrPath:"
- "removeObjectForKey:"
- "setAttributes:ofItemAtPath:error:"
- "setBnnsIrForCacheMap:withMilFile:"
- "sharedHandler"
- "stringWithUTF8String:"
- "v48@0:8@16@24@32^@40"
- "v48@0:8@16Q24@32^@40"
- "v64@0:8@16Q24@32@40@48^@56"

```
