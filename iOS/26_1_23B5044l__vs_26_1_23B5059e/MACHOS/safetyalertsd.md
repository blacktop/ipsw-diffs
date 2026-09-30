## safetyalertsd

> `/usr/libexec/safetyalertsd`

```diff

-64.0.25.0.0
-  __TEXT.__text: 0xd27d0
-  __TEXT.__auth_stubs: 0x1000
-  __TEXT.__objc_stubs: 0x2d80
+64.0.26.0.0
+  __TEXT.__text: 0xd707c
+  __TEXT.__auth_stubs: 0xfc0
+  __TEXT.__objc_stubs: 0x2ee0
   __TEXT.__init_offsets: 0x4
   __TEXT.__objc_methlist: 0xa84
-  __TEXT.__const: 0x9c18
-  __TEXT.__gcc_except_tab: 0xc5ac
-  __TEXT.__cstring: 0x504b
-  __TEXT.__oslogstring: 0x343af
+  __TEXT.__const: 0x9848
+  __TEXT.__gcc_except_tab: 0xcafc
+  __TEXT.__cstring: 0x51e8
+  __TEXT.__oslogstring: 0x35c4d
   __TEXT.__objc_classname: 0x1ea
-  __TEXT.__objc_methname: 0x366e
+  __TEXT.__objc_methname: 0x37a4
   __TEXT.__objc_methtype: 0x1939
   __TEXT.__ustring: 0x18
-  __TEXT.__unwind_info: 0x3cd8
-  __DATA_CONST.__auth_got: 0x810
-  __DATA_CONST.__got: 0x4d8
+  __TEXT.__unwind_info: 0x3d68
+  __DATA_CONST.__auth_got: 0x7f0
+  __DATA_CONST.__got: 0x4b8
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x8118
-  __DATA_CONST.__cfstring: 0x5700
+  __DATA_CONST.__const: 0x8018
+  __DATA_CONST.__cfstring: 0x5860
   __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x20
   __DATA_CONST.__objc_intobj: 0x30
   __DATA.__objc_const: 0x1160
-  __DATA.__objc_selrefs: 0xfc8
+  __DATA.__objc_selrefs: 0x1020
   __DATA.__objc_ivar: 0x7c
   __DATA.__objc_data: 0x280
   __DATA.__data: 0x430
-  __DATA.__bss: 0x530
+  __DATA.__bss: 0x550
   __DATA.__common: 0x48
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth

   - /usr/lib/libTelephonyUtilDynamic.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: EC27D12A-0C9D-30AC-AD52-08D6F65A7CB2
-  Functions: 3249
-  Symbols:   429
-  CStrings:  4374
+  UUID: 012C6135-CA11-3D6F-A0BD-4D7CEB52F6B9
+  Functions: 3251
+  Symbols:   421
+  CStrings:  4464
 
Symbols:
+ _OBJC_CLASS_$_GEOMapDataSubscriptionManager
+ _OBJC_CLASS_$_GEOMapRegion
- _CGPointZero
- _GEOActiveTileGroupChangedNotification
- _MKCoordinateRegionMakeWithDistance
- _OBJC_CLASS_$_MKMapSnapshotOptions
- _OBJC_CLASS_$_MKMapSnapshotter
- _OBJC_CLASS_$_UIGraphicsImageRenderer
- _OBJC_CLASS_$_UITraitCollection
- _UIImagePNGRepresentation
- _notify_cancel
- _notify_register_dispatch
CStrings:
+ "BYPASS_DOWNLOAD"
+ "CurrentLocation"
+ "MAPS_PRECACHE_DWELLING_DURATION_SECONDS"
+ "MAPS_PRECACHE_EXPIRATION_AGE_SECONDS"
+ "MAPS_PRECACHE_LOI_LOOKBACK_TIME_SECONDS"
+ "MAPS_PRECACHE_MAX_ALLOWED_REGIONS_COUNT"
+ "MAPS_PRECACHE_PERIODIC_TRIGGER_INTERVAL_SECONDS"
+ "MAPS_PRECACHE_REGION_RADIUS_METERS"
+ "No subscriptions to remove"
+ "Routine instance is invalid"
+ "UUIDString"
+ "addSubscriptionWithIdentifier:dataTypes:policy:region:expirationDate:callbackQueue:completionHandler:"
+ "code"
+ "com.apple.safetyalertsd.region_"
+ "com.apple.safetyalertsd.region_*"
+ "dateByAddingTimeInterval:"
+ "domain"
+ "eastLng"
+ "efficacy_manifest_v4.txt"
+ "entryDate"
+ "exitDate"
+ "fetchLocationsOfInterestVisitedBetweenStartDate:endDate:withHandler:"
+ "fetchSubscriptionsWithIdentifiers:callbackQueue:completionHandler:"
+ "hasEastLng"
+ "hasNorthLat"
+ "hasSouthLat"
+ "hasWestLng"
+ "initWithCenter:radius:"
+ "initWithTimeInterval:sinceDate:"
+ "isBLEDiscoveryDefaultOnSupported"
+ "isLocationAuthorized is not enabled"
+ "mapsPrecachingExpirationAgeSeconds"
+ "mapsPrecachingLOILookBackTimeSeconds"
+ "maxNumberOfRegionsAllowedForMapsPrecache"
+ "minDwellingDurationForRegionToMapsPrecacheSeconds"
+ "northLat"
+ "now"
+ "radiusOfRegionForMapsPrecachingMeters"
+ "region"
+ "removeSubscriptionWithIdentifier:callbackQueue:completionHandler:"
+ "safetyalertsmaps"
+ "southLat"
+ "timeIntervalSinceDate:"
+ "v16@?0@\"NSArray\"8"
+ "visits"
+ "westLng"
+ "{\"msg%{public}.0s\":\"#System,isBleDiscoveryAllowed\", \"isBLEDiscoveryDefaultOnSupported\":%{private}hhd, \"isEmergencyAlertSwitchEnabled\":%{private}hhd, \"isEnhancedDeliverySwitchEnabled\":%{private}hhd}"
+ "{\"msg%{public}.0s\":\"#aa,onAssetDonwloadCb\", \"fCodebookDownloadAttemptSuccess has value\":%{public}hhd, \"fCodebookDownloadAttemptSuccess\":%{public}d}"
+ "{\"msg%{public}.0s\":\"#asset,#ble,log\", \"isBLERelaySupported\":%{private}hhd, \"advertiseEvaluationIntervalSeconds\":%{private}d, \"discoveryEvaluationIntervalSeconds\":%{private}d, \"advertiseDurationSeconds\":%{private}d, \"minBatteryLevelForBLEActivity\":%{private}d, \"minDeviceDensityCount\":%{private}d, \"bleCBScanRate\":%{private}d, \"CBScanRateBackground\":%{private}d, \"bleCBAdvertiseRate\":%{private}d, \"bleDataVersion\":%{private}d, \"bleAdvertisementTimePrecisionInMSec\":%{private}d, \"isBLEDiscoveryDefaultOnSupported\":%{private}hhd}"
+ "{\"msg%{public}.0s\":\"#asset,#ble,readBleConfigFromFile\", \"isBLERelaySupported\":%{private}hhd, \"advertiseEvaluationIntervalSeconds\":%{private}d, \"discoveryEvaluationIntervalSeconds\":%{private}d, \"advertiseDurationSeconds\":%{private}d, \"minBatteryLevelForBLEActivity\":%{private}d, \"minDeviceDensityCount\":%{private}d, \"bleCBScanRate\":%{private}d, \"bleCBScanRateScreenOff\":%{private}d, \"bleCBAdvertiseRate\":%{private}d, \"bleDataVersion\":%{private}d, \"bleAdvertisementTimePrecisionInMSec\":%{private}d, \"isBLEDiscoveryDefaultOnSupported\":%{private}hhd}"
+ "{\"msg%{public}.0s\":\"#blecore,areAllGatesOpenForAdvertiser\", \"isIgneousCapable\":%{private}hhd, \"isIgneousEnabled\":%{private}hhd, \"isIgneousAllowed\":%{private}hhd, \"isBluetoothEnabled\":%{private}hhd, \"isHWAllowed\":%{private}hhd, \"isLocationAuth\":%{private}hhd, \"isBLERelayFeatureEnabled\":%{private}hhd, \"isPhone\":%{private}hhd}"
+ "{\"msg%{public}.0s\":\"#blecore,areAllGatesOpenForDiscovery\", \"isBluetoothEnabled\":%{private}hhd, \"isHWAllowed\":%{private}hhd, \"isLocationAuth\":%{private}hhd, \"isSwitchEnabled\":%{private}hhd, \"isBLERelayFeatureEnabled\":%{private}hhd, \"isEnhancedDeliverySwitchEnabled\":%{private}hhd}"
+ "{\"msg%{public}.0s\":\"#blecore,canForwardOverBLE,system is not ready for advertisement\"}"
+ "{\"msg%{public}.0s\":\"#blecore,evaluateBLEQDiscoverability\", \"motionState\":%{private}d, \"isSystemReadyForDiscovery\":%{private}hhd}"
+ "{\"msg%{public}.0s\":\"#blecore,onBleCoreAlertCb,ble receive not supported\"}"
+ "{\"msg%{public}.0s\":\"#blecore,onUserSettingsChanged\", \"discoveryAllowed\":%{private}d, \"fIsBleDiscoveryEnabled\":%{private}d}"
+ "{\"msg%{public}.0s\":\"#coreRoutine,Test,fetchLearnedLOI\"}"
+ "{\"msg%{public}.0s\":\"#coreRoutine,fetchLearnedLOI, RTRoutineManager not initialized\"}"
+ "{\"msg%{public}.0s\":\"#coreRoutine,fetchLearnedLOI,called\"}"
+ "{\"msg%{public}.0s\":\"#coreRoutine,fetchLearnedLOI,dateRange\", \"startDate\":%{public, location:escape_only}s, \"endDate\":%{public, location:escape_only}s, \"durationSeconds\":%{public}d}"
+ "{\"msg%{public}.0s\":\"#coreRoutine,fetchLearnedLOI,fetchError\", \"errorDescription\":%{public, location:escape_only}s, \"errorCode\":%{public}d, \"domain\":%{public, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#coreRoutine,fetchLearnedLOI,fetchSuccess\", \"totalLocationsFound\":%{public}d}"
+ "{\"msg%{public}.0s\":\"#coreRoutine,fetchLearnedLOI,invalidCallback\"}"
+ "{\"msg%{public}.0s\":\"#ctsa,onUserSettingsChanged\"}"
+ "{\"msg%{public}.0s\":\"#daemon,onUserSettingsChanged\"}"
+ "{\"msg%{public}.0s\":\"#evtTrk,getIgneousEvents\", \"bleAlertUID\":%{private, location:escape_only}s, \"startTimestamp\":\"%{private}0.1f\", \"endTimestamp\":\"%{private}0.1f\", \"responseCount\":%{private}d}"
+ "{\"msg%{public}.0s\":\"#evtTrk,getIgneousEvents\"}"
+ "{\"msg%{public}.0s\":\"#geometry,isCircleInGeometry\"}"
+ "{\"msg%{public}.0s\":\"#geometry,isLocInGeometryForGivenTime\", \"hLoc.timestamp\":\"%{private}0.3f\", \"startTime\":\"%{private}0.3f\", \"stopTime\":\"%{private}0.3f\"}"
+ "{\"msg%{public}.0s\":\"#geometry,isLocInGeometryForGivenTime\", \"isInsidePolygon\":%{private}hhd}"
+ "{\"msg%{public}.0s\":\"#geometry,isLocInGeometryForGivenTime\", \"startTime\":\"%{private}0.3f\", \"stopTime\":\"%{private}0.3f\", \"historicalLocationsLen\":%{private}d}"
+ "{\"msg%{public}.0s\":\"#geometry,isLocInGeometryForGivenTime,all locations before start timestamp\"}"
+ "{\"msg%{public}.0s\":\"#geometry,isLocInGeometryForGivenTime,last location in polygon\", \"lat\":\"%{sensitive}0.4f\", \"lon\":\"%{sensitive}0.4f\", \"timestamp\":\"%{private}0.2f\", \"isInsidePolygon\":%{private}hhd}"
+ "{\"msg%{public}.0s\":\"#geometry,isLocInGeometryForGivenTime,location in polygon\", \"lat\":\"%{sensitive}0.4f\", \"lon\":\"%{sensitive}0.4f\", \"timestamp\":\"%{private}0.2f\", \"isInsidePolygon\":%{private}hhd}"
+ "{\"msg%{public}.0s\":\"#geometry,isLocInGeometryForGivenTime,looking at last loc before start timestamp\", \"lat\":\"%{sensitive}0.4f\", \"lon\":\"%{sensitive}0.4f\", \"timestamp\":\"%{private}0.2f\", \"isInsidePolygon\":%{private}hhd}"
+ "{\"msg%{public}.0s\":\"#geometry,isLocInGeometryForGivenTime,past start timestamp\"}"
+ "{\"msg%{public}.0s\":\"#mapcache,#warning,shouldCache condition failed\"}"
+ "{\"msg%{public}.0s\":\"#mapcache,addNewRegion,start\", \"identifier\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#mapcache,addNewRegionForCaching,complete\", \"success\":%{private}hhd, \"error\":%{private, location:escape_only}@, \"identifier\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#mapcache,addNewRegionForCaching,regionCreated\"}"
+ "{\"msg%{public}.0s\":\"#mapcache,addRegionsWithGeo\", \"locationCount\":%{private}llu, \"allowedRegions\":%{private}d}"
+ "{\"msg%{public}.0s\":\"#mapcache,addRegionsWithGeo,adding top Dwelled Locations\", \"locationCount\":%{private}llu, \"allowedRegions\":%{private}d}"
+ "{\"msg%{public}.0s\":\"#mapcache,addRegionsWithGeo,addingAllLocations\", \"locationCount\":%{private}llu, \"allowedRegions\":%{private}d}"
+ "{\"msg%{public}.0s\":\"#mapcache,addRegionsWithGeo,current Location added\", \"status\":%{public}hhd}"
+ "{\"msg%{public}.0s\":\"#mapcache,addRegionsWithGeo,entry\", \"learnedLocationCount\":%{private}llu}"
+ "{\"msg%{public}.0s\":\"#mapcache,addRegionsWithGeo,index reached total dwell based LOI\"}"
+ "{\"msg%{public}.0s\":\"#mapcache,addRegionsWithGeo,no LOIs found\"}"
+ "{\"msg%{public}.0s\":\"#mapcache,cachingComplete,\", \"fCacheRequests\":%{private}llu, \"isNearCachedLocation\":%{private}hhd}"
+ "{\"msg%{public}.0s\":\"#mapcache,fetchAndRemoveAllRegions,entry\"}"
+ "{\"msg%{public}.0s\":\"#mapcache,fetchAndRemoveAllRegions,error\", \"error\":%{private, location:escape_only}@, \"errorDescription\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#mapcache,fetchAndRemoveAllRegions,fetchedSubscriptions\", \"fCacheRequests\":%{private}llu, \"isNearCachedLocation\":%{private}hhd}"
+ "{\"msg%{public}.0s\":\"#mapcache,fetchAndRemoveAllRegions,fetchedSubscriptions\", \"subscriptionCount\":%{private}llu}"
+ "{\"msg%{public}.0s\":\"#mapcache,fetchAndRemoveAllRegions,fetchingSubscriptions\", \"identifierCount\":%{private}llu}"
+ "{\"msg%{public}.0s\":\"#mapcache,fetchAndRemoveAllRegions,removal complete\"}"
+ "{\"msg%{public}.0s\":\"#mapcache,fetchLOIAndRefreshMapCache,\", \"result\":%{public}hhd}"
+ "{\"msg%{public}.0s\":\"#mapcache,fetchLOIAndRefreshMapCache,entry\"}"
+ "{\"msg%{public}.0s\":\"#mapcache,fetchLOIAndRefreshMapCache,error\", \"error\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#mapcache,fetchLOIAndRefreshMapCache,fLearnedLocationList\", \"fLearnedLocationList\":%{private}llu}"
+ "{\"msg%{public}.0s\":\"#mapcache,fetchLOIAndRefreshMapCache,receivedLocations\", \"locationCount\":%{private}llu}"
+ "{\"msg%{public}.0s\":\"#mapcache,getCenterLocationFromRegion, invalid region\"}"
+ "{\"msg%{public}.0s\":\"#mapcache,getDwellingThreshold\", \"dwellCriteria\":%{private}d, \"MA dwellCriteria\":%{private}d}"
+ "{\"msg%{public}.0s\":\"#mapcache,getIdentifierListForFetch\", \"wildcard\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#mapcache,getLOIBasedOnDwellingTime,addingMostDwelledLocation\", \"dwellTime\":\"%{private}.1f\"}"
+ "{\"msg%{public}.0s\":\"#mapcache,getLOIBasedOnDwellingTime,entry\", \"learnedLocationCount\":%{private}llu}"
+ "{\"msg%{public}.0s\":\"#mapcache,getLOIBasedOnDwellingTime,evaluatingLocation\", \"dwellTime\":\"%{private}.1f\", \"dwellThreshold\":\"%{private}.1f\", \"identifier\":%{private, location:escape_only}@}"
+ "{\"msg%{public}.0s\":\"#mapcache,getLOIBasedOnDwellingTime,exit\", \"mostDwelledCount\":%{private}llu}"
+ "{\"msg%{public}.0s\":\"#mapcache,getLOIBasedOnDwellingTime,exit\"}"
+ "{\"msg%{public}.0s\":\"#mapcache,getMapsPrecachingLOILookBackTimeSeconds\", \"look back window MA\":%{private}d, \"look back window\":%{private}d}"
+ "{\"msg%{public}.0s\":\"#mapcache,getMaxNumberOfAllowedRegionsCount\", \"maxRegions MA\":%{private}d, \"maxRegions\":%{private}d}"
+ "{\"msg%{public}.0s\":\"#mapcache,getNewIdentifier\", \"index\":%{private}d, \"identifier\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#mapcache,getRegionExpirationAgeSeconds\", \"expirationAge\":%{private}d, \"MA expirationAge\":%{private}d}"
+ "{\"msg%{public}.0s\":\"#mapcache,getRegionRadiusInMeters\", \"regionRadius\":%{private}d, \"radiusOfRegionForMapsPrecachingMeters\":%{private}d}"
+ "{\"msg%{public}.0s\":\"#mapcache,getTriggerPeriod\", \"triggerDuration\":%{private}d, \"MA triggerDuration\":%{private}d}"
+ "{\"msg%{public}.0s\":\"#mapcache,inCachedRegion\", \"dist\":\"%{public}f\"}"
+ "{\"msg%{public}.0s\":\"#mapcache,inCachedRegion\"}"
+ "{\"msg%{public}.0s\":\"#mapcache,inCachedRegion,fail\"}"
+ "{\"msg%{public}.0s\":\"#mapcache,inCachedRegion,success\"}"
+ "{\"msg%{public}.0s\":\"#mapcache,invalid locations\"}"
+ "{\"msg%{public}.0s\":\"#mapcache,invalid subscription manager\"}"
+ "{\"msg%{public}.0s\":\"#mapcache,onLocationAuthorized,authorized\"}"
+ "{\"msg%{public}.0s\":\"#mapcache,onLocationAuthorized,called\", \"isAuthorized\":%{public}hhd}"
+ "{\"msg%{public}.0s\":\"#mapcache,onLocationAuthorized,removalComplete\"}"
+ "{\"msg%{public}.0s\":\"#mapcache,purgeRegionSubscription,complete\", \"success\":%{private}hhd, \"error\":%{private, location:escape_only}@, \"fTotalRequestsToGeoInProgress\":%{private}d}"
+ "{\"msg%{public}.0s\":\"#mapcache,removeRegionsFromGeoCache,entry\", \"subscriptionCount\":%{private}llu}"
+ "{\"msg%{public}.0s\":\"#mapcache,removeRegionsFromGeoCache,exit\", \"reason\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#mapcache,removeRegionsFromGeoCache,removingSubscription\", \"identifier\":%{private, location:escape_only}@, \"fTotalRequestsToGeoInProgress\":%{private}d}"
+ "{\"msg%{public}.0s\":\"#mapcache,shouldCache\", \"lastCacheTime\":\"%{private}0.1f\", \"timeSinceLastCache\":\"%{private}.1f\", \"cacheIntervalSeconds\":%{private}d}"
+ "{\"msg%{public}.0s\":\"#mapcache,shouldCache,error\", \"error\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#mapcache,shouldCache,not enabled exiting\"}"
+ "{\"msg%{public}.0s\":\"#mapcache,shouldCache,notInCoveredRegion,exiting\"}"
+ "{\"msg%{public}.0s\":\"#mapcache,start\", \"triggerInterval\":%{private}d}"
+ "{\"msg%{public}.0s\":\"#mapcache,submitPrecacheStatusToMetrics\", \"triggerType\":%{private}d}"
+ "{\"msg%{public}.0s\":\"#mapcache,trigger don't cache\"}"
+ "{\"msg%{public}.0s\":\"#mapcache,trigger\"}"
+ "{\"msg%{public}.0s\":\"#mapcache,updateCachedRegionsListOnStart,entry\"}"
+ "{\"msg%{public}.0s\":\"#mapcache,updateCachingRegions,entry\"}"
+ "{\"msg%{public}.0s\":\"#mapcache,updateCachingRegions,removal complete\"}"
+ "{\"msg%{public}.0s\":\"#saEventHistory,findAllEventsStrictlyWithin\", \"responseSize\":%{private}d, \"fEventHistorySize\":%{private}d}"
+ "{\"msg%{public}.0s\":\"#safd,downloadRequest,bypass download\"}"
- "%s%s_%llu.png"
- "/tmp/"
- "MPRECACHE_LAST_TILE_NOTIFICATION_TIME"
- "MPRECACHE_NOTIFICATION_PRECACHE_SCHEDULED"
- "_setUseSnapshotService:"
- "cant create geometry"
- "com.apple.safetyalerts.saPrecacheOnChange"
- "drawAtPoint:"
- "efficacy_manifest_v2.txt"
- "ign_map_cache"
- "image"
- "imageWithActions:"
- "initWithOptions:"
- "initWithSize:"
- "radiusM"
- "saPrecaching"
- "setMapType:"
- "setRegion:"
- "setSize:"
- "setTraitCollection:"
- "startWithCompletionHandler:"
- "traitCollectionWithUserInterfaceStyle:"
- "v12@?0i8"
- "v16@?0@\"UIGraphicsImageRendererContext\"8"
- "v24@?0@\"MKMapSnapshot\"8@\"NSError\"16"
- "writeToFile:options:error:"
- "{\"msg%{public}.0s\":\"#asset,#ble,log\", \"isBLERelaySupported\":%{private}hhd, \"advertiseEvaluationIntervalSeconds\":%{private}d, \"discoveryEvaluationIntervalSeconds\":%{private}d, \"advertiseDurationSeconds\":%{private}d, \"minBatteryLevelForBLEActivity\":%{private}d, \"minDeviceDensityCount\":%{private}d, \"bleCBScanRate\":%{private}d, \"CBScanRateBackground\":%{private}d, \"bleCBAdvertiseRate\":%{private}d, \"bleDataVersion\":%{private}d, \"bleAdvertisementTimePrecisionInMSec\":%{private}d}"
- "{\"msg%{public}.0s\":\"#asset,#ble,readBleConfigFromFile\", \"isBLERelaySupported\":%{private}hhd, \"advertiseEvaluationIntervalSeconds\":%{private}d, \"discoveryEvaluationIntervalSeconds\":%{private}d, \"advertiseDurationSeconds\":%{private}d, \"minBatteryLevelForBLEActivity\":%{private}d, \"minDeviceDensityCount\":%{private}d, \"bleCBScanRate\":%{private}d, \"bleCBScanRateScreenOff\":%{private}d, \"bleCBAdvertiseRate\":%{private}d, \"bleDataVersion\":%{private}d, \"bleAdvertisementTimePrecisionInMSec\":%{private}d}"
- "{\"msg%{public}.0s\":\"#blecore,areAllGatesOpen\", \"isIgneousCapable\":%{private}hhd, \"isIgneousEnabled\":%{private}hhd, \"isIgneousAllowed\":%{private}hhd, \"isBluetoothEnabled\":%{private}hhd, \"isHWAllowed\":%{private}hhd, \"isLocationAuth\":%{private}hhd}"
- "{\"msg%{public}.0s\":\"#blecore,evaluateBLEQDiscoverability\", \"motionState\":%{private}d, \"areAllGatesEnabled\":%{private}hhd}"
- "{\"msg%{public}.0s\":\"#igManifestEntry,areaTooSmall\", \"area\":\"%{private}0.1f\"}"
- "{\"msg%{public}.0s\":\"#mapcache,cacheAttempt,indexTooLarge\", \"index\":%{private}llu, \"size\":%{private}llu}"
- "{\"msg%{public}.0s\":\"#mapcache,cacheAttempt,nothingToCache\"}"
- "{\"msg%{public}.0s\":\"#mapcache,cacheCanceled\"}"
- "{\"msg%{public}.0s\":\"#mapcache,cacheInitiated\", \"index\":%{private}llu}"
- "{\"msg%{public}.0s\":\"#mapcache,cachingProgress\", \"lastResult\":%{private}hhd, \"nextIndex\":%{private}llu}"
- "{\"msg%{public}.0s\":\"#mapcache,notificationReceived\", \"timeSinceLastNotification\":\"%{private}.1f\", \"cacheIntervalSeconds\":%{private}d, \"cacheIntervalAllowTime\":\"%{private}.1f\"}"
- "{\"msg%{public}.0s\":\"#mapcache,objects\", \"options\":%{private, location:escape_only}@, \"snapshot\":%{private, location:escape_only}@}"
- "{\"msg%{public}.0s\":\"#mapcache,onFetchVisitsOnly\"}"
- "{\"msg%{public}.0s\":\"#mapcache,onFetchVisitsOnly,addLocation\", \"lat\":\"%{sensitive}.1f\", \"lon\":\"%{sensitive}.1f\"}"
- "{\"msg%{public}.0s\":\"#mapcache,onMapsPrecacheTrigger\"}"
- "{\"msg%{public}.0s\":\"#mapcache,onMapsPrecacheTrigger,not enabled exiting\"}"
- "{\"msg%{public}.0s\":\"#mapcache,onMapsPrecacheTrigger,notInCoveredRegion,exiting\"}"
- "{\"msg%{public}.0s\":\"#mapcache,onVisitsAvailableForPrecache\"}"
- "{\"msg%{public}.0s\":\"#mapcache,onVisitsAvailableForPrecache,historicVisit\", \"lat\":\"%{sensitive}0.6f\", \"lon\":\"%{sensitive}0.6f\", \"radius\":\"%{private}0.2f\"}"
- "{\"msg%{public}.0s\":\"#mapcache,onVisitsAvailableForPrecache,historicVisit\", \"lat\":\"%{sensitive}0.6f\", \"lon\":\"%{sensitive}0.6f\"}"
- "{\"msg%{public}.0s\":\"#mapcache,onVisitsAvailableForPrecache,skipLocation,tooClose\", \"lat\":\"%{sensitive}0.6f\", \"lon\":\"%{sensitive}0.6f\", \"distance\":\"%{sensitive}0.1f\", \"minDistance\":\"%{private}0.1f\"}"
- "{\"msg%{public}.0s\":\"#mapcache,preCacheForRequest\", \"lat\":\"%{sensitive}.2f\", \"lon\":\"%{sensitive}.2f\", \"radius\":\"%{private}.2f\"}"
- "{\"msg%{public}.0s\":\"#mapcache,schedulePreCacheAfterTime\", \"ditheredStartTime\":\"%{public}.2f\", \"maxDitheredStartTime\":\"%{public}.2f\"}"
- "{\"msg%{public}.0s\":\"#mapcache,shouldCache\", \"lastCacheTime\":\"%{private}0.1f\", \"timeSinceLastCache\":\"%{private}.1f\", \"cacheIntervalSeconds\":%{private}d, \"notificationPrecacheScheduled\":%{private}hhd}"
- "{\"msg%{public}.0s\":\"#mapcache,snapshotCallback\", \"snapshot\":%{private, location:escape_only}@, \"error\":%{private, location:escape_only}@}"
- "{\"msg%{public}.0s\":\"#mapcache,snapshotCallback,writeToFile\", \"imageTempPath\":%{private, location:escape_only}@, \"isWritten\":%{private}hhd, \"writeError\":%{private, location:escape_only}@}"
- "{\"msg%{public}.0s\":\"#mapcache,start\", \"interval\":%{private}d}"
- "{\"msg%{public}.0s\":\"#mapcache,start,errorRegisteringForTileNotification\", \"GEOActiveTileGroupChangedNotification\":%{private, location:escape_only}s, \"status\":%{private}hhd}"
- "{\"msg%{public}.0s\":\"#mapcache,start,registeredForTileNotification\", \"GEOActiveTileGroupChangedNotification\":%{private, location:escape_only}s, \"status\":%{private}hhd}"
- "{\"msg%{public}.0s\":\"#mapcache,submitPrecacheStatusToMetrics\", \"isSuccess\":%{private}hhd, \"triggerType\":%{private}d}"
- "{\"msg%{public}.0s\":\"#mapcache,tileChangePrecacheNotScheduleRun\"}"
- "{\"msg%{public}.0s\":\"#mapcache,tileChangePrecacheRun\"}"
- "{\"msg%{public}.0s\":\"#mapcache,tileChangePrecacheScheduleRun\"}"
- "{\"msg%{public}.0s\":\"#saEventHistory,findAllEventsStrictlyWithin\", \"responseSize\":%{private}d}"

```
