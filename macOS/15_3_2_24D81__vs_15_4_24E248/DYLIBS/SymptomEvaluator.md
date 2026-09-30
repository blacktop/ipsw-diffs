## SymptomEvaluator

> `/System/Library/PrivateFrameworks/Symptoms.framework/Versions/A/Frameworks/SymptomEvaluator.framework/Versions/A/SymptomEvaluator`

```diff

-2001.80.5.0.0
-  __TEXT.__text: 0x1b7ff0
-  __TEXT.__auth_stubs: 0x1be0
-  __TEXT.__objc_methlist: 0x1002c
-  __TEXT.__cstring: 0x18793
-  __TEXT.__const: 0x748
-  __TEXT.__gcc_except_tab: 0x3108
-  __TEXT.__oslogstring: 0x2444b
+2022.100.26.0.0
+  __TEXT.__text: 0x1baba8
+  __TEXT.__auth_stubs: 0x1c20
+  __TEXT.__objc_methlist: 0x10b34
+  __TEXT.__cstring: 0x18a2b
+  __TEXT.__const: 0x788
+  __TEXT.__gcc_except_tab: 0x31a8
+  __TEXT.__oslogstring: 0x24ee4
   __TEXT.__dlopen_cstrs: 0x56
-  __TEXT.evaluator_cfg: 0x634d
-  __TEXT.__unwind_info: 0x4a98
-  __TEXT.__objc_classname: 0x15fe
-  __TEXT.__objc_methname: 0x2827e
-  __TEXT.__objc_methtype: 0x4717
-  __TEXT.__objc_stubs: 0x16ac0
-  __DATA_CONST.__got: 0xa70
-  __DATA_CONST.__const: 0x29f8
+  __TEXT.evaluator_cfg: 0x6417
+  __TEXT.__unwind_info: 0x4a88
+  __TEXT.__objc_classname: 0x161d
+  __TEXT.__objc_methname: 0x28b0a
+  __TEXT.__objc_methtype: 0x4ab6
+  __TEXT.__objc_stubs: 0x16fe0
+  __DATA_CONST.__got: 0xa78
+  __DATA_CONST.__const: 0x2a20
   __DATA_CONST.__objc_classlist: 0x688
   __DATA_CONST.__objc_catlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x108
+  __DATA_CONST.__objc_protolist: 0x110
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x8ee8
+  __DATA_CONST.__objc_selrefs: 0x9288
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x430
+  __DATA_CONST.__objc_superrefs: 0x438
   __DATA_CONST.__objc_arraydata: 0xa8
-  __AUTH_CONST.__auth_got: 0xe08
-  __AUTH_CONST.__const: 0x4050
-  __AUTH_CONST.__cfstring: 0x14620
-  __AUTH_CONST.__objc_const: 0x299d0
+  __AUTH_CONST.__auth_got: 0xe28
+  __AUTH_CONST.__const: 0x41c0
+  __AUTH_CONST.__cfstring: 0x14760
+  __AUTH_CONST.__objc_const: 0x29058
   __AUTH_CONST.__objc_intobj: 0x588
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH.__objc_data: 0x2710
-  __DATA.__objc_ivar: 0x1b50
-  __DATA.__data: 0x1588
+  __DATA.__objc_ivar: 0x1b88
+  __DATA.__data: 0x15e8
   __DATA.__crash_info: 0x40
-  __DATA.__bss: 0xb38
-  __DATA.__common: 0x169
+  __DATA.__bss: 0xb80
+  __DATA.__common: 0x160
   __DATA_DIRTY.__objc_data: 0x1a40
   __DATA_DIRTY.__data: 0x70
-  __DATA_DIRTY.__bss: 0x5a0
+  __DATA_DIRTY.__bss: 0x5b0
   __DATA_DIRTY.__common: 0xe8
   - /System/Library/Frameworks/CFNetwork.framework/Versions/A/CFNetwork
   - /System/Library/Frameworks/CoreData.framework/Versions/A/CoreData

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libspindump.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 260E3423-C1C0-3811-8854-9BDE09657F5C
-  Functions: 8263
-  Symbols:   17668
-  CStrings:  18017
+  UUID: 2C69DA5B-8EC4-3316-B512-B869B5C8495B
+  Functions: 8306
+  Symbols:   17923
+  CStrings:  18193
 
Symbols:
+ +[ArbitratorExpertSystemHandler disableResourceNotifyDampening].cold.1
+ +[ConfigurationHandler initialize].cold.1
+ +[ConsoleUserMonitor sharedInstance].cold.1
+ +[DailyMaintenanceActivity sharedInstance].cold.1
+ +[HourlyMaintenanceActivity sharedInstance].cold.1
+ +[ICMPPingProbe loadStringUtils].cold.1
+ +[LaunchServicesUtilities(ImplicitlyAssumedIdentityEntitlement) implicitlyAssumedIdentityEntitlementForBundleIdentifier:].cold.1
+ +[LocationStateRelay automaticallyNotifiesObserversForKey:]
+ +[LocationStateRelay sharedInstance].cold.1
+ +[NetworkDomainsUtility isValidDomain:].cold.1
+ +[NetworkStateRelay getStateRelayFor:].cold.1
+ +[PersonalHotspotRelay sharedInstance].cold.1
+ +[PowerStateRelay defaultRelay].cold.1
+ +[PrivacyProxyStateRelay sharedInstance].cold.1
+ +[ResourceNotifyHandler processOnBatteryOnly].cold.1
+ +[SemiDailyMaintenanceActivity sharedInstance].cold.1
+ +[SmartDataModeRelay sharedInstance].cold.1
+ +[WeeklyMaintenanceActivity sharedInstance].cold.1
+ -[AWDAgent overridePostMetricConfig].cold.1
+ -[BonjourProbe loadBonjourSymbols].cold.1
+ -[FlowAnalyticsEngine _has1stPartyImpliedBundleNameBehavior:].cold.1
+ -[FlowAnalyticsEngine _updateLiveUsage:wifiIn:wifiOut:cellIn:cellOut:wiredIn:wiredOut:btIn:btOut:xIn:xOut:isJumboFlow:isExpensive:closing:]
+ -[GeoDBHandler coordinatesToGeoHashWithLength:latitude:longitude:]
+ -[GeoDBHandler coordinatesToGeoHashWithLength:latitude:longitude:].cold.1
+ -[GeoDBHandler donateBiomeEventForEdgeSelectionWithPrefix:interfaceType:radioType:radioBand:latitude:longitude:reply:]
+ -[ICMPPingProbe _readData].cold.3
+ -[ICMPPingProbe _readData].cold.4
+ -[ICMPPingProbe _readData].cold.5
+ -[ICMPPingProbe _readData].cold.6
+ -[ICMPPingProbe stopTest].cold.1
+ -[IpsFileUtility createIpsFileWithBugType:contentType:additionalIpsHeaders:ipsData:inDirectory:fileNamePrefix:].cold.1
+ -[LocationStateRelay .cxx_destruct]
+ -[LocationStateRelay LOIUseAuthorized]
+ -[LocationStateRelay addPendingLOIBlocks:]
+ -[LocationStateRelay allLOIs]
+ -[LocationStateRelay authorizedToUseCoreRoutine]
+ -[LocationStateRelay callPendingLOIBlocksWithCLLocation:LOI:andError:]
+ -[LocationStateRelay cleanUpPendingLOIBlocks]
+ -[LocationStateRelay dealloc]
+ -[LocationStateRelay determineIfLocationOfInterestIsKnownOfType:queue:reply:]
+ -[LocationStateRelay fetchCurrentLocationLOIOnQueue:desiredAccuracy:reply:]
+ -[LocationStateRelay gpsInUse]
+ -[LocationStateRelay init]
+ -[LocationStateRelay loadCoreLocation]
+ -[LocationStateRelay loadCoreRoutine]
+ -[LocationStateRelay locationManager:didFailWithError:]
+ -[LocationStateRelay locationManager:didUpdateLocations:]
+ -[LocationStateRelay locationManagerDidChangeAuthorization:]
+ -[LocationStateRelay mobileWiFiLocationManager]
+ -[LocationStateRelay preflightFrameworks]
+ -[LocationStateRelay rtLOITypeToString:]
+ -[LocationStateRelay setAllLOIs:]
+ -[LocationStateRelay setGpsInUse:]
+ -[LocationStateRelay setLOIUseAuthorized:]
+ -[LocationStateRelay showLocationArrow]
+ -[LocationStateRelay unloadFrameworks]
+ -[NWActivityHandler serialNumberForInternalBuilds].cold.1
+ -[NetworkAnalyticsModel _trainModelForInterfaceType:sanitizedLQMTable:].cold.1
+ -[ServiceImpl _checkRateLimitForConnection:].cold.1
+ -[ServiceImpl _handleNOIClientForConnection:].cold.1
+ -[ServiceImpl assertEntitlement:entitlement:orWaiveOnIntent:].cold.1
+ -[ServiceImpl donateBiomeEventForEdgeSelectionWithPrefix:interfaceType:radioType:radioBand:latitude:longitude:reply:]
+ -[ServiceImpl listener:shouldAcceptNewConnection:].cold.1
+ -[SymptomsCAObserver addDelegate:forEvents:withQueue:completion:].cold.1
+ -[SymptomsCAObserver addDelegate:forEvents:withQueue:completion:].cold.2
+ -[SymptomsCAObserver addDelegate:forEvents:withQueue:completion:].cold.3
+ -[SymptomsCAObserver removeDelegate:withQueue:completion:].cold.1
+ -[SystemProperties buildVariant].cold.1
+ OBJC_IVAR_$_GeoDBHandler._locationRelay
+ OBJC_IVAR_$_LocationStateRelay.CLLocationManagerClassRef
+ OBJC_IVAR_$_LocationStateRelay._LOIUseAuthorized
+ OBJC_IVAR_$_LocationStateRelay._allLOIs
+ OBJC_IVAR_$_LocationStateRelay._gpsInUse
+ OBJC_IVAR_$_LocationStateRelay._internalQueue
+ OBJC_IVAR_$_LocationStateRelay.clCopyTechnologiesInUseFunc
+ OBJC_IVAR_$_LocationStateRelay.coreLocationDyLibHandle
+ OBJC_IVAR_$_LocationStateRelay.coreRoutineDyLibHandle
+ OBJC_IVAR_$_LocationStateRelay.locationRequestTimer
+ OBJC_IVAR_$_LocationStateRelay.mobileWiFiBundle
+ OBJC_IVAR_$_LocationStateRelay.mobileWiFiLocationManager
+ OBJC_IVAR_$_LocationStateRelay.pendingLOIBlocks
+ OBJC_IVAR_$_LocationStateRelay.routineManager
+ SFGetQueueAttribute.cold.1
+ SFGetStandardQueue.cold.1
+ _GetStrategyName
+ _OUTLINED_FUNCTION_10
+ _OUTLINED_FUNCTION_11
+ _OUTLINED_FUNCTION_12
+ _OUTLINED_FUNCTION_13
+ _OUTLINED_FUNCTION_14
+ _OUTLINED_FUNCTION_15
+ _OUTLINED_FUNCTION_16
+ _OUTLINED_FUNCTION_17
+ _OUTLINED_FUNCTION_18
+ _OUTLINED_FUNCTION_19
+ _OUTLINED_FUNCTION_20
+ _OUTLINED_FUNCTION_21
+ _OUTLINED_FUNCTION_22
+ _OUTLINED_FUNCTION_23
+ _OUTLINED_FUNCTION_24
+ _OUTLINED_FUNCTION_25
+ _OUTLINED_FUNCTION_5
+ _OUTLINED_FUNCTION_6
+ _OUTLINED_FUNCTION_7
+ _OUTLINED_FUNCTION_8
+ _OUTLINED_FUNCTION_9
+ __23-[ServiceImpl shutdown]_block_invoke.182
+ __26-[ICMPPingProbe _readData]_block_invoke.cold.1
+ __26-[ICMPPingProbe _readData]_block_invoke.cold.2
+ __28-[GeoDBHandler noteSymptom:]_block_invoke.81
+ __40-[AnalyticsLaunchpad configureInstance:]_block_invoke_2.cold.1
+ __40-[ServiceImpl clientTransactionsRelease]_block_invoke.181
+ __40-[ServiceImpl getOption:inScopes:reply:]_block_invoke.169
+ __40-[ServiceImpl setOption:inScopes:reply:]_block_invoke.166
+ __47-[GeoDBHandler processSymptomForInterfaceType:]_block_invoke.40
+ __48-[ServiceImpl initWithQueue:noiEngine:isHelper:]_block_invoke.143
+ __48-[ServiceImpl initWithQueue:noiEngine:isHelper:]_block_invoke.145
+ __48-[ServiceImpl initWithQueue:noiEngine:isHelper:]_block_invoke.148
+ __48-[ServiceImpl initWithQueue:noiEngine:isHelper:]_block_invoke.150
+ __49-[ServiceImpl waitForOSLogErrorSymptomWithReply:]_block_invoke.183
+ __49-[ServiceImpl waitForOSLogErrorSymptomWithReply:]_block_invoke.185
+ __52-[ServiceImpl createSnapshotFor:pred:actions:reply:]_block_invoke.165
+ __52-[ServiceImpl resetDataFor:nameKind:inScopes:reply:]_block_invoke.173
+ __55-[ServiceImpl assertFactString:module:asSymptom:reply:]_block_invoke.191
+ __75-[LocationStateRelay fetchCurrentLocationLOIOnQueue:desiredAccuracy:reply:]_block_invoke.14
+ __75-[LocationStateRelay fetchCurrentLocationLOIOnQueue:desiredAccuracy:reply:]_block_invoke.15
+ __75-[LocationStateRelay fetchCurrentLocationLOIOnQueue:desiredAccuracy:reply:]_block_invoke.17
+ __77-[LocationStateRelay determineIfLocationOfInterestIsKnownOfType:queue:reply:]_block_invoke.18
+ __83-[ServiceImpl performQueryOnEntity:fetchRequestProperties:pred:sort:actions:reply:]_block_invoke.164
+ __OBJC_$_INSTANCE_METHODS_LocationStateRelay
+ __OBJC_$_INSTANCE_VARIABLES_LocationStateRelay
+ __OBJC_$_PROP_LIST_LocationStateRelay
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CLLocationManagerDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CLLocationManagerDelegate
+ __OBJC_$_PROTOCOL_REFS_CLLocationManagerDelegate
+ __OBJC_CLASS_PROTOCOLS_$_LocationStateRelay
+ __OBJC_LABEL_PROTOCOL_$_CLLocationManagerDelegate
+ __OBJC_PROTOCOL_$_CLLocationManagerDelegate
+ ___118-[GeoDBHandler donateBiomeEventForEdgeSelectionWithPrefix:interfaceType:radioType:radioBand:latitude:longitude:reply:]_block_invoke
+ ___36+[LocationStateRelay sharedInstance]_block_invoke
+ ___37-[LocationStateRelay loadCoreRoutine]_block_invoke
+ ___38-[LocationStateRelay loadCoreLocation]_block_invoke
+ ___41-[LocationStateRelay preflightFrameworks]_block_invoke
+ ___45-[LocationStateRelay cleanUpPendingLOIBlocks]_block_invoke
+ ___47-[LocationStateRelay mobileWiFiLocationManager]_block_invoke
+ ___57-[LocationStateRelay locationManager:didUpdateLocations:]_block_invoke
+ ___70-[LocationStateRelay callPendingLOIBlocksWithCLLocation:LOI:andError:]_block_invoke
+ ___75-[LocationStateRelay fetchCurrentLocationLOIOnQueue:desiredAccuracy:reply:]_block_invoke
+ ___75-[LocationStateRelay fetchCurrentLocationLOIOnQueue:desiredAccuracy:reply:]_block_invoke_2
+ ___77-[LocationStateRelay determineIfLocationOfInterestIsKnownOfType:queue:reply:]_block_invoke
+ ___77-[LocationStateRelay determineIfLocationOfInterestIsKnownOfType:queue:reply:]_block_invoke_2
+ ___block_descriptor_48_e8_32s40bs_e57_v32?0"RTLocationOfInterest"8"CLLocation"16"NSError"24l
+ ___block_descriptor_48_e8_32s40r_e29_v24?0"NSArray"8"NSError"16l
+ ___block_descriptor_48_e8_32s40s_e42_v24?0"RTLocationOfInterest"8"NSError"16l
+ ___block_descriptor_48_e8_32s40s_e75_v32?0"NSDate"8?<v?"RTLocationOfInterest""CLLocation""NSError">16^B24l
+ ___block_descriptor_56_e8_32s40bs_e29_v24?0"NSArray"8"NSError"16l
+ ___block_descriptor_56_e8_32s40s48s_e75_v32?0"NSDate"8?<v?"RTLocationOfInterest""CLLocation""NSError">16^B24l
+ ___block_descriptor_80_e8_32s40s48s56s64s_e57_v32?0"RTLocationOfInterest"8"CLLocation"16"NSError"24l
+ ___softlink__BiomeLibrary
+ __block_literal_global.119
+ __block_literal_global.134
+ __softlink__BiomeLibrary.cold.1
+ _dispatch_group_create
+ _dispatch_group_enter
+ _dispatch_group_leave
+ _dispatch_group_wait
+ _flowPropertyScaleString
+ _geoHashBase32Map
+ _kNWStatsSelectInterfaceCompanionLinkBluetooth
+ _kNotificationBarcodeActivation
+ _liveUsageCountForProcess:subscriberTag:.errCount
+ _liveUsagePackForProcess:subscriberTag:.errCount
+ _liveUsagePackForProcess:subscriberTag:.lastLoggedTime
+ _loadCrashReporterSupport.cold.1
+ _objc_msgSend$ISOcountryCode
+ _objc_msgSend$_updateLiveUsage:wifiIn:wifiOut:cellIn:cellOut:wiredIn:wiredOut:btIn:btOut:xIn:xOut:isJumboFlow:isExpensive:closing:
+ _objc_msgSend$addPendingLOIBlocks:
+ _objc_msgSend$authorizationStatusForBundle:
+ _objc_msgSend$authorizedToUseCoreRoutine
+ _objc_msgSend$btIN
+ _objc_msgSend$btIN_exp
+ _objc_msgSend$btOUT
+ _objc_msgSend$btOUT_exp
+ _objc_msgSend$bundleWithPath:
+ _objc_msgSend$callPendingLOIBlocksWithCLLocation:LOI:andError:
+ _objc_msgSend$cleanUpPendingLOIBlocks
+ _objc_msgSend$coordinate
+ _objc_msgSend$coordinatesToGeoHashWithLength:latitude:longitude:
+ _objc_msgSend$deltaAccountingRxCompanionLinkBluetoothBytes
+ _objc_msgSend$deltaAccountingTxCompanionLinkBluetoothBytes
+ _objc_msgSend$donateBiomeEventForEdgeSelectionWithPrefix:interfaceType:radioType:radioBand:latitude:longitude:reply:
+ _objc_msgSend$fetchCurrentLocationLOIOnQueue:desiredAccuracy:reply:
+ _objc_msgSend$fetchLocationOfInterestAtLocation:withHandler:
+ _objc_msgSend$fetchLocationsOfInterestOfType:withHandler:
+ _objc_msgSend$gpsInUse
+ _objc_msgSend$horizontalAccuracy
+ _objc_msgSend$initWithEffectiveBundle:delegate:onQueue:
+ _objc_msgSend$initWithLatitude:longitude:
+ _objc_msgSend$latitude
+ _objc_msgSend$loadCoreLocation
+ _objc_msgSend$loadCoreRoutine
+ _objc_msgSend$locality
+ _objc_msgSend$locationServicesEnabled
+ _objc_msgSend$longitude
+ _objc_msgSend$markAsHavingReceivedLocation
+ _objc_msgSend$mobileWiFiLocationManager
+ _objc_msgSend$preflightFrameworks
+ _objc_msgSend$requestLocation
+ _objc_msgSend$reverseGeocodeLocation:completionHandler:
+ _objc_msgSend$rtLOITypeToString:
+ _objc_msgSend$setBtIN:
+ _objc_msgSend$setBtIN_exp:
+ _objc_msgSend$setBtOUT:
+ _objc_msgSend$setBtOUT_exp:
+ _objc_msgSend$setDesiredAccuracy:
+ _objc_msgSend$setLOIUseAuthorized:
+ _objc_msgSend$showLocationArrow
+ _objc_msgSend$unloadFrameworks
+ _runningRNFTurbo
+ activityLogHandle.cold.1
+ algosLogHandle.cold.1
+ boottime_secs.cold.1
+ configure_symptom_logging.cold.1
+ dateStringMillisecondsFromTimeInterval.cold.1
+ dateStringMillisecondsFromTimeInterval.cold.2
+ formattedDateStringForTimeInterval.cold.1
+ formattedDateStringForTimeInterval.cold.2
+ initializeActivityMeasurements.cold.2
+ internal_symptom_new.cold.1
+ loadCoreLocation.loadedCL
+ loadCoreLocation.pred
+ loadCoreRoutine.loadedCR
+ loadCoreRoutine.symbolLoadOnce
+ machAbsoluteTimeFromNanoseconds.cold.1
+ machAbsoluteTime_secs.cold.1
+ machContinuousTime_secs.cold.1
+ measureLaunchXPCHandle.cold.1
+ metricstreamLogHandle.cold.1
+ microsecondsFromMachAbsoluteTime.cold.1
+ millisecondsFromMachAbsoluteTime.cold.1
+ mobileWiFiLocationManager.pred
+ nanosecondsFromMachAbsoluteTime.cold.1
+ preflightFrameworks.pred
+ secondsFromMachAbsoluteTime.cold.1
+ sf_synchronize.cold.1
+ sf_synchronize.cold.2
+ stringByRemovingTrailingUUIDsAndLaunchServicesStuff.cold.1
+ symptomConnectionCreate.cold.1
+ timeIntervalFromMachAbsoluteTime.cold.1
+ timeStringMillisecondsDuration.cold.1
+ timeStringMillisecondsDuration.cold.2
+ timeStringMillisecondsDuration.cold.3
+ timeStringMillisecondsFromTimeInterval.cold.1
+ timeStringMillisecondsFromTimeInterval.cold.2
+ uptime_secs.cold.1
- -[FlowAnalyticsEngine _updateLiveUsage:wifiIn:wifiOut:cellIn:cellOut:wiredIn:wiredOut:xIn:xOut:isJumboFlow:isExpensive:closing:]
- -[GeoDBHandler donateBiomeEventForEdgeSelectionWithPrefix:interfaceType:radioType:radioBand:reply:]
- -[GeoDBHandler donateBiomeEventForEdgeSelectionWithPrefix:interfaceType:radioType:radioBand:reply:].cold.1
- -[ServiceImpl donateBiomeEventForEdgeSelectionWithPrefix:interfaceType:radioType:radioBand:reply:]
- __23-[ServiceImpl shutdown]_block_invoke.181
- __28-[GeoDBHandler noteSymptom:]_block_invoke.62
- __40-[ServiceImpl clientTransactionsRelease]_block_invoke.180
- __40-[ServiceImpl getOption:inScopes:reply:]_block_invoke.168
- __40-[ServiceImpl setOption:inScopes:reply:]_block_invoke.165
- __48-[ServiceImpl initWithQueue:noiEngine:isHelper:]_block_invoke.142
- __48-[ServiceImpl initWithQueue:noiEngine:isHelper:]_block_invoke.144
- __48-[ServiceImpl initWithQueue:noiEngine:isHelper:]_block_invoke.147
- __48-[ServiceImpl initWithQueue:noiEngine:isHelper:]_block_invoke.149
- __49-[ServiceImpl waitForOSLogErrorSymptomWithReply:]_block_invoke.182
- __49-[ServiceImpl waitForOSLogErrorSymptomWithReply:]_block_invoke.184
- __52-[ServiceImpl createSnapshotFor:pred:actions:reply:]_block_invoke.164
- __52-[ServiceImpl resetDataFor:nameKind:inScopes:reply:]_block_invoke.172
- __55-[ServiceImpl assertFactString:module:asSymptom:reply:]_block_invoke.190
- __83-[ServiceImpl performQueryOnEntity:fetchRequestProperties:pred:sort:actions:reply:]_block_invoke.163
- __block_literal_global.133
- _objc_msgSend$_updateLiveUsage:wifiIn:wifiOut:cellIn:cellOut:wiredIn:wiredOut:xIn:xOut:isJumboFlow:isExpensive:closing:
- _objc_msgSend$donateBiomeEventForEdgeSelectionWithPrefix:interfaceType:radioType:radioBand:reply:
- _objc_msgSend$fetchEstimatedISOCountryCode
CStrings:
+ "  %ld total reports for the day."
+ " NOT"
+ "#"
+ "/System/Library/Frameworks/CoreLocation.framework/CoreLocation"
+ "/System/Library/PrivateFrameworks/CoreRoutine.framework/CoreRoutine"
+ "/System/Library/PrivateFrameworks/MobileWiFi.framework"
+ "0123456789bcdefghjkmnpqrstuvwxyz"
+ "@\"CLLocationManager\""
+ "@\"LocationStateRelay\""
+ "@\"NSBundle\""
+ "@\"RTRoutineManager\""
+ "@40@0:8Q16d24d32"
+ "Already has a pending location request.  Resetting location timeout and removing expired requests."
+ "B24@0:8@\"CLLocationManager\"16"
+ "CLCopyTechnologiesInUse"
+ "CLGeocoder"
+ "CLLocation"
+ "CLLocationManager"
+ "CLLocationManagerClassRef"
+ "CLLocationManagerDelegate"
+ "CoreLocation Authorization Status for MobileWiFi is kCLAuthorizationStatusAuthorizedAlways"
+ "CoreLocation Authorization Status for MobileWiFi is kCLAuthorizationStatusAuthorizedWhenInUse"
+ "CoreLocation Authorization Status for MobileWiFi is kCLAuthorizationStatusDenied"
+ "CoreLocation Authorization Status for MobileWiFi is kCLAuthorizationStatusNotDetermined"
+ "CoreLocation Authorization Status for MobileWiFi is kCLAuthorizationStatusRestricted"
+ "CoreLocation Authorization Status for MobileWiFi is unknown status %d"
+ "CoreLocation failed to load due to %s\n"
+ "CoreLocation mobileWiFiLocationManager is nil."
+ "CoreRoutine failed to load due to %s\n"
+ "CoreRoutine routineManager is null."
+ "Did not receive location from MobileWiFiLocationManager after %d seconds, clearing pending block."
+ "GPS (baseline) - not implemented for platform"
+ "GPS is%s in use"
+ "GeoIP: (macOS) Biome donation for EdgeSelection with prefix: %{private}@, interface: %@, radio: %@, band: %@, latitude: %f, longitude: %f, elapsed/threshold: %f/%d sec"
+ "GeoIP: Computed geohash for latitude: %f, longitude: %f, hashLength: %zu, geohash: %@"
+ "GeoIP: Computing geohash for latitude: %f, longitude: %f, hashLength: %zu"
+ "GeoIP: Failed to get location, error: %@"
+ "GeoIP: Failed to load CLLocation or CLGeocoder"
+ "GeoIP: Missing geohash: %@, return"
+ "GeoIP: Missing isoCountryCode: %@ or city: %@, return"
+ "GeoIP: Reverse geocoding city: %{private}@, countryCode: %{private}@"
+ "GeoIP: Reverse geocoding failed, error: %@"
+ "GeoIP: Successfully loaded CLLocation and CLGeocoder"
+ "GeoIP: Timed out waiting for reverse geocoding, error: %ld"
+ "Gym"
+ "Home"
+ "ISOcountryCode"
+ "Invalid parameter not satisfying: %@"
+ "Just marked MobileWiFi as having received location"
+ "LOI type %@ is %s"
+ "LOI: location = <%{sensitive}f, %{sensitive}f>, type (as received from CoreRoutine) = %{sensitive}ld"
+ "LOI: locationManagerDidChangeAuthorization err = %ld"
+ "LOI: loi is null with error = %@"
+ "Location request failed with error: %@"
+ "Location requested at %@ but LocationStateRelay has not received a location at %@ (> %d seconds limit)."
+ "Location requested at %@ but the received location was determined at %@ (%.4f > %d limit)."
+ "LocationManager (%p) or CopyTechnologiesInUse (%p) is NULL."
+ "Number of pendingLOIBlocks = %lu, desiredAccuracy = %f"
+ "RTRoutineManager"
+ "Replying LOI for location requested at %@ (location determined at %@)"
+ "Requesting location from MobileWiFiLocationManager"
+ "SYMPTOM_BARCODE_ACTIVATION"
+ "School"
+ "Successfully loaded CoreLocation"
+ "SymptomAnalytics ServiceImpl: client has 'configuration' entitlement, rate-limit check waived"
+ "SymptomAnalytics ServiceImpl: found non-zero (%ld) fetch-offset (part of batched queries), rate-limit check waived"
+ "SymptomAnalytics ServiceImpl: query passed rate-limit check"
+ "T@\"NSArray\",&,V_allLOIs"
+ "TB,N,V_gpsInUse"
+ "Unable to set configuration object when class name is nil! {object:%@}"
+ "Work"
+ "_allLOIs"
+ "_gpsInUse"
+ "_internalQueue"
+ "_liveUsageCountForProcess: encountered unexpected nil tag (%llu previous errors)"
+ "_liveUsagePackForProcess: encountered unexpected nil tag (%llu previous errors)"
+ "_locationRelay"
+ "_updateLiveUsage:wifiIn:wifiOut:cellIn:cellOut:wiredIn:wiredOut:btIn:btOut:xIn:xOut:isJumboFlow:isExpensive:closing:"
+ "addPendingLOIBlocks:"
+ "allLOIs"
+ "authorizationStatusForBundle:"
+ "authorizedToUseCoreRoutine"
+ "authorizedToUseCoreRoutine is FALSE"
+ "btIN"
+ "btIN_exp"
+ "btOUT"
+ "btOUT_exp"
+ "bundleWithPath:"
+ "callPendingLOIBlocksWithCLLocation:LOI:andError:"
+ "clCopyTechnologiesInUseFunc"
+ "cleanUpPendingLOIBlocks"
+ "com.apple.symptoms.location.queue"
+ "coordinate"
+ "coordinatesToGeoHashWithLength:latitude:longitude:"
+ "coreLocationDyLibHandle"
+ "coreRoutineDyLibHandle"
+ "deltaAccountingRxCompanionLinkBluetoothBytes"
+ "deltaAccountingTxCompanionLinkBluetoothBytes"
+ "determineIfLocationOfInterestIsKnownOfType failed with error: %@"
+ "determineIfLocationOfInterestIsKnownOfType:queue:reply:"
+ "donateBiomeEventForEdgeSelectionWithPrefix:interfaceType:radioType:radioBand:latitude:longitude:reply:"
+ "fetchCurrentLocationLOIOnQueue:desiredAccuracy:reply:"
+ "fetchLocationOfInterestAtLocation:withHandler:"
+ "fetchLocationsOfInterestOfType:withHandler:"
+ "gpsInUse"
+ "hashLength <= GEOHASH_MAX_LENGTH"
+ "horizontalAccuracy"
+ "initWithEffectiveBundle:delegate:onQueue:"
+ "initWithLatitude:longitude:"
+ "kNotificationBarcodeActivation"
+ "known"
+ "latitude"
+ "loadCoreLocation"
+ "loadCoreLocation failed"
+ "loadCoreRoutine"
+ "loadCoreRoutine failed"
+ "locality"
+ "locationManager:didChangeAuthorizationStatus:"
+ "locationManager:didDetermineState:forRegion:"
+ "locationManager:didEnterRegion:"
+ "locationManager:didExitRegion:"
+ "locationManager:didFailRangingBeaconsForConstraint:error:"
+ "locationManager:didFailWithError:"
+ "locationManager:didFinishDeferredUpdatesWithError:"
+ "locationManager:didRangeBeacons:inRegion:"
+ "locationManager:didRangeBeacons:satisfyingConstraint:"
+ "locationManager:didStartMonitoringForRegion:"
+ "locationManager:didUpdateHeading:"
+ "locationManager:didUpdateLocations:"
+ "locationManager:didUpdateToLocation:fromLocation:"
+ "locationManager:didVisit:"
+ "locationManager:monitoringDidFailForRegion:withError:"
+ "locationManager:rangingBeaconsDidFailForRegion:withError:"
+ "locationManagerDidChangeAuthorization:"
+ "locationManagerDidPauseLocationUpdates:"
+ "locationManagerDidResumeLocationUpdates:"
+ "locationManagerShouldDisplayHeadingCalibration:"
+ "locationRequestTimer"
+ "locationServicesEnabled"
+ "locationServicesEnabled is FALSE"
+ "longitude"
+ "markAsHavingReceivedLocation"
+ "mobileWiFiBundle"
+ "mobileWiFiLocationManager"
+ "not known"
+ "pendingLOIBlocks"
+ "preflightFrameworks"
+ "requestLocation"
+ "reverseGeocodeLocation:completionHandler:"
+ "routineManager"
+ "rtLOITypeToString:"
+ "setAllLOIs:"
+ "setBtIN:"
+ "setBtIN_exp:"
+ "setBtOUT:"
+ "setBtOUT_exp:"
+ "setDesiredAccuracy:"
+ "setGpsInUse:"
+ "showLocationArrow"
+ "unloadFrameworks"
+ "v116@0:8@16q24q32q40q48q56q64q72q80q88q96B104B108B112"
+ "v24@0:8@\"CLLocationManager\"16"
+ "v24@?0@\"RTLocationOfInterest\"8@\"NSError\"16"
+ "v28@0:8@\"CLLocationManager\"16i24"
+ "v32@0:8@\"CLLocationManager\"16@\"CLHeading\"24"
+ "v32@0:8@\"CLLocationManager\"16@\"CLRegion\"24"
+ "v32@0:8@\"CLLocationManager\"16@\"CLVisit\"24"
+ "v32@0:8@\"CLLocationManager\"16@\"NSArray\"24"
+ "v32@0:8@\"CLLocationManager\"16@\"NSError\"24"
+ "v32@?0@\"NSDate\"8@?<v@?@\"RTLocationOfInterest\"@\"CLLocation\"@\"NSError\">16^B24"
+ "v32@?0@\"RTLocationOfInterest\"8@\"CLLocation\"16@\"NSError\"24"
+ "v40@0:8@\"CLLocationManager\"16@\"CLBeaconIdentityConstraint\"24@\"NSError\"32"
+ "v40@0:8@\"CLLocationManager\"16@\"CLBeaconRegion\"24@\"NSError\"32"
+ "v40@0:8@\"CLLocationManager\"16@\"CLLocation\"24@\"CLLocation\"32"
+ "v40@0:8@\"CLLocationManager\"16@\"CLRegion\"24@\"NSError\"32"
+ "v40@0:8@\"CLLocationManager\"16@\"NSArray\"24@\"CLBeaconIdentityConstraint\"32"
+ "v40@0:8@\"CLLocationManager\"16@\"NSArray\"24@\"CLBeaconRegion\"32"
+ "v40@0:8@\"CLLocationManager\"16q24@\"CLRegion\"32"
+ "v40@0:8@16d24@?32"
+ "v40@0:8@16q24@32"
+ "v40@0:8q16@24@?32"
+ "v72@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32@\"NSString\"40d48d56@?<v@?@\"NSDictionary\"@\"NSError\">64"
+ "v72@0:8@16@24@32@40d48d56@?64"
- "  %ld total reports for the day is still under the limit of %d."
- "  Cannot generate report for unknown trigger type %lu."
- "  Reached limit of %ld RESOURCE_NOTIFY reports per day. Disallow report."
- "-f"
- "-l"
- "<-"
- "GeoIP: (macOS) Biome donation for EdgeSelection with prefix: %{private}@, interface: %@, radio: %@, band: %@, elapsed/threshold: %f/%d sec"
- "GeoIP: Missing isoCountryCode: %@, return"
- "T"
- "Unexpected network type %ld in journal entry"
- "_updateLiveUsage:wifiIn:wifiOut:cellIn:cellOut:wiredIn:wiredOut:xIn:xOut:isJumboFlow:isExpensive:closing:"
- "ab"
- "do"
- "donateBiomeEventForEdgeSelectionWithPrefix:interfaceType:radioType:radioBand:reply:"
- "ff"
- "kNetworkType-unknown"
- "t"
- "v100@0:8@16q24q32q40q48q56q64q72q80B88B92B96"
- "v56@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32@\"NSString\"40@?<v@?@\"NSDictionary\"@\"NSError\">48"

```
