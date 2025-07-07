## CoreSpeechFoundation

> `/System/Library/PrivateFrameworks/CoreSpeechFoundation.framework/CoreSpeechFoundation`

```diff

-3300.119.1.1.7
-  __TEXT.__text: 0x4393c
-  __TEXT.__auth_stubs: 0x1170
-  __TEXT.__objc_methlist: 0x47d8
+3301.20.3.0.0
+  __TEXT.__text: 0x419d4
+  __TEXT.__auth_stubs: 0x1140
+  __TEXT.__objc_methlist: 0x4748
   __TEXT.__const: 0x338
-  __TEXT.__gcc_except_tab: 0xde0
-  __TEXT.__cstring: 0x7881
-  __TEXT.__oslogstring: 0x39c1
+  __TEXT.__gcc_except_tab: 0xb44
+  __TEXT.__cstring: 0x74c3
+  __TEXT.__oslogstring: 0x3669
   __TEXT.__dlopen_cstrs: 0x70
-  __TEXT.__unwind_info: 0x13a4
+  __TEXT.__unwind_info: 0x12b4
   __TEXT.__eh_frame: 0x38
-  __TEXT.__objc_classname: 0x92f
-  __TEXT.__objc_methname: 0xef09
-  __TEXT.__objc_methtype: 0x1ba5
-  __TEXT.__objc_stubs: 0x78e0
-  __DATA_CONST.__got: 0x1b8
-  __DATA_CONST.__const: 0xc18
-  __DATA_CONST.__objc_classlist: 0x2b0
+  __TEXT.__objc_classname: 0x904
+  __TEXT.__objc_methname: 0xec69
+  __TEXT.__objc_methtype: 0x1b63
+  __TEXT.__objc_stubs: 0x76c0
+  __DATA_CONST.__got: 0x1a8
+  __DATA_CONST.__const: 0xbe0
+  __DATA_CONST.__objc_classlist: 0x2a0
   __DATA_CONST.__objc_catlist: 0x0
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x6670
-  __DATA_CONST.__objc_selrefs: 0x3328
-  __DATA_CONST.__objc_arraydata: 0x48
+  __DATA_CONST.__objc_const: 0x6630
+  __DATA_CONST.__objc_selrefs: 0x32c0
+  __DATA_CONST.__objc_arraydata: 0x40
   __AUTH_CONST.__const: 0xb60
-  __AUTH_CONST.__objc_const: 0x1ea8
-  __AUTH_CONST.__cfstring: 0x50e0
-  __AUTH_CONST.__objc_arrayobj: 0x30
+  __AUTH_CONST.__objc_const: 0x1dd0
+  __AUTH_CONST.__cfstring: 0x4fc0
+  __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_floatobj: 0x110
-  __AUTH_CONST.__objc_intobj: 0x60
+  __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__objc_dictobj: 0x50
-  __AUTH_CONST.__auth_got: 0x8d0
-  __AUTH.__objc_data: 0xcd0
+  __AUTH_CONST.__auth_got: 0x8b8
+  __AUTH.__objc_data: 0xc30
   __DATA.__objc_protorefs: 0x8
-  __DATA.__objc_classrefs: 0x570
-  __DATA.__objc_superrefs: 0x228
+  __DATA.__objc_classrefs: 0x550
+  __DATA.__objc_superrefs: 0x220
   __DATA.__objc_ivar: 0x578
   __DATA.__data: 0x2e8
   __DATA.__common: 0x8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 7105ADE2-DFA6-3695-A9DD-DA58DC7FF4DC
-  Functions: 1829
-  Symbols:   6551
-  CStrings:  4514
+  UUID: 767DD3C9-F6AC-3A96-8453-5FF21D5C909B
+  Functions: 1815
+  Symbols:   6475
+  CStrings:  4452
 
Symbols:
+ +[CSUtils isM9Device]
+ -[CSAudioStopStreamOption initWithStopRecordingReason:expectedStopHostTime:trailingSilenceDurationAtEndpoint:holdRequest:supportsMagus:requestId:]
+ -[CSAudioStopStreamOption requestId]
+ -[CSAudioStopStreamOption setRequestId:]
+ -[CSFPreferences enableBenchmarkService:]
+ GCC_except_table1106
+ GCC_except_table1215
+ GCC_except_table1223
+ GCC_except_table1231
+ GCC_except_table1238
+ GCC_except_table1245
+ GCC_except_table1247
+ GCC_except_table1251
+ GCC_except_table1271
+ GCC_except_table1302
+ GCC_except_table1327
+ GCC_except_table1328
+ GCC_except_table1329
+ GCC_except_table1330
+ GCC_except_table1351
+ GCC_except_table1404
+ GCC_except_table1438
+ GCC_except_table1447
+ GCC_except_table1448
+ GCC_except_table1450
+ GCC_except_table1453
+ GCC_except_table1454
+ GCC_except_table1538
+ GCC_except_table1539
+ GCC_except_table1541
+ GCC_except_table1542
+ GCC_except_table1544
+ GCC_except_table1546
+ GCC_except_table1547
+ GCC_except_table1548
+ GCC_except_table1559
+ GCC_except_table1578
+ GCC_except_table1582
+ GCC_except_table1679
+ GCC_except_table1715
+ GCC_except_table572
+ GCC_except_table754
+ GCC_except_table755
+ GCC_except_table756
+ GCC_except_table761
+ GCC_except_table765
+ GCC_except_table770
+ GCC_except_table771
+ GCC_except_table772
+ GCC_except_table783
+ GCC_except_table795
+ GCC_except_table796
+ GCC_except_table821
+ GCC_except_table889
+ GCC_except_table891
+ GCC_except_table893
+ GCC_except_table900
+ GCC_except_table901
+ GCC_except_table985
+ _CSIsXR
+ _OBJC_IVAR_$_CSAudioStopStreamOption._requestId
+ __OBJC_$_PROP_LIST_NSObject.1412
+ __OBJC_$_PROP_LIST_NSObject.2422
+ __OBJC_$_PROP_LIST_NSObject.4169
+ __OBJC_$_PROP_LIST_NSObject.4853
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSAudioFileWriter.4854
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCopying.1063
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCopying.1248
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCopying.3826
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCopying.5116
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.1413
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.2423
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.4170
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.4855
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.1414
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.2424
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.4171
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.4856
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSAudioFileWriter.4857
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSCopying.1064
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSCopying.1249
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSCopying.3827
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSCopying.5117
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.1415
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.2425
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.4172
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.4858
+ __OBJC_$_PROTOCOL_REFS_CSAudioFileWriter.4859
+ ___21+[CSUtils isM9Device]_block_invoke
+ ___41-[CSFPreferences enableBenchmarkService:]_block_invoke
+ ___Block_byref_object_copy_.1421
+ ___Block_byref_object_copy_.1675
+ ___Block_byref_object_copy_.2707
+ ___Block_byref_object_copy_.2913
+ ___Block_byref_object_copy_.4109
+ ___Block_byref_object_copy_.4310
+ ___Block_byref_object_copy_.4734
+ ___Block_byref_object_copy_.4808
+ ___Block_byref_object_dispose_.1422
+ ___Block_byref_object_dispose_.1676
+ ___Block_byref_object_dispose_.2708
+ ___Block_byref_object_dispose_.2914
+ ___Block_byref_object_dispose_.4110
+ ___Block_byref_object_dispose_.4311
+ ___Block_byref_object_dispose_.4735
+ ___Block_byref_object_dispose_.4809
+ ___block_descriptor_41_e8_32r_e5_v8?0lr32l8
+ ___block_literal_global.107.977
+ ___block_literal_global.1429
+ ___block_literal_global.186
+ ___block_literal_global.202
+ ___block_literal_global.208
+ ___block_literal_global.2130
+ ___block_literal_global.2257
+ ___block_literal_global.238
+ ___block_literal_global.243
+ ___block_literal_global.248
+ ___block_literal_global.2624
+ ___block_literal_global.287
+ ___block_literal_global.292
+ ___block_literal_global.2938
+ ___block_literal_global.297
+ ___block_literal_global.302
+ ___block_literal_global.3107
+ ___block_literal_global.319
+ ___block_literal_global.324
+ ___block_literal_global.328
+ ___block_literal_global.329
+ ___block_literal_global.335
+ ___block_literal_global.340
+ ___block_literal_global.364
+ ___block_literal_global.369
+ ___block_literal_global.374
+ ___block_literal_global.4401
+ ___block_literal_global.4617
+ ___block_literal_global.4757
+ ___block_literal_global.978
+ __unnamed_array_storage.4608
+ _enableBenchmarkService:.onceToken
+ _isM9Device.isM9Device
+ _isM9Device.onceToken
+ _kCSDiagnosticReporterEndpointDelayNegative
+ _kCSDiagnosticReporterEndpointDelayTooHigh
+ _kCSDiagnosticReporterEndpointerProxyMissingFirstAudioSampleHostTime
+ _objc_msgSend$initWithStopRecordingReason:expectedStopHostTime:trailingSilenceDurationAtEndpoint:holdRequest:supportsMagus:requestId:
+ _sharedInstance.onceToken.1428
+ _sharedInstance.onceToken.3106
+ _sharedInstance.sharedInstance.1430
+ _sharedLogger.onceToken.2129
+ _xpc_string_create
- +[CSMil2BnnsUtils _changePermissionOfBnnsIr:]
- +[CSMil2BnnsUtils _compileWithExceptionHandlingUsingModelFilePath:bnnsIrPath:milConfigPath:error:]
- +[CSMil2BnnsUtils compileModelWithMilFile:bnnsIrCachePath:]
- +[CSMil2BnnsUtils mmapModelWithConfig:mappedSizeOut:]
- +[CSMil2BnnsUtils readBnnsIrFromCacheMapWithMilFile:]
- +[CSMil2BnnsUtils removeBnnsIrFromCacheMapWithMilFile:]
- +[CSMil2BnnsUtils removeConfigFromQuasarComputeEngineCacheWithMilBnnsPath:bnnsIrPath:]
- +[CSMil2BnnsUtils setBnnsIrForCacheMap:withMilFile:]
- +[CSOnDeviceCompilationHandler sharedHandler]
- -[CSOnDeviceCompilationHandler .cxx_destruct]
- -[CSOnDeviceCompilationHandler _compileModelAndAddToCacheWithConfigFiles:compileDirectoryPath:locale:assetVersion:hashToUse:]
- -[CSOnDeviceCompilationHandler compileAndUpdateDeviceCachesWithAsset:assetType:deviceId:currentLocale:compileDirectory:errOut:]
- -[CSOnDeviceCompilationHandler compileAndUpdateDeviceCachesWithAsset:assetType:endpointId:errOut:]
- -[CSOnDeviceCompilationHandler compileUsingConfig:locale:compileDirectory:errOut:]
- -[CSOnDeviceCompilationHandler init]
- GCC_except_table1113
- GCC_except_table1220
- GCC_except_table1228
- GCC_except_table1236
- GCC_except_table1248
- GCC_except_table1250
- GCC_except_table1252
- GCC_except_table1256
- GCC_except_table1276
- GCC_except_table1306
- GCC_except_table1310
- GCC_except_table1319
- GCC_except_table1344
- GCC_except_table1345
- GCC_except_table1346
- GCC_except_table1347
- GCC_except_table1368
- GCC_except_table1421
- GCC_except_table1464
- GCC_except_table1465
- GCC_except_table1467
- GCC_except_table1470
- GCC_except_table1471
- GCC_except_table1472
- GCC_except_table1552
- GCC_except_table1556
- GCC_except_table1558
- GCC_except_table1561
- GCC_except_table1562
- GCC_except_table1567
- GCC_except_table1569
- GCC_except_table1573
- GCC_except_table1574
- GCC_except_table1592
- GCC_except_table1596
- GCC_except_table1693
- GCC_except_table1729
- GCC_except_table569
- GCC_except_table747
- GCC_except_table748
- GCC_except_table749
- GCC_except_table758
- GCC_except_table759
- GCC_except_table763
- GCC_except_table764
- GCC_except_table768
- GCC_except_table780
- GCC_except_table784
- GCC_except_table792
- GCC_except_table818
- GCC_except_table885
- GCC_except_table886
- GCC_except_table890
- GCC_except_table897
- GCC_except_table898
- GCC_except_table941
- GCC_except_table942
- GCC_except_table943
- GCC_except_table944
- GCC_except_table945
- GCC_except_table946
- GCC_except_table947
- GCC_except_table948
- GCC_except_table950
- GCC_except_table992
- _AnalyticsSendEventLazy
- _NSFilePosixPermissions
- _NSLocalizedDescriptionKey
- _OBJC_CLASS_$_CSMil2BnnsUtils
- _OBJC_CLASS_$_CSOnDeviceCompilationHandler
- _OBJC_CLASS_$__EARmil2BnnsCompiler
- _OBJC_IVAR_$_CSOnDeviceCompilationHandler._queue
- _OBJC_METACLASS_$_CSMil2BnnsUtils
- _OBJC_METACLASS_$_CSOnDeviceCompilationHandler
- _QuasarC_setComputeEngineCacheLookupHandler
- __OBJC_$_CLASS_METHODS_CSMil2BnnsUtils
- __OBJC_$_CLASS_METHODS_CSOnDeviceCompilationHandler
- __OBJC_$_INSTANCE_METHODS_CSOnDeviceCompilationHandler
- __OBJC_$_INSTANCE_VARIABLES_CSOnDeviceCompilationHandler
- __OBJC_$_PROP_LIST_NSObject.1410
- __OBJC_$_PROP_LIST_NSObject.2490
- __OBJC_$_PROP_LIST_NSObject.4298
- __OBJC_$_PROP_LIST_NSObject.4983
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSAudioFileWriter.4984
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCopying.1061
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCopying.1246
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCopying.3956
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCopying.5245
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.1411
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.2491
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.4299
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.4985
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.1412
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.2492
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.4300
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.4986
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSAudioFileWriter.4987
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSCopying.1062
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSCopying.1247
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSCopying.3957
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSCopying.5246
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.1413
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.2493
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.4301
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.4988
- __OBJC_$_PROTOCOL_REFS_CSAudioFileWriter.4989
- __OBJC_CLASS_RO_$_CSMil2BnnsUtils
- __OBJC_CLASS_RO_$_CSOnDeviceCompilationHandler
- __OBJC_METACLASS_RO_$_CSMil2BnnsUtils
- __OBJC_METACLASS_RO_$_CSOnDeviceCompilationHandler
- __ZL21milBnnsIrCacheMapLock
- __ZL22modelMilBnnsIrCacheMap
- __ZL31CSModelEngineCacheLookUpHandlerPKcS0_Pcm
- ___127-[CSOnDeviceCompilationHandler compileAndUpdateDeviceCachesWithAsset:assetType:deviceId:currentLocale:compileDirectory:errOut:]_block_invoke
- ___45+[CSOnDeviceCompilationHandler sharedHandler]_block_invoke
- ___82-[CSOnDeviceCompilationHandler compileUsingConfig:locale:compileDirectory:errOut:]_block_invoke
- ___Block_byref_object_copy_.1419
- ___Block_byref_object_copy_.1673
- ___Block_byref_object_copy_.2774
- ___Block_byref_object_copy_.2975
- ___Block_byref_object_copy_.3053
- ___Block_byref_object_copy_.4238
- ___Block_byref_object_copy_.4439
- ___Block_byref_object_copy_.4864
- ___Block_byref_object_copy_.4938
- ___Block_byref_object_dispose_.1420
- ___Block_byref_object_dispose_.1674
- ___Block_byref_object_dispose_.2775
- ___Block_byref_object_dispose_.2976
- ___Block_byref_object_dispose_.3054
- ___Block_byref_object_dispose_.4239
- ___Block_byref_object_dispose_.4440
- ___Block_byref_object_dispose_.4865
- ___Block_byref_object_dispose_.4939
- ____ZL35sendAnalyticsEventBnnsIrFileMissingP8NSString_block_invoke
- ___block_descriptor_40_ea8_32s_e19_"NSDictionary"8?0ls32l8
- ___block_descriptor_72_e8_32s40s48s56s64r_e5_v8?0lr64l8s32l8s40l8s48l8s56l8
- ___block_descriptor_80_e8_32s40s48s56s64s72r_e5_v8?0lr72l8s32l8s40l8s48l8s56l8s64l8
- ___block_literal_global.107.975
- ___block_literal_global.1427
- ___block_literal_global.200
- ___block_literal_global.206
- ___block_literal_global.2196
- ___block_literal_global.2325
- ___block_literal_global.235
- ___block_literal_global.240
- ___block_literal_global.245
- ___block_literal_global.2691
- ___block_literal_global.284
- ___block_literal_global.289
- ___block_literal_global.294
- ___block_literal_global.299
- ___block_literal_global.3011
- ___block_literal_global.3078
- ___block_literal_global.316
- ___block_literal_global.321
- ___block_literal_global.3244
- ___block_literal_global.325
- ___block_literal_global.326
- ___block_literal_global.332
- ___block_literal_global.337
- ___block_literal_global.361
- ___block_literal_global.366
- ___block_literal_global.371
- ___block_literal_global.4528
- ___block_literal_global.4747
- ___block_literal_global.4887
- ___block_literal_global.976
- __unnamed_array_storage.2998
- __unnamed_array_storage.4738
- _objc_msgSend$_changePermissionOfBnnsIr:
- _objc_msgSend$_compileModelAndAddToCacheWithConfigFiles:compileDirectoryPath:locale:assetVersion:hashToUse:
- _objc_msgSend$_compileWithExceptionHandlingUsingModelFilePath:bnnsIrPath:milConfigPath:error:
- _objc_msgSend$compileAndUpdateDeviceCachesWithAsset:assetType:deviceId:currentLocale:compileDirectory:errOut:
- _objc_msgSend$compileModelWithMilFile:bnnsIrCachePath:
- _objc_msgSend$compileWithModelMilPath:bnnsIrOutPath:milConfigPath:errorOut:
- _objc_msgSend$decodeConfigFrom:forFirstPassSource:
- _objc_msgSend$getBackendTypeFromModelFile:
- _objc_msgSend$getIrNameFromModelNameForCompile:locale:assetVersion:hashToUse:
- _objc_msgSend$getMilConfigFromMilFilePath:
- _objc_msgSend$getSiriLanguageWithEndpointId:fallbackLanguage:
- _objc_msgSend$initWithDescription:
- _objc_msgSend$isBridgeOS
- _objc_msgSend$mmapWithFile:mappedSizeOut:
- _objc_msgSend$readBnnsIrFromCacheMapWithMilFile:
- _objc_msgSend$removeBnnsIrFromCacheMapWithMilFile:
- _objc_msgSend$setAttributes:ofItemAtPath:error:
- _objc_msgSend$setBnnsIrForCacheMap:withMilFile:
- _sharedHandler.onceToken
- _sharedHandler.sharedHandler
- _sharedInstance.onceToken.1426
- _sharedInstance.onceToken.3243
- _sharedInstance.sharedInstance.1428
- _sharedLogger.onceToken.2195
- _strlen
- _strncpy
CStrings:
+ "%s benchmarkService: is only avaiable on internal builds"
+ "-[CSFPreferences enableBenchmarkService:]"
+ "@60@0:8Q16Q24d32@40B48@52"
+ "HardwarePlatform"
+ "enableBenchmarkService:"
+ "endpointDelayNegative"
+ "endpointDelayTooHigh"
+ "endpointerProxyMissingFirstAudioSampleHostTime"
+ "initWithStopRecordingReason:expectedStopHostTime:trailingSilenceDurationAtEndpoint:holdRequest:supportsMagus:requestId:"
+ "isM9Device"
+ "t8006"
- "%s Caching bnnsIr %s to mil path %s"
- "%s Compilation done for modelFile: %@, output cacheIrPath: %@ with error: %@"
- "%s Compile MIL: %@ to BNNS IR: %@"
- "%s Creating model directory not success %@"
- "%s Error setting file permissions: %@"
- "%s No Valid backend for compilation is found for model file: %@ from config: %@"
- "%s Not implemented"
- "%s Only mil2Bnns is supported for prewarm"
- "%s bnnsIr already existed, touch file but skipping compilation for: %@"
- "%s bnnsIr cache path: %@ file does not exist"
- "%s checking modelMilBnnsIrCacheMap: %@"
- "%s compute Engine caching Input Mil path invalid or empty"
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
- "Mil2Bnns compilation"
- "MissingIrFileCount"
- "MissingIrFileForMilFileName"
- "_changePermissionOfBnnsIr:"
- "_compileModelAndAddToCacheWithConfigFiles:compileDirectoryPath:locale:assetVersion:hashToUse:"
- "_compileWithExceptionHandlingUsingModelFilePath:bnnsIrPath:milConfigPath:error:"
- "com.apple.corespeech.mil2bnns"
- "compileAndUpdateDeviceCachesWithAsset:assetType:deviceId:currentLocale:compileDirectory:errOut:"
- "compileAndUpdateDeviceCachesWithAsset:assetType:endpointId:errOut:"
- "compileModelWithMilFile:bnnsIrCachePath:"
- "compileUsingConfig:locale:compileDirectory:errOut:"
- "compileWithModelMilPath:bnnsIrOutPath:milConfigPath:errorOut:"
- "config files passed in for compilation is nil"
- "configfileNil"
- "defaultHash"
- "deviceId specified as nil"
- "getSiriLanguageWithEndpointId:fallbackLanguage:"
- "mil2Bnns compilation Failed with exception : %s"
- "mil2Bnns compilation unkown failure from EAR"
- "mmapModelWithConfig:mappedSizeOut:"
- "not avaiable for E5ML"
- "override"
- "readBnnsIrFromCacheMapWithMilFile:"
- "reason"
- "removeBnnsIrFromCacheMapWithMilFile:"
- "removeConfigFromQuasarComputeEngineCacheWithMilBnnsPath:bnnsIrPath:"
- "setAttributes:ofItemAtPath:error:"
- "setBnnsIrForCacheMap:withMilFile:"
- "sharedHandler"
- "v48@0:8@16@24@32^@40"
- "v48@0:8@16Q24@32^@40"
- "v64@0:8@16Q24@32@40@48^@56"

```
