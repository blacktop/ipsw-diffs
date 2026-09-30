## WorkflowKit

> `/System/Library/PrivateFrameworks/WorkflowKit.framework/WorkflowKit`

```diff

-4030.0.2.0.0
-  __TEXT.__text: 0x6c4f34
-  __TEXT.__auth_stubs: 0x7880
-  __TEXT.__objc_methlist: 0x2ec2c
-  __TEXT.__const: 0x11140
+4032.1.0.0.0
+  __TEXT.__text: 0x6d1a0c
+  __TEXT.__auth_stubs: 0x7970
+  __TEXT.__objc_methlist: 0x2ebfc
+  __TEXT.__const: 0x11310
   __TEXT.__dlopen_cstrs: 0xf25
-  __TEXT.__cstring: 0x820cc
-  __TEXT.__swift5_typeref: 0x7378
-  __TEXT.__constg_swiftt: 0x56ec
-  __TEXT.__swift5_fieldmd: 0x3bb4
-  __TEXT.__swift5_builtin: 0x438
+  __TEXT.__cstring: 0x82772
+  __TEXT.__swift5_typeref: 0x74b2
+  __TEXT.__constg_swiftt: 0x57e4
+  __TEXT.__swift5_fieldmd: 0x3c28
+  __TEXT.__swift5_builtin: 0x44c
   __TEXT.__swift5_reflstr: 0x3218
   __TEXT.__swift5_assocty: 0x1338
-  __TEXT.__swift5_proto: 0xcdc
-  __TEXT.__swift5_types: 0x5b4
-  __TEXT.__swift_as_entry: 0x76c
-  __TEXT.__swift_as_ret: 0x914
-  __TEXT.__swift5_capture: 0x1628
-  __TEXT.__oslogstring: 0x1831d
+  __TEXT.__swift5_proto: 0xcf0
+  __TEXT.__swift5_types: 0x5cc
+  __TEXT.__swift_as_entry: 0x778
+  __TEXT.__swift_as_ret: 0x918
+  __TEXT.__swift5_capture: 0x16ec
+  __TEXT.__oslogstring: 0x185e2
   __TEXT.__swift5_protos: 0xb4
   __TEXT.__swift5_mpenum: 0x88
-  __TEXT.__gcc_except_tab: 0x4a50
+  __TEXT.__gcc_except_tab: 0x4a6c
   __TEXT.__ustring: 0x39de
-  __TEXT.__unwind_info: 0x13df0
-  __TEXT.__eh_frame: 0x13dac
-  __TEXT.__objc_classname: 0x7da7
-  __TEXT.__objc_methname: 0x57efc
-  __TEXT.__objc_methtype: 0x968f
-  __TEXT.__objc_stubs: 0x35520
-  __DATA_CONST.__got: 0x4b00
-  __DATA_CONST.__const: 0xdd60
-  __DATA_CONST.__objc_classlist: 0x2128
+  __TEXT.__unwind_info: 0x14040
+  __TEXT.__eh_frame: 0x141d4
+  __TEXT.__objc_classname: 0x7d75
+  __TEXT.__objc_methname: 0x5802e
+  __TEXT.__objc_methtype: 0x9650
+  __TEXT.__objc_stubs: 0x35360
+  __DATA_CONST.__got: 0x4b78
+  __DATA_CONST.__const: 0xdcf8
+  __DATA_CONST.__objc_classlist: 0x2140
   __DATA_CONST.__objc_catlist: 0x3e8
-  __DATA_CONST.__objc_protolist: 0x588
+  __DATA_CONST.__objc_protolist: 0x580
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x120b0
+  __DATA_CONST.__objc_selrefs: 0x12138
   __DATA_CONST.__objc_protorefs: 0x1f0
-  __DATA_CONST.__objc_superrefs: 0x12d8
-  __DATA_CONST.__objc_arraydata: 0x14a0
-  __AUTH_CONST.__auth_got: 0x3c58
-  __AUTH_CONST.__const: 0x29290
-  __AUTH_CONST.__cfstring: 0x28ae0
-  __AUTH_CONST.__objc_const: 0x54640
-  __AUTH_CONST.__objc_dictobj: 0x488
+  __DATA_CONST.__objc_superrefs: 0x12d0
+  __DATA_CONST.__objc_arraydata: 0x14e0
+  __AUTH_CONST.__auth_got: 0x3cd0
+  __AUTH_CONST.__const: 0x2a600
+  __AUTH_CONST.__cfstring: 0x28bc0
+  __AUTH_CONST.__objc_const: 0x545e0
+  __AUTH_CONST.__objc_dictobj: 0x4b0
   __AUTH_CONST.__objc_intobj: 0xed0
   __AUTH_CONST.__objc_arrayobj: 0x978
   __AUTH_CONST.__objc_doubleobj: 0x20
-  __AUTH.__objc_data: 0xe9b0
-  __AUTH.__data: 0x3b80
-  __DATA.__objc_ivar: 0x2690
-  __DATA.__data: 0x8d80
-  __DATA.__bss: 0x16738
+  __AUTH.__objc_data: 0xebe8
+  __AUTH.__data: 0x3ce0
+  __DATA.__objc_ivar: 0x266c
+  __DATA.__data: 0x8df0
+  __DATA.__bss: 0x16948
   __DATA.__common: 0x60
-  __DATA_DIRTY.__objc_data: 0x8790
-  __DATA_DIRTY.__data: 0xc78
+  __DATA_DIRTY.__objc_data: 0x8740
+  __DATA_DIRTY.__data: 0xca8
   __DATA_DIRTY.__bss: 0xd38
   __DATA_DIRTY.__common: 0x10
   - /System/Library/Frameworks/Accelerate.framework/Accelerate

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: C1867666-ADC0-35F5-BC1A-637EE99E6FBA
-  Functions: 30174
-  Symbols:   64962
-  CStrings:  36439
+  UUID: 842C6B1B-4949-3113-9415-A36C9D3E1F31
+  Functions: 30429
+  Symbols:   65080
+  CStrings:  36507
 
Symbols:
+ +[NSUserDefaults(Workflow) markdownRenderingV2Enabled]
+ +[WFWorkflowRecord defaultShowInSearch]
+ -[WFActionOutputVariable variableProviderDidInvalidateOutputDetails:]
+ -[WFAppIntentExecutionAction outputOriginDisplayableAppBundleIdentifier]
+ -[WFCloudKitFolder initWithIdentifier:name:icon:encryptedSchemaVersion:]
+ -[WFDatabase isSavingWorkflowRecordForSync]
+ -[WFDatabase setIsSavingWorkflowRecordForSync:]
+ -[WFDatabase(Shortcuts) visibleReferencesForWorkflowIDs:sortBy:nameContaining:nameEqualing:hasAssociatedAppBundleIdentifier:associatedAppBundleIdentifier:isRecentlyModified:isRecentlyRun:limitTo:]
+ -[WFDatabase(Shortcuts) visibleReferencesForWorkflowIDs:sortByKeys:nameContaining:nameEqualing:hasAssociatedAppBundleIdentifier:associatedAppBundleIdentifier:isRecentlyModified:isRecentlyRun:limitTo:]
+ -[WFDatabase(SmartPrompts) bundleIdentifiersExemptedFromRepromptingUponCountIncrease]
+ -[WFDatabase(SmartPrompts) shouldPromptForCurrentContentItemCount:previousCount:contentOrigin:]
+ -[WFDynamicEnumerationParameter lock_setPossibleStatesCollection:]
+ -[WFDynamicEnumerationParameter possibleStatesLock]
+ -[WFLinkCalculateAppUsageIntentAction iconBackgroundColorName]
+ -[WFLinkCalculateAppUsageIntentAction iconSymbolColorName]
+ -[WFLinkCalculateAppUsageIntentAction iconSymbolName]
+ -[WFLinkCalculateAppUsageIntentAction outputOriginDisplayableAppBundleIdentifier]
+ -[WFLinkPhotosCreateMemoryAction requiredResources]
+ -[WFPBRunActionEvent hasShortcutsId]
+ -[WFPBRunActionEvent setShortcutsId:]
+ -[WFPBRunActionEvent shortcutsId]
+ -[WFRunActionEvent setShortcutsId:]
+ -[WFRunActionEvent shortcutsId]
+ -[WFRunWorkflowAction beginPersistentModeForSpotlightWhenReady]
+ -[WFRunWorkflowAction beginPersistentModeIfReady]
+ -[WFRunWorkflowAction endPersistentModeWithError:]
+ -[WFRunWorkflowAction hasBegunPersistentMode]
+ -[WFRunWorkflowAction setHasBegunPersistentMode:]
+ -[WFRunWorkflowAction setSpotlightReadyForPersistentMode:]
+ -[WFRunWorkflowAction spotlightReadyForPersistentMode]
+ -[WFWorkflow hasOutputAction]
+ -[WFWorkflow setHasOutputAction:]
+ -[WFWorkflow updateSearchAttribution]
+ -[WFWorkflowRecord hasOutputAction]
+ -[WFWorkflowRecord searchAttributionAppBundleIdentifier]
+ -[WFWorkflowRecord setHasOutputAction:]
+ -[WFWorkflowRecord setSearchAttributionAppBundleIdentifier:]
+ -[WFWorkflowRecord setShowInSearch:]
+ -[WFWorkflowRecord showInSearch]
+ -[WFWorkflowReference hasOutputAction]
+ -[WFWorkflowReference initWithIdentifier:name:color:glyphCharacter:associatedAppBundleIdentifier:searchAttributionAppBundleIdentifier:subtitle:actionsDescription:actionCount:syncHash:isDeleted:hiddenFromLibraryAndSync:creationDate:modificationDate:lastRunDate:remoteQuarantineStatus:remoteQuarantineHash:showInSearch:receivesInputFromSearch:hasShortcutInputVariables:disabledOnLockScreen:source:runEventsCount:hasOutputAction:]
+ -[WFWorkflowReference showInSearch]
+ GCC_except_table10014
+ GCC_except_table10015
+ GCC_except_table10016
+ GCC_except_table10018
+ GCC_except_table10020
+ GCC_except_table10022
+ GCC_except_table10025
+ GCC_except_table10030
+ GCC_except_table10035
+ GCC_except_table10046
+ GCC_except_table10201
+ GCC_except_table10221
+ GCC_except_table10224
+ GCC_except_table10262
+ GCC_except_table10430
+ GCC_except_table10436
+ GCC_except_table10455
+ GCC_except_table10609
+ GCC_except_table10643
+ GCC_except_table10709
+ GCC_except_table10716
+ GCC_except_table10718
+ GCC_except_table10720
+ GCC_except_table10748
+ GCC_except_table10753
+ GCC_except_table10793
+ GCC_except_table10796
+ GCC_except_table10799
+ GCC_except_table10802
+ GCC_except_table10998
+ GCC_except_table11092
+ GCC_except_table11109
+ GCC_except_table11131
+ GCC_except_table11173
+ GCC_except_table11494
+ GCC_except_table11520
+ GCC_except_table11523
+ GCC_except_table11611
+ GCC_except_table11886
+ GCC_except_table11892
+ GCC_except_table11895
+ GCC_except_table11898
+ GCC_except_table11901
+ GCC_except_table11906
+ GCC_except_table11913
+ GCC_except_table11918
+ GCC_except_table11921
+ GCC_except_table11924
+ GCC_except_table11927
+ GCC_except_table11930
+ GCC_except_table11933
+ GCC_except_table11936
+ GCC_except_table11939
+ GCC_except_table11942
+ GCC_except_table11945
+ GCC_except_table11948
+ GCC_except_table11951
+ GCC_except_table11954
+ GCC_except_table11976
+ GCC_except_table11977
+ GCC_except_table11978
+ GCC_except_table11979
+ GCC_except_table11984
+ GCC_except_table11985
+ GCC_except_table11990
+ GCC_except_table11991
+ GCC_except_table12092
+ GCC_except_table1228
+ GCC_except_table12288
+ GCC_except_table12483
+ GCC_except_table12498
+ GCC_except_table12504
+ GCC_except_table12506
+ GCC_except_table12511
+ GCC_except_table12574
+ GCC_except_table12587
+ GCC_except_table12595
+ GCC_except_table12636
+ GCC_except_table12673
+ GCC_except_table12687
+ GCC_except_table12689
+ GCC_except_table12691
+ GCC_except_table12774
+ GCC_except_table12790
+ GCC_except_table12896
+ GCC_except_table12946
+ GCC_except_table13001
+ GCC_except_table1301
+ GCC_except_table13030
+ GCC_except_table13084
+ GCC_except_table13095
+ GCC_except_table13139
+ GCC_except_table13141
+ GCC_except_table13459
+ GCC_except_table13492
+ GCC_except_table13609
+ GCC_except_table13638
+ GCC_except_table13644
+ GCC_except_table13691
+ GCC_except_table13785
+ GCC_except_table13798
+ GCC_except_table13801
+ GCC_except_table13813
+ GCC_except_table13820
+ GCC_except_table13821
+ GCC_except_table13831
+ GCC_except_table13842
+ GCC_except_table13968
+ GCC_except_table14038
+ GCC_except_table14043
+ GCC_except_table14047
+ GCC_except_table1406
+ GCC_except_table1411
+ GCC_except_table14238
+ GCC_except_table14306
+ GCC_except_table14551
+ GCC_except_table14581
+ GCC_except_table14697
+ GCC_except_table14865
+ GCC_except_table14870
+ GCC_except_table14879
+ GCC_except_table14882
+ GCC_except_table14999
+ GCC_except_table15022
+ GCC_except_table15033
+ GCC_except_table15036
+ GCC_except_table15351
+ GCC_except_table15402
+ GCC_except_table15416
+ GCC_except_table15419
+ GCC_except_table15613
+ GCC_except_table15740
+ GCC_except_table1736
+ GCC_except_table1749
+ GCC_except_table1754
+ GCC_except_table1756
+ GCC_except_table1758
+ GCC_except_table1995
+ GCC_except_table2071
+ GCC_except_table2152
+ GCC_except_table2162
+ GCC_except_table2333
+ GCC_except_table2341
+ GCC_except_table2371
+ GCC_except_table2524
+ GCC_except_table2551
+ GCC_except_table2619
+ GCC_except_table2656
+ GCC_except_table2772
+ GCC_except_table2775
+ GCC_except_table2789
+ GCC_except_table2881
+ GCC_except_table2934
+ GCC_except_table2951
+ GCC_except_table2957
+ GCC_except_table3169
+ GCC_except_table3192
+ GCC_except_table3202
+ GCC_except_table3226
+ GCC_except_table3230
+ GCC_except_table3255
+ GCC_except_table3287
+ GCC_except_table3303
+ GCC_except_table3307
+ GCC_except_table3366
+ GCC_except_table3379
+ GCC_except_table3382
+ GCC_except_table350
+ GCC_except_table353
+ GCC_except_table3568
+ GCC_except_table3574
+ GCC_except_table3578
+ GCC_except_table3579
+ GCC_except_table3883
+ GCC_except_table3887
+ GCC_except_table4256
+ GCC_except_table4257
+ GCC_except_table4376
+ GCC_except_table4478
+ GCC_except_table4491
+ GCC_except_table4510
+ GCC_except_table4518
+ GCC_except_table4693
+ GCC_except_table4886
+ GCC_except_table4976
+ GCC_except_table4990
+ GCC_except_table5110
+ GCC_except_table5137
+ GCC_except_table5141
+ GCC_except_table5181
+ GCC_except_table5247
+ GCC_except_table5270
+ GCC_except_table5310
+ GCC_except_table536
+ GCC_except_table5366
+ GCC_except_table5371
+ GCC_except_table5373
+ GCC_except_table5499
+ GCC_except_table5505
+ GCC_except_table5521
+ GCC_except_table5894
+ GCC_except_table6038
+ GCC_except_table6107
+ GCC_except_table6204
+ GCC_except_table627
+ GCC_except_table6334
+ GCC_except_table6335
+ GCC_except_table6336
+ GCC_except_table6437
+ GCC_except_table6484
+ GCC_except_table6502
+ GCC_except_table6531
+ GCC_except_table6858
+ GCC_except_table6871
+ GCC_except_table6934
+ GCC_except_table6935
+ GCC_except_table6940
+ GCC_except_table6941
+ GCC_except_table6944
+ GCC_except_table6950
+ GCC_except_table6955
+ GCC_except_table6960
+ GCC_except_table6961
+ GCC_except_table7001
+ GCC_except_table7006
+ GCC_except_table7064
+ GCC_except_table7075
+ GCC_except_table7345
+ GCC_except_table7355
+ GCC_except_table7429
+ GCC_except_table7507
+ GCC_except_table7811
+ GCC_except_table7854
+ GCC_except_table7901
+ GCC_except_table7902
+ GCC_except_table7968
+ GCC_except_table8098
+ GCC_except_table8236
+ GCC_except_table8241
+ GCC_except_table8252
+ GCC_except_table8432
+ GCC_except_table8439
+ GCC_except_table8450
+ GCC_except_table846
+ GCC_except_table9042
+ GCC_except_table9111
+ GCC_except_table9117
+ GCC_except_table9120
+ GCC_except_table9123
+ GCC_except_table9127
+ GCC_except_table9161
+ GCC_except_table919
+ GCC_except_table9215
+ GCC_except_table928
+ GCC_except_table9308
+ GCC_except_table9357
+ GCC_except_table9595
+ GCC_except_table9601
+ GCC_except_table9603
+ GCC_except_table9607
+ GCC_except_table9611
+ GCC_except_table9615
+ GCC_except_table9617
+ GCC_except_table9627
+ GCC_except_table9643
+ GCC_except_table9664
+ GCC_except_table9677
+ GCC_except_table9686
+ GCC_except_table9730
+ GCC_except_table9736
+ GCC_except_table9742
+ OBJC_IVAR_$_WFPBRunActionEvent._shortcutsId
+ _AssistantServicesLibraryCore.frameworkLibrary.54367
+ _ContactsLibrary.53894
+ _ContactsLibrary.67041
+ _ContactsLibraryCore.frameworkLibrary.32239
+ _ContactsLibraryCore.frameworkLibrary.48050
+ _ContactsLibraryCore.frameworkLibrary.53944
+ _ContactsLibraryCore.frameworkLibrary.61577
+ _ContactsLibraryCore.frameworkLibrary.65939
+ _ContactsLibraryCore.frameworkLibrary.67049
+ _CoreLocationLibraryCore.frameworkLibrary.41646
+ _CoreLocationLibraryCore.frameworkLibrary.48072
+ _CoreLocationLibraryCore.frameworkLibrary.59187
+ _CoreLocationLibraryCore.frameworkLibrary.59751
+ _CoreLocationLibraryCore.frameworkLibrary.61936
+ _CoreLocationLibraryCore.frameworkLibrary.63722
+ _CoreLocationLibraryCore.frameworkLibrary.65899
+ _HFTriggerActionSetsBuilderFunction.35702
+ _HFTriggerActionSetsBuilderFunction.38950
+ _HMCharacteristicMetadataFormatBoolFunction.2171
+ _HMCharacteristicMetadataFormatBoolFunction.28296
+ _HMCharacteristicMetadataFormatFloatFunction.2151
+ _HMCharacteristicMetadataFormatIntFunction.2158
+ _HMCharacteristicMetadataFormatIntFunction.28407
+ _HMCharacteristicMetadataFormatStringFunction.2164
+ _HMCharacteristicMetadataFormatUInt16Function.2139
+ _HMCharacteristicMetadataFormatUInt32Function.2132
+ _HMCharacteristicMetadataFormatUInt64Function.2124
+ _HMCharacteristicMetadataFormatUInt8Function.2145
+ _HMCharacteristicMetadataFormatUInt8Function.28414
+ _HomeKitLibrary.sLib.1585
+ _HomeKitLibrary.sLib.2119
+ _HomeKitLibrary.sLib.28276
+ _HomeKitLibrary.sLib.35729
+ _HomeKitLibrary.sLib.36568
+ _HomeKitLibrary.sLib.38961
+ _HomeKitLibrary.sLib.56540
+ _HomeKitLibrary.sOnce.1580
+ _HomeKitLibrary.sOnce.2118
+ _HomeKitLibrary.sOnce.28275
+ _HomeKitLibrary.sOnce.35727
+ _HomeKitLibrary.sOnce.36561
+ _HomeKitLibrary.sOnce.38956
+ _HomeKitLibrary.sOnce.56533
+ _HomeLibrary.sLib.28421
+ _HomeLibrary.sLib.35706
+ _HomeLibrary.sLib.38954
+ _HomeLibrary.sOnce.28417
+ _HomeLibrary.sOnce.35698
+ _HomeLibrary.sOnce.38946
+ _MediaPlayerLibrary.37113
+ _MediaPlayerLibrary.53671
+ _MediaPlayerLibraryCore.frameworkLibrary.37123
+ _MediaPlayerLibraryCore.frameworkLibrary.53678
+ _OBJC_CLASS_$_AFPreferences
+ _OBJC_CLASS_$_NSDimension
+ _OBJC_CLASS_$_WFDatabaseLegacyFolderRecord
+ _OBJC_CLASS_$_WFDatabaseLegacyOrderingRecord
+ _OBJC_CLASS_$_WFLinkPhotosCreateMemoryAction
+ _OBJC_CLASS_$_WFiWorkActionsMigration
+ _OBJC_CLASS_$__TtC11WorkflowKit42WFPhotosMemoryCreationAvailabilityResource
+ _OBJC_IVAR_$_WFDatabase._isSavingWorkflowRecordForSync
+ _OBJC_IVAR_$_WFDynamicEnumerationParameter._possibleStatesLock
+ _OBJC_IVAR_$_WFRunActionEvent._shortcutsId
+ _OBJC_IVAR_$_WFRunWorkflowAction._hasBegunPersistentMode
+ _OBJC_IVAR_$_WFRunWorkflowAction._spotlightReadyForPersistentMode
+ _OBJC_IVAR_$_WFWorkflowRecord._hasOutputAction
+ _OBJC_IVAR_$_WFWorkflowRecord._searchAttributionAppBundleIdentifier
+ _OBJC_IVAR_$_WFWorkflowRecord._showInSearch
+ _OBJC_IVAR_$_WFWorkflowReference._hasOutputAction
+ _OBJC_IVAR_$_WFWorkflowReference._showInSearch
+ _OBJC_METACLASS_$_WFDatabaseLegacyFolderRecord
+ _OBJC_METACLASS_$_WFDatabaseLegacyOrderingRecord
+ _OBJC_METACLASS_$_WFLinkPhotosCreateMemoryAction
+ _OBJC_METACLASS_$_WFiWorkActionsMigration
+ _OBJC_METACLASS_$__TtC11WorkflowKit42WFPhotosMemoryCreationAvailabilityResource
+ _PhotosLibraryCore.frameworkLibrary.1495
+ _ReminderKitLibraryCore.frameworkLibrary.25704
+ _RunningBoardServicesLibrary.27477
+ _RunningBoardServicesLibraryCore.frameworkLibrary.27482
+ _SAObjectsLibrary.sLib.70545
+ _SAObjectsLibrary.sOnce.70543
+ _UIKitLibrary.sLib.16298
+ _UIKitLibrary.sLib.23009
+ _UIKitLibrary.sLib.28688
+ _UIKitLibrary.sLib.29293
+ _UIKitLibrary.sLib.42599
+ _UIKitLibrary.sLib.49556
+ _UIKitLibrary.sLib.58900
+ _UIKitLibrary.sLib.61291
+ _UIKitLibrary.sLib.64389
+ _UIKitLibrary.sOnce.16296
+ _UIKitLibrary.sOnce.23002
+ _UIKitLibrary.sOnce.28681
+ _UIKitLibrary.sOnce.29290
+ _UIKitLibrary.sOnce.42597
+ _UIKitLibrary.sOnce.49546
+ _UIKitLibrary.sOnce.58895
+ _UIKitLibrary.sOnce.61281
+ _UIKitLibrary.sOnce.64379
+ _UIKitLibraryCore.frameworkLibrary.41903
+ _UIPasteboardFunction.42612
+ _UIPasteboardFunction.49551
+ _UIPasteboardFunction.61286
+ _UIPasteboardFunction.64384
+ _VCBundleIdentifierIntelligencePlatformDataActionsExtension
+ _WFDyldBulkImageLoadCallback.25128
+ _WFEnforceClass.10325
+ _WFEnforceClass.1041
+ _WFEnforceClass.13291
+ _WFEnforceClass.13499
+ _WFEnforceClass.1479
+ _WFEnforceClass.15646
+ _WFEnforceClass.16710
+ _WFEnforceClass.16831
+ _WFEnforceClass.17266
+ _WFEnforceClass.17901
+ _WFEnforceClass.1927
+ _WFEnforceClass.2096
+ _WFEnforceClass.21386
+ _WFEnforceClass.21625
+ _WFEnforceClass.22531
+ _WFEnforceClass.23420
+ _WFEnforceClass.23486
+ _WFEnforceClass.25099
+ _WFEnforceClass.25212
+ _WFEnforceClass.29116
+ _WFEnforceClass.29404
+ _WFEnforceClass.29490
+ _WFEnforceClass.29650
+ _WFEnforceClass.29839
+ _WFEnforceClass.30086
+ _WFEnforceClass.30831
+ _WFEnforceClass.31841
+ _WFEnforceClass.32387
+ _WFEnforceClass.3418
+ _WFEnforceClass.35877
+ _WFEnforceClass.36904
+ _WFEnforceClass.37387
+ _WFEnforceClass.3981
+ _WFEnforceClass.40872
+ _WFEnforceClass.42440
+ _WFEnforceClass.43928
+ _WFEnforceClass.46772
+ _WFEnforceClass.47205
+ _WFEnforceClass.47349
+ _WFEnforceClass.49449
+ _WFEnforceClass.50915
+ _WFEnforceClass.51401
+ _WFEnforceClass.57896
+ _WFEnforceClass.58796
+ _WFEnforceClass.59062
+ _WFEnforceClass.61089
+ _WFEnforceClass.6178
+ _WFEnforceClass.61800
+ _WFEnforceClass.63495
+ _WFEnforceClass.63987
+ _WFEnforceClass.64349
+ _WFEnforceClass.64998
+ _WFEnforceClass.65583
+ _WFEnforceClass.67405
+ _WFEnforceClass.71785
+ _WFEnforceClass.72081
+ _WFEnforceClass.72603
+ _WFEnforceClass.74004
+ _WFEnforceClass.74961
+ _WFEnforceClass.75902
+ _WFEnforceClass.7773
+ _WFEnforceClass.8258
+ _WFEnforceClass.8652
+ _WFEnforceClass.8991
+ _WFEnforceClass.9254
+ _WFEnforceClass.9598
+ _WFGroupingPropertyForMediaType.53665
+ _WFLinkActionIdentifierPhotosCreateMemoryMacOS
+ _WFLinkActionIdentifierPhotosCreateMemoryiOS
+ _WFWorkflowHasActionsWithBundleIdentifier
+ _WFWorkflowTypeShowInSearch
+ __CLASS_METHODS_WFiWorkActionsMigration
+ __CLASS_METHODS__TtC11WorkflowKit42WFPhotosMemoryCreationAvailabilityResource
+ __DATA_WFDatabaseLegacyFolderRecord
+ __DATA_WFDatabaseLegacyOrderingRecord
+ __DATA_WFiWorkActionsMigration
+ __DATA__TtC11WorkflowKit42WFPhotosMemoryCreationAvailabilityResource
+ __INSTANCE_METHODS_WFDatabaseLegacyFolderRecord
+ __INSTANCE_METHODS_WFDatabaseLegacyOrderingRecord
+ __INSTANCE_METHODS_WFiWorkActionsMigration
+ __INSTANCE_METHODS__TtC11WorkflowKit42WFPhotosMemoryCreationAvailabilityResource
+ __IVARS_WFDatabaseLegacyFolderRecord
+ __IVARS_WFDatabaseLegacyOrderingRecord
+ __METACLASS_DATA_WFDatabaseLegacyFolderRecord
+ __METACLASS_DATA_WFDatabaseLegacyOrderingRecord
+ __METACLASS_DATA_WFiWorkActionsMigration
+ __METACLASS_DATA__TtC11WorkflowKit42WFPhotosMemoryCreationAvailabilityResource
+ __OBJC_$_CLASS_METHODS_WFDatabase(LegacyFolderSync|ShortcutSync|Library|AccessResources|WFDatabaseProvider|TipKit|TrackedFilesystemNode|ShortcutSuggestions|Sync|AutoShortcutsPreferences|SmartPrompts|Conflicts|Bookmarks|Shortcuts|Triggers|Collections|RunEvents|PersistedSerializedParameters)
+ __OBJC_$_INSTANCE_METHODS_WFDatabase(LegacyFolderSync|ShortcutSync|Library|AccessResources|WFDatabaseProvider|TipKit|TrackedFilesystemNode|ShortcutSuggestions|Sync|AutoShortcutsPreferences|SmartPrompts|Conflicts|Bookmarks|Shortcuts|Triggers|Collections|RunEvents|PersistedSerializedParameters)
+ __OBJC_$_INSTANCE_METHODS_WFLinkPhotosCreateMemoryAction
+ __OBJC_$_PROP_LIST_WFRecordStorage
+ __OBJC_CLASS_PROTOCOLS_$_WFDatabase(LegacyFolderSync|ShortcutSync|Library|AccessResources|WFDatabaseProvider|TipKit|TrackedFilesystemNode|ShortcutSuggestions|Sync|AutoShortcutsPreferences|SmartPrompts|Conflicts|Bookmarks|Shortcuts|Triggers|Collections|RunEvents|PersistedSerializedParameters)
+ __OBJC_CLASS_RO_$_WFLinkPhotosCreateMemoryAction
+ __OBJC_METACLASS_RO_$_WFLinkPhotosCreateMemoryAction
+ __PROPERTIES_WFDatabaseLegacyFolderRecord
+ __PROPERTIES_WFDatabaseLegacyOrderingRecord
+ __PROTOCOLS__TtCE11WorkflowKitCSo20WFWorkflowActionTree14ActionObserver.7
+ ___200-[WFDatabase(Shortcuts) visibleReferencesForWorkflowIDs:sortByKeys:nameContaining:nameEqualing:hasAssociatedAppBundleIdentifier:associatedAppBundleIdentifier:isRecentlyModified:isRecentlyRun:limitTo:]_block_invoke
+ ___38-[WFDatabase(Sync) updateWalrusStatus]_block_invoke.268
+ ___38-[WFDatabase(Sync) updateWalrusStatus]_block_invoke_2.269
+ ___38-[WFWorkflow saveWithCompletionBlock:]_block_invoke.401
+ ___38-[WFWorkflow saveWithCompletionBlock:]_block_invoke_2
+ ___39-[WFDatabase notifyResultsAboutChange:]_block_invoke.300
+ ___39-[WFDatabase notifyResultsAboutChange:]_block_invoke.306
+ ___39-[WFDatabase notifyResultsAboutChange:]_block_invoke_2.304
+ ___39-[WFDatabase notifyResultsAboutChange:]_block_invoke_2.307
+ ___44-[WFBackgroundShortcutRunner unaliveProcess]_block_invoke.346
+ ___44-[WFBackgroundShortcutRunner unaliveProcess]_block_invoke.351
+ ___49-[WFDatabase(Shortcuts) applyConflictResolution:]_block_invoke.301
+ ___49-[WFRunWorkflowAction beginPersistentModeIfReady]_block_invoke
+ ___50-[WFRunWorkflowAction endPersistentModeWithError:]_block_invoke
+ ___55-[WFWorkflow configureAsSingleStepShortcutIfNecessary:]_block_invoke.442
+ ___74-[WFDatabase(Collections) _moveReferences:toIndexes:ofCollectionID:error:]_block_invoke.216
+ ___78-[WFBackgroundShortcutRunner resumeRunningFromContext:withRequest:completion:]_block_invoke.332
+ ___81-[WFDatabase(Shortcuts) deleteReference:tombstone:deleteConflictIfPresent:error:]_block_invoke.271
+ ___82-[WFDatabase initWithStoreDescription:runMigrationsIfNecessary:useLockFile:error:]_block_invoke.246
+ ___84-[WFBackgroundShortcutRunner runActionFromRunRequestData:runningContext:completion:]_block_invoke.295
+ ___84-[WFBackgroundShortcutRunner runActionFromRunRequestData:runningContext:completion:]_block_invoke.297
+ ___84-[WFBackgroundShortcutRunner runActionFromRunRequestData:runningContext:completion:]_block_invoke.302
+ ___84-[WFBackgroundShortcutRunner runActionFromRunRequestData:runningContext:completion:]_block_invoke_2.296
+ ___84-[WFDatabase(Collections) moveCollections:toIndex:ofCollectionWithIdentifier:error:]_block_invoke.230
+ ___85-[WFBackgroundShortcutRunner workflowController:didFinishRunningWithError:cancelled:]_block_invoke.408
+ ___85-[WFBackgroundShortcutRunner workflowController:didFinishRunningWithError:cancelled:]_block_invoke_2.409
+ ___85-[WFDatabase(SmartPrompts) bundleIdentifiersExemptedFromRepromptingUponCountIncrease]_block_invoke
+ ___94-[WFLinkActionProvider createActionsForRequests:allowsActionInDenyList:forceLocalActionsOnly:]_block_invoke.282
+ ___AssistantServicesLibraryCore_block_invoke.54368
+ ___Block_byref_object_copy_.10399
+ ___Block_byref_object_copy_.10685
+ ___Block_byref_object_copy_.11718
+ ___Block_byref_object_copy_.12244
+ ___Block_byref_object_copy_.12589
+ ___Block_byref_object_copy_.13510
+ ___Block_byref_object_copy_.15219
+ ___Block_byref_object_copy_.16292
+ ___Block_byref_object_copy_.18041
+ ___Block_byref_object_copy_.18143
+ ___Block_byref_object_copy_.19385
+ ___Block_byref_object_copy_.20304
+ ___Block_byref_object_copy_.20712
+ ___Block_byref_object_copy_.20792
+ ___Block_byref_object_copy_.22299
+ ___Block_byref_object_copy_.24812
+ ___Block_byref_object_copy_.25376
+ ___Block_byref_object_copy_.26492
+ ___Block_byref_object_copy_.27502
+ ___Block_byref_object_copy_.29279
+ ___Block_byref_object_copy_.2977
+ ___Block_byref_object_copy_.30164
+ ___Block_byref_object_copy_.31809
+ ___Block_byref_object_copy_.35436
+ ___Block_byref_object_copy_.35710
+ ___Block_byref_object_copy_.37135
+ ___Block_byref_object_copy_.38009
+ ___Block_byref_object_copy_.41448
+ ___Block_byref_object_copy_.42281
+ ___Block_byref_object_copy_.42591
+ ___Block_byref_object_copy_.43801
+ ___Block_byref_object_copy_.46793
+ ___Block_byref_object_copy_.46988
+ ___Block_byref_object_copy_.48147
+ ___Block_byref_object_copy_.49431
+ ___Block_byref_object_copy_.49888
+ ___Block_byref_object_copy_.5187
+ ___Block_byref_object_copy_.54360
+ ___Block_byref_object_copy_.56060
+ ___Block_byref_object_copy_.56959
+ ___Block_byref_object_copy_.57297
+ ___Block_byref_object_copy_.58137
+ ___Block_byref_object_copy_.59235
+ ___Block_byref_object_copy_.59654
+ ___Block_byref_object_copy_.60771
+ ___Block_byref_object_copy_.61437
+ ___Block_byref_object_copy_.61932
+ ___Block_byref_object_copy_.6290
+ ___Block_byref_object_copy_.64092
+ ___Block_byref_object_copy_.64692
+ ___Block_byref_object_copy_.64977
+ ___Block_byref_object_copy_.66040
+ ___Block_byref_object_copy_.68246
+ ___Block_byref_object_copy_.70229
+ ___Block_byref_object_copy_.71126
+ ___Block_byref_object_copy_.72181
+ ___Block_byref_object_copy_.72988
+ ___Block_byref_object_copy_.7387
+ ___Block_byref_object_copy_.74646
+ ___Block_byref_object_copy_.8536
+ ___Block_byref_object_copy_.9728
+ ___Block_byref_object_copy_.9773
+ ___Block_byref_object_dispose_.10400
+ ___Block_byref_object_dispose_.10686
+ ___Block_byref_object_dispose_.11719
+ ___Block_byref_object_dispose_.12245
+ ___Block_byref_object_dispose_.12590
+ ___Block_byref_object_dispose_.13511
+ ___Block_byref_object_dispose_.15220
+ ___Block_byref_object_dispose_.16293
+ ___Block_byref_object_dispose_.18042
+ ___Block_byref_object_dispose_.18144
+ ___Block_byref_object_dispose_.19386
+ ___Block_byref_object_dispose_.20305
+ ___Block_byref_object_dispose_.20713
+ ___Block_byref_object_dispose_.20793
+ ___Block_byref_object_dispose_.22300
+ ___Block_byref_object_dispose_.24813
+ ___Block_byref_object_dispose_.25377
+ ___Block_byref_object_dispose_.26493
+ ___Block_byref_object_dispose_.27503
+ ___Block_byref_object_dispose_.29280
+ ___Block_byref_object_dispose_.2978
+ ___Block_byref_object_dispose_.30165
+ ___Block_byref_object_dispose_.31810
+ ___Block_byref_object_dispose_.35437
+ ___Block_byref_object_dispose_.35711
+ ___Block_byref_object_dispose_.37136
+ ___Block_byref_object_dispose_.38010
+ ___Block_byref_object_dispose_.41449
+ ___Block_byref_object_dispose_.42282
+ ___Block_byref_object_dispose_.42592
+ ___Block_byref_object_dispose_.43802
+ ___Block_byref_object_dispose_.46794
+ ___Block_byref_object_dispose_.46989
+ ___Block_byref_object_dispose_.48148
+ ___Block_byref_object_dispose_.49432
+ ___Block_byref_object_dispose_.49889
+ ___Block_byref_object_dispose_.5188
+ ___Block_byref_object_dispose_.54361
+ ___Block_byref_object_dispose_.56061
+ ___Block_byref_object_dispose_.56960
+ ___Block_byref_object_dispose_.57298
+ ___Block_byref_object_dispose_.58138
+ ___Block_byref_object_dispose_.59236
+ ___Block_byref_object_dispose_.59655
+ ___Block_byref_object_dispose_.60772
+ ___Block_byref_object_dispose_.61438
+ ___Block_byref_object_dispose_.61933
+ ___Block_byref_object_dispose_.6291
+ ___Block_byref_object_dispose_.64093
+ ___Block_byref_object_dispose_.64693
+ ___Block_byref_object_dispose_.64978
+ ___Block_byref_object_dispose_.66041
+ ___Block_byref_object_dispose_.68247
+ ___Block_byref_object_dispose_.70230
+ ___Block_byref_object_dispose_.71127
+ ___Block_byref_object_dispose_.72182
+ ___Block_byref_object_dispose_.72989
+ ___Block_byref_object_dispose_.7388
+ ___Block_byref_object_dispose_.74647
+ ___Block_byref_object_dispose_.8537
+ ___Block_byref_object_dispose_.9729
+ ___Block_byref_object_dispose_.9774
+ ___ContactsLibraryCore_block_invoke.32240
+ ___ContactsLibraryCore_block_invoke.48051
+ ___ContactsLibraryCore_block_invoke.53945
+ ___ContactsLibraryCore_block_invoke.61578
+ ___ContactsLibraryCore_block_invoke.65940
+ ___ContactsLibraryCore_block_invoke.67050
+ ___CoreLocationLibraryCore_block_invoke.41647
+ ___CoreLocationLibraryCore_block_invoke.48073
+ ___CoreLocationLibraryCore_block_invoke.59188
+ ___CoreLocationLibraryCore_block_invoke.59752
+ ___CoreLocationLibraryCore_block_invoke.61937
+ ___CoreLocationLibraryCore_block_invoke.63723
+ ___CoreLocationLibraryCore_block_invoke.65900
+ ___HomeKitLibrary_block_invoke.1583
+ ___HomeKitLibrary_block_invoke.2126
+ ___HomeKitLibrary_block_invoke.28281
+ ___HomeKitLibrary_block_invoke.35735
+ ___HomeKitLibrary_block_invoke.36566
+ ___HomeKitLibrary_block_invoke.38959
+ ___HomeKitLibrary_block_invoke.56538
+ ___HomeLibrary_block_invoke.28419
+ ___HomeLibrary_block_invoke.35704
+ ___HomeLibrary_block_invoke.38952
+ ___MediaPlayerLibraryCore_block_invoke.37124
+ ___MediaPlayerLibraryCore_block_invoke.53679
+ ___PhotosLibraryCore_block_invoke.1496
+ ___ReminderKitLibraryCore_block_invoke.25705
+ ___RunningBoardServicesLibraryCore_block_invoke.27483
+ ___SAObjectsLibrary_block_invoke.70549
+ ___UIKitLibraryCore_block_invoke.41904
+ ___UIKitLibrary_block_invoke.16303
+ ___UIKitLibrary_block_invoke.23007
+ ___UIKitLibrary_block_invoke.28686
+ ___UIKitLibrary_block_invoke.29292
+ ___UIKitLibrary_block_invoke.42605
+ ___UIKitLibrary_block_invoke.49554
+ ___UIKitLibrary_block_invoke.58898
+ ___UIKitLibrary_block_invoke.61289
+ ___UIKitLibrary_block_invoke.64387
+ ___WFUpdateSmartPromptChangesToShortcutChanges_block_invoke.604
+ ___block_descriptor_32_e43_"NSString"24?0"WFWorkflowCollection"8Q16l
+ ___block_descriptor_91_e8_32s40s48s56s64s72s_e27_"WFDatabaseResult"16?0^8ls32l8s40l8s48l8s56l8s64l8s72l8
+ ___block_literal_global.10316
+ ___block_literal_global.1093
+ ___block_literal_global.10991
+ ___block_literal_global.11250
+ ___block_literal_global.11330
+ ___block_literal_global.12251
+ ___block_literal_global.1259
+ ___block_literal_global.12608
+ ___block_literal_global.1290
+ ___block_literal_global.13247
+ ___block_literal_global.13300
+ ___block_literal_global.13503
+ ___block_literal_global.13733
+ ___block_literal_global.13858
+ ___block_literal_global.1394
+ ___block_literal_global.14423
+ ___block_literal_global.14506
+ ___block_literal_global.14735
+ ___block_literal_global.15676
+ ___block_literal_global.15869
+ ___block_literal_global.1622
+ ___block_literal_global.16297
+ ___block_literal_global.1714
+ ___block_literal_global.172.22636
+ ___block_literal_global.176.45899
+ ___block_literal_global.178.29653
+ ___block_literal_global.178.39895
+ ___block_literal_global.178.69490
+ ___block_literal_global.178.74663
+ ___block_literal_global.179.26538
+ ___block_literal_global.180.36477
+ ___block_literal_global.18189
+ ___block_literal_global.183.72192
+ ___block_literal_global.183.74690
+ ___block_literal_global.186.52527
+ ___block_literal_global.186.72196
+ ___block_literal_global.186.74691
+ ___block_literal_global.18881
+ ___block_literal_global.189.45926
+ ___block_literal_global.189.60225
+ ___block_literal_global.189.60573
+ ___block_literal_global.189.74955
+ ___block_literal_global.18982
+ ___block_literal_global.191.60574
+ ___block_literal_global.191.72200
+ ___block_literal_global.192.6281
+ ___block_literal_global.19293
+ ___block_literal_global.193.25384
+ ___block_literal_global.193.45929
+ ___block_literal_global.193.66771
+ ___block_literal_global.194.72183
+ ___block_literal_global.195.29177
+ ___block_literal_global.19613
+ ___block_literal_global.19728
+ ___block_literal_global.199.18169
+ ___block_literal_global.199.45178
+ ___block_literal_global.199.57103
+ ___block_literal_global.201.60215
+ ___block_literal_global.202.18166
+ ___block_literal_global.202.21175
+ ___block_literal_global.202.56885
+ ___block_literal_global.203.46264
+ ___block_literal_global.205.25360
+ ___block_literal_global.206.60217
+ ___block_literal_global.20687
+ ___block_literal_global.208.49453
+ ___block_literal_global.2103
+ ___block_literal_global.21199
+ ___block_literal_global.219.68696
+ ___block_literal_global.221
+ ___block_literal_global.22100
+ ___block_literal_global.225.26834
+ ___block_literal_global.225.60200
+ ___block_literal_global.22521
+ ___block_literal_global.2256
+ ___block_literal_global.227.74637
+ ___block_literal_global.22707
+ ___block_literal_global.22805
+ ___block_literal_global.230.41499
+ ___block_literal_global.23003
+ ___block_literal_global.23066
+ ___block_literal_global.232.43403
+ ___block_literal_global.23295
+ ___block_literal_global.233
+ ___block_literal_global.23478
+ ___block_literal_global.238.60891
+ ___block_literal_global.239.74604
+ ___block_literal_global.24009
+ ___block_literal_global.244
+ ___block_literal_global.246
+ ___block_literal_global.247.37203
+ ___block_literal_global.24829
+ ___block_literal_global.251.55317
+ ___block_literal_global.251.68270
+ ___block_literal_global.25119
+ ___block_literal_global.252
+ ___block_literal_global.25215
+ ___block_literal_global.25342
+ ___block_literal_global.25654
+ ___block_literal_global.26218
+ ___block_literal_global.26515
+ ___block_literal_global.2667
+ ___block_literal_global.26824
+ ___block_literal_global.27059
+ ___block_literal_global.27558
+ ___block_literal_global.277.41430
+ ___block_literal_global.2820
+ ___block_literal_global.28270
+ ___block_literal_global.283.47106
+ ___block_literal_global.284.7484
+ ___block_literal_global.28682
+ ___block_literal_global.2886
+ ___block_literal_global.29197
+ ___block_literal_global.29282
+ ___block_literal_global.294.7873
+ ___block_literal_global.29405
+ ___block_literal_global.295
+ ___block_literal_global.2959
+ ___block_literal_global.29659
+ ___block_literal_global.29818
+ ___block_literal_global.30148
+ ___block_literal_global.305.58902
+ ___block_literal_global.311.58989
+ ___block_literal_global.312
+ ___block_literal_global.315
+ ___block_literal_global.31675
+ ___block_literal_global.33720
+ ___block_literal_global.34439
+ ___block_literal_global.348.41561
+ ___block_literal_global.348.8746
+ ___block_literal_global.35474
+ ___block_literal_global.357.41590
+ ___block_literal_global.35728
+ ___block_literal_global.3582
+ ___block_literal_global.36026
+ ___block_literal_global.364
+ ___block_literal_global.36473
+ ___block_literal_global.36562
+ ___block_literal_global.37042
+ ___block_literal_global.37201
+ ___block_literal_global.37406
+ ___block_literal_global.376
+ ___block_literal_global.38016
+ ___block_literal_global.38933
+ ___block_literal_global.391
+ ___block_literal_global.39536
+ ___block_literal_global.396
+ ___block_literal_global.398
+ ___block_literal_global.3985
+ ___block_literal_global.39894
+ ___block_literal_global.400
+ ___block_literal_global.404
+ ___block_literal_global.40716
+ ___block_literal_global.41180
+ ___block_literal_global.41498
+ ___block_literal_global.41682
+ ___block_literal_global.42316
+ ___block_literal_global.42441
+ ___block_literal_global.42598
+ ___block_literal_global.428
+ ___block_literal_global.42805
+ ___block_literal_global.430
+ ___block_literal_global.43431
+ ___block_literal_global.44034
+ ___block_literal_global.44137
+ ___block_literal_global.44464
+ ___block_literal_global.44542
+ ___block_literal_global.45181
+ ___block_literal_global.454.33661
+ ___block_literal_global.45655
+ ___block_literal_global.457.7398
+ ___block_literal_global.45908
+ ___block_literal_global.46258
+ ___block_literal_global.46368
+ ___block_literal_global.466
+ ___block_literal_global.469.67616
+ ___block_literal_global.47096
+ ___block_literal_global.47150
+ ___block_literal_global.47408
+ ___block_literal_global.477.67617
+ ___block_literal_global.478
+ ___block_literal_global.48167
+ ___block_literal_global.482
+ ___block_literal_global.49210
+ ___block_literal_global.49420
+ ___block_literal_global.49547
+ ___block_literal_global.49737
+ ___block_literal_global.49833
+ ___block_literal_global.50099
+ ___block_literal_global.51027
+ ___block_literal_global.51052
+ ___block_literal_global.51691
+ ___block_literal_global.51701
+ ___block_literal_global.52332
+ ___block_literal_global.52526
+ ___block_literal_global.52862
+ ___block_literal_global.52923
+ ___block_literal_global.53649
+ ___block_literal_global.5394
+ ___block_literal_global.53950
+ ___block_literal_global.54356
+ ___block_literal_global.54642
+ ___block_literal_global.54698
+ ___block_literal_global.55315
+ ___block_literal_global.55505
+ ___block_literal_global.55981
+ ___block_literal_global.5614
+ ___block_literal_global.56167
+ ___block_literal_global.56534
+ ___block_literal_global.56966
+ ___block_literal_global.57102
+ ___block_literal_global.57588
+ ___block_literal_global.57793
+ ___block_literal_global.59042
+ ___block_literal_global.59177
+ ___block_literal_global.60236
+ ___block_literal_global.60572
+ ___block_literal_global.60934
+ ___block_literal_global.61152
+ ___block_literal_global.61282
+ ___block_literal_global.61476
+ ___block_literal_global.61540
+ ___block_literal_global.625
+ ___block_literal_global.6278
+ ___block_literal_global.6344
+ ___block_literal_global.63595
+ ___block_literal_global.63673
+ ___block_literal_global.63984
+ ___block_literal_global.64341
+ ___block_literal_global.64380
+ ___block_literal_global.65300
+ ___block_literal_global.65917
+ ___block_literal_global.66780
+ ___block_literal_global.6699
+ ___block_literal_global.67037
+ ___block_literal_global.67075
+ ___block_literal_global.67449
+ ___block_literal_global.67771
+ ___block_literal_global.68014
+ ___block_literal_global.68329
+ ___block_literal_global.68695
+ ___block_literal_global.69181
+ ___block_literal_global.69259
+ ___block_literal_global.69332
+ ___block_literal_global.69495
+ ___block_literal_global.69842
+ ___block_literal_global.70226
+ ___block_literal_global.703.43137
+ ___block_literal_global.70544
+ ___block_literal_global.70711
+ ___block_literal_global.71060
+ ___block_literal_global.71465
+ ___block_literal_global.71602
+ ___block_literal_global.717
+ ___block_literal_global.71959
+ ___block_literal_global.72212
+ ___block_literal_global.726
+ ___block_literal_global.73006
+ ___block_literal_global.74434
+ ___block_literal_global.74661
+ ___block_literal_global.74976
+ ___block_literal_global.75677
+ ___block_literal_global.7580
+ ___block_literal_global.76575
+ ___block_literal_global.790
+ ___block_literal_global.7900
+ ___block_literal_global.8251
+ ___block_literal_global.8774
+ ___block_literal_global.9006
+ ___block_literal_global.916
+ ___block_literal_global.9422
+ ___block_literal_global.9686
+ ___getCLPlacemarkClass_block_invoke.59750
+ ___getCLPlacemarkClass_block_invoke.61935
+ ___getCLPlacemarkClass_block_invoke.65898
+ ___getCNContactStoreClass_block_invoke.67039
+ ___getMPMediaItemClass_block_invoke.53664
+ ___getMPMediaPropertyPredicateClass_block_invoke.37093
+ ___getMPMediaPropertyPredicateClass_block_invoke.53662
+ ___getMPMediaQueryClass_block_invoke.37096
+ ___getMPMediaQueryClass_block_invoke.53667
+ ___swift_assignWithCopy_strong
+ ___swift_assignWithTake_strong
+ ___swift_deallocate_boxed_opaque_existential_0
+ ___swift_destroy_strong
+ ___swift_initWithCopy_strong
+ __mutableRegisteredDefinitions.69267
+ _associated conformance 11WorkflowKit21LegacyFolderSyncError33_8A9DDB030552BA6036B004F4F1352C40LLOSHAASQ
+ _audit_stringAssistantServices.54383
+ _audit_stringContacts.32254
+ _audit_stringContacts.48065
+ _audit_stringContacts.53948
+ _audit_stringContacts.61582
+ _audit_stringContacts.65943
+ _audit_stringContacts.67056
+ _audit_stringCoreLocation.41662
+ _audit_stringCoreLocation.48077
+ _audit_stringCoreLocation.59191
+ _audit_stringCoreLocation.59766
+ _audit_stringCoreLocation.61951
+ _audit_stringCoreLocation.63736
+ _audit_stringCoreLocation.65914
+ _audit_stringMediaPlayer.37130
+ _audit_stringMediaPlayer.53685
+ _audit_stringPhotos.1502
+ _audit_stringReminderKit.25711
+ _audit_stringRunningBoardServices.27489
+ _audit_stringUIKit.41918
+ _block_copy_helper.180
+ _block_copy_helper.191
+ _block_copy_helper.38
+ _block_copy_helper.58
+ _block_copy_helper.68
+ _block_descriptor.182
+ _block_descriptor.193
+ _block_descriptor.40
+ _block_descriptor.60
+ _block_descriptor.70
+ _block_destroy_helper.181
+ _block_destroy_helper.192
+ _block_destroy_helper.39
+ _block_destroy_helper.59
+ _block_destroy_helper.69
+ _bundleIdentifiersExemptedFromRepromptingUponCountIncrease.onceToken
+ _bundleIdentifiersExemptedFromRepromptingUponCountIncrease.set
+ _classHFTriggerActionSetsBuilder.35700
+ _classHFTriggerActionSetsBuilder.38948
+ _classRegistrationLock.52239
+ _classRegistrationLock.72574
+ _classRegistrationLock.9204
+ _classUIPasteboard.42610
+ _classUIPasteboard.49549
+ _classUIPasteboard.61284
+ _classUIPasteboard.64382
+ _constantHMCharacteristicMetadataFormatBool.2169
+ _constantHMCharacteristicMetadataFormatBool.28294
+ _constantHMCharacteristicMetadataFormatFloat.2149
+ _constantHMCharacteristicMetadataFormatInt.2156
+ _constantHMCharacteristicMetadataFormatInt.28405
+ _constantHMCharacteristicMetadataFormatString.2162
+ _constantHMCharacteristicMetadataFormatUInt16.2137
+ _constantHMCharacteristicMetadataFormatUInt32.2130
+ _constantHMCharacteristicMetadataFormatUInt64.2122
+ _constantHMCharacteristicMetadataFormatUInt8.2143
+ _constantHMCharacteristicMetadataFormatUInt8.28412
+ _getCLPlacemarkClass.65833
+ _getCLPlacemarkClass.softClass.59749
+ _getCLPlacemarkClass.softClass.61934
+ _getCLPlacemarkClass.softClass.65897
+ _getCNContactStoreClass.softClass.67038
+ _getHFTriggerActionSetsBuilderClass.35688
+ _getHFTriggerActionSetsBuilderClass.38943
+ _getHMCharacteristicMetadataFormatBool.2108
+ _getHMCharacteristicMetadataFormatBool.28289
+ _getHMCharacteristicMetadataFormatFloat.2111
+ _getHMCharacteristicMetadataFormatInt.2110
+ _getHMCharacteristicMetadataFormatInt.28400
+ _getHMCharacteristicMetadataFormatString.2109
+ _getHMCharacteristicMetadataFormatUInt16.2113
+ _getHMCharacteristicMetadataFormatUInt32.2114
+ _getHMCharacteristicMetadataFormatUInt64.2115
+ _getHMCharacteristicMetadataFormatUInt8.2112
+ _getHMCharacteristicMetadataFormatUInt8.28399
+ _getMPMediaItemClass.softClass.53663
+ _getMPMediaPropertyPredicateClass.softClass.37092
+ _getMPMediaPropertyPredicateClass.softClass.53661
+ _getMPMediaQueryClass.softClass.37095
+ _getMPMediaQueryClass.softClass.53666
+ _getUIPasteboardClass.42595
+ _getUIPasteboardClass.49543
+ _getUIPasteboardClass.61275
+ _getUIPasteboardClass.64375
+ _initHFTriggerActionSetsBuilder.35697
+ _initHFTriggerActionSetsBuilder.38945
+ _initHMCharacteristicMetadataFormatBool.2166
+ _initHMCharacteristicMetadataFormatBool.28291
+ _initHMCharacteristicMetadataFormatFloat.2147
+ _initHMCharacteristicMetadataFormatInt.2153
+ _initHMCharacteristicMetadataFormatInt.28402
+ _initHMCharacteristicMetadataFormatString.2160
+ _initHMCharacteristicMetadataFormatUInt16.2134
+ _initHMCharacteristicMetadataFormatUInt32.2128
+ _initHMCharacteristicMetadataFormatUInt64.2117
+ _initHMCharacteristicMetadataFormatUInt8.2141
+ _initHMCharacteristicMetadataFormatUInt8.28409
+ _initUIPasteboard.42608
+ _initUIPasteboard.49545
+ _initUIPasteboard.61280
+ _initUIPasteboard.64378
+ _nw_parameters_set_include_peer_to_peer
+ _objc_msgSend$beginPersistentModeForSpotlightWhenReady
+ _objc_msgSend$beginPersistentModeIfReady
+ _objc_msgSend$bundleIdentifiersExemptedFromRepromptingUponCountIncrease
+ _objc_msgSend$endPersistentModeWithError:
+ _objc_msgSend$fullyQualifiedTypeName
+ _objc_msgSend$hasBegunPersistentMode
+ _objc_msgSend$hasDeltaFromOther
+ _objc_msgSend$hasOutputAction
+ _objc_msgSend$initWithIdentifier:name:color:glyphCharacter:associatedAppBundleIdentifier:searchAttributionAppBundleIdentifier:subtitle:actionsDescription:actionCount:syncHash:isDeleted:hiddenFromLibraryAndSync:creationDate:modificationDate:lastRunDate:remoteQuarantineStatus:remoteQuarantineHash:showInSearch:receivesInputFromSearch:hasShortcutInputVariables:disabledOnLockScreen:source:runEventsCount:hasOutputAction:
+ _objc_msgSend$isSavingWorkflowRecordForSync
+ _objc_msgSend$lock_setPossibleStatesCollection:
+ _objc_msgSend$outputOriginDisplayableAppBundleIdentifier
+ _objc_msgSend$searchAttributionAppBundleIdentifier
+ _objc_msgSend$setHasBegunPersistentMode:
+ _objc_msgSend$setHasOutputAction:
+ _objc_msgSend$setSearchAttributionAppBundleIdentifier:
+ _objc_msgSend$setShortcutsId:
+ _objc_msgSend$setShowInSearch:
+ _objc_msgSend$setSpotlightReadyForPersistentMode:
+ _objc_msgSend$shouldPromptForCurrentContentItemCount:previousCount:contentOrigin:
+ _objc_msgSend$showInSearch
+ _objc_msgSend$spotlightReadyForPersistentMode
+ _objc_msgSend$updateSearchAttribution
+ _objc_msgSend$visibleReferencesForWorkflowIDs:sortByKeys:nameContaining:nameEqualing:hasAssociatedAppBundleIdentifier:associatedAppBundleIdentifier:isRecentlyModified:isRecentlyRun:limitTo:
+ _objectdestroy.119Tm
+ _objectdestroy.122Tm
+ _objectdestroy.129Tm
+ _objectdestroy.139Tm
+ _objectdestroy.152Tm
+ _objectdestroy.162Tm
+ _objectdestroy.195Tm
+ _os_unfair_lock_assert_not_owner
+ _rediscoverDefinitionsIfNeeded.calledDefinitionVendingSelectors.69260
+ _rediscoverDefinitionsIfNeeded.lock.69262
+ _rediscoverDefinitionsIfNeeded.onceToken.69258
+ _sharedInstance.onceToken.12607
+ _sharedInstance.onceToken.59041
+ _sharedInstance.onceToken.9005
+ _sharedManager.onceToken.1621
+ _sharedManager.onceToken.60586
+ _sharedManager.onceToken.68328
+ _sharedManager.sharedManager.60587
+ _sharedManager.sharedManager.68330
+ _sharedRegistry.onceToken.16481
+ _sharedRegistry.onceToken.25413
+ _sharedRegistry.sharedRegistry.16482
+ _sharedRegistry.sharedRegistry.25414
+ _symbolic SAySo7NSErrorCSgGSgypSgIgyr_
+ _symbolic So28WFDatabaseLegacyFolderRecordC______pIgrzo_ s5ErrorP
+ _symbolic So30WFDatabaseLegacyOrderingRecordC______pIgrzo_ s5ErrorP
+ _symbolic _____ 11WorkflowKit21LegacyFolderSyncError33_8A9DDB030552BA6036B004F4F1352C40LLO
+ _symbolic _____ 11WorkflowKit21iWorkActionsMigrationC
+ _symbolic _____ 11WorkflowKit23LocaleChangesetProducerV
+ _symbolic _____ 11WorkflowKit23WFSpotlightQueryBuilderC20MeasurementFormatterV
+ _symbolic _____ 11WorkflowKit42WFPhotosMemoryCreationAvailabilityResourceC
+ _symbolic _____ So35WFDatabaseLegacyRecordSyncOperationV
+ _symbolic _____Sg 16GenerativeModels0aB12AvailabilityV0C0O14RestrictedInfoV0D6ReasonO
+ _symbolic _____Sg 7ToolKit18RestrictionContextO30PersonRepresentationDefinitionO
+ _symbolic ___________pIgrzo_ So35WFDatabaseLegacyRecordSyncOperationV s5ErrorP
+ _symbolic _____ySS_So11NSDimensionCtG s23_ContiguousArrayStorageC
+ _symbolic _____ySo11NSDimensionCG 10Foundation11MeasurementV
+ _symbolic _____y_____G s23_ContiguousArrayStorageC 7ToolKit18RestrictionContextO30PersonRepresentationDefinitionO
+ _symbolic ytSg
+ _symbolic ytSg______pIgrzo_ s5ErrorP
+ _symbolic yt______pIgrzo_ s5ErrorP
- -[WFCloudKitFolder initWithCollectionRecord:identifier:]
- -[WFCoreDataCollection(RecordStorage) deserializedLastRemoteShortcutOrderingSubset]
- -[WFCoreDataCollection(RecordStorage) setDeserializedLastRemoteShortcutOrderingSubset:]
- -[WFCoreDataCollectionModel .cxx_destruct]
- -[WFCoreDataCollectionModel cloudKitFolderRecordMetadata]
- -[WFCoreDataCollectionModel cloudKitOrderingRecordMetadata]
- -[WFCoreDataCollectionModel collectionOrdering]
- -[WFCoreDataCollectionModel coreDataCollection]
- -[WFCoreDataCollectionModel database]
- -[WFCoreDataCollectionModel glyphCharacter]
- -[WFCoreDataCollectionModel identifier]
- -[WFCoreDataCollectionModel initWithManagedObject:database:]
- -[WFCoreDataCollectionModel isDeleted]
- -[WFCoreDataCollectionModel isFolder]
- -[WFCoreDataCollectionModel isRootCollection]
- -[WFCoreDataCollectionModel lastRemoteCollectionOrderingSubset]
- -[WFCoreDataCollectionModel lastRemoteCollectionOrdering]
- -[WFCoreDataCollectionModel lastRemoteShortcutOrderingSubset]
- -[WFCoreDataCollectionModel lastRemoteShortcutOrdering]
- -[WFCoreDataCollectionModel lastSyncedEncryptedSchemaVersion]
- -[WFCoreDataCollectionModel lastSyncedHash]
- -[WFCoreDataCollectionModel managedObject]
- -[WFCoreDataCollectionModel name]
- -[WFCoreDataCollectionModel setCloudKitFolderRecordMetadata:]
- -[WFCoreDataCollectionModel setCloudKitOrderingRecordMetadata:]
- -[WFCoreDataCollectionModel setCollectionOrdering:]
- -[WFCoreDataCollectionModel setGlyphCharacter:]
- -[WFCoreDataCollectionModel setLastRemoteCollectionOrdering:]
- -[WFCoreDataCollectionModel setLastRemoteCollectionOrderingSubset:]
- -[WFCoreDataCollectionModel setLastRemoteShortcutOrdering:]
- -[WFCoreDataCollectionModel setLastRemoteShortcutOrderingSubset:]
- -[WFCoreDataCollectionModel setLastSyncedEncryptedSchemaVersion:]
- -[WFCoreDataCollectionModel setLastSyncedHash:]
- -[WFCoreDataCollectionModel setName:]
- -[WFCoreDataCollectionModel setShortcutOrdering:]
- -[WFCoreDataCollectionModel setWantedEncryptedSchemaVersion:]
- -[WFCoreDataCollectionModel shortcutOrdering]
- -[WFCoreDataCollectionModel wantedEncryptedSchemaVersion]
- -[WFCoreDataCollectionModel workflowType]
- -[WFDatabase destroysOnDeallocation]
- -[WFDatabase setDestroysOnDeallocation:]
- -[WFDatabase(Collections) allCollections]
- -[WFDatabase(Collections) collectionRecordForCollectionIdentifier:createIfNecessary:]
- -[WFDatabase(Collections) deletedFolders]
- -[WFDatabase(Shortcuts) hasWorkflowWithID:]
- -[WFDatabase(Shortcuts) visibleReferencesForWorkflowIDs:sortBy:nameContaining:nameEqualing:hasAssociatedAppBundleIdentifier:associatedAppBundleIdentifier:hasTombstonedConflicts:isRecentlyModified:isRecentlyRun:limitTo:]
- -[WFDatabase(Shortcuts) visibleReferencesForWorkflowIDs:sortByKeys:nameContaining:nameEqualing:hasAssociatedAppBundleIdentifier:associatedAppBundleIdentifier:hasTombstonedConflicts:isRecentlyModified:isRecentlyRun:limitTo:]
- -[WFDatabase(Shortcuts) workflowsWithTombstonedConflicts]
- -[WFDatabase(SmartPrompts) shouldPromptForCurrentContentItemCount:previousCount:]
- -[WFLinkCalculateAppUsageIntentAction icon]
- -[WFVariable variableProvider:variableWasMoved:]
- -[WFWorkflow setActionTree:]
- -[WFWorkflowCollectionRecord .cxx_destruct]
- -[WFWorkflowCollectionRecord cloudKitFolderRecordMetadata]
- -[WFWorkflowCollectionRecord cloudKitOrderingRecordMetadata]
- -[WFWorkflowCollectionRecord collectionOrdering]
- -[WFWorkflowCollectionRecord computedSyncHash]
- -[WFWorkflowCollectionRecord glyphCharacter]
- -[WFWorkflowCollectionRecord isDeleted]
- -[WFWorkflowCollectionRecord isFolder]
- -[WFWorkflowCollectionRecord lastRemoteCollectionOrderingSubset]
- -[WFWorkflowCollectionRecord lastRemoteCollectionOrdering]
- -[WFWorkflowCollectionRecord lastRemoteShortcutOrderingSubset]
- -[WFWorkflowCollectionRecord lastRemoteShortcutOrdering]
- -[WFWorkflowCollectionRecord lastSyncedEncryptedSchemaVersion]
- -[WFWorkflowCollectionRecord lastSyncedHash]
- -[WFWorkflowCollectionRecord name]
- -[WFWorkflowCollectionRecord saveChangesToStorage:error:]
- -[WFWorkflowCollectionRecord setCloudKitFolderRecordMetadata:]
- -[WFWorkflowCollectionRecord setCloudKitOrderingRecordMetadata:]
- -[WFWorkflowCollectionRecord setCollectionOrdering:]
- -[WFWorkflowCollectionRecord setGlyphCharacter:]
- -[WFWorkflowCollectionRecord setLastRemoteCollectionOrdering:]
- -[WFWorkflowCollectionRecord setLastRemoteCollectionOrderingSubset:]
- -[WFWorkflowCollectionRecord setLastRemoteShortcutOrdering:]
- -[WFWorkflowCollectionRecord setLastRemoteShortcutOrderingSubset:]
- -[WFWorkflowCollectionRecord setLastSyncedEncryptedSchemaVersion:]
- -[WFWorkflowCollectionRecord setLastSyncedHash:]
- -[WFWorkflowCollectionRecord setName:]
- -[WFWorkflowCollectionRecord setShortcutOrdering:]
- -[WFWorkflowCollectionRecord setWantedEncryptedSchemaVersion:]
- -[WFWorkflowCollectionRecord shortcutOrdering]
- -[WFWorkflowCollectionRecord wantedEncryptedSchemaVersion]
- -[WFWorkflowReference initWithIdentifier:name:color:glyphCharacter:associatedAppBundleIdentifier:subtitle:actionsDescription:actionCount:syncHash:isDeleted:hiddenFromLibraryAndSync:creationDate:modificationDate:lastRunDate:remoteQuarantineStatus:remoteQuarantineHash:receivesInputFromSearch:hasShortcutInputVariables:disabledOnLockScreen:source:runEventsCount:]
- GCC_except_table10000
- GCC_except_table10002
- GCC_except_table10004
- GCC_except_table10007
- GCC_except_table10010
- GCC_except_table10017
- GCC_except_table10183
- GCC_except_table10203
- GCC_except_table10206
- GCC_except_table10247
- GCC_except_table10415
- GCC_except_table10421
- GCC_except_table10440
- GCC_except_table10594
- GCC_except_table10628
- GCC_except_table10695
- GCC_except_table10702
- GCC_except_table10704
- GCC_except_table10706
- GCC_except_table10734
- GCC_except_table10739
- GCC_except_table10779
- GCC_except_table10782
- GCC_except_table10785
- GCC_except_table10788
- GCC_except_table10977
- GCC_except_table11071
- GCC_except_table11088
- GCC_except_table11110
- GCC_except_table11152
- GCC_except_table11510
- GCC_except_table11536
- GCC_except_table11555
- GCC_except_table11627
- GCC_except_table11902
- GCC_except_table11908
- GCC_except_table11911
- GCC_except_table11914
- GCC_except_table11917
- GCC_except_table11922
- GCC_except_table11929
- GCC_except_table11934
- GCC_except_table11937
- GCC_except_table11940
- GCC_except_table11943
- GCC_except_table11946
- GCC_except_table11949
- GCC_except_table11952
- GCC_except_table11955
- GCC_except_table11958
- GCC_except_table11961
- GCC_except_table11964
- GCC_except_table11967
- GCC_except_table11970
- GCC_except_table11993
- GCC_except_table11995
- GCC_except_table12000
- GCC_except_table12001
- GCC_except_table12006
- GCC_except_table12007
- GCC_except_table12008
- GCC_except_table12010
- GCC_except_table12108
- GCC_except_table1227
- GCC_except_table12320
- GCC_except_table12499
- GCC_except_table12514
- GCC_except_table12520
- GCC_except_table12522
- GCC_except_table12527
- GCC_except_table12621
- GCC_except_table12634
- GCC_except_table12642
- GCC_except_table12683
- GCC_except_table12720
- GCC_except_table12734
- GCC_except_table12736
- GCC_except_table12738
- GCC_except_table12820
- GCC_except_table12836
- GCC_except_table12942
- GCC_except_table12983
- GCC_except_table1300
- GCC_except_table13038
- GCC_except_table13067
- GCC_except_table13121
- GCC_except_table13132
- GCC_except_table13176
- GCC_except_table13178
- GCC_except_table13496
- GCC_except_table13529
- GCC_except_table13646
- GCC_except_table13675
- GCC_except_table13681
- GCC_except_table13728
- GCC_except_table13835
- GCC_except_table13838
- GCC_except_table13850
- GCC_except_table13857
- GCC_except_table13858
- GCC_except_table13859
- GCC_except_table13868
- GCC_except_table13879
- GCC_except_table14005
- GCC_except_table1405
- GCC_except_table14075
- GCC_except_table14080
- GCC_except_table14084
- GCC_except_table1410
- GCC_except_table14275
- GCC_except_table14343
- GCC_except_table14588
- GCC_except_table14618
- GCC_except_table14734
- GCC_except_table14905
- GCC_except_table14910
- GCC_except_table14919
- GCC_except_table14922
- GCC_except_table15039
- GCC_except_table15062
- GCC_except_table15073
- GCC_except_table15076
- GCC_except_table15431
- GCC_except_table15442
- GCC_except_table15456
- GCC_except_table15459
- GCC_except_table15653
- GCC_except_table15780
- GCC_except_table1735
- GCC_except_table1748
- GCC_except_table1753
- GCC_except_table1755
- GCC_except_table1757
- GCC_except_table1994
- GCC_except_table2070
- GCC_except_table2151
- GCC_except_table2161
- GCC_except_table2332
- GCC_except_table2340
- GCC_except_table2370
- GCC_except_table2523
- GCC_except_table2550
- GCC_except_table2618
- GCC_except_table2655
- GCC_except_table2771
- GCC_except_table2774
- GCC_except_table2788
- GCC_except_table2880
- GCC_except_table2933
- GCC_except_table2950
- GCC_except_table2956
- GCC_except_table3168
- GCC_except_table3190
- GCC_except_table3198
- GCC_except_table3225
- GCC_except_table3229
- GCC_except_table3253
- GCC_except_table3285
- GCC_except_table3301
- GCC_except_table3305
- GCC_except_table3364
- GCC_except_table3375
- GCC_except_table3380
- GCC_except_table349
- GCC_except_table352
- GCC_except_table3566
- GCC_except_table3570
- GCC_except_table3576
- GCC_except_table3577
- GCC_except_table3881
- GCC_except_table3885
- GCC_except_table4250
- GCC_except_table4251
- GCC_except_table4370
- GCC_except_table4472
- GCC_except_table4485
- GCC_except_table4504
- GCC_except_table4512
- GCC_except_table4687
- GCC_except_table4868
- GCC_except_table4970
- GCC_except_table4984
- GCC_except_table5102
- GCC_except_table5129
- GCC_except_table5133
- GCC_except_table5173
- GCC_except_table5231
- GCC_except_table5262
- GCC_except_table5302
- GCC_except_table535
- GCC_except_table5358
- GCC_except_table5363
- GCC_except_table5365
- GCC_except_table5491
- GCC_except_table5497
- GCC_except_table5513
- GCC_except_table5884
- GCC_except_table6028
- GCC_except_table6087
- GCC_except_table6194
- GCC_except_table626
- GCC_except_table6324
- GCC_except_table6325
- GCC_except_table6326
- GCC_except_table6427
- GCC_except_table6474
- GCC_except_table6492
- GCC_except_table6521
- GCC_except_table6846
- GCC_except_table6859
- GCC_except_table6922
- GCC_except_table6923
- GCC_except_table6928
- GCC_except_table6929
- GCC_except_table6932
- GCC_except_table6938
- GCC_except_table6943
- GCC_except_table6948
- GCC_except_table6949
- GCC_except_table6989
- GCC_except_table6994
- GCC_except_table7052
- GCC_except_table7063
- GCC_except_table7333
- GCC_except_table7343
- GCC_except_table7417
- GCC_except_table7495
- GCC_except_table7796
- GCC_except_table7839
- GCC_except_table7886
- GCC_except_table7887
- GCC_except_table7953
- GCC_except_table8083
- GCC_except_table8221
- GCC_except_table8226
- GCC_except_table8237
- GCC_except_table8417
- GCC_except_table8424
- GCC_except_table8435
- GCC_except_table845
- GCC_except_table9024
- GCC_except_table9093
- GCC_except_table9099
- GCC_except_table9102
- GCC_except_table9105
- GCC_except_table9109
- GCC_except_table9143
- GCC_except_table918
- GCC_except_table9197
- GCC_except_table927
- GCC_except_table9290
- GCC_except_table9339
- GCC_except_table9577
- GCC_except_table9583
- GCC_except_table9585
- GCC_except_table9589
- GCC_except_table9591
- GCC_except_table9593
- GCC_except_table9597
- GCC_except_table9599
- GCC_except_table9625
- GCC_except_table9646
- GCC_except_table9660
- GCC_except_table9669
- GCC_except_table9712
- GCC_except_table9718
- GCC_except_table9724
- GCC_except_table9994
- GCC_except_table9996
- GCC_except_table9997
- GCC_except_table9998
- _AssistantServicesLibraryCore.frameworkLibrary.54454
- _ContactsLibrary.53981
- _ContactsLibrary.67208
- _ContactsLibraryCore.frameworkLibrary.32208
- _ContactsLibraryCore.frameworkLibrary.47980
- _ContactsLibraryCore.frameworkLibrary.54031
- _ContactsLibraryCore.frameworkLibrary.61746
- _ContactsLibraryCore.frameworkLibrary.66106
- _ContactsLibraryCore.frameworkLibrary.67216
- _CoreLocationLibraryCore.frameworkLibrary.41580
- _CoreLocationLibraryCore.frameworkLibrary.48002
- _CoreLocationLibraryCore.frameworkLibrary.59274
- _CoreLocationLibraryCore.frameworkLibrary.59940
- _CoreLocationLibraryCore.frameworkLibrary.62105
- _CoreLocationLibraryCore.frameworkLibrary.63891
- _CoreLocationLibraryCore.frameworkLibrary.66067
- _HFTriggerActionSetsBuilderFunction.35670
- _HFTriggerActionSetsBuilderFunction.38917
- _HMCharacteristicMetadataFormatBoolFunction.2170
- _HMCharacteristicMetadataFormatBoolFunction.28270
- _HMCharacteristicMetadataFormatFloatFunction.2150
- _HMCharacteristicMetadataFormatIntFunction.2157
- _HMCharacteristicMetadataFormatIntFunction.28381
- _HMCharacteristicMetadataFormatStringFunction.2163
- _HMCharacteristicMetadataFormatUInt16Function.2138
- _HMCharacteristicMetadataFormatUInt32Function.2131
- _HMCharacteristicMetadataFormatUInt64Function.2123
- _HMCharacteristicMetadataFormatUInt8Function.2144
- _HMCharacteristicMetadataFormatUInt8Function.28388
- _HomeKitLibrary.sLib.1584
- _HomeKitLibrary.sLib.2118
- _HomeKitLibrary.sLib.28250
- _HomeKitLibrary.sLib.35697
- _HomeKitLibrary.sLib.36536
- _HomeKitLibrary.sLib.38928
- _HomeKitLibrary.sLib.56627
- _HomeKitLibrary.sOnce.1579
- _HomeKitLibrary.sOnce.2117
- _HomeKitLibrary.sOnce.28249
- _HomeKitLibrary.sOnce.35695
- _HomeKitLibrary.sOnce.36529
- _HomeKitLibrary.sOnce.38923
- _HomeKitLibrary.sOnce.56620
- _HomeLibrary.sLib.28395
- _HomeLibrary.sLib.35674
- _HomeLibrary.sLib.38921
- _HomeLibrary.sOnce.28391
- _HomeLibrary.sOnce.35666
- _HomeLibrary.sOnce.38913
- _MediaPlayerLibrary.37081
- _MediaPlayerLibrary.53758
- _MediaPlayerLibraryCore.frameworkLibrary.37091
- _MediaPlayerLibraryCore.frameworkLibrary.53765
- _OBJC_CLASS_$_WFCoreDataCollectionModel
- _OBJC_CLASS_$_WFWorkflowCollectionRecord
- _OBJC_IVAR_$_WFCoreDataCollectionModel._coreDataCollection
- _OBJC_IVAR_$_WFCoreDataCollectionModel._database
- _OBJC_IVAR_$_WFCoreDataCollectionModel._isRootCollection
- _OBJC_IVAR_$_WFCoreDataCollectionModel._workflowType
- _OBJC_IVAR_$_WFDatabase._destroysOnDeallocation
- _OBJC_IVAR_$_WFWorkflowCollectionRecord._cloudKitFolderRecordMetadata
- _OBJC_IVAR_$_WFWorkflowCollectionRecord._cloudKitOrderingRecordMetadata
- _OBJC_IVAR_$_WFWorkflowCollectionRecord._collectionOrdering
- _OBJC_IVAR_$_WFWorkflowCollectionRecord._deleted
- _OBJC_IVAR_$_WFWorkflowCollectionRecord._folder
- _OBJC_IVAR_$_WFWorkflowCollectionRecord._glyphCharacter
- _OBJC_IVAR_$_WFWorkflowCollectionRecord._lastRemoteCollectionOrdering
- _OBJC_IVAR_$_WFWorkflowCollectionRecord._lastRemoteCollectionOrderingSubset
- _OBJC_IVAR_$_WFWorkflowCollectionRecord._lastRemoteShortcutOrdering
- _OBJC_IVAR_$_WFWorkflowCollectionRecord._lastRemoteShortcutOrderingSubset
- _OBJC_IVAR_$_WFWorkflowCollectionRecord._lastSyncedEncryptedSchemaVersion
- _OBJC_IVAR_$_WFWorkflowCollectionRecord._lastSyncedHash
- _OBJC_IVAR_$_WFWorkflowCollectionRecord._name
- _OBJC_IVAR_$_WFWorkflowCollectionRecord._shortcutOrdering
- _OBJC_IVAR_$_WFWorkflowCollectionRecord._wantedEncryptedSchemaVersion
- _OBJC_METACLASS_$_WFCoreDataCollectionModel
- _OBJC_METACLASS_$_WFWorkflowCollectionRecord
- _PhotosLibraryCore.frameworkLibrary.1494
- _ReminderKitLibraryCore.frameworkLibrary.25664
- _RunningBoardServicesLibrary.27455
- _RunningBoardServicesLibraryCore.frameworkLibrary.27460
- _SAObjectsLibrary.sLib.70721
- _SAObjectsLibrary.sOnce.70719
- _UIKitLibrary.sLib.16271
- _UIKitLibrary.sLib.22973
- _UIKitLibrary.sLib.28662
- _UIKitLibrary.sLib.29259
- _UIKitLibrary.sLib.42533
- _UIKitLibrary.sLib.49485
- _UIKitLibrary.sLib.58987
- _UIKitLibrary.sLib.61460
- _UIKitLibrary.sLib.64558
- _UIKitLibrary.sOnce.16269
- _UIKitLibrary.sOnce.22966
- _UIKitLibrary.sOnce.28655
- _UIKitLibrary.sOnce.29256
- _UIKitLibrary.sOnce.42531
- _UIKitLibrary.sOnce.49475
- _UIKitLibrary.sOnce.58982
- _UIKitLibrary.sOnce.61450
- _UIKitLibrary.sOnce.64548
- _UIKitLibraryCore.frameworkLibrary.41837
- _UIPasteboardFunction.42546
- _UIPasteboardFunction.49480
- _UIPasteboardFunction.61455
- _UIPasteboardFunction.64553
- _VCBundleIdentifierDataActions
- _WFDyldBulkImageLoadCallback.25088
- _WFEnforceClass.10314
- _WFEnforceClass.1039
- _WFEnforceClass.13281
- _WFEnforceClass.13489
- _WFEnforceClass.1477
- _WFEnforceClass.15630
- _WFEnforceClass.16684
- _WFEnforceClass.16805
- _WFEnforceClass.17228
- _WFEnforceClass.17864
- _WFEnforceClass.1926
- _WFEnforceClass.2095
- _WFEnforceClass.21346
- _WFEnforceClass.21588
- _WFEnforceClass.22495
- _WFEnforceClass.23384
- _WFEnforceClass.23450
- _WFEnforceClass.25059
- _WFEnforceClass.25172
- _WFEnforceClass.29086
- _WFEnforceClass.29370
- _WFEnforceClass.29456
- _WFEnforceClass.29616
- _WFEnforceClass.29805
- _WFEnforceClass.30053
- _WFEnforceClass.30799
- _WFEnforceClass.31810
- _WFEnforceClass.32356
- _WFEnforceClass.3417
- _WFEnforceClass.35845
- _WFEnforceClass.36871
- _WFEnforceClass.37354
- _WFEnforceClass.3980
- _WFEnforceClass.40806
- _WFEnforceClass.42374
- _WFEnforceClass.43859
- _WFEnforceClass.46712
- _WFEnforceClass.47137
- _WFEnforceClass.47281
- _WFEnforceClass.49377
- _WFEnforceClass.50825
- _WFEnforceClass.51311
- _WFEnforceClass.57983
- _WFEnforceClass.58883
- _WFEnforceClass.59149
- _WFEnforceClass.61258
- _WFEnforceClass.6175
- _WFEnforceClass.61969
- _WFEnforceClass.63664
- _WFEnforceClass.64156
- _WFEnforceClass.64518
- _WFEnforceClass.65167
- _WFEnforceClass.65752
- _WFEnforceClass.67572
- _WFEnforceClass.71973
- _WFEnforceClass.72269
- _WFEnforceClass.72791
- _WFEnforceClass.74192
- _WFEnforceClass.75148
- _WFEnforceClass.76090
- _WFEnforceClass.7769
- _WFEnforceClass.8252
- _WFEnforceClass.8644
- _WFEnforceClass.8980
- _WFEnforceClass.9243
- _WFEnforceClass.9587
- _WFGroupingPropertyForMediaType.53752
- __OBJC_$_CLASS_METHODS_WFDatabase(ShortcutSync|Library|AccessResources|WFDatabaseProvider|TipKit|TrackedFilesystemNode|ShortcutSuggestions|Sync|AutoShortcutsPreferences|SmartPrompts|Conflicts|Bookmarks|Shortcuts|Triggers|Collections|RunEvents|PersistedSerializedParameters)
- __OBJC_$_INSTANCE_METHODS_WFCoreDataCollectionModel
- __OBJC_$_INSTANCE_METHODS_WFDatabase(ShortcutSync|Library|AccessResources|WFDatabaseProvider|TipKit|TrackedFilesystemNode|ShortcutSuggestions|Sync|AutoShortcutsPreferences|SmartPrompts|Conflicts|Bookmarks|Shortcuts|Triggers|Collections|RunEvents|PersistedSerializedParameters)
- __OBJC_$_INSTANCE_METHODS_WFWorkflowCollectionRecord
- __OBJC_$_INSTANCE_VARIABLES_WFCoreDataCollectionModel
- __OBJC_$_INSTANCE_VARIABLES_WFWorkflowCollectionRecord
- __OBJC_$_PROP_LIST_WFCoreDataCollectionModel
- __OBJC_$_PROP_LIST_WFDatabaseRecordStorage
- __OBJC_$_PROP_LIST_WFWorkflowCollectionRecord
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_WFDatabaseRecordStorage
- __OBJC_$_PROTOCOL_METHOD_TYPES_WFDatabaseRecordStorage
- __OBJC_CLASS_PROTOCOLS_$_WFCoreDataCollectionModel
- __OBJC_CLASS_PROTOCOLS_$_WFDatabase(ShortcutSync|Library|AccessResources|WFDatabaseProvider|TipKit|TrackedFilesystemNode|ShortcutSuggestions|Sync|AutoShortcutsPreferences|SmartPrompts|Conflicts|Bookmarks|Shortcuts|Triggers|Collections|RunEvents|PersistedSerializedParameters)
- __OBJC_CLASS_RO_$_WFCoreDataCollectionModel
- __OBJC_CLASS_RO_$_WFWorkflowCollectionRecord
- __OBJC_LABEL_PROTOCOL_$_WFDatabaseRecordStorage
- __OBJC_METACLASS_RO_$_WFCoreDataCollectionModel
- __OBJC_METACLASS_RO_$_WFWorkflowCollectionRecord
- __OBJC_PROTOCOL_$_WFDatabaseRecordStorage
- __PROTOCOLS__TtCE11WorkflowKitCSo20WFWorkflowActionTree14ActionObserver.5
- ___223-[WFDatabase(Shortcuts) visibleReferencesForWorkflowIDs:sortByKeys:nameContaining:nameEqualing:hasAssociatedAppBundleIdentifier:associatedAppBundleIdentifier:hasTombstonedConflicts:isRecentlyModified:isRecentlyRun:limitTo:]_block_invoke
- ___38-[WFDatabase(Sync) updateWalrusStatus]_block_invoke.289
- ___38-[WFDatabase(Sync) updateWalrusStatus]_block_invoke_2.290
- ___38-[WFWorkflow saveWithCompletionBlock:]_block_invoke.398
- ___39-[WFDatabase notifyResultsAboutChange:]_block_invoke.298
- ___39-[WFDatabase notifyResultsAboutChange:]_block_invoke.304
- ___39-[WFDatabase notifyResultsAboutChange:]_block_invoke_2.302
- ___39-[WFDatabase notifyResultsAboutChange:]_block_invoke_2.305
- ___43-[WFDatabase(Shortcuts) hasWorkflowWithID:]_block_invoke
- ___44-[WFBackgroundShortcutRunner unaliveProcess]_block_invoke.345
- ___44-[WFBackgroundShortcutRunner unaliveProcess]_block_invoke.349
- ___49-[WFDatabase(Shortcuts) applyConflictResolution:]_block_invoke.304
- ___51-[WFCoreDataCollectionModel setCollectionOrdering:]_block_invoke
- ___51-[WFCoreDataCollectionModel setCollectionOrdering:]_block_invoke_2
- ___55-[WFWorkflow configureAsSingleStepShortcutIfNecessary:]_block_invoke.434
- ___74-[WFDatabase(Collections) _moveReferences:toIndexes:ofCollectionID:error:]_block_invoke.217
- ___78-[WFBackgroundShortcutRunner resumeRunningFromContext:withRequest:completion:]_block_invoke.331
- ___81-[WFDatabase(Shortcuts) deleteReference:tombstone:deleteConflictIfPresent:error:]_block_invoke.278
- ___82-[WFDatabase initWithStoreDescription:runMigrationsIfNecessary:useLockFile:error:]_block_invoke.244
- ___84-[WFBackgroundShortcutRunner runActionFromRunRequestData:runningContext:completion:]_block_invoke.294
- ___84-[WFBackgroundShortcutRunner runActionFromRunRequestData:runningContext:completion:]_block_invoke.296
- ___84-[WFBackgroundShortcutRunner runActionFromRunRequestData:runningContext:completion:]_block_invoke.301
- ___84-[WFBackgroundShortcutRunner runActionFromRunRequestData:runningContext:completion:]_block_invoke_2.295
- ___85-[WFBackgroundShortcutRunner workflowController:didFinishRunningWithError:cancelled:]_block_invoke.407
- ___85-[WFBackgroundShortcutRunner workflowController:didFinishRunningWithError:cancelled:]_block_invoke_2.408
- ___85-[WFDatabase(Collections) collectionRecordForCollectionIdentifier:createIfNecessary:]_block_invoke
- ___94-[WFLinkActionProvider createActionsForRequests:allowsActionInDenyList:forceLocalActionsOnly:]_block_invoke_2
- ___AssistantServicesLibraryCore_block_invoke.54455
- ___Block_byref_object_copy_.10388
- ___Block_byref_object_copy_.10674
- ___Block_byref_object_copy_.11709
- ___Block_byref_object_copy_.12234
- ___Block_byref_object_copy_.12579
- ___Block_byref_object_copy_.13500
- ___Block_byref_object_copy_.15203
- ___Block_byref_object_copy_.16265
- ___Block_byref_object_copy_.18004
- ___Block_byref_object_copy_.18106
- ___Block_byref_object_copy_.19352
- ___Block_byref_object_copy_.20273
- ___Block_byref_object_copy_.20678
- ___Block_byref_object_copy_.20758
- ___Block_byref_object_copy_.22263
- ___Block_byref_object_copy_.24769
- ___Block_byref_object_copy_.25336
- ___Block_byref_object_copy_.26451
- ___Block_byref_object_copy_.27480
- ___Block_byref_object_copy_.29245
- ___Block_byref_object_copy_.2976
- ___Block_byref_object_copy_.30131
- ___Block_byref_object_copy_.31779
- ___Block_byref_object_copy_.35404
- ___Block_byref_object_copy_.35678
- ___Block_byref_object_copy_.37103
- ___Block_byref_object_copy_.37976
- ___Block_byref_object_copy_.41382
- ___Block_byref_object_copy_.42215
- ___Block_byref_object_copy_.42525
- ___Block_byref_object_copy_.43729
- ___Block_byref_object_copy_.46733
- ___Block_byref_object_copy_.46927
- ___Block_byref_object_copy_.48077
- ___Block_byref_object_copy_.49359
- ___Block_byref_object_copy_.49816
- ___Block_byref_object_copy_.5185
- ___Block_byref_object_copy_.54447
- ___Block_byref_object_copy_.56147
- ___Block_byref_object_copy_.57046
- ___Block_byref_object_copy_.57384
- ___Block_byref_object_copy_.58224
- ___Block_byref_object_copy_.59322
- ___Block_byref_object_copy_.59843
- ___Block_byref_object_copy_.60962
- ___Block_byref_object_copy_.61606
- ___Block_byref_object_copy_.62101
- ___Block_byref_object_copy_.6287
- ___Block_byref_object_copy_.64261
- ___Block_byref_object_copy_.64861
- ___Block_byref_object_copy_.65146
- ___Block_byref_object_copy_.66206
- ___Block_byref_object_copy_.68418
- ___Block_byref_object_copy_.70405
- ___Block_byref_object_copy_.71302
- ___Block_byref_object_copy_.72369
- ___Block_byref_object_copy_.73176
- ___Block_byref_object_copy_.7384
- ___Block_byref_object_copy_.74834
- ___Block_byref_object_copy_.8531
- ___Block_byref_object_copy_.9717
- ___Block_byref_object_copy_.9762
- ___Block_byref_object_dispose_.10389
- ___Block_byref_object_dispose_.10675
- ___Block_byref_object_dispose_.11710
- ___Block_byref_object_dispose_.12235
- ___Block_byref_object_dispose_.12580
- ___Block_byref_object_dispose_.13501
- ___Block_byref_object_dispose_.15204
- ___Block_byref_object_dispose_.16266
- ___Block_byref_object_dispose_.18005
- ___Block_byref_object_dispose_.18107
- ___Block_byref_object_dispose_.19353
- ___Block_byref_object_dispose_.20274
- ___Block_byref_object_dispose_.20679
- ___Block_byref_object_dispose_.20759
- ___Block_byref_object_dispose_.22264
- ___Block_byref_object_dispose_.24770
- ___Block_byref_object_dispose_.25337
- ___Block_byref_object_dispose_.26452
- ___Block_byref_object_dispose_.27481
- ___Block_byref_object_dispose_.29246
- ___Block_byref_object_dispose_.2977
- ___Block_byref_object_dispose_.30132
- ___Block_byref_object_dispose_.31780
- ___Block_byref_object_dispose_.35405
- ___Block_byref_object_dispose_.35679
- ___Block_byref_object_dispose_.37104
- ___Block_byref_object_dispose_.37977
- ___Block_byref_object_dispose_.41383
- ___Block_byref_object_dispose_.42216
- ___Block_byref_object_dispose_.42526
- ___Block_byref_object_dispose_.43730
- ___Block_byref_object_dispose_.46734
- ___Block_byref_object_dispose_.46928
- ___Block_byref_object_dispose_.48078
- ___Block_byref_object_dispose_.49360
- ___Block_byref_object_dispose_.49817
- ___Block_byref_object_dispose_.5186
- ___Block_byref_object_dispose_.54448
- ___Block_byref_object_dispose_.56148
- ___Block_byref_object_dispose_.57047
- ___Block_byref_object_dispose_.57385
- ___Block_byref_object_dispose_.58225
- ___Block_byref_object_dispose_.59323
- ___Block_byref_object_dispose_.59844
- ___Block_byref_object_dispose_.60963
- ___Block_byref_object_dispose_.61607
- ___Block_byref_object_dispose_.62102
- ___Block_byref_object_dispose_.6288
- ___Block_byref_object_dispose_.64262
- ___Block_byref_object_dispose_.64862
- ___Block_byref_object_dispose_.65147
- ___Block_byref_object_dispose_.66207
- ___Block_byref_object_dispose_.68419
- ___Block_byref_object_dispose_.70406
- ___Block_byref_object_dispose_.71303
- ___Block_byref_object_dispose_.72370
- ___Block_byref_object_dispose_.73177
- ___Block_byref_object_dispose_.7385
- ___Block_byref_object_dispose_.74835
- ___Block_byref_object_dispose_.8532
- ___Block_byref_object_dispose_.9718
- ___Block_byref_object_dispose_.9763
- ___ContactsLibraryCore_block_invoke.32209
- ___ContactsLibraryCore_block_invoke.47981
- ___ContactsLibraryCore_block_invoke.54032
- ___ContactsLibraryCore_block_invoke.61747
- ___ContactsLibraryCore_block_invoke.66107
- ___ContactsLibraryCore_block_invoke.67217
- ___CoreLocationLibraryCore_block_invoke.41581
- ___CoreLocationLibraryCore_block_invoke.48003
- ___CoreLocationLibraryCore_block_invoke.59275
- ___CoreLocationLibraryCore_block_invoke.59941
- ___CoreLocationLibraryCore_block_invoke.62106
- ___CoreLocationLibraryCore_block_invoke.63892
- ___CoreLocationLibraryCore_block_invoke.66068
- ___HomeKitLibrary_block_invoke.1582
- ___HomeKitLibrary_block_invoke.2125
- ___HomeKitLibrary_block_invoke.28255
- ___HomeKitLibrary_block_invoke.35703
- ___HomeKitLibrary_block_invoke.36534
- ___HomeKitLibrary_block_invoke.38926
- ___HomeKitLibrary_block_invoke.56625
- ___HomeLibrary_block_invoke.28393
- ___HomeLibrary_block_invoke.35672
- ___HomeLibrary_block_invoke.38919
- ___MediaPlayerLibraryCore_block_invoke.37092
- ___MediaPlayerLibraryCore_block_invoke.53766
- ___PhotosLibraryCore_block_invoke.1495
- ___ReminderKitLibraryCore_block_invoke.25665
- ___RunningBoardServicesLibraryCore_block_invoke.27461
- ___SAObjectsLibrary_block_invoke.70725
- ___UIKitLibraryCore_block_invoke.41838
- ___UIKitLibrary_block_invoke.16276
- ___UIKitLibrary_block_invoke.22971
- ___UIKitLibrary_block_invoke.28660
- ___UIKitLibrary_block_invoke.29258
- ___UIKitLibrary_block_invoke.42539
- ___UIKitLibrary_block_invoke.49483
- ___UIKitLibrary_block_invoke.58985
- ___UIKitLibrary_block_invoke.61458
- ___UIKitLibrary_block_invoke.64556
- ___WFUpdateSmartPromptChangesToShortcutChanges_block_invoke.606
- ___block_descriptor_49_e8_32s40s_e37_"WFWorkflowCollectionRecord"16?0^8ls32l8s40l8
- ___block_descriptor_72_e8_32s40s48s56s64s_e9_v16?0^8ls32l8s40l8s48l8s56l8s64l8
- ___block_descriptor_92_e8_32s40s48s56s64s72s_e27_"WFDatabaseResult"16?0^8ls32l8s40l8s48l8s56l8s64l8s72l8
- ___block_literal_global.10305
- ___block_literal_global.1091
- ___block_literal_global.10980
- ___block_literal_global.11239
- ___block_literal_global.11319
- ___block_literal_global.12241
- ___block_literal_global.1257
- ___block_literal_global.12598
- ___block_literal_global.1274
- ___block_literal_global.13237
- ___block_literal_global.13290
- ___block_literal_global.13493
- ___block_literal_global.13723
- ___block_literal_global.1377
- ___block_literal_global.13848
- ___block_literal_global.14402
- ___block_literal_global.14485
- ___block_literal_global.14709
- ___block_literal_global.15660
- ___block_literal_global.15861
- ___block_literal_global.1621
- ___block_literal_global.16270
- ___block_literal_global.1713
- ___block_literal_global.172.22600
- ___block_literal_global.176.45836
- ___block_literal_global.178.29619
- ___block_literal_global.178.39830
- ___block_literal_global.178.69665
- ___block_literal_global.178.74851
- ___block_literal_global.179.26497
- ___block_literal_global.180.36445
- ___block_literal_global.18152
- ___block_literal_global.183.72380
- ___block_literal_global.183.74878
- ___block_literal_global.186.52437
- ___block_literal_global.186.72384
- ___block_literal_global.186.74879
- ___block_literal_global.18848
- ___block_literal_global.189.45863
- ___block_literal_global.189.60415
- ___block_literal_global.189.60764
- ___block_literal_global.189.75143
- ___block_literal_global.18949
- ___block_literal_global.191.60765
- ___block_literal_global.191.72388
- ___block_literal_global.192.6278
- ___block_literal_global.19260
- ___block_literal_global.193.25344
- ___block_literal_global.193.29138
- ___block_literal_global.193.45866
- ___block_literal_global.193.66937
- ___block_literal_global.194.72371
- ___block_literal_global.19580
- ___block_literal_global.19695
- ___block_literal_global.199.18132
- ___block_literal_global.199.45112
- ___block_literal_global.199.57190
- ___block_literal_global.202.18129
- ___block_literal_global.202.21134
- ___block_literal_global.202.56972
- ___block_literal_global.203.46201
- ___block_literal_global.205.25320
- ___block_literal_global.206.60408
- ___block_literal_global.20653
- ___block_literal_global.208.49381
- ___block_literal_global.2102
- ___block_literal_global.21158
- ___block_literal_global.213.53735
- ___block_literal_global.219.68868
- ___block_literal_global.22064
- ___block_literal_global.22485
- ___block_literal_global.225.26794
- ___block_literal_global.225.60392
- ___block_literal_global.2255
- ___block_literal_global.22671
- ___block_literal_global.227.74825
- ___block_literal_global.22769
- ___block_literal_global.22967
- ___block_literal_global.230.41433
- ___block_literal_global.23030
- ___block_literal_global.232.43335
- ___block_literal_global.232.69344
- ___block_literal_global.23259
- ___block_literal_global.23442
- ___block_literal_global.239.74792
- ___block_literal_global.23968
- ___block_literal_global.245
- ___block_literal_global.247.37171
- ___block_literal_global.247.69340
- ___block_literal_global.24786
- ___block_literal_global.25079
- ___block_literal_global.251.55404
- ___block_literal_global.251.68442
- ___block_literal_global.25175
- ___block_literal_global.25302
- ___block_literal_global.25614
- ___block_literal_global.26177
- ___block_literal_global.26474
- ___block_literal_global.265
- ___block_literal_global.2666
- ___block_literal_global.26784
- ___block_literal_global.27018
- ___block_literal_global.27536
- ___block_literal_global.277.41364
- ___block_literal_global.277.47038
- ___block_literal_global.2819
- ___block_literal_global.282
- ___block_literal_global.28244
- ___block_literal_global.283.11322
- ___block_literal_global.28656
- ___block_literal_global.2885
- ___block_literal_global.29149
- ___block_literal_global.29248
- ___block_literal_global.29371
- ___block_literal_global.294.7867
- ___block_literal_global.2958
- ___block_literal_global.29625
- ___block_literal_global.29784
- ___block_literal_global.299.76755
- ___block_literal_global.30115
- ___block_literal_global.305.58989
- ___block_literal_global.306.14710
- ___block_literal_global.311.59076
- ___block_literal_global.31645
- ___block_literal_global.33697
- ___block_literal_global.34408
- ___block_literal_global.347.39573
- ___block_literal_global.348.41495
- ___block_literal_global.35442
- ___block_literal_global.35696
- ___block_literal_global.357.41524
- ___block_literal_global.3581
- ___block_literal_global.35994
- ___block_literal_global.363
- ___block_literal_global.36441
- ___block_literal_global.36530
- ___block_literal_global.37009
- ___block_literal_global.37169
- ___block_literal_global.37373
- ___block_literal_global.375
- ___block_literal_global.37983
- ___block_literal_global.38900
- ___block_literal_global.390
- ___block_literal_global.39460
- ___block_literal_global.395.60242
- ___block_literal_global.397
- ___block_literal_global.397.39546
- ___block_literal_global.39829
- ___block_literal_global.3984
- ___block_literal_global.40651
- ___block_literal_global.41114
- ___block_literal_global.41432
- ___block_literal_global.41616
- ___block_literal_global.420
- ___block_literal_global.422
- ___block_literal_global.42250
- ___block_literal_global.42375
- ___block_literal_global.42532
- ___block_literal_global.42739
- ___block_literal_global.43363
- ___block_literal_global.43967
- ___block_literal_global.44071
- ___block_literal_global.44398
- ___block_literal_global.44476
- ___block_literal_global.45115
- ___block_literal_global.454.33633
- ___block_literal_global.454.7393
- ___block_literal_global.45587
- ___block_literal_global.458
- ___block_literal_global.45845
- ___block_literal_global.46195
- ___block_literal_global.46305
- ___block_literal_global.469.67781
- ___block_literal_global.47028
- ___block_literal_global.47082
- ___block_literal_global.47339
- ___block_literal_global.475
- ___block_literal_global.477.67782
- ___block_literal_global.479
- ___block_literal_global.48097
- ___block_literal_global.49138
- ___block_literal_global.49349
- ___block_literal_global.49476
- ___block_literal_global.49666
- ___block_literal_global.49761
- ___block_literal_global.50027
- ___block_literal_global.50937
- ___block_literal_global.50962
- ___block_literal_global.51601
- ___block_literal_global.51611
- ___block_literal_global.52242
- ___block_literal_global.52436
- ___block_literal_global.52772
- ___block_literal_global.52833
- ___block_literal_global.53734
- ___block_literal_global.5392
- ___block_literal_global.54037
- ___block_literal_global.54443
- ___block_literal_global.54730
- ___block_literal_global.54786
- ___block_literal_global.55402
- ___block_literal_global.55592
- ___block_literal_global.56068
- ___block_literal_global.5612
- ___block_literal_global.56254
- ___block_literal_global.56621
- ___block_literal_global.57053
- ___block_literal_global.57189
- ___block_literal_global.57675
- ___block_literal_global.57880
- ___block_literal_global.59129
- ___block_literal_global.59264
- ___block_literal_global.60426
- ___block_literal_global.60763
- ___block_literal_global.61068
- ___block_literal_global.61321
- ___block_literal_global.61451
- ___block_literal_global.61645
- ___block_literal_global.61709
- ___block_literal_global.618
- ___block_literal_global.6275
- ___block_literal_global.6341
- ___block_literal_global.63764
- ___block_literal_global.63842
- ___block_literal_global.64153
- ___block_literal_global.64510
- ___block_literal_global.64549
- ___block_literal_global.65469
- ___block_literal_global.66085
- ___block_literal_global.66946
- ___block_literal_global.6696
- ___block_literal_global.67204
- ___block_literal_global.67242
- ___block_literal_global.67616
- ___block_literal_global.67940
- ___block_literal_global.68186
- ___block_literal_global.68501
- ___block_literal_global.68867
- ___block_literal_global.69357
- ___block_literal_global.69434
- ___block_literal_global.695
- ___block_literal_global.69507
- ___block_literal_global.69670
- ___block_literal_global.70017
- ___block_literal_global.703.43072
- ___block_literal_global.704
- ___block_literal_global.70402
- ___block_literal_global.70720
- ___block_literal_global.70887
- ___block_literal_global.71236
- ___block_literal_global.71641
- ___block_literal_global.72147
- ___block_literal_global.72400
- ___block_literal_global.73195
- ___block_literal_global.74622
- ___block_literal_global.74849
- ___block_literal_global.75164
- ___block_literal_global.7576
- ___block_literal_global.75865
- ___block_literal_global.76767
- ___block_literal_global.787
- ___block_literal_global.7895
- ___block_literal_global.8245
- ___block_literal_global.8763
- ___block_literal_global.8995
- ___block_literal_global.914
- ___block_literal_global.9411
- ___block_literal_global.9675
- ___getCLPlacemarkClass_block_invoke.59939
- ___getCLPlacemarkClass_block_invoke.62104
- ___getCLPlacemarkClass_block_invoke.66066
- ___getCNContactStoreClass_block_invoke.67206
- ___getMPMediaItemClass_block_invoke.53751
- ___getMPMediaPropertyPredicateClass_block_invoke.37061
- ___getMPMediaPropertyPredicateClass_block_invoke.53749
- ___getMPMediaQueryClass_block_invoke.37064
- ___getMPMediaQueryClass_block_invoke.53754
- __mutableRegisteredDefinitions.69442
- _audit_stringAssistantServices.54470
- _audit_stringContacts.32223
- _audit_stringContacts.47995
- _audit_stringContacts.54035
- _audit_stringContacts.61751
- _audit_stringContacts.66110
- _audit_stringContacts.67223
- _audit_stringCoreLocation.41596
- _audit_stringCoreLocation.48007
- _audit_stringCoreLocation.59278
- _audit_stringCoreLocation.59955
- _audit_stringCoreLocation.62120
- _audit_stringCoreLocation.63905
- _audit_stringCoreLocation.66082
- _audit_stringMediaPlayer.37098
- _audit_stringMediaPlayer.53772
- _audit_stringPhotos.1501
- _audit_stringReminderKit.25671
- _audit_stringRunningBoardServices.27467
- _audit_stringUIKit.41852
- _block_copy_helper.116
- _block_copy_helper.94
- _block_descriptor.118
- _block_descriptor.96
- _block_destroy_helper.117
- _block_destroy_helper.95
- _classHFTriggerActionSetsBuilder.35668
- _classHFTriggerActionSetsBuilder.38915
- _classRegistrationLock.52149
- _classRegistrationLock.72762
- _classRegistrationLock.9193
- _classUIPasteboard.42544
- _classUIPasteboard.49478
- _classUIPasteboard.61453
- _classUIPasteboard.64551
- _constantHMCharacteristicMetadataFormatBool.2168
- _constantHMCharacteristicMetadataFormatBool.28268
- _constantHMCharacteristicMetadataFormatFloat.2148
- _constantHMCharacteristicMetadataFormatInt.2155
- _constantHMCharacteristicMetadataFormatInt.28379
- _constantHMCharacteristicMetadataFormatString.2161
- _constantHMCharacteristicMetadataFormatUInt16.2136
- _constantHMCharacteristicMetadataFormatUInt32.2129
- _constantHMCharacteristicMetadataFormatUInt64.2121
- _constantHMCharacteristicMetadataFormatUInt8.2142
- _constantHMCharacteristicMetadataFormatUInt8.28386
- _getCLPlacemarkClass.66001
- _getCLPlacemarkClass.softClass.59938
- _getCLPlacemarkClass.softClass.62103
- _getCLPlacemarkClass.softClass.66065
- _getCNContactStoreClass.softClass.67205
- _getHFTriggerActionSetsBuilderClass.35656
- _getHFTriggerActionSetsBuilderClass.38910
- _getHMCharacteristicMetadataFormatBool.2107
- _getHMCharacteristicMetadataFormatBool.28263
- _getHMCharacteristicMetadataFormatFloat.2110
- _getHMCharacteristicMetadataFormatInt.2109
- _getHMCharacteristicMetadataFormatInt.28374
- _getHMCharacteristicMetadataFormatString.2108
- _getHMCharacteristicMetadataFormatUInt16.2112
- _getHMCharacteristicMetadataFormatUInt32.2113
- _getHMCharacteristicMetadataFormatUInt64.2114
- _getHMCharacteristicMetadataFormatUInt8.2111
- _getHMCharacteristicMetadataFormatUInt8.28373
- _getMPMediaItemClass.softClass.53750
- _getMPMediaPropertyPredicateClass.softClass.37060
- _getMPMediaPropertyPredicateClass.softClass.53748
- _getMPMediaQueryClass.softClass.37063
- _getMPMediaQueryClass.softClass.53753
- _getUIPasteboardClass.42529
- _getUIPasteboardClass.49472
- _getUIPasteboardClass.61444
- _getUIPasteboardClass.64544
- _initHFTriggerActionSetsBuilder.35665
- _initHFTriggerActionSetsBuilder.38912
- _initHMCharacteristicMetadataFormatBool.2165
- _initHMCharacteristicMetadataFormatBool.28265
- _initHMCharacteristicMetadataFormatFloat.2146
- _initHMCharacteristicMetadataFormatInt.2152
- _initHMCharacteristicMetadataFormatInt.28376
- _initHMCharacteristicMetadataFormatString.2159
- _initHMCharacteristicMetadataFormatUInt16.2133
- _initHMCharacteristicMetadataFormatUInt32.2127
- _initHMCharacteristicMetadataFormatUInt64.2116
- _initHMCharacteristicMetadataFormatUInt8.2140
- _initHMCharacteristicMetadataFormatUInt8.28383
- _initUIPasteboard.42542
- _initUIPasteboard.49474
- _initUIPasteboard.61449
- _initUIPasteboard.64547
- _objc_msgSend$cloudKitFolderRecordMetadata
- _objc_msgSend$cloudKitOrderingRecordMetadata
- _objc_msgSend$collectionOrdering
- _objc_msgSend$coreDataCollection
- _objc_msgSend$createTemporaryFileWithFilename:
- _objc_msgSend$deserializedLastRemoteCollectionOrdering
- _objc_msgSend$deserializedLastRemoteCollectionOrderingSubset
- _objc_msgSend$deserializedLastRemoteShortcutOrdering
- _objc_msgSend$deserializedLastRemoteShortcutOrderingSubset
- _objc_msgSend$destroysOnDeallocation
- _objc_msgSend$initWithActions:
- _objc_msgSend$initWithIdentifier:name:color:glyphCharacter:associatedAppBundleIdentifier:subtitle:actionsDescription:actionCount:syncHash:isDeleted:hiddenFromLibraryAndSync:creationDate:modificationDate:lastRunDate:remoteQuarantineStatus:remoteQuarantineHash:receivesInputFromSearch:hasShortcutInputVariables:disabledOnLockScreen:source:runEventsCount:
- _objc_msgSend$insertFolderWithName:icon:identifier:insertAt:error:
- _objc_msgSend$isRootCollection
- _objc_msgSend$lastRemoteShortcutOrderingSubsetData
- _objc_msgSend$setActionTree:
- _objc_msgSend$setCloudKitFolderRecordMetadata:
- _objc_msgSend$setCloudKitOrderingRecordMetadata:
- _objc_msgSend$setDeserializedLastRemoteCollectionOrdering:
- _objc_msgSend$setDeserializedLastRemoteCollectionOrderingSubset:
- _objc_msgSend$setDeserializedLastRemoteShortcutOrdering:
- _objc_msgSend$setDeserializedLastRemoteShortcutOrderingSubset:
- _objc_msgSend$setDestroysOnDeallocation:
- _objc_msgSend$setLastRemoteShortcutOrderingSubsetData:
- _objc_msgSend$setPossibleStates:
- _objc_msgSend$setPossibleStatesCollection:
- _objc_msgSend$setShortcutOrdering:forCollectionIdentifier:error:
- _objc_msgSend$setTemporarySyncFolderIcon:
- _objc_msgSend$setTemporarySyncFolderName:
- _objc_msgSend$shortcutIdentifiersWithQuery:error:
- _objc_msgSend$shortcutOrdering
- _objc_msgSend$shouldPromptForCurrentContentItemCount:previousCount:
- _objc_msgSend$sortedGroupings
- _objc_msgSend$sortedWorkflowsWithQuery:hasTombstonedConflicts:
- _objc_msgSend$temporarySyncFolderIcon
- _objc_msgSend$temporarySyncFolderName
- _objc_msgSend$visibleReferencesForWorkflowIDs:sortByKeys:nameContaining:nameEqualing:hasAssociatedAppBundleIdentifier:associatedAppBundleIdentifier:hasTombstonedConflicts:isRecentlyModified:isRecentlyRun:limitTo:
- _objc_msgSend$workflowType
- _objectdestroy.120Tm
- _objectdestroy.49Tm
- _objectdestroy.52Tm
- _objectdestroy.59Tm
- _objectdestroy.69Tm
- _objectdestroy.82Tm
- _objectdestroy.87Tm
- _rediscoverDefinitionsIfNeeded.calledDefinitionVendingSelectors.69435
- _rediscoverDefinitionsIfNeeded.lock.69437
- _rediscoverDefinitionsIfNeeded.onceToken.69433
- _sharedInstance.onceToken.12597
- _sharedInstance.onceToken.59128
- _sharedInstance.onceToken.8994
- _sharedManager.onceToken.1620
- _sharedManager.onceToken.60777
- _sharedManager.onceToken.68500
- _sharedManager.sharedManager.60778
- _sharedManager.sharedManager.68502
- _sharedRegistry.onceToken.16455
- _sharedRegistry.onceToken.25373
- _sharedRegistry.sharedRegistry.16456
- _sharedRegistry.sharedRegistry.25374
- _type_layout_string 11WorkflowKit35ParameterStateValueTransformContextV
CStrings:
+ "%s Attempted to coerce a non-Screen Time entity to WFApp"
+ "%s Content from %@ is exempted from re-prompting upon count increase"
+ "%s Failed to perform batch deletion of collections: %{public}@"
+ "%s Overriding entity attribution bundle identifier for '%@' with '%@'"
+ "%s Persistent mode has already been started."
+ "%s Persistent mode has not begun yet, so can't be ended."
+ "%s Persistent mode via WFRunWorkflowAction is currently only supported when running via Spotlight."
+ "%s Skipping beginning persistent mode for run workflow action since it will handle starting it: %@"
+ "%s Trying to run Snippet Action with a non SnippetIntent"
+ "%s [WFContactSubstitutableState] Could not cast parameter state to WFContactFieldEntry: %@"
+ "-[WFContactSubstitutableState initWithValue:]_block_invoke"
+ "-[WFDatabase(SmartPrompts) shouldPromptForCurrentContentItemCount:previousCount:contentOrigin:]"
+ "-[WFLinkActionProvider createActionsForRequests:allowsActionInDenyList:forceLocalActionsOnly:]"
+ "-[WFRunWorkflowAction beginPersistentModeIfReady]"
+ "-[WFRunWorkflowAction beginPersistentModeIfReady]_block_invoke"
+ "-[WFRunWorkflowAction endPersistentModeWithError:]"
+ "-[WFRunWorkflowAction endPersistentModeWithError:]_block_invoke"
+ "-[WFWorkflow saveWithCompletionBlock:]_block_invoke_2"
+ "/etc/"
+ "/private/etc/"
+ "<ContentGraphRepresentationContext key:"
+ "?"
+ "@\"CHSControlIdentity\""
+ "@\"NSString\"24@?0@\"WFWorkflowCollection\"8Q16"
+ "@\"WFWorkflowCollection\""
+ "@176@0:8@16@24q32S40@44@52@60@68Q76q84B92B96@100@108@116q124@132B140B144B148B152@156@164B172"
+ "@44@0:8@16@24S32q36"
+ "@44@0:8@16S24q28@36"
+ "@76@0:8@16@24@32@40B48@52B60B64Q68"
+ "@76@0:8@16Q24@32@40B48@52B60B64Q68"
+ "B40@0:8Q16Q24@32"
+ "B60@0:8@16@24S32q36@44^@52"
+ "Foundation localizations: %s"
+ "IntelligencePlatformDataActionsAppIntentsExtension.AppUsageAppEntity"
+ "IntelligencePlatformDataActionsAppIntentsExtension.AppUsageResultEntity"
+ "IntelligencePlatformDataActionsAppIntentsExtension.DeviceActivityDeviceAppEntity"
+ "LegacyFolderSync"
+ "Local WFWorkflowCollectionRecord with identifier %{public}s has the same recordChangeTag as fetched ordering record, this is likely our own change, discarding it."
+ "Memory Creation available"
+ "Memory Creation is Unavailable"
+ "Memory Creation is not available on this device."
+ "Memory Creation restricted with no reason"
+ "Memory Creation unavailable with info: %s"
+ "Memory Creation unavailable, unhandled enum case: %s"
+ "Memory Creation: assetIsNotReady, but still returning available"
+ "Memory Creation: restricted with reason %s"
+ "Preferred languages: %s"
+ "Preferred localizations: %s"
+ "Resolving typed value %s into content collection with context: %s, type: %s"
+ "Siri language: %s"
+ "T@\"NSArray\",N,C"
+ "T@\"NSData\",N,R"
+ "T@\"NSString\",&,N,V_shortcutsId"
+ "T@\"NSString\",C,N,V_searchAttributionAppBundleIdentifier"
+ "T@\"NSString\",C,N,V_shortcutsId"
+ "TB,N,V_hasBegunPersistentMode"
+ "TB,N,V_hasOutputAction"
+ "TB,N,V_isSavingWorkflowRecordForSync"
+ "TB,N,V_showInSearch"
+ "TB,N,V_spotlightReadyForPersistentMode"
+ "TB,R,N,V_hasOutputAction"
+ "TB,R,N,V_showInSearch"
+ "TS,N,R,Vicon"
+ "Tq,N,R,VencryptedSchemaVersion"
+ "T{os_unfair_lock_s=I},R,N,V_possibleStatesLock"
+ "WFDatabaseLegacyFolderRecord"
+ "WFDatabaseLegacyOrderingRecord"
+ "WFLinkPhotosCreateMemoryAction"
+ "WFMessageContentItem"
+ "WFiWorkActionsMigration"
+ "WorkflowKit.WFDatabaseLegacyFolderRecord"
+ "WorkflowKit.WFDatabaseLegacyOrderingRecord"
+ "_TtC11WorkflowKit42WFPhotosMemoryCreationAvailabilityResource"
+ "_hasBegunPersistentMode"
+ "_hasOutputAction"
+ "_isSavingWorkflowRecordForSync"
+ "_possibleStatesLock"
+ "_searchAttributionAppBundleIdentifier"
+ "_shortcutsId"
+ "_showInSearch"
+ "_spotlightReadyForPersistentMode"
+ "allCollectionIdentifiersForSync"
+ "allVariables"
+ "beginPersistentModeForSpotlightWhenReady"
+ "beginPersistentModeIfReady"
+ "bundleIdentifiersExemptedFromRepromptingUponCountIncrease"
+ "com.apple.Keynote"
+ "com.apple.Numbers"
+ "com.apple.Photos.OpenMemoryCreationViewIntent"
+ "com.apple.ScreenTimeWidgetApplication"
+ "com.apple.iWork.Keynote"
+ "com.apple.iWork.Numbers"
+ "com.apple.iWork.Pages"
+ "com.apple.mobileslideshow.OpenMemoryCreationViewIntent"
+ "debugLegacyFolderSyncState"
+ "defaultShowInSearch"
+ "desiredFolderSyncOperationForCollection:"
+ "desiredOrderingSyncOperationForCollection:"
+ "endPersistentModeWithError:"
+ "execute:"
+ "folderRecordForCollection:error:"
+ "fullyQualifiedTypeName"
+ "get desired folder sync operation"
+ "get desired ordering sync operation"
+ "get folder record"
+ "get ordering record"
+ "get remote folder ordering"
+ "get remote shortcut ordering"
+ "handle fetched folder record"
+ "handle fetched ordering record"
+ "handleDeletedFolderRecordWithIdentifier:error:"
+ "handleFetchedFolderRecordWithIdentifier:name:icon:encryptedSchemaVersion:cloudKitMetadata:error:"
+ "handleFetchedOrderingRecordWithIdentifier:shortcuts:folders:cloudKitMetadata:error:"
+ "hasBegunPersistentMode"
+ "hasFolderWithIdentifier:"
+ "hasOutputAction"
+ "hasShortcutsId"
+ "initWithIdentifier:name:color:glyphCharacter:associatedAppBundleIdentifier:searchAttributionAppBundleIdentifier:"
+ "initWithIdentifier:name:color:glyphCharacter:associatedAppBundleIdentifier:searchAttributionAppBundleIdentifier:subtitle:actionsDescription:actionCount:syncHash:isDeleted:hiddenFromLibraryAndSync:creationDate:modificationDate:lastRunDate:remoteQuarantineStatus:remoteQuarantineHash:showInSearch:receivesInputFromSearch:hasShortcutInputVariables:disabledOnLockScreen:source:runEventsCount:hasOutputAction:"
+ "initWithIdentifier:name:icon:encryptedSchemaVersion:"
+ "initWithName:icon:encryptedSchemaVersion:cloudKitMetadata:"
+ "initWithShortcuts:folders:cloudKitMetadata:"
+ "isSavingWorkflowRecordForSync"
+ "last remote collection subset: "
+ "last remote collections: "
+ "last remote shortcuts: "
+ "lastRemoteFolderOrderingForCollection:"
+ "lastRemoteShortcutOrderingForCollection:"
+ "lock_setPossibleStatesCollection:"
+ "markdownRenderingV2Enabled"
+ "markdown_rendering_v2"
+ "millimeters"
+ "orderingRecordForCollection:error:"
+ "outputOriginDisplayableAppBundleIdentifier"
+ "possibleStatesLock"
+ "searchAttributionAppBundleIdentifier"
+ "set folder cloudkit metadata"
+ "set ordering cloudkit metadata"
+ "setCloudKitMetadata:forFolderRecordWithIdentifier:error:"
+ "setCloudKitMetadata:forOrderingRecordWithIdentifier:error:"
+ "setHasBegunPersistentMode:"
+ "setHasOutputAction:"
+ "setIsSavingWorkflowRecordForSync:"
+ "setSearchAttributionAppBundleIdentifier:"
+ "setShortcutsId:"
+ "setShowInSearch:"
+ "setSpotlightReadyForPersistentMode:"
+ "sharedPreferences"
+ "shortcutsId"
+ "shouldPromptForCurrentContentItemCount:previousCount:contentOrigin:"
+ "showInSearch"
+ "spotlightReadyForPersistentMode"
+ "updateSearchAttribution"
+ "visibleReferencesForWorkflowIDs:sortBy:nameContaining:nameEqualing:hasAssociatedAppBundleIdentifier:associatedAppBundleIdentifier:isRecentlyModified:isRecentlyRun:limitTo:"
+ "visibleReferencesForWorkflowIDs:sortByKeys:nameContaining:nameEqualing:hasAssociatedAppBundleIdentifier:associatedAppBundleIdentifier:isRecentlyModified:isRecentlyRun:limitTo:"
- "%K == YES"
- "%s Creating test database at %@"
- "%s Destroying persistent store coordinator"
- "%s Failed to deserialize last remote shortcut ordering subset from plist data: %{public}@"
- "%s Failed to perform batch deletion of tombstoned folders: %{public}@"
- "%s Failed to perform batch reset of sync state on all collections: %{public}@"
- "%s Failed to serialize last remote shortcut ordering subset into plist data: %{public}@"
- "%s Reordering %lu shortcuts for %@"
- "%s Setting collection ordering for %@: %@"
- "%s Setting shortcut ordering for %@: %@"
- "%s Trying to run Snipppet Action with a non SnippetIntent"
- "%s Unable to set shortcut ordering for collection: %@ %@"
- "%s Unable to set shortcut ordering for folder: %@ %@"
- "+[WFDatabase createDatabaseForTesting]"
- "-[WFCoreDataCollection(RecordStorage) deserializedLastRemoteShortcutOrderingSubset]"
- "-[WFCoreDataCollection(RecordStorage) setDeserializedLastRemoteShortcutOrderingSubset:]"
- "-[WFCoreDataCollectionModel setCollectionOrdering:]"
- "-[WFCoreDataCollectionModel setShortcutOrdering:]"
- "-[WFDatabase(SmartPrompts) shouldPromptForCurrentContentItemCount:previousCount:]"
- "-[WFLinkActionProvider createActionsForRequests:allowsActionInDenyList:forceLocalActionsOnly:]_block_invoke_2"
- "-[WFWorkflowCollectionRecord saveChangesToStorage:error:]"
- "@\"NSManagedObject\"16@0:8"
- "@\"WFCoreDataCollection\""
- "@\"WFWorkflowCollectionRecord\"16@?0^@8"
- "@160@0:8@16@24q32S40@44@52@60Q68q76B84B88@92@100@108q116@124B132B136B140@144@152"
- "@32@0:8@\"NSManagedObject\"16@\"WFDatabase\"24"
- "@80@0:8@16@24@32@40B48@52B60B64B68Q72"
- "@80@0:8@16Q24@32@40B48@52B60B64B68Q72"
- "B32@0:8Q16Q24"
- "T@\"NSData\",C,N"
- "T@\"NSData\",C,N,V_cloudKitFolderRecordMetadata"
- "T@\"NSData\",C,N,V_cloudKitOrderingRecordMetadata"
- "T@\"NSManagedObject\",R,N"
- "T@\"NSOrderedSet\",C,N,V_collectionOrdering"
- "T@\"NSOrderedSet\",C,N,V_lastRemoteCollectionOrdering"
- "T@\"NSOrderedSet\",C,N,V_lastRemoteCollectionOrderingSubset"
- "T@\"NSOrderedSet\",C,N,V_lastRemoteShortcutOrdering"
- "T@\"NSOrderedSet\",C,N,V_lastRemoteShortcutOrderingSubset"
- "T@\"NSOrderedSet\",C,N,V_shortcutOrdering"
- "T@\"NSString\",R,N,V_workflowType"
- "T@\"WFCoreDataCollection\",R,N,V_coreDataCollection"
- "TB,N,V_destroysOnDeallocation"
- "TB,R,N,GisDeleted,V_deleted"
- "TB,R,N,GisFolder,V_folder"
- "TB,R,N,V_isRootCollection"
- "TS,N"
- "TS,N,V_glyphCharacter"
- "WFCoreDataCollectionModel"
- "WFDatabaseRecordStorage"
- "WFWorkflowCollectionRecord"
- "_cloudKitFolderRecordMetadata"
- "_cloudKitOrderingRecordMetadata"
- "_collectionOrdering"
- "_coreDataCollection"
- "_destroysOnDeallocation"
- "_folder"
- "_glyphCharacter"
- "_isRootCollection"
- "_lastRemoteCollectionOrdering"
- "_lastRemoteCollectionOrderingSubset"
- "_lastRemoteShortcutOrdering"
- "_lastRemoteShortcutOrderingSubset"
- "_shortcutOrdering"
- "_workflowType"
- "allCollections"
- "collectionOrdering"
- "collectionRecordForCollectionIdentifier:createIfNecessary:"
- "coreDataCollection"
- "createTemporaryFileWithFilename:"
- "deletedFolders"
- "deserializedLastRemoteShortcutOrderingSubset"
- "destroysOnDeallocation"
- "get/create collection by id"
- "has tombstoned conflicts"
- "hasTombstonedConflicts"
- "hasWorkflowWithID:"
- "initWithCollectionRecord:identifier:"
- "initWithIdentifier:name:color:glyphCharacter:associatedAppBundleIdentifier:"
- "initWithIdentifier:name:color:glyphCharacter:associatedAppBundleIdentifier:subtitle:actionsDescription:actionCount:syncHash:isDeleted:hiddenFromLibraryAndSync:creationDate:modificationDate:lastRunDate:remoteQuarantineStatus:remoteQuarantineHash:receivesInputFromSearch:hasShortcutInputVariables:disabledOnLockScreen:source:runEventsCount:"
- "insert folder into library"
- "isRootCollection"
- "setCollectionOrdering:"
- "setDeserializedLastRemoteShortcutOrderingSubset:"
- "setDestroysOnDeallocation:"
- "setGlyphCharacter:"
- "setLastRemoteCollectionOrdering:"
- "setLastRemoteCollectionOrderingSubset:"
- "setLastRemoteShortcutOrdering:"
- "setLastRemoteShortcutOrderingSubset:"
- "setLastRemoteShortcutOrderingSubsetData:"
- "setShortcutOrdering:"
- "shortcutOrdering"
- "shouldPromptForCurrentContentItemCount:previousCount:"
- "sortedWorkflowsWithQuery:hasTombstonedConflicts:"
- "variableProvider:variableWasMoved:"
- "visibleReferencesForWorkflowIDs:sortBy:nameContaining:nameEqualing:hasAssociatedAppBundleIdentifier:associatedAppBundleIdentifier:hasTombstonedConflicts:isRecentlyModified:isRecentlyRun:limitTo:"
- "visibleReferencesForWorkflowIDs:sortByKeys:nameContaining:nameEqualing:hasAssociatedAppBundleIdentifier:associatedAppBundleIdentifier:hasTombstonedConflicts:isRecentlyModified:isRecentlyRun:limitTo:"
- "workflowsWithTombstonedConflicts"

```
