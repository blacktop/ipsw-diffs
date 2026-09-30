## CoreRoutine

> `/System/Library/PrivateFrameworks/CoreRoutine.framework/CoreRoutine`

```diff

-990.0.10.0.0
-  __TEXT.__text: 0x42308
-  __TEXT.__auth_stubs: 0x6a0
-  __TEXT.__objc_methlist: 0x516c
-  __TEXT.__const: 0x280
-  __TEXT.__oslogstring: 0x2891
-  __TEXT.__cstring: 0x421c
-  __TEXT.__gcc_except_tab: 0x360
-  __TEXT.__unwind_info: 0x13b8
-  __TEXT.__objc_classname: 0x93a
-  __TEXT.__objc_methname: 0xa057
-  __TEXT.__objc_methtype: 0x1e08
-  __TEXT.__objc_stubs: 0x5760
-  __DATA_CONST.__got: 0x330
-  __DATA_CONST.__const: 0xdd8
-  __DATA_CONST.__objc_classlist: 0x2b8
+1044.0.2.0.0
+  __TEXT.__text: 0x6156c
+  __TEXT.__auth_stubs: 0x670
+  __TEXT.__objc_methlist: 0x7aa4
+  __TEXT.__const: 0x2b0
+  __TEXT.__oslogstring: 0x31c5
+  __TEXT.__cstring: 0x62d6
+  __TEXT.__gcc_except_tab: 0x36c
+  __TEXT.__unwind_info: 0x1d58
+  __TEXT.__objc_classname: 0xf3b
+  __TEXT.__objc_methname: 0xe9f8
+  __TEXT.__objc_methtype: 0x2696
+  __TEXT.__objc_stubs: 0x73a0
+  __DATA_CONST.__got: 0x490
+  __DATA_CONST.__const: 0x11a0
+  __DATA_CONST.__objc_classlist: 0x440
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1e80
+  __DATA_CONST.__objc_selrefs: 0x27f0
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x288
-  __DATA_CONST.__objc_arraydata: 0x90
-  __AUTH_CONST.__auth_got: 0x360
-  __AUTH_CONST.__const: 0x3c0
-  __AUTH_CONST.__cfstring: 0x3e80
-  __AUTH_CONST.__objc_const: 0x8d08
+  __DATA_CONST.__objc_superrefs: 0x410
+  __DATA_CONST.__objc_arraydata: 0x98
+  __AUTH_CONST.__auth_got: 0x348
+  __AUTH_CONST.__const: 0x3a0
+  __AUTH_CONST.__cfstring: 0x5820
+  __AUTH_CONST.__objc_const: 0xdd08
   __AUTH_CONST.__objc_intobj: 0xa8
+  __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__objc_dictobj: 0x50
-  __AUTH.__objc_data: 0x5f0
-  __DATA.__objc_ivar: 0x4fc
-  __DATA.__data: 0x2d8
-  __DATA_DIRTY.__objc_ivar: 0xa8
-  __DATA_DIRTY.__objc_data: 0x1540
+  __AUTH.__objc_data: 0x13b0
+  __DATA.__objc_ivar: 0x7dc
+  __DATA.__data: 0x308
+  __DATA_DIRTY.__objc_ivar: 0x124
+  __DATA_DIRTY.__objc_data: 0x16d0
   __DATA_DIRTY.__data: 0x30
-  __DATA_DIRTY.__bss: 0x40
+  __DATA_DIRTY.__bss: 0x50
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreLocation.framework/CoreLocation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Security.framework/Security
+  - /System/Library/Frameworks/_LocationEssentials.framework/_LocationEssentials
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/GeoServices.framework/GeoServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 6709BEA8-6E78-3BAB-A370-6608921051FC
-  Functions: 1813
-  Symbols:   5785
-  CStrings:  3153
+  UUID: 0E58356B-FAF1-348C-88A6-B38E05301059
+  Functions: 2751
+  Symbols:   8593
+  CStrings:  4363
 
Symbols:
+ +[NSDate(RTExtensions) dateFormatterForLogging]
+ +[RTAuthorizedLocationConfirmationStatusEnumerationContext supportsSecureCoding]
+ +[RTAuthorizedLocationDiagnosticStatus supportsSecureCoding]
+ +[RTAuthorizedLocationZDRLocationsEnumerationContext supportsSecureCoding]
+ +[RTBluePOIMetadata supportsSecureCoding]
+ +[RTBluePOITile supportsSecureCoding]
+ +[RTBluePOITileDownloadResult supportsSecureCoding]
+ +[RTGeoRoadDataEnumerationContext supportsSecureCoding]
+ +[RTGeoRoadDataEnumerationOptions supportsSecureCoding]
+ +[RTLearnedRoute supportsSecureCoding]
+ +[RTLearnedRouteFetchOptions _isValidRouteODLocation:routeDestinationLocation:routeFetchType:]
+ +[RTLearnedRouteFetchOptions isValidRouteFetchType:]
+ +[RTLearnedRouteFetchOptions supportsSecureCoding]
+ +[RTLearnedRouteLocation supportsSecureCoding]
+ +[RTLearnedRouteMetrics supportsSecureCoding]
+ +[RTLearnedRouteTravelMode deriveConfidenceFromRouteMetric:]
+ +[RTLearnedRouteTravelMode supportsSecureCoding]
+ +[RTLocalBluePOIResult supportsSecureCoding]
+ +[RTLocationsFromCoreLocationFetchOptions supportsSecureCoding]
+ +[RTPointOfInterest supportsSecureCoding]
+ +[RTPredictedContext maskForSources:]
+ +[RTPredictedContext supportsSecureCoding]
+ +[RTPredictedContextAnalytics supportsSecureCoding]
+ +[RTPredictedContextAnalyticsRolledLOIResult supportsSecureCoding]
+ +[RTPredictedContextDate supportsSecureCoding]
+ +[RTPredictedContextDateInterval supportsSecureCoding]
+ +[RTPredictedContextLocation supportsSecureCoding]
+ +[RTPredictedContextOptions supportsSecureCoding]
+ +[RTPredictedContextRequest supportsSecureCoding]
+ +[RTPredictedContextResult contextTypeForContext:]
+ +[RTPredictedContextResult contextTypeMaskForContext:]
+ +[RTPredictedContextResult supportsSecureCoding]
+ +[RTPredictedContextSequence supportsSecureCoding]
+ +[RTPredictedContextTransition supportsSecureCoding]
+ +[RTPredictedContextTransport supportsSecureCoding]
+ +[RTPredictedContextWorkout supportsSecureCoding]
+ +[RTSourceHealthKitWorkout supportsSecureCoding]
+ +[RTSourceHomeKit supportsSecureCoding]
+ +[RTSourceParkedCar supportsSecureCoding]
+ +[RTSourcePropagatedLocation supportsSecureCoding]
+ +[RTStoredUserCurationFetchOptions supportsSecureCoding]
+ +[RTTripClusterEnumerationContext supportsSecureCoding]
+ +[RTTripClusterEnumerationOptions supportsSecureCoding]
+ +[RTTripClusterMetadata _isValidClusterOrder:]
+ +[RTTripClusterMetadata supportsSecureCoding]
+ +[RTTripClusterMetadataFetchOptions supportsSecureCoding]
+ +[RTTripClusterRecencyEnumerationContext supportsSecureCoding]
+ +[RTTripClusterRecencyEnumerationOptions supportsSecureCoding]
+ +[RTTripClusterRoadTransitionsEnumerationContext supportsSecureCoding]
+ +[RTTripClusterRoadTransitionsEnumerationOptions supportsSecureCoding]
+ +[RTTripClusterRouteEnumerationContext supportsSecureCoding]
+ +[RTTripClusterRouteEnumerationOptions supportsSecureCoding]
+ +[RTTripClusterScheduleEnumerationContext supportsSecureCoding]
+ +[RTTripClusterScheduleEnumerationOptions supportsSecureCoding]
+ +[RTUserCuration supportsSecureCoding]
+ -[NSDate(RTExtensions) startOfDayAfterAddingUnit:value:]
+ -[NSUUID(RTExtensions) dataRepresentation]
+ -[RTAuthorizedLocationConfirmationStatusEnumerationContext .cxx_destruct]
+ -[RTAuthorizedLocationConfirmationStatusEnumerationContext copyWithZone:]
+ -[RTAuthorizedLocationConfirmationStatusEnumerationContext description]
+ -[RTAuthorizedLocationConfirmationStatusEnumerationContext encodeWithCoder:]
+ -[RTAuthorizedLocationConfirmationStatusEnumerationContext hash]
+ -[RTAuthorizedLocationConfirmationStatusEnumerationContext initWithCoder:]
+ -[RTAuthorizedLocationConfirmationStatusEnumerationContext initWithEnumerationOptions:]
+ -[RTAuthorizedLocationConfirmationStatusEnumerationContext initWithEnumerationOptions:offset:]
+ -[RTAuthorizedLocationConfirmationStatusEnumerationContext init]
+ -[RTAuthorizedLocationConfirmationStatusEnumerationContext isEqual:]
+ -[RTAuthorizedLocationConfirmationStatusEnumerationContext isEqualToContext:]
+ -[RTAuthorizedLocationConfirmationStatusEnumerationContext offset]
+ -[RTAuthorizedLocationConfirmationStatusEnumerationContext options]
+ -[RTAuthorizedLocationConfirmationStatusEnumerationOptions .cxx_destruct]
+ -[RTAuthorizedLocationConfirmationStatusEnumerationOptions batchSize]
+ -[RTAuthorizedLocationConfirmationStatusEnumerationOptions copyWithZone:]
+ -[RTAuthorizedLocationConfirmationStatusEnumerationOptions encodeWithCoder:]
+ -[RTAuthorizedLocationConfirmationStatusEnumerationOptions endDate]
+ -[RTAuthorizedLocationConfirmationStatusEnumerationOptions initWithCoder:]
+ -[RTAuthorizedLocationConfirmationStatusEnumerationOptions initWithOptions:startDate:endDate:]
+ -[RTAuthorizedLocationConfirmationStatusEnumerationOptions init]
+ -[RTAuthorizedLocationConfirmationStatusEnumerationOptions setBatchSize:]
+ -[RTAuthorizedLocationConfirmationStatusEnumerationOptions setEndDate:]
+ -[RTAuthorizedLocationConfirmationStatusEnumerationOptions setStartDate:]
+ -[RTAuthorizedLocationConfirmationStatusEnumerationOptions startDate]
+ -[RTAuthorizedLocationDiagnosticStatus .cxx_destruct]
+ -[RTAuthorizedLocationDiagnosticStatus copyWithZone:]
+ -[RTAuthorizedLocationDiagnosticStatus encodeWithCoder:]
+ -[RTAuthorizedLocationDiagnosticStatus fullConfirmationList]
+ -[RTAuthorizedLocationDiagnosticStatus initWithCoder:]
+ -[RTAuthorizedLocationDiagnosticStatus initWithStatus:zdrConfirmationList:]
+ -[RTAuthorizedLocationDiagnosticStatus setFullConfirmationList:]
+ -[RTAuthorizedLocationDiagnosticStatus setZdrConfirmationList:]
+ -[RTAuthorizedLocationDiagnosticStatus zdrConfirmationList]
+ -[RTAuthorizedLocationZDRLocationsEnumerationContext .cxx_destruct]
+ -[RTAuthorizedLocationZDRLocationsEnumerationContext copyWithZone:]
+ -[RTAuthorizedLocationZDRLocationsEnumerationContext description]
+ -[RTAuthorizedLocationZDRLocationsEnumerationContext encodeWithCoder:]
+ -[RTAuthorizedLocationZDRLocationsEnumerationContext hash]
+ -[RTAuthorizedLocationZDRLocationsEnumerationContext initWithCoder:]
+ -[RTAuthorizedLocationZDRLocationsEnumerationContext initWithEnumerationOptions:]
+ -[RTAuthorizedLocationZDRLocationsEnumerationContext initWithEnumerationOptions:offset:]
+ -[RTAuthorizedLocationZDRLocationsEnumerationContext init]
+ -[RTAuthorizedLocationZDRLocationsEnumerationContext isEqual:]
+ -[RTAuthorizedLocationZDRLocationsEnumerationContext isEqualToContext:]
+ -[RTAuthorizedLocationZDRLocationsEnumerationContext offset]
+ -[RTAuthorizedLocationZDRLocationsEnumerationContext options]
+ -[RTAuthorizedLocationZDRLocationsEnumerationOptions .cxx_destruct]
+ -[RTAuthorizedLocationZDRLocationsEnumerationOptions batchSize]
+ -[RTAuthorizedLocationZDRLocationsEnumerationOptions copyWithZone:]
+ -[RTAuthorizedLocationZDRLocationsEnumerationOptions encodeWithCoder:]
+ -[RTAuthorizedLocationZDRLocationsEnumerationOptions endDate]
+ -[RTAuthorizedLocationZDRLocationsEnumerationOptions initWithCoder:]
+ -[RTAuthorizedLocationZDRLocationsEnumerationOptions initWithOptions:startDate:endDate:maximumNumberOfItems:]
+ -[RTAuthorizedLocationZDRLocationsEnumerationOptions init]
+ -[RTAuthorizedLocationZDRLocationsEnumerationOptions maximumNumberOfItems]
+ -[RTAuthorizedLocationZDRLocationsEnumerationOptions setBatchSize:]
+ -[RTAuthorizedLocationZDRLocationsEnumerationOptions setEndDate:]
+ -[RTAuthorizedLocationZDRLocationsEnumerationOptions setStartDate:]
+ -[RTAuthorizedLocationZDRLocationsEnumerationOptions startDate]
+ -[RTBluePOIMetadata .cxx_destruct]
+ -[RTBluePOIMetadata categoryDenyList]
+ -[RTBluePOIMetadata copyWithZone:]
+ -[RTBluePOIMetadata description]
+ -[RTBluePOIMetadata encodeWithCoder:]
+ -[RTBluePOIMetadata geoCacheInfo]
+ -[RTBluePOIMetadata hash]
+ -[RTBluePOIMetadata identifier]
+ -[RTBluePOIMetadata initWithCoder:]
+ -[RTBluePOIMetadata initWithIdentifier:categoryDenyList:geoCacheInfo:modelCalibrationParameters:]
+ -[RTBluePOIMetadata init]
+ -[RTBluePOIMetadata isEqual:]
+ -[RTBluePOIMetadata modelCalibrationParameters]
+ -[RTBluePOITile .cxx_destruct]
+ -[RTBluePOITile apToModelMapping]
+ -[RTBluePOITile copyWithZone:]
+ -[RTBluePOITile date]
+ -[RTBluePOITile description]
+ -[RTBluePOITile downloadKey]
+ -[RTBluePOITile encodeWithCoder:]
+ -[RTBluePOITile geoCacheInfo]
+ -[RTBluePOITile geoTileKey]
+ -[RTBluePOITile hash]
+ -[RTBluePOITile identifier]
+ -[RTBluePOITile initWithCoder:]
+ -[RTBluePOITile initWithIdentifier:apToModelMapping:date:downloadKey:geoCacheInfo:geoTileKey:modelCalibrationParameters:modelURLs:pointsOfInterest:singlePOIMuid:size:]
+ -[RTBluePOITile init]
+ -[RTBluePOITile isEqual:]
+ -[RTBluePOITile modelCalibrationParameters]
+ -[RTBluePOITile modelURLs]
+ -[RTBluePOITile pointsOfInterest]
+ -[RTBluePOITile singlePOIMuid]
+ -[RTBluePOITile size]
+ -[RTBluePOITileDownloadResult .cxx_destruct]
+ -[RTBluePOITileDownloadResult copyWithZone:]
+ -[RTBluePOITileDownloadResult description]
+ -[RTBluePOITileDownloadResult downloadError]
+ -[RTBluePOITileDownloadResult downloadKey]
+ -[RTBluePOITileDownloadResult encodeWithCoder:]
+ -[RTBluePOITileDownloadResult hash]
+ -[RTBluePOITileDownloadResult initWithCoder:]
+ -[RTBluePOITileDownloadResult initWithDownloadKey:tileURL:tileCacheInfo:downloadError:]
+ -[RTBluePOITileDownloadResult init]
+ -[RTBluePOITileDownloadResult isEqual:]
+ -[RTBluePOITileDownloadResult tileCacheInfo]
+ -[RTBluePOITileDownloadResult tileURL]
+ -[RTGeoRoadDataEnumerationContext .cxx_destruct]
+ -[RTGeoRoadDataEnumerationContext copyWithZone:]
+ -[RTGeoRoadDataEnumerationContext description]
+ -[RTGeoRoadDataEnumerationContext encodeWithCoder:]
+ -[RTGeoRoadDataEnumerationContext hash]
+ -[RTGeoRoadDataEnumerationContext initWithCoder:]
+ -[RTGeoRoadDataEnumerationContext initWithEnumerationOptions:]
+ -[RTGeoRoadDataEnumerationContext initWithEnumerationOptions:offset:]
+ -[RTGeoRoadDataEnumerationContext init]
+ -[RTGeoRoadDataEnumerationContext isEqual:]
+ -[RTGeoRoadDataEnumerationContext isEqualToContext:]
+ -[RTGeoRoadDataEnumerationContext offset]
+ -[RTGeoRoadDataEnumerationContext options]
+ -[RTGeoRoadDataEnumerationOptions batchSize]
+ -[RTGeoRoadDataEnumerationOptions copyWithZone:]
+ -[RTGeoRoadDataEnumerationOptions encodeWithCoder:]
+ -[RTGeoRoadDataEnumerationOptions enumeratedType]
+ -[RTGeoRoadDataEnumerationOptions hash]
+ -[RTGeoRoadDataEnumerationOptions initWithCoder:]
+ -[RTGeoRoadDataEnumerationOptions initWithbatchSize:]
+ -[RTGeoRoadDataEnumerationOptions init]
+ -[RTGeoRoadDataEnumerationOptions isEqual:]
+ -[RTGeoRoadDataEnumerationOptions processingBlock]
+ -[RTGeoRoadDataEnumerationOptions setBatchSize:]
+ -[RTLearnedRoute .cxx_destruct]
+ -[RTLearnedRoute copyWithZone:]
+ -[RTLearnedRoute description]
+ -[RTLearnedRoute encodeWithCoder:]
+ -[RTLearnedRoute initWithCoder:]
+ -[RTLearnedRoute initWithLearnedRouteId:routeStartLocation:routeEndLocation:travelTimeEntireRouteSec:travelDistanceEntireRouteMeter:travelModeRoutes:routeStartLocationWithReferenceFrame:routeEndLocationWithReferenceFrame:]
+ -[RTLearnedRoute isEqual:]
+ -[RTLearnedRoute learnedRouteEndLocationWithReferenceFrame]
+ -[RTLearnedRoute learnedRouteEndLocation]
+ -[RTLearnedRoute learnedRouteIdentifier]
+ -[RTLearnedRoute learnedRouteStartLocationWithReferenceFrame]
+ -[RTLearnedRoute learnedRouteStartLocation]
+ -[RTLearnedRoute likelihood]
+ -[RTLearnedRoute setLikelihood:]
+ -[RTLearnedRoute travelModeRoutes]
+ -[RTLearnedRoute travelTimeEstimateForEntireRouteInSeconds]
+ -[RTLearnedRoute travelledDistanceEstimateForEntireRouteInMeters]
+ -[RTLearnedRouteFetchOptions .cxx_destruct]
+ -[RTLearnedRouteFetchOptions bundleIdentifier]
+ -[RTLearnedRouteFetchOptions bundlePath]
+ -[RTLearnedRouteFetchOptions copyWithZone:]
+ -[RTLearnedRouteFetchOptions description]
+ -[RTLearnedRouteFetchOptions destinationVisit]
+ -[RTLearnedRouteFetchOptions encodeWithCoder:]
+ -[RTLearnedRouteFetchOptions fetchAllRouteLocations]
+ -[RTLearnedRouteFetchOptions initWithBundleIdentifier:bundlePath:routeOriginLocation:routeDestinationLocation:routeDate:routeFetchType:fetchAllRouteLocations:routeOriginType:]
+ -[RTLearnedRouteFetchOptions initWithBundleIdentifier:routeOriginLocation:routeDestinationLocation:routeDate:routeFetchType:fetchAllRouteLocations:routeOriginType:]
+ -[RTLearnedRouteFetchOptions initWithBundlePath:routeOriginLocation:routeDestinationLocation:routeDate:routeFetchType:fetchAllRouteLocations:routeOriginType:]
+ -[RTLearnedRouteFetchOptions initWithCoder:]
+ -[RTLearnedRouteFetchOptions isEqual:]
+ -[RTLearnedRouteFetchOptions isEqualToFetchOptions:]
+ -[RTLearnedRouteFetchOptions originVisit]
+ -[RTLearnedRouteFetchOptions routeDate]
+ -[RTLearnedRouteFetchOptions routeFetchType]
+ -[RTLearnedRouteFetchOptions routeOriginType]
+ -[RTLearnedRouteFetchOptions setBundleIdentifier:]
+ -[RTLearnedRouteFetchOptions setBundlePath:]
+ -[RTLearnedRouteFetchOptions setDestinationVisit:]
+ -[RTLearnedRouteFetchOptions setOriginVisit:]
+ -[RTLearnedRouteLocation copyWithZone:]
+ -[RTLearnedRouteLocation course]
+ -[RTLearnedRouteLocation description]
+ -[RTLearnedRouteLocation encodeWithCoder:]
+ -[RTLearnedRouteLocation followedByUTurn]
+ -[RTLearnedRouteLocation initWithCoder:]
+ -[RTLearnedRouteLocation initWithLatitude:longitude:course:followedByUTurn:locationReferenceFrame:]
+ -[RTLearnedRouteLocation isEqual:]
+ -[RTLearnedRouteLocation latitude]
+ -[RTLearnedRouteLocation locationReferenceFrame]
+ -[RTLearnedRouteLocation longitude]
+ -[RTLearnedRouteMetrics .cxx_destruct]
+ -[RTLearnedRouteMetrics allRoutesCountForThisODPair]
+ -[RTLearnedRouteMetrics allTraversalCountBetweenThisODPair]
+ -[RTLearnedRouteMetrics copyWithZone:]
+ -[RTLearnedRouteMetrics description]
+ -[RTLearnedRouteMetrics encodeWithCoder:]
+ -[RTLearnedRouteMetrics initWithAllRoutesCountForThisODPair:allTraversalCountBetweenThisODPair:routeTraversalCount:routeTraversalCountOnTravelDayOfWeek:routeTravelCountOnTravelDayOfWeekHourOfDay:lastTravelledDate:]
+ -[RTLearnedRouteMetrics initWithCoder:]
+ -[RTLearnedRouteMetrics isEqual:]
+ -[RTLearnedRouteMetrics lastTravelledDate]
+ -[RTLearnedRouteMetrics routeTravelCountOnTravelDayOfWeekHourOfDay]
+ -[RTLearnedRouteMetrics routeTraversalCountOnTravelDayOfWeek]
+ -[RTLearnedRouteMetrics routeTraversalCount]
+ -[RTLearnedRouteTravelMode .cxx_destruct]
+ -[RTLearnedRouteTravelMode copyWithZone:]
+ -[RTLearnedRouteTravelMode description]
+ -[RTLearnedRouteTravelMode encodeWithCoder:]
+ -[RTLearnedRouteTravelMode initWithCoder:]
+ -[RTLearnedRouteTravelMode initWithRouteTravelMode:maxTravelTimeEstimateInSeconds:minTravelTimeEstimateInSeconds:meanTravelTimeEstimateInSeconds:maxTravelledDistanceEstimateInMeters:minTravelledDistanceEstimateInMeters:meanTravelledDistanceEstimateInMeters:routeLocations:learnedRouteLocations:learnedRouteMetrics:]
+ -[RTLearnedRouteTravelMode isEqual:]
+ -[RTLearnedRouteTravelMode learnedRouteLocations]
+ -[RTLearnedRouteTravelMode learnedRouteMetrics]
+ -[RTLearnedRouteTravelMode maxTravelTimeEstimateInSeconds]
+ -[RTLearnedRouteTravelMode maxTravelledDistanceEstimateInMeters]
+ -[RTLearnedRouteTravelMode meanTravelTimeEstimateInSeconds]
+ -[RTLearnedRouteTravelMode meanTravelledDistanceEstimateInMeters]
+ -[RTLearnedRouteTravelMode minTravelTimeEstimateInSeconds]
+ -[RTLearnedRouteTravelMode minTravelledDistanceEstimateInMeters]
+ -[RTLearnedRouteTravelMode routeLocations]
+ -[RTLearnedRouteTravelMode routeTravelMode]
+ -[RTLocalBluePOIResult .cxx_destruct]
+ -[RTLocalBluePOIResult aoiConfidences]
+ -[RTLocalBluePOIResult copyWithZone:]
+ -[RTLocalBluePOIResult description]
+ -[RTLocalBluePOIResult encodeWithCoder:]
+ -[RTLocalBluePOIResult hash]
+ -[RTLocalBluePOIResult initWithCoder:]
+ -[RTLocalBluePOIResult initWithPOIConfidences:aoiConfidences:referenceLocation:queryTime:]
+ -[RTLocalBluePOIResult init]
+ -[RTLocalBluePOIResult isEqual:]
+ -[RTLocalBluePOIResult mostConfidentAOI]
+ -[RTLocalBluePOIResult mostConfidentPOI]
+ -[RTLocalBluePOIResult poiConfidences]
+ -[RTLocalBluePOIResult queryTime]
+ -[RTLocalBluePOIResult referenceLocation]
+ -[RTLocalBluePOIResult setMostConfidentAOI:]
+ -[RTLocalBluePOIResult setMostConfidentPOI:]
+ -[RTLocationsFromCoreLocationFetchOptions .cxx_destruct]
+ -[RTLocationsFromCoreLocationFetchOptions copyWithZone:]
+ -[RTLocationsFromCoreLocationFetchOptions date]
+ -[RTLocationsFromCoreLocationFetchOptions description]
+ -[RTLocationsFromCoreLocationFetchOptions encodeWithCoder:]
+ -[RTLocationsFromCoreLocationFetchOptions initWithCoder:]
+ -[RTLocationsFromCoreLocationFetchOptions initWithDate:]
+ -[RTLocationsFromCoreLocationFetchOptions initWithDate:machContinuousTimeSec:numberOfSeconds:]
+ -[RTLocationsFromCoreLocationFetchOptions initWithMachContinuousTimeSec:]
+ -[RTLocationsFromCoreLocationFetchOptions initWithNumberOfSeconds:]
+ -[RTLocationsFromCoreLocationFetchOptions isEqual:]
+ -[RTLocationsFromCoreLocationFetchOptions isEqualToFetchOptions:]
+ -[RTLocationsFromCoreLocationFetchOptions machContinuousTimeSec]
+ -[RTLocationsFromCoreLocationFetchOptions numberOfSeconds]
+ -[RTMapItem categoryMUID]
+ -[RTMapItem geoMapItemIdentifier]
+ -[RTMapItem initWithIdentifier:name:category:categoryMUID:address:location:source:mapItemPlaceType:muid:resultProviderID:geoMapItemHandle:creationDate:expirationDate:extendedAttributes:displayLanguage:disputed:]
+ -[RTPointOfInterest .cxx_destruct]
+ -[RTPointOfInterest applePaySupport]
+ -[RTPointOfInterest copyWithZone:]
+ -[RTPointOfInterest description]
+ -[RTPointOfInterest encodeWithCoder:]
+ -[RTPointOfInterest filtered]
+ -[RTPointOfInterest fullyCoversTile]
+ -[RTPointOfInterest hash]
+ -[RTPointOfInterest identifier]
+ -[RTPointOfInterest initWithCoder:]
+ -[RTPointOfInterest initWithIdentifier:applePaySupport:filtered:fullyCoversTile:location:muid:polygon:]
+ -[RTPointOfInterest init]
+ -[RTPointOfInterest isEqual:]
+ -[RTPointOfInterest location]
+ -[RTPointOfInterest muid]
+ -[RTPointOfInterest polygon]
+ -[RTPredictedContext .cxx_destruct]
+ -[RTPredictedContext copyWithZone:]
+ -[RTPredictedContext dateInterval]
+ -[RTPredictedContext description]
+ -[RTPredictedContext encodeWithCoder:]
+ -[RTPredictedContext initWithCoder:]
+ -[RTPredictedContext initWithPredictedContextDateInterval:predictionSources:probability:]
+ -[RTPredictedContext isEqual:]
+ -[RTPredictedContext predictionSources]
+ -[RTPredictedContext probability]
+ -[RTPredictedContextAnalytics .cxx_destruct]
+ -[RTPredictedContextAnalytics copyWithZone:]
+ -[RTPredictedContextAnalytics description]
+ -[RTPredictedContextAnalytics encodeWithCoder:]
+ -[RTPredictedContextAnalytics initWithCoder:]
+ -[RTPredictedContextAnalytics initWithRolledLOIResult:]
+ -[RTPredictedContextAnalytics isEqual:]
+ -[RTPredictedContextAnalytics rolledLOIResult]
+ -[RTPredictedContextAnalyticsRolledLOIResult .cxx_destruct]
+ -[RTPredictedContextAnalyticsRolledLOIResult copyWithZone:]
+ -[RTPredictedContextAnalyticsRolledLOIResult description]
+ -[RTPredictedContextAnalyticsRolledLOIResult encodeWithCoder:]
+ -[RTPredictedContextAnalyticsRolledLOIResult identifier]
+ -[RTPredictedContextAnalyticsRolledLOIResult initWithCoder:]
+ -[RTPredictedContextAnalyticsRolledLOIResult initWithIdentifier:loiIsMissingFromCurrentVisitHistory:isHome:isWork:]
+ -[RTPredictedContextAnalyticsRolledLOIResult isEqual:]
+ -[RTPredictedContextAnalyticsRolledLOIResult isHome]
+ -[RTPredictedContextAnalyticsRolledLOIResult isWork]
+ -[RTPredictedContextAnalyticsRolledLOIResult loiIsMissingFromCurrentVisitHistory]
+ -[RTPredictedContextDate .cxx_destruct]
+ -[RTPredictedContextDate confidenceInterval]
+ -[RTPredictedContextDate copyWithZone:]
+ -[RTPredictedContextDate date]
+ -[RTPredictedContextDate description]
+ -[RTPredictedContextDate encodeWithCoder:]
+ -[RTPredictedContextDate initWithCoder:]
+ -[RTPredictedContextDate initWithDate:confidenceInterval:]
+ -[RTPredictedContextDate isEqual:]
+ -[RTPredictedContextDateInterval .cxx_destruct]
+ -[RTPredictedContextDateInterval copyWithZone:]
+ -[RTPredictedContextDateInterval description]
+ -[RTPredictedContextDateInterval encodeWithCoder:]
+ -[RTPredictedContextDateInterval endDate]
+ -[RTPredictedContextDateInterval initWithCoder:]
+ -[RTPredictedContextDateInterval initWithStartDate:endDate:]
+ -[RTPredictedContextDateInterval isEqual:]
+ -[RTPredictedContextDateInterval startDate]
+ -[RTPredictedContextLocation .cxx_destruct]
+ -[RTPredictedContextLocation copyWithZone:]
+ -[RTPredictedContextLocation description]
+ -[RTPredictedContextLocation encodeWithCoder:]
+ -[RTPredictedContextLocation initWithCoder:]
+ -[RTPredictedContextLocation initWithLocationOfInterest:dateInterval:predictionSources:probability:]
+ -[RTPredictedContextLocation isEqual:]
+ -[RTPredictedContextLocation locationOfInterest]
+ -[RTPredictedContextOptions .cxx_destruct]
+ -[RTPredictedContextOptions copyWithZone:]
+ -[RTPredictedContextOptions description]
+ -[RTPredictedContextOptions encodeWithCoder:]
+ -[RTPredictedContextOptions filterContextTypeMask]
+ -[RTPredictedContextOptions filterLocations]
+ -[RTPredictedContextOptions forecastWindowDateInterval]
+ -[RTPredictedContextOptions forecastWindowTimeInterval]
+ -[RTPredictedContextOptions initWithCoder:]
+ -[RTPredictedContextOptions initWithForecastWindowDateInterval:filterContextTypeMask:filterLocations:resultSortDescriptors:]
+ -[RTPredictedContextOptions initWithForecastWindowDateInterval:filterContextTypeMask:filterLocations:resultSortStartDateAscending:resultSortProbabilityAscending:]
+ -[RTPredictedContextOptions initWithForecastWindowDateInterval:forecastWindowTimeInterval:filterContextTypeMask:filterLocations:resultSortDescriptors:]
+ -[RTPredictedContextOptions initWithForecastWindowTimeInterval:filterContextTypeMask:filterLocations:resultSortDescriptors:]
+ -[RTPredictedContextOptions init]
+ -[RTPredictedContextOptions isEqual:]
+ -[RTPredictedContextOptions resultSortDescriptors]
+ -[RTPredictedContextOptions resultSortProbabilityAscending]
+ -[RTPredictedContextOptions resultSortStartDateAscending]
+ -[RTPredictedContextRequest .cxx_destruct]
+ -[RTPredictedContextRequest clientCount]
+ -[RTPredictedContextRequest copyWithZone:]
+ -[RTPredictedContextRequest description]
+ -[RTPredictedContextRequest encodeWithCoder:]
+ -[RTPredictedContextRequest identifier]
+ -[RTPredictedContextRequest inferenceTriggerReasonToString]
+ -[RTPredictedContextRequest inferenceTriggerReason]
+ -[RTPredictedContextRequest initWithCoder:]
+ -[RTPredictedContextRequest initWithIdentifier:predictedContextResult:requestStartDate:requestEndDate:inferenceTriggerReason:memoryFootprintStart:memoryFootprintEnd:clientCount:]
+ -[RTPredictedContextRequest isEqual:]
+ -[RTPredictedContextRequest memoryFootprintEnd]
+ -[RTPredictedContextRequest memoryFootprintStart]
+ -[RTPredictedContextRequest predictedContextResult]
+ -[RTPredictedContextRequest requestEndDate]
+ -[RTPredictedContextRequest requestStartDate]
+ -[RTPredictedContextResult .cxx_destruct]
+ -[RTPredictedContextResult analytics]
+ -[RTPredictedContextResult copyWithZone:]
+ -[RTPredictedContextResult currentPredictedContextsWithType:]
+ -[RTPredictedContextResult dateIntervalFromStart:end:]
+ -[RTPredictedContextResult description]
+ -[RTPredictedContextResult encodeWithCoder:]
+ -[RTPredictedContextResult generateSequencesFromDate:toDate:]
+ -[RTPredictedContextResult initWithCoder:]
+ -[RTPredictedContextResult initWithPredictedContexts:analytics:]
+ -[RTPredictedContextResult isEqual:]
+ -[RTPredictedContextResult nextStepPredictedContexts:]
+ -[RTPredictedContextResult nextStepPredictedContextsWithFilterMask:]
+ -[RTPredictedContextResult predictedContextsWithType:afterContext:]
+ -[RTPredictedContextResult predictedContexts]
+ -[RTPredictedContextResult predictedSequencesAfterContext:]
+ -[RTPredictedContextResult unknownPredictedContextFromStart:end:]
+ -[RTPredictedContextSequence .cxx_destruct]
+ -[RTPredictedContextSequence contexts]
+ -[RTPredictedContextSequence copyWithZone:]
+ -[RTPredictedContextSequence dateInterval]
+ -[RTPredictedContextSequence description]
+ -[RTPredictedContextSequence encodeWithCoder:]
+ -[RTPredictedContextSequence initWithCoder:]
+ -[RTPredictedContextSequence initWithProbability:dateInterval:predictedContexts:]
+ -[RTPredictedContextSequence isEqual:]
+ -[RTPredictedContextSequence predictedContexts]
+ -[RTPredictedContextSequence probability]
+ -[RTPredictedContextTransition .cxx_destruct]
+ -[RTPredictedContextTransition copyWithZone:]
+ -[RTPredictedContextTransition description]
+ -[RTPredictedContextTransition encodeWithCoder:]
+ -[RTPredictedContextTransition initWithCoder:]
+ -[RTPredictedContextTransition initWithPredictedContextTransports:predictedContextDateInterval:predictionSources:probability:]
+ -[RTPredictedContextTransition isEqual:]
+ -[RTPredictedContextTransition predictedContextTransports]
+ -[RTPredictedContextTransport copyWithZone:]
+ -[RTPredictedContextTransport description]
+ -[RTPredictedContextTransport encodeWithCoder:]
+ -[RTPredictedContextTransport initWithCoder:]
+ -[RTPredictedContextTransport initWithTransportMode:probability:]
+ -[RTPredictedContextTransport isEqual:]
+ -[RTPredictedContextTransport probability]
+ -[RTPredictedContextTransport transportMode]
+ -[RTPredictedContextWorkout .cxx_destruct]
+ -[RTPredictedContextWorkout copyWithZone:]
+ -[RTPredictedContextWorkout description]
+ -[RTPredictedContextWorkout encodeWithCoder:]
+ -[RTPredictedContextWorkout initWithCoder:]
+ -[RTPredictedContextWorkout initWithDateInterval:predictionSources:probability:sourceBundleIdentifier:workoutActivityType:]
+ -[RTPredictedContextWorkout isEqual:]
+ -[RTPredictedContextWorkout sourceBundleIdentifier]
+ -[RTPredictedContextWorkout workoutActivityType]
+ -[RTRoutineManager _enumerateElevationsWithOptions:reply:]
+ -[RTRoutineManager correctLabelForCurrentPlace:date:newLabel:handler:]
+ -[RTRoutineManager correctLabelForVisitWithIdentifier:entryDate:originalLabel:newLabel:handler:]
+ -[RTRoutineManager enumerateElevationsWithOptions:reply:]
+ -[RTRoutineManager fetchLearnedRoutesWithOptions:handler:]
+ -[RTRoutineManager fetchPredictedContextWithOptions:completionHandler:]
+ -[RTRoutineManager fetchTripClusterMetadataWithOptions:handler:]
+ -[RTRoutineManager onPredictedContextResult:error:]
+ -[RTRoutineManager onRemoteStatusUpdate:error:]
+ -[RTRoutineManager predictedContextHandler]
+ -[RTRoutineManager predictedContextOptions]
+ -[RTRoutineManager purgeTripClusterTable:handler:]
+ -[RTRoutineManager purgeTripClusterWithClusterID:handler:]
+ -[RTRoutineManager remoteStatusHandler]
+ -[RTRoutineManager setPredictedContextHandler:]
+ -[RTRoutineManager setPredictedContextOptions:]
+ -[RTRoutineManager setRemoteStatusHandler:]
+ -[RTRoutineManager setXpcQueue:]
+ -[RTRoutineManager startMonitoringPredictedContextWithOptions:completionHandler:]
+ -[RTRoutineManager startMonitoringRemoteStatusWithHandler:]
+ -[RTRoutineManager stopMonitoringPredictedContextWithHandler:]
+ -[RTRoutineManager stopMonitoringRemoteStatusWithHandler:]
+ -[RTRoutineManager submitUserCurationForDate:newLabel:handler:]
+ -[RTRoutineManager submitUserCurationForVisitDateRange:newLabel:handler:]
+ -[RTRoutineManager xpcQueue]
+ -[RTRoutineManagerExportedObject onPredictedContextResult:error:]
+ -[RTRoutineManagerExportedObject onRemoteStatusUpdate:error:]
+ -[RTSourceEventKit initWithEventIdentifier:startDate:endDate:title:location:allDay:sharingStatus:tentative:participationOptional:suggestionInfo_opaqueKey:suggestionsSchemaOrg:]
+ -[RTSourceEventKit participationOptional]
+ -[RTSourceEventKit tentative]
+ -[RTSourceHealthKitWorkout .cxx_destruct]
+ -[RTSourceHealthKitWorkout description]
+ -[RTSourceHealthKitWorkout encodeWithCoder:]
+ -[RTSourceHealthKitWorkout hash]
+ -[RTSourceHealthKitWorkout initWithCoder:]
+ -[RTSourceHealthKitWorkout initWithWorkoutUUID:startDate:]
+ -[RTSourceHealthKitWorkout isEqual:]
+ -[RTSourceHealthKitWorkout startDate]
+ -[RTSourceHealthKitWorkout workoutUUID]
+ -[RTSourceHomeKit .cxx_destruct]
+ -[RTSourceHomeKit description]
+ -[RTSourceHomeKit encodeWithCoder:]
+ -[RTSourceHomeKit hash]
+ -[RTSourceHomeKit identifier]
+ -[RTSourceHomeKit initWithCoder:]
+ -[RTSourceHomeKit initWithIdentifier:primary:]
+ -[RTSourceHomeKit init]
+ -[RTSourceHomeKit isEqual:]
+ -[RTSourceHomeKit primary]
+ -[RTSourceParkedCar .cxx_destruct]
+ -[RTSourceParkedCar description]
+ -[RTSourceParkedCar encodeWithCoder:]
+ -[RTSourceParkedCar hash]
+ -[RTSourceParkedCar identifier]
+ -[RTSourceParkedCar initWithCoder:]
+ -[RTSourceParkedCar initWithIdentifier:parkDate:]
+ -[RTSourceParkedCar init]
+ -[RTSourceParkedCar isEqual:]
+ -[RTSourceParkedCar parkDate]
+ -[RTSourcePropagatedLocation .cxx_destruct]
+ -[RTSourcePropagatedLocation date]
+ -[RTSourcePropagatedLocation description]
+ -[RTSourcePropagatedLocation encodeWithCoder:]
+ -[RTSourcePropagatedLocation hash]
+ -[RTSourcePropagatedLocation initWithCoder:]
+ -[RTSourcePropagatedLocation initWithDate:]
+ -[RTSourcePropagatedLocation init]
+ -[RTSourcePropagatedLocation isEqual:]
+ -[RTStoredUserCurationFetchOptions .cxx_destruct]
+ -[RTStoredUserCurationFetchOptions ascending]
+ -[RTStoredUserCurationFetchOptions description]
+ -[RTStoredUserCurationFetchOptions encodeWithCoder:]
+ -[RTStoredUserCurationFetchOptions hash]
+ -[RTStoredUserCurationFetchOptions initWithAscending:limit:]
+ -[RTStoredUserCurationFetchOptions initWithAscending:sortIndex:limit:]
+ -[RTStoredUserCurationFetchOptions initWithAscending:sortIndex:submissionDateInterval:visitDateInterval:limit:]
+ -[RTStoredUserCurationFetchOptions initWithAscending:submissionDateInterval:limit:]
+ -[RTStoredUserCurationFetchOptions initWithAscending:visitDateInterval:limit:]
+ -[RTStoredUserCurationFetchOptions initWithCoder:]
+ -[RTStoredUserCurationFetchOptions init]
+ -[RTStoredUserCurationFetchOptions isEqual:]
+ -[RTStoredUserCurationFetchOptions isEqualToFetchOptions:]
+ -[RTStoredUserCurationFetchOptions limit]
+ -[RTStoredUserCurationFetchOptions setSubmissionDateInterval:]
+ -[RTStoredUserCurationFetchOptions setVisitDateInterval:]
+ -[RTStoredUserCurationFetchOptions sortIndex]
+ -[RTStoredUserCurationFetchOptions submissionDateInterval]
+ -[RTStoredUserCurationFetchOptions visitDateInterval]
+ -[RTStoredVisitFetchOptions filterPairedVisitEntries]
+ -[RTStoredVisitFetchOptions initWithAscending:confidence:dateInterval:labelVisit:limit:sources:redact:]
+ -[RTStoredVisitFetchOptions initWithAscending:confidence:dateInterval:labelVisit:limit:sources:redact:filterPairedVisitEntries:]
+ -[RTStoredVisitFetchOptions redact]
+ -[RTTripClusterEnumerationContext .cxx_destruct]
+ -[RTTripClusterEnumerationContext copyWithZone:]
+ -[RTTripClusterEnumerationContext description]
+ -[RTTripClusterEnumerationContext encodeWithCoder:]
+ -[RTTripClusterEnumerationContext hash]
+ -[RTTripClusterEnumerationContext initWithCoder:]
+ -[RTTripClusterEnumerationContext initWithEnumerationOptions:]
+ -[RTTripClusterEnumerationContext initWithEnumerationOptions:offset:]
+ -[RTTripClusterEnumerationContext init]
+ -[RTTripClusterEnumerationContext isEqual:]
+ -[RTTripClusterEnumerationContext isEqualToContext:]
+ -[RTTripClusterEnumerationContext offset]
+ -[RTTripClusterEnumerationContext options]
+ -[RTTripClusterEnumerationOptions batchSize]
+ -[RTTripClusterEnumerationOptions copyWithZone:]
+ -[RTTripClusterEnumerationOptions description]
+ -[RTTripClusterEnumerationOptions encodeWithCoder:]
+ -[RTTripClusterEnumerationOptions endLatitude]
+ -[RTTripClusterEnumerationOptions endLongitude]
+ -[RTTripClusterEnumerationOptions enumeratedType]
+ -[RTTripClusterEnumerationOptions hash]
+ -[RTTripClusterEnumerationOptions initWithCoder:]
+ -[RTTripClusterEnumerationOptions initWithEndVisitLatitude:endLongitude:]
+ -[RTTripClusterEnumerationOptions initWithMinCountOfTraversal:startLatitude:startLongitude:endLatitude:endLongitude:]
+ -[RTTripClusterEnumerationOptions initWithStartAndEndVisitLatitude:startLongitude:endLatitude:endLongitude:]
+ -[RTTripClusterEnumerationOptions initWithStartVisitLatitude:startLongitude:]
+ -[RTTripClusterEnumerationOptions initWithStartVisitLatitude:startVisitLongitude:endVisitLatitude:endVisitLongitude:]
+ -[RTTripClusterEnumerationOptions initWithbatchSize:]
+ -[RTTripClusterEnumerationOptions init]
+ -[RTTripClusterEnumerationOptions isEqual:]
+ -[RTTripClusterEnumerationOptions minCountOfTraversal]
+ -[RTTripClusterEnumerationOptions processingBlock]
+ -[RTTripClusterEnumerationOptions setBatchSize:]
+ -[RTTripClusterEnumerationOptions setEndLatitude:]
+ -[RTTripClusterEnumerationOptions setEndLongitude:]
+ -[RTTripClusterEnumerationOptions setMinCountOfTraversal:]
+ -[RTTripClusterEnumerationOptions setStartLatitude:]
+ -[RTTripClusterEnumerationOptions setStartLongitude:]
+ -[RTTripClusterEnumerationOptions startLatitude]
+ -[RTTripClusterEnumerationOptions startLongitude]
+ -[RTTripClusterMetadata .cxx_destruct]
+ -[RTTripClusterMetadata averageTripDistance]
+ -[RTTripClusterMetadata averageTripTime]
+ -[RTTripClusterMetadata avgBikeDistance]
+ -[RTTripClusterMetadata avgBikeTime]
+ -[RTTripClusterMetadata avgWalkDistance]
+ -[RTTripClusterMetadata avgWalkTime]
+ -[RTTripClusterMetadata bikeTraversalCount]
+ -[RTTripClusterMetadata clusterID]
+ -[RTTripClusterMetadata clusterOrder]
+ -[RTTripClusterMetadata commuteID]
+ -[RTTripClusterMetadata copyWithZone:]
+ -[RTTripClusterMetadata countOfTraversal]
+ -[RTTripClusterMetadata dateOfMostRecentTrip]
+ -[RTTripClusterMetadata description]
+ -[RTTripClusterMetadata destinationLatitude]
+ -[RTTripClusterMetadata destinationLongitude]
+ -[RTTripClusterMetadata encodeWithCoder:]
+ -[RTTripClusterMetadata initWithCoder:]
+ -[RTTripClusterMetadata initWithTripClusterId:dateOfMostRecentTrip:modeOfTransport:countOfTraversal:originLatitude:originLongitude:destinationLatitude:destinationLongitude:averageTripTime:averageTripDistance:minimumTripTime:maximumTripTime:minimumTripDistance:maximumTripDistance:commuteID:isLocked:avgBikeDistance:avgBikeTime:avgWalkDistance:avgWalkTime:bikeTraversalCount:walkTraversalCount:clusterOrder:]
+ -[RTTripClusterMetadata isEqual:]
+ -[RTTripClusterMetadata isLocked]
+ -[RTTripClusterMetadata maximumTripDistance]
+ -[RTTripClusterMetadata maximumTripTime]
+ -[RTTripClusterMetadata minimumTripDistance]
+ -[RTTripClusterMetadata minimumTripTime]
+ -[RTTripClusterMetadata modeOfTransport]
+ -[RTTripClusterMetadata originLatitude]
+ -[RTTripClusterMetadata originLongitude]
+ -[RTTripClusterMetadata setAvgBikeDistance:]
+ -[RTTripClusterMetadata setAvgBikeTime:]
+ -[RTTripClusterMetadata setAvgWalkDistance:]
+ -[RTTripClusterMetadata setAvgWalkTime:]
+ -[RTTripClusterMetadata setBikeTraversalCount:]
+ -[RTTripClusterMetadata setClusterOrder:]
+ -[RTTripClusterMetadata setWalkTraversalCount:]
+ -[RTTripClusterMetadata walkTraversalCount]
+ -[RTTripClusterMetadataFetchOptions copyWithZone:]
+ -[RTTripClusterMetadataFetchOptions description]
+ -[RTTripClusterMetadataFetchOptions destinationVisitLatitude]
+ -[RTTripClusterMetadataFetchOptions destinationVisitLongitude]
+ -[RTTripClusterMetadataFetchOptions encodeWithCoder:]
+ -[RTTripClusterMetadataFetchOptions initWithCoder:]
+ -[RTTripClusterMetadataFetchOptions initWithOriginVisitLatitude:originVisitLongitude:destinationVisitLatitude:destinationVisitLongitude:]
+ -[RTTripClusterMetadataFetchOptions init]
+ -[RTTripClusterMetadataFetchOptions isEqual:]
+ -[RTTripClusterMetadataFetchOptions isEqualToFetchOptions:]
+ -[RTTripClusterMetadataFetchOptions originVisitLatitude]
+ -[RTTripClusterMetadataFetchOptions originVisitLongitude]
+ -[RTTripClusterRecencyEnumerationContext .cxx_destruct]
+ -[RTTripClusterRecencyEnumerationContext copyWithZone:]
+ -[RTTripClusterRecencyEnumerationContext description]
+ -[RTTripClusterRecencyEnumerationContext encodeWithCoder:]
+ -[RTTripClusterRecencyEnumerationContext hash]
+ -[RTTripClusterRecencyEnumerationContext initWithCoder:]
+ -[RTTripClusterRecencyEnumerationContext initWithEnumerationOptions:]
+ -[RTTripClusterRecencyEnumerationContext initWithEnumerationOptions:offset:]
+ -[RTTripClusterRecencyEnumerationContext init]
+ -[RTTripClusterRecencyEnumerationContext isEqual:]
+ -[RTTripClusterRecencyEnumerationContext isEqualToContext:]
+ -[RTTripClusterRecencyEnumerationContext offset]
+ -[RTTripClusterRecencyEnumerationContext options]
+ -[RTTripClusterRecencyEnumerationOptions .cxx_destruct]
+ -[RTTripClusterRecencyEnumerationOptions batchSize]
+ -[RTTripClusterRecencyEnumerationOptions clusterID]
+ -[RTTripClusterRecencyEnumerationOptions copyWithZone:]
+ -[RTTripClusterRecencyEnumerationOptions encodeWithCoder:]
+ -[RTTripClusterRecencyEnumerationOptions hash]
+ -[RTTripClusterRecencyEnumerationOptions initWithClusterID:]
+ -[RTTripClusterRecencyEnumerationOptions initWithCoder:]
+ -[RTTripClusterRecencyEnumerationOptions initWithbatchSize:]
+ -[RTTripClusterRecencyEnumerationOptions init]
+ -[RTTripClusterRecencyEnumerationOptions isEqual:]
+ -[RTTripClusterRecencyEnumerationOptions processingBlock]
+ -[RTTripClusterRecencyEnumerationOptions setBatchSize:]
+ -[RTTripClusterRecencyEnumerationOptions setClusterID:]
+ -[RTTripClusterRoadTransitionsEnumerationContext .cxx_destruct]
+ -[RTTripClusterRoadTransitionsEnumerationContext copyWithZone:]
+ -[RTTripClusterRoadTransitionsEnumerationContext description]
+ -[RTTripClusterRoadTransitionsEnumerationContext encodeWithCoder:]
+ -[RTTripClusterRoadTransitionsEnumerationContext hash]
+ -[RTTripClusterRoadTransitionsEnumerationContext initWithCoder:]
+ -[RTTripClusterRoadTransitionsEnumerationContext initWithEnumerationOptions:]
+ -[RTTripClusterRoadTransitionsEnumerationContext initWithEnumerationOptions:offset:]
+ -[RTTripClusterRoadTransitionsEnumerationContext init]
+ -[RTTripClusterRoadTransitionsEnumerationContext isEqual:]
+ -[RTTripClusterRoadTransitionsEnumerationContext isEqualToContext:]
+ -[RTTripClusterRoadTransitionsEnumerationContext offset]
+ -[RTTripClusterRoadTransitionsEnumerationContext options]
+ -[RTTripClusterRoadTransitionsEnumerationOptions .cxx_destruct]
+ -[RTTripClusterRoadTransitionsEnumerationOptions batchSize]
+ -[RTTripClusterRoadTransitionsEnumerationOptions clusterID]
+ -[RTTripClusterRoadTransitionsEnumerationOptions copyWithZone:]
+ -[RTTripClusterRoadTransitionsEnumerationOptions encodeWithCoder:]
+ -[RTTripClusterRoadTransitionsEnumerationOptions hash]
+ -[RTTripClusterRoadTransitionsEnumerationOptions initWithClusterID:]
+ -[RTTripClusterRoadTransitionsEnumerationOptions initWithCoder:]
+ -[RTTripClusterRoadTransitionsEnumerationOptions initWithbatchSize:]
+ -[RTTripClusterRoadTransitionsEnumerationOptions init]
+ -[RTTripClusterRoadTransitionsEnumerationOptions isEqual:]
+ -[RTTripClusterRoadTransitionsEnumerationOptions processingBlock]
+ -[RTTripClusterRoadTransitionsEnumerationOptions setBatchSize:]
+ -[RTTripClusterRoadTransitionsEnumerationOptions setClusterID:]
+ -[RTTripClusterRouteEnumerationContext .cxx_destruct]
+ -[RTTripClusterRouteEnumerationContext copyWithZone:]
+ -[RTTripClusterRouteEnumerationContext description]
+ -[RTTripClusterRouteEnumerationContext encodeWithCoder:]
+ -[RTTripClusterRouteEnumerationContext hash]
+ -[RTTripClusterRouteEnumerationContext initWithCoder:]
+ -[RTTripClusterRouteEnumerationContext initWithEnumerationOptions:]
+ -[RTTripClusterRouteEnumerationContext initWithEnumerationOptions:offset:]
+ -[RTTripClusterRouteEnumerationContext init]
+ -[RTTripClusterRouteEnumerationContext isEqual:]
+ -[RTTripClusterRouteEnumerationContext isEqualToContext:]
+ -[RTTripClusterRouteEnumerationContext offset]
+ -[RTTripClusterRouteEnumerationContext options]
+ -[RTTripClusterRouteEnumerationOptions .cxx_destruct]
+ -[RTTripClusterRouteEnumerationOptions batchSize]
+ -[RTTripClusterRouteEnumerationOptions clusterID]
+ -[RTTripClusterRouteEnumerationOptions copyWithZone:]
+ -[RTTripClusterRouteEnumerationOptions description]
+ -[RTTripClusterRouteEnumerationOptions encodeWithCoder:]
+ -[RTTripClusterRouteEnumerationOptions enumeratedType]
+ -[RTTripClusterRouteEnumerationOptions hash]
+ -[RTTripClusterRouteEnumerationOptions initWithClusterID:]
+ -[RTTripClusterRouteEnumerationOptions initWithCoder:]
+ -[RTTripClusterRouteEnumerationOptions initWithbatchSize:]
+ -[RTTripClusterRouteEnumerationOptions init]
+ -[RTTripClusterRouteEnumerationOptions isEqual:]
+ -[RTTripClusterRouteEnumerationOptions isEqualToOptions:]
+ -[RTTripClusterRouteEnumerationOptions processingBlock]
+ -[RTTripClusterRouteEnumerationOptions setBatchSize:]
+ -[RTTripClusterRouteEnumerationOptions setClusterID:]
+ -[RTTripClusterScheduleEnumerationContext .cxx_destruct]
+ -[RTTripClusterScheduleEnumerationContext copyWithZone:]
+ -[RTTripClusterScheduleEnumerationContext description]
+ -[RTTripClusterScheduleEnumerationContext encodeWithCoder:]
+ -[RTTripClusterScheduleEnumerationContext hash]
+ -[RTTripClusterScheduleEnumerationContext initWithCoder:]
+ -[RTTripClusterScheduleEnumerationContext initWithEnumerationOptions:]
+ -[RTTripClusterScheduleEnumerationContext initWithEnumerationOptions:offset:]
+ -[RTTripClusterScheduleEnumerationContext init]
+ -[RTTripClusterScheduleEnumerationContext isEqual:]
+ -[RTTripClusterScheduleEnumerationContext isEqualToContext:]
+ -[RTTripClusterScheduleEnumerationContext offset]
+ -[RTTripClusterScheduleEnumerationContext options]
+ -[RTTripClusterScheduleEnumerationOptions .cxx_destruct]
+ -[RTTripClusterScheduleEnumerationOptions batchSize]
+ -[RTTripClusterScheduleEnumerationOptions clusterID]
+ -[RTTripClusterScheduleEnumerationOptions copyWithZone:]
+ -[RTTripClusterScheduleEnumerationOptions encodeWithCoder:]
+ -[RTTripClusterScheduleEnumerationOptions hash]
+ -[RTTripClusterScheduleEnumerationOptions initWithClusterID:]
+ -[RTTripClusterScheduleEnumerationOptions initWithCoder:]
+ -[RTTripClusterScheduleEnumerationOptions initWithbatchSize:]
+ -[RTTripClusterScheduleEnumerationOptions init]
+ -[RTTripClusterScheduleEnumerationOptions isEqual:]
+ -[RTTripClusterScheduleEnumerationOptions processingBlock]
+ -[RTTripClusterScheduleEnumerationOptions setBatchSize:]
+ -[RTTripClusterScheduleEnumerationOptions setClusterID:]
+ -[RTTripSegment destinationLatitude]
+ -[RTTripSegment destinationLongitude]
+ -[RTTripSegment initWithTripSegmentIdentifier:dateInterval:tripDistance:tripDistanceUncertainty:modeOfTransportation:isConsumedByClustering:tripSegmentSequence:tripSegmentSequenceMax:originLatitude:originLongitude:destinationLatitude:destinationLongitude:tripCommuteID:]
+ -[RTTripSegment isConsumedByClustering]
+ -[RTTripSegment originLatitude]
+ -[RTTripSegment originLongitude]
+ -[RTTripSegment setIsConsumedByClustering:]
+ -[RTTripSegment setTripCommuteID:]
+ -[RTTripSegment tripCommuteID]
+ -[RTTripSegment tripSegmentSequenceMax]
+ -[RTTripSegment tripSegmentSequence]
+ -[RTUserCuration .cxx_destruct]
+ -[RTUserCuration abbreviatedDescription]
+ -[RTUserCuration copyWithZone:]
+ -[RTUserCuration curatedLabel]
+ -[RTUserCuration description]
+ -[RTUserCuration encodeWithCoder:]
+ -[RTUserCuration expirationDate]
+ -[RTUserCuration hash]
+ -[RTUserCuration identifier]
+ -[RTUserCuration initWithCoder:]
+ -[RTUserCuration initWithIdentifier:submissionDate:expirationDate:entryDate:exitDate:curatedLabel:]
+ -[RTUserCuration isEqual:]
+ -[RTUserCuration isEqualToUserCuration:]
+ -[RTUserCuration submissionDate]
+ -[RTUserCuration visitEntryDate]
+ -[RTUserCuration visitExitDate]
+ -[RTVisit identifier]
+ -[RTVisit initWithDate:type:location:entry:exit:dataPointCount:confidence:placeInference:source:identifier:]
+ GCC_except_table11
+ GCC_except_table160
+ GCC_except_table161
+ GCC_except_table168
+ GCC_except_table568
+ GCC_except_table7
+ _OBJC_CLASS_$_GEOMapItemIdentifier
+ _OBJC_CLASS_$_NSConstantArray
+ _OBJC_CLASS_$_NSURL
+ _OBJC_CLASS_$_RTAuthorizedLocationConfirmationStatusEnumerationContext
+ _OBJC_CLASS_$_RTAuthorizedLocationConfirmationStatusEnumerationOptions
+ _OBJC_CLASS_$_RTAuthorizedLocationDiagnosticStatus
+ _OBJC_CLASS_$_RTAuthorizedLocationZDRLocationsEnumerationContext
+ _OBJC_CLASS_$_RTAuthorizedLocationZDRLocationsEnumerationOptions
+ _OBJC_CLASS_$_RTBluePOIMetadata
+ _OBJC_CLASS_$_RTBluePOITile
+ _OBJC_CLASS_$_RTBluePOITileDownloadResult
+ _OBJC_CLASS_$_RTGeoRoadDataEnumerationContext
+ _OBJC_CLASS_$_RTGeoRoadDataEnumerationOptions
+ _OBJC_CLASS_$_RTLearnedRoute
+ _OBJC_CLASS_$_RTLearnedRouteFetchOptions
+ _OBJC_CLASS_$_RTLearnedRouteLocation
+ _OBJC_CLASS_$_RTLearnedRouteMetrics
+ _OBJC_CLASS_$_RTLearnedRouteTravelMode
+ _OBJC_CLASS_$_RTLocalBluePOIResult
+ _OBJC_CLASS_$_RTLocationsFromCoreLocationFetchOptions
+ _OBJC_CLASS_$_RTPointOfInterest
+ _OBJC_CLASS_$_RTPredictedContext
+ _OBJC_CLASS_$_RTPredictedContextAnalytics
+ _OBJC_CLASS_$_RTPredictedContextAnalyticsRolledLOIResult
+ _OBJC_CLASS_$_RTPredictedContextDate
+ _OBJC_CLASS_$_RTPredictedContextDateInterval
+ _OBJC_CLASS_$_RTPredictedContextLocation
+ _OBJC_CLASS_$_RTPredictedContextOptions
+ _OBJC_CLASS_$_RTPredictedContextRequest
+ _OBJC_CLASS_$_RTPredictedContextResult
+ _OBJC_CLASS_$_RTPredictedContextSequence
+ _OBJC_CLASS_$_RTPredictedContextTransition
+ _OBJC_CLASS_$_RTPredictedContextTransport
+ _OBJC_CLASS_$_RTPredictedContextWorkout
+ _OBJC_CLASS_$_RTSourceHealthKitWorkout
+ _OBJC_CLASS_$_RTSourceHomeKit
+ _OBJC_CLASS_$_RTSourceParkedCar
+ _OBJC_CLASS_$_RTSourcePropagatedLocation
+ _OBJC_CLASS_$_RTStoredUserCurationFetchOptions
+ _OBJC_CLASS_$_RTTripClusterEnumerationContext
+ _OBJC_CLASS_$_RTTripClusterEnumerationOptions
+ _OBJC_CLASS_$_RTTripClusterMetadata
+ _OBJC_CLASS_$_RTTripClusterMetadataFetchOptions
+ _OBJC_CLASS_$_RTTripClusterRecencyEnumerationContext
+ _OBJC_CLASS_$_RTTripClusterRecencyEnumerationOptions
+ _OBJC_CLASS_$_RTTripClusterRoadTransitionsEnumerationContext
+ _OBJC_CLASS_$_RTTripClusterRoadTransitionsEnumerationOptions
+ _OBJC_CLASS_$_RTTripClusterRouteEnumerationContext
+ _OBJC_CLASS_$_RTTripClusterRouteEnumerationOptions
+ _OBJC_CLASS_$_RTTripClusterScheduleEnumerationContext
+ _OBJC_CLASS_$_RTTripClusterScheduleEnumerationOptions
+ _OBJC_CLASS_$_RTUserCuration
+ _OBJC_IVAR_$_RTAuthorizedLocationConfirmationStatusEnumerationContext._offset
+ _OBJC_IVAR_$_RTAuthorizedLocationConfirmationStatusEnumerationContext._options
+ _OBJC_IVAR_$_RTAuthorizedLocationDiagnosticStatus._fullConfirmationList
+ _OBJC_IVAR_$_RTAuthorizedLocationDiagnosticStatus._zdrConfirmationList
+ _OBJC_IVAR_$_RTAuthorizedLocationZDRLocationsEnumerationContext._offset
+ _OBJC_IVAR_$_RTAuthorizedLocationZDRLocationsEnumerationContext._options
+ _OBJC_IVAR_$_RTBluePOIMetadata._categoryDenyList
+ _OBJC_IVAR_$_RTBluePOIMetadata._geoCacheInfo
+ _OBJC_IVAR_$_RTBluePOIMetadata._identifier
+ _OBJC_IVAR_$_RTBluePOIMetadata._modelCalibrationParameters
+ _OBJC_IVAR_$_RTBluePOITile._apToModelMapping
+ _OBJC_IVAR_$_RTBluePOITile._date
+ _OBJC_IVAR_$_RTBluePOITile._downloadKey
+ _OBJC_IVAR_$_RTBluePOITile._geoCacheInfo
+ _OBJC_IVAR_$_RTBluePOITile._geoTileKey
+ _OBJC_IVAR_$_RTBluePOITile._identifier
+ _OBJC_IVAR_$_RTBluePOITile._modelCalibrationParameters
+ _OBJC_IVAR_$_RTBluePOITile._modelURLs
+ _OBJC_IVAR_$_RTBluePOITile._pointsOfInterest
+ _OBJC_IVAR_$_RTBluePOITile._singlePOIMuid
+ _OBJC_IVAR_$_RTBluePOITile._size
+ _OBJC_IVAR_$_RTBluePOITileDownloadResult._downloadError
+ _OBJC_IVAR_$_RTBluePOITileDownloadResult._downloadKey
+ _OBJC_IVAR_$_RTBluePOITileDownloadResult._tileCacheInfo
+ _OBJC_IVAR_$_RTBluePOITileDownloadResult._tileURL
+ _OBJC_IVAR_$_RTGeoRoadDataEnumerationContext._offset
+ _OBJC_IVAR_$_RTGeoRoadDataEnumerationContext._options
+ _OBJC_IVAR_$_RTGeoRoadDataEnumerationOptions._batchSize
+ _OBJC_IVAR_$_RTLearnedRoute._learnedRouteEndLocation
+ _OBJC_IVAR_$_RTLearnedRoute._learnedRouteEndLocationWithReferenceFrame
+ _OBJC_IVAR_$_RTLearnedRoute._learnedRouteIdentifier
+ _OBJC_IVAR_$_RTLearnedRoute._learnedRouteStartLocation
+ _OBJC_IVAR_$_RTLearnedRoute._learnedRouteStartLocationWithReferenceFrame
+ _OBJC_IVAR_$_RTLearnedRoute._likelihood
+ _OBJC_IVAR_$_RTLearnedRoute._travelModeRoutes
+ _OBJC_IVAR_$_RTLearnedRoute._travelTimeEstimateForEntireRouteInSeconds
+ _OBJC_IVAR_$_RTLearnedRoute._travelledDistanceEstimateForEntireRouteInMeters
+ _OBJC_IVAR_$_RTLearnedRouteFetchOptions._bundleIdentifier
+ _OBJC_IVAR_$_RTLearnedRouteFetchOptions._bundlePath
+ _OBJC_IVAR_$_RTLearnedRouteFetchOptions._destinationVisit
+ _OBJC_IVAR_$_RTLearnedRouteFetchOptions._fetchAllRouteLocations
+ _OBJC_IVAR_$_RTLearnedRouteFetchOptions._originVisit
+ _OBJC_IVAR_$_RTLearnedRouteFetchOptions._routeDate
+ _OBJC_IVAR_$_RTLearnedRouteFetchOptions._routeFetchType
+ _OBJC_IVAR_$_RTLearnedRouteFetchOptions._routeOriginType
+ _OBJC_IVAR_$_RTLearnedRouteLocation._course
+ _OBJC_IVAR_$_RTLearnedRouteLocation._followedByUTurn
+ _OBJC_IVAR_$_RTLearnedRouteLocation._latitude
+ _OBJC_IVAR_$_RTLearnedRouteLocation._locationReferenceFrame
+ _OBJC_IVAR_$_RTLearnedRouteLocation._longitude
+ _OBJC_IVAR_$_RTLearnedRouteMetrics._allRoutesCountForThisODPair
+ _OBJC_IVAR_$_RTLearnedRouteMetrics._allTraversalCountBetweenThisODPair
+ _OBJC_IVAR_$_RTLearnedRouteMetrics._lastTravelledDate
+ _OBJC_IVAR_$_RTLearnedRouteMetrics._routeTravelCountOnTravelDayOfWeekHourOfDay
+ _OBJC_IVAR_$_RTLearnedRouteMetrics._routeTraversalCount
+ _OBJC_IVAR_$_RTLearnedRouteMetrics._routeTraversalCountOnTravelDayOfWeek
+ _OBJC_IVAR_$_RTLearnedRouteTravelMode._learnedRouteLocations
+ _OBJC_IVAR_$_RTLearnedRouteTravelMode._learnedRouteMetrics
+ _OBJC_IVAR_$_RTLearnedRouteTravelMode._maxTravelTimeEstimateInSeconds
+ _OBJC_IVAR_$_RTLearnedRouteTravelMode._maxTravelledDistanceEstimateInMeters
+ _OBJC_IVAR_$_RTLearnedRouteTravelMode._meanTravelTimeEstimateInSeconds
+ _OBJC_IVAR_$_RTLearnedRouteTravelMode._meanTravelledDistanceEstimateInMeters
+ _OBJC_IVAR_$_RTLearnedRouteTravelMode._minTravelTimeEstimateInSeconds
+ _OBJC_IVAR_$_RTLearnedRouteTravelMode._minTravelledDistanceEstimateInMeters
+ _OBJC_IVAR_$_RTLearnedRouteTravelMode._routeLocations
+ _OBJC_IVAR_$_RTLearnedRouteTravelMode._routeTravelMode
+ _OBJC_IVAR_$_RTLocalBluePOIResult._aoiConfidences
+ _OBJC_IVAR_$_RTLocalBluePOIResult._mostConfidentAOI
+ _OBJC_IVAR_$_RTLocalBluePOIResult._mostConfidentPOI
+ _OBJC_IVAR_$_RTLocalBluePOIResult._poiConfidences
+ _OBJC_IVAR_$_RTLocalBluePOIResult._queryTime
+ _OBJC_IVAR_$_RTLocalBluePOIResult._referenceLocation
+ _OBJC_IVAR_$_RTLocationsFromCoreLocationFetchOptions._date
+ _OBJC_IVAR_$_RTLocationsFromCoreLocationFetchOptions._machContinuousTimeSec
+ _OBJC_IVAR_$_RTLocationsFromCoreLocationFetchOptions._numberOfSeconds
+ _OBJC_IVAR_$_RTMapItem._categoryMUID
+ _OBJC_IVAR_$_RTPointOfInterest._applePaySupport
+ _OBJC_IVAR_$_RTPointOfInterest._filtered
+ _OBJC_IVAR_$_RTPointOfInterest._fullyCoversTile
+ _OBJC_IVAR_$_RTPointOfInterest._identifier
+ _OBJC_IVAR_$_RTPointOfInterest._location
+ _OBJC_IVAR_$_RTPointOfInterest._muid
+ _OBJC_IVAR_$_RTPointOfInterest._polygon
+ _OBJC_IVAR_$_RTPredictedContext._dateInterval
+ _OBJC_IVAR_$_RTPredictedContext._predictionSources
+ _OBJC_IVAR_$_RTPredictedContext._probability
+ _OBJC_IVAR_$_RTPredictedContextAnalytics._rolledLOIResult
+ _OBJC_IVAR_$_RTPredictedContextAnalyticsRolledLOIResult._identifier
+ _OBJC_IVAR_$_RTPredictedContextAnalyticsRolledLOIResult._isHome
+ _OBJC_IVAR_$_RTPredictedContextAnalyticsRolledLOIResult._isWork
+ _OBJC_IVAR_$_RTPredictedContextAnalyticsRolledLOIResult._loiIsMissingFromCurrentVisitHistory
+ _OBJC_IVAR_$_RTPredictedContextDate._confidenceInterval
+ _OBJC_IVAR_$_RTPredictedContextDate._date
+ _OBJC_IVAR_$_RTPredictedContextDateInterval._endDate
+ _OBJC_IVAR_$_RTPredictedContextDateInterval._startDate
+ _OBJC_IVAR_$_RTPredictedContextLocation._locationOfInterest
+ _OBJC_IVAR_$_RTPredictedContextOptions._filterContextTypeMask
+ _OBJC_IVAR_$_RTPredictedContextOptions._filterLocations
+ _OBJC_IVAR_$_RTPredictedContextOptions._forecastWindowDateInterval
+ _OBJC_IVAR_$_RTPredictedContextOptions._forecastWindowTimeInterval
+ _OBJC_IVAR_$_RTPredictedContextOptions._resultSortDescriptors
+ _OBJC_IVAR_$_RTPredictedContextOptions._resultSortProbabilityAscending
+ _OBJC_IVAR_$_RTPredictedContextOptions._resultSortStartDateAscending
+ _OBJC_IVAR_$_RTPredictedContextRequest._clientCount
+ _OBJC_IVAR_$_RTPredictedContextRequest._identifier
+ _OBJC_IVAR_$_RTPredictedContextRequest._inferenceTriggerReason
+ _OBJC_IVAR_$_RTPredictedContextRequest._memoryFootprintEnd
+ _OBJC_IVAR_$_RTPredictedContextRequest._memoryFootprintStart
+ _OBJC_IVAR_$_RTPredictedContextRequest._predictedContextResult
+ _OBJC_IVAR_$_RTPredictedContextRequest._requestEndDate
+ _OBJC_IVAR_$_RTPredictedContextRequest._requestStartDate
+ _OBJC_IVAR_$_RTPredictedContextResult._analytics
+ _OBJC_IVAR_$_RTPredictedContextResult._predictedContexts
+ _OBJC_IVAR_$_RTPredictedContextSequence._contexts
+ _OBJC_IVAR_$_RTPredictedContextSequence._dateInterval
+ _OBJC_IVAR_$_RTPredictedContextSequence._predictedContexts
+ _OBJC_IVAR_$_RTPredictedContextSequence._probability
+ _OBJC_IVAR_$_RTPredictedContextTransition._predictedContextTransports
+ _OBJC_IVAR_$_RTPredictedContextTransport._probability
+ _OBJC_IVAR_$_RTPredictedContextTransport._transportMode
+ _OBJC_IVAR_$_RTRoutineManager._predictedContextHandler
+ _OBJC_IVAR_$_RTRoutineManager._predictedContextOptions
+ _OBJC_IVAR_$_RTRoutineManager._remoteStatusHandler
+ _OBJC_IVAR_$_RTRoutineManager._xpcQueue
+ _OBJC_IVAR_$_RTSourcePropagatedLocation._date
+ _OBJC_IVAR_$_RTStoredUserCurationFetchOptions._ascending
+ _OBJC_IVAR_$_RTStoredUserCurationFetchOptions._limit
+ _OBJC_IVAR_$_RTStoredUserCurationFetchOptions._sortIndex
+ _OBJC_IVAR_$_RTStoredUserCurationFetchOptions._submissionDateInterval
+ _OBJC_IVAR_$_RTStoredUserCurationFetchOptions._visitDateInterval
+ _OBJC_IVAR_$_RTStoredVisitFetchOptions._filterPairedVisitEntries
+ _OBJC_IVAR_$_RTStoredVisitFetchOptions._redact
+ _OBJC_IVAR_$_RTTripClusterEnumerationContext._offset
+ _OBJC_IVAR_$_RTTripClusterEnumerationContext._options
+ _OBJC_IVAR_$_RTTripClusterMetadata._averageTripDistance
+ _OBJC_IVAR_$_RTTripClusterMetadata._averageTripTime
+ _OBJC_IVAR_$_RTTripClusterMetadata._avgBikeDistance
+ _OBJC_IVAR_$_RTTripClusterMetadata._avgBikeTime
+ _OBJC_IVAR_$_RTTripClusterMetadata._avgWalkDistance
+ _OBJC_IVAR_$_RTTripClusterMetadata._avgWalkTime
+ _OBJC_IVAR_$_RTTripClusterMetadata._bikeTraversalCount
+ _OBJC_IVAR_$_RTTripClusterMetadata._clusterID
+ _OBJC_IVAR_$_RTTripClusterMetadata._clusterOrder
+ _OBJC_IVAR_$_RTTripClusterMetadata._commuteID
+ _OBJC_IVAR_$_RTTripClusterMetadata._countOfTraversal
+ _OBJC_IVAR_$_RTTripClusterMetadata._dateOfMostRecentTrip
+ _OBJC_IVAR_$_RTTripClusterMetadata._destinationLatitude
+ _OBJC_IVAR_$_RTTripClusterMetadata._destinationLongitude
+ _OBJC_IVAR_$_RTTripClusterMetadata._isLocked
+ _OBJC_IVAR_$_RTTripClusterMetadata._maximumTripDistance
+ _OBJC_IVAR_$_RTTripClusterMetadata._maximumTripTime
+ _OBJC_IVAR_$_RTTripClusterMetadata._minimumTripDistance
+ _OBJC_IVAR_$_RTTripClusterMetadata._minimumTripTime
+ _OBJC_IVAR_$_RTTripClusterMetadata._modeOfTransport
+ _OBJC_IVAR_$_RTTripClusterMetadata._originLatitude
+ _OBJC_IVAR_$_RTTripClusterMetadata._originLongitude
+ _OBJC_IVAR_$_RTTripClusterMetadata._walkTraversalCount
+ _OBJC_IVAR_$_RTTripClusterMetadataFetchOptions._destinationVisitLatitude
+ _OBJC_IVAR_$_RTTripClusterMetadataFetchOptions._destinationVisitLongitude
+ _OBJC_IVAR_$_RTTripClusterMetadataFetchOptions._originVisitLatitude
+ _OBJC_IVAR_$_RTTripClusterMetadataFetchOptions._originVisitLongitude
+ _OBJC_IVAR_$_RTTripClusterRecencyEnumerationContext._offset
+ _OBJC_IVAR_$_RTTripClusterRecencyEnumerationContext._options
+ _OBJC_IVAR_$_RTTripClusterRoadTransitionsEnumerationContext._offset
+ _OBJC_IVAR_$_RTTripClusterRoadTransitionsEnumerationContext._options
+ _OBJC_IVAR_$_RTTripClusterRouteEnumerationContext._offset
+ _OBJC_IVAR_$_RTTripClusterRouteEnumerationContext._options
+ _OBJC_IVAR_$_RTTripClusterScheduleEnumerationContext._offset
+ _OBJC_IVAR_$_RTTripClusterScheduleEnumerationContext._options
+ _OBJC_IVAR_$_RTTripSegment._destinationLatitude
+ _OBJC_IVAR_$_RTTripSegment._destinationLongitude
+ _OBJC_IVAR_$_RTTripSegment._isConsumedByClustering
+ _OBJC_IVAR_$_RTTripSegment._originLatitude
+ _OBJC_IVAR_$_RTTripSegment._originLongitude
+ _OBJC_IVAR_$_RTTripSegment._tripCommuteID
+ _OBJC_IVAR_$_RTTripSegment._tripSegmentSequence
+ _OBJC_IVAR_$_RTTripSegment._tripSegmentSequenceMax
+ _OBJC_IVAR_$_RTUserCuration._curatedLabel
+ _OBJC_IVAR_$_RTUserCuration._expirationDate
+ _OBJC_IVAR_$_RTUserCuration._identifier
+ _OBJC_IVAR_$_RTUserCuration._submissionDate
+ _OBJC_IVAR_$_RTUserCuration._visitEntryDate
+ _OBJC_IVAR_$_RTUserCuration._visitExitDate
+ _OBJC_IVAR_$_RTVisit._identifier
+ _OBJC_METACLASS_$_RTAuthorizedLocationConfirmationStatusEnumerationContext
+ _OBJC_METACLASS_$_RTAuthorizedLocationConfirmationStatusEnumerationOptions
+ _OBJC_METACLASS_$_RTAuthorizedLocationDiagnosticStatus
+ _OBJC_METACLASS_$_RTAuthorizedLocationZDRLocationsEnumerationContext
+ _OBJC_METACLASS_$_RTAuthorizedLocationZDRLocationsEnumerationOptions
+ _OBJC_METACLASS_$_RTBluePOIMetadata
+ _OBJC_METACLASS_$_RTBluePOITile
+ _OBJC_METACLASS_$_RTBluePOITileDownloadResult
+ _OBJC_METACLASS_$_RTGeoRoadDataEnumerationContext
+ _OBJC_METACLASS_$_RTGeoRoadDataEnumerationOptions
+ _OBJC_METACLASS_$_RTLearnedRoute
+ _OBJC_METACLASS_$_RTLearnedRouteFetchOptions
+ _OBJC_METACLASS_$_RTLearnedRouteLocation
+ _OBJC_METACLASS_$_RTLearnedRouteMetrics
+ _OBJC_METACLASS_$_RTLearnedRouteTravelMode
+ _OBJC_METACLASS_$_RTLocalBluePOIResult
+ _OBJC_METACLASS_$_RTLocationsFromCoreLocationFetchOptions
+ _OBJC_METACLASS_$_RTPointOfInterest
+ _OBJC_METACLASS_$_RTPredictedContext
+ _OBJC_METACLASS_$_RTPredictedContextAnalytics
+ _OBJC_METACLASS_$_RTPredictedContextAnalyticsRolledLOIResult
+ _OBJC_METACLASS_$_RTPredictedContextDate
+ _OBJC_METACLASS_$_RTPredictedContextDateInterval
+ _OBJC_METACLASS_$_RTPredictedContextLocation
+ _OBJC_METACLASS_$_RTPredictedContextOptions
+ _OBJC_METACLASS_$_RTPredictedContextRequest
+ _OBJC_METACLASS_$_RTPredictedContextResult
+ _OBJC_METACLASS_$_RTPredictedContextSequence
+ _OBJC_METACLASS_$_RTPredictedContextTransition
+ _OBJC_METACLASS_$_RTPredictedContextTransport
+ _OBJC_METACLASS_$_RTPredictedContextWorkout
+ _OBJC_METACLASS_$_RTSourceHealthKitWorkout
+ _OBJC_METACLASS_$_RTSourceHomeKit
+ _OBJC_METACLASS_$_RTSourceParkedCar
+ _OBJC_METACLASS_$_RTSourcePropagatedLocation
+ _OBJC_METACLASS_$_RTStoredUserCurationFetchOptions
+ _OBJC_METACLASS_$_RTTripClusterEnumerationContext
+ _OBJC_METACLASS_$_RTTripClusterEnumerationOptions
+ _OBJC_METACLASS_$_RTTripClusterMetadata
+ _OBJC_METACLASS_$_RTTripClusterMetadataFetchOptions
+ _OBJC_METACLASS_$_RTTripClusterRecencyEnumerationContext
+ _OBJC_METACLASS_$_RTTripClusterRecencyEnumerationOptions
+ _OBJC_METACLASS_$_RTTripClusterRoadTransitionsEnumerationContext
+ _OBJC_METACLASS_$_RTTripClusterRoadTransitionsEnumerationOptions
+ _OBJC_METACLASS_$_RTTripClusterRouteEnumerationContext
+ _OBJC_METACLASS_$_RTTripClusterRouteEnumerationOptions
+ _OBJC_METACLASS_$_RTTripClusterScheduleEnumerationContext
+ _OBJC_METACLASS_$_RTTripClusterScheduleEnumerationOptions
+ _OBJC_METACLASS_$_RTUserCuration
+ _RTLogFacilityPredictedContext
+ _RTLogFacilityUserCuration
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_NSUUID_$_RTExtensions
+ __OBJC_$_CLASS_METHODS_RTAuthorizedLocationConfirmationStatusEnumerationContext
+ __OBJC_$_CLASS_METHODS_RTAuthorizedLocationDiagnosticStatus
+ __OBJC_$_CLASS_METHODS_RTAuthorizedLocationZDRLocationsEnumerationContext
+ __OBJC_$_CLASS_METHODS_RTBluePOIMetadata
+ __OBJC_$_CLASS_METHODS_RTBluePOITile
+ __OBJC_$_CLASS_METHODS_RTBluePOITileDownloadResult
+ __OBJC_$_CLASS_METHODS_RTGeoRoadDataEnumerationContext
+ __OBJC_$_CLASS_METHODS_RTGeoRoadDataEnumerationOptions
+ __OBJC_$_CLASS_METHODS_RTLearnedRoute
+ __OBJC_$_CLASS_METHODS_RTLearnedRouteFetchOptions
+ __OBJC_$_CLASS_METHODS_RTLearnedRouteLocation
+ __OBJC_$_CLASS_METHODS_RTLearnedRouteMetrics
+ __OBJC_$_CLASS_METHODS_RTLearnedRouteTravelMode
+ __OBJC_$_CLASS_METHODS_RTLocalBluePOIResult
+ __OBJC_$_CLASS_METHODS_RTLocationsFromCoreLocationFetchOptions
+ __OBJC_$_CLASS_METHODS_RTPointOfInterest
+ __OBJC_$_CLASS_METHODS_RTPredictedContext
+ __OBJC_$_CLASS_METHODS_RTPredictedContextAnalytics
+ __OBJC_$_CLASS_METHODS_RTPredictedContextAnalyticsRolledLOIResult
+ __OBJC_$_CLASS_METHODS_RTPredictedContextDate
+ __OBJC_$_CLASS_METHODS_RTPredictedContextDateInterval
+ __OBJC_$_CLASS_METHODS_RTPredictedContextLocation
+ __OBJC_$_CLASS_METHODS_RTPredictedContextOptions
+ __OBJC_$_CLASS_METHODS_RTPredictedContextRequest
+ __OBJC_$_CLASS_METHODS_RTPredictedContextResult
+ __OBJC_$_CLASS_METHODS_RTPredictedContextSequence
+ __OBJC_$_CLASS_METHODS_RTPredictedContextTransition
+ __OBJC_$_CLASS_METHODS_RTPredictedContextTransport
+ __OBJC_$_CLASS_METHODS_RTPredictedContextWorkout
+ __OBJC_$_CLASS_METHODS_RTSourceHealthKitWorkout
+ __OBJC_$_CLASS_METHODS_RTSourceHomeKit
+ __OBJC_$_CLASS_METHODS_RTSourceParkedCar
+ __OBJC_$_CLASS_METHODS_RTSourcePropagatedLocation
+ __OBJC_$_CLASS_METHODS_RTStoredUserCurationFetchOptions
+ __OBJC_$_CLASS_METHODS_RTTripClusterEnumerationContext
+ __OBJC_$_CLASS_METHODS_RTTripClusterEnumerationOptions
+ __OBJC_$_CLASS_METHODS_RTTripClusterMetadata
+ __OBJC_$_CLASS_METHODS_RTTripClusterMetadataFetchOptions
+ __OBJC_$_CLASS_METHODS_RTTripClusterRecencyEnumerationContext
+ __OBJC_$_CLASS_METHODS_RTTripClusterRecencyEnumerationOptions
+ __OBJC_$_CLASS_METHODS_RTTripClusterRoadTransitionsEnumerationContext
+ __OBJC_$_CLASS_METHODS_RTTripClusterRoadTransitionsEnumerationOptions
+ __OBJC_$_CLASS_METHODS_RTTripClusterRouteEnumerationContext
+ __OBJC_$_CLASS_METHODS_RTTripClusterRouteEnumerationOptions
+ __OBJC_$_CLASS_METHODS_RTTripClusterScheduleEnumerationContext
+ __OBJC_$_CLASS_METHODS_RTTripClusterScheduleEnumerationOptions
+ __OBJC_$_CLASS_METHODS_RTUserCuration
+ __OBJC_$_CLASS_PROP_LIST_RTAuthorizedLocationConfirmationStatusEnumerationContext
+ __OBJC_$_CLASS_PROP_LIST_RTAuthorizedLocationDiagnosticStatus
+ __OBJC_$_CLASS_PROP_LIST_RTAuthorizedLocationZDRLocationsEnumerationContext
+ __OBJC_$_CLASS_PROP_LIST_RTBluePOIMetadata
+ __OBJC_$_CLASS_PROP_LIST_RTBluePOITile
+ __OBJC_$_CLASS_PROP_LIST_RTBluePOITileDownloadResult
+ __OBJC_$_CLASS_PROP_LIST_RTGeoRoadDataEnumerationContext
+ __OBJC_$_CLASS_PROP_LIST_RTLearnedRoute
+ __OBJC_$_CLASS_PROP_LIST_RTLearnedRouteFetchOptions
+ __OBJC_$_CLASS_PROP_LIST_RTLearnedRouteLocation
+ __OBJC_$_CLASS_PROP_LIST_RTLearnedRouteMetrics
+ __OBJC_$_CLASS_PROP_LIST_RTLearnedRouteTravelMode
+ __OBJC_$_CLASS_PROP_LIST_RTLocalBluePOIResult
+ __OBJC_$_CLASS_PROP_LIST_RTLocationsFromCoreLocationFetchOptions
+ __OBJC_$_CLASS_PROP_LIST_RTPointOfInterest
+ __OBJC_$_CLASS_PROP_LIST_RTPredictedContext
+ __OBJC_$_CLASS_PROP_LIST_RTPredictedContextAnalytics
+ __OBJC_$_CLASS_PROP_LIST_RTPredictedContextAnalyticsRolledLOIResult
+ __OBJC_$_CLASS_PROP_LIST_RTPredictedContextDate
+ __OBJC_$_CLASS_PROP_LIST_RTPredictedContextDateInterval
+ __OBJC_$_CLASS_PROP_LIST_RTPredictedContextOptions
+ __OBJC_$_CLASS_PROP_LIST_RTPredictedContextRequest
+ __OBJC_$_CLASS_PROP_LIST_RTPredictedContextResult
+ __OBJC_$_CLASS_PROP_LIST_RTPredictedContextSequence
+ __OBJC_$_CLASS_PROP_LIST_RTPredictedContextTransition
+ __OBJC_$_CLASS_PROP_LIST_RTPredictedContextTransport
+ __OBJC_$_CLASS_PROP_LIST_RTStoredUserCurationFetchOptions
+ __OBJC_$_CLASS_PROP_LIST_RTTripClusterEnumerationContext
+ __OBJC_$_CLASS_PROP_LIST_RTTripClusterMetadata
+ __OBJC_$_CLASS_PROP_LIST_RTTripClusterMetadataFetchOptions
+ __OBJC_$_CLASS_PROP_LIST_RTTripClusterRecencyEnumerationContext
+ __OBJC_$_CLASS_PROP_LIST_RTTripClusterRoadTransitionsEnumerationContext
+ __OBJC_$_CLASS_PROP_LIST_RTTripClusterRouteEnumerationContext
+ __OBJC_$_CLASS_PROP_LIST_RTTripClusterScheduleEnumerationContext
+ __OBJC_$_CLASS_PROP_LIST_RTUserCuration
+ __OBJC_$_INSTANCE_METHODS_RTAuthorizedLocationConfirmationStatusEnumerationContext
+ __OBJC_$_INSTANCE_METHODS_RTAuthorizedLocationConfirmationStatusEnumerationOptions
+ __OBJC_$_INSTANCE_METHODS_RTAuthorizedLocationDiagnosticStatus
+ __OBJC_$_INSTANCE_METHODS_RTAuthorizedLocationZDRLocationsEnumerationContext
+ __OBJC_$_INSTANCE_METHODS_RTAuthorizedLocationZDRLocationsEnumerationOptions
+ __OBJC_$_INSTANCE_METHODS_RTBluePOIMetadata
+ __OBJC_$_INSTANCE_METHODS_RTBluePOITile
+ __OBJC_$_INSTANCE_METHODS_RTBluePOITileDownloadResult
+ __OBJC_$_INSTANCE_METHODS_RTGeoRoadDataEnumerationContext
+ __OBJC_$_INSTANCE_METHODS_RTGeoRoadDataEnumerationOptions
+ __OBJC_$_INSTANCE_METHODS_RTLearnedRoute
+ __OBJC_$_INSTANCE_METHODS_RTLearnedRouteFetchOptions
+ __OBJC_$_INSTANCE_METHODS_RTLearnedRouteLocation
+ __OBJC_$_INSTANCE_METHODS_RTLearnedRouteMetrics
+ __OBJC_$_INSTANCE_METHODS_RTLearnedRouteTravelMode
+ __OBJC_$_INSTANCE_METHODS_RTLocalBluePOIResult
+ __OBJC_$_INSTANCE_METHODS_RTLocationsFromCoreLocationFetchOptions
+ __OBJC_$_INSTANCE_METHODS_RTPointOfInterest
+ __OBJC_$_INSTANCE_METHODS_RTPredictedContext
+ __OBJC_$_INSTANCE_METHODS_RTPredictedContextAnalytics
+ __OBJC_$_INSTANCE_METHODS_RTPredictedContextAnalyticsRolledLOIResult
+ __OBJC_$_INSTANCE_METHODS_RTPredictedContextDate
+ __OBJC_$_INSTANCE_METHODS_RTPredictedContextDateInterval
+ __OBJC_$_INSTANCE_METHODS_RTPredictedContextLocation
+ __OBJC_$_INSTANCE_METHODS_RTPredictedContextOptions
+ __OBJC_$_INSTANCE_METHODS_RTPredictedContextRequest
+ __OBJC_$_INSTANCE_METHODS_RTPredictedContextResult
+ __OBJC_$_INSTANCE_METHODS_RTPredictedContextSequence
+ __OBJC_$_INSTANCE_METHODS_RTPredictedContextTransition
+ __OBJC_$_INSTANCE_METHODS_RTPredictedContextTransport
+ __OBJC_$_INSTANCE_METHODS_RTPredictedContextWorkout
+ __OBJC_$_INSTANCE_METHODS_RTSourceHealthKitWorkout
+ __OBJC_$_INSTANCE_METHODS_RTSourceHomeKit
+ __OBJC_$_INSTANCE_METHODS_RTSourceParkedCar
+ __OBJC_$_INSTANCE_METHODS_RTSourcePropagatedLocation
+ __OBJC_$_INSTANCE_METHODS_RTStoredUserCurationFetchOptions
+ __OBJC_$_INSTANCE_METHODS_RTTripClusterEnumerationContext
+ __OBJC_$_INSTANCE_METHODS_RTTripClusterEnumerationOptions
+ __OBJC_$_INSTANCE_METHODS_RTTripClusterMetadata
+ __OBJC_$_INSTANCE_METHODS_RTTripClusterMetadataFetchOptions
+ __OBJC_$_INSTANCE_METHODS_RTTripClusterRecencyEnumerationContext
+ __OBJC_$_INSTANCE_METHODS_RTTripClusterRecencyEnumerationOptions
+ __OBJC_$_INSTANCE_METHODS_RTTripClusterRoadTransitionsEnumerationContext
+ __OBJC_$_INSTANCE_METHODS_RTTripClusterRoadTransitionsEnumerationOptions
+ __OBJC_$_INSTANCE_METHODS_RTTripClusterRouteEnumerationContext
+ __OBJC_$_INSTANCE_METHODS_RTTripClusterRouteEnumerationOptions
+ __OBJC_$_INSTANCE_METHODS_RTTripClusterScheduleEnumerationContext
+ __OBJC_$_INSTANCE_METHODS_RTTripClusterScheduleEnumerationOptions
+ __OBJC_$_INSTANCE_METHODS_RTUserCuration
+ __OBJC_$_INSTANCE_VARIABLES_RTAuthorizedLocationConfirmationStatusEnumerationContext
+ __OBJC_$_INSTANCE_VARIABLES_RTAuthorizedLocationConfirmationStatusEnumerationOptions
+ __OBJC_$_INSTANCE_VARIABLES_RTAuthorizedLocationDiagnosticStatus
+ __OBJC_$_INSTANCE_VARIABLES_RTAuthorizedLocationZDRLocationsEnumerationContext
+ __OBJC_$_INSTANCE_VARIABLES_RTAuthorizedLocationZDRLocationsEnumerationOptions
+ __OBJC_$_INSTANCE_VARIABLES_RTBluePOIMetadata
+ __OBJC_$_INSTANCE_VARIABLES_RTBluePOITile
+ __OBJC_$_INSTANCE_VARIABLES_RTBluePOITileDownloadResult
+ __OBJC_$_INSTANCE_VARIABLES_RTGeoRoadDataEnumerationContext
+ __OBJC_$_INSTANCE_VARIABLES_RTGeoRoadDataEnumerationOptions
+ __OBJC_$_INSTANCE_VARIABLES_RTLearnedRoute
+ __OBJC_$_INSTANCE_VARIABLES_RTLearnedRouteFetchOptions
+ __OBJC_$_INSTANCE_VARIABLES_RTLearnedRouteLocation
+ __OBJC_$_INSTANCE_VARIABLES_RTLearnedRouteMetrics
+ __OBJC_$_INSTANCE_VARIABLES_RTLearnedRouteTravelMode
+ __OBJC_$_INSTANCE_VARIABLES_RTLocalBluePOIResult
+ __OBJC_$_INSTANCE_VARIABLES_RTLocationsFromCoreLocationFetchOptions
+ __OBJC_$_INSTANCE_VARIABLES_RTPointOfInterest
+ __OBJC_$_INSTANCE_VARIABLES_RTPredictedContext
+ __OBJC_$_INSTANCE_VARIABLES_RTPredictedContextAnalytics
+ __OBJC_$_INSTANCE_VARIABLES_RTPredictedContextAnalyticsRolledLOIResult
+ __OBJC_$_INSTANCE_VARIABLES_RTPredictedContextDate
+ __OBJC_$_INSTANCE_VARIABLES_RTPredictedContextDateInterval
+ __OBJC_$_INSTANCE_VARIABLES_RTPredictedContextLocation
+ __OBJC_$_INSTANCE_VARIABLES_RTPredictedContextOptions
+ __OBJC_$_INSTANCE_VARIABLES_RTPredictedContextRequest
+ __OBJC_$_INSTANCE_VARIABLES_RTPredictedContextResult
+ __OBJC_$_INSTANCE_VARIABLES_RTPredictedContextSequence
+ __OBJC_$_INSTANCE_VARIABLES_RTPredictedContextTransition
+ __OBJC_$_INSTANCE_VARIABLES_RTPredictedContextTransport
+ __OBJC_$_INSTANCE_VARIABLES_RTPredictedContextWorkout
+ __OBJC_$_INSTANCE_VARIABLES_RTSourceHealthKitWorkout
+ __OBJC_$_INSTANCE_VARIABLES_RTSourceHomeKit
+ __OBJC_$_INSTANCE_VARIABLES_RTSourceParkedCar
+ __OBJC_$_INSTANCE_VARIABLES_RTSourcePropagatedLocation
+ __OBJC_$_INSTANCE_VARIABLES_RTStoredUserCurationFetchOptions
+ __OBJC_$_INSTANCE_VARIABLES_RTTripClusterEnumerationContext
+ __OBJC_$_INSTANCE_VARIABLES_RTTripClusterEnumerationOptions
+ __OBJC_$_INSTANCE_VARIABLES_RTTripClusterMetadata
+ __OBJC_$_INSTANCE_VARIABLES_RTTripClusterMetadataFetchOptions
+ __OBJC_$_INSTANCE_VARIABLES_RTTripClusterRecencyEnumerationContext
+ __OBJC_$_INSTANCE_VARIABLES_RTTripClusterRecencyEnumerationOptions
+ __OBJC_$_INSTANCE_VARIABLES_RTTripClusterRoadTransitionsEnumerationContext
+ __OBJC_$_INSTANCE_VARIABLES_RTTripClusterRoadTransitionsEnumerationOptions
+ __OBJC_$_INSTANCE_VARIABLES_RTTripClusterRouteEnumerationContext
+ __OBJC_$_INSTANCE_VARIABLES_RTTripClusterRouteEnumerationOptions
+ __OBJC_$_INSTANCE_VARIABLES_RTTripClusterScheduleEnumerationContext
+ __OBJC_$_INSTANCE_VARIABLES_RTTripClusterScheduleEnumerationOptions
+ __OBJC_$_INSTANCE_VARIABLES_RTUserCuration
+ __OBJC_$_PROP_LIST_RTAuthorizedLocationConfirmationStatusEnumerationContext
+ __OBJC_$_PROP_LIST_RTAuthorizedLocationConfirmationStatusEnumerationOptions
+ __OBJC_$_PROP_LIST_RTAuthorizedLocationDiagnosticStatus
+ __OBJC_$_PROP_LIST_RTAuthorizedLocationZDRLocationsEnumerationContext
+ __OBJC_$_PROP_LIST_RTAuthorizedLocationZDRLocationsEnumerationOptions
+ __OBJC_$_PROP_LIST_RTBluePOIMetadata
+ __OBJC_$_PROP_LIST_RTBluePOITile
+ __OBJC_$_PROP_LIST_RTBluePOITileDownloadResult
+ __OBJC_$_PROP_LIST_RTGeoRoadDataEnumerationContext
+ __OBJC_$_PROP_LIST_RTGeoRoadDataEnumerationOptions
+ __OBJC_$_PROP_LIST_RTLearnedRoute
+ __OBJC_$_PROP_LIST_RTLearnedRouteFetchOptions
+ __OBJC_$_PROP_LIST_RTLearnedRouteLocation
+ __OBJC_$_PROP_LIST_RTLearnedRouteMetrics
+ __OBJC_$_PROP_LIST_RTLearnedRouteTravelMode
+ __OBJC_$_PROP_LIST_RTLocalBluePOIResult
+ __OBJC_$_PROP_LIST_RTLocationsFromCoreLocationFetchOptions
+ __OBJC_$_PROP_LIST_RTPointOfInterest
+ __OBJC_$_PROP_LIST_RTPredictedContext
+ __OBJC_$_PROP_LIST_RTPredictedContextAnalytics
+ __OBJC_$_PROP_LIST_RTPredictedContextAnalyticsRolledLOIResult
+ __OBJC_$_PROP_LIST_RTPredictedContextDate
+ __OBJC_$_PROP_LIST_RTPredictedContextDateInterval
+ __OBJC_$_PROP_LIST_RTPredictedContextLocation
+ __OBJC_$_PROP_LIST_RTPredictedContextOptions
+ __OBJC_$_PROP_LIST_RTPredictedContextRequest
+ __OBJC_$_PROP_LIST_RTPredictedContextResult
+ __OBJC_$_PROP_LIST_RTPredictedContextSequence
+ __OBJC_$_PROP_LIST_RTPredictedContextTransition
+ __OBJC_$_PROP_LIST_RTPredictedContextTransport
+ __OBJC_$_PROP_LIST_RTPredictedContextWorkout
+ __OBJC_$_PROP_LIST_RTSourceHealthKitWorkout
+ __OBJC_$_PROP_LIST_RTSourceHomeKit
+ __OBJC_$_PROP_LIST_RTSourceParkedCar
+ __OBJC_$_PROP_LIST_RTSourcePropagatedLocation
+ __OBJC_$_PROP_LIST_RTStoredUserCurationFetchOptions
+ __OBJC_$_PROP_LIST_RTTripClusterEnumerationContext
+ __OBJC_$_PROP_LIST_RTTripClusterEnumerationOptions
+ __OBJC_$_PROP_LIST_RTTripClusterMetadata
+ __OBJC_$_PROP_LIST_RTTripClusterMetadataFetchOptions
+ __OBJC_$_PROP_LIST_RTTripClusterRecencyEnumerationContext
+ __OBJC_$_PROP_LIST_RTTripClusterRecencyEnumerationOptions
+ __OBJC_$_PROP_LIST_RTTripClusterRoadTransitionsEnumerationContext
+ __OBJC_$_PROP_LIST_RTTripClusterRoadTransitionsEnumerationOptions
+ __OBJC_$_PROP_LIST_RTTripClusterRouteEnumerationContext
+ __OBJC_$_PROP_LIST_RTTripClusterRouteEnumerationOptions
+ __OBJC_$_PROP_LIST_RTTripClusterScheduleEnumerationContext
+ __OBJC_$_PROP_LIST_RTTripClusterScheduleEnumerationOptions
+ __OBJC_$_PROP_LIST_RTUserCuration
+ __OBJC_CLASS_PROTOCOLS_$_RTAuthorizedLocationConfirmationStatusEnumerationContext
+ __OBJC_CLASS_PROTOCOLS_$_RTAuthorizedLocationConfirmationStatusEnumerationOptions
+ __OBJC_CLASS_PROTOCOLS_$_RTAuthorizedLocationDiagnosticStatus
+ __OBJC_CLASS_PROTOCOLS_$_RTAuthorizedLocationZDRLocationsEnumerationContext
+ __OBJC_CLASS_PROTOCOLS_$_RTAuthorizedLocationZDRLocationsEnumerationOptions
+ __OBJC_CLASS_PROTOCOLS_$_RTBluePOIMetadata
+ __OBJC_CLASS_PROTOCOLS_$_RTBluePOITile
+ __OBJC_CLASS_PROTOCOLS_$_RTBluePOITileDownloadResult
+ __OBJC_CLASS_PROTOCOLS_$_RTGeoRoadDataEnumerationContext
+ __OBJC_CLASS_PROTOCOLS_$_RTGeoRoadDataEnumerationOptions
+ __OBJC_CLASS_PROTOCOLS_$_RTLearnedRoute
+ __OBJC_CLASS_PROTOCOLS_$_RTLearnedRouteFetchOptions
+ __OBJC_CLASS_PROTOCOLS_$_RTLearnedRouteLocation
+ __OBJC_CLASS_PROTOCOLS_$_RTLearnedRouteMetrics
+ __OBJC_CLASS_PROTOCOLS_$_RTLearnedRouteTravelMode
+ __OBJC_CLASS_PROTOCOLS_$_RTLocalBluePOIResult
+ __OBJC_CLASS_PROTOCOLS_$_RTLocationsFromCoreLocationFetchOptions
+ __OBJC_CLASS_PROTOCOLS_$_RTPointOfInterest
+ __OBJC_CLASS_PROTOCOLS_$_RTPredictedContext
+ __OBJC_CLASS_PROTOCOLS_$_RTPredictedContextAnalytics
+ __OBJC_CLASS_PROTOCOLS_$_RTPredictedContextAnalyticsRolledLOIResult
+ __OBJC_CLASS_PROTOCOLS_$_RTPredictedContextDate
+ __OBJC_CLASS_PROTOCOLS_$_RTPredictedContextDateInterval
+ __OBJC_CLASS_PROTOCOLS_$_RTPredictedContextLocation
+ __OBJC_CLASS_PROTOCOLS_$_RTPredictedContextOptions
+ __OBJC_CLASS_PROTOCOLS_$_RTPredictedContextRequest
+ __OBJC_CLASS_PROTOCOLS_$_RTPredictedContextResult
+ __OBJC_CLASS_PROTOCOLS_$_RTPredictedContextSequence
+ __OBJC_CLASS_PROTOCOLS_$_RTPredictedContextTransition
+ __OBJC_CLASS_PROTOCOLS_$_RTPredictedContextTransport
+ __OBJC_CLASS_PROTOCOLS_$_RTPredictedContextWorkout
+ __OBJC_CLASS_PROTOCOLS_$_RTStoredUserCurationFetchOptions
+ __OBJC_CLASS_PROTOCOLS_$_RTTripClusterEnumerationContext
+ __OBJC_CLASS_PROTOCOLS_$_RTTripClusterEnumerationOptions
+ __OBJC_CLASS_PROTOCOLS_$_RTTripClusterMetadata
+ __OBJC_CLASS_PROTOCOLS_$_RTTripClusterMetadataFetchOptions
+ __OBJC_CLASS_PROTOCOLS_$_RTTripClusterRecencyEnumerationContext
+ __OBJC_CLASS_PROTOCOLS_$_RTTripClusterRecencyEnumerationOptions
+ __OBJC_CLASS_PROTOCOLS_$_RTTripClusterRoadTransitionsEnumerationContext
+ __OBJC_CLASS_PROTOCOLS_$_RTTripClusterRoadTransitionsEnumerationOptions
+ __OBJC_CLASS_PROTOCOLS_$_RTTripClusterRouteEnumerationContext
+ __OBJC_CLASS_PROTOCOLS_$_RTTripClusterRouteEnumerationOptions
+ __OBJC_CLASS_PROTOCOLS_$_RTTripClusterScheduleEnumerationContext
+ __OBJC_CLASS_PROTOCOLS_$_RTTripClusterScheduleEnumerationOptions
+ __OBJC_CLASS_PROTOCOLS_$_RTUserCuration
+ __OBJC_CLASS_RO_$_RTAuthorizedLocationConfirmationStatusEnumerationContext
+ __OBJC_CLASS_RO_$_RTAuthorizedLocationConfirmationStatusEnumerationOptions
+ __OBJC_CLASS_RO_$_RTAuthorizedLocationDiagnosticStatus
+ __OBJC_CLASS_RO_$_RTAuthorizedLocationZDRLocationsEnumerationContext
+ __OBJC_CLASS_RO_$_RTAuthorizedLocationZDRLocationsEnumerationOptions
+ __OBJC_CLASS_RO_$_RTBluePOIMetadata
+ __OBJC_CLASS_RO_$_RTBluePOITile
+ __OBJC_CLASS_RO_$_RTBluePOITileDownloadResult
+ __OBJC_CLASS_RO_$_RTGeoRoadDataEnumerationContext
+ __OBJC_CLASS_RO_$_RTGeoRoadDataEnumerationOptions
+ __OBJC_CLASS_RO_$_RTLearnedRoute
+ __OBJC_CLASS_RO_$_RTLearnedRouteFetchOptions
+ __OBJC_CLASS_RO_$_RTLearnedRouteLocation
+ __OBJC_CLASS_RO_$_RTLearnedRouteMetrics
+ __OBJC_CLASS_RO_$_RTLearnedRouteTravelMode
+ __OBJC_CLASS_RO_$_RTLocalBluePOIResult
+ __OBJC_CLASS_RO_$_RTLocationsFromCoreLocationFetchOptions
+ __OBJC_CLASS_RO_$_RTPointOfInterest
+ __OBJC_CLASS_RO_$_RTPredictedContext
+ __OBJC_CLASS_RO_$_RTPredictedContextAnalytics
+ __OBJC_CLASS_RO_$_RTPredictedContextAnalyticsRolledLOIResult
+ __OBJC_CLASS_RO_$_RTPredictedContextDate
+ __OBJC_CLASS_RO_$_RTPredictedContextDateInterval
+ __OBJC_CLASS_RO_$_RTPredictedContextLocation
+ __OBJC_CLASS_RO_$_RTPredictedContextOptions
+ __OBJC_CLASS_RO_$_RTPredictedContextRequest
+ __OBJC_CLASS_RO_$_RTPredictedContextResult
+ __OBJC_CLASS_RO_$_RTPredictedContextSequence
+ __OBJC_CLASS_RO_$_RTPredictedContextTransition
+ __OBJC_CLASS_RO_$_RTPredictedContextTransport
+ __OBJC_CLASS_RO_$_RTPredictedContextWorkout
+ __OBJC_CLASS_RO_$_RTSourceHealthKitWorkout
+ __OBJC_CLASS_RO_$_RTSourceHomeKit
+ __OBJC_CLASS_RO_$_RTSourceParkedCar
+ __OBJC_CLASS_RO_$_RTSourcePropagatedLocation
+ __OBJC_CLASS_RO_$_RTStoredUserCurationFetchOptions
+ __OBJC_CLASS_RO_$_RTTripClusterEnumerationContext
+ __OBJC_CLASS_RO_$_RTTripClusterEnumerationOptions
+ __OBJC_CLASS_RO_$_RTTripClusterMetadata
+ __OBJC_CLASS_RO_$_RTTripClusterMetadataFetchOptions
+ __OBJC_CLASS_RO_$_RTTripClusterRecencyEnumerationContext
+ __OBJC_CLASS_RO_$_RTTripClusterRecencyEnumerationOptions
+ __OBJC_CLASS_RO_$_RTTripClusterRoadTransitionsEnumerationContext
+ __OBJC_CLASS_RO_$_RTTripClusterRoadTransitionsEnumerationOptions
+ __OBJC_CLASS_RO_$_RTTripClusterRouteEnumerationContext
+ __OBJC_CLASS_RO_$_RTTripClusterRouteEnumerationOptions
+ __OBJC_CLASS_RO_$_RTTripClusterScheduleEnumerationContext
+ __OBJC_CLASS_RO_$_RTTripClusterScheduleEnumerationOptions
+ __OBJC_CLASS_RO_$_RTUserCuration
+ __OBJC_METACLASS_RO_$_RTAuthorizedLocationConfirmationStatusEnumerationContext
+ __OBJC_METACLASS_RO_$_RTAuthorizedLocationConfirmationStatusEnumerationOptions
+ __OBJC_METACLASS_RO_$_RTAuthorizedLocationDiagnosticStatus
+ __OBJC_METACLASS_RO_$_RTAuthorizedLocationZDRLocationsEnumerationContext
+ __OBJC_METACLASS_RO_$_RTAuthorizedLocationZDRLocationsEnumerationOptions
+ __OBJC_METACLASS_RO_$_RTBluePOIMetadata
+ __OBJC_METACLASS_RO_$_RTBluePOITile
+ __OBJC_METACLASS_RO_$_RTBluePOITileDownloadResult
+ __OBJC_METACLASS_RO_$_RTGeoRoadDataEnumerationContext
+ __OBJC_METACLASS_RO_$_RTGeoRoadDataEnumerationOptions
+ __OBJC_METACLASS_RO_$_RTLearnedRoute
+ __OBJC_METACLASS_RO_$_RTLearnedRouteFetchOptions
+ __OBJC_METACLASS_RO_$_RTLearnedRouteLocation
+ __OBJC_METACLASS_RO_$_RTLearnedRouteMetrics
+ __OBJC_METACLASS_RO_$_RTLearnedRouteTravelMode
+ __OBJC_METACLASS_RO_$_RTLocalBluePOIResult
+ __OBJC_METACLASS_RO_$_RTLocationsFromCoreLocationFetchOptions
+ __OBJC_METACLASS_RO_$_RTPointOfInterest
+ __OBJC_METACLASS_RO_$_RTPredictedContext
+ __OBJC_METACLASS_RO_$_RTPredictedContextAnalytics
+ __OBJC_METACLASS_RO_$_RTPredictedContextAnalyticsRolledLOIResult
+ __OBJC_METACLASS_RO_$_RTPredictedContextDate
+ __OBJC_METACLASS_RO_$_RTPredictedContextDateInterval
+ __OBJC_METACLASS_RO_$_RTPredictedContextLocation
+ __OBJC_METACLASS_RO_$_RTPredictedContextOptions
+ __OBJC_METACLASS_RO_$_RTPredictedContextRequest
+ __OBJC_METACLASS_RO_$_RTPredictedContextResult
+ __OBJC_METACLASS_RO_$_RTPredictedContextSequence
+ __OBJC_METACLASS_RO_$_RTPredictedContextTransition
+ __OBJC_METACLASS_RO_$_RTPredictedContextTransport
+ __OBJC_METACLASS_RO_$_RTPredictedContextWorkout
+ __OBJC_METACLASS_RO_$_RTSourceHealthKitWorkout
+ __OBJC_METACLASS_RO_$_RTSourceHomeKit
+ __OBJC_METACLASS_RO_$_RTSourceParkedCar
+ __OBJC_METACLASS_RO_$_RTSourcePropagatedLocation
+ __OBJC_METACLASS_RO_$_RTStoredUserCurationFetchOptions
+ __OBJC_METACLASS_RO_$_RTTripClusterEnumerationContext
+ __OBJC_METACLASS_RO_$_RTTripClusterEnumerationOptions
+ __OBJC_METACLASS_RO_$_RTTripClusterMetadata
+ __OBJC_METACLASS_RO_$_RTTripClusterMetadataFetchOptions
+ __OBJC_METACLASS_RO_$_RTTripClusterRecencyEnumerationContext
+ __OBJC_METACLASS_RO_$_RTTripClusterRecencyEnumerationOptions
+ __OBJC_METACLASS_RO_$_RTTripClusterRoadTransitionsEnumerationContext
+ __OBJC_METACLASS_RO_$_RTTripClusterRoadTransitionsEnumerationOptions
+ __OBJC_METACLASS_RO_$_RTTripClusterRouteEnumerationContext
+ __OBJC_METACLASS_RO_$_RTTripClusterRouteEnumerationOptions
+ __OBJC_METACLASS_RO_$_RTTripClusterScheduleEnumerationContext
+ __OBJC_METACLASS_RO_$_RTTripClusterScheduleEnumerationOptions
+ __OBJC_METACLASS_RO_$_RTUserCuration
+ ___105-[RTRoutineManager fetchNextPredictedLocationsOfInterestFromLocation:startDate:timeInterval:withHandler:]_block_invoke_3
+ ___105-[RTRoutineManager fetchNextPredictedLocationsOfInterestFromLocation:startDate:timeInterval:withHandler:]_block_invoke_4
+ ___107-[RTRoutineManager userInteractionWithPredictedLocationOfInterest:interaction:feedback:geoMapItem:handler:]_block_invoke_4
+ ___111-[RTRoutineManager fetchPredictedLocationsOfInterestAssociatedToTitle:location:calendarIdentifier:withHandler:]_block_invoke_4
+ ___37+[RTPredictedContext maskForSources:]_block_invoke
+ ___37-[RTRoutineManager _createConnection]_block_invoke.413
+ ___38-[RTRoutineManager stopLeechingVisits]_block_invoke.469
+ ___38-[RTRoutineManager stopLeechingVisits]_block_invoke_2.470
+ ___38-[RTRoutineManager stopLeechingVisits]_block_invoke_3
+ ___40-[RTRoutineManager stopMonitoringVisits]_block_invoke.467
+ ___40-[RTRoutineManager stopMonitoringVisits]_block_invoke_2.468
+ ___40-[RTRoutineManager stopMonitoringVisits]_block_invoke_3
+ ___42-[RTRoutineManager addElevations:handler:]_block_invoke.556
+ ___42-[RTRoutineManager addElevations:handler:]_block_invoke_3
+ ___42-[RTRoutineManager clearAllVehicleEvents:]_block_invoke_4
+ ___44-[RTRoutineManager clearRoutineWithHandler:]_block_invoke_4
+ ___46-[RTRoutineManager fetchCurrentPeopleDensity:]_block_invoke_4
+ ___47+[NSDate(RTExtensions) dateFormatterForLogging]_block_invoke
+ ___49-[RTRoutineManager fetchRemoteStatusWithHandler:]_block_invoke_4
+ ___49-[RTRoutineManager fetchRoutineStateWithHandler:]_block_invoke.441
+ ___49-[RTRoutineManager fetchRoutineStateWithHandler:]_block_invoke_3
+ ___49-[RTRoutineManager stopMonitoringPlaceInferences]_block_invoke.475
+ ___49-[RTRoutineManager stopMonitoringPlaceInferences]_block_invoke_2.476
+ ___49-[RTRoutineManager stopMonitoringPlaceInferences]_block_invoke_3
+ ___50-[RTRoutineManager fetchAuthorizedLocationStatus:]_block_invoke_4
+ ___50-[RTRoutineManager purgeTripClusterTable:handler:]_block_invoke
+ ___50-[RTRoutineManager purgeTripClusterTable:handler:]_block_invoke_2
+ ___50-[RTRoutineManager purgeTripClusterTable:handler:]_block_invoke_3
+ ___50-[RTRoutineManager purgeTripClusterTable:handler:]_block_invoke_4
+ ___50-[RTRoutineManager setRoutineEnabled:withHandler:]_block_invoke_4
+ ___51-[RTRoutineManager fetchRoutineEnabledWithHandler:]_block_invoke.439
+ ___51-[RTRoutineManager fetchRoutineEnabledWithHandler:]_block_invoke_3
+ ___51-[RTRoutineManager startLeechingVisitsWithHandler:]_block_invoke_5
+ ___51-[RTRoutineManager stopLeechingLowConfidenceVisits]_block_invoke.471
+ ___51-[RTRoutineManager stopLeechingLowConfidenceVisits]_block_invoke_2.472
+ ___51-[RTRoutineManager stopLeechingLowConfidenceVisits]_block_invoke_3
+ ___52-[RTRoutineManagerExportedObject onVisit:withError:]_block_invoke
+ ___53-[RTRoutineManager clearAllVehicleEventsWithHandler:]_block_invoke.513
+ ___53-[RTRoutineManager clearAllVehicleEventsWithHandler:]_block_invoke.514
+ ___53-[RTRoutineManager fetchCloudSyncAuthorizationState:]_block_invoke_4
+ ___53-[RTRoutineManager fetchElevationsWithOptions:reply:]_block_invoke.557
+ ___53-[RTRoutineManager fetchElevationsWithOptions:reply:]_block_invoke_3
+ ___53-[RTRoutineManager fetchVehiclesWithOptions:handler:]_block_invoke_4
+ ___53-[RTRoutineManager startMonitoringVisitsWithHandler:]_block_invoke_5
+ ___54-[RTPredictedContextResult nextStepPredictedContexts:]_block_invoke
+ ___54-[RTRoutineManager deleteTripSegmentWithUUID:handler:]_block_invoke_4
+ ___54-[RTRoutineManager fetchLastVehicleEventsWithHandler:]_block_invoke_4
+ ___54-[RTRoutineManager processHindsightVisitsWithHandler:]_block_invoke_3
+ ___54-[RTRoutineManager processHindsightVisitsWithHandler:]_block_invoke_4
+ ___54-[RTRoutineManager removeVisitWithIdentifier:handler:]_block_invoke_4
+ ___56+[RTSignalGeneratorOptions visitsDescriptionDataAtPath:]_block_invoke.89
+ ___56+[RTSignalGeneratorOptions visitsDescriptionDataAtPath:]_block_invoke.91
+ ___56+[RTSignalGeneratorOptions visitsDescriptionDataAtPath:]_block_invoke.95
+ ___56+[RTSignalGeneratorOptions visitsDescriptionDataAtPath:]_block_invoke_2.90
+ ___56+[RTSignalGeneratorOptions visitsDescriptionDataAtPath:]_block_invoke_2.96
+ ___56-[RTRoutineManager stopMonitoringScenarioTriggerOfType:]_block_invoke.490
+ ___56-[RTRoutineManager stopMonitoringScenarioTriggerOfType:]_block_invoke_2.491
+ ___56-[RTRoutineManager stopMonitoringScenarioTriggerOfType:]_block_invoke_3
+ ___56-[RTRoutineManagerExportedObject onDensityUpdate:error:]_block_invoke
+ ___56-[RTRoutineManagerExportedObject onVehicleEvents:error:]_block_invoke
+ ___57-[RTRoutineManager enumerateElevationsWithOptions:reply:]_block_invoke
+ ___57-[RTRoutineManager fetchEstimatedLocationAtDate:handler:]_block_invoke_4
+ ___57-[RTRoutineManager fetchStoredVisitsWithOptions:handler:]_block_invoke_4
+ ___57-[RTRoutineManager fetchTripSegmentsWithOptions:handler:]_block_invoke_4
+ ___57-[RTRoutineManager vehicleEventAtLocation:notes:handler:]_block_invoke_4
+ ___58-[RTRoutineManager _enumerateElevationsWithOptions:reply:]_block_invoke
+ ___58-[RTRoutineManager _enumerateElevationsWithOptions:reply:]_block_invoke.558
+ ___58-[RTRoutineManager _enumerateElevationsWithOptions:reply:]_block_invoke.561
+ ___58-[RTRoutineManager fetchLearnedRoutesWithOptions:handler:]_block_invoke
+ ___58-[RTRoutineManager fetchLearnedRoutesWithOptions:handler:]_block_invoke_2
+ ___58-[RTRoutineManager fetchLearnedRoutesWithOptions:handler:]_block_invoke_3
+ ___58-[RTRoutineManager fetchLearnedRoutesWithOptions:handler:]_block_invoke_4
+ ___58-[RTRoutineManager purgeTripClusterWithClusterID:handler:]_block_invoke
+ ___58-[RTRoutineManager purgeTripClusterWithClusterID:handler:]_block_invoke_2
+ ___58-[RTRoutineManager purgeTripClusterWithClusterID:handler:]_block_invoke_3
+ ___58-[RTRoutineManager purgeTripClusterWithClusterID:handler:]_block_invoke_4
+ ___58-[RTRoutineManager stopMonitoringRemoteStatusWithHandler:]_block_invoke
+ ___58-[RTRoutineManager stopMonitoringRemoteStatusWithHandler:]_block_invoke.447
+ ___58-[RTRoutineManager stopMonitoringRemoteStatusWithHandler:]_block_invoke_2
+ ___58-[RTRoutineManager stopMonitoringRemoteStatusWithHandler:]_block_invoke_2.448
+ ___58-[RTRoutineManager stopMonitoringRemoteStatusWithHandler:]_block_invoke_3
+ ___58-[RTRoutineManagerExportedObject onPlaceInferences:error:]_block_invoke
+ ___59-[RTPredictedContextResult predictedSequencesAfterContext:]_block_invoke
+ ___59-[RTRoutineManager enumerateObjectsWithOptions:usingBlock:]_block_invoke.459
+ ___59-[RTRoutineManager startMonitoringRemoteStatusWithHandler:]_block_invoke
+ ___59-[RTRoutineManager startMonitoringRemoteStatusWithHandler:]_block_invoke.444
+ ___59-[RTRoutineManager startMonitoringRemoteStatusWithHandler:]_block_invoke_2
+ ___59-[RTRoutineManager startMonitoringRemoteStatusWithHandler:]_block_invoke_2.445
+ ___59-[RTRoutineManager startMonitoringRemoteStatusWithHandler:]_block_invoke_3
+ ___59-[RTRoutineManagerExportedObject onLeechedVisit:withError:]_block_invoke
+ ___60-[RTRoutineManager fetchFormattedPostalAddressesFromMeCard:]_block_invoke_3
+ ___60-[RTRoutineManager fetchFormattedPostalAddressesFromMeCard:]_block_invoke_4
+ ___60-[RTRoutineManager fetchPlaceInferencesWithOptions:handler:]_block_invoke_3
+ ___60-[RTRoutineManager fetchPlaceInferencesWithOptions:handler:]_block_invoke_4
+ ___61-[RTPredictedContextResult currentPredictedContextsWithType:]_block_invoke
+ ___61-[RTRoutineManager fetchRoutineModeFromLocation:withHandler:]_block_invoke_4
+ ___61-[RTRoutineManagerExportedObject onRemoteStatusUpdate:error:]_block_invoke
+ ___62-[RTRoutineManager startMonitoringForPeopleDiscovery:handler:]_block_invoke.547
+ ___62-[RTRoutineManager startMonitoringForPeopleDiscovery:handler:]_block_invoke_4
+ ___62-[RTRoutineManager stopMonitoringPredictedContextWithHandler:]_block_invoke
+ ___62-[RTRoutineManager stopMonitoringPredictedContextWithHandler:]_block_invoke.485
+ ___62-[RTRoutineManager stopMonitoringPredictedContextWithHandler:]_block_invoke_2
+ ___62-[RTRoutineManager stopMonitoringPredictedContextWithHandler:]_block_invoke_2.486
+ ___62-[RTRoutineManager stopMonitoringPredictedContextWithHandler:]_block_invoke_3
+ ___62-[RTRoutineManagerExportedObject onScenarioTrigger:withError:]_block_invoke
+ ___63+[RTSignalGeneratorOptions getVisitsFromVisitsDescriptionData:]_block_invoke.110
+ ___63-[RTRoutineManager fetchLocationsOfInterestOfType:withHandler:]_block_invoke_4
+ ___63-[RTRoutineManager submitUserCurationForDate:newLabel:handler:]_block_invoke
+ ___63-[RTRoutineManager submitUserCurationForDate:newLabel:handler:]_block_invoke.564
+ ___63-[RTRoutineManager submitUserCurationForDate:newLabel:handler:]_block_invoke_2
+ ___63-[RTRoutineManager submitUserCurationForDate:newLabel:handler:]_block_invoke_3
+ ___64-[RTRoutineManager extendLifetimeOfVisitWithIdentifier:handler:]_block_invoke_4
+ ___64-[RTRoutineManager fetchTripClusterMetadataWithOptions:handler:]_block_invoke
+ ___64-[RTRoutineManager fetchTripClusterMetadataWithOptions:handler:]_block_invoke_2
+ ___64-[RTRoutineManager fetchTripClusterMetadataWithOptions:handler:]_block_invoke_3
+ ___64-[RTRoutineManager fetchTripClusterMetadataWithOptions:handler:]_block_invoke_4
+ ___64-[RTRoutineManager fetchTripSegmentMetadataWithOptions:handler:]_block_invoke_4
+ ___64-[RTRoutineManager startLeechingLowConfidenceVisitsWithHandler:]_block_invoke_5
+ ___64-[RTRoutineManager stopMonitoringForPeopleDiscoveryWithHandler:]_block_invoke.548
+ ___64-[RTRoutineManager stopMonitoringForPeopleDiscoveryWithHandler:]_block_invoke.549
+ ___64-[RTRoutineManager stopMonitoringForPeopleDiscoveryWithHandler:]_block_invoke_3
+ ___65-[RTRoutineManager addBackgroundInertialOdometrySamples:handler:]_block_invoke.563
+ ___65-[RTRoutineManager addBackgroundInertialOdometrySamples:handler:]_block_invoke_3
+ ___65-[RTRoutineManager fetchEstimatedLocationAtDate:options:handler:]_block_invoke_4
+ ___65-[RTRoutineManager fetchLocationOfInterestForRegion:withHandler:]_block_invoke_4
+ ___65-[RTRoutineManager updateCloudSyncProvisionedForAccount:handler:]_block_invoke_4
+ ___65-[RTRoutineManagerExportedObject onPredictedContextResult:error:]_block_invoke
+ ___66-[RTRoutineManager extendLifetimeOfVisitsWithIdentifiers:handler:]_block_invoke_4
+ ___66-[RTRoutineManager fetchLocationOfInterestAtLocation:withHandler:]_block_invoke_4
+ ___66-[RTRoutineManager fetchMonitoredScenarioTriggerTypesWithHandler:]_block_invoke_4
+ ___66-[RTRoutineManager fetchPathToDiagnosticFilesWithOptions:handler:]_block_invoke_4
+ ___67-[RTPredictedContextResult predictedContextsWithType:afterContext:]_block_invoke
+ ___67-[RTRoutineManager removeLocationOfInterestWithIdentifier:handler:]_block_invoke_4
+ ___68-[RTPredictedContextResult nextStepPredictedContextsWithFilterMask:]_block_invoke
+ ___68-[RTRoutineManager _enumerateStoredLocationsWithOptions:usingBlock:]_block_invoke.464
+ ___68-[RTRoutineManager _enumerateStoredLocationsWithOptions:usingBlock:]_block_invoke.465
+ ___68-[RTRoutineManager fetchFamiliarityIndexResultsWithOptions:handler:]_block_invoke_4
+ ___68-[RTRoutineManager fetchLocationsForTripSegmentWithOptions:handler:]_block_invoke_4
+ ___68-[RTRoutineManager fetchPeopleCountEventsHistory:completionHandler:]_block_invoke.553
+ ___68-[RTRoutineManager fetchPeopleCountEventsHistory:completionHandler:]_block_invoke_3
+ ___69-[RTRoutineManager fetchLookbackWindowStartDateWithLocation:handler:]_block_invoke_4
+ ___69-[RTRoutineManager fetchTransitionsBetweenStartDate:endDate:handler:]_block_invoke_4
+ ___69-[RTRoutineManager startMonitoringScenarioTriggerOfType:withHandler:]_block_invoke_5
+ ___70-[RTRoutineManager fetchAllLocationsOfInterestForSettingsWithHandler:]_block_invoke_4
+ ___70-[RTRoutineManager fetchLocationOfInterestWithIdentifier:withHandler:]_block_invoke_4
+ ___70-[RTRoutineManager startMonitoringPlaceInferencesWithOptions:handler:]_block_invoke.473
+ ___70-[RTRoutineManager startMonitoringPlaceInferencesWithOptions:handler:]_block_invoke_2.474
+ ___70-[RTRoutineManager startMonitoringPlaceInferencesWithOptions:handler:]_block_invoke_3
+ ___71-[RTRoutineManager fetchContactScoresFromContactIDs:completionHandler:]_block_invoke.555
+ ___71-[RTRoutineManager fetchContactScoresFromContactIDs:completionHandler:]_block_invoke_3
+ ___71-[RTRoutineManager fetchPredictedContextWithOptions:completionHandler:]_block_invoke
+ ___71-[RTRoutineManager fetchPredictedContextWithOptions:completionHandler:]_block_invoke_2
+ ___71-[RTRoutineManager fetchPredictedContextWithOptions:completionHandler:]_block_invoke_3
+ ___71-[RTRoutineManager fetchPredictedContextWithOptions:completionHandler:]_block_invoke_4
+ ___72-[RTRoutineManager fetchPredictedLocationsOfInterestOnDate:withHandler:]_block_invoke_4
+ ___72-[RTRoutineManager fetchProximityHistoryFromEventIDs:completionHandler:]_block_invoke.552
+ ___72-[RTRoutineManager fetchProximityHistoryFromEventIDs:completionHandler:]_block_invoke_3
+ ___72-[RTRoutineManager setHintForRegionState:significantRegion:withHandler:]_block_invoke_4
+ ___72-[RTRoutineManager updateLocationOfInterestWithIdentifier:type:handler:]_block_invoke_4
+ ___72-[RTRoutineManagerExportedObject onLeechedLowConfidenceVisit:withError:]_block_invoke
+ ___73-[RTRoutineManager fetchLocationsCountForTripSegmentWithOptions:handler:]_block_invoke_4
+ ___73-[RTRoutineManager fetchLocationsOfInterestVisitedSinceDate:withHandler:]_block_invoke_4
+ ___73-[RTRoutineManager submitUserCurationForVisitDateRange:newLabel:handler:]_block_invoke
+ ___73-[RTRoutineManager submitUserCurationForVisitDateRange:newLabel:handler:]_block_invoke.565
+ ___73-[RTRoutineManager submitUserCurationForVisitDateRange:newLabel:handler:]_block_invoke_2
+ ___73-[RTRoutineManager submitUserCurationForVisitDateRange:newLabel:handler:]_block_invoke_3
+ ___75-[RTRoutineManager fetchPredictedExitDatesFromLocation:onDate:withHandler:]_block_invoke_4
+ ___75-[RTRoutineManager updateLocationOfInterestWithIdentifier:mapItem:handler:]_block_invoke_4
+ ___76-[RTRoutineManager addLocationOfInterestOfType:mapItem:customLabel:handler:]_block_invoke_4
+ ___76-[RTRoutineManager fetchAutomaticVehicleEventDetectionSupportedWithHandler:]_block_invoke_4
+ ___77-[RTRoutineManager _proxyForServicingSelector:asynchronous:withErrorHandler:]_block_invoke.415
+ ___77-[RTRoutineManager _proxyForServicingSelector:asynchronous:withErrorHandler:]_block_invoke.416
+ ___78-[RTRoutineManager fetchBackgroundInertialOdometrySamplesWithOptions:handler:]_block_invoke.562
+ ___78-[RTRoutineManager fetchBackgroundInertialOdometrySamplesWithOptions:handler:]_block_invoke_3
+ ___79-[RTRoutineManager fetchLocationsOfInterestAssociatedToIdentifier:withHandler:]_block_invoke_4
+ ___79-[RTRoutineManager updateLocationOfInterestWithIdentifier:customLabel:handler:]_block_invoke_4
+ ___81-[RTRoutineManager fetchProximityHistoryFromStartDate:endDate:completionHandler:]_block_invoke.551
+ ___81-[RTRoutineManager fetchProximityHistoryFromStartDate:endDate:completionHandler:]_block_invoke_3
+ ___81-[RTRoutineManager startMonitoringPredictedContextWithOptions:completionHandler:]_block_invoke
+ ___81-[RTRoutineManager startMonitoringPredictedContextWithOptions:completionHandler:]_block_invoke.483
+ ___81-[RTRoutineManager startMonitoringPredictedContextWithOptions:completionHandler:]_block_invoke_2
+ ___81-[RTRoutineManager startMonitoringPredictedContextWithOptions:completionHandler:]_block_invoke_2.484
+ ___81-[RTRoutineManager startMonitoringPredictedContextWithOptions:completionHandler:]_block_invoke_3
+ ___82-[RTRoutineManager fetchLocationsOfInterestWithinDistance:ofLocation:withHandler:]_block_invoke_4
+ ___84-[RTRoutineManager fetchDedupedLocationOfInterestIdentifiersWithIdentifier:handler:]_block_invoke_4
+ ___84-[RTRoutineManager fetchFinerGranularityInferredMapItemWithVisitIdentifier:handler:]_block_invoke_4
+ ___84-[RTRoutineManager updateLocationOfInterestWithIdentifier:type:customLabel:handler:]_block_invoke_4
+ ___85-[RTRoutineManager fetchPeopleDensityHistoryFromStartDate:endDate:completionHandler:]_block_invoke.554
+ ___85-[RTRoutineManager fetchPeopleDensityHistoryFromStartDate:endDate:completionHandler:]_block_invoke_3
+ ___88-[RTRoutineManager fetchLocationsOfInterestVisitedBetweenStartDate:endDate:withHandler:]_block_invoke_4
+ ___90-[RTRoutineManager fetchPredictedLocationsOfInterestBetweenStartDate:endDate:withHandler:]_block_invoke_4
+ ___92-[RTRoutineManager updateLocationOfInterestWithIdentifier:type:mapItem:customLabel:handler:]_block_invoke_4
+ ___96-[RTRoutineManager correctLabelForVisitWithIdentifier:entryDate:originalLabel:newLabel:handler:]_block_invoke
+ ___96-[RTRoutineManager correctLabelForVisitWithIdentifier:entryDate:originalLabel:newLabel:handler:]_block_invoke.566
+ ___96-[RTRoutineManager correctLabelForVisitWithIdentifier:entryDate:originalLabel:newLabel:handler:]_block_invoke_2
+ ___96-[RTRoutineManager correctLabelForVisitWithIdentifier:entryDate:originalLabel:newLabel:handler:]_block_invoke_3
+ ___Block_byref_object_copy_.559
+ ___Block_byref_object_dispose_.560
+ ___block_descriptor_40_e8_32bs_e5_v8?0ls32l8
+ ___block_descriptor_40_e8_32r_e25_v32?0"RTSource"8Q16^B24lr32l8
+ ___block_descriptor_40_e8_32s_e17_v16?0"NSError"8ls32l8
+ ___block_descriptor_41_e8_32bs_e5_v8?0ls32l8
+ ___block_descriptor_48_e8_32r40r_e29_v24?0"NSArray"8"NSError"16lr32l8r40l8
+ ___block_descriptor_48_e8_32s40bs_e20_v20?0B8"NSError"12ls32l8s40l8
+ ___block_descriptor_48_e8_32s40bs_e20_v24?0Q8"NSError"16ls32l8s40l8
+ ___block_descriptor_48_e8_32s40bs_e20_v24?0q8"NSError"16ls32l8s40l8
+ ___block_descriptor_48_e8_32s40bs_e28_v24?0"NSDate"8"NSError"16ls32l8s40l8
+ ___block_descriptor_48_e8_32s40bs_e29_v24?0"NSArray"8"NSError"16ls40l8s32l8
+ ___block_descriptor_48_e8_32s40bs_e30_v24?0"NSString"8"NSError"16ls32l8s40l8
+ ___block_descriptor_48_e8_32s40bs_e32_v24?0"CLLocation"8"NSError"16ls32l8s40l8
+ ___block_descriptor_48_e8_32s40bs_e33_v32?0"NSArray"8^B16"NSError"24ls32l8s40l8
+ ___block_descriptor_48_e8_32s40bs_e34_v24?0"NSDictionary"8"NSError"16ls32l8s40l8
+ ___block_descriptor_48_e8_32s40bs_e37_v24?0"RTPeopleDensity"8"NSError"16ls32l8s40l8
+ ___block_descriptor_48_e8_32s40bs_e39_v24?0"RTInferredMapItem"8"NSError"16ls32l8s40l8
+ ___block_descriptor_48_e8_32s40bs_e42_v24?0"RTLocationOfInterest"8"NSError"16ls32l8s40l8
+ ___block_descriptor_48_e8_32s40bs_e43_v24?0"RTTripSegmentMetadata"8"NSError"16ls32l8s40l8
+ ___block_descriptor_48_e8_32s40bs_e46_v24?0"RTPredictedContextResult"8"NSError"16ls32l8s40l8
+ ___block_descriptor_48_e8_32s40bs_e48_v24?0"RTAuthorizedLocationStatus"8"NSError"16ls32l8s40l8
+ ___block_descriptor_48_e8_32s40bs_e5_v8?0ls32l8s40l8
+ ___block_descriptor_48_e8_32s40bs_e8_v12?0B8ls32l8s40l8
+ ___block_descriptor_48_e8_32s_e25_B24?08"NSDictionary"16ls32l8
+ ___block_descriptor_48_e8_32s_e43_v32?0"RTPredictedContextSequence"8Q16^B24ls32l8
+ ___block_descriptor_48_e8_32s_e8_v16?08ls32l8
+ ___block_descriptor_49_e8_32s40bs_e5_v8?0ls40l8s32l8
+ ___block_descriptor_49_e8_32s40bs_e8_v16?08ls32l8s40l8
+ ___block_descriptor_56_e8_32s40s48bs_e28_v16?0"<RTDaemonProtocol>"8ls32l8s40l8s48l8
+ ___block_descriptor_56_e8_32s40s48bs_e5_v8?0ls32l8s48l8s40l8
+ ___block_descriptor_56_e8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
+ ___block_descriptor_56_e8_32s40s_e45_B24?0"RTPredictedContext"8"NSDictionary"16ls32l8s40l8
+ ___block_descriptor_56_e8_32s40s_e5_v8?0ls32l8s40l8
+ ___block_descriptor_64_e8_32s40s48s56s_e15_v32?08Q16^B24ls32l8s40l8s48l8s56l8
+ ___block_descriptor_64_e8_32s40s48s56s_e29_v32?0"NSDictionary"8Q16^B24ls32l8s40l8s48l8s56l8
+ ___block_descriptor_64_e8_32s40s48s_e45_B24?0"RTPredictedContext"8"NSDictionary"16ls32l8s40l8s48l8
+ ___block_descriptor_72_e8_32s40s48s56s64bs_e8_v16?08ls32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_80_e8_32s40bs48r56r64r72r_e29_v24?0"NSArray"8"NSError"16lr48l8r56l8s40l8r64l8r72l8s32l8
+ ___block_descriptor_80_e8_32s40s48s56s64bs_e8_v16?08ls32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_88_e8_32s40s48s56s64s72bs_e8_v16?08ls32l8s40l8s48l8s56l8s64l8s72l8
+ ___block_literal_global.17
+ ___block_literal_global.489
+ ___block_literal_global.516
+ ___block_literal_global.518
+ ___block_literal_global.520
+ ___block_literal_global.522
+ ___block_literal_global.524
+ ___block_literal_global.526
+ ___block_literal_global.528
+ ___block_literal_global.530
+ ___block_literal_global.532
+ ___block_literal_global.534
+ ___block_literal_global.536
+ ___block_literal_global.538
+ ___block_literal_global.540
+ ___block_literal_global.542
+ ___block_literal_global.544
+ ___block_literal_global.546
+ _kRTBluePOIMetadataModelCalibrationHighConfidence
+ _kRTBluePOIMetadataModelCalibrationHighThreshold
+ _kRTBluePOIMetadataModelCalibrationLowConfidence
+ _kRTBluePOIMetadataModelCalibrationLowThreshold
+ _kRTBluePOITileModelCalibrationHighThresholdAfterCalibrationApplePay
+ _kRTBluePOITileModelCalibrationHighThresholdAfterCalibrationNonApplePay
+ _kRTBluePOITileModelCalibrationHighThresholdBeforeCalibrationApplePay
+ _kRTBluePOITileModelCalibrationHighThresholdBeforeCalibrationNonApplePay
+ _kRTBluePOITileModelCalibrationHighestScoreApplePay
+ _kRTBluePOITileModelCalibrationHighestScoreNonApplePay
+ _kRTBluePOITileModelCalibrationLowThresholdAfterCalibrationApplePay
+ _kRTBluePOITileModelCalibrationLowThresholdAfterCalibrationNonApplePay
+ _kRTBluePOITileModelCalibrationLowThresholdBeforeCalibrationApplePay
+ _kRTBluePOITileModelCalibrationLowThresholdBeforeCalibrationNonApplePay
+ _kRTSignalGeneratorOptionsKeyCategory
+ _kRTSignalGeneratorOptionsKeyCategoryMUID
+ _kRTSignalGeneratorOptionsKeyConfidence
+ _kRTSignalGeneratorOptionsKeyDailyVisits
+ _kRTSignalGeneratorOptionsKeyMUID
+ _kRTSignalGeneratorOptionsKeyResultProviderID
+ _objc_getProperty
+ _objc_msgSend$_enumerateElevationsWithOptions:reply:
+ _objc_msgSend$_isValidRouteODLocation:routeDestinationLocation:routeFetchType:
+ _objc_msgSend$allRoutesCountForThisODPair
+ _objc_msgSend$allTraversalCountBetweenThisODPair
+ _objc_msgSend$analytics
+ _objc_msgSend$aoiConfidences
+ _objc_msgSend$apToModelMapping
+ _objc_msgSend$applePaySupport
+ _objc_msgSend$archivedDataWithRootObject:requiringSecureCoding:error:
+ _objc_msgSend$averageTripDistance
+ _objc_msgSend$averageTripTime
+ _objc_msgSend$avgBikeDistance
+ _objc_msgSend$avgBikeTime
+ _objc_msgSend$avgWalkDistance
+ _objc_msgSend$avgWalkTime
+ _objc_msgSend$bikeTraversalCount
+ _objc_msgSend$bundleIdentifier
+ _objc_msgSend$bundlePath
+ _objc_msgSend$categoryDenyList
+ _objc_msgSend$clusterID
+ _objc_msgSend$clusterOrder
+ _objc_msgSend$commuteID
+ _objc_msgSend$confidenceInterval
+ _objc_msgSend$contextTypeForContext:
+ _objc_msgSend$contextTypeMaskForContext:
+ _objc_msgSend$correctLabelForVisitWithIdentifier:entryDate:originalLabel:newLabel:handler:
+ _objc_msgSend$countOfTraversal
+ _objc_msgSend$course
+ _objc_msgSend$curatedLabel
+ _objc_msgSend$dataWithBytes:length:
+ _objc_msgSend$dateByAddingUnit:value:
+ _objc_msgSend$dateFormatterForLogging
+ _objc_msgSend$dateIntervalFromStart:end:
+ _objc_msgSend$dateOfMostRecentTrip
+ _objc_msgSend$dateWithTimeInterval:sinceDate:
+ _objc_msgSend$decodeDictionaryWithKeysOfClass:objectsOfClass:forKey:
+ _objc_msgSend$decodeFloatForKey:
+ _objc_msgSend$decodeInt32ForKey:
+ _objc_msgSend$destinationLatitude
+ _objc_msgSend$destinationLongitude
+ _objc_msgSend$destinationVisit
+ _objc_msgSend$destinationVisitLatitude
+ _objc_msgSend$destinationVisitLongitude
+ _objc_msgSend$downloadError
+ _objc_msgSend$downloadKey
+ _objc_msgSend$encodeFloat:forKey:
+ _objc_msgSend$encodeInt32:forKey:
+ _objc_msgSend$endLatitude
+ _objc_msgSend$endLongitude
+ _objc_msgSend$expirationDate
+ _objc_msgSend$fetchAllRouteLocations
+ _objc_msgSend$fetchElevationsWithContext:reply:
+ _objc_msgSend$fetchLearnedRoutesWithOptions:reply:
+ _objc_msgSend$fetchPredictedContextWithOptions:reply:
+ _objc_msgSend$fetchTripClusterMetadataWithOptions:reply:
+ _objc_msgSend$filterContextTypeMask
+ _objc_msgSend$filterLocations
+ _objc_msgSend$filterPairedVisitEntries
+ _objc_msgSend$filtered
+ _objc_msgSend$followedByUTurn
+ _objc_msgSend$forecastWindowDateInterval
+ _objc_msgSend$forecastWindowTimeInterval
+ _objc_msgSend$fullyCoversTile
+ _objc_msgSend$generateSequencesFromDate:toDate:
+ _objc_msgSend$geoCacheInfo
+ _objc_msgSend$geoMapItemIdentifier
+ _objc_msgSend$geoTileKey
+ _objc_msgSend$getUUIDBytes:
+ _objc_msgSend$inferenceTriggerReasonToString
+ _objc_msgSend$init
+ _objc_msgSend$initWithAllRoutesCountForThisODPair:allTraversalCountBetweenThisODPair:routeTraversalCount:routeTraversalCountOnTravelDayOfWeek:routeTravelCountOnTravelDayOfWeekHourOfDay:lastTravelledDate:
+ _objc_msgSend$initWithAscending:confidence:dateInterval:labelVisit:limit:sources:redact:
+ _objc_msgSend$initWithAscending:confidence:dateInterval:labelVisit:limit:sources:redact:filterPairedVisitEntries:
+ _objc_msgSend$initWithAscending:sortIndex:submissionDateInterval:visitDateInterval:limit:
+ _objc_msgSend$initWithBundleIdentifier:bundlePath:routeOriginLocation:routeDestinationLocation:routeDate:routeFetchType:fetchAllRouteLocations:routeOriginType:
+ _objc_msgSend$initWithClusterID:
+ _objc_msgSend$initWithDate:
+ _objc_msgSend$initWithDate:confidenceInterval:
+ _objc_msgSend$initWithDate:machContinuousTimeSec:numberOfSeconds:
+ _objc_msgSend$initWithDate:type:location:entry:exit:dataPointCount:confidence:placeInference:source:identifier:
+ _objc_msgSend$initWithDateInterval:predictionSources:probability:sourceBundleIdentifier:workoutActivityType:
+ _objc_msgSend$initWithDownloadKey:tileURL:tileCacheInfo:downloadError:
+ _objc_msgSend$initWithEventIdentifier:startDate:endDate:title:location:allDay:sharingStatus:tentative:participationOptional:suggestionInfo_opaqueKey:suggestionsSchemaOrg:
+ _objc_msgSend$initWithForecastWindowDateInterval:filterContextTypeMask:filterLocations:resultSortDescriptors:
+ _objc_msgSend$initWithForecastWindowDateInterval:forecastWindowTimeInterval:filterContextTypeMask:filterLocations:resultSortDescriptors:
+ _objc_msgSend$initWithIdentifier:apToModelMapping:date:downloadKey:geoCacheInfo:geoTileKey:modelCalibrationParameters:modelURLs:pointsOfInterest:singlePOIMuid:size:
+ _objc_msgSend$initWithIdentifier:applePaySupport:filtered:fullyCoversTile:location:muid:polygon:
+ _objc_msgSend$initWithIdentifier:categoryDenyList:geoCacheInfo:modelCalibrationParameters:
+ _objc_msgSend$initWithIdentifier:loiIsMissingFromCurrentVisitHistory:isHome:isWork:
+ _objc_msgSend$initWithIdentifier:name:category:categoryMUID:address:location:source:mapItemPlaceType:muid:resultProviderID:geoMapItemHandle:creationDate:expirationDate:extendedAttributes:displayLanguage:disputed:
+ _objc_msgSend$initWithIdentifier:parkDate:
+ _objc_msgSend$initWithIdentifier:predictedContextResult:requestStartDate:requestEndDate:inferenceTriggerReason:memoryFootprintStart:memoryFootprintEnd:clientCount:
+ _objc_msgSend$initWithIdentifier:primary:
+ _objc_msgSend$initWithIdentifier:submissionDate:expirationDate:entryDate:exitDate:curatedLabel:
+ _objc_msgSend$initWithLatitude:longitude:course:followedByUTurn:locationReferenceFrame:
+ _objc_msgSend$initWithLearnedRouteId:routeStartLocation:routeEndLocation:travelTimeEntireRouteSec:travelDistanceEntireRouteMeter:travelModeRoutes:routeStartLocationWithReferenceFrame:routeEndLocationWithReferenceFrame:
+ _objc_msgSend$initWithLocationOfInterest:dateInterval:predictionSources:probability:
+ _objc_msgSend$initWithMUID:coordinate:
+ _objc_msgSend$initWithMinCountOfTraversal:startLatitude:startLongitude:endLatitude:endLongitude:
+ _objc_msgSend$initWithOptions:startDate:endDate:
+ _objc_msgSend$initWithOptions:startDate:endDate:maximumNumberOfItems:
+ _objc_msgSend$initWithOriginVisitLatitude:originVisitLongitude:destinationVisitLatitude:destinationVisitLongitude:
+ _objc_msgSend$initWithPOIConfidences:aoiConfidences:referenceLocation:queryTime:
+ _objc_msgSend$initWithPredictedContextDateInterval:predictionSources:probability:
+ _objc_msgSend$initWithPredictedContextTransports:predictedContextDateInterval:predictionSources:probability:
+ _objc_msgSend$initWithPredictedContexts:analytics:
+ _objc_msgSend$initWithProbability:dateInterval:predictedContexts:
+ _objc_msgSend$initWithRolledLOIResult:
+ _objc_msgSend$initWithRouteTravelMode:maxTravelTimeEstimateInSeconds:minTravelTimeEstimateInSeconds:meanTravelTimeEstimateInSeconds:maxTravelledDistanceEstimateInMeters:minTravelledDistanceEstimateInMeters:meanTravelledDistanceEstimateInMeters:routeLocations:learnedRouteLocations:learnedRouteMetrics:
+ _objc_msgSend$initWithStartAndEndVisitLatitude:startLongitude:endLatitude:endLongitude:
+ _objc_msgSend$initWithStatus:zdrConfirmationList:
+ _objc_msgSend$initWithTransportMode:probability:
+ _objc_msgSend$initWithTripClusterId:dateOfMostRecentTrip:modeOfTransport:countOfTraversal:originLatitude:originLongitude:destinationLatitude:destinationLongitude:averageTripTime:averageTripDistance:minimumTripTime:maximumTripTime:minimumTripDistance:maximumTripDistance:commuteID:isLocked:avgBikeDistance:avgBikeTime:avgWalkDistance:avgWalkTime:bikeTraversalCount:walkTraversalCount:clusterOrder:
+ _objc_msgSend$initWithTripSegmentIdentifier:dateInterval:tripDistance:tripDistanceUncertainty:modeOfTransportation:isConsumedByClustering:tripSegmentSequence:tripSegmentSequenceMax:originLatitude:originLongitude:destinationLatitude:destinationLongitude:tripCommuteID:
+ _objc_msgSend$initWithWorkoutUUID:startDate:
+ _objc_msgSend$initWithbatchSize:
+ _objc_msgSend$isConsumedByClustering
+ _objc_msgSend$isEqualToData:
+ _objc_msgSend$isEqualToDictionary:
+ _objc_msgSend$isEqualToUserCuration:
+ _objc_msgSend$isHome
+ _objc_msgSend$isLocked
+ _objc_msgSend$isValidRouteFetchType:
+ _objc_msgSend$isWork
+ _objc_msgSend$key
+ _objc_msgSend$lastTravelledDate
+ _objc_msgSend$learnedRouteEndLocation
+ _objc_msgSend$learnedRouteEndLocationWithReferenceFrame
+ _objc_msgSend$learnedRouteIdentifier
+ _objc_msgSend$learnedRouteLocations
+ _objc_msgSend$learnedRouteMetrics
+ _objc_msgSend$learnedRouteStartLocation
+ _objc_msgSend$learnedRouteStartLocationWithReferenceFrame
+ _objc_msgSend$localeWithLocaleIdentifier:
+ _objc_msgSend$locationReferenceFrame
+ _objc_msgSend$loiIsMissingFromCurrentVisitHistory
+ _objc_msgSend$machContinuousTimeSec
+ _objc_msgSend$maxTravelTimeEstimateInSeconds
+ _objc_msgSend$maxTravelledDistanceEstimateInMeters
+ _objc_msgSend$maximumTripDistance
+ _objc_msgSend$maximumTripTime
+ _objc_msgSend$meanTravelTimeEstimateInSeconds
+ _objc_msgSend$meanTravelledDistanceEstimateInMeters
+ _objc_msgSend$minCountOfTraversal
+ _objc_msgSend$minTravelTimeEstimateInSeconds
+ _objc_msgSend$minTravelledDistanceEstimateInMeters
+ _objc_msgSend$minimumTripDistance
+ _objc_msgSend$minimumTripTime
+ _objc_msgSend$modeOfTransport
+ _objc_msgSend$modelCalibrationParameters
+ _objc_msgSend$modelURLs
+ _objc_msgSend$month
+ _objc_msgSend$numberOfSeconds
+ _objc_msgSend$numberWithUnsignedLongLong:
+ _objc_msgSend$numberWithUnsignedShort:
+ _objc_msgSend$onPredictedContextResult:error:
+ _objc_msgSend$onRemoteStatusUpdate:error:
+ _objc_msgSend$originLatitude
+ _objc_msgSend$originLongitude
+ _objc_msgSend$originVisit
+ _objc_msgSend$originVisitLatitude
+ _objc_msgSend$originVisitLongitude
+ _objc_msgSend$parkDate
+ _objc_msgSend$participationOptional
+ _objc_msgSend$poiConfidences
+ _objc_msgSend$pointsOfInterest
+ _objc_msgSend$polygon
+ _objc_msgSend$predictedContextHandler
+ _objc_msgSend$predictedContextOptions
+ _objc_msgSend$predictedContextTransports
+ _objc_msgSend$predictedContexts
+ _objc_msgSend$predictionSources
+ _objc_msgSend$primary
+ _objc_msgSend$probability
+ _objc_msgSend$purgeTripClusterTable:reply:
+ _objc_msgSend$purgeTripClusterWithClusterID:reply:
+ _objc_msgSend$queryTime
+ _objc_msgSend$redact
+ _objc_msgSend$remoteStatusHandler
+ _objc_msgSend$resultSortDescriptors
+ _objc_msgSend$rolledLOIResult
+ _objc_msgSend$routeDate
+ _objc_msgSend$routeFetchType
+ _objc_msgSend$routeLocations
+ _objc_msgSend$routeOriginType
+ _objc_msgSend$routeTravelCountOnTravelDayOfWeekHourOfDay
+ _objc_msgSend$routeTravelMode
+ _objc_msgSend$routeTraversalCount
+ _objc_msgSend$routeTraversalCountOnTravelDayOfWeek
+ _objc_msgSend$selector
+ _objc_msgSend$setPredictedContextHandler:
+ _objc_msgSend$setPredictedContextOptions:
+ _objc_msgSend$setRemoteStatusHandler:
+ _objc_msgSend$setWithArray:
+ _objc_msgSend$singlePOIMuid
+ _objc_msgSend$size
+ _objc_msgSend$sortDescriptorWithKey:ascending:selector:
+ _objc_msgSend$sortIndex
+ _objc_msgSend$sourceBundleIdentifier
+ _objc_msgSend$startLatitude
+ _objc_msgSend$startLongitude
+ _objc_msgSend$startMonitoringForPeopleDiscoveryWithIdentifier:configuration:reply:
+ _objc_msgSend$startMonitoringPredictedContextWithOptions:completionHandler:
+ _objc_msgSend$startMonitoringPredictedContextWithOptions:reply:
+ _objc_msgSend$startMonitoringRemoteStatusWithHandler:
+ _objc_msgSend$startMonitoringRemoteStatusWithReply:
+ _objc_msgSend$startOfDayForDate:
+ _objc_msgSend$stopMonitoringForPeopleDiscoveryWithIdentifier:reply:
+ _objc_msgSend$stopMonitoringPredictedContextWithReply:
+ _objc_msgSend$stopMonitoringRemoteStatusWithReply:
+ _objc_msgSend$submissionDate
+ _objc_msgSend$submissionDateInterval
+ _objc_msgSend$submitUserCurationForVisitDateRange:newLabel:handler:
+ _objc_msgSend$tentative
+ _objc_msgSend$tileCacheInfo
+ _objc_msgSend$tileURL
+ _objc_msgSend$transportMode
+ _objc_msgSend$travelModeRoutes
+ _objc_msgSend$travelTimeEstimateForEntireRouteInSeconds
+ _objc_msgSend$travelledDistanceEstimateForEntireRouteInMeters
+ _objc_msgSend$tripCommuteID
+ _objc_msgSend$tripSegmentSequence
+ _objc_msgSend$tripSegmentSequenceMax
+ _objc_msgSend$unarchivedObjectOfClass:fromData:error:
+ _objc_msgSend$unknownPredictedContextFromStart:end:
+ _objc_msgSend$unsignedLongLongValue
+ _objc_msgSend$visitDateInterval
+ _objc_msgSend$visitEntryDate
+ _objc_msgSend$visitExitDate
+ _objc_msgSend$walkTraversalCount
+ _objc_msgSend$workoutActivityType
+ _objc_msgSend$workoutUUID
+ _objc_msgSend$xpcQueue
+ _objc_msgSend$year
+ _objc_setProperty_atomic
- -[RTMapItem initWithIdentifier:name:category:address:location:source:mapItemPlaceType:muid:resultProviderID:geoMapItemHandle:creationDate:expirationDate:extendedAttributes:displayLanguage:disputed:]
- -[RTSourceEventKit initWithEventIdentifier:startDate:endDate:title:location:allDay:sharingStatus:suggestionInfo_opaqueKey:suggestionsSchemaOrg:]
- -[RTTripSegment initWithTripSegmentIdentifier:dateInterval:tripDistance:tripDistanceUncertainty:modeOfTransportation:]
- GCC_except_table100
- GCC_except_table107
- GCC_except_table109
- GCC_except_table9
- GCC_except_table99
- ___37-[RTRoutineManager _createConnection]_block_invoke.371
- ___38-[RTRoutineManager stopLeechingVisits]_block_invoke.424
- ___38-[RTRoutineManager stopLeechingVisits]_block_invoke_2.425
- ___40-[RTRoutineManager stopMonitoringVisits]_block_invoke.422
- ___40-[RTRoutineManager stopMonitoringVisits]_block_invoke_2.423
- ___42-[RTRoutineManager addElevations:handler:]_block_invoke.508
- ___49-[RTRoutineManager fetchRoutineStateWithHandler:]_block_invoke.397
- ___49-[RTRoutineManager stopMonitoringPlaceInferences]_block_invoke.430
- ___49-[RTRoutineManager stopMonitoringPlaceInferences]_block_invoke_2.431
- ___51-[RTRoutineManager fetchRoutineEnabledWithHandler:]_block_invoke.395
- ___51-[RTRoutineManager stopLeechingLowConfidenceVisits]_block_invoke.426
- ___51-[RTRoutineManager stopLeechingLowConfidenceVisits]_block_invoke_2.427
- ___53-[RTRoutineManager clearAllVehicleEventsWithHandler:]_block_invoke.466
- ___53-[RTRoutineManager fetchElevationsWithOptions:reply:]_block_invoke.509
- ___56+[RTSignalGeneratorOptions visitsDescriptionDataAtPath:]_block_invoke.74
- ___56+[RTSignalGeneratorOptions visitsDescriptionDataAtPath:]_block_invoke.78
- ___56+[RTSignalGeneratorOptions visitsDescriptionDataAtPath:]_block_invoke_2.79
- ___56-[RTRoutineManager stopMonitoringScenarioTriggerOfType:]_block_invoke.439
- ___56-[RTRoutineManager stopMonitoringScenarioTriggerOfType:]_block_invoke_2.440
- ___59-[RTRoutineManager enumerateObjectsWithOptions:usingBlock:]_block_invoke.409
- ___62-[RTRoutineManager startMonitoringForPeopleDiscovery:handler:]_block_invoke.499
- ___63+[RTSignalGeneratorOptions getVisitsFromVisitsDescriptionData:]_block_invoke.93
- ___64-[RTRoutineManager stopMonitoringForPeopleDiscoveryWithHandler:]_block_invoke.500
- ___64-[RTRoutineManager stopMonitoringForPeopleDiscoveryWithHandler:]_block_invoke.501
- ___65-[RTRoutineManager addBackgroundInertialOdometrySamples:handler:]_block_invoke.511
- ___68-[RTRoutineManager _enumerateStoredLocationsWithOptions:usingBlock:]_block_invoke.414
- ___68-[RTRoutineManager _enumerateStoredLocationsWithOptions:usingBlock:]_block_invoke.418
- ___68-[RTRoutineManager _enumerateStoredLocationsWithOptions:usingBlock:]_block_invoke.419
- ___68-[RTRoutineManager fetchPeopleCountEventsHistory:completionHandler:]_block_invoke.505
- ___70-[RTRoutineManager startMonitoringPlaceInferencesWithOptions:handler:]_block_invoke.428
- ___70-[RTRoutineManager startMonitoringPlaceInferencesWithOptions:handler:]_block_invoke_2.429
- ___71-[RTRoutineManager fetchContactScoresFromContactIDs:completionHandler:]_block_invoke.507
- ___72-[RTRoutineManager fetchProximityHistoryFromEventIDs:completionHandler:]_block_invoke.504
- ___78-[RTRoutineManager fetchBackgroundInertialOdometrySamplesWithOptions:handler:]_block_invoke.510
- ___81-[RTRoutineManager fetchProximityHistoryFromStartDate:endDate:completionHandler:]_block_invoke.503
- ___85-[RTRoutineManager fetchPeopleDensityHistoryFromStartDate:endDate:completionHandler:]_block_invoke.506
- ____RTSemaphoreWait_block_invoke
- ___block_descriptor_32_e35_B24?0"NSString"8"NSDictionary"16l
- ___block_descriptor_40_e8_32bs_e20_v20?0B8"NSError"12ls32l8
- ___block_descriptor_40_e8_32bs_e20_v24?0Q8"NSError"16ls32l8
- ___block_descriptor_40_e8_32bs_e20_v24?0q8"NSError"16ls32l8
- ___block_descriptor_40_e8_32bs_e28_v16?0"<RTDaemonProtocol>"8ls32l8
- ___block_descriptor_40_e8_32bs_e28_v24?0"NSDate"8"NSError"16ls32l8
- ___block_descriptor_40_e8_32bs_e30_v24?0"NSString"8"NSError"16ls32l8
- ___block_descriptor_40_e8_32bs_e32_v24?0"CLLocation"8"NSError"16ls32l8
- ___block_descriptor_40_e8_32bs_e37_v24?0"RTPeopleDensity"8"NSError"16ls32l8
- ___block_descriptor_40_e8_32bs_e39_v24?0"RTInferredMapItem"8"NSError"16ls32l8
- ___block_descriptor_40_e8_32bs_e42_v24?0"RTLocationOfInterest"8"NSError"16ls32l8
- ___block_descriptor_40_e8_32bs_e43_v24?0"RTTripSegmentMetadata"8"NSError"16ls32l8
- ___block_descriptor_40_e8_32bs_e48_v24?0"RTAuthorizedLocationStatus"8"NSError"16ls32l8
- ___block_descriptor_40_e8_32bs_e8_v12?0B8ls32l8
- ___block_descriptor_40_e8_32bs_e8_v16?08ls32l8
- ___block_descriptor_40_e8_v16?08l
- ___block_descriptor_41_e8_32bs_e8_v16?08ls32l8
- ___block_descriptor_48_e8_32bs_e8_v16?08ls32l8
- ___block_descriptor_56_e8_32r40r48r_e29_v24?0"NSArray"8"NSError"16lr32l8r40l8r48l8
- ___block_descriptor_56_e8_32s40s48bs_e5_v8?0ls32l8s40l8s48l8
- ___block_descriptor_72_e8_32s40s48bs56r_e28_v16?0"<RTDaemonProtocol>"8ls32l8s40l8r56l8s48l8
- ___block_literal_global.438
- ___block_literal_global.442
- ___block_literal_global.468
- ___block_literal_global.470
- ___block_literal_global.472
- ___block_literal_global.474
- ___block_literal_global.476
- ___block_literal_global.478
- ___block_literal_global.480
- ___block_literal_global.482
- ___block_literal_global.484
- ___block_literal_global.486
- ___block_literal_global.488
- ___block_literal_global.490
- ___block_literal_global.492
- ___block_literal_global.494
- ___block_literal_global.496
- ___block_literal_global.498
- ___block_literal_global.724
- _dispatch_semaphore_create
- _dispatch_semaphore_signal
- _dispatch_semaphore_wait
- _dispatch_time
- _objc_msgSend$_queue
- _objc_msgSend$containsString:
- _objc_msgSend$initWithEventIdentifier:startDate:endDate:title:location:allDay:sharingStatus:suggestionInfo_opaqueKey:suggestionsSchemaOrg:
- _objc_msgSend$initWithIdentifier:name:category:address:location:source:mapItemPlaceType:muid:resultProviderID:geoMapItemHandle:creationDate:expirationDate:extendedAttributes:displayLanguage:disputed:
- _objc_msgSend$initWithTripSegmentIdentifier:dateInterval:tripDistance:tripDistanceUncertainty:modeOfTransportation:
- _objc_msgSend$startMonitoringForPeopleDiscovery:configuration:reply:
- _objc_msgSend$stopMonitoringForPeopleDiscoveryWithReply:
- _objc_msgSend$submitToCoreAnalytics:type:duration:
- _objc_release_x2
CStrings:
+ "!Aq"
+ "\"q"
+ "#"
+ "%"
+ "%@ %@, dateInterval,%@,fetchRoadClass,%{sensitive}d,fetchFormOfWay,%{sensitive}d,fetchLocationType,%d,fetchPreferredNames,%{sensitive}d"
+ "%@, %@, %{sensitive}@"
+ "%@, %@, generated sequences before filling gaps with unknown state and computing probabilities, %lu"
+ "%@, %@, idx, %lu, output sequence, %{sensitive}@"
+ "%@, %@, input predictedContext, %{sensitive}@"
+ "%@, %@, mask, %lu"
+ "%@, %@, startDate, %@, endDate, %@"
+ "%@, date, %@"
+ "%@, eventIdentifier, %@, startDate, %@, endDate, %@, title, %@, location %@, sharingStatus, %@, suggestionsSchemaOrg, %@, participationTentative, %@, participationOptional, %@"
+ "%@, identifier, %@, parkDate, %@"
+ "%@, identifier, %@, primary, %s"
+ "%@, workoutUUID, %@, startDate, %@"
+ "%@,Initialized context with options clusterID,%@"
+ "%@: error from %@, %@"
+ "%@: invoked %@"
+ "%@: replying from %@"
+ "-[RTLearnedRouteFetchOptions initWithBundleIdentifier:bundlePath:routeOriginLocation:routeDestinationLocation:routeDate:routeFetchType:fetchAllRouteLocations:routeOriginType:]"
+ "-[RTLearnedRouteFetchOptions initWithBundleIdentifier:routeOriginLocation:routeDestinationLocation:routeDate:routeFetchType:fetchAllRouteLocations:routeOriginType:]"
+ "-[RTLearnedRouteFetchOptions initWithBundlePath:routeOriginLocation:routeDestinationLocation:routeDate:routeFetchType:fetchAllRouteLocations:routeOriginType:]"
+ "-[RTPredictedContextLocation encodeWithCoder:]"
+ "-[RTPredictedContextWorkout encodeWithCoder:]"
+ "-[RTRoutineManager _enumerateElevationsWithOptions:reply:]"
+ "-[RTRoutineManager enumerateElevationsWithOptions:reply:]"
+ "-[RTRoutineManager fetchLearnedRoutesWithOptions:handler:]"
+ "-[RTRoutineManager fetchPredictedContextWithOptions:completionHandler:]"
+ "-[RTRoutineManager fetchTripClusterMetadataWithOptions:handler:]"
+ "-[RTRoutineManager purgeTripClusterTable:handler:]"
+ "-[RTRoutineManager purgeTripClusterWithClusterID:handler:]"
+ "-[RTRoutineManager startMonitoringPredictedContextWithOptions:completionHandler:]"
+ "-[RTRoutineManager startMonitoringRemoteStatusWithHandler:]"
+ "-[RTRoutineManager stopMonitoringPredictedContextWithHandler:]"
+ "-[RTRoutineManager stopMonitoringRemoteStatusWithHandler:]"
+ "-[RTSourceHealthKitWorkout initWithWorkoutUUID:startDate:]"
+ "-[RTSourceHomeKit encodeWithCoder:]"
+ "-[RTSourceHomeKit initWithCoder:]"
+ "-[RTSourceParkedCar encodeWithCoder:]"
+ "-[RTSourceParkedCar initWithCoder:]"
+ "-[RTSourcePropagatedLocation encodeWithCoder:]"
+ "-[RTSourcePropagatedLocation initWithCoder:]"
+ "<Invalid>"
+ "@\"NSError\""
+ "@\"NSURL\""
+ "@\"RTAuthorizedLocationConfirmationStatusEnumerationOptions\""
+ "@\"RTAuthorizedLocationZDRLocationsEnumerationOptions\""
+ "@\"RTGeoRoadDataEnumerationOptions\""
+ "@\"RTLearnedRouteLocation\""
+ "@\"RTLearnedRouteMetrics\""
+ "@\"RTPolygon\""
+ "@\"RTPredictedContextAnalytics\""
+ "@\"RTPredictedContextDate\""
+ "@\"RTPredictedContextDateInterval\""
+ "@\"RTPredictedContextOptions\""
+ "@\"RTPredictedContextResult\""
+ "@\"RTTripClusterEnumerationOptions\""
+ "@\"RTTripClusterRecencyEnumerationOptions\""
+ "@\"RTTripClusterRoadTransitionsEnumerationOptions\""
+ "@\"RTTripClusterRouteEnumerationOptions\""
+ "@\"RTTripClusterScheduleEnumerationOptions\""
+ "@104@0:8@16@24@32@40@48Q56@64@72@80Q88d96"
+ "@108@0:8@16@24d32d40q48B56i60i64d68d76d84d92@100"
+ "@140@0:8@16@24@32@40@48@56Q64Q72Q80q88@96@104@112@120@128B136"
+ "@180@0:8@16@24q32i40d44d52d60d68d76d84d92d100d108d116@124B132d136d144d152d160i168i172s176"
+ "@32@0:8q16d24"
+ "@36@0:8@16B24B28B32"
+ "@36@0:8B16Q20@28"
+ "@40@0:8@16@24d32"
+ "@40@0:8d16@24@32"
+ "@48@0:8@16@24@32d40"
+ "@48@0:8@16Q24@32B40B44"
+ "@48@0:8d16Q24@32@40"
+ "@48@0:8d16d24d32B40i44"
+ "@48@0:8d16d24d32d40"
+ "@52@0:8B16Q20@28@36@44"
+ "@52@0:8S16d20d28d36d44"
+ "@56@0:8@16@24d32@40q48"
+ "@56@0:8@16d24Q32@40@48"
+ "@60@0:8@16@24@32@40i48B52i56"
+ "@60@0:8@16B24B28B32@36Q44@52"
+ "@60@0:8B16@20@28B36@40@48B56"
+ "@64@0:8@16@24@32@40@48@56"
+ "@64@0:8B16@20@28B36@40@48B56B60"
+ "@64@0:8Q16Q24Q32Q40Q48@56"
+ "@68@0:8@16@24@32@40@48i56B60i64"
+ "@72@0:8@16@24@32f40f44@48@56@64"
+ "@72@0:8q16f24f28f32f36f40f44@48@56@64"
+ "@80@0:8@16@24@32@40q48d56d64Q72"
+ "@92@0:8@16@24@32@40@48B56Q60B68B72@76@84"
+ "@96@0:8@16q24@32@40@48q56d64@72q80@88"
+ "B20@0:8i16"
+ "B20@0:8s16"
+ "B24@?0@\"RTPredictedContext\"8@\"NSDictionary\"16"
+ "B24@?0@8@\"NSDictionary\"16"
+ "B36@0:8@16@24i32"
+ "C"
+ "Category"
+ "CategoryMUID"
+ "Client Registration"
+ "CompanionSyncVisit"
+ "DailyVisits"
+ "Date: %@"
+ "Dominant Motion Notification"
+ "Encountered error while fetching predicted context, error, %@"
+ "Encountered error while starting to monitor predicted context, error, %@"
+ "Encountered error while starting to monitor remote status, error, %@"
+ "Encountered error while stopping monitoring of remote status, error, %@"
+ "Encountered error while stopping to monitor predicted context, error, %@"
+ "ID, %@, submissionDate, %@, visit duration, %@ -> %@"
+ "Invalid Reason (%ld)"
+ "Invalid parameter not satisfying: (routeOriginType == RTLearnedRouteOriginType_OriginIsCurrentLocation) || (routeOriginType == RTLearnedRouteOriginType_OriginIsVisitLocation) (in %s:%d)"
+ "Invalid parameter not satisfying: [RTLearnedRouteFetchOptions _isValidRouteODLocation:routeOriginLocation routeDestinationLocation:routeDestinationLocation routeFetchType:routeFetchType] (in %s:%d)"
+ "Invalid parameter not satisfying: [RTLearnedRouteFetchOptions isValidRouteFetchType:routeFetchType] (in %s:%d)"
+ "Invalid parameter not satisfying: bundleIdentifier (in %s:%d)"
+ "Invalid parameter not satisfying: bundleIdentifier || bundlePath (in %s:%d)"
+ "Invalid parameter not satisfying: bundlePath (in %s:%d)"
+ "Invalid parameter not satisfying: coder"
+ "Invalid parameter not satisfying: date || machContinuousTimeSec || numberOfSeconds"
+ "Invalid parameter not satisfying: downloadKey"
+ "Invalid parameter not satisfying: encoder (in %s:%d)"
+ "Invalid parameter not satisfying: entryDate"
+ "Invalid parameter not satisfying: exitDate"
+ "Invalid parameter not satisfying: geoTileKey > 0"
+ "Invalid parameter not satisfying: predictedContextTransports"
+ "Invalid parameter not satisfying: reply (in %s:%d)"
+ "Invalid parameter not satisfying: sourceBundleIdentifier"
+ "Invalid parameter not satisfying: submissionDate"
+ "Invalid parameter not satisfying: workoutUUID (in %s:%d)"
+ "IsPresumedAtAuthorizedLocation"
+ "LocalBluePOI"
+ "MUID"
+ "MachContinuousTimeSec: %.3f"
+ "Navigation Notification"
+ "NumberOfSeconds: %u"
+ "POIHistorySynced"
+ "PREDICTED CONTEXT"
+ "Periodic Trigger"
+ "RTAuthorizedLocationConfirmationStatusEnumerationContext"
+ "RTAuthorizedLocationConfirmationStatusEnumerationOptions"
+ "RTAuthorizedLocationDiagnosticStatus"
+ "RTAuthorizedLocationDiagnosticStatusFullConfirmation"
+ "RTAuthorizedLocationDiagnosticStatusZdrConfirmation"
+ "RTAuthorizedLocationZDRLocationsEnumerationContext"
+ "RTAuthorizedLocationZDRLocationsEnumerationOptions"
+ "RTBluePOIMetadata"
+ "RTBluePOITile"
+ "RTBluePOITileDownloadResult"
+ "RTGeoRoadDataEnumerationContext"
+ "RTGeoRoadDataEnumerationOptions"
+ "RTLearnedRoute"
+ "RTLearnedRouteFetchOptions"
+ "RTLearnedRouteLocation"
+ "RTLearnedRouteMetrics"
+ "RTLearnedRouteTravelMode"
+ "RTLocalBluePOIResult"
+ "RTLocationsFromCoreLocationFetchOptions"
+ "RTPointOfInterest"
+ "RTPredictedContext"
+ "RTPredictedContextAnalytics"
+ "RTPredictedContextAnalyticsRolledLOIResult"
+ "RTPredictedContextDate"
+ "RTPredictedContextDateInterval"
+ "RTPredictedContextLocation"
+ "RTPredictedContextOptions"
+ "RTPredictedContextRequest"
+ "RTPredictedContextResult"
+ "RTPredictedContextSequence"
+ "RTPredictedContextTransition"
+ "RTPredictedContextTransport"
+ "RTPredictedContextWorkout"
+ "RTRoutineManager: invoked enumerateElevationsWithOptions:reply:."
+ "RTRoutineManager: invoked fetchLearnedRoutesWithOptions."
+ "RTRoutineManager: invoked fetchTripClusterMetadataWithOptions."
+ "RTRoutineManager: invoked purgeTripClusterTable."
+ "RTRoutineManager: invoked purgeTripClusterWithClusterID."
+ "RTSourceHealthKitWorkout"
+ "RTSourceHomeKit"
+ "RTSourceParkedCar"
+ "RTSourcePropagatedLocation"
+ "RTStoredUserCurationFetchOptions"
+ "RTTripClusterEnumerationContext"
+ "RTTripClusterEnumerationOptions"
+ "RTTripClusterMetadata"
+ "RTTripClusterMetadataFetchOptions"
+ "RTTripClusterRecencyEnumerationContext"
+ "RTTripClusterRecencyEnumerationOptions"
+ "RTTripClusterRoadTransitionsEnumerationContext"
+ "RTTripClusterRoadTransitionsEnumerationOptions"
+ "RTTripClusterRouteEnumerationContext"
+ "RTTripClusterRouteEnumerationOptions"
+ "RTTripClusterScheduleEnumerationContext"
+ "RTTripClusterScheduleEnumerationOptions"
+ "RTUserCuration"
+ "ResultProviderID"
+ "S"
+ "S16@0:8"
+ "Single Shot"
+ "T@\"CLLocation\",C,N,V_destinationVisit"
+ "T@\"CLLocation\",C,N,V_originVisit"
+ "T@\"CLLocation\",R,N,V_learnedRouteEndLocation"
+ "T@\"CLLocation\",R,N,V_learnedRouteStartLocation"
+ "T@\"NSArray\",&,V_fullConfirmationList"
+ "T@\"NSArray\",&,V_zdrConfirmationList"
+ "T@\"NSArray\",R,C,N,V_contexts"
+ "T@\"NSArray\",R,C,N,V_predictedContexts"
+ "T@\"NSArray\",R,N,V_categoryDenyList"
+ "T@\"NSArray\",R,N,V_filterLocations"
+ "T@\"NSArray\",R,N,V_learnedRouteLocations"
+ "T@\"NSArray\",R,N,V_modelURLs"
+ "T@\"NSArray\",R,N,V_predictedContextTransports"
+ "T@\"NSArray\",R,N,V_predictionSources"
+ "T@\"NSArray\",R,N,V_resultSortDescriptors"
+ "T@\"NSArray\",R,N,V_routeLocations"
+ "T@\"NSArray\",R,N,V_travelModeRoutes"
+ "T@\"NSData\",R,N"
+ "T@\"NSData\",R,N,V_downloadKey"
+ "T@\"NSData\",R,N,V_geoCacheInfo"
+ "T@\"NSData\",R,N,V_tileCacheInfo"
+ "T@\"NSDate\",&,N,V_endDate"
+ "T@\"NSDate\",&,N,V_startDate"
+ "T@\"NSDate\",R,C,N,V_dateOfMostRecentTrip"
+ "T@\"NSDate\",R,C,N,V_requestEndDate"
+ "T@\"NSDate\",R,C,N,V_requestStartDate"
+ "T@\"NSDate\",R,C,N,V_routeDate"
+ "T@\"NSDate\",R,N,V_lastTravelledDate"
+ "T@\"NSDate\",R,N,V_parkDate"
+ "T@\"NSDate\",R,N,V_queryTime"
+ "T@\"NSDate\",R,N,V_submissionDate"
+ "T@\"NSDate\",R,N,V_visitEntryDate"
+ "T@\"NSDate\",R,N,V_visitExitDate"
+ "T@\"NSDateInterval\",C,N,V_submissionDateInterval"
+ "T@\"NSDateInterval\",C,N,V_visitDateInterval"
+ "T@\"NSDateInterval\",R,N,V_forecastWindowDateInterval"
+ "T@\"NSDictionary\",R,C,N,V_rolledLOIResult"
+ "T@\"NSDictionary\",R,N,V_aoiConfidences"
+ "T@\"NSDictionary\",R,N,V_apToModelMapping"
+ "T@\"NSDictionary\",R,N,V_modelCalibrationParameters"
+ "T@\"NSDictionary\",R,N,V_poiConfidences"
+ "T@\"NSError\",R,N,V_downloadError"
+ "T@\"NSNumber\",R,C,N,V_machContinuousTimeSec"
+ "T@\"NSNumber\",R,C,N,V_numberOfSeconds"
+ "T@\"NSNumber\",R,N,V_categoryMUID"
+ "T@\"NSNumber\",R,N,V_maximumNumberOfItems"
+ "T@\"NSObject<OS_dispatch_queue>\",&,N,V_xpcQueue"
+ "T@\"NSSet\",R,N,V_pointsOfInterest"
+ "T@\"NSString\",C,N,V_bundleIdentifier"
+ "T@\"NSString\",C,N,V_bundlePath"
+ "T@\"NSString\",R,N,V_identifier"
+ "T@\"NSString\",R,V_sourceBundleIdentifier"
+ "T@\"NSURL\",R,N,V_tileURL"
+ "T@\"NSUUID\",C,N,V_clusterID"
+ "T@\"NSUUID\",C,N,V_tripCommuteID"
+ "T@\"NSUUID\",R,C,N,V_clusterID"
+ "T@\"NSUUID\",R,C,N,V_commuteID"
+ "T@\"NSUUID\",R,N,V_learnedRouteIdentifier"
+ "T@\"NSUUID\",R,N,V_workoutUUID"
+ "T@\"RTAuthorizedLocationConfirmationStatusEnumerationOptions\",R,N,V_options"
+ "T@\"RTAuthorizedLocationZDRLocationsEnumerationOptions\",R,N,V_options"
+ "T@\"RTGeoRoadDataEnumerationOptions\",R,N,V_options"
+ "T@\"RTLearnedRouteLocation\",R,N,V_learnedRouteEndLocationWithReferenceFrame"
+ "T@\"RTLearnedRouteLocation\",R,N,V_learnedRouteStartLocationWithReferenceFrame"
+ "T@\"RTLearnedRouteMetrics\",R,N,V_learnedRouteMetrics"
+ "T@\"RTMapItem\",R,N,V_curatedLabel"
+ "T@\"RTPolygon\",R,N,V_polygon"
+ "T@\"RTPredictedContextAnalytics\",R,C,N,V_analytics"
+ "T@\"RTPredictedContextDate\",R,C,N,V_endDate"
+ "T@\"RTPredictedContextDate\",R,C,N,V_startDate"
+ "T@\"RTPredictedContextDateInterval\",R,C,N,V_dateInterval"
+ "T@\"RTPredictedContextOptions\",&,N,V_predictedContextOptions"
+ "T@\"RTPredictedContextResult\",R,N,V_predictedContextResult"
+ "T@\"RTTripClusterEnumerationOptions\",R,N,V_options"
+ "T@\"RTTripClusterRecencyEnumerationOptions\",R,N,V_options"
+ "T@\"RTTripClusterRoadTransitionsEnumerationOptions\",R,N,V_options"
+ "T@\"RTTripClusterRouteEnumerationOptions\",R,N,V_options"
+ "T@\"RTTripClusterScheduleEnumerationOptions\",R,N,V_options"
+ "T@?,C,N,V_predictedContextHandler"
+ "T@?,C,N,V_remoteStatusHandler"
+ "TB,N,V_isConsumedByClustering"
+ "TB,R,N,V_fetchAllRouteLocations"
+ "TB,R,N,V_filterPairedVisitEntries"
+ "TB,R,N,V_filtered"
+ "TB,R,N,V_followedByUTurn"
+ "TB,R,N,V_fullyCoversTile"
+ "TB,R,N,V_isHome"
+ "TB,R,N,V_isLocked"
+ "TB,R,N,V_isWork"
+ "TB,R,N,V_loiIsMissingFromCurrentVisitHistory"
+ "TB,R,N,V_participationOptional"
+ "TB,R,N,V_primary"
+ "TB,R,N,V_redact"
+ "TB,R,N,V_resultSortProbabilityAscending"
+ "TB,R,N,V_resultSortStartDateAscending"
+ "TB,R,N,V_tentative"
+ "TQ,N,V_mostConfidentAOI"
+ "TQ,N,V_mostConfidentPOI"
+ "TQ,R,N,V_allRoutesCountForThisODPair"
+ "TQ,R,N,V_allTraversalCountBetweenThisODPair"
+ "TQ,R,N,V_clientCount"
+ "TQ,R,N,V_filterContextTypeMask"
+ "TQ,R,N,V_geoTileKey"
+ "TQ,R,N,V_routeTravelCountOnTravelDayOfWeekHourOfDay"
+ "TQ,R,N,V_routeTraversalCount"
+ "TQ,R,N,V_routeTraversalCountOnTravelDayOfWeek"
+ "TQ,R,N,V_singlePOIMuid"
+ "TQ,R,N,V_sortIndex"
+ "TS,N,V_minCountOfTraversal"
+ "Td,N,V_avgBikeDistance"
+ "Td,N,V_avgBikeTime"
+ "Td,N,V_avgWalkDistance"
+ "Td,N,V_avgWalkTime"
+ "Td,N,V_endLatitude"
+ "Td,N,V_endLongitude"
+ "Td,N,V_startLatitude"
+ "Td,N,V_startLongitude"
+ "Td,R,N,V_averageTripDistance"
+ "Td,R,N,V_averageTripTime"
+ "Td,R,N,V_confidenceInterval"
+ "Td,R,N,V_course"
+ "Td,R,N,V_destinationLatitude"
+ "Td,R,N,V_destinationLongitude"
+ "Td,R,N,V_destinationVisitLatitude"
+ "Td,R,N,V_destinationVisitLongitude"
+ "Td,R,N,V_forecastWindowTimeInterval"
+ "Td,R,N,V_likelihood"
+ "Td,R,N,V_maximumTripDistance"
+ "Td,R,N,V_maximumTripTime"
+ "Td,R,N,V_memoryFootprintEnd"
+ "Td,R,N,V_memoryFootprintStart"
+ "Td,R,N,V_minimumTripDistance"
+ "Td,R,N,V_minimumTripTime"
+ "Td,R,N,V_originLatitude"
+ "Td,R,N,V_originLongitude"
+ "Td,R,N,V_originVisitLatitude"
+ "Td,R,N,V_originVisitLongitude"
+ "Td,R,N,V_probability"
+ "Td,R,N,V_size"
+ "Tf,R,N,V_maxTravelTimeEstimateInSeconds"
+ "Tf,R,N,V_maxTravelledDistanceEstimateInMeters"
+ "Tf,R,N,V_meanTravelTimeEstimateInSeconds"
+ "Tf,R,N,V_meanTravelledDistanceEstimateInMeters"
+ "Tf,R,N,V_minTravelTimeEstimateInSeconds"
+ "Tf,R,N,V_minTravelledDistanceEstimateInMeters"
+ "Tf,R,N,V_travelTimeEstimateForEntireRouteInSeconds"
+ "Tf,R,N,V_travelledDistanceEstimateForEntireRouteInMeters"
+ "Ti,N,V_bikeTraversalCount"
+ "Ti,N,V_walkTraversalCount"
+ "Ti,R,N,V_countOfTraversal"
+ "Ti,R,N,V_locationReferenceFrame"
+ "Ti,R,N,V_routeFetchType"
+ "Ti,R,N,V_routeOriginType"
+ "Ti,R,N,V_tripSegmentSequence"
+ "Ti,R,N,V_tripSegmentSequenceMax"
+ "Tq,R,N,V_inferenceTriggerReason"
+ "Tq,R,N,V_modeOfTransport"
+ "Tq,R,N,V_routeTravelMode"
+ "Tq,R,N,V_transportMode"
+ "Tq,R,N,V_workoutActivityType"
+ "Ts,N,V_clusterOrder"
+ "USER CURATION"
+ "UUID,%s,dateInterval,%@,tripDistance,%.1f,tripDistanceUncertainty,%.1f,modeOfTransportation,%llu,isConsumedByClustering,%d,tripSeqNumber,%d,tripSeqNumberMax,%d,originLat,%f,originLon,%f,dstLat,%f,dstLon,%f,tripCommuteID,%s"
+ "Visit Notification"
+ "YYYY-MM-dd HH:mm:ss"
+ "_allRoutesCountForThisODPair"
+ "_allTraversalCountBetweenThisODPair"
+ "_analytics"
+ "_aoiConfidences"
+ "_apToModelMapping"
+ "_averageTripDistance"
+ "_averageTripTime"
+ "_avgBikeDistance"
+ "_avgBikeTime"
+ "_avgWalkDistance"
+ "_avgWalkTime"
+ "_bikeTraversalCount"
+ "_bundleIdentifier"
+ "_bundlePath"
+ "_categoryDenyList"
+ "_categoryMUID"
+ "_clientCount"
+ "_clusterID"
+ "_clusterOrder"
+ "_commuteID"
+ "_confidenceInterval"
+ "_contexts"
+ "_countOfTraversal"
+ "_course"
+ "_curatedLabel"
+ "_dateOfMostRecentTrip"
+ "_destinationLatitude"
+ "_destinationLongitude"
+ "_destinationVisit"
+ "_destinationVisitLatitude"
+ "_destinationVisitLongitude"
+ "_downloadError"
+ "_downloadKey"
+ "_endLatitude"
+ "_endLongitude"
+ "_enumerateElevationsWithOptions:reply:"
+ "_fetchAllRouteLocations"
+ "_filterContextTypeMask"
+ "_filterLocations"
+ "_filterPairedVisitEntries"
+ "_filtered"
+ "_followedByUTurn"
+ "_forecastWindowDateInterval"
+ "_forecastWindowTimeInterval"
+ "_fullConfirmationList"
+ "_fullyCoversTile"
+ "_geoCacheInfo"
+ "_geoTileKey"
+ "_inferenceTriggerReason"
+ "_isConsumedByClustering"
+ "_isHome"
+ "_isLocked"
+ "_isValidClusterOrder:"
+ "_isValidRouteODLocation:routeDestinationLocation:routeFetchType:"
+ "_isWork"
+ "_lastTravelledDate"
+ "_learnedRouteEndLocation"
+ "_learnedRouteEndLocationWithReferenceFrame"
+ "_learnedRouteIdentifier"
+ "_learnedRouteLocations"
+ "_learnedRouteMetrics"
+ "_learnedRouteStartLocation"
+ "_learnedRouteStartLocationWithReferenceFrame"
+ "_likelihood"
+ "_locationReferenceFrame"
+ "_loiIsMissingFromCurrentVisitHistory"
+ "_machContinuousTimeSec"
+ "_maxTravelTimeEstimateInSeconds"
+ "_maxTravelledDistanceEstimateInMeters"
+ "_maximumNumberOfItems"
+ "_maximumTripDistance"
+ "_maximumTripTime"
+ "_meanTravelTimeEstimateInSeconds"
+ "_meanTravelledDistanceEstimateInMeters"
+ "_memoryFootprintEnd"
+ "_memoryFootprintStart"
+ "_minCountOfTraversal"
+ "_minTravelTimeEstimateInSeconds"
+ "_minTravelledDistanceEstimateInMeters"
+ "_minimumTripDistance"
+ "_minimumTripTime"
+ "_modeOfTransport"
+ "_modelCalibrationParameters"
+ "_modelURLs"
+ "_mostConfidentAOI"
+ "_mostConfidentPOI"
+ "_numberOfSeconds"
+ "_originLatitude"
+ "_originLongitude"
+ "_originVisit"
+ "_originVisitLatitude"
+ "_originVisitLongitude"
+ "_parkDate"
+ "_participationOptional"
+ "_peopleDiscoveryRegistrant %@"
+ "_poiConfidences"
+ "_pointsOfInterest"
+ "_polygon"
+ "_predictedContextHandler"
+ "_predictedContextOptions"
+ "_predictedContextResult"
+ "_predictedContextTransports"
+ "_predictedContexts"
+ "_predictionSources"
+ "_primary"
+ "_probability"
+ "_queryTime"
+ "_redact"
+ "_remoteStatusHandler"
+ "_requestEndDate"
+ "_requestStartDate"
+ "_resultSortDescriptors"
+ "_resultSortProbabilityAscending"
+ "_resultSortStartDateAscending"
+ "_rolledLOIResult"
+ "_routeDate"
+ "_routeFetchType"
+ "_routeLocations"
+ "_routeOriginType"
+ "_routeTravelCountOnTravelDayOfWeekHourOfDay"
+ "_routeTravelMode"
+ "_routeTraversalCount"
+ "_routeTraversalCountOnTravelDayOfWeek"
+ "_singlePOIMuid"
+ "_size"
+ "_sortIndex"
+ "_sourceBundleIdentifier"
+ "_startLatitude"
+ "_startLongitude"
+ "_submissionDate"
+ "_submissionDateInterval"
+ "_tentative"
+ "_tileCacheInfo"
+ "_tileURL"
+ "_transportMode"
+ "_travelModeRoutes"
+ "_travelTimeEstimateForEntireRouteInSeconds"
+ "_travelledDistanceEstimateForEntireRouteInMeters"
+ "_tripCommuteID"
+ "_tripSegmentSequence"
+ "_tripSegmentSequenceMax"
+ "_visitDateInterval"
+ "_visitEntryDate"
+ "_visitExitDate"
+ "_walkTraversalCount"
+ "_workoutActivityType"
+ "_workoutUUID"
+ "_xpcQueue"
+ "_zdrConfirmationList"
+ "abbreviatedDescription"
+ "allRoutesCountForThisODPair"
+ "allRoutesCountForThisODPair,%lu,allTraversalCountBetweenThisODPair,%lu,routeTraversalCount,%lu,routeTraversalCountOnTravelDayOfWeek,%lu,routeTravelCountOnTravelDayOfWeekHourOfDay,%lu,lastTravelledDate,%@"
+ "allTraversalCountBetweenThisODPair"
+ "analytics"
+ "aoiConfidences"
+ "apToModelMapping"
+ "archivedDataWithRootObject:requiringSecureCoding:error:"
+ "ascending, %@, confidence, %@, startDate, %@, endDate, %@, labelVisit, %@, limit, %@, redact, %d, filterPairedVisitEntries, %@"
+ "ascending, %@, sortIndex, %lu, submissionStartDate, %@, submissionEndDate, %@, visitStartDate, %@, visitEndDate, %@, limit, %@"
+ "averageTripDistance"
+ "averageTripTime"
+ "avgBikeDistance"
+ "avgBikeTime"
+ "avgTripDistance"
+ "avgTripTime"
+ "avgWalkDistance"
+ "avgWalkTime"
+ "batch size, %ld, end date, %@"
+ "batchSize,%lu,startLat,%.7f,startLon,%.7f,endLat,%.7f,endLon,%.7f,minCntTraversal,%d"
+ "bikeTraversalCount"
+ "bundleIdentifier"
+ "bundlePath"
+ "categoryDenyList"
+ "categoryMUID"
+ "clientCount"
+ "clusterID"
+ "clusterId"
+ "clusterId,%@,mostRecentTripDate,%@,modeOfTransport,%d,countOfTraversal,%d,originLat,%0.6f,originLon,%0.6f,destLat,%0.6f,destLon,%0.6f,avgTripTime,%0.2f,avgTripDistance,%0.2f,minTripTime,%0.2f,maxTripTime,%0.2f,minTripDistance,%0.2f,maxTripDistance,%0.2f,commuteID,%@,isLocked,%d,bikeTime,%0.2f,bikeDist,%02.f,walkTime,%0.2f,walkDist,%0.2f,cntBikeTravel,%d,cntWalkTravel,%d,clusterOrder,%d"
+ "clusterOrder"
+ "commuteID"
+ "confidenceInterval"
+ "contextTypeForContext:"
+ "contextTypeMaskForContext:"
+ "contexts"
+ "contexts, %lu"
+ "correctLabelForCurrentPlace:date:newLabel:handler:"
+ "correctLabelForVisitWithIdentifier:entryDate:originalLabel:newLabel:handler:"
+ "countOfTravel"
+ "countOfTraversal"
+ "course"
+ "creating _peopleDiscoveryRegistrant initWithConfigurationIdentifier %@"
+ "curatedLabel"
+ "currentPredictedContextsWithType:"
+ "dataRepresentation"
+ "dataWithBytes:length:"
+ "date, %@, confidenceInterval, %.2f"
+ "date, %@, type, %@, location, %@, entry, %@, exit, %@, dataPointCount, %lu, confidence, %.2f, placeInference, %@, source, %lu, identifier, %@"
+ "dateFormatterForLogging"
+ "dateInterval, %@, probability, %.2f, predictionSources, %@"
+ "dateInterval.startDate.date"
+ "dateIntervalFromStart:end:"
+ "dateOfMostRecentTrip"
+ "dateWithTimeInterval:sinceDate:"
+ "decodeDictionaryWithKeysOfClass:objectsOfClass:forKey:"
+ "decodeFloatForKey:"
+ "decodeInt32ForKey:"
+ "deriveConfidenceFromRouteMetric:"
+ "destinationLatitude"
+ "destinationLongitude"
+ "destinationVisit"
+ "destinationVisitLat"
+ "destinationVisitLatitude"
+ "destinationVisitLon"
+ "destinationVisitLongitude"
+ "downloadError"
+ "downloadKey"
+ "downloadKey, %@, tileURL, %@, tileCacheInfo, %@, downloadError, %@"
+ "en_US_POSIX"
+ "encodeFloat:forKey:"
+ "encodeInt32:forKey:"
+ "endLatitude"
+ "endLongitude"
+ "entry date is not Jan 1 2001 and will result in unexpected behavior, %@"
+ "enumerateElevationsWithOptions:reply:"
+ "f"
+ "f16@0:8"
+ "fetchAllRouteLoc"
+ "fetchAllRouteLoc,%d,origVisit,%@,dstVisit,%@,routeDate,%@,routeFetchType,%d,currLocFlag,%d,bundleID,%@,bundlePath,%@"
+ "fetchAllRouteLocations"
+ "fetchElevationsWithContext:reply:"
+ "fetchLearnedRoutesWithOptions:handler:"
+ "fetchLearnedRoutesWithOptions:reply:"
+ "fetchPredictedContextWithOptions:completionHandler:"
+ "fetchPredictedContextWithOptions:reply:"
+ "fetchTripClusterMetadataWithOptions:handler:"
+ "fetchTripClusterMetadataWithOptions:reply:"
+ "fetchType"
+ "filterContextTypeMask"
+ "filterLocations"
+ "filterPairedVisitEntries"
+ "filtered"
+ "followedByUTurn"
+ "forecastWindowDateInterval"
+ "forecastWindowDateInterval, %@, forecastWindowTimeInterval %f, filterContextTypeMask, %lu, filterLocations, %@, resultSortDescriptors, %@"
+ "forecastWindowTimeInterval"
+ "fullConfirmationList"
+ "fullyCoversTile"
+ "generateSequencesFromDate:toDate:"
+ "geoCacheInfo"
+ "geoMapItemIdentifier"
+ "geoTileKey"
+ "getUUIDBytes:"
+ "highThresholdAfterCalibrationApplePay"
+ "highThresholdAfterCalibrationNonApplePay"
+ "highThresholdBeforeCalibrationApplePay"
+ "highThresholdBeforeCalibrationNonApplePay"
+ "highestScoreApplePay"
+ "highestScoreNonApplePay"
+ "identifier, %@, date, %@, geoTileKey, %@, downloadKey, %@, geoCacheInfo, %@, size, %.1f kB, apToModelMapping count, %lu, singlePOIMuid, %@, model URLs, %@, modelCalibrationParameters, %@, pointsOfInterest, %@"
+ "identifier, %@, geoMapItemIdentifier, %@, name, \"%@\", category, %@, categoryMUID, %@, address, %@, location, %@, source, %@, map item place type, %@, muid, %lu, result provider ID: %ld, weight, %lf, creationDate, %@, extended attributes, %@, display language, %@, disputed, %@"
+ "identifier, %@, loiIsMissingFromCurrentVisitHistory, %lu, isHome, %lu, isWork, %lu"
+ "identifier, %@, model calibration parameters, %@, category deny list count, %lu, geoCacheInfo, %@"
+ "identifier, %@, muid, %lu, location, %@, applyPaySupport, %@, filtered, %@, fullyCoversTile, %@, polygon, %@"
+ "identifier, %@, predictedContextResult, %@, requestStartDate, %@, requestEndDate, %@, latency, %.2f, inferenceTriggerReason, %@, memoryFootprintStart, %.4f MB, memoryFootprintEnd, %.4f MB, clientCount, %lu"
+ "identifier, %@, submissionDate, %@, expirationDate, %@, entry time, %@, exit time, %@, curated label, %@"
+ "inferenceTriggerReason"
+ "inferenceTriggerReasonToString"
+ "initWithAllRoutesCountForThisODPair:allTraversalCountBetweenThisODPair:routeTraversalCount:routeTraversalCountOnTravelDayOfWeek:routeTravelCountOnTravelDayOfWeekHourOfDay:lastTravelledDate:"
+ "initWithAscending:confidence:dateInterval:labelVisit:limit:sources:redact:"
+ "initWithAscending:confidence:dateInterval:labelVisit:limit:sources:redact:filterPairedVisitEntries:"
+ "initWithAscending:limit:"
+ "initWithAscending:sortIndex:limit:"
+ "initWithAscending:sortIndex:submissionDateInterval:visitDateInterval:limit:"
+ "initWithAscending:submissionDateInterval:limit:"
+ "initWithAscending:visitDateInterval:limit:"
+ "initWithBundleIdentifier:bundlePath:routeOriginLocation:routeDestinationLocation:routeDate:routeFetchType:fetchAllRouteLocations:routeOriginType:"
+ "initWithBundleIdentifier:routeOriginLocation:routeDestinationLocation:routeDate:routeFetchType:fetchAllRouteLocations:routeOriginType:"
+ "initWithBundlePath:routeOriginLocation:routeDestinationLocation:routeDate:routeFetchType:fetchAllRouteLocations:routeOriginType:"
+ "initWithClusterID:"
+ "initWithDate:confidenceInterval:"
+ "initWithDate:machContinuousTimeSec:numberOfSeconds:"
+ "initWithDate:type:location:entry:exit:dataPointCount:confidence:placeInference:source:identifier:"
+ "initWithDateInterval:predictionSources:probability:sourceBundleIdentifier:workoutActivityType:"
+ "initWithDownloadKey:tileURL:tileCacheInfo:downloadError:"
+ "initWithEndVisitLatitude:endLongitude:"
+ "initWithEventIdentifier:startDate:endDate:title:location:allDay:sharingStatus:tentative:participationOptional:suggestionInfo_opaqueKey:suggestionsSchemaOrg:"
+ "initWithForecastWindowDateInterval:filterContextTypeMask:filterLocations:resultSortDescriptors:"
+ "initWithForecastWindowDateInterval:filterContextTypeMask:filterLocations:resultSortStartDateAscending:resultSortProbabilityAscending:"
+ "initWithForecastWindowDateInterval:forecastWindowTimeInterval:filterContextTypeMask:filterLocations:resultSortDescriptors:"
+ "initWithForecastWindowTimeInterval:filterContextTypeMask:filterLocations:resultSortDescriptors:"
+ "initWithIdentifier:apToModelMapping:date:downloadKey:geoCacheInfo:geoTileKey:modelCalibrationParameters:modelURLs:pointsOfInterest:singlePOIMuid:size:"
+ "initWithIdentifier:applePaySupport:filtered:fullyCoversTile:location:muid:polygon:"
+ "initWithIdentifier:categoryDenyList:geoCacheInfo:modelCalibrationParameters:"
+ "initWithIdentifier:loiIsMissingFromCurrentVisitHistory:isHome:isWork:"
+ "initWithIdentifier:name:category:categoryMUID:address:location:source:mapItemPlaceType:muid:resultProviderID:geoMapItemHandle:creationDate:expirationDate:extendedAttributes:displayLanguage:disputed:"
+ "initWithIdentifier:parkDate:"
+ "initWithIdentifier:predictedContextResult:requestStartDate:requestEndDate:inferenceTriggerReason:memoryFootprintStart:memoryFootprintEnd:clientCount:"
+ "initWithIdentifier:primary:"
+ "initWithIdentifier:submissionDate:expirationDate:entryDate:exitDate:curatedLabel:"
+ "initWithLatitude:longitude:course:followedByUTurn:locationReferenceFrame:"
+ "initWithLearnedRouteId:routeStartLocation:routeEndLocation:travelTimeEntireRouteSec:travelDistanceEntireRouteMeter:travelModeRoutes:routeStartLocationWithReferenceFrame:routeEndLocationWithReferenceFrame:"
+ "initWithLocationOfInterest:dateInterval:predictionSources:probability:"
+ "initWithMUID:coordinate:"
+ "initWithMachContinuousTimeSec:"
+ "initWithMinCountOfTraversal:startLatitude:startLongitude:endLatitude:endLongitude:"
+ "initWithNumberOfSeconds:"
+ "initWithOptions:startDate:endDate:"
+ "initWithOptions:startDate:endDate:maximumNumberOfItems:"
+ "initWithOriginVisitLatitude:originVisitLongitude:destinationVisitLatitude:destinationVisitLongitude:"
+ "initWithPOIConfidences:aoiConfidences:referenceLocation:queryTime:"
+ "initWithPredictedContextDateInterval:predictionSources:probability:"
+ "initWithPredictedContextTransports:predictedContextDateInterval:predictionSources:probability:"
+ "initWithPredictedContexts:analytics:"
+ "initWithProbability:dateInterval:predictedContexts:"
+ "initWithRolledLOIResult:"
+ "initWithRouteTravelMode:maxTravelTimeEstimateInSeconds:minTravelTimeEstimateInSeconds:meanTravelTimeEstimateInSeconds:maxTravelledDistanceEstimateInMeters:minTravelledDistanceEstimateInMeters:meanTravelledDistanceEstimateInMeters:routeLocations:learnedRouteLocations:learnedRouteMetrics:"
+ "initWithStartAndEndVisitLatitude:startLongitude:endLatitude:endLongitude:"
+ "initWithStartVisitLatitude:startLongitude:"
+ "initWithStartVisitLatitude:startVisitLongitude:endVisitLatitude:endVisitLongitude:"
+ "initWithStatus:zdrConfirmationList:"
+ "initWithTransportMode:probability:"
+ "initWithTripClusterId:dateOfMostRecentTrip:modeOfTransport:countOfTraversal:originLatitude:originLongitude:destinationLatitude:destinationLongitude:averageTripTime:averageTripDistance:minimumTripTime:maximumTripTime:minimumTripDistance:maximumTripDistance:commuteID:isLocked:avgBikeDistance:avgBikeTime:avgWalkDistance:avgWalkTime:bikeTraversalCount:walkTraversalCount:clusterOrder:"
+ "initWithTripSegmentIdentifier:dateInterval:tripDistance:tripDistanceUncertainty:modeOfTransportation:isConsumedByClustering:tripSegmentSequence:tripSegmentSequenceMax:originLatitude:originLongitude:destinationLatitude:destinationLongitude:tripCommuteID:"
+ "initWithWorkoutUUID:startDate:"
+ "initWithbatchSize:"
+ "isConsumedByClustering"
+ "isEqualToData:"
+ "isEqualToDictionary:"
+ "isEqualToUserCuration:"
+ "isHome"
+ "isLocked"
+ "isValidRouteFetchType:"
+ "isWork"
+ "iterating stored elevations between %@, batch size, %lu, offset, %lu"
+ "key"
+ "lastTravelledDate"
+ "lat,%.7f,lon,%.7f,course,%.3f,locationReferenceFrame,%d,followedByUTurn,%d"
+ "learnedRouteEndLocation"
+ "learnedRouteEndLocationWithReferenceFrame"
+ "learnedRouteIdentifier"
+ "learnedRouteLocations"
+ "learnedRouteMetrics"
+ "learnedRouteStartLocation"
+ "learnedRouteStartLocationWithReferenceFrame"
+ "likelihood"
+ "localeWithLocaleIdentifier:"
+ "locationOfInterest, %@, %@"
+ "locationReference"
+ "locationReferenceFrame"
+ "loiIsMissingFromCurrentVisitHistory"
+ "loiMissing"
+ "lowThresholdAfterCalibrationApplePay"
+ "lowThresholdAfterCalibrationNonApplePay"
+ "lowThresholdBeforeCalibrationApplePay"
+ "lowThresholdBeforeCalibrationNonApplePay"
+ "machContinuousTimeSec"
+ "maskForSources:"
+ "maxTravelDistance"
+ "maxTravelTime"
+ "maxTravelTimeEstimateInSeconds"
+ "maxTravelledDistanceEstimateInMeters"
+ "maxTripDistance"
+ "maxTripTime"
+ "maximumNumberOfItems"
+ "maximumTripDistance"
+ "maximumTripTime"
+ "meanTravelDistance"
+ "meanTravelTime"
+ "meanTravelTimeEstimateInSeconds"
+ "meanTravelledDistanceEstimateInMeters"
+ "memoryFootprintEnd"
+ "memoryFootprintStart"
+ "minCountOfTraversal"
+ "minTravelDistance"
+ "minTravelTime"
+ "minTravelTimeEstimateInSeconds"
+ "minTravelledDistanceEstimateInMeters"
+ "minTripDistance"
+ "minTripTime"
+ "minimumTripDistance"
+ "minimumTripTime"
+ "modeOfTransport"
+ "modelCalibrationHighConfidence"
+ "modelCalibrationHighThreshold"
+ "modelCalibrationLowConfidence"
+ "modelCalibrationLowThreshold"
+ "modelCalibrationParameters"
+ "modelURLs"
+ "month"
+ "mostConfidentAOI"
+ "mostConfidentPOI"
+ "mostRecentDate"
+ "nextStepPredictedContexts:"
+ "nextStepPredictedContextsWithFilterMask:"
+ "numberOfSeconds"
+ "numberWithUnsignedLongLong:"
+ "numberWithUnsignedShort:"
+ "onPredictedContextResult:error:"
+ "onRemoteStatusUpdate:error:"
+ "originLatitude"
+ "originLongitude"
+ "originVisit"
+ "originVisitLat"
+ "originVisitLat,%0.6f,originVisitLon,%0.6f,destinationVisitLat,%0.6f,destinationVisitLon,%0.6f"
+ "originVisitLatitude"
+ "originVisitLon"
+ "originVisitLongitude"
+ "parkDate"
+ "participationOptional"
+ "poiConfidences"
+ "poiConfidences, %@, aoiConfidences, %@, referenceLocation, %@, queryTime, %@"
+ "pointsOfInterest"
+ "polygon"
+ "predictedContextHandler"
+ "predictedContextOptions"
+ "predictedContextResult"
+ "predictedContextTransports"
+ "predictedContextTransports, %@, %@"
+ "predictedContexts"
+ "predictedContextsWithType:afterContext:"
+ "predictedSequencesAfterContext:"
+ "predictedTransportMode, %lu, probability, %.2f"
+ "predictionSources"
+ "primary"
+ "probability"
+ "probability, %f, dateInterval, %@, predictedContexts, %@"
+ "purgeTripClusterTable:handler:"
+ "purgeTripClusterTable:reply:"
+ "purgeTripClusterWithClusterID:handler:"
+ "purgeTripClusterWithClusterID:reply:"
+ "queryTime"
+ "redact"
+ "remoteStatusHandler"
+ "requestEndDate"
+ "requestStartDate"
+ "resultSortDescriptors"
+ "resultSortProbabilityAscending"
+ "resultSortStartDateAscending"
+ "rolledLOIResult"
+ "rolledLOIResult.count, %lu"
+ "routeDate"
+ "routeEndLocation"
+ "routeEndLocationWithReferenceFrame"
+ "routeFetchType"
+ "routeId"
+ "routeId,%@,startLocation,%@,endLocation,%@,totalRouteTimeSec,%0.6f,totalRouteDistanceMeters,%0.6f,numberOfTravelModeRoutes,%lu,startLocationWithRefFrame,%@,endLocationWithRefFrame,%@"
+ "routeLocations"
+ "routeOriginType"
+ "routeStartLocation"
+ "routeStartLocationWithReferenceFrame"
+ "routeTravelCountOnTravelDayOfWeekHourOfDay"
+ "routeTravelMode"
+ "routeTraversalCount"
+ "routeTraversalCountOnTravelDayOfWeek"
+ "s"
+ "s16@0:8"
+ "selector"
+ "setAvgBikeDistance:"
+ "setAvgBikeTime:"
+ "setAvgWalkDistance:"
+ "setAvgWalkTime:"
+ "setBikeTraversalCount:"
+ "setBundleIdentifier:"
+ "setBundlePath:"
+ "setClusterID:"
+ "setClusterOrder:"
+ "setDestinationVisit:"
+ "setEndDate:"
+ "setEndLatitude:"
+ "setEndLongitude:"
+ "setFullConfirmationList:"
+ "setIsConsumedByClustering:"
+ "setLikelihood:"
+ "setMinCountOfTraversal:"
+ "setMostConfidentAOI:"
+ "setMostConfidentPOI:"
+ "setOriginVisit:"
+ "setPredictedContextHandler:"
+ "setPredictedContextOptions:"
+ "setRemoteStatusHandler:"
+ "setStartDate:"
+ "setStartLatitude:"
+ "setStartLongitude:"
+ "setSubmissionDateInterval:"
+ "setTripCommuteID:"
+ "setVisitDateInterval:"
+ "setWalkTraversalCount:"
+ "setWithArray:"
+ "setXpcQueue:"
+ "setZdrConfirmationList:"
+ "singlePOIMuid"
+ "size"
+ "sortDescriptorWithKey:ascending:selector:"
+ "sortIndex"
+ "sourceBundleIdentifier"
+ "sourceBundleIdentifier, %@, workoutActivityType, %lld, %@"
+ "startDate, %@, endDate, %@"
+ "startLatitude"
+ "startLongitude"
+ "startMonitoringForPeopleDiscoveryWithIdentifier:configuration:reply:"
+ "startMonitoringPredictedContextWithOptions:completionHandler:"
+ "startMonitoringPredictedContextWithOptions:reply:"
+ "startMonitoringRemoteStatusWithHandler:"
+ "startMonitoringRemoteStatusWithReply:"
+ "startOfDayAfterAddingUnit:value:"
+ "startOfDayForDate:"
+ "stopMonitoringForPeopleDiscoveryWithIdentifier:reply:"
+ "stopMonitoringPredictedContextWithHandler:"
+ "stopMonitoringPredictedContextWithReply:"
+ "stopMonitoringRemoteStatusWithHandler:"
+ "stopMonitoringRemoteStatusWithReply:"
+ "submissionDate"
+ "submissionDateInterval"
+ "submitUserCurationForDate:newLabel:handler:"
+ "submitUserCurationForVisitDateRange:newLabel:handler:"
+ "tentative"
+ "tileCacheInfo"
+ "tileURL"
+ "transportMode"
+ "travelDistanceEntireRouteMeter"
+ "travelMode"
+ "travelMode,%ld,maxTravelTime,%0.3f,minTravelTime,%0.3f,meanTravelTime,%0.3f,maxTravelDistance,%0.3f,minTravelDistance,%0.3f,meanTravelDistance,%0.3f,routeLocationCount,%lu,learnedRouteLocationCount,%lu,learnedRouteMetrics,%@"
+ "travelModeRoutes"
+ "travelTimeEntireRouteSec"
+ "travelTimeEstimateForEntireRouteInSeconds"
+ "travelledDistanceEstimateForEntireRouteInMeters"
+ "tripCommuteID"
+ "tripSegmentFormOfWay, %{sensitive}@"
+ "tripSegmentRoadClass, %{sensitive}@"
+ "tripSegmentSequence"
+ "tripSegmentSequenceMax"
+ "tripSequenceNumber"
+ "tripSequenceNumberMax"
+ "unarchivedObjectOfClass:fromData:error:"
+ "unknownPredictedContextFromStart:end:"
+ "unsignedLongLongValue"
+ "v20@0:8S16"
+ "v20@0:8s16"
+ "v24@?0@\"NSDictionary\"8@\"NSError\"16"
+ "v24@?0@\"RTPredictedContextResult\"8@\"NSError\"16"
+ "v32@0:8@\"NSNumber\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@\"NSString\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@\"RTLearnedRouteFetchOptions\"16@?<v@?@\"NSArray\"^B@\"NSError\">24"
+ "v32@0:8@\"RTPredictedContextOptions\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@\"RTPredictedContextOptions\"16@?<v@?@\"RTPredictedContextResult\"@\"NSError\">24"
+ "v32@0:8@\"RTPredictedContextResult\"16@\"NSError\"24"
+ "v32@0:8@\"RTStoredElevationEnumerationContext\"16@?<v@?@\"NSArray\"@\"NSError\">24"
+ "v32@0:8@\"RTTripClusterMetadataFetchOptions\"16@?<v@?@\"NSArray\"@\"NSError\">24"
+ "v32@0:8q16@\"NSError\"24"
+ "v32@0:8q16@24"
+ "v32@?0@\"NSArray\"8^B16@\"NSError\"24"
+ "v32@?0@\"RTPredictedContextSequence\"8Q16^B24"
+ "v32@?0@\"RTSource\"8Q16^B24"
+ "v40@0:8@\"NSDateInterval\"16@\"GEOMapItemStorage\"24@?<v@?@\"NSError\">32"
+ "v56@0:8@\"NSUUID\"16@\"NSDate\"24@\"GEOMapItemStorage\"32@\"GEOMapItemStorage\"40@?<v@?@\"NSError\">48"
+ "v56@0:8@16@24@32@40@?48"
+ "visitDateInterval"
+ "visitEntryDate"
+ "visitExitDate"
+ "walkTraversalCount"
+ "workoutActivityType"
+ "workoutUUID"
+ "xpcQueue"
+ "year"
+ "zdrConfirmationList"
- "%@ %@, dateInterval,%@,fetchRoadClass,%d,fetchFormOfWay,%d,fetchLocationType,%d,fetchPreferredNames,%d"
- "%@ XPC Connection wasn't to use self.queue. (in %s:%d)"
- "%@, eventIdentifier, %@, startDate, %@, endDate, %@, title, %@, location %@, sharingStatus, %@, suggestionsSchemaOrg, %@"
- "-[RTRoutineManager _enumerateStoredLocationsWithOptions:usingBlock:]_block_invoke"
- "@132@0:8@16@24@32@40@48Q56Q64Q72q80@88@96@104@112@120B128"
- "@56@0:8@16@24d32d40q48"
- "@84@0:8@16@24@32@40@48B56Q60@68@76"
- "B24@?0@\"NSString\"8@\"NSDictionary\"16"
- "RT"
- "Semaphore wait timed out, we're hung!"
- "UUID,%s,dateInterval,%@,tripDistance,%.1f,tripDistanceUncertainty,%.1f,modeOfTransportation,%llu"
- "XPC timeout error while waiting for stored locations, %@."
- "ascending, %@, confidence, %@, startDate, %@, endDate, %@, labelVisit, %@, limit, %@"
- "containsString:"
- "date, %@, type, %@, location, %@, entry, %@, exit, %@, dataPointCount, %lu, confidence, %.2f, placeInference, %@, source, %lu"
- "fetchLocationsHelperQueue"
- "identifier, %@, name, \"%@\", category, %@, address, %@, location, %@, source, %@, map item place type, %@, muid, %lu, result provider ID: %ld, weight, %lf, creationDate, %@, extended attributes, %@, display language, %@, disputed, %@"
- "initWithEventIdentifier:startDate:endDate:title:location:allDay:sharingStatus:suggestionInfo_opaqueKey:suggestionsSchemaOrg:"
- "initWithIdentifier:name:category:address:location:source:mapItemPlaceType:muid:resultProviderID:geoMapItemHandle:creationDate:expirationDate:extendedAttributes:displayLanguage:disputed:"
- "initWithTripSegmentIdentifier:dateInterval:tripDistance:tripDistanceUncertainty:modeOfTransportation:"
- "rdar122420473 _peopleDiscoveryRegistrant %@"
- "rdar122420473 creating _peopleDiscoveryRegistrant initWithConfigurationIdentifier %@"
- "semaphore wait timeout"
- "startMonitoringForPeopleDiscovery:configuration:reply:"
- "stopMonitoringForPeopleDiscoveryWithReply:"
- "tripSegmentFormOfWay, %@"
- "tripSegmentRoadClass, %@"

```
