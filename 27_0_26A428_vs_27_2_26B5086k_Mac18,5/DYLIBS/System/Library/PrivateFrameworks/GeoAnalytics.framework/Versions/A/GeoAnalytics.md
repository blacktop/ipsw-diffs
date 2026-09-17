## GeoAnalytics

> `/System/Library/PrivateFrameworks/GeoAnalytics.framework/Versions/A/GeoAnalytics`

```diff

-2075.20.6.12.12
-  __TEXT.__text: 0x9b214
-  __TEXT.__objc_methlist: 0x249c
-  __TEXT.__const: 0x724
+2075.21.6.17.9
+  __TEXT.__text: 0x9ccb8
+  __TEXT.__objc_methlist: 0x2624
+  __TEXT.__const: 0x72c
   __TEXT.__dlopen_cstrs: 0x54
   __TEXT.__swift5_typeref: 0x4e
   __TEXT.__swift5_capture: 0x24

   __TEXT.__swift5_fieldmd: 0x44
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_types: 0x8
-  __TEXT.__gcc_except_tab: 0x5b0
-  __TEXT.__cstring: 0xeaf8
+  __TEXT.__gcc_except_tab: 0x5ec
+  __TEXT.__cstring: 0xecb3
   __TEXT.__oslogstring: 0xe6d
-  __TEXT.__unwind_info: 0x12f8
+  __TEXT.__unwind_info: 0x1358
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x7118
-  __DATA_CONST.__objc_classlist: 0x108
+  __DATA_CONST.__const: 0x71f0
+  __DATA_CONST.__objc_classlist: 0x120
   __DATA_CONST.__objc_catlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x60
+  __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3fe0
+  __DATA_CONST.__objc_selrefs: 0x41d8
   __DATA_CONST.__objc_protorefs: 0x20
-  __DATA_CONST.__objc_superrefs: 0xa0
-  __DATA_CONST.__objc_arraydata: 0xe50
-  __DATA_CONST.__got: 0x690
-  __AUTH_CONST.__const: 0x4008
-  __AUTH_CONST.__cfstring: 0x144c0
-  __AUTH_CONST.__objc_const: 0x2da8
-  __AUTH_CONST.__objc_intobj: 0x1cb0
+  __DATA_CONST.__objc_superrefs: 0xb8
+  __DATA_CONST.__objc_arraydata: 0xe78
+  __DATA_CONST.__got: 0x6b8
+  __AUTH_CONST.__const: 0x40f8
+  __AUTH_CONST.__cfstring: 0x146c0
+  __AUTH_CONST.__objc_const: 0x32c8
+  __AUTH_CONST.__objc_intobj: 0x1d88
   __AUTH_CONST.__objc_dictobj: 0x4b0
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH_CONST.__objc_arrayobj: 0x360
   __AUTH_CONST.__auth_got: 0x3d0
-  __AUTH.__objc_data: 0x140
+  __AUTH.__objc_data: 0x230
   __AUTH.__data: 0x40
-  __DATA.__objc_ivar: 0x1c4
-  __DATA.__data: 0x490
+  __DATA.__objc_ivar: 0x1f0
+  __DATA.__data: 0x550
   __DATA.__common: 0x8
   __DATA_DIRTY.__objc_data: 0x910
   __DATA_DIRTY.__data: 0x10
-  __DATA_DIRTY.__bss: 0x1d8
+  __DATA_DIRTY.__bss: 0x1d0
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/PrivateFrameworks/GeoServices.framework/Versions/A/GeoServices

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 1599
-  Symbols:   5016
-  CStrings:  2770
+  Functions: 1629
+  Symbols:   5162
+  CStrings:  2789
 
Symbols:
+ +[GEOAPPortal capturePeriodicSettingsWithMapSettings:mapUiShown:mapsFeatures:mapsUserSettings:routingSettings:widgetConfiguration:]
+ +[GEOAPPortal capturePeriodicSettingsWithMapSettings:mapUiShown:mapsFeatures:mapsUserSettings:routingSettings:widgetConfiguration:additionalStates:providedDropRate:completionQueue:completionBlock:]
+ +[GEOAPPortal captureShowcaseSuppressionWithBusinessId:localSearchProviderID:showcaseId:suppressionReason:adamId:multipleShowcaseMetadatas:]
+ +[GEOAPPortal captureShowcaseSuppressionWithBusinessId:localSearchProviderID:showcaseId:suppressionReason:adamId:multipleShowcaseMetadatas:additionalStates:providedDropRate:completionQueue:completionBlock:]
+ +[GEOAPPortal(Extras) captureShowcaseSuppressionEventWithBusinessId:localSearchProviderID:showcaseId:adamId:suppressionReason:multipleShowcaseMetadata:]
+ -[GEOAPEphemeralWidgetPropertiesStateStore displayHeight]
+ -[GEOAPEphemeralWidgetPropertiesStateStore displayWidth]
+ -[GEOAPEphemeralWidgetPropertiesStateStore family]
+ -[GEOAPEphemeralWidgetPropertiesStateStore initWithIsPreview:family:displayWidth:displayHeight:]
+ -[GEOAPEphemeralWidgetPropertiesStateStore isPreview]
+ -[GEOAPEphemeralWidgetTimelineEntriesStateStore .cxx_destruct]
+ -[GEOAPEphemeralWidgetTimelineEntriesStateStore enumerateEntriesWith:]
+ -[GEOAPEphemeralWidgetTimelineEntriesStateStore initWithEntries:]
+ -[GEOAPSharedStateData _consumeWidgetConfiguration]
+ -[GEOAPSharedStateData performWidgetConfigurationUpdate:]
+ -[GEOAPUserActionDataModelInfoProviders initWithWidgetPropertiesProvider:]
+ -[GEOAPUserActionDataModelInfoProviders initWithWidgetPropertiesProvider:widgetTimelineEntriesProvider:]
+ -[GEOAPUserActionDataModelInfoProviders initWithWidgetTimelineEntriesProvider:]
+ -[GEOAPUserActionDataModelInfoProviders widgetPropertiesDataModelProvider]
+ -[GEOAPUserActionDataModelInfoProviders widgetTimelineEntriesDataModelProvider]
+ -[GEOAPUserActionDataModelInfoProviders(Internal) widgetPropertiesState]
+ -[GEOAPUserActionDataModelInfoProviders(Internal) widgetTimelineEntriesState]
+ -[GEOAPWidgetTimelineEntryInfo content]
+ -[GEOAPWidgetTimelineEntryInfo hasRelevance]
+ -[GEOAPWidgetTimelineEntryInfo initWithContent:]
+ -[GEOAPWidgetTimelineEntryInfo initWithContent:relevance:]
+ -[GEOAPWidgetTimelineEntryInfo relevance]
+ GCC_except_table1050
+ GCC_except_table1053
+ GCC_except_table1058
+ GCC_except_table1060
+ GCC_except_table1165
+ GCC_except_table1194
+ GCC_except_table1196
+ GCC_except_table1214
+ GCC_except_table1218
+ GCC_except_table1220
+ GCC_except_table1222
+ GCC_except_table1435
+ GCC_except_table1473
+ GCC_except_table563
+ GCC_except_table567
+ GCC_except_table569
+ GCC_except_table572
+ GCC_except_table575
+ GCC_except_table578
+ GCC_except_table583
+ GCC_except_table585
+ GCC_except_table594
+ GCC_except_table597
+ GCC_except_table600
+ GCC_except_table649
+ GCC_except_table656
+ GCC_except_table665
+ OBJC_IVAR_$_GEOAPEphemeralWidgetPropertiesStateStore._displayHeight
+ OBJC_IVAR_$_GEOAPEphemeralWidgetPropertiesStateStore._displayWidth
+ OBJC_IVAR_$_GEOAPEphemeralWidgetPropertiesStateStore._family
+ OBJC_IVAR_$_GEOAPEphemeralWidgetPropertiesStateStore._isPreview
+ OBJC_IVAR_$_GEOAPEphemeralWidgetTimelineEntriesStateStore._entries
+ OBJC_IVAR_$_GEOAPSharedStateData._widgetConfigurationStateIso
+ OBJC_IVAR_$_GEOAPUserActionDataModelInfoProviders._widgetPropertiesProvider
+ OBJC_IVAR_$_GEOAPUserActionDataModelInfoProviders._widgetTimelineEntriesProvider
+ OBJC_IVAR_$_GEOAPWidgetTimelineEntryInfo._content
+ OBJC_IVAR_$_GEOAPWidgetTimelineEntryInfo._hasRelevance
+ OBJC_IVAR_$_GEOAPWidgetTimelineEntryInfo._relevance
+ _GeoAnalyticsConfig_AllowedCountriesForEnrichedResultsCount_Metadata_block_invoke_64
+ _GeoAnalyticsConfig_B74FC90_enabled_Metadata_block_invoke_67
+ _GeoAnalyticsConfig_GeoShifterObfuscationSeedIN_Metadata_block_invoke_66
+ _GeoAnalyticsConfig_LastMetroAssetCatalogDownload_Metadata_block_invoke_72
+ _GeoAnalyticsConfig_LocIntActiveBatchID_Metadata_block_invoke_68
+ _GeoAnalyticsConfig_LocIntSeqNo_Metadata_block_invoke_69
+ _GeoAnalyticsConfig_MetroAssetCatalogCheckInterval_Metadata_block_invoke_73
+ _GeoAnalyticsConfig_TrafficShiftingINEnabled_Metadata_block_invoke_65
+ _GeoAnalyticsConfig_UseriCloudAccountAvailable_Metadata_block_invoke_60
+ _GeoAnalyticsConfig_WidgetConfigurationMaxCountPerFamily
+ _GeoAnalyticsConfig_WidgetConfigurationMaxCountPerFamily_Metadata
+ _GeoAnalyticsConfig_WidgetConfigurationMaxCountPerFamily_Metadata_block_invoke_59
+ _GeoAnalyticsConfig__debug_AlwaysUseExpensiveUpload_Metadata_block_invoke_61
+ _GeoAnalyticsConfig__debug_CancelInflightUploads_Metadata_block_invoke_75
+ _GeoAnalyticsConfig__debug_KeepUploadFiles_Metadata_block_invoke_62
+ _GeoAnalyticsConfig__debug_NoMobileAssetPreloader_Metadata_block_invoke_76
+ _GeoAnalyticsConfig__debug_NoUploader_Metadata_block_invoke_74
+ _GeoAnalyticsConfig__debug_UploadCountersEnabled_Metadata_block_invoke_63
+ _GeoAnalyticsConfig__debug_simulateFileWriteError_Metadata_block_invoke_71
+ _GeoAnalyticsConfig__debug_simulateNoURLs_Metadata_block_invoke_70
+ _GeoAnalyticsStateConfig_widgetProperties_stateDisabled
+ _GeoAnalyticsStateConfig_widgetProperties_stateDisabled_Metadata
+ _GeoAnalyticsStateConfig_widgetProperties_stateDisabled_Metadata_block_invoke_71
+ _GeoAnalyticsStateConfig_widgetTimelineEntries_stateDisabled
+ _GeoAnalyticsStateConfig_widgetTimelineEntries_stateDisabled_Metadata
+ _GeoAnalyticsStateConfig_widgetTimelineEntries_stateDisabled_Metadata_block_invoke_72
+ _OBJC_CLASS_$_GEOAPEphemeralWidgetPropertiesStateStore
+ _OBJC_CLASS_$_GEOAPEphemeralWidgetTimelineEntriesStateStore
+ _OBJC_CLASS_$_GEOAPWidgetTimelineEntryInfo
+ _OBJC_CLASS_$_GEODisplaySize
+ _OBJC_CLASS_$_GEOLogMsgStateWidgetConfiguration
+ _OBJC_CLASS_$_GEOLogMsgStateWidgetProperties
+ _OBJC_CLASS_$_GEOLogMsgStateWidgetTimelineEntries
+ _OBJC_CLASS_$_GEOWidgetTimelineEntry
+ _OBJC_METACLASS_$_GEOAPEphemeralWidgetPropertiesStateStore
+ _OBJC_METACLASS_$_GEOAPEphemeralWidgetTimelineEntriesStateStore
+ _OBJC_METACLASS_$_GEOAPWidgetTimelineEntryInfo
+ __197+[GEOAPPortal capturePeriodicSettingsWithMapSettings:mapUiShown:mapsFeatures:mapsUserSettings:routingSettings:widgetConfiguration:additionalStates:providedDropRate:completionQueue:completionBlock:]_block_invoke
+ __206+[GEOAPPortal captureShowcaseSuppressionWithBusinessId:localSearchProviderID:showcaseId:suppressionReason:adamId:multipleShowcaseMetadatas:additionalStates:providedDropRate:completionQueue:completionBlock:]_block_invoke
+ __OBJC_$_INSTANCE_METHODS_GEOAPEphemeralWidgetPropertiesStateStore
+ __OBJC_$_INSTANCE_METHODS_GEOAPEphemeralWidgetTimelineEntriesStateStore
+ __OBJC_$_INSTANCE_METHODS_GEOAPWidgetTimelineEntryInfo
+ __OBJC_$_INSTANCE_VARIABLES_GEOAPEphemeralWidgetPropertiesStateStore
+ __OBJC_$_INSTANCE_VARIABLES_GEOAPEphemeralWidgetTimelineEntriesStateStore
+ __OBJC_$_INSTANCE_VARIABLES_GEOAPWidgetTimelineEntryInfo
+ __OBJC_$_PROP_LIST_GEOAPEphemeralWidgetPropertiesStateStore
+ __OBJC_$_PROP_LIST_GEOAPEphemeralWidgetTimelineEntriesStateStore
+ __OBJC_$_PROP_LIST_GEOAPUserActionWidgetPropertiesDataModelProviding
+ __OBJC_$_PROP_LIST_GEOAPWidgetTimelineEntryInfo
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_GEOAPUserActionWidgetPropertiesDataModelProviding
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_GEOAPUserActionWidgetTimelineEntriesDataModelProviding
+ __OBJC_$_PROTOCOL_METHOD_TYPES_GEOAPUserActionWidgetPropertiesDataModelProviding
+ __OBJC_$_PROTOCOL_METHOD_TYPES_GEOAPUserActionWidgetTimelineEntriesDataModelProviding
+ __OBJC_$_PROTOCOL_REFS_GEOAPUserActionWidgetPropertiesDataModelProviding
+ __OBJC_$_PROTOCOL_REFS_GEOAPUserActionWidgetTimelineEntriesDataModelProviding
+ __OBJC_CLASS_PROTOCOLS_$_GEOAPEphemeralWidgetPropertiesStateStore
+ __OBJC_CLASS_PROTOCOLS_$_GEOAPEphemeralWidgetTimelineEntriesStateStore
+ __OBJC_CLASS_RO_$_GEOAPEphemeralWidgetPropertiesStateStore
+ __OBJC_CLASS_RO_$_GEOAPEphemeralWidgetTimelineEntriesStateStore
+ __OBJC_CLASS_RO_$_GEOAPWidgetTimelineEntryInfo
+ __OBJC_LABEL_PROTOCOL_$_GEOAPUserActionWidgetPropertiesDataModelProviding
+ __OBJC_LABEL_PROTOCOL_$_GEOAPUserActionWidgetTimelineEntriesDataModelProviding
+ __OBJC_METACLASS_RO_$_GEOAPEphemeralWidgetPropertiesStateStore
+ __OBJC_METACLASS_RO_$_GEOAPEphemeralWidgetTimelineEntriesStateStore
+ __OBJC_METACLASS_RO_$_GEOAPWidgetTimelineEntryInfo
+ __OBJC_PROTOCOL_$_GEOAPUserActionWidgetPropertiesDataModelProviding
+ __OBJC_PROTOCOL_$_GEOAPUserActionWidgetTimelineEntriesDataModelProviding
+ ___197+[GEOAPPortal capturePeriodicSettingsWithMapSettings:mapUiShown:mapsFeatures:mapsUserSettings:routingSettings:widgetConfiguration:additionalStates:providedDropRate:completionQueue:completionBlock:]_block_invoke
+ ___206+[GEOAPPortal captureShowcaseSuppressionWithBusinessId:localSearchProviderID:showcaseId:suppressionReason:adamId:multipleShowcaseMetadatas:additionalStates:providedDropRate:completionQueue:completionBlock:]_block_invoke
+ ___51-[GEOAPSharedStateData _consumeWidgetConfiguration]_block_invoke
+ ___57-[GEOAPSharedStateData performWidgetConfigurationUpdate:]_block_invoke
+ ___57-[GEOAPSharedStateData performWidgetConfigurationUpdate:]_block_invoke_2
+ ___77-[GEOAPUserActionDataModelInfoProviders(Internal) widgetTimelineEntriesState]_block_invoke
+ ___block_descriptor_44_e8_32s_e11_v16?0i8I12l
+ ___block_descriptor_48_e8_32s40r_e14_B20?0i8B12f16l
+ ___block_descriptor_52_e8_32s40bs_e5_v8?0l
+ _objc_msgSend$_consumeWidgetConfiguration
+ _objc_msgSend$accessoryCircular
+ _objc_msgSend$accessoryCorner
+ _objc_msgSend$accessoryInline
+ _objc_msgSend$accessoryRectangular
+ _objc_msgSend$addEntries:
+ _objc_msgSend$capturePeriodicSettingsWithMapSettings:mapUiShown:mapsFeatures:mapsUserSettings:routingSettings:widgetConfiguration:additionalStates:providedDropRate:completionQueue:completionBlock:
+ _objc_msgSend$captureShowcaseSuppressionEventWithBusinessId:localSearchProviderID:showcaseId:adamId:suppressionReason:multipleShowcaseMetadata:
+ _objc_msgSend$captureShowcaseSuppressionWithBusinessId:localSearchProviderID:showcaseId:suppressionReason:adamId:multipleShowcaseMetadatas:additionalStates:providedDropRate:completionQueue:completionBlock:
+ _objc_msgSend$displayHeight
+ _objc_msgSend$displayWidth
+ _objc_msgSend$enumerateEntriesWith:
+ _objc_msgSend$extraLarge
+ _objc_msgSend$extraLargePortrait
+ _objc_msgSend$family
+ _objc_msgSend$hasAccessoryCircular
+ _objc_msgSend$hasAccessoryCorner
+ _objc_msgSend$hasAccessoryInline
+ _objc_msgSend$hasAccessoryRectangular
+ _objc_msgSend$hasExtraLarge
+ _objc_msgSend$hasExtraLargePortrait
+ _objc_msgSend$hasLarge
+ _objc_msgSend$hasMedium
+ _objc_msgSend$hasRelevance
+ _objc_msgSend$hasSmall
+ _objc_msgSend$isPreview
+ _objc_msgSend$large
+ _objc_msgSend$medium
+ _objc_msgSend$relevance
+ _objc_msgSend$setAccessoryCircular:
+ _objc_msgSend$setAccessoryCorner:
+ _objc_msgSend$setAccessoryInline:
+ _objc_msgSend$setAccessoryRectangular:
+ _objc_msgSend$setDisplaySize:
+ _objc_msgSend$setExtraLarge:
+ _objc_msgSend$setExtraLargePortrait:
+ _objc_msgSend$setFamily:
+ _objc_msgSend$setHeight:
+ _objc_msgSend$setIsPreview:
+ _objc_msgSend$setLarge:
+ _objc_msgSend$setMedium:
+ _objc_msgSend$setMultipleShowcaseMetadatas:
+ _objc_msgSend$setRelevance:
+ _objc_msgSend$setSmall:
+ _objc_msgSend$setWidgetConfiguration:
+ _objc_msgSend$setWidgetConfigurationState:
+ _objc_msgSend$setWidgetProperties:
+ _objc_msgSend$setWidgetTimelineEntries:
+ _objc_msgSend$setWidth:
+ _objc_msgSend$small
+ _objc_msgSend$widgetConfigurationState
+ _objc_msgSend$widgetProperties
+ _objc_msgSend$widgetPropertiesDataModelProvider
+ _objc_msgSend$widgetPropertiesState
+ _objc_msgSend$widgetTimelineEntries
+ _objc_msgSend$widgetTimelineEntriesDataModelProvider
+ _objc_msgSend$widgetTimelineEntriesState
- +[GEOAPPortal capturePeriodicSettingsWithMapSettings:mapUiShown:mapsFeatures:mapsUserSettings:routingSettings:]
- +[GEOAPPortal capturePeriodicSettingsWithMapSettings:mapUiShown:mapsFeatures:mapsUserSettings:routingSettings:additionalStates:providedDropRate:completionQueue:completionBlock:]
- +[GEOAPPortal captureShowcaseSuppressionWithBusinessId:localSearchProviderID:showcaseId:suppressionReason:adamId:]
- +[GEOAPPortal captureShowcaseSuppressionWithBusinessId:localSearchProviderID:showcaseId:suppressionReason:adamId:additionalStates:providedDropRate:completionQueue:completionBlock:]
- GCC_except_table1029
- GCC_except_table1034
- GCC_except_table1036
- GCC_except_table1140
- GCC_except_table1166
- GCC_except_table1168
- GCC_except_table1186
- GCC_except_table1190
- GCC_except_table1192
- GCC_except_table1405
- GCC_except_table1443
- GCC_except_table562
- GCC_except_table566
- GCC_except_table568
- GCC_except_table571
- GCC_except_table574
- GCC_except_table577
- GCC_except_table581
- GCC_except_table584
- GCC_except_table593
- GCC_except_table596
- GCC_except_table599
- GCC_except_table648
- GCC_except_table654
- GCC_except_table664
- _GeoAnalyticsConfig_AllowedCountriesForEnrichedResultsCount_Metadata_block_invoke_63
- _GeoAnalyticsConfig_B74FC90_enabled_Metadata_block_invoke_66
- _GeoAnalyticsConfig_GeoShifterObfuscationSeedIN_Metadata_block_invoke_65
- _GeoAnalyticsConfig_LastMetroAssetCatalogDownload_Metadata_block_invoke_71
- _GeoAnalyticsConfig_LocIntActiveBatchID_Metadata_block_invoke_67
- _GeoAnalyticsConfig_LocIntSeqNo_Metadata_block_invoke_68
- _GeoAnalyticsConfig_MetroAssetCatalogCheckInterval_Metadata_block_invoke_72
- _GeoAnalyticsConfig_TrafficShiftingINEnabled_Metadata_block_invoke_64
- _GeoAnalyticsConfig_UseriCloudAccountAvailable_Metadata_block_invoke_59
- _GeoAnalyticsConfig__debug_AlwaysUseExpensiveUpload_Metadata_block_invoke_60
- _GeoAnalyticsConfig__debug_CancelInflightUploads_Metadata_block_invoke_74
- _GeoAnalyticsConfig__debug_KeepUploadFiles_Metadata_block_invoke_61
- _GeoAnalyticsConfig__debug_NoMobileAssetPreloader_Metadata_block_invoke_75
- _GeoAnalyticsConfig__debug_NoUploader_Metadata_block_invoke_73
- _GeoAnalyticsConfig__debug_UploadCountersEnabled_Metadata_block_invoke_62
- _GeoAnalyticsConfig__debug_simulateFileWriteError_Metadata_block_invoke_70
- _GeoAnalyticsConfig__debug_simulateNoURLs_Metadata_block_invoke_69
- __177+[GEOAPPortal capturePeriodicSettingsWithMapSettings:mapUiShown:mapsFeatures:mapsUserSettings:routingSettings:additionalStates:providedDropRate:completionQueue:completionBlock:]_block_invoke
- __180+[GEOAPPortal captureShowcaseSuppressionWithBusinessId:localSearchProviderID:showcaseId:suppressionReason:adamId:additionalStates:providedDropRate:completionQueue:completionBlock:]_block_invoke
- ___177+[GEOAPPortal capturePeriodicSettingsWithMapSettings:mapUiShown:mapsFeatures:mapsUserSettings:routingSettings:additionalStates:providedDropRate:completionQueue:completionBlock:]_block_invoke
- ___180+[GEOAPPortal captureShowcaseSuppressionWithBusinessId:localSearchProviderID:showcaseId:suppressionReason:adamId:additionalStates:providedDropRate:completionQueue:completionBlock:]_block_invoke
- _objc_msgSend$capturePeriodicSettingsWithMapSettings:mapUiShown:mapsFeatures:mapsUserSettings:routingSettings:additionalStates:providedDropRate:completionQueue:completionBlock:
- _objc_msgSend$captureShowcaseSuppressionWithBusinessId:localSearchProviderID:showcaseId:suppressionReason:adamId:additionalStates:providedDropRate:completionQueue:completionBlock:
CStrings:
+ "B20@?0i8B12f16"
+ "DISPLAYED_VISITED_PLACES"
+ "MAP_VIEW_ACTIVATED"
+ "MAP_VIEW_FOREGROUNDED"
+ "MAP_VIEW_INSTANTIATED"
+ "SNAPSHOT"
+ "SNAPSHOTTER_USED"
+ "SWIPE_LEFT_SHOWCASE"
+ "SWIPE_RIGHT_SHOWCASE"
+ "TAP_ITEM_VISITED"
+ "TIMELINE"
+ "WIDGETKIT_CONTENT_REQUESTED"
+ "WidgetConfigurationMaxCountPerFamily"
+ "WidgetProperties"
+ "WidgetTimelineEntries"
+ "com.apple.GeoServices.Analytics.SharedState.widgetConfiguration"
+ "v16@?0i8I12"
+ "widgetProperties_stateDisabled"
+ "widgetTimelineEntries_stateDisabled"
```
