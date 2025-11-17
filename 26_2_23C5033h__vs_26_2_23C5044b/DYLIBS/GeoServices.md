## GeoServices

> `/System/Library/PrivateFrameworks/GeoServices.framework/GeoServices`

```diff

-2027.32.10.2.4
-  __TEXT.__text: 0x18c0b6c
+2027.32.10.2.10
+  __TEXT.__text: 0x18c08b8
   __TEXT.__auth_stubs: 0x41d0
   __TEXT.__objc_methlist: 0xdf434
   __TEXT.__const: 0x82557
-  __TEXT.__gcc_except_tab: 0x99454
+  __TEXT.__gcc_except_tab: 0x99458
   __TEXT.__cstring: 0xa4d06
   __TEXT.__dlopen_cstrs: 0x289
   __TEXT.__swift5_typeref: 0xe0c

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 7FAAE199-DC0D-3A52-B435-B620A4E0DDEF
+  UUID: 51F507B2-18D6-3949-AE95-4C95AD95EFD2
   Functions: 101911
   Symbols:   288813
   CStrings:  98648
Functions:
~ _getNRPairedDeviceRegistryClass : 236 -> 244
~ __getMetadataStruct : 176 -> 160
~ _GEODefaultsDomain : 76 -> 92
~ +[_GEOCountryConfigurationInfo get] : 168 -> 152
~ ___GEODefaultsDomain_block_invoke : 28 -> 48
~ ____registerStateCaptureCallbacks_block_invoke : 48 -> 44
~ __GEOReadStoredCountryCodeWithFallback : 180 -> 196
~ __GEOConfigProxy : 92 -> 108
~ -[_GEOCountryConfigurationInfo countryCode] : 32 -> 16
~ _GEOConfig_splitKeyPathComponents : 396 -> 372
~ _GEOFindOrCreateLog : 268 -> 260
~ ____GEOConfigProxy_block_invoke : 124 -> 132
~ __GEOConfigStorageDirectSystemReadOnly : 64 -> 56
~ __GEOConfigOptionsForDefaultsSource : 52 -> 60
~ -[GEOFilePaths init] : 168 -> 160
~ -[GEOConfigRemoteProxy init] : 180 -> 164
~ -[GEOPlatform hardwareIdentifier] : 92 -> 84
~ -[GEOMapService _loadOverriddenResultProviderID] : 64 -> 40
~ ___33-[GEOPlatform hardwareIdentifier]_block_invoke : 136 -> 128
~ ___45-[GEONavigationListener requestGuidanceState]_block_invoke : 104 -> 112
~ _GEOConfigGetBOOL : 84 -> 76
~ -[GEOABAssignmentResponse _readClientConfig] : 204 -> 228
~ __GEOGetConfigStorageRemote : 88 -> 96
~ _GeoServicesConfig_DebugActiveExperimentBranch_Metadata_block_invoke_357 : 36 -> 12
~ +[GEOExperimentConfiguration sharedConfiguration] : 100 -> 92
~ +[GEONetworkDefaults sharedNetworkDefaults] : 164 -> 188
~ _GEOConfig_getCountryAwareValueForKeyFromDictionary : 680 -> 696
~ ____getValue_block_invoke : 588 -> 580
~ +[GEOResourceManifestManager modernManager] : 96 -> 84
~ ___daemonXPCUtilIsolater_block_invoke : 76 -> 64
~ -[GEOPlatform supportsMultiUser] : 80 -> 72
~ +[GEOFilePaths _internal_geoServicesCacheDirectoryPath] : 164 -> 188
~ __GEODefaultsServerConnection : 196 -> 204
~ ___GEOGetGEOFilePathsLog_block_invoke : 80 -> 88
~ ___32-[GEOPlatform supportsMultiUser]_block_invoke : 40 -> 64
~ ____initStorageReadOnly_block_invoke : 400 -> 376
~ +[GEOPlatform isRunningInGeod] : 32 -> 24
~ -[GEOConfigStorageDirectReadOnly _readStore] : 860 -> 888
~ -[GEOConfigStorageExpiryCached resync] : 148 -> 172
~ _daemonXPCUtilIsolater : 84 -> 88
~ ____GEODefaultsServerConnection_block_invoke : 112 -> 120
~ -[GEOConfigStorageClient _init] : 56 -> 76
~ +[GEOXPCRequest reportsProgress] : 28 -> 8
~ _GEOSetThrottleToken : 168 -> 156
~ +[GEOXPCConnection daemonXPCConnectionCreationBlock] : 180 -> 188
~ +[GEOConfigGetExpiringKeysRequest replyClass] : 28 -> 20
~ -[GEOXPCConnection _reconnectIsolated] : 316 -> 324
~ -[GEOConfigGetExpiringKeysRequest keyOptions] : 28 -> 40
~ -[_GEOConfigKeyHelper _lookupKeyProperties] : 128 -> 120
~ _GeoServicesConfig_DeviceCountryCodeSourced_Metadata_block_invoke_66 : 20 -> 28
~ ___43-[_GEOConfigKeyHelper _lookupKeyProperties]_block_invoke : 196 -> 188
~ __GEOAddChangeListenerForKeys : 184 -> 180
~ -[GEOConfigAddChangeListenerRequest reply] : 28 -> 32
~ _GeoServicesConfig_TransactionsForPeers_Metadata_block_invoke_185 : 32 -> 28
~ +[GEOServer wantsPerMessageSignposts] : 24 -> 20
~ _GEOConfig_migrateEntitledKey : 296 -> 312
~ __GEOConfigStorageExpirySystem : 84 -> 104
~ -[_GEOServerProxy server] : 24 -> 36
~ -[GEOApplicationAuditToken bundleId] : 172 -> 160
~ -[GEOPeer auditToken] : 12 -> 24
~ -[GEOApplicationAuditToken initCommon] : 112 -> 136
~ _AppSupportLibraryCore : 320 -> 328
~ ___Block_byref_object_dispose_ : 28 -> 16
~ -[GEOConfigAddChangeListenerRequest .cxx_destruct] : 20 -> 24
~ -[GEOResourceManifestConfiguration init] : 152 -> 160
~ -[GEOPlatform deviceScreenScale] : 88 -> 100
~ -[GEOXPCReply .cxx_destruct] : 112 -> 132
~ -[GEOLocalizationRegionsInfo init] : 92 -> 116
~ __GEOConfigStorageDirectUserReadOnly : 60 -> 48
~ -[GEOXPCRequest preferredAuditToken] : 36 -> 12
~ -[GEOConfigGetExpiringKeysReply expiringKeys] : 44 -> 40
~ __directStoreForSource : 140 -> 168
~ -[GEOXPCReply error] : 20 -> 8
~ _GEOConfigGetArray : 32 -> 44
~ -[GEOXPCReply replyDictionary] : 100 -> 76
~ ___38-[GEOConfigStorageExpiryCached resync]_block_invoke : 136 -> 132
~ __GEOGetAllValuesInStore : 340 -> 356
~ ___42-[GEOConfigPersistence getAllExpiringKeys]_block_invoke : 80 -> 100
~ -[GEOConfigGetExpiringKeysReply .cxx_destruct] : 20 -> 48
~ _GEOConfig_pruneEntitledKeysForAuditToken : 636 -> 652
~ ____geoDefaultsToDict_block_invoke : 220 -> 236
~ ___GEOConfig_splitKeyPathComponents_block_invoke : 56 -> 60
~ -[GEOConfigGetAllValueInStoreReply isValid] : 20 -> 32
~ ___52+[GEOApplicationAuditToken currentProcessAuditToken]_block_invoke : 180 -> 172
~ +[GEOOfflineService stateManagerClass] : 100 -> 108
~ __GEOConfigStorageUser : 92 -> 108
~ -[GEOConfigStorageCached resync] : 224 -> 232
~ -[GEOConfigStorageDirectReadOnly resync] : 28 -> 24
~ -[GEOConfigGetAllValueInStoreReply keyStringsAndValues] : 36 -> 32
~ ____GEOGetConfigStorageRemote_block_invoke : 76 -> 60
~ -[GEOExperimentConfiguration init] : 252 -> 240
~ -[GEOConfigGetAllValueInStoreReply .cxx_destruct] : 44 -> 24
~ _GEOExperimentConfigurationPath : 16 -> 40
~ _GEOABAssignmentResponseReadAllFrom : 408 -> 416
~ -[_GEOLocationShifterRemoteProxy isLocationShiftEnabled] : 952 -> 944
~ -[GEOResourceManifestManager hasLoadedActiveTileGroup] : 76 -> 84
~ -[_GEOLocationShiftLocation latLng] : 16 -> 20
~ -[GEOLatLng(GEOProtoExtras) coordinate] : 68 -> 64
~ -[_GEOLocationShiftLocation accuracy] : 12 -> 28
~ -[GEONavdDefaults minimumDistanceToConsiderLeechedLocationInMeters] : 44 -> 20
~ _GeoServicesConfig_NavdMinimumDistanceToConsiderLeechedLocation_Metadata_block_invoke_280 : 12 -> 20
~ -[_GEOLocationShiftLocation .cxx_destruct] : 152 -> 144
~ _GeoServicesConfig_TerritoryRegulatoryMinimumRadius_Metadata_block_invoke_434 : 36 -> 16
~ -[GEOGeographicMetadataRequester _fetch] : 708 -> 696
~ _GeoServicesConfig_TerritoryRegulatoryAssetIsShiftedInChina_Metadata_block_invoke_432 : 40 -> 20
~ -[GEOGeographicMetadataRequester location] : 128 -> 148
~ _GEOActiveTileGroupPath : 104 -> 108
~ _GEOActiveTileGroupReadAllFrom : 412 -> 408
~ _GEOActiveTileGroupReadSpecified : 12656 -> 12660
~ sub_1866655ac -> sub_18663d668 : 412 -> 404
~ _SearchFoundationLibrary : 280 -> 284
~ _GEOResourceCachesDirectory : 76 -> 84
~ ____geoDefaultsToArray_block_invoke : 304 -> 288
~ _GEOGetNetworkRequestLog : 100 -> 84
~ -[NSURLSessionConfiguration(GEOExtras) _geo_setTLSMinimumSupportedProtocolVersion] : 460 -> 452
~ _GeoServicesConfig_MinTLSVersion_Metadata_block_invoke_74 : 40 -> 16
~ -[GEORequestCounterLocalProxy countersEnabled] : 40 -> 32
~ _GeoServicesConfig_RequestCounterEnabledDefault_Metadata_block_invoke_250 : 16 -> 40
~ _GEODataRequestKindToNWActivityLabel : 400 -> 408
~ _GEOGetThrottleToken : 124 -> 144
~ _GEODecodeXPCValue : 212 -> 220
~ -[GEOMessage userInfo] : 12 -> 16
~ _GeoServicesConfig_CustomEnvironmentConfiguration_Metadata_block_invoke_49 : 36 -> 12
~ -[GEOPlatform osVersion] : 108 -> 100
~ __networkDefaultsURL : 624 -> 632
~ ____GEOGetURLWithSource_block_invoke : 368 -> 364
~ -[GEOActiveTileGroup urlInfoSet] : 64 -> 68
~ sub_186667fc0 -> sub_186640060 : 284 -> 280
~ -[GEOActiveTileGroup _readUrlInfoSet] : 216 -> 220
~ _GEOApplicationIdentifierOrProcessName : 84 -> 108
~ _GeoOfflineConfig_CohortAllowList_Metadata_block_invoke : 28 -> 36
~ ____GEOConfigAddBlockListenerForKey_block_invoke : 472 -> 464
~ _GeoServicesConfig_ShouldAlwaysUpdateNetworkDefaultsAtLaunch_Metadata_block_invoke_225 : 16 -> 36
~ _GEOXPCErrorFromReply : 352 -> 360
~ -[GEOMessage _endSignpost] : 256 -> 268
~ __GEOConfigStorageSystem : 92 -> 84
~ ___30-[GEOMapService defaultTraits]_block_invoke : 1720 -> 1728
~ -[GEOMapServiceTraits transitScheduleFilter] : 88 -> 80
~ _GeoServicesConfig_DefaultTimeFilterDuration_Metadata_block_invoke_243 : 32 -> 40
~ ___GEOApplicationIdentifierOrProcessName_block_invoke : 312 -> 336
~ _GeoServicesConfig_OverriddedResultProviderID_Metadata_block_invoke_142 : 28 -> 36
~ -[GEOTraitsTransitScheduleFilter _readLowFrequencyFilter] : 208 -> 200
~ ___30-[GEOMapService defaultTraits]_block_invoke.55 : 96 -> 104
~ -[GEOTraitsTransitScheduleFilter lowFrequencyFilter] : 88 -> 80
~ _GeoServicesConfig_DefaultBrandFallbackSupport_Metadata_block_invoke_351 : 20 -> 28
~ _MapsFeaturesConfig_RemoteFeatureFlags_Metadata_block_invoke : 20 -> 12
~ _GeoServicesConfig_ClientAuthFeatureFlagsStateInfo_Metadata_block_invoke_400 : 28 -> 36
~ ___31-[GEOPlatform deviceCountrySKU]_block_invoke : 76 -> 68
~ _GeoServicesConfig_SKURegionsServiceAllowlist_Metadata_block_invoke_396 : 20 -> 28
~ ___71+[GEOAdditionalEnabledMarkets(GEOProtoExtras) additionalEnabledMarkets]_block_invoke : 116 -> 136
~ -[GEOAdditionalEnabledMarkets init] : 120 -> 100
~ -[GEOAdditionalEnabledMarkets(GEOProtoExtras) reload] : 284 -> 272
~ -[GEOAdditionalEnabledMarkets clearTransitMarkets] : 148 -> 128
~ +[GEOAdditionalEnabledMarkets(GEOProtoExtras) _additionalEnabledTransitMarkets] : 256 -> 248
~ _GeoServicesConfig_AdditionalTransitMarkets_Metadata_block_invoke_354 : 28 -> 36
~ -[GEOMapServiceTraits hasTimeSinceMapEnteredForeground] : 44 -> 36
~ _GeoServicesConfig_PlaceDataDebugAPI_Metadata_block_invoke_119 : 8 -> 16
~ -[GEOMapServiceTraits knownClientResolvedTypesCount] : 76 -> 68
~ _GeoServicesConfig_BusinessChatPreflightIdentifiers_Metadata_block_invoke_129 : 12 -> 20
~ -[GEOMapServiceTraits hasCurrentLocaleCurrencySymbol] : 60 -> 84
~ ___GEOIsFeatureActive_block_invoke : 184 -> 160
~ _GEOConfigGetSet : 48 -> 40
~ ___GEOIsFeatureActive_block_invoke_5 : 72 -> 84
~ -[GEOPDClientMetadata _readClientRevisions] : 228 -> 224
~ _MapsFeaturesConfig_MyPlacesFeatures_Metadata_block_invoke_47 : 20 -> 24
~ -[GEOPDClientMetadata _readSupportedElevationModels] : 212 -> 208
~ -[GEOLocation .cxx_destruct] : 172 -> 164
~ _GEOCanonicalResourceNameAndVersionForVersionedName : 1268 -> 1272
~ -[GEOActiveTileGroup _readActiveResources] : 208 -> 212
~ -[GEOResourceFetchRequest .cxx_destruct] : 112 -> 104
~ -[GEOResource _readFilename] : 228 -> 204
~ __ZNSt3__119__shared_weak_count16__release_sharedB8ne200100Ev : 116 -> 108
~ -[GEOResource init] : 120 -> 108
~ _GEOResourceReadSpecified : 3856 -> 3860
~ -[GEOURLInfo url] : 44 -> 20
~ _GEOResourcesPath : 104 -> 100
~ __GEOResourceCallReadAllRecursiveWithoutSynchronized : 260 -> 272
~ -[GEOResourceFetchRequest manifestConfiguration] : 36 -> 28
~ -[GEOResource _readChecksum] : 228 -> 208
~ -[GEORegionalResourceSet resources] : 80 -> 68
~ -[GEOResource resourceType] : 132 -> 104
~ -[GEOActiveTileGroup _readRegionalResources] : 212 -> 232
~ -[GEOURLInfoSet _readResourcesURL] : 232 -> 208
~ _GeoServicesConfig_AlternateResourceURLs_Metadata_block_invoke_62 : 20 -> 16
~ -[GEOResource hash] : 472 -> 480
~ -[GEOActiveTileGroup regionalResources] : 76 -> 84
~ -[GEORegionalResourceSet _readResources] : 224 -> 204
~ -[GEOURLInfoSet resourcesURL] : 68 -> 84
~ -[GEOURLInfoSet(Extras) alternateResourcesNSURLs] : 308 -> 292
~ -[GEOURLInfoSet alternateResourcesURLs] : 88 -> 72
~ -[GEOURLInfoSet(Extras) resourcesProxyURL] : 204 -> 216
~ ___GEODataRequestTimeout_block_invoke.254 : 48 -> 36
~ _GEOAuthProxyEnabledForURLInfoSet : 208 -> 200
~ _GeoServicesConfig_MapsAuthUseProxy_Metadata_block_invoke_123 : 40 -> 32
~ -[GEOURLInfoSet _readAuthProxyURL] : 208 -> 204
~ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC1B8ne200100ILi0EEEPKc : 196 -> 184
~ __ZNSt3__16__treeINS_12__value_typeIiN6gloria9ShardInfoEEENS_19__map_value_compareIiS4_NS_4lessIiEELb1EEENS_9allocatorIS4_EEE7destroyEPNS_11__tree_nodeIS4_PvEE : 164 -> 156
~ -[GEOResource dealloc] : 80 -> 76
~ -[GEOResource .cxx_destruct] : 156 -> 168
~ __ZNSt3__120__shared_ptr_emplaceIN6gloria12DbReaderDiskENS_9allocatorIS2_EEE21__on_zero_shared_weakEv : 24 -> 16
~ _GEOGetGeographicMetadataLog : 108 -> 84
~ __ZNSt3__127__tree_balance_after_insertB8ne200100IPNS_16__tree_node_baseIPvEEEEvT_S5_ : 424 -> 416
~ -[GEOResource validationMethod] : 124 -> 104
~ _GEOGetSHA1FromExtendedAttributes : 216 -> 204
~ -[GEOResourceLoader _cleanup] : 316 -> 324
~ -[GEOResourceFetchReply paths] : 16 -> 32
~ -[GEOGloriaDB .cxx_construct] : 36 -> 20
~ __ZN6gloria16BasicShardHeader8ReadFromERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE : 728 -> 720
~ -[GEOResourceLoader .cxx_destruct] : 248 -> 256
~ -[GEOReportedProgress .cxx_destruct] : 96 -> 120
~ -[GEOResourceInfo .cxx_destruct] : 80 -> 88
~ __ZNSt3__113basic_fstreamIcNS_11char_traitsIcEEEC1ERKNS_12basic_stringIcS2_NS_9allocatorIcEEEEj : 380 -> 392
~ __ZL20_GEOEclipticLatitude16GEOCelestialBodydb : 3964 -> 3968
~ -[NSDate(GEOCelestial) geo_julianDay] : 56 -> 72
~ __ZN16CAADynamicalTime6DeltaTEd : 1944 -> 1956
~ __ZL21_GEOEclipticLongitude16GEOCelestialBodydb : 4240 -> 4260
~ __ZN27CAACoordinateTransformation21Equatorial2HorizontalEddd : 196 -> 208
~ -[GEOHorizontalCelestialBodyData altitude] : 20 -> 32
~ __ZN22GEOFunctionInterceptor12nextMaxOrMinEb : 156 -> 176
~ -[GEOCelestialRiseTransitSet _numberOfEvents] : 32 -> 52
~ __ZN7CAADate8DateToJDElldb : 196 -> 188
~ __ZN22GEOFunctionInterceptor7getPeakEi : 160 -> 168
~ __ZN11CAANutation19NutationInObliquityEd : 612 -> 604
~ __ZNKSt3__110__function6__funcIPFddENS_9allocatorIS3_EES2_E7__cloneEPNS0_6__baseIS2_EE : 64 -> 40
~ __ZN8CAAEarth12RadiusVectorEdb : 608 -> 620
~ __ZL16_GEORadiusVector16GEOCelestialBodydb : 3572 -> 3592
~ __ZN11CAASidereal25MeanGreenwichSiderealTimeEd : 304 -> 296
~ __ZN17GEORiseTransitSet11eventOfTypeEj : 1536 -> 1512
~ __ZN7CAAMoon12RadiusVectorEd : 684 -> 696
~ __ZL17getRightAscensionPdS_d16GEOCelestialBodyb : 172 -> 192
~ __ZN7CAAMoon16EclipticLatitudeEd : 1012 -> 992
~ -[GEOCelestialRiseTransitSet _oldestEventInJulianDay] : 148 -> 136
~ __ZNSt3__16vectorI25CAARiseTransitSetDetails2NS_9allocatorIS1_EEE9push_backB8ne200100ERKS1_ : 324 -> 316
~ -[_GEOThrottlerLong expiresAt] : 32 -> 24
~ _GEOConfig_getRequiredEntitlement : 180 -> 176
~ -[GEOCelestialRiseTransitSet .cxx_destruct] : 92 -> 84
~ -[GEOPDClientMetadata .cxx_destruct] : 424 -> 412
~ -[GEOLunarEvent .cxx_destruct] : 16 -> 36
~ -[GEOCelestialEphemeris equatorialCoord] : 100 -> 112
~ -[GEOLunarEvent date] : 12 -> 32
~ -[GEOCelestialEphemeris radiusVector] : 116 -> 128
~ _GeoServicesConfig_LocalizationCapabilitiesSupportedPhoneticTypes_Metadata_block_invoke_388 : 32 -> 8
~ -[GEOMapServiceTraits _readCurrentLocaleCurrencySymbol] : 228 -> 220
~ -[GEOLocationShiftingEnabledRequest isValid] : 24 -> 32
~ _GEOURLString : 16 -> 40
~ _GeoServicesConfig_VoltairePolyLocationShiftURL_Metadata_block_invoke_14 : 12 -> 36
~ -[GEOURLInfoSet _readPolyLocationShiftURL] : 224 -> 232
~ -[GEOLocationShiftingEnabledResponse enabled] : 24 -> 32
~ -[GEOLocation latLng] : 88 -> 80
~ -[GEOLocationShiftingEnabledResponse isValid] : 20 -> 28
~ -[GEOLocation _readLatLng] : 220 -> 232
~ ___56+[GEOFilePathsPrivate daemonContainerPathUsingLibSystem]_block_invoke : 164 -> 140
~ -[GEOMapsAuthServiceHelper init] : 184 -> 196
~ -[GEOLocation _readRawCoordinate] : 212 -> 224
~ +[GEOFilePathsPrivate userContainerCachesPathUsingLibSystem] : 12 -> 24
~ +[GEOFilePaths dictionaryRepresentation] : 756 -> 744
~ +[GEOFilePathsPrivate userContainerLibPathUsingLibSystem] : 24 -> 36
~ -[GEOResourceManifestManager hasResourceManifest] : 132 -> 128
~ -[GEOMapsAuthServiceHelper _hasMAT] : 116 -> 120
~ _GeoServicesConfig_MapsAuthToken_Metadata_block_invoke_121 : 8 -> 36
~ -[GEOMapsAuthServiceHelper _hasMRT] : 96 -> 100
~ _GeoServicesConfig_MapsRefreshToken_Metadata_block_invoke_122 : 24 -> 32
~ __setDefaultNonRecursive : 1096 -> 1112
~ _GEOConfig_keyRequiresEntitlement : 24 -> 40
~ _GEOConfigSetDictionary : 32 -> 16
~ _GEOConfig_createEntitledKeyPathForKey : 376 -> 360
~ -[_GEOConfigDBOperationQueue scheduleTimer] : 84 -> 104
~ -[GEOPeer connection] : 8 -> 12
~ __GEOConfigPostKeysChangedNotification : 328 -> 320
~ __GEOConfigOptionsUseClientCache : 76 -> 92
~ ____notifyListenersOfKeyChange_block_invoke_2 : 44 -> 28
~ ____GEODefaultsServerConnection_block_invoke_2 : 968 -> 964
~ ___38-[GEOXPCConnection _reconnectIsolated]_block_invoke : 344 -> 320
~ -[GEOConfigKeyChangeNotification keyOptions] : 40 -> 20
~ -[GEOCountryConfiguration updateProvidersForCurrentCountry] : 12 -> 28
~ -[_GEOCountryConfigurationRemoteProxy _xpcConnection] : 36 -> 52
~ -[_GEOCountryConfigurationUpdateHandler .cxx_destruct] : 80 -> 72
~ _GeoServicesConfig_MapsAuthClientFeatureFlagsLastUpdated_Metadata_block_invoke_406 : 24 -> 32
~ ___49-[_GEOConfigChangedDelegateListener callListener]_block_invoke : 20 -> 32
~ ___35-[GEOXPCConnection _barrierIsReady]_block_invoke : 96 -> 100
~ ____scheduleResync_block_invoke : 404 -> 420
~ ____initKeyChangeListeners_block_invoke_3 : 332 -> 352
~ -[GEOConfigKeyChangeNotification isValid] : 108 -> 88
~ -[GEOClientNetworkMetrics .cxx_destruct] : 132 -> 144
~ ___35-[GEOXPCConnection _barrierIsReady]_block_invoke_2 : 40 -> 20
~ ___55-[_GEONetworkDefaultsLocalProxy _updateNetworkDefaults]_block_invoke_2 : 512 -> 532
~ sub_186685d58 -> sub_18665de64 : 500 -> 488
~ -[_GEOLocalRequestCounterTicket .cxx_destruct] : 36 -> 20
~ _GEOErrorToCounterInfoResult : 300 -> 288
~ -[GEORequestCountPowerLogger _readFromDisk] : 1060 -> 1056
~ ___33-[GEOPlatform clientCapabilities]_block_invoke : 712 -> 700
~ -[GEOClientCapabilities formattedStringClientCapabilities] : 64 -> 68
~ _GeoServicesConfig_NavdShouldRequestJunctionView_Metadata_block_invoke_272 : 20 -> 16
~ -[GEOClientCapabilities _readSupportsMultipointRoutings] : 224 -> 204
~ _MapsFeaturesConfig_Maps182_Metadata_block_invoke_53 : 28 -> 16
~ -[GEOFormattedStringClientCapabilities .cxx_destruct] : 48 -> 20
~ _GEOResourceDevResourcesPath : 24 -> 44
~ +[GEOOfflineStateManager shared] : 84 -> 104
~ -[GEOMapServiceTraits clearDeviceDisplayLanguages] : 144 -> 136
~ _GeoServicesConfig_RevGeoRequestShouldAlwaysPreserveRequestedLatLong_Metadata_block_invoke_156 : 16 -> 24
~ +[GEOGeoServiceTag(GEOProtoExtras) defaultTag] : 160 -> 132
~ -[GEOPDAnalyticMetadata _readServiceTags] : 212 -> 224
~ _GEOTileLoaderClientIdentifier : 144 -> 128
~ _MapsFeaturesConfig_ShelbyvilleTerrain_Metadata_block_invoke_13 : 24 -> 16
~ _GeoServicesConfig_ShouldOverrideCountryCode_Metadata_block_invoke_67 : 24 -> 32
~ _MapsFeaturesConfig_VKMLayoutEnabled_Flyover_Metadata_block_invoke_51 : 36 -> 28
~ _GEORegionalResourcesDirectory : 136 -> 144
~ -[GEOPlatform supportsAdvancedMap] : 96 -> 84
~ -[GEOClientCapabilities _readFormattedStringClientCapabilities] : 232 -> 212
~ _MapsFeature_IsEnabled_Maps182 : 40 -> 28
~ -[GEOClientCapabilities artworkCapabilities] : 92 -> 64
~ _GeoServicesConfig_NavdTransitTextInPlanningArtwork_Metadata_block_invoke_331 : 36 -> 32
~ -[GEOClientCapabilities _readSupportedTransitFeatures] : 232 -> 204
~ _GeoServicesConfig_NavdTransitListInstructionTimeText_Metadata_block_invoke_332 : 36 -> 32
~ -[GEOAdvisoryClientCapabilities .cxx_destruct] : 40 -> 44
~ +[GEOResourceManager sharedManager] : 96 -> 88
~ -[GEOTileLoaderConfiguration memoryCacheCountLimit] : 8 -> 36
~ -[GEOTileServerRemoteProxy open] : 28 -> 8
~ +[GEOOfflineVectorTileRequester tileProviderIdentifier] : 24 -> 16
~ _GEOTileProviderForOfflineStyle : 68 -> 44
~ +[GEOPrivacyManager sharedManager] : 184 -> 172
~ _GEOTilePointForCoordinate : 236 -> 248
~ -[GEOActiveTileSet availableTiles] : 52 -> 76
~ ___39+[GEOTileLoader singletonConfiguration]_block_invoke : 84 -> 60
~ -[GEOActiveTileSet _readAvailableTiles] : 212 -> 200
~ _GEOTileSetRegionReadAllFrom : 1784 -> 1796
~ -[GEOPrivacyManager hasFiredResetPrivacyWarningsNotification] : 12 -> 36
~ -[GEOTileServerLocalProxy open] : 32 -> 8
~ -[GEOResourceManifestManager _buildResourceNamesToPaths] : 1304 -> 1312
~ _MapsFeaturesConfig_ShelbyvilleGlobe_Metadata_block_invoke_7 : 32 -> 16
~ -[GEOTileCacheReserved .cxx_construct] : 88 -> 64
~ _GEOTileSetRegionIntersectsMapRect : 368 -> 392
~ -[GEOTileServerLocalProxy _registerBuiltInProviders] : 576 -> 552
~ +[GEOIdentifiedMapDataRequester tileProviderIdentifier] : 12 -> 36
~ +[GEOVisualLocalizationTileRequester tileProviderIdentifier] : 8 -> 16
~ -[GEONonTiledModel _readInfo] : 204 -> 208
~ -[GEOActiveTileGroup _readRegionalResourceCanonicalNameToFileName] : 224 -> 220
~ ___56-[GEOResourceManifestManager _buildResourceNamesToPaths]_block_invoke : 188 -> 164
~ _MapsFeaturesConfig_Maps298Enabled_Metadata_block_invoke_21 : 12 -> 28
~ -[GEOTileLoaderConfiguration manifestConfiguration] : 8 -> 24
~ -[GEOTilePool init] : 20 -> 36
~ -[GEOTileCache init] : 500 -> 516
~ __ZN3geo6detail20_GEOGenericContainerI11_GEOTileKeyU8__strongP11objc_objectNSt3__14hashIS2_EENS6_8equal_toIS2_EENS_35GEOGenericContainerWeakReferenceTagELm0ELm0ENS_29GEOGenericContainerLockingTagENS0_21_default_pointer_typeEE6_pruneEv : 152 -> 144
~ -[GEOActiveTileSet availableTilesCount] : 60 -> 56
~ +[GEOVoltaireSputnikMetadataTileRequester tileProviderIdentifier] : 12 -> 16
~ +[GEOFeatureSpecificSimpleTileRequester tileProviderIdentifier] : 24 -> 12
~ +[GEOPolygonSelectionSimpleTileRequester tileProviderIdentifier] : 36 -> 16
~ +[GEOMuninMeshRequester tileProviderIdentifier] : 16 -> 24
~ +[GEOGloriaQuadIDTileRequester tileProviderIdentifier] : 36 -> 20
~ +[GEOLegacyVisualLocalizationTileRequester tileProviderIdentifier] : 32 -> 16
~ +[GEOS2MapTileRequester tileProviderIdentifier] : 32 -> 24
~ ___35+[GEOResourceManager sharedManager]_block_invoke : 84 -> 88
~ -[GEOActiveTileGroup _readResourceCanonicalNameToFileName] : 204 -> 208
~ _MapsFeature_IsEnabled_Maps298 : 44 -> 28
~ -[GEOTileLoaderConfiguration diskCacheLocation] : 8 -> 16
~ +[GEOMuninHEIFTextureRequester tileProviderIdentifier] : 28 -> 36
~ +[GEOVisualLocalizationMetadataTileRequester tileProviderIdentifier] : 24 -> 8
~ _GEOTileProviderForStyle : 40 -> 48
~ +[GEOOfflineIdentifiedMapDataRequester tileProviderIdentifier] : 8 -> 16
~ +[GEOLiveTileRequester tileProviderIdentifier] : 16 -> 32
~ -[GEOTileServerLocalProxy _updateExpiringTilesets] : 624 -> 632
~ _GEOGetGEOPrivacyManagerLog : 84 -> 108
~ -[GEOTileLoaderConfiguration .cxx_destruct] : 108 -> 92
~ _MapsFeature_IsEnabled_ElevatedPolygons : 36 -> 28
~ -[GEONonTiledInfo name] : 40 -> 36
~ -[GEOPeer peerID] : 24 -> 28
~ -[GEONonTiledMaterialMap .cxx_destruct] : 20 -> 28
~ ___GEOConfigRemoveBlockListener_block_invoke : 440 -> 432
~ -[GEOResourceManifestServerRemoteProxy openConnection] : 24 -> 32
~ _MapsFeaturesConfig_ShelbyvilleBuildingHeights_Metadata_block_invoke_12 : 36 -> 32
~ -[GEOAttribution _readResources] : 224 -> 220
~ -[GEONonTiledModel .cxx_destruct] : 120 -> 128
~ _MapsFeature_IsEnabled_ShelbyvilleBuildingHeights : 24 -> 44
~ -[GEOMessage peer] : 8 -> 20
~ __initStorage : 164 -> 156
~ +[GEOOfflineService sharedNoCreate] : 12 -> 16
~ _GEOAttributionReadAllFrom : 408 -> 416
~ _GEOAttributionReadSpecified : 3008 -> 3000
~ -[GEOAttribution resources] : 80 -> 76
~ -[GEONonTiledAssets materialMapsCount] : 84 -> 92
~ -[GEONetworkEventData init] : 116 -> 108
~ -[GEONonTiledInfo .cxx_destruct] : 36 -> 24
~ ___29-[GEOXPCConnection reconnect]_block_invoke : 32 -> 20
~ ____initStorage_block_invoke : 116 -> 132
~ ____GEOFullDefaultsDomain_block_invoke : 168 -> 148
~ -[GEOActiveTileGroup _readAttributions] : 228 -> 204
~ _GeoUserSessionConfig_EVDirectionsFeedbackToggle_Metadata_block_invoke_12 : 24 -> 12
~ -[GEOAnalyticsPipelineStateData init] : 112 -> 120
~ -[GEOMapDataSubscriptionManager init] : 20 -> 24
~ -[GEOMapDataSubscriptionRemoteDownloadManager init] : 356 -> 344
~ -[GEOOfflineService _updateSubscribedRegions] : 372 -> 368
~ +[GEOMapSubscriptionsFetchRequest replyClass] : 24 -> 28
~ ___37-[GEOOfflineService _goActiveOnQueue]_block_invoke_2.38 : 92 -> 80
~ -[GEOUtilityService sendHeartbeat] : 216 -> 196
~ ___47-[GEOOfflineService _startCheckingConnectivity]_block_invoke : 440 -> 428
~ ___53+[GEOOfflineStateManager beginMonitoringAvailability]_block_invoke : 820 -> 832
~ -[GEODirectionsFeedbackCollector init] : 100 -> 76
~ -[_GEOConfigChangedBlockListener .cxx_destruct] : 100 -> 96
~ -[GEOActiveTileGroup clearHybridUnavailableRegions] : 168 -> 164
~ -[GEOOfflineService _setStateNeedsUpdate] : 392 -> 400
~ _GEOConfigGetBOOLForCountryCode : 80 -> 72
~ -[GEOObserverHashTable allObservers] : 128 -> 108
~ _GEOAvailableAnnouncementsReadAllFrom : 428 -> 424
~ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorIN8addr_obj5venue5FieldEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS8_m : 88 -> 72
~ __ZNSt3__16vectorIN12geomapregion7Polygon5PointENS_9allocatorIS3_EEE7reserveEm : 192 -> 168
~ -[GEOOfflineService state] : 92 -> 112
~ _GEOMapRectSpans180thMeridian : 44 -> 40
~ -[GEOMapRegion(GEOProtoExtras) hasRectangleVertices] : 112 -> 128
~ _GEOOfflineDeviceAsString : 144 -> 164
~ -[GEOXPCMessage _prepareMessage] : 192 -> 200
~ -[GEOMapSubscriptionsFetchRequest identifiersFilter] : 24 -> 28
~ -[GEOOfflineServiceSubscriptionStateChanged currentState] : 32 -> 40
~ -[GEOCountryConfiguration currentCountrySupportsCarIntegration] : 28 -> 16
~ -[GEOMapSubscriptionsFetchRequest .cxx_destruct] : 44 -> 36
~ _GEOMapRectForCoordinateRegion : 896 -> 884
~ ___40-[GEOPlatform _deviceSupportsNavigation]_block_invoke : 56 -> 48
~ +[GEOOfflineServiceSubscriptionStateChanged messageName] : 32 -> 20
~ -[GEOXPCMessage .cxx_destruct] : 36 -> 12
~ -[GEOMapSubscriptionsFetchRequest fetchExpired] : 20 -> 32
~ +[GEOMapDataSubscriptionManager sharedManager] : 100 -> 92
~ ___45-[GEOOfflineService _updateSubscribedRegions]_block_invoke : 604 -> 584
~ -[GEOAnnouncement _readMapRegion] : 220 -> 216
~ _GEOMapRegionReadSpecified : 2676 -> 2680
~ -[GEOAnnouncement mapRegion] : 92 -> 88
~ __ZNK12geomapregion7Polygon8containsERKNS0_5PointE : 236 -> 240
~ -[GEOAnnouncement .cxx_destruct] : 244 -> 248
~ _GEOMapRectForMapRegion : 460 -> 464
~ -[GEOURLCamera altitude] : 36 -> 16
~ -[GEOOfflineService isUsingOffline] : 216 -> 220
~ -[GEOActiveTileGroup identifier] : 24 -> 44
~ _GEOGetNetEventFileManagerLog : 108 -> 92
~ _GEOGetAnalyticDataFileLog : 100 -> 84
~ -[GEONetworkEventFileManager _startTimer] : 180 -> 196
~ ___44-[GEOReferenceTimeManager bestReferenceTime]_block_invoke : 32 -> 36
~ -[GEOSQLiteDB isolationQueue] : 24 -> 12
~ _GeoServicesConfig_ResourceManifestURL_Metadata_block_invoke_10 : 16 -> 24
~ -[GEOExperimentConfiguration experimentsInfo] : 108 -> 100
~ -[GEOPDABClientDatasetMetadata datasetId] : 24 -> 32
~ _GEOSessionIDReadAllFrom : 840 -> 856
~ ___FetchSubscriptions_block_invoke : 468 -> 484
~ _GEOConfigGetValueWithSourceString : 20 -> 32
~ _GEOGetUserTransportTypePreference : 156 -> 148
~ -[GEOAutomobileOptions init] : 124 -> 120
~ _MapsFeaturesConfig_ShelbyvillePuck_Metadata_block_invoke_16 : 28 -> 12
~ -[GEOOfflineVersionMetadataFetchReply isValid] : 8 -> 24
~ -[GEOOfflineVersionMetadata .cxx_destruct] : 28 -> 20
~ -[GEOUserSession _updateSharedSessionDataByAppId] : 252 -> 264
~ _GEOAPSessionDataReadAllFrom : 2772 -> 2760
~ +[GEOUserAccountInfo hasValidICloudAccountForAddingRatingsAndPhotos] : 188 -> 184
~ -[GEOPlace _readBusiness] : 216 -> 228
~ -[GEOMapItemStorage place] : 68 -> 92
~ ___74-[GEOMapItemStorage(GEOMapItem) _geoMapItemCreatingAndAssociatingIfNeeded]_block_invoke : 480 -> 456
~ -[GEOMapItemStorage _readUserValues] : 208 -> 200
~ -[GEOMapItemStorage(AdditionalFields) initAdditionalFields] : 76 -> 84
~ -[GEOMapItemStorage hasPlaceData] : 68 -> 60
~ _GeoServicesConfig_TransportTypePreference_Metadata_block_invoke : 12 -> 32
~ _GEOBatchLogMessageType : 64 -> 76
~ -[GEOLocation(GEOProtoExtras) coordinate] : 88 -> 96
~ -[GEOBaseMapItem _placeResult] : 16 -> 8
~ -[GEOMapItemAssistant _place] : 232 -> 240
~ -[GEOBaseMapItem _clientAttributes] : 28 -> 16
~ -[GEOBusiness init] : 116 -> 120
~ -[GEOMapItemStorage(GEOMapItem) geoFenceMapRegion] : 100 -> 76
~ -[GEOMapItemStorage _readPlace] : 228 -> 224
~ -[_GEOPlaceItem displayMapRegion] : 248 -> 240
~ -[GEOPlace mapRegion] : 92 -> 68
~ -[_GEOPlaceItem coordinate] : 44 -> 16
~ -[GEOPlace(GEOProtoExtras) coordinate] : 188 -> 176
~ -[GEOPlace center] : 84 -> 88
~ -[GEOMapItemStorage(GEOMapItem) addressDictionary] : 256 -> 260
~ -[_GEOPlaceItem addressDictionary] : 212 -> 236
~ -[GEOPlace _readAddress] : 208 -> 216
~ -[_GEOPlaceItem name] : 28 -> 32
~ -[GEOPlace(GEOProtoExtras) bestName] : 208 -> 196
~ -[GEOPlace _readName] : 228 -> 232
~ -[GEOMapItemStorage(GEOMapItem) areasOfInterest] : 92 -> 96
~ -[_GEOPlaceItem areasOfInterest] : 124 -> 120
~ -[GEOMapItemStorage(GEOMapItem) timezone] : 252 -> 256
~ -[_GEOPlaceItem timezone] : 156 -> 148
~ -[GEOPlace _readTimezone] : 232 -> 212
~ -[GEOTimezone identifier] : 60 -> 84
~ -[GEOMapItemStorage(GEOMapItem) _styleAttributes] : 80 -> 84
~ -[_GEOPlaceItem _styleAttributes] : 20 -> 16
~ -[GEOMapItemStorage(GEOMapItem) _muid] : 60 -> 64
~ -[_GEOPlaceItem _muid] : 28 -> 24
~ -[_GEOMapItemStorageNotificationTrampoline .cxx_destruct] : 104 -> 76
~ -[_GEOPlaceItem .cxx_destruct] : 148 -> 140
~ -[GEOBusiness .cxx_destruct] : 428 -> 420
~ -[GEOLogMsgState _readDeviceIdentifier] : 208 -> 220
~ -[GEOAnalyticsPipelineStateData isInternalTool] : 32 -> 20
~ -[GEOLogMsgState applicationIdentifier] : 72 -> 92
~ ___38+[GEOOfflineDataAccess sharedInstance]_block_invoke : 280 -> 272
~ ___65-[GEOResourceManifestUpdateAssertionRegistry hasActiveAssertions]_block_invoke : 480 -> 504
~ -[GEOOfflineVersionMetadataFetchRequest isValid] : 20 -> 28
~ -[_GEOMirroredProgress _update] : 428 -> 404
~ ___GEOGetReferenceTimeManagerLog_block_invoke : 96 -> 88
~ ___32+[GEOUserSession sharedInstance]_block_invoke : 72 -> 84
~ _GeoUserSessionConfig_ShortSessionDataByAppID_Metadata_block_invoke_10 : 32 -> 20
~ -[GEOResourceManifestManager serverProxy] : 12 -> 36
~ -[GEOOfflineVersionMetadataFetchReply .cxx_destruct] : 20 -> 40
~ _GeoUserSessionConfig_LocIntelSessionData_Metadata_block_invoke_14 : 12 -> 20
~ _GEOBatchAnalyticsSessionType : 32 -> 12
~ -[GEOUserSession _initializeShortAndNavData] : 100 -> 92
~ _GEOOnce : 140 -> 116
~ -[GEOResourceManifestServerRemoteProxy serverQueue] : 16 -> 36
~ -[GEOLogMsgStateApplicationIdentifier _readAppIdentifier] : 216 -> 204
~ +[GEOOfflineDataAccess sharedInstance] : 92 -> 84
~ -[GEOResourceManifestUpdateAssertionRegistry hasActiveAssertions] : 208 -> 200
~ -[GEOOfflineVersionMetadataFetchRequest reply] : 28 -> 12
~ +[GEOPlatform isRunningInGeoAPd] : 16 -> 40
~ _GeoServicesConfig_TileGroupRetryCountResetInterval_Metadata_block_invoke_208 : 40 -> 32
~ -[GEOOfflineVersionMetadataFetchReply metadata] : 32 -> 40
~ _GeoServicesConfig_ManifestSupportsAdditionalMarkets_Metadata_block_invoke_196 : 36 -> 12
~ +[GEOReferenceTimeData supportsSecureCoding] : 20 -> 12
~ ___55-[GEOResourceManifestServerLocalProxy resourceManifest]_block_invoke : 40 -> 44
~ _GEOResourceManifestDownloadReadSpecified : 1552 -> 1548
~ +[GEOUserSession initialShareSessionWithMaps] : 28 -> 16
~ -[GEOLogMsgState .cxx_destruct] : 1264 -> 1252
~ _GEOSessionIDWriteTo : 96 -> 88
~ -[GEOActiveResourceFilter .cxx_destruct] : 84 -> 108
~ _GEOServiceVersionReadAllFrom : 884 -> 888
~ _GEOResourceFilterReadSpecified : 2172 -> 2176
~ -[GEOResourceManifestConfiguration defaultScale] : 16 -> 28
~ -[GEORegionalResourceSet init] : 124 -> 116
~ _GEORegionalResourceSetReadSpecified : 1344 -> 1364
~ __GEOURLInfoSetCallReadAllRecursiveWithoutSynchronized : 1392 -> 1376
~ _GEOLocalizedStringReadSpecified : 1228 -> 1224
~ __GEOActiveTileGroupCallReadAllRecursiveWithoutSynchronized : 1880 -> 1852
~ _GEOCountryRegionTupleReadSpecified : 1224 -> 1244
~ _GEOSentinelTileReadAllFrom : 860 -> 852
~ -[GEOLogMsgState init] : 124 -> 104
~ +[GEOUserSession sharedInstance] : 100 -> 96
~ -[GEOConfigStorageSetValueForKeyRequest .cxx_destruct] : 88 -> 100
~ __GEORegionalResourceSetCallReadAllRecursiveWithoutSynchronized : 260 -> 276
~ _GEOURLInfoReadAllFrom : 1416 -> 1436
~ -[GEOAPSessionData sessionId] : 24 -> 40
~ -[GEOConfigStorageSetValueForKeyReply isValid] : 28 -> 20
~ -[GEOLogMsgStateApplicationIdentifier init] : 96 -> 104
~ -[GEOConfigStorageSetValueForKeyRequest keyOptions] : 36 -> 20
~ _GEODisplayStringReadAllFrom : 668 -> 660
~ __GEOAttributionCallReadAllRecursiveWithoutSynchronized : 264 -> 268
~ _MapsFeature_IsEnabled_PlaceCardShowcase : 20 -> 24
~ -[GEOPDClientMetadata _readSupportedMapsResultTypes] : 212 -> 208
~ -[GEOMapServiceTraits hasIsTourist] : 24 -> 40
~ sub_1866a6a30 -> sub_18667e960 : 236 -> 244
~ -[GEOCoalescingTimer scheduleRun] : 456 -> 464
~ _GEOLatLngReadAllFrom : 1376 -> 1372
~ -[GEOActiveTileGroup _readTileSets] : 212 -> 208
~ -[GEOActiveTileSet init] : 120 -> 124
~ _GEOActiveTileSetReadAllFrom : 416 -> 432
~ _GEOActiveTileSetReadSpecified : 4284 -> 4292
~ sub_1866a869c -> sub_1866805f0 : 72 -> 76
~ ___44-[GEOResourceManifestManager isMuninEnabled]_block_invoke : 44 -> 52
~ _MapsFeaturesConfig_IsMuninEnabled_Metadata_block_invoke_2 : 24 -> 16
~ -[GEOActiveTileGroup(GEOResourceManifestManagerAdditions) isMuninEnabled] : 92 -> 96
~ -[GEOActiveTileGroup _readMuninBuckets] : 212 -> 220
~ _GEOMuninBucketReadAllFrom : 1152 -> 1148
~ ____GEOConfigRangeCheckEnabled_block_invoke : 324 -> 336
~ +[GEONotificationPreferenceManager sharedManager] : 108 -> 96
~ -[GEOTraitsTransitScheduleFilter hasOperatingHoursRange] : 64 -> 56
~ __GEOPDComponentFilterCallReadAllRecursiveWithoutSynchronized : 148 -> 156
~ -[GEOTraitsTransitScheduleFilter _readOperatingHoursRange] : 212 -> 228
~ -[GEOPDTransitScheduleFilter hash] : 208 -> 184
~ -[GEOPDComponentInfo filter] : 68 -> 60
~ -[GEOPDFactoidFilter hash] : 76 -> 52
~ __ZNK8addr_obj27SerializedStructuredAddress3getEv : 4 -> 12
~ -[GEOTraitsTransitScheduleTimeRange startTime] : 40 -> 28
~ -[GEOPDDeparturePredicate hash] : 148 -> 128
~ -[GEOMapServiceTraits photosCount] : 44 -> 24
~ -[GEOPDCaptionedPhotoFilter init] : 124 -> 104
~ -[GEOPDCaptionedPhotoFilter _readPhotoSizeFilters] : 200 -> 208
~ -[GEOTraitsPhotoSize height] : 32 -> 24
~ -[GEOPDAmenitiesFilter hash] : 68 -> 52
~ -[GEOPDForwardInfoFilter hash] : 36 -> 28
~ -[GEOTraitsTransitScheduleFilter operatingHoursRange] : 76 -> 68
~ _GeoServicesConfig_RequestLegacyHoursComponent_Metadata_block_invoke_417 : 36 -> 28
~ -[GEOPDTransitScheduleFilter init] : 100 -> 108
~ -[GEOPDComponentFilter categorizedPhotosFilter] : 236 -> 224
~ -[GEOPDCategorizedPhotosFilter hash] : 280 -> 260
~ -[GEOPDComponentFilter amenitiesFilter] : 216 -> 212
~ -[GEOPDReviewFilter hash] : 132 -> 136
~ __ZN8addr_obj10getVersionEv : 68 -> 44
~ +[GEOAddressObject libraryVersion] : 148 -> 140
~ -[GEOPDAddressObjectFilter hash] : 100 -> 112
~ _GEOPDReverseGeocodingParametersHasSensitiveFields : 276 -> 272
~ -[GEOLocation hasIsMatchedLocation] : 24 -> 28
~ _GEOPDReverseGeocodingParametersClearSensitiveFields : 236 -> 232
~ _GEOLocationClearSensitiveFields : 468 -> 472
~ -[GEOPDPlaceRequestParameters _readMapsIdentifierPlaceLookupParameters] : 200 -> 188
~ _GEOPDAddressObjectFilterReadAllFrom : 872 -> 884
~ _GEOPDReverseGeocodingParametersReadSpecified : 1896 -> 1892
~ sub_1866b1e98 -> sub_186689d38 : 76 -> 80
~ -[GEOPDReverseGeocodingParameters hash] : 184 -> 180
~ __ZSt28__throw_bad_array_new_lengthB8ne200100v : 64 -> 80
~ -[GEOURLInfoSet _readAnalyticsCohortSessionURL] : 216 -> 212
~ _GEOBatchDescription : 288 -> 272
~ -[GEOAttribution _readUrl] : 212 -> 228
~ __NSDictionarySafeEncodingCopy : 808 -> 796
~ _GEOConfigGetDate : 36 -> 48
~ -[GEOXPCReplyError .cxx_destruct] : 96 -> 84
~ -[GEOUserSession(DependencyInjection) _get15moDeviceSessionConfiguredEpoch] : 44 -> 16
~ _GeoUserSessionConfig_FifteenMonthDeviceSessionConfiguredEpoch_Metadata_block_invoke : 20 -> 16
~ -[GEOUserSession(DependencyInjection) _get15moDeviceRawSessionData] : 36 -> 40
~ -[GEOAPSessionData mapsUserStartDate] : 40 -> 32
~ -[GEOAttribution url] : 84 -> 68
~ -[GEOLogMsgEvent _readMapsEngagement] : 216 -> 204
~ -[GEOUserSession(DependencyInjection) _get15moDeviceSessionData] : 224 -> 228
~ -[GEOAPSessionData hasRotated] : 36 -> 24
~ _GeoServicesConfig_AnalyticsCohortSessionURL_Metadata_block_invoke_34 : 24 -> 12
~ -[GEOLogMsgStateUserSession .cxx_destruct] : 104 -> 92
~ -[GEOLocalTime .cxx_destruct] : 108 -> 88
~ -[GEOLogMsgEventMapsEngagement .cxx_destruct] : 144 -> 152
~ ___68-[GEOSQLiteDB(ExternalFile) _waitForAllTransactionExternalResources]_block_invoke : 40 -> 32
~ -[GEOLogMsgStateUser init] : 116 -> 96
~ -[GEOAnalyticsPipelineStateData mapsUserStartDate] : 16 -> 36
~ -[GEOLogMsgState hasLookAroundView] : 76 -> 80
~ -[GEOLogMessage .cxx_destruct] : 32 -> 28
~ -[GEOLogMsgEventUserAction .cxx_destruct] : 180 -> 168
~ _GEOConfigSetBytes : 28 -> 20
~ _GeoServicesConfig_ThrottlerState_Metadata_block_invoke_77 : 8 -> 16
~ __GEOConfigRemoveValue : 16 -> 40
~ _GeoServicesConfig_MapsAuthProxy_Metadata_block_invoke_124 : 16 -> 8
~ -[GEOURLInfoSet authProxyURL] : 84 -> 92
~ -[GEOFeatureStyleAttributes .cxx_destruct] : 36 -> 40
~ -[GEOResourceManifestDownload _readResources] : 212 -> 216
~ _GEOResourcesReadAllFrom : 416 -> 432
~ sub_1866b9354 -> sub_1866911a4 : 404 -> 412
~ -[GEOResource _readFilters] : 228 -> 216
~ -[GEOPDStorefrontPresentationFilter hash] : 32 -> 12
~ -[GEOPDAnnotatedItemListFilter hash] : 56 -> 64
~ _MapsFeaturesConfig_ShelbyvilleStonehenge_Metadata_block_invoke_14 : 24 -> 16
~ -[GEOPDComponentFilter quickLinkFilter] : 216 -> 236
~ -[GEOPDQuickLinkFilter hash] : 72 -> 52
~ -[GEOPDComponentFilter relatedPlaceFilter] : 224 -> 232
~ -[GEOMapServiceTraits relatedPlaceItemCount] : 40 -> 20
~ -[GEOPDRelatedPlaceFilter hash] : 88 -> 108
~ -[GEOMapServiceTraits _readSupportedChildActions] : 208 -> 224
~ -[GEOPDResultSnippetFilter hash] : 164 -> 160
~ -[GEOPDPublisherFilter hash] : 76 -> 64
~ _MapsFeature_IsAvailable_ShelbyvilleSearch : 12 -> 36
~ -[GEOPDComponentInfo .cxx_destruct] : 108 -> 84
~ -[GEOMapServiceTraits wantsRouteCreationTip] : 44 -> 24
~ -[GEOPDSupportsOfflineMapsFilter hash] : 8 -> 28
~ ___28-[GEOPurgableFile _readData]_block_invoke_2 : 108 -> 112
~ -[GEOPDPlaceRequest _readPlaceRequestParameters] : 208 -> 204
~ -[_GEOURLStateCapture init] : 136 -> 140
~ -[GEOPDPlaceRequest requestType] : 128 -> 124
~ _GEOMapItemHandleShouldStoreRequestData : 32 -> 16
~ -[GEOPlaceCardRequester init] : 168 -> 156
~ -[GEOPDClientMetadata _readDeviceExtendedLocation] : 220 -> 216
~ _GEOLocationHasSensitiveFields : 216 -> 188
~ -[GEOPDPlaceRequest hasPlaceRequestParameters] : 68 -> 64
~ -[GEOPlaceRequestMessage request] : 20 -> 16
~ _GEOPDPhotoSizeFilterValueWriteTo : 132 -> 136
~ sub_1866c25e8 -> sub_18669a3e8 : 472 -> 476
~ _GEOPDPlaceRequestReadSpecified : 3628 -> 3636
~ -[GEOXPCRequest traits] : 24 -> 12
~ -[GEOPlaceRequestMessage timeout] : 24 -> 36
~ -[GEOXPCRequest throttleToken] : 16 -> 8
~ -[GEOPDPlaceRequest requestedComponents] : 80 -> 68
~ _GEOPDAmenitiesFilterReadAllFrom : 852 -> 840
~ _GEOPDCaptionedPhotoFilterReadAllFrom : 416 -> 396
~ _GEOPDCaptionedPhotoFilterReadSpecified : 1296 -> 1304
~ _GEOPDPhotoSizeFilterValueReadAllFrom : 888 -> 892
~ _GEOPDOfflineAreaFilterReadAllFrom : 528 -> 520
~ _GEOPDAnnotatedItemListFilterReadAllFrom : 672 -> 688
~ _GEOPDStorefrontFilterReadAllFrom : 460 -> 448
~ _GEOPDTipFilterReadAllFrom : 672 -> 676
~ _GEOPDPublisherFilterReadAllFrom : 848 -> 844
~ _GEOPDResultSnippetFilterReadAllFrom : 1984 -> 1988
~ _GEOPDSupportsOfflineMapsFilterReadAllFrom : 512 -> 508
~ _GEOPDFactoidFilterReadAllFrom : 848 -> 840
~ _GEOPDCategorizedPhotosFilterReadAllFrom : 416 -> 404
~ _GEOPDCategorizedPhotosFilterReadSpecified : 2420 -> 2440
~ _GEOPDTransitScheduleFilterReadAllFrom : 400 -> 424
~ _GEOPDTransitScheduleFilterReadSpecified : 1752 -> 1748
~ _GEOPDDeparturePredicateReadAllFrom : 916 -> 936
~ _GEOPDTimeRangeReadAllFrom : 864 -> 892
~ _GEOPDRelatedPlaceFilterReadAllFrom : 1096 -> 1116
~ _GEOPDReviewFilterReadAllFrom : 940 -> 956
~ _GEOPDForwardInfoFilterReadAllFrom : 536 -> 508
~ _GEOPDStorefrontPresentationFilterReadAllFrom : 452 -> 444
~ -[GEOPDPlaceRequest _readHandleData] : 220 -> 216
~ -[GEOPDPlaceRequest(GEOPDPlaceCache) cacheKey] : 484 -> 508
~ +[GEOPlaceDataRequester sharedInstance] : 92 -> 100
~ -[GEOExperimentConfiguration _mapsAbClientMetadata] : 132 -> 136
~ sub_1866d0bdc -> sub_1866a8a20 : 164 -> 152
~ _GeoServicesConfig_ValidateSensitiveFieldsAtSend_PlaceRequest_Metadata_block_invoke_392 : 40 -> 16
~ -[GEOMapServiceTraits requestPurpose] : 112 -> 104
~ -[GEOPlaceDataRequestConfig supportsOffline] : 16 -> 24
~ -[GEOServiceRequester networkOperationClasses] : 164 -> 188
~ -[GEOPlaceDataRequestConfig timeout] : 32 -> 40
~ _GEOURLLogFacility : 76 -> 80
~ sub_1866d2698 -> sub_1866aa4dc : 92 -> 88
~ _GEOGeoServiceTagReadAllFrom : 864 -> 868
~ __GEOPDPlaceRequestCallReadAllRecursiveWithoutSynchronized : 580 -> 564
~ _GEOAdditionalEnabledMarketsReadSpecified : 1184 -> 1164
~ _GEOLocalizationCapabilitiesReadAllFrom : 1436 -> 1440
~ __GEOPDClientMetadataCallReadAllRecursiveWithoutSynchronized : 364 -> 352
~ __GEOABSecondPartyPlaceRequestClientMetaDataCallReadAllRecursiveWithoutSynchronized : 444 -> 424
~ -[GEOPDClientMetadata hash] : 1124 -> 1144
~ -[GEOPDABClientDatasetMetadata hash] : 132 -> 140
~ -[GEOMapServiceTraits requestPriority] : 120 -> 112
~ -[GEOPlaceDataRequestConfig urlType] : 20 -> 40
~ _GEOPDTimeRangeWriteTo : 128 -> 116
~ -[GEOMapServiceTraits requestMode] : 104 -> 108
~ -[GEOPDAnalyticMetadata hash] : 848 -> 864
~ -[GEOAdditionalEnabledMarkets hash] : 104 -> 84
~ -[_GEOURLManifestListenerCallbackWithQueue .cxx_destruct] : 88 -> 100
~ -[GEODataRequest auditToken] : 16 -> 28
~ _GEOGetDataSessionURLLog : 104 -> 92
~ -[GEODataRequest bodyData] : 28 -> 16
~ _GEOURLSupportsMPTCP : 84 -> 68
~ -[GEOURLInfo supportsMultipathTCP] : 68 -> 44
~ -[GEOPlaceDataRequestConfig multipathServiceType] : 32 -> 40
~ _GEOURLMultipathAlternatePort : 92 -> 116
~ -[GEOResourceManifestManager hasActiveTileGroup] : 64 -> 52
~ _GEODataURLSessionGetIdentifierFromSession : 236 -> 224
~ _GEOAuthProxyEnabledForActiveTileGroup : 72 -> 60
~ __protobufHTTPHeaders : 632 -> 636
~ _GEOThrottleKeyStringForRequest : 68 -> 76
~ -[GEONetworkServiceRequesterOperation _fullURL] : 384 -> 400
~ -[GEOURLInfoSet _readDispatcherURL] : 228 -> 212
~ __GEOGetQueryForExperimentType : 276 -> 300
~ -[GEOPlaceDataRequestConfig additionalHTTPHeaders] : 224 -> 216
~ -[GEOURLInfo alternativeMultipathTCPPort] : 24 -> 28
~ _writeARPCPreamble : 568 -> 584
~ -[GEOPDPlaceRequest requestTypeCode] : 32 -> 20
~ __Z33GEOThrottleKeyMakeFromRequestKind18GEODataRequestKind : 172 -> 180
~ +[GEOProtobufSession sharedProtobufSession] : 172 -> 176
~ -[GEOPDPlaceRequest responseClass] : 40 -> 16
~ -[GEODataRequest throttleToken] : 12 -> 32
~ _GEOGetDataSessionProtobufLog : 100 -> 92
~ -[GEODataURLSession sessionIsolation] : 8 -> 28
~ -[GEODataRequest publicLogDescription] : 336 -> 356
~ -[GEOApplicationAuditToken publicLogDescription] : 184 -> 196
~ __GEORequestResponseLogRequest : 376 -> 356
~ _GeoServicesConfig_MapsRequestResponseLoggingPersisted_Metadata_block_invoke_198 : 28 -> 36
~ -[GEOProtobufSessionTask dataTask] : 24 -> 12
~ +[GEOThrottlerRequester sharedRequester] : 164 -> 168
~ -[GEODataURLSessionTask start] : 232 -> 220
~ -[GEODataRequest URL] : 28 -> 16
~ -[GEOApplicationAuditToken _secondaryIdentifier] : 32 -> 12
~ -[GEODataRequest multipathServiceType] : 24 -> 36
~ ___37-[GEODataRequest(Task) newURLRequest]_block_invoke : 24 -> 32
~ ___44-[GEONetworkServiceRequesterOperation start]_block_invoke : 1232 -> 1256
~ -[GEODataURLSession urlSessions] : 20 -> 8
~ -[GEODataRequest cachedData] : 36 -> 16
~ -[GEODataURLSessionTask _start] : 664 -> 652
~ -[GEODataRequest requestCounterTicket] : 8 -> 20
~ -[GEODataURLSessionTaskIdentifier hash] : 12 -> 20
~ _GEOGloriaEnumerateQuadKeysWithinRadiusFromCoordinate : 1448 -> 1428
~ _GEOCoordinatesForRegion : 312 -> 316
~ __ZL11_isAncestorRN6gloria6TileIdEy : 340 -> 356
~ __ZN6gloria12ShardManager24CheckShardInitializationERKNS_5ShardE : 180 -> 164
~ __ZN3geo8GloriaDB7QuadKey4SizeEv : 24 -> 8
~ __ZN6gloria16NoopDecompressor10decompressERNS_5SliceERNS_12ManagedSliceE : 84 -> 108
~ -[GEOTerritoryDataTerritoryInfo _readTerritoryTypes] : 184 -> 208
~ -[GEOTerritoryRegulatoryInfo hash] : 116 -> 124
~ -[GEOTerritoryDataTerritoryInfo .cxx_destruct] : 152 -> 128
~ -[GEOGloriaTessellationOptions dealloc] : 108 -> 92
~ -[GEOGloriaDB .cxx_destruct] : 120 -> 104
~ __ZNSt3__120__shared_ptr_pointerIPN6gloria16BasicShardHeaderENS_10shared_ptrIS2_E27__shared_ptr_default_deleteIS2_S2_EENS_9allocatorIS2_EEE21__on_zero_shared_weakEv : 32 -> 16
~ __ZNSt3__120__shared_ptr_pointerIPN3geo8GloriaDB7QuadKeyENS_10shared_ptrIN6gloria15RecordAttributeEE27__shared_ptr_default_deleteIS7_S3_EENS_9allocatorIS3_EEE21__on_zero_shared_weakEv : 16 -> 24
~ -[GEOGeographicMetadataResourceFetcher .cxx_destruct] : 96 -> 120
~ -[GEOTerritoryRegulatoryInfo .cxx_destruct] : 120 -> 116
~ _GEOCoordinateRegionMakeWithDistance : 252 -> 272
~ __ZN6gloria16BasicShardHeaderD0Ev : 124 -> 140
~ -[GEOTerritoryRegulatoryInfo isDisputed] : 20 -> 8
~ -[GEOGeographicMetadataRequester .cxx_destruct] : 220 -> 208
~ -[GEOResourceManifestServerLocalProxy metadata] : 304 -> 312
~ _GEOConfigSetString : 32 -> 24
~ -[GEODataRequestThrottler reset] : 140 -> 132
~ _GEOCalculateChangedKeys : 872 -> 880
~ _GeoServicesConfig_ThrottlerLogAsFault_Metadata_block_invoke_230 : 28 -> 32
~ -[GEODownloadMetadata timestamp] : 32 -> 28
~ ___30-[GEOMapService defaultTraits]_block_invoke_6 : 32 -> 24
~ -[_GEOConfigStorageRemote resync] : 4 -> 12
~ ___47-[GEOResourceManifestServerLocalProxy metadata]_block_invoke : 24 -> 28
~ -[GEODownloadMetadata _readUrl] : 204 -> 208
~ __GEOConfigRangeCheckEnabled : 92 -> 84
~ __getUserDefaultStringKeysForStateCapture : 40 -> 20
~ __getConfigStoreStringKeysForStateCapture : 20 -> 16
~ ____valuesForStore_block_invoke : 12 -> 36
~ _GeoServicesConfig_VoltaireDirectionsURL_Metadata_block_invoke_8 : 8 -> 32
~ -[GEOURLInfoSet _readEtaURL] : 228 -> 204
~ _GeoServicesConfig_SearchAttributionManifestURL_Metadata_block_invoke_11 : 16 -> 8
~ -[GEOURLInfoSet _readProblemSubmissionURL] : 208 -> 216
~ _GeoServicesConfig_VoltaireBatchReverseGeocoderURL_Metadata_block_invoke_15 : 20 -> 12
~ -[GEOURLInfoSet addressCorrectionUpdateURL] : 76 -> 92
~ __GEOConfigStorageCFPrefsReadWrite : 172 -> 164
~ _GeoServicesConfig_URLAddressCorrectionInitURL_Metadata_block_invoke_17 : 24 -> 16
~ -[GEOURLInfoSet _readAddressCorrectionInitURL] : 220 -> 204
~ ___GEODefaultsKeyStringForConfigKey_block_invoke : 20 -> 36
~ -[GEOURLInfo useAuthProxy] : 56 -> 64
~ _GeoServicesConfig_VoltaireETAURL_Metadata_block_invoke_9 : 12 -> 36
~ -[GEOURLInfoSet _readSearchAttributionManifestURL] : 232 -> 208
~ _GeoServicesConfig_VoltaireProblemSubmissionURL_Metadata_block_invoke_12 : 8 -> 32
~ -[GEOURLInfoSet problemSubmissionURL] : 64 -> 72
~ _GeoServicesConfig_VoltaireProblemStatusURL_Metadata_block_invoke_13 : 12 -> 36
~ -[GEOURLInfoSet _readProblemStatusURL] : 204 -> 212
~ _GeoServicesConfig_LocalizedCategoriesURL_Metadata_block_invoke_44 : 16 -> 8
~ -[GEOURLInfoSet _readProblemCategoriesURL] : 216 -> 224
~ _GeoServicesConfig_CurrentCountryURL_Metadata_block_invoke_21 : 24 -> 16
~ -[GEOURLInfoSet _readBatchReverseGeocoderURL] : 224 -> 232
~ _GeoServicesConfig_URLSimpleETAURL_Metadata_block_invoke_16 : 12 -> 36
~ -[GEOURLInfoSet simpleETAURL] : 68 -> 76
~ _GeoServicesConfig_URLAddressCorrectionUpdateURL_Metadata_block_invoke_18 : 32 -> 24
~ -[GEOURLInfoSet _readAddressCorrectionUpdateURL] : 208 -> 216
~ _GeoServicesConfig_URLReverseGeocoderVersionFileURL_Metadata_block_invoke_20 : 32 -> 24
~ -[GEOURLInfoSet _readReverseGeocoderVersionsURL] : 224 -> 232
~ _GeoServicesConfig_VoltaireAnnouncementsURL_Metadata_block_invoke_24 : 28 -> 20
~ -[GEOURLInfoSet _readAnnouncementsURL] : 212 -> 220
~ _GeoServicesConfig_ProblemOptInURL_Metadata_block_invoke_26 : 36 -> 28
~ -[GEOURLInfoSet _readProblemOptInURL] : 228 -> 204
~ _GeoServicesConfig_ExperimentsURL_Metadata_block_invoke_27 : 12 -> 36
~ -[GEOURLInfoSet _readAbExperimentURL] : 220 -> 228
~ _GeoServicesConfig_BusinessPortalBaseURL_Metadata_block_invoke_28 : 16 -> 8
~ -[GEOURLInfoSet _readBusinessPortalBaseURL] : 216 -> 224
~ _GeoServicesConfig_VoltaireLogMessageUsageURL_Metadata_block_invoke_29 : 20 -> 12
~ -[GEOURLInfoSet _readLogMessageUsageURL] : 212 -> 220
~ _GeoServicesConfig_SpatialLookupURL_Metadata_block_invoke_30 : 24 -> 16
~ -[GEOURLInfoSet _readRealtimeTrafficProbeURL] : 232 -> 208
~ _GeoServicesConfig_BatchTrafficProbeURL_Metadata_block_invoke_32 : 36 -> 28
~ -[GEOURLInfoSet _readBatchTrafficProbeURL] : 228 -> 212
~ ___46-[_GEOConfigChangedBlockListener callListener]_block_invoke : 32 -> 24
~ _GeoServicesConfig_RealtimeTrafficProbeURL_Metadata_block_invoke_31 : 32 -> 24
~ -[GEOURLInfoSet realtimeTrafficProbeURL] : 80 -> 88
~ -[GEONetworkObserver init] : 120 -> 116
~ -[GEOMapSubscriptionsFetchRequest isValid] : 32 -> 36
~ ___54-[GEOMapDataSubscriptionRemoteSyncManager _connection]_block_invoke : 268 -> 264
~ -[GEOMapSubscriptionFetchLastUpdatedDateRequest isValid] : 32 -> 36
~ -[GEOUserAccountInfo primaryICloudAccount] : 308 -> 300
~ +[GEOFeatureStyleAttributes(PersonalizedItem) searchResultStyleAttributes] : 124 -> 100
~ ___40-[GEONetworkObserver isNetworkReachable]_block_invoke : 96 -> 92
~ +[GEOMapSubscriptionTotalOfflineDataSizeRequest replyClass] : 36 -> 40
~ -[GEOMapDataSubscriptionRemoteSyncManager _connection] : 136 -> 132
~ +[GEOMapSubscriptionFetchLastUpdatedDateRequest replyClass] : 28 -> 12
~ ___58-[GEOMapDataSubscriptionRemoteDownloadManager _connection]_block_invoke : 276 -> 272
~ __GEOMapDataSubscriptionIdentifierIsCompatible : 204 -> 188
~ ___FetchExpiredSubscriptions_block_invoke : 440 -> 444
~ -[GEOMapSubscriptionFetchLastUpdatedDateRequest onPairedDevice] : 16 -> 20
~ ___80-[GEOMapDataSubscriptionLocalSyncManager _pairedDeviceSubscriptionStatesSummary]_block_invoke : 252 -> 248
~ -[GEOMapSubscriptionFetchLastUpdatedDateReply isValid] : 20 -> 24
~ -[GEOAnalyticsPipelineStateData hasMapSettingsLocationPrecisionType] : 52 -> 28
~ -[GEOOfflineDataConfiguration lastUpdatedDate] : 228 -> 232
~ -[GEOAPSessionData sessionCreateHour] : 40 -> 36
~ -[GEOMapServiceTraits hardwareIdentifier] : 72 -> 88
~ ___CalculateTotalOfflineDataSize_block_invoke : 164 -> 168
~ -[GEOMapSubscriptionTotalOfflineDataSizeReply isValid] : 12 -> 36
~ ___25-[GEOXPCConnection close]_block_invoke : 112 -> 100
~ -[GEOLocalTime hash] : 260 -> 280
~ -[GEOPeer .cxx_destruct] : 196 -> 176
~ -[GEOApplicationAuditToken .cxx_destruct] : 140 -> 164
~ -[GEOOfflineService _mapViewToUse] : 672 -> 680
~ _MapsFeature_IsEnabled_Alberta : 20 -> 44
~ ___42-[NSData(GEOHashUtilities) _geo_hexString]_block_invoke : 112 -> 116
~ -[GEOActiveTileGroup _readExplicitResources] : 228 -> 232
~ ___39+[GEOResourceRequester sharedRequester]_block_invoke : 176 -> 188
~ -[GEOURLOptions init] : 116 -> 104
~ -[GEOSearchCategoryStorage .cxx_destruct] : 128 -> 148
~ -[GEOMapSubscriptionFetchLastUpdatedDateReply timestamp] : 44 -> 28
~ _GEOGetETagFromExtendedAttributes : 224 -> 244
~ -[GEOResource alternateResourceURLIndex] : 24 -> 32
~ _GEOURLAuthenticationGenerateURLFromComponents : 1604 -> 1596
~ -[GEOResourceManifestServerLocalProxy authToken] : 352 -> 328
~ _escapeChars : 104 -> 96
~ _GeoServicesConfig_ResourceRequestAdditionalHTTPHeaders_Metadata_block_invoke_73 : 28 -> 36
~ ___GEOConfigRemoveDelegateListenerForKey_block_invoke_2 : 140 -> 132
~ -[GEOAnalyticsPipelineStateData _readMapLaunchSourceAppId] : 204 -> 224
~ -[GEOLogMsgState _readExperiments] : 208 -> 220
~ _GEOPDABClientDatasetMetadataReadAllFrom : 1100 -> 1088
~ -[GEOLogMsgState _readDeviceLocale] : 216 -> 228
~ -[GEOAnalyticsPipelineStateData hasLandscape] : 52 -> 40
~ -[GEOLogMsgStateMapUI .cxx_destruct] : 112 -> 92
~ -[GEOAnalyticsPipelineStateData mapUiShownAqiShown] : 132 -> 120
~ -[GEOLogMsgState _readMapUiShown] : 204 -> 216
~ -[GEOAnalyticsPipelineStateData mapViewMapType] : 128 -> 116
~ -[GEOLogMsgState _readMapView] : 224 -> 204
~ -[GEOAnalyticsPipelineStateData mapViewPitch] : 44 -> 32
~ -[GEOLogMsgStateMapView .cxx_destruct] : 92 -> 96
~ -[GEOURLInfoSet _readBackgroundDispatcherURL] : 216 -> 224
~ _GeoServicesConfig_BluePOIURL_Metadata_block_invoke_40 : 20 -> 12
~ -[GEOURLInfoSet _readBluePOIDispatcherURL] : 212 -> 220
~ _GeoServicesConfig_BackgroundRevGeoURL_Metadata_block_invoke_41 : 24 -> 16
~ -[GEOURLInfoSet backgroundRevGeoURL] : 80 -> 88
~ _GeoServicesConfig_ImageServiceURL_Metadata_block_invoke_42 : 24 -> 16
~ -[GEOURLInfoSet _readFeedbackLookupURL] : 228 -> 204
~ _GeoServicesConfig_AnalyticsShortSessionURL_Metadata_block_invoke_36 : 16 -> 8
~ -[GEOURLInfoSet _readAnalyticsShortSessionURL] : 216 -> 224
~ _GeoServicesConfig_WebModuleBaseURL_Metadata_block_invoke_55 : 16 -> 8
~ -[GEOURLInfoSet _readTokenAuthenticationURL] : 220 -> 228
~ _GeoServicesConfig_MapsAuthClientFeatureFlags_Metadata_block_invoke_404 : 20 -> 12
~ -[GEOURLInfoSet authenticatedClientFeatureFlagURL] : 64 -> 72
~ _GeoServicesConfig_EnrichmentSubmissionURL_Metadata_block_invoke_58 : 28 -> 20
~ -[GEOURLInfoSet _readUgcLogDiscardURL] : 228 -> 204
~ _GeoServicesConfig_PressureDataURL_Metadata_block_invoke_22 : 24 -> 16
~ -[GEOURLInfoSet poiBusynessActivityCollectionURL] : 84 -> 92
~ _GeoServicesConfig_RAPWebModuleBaseURL_Metadata_block_invoke_45 : 24 -> 16
~ -[GEOURLInfoSet offlineDataBatchListURL] : 72 -> 80
~ _GeoOfflineConfig_DownloadURL_Metadata_block_invoke_4 : 8 -> 32
~ -[GEOURLInfoSet _readBcxDispatcherURL] : 204 -> 212
~ _GeoServicesConfig_MapsURLShortenerURL_Metadata_block_invoke_65 : 12 -> 32
~ sub_1866e58f8 -> sub_1866bd704 : 104 -> 88
~ -[GEODownloadMetadata .cxx_destruct] : 148 -> 168
~ -[GEOResources .cxx_destruct] : 1224 -> 1228
~ -[GEOTileGroup .cxx_destruct] : 100 -> 104
~ -[_GEOMirroredProgress .cxx_destruct] : 24 -> 28
~ -[GEOActiveTileGroup uniqueIdentifier] : 72 -> 68
~ -[_GEOMirroredProgress dealloc] : 100 -> 72
~ -[GEODownloadMetadata hasEtag] : 60 -> 64
~ -[GEOResources authToken] : 68 -> 92
~ ___55-[GEOResourceManifestServerLocalProxy resourceManifest]_block_invoke.47 : 184 -> 188
~ -[GEOResourceManifestDownload osImageResources] : 64 -> 68
~ -[GEOTileGroup clearTileSets] : 152 -> 148
~ -[GEOActiveTileGroup _readUniqueIdentifier] : 224 -> 228
~ -[GEOResources _readResources] : 224 -> 220
~ -[GEOActiveTileGroup _readEnvironment] : 224 -> 216
~ -[GEOPeer debugIdentifier] : 36 -> 12
~ -[GEOActiveTileGroup _readOfflineMetadata] : 216 -> 224
~ -[GEOOfflineMetadata dataVersion] : 28 -> 40
~ sub_1866ea190 -> sub_1866c1fa0 : 120 -> 148
~ __ZNK12_GLOBAL__N_16Result12plistEncodedEv : 468 -> 472
~ _GEORequestCounterInterfaceTypesToStrings : 248 -> 256
~ -[GEOCoalescingTimer isScheduledToRun] : 112 -> 104
~ -[GEOTileLoader _scheduleCoalesceTimer] : 464 -> 476
~ -[GEOResourceManifestDownload .cxx_destruct] : 148 -> 144
~ -[GEOResourceManifestServerLocalProxy _considerChangingActiveTileGroup] : 1852 -> 1828
~ -[GEOResources tileGroupsCount] : 76 -> 68
~ ___60-[GEOConfigStorageDirectReadWrite _scheduleWriteDirectStore]_block_invoke : 1012 -> 1020
~ ___SetValue_block_invoke : 248 -> 240
~ -[GEOResourceManifestConfiguration tileGroupIdentifier] : 32 -> 8
~ -[GEOResources(Extras) preferredDataSetForMapsABClient] : 164 -> 156
~ -[GEOPDABClientDatasetMetadata hasDatasetId] : 20 -> 28
~ -[GEOResources _readDataSets] : 216 -> 220
~ -[GEOResourceFiltersManager activeScales] : 520 -> 508
~ -[GEOActiveResourceFilters filters] : 20 -> 32
~ -[GEOResourceFiltersManager activeScenarios] : 480 -> 468
~ _uniqueIdentifierForTileGroup : 436 -> 440
~ -[GEOActiveTileGroup _readActiveNames] : 200 -> 204
~ -[GEOResources urlInfoSets] : 64 -> 80
~ -[GEOURLInfoSet hasDataSet] : 40 -> 48
~ ___GEOGetNetworkStatusLog_block_invoke : 80 -> 76
~ -[GEOMapSubscriptionTotalOfflineDataSizeRequest isValid] : 28 -> 32
~ -[GEOResource hasUpdateMethod] : 24 -> 32
~ _GEOURLAuthenticationGenerateURL : 104 -> 128
~ ___48-[GEOResourceManifestServerLocalProxy authToken]_block_invoke : 32 -> 28
~ -[GEOMapSubscriptionTotalOfflineDataSizeReply sizeInBytes] : 40 -> 44
~ -[GEOAnalyticsPipelineStateData carPlayInfo] : 68 -> 88
~ -[GEOLogMsgStateExperiments init] : 112 -> 124
~ -[GEONetworkObserver isWiFiConnection] : 12 -> 32
~ -[GEOLogMsgStateDeviceLocale .cxx_destruct] : 144 -> 156
~ -[GEOAnalyticsPipelineStateData lookAroundEntryIconShown] : 44 -> 32
~ -[GEOLogMsgStateMapUIShown .cxx_destruct] : 32 -> 44
~ -[GEOAnalyticsPipelineStateData hasMapViewMapType] : 44 -> 32
~ -[GEOLogMsgState mapView] : 92 -> 72
~ _GeoServicesConfig_ProactiveRoutingURL_Metadata_block_invoke_38 : 20 -> 28
~ -[GEOResources tileSets] : 64 -> 92
~ -[GEOActiveTileGroup hasUniqueIdentifier] : 56 -> 80
~ -[GEOMapSubscriptionsFetchRequest reply] : 12 -> 28
~ -[GEOPDPlaceRequest analyticMetadata] : 68 -> 64
~ _GEOConfigRemoveDelegateListenerForKey : 300 -> 324
~ _GeoServicesConfig_BackgroundDispatcherURL_Metadata_block_invoke_39 : 16 -> 8
~ -[GEOURLInfoSet _readMapsURLShortenerURL] : 224 -> 208
~ -[GEOResources _readTileSets] : 204 -> 224
~ _GEOTileSetReadAllFrom : 428 -> 408
~ -[GEOResources dataSets] : 88 -> 84
~ -[GEOActiveTileGroup dataSet] : 68 -> 72
~ -[_GEOConfigDBUpdateOperation .cxx_destruct] : 108 -> 132
~ -[GEONetworkObserver isNetworkReachable] : 192 -> 188
~ -[GEOMapSubscriptionTotalOfflineDataSizeRequest reply] : 16 -> 8
~ -[GEOXPCConnection .cxx_destruct] : 144 -> 168
~ -[GEOPDPlaceRequest _readAnalyticMetadata] : 216 -> 204
~ -[GEOPDDatasetABStatus .cxx_destruct] : 32 -> 20
~ -[GEOLogMsgState deviceLocale] : 84 -> 64
~ -[GEOAnalyticsPipelineStateData hasMapSettingsSpeedLimitEnabled] : 36 -> 24
~ -[GEOLogMsgState _readMarket] : 208 -> 228
~ _GEOPDReviewReadAllFrom : 408 -> 432
~ -[GEOPDEntity init] : 100 -> 108
~ _GEOMapItemStorageReadAllFrom : 428 -> 420
~ -[GEOAnalyticsPipelineStateData hasMapsServerMetadata] : 60 -> 80
~ -[GEOLogMsgStateOffline .cxx_destruct] : 44 -> 24
~ -[GEOAnalyticsPipelineStateData _readPlaceCardPlaceActionDetailsTransitPlaceCardTransitDepartureSequenceUsageDirection] : 204 -> 212
~ _GEOMapItemStorageReadSpecified : 2656 -> 2648
~ -[GEOAnalyticsPipelineStateData _readSuggestionsDisplayedResults] : 212 -> 232
~ -[GEOLogMsgStateMapSettings .cxx_destruct] : 108 -> 112
~ -[GEOURLInfoSet _readJunctionImageServiceURL] : 208 -> 216
~ _GeoServicesConfig_MuninBaseURL_Metadata_block_invoke_50 : 12 -> 36
~ -[GEOURLInfoSet _readMuninBaseURL] : 228 -> 204
~ _GeoServicesConfig_WiFiQualityURL_Metadata_block_invoke_52 : 20 -> 12
~ -[GEOURLInfoSet _readWifiQualityURL] : 212 -> 220
~ _GeoServicesConfig_FeedbackSubmissionURL_Metadata_block_invoke_53 : 32 -> 24
~ -[GEOURLInfoSet _readFeedbackSubmissionURL] : 232 -> 208
~ _GeoServicesConfig_AnalyticsLongSessionURL_Metadata_block_invoke_35 : 12 -> 36
~ -[GEOURLInfoSet _readWebModuleBaseURL] : 216 -> 224
~ _GeoServicesConfig_WiFiTileURL_Metadata_block_invoke_56 : 24 -> 16
~ -[GEOURLInfoSet _readWifiQualityTileURL] : 208 -> 216
~ _GeoServicesConfig_TokenAuthenticationURL_Metadata_block_invoke_57 : 16 -> 8
~ -[GEOURLInfoSet _readEnrichmentSubmissionURL] : 224 -> 232
~ _GeoServicesConfig_BatchRevGeoPlaceRequestURL_Metadata_block_invoke_59 : 36 -> 28
~ -[GEOURLInfoSet _readPressureProbeDataURL] : 208 -> 216
~ _GeoServicesConfig_BusynessDataURL_Metadata_block_invoke_23 : 28 -> 20
~ -[GEOURLInfoSet _readRapWebBundleURL] : 208 -> 216
~ _GeoOfflineConfig_BatchListURL_Metadata_block_invoke_2 : 32 -> 24
~ -[GEOURLInfoSet _readOfflineDataDownloadBaseURL] : 216 -> 224
~ _GeoServicesConfig_BCXDispatcherURL_Metadata_block_invoke_61 : 20 -> 12
~ -[GEOURLInfoSet bcxDispatcherURL] : 88 -> 68
~ -[GEOResourceManifestDownload resources] : 84 -> 88
~ __ZNSt3__112__hash_tableIyNS_4hashIyEENS_8equal_toIyEENS_9allocatorIyEEE8__rehashILb1EEEvm : 532 -> 516
~ _GEOTileGroupReadAllFrom : 420 -> 404
~ -[GEOTileGroup init] : 116 -> 100
~ -[GEOLogMessageCollectionRequest requestTypeCode] : 8 -> 12
~ _GEOProtocolBufferRequestHeader : 152 -> 180
~ _GEOTileKeyHash : 88 -> 92
~ ___18-[GEODaemon peers]_block_invoke : 76 -> 104
~ __ZN3geo11_retain_ptrIU8__strongP11GEOTileDataNS_16_retain_objc_arcENS_17_release_objc_arcENS_10_hash_objcENS_11_equal_objcEE5resetES2_NS_22memory_management_modeE : 100 -> 96
~ _GEOCalculateDistanceRadius : 200 -> 172
~ _GEOTileGroupReadSpecified : 6432 -> 6436
~ sub_1866f8018 -> sub_1866cfecc : 88 -> 68
~ -[GEOResources tileGroups] : 80 -> 72
~ _GeoServicesConfig_CoreLocationKACURL_Metadata_block_invoke_64 : 32 -> 8
~ -[GEOTileGroup identifier] : 16 -> 40
~ +[GEODataURLSession sharedDataURLSession] : 168 -> 172
~ -[GEOActiveTileGroup _readActiveScenarios] : 208 -> 216
~ -[GEOResourceFiltersManager activeNames] : 368 -> 392
~ -[GEOActiveTileGroup activeNames] : 72 -> 76
~ -[_GEOConfigDBOperationBase .cxx_destruct] : 36 -> 20
~ __postureRegion : 140 -> 128
~ -[GEOTileRequest signpostIDs] : 28 -> 16
~ __ZNSt3__112__hash_tableINS_17__hash_value_typeIPKcPKN13AddrObjGoogle8protobuf14FileDescriptorEEENS_22__unordered_map_hasherIS3_S9_NS5_4hashIS3_EENS5_5streqELb1EEENS_21__unordered_map_equalIS3_S9_SD_SC_Lb1EEENS_9allocatorIS9_EEE6removeENS_21__hash_const_iteratorIPNS_11__hash_nodeIS9_PvEEEE : 316 -> 340
~ __ZNK8LoadItem9Requester27performAsyncOnCallbackQueueEU13block_pointerFvvE : 112 -> 108
~ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorIPvEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m : 100 -> 88
~ +[GEOAltitudeManifest sharedManager] : 92 -> 104
~ __ZNSt3__16vectorI31GeoCodecsLocalizationTableEntryN3geo17allocator_adapterIS1_NS2_5codec15zone_mallocatorEEEE8__appendEm : 428 -> 416
~ sub_1866f9610 -> sub_1866d14b0 : 32 -> 16
~ -[GEOTileServerLocalProxyBatchContext cacheMissStaleDataList] : 8 -> 24
~ -[_GEOSimpleTileRequesterOperation URL] : 92 -> 104
~ __ZN3geo5codec23_readCompressedPolygonsEP8VMP4TileRKNSt3__110shared_ptrINS0_10VectorTileEEE : 9472 -> 9468
~ ___55-[GEOSimpleTileRequester _updateHighestRunningPriority]_block_invoke : 36 -> 44
~ __ZNSt3__111__introsortINS_17_ClassicAlgPolicyERZ36-[GEOTileLoader _requestOnlineTiles]E3$_3PN3geo5Batch7KeyInfoELb0EEEvT1_S8_T0_NS_15iterator_traitsIS8_E15difference_typeEb : 3620 -> 3648
~ __ZN3gcl17ArithmeticDecoder21decodeSignedExpGolombEiRNS_17ArithmeticContextES2_ : 304 -> 300
~ -[GEOSimpleTileRequester _checkIfDone] : 864 -> 848
~ -[GEOTileKeyMap dealloc] : 192 -> 208
~ ___dispatch_work_block_invoke : 104 -> 108
~ __ZNSt3__120__shared_ptr_emplaceIN3geo5codec10VectorTileENS1_17allocator_adapterIS3_NS2_15zone_mallocatorEEEE21__on_zero_shared_weakEv : 212 -> 204
~ -[GEOSQLiteDB sqliteDB] : 8 -> 20
~ ___DeleteData_block_invoke : 104 -> 112
~ -[GEODataURLSessionTask delegate] : 48 -> 72
~ __ZNSt3__110__function6__funcIZ36-[GEOTileLoader _requestOnlineTiles]E3$_2NS_9allocatorIS2_EEFvRN8LoadItem9RequesterEEE7destroyEv : 32 -> 8
~ __ZNSt3__16vectorIU8__strongP11GEORoadEdgeNS_9allocatorIS3_EEE11__vallocateB8ne200100Em : 72 -> 64
~ -[GEOTileDB devicePostureRegion] : 128 -> 136
~ -[GEORegionalResourcesTileRequester start] : 1572 -> 1564
~ -[GEOTileRequester tileRequest] : 24 -> 12
~ -[GEOTileRequest keyList] : 20 -> 8
~ ___42-[GEORegionalResourcesTileRequester start]_block_invoke_2 : 40 -> 44
~ -[GEORegionalResourceTileData init] : 96 -> 120
~ -[GEOResourceFilter _readScenarios] : 200 -> 228
~ __ZNSt3__110__list_impIU8__strongP8NSStringNS_9allocatorIS3_EEE5clearEv : 112 -> 120
~ ___42-[GEORegionalResourcesTileRequester start]_block_invoke_4 : 348 -> 340
~ __ZL7_removeP14GEOTileKeyListP9_ListNode : 212 -> 208
~ __ZN4mgcl5tmesh7DecoderD1Ev : 500 -> 520
~ -[_GEOSimpleTileRequesterOperation request] : 28 -> 36
~ -[GEOSimpleTileRequester(Subclasses) downloadsDataToDisk] : 16 -> 20
~ __ZN3gcl5tmesh11DecoderImpl33parsePositionsAndConnectivityInfoENS_2bs15BasicByteStreamIKhEERNS1_35PositionsAndConnectivityInfoPrivateE : 340 -> 312
~ __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeIU8__strongP8NSStringN8LoadItem9RequesterEEEPvEEEEEclB8ne200100EPSB_ : 300 -> 308
~ +[GEOReachability sharedReachability] : 104 -> 96
~ -[GEOTileServerLocalProxyBatchContext cacheMissNoDataList] : 24 -> 20
~ __ZN3geo5codec17_readContourLinesEP8VMP4TileRKNSt3__110shared_ptrINS0_10VectorTileEEE25GeoCodecsContourLineUnits26GeoCodecsContourLineRegion : 9816 -> 9828
~ -[GEOActiveTileSet version] : 20 -> 40
~ __ZN3geo5codec16PBDataReaderObjCD1Ev : 108 -> 100
~ -[GEOVectorTile vectorTilePtr] : 52 -> 32
~ -[GEOTileKeyList dealloc] : 116 -> 108
~ ___82-[GEOSimpleTileRequester(GEOTileRequestBalancer) didStartOperationsForAllTileKeys]_block_invoke : 56 -> 28
~ __ZNSt3__110__function6__funcIZN3geo5codec29_readStyleAttributeRastersOldEP8VMP4TilePK16GeoCodecsTileKeyRKNS_10shared_ptrINS3_10VectorTileEEEbE3$_0NS_9allocatorISE_EEFvP11VMP4ChapterEE18destroy_deallocateEv : 16 -> 12
~ __recursivelyClearAllRelatedOperations : 156 -> 148
~ -[_GEOSimpleTileRequesterOperation downloadedFileURL] : 92 -> 84
~ -[GEODataURLSessionTask failedDueToCancel] : 152 -> 160
~ -[GEOClientMetrics networkMetrics] : 44 -> 36
~ -[GEODataURLSessionTask receivedRNFNotification] : 32 -> 8
~ -[GEOClientNetworkTransactionMetrics requestStart] : 32 -> 24
~ -[GEODataURLSessionTask incomingPayloadSize] : 16 -> 36
~ -[GEOLogMsgState _readTileSet] : 232 -> 212
~ -[GEOFeatureStyleAttributes featureStyleAttributesPtr] : 20 -> 8
~ __ZN3geo5codec22CurveVertexPoolDeallocEP24GeoCodecsCurveVertexPool : 124 -> 136
~ _bodySizeEstimateFromResponse : 184 -> 192
~ -[GEONetworkEventData _readAdditionalStates] : 204 -> 220
~ __ZN3geo11_retain_ptrIU8__strongP12NSDictionaryNS_16_retain_objc_arcENS_17_release_objc_arcENS_10_hash_objcENS_11_equal_objcEEC2EOS8_ : 116 -> 100
~ -[GEOApplicationAuditToken hash] : 96 -> 112
~ ___destroy_helper_block_ea8_32c49_ZTSKZ36-[GEOTileLoader _requestOnlineTiles]E3$_8 : 68 -> 84
~ __ZN3geo15BatchLoadHelperD1Ev : 128 -> 112
~ _GEOTileDBDevicePostureRegion : 24 -> 32
~ -[_GEORegionalResourcesTileLoader init] : 92 -> 104
~ -[GEOTileRequest auditToken] : 36 -> 28
~ -[GEOActiveTileGroup regionalResourcesCount] : 76 -> 72
~ _GEORegionalResourceTileKeyActiveScenarios : 156 -> 160
~ -[GEORegionalResourceTileData _readIcons] : 228 -> 216
~ __ZNSt3__110__list_impIN3geo5BatchENS_9allocatorIS2_EEE5clearEv : 192 -> 200
~ ___42-[GEORegionalResourcesTileRequester start]_block_invoke_3 : 264 -> 256
~ _GEOTileKeyIsOffline : 28 -> 32
~ -[GEOServer daemon] : 60 -> 52
~ -[NSDictionary(GEOXPCUtil) _geo_newXPCObject] : 80 -> 92
~ -[GEOTileData dealloc] : 412 -> 404
~ -[GEOTileServerLocalProxyBatchContext interestList] : 12 -> 20
~ -[GEOTileData length] : 104 -> 96
~ __ZNSt3__110__list_impI8LoadItemNS_9allocatorIS1_EEE13__delete_nodeB8ne200100EPNS_11__list_nodeIS1_PvEE : 460 -> 456
~ __ZN3gcl5tmesh11DecoderImpl14decodeResidualERKNS0_12BinarizationEPNS0_9ACContextE : 5004 -> 4992
~ ___42+[NSBundle(GeoServicesBundle) __geoBundle]_block_invoke : 96 -> 108
~ __ZN3geo5codec20chapterReadVarUint32EP11VMP4ChapterPj : 336 -> 324
~ -[GEOAltitudeManifest commonInit] : 112 -> 124
~ __ZNSt3__113__stable_sortINS_17_ClassicAlgPolicyERZN3geo5codec11_readLabelsEP8VMP4TileRKNS_10shared_ptrINS3_10VectorTileEEEE3$_0P28GeoCodecsLabelLanguageLocaleEEvT1_SF_T0_NS_15iterator_traitsISF_E15difference_typeEPNSI_10value_typeEl : 656 -> 644
~ -[GEOAltitudeManifestReserved .cxx_construct] : 40 -> 20
~ __ZNSt3__16vectorIiNS_9allocatorIiEEE8__appendEm : 352 -> 356
~ __ZNSt3__16vectorIyNS_9allocatorIyEEE9push_backB8ne200100ERKy : 228 -> 244
~ __ZNSt3__16__treeINS_12__value_typeIj23_GEOAltitudeTriggerDataEENS_19__map_value_compareIjS3_NS_4lessIjEELb1EEENS_9allocatorIS3_EEE7destroyEPNS_11__tree_nodeIS3_PvEE : 120 -> 132
~ __ZN3gcl8polyline9ACContext4initEi : 452 -> 440
~ __ZNSt3__16vectorIiNS_9allocatorIiEEEC2B8ne200100Em : 148 -> 128
~ __ZN3gcl5tmesh11DecoderImpl24decodeVertexAttributesACEPiPb : 17640 -> 17612
~ -[_GEOTileDBUpdateAccessTimeOperation key] : 24 -> 8
~ -[_GEOSimpleTileRequesterOperation delegate] : 44 -> 68
~ -[GEOActiveTileSet checksumType] : 104 -> 124
~ __ZNSt3__16vectorIN2gm6MatrixIiLi3ELi1EEEN3geo17allocator_adapterIS3_NS4_5codec15zone_mallocatorEEEE8__appendEm : 508 -> 512
~ ___GetDataForKey_block_invoke : 708 -> 704
~ __ZN3geo5codec13_postDecodingERKNSt3__110shared_ptrINS0_10VectorTileEEE : 11412 -> 11404
~ -[GEOVectorTile .cxx_destruct] : 164 -> 160
~ __ZNSt3__112__hash_tableIyNS_4hashIyEENS_8equal_toIyEENS_9allocatorIyEEED2Ev : 76 -> 84
~ -[GEOSimpleTileRequester activity] : 36 -> 40
~ -[GEOTileSetInfo .cxx_destruct] : 40 -> 20
~ -[GEOActiveTileSet _readSupportedLanguages] : 216 -> 224
~ -[_GEOSimpleTileRequesterOperation .cxx_destruct] : 212 -> 204
~ -[GEODataURLSessionTask .cxx_destruct] : 212 -> 200
~ -[GEODataRequest .cxx_destruct] : 168 -> 156
~ -[_GEOSimpleTileRequesterOperation httpResponseStatusCode] : 96 -> 120
~ -[GEODataURLSessionTask clientMetrics] : 624 -> 632
~ -[_GEOSimpleTileRequesterOperation isExistingCachedDataCurrent] : 36 -> 28
~ -[GEODataURLSessionTask downloadedFileURL] : 16 -> 24
~ __ZN12_GLOBAL__N_19isolationEv : 108 -> 84
~ -[GEOSimpleTileRequester balancer] : 28 -> 36
~ -[GEOTileRequester delegateQueue] : 8 -> 16
~ -[GEOActiveTileSet countryRegionAllowlists] : 72 -> 80
~ -[GEOTileRequestBalancer _pruneEmptyRequesters] : 244 -> 268
~ -[GEOActiveTileSet _readCountryRegionAllowlists] : 220 -> 228
~ -[GEOTileRequestBalancer requesters] : 20 -> 32
~ -[GEOPrioritizedTileKeys count] : 32 -> 44
~ -[GEOTileData fileURL] : 20 -> 36
~ -[GEOSimpleTileRequester highestRunningOperationPriority] : 140 -> 132
~ _GEOTileUnpackageBaseAndLocalization : 248 -> 240
~ -[GEOReachability _resetErrors] : 164 -> 144
~ -[GEOVectorTile .cxx_construct] : 52 -> 28
~ __ZN3geo5codec16PBDataReaderObjCC1EPKhm : 148 -> 160
~ -[GEODataURLSessionTask delegateQueue] : 20 -> 28
~ -[GEOClientNetworkTransactionMetrics secureConnectStart] : 20 -> 40
~ -[GEODataURLSessionTask(Convenience) entityTag] : 116 -> 120
~ -[GEODataURLSessionTask receivedData] : 20 -> 32
~ -[GEOTileRequest loadReason] : 8 -> 28
~ _GeoServicesConfig_ReportTileNetworkEventDetails_Metadata_block_invoke_116 : 28 -> 20
~ _GEOTileKeyZoom : 100 -> 96
~ __ZNSt3__16vectorI28GeoCodecsContourLinesFeatureN3geo17allocator_adapterIS1_NS2_5codec15zone_mallocatorEEEED2B8ne200100Ev : 228 -> 240
~ -[GEOResourceManifestManager _purgeCachedResourceInfo] : 212 -> 204
~ -[GEOURLInfoSet .cxx_destruct] : 1232 -> 1240
~ -[GEOActiveTileSet clearAvailableTiles] : 156 -> 152
~ -[GEOActiveTileSet .cxx_destruct] : 216 -> 228
~ -[GEOLocationShifter dealloc] : 140 -> 164
~ __ZNSt3__110__function6__funcI22GEOOscillatingFunctionNS_9allocatorIS2_EEFddEE18destroy_deallocateEv : 76 -> 84
~ -[GEOLocalizedString _readLocale] : 200 -> 224
~ -[_GEOPlaceDataItem addressObject] : 144 -> 152
~ __ZN8addr_obj12FingerprintsC2ERKNS_18AddressObjectProtoE : 588 -> 612
~ -[GEOPDComponentValue entity] : 60 -> 68
~ __ZN8addr_obj15V1AddressObjectC2ERKNS_12LocalizationERKNS_12FingerprintsERKNS_18AddressObjectProtoERKNS_17AddressObjectBase20AddressObjectVersionE : 456 -> 436
~ -[GEOPDPlace(PlaceDataExtras) _entityName] : 280 -> 268
~ -[GEOLocalizedString hasLocale] : 68 -> 60
~ -[GEOPDComponentValue placeInfo] : 68 -> 76
~ __ZN13AddrObjGoogle8protobuf23SourceCodeInfo_LocationC1Ev : 16 -> 8
~ __ZN8addr_obj6Logger11setCallbackEPFvNS0_7LogTypeERKNSt3__112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEESA_SA_E : 20 -> 28
~ __ZNSt3__114__split_bufferIN8addr_obj12Fingerprints11FingerprintERNS_9allocatorIS3_EEE17__destruct_at_endB8ne200100EPS3_ : 92 -> 80
~ -[GEOConfigStorageSetValueForKeyRequest keyValue] : 40 -> 44
~ -[GEOMapItemStorage(GEOMapItem) _clientAttributes] : 20 -> 28
~ -[GEOPDModuleLayoutEntry init] : 116 -> 120
~ -[GEOAPSessionData .cxx_destruct] : 36 -> 24
~ -[GEOPDPlace init] : 124 -> 100
~ -[GEOMapItemStorage _readAdditionalPlaceDatas] : 216 -> 208
~ -[GEOPDPlace _readMapsId] : 212 -> 224
~ _GEOPDMapsIdentifierReadAllFrom : 652 -> 672
~ -[GEOPDPlace mapsId] : 64 -> 72
~ -[GEOMapItemStorage internalDetourInfo] : 64 -> 88
~ -[GEOPDPlace _readComponents] : 232 -> 208
~ sub_186776618 -> sub_18674e538 : 456 -> 480
~ _GEOPDAmenitiesReadSpecified : 1600 -> 1608
~ -[GEOPDAssociatedApp init] : 104 -> 116
~ -[GEOPDRelatedPlace init] : 120 -> 108
~ _GEOPDRelatedPlaceReadAllFrom : 408 -> 420
~ _GEOPDRelatedPlaceReadSpecified : 2116 -> 2104
~ -[GEOPDAttribution init] : 96 -> 120
~ -[GEOPDReview init] : 100 -> 108
~ _GEOPDEntityReadAllFrom : 416 -> 428
~ _GEOPDPlaceInfoReadSpecified : 2684 -> 2696
~ ___25-[_GEOPlaceDataItem name]_block_invoke : 100 -> 88
~ ___42-[GEOPDPlace(PlaceDataExtras) _entityName]_block_invoke : 172 -> 184
~ -[GEOPDComponentValue addressObject] : 72 -> 80
~ _GEOPDPlaceReadAllFrom : 428 -> 420
~ sub_18677d850 -> sub_1867557c8 : 180 -> 188
~ -[GEOMapItemStorage placeData] : 88 -> 80
~ __ZN8addr_obj6Base6412encodeStringERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE : 1472 -> 1448
~ __ZNSt3__16vectorIN8addr_obj12Fingerprints11FingerprintENS_9allocatorIS3_EEE9push_backB8ne200100ERKS3_ : 64 -> 88
~ -[GEOMapItemStorage(GEOMapItem) name] : 148 -> 136
~ -[GEOPDEntity(PlaceDataExtras) bestLocalizedName] : 108 -> 120
~ -[GEOPDEntity names] : 68 -> 76
~ -[GEOStructuredAddress .cxx_destruct] : 472 -> 464
~ -[GEOPDBounds init] : 120 -> 96
~ _GEOPDBoundsReadAllFrom : 436 -> 424
~ _GEOPDBoundsReadSpecified : 1992 -> 1996
~ _GEOPDAddressObjectReadAllFrom : 596 -> 604
~ _GEOPDPlaceInfoReadAllFrom : 464 -> 488
~ -[GEOPDPlaceInfo init] : 112 -> 100
~ -[GEOPDComponent(PlaceDataExtras) statusCodeIsValid] : 80 -> 60
~ -[GEOPDHours init] : 120 -> 116
~ -[GEOPDQuickLink init] : 120 -> 100
~ _GEOPDRapReadAllFrom : 820 -> 840
~ -[GEOPDCaptionedPhoto init] : 116 -> 96
~ _GEOPDBusinessHoursReadAllFrom : 432 -> 424
~ -[GEOPDRestaurantReservationLink restaurantLinks] : 56 -> 76
~ -[GEOPDBusinessHours init] : 112 -> 124
~ __fetchPhotoRelatedDataAttributionsForPlaceData : 1104 -> 1080
~ _GEOPDHoursReadAllFrom : 420 -> 408
~ _GEOPDHoursReadSpecified : 2012 -> 2024
~ _GEOPDResultSnippetReadAllFrom : 416 -> 436
~ _GEOPDResultSnippetReadSpecified : 2460 -> 2464
~ -[GEOPDComponent attribution] : 64 -> 72
~ _GEOStyleAttributesReadAllFrom : 936 -> 916
~ _GEOPDStorefrontBundleIdReadAllFrom : 1044 -> 1032
~ -[GEOMapItemStorage hash] : 264 -> 256
~ -[GEOPDComponentValue .cxx_destruct] : 2088 -> 2096
~ __GEOPDPlaceCallReadAllRecursiveWithoutSynchronized : 116 -> 108
~ -[GEOPDAddressObject .cxx_destruct] : 104 -> 112
~ -[GEOPDISO3166Code .cxx_destruct] : 152 -> 144
~ -[GEOMapItemIdentifier .cxx_destruct] : 88 -> 96
~ -[GEOPDAttribution _readVendorId] : 184 -> 188
~ -[GEOPDShardedId .cxx_destruct] : 84 -> 112
~ -[GEOMapItemClientAttributes _readCorrectedLocationAttributes] : 200 -> 224
~ -[GEOPDComponentValue captionedPhoto] : 84 -> 80
~ -[GEOPDCaptionedPhoto attribution] : 216 -> 224
~ -[_GEOPlaceItem _placeData] : 36 -> 32
~ -[GEOMapItemStorage(GEOMapItem) _placeResult] : 88 -> 92
~ -[_GEOPlaceItem _placeResult] : 20 -> 16
~ -[GEOMapItemStorage(GEOMapItem) _place] : 92 -> 96
~ -[_GEOPlaceItem _place] : 24 -> 20
~ +[GEOMapService shouldResolveAttribution] : 24 -> 32
~ +[GEOSearchAttributionManifestManager sharedManager] : 92 -> 84
~ -[_GEOPlaceDataItem _placeData] : 28 -> 24
~ -[GEOPlace _readEntryPoints] : 204 -> 208
~ -[GEOAnalyticsPipelineStateData hasMapUiShownWeatherShown] : 24 -> 32
~ -[GEOMapItemStorageUserValues _readName] : 224 -> 216
~ -[GEOPDPlace hash] : 696 -> 676
~ -[GEOPDShardedId hash] : 288 -> 308
~ -[GEOPDRating init] : 100 -> 108
~ -[GEOMapItemStorageUserValues .cxx_destruct] : 184 -> 208
~ -[GEOPDComponentValue styleAttributes] : 76 -> 84
~ _GEOSearchAttributionManifestReadSpecified : 1696 -> 1680
~ ___57-[GEOFeatureStyleAttributes(PersonalizedItem) isLabelPOI]_block_invoke : 604 -> 588
~ _GEOSearchAttributionSourceReadAllFrom : 428 -> 420
~ _GeoServicesConfig_FeatureStyleAttributePOITypesThatAreLabels_Metadata_block_invoke_144 : 12 -> 20
~ _GEOPDTextBlockReadAllFrom : 420 -> 408
~ _GEOPDTextBlockReadSpecified : 1372 -> 1376
~ -[GEOMapItemStorage(GEOMapItem) _hasMUID] : 56 -> 84
~ -[GEOPDMessageLink init] : 116 -> 120
~ -[_GEOPlaceDataItem _hasMUID] : 64 -> 40
~ -[GEOSearchAttributionSource _readLocalizedAttributions] : 184 -> 208
~ -[GEOMapItemIdentifier muid] : 128 -> 136
~ -[GEOLocalizedAttribution init] : 120 -> 124
~ -[GEOPDShardedId hasMuid] : 40 -> 36
~ _GEOPDMessageLinkReadAllFrom : 412 -> 416
~ -[GEOPDShardedId muid] : 40 -> 24
~ _GEOPDMessageLinkReadSpecified : 2524 -> 2528
~ -[_GEOPlaceDataItem _muid] : 12 -> 20
~ -[GEOLocalizedAttribution _readLogoURLs] : 200 -> 204
~ _GEOPDShardedIdReadAllFrom : 2276 -> 2272
~ -[GEOLocalizedAttribution snippetLogoURLs] : 96 -> 88
~ -[GEOMapItemStorage(GEOMapItem) _photos] : 84 -> 80
~ _GEOPDQuickLinkReadSpecified : 1324 -> 1328
~ ___42-[_GEOPlaceDataItem _allPhotoAttributions]_block_invoke : 88 -> 84
~ -[GEOPDCaptionedPhoto _readPhoto] : 184 -> 188
~ -[GEOPDFlyover init] : 108 -> 124
~ _GEOPDFlyoverReadSpecified : 1748 -> 1768
~ _AppleMediaServicesLibraryCore : 324 -> 316
~ -[GEOPDContainedPlace init] : 96 -> 108
~ _GEOPDContainedPlaceReadAllFrom : 432 -> 420
~ _GEOPDContainedPlaceReadSpecified : 1800 -> 1812
~ -[GEODefaultPhotoInfoProvider designatedURLType] : 16 -> 8
~ -[GEOPDPhotoContent url] : 72 -> 80
~ -[GEODefaultPhotoInfoProvider sizeRatio] : 140 -> 128
~ -[GEOPDPlaceQuestionnaireResult init] : 104 -> 116
~ _GEOPDGroundViewLabelReadAllFrom : 940 -> 928
~ _GEOPDGroundViewLabelInfoReadSpecified : 1788 -> 1768
~ -[GEOSearchAttributionSource _readAttributionRequirements] : 180 -> 200
~ -[GEOSearchAttributionLoader .cxx_destruct] : 28 -> 40
~ -[GEOLocalizedAttribution language] : 88 -> 72
~ -[GEOMapItemPhotoOptions allowSmaller] : 36 -> 12
~ -[_GEOPlaceDataPhoto .cxx_destruct] : 104 -> 112
~ -[GEOPDPOIClaim .cxx_destruct] : 92 -> 112
~ -[GEOPDSupportsOfflineMaps .cxx_destruct] : 36 -> 48
~ -[GEOPDModuleLayoutEntry .cxx_destruct] : 164 -> 156
~ ____loadAttributions_block_invoke : 376 -> 372
~ -[GEOPDGroundViewLabelInfo .cxx_destruct] : 172 -> 152
~ _GEOAttributionAppReadAllFrom : 404 -> 416
~ -[GEOPDPlaceCollection init] : 124 -> 112
~ -[GEOAttributionApp init] : 96 -> 108
~ sub_1867ac8e8 -> sub_186784894 : 132 -> 120
~ -[GEOPDAttribution attributionUrls] : 84 -> 76
~ -[GEOPDComponentValue templatePlace] : 72 -> 80
~ -[GEOPDAttribution externalItemId] : 84 -> 76
~ -[GEOPDTemplatePlace templateDatas] : 76 -> 84
~ -[GEOPDTemplateData footer] : 80 -> 72
~ __actionURLSchemes : 448 -> 456
~ _GEOStyleAttributeReadAllFrom : 1096 -> 1116
~ _GEOPDPlaceQuestionnaireResultReadSpecified : 2940 -> 2944
~ -[GEOPDCategorizedPhotos photos] : 100 -> 76
~ _GEOPDButtonModuleConfigurationReadAllFrom : 648 -> 672
~ _GEOPDButtonItemReadSpecified : 1656 -> 1664
~ _GEOPDUnifiedActionModuleConfigurationReadAllFrom : 660 -> 652
~ __GEOPDGroupDataCallReadAllRecursiveWithoutSynchronized : 416 -> 424
~ -[GEOPDPlacecardLayoutConfiguration hash] : 96 -> 76
~ ____registerSupportSourcesIfNecessary_block_invoke : 256 -> 236
~ _GEOPDActionDataReadSpecified : 1868 -> 1864
~ -[GEOMapSubscriptionGetIdentifiersForPairedDeviceSyncRequest isValid] : 28 -> 12
~ -[GEOAutomobileOptions .cxx_destruct] : 136 -> 132
~ -[GEOCountryConfiguration currentCountrySupportsElectricVehicleRouting] : 28 -> 20
~ -[GEOPDEntity _readStyleAttributes] : 208 -> 216
~ _MapsFeaturesConfig_StandaloneWatchOffline_Metadata_block_invoke_34 : 40 -> 28
~ -[GEOMapSubscriptionGetIdentifiersForPairedDeviceSyncReply .cxx_destruct] : 44 -> 24
~ -[GEOMapDataSubscriptionManager .cxx_destruct] : 140 -> 132
~ -[GEOMapDataSubscriptionRemoteSyncManager .cxx_destruct] : 112 -> 124
~ -[GEOMapDataSubscriptionRemoteDownloadManager .cxx_destruct] : 112 -> 100
~ -[GEOMapDataSubscriptionRemotePersistence .cxx_destruct] : 8 -> 16
~ -[GEOMapServiceTraits hasDevicePlatform] : 44 -> 28
~ +[GEOIdealTransportTypeFinder idealTransportType] : 36 -> 20
~ _GEOPDTemplatePlaceModuleConfigurationReadAllFrom : 1720 -> 1744
~ _GEOPDPhotoContentReadAllFrom : 1424 -> 1416
~ ___getAVExternalDeviceClass_block_invoke : 160 -> 168
~ _GeoServicesConfig_ITTEnableDistanceThresholds_Metadata_block_invoke_263 : 36 -> 12
~ -[GEOMapItemHandle _readPlaceRefinementParameters] : 200 -> 204
~ _GEOPDPlaceRefinementParametersReadSpecified : 3428 -> 3416
~ _GeoServicesConfig_MapItemHandleCacheMaxItemCost_Metadata_block_invoke_361 : 24 -> 32
~ __GEOMapItemHandleCallReadAllRecursiveWithoutSynchronized : 120 -> 124
~ -[GEOPDPlaceRefinementParameters hash] : 432 -> 460
~ _GEOConfigSetArray : 24 -> 36
~ -[GEOTransitOptions init] : 96 -> 120
~ -[GEOCyclingOptions init] : 112 -> 108
~ -[GEOMapServiceTraits timeSinceMapEnteredForeground] : 40 -> 32
~ -[GEOPDPhoto init] : 104 -> 112
~ -[GEOMapServiceTraits currentLocaleCurrencySymbol] : 64 -> 68
~ -[GEOPDCollectionSuggestionParameters init] : 96 -> 124
~ -[GEOPDPlaceRequest(PlaceDataExtras) localTimestamp] : 260 -> 264
~ _GEOPDPlaceDescriptorResolutionParametersHasSensitiveFields : 84 -> 80
~ ____setDefaultArray_block_invoke_2 : 224 -> 228
~ -[GEOPDCollectionSuggestionParameters hash] : 316 -> 312
~ __GEOMapItemStorageCallReadAllRecursiveWithoutSynchronized : 420 -> 412
~ sub_1867bf2b8 -> sub_186797250 : 72 -> 76
~ -[GEOAttribution _readRegions] : 228 -> 204
~ -[GEORegionalResourceSet _readRegions] : 212 -> 200
~ _GEORegionalResourceTileKeyMake : 72 -> 64
~ _GEOTileKeyMakeEmpty : 40 -> 28
~ -[GEOPDPlaceRequest _readDisplayLanguages] : 208 -> 204
~ -[_GEOPlaceDataPhotoInfo .cxx_destruct] : 16 -> 20
~ _GEOPDSearchFieldPlaceholderParametersReadAllFrom : 1204 -> 1212
~ -[GEOPDAttribution(PlaceDataExtras) _isYelp] : 100 -> 92
~ -[GEOPDSearchFieldPlaceholderParameters hash] : 132 -> 128
~ -[GEOSearchAttributionInfo identifier] : 24 -> 16
~ -[GEOMapItemAttribution providerID] : 16 -> 8
~ _GEOGetSignedResourcesLog : 92 -> 100
~ -[GEOResourceLoadOperation .cxx_destruct] : 240 -> 244
~ -[GEORegionalResourceTileData .cxx_destruct] : 160 -> 148
~ __ZNSt3__112__hash_tableINS_17__hash_value_typeI11_GEOTileKeyNS_15__list_iteratorI9CacheItemPvEEEENS_22__unordered_map_hasherIS2_S7_7hashkey5eqkeyLb1EEENS_21__unordered_map_equalIS2_S7_SA_S9_Lb1EEENS_9allocatorIS7_EEE25__emplace_unique_key_argsIS2_JRKNS_21piecewise_construct_tENS_5tupleIJRKS2_EEENSL_IJEEEEEENS_4pairINS_15__hash_iteratorIPNS_11__hash_nodeIS7_S5_EEEEbEERKT_DpOT0_ : 1092 -> 1076
~ __ZN3geo13_geo_weak_ptrIU8__strongP11objc_objectEaSERKS4_ : 80 -> 96
~ __ZN3geo11_retain_ptrIU8__strongP12NSDictionaryNS_16_retain_objc_arcENS_17_release_objc_arcENS_10_hash_objcENS_11_equal_objcEEaSEOS8_ : 84 -> 92
~ -[GEOAnalyticsPipelineStateData hasMapSettingsWalkingAvoidBusyRoads] : 48 -> 24
~ +[GEOApplicationAuditToken supportsSecureCoding] : 28 -> 20
~ -[GEOAnalyticsPipelineStateData hasMapSettingsAvoidHills] : 24 -> 44
~ -[GEOTileKeyList(GEOXPCUtil) newXPCData] : 416 -> 428
~ -[GEOAnalyticsPipelineStateData hasMapSettingsAvoidBusyRoads] : 52 -> 40
~ __NSArraySafeEncodingCopy : 696 -> 708
~ -[GEOAnalyticsPipelineStateData hasMapSettingsEBike] : 44 -> 32
~ __ZN4mgcl4muid10decompressEPKcmPKiiPyim : 1156 -> 1160
~ -[GEOConfigStorageFallbackReader resync] : 264 -> 248
~ -[GEOConfigStorageCFPrefsReadOnly resync] : 8 -> 20
~ __ZN4mgcl4muid7Decoder6decEgkEiiPN3gcl17ArithmeticContextE : 500 -> 508
~ -[GEOPeer offlineCohortId] : 92 -> 84
~ __ZN4mgcl4ints15IntDecompressorItE10decompressEPKhmiimPt : 8224 -> 8236
~ -[GEOPDRoadAccessInfo .cxx_destruct] : 104 -> 112
~ -[GEOPDRap .cxx_destruct] : 48 -> 28
~ -[GEOPDStorefrontPresentation .cxx_destruct] : 152 -> 132
~ -[GEOPDFlyover clearLabelFrames] : 148 -> 156
~ -[GEOPDFlyover .cxx_destruct] : 128 -> 120
~ __ZNK22FeatureStyleAttributes7poiTypeEv : 144 -> 140
~ -[GEOResourceFilter .cxx_destruct] : 92 -> 88
~ ____ZL13_cacheMissErrv_block_invoke : 140 -> 144
~ -[GEOPDCaptionedPhoto .cxx_destruct] : 252 -> 240
~ _GEOErrorReason : 188 -> 168
~ -[GEOPDHours .cxx_destruct] : 128 -> 120
~ -[GEOPDRelatedPlace .cxx_destruct] : 104 -> 112
~ -[GEOResourceFilter dealloc] : 124 -> 104
~ -[GEOPDAssociatedApp .cxx_destruct] : 144 -> 136
~ -[GEOPDAmenities .cxx_destruct] : 128 -> 148
~ -[GEOPDBusinessHours .cxx_destruct] : 172 -> 192
~ -[GEOPDAttribution .cxx_destruct] : 208 -> 200
~ -[GEOPDRating .cxx_destruct] : 124 -> 152
~ -[GEOPDQuickLink .cxx_destruct] : 132 -> 136
~ ___37+[GEOReachability sharedReachability]_block_invoke : 84 -> 60
~ -[GEOSearchAttributionInfo .cxx_destruct] : 132 -> 124
~ -[GEOMapItemAttribution .cxx_destruct] : 128 -> 116
~ -[GEOPDRelatedPlace dealloc] : 100 -> 88
~ -[GEOPDCategorizedPhotos .cxx_destruct] : 164 -> 152
~ -[GEOPDPlaceQuestionnaireResult .cxx_destruct] : 168 -> 148
~ -[GEOMapItemMapsSyncAttributes _readMapsSyncIdentifier] : 204 -> 228
~ -[GEOPDBounds displayMapRegion] : 92 -> 100
~ __ZNK8addr_obj17AddressObjectBase15getLocalizationEv : 16 -> 8
~ -[GEOPDEntity namesCount] : 80 -> 88
~ -[GEOLocalizedString hasStringValue] : 76 -> 68
~ -[GEOPDRoadAccessInfo roadAccessPoints] : 72 -> 80
~ -[GEORoadAccessPoint location] : 44 -> 36
~ -[GEOPDEntity isDisputed] : 16 -> 24
~ -[GEOAddressObject hasKnownAccuracy] : 24 -> 16
~ -[GEOPDEntity hasIsPermanentlyClosed] : 48 -> 44
~ -[GEOBusiness _readSources] : 216 -> 220
~ -[GEOPDHours _readDays] : 212 -> 204
~ -[GEOTileRequester tearDown] : 136 -> 144
~ -[GEOPDHours daysCount] : 56 -> 80
~ -[GEOTileServerLocalProxyBatchContext .cxx_destruct] : 156 -> 164
~ -[GEOPDHours _readTimeRanges] : 228 -> 220
~ _GEOPDLocalTimeRangeReadAllFrom : 868 -> 884
~ _GEOPDHoursThresholdReadAllFrom : 1092 -> 1108
~ ___28-[GEOTileRequester tearDown]_block_invoke : 24 -> 32
~ -[GEOPDHours timeRangesCount] : 68 -> 64
~ -[GEOPhoto _readPhotoInfos] : 216 -> 220
~ -[GEOPDPhoto photoId] : 224 -> 220
~ -[GEOBusiness _readPhotos] : 220 -> 224
~ -[GEOPDEntity _readLocalizedCategorys] : 232 -> 228
~ -[GEOPlace hasName] : 80 -> 60
~ -[GEOPlace(GEOProtoExtras) firstBusiness] : 116 -> 104
~ -[GEOPlace business] : 88 -> 92
~ -[_GEOPlaceDataItem _customIconID] : 92 -> 100
~ -[GEOStyleAttributes customIconId] : 36 -> 28
~ -[_GEOPlaceDataItem _enhancedPlacement] : 132 -> 124
~ -[GEOFeatureStyleAttributes(PersonalizedItem) isTransit] : 56 -> 32
~ -[_GEOPlaceDataItem _place] : 132 -> 156
~ __ZL13_cacheMissErrv : 96 -> 104
~ -[_GEORegionalResourcesTileLoader .cxx_destruct] : 96 -> 88
~ -[GEOTileRequester .cxx_destruct] : 132 -> 152
~ -[GEOTileRequest .cxx_destruct] : 216 -> 192
~ __ZNSt3__110__function6__funcIZN3geo5codec20_readMaterialRastersEP8VMP4TilePK16GeoCodecsTileKeyRKNS_10shared_ptrINS3_10VectorTileEEEE3$_0NS_9allocatorISE_EEFvP11VMP4ChapterEE18destroy_deallocateEv : 8 -> 20
~ -[GEOEnhancedPlacement elevationInMeters] : 36 -> 24
~ __ZNSt3__110__function6__funcIZN3geo5codec26_readStyleAttributeRastersEP8VMP4TilePK16GeoCodecsTileKeyRKNS_10shared_ptrINS3_10VectorTileEEEbE3$_0NS_9allocatorISE_EEFvP11VMP4ChapterEE18destroy_deallocateEv : 12 -> 24
~ __GEOPDAmenityValueCallReadAllRecursiveWithoutSynchronized : 272 -> 260
~ __ZN3geo5codec19MercatorDequantizer8readInfoEP11VMP4Chapter : 344 -> 356
~ __GEOPDAmenitiesCallReadAllRecursiveWithoutSynchronized : 404 -> 424
~ __ZN3geo5codec14_readMaterialsEP11VMP4ChapterRNSt3__16vectorIyNS_17allocator_adapterIyNS0_15zone_mallocatorEEEEERNS4_I12VMP4MaterialNS5_ISA_S6_EEEERNS4_ImNS5_ImS6_EEEER25FeatureStyleAttributesSetb : 3376 -> 3396
~ _GEOPDModuleReadAllFrom : 432 -> 444
~ __GEOPDRelatedPlaceCallReadAllRecursiveWithoutSynchronized : 248 -> 260
~ _GEOPDUserReadSpecified : 1352 -> 1328
~ __GEOPDRatingCallReadAllRecursiveWithoutSynchronized : 408 -> 420
~ __ZNSt3__16vectorIN3gcl7Vector3IiEENS_9allocatorIS3_EEE8__appendEm : 684 -> 696
~ __GEOPDReviewCallReadAllRecursiveWithoutSynchronized : 300 -> 308
~ ___63-[GEOAltitudeManifest(Internal) getvalidFlyOverAnimationIDPool]_block_invoke : 200 -> 192
~ __GEOPDPhotoCallReadAllRecursiveWithoutSynchronized : 236 -> 224
~ __ZNSt3__110__function6__funcIZN3geo5codec9_readPoisEP8VMP4TileRK28GeoCodecsVMP4DecodingOptionsRKNS_10shared_ptrINS3_10VectorTileEEEE3$_0NS_9allocatorISE_EEFvmfEEclEOmOf : 60 -> 40
~ -[GEOPDLocalizedAddress init] : 120 -> 108
~ __ZNSt3__110__function6__funcIZN3geo5codec9_readPoisEP8VMP4TileRK28GeoCodecsVMP4DecodingOptionsRKNS_10shared_ptrINS3_10VectorTileEEEE3$_0NS_9allocatorISE_EEFvmfEE7destroyEv : 32 -> 12
~ _GEOPDLocalizedAddressReadSpecified : 1336 -> 1344
~ -[GEOAddress init] : 112 -> 104
~ __GEOPDAddressCallReadAllRecursiveWithoutSynchronized : 564 -> 584
~ __ZN3geo5codec14decodeVerticesEP11VMP4ChapterPP24GeoCodecsCurveVertexPoolPP19GeoCodecsVertexPoolb : 2896 -> 2904
~ __GEOPDCategoryCallReadAllRecursiveWithoutSynchronized : 260 -> 252
~ __ZN3geo5codec20_makeSpaceForShieldsEmPmRKNSt3__110shared_ptrINS0_10VectorTileEEE : 468 -> 480
~ __GEOPDEntityCallReadAllRecursiveWithoutSynchronized : 1008 -> 996
~ __ZNSt3__120__shared_ptr_pointerIPN8addr_obj15V2AddressObjectENS_10shared_ptrIS2_E27__shared_ptr_default_deleteIS2_S2_EENS_9allocatorIS2_EEE16__on_zero_sharedEv : 60 -> 48
~ __ZN8addr_obj15V2AddressObjectD0Ev : 84 -> 76
~ __ZNSt3__120__shared_ptr_pointerIPN8addr_obj15V2AddressObjectENS_10shared_ptrIS2_E27__shared_ptr_default_deleteIS2_S2_EENS_9allocatorIS2_EEE21__on_zero_shared_weakEv : 20 -> 28
~ _GEOPDOrientedPositionReadAllFrom : 1656 -> 1668
~ _GEOPDStorefrontViewReadAllFrom : 436 -> 416
~ -[GEOConfigStorageDirectReadWrite _clearWriteTransaction] : 112 -> 100
~ __ZN3geo5codec21decodeSectionEncodingEP9BitstreamPP19GeoCodecsVertexPoolbPK16GeoCodecsTileKeyP27GeoCodecsVectorTileRawPoint : 2416 -> 2436
~ __GEOPDPhotoPositionCallReadAllRecursiveWithoutSynchronized : 364 -> 356
~ ___31-[GEODataURLSessionTask cancel]_block_invoke : 276 -> 264
~ -[GEOPDStorefrontView init] : 104 -> 124
~ _GEOPDCameraMetadataReadSpecified : 2640 -> 2632
~ -[GEODataURLSessionTask requestCounterTicket] : 104 -> 80
~ _GEOPDLensProjectionReadAllFrom : 2480 -> 2488
~ _GEOErrorDomain : 12 -> 36
~ _GEOPDRigMetricsReadAllFrom : 1104 -> 1116
~ __ZN3geo5codec33decodeLabelLineRangeUsingTileLineEP9BitstreamP23GeoCodecsLabelLineRangeP30SharedLabelLineRangeDecodeInfoP28TileLabelLineRangeDecodeInfo : 412 -> 400
~ -[GEOAbstractRequestResponseTicket .cxx_destruct] : 132 -> 104
~ -[GEOPDPlaceRequest .cxx_destruct] : 308 -> 328
~ -[GEOPDComponentFilter .cxx_destruct] : 2004 -> 2024
~ -[GEOPDPlaceCollectionFilter .cxx_destruct] : 20 -> 44
~ -[GEOPDAnalyticMetadata .cxx_destruct] : 312 -> 308
~ -[GEOAbstractTicket .cxx_destruct] : 80 -> 92
~ -[GEOTransitOptions .cxx_destruct] : 120 -> 112
~ -[GEOUserPreferences .cxx_destruct] : 92 -> 100
~ __ZNSt3__116allocator_traitsIN3geo17allocator_adapterIZNS1_5codec14_findCrossingsERKNS_10shared_ptrINS3_10VectorTileEEEE11FeatureInfoNS3_15zone_mallocatorEEEE10deallocateB8ne200100ERSB_PS9_m : 220 -> 208
~ -[GEOResourceManifestDownloadTask .cxx_destruct] : 152 -> 132
~ __ZNSt3__16vectorI24GeoCodecsTrafficSkeletonN3geo17allocator_adapterIS1_NS2_5codec15zone_mallocatorEEEE12emplace_backIJRS1_EEES9_DpOT_ : 852 -> 840
~ -[GEOReportedProgress totalUnitCount] : 36 -> 8
~ -[GEOFormattedString init] : 104 -> 96
~ __GEOFormattedStringCallReadAllRecursiveWithoutSynchronized : 468 -> 460
~ __GEOPDResultSnippetCallReadAllRecursiveWithoutSynchronized : 444 -> 424
~ __GEOMapRegionCallReadAllRecursiveWithoutSynchronized : 248 -> 268
~ __GEOPDBoundsCallReadAllRecursiveWithoutSynchronized : 128 -> 108
~ __GEOPDCategorizedPhotosCallReadAllRecursiveWithoutSynchronized : 428 -> 416
~ __GEOPDPlaceQuestionnaireResultCallReadAllRecursiveWithoutSynchronized : 304 -> 316
~ __GEOPDBusinessHoursCallReadAllRecursiveWithoutSynchronized : 312 -> 304
~ -[_GEOPlaceDataItem _hasResultProviderID] : 24 -> 28
~ -[_GEOPlaceItem _hasResultProviderID] : 48 -> 44
~ -[_GEOPlaceDataItem _placeDisplayType] : 24 -> 12
~ -[GEOPDPlace(PlaceDataExtras) placeDisplayType] : 220 -> 204
~ -[_GEOPlaceItem _placeType] : 76 -> 68
~ __GEOMapItemIsEqualForWithinDistanceExcludingName : 320 -> 312
~ ___47-[GEOPDPlace(PlaceDataExtras) placeDisplayType]_block_invoke : 128 -> 140
~ -[GEOMapItemStorage(GEOMapItem) _placeType] : 76 -> 72
~ _GEOMapItemIsEqualToMapItemForPurposeWithinDistance : 1520 -> 1524
~ ___31-[_GEOPlaceDataItem _placeType]_block_invoke : 144 -> 140
~ -[GEOPlace hasLocalSearchProviderID] : 28 -> 32
~ sub_1867e2118 -> sub_1867b9fd0 : 132 -> 128
~ sub_1867e4408 -> sub_1867bc2bc : 180 -> 172
~ -[GEOETARequestSimple request] : 20 -> 40
~ -[GEOETARequest _readServiceTags] : 204 -> 228
~ _GeoServicesConfig_ValidateSensitiveFieldsAtSend_ETA_Metadata_block_invoke_394 : 24 -> 36
~ -[GEOKeyBagNotification state] : 20 -> 8
~ -[GEOMapService(ExternalRequestersOnly) serializedClientMetadataForParsec] : 328 -> 340
~ -[GEOPDClientMetadata resultListAttributionSupport] : 108 -> 104
~ -[GEOExperimentConfiguration _parsecClientMetadata] : 88 -> 112
~ -[GEOABAssignmentResponse _readParsecClientMetadata] : 212 -> 224
~ -[GEOPDClientMetadata _readBusinessChatPreflightIdentifiers] : 216 -> 228
~ ___GEOGetNetEventFileManagerLog_block_invoke : 76 -> 92
~ ___GEOGetAnalyticDataFileLog_block_invoke : 72 -> 92
~ ___34-[GEOSystemMonitor _systemDidWake]_block_invoke : 116 -> 144
~ -[GEOTileCache _receivedMemoryNotification] : 136 -> 120
~ -[GEOMapFeatureAccess allowNetworkTileLoad] : 16 -> 8
~ -[GEOComposedRouteLeg stepRange] : 12 -> 24
~ -[GEORouteMatch stepIndex] : 32 -> 8
~ _GEOMapRectMakeWithRadialDistance : 112 -> 116
~ -[GEOURLInfo .cxx_destruct] : 92 -> 108
~ ___SetXPCValue_block_invoke : 240 -> 264
~ -[GEOAnalyticsPipelineStateData mapViewLocationPuckInViewport] : 32 -> 20
~ -[GEOLogMsgState _readMapViewLocation] : 228 -> 208
~ -[GEOAnalyticsPipelineStateData mapViewLocationIsTourist] : 24 -> 44
~ -[GEOLogMsgState mapViewLocation] : 84 -> 72
~ -[GEOCarInfo init] : 112 -> 104
~ -[GEOAnalyticsPipelineStateData mapUiLayoutInfo] : 120 -> 108
~ -[GEOLogMsgState mapUi] : 92 -> 72
~ -[GEOAnalyticsPipelineStateData mapSettingsIsHandsFreeProfileEnabled] : 40 -> 28
~ -[GEOLogMsgState _readMapUi] : 208 -> 220
~ -[GEOAnalyticsPipelineStateData mapSettingsWalkingVoiceSettings] : 112 -> 120
~ -[GEODirectionsResponse sessionState] : 84 -> 88
~ -[GEOFormattedString .cxx_destruct] : 212 -> 232
~ ___48-[GEOUserAccountInfo isPrimaryICloudAccountPAID]_block_invoke : 104 -> 124
~ -[GEOLogMsgEventId .cxx_destruct] : 28 -> 40
~ -[GEOUserAccountInfo isPrimaryICloudAccountPAID] : 400 -> 420
~ _GEOBatchOpaqueAppID : 8 -> 32
~ -[GEORouteMatch isGoodMatch] : 28 -> 24
~ -[GEOComposedRouteStep startRouteCoordinate] : 16 -> 20
~ -[GEORouteMatch .cxx_construct] : 12 -> 20
~ _GEOBearingFromCoordinateToCoordinate : 176 -> 168
~ -[GEOComposedRoute sections] : 32 -> 8
~ _GEOMapRectInset : 68 -> 88
~ -[GEOComposedRouteSection startPointIndex] : 24 -> 28
~ -[GEOComposedRouteCoordinateArray _length] : 336 -> 356
~ _GEOPolylineCoordinateEqual : 76 -> 88
~ -[GEOComposedRoute coordinates] : 36 -> 24
~ _GEOPolylineCoordinateIsInvalid : 36 -> 48
~ -[GEORouteMatch routeCoordinate] : 28 -> 16
~ _GEOPolylineCoordinateIsValid : 24 -> 36
~ -[GEORouteMatch legIndex] : 44 -> 40
~ -[GEOComposedRouteSection endPointIndex] : 20 -> 24
~ -[GEOComposedRoute steps] : 8 -> 28
~ -[GEOComposedRouteLeg endPointIndex] : 20 -> 32
~ -[GEOComposedRoute elevationModel] : 8 -> 36
~ -[GEOComposedRouteStep endPointIndex] : 20 -> 12
~ -[GEORouteMatcher .cxx_destruct] : 156 -> 168
~ -[GEOComposedRoute revisionIdentifier] : 32 -> 28
~ -[GEOComposedRouteSection composedRouteSegmentIndex] : 36 -> 8
~ -[GEOComposedRoute source] : 8 -> 28
~ _GeoServicesConfig_UseProductionURLs_Metadata_block_invoke_6 : 32 -> 12
~ -[GEOComposedRouteCoordinateArray usesRoutingPathPoints] : 24 -> 20
~ -[GEONavigationDrivingMapMatcher transportType] : 8 -> 32
~ -[GEONavigationMapMatcher previousMatchResult] : 16 -> 24
~ -[GEONavigationMatchResult routeMatch] : 16 -> 8
~ -[GEONavigationMapMatcher routeMatcher] : 20 -> 28
~ -[GEOLocation rawCourse] : 124 -> 116
~ -[GEONavigationMapMatcher route] : 8 -> 20
~ -[GEOComposedRoute usesRoutingPathPoints] : 16 -> 12
~ -[GEOStructuredAddress thoroughfare] : 28 -> 20
~ _GEOPolylineCoordinateRangeIsInvalid : 108 -> 84
~ ___33-[GEOPathMatcher _cachedSegments]_block_invoke : 96 -> 76
~ -[GEOMatchedPathSegment startRouteCoordinate] : 52 -> 32
~ -[GEORouteMatcher route] : 20 -> 12
~ __ZL23GEOGetGEOPathMatcherLogv : 88 -> 84
~ -[GEOMatchedPathSegment endRouteCoordinate] : 44 -> 56
~ _GEOPolylineCoordinateRangeIntersectsRange : 124 -> 112
~ -[GEOMatchedPathSegment pointCount] : 44 -> 24
~ -[GEORouteMatcher targetLegIndex] : 28 -> 16
~ -[GEOMatchedPathSegment range] : 84 -> 56
~ -[GEOMultiSectionFeature roadWidth] : 44 -> 52
~ -[GEOPolylineCoordinateIterator current] : 24 -> 12
~ _GEOClosestCoordinateOnLineSegmentFromCoordinate3D : 144 -> 124
~ -[GEORouteMatcher useMatchedCoordinateForMatching] : 32 -> 12
~ -[GEORouteMatch road] : 12 -> 20
~ -[GEOMatchedPathSegment road] : 36 -> 8
~ -[GEOMapFeatureRoad isTunnel] : 80 -> 56
~ _GEOPolylineCoordinateWithinRange : 92 -> 112
~ _GEOLocationCoordinate3DLerp : 52 -> 44
~ -[GEOMapFeatureLine coordinates3d] : 740 -> 716
~ -[GEOMatchedPathSegment .cxx_construct] : 20 -> 40
~ -[GEOLocation timestamp] : 28 -> 32
~ -[GEORouteMatch step] : 96 -> 104
~ -[GEOMatchedPathSegment startLocationCoordinate] : 36 -> 24
~ -[_GEOCandidateRouteMatch .cxx_construct] : 12 -> 28
~ -[GEOFeature attributes] : 172 -> 180
~ -[GEOFeatureStyleAttributes isTunnel] : 92 -> 84
~ -[GEOMapFeatureRoad roadWidth] : 76 -> 92
~ -[GEOLocation course] : 16 -> 40
~ -[GEORouteMatcher useStrictInitialOnRouteCriteria] : 24 -> 32
~ -[GEOComposedRouteStep routeSegmentType] : 32 -> 36
~ -[GEORouteMatch consecutiveProgressionsOffRoute] : 24 -> 20
~ -[GEOMapFeatureMultiSegmentRoad feature] : 108 -> 132
~ -[GEORouteMatcher _topRouteMatchCandidate] : 8 -> 36
~ -[GEODrivingRouteMatcher _supportsSnapping] : 140 -> 156
~ -[GEORouteMatch detailedMatchInfo] : 20 -> 8
~ -[GEONavigationMapMatcher roadMatcher] : 28 -> 8
~ -[GEORouteMatch candidateSteps] : 24 -> 20
~ -[GEOComposedRouteMutableData etaRoute] : 12 -> 16
~ -[GEOComposedRoute endRouteCoordinate] : 40 -> 60
~ -[GEOComposedRouteLeg endRouteCoordinate] : 56 -> 36
~ -[GEOComposedRoute startRouteCoordinate] : 16 -> 36
~ -[GEOComposedRouteLeg legIndex] : 20 -> 28
~ -[GEONavigationMatchResult roadMatch] : 32 -> 36
~ ___31-[GEOComposedRoute mutableData]_block_invoke : 20 -> 40
~ -[GEOComposedRouteLeg destination] : 24 -> 12
~ -[GEOComposedWaypoint _readMapItemStorage] : 220 -> 212
~ -[GEORouteMatch shouldProjectLocationAlongRoute] : 32 -> 20
~ -[GEONavRoutePreloadStrategy _performNextRequests] : 1520 -> 1508
~ -[GEOComposedWaypoint uniqueWaypointID] : 72 -> 84
~ -[GEOComposedWaypoint(GEOWaypointExtras) uniqueID] : 160 -> 180
~ -[GEOComposedWaypoint _readUniqueWaypointID] : 220 -> 200
~ -[_GEOPlaceDataItem timezone] : 284 -> 292
~ -[GEOComposedRouteStep stepID] : 8 -> 20
~ -[GEOStep stepID] : 28 -> 20
~ -[GEOComposedRoute distance] : 16 -> 36
~ -[GEOComposedString .cxx_destruct] : 144 -> 124
~ -[GEONavigationProxy _sendPositionFromDestination] : 80 -> 108
~ -[GEOArrivalTimeAndDistanceInfo .cxx_destruct] : 16 -> 20
~ -[GEORouteMatch leg] : 188 -> 184
~ _GEORoundedMeasurementForDistance : 176 -> 168
~ __ZL23GEOGetGEOProbeCrumbsLogv : 92 -> 100
~ -[GEOArrivalTimeAndDistanceInfo arrivalTimeInfo] : 36 -> 8
~ -[GEOComposedRoute isWalkingOnlyTransitRoute] : 12 -> 32
~ sub_1867ea138 -> sub_1867c20d0 : 248 -> 228
~ -[GEOComposedRoute isOfflineRoute] : 36 -> 24
~ -[GEOComposedRouteLeg arrivalParameters] : 16 -> 28
~ -[GEOArrivalRegion arrivalRegion] : 36 -> 40
~ -[GEOMapRegion(GEOProtoExtras) coordinates] : 428 -> 420
~ __ZN3geo13containsPointIdEEbRKNSt3__16vectorIN2gm6MatrixIT_Li2ELi1EEENS1_9allocatorIS6_EEEERKS6_ : 368 -> 372
~ -[GEOComposedRoute lastEVStep] : 372 -> 392
~ -[GEOMapItemStorage(GEOMapItem) contactAddressType] : 220 -> 228
~ -[GEOComposedRouteSegment endStepIndex] : 32 -> 36
~ -[GEOComposedRoute segments] : 12 -> 20
~ -[GEOComposedWaypoint _readFindMyHandleID] : 216 -> 220
~ -[GEOComposedDrivingRouteStep evInfo] : 152 -> 136
~ -[GEOComposedRouteStep distance] : 36 -> 8
~ -[GEOComposedRoute isEVRoute] : 304 -> 312
~ -[GEOServerFormatStyleParser _parseIfNeeded] : 16 -> 40
~ sub_1867eb02c -> sub_1867c2fd0 : 20 -> 28
~ -[GEOServerFormatStyleParser tokenRanges] : 104 -> 92
~ -[GEOJunction drivingSide] : 8 -> 32
~ -[GEOComposedStringReplacementResult .cxx_destruct] : 128 -> 136
~ -[GEOCellConnectionQuality init] : 120 -> 100
~ -[GEOLogMsgEventNetworkSelectionHarvest .cxx_destruct] : 108 -> 112
~ -[GEONetworkEventFileManager _closeFiles] : 460 -> 476
~ -[GEOAnalyticsDataFile .cxx_destruct] : 40 -> 24
~ ___40-[GEONetworkEventFileManager commoninit]_block_invoke : 36 -> 12
~ -[GEOPDIcon .cxx_destruct] : 100 -> 96
~ -[GEOPDCategory .cxx_destruct] : 152 -> 124
~ -[GEOPDPhoto .cxx_destruct] : 148 -> 124
~ __ZNK5zilch18TrafficDynamicTile21feedUpdateTimeSecondsEv : 36 -> 24
~ __ZNSt3__16vectorIN8addr_obj5venue8TemplateENS_9allocatorIS3_EEE16__destroy_vectorclB8ne200100Ev : 96 -> 108
~ __ZN6google8protobuf2io19EpsCopyOutputStream23WriteStringMaybeAliasedEjRKNSt3__112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEEPh : 764 -> 776
~ __ZN4maps10path_codec4geo319RiceEncodedIntegersD1Ev : 28 -> 16
~ __ZN6google8protobuf8internal16InternalMetadata6DeleteINS0_15UnknownFieldSetEEEvv : 144 -> 168
~ -[GEOProbeCrumbs recentLocationHistory] : 1180 -> 1168
~ __ZN4maps10path_codec4geo319RiceEncodedIntegersC1EPN6google8protobuf5ArenaE : 16 -> 36
~ __ZN6google8protobuf8internal14ArenaStringPtr12ClearToEmptyEv : 84 -> 64
~ __ZN4maps10path_codec4geo319RiceEncodedIntegersC2EPN6google8protobuf5ArenaE : 176 -> 156
~ ___39-[GEOProbeCrumbs recentLocationHistory]_block_invoke_2 : 60 -> 68
~ __ZN6google8protobuf8internal14ArenaStringPtr7MutableENS2_12EmptyDefaultEPNS0_5ArenaE : 220 -> 232
~ __ZN4maps10path_codec9BitStream5writeEhj : 228 -> 216
~ __ZN6google8protobuf13RepeatedFieldIjE7ReserveEi : 356 -> 368
~ __ZN4maps10path_codec9BitStream8finalizeEv : 188 -> 176
~ __ZNK6google8protobuf11MessageLite21AppendPartialToStringEPNSt3__112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEE : 552 -> 564
~ __ZNK4maps10path_codec4geo319RiceEncodedIntegers18_InternalSerializeEPhPN6google8protobuf2io19EpsCopyOutputStreamE : 700 -> 712
~ ___39-[GEOProbeCrumbs recentLocationHistory]_block_invoke.10 : 88 -> 64
~ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE18__shrink_or_extendB8ne200100Em : 420 -> 412
~ ___39-[GEOProbeCrumbs recentLocationHistory]_block_invoke_2.11 : 232 -> 252
~ -[GEOETATrafficUpdateRequest init] : 124 -> 104
~ +[GEOETARequester sharedRequester] : 104 -> 112
~ -[GEOETATrafficUpdateRequest hasXpcUuid] : 68 -> 80
~ -[GEOETATrafficUpdateRequest tripOrigin] : 76 -> 64
~ -[GEOLocation hasTransportType] : 36 -> 48
~ -[GEOETATrafficUpdateRequest _readUserIncidentReports] : 232 -> 220
~ -[GEOLocation hasRoadClass] : 48 -> 28
~ -[GEOETARequestUpdateable request] : 20 -> 28
~ __ZN8addr_obj10Formatting26overrideLegacyShortAddressERKNS_12LocalizationERKNSt3__112basic_stringIcNS4_11char_traitsIcEENS4_9allocatorIcEEEE : 68 -> 60
~ -[GEOComposedGuidanceEvent hasHaptics] : 84 -> 76
~ __ZNK8addr_obj15V1AddressObject15getShortAddressEv : 612 -> 620
~ -[GEOComposedGuidanceEvent stackRanking] : 140 -> 132
~ -[GEOSignGuidance stackRanking] : 16 -> 36
~ -[GEOComposedStringOptions stringAttributes] : 36 -> 8
~ __GEOFormattedStringIsDirty : 540 -> 548
~ -[GEOComposedRoute cameraInfos] : 36 -> 32
~ -[GEOComposedRouteMutableData updateableCameraInfos] : 32 -> 24
~ -[GEOComposedStringReplacementResult tokenReplacementResults] : 28 -> 8
~ -[GEOSignGuidance shieldName] : 76 -> 84
~ -[GEOComposedGuidanceEvent isSpecial] : 76 -> 68
~ -[GEOGuidanceEvent eventType] : 128 -> 104
~ -[GEOComposedGuidanceEvent hasSignGuidance] : 12 -> 36
~ -[GEOSignGuidance signDetails] : 84 -> 92
~ -[GEOComposedGuidanceEvent shieldInfo] : 100 -> 92
~ -[GEOSignGuidance _readSignTitles] : 228 -> 204
~ -[GEOComposedGuidanceEvent stepIndex] : 36 -> 28
~ -[GEOGuidanceEvent hasArGuidance] : 64 -> 84
~ -[_GEOPlaceDataItem _hasTransit] : 120 -> 128
~ -[GEOAddressObject shortAddress] : 468 -> 460
~ -[GEOComposedWaypoint(GEOWaypointExtras) waypointCategory] : 364 -> 352
~ -[GEOComposedGuidanceEvent secondarySignStrings] : 24 -> 36
~ -[GEOComposedStringOptions shouldUpdateFormatStrings] : 28 -> 8
~ -[GEOGuidanceEvent spokenGuidance] : 68 -> 64
~ -[GEOComposedRouteStep timeCheckpoints] : 16 -> 28
~ -[GEOStep _readTimeCheckpoints] : 216 -> 204
~ -[GEOComposedRouteStep routeCoordinateRange] : 124 -> 104
~ -[GEOStep expectedTime] : 28 -> 40
~ -[GEOLocation(GEOProtoExtras) hasAccurateCourse] : 128 -> 136
~ -[GEONavigationMatchInfo roadWidthOnRoute] : 32 -> 12
~ -[GEORouteAttributes dealloc] : 136 -> 124
~ _GEONameInfoReadSpecified : 2368 -> 2340
~ -[GEOFormattedString _readFormatStyles] : 208 -> 228
~ __ZNSt3__15dequeI23_GEOProbeCrumbsLocationNS_9allocatorIS1_EEE26__maybe_remove_front_spareB8ne200100Eb : 96 -> 88
~ __ZNSt3__114__split_bufferIPN3geo16TransitEdgePieceERNS_9allocatorIS3_EEE13emplace_frontIJRS3_EEEvDpOT_ : 292 -> 288
~ -[GEOComposedGuidanceEvent exclusiveSetIdentifier] : 208 -> 200
~ -[GEOSpokenGuidance hasExclusiveSetIdentifier] : 48 -> 24
~ -[GEOComposedGuidanceEvent hasSpokenGuidance] : 8 -> 32
~ -[GEOComposedRoute destination] : 100 -> 116
~ -[GEOComposedRouteVisualInfo routeCoordinateRange] : 32 -> 12
~ __ZNK8addr_obj15V2AddressObject15getShortAddressEv : 348 -> 328
~ -[GEOMatchedPathSegment .cxx_destruct] : 84 -> 108
~ -[GEOComposedRoute composedGuidanceEvents] : 16 -> 12
~ -[GEOMapItemRoutineAttributes loiType] : 124 -> 116
~ -[GEOMapItemStorage(GEOMapItem) contactIsMe] : 204 -> 228
~ -[GEOMultiSectionFeature formOfWay] : 52 -> 36
~ -[GEONavigationMatchInfo distanceFromRoad] : 12 -> 16
~ __ZL25GEOGetGEOComposedRouteLogv : 112 -> 100
~ -[GEOResourceManifestManager allResourceNames] : 132 -> 112
~ -[GEOCompanionRouteStatus init] : 116 -> 104
~ -[GEOCompanionRouteStatus(CompanionExtras) isNavigating] : 96 -> 76
~ -[GEOCompanionRouteStatus routeID] : 68 -> 88
~ -[GEOCompanionDriveStep _readManeuverNames] : 224 -> 204
~ sub_1867f630c -> sub_1867ce190 : 96 -> 108
~ -[GEODirectionsRequest(GEOProtoExtras) initDefaultFeedbackInfo] : 232 -> 216
~ -[GEODirectionsRequest init] : 116 -> 108
~ ___40-[GEOUserSession _mapsUserSessionEntity]_block_invoke : 136 -> 132
~ -[GEOUserSessionEntity sessionRelativeTimestamp] : 24 -> 16
~ -[GEORouteAttributes init] : 120 -> 108
~ -[GEODirectionsRequest _readWaypointTypeds] : 204 -> 224
~ _GEOClientCapabilitiesReadAllFrom : 412 -> 424
~ -[GEODirectionsRequest hasSessionID] : 48 -> 28
~ sub_1867fa47c -> sub_1867d22e8 : 180 -> 172
~ sub_1867fbee4 -> sub_1867d3d48 : 92 -> 108
~ _GEOCompanionRouteContextReadAllFrom : 1220 -> 1224
~ -[GEOCompanionRouteContext(CompanionExtras) simpleDescription] : 280 -> 276
~ -[GEOCompanionRouteContext origin] : 44 -> 68
~ -[GEOComposedWaypoint .cxx_destruct] : 232 -> 220
~ -[GEOScreenDimension .cxx_destruct] : 44 -> 36
~ sub_1867ff37c -> sub_1867d71f4 : 96 -> 104
~ -[GEOLocation _readCoarseMetadata] : 212 -> 216
~ -[GEOCompanionStep distanceMeters] : 20 -> 36
~ sub_1867ff9ac -> sub_1867d7840 : 104 -> 108
~ _GEOPolylineCoordinateAsFullString : 80 -> 88
~ -[GEOLocation description] : 172 -> 176
~ -[GEORouteMatch locationCoordinate] : 24 -> 20
~ -[GEOFormattedString(GEOServicesExtras) formatTokens] : 12 -> 16
~ -[GEORouteMatch transitID] : 24 -> 20
~ -[GEOComposedRouteStep isStartOrResumeStep] : 112 -> 104
~ -[GEOComposedStringReplacementResult attributedSeparatorStrings] : 28 -> 8
~ ___27-[GEOComposedRoute traffic]_block_invoke : 84 -> 80
~ -[GEOComposedRouteStep maneuverRoadName] : 676 -> 680
~ -[GEOComposedRoute waypoints] : 460 -> 468
~ -[GEOStep _readRoadDescriptions] : 216 -> 228
~ -[GEOComposedStringReplacementResult attributedComponentStrings] : 20 -> 28
~ -[GEOComposedRouteStep geoStep] : 20 -> 12
~ -[GEOComposedWaypoint(GEOWaypointExtras) isServerProvidedWaypoint] : 12 -> 24
~ -[GEOFormattedString _readAlternativeString] : 228 -> 204
~ -[GEOStep maneuverType] : 132 -> 120
~ -[GEOJunction .cxx_destruct] : 40 -> 12
~ -[GEOComposedRoute traffic] : 280 -> 300
~ -[GEOComposedRouteLeg origin] : 32 -> 28
~ sub_186805264 -> sub_1867dd0d8 : 132 -> 148
~ _GEODirectionsRequestFeedbackReadSpecified : 1828 -> 1812
~ -[GEOCompanionWaypoint init] : 100 -> 116
~ -[GEOCompanionRouteDetails _readWaypoints] : 204 -> 232
~ -[GEOWaypointPlace _readRoadAccessPoints] : 228 -> 200
~ -[GEOCompanionRouteStatus displayedStepID] : 32 -> 20
~ -[GEOCompanionRouteStatus(CompanionExtras) effectiveStepID] : 104 -> 116
~ -[GEOCompanionStep stepID] : 32 -> 20
~ -[GEOCompanionRouteStatus(CompanionExtras) selectedRideIndices] : 212 -> 224
~ -[GEOCompanionRouteDetails dealloc] : 148 -> 132
~ -[GEOCompanionWaypoint .cxx_destruct] : 176 -> 188
~ -[GEOWaypointPlace .cxx_destruct] : 152 -> 156
~ -[GEOCompanionStep .cxx_destruct] : 316 -> 304
~ -[GEOCompanionDriveStep clearJunctionElements] : 148 -> 168
~ -[GEOTripInfo .cxx_destruct] : 20 -> 40
~ _GEODirectionsResponseReadAllFrom : 436 -> 416
~ -[GEOCompanionDriveStep .cxx_destruct] : 204 -> 228
~ -[GEODirectionsRequestFeedback .cxx_destruct] : 152 -> 140
~ _GEODirectionsResponseReadSpecified : 9212 -> 9216
~ sub_186809048 -> sub_1867e0ee4 : 172 -> 180
~ -[GEOGuidanceEvent .cxx_destruct] : 248 -> 244
~ -[GEODirectionsResponse clearProblemDetails] : 160 -> 152
~ -[GEODirectionsRequest .cxx_destruct] : 732 -> 752
~ -[GEORouteAttributes .cxx_destruct] : 204 -> 228
~ -[GEOCommonOptions .cxx_destruct] : 32 -> 48
~ -[GEOAdditionalEnabledMarkets .cxx_destruct] : 132 -> 144
~ -[GEODirectionsResponse init] : 124 -> 96
~ -[GEOMuninBucket .cxx_destruct] : 84 -> 92
~ -[GEOLogMsgStatePlaceCard .cxx_destruct] : 204 -> 192
~ _MapsFeaturesConfig_EnableMoreReportTypes_Metadata_block_invoke_18 : 28 -> 40
~ __GEOComposedWaypointCallReadAllRecursiveWithoutSynchronized : 124 -> 144
~ __GEOWaypointTypedCallReadAllRecursiveWithoutSynchronized : 140 -> 132
~ -[GEOPlaceActionDetails init] : 120 -> 108
~ -[GEOLogMsgStatePlaceCard _readCommingledRichProviderIds] : 224 -> 204
~ -[GEOPlaceActionDetails .cxx_destruct] : 192 -> 212
~ -[GEOLogMsgStatePlaceCard init] : 116 -> 96
~ -[GEOAlmanac nextTransit] : 12 -> 20
~ -[GEOProtobufSessionTask description] : 136 -> 124
~ -[GEODataURLSessionTask(Convenience) originalRequestURL] : 88 -> 80
~ __ZL18shouldCountRequest18GEODataRequestKind31GEOMapServiceTraits_RequestMode : 192 -> 172
~ -[GEODataURLSessionTask description] : 196 -> 184
~ __GEORequestResponseLogQueue : 104 -> 92
~ -[GEOProtobufSessionTask clientMetrics] : 92 -> 104
~ ____GEORequestResponseLogResponse_block_invoke : 948 -> 928
~ -[GEODataURLSessionTask protocolBufferHasPreamble] : 8 -> 16
~ -[GEOProtobufSessionTask requestTypeCode] : 12 -> 36
~ _GEOPDDatasetABStatusIsValid : 636 -> 612
~ -[GEOProtobufSessionTask(Result) response] : 32 -> 24
~ _GEOPDDatasetABStatusReadAllFrom : 844 -> 828
~ -[GEOPDForwardInfoFilter .cxx_destruct] : 24 -> 28
~ -[GEOPDRelatedPlaceFilter .cxx_destruct] : 48 -> 28
~ -[GEOPDCategorizedPhotosFilter dealloc] : 204 -> 196
~ -[GEOPDFactoidFilter .cxx_destruct] : 36 -> 32
~ -[GEOPDQuickLinkFilter .cxx_destruct] : 44 -> 48
~ -[GEOPDResultSnippetFilter .cxx_destruct] : 36 -> 32
~ -[GEOPDTipFilter .cxx_destruct] : 20 -> 24
~ -[GEOPDTransitScheduleFilter .cxx_destruct] : 132 -> 136
~ -[GEOPDDeparturePredicate .cxx_destruct] : 44 -> 48
~ -[GEOPDAnnotatedItemListFilter .cxx_destruct] : 20 -> 28
~ -[GEOPDAnnotatedItemListFilter dealloc] : 124 -> 136
~ -[GEOPDOfflineAreaFilter .cxx_destruct] : 44 -> 24
~ -[GEOPDAmenitiesFilter .cxx_destruct] : 28 -> 40
~ -[GEOPDPlaceResponse .cxx_destruct] : 316 -> 312
~ -[GEOPlaceReplyMessage isValid] : 96 -> 108
~ -[GEOPDCaptionedPhotoFilter dealloc] : 212 -> 216
~ -[GEOPDResultSnippetFilter dealloc] : 84 -> 104
~ -[GEOPDPlaceResponse _readMapsResults] : 224 -> 208
~ -[GEOPDReviewFilter .cxx_destruct] : 28 -> 32
~ -[GEOPDReviewFilter dealloc] : 128 -> 148
~ -[GEOPDCategorizedPhotosFilter .cxx_destruct] : 108 -> 132
~ -[GEOPDPlaceRequestParameters brandLookupParameters] : 92 -> 80
~ -[GEOPDComponentValue messageLink] : 60 -> 56
~ -[GEOPDMessageLink timezone] : 84 -> 88
~ -[GEOPDBrowseCategory .cxx_destruct] : 208 -> 216
~ -[GEONetworkServiceRequesterOperation .cxx_destruct] : 212 -> 192
~ _protobufDataWithHeader : 316 -> 336
~ _GEOStyleAttributeIsValid : 808 -> 800
~ -[GEOPDDatasetABStatus datasetId] : 36 -> 24
~ ____GEORequestResponseLogRequest_block_invoke : 1000 -> 972
~ -[GEORequestCounterTicketBase description] : 88 -> 84
~ __GEORequestResponseLogResponse : 340 -> 328
~ -[GEONetworkServiceRequesterOperation _cleanup] : 92 -> 84
~ _RegionContainsPoint : 296 -> 288
~ _GEOTileKeyAssertIsStandard : 144 -> 128
~ -[GEOApplicationAuditToken description] : 200 -> 212
~ -[GEOTileServerRemoteProxy close] : 28 -> 32
~ __ZN3geo25DbReaderTarFileDescriptorC2EiPU19objcproto9OS_os_log8NSObject : 3748 -> 3764
~ __ZNSt3__121__murmur2_or_cityhashImLm64EE18__hash_len_0_to_16B8ne200100EPKcm : 260 -> 276
~ __ZNK3geo25DbReaderTarFileDescriptor18createMemoryBufferERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEERKN6gloria10BufferTypeEPPKNSA_6BufferENS1_10shared_ptrINSA_11ShardHeaderEEE : 632 -> 616
~ __ZNKSt3__18equal_toINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEEclB8ne200100ERKS6_S9_ : 148 -> 132
~ -[GEOGloriaDB metadata] : 24 -> 40
~ __ZNK6gloria6Buffer11CheckBoundsERKxRKm : 20 -> 12
~ _GeoServicesConfig_PDPlaceCacheQuiescentTimeBeforeUpdate_Metadata_block_invoke_218 : 40 -> 16
~ -[GEOServiceVersion versionDomains] : 64 -> 56
~ -[GEOPDMapsResult init] : 112 -> 124
~ -[GEOPDBrandLookupParameters .cxx_destruct] : 108 -> 96
~ -[GEOPDMapsResult .cxx_destruct] : 208 -> 212
~ -[GEOActiveTileGroup versionManifest] : 68 -> 76
~ _GEOPDBrandLookupParametersReadAllFrom : 600 -> 620
~ _GEOPDMapsResultReadSpecified : 2268 -> 2288
~ -[GEOPDPlace(PlaceDataExtras) statusCodeIsValid] : 76 -> 88
~ __attributedGeoMapItemsForPlaceDatas : 412 -> 420
~ -[GEOPDPlaceResponse(GEOMapService) _disambiguationLabels] : 340 -> 332
~ -[GEOPDMapsResult place] : 76 -> 88
~ -[GEOPDPlaceResponse hasGlobalResult] : 68 -> 56
~ -[_GEOPlaceDataItem _hasTelephone] : 92 -> 80
~ ___43-[GEOPDPlace(PlaceDataExtras) phoneNumbers]_block_invoke : 384 -> 396
~ -[GEOPDEntity _readAltTelephones] : 224 -> 232
~ -[GEOMessageLink navBackgroundColorString] : 100 -> 120
~ -[GEOPDMessageLink navBackgroundColor] : 88 -> 100
~ __ZNK8addr_obj4geo328StructuredAddress_SubPremise13IsInitializedEv : 40 -> 20
~ _GEOMapRectForGEOTileKey : 160 -> 132
~ __ZNK3geo25DbReaderTarFileDescriptor9listFilesERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEERNS1_6vectorIS7_NS5_IS7_EEEE : 368 -> 376
~ __GEOPDPlaceIsDirty : 208 -> 212
~ -[GEOActiveTileGroup _readVersionManifest] : 216 -> 204
~ -[GEOVersionManifest serviceVersions] : 40 -> 16
~ _GEOPDMapsResultReadAllFrom : 412 -> 424
~ -[GEOPDPlaceResponse dotPlacesCount] : 76 -> 64
~ -[_GEOPlaceDataItem _iso3166Value] : 164 -> 156
~ __ZNK3geo9TarBuffer4ReadERKxRKmRN6gloria5SliceE : 148 -> 164
~ _GEOGetCoarseLocationLog : 112 -> 92
~ _GEOMapRectUnion : 164 -> 152
~ -[GEOStructuredAddress country] : 28 -> 20
~ -[GEOPDComponentFilter toolTipFilter] : 228 -> 212
~ -[GEOPDTooltipFilter hash] : 60 -> 56
~ -[GEOPDSearchBrowseCategorySuggestionParameters init] : 104 -> 100
~ -[GEOMapServiceTraits hasNavigationTransportType] : 24 -> 36
~ _GEOGetUserPreferredTransportType : 40 -> 60
~ -[GEOMapServiceTraits _readAutomobileOptions] : 212 -> 216
~ -[GEOAutomobileOptions _readVehicleSpecifications] : 204 -> 200
~ -[GEOMapServiceTraits _readTransitOptions] : 216 -> 228
~ -[GEOTransitOptions _readFareOptions] : 200 -> 224
~ -[GEOFareOptions dictionaryRepresentation] : 8 -> 36
~ -[GEOMapServiceTraits _readWalkingOptions] : 208 -> 220
~ -[GEOWalkingUserPreferences dictionaryRepresentation] : 8 -> 28
~ -[GEOMapServiceTraits _readCyclingOptions] : 228 -> 232
~ -[GEOCyclingVehicleSpecifications dictionaryRepresentation] : 8 -> 36
~ -[GEOMapServiceTraits _readUserActionMetadata] : 228 -> 232
~ sub_186817de4 -> sub_1867efca8 : 64 -> 76
~ _GEOPDViewportInfoReadAllFrom : 1188 -> 1196
~ _GEOPDSearchOriginationInfoReadSpecified : 2448 -> 2428
~ __GEOPDSearchBrowseCategorySuggestionParametersCallReadAllRecursiveWithoutSynchronized : 136 -> 132
~ -[GEOLocation hash] : 1944 -> 1916
~ -[GEOPDSearchBrowseCategorySuggestionParameters hash] : 592 -> 604
~ -[GEOPDViewportInfo hash] : 160 -> 144
~ -[GEOMapRegion hash] : 784 -> 776
~ -[GEOPDSearchOriginationInfo hash] : 204 -> 188
~ _GEOPDTooltipFilterReadAllFrom : 852 -> 836
~ -[GEOPlaceDataRequestConfig .cxx_destruct] : 88 -> 100
~ -[GEOPDSearchCapabilitiesParameters .cxx_destruct] : 84 -> 96
~ -[GEOPDViewportInfo .cxx_destruct] : 84 -> 100
~ -[GEOSearchCategory styleAttributes] : 160 -> 152
~ _GeoCodecsFeatureStyleAttributesCompare : 272 -> 260
~ __ZN3geo5codec29featureStyleAttributesCompareERKNSt3__110shared_ptrIK22FeatureStyleAttributesEES7_ : 228 -> 216
~ -[GEOSearchCategory shortDisplayString] : 128 -> 120
~ -[GEOPDBrowseCategory shortDisplayString] : 84 -> 96
~ _GEOPDSearchBrowseCategorySuggestionResultIsValid : 496 -> 484
~ _GEOPDBrowseCategoryIsValid : 1816 -> 1796
~ sub_186827b74 -> sub_1867ff9d8 : 284 -> 272
~ -[GEOPlaceDataRequestConfig usesBackgroundURL] : 20 -> 32
~ -[GEOPDPlaceGlobalResult _readAutocompleteResult] : 180 -> 208
~ -[GEOPDPlaceRequest(PlaceDataExtras) isBrandLookupRequest] : 136 -> 144
~ -[GEOPDTooltipFilter .cxx_destruct] : 28 -> 24
~ -[GEOPDSearchBrowseCategorySuggestionParameters .cxx_destruct] : 184 -> 204
~ -[GEOPDSearchOriginationInfo .cxx_destruct] : 116 -> 128
~ _GEOPDSearchBrowseCategorySuggestionResultReadAllFrom : 676 -> 664
~ _GEOPDBrowseCategoryReadSpecified : 3632 -> 3644
~ -[GEOPDSearchBrowseCategorySuggestionResult categorys] : 60 -> 56
~ -[GEOProtobufSessionTask .cxx_destruct] : 156 -> 148
~ -[GEODataRequestThrottlerToken .cxx_destruct] : 40 -> 20
~ -[GEOPDSearchBrowseCategorySuggestionResult .cxx_destruct] : 112 -> 108
~ -[GEOSearchCategory subcategories] : 20 -> 12
~ __GEOPDBrowseCategoryCallReadAllRecursiveWithoutSynchronized : 300 -> 276
~ -[GEOSearchCategory _browseCategory] : 16 -> 28
~ sub_18682adbc -> sub_186802c28 : 60 -> 80
~ _GEOETAStepIsValid : 1568 -> 1572
~ _GEONavigabilityInfoIsValid : 816 -> 792
~ sub_18682c110 -> sub_186803f7c : 80 -> 100
~ _GEONameInfoIsValid : 1120 -> 1116
~ _GEOFormattedStringIsValid : 708 -> 716
~ _GEOGuidanceImportanceModeIsValid : 904 -> 896
~ _GEOJunctionElementReadAllFrom : 1148 -> 1124
~ _GEOVisualLaneGuidanceIsValid : 780 -> 772
~ _GEOGenericCombinationsIsValid : 488 -> 496
~ _GEOAttributeIsValid : 796 -> 804
~ _GEORoutePlanningInfoIsValid : 792 -> 784
~ _GEOAdvisoriesInfoIsValid : 584 -> 608
~ _GEOPBTransitArtworkIsValid : 1224 -> 1232
~ _GEOArrivalRegionIsValid : 1072 -> 1080
~ _GEOTrafficSignalIsValid : 924 -> 916
~ _GEORestrictionZoneInfoIsValid : 1088 -> 1064
~ -[GEOETATrafficUpdateResponse init] : 112 -> 100
~ _GEOETATrafficUpdateResponseReadSpecified : 3684 -> 3692
~ sub_1868316a8 -> sub_186809510 : 64 -> 68
~ __GEOETATrafficUpdateResponseIsDirty : 884 -> 872
~ -[GEOETATrafficUpdateRequest _readXpcUuid] : 228 -> 208
~ -[GEOETAReplyUpdateable .cxx_destruct] : 104 -> 96
~ -[GEORecentLocationHistory init] : 100 -> 108
~ -[GEOETATrafficUpdateResponse waypointRoute] : 72 -> 92
~ -[GEOETARoute originWaypointInfo] : 92 -> 64
~ _GEOWaypointInfoReadAllFrom : 416 -> 412
~ -[GEOETARoute _readDestinationWaypointInfo] : 208 -> 212
~ -[GEOWaypointInfo evChargingInfo] : 76 -> 72
~ -[GEOETATrafficUpdateWaypointRoute traversalTimes] : 64 -> 76
~ -[GEOETATrafficUpdateRequest _readRouteAttributes] : 212 -> 204
~ -[GEOComposedRoute styleAttributes] : 16 -> 12
~ -[GEOETATrafficUpdateWaypointRoute newWaypointRoutes] : 68 -> 80
~ -[GEOWaypointRoute init] : 112 -> 104
~ -[GEOComposedRoute init] : 236 -> 244
~ -[GEORoutePlanningInfo init] : 96 -> 104
~ -[GEORouteInitializerData routeAttributes] : 20 -> 12
~ -[GEOWaypointRoute identifier] : 44 -> 36
~ -[GEOCommonResponseAttributes elevationModel] : 48 -> 44
~ -[GEONameInfo _readName] : 212 -> 224
~ -[GEORoutePlanningInfo _readTrafficDescriptionText] : 200 -> 224
~ _GEOPBTransitArtworkReadSpecified : 2996 -> 3004
~ -[GEORoutePlanningInfo _readLabelAction] : 224 -> 216
~ _GEOLabelActionReadAllFrom : 1100 -> 1108
~ -[GEORoutePlanningInfo _readRoutePlanningDescription] : 224 -> 216
~ -[GEORouteInformation duration] : 212 -> 204
~ sub_186836348 -> sub_18680e1a4 : 72 -> 80
~ -[GEORouteInformation separator] : 204 -> 212
~ -[GEOWaypointRouteFeatures avoidsTraffic] : 20 -> 28
~ -[GEORouteInitializerData styleAttributes] : 16 -> 8
~ -[GEORoute _readPathLeg] : 220 -> 232
~ _GeoServicesConfig_RequestRoutingPathPoints_Metadata_block_invoke_269 : 16 -> 40
~ -[GEORawPathGeometry decompressedPathData] : 104 -> 100
~ __ZN4maps10path_codec4geo314RoutingPathLeg5ClearEv : 236 -> 224
~ __ZN6google8protobuf8internal16ReadSizeFallbackEPKcj : 124 -> 136
~ __ZN4maps10path_codec4geo319RiceEncodedIntegers14_InternalParseEPKcPN6google8protobuf8internal12ParseContextE : 984 -> 972
~ __ZN6google8protobuf8internal11VarintParseIyEEPKcS4_PT_ : 148 -> 128
~ __ZN6google8protobuf5Arena18CreateMaybeMessageIN4maps10path_codec4geo316SupportPointDataEJEEEPT_PS1_DpOT0_ : 236 -> 224
~ __ZN6google8protobuf8internal20RepeatedPtrFieldBase7ReserveEi : 48 -> 28
~ __ZN6google8protobuf8internal20RepeatedPtrFieldBase7DestroyINS0_16RepeatedPtrFieldIN4maps10path_codec4geo34UUIDEE11TypeHandlerEEEvv : 160 -> 152
~ __ZNSt3__16vectorI23GEOLocationCoordinate3DNS_9allocatorIS1_EEE7reserveEm : 220 -> 208
~ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorI23GEOLocationCoordinate3DEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m : 104 -> 116
~ -[GEOCoordinateArraySupportPoint init] : 84 -> 104
~ __ZNSt3__16vectorI23GEOLocationCoordinate3DNS_9allocatorIS1_EEE18__assign_with_sizeB8ne200100IPS1_S6_EEvT_T0_l : 372 -> 380
~ __ZNSt3__16vectorIyNS_9allocatorIyEEE11__vallocateB8ne200100Em : 72 -> 84
~ __ZN6google8protobuf8internal20RepeatedPtrFieldBase7DestroyINS0_16RepeatedPtrFieldIN4maps10path_codec4geo316RoutingPathPointEE11TypeHandlerEEEvv : 160 -> 132
~ -[GEORawPathGeometry .cxx_destruct] : 72 -> 76
~ -[GEORouteInitializerData directionsRequest] : 28 -> 20
~ -[GEORoute _readSteps] : 208 -> 232
~ _GEOStepReadSpecified : 9640 -> 9644
~ sub_18683b5b8 -> sub_186813420 : 200 -> 204
~ -[GEOStep _readEvStateInfo] : 204 -> 224
~ sub_18683cc0c -> sub_186814a8c : 120 -> 124
~ _GEOWaypointInfoIsValid : 1304 -> 1312
~ sub_186840a28 -> sub_1868188b4 : 212 -> 204
~ _GEOEnrouteNoticeIsValid : 1892 -> 1916
~ _GEOConditionalFormattedStringIsValid : 560 -> 536
~ _GEORouteLineStyleInfoIsValid : 1376 -> 1384
~ _GEORouteInformationIsValid : 560 -> 552
~ _GEOLabelActionIsValid : 804 -> 800
~ _GEOMapRegionIsValid : 1116 -> 1120
~ _GEOCommonResponseAttributesIsValid : 620 -> 628
~ _GEOETATrafficUpdateResponseReadAllFrom : 424 -> 412
~ _GEOUUIDReadAllFrom : 1100 -> 1104
~ _GEOCommonResponseAttributesReadAllFrom : 836 -> 832
~ -[GEOETATrafficUpdateRequest .cxx_destruct] : 668 -> 648
~ -[GEOETATrafficUpdateResponse _readRoutes] : 212 -> 224
~ ___39-[GEOProbeCrumbs recentLocationHistory]_block_invoke : 68 -> 88
~ -[GEOETATrafficUpdateResponse _readWaypointRoute] : 232 -> 212
~ -[GEOComposedRouteLeg stepCount] : 24 -> 32
~ -[GEOETARoute _readOriginWaypointInfo] : 212 -> 216
~ -[GEOWaypointInfo _readEvChargingInfo] : 204 -> 200
~ -[GEOETATrafficUpdateWaypointRoute _readTraversalTimes] : 220 -> 200
~ -[GEOETATrafficUpdateRequest routeAttributes] : 88 -> 64
~ -[GEORouteInitializerData etaTrafficUpdateResponse] : 28 -> 8
~ -[GEOETATrafficUpdateWaypointRoute _readNewWaypointRoutes] : 208 -> 220
~ sub_1868491d8 -> sub_186821024 : 80 -> 88
~ -[GEORouteInitializerData waypoints] : 36 -> 28
~ -[GEORoutePlanningInfo _readTrafficDescriptionArtwork] : 220 -> 204
~ _GEOPBTransitArtworkReadAllFrom : 428 -> 436
~ -[GEOFormatArgument init] : 120 -> 112
~ _GEOFormatArgumentReadAllFrom : 416 -> 424
~ -[GEORouteInformation distance] : 232 -> 208
~ -[GEOWaypointRouteFeatures avoidsTolls] : 40 -> 16
~ -[GEORouteInitializerData address] : 36 -> 16
~ _GEOGetGEORouteBuilderLog : 96 -> 108
~ _GEORouteReadAllFrom : 420 -> 412
~ sub_18684e76c -> sub_186826570 : 388 -> 364
~ -[GEORoute _readPathMapMatcherInstructions] : 228 -> 220
~ -[_GEOCoordinatePath .cxx_construct] : 52 -> 28
~ __ZN4maps10path_codec4geo314RoutingPathLeg14_InternalParseEPKcPN6google8protobuf8internal12ParseContextE : 992 -> 1012
~ __ZN6google8protobuf8internal24InlineGreedyStringParserEPNSt3__112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEEPKcPNS1_12ParseContextE : 132 -> 144
~ __ZN4maps10path_codec4geo316SupportPointDataC2EPN6google8protobuf5ArenaE : 504 -> 524
~ __ZN6google8protobuf8internal21ReadPackedVarintArrayIZNS1_12VarintParserIiLb1EEEPKcPvS5_PNS1_12ParseContextEEUlyE_EES5_S5_S5_T_ : 184 -> 196
~ __ZN4maps10path_codec4geo310AnchorDataC2EPN6google8protobuf5ArenaE : 200 -> 188
~ __ZN6google8protobuf8internal20RepeatedPtrFieldBase14InternalExtendEi : 296 -> 308
~ -[GEOStep evStateInfo] : 76 -> 68
~ _GEODrivingWalkingInstructionIsValid : 580 -> 604
~ _GEOFormattedStringMetaDataIsValid : 816 -> 792
~ _GEOLaneArrowheadIsValid : 792 -> 816
~ _GEOConditionIsValid : 876 -> 880
~ -[GEOETAStep stepID] : 24 -> 36
~ -[GEOETARequestUpdateable .cxx_destruct] : 92 -> 112
~ __ZN6google8protobuf11MessageLite15ParseFromStringERKNSt3__112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEE : 152 -> 164
~ __ZN4maps10path_codec4geo315CommonPointData14_InternalParseEPKcPN6google8protobuf8internal12ParseContextE : 568 -> 556
~ __ZN6google8protobuf8internal21ReadPackedVarintArrayIZNS1_12VarintParserIjLb0EEEPKcPvS5_PNS1_12ParseContextEEUlyE_EES5_S5_S5_T_ : 176 -> 188
~ __ZN4maps10path_codec4geo316SupportPointData14_InternalParseEPKcPN6google8protobuf8internal12ParseContextE : 3012 -> 3000
~ __ZN6google8protobuf13RepeatedFieldIyE7ReserveEi : 360 -> 372
~ __ZN4maps10path_codec4geo314CompressedPathD1Ev : 32 -> 4
~ -[GEORawPathGeometry pathMatcherInstructions] : 36 -> 24
~ -[GEOComposedRouteCoordinateArray pathsCount] : 8 -> 16
~ -[GEOStep init] : 112 -> 104
~ _GEOArrivalPointIsValid : 692 -> 700
~ __ZN4maps10path_codec4geo316RoutingPathPointD2Ev : 220 -> 208
~ _GEONameInfoListIsValid : 496 -> 492
~ _GEOPBTransitIconIsValid : 892 -> 876
~ -[GEORoute _readDestinationListInstruction] : 204 -> 224
~ -[GEONameInfoList nameInfos] : 36 -> 40
~ _GEOLaneArrowheadReadAllFrom : 1128 -> 1136
~ -[GEORoute enrouteNoticesCount] : 64 -> 88
~ _GEOEnrouteNoticeReadAllFrom : 432 -> 416
~ _GEOPDLocalTimeRangeWriteTo : 116 -> 108
~ -[GEOStorageRouteRequestStorage init] : 116 -> 104
~ -[GEOPDPlacecardLayoutData .cxx_destruct] : 148 -> 128
~ -[GEOStorageRouteRequestStorage _readWaypoints] : 216 -> 204
~ -[GEOWaypointID _readFormattedAddressLineHints] : 224 -> 204
~ -[GEOPDBusinessHours _readWeeklyHours] : 180 -> 188
~ -[GEOPDQuickLink _readQuickLinkItems] : 192 -> 204
~ -[GEOPDBusinessAssets _readCoverPhotos] : 200 -> 192
~ -[GEOPDActionData _readActionLinks] : 192 -> 188
~ -[GEOPDScorecardLayout _readRatingCategorys] : 188 -> 192
~ -[GEOPDGroupData _readButtonItems] : 224 -> 200
~ -[GEOPDModuleLayoutEntry _readApplicationIds] : 228 -> 208
~ -[GEOPDStorefrontView .cxx_destruct] : 144 -> 164
~ -[GEOComposedRouteSegment segmentIndex] : 16 -> 20
~ -[GEOComposedRoute serverRouteID] : 12 -> 20
~ -[GEOStep _readManeuverNames] : 208 -> 232
~ _GEOLaneInfoReadAllFrom : 1464 -> 1472
~ -[GEOComposedWaypoint init] : 116 -> 104
~ -[GEOPDForwardInfo _readPreviousIds] : 208 -> 200
~ -[GEOPDLink init] : 108 -> 104
~ -[GEOPDRatingCategory _readLocalizedNames] : 204 -> 184
~ -[GEOPDBasemapRegionMetadata .cxx_destruct] : 100 -> 112
~ -[GEOStorageRouteRequestStorage .cxx_destruct] : 256 -> 244
~ -[GEOPDModuleConfiguration .cxx_destruct] : 92 -> 84
~ -[GEOPDButtonItem .cxx_destruct] : 140 -> 148
~ -[GEOPDForwardInfo .cxx_destruct] : 128 -> 152
~ -[GEOPDActionData .cxx_destruct] : 228 -> 204
~ -[GEOURLLocationQueryItem hasMapItemIdentifier] : 28 -> 32
~ -[GEOMapURLBuilder buildForWeb] : 88 -> 116
~ -[GEOURLLocationQueryItem init] : 80 -> 84
~ __geo_URLForDictionary : 1428 -> 1448
~ -[GEOPDActionLink init] : 112 -> 120
~ -[GEOPDPlacecardLayoutData _readModuleConfigurations] : 208 -> 188
~ -[GEOURLRouteHandle init] : 120 -> 108
~ -[GEOSearchCategoryStorage init] : 124 -> 116
~ -[GEOPDInlineRapEnablement .cxx_destruct] : 32 -> 40
~ -[GEOMapItemInitialRequestData .cxx_destruct] : 32 -> 28
~ -[GEOFormatStyle .cxx_destruct] : 132 -> 136
~ -[GEOPDUnifiedActionModuleConfiguration .cxx_destruct] : 112 -> 104
~ -[GEOPDGroupData .cxx_destruct] : 168 -> 144
~ -[GEOPDModule .cxx_destruct] : 144 -> 136
~ -[GEOPDPhotoContent .cxx_destruct] : 104 -> 112
~ -[GEOPDQuickLinkItem .cxx_destruct] : 204 -> 196
~ -[GEOPDAbout .cxx_destruct] : 108 -> 104
~ -[GEOPDPhotoConstraints .cxx_destruct] : 40 -> 32
~ -[GEOStorageRouteRequestStorage waypoints] : 68 -> 80
~ -[_GEOPlaceDataItem _resultProviderID] : 100 -> 108
~ -[GEOURLLocationQueryItem .cxx_destruct] : 92 -> 96
~ -[GEOMapURLBuilder .cxx_destruct] : 108 -> 116
~ -[GEOStep junctionElements] : 72 -> 60
~ -[GEOComposedRouteStep transportType] : 60 -> 40
~ -[GEORoute _readOriginListInstruction] : 204 -> 220
~ -[GEOGenericSubstitutes waypointCategory] : 68 -> 44
~ -[GEOFormatArgument hasValString] : 64 -> 56
~ -[GEOCondition expirationTime] : 24 -> 40
~ -[GEORoute destinationListInstruction] : 80 -> 72
~ -[GEORouteBuilderOutput segments] : 36 -> 12
~ -[GEOStep _readGuidanceEvents] : 228 -> 220
~ -[GEOSignGuidance hasJunctionInfo] : 84 -> 80
~ -[GEOComposedRouteStep maneuverType] : 24 -> 28
~ -[GEOSpokenGuidance _readAnnouncements] : 200 -> 224
~ -[GEOFormattedStringMetaData spokenPrivacyFilterType] : 68 -> 44
~ -[GEOVisualLaneGuidance titles] : 68 -> 76
~ -[GEORoute routeCameraInputInfos] : 64 -> 88
~ -[GEORouteBuilderOutput visualInfosForRouteNameLabels] : 8 -> 16
~ -[GEORoute _readUpdateLocations] : 228 -> 220
~ -[GEORestrictionZoneInfo restrictedZoneIds] : 24 -> 32
~ -[GEORoutePlanningInfo advisoriesInfo] : 72 -> 64
~ -[GEOAdvisoriesInfo _readGenericAdvisorys] : 216 -> 200
~ -[GEORouteInitializerData anchorPoints] : 12 -> 16
~ -[GEOWaypointRoute(EnrouteNoticesProvider) _geoTrafficCameras] : 400 -> 388
~ -[GEOWaypointRoute trafficSignals] : 68 -> 92
~ -[GEOEnrouteNotice type] : 128 -> 104
~ -[GEOTrafficSignal _readPosition] : 228 -> 220
~ -[GEOEnrouteNotice _readGuidances] : 228 -> 204
~ -[GEORoutePlanningInfo routeGeniusDescriptions] : 76 -> 68
~ -[GEOWaypointInfo hasPosition] : 56 -> 64
~ -[GEOComposedWaypoint waypoint] : 68 -> 88
~ -[GEOWaypointTyped _readWaypointPlace] : 200 -> 212
~ -[GEOComposedWaypoint _readLatLng] : 220 -> 208
~ -[GEOWaypointPlace _readCenter] : 204 -> 208
~ -[GEORecentLocationHistory dealloc] : 92 -> 88
~ -[GEOComposedETARoute routeOverviewDescriptionStrings] : 12 -> 16
~ -[GEOWaypointInfo _readWaypointCaption] : 224 -> 220
~ -[GEOETATrafficUpdateWaypointRoute .cxx_destruct] : 248 -> 252
~ -[GEOWaypointInfo .cxx_destruct] : 292 -> 268
~ -[GEOTrafficSignal .cxx_destruct] : 136 -> 128
~ -[GEOLaneArrowhead .cxx_destruct] : 36 -> 28
~ -[GEOGenericSubstitutes .cxx_destruct] : 96 -> 104
~ -[GEOCommonResponseAttributes .cxx_destruct] : 48 -> 44
~ -[GEOETATrafficUpdateWaypointRoute _readTrafficBannerTexts] : 220 -> 224
~ -[GEOComposedRoute dealloc] : 520 -> 516
~ -[GEOMessageLink navTintColorString] : 116 -> 104
~ -[GEOPDMessageLink _readNavTintColor] : 208 -> 204
~ +[GEOFeatureStyleAttributes(PersonalizedItem) workStyleAttributes] : 120 -> 104
~ _GEOETAResultIsValid : 1384 -> 1380
~ sub_186861258 -> sub_186838fb4 : 80 -> 52
~ _GEOETAResponseReadAllFrom : 412 -> 408
~ _GEOETAResultReadAllFrom : 436 -> 420
~ -[GEORoute arrivalParameterIndex] : 36 -> 28
~ _GEOArrivalParametersReadSpecified : 1876 -> 1884
~ -[GEORoute originWaypointInfo] : 84 -> 76
~ -[GEOFormatArgument _readStringSubstituteData] : 204 -> 228
~ -[GEOCondition type] : 44 -> 52
~ -[GEORouteLineStyleInfo laneChangeInfos] : 92 -> 68
~ -[GEORoute _readIncidentEndOffsetsInRoutes] : 224 -> 204
~ -[GEOComposedWaypoint(GEOWaypointExtras) chargingInfo] : 36 -> 24
~ -[GEOComposedWaypoint latLng] : 88 -> 68
~ -[GEOComposedRouteLeg geoDestinationWaypointInfo] : 12 -> 20
~ -[GEOWaypointPlace center] : 68 -> 72
~ -[GEORecentLocationHistory .cxx_destruct] : 228 -> 224
~ -[GEOComposedETARoute .cxx_destruct] : 140 -> 132
~ _GeoServicesConfig_NavdDebugTrafficOnRouteSection_Metadata_block_invoke_336 : 32 -> 12
~ -[GEOWaypointInfo hasEvChargingInfo] : 72 -> 80
~ -[GEOWaypointRoute .cxx_destruct] : 372 -> 364
~ -[GEOPBTransitArtwork .cxx_destruct] : 220 -> 228
~ -[GEOStep clearJunctionElements] : 144 -> 160
~ -[GEOCondition .cxx_destruct] : 96 -> 104
~ -[GEOArrivalParameters .cxx_destruct] : 132 -> 128
~ -[GEOETATrafficUpdateWaypointRoute trafficBannerTexts] : 76 -> 68
~ -[_GEOPlaceDataItem centerCoordinate] : 312 -> 304
~ +[GEOFeatureStyleAttributes(PersonalizedItem) homeStyleAttributes] : 116 -> 100
~ __GEOETAResponseIsDirty : 576 -> 604
~ _GEOETAResultReadSpecified : 2644 -> 2628
~ -[GEORoute originListInstruction] : 76 -> 68
~ -[GEOWaypointInfo name] : 92 -> 68
~ -[GEORoutePlanningInfo .cxx_destruct] : 304 -> 328
~ -[GEORouteLineStyleInfo .cxx_destruct] : 148 -> 172
~ -[GEOGenericStringData .cxx_destruct] : 100 -> 92
~ _GEOETAResponseReadSpecified : 2960 -> 2968
~ __GEOETAResultIsDirty : 136 -> 120
~ -[GEOStep junctionElementsCount] : 48 -> 68
~ -[GEOComposedRouteStep pointRange] : 52 -> 32
~ -[GEOWaypointRoute _readArrivalParameters] : 228 -> 220
~ -[GEOArrivalParameters init] : 96 -> 104
~ -[GEORoute _readDestinationWaypointInfo] : 212 -> 204
~ -[GEOFormatArgument genericCombinations] : 72 -> 64
~ -[GEOGenericCombinations substitutes] : 40 -> 16
~ -[GEOFormatArgument hasWaypointIndex] : 36 -> 28
~ -[GEOGenericStringData privacyFilterType] : 44 -> 52
~ -[GEOFormatArgument _readValString] : 224 -> 216
~ -[GEOCondition conditions] : 24 -> 40
~ _GEOMapPoint3DForCoordinate : 64 -> 52
~ _GEOComposedRouteSectionPadAndSquareBounds : 236 -> 248
~ _GEOCoordinate3DForMapPoint : 156 -> 144
~ -[GEOComposedRouteSegment endPointIndex] : 52 -> 56
~ -[GEORouteBuilderOutput pointSections] : 20 -> 28
~ -[GEOStep _readSignposts] : 224 -> 204
~ -[GEOStep(StepExtras) firstNameInfo] : 188 -> 176
~ -[GEOStep maneuverNames] : 68 -> 92
~ _GEOVisualLaneGuidanceReadSpecified : 1824 -> 1832
~ -[GEORoute _readEnrouteNotices] : 212 -> 204
~ _GEOEnrouteNoticeReadSpecified : 3436 -> 3444
~ -[GEORoute _readCellularCoverageOffsets] : 228 -> 220
~ -[GEORouteBuilderOutput guidanceEvents] : 16 -> 24
~ -[GEORoute _readRouteCameraInputInfos] : 228 -> 220
~ -[GEORouteLineStyleInfo _readLaneChangeInfos] : 224 -> 200
~ -[GEORoute _readElevationProfile] : 224 -> 216
~ -[GEORouteBuilderOutput cameraInfos] : 20 -> 28
~ -[GEOWaypointRoute restrictionZoneInfo] : 88 -> 80
~ -[GEORestrictionZoneInfo licensePlateRestrictionImpact] : 52 -> 60
~ -[GEORoutePlanningInfo _readAdvisoriesInfo] : 216 -> 208
~ _GEOAdvisoriesInfoReadSpecified : 2028 -> 2036
~ -[GEOWaypointRoute trafficCameras] : 80 -> 92
~ -[GEOWaypointRoute(EnrouteNoticesProvider) _geoTrafficSignals] : 404 -> 392
~ -[GEORoute enrouteNotices] : 76 -> 68
~ -[GEOComposedRoute _initializeManeuverDisplaySteps] : 84 -> 92
~ -[GEORoutePlanningInfo _readRouteGeniusDescriptions] : 212 -> 200
~ -[GEORouteTrafficBuilder init] : 156 -> 168
~ -[GEORoute _readTrafficColorOffsets] : 208 -> 228
~ -[GEORouteTrafficBuilder trafficColors] : 80 -> 60
~ -[GEORoute incidentEndOffsetsInRoutesCount] : 60 -> 72
~ -[GEOComposedRouteLeg geoOriginWaypointInfo] : 28 -> 8
~ -[GEOWaypointInfo _readPosition] : 228 -> 204
~ -[GEOWaypointRoute _readInitialPromptTypes] : 220 -> 208
~ -[GEOComposedETARouteLeg .cxx_destruct] : 116 -> 120
~ -[GEOComposedRoute geoWaypointRoute] : 36 -> 32
~ -[GEOETATrafficUpdateWaypointRoute routeLegs] : 88 -> 68
~ -[GEORoute trafficColorOffsets] : 72 -> 60
~ -[GEOETARoute trafficColorOffsets] : 72 -> 64
~ -[GEOComposedRouteLeg distance] : 28 -> 36
~ -[GEOETATrafficUpdateWaypointRoute _readIncidentsOnUserWaypointRoutes] : 200 -> 204
~ _GEONavigabilityInfoReadAllFrom : 1100 -> 1096
~ -[GEOETARoute _readIncidentEndOffsetsInETARoutes] : 208 -> 212
~ -[GEOComposedRoute routeInitializerData] : 20 -> 36
~ -[GEORouteInitializerData directionsResponse] : 36 -> 16
~ -[GEOComposedETARouteLeg destinationWaypointInfo] : 32 -> 36
~ -[GEOWaypointInfo hasWaypointCaption] : 80 -> 56
~ -[GEOTraversalTimes .cxx_destruct] : 20 -> 40
~ -[GEOETAStep .cxx_destruct] : 164 -> 168
~ -[GEONavigabilityInfo .cxx_destruct] : 24 -> 32
~ -[GEOWaypointRoute dealloc] : 96 -> 88
~ -[GEOAdvisoriesInfo .cxx_destruct] : 224 -> 232
~ -[GEORoute dealloc] : 168 -> 192
~ -[GEORoute .cxx_destruct] : 924 -> 932
~ -[GEOStep dealloc] : 80 -> 76
~ -[GEOStep .cxx_destruct] : 368 -> 364
~ -[GEOSpokenGuidance .cxx_destruct] : 140 -> 132
~ -[GEOFormattedStringMetaData .cxx_destruct] : 44 -> 20
~ -[GEODrivingWalkingInstruction .cxx_destruct] : 224 -> 216
~ -[GEOConditionalFormattedString .cxx_destruct] : 128 -> 136
~ -[GEORestrictionZoneInfo .cxx_destruct] : 84 -> 92
~ -[GEOWaypointRouteFeatures .cxx_destruct] : 20 -> 40
~ -[GEOComposedETARoute geoTrafficBannerTexts] : 72 -> 64
~ -[GEOComposedWaypoint(GEOWaypointExtras) name] : 88 -> 100
~ -[GEOComposedRoute .cxx_destruct] : 1052 -> 1048
~ -[GEOComposedStringArgument_Distance .cxx_destruct] : 92 -> 96
~ -[GEOComposedStringArgument .cxx_destruct] : 72 -> 92
~ -[GEOComposedStringArgument_Duration .cxx_destruct] : 104 -> 112
~ -[GEOComposedWaypointDisplayInfo .cxx_destruct] : 156 -> 144
~ -[GEOComposedRouteVisualInfo .cxx_destruct] : 172 -> 168
~ -[GEOComposedRouteCellularCoverage .cxx_destruct] : 88 -> 96
~ -[GEOComposedTrafficSignal .cxx_destruct] : 36 -> 28
~ -[GEOComposedEnrouteNotice .cxx_destruct] : 84 -> 80
~ -[GEOComposedGuidanceEvent .cxx_destruct] : 252 -> 244
~ +[GEOComposedRoute supportsSecureCoding] : 24 -> 36
~ -[GEOComposedStringCondition .cxx_destruct] : 80 -> 76
~ -[GEOComposedStringSubstitutionCandidate .cxx_destruct] : 84 -> 76
~ -[GEOComposedStringArgument_String .cxx_destruct] : 100 -> 112
~ -[GEOComposedDrivingRouteStep .cxx_destruct] : 28 -> 44
~ -[GEOComposedRouteSegment .cxx_destruct] : 12 -> 36
~ -[GEOComposedRouteLeg .cxx_destruct] : 200 -> 176
~ -[GEOComposedRouteSection .cxx_destruct] : 84 -> 88
~ -[GEOCoordinateArraySupportPoint .cxx_destruct] : 36 -> 20
~ -[GEORouteInitializerData .cxx_destruct] : 168 -> 148
~ __GEOETAStepIsDirty : 128 -> 132
~ _GEOJunctionElementWriteTo : 140 -> 164
~ __GEOPBTransitArtworkIsDirty : 184 -> 160
~ +[GEOCoordinateArraySupportPoint supportsSecureCoding] : 24 -> 12
~ +[GEOComposedString supportsSecureCoding] : 12 -> 32
~ +[GEOComposedStringSubstitutionCandidate supportsSecureCoding] : 24 -> 16
~ +[GEOComposedStringArgument_String supportsSecureCoding] : 32 -> 12
~ +[GEOComposedStringCondition supportsSecureCoding] : 8 -> 24
~ +[GEOComposedRouteSegment supportsSecureCoding] : 20 -> 36
~ +[GEOComposedDrivingRouteStep supportsSecureCoding] : 36 -> 20
~ +[GEOJunction supportsSecureCoding] : 20 -> 32
~ +[GEOComposedGuidanceEvent supportsSecureCoding] : 32 -> 12
~ +[GEOComposedTrafficSignal supportsSecureCoding] : 24 -> 16
~ +[GEOComposedRouteCellularCoverage supportsSecureCoding] : 20 -> 24
~ +[GEOComposedRouteVisualInfo supportsSecureCoding] : 36 -> 8
~ +[GEOComposedStringArgument_Duration supportsSecureCoding] : 36 -> 12
~ +[GEOComposedStringArgument_Distance supportsSecureCoding] : 28 -> 16
~ +[GEORouteInitializerData supportsSecureCoding] : 16 -> 20
~ sub_18687523c -> sub_18684ce74 : 188 -> 196
~ +[GEOComposedWaypointDisplayInfo supportsSecureCoding] : 8 -> 12
~ -[GEOComposedRoute name] : 36 -> 32
~ -[GEOComposedRouteTraffic(Deprecated) trafficColorOffsets] : 336 -> 316
~ -[GEOComposedWaypoint isCurrentLocation] : 44 -> 24
~ -[GEOComposedWaypoint(GEOWaypointExtras) displayInfo] : 20 -> 28
~ __GEOWaypointPlaceCallReadAllRecursiveWithoutSynchronized : 320 -> 312
~ -[GEOFeatureStyleAttributes featureStyleAttributes] : 24 -> 32
~ -[GEOComposedWaypointDisplayInfo waypointCaption] : 28 -> 32
~ -[GEOComposedRoute visualInfos] : 8 -> 36
~ -[GEOComposedRouteMutableData trafficDelayInfos] : 16 -> 20
~ sub_186895178 -> sub_18686cdbc : 600 -> 596
~ sub_18689596c -> sub_18686d5ac : 80 -> 88
~ sub_186895bb8 -> sub_18686d800 : 140 -> 148
~ sub_18689989c -> sub_1868714ec : 92 -> 112
~ sub_18689d674 -> sub_1868752d8 : 92 -> 72
~ sub_18689d6d0 -> sub_186875320 : 240 -> 256
~ sub_18689db38 -> sub_186875798 : 320 -> 332
~ sub_18689dde8 -> sub_186875a54 : 380 -> 360
~ sub_18689e294 -> sub_186875eec : 84 -> 68
~ sub_18689e460 -> sub_1868760a8 : 372 -> 384
~ sub_18689ea3c -> sub_186876690 : 84 -> 100
~ sub_18689f144 -> sub_186876da8 : 84 -> 104
~ sub_18689f574 -> sub_1868771ec : 92 -> 96
~ sub_18689f5d0 -> sub_18687724c : 432 -> 408
~ sub_1868a00f4 -> sub_186877d58 : 372 -> 380
~ sub_1868a078c -> sub_1868783f8 : 460 -> 472
~ sub_1868a0f68 -> sub_186878be0 : 88 -> 64
~ sub_1868a0fc0 -> sub_186878c20 : 72 -> 92
~ sub_1868a1008 -> sub_186878c7c : 464 -> 468
~ sub_1868a1880 -> sub_1868794f8 : 76 -> 68
~ sub_1868a18cc -> sub_18687953c : 484 -> 460
~ sub_1868a27d4 -> sub_18687a42c : 100 -> 76
~ sub_1868a2838 -> sub_18687a478 : 136 -> 140
~ sub_1868a3080 -> sub_18687acc4 : 116 -> 92
~ sub_1868a38c4 -> sub_18687b4f0 : 116 -> 124
~ sub_1868a498c -> sub_18687c5c0 : 136 -> 148
~ sub_1868a5d00 -> sub_18687d940 : 56 -> 80
~ sub_1868a8c40 -> sub_186880898 : 608 -> 616
~ sub_1868a9498 -> sub_1868810f8 : 144 -> 164
~ sub_1868a9f38 -> sub_186881bac : 480 -> 488
~ sub_1868aa118 -> sub_186881d94 : 52 -> 56
~ sub_1868aa290 -> sub_186881f10 : 172 -> 152
~ sub_1868d15e4 -> sub_1868a9250 : 292 -> 280
~ -[GEOFlyoverRegionVersions copyWithZone:] : 128 -> 132
~ -[GEOFlyoverRegionVersions readFrom:] : 1712 -> 1716
~ _GEOCoarseLocationRingReadAllFrom : 596 -> 600
~ -[GEOCoarseLocationRing copyWithZone:] : 128 -> 132
~ _GEOPDPopularNearbyResultReadSpecified : 1292 -> 1276
~ -[GEOPDPopularNearbyResult copyWithZone:] : 380 -> 384
~ -[GEOAttribution unknownFields] : 196 -> 204
~ -[GEOAttribution _reserveRegions:] : 288 -> 264
~ -[GEOResource copyWithZone:] : 1000 -> 1004
~ -[GEOAttribution copyWithZone:] : 964 -> 968
~ -[GEOCoverageExtent copyWithZone:] : 360 -> 364
~ _GEOCoverageExtentReadAllFrom : 2004 -> 2008
~ _GEORegionalResourceReadSpecified : 2412 -> 2420
~ -[GEORegionalResource copyWithZone:] : 1084 -> 1088
~ +[GEOVersionManifest serviceVersionType] : 40 -> 12
~ -[GEOTileGroup copyWithZone:] : 720 -> 732
~ -[GEOCompanionCyclingStep copyWithZone:] : 1036 -> 1040
~ _GEOCompanionCyclingStepReadSpecified : 3256 -> 3264
~ -[GEOCompanionDriveStep copyWithZone:] : 1100 -> 1104
~ _GEOCompanionDriveStepReadSpecified : 3584 -> 3592
~ -[GEOCompanionFerryStep copyWithZone:] : 864 -> 868
~ _GEOCompanionFerryStepReadSpecified : 2064 -> 2076
~ -[GEOCompanionGenericStep copyWithZone:] : 872 -> 876
~ _GEOCompanionGenericStepReadSpecified : 2072 -> 2080
~ _GEOCompanionWalkStepReadSpecified : 2064 -> 2076
~ -[GEOCompanionWalkStep copyWithZone:] : 864 -> 868
~ _GEOPBOfflineDataConfigurationReadSpecified : 2092 -> 2072
~ -[GEOPBOfflineDataConfiguration copyWithZone:] : 544 -> 552
~ -[GEOActiveTileGroup unknownFields] : 208 -> 212
~ _GEOStaleResourceIsValid : 672 -> 676
~ -[GEORegionalResourceSet copyWithZone:] : 600 -> 604
~ _GEORegionalResourceRegionReadSpecified : 1572 -> 1576
~ -[GEORegionalResourceRegion copyWithZone:] : 944 -> 948
~ +[GEORegionalResourceTile childrenType] : 36 -> 12
~ -[GEOActiveTileSet copyWithZone:] : 1456 -> 1460
~ -[GEOActiveTileGroup copyWithZone:] : 6400 -> 6404
~ _GEOJunctionInfoReadAllFrom : 1472 -> 1476
~ -[GEOJunctionInfo copyWithZone:] : 276 -> 280
~ +[GEORouteLineStyleInfo laneChangeInfoType] : 28 -> 32
~ -[GEOStep copyWithZone:] : 2388 -> 2392
~ _GEOWiFiQualityHoursReadSpecified : 1592 -> 1568
~ -[GEOWiFiQualityHours copyWithZone:] : 352 -> 356
~ -[GEOPDAnnotatedItemListFilter copyWithZone:] : 152 -> 156
~ -[GEOPDAnnotatedItemListFilter readFrom:] : 32 -> 36
~ _GEOPDDepartureSequenceReadSpecified : 3800 -> 3808
~ -[GEOPDDepartureSequence copyWithZone:] : 1080 -> 1084
~ _GEOPDDateTimeRangeReadAllFrom : 1204 -> 1208
~ -[GEOPDDateTimeRange copyWithZone:] : 232 -> 236
~ -[GEOPDHours copyWithZone:] : 404 -> 408
~ -[GEOPDCaptionedPhotoFilter readAll:] : 232 -> 216
~ -[GEOPDCaptionedPhotoFilter copyWithZone:] : 396 -> 400
~ -[GEOPDCategorizedPhotosFilter readAll:] : 224 -> 232
~ -[GEOPDCategorizedPhotosFilter copyWithZone:] : 584 -> 588
~ _GEOPDRatingFilterReadAllFrom : 520 -> 524
~ _GEOPDPhotoFilterReadAllFrom : 664 -> 668
~ _GEOPDSpatialLookupFilterReadAllFrom : 532 -> 536
~ _GEOPDSearchResultPlacePhotoFilterReadAllFrom : 692 -> 696
~ -[GEOPDSearchResultPlacePhotoFilter copyWithZone:] : 152 -> 156
~ -[GEOPDTipFilter copyWithZone:] : 152 -> 156
~ -[GEOPDPhotoFilter copyWithZone:] : 152 -> 156
~ -[GEOPDReviewFilter copyWithZone:] : 196 -> 200
~ _GEOPBTransitLineReadSpecified : 4460 -> 4468
~ -[GEOPBTransitLine copyWithZone:] : 904 -> 908
~ _GEORPFeatureHandleReadAllFrom : 2484 -> 2488
~ -[GEORPFeatureHandle copyWithZone:] : 416 -> 420
~ _GEORPVisibleTileSetReadAllFrom : 1140 -> 1144
~ -[GEORPVisibleTileSet copyWithZone:] : 208 -> 212
~ _GEOSuggestionEntryReadSpecified : 2192 -> 2200
~ -[GEOSuggestionEntry copyWithZone:] : 928 -> 932
~ -[GEOPDFlyover copyWithZone:] : 884 -> 892
~ -[GEOPDFlyover _reserveLabelFrames:] : 248 -> 264
~ -[GEODirectionsResponse _readClientMetrics] : 204 -> 208
~ -[GEODirectionsResponse copyWithZone:] : 3620 -> 3624
~ _GEOTileSetVersionReadSpecified : 2120 -> 2132
~ -[GEOTileSetVersion copyWithZone:] : 520 -> 528
~ -[GEOETAResponse _readClientMetrics] : 220 -> 228
~ -[GEOETAResponse copyWithZone:] : 1044 -> 1048
~ -[GEOETATrafficUpdateResponse _readClientMetrics] : 200 -> 208
~ -[GEOETATrafficUpdateResponse copyWithZone:] : 1664 -> 1668

```
