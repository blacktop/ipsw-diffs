## GeoAnalytics

> `/System/Library/PrivateFrameworks/GeoAnalytics.framework/GeoAnalytics`

```diff

-2031.34.7.17.33
-  __TEXT.__text: 0x8f740
-  __TEXT.__auth_stubs: 0x870
-  __TEXT.__objc_methlist: 0x206c
-  __TEXT.__const: 0x698
+2031.35.2.9.17
+  __TEXT.__text: 0x967ec
+  __TEXT.__auth_stubs: 0x920
+  __TEXT.__objc_methlist: 0x229c
+  __TEXT.__const: 0x6ac
   __TEXT.__dlopen_cstrs: 0x126
   __TEXT.__swift5_typeref: 0x4e
   __TEXT.__swift5_capture: 0x24
+  __TEXT.__cstring: 0xe18b
   __TEXT.__constg_swiftt: 0x54
   __TEXT.__swift5_reflstr: 0x17
   __TEXT.__swift5_fieldmd: 0x44
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_types: 0x8
-  __TEXT.__gcc_except_tab: 0x5ac
-  __TEXT.__cstring: 0xe0c5
+  __TEXT.__gcc_except_tab: 0x5d4
   __TEXT.__oslogstring: 0xdfc
-  __TEXT.__unwind_info: 0xe80
-  __TEXT.__objc_classname: 0x3aa
-  __TEXT.__objc_methname: 0x12fdc
-  __TEXT.__objc_methtype: 0x1c9f
-  __TEXT.__objc_stubs: 0xda00
-  __DATA_CONST.__got: 0x658
-  __DATA_CONST.__const: 0x6628
-  __DATA_CONST.__objc_classlist: 0xc8
+  __TEXT.__unwind_info: 0xee0
+  __TEXT.__objc_classname: 0x446
+  __TEXT.__objc_methname: 0x1351c
+  __TEXT.__objc_methtype: 0x1d1e
+  __TEXT.__objc_stubs: 0xdda0
+  __DATA_CONST.__got: 0x668
+  __DATA_CONST.__const: 0x66e8
+  __DATA_CONST.__objc_classlist: 0xe0
   __DATA_CONST.__objc_catlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x28
+  __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3e98
+  __DATA_CONST.__objc_selrefs: 0x3fb8
   __DATA_CONST.__objc_protorefs: 0x20
-  __DATA_CONST.__objc_superrefs: 0x80
-  __DATA_CONST.__objc_arraydata: 0xe60
-  __AUTH_CONST.__auth_got: 0x450
-  __AUTH_CONST.__const: 0x2e08
-  __AUTH_CONST.__cfstring: 0x13aa0
-  __AUTH_CONST.__objc_const: 0x1e68
-  __AUTH_CONST.__objc_intobj: 0x1c20
+  __DATA_CONST.__objc_superrefs: 0x90
+  __DATA_CONST.__objc_arraydata: 0xe70
+  __AUTH_CONST.__auth_got: 0x4a8
+  __AUTH_CONST.__const: 0x2ef8
+  __AUTH_CONST.__cfstring: 0x13b20
+  __AUTH_CONST.__objc_const: 0x2510
+  __AUTH_CONST.__objc_intobj: 0x1c50
   __AUTH_CONST.__objc_dictobj: 0x4b0
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH_CONST.__objc_arrayobj: 0x300
-  __AUTH.__objc_data: 0x140
+  __AUTH.__objc_data: 0x230
   __AUTH.__data: 0x40
-  __DATA.__objc_ivar: 0x144
-  __DATA.__data: 0x1e8
-  __DATA.__bss: 0xe8
+  __DATA.__objc_ivar: 0x194
+  __DATA.__data: 0x250
+  __DATA.__bss: 0xf8
   __DATA.__common: 0x8
   __DATA_DIRTY.__objc_data: 0x690
   __DATA_DIRTY.__data: 0x10
-  __DATA_DIRTY.__bss: 0x188
+  __DATA_DIRTY.__bss: 0x178
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/GeoServices.framework/GeoServices

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 10813C21-35AD-39B3-AE88-3105AAB1DD6F
-  Functions: 1404
-  Symbols:   6269
-  CStrings:  7574
+  UUID: 3C833ED5-D25F-3FD9-B8C3-C60CFCE33170
+  Functions: 1459
+  Symbols:   6459
+  CStrings:  7679
 
Symbols:
+ +[GEOAPPortal captureUgcDeleteLogsWithCertificates:signature:trigger:sessionSnapshot:additionalStates:providedDropRate:completionQueue:completionBlock:]
+ +[GEOAPPortal captureUserAction:target:value:dataModelInfoProviders:]
+ +[GEOAPPortal captureUserAction:target:value:sessionSnapshot:]
+ +[GEOAPPortal(DailyUsageCodeGen) addCodeGenDailyCountsWithActionTargetTuple:actionTargetValue:appGroup:dataModelInfoProvider:]
+ +[GEOAPPortal(DailyUsageCodeGen) addStaticDailyCountsWithActionTargetTuple:actionTargetValue:appGroup:dataModelInfoProvider:]
+ +[GEOAPPortal(DailyUsageCodeGen) dailyCountsWithActionTargetTuple:actionTargetValue:appGroup:dataModelInfoProvider:]
+ +[GEOAPPortal(Extras) captureUgcDeleteWithSignature:certificates:sessionSnapshot:trigger:queue:completion:]
+ +[GEOAPPortal(UserAction) capturePlaceCardUserAction:target:value:mapItem:timestamp:resultIndex:targetID:providerID:animationID:actionURL:photoID:placeCardType:localizedMapItemCategory:availableActions:unactionableUIElements:modules:commingledRichProviderIds:actionRichProviderId:classification:snapShot:]
+ +[GEOAPPortal(UserAction) captureUserAction:target:value:placeActionDetails:sessionSnapshot:]
+ +[GEOAPPortal(UserActionCodeGen) captureAccountSessionlessUserActionTargetPairWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:sessionSnapshot:dataModelInfoProviders:additionalStates:completionQueue:completionBlock:]
+ +[GEOAPPortal(UserActionCodeGen) captureArpPrivacyWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:sessionSnapshot:dataModelInfoProviders:additionalStates:completionQueue:completionBlock:]
+ +[GEOAPPortal(UserActionCodeGen) captureCarplayUserActionWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:sessionSnapshot:dataModelInfoProviders:additionalStates:completionQueue:completionBlock:]
+ +[GEOAPPortal(UserActionCodeGen) captureCuratedCollectionsSessionlessUserActionTargetPairRedactedCCStateWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:sessionSnapshot:dataModelInfoProviders:additionalStates:completionQueue:completionBlock:]
+ +[GEOAPPortal(UserActionCodeGen) captureCuratedCollectionsSessionlessUserActionTargetPairWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:sessionSnapshot:dataModelInfoProviders:additionalStates:completionQueue:completionBlock:]
+ +[GEOAPPortal(UserActionCodeGen) captureCuratedCollectionsShortUserActionTargetPairWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:sessionSnapshot:dataModelInfoProviders:additionalStates:completionQueue:completionBlock:]
+ +[GEOAPPortal(UserActionCodeGen) captureEnterMapsShortUserActionTargetPairWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:sessionSnapshot:dataModelInfoProviders:additionalStates:completionQueue:completionBlock:]
+ +[GEOAPPortal(UserActionCodeGen) captureFamiliarRoutesOnlyWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:sessionSnapshot:dataModelInfoProviders:additionalStates:completionQueue:completionBlock:]
+ +[GEOAPPortal(UserActionCodeGen) captureMapViewEngagementWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:sessionSnapshot:dataModelInfoProviders:additionalStates:completionQueue:completionBlock:]
+ +[GEOAPPortal(UserActionCodeGen) captureMuninCameraUserActionShortOnlyWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:sessionSnapshot:dataModelInfoProviders:additionalStates:completionQueue:completionBlock:]
+ +[GEOAPPortal(UserActionCodeGen) captureMuninUserActionShortOnlyWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:sessionSnapshot:dataModelInfoProviders:additionalStates:completionQueue:completionBlock:]
+ +[GEOAPPortal(UserActionCodeGen) captureNearbyTransitShortUserActionTargetPairWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:sessionSnapshot:dataModelInfoProviders:additionalStates:completionQueue:completionBlock:]
+ +[GEOAPPortal(UserActionCodeGen) captureOfflineSessionlessUserActionTargetPairWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:sessionSnapshot:dataModelInfoProviders:additionalStates:completionQueue:completionBlock:]
+ +[GEOAPPortal(UserActionCodeGen) captureOfflineShortUserActionTargetPairWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:sessionSnapshot:dataModelInfoProviders:additionalStates:completionQueue:completionBlock:]
+ +[GEOAPPortal(UserActionCodeGen) capturePlaceCardRevealWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:sessionSnapshot:dataModelInfoProviders:additionalStates:completionQueue:completionBlock:]
+ +[GEOAPPortal(UserActionCodeGen) capturePredExSessionlessUserActionTargetPairWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:sessionSnapshot:dataModelInfoProviders:additionalStates:completionQueue:completionBlock:]
+ +[GEOAPPortal(UserActionCodeGen) capturePredExShortUserActionTargetPairWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:sessionSnapshot:dataModelInfoProviders:additionalStates:completionQueue:completionBlock:]
+ +[GEOAPPortal(UserActionCodeGen) capturePriorityPlacecardActionShortUserActionsWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:sessionSnapshot:dataModelInfoProviders:additionalStates:completionQueue:completionBlock:]
+ +[GEOAPPortal(UserActionCodeGen) capturePriorityShortUserActionsWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:sessionSnapshot:dataModelInfoProviders:additionalStates:completionQueue:completionBlock:]
+ +[GEOAPPortal(UserActionCodeGen) captureRapSessionlessUserActionTargetPairWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:sessionSnapshot:dataModelInfoProviders:additionalStates:completionQueue:completionBlock:]
+ +[GEOAPPortal(UserActionCodeGen) captureRapShortAndSessionlessUserActionTargetPairWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:sessionSnapshot:dataModelInfoProviders:additionalStates:completionQueue:completionBlock:]
+ +[GEOAPPortal(UserActionCodeGen) captureRapUserActionShortOnlyWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:sessionSnapshot:dataModelInfoProviders:additionalStates:completionQueue:completionBlock:]
+ +[GEOAPPortal(UserActionCodeGen) captureSessionlessUserActionWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:sessionSnapshot:dataModelInfoProviders:additionalStates:completionQueue:completionBlock:]
+ +[GEOAPPortal(UserActionCodeGen) captureStandardShortWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:sessionSnapshot:dataModelInfoProviders:additionalStates:completionQueue:completionBlock:]
+ +[GEOAPPortal(UserActionCodeGen) captureStartEndNavWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:sessionSnapshot:dataModelInfoProviders:additionalStates:completionQueue:completionBlock:]
+ +[GEOAPPortal(UserActionCodeGen) captureTransitShortUserActionTargetPairWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:sessionSnapshot:dataModelInfoProviders:additionalStates:completionQueue:completionBlock:]
+ +[GEOAPPortal(UserActionCodeGen) captureUGCSessionlessUserActionTargetPairWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:sessionSnapshot:dataModelInfoProviders:additionalStates:completionQueue:completionBlock:]
+ +[GEOAPPortal(UserActionCodeGen) captureUGCShortUserActionTargetPairWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:sessionSnapshot:dataModelInfoProviders:additionalStates:completionQueue:completionBlock:]
+ +[GEOAPPortal(UserActionCodeGen) captureUserAction:target:value:moduleType:moduleMetadata:classification:richProviderId:sessionSnapshot:modelInfoProviders:additionalStates:completionQueue:completionBlock:]
+ +[GEOAPPortal(UserActionCodeGen) captureUserAction:target:value:moduleType:moduleMetadata:richProviderId:sessionSnapshot:modelInfoProviders:additionalStates:completionQueue:completionBlock:]
+ +[GEOAPPortal(UserActionCodeGen) captureVisualIntelligenceShortUserActionsWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:sessionSnapshot:dataModelInfoProviders:additionalStates:completionQueue:completionBlock:]
+ +[GEOAPUserSessionSnapshot snapshotForType:]
+ -[GEOAPEphemeralTapEventStateStore initWithResultIndex:businessId:localSearchProviderId:isEnriched:pinType:isGuide:]
+ -[GEOAPEphemeralTapEventStateStore isEnriched]
+ -[GEOAPEphemeralTapEventStateStore isGuide]
+ -[GEOAPEphemeralTapEventStateStore localSearchProviderId]
+ -[GEOAPEphemeralTapEventStateStore pinType]
+ -[GEOAPEphemeralTapEventStateStore searchResultBusinessId]
+ -[GEOAPEphemeralTapEventStateStore searchResultIndex]
+ -[GEOAPStateFactory stateForType:dataModelInfoProviders:]
+ -[GEOAPStateFactory(snapshot) sessionStateFromSnapshot:]
+ -[GEOAPUserActionDataModelInfoProviders .cxx_destruct]
+ -[GEOAPUserActionDataModelInfoProviders initWithSearchHomeProvider:]
+ -[GEOAPUserActionDataModelInfoProviders initWithSearchResultsProvider:]
+ -[GEOAPUserActionDataModelInfoProviders initWithTapEventProvider:]
+ -[GEOAPUserActionDataModelInfoProviders searchHomeDataModelProvider]
+ -[GEOAPUserActionDataModelInfoProviders searchResultsDataModelProvider]
+ -[GEOAPUserActionDataModelInfoProviders tapEventDataModelProvider]
+ -[GEOAPUserActionDataModelInfoProviders(Internal) pinTypeFromAPPinType:]
+ -[GEOAPUserActionDataModelInfoProviders(Internal) placeSummaryState]
+ -[GEOAPUserActionDataModelInfoProviders(Internal) resultTypeFromAPResultType:]
+ -[GEOAPUserActionDataModelInfoProviders(Internal) searchResultsState]
+ -[GEOAPUserActionDataModelInfoProviders(Internal) stateForType:]
+ -[GEOAPUserActionDataModelInfoProviders(Internal) tapEventState]
+ -[GEOAPUserSessionSnapshot navRelativeTimestamp]
+ -[GEOAPUserSessionSnapshot navSessionID]
+ -[GEOAPUserSessionSnapshot opaqueAppID]
+ -[GEOAPUserSessionSnapshot relativeTimestamp]
+ -[GEOAPUserSessionSnapshot sequenceNumber]
+ -[GEOAPUserSessionSnapshot sessionCreateHour]
+ -[GEOAPUserSessionSnapshot sessionCreateTime]
+ -[GEOAPUserSessionSnapshot sessionID]
+ -[GEOAPUserSessionSnapshot sessionSalt]
+ -[GEOAPUserSessionSnapshot sessionType]
+ -[GEOAPUserSessionSnapshot snapshotTime]
+ GCC_except_table1003
+ GCC_except_table1030
+ GCC_except_table1048
+ GCC_except_table1052
+ GCC_except_table1054
+ GCC_except_table124
+ GCC_except_table1266
+ GCC_except_table1304
+ GCC_except_table16
+ GCC_except_table23
+ GCC_except_table42
+ GCC_except_table44
+ GCC_except_table516
+ GCC_except_table519
+ GCC_except_table522
+ GCC_except_table524
+ GCC_except_table525
+ GCC_except_table565
+ GCC_except_table567
+ GCC_except_table572
+ GCC_except_table586
+ GCC_except_table591
+ GCC_except_table592
+ GCC_except_table601
+ GCC_except_table74
+ GCC_except_table76
+ GCC_except_table82
+ GCC_except_table84
+ GCC_except_table86
+ GCC_except_table887
+ GCC_except_table893
+ GCC_except_table92
+ _GEOBatchAnalyticsSessionType
+ _GeoAnalyticsStateConfig_searchHome_stateDisabled
+ _GeoAnalyticsStateConfig_searchHome_stateDisabled_Metadata
+ _GeoAnalyticsStateConfig_searchHome_stateDisabled_Metadata_block_invoke_62
+ _GeoAnalyticsStateConfig_searchResults_stateDisabled_Metadata_block_invoke_63
+ _GeoAnalyticsStateConfig_suggestions_stateDisabled_Metadata_block_invoke_64
+ _GeoAnalyticsStateConfig_tapEvent_stateDisabled_Metadata_block_invoke_65
+ _GeoAnalyticsStateConfig_tileSetStatic_stateDisabled_Metadata_block_invoke_67
+ _GeoAnalyticsStateConfig_tileSet_stateDisabled_Metadata_block_invoke_66
+ _GeoAnalyticsStateConfig_transitStep_stateDisabled_Metadata_block_invoke_69
+ _GeoAnalyticsStateConfig_transit_stateDisabled_Metadata_block_invoke_68
+ _GeoAnalyticsStateConfig_ugc_stateDisabled_Metadata_block_invoke_70
+ _GeoServicesConfig_PCIsRestricted
+ _OBJC_CLASS_$_GEOAPEphemeralTapEventStateStore
+ _OBJC_CLASS_$_GEOAPUserActionDataModelInfoProviders
+ _OBJC_CLASS_$_GEOAPUserSessionSnapshot
+ _OBJC_IVAR_$_GEOAPEphemeralTapEventStateStore._isEnriched
+ _OBJC_IVAR_$_GEOAPEphemeralTapEventStateStore._isGuide
+ _OBJC_IVAR_$_GEOAPEphemeralTapEventStateStore._localSearchProviderId
+ _OBJC_IVAR_$_GEOAPEphemeralTapEventStateStore._pinType
+ _OBJC_IVAR_$_GEOAPEphemeralTapEventStateStore._searchResultBusinessId
+ _OBJC_IVAR_$_GEOAPEphemeralTapEventStateStore._searchResultIndex
+ _OBJC_IVAR_$_GEOAPUserActionDataModelInfoProviders._searchHomeProvider
+ _OBJC_IVAR_$_GEOAPUserActionDataModelInfoProviders._searchResultsProvider
+ _OBJC_IVAR_$_GEOAPUserActionDataModelInfoProviders._tapEventProvider
+ _OBJC_IVAR_$_GEOAPUserSessionSnapshot._navRelativeTimestamp
+ _OBJC_IVAR_$_GEOAPUserSessionSnapshot._navSessionID
+ _OBJC_IVAR_$_GEOAPUserSessionSnapshot._opaqueAppID
+ _OBJC_IVAR_$_GEOAPUserSessionSnapshot._relativeTimestamp
+ _OBJC_IVAR_$_GEOAPUserSessionSnapshot._sequenceNumber
+ _OBJC_IVAR_$_GEOAPUserSessionSnapshot._sessionCreateHour
+ _OBJC_IVAR_$_GEOAPUserSessionSnapshot._sessionCreateTime
+ _OBJC_IVAR_$_GEOAPUserSessionSnapshot._sessionID
+ _OBJC_IVAR_$_GEOAPUserSessionSnapshot._sessionSalt
+ _OBJC_IVAR_$_GEOAPUserSessionSnapshot._sessionType
+ _OBJC_IVAR_$_GEOAPUserSessionSnapshot._snapshotTime
+ _OBJC_METACLASS_$_GEOAPEphemeralTapEventStateStore
+ _OBJC_METACLASS_$_GEOAPUserActionDataModelInfoProviders
+ _OBJC_METACLASS_$_GEOAPUserSessionSnapshot
+ __Block_copy
+ __Block_release
+ __OBJC_$_CLASS_METHODS_GEOAPUserSessionSnapshot
+ __OBJC_$_INSTANCE_METHODS_GEOAPEphemeralTapEventStateStore
+ __OBJC_$_INSTANCE_METHODS_GEOAPStateFactory(Convenience|snapshot)
+ __OBJC_$_INSTANCE_METHODS_GEOAPUserActionDataModelInfoProviders(Internal)
+ __OBJC_$_INSTANCE_METHODS_GEOAPUserSessionSnapshot
+ __OBJC_$_INSTANCE_VARIABLES_GEOAPEphemeralTapEventStateStore
+ __OBJC_$_INSTANCE_VARIABLES_GEOAPUserActionDataModelInfoProviders
+ __OBJC_$_INSTANCE_VARIABLES_GEOAPUserSessionSnapshot
+ __OBJC_$_PROP_LIST_GEOAPEphemeralTapEventStateStore
+ __OBJC_$_PROP_LIST_GEOAPUserActionDataModelInfoProviders
+ __OBJC_$_PROP_LIST_GEOAPUserActionTapEventDataModelProviding
+ __OBJC_$_PROP_LIST_GEOAPUserSessionSnapshot
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_GEOAPUserActionTapEventDataModelProviding
+ __OBJC_$_PROTOCOL_METHOD_TYPES_GEOAPUserActionTapEventDataModelProviding
+ __OBJC_$_PROTOCOL_REFS_GEOAPUserActionTapEventDataModelProviding
+ __OBJC_CLASS_PROTOCOLS_$_GEOAPEphemeralTapEventStateStore
+ __OBJC_CLASS_RO_$_GEOAPEphemeralTapEventStateStore
+ __OBJC_CLASS_RO_$_GEOAPUserActionDataModelInfoProviders
+ __OBJC_CLASS_RO_$_GEOAPUserSessionSnapshot
+ __OBJC_LABEL_PROTOCOL_$_GEOAPUserActionTapEventDataModelProviding
+ __OBJC_METACLASS_RO_$_GEOAPEphemeralTapEventStateStore
+ __OBJC_METACLASS_RO_$_GEOAPUserActionDataModelInfoProviders
+ __OBJC_METACLASS_RO_$_GEOAPUserSessionSnapshot
+ __OBJC_PROTOCOL_$_GEOAPUserActionTapEventDataModelProviding
+ ___152+[GEOAPPortal captureUgcDeleteLogsWithCertificates:signature:trigger:sessionSnapshot:additionalStates:providedDropRate:completionQueue:completionBlock:]_block_invoke
+ ___152+[GEOAPPortal captureUgcDeleteLogsWithCertificates:signature:trigger:sessionSnapshot:additionalStates:providedDropRate:completionQueue:completionBlock:]_block_invoke.116
+ ___205+[GEOAPPortal(UserActionCodeGen) captureUserAction:target:value:moduleType:moduleMetadata:classification:richProviderId:sessionSnapshot:modelInfoProviders:additionalStates:completionQueue:completionBlock:]_block_invoke
+ ___205+[GEOAPPortal(UserActionCodeGen) captureUserAction:target:value:moduleType:moduleMetadata:classification:richProviderId:sessionSnapshot:modelInfoProviders:additionalStates:completionQueue:completionBlock:]_block_invoke_2
+ ___219+[GEOAPPortal(UserActionCodeGen) captureArpPrivacyWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:sessionSnapshot:dataModelInfoProviders:additionalStates:completionQueue:completionBlock:]_block_invoke
+ ___220+[GEOAPPortal(UserActionCodeGen) captureStartEndNavWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:sessionSnapshot:dataModelInfoProviders:additionalStates:completionQueue:completionBlock:]_block_invoke
+ ___220+[GEOAPPortal(UserActionCodeGen) captureStartEndNavWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:sessionSnapshot:dataModelInfoProviders:additionalStates:completionQueue:completionBlock:]_block_invoke_2
+ ___222+[GEOAPPortal(UserActionCodeGen) captureStandardShortWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:sessionSnapshot:dataModelInfoProviders:additionalStates:completionQueue:completionBlock:]_block_invoke
+ ___224+[GEOAPPortal(UserActionCodeGen) capturePlaceCardRevealWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:sessionSnapshot:dataModelInfoProviders:additionalStates:completionQueue:completionBlock:]_block_invoke
+ ___226+[GEOAPPortal(UserActionCodeGen) captureCarplayUserActionWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:sessionSnapshot:dataModelInfoProviders:additionalStates:completionQueue:completionBlock:]_block_invoke
+ ___226+[GEOAPPortal(UserActionCodeGen) captureMapViewEngagementWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:sessionSnapshot:dataModelInfoProviders:additionalStates:completionQueue:completionBlock:]_block_invoke
+ ___227+[GEOAPPortal(UserActionCodeGen) captureFamiliarRoutesOnlyWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:sessionSnapshot:dataModelInfoProviders:additionalStates:completionQueue:completionBlock:]_block_invoke
+ ___230+[GEOAPPortal(UserActionCodeGen) captureSessionlessUserActionWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:sessionSnapshot:dataModelInfoProviders:additionalStates:completionQueue:completionBlock:]_block_invoke
+ ___231+[GEOAPPortal(UserActionCodeGen) captureRapUserActionShortOnlyWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:sessionSnapshot:dataModelInfoProviders:additionalStates:completionQueue:completionBlock:]_block_invoke
+ ___233+[GEOAPPortal(UserActionCodeGen) captureMuninUserActionShortOnlyWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:sessionSnapshot:dataModelInfoProviders:additionalStates:completionQueue:completionBlock:]_block_invoke
+ ___233+[GEOAPPortal(UserActionCodeGen) capturePriorityShortUserActionsWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:sessionSnapshot:dataModelInfoProviders:additionalStates:completionQueue:completionBlock:]_block_invoke
+ ___237+[GEOAPPortal(UserActionCodeGen) captureUGCShortUserActionTargetPairWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:sessionSnapshot:dataModelInfoProviders:additionalStates:completionQueue:completionBlock:]_block_invoke
+ ___239+[GEOAPPortal(UserActionCodeGen) captureMuninCameraUserActionShortOnlyWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:sessionSnapshot:dataModelInfoProviders:additionalStates:completionQueue:completionBlock:]_block_invoke
+ ___240+[GEOAPPortal(UserActionCodeGen) capturePredExShortUserActionTargetPairWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:sessionSnapshot:dataModelInfoProviders:additionalStates:completionQueue:completionBlock:]_block_invoke
+ ___241+[GEOAPPortal(UserActionCodeGen) captureOfflineShortUserActionTargetPairWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:sessionSnapshot:dataModelInfoProviders:additionalStates:completionQueue:completionBlock:]_block_invoke
+ ___241+[GEOAPPortal(UserActionCodeGen) captureTransitShortUserActionTargetPairWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:sessionSnapshot:dataModelInfoProviders:additionalStates:completionQueue:completionBlock:]_block_invoke
+ ___243+[GEOAPPortal(UserActionCodeGen) captureEnterMapsShortUserActionTargetPairWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:sessionSnapshot:dataModelInfoProviders:additionalStates:completionQueue:completionBlock:]_block_invoke
+ ___243+[GEOAPPortal(UserActionCodeGen) captureRapSessionlessUserActionTargetPairWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:sessionSnapshot:dataModelInfoProviders:additionalStates:completionQueue:completionBlock:]_block_invoke
+ ___243+[GEOAPPortal(UserActionCodeGen) captureUGCSessionlessUserActionTargetPairWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:sessionSnapshot:dataModelInfoProviders:additionalStates:completionQueue:completionBlock:]_block_invoke
+ ___243+[GEOAPPortal(UserActionCodeGen) captureVisualIntelligenceShortUserActionsWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:sessionSnapshot:dataModelInfoProviders:additionalStates:completionQueue:completionBlock:]_block_invoke
+ ___246+[GEOAPPortal(UserActionCodeGen) capturePredExSessionlessUserActionTargetPairWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:sessionSnapshot:dataModelInfoProviders:additionalStates:completionQueue:completionBlock:]_block_invoke
+ ___247+[GEOAPPortal(UserActionCodeGen) captureAccountSessionlessUserActionTargetPairWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:sessionSnapshot:dataModelInfoProviders:additionalStates:completionQueue:completionBlock:]_block_invoke
+ ___247+[GEOAPPortal(UserActionCodeGen) captureNearbyTransitShortUserActionTargetPairWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:sessionSnapshot:dataModelInfoProviders:additionalStates:completionQueue:completionBlock:]_block_invoke
+ ___247+[GEOAPPortal(UserActionCodeGen) captureOfflineSessionlessUserActionTargetPairWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:sessionSnapshot:dataModelInfoProviders:additionalStates:completionQueue:completionBlock:]_block_invoke
+ ___248+[GEOAPPortal(UserActionCodeGen) capturePriorityPlacecardActionShortUserActionsWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:sessionSnapshot:dataModelInfoProviders:additionalStates:completionQueue:completionBlock:]_block_invoke
+ ___251+[GEOAPPortal(UserActionCodeGen) captureRapShortAndSessionlessUserActionTargetPairWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:sessionSnapshot:dataModelInfoProviders:additionalStates:completionQueue:completionBlock:]_block_invoke
+ ___251+[GEOAPPortal(UserActionCodeGen) captureRapShortAndSessionlessUserActionTargetPairWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:sessionSnapshot:dataModelInfoProviders:additionalStates:completionQueue:completionBlock:]_block_invoke_2
+ ___252+[GEOAPPortal(UserActionCodeGen) captureCuratedCollectionsShortUserActionTargetPairWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:sessionSnapshot:dataModelInfoProviders:additionalStates:completionQueue:completionBlock:]_block_invoke
+ ___258+[GEOAPPortal(UserActionCodeGen) captureCuratedCollectionsSessionlessUserActionTargetPairWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:sessionSnapshot:dataModelInfoProviders:additionalStates:completionQueue:completionBlock:]_block_invoke
+ ___273+[GEOAPPortal(UserActionCodeGen) captureCuratedCollectionsSessionlessUserActionTargetPairRedactedCCStateWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:sessionSnapshot:dataModelInfoProviders:additionalStates:completionQueue:completionBlock:]_block_invoke
+ ___305+[GEOAPPortal(UserAction) capturePlaceCardUserAction:target:value:mapItem:timestamp:resultIndex:targetID:providerID:animationID:actionURL:photoID:placeCardType:localizedMapItemCategory:availableActions:unactionableUIElements:modules:commingledRichProviderIds:actionRichProviderId:classification:snapShot:]_block_invoke
+ ___305+[GEOAPPortal(UserAction) capturePlaceCardUserAction:target:value:mapItem:timestamp:resultIndex:targetID:providerID:animationID:actionURL:photoID:placeCardType:localizedMapItemCategory:availableActions:unactionableUIElements:modules:commingledRichProviderIds:actionRichProviderId:classification:snapShot:]_block_invoke_2
+ ___44+[GEOAPUserSessionSnapshot snapshotForType:]_block_invoke
+ ___68-[GEOAPUserActionDataModelInfoProviders(Internal) placeSummaryState]_block_invoke
+ ___69-[GEOAPUserActionDataModelInfoProviders(Internal) searchResultsState]_block_invoke
+ ___93+[GEOAPPortal(UserAction) captureUserAction:target:value:placeActionDetails:sessionSnapshot:]_block_invoke
+ ___Block_byref_object_copy_.1199
+ ___Block_byref_object_copy_.2400
+ ___Block_byref_object_copy_.3080
+ ___Block_byref_object_copy_.3156
+ ___Block_byref_object_dispose_.1200
+ ___Block_byref_object_dispose_.2401
+ ___Block_byref_object_dispose_.3081
+ ___Block_byref_object_dispose_.3157
+ ___block_descriptor_44_e8_32s_e61_v84?0d8{GEOSessionID=QQ}16d32d40I48{GEOSessionID=QQ}52d68d76ls32l8
+ ___block_descriptor_48_e8_32s40r_e40_B40?0Q8i16"NSString"20i28"NSString"32lr40l8s32l8
+ ___block_descriptor_48_e8_32s40s_e17_B28?0I8i12Q16I24ls32l8s40l8
+ ___block_literal_global.103.1737
+ ___block_literal_global.103.2357
+ ___block_literal_global.109.1744
+ ___block_literal_global.1129
+ ___block_literal_global.115.1751
+ ___block_literal_global.1204
+ ___block_literal_global.123.1760
+ ___block_literal_global.123.2182
+ ___block_literal_global.129.1767
+ ___block_literal_global.129.2189
+ ___block_literal_global.129.3222
+ ___block_literal_global.1315
+ ___block_literal_global.135.1774
+ ___block_literal_global.135.2194
+ ___block_literal_global.1359
+ ___block_literal_global.14.1482
+ ___block_literal_global.14.1656
+ ___block_literal_global.14.2105
+ ___block_literal_global.141.1781
+ ___block_literal_global.141.2201
+ ___block_literal_global.1462
+ ___block_literal_global.147.1788
+ ___block_literal_global.147.2208
+ ___block_literal_global.147.2367
+ ___block_literal_global.1476
+ ___block_literal_global.153.1795
+ ___block_literal_global.153.2215
+ ___block_literal_global.1646
+ ___block_literal_global.195.3240
+ ___block_literal_global.20.2112
+ ___block_literal_global.204.2379
+ ___block_literal_global.2097
+ ___block_literal_global.21.1490
+ ___block_literal_global.21.1666
+ ___block_literal_global.2316
+ ___block_literal_global.240.2599
+ ___block_literal_global.2429
+ ___block_literal_global.243.2603
+ ___block_literal_global.252.2611
+ ___block_literal_global.255.2613
+ ___block_literal_global.276.2627
+ ___block_literal_global.279.2629
+ ___block_literal_global.2841
+ ___block_literal_global.294.2635
+ ___block_literal_global.297.2637
+ ___block_literal_global.31.1156
+ ___block_literal_global.312.2643
+ ___block_literal_global.3122
+ ___block_literal_global.3288
+ ___block_literal_global.330.2651
+ ___block_literal_global.3395
+ ___block_literal_global.345.1881
+ ___block_literal_global.366.2273
+ ___block_literal_global.39.1501
+ ___block_literal_global.399.2678
+ ___block_literal_global.402.2680
+ ___block_literal_global.405.2684
+ ___block_literal_global.423.2700
+ ___block_literal_global.432.2707
+ ___block_literal_global.471.2718
+ ___block_literal_global.483.2723
+ ___block_literal_global.489.2725
+ ___block_literal_global.495.2729
+ ___block_literal_global.50.2135
+ ___block_literal_global.584
+ ___block_literal_global.61.1702
+ ___block_literal_global.62.2143
+ ___block_literal_global.65.2352
+ ___block_literal_global.68.2148
+ ___block_literal_global.722
+ ___block_literal_global.815.2083
+ ___block_literal_global.85.1716
+ ___block_literal_global.884
+ ___block_literal_global.91.1723
+ ___block_literal_global.97.1730
+ ___block_literal_global.975
+ ___block_literal_global.99.2832
+ ___chkstk_darwin
+ ___swift_instantiateConcreteTypeFromMangledNameV2
+ ___swift_memcpy8_8
+ __registerStateCaptureCallbacks.1649
+ __registerStateCaptureCallbacks.2100
+ __registerStateCaptureCallbacks.2319
+ __registerStateCaptureCallbacks.2432
+ __stateCaptureCallbackRegistration.1647
+ __stateCaptureCallbackRegistration.2098
+ __stateCaptureCallbackRegistration.2317
+ __stateCaptureCallbackRegistration.2430
+ _block_copy_helper
+ _block_descriptor
+ _block_destroy_helper
+ _captureUserAction:target:value:moduleType:moduleMetadata:classification:richProviderId:sessionSnapshot:modelInfoProviders:additionalStates:completionQueue:completionBlock:.onceToken
+ _captureUserAction:target:value:moduleType:moduleMetadata:classification:richProviderId:sessionSnapshot:modelInfoProviders:additionalStates:completionQueue:completionBlock:.runningInMapsApp
+ _objc_msgSend$addCodeGenDailyCountsWithActionTargetTuple:actionTargetValue:appGroup:dataModelInfoProvider:
+ _objc_msgSend$addStaticDailyCountsWithActionTargetTuple:actionTargetValue:appGroup:dataModelInfoProvider:
+ _objc_msgSend$captureAccountSessionlessUserActionTargetPairWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:sessionSnapshot:dataModelInfoProviders:additionalStates:completionQueue:completionBlock:
+ _objc_msgSend$captureArpPrivacyWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:sessionSnapshot:dataModelInfoProviders:additionalStates:completionQueue:completionBlock:
+ _objc_msgSend$captureCarplayUserActionWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:sessionSnapshot:dataModelInfoProviders:additionalStates:completionQueue:completionBlock:
+ _objc_msgSend$captureCuratedCollectionsSessionlessUserActionTargetPairRedactedCCStateWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:sessionSnapshot:dataModelInfoProviders:additionalStates:completionQueue:completionBlock:
+ _objc_msgSend$captureCuratedCollectionsSessionlessUserActionTargetPairWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:sessionSnapshot:dataModelInfoProviders:additionalStates:completionQueue:completionBlock:
+ _objc_msgSend$captureCuratedCollectionsShortUserActionTargetPairWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:sessionSnapshot:dataModelInfoProviders:additionalStates:completionQueue:completionBlock:
+ _objc_msgSend$captureEnterMapsShortUserActionTargetPairWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:sessionSnapshot:dataModelInfoProviders:additionalStates:completionQueue:completionBlock:
+ _objc_msgSend$captureFamiliarRoutesOnlyWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:sessionSnapshot:dataModelInfoProviders:additionalStates:completionQueue:completionBlock:
+ _objc_msgSend$captureMapViewEngagementWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:sessionSnapshot:dataModelInfoProviders:additionalStates:completionQueue:completionBlock:
+ _objc_msgSend$captureMuninCameraUserActionShortOnlyWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:sessionSnapshot:dataModelInfoProviders:additionalStates:completionQueue:completionBlock:
+ _objc_msgSend$captureMuninUserActionShortOnlyWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:sessionSnapshot:dataModelInfoProviders:additionalStates:completionQueue:completionBlock:
+ _objc_msgSend$captureNearbyTransitShortUserActionTargetPairWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:sessionSnapshot:dataModelInfoProviders:additionalStates:completionQueue:completionBlock:
+ _objc_msgSend$captureOfflineSessionlessUserActionTargetPairWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:sessionSnapshot:dataModelInfoProviders:additionalStates:completionQueue:completionBlock:
+ _objc_msgSend$captureOfflineShortUserActionTargetPairWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:sessionSnapshot:dataModelInfoProviders:additionalStates:completionQueue:completionBlock:
+ _objc_msgSend$capturePlaceCardRevealWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:sessionSnapshot:dataModelInfoProviders:additionalStates:completionQueue:completionBlock:
+ _objc_msgSend$capturePlaceCardUserAction:target:value:mapItem:timestamp:resultIndex:targetID:providerID:animationID:actionURL:photoID:placeCardType:localizedMapItemCategory:availableActions:unactionableUIElements:modules:commingledRichProviderIds:actionRichProviderId:classification:snapShot:
+ _objc_msgSend$capturePredExSessionlessUserActionTargetPairWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:sessionSnapshot:dataModelInfoProviders:additionalStates:completionQueue:completionBlock:
+ _objc_msgSend$capturePredExShortUserActionTargetPairWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:sessionSnapshot:dataModelInfoProviders:additionalStates:completionQueue:completionBlock:
+ _objc_msgSend$capturePriorityPlacecardActionShortUserActionsWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:sessionSnapshot:dataModelInfoProviders:additionalStates:completionQueue:completionBlock:
+ _objc_msgSend$capturePriorityShortUserActionsWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:sessionSnapshot:dataModelInfoProviders:additionalStates:completionQueue:completionBlock:
+ _objc_msgSend$captureRapSessionlessUserActionTargetPairWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:sessionSnapshot:dataModelInfoProviders:additionalStates:completionQueue:completionBlock:
+ _objc_msgSend$captureRapShortAndSessionlessUserActionTargetPairWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:sessionSnapshot:dataModelInfoProviders:additionalStates:completionQueue:completionBlock:
+ _objc_msgSend$captureRapUserActionShortOnlyWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:sessionSnapshot:dataModelInfoProviders:additionalStates:completionQueue:completionBlock:
+ _objc_msgSend$captureSessionlessUserActionWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:sessionSnapshot:dataModelInfoProviders:additionalStates:completionQueue:completionBlock:
+ _objc_msgSend$captureStandardShortWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:sessionSnapshot:dataModelInfoProviders:additionalStates:completionQueue:completionBlock:
+ _objc_msgSend$captureStartEndNavWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:sessionSnapshot:dataModelInfoProviders:additionalStates:completionQueue:completionBlock:
+ _objc_msgSend$captureTransitShortUserActionTargetPairWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:sessionSnapshot:dataModelInfoProviders:additionalStates:completionQueue:completionBlock:
+ _objc_msgSend$captureUGCSessionlessUserActionTargetPairWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:sessionSnapshot:dataModelInfoProviders:additionalStates:completionQueue:completionBlock:
+ _objc_msgSend$captureUGCShortUserActionTargetPairWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:sessionSnapshot:dataModelInfoProviders:additionalStates:completionQueue:completionBlock:
+ _objc_msgSend$captureUgcDeleteLogsWithCertificates:signature:trigger:sessionSnapshot:additionalStates:providedDropRate:completionQueue:completionBlock:
+ _objc_msgSend$captureUgcDeleteWithSignature:certificates:sessionSnapshot:trigger:queue:completion:
+ _objc_msgSend$captureUserAction:target:value:moduleType:moduleMetadata:classification:richProviderId:sessionSnapshot:modelInfoProviders:additionalStates:completionQueue:completionBlock:
+ _objc_msgSend$captureUserAction:target:value:moduleType:moduleMetadata:richProviderId:sessionSnapshot:modelInfoProviders:additionalStates:completionQueue:completionBlock:
+ _objc_msgSend$captureUserAction:target:value:sessionSnapshot:
+ _objc_msgSend$captureVisualIntelligenceShortUserActionsWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:sessionSnapshot:dataModelInfoProviders:additionalStates:completionQueue:completionBlock:
+ _objc_msgSend$dailyCountsWithActionTargetTuple:actionTargetValue:appGroup:dataModelInfoProvider:
+ _objc_msgSend$hasResults
+ _objc_msgSend$isEnriched
+ _objc_msgSend$isGuide
+ _objc_msgSend$localSearchProviderId
+ _objc_msgSend$navRelativeTimestamp
+ _objc_msgSend$opaqueAppID
+ _objc_msgSend$pinType
+ _objc_msgSend$pinTypeFromAPPinType:
+ _objc_msgSend$placeSummaryState
+ _objc_msgSend$placeSummaryWithIterationBlock:
+ _objc_msgSend$relativeTimestamp
+ _objc_msgSend$reportLogMsg:uploadBatchId:completionQueue:completion:
+ _objc_msgSend$resultTypeFromAPResultType:
+ _objc_msgSend$resultsWithIterationBlock:
+ _objc_msgSend$searchResultBusinessId
+ _objc_msgSend$searchResultIndex
+ _objc_msgSend$searchResultsDataModelProvider
+ _objc_msgSend$sequenceNumber
+ _objc_msgSend$sessionCreateHour
+ _objc_msgSend$sessionID
+ _objc_msgSend$sessionSalt
+ _objc_msgSend$sessionStateFromSnapshot:
+ _objc_msgSend$sessionType
+ _objc_msgSend$setShareSessionWithMaps:
+ _objc_msgSend$snapshotTime
+ _objc_msgSend$stateForType:dataModelInfoProviders:
+ _objc_msgSend$tapEvent
+ _objc_msgSend$tapEventDataModelProvider
+ _objc_msgSend$uuidFrom:
+ _sharedManager.onceToken.1182
+ _swift_allocObject
+ _swift_cvw_assignWithCopy
+ _swift_cvw_assignWithTake
+ _swift_cvw_destroy
+ _swift_cvw_initWithCopy
+ _swift_cvw_initializeBufferWithCopyOfBuffer
+ _swift_deallocObject
+ _swift_getTypeByMangledNameInContext2
+ _swift_isEscapingClosureAtFileLocation
+ _swift_release
+ _swift_retain
- +[GEOAPPortal capturePredExTrainingWithChanceOfPrecipitation:chanceOfRain:chanceOfSnow:endTime:durationUntilEventEnd:durationUntilEventStart:startTime:temperature:timeOfDay:timeSinceBackgrounded:actualTransportMode:dayOfWeek:distanceFromHereToHome:distanceFromHereToOrigin:distanceFromHereToParkedCar:distanceFromHereToWork:distanceFromHere:distanceFromOriginToDestination:entryType:weatherType:mapType:predictedTransportMode:preferredTransportMode:isInBasemode:isCarplayConnected:isTourist:isTransitPossible:routePlanningScreenPresented:userLocationGeohash4:isVehicleBluetoothConnected:weatherAqi:modelName:modelVersion:modelTrainedDate:]
- +[GEOAPPortal captureUgcDeleteLogsWithCertificates:signature:trigger:additionalStates:providedDropRate:completionQueue:completionBlock:]
- +[GEOAPPortal(DailyUsageCodeGen) addCodeGenDailyCountsWithActionTargetTuple:actionTargetValue:appGroup:]
- +[GEOAPPortal(DailyUsageCodeGen) addStaticDailyCountsWithActionTargetTuple:actionTargetValue:appGroup:]
- +[GEOAPPortal(DailyUsageCodeGen) dailyCountsWithActionTargetTuple:actionTargetValue:appGroup:]
- +[GEOAPPortal(PredEx) capturePredExTrainingWithChanceOfPrecipitation:chanceOfRain:chanceOfSnow:endTime:durationUntilEventEnd:durationUntilEventStart:startTime:temperature:timeOfDay:timeSinceBackgrounded:actualTransportMode:dayOfWeek:distanceFromHereToHome:distanceFromHereToOrigin:distanceFromHereToParkedCar:distanceFromHereToWork:distanceFromHere:distanceFromOriginToDestination:entryType:weatherType:mapType:predictedTransportMode:preferredTransportMode:isInBasemode:isTourist:isCarplayConnected:isTransitPossible:routePlanningScreenPresented:userLocation:isVehicleBluetoothConnected:weatherAqi:modelName:modelVersion:modelTrainedDate:]
- +[GEOAPPortal(PredEx) capturePredExTrainingWithChanceOfPrecipitation:chanceOfRain:chanceOfSnow:endTime:durationUntilEventEnd:durationUntilEventStart:startTime:temperature:timeOfDay:timeSinceBackgrounded:actualTransportMode:dayOfWeek:distanceFromHereToHome:distanceFromHereToOrigin:distanceFromHereToParkedCar:distanceFromHereToWork:distanceFromHere:distanceFromOriginToDestination:entryType:weatherType:mapType:predictedTransportMode:preferredTransportMode:isTourist:isCarplayConnected:isTransitPossible:userLocation:isVehicleBluetoothConnected:weatherAqi:]
- +[GEOAPPortal(PredEx) capturePredExTrainingWithChanceOfPrecipitation:chanceOfRain:chanceOfSnow:endTime:durationUntilEventEnd:durationUntilEventStart:startTime:temperature:timeOfDay:timeSinceBackgrounded:actualTransportMode:dayOfWeek:distanceFromHereToHome:distanceFromHereToOrigin:distanceFromHereToParkedCar:distanceFromHereToWork:distanceFromHere:distanceFromOriginToDestination:entryType:weatherType:mapType:predictedTransportMode:preferredTransportMode:isTourist:isCarplayConnected:isTransitPossible:userLocation:isVehicleBluetoothConnected:weatherAqi:modelName:modelVersion:modelTrainedDate:]
- +[GEOAPPortal(UserActionCodeGen) captureAccountSessionlessUserActionTargetPairWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:additionalStates:completionQueue:completionBlock:]
- +[GEOAPPortal(UserActionCodeGen) captureArpPrivacyWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:additionalStates:completionQueue:completionBlock:]
- +[GEOAPPortal(UserActionCodeGen) captureCarplayUserActionWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:additionalStates:completionQueue:completionBlock:]
- +[GEOAPPortal(UserActionCodeGen) captureCuratedCollectionsSessionlessUserActionTargetPairRedactedCCStateWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:additionalStates:completionQueue:completionBlock:]
- +[GEOAPPortal(UserActionCodeGen) captureCuratedCollectionsSessionlessUserActionTargetPairWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:additionalStates:completionQueue:completionBlock:]
- +[GEOAPPortal(UserActionCodeGen) captureCuratedCollectionsShortUserActionTargetPairWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:additionalStates:completionQueue:completionBlock:]
- +[GEOAPPortal(UserActionCodeGen) captureEnterMapsShortUserActionTargetPairWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:additionalStates:completionQueue:completionBlock:]
- +[GEOAPPortal(UserActionCodeGen) captureFamiliarRoutesOnlyWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:additionalStates:completionQueue:completionBlock:]
- +[GEOAPPortal(UserActionCodeGen) captureMapViewEngagementWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:additionalStates:completionQueue:completionBlock:]
- +[GEOAPPortal(UserActionCodeGen) captureMuninCameraUserActionShortOnlyWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:additionalStates:completionQueue:completionBlock:]
- +[GEOAPPortal(UserActionCodeGen) captureMuninUserActionShortOnlyWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:additionalStates:completionQueue:completionBlock:]
- +[GEOAPPortal(UserActionCodeGen) captureNearbyTransitShortUserActionTargetPairWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:additionalStates:completionQueue:completionBlock:]
- +[GEOAPPortal(UserActionCodeGen) captureOfflineSessionlessUserActionTargetPairWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:additionalStates:completionQueue:completionBlock:]
- +[GEOAPPortal(UserActionCodeGen) captureOfflineShortUserActionTargetPairWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:additionalStates:completionQueue:completionBlock:]
- +[GEOAPPortal(UserActionCodeGen) capturePlaceCardRevealWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:additionalStates:completionQueue:completionBlock:]
- +[GEOAPPortal(UserActionCodeGen) capturePredExSessionlessUserActionTargetPairWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:additionalStates:completionQueue:completionBlock:]
- +[GEOAPPortal(UserActionCodeGen) capturePredExShortUserActionTargetPairWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:additionalStates:completionQueue:completionBlock:]
- +[GEOAPPortal(UserActionCodeGen) capturePriorityPlacecardActionShortUserActionsWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:additionalStates:completionQueue:completionBlock:]
- +[GEOAPPortal(UserActionCodeGen) capturePriorityShortUserActionsWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:additionalStates:completionQueue:completionBlock:]
- +[GEOAPPortal(UserActionCodeGen) captureRapSessionlessUserActionTargetPairWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:additionalStates:completionQueue:completionBlock:]
- +[GEOAPPortal(UserActionCodeGen) captureRapShortAndSessionlessUserActionTargetPairWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:additionalStates:completionQueue:completionBlock:]
- +[GEOAPPortal(UserActionCodeGen) captureRapUserActionShortOnlyWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:additionalStates:completionQueue:completionBlock:]
- +[GEOAPPortal(UserActionCodeGen) captureSessionlessUserActionWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:additionalStates:completionQueue:completionBlock:]
- +[GEOAPPortal(UserActionCodeGen) captureStandardShortWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:additionalStates:completionQueue:completionBlock:]
- +[GEOAPPortal(UserActionCodeGen) captureStartEndNavWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:additionalStates:completionQueue:completionBlock:]
- +[GEOAPPortal(UserActionCodeGen) captureTransitShortUserActionTargetPairWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:additionalStates:completionQueue:completionBlock:]
- +[GEOAPPortal(UserActionCodeGen) captureUGCSessionlessUserActionTargetPairWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:additionalStates:completionQueue:completionBlock:]
- +[GEOAPPortal(UserActionCodeGen) captureUGCShortUserActionTargetPairWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:additionalStates:completionQueue:completionBlock:]
- +[GEOAPPortal(UserActionCodeGen) captureUserAction:target:value:moduleType:moduleMetadata:classification:richProviderId:additionalStates:completionQueue:completionBlock:]
- +[GEOAPPortal(UserActionCodeGen) captureVisualIntelligenceShortUserActionsWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:additionalStates:completionQueue:completionBlock:]
- GCC_except_table1002
- GCC_except_table1004
- GCC_except_table1022
- GCC_except_table1026
- GCC_except_table122
- GCC_except_table1240
- GCC_except_table1278
- GCC_except_table15
- GCC_except_table22
- GCC_except_table41
- GCC_except_table43
- GCC_except_table509
- GCC_except_table512
- GCC_except_table515
- GCC_except_table517
- GCC_except_table518
- GCC_except_table558
- GCC_except_table560
- GCC_except_table568
- GCC_except_table583
- GCC_except_table588
- GCC_except_table589
- GCC_except_table598
- GCC_except_table73
- GCC_except_table75
- GCC_except_table81
- GCC_except_table83
- GCC_except_table85
- GCC_except_table869
- GCC_except_table91
- GCC_except_table977
- _GeoAnalyticsStateConfig_searchResults_stateDisabled_Metadata_block_invoke_62
- _GeoAnalyticsStateConfig_suggestions_stateDisabled_Metadata_block_invoke_63
- _GeoAnalyticsStateConfig_tapEvent_stateDisabled_Metadata_block_invoke_64
- _GeoAnalyticsStateConfig_tileSetStatic_stateDisabled_Metadata_block_invoke_66
- _GeoAnalyticsStateConfig_tileSet_stateDisabled_Metadata_block_invoke_65
- _GeoAnalyticsStateConfig_transitStep_stateDisabled_Metadata_block_invoke_68
- _GeoAnalyticsStateConfig_transit_stateDisabled_Metadata_block_invoke_67
- _GeoAnalyticsStateConfig_ugc_stateDisabled_Metadata_block_invoke_69
- __OBJC_$_INSTANCE_METHODS_GEOAPStateFactory(Convenience)
- ___136+[GEOAPPortal captureUgcDeleteLogsWithCertificates:signature:trigger:additionalStates:providedDropRate:completionQueue:completionBlock:]_block_invoke
- ___136+[GEOAPPortal captureUgcDeleteLogsWithCertificates:signature:trigger:additionalStates:providedDropRate:completionQueue:completionBlock:]_block_invoke.116
- ___170+[GEOAPPortal(UserActionCodeGen) captureUserAction:target:value:moduleType:moduleMetadata:classification:richProviderId:additionalStates:completionQueue:completionBlock:]_block_invoke
- ___170+[GEOAPPortal(UserActionCodeGen) captureUserAction:target:value:moduleType:moduleMetadata:classification:richProviderId:additionalStates:completionQueue:completionBlock:]_block_invoke_2
- ___180+[GEOAPPortal(UserActionCodeGen) captureArpPrivacyWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:additionalStates:completionQueue:completionBlock:]_block_invoke
- ___181+[GEOAPPortal(UserActionCodeGen) captureStartEndNavWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:additionalStates:completionQueue:completionBlock:]_block_invoke
- ___181+[GEOAPPortal(UserActionCodeGen) captureStartEndNavWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:additionalStates:completionQueue:completionBlock:]_block_invoke_2
- ___183+[GEOAPPortal(UserActionCodeGen) captureStandardShortWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:additionalStates:completionQueue:completionBlock:]_block_invoke
- ___185+[GEOAPPortal(UserActionCodeGen) capturePlaceCardRevealWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:additionalStates:completionQueue:completionBlock:]_block_invoke
- ___187+[GEOAPPortal(UserActionCodeGen) captureCarplayUserActionWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:additionalStates:completionQueue:completionBlock:]_block_invoke
- ___187+[GEOAPPortal(UserActionCodeGen) captureMapViewEngagementWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:additionalStates:completionQueue:completionBlock:]_block_invoke
- ___188+[GEOAPPortal(UserActionCodeGen) captureFamiliarRoutesOnlyWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:additionalStates:completionQueue:completionBlock:]_block_invoke
- ___191+[GEOAPPortal(UserActionCodeGen) captureSessionlessUserActionWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:additionalStates:completionQueue:completionBlock:]_block_invoke
- ___192+[GEOAPPortal(UserActionCodeGen) captureRapUserActionShortOnlyWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:additionalStates:completionQueue:completionBlock:]_block_invoke
- ___194+[GEOAPPortal(UserActionCodeGen) captureMuninUserActionShortOnlyWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:additionalStates:completionQueue:completionBlock:]_block_invoke
- ___194+[GEOAPPortal(UserActionCodeGen) capturePriorityShortUserActionsWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:additionalStates:completionQueue:completionBlock:]_block_invoke
- ___198+[GEOAPPortal(UserActionCodeGen) captureUGCShortUserActionTargetPairWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:additionalStates:completionQueue:completionBlock:]_block_invoke
- ___200+[GEOAPPortal(UserActionCodeGen) captureMuninCameraUserActionShortOnlyWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:additionalStates:completionQueue:completionBlock:]_block_invoke
- ___201+[GEOAPPortal(UserActionCodeGen) capturePredExShortUserActionTargetPairWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:additionalStates:completionQueue:completionBlock:]_block_invoke
- ___202+[GEOAPPortal(UserActionCodeGen) captureOfflineShortUserActionTargetPairWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:additionalStates:completionQueue:completionBlock:]_block_invoke
- ___202+[GEOAPPortal(UserActionCodeGen) captureTransitShortUserActionTargetPairWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:additionalStates:completionQueue:completionBlock:]_block_invoke
- ___204+[GEOAPPortal(UserActionCodeGen) captureEnterMapsShortUserActionTargetPairWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:additionalStates:completionQueue:completionBlock:]_block_invoke
- ___204+[GEOAPPortal(UserActionCodeGen) captureRapSessionlessUserActionTargetPairWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:additionalStates:completionQueue:completionBlock:]_block_invoke
- ___204+[GEOAPPortal(UserActionCodeGen) captureUGCSessionlessUserActionTargetPairWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:additionalStates:completionQueue:completionBlock:]_block_invoke
- ___204+[GEOAPPortal(UserActionCodeGen) captureVisualIntelligenceShortUserActionsWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:additionalStates:completionQueue:completionBlock:]_block_invoke
- ___207+[GEOAPPortal(UserActionCodeGen) capturePredExSessionlessUserActionTargetPairWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:additionalStates:completionQueue:completionBlock:]_block_invoke
- ___208+[GEOAPPortal(UserActionCodeGen) captureAccountSessionlessUserActionTargetPairWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:additionalStates:completionQueue:completionBlock:]_block_invoke
- ___208+[GEOAPPortal(UserActionCodeGen) captureNearbyTransitShortUserActionTargetPairWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:additionalStates:completionQueue:completionBlock:]_block_invoke
- ___208+[GEOAPPortal(UserActionCodeGen) captureOfflineSessionlessUserActionTargetPairWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:additionalStates:completionQueue:completionBlock:]_block_invoke
- ___209+[GEOAPPortal(UserActionCodeGen) capturePriorityPlacecardActionShortUserActionsWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:additionalStates:completionQueue:completionBlock:]_block_invoke
- ___212+[GEOAPPortal(UserActionCodeGen) captureRapShortAndSessionlessUserActionTargetPairWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:additionalStates:completionQueue:completionBlock:]_block_invoke
- ___212+[GEOAPPortal(UserActionCodeGen) captureRapShortAndSessionlessUserActionTargetPairWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:additionalStates:completionQueue:completionBlock:]_block_invoke_2
- ___213+[GEOAPPortal(UserActionCodeGen) captureCuratedCollectionsShortUserActionTargetPairWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:additionalStates:completionQueue:completionBlock:]_block_invoke
- ___219+[GEOAPPortal(UserActionCodeGen) captureCuratedCollectionsSessionlessUserActionTargetPairWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:additionalStates:completionQueue:completionBlock:]_block_invoke
- ___234+[GEOAPPortal(UserActionCodeGen) captureCuratedCollectionsSessionlessUserActionTargetPairRedactedCCStateWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:additionalStates:completionQueue:completionBlock:]_block_invoke
- ___296+[GEOAPPortal(UserAction) capturePlaceCardUserAction:target:value:mapItem:timestamp:resultIndex:targetID:providerID:animationID:actionURL:photoID:placeCardType:localizedMapItemCategory:availableActions:unactionableUIElements:modules:commingledRichProviderIds:actionRichProviderId:classification:]_block_invoke
- ___296+[GEOAPPortal(UserAction) capturePlaceCardUserAction:target:value:mapItem:timestamp:resultIndex:targetID:providerID:animationID:actionURL:photoID:placeCardType:localizedMapItemCategory:availableActions:unactionableUIElements:modules:commingledRichProviderIds:actionRichProviderId:classification:]_block_invoke_2
- ___Block_byref_object_copy_.1101
- ___Block_byref_object_copy_.2230
- ___Block_byref_object_copy_.2888
- ___Block_byref_object_copy_.2962
- ___Block_byref_object_dispose_.1102
- ___Block_byref_object_dispose_.2231
- ___Block_byref_object_dispose_.2889
- ___Block_byref_object_dispose_.2963
- ___block_literal_global.103.1568
- ___block_literal_global.103.2187
- ___block_literal_global.1031
- ___block_literal_global.109.1575
- ___block_literal_global.1106
- ___block_literal_global.115.1582
- ___block_literal_global.1217
- ___block_literal_global.123.1591
- ___block_literal_global.123.2012
- ___block_literal_global.1263
- ___block_literal_global.129.1598
- ___block_literal_global.129.2019
- ___block_literal_global.129.3028
- ___block_literal_global.135.1605
- ___block_literal_global.135.2024
- ___block_literal_global.1375
- ___block_literal_global.1389
- ___block_literal_global.14.1395
- ___block_literal_global.14.1488
- ___block_literal_global.14.1937
- ___block_literal_global.141.1612
- ___block_literal_global.141.2031
- ___block_literal_global.147.1619
- ___block_literal_global.147.2038
- ___block_literal_global.147.2197
- ___block_literal_global.1478
- ___block_literal_global.153.1626
- ___block_literal_global.153.2045
- ___block_literal_global.1929
- ___block_literal_global.195.3046
- ___block_literal_global.20.1944
- ___block_literal_global.204.2209
- ___block_literal_global.21.1403
- ___block_literal_global.21.1498
- ___block_literal_global.2146
- ___block_literal_global.2238
- ___block_literal_global.240.2408
- ___block_literal_global.243.2412
- ___block_literal_global.252.2420
- ___block_literal_global.255.2422
- ___block_literal_global.2654
- ___block_literal_global.276.2436
- ___block_literal_global.279.2438
- ___block_literal_global.2930
- ___block_literal_global.294.2444
- ___block_literal_global.297.2446
- ___block_literal_global.3094
- ___block_literal_global.31.1058
- ___block_literal_global.312.2450
- ___block_literal_global.3135
- ___block_literal_global.330.2461
- ___block_literal_global.346.2473
- ___block_literal_global.367.2482
- ___block_literal_global.39.1414
- ___block_literal_global.399.2496
- ___block_literal_global.402.2498
- ___block_literal_global.405.2502
- ___block_literal_global.423.2519
- ___block_literal_global.471.2535
- ___block_literal_global.483.2540
- ___block_literal_global.488
- ___block_literal_global.489.2542
- ___block_literal_global.495.2546
- ___block_literal_global.50.1967
- ___block_literal_global.60
- ___block_literal_global.61.1534
- ___block_literal_global.626
- ___block_literal_global.65.2182
- ___block_literal_global.68.1978
- ___block_literal_global.715
- ___block_literal_global.803.1905
- ___block_literal_global.85.1547
- ___block_literal_global.91.1554
- ___block_literal_global.936
- ___block_literal_global.97.1561
- ___block_literal_global.99.2645
- __registerStateCaptureCallbacks.1481
- __registerStateCaptureCallbacks.1932
- __registerStateCaptureCallbacks.2149
- __registerStateCaptureCallbacks.2241
- __stateCaptureCallbackRegistration.1479
- __stateCaptureCallbackRegistration.1930
- __stateCaptureCallbackRegistration.2147
- __stateCaptureCallbackRegistration.2239
- _captureUserAction:target:value:moduleType:moduleMetadata:classification:richProviderId:additionalStates:completionQueue:completionBlock:.onceToken
- _captureUserAction:target:value:moduleType:moduleMetadata:classification:richProviderId:additionalStates:completionQueue:completionBlock:.runningInMapsApp
- _getPPUtilsClass
- _objc_msgSend$addCodeGenDailyCountsWithActionTargetTuple:actionTargetValue:appGroup:
- _objc_msgSend$addStaticDailyCountsWithActionTargetTuple:actionTargetValue:appGroup:
- _objc_msgSend$captureAccountSessionlessUserActionTargetPairWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:additionalStates:completionQueue:completionBlock:
- _objc_msgSend$captureArpPrivacyWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:additionalStates:completionQueue:completionBlock:
- _objc_msgSend$captureCarplayUserActionWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:additionalStates:completionQueue:completionBlock:
- _objc_msgSend$captureCuratedCollectionsSessionlessUserActionTargetPairRedactedCCStateWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:additionalStates:completionQueue:completionBlock:
- _objc_msgSend$captureCuratedCollectionsSessionlessUserActionTargetPairWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:additionalStates:completionQueue:completionBlock:
- _objc_msgSend$captureCuratedCollectionsShortUserActionTargetPairWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:additionalStates:completionQueue:completionBlock:
- _objc_msgSend$captureEnterMapsShortUserActionTargetPairWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:additionalStates:completionQueue:completionBlock:
- _objc_msgSend$captureFamiliarRoutesOnlyWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:additionalStates:completionQueue:completionBlock:
- _objc_msgSend$captureMapViewEngagementWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:additionalStates:completionQueue:completionBlock:
- _objc_msgSend$captureMuninCameraUserActionShortOnlyWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:additionalStates:completionQueue:completionBlock:
- _objc_msgSend$captureMuninUserActionShortOnlyWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:additionalStates:completionQueue:completionBlock:
- _objc_msgSend$captureNearbyTransitShortUserActionTargetPairWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:additionalStates:completionQueue:completionBlock:
- _objc_msgSend$captureOfflineSessionlessUserActionTargetPairWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:additionalStates:completionQueue:completionBlock:
- _objc_msgSend$captureOfflineShortUserActionTargetPairWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:additionalStates:completionQueue:completionBlock:
- _objc_msgSend$capturePlaceCardRevealWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:additionalStates:completionQueue:completionBlock:
- _objc_msgSend$capturePredExSessionlessUserActionTargetPairWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:additionalStates:completionQueue:completionBlock:
- _objc_msgSend$capturePredExShortUserActionTargetPairWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:additionalStates:completionQueue:completionBlock:
- _objc_msgSend$capturePredExTrainingWithChanceOfPrecipitation:chanceOfRain:chanceOfSnow:endTime:durationUntilEventEnd:durationUntilEventStart:startTime:temperature:timeOfDay:timeSinceBackgrounded:actualTransportMode:dayOfWeek:distanceFromHereToHome:distanceFromHereToOrigin:distanceFromHereToParkedCar:distanceFromHereToWork:distanceFromHere:distanceFromOriginToDestination:entryType:weatherType:mapType:predictedTransportMode:preferredTransportMode:isInBasemode:isCarplayConnected:isTourist:isTransitPossible:routePlanningScreenPresented:userLocationGeohash4:isVehicleBluetoothConnected:weatherAqi:modelName:modelVersion:modelTrainedDate:
- _objc_msgSend$capturePredExTrainingWithChanceOfPrecipitation:chanceOfRain:chanceOfSnow:endTime:durationUntilEventEnd:durationUntilEventStart:startTime:temperature:timeOfDay:timeSinceBackgrounded:actualTransportMode:dayOfWeek:distanceFromHereToHome:distanceFromHereToOrigin:distanceFromHereToParkedCar:distanceFromHereToWork:distanceFromHere:distanceFromOriginToDestination:entryType:weatherType:mapType:predictedTransportMode:preferredTransportMode:isInBasemode:isCarplayConnected:isTourist:isTransitPossible:routePlanningScreenPresented:userLocationGeohash4:isVehicleBluetoothConnected:weatherAqi:modelName:modelVersion:modelTrainedDate:experimentID:treatmentID:
- _objc_msgSend$capturePredExTrainingWithChanceOfPrecipitation:chanceOfRain:chanceOfSnow:endTime:durationUntilEventEnd:durationUntilEventStart:startTime:temperature:timeOfDay:timeSinceBackgrounded:actualTransportMode:dayOfWeek:distanceFromHereToHome:distanceFromHereToOrigin:distanceFromHereToParkedCar:distanceFromHereToWork:distanceFromHere:distanceFromOriginToDestination:entryType:weatherType:mapType:predictedTransportMode:preferredTransportMode:isInBasemode:isTourist:isCarplayConnected:isTransitPossible:routePlanningScreenPresented:userLocation:isVehicleBluetoothConnected:weatherAqi:modelName:modelVersion:modelTrainedDate:
- _objc_msgSend$capturePriorityPlacecardActionShortUserActionsWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:additionalStates:completionQueue:completionBlock:
- _objc_msgSend$capturePriorityShortUserActionsWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:additionalStates:completionQueue:completionBlock:
- _objc_msgSend$captureRapSessionlessUserActionTargetPairWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:additionalStates:completionQueue:completionBlock:
- _objc_msgSend$captureRapShortAndSessionlessUserActionTargetPairWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:additionalStates:completionQueue:completionBlock:
- _objc_msgSend$captureRapUserActionShortOnlyWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:additionalStates:completionQueue:completionBlock:
- _objc_msgSend$captureSessionlessUserActionWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:additionalStates:completionQueue:completionBlock:
- _objc_msgSend$captureStandardShortWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:additionalStates:completionQueue:completionBlock:
- _objc_msgSend$captureStartEndNavWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:additionalStates:completionQueue:completionBlock:
- _objc_msgSend$captureTransitShortUserActionTargetPairWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:additionalStates:completionQueue:completionBlock:
- _objc_msgSend$captureUGCSessionlessUserActionTargetPairWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:additionalStates:completionQueue:completionBlock:
- _objc_msgSend$captureUGCShortUserActionTargetPairWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:additionalStates:completionQueue:completionBlock:
- _objc_msgSend$captureUgcDeleteLogsWithCertificates:signature:trigger:additionalStates:providedDropRate:completionQueue:completionBlock:
- _objc_msgSend$captureUserAction:target:value:moduleType:moduleMetadata:classification:richProviderId:additionalStates:completionQueue:completionBlock:
- _objc_msgSend$captureUserAction:target:value:moduleType:moduleMetadata:richProviderId:additionalStates:completionQueue:completionBlock:
- _objc_msgSend$captureVisualIntelligenceShortUserActionsWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:additionalStates:completionQueue:completionBlock:
- _objc_msgSend$dailyCountsWithActionTargetTuple:actionTargetValue:appGroup:
- _sharedManager.onceToken.1084
CStrings:
+ "+[GEOAPPortal(DailyUsageCodeGen) addCodeGenDailyCountsWithActionTargetTuple:actionTargetValue:appGroup:dataModelInfoProvider:]"
+ "+[GEOAPPortal(UserActionCodeGen) captureUserAction:target:value:moduleType:moduleMetadata:classification:richProviderId:sessionSnapshot:modelInfoProviders:additionalStates:completionQueue:completionBlock:]"
+ "@\"<GEOAPUserActionSearchHomeDataModelProviding>\""
+ "@\"<GEOAPUserActionSearchResultsDataModelProviding>\""
+ "@\"<GEOAPUserActionTapEventDataModelProviding>\""
+ "@32@0:8q16@24"
+ "@44@0:8I16Q20I28B32i36B40"
+ "@44@0:8Q16@24i32@36"
+ "B28@?0I8i12Q16I24"
+ "B40@?0Q8i16@\"NSString\"20i28@\"NSString\"32"
+ "GEOAPEphemeralTapEventStateStore"
+ "GEOAPUserActionDataModelInfoProviders"
+ "GEOAPUserActionTapEventDataModelProviding"
+ "GEOAPUserSessionSnapshot"
+ "I16@0:8"
+ "Internal"
+ "REVEAL_FULL"
+ "SEARCH_TRAY_PLACES_ELLIPSIS_MENU"
+ "SearchHome"
+ "T@\"<GEOAPUserActionSearchHomeDataModelProviding>\",R,N,V_searchHomeProvider"
+ "T@\"<GEOAPUserActionSearchResultsDataModelProviding>\",R,N,V_searchResultsProvider"
+ "T@\"<GEOAPUserActionTapEventDataModelProviding>\",R,N,V_tapEventProvider"
+ "TB,R,N,V_isEnriched"
+ "TB,R,N,V_isGuide"
+ "TI,R,N"
+ "TI,R,N,V_localSearchProviderId"
+ "TI,R,N,V_opaqueAppID"
+ "TI,R,N,V_searchResultIndex"
+ "TI,R,N,V_sequenceNumber"
+ "TQ,R,N"
+ "TQ,R,N,V_searchResultBusinessId"
+ "TQ,R,N,V_sessionSalt"
+ "Td,R,N,V_navRelativeTimestamp"
+ "Td,R,N,V_relativeTimestamp"
+ "Td,R,N,V_sessionCreateHour"
+ "Td,R,N,V_sessionCreateTime"
+ "Td,R,N,V_snapshotTime"
+ "Ti,R,N"
+ "Ti,R,N,V_pinType"
+ "Ti,R,N,V_sessionType"
+ "T{GEOSessionID=QQ},R,N,V_navSessionID"
+ "T{GEOSessionID=QQ},R,N,V_sessionID"
+ "_isEnriched"
+ "_isGuide"
+ "_localSearchProviderId"
+ "_navRelativeTimestamp"
+ "_navSessionID"
+ "_opaqueAppID"
+ "_pinType"
+ "_relativeTimestamp"
+ "_searchHomeProvider"
+ "_searchResultBusinessId"
+ "_searchResultIndex"
+ "_searchResultsProvider"
+ "_sequenceNumber"
+ "_sessionCreateHour"
+ "_sessionCreateTime"
+ "_sessionID"
+ "_sessionSalt"
+ "_sessionType"
+ "_snapshotTime"
+ "_tapEventProvider"
+ "addCodeGenDailyCountsWithActionTargetTuple:actionTargetValue:appGroup:dataModelInfoProvider:"
+ "addStaticDailyCountsWithActionTargetTuple:actionTargetValue:appGroup:dataModelInfoProvider:"
+ "captureAccountSessionlessUserActionTargetPairWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:sessionSnapshot:dataModelInfoProviders:additionalStates:completionQueue:completionBlock:"
+ "captureArpPrivacyWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:sessionSnapshot:dataModelInfoProviders:additionalStates:completionQueue:completionBlock:"
+ "captureCarplayUserActionWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:sessionSnapshot:dataModelInfoProviders:additionalStates:completionQueue:completionBlock:"
+ "captureCuratedCollectionsSessionlessUserActionTargetPairRedactedCCStateWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:sessionSnapshot:dataModelInfoProviders:additionalStates:completionQueue:completionBlock:"
+ "captureCuratedCollectionsSessionlessUserActionTargetPairWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:sessionSnapshot:dataModelInfoProviders:additionalStates:completionQueue:completionBlock:"
+ "captureCuratedCollectionsShortUserActionTargetPairWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:sessionSnapshot:dataModelInfoProviders:additionalStates:completionQueue:completionBlock:"
+ "captureEnterMapsShortUserActionTargetPairWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:sessionSnapshot:dataModelInfoProviders:additionalStates:completionQueue:completionBlock:"
+ "captureFamiliarRoutesOnlyWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:sessionSnapshot:dataModelInfoProviders:additionalStates:completionQueue:completionBlock:"
+ "captureMapViewEngagementWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:sessionSnapshot:dataModelInfoProviders:additionalStates:completionQueue:completionBlock:"
+ "captureMuninCameraUserActionShortOnlyWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:sessionSnapshot:dataModelInfoProviders:additionalStates:completionQueue:completionBlock:"
+ "captureMuninUserActionShortOnlyWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:sessionSnapshot:dataModelInfoProviders:additionalStates:completionQueue:completionBlock:"
+ "captureNearbyTransitShortUserActionTargetPairWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:sessionSnapshot:dataModelInfoProviders:additionalStates:completionQueue:completionBlock:"
+ "captureOfflineSessionlessUserActionTargetPairWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:sessionSnapshot:dataModelInfoProviders:additionalStates:completionQueue:completionBlock:"
+ "captureOfflineShortUserActionTargetPairWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:sessionSnapshot:dataModelInfoProviders:additionalStates:completionQueue:completionBlock:"
+ "capturePlaceCardRevealWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:sessionSnapshot:dataModelInfoProviders:additionalStates:completionQueue:completionBlock:"
+ "capturePlaceCardUserAction:target:value:mapItem:timestamp:resultIndex:targetID:providerID:animationID:actionURL:photoID:placeCardType:localizedMapItemCategory:availableActions:unactionableUIElements:modules:commingledRichProviderIds:actionRichProviderId:classification:snapShot:"
+ "capturePredExSessionlessUserActionTargetPairWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:sessionSnapshot:dataModelInfoProviders:additionalStates:completionQueue:completionBlock:"
+ "capturePredExShortUserActionTargetPairWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:sessionSnapshot:dataModelInfoProviders:additionalStates:completionQueue:completionBlock:"
+ "capturePriorityPlacecardActionShortUserActionsWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:sessionSnapshot:dataModelInfoProviders:additionalStates:completionQueue:completionBlock:"
+ "capturePriorityShortUserActionsWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:sessionSnapshot:dataModelInfoProviders:additionalStates:completionQueue:completionBlock:"
+ "captureRapSessionlessUserActionTargetPairWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:sessionSnapshot:dataModelInfoProviders:additionalStates:completionQueue:completionBlock:"
+ "captureRapShortAndSessionlessUserActionTargetPairWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:sessionSnapshot:dataModelInfoProviders:additionalStates:completionQueue:completionBlock:"
+ "captureRapUserActionShortOnlyWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:sessionSnapshot:dataModelInfoProviders:additionalStates:completionQueue:completionBlock:"
+ "captureSessionlessUserActionWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:sessionSnapshot:dataModelInfoProviders:additionalStates:completionQueue:completionBlock:"
+ "captureStandardShortWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:sessionSnapshot:dataModelInfoProviders:additionalStates:completionQueue:completionBlock:"
+ "captureStartEndNavWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:sessionSnapshot:dataModelInfoProviders:additionalStates:completionQueue:completionBlock:"
+ "captureTransitShortUserActionTargetPairWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:sessionSnapshot:dataModelInfoProviders:additionalStates:completionQueue:completionBlock:"
+ "captureUGCSessionlessUserActionTargetPairWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:sessionSnapshot:dataModelInfoProviders:additionalStates:completionQueue:completionBlock:"
+ "captureUGCShortUserActionTargetPairWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:sessionSnapshot:dataModelInfoProviders:additionalStates:completionQueue:completionBlock:"
+ "captureUgcDeleteLogsWithCertificates:signature:trigger:sessionSnapshot:additionalStates:providedDropRate:completionQueue:completionBlock:"
+ "captureUgcDeleteWithSignature:certificates:sessionSnapshot:trigger:queue:completion:"
+ "captureUserAction:target:value:dataModelInfoProviders:"
+ "captureUserAction:target:value:moduleType:moduleMetadata:classification:richProviderId:sessionSnapshot:modelInfoProviders:additionalStates:completionQueue:completionBlock:"
+ "captureUserAction:target:value:moduleType:moduleMetadata:richProviderId:sessionSnapshot:modelInfoProviders:additionalStates:completionQueue:completionBlock:"
+ "captureUserAction:target:value:placeActionDetails:sessionSnapshot:"
+ "captureUserAction:target:value:sessionSnapshot:"
+ "captureVisualIntelligenceShortUserActionsWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:sessionSnapshot:dataModelInfoProviders:additionalStates:completionQueue:completionBlock:"
+ "dailyCountsWithActionTargetTuple:actionTargetValue:appGroup:dataModelInfoProvider:"
+ "hasResults"
+ "initWithResultIndex:businessId:localSearchProviderId:isEnriched:pinType:isGuide:"
+ "initWithSearchHomeProvider:"
+ "initWithSearchResultsProvider:"
+ "initWithTapEventProvider:"
+ "isEnriched"
+ "isGuide"
+ "localSearchProviderId"
+ "navRelativeTimestamp"
+ "opaqueAppID"
+ "pinType"
+ "pinTypeFromAPPinType:"
+ "placeSummaryState"
+ "placeSummaryWithIterationBlock:"
+ "relativeTimestamp"
+ "resultTypeFromAPResultType:"
+ "resultsWithIterationBlock:"
+ "searchHomeDataModelProvider"
+ "searchHome_stateDisabled"
+ "searchResultBusinessId"
+ "searchResultIndex"
+ "searchResultsDataModelProvider"
+ "sequenceNumber"
+ "sessionCreateHour"
+ "sessionCreateTime"
+ "sessionID"
+ "sessionSalt"
+ "sessionStateFromSnapshot:"
+ "sessionType"
+ "setShareSessionWithMaps:"
+ "snapshot"
+ "snapshotForType:"
+ "snapshotTime"
+ "stateForType:dataModelInfoProviders:"
+ "tapEvent"
+ "tapEventDataModelProvider"
+ "v104@0:8i16i20@24@32@40@48@56@64@72@80@88@?96"
+ "v160@0:8i16i20@24@32d40i48Q52@60Q68@76@84i92@96@104@112@120@128@136@144@152"
+ "v60@0:8@16@24@32i40@44@?52"
+ "v76@0:8@16@24i32@36@44@52@60@?68"
+ "v96@0:8i16i20@24@32@40@48@56@64@72@80@?88"
+ "{GEOSessionID=\"_high\"Q\"_low\"Q}"
+ "{GEOSessionID=QQ}16@0:8"
- "+[GEOAPPortal(DailyUsageCodeGen) addCodeGenDailyCountsWithActionTargetTuple:actionTargetValue:appGroup:]"
- "+[GEOAPPortal(UserActionCodeGen) captureUserAction:target:value:moduleType:moduleMetadata:classification:richProviderId:additionalStates:completionQueue:completionBlock:]"
- "@36@0:8Q16@24i32"
- "addCodeGenDailyCountsWithActionTargetTuple:actionTargetValue:appGroup:"
- "addStaticDailyCountsWithActionTargetTuple:actionTargetValue:appGroup:"
- "captureAccountSessionlessUserActionTargetPairWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:additionalStates:completionQueue:completionBlock:"
- "captureArpPrivacyWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:additionalStates:completionQueue:completionBlock:"
- "captureCarplayUserActionWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:additionalStates:completionQueue:completionBlock:"
- "captureCuratedCollectionsSessionlessUserActionTargetPairRedactedCCStateWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:additionalStates:completionQueue:completionBlock:"
- "captureCuratedCollectionsSessionlessUserActionTargetPairWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:additionalStates:completionQueue:completionBlock:"
- "captureCuratedCollectionsShortUserActionTargetPairWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:additionalStates:completionQueue:completionBlock:"
- "captureEnterMapsShortUserActionTargetPairWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:additionalStates:completionQueue:completionBlock:"
- "captureFamiliarRoutesOnlyWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:additionalStates:completionQueue:completionBlock:"
- "captureMapViewEngagementWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:additionalStates:completionQueue:completionBlock:"
- "captureMuninCameraUserActionShortOnlyWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:additionalStates:completionQueue:completionBlock:"
- "captureMuninUserActionShortOnlyWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:additionalStates:completionQueue:completionBlock:"
- "captureNearbyTransitShortUserActionTargetPairWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:additionalStates:completionQueue:completionBlock:"
- "captureOfflineSessionlessUserActionTargetPairWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:additionalStates:completionQueue:completionBlock:"
- "captureOfflineShortUserActionTargetPairWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:additionalStates:completionQueue:completionBlock:"
- "capturePlaceCardRevealWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:additionalStates:completionQueue:completionBlock:"
- "capturePredExSessionlessUserActionTargetPairWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:additionalStates:completionQueue:completionBlock:"
- "capturePredExShortUserActionTargetPairWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:additionalStates:completionQueue:completionBlock:"
- "capturePredExTrainingWithChanceOfPrecipitation:chanceOfRain:chanceOfSnow:endTime:durationUntilEventEnd:durationUntilEventStart:startTime:temperature:timeOfDay:timeSinceBackgrounded:actualTransportMode:dayOfWeek:distanceFromHereToHome:distanceFromHereToOrigin:distanceFromHereToParkedCar:distanceFromHereToWork:distanceFromHere:distanceFromOriginToDestination:entryType:weatherType:mapType:predictedTransportMode:preferredTransportMode:isInBasemode:isCarplayConnected:isTourist:isTransitPossible:routePlanningScreenPresented:userLocationGeohash4:isVehicleBluetoothConnected:weatherAqi:modelName:modelVersion:modelTrainedDate:"
- "capturePredExTrainingWithChanceOfPrecipitation:chanceOfRain:chanceOfSnow:endTime:durationUntilEventEnd:durationUntilEventStart:startTime:temperature:timeOfDay:timeSinceBackgrounded:actualTransportMode:dayOfWeek:distanceFromHereToHome:distanceFromHereToOrigin:distanceFromHereToParkedCar:distanceFromHereToWork:distanceFromHere:distanceFromOriginToDestination:entryType:weatherType:mapType:predictedTransportMode:preferredTransportMode:isInBasemode:isTourist:isCarplayConnected:isTransitPossible:routePlanningScreenPresented:userLocation:isVehicleBluetoothConnected:weatherAqi:modelName:modelVersion:modelTrainedDate:"
- "capturePredExTrainingWithChanceOfPrecipitation:chanceOfRain:chanceOfSnow:endTime:durationUntilEventEnd:durationUntilEventStart:startTime:temperature:timeOfDay:timeSinceBackgrounded:actualTransportMode:dayOfWeek:distanceFromHereToHome:distanceFromHereToOrigin:distanceFromHereToParkedCar:distanceFromHereToWork:distanceFromHere:distanceFromOriginToDestination:entryType:weatherType:mapType:predictedTransportMode:preferredTransportMode:isTourist:isCarplayConnected:isTransitPossible:userLocation:isVehicleBluetoothConnected:weatherAqi:"
- "capturePredExTrainingWithChanceOfPrecipitation:chanceOfRain:chanceOfSnow:endTime:durationUntilEventEnd:durationUntilEventStart:startTime:temperature:timeOfDay:timeSinceBackgrounded:actualTransportMode:dayOfWeek:distanceFromHereToHome:distanceFromHereToOrigin:distanceFromHereToParkedCar:distanceFromHereToWork:distanceFromHere:distanceFromOriginToDestination:entryType:weatherType:mapType:predictedTransportMode:preferredTransportMode:isTourist:isCarplayConnected:isTransitPossible:userLocation:isVehicleBluetoothConnected:weatherAqi:modelName:modelVersion:modelTrainedDate:"
- "capturePriorityPlacecardActionShortUserActionsWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:additionalStates:completionQueue:completionBlock:"
- "capturePriorityShortUserActionsWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:additionalStates:completionQueue:completionBlock:"
- "captureRapSessionlessUserActionTargetPairWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:additionalStates:completionQueue:completionBlock:"
- "captureRapShortAndSessionlessUserActionTargetPairWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:additionalStates:completionQueue:completionBlock:"
- "captureRapUserActionShortOnlyWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:additionalStates:completionQueue:completionBlock:"
- "captureSessionlessUserActionWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:additionalStates:completionQueue:completionBlock:"
- "captureStandardShortWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:additionalStates:completionQueue:completionBlock:"
- "captureStartEndNavWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:additionalStates:completionQueue:completionBlock:"
- "captureTransitShortUserActionTargetPairWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:additionalStates:completionQueue:completionBlock:"
- "captureUGCSessionlessUserActionTargetPairWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:additionalStates:completionQueue:completionBlock:"
- "captureUGCShortUserActionTargetPairWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:additionalStates:completionQueue:completionBlock:"
- "captureUgcDeleteLogsWithCertificates:signature:trigger:additionalStates:providedDropRate:completionQueue:completionBlock:"
- "captureUserAction:target:value:moduleType:moduleMetadata:classification:richProviderId:additionalStates:completionQueue:completionBlock:"
- "captureVisualIntelligenceShortUserActionsWithAction:target:value:moduleType:moduleMetadata:classification:richProviderId:additionalStates:completionQueue:completionBlock:"
- "dailyCountsWithActionTargetTuple:actionTargetValue:appGroup:"
- "v200@0:8@16@24@32@40@48@56@64@72@80@88i96@100i108i112i116i120i124i128i132i136i140i144i148@152@160@168@176@184@192"
- "v220@0:8@16@24@32@40@48@56@64@72@80@88i96@100i108i112i116i120i124i128i132i136i140i144i148@152@160@168@176@184@192i200@204@212"
- "v236@0:8@16@24@32@40@48@56@64@72@80@88i96@100i108i112i116i120i124i128i132i136i140i144i148@152@160@168@176@184@192@200@208i216@220@228"
- "v88@0:8i16i20@24@32@40@48@56@64@72@?80"

```
