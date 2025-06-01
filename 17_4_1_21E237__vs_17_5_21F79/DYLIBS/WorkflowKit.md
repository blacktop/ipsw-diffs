## WorkflowKit

> `/System/Library/PrivateFrameworks/WorkflowKit.framework/WorkflowKit`

```diff

-2510.5.1.0.0
-  __TEXT.__text: 0x2fdea8
+2605.0.5.0.0
+  __TEXT.__text: 0x2fee68
   __TEXT.__auth_stubs: 0x3590
-  __TEXT.__objc_methlist: 0x27c68
+  __TEXT.__objc_methlist: 0x27df8
   __TEXT.__const: 0x3140
-  __TEXT.__cstring: 0x34bb9
+  __TEXT.__cstring: 0x34cf9
   __TEXT.__constg_swiftt: 0xfe4
   __TEXT.__swift5_typeref: 0x1c25
   __TEXT.__swift5_builtin: 0xb4

   __TEXT.__swift5_protos: 0x1c
   __TEXT.__swift5_mpenum: 0x20
   __TEXT.__gcc_except_tab: 0x3728
-  __TEXT.__oslogstring: 0x12065
+  __TEXT.__oslogstring: 0x1208a
   __TEXT.__dlopen_cstrs: 0xde4
   __TEXT.__ustring: 0x363e
-  __TEXT.__unwind_info: 0xbf94
+  __TEXT.__unwind_info: 0xc148
   __TEXT.__eh_frame: 0x45a0
-  __TEXT.__objc_classname: 0x72b7
-  __TEXT.__objc_methname: 0x4e004
-  __TEXT.__objc_methtype: 0x84db
-  __TEXT.__objc_stubs: 0x319e0
-  __DATA_CONST.__got: 0xe00
-  __DATA_CONST.__const: 0xd0d8
-  __DATA_CONST.__objc_classlist: 0x1cf0
+  __TEXT.__objc_classname: 0x72cf
+  __TEXT.__objc_methname: 0x4e3d2
+  __TEXT.__objc_methtype: 0x8538
+  __TEXT.__objc_stubs: 0x31b40
+  __DATA_CONST.__got: 0xe08
+  __DATA_CONST.__const: 0xd150
+  __DATA_CONST.__objc_classlist: 0x1cf8
   __DATA_CONST.__objc_catlist: 0x378
   __DATA_CONST.__objc_protolist: 0x3e8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x36b78
-  __DATA_CONST.__objc_selrefs: 0xf8f0
+  __DATA_CONST.__objc_const: 0x36d98
+  __DATA_CONST.__objc_selrefs: 0xf988
   __DATA_CONST.__objc_protorefs: 0xf8
-  __DATA_CONST.__objc_classrefs: 0x2520
-  __DATA_CONST.__objc_superrefs: 0x11a0
+  __DATA_CONST.__objc_classrefs: 0x2528
+  __DATA_CONST.__objc_superrefs: 0x11a8
   __DATA_CONST.__objc_arraydata: 0x12c8
   __AUTH_CONST.__const: 0x6b70
-  __AUTH_CONST.__objc_const: 0x19158
-  __AUTH_CONST.__cfstring: 0x27360
-  __AUTH_CONST.__objc_intobj: 0x12d8
+  __AUTH_CONST.__objc_const: 0x191e8
+  __AUTH_CONST.__cfstring: 0x27460
+  __AUTH_CONST.__objc_intobj: 0x12f0
   __AUTH_CONST.__objc_arrayobj: 0x9d8
   __AUTH_CONST.__objc_dictobj: 0x2a8
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH_CONST.__auth_got: 0x1ae0
-  __AUTH.__objc_data: 0x9ad0
-  __AUTH.__data: 0xc20
-  __DATA.__objc_ivar: 0x25b0
+  __AUTH.__objc_data: 0x9928
+  __AUTH.__data: 0xc18
+  __DATA.__objc_ivar: 0x25d4
   __DATA.__objc_data: 0x50
-  __DATA.__data: 0x3c00
-  __DATA.__bss: 0x4a80
+  __DATA.__data: 0x3c98
+  __DATA.__bss: 0x4958
   __DATA.__common: 0x20
-  __DATA_DIRTY.__objc_data: 0x8ce8
-  __DATA_DIRTY.__data: 0x750
-  __DATA_DIRTY.__bss: 0x998
+  __DATA_DIRTY.__objc_data: 0x8ee0
+  __DATA_DIRTY.__data: 0x7d0
+  __DATA_DIRTY.__bss: 0x9a8
   __DATA_DIRTY.__common: 0x8
   - /System/Library/Frameworks/AppIntents.framework/AppIntents
   - /System/Library/Frameworks/CloudKit.framework/CloudKit

   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/Frameworks/UniformTypeIdentifiers.framework/UniformTypeIdentifiers
   - /System/Library/Frameworks/UserNotifications.framework/UserNotifications
+  - /System/Library/PrivateFrameworks/AACCore.framework/AACCore
   - /System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard
   - /System/Library/PrivateFrameworks/BiomeLibrary.framework/BiomeLibrary
   - /System/Library/PrivateFrameworks/BiomePubSub.framework/BiomePubSub

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: B5578FF8-FF54-3AB4-A237-3758EED5E70E
-  Functions: 18127
-  Symbols:   51818
-  CStrings:  26667
+  UUID: 3D33D079-57C8-3F59-AB78-D2B318082880
+  Functions: 18160
+  Symbols:   51921
+  CStrings:  26722
 
Symbols:
+ +[WFAssessmentModeManager isAssessmentModeSupportedOnCurrentDevice]
+ -[WFAction externalMetricsActionIdentifier]
+ -[WFAction externalMetricsBundleIdentifier]
+ -[WFAssessmentModeManager .cxx_destruct]
+ -[WFAssessmentModeManager assessmentGestalt]
+ -[WFAssessmentModeManager dealloc]
+ -[WFAssessmentModeManager delegate]
+ -[WFAssessmentModeManager initWithQueue:delegate:]
+ -[WFAssessmentModeManager isInAssessmentMode]
+ -[WFAssessmentModeManager isObservingLock]
+ -[WFAssessmentModeManager isObserving]
+ -[WFAssessmentModeManager observeValueForKeyPath:ofObject:change:context:]
+ -[WFAssessmentModeManager queue]
+ -[WFAssessmentModeManager setDelegate:]
+ -[WFAssessmentModeManager setIsObserving:]
+ -[WFAssessmentModeManager startObservingForAssesmentModeChangesIfNeeded]
+ -[WFHandleIntentAction externalMetricsActionIdentifier]
+ -[WFHandleIntentAction externalMetricsBundleIdentifier]
+ -[WFLinkAction externalMetricsActionIdentifier]
+ -[WFLinkAction externalMetricsBundleIdentifier]
+ -[WFLinkActionProvider queryMetadataByAppBundleIdentifier:entityIdentifier:]
+ -[WFPBRunActionEvent externalActionIdentifier]
+ -[WFPBRunActionEvent externalBundleIdentifier]
+ -[WFPBRunActionEvent hasExternalActionIdentifier]
+ -[WFPBRunActionEvent hasExternalBundleIdentifier]
+ -[WFPBRunActionEvent setExternalActionIdentifier:]
+ -[WFPBRunActionEvent setExternalBundleIdentifier:]
+ -[WFRunActionEvent externalActionIdentifier]
+ -[WFRunActionEvent externalBundleIdentifier]
+ -[WFRunActionEvent setExternalActionIdentifier:]
+ -[WFRunActionEvent setExternalBundleIdentifier:]
+ GCC_except_table10106
+ GCC_except_table10112
+ GCC_except_table10230
+ GCC_except_table10264
+ GCC_except_table10333
+ GCC_except_table10340
+ GCC_except_table10342
+ GCC_except_table10344
+ GCC_except_table10372
+ GCC_except_table10377
+ GCC_except_table10409
+ GCC_except_table10412
+ GCC_except_table10415
+ GCC_except_table10418
+ GCC_except_table10602
+ GCC_except_table10727
+ GCC_except_table10769
+ GCC_except_table11094
+ GCC_except_table11114
+ GCC_except_table11133
+ GCC_except_table11204
+ GCC_except_table11486
+ GCC_except_table11491
+ GCC_except_table11494
+ GCC_except_table11497
+ GCC_except_table11500
+ GCC_except_table11505
+ GCC_except_table11512
+ GCC_except_table11517
+ GCC_except_table11520
+ GCC_except_table11523
+ GCC_except_table11526
+ GCC_except_table11529
+ GCC_except_table11532
+ GCC_except_table11535
+ GCC_except_table11538
+ GCC_except_table11541
+ GCC_except_table11544
+ GCC_except_table11547
+ GCC_except_table11550
+ GCC_except_table11576
+ GCC_except_table11578
+ GCC_except_table11658
+ GCC_except_table11685
+ GCC_except_table11690
+ GCC_except_table11692
+ GCC_except_table11860
+ GCC_except_table12033
+ GCC_except_table12048
+ GCC_except_table12054
+ GCC_except_table12056
+ GCC_except_table12061
+ GCC_except_table12159
+ GCC_except_table12171
+ GCC_except_table12178
+ GCC_except_table12277
+ GCC_except_table12363
+ GCC_except_table12388
+ GCC_except_table12466
+ GCC_except_table12498
+ GCC_except_table12501
+ GCC_except_table12823
+ GCC_except_table12856
+ GCC_except_table12987
+ GCC_except_table13018
+ GCC_except_table13024
+ GCC_except_table13069
+ GCC_except_table13177
+ GCC_except_table13192
+ GCC_except_table13209
+ GCC_except_table13210
+ GCC_except_table13211
+ GCC_except_table13220
+ GCC_except_table13231
+ GCC_except_table13436
+ GCC_except_table13440
+ GCC_except_table13634
+ GCC_except_table13701
+ GCC_except_table13938
+ GCC_except_table13964
+ GCC_except_table14067
+ GCC_except_table14187
+ GCC_except_table14221
+ GCC_except_table14226
+ GCC_except_table14235
+ GCC_except_table14348
+ GCC_except_table14371
+ GCC_except_table14382
+ GCC_except_table14385
+ GCC_except_table14687
+ GCC_except_table14727
+ GCC_except_table14738
+ GCC_except_table14752
+ GCC_except_table14755
+ GCC_except_table14952
+ GCC_except_table1631
+ GCC_except_table1644
+ GCC_except_table1653
+ GCC_except_table1937
+ GCC_except_table1945
+ GCC_except_table1969
+ GCC_except_table2122
+ GCC_except_table2148
+ GCC_except_table2209
+ GCC_except_table2246
+ GCC_except_table2390
+ GCC_except_table2405
+ GCC_except_table2493
+ GCC_except_table2546
+ GCC_except_table2563
+ GCC_except_table2569
+ GCC_except_table2575
+ GCC_except_table2778
+ GCC_except_table2779
+ GCC_except_table2786
+ GCC_except_table2787
+ GCC_except_table2788
+ GCC_except_table2789
+ GCC_except_table2817
+ GCC_except_table2841
+ GCC_except_table2875
+ GCC_except_table2895
+ GCC_except_table2952
+ GCC_except_table2963
+ GCC_except_table2965
+ GCC_except_table2968
+ GCC_except_table3145
+ GCC_except_table3147
+ GCC_except_table3441
+ GCC_except_table3446
+ GCC_except_table3449
+ GCC_except_table3834
+ GCC_except_table3835
+ GCC_except_table3958
+ GCC_except_table4059
+ GCC_except_table4072
+ GCC_except_table4091
+ GCC_except_table4099
+ GCC_except_table4276
+ GCC_except_table4450
+ GCC_except_table4456
+ GCC_except_table4462
+ GCC_except_table4543
+ GCC_except_table4550
+ GCC_except_table4662
+ GCC_except_table4692
+ GCC_except_table4732
+ GCC_except_table4794
+ GCC_except_table4816
+ GCC_except_table4856
+ GCC_except_table4912
+ GCC_except_table4917
+ GCC_except_table4919
+ GCC_except_table5034
+ GCC_except_table5040
+ GCC_except_table5056
+ GCC_except_table5369
+ GCC_except_table5533
+ GCC_except_table5593
+ GCC_except_table5603
+ GCC_except_table5746
+ GCC_except_table5780
+ GCC_except_table5800
+ GCC_except_table5900
+ GCC_except_table5942
+ GCC_except_table5943
+ GCC_except_table5944
+ GCC_except_table6042
+ GCC_except_table6086
+ GCC_except_table6104
+ GCC_except_table6130
+ GCC_except_table6504
+ GCC_except_table6517
+ GCC_except_table6562
+ GCC_except_table6568
+ GCC_except_table6571
+ GCC_except_table6577
+ GCC_except_table6582
+ GCC_except_table6624
+ GCC_except_table6629
+ GCC_except_table6687
+ GCC_except_table7090
+ GCC_except_table7175
+ GCC_except_table7251
+ GCC_except_table7485
+ GCC_except_table7528
+ GCC_except_table7575
+ GCC_except_table7576
+ GCC_except_table7640
+ GCC_except_table7742
+ GCC_except_table7843
+ GCC_except_table7903
+ GCC_except_table7914
+ GCC_except_table8086
+ GCC_except_table8093
+ GCC_except_table8101
+ GCC_except_table8278
+ GCC_except_table8279
+ GCC_except_table8281
+ GCC_except_table8282
+ GCC_except_table8283
+ GCC_except_table8284
+ GCC_except_table8287
+ GCC_except_table8305
+ GCC_except_table8307
+ GCC_except_table8308
+ GCC_except_table8309
+ GCC_except_table8310
+ GCC_except_table8311
+ GCC_except_table8312
+ GCC_except_table8313
+ GCC_except_table8315
+ GCC_except_table8316
+ GCC_except_table8317
+ GCC_except_table8318
+ GCC_except_table8319
+ GCC_except_table8320
+ GCC_except_table8322
+ GCC_except_table8398
+ GCC_except_table8416
+ GCC_except_table8617
+ GCC_except_table8753
+ GCC_except_table8755
+ GCC_except_table8757
+ GCC_except_table8764
+ GCC_except_table8806
+ GCC_except_table8873
+ GCC_except_table8879
+ GCC_except_table8882
+ GCC_except_table8912
+ GCC_except_table8962
+ GCC_except_table9034
+ GCC_except_table9054
+ GCC_except_table9080
+ GCC_except_table9303
+ GCC_except_table9309
+ GCC_except_table9311
+ GCC_except_table9313
+ GCC_except_table9317
+ GCC_except_table9321
+ GCC_except_table9323
+ GCC_except_table9331
+ GCC_except_table9342
+ GCC_except_table9359
+ GCC_except_table9371
+ GCC_except_table9430
+ GCC_except_table9436
+ GCC_except_table9442
+ GCC_except_table9454
+ GCC_except_table9681
+ GCC_except_table9684
+ GCC_except_table9685
+ GCC_except_table9687
+ GCC_except_table9689
+ GCC_except_table9691
+ GCC_except_table9694
+ GCC_except_table9699
+ GCC_except_table9702
+ GCC_except_table9713
+ GCC_except_table9853
+ GCC_except_table9858
+ GCC_except_table9860
+ GCC_except_table9890
+ GCC_except_table9902
+ GCC_except_table9967
+ OBJC_IVAR_$_WFPBRunActionEvent._externalActionIdentifier
+ OBJC_IVAR_$_WFPBRunActionEvent._externalBundleIdentifier
+ _AssistantServicesLibrary.sLib.66367
+ _AssistantServicesLibrary.sOnce.66366
+ _ContactsLibrary.50785
+ _ContactsLibrary.63408
+ _ContactsLibraryCore.frameworkLibrary.30409
+ _ContactsLibraryCore.frameworkLibrary.45391
+ _ContactsLibraryCore.frameworkLibrary.50835
+ _ContactsLibraryCore.frameworkLibrary.57667
+ _ContactsLibraryCore.frameworkLibrary.62287
+ _ContactsLibraryCore.frameworkLibrary.63416
+ _CoreLocationLibraryCore.frameworkLibrary.39457
+ _CoreLocationLibraryCore.frameworkLibrary.45416
+ _CoreLocationLibraryCore.frameworkLibrary.55856
+ _CoreLocationLibraryCore.frameworkLibrary.56512
+ _CoreLocationLibraryCore.frameworkLibrary.58066
+ _CoreLocationLibraryCore.frameworkLibrary.59835
+ _CoreLocationLibraryCore.frameworkLibrary.62247
+ _HFTriggerActionSetsBuilderFunction.33333
+ _HFTriggerActionSetsBuilderFunction.36509
+ _HMCharacteristicMetadataFormatBoolFunction.2427
+ _HMCharacteristicMetadataFormatBoolFunction.26595
+ _HMCharacteristicMetadataFormatFloatFunction.2406
+ _HMCharacteristicMetadataFormatIntFunction.2413
+ _HMCharacteristicMetadataFormatIntFunction.26706
+ _HMCharacteristicMetadataFormatStringFunction.2420
+ _HMCharacteristicMetadataFormatUInt16Function.2392
+ _HMCharacteristicMetadataFormatUInt32Function.2385
+ _HMCharacteristicMetadataFormatUInt64Function.2375
+ _HMCharacteristicMetadataFormatUInt8Function.2399
+ _HMCharacteristicMetadataFormatUInt8Function.26713
+ _HomeKitLibrary.sLib.1762
+ _HomeKitLibrary.sLib.2368
+ _HomeKitLibrary.sLib.26575
+ _HomeKitLibrary.sLib.33381
+ _HomeKitLibrary.sLib.34063
+ _HomeKitLibrary.sLib.36520
+ _HomeKitLibrary.sLib.53399
+ _HomeKitLibrary.sOnce.1758
+ _HomeKitLibrary.sOnce.2367
+ _HomeKitLibrary.sOnce.26574
+ _HomeKitLibrary.sOnce.33379
+ _HomeKitLibrary.sOnce.34056
+ _HomeKitLibrary.sOnce.36515
+ _HomeKitLibrary.sOnce.53392
+ _HomeLibrary.sLib.26720
+ _HomeLibrary.sLib.33337
+ _HomeLibrary.sLib.36513
+ _HomeLibrary.sOnce.26716
+ _HomeLibrary.sOnce.33329
+ _HomeLibrary.sOnce.36505
+ _MediaPlayerLibrary.34775
+ _MediaPlayerLibrary.50580
+ _MediaPlayerLibraryCore.frameworkLibrary.34784
+ _MediaPlayerLibraryCore.frameworkLibrary.50586
+ _OBJC_CLASS_$_AEAssessmentModeGestalt
+ _OBJC_CLASS_$_WFAssessmentModeManager
+ _OBJC_IVAR_$_WFAssessmentModeManager._assessmentGestalt
+ _OBJC_IVAR_$_WFAssessmentModeManager._delegate
+ _OBJC_IVAR_$_WFAssessmentModeManager._isObserving
+ _OBJC_IVAR_$_WFAssessmentModeManager._isObservingLock
+ _OBJC_IVAR_$_WFAssessmentModeManager._queue
+ _OBJC_IVAR_$_WFRunActionEvent._externalActionIdentifier
+ _OBJC_IVAR_$_WFRunActionEvent._externalBundleIdentifier
+ _OBJC_METACLASS_$_WFAssessmentModeManager
+ _RunningBoardServicesLibrary.25773
+ _RunningBoardServicesLibraryCore.frameworkLibrary.25776
+ _SAObjectsLibrary.sLib.66632
+ _SAObjectsLibrary.sOnce.66630
+ _UIKitLibrary.sLib.15014
+ _UIKitLibrary.sLib.21563
+ _UIKitLibrary.sLib.26987
+ _UIKitLibrary.sLib.27588
+ _UIKitLibrary.sLib.40248
+ _UIKitLibrary.sLib.46573
+ _UIKitLibrary.sLib.55598
+ _UIKitLibrary.sLib.57414
+ _UIKitLibrary.sLib.60607
+ _UIKitLibrary.sOnce.15013
+ _UIKitLibrary.sOnce.21556
+ _UIKitLibrary.sOnce.26980
+ _UIKitLibrary.sOnce.27583
+ _UIKitLibrary.sOnce.40246
+ _UIKitLibrary.sOnce.46563
+ _UIKitLibrary.sOnce.55593
+ _UIKitLibrary.sOnce.57404
+ _UIKitLibrary.sOnce.60597
+ _UIKitLibraryCore.frameworkLibrary.39699
+ _UIPasteboardFunction.40261
+ _UIPasteboardFunction.46568
+ _UIPasteboardFunction.57409
+ _UIPasteboardFunction.60602
+ _WFActionGreenTeaContentDestinationMayLeaveDevice.onceToken.1365
+ _WFAssessmentModeActiveContext
+ _WFCloudKitLibraryFetchedKey
+ _WFEnforceClass.11157
+ _WFEnforceClass.1178
+ _WFEnforceClass.12304
+ _WFEnforceClass.12505
+ _WFEnforceClass.14411
+ _WFEnforceClass.15430
+ _WFEnforceClass.15576
+ _WFEnforceClass.16000
+ _WFEnforceClass.16680
+ _WFEnforceClass.1674
+ _WFEnforceClass.20064
+ _WFEnforceClass.20299
+ _WFEnforceClass.2109
+ _WFEnforceClass.21155
+ _WFEnforceClass.21952
+ _WFEnforceClass.22014
+ _WFEnforceClass.23379
+ _WFEnforceClass.2345
+ _WFEnforceClass.23558
+ _WFEnforceClass.27414
+ _WFEnforceClass.27682
+ _WFEnforceClass.27956
+ _WFEnforceClass.28195
+ _WFEnforceClass.28883
+ _WFEnforceClass.29975
+ _WFEnforceClass.30557
+ _WFEnforceClass.33519
+ _WFEnforceClass.34458
+ _WFEnforceClass.3472
+ _WFEnforceClass.35039
+ _WFEnforceClass.38571
+ _WFEnforceClass.40085
+ _WFEnforceClass.4068
+ _WFEnforceClass.41466
+ _WFEnforceClass.43954
+ _WFEnforceClass.44376
+ _WFEnforceClass.44577
+ _WFEnforceClass.44713
+ _WFEnforceClass.4528
+ _WFEnforceClass.46466
+ _WFEnforceClass.47871
+ _WFEnforceClass.48350
+ _WFEnforceClass.55495
+ _WFEnforceClass.57225
+ _WFEnforceClass.57931
+ _WFEnforceClass.5933
+ _WFEnforceClass.59606
+ _WFEnforceClass.60089
+ _WFEnforceClass.60445
+ _WFEnforceClass.61281
+ _WFEnforceClass.61944
+ _WFEnforceClass.62622
+ _WFEnforceClass.63723
+ _WFEnforceClass.67603
+ _WFEnforceClass.67794
+ _WFEnforceClass.68424
+ _WFEnforceClass.69672
+ _WFEnforceClass.70884
+ _WFEnforceClass.711
+ _WFEnforceClass.71679
+ _WFEnforceClass.7769
+ _WFEnforceClass.8188
+ _WFEnforceClass.8390
+ _WFEnforceClass.8767
+ _WFEnforceClass.9439
+ _WFGroupingPropertyForMediaType.50575
+ _WFSyncUnavailableMessageCountKey
+ _WFSyncUnavailableMessageDateKey
+ _WFSyncUnavailableMessageDismissedByUserKey
+ _WFWorkflowIsAppGroupIdentifier
+ _WFWorkflowIsShortcutsAppGroupIdentifier
+ _WFWorkflowRunSourcePencilSqueeze
+ __OBJC_$_CLASS_METHODS_WFAssessmentModeManager
+ __OBJC_$_INSTANCE_METHODS_WFAssessmentModeManager
+ __OBJC_$_INSTANCE_VARIABLES_WFAssessmentModeManager
+ __OBJC_$_PROP_LIST_WFAssessmentModeManager
+ __OBJC_CLASS_RO_$_WFAssessmentModeManager
+ __OBJC_METACLASS_RO_$_WFAssessmentModeManager
+ ___100-[WFCloudKitWebServiceRequest fetchProxiedRecordWithIdentifier:possibleItemTypes:completionHandler:]_block_invoke.270
+ ___104+[WFOutOfProcessWorkflowController(ContextualActions) computeFinderResizedSizesForImages:inSizes:error:]_block_invoke.167
+ ___116-[WFDialogTransformer sequentialParameterInputProvider:didAdvanceToParameter:action:defaultState:prompt:completion:]_block_invoke.342
+ ___116-[WFDialogTransformer sequentialParameterInputProvider:didAdvanceToParameter:action:defaultState:prompt:completion:]_block_invoke.344
+ ___116-[WFDialogTransformer sequentialParameterInputProvider:didAdvanceToParameter:action:defaultState:prompt:completion:]_block_invoke_2.346
+ ___119-[WFConditionalAction predicateForComparisonOperator:rightDate:secondRightDate:comparableTimeUnits:rightDurationValue:]_block_invoke.272
+ ___119-[WFConditionalAction predicateForComparisonOperator:rightDate:secondRightDate:comparableTimeUnits:rightDurationValue:]_block_invoke_2.274
+ ___119-[WFConditionalAction predicateForComparisonOperator:rightDate:secondRightDate:comparableTimeUnits:rightDurationValue:]_block_invoke_3.275
+ ___129-[WFActionDonationRecommender _fetchDonationsWithLimit:applicationBundleIdentifier:includeSuggestedForAllApps:completionHandler:]_block_invoke.183
+ ___135-[WFAction presentSmartPromptAuthorizationWithConfiguration:userInterface:databaseApprovalResult:contentDestination:completionHandler:]_block_invoke.652
+ ___143-[WFCloudKitItemRequest fetchItemsWithPredicate:itemType:groupName:properties:sortDescriptors:resultsLimit:qualityOfService:completionHandler:]_block_invoke.265
+ ___143-[WFCloudKitItemRequest fetchItemsWithPredicate:itemType:groupName:properties:sortDescriptors:resultsLimit:qualityOfService:completionHandler:]_block_invoke_2.267
+ ___170-[WFSmartPromptConfiguration initWithSmartPromptStates:attributionSet:previousAttributions:contentItemCache:action:contentDestination:reference:source:isWebpageCoercion:]_block_invoke.184
+ ___21-[ICAppRegistry init]_block_invoke.163
+ ___24-[WFActionRegistry fill]_block_invoke.189
+ ___24-[WFActionRegistry fill]_block_invoke_2.190
+ ___31-[WFWorkflow setWorkflowTypes:]_block_invoke.353
+ ___35-[WFAction finishRunningWithError:]_block_invoke.706
+ ___38-[WFDatabase(Sync) updateWalrusStatus]_block_invoke.274
+ ___38-[WFDatabase(Sync) updateWalrusStatus]_block_invoke_2.275
+ ___38-[WFWorkflow saveWithCompletionBlock:]_block_invoke.387
+ ___39-[WFActionRegistry updateCachesAndFill]_block_invoke.193
+ ___39-[WFActionRegistry updateCachesAndFill]_block_invoke.195
+ ___39-[WFActionRegistry updateCachesAndFill]_block_invoke_2.196
+ ___39-[WFDatabase notifyResultsAboutChange:]_block_invoke.276
+ ___43+[WFLinkEntityContentItem propertyBuilders]_block_invoke.212
+ ___43+[WFLinkEntityContentItem propertyBuilders]_block_invoke.222
+ ___43+[WFLinkEntityContentItem propertyBuilders]_block_invoke.224
+ ___44+[WFiTunesObject artworkURLsJSONTransformer]_block_invoke.215
+ ___44-[VCCKVoiceShortcutFetcher fetchRecordZones]_block_invoke.174
+ ___45-[ICManager performQueuedRequestIfApplicable]_block_invoke.196
+ ___45-[WFCloudKitResolveReferencesOperation start]_block_invoke.435
+ ___45-[WFCloudKitResolveReferencesOperation start]_block_invoke.436
+ ___46-[WFActionRegistry updateCacheWithCompletion:]_block_invoke.208
+ ___48+[WFShortcutSigningContext contextWithAuthData:]_block_invoke.175
+ ___48-[WFLinkAction runAsynchronouslyWithLinkAction:]_block_invoke.277
+ ___49-[VCCKVoiceShortcutFetcher fetchRecordsFromZone:]_block_invoke.182
+ ___49-[VCVoiceShortcutPeaceMigrator migrateWithError:]_block_invoke.190
+ ___49-[WFUIPresenterXPCConnection initWithConnection:]_block_invoke.158
+ ___50-[WFConditionalAction runAsynchronouslyWithInput:]_block_invoke.245
+ ___52-[WFHomeWorkflow shortcutsDictionaryRepresentations]_block_invoke.162
+ ___53-[WFDatabaseResult updateDescriptorsAndNotify:state:]_block_invoke.171
+ ___53-[WFIntentExecutor resolveIntent:withExtensionProxy:]_block_invoke.177
+ ___53-[WFIntentExecutor resolveIntent:withExtensionProxy:]_block_invoke_2.179
+ ___54-[WFActionRegistry fillActionProviders:updatingCache:]_block_invoke.201
+ ___54-[WFActionRegistry fillActionProviders:updatingCache:]_block_invoke.205
+ ___54-[WFActionRegistry fillActionProviders:updatingCache:]_block_invoke.206
+ ___54-[WFActionRegistry fillActionProviders:updatingCache:]_block_invoke_2.207
+ ___54-[WFHandleIntentAction finishRunningByContinuingInApp]_block_invoke.273
+ ___55+[WFActionRateLimiter performAction:onQueue:withBlock:]_block_invoke.180
+ ___55-[WFOpenUserActivityAction runAsynchronouslyWithInput:]_block_invoke.205
+ ___55-[WFWorkflow configureAsSingleStepShortcutIfNecessary:]_block_invoke.426
+ ___58-[WFDatabase(Shortcuts) duplicateReference:newName:error:]_block_invoke.319
+ ___58-[WFRemoteExecutionRunRequest writeMessageToWriter:error:]_block_invoke.209
+ ___59-[WFDialogTransformer showDialogRequest:completionHandler:]_block_invoke.206
+ ___59-[WFLinkAction enumeration:localizedLabelForPossibleState:]_block_invoke.412
+ ___59-[WFLinkAction getContentDestinationWithCompletionHandler:]_block_invoke.357
+ ___60-[WFCloudKitSyncSession applyConflictResolution:inDatabase:]_block_invoke.181
+ ___60-[WFLinkContentItemFilterAction runAsynchronouslyWithInput:]_block_invoke.175
+ ___62-[WFAction requestInterfacePresentationWithCompletionHandler:]_block_invoke.713
+ ___63-[WFDatabase(Library) createLibraryFromCurrentDatabaseSnapshot]_block_invoke.178
+ ___63-[WFDatabase(Library) createLibraryFromCurrentDatabaseSnapshot]_block_invoke.186
+ ___63-[WFDatabase(Library) createLibraryFromCurrentDatabaseSnapshot]_block_invoke.188
+ ___64-[WFSequentialParameterInputProvider askForParameterIfAvailable]_block_invoke.163
+ ___65+[WFRemoteWidgetDataProvider handleReceivedData:responseHandler:]_block_invoke.164
+ ___66+[INFile(Workflow) coerceContentItems:toSupportedUTIs:completion:]_block_invoke.192
+ ___66+[INFile(Workflow) coerceContentItems:toSupportedUTIs:completion:]_block_invoke.194
+ ___66+[INFile(Workflow) coerceContentItems:toSupportedUTIs:completion:]_block_invoke_2.193
+ ___66-[WFUIPresenterLaunchAngelConnection prepareConnectionIfNecessary]_block_invoke.300
+ ___66-[WFUIPresenterLaunchAngelConnection prepareConnectionIfNecessary]_block_invoke.301
+ ___68-[WFUIPresenter showDialogRequest:runningContext:completionHandler:]_block_invoke.194
+ ___69-[WFRemoteExecutionRunRequest inflateWithFileCoordinator:completion:]_block_invoke.173
+ ___69-[WFRemoteExecutionRunRequest inflateWithFileCoordinator:completion:]_block_invoke.174
+ ___71-[WFDatabase(Collections) moveReferences:toIndexes:ofCollection:error:]_block_invoke.221
+ ___71-[WFDatabase(Collections) moveReferences:toIndexes:ofCollection:error:]_block_invoke.223
+ ___71-[WFDatabase(Collections) moveReferences:toIndexes:ofCollection:error:]_block_invoke.227
+ ___73-[WFIntentActionProvider createActionsForRequests:forceLocalActionsOnly:]_block_invoke.170
+ ___74-[WFAppInstalledResource fetchiTunesStoreObjectForAppWithCompletionBlock:]_block_invoke.171
+ ___74-[WFAssessmentModeManager observeValueForKeyPath:ofObject:change:context:]_block_invoke
+ ___74-[WFRemoteQuarantinePolicyEvaluator _evaluatePolicyForRequest:completion:]_block_invoke.185
+ ___74-[WFRemoteQuarantinePolicyEvaluator _evaluatePolicyForRequest:completion:]_block_invoke.195
+ ___74-[WFRemoteQuarantinePolicyEvaluator _evaluatePolicyForRequest:completion:]_block_invoke_2.190
+ ___74-[WFRemoteQuarantinePolicyEvaluator _evaluatePolicyForRequest:completion:]_block_invoke_3.192
+ ___75+[VCVoiceShortcutPeaceMigrator migrateFromCloudKitIntoDatabaseIfNecessary:]_block_invoke.160
+ ___75-[WFRemoteExecutionRunRequest inflateInputData:fileCoordinator:completion:]_block_invoke.188
+ ___76-[WFLinkActionProvider queryMetadataByAppBundleIdentifier:entityIdentifier:]_block_invoke
+ ___77-[WFLinkAction fetchMissingDisplayRepresentationValuesWithCompletionHandler:]_block_invoke.390
+ ___77-[WFLinkAction fetchMissingDisplayRepresentationValuesWithCompletionHandler:]_block_invoke.397
+ ___77-[WFLinkAction fetchMissingDisplayRepresentationValuesWithCompletionHandler:]_block_invoke_2.391
+ ___77-[WFLinkAction fetchMissingDisplayRepresentationValuesWithCompletionHandler:]_block_invoke_2.399
+ ___77-[WFLinkAction fetchMissingDisplayRepresentationValuesWithCompletionHandler:]_block_invoke_3.404
+ ___78-[WFVariable getContentWithContext:trackContentAttribution:completionHandler:]_block_invoke.196
+ ___78-[WFVariable getContentWithContext:trackContentAttribution:completionHandler:]_block_invoke_2.197
+ ___79-[WFRemoteExecutionRunRequest inflateVariablesData:fileCoordinator:completion:]_block_invoke.181
+ ___79-[WFRemoteExecutionRunRequest inflateVariablesData:fileCoordinator:completion:]_block_invoke_2.186
+ ___81-[WFShortcutExtractor extractSignedShortcutFile:allowsRetryIfExpired:completion:]_block_invoke.226
+ ___82-[WFContextualActionSuggester suggestActionsForContext:numSuggestions:completion:]_block_invoke.230
+ ___84-[WFRemoteExecutionRunRequestResponse inflateOutputData:fileCoordinator:completion:]_block_invoke.179
+ ___86-[WFAction allowSessionKitSessionsIfNeededWithConfiguration:isManualInvocation:error:]_block_invoke.827
+ ___86-[WFAppPickerParameter loadPossibleStatesForEnumeration:searchTerm:completionHandler:]_block_invoke.158
+ ___86-[WFDatabase(Collections) moveCollections:toIndexes:ofCollectionWithIdentifier:error:]_block_invoke.255
+ ___86-[WFShortcutSigningContext validateSigningCertificateChainWithICloudIdentifier:error:]_block_invoke.225
+ ___87-[WFActionRegistry actionProviderDidChange:updatedActions:removedActions:addedActions:]_block_invoke.222
+ ___87-[WFRemoteExecutionRunRequestResponse inflateVariablesData:fileCoordinator:completion:]_block_invoke.169
+ ___87-[WFRemoteExecutionRunRequestResponse inflateVariablesData:fileCoordinator:completion:]_block_invoke_2.174
+ ___88-[WFAction performDataAccessChecksWithUserInterface:contentItemCache:completionHandler:]_block_invoke.635
+ ___88-[WFAction performDataAccessChecksWithUserInterface:contentItemCache:completionHandler:]_block_invoke.636
+ ___89+[WFOutOfProcessWorkflowController(ContextualActions) contextualActionsForContext:error:]_block_invoke.158
+ ___89-[WFCloudKitItemRequest fetchItemWithID:itemType:groupName:properties:completionHandler:]_block_invoke.276
+ ___89-[WFRemoteExecutionRunRequest inflateProcessedParametersData:fileCoordinator:completion:]_block_invoke.192
+ ___90-[WFCloudKitWebServiceRequest fetchRecordsWithItemType:filter:cacheKey:completionHandler:]_block_invoke.257
+ ___90-[WFMultipleValueParameterState processWithContext:userInputRequiredHandler:valueHandler:]_block_invoke.206
+ ___90-[WFMultipleValueParameterState processWithContext:userInputRequiredHandler:valueHandler:]_block_invoke_2.209
+ ___90-[WFMultipleValueParameterState processWithContext:userInputRequiredHandler:valueHandler:]_block_invoke_3.213
+ ___90-[WFMultipleValueParameterState processWithContext:userInputRequiredHandler:valueHandler:]_block_invoke_4.214
+ ___90-[WFMultipleValueParameterState processWithContext:userInputRequiredHandler:valueHandler:]_block_invoke_5.217
+ ___90-[WFMultipleValueParameterState processWithContext:userInputRequiredHandler:valueHandler:]_block_invoke_6.221
+ ___91-[WFCalendarPickerParameter loadPossibleStatesForEnumeration:searchTerm:completionHandler:]_block_invoke.169
+ ___94-[WFDynamicResolveParameter(WFParameterPicker) wf_loadStatesWithSearchTerm:completionHandler:]_block_invoke.236
+ ___94-[WFDynamicResolveParameter(WFParameterPicker) wf_loadStatesWithSearchTerm:completionHandler:]_block_invoke_2.239
+ ___94-[WFLinkActionProvider createActionsForRequests:allowsActionInDenyList:forceLocalActionsOnly:]_block_invoke.182
+ ___95-[WFActionDonationRecommender fetchRecommendedDonationsForAppPredictionsWithCompletionHandler:]_block_invoke.199
+ ___95-[WFActionDonationRecommender fetchRecommendedDonationsForAppPredictionsWithCompletionHandler:]_block_invoke.206
+ ___95-[WFActionDonationRecommender fetchRecommendedDonationsForAppPredictionsWithCompletionHandler:]_block_invoke_2.200
+ ___95-[WFActionDonationRecommender fetchRecommendedDonationsForAppPredictionsWithCompletionHandler:]_block_invoke_2.209
+ ___95-[WFActionDonationRecommender fetchRecommendedDonationsForAppPredictionsWithCompletionHandler:]_block_invoke_3.211
+ ___95-[WFActionDonationRecommender fetchRecommendedDonationsForAppPredictionsWithCompletionHandler:]_block_invoke_4.213
+ ___96-[WFActionRegistry createActionsWithIdentifiers:serializedParameterArray:forceLocalActionsOnly:]_block_invoke.176
+ ___96-[WFActionRegistry createActionsWithIdentifiers:serializedParameterArray:forceLocalActionsOnly:]_block_invoke_2.178
+ ___98+[WFOutOfProcessWorkflowController(ContextualActions) filteredContextualActions:forContext:error:]_block_invoke.163
+ ___98-[WFAction runWithInput:userInterface:runningDelegate:variableSource:workQueue:completionHandler:]_block_invoke.574
+ ___98-[WFAction runWithInput:userInterface:runningDelegate:variableSource:workQueue:completionHandler:]_block_invoke_2.575
+ ___98-[WFAction runWithInput:userInterface:runningDelegate:variableSource:workQueue:completionHandler:]_block_invoke_3.582
+ ___99-[WFAction performDeletionAuthorizationChecksWithUserInterface:contentItemCache:completionHandler:]_block_invoke.662
+ ___AssistantServicesLibrary_block_invoke.66372
+ ___Block_byref_object_copy_.1029
+ ___Block_byref_object_copy_.11293
+ ___Block_byref_object_copy_.11647
+ ___Block_byref_object_copy_.12514
+ ___Block_byref_object_copy_.13992
+ ___Block_byref_object_copy_.15009
+ ___Block_byref_object_copy_.16815
+ ___Block_byref_object_copy_.16917
+ ___Block_byref_object_copy_.18159
+ ___Block_byref_object_copy_.19092
+ ___Block_byref_object_copy_.19525
+ ___Block_byref_object_copy_.20924
+ ___Block_byref_object_copy_.23125
+ ___Block_byref_object_copy_.23763
+ ___Block_byref_object_copy_.25796
+ ___Block_byref_object_copy_.27572
+ ___Block_byref_object_copy_.2762
+ ___Block_byref_object_copy_.28274
+ ___Block_byref_object_copy_.29943
+ ___Block_byref_object_copy_.3041
+ ___Block_byref_object_copy_.33089
+ ___Block_byref_object_copy_.33362
+ ___Block_byref_object_copy_.34793
+ ___Block_byref_object_copy_.35643
+ ___Block_byref_object_copy_.36835
+ ___Block_byref_object_copy_.38798
+ ___Block_byref_object_copy_.39281
+ ___Block_byref_object_copy_.39926
+ ___Block_byref_object_copy_.40240
+ ___Block_byref_object_copy_.41345
+ ___Block_byref_object_copy_.44018
+ ___Block_byref_object_copy_.44181
+ ___Block_byref_object_copy_.44549
+ ___Block_byref_object_copy_.46448
+ ___Block_byref_object_copy_.46905
+ ___Block_byref_object_copy_.4785
+ ___Block_byref_object_copy_.51261
+ ___Block_byref_object_copy_.5171
+ ___Block_byref_object_copy_.53008
+ ___Block_byref_object_copy_.53780
+ ___Block_byref_object_copy_.54249
+ ___Block_byref_object_copy_.54878
+ ___Block_byref_object_copy_.55902
+ ___Block_byref_object_copy_.56413
+ ___Block_byref_object_copy_.56950
+ ___Block_byref_object_copy_.57569
+ ___Block_byref_object_copy_.60188
+ ___Block_byref_object_copy_.6045
+ ___Block_byref_object_copy_.60919
+ ___Block_byref_object_copy_.61260
+ ___Block_byref_object_copy_.62386
+ ___Block_byref_object_copy_.64465
+ ___Block_byref_object_copy_.66345
+ ___Block_byref_object_copy_.67071
+ ___Block_byref_object_copy_.68032
+ ___Block_byref_object_copy_.68809
+ ___Block_byref_object_copy_.70489
+ ___Block_byref_object_copy_.7749
+ ___Block_byref_object_copy_.780
+ ___Block_byref_object_copy_.8868
+ ___Block_byref_object_copy_.8919
+ ___Block_byref_object_copy_.9507
+ ___Block_byref_object_copy_.9807
+ ___Block_byref_object_dispose_.1030
+ ___Block_byref_object_dispose_.11294
+ ___Block_byref_object_dispose_.11648
+ ___Block_byref_object_dispose_.12515
+ ___Block_byref_object_dispose_.13993
+ ___Block_byref_object_dispose_.15010
+ ___Block_byref_object_dispose_.16816
+ ___Block_byref_object_dispose_.16918
+ ___Block_byref_object_dispose_.18160
+ ___Block_byref_object_dispose_.19093
+ ___Block_byref_object_dispose_.19526
+ ___Block_byref_object_dispose_.20925
+ ___Block_byref_object_dispose_.23126
+ ___Block_byref_object_dispose_.23764
+ ___Block_byref_object_dispose_.25797
+ ___Block_byref_object_dispose_.27573
+ ___Block_byref_object_dispose_.2763
+ ___Block_byref_object_dispose_.28275
+ ___Block_byref_object_dispose_.29944
+ ___Block_byref_object_dispose_.3042
+ ___Block_byref_object_dispose_.33090
+ ___Block_byref_object_dispose_.33363
+ ___Block_byref_object_dispose_.34794
+ ___Block_byref_object_dispose_.35644
+ ___Block_byref_object_dispose_.36836
+ ___Block_byref_object_dispose_.38799
+ ___Block_byref_object_dispose_.39282
+ ___Block_byref_object_dispose_.39927
+ ___Block_byref_object_dispose_.40241
+ ___Block_byref_object_dispose_.41346
+ ___Block_byref_object_dispose_.44019
+ ___Block_byref_object_dispose_.44182
+ ___Block_byref_object_dispose_.44550
+ ___Block_byref_object_dispose_.46449
+ ___Block_byref_object_dispose_.46906
+ ___Block_byref_object_dispose_.4786
+ ___Block_byref_object_dispose_.51262
+ ___Block_byref_object_dispose_.5172
+ ___Block_byref_object_dispose_.53009
+ ___Block_byref_object_dispose_.53781
+ ___Block_byref_object_dispose_.54250
+ ___Block_byref_object_dispose_.54879
+ ___Block_byref_object_dispose_.55903
+ ___Block_byref_object_dispose_.56414
+ ___Block_byref_object_dispose_.56951
+ ___Block_byref_object_dispose_.57570
+ ___Block_byref_object_dispose_.60189
+ ___Block_byref_object_dispose_.6046
+ ___Block_byref_object_dispose_.60920
+ ___Block_byref_object_dispose_.61261
+ ___Block_byref_object_dispose_.62387
+ ___Block_byref_object_dispose_.64466
+ ___Block_byref_object_dispose_.66346
+ ___Block_byref_object_dispose_.67072
+ ___Block_byref_object_dispose_.68033
+ ___Block_byref_object_dispose_.68810
+ ___Block_byref_object_dispose_.70490
+ ___Block_byref_object_dispose_.7750
+ ___Block_byref_object_dispose_.781
+ ___Block_byref_object_dispose_.8869
+ ___Block_byref_object_dispose_.8920
+ ___Block_byref_object_dispose_.9508
+ ___Block_byref_object_dispose_.9808
+ ___ContactsLibraryCore_block_invoke.30410
+ ___ContactsLibraryCore_block_invoke.45392
+ ___ContactsLibraryCore_block_invoke.50836
+ ___ContactsLibraryCore_block_invoke.57668
+ ___ContactsLibraryCore_block_invoke.62288
+ ___ContactsLibraryCore_block_invoke.63417
+ ___CoreLocationLibraryCore_block_invoke.39458
+ ___CoreLocationLibraryCore_block_invoke.45417
+ ___CoreLocationLibraryCore_block_invoke.55857
+ ___CoreLocationLibraryCore_block_invoke.56513
+ ___CoreLocationLibraryCore_block_invoke.58067
+ ___CoreLocationLibraryCore_block_invoke.59836
+ ___CoreLocationLibraryCore_block_invoke.62248
+ ___HomeKitLibrary_block_invoke.1760
+ ___HomeKitLibrary_block_invoke.2377
+ ___HomeKitLibrary_block_invoke.26580
+ ___HomeKitLibrary_block_invoke.33387
+ ___HomeKitLibrary_block_invoke.34061
+ ___HomeKitLibrary_block_invoke.36518
+ ___HomeKitLibrary_block_invoke.53397
+ ___HomeLibrary_block_invoke.26718
+ ___HomeLibrary_block_invoke.33335
+ ___HomeLibrary_block_invoke.36511
+ ___MediaPlayerLibraryCore_block_invoke.34785
+ ___MediaPlayerLibraryCore_block_invoke.50587
+ ___RunningBoardServicesLibraryCore_block_invoke.25777
+ ___SAObjectsLibrary_block_invoke.66636
+ ___UIKitLibraryCore_block_invoke.39700
+ ___UIKitLibrary_block_invoke.15017
+ ___UIKitLibrary_block_invoke.21561
+ ___UIKitLibrary_block_invoke.26985
+ ___UIKitLibrary_block_invoke.27586
+ ___UIKitLibrary_block_invoke.40254
+ ___UIKitLibrary_block_invoke.46571
+ ___UIKitLibrary_block_invoke.55596
+ ___UIKitLibrary_block_invoke.57412
+ ___UIKitLibrary_block_invoke.60605
+ ___WFContentPredicateForRowTemplateValue_block_invoke.220
+ ___WFContentSelectionActionParameterDefinitions_block_invoke.281
+ ___WFContentSelectionActionParameterDefinitions_block_invoke_2.283
+ ___WFLNPropertyQueryForRowTemplateValue_block_invoke.169
+ ___WFSearchActionsWithKeywords_block_invoke.231
+ ___WFShowResult_block_invoke.172
+ ___WFShowResult_block_invoke_2.174
+ ___WFShowResult_block_invoke_3.177
+ ___WFUpdateSmartPromptChangesToShortcutChanges_block_invoke.548
+ ___block_descriptor_40_e8_32s_e25_B16?0"LNQueryMetadata"8ls32l8
+ ___block_descriptor_72_e8_32s40s48s56s_e5_v8?0ls32l8s40l8s48l8s56l8
+ ___block_literal_global.10117
+ ___block_literal_global.1021
+ ___block_literal_global.10407
+ ___block_literal_global.11300
+ ___block_literal_global.11666
+ ___block_literal_global.1201
+ ___block_literal_global.12313
+ ___block_literal_global.12521
+ ___block_literal_global.12719
+ ___block_literal_global.12826
+ ___block_literal_global.13317
+ ___block_literal_global.13398
+ ___block_literal_global.13598
+ ___block_literal_global.1364
+ ___block_literal_global.1367
+ ___block_literal_global.14439
+ ___block_literal_global.14645
+ ___block_literal_global.149
+ ___block_literal_global.14980
+ ___block_literal_global.151
+ ___block_literal_global.157
+ ___block_literal_global.157.21261
+ ___block_literal_global.158.21837
+ ___block_literal_global.161.21838
+ ___block_literal_global.163.37594
+ ___block_literal_global.163.65652
+ ___block_literal_global.163.70506
+ ___block_literal_global.1643
+ ___block_literal_global.165.33978
+ ___block_literal_global.165.42082
+ ___block_literal_global.165.4494
+ ___block_literal_global.166
+ ___block_literal_global.167
+ ___block_literal_global.168.49434
+ ___block_literal_global.168.70533
+ ___block_literal_global.16958
+ ___block_literal_global.171.70534
+ ___block_literal_global.174.56754
+ ___block_literal_global.174.70879
+ ___block_literal_global.17690
+ ___block_literal_global.177.27468
+ ___block_literal_global.1772
+ ___block_literal_global.17759
+ ___block_literal_global.178.72322
+ ___block_literal_global.18066
+ ___block_literal_global.181.23561
+ ___block_literal_global.181.23768
+ ___block_literal_global.181.46469
+ ___block_literal_global.181.72324
+ ___block_literal_global.183.25841
+ ___block_literal_global.18384
+ ___block_literal_global.184.11290
+ ___block_literal_global.184.16939
+ ___block_literal_global.184.23769
+ ___block_literal_global.184.54058
+ ___block_literal_global.185
+ ___block_literal_global.186.41694
+ ___block_literal_global.187
+ ___block_literal_global.1870
+ ___block_literal_global.192
+ ___block_literal_global.194.49236
+ ___block_literal_global.197.27463
+ ___block_literal_global.198.50560
+ ___block_literal_global.19881
+ ___block_literal_global.199
+ ___block_literal_global.199.23729
+ ___block_literal_global.200
+ ___block_literal_global.200.64890
+ ___block_literal_global.201.42048
+ ___block_literal_global.204
+ ___block_literal_global.204.61624
+ ___block_literal_global.205
+ ___block_literal_global.205.50555
+ ___block_literal_global.20728
+ ___block_literal_global.21145
+ ___block_literal_global.212
+ ___block_literal_global.212.70475
+ ___block_literal_global.21313
+ ___block_literal_global.21557
+ ___block_literal_global.216.65358
+ ___block_literal_global.21628
+ ___block_literal_global.217
+ ___block_literal_global.218
+ ___block_literal_global.21836
+ ___block_literal_global.223
+ ___block_literal_global.224
+ ___block_literal_global.22445
+ ___block_literal_global.225
+ ___block_literal_global.225.64487
+ ___block_literal_global.229.24500
+ ___block_literal_global.229.34630
+ ___block_literal_global.229.65356
+ ___block_literal_global.23143
+ ___block_literal_global.232
+ ___block_literal_global.232.72263
+ ___block_literal_global.23400
+ ___block_literal_global.2352
+ ___block_literal_global.23563
+ ___block_literal_global.236
+ ___block_literal_global.236.52172
+ ___block_literal_global.23704
+ ___block_literal_global.24015
+ ___block_literal_global.244.23148
+ ___block_literal_global.24499
+ ___block_literal_global.245
+ ___block_literal_global.246
+ ___block_literal_global.24787
+ ___block_literal_global.2512
+ ___block_literal_global.25127
+ ___block_literal_global.25362
+ ___block_literal_global.254.44288
+ ___block_literal_global.256
+ ___block_literal_global.257
+ ___block_literal_global.258
+ ___block_literal_global.25838
+ ___block_literal_global.26183
+ ___block_literal_global.264
+ ___block_literal_global.26569
+ ___block_literal_global.268
+ ___block_literal_global.269
+ ___block_literal_global.26981
+ ___block_literal_global.273
+ ___block_literal_global.27479
+ ___block_literal_global.2755
+ ___block_literal_global.27575
+ ___block_literal_global.27684
+ ___block_literal_global.27935
+ ___block_literal_global.282.67571
+ ___block_literal_global.28258
+ ___block_literal_global.283
+ ___block_literal_global.284
+ ___block_literal_global.285
+ ___block_literal_global.290
+ ___block_literal_global.291
+ ___block_literal_global.291.6144
+ ___block_literal_global.29112
+ ___block_literal_global.292.67562
+ ___block_literal_global.295
+ ___block_literal_global.295.53018
+ ___block_literal_global.2954
+ ___block_literal_global.297
+ ___block_literal_global.297.55689
+ ___block_literal_global.29806
+ ___block_literal_global.299.53016
+ ___block_literal_global.302
+ ___block_literal_global.302.39372
+ ___block_literal_global.3025
+ ___block_literal_global.304
+ ___block_literal_global.306
+ ___block_literal_global.308.39391
+ ___block_literal_global.31.57594
+ ___block_literal_global.317
+ ___block_literal_global.317.51503
+ ___block_literal_global.31708
+ ___block_literal_global.32106
+ ___block_literal_global.323
+ ___block_literal_global.33125
+ ___block_literal_global.332
+ ___block_literal_global.33380
+ ___block_literal_global.33974
+ ___block_literal_global.340
+ ___block_literal_global.34057
+ ___block_literal_global.346
+ ___block_literal_global.34695
+ ___block_literal_global.34858
+ ___block_literal_global.353
+ ___block_literal_global.35650
+ ___block_literal_global.357
+ ___block_literal_global.359
+ ___block_literal_global.363
+ ___block_literal_global.3635
+ ___block_literal_global.36492
+ ___block_literal_global.365
+ ___block_literal_global.367
+ ___block_literal_global.36785
+ ___block_literal_global.37228
+ ___block_literal_global.373
+ ___block_literal_global.37593
+ ___block_literal_global.38264
+ ___block_literal_global.38415
+ ___block_literal_global.386
+ ___block_literal_global.386.37305
+ ___block_literal_global.38815
+ ___block_literal_global.390
+ ___block_literal_global.39030
+ ___block_literal_global.391
+ ___block_literal_global.39260
+ ___block_literal_global.39492
+ ___block_literal_global.39961
+ ___block_literal_global.40086
+ ___block_literal_global.401
+ ___block_literal_global.40247
+ ___block_literal_global.40459
+ ___block_literal_global.41015
+ ___block_literal_global.411
+ ___block_literal_global.412
+ ___block_literal_global.41483
+ ___block_literal_global.416
+ ___block_literal_global.41705
+ ___block_literal_global.42081
+ ___block_literal_global.42155
+ ___block_literal_global.42699
+ ___block_literal_global.43066
+ ___block_literal_global.43261
+ ___block_literal_global.43503
+ ___block_literal_global.43612
+ ___block_literal_global.4380
+ ___block_literal_global.440
+ ___block_literal_global.44278
+ ___block_literal_global.44332
+ ___block_literal_global.444
+ ___block_literal_global.44560
+ ___block_literal_global.44760
+ ___block_literal_global.4499
+ ___block_literal_global.455
+ ___block_literal_global.46226
+ ___block_literal_global.46438
+ ___block_literal_global.46564
+ ___block_literal_global.46753
+ ___block_literal_global.46850
+ ___block_literal_global.47088
+ ___block_literal_global.47979
+ ___block_literal_global.48001
+ ___block_literal_global.4835
+ ___block_literal_global.485
+ ___block_literal_global.48622
+ ___block_literal_global.48633
+ ___block_literal_global.49245
+ ___block_literal_global.4929
+ ___block_literal_global.49433
+ ___block_literal_global.49769
+ ___block_literal_global.49830
+ ___block_literal_global.50406
+ ___block_literal_global.50559
+ ___block_literal_global.50841
+ ___block_literal_global.51257
+ ___block_literal_global.51506
+ ___block_literal_global.51562
+ ___block_literal_global.5159
+ ___block_literal_global.52170
+ ___block_literal_global.52442
+ ___block_literal_global.52930
+ ___block_literal_global.53110
+ ___block_literal_global.53393
+ ___block_literal_global.5389
+ ___block_literal_global.53941
+ ___block_literal_global.54057
+ ___block_literal_global.54519
+ ___block_literal_global.54716
+ ___block_literal_global.549
+ ___block_literal_global.55742
+ ___block_literal_global.558
+ ___block_literal_global.55845
+ ___block_literal_global.5605
+ ___block_literal_global.562
+ ___block_literal_global.56753
+ ___block_literal_global.57051
+ ___block_literal_global.57405
+ ___block_literal_global.57612
+ ___block_literal_global.57697
+ ___block_literal_global.58239
+ ___block_literal_global.59707
+ ___block_literal_global.59786
+ ___block_literal_global.6.68053
+ ___block_literal_global.60086
+ ___block_literal_global.601
+ ___block_literal_global.60437
+ ___block_literal_global.6059
+ ___block_literal_global.60598
+ ___block_literal_global.61183
+ ___block_literal_global.615
+ ___block_literal_global.61589
+ ___block_literal_global.62265
+ ___block_literal_global.63165
+ ___block_literal_global.63404
+ ___block_literal_global.63442
+ ___block_literal_global.635
+ ___block_literal_global.63756
+ ___block_literal_global.64020
+ ___block_literal_global.64227
+ ___block_literal_global.64546
+ ___block_literal_global.64889
+ ___block_literal_global.65371
+ ___block_literal_global.65493
+ ___block_literal_global.65657
+ ___block_literal_global.658
+ ___block_literal_global.66003
+ ___block_literal_global.66275
+ ___block_literal_global.66342
+ ___block_literal_global.66631
+ ___block_literal_global.67003
+ ___block_literal_global.67407
+ ___block_literal_global.676
+ ___block_literal_global.67638
+ ___block_literal_global.68045
+ ___block_literal_global.688
+ ___block_literal_global.68828
+ ___block_literal_global.693
+ ___block_literal_global.70263
+ ___block_literal_global.705
+ ___block_literal_global.70504
+ ___block_literal_global.70709
+ ___block_literal_global.70900
+ ___block_literal_global.71448
+ ___block_literal_global.72535
+ ___block_literal_global.747
+ ___block_literal_global.751
+ ___block_literal_global.7820
+ ___block_literal_global.784
+ ___block_literal_global.813
+ ___block_literal_global.818
+ ___block_literal_global.8612
+ ___block_literal_global.865.72301
+ ___block_literal_global.870
+ ___block_literal_global.8850
+ ___block_literal_global.887
+ ___block_literal_global.9430
+ ___block_literal_global.967
+ ___getCLPlacemarkClass_block_invoke.56511
+ ___getCLPlacemarkClass_block_invoke.58065
+ ___getCLPlacemarkClass_block_invoke.62246
+ ___getCNContactStoreClass_block_invoke.63406
+ ___getMPMediaItemClass_block_invoke.50574
+ ___getMPMediaPropertyPredicateClass_block_invoke.34754
+ ___getMPMediaPropertyPredicateClass_block_invoke.50572
+ ___getMPMediaQueryClass_block_invoke.34757
+ ___getMPMediaQueryClass_block_invoke.50577
+ __unnamed_array_storage.10393
+ __unnamed_array_storage.12771
+ __unnamed_array_storage.13416
+ __unnamed_array_storage.14681
+ __unnamed_array_storage.15204
+ __unnamed_array_storage.17193
+ __unnamed_array_storage.178.60016
+ __unnamed_array_storage.18180
+ __unnamed_array_storage.183
+ __unnamed_array_storage.184
+ __unnamed_array_storage.184.50854
+ __unnamed_array_storage.196
+ __unnamed_array_storage.196.59256
+ __unnamed_array_storage.197
+ __unnamed_array_storage.208
+ __unnamed_array_storage.213
+ __unnamed_array_storage.213.21631
+ __unnamed_array_storage.215
+ __unnamed_array_storage.21659
+ __unnamed_array_storage.217
+ __unnamed_array_storage.222
+ __unnamed_array_storage.224
+ __unnamed_array_storage.230
+ __unnamed_array_storage.236
+ __unnamed_array_storage.236.29006
+ __unnamed_array_storage.236.44211
+ __unnamed_array_storage.242
+ __unnamed_array_storage.246
+ __unnamed_array_storage.247
+ __unnamed_array_storage.251
+ __unnamed_array_storage.251.44931
+ __unnamed_array_storage.25327
+ __unnamed_array_storage.263
+ __unnamed_array_storage.265
+ __unnamed_array_storage.272
+ __unnamed_array_storage.27947
+ __unnamed_array_storage.28461
+ __unnamed_array_storage.287
+ __unnamed_array_storage.29005
+ __unnamed_array_storage.299
+ __unnamed_array_storage.311
+ __unnamed_array_storage.31753
+ __unnamed_array_storage.32295
+ __unnamed_array_storage.324
+ __unnamed_array_storage.32777
+ __unnamed_array_storage.329
+ __unnamed_array_storage.335
+ __unnamed_array_storage.33716
+ __unnamed_array_storage.34658
+ __unnamed_array_storage.356
+ __unnamed_array_storage.365
+ __unnamed_array_storage.371
+ __unnamed_array_storage.371.71230
+ __unnamed_array_storage.37160
+ __unnamed_array_storage.377
+ __unnamed_array_storage.383
+ __unnamed_array_storage.390
+ __unnamed_array_storage.392
+ __unnamed_array_storage.39620
+ __unnamed_array_storage.401
+ __unnamed_array_storage.407
+ __unnamed_array_storage.41021
+ __unnamed_array_storage.413
+ __unnamed_array_storage.419
+ __unnamed_array_storage.42423
+ __unnamed_array_storage.434
+ __unnamed_array_storage.43475
+ __unnamed_array_storage.440
+ __unnamed_array_storage.44228
+ __unnamed_array_storage.446
+ __unnamed_array_storage.44930
+ __unnamed_array_storage.45231
+ __unnamed_array_storage.457
+ __unnamed_array_storage.458
+ __unnamed_array_storage.465
+ __unnamed_array_storage.47464
+ __unnamed_array_storage.49601
+ __unnamed_array_storage.50853
+ __unnamed_array_storage.51682
+ __unnamed_array_storage.518
+ __unnamed_array_storage.52000
+ __unnamed_array_storage.52803
+ __unnamed_array_storage.54364
+ __unnamed_array_storage.559
+ __unnamed_array_storage.560
+ __unnamed_array_storage.59255
+ __unnamed_array_storage.59923
+ __unnamed_array_storage.60015
+ __unnamed_array_storage.622
+ __unnamed_array_storage.63491
+ __unnamed_array_storage.64035
+ __unnamed_array_storage.64501
+ __unnamed_array_storage.65172
+ __unnamed_array_storage.66152
+ __unnamed_array_storage.66479
+ __unnamed_array_storage.68283
+ __unnamed_array_storage.71285
+ __unnamed_array_storage.842
+ __unnamed_array_storage.864
+ _audit_stringContacts.30424
+ _audit_stringContacts.45406
+ _audit_stringContacts.50839
+ _audit_stringContacts.57672
+ _audit_stringContacts.62291
+ _audit_stringContacts.63423
+ _audit_stringCoreLocation.39473
+ _audit_stringCoreLocation.45421
+ _audit_stringCoreLocation.55860
+ _audit_stringCoreLocation.56527
+ _audit_stringCoreLocation.58081
+ _audit_stringCoreLocation.59849
+ _audit_stringCoreLocation.62262
+ _audit_stringMediaPlayer.34788
+ _audit_stringMediaPlayer.50593
+ _audit_stringRunningBoardServices.25780
+ _audit_stringUIKit.39713
+ _classHFTriggerActionSetsBuilder.33331
+ _classHFTriggerActionSetsBuilder.36507
+ _classRegistrationLock.49146
+ _classRegistrationLock.68396
+ _classUIPasteboard.40259
+ _classUIPasteboard.46566
+ _classUIPasteboard.57407
+ _classUIPasteboard.60600
+ _constantHMCharacteristicMetadataFormatBool.2425
+ _constantHMCharacteristicMetadataFormatBool.26593
+ _constantHMCharacteristicMetadataFormatFloat.2404
+ _constantHMCharacteristicMetadataFormatInt.2411
+ _constantHMCharacteristicMetadataFormatInt.26704
+ _constantHMCharacteristicMetadataFormatString.2418
+ _constantHMCharacteristicMetadataFormatUInt16.2390
+ _constantHMCharacteristicMetadataFormatUInt32.2383
+ _constantHMCharacteristicMetadataFormatUInt64.2373
+ _constantHMCharacteristicMetadataFormatUInt8.2397
+ _constantHMCharacteristicMetadataFormatUInt8.26711
+ _getCLPlacemarkClass.62185
+ _getCLPlacemarkClass.softClass.56510
+ _getCLPlacemarkClass.softClass.58064
+ _getCLPlacemarkClass.softClass.62245
+ _getCNContactStoreClass.softClass.63405
+ _getHFTriggerActionSetsBuilderClass.33319
+ _getHFTriggerActionSetsBuilderClass.36502
+ _getHMCharacteristicMetadataFormatBool.2357
+ _getHMCharacteristicMetadataFormatBool.26588
+ _getHMCharacteristicMetadataFormatFloat.2360
+ _getHMCharacteristicMetadataFormatInt.2359
+ _getHMCharacteristicMetadataFormatInt.26699
+ _getHMCharacteristicMetadataFormatString.2358
+ _getHMCharacteristicMetadataFormatUInt16.2362
+ _getHMCharacteristicMetadataFormatUInt32.2363
+ _getHMCharacteristicMetadataFormatUInt64.2364
+ _getHMCharacteristicMetadataFormatUInt8.2361
+ _getHMCharacteristicMetadataFormatUInt8.26698
+ _getMPMediaItemClass.softClass.50573
+ _getMPMediaPropertyPredicateClass.softClass.34753
+ _getMPMediaPropertyPredicateClass.softClass.50571
+ _getMPMediaQueryClass.softClass.34756
+ _getMPMediaQueryClass.softClass.50576
+ _getUIPasteboardClass.40244
+ _getUIPasteboardClass.46560
+ _getUIPasteboardClass.57398
+ _getUIPasteboardClass.60593
+ _initHFTriggerActionSetsBuilder.33328
+ _initHFTriggerActionSetsBuilder.36504
+ _initHMCharacteristicMetadataFormatBool.2422
+ _initHMCharacteristicMetadataFormatBool.26590
+ _initHMCharacteristicMetadataFormatFloat.2401
+ _initHMCharacteristicMetadataFormatInt.2408
+ _initHMCharacteristicMetadataFormatInt.26701
+ _initHMCharacteristicMetadataFormatString.2415
+ _initHMCharacteristicMetadataFormatUInt16.2387
+ _initHMCharacteristicMetadataFormatUInt32.2380
+ _initHMCharacteristicMetadataFormatUInt64.2366
+ _initHMCharacteristicMetadataFormatUInt8.2394
+ _initHMCharacteristicMetadataFormatUInt8.26708
+ _initUIPasteboard.40257
+ _initUIPasteboard.46562
+ _initUIPasteboard.57403
+ _initUIPasteboard.60596
+ _objc_msgSend$assessmentGestalt
+ _objc_msgSend$assessmentModeManagerDidBecomeActive:
+ _objc_msgSend$externalMetricsActionIdentifier
+ _objc_msgSend$externalMetricsBundleIdentifier
+ _objc_msgSend$initWithQueue:
+ _objc_msgSend$isInAssessmentMode
+ _objc_msgSend$isObserving
+ _objc_msgSend$queryMetadataByAppBundleIdentifier:entityIdentifier:
+ _objc_msgSend$setExternalActionIdentifier:
+ _objc_msgSend$setExternalBundleIdentifier:
+ _objc_msgSend$setIsObserving:
+ _sharedInstance.onceToken.11665
+ _sharedInstance.onceToken.55741
+ _sharedManager.onceToken.1771
+ _sharedManager.onceToken.56765
+ _sharedManager.onceToken.64545
+ _sharedManager.sharedManager.56766
+ _sharedManager.sharedManager.64547
+ _sharedRegistry.onceToken.15205
+ _sharedRegistry.onceToken.23800
+ _sharedRegistry.sharedRegistry.15206
+ _sharedRegistry.sharedRegistry.23801
- GCC_except_table10090
- GCC_except_table10096
- GCC_except_table10214
- GCC_except_table10248
- GCC_except_table10317
- GCC_except_table10324
- GCC_except_table10326
- GCC_except_table10328
- GCC_except_table10356
- GCC_except_table10361
- GCC_except_table10393
- GCC_except_table10396
- GCC_except_table10399
- GCC_except_table10402
- GCC_except_table10586
- GCC_except_table10711
- GCC_except_table10753
- GCC_except_table11078
- GCC_except_table11098
- GCC_except_table11101
- GCC_except_table11188
- GCC_except_table11470
- GCC_except_table11475
- GCC_except_table11478
- GCC_except_table11481
- GCC_except_table11484
- GCC_except_table11489
- GCC_except_table11496
- GCC_except_table11501
- GCC_except_table11504
- GCC_except_table11507
- GCC_except_table11510
- GCC_except_table11513
- GCC_except_table11516
- GCC_except_table11519
- GCC_except_table11522
- GCC_except_table11525
- GCC_except_table11528
- GCC_except_table11531
- GCC_except_table11534
- GCC_except_table11560
- GCC_except_table11562
- GCC_except_table11642
- GCC_except_table11669
- GCC_except_table11674
- GCC_except_table11676
- GCC_except_table11828
- GCC_except_table12017
- GCC_except_table12032
- GCC_except_table12038
- GCC_except_table12040
- GCC_except_table12045
- GCC_except_table12143
- GCC_except_table12155
- GCC_except_table12162
- GCC_except_table12261
- GCC_except_table12347
- GCC_except_table12372
- GCC_except_table12450
- GCC_except_table12482
- GCC_except_table12485
- GCC_except_table12807
- GCC_except_table12840
- GCC_except_table12971
- GCC_except_table13002
- GCC_except_table13008
- GCC_except_table13053
- GCC_except_table13161
- GCC_except_table13176
- GCC_except_table13193
- GCC_except_table13194
- GCC_except_table13195
- GCC_except_table13204
- GCC_except_table13215
- GCC_except_table13405
- GCC_except_table13409
- GCC_except_table13603
- GCC_except_table13670
- GCC_except_table13907
- GCC_except_table13933
- GCC_except_table14036
- GCC_except_table14156
- GCC_except_table14190
- GCC_except_table14195
- GCC_except_table14204
- GCC_except_table14317
- GCC_except_table14340
- GCC_except_table14351
- GCC_except_table14354
- GCC_except_table14656
- GCC_except_table14696
- GCC_except_table14707
- GCC_except_table14721
- GCC_except_table14724
- GCC_except_table14921
- GCC_except_table1629
- GCC_except_table1642
- GCC_except_table1647
- GCC_except_table1935
- GCC_except_table1943
- GCC_except_table1965
- GCC_except_table2118
- GCC_except_table2144
- GCC_except_table2205
- GCC_except_table2242
- GCC_except_table2386
- GCC_except_table2401
- GCC_except_table2489
- GCC_except_table2542
- GCC_except_table2559
- GCC_except_table2565
- GCC_except_table2571
- GCC_except_table2774
- GCC_except_table2775
- GCC_except_table2782
- GCC_except_table2783
- GCC_except_table2784
- GCC_except_table2785
- GCC_except_table2809
- GCC_except_table2837
- GCC_except_table2871
- GCC_except_table2887
- GCC_except_table2948
- GCC_except_table2959
- GCC_except_table2961
- GCC_except_table2964
- GCC_except_table3137
- GCC_except_table3143
- GCC_except_table3437
- GCC_except_table3442
- GCC_except_table3445
- GCC_except_table3830
- GCC_except_table3831
- GCC_except_table3954
- GCC_except_table4055
- GCC_except_table4068
- GCC_except_table4087
- GCC_except_table4095
- GCC_except_table4272
- GCC_except_table4446
- GCC_except_table4452
- GCC_except_table4458
- GCC_except_table4539
- GCC_except_table4546
- GCC_except_table4658
- GCC_except_table4684
- GCC_except_table4728
- GCC_except_table4790
- GCC_except_table4812
- GCC_except_table4852
- GCC_except_table4908
- GCC_except_table4913
- GCC_except_table4915
- GCC_except_table5030
- GCC_except_table5036
- GCC_except_table5052
- GCC_except_table5361
- GCC_except_table5525
- GCC_except_table5585
- GCC_except_table5595
- GCC_except_table5738
- GCC_except_table5772
- GCC_except_table5792
- GCC_except_table5892
- GCC_except_table5932
- GCC_except_table5933
- GCC_except_table5934
- GCC_except_table6032
- GCC_except_table6076
- GCC_except_table6094
- GCC_except_table6120
- GCC_except_table6494
- GCC_except_table6507
- GCC_except_table6551
- GCC_except_table6552
- GCC_except_table6557
- GCC_except_table6558
- GCC_except_table6572
- GCC_except_table6614
- GCC_except_table6619
- GCC_except_table6677
- GCC_except_table7070
- GCC_except_table7165
- GCC_except_table7241
- GCC_except_table7469
- GCC_except_table7512
- GCC_except_table7559
- GCC_except_table7560
- GCC_except_table7624
- GCC_except_table7726
- GCC_except_table7827
- GCC_except_table7882
- GCC_except_table7887
- GCC_except_table8070
- GCC_except_table8077
- GCC_except_table8085
- GCC_except_table8261
- GCC_except_table8262
- GCC_except_table8263
- GCC_except_table8264
- GCC_except_table8265
- GCC_except_table8266
- GCC_except_table8267
- GCC_except_table8268
- GCC_except_table8269
- GCC_except_table8270
- GCC_except_table8271
- GCC_except_table8274
- GCC_except_table8276
- GCC_except_table8288
- GCC_except_table8289
- GCC_except_table8291
- GCC_except_table8294
- GCC_except_table8295
- GCC_except_table8297
- GCC_except_table8299
- GCC_except_table8300
- GCC_except_table8303
- GCC_except_table8382
- GCC_except_table8400
- GCC_except_table8601
- GCC_except_table8737
- GCC_except_table8739
- GCC_except_table8741
- GCC_except_table8748
- GCC_except_table8790
- GCC_except_table8857
- GCC_except_table8863
- GCC_except_table8866
- GCC_except_table8896
- GCC_except_table8946
- GCC_except_table9018
- GCC_except_table9038
- GCC_except_table9064
- GCC_except_table9287
- GCC_except_table9293
- GCC_except_table9295
- GCC_except_table9297
- GCC_except_table9299
- GCC_except_table9301
- GCC_except_table9305
- GCC_except_table9307
- GCC_except_table9326
- GCC_except_table9343
- GCC_except_table9355
- GCC_except_table9414
- GCC_except_table9420
- GCC_except_table9426
- GCC_except_table9438
- GCC_except_table9665
- GCC_except_table9667
- GCC_except_table9668
- GCC_except_table9669
- GCC_except_table9671
- GCC_except_table9673
- GCC_except_table9675
- GCC_except_table9678
- GCC_except_table9686
- GCC_except_table9697
- GCC_except_table9837
- GCC_except_table9842
- GCC_except_table9844
- GCC_except_table9874
- GCC_except_table9886
- GCC_except_table9951
- _AssistantServicesLibrary.sLib.66254
- _AssistantServicesLibrary.sOnce.66253
- _ContactsLibrary.50749
- _ContactsLibrary.63300
- _ContactsLibraryCore.frameworkLibrary.30373
- _ContactsLibraryCore.frameworkLibrary.45352
- _ContactsLibraryCore.frameworkLibrary.50799
- _ContactsLibraryCore.frameworkLibrary.57616
- _ContactsLibraryCore.frameworkLibrary.62237
- _ContactsLibraryCore.frameworkLibrary.63308
- _CoreLocationLibraryCore.frameworkLibrary.39416
- _CoreLocationLibraryCore.frameworkLibrary.45377
- _CoreLocationLibraryCore.frameworkLibrary.55805
- _CoreLocationLibraryCore.frameworkLibrary.56461
- _CoreLocationLibraryCore.frameworkLibrary.58015
- _CoreLocationLibraryCore.frameworkLibrary.59788
- _CoreLocationLibraryCore.frameworkLibrary.62197
- _HFTriggerActionSetsBuilderFunction.33278
- _HFTriggerActionSetsBuilderFunction.36458
- _HMCharacteristicMetadataFormatBoolFunction.2423
- _HMCharacteristicMetadataFormatBoolFunction.26565
- _HMCharacteristicMetadataFormatFloatFunction.2402
- _HMCharacteristicMetadataFormatIntFunction.2409
- _HMCharacteristicMetadataFormatIntFunction.26676
- _HMCharacteristicMetadataFormatStringFunction.2416
- _HMCharacteristicMetadataFormatUInt16Function.2388
- _HMCharacteristicMetadataFormatUInt32Function.2381
- _HMCharacteristicMetadataFormatUInt64Function.2371
- _HMCharacteristicMetadataFormatUInt8Function.2395
- _HMCharacteristicMetadataFormatUInt8Function.26683
- _HomeKitLibrary.sLib.1755
- _HomeKitLibrary.sLib.2364
- _HomeKitLibrary.sLib.26545
- _HomeKitLibrary.sLib.33326
- _HomeKitLibrary.sLib.34008
- _HomeKitLibrary.sLib.36469
- _HomeKitLibrary.sLib.53362
- _HomeKitLibrary.sOnce.1751
- _HomeKitLibrary.sOnce.2363
- _HomeKitLibrary.sOnce.26544
- _HomeKitLibrary.sOnce.33324
- _HomeKitLibrary.sOnce.34001
- _HomeKitLibrary.sOnce.36464
- _HomeKitLibrary.sOnce.53355
- _HomeLibrary.sLib.26690
- _HomeLibrary.sLib.33282
- _HomeLibrary.sLib.36462
- _HomeLibrary.sOnce.26686
- _HomeLibrary.sOnce.33274
- _HomeLibrary.sOnce.36454
- _MediaPlayerLibrary.34722
- _MediaPlayerLibrary.50544
- _MediaPlayerLibraryCore.frameworkLibrary.34731
- _MediaPlayerLibraryCore.frameworkLibrary.50550
- _RunningBoardServicesLibrary.25740
- _RunningBoardServicesLibraryCore.frameworkLibrary.25743
- _SAObjectsLibrary.sLib.66519
- _SAObjectsLibrary.sOnce.66517
- _UIKitLibrary.sLib.15008
- _UIKitLibrary.sLib.21528
- _UIKitLibrary.sLib.26957
- _UIKitLibrary.sLib.27558
- _UIKitLibrary.sLib.40206
- _UIKitLibrary.sLib.46534
- _UIKitLibrary.sLib.55547
- _UIKitLibrary.sLib.57363
- _UIKitLibrary.sLib.60558
- _UIKitLibrary.sOnce.15007
- _UIKitLibrary.sOnce.21521
- _UIKitLibrary.sOnce.26950
- _UIKitLibrary.sOnce.27553
- _UIKitLibrary.sOnce.40204
- _UIKitLibrary.sOnce.46524
- _UIKitLibrary.sOnce.55542
- _UIKitLibrary.sOnce.57353
- _UIKitLibrary.sOnce.60548
- _UIKitLibraryCore.frameworkLibrary.39658
- _UIPasteboardFunction.40219
- _UIPasteboardFunction.46529
- _UIPasteboardFunction.57358
- _UIPasteboardFunction.60553
- _WFActionGreenTeaContentDestinationMayLeaveDevice.onceToken.1358
- _WFEnforceClass.11165
- _WFEnforceClass.1171
- _WFEnforceClass.12312
- _WFEnforceClass.12513
- _WFEnforceClass.14419
- _WFEnforceClass.15424
- _WFEnforceClass.15570
- _WFEnforceClass.15994
- _WFEnforceClass.1667
- _WFEnforceClass.16674
- _WFEnforceClass.20030
- _WFEnforceClass.20266
- _WFEnforceClass.2103
- _WFEnforceClass.21121
- _WFEnforceClass.21916
- _WFEnforceClass.21979
- _WFEnforceClass.23344
- _WFEnforceClass.2341
- _WFEnforceClass.23523
- _WFEnforceClass.27383
- _WFEnforceClass.27652
- _WFEnforceClass.27927
- _WFEnforceClass.28168
- _WFEnforceClass.28856
- _WFEnforceClass.29939
- _WFEnforceClass.30521
- _WFEnforceClass.33464
- _WFEnforceClass.34404
- _WFEnforceClass.3468
- _WFEnforceClass.34989
- _WFEnforceClass.38529
- _WFEnforceClass.40043
- _WFEnforceClass.4066
- _WFEnforceClass.41421
- _WFEnforceClass.43909
- _WFEnforceClass.44331
- _WFEnforceClass.44532
- _WFEnforceClass.44668
- _WFEnforceClass.4531
- _WFEnforceClass.46427
- _WFEnforceClass.47832
- _WFEnforceClass.48313
- _WFEnforceClass.55444
- _WFEnforceClass.57174
- _WFEnforceClass.57880
- _WFEnforceClass.5935
- _WFEnforceClass.59559
- _WFEnforceClass.60042
- _WFEnforceClass.60396
- _WFEnforceClass.61232
- _WFEnforceClass.61892
- _WFEnforceClass.62575
- _WFEnforceClass.63615
- _WFEnforceClass.67491
- _WFEnforceClass.67639
- _WFEnforceClass.68269
- _WFEnforceClass.69516
- _WFEnforceClass.705
- _WFEnforceClass.70727
- _WFEnforceClass.71522
- _WFEnforceClass.7766
- _WFEnforceClass.8192
- _WFEnforceClass.8394
- _WFEnforceClass.8770
- _WFEnforceClass.9444
- _WFGroupingPropertyForMediaType.50539
- _WFShortcutsAppGroupIdentifier
- _WFWorkflowAppGroupIdentifier
- ___100-[WFCloudKitWebServiceRequest fetchProxiedRecordWithIdentifier:possibleItemTypes:completionHandler:]_block_invoke.267
- ___104+[WFOutOfProcessWorkflowController(ContextualActions) computeFinderResizedSizesForImages:inSizes:error:]_block_invoke.164
- ___116-[WFDialogTransformer sequentialParameterInputProvider:didAdvanceToParameter:action:defaultState:prompt:completion:]_block_invoke.339
- ___116-[WFDialogTransformer sequentialParameterInputProvider:didAdvanceToParameter:action:defaultState:prompt:completion:]_block_invoke.341
- ___116-[WFDialogTransformer sequentialParameterInputProvider:didAdvanceToParameter:action:defaultState:prompt:completion:]_block_invoke_2.343
- ___119-[WFConditionalAction predicateForComparisonOperator:rightDate:secondRightDate:comparableTimeUnits:rightDurationValue:]_block_invoke.269
- ___119-[WFConditionalAction predicateForComparisonOperator:rightDate:secondRightDate:comparableTimeUnits:rightDurationValue:]_block_invoke_2.271
- ___119-[WFConditionalAction predicateForComparisonOperator:rightDate:secondRightDate:comparableTimeUnits:rightDurationValue:]_block_invoke_3.272
- ___129-[WFActionDonationRecommender _fetchDonationsWithLimit:applicationBundleIdentifier:includeSuggestedForAllApps:completionHandler:]_block_invoke.177
- ___135-[WFAction presentSmartPromptAuthorizationWithConfiguration:userInterface:databaseApprovalResult:contentDestination:completionHandler:]_block_invoke.649
- ___143-[WFCloudKitItemRequest fetchItemsWithPredicate:itemType:groupName:properties:sortDescriptors:resultsLimit:qualityOfService:completionHandler:]_block_invoke.262
- ___143-[WFCloudKitItemRequest fetchItemsWithPredicate:itemType:groupName:properties:sortDescriptors:resultsLimit:qualityOfService:completionHandler:]_block_invoke_2.264
- ___170-[WFSmartPromptConfiguration initWithSmartPromptStates:attributionSet:previousAttributions:contentItemCache:action:contentDestination:reference:source:isWebpageCoercion:]_block_invoke.181
- ___21-[ICAppRegistry init]_block_invoke.160
- ___24-[WFActionRegistry fill]_block_invoke.186
- ___24-[WFActionRegistry fill]_block_invoke_2.187
- ___31-[WFWorkflow setWorkflowTypes:]_block_invoke.350
- ___35-[WFAction finishRunningWithError:]_block_invoke.703
- ___38-[WFDatabase(Sync) updateWalrusStatus]_block_invoke.271
- ___38-[WFDatabase(Sync) updateWalrusStatus]_block_invoke_2.272
- ___38-[WFWorkflow saveWithCompletionBlock:]_block_invoke.384
- ___39-[WFActionRegistry updateCachesAndFill]_block_invoke.190
- ___39-[WFActionRegistry updateCachesAndFill]_block_invoke.192
- ___39-[WFActionRegistry updateCachesAndFill]_block_invoke_2.193
- ___39-[WFDatabase notifyResultsAboutChange:]_block_invoke.273
- ___43+[WFLinkEntityContentItem propertyBuilders]_block_invoke.209
- ___43+[WFLinkEntityContentItem propertyBuilders]_block_invoke.219
- ___43+[WFLinkEntityContentItem propertyBuilders]_block_invoke.221
- ___44+[WFiTunesObject artworkURLsJSONTransformer]_block_invoke.212
- ___44-[VCCKVoiceShortcutFetcher fetchRecordZones]_block_invoke.171
- ___45-[ICManager performQueuedRequestIfApplicable]_block_invoke.193
- ___45-[WFCloudKitResolveReferencesOperation start]_block_invoke.432
- ___45-[WFCloudKitResolveReferencesOperation start]_block_invoke.433
- ___46-[WFActionRegistry updateCacheWithCompletion:]_block_invoke.205
- ___48+[WFShortcutSigningContext contextWithAuthData:]_block_invoke.172
- ___48-[WFLinkAction runAsynchronouslyWithLinkAction:]_block_invoke.274
- ___49-[VCCKVoiceShortcutFetcher fetchRecordsFromZone:]_block_invoke.179
- ___49-[VCVoiceShortcutPeaceMigrator migrateWithError:]_block_invoke.187
- ___49-[WFUIPresenterXPCConnection initWithConnection:]_block_invoke.155
- ___50-[WFConditionalAction runAsynchronouslyWithInput:]_block_invoke.242
- ___52-[WFHomeWorkflow shortcutsDictionaryRepresentations]_block_invoke.159
- ___53-[WFDatabaseResult updateDescriptorsAndNotify:state:]_block_invoke.168
- ___53-[WFIntentExecutor resolveIntent:withExtensionProxy:]_block_invoke.174
- ___53-[WFIntentExecutor resolveIntent:withExtensionProxy:]_block_invoke_2.176
- ___54-[WFActionRegistry fillActionProviders:updatingCache:]_block_invoke.198
- ___54-[WFActionRegistry fillActionProviders:updatingCache:]_block_invoke.199
- ___54-[WFActionRegistry fillActionProviders:updatingCache:]_block_invoke.203
- ___54-[WFActionRegistry fillActionProviders:updatingCache:]_block_invoke_2.204
- ___54-[WFHandleIntentAction finishRunningByContinuingInApp]_block_invoke.270
- ___55+[WFActionRateLimiter performAction:onQueue:withBlock:]_block_invoke.177
- ___55-[WFOpenUserActivityAction runAsynchronouslyWithInput:]_block_invoke.202
- ___55-[WFWorkflow configureAsSingleStepShortcutIfNecessary:]_block_invoke.423
- ___58-[WFDatabase(Shortcuts) duplicateReference:newName:error:]_block_invoke.316
- ___58-[WFRemoteExecutionRunRequest writeMessageToWriter:error:]_block_invoke.206
- ___59-[WFDialogTransformer showDialogRequest:completionHandler:]_block_invoke.203
- ___59-[WFLinkAction enumeration:localizedLabelForPossibleState:]_block_invoke.409
- ___59-[WFLinkAction getContentDestinationWithCompletionHandler:]_block_invoke.354
- ___60-[WFCloudKitSyncSession applyConflictResolution:inDatabase:]_block_invoke.178
- ___60-[WFLinkContentItemFilterAction runAsynchronouslyWithInput:]_block_invoke.172
- ___62-[WFAction requestInterfacePresentationWithCompletionHandler:]_block_invoke.710
- ___63-[WFDatabase(Library) createLibraryFromCurrentDatabaseSnapshot]_block_invoke.175
- ___63-[WFDatabase(Library) createLibraryFromCurrentDatabaseSnapshot]_block_invoke.179
- ___63-[WFDatabase(Library) createLibraryFromCurrentDatabaseSnapshot]_block_invoke.180
- ___64-[WFSequentialParameterInputProvider askForParameterIfAvailable]_block_invoke.160
- ___65+[WFRemoteWidgetDataProvider handleReceivedData:responseHandler:]_block_invoke.158
- ___66+[INFile(Workflow) coerceContentItems:toSupportedUTIs:completion:]_block_invoke.189
- ___66+[INFile(Workflow) coerceContentItems:toSupportedUTIs:completion:]_block_invoke.191
- ___66+[INFile(Workflow) coerceContentItems:toSupportedUTIs:completion:]_block_invoke_2.190
- ___66-[WFUIPresenterLaunchAngelConnection prepareConnectionIfNecessary]_block_invoke.297
- ___66-[WFUIPresenterLaunchAngelConnection prepareConnectionIfNecessary]_block_invoke.298
- ___68-[WFUIPresenter showDialogRequest:runningContext:completionHandler:]_block_invoke.191
- ___69-[WFRemoteExecutionRunRequest inflateWithFileCoordinator:completion:]_block_invoke.168
- ___69-[WFRemoteExecutionRunRequest inflateWithFileCoordinator:completion:]_block_invoke.170
- ___71-[WFDatabase(Collections) moveReferences:toIndexes:ofCollection:error:]_block_invoke.218
- ___71-[WFDatabase(Collections) moveReferences:toIndexes:ofCollection:error:]_block_invoke.220
- ___71-[WFDatabase(Collections) moveReferences:toIndexes:ofCollection:error:]_block_invoke.224
- ___73-[WFIntentActionProvider createActionsForRequests:forceLocalActionsOnly:]_block_invoke.167
- ___74-[WFAppInstalledResource fetchiTunesStoreObjectForAppWithCompletionBlock:]_block_invoke.168
- ___74-[WFRemoteQuarantinePolicyEvaluator _evaluatePolicyForRequest:completion:]_block_invoke.182
- ___74-[WFRemoteQuarantinePolicyEvaluator _evaluatePolicyForRequest:completion:]_block_invoke.192
- ___74-[WFRemoteQuarantinePolicyEvaluator _evaluatePolicyForRequest:completion:]_block_invoke_2.187
- ___74-[WFRemoteQuarantinePolicyEvaluator _evaluatePolicyForRequest:completion:]_block_invoke_3.189
- ___75+[VCVoiceShortcutPeaceMigrator migrateFromCloudKitIntoDatabaseIfNecessary:]_block_invoke.157
- ___75-[WFRemoteExecutionRunRequest inflateInputData:fileCoordinator:completion:]_block_invoke.185
- ___77-[WFLinkAction fetchMissingDisplayRepresentationValuesWithCompletionHandler:]_block_invoke.387
- ___77-[WFLinkAction fetchMissingDisplayRepresentationValuesWithCompletionHandler:]_block_invoke.394
- ___77-[WFLinkAction fetchMissingDisplayRepresentationValuesWithCompletionHandler:]_block_invoke_2.388
- ___77-[WFLinkAction fetchMissingDisplayRepresentationValuesWithCompletionHandler:]_block_invoke_2.396
- ___77-[WFLinkAction fetchMissingDisplayRepresentationValuesWithCompletionHandler:]_block_invoke_3.401
- ___78-[WFVariable getContentWithContext:trackContentAttribution:completionHandler:]_block_invoke.193
- ___78-[WFVariable getContentWithContext:trackContentAttribution:completionHandler:]_block_invoke_2.194
- ___79-[WFRemoteExecutionRunRequest inflateVariablesData:fileCoordinator:completion:]_block_invoke.178
- ___79-[WFRemoteExecutionRunRequest inflateVariablesData:fileCoordinator:completion:]_block_invoke_2.183
- ___81-[WFShortcutExtractor extractSignedShortcutFile:allowsRetryIfExpired:completion:]_block_invoke.223
- ___82-[WFContextualActionSuggester suggestActionsForContext:numSuggestions:completion:]_block_invoke.227
- ___84-[WFRemoteExecutionRunRequestResponse inflateOutputData:fileCoordinator:completion:]_block_invoke.176
- ___86-[WFAction allowSessionKitSessionsIfNeededWithConfiguration:isManualInvocation:error:]_block_invoke.821
- ___86-[WFAppPickerParameter loadPossibleStatesForEnumeration:searchTerm:completionHandler:]_block_invoke.155
- ___86-[WFDatabase(Collections) moveCollections:toIndexes:ofCollectionWithIdentifier:error:]_block_invoke.252
- ___86-[WFShortcutSigningContext validateSigningCertificateChainWithICloudIdentifier:error:]_block_invoke.222
- ___87-[WFActionRegistry actionProviderDidChange:updatedActions:removedActions:addedActions:]_block_invoke.219
- ___87-[WFRemoteExecutionRunRequestResponse inflateVariablesData:fileCoordinator:completion:]_block_invoke.166
- ___87-[WFRemoteExecutionRunRequestResponse inflateVariablesData:fileCoordinator:completion:]_block_invoke_2.171
- ___88-[WFAction performDataAccessChecksWithUserInterface:contentItemCache:completionHandler:]_block_invoke.632
- ___88-[WFAction performDataAccessChecksWithUserInterface:contentItemCache:completionHandler:]_block_invoke.633
- ___89+[WFOutOfProcessWorkflowController(ContextualActions) contextualActionsForContext:error:]_block_invoke.155
- ___89-[WFCloudKitItemRequest fetchItemWithID:itemType:groupName:properties:completionHandler:]_block_invoke.273
- ___89-[WFRemoteExecutionRunRequest inflateProcessedParametersData:fileCoordinator:completion:]_block_invoke.189
- ___90-[WFCloudKitWebServiceRequest fetchRecordsWithItemType:filter:cacheKey:completionHandler:]_block_invoke.254
- ___90-[WFMultipleValueParameterState processWithContext:userInputRequiredHandler:valueHandler:]_block_invoke.203
- ___90-[WFMultipleValueParameterState processWithContext:userInputRequiredHandler:valueHandler:]_block_invoke_2.206
- ___90-[WFMultipleValueParameterState processWithContext:userInputRequiredHandler:valueHandler:]_block_invoke_3.210
- ___90-[WFMultipleValueParameterState processWithContext:userInputRequiredHandler:valueHandler:]_block_invoke_4.211
- ___90-[WFMultipleValueParameterState processWithContext:userInputRequiredHandler:valueHandler:]_block_invoke_5.214
- ___90-[WFMultipleValueParameterState processWithContext:userInputRequiredHandler:valueHandler:]_block_invoke_6.218
- ___91-[WFCalendarPickerParameter loadPossibleStatesForEnumeration:searchTerm:completionHandler:]_block_invoke.166
- ___94-[WFDynamicResolveParameter(WFParameterPicker) wf_loadStatesWithSearchTerm:completionHandler:]_block_invoke.233
- ___94-[WFDynamicResolveParameter(WFParameterPicker) wf_loadStatesWithSearchTerm:completionHandler:]_block_invoke_2.236
- ___94-[WFLinkActionProvider createActionsForRequests:allowsActionInDenyList:forceLocalActionsOnly:]_block_invoke.173
- ___95-[WFActionDonationRecommender fetchRecommendedDonationsForAppPredictionsWithCompletionHandler:]_block_invoke.196
- ___95-[WFActionDonationRecommender fetchRecommendedDonationsForAppPredictionsWithCompletionHandler:]_block_invoke.203
- ___95-[WFActionDonationRecommender fetchRecommendedDonationsForAppPredictionsWithCompletionHandler:]_block_invoke_2.197
- ___95-[WFActionDonationRecommender fetchRecommendedDonationsForAppPredictionsWithCompletionHandler:]_block_invoke_2.206
- ___95-[WFActionDonationRecommender fetchRecommendedDonationsForAppPredictionsWithCompletionHandler:]_block_invoke_3.208
- ___95-[WFActionDonationRecommender fetchRecommendedDonationsForAppPredictionsWithCompletionHandler:]_block_invoke_4.210
- ___96-[WFActionRegistry createActionsWithIdentifiers:serializedParameterArray:forceLocalActionsOnly:]_block_invoke.173
- ___96-[WFActionRegistry createActionsWithIdentifiers:serializedParameterArray:forceLocalActionsOnly:]_block_invoke_2.175
- ___98+[WFOutOfProcessWorkflowController(ContextualActions) filteredContextualActions:forContext:error:]_block_invoke.160
- ___98-[WFAction runWithInput:userInterface:runningDelegate:variableSource:workQueue:completionHandler:]_block_invoke.571
- ___98-[WFAction runWithInput:userInterface:runningDelegate:variableSource:workQueue:completionHandler:]_block_invoke_2.572
- ___98-[WFAction runWithInput:userInterface:runningDelegate:variableSource:workQueue:completionHandler:]_block_invoke_3.579
- ___99-[WFAction performDeletionAuthorizationChecksWithUserInterface:contentItemCache:completionHandler:]_block_invoke.659
- ___AssistantServicesLibrary_block_invoke.66259
- ___Block_byref_object_copy_.1019
- ___Block_byref_object_copy_.11301
- ___Block_byref_object_copy_.11655
- ___Block_byref_object_copy_.12522
- ___Block_byref_object_copy_.14000
- ___Block_byref_object_copy_.15003
- ___Block_byref_object_copy_.16809
- ___Block_byref_object_copy_.16911
- ___Block_byref_object_copy_.18125
- ___Block_byref_object_copy_.19058
- ___Block_byref_object_copy_.19491
- ___Block_byref_object_copy_.20890
- ___Block_byref_object_copy_.23089
- ___Block_byref_object_copy_.23728
- ___Block_byref_object_copy_.25763
- ___Block_byref_object_copy_.27542
- ___Block_byref_object_copy_.2759
- ___Block_byref_object_copy_.28247
- ___Block_byref_object_copy_.29907
- ___Block_byref_object_copy_.3037
- ___Block_byref_object_copy_.33034
- ___Block_byref_object_copy_.33307
- ___Block_byref_object_copy_.34743
- ___Block_byref_object_copy_.35593
- ___Block_byref_object_copy_.36784
- ___Block_byref_object_copy_.38756
- ___Block_byref_object_copy_.39239
- ___Block_byref_object_copy_.39885
- ___Block_byref_object_copy_.40198
- ___Block_byref_object_copy_.41301
- ___Block_byref_object_copy_.43973
- ___Block_byref_object_copy_.44136
- ___Block_byref_object_copy_.44504
- ___Block_byref_object_copy_.46409
- ___Block_byref_object_copy_.46866
- ___Block_byref_object_copy_.4788
- ___Block_byref_object_copy_.51225
- ___Block_byref_object_copy_.5176
- ___Block_byref_object_copy_.52972
- ___Block_byref_object_copy_.53743
- ___Block_byref_object_copy_.54213
- ___Block_byref_object_copy_.54827
- ___Block_byref_object_copy_.55851
- ___Block_byref_object_copy_.56362
- ___Block_byref_object_copy_.56899
- ___Block_byref_object_copy_.57518
- ___Block_byref_object_copy_.60139
- ___Block_byref_object_copy_.6046
- ___Block_byref_object_copy_.60870
- ___Block_byref_object_copy_.61211
- ___Block_byref_object_copy_.62339
- ___Block_byref_object_copy_.64352
- ___Block_byref_object_copy_.66232
- ___Block_byref_object_copy_.66959
- ___Block_byref_object_copy_.67877
- ___Block_byref_object_copy_.68654
- ___Block_byref_object_copy_.70332
- ___Block_byref_object_copy_.773
- ___Block_byref_object_copy_.7748
- ___Block_byref_object_copy_.8873
- ___Block_byref_object_copy_.8924
- ___Block_byref_object_copy_.9512
- ___Block_byref_object_copy_.9812
- ___Block_byref_object_dispose_.1020
- ___Block_byref_object_dispose_.11302
- ___Block_byref_object_dispose_.11656
- ___Block_byref_object_dispose_.12523
- ___Block_byref_object_dispose_.14001
- ___Block_byref_object_dispose_.15004
- ___Block_byref_object_dispose_.16810
- ___Block_byref_object_dispose_.16912
- ___Block_byref_object_dispose_.18126
- ___Block_byref_object_dispose_.19059
- ___Block_byref_object_dispose_.19492
- ___Block_byref_object_dispose_.20891
- ___Block_byref_object_dispose_.23090
- ___Block_byref_object_dispose_.23729
- ___Block_byref_object_dispose_.25764
- ___Block_byref_object_dispose_.27543
- ___Block_byref_object_dispose_.2760
- ___Block_byref_object_dispose_.28248
- ___Block_byref_object_dispose_.29908
- ___Block_byref_object_dispose_.3038
- ___Block_byref_object_dispose_.33035
- ___Block_byref_object_dispose_.33308
- ___Block_byref_object_dispose_.34744
- ___Block_byref_object_dispose_.35594
- ___Block_byref_object_dispose_.36785
- ___Block_byref_object_dispose_.38757
- ___Block_byref_object_dispose_.39240
- ___Block_byref_object_dispose_.39886
- ___Block_byref_object_dispose_.40199
- ___Block_byref_object_dispose_.41302
- ___Block_byref_object_dispose_.43974
- ___Block_byref_object_dispose_.44137
- ___Block_byref_object_dispose_.44505
- ___Block_byref_object_dispose_.46410
- ___Block_byref_object_dispose_.46867
- ___Block_byref_object_dispose_.4789
- ___Block_byref_object_dispose_.51226
- ___Block_byref_object_dispose_.5177
- ___Block_byref_object_dispose_.52973
- ___Block_byref_object_dispose_.53744
- ___Block_byref_object_dispose_.54214
- ___Block_byref_object_dispose_.54828
- ___Block_byref_object_dispose_.55852
- ___Block_byref_object_dispose_.56363
- ___Block_byref_object_dispose_.56900
- ___Block_byref_object_dispose_.57519
- ___Block_byref_object_dispose_.60140
- ___Block_byref_object_dispose_.6047
- ___Block_byref_object_dispose_.60871
- ___Block_byref_object_dispose_.61212
- ___Block_byref_object_dispose_.62340
- ___Block_byref_object_dispose_.64353
- ___Block_byref_object_dispose_.66233
- ___Block_byref_object_dispose_.66960
- ___Block_byref_object_dispose_.67878
- ___Block_byref_object_dispose_.68655
- ___Block_byref_object_dispose_.70333
- ___Block_byref_object_dispose_.774
- ___Block_byref_object_dispose_.7749
- ___Block_byref_object_dispose_.8874
- ___Block_byref_object_dispose_.8925
- ___Block_byref_object_dispose_.9513
- ___Block_byref_object_dispose_.9813
- ___ContactsLibraryCore_block_invoke.30374
- ___ContactsLibraryCore_block_invoke.45353
- ___ContactsLibraryCore_block_invoke.50800
- ___ContactsLibraryCore_block_invoke.57617
- ___ContactsLibraryCore_block_invoke.62238
- ___ContactsLibraryCore_block_invoke.63309
- ___CoreLocationLibraryCore_block_invoke.39417
- ___CoreLocationLibraryCore_block_invoke.45378
- ___CoreLocationLibraryCore_block_invoke.55806
- ___CoreLocationLibraryCore_block_invoke.56462
- ___CoreLocationLibraryCore_block_invoke.58016
- ___CoreLocationLibraryCore_block_invoke.59789
- ___CoreLocationLibraryCore_block_invoke.62198
- ___HomeKitLibrary_block_invoke.1753
- ___HomeKitLibrary_block_invoke.2373
- ___HomeKitLibrary_block_invoke.26550
- ___HomeKitLibrary_block_invoke.33332
- ___HomeKitLibrary_block_invoke.34006
- ___HomeKitLibrary_block_invoke.36467
- ___HomeKitLibrary_block_invoke.53360
- ___HomeLibrary_block_invoke.26688
- ___HomeLibrary_block_invoke.33280
- ___HomeLibrary_block_invoke.36460
- ___MediaPlayerLibraryCore_block_invoke.34732
- ___MediaPlayerLibraryCore_block_invoke.50551
- ___RunningBoardServicesLibraryCore_block_invoke.25744
- ___SAObjectsLibrary_block_invoke.66523
- ___UIKitLibraryCore_block_invoke.39659
- ___UIKitLibrary_block_invoke.15011
- ___UIKitLibrary_block_invoke.21526
- ___UIKitLibrary_block_invoke.26955
- ___UIKitLibrary_block_invoke.27556
- ___UIKitLibrary_block_invoke.40212
- ___UIKitLibrary_block_invoke.46532
- ___UIKitLibrary_block_invoke.55545
- ___UIKitLibrary_block_invoke.57361
- ___UIKitLibrary_block_invoke.60556
- ___WFContentPredicateForRowTemplateValue_block_invoke.217
- ___WFContentSelectionActionParameterDefinitions_block_invoke.278
- ___WFContentSelectionActionParameterDefinitions_block_invoke_2.280
- ___WFLNPropertyQueryForRowTemplateValue_block_invoke.166
- ___WFSearchActionsWithKeywords_block_invoke.228
- ___WFShowResult_block_invoke.169
- ___WFShowResult_block_invoke_2.171
- ___WFShowResult_block_invoke_3.174
- ___WFUpdateSmartPromptChangesToShortcutChanges_block_invoke.545
- ___block_literal_global.1011
- ___block_literal_global.10122
- ___block_literal_global.10411
- ___block_literal_global.11308
- ___block_literal_global.11674
- ___block_literal_global.1194
- ___block_literal_global.12321
- ___block_literal_global.12529
- ___block_literal_global.12727
- ___block_literal_global.12834
- ___block_literal_global.13324
- ___block_literal_global.13405
- ___block_literal_global.1353
- ___block_literal_global.1358
- ___block_literal_global.13606
- ___block_literal_global.14447
- ___block_literal_global.145
- ___block_literal_global.146
- ___block_literal_global.14653
- ___block_literal_global.14974
- ___block_literal_global.154
- ___block_literal_global.154.21227
- ___block_literal_global.155
- ___block_literal_global.155.21802
- ___block_literal_global.158.21803
- ___block_literal_global.160
- ___block_literal_global.160.37550
- ___block_literal_global.160.65537
- ___block_literal_global.160.70349
- ___block_literal_global.162
- ___block_literal_global.162.33923
- ___block_literal_global.162.42036
- ___block_literal_global.162.4497
- ___block_literal_global.1636
- ___block_literal_global.165.49397
- ___block_literal_global.165.70376
- ___block_literal_global.168.70377
- ___block_literal_global.169
- ___block_literal_global.16952
- ___block_literal_global.171.56703
- ___block_literal_global.171.70722
- ___block_literal_global.173
- ___block_literal_global.174.27437
- ___block_literal_global.175.72150
- ___block_literal_global.1764
- ___block_literal_global.17658
- ___block_literal_global.17725
- ___block_literal_global.178.23526
- ___block_literal_global.178.23733
- ___block_literal_global.178.46430
- ___block_literal_global.178.72152
- ___block_literal_global.180.25808
- ___block_literal_global.18032
- ___block_literal_global.181.11298
- ___block_literal_global.181.16933
- ___block_literal_global.181.23734
- ___block_literal_global.181.54021
- ___block_literal_global.183.41647
- ___block_literal_global.18350
- ___block_literal_global.1863
- ___block_literal_global.191
- ___block_literal_global.191.49199
- ___block_literal_global.194.27432
- ___block_literal_global.195
- ___block_literal_global.195.50523
- ___block_literal_global.196
- ___block_literal_global.196.23694
- ___block_literal_global.197.64775
- ___block_literal_global.198.42002
- ___block_literal_global.19847
- ___block_literal_global.201.61575
- ___block_literal_global.202
- ___block_literal_global.202.50518
- ___block_literal_global.206
- ___block_literal_global.20695
- ___block_literal_global.209.70318
- ___block_literal_global.211
- ___block_literal_global.21111
- ___block_literal_global.21278
- ___block_literal_global.213
- ___block_literal_global.213.65243
- ___block_literal_global.215
- ___block_literal_global.21522
- ___block_literal_global.21593
- ___block_literal_global.21801
- ___block_literal_global.220
- ___block_literal_global.221
- ___block_literal_global.222.64374
- ___block_literal_global.22400
- ___block_literal_global.226
- ___block_literal_global.226.24462
- ___block_literal_global.226.34576
- ___block_literal_global.226.65241
- ___block_literal_global.227
- ___block_literal_global.228
- ___block_literal_global.228.72094
- ___block_literal_global.23107
- ___block_literal_global.233.52136
- ___block_literal_global.23365
- ___block_literal_global.2348
- ___block_literal_global.23528
- ___block_literal_global.23669
- ___block_literal_global.239
- ___block_literal_global.23977
- ___block_literal_global.241.23112
- ___block_literal_global.242
- ___block_literal_global.24461
- ___block_literal_global.24748
- ___block_literal_global.248
- ___block_literal_global.2508
- ___block_literal_global.25094
- ___block_literal_global.251.44243
- ___block_literal_global.25329
- ___block_literal_global.255
- ___block_literal_global.25805
- ___block_literal_global.261
- ___block_literal_global.26154
- ___block_literal_global.265
- ___block_literal_global.26539
- ___block_literal_global.266
- ___block_literal_global.267
- ___block_literal_global.26951
- ___block_literal_global.274
- ___block_literal_global.27448
- ___block_literal_global.2752
- ___block_literal_global.27545
- ___block_literal_global.276
- ___block_literal_global.27654
- ___block_literal_global.278
- ___block_literal_global.279.67459
- ___block_literal_global.27906
- ___block_literal_global.28231
- ___block_literal_global.286
- ___block_literal_global.287
- ___block_literal_global.288
- ___block_literal_global.288.6144
- ___block_literal_global.289.67450
- ___block_literal_global.29085
- ___block_literal_global.292.52982
- ___block_literal_global.294
- ___block_literal_global.294.55638
- ___block_literal_global.2950
- ___block_literal_global.296
- ___block_literal_global.296.52980
- ___block_literal_global.29770
- ___block_literal_global.298
- ___block_literal_global.299.39331
- ___block_literal_global.300
- ___block_literal_global.3021
- ___block_literal_global.305
- ___block_literal_global.305.39350
- ___block_literal_global.31.57543
- ___block_literal_global.314.51467
- ___block_literal_global.31672
- ___block_literal_global.320
- ___block_literal_global.32051
- ___block_literal_global.329
- ___block_literal_global.33070
- ___block_literal_global.331
- ___block_literal_global.33325
- ___block_literal_global.33919
- ___block_literal_global.34002
- ___block_literal_global.343
- ___block_literal_global.34641
- ___block_literal_global.34808
- ___block_literal_global.350
- ___block_literal_global.354
- ___block_literal_global.356
- ___block_literal_global.35600
- ___block_literal_global.360
- ___block_literal_global.362
- ___block_literal_global.3631
- ___block_literal_global.364
- ___block_literal_global.36441
- ___block_literal_global.36734
- ___block_literal_global.370
- ___block_literal_global.37190
- ___block_literal_global.37549
- ___block_literal_global.38222
- ___block_literal_global.383
- ___block_literal_global.383.37267
- ___block_literal_global.38373
- ___block_literal_global.387
- ___block_literal_global.38773
- ___block_literal_global.388
- ___block_literal_global.38988
- ___block_literal_global.392
- ___block_literal_global.39218
- ___block_literal_global.39451
- ___block_literal_global.39920
- ___block_literal_global.40044
- ___block_literal_global.40205
- ___block_literal_global.40417
- ___block_literal_global.406
- ___block_literal_global.408
- ___block_literal_global.40972
- ___block_literal_global.413
- ___block_literal_global.41438
- ___block_literal_global.41658
- ___block_literal_global.42035
- ___block_literal_global.42110
- ___block_literal_global.42654
- ___block_literal_global.43021
- ___block_literal_global.43216
- ___block_literal_global.434
- ___block_literal_global.43458
- ___block_literal_global.43567
- ___block_literal_global.4383
- ___block_literal_global.441
- ___block_literal_global.44233
- ___block_literal_global.44287
- ___block_literal_global.44515
- ___block_literal_global.44719
- ___block_literal_global.4502
- ___block_literal_global.452
- ___block_literal_global.46187
- ___block_literal_global.46399
- ___block_literal_global.46525
- ___block_literal_global.46714
- ___block_literal_global.46811
- ___block_literal_global.47049
- ___block_literal_global.47940
- ___block_literal_global.47962
- ___block_literal_global.4839
- ___block_literal_global.484
- ___block_literal_global.48585
- ___block_literal_global.48596
- ___block_literal_global.49208
- ___block_literal_global.4933
- ___block_literal_global.49396
- ___block_literal_global.49732
- ___block_literal_global.49793
- ___block_literal_global.50369
- ___block_literal_global.50522
- ___block_literal_global.50805
- ___block_literal_global.51221
- ___block_literal_global.51470
- ___block_literal_global.51526
- ___block_literal_global.5164
- ___block_literal_global.52134
- ___block_literal_global.52406
- ___block_literal_global.52894
- ___block_literal_global.53074
- ___block_literal_global.53356
- ___block_literal_global.53904
- ___block_literal_global.5391
- ___block_literal_global.54020
- ___block_literal_global.54483
- ___block_literal_global.546
- ___block_literal_global.54668
- ___block_literal_global.552
- ___block_literal_global.55691
- ___block_literal_global.55794
- ___block_literal_global.559
- ___block_literal_global.5607
- ___block_literal_global.56702
- ___block_literal_global.57000
- ___block_literal_global.57354
- ___block_literal_global.57561
- ___block_literal_global.57646
- ___block_literal_global.58188
- ___block_literal_global.59660
- ___block_literal_global.59739
- ___block_literal_global.598
- ___block_literal_global.6.67898
- ___block_literal_global.60039
- ___block_literal_global.60388
- ___block_literal_global.60549
- ___block_literal_global.6060
- ___block_literal_global.61134
- ___block_literal_global.612
- ___block_literal_global.61540
- ___block_literal_global.62215
- ___block_literal_global.63056
- ___block_literal_global.631
- ___block_literal_global.63296
- ___block_literal_global.63334
- ___block_literal_global.63648
- ___block_literal_global.63908
- ___block_literal_global.64114
- ___block_literal_global.64433
- ___block_literal_global.64774
- ___block_literal_global.652
- ___block_literal_global.65256
- ___block_literal_global.65378
- ___block_literal_global.65542
- ___block_literal_global.65888
- ___block_literal_global.66162
- ___block_literal_global.66229
- ___block_literal_global.66518
- ___block_literal_global.66891
- ___block_literal_global.670
- ___block_literal_global.67295
- ___block_literal_global.67526
- ___block_literal_global.67890
- ___block_literal_global.685
- ___block_literal_global.68673
- ___block_literal_global.690
- ___block_literal_global.70106
- ___block_literal_global.702
- ___block_literal_global.70347
- ___block_literal_global.70552
- ___block_literal_global.70743
- ___block_literal_global.71291
- ___block_literal_global.72361
- ___block_literal_global.744
- ___block_literal_global.748
- ___block_literal_global.777
- ___block_literal_global.7821
- ___block_literal_global.810
- ___block_literal_global.815
- ___block_literal_global.855
- ___block_literal_global.860
- ___block_literal_global.8615
- ___block_literal_global.884
- ___block_literal_global.8855
- ___block_literal_global.9435
- ___block_literal_global.964
- ___getCLPlacemarkClass_block_invoke.56460
- ___getCLPlacemarkClass_block_invoke.58014
- ___getCLPlacemarkClass_block_invoke.62196
- ___getCNContactStoreClass_block_invoke.63298
- ___getMPMediaItemClass_block_invoke.50538
- ___getMPMediaPropertyPredicateClass_block_invoke.34701
- ___getMPMediaPropertyPredicateClass_block_invoke.50536
- ___getMPMediaQueryClass_block_invoke.34704
- ___getMPMediaQueryClass_block_invoke.50541
- __unnamed_array_storage.10398
- __unnamed_array_storage.12779
- __unnamed_array_storage.13423
- __unnamed_array_storage.14674
- __unnamed_array_storage.15198
- __unnamed_array_storage.17188
- __unnamed_array_storage.175.59969
- __unnamed_array_storage.175.66001
- __unnamed_array_storage.177
- __unnamed_array_storage.181.50818
- __unnamed_array_storage.18146
- __unnamed_array_storage.193
- __unnamed_array_storage.193.59209
- __unnamed_array_storage.194
- __unnamed_array_storage.202
- __unnamed_array_storage.210
- __unnamed_array_storage.210.21596
- __unnamed_array_storage.211
- __unnamed_array_storage.212
- __unnamed_array_storage.21624
- __unnamed_array_storage.218
- __unnamed_array_storage.219
- __unnamed_array_storage.227
- __unnamed_array_storage.233
- __unnamed_array_storage.233.28979
- __unnamed_array_storage.233.44166
- __unnamed_array_storage.237
- __unnamed_array_storage.239
- __unnamed_array_storage.244
- __unnamed_array_storage.248
- __unnamed_array_storage.248.44891
- __unnamed_array_storage.25294
- __unnamed_array_storage.260
- __unnamed_array_storage.262
- __unnamed_array_storage.269
- __unnamed_array_storage.27918
- __unnamed_array_storage.284
- __unnamed_array_storage.28434
- __unnamed_array_storage.28978
- __unnamed_array_storage.296
- __unnamed_array_storage.308
- __unnamed_array_storage.31717
- __unnamed_array_storage.321
- __unnamed_array_storage.32240
- __unnamed_array_storage.326
- __unnamed_array_storage.32722
- __unnamed_array_storage.332
- __unnamed_array_storage.33661
- __unnamed_array_storage.34604
- __unnamed_array_storage.347
- __unnamed_array_storage.362
- __unnamed_array_storage.368
- __unnamed_array_storage.368.71073
- __unnamed_array_storage.37116
- __unnamed_array_storage.374
- __unnamed_array_storage.380
- __unnamed_array_storage.385
- __unnamed_array_storage.386
- __unnamed_array_storage.387
- __unnamed_array_storage.39579
- __unnamed_array_storage.398
- __unnamed_array_storage.404
- __unnamed_array_storage.40978
- __unnamed_array_storage.410
- __unnamed_array_storage.416
- __unnamed_array_storage.42378
- __unnamed_array_storage.431
- __unnamed_array_storage.43430
- __unnamed_array_storage.437
- __unnamed_array_storage.44183
- __unnamed_array_storage.443
- __unnamed_array_storage.44890
- __unnamed_array_storage.45192
- __unnamed_array_storage.455
- __unnamed_array_storage.462
- __unnamed_array_storage.47425
- __unnamed_array_storage.49564
- __unnamed_array_storage.50817
- __unnamed_array_storage.515
- __unnamed_array_storage.51646
- __unnamed_array_storage.51964
- __unnamed_array_storage.52767
- __unnamed_array_storage.54328
- __unnamed_array_storage.556
- __unnamed_array_storage.557
- __unnamed_array_storage.59208
- __unnamed_array_storage.59876
- __unnamed_array_storage.59968
- __unnamed_array_storage.618
- __unnamed_array_storage.63383
- __unnamed_array_storage.63923
- __unnamed_array_storage.64388
- __unnamed_array_storage.65057
- __unnamed_array_storage.66040
- __unnamed_array_storage.66366
- __unnamed_array_storage.68128
- __unnamed_array_storage.71128
- __unnamed_array_storage.839
- __unnamed_array_storage.854
- _audit_stringContacts.30388
- _audit_stringContacts.45367
- _audit_stringContacts.50803
- _audit_stringContacts.57621
- _audit_stringContacts.62241
- _audit_stringContacts.63315
- _audit_stringCoreLocation.39432
- _audit_stringCoreLocation.45382
- _audit_stringCoreLocation.55809
- _audit_stringCoreLocation.56476
- _audit_stringCoreLocation.58030
- _audit_stringCoreLocation.59802
- _audit_stringCoreLocation.62212
- _audit_stringMediaPlayer.34738
- _audit_stringMediaPlayer.50557
- _audit_stringRunningBoardServices.25747
- _audit_stringUIKit.39672
- _classHFTriggerActionSetsBuilder.33276
- _classHFTriggerActionSetsBuilder.36456
- _classRegistrationLock.49109
- _classRegistrationLock.68241
- _classUIPasteboard.40217
- _classUIPasteboard.46527
- _classUIPasteboard.57356
- _classUIPasteboard.60551
- _constantHMCharacteristicMetadataFormatBool.2421
- _constantHMCharacteristicMetadataFormatBool.26563
- _constantHMCharacteristicMetadataFormatFloat.2400
- _constantHMCharacteristicMetadataFormatInt.2407
- _constantHMCharacteristicMetadataFormatInt.26674
- _constantHMCharacteristicMetadataFormatString.2414
- _constantHMCharacteristicMetadataFormatUInt16.2386
- _constantHMCharacteristicMetadataFormatUInt32.2379
- _constantHMCharacteristicMetadataFormatUInt64.2369
- _constantHMCharacteristicMetadataFormatUInt8.2393
- _constantHMCharacteristicMetadataFormatUInt8.26681
- _getCLPlacemarkClass.62133
- _getCLPlacemarkClass.softClass.56459
- _getCLPlacemarkClass.softClass.58013
- _getCLPlacemarkClass.softClass.62195
- _getCNContactStoreClass.softClass.63297
- _getHFTriggerActionSetsBuilderClass.33264
- _getHFTriggerActionSetsBuilderClass.36451
- _getHMCharacteristicMetadataFormatBool.2353
- _getHMCharacteristicMetadataFormatBool.26558
- _getHMCharacteristicMetadataFormatFloat.2356
- _getHMCharacteristicMetadataFormatInt.2355
- _getHMCharacteristicMetadataFormatInt.26669
- _getHMCharacteristicMetadataFormatString.2354
- _getHMCharacteristicMetadataFormatUInt16.2358
- _getHMCharacteristicMetadataFormatUInt32.2359
- _getHMCharacteristicMetadataFormatUInt64.2360
- _getHMCharacteristicMetadataFormatUInt8.2357
- _getHMCharacteristicMetadataFormatUInt8.26668
- _getMPMediaItemClass.softClass.50537
- _getMPMediaPropertyPredicateClass.softClass.34700
- _getMPMediaPropertyPredicateClass.softClass.50535
- _getMPMediaQueryClass.softClass.34703
- _getMPMediaQueryClass.softClass.50540
- _getUIPasteboardClass.40202
- _getUIPasteboardClass.46521
- _getUIPasteboardClass.57347
- _getUIPasteboardClass.60544
- _initHFTriggerActionSetsBuilder.33273
- _initHFTriggerActionSetsBuilder.36453
- _initHMCharacteristicMetadataFormatBool.2418
- _initHMCharacteristicMetadataFormatBool.26560
- _initHMCharacteristicMetadataFormatFloat.2397
- _initHMCharacteristicMetadataFormatInt.2404
- _initHMCharacteristicMetadataFormatInt.26671
- _initHMCharacteristicMetadataFormatString.2411
- _initHMCharacteristicMetadataFormatUInt16.2383
- _initHMCharacteristicMetadataFormatUInt32.2376
- _initHMCharacteristicMetadataFormatUInt64.2362
- _initHMCharacteristicMetadataFormatUInt8.2390
- _initHMCharacteristicMetadataFormatUInt8.26678
- _initUIPasteboard.40215
- _initUIPasteboard.46523
- _initUIPasteboard.57352
- _initUIPasteboard.60547
- _sharedInstance.onceToken.11673
- _sharedInstance.onceToken.55690
- _sharedManager.onceToken.1763
- _sharedManager.onceToken.56714
- _sharedManager.onceToken.64432
- _sharedManager.sharedManager.56715
- _sharedManager.sharedManager.64434
- _sharedRegistry.onceToken.15199
- _sharedRegistry.onceToken.23765
- _sharedRegistry.sharedRegistry.15200
- _sharedRegistry.sharedRegistry.23766
CStrings:
+ "%s %lu queries returned for %@ in %@"
+ "-[WFLinkActionProvider queryMetadataByAppBundleIdentifier:entityIdentifier:]"
+ "@\"<WFAssessmentModeManagerDelegate>\""
+ "@\"AEAssessmentModeGestalt\""
+ "B16@?0@\"LNQueryMetadata\"8"
+ "ShortcutSourceActiveStarterShortcut"
+ "T@\"<WFAssessmentModeManagerDelegate>\",W,N,V_delegate"
+ "T@\"AEAssessmentModeGestalt\",R,N,V_assessmentGestalt"
+ "T@\"NSString\",&,N,V_externalActionIdentifier"
+ "T@\"NSString\",&,N,V_externalBundleIdentifier"
+ "T@\"NSString\",C,N,V_externalActionIdentifier"
+ "T@\"NSString\",C,N,V_externalBundleIdentifier"
+ "TB,N,V_isObserving"
+ "T{os_unfair_lock_s=I},R,N,V_isObservingLock"
+ "WFAssessmentModeManager"
+ "WFCloudKitLibraryFetched"
+ "WFSyncUnavailableMessageCount"
+ "WFSyncUnavailableMessageDate"
+ "WFSyncUnavailableMessageDismissedByUser"
+ "_assessmentGestalt"
+ "_externalActionIdentifier"
+ "_externalBundleIdentifier"
+ "_isObserving"
+ "_isObservingLock"
+ "active"
+ "assessmentGestalt"
+ "assessmentModeManagerDidBecomeActive:"
+ "externalActionIdentifier"
+ "externalBundleIdentifier"
+ "externalMetricsActionIdentifier"
+ "externalMetricsBundleIdentifier"
+ "hasExternalActionIdentifier"
+ "hasExternalBundleIdentifier"
+ "initWithQueue:"
+ "initWithQueue:delegate:"
+ "isAssessmentModeSupportedOnCurrentDevice"
+ "isInAssessmentMode"
+ "isObserving"
+ "isObservingLock"
+ "queryMetadataByAppBundleIdentifier:entityIdentifier:"
+ "setExternalActionIdentifier:"
+ "setExternalBundleIdentifier:"
+ "setIsObserving:"
+ "startObservingForAssesmentModeChangesIfNeeded"
+ "v24@0:8@\"LNActionExecutor\"16"

```
