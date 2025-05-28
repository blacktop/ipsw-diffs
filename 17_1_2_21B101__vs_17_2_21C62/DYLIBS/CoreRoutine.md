## CoreRoutine

> `/System/Library/PrivateFrameworks/CoreRoutine.framework/CoreRoutine`

```diff

-893.0.5.0.2
-  __TEXT.__text: 0x39494
-  __TEXT.__auth_stubs: 0x670
-  __TEXT.__objc_methlist: 0x42fc
-  __TEXT.__const: 0x188
-  __TEXT.__oslogstring: 0x2187
-  __TEXT.__cstring: 0x3899
-  __TEXT.__gcc_except_tab: 0x280
-  __TEXT.__unwind_info: 0x1044
-  __TEXT.__objc_classname: 0x809
-  __TEXT.__objc_methname: 0x8ae8
-  __TEXT.__objc_methtype: 0x1a11
-  __TEXT.__objc_stubs: 0x4c80
-  __DATA_CONST.__got: 0x50
-  __DATA_CONST.__const: 0xb20
+895.0.11.0.2
+  __TEXT.__text: 0x3aee0
+  __TEXT.__auth_stubs: 0x620
+  __TEXT.__objc_methlist: 0x442c
+  __TEXT.__const: 0x190
+  __TEXT.__oslogstring: 0x212b
+  __TEXT.__cstring: 0x39d2
+  __TEXT.__gcc_except_tab: 0x1b8
+  __TEXT.__unwind_info: 0x108c
+  __TEXT.__objc_classname: 0x815
+  __TEXT.__objc_methname: 0x8e98
+  __TEXT.__objc_methtype: 0x1ad5
+  __TEXT.__objc_stubs: 0x4ec0
+  __DATA_CONST.__got: 0x58
+  __DATA_CONST.__const: 0xb28
   __DATA_CONST.__objc_classlist: 0x278
-  __DATA_CONST.__objc_catlist: 0x28
+  __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x6050
-  __DATA_CONST.__objc_selrefs: 0x1a98
+  __DATA_CONST.__objc_const: 0x6180
+  __DATA_CONST.__objc_selrefs: 0x1b48
   __DATA_CONST.__objc_arraydata: 0x90
-  __AUTH_CONST.__cfstring: 0x33e0
-  __AUTH_CONST.__objc_const: 0x2930
-  __AUTH_CONST.__const: 0x380
+  __AUTH_CONST.__cfstring: 0x36e0
+  __AUTH_CONST.__objc_const: 0x29b8
+  __AUTH_CONST.__const: 0x340
   __AUTH_CONST.__objc_intobj: 0xa8
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__objc_dictobj: 0x50
-  __AUTH_CONST.__auth_got: 0x348
+  __AUTH_CONST.__auth_got: 0x320
   __AUTH.__objc_data: 0x5a0
   __DATA.__objc_protorefs: 0x18
-  __DATA.__objc_classrefs: 0x2a8
+  __DATA.__objc_classrefs: 0x2b0
   __DATA.__objc_superrefs: 0x248
-  __DATA.__objc_ivar: 0x478
-  __DATA.__data: 0x2c0
+  __DATA.__objc_ivar: 0x490
+  __DATA.__data: 0x2a0
   __DATA_DIRTY.__objc_ivar: 0x98
   __DATA_DIRTY.__objc_data: 0x1310
   __DATA_DIRTY.__data: 0x30

   - /System/Library/Frameworks/CoreLocation.framework/CoreLocation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Security.framework/Security
-  - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/GeoServices.framework/GeoServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1599
-  Symbols:   5130
-  CStrings:  2355
+  Functions: 1623
+  Symbols:   5200
+  CStrings:  2404
 
Symbols:
+ +[RTAddress _decodeGeoAddressObjectFromData:decompress:]
+ +[RTAddress _encodeGeoAddressObject:compress:]
+ +[RTAddress _mergedThoroughfareWithSubPremises:subThoroughfare:thoroughfare:]
+ +[RTAuthorizedLocationStatus supportsSecureCoding]
+ +[RTMapItem placeTypeToString:]
+ +[RTPlaceInference placeInferencePlaceTypeFromMapItem:userType:source:]
+ -[GEOAddressObject(RTExtensions) initWithCurrentLocaleFullThoroughfare:subLocality:locality:subAdministrativeArea:administrativeArea:postalCode:country:countryCode:]
+ -[GEOAddressObject(RTExtensions) initWithFullThoroughfare:subLocality:locality:subAdministrativeArea:administrativeArea:postalCode:country:countryCode:language:countryLocale:phoneticLocale:]
+ -[RTAddress geoAddressData]
+ -[RTAddress geoAddressObject]
+ -[RTAddress geoDictionaryRepresentation]
+ -[RTAddress initWithGeoDictionary:language:country:phoneticLocale:]
+ -[RTAddress initWithIdentifier:geoAddressData:subPremises:isIsland:creationDate:expirationDate:iso3166CountryCode:iso3166SubdivisionCode:]
+ -[RTAddress initWithIdentifier:geoAddressData:subPremises:subThoroughfare:thoroughfare:subLocality:locality:subAdministrativeArea:administrativeArea:administrativeAreaCode:postalCode:country:countryCode:inlandWater:ocean:areasOfInterest:isIsland:creationDate:expirationDate:iso3166CountryCode:iso3166SubdivisionCode:]
+ -[RTAddress initWithIdentifier:geoAddressObject:subPremises:isIsland:creationDate:expirationDate:iso3166CountryCode:iso3166SubdivisionCode:]
+ -[RTAuthorizedLocationStatus copyWithZone:]
+ -[RTAuthorizedLocationStatus description]
+ -[RTAuthorizedLocationStatus eStatus]
+ -[RTAuthorizedLocationStatus encodeWithCoder:]
+ -[RTAuthorizedLocationStatus initWithCoder:]
+ -[RTAuthorizedLocationStatus initWithStatus:]
+ -[RTAuthorizedLocationStatus isEqual:]
+ -[RTFamiliarityIndexOptions initWithDateInterval:lookbackInterval:spatialGranularity:referenceLocation:referenceLocationSummary:distance:]
+ -[RTFamiliarityIndexOptions lookbackInterval]
+ -[RTMapItem initWithIdentifier:name:category:address:location:source:mapItemPlaceType:muid:resultProviderID:geoMapItemHandle:creationDate:expirationDate:extendedAttributes:displayLanguage:disputed:]
+ -[RTMapItem mapItemPlaceType]
+ -[RTPeopleDensity initWithBundleUUID:startDate:endDate:densityScore:scanDuration:rssiHistogram:]
+ -[RTPeopleDensity rssiHistogram]
+ -[RTRoutineManager fetchAuthorizedLocationStatus:]
+ _NSLocaleCountryCode
+ _OBJC_CLASS_$_GEOAddressObject
+ _OBJC_CLASS_$_NSKeyedArchiver
+ _OBJC_CLASS_$_NSKeyedUnarchiver
+ _OBJC_CLASS_$_RTAuthorizedLocationStatus
+ _OBJC_IVAR_$_RTAddress._geoAddressData
+ _OBJC_IVAR_$_RTAddress._localGeoAddressObject
+ _OBJC_IVAR_$_RTAuthorizedLocationStatus._eStatus
+ _OBJC_IVAR_$_RTFamiliarityIndexOptions._lookbackInterval
+ _OBJC_IVAR_$_RTMapItem._mapItemPlaceType
+ _OBJC_IVAR_$_RTPeopleDensity._rssiHistogram
+ _OBJC_METACLASS_$_RTAuthorizedLocationStatus
+ _RTFamiliarityIndexErrorDomain
+ __OBJC_$_CATEGORY_GEOAddressObject_$_RTExtensions
+ __OBJC_$_CLASS_METHODS_RTAuthorizedLocationStatus
+ __OBJC_$_CLASS_PROP_LIST_RTAuthorizedLocationStatus
+ __OBJC_$_INSTANCE_METHODS_GEOAddressObject(RTExtensions)
+ __OBJC_$_INSTANCE_METHODS_RTAuthorizedLocationStatus
+ __OBJC_$_INSTANCE_VARIABLES_RTAuthorizedLocationStatus
+ __OBJC_$_PROP_LIST_RTAuthorizedLocationStatus
+ __OBJC_CLASS_PROTOCOLS_$_RTAuthorizedLocationStatus
+ __OBJC_CLASS_RO_$_RTAuthorizedLocationStatus
+ __OBJC_METACLASS_RO_$_RTAuthorizedLocationStatus
+ ___37-[RTRoutineManager _createConnection]_block_invoke.341
+ ___38-[RTRoutineManager stopLeechingVisits]_block_invoke.388
+ ___40-[RTRoutineManager stopMonitoringVisits]_block_invoke.387
+ ___42-[RTRoutineManager addElevations:handler:]_block_invoke.452
+ ___49-[RTRoutineManager fetchRoutineStateWithHandler:]_block_invoke.367
+ ___50-[RTRoutineManager fetchAuthorizedLocationStatus:]_block_invoke
+ ___50-[RTRoutineManager fetchAuthorizedLocationStatus:]_block_invoke_2
+ ___50-[RTRoutineManager fetchAuthorizedLocationStatus:]_block_invoke_3
+ ___51-[RTRoutineManager fetchRoutineEnabledWithHandler:]_block_invoke.364
+ ___51-[RTRoutineManager fetchRoutineEnabledWithHandler:]_block_invoke_2.366
+ ___51-[RTRoutineManager stopLeechingLowConfidenceVisits]_block_invoke.389
+ ___53-[RTRoutineManager clearAllVehicleEventsWithHandler:]_block_invoke.418
+ ___53-[RTRoutineManager fetchElevationsWithOptions:reply:]_block_invoke.453
+ ___56-[RTRoutineManager stopMonitoringScenarioTriggerOfType:]_block_invoke.393
+ ___59-[RTRoutineManager enumerateObjectsWithOptions:usingBlock:]_block_invoke.379
+ ___68-[RTRoutineManager _enumerateStoredLocationsWithOptions:usingBlock:]_block_invoke.385
+ ___68-[RTRoutineManager fetchPeopleCountEventsHistory:completionHandler:]_block_invoke.449
+ ___71-[RTRoutineManager fetchContactScoresFromContactIDs:completionHandler:]_block_invoke.451
+ ___72-[RTRoutineManager fetchProximityHistoryFromEventIDs:completionHandler:]_block_invoke.448
+ ___81-[RTRoutineManager fetchProximityHistoryFromStartDate:endDate:completionHandler:]_block_invoke.447
+ ___85-[RTRoutineManager fetchPeopleDensityHistoryFromStartDate:endDate:completionHandler:]_block_invoke.450
+ ___block_descriptor_40_e8_32bs_e48_v24?0"RTAuthorizedLocationStatus"8"NSError"16ls32l8
+ ___block_descriptor_48_e8_32r40r_e29_v24?0"NSArray"8"NSError"16lr32l8r40l8
+ ___block_literal_global.392
+ ___block_literal_global.395
+ ___block_literal_global.446
+ _objc_msgSend$_decodeGeoAddressObjectFromData:decompress:
+ _objc_msgSend$_encodeGeoAddressObject:compress:
+ _objc_msgSend$_mergedThoroughfareWithSubPremises:subThoroughfare:thoroughfare:
+ _objc_msgSend$addressDictionary
+ _objc_msgSend$areaOfInterests
+ _objc_msgSend$compressedDataUsingAlgorithm:error:
+ _objc_msgSend$decompressedDataUsingAlgorithm:error:
+ _objc_msgSend$dictionary
+ _objc_msgSend$eStatus
+ _objc_msgSend$encodedData
+ _objc_msgSend$fetchAuthorizedLocationStatus:
+ _objc_msgSend$finishDecoding
+ _objc_msgSend$finishEncoding
+ _objc_msgSend$fullAddressWithMultiline:
+ _objc_msgSend$fullThoroughfare
+ _objc_msgSend$geoAddressData
+ _objc_msgSend$geoAddressObject
+ _objc_msgSend$initForReadingFromData:error:
+ _objc_msgSend$initRequiringSecureCoding:
+ _objc_msgSend$initWithBundleUUID:startDate:endDate:densityScore:scanDuration:rssiHistogram:
+ _objc_msgSend$initWithContactAddressDictionary:language:country:phoneticLocale:
+ _objc_msgSend$initWithCurrentLocaleFullThoroughfare:subLocality:locality:subAdministrativeArea:administrativeArea:postalCode:country:countryCode:
+ _objc_msgSend$initWithDateInterval:lookbackInterval:spatialGranularity:referenceLocation:referenceLocationSummary:distance:
+ _objc_msgSend$initWithFullThoroughfare:subLocality:locality:subAdministrativeArea:administrativeArea:postalCode:country:countryCode:language:countryLocale:phoneticLocale:
+ _objc_msgSend$initWithIdentifier:geoAddressData:subPremises:isIsland:creationDate:expirationDate:iso3166CountryCode:iso3166SubdivisionCode:
+ _objc_msgSend$initWithIdentifier:geoAddressData:subPremises:subThoroughfare:thoroughfare:subLocality:locality:subAdministrativeArea:administrativeArea:administrativeAreaCode:postalCode:country:countryCode:inlandWater:ocean:areasOfInterest:isIsland:creationDate:expirationDate:iso3166CountryCode:iso3166SubdivisionCode:
+ _objc_msgSend$initWithIdentifier:geoAddressObject:subPremises:isIsland:creationDate:expirationDate:iso3166CountryCode:iso3166SubdivisionCode:
+ _objc_msgSend$initWithIdentifier:name:category:address:location:source:mapItemPlaceType:muid:resultProviderID:geoMapItemHandle:creationDate:expirationDate:extendedAttributes:displayLanguage:disputed:
+ _objc_msgSend$initWithStatus:
+ _objc_msgSend$lookbackInterval
+ _objc_msgSend$mapItemPlaceType
+ _objc_msgSend$postCode
+ _objc_msgSend$preferredLanguages
+ _objc_msgSend$structuredAddress
+ _objc_retain_x5
- -[RTAddress initWithIdentifier:subPremises:subThoroughfare:thoroughfare:subLocality:locality:subAdministrativeArea:administrativeArea:administrativeAreaCode:postalCode:country:countryCode:inlandWater:ocean:areasOfInterest:isIsland:creationDate:expirationDate:iso3166CountryCode:iso3166SubdivisionCode:]
- -[RTFamiliarityIndexOptions initWithDateInterval:spatialGranularity:referenceLocation:referenceLocationSummary:distance:]
- -[RTHangsMetrics init]
- -[RTHangsMetrics submitToCoreAnalytics:type:duration:]
- -[RTMapItem initWithIdentifier:name:category:address:location:source:muid:resultProviderID:geoMapItemHandle:creationDate:expirationDate:extendedAttributes:displayLanguage:disputed:]
- -[RTPeopleDensity initWithBundleUUID:startDate:endDate:densityScore:scanDuration:]
- _AnalyticsSendEvent
- _OBJC_CLASS_$_NSCharacterSet
- _OBJC_CLASS_$_NSPredicate
- _OBJC_CLASS_$_RTHangsMetrics
- _OBJC_METACLASS_$_RTHangsMetrics
- _RTAnalyticsEventHangsMetrics
- _RTLogFacilityMetric
- __OBJC_$_INSTANCE_METHODS_RTHangsMetrics
- __OBJC_CLASS_RO_$_RTHangsMetrics
- __OBJC_METACLASS_RO_$_RTHangsMetrics
- ___37-[RTRoutineManager _createConnection]_block_invoke.337
- ___38-[RTRoutineManager stopLeechingVisits]_block_invoke.387
- ___40-[RTRoutineManager stopMonitoringVisits]_block_invoke.386
- ___42-[RTRoutineManager addElevations:handler:]_block_invoke.450
- ___49-[RTRoutineManager fetchRoutineStateWithHandler:]_block_invoke.363
- ___51-[RTRoutineManager fetchRoutineEnabledWithHandler:]_block_invoke.360
- ___51-[RTRoutineManager fetchRoutineEnabledWithHandler:]_block_invoke_2.362
- ___51-[RTRoutineManager stopLeechingLowConfidenceVisits]_block_invoke.388
- ___53-[RTRoutineManager clearAllVehicleEventsWithHandler:]_block_invoke.416
- ___53-[RTRoutineManager fetchElevationsWithOptions:reply:]_block_invoke.451
- ___56-[RTRoutineManager stopMonitoringScenarioTriggerOfType:]_block_invoke.392
- ___59-[RTRoutineManager enumerateObjectsWithOptions:usingBlock:]_block_invoke.375
- ___68-[RTRoutineManager _enumerateStoredLocationsWithOptions:usingBlock:]_block_invoke.383
- ___68-[RTRoutineManager fetchPeopleCountEventsHistory:completionHandler:]_block_invoke.447
- ___71-[RTRoutineManager fetchContactScoresFromContactIDs:completionHandler:]_block_invoke.449
- ___72-[RTRoutineManager fetchProximityHistoryFromEventIDs:completionHandler:]_block_invoke.446
- ___81-[RTRoutineManager fetchProximityHistoryFromStartDate:endDate:completionHandler:]_block_invoke.445
- ___85-[RTRoutineManager fetchPeopleDensityHistoryFromStartDate:endDate:completionHandler:]_block_invoke.448
- ____RTSemaphoreWait_block_invoke
- ___block_descriptor_32_e31_q24?0"NSString"8"NSString"16l
- ___block_descriptor_32_e35_B24?0"NSString"8"NSDictionary"16l
- ___block_descriptor_56_e8_32r40r48r_e29_v24?0"NSArray"8"NSError"16lr32l8r40l8r48l8
- ___block_literal_global.391
- ___block_literal_global.394
- ___block_literal_global.418
- ___block_literal_global.630
- ___log_analytics_submission_block_invoke
- _dispatch_queue_get_label
- _dispatch_semaphore_create
- _dispatch_semaphore_signal
- _dispatch_semaphore_wait
- _dispatch_time
- _log_analytics_submission
- _objc_msgSend$_queue
- _objc_msgSend$appendFormat:
- _objc_msgSend$characterSetWithCharactersInString:
- _objc_msgSend$componentsSeparatedByCharactersInSet:
- _objc_msgSend$containsString:
- _objc_msgSend$filteredArrayUsingPredicate:
- _objc_msgSend$initWithBundleUUID:startDate:endDate:densityScore:scanDuration:
- _objc_msgSend$initWithCString:encoding:
- _objc_msgSend$initWithDateInterval:spatialGranularity:referenceLocation:referenceLocationSummary:distance:
- _objc_msgSend$initWithIdentifier:name:category:address:location:source:muid:resultProviderID:geoMapItemHandle:creationDate:expirationDate:extendedAttributes:displayLanguage:disputed:
- _objc_msgSend$initWithIdentifier:subPremises:subThoroughfare:thoroughfare:subLocality:locality:subAdministrativeArea:administrativeArea:administrativeAreaCode:postalCode:country:countryCode:inlandWater:ocean:areasOfInterest:isIsland:creationDate:expirationDate:iso3166CountryCode:iso3166SubdivisionCode:
- _objc_msgSend$now
- _objc_msgSend$predicateWithBlock:
- _objc_msgSend$sortedArrayUsingComparator:
- _objc_msgSend$stringWithCString:encoding:
- _objc_msgSend$submitToCoreAnalytics:type:duration:
CStrings:
+ "\x03!"
+ "\x0e\x17"
+ "\x12\x135"
+ "%@ %@, %@ %@ %@ (%@, %@, legacy)"
+ "%@ (%@, %@, GEOAddressObject)"
+ "%@, %@, [NSLocale currentLocale] failed for NSLocaleCountryCode"
+ "-[RTRoutineManager fetchAuthorizedLocationStatus:]"
+ "@\"GEOAddressObject\""
+ "@104@0:8@16@24@32@40@48@56@64@72@80@88@96"
+ "@132@0:8@16@24@32@40@48Q56Q64Q72q80@88@96@104@112@120B128"
+ "@180@0:8@16@24@32@40@48@56@64@72@80@88@96@104@112@120@128@136B144@148@156@164@172"
+ "@60@0:8@16d24Q32@40B48d52"
+ "@64@0:8@16@24@32d40d48@56"
+ "@76@0:8@16@24@32B40@44@52@60@68"
+ "@80@0:8@16@24@32@40@48@56@64@72"
+ "Admin"
+ "AdministrativeArea"
+ "Building"
+ "City"
+ "Confirmed."
+ "Continent"
+ "Country"
+ "CountryCode"
+ "Division"
+ "InlandWater"
+ "Intersection"
+ "Invalid parameter not satisfying: geoAddressObject"
+ "Invalid."
+ "Island"
+ "Locality"
+ "Not confirmed."
+ "Ocean"
+ "Postal"
+ "Q40@0:8@16Q24Q32"
+ "RTAuthorizedLocationStatus"
+ "RTFamiliarityIndexErrorDomain"
+ "Region"
+ "ReverseGeocodeRelatedPlaces"
+ "State"
+ "Street"
+ "SubAdministrativeArea"
+ "SubLocality"
+ "T@\"NSArray\",R,N"
+ "T@\"NSData\",R,C,N,V_geoAddressData"
+ "T@\"NSDictionary\",R,N,V_rssiHistogram"
+ "T@\"NSString\",R,C,N"
+ "TQ,R,N,V_mapItemPlaceType"
+ "Td,R,N,V_lookbackInterval"
+ "TimeZone"
+ "Tq,R,V_eStatus"
+ "Unavailable."
+ "Undefined"
+ "ZIP"
+ "_decodeGeoAddressObjectFromData:decompress:"
+ "_eStatus"
+ "_encodeGeoAddressObject:compress:"
+ "_geoAddressData"
+ "_localGeoAddressObject"
+ "_lookbackInterval"
+ "_mapItemPlaceType"
+ "_mergedThoroughfareWithSubPremises:subThoroughfare:thoroughfare:"
+ "_rssiHistogram"
+ "addressDictionary"
+ "areaOfInterests"
+ "compressedDataUsingAlgorithm:error:"
+ "dateInterval, %@, lookbackInterval, %.2f, spatialGranularity, %lu, referenceLocation, %@, referenceLocationSummary, %d, distance, %.2f"
+ "decompressedDataUsingAlgorithm:error:"
+ "dictionary"
+ "eStatus"
+ "encodedData"
+ "error decoding geoAddressData, %@"
+ "fetchAuthorizedLocationStatus:"
+ "finishDecoding"
+ "finishEncoding"
+ "fullAddressWithMultiline:"
+ "fullThoroughfare"
+ "geoAddress"
+ "geoAddressData"
+ "geoAddressObject"
+ "geoDictionaryRepresentation"
+ "identifier, %@, name, \"%@\", category, %@, address, %@, location, %@, source, %@, map item place type, %@, muid, %lu, result provider ID: %ld, weight, %lf, creationDate, %@, extended attributes, %@, display language, %@, disputed, %@"
+ "initForReadingFromData:error:"
+ "initRequiringSecureCoding:"
+ "initWithBundleUUID:startDate:endDate:densityScore:scanDuration:rssiHistogram:"
+ "initWithContactAddressDictionary:language:country:phoneticLocale:"
+ "initWithCurrentLocaleFullThoroughfare:subLocality:locality:subAdministrativeArea:administrativeArea:postalCode:country:countryCode:"
+ "initWithDateInterval:lookbackInterval:spatialGranularity:referenceLocation:referenceLocationSummary:distance:"
+ "initWithFullThoroughfare:subLocality:locality:subAdministrativeArea:administrativeArea:postalCode:country:countryCode:language:countryLocale:phoneticLocale:"
+ "initWithGeoDictionary:language:country:phoneticLocale:"
+ "initWithIdentifier:geoAddressData:subPremises:isIsland:creationDate:expirationDate:iso3166CountryCode:iso3166SubdivisionCode:"
+ "initWithIdentifier:geoAddressData:subPremises:subThoroughfare:thoroughfare:subLocality:locality:subAdministrativeArea:administrativeArea:administrativeAreaCode:postalCode:country:countryCode:inlandWater:ocean:areasOfInterest:isIsland:creationDate:expirationDate:iso3166CountryCode:iso3166SubdivisionCode:"
+ "initWithIdentifier:geoAddressObject:subPremises:isIsland:creationDate:expirationDate:iso3166CountryCode:iso3166SubdivisionCode:"
+ "initWithIdentifier:name:category:address:location:source:mapItemPlaceType:muid:resultProviderID:geoMapItemHandle:creationDate:expirationDate:extendedAttributes:displayLanguage:disputed:"
+ "initWithStatus:"
+ "lookbackInterval"
+ "mapItemPlaceType"
+ "placeInferencePlaceTypeFromMapItem:userType:source:"
+ "postCode"
+ "preferredLanguages"
+ "rssiHistogram"
+ "status,%ld,statusString,%@"
+ "structuredAddress"
+ "v24@0:8@?<v@?@\"RTAuthorizedLocationStatus\"@\"NSError\">16"
+ "v24@?0@\"RTAuthorizedLocationStatus\"8@\"NSError\"16"
- "\n=== BEGIN analytics submission for event %@ ===\n"
- "\x11\x11"
- "\x12\x13%"
- "\x1f\x04"
- "%@ %@, %@ %@ %@ (%@, %@)"
- "%@ : %@\n"
- "%@ XPC Connection wasn't to use self.queue. (in %s:%d)"
- "- "
- "=== END analytics submission for event %@ ===\n"
- "@124@0:8@16@24@32@40@48Q56Q64q72@80@88@96@104@112B120"
- "@172@0:8@16@24@32@40@48@56@64@72@80@88@96@104@112@120@128B136@140@148@156@164"
- "@52@0:8@16Q24@32B40d44"
- "@56@0:8@16@24@32d40d48"
- "B24@?0@\"NSString\"8@\"NSDictionary\"16"
- "CoreRoutine.HangsMetrics"
- "METRIC"
- "RT"
- "RTHangsMetrics"
- "Semaphore wait timed out, we're hung!"
- "T@\"NSArray\",R,N,V_areasOfInterest"
- "T@\"NSString\",R,C,N,V_administrativeArea"
- "T@\"NSString\",R,C,N,V_administrativeAreaCode"
- "T@\"NSString\",R,C,N,V_country"
- "T@\"NSString\",R,C,N,V_countryCode"
- "T@\"NSString\",R,C,N,V_inlandWater"
- "T@\"NSString\",R,C,N,V_locality"
- "T@\"NSString\",R,C,N,V_ocean"
- "T@\"NSString\",R,C,N,V_postalCode"
- "T@\"NSString\",R,C,N,V_subAdministrativeArea"
- "T@\"NSString\",R,C,N,V_subLocality"
- "T@\"NSString\",R,C,N,V_subThoroughfare"
- "T@\"NSString\",R,C,N,V_thoroughfare"
- "XPC timeout error while waiting for stored locations, %@."
- "appendFormat:"
- "characterSetWithCharactersInString:"
- "com.apple.%@"
- "componentsSeparatedByCharactersInSet:"
- "containsString:"
- "dateInterval, %@, spatialGranularity, %lu, referenceLocation, %@, referenceLocationSummary, %d, distance, %.2f"
- "fetchLocationsHelperQueue"
- "filteredArrayUsingPredicate:"
- "hangDuration"
- "hangType"
- "hungObject"
- "hungQueue"
- "identifier, %@, name, \"%@\", category, %@, address, %@, location, %@, source, %@, muid, %lu, result provider ID: %ld, weight, %lf, creationDate, %@, extended attributes, %@, display language, %@, disputed, %@"
- "initWithBundleUUID:startDate:endDate:densityScore:scanDuration:"
- "initWithCString:encoding:"
- "initWithDateInterval:spatialGranularity:referenceLocation:referenceLocationSummary:distance:"
- "initWithIdentifier:name:category:address:location:source:muid:resultProviderID:geoMapItemHandle:creationDate:expirationDate:extendedAttributes:displayLanguage:disputed:"
- "initWithIdentifier:subPremises:subThoroughfare:thoroughfare:subLocality:locality:subAdministrativeArea:administrativeArea:administrativeAreaCode:postalCode:country:countryCode:inlandWater:ocean:areasOfInterest:isIsland:creationDate:expirationDate:iso3166CountryCode:iso3166SubdivisionCode:"
- "now"
- "predicateWithBlock:"
- "q24@?0@\"NSString\"8@\"NSString\"16"
- "received error while getting [SYNC] asynchronous proxy to enumerate stored locations, %@."
- "semaphore wait timeout"
- "sortedArrayUsingComparator:"
- "stringWithCString:encoding:"
- "submitToCoreAnalytics:type:duration:"
- "v40@0:8@16q24d32"

```
