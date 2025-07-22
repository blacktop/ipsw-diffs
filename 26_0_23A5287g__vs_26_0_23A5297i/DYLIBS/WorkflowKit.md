## WorkflowKit

> `/System/Library/PrivateFrameworks/WorkflowKit.framework/WorkflowKit`

```diff

-4027.2.1.0.0
-  __TEXT.__text: 0x6c00e8
-  __TEXT.__auth_stubs: 0x7840
-  __TEXT.__objc_methlist: 0x2eb04
-  __TEXT.__const: 0x11060
+4030.0.2.0.0
+  __TEXT.__text: 0x6c4f34
+  __TEXT.__auth_stubs: 0x7880
+  __TEXT.__objc_methlist: 0x2ec2c
+  __TEXT.__const: 0x11140
   __TEXT.__dlopen_cstrs: 0xf25
-  __TEXT.__cstring: 0x81cf6
-  __TEXT.__constg_swiftt: 0x5664
-  __TEXT.__swift5_typeref: 0x72bc
+  __TEXT.__cstring: 0x820cc
+  __TEXT.__swift5_typeref: 0x7378
+  __TEXT.__constg_swiftt: 0x56ec
+  __TEXT.__swift5_fieldmd: 0x3bb4
   __TEXT.__swift5_builtin: 0x438
-  __TEXT.__swift5_reflstr: 0x3208
-  __TEXT.__swift5_fieldmd: 0x3b88
+  __TEXT.__swift5_reflstr: 0x3218
   __TEXT.__swift5_assocty: 0x1338
-  __TEXT.__swift5_proto: 0xcd4
-  __TEXT.__swift5_types: 0x5ac
+  __TEXT.__swift5_proto: 0xcdc
+  __TEXT.__swift5_types: 0x5b4
   __TEXT.__swift_as_entry: 0x76c
   __TEXT.__swift_as_ret: 0x914
-  __TEXT.__swift5_capture: 0x1604
-  __TEXT.__oslogstring: 0x17f8b
+  __TEXT.__swift5_capture: 0x1628
+  __TEXT.__oslogstring: 0x1831d
   __TEXT.__swift5_protos: 0xb4
   __TEXT.__swift5_mpenum: 0x88
-  __TEXT.__gcc_except_tab: 0x4a68
+  __TEXT.__gcc_except_tab: 0x4a50
   __TEXT.__ustring: 0x39de
-  __TEXT.__unwind_info: 0x13d00
-  __TEXT.__eh_frame: 0x13d04
-  __TEXT.__objc_classname: 0x7d82
-  __TEXT.__objc_methname: 0x57d19
+  __TEXT.__unwind_info: 0x13df0
+  __TEXT.__eh_frame: 0x13dac
+  __TEXT.__objc_classname: 0x7da7
+  __TEXT.__objc_methname: 0x57efc
   __TEXT.__objc_methtype: 0x968f
   __TEXT.__objc_stubs: 0x35520
-  __DATA_CONST.__got: 0x4ab8
-  __DATA_CONST.__const: 0xdd30
-  __DATA_CONST.__objc_classlist: 0x2110
+  __DATA_CONST.__got: 0x4b00
+  __DATA_CONST.__const: 0xdd60
+  __DATA_CONST.__objc_classlist: 0x2128
   __DATA_CONST.__objc_catlist: 0x3e8
   __DATA_CONST.__objc_protolist: 0x588
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x12068
+  __DATA_CONST.__objc_selrefs: 0x120b0
   __DATA_CONST.__objc_protorefs: 0x1f0
-  __DATA_CONST.__objc_superrefs: 0x12e0
+  __DATA_CONST.__objc_superrefs: 0x12d8
   __DATA_CONST.__objc_arraydata: 0x14a0
-  __AUTH_CONST.__auth_got: 0x3c38
-  __AUTH_CONST.__const: 0x291e0
-  __AUTH_CONST.__cfstring: 0x28b20
-  __AUTH_CONST.__objc_const: 0x54468
+  __AUTH_CONST.__auth_got: 0x3c58
+  __AUTH_CONST.__const: 0x29290
+  __AUTH_CONST.__cfstring: 0x28ae0
+  __AUTH_CONST.__objc_const: 0x54640
   __AUTH_CONST.__objc_dictobj: 0x488
   __AUTH_CONST.__objc_intobj: 0xed0
   __AUTH_CONST.__objc_arrayobj: 0x978
   __AUTH_CONST.__objc_doubleobj: 0x20
-  __AUTH.__objc_data: 0xe840
-  __AUTH.__data: 0x3b20
-  __DATA.__objc_ivar: 0x2688
-  __DATA.__data: 0x8c70
-  __DATA.__bss: 0x16638
+  __AUTH.__objc_data: 0xe9b0
+  __AUTH.__data: 0x3b80
+  __DATA.__objc_ivar: 0x2690
+  __DATA.__data: 0x8d80
+  __DATA.__bss: 0x16738
   __DATA.__common: 0x60
   __DATA_DIRTY.__objc_data: 0x8790
   __DATA_DIRTY.__data: 0xc78

   - /System/Library/PrivateFrameworks/AACCore.framework/AACCore
   - /System/Library/PrivateFrameworks/AppIntentsServices.framework/AppIntentsServices
   - /System/Library/PrivateFrameworks/AppProtection.framework/AppProtection
+  - /System/Library/PrivateFrameworks/AssistantServices.framework/AssistantServices
   - /System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard
   - /System/Library/PrivateFrameworks/BiomeLibrary.framework/BiomeLibrary
   - /System/Library/PrivateFrameworks/BiomeStreams.framework/BiomeStreams

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 7082EDCF-B62F-3BEF-9579-A6062759D6D8
-  Functions: 30090
-  Symbols:   64908
-  CStrings:  36391
+  UUID: C1867666-ADC0-35F5-BC1A-637EE99E6FBA
+  Functions: 30174
+  Symbols:   64962
+  CStrings:  36439
 
Symbols:
+ +[WFLinkCalculateAppUsageIntentAction outputIsExemptFromTaintTrackingInheritance]
+ +[WFLinkIPDataFindSportsEventsAction outputIsExemptFromTaintTrackingInheritance]
+ -[WFAction _finishRunningWithError:]
+ -[WFDatabase coreDataLibrary]
+ -[WFDatabase lastLoadedLibrarySyncHash]
+ -[WFDatabase removePermissionsWithoutAssociatedShortcuts]
+ -[WFDatabase saveLibraryToDatabase]
+ -[WFDatabase setLastLoadedLibrarySyncHash:]
+ -[WFDatabase(Shortcuts) hasWorkflowWithID:]
+ -[WFDynamicEnumerationParameter completionQueue]
+ -[WFDynamicEnumerationParameter initWithDefinition:]
+ -[WFDynamicEnumerationParameter setCompletionQueue:]
+ -[WFLinkCalculateAppUsageIntentAction getContentDestinationWithCompletionHandler:]
+ -[WFLinkCalculateAppUsageIntentAction icon]
+ -[WFLinkIPDataFindSportsEventsAction getContentDestinationWithCompletionHandler:]
+ -[WFLinkIPDataFindSportsEventsAction outputDisclosureLevel]
+ -[WFLinkVisualIntelligenceCameraAction requiredResources]
+ -[WFLinkWritingToolsAction getContentDestinationWithCompletionHandler:]
+ -[WFParameter preferredTypes]
+ -[WFResourceManager makeAccessResourcesAvailableWithUserInterface:completionQueue:completionHandler:]
+ -[WFWorkflowCreationOptions folderIdentifier]
+ -[WFWorkflowCreationOptions setFolderIdentifier:]
+ GCC_except_table10000
+ GCC_except_table10004
+ GCC_except_table10007
+ GCC_except_table10010
+ GCC_except_table10012
+ GCC_except_table10017
+ GCC_except_table10028
+ GCC_except_table10183
+ GCC_except_table10203
+ GCC_except_table10206
+ GCC_except_table10247
+ GCC_except_table10415
+ GCC_except_table10421
+ GCC_except_table10440
+ GCC_except_table10594
+ GCC_except_table10628
+ GCC_except_table10702
+ GCC_except_table10704
+ GCC_except_table10706
+ GCC_except_table10734
+ GCC_except_table10739
+ GCC_except_table10779
+ GCC_except_table10782
+ GCC_except_table10785
+ GCC_except_table10788
+ GCC_except_table10977
+ GCC_except_table11071
+ GCC_except_table11088
+ GCC_except_table11110
+ GCC_except_table11152
+ GCC_except_table11510
+ GCC_except_table11536
+ GCC_except_table11539
+ GCC_except_table11555
+ GCC_except_table11627
+ GCC_except_table11914
+ GCC_except_table11917
+ GCC_except_table11922
+ GCC_except_table11929
+ GCC_except_table11967
+ GCC_except_table11970
+ GCC_except_table11992
+ GCC_except_table11993
+ GCC_except_table12006
+ GCC_except_table12007
+ GCC_except_table12008
+ GCC_except_table12010
+ GCC_except_table12108
+ GCC_except_table1227
+ GCC_except_table12304
+ GCC_except_table12320
+ GCC_except_table12499
+ GCC_except_table12514
+ GCC_except_table12520
+ GCC_except_table12527
+ GCC_except_table12621
+ GCC_except_table12634
+ GCC_except_table12642
+ GCC_except_table12683
+ GCC_except_table12720
+ GCC_except_table12734
+ GCC_except_table12736
+ GCC_except_table12738
+ GCC_except_table12820
+ GCC_except_table12836
+ GCC_except_table12942
+ GCC_except_table12983
+ GCC_except_table1300
+ GCC_except_table13038
+ GCC_except_table13067
+ GCC_except_table13121
+ GCC_except_table13132
+ GCC_except_table13176
+ GCC_except_table13178
+ GCC_except_table13496
+ GCC_except_table13529
+ GCC_except_table13646
+ GCC_except_table13675
+ GCC_except_table13681
+ GCC_except_table13728
+ GCC_except_table13822
+ GCC_except_table13835
+ GCC_except_table13838
+ GCC_except_table13850
+ GCC_except_table13857
+ GCC_except_table13858
+ GCC_except_table13859
+ GCC_except_table13868
+ GCC_except_table13879
+ GCC_except_table14005
+ GCC_except_table1405
+ GCC_except_table14080
+ GCC_except_table14084
+ GCC_except_table1410
+ GCC_except_table14275
+ GCC_except_table14343
+ GCC_except_table14588
+ GCC_except_table14618
+ GCC_except_table14734
+ GCC_except_table14905
+ GCC_except_table14910
+ GCC_except_table14919
+ GCC_except_table14922
+ GCC_except_table15039
+ GCC_except_table15062
+ GCC_except_table15073
+ GCC_except_table15076
+ GCC_except_table15391
+ GCC_except_table15431
+ GCC_except_table15442
+ GCC_except_table15456
+ GCC_except_table15459
+ GCC_except_table15653
+ GCC_except_table15780
+ GCC_except_table1735
+ GCC_except_table1748
+ GCC_except_table1753
+ GCC_except_table1755
+ GCC_except_table1757
+ GCC_except_table1994
+ GCC_except_table2070
+ GCC_except_table2151
+ GCC_except_table2161
+ GCC_except_table2332
+ GCC_except_table2340
+ GCC_except_table2370
+ GCC_except_table246
+ GCC_except_table2523
+ GCC_except_table255
+ GCC_except_table2550
+ GCC_except_table2618
+ GCC_except_table2655
+ GCC_except_table2774
+ GCC_except_table2788
+ GCC_except_table2880
+ GCC_except_table2933
+ GCC_except_table2950
+ GCC_except_table2956
+ GCC_except_table3168
+ GCC_except_table3190
+ GCC_except_table3191
+ GCC_except_table3199
+ GCC_except_table3200
+ GCC_except_table3201
+ GCC_except_table3225
+ GCC_except_table3229
+ GCC_except_table3253
+ GCC_except_table3285
+ GCC_except_table3301
+ GCC_except_table3305
+ GCC_except_table3364
+ GCC_except_table3375
+ GCC_except_table3380
+ GCC_except_table349
+ GCC_except_table352
+ GCC_except_table3566
+ GCC_except_table3570
+ GCC_except_table3572
+ GCC_except_table3576
+ GCC_except_table3577
+ GCC_except_table3881
+ GCC_except_table3885
+ GCC_except_table4250
+ GCC_except_table4251
+ GCC_except_table4370
+ GCC_except_table4472
+ GCC_except_table4485
+ GCC_except_table4504
+ GCC_except_table4512
+ GCC_except_table4687
+ GCC_except_table4868
+ GCC_except_table4874
+ GCC_except_table4880
+ GCC_except_table4970
+ GCC_except_table4984
+ GCC_except_table5102
+ GCC_except_table5129
+ GCC_except_table5133
+ GCC_except_table5173
+ GCC_except_table5231
+ GCC_except_table5239
+ GCC_except_table5262
+ GCC_except_table53
+ GCC_except_table5302
+ GCC_except_table535
+ GCC_except_table5358
+ GCC_except_table5363
+ GCC_except_table5365
+ GCC_except_table5491
+ GCC_except_table5497
+ GCC_except_table5513
+ GCC_except_table5884
+ GCC_except_table6028
+ GCC_except_table6087
+ GCC_except_table6097
+ GCC_except_table6194
+ GCC_except_table626
+ GCC_except_table6324
+ GCC_except_table6325
+ GCC_except_table6326
+ GCC_except_table6427
+ GCC_except_table6474
+ GCC_except_table6492
+ GCC_except_table6521
+ GCC_except_table6859
+ GCC_except_table6922
+ GCC_except_table6923
+ GCC_except_table6928
+ GCC_except_table6929
+ GCC_except_table6932
+ GCC_except_table6938
+ GCC_except_table6943
+ GCC_except_table6948
+ GCC_except_table6949
+ GCC_except_table6989
+ GCC_except_table6994
+ GCC_except_table7052
+ GCC_except_table7063
+ GCC_except_table7333
+ GCC_except_table7343
+ GCC_except_table7417
+ GCC_except_table7495
+ GCC_except_table7796
+ GCC_except_table7839
+ GCC_except_table7886
+ GCC_except_table7887
+ GCC_except_table7953
+ GCC_except_table80
+ GCC_except_table8083
+ GCC_except_table8221
+ GCC_except_table8226
+ GCC_except_table8237
+ GCC_except_table84
+ GCC_except_table8417
+ GCC_except_table8424
+ GCC_except_table8435
+ GCC_except_table845
+ GCC_except_table9024
+ GCC_except_table9093
+ GCC_except_table9099
+ GCC_except_table9102
+ GCC_except_table9105
+ GCC_except_table9109
+ GCC_except_table9143
+ GCC_except_table918
+ GCC_except_table9197
+ GCC_except_table927
+ GCC_except_table9290
+ GCC_except_table9339
+ GCC_except_table9585
+ GCC_except_table9589
+ GCC_except_table9591
+ GCC_except_table9597
+ GCC_except_table9599
+ GCC_except_table9625
+ GCC_except_table9646
+ GCC_except_table9660
+ GCC_except_table9669
+ GCC_except_table9712
+ GCC_except_table9718
+ GCC_except_table9724
+ GCC_except_table9994
+ GCC_except_table9996
+ GCC_except_table9998
+ _AssistantServicesLibraryCore.frameworkLibrary.54454
+ _ContactsLibrary.53981
+ _ContactsLibrary.67208
+ _ContactsLibraryCore.frameworkLibrary.32208
+ _ContactsLibraryCore.frameworkLibrary.47980
+ _ContactsLibraryCore.frameworkLibrary.54031
+ _ContactsLibraryCore.frameworkLibrary.61746
+ _ContactsLibraryCore.frameworkLibrary.66106
+ _ContactsLibraryCore.frameworkLibrary.67216
+ _CoreLocationLibraryCore.frameworkLibrary.41580
+ _CoreLocationLibraryCore.frameworkLibrary.48002
+ _CoreLocationLibraryCore.frameworkLibrary.59274
+ _CoreLocationLibraryCore.frameworkLibrary.59940
+ _CoreLocationLibraryCore.frameworkLibrary.62105
+ _CoreLocationLibraryCore.frameworkLibrary.63891
+ _CoreLocationLibraryCore.frameworkLibrary.66067
+ _HFTriggerActionSetsBuilderFunction.35670
+ _HFTriggerActionSetsBuilderFunction.38917
+ _HMCharacteristicMetadataFormatBoolFunction.2170
+ _HMCharacteristicMetadataFormatBoolFunction.28270
+ _HMCharacteristicMetadataFormatFloatFunction.2150
+ _HMCharacteristicMetadataFormatIntFunction.2157
+ _HMCharacteristicMetadataFormatIntFunction.28381
+ _HMCharacteristicMetadataFormatStringFunction.2163
+ _HMCharacteristicMetadataFormatUInt16Function.2138
+ _HMCharacteristicMetadataFormatUInt32Function.2131
+ _HMCharacteristicMetadataFormatUInt64Function.2123
+ _HMCharacteristicMetadataFormatUInt8Function.2144
+ _HMCharacteristicMetadataFormatUInt8Function.28388
+ _HomeKitLibrary.sLib.1584
+ _HomeKitLibrary.sLib.2118
+ _HomeKitLibrary.sLib.28250
+ _HomeKitLibrary.sLib.35697
+ _HomeKitLibrary.sLib.36536
+ _HomeKitLibrary.sLib.38928
+ _HomeKitLibrary.sLib.56627
+ _HomeKitLibrary.sOnce.1579
+ _HomeKitLibrary.sOnce.2117
+ _HomeKitLibrary.sOnce.28249
+ _HomeKitLibrary.sOnce.35695
+ _HomeKitLibrary.sOnce.36529
+ _HomeKitLibrary.sOnce.38923
+ _HomeKitLibrary.sOnce.56620
+ _HomeLibrary.sLib.28395
+ _HomeLibrary.sLib.35674
+ _HomeLibrary.sLib.38921
+ _HomeLibrary.sLib.4481
+ _HomeLibrary.sOnce.28391
+ _HomeLibrary.sOnce.35666
+ _HomeLibrary.sOnce.38913
+ _HomeLibrary.sOnce.4476
+ _LNSystemEntityProtocolIdentifierURLRepresentable
+ _MediaPlayerLibrary.37081
+ _MediaPlayerLibrary.53758
+ _MediaPlayerLibraryCore.frameworkLibrary.37091
+ _MediaPlayerLibraryCore.frameworkLibrary.53765
+ _OBJC_CLASS_$_AFSystemAssistantExperienceStatusManager
+ _OBJC_CLASS_$_WFDatabaseFetchedRecordResult
+ _OBJC_CLASS_$_WFLinkCalculateAppUsageIntentAction
+ _OBJC_CLASS_$__TtC11WorkflowKit46WFVisualIntelligenceCameraAvailabilityResource
+ _OBJC_IVAR_$_WFDatabase._lastLoadedLibrarySyncHash
+ _OBJC_IVAR_$_WFDynamicEnumerationParameter._completionQueue
+ _OBJC_IVAR_$_WFParameter._preferredTypes
+ _OBJC_IVAR_$_WFWorkflowCreationOptions._folderIdentifier
+ _OBJC_METACLASS_$_WFDatabaseFetchedRecordResult
+ _OBJC_METACLASS_$_WFLinkCalculateAppUsageIntentAction
+ _OBJC_METACLASS_$__TtC11WorkflowKit46WFVisualIntelligenceCameraAvailabilityResource
+ _PhotosLibraryCore.frameworkLibrary.1494
+ _ReminderKitLibraryCore.frameworkLibrary.25664
+ _RunningBoardServicesLibrary.27455
+ _RunningBoardServicesLibraryCore.frameworkLibrary.27460
+ _SAObjectsLibrary.sLib.70721
+ _SAObjectsLibrary.sOnce.70719
+ _UIKitLibrary.sLib.16271
+ _UIKitLibrary.sLib.22973
+ _UIKitLibrary.sLib.28662
+ _UIKitLibrary.sLib.29259
+ _UIKitLibrary.sLib.42533
+ _UIKitLibrary.sLib.49485
+ _UIKitLibrary.sLib.58987
+ _UIKitLibrary.sLib.61460
+ _UIKitLibrary.sLib.64558
+ _UIKitLibrary.sOnce.16269
+ _UIKitLibrary.sOnce.22966
+ _UIKitLibrary.sOnce.28655
+ _UIKitLibrary.sOnce.29256
+ _UIKitLibrary.sOnce.42531
+ _UIKitLibrary.sOnce.49475
+ _UIKitLibrary.sOnce.58982
+ _UIKitLibrary.sOnce.61450
+ _UIKitLibrary.sOnce.64548
+ _UIKitLibraryCore.frameworkLibrary.41837
+ _UIPasteboardFunction.42546
+ _UIPasteboardFunction.49480
+ _UIPasteboardFunction.61455
+ _UIPasteboardFunction.64553
+ _WFActionGreenTeaContentDestinationMayLeaveDevice.onceToken.1167
+ _WFDyldBulkImageLoadCallback.25088
+ _WFEnforceClass.10314
+ _WFEnforceClass.1039
+ _WFEnforceClass.13281
+ _WFEnforceClass.13489
+ _WFEnforceClass.1477
+ _WFEnforceClass.15630
+ _WFEnforceClass.16684
+ _WFEnforceClass.16805
+ _WFEnforceClass.17228
+ _WFEnforceClass.17864
+ _WFEnforceClass.1926
+ _WFEnforceClass.2095
+ _WFEnforceClass.21346
+ _WFEnforceClass.21588
+ _WFEnforceClass.22495
+ _WFEnforceClass.23384
+ _WFEnforceClass.23450
+ _WFEnforceClass.25059
+ _WFEnforceClass.25172
+ _WFEnforceClass.29086
+ _WFEnforceClass.29370
+ _WFEnforceClass.29456
+ _WFEnforceClass.29616
+ _WFEnforceClass.29805
+ _WFEnforceClass.30053
+ _WFEnforceClass.30799
+ _WFEnforceClass.31810
+ _WFEnforceClass.32356
+ _WFEnforceClass.3417
+ _WFEnforceClass.35845
+ _WFEnforceClass.36871
+ _WFEnforceClass.37354
+ _WFEnforceClass.3980
+ _WFEnforceClass.40806
+ _WFEnforceClass.42374
+ _WFEnforceClass.43859
+ _WFEnforceClass.4523
+ _WFEnforceClass.46712
+ _WFEnforceClass.47137
+ _WFEnforceClass.47281
+ _WFEnforceClass.49377
+ _WFEnforceClass.50825
+ _WFEnforceClass.51311
+ _WFEnforceClass.57983
+ _WFEnforceClass.58883
+ _WFEnforceClass.59149
+ _WFEnforceClass.61258
+ _WFEnforceClass.6175
+ _WFEnforceClass.61969
+ _WFEnforceClass.63664
+ _WFEnforceClass.64156
+ _WFEnforceClass.64518
+ _WFEnforceClass.65167
+ _WFEnforceClass.65752
+ _WFEnforceClass.67572
+ _WFEnforceClass.71973
+ _WFEnforceClass.72269
+ _WFEnforceClass.72791
+ _WFEnforceClass.74192
+ _WFEnforceClass.75148
+ _WFEnforceClass.76090
+ _WFEnforceClass.7769
+ _WFEnforceClass.8252
+ _WFEnforceClass.8644
+ _WFEnforceClass.8980
+ _WFEnforceClass.9243
+ _WFEnforceClass.9587
+ _WFGroupingPropertyForMediaType.53752
+ _WFLinkActionIdentifierCalculateAppUsage
+ _WFLogCategoryCloudKitSync
+ __CLASS_METHODS__TtC11WorkflowKit46WFVisualIntelligenceCameraAvailabilityResource
+ __DATA_WFDatabaseFetchedRecordResult
+ __DATA__TtC11WorkflowKit46WFVisualIntelligenceCameraAvailabilityResource
+ __INSTANCE_METHODS_WFDatabaseFetchedRecordResult
+ __INSTANCE_METHODS__TtC11WorkflowKit46WFVisualIntelligenceCameraAvailabilityResource
+ __IVARS_WFDatabaseFetchedRecordResult
+ __METACLASS_DATA_WFDatabaseFetchedRecordResult
+ __METACLASS_DATA__TtC11WorkflowKit46WFVisualIntelligenceCameraAvailabilityResource
+ __OBJC_$_CLASS_METHODS_WFDatabase(ShortcutSync|Library|AccessResources|WFDatabaseProvider|TipKit|TrackedFilesystemNode|ShortcutSuggestions|Sync|AutoShortcutsPreferences|SmartPrompts|Conflicts|Bookmarks|Shortcuts|Triggers|Collections|RunEvents|PersistedSerializedParameters)
+ __OBJC_$_CLASS_METHODS_WFLinkCalculateAppUsageIntentAction
+ __OBJC_$_CLASS_METHODS_WFLinkIPDataFindSportsEventsAction
+ __OBJC_$_INSTANCE_METHODS_WFDatabase(ShortcutSync|Library|AccessResources|WFDatabaseProvider|TipKit|TrackedFilesystemNode|ShortcutSuggestions|Sync|AutoShortcutsPreferences|SmartPrompts|Conflicts|Bookmarks|Shortcuts|Triggers|Collections|RunEvents|PersistedSerializedParameters)
+ __OBJC_$_INSTANCE_METHODS_WFLinkCalculateAppUsageIntentAction
+ __OBJC_CLASS_PROTOCOLS_$_WFDatabase(ShortcutSync|Library|AccessResources|WFDatabaseProvider|TipKit|TrackedFilesystemNode|ShortcutSuggestions|Sync|AutoShortcutsPreferences|SmartPrompts|Conflicts|Bookmarks|Shortcuts|Triggers|Collections|RunEvents|PersistedSerializedParameters)
+ __OBJC_CLASS_RO_$_WFLinkCalculateAppUsageIntentAction
+ __OBJC_METACLASS_RO_$_WFLinkCalculateAppUsageIntentAction
+ __PROPERTIES_WFDatabaseFetchedRecordResult
+ ___101-[WFResourceManager makeAccessResourcesAvailableWithUserInterface:completionQueue:completionHandler:]_block_invoke
+ ___101-[WFResourceManager makeAccessResourcesAvailableWithUserInterface:completionQueue:completionHandler:]_block_invoke_2
+ ___101-[WFResourceManager makeAccessResourcesAvailableWithUserInterface:completionQueue:completionHandler:]_block_invoke_3
+ ___101-[WFResourceManager makeAccessResourcesAvailableWithUserInterface:completionQueue:completionHandler:]_block_invoke_4
+ ___114-[WFAppIntentExecutionAction completeLoadingPossibleStatesForEnumerationParameter:result:error:completionHandler:]_block_invoke.402
+ ___114-[WFAppIntentExecutionAction completeLoadingPossibleStatesForEnumerationParameter:result:error:completionHandler:]_block_invoke_2.404
+ ___127-[WFDialogTransformer sequentialParameterInputProvider:didAdvanceToParameter:action:defaultState:prompt:linkDialog:completion:]_block_invoke.382
+ ___127-[WFDialogTransformer sequentialParameterInputProvider:didAdvanceToParameter:action:defaultState:prompt:linkDialog:completion:]_block_invoke.389
+ ___127-[WFDialogTransformer sequentialParameterInputProvider:didAdvanceToParameter:action:defaultState:prompt:linkDialog:completion:]_block_invoke_2.383
+ ___127-[WFDialogTransformer sequentialParameterInputProvider:didAdvanceToParameter:action:defaultState:prompt:linkDialog:completion:]_block_invoke_2.391
+ ___127-[WFDialogTransformer sequentialParameterInputProvider:didAdvanceToParameter:action:defaultState:prompt:linkDialog:completion:]_block_invoke_3.393
+ ___34-[WFParameter initWithDefinition:]_block_invoke
+ ___36-[WFAction _finishRunningWithError:]_block_invoke
+ ___36-[WFAction _finishRunningWithError:]_block_invoke.460
+ ___36-[WFAction _finishRunningWithError:]_block_invoke_2
+ ___36-[WFAction _finishRunningWithError:]_block_invoke_3
+ ___36-[WFAction _finishRunningWithError:]_block_invoke_4
+ ___36-[WFDatabase(Library) latestLibrary]_block_invoke
+ ___39-[WFDatabase notifyResultsAboutChange:]_block_invoke.298
+ ___39-[WFDatabase notifyResultsAboutChange:]_block_invoke.304
+ ___39-[WFDatabase notifyResultsAboutChange:]_block_invoke_2.302
+ ___39-[WFDatabase notifyResultsAboutChange:]_block_invoke_2.305
+ ___43-[WFDatabase(Shortcuts) hasWorkflowWithID:]_block_invoke
+ ___47-[WFLinkAction updateParameterSummaryIfNeeded:]_block_invoke.291
+ ___49-[WFDatabase(Shortcuts) applyConflictResolution:]_block_invoke.304
+ ___56-[WFInterchangeManager performQueuedRequestIfApplicable]_block_invoke.213
+ ___57-[WFDatabase removePermissionsWithoutAssociatedShortcuts]_block_invoke
+ ___59-[WFLinkAction getContentDestinationWithCompletionHandler:]_block_invoke.347
+ ___60-[WFLinkContentItemFilterAction runAsynchronouslyWithInput:]_block_invoke.197
+ ___70-[WFLinkEntityContentItem generateFileRepresentation:options:forType:]_block_invoke.750
+ ___73-[WFAppIntentExecutionAction enumeration:localizedLabelForPossibleState:]_block_invoke.406
+ ___73-[WFLinkEntityContentItem generateObjectRepresentation:options:forClass:]_block_invoke.727
+ ___73-[WFLinkEntityContentItem generateObjectRepresentation:options:forClass:]_block_invoke.737
+ ___81-[WFDatabase(Shortcuts) deleteReference:tombstone:deleteConflictIfPresent:error:]_block_invoke.278
+ ___90-[WFInterchangeManager handleOpenURL:fromSourceApplication:errorHandler:postNotification:]_block_invoke.202
+ ___90-[WFInterchangeManager handleOpenURL:fromSourceApplication:errorHandler:postNotification:]_block_invoke_2.203
+ ___91-[WFAppIntentExecutionAction fetchMissingDisplayRepresentationValuesWithCompletionHandler:]_block_invoke.362
+ ___91-[WFAppIntentExecutionAction fetchMissingDisplayRepresentationValuesWithCompletionHandler:]_block_invoke.370
+ ___91-[WFAppIntentExecutionAction fetchMissingDisplayRepresentationValuesWithCompletionHandler:]_block_invoke_2.363
+ ___91-[WFAppIntentExecutionAction fetchMissingDisplayRepresentationValuesWithCompletionHandler:]_block_invoke_2.372
+ ___91-[WFAppIntentExecutionAction fetchMissingDisplayRepresentationValuesWithCompletionHandler:]_block_invoke_3.376
+ ___94-[WFAppIntentExecutionAction postProcessToolKitProcessedValue:forParameter:completionHandler:]_block_invoke.245
+ ___94-[WFAppIntentExecutionAction postProcessToolKitProcessedValue:forParameter:completionHandler:]_block_invoke_2.247
+ ___AssistantServicesLibraryCore_block_invoke.54455
+ ___Block_byref_object_copy_.10388
+ ___Block_byref_object_copy_.10674
+ ___Block_byref_object_copy_.11709
+ ___Block_byref_object_copy_.12234
+ ___Block_byref_object_copy_.12579
+ ___Block_byref_object_copy_.13500
+ ___Block_byref_object_copy_.15203
+ ___Block_byref_object_copy_.16265
+ ___Block_byref_object_copy_.18004
+ ___Block_byref_object_copy_.18106
+ ___Block_byref_object_copy_.19352
+ ___Block_byref_object_copy_.20273
+ ___Block_byref_object_copy_.20678
+ ___Block_byref_object_copy_.20758
+ ___Block_byref_object_copy_.22263
+ ___Block_byref_object_copy_.24769
+ ___Block_byref_object_copy_.25336
+ ___Block_byref_object_copy_.26451
+ ___Block_byref_object_copy_.27480
+ ___Block_byref_object_copy_.29245
+ ___Block_byref_object_copy_.2976
+ ___Block_byref_object_copy_.30131
+ ___Block_byref_object_copy_.31779
+ ___Block_byref_object_copy_.35404
+ ___Block_byref_object_copy_.35678
+ ___Block_byref_object_copy_.37103
+ ___Block_byref_object_copy_.37976
+ ___Block_byref_object_copy_.41382
+ ___Block_byref_object_copy_.42215
+ ___Block_byref_object_copy_.42525
+ ___Block_byref_object_copy_.43729
+ ___Block_byref_object_copy_.46733
+ ___Block_byref_object_copy_.46927
+ ___Block_byref_object_copy_.4784
+ ___Block_byref_object_copy_.48077
+ ___Block_byref_object_copy_.49359
+ ___Block_byref_object_copy_.49816
+ ___Block_byref_object_copy_.5185
+ ___Block_byref_object_copy_.54447
+ ___Block_byref_object_copy_.56147
+ ___Block_byref_object_copy_.57046
+ ___Block_byref_object_copy_.57384
+ ___Block_byref_object_copy_.58224
+ ___Block_byref_object_copy_.59322
+ ___Block_byref_object_copy_.59843
+ ___Block_byref_object_copy_.60962
+ ___Block_byref_object_copy_.61606
+ ___Block_byref_object_copy_.62101
+ ___Block_byref_object_copy_.6287
+ ___Block_byref_object_copy_.64261
+ ___Block_byref_object_copy_.64861
+ ___Block_byref_object_copy_.65146
+ ___Block_byref_object_copy_.66206
+ ___Block_byref_object_copy_.68418
+ ___Block_byref_object_copy_.70405
+ ___Block_byref_object_copy_.71302
+ ___Block_byref_object_copy_.72369
+ ___Block_byref_object_copy_.73176
+ ___Block_byref_object_copy_.7384
+ ___Block_byref_object_copy_.74834
+ ___Block_byref_object_copy_.8531
+ ___Block_byref_object_copy_.9717
+ ___Block_byref_object_copy_.9762
+ ___Block_byref_object_dispose_.10389
+ ___Block_byref_object_dispose_.10675
+ ___Block_byref_object_dispose_.11710
+ ___Block_byref_object_dispose_.12235
+ ___Block_byref_object_dispose_.12580
+ ___Block_byref_object_dispose_.13501
+ ___Block_byref_object_dispose_.15204
+ ___Block_byref_object_dispose_.16266
+ ___Block_byref_object_dispose_.18005
+ ___Block_byref_object_dispose_.18107
+ ___Block_byref_object_dispose_.19353
+ ___Block_byref_object_dispose_.20274
+ ___Block_byref_object_dispose_.20679
+ ___Block_byref_object_dispose_.20759
+ ___Block_byref_object_dispose_.22264
+ ___Block_byref_object_dispose_.24770
+ ___Block_byref_object_dispose_.25337
+ ___Block_byref_object_dispose_.26452
+ ___Block_byref_object_dispose_.27481
+ ___Block_byref_object_dispose_.29246
+ ___Block_byref_object_dispose_.2977
+ ___Block_byref_object_dispose_.30132
+ ___Block_byref_object_dispose_.31780
+ ___Block_byref_object_dispose_.35405
+ ___Block_byref_object_dispose_.35679
+ ___Block_byref_object_dispose_.37104
+ ___Block_byref_object_dispose_.37977
+ ___Block_byref_object_dispose_.41383
+ ___Block_byref_object_dispose_.42216
+ ___Block_byref_object_dispose_.42526
+ ___Block_byref_object_dispose_.43730
+ ___Block_byref_object_dispose_.46734
+ ___Block_byref_object_dispose_.46928
+ ___Block_byref_object_dispose_.4785
+ ___Block_byref_object_dispose_.48078
+ ___Block_byref_object_dispose_.49360
+ ___Block_byref_object_dispose_.49817
+ ___Block_byref_object_dispose_.5186
+ ___Block_byref_object_dispose_.54448
+ ___Block_byref_object_dispose_.56148
+ ___Block_byref_object_dispose_.57047
+ ___Block_byref_object_dispose_.57385
+ ___Block_byref_object_dispose_.58225
+ ___Block_byref_object_dispose_.59323
+ ___Block_byref_object_dispose_.59844
+ ___Block_byref_object_dispose_.60963
+ ___Block_byref_object_dispose_.61607
+ ___Block_byref_object_dispose_.62102
+ ___Block_byref_object_dispose_.6288
+ ___Block_byref_object_dispose_.64262
+ ___Block_byref_object_dispose_.64862
+ ___Block_byref_object_dispose_.65147
+ ___Block_byref_object_dispose_.66207
+ ___Block_byref_object_dispose_.68419
+ ___Block_byref_object_dispose_.70406
+ ___Block_byref_object_dispose_.71303
+ ___Block_byref_object_dispose_.72370
+ ___Block_byref_object_dispose_.73177
+ ___Block_byref_object_dispose_.7385
+ ___Block_byref_object_dispose_.74835
+ ___Block_byref_object_dispose_.8532
+ ___Block_byref_object_dispose_.9718
+ ___Block_byref_object_dispose_.9763
+ ___ContactsLibraryCore_block_invoke.32209
+ ___ContactsLibraryCore_block_invoke.47981
+ ___ContactsLibraryCore_block_invoke.54032
+ ___ContactsLibraryCore_block_invoke.61747
+ ___ContactsLibraryCore_block_invoke.66107
+ ___ContactsLibraryCore_block_invoke.67217
+ ___CoreLocationLibraryCore_block_invoke.41581
+ ___CoreLocationLibraryCore_block_invoke.48003
+ ___CoreLocationLibraryCore_block_invoke.59275
+ ___CoreLocationLibraryCore_block_invoke.59941
+ ___CoreLocationLibraryCore_block_invoke.62106
+ ___CoreLocationLibraryCore_block_invoke.63892
+ ___CoreLocationLibraryCore_block_invoke.66068
+ ___HomeKitLibrary_block_invoke.1582
+ ___HomeKitLibrary_block_invoke.2125
+ ___HomeKitLibrary_block_invoke.28255
+ ___HomeKitLibrary_block_invoke.35703
+ ___HomeKitLibrary_block_invoke.36534
+ ___HomeKitLibrary_block_invoke.38926
+ ___HomeKitLibrary_block_invoke.56625
+ ___HomeLibrary_block_invoke.28393
+ ___HomeLibrary_block_invoke.35672
+ ___HomeLibrary_block_invoke.38919
+ ___HomeLibrary_block_invoke.4479
+ ___MediaPlayerLibraryCore_block_invoke.37092
+ ___MediaPlayerLibraryCore_block_invoke.53766
+ ___PhotosLibraryCore_block_invoke.1495
+ ___ReminderKitLibraryCore_block_invoke.25665
+ ___RunningBoardServicesLibraryCore_block_invoke.27461
+ ___SAObjectsLibrary_block_invoke.70725
+ ___UIKitLibraryCore_block_invoke.41838
+ ___UIKitLibrary_block_invoke.16276
+ ___UIKitLibrary_block_invoke.22971
+ ___UIKitLibrary_block_invoke.28660
+ ___UIKitLibrary_block_invoke.29258
+ ___UIKitLibrary_block_invoke.42539
+ ___UIKitLibrary_block_invoke.49483
+ ___UIKitLibrary_block_invoke.58985
+ ___UIKitLibrary_block_invoke.61458
+ ___UIKitLibrary_block_invoke.64556
+ ___WFUpdateSmartPromptChangesToShortcutChanges_block_invoke.606
+ ___block_descriptor_40_e8_32s_e20_"WFLibrary"16?0^8ls32l8
+ ___block_descriptor_48_e8_32s40s_e35_v24?0"LNQueryOutput"8"NSError"16ls32l8s40l8
+ ___block_descriptor_64_e8_32s40s48s56s_e17_v16?0"NSError"8ls32l8s40l8s48l8s56l8
+ ___block_literal_global.10305
+ ___block_literal_global.1091
+ ___block_literal_global.10980
+ ___block_literal_global.11239
+ ___block_literal_global.11319
+ ___block_literal_global.1162
+ ___block_literal_global.1169
+ ___block_literal_global.12241
+ ___block_literal_global.1257
+ ___block_literal_global.12598
+ ___block_literal_global.13237
+ ___block_literal_global.13290
+ ___block_literal_global.13493
+ ___block_literal_global.13723
+ ___block_literal_global.1377
+ ___block_literal_global.13848
+ ___block_literal_global.14402
+ ___block_literal_global.14485
+ ___block_literal_global.14709
+ ___block_literal_global.15660
+ ___block_literal_global.15861
+ ___block_literal_global.1621
+ ___block_literal_global.16270
+ ___block_literal_global.1713
+ ___block_literal_global.172.22600
+ ___block_literal_global.176.45836
+ ___block_literal_global.178.29619
+ ___block_literal_global.178.39830
+ ___block_literal_global.178.69665
+ ___block_literal_global.178.74851
+ ___block_literal_global.179.26497
+ ___block_literal_global.180.36445
+ ___block_literal_global.18152
+ ___block_literal_global.183.72380
+ ___block_literal_global.183.74878
+ ___block_literal_global.186.52437
+ ___block_literal_global.186.72384
+ ___block_literal_global.186.74879
+ ___block_literal_global.18848
+ ___block_literal_global.189.4468
+ ___block_literal_global.189.45863
+ ___block_literal_global.189.60415
+ ___block_literal_global.189.60764
+ ___block_literal_global.189.75143
+ ___block_literal_global.18949
+ ___block_literal_global.191.60765
+ ___block_literal_global.191.72388
+ ___block_literal_global.192.6278
+ ___block_literal_global.19260
+ ___block_literal_global.193.25344
+ ___block_literal_global.193.29138
+ ___block_literal_global.193.45866
+ ___block_literal_global.193.66937
+ ___block_literal_global.194.72371
+ ___block_literal_global.19580
+ ___block_literal_global.19695
+ ___block_literal_global.199.18132
+ ___block_literal_global.199.45112
+ ___block_literal_global.199.57190
+ ___block_literal_global.202.18129
+ ___block_literal_global.202.21134
+ ___block_literal_global.202.56972
+ ___block_literal_global.203.46201
+ ___block_literal_global.205.25320
+ ___block_literal_global.206.60408
+ ___block_literal_global.20653
+ ___block_literal_global.208.49381
+ ___block_literal_global.2102
+ ___block_literal_global.21158
+ ___block_literal_global.213.53735
+ ___block_literal_global.219.68868
+ ___block_literal_global.22064
+ ___block_literal_global.22485
+ ___block_literal_global.225.26794
+ ___block_literal_global.225.60392
+ ___block_literal_global.2255
+ ___block_literal_global.22671
+ ___block_literal_global.227.74825
+ ___block_literal_global.22769
+ ___block_literal_global.22967
+ ___block_literal_global.230.41433
+ ___block_literal_global.23030
+ ___block_literal_global.232.43335
+ ___block_literal_global.232.69344
+ ___block_literal_global.23259
+ ___block_literal_global.23442
+ ___block_literal_global.239.74792
+ ___block_literal_global.23968
+ ___block_literal_global.247.37171
+ ___block_literal_global.247.69340
+ ___block_literal_global.24786
+ ___block_literal_global.25079
+ ___block_literal_global.251.55404
+ ___block_literal_global.251.68442
+ ___block_literal_global.25175
+ ___block_literal_global.25302
+ ___block_literal_global.25614
+ ___block_literal_global.26177
+ ___block_literal_global.26474
+ ___block_literal_global.2666
+ ___block_literal_global.26784
+ ___block_literal_global.27018
+ ___block_literal_global.27536
+ ___block_literal_global.277.41364
+ ___block_literal_global.277.47038
+ ___block_literal_global.2819
+ ___block_literal_global.28244
+ ___block_literal_global.283.11322
+ ___block_literal_global.28656
+ ___block_literal_global.2885
+ ___block_literal_global.29149
+ ___block_literal_global.29248
+ ___block_literal_global.29371
+ ___block_literal_global.294.7867
+ ___block_literal_global.2958
+ ___block_literal_global.29625
+ ___block_literal_global.29784
+ ___block_literal_global.299.76755
+ ___block_literal_global.30115
+ ___block_literal_global.305.58989
+ ___block_literal_global.306.14710
+ ___block_literal_global.311.59076
+ ___block_literal_global.31645
+ ___block_literal_global.320
+ ___block_literal_global.33697
+ ___block_literal_global.338.4748
+ ___block_literal_global.34408
+ ___block_literal_global.347.39573
+ ___block_literal_global.348.41495
+ ___block_literal_global.35442
+ ___block_literal_global.35696
+ ___block_literal_global.357.41524
+ ___block_literal_global.3581
+ ___block_literal_global.359
+ ___block_literal_global.35994
+ ___block_literal_global.36441
+ ___block_literal_global.36530
+ ___block_literal_global.37009
+ ___block_literal_global.37169
+ ___block_literal_global.37373
+ ___block_literal_global.37983
+ ___block_literal_global.38900
+ ___block_literal_global.39460
+ ___block_literal_global.395.60242
+ ___block_literal_global.397.39546
+ ___block_literal_global.39829
+ ___block_literal_global.3984
+ ___block_literal_global.40651
+ ___block_literal_global.41114
+ ___block_literal_global.41432
+ ___block_literal_global.41616
+ ___block_literal_global.42250
+ ___block_literal_global.42375
+ ___block_literal_global.42532
+ ___block_literal_global.42739
+ ___block_literal_global.43363
+ ___block_literal_global.4369
+ ___block_literal_global.43967
+ ___block_literal_global.44071
+ ___block_literal_global.44398
+ ___block_literal_global.44476
+ ___block_literal_global.4495
+ ___block_literal_global.45115
+ ___block_literal_global.454.33633
+ ___block_literal_global.454.7393
+ ___block_literal_global.45587
+ ___block_literal_global.45845
+ ___block_literal_global.46195
+ ___block_literal_global.46305
+ ___block_literal_global.469.67781
+ ___block_literal_global.47028
+ ___block_literal_global.47082
+ ___block_literal_global.47339
+ ___block_literal_global.475
+ ___block_literal_global.477.67782
+ ___block_literal_global.479
+ ___block_literal_global.48097
+ ___block_literal_global.4836
+ ___block_literal_global.49138
+ ___block_literal_global.4926
+ ___block_literal_global.49349
+ ___block_literal_global.49476
+ ___block_literal_global.49666
+ ___block_literal_global.49761
+ ___block_literal_global.50027
+ ___block_literal_global.50937
+ ___block_literal_global.50962
+ ___block_literal_global.5146
+ ___block_literal_global.51601
+ ___block_literal_global.51611
+ ___block_literal_global.52242
+ ___block_literal_global.52436
+ ___block_literal_global.52772
+ ___block_literal_global.52833
+ ___block_literal_global.53734
+ ___block_literal_global.5392
+ ___block_literal_global.54037
+ ___block_literal_global.54443
+ ___block_literal_global.54730
+ ___block_literal_global.54786
+ ___block_literal_global.55402
+ ___block_literal_global.55592
+ ___block_literal_global.56068
+ ___block_literal_global.5612
+ ___block_literal_global.56254
+ ___block_literal_global.56621
+ ___block_literal_global.57053
+ ___block_literal_global.57189
+ ___block_literal_global.57675
+ ___block_literal_global.57880
+ ___block_literal_global.59129
+ ___block_literal_global.59264
+ ___block_literal_global.60426
+ ___block_literal_global.60763
+ ___block_literal_global.61068
+ ___block_literal_global.61321
+ ___block_literal_global.61451
+ ___block_literal_global.61645
+ ___block_literal_global.61709
+ ___block_literal_global.6275
+ ___block_literal_global.6341
+ ___block_literal_global.63764
+ ___block_literal_global.63842
+ ___block_literal_global.64153
+ ___block_literal_global.64510
+ ___block_literal_global.65469
+ ___block_literal_global.66085
+ ___block_literal_global.66946
+ ___block_literal_global.6696
+ ___block_literal_global.67204
+ ___block_literal_global.67242
+ ___block_literal_global.67616
+ ___block_literal_global.67940
+ ___block_literal_global.68186
+ ___block_literal_global.68501
+ ___block_literal_global.68867
+ ___block_literal_global.69357
+ ___block_literal_global.69434
+ ___block_literal_global.695
+ ___block_literal_global.69507
+ ___block_literal_global.69670
+ ___block_literal_global.70017
+ ___block_literal_global.703.43072
+ ___block_literal_global.704
+ ___block_literal_global.70402
+ ___block_literal_global.70720
+ ___block_literal_global.70887
+ ___block_literal_global.71236
+ ___block_literal_global.71641
+ ___block_literal_global.72147
+ ___block_literal_global.72400
+ ___block_literal_global.73195
+ ___block_literal_global.739
+ ___block_literal_global.743
+ ___block_literal_global.746
+ ___block_literal_global.74622
+ ___block_literal_global.74849
+ ___block_literal_global.75164
+ ___block_literal_global.756
+ ___block_literal_global.7576
+ ___block_literal_global.75865
+ ___block_literal_global.759
+ ___block_literal_global.76767
+ ___block_literal_global.787
+ ___block_literal_global.7895
+ ___block_literal_global.8245
+ ___block_literal_global.8763
+ ___block_literal_global.8995
+ ___block_literal_global.914
+ ___block_literal_global.9411
+ ___block_literal_global.9675
+ ___getCLPlacemarkClass_block_invoke.59939
+ ___getCLPlacemarkClass_block_invoke.62104
+ ___getCLPlacemarkClass_block_invoke.66066
+ ___getCNContactStoreClass_block_invoke.67206
+ ___getMPMediaItemClass_block_invoke.53751
+ ___getMPMediaPropertyPredicateClass_block_invoke.37061
+ ___getMPMediaPropertyPredicateClass_block_invoke.53749
+ ___getMPMediaQueryClass_block_invoke.37064
+ ___getMPMediaQueryClass_block_invoke.53754
+ __mutableRegisteredDefinitions.69442
+ _associated conformance 11WorkflowKit17DrawerSearchIndexV0D18ResultSetItemMatch33_BE64EF1D94490A7CEC9B5F1A766DD337LLVyx_GSHAASQ
+ _audit_stringAssistantServices.54470
+ _audit_stringContacts.32223
+ _audit_stringContacts.47995
+ _audit_stringContacts.54035
+ _audit_stringContacts.61751
+ _audit_stringContacts.66110
+ _audit_stringContacts.67223
+ _audit_stringCoreLocation.41596
+ _audit_stringCoreLocation.48007
+ _audit_stringCoreLocation.59278
+ _audit_stringCoreLocation.59955
+ _audit_stringCoreLocation.62120
+ _audit_stringCoreLocation.63905
+ _audit_stringCoreLocation.66082
+ _audit_stringMediaPlayer.37098
+ _audit_stringMediaPlayer.53772
+ _audit_stringPhotos.1501
+ _audit_stringReminderKit.25671
+ _audit_stringRunningBoardServices.27467
+ _audit_stringUIKit.41852
+ _classHFTriggerActionSetsBuilder.35668
+ _classHFTriggerActionSetsBuilder.38915
+ _classRegistrationLock.52149
+ _classRegistrationLock.72762
+ _classRegistrationLock.9193
+ _classUIPasteboard.42544
+ _classUIPasteboard.49478
+ _classUIPasteboard.61453
+ _classUIPasteboard.64551
+ _constantHMCharacteristicMetadataFormatBool.2168
+ _constantHMCharacteristicMetadataFormatBool.28268
+ _constantHMCharacteristicMetadataFormatFloat.2148
+ _constantHMCharacteristicMetadataFormatInt.2155
+ _constantHMCharacteristicMetadataFormatInt.28379
+ _constantHMCharacteristicMetadataFormatString.2161
+ _constantHMCharacteristicMetadataFormatUInt16.2136
+ _constantHMCharacteristicMetadataFormatUInt32.2129
+ _constantHMCharacteristicMetadataFormatUInt64.2121
+ _constantHMCharacteristicMetadataFormatUInt8.2142
+ _constantHMCharacteristicMetadataFormatUInt8.28386
+ _getCLPlacemarkClass.66001
+ _getCLPlacemarkClass.softClass.59938
+ _getCLPlacemarkClass.softClass.62103
+ _getCLPlacemarkClass.softClass.66065
+ _getCNContactStoreClass.softClass.67205
+ _getHFTriggerActionSetsBuilderClass.35656
+ _getHFTriggerActionSetsBuilderClass.38910
+ _getHMCharacteristicMetadataFormatBool.2107
+ _getHMCharacteristicMetadataFormatBool.28263
+ _getHMCharacteristicMetadataFormatFloat.2110
+ _getHMCharacteristicMetadataFormatInt.2109
+ _getHMCharacteristicMetadataFormatInt.28374
+ _getHMCharacteristicMetadataFormatString.2108
+ _getHMCharacteristicMetadataFormatUInt16.2112
+ _getHMCharacteristicMetadataFormatUInt32.2113
+ _getHMCharacteristicMetadataFormatUInt64.2114
+ _getHMCharacteristicMetadataFormatUInt8.2111
+ _getHMCharacteristicMetadataFormatUInt8.28373
+ _getMPMediaItemClass.softClass.53750
+ _getMPMediaPropertyPredicateClass.softClass.37060
+ _getMPMediaPropertyPredicateClass.softClass.53748
+ _getMPMediaQueryClass.softClass.37063
+ _getMPMediaQueryClass.softClass.53753
+ _getUIPasteboardClass.42529
+ _getUIPasteboardClass.49472
+ _getUIPasteboardClass.61444
+ _getUIPasteboardClass.64544
+ _getWFToolKitExecutionLogObject
+ _initHFTriggerActionSetsBuilder.35665
+ _initHFTriggerActionSetsBuilder.38912
+ _initHMCharacteristicMetadataFormatBool.2165
+ _initHMCharacteristicMetadataFormatBool.28265
+ _initHMCharacteristicMetadataFormatFloat.2146
+ _initHMCharacteristicMetadataFormatInt.2152
+ _initHMCharacteristicMetadataFormatInt.28376
+ _initHMCharacteristicMetadataFormatString.2159
+ _initHMCharacteristicMetadataFormatUInt16.2133
+ _initHMCharacteristicMetadataFormatUInt32.2127
+ _initHMCharacteristicMetadataFormatUInt64.2116
+ _initHMCharacteristicMetadataFormatUInt8.2140
+ _initHMCharacteristicMetadataFormatUInt8.28383
+ _initUIPasteboard.42542
+ _initUIPasteboard.49474
+ _initUIPasteboard.61449
+ _initUIPasteboard.64547
+ _objc_msgSend$_finishRunningWithError:
+ _objc_msgSend$completionQueue
+ _objc_msgSend$folderIdentifier
+ _objc_msgSend$if_enumerateAsynchronouslyOnQueue:block:completionHandler:
+ _objc_msgSend$makeAccessResourcesAvailableWithUserInterface:completionQueue:completionHandler:
+ _objc_msgSend$removePermissionsWithoutAssociatedShortcuts
+ _objc_msgSend$setCompletionQueue:
+ _objc_msgSend$setFolderIdentifier:
+ _objc_msgSend$wf_isAllowedInXCallback
+ _rediscoverDefinitionsIfNeeded.calledDefinitionVendingSelectors.69435
+ _rediscoverDefinitionsIfNeeded.lock.69437
+ _rediscoverDefinitionsIfNeeded.onceToken.69433
+ _sharedInstance.onceToken.12597
+ _sharedInstance.onceToken.59128
+ _sharedInstance.onceToken.8994
+ _sharedManager.onceToken.1620
+ _sharedManager.onceToken.60777
+ _sharedManager.onceToken.68500
+ _sharedManager.sharedManager.60778
+ _sharedManager.sharedManager.68502
+ _sharedRegistry.onceToken.16455
+ _sharedRegistry.onceToken.25373
+ _sharedRegistry.sharedRegistry.16456
+ _sharedRegistry.sharedRegistry.25374
+ _symbolic SDy_____yx_G_____yx__GG 11WorkflowKit17DrawerSearchIndexV0D18ResultSetItemMatch33_BE64EF1D94490A7CEC9B5F1A766DD337LLV AC0dF0V0I0V
+ _symbolic So29WFDatabaseFetchedRecordResultCSg
+ _symbolic So29WFDatabaseFetchedRecordResultC______pIgrzo_ s5ErrorP
+ _symbolic _____ 11WorkflowKit17DrawerSearchIndexV0D18ResultSetItemMatch33_BE64EF1D94490A7CEC9B5F1A766DD337LLV
+ _symbolic _____ 11WorkflowKit46WFVisualIntelligenceCameraAvailabilityResourceC
+ _symbolic _____Sg 18AppIntentsServices18SnippetEnvironmentV
+ _symbolic _____y______G 11WorkflowKit17DrawerSearchIndexV0D18ResultSetItemMatch33_BE64EF1D94490A7CEC9B5F1A766DD337LLV AA0cdeH033_3DEEF7B2499E1B37D3EC5450A935870FLLO
+ _symbolic _____y_____y______G_____yAC__GG s17_NativeDictionaryV 11WorkflowKit17DrawerSearchIndexV0F18ResultSetItemMatch33_BE64EF1D94490A7CEC9B5F1A766DD337LLV AC0efgJ033_3DEEF7B2499E1B37D3EC5450A935870FLLO AE0fH0V0K0V
- +[NSUserDefaults(Sync) conflictResolutionEnabled]
- -[WFDatabase hasValidLibrary]
- -[WFDatabase reloadLibrary]
- -[WFDatabase(Library) coreDataLibrary]
- -[WFDatabase(Library) saveLibraryToDatabase]
- -[WFDatabase(Library) wipeAllLibrariesWithError:]
- -[WFDatabase(Shortcuts) createWorkflowWithIdentifier:record:error:]
- -[WFDatabase(Shortcuts) localConflictingReferenceForReference:]
- -[WFDatabase(Shortcuts) remoteConflictingReferenceForReference:]
- -[WFLinkWritingToolsAction contentDestinationWithError:]
- -[WFVariablePickerParameter .cxx_destruct]
- -[WFVariablePickerParameter initWithDefinition:]
- -[WFVariablePickerParameter preferredTypes]
- -[WFWorkflowCreationOptions collectionIdentifier]
- -[WFWorkflowCreationOptions setCollectionIdentifier:]
- -[WFWorkflowRecord isEquivalentForSyncTo:]
- GCC_except_table10013
- GCC_except_table10172
- GCC_except_table10196
- GCC_except_table10199
- GCC_except_table10201
- GCC_except_table10240
- GCC_except_table10408
- GCC_except_table10414
- GCC_except_table10433
- GCC_except_table10587
- GCC_except_table10621
- GCC_except_table10688
- GCC_except_table10697
- GCC_except_table10699
- GCC_except_table10727
- GCC_except_table10732
- GCC_except_table10772
- GCC_except_table10775
- GCC_except_table10778
- GCC_except_table10781
- GCC_except_table10971
- GCC_except_table11065
- GCC_except_table11082
- GCC_except_table11104
- GCC_except_table11146
- GCC_except_table11504
- GCC_except_table11530
- GCC_except_table11533
- GCC_except_table11549
- GCC_except_table11621
- GCC_except_table11896
- GCC_except_table11905
- GCC_except_table11916
- GCC_except_table11923
- GCC_except_table11928
- GCC_except_table11931
- GCC_except_table11986
- GCC_except_table11987
- GCC_except_table11988
- GCC_except_table11989
- GCC_except_table12002
- GCC_except_table12004
- GCC_except_table12102
- GCC_except_table1226
- GCC_except_table12299
- GCC_except_table12315
- GCC_except_table12494
- GCC_except_table12509
- GCC_except_table12515
- GCC_except_table12517
- GCC_except_table12616
- GCC_except_table12629
- GCC_except_table12637
- GCC_except_table12678
- GCC_except_table12715
- GCC_except_table12729
- GCC_except_table12731
- GCC_except_table12733
- GCC_except_table12815
- GCC_except_table12831
- GCC_except_table12937
- GCC_except_table12978
- GCC_except_table1299
- GCC_except_table13033
- GCC_except_table13062
- GCC_except_table13116
- GCC_except_table13127
- GCC_except_table13171
- GCC_except_table13173
- GCC_except_table13491
- GCC_except_table13524
- GCC_except_table13641
- GCC_except_table13670
- GCC_except_table13676
- GCC_except_table13723
- GCC_except_table13817
- GCC_except_table13830
- GCC_except_table13833
- GCC_except_table13845
- GCC_except_table13852
- GCC_except_table13853
- GCC_except_table13854
- GCC_except_table13863
- GCC_except_table13874
- GCC_except_table14000
- GCC_except_table1404
- GCC_except_table14070
- GCC_except_table14079
- GCC_except_table1409
- GCC_except_table14270
- GCC_except_table14338
- GCC_except_table14582
- GCC_except_table14612
- GCC_except_table14728
- GCC_except_table14899
- GCC_except_table14904
- GCC_except_table14913
- GCC_except_table14916
- GCC_except_table15033
- GCC_except_table15056
- GCC_except_table15067
- GCC_except_table15070
- GCC_except_table15385
- GCC_except_table15425
- GCC_except_table15436
- GCC_except_table15450
- GCC_except_table15453
- GCC_except_table15647
- GCC_except_table15774
- GCC_except_table1734
- GCC_except_table1747
- GCC_except_table1752
- GCC_except_table1754
- GCC_except_table1756
- GCC_except_table1993
- GCC_except_table2069
- GCC_except_table2150
- GCC_except_table2160
- GCC_except_table2331
- GCC_except_table2339
- GCC_except_table2369
- GCC_except_table245
- GCC_except_table2520
- GCC_except_table254
- GCC_except_table2547
- GCC_except_table2615
- GCC_except_table2652
- GCC_except_table2768
- GCC_except_table2785
- GCC_except_table2877
- GCC_except_table2930
- GCC_except_table2947
- GCC_except_table2953
- GCC_except_table3165
- GCC_except_table3187
- GCC_except_table3188
- GCC_except_table3195
- GCC_except_table3196
- GCC_except_table3197
- GCC_except_table3222
- GCC_except_table3226
- GCC_except_table3250
- GCC_except_table3282
- GCC_except_table3298
- GCC_except_table3302
- GCC_except_table3361
- GCC_except_table3372
- GCC_except_table3374
- GCC_except_table348
- GCC_except_table351
- GCC_except_table3563
- GCC_except_table3567
- GCC_except_table3569
- GCC_except_table3573
- GCC_except_table3574
- GCC_except_table3878
- GCC_except_table3882
- GCC_except_table4240
- GCC_except_table4241
- GCC_except_table4360
- GCC_except_table4462
- GCC_except_table4475
- GCC_except_table4494
- GCC_except_table4502
- GCC_except_table4677
- GCC_except_table4858
- GCC_except_table4864
- GCC_except_table4870
- GCC_except_table4960
- GCC_except_table4974
- GCC_except_table5089
- GCC_except_table5116
- GCC_except_table5120
- GCC_except_table5160
- GCC_except_table52
- GCC_except_table5218
- GCC_except_table5226
- GCC_except_table5249
- GCC_except_table5289
- GCC_except_table5345
- GCC_except_table5350
- GCC_except_table5352
- GCC_except_table536
- GCC_except_table5478
- GCC_except_table5484
- GCC_except_table5500
- GCC_except_table5871
- GCC_except_table6015
- GCC_except_table6074
- GCC_except_table6084
- GCC_except_table6181
- GCC_except_table627
- GCC_except_table6311
- GCC_except_table6312
- GCC_except_table6313
- GCC_except_table6414
- GCC_except_table6461
- GCC_except_table6479
- GCC_except_table6508
- GCC_except_table6833
- GCC_except_table6909
- GCC_except_table6910
- GCC_except_table6915
- GCC_except_table6916
- GCC_except_table6919
- GCC_except_table6925
- GCC_except_table6930
- GCC_except_table6935
- GCC_except_table6936
- GCC_except_table6976
- GCC_except_table6981
- GCC_except_table7039
- GCC_except_table7050
- GCC_except_table7320
- GCC_except_table7330
- GCC_except_table7404
- GCC_except_table7482
- GCC_except_table7783
- GCC_except_table7826
- GCC_except_table7873
- GCC_except_table7874
- GCC_except_table79
- GCC_except_table7940
- GCC_except_table8070
- GCC_except_table8208
- GCC_except_table8213
- GCC_except_table8224
- GCC_except_table83
- GCC_except_table8404
- GCC_except_table8411
- GCC_except_table8422
- GCC_except_table846
- GCC_except_table9011
- GCC_except_table9080
- GCC_except_table9086
- GCC_except_table9089
- GCC_except_table9092
- GCC_except_table9096
- GCC_except_table9130
- GCC_except_table9184
- GCC_except_table919
- GCC_except_table9277
- GCC_except_table928
- GCC_except_table9326
- GCC_except_table9563
- GCC_except_table9569
- GCC_except_table9571
- GCC_except_table9573
- GCC_except_table9575
- GCC_except_table9581
- GCC_except_table9631
- GCC_except_table9645
- GCC_except_table9654
- GCC_except_table9697
- GCC_except_table9703
- GCC_except_table9709
- GCC_except_table9979
- GCC_except_table9981
- GCC_except_table9982
- GCC_except_table9983
- GCC_except_table9985
- GCC_except_table9987
- GCC_except_table9989
- GCC_except_table9992
- GCC_except_table9995
- _AssistantServicesLibraryCore.frameworkLibrary.54487
- _ContactsLibrary.54014
- _ContactsLibrary.67248
- _ContactsLibraryCore.frameworkLibrary.32216
- _ContactsLibraryCore.frameworkLibrary.48011
- _ContactsLibraryCore.frameworkLibrary.54064
- _ContactsLibraryCore.frameworkLibrary.61785
- _ContactsLibraryCore.frameworkLibrary.66146
- _ContactsLibraryCore.frameworkLibrary.67256
- _CoreLocationLibraryCore.frameworkLibrary.41589
- _CoreLocationLibraryCore.frameworkLibrary.48033
- _CoreLocationLibraryCore.frameworkLibrary.59314
- _CoreLocationLibraryCore.frameworkLibrary.59980
- _CoreLocationLibraryCore.frameworkLibrary.62144
- _CoreLocationLibraryCore.frameworkLibrary.63930
- _CoreLocationLibraryCore.frameworkLibrary.66107
- _HFTriggerActionSetsBuilderFunction.35676
- _HFTriggerActionSetsBuilderFunction.38930
- _HMCharacteristicMetadataFormatBoolFunction.2210
- _HMCharacteristicMetadataFormatBoolFunction.28281
- _HMCharacteristicMetadataFormatFloatFunction.2190
- _HMCharacteristicMetadataFormatIntFunction.2197
- _HMCharacteristicMetadataFormatIntFunction.28392
- _HMCharacteristicMetadataFormatStringFunction.2203
- _HMCharacteristicMetadataFormatUInt16Function.2178
- _HMCharacteristicMetadataFormatUInt32Function.2171
- _HMCharacteristicMetadataFormatUInt64Function.2163
- _HMCharacteristicMetadataFormatUInt8Function.2184
- _HMCharacteristicMetadataFormatUInt8Function.28399
- _HomeKitLibrary.sLib.1624
- _HomeKitLibrary.sLib.2158
- _HomeKitLibrary.sLib.28261
- _HomeKitLibrary.sLib.35703
- _HomeKitLibrary.sLib.36542
- _HomeKitLibrary.sLib.38941
- _HomeKitLibrary.sLib.56661
- _HomeKitLibrary.sOnce.1619
- _HomeKitLibrary.sOnce.2157
- _HomeKitLibrary.sOnce.28260
- _HomeKitLibrary.sOnce.35701
- _HomeKitLibrary.sOnce.36535
- _HomeKitLibrary.sOnce.38936
- _HomeKitLibrary.sOnce.56654
- _HomeLibrary.sLib.28406
- _HomeLibrary.sLib.35680
- _HomeLibrary.sLib.38934
- _HomeLibrary.sLib.4516
- _HomeLibrary.sOnce.28402
- _HomeLibrary.sOnce.35672
- _HomeLibrary.sOnce.38926
- _HomeLibrary.sOnce.4511
- _MediaPlayerLibrary.37094
- _MediaPlayerLibrary.53791
- _MediaPlayerLibraryCore.frameworkLibrary.37104
- _MediaPlayerLibraryCore.frameworkLibrary.53798
- _OBJC_IVAR_$_WFVariablePickerParameter._preferredTypes
- _OBJC_IVAR_$_WFWorkflowCreationOptions._collectionIdentifier
- _OUTLINED_FUNCTION_261
- _OUTLINED_FUNCTION_262
- _OUTLINED_FUNCTION_263
- _PhotosLibraryCore.frameworkLibrary.1534
- _ReminderKitLibraryCore.frameworkLibrary.25680
- _RunningBoardServicesLibrary.27472
- _RunningBoardServicesLibraryCore.frameworkLibrary.27474
- _SAObjectsLibrary.sLib.70752
- _SAObjectsLibrary.sOnce.70750
- _UIKitLibrary.sLib.16300
- _UIKitLibrary.sLib.22991
- _UIKitLibrary.sLib.28673
- _UIKitLibrary.sLib.29271
- _UIKitLibrary.sLib.42542
- _UIKitLibrary.sLib.49516
- _UIKitLibrary.sLib.59026
- _UIKitLibrary.sLib.61499
- _UIKitLibrary.sLib.64597
- _UIKitLibrary.sOnce.16298
- _UIKitLibrary.sOnce.22984
- _UIKitLibrary.sOnce.28666
- _UIKitLibrary.sOnce.29268
- _UIKitLibrary.sOnce.42540
- _UIKitLibrary.sOnce.49506
- _UIKitLibrary.sOnce.59021
- _UIKitLibrary.sOnce.61489
- _UIKitLibrary.sOnce.64587
- _UIKitLibraryCore.frameworkLibrary.41846
- _UIPasteboardFunction.42555
- _UIPasteboardFunction.49511
- _UIPasteboardFunction.61494
- _UIPasteboardFunction.64592
- _WFActionGreenTeaContentDestinationMayLeaveDevice.onceToken.1166
- _WFConflictResolutionEnabledKey
- _WFDyldBulkImageLoadCallback.25103
- _WFEnforceClass.10347
- _WFEnforceClass.1056
- _WFEnforceClass.13311
- _WFEnforceClass.13519
- _WFEnforceClass.1517
- _WFEnforceClass.15658
- _WFEnforceClass.16714
- _WFEnforceClass.16835
- _WFEnforceClass.17257
- _WFEnforceClass.17892
- _WFEnforceClass.1966
- _WFEnforceClass.2135
- _WFEnforceClass.21363
- _WFEnforceClass.21605
- _WFEnforceClass.22512
- _WFEnforceClass.23402
- _WFEnforceClass.23468
- _WFEnforceClass.25074
- _WFEnforceClass.25187
- _WFEnforceClass.29097
- _WFEnforceClass.29382
- _WFEnforceClass.29468
- _WFEnforceClass.29628
- _WFEnforceClass.29817
- _WFEnforceClass.30064
- _WFEnforceClass.30807
- _WFEnforceClass.31818
- _WFEnforceClass.32364
- _WFEnforceClass.3457
- _WFEnforceClass.35851
- _WFEnforceClass.36883
- _WFEnforceClass.37367
- _WFEnforceClass.4019
- _WFEnforceClass.40815
- _WFEnforceClass.42383
- _WFEnforceClass.43858
- _WFEnforceClass.4558
- _WFEnforceClass.46737
- _WFEnforceClass.47169
- _WFEnforceClass.47312
- _WFEnforceClass.49408
- _WFEnforceClass.50859
- _WFEnforceClass.51345
- _WFEnforceClass.58022
- _WFEnforceClass.58922
- _WFEnforceClass.59188
- _WFEnforceClass.61297
- _WFEnforceClass.62008
- _WFEnforceClass.6206
- _WFEnforceClass.63703
- _WFEnforceClass.64195
- _WFEnforceClass.64557
- _WFEnforceClass.65206
- _WFEnforceClass.65791
- _WFEnforceClass.67613
- _WFEnforceClass.72004
- _WFEnforceClass.72300
- _WFEnforceClass.72822
- _WFEnforceClass.74224
- _WFEnforceClass.75180
- _WFEnforceClass.76123
- _WFEnforceClass.7797
- _WFEnforceClass.8280
- _WFEnforceClass.8676
- _WFEnforceClass.9012
- _WFEnforceClass.9275
- _WFEnforceClass.9619
- _WFGroupingPropertyForMediaType.53786
- _WFWorkflowTypeWatchKit
- __OBJC_$_CLASS_METHODS_WFDatabase(Library|AccessResources|WFDatabaseProvider|TipKit|TrackedFilesystemNode|ShortcutSuggestions|Sync|AutoShortcutsPreferences|SmartPrompts|Conflicts|Bookmarks|Shortcuts|Triggers|Collections|RunEvents|PersistedSerializedParameters)
- __OBJC_$_INSTANCE_METHODS_WFDatabase(Library|AccessResources|WFDatabaseProvider|TipKit|TrackedFilesystemNode|ShortcutSuggestions|Sync|AutoShortcutsPreferences|SmartPrompts|Conflicts|Bookmarks|Shortcuts|Triggers|Collections|RunEvents|PersistedSerializedParameters)
- __OBJC_$_INSTANCE_VARIABLES_WFVariablePickerParameter
- __OBJC_CLASS_PROTOCOLS_$_WFDatabase(Library|AccessResources|WFDatabaseProvider|TipKit|TrackedFilesystemNode|ShortcutSuggestions|Sync|AutoShortcutsPreferences|SmartPrompts|Conflicts|Bookmarks|Shortcuts|Triggers|Collections|RunEvents|PersistedSerializedParameters)
- ___114-[WFAppIntentExecutionAction completeLoadingPossibleStatesForEnumerationParameter:result:error:completionHandler:]_block_invoke.400
- ___114-[WFAppIntentExecutionAction completeLoadingPossibleStatesForEnumerationParameter:result:error:completionHandler:]_block_invoke_2.402
- ___127-[WFDialogTransformer sequentialParameterInputProvider:didAdvanceToParameter:action:defaultState:prompt:linkDialog:completion:]_block_invoke.381
- ___127-[WFDialogTransformer sequentialParameterInputProvider:didAdvanceToParameter:action:defaultState:prompt:linkDialog:completion:]_block_invoke.387
- ___127-[WFDialogTransformer sequentialParameterInputProvider:didAdvanceToParameter:action:defaultState:prompt:linkDialog:completion:]_block_invoke_2.382
- ___127-[WFDialogTransformer sequentialParameterInputProvider:didAdvanceToParameter:action:defaultState:prompt:linkDialog:completion:]_block_invoke_2.390
- ___127-[WFDialogTransformer sequentialParameterInputProvider:didAdvanceToParameter:action:defaultState:prompt:linkDialog:completion:]_block_invoke_3.392
- ___27-[WFDatabase reloadLibrary]_block_invoke
- ___35-[WFAction finishRunningWithError:]_block_invoke.460
- ___35-[WFAction finishRunningWithError:]_block_invoke_2
- ___35-[WFAction finishRunningWithError:]_block_invoke_3
- ___35-[WFAction finishRunningWithError:]_block_invoke_4
- ___39-[WFDatabase notifyResultsAboutChange:]_block_invoke.299
- ___39-[WFDatabase notifyResultsAboutChange:]_block_invoke.305
- ___39-[WFDatabase notifyResultsAboutChange:]_block_invoke_2.303
- ___39-[WFDatabase notifyResultsAboutChange:]_block_invoke_2.306
- ___42-[WFDatabase remoteChangeDebouncerDidFire]_block_invoke_2
- ___47-[WFLinkAction updateParameterSummaryIfNeeded:]_block_invoke_3
- ___48-[WFVariablePickerParameter initWithDefinition:]_block_invoke
- ___49-[WFDatabase(Shortcuts) applyConflictResolution:]_block_invoke.313
- ___56-[WFInterchangeManager performQueuedRequestIfApplicable]_block_invoke.211
- ___59-[WFLinkAction getContentDestinationWithCompletionHandler:]_block_invoke.346
- ___60-[WFLinkContentItemFilterAction runAsynchronouslyWithInput:]_block_invoke.192
- ___63-[WFDatabase(Shortcuts) localConflictingReferenceForReference:]_block_invoke
- ___64-[WFDatabase(Shortcuts) remoteConflictingReferenceForReference:]_block_invoke
- ___67-[WFDatabase(Shortcuts) createWorkflowWithIdentifier:record:error:]_block_invoke
- ___70-[WFLinkEntityContentItem generateFileRepresentation:options:forType:]_block_invoke.745
- ___73-[WFAppIntentExecutionAction enumeration:localizedLabelForPossibleState:]_block_invoke.404
- ___73-[WFLinkEntityContentItem generateObjectRepresentation:options:forClass:]_block_invoke.729
- ___81-[WFDatabase(Shortcuts) deleteReference:tombstone:deleteConflictIfPresent:error:]_block_invoke.281
- ___85-[WFResourceManager makeAccessResourcesAvailableWithUserInterface:completionHandler:]_block_invoke
- ___85-[WFResourceManager makeAccessResourcesAvailableWithUserInterface:completionHandler:]_block_invoke_2
- ___85-[WFResourceManager makeAccessResourcesAvailableWithUserInterface:completionHandler:]_block_invoke_3
- ___85-[WFResourceManager makeAccessResourcesAvailableWithUserInterface:completionHandler:]_block_invoke_4
- ___90-[WFInterchangeManager handleOpenURL:fromSourceApplication:errorHandler:postNotification:]_block_invoke_3
- ___90-[WFInterchangeManager handleOpenURL:fromSourceApplication:errorHandler:postNotification:]_block_invoke_4
- ___91-[WFAppIntentExecutionAction fetchMissingDisplayRepresentationValuesWithCompletionHandler:]_block_invoke.360
- ___91-[WFAppIntentExecutionAction fetchMissingDisplayRepresentationValuesWithCompletionHandler:]_block_invoke.368
- ___91-[WFAppIntentExecutionAction fetchMissingDisplayRepresentationValuesWithCompletionHandler:]_block_invoke_2.361
- ___91-[WFAppIntentExecutionAction fetchMissingDisplayRepresentationValuesWithCompletionHandler:]_block_invoke_2.370
- ___91-[WFAppIntentExecutionAction fetchMissingDisplayRepresentationValuesWithCompletionHandler:]_block_invoke_3.374
- ___94-[WFAppIntentExecutionAction postProcessToolKitProcessedValue:forParameter:completionHandler:]_block_invoke_3
- ___94-[WFAppIntentExecutionAction postProcessToolKitProcessedValue:forParameter:completionHandler:]_block_invoke_4
- ___AssistantServicesLibraryCore_block_invoke.54488
- ___Block_byref_object_copy_.10421
- ___Block_byref_object_copy_.10707
- ___Block_byref_object_copy_.11741
- ___Block_byref_object_copy_.12263
- ___Block_byref_object_copy_.12608
- ___Block_byref_object_copy_.13530
- ___Block_byref_object_copy_.15231
- ___Block_byref_object_copy_.16294
- ___Block_byref_object_copy_.18032
- ___Block_byref_object_copy_.18134
- ___Block_byref_object_copy_.19379
- ___Block_byref_object_copy_.20300
- ___Block_byref_object_copy_.20705
- ___Block_byref_object_copy_.20785
- ___Block_byref_object_copy_.22280
- ___Block_byref_object_copy_.24789
- ___Block_byref_object_copy_.25351
- ___Block_byref_object_copy_.26467
- ___Block_byref_object_copy_.27491
- ___Block_byref_object_copy_.29257
- ___Block_byref_object_copy_.30140
- ___Block_byref_object_copy_.3016
- ___Block_byref_object_copy_.31787
- ___Block_byref_object_copy_.35410
- ___Block_byref_object_copy_.35684
- ___Block_byref_object_copy_.37116
- ___Block_byref_object_copy_.37989
- ___Block_byref_object_copy_.41391
- ___Block_byref_object_copy_.42224
- ___Block_byref_object_copy_.42534
- ___Block_byref_object_copy_.43736
- ___Block_byref_object_copy_.46758
- ___Block_byref_object_copy_.46959
- ___Block_byref_object_copy_.48108
- ___Block_byref_object_copy_.4819
- ___Block_byref_object_copy_.49390
- ___Block_byref_object_copy_.49847
- ___Block_byref_object_copy_.5217
- ___Block_byref_object_copy_.54480
- ___Block_byref_object_copy_.56179
- ___Block_byref_object_copy_.57080
- ___Block_byref_object_copy_.57418
- ___Block_byref_object_copy_.58263
- ___Block_byref_object_copy_.59362
- ___Block_byref_object_copy_.59883
- ___Block_byref_object_copy_.61001
- ___Block_byref_object_copy_.61645
- ___Block_byref_object_copy_.62140
- ___Block_byref_object_copy_.6318
- ___Block_byref_object_copy_.64300
- ___Block_byref_object_copy_.64900
- ___Block_byref_object_copy_.65185
- ___Block_byref_object_copy_.66246
- ___Block_byref_object_copy_.68457
- ___Block_byref_object_copy_.70436
- ___Block_byref_object_copy_.71333
- ___Block_byref_object_copy_.72400
- ___Block_byref_object_copy_.73207
- ___Block_byref_object_copy_.7415
- ___Block_byref_object_copy_.74866
- ___Block_byref_object_copy_.8561
- ___Block_byref_object_copy_.9749
- ___Block_byref_object_copy_.9794
- ___Block_byref_object_dispose_.10422
- ___Block_byref_object_dispose_.10708
- ___Block_byref_object_dispose_.11742
- ___Block_byref_object_dispose_.12264
- ___Block_byref_object_dispose_.12609
- ___Block_byref_object_dispose_.13531
- ___Block_byref_object_dispose_.15232
- ___Block_byref_object_dispose_.16295
- ___Block_byref_object_dispose_.18033
- ___Block_byref_object_dispose_.18135
- ___Block_byref_object_dispose_.19380
- ___Block_byref_object_dispose_.20301
- ___Block_byref_object_dispose_.20706
- ___Block_byref_object_dispose_.20786
- ___Block_byref_object_dispose_.22281
- ___Block_byref_object_dispose_.24790
- ___Block_byref_object_dispose_.25352
- ___Block_byref_object_dispose_.26468
- ___Block_byref_object_dispose_.27492
- ___Block_byref_object_dispose_.29258
- ___Block_byref_object_dispose_.30141
- ___Block_byref_object_dispose_.3017
- ___Block_byref_object_dispose_.31788
- ___Block_byref_object_dispose_.35411
- ___Block_byref_object_dispose_.35685
- ___Block_byref_object_dispose_.37117
- ___Block_byref_object_dispose_.37990
- ___Block_byref_object_dispose_.41392
- ___Block_byref_object_dispose_.42225
- ___Block_byref_object_dispose_.42535
- ___Block_byref_object_dispose_.43737
- ___Block_byref_object_dispose_.46759
- ___Block_byref_object_dispose_.46960
- ___Block_byref_object_dispose_.48109
- ___Block_byref_object_dispose_.4820
- ___Block_byref_object_dispose_.49391
- ___Block_byref_object_dispose_.49848
- ___Block_byref_object_dispose_.5218
- ___Block_byref_object_dispose_.54481
- ___Block_byref_object_dispose_.56180
- ___Block_byref_object_dispose_.57081
- ___Block_byref_object_dispose_.57419
- ___Block_byref_object_dispose_.58264
- ___Block_byref_object_dispose_.59363
- ___Block_byref_object_dispose_.59884
- ___Block_byref_object_dispose_.61002
- ___Block_byref_object_dispose_.61646
- ___Block_byref_object_dispose_.62141
- ___Block_byref_object_dispose_.6319
- ___Block_byref_object_dispose_.64301
- ___Block_byref_object_dispose_.64901
- ___Block_byref_object_dispose_.65186
- ___Block_byref_object_dispose_.66247
- ___Block_byref_object_dispose_.68458
- ___Block_byref_object_dispose_.70437
- ___Block_byref_object_dispose_.71334
- ___Block_byref_object_dispose_.72401
- ___Block_byref_object_dispose_.73208
- ___Block_byref_object_dispose_.7416
- ___Block_byref_object_dispose_.74867
- ___Block_byref_object_dispose_.8562
- ___Block_byref_object_dispose_.9750
- ___Block_byref_object_dispose_.9795
- ___ContactsLibraryCore_block_invoke.32217
- ___ContactsLibraryCore_block_invoke.48012
- ___ContactsLibraryCore_block_invoke.54065
- ___ContactsLibraryCore_block_invoke.61786
- ___ContactsLibraryCore_block_invoke.66147
- ___ContactsLibraryCore_block_invoke.67257
- ___CoreLocationLibraryCore_block_invoke.41590
- ___CoreLocationLibraryCore_block_invoke.48034
- ___CoreLocationLibraryCore_block_invoke.59315
- ___CoreLocationLibraryCore_block_invoke.59981
- ___CoreLocationLibraryCore_block_invoke.62145
- ___CoreLocationLibraryCore_block_invoke.63931
- ___CoreLocationLibraryCore_block_invoke.66108
- ___HomeKitLibrary_block_invoke.1622
- ___HomeKitLibrary_block_invoke.2165
- ___HomeKitLibrary_block_invoke.28266
- ___HomeKitLibrary_block_invoke.35709
- ___HomeKitLibrary_block_invoke.36540
- ___HomeKitLibrary_block_invoke.38939
- ___HomeKitLibrary_block_invoke.56659
- ___HomeLibrary_block_invoke.28404
- ___HomeLibrary_block_invoke.35678
- ___HomeLibrary_block_invoke.38932
- ___HomeLibrary_block_invoke.4514
- ___MediaPlayerLibraryCore_block_invoke.37105
- ___MediaPlayerLibraryCore_block_invoke.53799
- ___PhotosLibraryCore_block_invoke.1535
- ___ReminderKitLibraryCore_block_invoke.25681
- ___RunningBoardServicesLibraryCore_block_invoke.27475
- ___SAObjectsLibrary_block_invoke.70756
- ___UIKitLibraryCore_block_invoke.41847
- ___UIKitLibrary_block_invoke.16305
- ___UIKitLibrary_block_invoke.22989
- ___UIKitLibrary_block_invoke.28671
- ___UIKitLibrary_block_invoke.29270
- ___UIKitLibrary_block_invoke.42548
- ___UIKitLibrary_block_invoke.49514
- ___UIKitLibrary_block_invoke.59024
- ___UIKitLibrary_block_invoke.61497
- ___UIKitLibrary_block_invoke.64595
- ___WFUpdateSmartPromptChangesToShortcutChanges_block_invoke.604
- ___block_descriptor_32_e40_B24?0"WFDatabaseObjectDescriptor"8^B16l
- ___block_descriptor_64_e8_32s40s48s56r_e9_v16?0^8ls32l8s40l8s48l8r56l8
- ___block_literal_global.10338
- ___block_literal_global.11013
- ___block_literal_global.1108
- ___block_literal_global.11273
- ___block_literal_global.11351
- ___block_literal_global.1161
- ___block_literal_global.1168
- ___block_literal_global.12270
- ___block_literal_global.12627
- ___block_literal_global.1264
- ___block_literal_global.13267
- ___block_literal_global.13320
- ___block_literal_global.13523
- ___block_literal_global.1366
- ___block_literal_global.13753
- ___block_literal_global.13878
- ___block_literal_global.14433
- ___block_literal_global.14516
- ___block_literal_global.14737
- ___block_literal_global.15688
- ___block_literal_global.15889
- ___block_literal_global.16299
- ___block_literal_global.1661
- ___block_literal_global.172.22618
- ___block_literal_global.1753
- ___block_literal_global.176.45838
- ___block_literal_global.178.29631
- ___block_literal_global.178.39842
- ___block_literal_global.178.69701
- ___block_literal_global.178.74883
- ___block_literal_global.179.26513
- ___block_literal_global.180.36451
- ___block_literal_global.18180
- ___block_literal_global.183.72411
- ___block_literal_global.183.74910
- ___block_literal_global.186.52471
- ___block_literal_global.186.72415
- ___block_literal_global.186.74911
- ___block_literal_global.18876
- ___block_literal_global.189.4503
- ___block_literal_global.189.45865
- ___block_literal_global.189.60457
- ___block_literal_global.189.60803
- ___block_literal_global.189.75175
- ___block_literal_global.18977
- ___block_literal_global.191.60804
- ___block_literal_global.191.72419
- ___block_literal_global.192.6309
- ___block_literal_global.19287
- ___block_literal_global.193.25359
- ___block_literal_global.193.29149
- ___block_literal_global.193.45868
- ___block_literal_global.193.66977
- ___block_literal_global.194.72402
- ___block_literal_global.19607
- ___block_literal_global.19722
- ___block_literal_global.199.18160
- ___block_literal_global.199.45114
- ___block_literal_global.199.57224
- ___block_literal_global.202.18157
- ___block_literal_global.202.21151
- ___block_literal_global.202.57006
- ___block_literal_global.203.46203
- ___block_literal_global.205.25335
- ___block_literal_global.206.60450
- ___block_literal_global.20680
- ___block_literal_global.208.49412
- ___block_literal_global.21175
- ___block_literal_global.213.53769
- ___block_literal_global.2142
- ___block_literal_global.219.68907
- ___block_literal_global.22081
- ___block_literal_global.225.26808
- ___block_literal_global.225.60434
- ___block_literal_global.22502
- ___block_literal_global.22689
- ___block_literal_global.227.74857
- ___block_literal_global.22787
- ___block_literal_global.2295
- ___block_literal_global.22985
- ___block_literal_global.230.41442
- ___block_literal_global.23048
- ___block_literal_global.232.43345
- ___block_literal_global.232.69382
- ___block_literal_global.23277
- ___block_literal_global.23460
- ___block_literal_global.239.74824
- ___block_literal_global.23987
- ___block_literal_global.247.37184
- ___block_literal_global.247.69378
- ___block_literal_global.24806
- ___block_literal_global.25094
- ___block_literal_global.251.55436
- ___block_literal_global.251.68481
- ___block_literal_global.25190
- ___block_literal_global.25317
- ___block_literal_global.25629
- ___block_literal_global.26193
- ___block_literal_global.26490
- ___block_literal_global.26798
- ___block_literal_global.27030
- ___block_literal_global.2706
- ___block_literal_global.27547
- ___block_literal_global.277.41373
- ___block_literal_global.277.47070
- ___block_literal_global.28255
- ___block_literal_global.283.11354
- ___block_literal_global.2859
- ___block_literal_global.28667
- ___block_literal_global.29160
- ___block_literal_global.2925
- ___block_literal_global.29260
- ___block_literal_global.29383
- ___block_literal_global.294.7895
- ___block_literal_global.29637
- ___block_literal_global.29796
- ___block_literal_global.299.76792
- ___block_literal_global.2998
- ___block_literal_global.30124
- ___block_literal_global.305.59028
- ___block_literal_global.306.14738
- ___block_literal_global.311.59115
- ___block_literal_global.31653
- ___block_literal_global.319.56188
- ___block_literal_global.33703
- ___block_literal_global.338.4783
- ___block_literal_global.34414
- ___block_literal_global.347.39584
- ___block_literal_global.348.41504
- ___block_literal_global.35448
- ___block_literal_global.357.41533
- ___block_literal_global.357.60296
- ___block_literal_global.35702
- ___block_literal_global.36000
- ___block_literal_global.3621
- ___block_literal_global.36447
- ___block_literal_global.36536
- ___block_literal_global.37021
- ___block_literal_global.37182
- ___block_literal_global.37386
- ___block_literal_global.37996
- ___block_literal_global.38913
- ___block_literal_global.393
- ___block_literal_global.39471
- ___block_literal_global.397.39557
- ___block_literal_global.39841
- ___block_literal_global.40662
- ___block_literal_global.41123
- ___block_literal_global.41441
- ___block_literal_global.41625
- ___block_literal_global.42259
- ___block_literal_global.42384
- ___block_literal_global.42541
- ___block_literal_global.42748
- ___block_literal_global.43372
- ___block_literal_global.43901
- ___block_literal_global.4403
- ___block_literal_global.44073
- ___block_literal_global.44399
- ___block_literal_global.44478
- ___block_literal_global.45117
- ___block_literal_global.4530
- ___block_literal_global.454.33639
- ___block_literal_global.45589
- ___block_literal_global.457.7423
- ___block_literal_global.45847
- ___block_literal_global.46197
- ___block_literal_global.46246
- ___block_literal_global.46325
- ___block_literal_global.469.67822
- ___block_literal_global.47060
- ___block_literal_global.47114
- ___block_literal_global.47370
- ___block_literal_global.477.67823
- ___block_literal_global.478
- ___block_literal_global.48128
- ___block_literal_global.482
- ___block_literal_global.4868
- ___block_literal_global.49169
- ___block_literal_global.49380
- ___block_literal_global.49507
- ___block_literal_global.4958
- ___block_literal_global.49697
- ___block_literal_global.49792
- ___block_literal_global.50058
- ___block_literal_global.50971
- ___block_literal_global.50996
- ___block_literal_global.51635
- ___block_literal_global.51645
- ___block_literal_global.5178
- ___block_literal_global.52276
- ___block_literal_global.52470
- ___block_literal_global.52806
- ___block_literal_global.52867
- ___block_literal_global.53768
- ___block_literal_global.54070
- ___block_literal_global.5424
- ___block_literal_global.54476
- ___block_literal_global.54763
- ___block_literal_global.54819
- ___block_literal_global.55434
- ___block_literal_global.55624
- ___block_literal_global.56100
- ___block_literal_global.56288
- ___block_literal_global.5644
- ___block_literal_global.56655
- ___block_literal_global.57087
- ___block_literal_global.57223
- ___block_literal_global.57709
- ___block_literal_global.57919
- ___block_literal_global.59168
- ___block_literal_global.59303
- ___block_literal_global.599
- ___block_literal_global.60468
- ___block_literal_global.60802
- ___block_literal_global.61107
- ___block_literal_global.61360
- ___block_literal_global.61490
- ___block_literal_global.61684
- ___block_literal_global.61748
- ___block_literal_global.6306
- ___block_literal_global.6372
- ___block_literal_global.63803
- ___block_literal_global.63881
- ___block_literal_global.64192
- ___block_literal_global.64588
- ___block_literal_global.65508
- ___block_literal_global.66125
- ___block_literal_global.66986
- ___block_literal_global.67244
- ___block_literal_global.6727
- ___block_literal_global.67282
- ___block_literal_global.67657
- ___block_literal_global.67981
- ___block_literal_global.68225
- ___block_literal_global.68540
- ___block_literal_global.68906
- ___block_literal_global.692
- ___block_literal_global.69395
- ___block_literal_global.69472
- ___block_literal_global.69545
- ___block_literal_global.69706
- ___block_literal_global.70052
- ___block_literal_global.701
- ___block_literal_global.703.43082
- ___block_literal_global.70433
- ___block_literal_global.70751
- ___block_literal_global.70918
- ___block_literal_global.71267
- ___block_literal_global.71672
- ___block_literal_global.72178
- ___block_literal_global.72431
- ___block_literal_global.731
- ___block_literal_global.73226
- ___block_literal_global.735
- ___block_literal_global.738
- ___block_literal_global.74654
- ___block_literal_global.74881
- ___block_literal_global.75196
- ___block_literal_global.752
- ___block_literal_global.755
- ___block_literal_global.75898
- ___block_literal_global.7606
- ___block_literal_global.76804
- ___block_literal_global.7923
- ___block_literal_global.804
- ___block_literal_global.8273
- ___block_literal_global.8795
- ___block_literal_global.9027
- ___block_literal_global.931
- ___block_literal_global.9443
- ___block_literal_global.9707
- ___getCLPlacemarkClass_block_invoke.59979
- ___getCLPlacemarkClass_block_invoke.62143
- ___getCLPlacemarkClass_block_invoke.66106
- ___getCNContactStoreClass_block_invoke.67246
- ___getMPMediaItemClass_block_invoke.53785
- ___getMPMediaPropertyPredicateClass_block_invoke.37074
- ___getMPMediaPropertyPredicateClass_block_invoke.53783
- ___getMPMediaQueryClass_block_invoke.37077
- ___getMPMediaQueryClass_block_invoke.53788
- __mutableRegisteredDefinitions.69480
- _audit_stringAssistantServices.54503
- _audit_stringContacts.32231
- _audit_stringContacts.48026
- _audit_stringContacts.54068
- _audit_stringContacts.61790
- _audit_stringContacts.66150
- _audit_stringContacts.67263
- _audit_stringCoreLocation.41605
- _audit_stringCoreLocation.48038
- _audit_stringCoreLocation.59318
- _audit_stringCoreLocation.59995
- _audit_stringCoreLocation.62159
- _audit_stringCoreLocation.63944
- _audit_stringCoreLocation.66122
- _audit_stringMediaPlayer.37111
- _audit_stringMediaPlayer.53805
- _audit_stringPhotos.1541
- _audit_stringReminderKit.25687
- _audit_stringRunningBoardServices.27478
- _audit_stringUIKit.41861
- _classHFTriggerActionSetsBuilder.35674
- _classHFTriggerActionSetsBuilder.38928
- _classRegistrationLock.52183
- _classRegistrationLock.72793
- _classRegistrationLock.9225
- _classUIPasteboard.42553
- _classUIPasteboard.49509
- _classUIPasteboard.61492
- _classUIPasteboard.64590
- _constantHMCharacteristicMetadataFormatBool.2208
- _constantHMCharacteristicMetadataFormatBool.28279
- _constantHMCharacteristicMetadataFormatFloat.2188
- _constantHMCharacteristicMetadataFormatInt.2195
- _constantHMCharacteristicMetadataFormatInt.28390
- _constantHMCharacteristicMetadataFormatString.2201
- _constantHMCharacteristicMetadataFormatUInt16.2176
- _constantHMCharacteristicMetadataFormatUInt32.2169
- _constantHMCharacteristicMetadataFormatUInt64.2161
- _constantHMCharacteristicMetadataFormatUInt8.2182
- _constantHMCharacteristicMetadataFormatUInt8.28397
- _getCLPlacemarkClass.66041
- _getCLPlacemarkClass.softClass.59978
- _getCLPlacemarkClass.softClass.62142
- _getCLPlacemarkClass.softClass.66105
- _getCNContactStoreClass.softClass.67245
- _getHFTriggerActionSetsBuilderClass.35662
- _getHFTriggerActionSetsBuilderClass.38923
- _getHMCharacteristicMetadataFormatBool.2147
- _getHMCharacteristicMetadataFormatBool.28274
- _getHMCharacteristicMetadataFormatFloat.2150
- _getHMCharacteristicMetadataFormatInt.2149
- _getHMCharacteristicMetadataFormatInt.28385
- _getHMCharacteristicMetadataFormatString.2148
- _getHMCharacteristicMetadataFormatUInt16.2152
- _getHMCharacteristicMetadataFormatUInt32.2153
- _getHMCharacteristicMetadataFormatUInt64.2154
- _getHMCharacteristicMetadataFormatUInt8.2151
- _getHMCharacteristicMetadataFormatUInt8.28384
- _getMPMediaItemClass.softClass.53784
- _getMPMediaPropertyPredicateClass.softClass.37073
- _getMPMediaPropertyPredicateClass.softClass.53782
- _getMPMediaQueryClass.softClass.37076
- _getMPMediaQueryClass.softClass.53787
- _getUIPasteboardClass.42538
- _getUIPasteboardClass.49503
- _getUIPasteboardClass.61483
- _getUIPasteboardClass.64583
- _initHFTriggerActionSetsBuilder.35671
- _initHFTriggerActionSetsBuilder.38925
- _initHMCharacteristicMetadataFormatBool.2205
- _initHMCharacteristicMetadataFormatBool.28276
- _initHMCharacteristicMetadataFormatFloat.2186
- _initHMCharacteristicMetadataFormatInt.2192
- _initHMCharacteristicMetadataFormatInt.28387
- _initHMCharacteristicMetadataFormatString.2199
- _initHMCharacteristicMetadataFormatUInt16.2173
- _initHMCharacteristicMetadataFormatUInt32.2167
- _initHMCharacteristicMetadataFormatUInt64.2156
- _initHMCharacteristicMetadataFormatUInt8.2180
- _initHMCharacteristicMetadataFormatUInt8.28394
- _initUIPasteboard.42551
- _initUIPasteboard.49505
- _initUIPasteboard.61488
- _initUIPasteboard.64586
- _nw_parameters_set_include_peer_to_peer
- _objc_msgSend$collectionIdentifier
- _objc_msgSend$hasDeltaFromOriginal
- _objc_msgSend$hasDeltaFromOther
- _objc_msgSend$hasValidLibrary
- _objc_msgSend$hiddenInComplication
- _objc_msgSend$makeAccessResourcesAvailableWithUserInterface:completionHandler:
- _objc_msgSend$reloadLibrary
- _objc_msgSend$setCollectionIdentifier:
- _objc_msgSend$setLibrary:
- _rediscoverDefinitionsIfNeeded.calledDefinitionVendingSelectors.69473
- _rediscoverDefinitionsIfNeeded.lock.69475
- _rediscoverDefinitionsIfNeeded.onceToken.69471
- _sharedInstance.onceToken.12626
- _sharedInstance.onceToken.59167
- _sharedInstance.onceToken.9026
- _sharedManager.onceToken.1660
- _sharedManager.onceToken.60816
- _sharedManager.onceToken.68539
- _sharedManager.sharedManager.60817
- _sharedManager.sharedManager.68541
- _sharedRegistry.onceToken.16485
- _sharedRegistry.onceToken.25388
- _sharedRegistry.sharedRegistry.16486
- _sharedRegistry.sharedRegistry.25389
CStrings:
+ "%s Action is not running during the completion of a UI presentation request, returning with user cancelled error"
+ "%s Failed to process all parameters when updating parameter summary, this is not an fatal error continuing %@"
+ "%s No completionQueue provided to if_enumerateAsynchronouslyInSequence"
+ "%s Not opening file-based URL in response to success/cancellation: %@"
+ "%s URL cannot be used as failure handler, bailing out."
+ "%s URL cannot be used as success/cancellation handler: %@"
+ "%s URLRepresentable entity export did not produce a URL"
+ "%s Unable to create connection for URL export: %@"
+ "%s Unable to export URLRepresentable entity as URL: %@"
+ "%s Unable to make LNValue from %@ because %@ doesn't accept it"
+ "%s Unable to remove invalid access resource permissions: %{public}@"
+ "%s Unable to remove invalid smart prompt permissions: %{public}@"
+ "-[WFAction _finishRunningWithError:]"
+ "-[WFAppIntentExecutionAction postProcessToolKitProcessedValue:forParameter:completionHandler:]_block_invoke"
+ "-[WFDatabase library]"
+ "-[WFDatabase removePermissionsWithoutAssociatedShortcuts]_block_invoke"
+ "-[WFDatabase saveLibraryToDatabase]"
+ "-[WFInterchangeManager handleOpenURL:fromSourceApplication:errorHandler:postNotification:]_block_invoke"
+ "-[WFInterchangeManager handleOpenURL:fromSourceApplication:errorHandler:postNotification:]_block_invoke_2"
+ "-[WFLinkAction updateParameterSummaryIfNeeded:]_block_invoke_2"
+ "-[WFResourceManager makeAccessResourcesAvailableWithUserInterface:completionQueue:completionHandler:]"
+ "@\"WFLibrary\"16@?0^@8"
+ "@56@0:8@16@24@32@40^@48"
+ "Background Color"
+ "Background Color (WFQRBackgroundColor)"
+ "Fetched authorizations are older than local, will ignore them and overwrite them with local."
+ "Foreground Color"
+ "Foreground Color (WFQRForegroundColor)"
+ "Found conflict for workflow with identifier %{public}s"
+ "Local WFWorkflowRecord with identifier %{public}s has the same recordChangeTag as fetched record, this is likely our own change, discarding it."
+ "Remote record modification date %s is not greater than local record modification date %s"
+ "Request…"
+ "Rounded"
+ "Rounded (WFQRRounded)"
+ "Send ${WFSendEmailActionInputAttachments} as ${WFSendEmailActionSubject} to ${WFSendEmailActionToRecipients} (Parameter Summary)"
+ "Send ${WFSendEmailActionInputAttachments} with ${WFSendEmailActionSubject} to ${WFSendEmailActionToRecipients}"
+ "ShortcutSync"
+ "T@\"NSObject<OS_dispatch_queue>\",&,N,V_completionQueue"
+ "T@\"NSString\",C,N,V_folderIdentifier"
+ "TQ,N,R,VresultType"
+ "Tq,N,V_lastLoadedLibrarySyncHash"
+ "Visual Intelligence Unavailable"
+ "Visual Intelligence is not currently available."
+ "WFDatabaseFetchedRecordResult"
+ "WFLinkCalculateAppUsageIntentAction"
+ "WFQRBackgroundColor"
+ "WFQRForegroundColor"
+ "WorkflowKit.WFDatabaseFetchedRecordResult"
+ "_TtC11WorkflowKit46WFVisualIntelligenceCameraAvailabilityResource"
+ "_completionQueue"
+ "_finishRunningWithError:"
+ "_folderIdentifier"
+ "_lastLoadedLibrarySyncHash"
+ "allowCreatingConflicts"
+ "completionQueue"
+ "equal change tag"
+ "get latest library"
+ "handle fetched workflow record"
+ "handleFetchedWorkflowRecord:identifier:recordChangeTag:modificationDate:error:"
+ "hasWorkflowWithID:"
+ "hourglass"
+ "if_enumerateAsynchronouslyOnQueue:block:completionHandler:"
+ "import questions"
+ "initWithResultType:reason:"
+ "isVisualIntelligenceEnabled"
+ "lastLoadedLibrarySyncHash"
+ "makeAccessResourcesAvailableWithUserInterface:completionQueue:completionHandler:"
+ "mergeChangesFrom:into:"
+ "public.url"
+ "reasonsForConflictWithLocalWorkflow:remoteWorkflow:"
+ "recordChangeTag"
+ "remove extra permissions"
+ "removePermissionsWithoutAssociatedShortcuts"
+ "setCompletionQueue:"
+ "setFolderIdentifier:"
+ "setLastLoadedLibrarySyncHash:"
+ "stale modification date"
+ "wf_isAllowedInXCallback"
- "%s Action is not running during the completion of a UI presentation request, returning"
- "%s Found existing library in CoreData, attempting to merge"
- "%s Merge result: deltaFromOther: %@, deltaFromOriginal: %@"
- "%s Not opening file-based URL in response to success: %@"
- "%s There's no existing Core Data library, attempting to save library"
- "-[WFAction finishRunningWithError:]"
- "-[WFDatabase reloadLibrary]_block_invoke"
- "-[WFDatabase(Library) saveLibraryToDatabase]"
- "-[WFInterchangeManager handleOpenURL:fromSourceApplication:errorHandler:postNotification:]_block_invoke_4"
- "B24@?0@\"WFDatabaseObjectDescriptor\"8^B16"
- "Calling latestLibrary on WFDatabase is only supported when the Coherence Library feature flag is on"
- "Send ${WFSendEmailActionInputAttachments} to ${WFSendEmailActionToRecipients} as ${WFSendEmailActionSubject} (Parameter Summary)"
- "Send ${WFSendEmailActionInputAttachments} to ${WFSendEmailActionToRecipients} with ${WFSendEmailActionSubject}"
- "T@\"NSString\",C,N,V_collectionIdentifier"
- "WFConflictResolutionEnabled"
- "WFDatabase+Library.m"
- "_collectionIdentifier"
- "conflictResolutionEnabled"
- "create workflow with identifier"
- "createWorkflowWithIdentifier:record:error:"
- "getting local conflict for shortcut"
- "getting remote conflict for shortcut"
- "hasValidLibrary"
- "isEquivalentForSyncTo:"
- "localConflictingReferenceForReference:"
- "reloadLibrary"
- "reloading library"
- "remoteConflictingReferenceForReference:"
- "setCollectionIdentifier:"
- "wipeAllLibrariesWithError:"

```
