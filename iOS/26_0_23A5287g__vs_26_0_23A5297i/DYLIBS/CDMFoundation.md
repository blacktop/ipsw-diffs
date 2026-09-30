## CDMFoundation

> `/System/Library/PrivateFrameworks/CDMFoundation.framework/CDMFoundation`

```diff

-3500.71.1.0.0
-  __TEXT.__text: 0x27b908
+3500.75.1.0.0
+  __TEXT.__text: 0x27bd8c
   __TEXT.__auth_stubs: 0x9b40
   __TEXT.__objc_methlist: 0x7f94
-  __TEXT.__const: 0xb9bf
-  __TEXT.__swift5_typeref: 0x41e0
-  __TEXT.__swift5_fieldmd: 0x3d2c
+  __TEXT.__const: 0xb9cf
+  __TEXT.__swift5_typeref: 0x41f4
+  __TEXT.__swift5_fieldmd: 0x3d38
   __TEXT.__constg_swiftt: 0x55d8
   __TEXT.__swift5_protos: 0x9c
-  __TEXT.__cstring: 0x1cd75
+  __TEXT.__cstring: 0x1cda5
   __TEXT.__swift5_types: 0x570
   __TEXT.__swift5_proto: 0x9b8
   __TEXT.__swift5_reflstr: 0x300a
   __TEXT.__oslogstring: 0x1c539
   __TEXT.__swift5_assocty: 0x438
-  __TEXT.__swift5_capture: 0xd40
+  __TEXT.__swift5_capture: 0xd54
   __TEXT.__swift5_builtin: 0xf0
   __TEXT.__swift5_mpenum: 0x3c
   __TEXT.__swift_as_entry: 0x224
   __TEXT.__swift_as_ret: 0x270
   __TEXT.__gcc_except_tab: 0xc800
   __TEXT.__ustring: 0x164
-  __TEXT.__unwind_info: 0x7a90
+  __TEXT.__unwind_info: 0x7a98
   __TEXT.__eh_frame: 0x7e5c
   __TEXT.__objc_classname: 0x15aa
   __TEXT.__objc_methname: 0x16523
   __TEXT.__objc_methtype: 0x2ff2
   __TEXT.__objc_stubs: 0x10180
   __DATA_CONST.__got: 0x27b0
-  __DATA_CONST.__const: 0x1da8
+  __DATA_CONST.__const: 0x1db8
   __DATA_CONST.__objc_classlist: 0x8c0
   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0x140

   __DATA_CONST.__objc_superrefs: 0x3f8
   __DATA_CONST.__objc_arraydata: 0xa0
   __AUTH_CONST.__auth_got: 0x4db8
-  __AUTH_CONST.__const: 0xa5b8
+  __AUTH_CONST.__const: 0xa608
   __AUTH_CONST.__cfstring: 0x7da0
-  __AUTH_CONST.__objc_const: 0x12010
+  __AUTH_CONST.__objc_const: 0x12030
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_intobj: 0x420

   __AUTH.__objc_data: 0x1fa8
   __AUTH.__data: 0x46c8
   __DATA.__objc_ivar: 0x74c
-  __DATA.__data: 0x2c08
+  __DATA.__data: 0x2c28
   __DATA.__bss: 0x10d80
   __DATA.__common: 0x808
   __DATA_DIRTY.__objc_data: 0x3af8

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 747326C4-468C-30EB-A3BD-E46152BB6EE3
-  Functions: 11541
-  Symbols:   21617
-  CStrings:  9582
+  UUID: 11703A57-FD0D-389E-ABB4-8D88A22D690E
+  Functions: 11557
+  Symbols:   21633
+  CStrings:  9584
 
Symbols:
+ ___100+[CDMDataDispatcher dispatchCdmRequestData:requestId:withCurrentServiceGraph:dataDispatcherContext:]_block_invoke.370
+ ___141+[CDMServiceGraphNode initWithName:forHandler:usingFunction:withError:cancellationBlock:requestId:dataDispatcherContext:serviceMetricsArray:]_block_invoke.357
+ ___141+[CDMServiceGraphNode initWithName:forHandler:usingFunction:withError:cancellationBlock:requestId:dataDispatcherContext:serviceMetricsArray:]_block_invoke.359
+ ___141+[CDMServiceGraphNode initWithName:forHandler:usingFunction:withError:cancellationBlock:requestId:dataDispatcherContext:serviceMetricsArray:]_block_invoke.371
+ ___26-[CDMXPCClient connection]_block_invoke.425
+ ___32-[CDMMDSServiceGraph buildGraph]_block_invoke.591
+ ___32-[CDMMDSServiceGraph buildGraph]_block_invoke.595
+ ___32-[CDMNLUServiceGraph buildGraph]_block_invoke.615
+ ___32-[CDMNLUServiceGraph buildGraph]_block_invoke.617
+ ___32-[CDMNLUServiceGraph buildGraph]_block_invoke.622
+ ___32-[CDMNLUServiceGraph buildGraph]_block_invoke.626
+ ___32-[CDMNLUServiceGraph buildGraph]_block_invoke.627
+ ___32-[CDMNLUServiceGraph buildGraph]_block_invoke.634
+ ___32-[CDMNLUServiceGraph buildGraph]_block_invoke.635
+ ___32-[CDMNLUServiceGraph buildGraph]_block_invoke.645
+ ___32-[CDMNLUServiceGraph buildGraph]_block_invoke.652
+ ___32-[CDMNLUServiceGraph buildGraph]_block_invoke.659
+ ___32-[CDMNLUServiceGraph buildGraph]_block_invoke.660
+ ___32-[CDMNLUServiceGraph buildGraph]_block_invoke.677
+ ___32-[CDMNLUServiceGraph buildGraph]_block_invoke_2.631
+ ___32-[CDMNLUServiceGraph buildGraph]_block_invoke_2.644
+ ___32-[CDMNLUServiceGraph buildGraph]_block_invoke_2.674
+ ___35-[CDMNLUPreprocessGraph buildGraph]_block_invoke.597
+ ___35-[CDMNLUPreprocessGraph buildGraph]_block_invoke.601
+ ___35-[CDMNLUPreprocessGraph buildGraph]_block_invoke.602
+ ___35-[CDMNLUPreprocessGraph buildGraph]_block_invoke.607
+ ___35-[CDMNLUPreprocessGraph buildGraph]_block_invoke.613
+ ___35-[CDMNLUPreprocessGraph buildGraph]_block_invoke.622
+ ___35-[CDMXPCClient areAssetsAvailable:]_block_invoke.430
+ ___37-[CDMServiceGraph buildGraphInternal]_block_invoke.402
+ ___38-[CDMEmbeddingServiceGraph buildGraph]_block_invoke.512
+ ___39-[CDMHelloWorldServiceGraph buildGraph]_block_invoke.587
+ ___41-[CDMSsuInferenceServiceGraph buildGraph]_block_invoke.582
+ ___41-[CDMSsuInferenceServiceGraph buildGraph]_block_invoke.586
+ ___44-[CDMServiceCenter handleSetup:forCallback:]_block_invoke.532
+ ___44-[CDMServiceCenter handleSetup:forCallback:]_block_invoke.533
+ ___44-[CDMServiceCenter handleSetup:forCallback:]_block_invoke.540
+ ___44-[CDMServiceCenter handleSetup:forCallback:]_block_invoke.542
+ ___44-[CDMServiceCenter handleSetup:forCallback:]_block_invoke.549
+ ___44-[CDMServiceCenter handleSetup:forCallback:]_block_invoke.550
+ ___44-[CDMServiceCenter handleSetup:forCallback:]_block_invoke.556
+ ___44-[CDMServiceCenter handleSetup:forCallback:]_block_invoke_2.557
+ ___44-[CDMXPCClient doHandleCommand:forCallback:]_block_invoke.450
+ ___44-[CDMXPCClient warmupWithCompletionHandler:]_block_invoke.434
+ ___45-[CDMServiceCenter handleWarmup:forCallback:]_block_invoke.509
+ ___46-[CDMServiceCenter handleCommand:forCallback:]_block_invoke.493
+ ___46-[CDMServiceCenter handleCommand:forCallback:]_block_invoke.498
+ ___46-[CDMServiceCenter handleCommand:forCallback:]_block_invoke.500
+ ___47-[CDMXPCClient waitForDataDispatcherCompletion]_block_invoke.446
+ ___61+[CDMDataDispatcher dispatchUaaPData:withResponse:requestId:]_block_invoke.432
+ ___63-[CDMXPCClient processCDMNluRequest:nullableCompletionHandler:]_block_invoke.441
+ ___76+[CDMServiceGraph dispatchServiceGraphRequestLogging:dataDispatcherContext:]_block_invoke.465
+ ___76-[CDMCATIChildService buildLegacyBloomFilterAndExactMatchDictForInvocation:]_block_invoke.429
+ ___77+[CDMDataDispatcher dispatchCdmResponseData:requestId:dataDispatcherContext:]_block_invoke.378
+ ___77+[CDMDataDispatcher dispatchSpanizationData:requestId:dataDispatcherContext:]_block_invoke.410
+ ___83+[CDMSSUService(SystemEvent) fetchVoiceShortcutsWithMatcher:assetCollection:block:]_block_invoke.406
+ ___83-[CDMCATIChildService constructWeightMatrixForInference:numModels:guids:modelType:]_block_invoke.416
+ ___87+[CDMServiceGraph dispatchServiceGraphResponseLogging:requestId:dataDispatcherContext:]_block_invoke.470
+ ___89+[CDMDataDispatcher dispatchCurrentTurnTokenizationData:requestId:dataDispatcherContext:]_block_invoke.388
+ ___Block_byref_object_copy_.10323
+ ___Block_byref_object_copy_.1095
+ ___Block_byref_object_copy_.2013
+ ___Block_byref_object_copy_.2119
+ ___Block_byref_object_copy_.2749
+ ___Block_byref_object_copy_.3323
+ ___Block_byref_object_copy_.337
+ ___Block_byref_object_copy_.3573
+ ___Block_byref_object_copy_.3724
+ ___Block_byref_object_copy_.457
+ ___Block_byref_object_copy_.484
+ ___Block_byref_object_copy_.5034
+ ___Block_byref_object_copy_.6464
+ ___Block_byref_object_copy_.7039
+ ___Block_byref_object_copy_.7988
+ ___Block_byref_object_copy_.8569
+ ___Block_byref_object_dispose_.10324
+ ___Block_byref_object_dispose_.1096
+ ___Block_byref_object_dispose_.2014
+ ___Block_byref_object_dispose_.2120
+ ___Block_byref_object_dispose_.2750
+ ___Block_byref_object_dispose_.3324
+ ___Block_byref_object_dispose_.338
+ ___Block_byref_object_dispose_.3574
+ ___Block_byref_object_dispose_.3725
+ ___Block_byref_object_dispose_.458
+ ___Block_byref_object_dispose_.485
+ ___Block_byref_object_dispose_.5035
+ ___Block_byref_object_dispose_.6465
+ ___Block_byref_object_dispose_.7040
+ ___Block_byref_object_dispose_.7989
+ ___Block_byref_object_dispose_.8570
+ ___block_literal_global.10220
+ ___block_literal_global.10553
+ ___block_literal_global.10711
+ ___block_literal_global.10979
+ ___block_literal_global.1163
+ ___block_literal_global.1343
+ ___block_literal_global.2036
+ ___block_literal_global.312
+ ___block_literal_global.314
+ ___block_literal_global.3585
+ ___block_literal_global.388
+ ___block_literal_global.392
+ ___block_literal_global.394
+ ___block_literal_global.394.8074
+ ___block_literal_global.418
+ ___block_literal_global.4254
+ ___block_literal_global.431
+ ___block_literal_global.4370
+ ___block_literal_global.442
+ ___block_literal_global.446
+ ___block_literal_global.4502
+ ___block_literal_global.463
+ ___block_literal_global.482
+ ___block_literal_global.5328
+ ___block_literal_global.5600
+ ___block_literal_global.584
+ ___block_literal_global.586
+ ___block_literal_global.588
+ ___block_literal_global.590
+ ___block_literal_global.653
+ ___block_literal_global.655
+ ___block_literal_global.6587
+ ___block_literal_global.6988
+ ___block_literal_global.7404
+ ___block_literal_global.7582
+ ___block_literal_global.7667
+ ___block_literal_global.8141
+ ___block_literal_global.8186
+ ___block_literal_global.9698
+ ___block_literal_global.9907
+ _block_copy_helper.190
+ _block_copy_helper.207
+ _block_descriptor.192
+ _block_descriptor.209
+ _block_destroy_helper.191
+ _block_destroy_helper.208
+ _getNameStringToEnumDict.onceToken.7666
+ _getNameStringToEnumDict.onceToken.8185
+ _objectdestroy.176Tm
+ _symbolic So14CDMClientSetupC
- ___100+[CDMDataDispatcher dispatchCdmRequestData:requestId:withCurrentServiceGraph:dataDispatcherContext:]_block_invoke.373
- ___141+[CDMServiceGraphNode initWithName:forHandler:usingFunction:withError:cancellationBlock:requestId:dataDispatcherContext:serviceMetricsArray:]_block_invoke.360
- ___141+[CDMServiceGraphNode initWithName:forHandler:usingFunction:withError:cancellationBlock:requestId:dataDispatcherContext:serviceMetricsArray:]_block_invoke.362
- ___141+[CDMServiceGraphNode initWithName:forHandler:usingFunction:withError:cancellationBlock:requestId:dataDispatcherContext:serviceMetricsArray:]_block_invoke.374
- ___26-[CDMXPCClient connection]_block_invoke.428
- ___32-[CDMMDSServiceGraph buildGraph]_block_invoke.594
- ___32-[CDMMDSServiceGraph buildGraph]_block_invoke.598
- ___32-[CDMNLUServiceGraph buildGraph]_block_invoke.620
- ___32-[CDMNLUServiceGraph buildGraph]_block_invoke.621
- ___32-[CDMNLUServiceGraph buildGraph]_block_invoke.625
- ___32-[CDMNLUServiceGraph buildGraph]_block_invoke.632
- ___32-[CDMNLUServiceGraph buildGraph]_block_invoke.637
- ___32-[CDMNLUServiceGraph buildGraph]_block_invoke.638
- ___32-[CDMNLUServiceGraph buildGraph]_block_invoke.639
- ___32-[CDMNLUServiceGraph buildGraph]_block_invoke.651
- ___32-[CDMNLUServiceGraph buildGraph]_block_invoke.655
- ___32-[CDMNLUServiceGraph buildGraph]_block_invoke.662
- ___32-[CDMNLUServiceGraph buildGraph]_block_invoke.675
- ___32-[CDMNLUServiceGraph buildGraph]_block_invoke.680
- ___32-[CDMNLUServiceGraph buildGraph]_block_invoke_2.634
- ___32-[CDMNLUServiceGraph buildGraph]_block_invoke_2.647
- ___32-[CDMNLUServiceGraph buildGraph]_block_invoke_2.677
- ___35-[CDMNLUPreprocessGraph buildGraph]_block_invoke.604
- ___35-[CDMNLUPreprocessGraph buildGraph]_block_invoke.605
- ___35-[CDMNLUPreprocessGraph buildGraph]_block_invoke.606
- ___35-[CDMNLUPreprocessGraph buildGraph]_block_invoke.610
- ___35-[CDMNLUPreprocessGraph buildGraph]_block_invoke.616
- ___35-[CDMNLUPreprocessGraph buildGraph]_block_invoke.628
- ___35-[CDMXPCClient areAssetsAvailable:]_block_invoke.433
- ___37-[CDMServiceGraph buildGraphInternal]_block_invoke.405
- ___38-[CDMEmbeddingServiceGraph buildGraph]_block_invoke.515
- ___39-[CDMHelloWorldServiceGraph buildGraph]_block_invoke.590
- ___41-[CDMSsuInferenceServiceGraph buildGraph]_block_invoke.585
- ___41-[CDMSsuInferenceServiceGraph buildGraph]_block_invoke.589
- ___44-[CDMServiceCenter handleSetup:forCallback:]_block_invoke.535
- ___44-[CDMServiceCenter handleSetup:forCallback:]_block_invoke.536
- ___44-[CDMServiceCenter handleSetup:forCallback:]_block_invoke.543
- ___44-[CDMServiceCenter handleSetup:forCallback:]_block_invoke.545
- ___44-[CDMServiceCenter handleSetup:forCallback:]_block_invoke.552
- ___44-[CDMServiceCenter handleSetup:forCallback:]_block_invoke.553
- ___44-[CDMServiceCenter handleSetup:forCallback:]_block_invoke.559
- ___44-[CDMServiceCenter handleSetup:forCallback:]_block_invoke_2.560
- ___44-[CDMXPCClient doHandleCommand:forCallback:]_block_invoke.453
- ___44-[CDMXPCClient warmupWithCompletionHandler:]_block_invoke.437
- ___45-[CDMServiceCenter handleWarmup:forCallback:]_block_invoke.512
- ___46-[CDMServiceCenter handleCommand:forCallback:]_block_invoke.496
- ___46-[CDMServiceCenter handleCommand:forCallback:]_block_invoke.501
- ___46-[CDMServiceCenter handleCommand:forCallback:]_block_invoke.503
- ___47-[CDMXPCClient waitForDataDispatcherCompletion]_block_invoke.449
- ___61+[CDMDataDispatcher dispatchUaaPData:withResponse:requestId:]_block_invoke.435
- ___63-[CDMXPCClient processCDMNluRequest:nullableCompletionHandler:]_block_invoke.444
- ___76+[CDMServiceGraph dispatchServiceGraphRequestLogging:dataDispatcherContext:]_block_invoke.468
- ___76-[CDMCATIChildService buildLegacyBloomFilterAndExactMatchDictForInvocation:]_block_invoke.432
- ___77+[CDMDataDispatcher dispatchCdmResponseData:requestId:dataDispatcherContext:]_block_invoke.381
- ___77+[CDMDataDispatcher dispatchSpanizationData:requestId:dataDispatcherContext:]_block_invoke.413
- ___83+[CDMSSUService(SystemEvent) fetchVoiceShortcutsWithMatcher:assetCollection:block:]_block_invoke.409
- ___83-[CDMCATIChildService constructWeightMatrixForInference:numModels:guids:modelType:]_block_invoke.419
- ___87+[CDMServiceGraph dispatchServiceGraphResponseLogging:requestId:dataDispatcherContext:]_block_invoke.473
- ___89+[CDMDataDispatcher dispatchCurrentTurnTokenizationData:requestId:dataDispatcherContext:]_block_invoke.391
- ___Block_byref_object_copy_.10321
- ___Block_byref_object_copy_.1098
- ___Block_byref_object_copy_.2016
- ___Block_byref_object_copy_.2122
- ___Block_byref_object_copy_.2752
- ___Block_byref_object_copy_.3326
- ___Block_byref_object_copy_.340
- ___Block_byref_object_copy_.3576
- ___Block_byref_object_copy_.3727
- ___Block_byref_object_copy_.460
- ___Block_byref_object_copy_.487
- ___Block_byref_object_copy_.5037
- ___Block_byref_object_copy_.6467
- ___Block_byref_object_copy_.7042
- ___Block_byref_object_copy_.7991
- ___Block_byref_object_copy_.8572
- ___Block_byref_object_dispose_.10322
- ___Block_byref_object_dispose_.1099
- ___Block_byref_object_dispose_.2017
- ___Block_byref_object_dispose_.2123
- ___Block_byref_object_dispose_.2753
- ___Block_byref_object_dispose_.3327
- ___Block_byref_object_dispose_.341
- ___Block_byref_object_dispose_.3577
- ___Block_byref_object_dispose_.3728
- ___Block_byref_object_dispose_.461
- ___Block_byref_object_dispose_.488
- ___Block_byref_object_dispose_.5038
- ___Block_byref_object_dispose_.6468
- ___Block_byref_object_dispose_.7043
- ___Block_byref_object_dispose_.7992
- ___Block_byref_object_dispose_.8573
- ___block_literal_global.10218
- ___block_literal_global.10551
- ___block_literal_global.10709
- ___block_literal_global.10977
- ___block_literal_global.1166
- ___block_literal_global.1346
- ___block_literal_global.2039
- ___block_literal_global.315
- ___block_literal_global.317
- ___block_literal_global.3588
- ___block_literal_global.391
- ___block_literal_global.395
- ___block_literal_global.397.8077
- ___block_literal_global.400
- ___block_literal_global.421
- ___block_literal_global.4257
- ___block_literal_global.434
- ___block_literal_global.4373
- ___block_literal_global.449
- ___block_literal_global.4505
- ___block_literal_global.451
- ___block_literal_global.466
- ___block_literal_global.485
- ___block_literal_global.5331
- ___block_literal_global.5603
- ___block_literal_global.587
- ___block_literal_global.589
- ___block_literal_global.591
- ___block_literal_global.593
- ___block_literal_global.656
- ___block_literal_global.658
- ___block_literal_global.6590
- ___block_literal_global.6991
- ___block_literal_global.7407
- ___block_literal_global.7585
- ___block_literal_global.7670
- ___block_literal_global.8144
- ___block_literal_global.8189
- ___block_literal_global.9697
- ___block_literal_global.9906
- _block_copy_helper.201
- _block_descriptor.203
- _block_destroy_helper.202
- _getNameStringToEnumDict.onceToken.7669
- _getNameStringToEnumDict.onceToken.8188
- _objectdestroy.170Tm
CStrings:
+ "Summarise mediaitem override for visual intelligence triggered. Dont run override rule"
+ "com.apple.ScreenshotServicesService"
+ "setupQueue"
- "Summarise mediaitem override for visual intelligence camera triggred. Dont run override rule"

```
