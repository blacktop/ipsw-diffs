## WiFiAnalytics

> `/System/Library/PrivateFrameworks/WiFiAnalytics.framework/WiFiAnalytics`

```diff

-788.1.0.0.0
-  __TEXT.__text: 0x12f2c4
-  __TEXT.__auth_stubs: 0x1030
-  __TEXT.__objc_methlist: 0xf2f0
-  __TEXT.__const: 0x3a0
+795.19.0.0.0
+  __TEXT.__text: 0x14c2e0
+  __TEXT.__auth_stubs: 0x1010
+  __TEXT.__objc_methlist: 0xfe18
+  __TEXT.__const: 0x390
   __TEXT.__dlopen_cstrs: 0x56
-  __TEXT.__cstring: 0x121b7
-  __TEXT.__oslogstring: 0xe823
+  __TEXT.__cstring: 0x1385b
+  __TEXT.__oslogstring: 0x1058f
   __TEXT.__constg_swiftt: 0x1e0
-  __TEXT.__swift5_typeref: 0x14b
+  __TEXT.__swift5_typeref: 0x145
   __TEXT.__swift5_reflstr: 0xb1
   __TEXT.__swift5_fieldmd: 0x88
-  __TEXT.__swift5_capture: 0x2d0
+  __TEXT.__swift5_capture: 0x1b0
   __TEXT.__swift5_types: 0x4
-  __TEXT.__gcc_except_tab: 0x2d88
-  __TEXT.__unwind_info: 0x26e0
-  __TEXT.__eh_frame: 0x548
-  __TEXT.__objc_classname: 0xec1
-  __TEXT.__objc_methname: 0x1f539
-  __TEXT.__objc_methtype: 0x3e14
-  __TEXT.__objc_stubs: 0xcd00
-  __DATA_CONST.__got: 0x740
-  __DATA_CONST.__const: 0x1f00
-  __DATA_CONST.__objc_classlist: 0x400
-  __DATA_CONST.__objc_catlist: 0x8
+  __TEXT.__gcc_except_tab: 0x2f58
+  __TEXT.__unwind_info: 0x2ff8
+  __TEXT.__eh_frame: 0x398
+  __TEXT.__objc_classname: 0xf79
+  __TEXT.__objc_methname: 0x21017
+  __TEXT.__objc_methtype: 0x3fb4
+  __TEXT.__objc_stubs: 0xe320
+  __DATA_CONST.__got: 0x7a0
+  __DATA_CONST.__const: 0x2140
+  __DATA_CONST.__objc_classlist: 0x438
+  __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x8210
-  __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x2d8
-  __DATA_CONST.__objc_arraydata: 0x490
-  __AUTH_CONST.__auth_got: 0x828
-  __AUTH_CONST.__const: 0x1670
-  __AUTH_CONST.__cfstring: 0xd500
-  __AUTH_CONST.__objc_const: 0x15258
-  __AUTH_CONST.__objc_intobj: 0x240
-  __AUTH_CONST.__objc_arrayobj: 0x5d0
-  __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH.__objc_data: 0x458
-  __DATA.__objc_ivar: 0xf8c
-  __DATA.__data: 0x3f0
+  __DATA_CONST.__objc_selrefs: 0x87d0
+  __DATA_CONST.__objc_protorefs: 0x10
+  __DATA_CONST.__objc_superrefs: 0x318
+  __DATA_CONST.__objc_arraydata: 0x8e0
+  __AUTH_CONST.__auth_got: 0x818
+  __AUTH_CONST.__const: 0x1450
+  __AUTH_CONST.__cfstring: 0xe640
+  __AUTH_CONST.__objc_const: 0x15c78
+  __AUTH_CONST.__objc_arrayobj: 0x768
+  __AUTH_CONST.__objc_intobj: 0x480
+  __AUTH_CONST.__objc_dictobj: 0x50
+  __AUTH.__objc_data: 0x4f8
+  __DATA.__objc_ivar: 0xf94
+  __DATA.__data: 0x3a0
   __DATA.__bss: 0x1c
   __DATA.__common: 0x11d0
-  __DATA_DIRTY.__objc_data: 0x25f8
-  __DATA_DIRTY.__data: 0x48
-  __DATA_DIRTY.__bss: 0x150
+  __DATA_DIRTY.__objc_ivar: 0x9c
+  __DATA_DIRTY.__objc_data: 0x2788
+  __DATA_DIRTY.__data: 0x98
+  __DATA_DIRTY.__bss: 0x160
   __DATA_DIRTY.__common: 0x28
   - /System/Library/Frameworks/CoreData.framework/CoreData
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 16F98357-0048-3CD3-A288-2AD124B1B05E
-  Functions: 5641
-  Symbols:   15443
-  CStrings:  11868
+  UUID: DE059BE6-13FE-302C-83AB-15519D616C86
+  Functions: 5881
+  Symbols:   16200
+  CStrings:  12573
 
Symbols:
+ +[LeaveMO unusedSuperEntityProperties]
+ +[LeaveMO(CoreDataProperties) fetchRequest]
+ +[LinkChangePolicyHandler processJoinEvent:on:]
+ +[UsageHelper dateFormatterQueue]
+ +[UsagePoliciesHandler _calculateTDEdgeParamsVersion]
+ +[UsagePoliciesHandler _getCurrentAutoLeaveRssiPolicyType]
+ +[UsagePoliciesHandler tdEdgeParamsVersionAsString:]
+ +[UsagePoliciesHandler tdEdgeParamsVersion]
+ +[WADeviceAnalyticsClient availableEventsWithError:]
+ +[WADeviceAnalyticsClient joinReasonAsString:]
+ +[WADeviceAnalyticsClient joinStatusAsString:]
+ +[WADeviceAnalyticsClient leaveReasonAsString:]
+ +[WADeviceAnalyticsClient motionStateAsString:]
+ +[WADeviceAnalyticsClient roamReasonAsString:]
+ +[WADeviceAnalyticsClient roamStatusAsString:]
+ +[WADeviceAnalyticsClient sharedDeviceAnalyticsClientWithCustomStore:]
+ +[WADeviceAnalyticsDatedRecord unusedSuperEntityProperties]
+ +[WADeviceAnalyticsDiagnosticStateRecord unusedSuperEntityProperties]
+ +[WADeviceAnalyticsFaultRecord unusedSuperEntityProperties]
+ +[WADeviceAnalyticsJoinRecord joinFailureAsString:]
+ +[WADeviceAnalyticsJoinRecord joinReasonAsString:]
+ +[WADeviceAnalyticsLinkTestRecord unusedSuperEntityProperties]
+ +[WADeviceAnalyticsRecoveryRecord unusedSuperEntityProperties]
+ +[WADeviceAnalytics_Entity_Property propertyUsedAsFilterIn:]
+ +[WADeviceAnalytics_Entity_Property propertyWith:]
+ +[WADeviceAnalytics_Entity_Property useAsDescription:]
+ +[WADeviceAnalytics_Event eventDescription:from:withError:]
+ +[WADeviceAnalytics_Event eventsIn:withPredicate:]
+ +[WADeviceAnalytics_Event sequenceEdgeEventsIn:]
+ +[WADeviceAnalytics_Event sequenceEndEventsIn:]
+ +[WADeviceAnalytics_Event sequenceEventsIn:]
+ +[WADeviceAnalytics_Event sequenceStartEventsIn:]
+ +[WADeviceAnalytics_Event shallowCopyOfUsedEventsIn:]
+ +[WADeviceAnalytics_Event useAsDescription:]
+ +[WADeviceAnalytics_Event useAsEnd:inEvents:withError:]
+ +[WADeviceAnalytics_Event useAsEvent:inEvents:withError:]
+ +[WADeviceAnalytics_Event useAsStart:inEvents:withError:]
+ +[WAEventLeave leaveReasonAsString:]
+ +[WAMigrationUtils addMissingRecoveryRelationships:withError:]
+ +[WAMigrationUtils copyRoamTargetColumnsAddMissingRoamRelationships:withError:]
+ +[WAMigrationUtils mapOldJoinReason:andWAManualAssociationTypeMaskToJoinReason:]
+ +[WAMigrationUtils migrationManagerTo:from:withError:]
+ +[WAMigrationUtils modelWithHash:withError:]
+ +[WAMigrationUtils referenceForModel:withError:]
+ +[WAMigrationUtils remodelJoinReasonOnContext:withError:]
+ +[WAMigrationUtils stagedMigrationManagerIfNeededForMOM:andStore:withError:]
+ +[WAMigrationUtils tryToMigrate:using:withError:]
+ +[WAPersistentContainer availableEventsWithError:]
+ +[WAPersistentContainer predicateForIsSubEntity]
+ +[WAPersistentContainer validateEntityForGroupbyRequest:]
+ +[WAUtil defaultKeysAllowedOnCustomerInstalls]
+ +[WAUtil enableCoreDataConcurrencyDebug]
+ +[WAUtil filterArrayForDottedKeyPaths:]
+ +[WAUtil filterArrayForKeys:]
+ +[WAUtil getWeekStartForDate:]
+ -[AnalyticsProcessor event:andResetMoc:andRunPostProcessing:withError:]
+ -[AnalyticsProcessor processCachedFaultsAndResetMoc:]
+ -[AnalyticsProcessor setTimeSeriesPoliciesHandler:]
+ -[AnalyticsProcessor timeSeriesPoliciesHandler]
+ -[AnalyticsProcessor updateBandResidencyWithReason:]
+ -[AnalyticsProcessor updateContextAwareTDPolicies:]
+ -[AnalyticsReader eventSequencesFor:since:until:sortingAsc:withError:]
+ -[AnalyticsReader isBandRelevantForSSID:onBand:]
+ -[LeaveMO attributeDescription:]
+ -[NSManagedObject(WiFiAnalytics) _allAttributes]
+ -[NSManagedObject(WiFiAnalytics) dictionaryRepresentationFor:]
+ -[RoamMO attributeDescription:]
+ -[TimeseriesPoliciesHandler .cxx_destruct]
+ -[TimeseriesPoliciesHandler checkRejoinAfterLeaveEvent:In:]
+ -[TimeseriesPoliciesHandler configureContextAwareTDEventsToFetchWithError:]
+ -[TimeseriesPoliciesHandler container]
+ -[TimeseriesPoliciesHandler findEdgeBSSFromRoamEventBeforeLeaveEvent:In:]
+ -[TimeseriesPoliciesHandler findEdgeBSSIn:byCheckingLeaveEventsUntil:]
+ -[TimeseriesPoliciesHandler findEventsIn:aroundIndex:noEarlierThan:noLaterThan:withPredicate:findingAll:]
+ -[TimeseriesPoliciesHandler findNextLeaveEventFrom:In:]
+ -[TimeseriesPoliciesHandler findRoamEventBeforeLeaveEvent:In:]
+ -[TimeseriesPoliciesHandler initWithPersistentContainer:]
+ -[TimeseriesPoliciesHandler setContainer:]
+ -[TimeseriesPoliciesHandler updateBSSMOWithEdgeBSSSet:tdEdgeParamsVersion:withError:]
+ -[TimeseriesPoliciesHandler updateEdgeBssWithReason:at:timeSpan:]
+ -[TimeseriesPoliciesHandler updatePoliciesTableWithReason:withPolicyType:withOutcome:]
+ -[UsagePoliciesHandler _updateIsBandResidencyLow:forBand:onNetwork:counters:]
+ -[UsagePoliciesHandler canRunContextAwareTDPolicyNow]
+ -[UsagePoliciesHandler canRunPolicyAtCurrentTimeForPolicyType:timespan:]
+ -[UsagePoliciesHandler isContextAwareTDPolicyExecutionIntervalSufficient]
+ -[UsagePoliciesHandler isContextAwareTDPolicyLastWeekWiFiUsageSufficient]
+ -[UsagePoliciesHandler resetAllInstancesUsageToZero:forTimeSpan:]
+ -[UsagePoliciesHandler submitBSSEventsFor:]
+ -[UsagePoliciesHandler submitNetworkEventsFor:]
+ -[UsagePoliciesHandler totalWiFiUsageInTimeSpan:around:]
+ -[UsagePoliciesHandler updateAutoLeaveRssiWithReason:]
+ -[UsagePoliciesHandler updateBandResidencyWithReason:]
+ -[UsagePoliciesHandler updatePoliciesTableWithPolicyType:reason:dateLessThen:object:timeSpan:]
+ -[WAClient asyncSubmitEvent:andDeferReclaimMem:andRunPostProcessing:uponCompletionDo:]
+ -[WAClient asyncSubmitEvent:uponCompletionDo:]
+ -[WAClient submitEvent:andDeferReclaimMem:andRunPostProcessing:withError:]
+ -[WAClient submitEvent:async:andDeferReclaimMem:andRunPostProcessing:uponCompletionDo:]
+ -[WAClient submitEvent:withError:]
+ -[WADeviceAnalyticsClient _dhcpEventOnBssid:ssid:serverInfo:at:with:andDeferReclaimMem:]
+ -[WADeviceAnalyticsClient _diagnosticEventAt:with:andDeferReclaimMem:]
+ -[WADeviceAnalyticsClient _event:andDeferReclaimMem:andRunPostProcessing:withError:]
+ -[WADeviceAnalyticsClient _faultEventOn:at:with:andDeferReclaimMem:]
+ -[WADeviceAnalyticsClient _geoTagEventOnBssid:ssid:lat:lon:at:andDeferReclaimMem:andRunPostProcessing:]
+ -[WADeviceAnalyticsClient _joinEventOnBssid:ssid:at:with:andDeferReclaimMem:andRunPostProcessing:]
+ -[WADeviceAnalyticsClient _linkTestEventOn:at:with:andDeferReclaimMem:]
+ -[WADeviceAnalyticsClient _lqmEvent:on:at:andDeferReclaimMem:]
+ -[WADeviceAnalyticsClient _recoveryEventOnBssid:at:with:andDeferReclaimMem:]
+ -[WADeviceAnalyticsClient _removeKnownNetworkEvent:at:andDeferReclaimMem:]
+ -[WADeviceAnalyticsClient _scanResultEventWith:ssid:whileOn:at:with:andDeferReclaimMem:]
+ -[WADeviceAnalyticsClient _updateBSS:withParsedBeacon:andDeferReclaimMem:]
+ -[WADeviceAnalyticsClient _updateNetwork:switchedFrom:at:andDeferReclaimMem:]
+ -[WADeviceAnalyticsClient asyncAddEvent:andDeferReclaimMem:andRunPostProcessing:uponCompletionDo:]
+ -[WADeviceAnalyticsClient asyncAddEvent:uponCompletionDo:]
+ -[WADeviceAnalyticsClient event:andDeferReclaimMem:andRunPostProcessing:withError:]
+ -[WADeviceAnalyticsClient event:withError:]
+ -[WADeviceAnalyticsClient eventSequencesFor:since:until:sortingAsc:withError:]
+ -[WADeviceAnalyticsClient initWithStore:]
+ -[WADeviceAnalyticsClient isBandRelevantForSSID:onBand:]
+ -[WADeviceAnalyticsClient prunableEntitiesWithDate]
+ -[WADeviceAnalyticsClient setCachedParamsWithBssid:ssid:]
+ -[WADeviceAnalyticsClient updateCachedParamsIfNeeded:]
+ -[WADeviceAnalyticsDatedRecord attributeDescription:]
+ -[WADeviceAnalyticsJoinRecord attributeDescription:]
+ -[WADeviceAnalytics_Entity_Property .cxx_destruct]
+ -[WADeviceAnalytics_Entity_Property copyWithZone:]
+ -[WADeviceAnalytics_Entity_Property description]
+ -[WADeviceAnalytics_Entity_Property dontUseProperty]
+ -[WADeviceAnalytics_Entity_Property filterPredicate]
+ -[WADeviceAnalytics_Entity_Property propertyPath]
+ -[WADeviceAnalytics_Entity_Property setFilterPredicate:]
+ -[WADeviceAnalytics_Entity_Property setPropertyPath:]
+ -[WADeviceAnalytics_Entity_Property setUseAs:]
+ -[WADeviceAnalytics_Entity_Property useAs]
+ -[WADeviceAnalytics_Event .cxx_destruct]
+ -[WADeviceAnalytics_Event description]
+ -[WADeviceAnalytics_Event dontUseEvent]
+ -[WADeviceAnalytics_Event entityFilter]
+ -[WADeviceAnalytics_Event entity]
+ -[WADeviceAnalytics_Event eventType]
+ -[WADeviceAnalytics_Event initWithEntity:]
+ -[WADeviceAnalytics_Event initWithUsedPropertiesFromUsedEvent:]
+ -[WADeviceAnalytics_Event keyPathsToFetch]
+ -[WADeviceAnalytics_Event propertiesToFetch]
+ -[WADeviceAnalytics_Event properties]
+ -[WADeviceAnalytics_Event relationshipKeyPathsToFetch]
+ -[WADeviceAnalytics_Event setEntity:]
+ -[WADeviceAnalytics_Event setEntityFilter:]
+ -[WADeviceAnalytics_Event setEventType:]
+ -[WADeviceAnalytics_Event setKeyPathsToFetch:]
+ -[WADeviceAnalytics_Event setProperties:]
+ -[WADeviceAnalytics_Event setPropertiesToFetch:]
+ -[WADeviceAnalytics_Event setPropertiesToFetch:withError:]
+ -[WADeviceAnalytics_Event setRelationshipKeyPathsToFetch:]
+ -[WADeviceAnalytics_Event setUseAs:]
+ -[WADeviceAnalytics_Event useAs]
+ -[WADeviceAnalytics_Event useEventAsSequenceEnd]
+ -[WADeviceAnalytics_Event useEventAsSequenceEvent]
+ -[WADeviceAnalytics_Event useEventAsSequenceStart]
+ -[WADeviceAnalytics_Event usedPropertiesDescription]
+ -[WADeviceAnalytics_EventSequence .cxx_destruct]
+ -[WADeviceAnalytics_EventSequence asc]
+ -[WADeviceAnalytics_EventSequence description]
+ -[WADeviceAnalytics_EventSequence endEventMO]
+ -[WADeviceAnalytics_EventSequence endEvent]
+ -[WADeviceAnalytics_EventSequence eventMOs]
+ -[WADeviceAnalytics_EventSequence events]
+ -[WADeviceAnalytics_EventSequence initWithStartRecord:endRecord:sequenceRecords:asc:forEvents:forExport:]
+ -[WADeviceAnalytics_EventSequence setAsc:]
+ -[WADeviceAnalytics_EventSequence setEndEvent:]
+ -[WADeviceAnalytics_EventSequence setEndEventMO:]
+ -[WADeviceAnalytics_EventSequence setEventMOs:]
+ -[WADeviceAnalytics_EventSequence setEvents:]
+ -[WADeviceAnalytics_EventSequence setStartEvent:]
+ -[WADeviceAnalytics_EventSequence setStartEventMO:]
+ -[WADeviceAnalytics_EventSequence startEventMO]
+ -[WADeviceAnalytics_EventSequence startEvent]
+ -[WAEvent .cxx_destruct]
+ -[WAEvent _processEventOnPersistentContainer:withError:]
+ -[WAEvent band]
+ -[WAEvent beaconPerHistory]
+ -[WAEvent beaconSchedHistory]
+ -[WAEvent bssid]
+ -[WAEvent bw]
+ -[WAEvent ccaHistory]
+ -[WAEvent channel]
+ -[WAEvent description]
+ -[WAEvent dictionaryForCA]
+ -[WAEvent entity]
+ -[WAEvent eventDate]
+ -[WAEvent eventNameForCA]
+ -[WAEvent fwTxFramesHistory]
+ -[WAEvent fwTxPerHistory]
+ -[WAEvent initWithEntity:bssid:at:withLqmHistory:]
+ -[WAEvent lqmHistoriesDescription]
+ -[WAEvent motionState]
+ -[WAEvent noiseHistory]
+ -[WAEvent processEventOnPersistentContainer:andRunPostprocessing:withError:]
+ -[WAEvent reason]
+ -[WAEvent rssiHistory]
+ -[WAEvent rssi]
+ -[WAEvent setBand:]
+ -[WAEvent setBeaconPerHistory:]
+ -[WAEvent setBeaconSchedHistory:]
+ -[WAEvent setBssid:]
+ -[WAEvent setBw:]
+ -[WAEvent setCcaHistory:]
+ -[WAEvent setChannel:]
+ -[WAEvent setEntity:]
+ -[WAEvent setEventDate:]
+ -[WAEvent setFwTxFramesHistory:]
+ -[WAEvent setFwTxPerHistory:]
+ -[WAEvent setMotionState:]
+ -[WAEvent setNoiseHistory:]
+ -[WAEvent setReason:]
+ -[WAEvent setRssi:]
+ -[WAEvent setRssiHistory:]
+ -[WAEvent setSnrHistory:]
+ -[WAEvent setStatus:]
+ -[WAEvent setSubreason:]
+ -[WAEvent setTxFrameHistory:]
+ -[WAEvent setTxPerHistory:]
+ -[WAEvent snrHistory]
+ -[WAEvent status]
+ -[WAEvent submitEventToCA]
+ -[WAEvent subreason]
+ -[WAEvent txFrameHistory]
+ -[WAEvent txPerHistory]
+ -[WAEvent updateRecord:]
+ -[WAEventLQMHistory .cxx_destruct]
+ -[WAEventLQMHistory beaconPerHistory]
+ -[WAEventLQMHistory beaconSchedHistory]
+ -[WAEventLQMHistory ccaHistory]
+ -[WAEventLQMHistory fwTxFramesHistory]
+ -[WAEventLQMHistory fwTxPerHistory]
+ -[WAEventLQMHistory init]
+ -[WAEventLQMHistory noiseHistory]
+ -[WAEventLQMHistory rssiHistory]
+ -[WAEventLQMHistory setBeaconPerHistory:]
+ -[WAEventLQMHistory setBeaconSchedHistory:]
+ -[WAEventLQMHistory setCcaHistory:]
+ -[WAEventLQMHistory setFwTxFramesHistory:]
+ -[WAEventLQMHistory setFwTxPerHistory:]
+ -[WAEventLQMHistory setNoiseHistory:]
+ -[WAEventLQMHistory setRssiHistory:]
+ -[WAEventLQMHistory setSnrHistory:]
+ -[WAEventLQMHistory setTxFrameHistory:]
+ -[WAEventLQMHistory setTxPerHistory:]
+ -[WAEventLQMHistory snrHistory]
+ -[WAEventLQMHistory txFrameHistory]
+ -[WAEventLQMHistory txPerHistory]
+ -[WAEventLeave associationDuration]
+ -[WAEventLeave description]
+ -[WAEventLeave initWithBssid:ssid:at:data:withLqmHistory:withError:]
+ -[WAEventLeave isInVoluntary]
+ -[WAEventLeave processEventOnPersistentContainer:andRunPostprocessing:withError:]
+ -[WAEventLeave processEventOnPersistentContainer:withError:]
+ -[WAEventLeave setAssociationDuration:]
+ -[WAEventLeave setIsInVoluntary:]
+ -[WAEventLeave updateRecord:]
+ -[WAEventRoamStatus description]
+ -[WAEventRoamStatus dictionaryForCA]
+ -[WAEventRoamStatus eventNameForCA]
+ -[WAEventRoamStatus initWithDriverEvent:andDeviceCapabilities:at:withLqmHistory:withError:]
+ -[WAEventRoamStatus processEventOnPersistentContainer:andRunPostprocessing:withError:]
+ -[WAPersistentContainer _eventSequencesFor:withSequenceStartEvents:withSequenceEndEvents:withSequenceEvents:since:until:sortingAsc:forExport:withError:]
+ -[WAPersistentContainer _prunableEntitiesWithDate]
+ -[WAPersistentContainer eventSequencesFor:since:until:sortingAsc:forExport:withError:]
+ -[WAPersistentContainer eventSequencesFor:since:until:sortingAsc:withError:]
+ -[WAPersistentContainer fetchDatedEvents:since:until:ascending:withError:]
+ -[WiFiAnalyticsAWDWiFiDPSNANSnapshot hasNanInfraImpact]
+ -[WiFiAnalyticsAWDWiFiDPSNANSnapshot nanInfraImpact]
+ -[WiFiAnalyticsAWDWiFiDPSNANSnapshot setHasNanInfraImpact:]
+ -[WiFiAnalyticsAWDWiFiDPSNANSnapshot setNanInfraImpact:]
+ GCC_except_table101
+ GCC_except_table103
+ GCC_except_table106
+ GCC_except_table108
+ GCC_except_table115
+ GCC_except_table117
+ GCC_except_table119
+ GCC_except_table127
+ GCC_except_table128
+ GCC_except_table129
+ GCC_except_table137
+ GCC_except_table143
+ GCC_except_table149
+ GCC_except_table156
+ GCC_except_table159
+ GCC_except_table161
+ GCC_except_table162
+ GCC_except_table168
+ GCC_except_table173
+ GCC_except_table174
+ GCC_except_table179
+ GCC_except_table180
+ GCC_except_table185
+ GCC_except_table186
+ GCC_except_table191
+ GCC_except_table192
+ GCC_except_table197
+ GCC_except_table198
+ GCC_except_table209
+ GCC_except_table24
+ GCC_except_table28
+ GCC_except_table280
+ GCC_except_table30
+ GCC_except_table32
+ GCC_except_table56
+ GCC_except_table62
+ GCC_except_table89
+ GCC_except_table93
+ GCC_except_table95
+ OBJC_IVAR_$_WiFiAnalyticsAWDWiFiDPSNANSnapshot._nanInfraImpact
+ _Apple80211ErrToStr
+ _NSPersistentStoreStagedMigrationManagerOptionKey
+ _NSStoreModelVersionHashesKey
+ _NSStringFromClass
+ _OBJC_CLASS_$_LeaveMO
+ _OBJC_CLASS_$_NSCustomMigrationStage
+ _OBJC_CLASS_$_NSLightweightMigrationStage
+ _OBJC_CLASS_$_NSManagedObjectModelReference
+ _OBJC_CLASS_$_NSPersistentStoreCoordinator
+ _OBJC_CLASS_$_NSStagedMigrationManager
+ _OBJC_CLASS_$_TimeseriesPoliciesHandler
+ _OBJC_CLASS_$_WADeviceAnalytics_Entity_Property
+ _OBJC_CLASS_$_WADeviceAnalytics_Event
+ _OBJC_CLASS_$_WADeviceAnalytics_EventSequence
+ _OBJC_CLASS_$_WAEvent
+ _OBJC_CLASS_$_WAEventLQMHistory
+ _OBJC_CLASS_$_WAEventLeave
+ _OBJC_CLASS_$_WAMigrationUtils
+ _OBJC_IVAR_$_AnalyticsProcessor._timeSeriesPoliciesHandler
+ _OBJC_IVAR_$_TimeseriesPoliciesHandler._container
+ _OBJC_IVAR_$_WADeviceAnalytics_Entity_Property._filterPredicate
+ _OBJC_IVAR_$_WADeviceAnalytics_Entity_Property._propertyPath
+ _OBJC_IVAR_$_WADeviceAnalytics_Entity_Property._useAs
+ _OBJC_IVAR_$_WADeviceAnalytics_Event._entity
+ _OBJC_IVAR_$_WADeviceAnalytics_Event._entityFilter
+ _OBJC_IVAR_$_WADeviceAnalytics_Event._eventType
+ _OBJC_IVAR_$_WADeviceAnalytics_Event._keyPathsToFetch
+ _OBJC_IVAR_$_WADeviceAnalytics_Event._properties
+ _OBJC_IVAR_$_WADeviceAnalytics_Event._propertiesToFetch
+ _OBJC_IVAR_$_WADeviceAnalytics_Event._relationshipKeyPathsToFetch
+ _OBJC_IVAR_$_WADeviceAnalytics_Event._useAs
+ _OBJC_IVAR_$_WADeviceAnalytics_EventSequence._asc
+ _OBJC_IVAR_$_WADeviceAnalytics_EventSequence._endEvent
+ _OBJC_IVAR_$_WADeviceAnalytics_EventSequence._endEventMO
+ _OBJC_IVAR_$_WADeviceAnalytics_EventSequence._eventMOs
+ _OBJC_IVAR_$_WADeviceAnalytics_EventSequence._events
+ _OBJC_IVAR_$_WADeviceAnalytics_EventSequence._startEvent
+ _OBJC_IVAR_$_WADeviceAnalytics_EventSequence._startEventMO
+ _OBJC_IVAR_$_WAEvent._band
+ _OBJC_IVAR_$_WAEvent._beaconPerHistory
+ _OBJC_IVAR_$_WAEvent._beaconSchedHistory
+ _OBJC_IVAR_$_WAEvent._bssid
+ _OBJC_IVAR_$_WAEvent._bw
+ _OBJC_IVAR_$_WAEvent._ccaHistory
+ _OBJC_IVAR_$_WAEvent._channel
+ _OBJC_IVAR_$_WAEvent._entity
+ _OBJC_IVAR_$_WAEvent._eventDate
+ _OBJC_IVAR_$_WAEvent._fwTxFramesHistory
+ _OBJC_IVAR_$_WAEvent._fwTxPerHistory
+ _OBJC_IVAR_$_WAEvent._motionState
+ _OBJC_IVAR_$_WAEvent._noiseHistory
+ _OBJC_IVAR_$_WAEvent._reason
+ _OBJC_IVAR_$_WAEvent._rssi
+ _OBJC_IVAR_$_WAEvent._rssiHistory
+ _OBJC_IVAR_$_WAEvent._snrHistory
+ _OBJC_IVAR_$_WAEvent._status
+ _OBJC_IVAR_$_WAEvent._subreason
+ _OBJC_IVAR_$_WAEvent._txFrameHistory
+ _OBJC_IVAR_$_WAEvent._txPerHistory
+ _OBJC_IVAR_$_WAEventLQMHistory._beaconPerHistory
+ _OBJC_IVAR_$_WAEventLQMHistory._beaconSchedHistory
+ _OBJC_IVAR_$_WAEventLQMHistory._ccaHistory
+ _OBJC_IVAR_$_WAEventLQMHistory._fwTxFramesHistory
+ _OBJC_IVAR_$_WAEventLQMHistory._fwTxPerHistory
+ _OBJC_IVAR_$_WAEventLQMHistory._noiseHistory
+ _OBJC_IVAR_$_WAEventLQMHistory._rssiHistory
+ _OBJC_IVAR_$_WAEventLQMHistory._snrHistory
+ _OBJC_IVAR_$_WAEventLQMHistory._txFrameHistory
+ _OBJC_IVAR_$_WAEventLQMHistory._txPerHistory
+ _OBJC_IVAR_$_WAEventLeave._associationDuration
+ _OBJC_IVAR_$_WAEventLeave._isInVoluntary
+ _OBJC_METACLASS_$_LeaveMO
+ _OBJC_METACLASS_$_TimeseriesPoliciesHandler
+ _OBJC_METACLASS_$_WADeviceAnalytics_Entity_Property
+ _OBJC_METACLASS_$_WADeviceAnalytics_Event
+ _OBJC_METACLASS_$_WADeviceAnalytics_EventSequence
+ _OBJC_METACLASS_$_WAEvent
+ _OBJC_METACLASS_$_WAEventLQMHistory
+ _OBJC_METACLASS_$_WAEventLeave
+ _OBJC_METACLASS_$_WAMigrationUtils
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_NSManagedObject_$_WiFiAnalytics
+ __OBJC_$_CATEGORY_NSManagedObject_$_WiFiAnalytics
+ __OBJC_$_CLASS_METHODS_LeaveMO(CoreDataProperties)
+ __OBJC_$_CLASS_METHODS_UsagePoliciesHandler
+ __OBJC_$_CLASS_METHODS_WADeviceAnalytics_Entity_Property
+ __OBJC_$_CLASS_METHODS_WADeviceAnalytics_Event
+ __OBJC_$_CLASS_METHODS_WAEventLeave
+ __OBJC_$_CLASS_METHODS_WAMigrationUtils
+ __OBJC_$_INSTANCE_METHODS_LeaveMO
+ __OBJC_$_INSTANCE_METHODS_RoamMO
+ __OBJC_$_INSTANCE_METHODS_TimeseriesPoliciesHandler
+ __OBJC_$_INSTANCE_METHODS_WADeviceAnalytics_Entity_Property
+ __OBJC_$_INSTANCE_METHODS_WADeviceAnalytics_Event
+ __OBJC_$_INSTANCE_METHODS_WADeviceAnalytics_EventSequence
+ __OBJC_$_INSTANCE_METHODS_WAEvent
+ __OBJC_$_INSTANCE_METHODS_WAEventLQMHistory
+ __OBJC_$_INSTANCE_METHODS_WAEventLeave
+ __OBJC_$_INSTANCE_VARIABLES_TimeseriesPoliciesHandler
+ __OBJC_$_INSTANCE_VARIABLES_WADeviceAnalytics_Entity_Property
+ __OBJC_$_INSTANCE_VARIABLES_WADeviceAnalytics_Event
+ __OBJC_$_INSTANCE_VARIABLES_WADeviceAnalytics_EventSequence
+ __OBJC_$_INSTANCE_VARIABLES_WAEvent
+ __OBJC_$_INSTANCE_VARIABLES_WAEventLQMHistory
+ __OBJC_$_INSTANCE_VARIABLES_WAEventLeave
+ __OBJC_$_PROP_LIST_TimeseriesPoliciesHandler
+ __OBJC_$_PROP_LIST_WADeviceAnalytics_Entity_Property
+ __OBJC_$_PROP_LIST_WADeviceAnalytics_Event
+ __OBJC_$_PROP_LIST_WADeviceAnalytics_EventSequence
+ __OBJC_$_PROP_LIST_WAEvent
+ __OBJC_$_PROP_LIST_WAEventLQMHistory
+ __OBJC_$_PROP_LIST_WAEventLeave
+ __OBJC_CLASS_RO_$_LeaveMO
+ __OBJC_CLASS_RO_$_TimeseriesPoliciesHandler
+ __OBJC_CLASS_RO_$_WADeviceAnalytics_Entity_Property
+ __OBJC_CLASS_RO_$_WADeviceAnalytics_Event
+ __OBJC_CLASS_RO_$_WADeviceAnalytics_EventSequence
+ __OBJC_CLASS_RO_$_WAEvent
+ __OBJC_CLASS_RO_$_WAEventLQMHistory
+ __OBJC_CLASS_RO_$_WAEventLeave
+ __OBJC_CLASS_RO_$_WAMigrationUtils
+ __OBJC_METACLASS_RO_$_LeaveMO
+ __OBJC_METACLASS_RO_$_TimeseriesPoliciesHandler
+ __OBJC_METACLASS_RO_$_WADeviceAnalytics_Entity_Property
+ __OBJC_METACLASS_RO_$_WADeviceAnalytics_Event
+ __OBJC_METACLASS_RO_$_WADeviceAnalytics_EventSequence
+ __OBJC_METACLASS_RO_$_WAEvent
+ __OBJC_METACLASS_RO_$_WAEventLQMHistory
+ __OBJC_METACLASS_RO_$_WAEventLeave
+ __OBJC_METACLASS_RO_$_WAMigrationUtils
+ __OBJC_PROTOCOL_REFERENCE_$_NSSecureCoding
+ ___101-[WAClient updateRoamPoliciesAndSummarizeAnalyticsForNetwork:maxAgeInDays:andReply:queuedInvocation:]_block_invoke.233
+ ___101-[WAClient updateRoamPoliciesAndSummarizeAnalyticsForNetwork:maxAgeInDays:andReply:queuedInvocation:]_block_invoke.236
+ ___29+[UsageHelper binnedDate:as:]_block_invoke
+ ___29+[UsageHelper binnedDate:as:]_block_invoke.117
+ ___29+[UsageHelper binnedDate:as:]_block_invoke.118
+ ___29+[UsageHelper binnedDate:as:]_block_invoke.119
+ ___33+[UsageHelper dateFormatterQueue]_block_invoke
+ ___38-[WAClient _establishDaemonConnection]_block_invoke.181
+ ___38-[WAClient _establishDaemonConnection]_block_invoke.183
+ ___38-[WAClient _establishDaemonConnection]_block_invoke.186
+ ___38-[WAClient _establishDaemonConnection]_block_invoke_2.182
+ ___38-[WAClient _establishDaemonConnection]_block_invoke_2.184
+ ___40+[WAUtil enableCoreDataConcurrencyDebug]_block_invoke
+ ___41-[WADeviceAnalyticsClient initWithStore:]_block_invoke
+ ___44+[WAMigrationUtils modelWithHash:withError:]_block_invoke
+ ___44-[WADeviceAnalyticsClient loadStoreIfNeeded]_block_invoke.62
+ ___44-[WADeviceAnalyticsClient loadStoreIfNeeded]_block_invoke.91
+ ___47+[LinkChangePolicyHandler processJoinEvent:on:]_block_invoke
+ ___47-[WAPersistentContainer batchDelete:withError:]_block_invoke.340
+ ___48-[AnalyticsReader isBandRelevantForSSID:onBand:]_block_invoke
+ ___49-[WAClient _killDaemonAndReply:queuedInvocation:]_block_invoke.157
+ ___50+[WADeviceAnalytics_Event eventsIn:withPredicate:]_block_invoke
+ ___50-[WAClient _getDpsStatsandReply:queuedInvocation:]_block_invoke.151
+ ___50-[WAClient _getDpsStatsandReply:queuedInvocation:]_block_invoke.155
+ ___52-[WAClient _getUsageStatsandReply:queuedInvocation:]_block_invoke.252
+ ___52-[WAClient _getUsageStatsandReply:queuedInvocation:]_block_invoke.256
+ ___53-[AnalyticsProcessor processCachedFaultsAndResetMoc:]_block_invoke
+ ___54+[WAMigrationUtils migrationManagerTo:from:withError:]_block_invoke
+ ___54+[WAMigrationUtils migrationManagerTo:from:withError:]_block_invoke.167
+ ___54-[UsagePoliciesHandler updateAutoLeaveRssiWithReason:]_block_invoke
+ ___56-[AnalyticsProcessor processDeferredPoliciesWithReason:]_block_invoke_5
+ ___56-[AnalyticsProcessor processDeferredPoliciesWithReason:]_block_invoke_6
+ ___56-[WAClient _clearMessageStoreAndReply:queuedInvocation:]_block_invoke.159
+ ___56-[WADeviceAnalyticsClient isBandRelevantForSSID:onBand:]_block_invoke
+ ___57+[WAMigrationUtils remodelJoinReasonOnContext:withError:]_block_invoke
+ ___62-[WAClient _processManagedFault:at:andReply:queuedInvocation:]_block_invoke.247
+ ___62-[WAClient _processManagedFault:at:andReply:queuedInvocation:]_block_invoke.251
+ ___64-[WAClient _sendMemoryPressureRequestAndReply:queuedInvocation:]_block_invoke.165
+ ___65-[WAClient _triggerQueryForNWActivity:andReply:queuedInvocation:]_block_invoke.136
+ ___65-[WAClient _triggerQueryForNWActivity:andReply:queuedInvocation:]_block_invoke.140
+ ___68-[WAClient _getMessagesModelForGroupType:andReply:queuedInvocation:]_block_invoke.160
+ ___68-[WAClient _getMessagesModelForGroupType:andReply:queuedInvocation:]_block_invoke.163
+ ___68-[WAClient _signalPotentialNewIORChannelsAndReply:queuedInvocation:]_block_invoke.218
+ ___68-[WAClient _signalPotentialNewIORChannelsAndReply:queuedInvocation:]_block_invoke.222
+ ___69-[WADeviceAnalyticsClient processDeferredPriorityPoliciesWithReason:]_block_invoke.117
+ ___70+[AnalyticsStoreProxy batchDelete:withPredicate:withFetchRequest:moc:]_block_invoke.71
+ ___70+[WADeviceAnalyticsClient sharedDeviceAnalyticsClientWithCustomStore:]_block_invoke
+ ___70-[AnalyticsReader eventSequencesFor:since:until:sortingAsc:withError:]_block_invoke
+ ___70-[WAClient _getDeviceAnalyticsConfigurationAndReply:queuedInvocation:]_block_invoke.228
+ ___70-[WAClient _getDeviceAnalyticsConfigurationAndReply:queuedInvocation:]_block_invoke.232
+ ___70-[WAClient _issueIOReportManagementCommand:andReply:queuedInvocation:]_block_invoke.242
+ ___70-[WAClient _issueIOReportManagementCommand:andReply:queuedInvocation:]_block_invoke.246
+ ___71-[AnalyticsProcessor event:andResetMoc:andRunPostProcessing:withError:]_block_invoke
+ ___71-[WAClient _setDeviceAnalyticsConfiguration:andReply:queuedInvocation:]_block_invoke.214
+ ___71-[WAClient _setDeviceAnalyticsConfiguration:andReply:queuedInvocation:]_block_invoke.217
+ ___73-[WADeviceAnalyticsClient performPruneTestBSSes:networks:lans:withError:]_block_invoke.125
+ ___74-[WAClient _triggerQueryForNWActivityWithPeers:andReply:queuedInvocation:]_block_invoke.131
+ ___74-[WAClient _triggerQueryForNWActivityWithPeers:andReply:queuedInvocation:]_block_invoke.135
+ ___74-[WAClient submitEvent:andDeferReclaimMem:andRunPostProcessing:withError:]_block_invoke
+ ___75-[WAClient _triggerDeviceAnalyticsStoreMigrationAndReply:queuedInvocation:]_block_invoke.237
+ ___75-[WAClient _triggerDeviceAnalyticsStoreMigrationAndReply:queuedInvocation:]_block_invoke.241
+ ___78-[AnalyticsStoreFileWriter exportEntityToCSV:batchSize:maxAge:toURL:fileDate:]_block_invoke
+ ___78-[WADeviceAnalyticsClient eventSequencesFor:since:until:sortingAsc:withError:]_block_invoke
+ ___79+[WAMigrationUtils copyRoamTargetColumnsAddMissingRoamRelationships:withError:]_block_invoke
+ ___80-[WAClient _lqmCrashTracerNotifyForInterfaceWithName:andReply:queuedInvocation:]_block_invoke.206
+ ___80-[WAClient _lqmCrashTracerNotifyForInterfaceWithName:andReply:queuedInvocation:]_block_invoke.209
+ ___83-[WADeviceAnalyticsClient event:andDeferReclaimMem:andRunPostProcessing:withError:]_block_invoke
+ ___87-[WAClient _lqmCrashTracerReceiveBlock:forInterfaceWithName:andReply:queuedInvocation:]_block_invoke.210
+ ___87-[WAClient _lqmCrashTracerReceiveBlock:forInterfaceWithName:andReply:queuedInvocation:]_block_invoke.213
+ ___88-[WAClient _trapCrashMiniTracerDumpReadyForInterfaceWithName:andReply:queuedInvocation:]_block_invoke.202
+ ___88-[WAClient _trapCrashMiniTracerDumpReadyForInterfaceWithName:andReply:queuedInvocation:]_block_invoke.205
+ ___91-[WAClient _updateRoamPoliciesForSourceBssid:andUpdateRoamCache:andReply:queuedInvocation:]_block_invoke.223
+ ___91-[WAClient _updateRoamPoliciesForSourceBssid:andUpdateRoamCache:andReply:queuedInvocation:]_block_invoke.227
+ ___93-[WAClient _triggerDatapathDiagnosticsAndCollectUpdates:waMessage:andReply:queuedInvocation:]_block_invoke.146
+ ___93-[WAClient _triggerDatapathDiagnosticsAndCollectUpdates:waMessage:andReply:queuedInvocation:]_block_invoke.150
+ ___95-[WAClient convertWiFiStatsIntoPercentile:analysisGroup:groupTarget:andReply:queuedInvocation:]_block_invoke.141
+ ___95-[WAClient convertWiFiStatsIntoPercentile:analysisGroup:groupTarget:andReply:queuedInvocation:]_block_invoke.145
+ ___98-[WADeviceAnalyticsClient asyncAddEvent:andDeferReclaimMem:andRunPostProcessing:uponCompletionDo:]_block_invoke
+ ___block_descriptor_32_e25_q24?0"NSURL"8"NSURL"16l
+ ___block_descriptor_32_e39_q24?0"NSDictionary"8"NSDictionary"16l
+ ___block_descriptor_40_e65_B32?0"NSStagedMigrationManager"8"NSCustomMigrationStage"16^24l
+ ___block_descriptor_40_e8_32s_e28_v24?0"NSFetchRequest"8^16ls32l8
+ ___block_descriptor_48_e8_32r40r_e20_v20?0B8"NSError"12lr32l8r40l8
+ ___block_descriptor_48_e8_32s40s_e50_v32?0"NSString"8"WADeviceAnalytics_Event"16^B24ls32l8s40l8
+ ___block_descriptor_48_e8_32s_e28_v24?0"NSFetchRequest"8^16ls32l8
+ ___block_descriptor_56_e8_32s40s_e5_v8?0ls32l8s40l8
+ ___block_descriptor_58_e8_32s40r48r_e5_v8?0lr40l8s32l8r48l8
+ ___block_descriptor_58_e8_32s40s48bs_e5_v8?0ls32l8s40l8s48l8
+ ___block_descriptor_58_e8_32s40s48r_e5_v8?0lr48l8s32l8s40l8
+ ___block_descriptor_58_e8_32s40s48r_e5_v8?0ls32l8s40l8r48l8
+ ___block_descriptor_64_e8_32s40r48r_e5_v8?0ls32l8r40l8r48l8
+ ___block_descriptor_64_e8_32s40s48r_e5_v8?0ls32l8s40l8r48l8
+ ___block_descriptor_66_e8_32s40s48r56r_e5_v8?0ls32l8r48l8s40l8r56l8
+ ___block_descriptor_72_e8_32s40s48s56r64r_e5_v8?0ls32l8s40l8r56l8s48l8r64l8
+ ___block_descriptor_81_e8_32s40s48s56s64r72r_e5_v8?0lr64l8s32l8s40l8s48l8s56l8r72l8
+ ___block_descriptor_96_e8_32s40s48s56s64s72r_e5_v8?0ls32l8s40l8s48l8s56l8r72l8s64l8
+ ___block_literal_global.116
+ ___block_literal_global.133
+ ___block_literal_global.138
+ ___block_literal_global.143
+ ___block_literal_global.148
+ ___block_literal_global.153
+ ___block_literal_global.162
+ ___block_literal_global.204
+ ___block_literal_global.208
+ ___block_literal_global.212
+ ___block_literal_global.216
+ ___block_literal_global.220
+ ___block_literal_global.225
+ ___block_literal_global.230
+ ___block_literal_global.235
+ ___block_literal_global.239
+ ___block_literal_global.244
+ ___block_literal_global.249
+ ___block_literal_global.254
+ _convertLinkChangeReasonToString
+ _objc_msgSend$_allAttributes
+ _objc_msgSend$_calculateTDEdgeParamsVersion
+ _objc_msgSend$_dhcpEventOnBssid:ssid:serverInfo:at:with:andDeferReclaimMem:
+ _objc_msgSend$_diagnosticEventAt:with:andDeferReclaimMem:
+ _objc_msgSend$_event:andDeferReclaimMem:andRunPostProcessing:withError:
+ _objc_msgSend$_eventSequencesFor:withSequenceStartEvents:withSequenceEndEvents:withSequenceEvents:since:until:sortingAsc:forExport:withError:
+ _objc_msgSend$_geoTagEventOnBssid:ssid:lat:lon:at:andDeferReclaimMem:andRunPostProcessing:
+ _objc_msgSend$_getCurrentAutoLeaveRssiPolicyType
+ _objc_msgSend$_joinEventOnBssid:ssid:at:with:andDeferReclaimMem:andRunPostProcessing:
+ _objc_msgSend$_linkTestEventOn:at:with:andDeferReclaimMem:
+ _objc_msgSend$_lqmEvent:on:at:andDeferReclaimMem:
+ _objc_msgSend$_prunableEntitiesWithDate
+ _objc_msgSend$_recoveryEventOnBssid:at:with:andDeferReclaimMem:
+ _objc_msgSend$_removeKnownNetworkEvent:at:andDeferReclaimMem:
+ _objc_msgSend$_scanResultEventWith:ssid:whileOn:at:with:andDeferReclaimMem:
+ _objc_msgSend$_updateBSS:withParsedBeacon:andDeferReclaimMem:
+ _objc_msgSend$_updateIsBandResidencyLow:forBand:onNetwork:counters:
+ _objc_msgSend$_updateNetwork:switchedFrom:at:andDeferReclaimMem:
+ _objc_msgSend$addMissingRecoveryRelationships:withError:
+ _objc_msgSend$analyticsProcessorObj
+ _objc_msgSend$associationDuration
+ _objc_msgSend$asyncAddEvent:andDeferReclaimMem:andRunPostProcessing:uponCompletionDo:
+ _objc_msgSend$autoLeaveRssiTelemetry
+ _objc_msgSend$availableEventsWithError:
+ _objc_msgSend$canRunContextAwareTDPolicyNow
+ _objc_msgSend$canRunPolicyAtCurrentTimeForPolicyType:timespan:
+ _objc_msgSend$checkRejoinAfterLeaveEvent:In:
+ _objc_msgSend$compare:options:
+ _objc_msgSend$configureContextAwareTDEventsToFetchWithError:
+ _objc_msgSend$conformsToProtocol:
+ _objc_msgSend$contentsOfDirectoryAtURL:includingPropertiesForKeys:options:error:
+ _objc_msgSend$copyRoamTargetColumnsAddMissingRoamRelationships:withError:
+ _objc_msgSend$dateFormatterQueue
+ _objc_msgSend$datedProperty
+ _objc_msgSend$defaultCStringEncoding
+ _objc_msgSend$defaultKeysAllowedOnCustomerInstalls
+ _objc_msgSend$dictionaryForCA
+ _objc_msgSend$dictionaryRepresentationFor:
+ _objc_msgSend$dictionaryWithValuesForKeys:
+ _objc_msgSend$enableCoreDataConcurrencyDebug
+ _objc_msgSend$endEvent
+ _objc_msgSend$entityFilter
+ _objc_msgSend$entityVersionHashesByName
+ _objc_msgSend$evaluateWithObject:
+ _objc_msgSend$event:andDeferReclaimMem:andRunPostProcessing:withError:
+ _objc_msgSend$event:andResetMoc:andRunPostProcessing:withError:
+ _objc_msgSend$eventDescription:from:withError:
+ _objc_msgSend$eventNameForCA
+ _objc_msgSend$eventSequencesFor:since:until:sortingAsc:forExport:withError:
+ _objc_msgSend$eventSequencesFor:since:until:sortingAsc:withError:
+ _objc_msgSend$eventType
+ _objc_msgSend$events
+ _objc_msgSend$eventsIn:withPredicate:
+ _objc_msgSend$fetchDatedEvents:since:until:ascending:withError:
+ _objc_msgSend$filterArrayForDottedKeyPaths:
+ _objc_msgSend$filterArrayForKeys:
+ _objc_msgSend$findEdgeBSSFromRoamEventBeforeLeaveEvent:In:
+ _objc_msgSend$findEdgeBSSIn:byCheckingLeaveEventsUntil:
+ _objc_msgSend$findEventsIn:aroundIndex:noEarlierThan:noLaterThan:withPredicate:findingAll:
+ _objc_msgSend$findNextLeaveEventFrom:In:
+ _objc_msgSend$findRoamEventBeforeLeaveEvent:In:
+ _objc_msgSend$initWithCalendarIdentifier:
+ _objc_msgSend$initWithCurrentModelReference:nextModelReference:
+ _objc_msgSend$initWithEntity:
+ _objc_msgSend$initWithMigrationStages:
+ _objc_msgSend$initWithModel:versionChecksum:
+ _objc_msgSend$initWithStartRecord:endRecord:sequenceRecords:asc:forEvents:forExport:
+ _objc_msgSend$initWithStore:
+ _objc_msgSend$initWithUsedPropertiesFromUsedEvent:
+ _objc_msgSend$initWithVersionChecksums:
+ _objc_msgSend$is2GHzResidencyLow
+ _objc_msgSend$is5GHzResidencyLow
+ _objc_msgSend$is6GHzResidencyLow
+ _objc_msgSend$isBandRelevantForSSID:onBand:
+ _objc_msgSend$isContextAwareTDPolicyExecutionIntervalSufficient
+ _objc_msgSend$isContextAwareTDPolicyLastWeekWiFiUsageSufficient
+ _objc_msgSend$isEdgeForLeaveTelemetry
+ _objc_msgSend$isInVoluntary
+ _objc_msgSend$isSubclassOfClass:
+ _objc_msgSend$isWork
+ _objc_msgSend$joinFailureAsString:
+ _objc_msgSend$joinReasonAsString:
+ _objc_msgSend$keyPathsToFetch
+ _objc_msgSend$leaveReasonAsString:
+ _objc_msgSend$longValue
+ _objc_msgSend$mapOldJoinReason:andWAManualAssociationTypeMaskToJoinReason:
+ _objc_msgSend$metadataForPersistentStoreOfType:URL:options:error:
+ _objc_msgSend$migrationManagerTo:from:withError:
+ _objc_msgSend$modelWithHash:withError:
+ _objc_msgSend$motionStateAsString:
+ _objc_msgSend$noiseHistory
+ _objc_msgSend$notPredicateWithSubpredicate:
+ _objc_msgSend$numberWithLong:
+ _objc_msgSend$orPredicateWithSubpredicates:
+ _objc_msgSend$performSelector:withObject:
+ _objc_msgSend$predicateForIsSubEntity
+ _objc_msgSend$processCachedFaultsAndResetMoc:
+ _objc_msgSend$processEventOnPersistentContainer:andRunPostprocessing:withError:
+ _objc_msgSend$processJoinEvent:on:
+ _objc_msgSend$properties
+ _objc_msgSend$propertiesToFetch
+ _objc_msgSend$propertyPath
+ _objc_msgSend$propertyWith:
+ _objc_msgSend$reasonForRunning
+ _objc_msgSend$referenceForModel:withError:
+ _objc_msgSend$remodelJoinReasonOnContext:withError:
+ _objc_msgSend$resetAllInstancesUsageToZero:forTimeSpan:
+ _objc_msgSend$reverseObjectEnumerator
+ _objc_msgSend$sequenceEdgeEventsIn:
+ _objc_msgSend$sequenceEndEventsIn:
+ _objc_msgSend$sequenceEventsIn:
+ _objc_msgSend$sequenceStartEventsIn:
+ _objc_msgSend$setAsc:
+ _objc_msgSend$setAssocDuration:
+ _objc_msgSend$setAssociationDuration:
+ _objc_msgSend$setAutoLeaveRssiTelemetry:
+ _objc_msgSend$setBeaconPerHistory:
+ _objc_msgSend$setBeaconSchedHistory:
+ _objc_msgSend$setBw:
+ _objc_msgSend$setCachedParamsWithBssid:ssid:
+ _objc_msgSend$setCcaHistory:
+ _objc_msgSend$setChannelWidth:
+ _objc_msgSend$setDidMigrateHandler:
+ _objc_msgSend$setEndEvent:
+ _objc_msgSend$setEndEventMO:
+ _objc_msgSend$setEntityFilter:
+ _objc_msgSend$setEventMOs:
+ _objc_msgSend$setEventType:
+ _objc_msgSend$setEvents:
+ _objc_msgSend$setFwTxFramesHistory:
+ _objc_msgSend$setFwTxPerHistory:
+ _objc_msgSend$setIs2GHzResidencyLow:
+ _objc_msgSend$setIs5GHzResidencyLow:
+ _objc_msgSend$setIs6GHzResidencyLow:
+ _objc_msgSend$setIsEdgeForLeaveTelemetry:
+ _objc_msgSend$setIsInVoluntary:
+ _objc_msgSend$setKeyPathsToFetch:
+ _objc_msgSend$setLabel:
+ _objc_msgSend$setNoiseHistory:
+ _objc_msgSend$setProperties:
+ _objc_msgSend$setPropertiesToFetch:withError:
+ _objc_msgSend$setPropertyPath:
+ _objc_msgSend$setRelationshipKeyPathsToFetch:
+ _objc_msgSend$setRssiHistory:
+ _objc_msgSend$setSnrHistory:
+ _objc_msgSend$setStartEvent:
+ _objc_msgSend$setStartEventMO:
+ _objc_msgSend$setSubReason:
+ _objc_msgSend$setSubreason:
+ _objc_msgSend$setTdEdgeParamsVersion:
+ _objc_msgSend$setTxFrameHistory:
+ _objc_msgSend$setTxPerHistory:
+ _objc_msgSend$shallowCopyOfUsedEventsIn:
+ _objc_msgSend$sharedDeviceAnalyticsClientWithCustomStore:
+ _objc_msgSend$sortUsingSelector:
+ _objc_msgSend$sortedArrayUsingComparator:
+ _objc_msgSend$stagedMigrationManagerIfNeededForMOM:andStore:withError:
+ _objc_msgSend$startEvent
+ _objc_msgSend$subarrayWithRange:
+ _objc_msgSend$submitBSSEventsFor:
+ _objc_msgSend$submitEvent:andDeferReclaimMem:andRunPostProcessing:withError:
+ _objc_msgSend$submitEvent:async:andDeferReclaimMem:andRunPostProcessing:uponCompletionDo:
+ _objc_msgSend$submitNetworkEventsFor:
+ _objc_msgSend$subreason
+ _objc_msgSend$superclass
+ _objc_msgSend$supportsSecureCoding
+ _objc_msgSend$tdEdgeParamsVersion
+ _objc_msgSend$tdEdgeParamsVersionAsString:
+ _objc_msgSend$timeSeriesPoliciesHandler
+ _objc_msgSend$timeSinceLastPruning
+ _objc_msgSend$timeSpanSelectorToString:
+ _objc_msgSend$totalWiFiUsageInTimeSpan:around:
+ _objc_msgSend$tryToMigrate:using:withError:
+ _objc_msgSend$unusedSuperEntityProperties
+ _objc_msgSend$updateAutoLeaveRssiWithReason:
+ _objc_msgSend$updateBSSMOWithEdgeBSSSet:tdEdgeParamsVersion:withError:
+ _objc_msgSend$updateBandResidencyWithReason:
+ _objc_msgSend$updateCachedParamsIfNeeded:
+ _objc_msgSend$updateContextAwareTDPolicies:
+ _objc_msgSend$updateEdgeBssWithReason:at:timeSpan:
+ _objc_msgSend$updatePoliciesTableWithPolicyType:reason:dateLessThen:object:timeSpan:
+ _objc_msgSend$updatePoliciesTableWithReason:withPolicyType:withOutcome:
+ _objc_msgSend$upperEdge
+ _objc_msgSend$useAsDescription:
+ _objc_msgSend$useAsEvent:inEvents:withError:
+ _objc_msgSend$useEventAsSequenceEnd
+ _objc_msgSend$useEventAsSequenceEvent
+ _objc_msgSend$useEventAsSequenceStart
+ _objc_msgSend$usedPropertiesDescription
+ _objc_msgSend$validateEntityForGroupbyRequest:
+ _objc_msgSend$versionChecksum
+ _objc_retain_x28
+ _property_getAttributes
- +[EventLeaveNetwork processRecord:bssid:ssid:withPersistentContainer:andRunPostprocessing:]
- +[LinkChangePolicyHandler processJoinEvent:]
- +[WADeviceAnalyticsLeaveRecord(CoreDataProperties) fetchRequest]
- -[AnalyticsProcessor leaveEventOnBssid:ssid:at:with:andResetMoc:andRunPostProcessing:]
- -[AnalyticsProcessor processCachedFaultsAndResetCache:andResetMoc:]
- -[AnalyticsProcessor roamEvent:at:andResetMoc:andRunPostProcessing:withError:]
- -[UsagePoliciesHandler updatePoliciesTableWithReason:dateLessThen:object:timeSpan:]
- -[WAClient submitEvent:at:andDeferReclaimMem:andRunPostProcessing:withError:]
- -[WADeviceAnalyticsClient immediateProcessCachedFaultsAndDeferReclaimMem:]
- -[WADeviceAnalyticsClient init]
- -[WADeviceAnalyticsClient leaveEventOnBssid:ssid:at:with:]
- -[WADeviceAnalyticsClient leaveEventOnBssid:ssid:at:with:andDeferReclaimMem:]
- -[WADeviceAnalyticsClient roamEvent:at:]
- -[WADeviceAnalyticsClient roamEvent:at:andDeferReclaimMem:andRunPostProcessing:]
- -[WADeviceAnalyticsClient roamEvent:at:andDeferReclaimMem:andRunPostProcessing:withError:]
- -[WAEventRoamStatus beaconPerHistory]
- -[WAEventRoamStatus beaconSchedHistory]
- -[WAEventRoamStatus ccaHistory]
- -[WAEventRoamStatus fwTxFramesHistory]
- -[WAEventRoamStatus fwTxPerHistory]
- -[WAEventRoamStatus initWithDriverEvent:andDeviceCapabilities:]
- -[WAEventRoamStatus initWithDriverEvent:andDeviceCapabilities:withError:]
- -[WAEventRoamStatus motionState]
- -[WAEventRoamStatus noiseHistory]
- -[WAEventRoamStatus processEventAt:withPersistentContainer:andRunPostprocessing:withError:]
- -[WAEventRoamStatus reason]
- -[WAEventRoamStatus rssiHistory]
- -[WAEventRoamStatus setBeaconPerHistory:]
- -[WAEventRoamStatus setBeaconSchedHistory:]
- -[WAEventRoamStatus setCcaHistory:]
- -[WAEventRoamStatus setFwTxFramesHistory:]
- -[WAEventRoamStatus setFwTxPerHistory:]
- -[WAEventRoamStatus setNoiseHistory:]
- -[WAEventRoamStatus setReason:]
- -[WAEventRoamStatus setRssiHistory:]
- -[WAEventRoamStatus setSnrHistory:]
- -[WAEventRoamStatus setStatus:]
- -[WAEventRoamStatus setTxFrameHistory:]
- -[WAEventRoamStatus setTxPerHistory:]
- -[WAEventRoamStatus snrHistory]
- -[WAEventRoamStatus status]
- -[WAEventRoamStatus submitEventToCA]
- -[WAEventRoamStatus txFrameHistory]
- -[WAEventRoamStatus txPerHistory]
- GCC_except_table105
- GCC_except_table112
- GCC_except_table114
- GCC_except_table116
- GCC_except_table118
- GCC_except_table122
- GCC_except_table124
- GCC_except_table131
- GCC_except_table132
- GCC_except_table136
- GCC_except_table138
- GCC_except_table140
- GCC_except_table151
- GCC_except_table154
- GCC_except_table160
- GCC_except_table163
- GCC_except_table166
- GCC_except_table169
- GCC_except_table172
- GCC_except_table175
- GCC_except_table178
- GCC_except_table181
- GCC_except_table187
- GCC_except_table193
- GCC_except_table199
- GCC_except_table254
- GCC_except_table46
- GCC_except_table54
- GCC_except_table58
- GCC_except_table60
- GCC_except_table64
- GCC_except_table66
- GCC_except_table72
- GCC_except_table75
- GCC_except_table78
- GCC_except_table81
- GCC_except_table84
- GCC_except_table86
- GCC_except_table87
- GCC_except_table99
- _OBJC_CLASS_$_EventLeaveNetwork
- _OBJC_CLASS_$_NSMutableOrderedSet
- _OBJC_CLASS_$_WADeviceAnalyticsLeaveRecord
- _OBJC_IVAR_$_WAEventRoamStatus._associatedDur
- _OBJC_IVAR_$_WAEventRoamStatus._bandsInNetwork
- _OBJC_IVAR_$_WAEventRoamStatus._beaconPerHistory
- _OBJC_IVAR_$_WAEventRoamStatus._beaconSchedHistory
- _OBJC_IVAR_$_WAEventRoamStatus._ccaHistory
- _OBJC_IVAR_$_WAEventRoamStatus._ccaInt
- _OBJC_IVAR_$_WAEventRoamStatus._ccaOthers
- _OBJC_IVAR_$_WAEventRoamStatus._ccaTotal
- _OBJC_IVAR_$_WAEventRoamStatus._deviceIs6eCapable
- _OBJC_IVAR_$_WAEventRoamStatus._driverRoamProfile
- _OBJC_IVAR_$_WAEventRoamStatus._flags
- _OBJC_IVAR_$_WAEventRoamStatus._fwTxFramesHistory
- _OBJC_IVAR_$_WAEventRoamStatus._fwTxPerHistory
- _OBJC_IVAR_$_WAEventRoamStatus._hasAssociatedDur
- _OBJC_IVAR_$_WAEventRoamStatus._hasCcaInt
- _OBJC_IVAR_$_WAEventRoamStatus._hasCcaOthers
- _OBJC_IVAR_$_WAEventRoamStatus._hasCcaTotal
- _OBJC_IVAR_$_WAEventRoamStatus._hasHostReason
- _OBJC_IVAR_$_WAEventRoamStatus._hasLateRoam
- _OBJC_IVAR_$_WAEventRoamStatus._hasMotionState
- _OBJC_IVAR_$_WAEventRoamStatus._hasOriginBcnPer
- _OBJC_IVAR_$_WAEventRoamStatus._hasOriginChannelScore
- _OBJC_IVAR_$_WAEventRoamStatus._hasOriginFwTxPer
- _OBJC_IVAR_$_WAEventRoamStatus._hasOriginTxPer
- _OBJC_IVAR_$_WAEventRoamStatus._hasVoipActive
- _OBJC_IVAR_$_WAEventRoamStatus._hostReason
- _OBJC_IVAR_$_WAEventRoamStatus._lateRoam
- _OBJC_IVAR_$_WAEventRoamStatus._motionState
- _OBJC_IVAR_$_WAEventRoamStatus._noiseHistory
- _OBJC_IVAR_$_WAEventRoamStatus._originBcnPer
- _OBJC_IVAR_$_WAEventRoamStatus._originChannelScore
- _OBJC_IVAR_$_WAEventRoamStatus._originFwTxPer
- _OBJC_IVAR_$_WAEventRoamStatus._originTxPer
- _OBJC_IVAR_$_WAEventRoamStatus._reason
- _OBJC_IVAR_$_WAEventRoamStatus._roamCache
- _OBJC_IVAR_$_WAEventRoamStatus._roamScanDuration
- _OBJC_IVAR_$_WAEventRoamStatus._rssiHistory
- _OBJC_IVAR_$_WAEventRoamStatus._scannedChannelCount
- _OBJC_IVAR_$_WAEventRoamStatus._snrHistory
- _OBJC_IVAR_$_WAEventRoamStatus._sourceAKMs
- _OBJC_IVAR_$_WAEventRoamStatus._sourceAuth
- _OBJC_IVAR_$_WAEventRoamStatus._sourceBssid
- _OBJC_IVAR_$_WAEventRoamStatus._sourcePhyMode
- _OBJC_IVAR_$_WAEventRoamStatus._status
- _OBJC_IVAR_$_WAEventRoamStatus._targetAKMs
- _OBJC_IVAR_$_WAEventRoamStatus._targetApProfile
- _OBJC_IVAR_$_WAEventRoamStatus._targetAuth
- _OBJC_IVAR_$_WAEventRoamStatus._targetBssid
- _OBJC_IVAR_$_WAEventRoamStatus._targetPhyMode
- _OBJC_IVAR_$_WAEventRoamStatus._txFrameHistory
- _OBJC_IVAR_$_WAEventRoamStatus._txPerHistory
- _OBJC_IVAR_$_WAEventRoamStatus._voipActive
- _OBJC_METACLASS_$_EventLeaveNetwork
- _OBJC_METACLASS_$_WADeviceAnalyticsLeaveRecord
- __OBJC_$_CLASS_METHODS_EventLeaveNetwork
- __OBJC_$_CLASS_METHODS_WADeviceAnalyticsLeaveRecord(CoreDataProperties)
- __OBJC_CLASS_RO_$_EventLeaveNetwork
- __OBJC_CLASS_RO_$_WADeviceAnalyticsLeaveRecord
- __OBJC_METACLASS_RO_$_EventLeaveNetwork
- __OBJC_METACLASS_RO_$_WADeviceAnalyticsLeaveRecord
- ___101-[WAClient updateRoamPoliciesAndSummarizeAnalyticsForNetwork:maxAgeInDays:andReply:queuedInvocation:]_block_invoke.232
- ___101-[WAClient updateRoamPoliciesAndSummarizeAnalyticsForNetwork:maxAgeInDays:andReply:queuedInvocation:]_block_invoke.235
- ___31-[WADeviceAnalyticsClient init]_block_invoke
- ___38-[WAClient _establishDaemonConnection]_block_invoke.180
- ___38-[WAClient _establishDaemonConnection]_block_invoke.182
- ___38-[WAClient _establishDaemonConnection]_block_invoke.184
- ___38-[WAClient _establishDaemonConnection]_block_invoke_2.181
- ___38-[WAClient _establishDaemonConnection]_block_invoke_2.183
- ___44+[LinkChangePolicyHandler processJoinEvent:]_block_invoke
- ___44-[WADeviceAnalyticsClient loadStoreIfNeeded]_block_invoke.57
- ___44-[WADeviceAnalyticsClient loadStoreIfNeeded]_block_invoke.86
- ___47-[WAPersistentContainer batchDelete:withError:]_block_invoke.306
- ___49-[WAClient _killDaemonAndReply:queuedInvocation:]_block_invoke.155
- ___50-[WAClient _getDpsStatsandReply:queuedInvocation:]_block_invoke.150
- ___50-[WAClient _getDpsStatsandReply:queuedInvocation:]_block_invoke.153
- ___52-[WAClient _getUsageStatsandReply:queuedInvocation:]_block_invoke.251
- ___52-[WAClient _getUsageStatsandReply:queuedInvocation:]_block_invoke.254
- ___54+[WADeviceAnalyticsClient sharedDeviceAnalyticsClient]_block_invoke
- ___56-[WAClient _clearMessageStoreAndReply:queuedInvocation:]_block_invoke.157
- ___62-[WAClient _processManagedFault:at:andReply:queuedInvocation:]_block_invoke.246
- ___62-[WAClient _processManagedFault:at:andReply:queuedInvocation:]_block_invoke.249
- ___64-[WAClient _sendMemoryPressureRequestAndReply:queuedInvocation:]_block_invoke.163
- ___65-[WAClient _triggerQueryForNWActivity:andReply:queuedInvocation:]_block_invoke.135
- ___65-[WAClient _triggerQueryForNWActivity:andReply:queuedInvocation:]_block_invoke.138
- ___67-[AnalyticsProcessor processCachedFaultsAndResetCache:andResetMoc:]_block_invoke
- ___68-[WAClient _getMessagesModelForGroupType:andReply:queuedInvocation:]_block_invoke.159
- ___68-[WAClient _getMessagesModelForGroupType:andReply:queuedInvocation:]_block_invoke.162
- ___68-[WAClient _signalPotentialNewIORChannelsAndReply:queuedInvocation:]_block_invoke.217
- ___68-[WAClient _signalPotentialNewIORChannelsAndReply:queuedInvocation:]_block_invoke.220
- ___69-[WADeviceAnalyticsClient processDeferredPriorityPoliciesWithReason:]_block_invoke.110
- ___70+[AnalyticsStoreProxy batchDelete:withPredicate:withFetchRequest:moc:]_block_invoke.64
- ___70-[WAClient _getDeviceAnalyticsConfigurationAndReply:queuedInvocation:]_block_invoke.227
- ___70-[WAClient _getDeviceAnalyticsConfigurationAndReply:queuedInvocation:]_block_invoke.230
- ___70-[WAClient _issueIOReportManagementCommand:andReply:queuedInvocation:]_block_invoke.241
- ___70-[WAClient _issueIOReportManagementCommand:andReply:queuedInvocation:]_block_invoke.244
- ___71-[WAClient _setDeviceAnalyticsConfiguration:andReply:queuedInvocation:]_block_invoke.213
- ___71-[WAClient _setDeviceAnalyticsConfiguration:andReply:queuedInvocation:]_block_invoke.216
- ___74-[WAClient _triggerQueryForNWActivityWithPeers:andReply:queuedInvocation:]_block_invoke.130
- ___74-[WAClient _triggerQueryForNWActivityWithPeers:andReply:queuedInvocation:]_block_invoke.133
- ___74-[WADeviceAnalyticsClient immediateProcessCachedFaultsAndDeferReclaimMem:]_block_invoke
- ___75-[WAClient _triggerDeviceAnalyticsStoreMigrationAndReply:queuedInvocation:]_block_invoke.236
- ___75-[WAClient _triggerDeviceAnalyticsStoreMigrationAndReply:queuedInvocation:]_block_invoke.239
- ___77-[WADeviceAnalyticsClient leaveEventOnBssid:ssid:at:with:andDeferReclaimMem:]_block_invoke
- ___78-[AnalyticsProcessor roamEvent:at:andResetMoc:andRunPostProcessing:withError:]_block_invoke
- ___80-[WAClient _lqmCrashTracerNotifyForInterfaceWithName:andReply:queuedInvocation:]_block_invoke.205
- ___80-[WAClient _lqmCrashTracerNotifyForInterfaceWithName:andReply:queuedInvocation:]_block_invoke.208
- ___86-[AnalyticsProcessor leaveEventOnBssid:ssid:at:with:andResetMoc:andRunPostProcessing:]_block_invoke
- ___87-[WAClient _lqmCrashTracerReceiveBlock:forInterfaceWithName:andReply:queuedInvocation:]_block_invoke.209
- ___87-[WAClient _lqmCrashTracerReceiveBlock:forInterfaceWithName:andReply:queuedInvocation:]_block_invoke.212
- ___88-[WAClient _trapCrashMiniTracerDumpReadyForInterfaceWithName:andReply:queuedInvocation:]_block_invoke.201
- ___88-[WAClient _trapCrashMiniTracerDumpReadyForInterfaceWithName:andReply:queuedInvocation:]_block_invoke.204
- ___90-[WADeviceAnalyticsClient roamEvent:at:andDeferReclaimMem:andRunPostProcessing:withError:]_block_invoke
- ___91-[WAClient _updateRoamPoliciesForSourceBssid:andUpdateRoamCache:andReply:queuedInvocation:]_block_invoke.222
- ___91-[WAClient _updateRoamPoliciesForSourceBssid:andUpdateRoamCache:andReply:queuedInvocation:]_block_invoke.225
- ___93-[WAClient _triggerDatapathDiagnosticsAndCollectUpdates:waMessage:andReply:queuedInvocation:]_block_invoke.145
- ___93-[WAClient _triggerDatapathDiagnosticsAndCollectUpdates:waMessage:andReply:queuedInvocation:]_block_invoke.148
- ___95-[WAClient convertWiFiStatsIntoPercentile:analysisGroup:groupTarget:andReply:queuedInvocation:]_block_invoke.140
- ___95-[WAClient convertWiFiStatsIntoPercentile:analysisGroup:groupTarget:andReply:queuedInvocation:]_block_invoke.143
- ___block_descriptor_49_e8_32s40r_e5_v8?0lr40l8s32l8
- ___block_descriptor_59_e8_32s40r48r_e5_v8?0lr40l8s32l8r48l8
- ___block_descriptor_74_e8_32s40s48s56r64r_e5_v8?0lr56l8s32l8s40l8r64l8s48l8
- ___block_descriptor_74_e8_32s40s48s56r64r_e5_v8?0lr56l8s32l8s40l8s48l8r64l8
- ___block_descriptor_81_e8_32s40s48s56s64bs72r_e5_v8?0ls32l8s40l8s48l8s56l8s64l8r72l8
- ___block_literal_global.132
- ___block_literal_global.137
- ___block_literal_global.142
- ___block_literal_global.147
- ___block_literal_global.152
- ___block_literal_global.161
- ___block_literal_global.203
- ___block_literal_global.207
- ___block_literal_global.211
- ___block_literal_global.215
- ___block_literal_global.219
- ___block_literal_global.224
- ___block_literal_global.229
- ___block_literal_global.234
- ___block_literal_global.238
- ___block_literal_global.243
- ___block_literal_global.248
- ___block_literal_global.251
- _kWAMessageKeyApProfile
- _kWAMessageKeyAssociationState
- _kWAMessageKeyIsDriverAvailabilityNonFatal
- _kWAMessageKeyReasonString
- _kWAMessageKeyRecoveryLatency
- _kWAMessageKeySubReason
- _kWAMessageKeySubReasonString
- _kWAMessageKeyTimeBetweenFailure
- _kWAMessageKeyTotalNumberOfJoinAttempts
- _kWAMessageKeyWPSMfgElement
- _kWAMessageKeyWPSPrimaryConfigMethods
- _kWAMessageKeyWPSPrimaryDeviceNameData
- _kWAMessageKeyWPSPrimaryDeviceNameElement
- _kWAMessageKeyWPSPrimaryDeviceTypeCategory
- _kWAMessageKeyWPSPrimaryDeviceTypeSubCategory
- _kWAMessageKeyWPSResponseType
- _kWAMessageMetricNameWatchdogEvent
- _objc_claimAutoreleasedReturnValue
- _objc_msgSend$fwReason
- _objc_msgSend$initWithDriverEvent:andDeviceCapabilities:withError:
- _objc_msgSend$leaveEventOnBssid:ssid:at:with:andDeferReclaimMem:
- _objc_msgSend$leaveEventOnBssid:ssid:at:with:andResetMoc:andRunPostProcessing:
- _objc_msgSend$orderedSetWithObject:
- _objc_msgSend$processCachedFaultsAndResetCache:andResetMoc:
- _objc_msgSend$processEventAt:withPersistentContainer:andRunPostprocessing:withError:
- _objc_msgSend$processJoinEvent:
- _objc_msgSend$roamEvent:at:andDeferReclaimMem:andRunPostProcessing:withError:
- _objc_msgSend$roamEvent:at:andResetMoc:andRunPostProcessing:withError:
- _objc_msgSend$setFwReason:
- _objc_msgSend$setTargetChannelWidth:
- _objc_msgSend$success
- _objc_msgSend$updatePoliciesTableWithReason:dateLessThen:object:timeSpan:
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x5
- _objc_retain_x9
- _sqrt
- _symbolic _____ s5UInt8V
CStrings:
+ "%@ %@ %@ from %@ to %@"
+ "%@ for %@ -- %@"
+ "%@ on %@: %@(%@) %@ isInvol:%@ motion:%@ rssi:%@ assocDur:%@"
+ "%@%@%@"
+ "%@.%@"
+ "%K == %@ AND %K == %@"
+ "%K == YES"
+ "%K >= %@"
+ "%s (%d)"
+ "%{public}s::%d:Added %@ at [%@] to [%@][%@][%@]"
+ "%{public}s::%d:Attribute %@ should have been described by the children class (%@): %@"
+ "%{public}s::%d:BSS EdgeParamsVersion does not match version in db: %hd (%@) version required: %hd (%@). Waiting for the weekly policy to run. Before that, you will see conservative TD behavior."
+ "%{public}s::%d:BSS entity misses bssid."
+ "%{public}s::%d:Calling updateBandResidencyWithReason: on current process"
+ "%{public}s::%d:Calling updateContextAwareTDPolicies: on current process"
+ "%{public}s::%d:Cannot run updateContextAwareTDPolicies now - skipping"
+ "%{public}s::%d:Class %@ does not implement jumpBackOneSpan"
+ "%{public}s::%d:ContextAwareTD update fails. Reset managed object context. "
+ "%{public}s::%d:ContextAwareTD update is not expected to run on processes else than %@"
+ "%{public}s::%d:CoreData %@ threw exception: %@"
+ "%{public}s::%d:CoreData exception %@ while fetching %@"
+ "%{public}s::%d:CoreData threw exception while materializing %@ on %@: %@"
+ "%{public}s::%d:CoreData threw exception: %@"
+ "%{public}s::%d:Edge BSS detection complete. Found %lu edge BSSes: %@"
+ "%{public}s::%d:Either set at least one event as sequence start (%@) and at least one as sequence end (%@) or neither."
+ "%{public}s::%d:Error %@ while fetching %@"
+ "%{public}s::%d:Error getting _timeSeriesPoliciesHandler"
+ "%{public}s::%d:Error getting _usagePoliciesHandler"
+ "%{public}s::%d:Event %@ does not exist in %@"
+ "%{public}s::%d:Fail to get cumulativeUsage"
+ "%{public}s::%d:Fail to get currentAutoLeaveRssiType."
+ "%{public}s::%d:Fail to get reference date"
+ "%{public}s::%d:Fail to get the dateEdges for edgebss calculation."
+ "%{public}s::%d:Fail to run policy %@, stop updateAutoLeaveRssi"
+ "%{public}s::%d:Fail to run policy, autoLeaveRssi is not updated do not save the results. Wait to tomorrow to try again."
+ "%{public}s::%d:Fail to save contextAwareTD updates to database (edgeBss, autoLeaveRssi, policy records)."
+ "%{public}s::%d:Failed to fetch all %@ instances for reset: %@"
+ "%{public}s::%d:Failed to reset %@ instances to zero usage, continuing with processing"
+ "%{public}s::%d:Faulting attribute: %@(%@) in %@ -- Add to propertiesToFetch"
+ "%{public}s::%d:Ignoring non secure codeable object in %@ (%@) for %@: %@"
+ "%{public}s::%d:Ignoring toMany relationship %@(%@) in %@"
+ "%{public}s::%d:Invalid band value for residency calculation. Band %hd not in valid range. Valid: 2G=%hd, 5G=%hd, 6G=%hd"
+ "%{public}s::%d:Invalid band value. Provided: %hd, Expected: WABand2G (%hd) || WABand5G (%hd) || WABand6G (%hd)"
+ "%{public}s::%d:Invalid tdEdgeParamsVersion: %d"
+ "%{public}s::%d:No lastPolicyRun, we will execute policy %@"
+ "%{public}s::%d:No sequences found. The DB is new. Cause can be new device, migration fail. "
+ "%{public}s::%d:No usage data for band %hd on SSID %@, setting to Low residency"
+ "%{public}s::%d:PoliciesMO dateWithinLatestComplete = %@, lastUsagePolicyRunDate binnedDate lowerEdge = %@"
+ "%{public}s::%d:PoliciesUsageMO dateWithinLatestComplete = %@, lastUsagePolicyRun.date_lt = %@"
+ "%{public}s::%d:PolicyType is required"
+ "%{public}s::%d:Processing %@"
+ "%{public}s::%d:Reset %lu %@ entities to zero usage for %@"
+ "%{public}s::%d:Resetting AnalyticsProcessor bssidForCachedFaults to %@"
+ "%{public}s::%d:Resetting latestBssid to %@ latestNetwork to %@"
+ "%{public}s::%d:Returning %@ records"
+ "%{public}s::%d:Returning %lu sequences %@"
+ "%{public}s::%d:Returning a single sequence with %lu events"
+ "%{public}s::%d:Run updateContextAwareTDPolicies successfully"
+ "%{public}s::%d:Stored Policy (%@) run at (%@) for reason: %@ with outcome: %@"
+ "%{public}s::%d:Stored Policy (%@) run at (%@) timeSinceLastPruning:%@"
+ "%{public}s::%d:TD Edge Params Version: Legacy (ContextAwareTriggerDisconnect disabled)"
+ "%{public}s::%d:TD Edge Params Version: UsageBased (ContextAwareTriggerDisconnect enabled)"
+ "%{public}s::%d:This should never be called, this method is to be implemented by subclasses"
+ "%{public}s::%d:Total WiFi Usage duration: %@ around time: %@ is %lu"
+ "%{public}s::%d:Unable to fetch all joins: %@"
+ "%{public}s::%d:Unable to fetch all recoveries: %@"
+ "%{public}s::%d:Unable to fetch all roams: %@"
+ "%{public}s::%d:Unable to fetch sequences: %@"
+ "%{public}s::%d:Unable to get Staged Migration Manager to version 18 or newer: %@"
+ "%{public}s::%d:Unable to get a PersistentContainer for model name: %@ %@ (%@)"
+ "%{public}s::%d:Unable to get context from migrationManager (%@) container (%@)"
+ "%{public}s::%d:Unable to get lightweight migration stage step to V18 or newer"
+ "%{public}s::%d:Unable to get metadata for store at %@: %@"
+ "%{public}s::%d:Unable to get model for %@"
+ "%{public}s::%d:Unable to get model for store at %@: %@"
+ "%{public}s::%d:Unable to list model versions on %@: %@"
+ "%{public}s::%d:Unable to save changes to Join: %@"
+ "%{public}s::%d:Unable to save changes to Recovery: %@"
+ "%{public}s::%d:Unable to save changes to Roam: %@"
+ "%{public}s::%d:Unable to update edgebss results with error: %@"
+ "%{public}s::%d:Unexpected non secure codeable object: %@ in results (%lu) for request: %@"
+ "%{public}s::%d:Unsupported band %u"
+ "%{public}s::%d:Updated autoLeaveRssi for %lu edge BSS entities - Coverage: %@"
+ "%{public}s::%d:Updated band residency for %lu networks (%lu network no usage in the last week). 2G Low Residency %lu - 2G High Residency %lu - 5G Low Residency %lu - 5G High Residency %lu - 6G Low Residency %lu - 6G High Residency %lu"
+ "%{public}s::%d:User manual join ssid = %@ bssid = %@ joinReason = %@ subReason = %@, checking the most recent event from ssid = %@, bssid = %@, isLeaveByTD = %@ entity = %@ leaveReason = %@, isLeaveToManualJoinIntervalValid = %@ interval = %@, isLeaveFromSameJoinNetwork = %@, disable isEdgeForLeave decision %@"
+ "%{public}s::%d:Warning: Item does not have date. Skipping."
+ "%{public}s::%d:`WADeviceAnalytics_UsePropertyAsFilter`, requires a non nil predicate"
+ "%{public}s::%d:`filter` predicate requires useAs (%lu) with `WADeviceAnalytics_UsePropertyAsFilter`"
+ "%{public}s::%d:bssid(%@) is the wildcard address"
+ "%{public}s::%d:cannot find %@ property in attributes or 1st level to1 relationships of %@"
+ "%{public}s::%d:configureContextAwareTDEventsToFetchWithError fails: %@"
+ "%{public}s::%d:entity does not contain attribute `date`"
+ "%{public}s::%d:event: %@"
+ "%{public}s::%d:eventDate nil"
+ "%{public}s::%d:eventsOfInterests cannot be empty"
+ "%{public}s::%d:fetch edgeBSSCount for Network %@ failed."
+ "%{public}s::%d:fetch lastPolicyRun fails with error %@"
+ "%{public}s::%d:fetch most recent leave event fails"
+ "%{public}s::%d:fetching dated events of type %@ between %@ and %@ failed with %@ - bailing from creating the sequence"
+ "%{public}s::%d:fetching dated events of type %@ between %@ and %@ failed with %@ - bailing from creating the sequences"
+ "%{public}s::%d:fetching eventsOfInterests: %@"
+ "%{public}s::%d:join event: %@[%@]"
+ "%{public}s::%d:last week wifi usage = %@, threshold = %@, isWiFiUsageSufficient = %@"
+ "%{public}s::%d:missing required parameter: bssid(%@) eventDate(%@)"
+ "%{public}s::%d:nil bss"
+ "%{public}s::%d:nil event, bailing"
+ "%{public}s::%d:nil network"
+ "%{public}s::%d:policyExecutionIntervalSufficient = %lu wifiUsageLastWeekSufficient = %lu - skipping"
+ "%{public}s::%d:processing %@ failed:%@"
+ "%{public}s::%d:resetAllInstancesUsageToZero only supports NetworkMO and LANMO entities, got %@"
+ "%{public}s::%d:sequenceStartEvents: %@ \n sequenceEndEvents: %@ \n sequenceEvents: %@"
+ "%{public}s::%d:some subentities of %@ have relationship %@ set as toOne and some as toMany"
+ "%{public}s::%d:ssid[%@] : isBand %@ relevantForSSID = %@"
+ "%{public}s::%d:unable to find bss for %@"
+ "%{public}s::%d:unable to get BSSMOs: %@"
+ "%{public}s::%d:unable to get SSID total usage data for network %@: %@"
+ "%{public}s::%d:unable to get available dimensions for edge BSS timeSpan %@: %@"
+ "%{public}s::%d:unable to get available dimensions for timeSpan %@: %@"
+ "%{public}s::%d:unable to get edge BSS usage data for network %@: %@"
+ "%{public}s::%d:unable to get usage data for network %@: %@"
+ "%{public}s::%d:unable to use band dimension for network %@: %@"
+ "%{public}s::%d:unable to use bssid dimension for edge BSS network %@: %@"
+ "%{public}s::%d:unable to use ssid dimension for edge BSS network %@: %@"
+ "%{public}s::%d:unable to use ssid dimension for network %@: %@"
+ "(reason = %@ OR reason = %@) AND rssi < %@"
+ "(source == %@ or bss == %@) and status == 0"
+ "(useAs & %d) > 0 OR (useAs & %d) > 0"
+ "+[LinkChangePolicyHandler processJoinEvent:on:]"
+ "+[UsagePoliciesHandler _calculateTDEdgeParamsVersion]"
+ "+[WADeviceAnalyticsClient sharedDeviceAnalyticsClientWithCustomStore:]"
+ "+[WADeviceAnalyticsClient sharedDeviceAnalyticsClientWithCustomStore:]_block_invoke"
+ "+[WADeviceAnalytics_Event eventDescription:from:withError:]"
+ "+[WADeviceAnalytics_Event useAsEnd:inEvents:withError:]"
+ "+[WADeviceAnalytics_Event useAsEvent:inEvents:withError:]"
+ "+[WADeviceAnalytics_Event useAsStart:inEvents:withError:]"
+ "+[WAMigrationUtils addMissingRecoveryRelationships:withError:]"
+ "+[WAMigrationUtils copyRoamTargetColumnsAddMissingRoamRelationships:withError:]"
+ "+[WAMigrationUtils migrationManagerTo:from:withError:]"
+ "+[WAMigrationUtils migrationManagerTo:from:withError:]_block_invoke"
+ "+[WAMigrationUtils modelWithHash:withError:]"
+ "+[WAMigrationUtils referenceForModel:withError:]"
+ "+[WAMigrationUtils remodelJoinReasonOnContext:withError:]"
+ "+[WAMigrationUtils stagedMigrationManagerIfNeededForMOM:andStore:withError:]"
+ "+[WAMigrationUtils tryToMigrate:using:withError:]"
+ "+[WAPersistentContainer validateEntityForGroupbyRequest:]"
+ "+[WAUtil enableCoreDataConcurrencyDebug]_block_invoke"
+ ",R"
+ "-[AnalyticsProcessor event:andResetMoc:andRunPostProcessing:withError:]"
+ "-[AnalyticsProcessor event:andResetMoc:andRunPostProcessing:withError:]_block_invoke"
+ "-[AnalyticsProcessor processCachedFaultsAndResetMoc:]"
+ "-[AnalyticsProcessor updateBandResidencyWithReason:]"
+ "-[AnalyticsProcessor updateContextAwareTDPolicies:]"
+ "-[AnalyticsReader eventSequencesFor:since:until:sortingAsc:withError:]"
+ "-[AnalyticsReader isBandRelevantForSSID:onBand:]"
+ "-[AnalyticsReader isBandRelevantForSSID:onBand:]_block_invoke"
+ "-[AnalyticsStoreFileWriter exportEntityToCSV:batchSize:maxAge:toURL:fileDate:]_block_invoke"
+ "-[AnalyticsStoreFileWriter writeRelationshipsHeaders:ofEntity:with:]"
+ "-[NSManagedObject(WiFiAnalytics) dictionaryRepresentationFor:]"
+ "-[TimeseriesPoliciesHandler findEventsIn:aroundIndex:noEarlierThan:noLaterThan:withPredicate:findingAll:]"
+ "-[TimeseriesPoliciesHandler updateBSSMOWithEdgeBSSSet:tdEdgeParamsVersion:withError:]"
+ "-[TimeseriesPoliciesHandler updateEdgeBssWithReason:at:timeSpan:]"
+ "-[TimeseriesPoliciesHandler updatePoliciesTableWithReason:withPolicyType:withOutcome:]"
+ "-[UsagePoliciesHandler canRunPolicyAtCurrentTimeForPolicyType:timespan:]"
+ "-[UsagePoliciesHandler isContextAwareTDPolicyExecutionIntervalSufficient]"
+ "-[UsagePoliciesHandler isContextAwareTDPolicyLastWeekWiFiUsageSufficient]"
+ "-[UsagePoliciesHandler resetAllInstancesUsageToZero:forTimeSpan:]"
+ "-[UsagePoliciesHandler submitBSSEventsFor:]"
+ "-[UsagePoliciesHandler submitNetworkEventsFor:]"
+ "-[UsagePoliciesHandler totalWiFiUsageInTimeSpan:around:]"
+ "-[UsagePoliciesHandler updateAutoLeaveRssiWithReason:]"
+ "-[UsagePoliciesHandler updateBandResidencyWithReason:]"
+ "-[UsagePoliciesHandler updatePoliciesTableWithPolicyType:reason:dateLessThen:object:timeSpan:]"
+ "-[WAAnalyticsAccess _performFetchWithBlockAndWait:error:onMoc:]_block_invoke"
+ "-[WADeviceAnalyticsClient _dhcpEventOnBssid:ssid:serverInfo:at:with:andDeferReclaimMem:]"
+ "-[WADeviceAnalyticsClient _geoTagEventOnBssid:ssid:lat:lon:at:andDeferReclaimMem:andRunPostProcessing:]"
+ "-[WADeviceAnalyticsClient eventSequencesFor:since:until:sortingAsc:withError:]"
+ "-[WADeviceAnalyticsClient initWithStore:]"
+ "-[WADeviceAnalyticsClient initWithStore:]_block_invoke"
+ "-[WADeviceAnalyticsClient isBandRelevantForSSID:onBand:]"
+ "-[WADeviceAnalyticsClient setCachedParamsWithBssid:ssid:]"
+ "-[WADeviceAnalyticsClient updateCachedParamsIfNeeded:]"
+ "-[WADeviceAnalyticsDatedRecord attributeDescription:]"
+ "-[WADeviceAnalytics_Event setPropertiesToFetch:withError:]"
+ "-[WAEvent _processEventOnPersistentContainer:withError:]"
+ "-[WAEvent initWithEntity:bssid:at:withLqmHistory:]"
+ "-[WAEvent processEventOnPersistentContainer:andRunPostprocessing:withError:]"
+ "-[WAEventLeave processEventOnPersistentContainer:andRunPostprocessing:withError:]"
+ "-[WAEventRoamStatus dictionaryForCA]"
+ "-[WAEventRoamStatus initWithDriverEvent:andDeviceCapabilities:at:withLqmHistory:withError:]"
+ "-[WAEventRoamStatus processEventOnPersistentContainer:andRunPostprocessing:withError:]"
+ "-[WAPersistentContainer _eventSequencesFor:withSequenceStartEvents:withSequenceEndEvents:withSequenceEvents:since:until:sortingAsc:forExport:withError:]"
+ "-[WAPersistentContainer eventSequencesFor:since:until:sortingAsc:forExport:withError:]"
+ "-[WAPersistentContainer fetchDatedEvents:since:until:ascending:withError:]"
+ "."
+ "6EDisabled"
+ "6EEnabled"
+ "="
+ "@\"NSManagedObject\""
+ "@\"TimeseriesPoliciesHandler\""
+ "@24@0:8^@16"
+ "@32@0:8^Q16@24"
+ "@52@0:8@16@24@32B40^@44"
+ "@56@0:8@16@24@32B40@44B52"
+ "@56@0:8@16@24@32B40B44^@48"
+ "@60@0:8@16Q24@32@40@48B56"
+ "@80@0:8@16@24@32@40@48@56B64B68^@72"
+ "@88@0:8@16@24@32{?=Biisds}40@72^@80"
+ "@distinctUnionOfObjects.bssid"
+ "AirPlay"
+ "AnalyticsProcessor event processCachedFaultsAndResetCache"
+ "AnalyticsProcessor event:"
+ "AnalyticsProcessor event: processCachedFaultsAndResetCache"
+ "Application"
+ "AskToJoin"
+ "Auto"
+ "AutoHotspot"
+ "AutoInstantHotspot"
+ "AutoJoinDisabled"
+ "AutoUnlock"
+ "B32@0:8@16Q24"
+ "B32@?0@\"NSStagedMigrationManager\"8@\"NSCustomMigrationStage\"16^@24"
+ "B40@0:8@16@?24^@32"
+ "B40@0:8@16B24B28^@32"
+ "BatterySaverMode"
+ "BssChanged"
+ "BssSteering"
+ "Captive"
+ "CarPlayDisabled"
+ "ColocatedUserJoin"
+ "ContextAwareTriggerDisconnect"
+ "ControlCenter"
+ "DecryptFailure"
+ "DeviceAnalytics 17.1.mom"
+ "Driving"
+ "Driving Stop"
+ "EapFailure"
+ "EapRestart"
+ "EntityType"
+ "ExceededAssignedRFPowerBudget"
+ "ExceededAssignedRoamPowerBudget"
+ "ExceededRelativeRFPowerBudget"
+ "ExceededRelativeRoamPowerBudget"
+ "FETCH "
+ "FILTER: "
+ "Faulting"
+ "FromAnyClient"
+ "FromApp"
+ "FromAskToJoin"
+ "FromControlCenter"
+ "FromHomeKit"
+ "FromOtherClient"
+ "FromRecommendation"
+ "FromSettings"
+ "FromSetup"
+ "FromSharing"
+ "GROUP_BY "
+ "HomeKit"
+ "HotspotAssociation"
+ "HotspotConnectionInactive"
+ "HotspotTransition"
+ "InfraRelayDisconnect"
+ "InternetSharing"
+ "Invalid"
+ "LeaveMO"
+ "Legacy"
+ "Legacy Transition"
+ "Lightweight migration to V18 or newer to delete Roam target columns and Join.success"
+ "Max"
+ "Misc"
+ "NOT SELF contains '.'"
+ "NetworkTransition"
+ "None"
+ "NotPrimary"
+ "Other"
+ "OtherClient"
+ "P2PRealTimeInitiated"
+ "PreferenceChanged"
+ "Q32@0:8Q16Q24"
+ "Recommendation"
+ "Running"
+ "SELF contains '.'"
+ "SELF.entity == %@"
+ "SELF.path ENDSWITH '.mom'"
+ "Schema has properties and relationships moved to Event and can be lightweight migrated. Afterwards, copy roam 'target*' attributes and relationshups into the new properties in Event and derive Network and Lan. Then remodel Join's reason, subReason and status"
+ "Seamless Transition"
+ "SeamlessNetworkTransition"
+ "SequenceEnd "
+ "SequenceEvent "
+ "SequenceStart "
+ "Settings"
+ "Setup"
+ "Sharing"
+ "SharingSilentRepair"
+ "ShortLease"
+ "SleepDenylisted"
+ "SleepOnCaptive"
+ "Stationary"
+ "T:"
+ "T@\"NSArray\",&,N,V_eventMOs"
+ "T@\"NSArray\",&,N,V_events"
+ "T@\"NSArray\",&,V_propertiesToFetch"
+ "T@\"NSArray\",&,V_relationshipKeyPathsToFetch"
+ "T@\"NSArray\",C,N,V_beaconPerHistory"
+ "T@\"NSArray\",C,N,V_beaconSchedHistory"
+ "T@\"NSArray\",C,N,V_ccaHistory"
+ "T@\"NSArray\",C,N,V_fwTxFramesHistory"
+ "T@\"NSArray\",C,N,V_fwTxPerHistory"
+ "T@\"NSArray\",C,N,V_noiseHistory"
+ "T@\"NSArray\",C,N,V_rssiHistory"
+ "T@\"NSArray\",C,N,V_snrHistory"
+ "T@\"NSArray\",C,N,V_txFrameHistory"
+ "T@\"NSArray\",C,N,V_txPerHistory"
+ "T@\"NSDate\",&,N,V_eventDate"
+ "T@\"NSDictionary\",&,N,V_endEvent"
+ "T@\"NSDictionary\",&,N,V_startEvent"
+ "T@\"NSDictionary\",&,V_properties"
+ "T@\"NSEntityDescription\",&,N,V_entity"
+ "T@\"NSManagedObject\",&,N,V_endEventMO"
+ "T@\"NSManagedObject\",&,N,V_startEventMO"
+ "T@\"NSObject<OS_dispatch_queue>\",R"
+ "T@\"NSOrderedSet\",&,D,N"
+ "T@\"NSOrderedSet\",R,D,N"
+ "T@\"NSPredicate\",&,V_entityFilter"
+ "T@\"NSSet\",&,V_keyPathsToFetch"
+ "T@\"NSString\",&,V_eventType"
+ "T@\"NSString\",&,V_propertyPath"
+ "T@\"TimeseriesPoliciesHandler\",&,N,V_timeSeriesPoliciesHandler"
+ "TB,N,V_asc"
+ "TB,N,V_isInVoluntary"
+ "TI,N,V_nanInfraImpact"
+ "Td,N,V_associationDuration"
+ "TemporarilyDisabled"
+ "Thermal"
+ "This should never be called, this method is to be implemented by subclasses"
+ "Ti,N,V_subreason"
+ "Ti,R,D"
+ "TimeseriesPoliciesHandler"
+ "Transition"
+ "TriggerDisconnect"
+ "Ts,N,V_band"
+ "Ts,N,V_bw"
+ "Ts,N,V_channel"
+ "Ts,N,V_rssi"
+ "UNUSED"
+ "Unable to get context from migrationManager (%@) container (%@)"
+ "Unable to get lightweight migration stage step to V18 or newer"
+ "Unable to get model for %@"
+ "Unknown"
+ "Unknown(%lu)"
+ "Unknown=%u"
+ "UnspecifiedClientDisconnect"
+ "UsageBased"
+ "UserNotification"
+ "UserOverridesAutoJoinDenyList"
+ "WADeviceAnalytics_Entity_Property"
+ "WADeviceAnalytics_Event"
+ "WADeviceAnalytics_EventSequence"
+ "WAEvent"
+ "WAEvent processEventOnPersistentContainer:"
+ "WAEventLQMHistory"
+ "WAEventLeave"
+ "WAEventLeave processEventAt:"
+ "WAMigrationUtils"
+ "WAStore_EnableCoreDataConcurrencyDebug"
+ "Walking"
+ "WiFiAnalytics-795.19 Feb  9 2026 22:44:13"
+ "WiFiManager"
+ "_allAttributes"
+ "_asc"
+ "_associationDuration"
+ "_bw"
+ "_calculateTDEdgeParamsVersion"
+ "_dhcpEventOnBssid:ssid:serverInfo:at:with:andDeferReclaimMem:"
+ "_diagnosticEventAt:with:andDeferReclaimMem:"
+ "_endEvent"
+ "_endEventMO"
+ "_entityFilter"
+ "_event:andDeferReclaimMem:andRunPostProcessing:withError:"
+ "_eventMOs"
+ "_eventSequencesFor:withSequenceStartEvents:withSequenceEndEvents:withSequenceEvents:since:until:sortingAsc:forExport:withError:"
+ "_events"
+ "_faultEventOn:at:with:andDeferReclaimMem:"
+ "_geoTagEventOnBssid:ssid:lat:lon:at:andDeferReclaimMem:andRunPostProcessing:"
+ "_getCurrentAutoLeaveRssiPolicyType"
+ "_isInVoluntary"
+ "_joinEventOnBssid:ssid:at:with:andDeferReclaimMem:andRunPostProcessing:"
+ "_keyPathsToFetch"
+ "_linkTestEventOn:at:with:andDeferReclaimMem:"
+ "_lqmEvent:on:at:andDeferReclaimMem:"
+ "_nanInfraImpact"
+ "_processEventOnPersistentContainer:withError:"
+ "_properties"
+ "_propertiesToFetch"
+ "_propertyPath"
+ "_prunableEntitiesWithDate"
+ "_recoveryEventOnBssid:at:with:andDeferReclaimMem:"
+ "_relationshipKeyPathsToFetch"
+ "_removeKnownNetworkEvent:at:andDeferReclaimMem:"
+ "_scanResultEventWith:ssid:whileOn:at:with:andDeferReclaimMem:"
+ "_startEvent"
+ "_startEventMO"
+ "_subreason"
+ "_timeSeriesPoliciesHandler"
+ "_updateBSS:withParsedBeacon:andDeferReclaimMem:"
+ "_updateIsBandResidencyLow:forBand:onNetwork:counters:"
+ "_updateNetwork:switchedFrom:at:andDeferReclaimMem:"
+ "addMissingRecoveryRelationships:withError:"
+ "asc"
+ "asyncAddEvent:andDeferReclaimMem:andRunPostProcessing:uponCompletionDo:"
+ "asyncAddEvent:uponCompletionDo:"
+ "asyncSubmitEvent:andDeferReclaimMem:andRunPostProcessing:uponCompletionDo:"
+ "asyncSubmitEvent:uponCompletionDo:"
+ "attributeDescription:"
+ "autoLeaveRssiTelemetry"
+ "availableEventsWithError:"
+ "band == %@"
+ "band2GResidencyHigh"
+ "band2GResidencyLow"
+ "band5GResidencyHigh"
+ "band5GResidencyLow"
+ "band6GResidencyHigh"
+ "band6GResidencyLow"
+ "bss.lan"
+ "bss.mostRecentBand"
+ "bw"
+ "canRunContextAwareTDPolicyNow"
+ "canRunPolicyAtCurrentTimeForPolicyType:timespan:"
+ "cannot find %@ property in attributes or 1st level to1 relationships of %@"
+ "checkRejoinAfterLeaveEvent:In:"
+ "com.apple.CoreData.ConcurrencyDebug"
+ "com.apple.wifi.bss"
+ "com.apple.wifi.network"
+ "com.apple.wifianalytics.dateformatter"
+ "compare:options:"
+ "configureContextAwareTDEventsToFetchWithError:"
+ "contentsOfDirectoryAtURL:includingPropertiesForKeys:options:error:"
+ "copyRoamTargetColumnsAddMissingRoamRelationships:withError:"
+ "dateFormatterQueue"
+ "defaultCStringEncoding"
+ "defaultKeysAllowedOnCustomerInstalls"
+ "dictionaryForCA"
+ "dictionaryRepresentationFor:"
+ "dictionaryWithValuesForKeys:"
+ "dontUseEvent"
+ "dontUseProperty"
+ "edgeBSSCount"
+ "edgeBSSRatio"
+ "enableCoreDataConcurrencyDebug"
+ "endEvent"
+ "endEventMO"
+ "entity does not contain attribute `date`"
+ "entityFilter"
+ "entityVersionHashesByName"
+ "evaluateWithObject:"
+ "event:%@ usedAs:%@ keyPathsToFetch:%@ entityFilter:%@"
+ "event:andDeferReclaimMem:andRunPostProcessing:withError:"
+ "event:andResetMoc:andRunPostProcessing:withError:"
+ "event:withError:"
+ "eventDescription:from:withError:"
+ "eventMOs"
+ "eventNameForCA"
+ "eventSequencesFor:since:until:sortingAsc:forExport:withError:"
+ "eventSequencesFor:since:until:sortingAsc:withError:"
+ "events"
+ "eventsIn:withPredicate:"
+ "fetchDatedEvents:since:until:ascending:withError:"
+ "filterArrayForDottedKeyPaths:"
+ "filterArrayForKeys:"
+ "findEdgeBSSFromRoamEventBeforeLeaveEvent:In:"
+ "findEdgeBSSIn:byCheckingLeaveEventsUntil:"
+ "findEventsIn:aroundIndex:noEarlierThan:noLaterThan:withPredicate:findingAll:"
+ "findNextLeaveEventFrom:In:"
+ "findRoamEventBeforeLeaveEvent:In:"
+ "getWeekStartForDate:"
+ "hasNanInfraImpact"
+ "i24@0:8i16i20"
+ "info"
+ "initWithBssid:ssid:at:data:withLqmHistory:withError:"
+ "initWithCalendarIdentifier:"
+ "initWithCurrentModelReference:nextModelReference:"
+ "initWithDriverEvent:andDeviceCapabilities:at:withLqmHistory:withError:"
+ "initWithEntity:"
+ "initWithEntity:bssid:at:withLqmHistory:"
+ "initWithMigrationStages:"
+ "initWithModel:versionChecksum:"
+ "initWithStartRecord:endRecord:sequenceRecords:asc:forEvents:forExport:"
+ "initWithStore:"
+ "initWithUsedPropertiesFromUsedEvent:"
+ "initWithVersionChecksums:"
+ "is2GHzResidencyLow"
+ "is5GHzResidencyLow"
+ "is6GHzResidencyLow"
+ "isBandRelevantForSSID:onBand:"
+ "isContextAwareTDPolicyExecutionIntervalSufficient"
+ "isContextAwareTDPolicyLastWeekWiFiUsageSufficient"
+ "isEdgeForLeaveTelemetry"
+ "isSubclassOfClass:"
+ "joinFailureAsString:"
+ "joinReasonAsString:"
+ "joinStatusAsString:"
+ "keyPathsToFetch"
+ "leaveReasonAsString:"
+ "longValue"
+ "lqmHistoriesDescription"
+ "mapOldJoinReason:andWAManualAssociationTypeMaskToJoinReason:"
+ "metadataForPersistentStoreOfType:URL:options:error:"
+ "migrationManagerTo:from:withError:"
+ "missing required parameter: bssid(%@) eventDate(%@)"
+ "modelWithHash:withError:"
+ "motionStateAsString:"
+ "nanInfraImpact"
+ "networkUsagePerc"
+ "networkUsageSec"
+ "notPredicateWithSubpredicate:"
+ "numberWithLong:"
+ "orPredicateWithSubpredicates:"
+ "predicateForIsSubEntity"
+ "processCachedFaultsAndResetMoc:"
+ "processEventOnPersistentContainer:andRunPostprocessing:withError:"
+ "processEventOnPersistentContainer:withError:"
+ "processJoinEvent:on:"
+ "processing %@ failed:%@"
+ "properties"
+ "propertiesToFetch"
+ "property:%@ useAs:%@%@"
+ "propertyPath"
+ "propertyUsedAsFilterIn:"
+ "propertyWith:"
+ "prunableEntitiesWithDate"
+ "q24@?0@\"NSDictionary\"8@\"NSDictionary\"16"
+ "q24@?0@\"NSURL\"8@\"NSURL\"16"
+ "reason != %d"
+ "referenceForModel:withError:"
+ "relationshipKeyPathsToFetch"
+ "remodelJoinReasonOnContext:withError:"
+ "resetAllInstancesUsageToZero:forTimeSpan:"
+ "reverseObjectEnumerator"
+ "roamReasonAsString:"
+ "roamStatusAsString:"
+ "rssiHistory:%@ ..."
+ "sequence start: %@\nevents (%lu): %@\nsequence end: %@"
+ "sequenceEdgeEventsIn:"
+ "sequenceEndEventsIn:"
+ "sequenceEventsIn:"
+ "sequenceStartEventsIn:"
+ "setAsc:"
+ "setAssocDuration:"
+ "setAssociationDuration:"
+ "setAutoLeaveRssiTelemetry:"
+ "setBw:"
+ "setCachedParamsWithBssid:ssid:"
+ "setDidMigrateHandler:"
+ "setEndEvent:"
+ "setEndEventMO:"
+ "setEntityFilter:"
+ "setEventMOs:"
+ "setEvents:"
+ "setHasNanInfraImpact:"
+ "setIs2GHzResidencyLow:"
+ "setIs5GHzResidencyLow:"
+ "setIs6GHzResidencyLow:"
+ "setIsEdgeForLeaveTelemetry:"
+ "setIsInVoluntary:"
+ "setKeyPathsToFetch:"
+ "setLabel:"
+ "setNanInfraImpact:"
+ "setProperties:"
+ "setPropertiesToFetch:withError:"
+ "setPropertyPath:"
+ "setRelationshipKeyPathsToFetch:"
+ "setStartEvent:"
+ "setStartEventMO:"
+ "setSubReason:"
+ "setSubreason:"
+ "setTdEdgeParamsVersion:"
+ "setTimeSeriesPoliciesHandler:"
+ "shallowCopyOfUsedEventsIn:"
+ "sharedDeviceAnalyticsClientWithCustomStore:"
+ "sortUsingSelector:"
+ "sortedArrayUsingComparator:"
+ "source.bssid"
+ "stagedMigrationManagerIfNeededForMOM:andStore:withError:"
+ "startEvent"
+ "startEventMO"
+ "subarrayWithRange:"
+ "submitBSSEventsFor:"
+ "submitEvent:andDeferReclaimMem:andRunPostProcessing:withError:"
+ "submitEvent:async:andDeferReclaimMem:andRunPostProcessing:uponCompletionDo:"
+ "submitEvent:withError:"
+ "submitNetworkEventsFor:"
+ "superentity != nil"
+ "target.lan"
+ "target.network"
+ "tdEdgeParamsVersion"
+ "tdEdgeParamsVersionAsString:"
+ "timeSeriesPoliciesHandler"
+ "totalWiFiUsageInTimeSpan:around:"
+ "tryToMigrate:using:withError:"
+ "unusedSuperEntityProperties"
+ "updateAutoLeaveRssi"
+ "updateAutoLeaveRssiTelemetryOnly"
+ "updateAutoLeaveRssiWithReason:"
+ "updateBSSMOWithEdgeBSSSet:tdEdgeParamsVersion:withError:"
+ "updateBandResidency"
+ "updateBandResidencyWithReason:"
+ "updateCachedParamsIfNeeded:"
+ "updateContextAwareTDPolicies:"
+ "updateEdgeBss"
+ "updateEdgeBssWithReason:at:timeSpan:"
+ "updatePoliciesTableWithPolicyType:reason:dateLessThen:object:timeSpan:"
+ "updatePoliciesTableWithReason:withPolicyType:withOutcome:"
+ "useAs == %d"
+ "useAs == %u"
+ "useAsDescription:"
+ "useAsEnd:inEvents:withError:"
+ "useAsEvent:inEvents:withError:"
+ "useAsStart:inEvents:withError:"
+ "useEventAsSequenceEnd"
+ "useEventAsSequenceEvent"
+ "useEventAsSequenceStart"
+ "usedPropertiesDescription"
+ "v20@?0B8@\"NSError\"12"
+ "v24@?0@\"NSFetchRequest\"8^@16"
+ "v32@?0@\"NSString\"8@\"WADeviceAnalytics_Event\"16^B24"
+ "v36@0:8@16@24B32"
+ "v40@0:8@16B24B28@?32"
+ "v40@0:8B16s20@24@32"
+ "v44@0:8@16B24B28B32@?36"
+ "v56@0:8@16@24@32@40Q48"
+ "validateEntityForGroupbyRequest:"
+ "versionChecksum"
+ "yyyy-MM-dd"
+ "{?=\"ts\"b1\"duration\"b1\"nanInfraImpact\"b1\"sdb\"b1\"use\"b1}"
+ "\xa4Q"
- "%{public}s::%d:Added Leave at [%@] to [%@][%@][%@]"
- "%{public}s::%d:ERROR: Exiting with nil WADeviceAnalyticsClient"
- "%{public}s::%d:Entity %@ is not a Dated Event"
- "%{public}s::%d:Error fetching %@: %@"
- "%{public}s::%d:Resetting cachedEdgeParams and current bssid"
- "%{public}s::%d:`WADeviceAnalytics_UsageDimensionAsFilter`, requires a non nil predicate"
- "%{public}s::%d:`filter` predicate requires useAs (%lu) with `WADeviceAnalytics_UsageDimensionAsFilter`"
- "%{public}s::%d:entity %@ is a sub-entity, skip (will be pruned at the parent level)"
- "%{public}s::%d:nil RoamEvent, bailing"
- "%{public}s::%d:no leaveRecord"
- "%{public}s::%d:processing RoamEvent failed"
- "(source == %@ or target == %@) and status == 0"
- "+[EventLeaveNetwork processRecord:bssid:ssid:withPersistentContainer:andRunPostprocessing:]"
- "+[LinkChangePolicyHandler processJoinEvent:]"
- "+[WADeviceAnalyticsClient sharedDeviceAnalyticsClient]"
- "+[WADeviceAnalyticsClient sharedDeviceAnalyticsClient]_block_invoke"
- "-[AnalyticsProcessor leaveEventOnBssid:ssid:at:with:andResetMoc:andRunPostProcessing:]_block_invoke"
- "-[AnalyticsProcessor processCachedFaultsAndResetCache:andResetMoc:]"
- "-[AnalyticsProcessor roamEvent:at:andResetMoc:andRunPostProcessing:withError:]"
- "-[AnalyticsProcessor roamEvent:at:andResetMoc:andRunPostProcessing:withError:]_block_invoke"
- "-[AnalyticsStoreFileWriter exportEntityToCSV:batchSize:maxAge:toURL:fileDate:]"
- "-[UsagePoliciesHandler updatePoliciesTableWithReason:dateLessThen:object:timeSpan:]"
- "-[WADeviceAnalyticsClient dhcpEventOnBssid:ssid:serverInfo:at:with:andDeferReclaimMem:]_block_invoke"
- "-[WADeviceAnalyticsClient geoTagEventOnBssid:ssid:lat:lon:at:andDeferReclaimMem:andRunPostProcessing:]_block_invoke"
- "-[WADeviceAnalyticsClient immediateProcessCachedFaultsAndDeferReclaimMem:]_block_invoke"
- "-[WADeviceAnalyticsClient init]"
- "-[WADeviceAnalyticsClient init]_block_invoke"
- "-[WADeviceAnalyticsClient leaveEventOnBssid:ssid:at:with:andDeferReclaimMem:]_block_invoke"
- "-[WADeviceAnalyticsClient roamEvent:at:andDeferReclaimMem:andRunPostProcessing:withError:]"
- "-[WAEventRoamStatus initWithDriverEvent:andDeviceCapabilities:withError:]"
- "-[WAEventRoamStatus processEventAt:withPersistentContainer:andRunPostprocessing:withError:]"
- "-[WAEventRoamStatus submitEventToCA]"
- "AnalyticsProcessor leaveEventOnBssid:ssid:"
- "AnalyticsProcessor roamEvent:at:"
- "AnalyticsProcessor roamEvent:at: processCachedFaultsAndResetCache"
- "B40@0:8@16@24B32B36"
- "B48@0:8@16@24B32B36^@40"
- "B52@0:8@16@24@32@?40B48"
- "Entity %@ is not a Dated Event"
- "EventLeaveNetwork"
- "WADeviceAnalyticsLeaveRecord"
- "WiFiAnalytics-788.1 Jan 27 2026 20:59:44"
- "WiFiAnalytics-788.1 Jan 27 2026 20:59:45"
- "associationState"
- "com.apple.wifi.WatchdogEvent"
- "fwSubReason"
- "immediateProcessCachedFaultsAndDeferReclaimMem:"
- "initWithDriverEvent:andDeviceCapabilities:"
- "initWithDriverEvent:andDeviceCapabilities:withError:"
- "isDriverAvailabilityNonFatal"
- "leaveEventOnBssid:ssid:at:with:"
- "leaveEventOnBssid:ssid:at:with:andDeferReclaimMem:"
- "leaveEventOnBssid:ssid:at:with:andResetMoc:andRunPostProcessing:"
- "linkTests"
- "orderedSetWithObject:"
- "processCachedFaultsAndResetCache:andResetMoc:"
- "processEventAt:withPersistentContainer:andRunPostprocessing:withError:"
- "processJoinEvent:"
- "processing RoamEvent failed"
- "recoveryLatency"
- "roamEvent:at:"
- "roamEvent:at:andDeferReclaimMem:andRunPostProcessing:"
- "roamEvent:at:andDeferReclaimMem:andRunPostProcessing:withError:"
- "roamEvent:at:andResetMoc:andRunPostProcessing:withError:"
- "setFwReason:"
- "setTargetChannelWidth:"
- "submitEvent:at:andDeferReclaimMem:andRunPostProcessing:withError:"
- "subreasonString"
- "target.bssid"
- "target.bssid == %@"
- "target.mostRecentBand"
- "target.mostRecentChannel"
- "timeBetweenFailure"
- "totalNumberOfJoinAttempts"
- "updatePoliciesTableWithReason:dateLessThen:object:timeSpan:"
- "v48@0:8@16@24@32Q40"
- "wpsConfigMethods"
- "wpsManufacturerElement"
- "wpsPrimaryDeviceTypeCategory"
- "wpsPrimaryDeviceTypeSubCategory"
- "wpsResponseType"
- "\xceQ"

```
