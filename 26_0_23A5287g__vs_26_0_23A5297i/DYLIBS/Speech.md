## Speech

> `/System/Library/Frameworks/Speech.framework/Speech`

```diff

-3500.97.2.0.0
-  __TEXT.__text: 0x1d1a68
-  __TEXT.__auth_stubs: 0x2bb0
-  __TEXT.__objc_methlist: 0x45ec
-  __TEXT.__const: 0xc870
-  __TEXT.__cstring: 0xa85b
-  __TEXT.__constg_swiftt: 0x4430
-  __TEXT.__swift5_typeref: 0x62ac
-  __TEXT.__swift5_reflstr: 0x4575
+3500.101.2.0.0
+  __TEXT.__text: 0x1d2b88
+  __TEXT.__auth_stubs: 0x2c30
+  __TEXT.__objc_methlist: 0x464c
+  __TEXT.__const: 0xc878
+  __TEXT.__cstring: 0xa8e9
+  __TEXT.__constg_swiftt: 0x4438
+  __TEXT.__swift5_typeref: 0x62bc
+  __TEXT.__swift5_reflstr: 0x4565
   __TEXT.__swift5_fieldmd: 0x39cc
   __TEXT.__swift5_builtin: 0xc8
   __TEXT.__swift5_assocty: 0x9c0
   __TEXT.__swift5_proto: 0x864
   __TEXT.__swift5_types: 0x358
-  __TEXT.__oslogstring: 0x3f97
+  __TEXT.__oslogstring: 0x4005
   __TEXT.__swift5_capture: 0x26e4
   __TEXT.__swift5_acfuncs: 0x564
   __TEXT.__swift_as_entry: 0x9fc
   __TEXT.__swift_as_ret: 0xa0c
   __TEXT.__swift5_protos: 0x64
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__gcc_except_tab: 0x890
-  __TEXT.__unwind_info: 0x87b0
-  __TEXT.__eh_frame: 0x12108
+  __TEXT.__gcc_except_tab: 0x894
+  __TEXT.__unwind_info: 0x8800
+  __TEXT.__eh_frame: 0x121b8
   __TEXT.__objc_classname: 0xadc
-  __TEXT.__objc_methname: 0xe2cc
-  __TEXT.__objc_methtype: 0x2a5b
-  __TEXT.__objc_stubs: 0x4ec0
-  __DATA_CONST.__got: 0xd70
+  __TEXT.__objc_methname: 0xe415
+  __TEXT.__objc_methtype: 0x2a85
+  __TEXT.__objc_stubs: 0x4f80
+  __DATA_CONST.__got: 0xd80
   __DATA_CONST.__const: 0x1428
   __DATA_CONST.__objc_classlist: 0x450
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x190
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2bd8
+  __DATA_CONST.__objc_selrefs: 0x2c18
   __DATA_CONST.__objc_protorefs: 0xf0
   __DATA_CONST.__objc_superrefs: 0x210
   __DATA_CONST.__objc_arraydata: 0x90
-  __AUTH_CONST.__auth_got: 0x15e8
+  __AUTH_CONST.__auth_got: 0x1628
   __AUTH_CONST.__const: 0xbcd0
   __AUTH_CONST.__cfstring: 0x3f20
-  __AUTH_CONST.__objc_const: 0xcd20
+  __AUTH_CONST.__objc_const: 0xcd50
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_intobj: 0xf0
   __AUTH.__objc_data: 0x1540
-  __AUTH.__data: 0x2990
-  __DATA.__objc_ivar: 0x574
-  __DATA.__data: 0x3948
+  __AUTH.__data: 0x2980
+  __DATA.__objc_ivar: 0x578
+  __DATA.__data: 0x3988
   __DATA.__common: 0x300
-  __DATA.__bss: 0xdc80
+  __DATA.__bss: 0xdc90
   __DATA_DIRTY.__objc_data: 0xf08
-  __DATA_DIRTY.__data: 0x2b18
-  __DATA_DIRTY.__bss: 0x4e9
+  __DATA_DIRTY.__data: 0x2b58
+  __DATA_DIRTY.__bss: 0x4d9
   __DATA_DIRTY.__common: 0x110
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: A5047C1C-4CAF-3A49-B2B2-AF028EBDBC03
-  Functions: 12675
-  Symbols:   14612
-  CStrings:  4461
+  UUID: 3616805A-CEF5-3736-8768-C0235131B4E2
+  Functions: 12692
+  Symbols:   14642
+  CStrings:  4476
 
Symbols:
+ +[SFSpeechAssetManager fetchAssetWithConfig:clientIdentifier:expiration:detailedProgress:completion:timeout:]
+ +[SFSpeechAssetManager fetchAssetWithConfig:clientIdentifier:expiration:progress:completion:]
+ -[SFLocalSpeechRecognitionClient downloadAssetsForConfig:clientID:expiration:detailedProgress:completionHandler:]
+ -[SFLocalSpeechRecognitionClient downloadAssetsForConfig:clientID:expiration:progress:completionHandler:]
+ -[SFPersonaManager _detectNewPersonas:currentPersonaIds:]
+ -[SFPersonaManager _detectRemovedPersonas:currentPersonaIds:]
+ -[SFPersonaManager addObserver:]
+ -[SFPersonaManager observers]
+ -[SFPersonaManager removeObserver:]
+ -[SFPersonaManager setObservers:]
+ GCC_except_table1043
+ GCC_except_table1068
+ GCC_except_table1071
+ GCC_except_table1154
+ GCC_except_table1175
+ GCC_except_table1361
+ GCC_except_table1370
+ GCC_except_table1376
+ GCC_except_table1389
+ GCC_except_table1391
+ GCC_except_table1393
+ GCC_except_table1394
+ GCC_except_table1395
+ GCC_except_table1398
+ GCC_except_table1400
+ _OBJC_CLASS_$_NSHashTable
+ _OBJC_IVAR_$_SFPersonaManager._observers
+ _SFSpeechErrorCodeInsufficientResources
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_SFSpeechProfileResourceMonitorObserver
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SFSpeechProfileResourceMonitorObserver
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SFSpeechProfileResourceMonitorObserver
+ __OBJC_$_PROTOCOL_REFS_SFSpeechProfileResourceMonitorObserver
+ __OBJC_LABEL_PROTOCOL_$_SFSpeechProfileResourceMonitorObserver
+ __OBJC_PROTOCOL_$_SFSpeechProfileResourceMonitorObserver
+ ___105-[SFLocalSpeechRecognitionClient downloadAssetsForConfig:clientID:expiration:progress:completionHandler:]_block_invoke
+ ___105-[SFLocalSpeechRecognitionClient downloadAssetsForConfig:clientID:expiration:progress:completionHandler:]_block_invoke.56
+ ___105-[SFLocalSpeechRecognitionClient downloadAssetsForConfig:clientID:expiration:progress:completionHandler:]_block_invoke_2
+ ___105-[SFLocalSpeechRecognitionClient downloadAssetsForConfig:clientID:expiration:progress:completionHandler:]_block_invoke_3
+ ___109+[SFSpeechAssetManager fetchAssetWithConfig:clientIdentifier:expiration:detailedProgress:completion:timeout:]_block_invoke
+ ___109+[SFSpeechAssetManager fetchAssetWithConfig:clientIdentifier:expiration:detailedProgress:completion:timeout:]_block_invoke_2
+ ___113-[SFLocalSpeechRecognitionClient downloadAssetsForConfig:clientID:expiration:detailedProgress:completionHandler:]_block_invoke
+ ___113-[SFLocalSpeechRecognitionClient downloadAssetsForConfig:clientID:expiration:detailedProgress:completionHandler:]_block_invoke.57
+ ___113-[SFLocalSpeechRecognitionClient downloadAssetsForConfig:clientID:expiration:detailedProgress:completionHandler:]_block_invoke_2
+ ___32-[SFPersonaManager addObserver:]_block_invoke
+ ___35-[SFPersonaManager removeObserver:]_block_invoke
+ ___58-[SFEntitledAssetManager registerAssetDelegate:assetType:]_block_invoke.504
+ ___58-[SFEntitledAssetManager registerAssetDelegate:assetType:]_block_invoke.508
+ ___58-[SFEntitledAssetManager registerAssetDelegate:assetType:]_block_invoke_2.505
+ ___93+[SFSpeechAssetManager fetchAssetWithConfig:clientIdentifier:expiration:progress:completion:]_block_invoke
+ ___Block_byref_object_copy_.1837
+ ___Block_byref_object_copy_.2175
+ ___Block_byref_object_copy_.2432
+ ___Block_byref_object_copy_.3041
+ ___Block_byref_object_dispose_.1838
+ ___Block_byref_object_dispose_.2176
+ ___Block_byref_object_dispose_.2433
+ ___Block_byref_object_dispose_.3042
+ ___block_descriptor_80_e8_32s40s48s56s64bs72bs_e5_v8?0ls32l8s64l8s72l8s40l8s48l8s56l8
+ ___block_literal_global.1895
+ ___block_literal_global.2133
+ ___block_literal_global.2465
+ ___block_literal_global.2839
+ ___block_literal_global.3095
+ ___block_literal_global.430
+ ___block_literal_global.432
+ ___block_literal_global.454
+ _objc_msgSend$downloadAssetsForConfig:clientID:expiration:detailedProgress:
+ _objc_msgSend$downloadAssetsForConfig:clientID:expiration:detailedProgress:completionHandler:
+ _objc_msgSend$downloadAssetsForConfig:clientID:expiration:progress:completionHandler:
+ _objc_msgSend$endModelRetentionWithCompletion:
+ _objc_msgSend$fetchAssetWithConfig:clientIdentifier:expiration:detailedProgress:completion:timeout:
+ _objc_msgSend$fetchAssetWithConfig:clientIdentifier:expiration:progress:completion:
+ _objc_msgSend$minusSet:
+ _objc_msgSend$newPersonas:
+ _objc_msgSend$removedPersonas:
+ _objc_msgSend$weakObjectsHashTable
+ _sharedInstance.onceToken.1894
+ _sharedInstance.onceToken.1964
+ _sharedInstance.sharedManager.1896
+ _sharedInstance.sharedManager.1965
+ _swift_unownedRelease
+ _swift_unownedRetain
+ _swift_unownedRetainStrong
+ _symbolic _____Sg 10Foundation4DateV
+ _symbolic _____Xo 6Speech0A16RecognizerWorkerC
- -[SFLocalSpeechRecognitionClient downloadAssetsForConfig:clientID:detailedProgress:completionHandler:]
- -[SFLocalSpeechRecognitionClient downloadAssetsForConfig:clientID:progress:completionHandler:]
- GCC_except_table1035
- GCC_except_table1060
- GCC_except_table1063
- GCC_except_table1146
- GCC_except_table1167
- GCC_except_table1353
- GCC_except_table1358
- GCC_except_table1362
- GCC_except_table1368
- GCC_except_table1380
- GCC_except_table1381
- GCC_except_table1383
- GCC_except_table1384
- GCC_except_table1385
- GCC_except_table1388
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_SFSpeechProfileResourceMonitorDelegate
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_SFSpeechProfileResourceMonitorDelegate
- __OBJC_$_PROTOCOL_METHOD_TYPES_SFSpeechProfileResourceMonitorDelegate
- __OBJC_$_PROTOCOL_REFS_SFSpeechProfileResourceMonitorDelegate
- __OBJC_LABEL_PROTOCOL_$_SFSpeechProfileResourceMonitorDelegate
- __OBJC_PROTOCOL_$_SFSpeechProfileResourceMonitorDelegate
- ___102-[SFLocalSpeechRecognitionClient downloadAssetsForConfig:clientID:detailedProgress:completionHandler:]_block_invoke
- ___102-[SFLocalSpeechRecognitionClient downloadAssetsForConfig:clientID:detailedProgress:completionHandler:]_block_invoke.57
- ___102-[SFLocalSpeechRecognitionClient downloadAssetsForConfig:clientID:detailedProgress:completionHandler:]_block_invoke_2
- ___58-[SFEntitledAssetManager registerAssetDelegate:assetType:]_block_invoke.510
- ___58-[SFEntitledAssetManager registerAssetDelegate:assetType:]_block_invoke.511
- ___58-[SFEntitledAssetManager registerAssetDelegate:assetType:]_block_invoke_2.508
- ___82+[SFSpeechAssetManager fetchAssetWithConfig:clientIdentifier:progress:completion:]_block_invoke
- ___94-[SFLocalSpeechRecognitionClient downloadAssetsForConfig:clientID:progress:completionHandler:]_block_invoke
- ___94-[SFLocalSpeechRecognitionClient downloadAssetsForConfig:clientID:progress:completionHandler:]_block_invoke.56
- ___94-[SFLocalSpeechRecognitionClient downloadAssetsForConfig:clientID:progress:completionHandler:]_block_invoke_2
- ___94-[SFLocalSpeechRecognitionClient downloadAssetsForConfig:clientID:progress:completionHandler:]_block_invoke_3
- ___98+[SFSpeechAssetManager fetchAssetWithConfig:clientIdentifier:detailedProgress:completion:timeout:]_block_invoke
- ___98+[SFSpeechAssetManager fetchAssetWithConfig:clientIdentifier:detailedProgress:completion:timeout:]_block_invoke_2
- ___Block_byref_object_copy_.1836
- ___Block_byref_object_copy_.2153
- ___Block_byref_object_copy_.2413
- ___Block_byref_object_copy_.3018
- ___Block_byref_object_dispose_.1837
- ___Block_byref_object_dispose_.2154
- ___Block_byref_object_dispose_.2414
- ___Block_byref_object_dispose_.3019
- ___block_descriptor_72_e8_32s40s48s56bs64bs_e5_v8?0ls32l8s56l8s64l8s40l8s48l8
- ___block_literal_global.1897
- ___block_literal_global.2112
- ___block_literal_global.2446
- ___block_literal_global.2821
- ___block_literal_global.3072
- ___block_literal_global.433
- ___block_literal_global.435
- ___block_literal_global.460.2107
- _objc_msgSend$_endModelRetentionWithCompletion:
- _objc_msgSend$downloadAssetsForConfig:clientID:detailedProgress:
- _objc_msgSend$downloadAssetsForConfig:clientID:detailedProgress:completionHandler:
- _objc_msgSend$downloadAssetsForConfig:clientID:progress:completionHandler:
- _sharedInstance.onceToken.1896
- _sharedInstance.onceToken.1941
- _sharedInstance.sharedManager.1898
- _sharedInstance.sharedManager.1942
CStrings:
+ "%s Detected new persona(s): %@"
+ "%s Detected removed persona(s): %@"
+ "%s No new personas."
+ "%s No removed personas."
+ "+[SFSpeechAssetManager fetchAssetWithConfig:clientIdentifier:expiration:detailedProgress:completion:timeout:]"
+ "+[SFSpeechAssetManager fetchAssetWithConfig:clientIdentifier:expiration:progress:completion:]"
+ "-[SFPersonaManager _detectNewPersonas:currentPersonaIds:]"
+ "-[SFPersonaManager _detectRemovedPersonas:currentPersonaIds:]"
+ "SFSpeechProfileResourceMonitorObserver"
+ "Vv44@0:8@\"SFEntitledAssetConfig\"16@\"NSString\"24@\"NSDate\"32B40"
+ "Vv44@0:8@16@24@32B40"
+ "_detectNewPersonas:currentPersonaIds:"
+ "_detectRemovedPersonas:currentPersonaIds:"
+ "downloadAssetsForConfig:clientID:expiration:detailedProgress:"
+ "downloadAssetsForConfig:clientID:expiration:detailedProgress:completionHandler:"
+ "downloadAssetsForConfig:clientID:expiration:progress:completionHandler:"
+ "endModelRetentionWithCompletion:"
+ "fetchAssetWithConfig:clientIdentifier:expiration:detailedProgress:completion:timeout:"
+ "fetchAssetWithConfig:clientIdentifier:expiration:progress:completion:"
+ "minusSet:"
+ "newPersonas:"
+ "removedPersonas:"
+ "v64@0:8@16@24@32@?40@?48d56"
+ "weakObjectsHashTable"
- "+[SFSpeechAssetManager fetchAssetWithConfig:clientIdentifier:detailedProgress:completion:timeout:]"
- "+[SFSpeechAssetManager fetchAssetWithConfig:clientIdentifier:progress:completion:]"
- "SFSpeechProfileResourceMonitorDelegate"
- "Vv36@0:8@\"SFEntitledAssetConfig\"16@\"NSString\"24B32"
- "Vv36@0:8@16@24B32"
- "_endModelRetentionWithCompletion:"
- "downloadAssetsForConfig:clientID:detailedProgress:"
- "downloadAssetsForConfig:clientID:detailedProgress:completionHandler:"
- "downloadAssetsForConfig:clientID:progress:completionHandler:"

```
