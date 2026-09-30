## WorkflowKit

> `/System/Library/PrivateFrameworks/WorkflowKit.framework/Versions/A/WorkflowKit`

```diff

-5034.0.10.0.0
-  __TEXT.__text: 0x91b5dc
-  __TEXT.__objc_methlist: 0x2ed38
-  __TEXT.__const: 0x24038
-  __TEXT.__dlopen_cstrs: 0xeec
-  __TEXT.__swift5_typeref: 0xcdba
-  __TEXT.__cstring: 0x8c3ef
-  __TEXT.__oslogstring: 0x21fe6
-  __TEXT.__constg_swiftt: 0x95cc
-  __TEXT.__swift5_reflstr: 0x6028
-  __TEXT.__swift5_fieldmd: 0x7640
-  __TEXT.__swift5_builtin: 0x668
-  __TEXT.__swift5_assocty: 0x2338
-  __TEXT.__swift5_proto: 0x1a6c
-  __TEXT.__swift5_types: 0xb0c
-  __TEXT.__swift5_capture: 0x53e8
-  __TEXT.__swift_as_entry: 0xac0
-  __TEXT.__swift_as_ret: 0xbe4
-  __TEXT.__swift_as_cont: 0x1368
-  __TEXT.__swift5_protos: 0x138
+5037.0.17.0.0
+  __TEXT.__text: 0x929ac4
+  __TEXT.__objc_methlist: 0x2ee7c
+  __TEXT.__const: 0x24318
+  __TEXT.__dlopen_cstrs: 0xf56
+  __TEXT.__swift5_typeref: 0xcf62
+  __TEXT.__cstring: 0x8cb81
+  __TEXT.__oslogstring: 0x22aa7
+  __TEXT.__constg_swiftt: 0x966c
+  __TEXT.__swift5_reflstr: 0x61b8
+  __TEXT.__swift5_fieldmd: 0x7754
+  __TEXT.__swift5_builtin: 0x654
+  __TEXT.__swift5_assocty: 0x22a8
+  __TEXT.__swift5_proto: 0x1a64
+  __TEXT.__swift5_types: 0xb14
+  __TEXT.__swift5_capture: 0x55e4
+  __TEXT.__swift_as_entry: 0xae0
+  __TEXT.__swift_as_ret: 0xc00
+  __TEXT.__swift_as_cont: 0x1384
+  __TEXT.__swift5_protos: 0x13c
   __TEXT.__swift5_mpenum: 0xc4
-  __TEXT.__gcc_except_tab: 0x4d30
+  __TEXT.__gcc_except_tab: 0x4dd4
   __TEXT.__ustring: 0x3d82
-  __TEXT.__unwind_info: 0x1b398
-  __TEXT.__eh_frame: 0x21d80
+  __TEXT.__unwind_info: 0x1b648
+  __TEXT.__eh_frame: 0x22360
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x5008
-  __DATA_CONST.__objc_classlist: 0x2430
-  __DATA_CONST.__objc_catlist: 0x3e8
-  __DATA_CONST.__objc_protolist: 0x688
+  __DATA_CONST.__const: 0x50b0
+  __DATA_CONST.__objc_classlist: 0x2420
+  __DATA_CONST.__objc_catlist: 0x3e0
+  __DATA_CONST.__objc_protolist: 0x690
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x13728
-  __DATA_CONST.__objc_protorefs: 0x298
-  __DATA_CONST.__objc_superrefs: 0x1390
-  __DATA_CONST.__objc_arraydata: 0x1728
-  __DATA_CONST.__got: 0x5bc0
-  __AUTH_CONST.__const: 0x4a0c8
-  __AUTH_CONST.__cfstring: 0x2c620
-  __AUTH_CONST.__objc_const: 0x55a08
-  __AUTH_CONST.__objc_dictobj: 0x528
+  __DATA_CONST.__objc_selrefs: 0x13820
+  __DATA_CONST.__objc_protorefs: 0x290
+  __DATA_CONST.__objc_superrefs: 0x1380
+  __DATA_CONST.__objc_arraydata: 0x1690
+  __DATA_CONST.__got: 0x5ba0
+  __AUTH_CONST.__const: 0x4a718
+  __AUTH_CONST.__cfstring: 0x2c760
+  __AUTH_CONST.__objc_const: 0x559c8
+  __AUTH_CONST.__objc_dictobj: 0x4d8
   __AUTH_CONST.__objc_intobj: 0x1038
-  __AUTH_CONST.__objc_arrayobj: 0x978
+  __AUTH_CONST.__objc_arrayobj: 0x960
   __AUTH_CONST.__objc_doubleobj: 0x20
-  __AUTH_CONST.__auth_got: 0x4e08
-  __AUTH.__objc_data: 0xf618
-  __AUTH.__data: 0x63b8
-  __DATA.__objc_ivar: 0x21e0
-  __DATA.__data: 0xc8a8
-  __DATA.__bss: 0x2db10
-  __DATA.__common: 0x23f8
-  __DATA_DIRTY.__objc_data: 0xa728
-  __DATA_DIRTY.__data: 0x1e98
+  __AUTH_CONST.__auth_got: 0x4e28
+  __AUTH.__objc_data: 0xf560
+  __AUTH.__data: 0x6358
+  __DATA.__objc_ivar: 0x21c8
+  __DATA.__data: 0xc8f8
+  __DATA.__bss: 0x2d990
+  __DATA.__common: 0x2cb8
+  __DATA_DIRTY.__objc_data: 0xa6d8
+  __DATA_DIRTY.__data: 0x1e90
   __DATA_DIRTY.__bss: 0x2358
   __DATA_DIRTY.__common: 0x18
   - /System/Library/Frameworks/Accelerate.framework/Versions/A/Accelerate

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 43081
-  Symbols:   43137
-  CStrings:  17870
+  Functions: 43267
+  Symbols:   43210
+  CStrings:  17945
 
Symbols:
+ +[NSUserDefaults(Workflow) setShouldHideCompositionPane:]
+ +[NSUserDefaults(Workflow) shouldHideCompositionPane]
+ +[WFAppInFocusTrigger(ContentInput) contentCollectionWithEventInfo:completion:]
+ +[WFDiskMountTrigger eventNameEventInfoKey]
+ +[WFProgramNode(Errors) errorForInvalidVariable:reason:]
+ +[WFProgramNode(Errors) errorForVariableMissingProducingTrigger:]
+ +[WFScreenTimeHelper areWebContentRestrictionsEnabled]
+ +[WFWritingToolsAvailabilityResource isSystemWritingToolsAvailable]
+ -[LNActionParameterMetadata(Workflow) wf_contentItemClassUsingOwnEntityMetadata]
+ -[WFAction(Definition) rateLimitKeySuffix]
+ -[WFAction(Definition) rateLimitMaxDelay]
+ -[WFAction(Definition) rateLimitMultiplier]
+ -[WFAlarmDataSource .cxx_destruct]
+ -[WFAlarmDataSource addObserver:]
+ -[WFAlarmDataSource alarmAtRow:]
+ -[WFAlarmDataSource dataSourceDidReload:]
+ -[WFAlarmDataSource dataSource]
+ -[WFAlarmDataSource dealloc]
+ -[WFAlarmDataSource init]
+ -[WFAlarmDataSource numberOfAlarms]
+ -[WFAlarmDataSource observers]
+ -[WFAlarmDataSource reloadAlarms]
+ -[WFAlarmDataSource removeObserver:]
+ -[WFAppIntentExecutionAction connection:requestUnlockForAppProtectionWithReply:]
+ -[WFAppIntentExecutionAction linkActionWithParameterStates:usingConnectionPolicy:forUseCase:]
+ -[WFAppIntentExecutionAction valueForParameterData:withParameterState:forUseCase:]
+ -[WFAppPickerParameter omittedAppBundleIdentifiers]
+ -[WFCloudKitSyncToken clientVersionForCompletedActivity:]
+ -[WFCloudKitSyncToken completedOneTimeActivitiesData]
+ -[WFCloudKitSyncToken markActivityCompleted:]
+ -[WFCloudKitSyncToken setCompletedOneTimeActivitiesData:]
+ -[WFCloudKitSyncToken wf_completedOneTimeActivities]
+ -[WFDatabase(TrackedFilesystemNode) trackedFilesystemNodeForTriggerID:]
+ -[WFDatabase(WFDatabaseProvider) allDatabases]
+ -[WFDatabase(WFDatabaseProvider) databaseForWorkflowID:]
+ -[WFLinkAction linkActionWithSerializedParametersUsingConnectionPolicy:forUseCase:]
+ -[WFLinkAction setOutputInFinishRunningWithResult:]
+ -[WFLinkActionApplicationParameterDefinition linkValueFromParameterState:action:forUseCase:]
+ -[WFLinkActionArrayParameterDefinition linkValueFromParameterState:action:forUseCase:]
+ -[WFLinkActionAttributedStringParameterDefinition linkValueFromParameterState:action:forUseCase:]
+ -[WFLinkActionBoolParameterDefinition linkValueFromParameterState:action:forUseCase:]
+ -[WFLinkActionCodableValueParameterDefinition linkValueFromParameterState:action:forUseCase:]
+ -[WFLinkActionConfiguredSystemActionParameterDefinition linkValueFromParameterState:action:forUseCase:]
+ -[WFLinkActionCurrencyAmountParameterDefinition linkValueFromParameterState:action:forUseCase:]
+ -[WFLinkActionDateComponentsParameterDefinition linkValueFromParameterState:action:forUseCase:]
+ -[WFLinkActionDateParameterDefinition linkValueFromParameterState:action:forUseCase:]
+ -[WFLinkActionDoubleParameterDefinition linkValueFromParameterState:action:forUseCase:]
+ -[WFLinkActionDynamicOptionsParameterDefinition linkValueFromParameterState:action:forUseCase:]
+ -[WFLinkActionEntityCollectionSearchCriteriaParameterDefinition linkValueFromParameterState:action:forUseCase:]
+ -[WFLinkActionEntityParameterDefinition linkValueFromParameterState:action:forUseCase:]
+ -[WFLinkActionEnumParameterDefinition linkValueFromParameterState:action:forUseCase:]
+ -[WFLinkActionFileEntityParameterDefinition linkValueFromParameterState:action:forUseCase:]
+ -[WFLinkActionFileParameterDefinition linkValueFromParameterState:action:forUseCase:]
+ -[WFLinkActionIntParameterDefinition linkValueFromParameterState:action:forUseCase:]
+ -[WFLinkActionMeasurementParameterDefinition linkValueFromParameterState:action:forUseCase:]
+ -[WFLinkActionParameterDefinition linkValueFromParameterState:action:forUseCase:]
+ -[WFLinkActionPaymentMethodParameterDefinition linkValueFromParameterState:action:forUseCase:]
+ -[WFLinkActionPersonParameterDefinition linkValueFromParameterState:action:forUseCase:]
+ -[WFLinkActionPhotoItemCollectionParameterDefinition linkValueFromParameterState:action:forUseCase:]
+ -[WFLinkActionPlacemarkParameterDefinition linkValueFromParameterState:action:forUseCase:]
+ -[WFLinkActionRecurrenceRuleParameterDefinition linkValueFromParameterState:action:forUseCase:]
+ -[WFLinkActionStringParameterDefinition linkValueFromParameterState:action:forUseCase:]
+ -[WFLinkActionStringSearchCriteriaParameterDefinition linkValueFromParameterState:action:forUseCase:]
+ -[WFLinkActionSystemShortcutParameterDefinition linkValueFromParameterState:action:forUseCase:]
+ -[WFLinkActionURLParameterDefinition linkValueFromParameterState:action:forUseCase:]
+ -[WFLinkActionUnionParameterDefinition linkValueFromParameterState:action:forUseCase:]
+ -[WFLinkContentItemFilterAction runSpotlightQuery:sortingAndSlicingBeforeHydrationWithSortKey:random:ascending:instanceKey:]
+ -[WFLinkContentItemFilterAction wf_collection:orderedByInstanceIdentifiers:]
+ -[WFLinkContentItemFilterAction wf_spotlightSortKeyForProperty:]
+ -[WFSpotlightSortCandidate .cxx_destruct]
+ -[WFSpotlightSortCandidate instanceIdentifier]
+ -[WFSpotlightSortCandidate setInstanceIdentifier:]
+ -[WFSpotlightSortCandidate setSortValue:]
+ -[WFSpotlightSortCandidate sortValue]
+ -[WFUIPresenterLaunchAngelConnection _cleanUpOnQueueWithReason:]
+ -[WFUIPresenterLaunchAngelConnection _handleConnectionInterruption]
+ -[WFUIPresenterLaunchAngelConnection _handleConnectionInvalidation:]
+ -[WFUIPresenterLaunchAngelConnection isolationQueue]
+ -[WFUIPresenterLaunchAngelConnection makeConfiguredConnectionForHost:]
+ -[WFUIPresenterLaunchAngelConnection takeErrorHandler]
+ -[WFWorkflowController dispatchDelegateBlock:]
+ GCC_except_table1001
+ GCC_except_table10042
+ GCC_except_table1014
+ GCC_except_table10212
+ GCC_except_table10218
+ GCC_except_table10237
+ GCC_except_table10403
+ GCC_except_table10438
+ GCC_except_table10471
+ GCC_except_table10473
+ GCC_except_table10505
+ GCC_except_table10507
+ GCC_except_table10509
+ GCC_except_table10551
+ GCC_except_table10556
+ GCC_except_table10596
+ GCC_except_table10599
+ GCC_except_table10602
+ GCC_except_table10605
+ GCC_except_table10794
+ GCC_except_table10906
+ GCC_except_table10923
+ GCC_except_table10969
+ GCC_except_table11216
+ GCC_except_table11243
+ GCC_except_table11258
+ GCC_except_table11318
+ GCC_except_table11462
+ GCC_except_table11543
+ GCC_except_table11549
+ GCC_except_table11552
+ GCC_except_table11555
+ GCC_except_table11561
+ GCC_except_table11564
+ GCC_except_table11571
+ GCC_except_table11575
+ GCC_except_table11580
+ GCC_except_table11587
+ GCC_except_table11592
+ GCC_except_table11595
+ GCC_except_table11598
+ GCC_except_table11601
+ GCC_except_table11604
+ GCC_except_table11607
+ GCC_except_table11610
+ GCC_except_table11613
+ GCC_except_table11616
+ GCC_except_table11619
+ GCC_except_table11622
+ GCC_except_table11625
+ GCC_except_table11628
+ GCC_except_table11733
+ GCC_except_table11923
+ GCC_except_table12083
+ GCC_except_table12104
+ GCC_except_table12106
+ GCC_except_table12111
+ GCC_except_table12156
+ GCC_except_table12163
+ GCC_except_table12217
+ GCC_except_table12256
+ GCC_except_table12270
+ GCC_except_table12274
+ GCC_except_table12276
+ GCC_except_table12372
+ GCC_except_table12388
+ GCC_except_table12493
+ GCC_except_table12554
+ GCC_except_table12607
+ GCC_except_table12636
+ GCC_except_table12692
+ GCC_except_table12703
+ GCC_except_table12753
+ GCC_except_table12755
+ GCC_except_table12770
+ GCC_except_table12928
+ GCC_except_table12990
+ GCC_except_table13039
+ GCC_except_table13118
+ GCC_except_table1314
+ GCC_except_table13146
+ GCC_except_table13152
+ GCC_except_table13201
+ GCC_except_table13245
+ GCC_except_table13258
+ GCC_except_table13263
+ GCC_except_table13284
+ GCC_except_table13285
+ GCC_except_table13286
+ GCC_except_table13295
+ GCC_except_table13306
+ GCC_except_table13456
+ GCC_except_table13482
+ GCC_except_table13484
+ GCC_except_table13544
+ GCC_except_table13556
+ GCC_except_table13560
+ GCC_except_table13796
+ GCC_except_table13864
+ GCC_except_table14139
+ GCC_except_table14180
+ GCC_except_table1421
+ GCC_except_table1426
+ GCC_except_table14309
+ GCC_except_table14412
+ GCC_except_table14417
+ GCC_except_table14426
+ GCC_except_table14429
+ GCC_except_table14523
+ GCC_except_table14534
+ GCC_except_table14536
+ GCC_except_table14549
+ GCC_except_table14666
+ GCC_except_table14804
+ GCC_except_table14825
+ GCC_except_table14836
+ GCC_except_table14850
+ GCC_except_table14853
+ GCC_except_table15067
+ GCC_except_table15094
+ GCC_except_table15190
+ GCC_except_table1609
+ GCC_except_table1613
+ GCC_except_table1615
+ GCC_except_table1617
+ GCC_except_table1688
+ GCC_except_table1702
+ GCC_except_table1707
+ GCC_except_table1709
+ GCC_except_table1711
+ GCC_except_table1982
+ GCC_except_table2061
+ GCC_except_table2155
+ GCC_except_table2371
+ GCC_except_table2574
+ GCC_except_table2604
+ GCC_except_table2680
+ GCC_except_table2721
+ GCC_except_table2830
+ GCC_except_table2833
+ GCC_except_table2847
+ GCC_except_table2917
+ GCC_except_table2950
+ GCC_except_table2967
+ GCC_except_table2973
+ GCC_except_table3025
+ GCC_except_table3035
+ GCC_except_table3043
+ GCC_except_table3051
+ GCC_except_table3079
+ GCC_except_table3122
+ GCC_except_table3426
+ GCC_except_table3479
+ GCC_except_table3484
+ GCC_except_table3517
+ GCC_except_table3535
+ GCC_except_table3539
+ GCC_except_table3601
+ GCC_except_table3612
+ GCC_except_table3614
+ GCC_except_table3617
+ GCC_except_table3719
+ GCC_except_table3727
+ GCC_except_table3731
+ GCC_except_table3733
+ GCC_except_table3737
+ GCC_except_table3738
+ GCC_except_table384
+ GCC_except_table3877
+ GCC_except_table4003
+ GCC_except_table4007
+ GCC_except_table431
+ GCC_except_table434
+ GCC_except_table4386
+ GCC_except_table4499
+ GCC_except_table4588
+ GCC_except_table4602
+ GCC_except_table4621
+ GCC_except_table4629
+ GCC_except_table4779
+ GCC_except_table4982
+ GCC_except_table4988
+ GCC_except_table4994
+ GCC_except_table5045
+ GCC_except_table5059
+ GCC_except_table5121
+ GCC_except_table5192
+ GCC_except_table5219
+ GCC_except_table5226
+ GCC_except_table5268
+ GCC_except_table533
+ GCC_except_table5330
+ GCC_except_table5339
+ GCC_except_table5398
+ GCC_except_table5453
+ GCC_except_table5461
+ GCC_except_table5463
+ GCC_except_table5501
+ GCC_except_table5510
+ GCC_except_table5511
+ GCC_except_table5593
+ GCC_except_table5673
+ GCC_except_table5676
+ GCC_except_table5679
+ GCC_except_table5682
+ GCC_except_table5685
+ GCC_except_table5688
+ GCC_except_table5690
+ GCC_except_table5697
+ GCC_except_table5699
+ GCC_except_table5709
+ GCC_except_table5713
+ GCC_except_table5969
+ GCC_except_table6119
+ GCC_except_table6152
+ GCC_except_table620
+ GCC_except_table6226
+ GCC_except_table6238
+ GCC_except_table6351
+ GCC_except_table6431
+ GCC_except_table6497
+ GCC_except_table6498
+ GCC_except_table6499
+ GCC_except_table6599
+ GCC_except_table6649
+ GCC_except_table6667
+ GCC_except_table6910
+ GCC_except_table6911
+ GCC_except_table6912
+ GCC_except_table6913
+ GCC_except_table6914
+ GCC_except_table7070
+ GCC_except_table7071
+ GCC_except_table716
+ GCC_except_table7203
+ GCC_except_table7208
+ GCC_except_table7266
+ GCC_except_table7279
+ GCC_except_table7341
+ GCC_except_table7342
+ GCC_except_table749
+ GCC_except_table751
+ GCC_except_table753
+ GCC_except_table7551
+ GCC_except_table7561
+ GCC_except_table757
+ GCC_except_table7638
+ GCC_except_table7648
+ GCC_except_table7890
+ GCC_except_table7934
+ GCC_except_table7981
+ GCC_except_table7982
+ GCC_except_table8019
+ GCC_except_table8075
+ GCC_except_table8143
+ GCC_except_table8285
+ GCC_except_table8296
+ GCC_except_table8415
+ GCC_except_table8424
+ GCC_except_table8436
+ GCC_except_table8494
+ GCC_except_table8505
+ GCC_except_table8507
+ GCC_except_table8509
+ GCC_except_table8510
+ GCC_except_table9031
+ GCC_except_table9072
+ GCC_except_table9077
+ GCC_except_table9081
+ GCC_except_table9083
+ GCC_except_table9085
+ GCC_except_table9087
+ GCC_except_table9116
+ GCC_except_table916
+ GCC_except_table9254
+ GCC_except_table9306
+ GCC_except_table9510
+ GCC_except_table9516
+ GCC_except_table9521
+ GCC_except_table9525
+ GCC_except_table9527
+ GCC_except_table9529
+ GCC_except_table9531
+ GCC_except_table9535
+ GCC_except_table9537
+ GCC_except_table9549
+ GCC_except_table9553
+ GCC_except_table9566
+ GCC_except_table9579
+ GCC_except_table9585
+ GCC_except_table9593
+ GCC_except_table9640
+ GCC_except_table9646
+ GCC_except_table9652
+ GCC_except_table9690
+ GCC_except_table9699
+ GCC_except_table9797
+ GCC_except_table9856
+ GCC_except_table9885
+ GCC_except_table9887
+ GCC_except_table9893
+ GCC_except_table9895
+ GCC_except_table9904
+ GCC_except_table9925
+ GCC_except_table9926
+ GCC_except_table9929
+ GCC_except_table9934
+ OBJC_IVAR_$_WFAlarmDataSource._dataSource
+ OBJC_IVAR_$_WFAlarmDataSource._observers
+ OBJC_IVAR_$_WFAppPickerParameter._omittedAppBundleIdentifiers
+ OBJC_IVAR_$_WFCloudKitSyncToken._completedOneTimeActivitiesData
+ OBJC_IVAR_$_WFSpotlightSortCandidate._instanceIdentifier
+ OBJC_IVAR_$_WFSpotlightSortCandidate._sortValue
+ OBJC_IVAR_$_WFUIPresenterLaunchAngelConnection._isolationQueue
+ WebContentRestrictionsLibraryCore.frameworkLibrary
+ _ACAccountTypeIdentifierIMAPMail
+ _OBJC_CLASS_$_LNAnyEntityType
+ _OBJC_CLASS_$_WFAlarmDataSource
+ _OBJC_CLASS_$_WFSpotlightSortCandidate
+ _OBJC_CLASS_$__TtC11WorkflowKit21AppShortcutDataSource
+ _OBJC_METACLASS_$_WFAlarmDataSource
+ _OBJC_METACLASS_$_WFSpotlightSortCandidate
+ _OBJC_METACLASS_$__TtC11WorkflowKit21AppShortcutDataSource
+ _WFHandleIntentActionRateLimitMaxDelayKey
+ _WFHandleIntentActionRateLimitMultiplierKey
+ _WFLinkMessageEntityPreHydrationCap
+ _WFParameterOmittedAppBundleIdentifiersKey
+ _WFShortcutsExternalTriggerStoreURL
+ _WFShouldHideCompositionPane
+ _WFSpotlightAppEntityInstanceIdentifierKey
+ _WFSpotlightSnippetKey
+ _WFSpotlightTextContentKey
+ _WFWhatsNewLastPresentationOSVersionKey
+ __124-[WFLinkContentItemFilterAction runSpotlightQuery:sortingAndSlicingBeforeHydrationWithSortKey:random:ascending:instanceKey:]_block_invoke
+ __70-[WFUIPresenterLaunchAngelConnection makeConfiguredConnectionForHost:]_block_invoke
+ __CDInformativeContextualChangeNewValueKey
+ __CDInformativeContextualChangeOldValueKey
+ __DATA__TtC11WorkflowKit21AppShortcutDataSource
+ __INSTANCE_METHODS__TtC11WorkflowKit21AppShortcutDataSource
+ __IVARS__TtC11WorkflowKit21AppShortcutDataSource
+ __METACLASS_DATA__TtC11WorkflowKit21AppShortcutDataSource
+ __OBJC_$_CLASS_METHODS_WFAppInFocusTrigger(ContentInput|CoreDuetContext)
+ __OBJC_$_CLASS_METHODS_WFTriggerInputVariable(WorkflowKit|WorkflowKit1)
+ __OBJC_$_INSTANCE_METHODS_WFAlarmDataSource
+ __OBJC_$_INSTANCE_METHODS_WFAppInFocusTrigger(ContentInput|CoreDuetContext)
+ __OBJC_$_INSTANCE_METHODS_WFSpotlightSortCandidate
+ __OBJC_$_INSTANCE_METHODS_WFTriggerInputVariable(WorkflowKit|WorkflowKit1)
+ __OBJC_$_INSTANCE_VARIABLES_WFAlarmDataSource
+ __OBJC_$_INSTANCE_VARIABLES_WFSpotlightSortCandidate
+ __OBJC_$_PROP_LIST_FCActivityDescribing
+ __OBJC_$_PROP_LIST_WFAlarmDataSource
+ __OBJC_$_PROP_LIST_WFSpotlightSortCandidate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_FCActivityDescribing
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_LNConnectionDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_FCActivityDescribing
+ __OBJC_$_PROTOCOL_METHOD_TYPES_LNConnectionDelegate
+ __OBJC_$_PROTOCOL_REFS_FCActivityDescribing
+ __OBJC_$_PROTOCOL_REFS_LNConnectionDelegate
+ __OBJC_CLASS_PROTOCOLS_$_WFAlarmDataSource
+ __OBJC_CLASS_RO_$_WFAlarmDataSource
+ __OBJC_CLASS_RO_$_WFSpotlightSortCandidate
+ __OBJC_LABEL_PROTOCOL_$_FCActivityDescribing
+ __OBJC_LABEL_PROTOCOL_$_LNConnectionDelegate
+ __OBJC_METACLASS_RO_$_WFAlarmDataSource
+ __OBJC_METACLASS_RO_$_WFSpotlightSortCandidate
+ __OBJC_PROTOCOL_$_FCActivityDescribing
+ __OBJC_PROTOCOL_$_LNConnectionDelegate
+ ___124-[WFLinkContentItemFilterAction runSpotlightQuery:sortingAndSlicingBeforeHydrationWithSortKey:random:ascending:instanceKey:]_block_invoke
+ ___42-[WFUIPresenterLaunchAngelConnection host]_block_invoke
+ ___46-[WFUIPresenterLaunchAngelConnection setHost:]_block_invoke
+ ___46-[WFUIPresenterXPCConnection setErrorHandler:]_block_invoke
+ ___48-[WFUIPresenterLaunchAngelConnection connection]_block_invoke
+ ___50-[WFUIPresenterLaunchAngelConnection errorHandler]_block_invoke
+ ___52-[WFUIPresenterLaunchAngelConnection setConnection:]_block_invoke
+ ___54-[WFUIPresenterLaunchAngelConnection setErrorHandler:]_block_invoke
+ ___54-[WFUIPresenterLaunchAngelConnection takeErrorHandler]_block_invoke
+ ___59-[WFUIPresenterLaunchAngelConnection connectionInterrupted]_block_invoke
+ ___63-[WFUIPresenterLaunchAngelConnection setConnectionInterrupted:]_block_invoke
+ ___68-[WFUIPresenterLaunchAngelConnection _handleConnectionInvalidation:]_block_invoke
+ ___70-[WFUIPresenterLaunchAngelConnection makeConfiguredConnectionForHost:]_block_invoke
+ ___70-[WFUIPresenterLaunchAngelConnection makeConfiguredConnectionForHost:]_block_invoke_2
+ ___86-[WFLinkActionArrayParameterDefinition linkValueFromParameterState:action:forUseCase:]_block_invoke
+ ___93-[WFAppIntentExecutionAction linkActionWithParameterStates:usingConnectionPolicy:forUseCase:]_block_invoke
+ ___WebContentRestrictionsLibraryCore_block_invoke
+ ___block_descriptor_33_e32_B16?0"<FCActivityDescribing>"8l
+ ___block_descriptor_40_e8_32w_e57_v16?0"BSServiceConnection<BSServiceConnectionContext>"8l
+ ___block_descriptor_41_e8_32r_e11_q24?0816l
+ ___block_descriptor_48_e8_32r40r_e38_v24?0"WFDialogResponse"8"NSError"16l
+ ___block_descriptor_48_e8_32s40w_e42_v16?0"<BSServiceConnectionConfiguring>"8l
+ ___block_descriptor_56_e8_32s40s48s_e17_v16?0"NSArray"8l
+ ___block_descriptor_56_e8_32s40s_e20_"LNValue"24?08Q16l
+ ___block_descriptor_56_e8_32s40s_e50_"LNProperty"24?0"LNActionParameterMetadata"8Q16l
+ ___block_descriptor_57_e8_32s40s48r_e17_v16?0"NSError"8l
+ ___block_descriptor_72_e8_32s40s48r56r_e29_v16?0"NSMutableDictionary"8l
+ ___block_descriptor_89_e8_32s40s48s56bs64r72r_e17_v16?0"NSArray"8l
+ ___copy_helper_block_e8_32s40s48s56b64r72r
+ ___getWCRBrowserEngineClientClass_block_invoke
+ ___swift_memcpy336_8
+ _arc4random_uniform
+ _associated conformance 11WorkflowKit31TriggerRegistrationUpdateReasonOSHAASQ
+ _associated conformance 11WorkflowKit36WFTestingContainerDefinitionProvider025_150F24DA937B90A43122A8C1I5B3B56LLV5ErrorOSHAASQ
+ _audit_stringWebContentRestrictions
+ _dispatch_block_create
+ _flat unique So20FCActivityDescribing_p
+ _get_enum_tag_for_layout_string 11WorkflowKit12WFNewTriggerCAA0D24RegistrationUpdateReasonOSbIeggnd_Sg
+ _get_enum_tag_for_layout_string 11WorkflowKit12WFNewTriggerCSSIeggg_Sg
+ _get_enum_tag_for_layout_string 11WorkflowKit12WFNewTriggerCSo6WFIconCSgIeggo_Sg
+ _get_enum_tag_for_layout_string SDySSSo20WFPropertyListObject_pGABIeggo_Sg
+ _objc_msgSend$_cleanUpOnQueueWithReason:
+ _objc_msgSend$_handleConnectionInterruption
+ _objc_msgSend$_handleConnectionInvalidation:
+ _objc_msgSend$alarmsDidChange:
+ _objc_msgSend$completedOneTimeActivitiesData
+ _objc_msgSend$connectionWithDelegate:userIdentity:error:
+ _objc_msgSend$contentCreationDate
+ _objc_msgSend$dispatchDelegateBlock:
+ _objc_msgSend$errorForInvalidVariable:reason:
+ _objc_msgSend$errorForVariableMissingProducingTrigger:
+ _objc_msgSend$initWithSymbolName:bundle:
+ _objc_msgSend$initWithUniqueID:
+ _objc_msgSend$isEnhancedSiriEnabled
+ _objc_msgSend$isGenericShortcutInputVariableUsed
+ _objc_msgSend$isSystemWritingToolsAvailable
+ _objc_msgSend$linkActionWithParameterStates:usingConnectionPolicy:forUseCase:
+ _objc_msgSend$linkActionWithSerializedParametersUsingConnectionPolicy:forUseCase:
+ _objc_msgSend$linkValueFromParameterState:action:forUseCase:
+ _objc_msgSend$makeConfiguredConnectionForHost:
+ _objc_msgSend$maxCount
+ _objc_msgSend$neverSyncedTriggersToAppendWithLocalWorkflow:remoteWorkflow:pendingInitialSyncTriggerUUIDs:
+ _objc_msgSend$omittedAppBundleIdentifiers
+ _objc_msgSend$parentAccount
+ _objc_msgSend$pendingInitialSync
+ _objc_msgSend$predicateForChangeAtKeyPath:
+ _objc_msgSend$previousSunriseKey
+ _objc_msgSend$previousSunsetKey
+ _objc_msgSend$rateLimitKeySuffix
+ _objc_msgSend$rateLimitMaxDelay
+ _objc_msgSend$rateLimitMultiplier
+ _objc_msgSend$refreshAvailabilityOfAllRequiredResources
+ _objc_msgSend$runSpotlightQuery:sortingAndSlicingBeforeHydrationWithSortKey:random:ascending:instanceKey:
+ _objc_msgSend$setAddToLibrary:
+ _objc_msgSend$setCompletedOneTimeActivitiesData:
+ _objc_msgSend$setInstanceIdentifier:
+ _objc_msgSend$setMaximumValue:
+ _objc_msgSend$setMinimumValue:
+ _objc_msgSend$setOutputInFinishRunningWithResult:
+ _objc_msgSend$setPendingInitialSync:
+ _objc_msgSend$setSortValue:
+ _objc_msgSend$shouldEvaluateURLs
+ _objc_msgSend$sortValue
+ _objc_msgSend$supportsCoercion
+ _objc_msgSend$takeErrorHandler
+ _objc_msgSend$valueForParameterData:withParameterState:forUseCase:
+ _objc_msgSend$wf_collection:orderedByInstanceIdentifiers:
+ _objc_msgSend$wf_completedOneTimeActivities
+ _objc_msgSend$wf_shortcutsExternalTriggersDirectoryURL
+ _objc_msgSend$wf_spotlightSortKeyForProperty:
+ _pow
+ _symbolic SDySS______pGABIeggo_ So20WFPropertyListObjectP
+ _symbolic SDySS______pGABIegnr_ So20WFPropertyListObjectP
+ _symbolic SDySS______pGABcSg So20WFPropertyListObjectP
+ _symbolic Sb___________tcSg 11WorkflowKit12WFNewTriggerC AA0D24RegistrationUpdateReasonO
+ _symbolic Sb______pIgrzo_ s5ErrorP
+ _symbolic So22WFLeaveLocationTriggerCXMT
+ _symbolic So23WFArriveLocationTriggerCXMT
+ _symbolic So31_CDContextualChangeRegistrationCSg
+ _symbolic So32WFOutOfProcessWorkflowControllerCyYbc
+ _symbolic So6WFIconCSg_____cSg 11WorkflowKit12WFNewTriggerC
+ _symbolic _____ 11WorkflowKit12WFNewTriggerC17PendingEnablement33_31676935EC5D0EBE3B7BA15E25694244LLO
+ _symbolic _____ 11WorkflowKit31TriggerRegistrationUpdateReasonO
+ _symbolic _____ 11WorkflowKit36WFTestingContainerDefinitionProvider025_150F24DA937B90A43122A8C1I5B3B56LLV
+ _symbolic _____ 11WorkflowKit36WFTestingContainerDefinitionProvider025_150F24DA937B90A43122A8C1I5B3B56LLV5ErrorO
+ _symbolic _____ So26WFUserFocusActivityTriggerC11WorkflowKitE0B11DrawerEntryV
+ _symbolic _____SSIeggg_ 11WorkflowKit12WFNewTriggerC
+ _symbolic _____SSytIegnnr_ 11WorkflowKit12WFNewTriggerC
+ _symbolic _____Sg 10Foundation8CalendarV
+ _symbolic _____SgXw 11WorkflowKit26WFTriggerRegistrationStoreC
+ _symbolic _____So6WFIconCSgIeggo_ 11WorkflowKit12WFNewTriggerC
+ _symbolic _____So6WFIconCSgIegnr_ 11WorkflowKit12WFNewTriggerC
+ _symbolic __________SbIeggnd_ 11WorkflowKit12WFNewTriggerC AA0D24RegistrationUpdateReasonO
+ _symbolic __________SbIegnnr_ 11WorkflowKit12WFNewTriggerC AA0D24RegistrationUpdateReasonO
+ _symbolic ______p So20FCActivityDescribingP
+ _symbolic _____ySOSay_____GG s17_NativeDictionaryV s6UInt16V
+ _symbolic _____ySo31_CDContextualChangeRegistrationCSgG 15Synchronization5MutexVAARi_zrlE
+ _symbolic _____y_____G s23_ContiguousArrayStorageC So22WFContactFieldPropertya
+ _symbolic _____y_____G s23_ContiguousArrayStorageC So26WFUserFocusActivityTriggerC11WorkflowKitE0E11DrawerEntryV
+ _symbolic _____y_____G s23_ContiguousArrayStorageC s6UInt16V
+ _symbolic y______SStcSg 11WorkflowKit12WFNewTriggerC
+ _type_layout_string So26WFUserFocusActivityTriggerC11WorkflowKitE0B11DrawerEntryV
+ getMTAlarmDataSourceClass
+ getMTAlarmManagerClass
+ getWCRBrowserEngineClientClass.softClass
- +[WFAppShortcutsResultCache sharedCache]
- +[WFDiskMountTrigger triggerIDEventInfoKey]
- -[WFAppIntentExecutionAction linkActionWithParameterStates:usingConnectionPolicy:]
- -[WFAppIntentExecutionAction valueForParameterData:withParameterState:]
- -[WFAppShortcutDataSource .cxx_destruct]
- -[WFAppShortcutDataSource cache]
- -[WFAppShortcutDataSource dataSource]
- -[WFAppShortcutDataSource fetchAppShortcutsForBundleIdentifier:localeIdentifier:completionHandler:]
- -[WFAppShortcutDataSource fetchAppShortcutsForBundleIdentifiers:localeIdentifier:error:]
- -[WFAppShortcutDataSource initWithAppShortcutsDenyListEnvironment:environment:]
- -[WFAppShortcutDataSource initWithAppShortcutsDenyListEnvironment:environment:cache:]
- -[WFAppShortcutsPendingFetch .cxx_destruct]
- -[WFAppShortcutsPendingFetch generation]
- -[WFAppShortcutsPendingFetch handlers]
- -[WFAppShortcutsPendingFetch initWithGeneration:handler:]
- -[WFAppShortcutsPendingFetch setGeneration:]
- -[WFAppShortcutsPendingFetch setHandlers:]
- -[WFAppShortcutsResultCache .cxx_destruct]
- -[WFAppShortcutsResultCache _queue_invalidateAll]
- -[WFAppShortcutsResultCache _queue_invalidateBundleIdentifiers:]
- -[WFAppShortcutsResultCache appShortcutsChangedNotification:]
- -[WFAppShortcutsResultCache attachOrStartPendingFetchForBundleIdentifier:localeIdentifier:handler:]
- -[WFAppShortcutsResultCache cachedAppShortcutsForBundleIdentifier:localeIdentifier:]
- -[WFAppShortcutsResultCache completePendingFetchForBundleIdentifier:localeIdentifier:appShortcuts:error:]
- -[WFAppShortcutsResultCache dealloc]
- -[WFAppShortcutsResultCache init]
- -[WFAppShortcutsResultCache invalidateAll]
- -[WFAppShortcutsResultCache invalidateBundleIdentifiers:]
- -[WFDatabase(TrackedFilesystemNode) trackedFilesystemNodeForTriggerKey:]
- -[WFExtractShortcutResult setSidecarTrigger:]
- -[WFExtractShortcutResult sidecarTrigger]
- -[WFLinkAction linkActionWithSerializedParametersUsingConnectionPolicy:]
- -[WFLinkActionApplicationParameterDefinition linkValueFromParameterState:action:]
- -[WFLinkActionArrayParameterDefinition linkValueFromParameterState:action:]
- -[WFLinkActionAttributedStringParameterDefinition linkValueFromParameterState:action:]
- -[WFLinkActionBoolParameterDefinition linkValueFromParameterState:action:]
- -[WFLinkActionCodableValueParameterDefinition linkValueFromParameterState:action:]
- -[WFLinkActionConfiguredSystemActionParameterDefinition linkValueFromParameterState:action:]
- -[WFLinkActionCurrencyAmountParameterDefinition linkValueFromParameterState:action:]
- -[WFLinkActionDateComponentsParameterDefinition linkValueFromParameterState:action:]
- -[WFLinkActionDateParameterDefinition linkValueFromParameterState:action:]
- -[WFLinkActionDoubleParameterDefinition linkValueFromParameterState:action:]
- -[WFLinkActionDynamicOptionsParameterDefinition linkValueFromParameterState:action:]
- -[WFLinkActionEntityCollectionSearchCriteriaParameterDefinition linkValueFromParameterState:action:]
- -[WFLinkActionEntityParameterDefinition linkValueFromParameterState:action:]
- -[WFLinkActionEnumParameterDefinition linkValueFromParameterState:action:]
- -[WFLinkActionFileEntityParameterDefinition linkValueFromParameterState:action:]
- -[WFLinkActionFileParameterDefinition linkValueFromParameterState:action:]
- -[WFLinkActionIntParameterDefinition linkValueFromParameterState:action:]
- -[WFLinkActionMeasurementParameterDefinition linkValueFromParameterState:action:]
- -[WFLinkActionParameterDefinition linkValueFromParameterState:action:]
- -[WFLinkActionPaymentMethodParameterDefinition linkValueFromParameterState:]
- -[WFLinkActionPersonParameterDefinition linkValueFromParameterState:action:]
- -[WFLinkActionPhotoItemCollectionParameterDefinition linkValueFromParameterState:]
- -[WFLinkActionPlacemarkParameterDefinition linkValueFromParameterState:action:]
- -[WFLinkActionRecurrenceRuleParameterDefinition linkValueFromParameterState:action:]
- -[WFLinkActionStringParameterDefinition linkValueFromParameterState:action:]
- -[WFLinkActionStringSearchCriteriaParameterDefinition linkValueFromParameterState:action:]
- -[WFLinkActionSystemShortcutParameterDefinition linkValueFromParameterState:action:]
- -[WFLinkActionURLParameterDefinition linkValueFromParameterState:action:]
- -[WFLinkActionUnionParameterDefinition linkValueFromParameterState:action:]
- -[WFUIPresenterLaunchAngelConnection cleanUpWithReason:]
- -[WFUIPresenterLaunchAngelConnection connectionLock]
- -[WFUIPresenterLaunchAngelConnection hostLock]
- -[WFUIPresenterLaunchAngelConnection stateLock]
- -[WFWorkflowFile sidecarTrigger]
- GCC_except_table10035
- GCC_except_table1007
- GCC_except_table10205
- GCC_except_table10211
- GCC_except_table10230
- GCC_except_table10396
- GCC_except_table1040
- GCC_except_table10431
- GCC_except_table10464
- GCC_except_table10466
- GCC_except_table10491
- GCC_except_table10500
- GCC_except_table10502
- GCC_except_table10544
- GCC_except_table10549
- GCC_except_table10589
- GCC_except_table10592
- GCC_except_table10595
- GCC_except_table10598
- GCC_except_table10787
- GCC_except_table10899
- GCC_except_table10915
- GCC_except_table10961
- GCC_except_table11203
- GCC_except_table11230
- GCC_except_table11245
- GCC_except_table11305
- GCC_except_table11449
- GCC_except_table11530
- GCC_except_table11536
- GCC_except_table11539
- GCC_except_table11542
- GCC_except_table11545
- GCC_except_table11548
- GCC_except_table11551
- GCC_except_table11554
- GCC_except_table11562
- GCC_except_table11574
- GCC_except_table11579
- GCC_except_table11582
- GCC_except_table11585
- GCC_except_table11588
- GCC_except_table11591
- GCC_except_table11594
- GCC_except_table11597
- GCC_except_table11600
- GCC_except_table11603
- GCC_except_table11606
- GCC_except_table11609
- GCC_except_table11612
- GCC_except_table11615
- GCC_except_table11720
- GCC_except_table11910
- GCC_except_table12070
- GCC_except_table12085
- GCC_except_table12091
- GCC_except_table12093
- GCC_except_table12130
- GCC_except_table12150
- GCC_except_table12204
- GCC_except_table12243
- GCC_except_table12257
- GCC_except_table12261
- GCC_except_table12263
- GCC_except_table12358
- GCC_except_table12374
- GCC_except_table12479
- GCC_except_table12540
- GCC_except_table12592
- GCC_except_table12621
- GCC_except_table12677
- GCC_except_table12688
- GCC_except_table12733
- GCC_except_table12735
- GCC_except_table12900
- GCC_except_table12962
- GCC_except_table13011
- GCC_except_table13089
- GCC_except_table13117
- GCC_except_table13123
- GCC_except_table13172
- GCC_except_table13216
- GCC_except_table13229
- GCC_except_table13234
- GCC_except_table13248
- GCC_except_table13255
- GCC_except_table13256
- GCC_except_table13257
- GCC_except_table13266
- GCC_except_table13427
- GCC_except_table13453
- GCC_except_table13455
- GCC_except_table13515
- GCC_except_table1352
- GCC_except_table13527
- GCC_except_table13531
- GCC_except_table13767
- GCC_except_table13835
- GCC_except_table14110
- GCC_except_table14151
- GCC_except_table14280
- GCC_except_table14383
- GCC_except_table14388
- GCC_except_table14397
- GCC_except_table14400
- GCC_except_table14465
- GCC_except_table14505
- GCC_except_table14507
- GCC_except_table14520
- GCC_except_table1459
- GCC_except_table14637
- GCC_except_table1464
- GCC_except_table14775
- GCC_except_table14796
- GCC_except_table14807
- GCC_except_table14821
- GCC_except_table14824
- GCC_except_table15037
- GCC_except_table15064
- GCC_except_table15160
- GCC_except_table1645
- GCC_except_table1649
- GCC_except_table1651
- GCC_except_table1653
- GCC_except_table1724
- GCC_except_table1738
- GCC_except_table1743
- GCC_except_table1745
- GCC_except_table1747
- GCC_except_table2017
- GCC_except_table2096
- GCC_except_table2190
- GCC_except_table2406
- GCC_except_table2609
- GCC_except_table2639
- GCC_except_table2715
- GCC_except_table2756
- GCC_except_table2864
- GCC_except_table2867
- GCC_except_table2881
- GCC_except_table2949
- GCC_except_table2982
- GCC_except_table2999
- GCC_except_table3005
- GCC_except_table3057
- GCC_except_table3067
- GCC_except_table3075
- GCC_except_table3083
- GCC_except_table3111
- GCC_except_table3154
- GCC_except_table3456
- GCC_except_table3509
- GCC_except_table3514
- GCC_except_table3547
- GCC_except_table3565
- GCC_except_table3569
- GCC_except_table3631
- GCC_except_table3642
- GCC_except_table3644
- GCC_except_table3647
- GCC_except_table3749
- GCC_except_table3757
- GCC_except_table3761
- GCC_except_table3763
- GCC_except_table3767
- GCC_except_table3768
- GCC_except_table3907
- GCC_except_table4033
- GCC_except_table4037
- GCC_except_table424
- GCC_except_table427
- GCC_except_table4416
- GCC_except_table4529
- GCC_except_table4618
- GCC_except_table4632
- GCC_except_table4651
- GCC_except_table4659
- GCC_except_table4809
- GCC_except_table5012
- GCC_except_table5018
- GCC_except_table5024
- GCC_except_table5075
- GCC_except_table5089
- GCC_except_table5151
- GCC_except_table5222
- GCC_except_table5249
- GCC_except_table5255
- GCC_except_table526
- GCC_except_table5299
- GCC_except_table5360
- GCC_except_table5369
- GCC_except_table5430
- GCC_except_table5487
- GCC_except_table5492
- GCC_except_table5494
- GCC_except_table5606
- GCC_except_table5686
- GCC_except_table5689
- GCC_except_table5698
- GCC_except_table5701
- GCC_except_table5708
- GCC_except_table5710
- GCC_except_table5712
- GCC_except_table5716
- GCC_except_table5718
- GCC_except_table5722
- GCC_except_table5726
- GCC_except_table5982
- GCC_except_table613
- GCC_except_table6132
- GCC_except_table6165
- GCC_except_table6241
- GCC_except_table6253
- GCC_except_table6366
- GCC_except_table6445
- GCC_except_table6511
- GCC_except_table6512
- GCC_except_table6513
- GCC_except_table6613
- GCC_except_table6662
- GCC_except_table6680
- GCC_except_table6923
- GCC_except_table6924
- GCC_except_table6925
- GCC_except_table6926
- GCC_except_table6927
- GCC_except_table7082
- GCC_except_table709
- GCC_except_table7202
- GCC_except_table7207
- GCC_except_table7265
- GCC_except_table7276
- GCC_except_table7339
- GCC_except_table7340
- GCC_except_table739
- GCC_except_table742
- GCC_except_table744
- GCC_except_table750
- GCC_except_table7549
- GCC_except_table7559
- GCC_except_table7636
- GCC_except_table7646
- GCC_except_table7929
- GCC_except_table7976
- GCC_except_table7977
- GCC_except_table8015
- GCC_except_table8071
- GCC_except_table8139
- GCC_except_table8278
- GCC_except_table8289
- GCC_except_table8408
- GCC_except_table8417
- GCC_except_table8429
- GCC_except_table8487
- GCC_except_table8498
- GCC_except_table8500
- GCC_except_table8502
- GCC_except_table8503
- GCC_except_table9024
- GCC_except_table9065
- GCC_except_table9070
- GCC_except_table9074
- GCC_except_table9076
- GCC_except_table9078
- GCC_except_table9080
- GCC_except_table909
- GCC_except_table9109
- GCC_except_table9247
- GCC_except_table9299
- GCC_except_table9503
- GCC_except_table9509
- GCC_except_table9514
- GCC_except_table9518
- GCC_except_table9520
- GCC_except_table9522
- GCC_except_table9524
- GCC_except_table9528
- GCC_except_table9530
- GCC_except_table9542
- GCC_except_table9546
- GCC_except_table9559
- GCC_except_table9572
- GCC_except_table9578
- GCC_except_table9586
- GCC_except_table9633
- GCC_except_table9639
- GCC_except_table9645
- GCC_except_table9683
- GCC_except_table9692
- GCC_except_table9790
- GCC_except_table9849
- GCC_except_table9878
- GCC_except_table9880
- GCC_except_table9886
- GCC_except_table9888
- GCC_except_table9890
- GCC_except_table9918
- GCC_except_table9919
- GCC_except_table9920
- GCC_except_table9922
- GCC_except_table994
- OBJC_IVAR_$_WFAppShortcutDataSource._cache
- OBJC_IVAR_$_WFAppShortcutDataSource._dataSource
- OBJC_IVAR_$_WFAppShortcutsPendingFetch._generation
- OBJC_IVAR_$_WFAppShortcutsPendingFetch._handlers
- OBJC_IVAR_$_WFAppShortcutsResultCache._cachedShortcutsByBundle
- OBJC_IVAR_$_WFAppShortcutsResultCache._generation
- OBJC_IVAR_$_WFAppShortcutsResultCache._memoryPressureSource
- OBJC_IVAR_$_WFAppShortcutsResultCache._pendingFetchesByCompositeKey
- OBJC_IVAR_$_WFAppShortcutsResultCache._queue
- OBJC_IVAR_$_WFExtractShortcutResult._sidecarTrigger
- OBJC_IVAR_$_WFUIPresenterLaunchAngelConnection._connectionLock
- OBJC_IVAR_$_WFUIPresenterLaunchAngelConnection._hostLock
- OBJC_IVAR_$_WFUIPresenterLaunchAngelConnection._stateLock
- _ACAccountTypeIdentifierAppleAccount
- _NSCurrentLocaleDidChangeNotification
- _OBJC_CLASS_$_WFAppShortcutDataSource
- _OBJC_CLASS_$_WFAppShortcutsPendingFetch
- _OBJC_CLASS_$_WFAppShortcutsResultCache
- _OBJC_CLASS_$_WFSwiftAppShortcutDataSource
- _OBJC_CLASS_$__TtC11WorkflowKit39WFAskLLMActionModelParameterDescription
- _OBJC_METACLASS_$_WFAppShortcutDataSource
- _OBJC_METACLASS_$_WFAppShortcutsPendingFetch
- _OBJC_METACLASS_$_WFAppShortcutsResultCache
- _OBJC_METACLASS_$_WFSwiftAppShortcutDataSource
- _OBJC_METACLASS_$__TtC11WorkflowKit39WFAskLLMActionModelParameterDescription
- _PROTOCOLS__TtC11WorkflowKit39WFAskLLMActionModelParameterDescription
- _WFAppShortcutDataSourceEnvironmentToOrganizationStyle
- __66-[WFUIPresenterLaunchAngelConnection prepareConnectionIfNecessary]_block_invoke
- __CATEGORY_LNAutoShortcutsProvider_$_WorkflowKit
- __CATEGORY_PROTOCOLS_LNAutoShortcutsProvider_$_WorkflowKit
- __DATA_WFSwiftAppShortcutDataSource
- __DATA__TtC11WorkflowKit39WFAskLLMActionModelParameterDescription
- __INSTANCE_METHODS_WFSwiftAppShortcutDataSource
- __INSTANCE_METHODS__TtC11WorkflowKit39WFAskLLMActionModelParameterDescription
- __IVARS_WFSwiftAppShortcutDataSource
- __IVARS__TtC11WorkflowKit39WFAskLLMActionModelParameterDescription
- __METACLASS_DATA_WFSwiftAppShortcutDataSource
- __METACLASS_DATA__TtC11WorkflowKit39WFAskLLMActionModelParameterDescription
- __OBJC_$_CLASS_METHODS_WFAppInFocusTrigger
- __OBJC_$_CLASS_METHODS_WFAppShortcutsResultCache
- __OBJC_$_CLASS_METHODS_WFTriggerInputVariable(WorkflowKit)
- __OBJC_$_CLASS_PROP_LIST_WFAppShortcutsResultCache
- __OBJC_$_INSTANCE_METHODS_WFAppInFocusTrigger(CoreDuetContext)
- __OBJC_$_INSTANCE_METHODS_WFAppShortcutDataSource
- __OBJC_$_INSTANCE_METHODS_WFAppShortcutsPendingFetch
- __OBJC_$_INSTANCE_METHODS_WFAppShortcutsResultCache
- __OBJC_$_INSTANCE_METHODS_WFTriggerInputVariable(WorkflowKit)
- __OBJC_$_INSTANCE_VARIABLES_WFAppShortcutDataSource
- __OBJC_$_INSTANCE_VARIABLES_WFAppShortcutsPendingFetch
- __OBJC_$_INSTANCE_VARIABLES_WFAppShortcutsResultCache
- __OBJC_$_PROP_LIST_WFAppShortcutDataSource
- __OBJC_$_PROP_LIST_WFAppShortcutsPendingFetch
- __OBJC_CLASS_RO_$_WFAppShortcutDataSource
- __OBJC_CLASS_RO_$_WFAppShortcutsPendingFetch
- __OBJC_CLASS_RO_$_WFAppShortcutsResultCache
- __OBJC_METACLASS_RO_$_WFAppShortcutDataSource
- __OBJC_METACLASS_RO_$_WFAppShortcutsPendingFetch
- __OBJC_METACLASS_RO_$_WFAppShortcutsResultCache
- __PROTOCOLS__TtC11WorkflowKit39WFAskLLMActionModelParameterDescription
- __PROTOCOL_INSTANCE_METHODS_WFSwiftStoredAppShortcutsProvider
- __PROTOCOL_METHOD_TYPES_WFSwiftStoredAppShortcutsProvider
- __PROTOCOL_WFSwiftStoredAppShortcutsProvider
- ___105-[WFAppShortcutsResultCache completePendingFetchForBundleIdentifier:localeIdentifier:appShortcuts:error:]_block_invoke
- ___33-[WFAppShortcutsResultCache init]_block_invoke
- ___40+[WFAppShortcutsResultCache sharedCache]_block_invoke
- ___42-[WFAppShortcutsResultCache invalidateAll]_block_invoke
- ___57-[WFAppShortcutsResultCache invalidateBundleIdentifiers:]_block_invoke
- ___66-[WFUIPresenterLaunchAngelConnection prepareConnectionIfNecessary]_block_invoke_2
- ___75-[WFLinkActionArrayParameterDefinition linkValueFromParameterState:action:]_block_invoke
- ___82-[WFAppIntentExecutionAction linkActionWithParameterStates:usingConnectionPolicy:]_block_invoke
- ___84-[WFAppShortcutsResultCache cachedAppShortcutsForBundleIdentifier:localeIdentifier:]_block_invoke
- ___99-[WFAppShortcutDataSource fetchAppShortcutsForBundleIdentifier:localeIdentifier:completionHandler:]_block_invoke
- ___99-[WFAppShortcutsResultCache attachOrStartPendingFetchForBundleIdentifier:localeIdentifier:handler:]_block_invoke
- ___99-[WFAppShortcutsResultCache attachOrStartPendingFetchForBundleIdentifier:localeIdentifier:handler:]_block_invoke_2
- ___99-[WFAppShortcutsResultCache attachOrStartPendingFetchForBundleIdentifier:localeIdentifier:handler:]_block_invoke_3
- ___block_descriptor_34_e32_B16?0"<FCActivityDescribing>"8l
- ___block_descriptor_40_e8_32s_e42_v16?0"<BSServiceConnectionConfiguring>"8l
- ___block_descriptor_40_e8_32s_e57_v16?0"BSServiceConnection<BSServiceConnectionContext>"8l
- ___block_descriptor_48_e8_32s40s_e20_"LNValue"24?08Q16l
- ___block_descriptor_48_e8_32s40s_e50_"LNProperty"24?0"LNActionParameterMetadata"8Q16l
- ___block_descriptor_56_e8_32s40s48r_e29_v16?0"NSMutableDictionary"8l
- ___block_descriptor_56_e8_32s40s48s_e29_v24?0"NSArray"8"NSError"16l
- ___block_descriptor_56_e8_32s40s48w_e5_v8?0l
- ___block_descriptor_64_e8_32s40s48bs56r_e5_v8?0l
- ___block_descriptor_88_e8_32s40s48s56s64s72s80r_e5_v8?0l
- ___copy_helper_block_e8_32s40s48s56s64s72s80r
- ___swift_memcpy256_8
- __dispatch_source_type_memorypressure
- _associated conformance So22WFLeaveLocationTriggerC11WorkflowKitE9LeaveTimeOSHACSQ
- _associated conformance So22WFLeaveLocationTriggerC11WorkflowKitE9LeaveTimeOs12CaseIterableAC8AllCasessAFP_Sl
- _associated conformance So23WFArriveLocationTriggerC11WorkflowKitE10ArriveTimeOSHACSQ
- _associated conformance So23WFArriveLocationTriggerC11WorkflowKitE10ArriveTimeOs12CaseIterableAC8AllCasessAFP_Sl
- _flat unique So33WFSwiftStoredAppShortcutsProvider_p
- _objc_msgSend$_queue_invalidateAll
- _objc_msgSend$_queue_invalidateBundleIdentifiers:
- _objc_msgSend$attachOrStartPendingFetchForBundleIdentifier:localeIdentifier:handler:
- _objc_msgSend$cachedAppShortcutsForBundleIdentifier:localeIdentifier:
- _objc_msgSend$cleanUpWithReason:
- _objc_msgSend$completePendingFetchForBundleIdentifier:localeIdentifier:appShortcuts:error:
- _objc_msgSend$connectionInterrupted
- _objc_msgSend$connectionWithUserIdentity:error:
- _objc_msgSend$fetchAppShortcutForBundleIdentifiers:localeIdentifier:error:
- _objc_msgSend$fetchAppShortcutsForBundleIdentifier:localeIdentifier:completionHandler:
- _objc_msgSend$generation
- _objc_msgSend$handlers
- _objc_msgSend$initWithAppShortcutsDenyListEnvironment:environment:cache:
- _objc_msgSend$initWithAppShortcutsProvider:denyListEnvironment:organizationStyle:
- _objc_msgSend$initWithGeneration:handler:
- _objc_msgSend$invalidateAll
- _objc_msgSend$invalidateBundleIdentifiers:
- _objc_msgSend$linkActionWithParameterStates:usingConnectionPolicy:
- _objc_msgSend$linkActionWithSerializedParametersUsingConnectionPolicy:
- _objc_msgSend$linkValueFromParameterState:action:
- _objc_msgSend$mappingModelFromBundles:forSourceModel:destinationModel:
- _objc_msgSend$refreshTriggerWithWorkflowID:triggerUUID:urlWrapper:completion:
- _objc_msgSend$setSidecarTrigger:
- _objc_msgSend$sharedCache
- _objc_msgSend$sidecarTrigger
- _objc_msgSend$valueForParameterData:withParameterState:
- _symbolic Say_____G 10ContentKit21WFGenerativeModelNameO
- _symbolic Say_____G 7ToolKit0A14VisibilityFlagV
- _symbolic Say_____G 7ToolKit0A4FlagV
- _symbolic Say_____G 7ToolKit19ParameterDefinitionV0C5FlagsV
- _symbolic Say_____G So22WFLeaveLocationTriggerC11WorkflowKitE9LeaveTimeO
- _symbolic Say_____G So23WFArriveLocationTriggerC11WorkflowKitE10ArriveTimeO
- _symbolic _____ 11WorkflowKit39WFAskLLMActionModelParameterDescriptionC
- _symbolic _____ So22WFLeaveLocationTriggerC11WorkflowKitE9LeaveTimeO
- _symbolic _____ So23WFArriveLocationTriggerC11WorkflowKitE10ArriveTimeO
- _symbolic _____Sg 7ToolKit19ParameterDefinitionV0A8MetadataV
- _symbolic _____Sg 7ToolKit19ParameterDefinitionV15BooleanMetadataV
- _symbolic _____Sg_ABt 10Foundation3URLV
- sharedCache.onceToken
- sharedCache.sharedCache
CStrings:
+ "%s Action \"%@\" is being rate limited because it passed the threshold of %li runs. Delaying execution for %f seconds."
+ "%s Denying Writing Tools availability due to regional check"
+ "%s Failed to create inferred mapping model, bailing out"
+ "%s Failed to serialize one-time-activity map, keeping existing data: %{public}@"
+ "%s Find Message routed to %{public}s"
+ "%s For MessageEntity querying, we also fetch %@ in order to do pre-hydration sorting"
+ "%s Ignoring a duplicate dialog completion, this request already completed"
+ "%s Invalidating launch angel connection because 'the connection class is deallocating'"
+ "%s Messages MessageEntity sorting path. We proceed by first sorting, optionally slicing, then hydrating"
+ "%s Messages pre-hydration sorting and slicing limit is %ld"
+ "%s No default presenter for ToolKit snippet environment request (expected on watchOS); replying with no environment"
+ "%s No default presenter for ToolKit snippet size request (expected on watchOS); replying with no size"
+ "%s Not sorting Message so we grab at most %ld entities and silently drop the rest"
+ "%s NoteEntity coercion returning nil because title and body were nil"
+ "%s NoteEntity content LNProperty was nil, which is unexpected"
+ "%s Recovered file representation for INFile with a fileURL by inferring type/filename from disk after direct construction failed"
+ "%s Streamed %ld results, kept %ld before hydration"
+ "%s Unable resolve spotlight sort key for Message entity with sortDescriptor %@"
+ "+[WFWritingToolsAvailabilityResource isSystemWritingToolsAvailable]"
+ "-[INFile(Workflow) wf_fileRepresentation]"
+ "-[WFCloudKitSyncToken markActivityCompleted:]"
+ "-[WFDialogTransformer getEnvironmentForLinkViewSnippetWithDialog:completion:]"
+ "-[WFDialogTransformer getPreferredSizeForLinkViewSnippetWithDialog:completion:]"
+ "-[WFLinkActionPersonParameterDefinition linkValueFromParameterState:action:forUseCase:]"
+ "-[WFLinkContentItemFilterAction runSpotlightQuery:sortingAndSlicingBeforeHydrationWithSortKey:random:ascending:instanceKey:]"
+ "-[WFLinkContentItemFilterAction runSpotlightQuery:sortingAndSlicingBeforeHydrationWithSortKey:random:ascending:instanceKey:]_block_invoke"
+ "-[WFUIPresenterLaunchAngelConnection _cleanUpOnQueueWithReason:]"
+ "-[WFUIPresenterLaunchAngelConnection _handleConnectionInterruption]"
+ "-[WFUIPresenterLaunchAngelConnection _handleConnectionInvalidation:]"
+ "-[WFUIPresenterLaunchAngelConnection dealloc]"
+ "-[WFUIPresenterLaunchAngelConnection makeConfiguredConnectionForHost:]_block_invoke_2"
+ "/%@"
+ "/System/Library/PrivateFrameworks/WebContentRestrictions.framework/Contents/MacOS/WebContentRestrictions"
+ "Alarms & Timers"
+ "Alarms & Timers (WFVolumeSetting)"
+ "Alerts & System Sounds"
+ "Alerts & System Sounds (WFVolumeSetting)"
+ "Already observing sunrise/sunset changes"
+ "Base WFVariable is abstract and cannot be exported"
+ "Class getWCRBrowserEngineClientClass(void)_block_invoke"
+ "Coercion aggrandizement applied to a variable that does not support coercion"
+ "Configure %@ to enable this automation."
+ "Configure this automation."
+ "Couldn't build record to recover triggers for %{public}s; skipping"
+ "ExternalTriggers.sqlite"
+ "Failed to apply recovered unified triggers for %{public}s: %{public}@"
+ "Failed to convert enumeration case '%s' into a WFLinkDynamicOptionSubstitutableState - missing LNEnumMetadata for parameter: %@"
+ "Failed to convert enumeration case '%s' into a WFNSUnitSubstitutableState - unrecognized unit symbol for parameter: %@"
+ "Failed to migrate workflow %s: %@"
+ "Failed to observe sunrise/sunset changes: _CDContextualChangeRegistration creation failed"
+ "Failed to observe sunrise/sunset changes: no keypath for the sunrise/sunset data dictionary"
+ "Failed to remove migrated workflow %s: %@"
+ "Found pending trigger %{public}s in local workflow, AND in remote record"
+ "Invalid variable"
+ "Malformed conditional: no action follows %@ in groupedConditionals"
+ "MaxDelay"
+ "Merging %ld never-synced automation trigger(s) into the incoming record instead of conflicting"
+ "Migrate external trigger "
+ "Multiplier"
+ "NSURL * _Nonnull WFShortcutsExternalTriggerStoreURL(void)"
+ "No enumeration metadata found for type '"
+ "Observing sunrise/sunset changes, registration: %{public}@"
+ "OmittedAppBundleIdentifiers"
+ "Only run when the email subject contains this text."
+ "Only run when the message contains this text."
+ "Only run when the notification message contains this text."
+ "Only run when the notification subtitle contains this text."
+ "Only run when the notification title contains this text."
+ "Recovered %ld unified automation trigger(s) for workflow %{public}s"
+ "Show the model’s response and make additional requests before the final response is passed to the next action.\n\n**Private Cloud Compute Models**\nUse large server-based models on Private Cloud Compute to handle complex requests while protecting your privacy.\n\n**On-Device Model**\nUse the on-device model to handle simple requests without the need for a network connection.\n\nImage analysis is supported by the Private Cloud Compute and Extension models, however image generation is not supported."
+ "Sunrise/sunset data changed; updating trigger registration"
+ "The volume setting to change: Media, Ringtone, Alarms & Timers, or Alerts & System Sounds."
+ "The volume setting to change: Media, Ringtone, Alarms & Timers, or Alerts & System Sounds. (WFVolumeSetting)"
+ "ThrottleCount"
+ "Time Range"
+ "Trigger-input variable missing its producing trigger"
+ "Trigger-input variable references a trigger that is not present in the workflow"
+ "Unexpected trigger plist format recovering triggers for %{public}s; skipping"
+ "Variable Class"
+ "Visual Intelligence Icon - Legacy"
+ "WCRBrowserEngineClient"
+ "WFArriveLocation,WFArriveStartTime,WFArriveEndTime"
+ "WFArriveTimeRange"
+ "WFLeaveLocation,WFLeaveStartTime,WFLeaveEndTime"
+ "WFLeaveTimeRange"
+ "WFMailGLPSearchClient.scan returned a full page (%ld/%ld); results may be capped"
+ "WFScreenTimeHelper.m"
+ "WFShouldHideCompositionPane"
+ "WFUserFocusActivityTrigger."
+ "WFWhatsNewLastPresentationOSVersion"
+ "When I arrive at ${WFArriveLocation}"
+ "When I arrive at ${WFArriveLocation} between ${WFArriveStartTime} and ${WFArriveEndTime}"
+ "When I leave ${WFLeaveLocation}"
+ "When I leave ${WFLeaveLocation} between ${WFLeaveStartTime} and ${WFLeaveEndTime}"
+ "[%s] No enumeration metadata found for type '%s' in bundle '%s' — falling back to raw enum case '%s'"
+ "[%s] Recovered enum metadata for type '%s' under fallback bundle '%s' (TypedValue bundle '%s' had no registered metadata)"
+ "_kMDItemSnippet"
+ "alarm.waves.left.and.right.fill"
+ "arrow.down.forward.square.fill"
+ "battery.100percent"
+ "battery.25percent"
+ "battery.50percent"
+ "battery.5percent"
+ "battery.75percent"
+ "com.apple.shortcuts.WFUIPresenterLaunchAngelConnection.isolation"
+ "configuration changed"
+ "currentPersonaFilename: UserManagement is available but current persona id is nil"
+ "eventName"
+ "failed to parse trigger uniqueID %{public}s"
+ "https://support.apple.com/127901?cid=mc-ols-icloud-article_127901-macos-62020270"
+ "initial registration"
+ "recover unified triggers after upgrade"
+ "softlink:r:path:/System/Library/PrivateFrameworks/WebContentRestrictions.framework/WebContentRestrictions"
+ "sunrise/sunset data changed"
+ "trigger-watcher:sunrise-sunset"
+ "void *WebContentRestrictionsLibrary(void)"
+ "wallet_transaction"
+ "“When %@ is turned on or off”"
+ "“When this device joins Home network”"
- "%s Action \"%@\" is being rate limited because it passed the threshold of %li runs. Delaying execution for %li seconds."
- "%s Could not find explicit mapping model, trying to construct inferred one"
- "%s Failed to create mapping model, bailing out"
- "%s Find Message routed to %{public}s (rdar://179176856)"
- "**Extensions**\nApps installed on your device can expose models to Shortcuts, so you can tap into their broad world knowledge and domain expertise. You can enable extensions in Settings > Apple Intelligence & Siri."
- "**Private Cloud Compute Models**\nUse large server-based models on Private Cloud Compute to handle complex requests while protecting your privacy.\n\n**On-Device Model**\nUse the on-device model to handle simple requests without the need for a network connection."
- "-[WFLinkActionPersonParameterDefinition linkValueFromParameterState:action:]"
- "-[WFUIPresenterLaunchAngelConnection cleanUpWithReason:]"
- "-[WFUIPresenterLaunchAngelConnection prepareConnectionIfNecessary]_block_invoke"
- "-[WFUIPresenterLaunchAngelConnection prepareConnectionIfNecessary]_block_invoke_2"
- "At Any Time"
- "Attempted to export a WFConditionalAction with else-if branches, but the else_if feature flag is turned off!"
- "Between"
- "Fetch timed out"
- "Image analysis is supported by the Private Cloud Compute and Extension models, however image generation is not supported."
- "Show the model’s response and make additional requests before the final response is passed to the next action."
- "The volume setting to change, either Media or Ringtone."
- "The volume setting to change, either Media or Ringtone. (WFVolumeSetting)"
- "Trigger has no associated workflow"
- "WFAppShortcutsResultCache"
- "WFArriveLocation,WFArriveTime(any)"
- "WFArriveLocation,WFArriveTime(specific),WFArriveStartTime,WFArriveEndTime"
- "WFArriveTime"
- "WFLeaveLocation,WFLeaveTime(any)"
- "WFLeaveLocation,WFLeaveTime(specific),WFLeaveStartTime,WFLeaveEndTime"
- "WFLeaveTime"
- "WFMailGLPSearchClient.scan returned a full page (%ld/%ld); results may be capped (rdar://179176856)"
- "When I arrive at ${WFArriveLocation} ${WFArriveTime}"
- "When I arrive at ${WFArriveLocation} ${WFArriveTime} ${WFArriveStartTime} and ${WFArriveEndTime}"
- "When I leave ${WFLeaveLocation} ${WFLeaveTime}"
- "When I leave ${WFLeaveLocation} ${WFLeaveTime} ${WFLeaveStartTime} and ${WFLeaveEndTime}"
- "WorkflowKit.WFAskLLMActionModelParameterDescription"
- "any"
- "com.apple.WorkflowKit"
- "com.apple.WorkflowKit.WFAppShortcutsResultCache"
- "com.apple.sleep.sleep-mode"
- "else_if"
- "failed to parse trigger filesystem node ID %{public}s"
- "https://support.apple.com/guide/icloud/mmfdc8a6b022"
- "the connection class is deallocating"
- "wallet.bifold.fill"
- "|%@"
- "“When I get an email from Johann”"
- "“When this device joins the Home network”"
```
