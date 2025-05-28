## WorkflowKit

> `/System/Library/PrivateFrameworks/WorkflowKit.framework/WorkflowKit`

```diff

-2038.0.1.10.0
-  __TEXT.__text: 0x2ec14c
-  __TEXT.__auth_stubs: 0x3410
-  __TEXT.__objc_methlist: 0x27e30
+2106.100.3.1.0
+  __TEXT.__text: 0x2eb9c0
+  __TEXT.__auth_stubs: 0x3430
+  __TEXT.__objc_methlist: 0x27c20
   __TEXT.__const: 0x30c0
-  __TEXT.__cstring: 0x3476d
+  __TEXT.__cstring: 0x3438f
   __TEXT.__constg_swiftt: 0xf38
   __TEXT.__swift5_typeref: 0x1ce7
   __TEXT.__swift5_builtin: 0xa0

   __TEXT.__swift5_protos: 0x1c
   __TEXT.__swift5_capture: 0x594
   __TEXT.__swift5_mpenum: 0x20
-  __TEXT.__gcc_except_tab: 0x3654
-  __TEXT.__oslogstring: 0x117e3
-  __TEXT.__dlopen_cstrs: 0xde2
-  __TEXT.__ustring: 0x3642
-  __TEXT.__unwind_info: 0xbb74
-  __TEXT.__eh_frame: 0x43b0
-  __TEXT.__objc_classname: 0x747f
-  __TEXT.__objc_methname: 0x4deb8
-  __TEXT.__objc_methtype: 0x84e1
-  __TEXT.__objc_stubs: 0x31780
-  __DATA_CONST.__got: 0xdc8
-  __DATA_CONST.__const: 0xd108
-  __DATA_CONST.__objc_classlist: 0x1d38
+  __TEXT.__gcc_except_tab: 0x3690
+  __TEXT.__oslogstring: 0x118dc
+  __TEXT.__dlopen_cstrs: 0xd80
+  __TEXT.__ustring: 0x3656
+  __TEXT.__unwind_info: 0xbb24
+  __TEXT.__eh_frame: 0x43d8
+  __TEXT.__objc_classname: 0x73c8
+  __TEXT.__objc_methname: 0x4ddbe
+  __TEXT.__objc_methtype: 0x84cc
+  __TEXT.__objc_stubs: 0x315e0
+  __DATA_CONST.__got: 0xdc0
+  __DATA_CONST.__const: 0xd030
+  __DATA_CONST.__objc_classlist: 0x1d10
   __DATA_CONST.__objc_catlist: 0x368
-  __DATA_CONST.__objc_protolist: 0x3e8
+  __DATA_CONST.__objc_protolist: 0x3e0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x372d8
-  __DATA_CONST.__objc_selrefs: 0xf8a0
-  __DATA_CONST.__objc_arraydata: 0x12e8
-  __AUTH_CONST.__const: 0x5f30
+  __DATA_CONST.__objc_const: 0x36f88
+  __DATA_CONST.__objc_selrefs: 0xf840
+  __DATA_CONST.__objc_arraydata: 0x12c8
+  __AUTH_CONST.__const: 0x5ed0
   __AUTH_CONST.__auth_ptr: 0xb8
-  __AUTH_CONST.__objc_const: 0x19508
-  __AUTH_CONST.__cfstring: 0x272a0
+  __AUTH_CONST.__objc_const: 0x19280
+  __AUTH_CONST.__cfstring: 0x27160
   __AUTH_CONST.__objc_intobj: 0x12a8
   __AUTH_CONST.__objc_arrayobj: 0x9d8
   __AUTH_CONST.__objc_dictobj: 0x2a8
   __AUTH_CONST.__objc_doubleobj: 0x20
-  __AUTH_CONST.__auth_got: 0x1a20
-  __AUTH.__objc_data: 0xd5e0
+  __AUTH_CONST.__auth_got: 0x1a30
+  __AUTH.__objc_data: 0xd450
   __AUTH.__data: 0xc50
   __DATA.__objc_protorefs: 0xf0
-  __DATA.__objc_classrefs: 0x24f8
-  __DATA.__objc_superrefs: 0x11e8
-  __DATA.__objc_ivar: 0x261c
-  __DATA.__data: 0x3d40
-  __DATA.__bss: 0x49f8
+  __DATA.__objc_classrefs: 0x24f0
+  __DATA.__objc_superrefs: 0x11d8
+  __DATA.__objc_ivar: 0x2604
+  __DATA.__data: 0x3ce8
+  __DATA.__bss: 0x49a0
   __DATA.__common: 0x38
   __DATA_DIRTY.__objc_data: 0x53a0
   __DATA_DIRTY.__data: 0x710

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 17885
-  Symbols:   51858
-  CStrings:  21607
+  Functions: 17828
+  Symbols:   51659
+  CStrings:  21555
 
Symbols:
+ +[WFAppInFocusTrigger isSupportedOnThisDevice]
+ +[WFArriveLocationTrigger isSupportedOnThisDevice]
+ +[WFLeaveLocationTrigger isSupportedOnThisDevice]
+ +[WFPredictedLocationTransitionTrigger isSupportedOnThisDevice]
+ +[WFSmartPromptStringGenerator localizedOutputContentDescriptionWithContentCollection:]
+ -[LNImage(Workflow) contextualActionIcon]
+ -[WFDatabase(PersistedSerializedParameters) badgeTypeForEntityIdentifier:error:]
+ -[WFDatabase(PersistedSerializedParameters) storeSerializedParameters:forIdentifier:queryName:badgeType:error:]
+ -[WFDatabase(SmartPrompts) saveOutputActionSmartPromtDataForWorkflowReference:error:]
+ -[WFDatabaseProxy saveOutputActionSmartPromtDataForWorkflowReference:error:]
+ -[WFDialogTransformer allowsHandoff]
+ -[WFDialogTransformer presentAlertWithSmartPromptConfiguration:completionHandler:]
+ -[WFDialogTransformer presentationMode]
+ -[WFDialogTransformer setAllowsHandoff:]
+ -[WFDialogTransformer setPresentationMode:]
+ -[WFFocusConfigurationLinkAction disabledOnPlatforms]
+ -[WFHandleIntentAction disabledOnPlatforms]
+ -[WFLinkAction supportedAppIdentifiers]
+ -[WFLinkMusicRecognitionRecognizeMusicAction disabledOnPlatforms]
+ -[WFResourceManager stateLock]
+ -[WFResourceManager targetSelectorLock]
+ -[WFSmartPromptConfiguration initWithOutputContentCollection:reference:source:]
+ -[WFVariableString processIntoStringsAndAttachmentsWithContext:options:completionHandler:]
+ -[WFWorkflowController lastExecutedAction]
+ -[WFWorkflowController setLastExecutedAction:]
+ GCC_except_table10089
+ GCC_except_table10095
+ GCC_except_table10213
+ GCC_except_table10316
+ GCC_except_table10323
+ GCC_except_table10325
+ GCC_except_table10327
+ GCC_except_table10355
+ GCC_except_table10360
+ GCC_except_table10392
+ GCC_except_table10395
+ GCC_except_table10398
+ GCC_except_table10401
+ GCC_except_table10582
+ GCC_except_table10707
+ GCC_except_table10749
+ GCC_except_table11074
+ GCC_except_table11094
+ GCC_except_table11097
+ GCC_except_table11113
+ GCC_except_table11184
+ GCC_except_table11470
+ GCC_except_table11475
+ GCC_except_table11478
+ GCC_except_table11481
+ GCC_except_table11484
+ GCC_except_table11489
+ GCC_except_table11496
+ GCC_except_table11501
+ GCC_except_table11507
+ GCC_except_table11510
+ GCC_except_table11513
+ GCC_except_table11516
+ GCC_except_table11519
+ GCC_except_table11522
+ GCC_except_table11525
+ GCC_except_table11528
+ GCC_except_table11531
+ GCC_except_table11534
+ GCC_except_table11560
+ GCC_except_table11642
+ GCC_except_table11669
+ GCC_except_table11674
+ GCC_except_table11676
+ GCC_except_table1170
+ GCC_except_table11816
+ GCC_except_table11831
+ GCC_except_table11984
+ GCC_except_table11999
+ GCC_except_table12005
+ GCC_except_table12007
+ GCC_except_table12012
+ GCC_except_table12110
+ GCC_except_table12122
+ GCC_except_table12129
+ GCC_except_table12228
+ GCC_except_table12314
+ GCC_except_table12339
+ GCC_except_table1241
+ GCC_except_table12417
+ GCC_except_table12448
+ GCC_except_table12451
+ GCC_except_table12772
+ GCC_except_table12805
+ GCC_except_table12936
+ GCC_except_table12974
+ GCC_except_table12980
+ GCC_except_table13133
+ GCC_except_table13147
+ GCC_except_table13164
+ GCC_except_table13165
+ GCC_except_table13166
+ GCC_except_table13175
+ GCC_except_table13186
+ GCC_except_table13376
+ GCC_except_table13380
+ GCC_except_table1344
+ GCC_except_table1349
+ GCC_except_table13574
+ GCC_except_table13641
+ GCC_except_table13882
+ GCC_except_table13908
+ GCC_except_table14011
+ GCC_except_table14128
+ GCC_except_table14162
+ GCC_except_table14167
+ GCC_except_table14176
+ GCC_except_table14289
+ GCC_except_table14312
+ GCC_except_table14323
+ GCC_except_table14326
+ GCC_except_table14644
+ GCC_except_table14684
+ GCC_except_table14695
+ GCC_except_table14709
+ GCC_except_table14712
+ GCC_except_table14909
+ GCC_except_table1633
+ GCC_except_table1646
+ GCC_except_table1651
+ GCC_except_table1655
+ GCC_except_table1938
+ GCC_except_table1946
+ GCC_except_table1968
+ GCC_except_table2121
+ GCC_except_table2146
+ GCC_except_table2207
+ GCC_except_table2244
+ GCC_except_table2393
+ GCC_except_table2408
+ GCC_except_table2495
+ GCC_except_table2548
+ GCC_except_table2565
+ GCC_except_table2571
+ GCC_except_table2577
+ GCC_except_table2788
+ GCC_except_table2789
+ GCC_except_table2796
+ GCC_except_table2797
+ GCC_except_table2798
+ GCC_except_table2799
+ GCC_except_table2823
+ GCC_except_table2827
+ GCC_except_table2851
+ GCC_except_table2885
+ GCC_except_table2901
+ GCC_except_table2905
+ GCC_except_table2961
+ GCC_except_table2972
+ GCC_except_table2974
+ GCC_except_table2977
+ GCC_except_table3150
+ GCC_except_table3154
+ GCC_except_table318
+ GCC_except_table321
+ GCC_except_table3447
+ GCC_except_table3452
+ GCC_except_table3455
+ GCC_except_table377
+ GCC_except_table3840
+ GCC_except_table3841
+ GCC_except_table3964
+ GCC_except_table4064
+ GCC_except_table4077
+ GCC_except_table4096
+ GCC_except_table4104
+ GCC_except_table4281
+ GCC_except_table4455
+ GCC_except_table4461
+ GCC_except_table4467
+ GCC_except_table4557
+ GCC_except_table4669
+ GCC_except_table4695
+ GCC_except_table4699
+ GCC_except_table4739
+ GCC_except_table4801
+ GCC_except_table4823
+ GCC_except_table4863
+ GCC_except_table4919
+ GCC_except_table4924
+ GCC_except_table4926
+ GCC_except_table494
+ GCC_except_table497
+ GCC_except_table5041
+ GCC_except_table5047
+ GCC_except_table5063
+ GCC_except_table5372
+ GCC_except_table5536
+ GCC_except_table5596
+ GCC_except_table5606
+ GCC_except_table5748
+ GCC_except_table5782
+ GCC_except_table5802
+ GCC_except_table5902
+ GCC_except_table5943
+ GCC_except_table5944
+ GCC_except_table5945
+ GCC_except_table6043
+ GCC_except_table606
+ GCC_except_table6087
+ GCC_except_table6105
+ GCC_except_table6131
+ GCC_except_table6505
+ GCC_except_table6518
+ GCC_except_table6562
+ GCC_except_table6563
+ GCC_except_table6568
+ GCC_except_table6569
+ GCC_except_table6572
+ GCC_except_table6578
+ GCC_except_table6583
+ GCC_except_table6625
+ GCC_except_table6630
+ GCC_except_table6688
+ GCC_except_table7078
+ GCC_except_table7088
+ GCC_except_table7176
+ GCC_except_table7252
+ GCC_except_table7479
+ GCC_except_table7522
+ GCC_except_table7569
+ GCC_except_table7570
+ GCC_except_table7634
+ GCC_except_table7736
+ GCC_except_table7837
+ GCC_except_table7892
+ GCC_except_table7897
+ GCC_except_table7908
+ GCC_except_table803
+ GCC_except_table8080
+ GCC_except_table8087
+ GCC_except_table8095
+ GCC_except_table8271
+ GCC_except_table8272
+ GCC_except_table8273
+ GCC_except_table8274
+ GCC_except_table8275
+ GCC_except_table8276
+ GCC_except_table8277
+ GCC_except_table8278
+ GCC_except_table8279
+ GCC_except_table8280
+ GCC_except_table8281
+ GCC_except_table8284
+ GCC_except_table8286
+ GCC_except_table8287
+ GCC_except_table8290
+ GCC_except_table8295
+ GCC_except_table8296
+ GCC_except_table8298
+ GCC_except_table8299
+ GCC_except_table8300
+ GCC_except_table8301
+ GCC_except_table8302
+ GCC_except_table8303
+ GCC_except_table8304
+ GCC_except_table8305
+ GCC_except_table8306
+ GCC_except_table8307
+ GCC_except_table8394
+ GCC_except_table8412
+ GCC_except_table8608
+ GCC_except_table871
+ GCC_except_table8744
+ GCC_except_table8746
+ GCC_except_table8748
+ GCC_except_table8755
+ GCC_except_table8797
+ GCC_except_table880
+ GCC_except_table8864
+ GCC_except_table8870
+ GCC_except_table8873
+ GCC_except_table8903
+ GCC_except_table8953
+ GCC_except_table9025
+ GCC_except_table9045
+ GCC_except_table9071
+ GCC_except_table9294
+ GCC_except_table9300
+ GCC_except_table9302
+ GCC_except_table9304
+ GCC_except_table9306
+ GCC_except_table9308
+ GCC_except_table9312
+ GCC_except_table9314
+ GCC_except_table9322
+ GCC_except_table9332
+ GCC_except_table9349
+ GCC_except_table9361
+ GCC_except_table9416
+ GCC_except_table9422
+ GCC_except_table9428
+ GCC_except_table9440
+ GCC_except_table9667
+ GCC_except_table9669
+ GCC_except_table9670
+ GCC_except_table9671
+ GCC_except_table9673
+ GCC_except_table9675
+ GCC_except_table9677
+ GCC_except_table9680
+ GCC_except_table9685
+ GCC_except_table9688
+ GCC_except_table9699
+ GCC_except_table9837
+ GCC_except_table9842
+ GCC_except_table9844
+ GCC_except_table9874
+ GCC_except_table9886
+ GCC_except_table9950
+ _AssistantServicesLibrary.sLib.65951
+ _AssistantServicesLibrary.sOnce.65950
+ _ContactsLibrary.50634
+ _ContactsLibrary.62970
+ _ContactsLibraryCore.frameworkLibrary.30300
+ _ContactsLibraryCore.frameworkLibrary.45244
+ _ContactsLibraryCore.frameworkLibrary.50684
+ _ContactsLibraryCore.frameworkLibrary.57320
+ _ContactsLibraryCore.frameworkLibrary.61898
+ _ContactsLibraryCore.frameworkLibrary.62978
+ _CoreLocationLibraryCore.frameworkLibrary.39362
+ _CoreLocationLibraryCore.frameworkLibrary.45269
+ _CoreLocationLibraryCore.frameworkLibrary.55502
+ _CoreLocationLibraryCore.frameworkLibrary.56157
+ _CoreLocationLibraryCore.frameworkLibrary.57717
+ _CoreLocationLibraryCore.frameworkLibrary.59422
+ _CoreLocationLibraryCore.frameworkLibrary.61858
+ _HFTriggerActionSetsBuilderFunction.33197
+ _HFTriggerActionSetsBuilderFunction.36363
+ _HMCharacteristicMetadataFormatBoolFunction.2403
+ _HMCharacteristicMetadataFormatBoolFunction.26517
+ _HMCharacteristicMetadataFormatFloatFunction.2382
+ _HMCharacteristicMetadataFormatIntFunction.2389
+ _HMCharacteristicMetadataFormatIntFunction.26628
+ _HMCharacteristicMetadataFormatStringFunction.2396
+ _HMCharacteristicMetadataFormatUInt16Function.2368
+ _HMCharacteristicMetadataFormatUInt32Function.2361
+ _HMCharacteristicMetadataFormatUInt64Function.2351
+ _HMCharacteristicMetadataFormatUInt8Function.2375
+ _HMCharacteristicMetadataFormatUInt8Function.26635
+ _HomeKitLibrary.sLib.1741
+ _HomeKitLibrary.sLib.2344
+ _HomeKitLibrary.sLib.26497
+ _HomeKitLibrary.sLib.33245
+ _HomeKitLibrary.sLib.33924
+ _HomeKitLibrary.sLib.36374
+ _HomeKitLibrary.sLib.53289
+ _HomeKitLibrary.sOnce.1737
+ _HomeKitLibrary.sOnce.2343
+ _HomeKitLibrary.sOnce.26496
+ _HomeKitLibrary.sOnce.33243
+ _HomeKitLibrary.sOnce.33917
+ _HomeKitLibrary.sOnce.36369
+ _HomeKitLibrary.sOnce.53282
+ _HomeLibrary.sLib.26642
+ _HomeLibrary.sLib.33201
+ _HomeLibrary.sLib.36367
+ _HomeLibrary.sOnce.26638
+ _HomeLibrary.sOnce.33193
+ _HomeLibrary.sOnce.36359
+ _MediaPlayerLibrary.34634
+ _MediaPlayerLibrary.50428
+ _MediaPlayerLibraryCore.frameworkLibrary.34644
+ _MediaPlayerLibraryCore.frameworkLibrary.50434
+ _OBJC_CLASS_$_VCAccessSpecifier
+ _OBJC_IVAR_$_WFDialogTransformer._allowsHandoff
+ _OBJC_IVAR_$_WFDialogTransformer._presentationMode
+ _OBJC_IVAR_$_WFLinkAction._connectionLock
+ _OBJC_IVAR_$_WFResourceManager._stateLock
+ _OBJC_IVAR_$_WFResourceManager._targetSelectorLock
+ _OBJC_IVAR_$_WFWorkflowController._lastExecutedAction
+ _RunningBoardServicesLibrary.25696
+ _RunningBoardServicesLibraryCore.frameworkLibrary.25699
+ _SAObjectsLibrary.sLib.66215
+ _SAObjectsLibrary.sOnce.66213
+ _UIKitLibrary.sLib.15034
+ _UIKitLibrary.sLib.21502
+ _UIKitLibrary.sLib.26907
+ _UIKitLibrary.sLib.27501
+ _UIKitLibrary.sLib.40160
+ _UIKitLibrary.sLib.46426
+ _UIKitLibrary.sLib.55244
+ _UIKitLibrary.sLib.57061
+ _UIKitLibrary.sLib.60188
+ _UIKitLibrary.sOnce.15033
+ _UIKitLibrary.sOnce.21495
+ _UIKitLibrary.sOnce.26900
+ _UIKitLibrary.sOnce.27496
+ _UIKitLibrary.sOnce.40158
+ _UIKitLibrary.sOnce.46416
+ _UIKitLibrary.sOnce.55239
+ _UIKitLibrary.sOnce.57051
+ _UIKitLibrary.sOnce.60178
+ _UIKitLibraryCore.frameworkLibrary.39610
+ _UIPasteboardFunction.40173
+ _UIPasteboardFunction.46421
+ _UIPasteboardFunction.57056
+ _UIPasteboardFunction.60183
+ _VCBundleIdentifierShortcutsTopHitExtensionHostApp
+ _WFEnforceClass.11214
+ _WFEnforceClass.1180
+ _WFEnforceClass.12356
+ _WFEnforceClass.12554
+ _WFEnforceClass.14424
+ _WFEnforceClass.15448
+ _WFEnforceClass.15594
+ _WFEnforceClass.16014
+ _WFEnforceClass.1665
+ _WFEnforceClass.16690
+ _WFEnforceClass.20012
+ _WFEnforceClass.20242
+ _WFEnforceClass.2088
+ _WFEnforceClass.21094
+ _WFEnforceClass.21877
+ _WFEnforceClass.21939
+ _WFEnforceClass.2321
+ _WFEnforceClass.23297
+ _WFEnforceClass.23476
+ _WFEnforceClass.27327
+ _WFEnforceClass.27595
+ _WFEnforceClass.27869
+ _WFEnforceClass.28105
+ _WFEnforceClass.28785
+ _WFEnforceClass.29851
+ _WFEnforceClass.30447
+ _WFEnforceClass.33382
+ _WFEnforceClass.34320
+ _WFEnforceClass.3433
+ _WFEnforceClass.34899
+ _WFEnforceClass.38477
+ _WFEnforceClass.39997
+ _WFEnforceClass.4036
+ _WFEnforceClass.41344
+ _WFEnforceClass.43796
+ _WFEnforceClass.44224
+ _WFEnforceClass.44424
+ _WFEnforceClass.44559
+ _WFEnforceClass.4505
+ _WFEnforceClass.46321
+ _WFEnforceClass.47720
+ _WFEnforceClass.48199
+ _WFEnforceClass.55141
+ _WFEnforceClass.56871
+ _WFEnforceClass.57583
+ _WFEnforceClass.59193
+ _WFEnforceClass.5948
+ _WFEnforceClass.59673
+ _WFEnforceClass.60027
+ _WFEnforceClass.60903
+ _WFEnforceClass.61562
+ _WFEnforceClass.62247
+ _WFEnforceClass.63285
+ _WFEnforceClass.67183
+ _WFEnforceClass.67334
+ _WFEnforceClass.67963
+ _WFEnforceClass.69208
+ _WFEnforceClass.70490
+ _WFEnforceClass.71285
+ _WFEnforceClass.7138
+ _WFEnforceClass.7749
+ _WFEnforceClass.7957
+ _WFEnforceClass.8213
+ _WFEnforceClass.8434
+ _WFEnforceClass.8812
+ _WFEnforceClass.9464
+ _WFGetBootSessionUUID
+ _WFGroupingPropertyForMediaType.50422
+ ___111-[WFDatabase(PersistedSerializedParameters) storeSerializedParameters:forIdentifier:queryName:badgeType:error:]_block_invoke
+ ___116-[WFDialogTransformer sequentialParameterInputProvider:didAdvanceToParameter:action:defaultState:prompt:completion:]_block_invoke.335
+ ___116-[WFDialogTransformer sequentialParameterInputProvider:didAdvanceToParameter:action:defaultState:prompt:completion:]_block_invoke.337
+ ___116-[WFDialogTransformer sequentialParameterInputProvider:didAdvanceToParameter:action:defaultState:prompt:completion:]_block_invoke_2.339
+ ___135-[WFAction presentSmartPromptAuthorizationWithConfiguration:userInterface:databaseApprovalResult:contentDestination:completionHandler:]_block_invoke.645
+ ___26-[WFLinkAction connection]_block_invoke
+ ___35-[WFAction finishRunningWithError:]_block_invoke.699
+ ___41-[LNImage(Workflow) contextualActionIcon]_block_invoke
+ ___41-[WFLinkAction linkActionWithParameters:]_block_invoke
+ ___48-[WFLinkAction runAsynchronouslyWithLinkAction:]_block_invoke.268
+ ___54-[WFHandleIntentAction finishRunningByContinuingInApp]_block_invoke.267
+ ___58-[WFWorkflow databaseDidChange:modified:inserted:removed:]_block_invoke_2
+ ___59-[WFDialogTransformer showDialogRequest:completionHandler:]_block_invoke.200
+ ___59-[WFLinkAction enumeration:localizedLabelForPossibleState:]_block_invoke.403
+ ___59-[WFLinkAction getContentDestinationWithCompletionHandler:]_block_invoke.348
+ ___62-[WFAction requestInterfacePresentationWithCompletionHandler:]_block_invoke.706
+ ___73-[WFLinkActionProvider enumMetadataByAppBundleIdentifier:enumIdentifier:]_block_invoke
+ ___76-[WFDatabaseProxy saveOutputActionSmartPromtDataForWorkflowReference:error:]_block_invoke
+ ___76-[WFDatabaseProxy saveOutputActionSmartPromtDataForWorkflowReference:error:]_block_invoke_2
+ ___77-[WFLinkAction fetchMissingDisplayRepresentationValuesWithCompletionHandler:]_block_invoke.381
+ ___77-[WFLinkAction fetchMissingDisplayRepresentationValuesWithCompletionHandler:]_block_invoke.388
+ ___77-[WFLinkAction fetchMissingDisplayRepresentationValuesWithCompletionHandler:]_block_invoke_2.382
+ ___77-[WFLinkAction fetchMissingDisplayRepresentationValuesWithCompletionHandler:]_block_invoke_2.390
+ ___77-[WFLinkAction fetchMissingDisplayRepresentationValuesWithCompletionHandler:]_block_invoke_3.395
+ ___80-[WFDatabase(PersistedSerializedParameters) badgeTypeForEntityIdentifier:error:]_block_invoke
+ ___82-[WFDialogTransformer presentAlertWithSmartPromptConfiguration:completionHandler:]_block_invoke
+ ___87+[WFSmartPromptStringGenerator localizedOutputContentDescriptionWithContentCollection:]_block_invoke
+ ___88-[WFAction performDataAccessChecksWithUserInterface:contentItemCache:completionHandler:]_block_invoke.628
+ ___88-[WFAction performDataAccessChecksWithUserInterface:contentItemCache:completionHandler:]_block_invoke.629
+ ___90-[WFVariableString processIntoStringsAndAttachmentsWithContext:options:completionHandler:]_block_invoke
+ ___90-[WFVariableString processIntoStringsAndAttachmentsWithContext:options:completionHandler:]_block_invoke_2
+ ___90-[WFVariableString processIntoStringsAndAttachmentsWithContext:options:completionHandler:]_block_invoke_3
+ ___90-[WFVariableString processIntoStringsAndAttachmentsWithContext:options:completionHandler:]_block_invoke_4
+ ___90-[WFVariableString processIntoStringsAndAttachmentsWithContext:options:completionHandler:]_block_invoke_5
+ ___99-[WFAction performDeletionAuthorizationChecksWithUserInterface:contentItemCache:completionHandler:]_block_invoke.655
+ ___AssistantServicesLibrary_block_invoke.65956
+ ___Block_byref_object_copy_.1016
+ ___Block_byref_object_copy_.11351
+ ___Block_byref_object_copy_.11702
+ ___Block_byref_object_copy_.12560
+ ___Block_byref_object_copy_.14002
+ ___Block_byref_object_copy_.15029
+ ___Block_byref_object_copy_.16824
+ ___Block_byref_object_copy_.16927
+ ___Block_byref_object_copy_.18115
+ ___Block_byref_object_copy_.19047
+ ___Block_byref_object_copy_.19471
+ ___Block_byref_object_copy_.20862
+ ___Block_byref_object_copy_.23042
+ ___Block_byref_object_copy_.23678
+ ___Block_byref_object_copy_.25720
+ ___Block_byref_object_copy_.2743
+ ___Block_byref_object_copy_.27485
+ ___Block_byref_object_copy_.28178
+ ___Block_byref_object_copy_.29819
+ ___Block_byref_object_copy_.3018
+ ___Block_byref_object_copy_.32954
+ ___Block_byref_object_copy_.33226
+ ___Block_byref_object_copy_.34656
+ ___Block_byref_object_copy_.35502
+ ___Block_byref_object_copy_.36693
+ ___Block_byref_object_copy_.38705
+ ___Block_byref_object_copy_.39187
+ ___Block_byref_object_copy_.39838
+ ___Block_byref_object_copy_.40152
+ ___Block_byref_object_copy_.41221
+ ___Block_byref_object_copy_.43850
+ ___Block_byref_object_copy_.44033
+ ___Block_byref_object_copy_.44396
+ ___Block_byref_object_copy_.46303
+ ___Block_byref_object_copy_.46758
+ ___Block_byref_object_copy_.4759
+ ___Block_byref_object_copy_.51109
+ ___Block_byref_object_copy_.5153
+ ___Block_byref_object_copy_.52894
+ ___Block_byref_object_copy_.53669
+ ___Block_byref_object_copy_.54137
+ ___Block_byref_object_copy_.54691
+ ___Block_byref_object_copy_.55548
+ ___Block_byref_object_copy_.56058
+ ___Block_byref_object_copy_.56595
+ ___Block_byref_object_copy_.57214
+ ___Block_byref_object_copy_.59770
+ ___Block_byref_object_copy_.60499
+ ___Block_byref_object_copy_.6059
+ ___Block_byref_object_copy_.60882
+ ___Block_byref_object_copy_.62003
+ ___Block_byref_object_copy_.64036
+ ___Block_byref_object_copy_.65929
+ ___Block_byref_object_copy_.66653
+ ___Block_byref_object_copy_.67571
+ ___Block_byref_object_copy_.68347
+ ___Block_byref_object_copy_.70097
+ ___Block_byref_object_copy_.7737
+ ___Block_byref_object_copy_.8914
+ ___Block_byref_object_copy_.8965
+ ___Block_byref_object_copy_.9526
+ ___Block_byref_object_copy_.9827
+ ___Block_byref_object_dispose_.1017
+ ___Block_byref_object_dispose_.11352
+ ___Block_byref_object_dispose_.11703
+ ___Block_byref_object_dispose_.12561
+ ___Block_byref_object_dispose_.14003
+ ___Block_byref_object_dispose_.15030
+ ___Block_byref_object_dispose_.16825
+ ___Block_byref_object_dispose_.16928
+ ___Block_byref_object_dispose_.18116
+ ___Block_byref_object_dispose_.19048
+ ___Block_byref_object_dispose_.19472
+ ___Block_byref_object_dispose_.20863
+ ___Block_byref_object_dispose_.23043
+ ___Block_byref_object_dispose_.23679
+ ___Block_byref_object_dispose_.25721
+ ___Block_byref_object_dispose_.2744
+ ___Block_byref_object_dispose_.27486
+ ___Block_byref_object_dispose_.28179
+ ___Block_byref_object_dispose_.29820
+ ___Block_byref_object_dispose_.3019
+ ___Block_byref_object_dispose_.32955
+ ___Block_byref_object_dispose_.33227
+ ___Block_byref_object_dispose_.34657
+ ___Block_byref_object_dispose_.35503
+ ___Block_byref_object_dispose_.36694
+ ___Block_byref_object_dispose_.38706
+ ___Block_byref_object_dispose_.39188
+ ___Block_byref_object_dispose_.39839
+ ___Block_byref_object_dispose_.40153
+ ___Block_byref_object_dispose_.41222
+ ___Block_byref_object_dispose_.43851
+ ___Block_byref_object_dispose_.44034
+ ___Block_byref_object_dispose_.44397
+ ___Block_byref_object_dispose_.46304
+ ___Block_byref_object_dispose_.46759
+ ___Block_byref_object_dispose_.4760
+ ___Block_byref_object_dispose_.51110
+ ___Block_byref_object_dispose_.5154
+ ___Block_byref_object_dispose_.52895
+ ___Block_byref_object_dispose_.53670
+ ___Block_byref_object_dispose_.54138
+ ___Block_byref_object_dispose_.54692
+ ___Block_byref_object_dispose_.55549
+ ___Block_byref_object_dispose_.56059
+ ___Block_byref_object_dispose_.56596
+ ___Block_byref_object_dispose_.57215
+ ___Block_byref_object_dispose_.59771
+ ___Block_byref_object_dispose_.60500
+ ___Block_byref_object_dispose_.6060
+ ___Block_byref_object_dispose_.60883
+ ___Block_byref_object_dispose_.62004
+ ___Block_byref_object_dispose_.64037
+ ___Block_byref_object_dispose_.65930
+ ___Block_byref_object_dispose_.66654
+ ___Block_byref_object_dispose_.67572
+ ___Block_byref_object_dispose_.68348
+ ___Block_byref_object_dispose_.70098
+ ___Block_byref_object_dispose_.7738
+ ___Block_byref_object_dispose_.8915
+ ___Block_byref_object_dispose_.8966
+ ___Block_byref_object_dispose_.9527
+ ___Block_byref_object_dispose_.9828
+ ___ContactsLibraryCore_block_invoke.30301
+ ___ContactsLibraryCore_block_invoke.45245
+ ___ContactsLibraryCore_block_invoke.50685
+ ___ContactsLibraryCore_block_invoke.57321
+ ___ContactsLibraryCore_block_invoke.61899
+ ___ContactsLibraryCore_block_invoke.62979
+ ___CoreLocationLibraryCore_block_invoke.39363
+ ___CoreLocationLibraryCore_block_invoke.45270
+ ___CoreLocationLibraryCore_block_invoke.55503
+ ___CoreLocationLibraryCore_block_invoke.56158
+ ___CoreLocationLibraryCore_block_invoke.57718
+ ___CoreLocationLibraryCore_block_invoke.59423
+ ___CoreLocationLibraryCore_block_invoke.61859
+ ___HomeKitLibrary_block_invoke.1740
+ ___HomeKitLibrary_block_invoke.2353
+ ___HomeKitLibrary_block_invoke.26502
+ ___HomeKitLibrary_block_invoke.33251
+ ___HomeKitLibrary_block_invoke.33922
+ ___HomeKitLibrary_block_invoke.36372
+ ___HomeKitLibrary_block_invoke.53287
+ ___HomeLibrary_block_invoke.26640
+ ___HomeLibrary_block_invoke.33199
+ ___HomeLibrary_block_invoke.36365
+ ___MediaPlayerLibraryCore_block_invoke.34645
+ ___MediaPlayerLibraryCore_block_invoke.50435
+ ___RunningBoardServicesLibraryCore_block_invoke.25700
+ ___SAObjectsLibrary_block_invoke.66219
+ ___UIKitLibraryCore_block_invoke.39611
+ ___UIKitLibrary_block_invoke.15037
+ ___UIKitLibrary_block_invoke.21500
+ ___UIKitLibrary_block_invoke.26905
+ ___UIKitLibrary_block_invoke.27499
+ ___UIKitLibrary_block_invoke.40166
+ ___UIKitLibrary_block_invoke.46424
+ ___UIKitLibrary_block_invoke.55242
+ ___UIKitLibrary_block_invoke.57059
+ ___UIKitLibrary_block_invoke.60186
+ ___block_descriptor_40_e8_32s_e24_B16?0"LNEnumMetadata"8ls32l8
+ ___block_descriptor_48_e8_32s40bs_e38_v24?0"<LNDialogResult>"8"NSError"16ls40l8s32l8
+ ___block_descriptor_64_e8_32s40s48s56bs_e29_v24?0"NSArray"8"NSError"16ls56l8s32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48s56s_e61_v40?0"<WFVariableStringContent>"8Q16?<v?"NSError">24^B32ls32l8s40l8s48l8s56l8
+ ___block_descriptor_72_e8_32s40s48s56s_e9_16?0^8ls32l8s40l8s48l8s56l8
+ ___block_literal_global.1009
+ ___block_literal_global.10135
+ ___block_literal_global.10462
+ ___block_literal_global.11358
+ ___block_literal_global.11720
+ ___block_literal_global.1202
+ ___block_literal_global.12365
+ ___block_literal_global.12565
+ ___block_literal_global.12763
+ ___block_literal_global.12870
+ ___block_literal_global.13354
+ ___block_literal_global.13435
+ ___block_literal_global.13632
+ ___block_literal_global.1366
+ ___block_literal_global.14452
+ ___block_literal_global.14653
+ ___block_literal_global.15000
+ ___block_literal_global.151.21199
+ ___block_literal_global.152.21763
+ ___block_literal_global.155.21764
+ ___block_literal_global.157.37497
+ ___block_literal_global.157.65212
+ ___block_literal_global.157.70114
+ ___block_literal_global.159.33840
+ ___block_literal_global.159.41935
+ ___block_literal_global.159.4471
+ ___block_literal_global.1601
+ ___block_literal_global.161.71903
+ ___block_literal_global.162.49281
+ ___block_literal_global.162.70140
+ ___block_literal_global.165.70141
+ ___block_literal_global.168.56399
+ ___block_literal_global.168.70485
+ ___block_literal_global.16969
+ ___block_literal_global.171.27381
+ ___block_literal_global.175.23683
+ ___block_literal_global.175.46324
+ ___block_literal_global.1750
+ ___block_literal_global.17662
+ ___block_literal_global.177.25765
+ ___block_literal_global.17716
+ ___block_literal_global.178.11348
+ ___block_literal_global.178.16949
+ ___block_literal_global.178.23684
+ ___block_literal_global.178.53945
+ ___block_literal_global.180.41553
+ ___block_literal_global.18022
+ ___block_literal_global.18340
+ ___block_literal_global.1849
+ ___block_literal_global.188.49084
+ ___block_literal_global.191.27376
+ ___block_literal_global.192.50406
+ ___block_literal_global.193.23644
+ ___block_literal_global.194.64457
+ ___block_literal_global.198.61246
+ ___block_literal_global.19829
+ ___block_literal_global.199.50401
+ ___block_literal_global.206.70083
+ ___block_literal_global.20667
+ ___block_literal_global.21084
+ ___block_literal_global.21250
+ ___block_literal_global.21496
+ ___block_literal_global.21567
+ ___block_literal_global.216.43346
+ ___block_literal_global.217
+ ___block_literal_global.21762
+ ___block_literal_global.218.70040
+ ___block_literal_global.219.64058
+ ___block_literal_global.220.71849
+ ___block_literal_global.223.24410
+ ___block_literal_global.223.34492
+ ___block_literal_global.22359
+ ___block_literal_global.225
+ ___block_literal_global.226.52011
+ ___block_literal_global.227.56671
+ ___block_literal_global.228
+ ___block_literal_global.23060
+ ___block_literal_global.2328
+ ___block_literal_global.23318
+ ___block_literal_global.23479
+ ___block_literal_global.235.52012
+ ___block_literal_global.23619
+ ___block_literal_global.238.23065
+ ___block_literal_global.238.25021
+ ___block_literal_global.23928
+ ___block_literal_global.244.67175
+ ___block_literal_global.24409
+ ___block_literal_global.24694
+ ___block_literal_global.2488
+ ___block_literal_global.25038
+ ___block_literal_global.25293
+ ___block_literal_global.25762
+ ___block_literal_global.26107
+ ___block_literal_global.26491
+ ___block_literal_global.26901
+ ___block_literal_global.2736
+ ___block_literal_global.27392
+ ___block_literal_global.274.52918
+ ___block_literal_global.27488
+ ___block_literal_global.27597
+ ___block_literal_global.277
+ ___block_literal_global.27848
+ ___block_literal_global.28162
+ ___block_literal_global.284.55246
+ ___block_literal_global.285.52909
+ ___block_literal_global.288.52906
+ ___block_literal_global.29014
+ ___block_literal_global.292.52904
+ ___block_literal_global.2934
+ ___block_literal_global.296.52900
+ ___block_literal_global.29683
+ ___block_literal_global.299
+ ___block_literal_global.3002
+ ___block_literal_global.305.39306
+ ___block_literal_global.31.57247
+ ___block_literal_global.31599
+ ___block_literal_global.31979
+ ___block_literal_global.32990
+ ___block_literal_global.33244
+ ___block_literal_global.33836
+ ___block_literal_global.33918
+ ___block_literal_global.34557
+ ___block_literal_global.34719
+ ___block_literal_global.35509
+ ___block_literal_global.3598
+ ___block_literal_global.361.31520
+ ___block_literal_global.36346
+ ___block_literal_global.36636
+ ___block_literal_global.37122
+ ___block_literal_global.37496
+ ___block_literal_global.377
+ ___block_literal_global.38169
+ ___block_literal_global.382
+ ___block_literal_global.38319
+ ___block_literal_global.386
+ ___block_literal_global.38722
+ ___block_literal_global.38937
+ ___block_literal_global.39166
+ ___block_literal_global.39397
+ ___block_literal_global.395
+ ___block_literal_global.39873
+ ___block_literal_global.39998
+ ___block_literal_global.40159
+ ___block_literal_global.40371
+ ___block_literal_global.40904
+ ___block_literal_global.41363
+ ___block_literal_global.41564
+ ___block_literal_global.41934
+ ___block_literal_global.42009
+ ___block_literal_global.42553
+ ___block_literal_global.42918
+ ___block_literal_global.431.63423
+ ___block_literal_global.43114
+ ___block_literal_global.43344
+ ___block_literal_global.43455
+ ___block_literal_global.4357
+ ___block_literal_global.44119
+ ___block_literal_global.44180
+ ___block_literal_global.44619
+ ___block_literal_global.4476
+ ___block_literal_global.46082
+ ___block_literal_global.46293
+ ___block_literal_global.46417
+ ___block_literal_global.46606
+ ___block_literal_global.46703
+ ___block_literal_global.46942
+ ___block_literal_global.47828
+ ___block_literal_global.47850
+ ___block_literal_global.4812
+ ___block_literal_global.48471
+ ___block_literal_global.48482
+ ___block_literal_global.4905
+ ___block_literal_global.49093
+ ___block_literal_global.49280
+ ___block_literal_global.49618
+ ___block_literal_global.49679
+ ___block_literal_global.50253
+ ___block_literal_global.50405
+ ___block_literal_global.50690
+ ___block_literal_global.51105
+ ___block_literal_global.51350
+ ___block_literal_global.5137
+ ___block_literal_global.51406
+ ___block_literal_global.52009
+ ___block_literal_global.52282
+ ___block_literal_global.52816
+ ___block_literal_global.53002
+ ___block_literal_global.53283
+ ___block_literal_global.5369
+ ___block_literal_global.53830
+ ___block_literal_global.53944
+ ___block_literal_global.54407
+ ___block_literal_global.55388
+ ___block_literal_global.55491
+ ___block_literal_global.5585
+ ___block_literal_global.56398
+ ___block_literal_global.56697
+ ___block_literal_global.57052
+ ___block_literal_global.57265
+ ___block_literal_global.57350
+ ___block_literal_global.57879
+ ___block_literal_global.59294
+ ___block_literal_global.59373
+ ___block_literal_global.594
+ ___block_literal_global.59670
+ ___block_literal_global.6.67592
+ ___block_literal_global.60019
+ ___block_literal_global.60179
+ ___block_literal_global.6073
+ ___block_literal_global.60805
+ ___block_literal_global.6107
+ ___block_literal_global.61211
+ ___block_literal_global.61876
+ ___block_literal_global.62726
+ ___block_literal_global.62966
+ ___block_literal_global.63004
+ ___block_literal_global.63318
+ ___block_literal_global.63595
+ ___block_literal_global.63798
+ ___block_literal_global.64117
+ ___block_literal_global.64456
+ ___block_literal_global.648
+ ___block_literal_global.64934
+ ___block_literal_global.65054
+ ___block_literal_global.651
+ ___block_literal_global.65217
+ ___block_literal_global.65551
+ ___block_literal_global.65588
+ ___block_literal_global.65859
+ ___block_literal_global.65926
+ ___block_literal_global.66214
+ ___block_literal_global.66586
+ ___block_literal_global.66990
+ ___block_literal_global.67219
+ ___block_literal_global.67584
+ ___block_literal_global.68365
+ ___block_literal_global.698
+ ___block_literal_global.69869
+ ___block_literal_global.70112
+ ___block_literal_global.70316
+ ___block_literal_global.70506
+ ___block_literal_global.71055
+ ___block_literal_global.72111
+ ___block_literal_global.7262
+ ___block_literal_global.740
+ ___block_literal_global.744
+ ___block_literal_global.7804
+ ___block_literal_global.7973
+ ___block_literal_global.849
+ ___block_literal_global.854
+ ___block_literal_global.856
+ ___block_literal_global.8662
+ ___block_literal_global.884
+ ___block_literal_global.8896
+ ___block_literal_global.9455
+ ___block_literal_global.964
+ ___getCLPlacemarkClass_block_invoke.56156
+ ___getCLPlacemarkClass_block_invoke.57716
+ ___getCLPlacemarkClass_block_invoke.61857
+ ___getCNContactStoreClass_block_invoke.62968
+ ___getMPMediaItemClass_block_invoke.50421
+ ___getMPMediaPropertyPredicateClass_block_invoke.34613
+ ___getMPMediaPropertyPredicateClass_block_invoke.50419
+ ___getMPMediaQueryClass_block_invoke.34616
+ ___getMPMediaQueryClass_block_invoke.50424
+ __unnamed_array_storage.10448
+ __unnamed_array_storage.12815
+ __unnamed_array_storage.13453
+ __unnamed_array_storage.14691
+ __unnamed_array_storage.15223
+ __unnamed_array_storage.17197
+ __unnamed_array_storage.172.59601
+ __unnamed_array_storage.175.65702
+ __unnamed_array_storage.178.50703
+ __unnamed_array_storage.18136
+ __unnamed_array_storage.190.58842
+ __unnamed_array_storage.207.21570
+ __unnamed_array_storage.21598
+ __unnamed_array_storage.216.44061
+ __unnamed_array_storage.230.28908
+ __unnamed_array_storage.25258
+ __unnamed_array_storage.27860
+ __unnamed_array_storage.28366
+ __unnamed_array_storage.28907
+ __unnamed_array_storage.31640
+ __unnamed_array_storage.32161
+ __unnamed_array_storage.32642
+ __unnamed_array_storage.33579
+ __unnamed_array_storage.34520
+ __unnamed_array_storage.365.70836
+ __unnamed_array_storage.37027
+ __unnamed_array_storage.383.40793
+ __unnamed_array_storage.39531
+ __unnamed_array_storage.40910
+ __unnamed_array_storage.42277
+ __unnamed_array_storage.43333
+ __unnamed_array_storage.44078
+ __unnamed_array_storage.44789
+ __unnamed_array_storage.45086
+ __unnamed_array_storage.47314
+ __unnamed_array_storage.49449
+ __unnamed_array_storage.50702
+ __unnamed_array_storage.51525
+ __unnamed_array_storage.51843
+ __unnamed_array_storage.52690
+ __unnamed_array_storage.54252
+ __unnamed_array_storage.58841
+ __unnamed_array_storage.59508
+ __unnamed_array_storage.59600
+ __unnamed_array_storage.63053
+ __unnamed_array_storage.63610
+ __unnamed_array_storage.64072
+ __unnamed_array_storage.64739
+ __unnamed_array_storage.65734
+ __unnamed_array_storage.66062
+ __unnamed_array_storage.67822
+ __unnamed_array_storage.70892
+ __unnamed_array_storage.855
+ _audit_stringContacts.30315
+ _audit_stringContacts.45259
+ _audit_stringContacts.50688
+ _audit_stringContacts.57325
+ _audit_stringContacts.61902
+ _audit_stringContacts.62985
+ _audit_stringCoreLocation.39378
+ _audit_stringCoreLocation.45274
+ _audit_stringCoreLocation.55506
+ _audit_stringCoreLocation.56172
+ _audit_stringCoreLocation.57732
+ _audit_stringCoreLocation.59436
+ _audit_stringCoreLocation.61873
+ _audit_stringMediaPlayer.34651
+ _audit_stringMediaPlayer.50441
+ _audit_stringRunningBoardServices.25703
+ _audit_stringUIKit.39624
+ _classHFTriggerActionSetsBuilder.33195
+ _classHFTriggerActionSetsBuilder.36361
+ _classRegistrationLock.48994
+ _classRegistrationLock.67935
+ _classUIPasteboard.40171
+ _classUIPasteboard.46419
+ _classUIPasteboard.57054
+ _classUIPasteboard.60181
+ _constantHMCharacteristicMetadataFormatBool.2401
+ _constantHMCharacteristicMetadataFormatBool.26515
+ _constantHMCharacteristicMetadataFormatFloat.2380
+ _constantHMCharacteristicMetadataFormatInt.2387
+ _constantHMCharacteristicMetadataFormatInt.26626
+ _constantHMCharacteristicMetadataFormatString.2394
+ _constantHMCharacteristicMetadataFormatUInt16.2366
+ _constantHMCharacteristicMetadataFormatUInt32.2359
+ _constantHMCharacteristicMetadataFormatUInt64.2349
+ _constantHMCharacteristicMetadataFormatUInt8.2373
+ _constantHMCharacteristicMetadataFormatUInt8.26633
+ _getCLPlacemarkClass.61795
+ _getCLPlacemarkClass.softClass.56155
+ _getCLPlacemarkClass.softClass.57715
+ _getCLPlacemarkClass.softClass.61856
+ _getCNContactStoreClass.softClass.62967
+ _getHFTriggerActionSetsBuilderClass.33183
+ _getHFTriggerActionSetsBuilderClass.36356
+ _getHMCharacteristicMetadataFormatBool.2333
+ _getHMCharacteristicMetadataFormatBool.26510
+ _getHMCharacteristicMetadataFormatFloat.2336
+ _getHMCharacteristicMetadataFormatInt.2335
+ _getHMCharacteristicMetadataFormatInt.26621
+ _getHMCharacteristicMetadataFormatString.2334
+ _getHMCharacteristicMetadataFormatUInt16.2338
+ _getHMCharacteristicMetadataFormatUInt32.2339
+ _getHMCharacteristicMetadataFormatUInt64.2340
+ _getHMCharacteristicMetadataFormatUInt8.2337
+ _getHMCharacteristicMetadataFormatUInt8.26620
+ _getMPMediaItemClass.softClass.50420
+ _getMPMediaPropertyPredicateClass.softClass.34612
+ _getMPMediaPropertyPredicateClass.softClass.50418
+ _getMPMediaQueryClass.softClass.34615
+ _getMPMediaQueryClass.softClass.50423
+ _getUIPasteboardClass.40156
+ _getUIPasteboardClass.46413
+ _getUIPasteboardClass.57045
+ _getUIPasteboardClass.60174
+ _getWFTestingLifecycleLogObject
+ _initHFTriggerActionSetsBuilder.33192
+ _initHFTriggerActionSetsBuilder.36358
+ _initHMCharacteristicMetadataFormatBool.2398
+ _initHMCharacteristicMetadataFormatBool.26512
+ _initHMCharacteristicMetadataFormatFloat.2377
+ _initHMCharacteristicMetadataFormatInt.2384
+ _initHMCharacteristicMetadataFormatInt.26623
+ _initHMCharacteristicMetadataFormatString.2391
+ _initHMCharacteristicMetadataFormatUInt16.2363
+ _initHMCharacteristicMetadataFormatUInt32.2356
+ _initHMCharacteristicMetadataFormatUInt64.2342
+ _initHMCharacteristicMetadataFormatUInt8.2370
+ _initHMCharacteristicMetadataFormatUInt8.26630
+ _initUIPasteboard.40169
+ _initUIPasteboard.46415
+ _initUIPasteboard.57050
+ _initUIPasteboard.60177
+ _objc_msgSend$_uri
+ _objc_msgSend$accessSpecifierForCurrentProcess
+ _objc_msgSend$allowsHandoff
+ _objc_msgSend$apertureIconForActionIdentifier:
+ _objc_msgSend$badgeType
+ _objc_msgSend$getObjectRepresentation:forClass:options:
+ _objc_msgSend$iconWithImageData:scale:displayStyle:
+ _objc_msgSend$iconWithImageURL:displayStyle:
+ _objc_msgSend$iconWithSystemName:
+ _objc_msgSend$localizedOutputContentDescriptionWithContentCollection:
+ _objc_msgSend$overrideDoneButtonTitle:
+ _objc_msgSend$presentationMode
+ _objc_msgSend$processIntoStringsAndAttachmentsWithContext:options:completionHandler:
+ _objc_msgSend$saveOutputActionSmartPromtDataForWorkflowReference:completion:
+ _objc_msgSend$saveOutputActionSmartPromtDataForWorkflowReference:error:
+ _objc_msgSend$setBadgeType:
+ _objc_msgSend$setLastExecutedAction:
+ _sharedInstance.onceToken.11719
+ _sharedInstance.onceToken.55387
+ _sharedInstance.onceToken.7972
+ _sharedManager.onceToken.1749
+ _sharedManager.onceToken.56410
+ _sharedManager.onceToken.64116
+ _sharedManager.onceToken.65550
+ _sharedManager.sharedManager.56411
+ _sharedManager.sharedManager.64118
+ _sharedManager.sharedManager.65552
+ _sharedRegistry.onceToken.15224
+ _sharedRegistry.onceToken.23715
+ _sharedRegistry.sharedRegistry.15225
+ _sharedRegistry.sharedRegistry.23716
- +[NSUserDefaults(Workflow) dawnFluidityEnabled]
- +[NSUserDefaults(Workflow) springBoardActionButton]
- +[WFApplicationVisibilitySystemEventProvider isAvailable]
- +[WFCallStatusSystemEventProvider canProxyTelephony]
- +[WFCallStatusSystemEventProvider isAvailable]
- +[WFRunningWorkflowManager sharedManager]
- +[WFWorkflowController initialize]
- -[WFApplicationVisibilitySystemEventProvider .cxx_destruct]
- -[WFApplicationVisibilitySystemEventProvider applicationDidAppearEventType]
- -[WFApplicationVisibilitySystemEventProvider applicationDidDisappearEventType]
- -[WFApplicationVisibilitySystemEventProvider dealloc]
- -[WFApplicationVisibilitySystemEventProvider eventCallback]
- -[WFApplicationVisibilitySystemEventProvider handleLayoutChange:]
- -[WFApplicationVisibilitySystemEventProvider init]
- -[WFApplicationVisibilitySystemEventProvider invalidate]
- -[WFApplicationVisibilitySystemEventProvider layoutContainsApplication:]
- -[WFApplicationVisibilitySystemEventProvider monitor]
- -[WFApplicationVisibilitySystemEventProvider resume]
- -[WFApplicationVisibilitySystemEventProvider setEventCallback:]
- -[WFApplicationVisibilitySystemEventProvider setState:]
- -[WFApplicationVisibilitySystemEventProvider state]
- -[WFCallStatusSystemEventProvider .cxx_destruct]
- -[WFCallStatusSystemEventProvider callCenter]
- -[WFCallStatusSystemEventProvider callStatusChanged:]
- -[WFCallStatusSystemEventProvider eventCallback]
- -[WFCallStatusSystemEventProvider invalidate]
- -[WFCallStatusSystemEventProvider resume]
- -[WFCallStatusSystemEventProvider setCallCenter:]
- -[WFCallStatusSystemEventProvider setEventCallback:]
- -[WFCallStatusSystemEventProvider updateWithCall:]
- -[WFDatabase(PersistedSerializedParameters) storeSerializedParameters:forIdentifier:queryName:error:]
- -[WFDialogTransformer actionForAttribution]
- -[WFFocusConfigurationLinkAction parameterCollapsingBehavior]
- -[WFResourceManager stateAccessQueue]
- -[WFRunningWorkflowManager .cxx_destruct]
- -[WFRunningWorkflowManager applicationContext:applicationStateDidChange:]
- -[WFRunningWorkflowManager dealloc]
- -[WFRunningWorkflowManager demoResetBlock]
- -[WFRunningWorkflowManager init]
- -[WFRunningWorkflowManager runningWorkflowControllerSet]
- -[WFRunningWorkflowManager runningWorkflowControllers]
- -[WFRunningWorkflowManager runningWorkflows]
- -[WFRunningWorkflowManager setDemoResetBlock:]
- -[WFRunningWorkflowManager updateAssertions]
- -[WFRunningWorkflowManager updateRunningWorkflowCount]
- -[WFRunningWorkflowManager workflowControllerAssertionTable]
- -[WFRunningWorkflowManager workflowControllerDidStart:]
- -[WFRunningWorkflowManager workflowControllerDidStop:]
- -[WFSiriVisibilitySystemEventProvider applicationDidAppearEventType]
- -[WFSiriVisibilitySystemEventProvider applicationDidDisappearEventType]
- -[WFSiriVisibilitySystemEventProvider layoutContainsApplication:]
- -[WFSystemEventObserver .cxx_destruct]
- -[WFSystemEventObserver addObserver:]
- -[WFSystemEventObserver initWithProviders:]
- -[WFSystemEventObserver invalidate]
- -[WFSystemEventObserver invalidated]
- -[WFSystemEventObserver observers]
- -[WFSystemEventObserver providers]
- -[WFSystemEventObserver removeObserver:]
- -[WFSystemEventObserver resume]
- -[WFSystemEventObserver setInvalidated:]
- -[WFVariableString processIntoStringsAndAttachmentsWithContext:completionHandler:]
- GCC_except_table10123
- GCC_except_table10129
- GCC_except_table10281
- GCC_except_table10350
- GCC_except_table10357
- GCC_except_table10359
- GCC_except_table10361
- GCC_except_table10389
- GCC_except_table10394
- GCC_except_table10426
- GCC_except_table10429
- GCC_except_table10432
- GCC_except_table10435
- GCC_except_table10616
- GCC_except_table10741
- GCC_except_table10783
- GCC_except_table11108
- GCC_except_table11128
- GCC_except_table11131
- GCC_except_table11147
- GCC_except_table11218
- GCC_except_table11509
- GCC_except_table11512
- GCC_except_table11515
- GCC_except_table11520
- GCC_except_table11527
- GCC_except_table11532
- GCC_except_table11535
- GCC_except_table11538
- GCC_except_table11541
- GCC_except_table11544
- GCC_except_table11547
- GCC_except_table11550
- GCC_except_table11553
- GCC_except_table11556
- GCC_except_table11559
- GCC_except_table11565
- GCC_except_table11591
- GCC_except_table11593
- GCC_except_table11673
- GCC_except_table11700
- GCC_except_table11705
- GCC_except_table11707
- GCC_except_table11847
- GCC_except_table11862
- GCC_except_table1191
- GCC_except_table12015
- GCC_except_table12030
- GCC_except_table12036
- GCC_except_table12038
- GCC_except_table12043
- GCC_except_table12141
- GCC_except_table12153
- GCC_except_table12160
- GCC_except_table12258
- GCC_except_table12344
- GCC_except_table12369
- GCC_except_table12468
- GCC_except_table12499
- GCC_except_table12502
- GCC_except_table1262
- GCC_except_table12823
- GCC_except_table12856
- GCC_except_table12987
- GCC_except_table13031
- GCC_except_table13076
- GCC_except_table13184
- GCC_except_table13198
- GCC_except_table13215
- GCC_except_table13216
- GCC_except_table13217
- GCC_except_table13226
- GCC_except_table13237
- GCC_except_table13427
- GCC_except_table13431
- GCC_except_table13625
- GCC_except_table1365
- GCC_except_table13692
- GCC_except_table1370
- GCC_except_table13942
- GCC_except_table13968
- GCC_except_table14071
- GCC_except_table14188
- GCC_except_table14222
- GCC_except_table14227
- GCC_except_table14236
- GCC_except_table14349
- GCC_except_table14372
- GCC_except_table14383
- GCC_except_table14386
- GCC_except_table14702
- GCC_except_table14742
- GCC_except_table14753
- GCC_except_table14767
- GCC_except_table14770
- GCC_except_table14967
- GCC_except_table1666
- GCC_except_table1671
- GCC_except_table1673
- GCC_except_table1675
- GCC_except_table1958
- GCC_except_table1966
- GCC_except_table1988
- GCC_except_table2141
- GCC_except_table2166
- GCC_except_table2227
- GCC_except_table2264
- GCC_except_table2413
- GCC_except_table2428
- GCC_except_table2515
- GCC_except_table2568
- GCC_except_table2585
- GCC_except_table2591
- GCC_except_table2597
- GCC_except_table2806
- GCC_except_table2807
- GCC_except_table2814
- GCC_except_table2815
- GCC_except_table2816
- GCC_except_table2817
- GCC_except_table2841
- GCC_except_table2845
- GCC_except_table2869
- GCC_except_table2903
- GCC_except_table2919
- GCC_except_table2923
- GCC_except_table2952
- GCC_except_table2960
- GCC_except_table2962
- GCC_except_table2999
- GCC_except_table3010
- GCC_except_table3012
- GCC_except_table3015
- GCC_except_table3188
- GCC_except_table320
- GCC_except_table323
- GCC_except_table3483
- GCC_except_table3488
- GCC_except_table3491
- GCC_except_table379
- GCC_except_table3875
- GCC_except_table3876
- GCC_except_table3999
- GCC_except_table4099
- GCC_except_table4112
- GCC_except_table4131
- GCC_except_table4139
- GCC_except_table4316
- GCC_except_table4490
- GCC_except_table4496
- GCC_except_table4502
- GCC_except_table4592
- GCC_except_table4704
- GCC_except_table4730
- GCC_except_table4734
- GCC_except_table4774
- GCC_except_table4836
- GCC_except_table4858
- GCC_except_table4898
- GCC_except_table4954
- GCC_except_table4959
- GCC_except_table4961
- GCC_except_table5076
- GCC_except_table5082
- GCC_except_table5098
- GCC_except_table515
- GCC_except_table518
- GCC_except_table5401
- GCC_except_table5565
- GCC_except_table5625
- GCC_except_table5635
- GCC_except_table5777
- GCC_except_table5811
- GCC_except_table5969
- GCC_except_table5970
- GCC_except_table5971
- GCC_except_table6067
- GCC_except_table6111
- GCC_except_table6129
- GCC_except_table6155
- GCC_except_table627
- GCC_except_table6543
- GCC_except_table6556
- GCC_except_table6600
- GCC_except_table6601
- GCC_except_table6606
- GCC_except_table6607
- GCC_except_table6610
- GCC_except_table6616
- GCC_except_table6621
- GCC_except_table6663
- GCC_except_table6668
- GCC_except_table6726
- GCC_except_table7116
- GCC_except_table7126
- GCC_except_table7214
- GCC_except_table7290
- GCC_except_table7517
- GCC_except_table7560
- GCC_except_table7607
- GCC_except_table7608
- GCC_except_table7672
- GCC_except_table7774
- GCC_except_table7875
- GCC_except_table7930
- GCC_except_table7935
- GCC_except_table7946
- GCC_except_table8118
- GCC_except_table8125
- GCC_except_table8133
- GCC_except_table824
- GCC_except_table8315
- GCC_except_table8317
- GCC_except_table8318
- GCC_except_table8319
- GCC_except_table8322
- GCC_except_table8324
- GCC_except_table8325
- GCC_except_table8328
- GCC_except_table8333
- GCC_except_table8334
- GCC_except_table8336
- GCC_except_table8337
- GCC_except_table8338
- GCC_except_table8339
- GCC_except_table8340
- GCC_except_table8341
- GCC_except_table8342
- GCC_except_table8343
- GCC_except_table8344
- GCC_except_table8345
- GCC_except_table8347
- GCC_except_table8348
- GCC_except_table8349
- GCC_except_table8350
- GCC_except_table8351
- GCC_except_table8352
- GCC_except_table8354
- GCC_except_table8434
- GCC_except_table8450
- GCC_except_table8646
- GCC_except_table8782
- GCC_except_table8784
- GCC_except_table8786
- GCC_except_table8793
- GCC_except_table8834
- GCC_except_table8901
- GCC_except_table8907
- GCC_except_table8910
- GCC_except_table892
- GCC_except_table8940
- GCC_except_table8990
- GCC_except_table901
- GCC_except_table9062
- GCC_except_table9082
- GCC_except_table9107
- GCC_except_table9330
- GCC_except_table9336
- GCC_except_table9338
- GCC_except_table9340
- GCC_except_table9342
- GCC_except_table9344
- GCC_except_table9348
- GCC_except_table9350
- GCC_except_table9358
- GCC_except_table9368
- GCC_except_table9385
- GCC_except_table9397
- GCC_except_table9452
- GCC_except_table9458
- GCC_except_table9464
- GCC_except_table9476
- GCC_except_table9701
- GCC_except_table9703
- GCC_except_table9704
- GCC_except_table9705
- GCC_except_table9707
- GCC_except_table9709
- GCC_except_table9711
- GCC_except_table9714
- GCC_except_table9719
- GCC_except_table9722
- GCC_except_table9733
- GCC_except_table9871
- GCC_except_table9876
- GCC_except_table9878
- GCC_except_table9908
- GCC_except_table9920
- GCC_except_table9984
- _AssistantServicesLibrary.sLib.66225
- _AssistantServicesLibrary.sOnce.66224
- _ContactsLibrary.50856
- _ContactsLibrary.63261
- _ContactsLibraryCore.frameworkLibrary.30530
- _ContactsLibraryCore.frameworkLibrary.45466
- _ContactsLibraryCore.frameworkLibrary.50906
- _ContactsLibraryCore.frameworkLibrary.57530
- _ContactsLibraryCore.frameworkLibrary.62188
- _ContactsLibraryCore.frameworkLibrary.63269
- _CoreLocationLibraryCore.frameworkLibrary.39573
- _CoreLocationLibraryCore.frameworkLibrary.45491
- _CoreLocationLibraryCore.frameworkLibrary.55717
- _CoreLocationLibraryCore.frameworkLibrary.56372
- _CoreLocationLibraryCore.frameworkLibrary.58011
- _CoreLocationLibraryCore.frameworkLibrary.59715
- _CoreLocationLibraryCore.frameworkLibrary.62149
- _FBSDisplayLayoutElementSiriIdentifier
- _HFTriggerActionSetsBuilderFunction.33427
- _HFTriggerActionSetsBuilderFunction.36593
- _HMCharacteristicMetadataFormatBoolFunction.2507
- _HMCharacteristicMetadataFormatBoolFunction.26689
- _HMCharacteristicMetadataFormatFloatFunction.2486
- _HMCharacteristicMetadataFormatIntFunction.2493
- _HMCharacteristicMetadataFormatIntFunction.26800
- _HMCharacteristicMetadataFormatStringFunction.2500
- _HMCharacteristicMetadataFormatUInt16Function.2472
- _HMCharacteristicMetadataFormatUInt32Function.2465
- _HMCharacteristicMetadataFormatUInt64Function.2455
- _HMCharacteristicMetadataFormatUInt8Function.2479
- _HMCharacteristicMetadataFormatUInt8Function.26807
- _HomeKitLibrary.sLib.1841
- _HomeKitLibrary.sLib.2448
- _HomeKitLibrary.sLib.26669
- _HomeKitLibrary.sLib.33475
- _HomeKitLibrary.sLib.34154
- _HomeKitLibrary.sLib.36604
- _HomeKitLibrary.sLib.53503
- _HomeKitLibrary.sOnce.1837
- _HomeKitLibrary.sOnce.2447
- _HomeKitLibrary.sOnce.26668
- _HomeKitLibrary.sOnce.33473
- _HomeKitLibrary.sOnce.34147
- _HomeKitLibrary.sOnce.36599
- _HomeKitLibrary.sOnce.53496
- _HomeLibrary.sLib.26814
- _HomeLibrary.sLib.33431
- _HomeLibrary.sLib.36597
- _HomeLibrary.sOnce.26810
- _HomeLibrary.sOnce.33423
- _HomeLibrary.sOnce.36589
- _MediaPlayerLibrary.34863
- _MediaPlayerLibrary.50649
- _MediaPlayerLibraryCore.frameworkLibrary.34872
- _MediaPlayerLibraryCore.frameworkLibrary.50656
- _OBJC_CLASS_$_WFApplicationVisibilitySystemEventProvider
- _OBJC_CLASS_$_WFBackgroundAssertion
- _OBJC_CLASS_$_WFCallStatusSystemEventProvider
- _OBJC_CLASS_$_WFRunningWorkflowManager
- _OBJC_CLASS_$_WFSiriVisibilitySystemEventProvider
- _OBJC_CLASS_$_WFSystemEventObserver
- _OBJC_IVAR_$_WFApplicationVisibilitySystemEventProvider._monitor
- _OBJC_IVAR_$_WFApplicationVisibilitySystemEventProvider._state
- _OBJC_IVAR_$_WFApplicationVisibilitySystemEventProvider.eventCallback
- _OBJC_IVAR_$_WFCallStatusSystemEventProvider._callCenter
- _OBJC_IVAR_$_WFCallStatusSystemEventProvider.eventCallback
- _OBJC_IVAR_$_WFResourceManager._stateAccessQueue
- _OBJC_IVAR_$_WFRunningWorkflowManager._demoResetBlock
- _OBJC_IVAR_$_WFRunningWorkflowManager._runningWorkflowControllerSet
- _OBJC_IVAR_$_WFRunningWorkflowManager._workflowControllerAssertionTable
- _OBJC_IVAR_$_WFSystemEventObserver._invalidated
- _OBJC_IVAR_$_WFSystemEventObserver._observers
- _OBJC_IVAR_$_WFSystemEventObserver._providers
- _OBJC_METACLASS_$_WFApplicationVisibilitySystemEventProvider
- _OBJC_METACLASS_$_WFCallStatusSystemEventProvider
- _OBJC_METACLASS_$_WFRunningWorkflowManager
- _OBJC_METACLASS_$_WFSiriVisibilitySystemEventProvider
- _OBJC_METACLASS_$_WFSystemEventObserver
- _RunningBoardServicesLibrary.25867
- _RunningBoardServicesLibraryCore.frameworkLibrary.25870
- _SAObjectsLibrary.sLib.66489
- _SAObjectsLibrary.sOnce.66487
- _TelephonyUtilitiesLibrary
- _TelephonyUtilitiesLibraryCore.frameworkLibrary
- _UIKitLibrary.sLib.15231
- _UIKitLibrary.sLib.21686
- _UIKitLibrary.sLib.27079
- _UIKitLibrary.sLib.27745
- _UIKitLibrary.sLib.40370
- _UIKitLibrary.sLib.46647
- _UIKitLibrary.sLib.55459
- _UIKitLibrary.sLib.57271
- _UIKitLibrary.sLib.60481
- _UIKitLibrary.sOnce.15230
- _UIKitLibrary.sOnce.21679
- _UIKitLibrary.sOnce.27072
- _UIKitLibrary.sOnce.27740
- _UIKitLibrary.sOnce.40368
- _UIKitLibrary.sOnce.46637
- _UIKitLibrary.sOnce.55454
- _UIKitLibrary.sOnce.57261
- _UIKitLibrary.sOnce.60471
- _UIKitLibraryCore.frameworkLibrary.39821
- _UIPasteboardFunction.40383
- _UIPasteboardFunction.46642
- _UIPasteboardFunction.57266
- _UIPasteboardFunction.60476
- _WFDeviceCapabilityCellularTelephony
- _WFEnforceClass.11323
- _WFEnforceClass.1184
- _WFEnforceClass.12571
- _WFEnforceClass.12768
- _WFEnforceClass.14639
- _WFEnforceClass.15646
- _WFEnforceClass.15792
- _WFEnforceClass.16212
- _WFEnforceClass.16884
- _WFEnforceClass.1765
- _WFEnforceClass.20196
- _WFEnforceClass.20426
- _WFEnforceClass.21279
- _WFEnforceClass.2190
- _WFEnforceClass.22061
- _WFEnforceClass.22123
- _WFEnforceClass.23469
- _WFEnforceClass.23648
- _WFEnforceClass.2425
- _WFEnforceClass.27571
- _WFEnforceClass.27839
- _WFEnforceClass.28113
- _WFEnforceClass.28349
- _WFEnforceClass.29031
- _WFEnforceClass.30081
- _WFEnforceClass.30677
- _WFEnforceClass.33612
- _WFEnforceClass.34564
- _WFEnforceClass.35129
- _WFEnforceClass.3538
- _WFEnforceClass.38699
- _WFEnforceClass.40207
- _WFEnforceClass.4155
- _WFEnforceClass.41573
- _WFEnforceClass.44023
- _WFEnforceClass.44451
- _WFEnforceClass.44651
- _WFEnforceClass.44785
- _WFEnforceClass.4619
- _WFEnforceClass.46543
- _WFEnforceClass.47941
- _WFEnforceClass.48420
- _WFEnforceClass.55356
- _WFEnforceClass.57081
- _WFEnforceClass.57877
- _WFEnforceClass.59486
- _WFEnforceClass.59966
- _WFEnforceClass.60320
- _WFEnforceClass.6092
- _WFEnforceClass.61197
- _WFEnforceClass.61853
- _WFEnforceClass.62536
- _WFEnforceClass.63576
- _WFEnforceClass.67457
- _WFEnforceClass.67608
- _WFEnforceClass.68237
- _WFEnforceClass.69477
- _WFEnforceClass.70759
- _WFEnforceClass.71551
- _WFEnforceClass.7280
- _WFEnforceClass.7874
- _WFEnforceClass.8081
- _WFEnforceClass.8323
- _WFEnforceClass.8544
- _WFEnforceClass.8921
- _WFEnforceClass.9575
- _WFGroupingPropertyForMediaType.50643
- _WFLogCategoryCallStatusProvider
- _WFLogCategorySystemEventObserver
- _WFNameFromSystemEvent
- _WFWorkflowControllerDidStartNotification
- _WFWorkflowControllerDidStopNotification
- _WFWorkflowControllerDidStopNotificationErrorKey
- __OBJC_$_CLASS_METHODS_WFApplicationVisibilitySystemEventProvider
- __OBJC_$_CLASS_METHODS_WFCallStatusSystemEventProvider
- __OBJC_$_CLASS_METHODS_WFRunningWorkflowManager
- __OBJC_$_CLASS_METHODS_WFWorkflowController
- __OBJC_$_INSTANCE_METHODS_WFApplicationVisibilitySystemEventProvider
- __OBJC_$_INSTANCE_METHODS_WFCallStatusSystemEventProvider
- __OBJC_$_INSTANCE_METHODS_WFRunningWorkflowManager
- __OBJC_$_INSTANCE_METHODS_WFSiriVisibilitySystemEventProvider
- __OBJC_$_INSTANCE_METHODS_WFSystemEventObserver
- __OBJC_$_INSTANCE_VARIABLES_WFApplicationVisibilitySystemEventProvider
- __OBJC_$_INSTANCE_VARIABLES_WFCallStatusSystemEventProvider
- __OBJC_$_INSTANCE_VARIABLES_WFRunningWorkflowManager
- __OBJC_$_INSTANCE_VARIABLES_WFSystemEventObserver
- __OBJC_$_PROP_LIST_WFApplicationVisibilitySystemEventProvider
- __OBJC_$_PROP_LIST_WFCallStatusSystemEventProvider
- __OBJC_$_PROP_LIST_WFRunningWorkflowManager
- __OBJC_$_PROP_LIST_WFSystemEventObserver
- __OBJC_$_PROP_LIST_WFSystemEventProvider
- __OBJC_$_PROTOCOL_CLASS_METHODS_WFSystemEventProvider
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_WFSystemEventProvider
- __OBJC_$_PROTOCOL_METHOD_TYPES_WFSystemEventProvider
- __OBJC_$_PROTOCOL_REFS_WFSystemEventProvider
- __OBJC_CLASS_PROTOCOLS_$_WFApplicationVisibilitySystemEventProvider
- __OBJC_CLASS_PROTOCOLS_$_WFCallStatusSystemEventProvider
- __OBJC_CLASS_PROTOCOLS_$_WFRunningWorkflowManager
- __OBJC_CLASS_RO_$_WFApplicationVisibilitySystemEventProvider
- __OBJC_CLASS_RO_$_WFCallStatusSystemEventProvider
- __OBJC_CLASS_RO_$_WFRunningWorkflowManager
- __OBJC_CLASS_RO_$_WFSiriVisibilitySystemEventProvider
- __OBJC_CLASS_RO_$_WFSystemEventObserver
- __OBJC_LABEL_PROTOCOL_$_WFSystemEventProvider
- __OBJC_METACLASS_RO_$_WFApplicationVisibilitySystemEventProvider
- __OBJC_METACLASS_RO_$_WFCallStatusSystemEventProvider
- __OBJC_METACLASS_RO_$_WFRunningWorkflowManager
- __OBJC_METACLASS_RO_$_WFSiriVisibilitySystemEventProvider
- __OBJC_METACLASS_RO_$_WFSystemEventObserver
- __OBJC_PROTOCOL_$_WFSystemEventProvider
- ___101-[WFDatabase(PersistedSerializedParameters) storeSerializedParameters:forIdentifier:queryName:error:]_block_invoke
- ___116-[WFDialogTransformer sequentialParameterInputProvider:didAdvanceToParameter:action:defaultState:prompt:completion:]_block_invoke.327
- ___116-[WFDialogTransformer sequentialParameterInputProvider:didAdvanceToParameter:action:defaultState:prompt:completion:]_block_invoke.329
- ___116-[WFDialogTransformer sequentialParameterInputProvider:didAdvanceToParameter:action:defaultState:prompt:completion:]_block_invoke_2.331
- ___135-[WFAction presentSmartPromptAuthorizationWithConfiguration:userInterface:databaseApprovalResult:contentDestination:completionHandler:]_block_invoke.643
- ___31-[WFSystemEventObserver resume]_block_invoke
- ___34-[WFResourceManager resourceNodes]_block_invoke
- ___35-[WFAction finishRunningWithError:]_block_invoke.697
- ___38-[WFResourceManager addResourceNodes:]_block_invoke
- ___39-[WFResourceManager resourcesAvailable]_block_invoke
- ___41+[WFRunningWorkflowManager sharedManager]_block_invoke
- ___41-[WFCallStatusSystemEventProvider resume]_block_invoke
- ___41-[WFResourceManager removeResourceNodes:]_block_invoke
- ___41-[WFResourceManager unavailableResources]_block_invoke
- ___44-[WFRunningWorkflowManager runningWorkflows]_block_invoke
- ___44-[WFRunningWorkflowManager updateAssertions]_block_invoke
- ___44-[WFRunningWorkflowManager updateAssertions]_block_invoke.169
- ___46-[WFResourceManager unavailableResourceErrors]_block_invoke
- ___48-[WFLinkAction runAsynchronouslyWithLinkAction:]_block_invoke.265
- ___52-[WFApplicationVisibilitySystemEventProvider resume]_block_invoke
- ___53-[WFResourceManager resourceNodeAvailabilityChanged:]_block_invoke
- ___54-[WFHandleIntentAction finishRunningByContinuingInApp]_block_invoke.265
- ___57-[WFResourceManager resourcesRequiredForDisplayAvailable]_block_invoke
- ___58-[WFWorkflow databaseDidChange:modified:inserted:removed:]_block_invoke.631
- ___59-[WFDialogTransformer showDialogRequest:completionHandler:]_block_invoke.198
- ___59-[WFLinkAction enumeration:localizedLabelForPossibleState:]_block_invoke.401
- ___59-[WFLinkAction getContentDestinationWithCompletionHandler:]_block_invoke.346
- ___62-[WFAction requestInterfacePresentationWithCompletionHandler:]_block_invoke.704
- ___77-[WFLinkAction fetchMissingDisplayRepresentationValuesWithCompletionHandler:]_block_invoke.379
- ___77-[WFLinkAction fetchMissingDisplayRepresentationValuesWithCompletionHandler:]_block_invoke.386
- ___77-[WFLinkAction fetchMissingDisplayRepresentationValuesWithCompletionHandler:]_block_invoke_2.380
- ___77-[WFLinkAction fetchMissingDisplayRepresentationValuesWithCompletionHandler:]_block_invoke_2.388
- ___77-[WFLinkAction fetchMissingDisplayRepresentationValuesWithCompletionHandler:]_block_invoke_3.393
- ___82-[WFVariableString processIntoStringsAndAttachmentsWithContext:completionHandler:]_block_invoke
- ___82-[WFVariableString processIntoStringsAndAttachmentsWithContext:completionHandler:]_block_invoke_2
- ___82-[WFVariableString processIntoStringsAndAttachmentsWithContext:completionHandler:]_block_invoke_3
- ___82-[WFVariableString processIntoStringsAndAttachmentsWithContext:completionHandler:]_block_invoke_4
- ___82-[WFVariableString processIntoStringsAndAttachmentsWithContext:completionHandler:]_block_invoke_5
- ___88-[WFAction performDataAccessChecksWithUserInterface:contentItemCache:completionHandler:]_block_invoke.626
- ___88-[WFAction performDataAccessChecksWithUserInterface:contentItemCache:completionHandler:]_block_invoke.627
- ___99-[WFAction performDeletionAuthorizationChecksWithUserInterface:contentItemCache:completionHandler:]_block_invoke.653
- ___AssistantServicesLibrary_block_invoke.66230
- ___Block_byref_object_copy_.1017
- ___Block_byref_object_copy_.11460
- ___Block_byref_object_copy_.11917
- ___Block_byref_object_copy_.12776
- ___Block_byref_object_copy_.14217
- ___Block_byref_object_copy_.15226
- ___Block_byref_object_copy_.17018
- ___Block_byref_object_copy_.17120
- ___Block_byref_object_copy_.18300
- ___Block_byref_object_copy_.19232
- ___Block_byref_object_copy_.19656
- ___Block_byref_object_copy_.21047
- ___Block_byref_object_copy_.23212
- ___Block_byref_object_copy_.23850
- ___Block_byref_object_copy_.25889
- ___Block_byref_object_copy_.27729
- ___Block_byref_object_copy_.28423
- ___Block_byref_object_copy_.2848
- ___Block_byref_object_copy_.30050
- ___Block_byref_object_copy_.3124
- ___Block_byref_object_copy_.33184
- ___Block_byref_object_copy_.33456
- ___Block_byref_object_copy_.34884
- ___Block_byref_object_copy_.35732
- ___Block_byref_object_copy_.36925
- ___Block_byref_object_copy_.38927
- ___Block_byref_object_copy_.39400
- ___Block_byref_object_copy_.40049
- ___Block_byref_object_copy_.40362
- ___Block_byref_object_copy_.41450
- ___Block_byref_object_copy_.44077
- ___Block_byref_object_copy_.44260
- ___Block_byref_object_copy_.44623
- ___Block_byref_object_copy_.46525
- ___Block_byref_object_copy_.46979
- ___Block_byref_object_copy_.4874
- ___Block_byref_object_copy_.51331
- ___Block_byref_object_copy_.5291
- ___Block_byref_object_copy_.53115
- ___Block_byref_object_copy_.53883
- ___Block_byref_object_copy_.54352
- ___Block_byref_object_copy_.54906
- ___Block_byref_object_copy_.55763
- ___Block_byref_object_copy_.56273
- ___Block_byref_object_copy_.56808
- ___Block_byref_object_copy_.57424
- ___Block_byref_object_copy_.57733
- ___Block_byref_object_copy_.60063
- ___Block_byref_object_copy_.60792
- ___Block_byref_object_copy_.61176
- ___Block_byref_object_copy_.6203
- ___Block_byref_object_copy_.62292
- ___Block_byref_object_copy_.64308
- ___Block_byref_object_copy_.65482
- ___Block_byref_object_copy_.66203
- ___Block_byref_object_copy_.66927
- ___Block_byref_object_copy_.67845
- ___Block_byref_object_copy_.68621
- ___Block_byref_object_copy_.70367
- ___Block_byref_object_copy_.7866
- ___Block_byref_object_copy_.9023
- ___Block_byref_object_copy_.9074
- ___Block_byref_object_copy_.9637
- ___Block_byref_object_copy_.9940
- ___Block_byref_object_dispose_.1018
- ___Block_byref_object_dispose_.11461
- ___Block_byref_object_dispose_.11918
- ___Block_byref_object_dispose_.12777
- ___Block_byref_object_dispose_.14218
- ___Block_byref_object_dispose_.15227
- ___Block_byref_object_dispose_.17019
- ___Block_byref_object_dispose_.17121
- ___Block_byref_object_dispose_.18301
- ___Block_byref_object_dispose_.19233
- ___Block_byref_object_dispose_.19657
- ___Block_byref_object_dispose_.21048
- ___Block_byref_object_dispose_.23213
- ___Block_byref_object_dispose_.23851
- ___Block_byref_object_dispose_.25890
- ___Block_byref_object_dispose_.27730
- ___Block_byref_object_dispose_.28424
- ___Block_byref_object_dispose_.2849
- ___Block_byref_object_dispose_.30051
- ___Block_byref_object_dispose_.3125
- ___Block_byref_object_dispose_.33185
- ___Block_byref_object_dispose_.33457
- ___Block_byref_object_dispose_.34885
- ___Block_byref_object_dispose_.35733
- ___Block_byref_object_dispose_.36926
- ___Block_byref_object_dispose_.38928
- ___Block_byref_object_dispose_.39401
- ___Block_byref_object_dispose_.40050
- ___Block_byref_object_dispose_.40363
- ___Block_byref_object_dispose_.41451
- ___Block_byref_object_dispose_.44078
- ___Block_byref_object_dispose_.44261
- ___Block_byref_object_dispose_.44624
- ___Block_byref_object_dispose_.46526
- ___Block_byref_object_dispose_.46980
- ___Block_byref_object_dispose_.4875
- ___Block_byref_object_dispose_.51332
- ___Block_byref_object_dispose_.5292
- ___Block_byref_object_dispose_.53116
- ___Block_byref_object_dispose_.53884
- ___Block_byref_object_dispose_.54353
- ___Block_byref_object_dispose_.54907
- ___Block_byref_object_dispose_.55764
- ___Block_byref_object_dispose_.56274
- ___Block_byref_object_dispose_.56809
- ___Block_byref_object_dispose_.57425
- ___Block_byref_object_dispose_.57734
- ___Block_byref_object_dispose_.60064
- ___Block_byref_object_dispose_.60793
- ___Block_byref_object_dispose_.61177
- ___Block_byref_object_dispose_.6204
- ___Block_byref_object_dispose_.62293
- ___Block_byref_object_dispose_.64309
- ___Block_byref_object_dispose_.65483
- ___Block_byref_object_dispose_.66204
- ___Block_byref_object_dispose_.66928
- ___Block_byref_object_dispose_.67846
- ___Block_byref_object_dispose_.68622
- ___Block_byref_object_dispose_.70368
- ___Block_byref_object_dispose_.7867
- ___Block_byref_object_dispose_.9024
- ___Block_byref_object_dispose_.9075
- ___Block_byref_object_dispose_.9638
- ___Block_byref_object_dispose_.9941
- ___ContactsLibraryCore_block_invoke.30531
- ___ContactsLibraryCore_block_invoke.45467
- ___ContactsLibraryCore_block_invoke.50907
- ___ContactsLibraryCore_block_invoke.57531
- ___ContactsLibraryCore_block_invoke.62189
- ___ContactsLibraryCore_block_invoke.63270
- ___CoreLocationLibraryCore_block_invoke.39574
- ___CoreLocationLibraryCore_block_invoke.45492
- ___CoreLocationLibraryCore_block_invoke.55718
- ___CoreLocationLibraryCore_block_invoke.56373
- ___CoreLocationLibraryCore_block_invoke.58012
- ___CoreLocationLibraryCore_block_invoke.59716
- ___CoreLocationLibraryCore_block_invoke.62150
- ___HomeKitLibrary_block_invoke.1840
- ___HomeKitLibrary_block_invoke.2457
- ___HomeKitLibrary_block_invoke.26674
- ___HomeKitLibrary_block_invoke.33481
- ___HomeKitLibrary_block_invoke.34152
- ___HomeKitLibrary_block_invoke.36602
- ___HomeKitLibrary_block_invoke.53501
- ___HomeLibrary_block_invoke.26812
- ___HomeLibrary_block_invoke.33429
- ___HomeLibrary_block_invoke.36595
- ___MediaPlayerLibraryCore_block_invoke.34873
- ___MediaPlayerLibraryCore_block_invoke.50657
- ___RunningBoardServicesLibraryCore_block_invoke.25871
- ___SAObjectsLibrary_block_invoke.66493
- ___TelephonyUtilitiesLibraryCore_block_invoke
- ___UIKitLibraryCore_block_invoke.39822
- ___UIKitLibrary_block_invoke.15234
- ___UIKitLibrary_block_invoke.21684
- ___UIKitLibrary_block_invoke.27077
- ___UIKitLibrary_block_invoke.27743
- ___UIKitLibrary_block_invoke.40376
- ___UIKitLibrary_block_invoke.46645
- ___UIKitLibrary_block_invoke.55457
- ___UIKitLibrary_block_invoke.57269
- ___UIKitLibrary_block_invoke.60479
- ___block_descriptor_32_e45_"WFWorkflow"24?0"WFWorkflowController"8Q16l
- ___block_descriptor_40_e8_32s_e39_v32?0"<WFSystemEventProvider>"8q1624ls32l8
- ___block_descriptor_48_e8_32s40bs_e31_v24?0"CATResult"8"NSError"16ls40l8s32l8
- ___block_descriptor_56_e8_32s40s48s_e61_v40?0"<WFVariableStringContent>"8Q16?<v?"NSError">24^B32ls32l8s40l8s48l8
- ___block_descriptor_64_e8_32s40s48s56bs_e29_v24?0"NSArray"8"NSError"16ls32l8s40l8s48l8s56l8
- ___block_descriptor_64_e8_32s40s48s56s_e9_16?0^8ls32l8s40l8s48l8s56l8
- ___block_descriptor_72_e8_32s40s48s56s64r_e24_v16?0"NSNotification"8ls32l8s40l8s48l8r64l8s56l8
- ___block_literal_global.1010
- ___block_literal_global.10248
- ___block_literal_global.10572
- ___block_literal_global.11467
- ___block_literal_global.11670
- ___block_literal_global.11935
- ___block_literal_global.1206
- ___block_literal_global.12580
- ___block_literal_global.12779
- ___block_literal_global.12979
- ___block_literal_global.13086
- ___block_literal_global.13568
- ___block_literal_global.13649
- ___block_literal_global.1370
- ___block_literal_global.13847
- ___block_literal_global.14668
- ___block_literal_global.148
- ___block_literal_global.14858
- ___block_literal_global.151.21384
- ___block_literal_global.15197
- ___block_literal_global.152.21947
- ___block_literal_global.155.21948
- ___block_literal_global.157.37719
- ___block_literal_global.157.70384
- ___block_literal_global.159.34070
- ___block_literal_global.159.42165
- ___block_literal_global.159.4585
- ___block_literal_global.159.65485
- ___block_literal_global.161.72175
- ___block_literal_global.162.49502
- ___block_literal_global.162.70410
- ___block_literal_global.165.70411
- ___block_literal_global.168.27625
- ___block_literal_global.168.56614
- ___block_literal_global.168.70754
- ___block_literal_global.169
- ___block_literal_global.1701
- ___block_literal_global.17162
- ___block_literal_global.173.12946
- ___block_literal_global.175.23855
- ___block_literal_global.175.46546
- ___block_literal_global.178.11457
- ___block_literal_global.178.17142
- ___block_literal_global.178.23856
- ___block_literal_global.178.54160
- ___block_literal_global.17846
- ___block_literal_global.179.63008
- ___block_literal_global.17901
- ___block_literal_global.180.41783
- ___block_literal_global.18207
- ___block_literal_global.1850
- ___block_literal_global.18525
- ___block_literal_global.188.27620
- ___block_literal_global.188.49305
- ___block_literal_global.192.50627
- ___block_literal_global.193.23816
- ___block_literal_global.194.64729
- ___block_literal_global.1950
- ___block_literal_global.198.61540
- ___block_literal_global.199.50622
- ___block_literal_global.20013
- ___block_literal_global.206.70353
- ___block_literal_global.20852
- ___block_literal_global.21269
- ___block_literal_global.21435
- ___block_literal_global.216.43573
- ___block_literal_global.216.72119
- ___block_literal_global.21680
- ___block_literal_global.21751
- ___block_literal_global.218.70310
- ___block_literal_global.219.64330
- ___block_literal_global.219.72123
- ___block_literal_global.21946
- ___block_literal_global.222.65197
- ___block_literal_global.223.24582
- ___block_literal_global.223.34721
- ___block_literal_global.224.65193
- ___block_literal_global.22543
- ___block_literal_global.226.52233
- ___block_literal_global.227.72200
- ___block_literal_global.23231
- ___block_literal_global.23490
- ___block_literal_global.235.25205
- ___block_literal_global.235.52234
- ___block_literal_global.236
- ___block_literal_global.23651
- ___block_literal_global.23791
- ___block_literal_global.24100
- ___block_literal_global.2432
- ___block_literal_global.244.67449
- ___block_literal_global.24581
- ___block_literal_global.24866
- ___block_literal_global.25221
- ___block_literal_global.25472
- ___block_literal_global.2593
- ___block_literal_global.25930
- ___block_literal_global.26280
- ___block_literal_global.26663
- ___block_literal_global.27073
- ___block_literal_global.27148
- ___block_literal_global.272
- ___block_literal_global.275
- ___block_literal_global.27636
- ___block_literal_global.27732
- ___block_literal_global.27841
- ___block_literal_global.28092
- ___block_literal_global.283
- ___block_literal_global.284.55461
- ___block_literal_global.28407
- ___block_literal_global.2841
- ___block_literal_global.286
- ___block_literal_global.288.53125
- ___block_literal_global.292.53122
- ___block_literal_global.29260
- ___block_literal_global.297
- ___block_literal_global.29914
- ___block_literal_global.303
- ___block_literal_global.3041
- ___block_literal_global.31.57457
- ___block_literal_global.3109
- ___block_literal_global.31827
- ___block_literal_global.32205
- ___block_literal_global.33220
- ___block_literal_global.33474
- ___block_literal_global.34066
- ___block_literal_global.34148
- ___block_literal_global.34786
- ___block_literal_global.34948
- ___block_literal_global.35739
- ___block_literal_global.36576
- ___block_literal_global.36870
- ___block_literal_global.3714
- ___block_literal_global.37222
- ___block_literal_global.375
- ___block_literal_global.37718
- ___block_literal_global.38391
- ___block_literal_global.38541
- ___block_literal_global.38944
- ___block_literal_global.391
- ___block_literal_global.39149
- ___block_literal_global.39379
- ___block_literal_global.39608
- ___block_literal_global.40084
- ___block_literal_global.40208
- ___block_literal_global.40369
- ___block_literal_global.40581
- ___block_literal_global.41134
- ___block_literal_global.41592
- ___block_literal_global.41794
- ___block_literal_global.42164
- ___block_literal_global.42236
- ___block_literal_global.427
- ___block_literal_global.42780
- ___block_literal_global.43145
- ___block_literal_global.43341
- ___block_literal_global.43571
- ___block_literal_global.43682
- ___block_literal_global.44346
- ___block_literal_global.44634
- ___block_literal_global.4471
- ___block_literal_global.44840
- ___block_literal_global.4590
- ___block_literal_global.46304
- ___block_literal_global.46515
- ___block_literal_global.46638
- ___block_literal_global.46828
- ___block_literal_global.46924
- ___block_literal_global.47163
- ___block_literal_global.48049
- ___block_literal_global.48071
- ___block_literal_global.48692
- ___block_literal_global.48703
- ___block_literal_global.4927
- ___block_literal_global.49314
- ___block_literal_global.49501
- ___block_literal_global.49839
- ___block_literal_global.49900
- ___block_literal_global.5020
- ___block_literal_global.50474
- ___block_literal_global.50626
- ___block_literal_global.50912
- ___block_literal_global.51327
- ___block_literal_global.51572
- ___block_literal_global.51628
- ___block_literal_global.52231
- ___block_literal_global.52504
- ___block_literal_global.5255
- ___block_literal_global.53038
- ___block_literal_global.53216
- ___block_literal_global.53497
- ___block_literal_global.54044
- ___block_literal_global.54159
- ___block_literal_global.54622
- ___block_literal_global.5516
- ___block_literal_global.55603
- ___block_literal_global.55706
- ___block_literal_global.56613
- ___block_literal_global.56907
- ___block_literal_global.57262
- ___block_literal_global.5732
- ___block_literal_global.57475
- ___block_literal_global.57560
- ___block_literal_global.57729
- ___block_literal_global.58173
- ___block_literal_global.592
- ___block_literal_global.59587
- ___block_literal_global.59666
- ___block_literal_global.59963
- ___block_literal_global.6.67866
- ___block_literal_global.60312
- ___block_literal_global.60472
- ___block_literal_global.61099
- ___block_literal_global.61505
- ___block_literal_global.62167
- ___block_literal_global.6217
- ___block_literal_global.6252
- ___block_literal_global.63017
- ___block_literal_global.63257
- ___block_literal_global.63295
- ___block_literal_global.63609
- ___block_literal_global.63870
- ___block_literal_global.64070
- ___block_literal_global.64389
- ___block_literal_global.646
- ___block_literal_global.64728
- ___block_literal_global.649
- ___block_literal_global.65210
- ___block_literal_global.65330
- ___block_literal_global.65490
- ___block_literal_global.65825
- ___block_literal_global.65862
- ___block_literal_global.66133
- ___block_literal_global.66200
- ___block_literal_global.66488
- ___block_literal_global.66860
- ___block_literal_global.67264
- ___block_literal_global.67493
- ___block_literal_global.67858
- ___block_literal_global.68640
- ___block_literal_global.696
- ___block_literal_global.70139
- ___block_literal_global.70382
- ___block_literal_global.70585
- ___block_literal_global.70775
- ___block_literal_global.71321
- ___block_literal_global.72387
- ___block_literal_global.738
- ___block_literal_global.7403
- ___block_literal_global.742
- ___block_literal_global.7930
- ___block_literal_global.8097
- ___block_literal_global.848
- ___block_literal_global.853
- ___block_literal_global.857
- ___block_literal_global.8771
- ___block_literal_global.881
- ___block_literal_global.9005
- ___block_literal_global.9566
- ___block_literal_global.961
- ___getCLPlacemarkClass_block_invoke.56371
- ___getCLPlacemarkClass_block_invoke.58010
- ___getCLPlacemarkClass_block_invoke.62148
- ___getCNContactStoreClass_block_invoke.63259
- ___getMPMediaItemClass_block_invoke.50642
- ___getMPMediaPropertyPredicateClass_block_invoke.34842
- ___getMPMediaPropertyPredicateClass_block_invoke.50640
- ___getMPMediaQueryClass_block_invoke.34845
- ___getMPMediaQueryClass_block_invoke.50645
- ___getTUCallCenterCallStatusChangedNotificationSymbolLoc_block_invoke
- ___getTUCallCenterClass_block_invoke
- ___getTUCallCenterVideoCallStatusChangedNotificationSymbolLoc_block_invoke
- ___getTUCallClass_block_invoke
- ___getWFCallStatusProviderLogObject_block_invoke
- ___getWFSystemEventObserverLogObject_block_invoke
- __unnamed_array_storage.10559
- __unnamed_array_storage.13031
- __unnamed_array_storage.13667
- __unnamed_array_storage.14904
- __unnamed_array_storage.15420
- __unnamed_array_storage.172.59894
- __unnamed_array_storage.17390
- __unnamed_array_storage.175.65976
- __unnamed_array_storage.178.50925
- __unnamed_array_storage.18321
- __unnamed_array_storage.190.59136
- __unnamed_array_storage.207.21754
- __unnamed_array_storage.216.44288
- __unnamed_array_storage.21782
- __unnamed_array_storage.230.29154
- __unnamed_array_storage.25437
- __unnamed_array_storage.28104
- __unnamed_array_storage.28611
- __unnamed_array_storage.29153
- __unnamed_array_storage.31868
- __unnamed_array_storage.32387
- __unnamed_array_storage.32868
- __unnamed_array_storage.33809
- __unnamed_array_storage.34749
- __unnamed_array_storage.355
- __unnamed_array_storage.37255
- __unnamed_array_storage.383.41013
- __unnamed_array_storage.39742
- __unnamed_array_storage.41140
- __unnamed_array_storage.42504
- __unnamed_array_storage.43560
- __unnamed_array_storage.44305
- __unnamed_array_storage.45011
- __unnamed_array_storage.45308
- __unnamed_array_storage.47535
- __unnamed_array_storage.49670
- __unnamed_array_storage.50924
- __unnamed_array_storage.51747
- __unnamed_array_storage.52065
- __unnamed_array_storage.52912
- __unnamed_array_storage.54467
- __unnamed_array_storage.59135
- __unnamed_array_storage.59801
- __unnamed_array_storage.59893
- __unnamed_array_storage.63344
- __unnamed_array_storage.63884
- __unnamed_array_storage.64344
- __unnamed_array_storage.65009
- __unnamed_array_storage.66008
- __unnamed_array_storage.66336
- __unnamed_array_storage.68096
- __unnamed_array_storage.71158
- __unnamed_array_storage.856
- _audit_stringContacts.30545
- _audit_stringContacts.45481
- _audit_stringContacts.50910
- _audit_stringContacts.57535
- _audit_stringContacts.62192
- _audit_stringContacts.63276
- _audit_stringCoreLocation.39589
- _audit_stringCoreLocation.45496
- _audit_stringCoreLocation.55721
- _audit_stringCoreLocation.56387
- _audit_stringCoreLocation.58026
- _audit_stringCoreLocation.59729
- _audit_stringCoreLocation.62164
- _audit_stringMediaPlayer.34879
- _audit_stringMediaPlayer.50663
- _audit_stringRunningBoardServices.25874
- _audit_stringTelephonyUtilities
- _audit_stringUIKit.39835
- _classHFTriggerActionSetsBuilder.33425
- _classHFTriggerActionSetsBuilder.36591
- _classRegistrationLock.49215
- _classRegistrationLock.68209
- _classUIPasteboard.40381
- _classUIPasteboard.46640
- _classUIPasteboard.57264
- _classUIPasteboard.60474
- _constantHMCharacteristicMetadataFormatBool.2505
- _constantHMCharacteristicMetadataFormatBool.26687
- _constantHMCharacteristicMetadataFormatFloat.2484
- _constantHMCharacteristicMetadataFormatInt.2491
- _constantHMCharacteristicMetadataFormatInt.26798
- _constantHMCharacteristicMetadataFormatString.2498
- _constantHMCharacteristicMetadataFormatUInt16.2470
- _constantHMCharacteristicMetadataFormatUInt32.2463
- _constantHMCharacteristicMetadataFormatUInt64.2453
- _constantHMCharacteristicMetadataFormatUInt8.2477
- _constantHMCharacteristicMetadataFormatUInt8.26805
- _getCLPlacemarkClass.62086
- _getCLPlacemarkClass.softClass.56370
- _getCLPlacemarkClass.softClass.58009
- _getCLPlacemarkClass.softClass.62147
- _getCNContactStoreClass.softClass.63258
- _getHFTriggerActionSetsBuilderClass.33413
- _getHFTriggerActionSetsBuilderClass.36586
- _getHMCharacteristicMetadataFormatBool.2437
- _getHMCharacteristicMetadataFormatBool.26682
- _getHMCharacteristicMetadataFormatFloat.2440
- _getHMCharacteristicMetadataFormatInt.2439
- _getHMCharacteristicMetadataFormatInt.26793
- _getHMCharacteristicMetadataFormatString.2438
- _getHMCharacteristicMetadataFormatUInt16.2442
- _getHMCharacteristicMetadataFormatUInt32.2443
- _getHMCharacteristicMetadataFormatUInt64.2444
- _getHMCharacteristicMetadataFormatUInt8.2441
- _getHMCharacteristicMetadataFormatUInt8.26792
- _getMPMediaItemClass.softClass.50641
- _getMPMediaPropertyPredicateClass.softClass.34841
- _getMPMediaPropertyPredicateClass.softClass.50639
- _getMPMediaQueryClass.softClass.34844
- _getMPMediaQueryClass.softClass.50644
- _getTUCallCenterCallStatusChangedNotificationSymbolLoc.ptr
- _getTUCallCenterClass.softClass
- _getTUCallCenterVideoCallStatusChangedNotificationSymbolLoc.ptr
- _getTUCallClass.softClass
- _getUIPasteboardClass.40366
- _getUIPasteboardClass.46634
- _getUIPasteboardClass.57255
- _getUIPasteboardClass.60467
- _getWFCallStatusProviderLogObject
- _getWFCallStatusProviderLogObject.log
- _getWFCallStatusProviderLogObject.onceToken
- _getWFSystemEventObserverLogObject
- _getWFSystemEventObserverLogObject.log
- _getWFSystemEventObserverLogObject.onceToken
- _initHFTriggerActionSetsBuilder.33422
- _initHFTriggerActionSetsBuilder.36588
- _initHMCharacteristicMetadataFormatBool.2502
- _initHMCharacteristicMetadataFormatBool.26684
- _initHMCharacteristicMetadataFormatFloat.2481
- _initHMCharacteristicMetadataFormatInt.2488
- _initHMCharacteristicMetadataFormatInt.26795
- _initHMCharacteristicMetadataFormatString.2495
- _initHMCharacteristicMetadataFormatUInt16.2467
- _initHMCharacteristicMetadataFormatUInt32.2460
- _initHMCharacteristicMetadataFormatUInt64.2446
- _initHMCharacteristicMetadataFormatUInt8.2474
- _initHMCharacteristicMetadataFormatUInt8.26802
- _initUIPasteboard.40379
- _initUIPasteboard.46636
- _initUIPasteboard.57260
- _initUIPasteboard.60470
- _objc_msgSend$actionForAttribution
- _objc_msgSend$applicationDidAppearEventType
- _objc_msgSend$applicationDidDisappearEventType
- _objc_msgSend$backgroundAssertionWithName:expirationHandler:
- _objc_msgSend$callCenter
- _objc_msgSend$callStatusChanged:
- _objc_msgSend$callUUID
- _objc_msgSend$canProxyTelephony
- _objc_msgSend$currentAudioAndVideoCalls
- _objc_msgSend$demoResetBlock
- _objc_msgSend$end
- _objc_msgSend$eventCallback
- _objc_msgSend$handleLayoutChange:
- _objc_msgSend$isTimePickerParameter
- _objc_msgSend$layoutContainsApplication:
- _objc_msgSend$monitor
- _objc_msgSend$observer:provider:observedEvent:object:
- _objc_msgSend$processIntoStringsAndAttachmentsWithContext:completionHandler:
- _objc_msgSend$providers
- _objc_msgSend$registerWithCompletionHandler:
- _objc_msgSend$runningWorkflowControllerSet
- _objc_msgSend$runningWorkflowControllers
- _objc_msgSend$runningWorkflows
- _objc_msgSend$setEventCallback:
- _objc_msgSend$setIdleTimerDisabled:
- _objc_msgSend$springBoardActionButton
- _objc_msgSend$updateAssertions
- _objc_msgSend$updateRunningWorkflowCount
- _objc_msgSend$updateWithCall:
- _objc_msgSend$workflowControllerAssertionTable
- _sharedInstance.onceToken.11934
- _sharedInstance.onceToken.55602
- _sharedInstance.onceToken.8096
- _sharedManager.onceToken.1849
- _sharedManager.onceToken.56625
- _sharedManager.onceToken.57750
- _sharedManager.onceToken.64388
- _sharedManager.onceToken.65824
- _sharedManager.sharedManager.56626
- _sharedManager.sharedManager.57751
- _sharedManager.sharedManager.64390
- _sharedManager.sharedManager.65826
- _sharedRegistry.onceToken.15421
- _sharedRegistry.onceToken.23887
- _sharedRegistry.sharedRegistry.15422
- _sharedRegistry.sharedRegistry.23888
CStrings:
+ "\x01\x14\x17\x13\x1e"
+ "\x13\x1f"
+ "!\x17&"
+ "%s Found Build Products Layout: Flat via inspecting test bundle directory %{public}@ - Using runner %{public}@"
+ "%s Found Build Products Layout: Hierarchical via inspecting test bundle directory %{public}@ - Using runner %{public}@"
+ "%s Test bundle %{public}@ is not under AppleInternal folder"
+ "%s Test runner %{public}@ was not found in AppleInternal/Applications folder"
+ "%s Unable to archive output smart prompt content collection"
+ "%s Unable to locate XCTRunner relative to our test bundle URL %@ - did not find ../PlugIns directory and  did not find ../Tests directory"
+ "%s WFHarnessTestRunnerClient skipping callback because testDelegate does not respond to didFinishRunningHarnessTestsWithResult"
+ "-[WFHarnessTestRunnerClient handleWorkflowRunResult:completion:]"
+ "-[WFSmartPromptConfiguration initWithOutputContentCollection:reference:source:]"
+ "@\"<LNDialogResult>\""
+ "Any of %1$lu Wallet passes or payment cards tapped"
+ "AppleInternal"
+ "Applications/ShortcutsTestHost.app"
+ "B16@?0@\"LNEnumMetadata\"8"
+ "T@\"<LNDialogResult>\",&,N,V_catResult"
+ "T@\"WFAction\",&,N,V_lastExecutedAction"
+ "TB,N,V_allowsHandoff"
+ "TQ,N,V_presentationMode"
+ "Tests"
+ "T{os_unfair_lock_s=I},R,N,V_stateLock"
+ "T{os_unfair_lock_s=I},R,N,V_targetSelectorLock"
+ "Unable to get App Shortcut badge value: %@"
+ "_allowsHandoff"
+ "_connectionLock"
+ "_lastExecutedAction"
+ "_presentationMode"
+ "_stateLock"
+ "_targetSelectorLock"
+ "_uri"
+ "a"
+ "accessSpecifierForCurrentProcess"
+ "allowsHandoff"
+ "apertureIconForActionIdentifier:"
+ "badge"
+ "badgeType"
+ "badgeTypeForEntityIdentifier:error:"
+ "contextualActionIcon"
+ "getObjectRepresentation:forClass:options:"
+ "getting entity badge"
+ "iconWithImageData:scale:displayStyle:"
+ "iconWithImageURL:displayStyle:"
+ "iconWithSystemName:"
+ "initWithName:subtitle:icon:badge:"
+ "initWithOutputContentCollection:reference:source:"
+ "kern.bootsessionuuid"
+ "lastExecutedAction"
+ "localizedOutputContentDescriptionWithContentCollection:"
+ "overrideDoneButtonTitle:"
+ "presentationMode"
+ "processIntoStringsAndAttachmentsWithContext:options:completionHandler:"
+ "saveOutputActionSmartPromtDataForWorkflowReference:completion:"
+ "saveOutputActionSmartPromtDataForWorkflowReference:error:"
+ "setAllowsHandoff:"
+ "setBadgeType:"
+ "setLastExecutedAction:"
+ "setPresentationMode:"
+ "stateLock"
+ "storeSerializedParameters:forIdentifier:queryName:badgeType:error:"
+ "targetSelectorLock"
+ "v32@0:8@\"WFWorkflowReference\"16@?<v@?@\"NSError\">24"
+ "v56@0:8@16@24@32Q40^@48"
- "\x01\x13\x17\x13\x1e"
- "\x01\x14"
- "\x03\x1f"
- "!\x17\x16"
- "%s %@ did not start because it is not currently available"
- "%s Background workflow %@ stopped with error %{public}@"
- "%s Providers (specifically %@) should not be delivering events after invalidation"
- "%s Test bundle %@ is not rooted in a PlugIns folder"
- "%s Unable to update call status with call due to unknown call status"
- "%s Workflow observed a database modification that might involve it, but we're currently running it. Ignoring the change. (%@)"
- "-[WFApplicationVisibilitySystemEventProvider applicationDidAppearEventType] must be overridden"
- "-[WFApplicationVisibilitySystemEventProvider applicationDidDisappearEventType] must be overridden"
- "-[WFCallStatusSystemEventProvider updateWithCall:]"
- "-[WFRunningWorkflowManager updateAssertions]_block_invoke"
- "-[WFSystemEventObserver resume]"
- "-[WFSystemEventObserver resume]_block_invoke"
- "-[WFWorkflow databaseDidChange:modified:inserted:removed:]"
- "@\"CATResult\""
- "@\"TUCallCenter\""
- "@\"WFWorkflow\"24@?0@\"WFWorkflowController\"8Q16"
- "@?<v@?@\"<WFSystemEventProvider>\"q@>16@0:8"
- "ActionButton"
- "Any of %1$lu Wallet passes or payment cards "
- "CallStatusProvider"
- "Class getTUCallCenterClass(void)_block_invoke"
- "Class getTUCallClass(void)_block_invoke"
- "NSNotificationName getTUCallCenterCallStatusChangedNotification(void)"
- "NSNotificationName getTUCallCenterVideoCallStatusChangedNotification(void)"
- "SystemEventObserver"
- "T@\"CATResult\",&,N,V_catResult"
- "T@\"FBSDisplayLayoutMonitor\",R,N,V_monitor"
- "T@\"NSArray\",R,N,V_providers"
- "T@\"NSHashTable\",R,N,V_observers"
- "T@\"NSHashTable\",R,N,V_workflowControllerAssertionTable"
- "T@\"NSMutableOrderedSet\",R,N,V_runningWorkflowControllerSet"
- "T@\"TUCallCenter\",&,N,V_callCenter"
- "T@?,C,N,V_demoResetBlock"
- "T@?,C,N,VeventCallback"
- "TB,N,V_state"
- "TUCall"
- "TUCallCenter"
- "TUCallCenterCallStatusChangedNotification"
- "TUCallCenterVideoCallStatusChangedNotification"
- "WFApplicationVisibilitySystemEventProvider"
- "WFCallStatusSystemEventProvider"
- "WFCallStatusSystemEventProvider.m"
- "WFRunningWorkflowManager"
- "WFSiriVisibilitySystemEventProvider"
- "WFSystemEventObserver"
- "WFSystemEventProvider"
- "WFWorkflowDidStartNotification"
- "WFWorkflowDidStopNotification"
- "_callCenter"
- "_demoResetBlock"
- "_monitor"
- "_providers"
- "_runningWorkflowControllerSet"
- "_workflowControllerAssertionTable"
- "actionForAttribution"
- "addObserver:"
- "applicationDidAppearEventType"
- "applicationDidDisappearEventType"
- "backgroundAssertionWithName:expirationHandler:"
- "call active"
- "call disconnected"
- "call disconnecting"
- "call held"
- "call idle"
- "call ringing"
- "call sending"
- "callCenter"
- "callStatusChanged:"
- "callUUID"
- "canProxyTelephony"
- "com.apple.shortcuts.WFResourceManager.stateAccessQueue"
- "currentAudioAndVideoCalls"
- "dawnFluidity"
- "dawnFluidityEnabled"
- "demoResetBlock"
- "eventCallback"
- "handleLayoutChange:"
- "initWithImageData:scale:displayStyle:"
- "initWithName:subtitle:icon:"
- "initWithProviders:"
- "initWithSystemName:"
- "layoutContainsApplication:"
- "monitor"
- "observer:provider:observedEvent:object:"
- "processIntoStringsAndAttachmentsWithContext:completionHandler:"
- "providers"
- "registerWithCompletionHandler:"
- "runningWorkflowControllerSet"
- "runningWorkflowControllers"
- "runningWorkflows"
- "setCallCenter:"
- "setDemoResetBlock:"
- "setEventCallback:"
- "setIdleTimerDisabled:"
- "siri did appear"
- "siri did disappear"
- "softlink:r:path:/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities"
- "soup spilled oh no"
- "springBoardActionButton"
- "storeSerializedParameters:forIdentifier:queryName:error:"
- "updateAssertions"
- "updateRunningWorkflowCount"
- "updateWithCall:"
- "v24@0:8@?<v@?@\"<WFSystemEventProvider>\"q@>16"
- "v24@?0@\"CATResult\"8@\"NSError\"16"
- "v32@?0@\"<WFSystemEventProvider>\"8q16@24"
- "void *TelephonyUtilitiesLibrary(void)"
- "workflowControllerAssertionTable"
- "workflowControllerDidStart:"
- "workflowControllerDidStop:"

```
