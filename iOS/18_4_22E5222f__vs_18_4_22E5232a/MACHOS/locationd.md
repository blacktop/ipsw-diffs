## locationd

> `/usr/libexec/locationd`

```diff

-2960.0.55.2.0
-  __TEXT.__text: 0x1ad6c0c
-  __TEXT.__auth_stubs: 0x6050
-  __TEXT.__objc_stubs: 0x42860
+2960.0.58.0.0
+  __TEXT.__text: 0x1ad833c
+  __TEXT.__auth_stubs: 0x60a0
+  __TEXT.__objc_stubs: 0x42880
   __TEXT.__init_offsets: 0xb30
-  __TEXT.__objc_methlist: 0x2f018
-  __TEXT.__const: 0x1503d9
-  __TEXT.__cstring: 0x1d9b1c
-  __TEXT.__gcc_except_tab: 0xde9e0
-  __TEXT.__objc_methname: 0x5fd8b
-  __TEXT.__oslogstring: 0x274db7
+  __TEXT.__objc_methlist: 0x2f030
+  __TEXT.__const: 0x1503e9
+  __TEXT.__cstring: 0x1d9b65
+  __TEXT.__gcc_except_tab: 0xdeaa4
+  __TEXT.__objc_methname: 0x5fe2b
+  __TEXT.__oslogstring: 0x275834
   __TEXT.__objc_classname: 0x7b83
   __TEXT.__objc_methtype: 0x4063e
   __TEXT.__constg_swiftt: 0x204

   __TEXT.__swift5_reflstr: 0x29
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_capture: 0x40
-  __TEXT.__unwind_info: 0x6f230
+  __TEXT.__unwind_info: 0x6f260
   __TEXT.__eh_frame: 0x1370
-  __DATA_CONST.__auth_got: 0x3048
+  __DATA_CONST.__auth_got: 0x3070
   __DATA_CONST.__got: 0x2d08
   __DATA_CONST.__auth_ptr: 0x340
   __DATA_CONST.__const: 0xb1528
-  __DATA_CONST.__cfstring: 0x420a0
+  __DATA_CONST.__cfstring: 0x420c0
   __DATA_CONST.__objc_classlist: 0x1458
   __DATA_CONST.__objc_catlist: 0xc8
   __DATA_CONST.__objc_protolist: 0xd98

   __DATA_CONST.__objc_arrayobj: 0x870
   __DATA_CONST.__objc_floatobj: 0x80
   __DATA_CONST.__linkguard: 0x15
-  __DATA.__objc_const: 0x4d5b8
-  __DATA.__objc_selrefs: 0x14c28
-  __DATA.__objc_ivar: 0x38f4
+  __DATA.__objc_const: 0x4d5e8
+  __DATA.__objc_selrefs: 0x14c38
+  __DATA.__objc_ivar: 0x38f8
   __DATA.__objc_data: 0xcdb8
   __DATA.__data: 0x614e8
   __DATA.__common: 0x3fd0
-  __DATA.__bss: 0xf550
+  __DATA.__bss: 0xf558
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/ActivityKit.framework/ActivityKit

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 100701
-  Symbols:   3063
-  CStrings:  83104
+  Functions: 100707
+  Symbols:   3068
+  CStrings:  83112
 
Symbols:
+ _CLLogEncryptData
+ _CLLogEncryptDataSize
+ _CLLogEncryptionClearObsoleteKeys
+ _CLLogEncryptionInit
+ _CLLogEncryptionSetDisabled
CStrings:
+ "#Pinning per-app prompts are not allowed when LocationPinning is enabled."
+ "/AppleInternal/Library/BuildRoots/d6c8d13a-ff2c-11ef-b4ee-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.4.Internal.sdk/usr/local/include/boost/geometry/algorithms/detail/throw_on_empty_input.hpp"
+ "/AppleInternal/Library/BuildRoots/d6c8d13a-ff2c-11ef-b4ee-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.4.Internal.sdk/usr/local/include/boost/uuid/detail/random_provider_posix.ipp"
+ "/AppleInternal/Library/BuildRoots/d6c8d13a-ff2c-11ef-b4ee-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.4.Internal.sdk/usr/local/include/boost/uuid/string_generator.hpp"
+ "/AppleInternal/Library/BuildRoots/d6c8d13a-ff2c-11ef-b4ee-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.4.Internal.sdk/usr/local/include/google/protobuf/repeated_field.h"
+ "/AppleInternal/Library/BuildRoots/d6c8d13a-ff2c-11ef-b4ee-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.4.Internal.sdk/usr/local/include/google/protobuf/wire_format_lite_inl.h"
+ "22:33:02"
+ "22:53:18"
+ "DisableLogEncryption"
+ "Mar 12 2025"
+ "Mar 12 2025 22:36:14"
+ "MinimumTimeBetweenExpensiveQueries"
+ "Td,N,V_minTimeBetweenExpensiveQueries"
+ "_minTimeBetweenExpensiveQueries"
+ "handleNewLocation:shouldUpdateTerritories:"
+ "log_encryption_keys"
+ "minTimeBetweenExpensiveQueries"
+ "setMinTimeBetweenExpensiveQueries:"
+ "{\"msg%{public}.0s\":\"#EED2 created location dict\", \"timestamp\":%{public}lld, \"lat\":%{public, location:Encrypted_latitude}.*P, \"lon\":%{public, location:Encrypted_longitude}.*P, \"altitude (HAE)\":\"%{sensitive}.2f\", \"hunc\":\"%{public}f\", \"vunc\":\"%{public}f\"}"
+ "{\"msg%{public}.0s\":\"#GnssRefLocationCache,Warning invalid assistance location,invalid coordinates\", \"lat\":%{public, location:Encrypted_latitude}.*P, \"lon\":%{public, location:Encrypted_longitude}.*P}"
+ "{\"msg%{public}.0s\":\"#GnssRefLocationCache,feedRefLocationFromRefPosMaintenance\", \"type\":%{public}d, \"timestamp\":\"%{public}.1f\", \"cacheTimestamp\":\"%{public}.1f\", \"lat\":%{public, location:Encrypted_latitude}.*P, \"lon\":%{public, location:Encrypted_longitude}.*P, \"hacc\":\"%{public}.1f\", \"alt\":\"%{private}.2f\", \"vunc\":\"%{public}.1f\"}"
+ "{\"msg%{public}.0s\":\"#SLC Got location\", \"location\":%{public, location:Encrypted_CLClientLocation}.*P}"
+ "{\"msg%{public}.0s\":\"#SLC location changed\", \"now_s\":\"%{public}.09f\", \"location\":%{public, location:Encrypted_CLClientLocation}.*P, \"distance\":\"%{private}f\"}"
+ "{\"msg%{public}.0s\":\"#SPI getLocation #cclp\", \"gotLocation\":%{public}hhd, \"location\":%{public, location:Encrypted_CLClientLocation}.*P}"
+ "{\"msg%{public}.0s\":\"#Spi, altered getLocation\", \"location\":%{public, location:Encrypted_CLClientLocation}.*P, \"timestampGps\":\"%{private}f\", \"machTime\":\"%{private}f\", \"gotLocation\":%{private}hhd, \"specialCoordinateLat\":%{public, location:Encrypted_latitude}.*P, \"specialCoordinateLon\":%{public, location:Encrypted_longitude}.*P, \"specialHorizontalAccuracy\":\"%{private}f\"}"
+ "{\"msg%{public}.0s\":\"#awd #thumper Caching location \", \"lat\":%{public, location:Encrypted_latitude}.*P, \"lon\":%{public, location:Encrypted_longitude}.*P, \"alt\":\"%{private}f\", \"accuracy\":\"%{private}f\"}"
+ "{\"msg%{public}.0s\":\"#awd #thumper location log\", \"lat\":%{public, location:Encrypted_latitude}.*P, \"lon\":%{public, location:Encrypted_longitude}.*P, \"alt\":\"%{private}f\", \"accuracy\":\"%{private}f\", \"source\":%{private}u}"
+ "{\"msg%{public}.0s\":\"#cclp UpdateLastReceivedLocationTimer fired. Using location\", \"location\":%{public, location:Encrypted_CLClientLocation}.*P}"
+ "{\"msg%{public}.0s\":\"#cclp onLocationNotification\", \"Notification\":%{public, location:escape_only}s, \"location\":%{public, location:Encrypted_CLClientLocation}.*P}"
+ "{\"msg%{public}.0s\":\"#cclp passing cached location to reply\", \"location\":%{public, location:Encrypted_CLClientLocation}.*P}"
+ "{\"msg%{public}.0s\":\"#cclp perform snapping on location by LC\", \"location\":%{public, location:Encrypted_CLClientLocation}.*P}"
+ "{\"msg%{public}.0s\":\"#cclp snapLocation reply\", \"permanent\":%{public}hhd, \"cacheAge\":\"%{public}f\", \"cacheAgeLessThanExtendedInterval\":%{public}hhd, \"hasCachedLocation\":%{public}hhd, \"location\":%{public, location:Encrypted_CLClientLocation}.*P}"
+ "{\"msg%{public}.0s\":\"#circularGeographicCondition created\", \"coordinate\":%{public, location:Encrypted_CLLocationCoordinate2D}.*P, \"radius\":\"%{public}f\", \"identifier\":%{public, location:escape_only}@, \"removePersistingFenceFromMonitoring\":%{public}hhd, \"self\":\"%{public}p\"}"
+ "{\"msg%{public}.0s\":\"#clcac location not specified. NonZonal-AC differs from Zonal-AC at current-location. Showing location-arrow\", \"Client\":%{public, location:escape_only}s, \"CLCAC-currentLocation\":%{public, location:Encrypted_CLClientLocation}.*P, \"NonZonalAC\":%{public, location:escape_only}@, \"ZonalAC\":%{public, location:escape_only}@}"
+ "{\"msg%{public}.0s\":\"#clcac location not specified. NonZonal-AC is same as Zonal-AC at current-location. Skip showing location-arrow\", \"Client\":%{public, location:escape_only}s, \"CLCAC-currentLocation\":%{public, location:Encrypted_CLClientLocation}.*P}"
+ "{\"msg%{public}.0s\":\"#cms mode init visit\", \"\"visit\".coordinate.latitude\":%{public, location:Encrypted_latitude}.*P, \"\"visit\".coordinate.longitude\":%{public, location:Encrypted_longitude}.*P, \"\"visit\".hAcc\":\"%{public}f\", \"\"visit\".arrival\":%{private, location:escape_only}@, \"\"visit\".departure\":%{private, location:escape_only}@, \"\"visit\".placeInference\":%{sensitive, location:escape_only}@, \"entry\":%{public}hhd}"
+ "{\"msg%{public}.0s\":\"#gnss DOT\", \"lat\":%{public, location:Encrypted_latitude}.*P, \"lon\":%{public, location:Encrypted_longitude}.*P, \"directionOfTravel\":%{public}d, \"directionOfTravelUnc\":%{public}d, \"roadWidth\":%{public}d, \"startLatitude\":\"%{private}.08f\", \"startLongitude\":\"%{private}.08f\", \"lengthOfLinearSegment\":%{public}d, \"machtime\":%{public}d}"
+ "{\"msg%{public}.0s\":\"#gnss MMP\", \"lat\":%{public, location:Encrypted_latitude}.*P, \"lon\":%{public, location:Encrypted_longitude}.*P, \"uncEllipseSemiMajor\":%{public}d, \"uncEllipseSemiMinor\":%{public}d, \"uncEllipseAzimuth\":%{public}d}"
+ "{\"msg%{public}.0s\":\"#gnssawd GnssSessionData log\", \"sessionDuration\":%{private}lld, \"fEpochCount\":%{private}lld, \"yieldCount\":%{private}lld, \"lat\":%{public, location:Encrypted_latitude}.*P, \"lon\":%{public, location:Encrypted_longitude}.*P, \"alt\":\"%{private}f\", \"accuracy\":\"%{private}f\", \"ttff\":%{private}d, \"mcc\":%{private}d, \"mnc\":%{private}d, \"sid\":%{private}d, \"nid\":%{private}d, \"transFreq\":\"%{private}f\", \"transBW\":\"%{private}f\", \"transBand\":%{private}d, \"isEmergency\":%{private}d}"
+ "{\"msg%{public}.0s\":\"#luHistorical specified Center is not valid\", \"ClientKeyPath\":%{public, location:escape_only}@, \"self\":\"%{public}p\", \"Center.lat\":%{public, location:Encrypted_latitude}.*P, \"Center.lon\":%{public, location:Encrypted_longitude}.*P}"
+ "{\"msg%{public}.0s\":\"#luLive locationData does not have any entries\", \"ClientKeyPath\":%{public, location:escape_only}@, \"self\":\"%{public}p\", \"locationCountAfterSerialization\":%{public}d, \"location\":%{public, location:Encrypted_CLClientLocation}.*P}"
+ "{\"msg%{public}.0s\":\"#luLive sending location\", \"ClientKeyPath\":%{public, location:escape_only}@, \"self\":\"%{public}p\", \"locationCountAfterSerialization\":%{public}d, \"location\":%{public, location:Encrypted_CLClientLocation}.*P}"
+ "{\"msg%{public}.0s\":\"#luLive unmarking #stationary by location-wandering\", \"ClientKeyPath\":%{public, location:escape_only}@, \"self\":\"%{public}p\", \"wander\":\"%{public}f\", \"OldTS\":\"%{public}f\", \"NewTS\":\"%{public}f\", \"refLat\":%{public, location:Encrypted_latitude}.*P, \"refLon\":%{public, location:Encrypted_longitude}.*P, \"lat\":%{public, location:Encrypted_latitude}.*P, \"lon\":%{public, location:Encrypted_longitude}.*P}"
+ "{\"msg%{public}.0s\":\"#msim performCellHarvesting\", \"subHarvester\":%{public, location:CLSubHarvesterIdentifier}lld, \"SimInstance\":%{public}u, \"location\":%{public, location:Encrypted_CLClientLocation}.*P}"
+ "{\"msg%{public}.0s\":\"#pla #zone-relevance-tracker for circular-region\", \"monitoring\":%{public, location:escape_only}s, \"lat\":%{public, location:Encrypted_latitude}.*P, \"lon\":%{public, location:Encrypted_longitude}.*P, \"radius\":\"%{public}.3f\", \"Client\":%{public, location:escape_only}s, \"ZoneId\":%{public, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#pla #zone-relevance-tracker, location notification\", \"notification\":%{public, location:CLLocationProvider_Type::Notification}lld, \"_currentLocation\":%{public, location:Encrypted_CLClientLocation}.*P, \"NewLocation\":%{public, location:Encrypted_CLClientLocation}.*P}"
+ "{\"msg%{public}.0s\":\"#pla Skip #clldu-MarkZonesAsRelevant. Invalid location\", \"dictionary\":%{public, location:escape_only}@, \"location\":%{public, location:Encrypted_CLClientLocation}.*P}"
+ "{\"msg%{public}.0s\":\"#pla freshAuthorizationContext location updated\", \"Client\":%{public, location:escape_only}@, \"provided-location\":%{public, location:Encrypted_CLClientLocation}.*P, \"fetched-location-ZRT\":%{public, location:Encrypted_CLClientLocation}.*P}"
+ "{\"msg%{public}.0s\":\"Adding geographic fence\", \"onBehalf\":%{public, location:escape_only}s, \"clientKey\":%{public, location:escape_only}s, \"fenceName\":%{private, location:escape_only}s, \"center.latitude\":%{public, location:Encrypted_latitude}.*P, \"center.longitude\":%{public, location:Encrypted_longitude}.*P, \"radius\":\"%{public}f\", \"desiredAccuracy\":\"%{public}f\"}"
+ "{\"msg%{public}.0s\":\"Appending location\", \"location\":%{public, location:Encrypted_CLClientLocation}.*P}"
+ "{\"msg%{public}.0s\":\"CLDaemonLocationUpdaterHistorical(ctor) #luHistorical\", \"event\":%{public, location:escape_only}s, \"ClientKeyPath\":%{public, location:escape_only}@, \"this\":\"%{public}p\", \"SampleCount\":%{public}d, \"Radius\":\"%{public}f\", \"DateInterval\":%{public, location:escape_only}@, \"CenterSpecified\":%{public}hhd, \"Center.lat\":%{public, location:Encrypted_latitude}.*P, \"Center.lon\":%{public, location:Encrypted_longitude}.*P}"
+ "{\"msg%{public}.0s\":\"GPSODOM\", \"event\":%{public, location:escape_only}s, \"gpsNs\":%{public}lld, \"cfTime\":\"%{public}f\", \"cfTimeGps\":\"%{public}f\", \"machTime\":\"%{public}f\", \"machContinuousTime\":\"%{public}f\", \"posValid\":%{public}hhd, \"lat\":%{public, location:Encrypted_latitude}.*P, \"lon\":%{public, location:Encrypted_longitude}.*P, \"altitude\":\"%{private}f\", \"undulation\":\"%{public}f\", \"hunc\":\"%{public}f\", \"vunc\":\"%{public}f\", \"semiMaj\":\"%{public}f\", \"semiMin\":\"%{public}f\", \"semiMajAz\":\"%{public}f\", \"reliability\":%{public}d, \"speedValid\":%{public}hhd, \"speed\":\"%{public}f\", \"speedUnc\":\"%{public}f\", \"courseValid\":%{public}hhd, \"course\":\"%{public}f\", \"courseUnc\":\"%{public}f\", \"gnssContent\":%{public}d, \"ravenPosUsed\":%{public}hhd, \"odometry\":\"%{public}f\", \"deltaDist\":\"%{public}f\", \"deltaDistUnc\":\"%{public}f\", \"odometryValid\":%{public}hhd}"
+ "{\"msg%{public}.0s\":\"GnssEvent\", \"event\":%{public, location:escape_only}s, \"gpsNs\":%{public}lld, \"gpsTimeUncMs\":\"%{public}f\", \"cfTime\":\"%{public}f\", \"cfTimeGps\":\"%{public}f\", \"machTime\":\"%{public}f\", \"machContinuousTime\":\"%{public}f\", \"leapSeconds\":%{public}d, \"posValid\":%{public}hhd, \"lat\":%{public, location:Encrypted_latitude}.*P, \"lon\":%{public, location:Encrypted_longitude}.*P, \"altitude\":\"%{private}f\", \"undulation\":\"%{public}f\", \"undulationModel\":%{public}d, \"hunc\":\"%{public}f\", \"vunc\":\"%{public}f\", \"semiMaj\":\"%{public}f\", \"semiMin\":\"%{public}f\", \"semiMajAz\":\"%{public}f\", \"reliability\":%{public}d, \"speedValid\":%{public}hhd, \"speed\":\"%{public}f\", \"speedUnc\":\"%{public}f\", \"courseValid\":%{public}hhd, \"course\":\"%{public}f\", \"courseUnc\":\"%{public}f\", \"imag\":%{public}d, \"gnssContent\":%{public}d}"
+ "{\"msg%{public}.0s\":\"GnssEvent\", \"event\":%{public, location:escape_only}s, \"location\":%{public, location:Encrypted_CLClientLocation}.*P, \"isIndia\":%{private}hhd, \"isCPI\":%{public}hhd}"
+ "{\"msg%{public}.0s\":\"GnssEvent\", \"event\":%{public, location:escape_only}s, \"timestamp\":\"%{public}f\", \"lat\":%{public, location:Encrypted_latitude}.*P, \"lon\":%{public, location:Encrypted_longitude}.*P, \"directionOfTravel\":\"%{public}f\", \"directionOfTravelUnc\":\"%{public}f\", \"roadWidth\":\"%{public}f\", \"startLatitude\":\"%{private}.08f\", \"startLongitude\":\"%{private}.08f\", \"lengthOfLinearSegment\":\"%{public}f\", \"machtime\":\"%{public}f\"}"
+ "{\"msg%{public}.0s\":\"GnssEvent\", \"event\":%{public, location:escape_only}s, \"timestamp\":\"%{public}f\", \"lat\":%{public, location:Encrypted_latitude}.*P, \"lon\":%{public, location:Encrypted_longitude}.*P, \"uncEllipseSemiMajor\":\"%{public}f\", \"uncEllipseSemiMinor\":\"%{public}f\", \"uncEllipseAzimuth\":\"%{public}f\"}"
+ "{\"msg%{public}.0s\":\"Harvest-Collect\", \"subHarvester\":%{public, location:CLSubHarvesterIdentifier}lld, \"location\":%{public, location:Encrypted_CLClientLocation}.*P, \"tripId\":%{private, location:escape_only}s, \"rat\":%{private}d, \"mcc\":%{private}d, \"mnc\":%{private}d, \"motionVehicleConnectedStateChanged\":%{private}d, \"motionVehicleConnected\":%{private}d, \"rawMotionActivity\":%{private, location:CLMotionActivity}.*P, \"motionActivity\":%{private, location:CLMotionActivity}.*P, \"dominantMotionActivity\":%{private, location:CLMotionActivity}.*P, \"isProactiveLocationSession\":%{private}d}"
+ "{\"msg%{public}.0s\":\"Harvest-Database-Collect\", \"subHarvester\":%{public, location:CLSubHarvesterIdentifier}lld, \"location\":%{public, location:Encrypted_CLClientLocation}.*P}"
+ "{\"msg%{public}.0s\":\"Invalid batched location\", \"location\":%{public, location:Encrypted_CLClientLocation}.*P}"
+ "{\"msg%{public}.0s\":\"Location #compensation Snapping\", \"Input\":%{public, location:Encrypted_CLClientLocation}.*P, \"Output\":%{public, location:Encrypted_CLClientLocation}.*P, \"distance\":\"%{public}f\", \"GeoResultCode\":%{public}ld}"
+ "{\"msg%{public}.0s\":\"Location #compensation gonna be Snapping\", \"Input\":%{public, location:Encrypted_CLClientLocation}.*P}"
+ "{\"msg%{public}.0s\":\"Notify location is\", \"location\":%{public, location:Encrypted_CLClientLocation}.*P}"
+ "{\"msg%{public}.0s\":\"Notifying clients with location\", \"location\":%{public, location:Encrypted_CLClientLocation}.*P, \"notification\":%{public, location:CLLocationProvider_Type::Notification}lld}"
+ "{\"msg%{public}.0s\":\"Reached location, preparing next\", \"reachedLat\":%{public, location:Encrypted_latitude}.*P, \"reachedLon\":%{public, location:Encrypted_longitude}.*P}"
+ "{\"msg%{public}.0s\":\"Sending location to client\", \"Client\":%{public, location:escape_only}@, \"DC\":\"%{public}p\", \"location\":%{public, location:Encrypted_CLClientLocation}.*P, \"desiredAccuracy\":\"%{public}f\"}"
+ "{\"msg%{public}.0s\":\"Using simulated location from defaults\", \"location\":%{public, location:Encrypted_CLClientLocation}.*P}"
+ "{\"msg%{public}.0s\":\"[LOI] Received a location\", \"location\":%{public, location:Encrypted_CLClientLocation}.*P}"
+ "{\"msg%{public}.0s\":\"applying bounding-box-specific overrides\", \"lat\":%{public, location:Encrypted_latitude}.*P, \"lon\":%{public, location:Encrypted_longitude}.*P, \"latMin\":%{public, location:Encrypted_latitude}.*P, \"lonMin\":%{public, location:Encrypted_longitude}.*P, \"latMax\":%{public, location:Encrypted_latitude}.*P, \"lonMax\":%{public, location:Encrypted_longitude}.*P}"
+ "{\"msg%{public}.0s\":\"checking distance to visit\", \"lat\":%{public, location:Encrypted_latitude}.*P, \"lon\":%{public, location:Encrypted_longitude}.*P}"
+ "{\"msg%{public}.0s\":\"computed deltas\", \"deltaR\":\"%{public}f\", \"deltaT\":\"%{public}f\", \"debounceTime\":\"%{public}f\", \"staleTime\":\"%{public}f\", \"prevCoordinate\":%{public, location:Encrypted_CLLocationCoordinate2D}.*P}"
+ "{\"msg%{public}.0s\":\"computing #clldu freshAuthContext\", \"EffectiveRegistration\":%{public, location:CLClientRegistrationResult}lld, \"TransientRegistration\":%{public, location:CLClientRegistrationResult}lld, \"bigSwitchState\":%{public}hhd, \"isClientZonal\":%{public}hhd, \"location\":%{public, location:Encrypted_CLClientLocation}.*P, \"dictionary\":%{public, location:escape_only}@}"
+ "{\"msg%{public}.0s\":\"faraway location encountered\", \"time_s\":\"%{public}.09f\", \"distance\":\"%{public}.2f\", \"lat\":%{public, location:Encrypted_latitude}.*P, \"lon\":%{public, location:Encrypted_longitude}.*P}"
+ "{\"msg%{public}.0s\":\"fetch estimated device location at BA location time\", \"lat\":%{public, location:Encrypted_latitude}.*P, \"lng\":%{public, location:Encrypted_longitude}.*P, \"ucc\":%{private}d, \"subHarvester\":%{public, location:CLSubHarvesterIdentifier}lld}"
+ "{\"msg%{public}.0s\":\"fetchRoutineLoiType\", \"subHarvester\":%{public, location:CLSubHarvesterIdentifier}lld, \"location\":%{public, location:Encrypted_CLClientLocation}.*P, \"loiType\":%{private, location:RTLocationOfInterestType}lld}"
+ "{\"msg%{public}.0s\":\"fetchRoutineMode\", \"subHarvester\":%{public, location:CLSubHarvesterIdentifier}lld, \"location\":%{public, location:Encrypted_CLClientLocation}.*P, \"routineMode\":%{private, location:RTRoutineMode}lld}"
+ "{\"msg%{public}.0s\":\"find nearest location\", \"lat\":%{public, location:Encrypted_latitude}.*P, \"lng\":%{public, location:Encrypted_longitude}.*P, \"ucc\":%{private}d, \"time interval\":%{private}d, \"subHarvester\":%{public, location:CLSubHarvesterIdentifier}lld}"
+ "{\"msg%{public}.0s\":\"ignoring since accuracy is too large\", \"subHarvester\":%{public, location:CLSubHarvesterIdentifier}lld, \"lat\":%{public, location:Encrypted_latitude}.*P, \"lon\":%{public, location:Encrypted_longitude}.*P, \"horizontalAccuracy\":\"%{private}f\"}"
+ "{\"msg%{public}.0s\":\"isInside\", \"fZoneId\":%{private}d, \"minLat\":\"%{private}f\", \"maxLat\":\"%{private}f\", \"minLon\":\"%{private}f\", \"maxLon\":\"%{private}f\", \"latitude\":%{public, location:Encrypted_latitude}.*P, \"longitude\":%{public, location:Encrypted_longitude}.*P, \"isInsize\":%{private}hhd}"
+ "{\"msg%{public}.0s\":\"location is filtered due to lack of additional information\", \"lat\":%{public, location:Encrypted_latitude}.*P, \"lng\":%{public, location:Encrypted_longitude}.*P, \"ucc\":%{private}d, \"timestamp\":%{private}d, \"last.lat\":%{public, location:Encrypted_latitude}.*P, \"last.lng\":%{public, location:Encrypted_longitude}.*P, \"last.ucc\":%{private}d, \"last.timestamp\":%{private}d, \"subHarvester\":%{public, location:CLSubHarvesterIdentifier}lld}"
+ "{\"msg%{public}.0s\":\"location is set\", \"lat\":%{public, location:Encrypted_latitude}.*P, \"lng\":%{public, location:Encrypted_longitude}.*P, \"ucc\":%{private}d, \"timestamp\":%{private}d, \"subHarvester\":%{public, location:CLSubHarvesterIdentifier}lld}"
+ "{\"msg%{public}.0s\":\"location source updated with\", \"altitude\":\"%{private}f\", \"time_s\":\"%{private}.09f\", \"lat\":%{public, location:Encrypted_latitude}.*P, \"lon\":%{public, location:Encrypted_longitude}.*P, \"type\":%{private}d, \"isPrefilteredLocation\":%{private}d, \"rawAltitude\":\"%{private}f\", \"rawVerticalAccuracy\":\"%{private}f\", \"DEM\":\"%{private}f\", \"horizontalAccuracy\":\"%{private}f\", \"verticalAccuracy\":\"%{private}f\", \"DEMUncertainty\":\"%{private}f\", \"Environment\":%{private}d, \"Slope\":\"%{private}f\", \"MaxAbsSlope\":\"%{private}f\", \"Speed\":\"%{private}f\", \"SpeedAccuracy\":\"%{private}f\", \"MatchQuality\":%{private}d, \"AltitudeState\":%{private}d, \"RefProvider\":%{private}d}"
+ "{\"msg%{public}.0s\":\"next location\", \"location\":%{public, location:Encrypted_CLClientLocation}.*P}"
+ "{\"msg%{public}.0s\":\"onLocationNotification\", \"subHarvester\":%{public, location:CLSubHarvesterIdentifier}lld, \"notification\":%{private, location:CLLocationProvider_Type::Notification}lld, \"location\":%{public, location:Encrypted_CLClientLocation}.*P}"
+ "{\"msg%{public}.0s\":\"prefiltered location source updated with\", \"altitude\":\"%{private}f\", \"time_s\":\"%{private}.09f\", \"lat\":%{public, location:Encrypted_latitude}.*P, \"lon\":%{public, location:Encrypted_longitude}.*P, \"type\":%{private}d, \"isPrefilteredLocation\":%{private}d, \"rawAltitude\":\"%{private}f\", \"rawVerticalAccuracy\":\"%{private}f\", \"DEM\":\"%{private}f\"}"
+ "{\"msg%{public}.0s\":\"prepareAdvertisementsForSPFinder\", \"avengerPublicKey\":%{public, location:escape_only}s, \"timestamp\":\"%{private}f\", \"scantime\":%{private, location:escape_only}s, \"latitude\":%{public, location:Encrypted_latitude}.*P, \"longitude\":%{public, location:Encrypted_longitude}.*P, \"altitude\":\"%{private}f\", \"rawHorizontalAccuracy\":\"%{private}f\", \"horizontalAccuracy\":\"%{private}f\", \"verticalAccuracy\":\"%{private}f\", \"speed\":\"%{private}f\", \"speedAccuracy\":\"%{private}f\", \"course\":\"%{private}f\", \"courseAccuracy\":\"%{private}f\", \"type\":%{private}lu, \"integrity\":%{private}lu, \"floor\":%{private}lu, \"maxActivityBasedSpeedSinceLastLocation\":\"%{private}f\", \"maxActivityBasedSpeedSinceAdvertisement\":\"%{private}f\", \"ownedAccessory\":%{public}hhd, \"subHarvester\":%{public, location:CLSubHarvesterIdentifier}lld}"
+ "{\"msg%{public}.0s\":\"received request to resolve whether the following location is inside sanctioned floor transition polygons: \", \"lat\":%{public, location:Encrypted_latitude}.*P, \"lon\":%{public, location:Encrypted_longitude}.*P}"
+ "{\"msg%{public}.0s\":\"received request to resolve whether the following location is inside sanctioned polygons: \", \"lat\":%{public, location:Encrypted_latitude}.*P, \"lon\":%{public, location:Encrypted_longitude}.*P}"
+ "{\"msg%{public}.0s\":\"settings initialized\", \"AllowSimulatedLocations\":%{public}hhd, \"CountryLocationMinimumConfidence\":%{public}d, \"MaximumCountryLocationChangeSpeed\":\"%{public}f\", \"MaximumCountryLocationChangeAccuracy\":\"%{public}f\", \"MinimumMoveDistance\":\"%{public}f\", \"CountryLocationDebounceTime\":\"%{public}f\", \"CountryLocationStalenessTime\":\"%{public}f\", \"TimeToCountryUnknown\":\"%{public}f\", \"MinimumTimeBetweenExpensiveQueries\":\"%{public}f\", \"TimeToCountryCheapLocation\":\"%{public}f\"}"
+ "{\"msg%{public}.0s\":\"settings updated\", \"AllowSimulatedLocations\":%{public}hhd, \"CountryLocationMinimumConfidence\":%{public}d, \"MaximumCountryLocationChangeSpeed\":\"%{public}f\", \"MaximumCountryLocationChangeAccuracy\":\"%{public}f\", \"MinimumMoveDistance\":\"%{public}f\", \"CountryLocationDebounceTime\":\"%{public}f\", \"CountryLocationStalenessTime\":\"%{public}f\", \"TimeToCountryUnknown\":\"%{public}f\", \"TimeToCountryCheapLocation\":\"%{public}f\", \"TimeToRequestCheapActiveLocation\":\"%{public}f\", \"MinimumTimeBetweenExpensiveQueries\":\"%{public}f\", \"CountryDebounceInterval\":%{public}d}"
+ "{\"msg%{public}.0s\":\"throwing out non-gps, non-accessory location\", \"subHarvester\":%{public, location:CLSubHarvesterIdentifier}lld, \"location\":%{public, location:Encrypted_CLClientLocation}.*P}"
- "/AppleInternal/Library/BuildRoots/a893df77-fa81-11ef-9813-de23e2c06a38/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.4.Internal.sdk/usr/local/include/boost/geometry/algorithms/detail/throw_on_empty_input.hpp"
- "/AppleInternal/Library/BuildRoots/a893df77-fa81-11ef-9813-de23e2c06a38/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.4.Internal.sdk/usr/local/include/boost/uuid/detail/random_provider_posix.ipp"
- "/AppleInternal/Library/BuildRoots/a893df77-fa81-11ef-9813-de23e2c06a38/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.4.Internal.sdk/usr/local/include/boost/uuid/string_generator.hpp"
- "/AppleInternal/Library/BuildRoots/a893df77-fa81-11ef-9813-de23e2c06a38/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.4.Internal.sdk/usr/local/include/google/protobuf/repeated_field.h"
- "/AppleInternal/Library/BuildRoots/a893df77-fa81-11ef-9813-de23e2c06a38/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.4.Internal.sdk/usr/local/include/google/protobuf/wire_format_lite_inl.h"
- "21:53:38"
- "22:14:21"
- "Adding geographic fence [%{public}s]/%{public}s/%{private}s, center, %{private}f, %{private}f, radius, %{public}.2f, desiredAccuracy, %{public}.2f"
- "Mar  6 2025"
- "Mar  6 2025 21:56:33"
- "handleNewLocation:"
- "{\"msg%{public}.0s\":\"#EED2 created location dict\", \"timestamp\":%{public}lld, \"lat\":\"%{sensitive}.08f\", \"lon\":\"%{sensitive}.08f\", \"altitude (HAE)\":\"%{sensitive}.2f\", \"hunc\":\"%{public}f\", \"vunc\":\"%{public}f\"}"
- "{\"msg%{public}.0s\":\"#GnssRefLocationCache,Warning invalid assistance location,invalid coordinates\", \"lat\":\"%{sensitive}.08f\", \"lon\":\"%{sensitive}.08f\"}"
- "{\"msg%{public}.0s\":\"#GnssRefLocationCache,feedRefLocationFromRefPosMaintenance\", \"type\":%{public}d, \"timestamp\":\"%{public}.1f\", \"cacheTimestamp\":\"%{public}.1f\", \"lat\":\"%{sensitive}.08f\", \"lon\":\"%{sensitive}.08f\", \"hacc\":\"%{public}.1f\", \"alt\":\"%{private}.2f\", \"vunc\":\"%{public}.1f\"}"
- "{\"msg%{public}.0s\":\"#SLC Got location\", \"location\":%{sensitive, location:CLClientLocation}.*P}"
- "{\"msg%{public}.0s\":\"#SLC location changed\", \"now_s\":\"%{public}.09f\", \"location\":%{sensitive, location:CLClientLocation}.*P, \"distance\":\"%{private}f\"}"
- "{\"msg%{public}.0s\":\"#SPI getLocation #cclp\", \"gotLocation\":%{public}hhd, \"location\":%{sensitive, location:CLClientLocation}.*P}"
- "{\"msg%{public}.0s\":\"#Spi, altered getLocation\", \"location\":%{sensitive, location:CLClientLocation}.*P, \"timestampGps\":\"%{private}f\", \"machTime\":\"%{private}f\", \"gotLocation\":%{private}hhd, \"specialCoordinateLat\":\"%{sensitive}.08f\", \"specialCoordinateLon\":\"%{sensitive}.08f\", \"specialHorizontalAccuracy\":\"%{private}f\"}"
- "{\"msg%{public}.0s\":\"#awd #thumper Caching location \", \"lat\":\"%{sensitive}.08f\", \"lon\":\"%{sensitive}.08f\", \"alt\":\"%{private}f\", \"accuracy\":\"%{private}f\"}"
- "{\"msg%{public}.0s\":\"#awd #thumper location log\", \"lat\":\"%{sensitive}.08f\", \"lon\":\"%{sensitive}.08f\", \"alt\":\"%{private}f\", \"accuracy\":\"%{private}f\", \"source\":%{private}u}"
- "{\"msg%{public}.0s\":\"#cclp UpdateLastReceivedLocationTimer fired. Using location\", \"location\":%{sensitive, location:CLClientLocation}.*P}"
- "{\"msg%{public}.0s\":\"#cclp onLocationNotification\", \"Notification\":%{public, location:escape_only}s, \"location\":%{sensitive, location:CLClientLocation}.*P}"
- "{\"msg%{public}.0s\":\"#cclp passing cached location to reply\", \"location\":%{sensitive, location:CLClientLocation}.*P}"
- "{\"msg%{public}.0s\":\"#cclp perform snapping on location by LC\", \"location\":%{sensitive, location:CLClientLocation}.*P}"
- "{\"msg%{public}.0s\":\"#cclp snapLocation reply\", \"permanent\":%{public}hhd, \"cacheAge\":\"%{public}f\", \"cacheAgeLessThanExtendedInterval\":%{public}hhd, \"hasCachedLocation\":%{public}hhd, \"location\":%{sensitive, location:CLClientLocation}.*P}"
- "{\"msg%{public}.0s\":\"#circularGeographicCondition created\", \"lat\":\"%{sensitive}.08f\", \"lon\":\"%{sensitive}.08f\", \"radius\":\"%{public}f\", \"identifier\":%{public, location:escape_only}@, \"removePersistingFenceFromMonitoring\":%{public}hhd, \"self\":\"%{public}p\"}"
- "{\"msg%{public}.0s\":\"#clcac location not specified. NonZonal-AC differs from Zonal-AC at current-location. Showing location-arrow\", \"Client\":%{public, location:escape_only}s, \"CLCAC-currentLocation\":%{sensitive, location:CLClientLocation}.*P, \"NonZonalAC\":%{public, location:escape_only}@, \"ZonalAC\":%{public, location:escape_only}@}"
- "{\"msg%{public}.0s\":\"#clcac location not specified. NonZonal-AC is same as Zonal-AC at current-location. Skip showing location-arrow\", \"Client\":%{public, location:escape_only}s, \"CLCAC-currentLocation\":%{sensitive, location:CLClientLocation}.*P}"
- "{\"msg%{public}.0s\":\"#cms mode init visit\", \"entry\":%{public}hhd, \"visit\":%{private, location:escape_only}@}"
- "{\"msg%{public}.0s\":\"#gnss DOT\", \"lat\":\"%{sensitive}.08f\", \"lon\":\"%{sensitive}.08f\", \"directionOfTravel\":%{public}d, \"directionOfTravelUnc\":%{public}d, \"roadWidth\":%{public}d, \"startLatitude\":\"%{private}.08f\", \"startLongitude\":\"%{private}.08f\", \"lengthOfLinearSegment\":%{public}d, \"machtime\":%{public}d}"
- "{\"msg%{public}.0s\":\"#gnss MMP\", \"lat\":\"%{sensitive}.08f\", \"lon\":\"%{sensitive}.08f\", \"uncEllipseSemiMajor\":%{public}d, \"uncEllipseSemiMinor\":%{public}d, \"uncEllipseAzimuth\":%{public}d}"
- "{\"msg%{public}.0s\":\"#gnssawd GnssSessionData log\", \"sessionDuration\":%{private}lld, \"fEpochCount\":%{private}lld, \"yieldCount\":%{private}lld, \"lat\":\"%{sensitive}.08f\", \"lon\":\"%{sensitive}.08f\", \"alt\":\"%{private}f\", \"accuracy\":\"%{private}f\", \"ttff\":%{private}d, \"mcc\":%{private}d, \"mnc\":%{private}d, \"sid\":%{private}d, \"nid\":%{private}d, \"transFreq\":\"%{private}f\", \"transBW\":\"%{private}f\", \"transBand\":%{private}d, \"isEmergency\":%{private}d}"
- "{\"msg%{public}.0s\":\"#luHistorical specified Center is not valid\", \"ClientKeyPath\":%{public, location:escape_only}@, \"self\":\"%{public}p\", \"Center.lat\":\"%{sensitive}.08f\", \"Center.lon\":\"%{sensitive}.08f\"}"
- "{\"msg%{public}.0s\":\"#luLive locationData does not have any entries\", \"ClientKeyPath\":%{public, location:escape_only}@, \"self\":\"%{public}p\", \"locationCountAfterSerialization\":%{public}d, \"location\":%{sensitive, location:CLClientLocation}.*P}"
- "{\"msg%{public}.0s\":\"#luLive sending location\", \"ClientKeyPath\":%{public, location:escape_only}@, \"self\":\"%{public}p\", \"locationCountAfterSerialization\":%{public}d, \"location\":%{sensitive, location:CLClientLocation}.*P}"
- "{\"msg%{public}.0s\":\"#luLive unmarking #stationary by location-wandering\", \"ClientKeyPath\":%{public, location:escape_only}@, \"self\":\"%{public}p\", \"wander\":\"%{public}f\", \"OldTS\":\"%{public}f\", \"NewTS\":\"%{public}f\", \"refLat\":\"%{sensitive}.08f\", \"refLon\":\"%{sensitive}.08f\", \"lat\":\"%{sensitive}.08f\", \"lon\":\"%{sensitive}.08f\"}"
- "{\"msg%{public}.0s\":\"#msim performCellHarvesting\", \"subHarvester\":%{public, location:CLSubHarvesterIdentifier}lld, \"SimInstance\":%{public}u, \"location\":%{sensitive, location:CLClientLocation}.*P}"
- "{\"msg%{public}.0s\":\"#pla #zone-relevance-tracker for circular-region\", \"monitoring\":%{public, location:escape_only}s, \"lat\":\"%{sensitive}.08f\", \"lon\":\"%{sensitive}.08f\", \"radius\":\"%{public}.3f\", \"Client\":%{public, location:escape_only}s, \"ZoneId\":%{public, location:escape_only}s}"
- "{\"msg%{public}.0s\":\"#pla #zone-relevance-tracker, location notification\", \"notification\":%{public, location:CLLocationProvider_Type::Notification}lld, \"_currentLocation\":%{sensitive, location:CLClientLocation}.*P, \"NewLocation\":%{sensitive, location:CLClientLocation}.*P}"
- "{\"msg%{public}.0s\":\"#pla Skip #clldu-MarkZonesAsRelevant. Invalid location\", \"dictionary\":%{public, location:escape_only}@, \"location\":%{sensitive, location:CLClientLocation}.*P}"
- "{\"msg%{public}.0s\":\"#pla freshAuthorizationContext location updated\", \"Client\":%{public, location:escape_only}@, \"provided-location\":%{sensitive, location:CLClientLocation}.*P, \"fetched-location-ZRT\":%{sensitive, location:CLClientLocation}.*P}"
- "{\"msg%{public}.0s\":\"Appending location\", \"location\":%{sensitive, location:CLClientLocation}.*P}"
- "{\"msg%{public}.0s\":\"CLDaemonLocationUpdaterHistorical(ctor) #luHistorical\", \"event\":%{public, location:escape_only}s, \"ClientKeyPath\":%{public, location:escape_only}@, \"this\":\"%{public}p\", \"SampleCount\":%{public}d, \"Radius\":\"%{public}f\", \"DateInterval\":%{public, location:escape_only}@, \"CenterSpecified\":%{public}hhd, \"Center.lat\":\"%{sensitive}.08f\", \"Center.lon\":\"%{sensitive}.08f\"}"
- "{\"msg%{public}.0s\":\"GPSODOM\", \"event\":%{public, location:escape_only}s, \"gpsNs\":%{public}lld, \"cfTime\":\"%{public}f\", \"cfTimeGps\":\"%{public}f\", \"machTime\":\"%{public}f\", \"machContinuousTime\":\"%{public}f\", \"posValid\":%{public}hhd, \"lat\":\"%{sensitive}.08f\", \"lon\":\"%{sensitive}.08f\", \"altitude\":\"%{private}f\", \"undulation\":\"%{public}f\", \"hunc\":\"%{public}f\", \"vunc\":\"%{public}f\", \"semiMaj\":\"%{public}f\", \"semiMin\":\"%{public}f\", \"semiMajAz\":\"%{public}f\", \"reliability\":%{public}d, \"speedValid\":%{public}hhd, \"speed\":\"%{public}f\", \"speedUnc\":\"%{public}f\", \"courseValid\":%{public}hhd, \"course\":\"%{public}f\", \"courseUnc\":\"%{public}f\", \"gnssContent\":%{public}d, \"ravenPosUsed\":%{public}hhd, \"odometry\":\"%{public}f\", \"deltaDist\":\"%{public}f\", \"deltaDistUnc\":\"%{public}f\", \"odometryValid\":%{public}hhd}"
- "{\"msg%{public}.0s\":\"GnssEvent\", \"event\":%{public, location:escape_only}s, \"gpsNs\":%{public}lld, \"gpsTimeUncMs\":\"%{public}f\", \"cfTime\":\"%{public}f\", \"cfTimeGps\":\"%{public}f\", \"machTime\":\"%{public}f\", \"machContinuousTime\":\"%{public}f\", \"leapSeconds\":%{public}d, \"posValid\":%{public}hhd, \"lat\":\"%{sensitive}.08f\", \"lon\":\"%{sensitive}.08f\", \"altitude\":\"%{private}f\", \"undulation\":\"%{public}f\", \"undulationModel\":%{public}d, \"hunc\":\"%{public}f\", \"vunc\":\"%{public}f\", \"semiMaj\":\"%{public}f\", \"semiMin\":\"%{public}f\", \"semiMajAz\":\"%{public}f\", \"reliability\":%{public}d, \"speedValid\":%{public}hhd, \"speed\":\"%{public}f\", \"speedUnc\":\"%{public}f\", \"courseValid\":%{public}hhd, \"course\":\"%{public}f\", \"courseUnc\":\"%{public}f\", \"imag\":%{public}d, \"gnssContent\":%{public}d}"
- "{\"msg%{public}.0s\":\"GnssEvent\", \"event\":%{public, location:escape_only}s, \"location\":%{sensitive, location:CLClientLocation}.*P, \"isIndia\":%{private}hhd, \"isCPI\":%{public}hhd}"
- "{\"msg%{public}.0s\":\"GnssEvent\", \"event\":%{public, location:escape_only}s, \"timestamp\":\"%{public}f\", \"lat\":\"%{sensitive}.08f\", \"lon\":\"%{sensitive}.08f\", \"directionOfTravel\":\"%{public}f\", \"directionOfTravelUnc\":\"%{public}f\", \"roadWidth\":\"%{public}f\", \"startLatitude\":\"%{private}.08f\", \"startLongitude\":\"%{private}.08f\", \"lengthOfLinearSegment\":\"%{public}f\", \"machtime\":\"%{public}f\"}"
- "{\"msg%{public}.0s\":\"GnssEvent\", \"event\":%{public, location:escape_only}s, \"timestamp\":\"%{public}f\", \"lat\":\"%{sensitive}.08f\", \"lon\":\"%{sensitive}.08f\", \"uncEllipseSemiMajor\":\"%{public}f\", \"uncEllipseSemiMinor\":\"%{public}f\", \"uncEllipseAzimuth\":\"%{public}f\"}"
- "{\"msg%{public}.0s\":\"Harvest-Collect\", \"subHarvester\":%{public, location:CLSubHarvesterIdentifier}lld, \"location\":%{sensitive, location:CLClientLocation}.*P, \"tripId\":%{private, location:escape_only}s, \"rat\":%{private}d, \"mcc\":%{private}d, \"mnc\":%{private}d, \"motionVehicleConnectedStateChanged\":%{private}d, \"motionVehicleConnected\":%{private}d, \"rawMotionActivity\":%{private, location:CLMotionActivity}.*P, \"motionActivity\":%{private, location:CLMotionActivity}.*P, \"dominantMotionActivity\":%{private, location:CLMotionActivity}.*P, \"isProactiveLocationSession\":%{private}d}"
- "{\"msg%{public}.0s\":\"Harvest-Database-Collect\", \"subHarvester\":%{public, location:CLSubHarvesterIdentifier}lld, \"location\":%{sensitive, location:CLClientLocation}.*P}"
- "{\"msg%{public}.0s\":\"Invalid batched location\", \"location\":%{sensitive, location:CLClientLocation}.*P}"
- "{\"msg%{public}.0s\":\"Location #compensation Snapping\", \"Input\":%{sensitive, location:CLClientLocation}.*P, \"Output\":%{sensitive, location:CLClientLocation}.*P, \"distance\":\"%{public}f\", \"GeoResultCode\":%{public}ld}"
- "{\"msg%{public}.0s\":\"Location #compensation gonna be Snapping\", \"Input\":%{sensitive, location:CLClientLocation}.*P}"
- "{\"msg%{public}.0s\":\"Notify location is\", \"location\":%{sensitive, location:CLClientLocation}.*P}"
- "{\"msg%{public}.0s\":\"Notifying clients with location\", \"location\":%{sensitive, location:CLClientLocation}.*P, \"notification\":%{public, location:CLLocationProvider_Type::Notification}lld}"
- "{\"msg%{public}.0s\":\"Reached location, preparing next\", \"reachedLat\":\"%{sensitive}.08f\", \"reachedLon\":\"%{sensitive}.08f\"}"
- "{\"msg%{public}.0s\":\"Sending location to client\", \"Client\":%{public, location:escape_only}@, \"DC\":\"%{public}p\", \"location\":%{sensitive, location:CLClientLocation}.*P, \"desiredAccuracy\":\"%{public}f\"}"
- "{\"msg%{public}.0s\":\"Using simulated location from defaults\", \"location\":%{sensitive, location:CLClientLocation}.*P}"
- "{\"msg%{public}.0s\":\"[LOI] Received a location\", \"location\":%{sensitive, location:CLClientLocation}.*P}"
- "{\"msg%{public}.0s\":\"applying bounding-box-specific overrides\", \"lat\":\"%{sensitive}.08f\", \"lon\":\"%{sensitive}.08f\", \"latMin\":\"%{sensitive}.08f\", \"lonMin\":\"%{sensitive}.08f\", \"latMax\":\"%{sensitive}.08f\", \"lonMax\":\"%{sensitive}.08f\"}"
- "{\"msg%{public}.0s\":\"checking distance to visit\", \"lat\":\"%{sensitive}.08f\", \"lon\":\"%{sensitive}.08f\"}"
- "{\"msg%{public}.0s\":\"computed deltas\", \"deltaR\":\"%{public}f\", \"deltaT\":\"%{public}f\", \"debounceTime\":\"%{public}f\", \"staleTime\":\"%{public}f\", \"prevLat\":\"%{sensitive}.08f\", \"prevLon\":\"%{sensitive}.08f\"}"
- "{\"msg%{public}.0s\":\"computing #clldu freshAuthContext\", \"EffectiveRegistration\":%{public, location:CLClientRegistrationResult}lld, \"TransientRegistration\":%{public, location:CLClientRegistrationResult}lld, \"bigSwitchState\":%{public}hhd, \"isClientZonal\":%{public}hhd, \"location\":%{sensitive, location:CLClientLocation}.*P, \"dictionary\":%{public, location:escape_only}@}"
- "{\"msg%{public}.0s\":\"faraway location encountered\", \"time_s\":\"%{public}.09f\", \"distance\":\"%{public}.2f\", \"lat\":\"%{sensitive}.08f\", \"lon\":\"%{sensitive}.08f\"}"
- "{\"msg%{public}.0s\":\"fetch estimated device location at BA location time\", \"lat\":\"%{sensitive}.08f\", \"lng\":\"%{sensitive}.08f\", \"ucc\":%{private}d, \"subHarvester\":%{public, location:CLSubHarvesterIdentifier}lld}"
- "{\"msg%{public}.0s\":\"fetchRoutineLoiType\", \"subHarvester\":%{public, location:CLSubHarvesterIdentifier}lld, \"location\":%{sensitive, location:CLClientLocation}.*P, \"loiType\":%{private, location:RTLocationOfInterestType}lld}"
- "{\"msg%{public}.0s\":\"fetchRoutineMode\", \"subHarvester\":%{public, location:CLSubHarvesterIdentifier}lld, \"location\":%{sensitive, location:CLClientLocation}.*P, \"routineMode\":%{private, location:RTRoutineMode}lld}"
- "{\"msg%{public}.0s\":\"find nearest location\", \"lat\":\"%{sensitive}.08f\", \"lng\":\"%{sensitive}.08f\", \"ucc\":%{private}d, \"time interval\":%{private}d, \"subHarvester\":%{public, location:CLSubHarvesterIdentifier}lld}"
- "{\"msg%{public}.0s\":\"ignoring since accuracy is too large\", \"subHarvester\":%{public, location:CLSubHarvesterIdentifier}lld, \"lat\":\"%{sensitive}.08f\", \"lon\":\"%{sensitive}.08f\", \"horizontalAccuracy\":\"%{private}f\"}"
- "{\"msg%{public}.0s\":\"isInside\", \"fZoneId\":%{private}d, \"minLat\":\"%{private}f\", \"maxLat\":\"%{private}f\", \"minLon\":\"%{private}f\", \"maxLon\":\"%{private}f\", \"latitude\":\"%{sensitive}.08f\", \"longitude\":\"%{sensitive}.08f\", \"isInsize\":%{private}hhd}"
- "{\"msg%{public}.0s\":\"location is filtered due to lack of additional information\", \"lat\":\"%{sensitive}.08f\", \"lng\":\"%{sensitive}.08f\", \"ucc\":%{private}d, \"timestamp\":%{private}d, \"last.lat\":\"%{sensitive}.08f\", \"last.lng\":\"%{sensitive}.08f\", \"last.ucc\":%{private}d, \"last.timestamp\":%{private}d, \"subHarvester\":%{public, location:CLSubHarvesterIdentifier}lld}"
- "{\"msg%{public}.0s\":\"location is set\", \"lat\":\"%{sensitive}.08f\", \"lng\":\"%{sensitive}.08f\", \"ucc\":%{private}d, \"timestamp\":%{private}d, \"subHarvester\":%{public, location:CLSubHarvesterIdentifier}lld}"
- "{\"msg%{public}.0s\":\"location source updated with\", \"altitude\":\"%{private}f\", \"time_s\":\"%{private}.09f\", \"lat\":\"%{sensitive}.08f\", \"lon\":\"%{sensitive}.08f\", \"type\":%{private}d, \"isPrefilteredLocation\":%{private}d, \"rawAltitude\":\"%{private}f\", \"rawVerticalAccuracy\":\"%{private}f\", \"DEM\":\"%{private}f\", \"horizontalAccuracy\":\"%{private}f\", \"verticalAccuracy\":\"%{private}f\", \"DEMUncertainty\":\"%{private}f\", \"Environment\":%{private}d, \"Slope\":\"%{private}f\", \"MaxAbsSlope\":\"%{private}f\", \"Speed\":\"%{private}f\", \"SpeedAccuracy\":\"%{private}f\", \"MatchQuality\":%{private}d, \"AltitudeState\":%{private}d, \"RefProvider\":%{private}d}"
- "{\"msg%{public}.0s\":\"next location\", \"location\":%{sensitive, location:CLClientLocation}.*P}"
- "{\"msg%{public}.0s\":\"onLocationNotification\", \"subHarvester\":%{public, location:CLSubHarvesterIdentifier}lld, \"notification\":%{private, location:CLLocationProvider_Type::Notification}lld, \"location\":%{sensitive, location:CLClientLocation}.*P}"
- "{\"msg%{public}.0s\":\"prefiltered location source updated with\", \"altitude\":\"%{private}f\", \"time_s\":\"%{private}.09f\", \"lat\":\"%{sensitive}.08f\", \"lon\":\"%{sensitive}.08f\", \"type\":%{private}d, \"isPrefilteredLocation\":%{private}d, \"rawAltitude\":\"%{private}f\", \"rawVerticalAccuracy\":\"%{private}f\", \"DEM\":\"%{private}f\"}"
- "{\"msg%{public}.0s\":\"prepareAdvertisementsForSPFinder\", \"avengerPublicKey\":%{public, location:escape_only}s, \"timestamp\":\"%{private}f\", \"scantime\":%{private, location:escape_only}s, \"latitude\":\"%{sensitive}.08f\", \"longitude\":\"%{sensitive}.08f\", \"altitude\":\"%{private}f\", \"rawHorizontalAccuracy\":\"%{private}f\", \"horizontalAccuracy\":\"%{private}f\", \"verticalAccuracy\":\"%{private}f\", \"speed\":\"%{private}f\", \"speedAccuracy\":\"%{private}f\", \"course\":\"%{private}f\", \"courseAccuracy\":\"%{private}f\", \"type\":%{private}lu, \"integrity\":%{private}lu, \"floor\":%{private}lu, \"maxActivityBasedSpeedSinceLastLocation\":\"%{private}f\", \"maxActivityBasedSpeedSinceAdvertisement\":\"%{private}f\", \"ownedAccessory\":%{public}hhd, \"subHarvester\":%{public, location:CLSubHarvesterIdentifier}lld}"
- "{\"msg%{public}.0s\":\"received request to resolve whether the following location is inside sanctioned floor transition polygons: \", \"lat\":\"%{sensitive}.08f\", \"lon\":\"%{sensitive}.08f\"}"
- "{\"msg%{public}.0s\":\"received request to resolve whether the following location is inside sanctioned polygons: \", \"lat\":\"%{sensitive}.08f\", \"lon\":\"%{sensitive}.08f\"}"
- "{\"msg%{public}.0s\":\"settings initialized\", \"AllowSimulatedLocations\":%{public}hhd, \"CountryLocationMinimumConfidence\":%{public}d, \"MaximumCountryLocationChangeSpeed\":\"%{public}f\", \"MaximumCountryLocationChangeAccuracy\":\"%{public}f\", \"MinimumMoveDistance\":\"%{public}f\", \"CountryLocationDebounceTime\":\"%{public}f\", \"CountryLocationStalenessTime\":\"%{public}f\", \"TimeToCountryUnknown\":\"%{public}f\", \"TimeToCountryCheapLocation\":\"%{public}f\"}"
- "{\"msg%{public}.0s\":\"settings updated\", \"AllowSimulatedLocations\":%{public}hhd, \"CountryLocationMinimumConfidence\":%{public}d, \"MaximumCountryLocationChangeSpeed\":\"%{public}f\", \"MaximumCountryLocationChangeAccuracy\":\"%{public}f\", \"MinimumMoveDistance\":\"%{public}f\", \"CountryLocationDebounceTime\":\"%{public}f\", \"CountryLocationStalenessTime\":\"%{public}f\", \"TimeToCountryUnknown\":\"%{public}f\", \"TimeToCountryCheapLocation\":\"%{public}f\", \"TimeToRequestCheapActiveLocation\":\"%{public}f\", \"CountryDebounceInterval\":%{public}d}"
- "{\"msg%{public}.0s\":\"throwing out non-gps, non-accessory location\", \"subHarvester\":%{public, location:CLSubHarvesterIdentifier}lld, \"location\":%{sensitive, location:CLClientLocation}.*P}"

```
