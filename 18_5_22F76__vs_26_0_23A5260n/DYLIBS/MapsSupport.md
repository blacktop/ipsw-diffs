## MapsSupport

> `/System/Library/PrivateFrameworks/MapsSupport.framework/MapsSupport`

```diff

-2864.35.3.6.9
-  __TEXT.__text: 0x7e3e4
+2898.30.5.20.14
+  __TEXT.__text: 0x7f9dc
   __TEXT.__auth_stubs: 0xac0
-  __TEXT.__objc_methlist: 0x835c
-  __TEXT.__const: 0x280
+  __TEXT.__objc_methlist: 0x8368
+  __TEXT.__const: 0x290
+  __TEXT.__cstring: 0x5fb3
+  __TEXT.__oslogstring: 0x8130
+  __TEXT.__gcc_except_tab: 0x1270
   __TEXT.__dlopen_cstrs: 0x104
-  __TEXT.__cstring: 0x5fb6
-  __TEXT.__oslogstring: 0x82b5
-  __TEXT.__gcc_except_tab: 0x135c
   __TEXT.__ustring: 0x2b2
-  __TEXT.__unwind_info: 0x1da0
-  __TEXT.__objc_classname: 0x12c8
-  __TEXT.__objc_methname: 0x1199f
-  __TEXT.__objc_methtype: 0x34a3
-  __TEXT.__objc_stubs: 0xcd40
-  __DATA_CONST.__got: 0x6d8
-  __DATA_CONST.__const: 0x2b88
+  __TEXT.__unwind_info: 0x1e40
+  __TEXT.__objc_classname: 0x12bb
+  __TEXT.__objc_methname: 0x1198b
+  __TEXT.__objc_methtype: 0x34a0
+  __TEXT.__objc_stubs: 0xcd80
+  __DATA_CONST.__got: 0x6b0
+  __DATA_CONST.__const: 0x2f20
   __DATA_CONST.__objc_classlist: 0x348
   __DATA_CONST.__objc_catlist: 0x90
   __DATA_CONST.__objc_protolist: 0x238
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4380
+  __DATA_CONST.__objc_selrefs: 0x4398
   __DATA_CONST.__objc_protorefs: 0x78
   __DATA_CONST.__objc_superrefs: 0x358
   __DATA_CONST.__objc_arraydata: 0x18
   __AUTH_CONST.__auth_got: 0x570
-  __AUTH_CONST.__const: 0xc40
-  __AUTH_CONST.__cfstring: 0x43e0
-  __AUTH_CONST.__objc_const: 0xd718
+  __AUTH_CONST.__const: 0xc60
+  __AUTH_CONST.__cfstring: 0x4400
+  __AUTH_CONST.__objc_const: 0xd6e0
   __AUTH_CONST.__objc_intobj: 0x228
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_doubleobj: 0x30
   __AUTH.__objc_data: 0x14a0
   __AUTH.__data: 0x10
-  __DATA.__objc_ivar: 0x4bc
-  __DATA.__data: 0x1dc0
-  __DATA.__bss: 0x30
-  __DATA.__common: 0x10
-  __DATA_DIRTY.__objc_ivar: 0x36c
+  __DATA.__objc_ivar: 0x818
+  __DATA.__data: 0x1ad0
+  __DATA.__bss: 0x1e0
   __DATA_DIRTY.__objc_data: 0xc30
-  __DATA_DIRTY.__data: 0x10
-  __DATA_DIRTY.__bss: 0x260
-  __DATA_DIRTY.__common: 0x40
+  __DATA_DIRTY.__bss: 0x118
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CloudKit.framework/CloudKit
   - /System/Library/Frameworks/Contacts.framework/Contacts

   - /System/Library/PrivateFrameworks/TCC.framework/TCC
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 84473153-191F-34CF-A52F-029669F48B3E
-  Functions: 2828
-  Symbols:   9705
-  CStrings:  5407
+  UUID: 8C7C4C11-3BAB-3B48-8DA8-C659F9104A5E
+  Functions: 2884
+  Symbols:   10091
+  CStrings:  5402
 
Symbols:
+ +[GEOSharedNavState(Testing) _msp_blockedTestTripIdentifiers].cold.1
+ +[GEOSharedNavState(Testing) _msp_testTripsByIdentifier].cold.1
+ +[MSPContact properties].cold.1
+ +[MSPMapsInstallState sharedState].cold.1
+ +[MSPMapsPushDaemonRemoteProxy sharedInstance].cold.1
+ +[MSPSharedTripCapabilityLevelFetcher sharedFetcher].cold.1
+ +[MSPSharedTripService _supportsPassingClosureReasons].cold.1
+ +[NSUUID(MSPAdditions) _maps_zeroUUID].cold.1
+ -[MSPMapsPushDaemonRemoteProxy addSufficientVisitsNotification:message:]
+ -[MSPSharedTripBlocklist setStoreSubscriptionTypes:]
+ -[MSPSharedTripBlocklist storeDidChange:]
+ -[MSPSharedTripBlocklist storeSubscriptionTypes]
+ -[MSPSharedTripService _performBlockAfterInitialSync:].cold.1
+ -[MSPSharedTripService _supportsArchivingSharingState].cold.1
+ -[MSPSharedTripService _supportsMonitoringBlockList].cold.1
+ GCC_except_table21
+ GCC_except_table24
+ GCC_except_table27
+ GCC_except_table30
+ GCC_except_table45
+ _CompanionSyncLibraryCore.frameworkLibrary
+ _DeviceIdentityLibraryCore
+ _GEOConfigMSPDefaultArrivingSoonInterval_Metadata_block_invoke_34
+ _GEOConfigMSPDefaultMaxNumberOfNotifications_Metadata_block_invoke_35
+ _GEOConfigMSPDefaultMinimumNotificationInterval_Metadata_block_invoke_36
+ _GEOConfigMSPDefaultTripAbandonExpiryInterval_Metadata_block_invoke_37
+ _GEOConfigMSPDefaultTripClosedExpiryInterval_Metadata_block_invoke_38
+ _GEOConfigMSPDefaultTripExpirationCheckupInterval_Metadata_block_invoke_39
+ _GEOConfigMSPForceLiveStrategy_Metadata_block_invoke_40
+ _GEOConfigMSPInitialMinimumETADifference_Metadata_block_invoke_41
+ _GEOConfigMSPInternalOnly_EnableSharedTripMangler
+ _GEOConfigMSPInternalOnly_EnableSharedTripMangler_Metadata
+ _GEOConfigMSPInternalOnly_EnableSharedTripMangler_Metadata_block_invoke_33
+ _GEOConfigMSPMaximumNumberNotificationsMessageStrategy_Metadata_block_invoke_42
+ _GEOConfigMSPMinimumETADifferenceIncrement_Metadata_block_invoke_43
+ _GEOConfigMSPSenderLiveStrategyETAUpdateIntervalThrottle_Metadata_block_invoke_44
+ _GEOConfigMSPSenderMinimalStrategyETANearArrivalInterval_Metadata_block_invoke_45
+ _GEOConfigMSPSenderMinimalStrategyETAUpdateIntervalThrottle_Metadata_block_invoke_46
+ _GEOConfigMSPSenderMinimalStrategyETAUpdateNearArrivalIntervalThrottle_Metadata_block_invoke_47
+ _GEOConfigMSPSharedETASenderIdentifier_Metadata_block_invoke_48
+ _GEOConfigMSPSharedTripServerEnabled_Metadata_block_invoke_49
+ _MSPBundle.bundle
+ _MSPBundle.cold.1
+ _MSPBundle.onceToken
+ _MSPGetMSPAuthFeedbackReportTicketLog.cold.1
+ _MSPGetMSPAuthFeedbackReportTicketLog.log
+ _MSPGetMSPAuthFeedbackReportTicketLog.onceToken
+ _MSPGetMSPFeedbackSubmissionTicketLog.cold.1
+ _MSPGetMSPFeedbackSubmissionTicketLog.log
+ _MSPGetMSPFeedbackSubmissionTicketLog.onceToken
+ _MSPGetMSPWalletRAPLog.log
+ _MSPGetMSPWalletRAPLog.onceToken
+ _MSPGetSharedTripCapabilityFetchingLog.cold.1
+ _MSPGetSharedTripCapabilityFetchingQueueLog.cold.1
+ _MSPGetSharedTripCapabilityFetchingQueueLog.log
+ _MSPGetSharedTripCapabilityFetchingQueueLog.onceToken
+ _MSPGetSharedTripIDSTransportLog.cold.1
+ _MSPGetSharedTripLog.cold.1
+ _MSPGetSharedTripNavEventsLog.cold.1
+ _MSPGetSharedTripStorageLog.cold.1
+ _MSPGetSharedTripVirtualReceiverLog.cold.1
+ _MSPGetSharedTripVirtualReceiverLog.log
+ _MSPGetSharedTripVirtualReceiverLog.onceToken
+ _MSPGetUGCBAAUtilitiesLog.cold.1
+ _MSPGetUGCBAAUtilitiesLog.log
+ _MSPGetUGCBAAUtilitiesLog.onceToken
+ _MSPUGCFetchClientCertificate.cold.1
+ _MSPUGCFetchClientCertificate.cold.2
+ _MSPWalletRAPAuthenticatedFeedbackTicket.cold.1
+ _MapsIDSIDStatusBlocked
+ _MapsIDSIDStatusFailed
+ _MapsPerformSelector
+ _NanoRegistryLibraryCore.frameworkLibrary
+ _OBJC_CLASS_$__TtC8MapsSync13MapsSyncStore
+ _OBJC_IVAR_$_MSPBookmarkStorage._has
+ _OBJC_IVAR_$_MSPBookmarkStorage._identifier
+ _OBJC_IVAR_$_MSPBookmarkStorage._placeBookmark
+ _OBJC_IVAR_$_MSPBookmarkStorage._position
+ _OBJC_IVAR_$_MSPBookmarkStorage._regionBookmark
+ _OBJC_IVAR_$_MSPBookmarkStorage._routeBookmark
+ _OBJC_IVAR_$_MSPBookmarkStorage._timestamp
+ _OBJC_IVAR_$_MSPBookmarkStorage._transitLineBookmark
+ _OBJC_IVAR_$_MSPBookmarkStorage._type
+ _OBJC_IVAR_$_MSPBookmarkStorage._unknownFields
+ _OBJC_IVAR_$_MSPCollectionItemReplicaStorage._clientIdentifier
+ _OBJC_IVAR_$_MSPCollectionItemReplicaStorage._records
+ _OBJC_IVAR_$_MSPCollectionItemReplicaStorage._unknownFields
+ _OBJC_IVAR_$_MSPCollectionItemStorage._contents
+ _OBJC_IVAR_$_MSPCollectionItemStorage._contentsTimestamp
+ _OBJC_IVAR_$_MSPCollectionItemStorage._position
+ _OBJC_IVAR_$_MSPCollectionItemStorage._positionTimestamp
+ _OBJC_IVAR_$_MSPCollectionItemStorage._storageIdentifier
+ _OBJC_IVAR_$_MSPCollectionItemStorage._unknownFields
+ _OBJC_IVAR_$_MSPCollectionStorage._collectionDescription
+ _OBJC_IVAR_$_MSPCollectionStorage._image
+ _OBJC_IVAR_$_MSPCollectionStorage._imageURL
+ _OBJC_IVAR_$_MSPCollectionStorage._itemData
+ _OBJC_IVAR_$_MSPCollectionStorage._title
+ _OBJC_IVAR_$_MSPCollectionStorage._unknownFields
+ _OBJC_IVAR_$_MSPCompanionSyncedItem._bookmark
+ _OBJC_IVAR_$_MSPCompanionSyncedItem._changeType
+ _OBJC_IVAR_$_MSPCompanionSyncedItem._has
+ _OBJC_IVAR_$_MSPCompanionSyncedItem._pin
+ _OBJC_IVAR_$_MSPCompanionSyncedItem._searchRequest
+ _OBJC_IVAR_$_MSPCompanionSyncedItem._syncId
+ _OBJC_IVAR_$_MSPCompanionSyncedItem._unknownFields
+ _OBJC_IVAR_$_MSPDirectionsSearch._has
+ _OBJC_IVAR_$_MSPDirectionsSearch._navigationInterrupted
+ _OBJC_IVAR_$_MSPDirectionsSearch._routeRequestStorage
+ _OBJC_IVAR_$_MSPDirectionsSearch._unknownFields
+ _OBJC_IVAR_$_MSPDroppedPin._floorOrdinal
+ _OBJC_IVAR_$_MSPDroppedPin._has
+ _OBJC_IVAR_$_MSPDroppedPin._latLng
+ _OBJC_IVAR_$_MSPDroppedPin._mapRegion
+ _OBJC_IVAR_$_MSPDroppedPin._timestamp
+ _OBJC_IVAR_$_MSPDroppedPin._unknownFields
+ _OBJC_IVAR_$_MSPEditableQuery._container
+ _OBJC_IVAR_$_MSPEditableQuery._context
+ _OBJC_IVAR_$_MSPEditableQuery._editedState
+ _OBJC_IVAR_$_MSPFileContainerPersister._ioQueue
+ _OBJC_IVAR_$_MSPFileContainerPersister._persistenceFileURL
+ _OBJC_IVAR_$_MSPGroupSessionStorage._fromID
+ _OBJC_IVAR_$_MSPGroupSessionStorage._groupIdentifier
+ _OBJC_IVAR_$_MSPGroupSessionStorage._has
+ _OBJC_IVAR_$_MSPGroupSessionStorage._lastUpdateTimestamp
+ _OBJC_IVAR_$_MSPGroupSessionStorage._liveStrategyIdentifiers
+ _OBJC_IVAR_$_MSPGroupSessionStorage._messageStrategyIdentifiers
+ _OBJC_IVAR_$_MSPGroupSessionStorage._minimalStrategyIdentifiers
+ _OBJC_IVAR_$_MSPGroupSessionStorage._originatorIdentifier
+ _OBJC_IVAR_$_MSPGroupSessionStorage._receivingAccountIdentifier
+ _OBJC_IVAR_$_MSPGroupSessionStorage._receivingHandle
+ _OBJC_IVAR_$_MSPGroupSessionStorage._smsStrategyIdentifiers
+ _OBJC_IVAR_$_MSPGroupSessionStorage._state
+ _OBJC_IVAR_$_MSPGroupSessionStorage._unknownFields
+ _OBJC_IVAR_$_MSPHistoryEntryStorage._directionsSearch
+ _OBJC_IVAR_$_MSPHistoryEntryStorage._has
+ _OBJC_IVAR_$_MSPHistoryEntryStorage._identifier
+ _OBJC_IVAR_$_MSPHistoryEntryStorage._placeDisplay
+ _OBJC_IVAR_$_MSPHistoryEntryStorage._position
+ _OBJC_IVAR_$_MSPHistoryEntryStorage._querySearch
+ _OBJC_IVAR_$_MSPHistoryEntryStorage._ridesharingTrip
+ _OBJC_IVAR_$_MSPHistoryEntryStorage._searchType
+ _OBJC_IVAR_$_MSPHistoryEntryStorage._timestamp
+ _OBJC_IVAR_$_MSPHistoryEntryStorage._tracksRAPRecordingOnly
+ _OBJC_IVAR_$_MSPHistoryEntryStorage._transitLineItem
+ _OBJC_IVAR_$_MSPHistoryEntryStorage._unknownFields
+ _OBJC_IVAR_$_MSPPinStorage._droppedPin
+ _OBJC_IVAR_$_MSPPinStorage._has
+ _OBJC_IVAR_$_MSPPinStorage._identifier
+ _OBJC_IVAR_$_MSPPinStorage._position
+ _OBJC_IVAR_$_MSPPinStorage._timestamp
+ _OBJC_IVAR_$_MSPPinStorage._type
+ _OBJC_IVAR_$_MSPPinStorage._unknownFields
+ _OBJC_IVAR_$_MSPPinnedPlaceContactStorage._contactIdentifier
+ _OBJC_IVAR_$_MSPPinnedPlaceContactStorage._handleValue
+ _OBJC_IVAR_$_MSPPinnedPlaceContactStorage._labeledValueIdentifier
+ _OBJC_IVAR_$_MSPPinnedPlaceContactStorage._unknownFields
+ _OBJC_IVAR_$_MSPPinnedPlaceStorage._contactStorages
+ _OBJC_IVAR_$_MSPPinnedPlaceStorage._customName
+ _OBJC_IVAR_$_MSPPinnedPlaceStorage._has
+ _OBJC_IVAR_$_MSPPinnedPlaceStorage._hidden
+ _OBJC_IVAR_$_MSPPinnedPlaceStorage._identifier
+ _OBJC_IVAR_$_MSPPinnedPlaceStorage._mapItemStorage
+ _OBJC_IVAR_$_MSPPinnedPlaceStorage._originatingAddressString
+ _OBJC_IVAR_$_MSPPinnedPlaceStorage._type
+ _OBJC_IVAR_$_MSPPinnedPlaceStorage._unknownFields
+ _OBJC_IVAR_$_MSPPlaceBookmark._droppedPinCoordinate
+ _OBJC_IVAR_$_MSPPlaceBookmark._droppedPinFloorOrdinal
+ _OBJC_IVAR_$_MSPPlaceBookmark._has
+ _OBJC_IVAR_$_MSPPlaceBookmark._mapItemStorage
+ _OBJC_IVAR_$_MSPPlaceBookmark._origin
+ _OBJC_IVAR_$_MSPPlaceBookmark._title
+ _OBJC_IVAR_$_MSPPlaceBookmark._unknownFields
+ _OBJC_IVAR_$_MSPPlaceDisplay._placeMapItemStorage
+ _OBJC_IVAR_$_MSPPlaceDisplay._supersededSearchIdentifier
+ _OBJC_IVAR_$_MSPPlaceDisplay._unknownFields
+ _OBJC_IVAR_$_MSPQuerySearch._language
+ _OBJC_IVAR_$_MSPQuerySearch._locationDisplayString
+ _OBJC_IVAR_$_MSPQuerySearch._mapRegion
+ _OBJC_IVAR_$_MSPQuerySearch._query
+ _OBJC_IVAR_$_MSPQuerySearch._unknownFields
+ _OBJC_IVAR_$_MSPRegionBookmark._region
+ _OBJC_IVAR_$_MSPRegionBookmark._title
+ _OBJC_IVAR_$_MSPRegionBookmark._unknownFields
+ _OBJC_IVAR_$_MSPRidesharingTrip._endWaypoint
+ _OBJC_IVAR_$_MSPRidesharingTrip._startWaypoint
+ _OBJC_IVAR_$_MSPRidesharingTrip._unknownFields
+ _OBJC_IVAR_$_MSPRouteBookmark._routeRequestStorage
+ _OBJC_IVAR_$_MSPRouteBookmark._unknownFields
+ _OBJC_IVAR_$_MSPSenderIDSStrategy._capabilitiesByParticipant
+ _OBJC_IVAR_$_MSPSenderIDSStrategy._groupSession
+ _OBJC_IVAR_$_MSPSenderIDSStrategy._lastETAUpdateDates
+ _OBJC_IVAR_$_MSPSenderIDSStrategy._participantsByCapabilities
+ _OBJC_IVAR_$_MSPSenderLiveStrategy._participantsNeedingRoute
+ _OBJC_IVAR_$_MSPSenderLiveStrategy._tokensByHandle
+ _OBJC_IVAR_$_MSPSenderMessageStrategy._delegate
+ _OBJC_IVAR_$_MSPSenderMessageStrategy._serviceName
+ _OBJC_IVAR_$_MSPSenderMessageStrategy._type
+ _OBJC_IVAR_$_MSPSharedTripBlocklist.storeSubscriptionTypes
+ _OBJC_IVAR_$_MSPSharedTripIDSCapabilityFetchingQueue._batchIDQueryController
+ _OBJC_IVAR_$_MSPSharedTripIDSCapabilityFetchingQueue._capabilityType
+ _OBJC_IVAR_$_MSPSharedTripIDSCapabilityFetchingQueue._retryAfterBackoffTimer
+ _OBJC_IVAR_$_MSPSharedTripIDSCapabilityFetchingQueue._service
+ _OBJC_IVAR_$_MSPSharedTripMessagesCapabilityFetchingQueue._batchDelayInterval
+ _OBJC_IVAR_$_MSPSharedTripMessagesCapabilityFetchingQueue._batchDelayTimer
+ _OBJC_IVAR_$_MSPSharedTripMessagesCapabilityFetchingQueue._batchSize
+ _OBJC_IVAR_$_MSPSharedTripMessagesCapabilityFetchingQueue._fetchedStatusesByHandle
+ _OBJC_IVAR_$_MSPSharedTripVirtualContact._deviceHandlesByVersion
+ _OBJC_IVAR_$_MSPSharedTripVirtualContact._virtualReceiverHandle
+ _OBJC_IVAR_$_MSPSharedTripVirtualContact._virtualReceiverName
+ _OBJC_IVAR_$_MSPSharingRestorationStorage._createdTimestamp
+ _OBJC_IVAR_$_MSPSharingRestorationStorage._groupIdentifier
+ _OBJC_IVAR_$_MSPSharingRestorationStorage._has
+ _OBJC_IVAR_$_MSPSharingRestorationStorage._mapsIdentifiers
+ _OBJC_IVAR_$_MSPSharingRestorationStorage._messagesIdentifiers
+ _OBJC_IVAR_$_MSPSharingRestorationStorage._unknownFields
+ _OBJC_IVAR_$_MSPTransitLineBookmark._transitLineStorage
+ _OBJC_IVAR_$_MSPTransitLineBookmark._unknownFields
+ _OBJC_IVAR_$_MSPTransitStorageArtwork._accessibilityText
+ _OBJC_IVAR_$_MSPTransitStorageArtwork._artworkSourceType
+ _OBJC_IVAR_$_MSPTransitStorageArtwork._artworkUseType
+ _OBJC_IVAR_$_MSPTransitStorageArtwork._has
+ _OBJC_IVAR_$_MSPTransitStorageArtwork._hasRoutingIncidentBadge
+ _OBJC_IVAR_$_MSPTransitStorageArtwork._icon
+ _OBJC_IVAR_$_MSPTransitStorageArtwork._iconFallbackShield
+ _OBJC_IVAR_$_MSPTransitStorageArtwork._shield
+ _OBJC_IVAR_$_MSPTransitStorageArtwork._unknownFields
+ _OBJC_IVAR_$_MSPTransitStorageIcon._cartoID
+ _OBJC_IVAR_$_MSPTransitStorageIcon._defaultTransitType
+ _OBJC_IVAR_$_MSPTransitStorageIcon._has
+ _OBJC_IVAR_$_MSPTransitStorageIcon._iconAttributeKey
+ _OBJC_IVAR_$_MSPTransitStorageIcon._iconAttributeValue
+ _OBJC_IVAR_$_MSPTransitStorageIcon._iconType
+ _OBJC_IVAR_$_MSPTransitStorageIcon._unknownFields
+ _OBJC_IVAR_$_MSPTransitStorageIncident._affectedEntities
+ _OBJC_IVAR_$_MSPTransitStorageIncident._blockingIncident
+ _OBJC_IVAR_$_MSPTransitStorageIncident._creationDatetime
+ _OBJC_IVAR_$_MSPTransitStorageIncident._endDatetime
+ _OBJC_IVAR_$_MSPTransitStorageIncident._fullDescription
+ _OBJC_IVAR_$_MSPTransitStorageIncident._has
+ _OBJC_IVAR_$_MSPTransitStorageIncident._iconType
+ _OBJC_IVAR_$_MSPTransitStorageIncident._lastUpdatedDatetime
+ _OBJC_IVAR_$_MSPTransitStorageIncident._messageForNonRoutable
+ _OBJC_IVAR_$_MSPTransitStorageIncident._messageForRoutePlanning
+ _OBJC_IVAR_$_MSPTransitStorageIncident._messageForRouteStepping
+ _OBJC_IVAR_$_MSPTransitStorageIncident._muid
+ _OBJC_IVAR_$_MSPTransitStorageIncident._startDatetime
+ _OBJC_IVAR_$_MSPTransitStorageIncident._summary
+ _OBJC_IVAR_$_MSPTransitStorageIncident._title
+ _OBJC_IVAR_$_MSPTransitStorageIncident._unknownFields
+ _OBJC_IVAR_$_MSPTransitStorageIncidentEntity._has
+ _OBJC_IVAR_$_MSPTransitStorageIncidentEntity._muid
+ _OBJC_IVAR_$_MSPTransitStorageIncidentEntity._nextStopsMuids
+ _OBJC_IVAR_$_MSPTransitStorageIncidentEntity._unknownFields
+ _OBJC_IVAR_$_MSPTransitStorageLine._alternateArtwork
+ _OBJC_IVAR_$_MSPTransitStorageLine._artwork
+ _OBJC_IVAR_$_MSPTransitStorageLine._has
+ _OBJC_IVAR_$_MSPTransitStorageLine._headerArtwork
+ _OBJC_IVAR_$_MSPTransitStorageLine._lineColorString
+ _OBJC_IVAR_$_MSPTransitStorageLine._locationHint
+ _OBJC_IVAR_$_MSPTransitStorageLine._modeArtwork
+ _OBJC_IVAR_$_MSPTransitStorageLine._muid
+ _OBJC_IVAR_$_MSPTransitStorageLine._name
+ _OBJC_IVAR_$_MSPTransitStorageLine._system
+ _OBJC_IVAR_$_MSPTransitStorageLine._unknownFields
+ _OBJC_IVAR_$_MSPTransitStorageLineItem._incidents
+ _OBJC_IVAR_$_MSPTransitStorageLineItem._line
+ _OBJC_IVAR_$_MSPTransitStorageLineItem._storedMapRegion
+ _OBJC_IVAR_$_MSPTransitStorageLineItem._transitAttribution
+ _OBJC_IVAR_$_MSPTransitStorageLineItem._unknownFields
+ _OBJC_IVAR_$_MSPTransitStorageShield._has
+ _OBJC_IVAR_$_MSPTransitStorageShield._shieldColorString
+ _OBJC_IVAR_$_MSPTransitStorageShield._shieldText
+ _OBJC_IVAR_$_MSPTransitStorageShield._shieldType
+ _OBJC_IVAR_$_MSPTransitStorageShield._unknownFields
+ _OBJC_IVAR_$_MSPTransitStorageSystem._artwork
+ _OBJC_IVAR_$_MSPTransitStorageSystem._has
+ _OBJC_IVAR_$_MSPTransitStorageSystem._muid
+ _OBJC_IVAR_$_MSPTransitStorageSystem._name
+ _OBJC_IVAR_$_MSPTransitStorageSystem._unknownFields
+ _OBJC_IVAR_$__MSPContainerEditAddition._addedImmutableObjects
+ _OBJC_IVAR_$__MSPContainerEditAddition._identifiersAtopByIdentifier
+ _OBJC_IVAR_$__MSPContainerEditAddition._indexesOfAddedObjects
+ _OBJC_IVAR_$__MSPContainerEditAddition._objects
+ _OBJC_IVAR_$__MSPContainerEditContentUpdate._updatedImmutableObject
+ _OBJC_IVAR_$__MSPContainerEditContentUpdate._updatedObject
+ _OBJC_IVAR_$__MSPContainerEditRemoval._indexesOfRemovedObjects
+ _OBJC_IVAR_$__MSPContainerEditRemoval._originalObjects
+ _OBJC_IVAR_$__MSPContainerEditRemoval._removedImmutableObjects
+ _OBJC_IVAR_$__MSPContainerEditReplacement._indexesOfReplacedObjects
+ _OBJC_IVAR_$__MSPContainerEditReplacement._originalImmutableObjects
+ _OBJC_IVAR_$__MSPContainerEditReplacement._originalObjects
+ _OBJC_IVAR_$__MSPContainerEditReplacement._replacementImmutableObjects
+ _OBJC_IVAR_$__MSPContainerEditReplacement._replacementObjects
+ _OUTLINED_FUNCTION_0
+ __OBJC_$_PROP_LIST_MSPSharedTripBlocklist
+ __OBJC_$_PROP_LIST__TtP8MapsSync21MapsSyncStoreDelegate_
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT__TtP8MapsSync21MapsSyncStoreDelegate_
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS__TtP8MapsSync21MapsSyncStoreDelegate_
+ __OBJC_$_PROTOCOL_METHOD_TYPES__TtP8MapsSync21MapsSyncStoreDelegate_
+ __OBJC_LABEL_PROTOCOL_$__TtP8MapsSync21MapsSyncStoreDelegate_
+ __OBJC_PROTOCOL_$__TtP8MapsSync21MapsSyncStoreDelegate_
+ ___29-[MSPMapsPaths nanoDirectory]_block_invoke
+ ___41-[MSPSharedTripBlocklist storeDidChange:]_block_invoke
+ ___63-[MSPStorageTipsManager fetchProposedTipWithCompletionHandler:]_block_invoke_2.cold.1
+ ___63-[MSPStorageTipsManager fetchProposedTipWithCompletionHandler:]_block_invoke_2.cold.2
+ ___63-[MSPStorageTipsManager fetchProposedTipWithCompletionHandler:]_block_invoke_2.cold.3
+ ___MSPUGCPerformLogDiscardForSessionEntityWithCompletion_block_invoke.cold.1
+ ___block_descriptor_40_e8_32w_e82_v48?0"MSPSharedTripSharingIdentity"8"NSArray"16"NSDictionary"24"NSArray"32Q40lw32l8
+ ___block_descriptor_56_e8_32s40bs48w_e5_v8?0lw48l8s40l8s32l8
+ ___block_descriptor_64_e8_32s40s48bs56r_e17_v16?0"NSError"8lr56l8s32l8s40l8s48l8
+ ___block_literal_global.190
+ ___block_literal_global.197
+ ___block_literal_global.204
+ ___block_literal_global.211
+ ___block_literal_global.218
+ ___block_literal_global.225
+ ___block_literal_global.242
+ ___block_literal_global.254
+ ___block_literal_global.261
+ ___block_literal_global.268
+ ___block_literal_global.275
+ ___block_literal_global.287
+ ___getNRPairedDeviceRegistryClass_block_invoke.cold.1
+ ___getSYServiceClass_block_invoke.cold.1
+ __maps_setNeedsUpdate:withSelector:.hasScheduledInvocationForSelectorsKey
+ __maps_zeroUUID.onceToken
+ __maps_zeroUUID.zeroUUID
+ __msp_blockedTestTripIdentifiers.onceToken
+ __msp_blockedTestTripIdentifiers.set
+ __msp_testTrip.onceToken
+ __msp_testTrip.trip
+ __msp_testTripClosedTripInPast.onceToken
+ __msp_testTripClosedTripInPast.trip
+ __msp_testTripSky.onceToken
+ __msp_testTripSky.trip
+ __msp_testTripWithMultipleStops.onceToken
+ __msp_testTripWithMultipleStops.trip
+ __msp_testTripWithMultipleStopsMiddleOfTrip.onceToken
+ __msp_testTripWithMultipleStopsMiddleOfTrip.trip
+ __msp_testTripsByIdentifier.onceToken
+ __msp_testTripsByIdentifier.tripsByID
+ __supportsArchivingSharingState.onceToken
+ __supportsArchivingSharingState.supported
+ __supportsMonitoringBlockList.onceToken
+ __supportsMonitoringBlockList.supported
+ __supportsPassingClosureReasons.onceToken
+ __supportsPassingClosureReasons.supported
+ _additionalKeyDescriptors
+ _getDeviceIdentityIssueClientCertificateWithCompletionSymbolLoc
+ _getDeviceIdentityIssueClientCertificateWithCompletionSymbolLoc.ptr
+ _getDeviceIdentityUCRTAttestationSupportedSymbolLoc
+ _getDeviceIdentityUCRTAttestationSupportedSymbolLoc.ptr
+ _getNRPairedDeviceRegistryClass.softClass
+ _getSYServiceClass.softClass
+ _getkMAOptionsBAAKeychainLabel
+ _getkMAOptionsBAAKeychainLabel.cold.1
+ _getkMAOptionsBAAKeychainLabelSymbolLoc
+ _getkMAOptionsBAAKeychainLabelSymbolLoc.ptr
+ _getkMAOptionsBAANonce
+ _getkMAOptionsBAANonce.cold.1
+ _getkMAOptionsBAANonceSymbolLoc
+ _getkMAOptionsBAANonceSymbolLoc.ptr
+ _getkMAOptionsBAAOIDHardwareProperties
+ _getkMAOptionsBAAOIDHardwareProperties.cold.1
+ _getkMAOptionsBAAOIDHardwarePropertiesSymbolLoc
+ _getkMAOptionsBAAOIDHardwarePropertiesSymbolLoc.ptr
+ _getkMAOptionsBAAOIDKeyUsageProperties
+ _getkMAOptionsBAAOIDKeyUsageProperties.cold.1
+ _getkMAOptionsBAAOIDKeyUsagePropertiesSymbolLoc
+ _getkMAOptionsBAAOIDKeyUsagePropertiesSymbolLoc.ptr
+ _getkMAOptionsBAAOIDNonce
+ _getkMAOptionsBAAOIDNonce.cold.1
+ _getkMAOptionsBAAOIDNonceSymbolLoc
+ _getkMAOptionsBAAOIDNonceSymbolLoc.ptr
+ _getkMAOptionsBAAOIDSToInclude
+ _getkMAOptionsBAAOIDSToInclude.cold.1
+ _getkMAOptionsBAAOIDSToIncludeSymbolLoc
+ _getkMAOptionsBAAOIDSToIncludeSymbolLoc.ptr
+ _getkMAOptionsBAASCRTAttestation
+ _getkMAOptionsBAASCRTAttestation.cold.1
+ _getkMAOptionsBAASCRTAttestationSymbolLoc
+ _getkMAOptionsBAASCRTAttestationSymbolLoc.ptr
+ _getkMAOptionsBAAValidity
+ _getkMAOptionsBAAValidity.cold.1
+ _getkMAOptionsBAAValiditySymbolLoc
+ _getkMAOptionsBAAValiditySymbolLoc.ptr
+ _getkMAOptionsResuseExistingKey
+ _getkMAOptionsResuseExistingKey.cold.1
+ _getkMAOptionsResuseExistingKeySymbolLoc
+ _getkMAOptionsResuseExistingKeySymbolLoc.ptr
+ _kMapsNeedsUpdateSelectorsToInvokeKey
+ _keyDescriptorsForFetching
+ _maps_DeviceIdentityIssueClientCertificateWithCompletion
+ _maps_DeviceIdentityIssueClientCertificateWithCompletion.cold.1
+ _maps_DeviceIdentityUCRTAttestationSupported
+ _maps_DeviceIdentityUCRTAttestationSupported.cold.1
+ _objc_msgSend$_setError
+ _objc_msgSend$addSufficientVisitsNotification:message:
+ _objc_msgSend$getBytes:range:
+ _objc_msgSend$hasError
+ _objc_msgSend$initWithExpiryTime:sharedTripIdentifier:
+ _objc_msgSend$position
+ _objc_msgSend$sharedStore
+ _objc_msgSend$subscribe:
+ _pathsAtLocation:.me
+ _pathsAtLocation:.me.32
+ _pathsAtLocation:.me.34
+ _pathsAtLocation:.onceToken
+ _pathsAtLocation:.onceToken.33
+ _pathsAtLocation:.onceToken.35
+ _properties.onceToken
+ _properties.properties
+ _sharedFetcher._once
+ _sharedFetcher._sharedFetcher
+ _sharedInstance.blocklist
+ _sharedInstance.daemonHandle
+ _sharedInstance.me
+ _sharedInstance.once
+ _sharedInstance.onceToken
+ _sharedInstance.sharedInstance
+ _sharedInstance.singleton
+ _sharedState.once
+ _sharedState.singleton
- -[MSPSharedTripBlocklist _cancelTimeoutTimer]
- -[MSPSharedTripBlocklist _resumeIsolationQueueIfNeeded]
- -[MSPSharedTripBlocklist storeControllerWithDataChanged:]
- -[MSPSharedTripBlocklist storeControllerWithDidLoad:]
- -[MSPSharedTripBlocklist storeControllerWithFailedToLoad:]
- GCC_except_table1
- GCC_except_table26
- GCC_except_table44
- OBJC_IVAR_$_PBDataReader._bytes
- OBJC_IVAR_$_PBDataReader._error
- OBJC_IVAR_$_PBDataReader._length
- OBJC_IVAR_$_PBDataReader._pos
- _GEOConfigMSPDefaultArrivingSoonInterval_Metadata_block_invoke_33
- _GEOConfigMSPDefaultMaxNumberOfNotifications_Metadata_block_invoke_34
- _GEOConfigMSPDefaultMinimumNotificationInterval_Metadata_block_invoke_35
- _GEOConfigMSPDefaultTripAbandonExpiryInterval_Metadata_block_invoke_36
- _GEOConfigMSPDefaultTripClosedExpiryInterval_Metadata_block_invoke_37
- _GEOConfigMSPDefaultTripExpirationCheckupInterval_Metadata_block_invoke_38
- _GEOConfigMSPForceLiveStrategy_Metadata_block_invoke_39
- _GEOConfigMSPInitialMinimumETADifference_Metadata_block_invoke_40
- _GEOConfigMSPMaximumNumberNotificationsMessageStrategy_Metadata_block_invoke_41
- _GEOConfigMSPMinimumETADifferenceIncrement_Metadata_block_invoke_42
- _GEOConfigMSPSenderLiveStrategyETAUpdateIntervalThrottle_Metadata_block_invoke_43
- _GEOConfigMSPSenderMinimalStrategyETANearArrivalInterval_Metadata_block_invoke_44
- _GEOConfigMSPSenderMinimalStrategyETAUpdateIntervalThrottle_Metadata_block_invoke_45
- _GEOConfigMSPSenderMinimalStrategyETAUpdateNearArrivalIntervalThrottle_Metadata_block_invoke_46
- _GEOConfigMSPSharedETASenderIdentifier_Metadata_block_invoke_47
- _GEOConfigMSPSharedTripServerEnabled_Metadata_block_invoke_48
- _OBJC_CLASS_$__TtC8MapsSync19MapsSyncStoreConfig
- _OBJC_CLASS_$__TtC8MapsSync23MapsSyncStoreController
- _OBJC_IVAR_$_MSPSharedTripBlocklist._store
- _OBJC_IVAR_$_MSPSharedTripBlocklist._storeController
- _OBJC_IVAR_$_MSPSharedTripBlocklist._storeLoadTimeoutTimer
- _OBJC_IVAR_$_MSPSharedTripBlocklist._storeQueue
- _OBJC_IVAR_$_MSPSharedTripBlocklist._waitingForStoreToLoad
- __MergedGlobals
- __MergedGlobals.1
- __MergedGlobals.9
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT__TtP8MapsSync31MapsSyncStoreControllerDelegate_
- __OBJC_$_PROTOCOL_INSTANCE_METHODS__TtP8MapsSync31MapsSyncStoreControllerDelegate_
- __OBJC_$_PROTOCOL_METHOD_TYPES__TtP8MapsSync31MapsSyncStoreControllerDelegate_
- __OBJC_LABEL_PROTOCOL_$__TtP8MapsSync31MapsSyncStoreControllerDelegate_
- __OBJC_PROTOCOL_$__TtP8MapsSync31MapsSyncStoreControllerDelegate_
- ___30-[MSPSharedTripBlocklist init]_block_invoke_2
- ___53-[MSPSharedTripBlocklist storeControllerWithDidLoad:]_block_invoke
- ___57-[MSPSharedTripBlocklist storeControllerWithDataChanged:]_block_invoke
- ___block_descriptor_48_e8_32s40w_e82_v48?0"MSPSharedTripSharingIdentity"8"NSArray"16"NSDictionary"24"NSArray"32Q40lw40l8s32l8
- ___block_literal_global.192
- ___block_literal_global.199
- ___block_literal_global.206
- ___block_literal_global.213
- ___block_literal_global.220
- ___block_literal_global.227
- ___block_literal_global.244
- ___block_literal_global.256
- ___block_literal_global.263
- ___block_literal_global.270
- ___block_literal_global.277
- _objc_msgSend$_cancelTimeoutTimer
- _objc_msgSend$_resumeIsolationQueueIfNeeded
- _objc_msgSend$defaultStoreConfig
- _objc_msgSend$initWithConfig:notifyForChanges:callbackQueue:delegate:
- _objc_msgSend$initWithStore:
- _objc_msgSend$initWithStore:expiryTime:sharedTripIdentifier:
CStrings:
+ "MSPInternalOnly_EnableSharedTripManglerKey"
+ "T@\"NSArray\",C,N"
+ "T@\"NSArray\",C,N,VstoreSubscriptionTypes"
+ "[%{public}@] block | failed to block identifiers %@: error: %@"
+ "[%{public}@] clear | failed to delete all identifiers with error: %@"
+ "[%{public}@] fetch | _fetchSyncedIdentifiers failed to fetch with error: %@"
+ "[%{public}@] purge | failed to remove identifiers with error %@"
+ "[%{public}@] reload | could not load from sync"
+ "[%{public}@] unblock | failed to unblock identifiers %@: error: %@"
+ "[GS] - mangling chunk message by dropping message ID"
+ "_TtP8MapsSync21MapsSyncStoreDelegate_"
+ "_setError"
+ "addSufficientVisitsNotification:message:"
+ "getBytes:range:"
+ "hasError"
+ "initWithExpiryTime:sharedTripIdentifier:"
+ "navigationListener:didUpdateNoCellCoverage:"
+ "navigationListener:didUpdateNoCellCoverageInfo:"
+ "setStoreSubscriptionTypes:"
+ "sharedStore"
+ "storeDidChange:"
+ "storeDidChangeWithTypes:"
+ "storeSubscriptionTypes"
+ "subscribe:"
+ "v32@0:8@\"GEONavigationListener\"16@\"GEONavigationListenerNoCellCoverageInfo\"24"
+ "v32@0:8@\"NSString\"16@\"NSString\"24"
- "@\"_TtC8MapsSync13MapsSyncStore\""
- "@\"_TtC8MapsSync23MapsSyncStoreController\""
- "[%{public}@] block | failed to block identifiers %@: error: %@, has store: %@"
- "[%{public}@] clear | failed to delete all identifiers with error: %@, has store: %@"
- "[%{public}@] fetch | _fetchSyncedIdentifiers failed to fetch with error: %@, has store: %@"
- "[%{public}@] purge | failed to remove identifiers with error %@, has store: %@"
- "[%{public}@] reload | could not load from sync (has store: %@)"
- "[%{public}@] store | cancelling timeout timer"
- "[%{public}@] store | failed to load: %@"
- "[%{public}@] store | loaded"
- "[%{public}@] store | loaded after we already resumed our queue, force reload blocked identifiers"
- "[%{public}@] timed out waiting to load store"
- "[%{public}@] tried to resume isolation queue, but already resumed (store may have loaded late)"
- "[%{public}@] unblock | failed to unblock identifiers %@: error: %@, has store: %@"
- "_TtP8MapsSync31MapsSyncStoreControllerDelegate_"
- "_cancelTimeoutTimer"
- "_resumeIsolationQueueIfNeeded"
- "_store"
- "_storeController"
- "_storeLoadTimeoutTimer"
- "_storeQueue"
- "_waitingForStoreToLoad"
- "com.apple.mapspushd.SharedTripBlocklist.store"
- "defaultStoreConfig"
- "initWithConfig:notifyForChanges:callbackQueue:delegate:"
- "initWithStore:"
- "initWithStore:expiryTime:sharedTripIdentifier:"
- "storeControllerWithDataChanged:"
- "storeControllerWithDataTypesChanged:"
- "storeControllerWithDidLoad:"
- "storeControllerWithFailedToLoad:"
- "v24@0:8@\"_TtC8MapsSync13MapsSyncStore\"16"

```
