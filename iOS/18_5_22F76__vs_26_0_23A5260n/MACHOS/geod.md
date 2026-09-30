## geod

> `/System/Library/PrivateFrameworks/GeoServices.framework/geod`

```diff

-1986.35.3.6.3
-  __TEXT.__text: 0x4a6c0
-  __TEXT.__auth_stubs: 0xf70
-  __TEXT.__objc_stubs: 0x95a0
-  __TEXT.__objc_methlist: 0x2bf4
-  __TEXT.__const: 0x270
-  __TEXT.__gcc_except_tab: 0x130c
-  __TEXT.__objc_methname: 0x9363
-  __TEXT.__oslogstring: 0x2ef4
-  __TEXT.__cstring: 0x5689
-  __TEXT.__objc_classname: 0x9bf
-  __TEXT.__objc_methtype: 0x1871
-  __TEXT.__unwind_info: 0x14d0
-  __DATA_CONST.__auth_got: 0x7c8
-  __DATA_CONST.__got: 0xb98
-  __DATA_CONST.__const: 0x2578
-  __DATA_CONST.__cfstring: 0x37a0
-  __DATA_CONST.__objc_classlist: 0x218
-  __DATA_CONST.__objc_catlist: 0x28
-  __DATA_CONST.__objc_protolist: 0xb0
+2018.30.5.20.2
+  __TEXT.__text: 0x5256c
+  __TEXT.__auth_stubs: 0x10e0
+  __TEXT.__objc_stubs: 0xa460
+  __TEXT.__objc_methlist: 0x30fc
+  __TEXT.__const: 0x281
+  __TEXT.__dlopen_cstrs: 0x5e
+  __TEXT.__gcc_except_tab: 0x1610
+  __TEXT.__objc_methname: 0xa3d8
+  __TEXT.__cstring: 0x65d8
+  __TEXT.__oslogstring: 0x36f7
+  __TEXT.__objc_classname: 0xaa2
+  __TEXT.__objc_methtype: 0x1e53
+  __TEXT.__unwind_info: 0x13f0
+  __DATA_CONST.__auth_got: 0x880
+  __DATA_CONST.__got: 0xd50
+  __DATA_CONST.__const: 0x28b8
+  __DATA_CONST.__cfstring: 0x4120
+  __DATA_CONST.__objc_classlist: 0x230
+  __DATA_CONST.__objc_catlist: 0x30
+  __DATA_CONST.__objc_protolist: 0xd0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x140
-  __DATA_CONST.__objc_intobj: 0xf0
-  __DATA_CONST.__objc_arraydata: 0x2c0
-  __DATA_CONST.__objc_arrayobj: 0x558
+  __DATA_CONST.__objc_superrefs: 0x168
+  __DATA_CONST.__objc_intobj: 0x180
+  __DATA_CONST.__objc_arraydata: 0x3a0
+  __DATA_CONST.__objc_arrayobj: 0x630
   __DATA_CONST.__objc_dictobj: 0x78
-  __DATA.__objc_const: 0x7608
-  __DATA.__objc_selrefs: 0x28a8
-  __DATA.__objc_ivar: 0x210
-  __DATA.__objc_data: 0x14f0
-  __DATA.__data: 0x840
-  __DATA.__bss: 0x290
+  __DATA.__objc_const: 0x4fd0
+  __DATA.__objc_selrefs: 0x2cf8
+  __DATA.__objc_ivar: 0x264
+  __DATA.__objc_data: 0x15e0
+  __DATA.__data: 0x9c0
+  __DATA.__bss: 0x278
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/Network.framework/Network
   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/PrivateFrameworks/CacheDelete.framework/CacheDelete
   - /System/Library/PrivateFrameworks/GeoServices.framework/GeoServices

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: E6A89FA0-E9A5-37E2-88EF-0516AFE3E569
-  Functions: 1381
-  Symbols:   646
-  CStrings:  3146
+  UUID: 1E230FB2-7425-3CB7-B5B2-9A364996BC46
+  Functions: 1352
+  Symbols:   712
+  CStrings:  3574
 
Symbols:
+ _CFPreferencesAppSynchronize
+ _CFPreferencesCopyAppValue
+ _CFPreferencesCopyKeyList
+ _CFPreferencesCopyMultiple
+ _CFPreferencesSetAppValue
+ _CFPreferencesSetMultiple
+ _GEOConfigGetDictionary
+ _GEOConfigGetUint64
+ _GEOConfigRemoveBlockListener
+ _GEOConfigRemoveDelegateListenerForAllKeys
+ _GEOConfigVersionKey
+ _GEOCountryConfigurationCountryCodeChangedDarwinNotification
+ _GEODefaultsClearedVersionKey
+ _GEODeviceCountryCodeKey
+ _GEOGetApproximateTapewormIterations
+ _GEOGetCountryConfigurationLog
+ _GEOInsertTapewormOnDispatchTimer
+ _GEOPlaceRequestExtrasUpdatedNotification
+ _GeoServicesConfig_CountryConfigCache
+ _GeoServicesConfig_CountryConfigUseCheckNetworkSignature
+ _GeoServicesConfig_CountryConfigurationRefreshOnReachability
+ _GeoServicesConfig_CountryConfigurationUpdateTimerInterval
+ _GeoServicesConfig_CountryProviders
+ _GeoServicesConfig_DeviceCountryCodeSourced
+ _GeoServicesConfig_DirectionsRequestURLQueryItems
+ _GeoServicesConfig_GeodTapewormEnabled
+ _GeoServicesConfig_GeodTapewormInstructionCount
+ _GeoServicesConfig_GeodTapewormTimerIntervalMs
+ _GeoServicesConfig_GetConfigStoreStringKeysForSystemMigration
+ _GeoServicesConfig_GetConfigStoreStringKeysForXPCMigration
+ _GeoServicesConfig_MapsURLCacheTTL
+ _GeoServicesConfig_OverrideCountryCode
+ _GeoServicesConfig_ShouldOverrideCountryCode
+ _OBJC_CLASS_$_GEOCountryConfigFetchGeoIPReply
+ _OBJC_CLASS_$_GEOCountryConfigFetchGeoIPRequest
+ _OBJC_CLASS_$_GEOCountryConfigUpdateReply
+ _OBJC_CLASS_$_GEOCountryConfigUpdateRequest
+ _OBJC_CLASS_$_GEODirectionsRequest
+ _OBJC_CLASS_$_GEOExperimentFetchBucketIDReply
+ _OBJC_CLASS_$_GEOExperimentFetchBucketIDRequest
+ _OBJC_CLASS_$_GEOMapServiceTraits
+ _OBJC_CLASS_$_GEOMapsURLShortenerReply
+ _OBJC_CLASS_$_GEOMapsURLShortenerRequest
+ _OBJC_CLASS_$_GEOPairedDeviceCheckinReply
+ _OBJC_CLASS_$_GEOPairedDeviceCheckinRequest
+ _OBJC_CLASS_$_GEOPairedDeviceClientInfo
+ _OBJC_CLASS_$_GEOPairedDeviceFetchGeoIPCCReply
+ _OBJC_CLASS_$_GEOPairedDeviceServiceReply
+ _OBJC_CLASS_$_GEOPlaceFetchURLCacheReply
+ _OBJC_CLASS_$_GEOPlaceFetchURLCacheRequest
+ _OBJC_CLASS_$_GEOPlacePlaceRequestExtrasRegistered
+ _OBJC_CLASS_$_GEOPlaceRegisterPlaceRequestExtras
+ _OBJC_CLASS_$_GEORequestResponseMetadataRecorder
+ _OBJC_CLASS_$_GEOThrottlerRequester
+ _OBJC_CLASS_$_GEOUserSession
+ _OBJC_CLASS_$_GEOUtilityCheckinWithPairedDeviceReply
+ _OBJC_CLASS_$_GEOUtilityCheckinWithPairedDeviceRequest
+ _OBJC_CLASS_$_NSCache
+ _OBJC_CLASS_$_NSHTTPURLResponse
+ _OBJC_CLASS_$_NSMutableURLRequest
+ _OBJC_CLASS_$_NSURLSession
+ _OBJC_CLASS_$_NSURLSessionConfiguration
+ _OBJC_CLASS_$__GEOCountryConfigurationInfo
+ __GEOConfigAddDelegateListenerForKey
+ __GEOConfigStorageSystem
+ __GEOConfigStorageUser
+ __GEOConfigStorageXPC
+ __GEODefaultsUseServer
+ __GEOFullDefaultsDomain
+ __GEO_validateCountryCode
+ __xpc_type_array
+ _geo_object_isolater_create
+ _kCFErrorDescriptionKey
+ _kCFPreferencesAnyHost
+ _kCFPreferencesCurrentUser
+ _kCountryProvidersChangedDarwinNotification
+ _nw_context_copy_implicit_context
+ _nw_context_set_privacy_level
+ _xpc_array_get_count
+ _xpc_dictionary_get_array
- _GEODiskSpaceProviderFreePurgableRequestTimeout
- _GEODiskSpaceProviderPurgableRequestTimeout
- _GEOExperimentInfoChangedInternalNotification
- _GEOMigrateDefaults
- _OBJC_CLASS_$_GEODiskSpaceManager
- _OBJC_CLASS_$_GEOExperimentServerLocalProxy
- _OBJC_CLASS_$_GEOPairedDevicePingReply
- _OBJC_CLASS_$_GEOPairedDevicePingRequest
- _OBJC_CLASS_$_GEOPlaceCardDiskSpaceProvider
- _OBJC_CLASS_$_GEOTileCacheDiskSpaceProvider
- _OBJC_METACLASS_$_GEODiskSpaceManager
- _OBJC_METACLASS_$_GEOExperimentServerLocalProxy
- _OBJC_METACLASS_$_GEOPlaceCardDiskSpaceProvider
- _OBJC_METACLASS_$_GEOTileCacheDiskSpaceProvider
CStrings:
+ "%@:%@"
+ "-[GEOPDPlaceCache _evictPlaceWithHash:]"
+ "-[GEOPDPlaceCache _storePlace:withHash:forRequestKeys:]"
+ "-[GEOPDPlaceCache calculateFreeableSpaceSync]"
+ "-[GEOPDPlaceCache calculateFreeableSpaceWithHandler:]"
+ "-[GEOPDPlaceCache cancelCleanupBlockSchedule]"
+ "-[GEOPDPlaceCache deletePhoneNumberMapping]"
+ "-[GEOPDPlaceCache enqueueAccessTimeUpdateForCacheKey:accessTime:]"
+ "-[GEOPDPlaceCache evictAllEntries]"
+ "-[GEOPDPlaceCache lookupIdentifierByPhoneNumber:]"
+ "-[GEOPDPlaceCache lookupPlaceByIdentifier:allowExpired:resultBlock:]"
+ "-[GEOPDPlaceCache runCleanupBlock:inSecondsFromNow:]"
+ "-[GEOPDPlaceCache scheduleCleanup]"
+ "-[GEOPDPlaceCache shrinkBySize:finished:]"
+ "-[GEOPDPlaceCache shrinkBySizeSync:]"
+ "-[GEOPDPlaceCache storePlace:forRequest:]"
+ "-[GEOPDPlaceCache storePlace:forRequest:completionQueue:completion:]"
+ "-[GEOPDPlaceCache trackPlace:]"
+ "-[GEOPDPlaceCache trackPlace:completionQueue:completion:]"
+ "@\"<GEOCancellable>\""
+ "@\"<_GEOCountryConfigurationServerProxyDelegate>\""
+ "@\"NSCache\""
+ "@\"geo_object_isolater\""
+ "@20@0:8I16"
+ "@32@0:8@\"<_GEOCountryConfigurationServerProxyDelegate>\"16@\"NSObject<OS_dispatch_queue>\"24"
+ "@expire_time"
+ "@long_url"
+ "@rowid"
+ "@short_url"
+ "AddressCorrectionAuthStatus"
+ "Assertion failed: name.length > 0"
+ "B32@?0@\"NSURL\"8@\"NSURL\"16q24"
+ "B32@?0q8@\"NSString\"16Q24"
+ "B40@?0q8@\"NSString\"16@\"NSString\"24Q32"
+ "B48@?0r^{_GEOTileKey=b7b1(?={_GEOStandardTileKey=b40b6b26b26b14b4b4}{_GEOGloriaQuadIDTileKey=b6b64b14b4(?={?=b10b10b12}{?=b10b22}I)}{_GEORegionalResourceKey=b32b8b6b8b8b1b57}{_GEOSputnikMetadataKey=b32b24b14b8b42}{_GEOFlyoverKey=b6b26b26b8b24b14b8b8}{_GEOTransitLineSelectionKey=b6b25b25b64}{_GEOPolygonSelectionKey=b6b25b25b64}{_GEORoadSelectionKey=b6b25b25b64}{_GEOContourLinesKey=b6b26b26b4b8b50}{_GEOTileOverlayKey=b6b26b26b8b32b16b6}{_GEOIdentifiedResourceKey=QCCb1b39}{_GEOMuninMeshKey=b64b32b16b5b3}{_GEOVisualLocalizationTrackKey=SCb16b6b26b26b22}{_GEOVisualLocalizationMetadataKey=b6b9b25b6b26b26b22}{_GEOVisualLocalizationDataKey=QCb5b21b21b1}{_GEOS2TileKey=b6b26b26b3b14b4b4b37}{_GEOLiveTileKey=b6b26b26b14b4b4b4b36})}8@\"GEOTileData\"16B24@\"NSString\"28C36d40"
+ "Became reachable. Scheduling country code update"
+ "COMPONENT_TYPE_BRAND_LOGO_EMBEDDING"
+ "COMPONENT_TYPE_EXPERT_CONTENT"
+ "COMPONENT_TYPE_LOCALIZED_NAMES"
+ "COMPONENT_TYPE_VISITED_PLACES_META_DATA"
+ "COMPONENT_TYPE_VISUAL_EVIDENCE"
+ "CREATE INDEX IF NOT EXISTS maps_url_expire_time_idx ON maps_url (expire_time);"
+ "CREATE INDEX IF NOT EXISTS maps_url_long_url_idx ON maps_url (long_url);"
+ "CREATE INDEX IF NOT EXISTS maps_url_short_url_idx ON maps_url (short_url);"
+ "CREATE TABLE IF NOT EXISTS maps_url (    rowid INTEGER PRIMARY KEY NOT NULL,    short_url TEXT NOT NULL UNIQUE,    long_url TEXT NOT NULL UNIQUE,    expire_time INT NOT NULL    );"
+ "ClimateShowAirQualityIndex"
+ "ClimateShowWeatherConditions"
+ "ConsoleLogLevel"
+ "Could not determine current country code: %{public}@"
+ "Country Code"
+ "Country code '%{public}@' is not a valid ISO 3166-1 alpha-2 country code. Ignoring..."
+ "Country code changed. Informing delegate"
+ "Country-specific networkDefaults changed. Informing delegate"
+ "CountryConfiguration"
+ "CountryProviders"
+ "DELETE FROM maps_url    WHERE expire_time < @expire_time;"
+ "DELETE FROM maps_url;"
+ "DROP TABLE maps_url"
+ "DefaultsSanitizedVersion"
+ "DeleteMapsURLs"
+ "DeviceCountryCode"
+ "DeviceCountryCodeSourced"
+ "DisableSundanceCleanup"
+ "Error iterating Maps URLs: %@"
+ "Error trying to lookup long maps url: %@"
+ "Error trying to lookup short maps url: %@"
+ "Error updating maps url expiry: %@"
+ "Failed to store maps urls: %@"
+ "Finished updating country configuration. Calling callback."
+ "Found %d keys (met threshold %d) running Sundance cleanup"
+ "Found %d keys (under threshold %d) NOT running Sundance cleanup"
+ "GEOAddressCorrectionEnabled"
+ "GEOConfigChangeListenerDelegate"
+ "GEOLastNetworkDefaultsURL"
+ "GEOLocalizedCategoriesURL"
+ "GEOMapAppearanceModeKey"
+ "GEOMapLocalizeLabels"
+ "GEOMapsAuthToken"
+ "GEOMapsRefreshToken"
+ "GEOMapsURLShorteningServer"
+ "GEOResourceManifestUpdateTimeInterval"
+ "GEOUseProductionURLs"
+ "GEOVoltaireDirectionsURL"
+ "GEOVoltaireETAURL"
+ "GEOVoltaireProblemURL"
+ "GEOVoltaireResourceManifestURL"
+ "GEOVoltaireSearchAttributionManifestURL"
+ "GetAllMapsURLs"
+ "GetLocale"
+ "GetLongMapsURL"
+ "GetShortMapsURL"
+ "Got non-200 result %d: %@"
+ "Got non-30[123] result %d"
+ "Got response of unexpected type %@"
+ "HelpImproveMapsAddressCorrectionAuthStatus"
+ "Helpers"
+ "INSERT OR REPLACE INTO maps_url    (short_url, long_url, expire_time)    VALUES (@short_url, @long_url, @expire_time);"
+ "Invalid options"
+ "LAYER_ROUTING_V4"
+ "LAYER_ROUTING_V4_METADATA"
+ "LAYER_ROUTING_V4_TRAFFIC_INCIDENTS"
+ "LAYER_ROUTING_V4_TRANSIT"
+ "LAYER_ROUTING_V5"
+ "LAYER_ROUTING_V5_METADATA"
+ "LAYER_ROUTING_V5_TRAFFIC_INCIDENTS"
+ "LAYER_ROUTING_V5_TRANSIT"
+ "Lengthen result: %{private}@ - %{private, mask.hash}@ - %{public}@"
+ "Lengthened URL: \"%{private, mask.hash}@\" wasCached: %{private}s error: %{public}@"
+ "Lengthening URL: \"%{private, mask.hash}@\""
+ "Location"
+ "LogLevel"
+ "Missing request or traits"
+ "NSURLSessionDelegate"
+ "NSURLSessionTaskDelegate"
+ "NavigationShowHeadingKey"
+ "NavigationShowSpeedLimitKey"
+ "Network signature unchanged, not updating"
+ "No shortening service URL available, failing"
+ "Not an HTTP response object?!"
+ "Not updating access time for MapsURL cache, was last touched %d seconds ago (min is %d seconds)"
+ "Overriding country code to '%{private}@' (is actually '%{private}@')"
+ "POST"
+ "PreferredTransportType"
+ "PruneMapsURLs"
+ "RDEstimate"
+ "Reachability changed: %{private}@"
+ "Received country code '%{private}@' from network"
+ "Received country code change notification. Informing delegate."
+ "Received country providers change notification. Informing delegate."
+ "Received error: %@"
+ "Received non-ISO 3166-1 alpha-2 country code"
+ "Refusing to update country code again, will try again in %f seconds: %{public}@"
+ "Regulatory Domain updated. Scheduling country code update"
+ "RegulatoryDomain.framework is not available"
+ "Response \"%@\" was not a valid URL"
+ "Result code %d"
+ "Result code %d: %@"
+ "SELECT rowid, long_url, expire_time    FROM maps_url    WHERE short_url = @short_url;"
+ "SELECT rowid, short_url, expire_time    FROM maps_url    WHERE long_url = @long_url;"
+ "SELECT rowid, short_url, long_url, expire_time    FROM maps_url;"
+ "SetMapsURL"
+ "Shorten result: %{private}@ - %{private, mask.hash}@ - %{public}@"
+ "Shortened URL: \"%{private, mask.hash}@\" wasCached: %{private}s error: %{public}@"
+ "Shortening URL: \"%{private, mask.hash}@\""
+ "Sundance cleanup disabled, not running"
+ "UPDATE maps_url    SET expire_time = @expire_time    WHERE rowid = @rowid;"
+ "URLSession:didBecomeInvalidWithError:"
+ "URLSession:didCreateTask:"
+ "URLSession:didReceiveChallenge:completionHandler:"
+ "URLSession:task:didCompleteWithError:"
+ "URLSession:task:didFinishCollectingMetrics:"
+ "URLSession:task:didReceiveChallenge:completionHandler:"
+ "URLSession:task:didReceiveInformationalResponse:"
+ "URLSession:task:didSendBodyData:totalBytesSent:totalBytesExpectedToSend:"
+ "URLSession:task:needNewBodyStream:"
+ "URLSession:task:needNewBodyStreamFromOffset:completionHandler:"
+ "URLSession:task:willBeginDelayedRequest:completionHandler:"
+ "URLSession:task:willPerformHTTPRedirection:newRequest:completionHandler:"
+ "URLSession:taskIsWaitingForConnectivity:"
+ "URLSessionDidFinishEventsForBackgroundURLSession:"
+ "URLShortener"
+ "Unreachable reached: Invalid source: %d"
+ "Update timer fired. Updating country code"
+ "UpdateMapsURLExpiry"
+ "XZ"
+ "_GEOCountryConfigurationLocalProxy"
+ "_GEOCountryConfigurationRemoteProxy"
+ "_GEOCountryConfigurationServerProxy"
+ "_addSubscriptionWithIdentifier:auditToken:dataTypes:policy:region:displayName:expirationDate:updateInterval:callbackQueue:completionHandler:"
+ "_buildNetworkSignature"
+ "_cache"
+ "_cacheIsolater"
+ "_callCompletionHandler:"
+ "_callback"
+ "_callbackQueue"
+ "_checkThrottlerOrScheduleUpdate:"
+ "_checkinWithPairedDevice:"
+ "_clampedTimeout"
+ "_countryCodeChangedToken"
+ "_countryCodeOverrideChangeListener"
+ "_delegateQueue"
+ "_determineGeoIPCountryCode:completion:"
+ "_determineGeoIPCountryCodeLocal:"
+ "_determineRegulatoryDomain:"
+ "_determineRegulatoryDomainSync:"
+ "_expandURL:asyncCompletion:"
+ "_geoIPCompletions"
+ "_geoIPLookupTask"
+ "_geo_arrayFromXPCObject:"
+ "_geo_setTLSMinimumSupportedProtocolVersion"
+ "_getCachedCountryInfoForSource:"
+ "_getNetworkSignature:"
+ "_postNotificationsForOldInfo:newInfo:"
+ "_processLengthenResponse:data:error:completion:"
+ "_processShortenResponse:data:error:completion:"
+ "_providersChangedToken"
+ "_reachabilityChanged:"
+ "_regulatoryDomainListener"
+ "_regulatoryDomainUpdated"
+ "_safePairedDeviceClientInfo"
+ "_scheduleUpdate:source:"
+ "_scheduledUpdateTimer"
+ "_sessionCache"
+ "_sessionCacheIsolater"
+ "_shortenURL:asyncCompletion:"
+ "_updateCachedCountryInfo:"
+ "_updateCountryCode:"
+ "_updateMapsURLExpiry:expireTime:"
+ "_updatePairedDeviceInfo"
+ "_urlSession:"
+ "_withCache:"
+ "_xpcConnection"
+ "addNetworkReachableObserver:selector:"
+ "addSupportedMessages:"
+ "allHeaderFields"
+ "arrayWithArray:"
+ "asynchronousGetURL:kind:auditToken:requestCounterTicket:queue:completionHandler:"
+ "base64EncodedStringWithOptions:"
+ "bluepoi"
+ "cc"
+ "checkin"
+ "checkinWithPairedDeviceMessage:completionHandler:"
+ "checkinWithPairedDeviceWithRequest:"
+ "cis"
+ "clientInfo"
+ "com.apple.GeoServices.CountryCode"
+ "com.apple.GeoServices.CountryConfiguration.cache"
+ "com.apple.GeoServices.OfflineService"
+ "com.apple.geo.CountryConfiguration.lp"
+ "com.apple.geo.CountryConfiguration.rp"
+ "com.apple.geoservices.experiments.bucket-id.read"
+ "com.apple.geoservices.geoip"
+ "com.apple.geoservices.register_place_request_extras"
+ "countryCode:source:"
+ "createServerConnectionFor:debugIdentifier:eventHandler:"
+ "current RDEstimate < kRDPriorityWiFiAP or == \"%@\", ignoring"
+ "current RDEstimate count == %d, ignoring"
+ "currentEstimates"
+ "currentPairedDeviceClientInfo"
+ "dataTaskWithRequest:completionHandler:"
+ "dataUsingEncoding:"
+ "dateOfLastUpdate"
+ "deleteExisting"
+ "dictionaryWithObject:forKey:"
+ "encodeAsDictionary"
+ "ephemeralSessionConfiguration"
+ "expandURLWithRequest:"
+ "extras are not encodeable as data??"
+ "extras are not parseable as GEOPDPlaceRequest"
+ "fetchAllURLCacheEntriesWithRequest:"
+ "fetchAllURLCacheEntriesWithRequesterHandler:"
+ "fetchBucketID:"
+ "fetchBucketIDWithRequest:"
+ "fetchGEOIPCCWithPairedDeviceMessage:completionHandler:"
+ "fetchGEOIPCCWithRequest:"
+ "fetchGEOIPCountryCode:auditToken:callback:"
+ "fetchGEOIPCountryCode:callback:"
+ "fetchGeoIpCc"
+ "fetchRawShiftFunctionResponseForRequest:auditToken:callbackQueue:completionHandler:"
+ "fetchShiftFunctionWithPairedDeviceMessage:completionHandler:"
+ "forced"
+ "geo_hasApplicationAttribution:"
+ "geo_setApplicationAttribution:"
+ "geoip"
+ "get"
+ "getCurrentPairedDeviceClientInfo:"
+ "hasPrivacyMetadata"
+ "hasRedactedAnalyticData"
+ "initWithCountryCode:source:"
+ "initWithData:encoding:"
+ "initWithDelegate:delegateQueue:"
+ "initWithDictionary:"
+ "initWithProxiedApplicationBundleId:"
+ "initializeIfNecessary"
+ "isEqualToDictionary:"
+ "isNetworkReachable"
+ "issuePlaceRequestWithPairedDeviceMessage:completionHandler:"
+ "iterateAllMapsURLsWithBlock:finishedBlock:"
+ "kRDPriorityWiFiAP"
+ "kRegulatoryDomainUpdateNotification"
+ "loadKey:additionalInfo:priority:forClient:auditToken:options:cacheInfo:reason:qos:signpostID:createTime:callbackQ:beginNetwork:callback:"
+ "local"
+ "location"
+ "locationShift"
+ "lookupLongMapsURLFor:completion:"
+ "lookupShortMapsURLFor:completion:"
+ "mapsurlshortener"
+ "mcc"
+ "messageQueue"
+ "metadata"
+ "networkSignature"
+ "numberWithUnsignedLong:"
+ "overrideTokenWithOfflineCohortId:"
+ "overrideTokenWithSecondaryIdentifier:"
+ "placeRequest"
+ "priorityIsAtLeast:"
+ "privacyMetadata"
+ "processURLWithRequest:"
+ "q"
+ "rd"
+ "received GeoIP country code of unexpected length"
+ "recordRedactedDirectionsRequestResponseAnalyticsData:"
+ "redactedAnalyticData"
+ "registerPlaceRequestExtrasWithRequest:"
+ "removeNetworkReachableObserver:"
+ "requestCompleted:"
+ "requestWithURL:cachePolicy:timeoutInterval:"
+ "resume"
+ "rideBookingExtensionsEnabledStatusKey"
+ "rideBookingShouldAutomaticallyEnableExtensionsKey"
+ "sendCheckin:withReply:"
+ "serverProxy:countryCodeDidChange:"
+ "serverProxyProvidersDidChange:"
+ "session"
+ "sessionWithConfiguration:"
+ "setBucket:"
+ "setCheckin:"
+ "setClientInfo:"
+ "setClientVersion:"
+ "setCountryCode:"
+ "setFetchGeoIpCc:"
+ "setHTTPBody:"
+ "setHTTPMethod:"
+ "setInitialShareSessionWithMaps:"
+ "setLocationShift:"
+ "setPlaceRequest:"
+ "setPrivacyMetadata:"
+ "setResponseData:"
+ "setValue:"
+ "set_usesNWLoader:"
+ "sharedCache"
+ "shorten"
+ "shortenURLWithRequest:"
+ "shouldCacheByBasemapIDForRequest:"
+ "signature"
+ "softlink:o:path:/System/Library/PrivateFrameworks/RegulatoryDomain.framework/RegulatoryDomain"
+ "startingRequestWithTask:"
+ "statusCode"
+ "storeShortMapURL:longMapsURL:"
+ "supportsMultiUser"
+ "timeoutSeconds"
+ "toServerResponse"
+ "unable to convert GeoIP country code to string"
+ "unable to prune urls: %@"
+ "updateCountryCodeWithCallbackQueue:callback:"
+ "updateCountryConfiguration:"
+ "updateInterval"
+ "updateTimestamp"
+ "updateWithRequest:"
+ "v16@?0@\"GEODataURLSessionTask\"8"
+ "v16@?0@\"NSMutableDictionary\"8"
+ "v16@?0@\"NSString\"8"
+ "v16@?0@\"NSURL\"8"
+ "v20@0:8I16"
+ "v24@0:8@\"NSURLSession\"16"
+ "v24@0:8@?<v@?@\"NSNumber\"@\"NSError\">16"
+ "v24@?0@\"GEOCountryConfigFetchGeoIPReply\"8@\"NSError\"16"
+ "v24@?0@\"GEOCountryConfigUpdateReply\"8@\"NSError\"16"
+ "v24@?0@\"GEOPairedDeviceCheckinReply\"8@\"NSError\"16"
+ "v24@?0@\"GEOPairedDeviceClientInfo\"8@\"NSError\"16"
+ "v24@?0@\"GEOPairedDeviceFetchGeoIPCCReply\"8@\"NSError\"16"
+ "v24@?0@\"GEOPairedDeviceServiceReply\"8@\"NSError\"16"
+ "v24@?0@\"NSNumber\"8@\"NSError\"16"
+ "v24@?0@\"NSString\"8@\"NSError\"16"
+ "v28@0:8d16I24"
+ "v28@?0@\"NSURL\"8B16@\"NSError\"20"
+ "v28@?0I8@\"NSString\"12@\"NSError\"20"
+ "v32@0:8@\"NSObject<OS_dispatch_queue>\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@\"NSURLSession\"16@\"NSError\"24"
+ "v32@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24"
+ "v32@0:8q16Q24"
+ "v32@0:8{?=I^v}16"
+ "v32@?0@\"NSData\"8@\"NSURLResponse\"16@\"NSError\"24"
+ "v32@?0@\"NSString\"8@\"NSString\"16^B24"
+ "v40@0:8@\"NSObject<OS_dispatch_queue>\"16@\"GEOApplicationAuditToken\"24@?<v@?@\"NSString\"@\"NSDate\"@\"NSError\">32"
+ "v40@0:8@\"NSURLSession\"16@\"NSURLAuthenticationChallenge\"24@?<v@?q@\"NSURLCredential\">32"
+ "v40@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24@\"NSError\"32"
+ "v40@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24@\"NSHTTPURLResponse\"32"
+ "v40@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24@\"NSURLSessionTaskMetrics\"32"
+ "v40@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24@?<v@?@\"NSInputStream\">32"
+ "v48@0:8@\"NSData\"16@\"GEOApplicationAuditToken\"24@\"NSObject<OS_dispatch_queue>\"32@?<v@?@\"NSData\"@\"NSError\">40"
+ "v48@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24@\"NSURLAuthenticationChallenge\"32@?<v@?q@\"NSURLCredential\">40"
+ "v48@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24@\"NSURLRequest\"32@?<v@?q@\"NSURLRequest\">40"
+ "v48@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24q32@?<v@?@\"NSInputStream\">40"
+ "v48@0:8@16@24q32@?40"
+ "v48@?0r^{_GEOTileKey=b7b1(?={_GEOStandardTileKey=b40b6b26b26b14b4b4}{_GEOGloriaQuadIDTileKey=b6b64b14b4(?={?=b10b10b12}{?=b10b22}I)}{_GEORegionalResourceKey=b32b8b6b8b8b1b57}{_GEOSputnikMetadataKey=b32b24b14b8b42}{_GEOFlyoverKey=b6b26b26b8b24b14b8b8}{_GEOTransitLineSelectionKey=b6b25b25b64}{_GEOPolygonSelectionKey=b6b25b25b64}{_GEORoadSelectionKey=b6b25b25b64}{_GEOContourLinesKey=b6b26b26b4b8b50}{_GEOTileOverlayKey=b6b26b26b8b32b16b6}{_GEOIdentifiedResourceKey=QCCb1b39}{_GEOMuninMeshKey=b64b32b16b5b3}{_GEOVisualLocalizationTrackKey=SCb16b6b26b26b22}{_GEOVisualLocalizationMetadataKey=b6b9b25b6b26b26b22}{_GEOVisualLocalizationDataKey=QCb5b21b21b1}{_GEOS2TileKey=b6b26b26b3b14b4b4b37}{_GEOLiveTileKey=b6b26b26b14b4b4b4b36})}8@\"GEOTileData\"16Q24@\"NSError\"32@\"NSDictionary\"40"
+ "v56@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24@\"NSHTTPURLResponse\"32@\"NSURLRequest\"40@?<v@?@\"NSURLRequest\">48"
+ "v56@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24q32q40q48"
+ "v56@0:8@16@24@32r^{_GEOTileKey=b7b1(?={_GEOStandardTileKey=b40b6b26b26b14b4b4}{_GEOGloriaQuadIDTileKey=b6b64b14b4(?={?=b10b10b12}{?=b10b22}I)}{_GEORegionalResourceKey=b32b8b6b8b8b1b57}{_GEOSputnikMetadataKey=b32b24b14b8b42}{_GEOFlyoverKey=b6b26b26b8b24b14b8b8}{_GEOTransitLineSelectionKey=b6b25b25b64}{_GEOPolygonSelectionKey=b6b25b25b64}{_GEORoadSelectionKey=b6b25b25b64}{_GEOContourLinesKey=b6b26b26b4b8b50}{_GEOTileOverlayKey=b6b26b26b8b32b16b6}{_GEOIdentifiedResourceKey=QCCb1b39}{_GEOMuninMeshKey=b64b32b16b5b3}{_GEOVisualLocalizationTrackKey=SCb16b6b26b26b22}{_GEOVisualLocalizationMetadataKey=b6b9b25b6b26b26b22}{_GEOVisualLocalizationDataKey=QCb5b21b21b1}{_GEOS2TileKey=b6b26b26b3b14b4b4b37}{_GEOLiveTileKey=b6b26b26b14b4b4b4b36})}40@48"
+ "v56@0:8@16@24q32q40q48"
+ "valueChangedForGEOConfigKey:"
+ "version"
- "/AppleInternal/Library/Frameworks/PairedDeviceRegistry.framework/PairedDeviceRegistry"
- "/System/AppleInternal/Library/Frameworks/PairedDeviceRegistry.framework/PairedDeviceRegistry"
- "/System/Library/Frameworks/PairedDeviceRegistry.framework/PairedDeviceRegistry"
- "/System/Library/PrivateFrameworks/PairedDeviceRegistry.framework/PairedDeviceRegistry"
- "@\"GEOPDPlaceCache\""
- "Assertion failed: _offlineService != ((void *)0)"
- "B48@?0r^{_GEOTileKey=b7b1(?={_GEOStandardTileKey=b40b6b26b26b14b4b4}{_GEOGloriaQuadIDTileKey=b6b64b14b4(?={?=b10b10b12}I)}{_GEORegionalResourceKey=b32b8b6b8b8b1b57}{_GEOSputnikMetadataKey=b32b24b14b8b42}{_GEOFlyoverKey=b6b26b26b8b24b14b8b8}{_GEOTransitLineSelectionKey=b6b25b25b64}{_GEOPolygonSelectionKey=b6b25b25b64}{_GEORoadSelectionKey=b6b25b25b64}{_GEOContourLinesKey=b6b26b26b4b8b50}{_GEOTileOverlayKey=b6b26b26b8b32b16b6}{_GEOIdentifiedResourceKey=QCCb1b39}{_GEOMuninMeshKey=b64b32b16b5b3}{_GEOVisualLocalizationTrackKey=SCb16b6b26b26b22}{_GEOVisualLocalizationMetadataKey=b6b9b25b6b26b26b22}{_GEOVisualLocalizationDataKey=QCb5b21b21b1}{_GEOS2TileKey=b6b26b26b3b14b4b4b37}{_GEOLiveTileKey=b6b26b26b14b4b4b4b36})}8@\"GEOTileData\"16B24@\"NSString\"28C36d40"
- "GEODirectionsRequesterServerLocalProxy"
- "GetValue"
- "INVALID"
- "LSApplicationRecord"
- "MAPurgeAll"
- "MAPurgeCatalogs"
- "Missign request or traits"
- "NRDevice"
- "NRDevicePropertyIsActive"
- "NRDevicePropertyIsAltAccount"
- "NRDevicePropertyProductType"
- "NRDevicePropertyScreenScale"
- "NRDevicePropertySystemBuildVersion"
- "NRDevicePropertySystemVersion"
- "NRPairedDeviceRegistryDevicesDidUpdateNotification"
- "NRVersionIsGreaterThanOrEqual"
- "NRWatchOSVersionForRemoteDevice"
- "PDRRegistry"
- "PING"
- "PONG"
- "_addSubscriptionWithIdentifier:auditToken:dataTypes:policy:region:displayName:expirationDate:callbackQueue:completionHandler:"
- "_pdPlaceCache"
- "bid"
- "loadKey:additionalInfo:priority:forClient:auditToken:options:reason:qos:signpostID:createTime:callbackQ:beginNetwork:callback:"
- "pingOverIDSWithMessage:"
- "pingWithPairedDeviceMessage:completionHandler:"
- "processRequest:requestMetaData:queue:response:"
- "readReqRespMetadataWithMessage:"
- "requestMetadata"
- "requestResponseMetadataFileDescriptorForBatchID:"
- "sendPing:withReply:"
- "serverQueue"
- "setPing:"
- "setResponseMetadata:"
- "setType:"
- "shouldCacheByIDForRequest:"
- "v24@?0@\"GEOPairedDevicePingReply\"8@\"NSError\"16"
- "v32@?0@\"NSData\"8@\"NSData\"16@\"NSError\"24"
- "v48@?0r^{_GEOTileKey=b7b1(?={_GEOStandardTileKey=b40b6b26b26b14b4b4}{_GEOGloriaQuadIDTileKey=b6b64b14b4(?={?=b10b10b12}I)}{_GEORegionalResourceKey=b32b8b6b8b8b1b57}{_GEOSputnikMetadataKey=b32b24b14b8b42}{_GEOFlyoverKey=b6b26b26b8b24b14b8b8}{_GEOTransitLineSelectionKey=b6b25b25b64}{_GEOPolygonSelectionKey=b6b25b25b64}{_GEORoadSelectionKey=b6b25b25b64}{_GEOContourLinesKey=b6b26b26b4b8b50}{_GEOTileOverlayKey=b6b26b26b8b32b16b6}{_GEOIdentifiedResourceKey=QCCb1b39}{_GEOMuninMeshKey=b64b32b16b5b3}{_GEOVisualLocalizationTrackKey=SCb16b6b26b26b22}{_GEOVisualLocalizationMetadataKey=b6b9b25b6b26b26b22}{_GEOVisualLocalizationDataKey=QCb5b21b21b1}{_GEOS2TileKey=b6b26b26b3b14b4b4b37}{_GEOLiveTileKey=b6b26b26b14b4b4b4b36})}8@\"GEOTileData\"16Q24@\"NSError\"32@\"NSDictionary\"40"
- "v56@0:8@16@24@32r^{_GEOTileKey=b7b1(?={_GEOStandardTileKey=b40b6b26b26b14b4b4}{_GEOGloriaQuadIDTileKey=b6b64b14b4(?={?=b10b10b12}I)}{_GEORegionalResourceKey=b32b8b6b8b8b1b57}{_GEOSputnikMetadataKey=b32b24b14b8b42}{_GEOFlyoverKey=b6b26b26b8b24b14b8b8}{_GEOTransitLineSelectionKey=b6b25b25b64}{_GEOPolygonSelectionKey=b6b25b25b64}{_GEORoadSelectionKey=b6b25b25b64}{_GEOContourLinesKey=b6b26b26b4b8b50}{_GEOTileOverlayKey=b6b26b26b8b32b16b6}{_GEOIdentifiedResourceKey=QCCb1b39}{_GEOMuninMeshKey=b64b32b16b5b3}{_GEOVisualLocalizationTrackKey=SCb16b6b26b26b22}{_GEOVisualLocalizationMetadataKey=b6b9b25b6b26b26b22}{_GEOVisualLocalizationDataKey=QCb5b21b21b1}{_GEOS2TileKey=b6b26b26b3b14b4b4b37}{_GEOLiveTileKey=b6b26b26b14b4b4b4b36})}40@48"

```
