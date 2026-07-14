## GeoServices

> `/System/Library/PrivateFrameworks/GeoServices.framework/GeoServices`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__got`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-  __TEXT.__text: 0x1998094
+  __TEXT.__text: 0x1998244
   __TEXT.__auth_stubs: 0x41a0
   __TEXT.__objc_methlist: 0xe067c
   __TEXT.__const: 0x825ff
   __TEXT.__gcc_except_tab: 0x97f84
-  __TEXT.__cstring: 0xa6a58
+  __TEXT.__cstring: 0xa6b11
   __TEXT.__dlopen_cstrs: 0x289
   __TEXT.__swift5_typeref: 0xe0e
   __TEXT.__swift5_capture: 0x488

   __TEXT.__objc_methtype: 0x74922
   __TEXT.__objc_stubs: 0x7e000
   __DATA_CONST.__got: 0x4208
-  __DATA_CONST.__const: 0x261f0
+  __DATA_CONST.__const: 0x26220
   __DATA_CONST.__objc_classlist: 0x6150
   __DATA_CONST.__objc_catlist: 0xc8
   __DATA_CONST.__objc_protolist: 0x840

   __DATA_CONST.__objc_arraydata: 0x39c8
   __AUTH_CONST.__auth_got: 0x20e8
   __AUTH_CONST.__const: 0x13e18
-  __AUTH_CONST.__cfstring: 0xb1840
+  __AUTH_CONST.__cfstring: 0xb18a0
   __AUTH_CONST.__objc_const: 0x180fb8
   __AUTH_CONST.__objc_intobj: 0x1698
   __AUTH_CONST.__objc_arrayobj: 0x7b0

   - /usr/lib/swift/libswiftos.dylib
   Functions: 102835
   Symbols:   188755
-  CStrings:  71826
+  CStrings:  71829
 
Functions:
~ -[GEOPlatform init] : 108 -> 104
~ -[_GEOCountryConfigurationRemoteProxy initWithDelegate:delegateQueue:] : 384 -> 388
~ __getMetadataStruct : 152 -> 148
~ _GEODefaultsDomain : 100 -> 72
~ _GEOConfigGetDictionary : 48 -> 44
~ ____registerStateCaptureCallbacks_block_invoke : 40 -> 44
~ ____initKeyChangeListeners_block_invoke : 456 -> 452
~ _GEOConfig_splitKeyPathComponents : 400 -> 384
~ -[GEOConfigStorageExpiryCached _expiryForKey:] : 128 -> 144
~ -[GEOConfigStorageCached getConfigValueForKey:countryCode:options:source:] : 644 -> 648
~ _GEOFindOrCreateLog : 284 -> 280
~ ____GEOConfigProxy_block_invoke : 116 -> 120
~ __GEOConfigStorageDirectSystemReadOnly : 72 -> 68
~ -[GEOLocationShifter init] : 504 -> 508
~ -[GEOPlatform hardwareIdentifier] : 120 -> 116
~ -[GEOMapService _loadOverriddenResultProviderID] : 40 -> 44
~ ___33-[GEOPlatform hardwareIdentifier]_block_invoke : 136 -> 132
~ -[GEONavigationListener _notifyWithGuidanceState:] : 192 -> 196
~ +[GEOUserSession setInitialShareSessionWithMaps:] : 16 -> 12
~ -[GEOCountryConfiguration _countryCodeOnIsolationQueue] : 124 -> 128
~ -[GEOABAssignmentResponse(GEOExperimentConfigurationExtras) _clientConfigValueForKey:] : 600 -> 596
~ _GEODefaultsGetUseTestDefaults : 32 -> 36
~ -[GEOABClientConfig _readConfigKeyValues] : 204 -> 200
~ _GEOConfig_getCountryAwareValueForKeyFromDictionary : 692 -> 696
~ ____getValue_block_invoke : 596 -> 592
~ +[GEOXPCConnection getServerConnectionFor:debugIdentifier:queue:creationBlock:reconnectBlock:eventHandler:] : 568 -> 572
~ -[GEOPlatform supportsMultiUser] : 72 -> 100
~ __GEODefaultsServerConnection : 204 -> 220
~ -[GEOConfigGetExpiringKeysRequest setKeyOptions:] : 24 -> 40
~ ___GEOGetGEOFilePathsLog_block_invoke : 84 -> 88
~ -[GEOConfigStorageDirectReadOnly _readStore] : 904 -> 884
~ -[GEOConfigStorageExpiryCached resync] : 164 -> 180
~ -[GEOConfigStorageClient getExpiringKeys:result:] : 252 -> 268
~ -[GEOConfigGetExpiringKeysRequest initWithTraits:auditToken:throttleToken:] : 40 -> 24
~ -[GEOXPCConnection setReconnectAutomatically:] : 144 -> 128
~ ___49-[GEODaemon initWithPort:createXPCListenerBlock:]_block_invoke : 488 -> 504
~ -[GEOXPCConnection _reconnectIsolated] : 316 -> 300
~ -[GEOConfigGetExpiringKeysRequest encodeToXPCDictionary:] : 144 -> 132
~ -[GEOConfigStorageDirectReadOnly getConfigValueForKey:countryCode:options:source:] : 184 -> 180
~ __GEO_validateCountryCode : 296 -> 300
~ ____GEOConfigAddListenerForKey_block_invoke_2 : 556 -> 552
~ -[_GEOCountryConfigurationInfo .cxx_destruct] : 100 -> 104
~ ___43-[_GEOConfigKeyHelper _lookupKeyProperties]_block_invoke : 200 -> 196
~ __GEOAddChangeListenerForKeys : 188 -> 172
~ -[GEOPeer _updateConnectionDebugIdentifier] : 220 -> 236
~ -[GEOXPCConnection setDebugIdentifier:] : 28 -> 12
~ +[GEOServer wantsPerMessageSignposts] : 36 -> 20
~ _GEOConfig_migrateEntitledKey : 308 -> 312
~ -[GEOConfigStorageSQLite _getExpiringKeyForKey:] : 200 -> 196
~ ___44-[GEOConfigPersistence getExpireForKeyPath:]_block_invoke : 104 -> 108
~ -[GEOConfigLocalProxy configExpiryForOptions:] : 120 -> 116
~ -[GEOConfigPersistence getExpireForKeyPath:] : 316 -> 320
~ -[_GEOConfigStorageLocalHelper getConfigValueForKey:countryCode:options:source:] : 264 -> 260
~ -[GEODefaultsDBDict objectForKeyedSubscript:] : 12 -> 28
~ ___28-[GEODaemon peerDidConnect:]_block_invoke.44 : 104 -> 88
~ -[GEODefaultsDBValue value] : 8 -> 12
~ -[GEOConfigLocalProxy configExpiryForSource:] : 440 -> 436
~ ___29-[_GEOConfigCache withCache:]_block_invoke : 32 -> 36
~ __GEOConfigStorageExpirySystem : 120 -> 100
~ ___44-[GEODaemon handleIncomingMessage:fromPeer:]_block_invoke.38 : 328 -> 312
~ -[GEOXPCConnection initWithClientConnection:debugIdentifier:] : 200 -> 204
~ -[GEOApplicationAuditToken _bundleIdForAuditToken] : 780 -> 792
~ -[GEOPeer initWithConnection:daemon:] : 580 -> 600
~ -[GEOApplicationAuditToken bundleId] : 180 -> 192
~ -[GEODaemon _createPeerForConnection:] : 128 -> 116
~ -[GEOApplicationAuditToken initCommon] : 112 -> 108
~ _AppSupportLibraryCore : 320 -> 324
~ -[GEOConfigStorageSQLite _instanceSpecificGetKey:] : 32 -> 28
~ -[GEOXPCRequest send:] : 384 -> 400
~ ___59-[GEOConfigAddChangeListenerRequest encodeToXPCDictionary:]_block_invoke : 132 -> 116
~ -[GEOXPCConnection sendMessage:] : 276 -> 292
~ -[GEOConfigAddChangeListenerRequest .cxx_destruct] : 44 -> 28
~ -[GEOResourceManifestConfiguration init] : 184 -> 156
~ -[GEOPlatform deviceScreenScale] : 88 -> 84
~ -[GEOXPCReply .cxx_destruct] : 112 -> 116
~ -[GEOLocalizationRegionsInfo init] : 100 -> 96
~ -[_GEOResourceManifestTileGroupObserverProxy init] : 116 -> 88
~ __GEOConfigStorageDirectUserReadOnly : 88 -> 84
~ -[GEOXPCRequest preferredAuditToken] : 24 -> 8
~ -[GEOConfigGetExpiringKeysReply expiringKeys] : 28 -> 44
~ ___50-[GEOXPCConnection sendMessage:withReply:handler:]_block_invoke_2 : 108 -> 112
~ _GEOConfigGetArray : 24 -> 20
~ -[GEOXPCReply replyDictionary] : 88 -> 72
~ -[GEOConfigGetAllValueInStoreRequest keyOptions] : 40 -> 24
~ -[GEOXPCConnection sendMessageWithReplySync:] : 252 -> 236
~ ___38-[GEOConfigStorageExpiryCached resync]_block_invoke : 140 -> 156
~ __GEOGetAllValuesInStore : 388 -> 360
~ -[GEOConfigStorageSQLite getAllExpiringKeys] : 28 -> 24
~ ___42-[GEOConfigPersistence getAllExpiringKeys]_block_invoke : 92 -> 76
~ -[GEOConfigGetExpiringKeysReply initWithXPCDictionary:error:] : 540 -> 524
~ -[GEOXPCRequest setService:] : 72 -> 88
~ ___65-[GEOConfigAddChangeListenerRequest initWithXPCDictionary:error:]_block_invoke : 184 -> 168
~ _GEOConfig_pruneEntitledKeysForAuditToken : 668 -> 652
~ -[GEOConfigGetAllValueInStoreReply setKeyStringsAndValues:] : 80 -> 96
~ ____geoDefaultsToDict_block_invoke : 224 -> 240
~ -[GEOConfigGetAllValueInStoreRequest initWithXPCDictionary:error:] : 164 -> 148
~ ___GEOConfig_splitKeyPathComponents_block_invoke : 64 -> 48
~ -[GEOConfigGetAllValueInStoreReply encodeToXPCDictionary:] : 168 -> 152
~ ___52-[GEOResourceManifestManager initWithConfiguration:]_block_invoke_3 : 200 -> 204
~ ___52+[GEOApplicationAuditToken currentProcessAuditToken]_block_invoke : 164 -> 192
~ +[GEOOfflineService stateManagerClass] : 96 -> 100
~ -[GEOApplicationAuditToken(Entitlements) _valueForEntitlement:] : 628 -> 624
~ +[GEOOfflineStateManager isCohortAllowed:] : 284 -> 288
~ __GEOConfigStorageUser : 124 -> 120
~ -[GEOConfigStorageCached resync] : 236 -> 240
~ -[GEOConfigStorageDirectReadOnly resync] : 32 -> 12
~ -[GEOConfigGetAllValueInStoreReply keyStringsAndValues] : 44 -> 28
~ ____GEOGetConfigStorageRemote_block_invoke : 72 -> 76
~ -[GEOExperimentConfiguration init] : 236 -> 232
~ -[GEOObserverHashTable initWithProtocol:queue:] : 240 -> 256
~ -[GEOConfigGetAllValueInStoreReply .cxx_destruct] : 24 -> 44
~ _GEOABAssignmentResponseReadAllFrom : 428 -> 424
~ -[GEOLocation(GEOProtoExtras) initWithLocation:isUserLocation:floorOrdinal:] : 204 -> 208
~ -[GEOLocation setHorizontalAccuracy:] : 72 -> 68
~ +[GEOGeographicMetadataRequester _fetchPossibleTerritoriesForLocation:retryCount:responseQueue:responseBlock:] : 544 -> 548
~ -[GEOLocation horizontalAccuracy] : 28 -> 44
~ -[GEOLatLng(GEOProtoExtras) initWithLatitude:longitude:] : 148 -> 132
~ _GEOConfigGetDouble : 108 -> 104
~ ___56-[_GEOLocationShifterRemoteProxy isLocationShiftEnabled]_block_invoke : 68 -> 88
~ -[GEOLatLng(GEOProtoExtras) initWithCoordinate:] : 20 -> 32
~ -[_GEOLocationShiftLocation latLng] : 8 -> 28
~ -[GEOLatLng(GEOProtoExtras) coordinate] : 72 -> 88
~ -[GEOLatLng lat] : 40 -> 36
~ -[GEOGeographicMetadataRequester initWithType:mcc:mnc:queue:delegate:territoryBlock:] : 812 -> 816
~ -[GEOGeographicMetadataResourceFetcher initForResourceName:] : 148 -> 144
~ -[GEOGeographicMetadataRequester location] : 132 -> 136
~ -[GEOGeographicMetadataResourceFetcher fetchMetadataForLocation:responseQueue:block:] : 240 -> 236
~ sub_186c30e20 -> sub_186c2cda0 : 416 -> 432
~ _SearchFoundationLibrary : 280 -> 296
~ _GEOGetNetworkRequestLog : 120 -> 124
~ +[_GEOLocalRequestCounterTicket requestCounterTicketForType:auditToken:traits:persistence:] : 180 -> 176
~ _GEODataRequestKindToNWActivityLabel : 388 -> 404
~ -[GEOPeer shouldThrottleMessageForServer:] : 476 -> 496
~ -[GEOConfigStorageXPC _instanceSpecificGetKeyPath:] : 20 -> 16
~ ___55-[GEOConfigPersistence xpcDefaultForKeyPathComponents:]_block_invoke : 340 -> 344
~ -[GEOConfigStorageXPC _instanceSpecificGetKey:] : 36 -> 32
~ -[GEORingThrottler addRequestTimestamp] : 176 -> 160
~ -[GEOMessage initWithXPCMessage:peer:] : 824 -> 808
~ _GEODecodeXPCValue : 232 -> 216
~ -[GEOMessage userInfo] : 36 -> 20
~ -[GEORingThrottler .cxx_construct] : 16 -> 20
~ _GeoServicesConfig_NetworkDefaultsURL_Metadata_block_invoke_7 : 8 -> 36
~ __networkDefaultsURL : 680 -> 684
~ ____GEOGetURLWithSource_block_invoke : 384 -> 380
~ -[GEOActiveTileGroup urlInfoSet] : 84 -> 88
~ sub_186c34d60 -> sub_186c30d04 : 268 -> 264
~ -[GEOActiveTileGroup _readUrlInfoSet] : 228 -> 232
~ _GEOApplicationIdentifierOrProcessName : 128 -> 124
~ -[GEOResourceManifestConfiguration .cxx_destruct] : 176 -> 180
~ _GEOABClientConfigReadSpecified : 1456 -> 1452
~ ___GEOGetNetworkDefaultsLog_block_invoke : 88 -> 92
~ ____GEOConfigAddBlockListenerForKey_block_invoke : 452 -> 448
~ +[NSDictionary(GEOXPCUtil) _geo_replyDictionaryForError:key:] : 208 -> 192
~ -[GEOMessage sendReply:] : 408 -> 392
~ -[NSDictionary(GEOXPCUtil) _geo_errorForKey:] : 124 -> 108
~ -[GEOMessage .cxx_destruct] : 132 -> 116
~ ___84-[_GEONetworkDefaultsRemoteProxy updateNetworkDefaultsWithReason:completionHandler:]_block_invoke.192 : 520 -> 504
~ -[GEOMessage _endSignpost] : 268 -> 284
~ ___84-[_GEONetworkDefaultsRemoteProxy updateNetworkDefaultsWithReason:completionHandler:]_block_invoke : 32 -> 4
~ __GEOConfigStorageSystem : 104 -> 100
~ ___30-[GEOMapService defaultTraits]_block_invoke : 1800 -> 1804
~ -[GEOMapServiceTraits transitScheduleFilter] : 100 -> 96
~ ___30-[GEOMapService defaultTraits]_block_invoke_3 : 48 -> 52
~ -[GEOTraitsTransitScheduleFilter _readLowFrequencyFilter] : 228 -> 224
~ ___30-[GEOMapService defaultTraits]_block_invoke_5 : 80 -> 84
~ -[GEOMapServiceTraits setHttpRequestPriority:] : 52 -> 48
~ ___30-[GEOMapService defaultTraits]_block_invoke_7 : 84 -> 88
~ -[GEOMapServiceTraits addSupportedAutocompleteListType:] : 164 -> 160
~ ___30-[GEOMapService defaultTraits]_block_invoke.55 : 92 -> 96
~ -[GEOTraitsTransitScheduleFilter highFrequencyFilter] : 84 -> 80
~ -[GEOTraitsTransitScheduleModeFilter(GEOMapServiceExtras) configureWithDefaultStartTime:duration:numAdditionalDepartures:] : 300 -> 304
~ -[_GEOConfigKeyHelper isEqual:] : 156 -> 152
~ -[GEOConfigStorageReadWriteAdapter initWithStorage:] : 120 -> 124
~ -[GEOPDClientMetadata setDeviceCountryCode:] : 112 -> 124
~ -[GEOPDClientMetadata setDeviceSku:] : 112 -> 100
~ -[GEOPDPlaceRequest(PlaceDataExtras) _initWithTraits:includeHistoricalLocations:supportedMapsResultTypes:] : 912 -> 892
~ -[GEOPDAnalyticMetadata(PlaceDataExtras) initWithTraits:] : 892 -> 880
~ -[GEOMapServiceTraits displayRegion] : 100 -> 92
~ -[GEOPDClientMetadata setDisplayRegion:] : 120 -> 128
~ -[GEOPDClientMetadata setEnablePreflightVenues:] : 56 -> 68
~ -[GEOPDClientMetadata setLocalizationCapabilities:] : 108 -> 96
~ _MapsFeature_IsEnabled_SearchAndDiscovery : 32 -> 24
~ -[GEOPDClientMetadata setPreferredDistanceUnit:] : 52 -> 60
~ ___GEOIsFeatureActive_block_invoke_5 : 80 -> 60
~ -[GEOPDClientMetadata _readClientRevisions] : 228 -> 216
~ _MapsFeature_IsEnabled_ApplePayEnhancementsEnabled : 72 -> 84
~ -[GEOPDClientMetadata addClientRevisions:] : 152 -> 140
~ _MapsFeature_IsEnabled_MyPlacesFeatures : 16 -> 40
~ -[GEOPDClientMetadata _readSupportedElevationModels] : 204 -> 212
~ _MapsFeature_IsEnabled_ExpertPartners : 44 -> 36
~ -[GEOPDClientMetadata setSupportHikeDisclaimer:] : 44 -> 52
~ -[GEOLocation .cxx_destruct] : 152 -> 148
~ _GEOCanonicalResourceNameAndVersionForVersionedName : 1304 -> 1308
~ -[GEOResourceRequester fetchResources:force:unpack:manifestConfiguration:auditToken:queue:handler:] : 52 -> 48
~ -[GEOActiveTileGroup _readActiveResources] : 228 -> 212
~ -[GEOResourceRequesterRemoteProxy fetchResources:force:unpack:manifestConfiguration:auditToken:signpostID:queue:handler:] : 332 -> 352
~ -[GEOResourceFetchRequest encodeToXPCDictionary:] : 604 -> 600
~ -[GEOXPCRequest _createConnectionWithQueue:] : 184 -> 188
~ -[GEOResourceFetchRequest .cxx_destruct] : 92 -> 88
~ -[GEOResource _readFilename] : 212 -> 216
~ -[GEOResourceRequester fetchResources:force:unpack:manifestConfiguration:auditToken:signpostID:queue:handler:] : 36 -> 32
~ __GEOResourceCallReadAllRecursiveWithoutSynchronized : 260 -> 264
~ -[GEOResourceFetchRequest initWithXPCDictionary:error:] : 668 -> 696
~ -[GEOResource readFrom:] : 12 -> 16
~ -[GEOResourceFetchRequest manifestConfiguration] : 32 -> 28
~ -[GEOResource _readChecksum] : 228 -> 212
~ -[GEOActiveTileGroup(Extras) isRegionalResource:] : 580 -> 596
~ -[GEOResourceLoader initWithTargetDirectory:auditToken:baseURL:alternateURLs:proxyURL:resources:forceUpdateCheck:maximumConcurrentLoads:additionalDirectoryToConsider:log:signpostID:] : 1116 -> 1120
~ +[GEOReportedProgress progressWithTotalUnitCount:] : 68 -> 96
~ -[GEOResourceInfo resource] : 16 -> 20
~ -[GEOReportedProgress setTotalUnitCount:] : 24 -> 20
~ -[GEOURLInfoSet _readResourcesURL] : 224 -> 228
~ _GeoServicesConfig_AlternateResourceURLs_Metadata_block_invoke_62 : 12 -> 8
~ -[GEOURLInfoSet resourcesURL] : 92 -> 96
~ -[GEOURLInfoSet(Extras) alternateResourcesNSURLs] : 308 -> 304
~ -[GEOURLInfoSet alternateResourcesURLs] : 72 -> 76
~ ___46-[GEOReportedProgress setCancellationHandler:]_block_invoke : 68 -> 96
~ ___GEODataRequestTimeout_block_invoke.254 : 80 -> 84
~ _GEOAuthProxyEnabledForURLInfoSet : 212 -> 208
~ __ZNSt3__120__shared_ptr_emplaceIN6gloria12DbReaderDiskENS_9allocatorIS2_EEE21__on_zero_shared_weakEv : 8 -> 12
~ _GEOGetGeographicMetadataLog : 124 -> 120
~ -[GEOGeographicMetadataRequester _processTerritories:error:] : 920 -> 924
~ -[GEOResourceFetchReply .cxx_destruct] : 88 -> 84
~ -[GEOResourceInfo equivalentResources] : 16 -> 20
~ -[GEOReportedProgress setCompletedUnitCount:] : 28 -> 24
~ -[GEOResourceLoader _cleanup] : 320 -> 324
~ -[GEOResourceFetchReply initWithXPCDictionary:error:] : 556 -> 568
~ ___121-[GEOResourceRequesterRemoteProxy fetchResources:force:unpack:manifestConfiguration:auditToken:signpostID:queue:handler:]_block_invoke : 400 -> 388
~ ___85-[GEOGeographicMetadataResourceFetcher fetchMetadataForLocation:responseQueue:block:]_block_invoke_3 : 112 -> 140
~ -[GEOResourceLoader .cxx_destruct] : 264 -> 236
~ -[GEOReportedProgress .cxx_destruct] : 96 -> 92
~ -[GEOCelestialRiseTransitSet _numberOfEvents] : 48 -> 52
~ -[GEOLunarEventCalculator lunarEventsFrom:to:] : 52 -> 80
~ __ZN11CAASidereal25MeanGreenwichSiderealTimeEd : 288 -> 292
~ -[GEOSolarEventCalculator initWithLocation:time:altitudeInDegrees:accuracy:after:] : 292 -> 288
~ __ZN17GEORiseTransitSet11eventOfTypeEj : 1540 -> 1512
~ -[GEOSolarEventCalculator dealloc] : 128 -> 124
~ -[GEOCelestialRiseTransitSet _oldestEventInJulianDay] : 128 -> 132
~ -[GEOLunarEventCalculator lunarEventsFrom:to:altitude:] : 2024 -> 2020
~ -[_GEOThrottlerShort captureState] : 24 -> 28
~ -[GEOConfigStorageXPC _instanceSpecificSetValue:forKey:] : 28 -> 24
~ -[GEOCelestialRiseTransitSet .cxx_destruct] : 80 -> 84
~ -[GEOPDClientMetadata dealloc] : 168 -> 152
~ -[GEOPDClientMetadata .cxx_destruct] : 424 -> 404
~ +[NSDate(GEOCelestial) geo_dateWithJulianDay:] : 60 -> 64
~ -[GEOLunarEvent .cxx_destruct] : 12 -> 40
~ -[GEOCelestialEphemeris equatorialCoord] : 128 -> 132
~ -[GEOLunarEvent date] : 32 -> 28
~ -[GEOMapService(ExternalRequestersOnly) serializedClientMetadataForTraits:] : 128 -> 132
~ -[GEOMapServiceTraits _readCurrentLocaleCurrencySymbol] : 208 -> 224
~ -[GEOPDClientMetadata readAll:] : 196 -> 212
~ -[GEOLocationShiftingEnabledRequest initWithXPCDictionary:error:] : 108 -> 104
~ +[GEOLocationShifter isLocationShiftEnabled] : 84 -> 88
~ _GeoServicesConfig_VoltairePolyLocationShiftURL_Metadata_block_invoke_14 : 12 -> 8
~ -[GEOURLInfoSet _readPolyLocationShiftURL] : 232 -> 204
~ -[GEOLocation _readLatLng] : 204 -> 232
~ ___56+[GEOFilePathsPrivate daemonContainerPathUsingLibSystem]_block_invoke : 152 -> 168
~ -[GEOMapsAuthServiceHelper init] : 196 -> 184
~ -[GEOLocation setIsShifted:] : 68 -> 64
~ -[GEOResourceManifestManager hasResourceManifest] : 136 -> 120
~ -[GEOMapsAuthServiceHelper _hasMRT] : 100 -> 116
~ -[GEOResourceManifestManager captureStatePlistWithHints:] : 968 -> 972
~ __deleteOldEntitledKey : 204 -> 200
~ _GEOConfig_keyRequiresEntitlement : 12 -> 16
~ -[GEOConfigStorageSQLiteBase setConfigValue:forKey:options:synchronous:] : 4 -> 32
~ -[_GEOLocationShifterRemoteProxy memoryCache] : 56 -> 60
~ _GEOConfigSetDictionary : 16 -> 12
~ ___56-[GEOXPCConnection initiateBarrierIfNecessary:delegate:]_block_invoke : 216 -> 200
~ -[GEOPeer connection] : 20 -> 36
~ __GEOConfigOptionsUseClientCache : 28 -> 32
~ ____notifyListenersOfKeyChange_block_invoke_2 : 24 -> 36
~ -[GEOConfigKeyChangeNotification initWithXPCDictionary:error:] : 412 -> 396
~ ___38-[GEOXPCConnection _reconnectIsolated]_block_invoke : 344 -> 328
~ -[GEOConfigKeyChangeNotification keyOptions] : 32 -> 16
~ -[_GEOCountryConfigurationRemoteProxy updateCountryCodeWithCallbackQueue:callback:] : 244 -> 248
~ -[GEOCountryConfigUpdateRequest initWithTraits:auditToken:throttleToken:] : 28 -> 24
~ -[_GEOCountryConfigurationRemoteProxy _xpcConnection] : 40 -> 44
~ -[GEOPlatform mapsFeatureFreedomEnabled] : 136 -> 132
~ -[_GEOCountryConfigurationUpdateHandler setCallbackQueue:] : 64 -> 68
~ -[GEOCountryConfigUpdateRequest initWithXPCDictionary:error:] : 104 -> 100
~ -[_GEOCountryConfigurationInfo encodeAsDictionary] : 260 -> 264
~ -[GEOConfigStorageDirectReadWrite setConfigValue:forKey:options:synchronous:] : 628 -> 624
~ ___68-[GEOCountryConfiguration updateCountryConfiguration:callbackQueue:]_block_invoke_2.147 : 124 -> 96
~ -[GEOCountryConfigUpdateReply encodeToXPCDictionary:] : 60 -> 56
~ -[_GEOCountryConfigurationUpdateHandler .cxx_destruct] : 92 -> 96
~ -[GEOCountryConfigUpdateReply initWithXPCDictionary:error:] : 108 -> 104
~ ___83-[_GEOCountryConfigurationRemoteProxy updateCountryCodeWithCallbackQueue:callback:]_block_invoke : 156 -> 128
~ ___49-[_GEOConfigChangedDelegateListener callListener]_block_invoke : 20 -> 16
~ ____scheduleResync_block_invoke : 440 -> 444
~ -[GEOConfigStorageSQLite _instanceSpecificSetValue:forKey:] : 28 -> 24
~ -[_GEOCountryConfigurationInfo dateOfLastUpdate] : 24 -> 28
~ ____initKeyChangeListeners_block_invoke_3 : 360 -> 372
~ -[GEOConfigKeyChangeNotification encodeToXPCDictionary:] : 436 -> 424
~ -[_GEOLocalRequestCounterTicket _incrementForApp:offlineCohortId:requestMode:startTime:endTime:requestType:result:error:xmitBytes:recvBytes:usedInterfaces:] : 600 -> 596
~ -[GEORequestCountPowerLogger _setIsDirty:] : 184 -> 188
~ -[GEOClientNetworkMetrics .cxx_destruct] : 132 -> 128
~ ___35-[GEOXPCConnection _barrierIsReady]_block_invoke_2 : 28 -> 12
~ -[GEOConfigKeyChangeNotification setKeyStrings:] : 92 -> 108
~ -[_GEONetworkDefaultsLocalProxy _processNetworkDefaultsResponse:data:error:request:] : 912 -> 916
~ +[GEONetworkEventDataRecorder recordNetworkEventDataForDataRequestKind:usedBackgroundURL:requestAppIdentifier:appMajorVersion:appMinorVersion:error:clientMetrics:additionalStates:] : 652 -> 648
~ -[GEOOfflineStateManager reportResponse:usedInterfaces:requestMode:forCohortId:duration:error:] : 224 -> 228
~ -[_GEOLocalRequestCounterTicket .cxx_destruct] : 36 -> 32
~ -[GEORequestCountPowerLogger _readFromDisk] : 1072 -> 1076
~ -[GEOReferenceTimeData kernTime] : 12 -> 8
~ ___52-[GEOMapService setDefaultTraitsHardwareIdentifier:]_block_invoke : 96 -> 100
~ -[GEOFormattedStringClientCapabilities .cxx_destruct] : 44 -> 40
~ +[GEOResourceManifestManager modernManagerForConfiguration:] : 264 -> 268
~ -[GEOLocation setTimestamp:] : 44 -> 72
~ +[GEOOfflineStateManager shared] : 116 -> 120
~ -[GEOMapServiceTraits appMinorVersion] : 80 -> 96
~ -[GEOPDAnalyticMetadata setHardwareModel:] : 120 -> 104
~ -[GEOLocation setHeading:] : 48 -> 44
~ -[GEOMapService ticketForReverseGeocodeLocation:preserveOriginalLocation:placeTypeLimit:traits:] : 276 -> 280
~ -[GEOMapServiceTraits appIdentifier] : 84 -> 100
~ -[GEOPDAnalyticMetadata setAppIdentifier:] : 120 -> 104
~ -[GEOMapServiceTraits _readAppMajorVersion] : 208 -> 224
~ -[GEOPDAnalyticMetadata setHardwareClass:] : 116 -> 100
~ -[GEOMapServiceTraits _readHardwareIdentifier] : 204 -> 220
~ -[GEOPDAnalyticMetadata setOsVersion:] : 112 -> 96
~ ___26-[GEOPlatform productName]_block_invoke : 72 -> 88
~ -[GEOPDAnalyticMetadata setProductName:] : 116 -> 100
~ -[GEOMapServiceTraits hasRouteStopCount] : 28 -> 44
~ -[GEOPDAnalyticMetadata setIsInternalInstall:] : 72 -> 56
~ -[GEOMapServiceTraits isAPICall] : 20 -> 36
~ -[GEOPDAnalyticMetadata setIsFromApi:] : 64 -> 48
~ -[GEOGeoServiceTag setTag:] : 80 -> 96
~ -[GEOPDAnalyticMetadata _readServiceTags] : 228 -> 208
~ -[GEOConfigStorageFallbackReader getConfigValueForKey:countryCode:options:source:] : 376 -> 380
~ -[GEOConfigStorageCFPrefsReadOnly getConfigValueForKey:countryCode:options:source:] : 536 -> 564
~ _GEOTileLoaderClientIdentifier : 160 -> 132
~ _GeoServicesConfig_ShouldOverrideCountryCode_Metadata_block_invoke_67 : 24 -> 20
~ ___68-[GEOCountryConfiguration updateCountryConfiguration:callbackQueue:]_block_invoke.146 : 100 -> 104
~ _MapsFeature_AddBlockListener : 572 -> 568
~ -[GEOResourceManifestConfiguration environment] : 220 -> 224
~ _GeoServicesConfig_ResourceManifestEnvironment_Metadata_block_invoke_69 : 28 -> 24
~ _GEORegionalResourcesDirectory : 152 -> 156
~ -[GEOClientCapabilities setTransitMarketSupport:] : 68 -> 64
~ -[GEOMapService setDefaultTraitsHardwareIdentifier:] : 188 -> 192
~ -[GEOAdvisoryClientCapabilities .cxx_destruct] : 32 -> 28
~ -[GEOTileCache setMaxCost:] : 132 -> 136
~ -[GEOTilePool setMaxCost:] : 156 -> 152
~ -[GEOTileLoader initWithConfiguration:] : 28 -> 32
~ +[GEOOfflineVectorTileRequester tileProviderIdentifier] : 12 -> 8
~ -[GEOActiveTileSet _readAvailableTiles] : 204 -> 220
~ _GEOTileSetRegionReadAllFrom : 1920 -> 1904
~ +[GEOVoltaireSimple3DTileRequester tileProviderIdentifier] : 32 -> 36
~ +[GEORegionalResourcesTileRequester tileProviderIdentifier] : 8 -> 36
~ -[GEOResourceManifestManager _buildResourceNamesToPaths] : 1372 -> 1376
~ _MapsFeaturesConfig_ShelbyvilleGlobe_Metadata_block_invoke_7 : 36 -> 32
~ -[GEOTileCache _evictWithMaxCost:maxCapacity:] : 244 -> 248
~ -[GEOTileServerProxy initWithCacheDBLocation:cacheFilesLocation:manifestConfiguration:locale:delegateQueue:delegate:] : 452 -> 448
~ -[GEOTileServerLocalProxy _registerBuiltInProviders] : 568 -> 572
~ +[GEOIdentifiedMapDataRequester tileProviderIdentifier] : 24 -> 20
~ ___56-[GEOResourceManifestManager _buildResourceNamesToPaths]_block_invoke : 184 -> 188
~ -[GEOExperimentConfiguration addExperimentObserver:queue:] : 8 -> 36
~ -[GEOObserverHashTable registerObserver:queue:] : 172 -> 176
~ _MapsFeaturesConfig_Maps298Enabled_Metadata_block_invoke_21 : 16 -> 12
~ -[GEOTileLoaderConfiguration setLocale:] : 72 -> 76
~ -[GEOTilePool initWithSideCacheEnabled:] : 536 -> 532
~ -[GEOTileCache init] : 524 -> 528
~ __ZN3geo6detail20_GEOGenericContainerI11_GEOTileKeyU8__strongP11objc_objectNSt3__14hashIS2_EENS6_8equal_toIS2_EENS_35GEOGenericContainerWeakReferenceTagELm0ELm0ENS_29GEOGenericContainerLockingTagENS0_21_default_pointer_typeEE6_pruneEv : 132 -> 128
~ -[GEOActiveTileSet(GEOResourceManifestManagerAdditions) maximumZoomLevelInRect:] : 192 -> 176
~ +[GEOVoltaireSputnikMetadataTileRequester tileProviderIdentifier] : 28 -> 32
~ +[GEOVoltaireTileRequester tileProviderIdentifier] : 12 -> 28
~ +[GEOFeatureSpecificSimpleTileRequester tileProviderIdentifier] : 12 -> 8
~ +[GEOPolygonSelectionSimpleTileRequester tileProviderIdentifier] : 12 -> 16
~ +[GEOMuninMeshRequester tileProviderIdentifier] : 16 -> 28
~ +[GEOGloriaQuadIDTileRequester tileProviderIdentifier] : 8 -> 24
~ +[GEOLegacyVisualLocalizationTileRequester tileProviderIdentifier] : 36 -> 8
~ +[GEOS2MapTileRequester tileProviderIdentifier] : 12 -> 8
~ -[GEOActiveTileGroup _setNoFlagsResourceCanonicalNameToFileNameValue:forKey:] : 160 -> 164
~ _MapsFeature_IsEnabled_Maps298 : 44 -> 40
~ -[GEOTileLoaderConfiguration setManifestConfiguration:] : 68 -> 72
~ +[GEOVisualLocalizationMetadataTileRequester tileProviderIdentifier] : 32 -> 28
~ _GEOTileProviderForStyle : 48 -> 52
~ +[GEOLiveTileRequester tileProviderIdentifier] : 32 -> 28
~ -[GEOResourceManager isDevResourceWithName:fallbackBundle:fallbackNameHandler:] : 120 -> 124
~ _MapsFeature_IsEnabled_ElevatedPolygons : 20 -> 16
~ -[GEONonTiledInfo name] : 92 -> 76
~ -[GEOPeer peerID] : 28 -> 12
~ -[GEONonTiledMaterialMap .cxx_destruct] : 28 -> 32
~ ___GEOConfigRemoveBlockListener_block_invoke : 440 -> 436
~ -[GEOResourceManifestServerRemoteProxy openConnection] : 24 -> 28
~ _MapsFeaturesConfig_ShelbyvilleBuildingHeights_Metadata_block_invoke_12 : 32 -> 28
~ -[GEONonTiledModel .cxx_destruct] : 120 -> 104
~ -[GEOPeer hasEntitlement:] : 92 -> 112
~ _MapsFeature_IsEnabled_ShelbyvilleBuildingHeights : 36 -> 16
~ -[GEOMessage peer] : 28 -> 16
~ __initStorage : 164 -> 160
~ -[GEONonTiledAssets materialMapsCount] : 88 -> 92
~ -[GEONetworkEventData init] : 112 -> 108
~ ___29-[GEOXPCConnection reconnect]_block_invoke : 12 -> 16
~ ____initStorage_block_invoke : 108 -> 136
~ _GeoUserSessionConfig_EVDirectionsFeedbackToggle_Metadata_block_invoke_12 : 24 -> 28
~ -[GEOAnalyticsPipelineStateData init] : 100 -> 96
~ -[GEOOfflineService initWithSubscriptionManager:preferredAuditToken:] : 652 -> 656
~ -[GEOMapDataSubscriptionManager initWithPersistence:downloadManager:syncManager:] : 412 -> 408
~ -[GEOMapDataSubscriptionRemoteDownloadManager setDelegate:] : 40 -> 12
~ -[GEOMapDataSubscriptionRemoteSyncManager setDelegate:] : 32 -> 28
~ -[GEOOfflineServiceStateSubscribeRequest encodeToXPCDictionary:] : 124 -> 128
~ _GeoOfflineConfig_CohortStateTTL_Metadata_block_invoke_18 : 16 -> 12
~ -[GEOOfflineService _updateSubscribedRegions] : 344 -> 348
~ -[GEOMapDataSubscriptionManager fetchAllSubscriptionsWithCallbackQueue:completionHandler:] : 24 -> 20
~ -[GEOMapDataSubscriptionRemotePersistence fetchSubscriptionsWithIdentifiers:callbackQueue:completionHandler:] : 256 -> 272
~ +[GEOMapSubscriptionsFetchRequest replyClass] : 40 -> 24
~ -[GEODirectionsFeedbackCollector init] : 80 -> 84
~ _MapsFeature_IsEnabled_EVRouting : 40 -> 36
~ -[GEOSQLiteDB executeAsync:errorHandler:] : 212 -> 216
~ -[GEONetworkEventData setCountryCode:] : 104 -> 100
~ -[GEOOfflineServiceSubscriptionStateChanged setCurrentState:] : 36 -> 40
~ -[GEOMapDataSubscriptionLocalPersistence fetchSubscriptionsWithIdentifiers:callbackQueue:completionHandler:] : 20 -> 16
~ -[GEOCountryConfiguration countryCode:supportsFeature:] : 1076 -> 1080
~ _GEOConfigGetBOOLForCountryCode : 96 -> 92
~ -[GEOResourceManager pathForResourceWithName:fallbackBundle:] : 8 -> 12
~ -[GEONavdPeer connection] : 8 -> 36
~ _GEOAvailableAnnouncementsReadAllFrom : 428 -> 432
~ -[GEOMapRegion _readVertexs] : 200 -> 228
~ _GEOMapRectSpans180thMeridian : 56 -> 60
~ -[GEOMapRegion addVertex:] : 132 -> 160
~ _GEOOfflineSuggestedStateAsString : 144 -> 128
~ -[GEOMapSubscriptionsFetchRequest initWithXPCDictionary:error:] : 388 -> 404
~ -[GEOXPCMessage _prepareMessage] : 180 -> 196
~ -[GEOMapSubscriptionsFetchRequest identifiersFilter] : 24 -> 44
~ -[GEOMapDataSubscriptionManager fetchSubscriptionsWithIdentifiers:callbackQueue:completionHandler:] : 8 -> 36
~ ___109-[GEOMapDataSubscriptionRemotePersistence fetchSubscriptionsWithIdentifiers:callbackQueue:completionHandler:]_block_invoke : 144 -> 128
~ -[GEOMapSubscriptionsFetchRequest .cxx_destruct] : 36 -> 24
~ -[GEOAnalyticsPipelineStateData setMapViewIsAdvancedMap:] : 52 -> 80
~ _GEOMapRectForCoordinateRegion : 852 -> 856
~ ___40-[GEOPlatform _deviceSupportsNavigation]_block_invoke : 64 -> 60
~ ___69-[GEOOfflineService initWithSubscriptionManager:preferredAuditToken:]_block_invoke_3 : 1580 -> 1596
~ -[GEOMapSubscriptionsFetchRequest fetchExpired] : 20 -> 40
~ +[GEOMapDataSubscriptionManager sharedManager] : 104 -> 100
~ ___45-[GEOOfflineService _updateSubscribedRegions]_block_invoke : 600 -> 604
~ -[GEONavdPeer hasEntitlement:] : 428 -> 424
~ _GEOAvailableAnnouncementsReadSpecified : 1068 -> 1072
~ -[GEOAnalyticsPipelineStateData setDeviceInDarkMode:] : 60 -> 56
~ -[GEOAnnouncement _readMapRegion] : 208 -> 212
~ _GEOMapRegionReadSpecified : 2680 -> 2676
~ -[GEOAnnouncement mapRegion] : 80 -> 84
~ __ZNK12geomapregion7Polygon8containsERKNS0_5PointE : 244 -> 240
~ -[GEOActiveTileGroup identifier] : 24 -> 28
~ -[GEONetworkEventData setDatasetId:] : 64 -> 60
~ -[GEONetworkEventFileManager _createIfNeededNetworkEventDataDirectory:] : 340 -> 344
~ -[GEOClientNetworkTransactionMetrics writeTo:] : 756 -> 752
~ -[GEONetworkEventFileManager _filepathFromDate:] : 188 -> 160
~ -[GEOAnalyticsDataFile writeAnalyticData:] : 400 -> 396
~ -[GEONetworkEventFileManager _startTimer] : 188 -> 192
~ ___44-[GEOReferenceTimeManager bestReferenceTime]_block_invoke : 28 -> 24
~ -[GEOResourceManifestConfiguration applicationIdentifier] : 72 -> 76
~ -[GEOExperimentConfiguration experimentsInfo] : 100 -> 96
~ -[GEOPDABClientDatasetMetadata datasetId] : 32 -> 36
~ _GEOSessionIDReadAllFrom : 860 -> 856
~ -[GEONetworkEventFile initForWriteWithFilePath:] : 92 -> 96
~ -[GEOAnalyticsDataFile prepareFileWithFilePath:isForWrite:] : 552 -> 548
~ ___42-[GEOOfflineStateManager _stateForCohort:]_block_invoke : 312 -> 284
~ -[GEOAnalyticsPipelineStateData setMapViewIsGlobeProjection:] : 52 -> 64
~ -[GEOPeer valueForEntitlement:] : 116 -> 136
~ _GEOConfigGetValueWithSourceString : 20 -> 48
~ ___81-[GEOOfflineLocalDataAccess getOfflineVersionMetadataWithCallbackQueue:callback:]_block_invoke : 140 -> 112
~ -[GEOOfflineDataConfiguration _configurationIsolated] : 888 -> 916
~ -[GEOOfflineVersionMetadataFetchReply setMetadata:] : 96 -> 100
~ _MapsFeaturesConfig_ShelbyvillePuck_Metadata_block_invoke_16 : 32 -> 28
~ -[GEOOfflineVersionMetadataFetchReply encodeToXPCDictionary:] : 168 -> 172
~ -[GEOUserSession _updateSharedSessionDataByAppId] : 256 -> 252
~ -[GEOLocation(GEOProtoExtras) initWithLatitude:longitude:floorOrdinal:] : 124 -> 128
~ -[GEOMapItemStorage setPlace:] : 116 -> 112
~ -[_GEOMapItemStorageNotificationTrampoline initWithMapItem:mapItemStorage:] : 404 -> 408
~ -[GEOMapItemStorage place] : 88 -> 84
~ ___74-[GEOMapItemStorage(GEOMapItem) _geoMapItemCreatingAndAssociatingIfNeeded]_block_invoke : 508 -> 512
~ -[GEOMapItemStorage setClientAttributes:] : 116 -> 112
~ -[GEOMapItemStorage(AdditionalFields) initAdditionalFields] : 100 -> 104
~ -[GEOMapItemStorage hasPlaceData] : 64 -> 60
~ -[GEORingThrottler .cxx_destruct] : 44 -> 48
~ _GeoServicesConfig_TransportTypePreference_Metadata_block_invoke : 32 -> 12
~ _GEOBatchLogMessageType : 72 -> 56
~ -[GEOLocation(GEOProtoExtras) initWithLatitude:longitude:] : 24 -> 28
~ -[GEOMapItemAssistant coordinate] : 68 -> 64
~ +[GEOMapItemStorage(GEOMapItem) mapItemStorageForGEOMapItem:] : 664 -> 668
~ -[GEOPlace(GEOProtoExtras) initWithLatitude:longitude:addressDictionary:] : 372 -> 368
~ -[GEOMapRegion(GEOProtoExtras) initWithLatitude:longitude:] : 156 -> 160
~ -[GEOBaseMapItem _clientAttributes] : 36 -> 32
~ -[GEOMapItemStorage(GEOMapItem) initWithPlace:clientAttributes:userValues:] : 284 -> 288
~ -[GEOMapItemStorage setUserValues:] : 100 -> 112
~ -[GEOPlace(GEOMapItemExtras) geoMapItem] : 88 -> 72
~ -[_GEOPlaceItem initWithPlace:] : 172 -> 176
~ -[GEOBusiness init] : 96 -> 124
~ -[GEOMapItemStorage(GEOMapItem) geoFenceMapRegion] : 84 -> 88
~ -[GEOMapItemStorage _readPlace] : 200 -> 228
~ -[_GEOPlaceItem displayMapRegion] : 228 -> 232
~ -[GEOPlace mapRegion] : 96 -> 92
~ -[_GEOPlaceItem coordinate] : 32 -> 36
~ -[GEOPlace center] : 88 -> 84
~ -[_GEOPlaceItem addressDictionary] : 244 -> 248
~ -[GEOPlace _readAddress] : 232 -> 228
~ -[_GEOPlaceItem name] : 16 -> 20
~ -[GEOPlace _readName] : 204 -> 232
~ -[_GEOPlaceItem timezone] : 148 -> 152
~ -[GEOTimezone identifier] : 92 -> 88
~ -[_GEOPlaceItem _muid] : 8 -> 12
~ -[GEOMapItemAssistant .cxx_destruct] : 212 -> 208
~ -[_GEOPlaceItem .cxx_destruct] : 152 -> 124
~ -[GEOBusiness .cxx_destruct] : 424 -> 404
~ -[GEOLogMsgStateDeviceIdentifier setIsInternalInstall:] : 48 -> 68
~ -[GEOAnalyticsPipelineStateData isInternalTool] : 44 -> 24
~ -[GEOLogMsgState applicationIdentifier] : 100 -> 88
~ ___47-[GEOOfflineRemoteDataAccess _ensureConnection]_block_invoke : 152 -> 148
~ -[_GEOMirroredProgress _update] : 428 -> 432
~ ___GEOGetReferenceTimeManagerLog_block_invoke : 72 -> 68
~ -[GEOResourceManifestDownload initWithData:] : 124 -> 96
~ ___32+[GEOUserSession sharedInstance]_block_invoke : 60 -> 88
~ -[NSProgress(GEOExtras) _geo_setUserInfo:] : 840 -> 856
~ -[GEOLogMsgState setApplicationIdentifier:] : 120 -> 104
~ -[GEOResourceManifestManager serverProxy] : 24 -> 28
~ ___82-[GEOOfflineRemoteDataAccess getOfflineVersionMetadataWithCallbackQueue:callback:]_block_invoke : 152 -> 148
~ _GeoUserSessionConfig_LocIntelSessionData_Metadata_block_invoke_14 : 36 -> 20
~ _GEOBatchAnalyticsSessionType : 32 -> 20
~ -[GEOUserSession _initializeShortAndNavData] : 84 -> 112
~ -[GEOXPCConnection sendMessageReporingProgress:withReply:handler:] : 580 -> 596
~ -[GEOLogMsgStateApplicationIdentifier setAppType:] : 36 -> 56
~ -[GEOOfflineRemoteDataAccess _ensureConnection] : 136 -> 132
~ -[GEOOfflineVersionMetadataFetchRequest reply] : 20 -> 24
~ +[GEOPlatform isRunningInGeoAPd] : 32 -> 28
~ +[NSURL(GEOExtras) _geo_URLWithString:tokenSubstitutions:] : 988 -> 960
~ +[GEOReferenceTimeData supportsSecureCoding] : 28 -> 24
~ _GEOResourceManifestDownloadReadSpecified : 1544 -> 1548
~ +[GEOUserSession initialShareSessionWithMaps] : 40 -> 20
~ -[GEOLogMsgStateDeviceIdentifier copyWithZone:] : 524 -> 512
~ _GEOConfigSetBOOL : 128 -> 124
~ -[GEOConfigStorageClient setConfigValue:forKey:options:synchronous:] : 248 -> 264
~ -[GEOConfigStorageSetValueForKeyRequest setKeyOptions:] : 44 -> 32
~ -[GEOLocalTime setTimezoneOffsetFromGmtInHours:] : 48 -> 60
~ -[GEOLogMsgStateApplicationIdentifier readAll:] : 196 -> 212
~ -[GEOResourceManifestServerRemoteProxy activateResourceScale:] : 204 -> 208
~ -[GEOResourceManifestActivateFilterRequest filter] : 28 -> 24
~ -[GEOActiveResourceFilter resetFilter] : 96 -> 100
~ -[GEOResourceManifestActivateFilterRequest encodeToXPCDictionary:] : 196 -> 192
~ -[GEOActiveResourceFilter writeTo:] : 248 -> 252
~ -[GEOResourceManifestActivateFilterRequest .cxx_destruct] : 32 -> 28
~ -[GEOResource _addNoFlagsFilter:] : 160 -> 132
~ -[GEOResourceManifestActivateFilterRequest initWithXPCDictionary:error:] : 300 -> 296
~ __GEOURLInfoSetCallReadAllRecursiveWithoutSynchronized : 1376 -> 1380
~ _GEOLocalizedStringReadSpecified : 1240 -> 1236
~ -[GEOActiveTileSet _addNoFlagsSupportedLanguage:] : 140 -> 156
~ _GEOCountryRegionTupleReadSpecified : 1236 -> 1252
~ __GEOActiveTileSetCallReadAllRecursiveWithoutSynchronized : 428 -> 412
~ -[GEOCountryRegionTuple readAll:] : 204 -> 188
~ -[GEORegionalResourceSet readAll:] : 208 -> 224
~ -[GEOLogMsgState copyWithZone:] : 2248 -> 2268
~ +[GEOUserSession sharedInstance] : 116 -> 128
~ -[GEOConfigStorageSetValueForKeyRequest .cxx_destruct] : 104 -> 88
~ -[GEOSQLiteDB int64ForColumn:inStatment:] : 124 -> 108
~ -[GEOConfigStorageSetValueForKeyRequest setKeyValue:] : 108 -> 92
~ -[GEOAttribution readAll:] : 216 -> 200
~ -[GEOLogMsgEvent addLogMsgState:] : 164 -> 148
~ -[GEOLocalTime(GEOExtras) initWithCFAbsoluteTime:] : 176 -> 192
~ -[GEOLogMsgStateUserSession setEventTime:] : 72 -> 88
~ -[GEOLogMessage setLogMessageType:] : 60 -> 44
~ -[GEOLogMsgEvent readAll:] : 200 -> 220
~ -[GEOLocalTime writeTo:] : 196 -> 208
~ -[GEOConfigStorageSetValueForKeyRequest keyOptions] : 20 -> 36
~ -[GEOVersionManifest readAll:] : 32 -> 4
~ _MapsFeature_IsEnabled_PlaceCardShowcase : 32 -> 44
~ -[GEOPDClientMetadata addSupportedMapsResultType:] : 156 -> 136
~ -[GEOPDClientMetadata setSupportEnrichment:] : 56 -> 44
~ -[GEOPDClientMetadata _readSupportedMapsResultTypes] : 204 -> 220
~ -[GEOPDPlaceRequest setDisplayRegion:] : 112 -> 116
~ -[GEOPDPlaceRequest(PlaceDataExtras) addRequestedComponentsForReason:traits:count:] : 136 -> 148
~ +[GEOPDPlaceRequest(PlaceDataExtras) componentInfoWithType:count:traits:] : 2256 -> 2240
~ sub_186c9fb98 -> sub_186c9bbb8 : 236 -> 240
~ -[GEOABAssignmentResponse mapsAbClientMetadata] : 76 -> 72
~ -[GEOCoalescingTimer scheduleRun] : 468 -> 440
~ _GEOLatLngReadAllFrom : 1400 -> 1396
~ ___44-[GEOResourceManifestManager isMuninEnabled]_block_invoke : 68 -> 72
~ _MapsFeaturesConfig_IsMuninEnabled_Metadata_block_invoke_2 : 16 -> 12
~ -[GEOActiveTileGroup _addNoFlagsMuninBucket:] : 156 -> 160
~ ____GEOConfigRangeCheckEnabled_block_invoke : 348 -> 344
~ +[GEONotificationPreferenceManager sharedManager] : 108 -> 112
~ -[GEOPDComponentInfo(PlaceDataExtras) initWithType:count:] : 176 -> 172
~ -[GEOPDETAFilter readAll:] : 244 -> 248
~ -[GEOTraitsTransitScheduleTimeRange duration] : 36 -> 32
~ -[GEOPDTransitScheduleFilter setDeparturePredicateStamp:] : 144 -> 148
~ -[GEOTraitsTransitScheduleFilter hasOperatingHoursRange] : 84 -> 64
~ ___86+[GEOPDPlaceRequest(PlaceDataExtras) createRequestedComponentsForReason:traits:count:]_block_invoke : 20 -> 36
~ __GEOPDComponentFilterCallReadAllRecursiveWithoutSynchronized : 148 -> 152
~ -[GEOTraitsTransitScheduleFilter _readOperatingHoursRange] : 228 -> 224
~ __ZNK8addr_obj27SerializedStructuredAddress3getEv : 8 -> 12
~ -[GEOTraitsTransitScheduleTimeRange startTime] : 16 -> 44
~ -[GEOPDComponentFilter setFactoidFilter:] : 148 -> 152
~ -[GEOMapServiceTraits photosCount] : 40 -> 36
~ -[GEOPDCaptionedPhotoFilter _readPhotoSizeFilters] : 188 -> 192
~ -[GEOTraitsPhotoSize height] : 32 -> 28
~ -[GEOPDForwardInfoFilter hash] : 16 -> 20
~ -[GEOPDComponentFilter(PlaceDataExtras) initReviewUserPhotoFilterWithTraits:] : 452 -> 448
~ -[GEOPDComponentFilter setReviewFilter:] : 140 -> 144
~ -[GEOTraitsTransitScheduleFilter operatingHoursRange] : 100 -> 96
~ -[GEOPDComponentFilter factoidFilter] : 232 -> 236
~ -[GEOLatLng writeTo:] : 220 -> 216
~ -[GEOPDComponentInfo isEqual:] : 376 -> 380
~ -[GEOPDComponentFilter(PlaceDataExtras) initTransitScheduleFilterWithTraits:] : 572 -> 568
~ -[GEOPDCategorizedPhotosFilter hash] : 272 -> 276
~ -[GEOPDComponentFilter(PlaceDataExtras) initCaptionedPhotoFilterWithTraits:] : 392 -> 420
~ __ZN8addr_obj10getVersionEv : 60 -> 64
~ -[GEOPDComponentFilter(PlaceDataExtras) initAddressObjectFilterWithLibraryVersion:] : 148 -> 176
~ -[GEOPDAddressObjectFilter hash] : 124 -> 128
~ -[GEOPDPlaceRequestParameters(PlaceDataExtras) initWithReverseGeocodeLocation:preserveOriginalLocation:placeTypeLimit:] : 312 -> 308
~ -[GEOPDPlaceRequestParameters _readReverseGeocodingParameters] : 228 -> 232
~ -[GEOMapItemInitialRequestData setRequestType:] : 44 -> 40
~ -[GEOPDReverseGeocodingParameters readAll:] : 252 -> 256
~ -[GEOMapItemInitialRequestData setPlaceRequestParameters:] : 92 -> 88
~ _GEOPDReverseGeocodingParametersHasSensitiveFields : 284 -> 288
~ -[GEOLocation hasIsMatchedLocation] : 48 -> 44
~ _GEOPDReverseGeocodingParametersClearSensitiveFields : 244 -> 248
~ _GEOLocationClearSensitiveFields : 472 -> 468
~ -[GEOPDReverseGeocodingParameters writeTo:] : 768 -> 772
~ -[GEOLocation writeTo:] : 1256 -> 1284
~ _GEOPDReverseGeocodingParametersReadSpecified : 1920 -> 1924
~ -[GEOLatLng readAll:] : 24 -> 20
~ -[GEOURLInfoSet _readAnalyticsCohortSessionURL] : 220 -> 204
~ _GEOBatchDescription : 292 -> 276
~ -[GEOAttribution _readUrl] : 224 -> 208
~ -[GEOLogMsgEvent setMapsEngagement:] : 116 -> 132
~ __NSDictionarySafeEncodingCopy : 836 -> 808
~ _GEOConfigGetDate : 40 -> 36
~ -[GEOXPCReplyError .cxx_destruct] : 84 -> 68
~ -[GEOLogMsgEventMapsEngagement setAppType:] : 48 -> 68
~ -[GEOUserSession(DependencyInjection) _get15moDeviceSessionConfiguredEpoch] : 44 -> 40
~ _GeoUserSessionConfig_FifteenMonthDeviceSessionConfiguredEpoch_Metadata_block_invoke : 20 -> 24
~ -[GEOUserSession(DependencyInjection) _get15moDeviceRawSessionData] : 36 -> 32
~ -[GEOAPSessionData mapsUserStartDate] : 40 -> 24
~ -[GEOLogMsgStateUser writeTo:] : 740 -> 756
~ _GEOMapPointsPerMeterAtLatitude : 264 -> 248
~ -[GEOLogMsgEventMapsEngagement init] : 96 -> 112
~ -[GEOXPCReplyError encodeToXPCDictionary:] : 328 -> 344
~ -[GEOLogMsgEventMapsEngagement setReportingChannel:] : 52 -> 40
~ -[GEOUserSession(DependencyInjection) _get15moDeviceSessionData] : 240 -> 236
~ -[GEOAPSessionData setHasRotated:] : 64 -> 36
~ -[GEOUserSession(DependencyInjection) _set15moDeviceSessionData:] : 100 -> 96
~ -[GEOAPSessionData hasRotated] : 40 -> 24
~ -[GEOLogMsgEventMapsEngagement readAll:] : 184 -> 200
~ -[GEOSQLiteDB executeStatement:statementBlock:] : 424 -> 428
~ _GeoServicesConfig_AnalyticsCohortSessionURL_Metadata_block_invoke_34 : 32 -> 12
~ -[GEOLogMsgEvent _readWifiConnectionQualityProbeEvent] : 220 -> 204
~ -[GEOLogMessage addLogMsgEvent:] : 128 -> 144
~ -[GEOLogMsgStateUserSession .cxx_destruct] : 88 -> 108
~ -[GEOLocalTime .cxx_destruct] : 96 -> 108
~ -[GEOLogMsgEventMapsEngagement .cxx_destruct] : 152 -> 136
~ ___59-[GEOSQLiteDB bindBlobParameter:toValue:inStatement:error:]_block_invoke : 156 -> 172
~ -[GEOLogMsgState setUser:] : 100 -> 120
~ -[GEOAnalyticsPipelineStateData mapsUserStartDate] : 24 -> 36
~ -[GEOLogMsgState hasLookAroundView] : 76 -> 60
~ -[GEOLogMessage writeTo:] : 352 -> 368
~ -[GEOLogMsgState writeTo:] : 2276 -> 2260
~ -[GEOLogMessage .cxx_destruct] : 24 -> 40
~ -[GEOLogMsgEventUserAction .cxx_destruct] : 164 -> 180
~ -[GEOAPSessionData setCreateTime:] : 56 -> 60
~ +[GEOUserSession(DependencyInjection) _newSessionId] : 76 -> 72
~ -[GEOAPSessionData writeTo:] : 528 -> 532
~ -[GEOUserSession _sessionCreateHourWithSessionCreateTime:] : 248 -> 244
~ -[GEOMapService ticketForDatasetCheckWithTraits:] : 196 -> 200
~ -[GEOUserSession _updateNavSessionIDAtTime:] : 304 -> 316
~ ___57-[GEOPDAnalyticMetadata(PlaceDataExtras) initWithTraits:]_block_invoke : 188 -> 192
~ -[GEOPDAnalyticMetadata setSessionCreateHour:] : 52 -> 68
~ _GeoServicesConfig_DispatcherURL_Metadata_block_invoke_25 : 8 -> 36
~ -[GEOPDPlaceRequest isEqual:] : 656 -> 644
~ -[GEOPDAnalyticMetadata isEqual:] : 976 -> 992
~ -[GEOGeoServiceTag isEqual:] : 212 -> 208
~ -[GEOPDStorefrontPresentationFilter hash] : 8 -> 12
~ -[GEOPDComponentFilter(PlaceDataExtras) initAnnotatedItemListFilterWithTraits:] : 420 -> 416
~ -[GEOPDAnnotatedItemListFilter hash] : 56 -> 60
~ _MapsFeaturesConfig_ShelbyvilleStonehenge_Metadata_block_invoke_14 : 28 -> 24
~ -[GEOPDComponentFilter relatedPlaceFilter] : 236 -> 240
~ -[GEOMapServiceTraits relatedPlaceItemCount] : 36 -> 32
~ -[GEOPDRelatedPlaceFilter hash] : 104 -> 108
~ -[GEOMapServiceTraits hasSupportChildItems] : 44 -> 40
~ -[GEOPDComponentFilter setResultSnippetFilter:] : 160 -> 164
~ -[GEOMapServiceTraits _readSupportedChildActions] : 204 -> 232
~ -[GEOPDResultSnippetFilter hash] : 172 -> 176
~ -[GEOPDComponentFilter(PlaceDataExtras) initTipUserPhotoFilterWithTraits:] : 396 -> 392
~ -[GEOPDTipFilter hash] : 52 -> 68
~ +[GEOPDPlaceRequest(PlaceDataExtras) collectionComponentInfoForReason:count:traits:] : 556 -> 572
~ -[GEOPDPlaceCollectionFilter hash] : 272 -> 256
~ +[GEOPDPlaceRequest(PlaceDataExtras) publisherComponentInfoForReason:count:traits:] : 252 -> 236
~ -[GEOPDPublisherFilter hash] : 80 -> 52
~ _MapsFeature_IsAvailable_ShelbyvilleSearch : 16 -> 12
~ -[GEOPDComponentInfo .cxx_destruct] : 84 -> 88
~ -[GEOMapServiceTraits wantsRouteCreationTip] : 40 -> 36
~ -[GEOPDSupportsOfflineMapsFilter hash] : 28 -> 12
~ ____getPlaceRequestExtras_block_invoke : 188 -> 208
~ -[GEOPDPlaceRequest(PlaceDataExtras) addRequestedComponents:] : 272 -> 268
~ -[GEOPDPlaceRequest _readPlaceRequestParameters] : 228 -> 200
~ -[_GEOURLStateCapture init] : 132 -> 160
~ __dispatcherSupportsService : 316 -> 300
~ _GEOMapItemHandleShouldStoreRequestData : 24 -> 40
~ -[GEOPDPlaceRequest clientMetadata] : 72 -> 76
~ -[GEOPDClientMetadata deviceExtendedLocation] : 96 -> 80
~ -[GEOPDClientMetadata _readDeviceExtendedLocation] : 216 -> 232
~ -[GEOPDClientMetadata deviceHistoricalLocations] : 88 -> 72
~ -[GEOPDClientMetadata _readDeviceHistoricalLocations] : 220 -> 204
~ -[GEOPDClientMetadata hasDeviceExtendedLocation] : 60 -> 76
~ -[GEOPDClientMetadata clearSensitiveFields:] : 28 -> 40
~ -[GEOPDPlaceRequest hasPlaceRequestParameters] : 56 -> 60
~ -[GEOPlaceRequestMessage setTimeout:] : 36 -> 32
~ ___134-[GEOPlaceCardRequester performPlaceDataRequest:traits:cachePolicy:timeout:auditToken:throttleToken:networkActivity:requesterHandler:]_block_invoke : 100 -> 104
~ -[GEOTraitsTransitScheduleTimeRange writeTo:] : 176 -> 172
~ -[GEOPDPlaceRequest readAll:] : 220 -> 208
~ -[GEOPDAnalyticMetadata readAll:] : 220 -> 204
~ -[GEOGeoServiceTag writeTo:] : 180 -> 176
~ -[GEOPDStorefrontPresentationFilter writeTo:] : 8 -> 12
~ sub_186cce290 -> sub_186cca314 : 508 -> 504
~ -[GEOXPCRequest traits] : 24 -> 28
~ -[GEOPlaceRequestMessage timeout] : 24 -> 20
~ -[GEOPlaceDataRequester startWithRequest:traits:timeout:auditToken:throttleToken:completionHandler:] : 720 -> 724
~ -[GEOPDClientMetadata init] : 112 -> 96
~ -[GEOPDClientMetadata setAbClientMetadata:] : 112 -> 128
~ _GEOGreenTeaGetLog : 20 -> 48
~ -[GEOPlaceDataRequestConfig initWithTimeout:request:traits:] : 816 -> 788
~ -[GEOServiceRequester _operationClassForTraits:requestKind:forCohort:config:error:] : 2352 -> 2348
~ -[GEOPlaceDataRequestConfig supportsOffline] : 28 -> 32
~ -[GEONetworkServiceRequesterOperation initWithRequest:traits:auditToken:config:throttleToken:options:willSendRequestHandler:validationHandler:completionHandler:] : 596 -> 592
~ -[GEOPlaceDataRequestConfig timeout] : 20 -> 24
~ -[GEOServiceRequester _keyForRequest:] : 60 -> 56
~ -[GEOPDPlaceRequest hash] : 512 -> 500
~ sub_186ce05f8 -> sub_186cdc66c : 88 -> 104
~ _GEOGeoServiceTagReadAllFrom : 904 -> 920
~ __GEOPDAnalyticMetadataCallReadAllRecursiveWithoutSynchronized : 308 -> 292
~ -[GEOGeoServiceTag readAll:] : 16 -> 12
~ __GEOPDPlaceRequestCallReadAllRecursiveWithoutSynchronized : 592 -> 564
~ _GEOLocalizationCapabilitiesReadAllFrom : 1488 -> 1504
~ __GEOPDClientMetadataCallReadAllRecursiveWithoutSynchronized : 372 -> 356
~ __GEOABSecondPartyPlaceRequestClientMetaDataCallReadAllRecursiveWithoutSynchronized : 432 -> 448
~ -[GEOPDClientMetadata hash] : 1140 -> 1156
~ -[GEOABSecondPartyPlaceRequestClientMetaData hash] : 108 -> 104
~ -[GEOPDABClientDatasetMetadata hash] : 136 -> 140
~ +[GEOProtobufSession sharedDelegateQueue] : 128 -> 124
~ -[GEOPlaceDataRequestConfig dataRequestKindForRequest:traits:] : 268 -> 240
~ -[GEOMapServiceTraits requestPriority] : 116 -> 112
~ -[GEOPlaceDataRequestConfig urlType] : 32 -> 36
~ -[GEOPurgableFile initWithURL:changedNotification:purgeDelay:protocolBufferType:] : 8 -> 4
~ -[GEOPDPlaceCollectionFilter writeTo:] : 376 -> 348
~ -[GEOMapServiceTraits requestMode] : 128 -> 124
~ -[GEOPDABClientDatasetMetadata readAll:] : 16 -> 4
~ -[GEOPDAnalyticMetadata hash] : 860 -> 876
~ -[_GEOURLManifestListenerCallbackWithQueue .cxx_destruct] : 108 -> 104
~ ___46-[GEODataURLSessionList urlSessionForRequest:]_block_invoke : 236 -> 208
~ _GEOURLSupportsMPTCP : 64 -> 60
~ -[GEOPlaceDataRequestConfig multipathServiceType] : 44 -> 16
~ _GEOURLMultipathAlternatePort : 112 -> 92
~ -[GEODataRequest(GEOProtobufSession) initWithKind:protobufRequest:URL:additionalHTTPHeaders:auditToken:timeoutInterval:traits:requestCounterTicket:multipathServiceType:multipathAlternatePort:throttleToken:options:] : 736 -> 720
~ _GEODataURLSessionGetIdentifierFromSession : 236 -> 240
~ -[GEOABSecondPartyPlaceRequestClientMetaData writeTo:] : 736 -> 732
~ -[GEOPDABClientDatasetMetadata writeTo:] : 180 -> 184
~ _GEOAuthProxyEnabledForActiveTileGroup : 84 -> 64
~ __protobufHTTPHeaders : 692 -> 676
~ -[GEODataRequest initWithKind:URL:auditToken:timeoutInterval:additionalHTTPHeaders:bodyData:userAgent:entityTag:cachedData:requestCounterTicket:multipathServiceType:multipathAlternatePort:throttleToken:options:] : 56 -> 60
~ -[GEONetworkServiceRequesterOperation _fullURL] : 424 -> 420
~ -[GEOURLInfoSet _readDispatcherURL] : 228 -> 232
~ -[GEOExperimentConfiguration updateURLComponents:forRequestKind:] : 768 -> 764
~ -[GEOURLInfo alternativeMultipathTCPPort] : 28 -> 44
~ _writeARPCPreamble : 616 -> 632
~ -[GEOPDPlaceRequest requestTypeCode] : 8 -> 12
~ _GeoServicesConfig_ProtobufSessionAdditionalHTTPHeaders_Metadata_block_invoke_72 : 24 -> 20
~ -[GEODataRequest setCachedData:] : 24 -> 28
~ +[GEOProtobufSession sharedProtobufSession] : 188 -> 184
~ -[GEOPDPlaceRequest responseClass] : 28 -> 32
~ -[GEOProtobufSession taskWithRequest:requestTypeCode:responseClass:delegate:delegateQueue:] : 640 -> 636
~ -[GEODataRequest throttleToken] : 16 -> 20
~ _GEOGetDataSessionProtobufLog : 120 -> 116
~ -[GEODataRequest publicLogDescription] : 376 -> 380
~ -[GEOApplicationAuditToken publicLogDescription] : 216 -> 212
~ __GEORequestResponseLogRequest : 364 -> 368
~ -[GEOProtobufSessionTask dataTask] : 32 -> 12
~ -[GEOThrottlerRequester allowRequest:forClient:throttlerToken:error:] : 272 -> 256
~ -[GEODataURLSessionTask start] : 224 -> 228
~ -[_GEOURLManifestListenerCallbackWithQueue performHandler:] : 308 -> 304
~ -[NSURLSessionConfiguration(GEODataRequest) geo_isCompatibleWithRequest:] : 828 -> 832
~ -[GEOApplicationAuditToken _secondaryIdentifier] : 12 -> 8
~ -[NSURLSessionConfiguration(GEODataRequest) geo_configureWithRequest:] : 364 -> 368
~ -[NSURLSessionConfiguration(GEOApplicationAuditToken) geo_setApplicationAttribution:] : 300 -> 296
~ -[GEODataURLSessionTask setCachedData:] : 32 -> 36
~ ___44-[GEONetworkServiceRequesterOperation start]_block_invoke : 1288 -> 1284
~ -[GEODataURLSessionTaskIdentifier hash] : 8 -> 12
~ _GEOGloriaEnumerateQuadKeysWithinRadiusFromCoordinate : 1468 -> 1464
~ -[GEOTerritoryDataTerritoryInfo .cxx_destruct] : 144 -> 148
~ -[GEOGloriaTessellationOptions dealloc] : 104 -> 100
~ __ZNSt3__120__shared_ptr_pointerIPN3geo8GloriaDB7QuadKeyENS_10shared_ptrIN6gloria15RecordAttributeEE27__shared_ptr_default_deleteIS7_S3_EENS_9allocatorIS3_EEE21__on_zero_shared_weakEv : 20 -> 24
~ -[GEOGeographicMetadataResourceFetcher .cxx_destruct] : 108 -> 104
~ -[GEONetworkDefaults serverProxy:networkDefaultsDidChange:] : 256 -> 260
~ _GEOConfigSetString : 20 -> 16
~ -[GEODownloadMetadata _readUrl] : 228 -> 200
~ __getUserDefaultStringKeysForStateCapture : 36 -> 32
~ __getConfigStoreStringKeysForStateCapture : 12 -> 16
~ _GeoServicesConfig_VoltaireDirectionsURL_Metadata_block_invoke_8 : 16 -> 12
~ -[GEOURLInfoSet _readEtaURL] : 208 -> 212
~ _GeoServicesConfig_SearchAttributionManifestURL_Metadata_block_invoke_11 : 28 -> 24
~ -[GEOURLInfoSet _readProblemSubmissionURL] : 228 -> 232
~ _GeoServicesConfig_VoltaireBatchReverseGeocoderURL_Metadata_block_invoke_15 : 16 -> 12
~ -[GEOURLInfoSet addressCorrectionUpdateURL] : 84 -> 88
~ _GeoServicesConfig_URLAddressCorrectionInitURL_Metadata_block_invoke_17 : 16 -> 12
~ -[GEOURLInfoSet _readAddressCorrectionInitURL] : 208 -> 212
~ ___GEODefaultsKeyStringForConfigKey_block_invoke : 88 -> 84
~ -[GEOURLInfo useAuthProxy] : 56 -> 60
~ _GeoServicesConfig_VoltaireETAURL_Metadata_block_invoke_9 : 24 -> 20
~ -[GEOURLInfoSet _readSearchAttributionManifestURL] : 220 -> 224
~ _GeoServicesConfig_VoltaireProblemSubmissionURL_Metadata_block_invoke_12 : 12 -> 8
~ -[GEOURLInfoSet problemSubmissionURL] : 92 -> 96
~ _GeoServicesConfig_VoltaireProblemStatusURL_Metadata_block_invoke_13 : 20 -> 16
~ -[GEOURLInfoSet _readProblemStatusURL] : 220 -> 224
~ _GeoServicesConfig_LocalizedCategoriesURL_Metadata_block_invoke_44 : 32 -> 28
~ -[GEOURLInfoSet _readProblemCategoriesURL] : 224 -> 228
~ _GeoServicesConfig_CurrentCountryURL_Metadata_block_invoke_21 : 8 -> 36
~ -[GEOURLInfoSet _readBatchReverseGeocoderURL] : 232 -> 204
~ _GeoServicesConfig_URLSimpleETAURL_Metadata_block_invoke_16 : 32 -> 28
~ -[GEOURLInfoSet simpleETAURL] : 80 -> 84
~ _GeoServicesConfig_URLAddressCorrectionUpdateURL_Metadata_block_invoke_18 : 36 -> 32
~ -[GEOURLInfoSet _readAddressCorrectionUpdateURL] : 204 -> 208
~ _GeoServicesConfig_URLReverseGeocoderVersionFileURL_Metadata_block_invoke_20 : 12 -> 8
~ -[GEOURLInfoSet _readReverseGeocoderVersionsURL] : 204 -> 208
~ _GeoServicesConfig_VoltaireAnnouncementsURL_Metadata_block_invoke_24 : 16 -> 12
~ -[GEOURLInfoSet _readAnnouncementsURL] : 216 -> 220
~ _GeoServicesConfig_ProblemOptInURL_Metadata_block_invoke_26 : 32 -> 28
~ -[GEOURLInfoSet _readProblemOptInURL] : 224 -> 228
~ _GeoServicesConfig_ExperimentsURL_Metadata_block_invoke_27 : 12 -> 8
~ -[GEOURLInfoSet _readAbExperimentURL] : 212 -> 216
~ _GeoServicesConfig_BusinessPortalBaseURL_Metadata_block_invoke_28 : 20 -> 16
~ -[GEOURLInfoSet _readBusinessPortalBaseURL] : 204 -> 208
~ _GeoServicesConfig_VoltaireLogMessageUsageURL_Metadata_block_invoke_29 : 28 -> 24
~ -[GEOURLInfoSet _readLogMessageUsageURL] : 228 -> 232
~ _GeoServicesConfig_SpatialLookupURL_Metadata_block_invoke_30 : 36 -> 32
~ -[GEOURLInfoSet _readRealtimeTrafficProbeURL] : 208 -> 212
~ _GeoServicesConfig_BatchTrafficProbeURL_Metadata_block_invoke_32 : 24 -> 20
~ -[GEOURLInfoSet _readBatchTrafficProbeURL] : 220 -> 224
~ _GeoServicesConfig_RealtimeTrafficProbeURL_Metadata_block_invoke_31 : 16 -> 12
~ -[GEOURLInfoSet realtimeTrafficProbeURL] : 96 -> 100
~ _GeoServicesConfig_LogMessageUsageV3URL_Metadata_block_invoke_33 : 20 -> 16
~ -[GEONetworkObserver _networkPathUpdated:] : 1052 -> 1068
~ -[GEOMapSubscriptionsFetchRequest isValid] : 16 -> 36
~ -[GEOMapDataSubscriptionManager fetchLastUpdatedDateForPairedDeviceOfflineSubscriptionsWithQueue:completionHandler:] : 8 -> 20
~ -[GEOMapSubscriptionFetchLastUpdatedDateRequest initWithTraits:auditToken:throttleToken:] : 32 -> 52
~ ___54-[GEOMapDataSubscriptionRemoteSyncManager _connection]_block_invoke : 264 -> 276
~ -[GEOMapSubscriptionFetchLastUpdatedDateRequest isValid] : 24 -> 8
~ ___40-[GEONetworkObserver isNetworkReachable]_block_invoke : 96 -> 68
~ -[GEOMapDataSubscriptionManager _calculateTotalSizeOfOfflineSubscriptionsWithCallbackQueue:completionHandler:] : 36 -> 16
~ +[GEOMapSubscriptionTotalOfflineDataSizeRequest replyClass] : 20 -> 40
~ -[GEOMapDataSubscriptionRemoteSyncManager fetchLastUpdatedDateForPairedDeviceOfflineSubscriptionsWithQueue:completionHandler:] : 256 -> 268
~ -[GEOMapSubscriptionFetchLastUpdatedDateRequest setOnPairedDevice:] : 40 -> 28
~ -[GEOMapDataSubscriptionRemoteSyncManager _connection] : 152 -> 164
~ -[GEOMapSubscriptionFetchLastUpdatedDateRequest encodeToXPCDictionary:] : 144 -> 132
~ -[GEOMapDataSubscriptionManager fetchLastUpdatedDateForOfflineSubscriptionsWithQueue:completionHandler:] : 16 -> 12
~ ___58-[GEOMapDataSubscriptionRemoteDownloadManager _connection]_block_invoke : 276 -> 280
~ -[GEOMapDataSubscriptionLocalPersistence fetchExpiredSubscriptionsWithIdentifiers:callbackQueue:completionHandler:] : 28 -> 24
~ ___FetchExpiredSubscriptions_block_invoke : 480 -> 464
~ -[GEOMapSubscriptionFetchLastUpdatedDateRequest onPairedDevice] : 16 -> 36
~ -[GEOMapDataSubscriptionLocalSyncManager fetchLastUpdatedDateForPairedDeviceOfflineSubscriptionsWithQueue:completionHandler:] : 192 -> 204
~ -[GEOMapSubscriptionTotalOfflineDataSizeRequest initWithXPCDictionary:error:] : 112 -> 100
~ -[GEOMapDataSubscriptionLocalPersistence calculateTotalSizeOfOfflineSubscriptionsWithCallbackQueue:completionHandler:] : 36 -> 32
~ -[GEOTileDB calculateSizeOfAllOfflineDataWithCallbackQueue:callback:] : 296 -> 300
~ ___125-[GEOMapDataSubscriptionLocalSyncManager fetchLastUpdatedDateForPairedDeviceOfflineSubscriptionsWithQueue:completionHandler:]_block_invoke_2 : 36 -> 48
~ -[GEOMapSubscriptionFetchLastUpdatedDateReply encodeToXPCDictionary:] : 144 -> 132
~ -[GEOAnalyticsPipelineStateData setMapSettingsLocationPrecisionType:] : 60 -> 56
~ ___117-[GEOMapDataSubscriptionLocalDownloadManager fetchLastUpdatedDateForOfflineSubscriptionsWithQueue:completionHandler:]_block_invoke : 104 -> 108
~ ___42-[GEOUserSession _mapsShortSessionValues:]_block_invoke : 28 -> 24
~ -[GEOAPSessionData sessionCreateHour] : 16 -> 20
~ -[GEOMapItemStorage readFrom:] : 20 -> 16
~ ___69-[GEOTileDB calculateSizeOfAllOfflineDataWithCallbackQueue:callback:]_block_invoke_2 : 52 -> 36
~ -[GEOMapSubscriptionTotalOfflineDataSizeReply encodeToXPCDictionary:] : 148 -> 132
~ ___25-[GEOXPCConnection close]_block_invoke : 104 -> 92
~ -[GEOPDAnalyticMetadata setRequestTime:] : 112 -> 96
~ -[GEOLocalTime hash] : 264 -> 276
~ -[GEOPeer .cxx_destruct] : 188 -> 176
~ -[GEOApplicationAuditToken .cxx_destruct] : 156 -> 152
~ -[GEOOfflineService _mapViewToUse] : 680 -> 684
~ _GEOConfigSetInteger : 132 -> 128
~ -[GEOConfigStorageFallbackWriter setConfigValue:forKey:options:synchronous:] : 24 -> 28
~ _MapsFeature_IsEnabled_Alberta : 20 -> 16
~ -[GEOActiveTileGroup(GEOResourceManifestManagerAdditions) hashForPurpose:] : 740 -> 744
~ -[NSArray(GEOFunctionalExtras) _geo_compactMap:] : 412 -> 408
~ ___74-[GEOActiveTileGroup(GEOResourceManifestManagerAdditions) hashForPurpose:]_block_invoke_2 : 8 -> 12
~ ___42-[NSData(GEOHashUtilities) _geo_hexString]_block_invoke : 136 -> 132
~ -[GEOActiveTileGroup _readExplicitResources] : 204 -> 208
~ -[GEOResourceRequester fetchResources:force:manifestConfiguration:auditToken:queue:handler:] : 236 -> 232
~ -[GEOResourceFilter writeTo:] : 464 -> 468
~ -[GEOAnalyticsPipelineStateData setMapFeaturePersonalCollectionsCount:] : 72 -> 68
~ -[GEOURLOptions setUserTrackingMode:] : 44 -> 48
~ -[GEOSearchCategoryStorage .cxx_destruct] : 132 -> 128
~ ___42-[GEONetworkObserver _networkPathUpdated:]_block_invoke : 128 -> 112
~ -[GEOMapSubscriptionFetchLastUpdatedDateReply initWithXPCDictionary:error:] : 172 -> 160
~ ___126-[GEOMapDataSubscriptionRemoteSyncManager fetchLastUpdatedDateForPairedDeviceOfflineSubscriptionsWithQueue:completionHandler:]_block_invoke : 224 -> 204
~ -[GEOMapSubscriptionFetchLastUpdatedDateReply timestamp] : 32 -> 16
~ _GEOGetETagFromExtendedAttributes : 240 -> 244
~ -[GEOReportedProgress becomeCurrentWithPendingUnitCount:] : 12 -> 8
~ -[GEOResource alternateResourceURLIndex] : 16 -> 20
~ _GEOURLAuthenticationGenerateURLFromComponents : 1672 -> 1668
~ ___54-[GEOCountryConfiguration urlAuthenticationTimeToLive]_block_invoke : 216 -> 220
~ _GeoServicesConfig_ResourceRequestAdditionalHTTPHeaders_Metadata_block_invoke_73 : 40 -> 36
~ -[GEOURLCamera writeTo:] : 260 -> 264
~ -[GEOReportedProgress resignCurrent] : 36 -> 32
~ ___119-[GEOMapDataSubscriptionRemotePersistence calculateTotalSizeOfOfflineSubscriptionsWithCallbackQueue:completionHandler:]_block_invoke : 136 -> 108
~ -[GEOAnalyticsPipelineStateData _readMapLaunchSourceAppId] : 228 -> 208
~ -[GEOLogMsgState _readExperiments] : 232 -> 220
~ -[GEOABSecondPartyPlaceRequestClientMetaData init] : 124 -> 120
~ _GEOPDABClientDatasetMetadataReadAllFrom : 1168 -> 1152
~ -[GEOLogMsgStateExperiments _readDatasetAbStatus] : 220 -> 204
~ -[GEOPDDatasetABStatus setDatasetId:] : 64 -> 48
~ -[GEOLogMsgStateDeviceConnection setDeviceCountryCode:] : 96 -> 112
~ -[GEONetworkObserver _isConnectionType:] : 212 -> 196
~ -[GEOLogMsgStateDeviceLocale setDeviceOutputLocale:] : 108 -> 96
~ -[GEOAnalyticsPipelineStateData _readDeviceOutputLocale] : 204 -> 216
~ -[GEOLogMsgStateDeviceLocale readAll:] : 192 -> 212
~ -[GEOAnalyticsPipelineStateData mapSettingsLocationPrecisionType] : 120 -> 132
~ -[GEOLogMsgStateMapSettings setLocationType:] : 56 -> 44
~ -[GEOAnalyticsPipelineStateData hasMapSettingsIsHandsFreeProfileEnabled] : 44 -> 24
~ -[GEOLogMsgState setMapUi:] : 100 -> 120
~ -[GEOAnalyticsPipelineStateData hasLandscape] : 44 -> 24
~ -[GEOLogMsgStateMapUI .cxx_destruct] : 92 -> 112
~ -[GEOAnalyticsPipelineStateData mapUiShownAqiShown] : 132 -> 112
~ -[GEOLogMsgStateMapUIShown setIsAirQualityShown:] : 48 -> 36
~ -[GEOAnalyticsPipelineStateData hasLookAroundEntryIconShown] : 52 -> 32
~ -[GEOLogMsgState setMapView:] : 112 -> 100
~ -[GEOAnalyticsPipelineStateData mapViewMapType] : 104 -> 116
~ -[GEOLogMsgState _readMapView] : 208 -> 228
~ -[GEOAnalyticsPipelineStateData hasMapViewStyleZoomLevel] : 32 -> 44
~ -[GEOLogMsgStateMapView setIsAdvancedMap:] : 40 -> 60
~ -[GEOAnalyticsPipelineStateData mapViewIsGlobeProjection] : 36 -> 16
~ -[GEOLogMsgStateMapView setIsGlobeProjection:] : 40 -> 60
~ -[GEOAnalyticsPipelineStateData _readMapViewMapRegion] : 208 -> 220
~ -[GEOLogMsgStateMapView setMapRegion:] : 96 -> 84
~ -[GEOAnalyticsPipelineStateData mapViewPitch] : 20 -> 32
~ -[GEOLogMsgStateMapView .cxx_destruct] : 108 -> 92
~ -[GEOURLInfoSet _readBackgroundDispatcherURL] : 208 -> 212
~ _GeoServicesConfig_BluePOIURL_Metadata_block_invoke_40 : 24 -> 20
~ -[GEOURLInfoSet _readBluePOIDispatcherURL] : 232 -> 204
~ _GeoServicesConfig_BackgroundRevGeoURL_Metadata_block_invoke_41 : 32 -> 28
~ -[GEOURLInfoSet backgroundRevGeoURL] : 72 -> 76
~ _GeoServicesConfig_ImageServiceURL_Metadata_block_invoke_42 : 28 -> 24
~ -[GEOURLInfoSet _readFeedbackLookupURL] : 220 -> 224
~ _GeoServicesConfig_AnalyticsShortSessionURL_Metadata_block_invoke_36 : 8 -> 36
~ -[GEOURLInfoSet _readAnalyticsShortSessionURL] : 224 -> 228
~ _GeoServicesConfig_WebModuleBaseURL_Metadata_block_invoke_55 : 8 -> 36
~ -[GEOURLInfoSet authenticatedClientFeatureFlagURL] : 100 -> 72
~ _GeoServicesConfig_EnrichmentSubmissionURL_Metadata_block_invoke_58 : 8 -> 36
~ -[GEOURLInfoSet _readUgcLogDiscardURL] : 208 -> 212
~ _GeoServicesConfig_PressureDataURL_Metadata_block_invoke_22 : 12 -> 8
~ -[GEOURLInfoSet poiBusynessActivityCollectionURL] : 92 -> 96
~ _GeoServicesConfig_RAPWebModuleBaseURL_Metadata_block_invoke_45 : 20 -> 16
~ -[GEOURLInfoSet offlineDataBatchListURL] : 96 -> 100
~ _GeoOfflineConfig_DownloadURL_Metadata_block_invoke_4 : 24 -> 20
~ -[GEOURLInfoSet _readBcxDispatcherURL] : 212 -> 216
~ _GeoServicesConfig_MapsURLShortenerURL_Metadata_block_invoke_65 : 16 -> 12
~ -[_GEONetworkDefaultsLocalProxy captureStatePlistWithHints:] : 204 -> 220
~ sub_186d00fa4 -> sub_186cfceb4 : 100 -> 84
~ -[_GEOMirroredProgress dealloc] : 76 -> 80
~ -[GEOResourceManifestDownloadTask initWithURL:eTag:] : 212 -> 208
~ -[GEOActiveTileGroup _readEnvironment] : 216 -> 232
~ -[GEOPeer debugIdentifier] : 28 -> 16
~ -[GEOOfflineDataConfiguration captureStatePlistWithHints:] : 1348 -> 1344
~ ___153-[GEOTileLoader loadKey:additionalInfo:priority:forClient:auditToken:options:cacheInfo:reason:qos:signpostID:createTime:callbackQ:beginNetwork:callback:]_block_invoke_2 : 2436 -> 2408
~ -[GEOTilePool tileForKey:] : 544 -> 540
~ ___35-[_GEOConfigDBOperationQueue init:]_block_invoke : 92 -> 64
~ ___60-[GEOConfigStorageDirectReadWrite _scheduleWriteDirectStore]_block_invoke : 1008 -> 1004
~ -[GEOResources tileGroupAtIndex:] : 80 -> 84
~ -[GEOResources(Extras) preferredDataSetForClientDatasetMetadata:] : 444 -> 440
~ -[GEOActiveTileGroup _readActiveNames] : 200 -> 204
~ -[GEOResources(GEOURLExtras) preferedURLSetFor:] : 548 -> 544
~ ___GEOGetNetworkStatusLog_block_invoke : 72 -> 76
~ -[GEOMapDataSubscriptionManager fetchAllExpiredSubscriptionsWithCallbackQueue:completionHandler:] : 44 -> 24
~ -[GEOMapSubscriptionTotalOfflineDataSizeRequest encodeToXPCDictionary:] : 64 -> 80
~ -[GEOResource hasUpdateMethod] : 36 -> 40
~ _GEOURLAuthenticationGenerateURL : 140 -> 136
~ ___48-[GEOResourceManifestServerLocalProxy authToken]_block_invoke : 92 -> 96
~ -[GEOReportedProgress setUserInfoObject:forKey:] : 28 -> 24
~ -[GEOURLOptions readAll:] : 208 -> 224
~ -[GEOMapSubscriptionTotalOfflineDataSizeReply sizeInBytes] : 40 -> 28
~ -[GEOAnalyticsPipelineStateData carPlayInfo] : 100 -> 80
~ -[GEOLogMsgStateExperiments init] : 96 -> 116
~ _GEOABSecondPartyPlaceRequestClientMetaDataReadSpecified : 1484 -> 1480
~ -[GEOPDDatasetABStatus copyWithZone:] : 168 -> 152
~ -[GEOLogMsgState setDeviceSettings:] : 128 -> 112
~ ___40-[GEONetworkObserver _isConnectionType:]_block_invoke : 92 -> 76
~ -[GEOLogMsgStateDeviceLocale .cxx_destruct] : 148 -> 168
~ -[GEOAnalyticsPipelineStateData hasMapSettingsDirectionsWakeDevice] : 44 -> 24
~ -[GEOLogMsgStateMapUIShown setActiveNavMode:] : 56 -> 44
~ -[GEOAnalyticsPipelineStateData lookAroundEntryIconShown] : 28 -> 40
~ -[GEOLogMsgStateMapUIShown .cxx_destruct] : 28 -> 48
~ -[GEOAnalyticsPipelineStateData hasMapViewMapType] : 48 -> 28
~ -[GEOLogMsgStateMapView setMapType:] : 44 -> 64
~ -[GEOAnalyticsPipelineStateData mapViewStyleZoomLevel] : 20 -> 32
~ -[GEOLogMsgStateMapView setStyleZoomLevel:] : 40 -> 60
~ _GeoServicesConfig_ProactiveRoutingURL_Metadata_block_invoke_38 : 16 -> 12
~ -[GEOActiveTileGroup hasUniqueIdentifier] : 84 -> 68
~ -[GEOMapSubscriptionsFetchRequest encodeToXPCDictionary:] : 440 -> 424
~ -[GEOPDPlaceRequest analyticMetadata] : 80 -> 84
~ _GeoServicesConfig_BackgroundDispatcherURL_Metadata_block_invoke_39 : 12 -> 8
~ -[GEOResources _readTileSets] : 204 -> 220
~ _GEOTileSetReadAllFrom : 420 -> 436
~ -[_GEOConfigDBUpdateOperation .cxx_destruct] : 88 -> 92
~ -[GEOServiceURLsActiveTileGroupMigrator needsMigrationForNewTileGroup:inResourceManifest:oldTileGroup:dataSet:] : 160 -> 156
~ -[GEONetworkObserver isNetworkReachable] : 188 -> 204
~ -[GEOMapSubscriptionsFetchRequest setIdentifiersFilter:] : 80 -> 96
~ -[GEOMapDataSubscriptionRemotePersistence calculateTotalSizeOfOfflineSubscriptionsWithCallbackQueue:completionHandler:] : 232 -> 216
~ -[GEOMapSubscriptionTotalOfflineDataSizeRequest reply] : 20 -> 36
~ -[GEOPDPlaceRequest _readAnalyticMetadata] : 216 -> 200
~ -[GEOLogMsgStateExperiments setDatasetAbStatus:] : 124 -> 108
~ -[GEOPDDatasetABStatus .cxx_destruct] : 28 -> 44
~ -[GEOLogMsgState deviceLocale] : 80 -> 100
~ -[GEOAnalyticsPipelineStateData venueExperienceShown] : 132 -> 112
~ -[GEOLogMsgStateMapUIShown copyWithZone:] : 324 -> 312
~ -[GEOAnalyticsPipelineStateData mapViewZoomLevel] : 36 -> 16
~ -[GEOLogMsgStateMapView setZoomLevel:] : 64 -> 52
~ -[GEOAnalyticsPipelineStateData setMapFeatureElectronicVehicleCount:] : 64 -> 76
~ -[GEOMapSubscriptionTotalOfflineDataSizeRequest initWithTraits:auditToken:throttleToken:] : 52 -> 36
~ ___116-[GEOMapDataSubscriptionRemotePersistence fetchExpiredSubscriptionsWithIdentifiers:callbackQueue:completionHandler:]_block_invoke : 156 -> 140
~ -[GEOLogMsgState setMapUiShown:] : 120 -> 108
~ -[GEOAnalyticsPipelineStateData hasMapSettingsSpeedLimitEnabled] : 32 -> 44
~ -[GEOLogMsgState _readMarket] : 212 -> 228
~ -[GEOPDEntity init] : 104 -> 108
~ _GEOMapItemStorageReadAllFrom : 424 -> 436
~ -[GEOLogMsgState setMapViewLocation:] : 112 -> 100
~ -[GEOAnalyticsPipelineStateData hasMapsServerMetadata] : 80 -> 60
~ -[GEOLogMsgStateOffline .cxx_destruct] : 28 -> 48
~ -[GEOAnalyticsPipelineStateData hasMapViewLocationIsTourist] : 40 -> 52
~ -[GEOLogMsgStateMapViewLocation copyWithZone:] : 220 -> 208
~ -[GEOAnalyticsPipelineStateData _readMapsServerMetadataSuggestionEntryDisplayeds] : 204 -> 216
~ -[GEOLogMsgStateMarket setMarket:] : 84 -> 72
~ ___43-[GEOUserSession shortAndNavSessionValues:]_block_invoke : 168 -> 148
~ -[GEOLogMsgStateExperiments writeTo:] : 444 -> 460
~ -[GEOPDDatasetABStatus writeTo:] : 132 -> 148
~ -[GEOLogMsgStateUser setMapsUseStartDate:] : 48 -> 64
~ -[GEOURLInfoSet _readJunctionImageServiceURL] : 228 -> 232
~ _GeoServicesConfig_MuninBaseURL_Metadata_block_invoke_50 : 36 -> 32
~ -[GEOURLInfoSet _readMuninBaseURL] : 204 -> 208
~ _GeoServicesConfig_WiFiQualityURL_Metadata_block_invoke_52 : 12 -> 8
~ -[GEOURLInfoSet _readWifiQualityURL] : 212 -> 216
~ _GeoServicesConfig_FeedbackSubmissionURL_Metadata_block_invoke_53 : 28 -> 24
~ -[GEOURLInfoSet _readFeedbackSubmissionURL] : 228 -> 232
~ _GeoServicesConfig_AnalyticsLongSessionURL_Metadata_block_invoke_35 : 24 -> 20
~ -[GEOURLInfoSet _readWebModuleBaseURL] : 216 -> 220
~ _GeoServicesConfig_WiFiTileURL_Metadata_block_invoke_56 : 28 -> 24
~ -[GEOURLInfoSet _readWifiQualityTileURL] : 204 -> 208
~ _GeoServicesConfig_TokenAuthenticationURL_Metadata_block_invoke_57 : 20 -> 16
~ -[GEOURLInfoSet _readEnrichmentSubmissionURL] : 208 -> 212
~ _GeoServicesConfig_BatchRevGeoPlaceRequestURL_Metadata_block_invoke_59 : 20 -> 16
~ -[GEOURLInfoSet _readPressureProbeDataURL] : 212 -> 216
~ _GeoServicesConfig_BusynessDataURL_Metadata_block_invoke_23 : 28 -> 24
~ -[GEOURLInfoSet _readRapWebBundleURL] : 204 -> 208
~ _GeoOfflineConfig_BatchListURL_Metadata_block_invoke_2 : 16 -> 12
~ -[GEOURLInfoSet _readOfflineDataDownloadBaseURL] : 228 -> 232
~ _GeoServicesConfig_BCXDispatcherURL_Metadata_block_invoke_61 : 36 -> 32
~ -[GEOLogMessageCollectionRequest requestTypeCode] : 20 -> 36
~ _GEOProtocolBufferRequestHeader : 180 -> 164
~ _GEOTileKeyHash : 92 -> 76
~ ___18-[GEODaemon peers]_block_invoke : 96 -> 80
~ sub_186d25bf4 -> sub_186d21a94 : 64 -> 68
~ -[GEOResources(Extras) isValid] : 128 -> 124
~ -[GEOResources tileGroups] : 76 -> 80
~ _GeoServicesConfig_CoreLocationKACURL_Metadata_block_invoke_64 : 16 -> 12
~ -[GEOTileGroup identifier] : 24 -> 28
~ ___68-[GEOResourceManifestDownloadTask startWithQueue:completionHandler:]_block_invoke_2 : 472 -> 468
~ -[GEOTileLoader _notifyObserversOfSuccess:sizeInBytes:source:options:] : 412 -> 428
~ __ZN3gcl5tmesh11DecoderImpl18decompressGeometryEiPNS_7Vector3IiEE : 1300 -> 1288
~ +[GEOAltitudeManifest sharedManager] : 128 -> 108
~ __ZNSt3__16vectorI31GeoCodecsLocalizationTableEntryN3geo17allocator_adapterIS1_NS2_5codec15zone_mallocatorEEEE8__appendEm : 388 -> 404
~ -[_GEOTileDBUpdateAccessTimeOperation initWithTileKey:timestamp:] : 140 -> 112
~ -[_GEOSimpleTileRequesterOperation setTask:] : 88 -> 68
~ __ZN3geo5codec23_readCompressedPolygonsEP8VMP4TileRKNSt3__110shared_ptrINS0_10VectorTileEEE : 9124 -> 9140
~ -[GEOTileLoader _loadedTileForLocalKey:preliminary:quickly:tileDecoder:data:disburseTile:] : 1304 -> 1288
~ __ZN3gcl17ArithmeticDecoder21decodeSignedExpGolombEiRNS_17ArithmeticContextES2_ : 292 -> 308
~ ___dispatch_work_block_invoke : 100 -> 104
~ ___61-[GEOTileRequestBalancer _startOperationsWithAvailableCount:]_block_invoke : 384 -> 396
~ __ZNSt3__120__shared_ptr_emplaceIN3geo5codec10VectorTileENS1_17allocator_adapterIS3_NS2_15zone_mallocatorEEEE21__on_zero_shared_weakEv : 220 -> 204
~ -[GEOTileKeyMap setObject:forKey:] : 660 -> 664
~ +[GEOApplicationAuditToken(TileLoader) compositeTokenForTokens:] : 484 -> 480
~ -[GEOTileDB devicePostureRegion] : 136 -> 140
~ -[GEORegionalResourcesTileRequester start] : 1628 -> 1624
~ -[GEOTileRequest keyList] : 36 -> 8
~ ___42-[GEORegionalResourcesTileRequester start]_block_invoke_2 : 40 -> 36
~ -[GEORegionalResourceTileData init] : 108 -> 112
~ -[GEOResource(GeoServicesExtras) _geo_isRelevantForScales:scenarios:] : 504 -> 532
~ __ZNSt3__110__list_impIU8__strongP8NSStringNS_9allocatorIS3_EEE5clearEv : 132 -> 136
~ ___118-[_GEORegionalResourcesTileLoader loadResourcesForTileKey:manifestConfiguration:auditToken:signpostID:finished:error:]_block_invoke : 260 -> 256
~ -[GEOTileData .cxx_destruct] : 92 -> 96
~ ___42-[GEORegionalResourcesTileRequester start]_block_invoke_4 : 348 -> 344
~ -[GEOTileLoader _tileDecoderForTileKey:quickly:] : 572 -> 588
~ __ZNK25FeatureStyleAttributesSet29FeatureStyleAttributesCompareclERKNSt3__110shared_ptrIK22FeatureStyleAttributesEES7_ : 360 -> 348
~ -[GEOAltitudeManifest parseManifest:] : 208 -> 188
~ __ZN3gcl5tmesh11DecoderImpl18parseAttributeInfoENS_2bs15BasicByteStreamIKhEERNS1_20AttributeInfoPrivateE : 304 -> 288
~ -[_GEOTileDBWriteQueue addOperation:] : 168 -> 172
~ -[_GEOSimpleTileRequesterOperation setRequestingBundleId:] : 68 -> 64
~ -[GEORequestCounterTicketBase _subTask:completed:error:started:finished:xmitBytes:recvBytes:usedInterfaces:] : 256 -> 260
~ -[_GEOSimpleTileRequesterOperation request] : 12 -> 8
~ -[GEOSimpleTileRequester(Subclasses) downloadsDataToDisk] : 28 -> 12
~ __ZN3gcl5tmesh11DecoderImpl33parsePositionsAndConnectivityInfoENS_2bs15BasicByteStreamIKhEERNS1_35PositionsAndConnectivityInfoPrivateE : 324 -> 312
~ +[GEOReachability sharedReachability] : 120 -> 116
~ -[GEOTileServerLocalProxyBatchContext cacheMissNoDataList] : 32 -> 16
~ __ZN3geo5codec17_readContourLinesEP8VMP4TileRKNSt3__110shared_ptrINS0_10VectorTileEEE25GeoCodecsContourLineUnits26GeoCodecsContourLineRegion : 9672 -> 9644
~ -[GEOVectorTile initWithVMP4:localizationData:tileKey:] : 1352 -> 1332
~ -[GEOActiveTileSet version] : 40 -> 24
~ __ZN3geo5codec16PBDataReaderObjCD1Ev : 96 -> 100
~ -[GEOVectorTile vectorTilePtr] : 40 -> 52
~ ___82-[GEOSimpleTileRequester(GEOTileRequestBalancer) didStartOperationsForAllTileKeys]_block_invoke : 40 -> 56
~ __ZN3geo5codec23_readChapter3DBuildingsEP8VMP4TiletRNSt3__16vectorI26GeoCodecs3DBuildingFeatureNS_17allocator_adapterIS5_NS0_15zone_mallocatorEEEEERKNS3_10shared_ptrINS0_10VectorTileEEE : 2316 -> 2300
~ ___123-[GEOTileServerRemoteProxy initWithCacheDBLocation:cacheFilesLocation:manifestConfiguration:locale:delegateQueue:delegate:]_block_invoke : 96 -> 112
~ __ZN3geo5codec19_readTransitSystemsEP8VMP4TilePK16GeoCodecsTileKeyRKNSt3__110shared_ptrINS0_10VectorTileEEE : 13668 -> 13652
~ -[GEOSimpleTileRequester(Subclasses) tileEditionForKey:] : 64 -> 68
~ -[_GEOSimpleTileRequesterOperation downloadedFileURL] : 112 -> 108
~ -[GEODataURLSessionTask failedDueToCancel] : 152 -> 156
~ -[GEOTileRequestBalancer requester:completedOperations:] : 192 -> 204
~ -[GEOTileSetInfo writeTo:] : 248 -> 268
~ -[GEOClientNetworkTransactionMetrics setMultipathServiceType:] : 48 -> 44
~ -[GEODataURLSessionTask receivedRNFNotification] : 36 -> 8
~ -[_GEOSimpleTileRequesterOperation responseEtag] : 36 -> 32
~ ___51-[GEODataURLSessionTask notifyDelegateWithSession:]_block_invoke : 20 -> 24
~ -[GEOClientNetworkTransactionMetrics requestStart] : 44 -> 40
~ -[GEODataURLSessionTask response] : 108 -> 112
~ -[GEODataURLSessionTask(Tiles) validateTileResponse:error:] : 48 -> 44
~ -[GEOSimpleTileRequester(OperationDelegate) verifyDataIntegrity:checksumMethod:] : 600 -> 604
~ -[GEOClientMetrics copyWithZone:] : 232 -> 228
~ -[GEODataURLSessionTask incomingPayloadSize] : 16 -> 20
~ -[GEOClientMetrics setQueuedTime:] : 48 -> 44
~ -[GEOSimpleTileRequester(OperationDelegate) additionalNetworkEventAnalyticsStatesForKey:] : 12 -> 28
~ -[GEOLogMsgState _readTileSet] : 204 -> 224
~ -[GEOTileServerProxy delegate] : 64 -> 60
~ -[GEOFeatureStyleAttributes featureStyleAttributesPtr] : 24 -> 8
~ __ZN3geo5codec22CurveVertexPoolDeallocEP24GeoCodecsCurveVertexPool : 116 -> 132
~ -[GEODataURLSessionTask(URLSessionTask) dataURLSession:taskDidCompleteWithError:] : 676 -> 680
~ -[GEONetworkEventData _readAdditionalStates] : 216 -> 212
~ __ZN3geo11_retain_ptrIU8__strongP12NSDictionaryNS_16_retain_objc_arcENS_17_release_objc_arcENS_10_hash_objcENS_11_equal_objcEEC2EOS8_ : 136 -> 108
~ -[GEOApplicationAuditToken hash] : 112 -> 108
~ ___destroy_helper_block_ea8_32c49_ZTSKZ36-[GEOTileLoader _requestOnlineTiles]E3$_8 : 84 -> 88
~ __ZN3geo15BatchLoadHelperD1Ev : 96 -> 124
~ -[GEOTileRequest initWithKeyList:manifestConfiguration:locale:cachedEtags:cachedData:priorities:signpostIDs:createTimes:additionalInfos:cacheInfos:auditToken:constraints:backgroundSessionIdentifier:shouldParticipateInBalancer:reason:] : 676 -> 680
~ -[GEORegionalResourcesTileRequester initWithTileRequest:delegateQueue:delegate:] : 264 -> 260
~ -[GEOTileRequester setDeviceRegion:] : 84 -> 88
~ -[_GEORegionalResourcesTileLoader init] : 92 -> 88
~ -[GEOTileRequest auditToken] : 16 -> 20
~ -[_GEORegionalResourcesTileLoader loadResourcesForTileKey:manifestConfiguration:auditToken:signpostID:finished:error:] : 1576 -> 1572
~ -[GEOActiveTileGroup regionalResourcesCount] : 88 -> 92
~ _GEORegionalResourceTileKeyActiveScenarios : 172 -> 168
~ -[GEOTileKeyList addKey:lostKey:] : 460 -> 464
~ ___42-[GEORegionalResourcesTileRequester start]_block_invoke_3 : 268 -> 264
~ -[GEORegionalResourceTileData readAll:] : 224 -> 196
~ ___74-[GEORegionalResourcesTileRequester _generateEndSignpostEventIfNecessary:]_block_invoke : 252 -> 248
~ -[GEOOfflineStateManager reportTileResponse:usedInterfaces:forCohortId:duration:error:] : 264 -> 280
~ -[GEOServer daemon] : 64 -> 48
~ ___70-[GEOTileLoader _notifyObserversOfSuccess:sizeInBytes:source:options:]_block_invoke : 144 -> 160
~ __ZN3gcl5tmesh11DecoderImpl14decodeResidualERKNS0_12BinarizationEPNS0_9ACContextE : 5100 -> 5088
~ ___42+[NSBundle(GeoServicesBundle) __geoBundle]_block_invoke : 96 -> 108
~ __ZN3geo5codec20chapterReadVarUint32EP11VMP4ChapterPj : 328 -> 316
~ -[GEOAltitudeManifest commonInit] : 104 -> 116
~ __ZNSt3__113__stable_sortINS_17_ClassicAlgPolicyERZN3geo5codec11_readLabelsEP8VMP4TileRKNS_10shared_ptrINS3_10VectorTileEEEE3$_0P28GeoCodecsLabelLanguageLocaleEEvT1_SF_T0_NS_15iterator_traitsISF_E15difference_typeEPNSI_10value_typeEl : 644 -> 632
~ -[GEOAltitudeManifestReserved .cxx_construct] : 36 -> 48
~ __ZN3geo5codecL22findLabelLanguageLocalEPKvS2_ : 48 -> 64
~ -[GEOTileDB _performOnDBQueue:] : 8 -> 24
~ __ZNSt3__16vectorIiNS_9allocatorIiEEE8__appendEm : 344 -> 332
~ -[GEOAltitudeManifest parser:didStartElement:namespaceURI:qualifiedName:attributes:] : 1880 -> 1892
~ __ZN3gcl5tmesh11DecoderImpl24decodeVertexAttributesACEPiPb : 18320 -> 18336
~ -[GEOActiveTileGroup(GEOResourceManifestManagerAdditions) activeTileSetForStyle:size:scale:] : 356 -> 360
~ -[_GEOSimpleTileRequesterOperation start] : 1272 -> 1288
~ -[GEOVoltaireTileRequester activeTileSetForKey:] : 148 -> 160
~ -[GEOSimpleTileRequester _createOperationsForTileKey:priority:] : 2520 -> 2524
~ -[_GEOSimpleTileRequesterOperation delegate] : 60 -> 56
~ -[GEOSimpleTileRequester newRequestWithKind:URL:useProxyAuth:entityTag:cachedData:timeout:requestCounterTicket:] : 1456 -> 1440
~ __ZNSt3__16vectorIN2gm6MatrixIiLi3ELi1EEEN3geo17allocator_adapterIS3_NS4_5codec15zone_mallocatorEEEE8__appendEm : 484 -> 468
~ ___58-[GEOSQLiteDB bindIntParameter:toValue:inStatement:error:]_block_invoke : 16 -> 32
~ __ZN3geo5codec10VectorTile23_tileBoundsForBuildingsEv : 1004 -> 988
~ -[GEOActiveTileGroup(GEOResourceManifestManagerAdditions) activeTileSetForKey:] : 240 -> 228
~ -[GEOVectorTile .cxx_destruct] : 180 -> 160
~ ___40-[GEOTileServerRemoteProxy _handleTile:]_block_invoke_2 : 84 -> 100
~ __ZN3geo5codec10_readLinesEP8VMP4TileRKNSt3__110shared_ptrINS0_10VectorTileEEE : 14140 -> 14156
~ +[NSDictionary(GEOXPCUtil) _geo_dictionaryFromXPCObject:] : 144 -> 128
~ __ZN3geo5codec19_readTransitNetworkEP8VMP4TilePK16GeoCodecsTileKeyRKNSt3__110shared_ptrINS0_10VectorTileEEE : 33200 -> 33184
~ _GEOGetTileServerRemoteProxyLog : 112 -> 128
~ __ZNSt3__16__treeINS_10shared_ptrIK22FeatureStyleAttributesEEN25FeatureStyleAttributesSet29FeatureStyleAttributesCompareENS_9allocatorIS4_EEE7destroyEPNS_11__tree_nodeIS4_PvEE : 140 -> 156
~ -[GEODataURLSessionTask(URLSessionTask) dataURLSession:willSendRequestForEstablishedConnection:completionHandler:] : 352 -> 336
~ -[GEOTileSetInfo .cxx_destruct] : 36 -> 20
~ -[GEOActiveTileSet _readSupportedLanguages] : 220 -> 224
~ -[_GEOSimpleTileRequesterOperation .cxx_destruct] : 204 -> 200
~ ___122-[GEOTileDB addData:forKey:edition:set:provider:etag:reason:isIdenticalToExistingStaleData:forSubscriptionWithIdentifier:]_block_invoke : 320 -> 324
~ -[_GEOSimpleTileRequesterOperation dataURLSession:didCompleteTask:] : 2372 -> 2368
~ -[_GEOTileDBAddTileOperation initWithTileKey:tileSet:data:ETag:reason:externalResourceUUID:forSubscriptionWithIdentifier:] : 264 -> 280
~ -[GEOLogMsgStateTileSet writeTo:] : 312 -> 296
~ -[GEOSimpleTileRequester(OperationDelegate) operationFinished:] : 152 -> 156
~ -[_GEOSimpleTileRequesterOperation clearAllRelatedOperations] : 84 -> 80
~ -[GEOSimpleTileRequester _generateEndSignpostEventIfNecessary:] : 244 -> 248
~ -[_GEOSimpleTileRequesterOperation httpResponseStatusCode] : 120 -> 116
~ -[GEODataURLSessionTask clientMetrics] : 676 -> 680
~ -[_GEOSimpleTileRequesterOperation contentLength] : 80 -> 76
~ -[GEOSimpleTileRequester _removeRunningOperation:] : 180 -> 184
~ -[_GEOSimpleTileRequesterOperation isExistingCachedDataCurrent] : 8 -> 36
~ -[GEODataURLSessionTask downloadedFileURL] : 84 -> 56
~ __ZN12_GLOBAL__N_19isolationEv : 128 -> 124
~ -[GEOSimpleTileRequester(Subclasses) tileSetForKey:] : 228 -> 200
~ -[GEOTileRequestBalancer _requester:incrementRunningOperationsCount:] : 352 -> 348
~ -[GEOActiveTileSet _readCountryRegionAllowlists] : 200 -> 204
~ -[GEOTileRequestBalancer requesters] : 36 -> 16
~ -[GEOPrioritizedTileKeys count] : 32 -> 48
~ -[GEOTileData readDataWithError:] : 144 -> 148
~ -[GEOReachability reportTileLoadSuccess:] : 136 -> 132
~ -[GEOActiveTileGroup(GEOResourceManifestManagerAdditions) languageForTileKey:] : 100 -> 104
~ _GEOTileUnpackageBaseAndLocalization : 260 -> 256
~ -[GEOTileData readDataWithOptions:error:] : 132 -> 136
~ -[GEOReachability _resetErrors] : 140 -> 156
~ -[GEOVectorTile .cxx_construct] : 32 -> 28
~ __ZN3geo5codec16PBDataReaderObjCC1EPKhm : 136 -> 152
~ ___93-[GEODataURLSessionTask(URLSessionTask) dataURLSession:didReceiveResponse:completionHandler:]_block_invoke : 216 -> 220
~ -[_GEOSimpleTileRequesterOperation dataURLSession:shouldConvertDataTask:toDownloadTaskForEstimatedResponseSize:completionHandler:] : 340 -> 356
~ -[GEOVoltaireTileRequester shouldDownloadToDiskForTileKey:estimatedDataSize:] : 80 -> 60
~ -[GEODataURLSessionTask notifyDelegateWithSession:] : 212 -> 216
~ -[GEOClientNetworkTransactionMetrics secureConnectStart] : 36 -> 16
~ -[GEODataURLSessionTask(Convenience) HTTPStatusCode] : 80 -> 64
~ -[GEODataURLSessionTask validateTransportWithError:] : 436 -> 452
~ -[GEODataURLSessionTask(Convenience) entityTag] : 136 -> 120
~ -[GEODataURLSessionTask receivedData] : 72 -> 76
~ -[GEODataURLSessionTask(Tiles) validateNonEmptyResponseWithError:] : 292 -> 308
~ -[GEOVoltaireTileRequester shouldAllowEmptyDataForTileKey:] : 60 -> 40
~ -[GEOTileRequest loadReason] : 8 -> 12
~ -[GEOClientNetworkTransactionMetrics copyWithZone:] : 836 -> 852
~ -[GEOVoltaireTileRequester additionalAnalyticsStatesForKey:] : 336 -> 332
~ -[GEOTileSetInfo setStyle:] : 40 -> 56
~ _GEOTileKeyZoom : 100 -> 116
~ -[GEOLogMsgStateTileSet addTileSetInfo:] : 148 -> 136
~ +[GEONetworkEventDataRecorder recordNetworkEventDataForTileKey:requestAppIdentifier:appMajorVersion:appMinorVersion:error:clientMetrics:additionalStates:] : 704 -> 700
~ -[GEOTileLoader proxyDidDownloadRegionalResources:] : 120 -> 136
~ __ZN3geo5codec22DaVinciMetaDataDeallocEP24GeoCodecsDaVinciMetaData : 240 -> 224
~ __ZNK12GEOLocalPeak10mightReachEd : 212 -> 216
~ _geo_isDayLightForLocation : 184 -> 180
~ -[GEOLocationShifter .cxx_destruct] : 80 -> 84
~ -[GEOLocalizedString _readLocale] : 224 -> 220
~ ___63+[GEOAddressObject(PlaceDataExtras) addressObjectForPlaceData:]_block_invoke : 632 -> 636
~ __ZN8addr_obj12FingerprintsC2ERKNS_18AddressObjectProtoE : 596 -> 592
~ -[GEOPDComponentValue entity] : 92 -> 96
~ __ZN8addr_obj15V1AddressObjectC2ERKNS_12LocalizationERKNS_12FingerprintsERKNS_18AddressObjectProtoERKNS_17AddressObjectBase20AddressObjectVersionE : 428 -> 456
~ -[GEOPDPlace(PlaceDataExtras) _entityName] : 276 -> 280
~ -[GEOLocalizedString hasLocale] : 80 -> 76
~ -[GEOPDComponentValue placeInfo] : 104 -> 76
~ __ZNSt3__114__split_bufferIN8addr_obj12Fingerprints11FingerprintERNS_9allocatorIS3_EEED2Ev : 56 -> 68
~ -[GEOConfigStorageSetValueForKeyRequest keyValue] : 36 -> 20
~ -[GEOMapItemStorage(GEOMapItem) _clientAttributes] : 20 -> 24
~ -[GEOMapItemClientAttributes setMapsSyncAttributes:] : 96 -> 124
~ -[GEOAPSessionData .cxx_destruct] : 40 -> 44
~ ___22-[GEOUserSession init]_block_invoke : 100 -> 96
~ sub_186db2e64 -> sub_186daeca4 : 64 -> 68
~ -[GEOMapItemStorage additionalPlaceDatas] : 76 -> 72
~ -[GEOAPSessionData setSessionCreateHour:] : 60 -> 64
~ -[GEOMapItemStorage _readAdditionalPlaceDatas] : 228 -> 224
~ -[GEOPDPlace _readMapsId] : 232 -> 204
~ _GEOPDMapsIdentifierReadAllFrom : 684 -> 680
~ -[GEOMapItemIdentifier initWithMapsIdentifier:] : 168 -> 172
~ -[GEOPDShardedId copyWithZone:] : 392 -> 388
~ _GEOPDRoadAccessInfoReadAllFrom : 660 -> 664
~ sub_186dba388 -> sub_186db61ac : 68 -> 64
~ -[GEOPDPlace copyWithZone:] : 1300 -> 1272
~ -[GEOMapItemMapsSyncAttributes copyWithZone:] : 428 -> 424
~ -[GEOPDComponentValue addressObject] : 104 -> 76
~ sub_186dbbfd8 -> sub_186db7dbc : 236 -> 232
~ sub_186dbea74 -> sub_186dba854 : 180 -> 184
~ -[GEOMapItemStorage placeData] : 72 -> 100
~ __ZN8addr_obj6Base6412encodeStringERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE : 1456 -> 1460
~ -[GEOMapItemClientAttributes copyWithZone:] : 444 -> 440
~ +[GEOLocalizedString(GEOExtras) bestLocalizedString:forPreferredLanguages:fallbackToFirstAvailable:] : 580 -> 584
~ -[GEOLocalizedString .cxx_destruct] : 148 -> 144
~ +[GEOAddressObject(PlaceDataExtras) addressObjectForPlaceData:] : 844 -> 848
~ -[GEOAnalyticsPipelineStateData hasMapSettingsTrafficEnabled] : 24 -> 52
~ -[GEOPDHours init] : 112 -> 116
~ -[GEOPDShardedId setResultProviderId:] : 64 -> 60
~ -[GEOPDResultSnippet init] : 116 -> 120
~ -[GEOPDShardedId setCenter:] : 88 -> 84
~ _GEOPDRatingReadAllFrom : 420 -> 424
~ -[GEOPDMapsIdentifier setShardedId:] : 72 -> 100
~ sub_186dd990c -> sub_186dd574c : 64 -> 68
~ -[GEOStyleAttributes addAttribute:] : 124 -> 120
~ _GEOPDRatingReadSpecified : 2340 -> 2344
~ _GEOStyleAttributesReadAllFrom : 932 -> 928
~ -[GEOPDStorefront addBundleId:] : 148 -> 152
~ -[GEOMapItemStorage hash] : 248 -> 244
~ -[GEOPDAttribution _readVendorId] : 200 -> 204
~ -[GEOMapItemMapsSyncAttributes hash] : 152 -> 148
~ +[GEOMapItemStorage(GEOMapItem) mapItemStorageForPlace:] : 104 -> 108
~ -[GEOMapItemClientAttributes _readCorrectedLocationAttributes] : 216 -> 212
~ -[GEOPDCaptionedPhoto attribution] : 216 -> 220
~ ___93-[GEOProtobufSessionTask(DataTask) dataURLSession:willSendRequest:forTask:completionHandler:]_block_invoke : 232 -> 228
~ -[_GEOPlaceItem _placeData] : 16 -> 20
~ -[GEONetworkServiceRequesterOperation protobufSession:willSendRequest:forTask:completionHandler:] : 248 -> 244
~ -[_GEOPlaceItem _placeResult] : 72 -> 76
~ ___97-[GEONetworkServiceRequesterOperation protobufSession:willSendRequest:forTask:completionHandler:]_block_invoke : 280 -> 276
~ ___114-[GEODataURLSessionTask(URLSessionTask) dataURLSession:willSendRequestForEstablishedConnection:completionHandler:]_block_invoke_2 : 340 -> 344
~ ___93-[GEOProtobufSessionTask(DataTask) dataURLSession:willSendRequest:forTask:completionHandler:]_block_invoke_2 : 32 -> 28
~ +[GEOMapService shouldResolveAttribution] : 20 -> 24
~ -[GEOSearchAttributionServerRemoteProxy loadAttributionInfoForIdentifiers:completionHandler:] : 212 -> 208
~ -[_GEOPlaceDataItem _placeData] : 64 -> 68
~ -[GEOMapItemStorageUserValues _readName] : 212 -> 208
~ -[GEOPDPlace hash] : 672 -> 676
~ -[GEOPDShardedId hash] : 284 -> 280
~ -[GEOPDRating init] : 96 -> 100
~ -[GEOMapItemStorageUserValues .cxx_destruct] : 184 -> 212
~ -[GEOFeatureStyleAttributes initWithPlaceStyleAttributes:] : 620 -> 624
~ _GEOSearchAttributionManifestReadSpecified : 1708 -> 1704
~ ___57-[GEOFeatureStyleAttributes(PersonalizedItem) isLabelPOI]_block_invoke : 620 -> 592
~ sub_186de4338 -> sub_186de017c : 72 -> 68
~ -[GEOFeatureStyleAttributes hasKey:value:] : 108 -> 112
~ -[GEOSearchAttributionManifest _addNoFlagsSearchAttributionSources:] : 156 -> 152
~ _GEOPDTextBlockReadAllFrom : 400 -> 416
~ _GEOMapItemHashForPurpose : 336 -> 352
~ -[_GEOPlaceDataItem _hasMUID] : 40 -> 44
~ -[GEOSearchAttributionSource _readLocalizedAttributions] : 200 -> 196
~ -[GEOMapItemIdentifier muid] : 120 -> 124
~ _GEOLocalizedAttributionReadSpecified : 1644 -> 1640
~ _GEOPDMessageLinkReadAllFrom : 440 -> 412
~ -[GEOPDShardedId muid] : 24 -> 20
~ _GEOPDMessageLinkReadSpecified : 2560 -> 2564
~ -[GEOSearchAttributionSource _addNoFlagsLocalizedAttribution:] : 160 -> 156
~ -[_GEOPlaceDataItem _muid] : 36 -> 8
~ -[GEOLocalizedAttribution snippetLogoURLs] : 104 -> 100
~ _GEOPDPhotoReadSpecified : 1264 -> 1268
~ _GEOPDFlyoverReadSpecified : 1752 -> 1748
~ -[GEOPDPhoto _addNoFlagsPhotoVersion:] : 144 -> 148
~ -[GEOAMPPhotoInfoProvider initWithPhotoContent:] : 712 -> 708
~ _AppleMediaServicesLibraryCore : 312 -> 316
~ -[GEOMapItemStorage isEqual:] : 412 -> 408
~ _GEOPDContainedPlaceReadSpecified : 1828 -> 1832
~ ____photoContentForURLType_block_invoke : 84 -> 80
~ -[GEOPDCategorizedPhotos init] : 104 -> 108
~ +[GEODefaultPhotoInfoProvider sortedPhotoInfoFromPhotoVersions:] : 528 -> 524
~ -[GEOPDPhotoContent url] : 80 -> 84
~ -[GEODefaultPhotoInfoProvider sizeRatio] : 136 -> 148
~ -[GEOSearchAttributionLoader loadAttributionInfoForIdentifier:allowNetwork:completionHandler:] : 4268 -> 4256
~ -[GEOSearchAttributionSource sourceIdentifier] : 208 -> 236
~ _GEOPDEnhancedPlacementReadAllFrom : 1760 -> 1764
~ -[GEOLocalizedAttribution _readLanguage] : 204 -> 200
~ -[GEOPDGroundViewLabelInfo init] : 104 -> 120
~ ___94-[GEOSearchAttributionLoader loadAttributionInfoForIdentifier:allowNetwork:completionHandler:]_block_invoke : 284 -> 268
~ _GEOPDGroundViewLabelInfoReadAllFrom : 416 -> 420
~ -[GEOLocalizedAttribution(GEODeviceSpecific) bestURLForLogos:scale:] : 532 -> 528
~ -[GEOPDComponent addCommingledAttributions:] : 136 -> 140
~ -[GEOLocalizedAttribution captionDisplayString] : 216 -> 212
~ -[NSArray(GEOMapItemPhoto) _geo_firstPhotoOfAtLeastSize:] : 476 -> 480
~ -[GEOSearchAttributionSource _readAttributionRequirements] : 208 -> 204
~ -[_GEOPlaceDataPhoto bestPhotoForSize:allowSmaller:] : 144 -> 148
~ ___94-[GEOSearchAttributionServerRemoteProxy _loadAttributionInfoForIdentifiers:completionHandler:]_block_invoke : 248 -> 244
~ +[GEOMapItemPhotoOptions defaultPhotoOptionsWithAllowSmaller:] : 96 -> 80
~ -[GEOSearchAttributionLoader .cxx_destruct] : 32 -> 16
~ -[_GEOPlaceDataPhoto bestPhotoForSize:options:] : 200 -> 204
~ -[GEOPhotoInfoSource bestPhotoForSize:options:] : 260 -> 256
~ _GEOPDTrailHeadReadSpecified : 1936 -> 1940
~ -[GEODefaultPhotoInfoProvider bestPhotoForSize:options:] : 536 -> 532
~ -[_GEOPlaceDataPhoto .cxx_destruct] : 100 -> 104
~ -[GEODefaultPhotoInfoProvider .cxx_destruct] : 32 -> 28
~ -[GEOPDPlacecardLayoutConfiguration .cxx_destruct] : 88 -> 92
~ ___94-[GEOSearchAttributionServerRemoteProxy _loadAttributionInfoForIdentifiers:completionHandler:]_block_invoke_3 : 648 -> 644
~ -[GEOPDModuleLayoutEntry .cxx_destruct] : 168 -> 172
~ ___91-[GEOSearchAttributionManifestManager loadAttributionInfoForIdentifiers:completionHandler:]_block_invoke : 36 -> 32
~ ___129-[_GEOPlaceDataItem initWithPlaceData:attributionMap:disambiguationLabel:detourInfo:externalTransitStationCode:additionalPlaces:]_block_invoke_2 : 84 -> 88
~ -[GEOSearchAttributionInfo supportsActionURLs] : 496 -> 492
~ -[GEOPDMiniBrowseCategories init] : 96 -> 100
~ -[GEOSearchAttributionSource _readAttributionApps] : 192 -> 188
~ _GEOPDMiniBrowseCategoriesReadAllFrom : 440 -> 412
~ -[GEOSearchAttributionInfo attributionApps] : 84 -> 80
~ _GEOPDMiniBrowseCategoriesReadSpecified : 1256 -> 1260
~ _GEOAttributionAppReadAllFrom : 400 -> 428
~ -[GEOPDPlaceCollection init] : 96 -> 100
~ _GEOAttributionAppReadSpecified : 2100 -> 2096
~ _GEOPDPlaceCollectionReadAllFrom : 416 -> 420
~ -[GEOAttributionApp init] : 104 -> 100
~ sub_186df2fe0 -> sub_186deee00 : 132 -> 136
~ -[GEOSearchAttributionSource _addNoFlagsAttributionApps:] : 132 -> 160
~ _GEOPDTemplatePlaceReadAllFrom : 440 -> 412
~ -[GEOAttributionApp _readHandledSchemes] : 228 -> 224
~ -[GEOPDTemplatePlace init] : 116 -> 120
~ -[GEOAttributionApp _addNoFlagsHandledSchemes:] : 132 -> 160
~ -[GEOPDTemplatePlace templateDatas] : 100 -> 104
~ -[GEOMapItemPhotosAttribution initWithSearchAttributionInfo:serverAttributionURLs:clientActionURLs:poiID:] : 956 -> 952
~ -[GEOPDTemplatePlace _readTemplateDatas] : 196 -> 200
~ -[GEOSearchAttributionSource supportsAction:forComponent:] : 424 -> 420
~ -[GEOPDTemplateData init] : 124 -> 96
~ -[GEOSearchAttributionSource supportedComponentActions] : 96 -> 92
~ _GEOPDTemplateDataReadSpecified : 2676 -> 2648
~ -[GEOSearchAttributionInfo source] : 28 -> 24
~ -[GEOPDTemplateData footer] : 100 -> 104
~ __actionURLSchemes : 448 -> 476
~ -[GEOPDDataItem init] : 124 -> 96
~ -[GEOSearchAttributionSource webBaseActionURL] : 208 -> 236
~ _GEOPDDataItemReadAllFrom : 432 -> 436
~ -[GEOSearchAttributionInfo webBaseActionURL] : 16 -> 12
~ _GEOPDDataItemReadSpecified : 2288 -> 2292
~ _GEOActionURLViewPhotosURLs : 24 -> 52
~ -[GEOPDDataItem _readRatingData] : 208 -> 180
~ __GEOActionURLs : 908 -> 904
~ -[GEOPDDataItem ratingData] : 80 -> 84
~ -[GEOMapItemAttribution initWithSearchAttributionInfo:serverAttributionURLs:clientActionURLs:poiID:] : 136 -> 132
~ _GEOPDRatingDataReadSpecified : 1320 -> 1324
~ -[GEOMapItemAttribution initWithSearchAttributionInfo:serverAttributionURLs:clientActionURLs:] : 200 -> 196
~ _GEOPDCategorizedPhotosReadSpecified : 1800 -> 1804
~ _GEOStyleAttributeReadAllFrom : 1160 -> 1172
~ _GEOPDPlaceQuestionnaireResultReadSpecified : 2984 -> 2968
~ _GEOPDActionDataReadSpecified : 1880 -> 1884
~ -[GEOMapDataSubscriptionRemoteSyncManager fetchSubscriptionIdentifiersToSyncToPairedDeviceWithQueue:completionHandler:] : 268 -> 248
~ -[GEOMapSubscriptionGetIdentifiersForPairedDeviceSyncRequest encodeToXPCDictionary:] : 56 -> 76
~ -[GEOAnalyticsPipelineStateData setMapSettingsTrafficEnabled:] : 64 -> 60
~ -[GEOUserPreferences setAvoidHighways:] : 60 -> 64
~ -[GEOMapItemStorageUserValues readAll:] : 188 -> 184
~ -[GEOPDEntity _readStyleAttributes] : 212 -> 216
~ -[GEOMapItemStorageUserValues hasName] : 72 -> 84
~ -[GEOMapSubscriptionGetIdentifiersForPairedDeviceSyncRequest initWithXPCDictionary:error:] : 84 -> 104
~ _MapsFeature_IsEnabled_StandaloneWatchOffline : 28 -> 24
~ ___87-[GEOTileDB fetchSubscriptionsMatchingIdentifiers:toSyncToPairedDevice:queue:callback:]_block_invoke_3 : 40 -> 44
~ ___118-[GEOMapDataSubscriptionLocalSyncManager fetchSubscriptionIdentifiersToSyncToPairedDeviceWithQueue:completionHandler:]_block_invoke_2 : 176 -> 188
~ -[GEOMapSubscriptionGetIdentifiersForPairedDeviceSyncReply .cxx_destruct] : 20 -> 40
~ -[GEOMapDataSubscriptionManager .cxx_destruct] : 136 -> 132
~ -[GEOObserverHashTable .cxx_destruct] : 104 -> 108
~ -[GEOMapDataSubscriptionRemoteSyncManager .cxx_destruct] : 100 -> 128
~ -[GEOMapDataSubscriptionRemotePersistence .cxx_destruct] : 36 -> 8
~ -[GEOMapServiceTraits setDevicePlatform:] : 60 -> 56
~ ___getAVExternalDeviceClass_block_invoke : 168 -> 172
~ -[GEOMapServiceTraits searchOriginationType] : 112 -> 108
~ -[GEOMapService _resolveMapItemFromHandle:withTraits:cachePolicy:coordinateOnlyRefinement:completionHandler:] : 1384 -> 1388
~ -[GEOMapItemHandle _readPlaceRefinementParameters] : 216 -> 212
~ -[GEOMapService handleCache] : 188 -> 192
~ __GEOMapItemHandleCallReadAllRecursiveWithoutSynchronized : 124 -> 120
~ -[GEOPDPlaceRefinementParameters hash] : 448 -> 452
~ -[GEOMapItemHandle handleType] : 124 -> 120
~ -[GEOMapService _ticketForRefreshingHandle:traits:] : 336 -> 340
~ -[GEOMapServiceTraits setAutomobileOptions:] : 112 -> 108
~ -[GEOWalkingOptions setWalkingUserPreferences:] : 116 -> 120
~ -[GEOMapServiceTraits setWalkingOptions:] : 100 -> 96
~ -[GEOTransitOptions setRoutingBehavior:] : 64 -> 68
~ -[GEOMapServiceTraits setTransitOptions:] : 104 -> 132
~ -[GEOCyclingOptions setCyclingVehicleSpecifications:] : 92 -> 96
~ -[GEOMapServiceTraits setHistoricalLocations:] : 168 -> 164
~ -[GEOPDModule readAll:] : 228 -> 232
~ -[GEOMapServiceTraits setCurrentLocaleCurrencySymbol:] : 128 -> 124
~ -[GEOMapService ticketForMapsHomeWithTraits:] : 160 -> 164
~ -[GEOPDPlaceRequest(PlaceDataExtras) initForMapsHomeWithTraits:] : 356 -> 352
~ -[GEOPDPlacecardLayoutConfiguration readAll:] : 28 -> 32
~ -[GEOMapServiceTraits timeSinceMapEnteredForeground] : 16 -> 44
~ -[GEOPDPhoto init] : 120 -> 124
~ -[GEOMapServiceTraits currentLocaleCurrencySymbol] : 72 -> 96
~ -[GEOPDClientMetadata setPreferredDisplayCurrencySymbol:] : 120 -> 92
~ -[GEOPDCollectionSuggestionParameters init] : 108 -> 112
~ -[GEOPDPlaceRequest(PlaceDataExtras) localTimestamp] : 288 -> 284
~ _GEOPDPlaceDescriptorResolutionParametersHasSensitiveFields : 72 -> 76
~ -[GEOPDPlaceRequestParameters(PlaceDataExtras) initWithPlaceRefinementParameters:traits:] : 132 -> 128
~ -[GEOPDPlaceRequestParameters setPlaceRefinementParameters:] : 144 -> 148
~ -[GEOMapItemHandle writeTo:] : 428 -> 424
~ -[GEOUserPreferences writeTo:] : 384 -> 388
~ -[GEOPDShardedId writeTo:] : 364 -> 360
~ -[GEOPDCollectionSuggestionParameters writeTo:] : 928 -> 932
~ -[GEORecentLocations init] : 312 -> 308
~ -[GEOPDCollectionSuggestionParameters hash] : 316 -> 320
~ _MapsFeature_IsEnabled_NaturalSearchMaps : 84 -> 80
~ -[GEOMapService ticketForSearchFieldPlaceholderWithTraits:] : 160 -> 164
~ __GEOMapItemStorageCallReadAllRecursiveWithoutSynchronized : 392 -> 420
~ -[GEOSQLiteDB statementForKey:] : 88 -> 92
~ -[GEOLocation setSpeedAccuracy:] : 48 -> 44
~ -[GEOPDSearchFieldPlaceholderParameters writeTo:] : 208 -> 212
~ -[GEOLocation readFrom:] : 20 -> 16
~ -[GEOPDPlace isEqual:] : 860 -> 864
~ -[_GEOPlaceDataPhotoInfo .cxx_destruct] : 40 -> 36
~ -[GEOPDSearchFieldPlaceholderParameters hash] : 152 -> 156
~ -[GEOMapItemAttribution providerID] : 28 -> 24
~ _getAMSMediaArtworkClass : 240 -> 244
~ -[GEORegionalResourceTileDecoder decodeTile:forKey:] : 100 -> 96
~ -[GEOResourceLoadOperation URLSession:task:didReceiveChallenge:completionHandler:] : 444 -> 448
~ -[GEOTilePool setTile:forKey:cost:] : 1008 -> 1036
~ -[GEOTileCache setTile:forKey:cost:] : 568 -> 572
~ __ZN3geo13_geo_weak_ptrIU8__strongP11objc_objectEaSERKS4_ : 84 -> 80
~ __ZN3geo11_retain_ptrIU8__strongP12NSDictionaryNS_16_retain_objc_arcENS_17_release_objc_arcENS_10_hash_objcENS_11_equal_objcEEaSEOS8_ : 80 -> 84
~ -[GEOAnalyticsPipelineStateData hasMapSettingsWalkingAvoidHills] : 36 -> 32
~ -[GEOTileServerRemoteProxy loadTiles:batchID:priorities:hasAdditionalInfos:additionalInfos:signpostIDs:createTimes:reason:options:cacheInfos:auditToken:] : 1100 -> 1104
~ -[GEOAnalyticsPipelineStateData hasMapSettingsAvoidHills] : 52 -> 48
~ -[GEOTileKeyList(GEOXPCUtil) newXPCData] : 444 -> 416
~ -[GEOAnalyticsPipelineStateData setMapSettingsAvoidBusyRoads:] : 64 -> 60
~ __NSArraySafeEncodingCopy : 704 -> 708
~ -[GEOAnalyticsPipelineStateData hasMapSettingsEBike] : 36 -> 32
~ _setManifestConfiguration : 140 -> 144
~ -[GEOAnalyticsPipelineStateData setMapSettingsEBike:] : 72 -> 68
~ _setLocale : 156 -> 128
~ -[GEOAnalyticsPipelineStateData setMapSettingsIsHandsFreeProfileEnabled:] : 60 -> 56
~ ___GEOGetTileServerRemoteProxyLog_block_invoke : 96 -> 80
~ __ZN4mgcl4muid10decompressEPKcmPKiiPyim : 1168 -> 1184
~ -[GEOConfigStorageFallbackReader resync] : 256 -> 260
~ -[GEOConfigStorageCFPrefsReadOnly resync] : 4 -> 16
~ __ZN4mgcl4muid7Decoder6decEgkEiiPN3gcl17ArithmeticContextE : 508 -> 492
~ +[GEOTileLoader modernLoaderForResourceManifestConfiguration:locale:] : 1128 -> 1112
~ -[GEOPeer offlineCohortId] : 112 -> 96
~ -[GEOTileServerLocalProxy generateRequestedFromTileLoaderBeginSignpost:tileKey:options:] : 224 -> 208
~ __ZN4mgcl6iarray7Decoder10decompressEPKhRKNS1_9ArrayInfoENS0_12BinarizationENS0_18PredictionStrategyERmPb : 1844 -> 1832
~ -[GEOAnalyticsPipelineStateData setMapSettingsNotificationsEnabled:] : 64 -> 60
~ ___47-[GEOTileLoader proxy:willGoToNetworkForTiles:]_block_invoke_2 : 344 -> 360
~ __ZN4mgcl4ints15IntDecompressorItE10decompressEPKhmiimPt : 8260 -> 8244
~ -[GEOPDRoadAccessInfo .cxx_destruct] : 88 -> 92
~ -[GEORoadAccessPoint .cxx_destruct] : 96 -> 92
~ -[GEOPDSource .cxx_destruct] : 140 -> 124
~ __ZNSt3__16vectorIbNS_9allocatorIbEEEC1Em : 240 -> 260
~ -[GEOPDRap .cxx_destruct] : 40 -> 36
~ -[GEOPDStorefrontPresentation .cxx_destruct] : 128 -> 132
~ -[GEOPDFlyover .cxx_destruct] : 120 -> 116
~ -[GEOPDReview .cxx_destruct] : 184 -> 188
~ -[GEOMapItemAttribution .cxx_destruct] : 116 -> 144
~ -[GEOPDCategorizedPhotos .cxx_destruct] : 168 -> 152
~ -[GEOPDPlaceQuestionnaireResult .cxx_destruct] : 148 -> 168
~ -[GEOMapItemMapsSyncAttributes _readMapsSyncIdentifier] : 216 -> 212
~ -[GEOPDBounds _readDisplayMapRegion] : 200 -> 204
~ -[GEOPlace setType:] : 64 -> 60
~ -[GEOPDBounds displayMapRegion] : 92 -> 96
~ -[GEOPlace setPhoneticLocaleIdentifier:] : 104 -> 100
~ -[GEOPDEntity namesCount] : 84 -> 88
~ -[GEOLocalizedString hasStringValue] : 64 -> 60
~ -[GEOPDEntity spokenNameAtIndex:] : 100 -> 72
~ -[GEOPlace setSpokenName:] : 104 -> 100
~ -[GEOPDRoadAccessInfo roadAccessPoints] : 80 -> 84
~ -[GEOPlace _addNoFlagsEntryPoint:] : 136 -> 132
~ -[GEOPDEntity isDisputed] : 28 -> 32
~ -[GEOAddressObject hasKnownAccuracy] : 44 -> 40
~ -[GEOPDPlace muid] : 16 -> 20
~ -[GEOPlace setLocalSearchProviderID:] : 72 -> 68
~ -[GEOPDEntity telephone] : 96 -> 100
~ -[GEOBusiness setTelephone:] : 96 -> 92
~ -[GEOPDEntity url] : 80 -> 84
~ -[GEOBusiness setURL:] : 120 -> 116
~ -[GEOPDEntity hasIsPermanentlyClosed] : 44 -> 48
~ -[GEOBusiness _addNoFlagsSource:] : 152 -> 148
~ -[GEOTimeRange(PlaceDataExtras) initWithPlaceDataTimeRange:] : 176 -> 180
~ -[GEOBusiness _addNoFlagsOpenHours:] : 148 -> 144
~ -[GEOPhotoInfo(PlaceDataExtras) initWithPlaceDataPhotoContent:] : 432 -> 404
~ -[GEOPhoto _addNoFlagsPhotoInfo:] : 136 -> 132
~ -[GEOPDPhoto photoId] : 236 -> 208
~ -[GEOBusiness _addNoFlagsPhoto:] : 160 -> 156
~ -[GEOCategory(PlaceDataExtras) initWithPlaceDataCategory:] : 408 -> 412
~ -[GEOCategory setAlias:] : 104 -> 100
~ -[GEOPDCategory level] : 44 -> 16
~ -[GEOCategory setLevel:] : 52 -> 48
~ -[GEOLocalizedName(PlaceDataExtras) initWithPlaceDataLocalizedString:] : 228 -> 232
~ -[GEOPlace businessAtIndex:] : 72 -> 100
~ -[_GEOPlaceDataItem _customIconID] : 80 -> 84
~ -[GEOStyleAttributes customIconId] : 16 -> 44
~ ___66+[GEOPDLabelGeometry(PlaceDataExtras) labelGeometryWithPlaceData:]_block_invoke : 336 -> 340
~ -[GEORegionalResourcesTileRequester .cxx_destruct] : 136 -> 132
~ ___74+[GEOPDEnhancedPlacement(PlaceDataExtras) enhancedPlacementWithPlaceData:]_block_invoke : 324 -> 328
~ -[_GEORegionalResourcesTileLoader dealloc] : 80 -> 76
~ ___49-[GEOResourceLoader _loadNextResourceFromNetwork]_block_invoke_2 : 844 -> 848
~ -[_GEORegionalResourcesTileLoader .cxx_destruct] : 104 -> 100
~ -[GEOTileRequest .cxx_destruct] : 192 -> 208
~ __ZN4mgcl6raster20PolygonRasterDecoderItED1Ev : 216 -> 232
~ -[GEOPDAmenities _addNoFlagsAmenity:] : 136 -> 152
~ __ZN3geo5codec19MercatorDequantizer8readInfoEP11VMP4Chapter : 352 -> 336
~ -[GEOPDAmenityValue isEqual:] : 408 -> 392
~ __ZN3geo5codec14_readMaterialsEP11VMP4ChapterRNSt3__16vectorIyNS_17allocator_adapterIyNS0_15zone_mallocatorEEEEERNS4_I12VMP4MaterialNS5_ISA_S6_EEEERNS4_ImNS5_ImS6_EEEER25FeatureStyleAttributesSetb : 3464 -> 3480
~ __GEOPDRelatedPlaceCallReadAllRecursiveWithoutSynchronized : 248 -> 252
~ -[GEOPDShardedId isEqual:] : 448 -> 444
~ __GEOPDRatingCallReadAllRecursiveWithoutSynchronized : 432 -> 416
~ __ZNSt3__16vectorIN3gcl7Vector3IiEENS_9allocatorIS3_EEE8__appendEm : 692 -> 708
~ __GEOPDReviewCallReadAllRecursiveWithoutSynchronized : 292 -> 296
~ -[GEOLocalizedString readAll:] : 192 -> 188
~ -[GEOPDUser readAll:] : 240 -> 244
~ __ZNSt3__112__hash_tableIyNS_4hashIyEENS_8equal_toIyEENS_9allocatorIyEEE25__emplace_unique_key_argsIyJRKyEEENS_4pairINS_15__hash_iteratorIPNS_11__hash_nodeIyPvEEEEbEERKT_DpOT0_ : 512 -> 508
~ -[GEOPDRating readAll:] : 256 -> 228
~ -[GEOLocalizedString isEqual:] : 204 -> 200
~ -[GEOPDAddress isEqual:] : 292 -> 276
~ __ZN3geo5codec15decodeZoomRanksEP9BitstreammNSt3__18functionIFvmfEEE : 1060 -> 1044
~ _GEOPDLocalizedAddressReadSpecified : 1360 -> 1364
~ -[GEOAddress init] : 116 -> 112
~ -[GEOPDLocalizedAddress isEqual:] : 204 -> 208
~ -[GEOAddress isEqual:] : 252 -> 264
~ __ZN3geo5codec14decodeVerticesEP11VMP4ChapterPP24GeoCodecsCurveVertexPoolPP19GeoCodecsVertexPoolb : 2868 -> 2888
~ -[GEOStructuredAddress isEqual:] : 752 -> 780
~ -[GEOPDRoadAccessInfo isEqual:] : 156 -> 128
~ -[GEOLatLng isEqual:] : 308 -> 304
~ -[GEOPDEntity _addNoFlagsLocalizedCategory:] : 152 -> 136
~ __ZN3geo5codec20_makeSpaceForShieldsEmPmRKNSt3__110shared_ptrINS0_10VectorTileEEE : 480 -> 464
~ -[GEOPDCategory readAll:] : 212 -> 196
~ __ZNSt3__16vectorI20GeoCodecsRoadFeatureN3geo17allocator_adapterIS1_NS2_5codec15zone_mallocatorEEEE8__appendEm : 784 -> 804
~ -[GEOStyleAttributes readAll:] : 24 -> 20
~ -[GEOPDCategory isEqual:] : 260 -> 264
~ -[GEOPDRap isEqual:] : 180 -> 176
~ -[GEOPDEntity isPermanentlyClosed] : 16 -> 20
~ _GEOPDOrientedPositionReadAllFrom : 1680 -> 1676
~ _GEOPDStorefrontViewReadAllFrom : 412 -> 416
~ -[GEOConfigStorageDirectReadWrite _clearWriteTransaction] : 76 -> 88
~ __ZN3geo5codec21decodeSectionEncodingEP9BitstreamPP19GeoCodecsVertexPoolbPK16GeoCodecsTileKeyP27GeoCodecsVectorTileRawPoint : 2424 -> 2444
~ -[GEOPDCameraMetadata readAll:] : 260 -> 256
~ ___31-[GEODataURLSessionTask cancel]_block_invoke : 288 -> 260
~ -[GEOPDOrientedTilePosition readAll:] : 24 -> 4
~ __ZN3geo5codec18decodeAttributeSetI16GeoCodecsFeatureEEbaP9BitstreamjP25FeatureStyleAttributesSetPT_m : 2756 -> 2744
~ -[GEOTileCoordinate readAll:] : 32 -> 28
~ -[GEOPDStorefrontView init] : 124 -> 96
~ -[GEOPDCameraMetadata init] : 116 -> 96
~ -[GEOMapsAuthServiceHelper checkNetworkError:sendingGeoDErrorIfApplicable:] : 312 -> 332
~ _GEOPDCameraMetadataReadSpecified : 2728 -> 2724
~ -[GEODataURLSessionTask requestCounterTicket] : 100 -> 104
~ -[GEOPDPhotoPosition _addNoFlagsCameraMetadata:] : 160 -> 156
~ _GEOErrorDomain : 28 -> 32
~ _GEOTileCoordinateReadAllFrom : 1448 -> 1444
~ ___134-[GEOPlaceCardRequester performPlaceDataRequest:traits:cachePolicy:timeout:auditToken:throttleToken:networkActivity:requesterHandler:]_block_invoke.48 : 668 -> 672
~ -[GEOAnalyticsPipelineStateData setMapFeatureLibraryGuidesSavedPlacesCount:] : 80 -> 76
~ -[GEOPlaceCardRequester _getConnectionForRequestUUID:delete:] : 224 -> 208
~ __ZN3geo5codec33decodeLabelLineRangeUsingTileLineEP9BitstreamP23GeoCodecsLabelLineRangeP30SharedLabelLineRangeDecodeInfoP28TileLabelLineRangeDecodeInfo : 380 -> 400
~ -[GEOPlaceReplyMessage response] : 40 -> 36
~ ___56-[_GEOMapsHomeTicket submitWithHandler:networkActivity:]_block_invoke : 312 -> 316
~ -[GEOPlaceRequestMessage .cxx_destruct] : 100 -> 96
~ -[GEOPDCollectionSuggestionParameters .cxx_destruct] : 188 -> 176
~ -[GEOPDAnalyticMetadata .cxx_destruct] : 316 -> 332
~ -[GEOGeoServiceTag .cxx_destruct] : 104 -> 100
~ -[GEOUserPreferences .cxx_destruct] : 108 -> 112
~ -[GEOResourceManifestDownloadTask .cxx_destruct] : 128 -> 144
~ -[GEOPDClientMetadata copyWithZone:] : 1792 -> 1776
~ -[GEOLocation clearSensitiveFields:] : 16 -> 28
~ __ZN4mgcl4ints15IntDecompressorIjE10decompressEPKhmiimPj : 7940 -> 7928
~ -[GEOPlace(GEOProtoExtras) setCenterCoordinate:] : 204 -> 184
~ __ZNSt3__16vectorI24GeoCodecsTrafficSkeletonN3geo17allocator_adapterIS1_NS2_5codec15zone_mallocatorEEEE12emplace_backIJRS1_EEES9_DpOT_ : 836 -> 852
~ -[GEOResourceLoadOperation URLSession:task:didCompleteWithError:] : 672 -> 676
~ -[GEOReportedProgress totalUnitCount] : 28 -> 24
~ -[GEOPDPlaceInfo readAll:] : 296 -> 300
~ _GEOTimezoneReadAllFrom : 616 -> 612
~ _GEOPDBasemapRegionMetadataReadAllFrom : 600 -> 604
~ -[GEOTimezone isEqual:] : 140 -> 136
~ -[GEOPDBounds readAll:] : 232 -> 236
~ __GEOMapRegionCallReadAllRecursiveWithoutSynchronized : 272 -> 268
~ -[GEOPDViewportFrame readAll:] : 260 -> 264
~ -[GEOMapRegion isEqual:] : 492 -> 488
~ __GEOPDCategorizedPhotosCallReadAllRecursiveWithoutSynchronized : 412 -> 428
~ -[GEOPDPhotoConstraints isEqual:] : 324 -> 308
~ -[GEOPDLocationInfoItem isEqual:] : 180 -> 184
~ -[GEOMapItemStorageUserValues isEqual:] : 308 -> 304
~ -[GEOPDStorefrontView isEqual:] : 328 -> 332
~ -[GEOTileCoordinate isEqual:] : 264 -> 260
~ -[_GEOPlaceItem _placeType] : 60 -> 76
~ __GEOMapItemIsEqualForWithinDistanceExcludingName : 416 -> 432
~ -[GEOMapItemStorage(GEOMapItem) _placeType] : 84 -> 68
~ _GEOMapItemIsEqualToMapItemForPurposeWithinDistance : 1712 -> 1696
~ ___31-[_GEOPlaceDataItem _placeType]_block_invoke : 124 -> 128
~ -[GEOPlace hasLocalSearchProviderID] : 40 -> 36
~ sub_186e41320 -> sub_186e3d100 : 128 -> 132
~ -[GEOPlace type] : 120 -> 116
~ -[GEOETARequestSimple initWithXPCDictionary:error:] : 312 -> 296
~ sub_186e437e4 -> sub_186e3f5b4 : 180 -> 164
~ -[GEOETARequestSimple request] : 20 -> 36
~ -[GEOETARequest _addNoFlagsServiceTag:] : 148 -> 132
~ -[GEOKeyBagNotification state] : 36 -> 8
~ -[GEONavdClientInfo initWithCanonicalName:instanceId:] : 328 -> 324
~ -[GEOObserverHashTable unregisterObserver:] : 136 -> 140
~ -[GEOApplicationAuditToken initWithProxiedApplicationBundleId:] : 100 -> 128
~ -[GEOMapService(ExternalRequestersOnly) serializedClientMetadataForParsec] : 372 -> 376
~ -[GEOPDClientMetadata setBusinessChatPreflightIdentifiers:] : 160 -> 156
~ ___GEOGetNetEventFileManagerLog_block_invoke : 72 -> 76
~ ___GEOGetAnalyticDataFileLog_block_invoke : 80 -> 92
~ ___34-[GEOSystemMonitor _systemDidWake]_block_invoke : 140 -> 124
~ -[GEOTileCache _receivedMemoryNotification] : 124 -> 128
~ -[GEOTilePool _receivedMemoryNotification] : 156 -> 152
~ -[GEOFeatureStyleAttributes initWithFeatureStyleAttributesPtr:] : 140 -> 144
~ -[GEOMapFeatureAccess allowNetworkTileLoad] : 20 -> 16
~ -[GEOComposedRoute legs] : 24 -> 12
~ -[GEORouteMatch stepIndex] : 20 -> 32
~ ___SetXPCValue_block_invoke : 296 -> 300
~ -[GEOAnalyticsPipelineStateData mapViewLocationPuckInViewport] : 40 -> 20
~ -[GEOLogMsgStateMapViewLocation setTouristInfo:] : 100 -> 88
~ -[GEOAnalyticsPipelineStateData mapViewLocationIsTourist] : 36 -> 16
~ -[GEOLogMsgState mapViewLocation] : 88 -> 76
~ -[GEOScreenDimension copyWithZone:] : 176 -> 188
~ -[GEOLogMsgStateMapSettings setLabelEnabled:] : 56 -> 44
~ -[GEOAnalyticsPipelineStateData mapSettingsPauseSpokenAudioEnabled] : 36 -> 16
~ -[GEOLogMsgStateMapSettings setHFPEnabled:] : 44 -> 64
~ -[GEOAnalyticsPipelineStateData mapUiLayoutInfo] : 124 -> 104
~ -[GEOLogMsgState mapUi] : 72 -> 92
~ -[GEOAnalyticsPipelineStateData mapSettingsSpeedLimitEnabled] : 36 -> 16
~ -[GEOLogMsgStateMapSettings setSpeedLimitEnabled:] : 40 -> 60
~ -[GEOAnalyticsPipelineStateData mapSettingsDrivingVoiceSettings] : 116 -> 128
~ -[GEOLogMsgStateMapSettings setWalkingVoiceSettings:] : 44 -> 64
~ -[GEOAnalyticsPipelineStateData mapSettingsIsHandsFreeProfileEnabled] : 36 -> 16
~ -[GEOLogMsgStateMapUI setLayoutInfo:] : 64 -> 52
~ -[GEOAnalyticsPipelineStateData mapUiLayoutStyle] : 112 -> 124
~ -[GEOLogMsgStateMapUI setLayoutStyle:] : 40 -> 60
~ -[GEOAnalyticsPipelineStateData mapUiNumberOfMapsWindows] : 44 -> 24
~ -[GEOLogMsgStateMapUI setNumberOfMapsWindows:] : 40 -> 60
~ -[GEOAnalyticsPipelineStateData windowSize] : 112 -> 124
~ -[GEOLogMsgStateMapUI setWindowSize:] : 40 -> 60
~ -[GEOAnalyticsPipelineStateData mapSettingsTransportMode] : 104 -> 116
~ -[GEOLogMsgStateMapSettings setDrivingVoiceSettings:] : 48 -> 36
~ -[GEOAnalyticsPipelineStateData mapSettingsWalkingVoiceSettings] : 124 -> 104
~ -[GEOLogMsgStateMapUI setLandscape:] : 52 -> 40
~ -[GEODirectionsResponse sessionState] : 92 -> 88
~ -[GEOFormattedString .cxx_destruct] : 208 -> 224
~ -[GEOLogMsgEvent setMapsEnvironment:] : 116 -> 132
~ ___48-[GEOUserAccountInfo isPrimaryICloudAccountPAID]_block_invoke : 124 -> 140
~ -[GEOLogMsgEventId .cxx_destruct] : 32 -> 48
~ -[GEOUserAccountInfo isPrimaryICloudAccountPAID] : 416 -> 432
~ _GEOBatchOpaqueAppID : 16 -> 32
~ -[GEOComposedRoute stepsCount] : 36 -> 24
~ -[GEORouteMatch isGoodMatch] : 36 -> 16
~ -[GEOComposedRoute pointAt:] : 36 -> 24
~ -[GEOComposedRouteCoordinateArray coordinateOnRouteAt:] : 528 -> 508
~ -[GEOComposedRoute stepAtIndex:] : 100 -> 120
~ -[_GEOCoordinatePath coordinateAt:] : 432 -> 416
~ -[GEOComposedRouteStep startRouteCoordinate] : 32 -> 28
~ -[GEOComposedRoute pointAtRouteCoordinate:] : 20 -> 8
~ -[GEORouteMatch .cxx_construct] : 20 -> 32
~ _GEOBearingFromCoordinateToCoordinate : 176 -> 164
~ -[GEORouteMatch setIsGoodMatch:] : 16 -> 28
~ _GEOMapRectInset : 80 -> 84
~ -[GEOComposedRouteSection startPointIndex] : 12 -> 28
~ -[GEOComposedRouteCoordinateArray _length] : 352 -> 336
~ _GEOPolylineCoordinateEqual : 76 -> 72
~ -[GEOComposedRoute coordinates] : 68 -> 72
~ _GEOPolylineCoordinateIsInvalid : 20 -> 36
~ -[GEORouteMatch routeCoordinate] : 24 -> 8
~ _GEOPolylineCoordinateIsValid : 24 -> 40
~ -[GEOComposedRouteCoordinateArray coordinateCount] : 28 -> 8
~ -[GEOComposedRoute pointCount] : 56 -> 44
~ -[GEORouteMatch legIndex] : 36 -> 52
~ -[GEOComposedRouteSection endPointIndex] : 24 -> 40
~ -[GEORouteMatch route] : 32 -> 12
~ -[GEOComposedRoute(Conversions) distanceBetweenRouteCoordinate:andRouteCoordinate:] : 100 -> 120
~ -[GEOComposedRouteCoordinateArray(Conversions) distanceBetweenRouteCoordinate:andRouteCoordinate:] : 76 -> 88
~ -[GEOComposedRoute distanceBetweenRoutePointIndex:toPointIndex:] : 924 -> 928
~ -[GEOComposedRouteStep startPointIndex] : 28 -> 24
~ -[GEOComposedRoute coordinateAtOffset:fromRoutePoint:] : 40 -> 12
~ -[GEOComposedRouteStep endPointIndex] : 8 -> 24
~ -[GEOComposedRouteCoordinateArray(Conversions) routeIndexForLocalIndex:onPath:] : 220 -> 204
~ _GEOPolylineCoordinateIsABeforeB : 48 -> 76
~ -[GEOComposedRoute revisionIdentifier] : 36 -> 8
~ -[GEOComposedRouteSection composedRouteSegmentIndex] : 28 -> 24
~ -[GEOComposedRoute source] : 32 -> 36
~ _GeoServicesConfig_UseProductionURLs_Metadata_block_invoke_6 : 28 -> 24
~ -[GEOActiveTileSet isEqual:] : 728 -> 716
~ -[GEOComposedRouteCoordinateArray usesRoutingPathPoints] : 28 -> 12
~ -[GEOLocation speed] : 24 -> 20
~ -[GEONavigationMapMatcher previousMatchResult] : 36 -> 20
~ -[GEONavigationMatchResult routeMatch] : 28 -> 12
~ -[GEOComposedRoute(Conversions) routeCoordinateForDistance:beforeRouteCoordinate:] : 100 -> 88
~ -[GEOComposedRouteCoordinateArray(Conversions) routeCoordinateForDistance:beforeRouteCoordinate:] : 16 -> 28
~ -[GEOComposedRoute(Conversions) routeCoordinateForDistance:afterRouteCoordinate:] : 96 -> 100
~ -[GEOLocation rawCourse] : 116 -> 112
~ -[GEONavigationMapMatcher route] : 36 -> 8
~ -[GEOPathMatcher _isRangeValid:] : 192 -> 188
~ +[GEODefaultsDBValue dbValue:type:value:] : 136 -> 140
~ -[GEOComposedRouteStep drivingSide] : 20 -> 16
~ -[GEORouteMatcher closestRouteCoordinateForLocationCoordinate:] : 1132 -> 1136
~ -[GEOComposedRouteSection pointCount] : 36 -> 32
~ -[GEODefaultsDBValue setDbId:] : 16 -> 20
~ -[GEOPathMatcher _matchedSegmentsInRange:ofMatchedSegments:] : 1000 -> 996
~ -[GEOMatchedPathSegment endRouteCoordinate] : 60 -> 32
~ _GEOPolylineCoordinateRangeIntersectsRange : 124 -> 120
~ -[GEOMatchedPathSegment pointCount] : 28 -> 32
~ _GEOPolylineCoordinateInRange : 100 -> 96
~ -[GEORouteMatcher _startRouteMatch] : 104 -> 88
~ -[GEODrivingRouteMatcher _startStepForPreviousRouteMatch:] : 396 -> 380
~ -[GEOMultiSectionFeature roadWidth] : 44 -> 28
~ -[GEODrivingRouteMatcher _modifiedCourseAccuracyForLocation:previousRouteMatch:] : 452 -> 440
~ -[GEOPolylineCoordinateIterator current] : 28 -> 24
~ ___63-[GEORouteMatcher matchToRouteWithLocation:previousRouteMatch:]_block_invoke : 220 -> 236
~ -[GEODrivingRouteMatcher _coordinateFromLocation:] : 196 -> 180
~ -[GEORouteMatcher useMatchedCoordinateForMatching] : 12 -> 16
~ -[_GEORouteMatchingSegment distanceFromCoordinate:outCoordinateOnSegment:outRouteCoordinate:] : 444 -> 460
~ -[GEORouteMatch road] : 36 -> 16
~ -[GEOMatchedPathSegment _interpolatedCoordinateFrom:routeCoordinate:] : 760 -> 764
~ _GEOPolylineCoordinateWithinRange : 116 -> 112
~ -[GEOMatchedPathSegment initWithRoute:road:coordinates:roadRange:] : 648 -> 652
~ -[GEOLocation timestamp] : 16 -> 32
~ -[GEORouteMatch step] : 112 -> 92
~ -[GEORouteMatcher _roadWidthForSnappedSegment:] : 120 -> 104
~ -[GEODrivingRouteMatcher _courseWeightForLocation:accuracyType:] : 212 -> 200
~ -[_GEOCandidateRouteMatch .cxx_construct] : 32 -> 28
~ -[GEOFeature attributes] : 192 -> 176
~ -[GEODrivingRouteMatcher _maxMatchDistance:routeCoordinate:previousRouteMatch:timeSinceTunnel:] : 244 -> 260
~ -[GEOFeatureStyleAttributes isTunnel] : 84 -> 100
~ -[GEODrivingRouteMatcher _modifiedHorizontalAccuracy:routeCoordinate:] : 80 -> 64
~ -[GEOMapFeatureRoad roadWidth] : 100 -> 84
~ -[GEODrivingRouteMatcher _maxCourseDelta:previousRouteMatch:timeSinceTunnel:] : 328 -> 316
~ -[GEOLocation course] : 44 -> 40
~ -[GEORouteMatcher useStrictInitialOnRouteCriteria] : 12 -> 16
~ -[_GEOCandidateRouteMatch setSegment:] : 100 -> 84
~ -[GEORouteMatch consecutiveProgressionsOffRoute] : 20 -> 36
~ -[GEOMapFeatureMultiSegmentRoad feature] : 116 -> 112
~ -[GEORouteMatcher _topRouteMatchCandidate] : 28 -> 16
~ -[GEORouteMatch setRoadWidth:] : 8 -> 36
~ -[GEODrivingRouteMatcher _supportsSnapping] : 160 -> 144
~ -[GEOMatchedPathSegment locationCoordinateForRouteCoordinate:] : 196 -> 184
~ -[GEORouteMatch updateOffRouteProgress:minDistanceToGetOnRoute:] : 464 -> 444
~ -[GEORouteMatcher _finishRouteMatch:previousRouteMatch:forLocation:] : 204 -> 208
~ -[GEONavigationMatchInfo setMaxCourseDelta:] : 16 -> 28
~ -[GEODrivingRouteMatcher _finishRouteMatch:previousRouteMatch:forLocation:] : 764 -> 768
~ -[GEORouteMatch setModifiedCourseAccuracy:] : 36 -> 20
~ -[GEONavigationMatchInfo setRouteMatchScore:] : 28 -> 12
~ -[GEORouteMatch setStepIndex:] : 20 -> 36
~ -[GEONavigationMatchInfo setCourseWeight:] : 36 -> 20
~ -[GEORouteMatch setDetailedMatchInfo:] : 92 -> 76
~ -[GEONavigationMatchInfo setRoadWidthOnRoute:] : 36 -> 20
~ -[GEORouteMatch detailedMatchInfo] : 28 -> 8
~ -[GEONavigationMapMatcher roadMatcher] : 36 -> 24
~ -[GEORouteMatch candidateSteps] : 24 -> 36
~ -[GEOComposedRouteLeg endRouteCoordinate] : 56 -> 28
~ -[GEOComposedRoute(Extras) _iterateTravelTimeRangesForStep:handler:] : 548 -> 544
~ -[GEOComposedRouteLeg legIndex] : 36 -> 8
~ -[GEOComposedETARouteStep travelTime] : 16 -> 28
~ -[GEONavigationMatchResult setRouteMatch:] : 68 -> 84
~ -[GEONavigationMapMatcher setPreviousMatchResult:] : 72 -> 88
~ -[GEONavigationMatchResult roadMatch] : 16 -> 20
~ -[GEORouteMatch setShouldProjectLocationAlongRoute:] : 8 -> 20
~ -[GEOComposedWaypoint _readMapItemStorage] : 224 -> 212
~ -[GEORouteMatch shouldProjectLocationAlongRoute] : 16 -> 32
~ ___72-[GEOComposedRoute(Extras) remainingTimeToEndOfCurrentLegFrom:etaRoute:]_block_invoke : 92 -> 88
~ -[GEOComposedWaypoint uniqueWaypointID] : 100 -> 72
~ -[GEOComposedWaypoint(GEOWaypointExtras) geoMapItem] : 16 -> 12
~ ___29-[_GEOPlaceDataItem timezone]_block_invoke : 224 -> 228
~ -[GEOComposedWaypoint(GEOWaypointExtras) uniqueID] : 184 -> 180
~ +[NSUUID(GEOExtras) _geo_uuidForData:] : 220 -> 224
~ -[GEOComposedWaypoint(GEOWaypointExtras) timezone] : 96 -> 92
~ ___42-[GEORoutePreloader updateWithRouteMatch:]_block_invoke : 436 -> 440
~ -[GEOComposedRouteStep stepID] : 16 -> 12
~ -[GEOComposedRouteMutableData evInfoForStepID:] : 124 -> 128
~ +[NSMeasurement(GEOExtras) _geo_distanceMeasurementForMeters:] : 136 -> 148
~ -[GEONavigationServer(XPCInterface) _forEachValidClientOnIsolationQueue:] : 304 -> 288
~ -[GEOFormattedString _readFormatArguments] : 228 -> 200
~ sub_186e54de8 -> sub_186e50a0c : 96 -> 92
~ -[GEONavigationProxy _sendPositionFromDestination] : 100 -> 104
~ -[GEOArrivalTimeAndDistanceInfo setDistanceRemainingToEndOfRoute:] : 16 -> 12
~ -[GEONavigationProxy setETAUpdate:] : 164 -> 168
~ -[GEOArrivalTimeInfo encodeWithCoder:] : 136 -> 132
~ -[GEONavigationListener _notifyWithPositionFromDestination:] : 200 -> 188
~ -[GEORouteMatch leg] : 212 -> 196
~ __ZL23GEOGetGEOProbeCrumbsLogv : 128 -> 124
~ ___38-[GEONavigationListener setETAUpdate:]_block_invoke : 212 -> 216
~ -[GEOArrivalTimeInfo initWithLegIndex:remainingTime:] : 116 -> 112
~ -[GEONavigationProxy remoteObject] : 64 -> 84
~ -[GEOComposedRouteCoordinateArray(Conversions) distanceToEndFromRouteCoordinate:] : 80 -> 60
~ -[GEOArrivalRegion arrivalRegion] : 88 -> 92
~ -[GEOMapRegion(Containment) containsCoordinate:radius:] : 836 -> 832
~ -[GEOMapRegion(GEOProtoExtras) coordinates] : 452 -> 424
~ __ZN3geo13containsPointIdEEbRKNSt3__16vectorIN2gm6MatrixIT_Li2ELi1EEENS1_9allocatorIS6_EEEERKS6_ : 352 -> 380
~ -[GEONavigationListener setPositionFromManeuver:] : 340 -> 344
~ -[GEOComposedRouteSegment remainingDistanceAlongSegmentFromStepIndex:currentStepRemainingDistance:] : 188 -> 184
~ -[GEONavigationProxy setPositionFromManeuver:] : 28 -> 32
~ -[GEOComposedRouteSegment endStepIndex] : 20 -> 48
~ -[GEOComposedDrivingRouteStep evInfo] : 164 -> 168
~ -[GEOComposedRouteStep distance] : 8 -> 36
~ -[GEOServerFormatStyleParser _parseIfNeeded] : 24 -> 44
~ -[GEORouteMatch routeID] : 20 -> 32
~ ___49-[GEONavigationListener setPositionFromManeuver:]_block_invoke : 20 -> 36
~ sub_186e576ac -> sub_186e5331c : 208 -> 224
~ -[GEOCellConnectionQuality readAll:] : 216 -> 232
~ -[GEOLogMsgEventNetworkSelectionHarvest writeTo:] : 120 -> 136
~ -[GEOCellConnectionQuality setWifiTxPER:] : 76 -> 60
~ -[GEOLogMsgEventNetworkSelectionHarvest .cxx_destruct] : 92 -> 108
~ -[GEONetworkEventFileManager _closeFiles] : 484 -> 488
~ -[GEOAnalyticsDataFile .cxx_destruct] : 12 -> 40
~ -[GEOPDPhoto .cxx_destruct] : 132 -> 136
~ -[GEOTimezone .cxx_destruct] : 112 -> 108
~ __ZNK5zilch18TrafficDynamicTile21feedUpdateTimeSecondsEv : 8 -> 12
~ __ZN8addr_obj9VenueInfoD1Ev : 64 -> 92
~ +[GEOMapURLParser isValidMapURL:] : 392 -> 396
~ -[GEOPDPlaceRequest(PlaceDataExtras) initForBrandLookupWithIMessageUid:traits:] : 296 -> 292
~ __ZN6google8protobuf2io19EpsCopyOutputStream23WriteStringMaybeAliasedEjRKNSt3__112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEEPh : 624 -> 628
~ -[GEOProbeCrumbs _encodedDataForIntegersCount:valueCallback:] : 1480 -> 1460
~ __ZN4maps10path_codec4geo319RiceEncodedIntegersD1Ev : 4 -> 20
~ __ZN6google8protobuf8internal16InternalMetadata6DeleteINS0_15UnknownFieldSetEEEvv : 140 -> 144
~ -[GEOProbeCrumbs recentLocationHistory] : 1248 -> 1244
~ -[GEORecentLocationHistory setEncodedLats:] : 96 -> 112
~ __ZN4maps10path_codec4geo319RiceEncodedIntegersC1EPN6google8protobuf5ArenaE : 12 -> 28
~ __ZN6google8protobuf8internal14ArenaStringPtr12ClearToEmptyEv : 68 -> 84
~ __ZN4maps10path_codec4geo319RiceEncodedIntegersC2EPN6google8protobuf5ArenaE : 168 -> 156
~ ___39-[GEOProbeCrumbs recentLocationHistory]_block_invoke_2 : 60 -> 88
~ __ZN6google8protobuf8internal14ArenaStringPtr7MutableENS2_12EmptyDefaultEPNS0_5ArenaE : 212 -> 228
~ __ZN4maps10path_codec9BitStream5writeEhj : 216 -> 200
~ __ZN6google8protobuf13RepeatedFieldIjE7ReserveEi : 360 -> 344
~ __ZN4maps10path_codec9BitStream8finalizeEv : 396 -> 380
~ __ZNK6google8protobuf11MessageLite21AppendPartialToStringEPNSt3__112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEE : 528 -> 544
~ __ZNK4maps10path_codec4geo319RiceEncodedIntegers18_InternalSerializeEPhPN6google8protobuf2io19EpsCopyOutputStreamE : 708 -> 724
~ -[GEORecentLocationHistory setBaseDistanceToDestination:] : 64 -> 68
~ ___39-[GEOProbeCrumbs recentLocationHistory]_block_invoke.10 : 60 -> 88
~ -[GEORecentLocationHistory setEncodedDistancesToDestination:] : 96 -> 100
~ ___39-[GEOProbeCrumbs recentLocationHistory]_block_invoke_2.11 : 248 -> 244
~ -[GEORecentLocationHistory setEncodedTimestamps:] : 116 -> 100
~ -[GEOETATrafficUpdateRequest setClientCapabilities:] : 128 -> 112
~ -[GEOCommonOptions setExcludeGuidance:] : 48 -> 64
~ -[GEOETATrafficUpdateRequest setTripOrigin:] : 104 -> 120
~ +[GEOETARequester sharedRequester] : 108 -> 124
~ -[GEOETATrafficUpdateRequest setAbClientMetadata:] : 108 -> 124
~ -[GEOETARequester startRequest:connectionProperties:auditToken:throttleToken:callbackQueue:willSendRequest:finished:networkActivity:error:] : 1528 -> 1544
~ -[GEOETATrafficUpdateRequest tripOrigin] : 76 -> 96
~ -[GEOLocation hasTransportType] : 48 -> 28
~ -[GEOETATrafficUpdateRequest _readUserIncidentReports] : 228 -> 212
~ +[_GEOETARemoteProvider provderWithWillSendRequest:finished:networkActivity:error:] : 204 -> 208
~ -[GEOLocation hasRoadClass] : 24 -> 52
~ -[GEOETARequestUpdateable encodeToXPCDictionary:] : 268 -> 272
~ -[GEOApplicationAuditToken encodeToXPCDictionary:] : 212 -> 224
~ -[GEOETATrafficUpdateRequest readAll:] : 220 -> 208
~ -[GEOArtworkCapabilities writeTo:] : 168 -> 164
~ -[GEOCommonOptions writeTo:] : 356 -> 372
~ __ZN8addr_obj10Formatting26overrideLegacyShortAddressERKNS_12LocalizationERKNSt3__112basic_stringIcNS4_11char_traitsIcEENS4_9allocatorIcEEEE : 84 -> 68
~ -[GEOComposedString encodeWithCoder:] : 216 -> 236
~ -[GEORouteMatch encodeWithCoder:] : 380 -> 360
~ -[GEOComposedRouteMutableData updateableCameraInfos] : 12 -> 32
~ -[GEORouteMatch setRoute:] : 120 -> 132
~ -[GEOSignGuidance _readSignTitles] : 220 -> 224
~ -[GEOProbeCrumbs addLocation:polyCoordinate:timestamp:] : 2124 -> 2140
~ +[GEOLatLngE7(GEOProtoExtras) toE7Coordinate:] : 24 -> 36
~ +[GEOPDTransitInfoSnippet(PlaceDataExtras) transitInfoSnippetForPlaceData:] : 292 -> 296
~ -[GEOComposedWaypoint(GEOWaypointExtras) waypointCategory] : 384 -> 380
~ -[GEOGuidanceEvent spokenGuidance] : 84 -> 88
~ -[GEOComposedRouteStep timeCheckpoints] : 20 -> 16
~ -[GEOStep _readTimeCheckpoints] : 204 -> 208
~ -[GEOComposedRouteStep routeCoordinateRange] : 116 -> 112
~ -[GEOLocation(GEOProtoExtras) hasAccurateCourse] : 144 -> 116
~ -[GEOLocation hasCourseAccuracy] : 20 -> 48
~ -[GEORouteMatcher _scoreModifierForStep:previousStep:] : 28 -> 32
~ -[GEOArrivalTimeInfo initWithCoder:] : 160 -> 156
~ -[GEONavigationListener setETAUpdate:] : 188 -> 172
~ ___64-[GEONavigationServer(XPCInterface) setPositionFromDestination:]_block_invoke_2 : 28 -> 32
~ -[GEORouteMatch initWithCoder:] : 568 -> 580
~ -[GEOComposedGuidanceEvent isEqual:] : 164 -> 168
~ -[GEONavigationMatchInfo roadWidthOnRoute] : 28 -> 24
~ -[GEORouteAttributes dealloc] : 120 -> 124
~ _GEONameInfoReadSpecified : 2436 -> 2432
~ -[GEOComposedRoute destination] : 112 -> 128
~ -[GEOComposedRouteVisualInfo routeCoordinateRange] : 16 -> 36
~ __ZNK8addr_obj15V2AddressObject15getShortAddressEv : 340 -> 336
~ -[GEOComposedRoute composedGuidanceEvents] : 8 -> 12
~ -[GEOMapItemRoutineAttributes loiType] : 108 -> 104
~ -[GEOMultiSectionFeature formOfWay] : 36 -> 40
~ -[GEONavigationMatchInfo distanceFromRoad] : 24 -> 20
~ __ZL25GEOGetGEOComposedRouteLogv : 108 -> 112
~ _GEOPolylineCoordinateAsString : 184 -> 180
~ -[GEOCompanionDriveStep readAll:] : 208 -> 212
~ -[GEONameInfo copyWithZone:] : 576 -> 572
~ -[GEOCompanionStep readAll:] : 224 -> 196
~ -[GEONameInfoList copyWithZone:] : 364 -> 360
~ -[GEOCompanionDriveStep _reserveJunctionElements:] : 244 -> 248
~ -[GEONameInfoList addNameInfo:] : 148 -> 144
~ -[GEODirectionsRequest(GEOProtoExtras) initDefaultFeedbackInfo] : 168 -> 172
~ -[GEODirectionsRequest hasSessionRelativeTimestamp] : 48 -> 44
~ -[GEOCompanionStep copyWithZone:] : 1484 -> 1488
~ sub_186e6cf08 -> sub_186e68ccc : 348 -> 344
~ -[GEOJunction elements] : 24 -> 28
~ ___40-[GEOUserSession _mapsUserSessionEntity]_block_invoke : 148 -> 128
~ -[GEOUserSessionEntity sessionID] : 16 -> 36
~ -[GEODirectionsRequest setSessionID:] : 56 -> 68
~ -[GEOUserSessionEntity sessionRelativeTimestamp] : 28 -> 16
~ -[GEODirectionsRequest readAll:] : 224 -> 220
~ -[GEORouteAttributes init] : 100 -> 104
~ _GEOClientCapabilitiesReadAllFrom : 440 -> 436
~ -[GEOCompanionRouteStatus(CompanionCompatibility) instanceCompatibleWithProtocolVersion:] : 784 -> 788
~ -[GEODirectionsRequest hasSessionID] : 48 -> 44
~ -[GEOCompanionRouteContext origin] : 60 -> 64
~ -[GEOMapItemRoutineAttributes writeTo:] : 512 -> 508
~ __GEOComposedWaypointIsDirty : 228 -> 200
~ -[GEOMapItemRoutineAttributes readAll:] : 188 -> 184
~ -[GEOPDComponentValue writeTo:] : 3360 -> 3364
~ -[GEOLatLngE7 writeTo:] : 148 -> 144
~ -[GEOComposedWaypoint writeTo:] : 688 -> 692
~ -[GEOLocalizedString writeTo:] : 424 -> 420
~ -[GEOPDStorefrontView writeTo:] : 460 -> 464
~ -[GEOPDRigMetrics writeTo:] : 120 -> 116
~ -[GEOPDPlaceInfo writeTo:] : 624 -> 628
~ -[GEOTimezone writeTo:] : 140 -> 136
~ ___51-[GEOSQLiteDB bindNullParameter:inStatement:error:]_block_invoke : 24 -> 28
~ -[GEOSubPremise .cxx_destruct] : 84 -> 112
~ __ZNSt3__120__shared_ptr_pointerIPN5zilch18TrafficDynamicTile8IncidentENS_10shared_ptrIS3_E27__shared_ptr_default_deleteIS3_S3_EENS_9allocatorIS3_EEE21__on_zero_shared_weakEv : 24 -> 8
~ -[GEOTouristInfo writeTo:] : 164 -> 184
~ -[GEOPlaceReplyMessage encodeToXPCDictionary:] : 276 -> 272
~ -[GEOPDPlaceResponse writeTo:] : 1444 -> 1428
~ sub_186e7f5dc -> sub_186e7b38c : 80 -> 100
~ -[GEODirectionsRequest copyWithZone:] : 3416 -> 3412
~ -[GEOCompanionRouteStatus setRouteMatchCoordinate:] : 120 -> 104
~ sub_186e81efc -> sub_186e7dcac : 108 -> 92
~ ___53-[GEONavigationListener setLocation:routeCoordinate:]_block_invoke : 428 -> 444
~ -[GEONavigationServer(XPCInterface) setLocation:routeCoordinate:] : 428 -> 412
~ -[GEONavigationListener setLocation:routeCoordinate:] : 176 -> 180
~ -[GEOLocation description] : 176 -> 192
~ -[GEORouteMatch locationCoordinate] : 8 -> 20
~ -[GEOComposedString stringWithOptions:] : 104 -> 108
~ -[GEOFormattedString(GEOServicesExtras) formatTokens] : 16 -> 12
~ -[GEOComposedRoute segmentIndexForStepIndex:] : 348 -> 336
~ -[GEORouteMatch transitID] : 32 -> 12
~ -[GEOComposedRoute distanceBetweenLocation:nextPointIndex:toPointIndex:] : 272 -> 276
~ -[GEOComposedRouteTraffic routeTrafficColors] : 32 -> 28
~ -[GEOComposedRoute laneCountAtRouteCoordinate:] : 700 -> 704
~ -[GEOComposedRouteStep maneuverStartRouteCoordinate] : 12 -> 8
~ -[GEOJunction numElements] : 44 -> 48
~ -[GEOComposedRouteStep isStartOrResumeStep] : 140 -> 136
~ -[GEOComposedRouteMutableData traffic] : 24 -> 28
~ -[GEOComposedRouteStep maneuverRoadName] : 760 -> 756
~ -[GEOComposedStringReplacementResult attributedComponentStrings] : 12 -> 16
~ -[GEOComposedWaypoint(GEOWaypointExtras) isServerProvidedWaypoint] : 8 -> 36
~ -[GEOJunction initWithCoder:] : 216 -> 220
~ sub_186e88a60 -> sub_186e84824 : 136 -> 132
~ -[GEOTripInfo copyWithZone:] : 140 -> 144
~ -[GEODirectionsResponse copyWithZone:] : 3612 -> 3608
~ -[GEOCompanionRouteDetails _addNoFlagsWaypoints:] : 144 -> 148
~ -[GEOWaypointPlace _readRoadAccessPoints] : 220 -> 216
~ -[GEOCompanionWaypoint .cxx_destruct] : 192 -> 164
~ -[GEOWaypointPlace .cxx_destruct] : 160 -> 156
~ -[GEOTripInfo .cxx_destruct] : 40 -> 44
~ -[GEOWaypointPlace readAll:] : 208 -> 204
~ -[GEODirectionsRequestFeedback .cxx_destruct] : 144 -> 148
~ sub_186e8e668 -> sub_186e8a40c : 176 -> 172
~ -[GEOGuidanceEvent .cxx_destruct] : 224 -> 228
~ -[GEODirectionsRequest .cxx_destruct] : 752 -> 748
~ -[GEOCommonOptions .cxx_destruct] : 28 -> 32
~ -[GEODirectionsResponse init] : 96 -> 124
~ -[GEOCompanionRouteStatus hasHapticsType] : 44 -> 48
~ -[GEOWaypointTyped readAll:] : 196 -> 224
~ -[GEOMuninBucket .cxx_destruct] : 84 -> 100
~ -[GEOLogMsgStateUserSession setNavSessionRelativeTimestamp:] : 36 -> 56
~ _MapsFeaturesConfig_EnableMoreReportTypes_Metadata_block_invoke_18 : 36 -> 32
~ -[GEOComposedRoute registerObserver:] : 180 -> 184
~ -[GEOWaypointID readAll:] : 224 -> 220
~ __GEOComposedWaypointCallReadAllRecursiveWithoutSynchronized : 148 -> 152
~ -[GEOAlmanac nextSunset] : 20 -> 16
~ __Z27StringFromGEOSolarEventTypej : 236 -> 240
~ -[GEOAnalyticsPipelineStateData mapViewViewMode] : 104 -> 116
~ -[GEOLogMsgStateMapView setViewMode:] : 44 -> 64
~ -[GEOAnalyticsPipelineStateData placeCardState] : 80 -> 92
~ -[GEOLogMsgStatePlaceCard copyWithZone:] : 1240 -> 1224
~ -[GEOPlaceActionDetails readAll:] : 224 -> 208
~ -[GEOLogMsgState setPlaceCard:] : 104 -> 120
~ -[GEOPlaceActionDetails .cxx_destruct] : 184 -> 200
~ -[GEOLogMsgStatePlaceCard writeTo:] : 1244 -> 1260
~ -[GEOPlaceActionDetails writeTo:] : 732 -> 748
~ -[GEOLogMsgStatePlaceCard readAll:] : 196 -> 216
~ -[GEOSearchCategoryStorage writeTo:] : 396 -> 380
~ -[GEOPDBrowseCategory readAll:] : 256 -> 240
~ -[GEOMapServiceTraits _readMapRegion] : 224 -> 220
~ -[GEOMapService ticketForCategoryListWithTraits:isFromNoQueryState:] : 176 -> 180
~ -[GEOMapServiceTraits setNavigating:] : 56 -> 52
~ -[GEOCyclingUserPreferences copyWithZone:] : 232 -> 236
~ -[GEOMapServiceTraits setSupportUnresolvedDirectionIntent:] : 56 -> 52
~ -[GEOFareOptions copyWithZone:] : 200 -> 204
~ -[GEOProtobufSessionTask description] : 132 -> 144
~ -[GEODataURLSessionTask(Convenience) originalRequestURL] : 96 -> 112
~ __ZL18shouldCountRequest18GEODataRequestKind31GEOMapServiceTraits_RequestMode : 192 -> 164
~ -[GEOProtobufSessionTask(DataTask) parseResponseFromResponseData:] : 372 -> 368
~ -[GEODataURLSessionTask description] : 208 -> 212
~ -[GEOProtobufSessionTask(DataTask) _decodeResponseFromTask:completion:] : 568 -> 564
~ __GEORequestResponseLogQueue : 100 -> 104
~ -[GEOProtobufSessionTask clientMetrics] : 100 -> 96
~ ____GEORequestResponseLogResponse_block_invoke : 956 -> 960
~ -[GEOServiceRequester _takeCurrentOperationForRequest:] : 280 -> 276
~ -[GEODataURLSessionTask backingTask] : 8 -> 12
~ -[GEOProtobufSessionTask(DataTask) dataURLSession:didCompleteTask:] : 588 -> 584
~ -[GEODataURLSessionTask protocolBufferHasPreamble] : 8 -> 12
~ -[GEOProtobufSessionTask requestTypeCode] : 20 -> 16
~ _GEOPDDatasetABStatusIsValid : 680 -> 652
~ -[GEOProtobufSessionTask completeWithCancelled:error:response:] : 432 -> 428
~ -[PBCodable(GEOClientMetrics) setClientMetricsIfSupported:] : 116 -> 120
~ -[GEOProtobufSessionTask(Result) response] : 80 -> 76
~ -[GEOPDPlaceResponse .cxx_destruct] : 328 -> 332
~ -[GEOPlaceReplyMessage setResponse:] : 108 -> 104
~ -[GEOPDComponentValue messageLink] : 92 -> 96
~ -[GEOMessageLink initWithMessageLink:] : 292 -> 288
~ -[GEOPDMessageLink timezone] : 92 -> 96
~ -[GEOStyleAttribute writeTo:] : 188 -> 184
~ -[GEOPlaceDataRequestConfig serviceTypeNumber] : 44 -> 32
~ -[GEOPDBrowseCategory .cxx_destruct] : 220 -> 204
~ -[GEONetworkServiceRequesterOperation .cxx_destruct] : 204 -> 200
~ _protobufDataWithHeader : 348 -> 320
~ _GEOStyleAttributeIsValid : 868 -> 864
~ __GEORequestResponseLogResponse : 328 -> 332
~ -[GEOExperimentConfiguration refreshDatasetABStatus:] : 132 -> 128
~ -[GEOPDDatasetABStatus hasDatasetId] : 36 -> 40
~ -[GEOCoarseLocationProvider fetchCoarseEquivalentForLocation:callbackQueue:callback:] : 40 -> 36
~ _GEOTileKeyAssertIsStandard : 140 -> 124
~ _GEOGloriaQuadIDTileKeyMakeWithCoordinate : 144 -> 128
~ -[GEOTileLoader loadKey:additionalInfo:priority:forClient:options:reason:qos:signpostID:createTime:callbackQ:beginNetwork:callback:] : 276 -> 280
~ -[GEOApplicationAuditToken description] : 220 -> 216
~ -[GEOVectorTileDecoder canDecodeTile:quickly:] : 168 -> 172
~ ___103-[GEOCoarseLocationProvider _fetchCoarseEquivalentForLocation:addLocationNoise:callbackQueue:callback:]_block_invoke.7 : 608 -> 604
~ -[GEOTileServerRemoteProxy close] : 28 -> 32
~ -[GEOCoarseLocationData initWithFileURL:tileKey:] : 480 -> 476
~ +[GEOPDMessageLink(PlaceDataExtras) messageLinkForPlaceData:] : 280 -> 284
~ -[GEOMessageLink navBackgroundColorString] : 104 -> 132
~ -[GEOPDMessageLink navBackgroundColor] : 104 -> 108
~ ___103-[GEOCoarseLocationProvider _fetchCoarseEquivalentForLocation:addLocationNoise:callbackQueue:callback:]_block_invoke : 624 -> 652
~ ___79-[_GEOPlaceRequestTicket submitWithHandler:auditToken:timeout:networkActivity:]_block_invoke_3 : 208 -> 212
~ -[GEOCoarseLocationProvider _snapNonMercatorCoordinateIfNecessary:callbackQueue:callback:] : 688 -> 716
~ __ZNK3geo9TarBuffer4ReadERKxRKmRN6gloria5SliceE : 164 -> 168
~ _GEOGetCoarseLocationLog : 116 -> 112
~ _GEOMapRectUnion : 172 -> 176
~ -[GEOStructuredAddress country] : 76 -> 72
~ -[GEOPDTooltipFilter hash] : 68 -> 72
~ -[GEOPDPlaceRequest(PlaceDataExtras) browseCategorySuggestionparametersWithTraits:isFromNoQueryState:] : 952 -> 948
~ -[GEOPDSearchBrowseCategorySuggestionParameters init] : 100 -> 116
~ +[GEOPDViewportInfo(PlaceDataExtras) viewportInfoForTraits:] : 120 -> 108
~ -[GEOMapServiceTraits hasTimeSinceMapViewportChanged] : 48 -> 44
~ -[GEOPDSearchBrowseCategorySuggestionParameters setViewportInfo:] : 152 -> 156
~ -[GEOMapServiceTraits devicePlatform] : 104 -> 132
~ -[GEOPDSearchBrowseCategorySuggestionParameters setSearchOriginationInfo:] : 156 -> 160
~ -[GEOMapServiceTraits _dictionaryRepresentation:] : 13068 -> 13064
~ -[GEOPDViewportInfo writeTo:] : 196 -> 216
~ -[GEOPDSearchOriginationInfo readAll:] : 244 -> 224
~ -[GEOPDComponentFilter setToolTipFilter:] : 144 -> 148
~ -[GEOMapServiceTraits hasMapRegion] : 76 -> 72
~ -[GEOPDViewportInfo setMapRegion:] : 84 -> 88
~ -[GEOMapServiceTraits timeSinceMapViewportChanged] : 24 -> 20
~ -[GEOPDViewportInfo setTimeSinceMapViewportChanged:] : 56 -> 60
~ -[GEOMapServiceTraits hasNavigationTransportType] : 52 -> 48
~ _GEOGetUserPreferredTransportType : 60 -> 32
~ -[GEOPDSearchOriginationInfo(PlaceDataExtras) initWithTraits:] : 624 -> 620
~ -[GEOPDPlaceRequestParameters setBrowseCategorySuggestionParameters:] : 136 -> 140
~ -[GEOTraitsTransitScheduleTimeRange readAll:] : 4 -> 32
~ -[GEOFareOptions readAll:] : 28 -> 32
~ -[GEOPDVenueIdentifier readAll:] : 244 -> 240
~ -[GEOCyclingVehicleSpecifications readAll:] : 16 -> 20
~ -[GEOMapServiceTraits _readAutomobileOptions] : 220 -> 216
~ -[GEOAutomobileOptions _readVehicleSpecifications] : 224 -> 228
~ -[GEOMapServiceTraits _readTransitOptions] : 232 -> 228
~ -[GEOFareOptions dictionaryRepresentation] : 12 -> 16
~ -[GEOMapServiceTraits _readWalkingOptions] : 208 -> 204
~ -[GEOWalkingUserPreferences dictionaryRepresentation] : 24 -> 28
~ -[GEOMapServiceTraits _readCyclingOptions] : 220 -> 216
~ -[GEOCyclingVehicleSpecifications dictionaryRepresentation] : 36 -> 8
~ -[GEOMapServiceTraits _readUserActionMetadata] : 204 -> 232
~ _GEOPDViewportInfoReadAllFrom : 1248 -> 1236
~ _GEOPDSearchOriginationInfoReadSpecified : 2492 -> 2472
~ -[GEOPDSSearchEvChargingParameters readAll:] : 240 -> 244
~ -[GEOLocation hash] : 1936 -> 1932
~ -[GEOPDViewportInfo hash] : 144 -> 148
~ -[GEOMapRegion hash] : 776 -> 792
~ -[GEOPDSearchOriginationInfo hash] : 184 -> 196
~ -[GEOMapService ticketForSearchCapabilitiesWithTraits:] : 216 -> 220
~ -[GEOPDPlaceRequest(PlaceDataExtras) initForSearchCapabilitiesWithTraits:] : 252 -> 248
~ -[GEOPDViewportInfo .cxx_destruct] : 96 -> 100
~ -[GEOSearchCategory styleAttributes] : 164 -> 180
~ -[GEOPDBrowseCategory styleAttributes] : 220 -> 232
~ _GeoCodecsFeatureStyleAttributesCompare : 268 -> 284
~ __ZN3geo5codec29featureStyleAttributesCompareERKNSt3__110shared_ptrIK22FeatureStyleAttributesEES7_ : 224 -> 212
~ -[GEOSearchCategory shortDisplayString] : 128 -> 144
~ -[GEOPDBrowseCategory shortDisplayString] : 108 -> 88
~ _GEOPDSearchBrowseCategorySuggestionResultIsValid : 712 -> 700
~ sub_186ebdff8 -> sub_186eb9e4c : 64 -> 76
~ -[GEOPlaceDataRequestConfig additionalStatesForNetworkEvent] : 280 -> 264
~ -[GEOLogMsgStatePlaceRequest setPlaceRequestType:] : 40 -> 56
~ __GEOPDPlaceGlobalResultIsDirty : 1692 -> 1708
~ -[GEOLogMsgStatePlaceRequest writeTo:] : 172 -> 188
~ -[GEOPDPlace setNilPlace:] : 48 -> 52
~ -[GEOPDPlaceRequest(PlaceDataExtras) isBrandLookupRequest] : 160 -> 156
~ -[GEOPDSearchBrowseCategorySuggestionParameters .cxx_destruct] : 196 -> 184
~ -[GEOPDSearchOriginationInfo .cxx_destruct] : 108 -> 120
~ _GEOPDSearchBrowseCategorySuggestionResultReadAllFrom : 928 -> 948
~ sub_186ec3ff4 -> sub_186ebfe88 : 68 -> 48
~ -[GEOPDSearchBrowseCategorySuggestionResult categorys] : 104 -> 76
~ -[GEOProtobufSessionTask .cxx_destruct] : 152 -> 136
~ -[GEOPDBrowseCategory _readSubCategorys] : 184 -> 196
~ -[GEOPDSearchBrowseCategorySuggestionResult .cxx_destruct] : 112 -> 84
~ -[GEOSearchCategory isEqual:] : 120 -> 136
~ __GEOPDBrowseCategoryCallReadAllRecursiveWithoutSynchronized : 296 -> 280
~ -[GEOSearchCategoryStorage setBrowseCategory:] : 116 -> 96
~ _GEOETAStepIsValid : 1756 -> 1772
~ sub_186ec69f8 -> sub_186ec2838 : 104 -> 108
~ _GEONameInfoIsValid : 1296 -> 1292
~ _GEORestrictionZoneInfoIsValid : 1192 -> 1208
~ -[GEOETATrafficUpdateWaypointRoute init] : 100 -> 120
~ -[GEOUUID writeTo:] : 176 -> 188
~ -[GEOETATrafficUpdateResponse _readDatasetAbStatus] : 228 -> 212
~ -[GEORecentLocationHistory init] : 112 -> 100
~ -[GEOLatLngE7(GEOProtoExtras) initWithE7Latitude:longitude:] : 132 -> 148
~ -[GEOLatLngE7 setLngE7:] : 24 -> 20
~ -[GEORecentLocationHistory setBaseTimestamp:] : 64 -> 68
~ -[GEOComposedETARoute updateForResponse:route:] : 4096 -> 4108
~ _GEOETARouteReadAllFrom : 412 -> 432
~ -[GEOComposedETARoute _startingStepIndexForResponse:onRoute:] : 388 -> 400
~ -[GEOETAStep expectedTime] : 32 -> 20
~ -[GEOComposedETARouteLeg setSteps:] : 92 -> 72
~ -[GEOETARoute originWaypointInfo] : 96 -> 80
~ _GEOWaypointInfoReadAllFrom : 436 -> 440
~ -[GEOComposedETARouteLeg setOriginWaypointInfo:] : 76 -> 88
~ -[GEOETARoute _readDestinationWaypointInfo] : 232 -> 220
~ -[GEOComposedETARouteLeg setDestinationWaypointInfo:] : 64 -> 92
~ -[GEOWaypointInfo evChargingInfo] : 80 -> 96
~ -[GEOETATrafficUpdateWaypointRoute traversalTimes] : 76 -> 92
~ -[GEOTraversalTimes historicalEstimatedSeconds] : 16 -> 32
~ -[GEOETATrafficUpdateRequest _readRouteAttributes] : 216 -> 232
~ -[GEOComposedRoute styleAttributes] : 12 -> 28
~ -[GEOETATrafficUpdateWaypointRoute newWaypointRoutes] : 72 -> 56
~ -[GEOWaypointRoute init] : 116 -> 100
~ -[GEOETATrafficUpdateWaypointRoute _addNoFlagsNewWaypointRoutes:] : 144 -> 160
~ -[GEORoutePlanningInfo init] : 100 -> 116
~ -[GEORouteInitializerData routeAttributes] : 8 -> 24
~ -[GEOWaypointRoute _addNoFlagsName:] : 132 -> 136
~ -[GEONameInfo _readName] : 224 -> 220
~ -[GEORouteInformation routeDescription] : 224 -> 228
~ -[GEOComposedStringArgument_Distance _initWithGeoFormatArgument:] : 312 -> 340
~ -[GEOWaypointRouteFeatures avoidsTraffic] : 16 -> 32
~ -[GEORouteInitializerData styleAttributes] : 36 -> 20
~ -[GEORawPathGeometry initWithRawData:pathMatcherInstructions:] : 180 -> 168
~ -[GEOComposedRouteCoordinateArray initWithRawRouteGeometry:] : 2720 -> 2700
~ -[GEORawPathGeometry decompressedPathData] : 96 -> 112
~ __ZN4maps10path_codec4geo314RoutingPathLeg5ClearEv : 212 -> 228
~ __ZN6google8protobuf8internal16ReadSizeFallbackEPKcj : 136 -> 120
~ __ZN4maps10path_codec4geo319RiceEncodedIntegers14_InternalParseEPKcPN6google8protobuf8internal12ParseContextE : 980 -> 964
~ __ZN6google8protobuf8internal11VarintParseIyEEPKcS4_PT_ : 132 -> 148
~ __ZN6google8protobuf5Arena18CreateMaybeMessageIN4maps10path_codec4geo316SupportPointDataEJEEEPT_PS1_DpOT0_ : 224 -> 208
~ __ZN6google8protobuf8internal20RepeatedPtrFieldBase7ReserveEi : 48 -> 32
~ __ZN6google8protobuf8internal20RepeatedPtrFieldBase7DestroyINS0_16RepeatedPtrFieldIN4maps10path_codec4geo34UUIDEE11TypeHandlerEEEvv : 168 -> 172
~ -[_GEOCoordinatePath setBasicCoordinates:] : 212 -> 208
~ __ZN6google8protobuf8internal20RepeatedPtrFieldBase7DestroyINS0_16RepeatedPtrFieldIN4maps10path_codec4geo316RoutingPathPointEE11TypeHandlerEEEvv : 148 -> 132
~ -[GEORawPathGeometry .cxx_destruct] : 76 -> 80
~ ___117+[GEORouteBuilder _componentsForGeoWaypointRoute:initializerData:coordinates:custodian:outLegs:outSegments:outSteps:]_block_invoke : 60 -> 40
~ -[GEORouteInitializerData directionsRequest] : 28 -> 32
~ -[GEOComposedRouteCoordinateArray coordinateCountForPathAtIndex:] : 72 -> 84
~ -[GEOStep maneuverStartPointOffsetCm] : 24 -> 28
~ -[GEOComposedRouteStep initWithComposedRoute:geoRouteLeg:geoStep:routeSegmentType:stepIndex:startRouteCoordinate:endRouteCoordinate:maneuverStartRouteCoordinate:] : 396 -> 392
~ -[GEOStep _readEvStateInfo] : 212 -> 228
~ sub_186ede034 -> sub_186ed9f04 : 120 -> 136
~ _GEOLabelActionIsValid : 912 -> 916
~ _GEOMapRegionIsValid : 1208 -> 1204
~ _GEOCommonResponseAttributesIsValid : 704 -> 688
~ _GEOETATrafficUpdateWaypointRouteReadSpecified : 2820 -> 2840
~ _GEOUUIDReadAllFrom : 1112 -> 1108
~ _GEOCommonResponseAttributesReadAllFrom : 864 -> 848
~ -[GEOETATrafficUpdateWaypointRoute writeTo:] : 1304 -> 1288
~ -[GEOCommonResponseAttributes writeTo:] : 152 -> 136
~ -[GEOETATrafficUpdateResponse initWithData:] : 104 -> 120
~ ___154-[GEOETATrafficUpdateRequester sendConditionalETATrafficUpdateRequest:timeWindowDuration:auditToken:throttleToken:willSendRequestHandler:finishedHandler:]_block_invoke_2 : 28 -> 32
~ -[GEOLatLngE7 setLatE7:] : 16 -> 44
~ -[GEORecentLocationHistory setBaseLocation:] : 104 -> 108
~ ___39-[GEOProbeCrumbs recentLocationHistory]_block_invoke : 72 -> 84
~ -[GEOETATrafficUpdateWaypointRoute _addNoFlagsRouteLeg:] : 148 -> 132
~ -[GEOComposedRouteLeg stepCount] : 24 -> 8
~ -[GEOETARoute _readOriginWaypointInfo] : 204 -> 220
~ -[GEOWaypointInfo _readEvChargingInfo] : 208 -> 224
~ -[GEOETATrafficUpdateWaypointRoute _readTraversalTimes] : 204 -> 220
~ -[GEOTraversalTimes conservativeEstimatedSeconds] : 36 -> 20
~ -[GEOETATrafficUpdateWaypointRoute _readNewWaypointRoutes] : 228 -> 212
~ sub_186eec278 -> sub_186ee8158 : 80 -> 96
~ -[GEORouteInitializerData waypoints] : 8 -> 24
~ _GEORoutePlanningInfoReadAllFrom : 420 -> 436
~ -[GEOETATrafficUpdateResponse _readResponseAttributes] : 204 -> 220
~ -[GEOWaypointRouteFeatures avoidsTolls] : 20 -> 36
~ -[GEORouteInitializerData address] : 16 -> 36
~ _GEOGetGEORouteBuilderLog : 104 -> 100
~ -[GEORoute _readPathMapMatcherInstructions] : 224 -> 212
~ -[_GEOCoordinatePath .cxx_construct] : 32 -> 28
~ __ZN4maps10path_codec4geo314RoutingPathLeg14_InternalParseEPKcPN6google8protobuf8internal12ParseContextE : 1000 -> 984
~ __ZN6google8protobuf8internal24InlineGreedyStringParserEPNSt3__112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEEPKcPNS1_12ParseContextE : 120 -> 136
~ __ZN4maps10path_codec4geo316SupportPointDataC2EPN6google8protobuf5ArenaE : 548 -> 564
~ __ZN6google8protobuf8internal21ReadPackedVarintArrayIZNS1_12VarintParserIiLb1EEEPKcPvS5_PNS1_12ParseContextEEUlyE_EES5_S5_S5_T_ : 200 -> 184
~ __ZN4maps10path_codec4geo310AnchorDataC2EPN6google8protobuf5ArenaE : 180 -> 196
~ __ZN6google8protobuf8internal20RepeatedPtrFieldBase14InternalExtendEi : 312 -> 296
~ __ZN4maps10path_codec4geo310AnchorDataD2Ev : 92 -> 96
~ -[GEOCoordinateArraySupportPoint setLegacyRoadClass:] : 24 -> 36
~ -[GEORecentLocationHistory setLatlngCount:] : 48 -> 64
~ -[GEOETAStep stepID] : 32 -> 20
~ -[GEOComposedETARouteStep setRouteCoordinateRange:] : 8 -> 36
~ +[GEOComposedStringArgument argumentForGeoFormatArgument:] : 440 -> 444
~ -[GEOComposedStringArgument_Duration _initWithGeoFormatArgument:] : 364 -> 360
~ __ZN6google8protobuf11MessageLite15ParseFromStringERKNSt3__112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEE : 160 -> 144
~ __ZN4maps10path_codec4geo315CommonPointData14_InternalParseEPKcPN6google8protobuf8internal12ParseContextE : 560 -> 544
~ __ZN6google8protobuf8internal21ReadPackedVarintArrayIZNS1_12VarintParserIjLb0EEEPKcPvS5_PNS1_12ParseContextEEUlyE_EES5_S5_S5_T_ : 172 -> 188
~ sub_186ef96f8 -> sub_186ef5648 : 52 -> 68
~ __ZN6google8protobuf13RepeatedFieldIyE7ReserveEi : 360 -> 344
~ __ZN4maps10path_codec4geo314CompressedPathD1Ev : 24 -> 28
~ -[GEOCoordinateArraySupportPoint setIndex:] : 28 -> 8
~ -[GEORawPathGeometry pathMatcherInstructions] : 60 -> 80
~ -[GEOComposedRouteCoordinateArray pathsCount] : 20 -> 32
~ sub_186efad74 -> sub_186ef6cd4 : 68 -> 52
~ __ZN4maps10path_codec4geo316RoutingPathPointD2Ev : 204 -> 224
~ _GEONameInfoListIsValid : 512 -> 508
~ -[GEOComposedGuidanceEvent initWithGeoGuidanceEvent:step:legIndex:coordinates:] : 2200 -> 2172
~ -[GEONameInfoList nameInfos] : 84 -> 80
~ -[GEOPDQuickLinkActionDataParams readAll:] : 220 -> 236
~ -[GEOPDRatingCategory readAll:] : 240 -> 256
~ -[GEOPDGroundViewLabel copyWithZone:] : 392 -> 396
~ -[GEOTileCoordinate copyWithZone:] : 232 -> 228
~ -[GEOStorageRouteRequestStorage readAll:] : 196 -> 200
~ -[GEOWaypointID writeTo:] : 756 -> 752
~ -[GEOPDAbout writeTo:] : 308 -> 324
~ -[GEOPDPhotoConstraints writeTo:] : 428 -> 444
~ -[GEOPDEntity copyWithZone:] : 3108 -> 3112
~ -[GEOLocalizedString copyWithZone:] : 372 -> 368
~ -[GEOPDAttribution addAttributionUrl:] : 156 -> 160
~ -[GEOPDCameraMetadata copyWithZone:] : 508 -> 504
~ -[GEOStorageRouteRequestStorage _addNoFlagsWaypoints:] : 144 -> 148
~ -[GEOWaypointID _readFormattedAddressLineHints] : 224 -> 220
~ -[GEOPDBusinessHours _readWeeklyHours] : 188 -> 192
~ -[GEOTimezone copyWithZone:] : 140 -> 136
~ -[GEOPDBounds copyWithZone:] : 496 -> 500
~ -[GEOPDRigMetrics copyWithZone:] : 80 -> 108
~ -[GEOPDAbout addText:] : 132 -> 148
~ -[GEOPDScorecardLayout _addNoFlagsRatingCategory:] : 156 -> 140
~ -[GEOPDQuickLinkActionDataParams copyWithZone:] : 424 -> 440
~ -[GEOPDScorecardLayout addRatingCategory:] : 164 -> 148
~ -[GEOPDStorefrontView .cxx_destruct] : 172 -> 144
~ -[GEOPDPhotoPosition dealloc] : 92 -> 88
~ -[GEOPDHoursThreshold .cxx_destruct] : 48 -> 20
~ -[GEOComposedRouteSegment segmentIndex] : 32 -> 28
~ -[GEOComposedRouteLeg setSegmentRange:] : 20 -> 24
~ +[GEORouteBuilder _guidanceEventsForGeoWaypointRoute:legs:steps:coordinates:] : 1384 -> 1412
~ -[GEOPDSupportsOfflineMaps copyWithZone:] : 176 -> 180
~ -[GEOWaypointID _addNoFlagsFormattedAddressLineHint:] : 148 -> 144
~ -[GEOPDAbout copyWithZone:] : 344 -> 360
~ -[GEOPDRatingCategory _readLocalizedNames] : 192 -> 208
~ -[GEOPDModuleLayoutEntry addModules:] : 156 -> 160
~ -[GEOSearchCategoryStorage copyWithZone:] : 360 -> 356
~ -[GEOStorageRouteRequestStorage .cxx_destruct] : 248 -> 252
~ -[GEOPDRigMetrics dealloc] : 92 -> 88
~ -[GEOPDISO3166Code copyWithZone:] : 464 -> 468
~ -[GEOMapItemInitialRequestData copyWithZone:] : 164 -> 160
~ __geo_URLForDictionary : 1476 -> 1448
~ -[GEOStyleAttribute copyWithZone:] : 200 -> 196
~ -[GEOFormattedString addFormatStyle:] : 144 -> 148
~ -[GEOPDRap copyWithZone:] : 140 -> 168
~ -[GEOPDGroundViewLabelInfo copyWithZone:] : 496 -> 500
~ -[GEOLatLngE7 copyWithZone:] : 144 -> 140
~ -[GEOPDStorefrontPresentation copyWithZone:] : 376 -> 380
~ -[GEOWaypointID copyWithZone:] : 800 -> 796
~ -[GEOPDActionData _addNoFlagsActionLink:] : 140 -> 156
~ -[GEOPDPhotoConstraints copyWithZone:] : 504 -> 488
~ -[GEOURLRouteHandle init] : 104 -> 108
~ -[GEOSearchCategoryStorage init] : 104 -> 120
~ -[GEOPDBrowseCategory copyWithZone:] : 984 -> 964
~ -[GEOPDInlineRapEnablement .cxx_destruct] : 36 -> 40
~ -[GEOMapItemInitialRequestData .cxx_destruct] : 40 -> 36
~ -[GEOFormatStyle .cxx_destruct] : 148 -> 152
~ -[GEOWaypointID .cxx_destruct] : 192 -> 188
~ -[GEOPDAbout .cxx_destruct] : 108 -> 92
~ -[GEOPDPhotoConstraints .cxx_destruct] : 32 -> 48
~ -[GEOURLLocationQueryItem resolvedLocation] : 200 -> 204
~ _MapsFeature_IsEnabled_URLUnification : 32 -> 28
~ -[GEOStep _reserveJunctionElements:] : 268 -> 272
~ -[GEOComposedRouteSegment initWithComposedRoute:stepRange:pointRange:segmentIndex:] : 188 -> 184
~ ___103-[GEOComposedRouteLeg initWithComposedRoute:geoRouteLeg:legIndex:origin:destination:arrivalParameters:]_block_invoke_2 : 112 -> 116
~ +[GEORouteBuilder buildPointSectionsWithSteps:segments:coordinates:] : 1204 -> 1220
~ -[GEOComposedRouteCoordinateArray(Conversions) distanceBetweenIndex:andIndex:] : 92 -> 72
~ _GEOMetersBetweenMapPoints : 256 -> 260
~ +[GEORouteBuilder buildMapRegionFromPointSections:] : 584 -> 580
~ _GEOMapBoxIsNull : 76 -> 80
~ -[GEORouteBuilderOutput setBoundingMapRegion:] : 64 -> 92
~ -[GEOWaypointRoute distanceMeters] : 40 -> 44
~ -[GEORouteBuilderOutput setDistance:] : 32 -> 28
~ -[GEOSignGuidance hasJunctionInfo] : 60 -> 64
~ -[GEOComposedRouteStep maneuverType] : 44 -> 40
~ -[GEOVisualLaneGuidance _addNoFlagsInstruction:] : 132 -> 136
~ +[GEORouteBuilder _cellularCoverageForGeoWaypointRoute:coordinates:] : 1148 -> 1176
~ -[GEOComposedRouteCellularCoverage initWithOffsets:coverage:routeLength:] : 456 -> 460
~ -[GEORouteBuilderOutput setVisualInfos:] : 68 -> 80
~ +[GEOComposedRouteVisualInfo(Internal) visualInfosForRouteLabelsForGeoWaypointRoute:coordinates:] : 720 -> 736
~ -[GEORoute _readRouteNames] : 228 -> 232
~ -[GEORouteBuilderOutput setVisualInfosForRouteNameLabels:] : 84 -> 80
~ -[GEORoute _addNoFlagsRouteCameraInputInfo:] : 156 -> 140
~ -[GEOComposedRouteVisualInfo(Internal) initWithGeoRouteLineStyleInfo:pathIndex:coordinates:distanceOffset:] : 1584 -> 1568
~ -[GEORouteLineStyleInfo _readStyleAttributes] : 216 -> 200
~ -[GEOComposedRouteVisualInfo(Internal) _typeForStyleAttribute:] : 48 -> 52
~ -[GEOComposedRouteCoordinateArray(Conversions) routeCoordinateRangeForPathIndex:] : 288 -> 300
~ -[GEORouteLineStyleInfo endOffsetCm] : 20 -> 24
~ -[GEORouteBuilderOutput setSource:] : 32 -> 28
~ -[GEOComposedRoute _ingestRouteBuilderOutput:] : 688 -> 692
~ -[GEORouteBuilderOutput visualInfosForRouteNameLabels] : 8 -> 36
~ -[GEOAdvisoriesInfo _readGenericAdvisorys] : 208 -> 224
~ -[GEORouteInitializerData anchorPoints] : 12 -> 28
~ -[GEOComposedRoute _initCommuteNotificationStrings:] : 300 -> 304
~ -[GEOWaypointRoute(EnrouteNoticesProvider) _geoTrafficCameras] : 404 -> 400
~ -[GEOWaypointRoute _addNoFlagsTrafficSignal:] : 136 -> 140
~ ___58+[GEOEnrouteNoticesUtil _enrouteNoticesForRoute:provider:]_block_invoke : 480 -> 476
~ -[GEORoutePlanningInfo routeGeniusDescriptions] : 72 -> 76
~ -[GEOComposedWaypointDisplayInfo initWithGeoWaypointInfo:waypoint:] : 148 -> 144
~ -[GEOComposedWaypoint waypoint] : 80 -> 84
~ -[GEOWaypointTyped _readWaypointPlace] : 228 -> 224
~ -[GEOComposedWaypoint _readLatLng] : 200 -> 204
~ -[GEOWaypointPlace _readCenter] : 208 -> 204
~ -[GEORecentLocationHistory dealloc] : 104 -> 108
~ -[GEORouteTrafficBuilder buildTrafficForRoute:etaRoute:] : 160 -> 156
~ -[GEOWaypointInfo _readWaypointCaption] : 224 -> 208
~ -[GEOETATrafficUpdateWaypointRoute .cxx_destruct] : 244 -> 228
~ -[GEOCommonResponseAttributes .cxx_destruct] : 44 -> 28
~ -[GEOETATrafficUpdateWaypointRoute _readTrafficBannerTexts] : 228 -> 212
~ -[GEOComposedRoute dealloc] : 524 -> 528
~ -[GEOMessageLink responseTime] : 124 -> 152
~ -[GEOMapService ticketForBrandLookupWithIMessageUid:traits:] : 184 -> 188
~ -[GEOMessageLink navTintColorString] : 124 -> 120
~ +[GEOFeatureStyleAttributes(PersonalizedItem) workStyleAttributes] : 96 -> 112
~ -[GEOETAResult writeTo:] : 876 -> 864
~ +[GEORouteBuilder _composedRouteSegmentForStartStep:andEndStep:segmentIndex:andCustodian:] : 892 -> 888
~ _GEOArrivalParametersReadSpecified : 1940 -> 1944
~ +[GEORouteBuilder _composedRouteLegForStartStep:endStep:startSegment:endSegment:custodian:geoRouteLeg:legIndex:origin:destination:arrivalParameters:legLength:] : 720 -> 716
~ -[GEODrivingWalkingInstruction _readNormalCommands] : 196 -> 184
~ -[GEOComposedRouteCoordinateArray(Conversions) distanceFromStartToIndex:] : 480 -> 492
~ -[GEOTrafficSignal position] : 88 -> 92
~ -[GEORouteTrafficBuilder buildTrafficForRoute:] : 144 -> 140
~ -[GEORoute _readIncidentEndOffsetsInRoutes] : 228 -> 232
~ -[GEOComposedWaypoint(GEOWaypointExtras) chargingInfo] : 28 -> 24
~ -[GEOComposedRouteLeg geoDestinationWaypointInfo] : 12 -> 16
~ -[GEORouteBuilderOutput .cxx_destruct] : 200 -> 228
~ -[GEORecentLocationHistory .cxx_destruct] : 204 -> 208
~ -[GEOComposedETARoute .cxx_destruct] : 132 -> 128
~ -[GEOArrivalParameters .cxx_destruct] : 148 -> 152
~ -[GEOUUID .cxx_destruct] : 32 -> 44
~ -[GEOETATrafficUpdateWaypointRoute trafficBannerTexts] : 84 -> 100
~ +[GEOFeatureStyleAttributes(PersonalizedItem) homeStyleAttributes] : 96 -> 112
~ -[GEOETAResponse _addNoFlagsEtaResult:] : 144 -> 160
~ -[GEOWaypointInfo name] : 88 -> 72
~ -[GEOETATrafficUpdateResponse clearProblemDetails] : 144 -> 160
~ -[GEOGenericStringData .cxx_destruct] : 92 -> 108
~ __GEOETAResultIsDirty : 128 -> 144
~ -[GEOStep junctionElementsCount] : 56 -> 60
~ -[GEOComposedRouteStep pointRange] : 32 -> 28
~ _GEOMapPoint3DForCoordinate : 52 -> 56
~ _GEOComposedRouteSectionPadAndSquareBounds : 248 -> 244
~ _GEOCoordinate3DForMapPoint : 152 -> 156
~ -[GEORouteBuilderOutput pointSections] : 28 -> 24
~ _GEOVisualLaneGuidanceReadSpecified : 1804 -> 1808
~ +[GEORouteBuilder _isGuidanceEventAtEndOfLeg:] : 40 -> 36
~ -[GEORoute _addNoFlagsEnrouteNotice:] : 148 -> 152
~ -[GEORouteBuilderOutput setGuidanceEvents:] : 72 -> 68
~ -[GEORoute cellularCoverageOffsetAtIndex:] : 220 -> 224
~ +[GEORouteBuilder _visualInfosForGuidanceEvents:steps:coordinates:] : 712 -> 724
~ +[GEOComposedRouteVisualInfo(Internal) visualInfosForGeoWaypointRoute:coordinates:updateable:] : 336 -> 352
~ -[GEORoute _readRouteLineStyleInfos] : 212 -> 228
~ +[GEOComposedRouteVisualInfo(Internal) _infosForRouteLineStyleInfos:pathIndex:coordinates:updateable:] : 428 -> 412
~ -[GEORoute routeNames] : 96 -> 80
~ +[GEOComposedRouteVisualInfo(Internal) cameraInfosForGeoWaypointRoute:coordinates:updateable:] : 328 -> 344
~ -[GEORouteLineStyleInfo _readLaneChangeInfos] : 200 -> 220
~ -[GEOComposedRouteCoordinateArray(Conversions) routeCoordinateForDistanceAfterStart:] : 16 -> 28
~ -[GEORoute _readElevationProfile] : 228 -> 232
~ -[GEORouteBuilderOutput legs] : 20 -> 36
~ -[GEOComposedRouteCoordinateArray(Zilch) usesZilch] : 12 -> 28
~ -[GEORouteBuilderOutput cameraInfos] : 24 -> 20
~ -[GEOWaypointRoute _readRestrictionZoneInfo] : 216 -> 220
~ -[GEORouteRestrictionZoneInfo initWithGeoWaypointRoute:] : 504 -> 500
~ _GEOAdvisoriesInfoReadSpecified : 2028 -> 2032
~ +[GEOEnrouteNoticesUtil createEnrouteNoticesForComposedRoute:routeInitializerData:] : 280 -> 276
~ -[GEOWaypointRoute trafficCameras] : 72 -> 76
~ -[GEOWaypointRoute(EnrouteNoticesProvider) _geoTrafficSignals] : 416 -> 412
~ -[GEOTrafficSignal _readIdentifier] : 200 -> 204
~ +[GEOEnrouteNoticesUtil _forEachGeoEnrouteNoticeOnRoute:handler:] : 456 -> 484
~ -[GEORoutePlanningInfo _readRouteGeniusDescriptions] : 212 -> 216
~ -[GEORouteTrafficBuilder _buildTrafficForRoute:toDistance:] : 1368 -> 1364
~ -[GEORoute _readTrafficColorOffsets] : 212 -> 216
~ -[GEOComposedRouteTraffic _incidentsForRoute:] : 1128 -> 1124
~ -[GEOComposedRouteLeg geoOriginWaypointInfo] : 12 -> 16
~ -[GEOComposedWaypointDisplayInfo _initPositionWithGeoWaypointInfo:waypoint:] : 404 -> 400
~ -[GEOWaypointRoute _readInitialPromptTypes] : 216 -> 220
~ -[GEOComposedETARoute uniqueRouteID] : 28 -> 24
~ -[GEOComposedRouteMutableData updateForRoute:etaRoute:] : 1308 -> 1312
~ -[GEOComposedETARouteLeg .cxx_destruct] : 116 -> 112
~ -[GEOComposedRoute geoWaypointRoute] : 12 -> 16
~ -[GEOComposedETARoute length] : 28 -> 8
~ -[GEOETATrafficUpdateWaypointRoute routeLegs] : 80 -> 96
~ -[GEORoute trafficColorOffsets] : 76 -> 60
~ -[GEOETARoute trafficColorOffsets] : 64 -> 48
~ -[GEOComposedRouteLeg distance] : 8 -> 12
~ -[GEOComposedRouteTrafficColorInfo setOffsetMeters:] : 36 -> 32
~ -[GEOComposedRoute coordinateAtOffset:] : 12 -> 16
~ -[GEOComposedRouteTraffic _incidentsForRoute:etaRoute:] : 1192 -> 1172
~ -[GEOETATrafficUpdateWaypointRoute _readIncidentsOnUserWaypointRoutes] : 220 -> 204
~ _GEONavigabilityInfoReadAllFrom : 1100 -> 1116
~ -[GEOETARoute _readIncidentEndOffsetsInETARoutes] : 216 -> 200
~ -[GEOComposedRoute routeInitializerData] : 76 -> 60
~ -[GEORouteInitializerData directionsResponse] : 12 -> 32
~ -[GEOComposedRouteTraffic .cxx_destruct] : 92 -> 104
~ +[GEOComposedRouteVisualInfo(Internal) visualInfosForRoute:etaRoute:] : 1084 -> 1104
~ -[GEOComposedETARouteLeg length] : 12 -> 24
~ -[GEOETARoute _readRouteCameraInputInfos] : 220 -> 208
~ -[GEOComposedWaypointDisplayInfo setWaypointInfo:] : 504 -> 500
~ -[GEOWaypointInfo hasWaypointCaption] : 60 -> 76
~ -[GEOETATrafficUpdateResponse dealloc] : 100 -> 84
~ -[GEOTraversalTimes .cxx_destruct] : 48 -> 32
~ -[GEOETAStep .cxx_destruct] : 152 -> 168
~ -[GEOWaypointRouteFeatures .cxx_destruct] : 48 -> 20
~ -[GEOComposedETARoute geoTrafficBannerTexts] : 72 -> 68
~ -[GEONavigationProxy setTrafficForCurrentRoute:] : 120 -> 124
~ -[GEOComposedRouteSegment setComposedRoute:] : 12 -> 40
~ -[GEOComposedRoute .cxx_destruct] : 1068 -> 1040
~ -[GEOComposedStringArgument_Distance .cxx_destruct] : 92 -> 88
~ -[GEOComposedStringArgument .cxx_destruct] : 96 -> 68
~ -[GEOComposedStringArgument_Duration .cxx_destruct] : 92 -> 88
~ -[GEOComposedRouteMutableData .cxx_destruct] : 188 -> 192
~ -[GEOComposedWaypointDisplayInfo .cxx_destruct] : 152 -> 132
~ -[GEOComposedRouteVisualInfo .cxx_destruct] : 156 -> 172
~ -[GEOComposedRouteCellularCoverage .cxx_destruct] : 80 -> 84
~ -[GEORouteRestrictionZoneInfo .cxx_destruct] : 40 -> 36
~ -[GEOVehicleInfo writeTo:] : 188 -> 172
~ -[GEOETAStep readAll:] : 268 -> 252
~ -[GEOComposedDrivingRouteStep .cxx_destruct] : 44 -> 48
~ -[GEOComposedRouteSegment .cxx_destruct] : 28 -> 24
~ -[GEOComposedRouteLeg .cxx_destruct] : 172 -> 176
~ -[GEOComposedRouteSection .cxx_destruct] : 88 -> 72
~ -[_GEOCoordinatePath .cxx_destruct] : 132 -> 144
~ -[GEOTripInfo writeTo:] : 152 -> 140
~ -[GEOCoordinateArraySupportPoint .cxx_destruct] : 24 -> 20
~ __GEOETAStepIsDirty : 128 -> 112
~ -[GEOStep readAll:] : 216 -> 220
~ -[GEONameInfo readAll:] : 200 -> 196
~ -[GEOWaypointRoute readFrom:] : 20 -> 40
~ -[GEOCoordinateArraySupportPoint initWithCoder:] : 424 -> 404
~ -[GEOComposedRouteLeg setRoute:] : 40 -> 12
~ -[GEOComposedRouteSegment initWithCoder:] : 248 -> 244
~ -[GEOComposedDrivingRouteStep initWithCoder:] : 184 -> 188
~ -[GEOComposedRouteStep initWithCoder:] : 604 -> 600
~ -[GEOComposedGuidanceEvent initWithCoder:] : 1332 -> 1336
~ -[GEOComposedStringArgument_Distance initWithCoder:] : 308 -> 304
~ -[GEOComposedRouteCellularCoverage initWithCoder:] : 312 -> 296
~ -[GEOComposedRouteVisualInfo initWithCoder:] : 756 -> 776
~ -[GEOStyleAttributes readFrom:] : 16 -> 12
~ -[GEOPBTransitArtwork readFrom:] : 36 -> 40
~ +[GEOComposedStringArgument_Distance supportsSecureCoding] : 16 -> 28
~ -[GEORouteInitializerData initWithCoder:] : 548 -> 536
~ -[GEODirectionsResponse readFrom:] : 32 -> 28
~ -[GEOComposedRouteMutableData initWithCoder:] : 672 -> 676
~ -[GEOComposedETARouteStep initWithCoder:] : 288 -> 268
~ -[GEOETATrafficUpdateWaypointRoute readFrom:] : 36 -> 20
~ ___35-[GEOComposedRoute setMutableData:]_block_invoke : 88 -> 60
~ -[GEOComposedRouteTraffic(Deprecated) trafficColorOffsets] : 324 -> 320
~ -[GEOComposedRoute waypointDisplayInfoForWaypoint:] : 508 -> 512
~ __GEOWaypointPlaceCallReadAllRecursiveWithoutSynchronized : 312 -> 308
~ -[GEOComposedRouteMutableData destinationDisplayInfoForLeg:] : 116 -> 120
~ -[GEOComposedWaypoint(GEOWaypointExtras) styleAttributes] : 296 -> 292
~ -[GEOFeatureStyleAttributes featureStyleAttributes] : 20 -> 24
~ -[GEOComposedWaypointDisplayInfo waypointCaption] : 24 -> 20
~ -[GEOComposedRoute visualInfosForRouteNameLabels] : 32 -> 36
~ sub_186f6b730 -> sub_186f67734 : 600 -> 596
~ sub_186f7a390 -> sub_186f76390 : 80 -> 68
~ sub_186f7abfc -> sub_186f76bf0 : 96 -> 112
~ sub_186f81ba8 -> sub_186f7dbac : 360 -> 372
~ sub_186faac10 -> sub_186fa6c20 : 60 -> 76
~ -[GEOPDMIFAutocompleteRequest _initWithDictionary:isJSON:] : 4492 -> 4576
~ -[GEOPDClientMetadata _initWithDictionary:isJSON:] : 7816 -> 7984
~ -[GEOPDClientMetadata StringAsClientRevisions:] : 892 -> 976
~ -[GEOPDClientMetadata StringAsClientRevision:] : 892 -> 976
~ -[GEOPDComponentFilter(PlaceDataExtras) initEntityFilterWithSpokenNames] : 208 -> 188
~ sub_1885b0648 -> sub_1885ac7f8 : 76 -> 60
~ -[GEOSearchResultSection init] : 64 -> 68
~ __ZN3geo7MapNodeD1Ev : 16 -> 28
CStrings:
+ "CLIENT_REVISION_CAN_SHOW_AUTO_GENERATED_GUIDES"
+ "CLIENT_REVISION_CAN_SUPPORT_ENRICHMENT_ORGANIC_DUPE"
+ "CLIENT_REVISION_CAN_SUPPORT_RICH_LAYOUT_PLACE_SUGGESTIONS_SEARCH_HOME_WITH_GUIDE_VIEW"
```
