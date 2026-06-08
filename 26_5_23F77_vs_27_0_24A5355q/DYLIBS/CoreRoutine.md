## CoreRoutine

> `/System/Library/PrivateFrameworks/CoreRoutine.framework/CoreRoutine`

```diff

-1075.0.2.0.0
-  __TEXT.__text: 0x697a8
-  __TEXT.__auth_stubs: 0x630
-  __TEXT.__objc_methlist: 0x80a0
+1109.0.3.0.0
+  __TEXT.__text: 0x6d484
+  __TEXT.__objc_methlist: 0x8b90
   __TEXT.__const: 0x2c8
-  __TEXT.__oslogstring: 0x34c8
-  __TEXT.__cstring: 0x6716
+  __TEXT.__oslogstring: 0x35c8
+  __TEXT.__cstring: 0x7657
   __TEXT.__gcc_except_tab: 0x340
-  __TEXT.__unwind_info: 0x2030
-  __TEXT.__objc_classname: 0xffb
-  __TEXT.__objc_methname: 0xf455
-  __TEXT.__objc_methtype: 0x2786
-  __TEXT.__objc_stubs: 0x77c0
-  __DATA_CONST.__got: 0x4b8
-  __DATA_CONST.__const: 0x1290
-  __DATA_CONST.__objc_classlist: 0x478
+  __TEXT.__unwind_info: 0x2018
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x14b8
+  __DATA_CONST.__objc_classlist: 0x4d0
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2938
+  __DATA_CONST.__objc_selrefs: 0x2be0
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x440
+  __DATA_CONST.__objc_superrefs: 0x498
   __DATA_CONST.__objc_arraydata: 0x98
-  __AUTH_CONST.__auth_got: 0x328
-  __AUTH_CONST.__const: 0x3c0
-  __AUTH_CONST.__cfstring: 0x5b60
-  __AUTH_CONST.__objc_const: 0xe7c0
+  __DATA_CONST.__got: 0x540
+  __AUTH_CONST.__const: 0x3a0
+  __AUTH_CONST.__cfstring: 0x64a0
+  __AUTH_CONST.__objc_const: 0xfdb0
+  __AUTH_CONST.__objc_intobj: 0x120
   __AUTH_CONST.__objc_doubleobj: 0x20
-  __AUTH_CONST.__objc_intobj: 0xa8
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_dictobj: 0x50
-  __AUTH.__objc_data: 0x1590
-  __DATA.__objc_ivar: 0x83c
-  __DATA.__data: 0x308
-  __DATA_DIRTY.__objc_ivar: 0x130
-  __DATA_DIRTY.__objc_data: 0x1720
+  __AUTH_CONST.__auth_got: 0x0
+  __AUTH.__objc_data: 0x15e0
+  __DATA.__objc_ivar: 0x91c
+  __DATA.__data: 0x2e8
+  __DATA_DIRTY.__objc_ivar: 0x160
+  __DATA_DIRTY.__objc_data: 0x1a40
   __DATA_DIRTY.__data: 0x30
   __DATA_DIRTY.__bss: 0x50
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/Frameworks/_LocationEssentials.framework/_LocationEssentials
-  - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
+  - /System/Library/PrivateFrameworks/CoreRoutineDiagnostics.framework/CoreRoutineDiagnostics
   - /System/Library/PrivateFrameworks/GeoServices.framework/GeoServices
+  - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 0727AA75-27D8-3BFB-BFB6-42EE2A70E1A0
-  Functions: 2874
-  Symbols:   8966
-  CStrings:  4529
+  UUID: BB875924-5A00-3410-A17D-F135E1386C7B
+  Functions: 3095
+  Symbols:   9680
+  CStrings:  2017
 
Symbols:
+ +[RTAltimeterFloorMapData supportsSecureCoding]
+ +[RTAltimeterFloorMapDataEnumerationContext supportsSecureCoding]
+ +[RTAltimeterFloorMapDataEnumerationOptions supportsSecureCoding]
+ +[RTAltimeterFloorMapEntry supportsSecureCoding]
+ +[RTAltimeterFloorMapTransitionModel supportsSecureCoding]
+ +[RTBluePOIModernCategory supportsSecureCoding]
+ +[RTDataIntegrityValidationResult supportsSecureCoding]
+ +[RTMapItem categoryDescriptionFromCategory:]
+ +[RTPointOfInterest descriptionForPopularityTier:]
+ +[RTRawAltimeterData supportsSecureCoding]
+ +[RTRawAltimeterDataEnumerationContext supportsSecureCoding]
+ +[RTRawAltimeterDataEnumerationOptions supportsSecureCoding]
+ +[RTRoutineManager isInternalInstall]
+ +[RTTripClusterRouteSummaryEnumerationContext supportsSecureCoding]
+ +[RTTripClusterRouteSummaryEnumerationOptions supportsSecureCoding]
+ -[NSDate(RTExtensions) filenameDateString]
+ -[RTAltimeterFloorMapData .cxx_destruct]
+ -[RTAltimeterFloorMapData copyWithZone:]
+ -[RTAltimeterFloorMapData description]
+ -[RTAltimeterFloorMapData encodeWithCoder:]
+ -[RTAltimeterFloorMapData endTime]
+ -[RTAltimeterFloorMapData expirationDate]
+ -[RTAltimeterFloorMapData floorMapArray]
+ -[RTAltimeterFloorMapData hash]
+ -[RTAltimeterFloorMapData initWithAltimeterFloorMapData:startTime:endTime:type:referenceUUID:floorMapArray:transitionModels:]
+ -[RTAltimeterFloorMapData initWithAltimeterFloorMapData:startTime:endTime:type:referenceUUID:floorMapArray:transitionModels:expirationDate:]
+ -[RTAltimeterFloorMapData initWithCoder:]
+ -[RTAltimeterFloorMapData isEqual:]
+ -[RTAltimeterFloorMapData referenceUUID]
+ -[RTAltimeterFloorMapData startTime]
+ -[RTAltimeterFloorMapData transitionModels]
+ -[RTAltimeterFloorMapData type]
+ -[RTAltimeterFloorMapData uuid]
+ -[RTAltimeterFloorMapDataEnumerationContext .cxx_destruct]
+ -[RTAltimeterFloorMapDataEnumerationContext copyWithZone:]
+ -[RTAltimeterFloorMapDataEnumerationContext description]
+ -[RTAltimeterFloorMapDataEnumerationContext encodeWithCoder:]
+ -[RTAltimeterFloorMapDataEnumerationContext initWithCoder:]
+ -[RTAltimeterFloorMapDataEnumerationContext initWithEnumerationOptions:]
+ -[RTAltimeterFloorMapDataEnumerationContext initWithEnumerationOptions:offset:]
+ -[RTAltimeterFloorMapDataEnumerationContext init]
+ -[RTAltimeterFloorMapDataEnumerationContext offset]
+ -[RTAltimeterFloorMapDataEnumerationContext options]
+ -[RTAltimeterFloorMapDataEnumerationOptions .cxx_destruct]
+ -[RTAltimeterFloorMapDataEnumerationOptions copyWithZone:]
+ -[RTAltimeterFloorMapDataEnumerationOptions description]
+ -[RTAltimeterFloorMapDataEnumerationOptions encodeWithCoder:]
+ -[RTAltimeterFloorMapDataEnumerationOptions endDate]
+ -[RTAltimeterFloorMapDataEnumerationOptions expirationDateBefore]
+ -[RTAltimeterFloorMapDataEnumerationOptions initWithCoder:]
+ -[RTAltimeterFloorMapDataEnumerationOptions initWithStartDate:endDate:maximumNumberOfItems:]
+ -[RTAltimeterFloorMapDataEnumerationOptions initWithStartDate:endDate:maximumNumberOfItems:referenceUUID:]
+ -[RTAltimeterFloorMapDataEnumerationOptions init]
+ -[RTAltimeterFloorMapDataEnumerationOptions maximumNumberOfItems]
+ -[RTAltimeterFloorMapDataEnumerationOptions referenceUUID]
+ -[RTAltimeterFloorMapDataEnumerationOptions setEndDate:]
+ -[RTAltimeterFloorMapDataEnumerationOptions setExpirationDateBefore:]
+ -[RTAltimeterFloorMapDataEnumerationOptions setMaximumNumberOfItems:]
+ -[RTAltimeterFloorMapDataEnumerationOptions setReferenceUUID:]
+ -[RTAltimeterFloorMapDataEnumerationOptions setStartDate:]
+ -[RTAltimeterFloorMapDataEnumerationOptions startDate]
+ -[RTAltimeterFloorMapEntry copyWithZone:]
+ -[RTAltimeterFloorMapEntry description]
+ -[RTAltimeterFloorMapEntry duration]
+ -[RTAltimeterFloorMapEntry elevationUncertainty]
+ -[RTAltimeterFloorMapEntry elevation]
+ -[RTAltimeterFloorMapEntry encodeWithCoder:]
+ -[RTAltimeterFloorMapEntry floorIndex]
+ -[RTAltimeterFloorMapEntry hash]
+ -[RTAltimeterFloorMapEntry initWithCoder:]
+ -[RTAltimeterFloorMapEntry initWithFloorMapEntry:elevation:elevationUncertainty:initialFloorProbability:duration:]
+ -[RTAltimeterFloorMapEntry initialFloorProbability]
+ -[RTAltimeterFloorMapEntry isEqual:]
+ -[RTAltimeterFloorMapTransitionModel averageSteps]
+ -[RTAltimeterFloorMapTransitionModel copyWithZone:]
+ -[RTAltimeterFloorMapTransitionModel description]
+ -[RTAltimeterFloorMapTransitionModel elevationChangeStandardDeviation]
+ -[RTAltimeterFloorMapTransitionModel encodeWithCoder:]
+ -[RTAltimeterFloorMapTransitionModel endFloorIndex]
+ -[RTAltimeterFloorMapTransitionModel hash]
+ -[RTAltimeterFloorMapTransitionModel initWithCoder:]
+ -[RTAltimeterFloorMapTransitionModel initWithTransitionModel:endFloorIndex:meanElevationChange:elevationChangeStandardDeviation:meanTransitionTime:transitionTimeStandardDeviation:averageSteps:standardDeviationSteps:occurrenceCount:]
+ -[RTAltimeterFloorMapTransitionModel isEqual:]
+ -[RTAltimeterFloorMapTransitionModel meanElevationChange]
+ -[RTAltimeterFloorMapTransitionModel meanTransitionTime]
+ -[RTAltimeterFloorMapTransitionModel occurrenceCount]
+ -[RTAltimeterFloorMapTransitionModel standardDeviationSteps]
+ -[RTAltimeterFloorMapTransitionModel startFloorIndex]
+ -[RTAltimeterFloorMapTransitionModel transitionTimeStandardDeviation]
+ -[RTBluePOIModernCategory .cxx_destruct]
+ -[RTBluePOIModernCategory copyWithZone:]
+ -[RTBluePOIModernCategory description]
+ -[RTBluePOIModernCategory encodeWithCoder:]
+ -[RTBluePOIModernCategory hash]
+ -[RTBluePOIModernCategory idString]
+ -[RTBluePOIModernCategory initWithCoder:]
+ -[RTBluePOIModernCategory initWithIdString:muid:]
+ -[RTBluePOIModernCategory init]
+ -[RTBluePOIModernCategory isEqual:]
+ -[RTBluePOIModernCategory muid]
+ -[RTBluePOITile distancePriors]
+ -[RTBluePOITile initWithIdentifier:apToModelMapping:date:distancePriors:downloadKey:geoCacheInfo:geoTileKey:hashedApToModelMapping:hashedApToModelMappingDataURL:hashSalt:modelCalibrationParameters:models:modelURLs:pointsOfInterest:singlePOIMuid:size:]
+ -[RTDataIntegrityValidationResult .cxx_destruct]
+ -[RTDataIntegrityValidationResult copyWithZone:]
+ -[RTDataIntegrityValidationResult description]
+ -[RTDataIntegrityValidationResult encodeWithCoder:]
+ -[RTDataIntegrityValidationResult executionDuration]
+ -[RTDataIntegrityValidationResult hash]
+ -[RTDataIntegrityValidationResult initWithCoder:]
+ -[RTDataIntegrityValidationResult initWithOrphanCountsByType:sampleOrphanedVisitIdentifiers:sampleOrphanedLOIIdentifiers:sampleUnexpectedFileExtensions:executionDuration:]
+ -[RTDataIntegrityValidationResult isEqual:]
+ -[RTDataIntegrityValidationResult isEqualToDataIntegrityValidationResult:]
+ -[RTDataIntegrityValidationResult orphanCountsByType]
+ -[RTDataIntegrityValidationResult sampleOrphanedLOIIdentifiers]
+ -[RTDataIntegrityValidationResult sampleOrphanedVisitIdentifiers]
+ -[RTDataIntegrityValidationResult sampleUnexpectedFileExtensions]
+ -[RTDataIntegrityValidationResult totalOrphansDetected]
+ -[RTLearnedRoute associatedPlaceInferences]
+ -[RTLearnedRoute initWithLearnedRouteId:routeStartLocation:routeEndLocation:travelTimeEntireRouteSec:travelDistanceEntireRouteMeter:travelModeRoutes:routeStartLocationWithReferenceFrame:routeEndLocationWithReferenceFrame:routeSummary:associatedPlaceInferences:]
+ -[RTLearnedRoute initWithLearnedRouteId:routeStartLocation:routeEndLocation:travelTimeEntireRouteSec:travelDistanceEntireRouteMeter:travelModeRoutes:routeStartLocationWithReferenceFrame:routeEndLocationWithReferenceFrame:routeSummary:associatedPlaceInferences:schedule:recentTripTimes:]
+ -[RTLearnedRoute recentTripTimes]
+ -[RTLearnedRoute routeSummary]
+ -[RTLearnedRoute schedule]
+ -[RTMapItem alternateCategoryMUIDs]
+ -[RTMapItem categoryDescription]
+ -[RTMapItem initWithIdentifier:name:category:categoryMUID:alternateCategoryMUIDs:address:location:source:mapItemPlaceType:muid:resultProviderID:geoMapItemHandle:geoMapItemIdentifier:creationDate:expirationDate:extendedAttributes:displayLanguage:disputed:businessHours:]
+ -[RTMapItem initWithIdentifier:name:category:categoryMUID:alternateCategoryMUIDs:address:location:source:mapItemPlaceType:muid:resultProviderID:geoMapItemHandle:geoMapItemIdentifier:creationDate:expirationDate:extendedAttributes:displayLanguage:disputed:businessHours:categoryDescription:]
+ -[RTMapItem mapItemWithCategoryDescription:]
+ -[RTPlaceInferenceOptions includeCandidates]
+ -[RTPlaceInferenceOptions initWithFidelityPolicy:includeCandidates:clientIdentifier:]
+ -[RTPlaceInferenceOptions initWithFidelityPolicy:locations:accessPoints:distance:location:startDate:endDate:limit:useBackground:includeCandidates:clientIdentifier:]
+ -[RTPointOfInterest alternateCategoryMuids]
+ -[RTPointOfInterest categoryMuid]
+ -[RTPointOfInterest initWithIdentifier:alternateCategoryMuids:applePaySupport:categoryMuid:filtered:fullyCoversTile:location:muid:polygon:popularityTier:]
+ -[RTPointOfInterest popularityTier]
+ -[RTPointOfInterestAttributes initWithApplePaySupport:category:location:muid:name:nearbyPoiCount:popularityTier:]
+ -[RTPointOfInterestAttributes location]
+ -[RTPointOfInterestAttributes name]
+ -[RTPointOfInterestAttributes popularityTier]
+ -[RTRawAltimeterData .cxx_destruct]
+ -[RTRawAltimeterData altimeterData]
+ -[RTRawAltimeterData altimeterValueUncertainty]
+ -[RTRawAltimeterData copyWithZone:]
+ -[RTRawAltimeterData description]
+ -[RTRawAltimeterData encodeWithCoder:]
+ -[RTRawAltimeterData endTime]
+ -[RTRawAltimeterData initWithCoder:]
+ -[RTRawAltimeterData initWithRawAltimeter:startTime:endTime:altimeterData:altimeterValueUncertainty:]
+ -[RTRawAltimeterData initWithRawAltimeter:startTime:endTime:altimeterData:altimeterValueUncertainty:stepCount:]
+ -[RTRawAltimeterData startTime]
+ -[RTRawAltimeterData stepCount]
+ -[RTRawAltimeterData uuid]
+ -[RTRawAltimeterDataEnumerationContext .cxx_destruct]
+ -[RTRawAltimeterDataEnumerationContext copyWithZone:]
+ -[RTRawAltimeterDataEnumerationContext description]
+ -[RTRawAltimeterDataEnumerationContext encodeWithCoder:]
+ -[RTRawAltimeterDataEnumerationContext initWithCoder:]
+ -[RTRawAltimeterDataEnumerationContext initWithEnumerationOptions:]
+ -[RTRawAltimeterDataEnumerationContext initWithEnumerationOptions:offset:]
+ -[RTRawAltimeterDataEnumerationContext init]
+ -[RTRawAltimeterDataEnumerationContext offset]
+ -[RTRawAltimeterDataEnumerationContext options]
+ -[RTRawAltimeterDataEnumerationOptions .cxx_destruct]
+ -[RTRawAltimeterDataEnumerationOptions copyWithZone:]
+ -[RTRawAltimeterDataEnumerationOptions description]
+ -[RTRawAltimeterDataEnumerationOptions encodeWithCoder:]
+ -[RTRawAltimeterDataEnumerationOptions endDate]
+ -[RTRawAltimeterDataEnumerationOptions initWithCoder:]
+ -[RTRawAltimeterDataEnumerationOptions initWithStartDate:endDate:maximumNumberOfItems:]
+ -[RTRawAltimeterDataEnumerationOptions init]
+ -[RTRawAltimeterDataEnumerationOptions maximumNumberOfItems]
+ -[RTRawAltimeterDataEnumerationOptions setEndDate:]
+ -[RTRawAltimeterDataEnumerationOptions setMaximumNumberOfItems:]
+ -[RTRawAltimeterDataEnumerationOptions setStartDate:]
+ -[RTRawAltimeterDataEnumerationOptions startDate]
+ -[RTRoutineManager _launchTaskWithSelector:remainingAttempts:proxyErrorHandler:transaction:taskBlock:]
+ -[RTRoutineManager(AltimeterFloorMap) fetchAltimeterFloorMapDataWithOptions:handler:]
+ -[RTRoutineManager(AltimeterFloorMap) removeAltimeterFloorMapData:startDate:endDate:handler:]
+ -[RTRoutineManager(AltimeterFloorMap) storeAltimeterFloorMapData:handler:]
+ -[RTRoutineManager(RawAltimeter) fetchRawAltimeterDataWithOptions:handler:]
+ -[RTRoutineManager(RawAltimeter) removeRawAltimeterData:startDate:endDate:handler:]
+ -[RTRoutineManager(RawAltimeter) storeRawAltimeterData:handler:]
+ -[RTTripClusterEnumerationOptions .cxx_destruct]
+ -[RTTripClusterEnumerationOptions initWithMinCountOfTraversal:startLatitude:startLongitude:endLatitude:endLongitude:timeWindowStart:timeWindowEnd:]
+ -[RTTripClusterEnumerationOptions initWithTimeWindowStart:timeWindowEnd:]
+ -[RTTripClusterEnumerationOptions setTimeWindowEnd:]
+ -[RTTripClusterEnumerationOptions setTimeWindowStart:]
+ -[RTTripClusterEnumerationOptions timeWindowEnd]
+ -[RTTripClusterEnumerationOptions timeWindowStart]
+ -[RTTripClusterRouteSummaryEnumerationContext .cxx_destruct]
+ -[RTTripClusterRouteSummaryEnumerationContext copyWithZone:]
+ -[RTTripClusterRouteSummaryEnumerationContext description]
+ -[RTTripClusterRouteSummaryEnumerationContext encodeWithCoder:]
+ -[RTTripClusterRouteSummaryEnumerationContext initWithCoder:]
+ -[RTTripClusterRouteSummaryEnumerationContext initWithEnumerationOptions:]
+ -[RTTripClusterRouteSummaryEnumerationContext initWithEnumerationOptions:offset:]
+ -[RTTripClusterRouteSummaryEnumerationContext init]
+ -[RTTripClusterRouteSummaryEnumerationContext isEqual:]
+ -[RTTripClusterRouteSummaryEnumerationContext offset]
+ -[RTTripClusterRouteSummaryEnumerationContext options]
+ -[RTTripClusterRouteSummaryEnumerationOptions .cxx_destruct]
+ -[RTTripClusterRouteSummaryEnumerationOptions batchSize]
+ -[RTTripClusterRouteSummaryEnumerationOptions clusterID]
+ -[RTTripClusterRouteSummaryEnumerationOptions copyWithZone:]
+ -[RTTripClusterRouteSummaryEnumerationOptions description]
+ -[RTTripClusterRouteSummaryEnumerationOptions encodeWithCoder:]
+ -[RTTripClusterRouteSummaryEnumerationOptions initWithClusterID:]
+ -[RTTripClusterRouteSummaryEnumerationOptions initWithCoder:]
+ -[RTTripClusterRouteSummaryEnumerationOptions init]
+ -[RTTripClusterRouteSummaryEnumerationOptions isEqual:]
+ -[RTTripClusterRouteSummaryEnumerationOptions setBatchSize:]
+ -[RTTripClusterRouteSummaryEnumerationOptions setClusterID:]
+ GCC_except_table178
+ GCC_except_table179
+ GCC_except_table184
+ GCC_except_table44
+ GCC_except_table454
+ GCC_except_table584
+ _CFBooleanGetTypeID
+ _CFBooleanGetValue
+ _CFGetTypeID
+ _MGCopyAnswer
+ _OBJC_CLASS_$_RTAltimeterFloorMapData
+ _OBJC_CLASS_$_RTAltimeterFloorMapDataEnumerationContext
+ _OBJC_CLASS_$_RTAltimeterFloorMapDataEnumerationOptions
+ _OBJC_CLASS_$_RTAltimeterFloorMapEntry
+ _OBJC_CLASS_$_RTAltimeterFloorMapTransitionModel
+ _OBJC_CLASS_$_RTBluePOIModernCategory
+ _OBJC_CLASS_$_RTBugCaptureConfiguration
+ _OBJC_CLASS_$_RTBugCaptureManager
+ _OBJC_CLASS_$_RTDataIntegrityValidationResult
+ _OBJC_CLASS_$_RTRawAltimeterData
+ _OBJC_CLASS_$_RTRawAltimeterDataEnumerationContext
+ _OBJC_CLASS_$_RTRawAltimeterDataEnumerationOptions
+ _OBJC_CLASS_$_RTTransaction
+ _OBJC_CLASS_$_RTTransactionManager
+ _OBJC_CLASS_$_RTTransactionMetricsManager
+ _OBJC_CLASS_$_RTTripClusterRouteSummaryEnumerationContext
+ _OBJC_CLASS_$_RTTripClusterRouteSummaryEnumerationOptions
+ _OBJC_IVAR_$_RTAltimeterFloorMapData._endTime
+ _OBJC_IVAR_$_RTAltimeterFloorMapData._expirationDate
+ _OBJC_IVAR_$_RTAltimeterFloorMapData._floorMapArray
+ _OBJC_IVAR_$_RTAltimeterFloorMapData._referenceUUID
+ _OBJC_IVAR_$_RTAltimeterFloorMapData._startTime
+ _OBJC_IVAR_$_RTAltimeterFloorMapData._transitionModels
+ _OBJC_IVAR_$_RTAltimeterFloorMapData._type
+ _OBJC_IVAR_$_RTAltimeterFloorMapData._uuid
+ _OBJC_IVAR_$_RTAltimeterFloorMapDataEnumerationContext._offset
+ _OBJC_IVAR_$_RTAltimeterFloorMapDataEnumerationContext._options
+ _OBJC_IVAR_$_RTAltimeterFloorMapEntry._duration
+ _OBJC_IVAR_$_RTAltimeterFloorMapEntry._elevation
+ _OBJC_IVAR_$_RTAltimeterFloorMapEntry._elevationUncertainty
+ _OBJC_IVAR_$_RTAltimeterFloorMapEntry._floorIndex
+ _OBJC_IVAR_$_RTAltimeterFloorMapEntry._initialFloorProbability
+ _OBJC_IVAR_$_RTAltimeterFloorMapTransitionModel._averageSteps
+ _OBJC_IVAR_$_RTAltimeterFloorMapTransitionModel._elevationChangeStandardDeviation
+ _OBJC_IVAR_$_RTAltimeterFloorMapTransitionModel._endFloorIndex
+ _OBJC_IVAR_$_RTAltimeterFloorMapTransitionModel._meanElevationChange
+ _OBJC_IVAR_$_RTAltimeterFloorMapTransitionModel._meanTransitionTime
+ _OBJC_IVAR_$_RTAltimeterFloorMapTransitionModel._occurrenceCount
+ _OBJC_IVAR_$_RTAltimeterFloorMapTransitionModel._standardDeviationSteps
+ _OBJC_IVAR_$_RTAltimeterFloorMapTransitionModel._startFloorIndex
+ _OBJC_IVAR_$_RTAltimeterFloorMapTransitionModel._transitionTimeStandardDeviation
+ _OBJC_IVAR_$_RTBluePOIModernCategory._idString
+ _OBJC_IVAR_$_RTBluePOIModernCategory._muid
+ _OBJC_IVAR_$_RTBluePOITile._distancePriors
+ _OBJC_IVAR_$_RTDataIntegrityValidationResult._executionDuration
+ _OBJC_IVAR_$_RTDataIntegrityValidationResult._orphanCountsByType
+ _OBJC_IVAR_$_RTDataIntegrityValidationResult._sampleOrphanedLOIIdentifiers
+ _OBJC_IVAR_$_RTDataIntegrityValidationResult._sampleOrphanedVisitIdentifiers
+ _OBJC_IVAR_$_RTDataIntegrityValidationResult._sampleUnexpectedFileExtensions
+ _OBJC_IVAR_$_RTDataIntegrityValidationResult._totalOrphansDetected
+ _OBJC_IVAR_$_RTLearnedRoute._associatedPlaceInferences
+ _OBJC_IVAR_$_RTLearnedRoute._recentTripTimes
+ _OBJC_IVAR_$_RTLearnedRoute._routeSummary
+ _OBJC_IVAR_$_RTLearnedRoute._schedule
+ _OBJC_IVAR_$_RTMapItem._alternateCategoryMUIDs
+ _OBJC_IVAR_$_RTMapItem._categoryDescription
+ _OBJC_IVAR_$_RTPlaceInferenceOptions._includeCandidates
+ _OBJC_IVAR_$_RTPointOfInterest._alternateCategoryMuids
+ _OBJC_IVAR_$_RTPointOfInterest._categoryMuid
+ _OBJC_IVAR_$_RTPointOfInterest._popularityTier
+ _OBJC_IVAR_$_RTPointOfInterestAttributes._location
+ _OBJC_IVAR_$_RTPointOfInterestAttributes._name
+ _OBJC_IVAR_$_RTPointOfInterestAttributes._popularityTier
+ _OBJC_IVAR_$_RTRawAltimeterData._altimeterData
+ _OBJC_IVAR_$_RTRawAltimeterData._altimeterValueUncertainty
+ _OBJC_IVAR_$_RTRawAltimeterData._endTime
+ _OBJC_IVAR_$_RTRawAltimeterData._startTime
+ _OBJC_IVAR_$_RTRawAltimeterData._stepCount
+ _OBJC_IVAR_$_RTRawAltimeterData._uuid
+ _OBJC_IVAR_$_RTRawAltimeterDataEnumerationContext._offset
+ _OBJC_IVAR_$_RTRawAltimeterDataEnumerationContext._options
+ _OBJC_IVAR_$_RTTripClusterRouteSummaryEnumerationContext._offset
+ _OBJC_IVAR_$_RTTripClusterRouteSummaryEnumerationContext._options
+ _OBJC_METACLASS_$_RTAltimeterFloorMapData
+ _OBJC_METACLASS_$_RTAltimeterFloorMapDataEnumerationContext
+ _OBJC_METACLASS_$_RTAltimeterFloorMapDataEnumerationOptions
+ _OBJC_METACLASS_$_RTAltimeterFloorMapEntry
+ _OBJC_METACLASS_$_RTAltimeterFloorMapTransitionModel
+ _OBJC_METACLASS_$_RTBluePOIModernCategory
+ _OBJC_METACLASS_$_RTDataIntegrityValidationResult
+ _OBJC_METACLASS_$_RTRawAltimeterData
+ _OBJC_METACLASS_$_RTRawAltimeterDataEnumerationContext
+ _OBJC_METACLASS_$_RTRawAltimeterDataEnumerationOptions
+ _OBJC_METACLASS_$_RTTripClusterRouteSummaryEnumerationContext
+ _OBJC_METACLASS_$_RTTripClusterRouteSummaryEnumerationOptions
+ __OBJC_$_CLASS_METHODS_RTAltimeterFloorMapData
+ __OBJC_$_CLASS_METHODS_RTAltimeterFloorMapDataEnumerationContext
+ __OBJC_$_CLASS_METHODS_RTAltimeterFloorMapDataEnumerationOptions
+ __OBJC_$_CLASS_METHODS_RTAltimeterFloorMapEntry
+ __OBJC_$_CLASS_METHODS_RTAltimeterFloorMapTransitionModel
+ __OBJC_$_CLASS_METHODS_RTBluePOIModernCategory
+ __OBJC_$_CLASS_METHODS_RTDataIntegrityValidationResult
+ __OBJC_$_CLASS_METHODS_RTRawAltimeterData
+ __OBJC_$_CLASS_METHODS_RTRawAltimeterDataEnumerationContext
+ __OBJC_$_CLASS_METHODS_RTRawAltimeterDataEnumerationOptions
+ __OBJC_$_CLASS_METHODS_RTTripClusterRouteSummaryEnumerationContext
+ __OBJC_$_CLASS_METHODS_RTTripClusterRouteSummaryEnumerationOptions
+ __OBJC_$_CLASS_PROP_LIST_RTAltimeterFloorMapData
+ __OBJC_$_CLASS_PROP_LIST_RTAltimeterFloorMapDataEnumerationContext
+ __OBJC_$_CLASS_PROP_LIST_RTAltimeterFloorMapEntry
+ __OBJC_$_CLASS_PROP_LIST_RTAltimeterFloorMapTransitionModel
+ __OBJC_$_CLASS_PROP_LIST_RTBluePOIModernCategory
+ __OBJC_$_CLASS_PROP_LIST_RTDataIntegrityValidationResult
+ __OBJC_$_CLASS_PROP_LIST_RTRawAltimeterData
+ __OBJC_$_CLASS_PROP_LIST_RTRawAltimeterDataEnumerationContext
+ __OBJC_$_CLASS_PROP_LIST_RTTripClusterRouteSummaryEnumerationContext
+ __OBJC_$_INSTANCE_METHODS_RTAltimeterFloorMapData
+ __OBJC_$_INSTANCE_METHODS_RTAltimeterFloorMapDataEnumerationContext
+ __OBJC_$_INSTANCE_METHODS_RTAltimeterFloorMapDataEnumerationOptions
+ __OBJC_$_INSTANCE_METHODS_RTAltimeterFloorMapEntry
+ __OBJC_$_INSTANCE_METHODS_RTAltimeterFloorMapTransitionModel
+ __OBJC_$_INSTANCE_METHODS_RTBluePOIModernCategory
+ __OBJC_$_INSTANCE_METHODS_RTDataIntegrityValidationResult
+ __OBJC_$_INSTANCE_METHODS_RTRawAltimeterData
+ __OBJC_$_INSTANCE_METHODS_RTRawAltimeterDataEnumerationContext
+ __OBJC_$_INSTANCE_METHODS_RTRawAltimeterDataEnumerationOptions
+ __OBJC_$_INSTANCE_METHODS_RTRoutineManager(AltimeterFloorMap|RawAltimeter|Skyline)
+ __OBJC_$_INSTANCE_METHODS_RTTripClusterRouteSummaryEnumerationContext
+ __OBJC_$_INSTANCE_METHODS_RTTripClusterRouteSummaryEnumerationOptions
+ __OBJC_$_INSTANCE_VARIABLES_RTAltimeterFloorMapData
+ __OBJC_$_INSTANCE_VARIABLES_RTAltimeterFloorMapDataEnumerationContext
+ __OBJC_$_INSTANCE_VARIABLES_RTAltimeterFloorMapDataEnumerationOptions
+ __OBJC_$_INSTANCE_VARIABLES_RTAltimeterFloorMapEntry
+ __OBJC_$_INSTANCE_VARIABLES_RTAltimeterFloorMapTransitionModel
+ __OBJC_$_INSTANCE_VARIABLES_RTBluePOIModernCategory
+ __OBJC_$_INSTANCE_VARIABLES_RTDataIntegrityValidationResult
+ __OBJC_$_INSTANCE_VARIABLES_RTRawAltimeterData
+ __OBJC_$_INSTANCE_VARIABLES_RTRawAltimeterDataEnumerationContext
+ __OBJC_$_INSTANCE_VARIABLES_RTRawAltimeterDataEnumerationOptions
+ __OBJC_$_INSTANCE_VARIABLES_RTTripClusterRouteSummaryEnumerationContext
+ __OBJC_$_INSTANCE_VARIABLES_RTTripClusterRouteSummaryEnumerationOptions
+ __OBJC_$_PROP_LIST_RTAltimeterFloorMapData
+ __OBJC_$_PROP_LIST_RTAltimeterFloorMapDataEnumerationContext
+ __OBJC_$_PROP_LIST_RTAltimeterFloorMapDataEnumerationOptions
+ __OBJC_$_PROP_LIST_RTAltimeterFloorMapEntry
+ __OBJC_$_PROP_LIST_RTAltimeterFloorMapTransitionModel
+ __OBJC_$_PROP_LIST_RTBluePOIModernCategory
+ __OBJC_$_PROP_LIST_RTDataIntegrityValidationResult
+ __OBJC_$_PROP_LIST_RTRawAltimeterData
+ __OBJC_$_PROP_LIST_RTRawAltimeterDataEnumerationContext
+ __OBJC_$_PROP_LIST_RTRawAltimeterDataEnumerationOptions
+ __OBJC_$_PROP_LIST_RTTripClusterRouteSummaryEnumerationContext
+ __OBJC_$_PROP_LIST_RTTripClusterRouteSummaryEnumerationOptions
+ __OBJC_CLASS_PROTOCOLS_$_RTAltimeterFloorMapData
+ __OBJC_CLASS_PROTOCOLS_$_RTAltimeterFloorMapDataEnumerationContext
+ __OBJC_CLASS_PROTOCOLS_$_RTAltimeterFloorMapEntry
+ __OBJC_CLASS_PROTOCOLS_$_RTAltimeterFloorMapTransitionModel
+ __OBJC_CLASS_PROTOCOLS_$_RTBluePOIModernCategory
+ __OBJC_CLASS_PROTOCOLS_$_RTDataIntegrityValidationResult
+ __OBJC_CLASS_PROTOCOLS_$_RTRawAltimeterData
+ __OBJC_CLASS_PROTOCOLS_$_RTRawAltimeterDataEnumerationContext
+ __OBJC_CLASS_PROTOCOLS_$_RTTripClusterRouteSummaryEnumerationContext
+ __OBJC_CLASS_PROTOCOLS_$_RTTripClusterRouteSummaryEnumerationOptions
+ __OBJC_CLASS_RO_$_RTAltimeterFloorMapData
+ __OBJC_CLASS_RO_$_RTAltimeterFloorMapDataEnumerationContext
+ __OBJC_CLASS_RO_$_RTAltimeterFloorMapDataEnumerationOptions
+ __OBJC_CLASS_RO_$_RTAltimeterFloorMapEntry
+ __OBJC_CLASS_RO_$_RTAltimeterFloorMapTransitionModel
+ __OBJC_CLASS_RO_$_RTBluePOIModernCategory
+ __OBJC_CLASS_RO_$_RTDataIntegrityValidationResult
+ __OBJC_CLASS_RO_$_RTRawAltimeterData
+ __OBJC_CLASS_RO_$_RTRawAltimeterDataEnumerationContext
+ __OBJC_CLASS_RO_$_RTRawAltimeterDataEnumerationOptions
+ __OBJC_CLASS_RO_$_RTTripClusterRouteSummaryEnumerationContext
+ __OBJC_CLASS_RO_$_RTTripClusterRouteSummaryEnumerationOptions
+ __OBJC_METACLASS_RO_$_RTAltimeterFloorMapData
+ __OBJC_METACLASS_RO_$_RTAltimeterFloorMapDataEnumerationContext
+ __OBJC_METACLASS_RO_$_RTAltimeterFloorMapDataEnumerationOptions
+ __OBJC_METACLASS_RO_$_RTAltimeterFloorMapEntry
+ __OBJC_METACLASS_RO_$_RTAltimeterFloorMapTransitionModel
+ __OBJC_METACLASS_RO_$_RTBluePOIModernCategory
+ __OBJC_METACLASS_RO_$_RTDataIntegrityValidationResult
+ __OBJC_METACLASS_RO_$_RTRawAltimeterData
+ __OBJC_METACLASS_RO_$_RTRawAltimeterDataEnumerationContext
+ __OBJC_METACLASS_RO_$_RTRawAltimeterDataEnumerationOptions
+ __OBJC_METACLASS_RO_$_RTTripClusterRouteSummaryEnumerationContext
+ __OBJC_METACLASS_RO_$_RTTripClusterRouteSummaryEnumerationOptions
+ ___102-[RTRoutineManager _launchTaskWithSelector:remainingAttempts:proxyErrorHandler:transaction:taskBlock:]_block_invoke
+ ___37-[RTRoutineManager _createConnection]_block_invoke.441
+ ___38-[RTRoutineManager stopLeechingVisits]_block_invoke.504
+ ___38-[RTRoutineManager stopLeechingVisits]_block_invoke_2.505
+ ___40-[RTRoutineManager stopMonitoringVisits]_block_invoke.502
+ ___40-[RTRoutineManager stopMonitoringVisits]_block_invoke_2.503
+ ___42-[RTRoutineManager addElevations:handler:]_block_invoke.597
+ ___49-[RTRoutineManager fetchRoutineStateWithHandler:]_block_invoke.476
+ ___49-[RTRoutineManager stopMonitoringPlaceInferences]_block_invoke.510
+ ___49-[RTRoutineManager stopMonitoringPlaceInferences]_block_invoke_2.511
+ ___50-[RTRoutineManager fetchAuthorizedLocationStatus:]_block_invoke.552
+ ___51-[RTRoutineManager fetchRoutineEnabledWithHandler:]_block_invoke.474
+ ___51-[RTRoutineManager stopLeechingLowConfidenceVisits]_block_invoke.506
+ ___51-[RTRoutineManager stopLeechingLowConfidenceVisits]_block_invoke_2.507
+ ___53-[RTRoutineManager clearAllVehicleEventsWithHandler:]_block_invoke.554
+ ___53-[RTRoutineManager clearAllVehicleEventsWithHandler:]_block_invoke.555
+ ___53-[RTRoutineManager fetchElevationsWithOptions:reply:]_block_invoke.598
+ ___56-[RTRoutineManager stopMonitoringScenarioTriggerOfType:]_block_invoke.526
+ ___56-[RTRoutineManager stopMonitoringScenarioTriggerOfType:]_block_invoke_2.527
+ ___57-[RTRoutineManager fetchStoredVisitsWithOptions:handler:]_block_invoke.512
+ ___58-[RTRoutineManager _enumerateElevationsWithOptions:reply:]_block_invoke.599
+ ___58-[RTRoutineManager _enumerateElevationsWithOptions:reply:]_block_invoke.602
+ ___58-[RTRoutineManager stopMonitoringForGeneratedTripSegments]_block_invoke.471
+ ___58-[RTRoutineManager stopMonitoringForGeneratedTripSegments]_block_invoke_2.472
+ ___58-[RTRoutineManager stopMonitoringRemoteStatusWithHandler:]_block_invoke.482
+ ___58-[RTRoutineManager stopMonitoringRemoteStatusWithHandler:]_block_invoke_2.483
+ ___59-[RTRoutineManager enumerateObjectsWithOptions:usingBlock:]_block_invoke.494
+ ___59-[RTRoutineManager startMonitoringRemoteStatusWithHandler:]_block_invoke.479
+ ___59-[RTRoutineManager startMonitoringRemoteStatusWithHandler:]_block_invoke_2.480
+ ___62-[RTRoutineManager startMonitoringForPeopleDiscovery:handler:]_block_invoke.588
+ ___62-[RTRoutineManager stopMonitoringPredictedContextWithHandler:]_block_invoke.521
+ ___62-[RTRoutineManager stopMonitoringPredictedContextWithHandler:]_block_invoke_2.522
+ ___63-[RTRoutineManager fetchLocationsOfInterestOfType:withHandler:]_block_invoke.530
+ ___63-[RTRoutineManager submitUserCurationForDate:newLabel:handler:]_block_invoke.605
+ ___64-[RTRoutineManager stopMonitoringForPeopleDiscoveryWithHandler:]_block_invoke.589
+ ___64-[RTRoutineManager stopMonitoringForPeopleDiscoveryWithHandler:]_block_invoke.590
+ ___64-[RTRoutineManager(RawAltimeter) storeRawAltimeterData:handler:]_block_invoke
+ ___64-[RTRoutineManager(RawAltimeter) storeRawAltimeterData:handler:]_block_invoke_2
+ ___64-[RTRoutineManager(RawAltimeter) storeRawAltimeterData:handler:]_block_invoke_3
+ ___65-[RTRoutineManager addBackgroundInertialOdometrySamples:handler:]_block_invoke.604
+ ___68-[RTRoutineManager _enumerateStoredLocationsWithOptions:usingBlock:]_block_invoke.499
+ ___68-[RTRoutineManager _enumerateStoredLocationsWithOptions:usingBlock:]_block_invoke.500
+ ___68-[RTRoutineManager fetchPeopleCountEventsHistory:completionHandler:]_block_invoke.594
+ ___70-[RTRoutineManager fetchLocationOfInterestWithIdentifier:withHandler:]_block_invoke.528
+ ___70-[RTRoutineManager startMonitoringPlaceInferencesWithOptions:handler:]_block_invoke.508
+ ___70-[RTRoutineManager startMonitoringPlaceInferencesWithOptions:handler:]_block_invoke_2.509
+ ___71-[RTRoutineManager fetchContactScoresFromContactIDs:completionHandler:]_block_invoke.596
+ ___72-[RTRoutineManager fetchProximityHistoryFromEventIDs:completionHandler:]_block_invoke.593
+ ___73-[RTRoutineManager fetchLocationsOfInterestVisitedSinceDate:withHandler:]_block_invoke.534
+ ___73-[RTRoutineManager submitUserCurationForVisitDateRange:newLabel:handler:]_block_invoke.606
+ ___74-[RTRoutineManager(AltimeterFloorMap) storeAltimeterFloorMapData:handler:]_block_invoke
+ ___74-[RTRoutineManager(AltimeterFloorMap) storeAltimeterFloorMapData:handler:]_block_invoke_2
+ ___74-[RTRoutineManager(AltimeterFloorMap) storeAltimeterFloorMapData:handler:]_block_invoke_3
+ ___75-[RTRoutineManager(RawAltimeter) fetchRawAltimeterDataWithOptions:handler:]_block_invoke
+ ___75-[RTRoutineManager(RawAltimeter) fetchRawAltimeterDataWithOptions:handler:]_block_invoke_2
+ ___75-[RTRoutineManager(RawAltimeter) fetchRawAltimeterDataWithOptions:handler:]_block_invoke_3
+ ___77-[RTRoutineManager _proxyForServicingSelector:asynchronous:withErrorHandler:]_block_invoke.447
+ ___77-[RTRoutineManager _proxyForServicingSelector:asynchronous:withErrorHandler:]_block_invoke.448
+ ___78-[RTRoutineManager fetchBackgroundInertialOdometrySamplesWithOptions:handler:]_block_invoke.603
+ ___81-[RTRoutineManager fetchProximityHistoryFromStartDate:endDate:completionHandler:]_block_invoke.592
+ ___81-[RTRoutineManager startMonitoringPredictedContextWithOptions:completionHandler:]_block_invoke.519
+ ___81-[RTRoutineManager startMonitoringPredictedContextWithOptions:completionHandler:]_block_invoke_2.520
+ ___83-[RTRoutineManager(RawAltimeter) removeRawAltimeterData:startDate:endDate:handler:]_block_invoke
+ ___83-[RTRoutineManager(RawAltimeter) removeRawAltimeterData:startDate:endDate:handler:]_block_invoke_2
+ ___83-[RTRoutineManager(RawAltimeter) removeRawAltimeterData:startDate:endDate:handler:]_block_invoke_3
+ ___85-[RTRoutineManager fetchPeopleDensityHistoryFromStartDate:endDate:completionHandler:]_block_invoke.595
+ ___85-[RTRoutineManager(AltimeterFloorMap) fetchAltimeterFloorMapDataWithOptions:handler:]_block_invoke
+ ___85-[RTRoutineManager(AltimeterFloorMap) fetchAltimeterFloorMapDataWithOptions:handler:]_block_invoke_2
+ ___85-[RTRoutineManager(AltimeterFloorMap) fetchAltimeterFloorMapDataWithOptions:handler:]_block_invoke_3
+ ___88-[RTRoutineManager fetchLocationsOfInterestVisitedBetweenStartDate:endDate:withHandler:]_block_invoke.538
+ ___93-[RTRoutineManager(AltimeterFloorMap) removeAltimeterFloorMapData:startDate:endDate:handler:]_block_invoke
+ ___93-[RTRoutineManager(AltimeterFloorMap) removeAltimeterFloorMapData:startDate:endDate:handler:]_block_invoke_2
+ ___93-[RTRoutineManager(AltimeterFloorMap) removeAltimeterFloorMapData:startDate:endDate:handler:]_block_invoke_3
+ ___96-[RTRoutineManager correctLabelForVisitWithIdentifier:entryDate:originalLabel:newLabel:handler:]_block_invoke.607
+ ___Block_byref_object_copy_.600
+ ___Block_byref_object_dispose_.601
+ ___NSDictionary0__struct
+ ___block_descriptor_32_e26_v24?08"RTTransaction"16l
+ ___block_descriptor_40_e8_32bs_e32_v28?0"NSArray"8B16"NSError"20ls32l8
+ ___block_descriptor_40_e8_32bs_e39_v28?0"NSMutableArray"8B16"NSError"20ls32l8
+ ___block_descriptor_40_e8_32s_e26_v24?08"RTTransaction"16ls32l8
+ ___block_descriptor_48_e8_32s40bs_e26_v24?08"RTTransaction"16ls32l8s40l8
+ ___block_descriptor_48_e8_32s40bs_e46_v24?0"<RTDaemonProtocol>"8"RTTransaction"16ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e17_v16?0"NSError"8ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e26_v24?08"RTTransaction"16ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e5_v8?0ls32l8s40l8
+ ___block_descriptor_48_e8_32s_e26_v24?08"RTTransaction"16ls32l8
+ ___block_descriptor_49_e8_32s40bs_e26_v24?08"RTTransaction"16ls32l8s40l8
+ ___block_descriptor_49_e8_32s40bs_e5_v8?0ls32l8s40l8
+ ___block_descriptor_56_e8_32s40bs48r_e29_v24?0"NSArray"8"NSError"16ls32l8r48l8s40l8
+ ___block_descriptor_56_e8_32s40bs_e26_v24?08"RTTransaction"16ls32l8s40l8
+ ___block_descriptor_56_e8_32s40s48bs_e17_v16?0"NSError"8ls32l8s40l8s48l8
+ ___block_descriptor_56_e8_32s40s48bs_e20_v20?0B8"NSError"12ls32l8s40l8s48l8
+ ___block_descriptor_56_e8_32s40s48bs_e20_v24?0Q8"NSError"16ls32l8s40l8s48l8
+ ___block_descriptor_56_e8_32s40s48bs_e20_v24?0q8"NSError"16ls32l8s40l8s48l8
+ ___block_descriptor_56_e8_32s40s48bs_e26_v24?08"RTTransaction"16ls32l8s40l8s48l8
+ ___block_descriptor_56_e8_32s40s48bs_e28_v24?0"NSDate"8"NSError"16ls32l8s40l8s48l8
+ ___block_descriptor_56_e8_32s40s48bs_e29_v24?0"NSArray"8"NSError"16ls32l8s40l8s48l8
+ ___block_descriptor_56_e8_32s40s48bs_e30_v24?0"NSString"8"NSError"16ls32l8s40l8s48l8
+ ___block_descriptor_56_e8_32s40s48bs_e32_v24?0"CLLocation"8"NSError"16ls32l8s40l8s48l8
+ ___block_descriptor_56_e8_32s40s48bs_e33_v32?0"NSArray"8^B16"NSError"24ls32l8s40l8s48l8
+ ___block_descriptor_56_e8_32s40s48bs_e34_v24?0"NSDictionary"8"NSError"16ls32l8s40l8s48l8
+ ___block_descriptor_56_e8_32s40s48bs_e37_v24?0"RTPeopleDensity"8"NSError"16ls32l8s40l8s48l8
+ ___block_descriptor_56_e8_32s40s48bs_e42_v24?0"RTLocationOfInterest"8"NSError"16ls32l8s40l8s48l8
+ ___block_descriptor_56_e8_32s40s48bs_e43_v24?0"RTTripSegmentMetadata"8"NSError"16ls32l8s40l8s48l8
+ ___block_descriptor_56_e8_32s40s48bs_e46_v24?0"<RTDaemonProtocol>"8"RTTransaction"16ls32l8s40l8s48l8
+ ___block_descriptor_56_e8_32s40s48bs_e46_v24?0"RTPredictedContextResult"8"NSError"16ls32l8s40l8s48l8
+ ___block_descriptor_56_e8_32s40s48bs_e5_v8?0ls48l8s32l8s40l8
+ ___block_descriptor_56_e8_32s40s48bs_e8_v12?0B8ls32l8s40l8s48l8
+ ___block_descriptor_57_e8_32s40bs_e5_v8?0ls32l8s40l8
+ ___block_descriptor_57_e8_32s40s48bs_e5_v8?0ls32l8s48l8s40l8
+ ___block_descriptor_64_e8_32s40bs_e26_v24?08"RTTransaction"16ls32l8s40l8
+ ___block_descriptor_64_e8_32s40s48bs56r_e5_v8?0lr56l8s48l8s32l8s40l8
+ ___block_descriptor_64_e8_32s40s48bs_e17_v16?0"NSError"8ls32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48bs_e26_v24?08"RTTransaction"16ls32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48bs_e29_v24?0"NSArray"8"NSError"16ls32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48bs_e42_v24?0"RTLocationOfInterest"8"NSError"16ls32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48bs_e46_v24?0"<RTDaemonProtocol>"8"RTTransaction"16ls32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48bs_e48_v24?0"RTAuthorizedLocationStatus"8"NSError"16ls32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48bs_e5_v8?0ls32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48bs_e8_v12?0B8ls32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48s56bs_e26_v24?08"RTTransaction"16ls32l8s40l8s48l8s56l8
+ ___block_descriptor_64_e8_32s40s48s56bs_e5_v8?0ls32l8s40l8s56l8s48l8
+ ___block_descriptor_72_e8_32s40s48s56bs_e26_v24?08"RTTransaction"16ls32l8s40l8s48l8s56l8
+ ___block_descriptor_72_e8_32s40s48s56bs_e5_v8?0ls32l8s40l8s56l8s48l8
+ ___block_descriptor_72_e8_32s40s48s56s64bs_e26_v24?08"RTTransaction"16ls32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_80_e8_32s40s48s56s64bs_e26_v24?08"RTTransaction"16ls32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_80_e8_32s40s48s56s64bs_e5_v8?0ls32l8s64l8s40l8s48l8s56l8
+ ___block_descriptor_88_e8_32s40bs48r56r64r72r80r_e29_v24?0"NSArray"8"NSError"16lr48l8r56l8s40l8r64l8r72l8r80l8s32l8
+ ___block_descriptor_88_e8_32s40s48bs56bs64r_e17_v16?0"NSError"8ls32l8s48l8r64l8s56l8s40l8
+ ___block_descriptor_88_e8_32s40s48s56s64s72bs_e26_v24?08"RTTransaction"16ls32l8s40l8s48l8s56l8s64l8s72l8
+ ___block_literal_global.10
+ ___block_literal_global.12
+ ___block_literal_global.20
+ ___block_literal_global.470
+ ___block_literal_global.525
+ ___block_literal_global.563
+ ___block_literal_global.565
+ ___block_literal_global.567
+ ___block_literal_global.569
+ ___block_literal_global.571
+ ___block_literal_global.573
+ ___block_literal_global.575
+ ___block_literal_global.577
+ ___block_literal_global.579
+ ___block_literal_global.581
+ ___block_literal_global.583
+ ___block_literal_global.585
+ ___block_literal_global.587
+ __os_feature_enabled_impl
+ _kRTBluePOITileModelCalibrationHighThresholdAfterCalibrationCombinedApplePay
+ _kRTBluePOITileModelCalibrationHighThresholdAfterCalibrationCombinedNonApplePay
+ _kRTBluePOITileModelCalibrationHighThresholdAfterCalibrationUncovered
+ _kRTBluePOITileModelCalibrationHighThresholdBeforeCalibrationCombinedApplePay
+ _kRTBluePOITileModelCalibrationHighThresholdBeforeCalibrationCombinedNonApplePay
+ _kRTBluePOITileModelCalibrationHighThresholdBeforeCalibrationUncovered
+ _kRTBluePOITileModelCalibrationHighestScoreCombinedApplePay
+ _kRTBluePOITileModelCalibrationHighestScoreCombinedNonApplePay
+ _kRTBluePOITileModelCalibrationHighestScoreUncovered
+ _kRTBluePOITileModelCalibrationLowThresholdAfterCalibrationCombinedApplePay
+ _kRTBluePOITileModelCalibrationLowThresholdAfterCalibrationCombinedNonApplePay
+ _kRTBluePOITileModelCalibrationLowThresholdAfterCalibrationUncovered
+ _kRTBluePOITileModelCalibrationLowThresholdBeforeCalibrationCombinedApplePay
+ _kRTBluePOITileModelCalibrationLowThresholdBeforeCalibrationCombinedNonApplePay
+ _kRTBluePOITileModelCalibrationLowThresholdBeforeCalibrationUncovered
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$_launchTaskWithSelector:remainingAttempts:proxyErrorHandler:transaction:taskBlock:
+ _objc_msgSend$alternateCategoryMuids
+ _objc_msgSend$associatedPlaceInferences
+ _objc_msgSend$averageSteps
+ _objc_msgSend$category
+ _objc_msgSend$categoryDescription
+ _objc_msgSend$categoryMuid
+ _objc_msgSend$characterAtIndex:
+ _objc_msgSend$characterIsMember:
+ _objc_msgSend$configurationWithProfile:internalInstall:
+ _objc_msgSend$copyWithZone:
+ _objc_msgSend$descriptionForPopularityTier:
+ _objc_msgSend$distancePriors
+ _objc_msgSend$duration
+ _objc_msgSend$elevationChangeStandardDeviation
+ _objc_msgSend$end
+ _objc_msgSend$endFloorIndex
+ _objc_msgSend$executionDuration
+ _objc_msgSend$expirationDateBefore
+ _objc_msgSend$fetchAltimeterFloorMapDataWithOptions:reply:
+ _objc_msgSend$fetchRawAltimeterDataWithOptions:reply:
+ _objc_msgSend$floorIndex
+ _objc_msgSend$floorMapArray
+ _objc_msgSend$hasPrefix:
+ _objc_msgSend$idString
+ _objc_msgSend$initWithAltimeterFloorMapData:startTime:endTime:type:referenceUUID:floorMapArray:transitionModels:expirationDate:
+ _objc_msgSend$initWithApplePaySupport:category:location:muid:name:nearbyPoiCount:popularityTier:
+ _objc_msgSend$initWithConfiguration:
+ _objc_msgSend$initWithFidelityPolicy:locations:accessPoints:distance:location:startDate:endDate:limit:useBackground:includeCandidates:clientIdentifier:
+ _objc_msgSend$initWithFloorMapEntry:elevation:elevationUncertainty:initialFloorProbability:duration:
+ _objc_msgSend$initWithIdString:muid:
+ _objc_msgSend$initWithIdentifier:alternateCategoryMuids:applePaySupport:categoryMuid:filtered:fullyCoversTile:location:muid:polygon:popularityTier:
+ _objc_msgSend$initWithIdentifier:apToModelMapping:date:distancePriors:downloadKey:geoCacheInfo:geoTileKey:hashedApToModelMapping:hashedApToModelMappingDataURL:hashSalt:modelCalibrationParameters:models:modelURLs:pointsOfInterest:singlePOIMuid:size:
+ _objc_msgSend$initWithIdentifier:name:category:categoryMUID:alternateCategoryMUIDs:address:location:source:mapItemPlaceType:muid:resultProviderID:geoMapItemHandle:geoMapItemIdentifier:creationDate:expirationDate:extendedAttributes:displayLanguage:disputed:businessHours:
+ _objc_msgSend$initWithIdentifier:name:category:categoryMUID:alternateCategoryMUIDs:address:location:source:mapItemPlaceType:muid:resultProviderID:geoMapItemHandle:geoMapItemIdentifier:creationDate:expirationDate:extendedAttributes:displayLanguage:disputed:businessHours:categoryDescription:
+ _objc_msgSend$initWithLearnedRouteId:routeStartLocation:routeEndLocation:travelTimeEntireRouteSec:travelDistanceEntireRouteMeter:travelModeRoutes:routeStartLocationWithReferenceFrame:routeEndLocationWithReferenceFrame:routeSummary:associatedPlaceInferences:schedule:recentTripTimes:
+ _objc_msgSend$initWithMetricsManager:bugCaptureManager:
+ _objc_msgSend$initWithMinCountOfTraversal:startLatitude:startLongitude:endLatitude:endLongitude:timeWindowStart:timeWindowEnd:
+ _objc_msgSend$initWithOrphanCountsByType:sampleOrphanedVisitIdentifiers:sampleOrphanedLOIIdentifiers:sampleUnexpectedFileExtensions:executionDuration:
+ _objc_msgSend$initWithRawAltimeter:startTime:endTime:altimeterData:altimeterValueUncertainty:stepCount:
+ _objc_msgSend$initWithStartDate:endDate:maximumNumberOfItems:
+ _objc_msgSend$initWithStartDate:endDate:maximumNumberOfItems:referenceUUID:
+ _objc_msgSend$initWithTransitionModel:endFloorIndex:meanElevationChange:elevationChangeStandardDeviation:meanTransitionTime:transitionTimeStandardDeviation:averageSteps:standardDeviationSteps:occurrenceCount:
+ _objc_msgSend$initialFloorProbability
+ _objc_msgSend$isEqualToDataIntegrityValidationResult:
+ _objc_msgSend$isInternalInstall
+ _objc_msgSend$lowercaseLetterCharacterSet
+ _objc_msgSend$maximumNumberOfItems
+ _objc_msgSend$meanElevationChange
+ _objc_msgSend$meanTransitionTime
+ _objc_msgSend$nearbyPoiCount
+ _objc_msgSend$occurrenceCount
+ _objc_msgSend$orphanCountsByType
+ _objc_msgSend$popularityTier
+ _objc_msgSend$recentTripTimes
+ _objc_msgSend$referenceUUID
+ _objc_msgSend$removeAltimeterFloorMapData:startDate:endDate:reply:
+ _objc_msgSend$removeRawAltimeterData:startDate:endDate:reply:
+ _objc_msgSend$routeSummary
+ _objc_msgSend$sampleOrphanedLOIIdentifiers
+ _objc_msgSend$sampleOrphanedVisitIdentifiers
+ _objc_msgSend$sampleUnexpectedFileExtensions
+ _objc_msgSend$schedule
+ _objc_msgSend$setBatchSize:
+ _objc_msgSend$setClusterID:
+ _objc_msgSend$setExpirationDateBefore:
+ _objc_msgSend$setSharedInstance:
+ _objc_msgSend$standardDeviationSteps
+ _objc_msgSend$startFloorIndex
+ _objc_msgSend$startWithName:
+ _objc_msgSend$storeAltimeterFloorMapData:reply:
+ _objc_msgSend$storeRawAltimeterData:reply:
+ _objc_msgSend$substringFromIndex:
+ _objc_msgSend$timeWindowEnd
+ _objc_msgSend$timeWindowStart
+ _objc_msgSend$totalOrphansDetected
+ _objc_msgSend$transitionModels
+ _objc_msgSend$transitionTimeStandardDeviation
+ _objc_msgSend$uppercaseLetterCharacterSet
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x4
+ _objc_retain_x5
+ _objc_retain_x6
- -[RTBluePOITile initWithIdentifier:apToModelMapping:date:downloadKey:geoCacheInfo:geoTileKey:hashedApToModelMapping:hashedApToModelMappingDataURL:hashSalt:modelCalibrationParameters:models:modelURLs:pointsOfInterest:singlePOIMuid:size:]
- -[RTHangsMetrics init]
- -[RTHangsMetrics submitToCoreAnalytics:type:duration:]
- -[RTPointOfInterest initWithIdentifier:applePaySupport:filtered:fullyCoversTile:location:muid:polygon:]
- -[RTPointOfInterestAttributes initWithApplePaySupport:category:muid:nearbyPoiCount:]
- -[RTRoutineManager _launchTaskWithSelector:remainingAttempts:proxyErrorHandler:taskBlock:]
- -[RTTripClusterEnumerationOptions initWithMinCountOfTraversal:startLatitude:startLongitude:endLatitude:endLongitude:]
- GCC_except_table175
- GCC_except_table176
- GCC_except_table183
- GCC_except_table583
- _AnalyticsSendEvent
- _OBJC_CLASS_$_RTHangsMetrics
- _OBJC_METACLASS_$_RTHangsMetrics
- _RTAnalyticsEventHangsMetrics
- _RTLogFacilityMetric
- __OBJC_$_INSTANCE_METHODS_RTHangsMetrics
- __OBJC_$_INSTANCE_METHODS_RTRoutineManager(Skyline)
- __OBJC_CLASS_RO_$_RTHangsMetrics
- __OBJC_METACLASS_RO_$_RTHangsMetrics
- ___37-[RTRoutineManager _createConnection]_block_invoke.418
- ___38-[RTRoutineManager stopLeechingVisits]_block_invoke.478
- ___38-[RTRoutineManager stopLeechingVisits]_block_invoke_2.479
- ___40-[RTRoutineManager stopMonitoringVisits]_block_invoke.476
- ___40-[RTRoutineManager stopMonitoringVisits]_block_invoke_2.477
- ___42-[RTRoutineManager addElevations:handler:]_block_invoke.571
- ___49-[RTRoutineManager fetchRoutineStateWithHandler:]_block_invoke.450
- ___49-[RTRoutineManager stopMonitoringPlaceInferences]_block_invoke.484
- ___49-[RTRoutineManager stopMonitoringPlaceInferences]_block_invoke_2.485
- ___50-[RTRoutineManager fetchAuthorizedLocationStatus:]_block_invoke.526
- ___51-[RTRoutineManager fetchRoutineEnabledWithHandler:]_block_invoke.448
- ___51-[RTRoutineManager stopLeechingLowConfidenceVisits]_block_invoke.480
- ___51-[RTRoutineManager stopLeechingLowConfidenceVisits]_block_invoke_2.481
- ___53-[RTRoutineManager clearAllVehicleEventsWithHandler:]_block_invoke.528
- ___53-[RTRoutineManager clearAllVehicleEventsWithHandler:]_block_invoke.529
- ___53-[RTRoutineManager fetchElevationsWithOptions:reply:]_block_invoke.572
- ___56-[RTRoutineManager stopMonitoringScenarioTriggerOfType:]_block_invoke.500
- ___56-[RTRoutineManager stopMonitoringScenarioTriggerOfType:]_block_invoke_2.501
- ___57-[RTRoutineManager fetchStoredVisitsWithOptions:handler:]_block_invoke.486
- ___58-[RTRoutineManager _enumerateElevationsWithOptions:reply:]_block_invoke.573
- ___58-[RTRoutineManager _enumerateElevationsWithOptions:reply:]_block_invoke.576
- ___58-[RTRoutineManager stopMonitoringForGeneratedTripSegments]_block_invoke.445
- ___58-[RTRoutineManager stopMonitoringForGeneratedTripSegments]_block_invoke_2.446
- ___58-[RTRoutineManager stopMonitoringRemoteStatusWithHandler:]_block_invoke.456
- ___58-[RTRoutineManager stopMonitoringRemoteStatusWithHandler:]_block_invoke_2.457
- ___59-[RTRoutineManager enumerateObjectsWithOptions:usingBlock:]_block_invoke.468
- ___59-[RTRoutineManager startMonitoringRemoteStatusWithHandler:]_block_invoke.453
- ___59-[RTRoutineManager startMonitoringRemoteStatusWithHandler:]_block_invoke_2.454
- ___62-[RTRoutineManager startMonitoringForPeopleDiscovery:handler:]_block_invoke.562
- ___62-[RTRoutineManager stopMonitoringPredictedContextWithHandler:]_block_invoke.495
- ___62-[RTRoutineManager stopMonitoringPredictedContextWithHandler:]_block_invoke_2.496
- ___63-[RTRoutineManager fetchLocationsOfInterestOfType:withHandler:]_block_invoke.504
- ___63-[RTRoutineManager submitUserCurationForDate:newLabel:handler:]_block_invoke.579
- ___64-[RTRoutineManager stopMonitoringForPeopleDiscoveryWithHandler:]_block_invoke.563
- ___64-[RTRoutineManager stopMonitoringForPeopleDiscoveryWithHandler:]_block_invoke.564
- ___65-[RTRoutineManager addBackgroundInertialOdometrySamples:handler:]_block_invoke.578
- ___68-[RTRoutineManager _enumerateStoredLocationsWithOptions:usingBlock:]_block_invoke.473
- ___68-[RTRoutineManager _enumerateStoredLocationsWithOptions:usingBlock:]_block_invoke.474
- ___68-[RTRoutineManager fetchPeopleCountEventsHistory:completionHandler:]_block_invoke.568
- ___70-[RTRoutineManager fetchLocationOfInterestWithIdentifier:withHandler:]_block_invoke.502
- ___70-[RTRoutineManager startMonitoringPlaceInferencesWithOptions:handler:]_block_invoke.482
- ___70-[RTRoutineManager startMonitoringPlaceInferencesWithOptions:handler:]_block_invoke_2.483
- ___71-[RTRoutineManager fetchContactScoresFromContactIDs:completionHandler:]_block_invoke.570
- ___72-[RTRoutineManager fetchProximityHistoryFromEventIDs:completionHandler:]_block_invoke.567
- ___73-[RTRoutineManager fetchLocationsOfInterestVisitedSinceDate:withHandler:]_block_invoke.508
- ___73-[RTRoutineManager submitUserCurationForVisitDateRange:newLabel:handler:]_block_invoke.580
- ___77-[RTRoutineManager _proxyForServicingSelector:asynchronous:withErrorHandler:]_block_invoke.420
- ___77-[RTRoutineManager _proxyForServicingSelector:asynchronous:withErrorHandler:]_block_invoke.421
- ___78-[RTRoutineManager fetchBackgroundInertialOdometrySamplesWithOptions:handler:]_block_invoke.577
- ___81-[RTRoutineManager fetchProximityHistoryFromStartDate:endDate:completionHandler:]_block_invoke.566
- ___81-[RTRoutineManager startMonitoringPredictedContextWithOptions:completionHandler:]_block_invoke.493
- ___81-[RTRoutineManager startMonitoringPredictedContextWithOptions:completionHandler:]_block_invoke_2.494
- ___85-[RTRoutineManager fetchPeopleDensityHistoryFromStartDate:endDate:completionHandler:]_block_invoke.569
- ___88-[RTRoutineManager fetchLocationsOfInterestVisitedBetweenStartDate:endDate:withHandler:]_block_invoke.512
- ___90-[RTRoutineManager _launchTaskWithSelector:remainingAttempts:proxyErrorHandler:taskBlock:]_block_invoke
- ___96-[RTRoutineManager correctLabelForVisitWithIdentifier:entryDate:originalLabel:newLabel:handler:]_block_invoke.581
- ___Block_byref_object_copy_.574
- ___Block_byref_object_dispose_.575
- ___block_descriptor_32_e31_q24?0"NSString"8"NSString"16l
- ___block_descriptor_32_e8_v16?08l
- ___block_descriptor_40_e8_32bs_e5_v8?0ls32l8
- ___block_descriptor_40_e8_32s_e17_v16?0"NSError"8ls32l8
- ___block_descriptor_40_e8_32s_e8_v16?08ls32l8
- ___block_descriptor_41_e8_32bs_e5_v8?0ls32l8
- ___block_descriptor_48_e8_32s40bs_e20_v20?0B8"NSError"12ls32l8s40l8
- ___block_descriptor_48_e8_32s40bs_e20_v24?0Q8"NSError"16ls32l8s40l8
- ___block_descriptor_48_e8_32s40bs_e20_v24?0q8"NSError"16ls32l8s40l8
- ___block_descriptor_48_e8_32s40bs_e28_v16?0"<RTDaemonProtocol>"8ls32l8s40l8
- ___block_descriptor_48_e8_32s40bs_e28_v24?0"NSDate"8"NSError"16ls32l8s40l8
- ___block_descriptor_48_e8_32s40bs_e30_v24?0"NSString"8"NSError"16ls32l8s40l8
- ___block_descriptor_48_e8_32s40bs_e32_v24?0"CLLocation"8"NSError"16ls32l8s40l8
- ___block_descriptor_48_e8_32s40bs_e33_v32?0"NSArray"8^B16"NSError"24ls32l8s40l8
- ___block_descriptor_48_e8_32s40bs_e34_v24?0"NSDictionary"8"NSError"16ls32l8s40l8
- ___block_descriptor_48_e8_32s40bs_e37_v24?0"RTPeopleDensity"8"NSError"16ls32l8s40l8
- ___block_descriptor_48_e8_32s40bs_e42_v24?0"RTLocationOfInterest"8"NSError"16ls32l8s40l8
- ___block_descriptor_48_e8_32s40bs_e43_v24?0"RTTripSegmentMetadata"8"NSError"16ls32l8s40l8
- ___block_descriptor_48_e8_32s40bs_e46_v24?0"RTPredictedContextResult"8"NSError"16ls32l8s40l8
- ___block_descriptor_48_e8_32s40bs_e8_v12?0B8ls32l8s40l8
- ___block_descriptor_48_e8_32s40bs_e8_v16?08ls32l8s40l8
- ___block_descriptor_48_e8_32s40s_e8_v16?08ls32l8s40l8
- ___block_descriptor_48_e8_32s_e8_v16?08ls32l8
- ___block_descriptor_49_e8_32bs_e5_v8?0ls32l8
- ___block_descriptor_49_e8_32s40bs_e5_v8?0ls40l8s32l8
- ___block_descriptor_49_e8_32s40bs_e8_v16?08ls32l8s40l8
- ___block_descriptor_56_e8_32s40bs_e29_v24?0"NSArray"8"NSError"16ls32l8s40l8
- ___block_descriptor_56_e8_32s40bs_e42_v24?0"RTLocationOfInterest"8"NSError"16ls32l8s40l8
- ___block_descriptor_56_e8_32s40bs_e48_v24?0"RTAuthorizedLocationStatus"8"NSError"16ls32l8s40l8
- ___block_descriptor_56_e8_32s40bs_e8_v12?0B8ls32l8s40l8
- ___block_descriptor_56_e8_32s40bs_e8_v16?08ls32l8s40l8
- ___block_descriptor_56_e8_32s40s48bs_e28_v16?0"<RTDaemonProtocol>"8ls32l8s40l8s48l8
- ___block_descriptor_56_e8_32s40s48bs_e5_v8?0ls32l8s48l8s40l8
- ___block_descriptor_56_e8_32s40s48bs_e8_v16?08ls32l8s40l8s48l8
- ___block_descriptor_64_e8_32s40bs_e8_v16?08ls32l8s40l8
- ___block_descriptor_64_e8_32s40s48bs_e28_v16?0"<RTDaemonProtocol>"8ls32l8s40l8s48l8
- ___block_descriptor_64_e8_32s40s48bs_e8_v16?08ls32l8s40l8s48l8
- ___block_descriptor_64_e8_32s40s48s56bs_e8_v16?08ls32l8s40l8s48l8s56l8
- ___block_descriptor_72_e8_32s40bs48bs_e17_v16?0"NSError"8ls32l8s40l8s48l8
- ___block_descriptor_72_e8_32s40s48s56bs_e8_v16?08ls32l8s40l8s48l8s56l8
- ___block_descriptor_72_e8_32s40s48s56s64bs_e8_v16?08ls32l8s40l8s48l8s56l8s64l8
- ___block_descriptor_80_e8_32s40bs48r56r64r72r_e29_v24?0"NSArray"8"NSError"16lr48l8r56l8s40l8r64l8r72l8s32l8
- ___block_descriptor_80_e8_32s40s48s56s64bs_e8_v16?08ls32l8s40l8s48l8s56l8s64l8
- ___block_descriptor_88_e8_32s40s48s56s64s72bs_e8_v16?08ls32l8s40l8s48l8s56l8s64l8s72l8
- ___block_literal_global.17
- ___block_literal_global.19
- ___block_literal_global.21
- ___block_literal_global.444
- ___block_literal_global.499
- ___block_literal_global.531
- ___block_literal_global.533
- ___block_literal_global.535
- ___block_literal_global.537
- ___block_literal_global.539
- ___block_literal_global.541
- ___block_literal_global.543
- ___block_literal_global.545
- ___block_literal_global.547
- ___block_literal_global.549
- ___block_literal_global.551
- ___block_literal_global.553
- ___block_literal_global.555
- ___log_analytics_submission_block_invoke
- _dispatch_queue_get_label
- _log_analytics_submission
- _objc_msgSend$_launchTaskWithSelector:remainingAttempts:proxyErrorHandler:taskBlock:
- _objc_msgSend$characterSetWithCharactersInString:
- _objc_msgSend$componentsSeparatedByCharactersInSet:
- _objc_msgSend$initWithApplePaySupport:category:muid:nearbyPoiCount:
- _objc_msgSend$initWithCString:encoding:
- _objc_msgSend$initWithFidelityPolicy:locations:accessPoints:distance:location:startDate:endDate:limit:useBackground:clientIdentifier:
- _objc_msgSend$initWithIdentifier:apToModelMapping:date:downloadKey:geoCacheInfo:geoTileKey:hashedApToModelMapping:hashedApToModelMappingDataURL:hashSalt:modelCalibrationParameters:models:modelURLs:pointsOfInterest:singlePOIMuid:size:
- _objc_msgSend$initWithIdentifier:applePaySupport:filtered:fullyCoversTile:location:muid:polygon:
- _objc_msgSend$initWithIdentifier:name:category:categoryMUID:address:location:source:mapItemPlaceType:muid:resultProviderID:geoMapItemHandle:geoMapItemIdentifier:creationDate:expirationDate:extendedAttributes:displayLanguage:disputed:businessHours:
- _objc_msgSend$initWithLearnedRouteId:routeStartLocation:routeEndLocation:travelTimeEntireRouteSec:travelDistanceEntireRouteMeter:travelModeRoutes:routeStartLocationWithReferenceFrame:routeEndLocationWithReferenceFrame:
- _objc_msgSend$initWithMinCountOfTraversal:startLatitude:startLongitude:endLatitude:endLongitude:
- _objc_msgSend$initWithStartAndEndVisitLatitude:startLongitude:endLatitude:endLongitude:
- _objc_msgSend$sortedArrayUsingComparator:
- _objc_msgSend$stringWithCString:encoding:
CStrings:
+ "%C"
+ "-[RTRoutineManager(AltimeterFloorMap) fetchAltimeterFloorMapDataWithOptions:handler:]"
+ "-[RTRoutineManager(AltimeterFloorMap) removeAltimeterFloorMapData:startDate:endDate:handler:]"
+ "-[RTRoutineManager(AltimeterFloorMap) storeAltimeterFloorMapData:handler:]"
+ "-[RTRoutineManager(RawAltimeter) fetchRawAltimeterDataWithOptions:handler:]"
+ "-[RTRoutineManager(RawAltimeter) removeRawAltimeterData:startDate:endDate:handler:]"
+ "-[RTRoutineManager(RawAltimeter) storeRawAltimeterData:handler:]"
+ "Ending transaction on error for %@, duration: %.3fs"
+ "ExtendedTimeToLive"
+ "GEOPOICategory"
+ "Head"
+ "InternalBuild"
+ "Invalid parameter not satisfying: altimeterFloorMapDataArray (in %s:%d)"
+ "Invalid parameter not satisfying: endDate (in %s:%d)"
+ "Invalid parameter not satisfying: rawAltimeterDataArray (in %s:%d)"
+ "RTDataIntegrityValidationResult, total, %lu, visitToPlace, %@, visitToMapItem, %@, loiToMapItem, %@, unexpectedFileExtensions, %@, duration, %.2fs"
+ "RTRoutineManager.%@"
+ "RTTripClusterRouteSummaryEnumerationContext: options=%@, offset=%lu"
+ "RTTripClusterRouteSummaryEnumerationOptions: clusterID=%@, batchSize=%lu"
+ "Reusing transaction for retry of %@"
+ "Started transaction for %@"
+ "Tail"
+ "Torso"
+ "UUID,%@,startTime,%@,endTime,%@,altimeterData,%.3lf,altimeterValueUncertainty,%.3lf,stepCount,%u"
+ "UUID,%@,startTime,%@,endTime,%@,type,%d,referenceUUID,%@,floorMapEntries,%lu,transitionModels,%lu,expirationDate,%@"
+ "Wallet"
+ "alternateCategoryMUIDs"
+ "alternateCategoryMuids"
+ "altimeterFloorMapEndTimeIdentifier"
+ "altimeterFloorMapExpirationDateIdentifier"
+ "altimeterFloorMapFloorMapArrayIdentifier"
+ "altimeterFloorMapReferenceUUIDIdentifier"
+ "altimeterFloorMapStartTimeIdentifier"
+ "altimeterFloorMapTransitionModelsIdentifier"
+ "altimeterFloorMapTypeIdentifier"
+ "altimeterFloorMapUUIDIdentifier"
+ "associatedPlaceInferences"
+ "b"
+ "batchSize,%lu,startLat,%.7f,startLon,%.7f,endLat,%.7f,endLon,%.7f,minCntTraversal,%d,timeWindowStart,%@,timeWindowEnd,%@"
+ "categoryDescription"
+ "categoryMuid"
+ "distancePriors"
+ "executionDuration"
+ "expirationDateBefore"
+ "fidelityPolicy, %@, locations count, %lu, last location, %@, accessPoints count, %lu, last accessPoint, %@, location, %@, distance, %f, startDate, %@, endDate, %@, limit, %ld, useBackground, %@, includeCandidates, %@, clientIdentifier, %@"
+ "floorIndex,%d,elevation,%.3f,elevationUncertainty,%.3f,initialFloorProbability,%.3f,duration,%.3lf"
+ "floorMapEntryDurationIdentifier"
+ "floorMapEntryElevationIdentifier"
+ "floorMapEntryElevationUncertaintyIdentifier"
+ "floorMapEntryFloorIndexIdentifier"
+ "floorMapEntryInitialFloorProbabilityIdentifier"
+ "highThresholdAfterCalibrationCombinedApplePay"
+ "highThresholdAfterCalibrationCombinedNonApplePay"
+ "highThresholdAfterCalibrationUncovered"
+ "highThresholdBeforeCalibrationCombinedApplePay"
+ "highThresholdBeforeCalibrationCombinedNonApplePay"
+ "highThresholdBeforeCalibrationUncovered"
+ "highestScoreCombinedApplePay"
+ "highestScoreCombinedNonApplePay"
+ "highestScoreUncovered"
+ "idString"
+ "idString, %@, muid, %llu"
+ "identifier, %@, date, %@, geoTileKey, %@, downloadKey, %@, distance priors, %@, geoCacheInfo, %@, size, %.1f kB, hashSalt, %@, apToModelMapping count, %lu, hashedApToModelMapping count, %lu, hashedApToModelMappingDataURL, %@, singlePOIMuid, %@, models, %@, model URLs, %@, modelCalibrationParameters, %@, pointsOfInterest, %@"
+ "identifier, %@, geoMapItemIdentifier, %@ (%@), name, \"%@\", category, %@, categoryDescription, %@, categoryMUID, %@, alternateCategoryMUIDs, %@, address, %@, location, %@, source, %@, map item place type, %@, muid, %lu, result provider ID: %ld, weight, %lf, creationDate, %@, businessHours, %@, extended attributes, %@, display language, %@, disputed, %@"
+ "identifier, %@, muid, %lu, location, %@, applyPaySupport, %@, filtered, %@, fullyCoversTile, %@, popularityTier, %@, categoryMuid, %llu, alternateCategoryMuids, %@"
+ "includeCandidates"
+ "lowThresholdAfterCalibrationCombinedApplePay"
+ "lowThresholdAfterCalibrationCombinedNonApplePay"
+ "lowThresholdAfterCalibrationUncovered"
+ "lowThresholdBeforeCalibrationCombinedApplePay"
+ "lowThresholdBeforeCalibrationCombinedNonApplePay"
+ "lowThresholdBeforeCalibrationUncovered"
+ "muid, %lu, applePaySupport, %@, category, %@, location, %@, name, %@, nearbyPOICount, %lu, popularityTier, %@"
+ "orphanCountsByType"
+ "popularityTier"
+ "rawAltimeterDataIdentifier"
+ "rawAltimeterEndTimeIdentifier"
+ "rawAltimeterStartTimeIdentifier"
+ "rawAltimeterStepCountIdentifier"
+ "rawAltimeterUUIDIdentifier"
+ "rawAltimeterValueUncertaintyIdentifier"
+ "recentTripTimes"
+ "referenceUUID"
+ "routeSummary"
+ "sampleOrphanedLOIIdentifiers"
+ "sampleOrphanedVisitIdentifiers"
+ "sampleUnexpectedFileExtensions"
+ "schedule"
+ "source, %@, confidence, %.3f, mapItem, %@"
+ "startDate,%@,endDate,%@,maximumNumberOfItems,%@"
+ "startDate,%@,endDate,%@,maximumNumberOfItems,%@,referenceUUID,%@,expirationDateBefore,%@"
+ "startFloorIndex,%d,endFloorIndex,%d,meanElevationChange,%.3f,elevationChangeStdDev,%.3f,meanTransitionTime,%.3lf,transitionTimeStdDev,%.3lf,averageSteps,%.3f,standardDeviationSteps,%.3f,occurrenceCount,%d"
+ "timeWindowEnd"
+ "timeWindowStart"
+ "transitionModelAverageStepsIdentifier"
+ "transitionModelElevationChangeStandardDeviationIdentifier"
+ "transitionModelEndFloorIndexIdentifier"
+ "transitionModelMeanElevationChangeIdentifier"
+ "transitionModelMeanTransitionTimeIdentifier"
+ "transitionModelOccurrenceCountIdentifier"
+ "transitionModelStandardDeviationStepsIdentifier"
+ "transitionModelStartFloorIndexIdentifier"
+ "transitionModelTransitionTimeStandardDeviationIdentifier"
+ "v24@?0@\"<RTDaemonProtocol>\"8@\"RTTransaction\"16"
+ "v24@?0@8@\"RTTransaction\"16"
+ "v28@?0@\"NSArray\"8B16@\"NSError\"20"
+ "v28@?0@\"NSMutableArray\"8B16@\"NSError\"20"
+ "yyyy-MM-dd-HHmmss"
- "\n=== BEGIN analytics submission for event %@ ===\n"
- "#16@0:8"
- "#24@0:8@16"
- "%@ : %@\n"
- "- "
- ".cxx_destruct"
- "=== END analytics submission for event %@ ===\n"
- "@"
- "@\"CLLocation\""
- "@\"GEOAddressObject\""
- "@\"NSArray\""
- "@\"NSData\""
- "@\"NSDate\""
- "@\"NSDateInterval\""
- "@\"NSDictionary\""
- "@\"NSError\""
- "@\"NSMutableDictionary\""
- "@\"NSNumber\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSSet\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"NSURL\""
- "@\"NSUUID\""
- "@\"NSXPCConnection\""
- "@\"RTAddress\""
- "@\"RTAuthorizedLocationConfirmationStatusEnumerationOptions\""
- "@\"RTAuthorizedLocationZDRLocationsEnumerationOptions\""
- "@\"RTBackgroundInertialOdometrySampleEnumerationOptions\""
- "@\"RTCoordinate\""
- "@\"RTDistanceInterval\""
- "@\"RTEventAgentHelper\""
- "@\"RTGeoRoadDataEnumerationOptions\""
- "@\"RTLearnedRouteLocation\""
- "@\"RTLearnedRouteMetrics\""
- "@\"RTLocation\""
- "@\"RTLocationDownsamplerTree\""
- "@\"RTLocationOfInterest\""
- "@\"RTMapItem\""
- "@\"RTMapItemExtendedAttributes\""
- "@\"RTPeopleDensityCallbackConfiguration\""
- "@\"RTPeopleDiscoveryServiceConfiguration\""
- "@\"RTPlaceInference\""
- "@\"RTPlaceInferenceOptions\""
- "@\"RTPolygon\""
- "@\"RTPredictedContextAnalytics\""
- "@\"RTPredictedContextDate\""
- "@\"RTPredictedContextDateInterval\""
- "@\"RTPredictedContextOptions\""
- "@\"RTPredictedContextResult\""
- "@\"RTRoutineManager\""
- "@\"RTRoutineManagerRegistrantAction\""
- "@\"RTRoutineManagerRegistrantGeneratedTripSegments\""
- "@\"RTRoutineManagerRegistrantPeopleDiscovery\""
- "@\"RTRoutineManagerRegistrantScenarioTrigger\""
- "@\"RTStoredElevationEnumerationOptions\""
- "@\"RTStoredLocationEnumerationOptions\""
- "@\"RTSynthesizedLocationEnumerationOptions\""
- "@\"RTTokenBucket\""
- "@\"RTTripClusterEnumerationOptions\""
- "@\"RTTripClusterRecencyEnumerationOptions\""
- "@\"RTTripClusterRoadTransitionsEnumerationOptions\""
- "@\"RTTripClusterRouteEnumerationOptions\""
- "@\"RTTripClusterScheduleEnumerationOptions\""
- "@\"RTTripClusterWaypointEnumerationOptions\""
- "@\"RTTripSegmentInertialDataEnumerationOptions\""
- "@\"RTVehicleEvent\""
- "@104@0:8@16@24@32@40@48@56@64@72@80@88@96"
- "@108@0:8@16@24d32d40q48B56i60i64d68d76d84d92@100"
- "@136@0:8@16@24@32@40@48Q56@64@72@80@88@96@104@112Q120d128"
- "@148@0:8@16@24@32@40@48@56Q64Q72Q80q88@96@104@112@120@128@136B144"
- "@156@0:8@16@24@32@40@48@56Q64Q72Q80q88@96@104@112@120@128@136B144@148"
- "@16@0:8"
- "@180@0:8@16@24@32@40@48@56@64@72@80@88@96@104@112@120@128@136B144@148@156@164@172"
- "@180@0:8@16@24q32i40d44d52d60d68d76d84d92d100d108d116@124B132d136d144d152d160i168i172s176"
- "@20@0:8B16"
- "@24@0:8:16"
- "@24@0:8@\"NSCoder\"16"
- "@24@0:8@16"
- "@24@0:8@?16"
- "@24@0:8Q16"
- "@24@0:8^{_NSZone=}16"
- "@24@0:8d16"
- "@24@0:8q16"
- "@28@0:8@16B24"
- "@28@0:8@16i24"
- "@28@0:8B16@20"
- "@32@0:8:16@24"
- "@32@0:8:16@?24"
- "@32@0:8@16@24"
- "@32@0:8@16@?24"
- "@32@0:8@16Q24"
- "@32@0:8@16^@24"
- "@32@0:8@16d24"
- "@32@0:8@16q24"
- "@32@0:8Q16@24"
- "@32@0:8Q16@?24"
- "@32@0:8Q16q24"
- "@32@0:8d16@24"
- "@32@0:8d16d24"
- "@32@0:8q16d24"
- "@36@0:8:16B24@?28"
- "@36@0:8@16B24B28B32"
- "@36@0:8B16@20@28"
- "@36@0:8B16Q20@28"
- "@36@0:8d16B24d28"
- "@40@0:8:16@24@32"
- "@40@0:8@16@24@32"
- "@40@0:8@16@24d32"
- "@40@0:8@16@24q32"
- "@40@0:8@16@?24d32"
- "@40@0:8@16@?24q32"
- "@40@0:8@16B24B28B32B36"
- "@40@0:8@16d24Q32"
- "@40@0:8@16d24d32"
- "@40@0:8@16q24@32"
- "@40@0:8@16q24Q32"
- "@40@0:8B16Q20@28B36"
- "@40@0:8Q16@24@32"
- "@40@0:8Q16Q24@32"
- "@40@0:8Q16Q24@?32"
- "@40@0:8d16@24@32"
- "@40@0:8d16d24d32"
- "@40@0:8q16q24q32"
- "@44@0:8@16B24d28q36"
- "@44@0:8@16d24Q32B40"
- "@44@0:8B16@20@28@36"
- "@44@0:8B16@20Q28Q36"
- "@48@0:8@16@24@32@40"
- "@48@0:8@16@24@32^@40"
- "@48@0:8@16@24@32d40"
- "@48@0:8@16@24Q32@40"
- "@48@0:8@16@?24d32Q40"
- "@48@0:8@16Q24@32@40"
- "@48@0:8@16Q24@32B40B44"
- "@48@0:8@16d24Q32@40"
- "@48@0:8@16q24Q32@40"
- "@48@0:8@16q24Q32Q40"
- "@48@0:8B16@20@28B36@40"
- "@48@0:8Q16@24@32@40"
- "@48@0:8Q16Q24Q32@40"
- "@48@0:8d16@24@32@40"
- "@48@0:8d16@24d32q40"
- "@48@0:8d16Q24@32@40"
- "@48@0:8d16d24d32@40"
- "@48@0:8d16d24d32B40i44"
- "@48@0:8d16d24d32d40"
- "@52@0:8@16@24B32d36q44"
- "@52@0:8@16B24@28Q36Q44"
- "@52@0:8@16d24Q32@40i48"
- "@52@0:8B16Q20@28@36@44"
- "@52@0:8S16d20d28d36d44"
- "@52@0:8d16d24d32@40i48"
- "@56@0:8@16@24@32@40@48"
- "@56@0:8@16@24Q32@40@48"
- "@56@0:8@16d24@32q40@48"
- "@56@0:8@16d24Q32@40i48B52"
- "@56@0:8@16q24@32Q40Q48"
- "@56@0:8@16q24q32d40@48"
- "@56@0:8B16@20@28B36@40@48"
- "@56@0:8Q16Q24Q32Q40@48"
- "@56@0:8d16@24@32@40@48"
- "@60@0:8@16@24@32@40i48B52i56"
- "@60@0:8@16@24B32@36Q44Q52"
- "@60@0:8@16B24B28B32@36Q44@52"
- "@60@0:8@16d24Q32@40B48d52"
- "@60@0:8B16@20@28B36@40@48B56"
- "@64@0:8@16@24@32@40@48@56"
- "@64@0:8@16@24@32@40@48q56"
- "@64@0:8@16@24@32@40d48Q56"
- "@64@0:8@16@24@32Q40Q48Q56"
- "@64@0:8@16@24@32d40d48@56"
- "@64@0:8@16@24d32@40q48Q56"
- "@64@0:8@16@24d32Q40@48@56"
- "@64@0:8@16@24q32Q40@48@56"
- "@64@0:8@16d24Q32@40i48B52d56"
- "@64@0:8B16@20@28B36@40@48B56B60"
- "@64@0:8Q16Q24Q32Q40Q48@56"
- "@68@0:8@16@24@32@40@48B56Q60"
- "@68@0:8@16@24@32@40@48i56B60i64"
- "@68@0:8@16@24B32@36@44Q52Q60"
- "@72@0:8@16@24@32f40f44@48@56@64"
- "@72@0:8@16Q24Q32Q40@48d56@64"
- "@72@0:8@16d24Q32@40i48B52B56d60B68"
- "@72@0:8@16d24d32d40Q48d56d64"
- "@72@0:8q16f24f28f32f36f40f44@48@56@64"
- "@76@0:8@16@24@32@40@48B56Q60@68"
- "@76@0:8@16@24@32B40@44@52@60@68"
- "@76@0:8d16d24d32d40d48@56i64d68"
- "@80@0:8@16@24@32@40@48@56@64@72"
- "@80@0:8@16@24@32@40q48d56d64Q72"
- "@80@0:8@16@24@32B40@44@52@60@68B76"
- "@80@0:8@16@24@32q40d48@56@64@72"
- "@80@0:8@16Q24Q32Q40@48d56@64@72"
- "@80@0:8@16d24@32q40Q48@56@64@72"
- "@80@0:8@16q24@32@40@48q56d64@72"
- "@84@0:8d16d24d32d40d48@56i64d68Q76"
- "@88@0:8@16@24Q32Q40Q48@56d64d72@80"
- "@88@0:8@16q24@32@40@48q56d64@72q80"
- "@92@0:8@16@24@32@40@48B56Q60B68B72@76@84"
- "@92@0:8Q16@24@32d40@48@56@64q72B80@84"
- "@96@0:8@16@24Q32Q40Q48@56d64d72@80@88"
- "@96@0:8@16q24@32@40@48q56d64@72q80@88"
- "@?"
- "@?16@0:8"
- "B"
- "B16@0:8"
- "B20@0:8i16"
- "B20@0:8s16"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B24@0:8Q16"
- "B24@0:8d16"
- "B24@0:8q16"
- "B32@0:8@16@24"
- "B36@0:8@16@24i32"
- "CoreRoutine.HangsMetrics"
- "Invalid parameter not satisfying: geoMapItemHandle"
- "JSONStringFromNSDictionary:error:"
- "METRIC"
- "NSCoding"
- "NSCopying"
- "NSObject"
- "NSSecureCoding"
- "NextLessDecimatedDownsamplingPreference:"
- "Q16@0:8"
- "Q24@0:8@16"
- "Q24@0:8d16"
- "Q32@0:8Q16Q24"
- "Q40@0:8@16Q24Q32"
- "RTAddress"
- "RTAddressSubPremise"
- "RTAuthorizedLocationConfirmationStatusEnumerationContext"
- "RTAuthorizedLocationConfirmationStatusEnumerationOptions"
- "RTAuthorizedLocationDiagnosticStatus"
- "RTAuthorizedLocationZDRLocationsEnumerationContext"
- "RTAuthorizedLocationZDRLocationsEnumerationOptions"
- "RTBackgroundInertialOdometrySampleEnumerationContext"
- "RTBackgroundInertialOdometrySampleEnumerationOptions"
- "RTBluePOIMetadata"
- "RTBluePOIModel"
- "RTBluePOITile"
- "RTBluePOITileDownloadResult"
- "RTBusinessHours"
- "RTContactScore"
- "RTCoordinate"
- "RTDaemonProtocol"
- "RTDailyHours"
- "RTDiagnosticOptions"
- "RTDiagnosticOptionsMaskToString:"
- "RTDistanceInterval"
- "RTElevation"
- "RTEnumerationOptions"
- "RTEstimatedLocationOptions"
- "RTEventAgentHelper"
- "RTExtensions"
- "RTFamiliarityIndexOptions"
- "RTFamiliarityIndexResult"
- "RTFetchFingerprintsOptions"
- "RTFingerprint"
- "RTFrameworkProtocol"
- "RTGeoRoadDataEnumerationContext"
- "RTGeoRoadDataEnumerationOptions"
- "RTHangsMetrics"
- "RTHint"
- "RTInferredMapItem"
- "RTLearnedRoute"
- "RTLearnedRouteFetchOptions"
- "RTLearnedRouteLocation"
- "RTLearnedRouteMetrics"
- "RTLearnedRouteTravelMode"
- "RTLocalBluePOIResult"
- "RTLocalTimeInterval"
- "RTLocation"
- "RTLocationDownsampler"
- "RTLocationDownsamplerTree"
- "RTLocationOfInterest"
- "RTLocationOfInterestEnumerationOptions"
- "RTLocationOfInterestTransition"
- "RTLocationOfInterestVisit"
- "RTLocationsForTripSegmentFetchOptions"
- "RTLocationsFromCoreLocationFetchOptions"
- "RTMapItem"
- "RTMapItemExtendedAttributes"
- "RTMapServiceOptions"
- "RTMotionActivity"
- "RTPair"
- "RTPeopleCountEvent"
- "RTPeopleDensity"
- "RTPeopleDensityCallbackConfiguration"
- "RTPeopleDiscoveryServiceConfiguration"
- "RTPlaceInference"
- "RTPlaceInferenceOptions"
- "RTPlaceInferenceQuery"
- "RTPointOfInterest"
- "RTPointOfInterestAttributes"
- "RTPolygon"
- "RTPredictedContext"
- "RTPredictedContextAnalytics"
- "RTPredictedContextAnalyticsRolledLOIResult"
- "RTPredictedContextDate"
- "RTPredictedContextDateInterval"
- "RTPredictedContextLocation"
- "RTPredictedContextOptions"
- "RTPredictedContextRequest"
- "RTPredictedContextResult"
- "RTPredictedContextSequence"
- "RTPredictedContextTransition"
- "RTPredictedContextTransport"
- "RTPredictedContextWorkout"
- "RTPredictedDate"
- "RTPredictedLocationOfInterest"
- "RTProximityEvent"
- "RTRoutineManager"
- "RTRoutineManagerExportedObject"
- "RTRoutineManagerRegistrant"
- "RTRoutineManagerRegistrantGeneratedTripSegments"
- "RTRoutineManagerRegistrantPeopleDiscovery"
- "RTRoutineManagerRegistrantScenarioTrigger"
- "RTScenarioTrigger"
- "RTScenarioTriggerSettled"
- "RTScenarioTriggerUnsettled"
- "RTSignalGeneratorOptions"
- "RTSource"
- "RTSourceCoreRoutine"
- "RTSourceCoreRoutineLearnedLocation"
- "RTSourceCoreRoutineVehicleEvent"
- "RTSourceEventKit"
- "RTSourceHealthKitWorkout"
- "RTSourceHomeKit"
- "RTSourceMapsSupport"
- "RTSourceMapsSupportFavoritePlace"
- "RTSourceMapsSupportHistoryEntry"
- "RTSourceMapsSupportHistoryEntryPlaceDisplay"
- "RTSourceMapsSupportHistoryEntryRoute"
- "RTSourceParkedCar"
- "RTSourcePropagatedLocation"
- "RTStoredElevationEnumerationContext"
- "RTStoredElevationEnumerationOptions"
- "RTStoredHintEnumerationOptions"
- "RTStoredLocationEnumerationContext"
- "RTStoredLocationEnumerationOptions"
- "RTStoredTripSegmentFetchOptions"
- "RTStoredUserCurationFetchOptions"
- "RTStoredVehicleFetchOptions"
- "RTStoredVisitFetchOptions"
- "RTSynthesizedLocationEnumerationContext"
- "RTSynthesizedLocationEnumerationOptions"
- "RTTokenBucket"
- "RTTripClusterEnumerationContext"
- "RTTripClusterEnumerationOptions"
- "RTTripClusterMetadata"
- "RTTripClusterMetadataFetchOptions"
- "RTTripClusterRecencyEnumerationContext"
- "RTTripClusterRecencyEnumerationOptions"
- "RTTripClusterRoadTransitionsEnumerationContext"
- "RTTripClusterRoadTransitionsEnumerationOptions"
- "RTTripClusterRouteEnumerationContext"
- "RTTripClusterRouteEnumerationOptions"
- "RTTripClusterScheduleEnumerationContext"
- "RTTripClusterScheduleEnumerationOptions"
- "RTTripClusterWaypointEnumerationContext"
- "RTTripClusterWaypointEnumerationOptions"
- "RTTripSegment"
- "RTTripSegmentFormOfWay"
- "RTTripSegmentInertialDataEnumerationContext"
- "RTTripSegmentInertialDataEnumerationOptions"
- "RTTripSegmentLocationType"
- "RTTripSegmentMetadata"
- "RTTripSegmentMetadataFetchOptions"
- "RTTripSegmentRoadClass"
- "RTUserCuration"
- "RTVehicle"
- "RTVehicleEvent"
- "RTVisit"
- "RTWiFiAccessPoint"
- "S"
- "S16@0:8"
- "Skyline"
- "T#,R"
- "T@\"CLLocation\",C,N,V_boundingBoxLocation"
- "T@\"CLLocation\",C,N,V_destinationVisit"
- "T@\"CLLocation\",C,N,V_originVisit"
- "T@\"CLLocation\",R,N,V_learnedRouteEndLocation"
- "T@\"CLLocation\",R,N,V_learnedRouteStartLocation"
- "T@\"NSArray\",&,N,V_locations"
- "T@\"NSArray\",&,V_fullConfirmationList"
- "T@\"NSArray\",&,V_zdrConfirmationList"
- "T@\"NSArray\",R,C,N,V_businessHours"
- "T@\"NSArray\",R,C,N,V_combinedFrequencyScores"
- "T@\"NSArray\",R,C,N,V_combinedRecencyScores"
- "T@\"NSArray\",R,C,N,V_combinedSignificanceScores"
- "T@\"NSArray\",R,C,N,V_contexts"
- "T@\"NSArray\",R,C,N,V_dailyHours"
- "T@\"NSArray\",R,C,N,V_predictedContexts"
- "T@\"NSArray\",R,C,N,V_timeIntervals"
- "T@\"NSArray\",R,N"
- "T@\"NSArray\",R,N,V_accessPoints"
- "T@\"NSArray\",R,N,V_categoryDenyList"
- "T@\"NSArray\",R,N,V_expectedVisits"
- "T@\"NSArray\",R,N,V_filterLocations"
- "T@\"NSArray\",R,N,V_formOfWay"
- "T@\"NSArray\",R,N,V_learnedRouteLocations"
- "T@\"NSArray\",R,N,V_locationType"
- "T@\"NSArray\",R,N,V_locations"
- "T@\"NSArray\",R,N,V_modelURLs"
- "T@\"NSArray\",R,N,V_predictedContextTransports"
- "T@\"NSArray\",R,N,V_predictionSources"
- "T@\"NSArray\",R,N,V_resultSortDescriptors"
- "T@\"NSArray\",R,N,V_roadClass"
- "T@\"NSArray\",R,N,V_routeLocations"
- "T@\"NSArray\",R,N,V_sources"
- "T@\"NSArray\",R,N,V_subPremises"
- "T@\"NSArray\",R,N,V_travelModeRoutes"
- "T@\"NSArray\",R,N,V_vertices"
- "T@\"NSArray\",R,N,V_visits"
- "T@\"NSData\",&,N,V_photo"
- "T@\"NSData\",R,C,N,V_geoAddressData"
- "T@\"NSData\",R,N,V_downloadKey"
- "T@\"NSData\",R,N,V_geoCacheInfo"
- "T@\"NSData\",R,N,V_geoMapItemHandle"
- "T@\"NSData\",R,N,V_geoMapItemIdentifier"
- "T@\"NSData\",R,N,V_hashSalt"
- "T@\"NSData\",R,N,V_tileCacheInfo"
- "T@\"NSDate\",&,N,V_creationDate"
- "T@\"NSDate\",&,N,V_endDate"
- "T@\"NSDate\",&,N,V_startDate"
- "T@\"NSDate\",C,N,V_date"
- "T@\"NSDate\",R,C,N,V_date"
- "T@\"NSDate\",R,C,N,V_dateOfMostRecentTrip"
- "T@\"NSDate\",R,C,N,V_entry"
- "T@\"NSDate\",R,C,N,V_exit"
- "T@\"NSDate\",R,C,N,V_requestEndDate"
- "T@\"NSDate\",R,C,N,V_requestStartDate"
- "T@\"NSDate\",R,C,N,V_routeDate"
- "T@\"NSDate\",R,C,N,V_startDate"
- "T@\"NSDate\",R,C,N,V_stopDate"
- "T@\"NSDate\",R,N,V_creationDate"
- "T@\"NSDate\",R,N,V_date"
- "T@\"NSDate\",R,N,V_endDate"
- "T@\"NSDate\",R,N,V_entryDate"
- "T@\"NSDate\",R,N,V_exitDate"
- "T@\"NSDate\",R,N,V_expirationDate"
- "T@\"NSDate\",R,N,V_lastTravelledDate"
- "T@\"NSDate\",R,N,V_nextEntryTime"
- "T@\"NSDate\",R,N,V_parkDate"
- "T@\"NSDate\",R,N,V_queryTime"
- "T@\"NSDate\",R,N,V_start"
- "T@\"NSDate\",R,N,V_startDate"
- "T@\"NSDate\",R,N,V_submissionDate"
- "T@\"NSDate\",R,N,V_usageDate"
- "T@\"NSDate\",R,N,V_visitEntryDate"
- "T@\"NSDate\",R,N,V_visitExitDate"
- "T@\"NSDateInterval\",C,N,V_dateInterval"
- "T@\"NSDateInterval\",C,N,V_submissionDateInterval"
- "T@\"NSDateInterval\",C,N,V_visitDateInterval"
- "T@\"NSDateInterval\",R,C,N,V_dateInterval"
- "T@\"NSDateInterval\",R,N,V_dateInterval"
- "T@\"NSDateInterval\",R,N,V_forecastWindowDateInterval"
- "T@\"NSDictionary\",R,C,N,V__scenarioTriggerHandlers"
- "T@\"NSDictionary\",R,C,N,V_rolledLOIResult"
- "T@\"NSDictionary\",R,N,V_aoiConfidences"
- "T@\"NSDictionary\",R,N,V_apToModelMapping"
- "T@\"NSDictionary\",R,N,V_featureToHashedApMapping"
- "T@\"NSDictionary\",R,N,V_hashedApToModelMapping"
- "T@\"NSDictionary\",R,N,V_modelCalibrationParameters"
- "T@\"NSDictionary\",R,N,V_poiConfidences"
- "T@\"NSDictionary\",R,N,V_rssiHistogram"
- "T@\"NSDictionary\",R,N,V_suggestionsSchemaOrg"
- "T@\"NSError\",R,N,V_downloadError"
- "T@\"NSNumber\",R,C,N,V_machContinuousTimeSec"
- "T@\"NSNumber\",R,C,N,V_numberOfSeconds"
- "T@\"NSNumber\",R,N,V_categoryMUID"
- "T@\"NSNumber\",R,N,V_confidence"
- "T@\"NSNumber\",R,N,V_distance"
- "T@\"NSNumber\",R,N,V_distanceToNearestAOILowerBound"
- "T@\"NSNumber\",R,N,V_limit"
- "T@\"NSNumber\",R,N,V_maximumNumberOfItems"
- "T@\"NSNumber\",R,N,V_sourceFilter"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_queue"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_xpcQueue"
- "T@\"NSSet\",R,N,V_models"
- "T@\"NSSet\",R,N,V_pointsOfInterest"
- "T@\"NSSet\",R,N,V_sources"
- "T@\"NSString\",&,N,V_restorationIdentifier"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",C,N,V_addressIdentifier"
- "T@\"NSString\",C,N,V_bundleIdentifier"
- "T@\"NSString\",C,N,V_bundlePath"
- "T@\"NSString\",C,N,V_notes"
- "T@\"NSString\",C,N,V_vehicleIdentifier"
- "T@\"NSString\",R,C"
- "T@\"NSString\",R,C,N"
- "T@\"NSString\",R,C,N,V_bluetoothAddress"
- "T@\"NSString\",R,C,N,V_category"
- "T@\"NSString\",R,C,N,V_displayLanguage"
- "T@\"NSString\",R,C,N,V_iso3166CountryCode"
- "T@\"NSString\",R,C,N,V_iso3166SubdivisionCode"
- "T@\"NSString\",R,C,N,V_name"
- "T@\"NSString\",R,C,N,V_subPremise"
- "T@\"NSString\",R,C,N,V_vehicleModelName"
- "T@\"NSString\",R,C,N,V_vehicleName"
- "T@\"NSString\",R,N"
- "T@\"NSString\",R,N,V_analyticsIdentifier"
- "T@\"NSString\",R,N,V_category"
- "T@\"NSString\",R,N,V_clientIdentifier"
- "T@\"NSString\",R,N,V_configurationIdentifier"
- "T@\"NSString\",R,N,V_contactID"
- "T@\"NSString\",R,N,V_customLabel"
- "T@\"NSString\",R,N,V_endLocationName"
- "T@\"NSString\",R,N,V_eventIdentifier"
- "T@\"NSString\",R,N,V_featureToHashedApMappingDataURL"
- "T@\"NSString\",R,N,V_hashedApToModelMappingDataURL"
- "T@\"NSString\",R,N,V_identifier"
- "T@\"NSString\",R,N,V_location"
- "T@\"NSString\",R,N,V_mac"
- "T@\"NSString\",R,N,V_preferredName"
- "T@\"NSString\",R,N,V_sourceIdentifier"
- "T@\"NSString\",R,N,V_startLocationName"
- "T@\"NSString\",R,N,V_suggestionInfo_opaqueKey"
- "T@\"NSString\",R,N,V_title"
- "T@\"NSString\",R,N,V_url"
- "T@\"NSString\",R,V_sourceBundleIdentifier"
- "T@\"NSURL\",R,N,V_tileURL"
- "T@\"NSUUID\",&,N,V_identifier"
- "T@\"NSUUID\",C,N,V_clusterID"
- "T@\"NSUUID\",C,N,V_identifier"
- "T@\"NSUUID\",C,N,V_tripCommuteID"
- "T@\"NSUUID\",R,C,N,V_clusterID"
- "T@\"NSUUID\",R,C,N,V_commuteID"
- "T@\"NSUUID\",R,C,N,V_identifier"
- "T@\"NSUUID\",R,N,V_eventID"
- "T@\"NSUUID\",R,N,V_identifier"
- "T@\"NSUUID\",R,N,V_learnedRouteIdentifier"
- "T@\"NSUUID\",R,N,V_loiIdentifier"
- "T@\"NSUUID\",R,N,V_uuid"
- "T@\"NSUUID\",R,N,V_visitIdentifier"
- "T@\"NSUUID\",R,N,V_visitIdentifierDestination"
- "T@\"NSUUID\",R,N,V_visitIdentifierOrigin"
- "T@\"NSUUID\",R,N,V_workoutUUID"
- "T@\"NSXPCConnection\",&,N,V_xpcConnection"
- "T@\"RTAddress\",R,N,V_address"
- "T@\"RTAuthorizedLocationConfirmationStatusEnumerationOptions\",R,N,V_options"
- "T@\"RTAuthorizedLocationZDRLocationsEnumerationOptions\",R,N,V_options"
- "T@\"RTBackgroundInertialOdometrySampleEnumerationOptions\",R,N,V_options"
- "T@\"RTCoordinate\",R,N,V_centroid"
- "T@\"RTDistanceInterval\",R,N,V_distanceInterval"
- "T@\"RTEventAgentHelper\",&,N,V_eventAgentHelper"
- "T@\"RTGeoRoadDataEnumerationOptions\",R,N,V_options"
- "T@\"RTLearnedRouteLocation\",R,N,V_learnedRouteEndLocationWithReferenceFrame"
- "T@\"RTLearnedRouteLocation\",R,N,V_learnedRouteStartLocationWithReferenceFrame"
- "T@\"RTLearnedRouteMetrics\",R,N,V_learnedRouteMetrics"
- "T@\"RTLocation\",C,N,V_location"
- "T@\"RTLocation\",R,C,N,V_location"
- "T@\"RTLocation\",R,N,V_endLocation"
- "T@\"RTLocation\",R,N,V_location"
- "T@\"RTLocation\",R,N,V_referenceLocation"
- "T@\"RTLocation\",R,N,V_startLocation"
- "T@\"RTLocationDownsamplerTree\",&,N,V_left"
- "T@\"RTLocationDownsamplerTree\",&,N,V_right"
- "T@\"RTLocationOfInterest\",C,N,V_nearbyLocationOfInterest"
- "T@\"RTLocationOfInterest\",R,N,V_locationOfInterest"
- "T@\"RTMapItem\",&,N,V_mapItem"
- "T@\"RTMapItem\",R,N,V_curatedLabel"
- "T@\"RTMapItem\",R,N,V_finerGranularityMapItem"
- "T@\"RTMapItem\",R,N,V_mapItem"
- "T@\"RTMapItem\",R,N,V_originalLabel"
- "T@\"RTMapItemExtendedAttributes\",&,N,V_extendedAttributes"
- "T@\"RTPeopleDensityCallbackConfiguration\",R,N,V_densityCallbackConfiguration"
- "T@\"RTPeopleDiscoveryServiceConfiguration\",R,N,V_configuration"
- "T@\"RTPlaceInference\",&,N,V_placeInference"
- "T@\"RTPlaceInference\",R,N,V_placeInference"
- "T@\"RTPlaceInferenceOptions\",&,N,V_placeInferenceOptions"
- "T@\"RTPolygon\",R,N,V_polygon"
- "T@\"RTPredictedContextAnalytics\",R,C,N,V_analytics"
- "T@\"RTPredictedContextDate\",R,C,N,V_endDate"
- "T@\"RTPredictedContextDate\",R,C,N,V_startDate"
- "T@\"RTPredictedContextDateInterval\",R,C,N,V_dateInterval"
- "T@\"RTPredictedContextOptions\",&,N,V_predictedContextOptions"
- "T@\"RTPredictedContextResult\",R,N,V_predictedContextResult"
- "T@\"RTRoutineManager\",W,N,V_routineManager"
- "T@\"RTRoutineManagerRegistrantAction\",&,N,V_actionRegistrant"
- "T@\"RTRoutineManagerRegistrantGeneratedTripSegments\",&,N,V_generatedTripSegmentRegistrant"
- "T@\"RTRoutineManagerRegistrantPeopleDiscovery\",&,N,V_peopleDiscoveryRegistrant"
- "T@\"RTRoutineManagerRegistrantScenarioTrigger\",&,N,V_scenarioTriggerRegistrant"
- "T@\"RTSource\",R,N"
- "T@\"RTStoredElevationEnumerationOptions\",R,N,V_options"
- "T@\"RTStoredLocationEnumerationOptions\",R,C,N,V_options"
- "T@\"RTSynthesizedLocationEnumerationOptions\",R,N,V_options"
- "T@\"RTTokenBucket\",&,N,V_clientThrottle"
- "T@\"RTTripClusterEnumerationOptions\",R,N,V_options"
- "T@\"RTTripClusterRecencyEnumerationOptions\",R,N,V_options"
- "T@\"RTTripClusterRoadTransitionsEnumerationOptions\",R,N,V_options"
- "T@\"RTTripClusterRouteEnumerationOptions\",R,N,V_options"
- "T@\"RTTripClusterScheduleEnumerationOptions\",R,N,V_options"
- "T@\"RTTripClusterWaypointEnumerationOptions\",R,N,V_options"
- "T@\"RTTripSegmentInertialDataEnumerationOptions\",R,N,V_options"
- "T@\"RTVehicleEvent\",R,N,V_vehicleEvent"
- "T@,R,N,V_firstObject"
- "T@,R,N,V_secondObject"
- "T@?,C,N,V_clientCallback"
- "T@?,C,N,V_leechedLowConfidenceVisitHandler"
- "T@?,C,N,V_leechedVisitHandler"
- "T@?,C,N,V_peopleDiscoveryErrorHandler"
- "T@?,C,N,V_placeInferencesHandler"
- "T@?,C,N,V_predictedContextHandler"
- "T@?,C,N,V_remoteStatusHandler"
- "T@?,C,N,V_vehicleEventsHandler"
- "T@?,C,N,V_visitHandler"
- "T@?,R,N,V_densityUpdateHandler"
- "TB,N,V_ascending"
- "TB,N,V_confirmed"
- "TB,N,V_downsampleRequired"
- "TB,N,V_isConsumedByClustering"
- "TB,N,V_isMe"
- "TB,N,V_locationFinalized"
- "TB,N,V_smoothingRequired"
- "TB,N,V_targetUserSession"
- "TB,N,V_userSetLocation"
- "TB,N,V_usualLocation"
- "TB,R"
- "TB,R,N,GisAllDay,V_allDay"
- "TB,R,N,GisAscending,V_ascending"
- "TB,R,N,GisRegistered"
- "TB,R,N,V_applePaySupport"
- "TB,R,N,V_ascending"
- "TB,R,N,V_disputed"
- "TB,R,N,V_enableFallbackModel"
- "TB,R,N,V_fetchAllRouteLocations"
- "TB,R,N,V_filterPairedVisitEntries"
- "TB,R,N,V_filtered"
- "TB,R,N,V_followedByUTurn"
- "TB,R,N,V_fullyCoversTile"
- "TB,R,N,V_isHome"
- "TB,R,N,V_isIsland"
- "TB,R,N,V_isLocked"
- "TB,R,N,V_isWork"
- "TB,R,N,V_labelVisit"
- "TB,R,N,V_loiIsMissingFromCurrentVisitHistory"
- "TB,R,N,V_navigationWasInterrupted"
- "TB,R,N,V_participationOptional"
- "TB,R,N,V_primary"
- "TB,R,N,V_redact"
- "TB,R,N,V_referenceLocationSummary"
- "TB,R,N,V_registered"
- "TB,R,N,V_resultSortProbabilityAscending"
- "TB,R,N,V_resultSortStartDateAscending"
- "TB,R,N,V_tentative"
- "TB,R,N,V_useBackground"
- "TB,R,N,V_useBackgroundTraits"
- "TB,R,N,V_wrappedVisit"
- "TB,R,V_fetchFormOfWay"
- "TB,R,V_fetchLocationType"
- "TB,R,V_fetchPreferredNames"
- "TB,R,V_fetchRoadClass"
- "TQ,N,V_batchSize"
- "TQ,N,V_frequencyCount"
- "TQ,N,V_locationQuality"
- "TQ,N,V_maximumErrorIndex"
- "TQ,N,V_mostConfidentAOI"
- "TQ,N,V_mostConfidentPOI"
- "TQ,N,V_optionsMask"
- "TQ,N,V_settledState"
- "TQ,N,V_source"
- "TQ,R"
- "TQ,R,N"
- "TQ,R,N,V_advertisingCapability"
- "TQ,R,N,V_allRoutesCountForThisODPair"
- "TQ,R,N,V_allTraversalCountBetweenThisODPair"
- "TQ,R,N,V_batchSize"
- "TQ,R,N,V_clientCount"
- "TQ,R,N,V_confidence"
- "TQ,R,N,V_familyCount"
- "TQ,R,N,V_fidelityPolicy"
- "TQ,R,N,V_fidelityPolicyMask"
- "TQ,R,N,V_filterContextTypeMask"
- "TQ,R,N,V_friendsCount"
- "TQ,R,N,V_geoTileKey"
- "TQ,R,N,V_hoursType"
- "TQ,R,N,V_limit"
- "TQ,R,N,V_locationOfInterestSource"
- "TQ,R,N,V_magnitude"
- "TQ,R,N,V_mapItemPlaceType"
- "TQ,R,N,V_monitoredScenarioTriggerTypes"
- "TQ,R,N,V_muid"
- "TQ,R,N,V_nearbyPoiCount"
- "TQ,R,N,V_observationInterval"
- "TQ,R,N,V_offset"
- "TQ,R,N,V_periodicReportInterval"
- "TQ,R,N,V_placeType"
- "TQ,R,N,V_routeTravelCountOnTravelDayOfWeekHourOfDay"
- "TQ,R,N,V_routeTraversalCount"
- "TQ,R,N,V_routeTraversalCountOnTravelDayOfWeek"
- "TQ,R,N,V_serviceLevel"
- "TQ,R,N,V_settledState"
- "TQ,R,N,V_sharingStatus"
- "TQ,R,N,V_singlePOIMuid"
- "TQ,R,N,V_sortIndex"
- "TQ,R,N,V_source"
- "TQ,R,N,V_sourceAccuracy"
- "TQ,R,N,V_spatialGranularity"
- "TQ,R,N,V_storageDuration"
- "TQ,R,N,V_totalCount"
- "TQ,R,N,V_type"
- "TQ,R,N,V_typeSource"
- "TQ,R,N,V_userType"
- "TQ,R,N,V_userTypeSource"
- "TQ,R,N,V_weekday"
- "TQ,R,N,V_workoutLocationType"
- "TS,N,V_minCountOfTraversal"
- "Td,N,V_avgBikeDistance"
- "Td,N,V_avgBikeTime"
- "Td,N,V_avgWalkDistance"
- "Td,N,V_avgWalkTime"
- "Td,N,V_endLatitude"
- "Td,N,V_endLongitude"
- "Td,N,V_frequencyScore"
- "Td,N,V_horizontalAccuracy"
- "Td,N,V_horizontalUncertainty"
- "Td,N,V_interArrivalTime"
- "Td,N,V_lastBucketFill"
- "Td,N,V_latitude"
- "Td,N,V_longitude"
- "Td,N,V_maximumError"
- "Td,N,V_recencyScore"
- "Td,N,V_runningMean"
- "Td,N,V_runningMeanOfSquares"
- "Td,N,V_significanceScore"
- "Td,N,V_smoothingErrorThreshold"
- "Td,N,V_startLatitude"
- "Td,N,V_startLongitude"
- "Td,N,V_wifiConfidence"
- "Td,R,N"
- "Td,R,N,V_age"
- "Td,R,N,V_altitude"
- "Td,R,N,V_averageSpeed"
- "Td,R,N,V_averageTripDistance"
- "Td,R,N,V_averageTripTime"
- "Td,R,N,V_confidence"
- "Td,R,N,V_confidenceInterval"
- "Td,R,N,V_course"
- "Td,R,N,V_densityScore"
- "Td,R,N,V_destinationLatitude"
- "Td,R,N,V_destinationLongitude"
- "Td,R,N,V_destinationVisitLatitude"
- "Td,R,N,V_destinationVisitLongitude"
- "Td,R,N,V_distance"
- "Td,R,N,V_elevation"
- "Td,R,N,V_elevationUncertainty"
- "Td,R,N,V_endTime"
- "Td,R,N,V_familiarityIndex"
- "Td,R,N,V_finerGranularityMapItemConfidence"
- "Td,R,N,V_forecastWindowTimeInterval"
- "Td,R,N,V_latitude"
- "Td,R,N,V_likelihood"
- "Td,R,N,V_locationOfInterestConfidence"
- "Td,R,N,V_longitude"
- "Td,R,N,V_lookbackInterval"
- "Td,R,N,V_maximumTripDistance"
- "Td,R,N,V_maximumTripTime"
- "Td,R,N,V_memoryFootprintEnd"
- "Td,R,N,V_memoryFootprintStart"
- "Td,R,N,V_minimumTripDistance"
- "Td,R,N,V_minimumTripTime"
- "Td,R,N,V_originLatitude"
- "Td,R,N,V_originLongitude"
- "Td,R,N,V_originVisitLatitude"
- "Td,R,N,V_originVisitLongitude"
- "Td,R,N,V_probability"
- "Td,R,N,V_scanDuration"
- "Td,R,N,V_size"
- "Td,R,N,V_socialScore"
- "Td,R,N,V_speed"
- "Td,R,N,V_startTime"
- "Td,R,N,V_timeInterval"
- "Td,R,N,V_tripDistance"
- "Td,R,N,V_tripDistanceUncertainty"
- "Td,R,N,V_uncertainty"
- "Td,R,N,V_verticalUncertainty"
- "Td,R,N,V_weight"
- "Td,R,V_endDistance"
- "Td,R,V_intervalLength"
- "Td,R,V_startDistance"
- "Tf,R,N,V_maxTravelTimeEstimateInSeconds"
- "Tf,R,N,V_maxTravelledDistanceEstimateInMeters"
- "Tf,R,N,V_meanTravelTimeEstimateInSeconds"
- "Tf,R,N,V_meanTravelledDistanceEstimateInMeters"
- "Tf,R,N,V_minTravelTimeEstimateInSeconds"
- "Tf,R,N,V_minTravelledDistanceEstimateInMeters"
- "Tf,R,N,V_travelTimeEstimateForEntireRouteInSeconds"
- "Tf,R,N,V_travelledDistanceEstimateForEntireRouteInMeters"
- "Ti,N,V_bikeTraversalCount"
- "Ti,N,V_tripSegmentSequence"
- "Ti,N,V_tripSegmentSequenceMax"
- "Ti,N,V_type"
- "Ti,N,V_walkTraversalCount"
- "Ti,R,N,V_countOfTraversal"
- "Ti,R,N,V_locationReferenceFrame"
- "Ti,R,N,V_referenceFrame"
- "Ti,R,N,V_routeFetchType"
- "Ti,R,N,V_routeOriginType"
- "Tq,N,V_modeOfTransportation"
- "Tq,N,V_preferredDownsamplingLevel"
- "Tq,N,V_wifiFingerprintLabelType"
- "Tq,R,N,V_channel"
- "Tq,R,N,V_dataPointCount"
- "Tq,R,N,V_errorCode"
- "Tq,R,N,V_estimationStatus"
- "Tq,R,N,V_geoFormOfWay"
- "Tq,R,N,V_geoRoadClass"
- "Tq,R,N,V_inferenceTriggerReason"
- "Tq,R,N,V_limit"
- "Tq,R,N,V_locationType"
- "Tq,R,N,V_modeOfTransport"
- "Tq,R,N,V_modeOfTransportation"
- "Tq,R,N,V_relationship"
- "Tq,R,N,V_resultProviderID"
- "Tq,R,N,V_routeTravelMode"
- "Tq,R,N,V_rssi"
- "Tq,R,N,V_source"
- "Tq,R,N,V_subPremiseType"
- "Tq,R,N,V_transportMode"
- "Tq,R,N,V_type"
- "Tq,R,N,V_workoutActivityType"
- "Tq,R,V_eStatus"
- "Ts,N,V_clusterOrder"
- "UTF8String"
- "UUIDString"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "__scenarioTriggerHandlers"
- "_accessPoints"
- "_actionRegistrant"
- "_address"
- "_addressIdentifier"
- "_administrativeArea"
- "_administrativeAreaCode"
- "_advertisingCapability"
- "_age"
- "_allDay"
- "_allRoutesCountForThisODPair"
- "_allTraversalCountBetweenThisODPair"
- "_altitude"
- "_analytics"
- "_analyticsIdentifier"
- "_aoiConfidences"
- "_apToModelMapping"
- "_applePaySupport"
- "_areasOfInterest"
- "_ascending"
- "_averageSpeed"
- "_averageTripDistance"
- "_averageTripTime"
- "_avgBikeDistance"
- "_avgBikeTime"
- "_avgWalkDistance"
- "_avgWalkTime"
- "_batchSize"
- "_bikeTraversalCount"
- "_bluetoothAddress"
- "_boundingBoxLocation"
- "_bundleIdentifier"
- "_bundlePath"
- "_businessHours"
- "_capacity"
- "_category"
- "_categoryDenyList"
- "_categoryMUID"
- "_centroid"
- "_channel"
- "_clientCallback"
- "_clientCount"
- "_clientIdentifier"
- "_clientThrottle"
- "_clusterID"
- "_clusterOrder"
- "_combinedFrequencyScores"
- "_combinedRecencyScores"
- "_combinedSignificanceScores"
- "_commuteID"
- "_confidence"
- "_confidenceInterval"
- "_configuration"
- "_configurationIdentifier"
- "_confirmed"
- "_consumeTokens:"
- "_contactID"
- "_contexts"
- "_coreroutineBundle"
- "_coreroutine_LocalizedStringForKey:"
- "_countOfTraversal"
- "_country"
- "_countryCode"
- "_course"
- "_createConnection"
- "_creationDate"
- "_curatedLabel"
- "_customLabel"
- "_dailyHours"
- "_dataPointCount"
- "_date"
- "_dateInterval"
- "_dateOfMostRecentTrip"
- "_decodeGeoAddressObjectFromData:decompress:"
- "_densityCallbackConfiguration"
- "_densityHandler"
- "_densityScore"
- "_densityUpdateHandler"
- "_destinationLatitude"
- "_destinationLongitude"
- "_destinationVisit"
- "_destinationVisitLatitude"
- "_destinationVisitLongitude"
- "_displayLanguage"
- "_disputed"
- "_distance"
- "_distanceInterval"
- "_distanceToNearestAOILowerBound"
- "_downloadError"
- "_downloadKey"
- "_downsampleLocations:errorFunction:errorThreshold:"
- "_downsampleLocations:errorFunction:outputSize:"
- "_downsampleRequired"
- "_eStatus"
- "_elevation"
- "_elevationUncertainty"
- "_enableFallbackModel"
- "_encodeGeoAddressObject:compress:"
- "_endDate"
- "_endDistance"
- "_endLatitude"
- "_endLocation"
- "_endLocationName"
- "_endLongitude"
- "_endTime"
- "_entry"
- "_entryDate"
- "_enumerateElevationsWithOptions:reply:"
- "_enumerateStoredLocationsWithOptions:usingBlock:"
- "_errorCode"
- "_estimationStatus"
- "_eventAgentHelper"
- "_eventID"
- "_eventIdentifier"
- "_exit"
- "_exitDate"
- "_expectedVisits"
- "_expirationDate"
- "_extendedAttributes"
- "_familiarityIndex"
- "_familyCount"
- "_featureToHashedApMapping"
- "_featureToHashedApMappingDataURL"
- "_fetchAllRouteLocations"
- "_fetchFormOfWay"
- "_fetchLocationType"
- "_fetchPreferredNames"
- "_fetchRoadClass"
- "_fidelityPolicy"
- "_fidelityPolicyMask"
- "_fillRate"
- "_filterContextTypeMask"
- "_filterLocations"
- "_filterPairedVisitEntries"
- "_filtered"
- "_finerGranularityMapItem"
- "_finerGranularityMapItemConfidence"
- "_firstObject"
- "_followedByUTurn"
- "_forecastWindowDateInterval"
- "_forecastWindowTimeInterval"
- "_formOfWay"
- "_frequencyCount"
- "_frequencyScore"
- "_friendsCount"
- "_fullConfirmationList"
- "_fullyCoversTile"
- "_generatedTripSegmentRegistrant"
- "_geoAddressData"
- "_geoCacheInfo"
- "_geoFormOfWay"
- "_geoMapItemHandle"
- "_geoMapItemIdentifier"
- "_geoRoadClass"
- "_geoTileKey"
- "_hashSalt"
- "_hashedApToModelMapping"
- "_hashedApToModelMappingDataURL"
- "_horizontalAccuracy"
- "_horizontalUncertainty"
- "_hoursType"
- "_identifier"
- "_inferenceTriggerReason"
- "_inlandWater"
- "_interArrivalTime"
- "_intervalLength"
- "_isConsumedByClustering"
- "_isHome"
- "_isIsland"
- "_isLocked"
- "_isMe"
- "_isValidClusterOrder:"
- "_isValidRouteODLocation:routeDestinationLocation:routeFetchType:"
- "_isWork"
- "_iso3166CountryCode"
- "_iso3166SubdivisionCode"
- "_labelVisit"
- "_lastArrivalTime"
- "_lastBucketFill"
- "_lastTravelledDate"
- "_latitude"
- "_launchTaskWithSelector:remainingAttempts:proxyErrorHandler:taskBlock:"
- "_learnedRouteEndLocation"
- "_learnedRouteEndLocationWithReferenceFrame"
- "_learnedRouteIdentifier"
- "_learnedRouteLocations"
- "_learnedRouteMetrics"
- "_learnedRouteStartLocation"
- "_learnedRouteStartLocationWithReferenceFrame"
- "_leechedLowConfidenceVisitHandler"
- "_leechedVisitHandler"
- "_left"
- "_likelihood"
- "_limit"
- "_localGeoAddressObject"
- "_locality"
- "_location"
- "_locationFinalized"
- "_locationOfInterest"
- "_locationOfInterestConfidence"
- "_locationOfInterestSource"
- "_locationQuality"
- "_locationReferenceFrame"
- "_locationType"
- "_locations"
- "_loiIdentifier"
- "_loiIsMissingFromCurrentVisitHistory"
- "_longitude"
- "_lookbackInterval"
- "_mac"
- "_machContinuousTimeSec"
- "_magnitude"
- "_mapItem"
- "_mapItemPlaceType"
- "_maxTravelTimeEstimateInSeconds"
- "_maxTravelledDistanceEstimateInMeters"
- "_maximumError"
- "_maximumErrorIndex"
- "_maximumNumberOfItems"
- "_maximumTripDistance"
- "_maximumTripTime"
- "_meanTravelTimeEstimateInSeconds"
- "_meanTravelledDistanceEstimateInMeters"
- "_memoryFootprintEnd"
- "_memoryFootprintStart"
- "_mergedThoroughfareWithSubPremises:subThoroughfare:thoroughfare:"
- "_minCountOfTraversal"
- "_minTravelTimeEstimateInSeconds"
- "_minTravelledDistanceEstimateInMeters"
- "_minimumTripDistance"
- "_minimumTripTime"
- "_modeOfTransport"
- "_modeOfTransportation"
- "_modelCalibrationParameters"
- "_modelURLs"
- "_models"
- "_monitoredScenarioTriggerTypes"
- "_mostConfidentAOI"
- "_mostConfidentPOI"
- "_muid"
- "_name"
- "_navigationWasInterrupted"
- "_nearbyLocationOfInterest"
- "_nearbyPoiCount"
- "_nextEntryTime"
- "_notes"
- "_numberOfSeconds"
- "_observationInterval"
- "_ocean"
- "_offset"
- "_operationCost"
- "_operationsAllowed"
- "_options"
- "_optionsMask"
- "_originLatitude"
- "_originLongitude"
- "_originVisit"
- "_originVisitLatitude"
- "_originVisitLongitude"
- "_originalLabel"
- "_parkDate"
- "_participationOptional"
- "_peopleDiscoveryErrorHandler"
- "_peopleDiscoveryRegistrant"
- "_periodicReportInterval"
- "_photo"
- "_placeInference"
- "_placeInferenceOptions"
- "_placeInferencesHandler"
- "_placeType"
- "_poiConfidences"
- "_pointsOfInterest"
- "_polygon"
- "_postalCode"
- "_predictedContextHandler"
- "_predictedContextOptions"
- "_predictedContextResult"
- "_predictedContextTransports"
- "_predictedContexts"
- "_predictionSources"
- "_preferredDownsamplingLevel"
- "_preferredName"
- "_primary"
- "_probability"
- "_proxyForServicingSelector:asynchronous:withErrorHandler:"
- "_proxyForServicingSelector:withErrorHandler:"
- "_queryTime"
- "_queue"
- "_recencyScore"
- "_redact"
- "_referenceFrame"
- "_referenceLocation"
- "_referenceLocationSummary"
- "_registered"
- "_relationship"
- "_remoteStatusHandler"
- "_replenishTokens"
- "_requestEndDate"
- "_requestStartDate"
- "_restorationIdentifier"
- "_resultProviderID"
- "_resultSortDescriptors"
- "_resultSortProbabilityAscending"
- "_resultSortStartDateAscending"
- "_right"
- "_roadClass"
- "_rolledLOIResult"
- "_routeDate"
- "_routeFetchType"
- "_routeLocations"
- "_routeOriginType"
- "_routeTravelCountOnTravelDayOfWeekHourOfDay"
- "_routeTravelMode"
- "_routeTraversalCount"
- "_routeTraversalCountOnTravelDayOfWeek"
- "_routineManager"
- "_rssi"
- "_rssiHistogram"
- "_runningMean"
- "_runningMeanOfSquares"
- "_scanDuration"
- "_scenarioTriggerRegistrant"
- "_secondObject"
- "_serviceLevel"
- "_setQueue:"
- "_settledState"
- "_sharingStatus"
- "_significanceScore"
- "_singlePOIMuid"
- "_size"
- "_smoothingErrorThreshold"
- "_smoothingRequired"
- "_socialScore"
- "_sortIndex"
- "_source"
- "_sourceAccuracy"
- "_sourceBundleIdentifier"
- "_sourceFilter"
- "_sourceIdentifier"
- "_sources"
- "_spatialGranularity"
- "_speed"
- "_start"
- "_startDate"
- "_startDistance"
- "_startLatitude"
- "_startLocation"
- "_startLocationName"
- "_startLongitude"
- "_startTime"
- "_stopDate"
- "_storageDuration"
- "_subAdministrativeArea"
- "_subLocality"
- "_subPremise"
- "_subPremiseType"
- "_subPremises"
- "_subThoroughfare"
- "_submissionDate"
- "_submissionDateInterval"
- "_suggestionInfo_opaqueKey"
- "_suggestionsSchemaOrg"
- "_targetUserSession"
- "_tentative"
- "_thoroughfare"
- "_tileCacheInfo"
- "_tileURL"
- "_timeInterval"
- "_timeIntervals"
- "_title"
- "_tokenBucket"
- "_totalCount"
- "_totalInterArrivalTime"
- "_totalOperations"
- "_totalTokensConsumed"
- "_totalTokensGenerated"
- "_transportMode"
- "_travelModeRoutes"
- "_travelTimeEstimateForEntireRouteInSeconds"
- "_travelledDistanceEstimateForEntireRouteInMeters"
- "_tripCommuteID"
- "_tripDistance"
- "_tripDistanceUncertainty"
- "_tripSegmentSequence"
- "_tripSegmentSequenceMax"
- "_type"
- "_typeSource"
- "_uncertainty"
- "_url"
- "_usageDate"
- "_useBackground"
- "_useBackgroundTraits"
- "_userSetLocation"
- "_userType"
- "_userTypeSource"
- "_usualLocation"
- "_uuid"
- "_vehicleEvent"
- "_vehicleEventsHandler"
- "_vehicleIdentifier"
- "_vehicleModelName"
- "_vehicleName"
- "_verticalUncertainty"
- "_vertices"
- "_visitDateInterval"
- "_visitEntryDate"
- "_visitExitDate"
- "_visitHandler"
- "_visitIdentifier"
- "_visitIdentifierDestination"
- "_visitIdentifierOrigin"
- "_visits"
- "_walkTraversalCount"
- "_wastedTokens"
- "_weekday"
- "_weight"
- "_wifiConfidence"
- "_wifiFingerprintLabelType"
- "_workoutActivityType"
- "_workoutLocationType"
- "_workoutUUID"
- "_wrappedVisit"
- "_xpcConnection"
- "_xpcQueue"
- "_zdrConfirmationList"
- "abbreviatedDescription"
- "actionRegistrant"
- "addBackgroundInertialOdometrySamples:handler:"
- "addBackgroundInertialOdometrySamples:reply:"
- "addElevations:handler:"
- "addLocationOfInterestOfType:mapItem:customLabel:handler:"
- "addLocationOfInterestOfType:mapItemStorage:customLabel:reply:"
- "addObject:"
- "addObjectsFromArray:"
- "addressDictionary"
- "advertisingCapability"
- "aggregateAdvertisingCapability:with:"
- "aggregateObservationInterval:with:"
- "aggregateServiceLevel:with:"
- "aggregateStorageDuration:with:"
- "allKeys"
- "allLocations"
- "allObjects"
- "allValues"
- "allocWithZone:"
- "allowedClasses"
- "allowsKeyedCoding"
- "appendFormat:"
- "appendSource:"
- "appendString:"
- "areaOfInterests"
- "array"
- "arrayWithArray:"
- "arrayWithCapacity:"
- "arrayWithObject:"
- "arrayWithObjects:count:"
- "autorelease"
- "autoupdatingCurrentLocale"
- "averageTripDistance"
- "averageTripTime"
- "batchSize,%lu,startLat,%.7f,startLon,%.7f,endLat,%.7f,endLon,%.7f,minCntTraversal,%d"
- "betweenDate:andDate:"
- "bluetoothAddress"
- "boolValue"
- "bundleForClass:"
- "callStackSymbols"
- "characterSetWithCharactersInString:"
- "class"
- "clearAllVehicleEvents"
- "clearAllVehicleEvents:"
- "clearAllVehicleEventsWithHandler:"
- "clearAllVehicleEventsWithReply:"
- "clearMask"
- "clearRoutineWithHandler:"
- "clearRoutineWithReply:"
- "clientCallback"
- "clientLocation"
- "clientThrottle"
- "code"
- "com.apple.%@"
- "combinedFrequencyScores"
- "combinedRecencyScores"
- "combinedSignificanceScores"
- "compare:"
- "component:fromDate:"
- "components:fromDate:"
- "componentsJoinedByString:"
- "componentsSeparatedByCharactersInSet:"
- "compressedDataUsingAlgorithm:error:"
- "configuration"
- "configurationIdentifier"
- "conformsToProtocol:"
- "consolidatedConfidenceFromConfidences:"
- "consolidatedSourceFromInferredMapItems:"
- "contactID"
- "contextTypeMaskForContext:"
- "convertContactFrequencyToString:"
- "convertContactRecencyToString:"
- "convertContactSignificanceToString:"
- "convertPersonRelationshipToString:"
- "coordinate"
- "coordinateToString"
- "copy"
- "copyWithZone:"
- "correctLabelForCurrentPlace:date:newLabel:handler:"
- "correctLabelForVisitWithIdentifier:entryDate:originalLabel:newLabel:handler:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "countOfOperationsAllowed"
- "countOfOperationsAllowedWithCost:"
- "countOfTraversal"
- "createConnection"
- "createErrorFunctionWithAbsoluteCrosstrackDistance"
- "createErrorFunctionWithPerpendicularDistance"
- "createErrorFunctionWithPerpendicularDistanceAndSpeed"
- "currentCalendar"
- "currentPredictedContextsWithType:"
- "d"
- "d16@0:8"
- "d24@0:8@16"
- "d24@0:8@?16"
- "d24@0:8Q16"
- "d24@0:8d16"
- "dataRepresentation"
- "dataWithBytes:length:"
- "dataWithJSONObject:options:error:"
- "dateBisectingDate1:date2:"
- "dateByAddingComponents:toDate:options:"
- "dateByAddingTimeInterval:"
- "dateByAddingUnit:value:"
- "dateByAddingUnit:value:toDate:options:"
- "dateByRoundingWithTimeQuantization:"
- "dateFormatter"
- "dateFormatterForLogging"
- "dateFromComponents:"
- "dateIntervalFromStart:end:"
- "dateOfMostRecentTrip"
- "dateReducedToResolution:"
- "dateReducedToResolution:calendar:"
- "dateWithHour:minute:second:"
- "dateWithResolution:"
- "dateWithResolution:calendar:"
- "dateWithTimeInterval:sinceDate:"
- "dateWithTimeIntervalSince1970:"
- "dateWithTimeIntervalSinceNow:"
- "dateWithTimeIntervalSinceReferenceDate:"
- "day"
- "dealloc"
- "debugDescription"
- "decodeBoolForKey:"
- "decodeDictionaryWithKeysOfClass:objectsOfClass:forKey:"
- "decodeDoubleForKey:"
- "decodeFloatForKey:"
- "decodeInt32ForKey:"
- "decodeInt64ForKey:"
- "decodeIntForKey:"
- "decodeIntegerForKey:"
- "decodeObjectForKey:"
- "decodeObjectOfClass:forKey:"
- "decodeObjectOfClasses:forKey:"
- "decompressedDataUsingAlgorithm:error:"
- "dedupeInferredMapItems:"
- "defaultManager"
- "deleteCharactersInRange:"
- "deleteTripSegmentWithUUID:handler:"
- "deleteTripSegmentWithUUID:reply:"
- "densityCallbackConfiguration"
- "densityScore"
- "densityUpdateHandler"
- "deriveConfidenceFromRouteMetric:"
- "descriptionDictionary"
- "destinationVisitLatitude"
- "destinationVisitLongitude"
- "dictionary"
- "dictionaryWithCapacity:"
- "dictionaryWithContentsOfFile:"
- "dictionaryWithObjects:forKeys:count:"
- "distanceFromLocation:"
- "distantFuture"
- "distantPast"
- "domain"
- "doubleValue"
- "downsampleLocations:errorFunction:errorThreshold:outputSize:"
- "downsampleLocations:outputSize:"
- "dumpStatistics"
- "eStatus"
- "earlierDate:"
- "encodeBool:forKey:"
- "encodeDouble:forKey:"
- "encodeFloat:forKey:"
- "encodeInt32:forKey:"
- "encodeInt64:forKey:"
- "encodeInt:forKey:"
- "encodeInteger:forKey:"
- "encodeObject:forKey:"
- "encodeWithCoder:"
- "encodedData"
- "endOfDay"
- "engageInVehicleEventWithIdentifier:"
- "engageInVehicleEventWithIdentifier:reply:"
- "enumerateElevationsWithOptions:reply:"
- "enumerateKeysAndObjectsUsingBlock:"
- "enumerateObjectsUsingBlock:"
- "enumerateObjectsWithOptions:usingBlock:"
- "enumerateStoredLocationsWithOptions:usingBlock:"
- "enumeratedType"
- "errorWithDomain:code:userInfo:"
- "evaluateLocationsWithErrorFunction:"
- "eventAgentHelper"
- "eventID"
- "exceptionWithName:reason:userInfo:"
- "exchangeObjectAtIndex:withObjectAtIndex:"
- "exportedInterface"
- "extendLifetimeOfVisitWithIdentifier:handler:"
- "extendLifetimeOfVisitsWithIdentifiers:handler:"
- "extendLifetimeOfVisitsWithIdentifiers:reply:"
- "extendedAttributes"
- "f"
- "f16@0:8"
- "familyCount"
- "fetchAllLocationsOfInterestForSettingsWithHandler:"
- "fetchAllLocationsOfInterestForSettingsWithReply:"
- "fetchAllRouteLocations"
- "fetchAuthorizedLocationStatus:"
- "fetchAutomaticVehicleEventDetectionSupportedWithHandler:"
- "fetchAutomaticVehicleEventDetectionSupportedWithReply:"
- "fetchBackgroundInertialOdometrySamplesWithOptions:handler:"
- "fetchBackgroundInertialOdometrySamplesWithOptions:reply:"
- "fetchCloudSyncAuthorizationState:"
- "fetchCloudSyncAuthorizationStateWithReply:"
- "fetchContactScoresFromContactIDs:completionHandler:"
- "fetchCurrentPeopleDensity:"
- "fetchCurrentPredictedLocationsOfInterestLookingBack:lookingAhead:handler:"
- "fetchCurrentPredictedLocationsOfInterestLookingBack:lookingAhead:reply:"
- "fetchDedupedLocationOfInterestIdentifiersWithIdentifier:handler:"
- "fetchDedupedLocationOfInterestIdentifiersWithIdentifier:reply:"
- "fetchElevationsWithContext:reply:"
- "fetchElevationsWithOptions:reply:"
- "fetchEnumerableObjectsWithOptions:offset:reply:"
- "fetchEstimatedLocationAtDate:handler:"
- "fetchEstimatedLocationAtDate:options:handler:"
- "fetchEstimatedLocationAtDate:options:reply:"
- "fetchFamiliarityIndexResultsWithOptions:handler:"
- "fetchFamiliarityIndexResultsWithOptions:reply:"
- "fetchFinerGranularityInferredMapItemWithVisitIdentifier:handler:"
- "fetchFinerGranularityInferredMapItemWithVisitIdentifier:reply:"
- "fetchFormattedPostalAddressesFromMeCard:"
- "fetchLastVehicleEventsWithHandler:"
- "fetchLastVehicleEventsWithReply:"
- "fetchLearnedRoutesWithOptions:handler:"
- "fetchLearnedRoutesWithOptions:reply:"
- "fetchLocationOfInterestAtLocation:reply:"
- "fetchLocationOfInterestAtLocation:withHandler:"
- "fetchLocationOfInterestForRegion:reply:"
- "fetchLocationOfInterestForRegion:withHandler:"
- "fetchLocationOfInterestWithIdentifier:reply:"
- "fetchLocationOfInterestWithIdentifier:withHandler:"
- "fetchLocationsCountForTripSegmentWithOptions:handler:"
- "fetchLocationsCountForTripSegmentWithOptions:reply:"
- "fetchLocationsForTripSegmentWithOptions:handler:"
- "fetchLocationsForTripSegmentWithOptions:reply:"
- "fetchLocationsOfInterestAssociatedToIdentifier:reply:"
- "fetchLocationsOfInterestAssociatedToIdentifier:withHandler:"
- "fetchLocationsOfInterestOfType:reply:"
- "fetchLocationsOfInterestOfType:withHandler:"
- "fetchLocationsOfInterestVisitedBetweenStartDate:endDate:reply:"
- "fetchLocationsOfInterestVisitedBetweenStartDate:endDate:withHandler:"
- "fetchLocationsOfInterestVisitedSinceDate:withHandler:"
- "fetchLocationsOfInterestWithinDistance:ofLocation:reply:"
- "fetchLocationsOfInterestWithinDistance:ofLocation:withHandler:"
- "fetchLookbackWindowStartDateWithHandler:"
- "fetchLookbackWindowStartDateWithLocation:handler:"
- "fetchLookbackWindowStartDateWithLocation:reply:"
- "fetchMonitoredScenarioTriggerTypesWithHandler:"
- "fetchMonitoredScenarioTriggerTypesWithReply:"
- "fetchNextPredictedLocationsOfInterestFromLocation:startDate:timeInterval:reply:"
- "fetchNextPredictedLocationsOfInterestFromLocation:startDate:timeInterval:withHandler:"
- "fetchNextPredictedLocationsOfInterestWithHandler:"
- "fetchOngoingPeopleDensity:"
- "fetchPathToDiagnosticFilesWithOptions:handler:"
- "fetchPathToDiagnosticFilesWithOptions:reply:"
- "fetchPeopleCountEventsHistory:completionHandler:"
- "fetchPeopleDensityHistoryFromStartDate:endDate:completionHandler:"
- "fetchPlaceInferencesWithOptions:handler:"
- "fetchPlaceInferencesWithOptions:reply:"
- "fetchPredictedContextWithOptions:completionHandler:"
- "fetchPredictedContextWithOptions:reply:"
- "fetchPredictedExitDatesFromLocation:onDate:reply:"
- "fetchPredictedExitDatesFromLocation:onDate:withHandler:"
- "fetchPredictedLocationsOfInterestAssociatedToTitle:location:calendarIdentifier:reply:"
- "fetchPredictedLocationsOfInterestAssociatedToTitle:location:calendarIdentifier:withHandler:"
- "fetchPredictedLocationsOfInterestBetweenStartDate:endDate:reply:"
- "fetchPredictedLocationsOfInterestBetweenStartDate:endDate:withHandler:"
- "fetchPredictedLocationsOfInterestOnDate:reply:"
- "fetchPredictedLocationsOfInterestOnDate:withHandler:"
- "fetchProximityHistoryFromEventIDs:completionHandler:"
- "fetchProximityHistoryFromStartDate:endDate:completionHandler:"
- "fetchRemoteStatusWithHandler:"
- "fetchRemoteStatusWithReply:"
- "fetchRoutineEnabledWithHandler:"
- "fetchRoutineEnabledWithReply:"
- "fetchRoutineModeFromLocation:reply:"
- "fetchRoutineModeFromLocation:withHandler:"
- "fetchRoutineStateWithHandler:"
- "fetchStoredLocationsWithContext:reply:"
- "fetchStoredVisitsWithOptions:handler:"
- "fetchStoredVisitsWithOptions:reply:"
- "fetchTransitionsBetweenStartDate:endDate:handler:"
- "fetchTransitionsBetweenStartDate:endDate:reply:"
- "fetchTripClusterMetadataWithOptions:handler:"
- "fetchTripClusterMetadataWithOptions:reply:"
- "fetchTripSegmentMetadataWithOptions:handler:"
- "fetchTripSegmentMetadataWithOptions:reply:"
- "fetchTripSegmentsWithOptions:handler:"
- "fetchTripSegmentsWithOptions:reply:"
- "fetchVehiclesWithOptions:handler:"
- "fetchVehiclesWithOptions:reply:"
- "fidelityPolicy"
- "fidelityPolicy, %@, locations count, %lu, last location, %@, accessPoints count, %lu, last accessPoint, %@, location, %@, distance, %f, startDate, %@, endDate, %@, limit, %ld, useBackground, %@, clientIdentifier, %@"
- "fidelityPolicyMaskToString:"
- "fileExistsAtPath:"
- "filterConvergingLocations:"
- "filteredArrayUsingPredicate:"
- "fingerprintLabelTypeToString:"
- "finishDecoding"
- "finishEncoding"
- "flatten"
- "frequencyCount"
- "frequencyScore"
- "friendsCount"
- "fullAddressWithMultiline:"
- "fullConfirmationList"
- "fullThoroughfare"
- "generateSequencesFromDate:toDate:"
- "generatedTripSegmentRegistrant"
- "geoAddressObject"
- "geoDictionaryRepresentation"
- "geoMapItemSource"
- "geoMapItemSourceToString:"
- "getClusterClassOfObject:"
- "getEarliestDate:"
- "getFormattedDateString"
- "getUUIDBytes:"
- "getVisitsFromVisitsDescriptionData:"
- "handleDaemonStart"
- "hangDuration"
- "hangType"
- "hasKnownTypeItem:"
- "hasMask:"
- "hash"
- "heaviestMapItemFrom:closestToLocation:distanceCalculator:error:"
- "hintSourceToString:"
- "hour"
- "hungObject"
- "hungQueue"
- "i16@0:8"
- "identifier, %@, date, %@, geoTileKey, %@, downloadKey, %@, geoCacheInfo, %@, size, %.1f kB, hashSalt, %@, apToModelMapping count, %lu, hashedApToModelMapping count, %lu, hashedApToModelMappingDataURL, %@, singlePOIMuid, %@, models, %@, model URLs, %@, modelCalibrationParameters, %@, pointsOfInterest, %@"
- "identifier, %@, geoMapItemIdentifier, %@ (%@), name, \"%@\", category, %@, categoryMUID, %@, businessHours, %@, address, %@, location, %@, source, %@, map item place type, %@, muid, %lu, result provider ID: %ld, weight, %lf, creationDate, %@, extended attributes, %@, display language, %@, disputed, %@"
- "identifier, %@, muid, %lu, location, %@, applyPaySupport, %@, filtered, %@, fullyCoversTile, %@"
- "indexOfObjectPassingTest:"
- "inferenceTriggerReasonToString"
- "init"
- "initForReadingFromData:error:"
- "initRequiringSecureCoding:"
- "initWithAddressIdentifier:isMe:wifiConfidence:wifiFingerprintLabelType:"
- "initWithAdvertisingCapability:serviceLevel:observationInterval:storageDuration:densityCallbackConfiguration:"
- "initWithAggregation:"
- "initWithAllRoutesCountForThisODPair:allTraversalCountBetweenThisODPair:routeTraversalCount:routeTraversalCountOnTravelDayOfWeek:routeTravelCountOnTravelDayOfWeekHourOfDay:lastTravelledDate:"
- "initWithApplePaySupport:category:muid:nearbyPoiCount:"
- "initWithAscending:batchSize:dateInterval:wrappedVisit:"
- "initWithAscending:confidence:dateInterval:labelVisit:limit:"
- "initWithAscending:confidence:dateInterval:labelVisit:limit:sources:"
- "initWithAscending:confidence:dateInterval:labelVisit:limit:sources:redact:"
- "initWithAscending:confidence:dateInterval:labelVisit:limit:sources:redact:filterPairedVisitEntries:"
- "initWithAscending:confidence:dateInterval:limit:"
- "initWithAscending:dateInterval:limit:"
- "initWithAscending:limit:"
- "initWithAscending:sortIndex:limit:"
- "initWithAscending:sortIndex:submissionDateInterval:visitDateInterval:limit:"
- "initWithAscending:submissionDateInterval:limit:"
- "initWithAscending:visitDateInterval:limit:"
- "initWithAverageSpeed:enableFallbackModel:timeInterval:"
- "initWithBundleIdentifier:bundlePath:routeOriginLocation:routeDestinationLocation:routeDate:routeFetchType:fetchAllRouteLocations:routeOriginType:"
- "initWithBundleIdentifier:routeOriginLocation:routeDestinationLocation:routeDate:routeFetchType:fetchAllRouteLocations:routeOriginType:"
- "initWithBundlePath:routeOriginLocation:routeDestinationLocation:routeDate:routeFetchType:fetchAllRouteLocations:routeOriginType:"
- "initWithBundleUUID:startDate:endDate:densityScore:scanDuration:rssiHistogram:"
- "initWithCString:encoding:"
- "initWithCentroid:vertices:"
- "initWithClientLocation:"
- "initWithClusterID:"
- "initWithCoder:"
- "initWithConfigurationIdentifier:"
- "initWithContactAddressDictionary:language:country:phoneticLocale:"
- "initWithContactID:frequencyScore:recencyScore:significanceScore:frequencyCount:runningMean:runningMeanOfSquares:"
- "initWithCreationDate:forecastWindowDateInterval:forecastWindowTimeInterval:filterContextTypeMask:filterLocations:resultSortDescriptors:"
- "initWithCurrentLocaleFullThoroughfare:subLocality:locality:subAdministrativeArea:administrativeArea:postalCode:country:countryCode:"
- "initWithData:encoding:"
- "initWithDate:"
- "initWithDate:confidenceInterval:"
- "initWithDate:location:vehicleIdentifier:userSetLocation:notes:identifier:photo:mapItem:confirmed:"
- "initWithDate:machContinuousTimeSec:numberOfSeconds:"
- "initWithDate:type:location:entry:exit:dataPointCount:confidence:placeInference:"
- "initWithDate:type:location:entry:exit:dataPointCount:confidence:placeInference:source:"
- "initWithDate:type:location:entry:exit:dataPointCount:confidence:placeInference:source:identifier:"
- "initWithDate:uncertainty:confidence:"
- "initWithDateInterval:"
- "initWithDateInterval:batchSize:"
- "initWithDateInterval:distanceInterval:geoFormOfWay:"
- "initWithDateInterval:distanceInterval:geoRoadClass:"
- "initWithDateInterval:distanceInterval:locationType:"
- "initWithDateInterval:familiarityIndex:"
- "initWithDateInterval:fetchRoadClass:fetchFormOfWay:fetchLocationType:fetchPreferredNames:"
- "initWithDateInterval:horizontalAccuracy:batchSize:"
- "initWithDateInterval:horizontalAccuracy:batchSize:ascending:"
- "initWithDateInterval:horizontalAccuracy:batchSize:boundingBoxLocation:"
- "initWithDateInterval:horizontalAccuracy:batchSize:boundingBoxLocation:type:"
- "initWithDateInterval:horizontalAccuracy:batchSize:boundingBoxLocation:type:downsampleRequired:"
- "initWithDateInterval:horizontalAccuracy:batchSize:boundingBoxLocation:type:downsampleRequired:smoothingErrorThreshold:"
- "initWithDateInterval:horizontalAccuracy:batchSize:boundingBoxLocation:type:smoothingRequired:downsampleRequired:smoothingErrorThreshold:ascending:"
- "initWithDateInterval:limit:"
- "initWithDateInterval:lookbackInterval:spatialGranularity:referenceLocation:referenceLocationSummary:distance:"
- "initWithDateInterval:predictionSources:probability:sourceBundleIdentifier:workoutActivityType:workoutLocationType:"
- "initWithDateInterval:preferredDownsamplingLevel:"
- "initWithDateInterval:preferredDownsamplingLevel:batchSize:"
- "initWithDateInterval:preferredDownsamplingLevel:batchSize:boundingBoxLocation:"
- "initWithDateInterval:preferredDownsamplingLevel:boundingBoxLocation:batchSize:offset:"
- "initWithDateInterval:settledState:"
- "initWithDateInterval:spatialGranularity:"
- "initWithDateInterval:vehicleName:vehicleModelName:bluetoothAddress:"
- "initWithDictionary:"
- "initWithDomain:code:userInfo:"
- "initWithDownloadKey:tileURL:tileCacheInfo:downloadError:"
- "initWithElevation:dateInterval:"
- "initWithElevation:dateInterval:elevationUncertainty:estimationStatus:"
- "initWithEndVisitLatitude:endLongitude:"
- "initWithEnumerationOptions:"
- "initWithEnumerationOptions:offset:"
- "initWithEventID:startDate:endDate:relationship:socialScore:combinedFrequencyScores:combinedRecencyScores:combinedSignificanceScores:"
- "initWithEventID:startDate:endDate:totalCount:familyCount:friendsCount:"
- "initWithEventIdentifier:startDate:endDate:title:location:allDay:sharingStatus:"
- "initWithEventIdentifier:startDate:endDate:title:location:allDay:sharingStatus:suggestionInfo_opaqueKey:"
- "initWithEventIdentifier:startDate:endDate:title:location:allDay:sharingStatus:tentative:participationOptional:suggestionInfo_opaqueKey:suggestionsSchemaOrg:"
- "initWithExtendedAttributesMO:"
- "initWithFidelityPolicy:locations:accessPoints:"
- "initWithFidelityPolicy:locations:accessPoints:clientIdentifier:"
- "initWithFidelityPolicy:locations:accessPoints:distance:location:startDate:endDate:limit:useBackground:clientIdentifier:"
- "initWithFillRate:capacity:"
- "initWithFillRate:capacity:initialAllocation:"
- "initWithFirstJSONDictionary:"
- "initWithFirstObject:secondObject:"
- "initWithForecastWindowDateInterval:filterContextTypeMask:filterLocations:resultSortDescriptors:"
- "initWithForecastWindowDateInterval:filterContextTypeMask:filterLocations:resultSortStartDateAscending:resultSortProbabilityAscending:"
- "initWithForecastWindowTimeInterval:filterContextTypeMask:filterLocations:resultSortDescriptors:"
- "initWithFormat:"
- "initWithFormat:arguments:"
- "initWithFullThoroughfare:subLocality:locality:subAdministrativeArea:administrativeArea:postalCode:country:countryCode:language:countryLocale:phoneticLocale:"
- "initWithGeoDictionary:language:country:phoneticLocale:"
- "initWithHoursType:dailyHours:"
- "initWithIdentifier:"
- "initWithIdentifier:addressIdentifier:isMe:wifiConfidence:wifiFingerprintLabelType:"
- "initWithIdentifier:apToModelMapping:date:downloadKey:geoCacheInfo:geoTileKey:hashedApToModelMapping:hashedApToModelMappingDataURL:hashSalt:modelCalibrationParameters:models:modelURLs:pointsOfInterest:singlePOIMuid:size:"
- "initWithIdentifier:applePaySupport:filtered:fullyCoversTile:location:muid:polygon:"
- "initWithIdentifier:categoryDenyList:geoCacheInfo:modelCalibrationParameters:"
- "initWithIdentifier:date:errorCode:fidelityPolicyMask:placeInference:sourceIdentifier:"
- "initWithIdentifier:date:fidelityPolicyMask:placeInference:"
- "initWithIdentifier:date:fidelityPolicyMask:placeInference:sourceIdentifier:"
- "initWithIdentifier:entry:exit:location:locationOfInterestConfidence:locationOfInterestSource:"
- "initWithIdentifier:featureToHashedApMapping:featureToHashedApMappingDataURL:url:"
- "initWithIdentifier:geoAddressData:subPremises:isIsland:creationDate:expirationDate:iso3166CountryCode:iso3166SubdivisionCode:"
- "initWithIdentifier:geoAddressData:subPremises:subThoroughfare:thoroughfare:subLocality:locality:subAdministrativeArea:administrativeArea:administrativeAreaCode:postalCode:country:countryCode:inlandWater:ocean:areasOfInterest:isIsland:creationDate:expirationDate:iso3166CountryCode:iso3166SubdivisionCode:"
- "initWithIdentifier:geoAddressObject:subPremises:isIsland:creationDate:expirationDate:iso3166CountryCode:iso3166SubdivisionCode:"
- "initWithIdentifier:loiIsMissingFromCurrentVisitHistory:isHome:isWork:"
- "initWithIdentifier:name:category:categoryMUID:address:location:source:mapItemPlaceType:muid:resultProviderID:geoMapItemHandle:geoMapItemIdentifier:creationDate:expirationDate:extendedAttributes:displayLanguage:disputed:"
- "initWithIdentifier:name:category:categoryMUID:address:location:source:mapItemPlaceType:muid:resultProviderID:geoMapItemHandle:geoMapItemIdentifier:creationDate:expirationDate:extendedAttributes:displayLanguage:disputed:businessHours:"
- "initWithIdentifier:parkDate:"
- "initWithIdentifier:predictedContextResult:requestStartDate:requestEndDate:inferenceTriggerReason:memoryFootprintStart:memoryFootprintEnd:clientCount:"
- "initWithIdentifier:primary:"
- "initWithIdentifier:settledState:start:accessPoints:"
- "initWithIdentifier:startDate:stopDate:visitIdentifierOrigin:visitIdentifierDestination:modeOfTransportation:"
- "initWithIdentifier:submissionDate:expirationDate:entryDate:exitDate:curatedLabel:"
- "initWithIdentifier:submissionDate:expirationDate:entryDate:exitDate:visitIdentifier:originalLabel:curatedLabel:"
- "initWithLatitude:longitude:"
- "initWithLatitude:longitude:course:followedByUTurn:locationReferenceFrame:"
- "initWithLatitude:longitude:horizontalUncertainty:altitude:verticalUncertainty:date:referenceFrame:speed:"
- "initWithLatitude:longitude:horizontalUncertainty:altitude:verticalUncertainty:date:referenceFrame:speed:sourceAccuracy:"
- "initWithLatitude:longitude:horizontalUncertainty:date:"
- "initWithLatitude:longitude:horizontalUncertainty:date:referenceFrame:"
- "initWithLearnedRouteId:routeStartLocation:routeEndLocation:travelTimeEntireRouteSec:travelDistanceEntireRouteMeter:travelModeRoutes:routeStartLocationWithReferenceFrame:routeEndLocationWithReferenceFrame:"
- "initWithLocation:confidence:identifier:type:typeSource:visits:customLabel:mapItem:"
- "initWithLocation:source:date:"
- "initWithLocationOfInterest:confidence:nextEntryTime:modeOfTransportation:sources:"
- "initWithLocationOfInterest:dateInterval:predictionSources:probability:"
- "initWithLocations:errorFunction:"
- "initWithMac:rssi:channel:age:date:"
- "initWithMachContinuousTimeSec:"
- "initWithMachServiceName:options:"
- "initWithMapItem:confidence:source:"
- "initWithMapItem:finerGranularityMapItem:userType:userTypeSource:placeType:referenceLocation:confidence:finerGranularityMapItemConfidence:loiIdentifier:"
- "initWithMapItem:finerGranularityMapItem:userType:userTypeSource:placeType:referenceLocation:confidence:finerGranularityMapItemConfidence:loiIdentifier:preferredName:"
- "initWithMapItem:userType:userTypeSource:placeType:referenceLocation:confidence:loiIdentifier:"
- "initWithMapItem:userType:userTypeSource:placeType:referenceLocation:confidence:loiIdentifier:preferredName:"
- "initWithMinCountOfTraversal:startLatitude:startLongitude:endLatitude:endLongitude:"
- "initWithNumberOfSeconds:"
- "initWithOptions:startDate:endDate:"
- "initWithOptions:startDate:endDate:maximumNumberOfItems:"
- "initWithOptionsMask:"
- "initWithOriginVisitLatitude:originVisitLongitude:destinationVisitLatitude:destinationVisitLongitude:"
- "initWithPOIConfidences:aoiConfidences:distanceToNearestAOILowerBound:referenceLocation:queryTime:"
- "initWithPOIConfidences:aoiConfidences:referenceLocation:queryTime:"
- "initWithPeriodicReportInterval:magnitude:densityUpdateHandler:"
- "initWithPredictedContextDateInterval:predictionSources:probability:"
- "initWithPredictedContextTransports:predictedContextDateInterval:predictionSources:probability:"
- "initWithPredictedContexts:analytics:"
- "initWithProbability:dateInterval:predictedContexts:"
- "initWithReferenceLocation:ascending:dateInterval:limit:batchSize:"
- "initWithReferenceLocation:sourceFilter:ascending:dateInterval:limit:batchSize:"
- "initWithReferenceLocation:sourceFilter:ascending:distance:dateInterval:limit:batchSize:"
- "initWithRestorationIdentifier:"
- "initWithRestorationIdentifier:targetUserSession:"
- "initWithRoadClass:formOfWay:locationType:startLocationName:endLocationName:"
- "initWithRolledLOIResult:"
- "initWithRouteTravelMode:maxTravelTimeEstimateInSeconds:minTravelTimeEstimateInSeconds:meanTravelTimeEstimateInSeconds:maxTravelledDistanceEstimateInMeters:minTravelledDistanceEstimateInMeters:meanTravelledDistanceEstimateInMeters:routeLocations:learnedRouteLocations:learnedRouteMetrics:"
- "initWithRoutineManager:"
- "initWithServiceLevel:storageDuration:observationInterval:densityCallbackConfiguration:"
- "initWithStartAndEndVisitLatitude:startLongitude:endLatitude:endLongitude:"
- "initWithStartDate:endDate:"
- "initWithStartDate:length:"
- "initWithStartDistance:endDistance:"
- "initWithStartLocation:endLocation:expectedVisits:"
- "initWithStartTime:endTime:"
- "initWithStartVisitLatitude:startLongitude:"
- "initWithStartVisitLatitude:startVisitLongitude:endVisitLatitude:endVisitLongitude:"
- "initWithStatus:"
- "initWithStatus:zdrConfirmationList:"
- "initWithSubPremise:subPremiseType:"
- "initWithTargetUserSession:"
- "initWithTransportMode:probability:"
- "initWithTripClusterId:dateOfMostRecentTrip:modeOfTransport:countOfTraversal:originLatitude:originLongitude:destinationLatitude:destinationLongitude:averageTripTime:averageTripDistance:minimumTripTime:maximumTripTime:minimumTripDistance:maximumTripDistance:commuteID:isLocked:avgBikeDistance:avgBikeTime:avgWalkDistance:avgWalkTime:bikeTraversalCount:walkTraversalCount:clusterOrder:"
- "initWithTripSegment:"
- "initWithTripSegment:fetchRoadClass:fetchFormOfWay:fetchLocationType:fetchPreferredNames:"
- "initWithTripSegment:preferredDownsamplingLevel:"
- "initWithTripSegment:preferredDownsamplingLevel:batchSize:offset:"
- "initWithTripSegment:preferredDownsamplingLevel:boundingBoxLocation:batchSize:offset:"
- "initWithTripSegmentIdentifier:dateInterval:tripDistance:tripDistanceUncertainty:modeOfTransportation:isConsumedByClustering:tripSegmentSequence:tripSegmentSequenceMax:originLatitude:originLongitude:destinationLatitude:destinationLongitude:tripCommuteID:"
- "initWithType:"
- "initWithType:confidence:startDate:"
- "initWithUUIDBytes:"
- "initWithUsageDate:"
- "initWithUsageDate:navigationWasInterrupted:"
- "initWithUseBackgroundTraits:analyticsIdentifier:"
- "initWithUseBackgroundTraits:analyticsIdentifier:clientIdentifier:"
- "initWithVehicleEvent:"
- "initWithVertices:"
- "initWithVisitsDescriptionData:"
- "initWithVisitsDescriptionPListPath:"
- "initWithWeekday:timeIntervals:"
- "initWithWorkoutUUID:startDate:"
- "initWithbatchSize:"
- "initWithinDistance:location:startDate:endDate:"
- "initWithinDistance:location:startDate:endDate:clientIdentifier:"
- "intValue"
- "integerValue"
- "interArrivalTime"
- "interfaceWithProtocol:"
- "intersectsDateInterval:"
- "invalidate"
- "isAfterDate:"
- "isAllDay"
- "isAscending"
- "isBeforeDate:"
- "isDateWithinLast24Hours:"
- "isEqual:"
- "isEqualToAddress:"
- "isEqualToAddressSubPremise:"
- "isEqualToArray:"
- "isEqualToBusinessHours:"
- "isEqualToContext:"
- "isEqualToCoordinate:"
- "isEqualToDailyHours:"
- "isEqualToData:"
- "isEqualToDate:"
- "isEqualToDateInterval:"
- "isEqualToDictionary:"
- "isEqualToFetchOptions:"
- "isEqualToLocalTimeInterval:"
- "isEqualToLocation:"
- "isEqualToMapItem:"
- "isEqualToMapItemExtendedAttributes:"
- "isEqualToNumber:"
- "isEqualToOptions:"
- "isEqualToPlaceInference:"
- "isEqualToPolygon:"
- "isEqualToString:"
- "isEqualToUserCuration:"
- "isEqualToVisit:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isOnOrAfter:"
- "isOnOrBefore:"
- "isProxy"
- "isRegistered"
- "isSubclassOfClass:"
- "isValid"
- "isValidJSONObject:"
- "isValidRouteFetchType:"
- "key"
- "lastBucketFill"
- "lastObject"
- "laterDate:"
- "launchTaskWithSelector:remainingAttempts:proxyErrorHandler:taskBlock:"
- "launchdManaged"
- "learnedRouteEndLocation"
- "learnedRouteEndLocationWithReferenceFrame"
- "learnedRouteIdentifier"
- "learnedRouteStartLocation"
- "learnedRouteStartLocationWithReferenceFrame"
- "leechedLowConfidenceVisitHandler"
- "leechedVisitHandler"
- "left"
- "length"
- "likelihood"
- "localTimeZone"
- "localeWithLocaleIdentifier:"
- "localizedStringForKey:value:table:"
- "locationOfInterestTypeIsValid:"
- "locationOfInterestTypeSourceToString:"
- "locationOfInterestTypeToString:"
- "locationReferenceFrame"
- "loiIsMissingFromCurrentVisitHistory"
- "lowercaseString"
- "mainBundle"
- "mapItem, %@, confidence, %.3f, source, %@"
- "mapItemStorageForGEOMapItem:"
- "mapsIdentifierString"
- "maskForSources:"
- "maxTravelTimeEstimateInSeconds"
- "maxTravelledDistanceEstimateInMeters"
- "maximumError"
- "maximumErrorIndex"
- "maximumTripDistance"
- "maximumTripTime"
- "meanTravelTimeEstimateInSeconds"
- "meanTravelledDistanceEstimateInMeters"
- "mergeTripSegment:other:"
- "mergeWithAnotherContactScore:"
- "mergedThoroughfare"
- "minTravelTimeEstimateInSeconds"
- "minTravelledDistanceEstimateInMeters"
- "minimumTripDistance"
- "minimumTripTime"
- "minute"
- "modeOfTransportationToString:"
- "monitoredScenarioTriggerTypes"
- "month"
- "mostConfidentAOI"
- "mostConfidentPOI"
- "motionActivityConfidenceFromString:"
- "motionActivityConfidenceToString:"
- "motionActivityTypeFromString:"
- "motionActivityTypeToString:"
- "muid, %lu, applePaySupport, %@, category, %@, nearbyPOICount, %lu"
- "mutableCopy"
- "nameFromType:"
- "nameFromUserType:"
- "nextStepPredictedContextsWithFilterMask:"
- "nilUUID"
- "now"
- "numberWithBool:"
- "numberWithDouble:"
- "numberWithInteger:"
- "numberWithLongLong:"
- "numberWithUnsignedInt:"
- "numberWithUnsignedInteger:"
- "numberWithUnsignedLongLong:"
- "numberWithUnsignedShort:"
- "objectAtIndex:"
- "objectAtIndexedSubscript:"
- "objectForKey:"
- "objectForKeyedSubscript:"
- "observationInterval"
- "onDensityUpdate:error:"
- "onGeneratedTripSegment:andError:"
- "onGeneratedTripSegment:withError:"
- "onLeechedLowConfidenceVisit:withError:"
- "onLeechedVisit:withError:"
- "onPlaceInferences:error:"
- "onPredictedContextResult:error:"
- "onRemoteStatusUpdate:error:"
- "onScenarioTrigger:withError:"
- "onScenarioTriggers:error:"
- "onVehicleEvents:error:"
- "onVisit:withError:"
- "operationAllowed"
- "operationAllowedWithCost:"
- "originVisitLatitude"
- "originVisitLongitude"
- "outputToDictionary"
- "outputToDictionaryReadableDate:"
- "outputToFirstJSONDictionary"
- "peopleDiscoveryErrorHandler"
- "peopleDiscoveryRegistrant"
- "performBluePOIQueryLookingBack:lookingAhead:handler:"
- "performBluePOIQueryLookingBack:lookingAhead:reply:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "periodicReportInterval"
- "placeInferenceOptions"
- "placeInferencePlaceTypeFromMapItem:userType:source:"
- "placeInferencesHandler"
- "placeTypeToString:"
- "postCode"
- "predicateWithBlock:"
- "predictedContextHandler"
- "predictedContextOptions"
- "predictedContextsWithType:afterContext:"
- "predictedSequencesAfterContext:"
- "preferredLanguages"
- "processHindsightVisitsWithHandler:"
- "processHindsightVisitsWithReply:"
- "processingBlock"
- "pruneVisitsWithDateInterval:"
- "purgeTripClusterTable:handler:"
- "purgeTripClusterTable:reply:"
- "purgeTripClusterWithClusterID:handler:"
- "purgeTripClusterWithClusterID:reply:"
- "q16@0:8"
- "q24@0:8@16"
- "q24@0:8q16"
- "q24@?0@\"NSString\"8@\"NSString\"16"
- "queue"
- "recencyScore"
- "recentCompare:"
- "registered"
- "relationship"
- "release"
- "remoteObjectInterface"
- "remoteObjectProxyWithErrorHandler:"
- "remoteStatusHandler"
- "removeLocationOfInterestWithIdentifier:handler:"
- "removeLocationOfInterestWithIdentifier:reply:"
- "removeObjectForKey:"
- "removeVisitWithIdentifier:handler:"
- "removeVisitWithIdentifier:reply:"
- "reset"
- "respondsToSelector:"
- "restorationIdentifier"
- "resultSortProbabilityAscending"
- "resultSortStartDateAscending"
- "resume"
- "retain"
- "retainCount"
- "reverseObjectEnumerator"
- "right"
- "roundingUpDate:bucketDurationMinute:"
- "routeFetchType"
- "routeTravelMode"
- "routineManager"
- "routineModeToString:"
- "runningMean"
- "runningMeanOfSquares"
- "s"
- "s16@0:8"
- "sampledLocations"
- "scanDuration"
- "scenarioTriggerHandlers"
- "scenarioTriggerRegistrant"
- "scenarioTriggerSettledStateToString:"
- "scenarioTriggerTypeToString:"
- "second"
- "secondsForStorageDuration:"
- "selector"
- "selectorIsAllowed:"
- "self"
- "serviceLevel"
- "setActionRegistrant:"
- "setAddressIdentifier:"
- "setAscending:"
- "setAvgBikeDistance:"
- "setAvgBikeTime:"
- "setAvgWalkDistance:"
- "setAvgWalkTime:"
- "setBatchSize:"
- "setBikeTraversalCount:"
- "setBoundingBoxLocation:"
- "setBundleIdentifier:"
- "setBundlePath:"
- "setClass:forSelector:argumentIndex:ofReply:"
- "setClasses:forSelector:argumentIndex:ofReply:"
- "setClientCallback:"
- "setClientThrottle:"
- "setClusterID:"
- "setClusterOrder:"
- "setConfidence:"
- "setConfirmed:"
- "setCreationDate:"
- "setDate:"
- "setDateFormat:"
- "setDateInterval:"
- "setDateStyle:"
- "setDay:"
- "setDestinationVisit:"
- "setDownsampleRequired:"
- "setEndDate:"
- "setEndLatitude:"
- "setEndLongitude:"
- "setEventAgentHelper:"
- "setExportedInterface:"
- "setExportedObject:"
- "setExtendedAttributes:"
- "setFrequencyCount:"
- "setFrequencyScore:"
- "setFullConfirmationList:"
- "setGeneratedTripSegmentRegistrant:"
- "setHintForRegionState:significantRegion:reply:"
- "setHintForRegionState:significantRegion:withHandler:"
- "setHorizontalAccuracy:"
- "setHorizontalUncertainty:"
- "setHour:"
- "setIdentifier:"
- "setInterArrivalTime:"
- "setIsConsumedByClustering:"
- "setIsMe:"
- "setLastBucketFill:"
- "setLatitude:"
- "setLeechedLowConfidenceVisitHandler:"
- "setLeechedVisitHandler:"
- "setLeft:"
- "setLikelihood:"
- "setLocale:"
- "setLocation:"
- "setLocationFinalized:"
- "setLocationQuality:"
- "setLocations:"
- "setLongitude:"
- "setMapItem:"
- "setMask:"
- "setMaximumError:"
- "setMaximumErrorIndex:"
- "setMinCountOfTraversal:"
- "setMinute:"
- "setModeOfTransportation:"
- "setMostConfidentAOI:"
- "setMostConfidentPOI:"
- "setNearbyLocationOfInterest:"
- "setNotes:"
- "setObject:atIndexedSubscript:"
- "setObject:forKey:"
- "setObject:forKeyedSubscript:"
- "setOptionsMask:"
- "setOriginVisit:"
- "setPeopleDiscoveryErrorHandler:"
- "setPeopleDiscoveryRegistrant:"
- "setPhoto:"
- "setPlaceInference:"
- "setPlaceInferenceOptions:"
- "setPlaceInferencesHandler:"
- "setPredictedContextHandler:"
- "setPredictedContextOptions:"
- "setPreferredDownsamplingLevel:"
- "setQueue:"
- "setRecencyScore:"
- "setRemoteObjectInterface:"
- "setRemoteStatusHandler:"
- "setRestorationIdentifier:"
- "setRight:"
- "setRoutineEnabled:"
- "setRoutineEnabled:reply:"
- "setRoutineEnabled:withHandler:"
- "setRoutineManager:"
- "setRunningMean:"
- "setRunningMeanOfSquares:"
- "setScenarioTriggerRegistrant:"
- "setSecond:"
- "setSettledState:"
- "setSignificanceScore:"
- "setSmoothingErrorThreshold:"
- "setSmoothingRequired:"
- "setSource:"
- "setStartDate:"
- "setStartLatitude:"
- "setStartLongitude:"
- "setSubmissionDateInterval:"
- "setTargetUserSession:"
- "setTimeStyle:"
- "setTimeZone:"
- "setTripCommuteID:"
- "setTripSegmentSequence:"
- "setTripSegmentSequenceMax:"
- "setType:"
- "setUncertainty:"
- "setUserSetLocation:"
- "setUsualLocation:"
- "setValue:forKey:"
- "setVehicleEventsHandler:"
- "setVehicleIdentifier:"
- "setVisitDateInterval:"
- "setVisitHandler:"
- "setWalkTraversalCount:"
- "setWifiConfidence:"
- "setWifiFingerprintLabelType:"
- "setWithArray:"
- "setWithObject:"
- "setWithObjects:"
- "setXpcConnection:"
- "setXpcQueue:"
- "setZdrConfirmationList:"
- "sharingStatusToString:"
- "shouldAdvertise"
- "shuffle"
- "significanceScore"
- "signingIdentifierFromSelf"
- "socialScore"
- "sortDescriptorWithKey:ascending:"
- "sortDescriptorWithKey:ascending:selector:"
- "sortUsingComparator:"
- "sortUsingDescriptors:"
- "sortedArrayUsingComparator:"
- "sourceAccuracyToString:"
- "sourceToString:"
- "splitLocationsWithErrorFunction:"
- "startLeechingLowConfidenceVisitsWithHandler:"
- "startLeechingLowConfidenceVisitsWithReply:"
- "startLeechingVisitsWithHandler:"
- "startLeechingVisitsWithReply:"
- "startMonitoringForGeneratedTripSegmentsWithCallback:"
- "startMonitoringForGeneratedTripSegmentsWithReply:"
- "startMonitoringForPeopleDiscovery:"
- "startMonitoringForPeopleDiscovery:handler:"
- "startMonitoringForPeopleDiscoveryWithIdentifier:configuration:reply:"
- "startMonitoringForScenarioTriggerTypes:handler:"
- "startMonitoringPlaceInferencesWithOptions:handler:"
- "startMonitoringPlaceInferencesWithOptions:reply:"
- "startMonitoringPredictedContextWithOptions:completionHandler:"
- "startMonitoringPredictedContextWithOptions:reply:"
- "startMonitoringRemoteStatusWithHandler:"
- "startMonitoringRemoteStatusWithReply:"
- "startMonitoringScenarioTriggerOfType:reply:"
- "startMonitoringScenarioTriggerOfType:withHandler:"
- "startMonitoringVehicleEventsWithHandler:"
- "startMonitoringVehicleEventsWithReply:"
- "startMonitoringVisitsWithHandler:"
- "startMonitoringVisitsWithReply:"
- "startMonitoringWithCallback:"
- "startOfDay"
- "startOfDayAfterAddingUnit:value:"
- "startOfDayForDate:"
- "stopLeechingLowConfidenceVisits"
- "stopLeechingLowConfidenceVisitsWithReply:"
- "stopLeechingVisits"
- "stopLeechingVisitsWithReply:"
- "stopMonitoring"
- "stopMonitoringForGeneratedTripSegments"
- "stopMonitoringForGeneratedTripSegmentsWithReply:"
- "stopMonitoringForPeopleDiscovery"
- "stopMonitoringForPeopleDiscoveryWithHandler:"
- "stopMonitoringForPeopleDiscoveryWithIdentifier:reply:"
- "stopMonitoringForScenarioTriggerTypes:"
- "stopMonitoringNextPredictedLocationsOfInterest"
- "stopMonitoringPlaceInferences"
- "stopMonitoringPlaceInferencesWithReply:"
- "stopMonitoringPredictedContextWithHandler:"
- "stopMonitoringPredictedContextWithReply:"
- "stopMonitoringRemoteStatusWithHandler:"
- "stopMonitoringRemoteStatusWithReply:"
- "stopMonitoringScenarioTriggerOfType:"
- "stopMonitoringScenarioTriggerOfType:reply:"
- "stopMonitoringVehicleEvents"
- "stopMonitoringVehicleEventsWithReply:"
- "stopMonitoringVisits"
- "stopMonitoringVisitsWithReply:"
- "storageDuration"
- "string"
- "stringForSubPremiseType:"
- "stringFromDate"
- "stringFromDate:"
- "stringFromTimestamp:"
- "stringFromVisitIncidentType:"
- "stringValue"
- "stringWithCString:encoding:"
- "stringWithFormat:"
- "structuredAddress"
- "subarrayWithRange:"
- "submitToCoreAnalytics:type:duration:"
- "submitUserCurationForDate:newLabel:handler:"
- "submitUserCurationForVisitDateRange:newLabel:handler:"
- "superclass"
- "supportsSecureCoding"
- "synchronousRemoteObjectProxyWithErrorHandler:"
- "targetUserSession"
- "timeIntervalSince1970"
- "timeIntervalSinceDate:"
- "timeIntervalSinceReferenceDate"
- "timeIntervalUntilOperationAllowed"
- "timeIntervalUntilOperationAllowedWithCost:"
- "timestamp"
- "totalCount"
- "travelTimeEstimateForEntireRouteInSeconds"
- "travelledDistanceEstimateForEntireRouteInMeters"
- "tripSegmentSequence"
- "tripSegmentSequenceMax"
- "unarchivedObjectOfClass:fromData:error:"
- "unknownPredictedContextFromStart:end:"
- "unsignedIntValue"
- "unsignedIntegerValue"
- "unsignedLongLongValue"
- "updateCloudSyncProvisionedForAccount:handler:"
- "updateCloudSyncProvisionedForAccount:reply:"
- "updateLocationOfInterestWithIdentifier:customLabel:handler:"
- "updateLocationOfInterestWithIdentifier:customLabel:reply:"
- "updateLocationOfInterestWithIdentifier:mapItem:handler:"
- "updateLocationOfInterestWithIdentifier:mapItemStorage:reply:"
- "updateLocationOfInterestWithIdentifier:type:customLabel:handler:"
- "updateLocationOfInterestWithIdentifier:type:customLabel:reply:"
- "updateLocationOfInterestWithIdentifier:type:handler:"
- "updateLocationOfInterestWithIdentifier:type:mapItem:customLabel:handler:"
- "updateLocationOfInterestWithIdentifier:type:mapItemStorage:customLabel:reply:"
- "updateLocationOfInterestWithIdentifier:type:reply:"
- "updateVehicleEventWithIdentifier:geoMapItem:"
- "updateVehicleEventWithIdentifier:geoMapItem:reply:"
- "updateVehicleEventWithIdentifier:location:"
- "updateVehicleEventWithIdentifier:location:reply:"
- "updateVehicleEventWithIdentifier:notes:"
- "updateVehicleEventWithIdentifier:notes:reply:"
- "updateVehicleEventWithIdentifier:photo:"
- "updateVehicleEventWithIdentifier:photo:reply:"
- "updateWeightWithSource:extendedAttributes:"
- "userInteractionWithPredictedLocationOfInterest:interaction:feedback:"
- "userInteractionWithPredictedLocationOfInterest:interaction:feedback:geoMapItem:handler:"
- "userInteractionWithPredictedLocationOfInterest:interaction:feedback:geoMapItem:reply:"
- "userSpecificPlaceTypeSourceToString:"
- "userSpecificPlaceTypeToString:"
- "uuid"
- "v16@0:8"
- "v16@?0@\"<RTDaemonProtocol>\"8"
- "v16@?0@8"
- "v20@0:8B16"
- "v20@0:8S16"
- "v20@0:8i16"
- "v20@0:8s16"
- "v24@0:8@\"NSCoder\"16"
- "v24@0:8@\"NSString\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8@?<v@?@\"NSArray\"@\"NSError\">16"
- "v24@0:8@?<v@?@\"NSDictionary\"@\"NSError\">16"
- "v24@0:8@?<v@?@\"NSError\">16"
- "v24@0:8@?<v@?@\"RTAuthorizedLocationStatus\"@\"NSError\">16"
- "v24@0:8@?<v@?@\"RTPeopleDensity\"@\"NSError\">16"
- "v24@0:8@?<v@?B>16"
- "v24@0:8@?<v@?B@\"NSError\">16"
- "v24@0:8@?<v@?Q@\"NSError\">16"
- "v24@0:8@?<v@?q@\"NSError\">16"
- "v24@0:8Q16"
- "v24@0:8d16"
- "v24@0:8q16"
- "v28@0:8B16@?20"
- "v28@0:8B16@?<v@?@\"NSError\">20"
- "v32@0:8@\"CLCircularRegion\"16@?<v@?@\"RTLocationOfInterest\"@\"NSError\">24"
- "v32@0:8@\"CLLocation\"16@?<v@?@\"NSDate\"@\"NSError\">24"
- "v32@0:8@\"CLLocation\"16@?<v@?@\"RTLocationOfInterest\"@\"NSError\">24"
- "v32@0:8@\"CLLocation\"16@?<v@?q@\"NSError\">24"
- "v32@0:8@\"NSArray\"16@\"NSError\"24"
- "v32@0:8@\"NSArray\"16@?<v@?@\"NSArray\"@\"NSError\">24"
- "v32@0:8@\"NSArray\"16@?<v@?@\"NSError\">24"
- "v32@0:8@\"NSDate\"16@?<v@?@\"NSArray\"@\"NSError\">24"
- "v32@0:8@\"NSNumber\"16@?<v@?@\"NSError\">24"
- "v32@0:8@\"NSSet\"16@?<v@?@\"NSError\">24"
- "v32@0:8@\"NSString\"16@?<v@?@\"NSArray\"@\"NSError\">24"
- "v32@0:8@\"NSString\"16@?<v@?@\"NSError\">24"
- "v32@0:8@\"NSUUID\"16@?<v@?@\"NSArray\"@\"NSError\">24"
- "v32@0:8@\"NSUUID\"16@?<v@?@\"NSError\">24"
- "v32@0:8@\"NSUUID\"16@?<v@?@\"RTInferredMapItem\"@\"NSError\">24"
- "v32@0:8@\"NSUUID\"16@?<v@?@\"RTLocationOfInterest\"@\"NSError\">24"
- "v32@0:8@\"RTBackgroundInertialOdometrySampleEnumerationOptions\"16@?<v@?@\"NSArray\"@\"NSError\">24"
- "v32@0:8@\"RTDiagnosticOptions\"16@?<v@?@\"NSString\"@\"NSError\">24"
- "v32@0:8@\"RTFamiliarityIndexOptions\"16@?<v@?@\"NSArray\"@\"NSError\">24"
- "v32@0:8@\"RTLearnedRouteFetchOptions\"16@?<v@?@\"NSArray\"^B@\"NSError\">24"
- "v32@0:8@\"RTLocationsForTripSegmentFetchOptions\"16@?<v@?@\"NSArray\"@\"NSError\">24"
- "v32@0:8@\"RTLocationsForTripSegmentFetchOptions\"16@?<v@?Q@\"NSError\">24"
- "v32@0:8@\"RTPlaceInferenceOptions\"16@?<v@?@\"NSArray\"@\"NSError\">24"
- "v32@0:8@\"RTPlaceInferenceOptions\"16@?<v@?@\"NSError\">24"
- "v32@0:8@\"RTPredictedContextOptions\"16@?<v@?@\"NSError\">24"
- "v32@0:8@\"RTPredictedContextOptions\"16@?<v@?@\"RTPredictedContextResult\"@\"NSError\">24"
- "v32@0:8@\"RTPredictedContextResult\"16@\"NSError\"24"
- "v32@0:8@\"RTScenarioTrigger\"16@\"NSError\"24"
- "v32@0:8@\"RTStoredElevationEnumerationContext\"16@?<v@?@\"NSArray\"@\"NSError\">24"
- "v32@0:8@\"RTStoredElevationEnumerationOptions\"16@?<v@?@\"NSArray\"@\"NSError\">24"
- "v32@0:8@\"RTStoredLocationEnumerationContext\"16@?<v@?@\"NSArray\"@\"NSError\">24"
- "v32@0:8@\"RTStoredTripSegmentFetchOptions\"16@?<v@?@\"NSArray\"@\"NSError\">24"
- "v32@0:8@\"RTStoredVehicleFetchOptions\"16@?<v@?@\"NSArray\"@\"NSError\">24"
- "v32@0:8@\"RTStoredVisitFetchOptions\"16@?<v@?@\"NSArray\"@\"NSError\">24"
- "v32@0:8@\"RTTripClusterMetadataFetchOptions\"16@?<v@?@\"NSArray\"@\"NSError\">24"
- "v32@0:8@\"RTTripSegment\"16@\"NSError\"24"
- "v32@0:8@\"RTTripSegmentMetadataFetchOptions\"16@?<v@?@\"RTTripSegmentMetadata\"@\"NSError\">24"
- "v32@0:8@\"RTVisit\"16@\"NSError\"24"
- "v32@0:8@16@24"
- "v32@0:8@16@?24"
- "v32@0:8Q16@24"
- "v32@0:8Q16@?24"
- "v32@0:8Q16@?<v@?@\"NSError\">24"
- "v32@0:8q16@\"NSError\"24"
- "v32@0:8q16@24"
- "v32@0:8q16@?24"
- "v32@0:8q16@?<v@?@\"NSArray\"@\"NSError\">24"
- "v40@0:8@\"CLLocation\"16@\"NSDate\"24@?<v@?@\"NSArray\"@\"NSError\">32"
- "v40@0:8@\"CLLocation\"16@\"NSString\"24@?<v@?@\"NSError\">32"
- "v40@0:8@\"NSDate\"16@\"NSDate\"24@?<v@?@\"NSArray\"@\"NSError\">32"
- "v40@0:8@\"NSDate\"16@\"RTEstimatedLocationOptions\"24@?<v@?@\"CLLocation\"@\"NSError\">32"
- "v40@0:8@\"NSDateInterval\"16@\"GEOMapItemStorage\"24@?<v@?@\"NSError\">32"
- "v40@0:8@\"NSString\"16@\"RTPeopleDiscoveryServiceConfiguration\"24@?<v@?@\"NSError\">32"
- "v40@0:8@\"NSUUID\"16@\"CLLocation\"24@?<v@?@\"NSError\">32"
- "v40@0:8@\"NSUUID\"16@\"GEOMapItemStorage\"24@?<v@?@\"NSError\">32"
- "v40@0:8@\"NSUUID\"16@\"NSData\"24@?<v@?@\"NSError\">32"
- "v40@0:8@\"NSUUID\"16@\"NSString\"24@?<v@?@\"NSError\">32"
- "v40@0:8@\"NSUUID\"16q24@?<v@?@\"NSError\">32"
- "v40@0:8@\"RTEnumerationOptions\"16@\"NSNumber\"24@?<v@?@\"NSArray\"@\"NSNumber\"@\"NSError\">32"
- "v40@0:8@16@24@?32"
- "v40@0:8@16Q24@32"
- "v40@0:8@16q24@?32"
- "v40@0:8@16q24d32"
- "v40@0:8d16@\"CLLocation\"24@?<v@?@\"NSArray\"@\"NSError\">32"
- "v40@0:8d16@24@?32"
- "v40@0:8d16d24@?32"
- "v40@0:8d16d24@?<v@?@\"NSArray\"@\"NSArray\"@\"NSArray\"@\"NSError\">32"
- "v40@0:8d16d24@?<v@?@\"NSArray\"@\"NSError\">32"
- "v40@0:8q16@\"CLCircularRegion\"24@?<v@?B@\"NSError\">32"
- "v40@0:8q16@24@?32"
- "v48@0:8:16Q24@?32@?40"
- "v48@0:8@\"CLLocation\"16@\"NSDate\"24d32@?<v@?@\"NSArray\"@\"NSError\">40"
- "v48@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32@?<v@?@\"NSArray\"@\"NSError\">40"
- "v48@0:8@\"NSUUID\"16q24@\"NSString\"32@?<v@?@\"NSError\">40"
- "v48@0:8@16@24@32@?40"
- "v48@0:8@16@24d32@?40"
- "v48@0:8@16q24@32@?40"
- "v48@0:8q16@\"GEOMapItemStorage\"24@\"NSString\"32@?<v@?@\"RTLocationOfInterest\"@\"NSError\">40"
- "v48@0:8q16@24@32@?40"
- "v56@0:8@\"NSUUID\"16@\"NSDate\"24@\"GEOMapItemStorage\"32@\"GEOMapItemStorage\"40@?<v@?@\"NSError\">48"
- "v56@0:8@\"NSUUID\"16q24@\"GEOMapItemStorage\"32@\"NSString\"40@?<v@?@\"RTLocationOfInterest\"@\"NSError\">48"
- "v56@0:8@\"RTPredictedLocationOfInterest\"16Q24@\"NSString\"32@\"GEOMapItemStorage\"40@?<v@?@\"NSError\">48"
- "v56@0:8@16@24@32@40@?48"
- "v56@0:8@16Q24@32@40@?48"
- "v56@0:8@16q24@32@40@?48"
- "validMUID"
- "validVisitSources:"
- "valueForKey:"
- "valueForKeyPath:"
- "vehicleEventAtLocation:notes:"
- "vehicleEventAtLocation:notes:handler:"
- "vehicleEventAtLocation:notes:reply:"
- "vehicleEventsHandler"
- "visitHandler"
- "visitIncidentTypeFromString:"
- "visitsDescriptionDataAtPath:"
- "visitsOverlapping:"
- "weekdayStringFromDate"
- "weight"
- "weightForExtendedAttributes:"
- "weightForSource:"
- "xpcConnection"
- "xpcQueue"
- "year"
- "zdrConfirmationList"
- "zone"

```
