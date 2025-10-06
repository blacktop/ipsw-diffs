## libcoreroutine.dylib

> `/usr/lib/libcoreroutine.dylib`

```diff

-900.0.12.0.0
-  __TEXT.__text: 0x4691b0
+900.0.25.0.0
+  __TEXT.__text: 0x477460
   __TEXT.__auth_stubs: 0x1880
-  __TEXT.__objc_methlist: 0x22e38
-  __TEXT.__const: 0x1ac8
-  __TEXT.__gcc_except_tab: 0x17520
-  __TEXT.__oslogstring: 0x52158
-  __TEXT.__cstring: 0x3451f
+  __TEXT.__objc_methlist: 0x23668
+  __TEXT.__const: 0x1b28
+  __TEXT.__gcc_except_tab: 0x17c38
+  __TEXT.__oslogstring: 0x53831
+  __TEXT.__cstring: 0x34fb3
   __TEXT.__ustring: 0x16
-  __TEXT.__dlopen_cstrs: 0x254
-  __TEXT.__unwind_info: 0xa964
-  __TEXT.__objc_classname: 0x4511
-  __TEXT.__objc_methname: 0x6bcff
-  __TEXT.__objc_methtype: 0xa6f9
-  __TEXT.__objc_stubs: 0x40b00
+  __TEXT.__dlopen_cstrs: 0x1fe
+  __TEXT.__unwind_info: 0xa928
+  __TEXT.__objc_classname: 0x462d
+  __TEXT.__objc_methname: 0x6dc73
+  __TEXT.__objc_methtype: 0xa9a4
+  __TEXT.__objc_stubs: 0x41a00
   __DATA_CONST.__got: 0xa70
-  __DATA_CONST.__const: 0xb9c0
-  __DATA_CONST.__objc_classlist: 0x10b0
+  __DATA_CONST.__const: 0xbb20
+  __DATA_CONST.__objc_classlist: 0x10e0
   __DATA_CONST.__objc_catlist: 0x2c8
-  __DATA_CONST.__objc_protolist: 0x2c0
+  __DATA_CONST.__objc_protolist: 0x2c8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x34360
-  __DATA_CONST.__objc_selrefs: 0x129d8
+  __DATA_CONST.__objc_const: 0x35058
+  __DATA_CONST.__objc_selrefs: 0x12e18
   __DATA_CONST.__objc_protorefs: 0x108
-  __DATA_CONST.__objc_classrefs: 0x1cb8
-  __DATA_CONST.__objc_superrefs: 0xe50
+  __DATA_CONST.__objc_classrefs: 0x1d08
+  __DATA_CONST.__objc_superrefs: 0xe80
   __DATA_CONST.__objc_arraydata: 0x1f58
-  __AUTH_CONST.__const: 0x2680
-  __AUTH_CONST.__cfstring: 0x1fc60
-  __AUTH_CONST.__objc_const: 0xdd18
-  __AUTH_CONST.__objc_intobj: 0x30a8
-  __AUTH_CONST.__objc_doubleobj: 0x900
+  __AUTH_CONST.__const: 0x2720
+  __AUTH_CONST.__cfstring: 0x201a0
+  __AUTH_CONST.__objc_const: 0xdf58
+  __AUTH_CONST.__objc_intobj: 0x30c0
+  __AUTH_CONST.__objc_doubleobj: 0x910
   __AUTH_CONST.__objc_arrayobj: 0xbd0
   __AUTH_CONST.__objc_dictobj: 0xf0
   __AUTH_CONST.__objc_floatobj: 0x20
   __AUTH_CONST.__auth_got: 0xc50
-  __AUTH.__objc_data: 0x1cc0
-  __DATA.__objc_ivar: 0x1c90
-  __DATA.__data: 0x2488
+  __AUTH.__objc_data: 0x1ea0
+  __DATA.__objc_ivar: 0x1d18
+  __DATA.__data: 0x24e8
   __DATA.__bss: 0x60
-  __DATA_DIRTY.__objc_ivar: 0xca4
+  __DATA_DIRTY.__objc_ivar: 0xce8
   __DATA_DIRTY.__objc_data: 0x8a20
   __DATA_DIRTY.__data: 0x4b0
-  __DATA_DIRTY.__bss: 0x168
+  __DATA_DIRTY.__bss: 0x158
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CloudKit.framework/CloudKit
   - /System/Library/Frameworks/Contacts.framework/Contacts

   - /System/Library/PrivateFrameworks/AssistantServices.framework/AssistantServices
   - /System/Library/PrivateFrameworks/BiomeLibrary.framework/BiomeLibrary
   - /System/Library/PrivateFrameworks/BiomeStreams.framework/BiomeStreams
+  - /System/Library/PrivateFrameworks/BiometricKit.framework/BiometricKit
   - /System/Library/PrivateFrameworks/BluetoothManager.framework/BluetoothManager
   - /System/Library/PrivateFrameworks/CarKit.framework/CarKit
   - /System/Library/PrivateFrameworks/CommunicationsFilter.framework/CommunicationsFilter

   - /System/Library/PrivateFrameworks/CoreTime.framework/CoreTime
   - /System/Library/PrivateFrameworks/CoreUtils.framework/CoreUtils
   - /System/Library/PrivateFrameworks/Espresso.framework/Espresso
+  - /System/Library/PrivateFrameworks/FamilyCircle.framework/FamilyCircle
   - /System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices
   - /System/Library/PrivateFrameworks/GeoServices.framework/GeoServices
   - /System/Library/PrivateFrameworks/HeroDataClient.framework/HeroDataClient

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 27A2E5E8-2AF5-3D10-9CC3-9454655AF314
-  Functions: 15231
-  Symbols:   49776
-  CStrings:  30656
+  UUID: E6DCD95B-3088-3E74-BB5C-137DC1FC0CC4
+  Functions: 15443
+  Symbols:   50439
+  CStrings:  31072
 
Symbols:
+ +[RTAuthorizedLocationManager _locationAvailabilityFromCLLocation:]
+ +[RTAuthorizedLocationVisitLog decodeTimeSourceWithValue:isRetroRegistration:isTrusted:]
+ +[RTAuthorizedLocationVisitLog encodeTimeSourceWithValue:isTrusted:isRetroRegistration:]
+ +[RTDaemonClientRegistrarPeopleDiscovery supportsSecureCoding]
+ +[RTPeopleDensityRecord _computeDensityScore:scanDuration:forRecords:]
+ +[RTPeopleDensityRecord _computeMeanOfRssi:]
+ +[RTPeopleDensityRecord computeRssiHistogramForAdvs:]
+ +[RTPeopleDiscoveryProvider _convertObservationIntervalToDouble:]
+ +[RTPeopleDiscoveryProvider _scanLevelFromServiceLevel:observationInterval:]
+ +[RTPeopleDiscoveryProvider periodicPurgePolicy]
+ +[SMTriggerDestinationStateMO managedObjectWithSessionIdentifier:lastLockDate:lastUnlockDate:predominantModeOfTransport:currentStatus:currentStatusDate:date:shouldRetryETAQuery:numberOfETARetries:upperBoundEtaCrowFliesUpperBoundEta:upperBoundEtaMapsUpperBoundEta:roundTripReminderDate:timeToUpdateStatus:mapsExpectedTravelTime:remainingDistance:managedObjectContext:]
+ -[RTAddressMO description]
+ -[RTAuthorizedLocation initWithLoi:dwellTime:numberOfDaysVisited:ageDaysFirstVisit:ageDaysFirstRegisteredVisit:locationTechnologyAvailability:visitsWithTechnologyAnnotation:visitsWithGPS:visitsWithWiFiHI:]
+ -[RTAuthorizedLocation locationTechnologyAvailability]
+ -[RTAuthorizedLocation rank]
+ -[RTAuthorizedLocation setRank:]
+ -[RTAuthorizedLocation visitsWithGPS]
+ -[RTAuthorizedLocation visitsWithTechnologyAnnotation]
+ -[RTAuthorizedLocation visitsWithWiFiHI]
+ -[RTAuthorizedLocationBiometricsManager .cxx_destruct]
+ -[RTAuthorizedLocationBiometricsManager _getTimeSinceLastSuccessfulBiometricAuthentication:]
+ -[RTAuthorizedLocationBiometricsManager dateOfLastUpdate]
+ -[RTAuthorizedLocationBiometricsManager dateOfMostRecentBiometricAuthentication]
+ -[RTAuthorizedLocationBiometricsManager defaultOverrideTimeSinceLastSuccessfulBiometricAuthentication:]
+ -[RTAuthorizedLocationBiometricsManager defaultsManager]
+ -[RTAuthorizedLocationBiometricsManager initWithTrustedTimeCache:defaultsManager:]
+ -[RTAuthorizedLocationBiometricsManager platform]
+ -[RTAuthorizedLocationBiometricsManager setDateOfLastUpdate:]
+ -[RTAuthorizedLocationBiometricsManager setDateOfMostRecentBiometricAuthentication:]
+ -[RTAuthorizedLocationBiometricsManager trustedTimeCache]
+ -[RTAuthorizedLocationBiometricsManager updateDateOfLastSuccessfulBiometricAuthentication]
+ -[RTAuthorizedLocationCurationMetrics fractionOfVisitsToTopLOIWithGPS]
+ -[RTAuthorizedLocationCurationMetrics fractionOfVisitsToTopLOIWithWiFiHI]
+ -[RTAuthorizedLocationCurationMetrics setFractionOfVisitsToTopLOIWithGPS:]
+ -[RTAuthorizedLocationCurationMetrics setFractionOfVisitsToTopLOIWithWiFiHI:]
+ -[RTAuthorizedLocationCurationMetrics setVisitsToTopLOIWithTechAvailabilityKnown:]
+ -[RTAuthorizedLocationCurationMetrics visitsToTopLOIWithTechAvailabilityKnown]
+ -[RTAuthorizedLocationDatabaseInitializationMetrics eraseInstallInitializationAttemptCount]
+ -[RTAuthorizedLocationDatabaseInitializationMetrics eraseInstallInitializationCompletionTimeHours]
+ -[RTAuthorizedLocationDatabaseInitializationMetrics init]
+ -[RTAuthorizedLocationDatabaseInitializationMetrics numberOfALOIsGeneratedDuringEraseInstallInitialization]
+ -[RTAuthorizedLocationDatabaseInitializationMetrics numberOfVisitsRegisteredDuringEraseInstallInitialization]
+ -[RTAuthorizedLocationDatabaseInitializationMetrics setEraseInstallInitializationAttemptCount:]
+ -[RTAuthorizedLocationDatabaseInitializationMetrics setEraseInstallInitializationCompletionTimeHours:]
+ -[RTAuthorizedLocationDatabaseInitializationMetrics setNumberOfALOIsGeneratedDuringEraseInstallInitialization:]
+ -[RTAuthorizedLocationDatabaseInitializationMetrics setNumberOfVisitsRegisteredDuringEraseInstallInitialization:]
+ -[RTAuthorizedLocationManager _checkConfiguration]
+ -[RTAuthorizedLocationManager _computeLocationTechnologyAvailabilityForDateInterval:]
+ -[RTAuthorizedLocationManager _computeLocationTechnologyExpectationFromHistoricalAvailability:]
+ -[RTAuthorizedLocationManager _fetchAuthorizedLocationExtendedStatus:]
+ -[RTAuthorizedLocationManager _fetchAuthorizedLocationExtendedStatusWithMetrics:]
+ -[RTAuthorizedLocationManager _isExpeditedSyncAndLearnRequired]
+ -[RTAuthorizedLocationManager _isRoutineEnabled]
+ -[RTAuthorizedLocationManager _loadEraseInstallInitializationXPCCriteriaFromDefaults]
+ -[RTAuthorizedLocationManager _registerForDeviceUnlockNotification]
+ -[RTAuthorizedLocationManager _runEraseInstallDatabaseInitialization:]
+ -[RTAuthorizedLocationManager _setupEraseInstallDatabaseInitializationActivity]
+ -[RTAuthorizedLocationManager _updateMostRecentDateAtWhichDeviceDataIsTrusted]
+ -[RTAuthorizedLocationManager allowUnsecureTimeFallback]
+ -[RTAuthorizedLocationManager authorizationManager]
+ -[RTAuthorizedLocationManager biometricsManager]
+ -[RTAuthorizedLocationManager eraseInstallDatabaseInitializationAttemptCount]
+ -[RTAuthorizedLocationManager eraseInstallDatabaseInitializationMaxAttemptCount]
+ -[RTAuthorizedLocationManager eraseInstallInitializationStartDate]
+ -[RTAuthorizedLocationManager eraseInstallInitializationXpcCriteria]
+ -[RTAuthorizedLocationManager eraseVisitLogDatabase:]
+ -[RTAuthorizedLocationManager fetchAuthorizedLocationExtendedStatus:]
+ -[RTAuthorizedLocationManager fetchVisitLogsWithOptions:handler:]
+ -[RTAuthorizedLocationManager initWithVisitManager:locationManager:distanceCalculator:learnedLocationManager:motionActivityManager:visitLogStore:defaultsManager:xpcActivityManager:dataProtectionManager:persistenceMirroringManager:platform:authorizationManager:]
+ -[RTAuthorizedLocationManager isEraseInstallDatabaseInitializationRequired]
+ -[RTAuthorizedLocationManager isSupportedDevice]
+ -[RTAuthorizedLocationManager metrics]
+ -[RTAuthorizedLocationManager mostRecentDateAtWhichDeviceDataIsTrusted]
+ -[RTAuthorizedLocationManager persistenceMirroringManager]
+ -[RTAuthorizedLocationManager platform]
+ -[RTAuthorizedLocationManager runEraseInstallDatabaseInitialization:]
+ -[RTAuthorizedLocationManager setAllowUnsecureTimeFallback:]
+ -[RTAuthorizedLocationManager setAuthorizationManager:]
+ -[RTAuthorizedLocationManager setEraseInstallDatabaseInitializationAttemptCount:]
+ -[RTAuthorizedLocationManager setEraseInstallDatabaseInitializationMaxAttemptCount:]
+ -[RTAuthorizedLocationManager setEraseInstallInitializationStartDate:]
+ -[RTAuthorizedLocationManager setEraseInstallInitializationXpcCriteria:]
+ -[RTAuthorizedLocationManager setIsEraseInstallDatabaseInitializationRequired:]
+ -[RTAuthorizedLocationManager setMetrics:]
+ -[RTAuthorizedLocationManager setMostRecentDateAtWhichDeviceDataIsTrusted:]
+ -[RTAuthorizedLocationMetrics .cxx_destruct]
+ -[RTAuthorizedLocationMetrics convertToDictionary]
+ -[RTAuthorizedLocationMetrics curationMetrics]
+ -[RTAuthorizedLocationMetrics daemonStartDate]
+ -[RTAuthorizedLocationMetrics initWithDaemonStartDate:]
+ -[RTAuthorizedLocationMetrics initializationMetrics]
+ -[RTAuthorizedLocationMetrics lastQueryMetricSubmissionDate]
+ -[RTAuthorizedLocationMetrics locationServicesEnabled]
+ -[RTAuthorizedLocationMetrics queryMetrics]
+ -[RTAuthorizedLocationMetrics routineEnabled]
+ -[RTAuthorizedLocationMetrics setCurationMetrics:]
+ -[RTAuthorizedLocationMetrics setInitializationMetrics:]
+ -[RTAuthorizedLocationMetrics setLastQueryMetricSubmissionDate:]
+ -[RTAuthorizedLocationMetrics setLocationServicesEnabled:]
+ -[RTAuthorizedLocationMetrics setQueryMetrics:]
+ -[RTAuthorizedLocationMetrics setRoutineEnabled:]
+ -[RTAuthorizedLocationMetrics submitToCoreAnalytics]
+ -[RTAuthorizedLocationMetrics timeSinceDaemonStart]
+ -[RTAuthorizedLocationMetrics timeSinceLastQueryMetricsSubmission]
+ -[RTAuthorizedLocationQueryMetrics isHistoricallyALowDiversityLocation]
+ -[RTAuthorizedLocationQueryMetrics setIsHistoricallyALowDiversityLocation:]
+ -[RTAuthorizedLocationVisitLog initWithVisitIdentifier:registrationDate:locationTechnologyAvailability:]
+ -[RTAuthorizedLocationVisitLog locationTechnologyAvailability]
+ -[RTAuthorizedLocationVisitLogStore _updateVisitLogDistantFutureFlagWithStatus:TrustedTimeAvailability:isRetroRegistration:]
+ -[RTAuthorizedLocationVisitLogStore getEraseInstallRetroRegistrationStatus]
+ -[RTAuthorizedLocationVisitLogStore setEraseInstallRetroRegistrationStatus:]
+ -[RTAuthorizedLocationVisitLogStore setTrustedTimeRecentAvailability:]
+ -[RTAuthorizedLocationVisitLogStore wasTrustedTimeRecentlyAvailable]
+ -[RTDaemonClient fetchOngoingPeopleDensity:]
+ -[RTDaemonClient peopleDiscoveryRegistrar:didReceivePeopleDensityUpdate:error:]
+ -[RTDaemonClient peopleDiscoveryRegistrar]
+ -[RTDaemonClient setPeopleDiscoveryRegistrar:]
+ -[RTDaemonClient startMonitoringForPeopleDiscovery:configuration:reply:]
+ -[RTDaemonClient stopMonitoringForPeopleDiscoveryWithReply:]
+ -[RTDaemonClientInternal eraseVisitLogDatabase:]
+ -[RTDaemonClientInternal fetchAuthorizedLocationExtendedStatus:]
+ -[RTDaemonClientInternal fetchVisitLogsWithDateInterval:reply:]
+ -[RTDaemonClientInternal forceAuthorizedLocationEraseInstallInitialization:]
+ -[RTDaemonClientRegistrarPeopleDiscovery .cxx_destruct]
+ -[RTDaemonClientRegistrarPeopleDiscovery _onPeopleDensityUpdateNotification:]
+ -[RTDaemonClientRegistrarPeopleDiscovery addPendingPeopleDensityUpdateBlock:failBlock:description:]
+ -[RTDaemonClientRegistrarPeopleDiscovery clientIdentifier]
+ -[RTDaemonClientRegistrarPeopleDiscovery configuration]
+ -[RTDaemonClientRegistrarPeopleDiscovery countOfPendingInvocations]
+ -[RTDaemonClientRegistrarPeopleDiscovery delegate]
+ -[RTDaemonClientRegistrarPeopleDiscovery dispatcher]
+ -[RTDaemonClientRegistrarPeopleDiscovery encodeWithCoder:]
+ -[RTDaemonClientRegistrarPeopleDiscovery initWithCoder:]
+ -[RTDaemonClientRegistrarPeopleDiscovery initWithPeopleDiscoveryProvider:queue:]
+ -[RTDaemonClientRegistrarPeopleDiscovery init]
+ -[RTDaemonClientRegistrarPeopleDiscovery invocationsPending]
+ -[RTDaemonClientRegistrarPeopleDiscovery onPeopleDensityUpdateNotification:]
+ -[RTDaemonClientRegistrarPeopleDiscovery peopleDiscoveryProvider]
+ -[RTDaemonClientRegistrarPeopleDiscovery queue]
+ -[RTDaemonClientRegistrarPeopleDiscovery registered]
+ -[RTDaemonClientRegistrarPeopleDiscovery setConfiguration:]
+ -[RTDaemonClientRegistrarPeopleDiscovery setDelegate:]
+ -[RTDaemonClientRegistrarPeopleDiscovery setDispatcher:]
+ -[RTDaemonClientRegistrarPeopleDiscovery setPeopleDiscoveryProvider:]
+ -[RTDaemonClientRegistrarPeopleDiscovery startMonitoringForPeopleDiscoveryWithIdentifier:configuration:]
+ -[RTDaemonClientRegistrarPeopleDiscovery stopMonitoringForPeopleDiscovery]
+ -[RTMapItemMO description]
+ -[RTPeopleDensityRecord fetchCurrentObservationBundle]
+ -[RTPeopleDensityRecord runningRecentBundle]
+ -[RTPeopleDensityRecord setRunningRecentBundle:]
+ -[RTPeopleDensityRecord updateConfidenceThreshold:]
+ -[RTPeopleDensityRecord updateObservationIntervalSeconds:]
+ -[RTPeopleDensityRecordRunningRecentObservation .cxx_destruct]
+ -[RTPeopleDensityRecordRunningRecentObservation addRecord:]
+ -[RTPeopleDensityRecordRunningRecentObservation currentConfidenceThreshold]
+ -[RTPeopleDensityRecordRunningRecentObservation currentObservationIntervalSeconds]
+ -[RTPeopleDensityRecordRunningRecentObservation getHistogram]
+ -[RTPeopleDensityRecordRunningRecentObservation init]
+ -[RTPeopleDensityRecordRunningRecentObservation runningAdvertisementsPerRecord]
+ -[RTPeopleDensityRecordRunningRecentObservation runningRecords]
+ -[RTPeopleDensityRecordRunningRecentObservation setCurrentConfidenceThreshold:]
+ -[RTPeopleDensityRecordRunningRecentObservation setCurrentObservationIntervalSeconds:]
+ -[RTPeopleDensityRecordRunningRecentObservation setRunningAdvertisementsPerRecord:]
+ -[RTPeopleDensityRecordRunningRecentObservation setRunningRecords:]
+ -[RTPeopleDensityRecordRunningRecentObservation trimRunningRecordsBeforeRef:]
+ -[RTPeopleDensityRecordRunningRecentObservation updateHistogramWithAdvs:]
+ -[RTPeopleDensitySingleRecord .cxx_destruct]
+ -[RTPeopleDensitySingleRecord setStartDatetime:]
+ -[RTPeopleDensitySingleRecord startDatetime]
+ -[RTPeopleDensityUpdateNotification .cxx_destruct]
+ -[RTPeopleDensityUpdateNotification densityBundles]
+ -[RTPeopleDensityUpdateNotification initWithPeopleDensityBundles:]
+ -[RTPeopleDiscoveryProvider _addClientConfiguration:withIdentifier:]
+ -[RTPeopleDiscoveryProvider _aggregateAndApplyConfiguration]
+ -[RTPeopleDiscoveryProvider _logClientConfigurations]
+ -[RTPeopleDiscoveryProvider _purgeEvents]
+ -[RTPeopleDiscoveryProvider _removeClientConfiguration:]
+ -[RTPeopleDiscoveryProvider addClient:withIdentifier:withConfiguration:]
+ -[RTPeopleDiscoveryProvider broughtUp]
+ -[RTPeopleDiscoveryProvider clientConfigurations]
+ -[RTPeopleDiscoveryProvider fetchMostRecentPeopleDensity:]
+ -[RTPeopleDiscoveryProvider momentsConfiguration]
+ -[RTPeopleDiscoveryProvider notificationHelper]
+ -[RTPeopleDiscoveryProvider onBufferedDevicesReceivedNotification]
+ -[RTPeopleDiscoveryProvider onCoreLocationProviderCameUpNotification]
+ -[RTPeopleDiscoveryProvider performPurgeOfType:referenceDate:completion:]
+ -[RTPeopleDiscoveryProvider removeClient:]
+ -[RTPeopleDiscoveryProvider setBroughtUp:]
+ -[RTPeopleDiscoveryProvider setClientConfigurations:]
+ -[RTPeopleDiscoveryProvider setMomentsConfiguration:]
+ -[RTPeopleDiscoveryProvider setNotificationHelper:]
+ -[RTTrustedTimeCache convertMachContinuousTicksToSeconds:]
+ -[RTVisitMO description]
+ -[RTXPCActivityCriteria isEqual:]
+ -[SMSuggestionsManager _getFAFamilyMembersFromAAAFamilyWithHandler:]
+ -[SMSuggestionsManager _getSMHandlesFromFAFamilyMembers:error:]
+ -[SMTriggerDestination _evaluateStatusUsingCurrentLocation:]
+ -[SMTriggerDestination idleMaxDistanceThreshold]
+ -[SMTriggerDestination idleTimeoutThreshold]
+ -[SMTriggerDestination originLocation]
+ -[SMTriggerDestination setIdleMaxDistanceThreshold:]
+ -[SMTriggerDestination setIdleTimeoutThreshold:]
+ -[SMTriggerDestination setOriginLocation:]
+ GCC_except_table145
+ GCC_except_table210
+ GCC_except_table97
+ _OBJC_CLASS_$_BKDevice
+ _OBJC_CLASS_$_BKDeviceManager
+ _OBJC_CLASS_$_FAFetchFamilyCircleRequest
+ _OBJC_CLASS_$_RTAuthorizedLocationBiometricsManager
+ _OBJC_CLASS_$_RTAuthorizedLocationDatabaseInitializationMetrics
+ _OBJC_CLASS_$_RTAuthorizedLocationMetrics
+ _OBJC_CLASS_$_RTDaemonClientRegistrarPeopleDiscovery
+ _OBJC_CLASS_$_RTPeopleDensityRecordRunningRecentObservation
+ _OBJC_CLASS_$_RTPeopleDensityUpdateNotification
+ _OBJC_CLASS_$_RTPeopleDiscoveryServiceConfiguration
+ _OBJC_IVAR_$_RTAuthorizedLocation._locationTechnologyAvailability
+ _OBJC_IVAR_$_RTAuthorizedLocation._rank
+ _OBJC_IVAR_$_RTAuthorizedLocation._visitsWithGPS
+ _OBJC_IVAR_$_RTAuthorizedLocation._visitsWithTechnologyAnnotation
+ _OBJC_IVAR_$_RTAuthorizedLocation._visitsWithWiFiHI
+ _OBJC_IVAR_$_RTAuthorizedLocationBiometricsManager._dateOfLastUpdate
+ _OBJC_IVAR_$_RTAuthorizedLocationBiometricsManager._dateOfMostRecentBiometricAuthentication
+ _OBJC_IVAR_$_RTAuthorizedLocationBiometricsManager._defaultsManager
+ _OBJC_IVAR_$_RTAuthorizedLocationBiometricsManager._platform
+ _OBJC_IVAR_$_RTAuthorizedLocationBiometricsManager._trustedTimeCache
+ _OBJC_IVAR_$_RTAuthorizedLocationCurationMetrics._fractionOfVisitsToTopLOIWithGPS
+ _OBJC_IVAR_$_RTAuthorizedLocationCurationMetrics._fractionOfVisitsToTopLOIWithWiFiHI
+ _OBJC_IVAR_$_RTAuthorizedLocationCurationMetrics._visitsToTopLOIWithTechAvailabilityKnown
+ _OBJC_IVAR_$_RTAuthorizedLocationDatabaseInitializationMetrics._eraseInstallInitializationAttemptCount
+ _OBJC_IVAR_$_RTAuthorizedLocationDatabaseInitializationMetrics._eraseInstallInitializationCompletionTimeHours
+ _OBJC_IVAR_$_RTAuthorizedLocationDatabaseInitializationMetrics._numberOfALOIsGeneratedDuringEraseInstallInitialization
+ _OBJC_IVAR_$_RTAuthorizedLocationDatabaseInitializationMetrics._numberOfVisitsRegisteredDuringEraseInstallInitialization
+ _OBJC_IVAR_$_RTAuthorizedLocationMetrics._curationMetrics
+ _OBJC_IVAR_$_RTAuthorizedLocationMetrics._daemonStartDate
+ _OBJC_IVAR_$_RTAuthorizedLocationMetrics._initializationMetrics
+ _OBJC_IVAR_$_RTAuthorizedLocationMetrics._lastQueryMetricSubmissionDate
+ _OBJC_IVAR_$_RTAuthorizedLocationMetrics._locationServicesEnabled
+ _OBJC_IVAR_$_RTAuthorizedLocationMetrics._queryMetrics
+ _OBJC_IVAR_$_RTAuthorizedLocationMetrics._routineEnabled
+ _OBJC_IVAR_$_RTAuthorizedLocationQueryMetrics._isHistoricallyALowDiversityLocation
+ _OBJC_IVAR_$_RTAuthorizedLocationVisitLog._locationTechnologyAvailability
+ _OBJC_IVAR_$_RTDaemonClient._peopleDiscoveryRegistrar
+ _OBJC_IVAR_$_RTPeopleDensityRecord._runningRecentBundle
+ _OBJC_IVAR_$_RTPeopleDensityRecordRunningRecentObservation._currentConfidenceThreshold
+ _OBJC_IVAR_$_RTPeopleDensityRecordRunningRecentObservation._currentObservationIntervalSeconds
+ _OBJC_IVAR_$_RTPeopleDensityRecordRunningRecentObservation._runningAdvertisementsPerRecord
+ _OBJC_IVAR_$_RTPeopleDensityRecordRunningRecentObservation._runningRecords
+ _OBJC_IVAR_$_RTPeopleDensitySingleRecord._startDatetime
+ _OBJC_IVAR_$_RTPeopleDensityUpdateNotification._densityBundles
+ _OBJC_IVAR_$_SMTriggerDestination._idleMaxDistanceThreshold
+ _OBJC_IVAR_$_SMTriggerDestination._idleTimeoutThreshold
+ _OBJC_IVAR_$_SMTriggerDestination._originLocation
+ _OBJC_METACLASS_$_RTAuthorizedLocationBiometricsManager
+ _OBJC_METACLASS_$_RTAuthorizedLocationDatabaseInitializationMetrics
+ _OBJC_METACLASS_$_RTAuthorizedLocationMetrics
+ _OBJC_METACLASS_$_RTDaemonClientRegistrarPeopleDiscovery
+ _OBJC_METACLASS_$_RTPeopleDensityRecordRunningRecentObservation
+ _OBJC_METACLASS_$_RTPeopleDensityUpdateNotification
+ _ObservationIntervalPriority
+ _RTDaemonClientRegistrarPeopleDiscoveryCodingKeyClientIdentifier
+ _RTDaemonClientRegistrarPeopleDiscoveryCodingKeyConfiguration
+ _SMTriggerDestinationIdleMaxDistanceThreshold
+ _SMTriggerDestinationIdleTimeoutThreshold
+ _StorageDurationPriority
+ __OBJC_$_CLASS_METHODS_RTAuthorizedLocationManager
+ __OBJC_$_CLASS_METHODS_RTDaemonClientRegistrarPeopleDiscovery
+ __OBJC_$_CLASS_PROP_LIST_RTDaemonClientRegistrarPeopleDiscovery
+ __OBJC_$_INSTANCE_METHODS_RTAuthorizedLocationBiometricsManager
+ __OBJC_$_INSTANCE_METHODS_RTAuthorizedLocationDatabaseInitializationMetrics
+ __OBJC_$_INSTANCE_METHODS_RTAuthorizedLocationMetrics
+ __OBJC_$_INSTANCE_METHODS_RTDaemonClientRegistrarPeopleDiscovery
+ __OBJC_$_INSTANCE_METHODS_RTPeopleDensityRecordRunningRecentObservation
+ __OBJC_$_INSTANCE_METHODS_RTPeopleDensityUpdateNotification
+ __OBJC_$_INSTANCE_VARIABLES_RTAuthorizedLocationBiometricsManager
+ __OBJC_$_INSTANCE_VARIABLES_RTAuthorizedLocationDatabaseInitializationMetrics
+ __OBJC_$_INSTANCE_VARIABLES_RTAuthorizedLocationMetrics
+ __OBJC_$_INSTANCE_VARIABLES_RTDaemonClientRegistrarPeopleDiscovery
+ __OBJC_$_INSTANCE_VARIABLES_RTPeopleDensityRecordRunningRecentObservation
+ __OBJC_$_INSTANCE_VARIABLES_RTPeopleDensityUpdateNotification
+ __OBJC_$_PROP_LIST_RTAuthorizedLocationBiometricsManager
+ __OBJC_$_PROP_LIST_RTAuthorizedLocationDatabaseInitializationMetrics
+ __OBJC_$_PROP_LIST_RTAuthorizedLocationMetrics
+ __OBJC_$_PROP_LIST_RTDaemonClientRegistrarPeopleDiscovery
+ __OBJC_$_PROP_LIST_RTPeopleDensityRecordRunningRecentObservation
+ __OBJC_$_PROP_LIST_RTPeopleDensityUpdateNotification
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_RTDaemonClientRegistrarPeopleDiscoveryProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_RTDaemonClientRegistrarPeopleDiscoveryProtocol
+ __OBJC_$_PROTOCOL_REFS_RTDaemonClientRegistrarPeopleDiscoveryProtocol
+ __OBJC_CLASS_PROTOCOLS_$_RTDaemonClientRegistrarPeopleDiscovery
+ __OBJC_CLASS_RO_$_RTAuthorizedLocationBiometricsManager
+ __OBJC_CLASS_RO_$_RTAuthorizedLocationDatabaseInitializationMetrics
+ __OBJC_CLASS_RO_$_RTAuthorizedLocationMetrics
+ __OBJC_CLASS_RO_$_RTDaemonClientRegistrarPeopleDiscovery
+ __OBJC_CLASS_RO_$_RTPeopleDensityRecordRunningRecentObservation
+ __OBJC_CLASS_RO_$_RTPeopleDensityUpdateNotification
+ __OBJC_LABEL_PROTOCOL_$_RTDaemonClientRegistrarPeopleDiscoveryProtocol
+ __OBJC_METACLASS_RO_$_RTAuthorizedLocationBiometricsManager
+ __OBJC_METACLASS_RO_$_RTAuthorizedLocationDatabaseInitializationMetrics
+ __OBJC_METACLASS_RO_$_RTAuthorizedLocationMetrics
+ __OBJC_METACLASS_RO_$_RTDaemonClientRegistrarPeopleDiscovery
+ __OBJC_METACLASS_RO_$_RTPeopleDensityRecordRunningRecentObservation
+ __OBJC_METACLASS_RO_$_RTPeopleDensityUpdateNotification
+ __OBJC_PROTOCOL_$_RTDaemonClientRegistrarPeopleDiscoveryProtocol
+ ___117-[RTAuthorizedLocationManager _assertRecentMotionActivityAndLocationHistoryAreConsistentForAuthorizedLocation:visit:]_block_invoke.98
+ ___124-[RTAuthorizedLocationVisitLogStore _updateVisitLogDistantFutureFlagWithStatus:TrustedTimeAvailability:isRetroRegistration:]_block_invoke
+ ___124-[RTAuthorizedLocationVisitLogStore _updateVisitLogDistantFutureFlagWithStatus:TrustedTimeAvailability:isRetroRegistration:]_block_invoke_2
+ ___147-[RTPeopleDiscoveryProvider initWithDefaultManager:proximityEventStore:peopleDensityStore:advertisementManager:dataProtectionManager:timerManager:]_block_invoke
+ ___147-[RTPeopleDiscoveryProvider initWithDefaultManager:proximityEventStore:peopleDensityStore:advertisementManager:dataProtectionManager:timerManager:]_block_invoke_2
+ ___147-[RTPeopleDiscoveryProvider initWithDefaultManager:proximityEventStore:peopleDensityStore:advertisementManager:dataProtectionManager:timerManager:]_block_invoke_3
+ ___147-[RTPeopleDiscoveryProvider initWithDefaultManager:proximityEventStore:peopleDensityStore:advertisementManager:dataProtectionManager:timerManager:]_block_invoke_4
+ ___25-[RTDaemonClient restore]_block_invoke.526
+ ___25-[RTDaemonClient restore]_block_invoke.529
+ ___25-[RTDaemonClient restore]_block_invoke.535
+ ___35-[RTPeopleDiscoveryProvider _setup]_block_invoke.104
+ ___35-[RTPeopleDiscoveryProvider _setup]_block_invoke.96
+ ___367+[SMTriggerDestinationStateMO managedObjectWithSessionIdentifier:lastLockDate:lastUnlockDate:predominantModeOfTransport:currentStatus:currentStatusDate:date:shouldRetryETAQuery:numberOfETARetries:upperBoundEtaCrowFliesUpperBoundEta:upperBoundEtaMapsUpperBoundEta:roundTripReminderDate:timeToUpdateStatus:mapsExpectedTravelTime:remainingDistance:managedObjectContext:]_block_invoke
+ ___40-[SMInitiatorService _onDeletedMessage:]_block_invoke.167
+ ___41-[RTPeopleDiscoveryProvider _purgeEvents]_block_invoke
+ ___41-[RTPeopleDiscoveryProvider _purgeEvents]_block_invoke.117
+ ___42-[RTPeopleDiscoveryProvider removeClient:]_block_invoke
+ ___43-[RTDaemonClientInternal setXpcConnection:]_block_invoke.634
+ ___44-[RTDaemonClient fetchOngoingPeopleDensity:]_block_invoke
+ ___44-[RTDaemonClient fetchOngoingPeopleDensity:]_block_invoke_2
+ ___44-[RTXPCActivityManager _registerRegistrant:]_block_invoke.220
+ ___45-[RTLocationManager _storeLocations:handler:]_block_invoke.156
+ ___45-[RTPeopleDensityRecord _closeDensityBundle:]_block_invoke.40
+ ___45-[SMInitiatorService _onDeletedConversation:]_block_invoke.170
+ ___47-[RTClientListener _setupConnection:forClient:]_block_invoke.262
+ ___48-[RTAuthorizedLocationManager _isRoutineEnabled]_block_invoke
+ ___48-[RTDaemonClientInternal eraseVisitLogDatabase:]_block_invoke
+ ___48-[RTDaemonClientInternal eraseVisitLogDatabase:]_block_invoke_2
+ ___49-[SMInitiatorService _purgePredating:completion:]_block_invoke.135
+ ___49-[SMInitiatorService _purgePredating:completion:]_block_invoke.137
+ ___49-[SMInitiatorService _purgePredating:completion:]_block_invoke.139
+ ___49-[SMInitiatorService _purgePredating:completion:]_block_invoke_2.136
+ ___49-[SMInitiatorService _purgePredating:completion:]_block_invoke_2.138
+ ___49-[SMInitiatorService _startInitializationProcess]_block_invoke.151
+ ___49-[SMInitiatorService _startInitializationProcess]_block_invoke.160
+ ___49-[SMInitiatorService _startInitializationProcess]_block_invoke_2.163
+ ___50-[RTDaemonClient removeVisitWithIdentifier:reply:]_block_invoke.556
+ ___52-[RTAuthorizedLocationMetrics submitToCoreAnalytics]_block_invoke
+ ___52-[RTAuthorizedLocationMetrics submitToCoreAnalytics]_block_invoke_2
+ ___53-[RTAuthorizedLocationManager _setupVisitLogActivity]_block_invoke.32
+ ___53-[RTAuthorizedLocationManager eraseVisitLogDatabase:]_block_invoke
+ ___53-[RTDaemonClient fetchStoredVisitsWithOptions:reply:]_block_invoke.469
+ ___53-[RTDaemonClient fetchStoredVisitsWithOptions:reply:]_block_invoke.471
+ ___53-[RTDaemonClient fetchStoredVisitsWithOptions:reply:]_block_invoke.473
+ ___53-[RTDaemonClient fetchStoredVisitsWithOptions:reply:]_block_invoke_2.472
+ ___53-[RTVisitMonitor fetchVisitsFromDate:toDate:handler:]_block_invoke.132
+ ___54-[RTDaemonClient connection:handleInvocation:isReply:]_block_invoke.431
+ ___54-[SMDaemonClient connection:handleInvocation:isReply:]_block_invoke.49
+ ___55-[RTLocationManager _removeLocationsPredating:handler:]_block_invoke.211
+ ___57-[SMInitiatorService _setupOncePersistenceStackAvailable]_block_invoke.112
+ ___57-[SMInitiatorService _setupOncePersistenceStackAvailable]_block_invoke.114
+ ___58-[RTPeopleDiscoveryProvider fetchMostRecentPeopleDensity:]_block_invoke
+ ___58-[RTTrustedTimeCache convertMachContinuousTicksToSeconds:]_block_invoke
+ ___58-[SMSuggestionsManager _suppressSuggestion:context:error:]_block_invoke.192
+ ___58-[SMSuggestionsManager _suppressSuggestion:context:error:]_block_invoke.203
+ ___58-[SMSuggestionsManager _suppressSuggestion:context:error:]_block_invoke.204
+ ___59-[SMInitiatorService _initializeSessionWithHandle:handler:]_block_invoke.211
+ ___59-[SMSuggestionsManager _isFirstTimeUserOfZelkovaWithError:]_block_invoke.306
+ ___60-[RTPeopleDiscoveryProvider _aggregateAndApplyConfiguration]_block_invoke
+ ___60-[RTPeopleDiscoveryProvider _aggregateAndApplyConfiguration]_block_invoke.142
+ ___60-[RTPeopleDiscoveryProvider _aggregateAndApplyConfiguration]_block_invoke_2
+ ___60-[RTPeopleDiscoveryProvider _aggregateAndApplyConfiguration]_block_invoke_3
+ ___61-[RTLocationManager fetchCurrentLocationWithOptions:handler:]_block_invoke.169
+ ___61-[RTPeopleDiscoveryProvider _fetchAndReconcileAdvertisements]_block_invoke.125
+ ___61-[RTVisitMonitor _setupGeoFencesForVisit:pipelineType:error:]_block_invoke.156
+ ___61-[RTVisitMonitor _setupGeoFencesForVisit:pipelineType:error:]_block_invoke_2.157
+ ___62-[RTLocationManager _fetchStoredLocationsWithContext:handler:]_block_invoke.186
+ ___62-[SMTriggerDestination _updateInitiatorStatusDestinationBound]_block_invoke.208
+ ___63-[RTDaemonClientInternal fetchVisitLogsWithDateInterval:reply:]_block_invoke
+ ___63-[RTDaemonClientInternal fetchVisitLogsWithDateInterval:reply:]_block_invoke_2
+ ___64-[RTDaemonClient fetchPredictedLocationsOfInterestOnDate:reply:]_block_invoke.450
+ ___64-[RTDaemonClientInternal fetchAuthorizedLocationExtendedStatus:]_block_invoke
+ ___64-[RTDaemonClientInternal fetchAuthorizedLocationExtendedStatus:]_block_invoke_2
+ ___65-[RTAuthorizedLocationManager fetchVisitLogsWithOptions:handler:]_block_invoke
+ ___65-[RTLocationManager locationManager:didDetermineState:forRegion:]_block_invoke.234
+ ___65-[SMDaemonClient startMonitoringInitiatorSafetyCacheWithHandler:]_block_invoke.58
+ ___66-[SMInitiatorService _fetchSessionReceiptForSessionID:completion:]_block_invoke.239
+ ___67-[RTDaemonClient fetchPredictedExitDatesFromLocation:onDate:reply:]_block_invoke.518
+ ___67-[RTLocationManager _fetchEstimatedLocationAtDate:options:handler:]_block_invoke.197
+ ___67-[RTLocationManager locationManager:didUpdateLocations:completion:]_block_invoke.159
+ ___67-[RTLocationManager locationManager:didUpdateLocations:completion:]_block_invoke.164
+ ___67-[RTLocationManager locationManager:didUpdateLocations:completion:]_block_invoke_2.163
+ ___67-[SMInitiatorService _startFrequentSingleShotFetchAllZonesActivity]_block_invoke.190
+ ___67-[SMInitiatorService _startInfrequentPeriodicFetchAllZonesActivity]_block_invoke.198
+ ___67-[SMSuggestionsManager _fetchMostLikelyReceiverHandlesWithHandler:]_block_invoke.224
+ ___67-[SMSuggestionsManager _fetchMostLikelyReceiverHandlesWithHandler:]_block_invoke.225
+ ___68-[RTAuthorizedLocationVisitLogStore _fetchVisitLogWithUUID:handler:]_block_invoke.29
+ ___68-[RTAuthorizedLocationVisitLogStore wasTrustedTimeRecentlyAvailable]_block_invoke
+ ___68-[SMSuggestionsManager _getFAFamilyMembersFromAAAFamilyWithHandler:]_block_invoke
+ ___69-[RTAuthorizedLocationManager _curateAuthorizedLocationsWithHandler:]_block_invoke.85
+ ___69-[RTAuthorizedLocationManager _curateAuthorizedLocationsWithHandler:]_block_invoke.94
+ ___69-[RTAuthorizedLocationManager fetchAuthorizedLocationExtendedStatus:]_block_invoke
+ ___69-[RTAuthorizedLocationManager runEraseInstallDatabaseInitialization:]_block_invoke
+ ___70-[RTAuthorizedLocationManager _fetchAuthorizedLocationExtendedStatus:]_block_invoke
+ ___70-[RTAuthorizedLocationManager _runEraseInstallDatabaseInitialization:]_block_invoke
+ ___70-[RTAuthorizedLocationManager _runEraseInstallDatabaseInitialization:]_block_invoke.116
+ ___70-[RTAuthorizedLocationManager _runEraseInstallDatabaseInitialization:]_block_invoke.117
+ ___70-[RTDaemonClient vehicleEventRegistrar:didReceiveVehicleEvents:error:]_block_invoke.548
+ ___71-[SMSuggestionsManager _fetchMostLikelySessionDestinationsWithHandler:]_block_invoke.229
+ ___71-[SMSuggestionsManager _fetchMostLikelySessionDestinationsWithHandler:]_block_invoke.237
+ ___71-[SMSuggestionsManager _fetchMostLikelySessionDestinationsWithHandler:]_block_invoke.244
+ ___71-[SMSuggestionsManager _fetchMostLikelySessionDestinationsWithHandler:]_block_invoke.246
+ ___71-[SMSuggestionsManager _fetchSuggestedSessionConfigurationWithHandler:]_block_invoke.216
+ ___72-[RTAuthorizedLocationVisitLogStore _fetchVisitLogsWithOptions:handler:]_block_invoke.20
+ ___72-[RTDaemonClientInternal fetchFusionCandidatesForVisitIdentifier:reply:]_block_invoke.657
+ ___72-[RTPeopleDiscoveryProvider addClient:withIdentifier:withConfiguration:]_block_invoke
+ ___72-[RTPeopleDiscoveryProvider addClient:withIdentifier:withConfiguration:]_block_invoke.132
+ ___72-[SMSuggestionsManager _didInteractInPastWithHandle:timeInterval:error:]_block_invoke.279
+ ___72-[SMSuggestionsManager _showSuggestionsDetectionUIWithSuggestion:error:]_block_invoke.186
+ ___73-[RTPeopleDiscoveryProvider performPurgeOfType:referenceDate:completion:]_block_invoke
+ ___74-[SMInitiatorService _initializeAndStartSessionWithConfiguration:handler:]_block_invoke.219
+ ___74-[SMInitiatorService _initializeAndStartSessionWithConfiguration:handler:]_block_invoke.223
+ ___74-[SMInitiatorService _initializeAndStartSessionWithConfiguration:handler:]_block_invoke.224
+ ___74-[SMInitiatorService _initializeAndStartSessionWithConfiguration:handler:]_block_invoke.227
+ ___74-[SMInitiatorService _initializeAndStartSessionWithConfiguration:handler:]_block_invoke.229
+ ___75-[RTAuthorizedLocationVisitLogStore getEraseInstallRetroRegistrationStatus]_block_invoke
+ ___76-[RTDaemonClient scenarioTriggerRegistrar:didReceiveScenarioTriggers:error:]_block_invoke.513
+ ___76-[RTDaemonClient scenarioTriggerRegistrar:didReceiveScenarioTriggers:error:]_block_invoke.514
+ ___76-[RTDaemonClientInternal forceAuthorizedLocationEraseInstallInitialization:]_block_invoke
+ ___76-[RTDaemonClientInternal forceAuthorizedLocationEraseInstallInitialization:]_block_invoke_2
+ ___76-[RTDaemonClientRegistrarPeopleDiscovery onPeopleDensityUpdateNotification:]_block_invoke
+ ___77-[SMSuggestionsManager _getNPLOIsWithOnlyHighConfidence:location:date:error:]_block_invoke.372
+ ___79-[RTAuthorizedLocationManager _setupEraseInstallDatabaseInitializationActivity]_block_invoke
+ ___79-[RTAuthorizedLocationManager _setupEraseInstallDatabaseInitializationActivity]_block_invoke.64
+ ___79-[RTAuthorizedLocationManager _setupEraseInstallDatabaseInitializationActivity]_block_invoke.66
+ ___79-[RTAuthorizedLocationManager _setupEraseInstallDatabaseInitializationActivity]_block_invoke.68
+ ___79-[RTAuthorizedLocationManager _setupEraseInstallDatabaseInitializationActivity]_block_invoke_2
+ ___79-[RTDaemonClient addLocationOfInterestOfType:mapItemStorage:customLabel:reply:]_block_invoke.552
+ ___79-[RTDaemonClient peopleDiscoveryRegistrar:didReceivePeopleDensityUpdate:error:]_block_invoke
+ ___79-[RTDaemonClient peopleDiscoveryRegistrar:didReceivePeopleDensityUpdate:error:]_block_invoke.570
+ ___79-[RTDaemonClient peopleDiscoveryRegistrar:didReceivePeopleDensityUpdate:error:]_block_invoke_2
+ ___80-[RTDaemonClient fetchLocationsOfInterestVisitedBetweenStartDate:endDate:reply:]_block_invoke.502
+ ___82-[RTDaemonClient fetchPredictedLocationsOfInterestBetweenStartDate:endDate:reply:]_block_invoke.521
+ ___84-[SMSuggestionsMetricsManager _getNPLOIsWithOnlyHighConfidence:location:date:error:]_block_invoke.146
+ ___85-[RTAuthorizedLocationManager _computeLocationTechnologyAvailabilityForDateInterval:]_block_invoke
+ ___85-[SMSuggestionsMetricsManager _getSuggestionsCountSelectedForPastDate:endDate:error:]_block_invoke.129
+ ___94-[RTAuthorizedLocationManager _updateVisitLogWithTrustedTime:isRetroRegistrationTime:handler:]_block_invoke.78
+ ___94-[RTAuthorizedLocationManager _updateVisitLogWithTrustedTime:isRetroRegistrationTime:handler:]_block_invoke.80
+ ___94-[RTAuthorizedLocationManager _updateVisitLogWithTrustedTime:isRetroRegistrationTime:handler:]_block_invoke.81
+ ___97-[RTAuthorizedLocationManager _assertRecentLocationTechnologyQualityForAuthorizedLocation:visit:]_block_invoke.99
+ ___97-[RTDaemonClient fetchNextPredictedLocationsOfInterestFromLocation:startDate:timeInterval:reply:]_block_invoke.437
+ ___block_descriptor_155_e8_32s40s48s56s64s72s80s88s96s104s112r_e5_v8?0lr112l8s32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8s96l8s104l8
+ ___block_descriptor_48_e8_32s40bs_e36_v24?0"FAFamilyCircle"8"NSError"16ls40l8s32l8
+ ___block_descriptor_48_e8_32s40r_e8_v12?0B8lr40l8s32l8
+ ___block_descriptor_49_e8_32s_e5_v8?0ls32l8
+ ___block_descriptor_56_e8_32s40bs_e37_v24?0"RTPeopleDensity"8"NSError"16ls32l8s40l8
+ ___block_descriptor_56_e8_32s40bs_e51_v32?0"RTAuthorizedLocationStatus"8q16"NSError"24ls32l8s40l8
+ ___block_descriptor_56_e8_32s40r_e20_v20?0B8"NSError"12ls32l8r40l8
+ ___block_descriptor_64_e8_32s40s48bs_e51_v32?0"RTAuthorizedLocationStatus"8q16"NSError"24ls32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48r_e17_v16?0"NSError"8lr48l8s32l8s40l8
+ ___block_descriptor_72_e8_32s40s48r56r64r_e33_v32?0"RTMotionActivity"8Q16^B24ls32l8r48l8r56l8r64l8s40l8
+ ___block_descriptor_80_e8_32s40s48s56bs_e5_v8?0ls32l8s40l8s56l8s48l8
+ ___block_descriptor_88_e8_32s40s48s56s64r72r_e29_v24?0"NSArray"8"NSError"16lr64l8s32l8r72l8s40l8s48l8s56l8
+ ___block_literal_global.116
+ ___block_literal_global.119
+ ___block_literal_global.134
+ ___block_literal_global.145
+ ___block_literal_global.153
+ ___block_literal_global.155
+ ___block_literal_global.157
+ ___block_literal_global.162
+ ___block_literal_global.165
+ ___block_literal_global.169
+ ___block_literal_global.172
+ ___block_literal_global.226
+ ___block_literal_global.227
+ ___block_literal_global.371
+ ___block_literal_global.374
+ ___block_literal_global.437
+ ___block_literal_global.452
+ ___block_literal_global.520
+ ___block_literal_global.523
+ ___block_literal_global.528
+ ___block_literal_global.531
+ ___block_literal_global.537
+ ___block_literal_global.565
+ ___block_literal_global.617
+ ___block_literal_global.704
+ __unnamed_array_storage.102
+ __unnamed_array_storage.127
+ __unnamed_array_storage.140
+ __unnamed_array_storage.143
+ __unnamed_array_storage.201
+ __unnamed_array_storage.235
+ __unnamed_array_storage.240
+ _kSMSuggestionFirstTimeUserSuppressionEndTime
+ _kSMSuggestionFirstTimeUserSuppressionSessionConfigurationCount
+ _kSMSuggestionFirstTimeUserSuppressionStartTime
+ _objc_msgSend$_addClientConfiguration:withIdentifier:
+ _objc_msgSend$_aggregateAndApplyConfiguration
+ _objc_msgSend$_checkConfiguration
+ _objc_msgSend$_computeDensityScore:scanDuration:forRecords:
+ _objc_msgSend$_computeLocationTechnologyAvailabilityForDateInterval:
+ _objc_msgSend$_computeLocationTechnologyExpectationFromHistoricalAvailability:
+ _objc_msgSend$_computeMeanOfRssi:
+ _objc_msgSend$_convertObservationIntervalToDouble:
+ _objc_msgSend$_evaluateStatusUsingCurrentLocation:
+ _objc_msgSend$_fetchAuthorizedLocationExtendedStatus:
+ _objc_msgSend$_fetchAuthorizedLocationExtendedStatusWithMetrics:
+ _objc_msgSend$_getFAFamilyMembersFromAAAFamilyWithHandler:
+ _objc_msgSend$_getSMHandlesFromFAFamilyMembers:error:
+ _objc_msgSend$_getTimeSinceLastSuccessfulBiometricAuthentication:
+ _objc_msgSend$_isExpeditedSyncAndLearnRequired
+ _objc_msgSend$_isRoutineEnabled
+ _objc_msgSend$_loadEraseInstallInitializationXPCCriteriaFromDefaults
+ _objc_msgSend$_locationAvailabilityFromCLLocation:
+ _objc_msgSend$_logClientConfigurations
+ _objc_msgSend$_onPeopleDensityUpdateNotification:
+ _objc_msgSend$_purgeEvents
+ _objc_msgSend$_registerForDeviceUnlockNotification
+ _objc_msgSend$_removeClientConfiguration:
+ _objc_msgSend$_runEraseInstallDatabaseInitialization:
+ _objc_msgSend$_scanLevelFromServiceLevel:observationInterval:
+ _objc_msgSend$_setupEraseInstallDatabaseInitializationActivity
+ _objc_msgSend$_updateMostRecentDateAtWhichDeviceDataIsTrusted
+ _objc_msgSend$_updateVisitLogDistantFutureFlagWithStatus:TrustedTimeAvailability:isRetroRegistration:
+ _objc_msgSend$addClient:withIdentifier:withConfiguration:
+ _objc_msgSend$addPendingPeopleDensityUpdateBlock:failBlock:description:
+ _objc_msgSend$addRecord:
+ _objc_msgSend$availableDevices
+ _objc_msgSend$biometricsManager
+ _objc_msgSend$computeRssiHistogramForAdvs:
+ _objc_msgSend$configure:withCompletionHandler:
+ _objc_msgSend$convertMachContinuousTicksToSeconds:
+ _objc_msgSend$curationMetrics
+ _objc_msgSend$currentConfidenceThreshold
+ _objc_msgSend$currentStatusDate
+ _objc_msgSend$daemonResponseLatencyMs
+ _objc_msgSend$decodeTimeSourceWithValue:isRetroRegistration:isTrusted:
+ _objc_msgSend$defaultOverrideTimeSinceLastSuccessfulBiometricAuthentication:
+ _objc_msgSend$densityBundles
+ _objc_msgSend$densityCallbackConfiguration
+ _objc_msgSend$deviceWithDescriptor:error:
+ _objc_msgSend$encodeTimeSourceWithValue:isTrusted:isRetroRegistration:
+ _objc_msgSend$eraseInstallInitializationAttemptCount
+ _objc_msgSend$eraseInstallInitializationCompletionTimeHours
+ _objc_msgSend$eraseVisitLogDatabase:
+ _objc_msgSend$fetchAuthorizedLocationExtendedStatus:
+ _objc_msgSend$fetchCurrentObservationBundle
+ _objc_msgSend$fetchMostRecentPeopleDensity:
+ _objc_msgSend$fractionOfVisitsToTopLOIWithGPS
+ _objc_msgSend$fractionOfVisitsToTopLOIWithWiFiHI
+ _objc_msgSend$getEraseInstallRetroRegistrationStatus
+ _objc_msgSend$getHistogram
+ _objc_msgSend$historicalRejectionReasonCode
+ _objc_msgSend$historicalRejectionSpeedMps
+ _objc_msgSend$idleMaxDistanceThreshold
+ _objc_msgSend$idleTimeoutThreshold
+ _objc_msgSend$initWithDaemonStartDate:
+ _objc_msgSend$initWithLoi:dwellTime:numberOfDaysVisited:ageDaysFirstVisit:ageDaysFirstRegisteredVisit:locationTechnologyAvailability:visitsWithTechnologyAnnotation:visitsWithGPS:visitsWithWiFiHI:
+ _objc_msgSend$initWithPeopleDensityBundles:
+ _objc_msgSend$initWithPeopleDiscoveryProvider:queue:
+ _objc_msgSend$initWithServiceLevel:storageDuration:observationInterval:densityCallbackConfiguration:
+ _objc_msgSend$initWithSessionIdentifier:currentStatus:currentStatusDate:lastLockDate:lastUnlockDate:predominantModeOfTransport:numberOfETARetries:shouldRetryETAQuery:roundTripReminderDate:timeToUpdateStatus:upperBoundEta:mapsExpectedTravelTime:remainingDistance:date:
+ _objc_msgSend$initWithTrustedTimeCache:defaultsManager:
+ _objc_msgSend$initWithVisitIdentifier:registrationDate:locationTechnologyAvailability:
+ _objc_msgSend$initWithVisitManager:locationManager:distanceCalculator:learnedLocationManager:motionActivityManager:visitLogStore:defaultsManager:xpcActivityManager:dataProtectionManager:persistenceMirroringManager:platform:authorizationManager:
+ _objc_msgSend$initializationMetrics
+ _objc_msgSend$isHistoricallyALowDiversityLocation
+ _objc_msgSend$lastMatchEventWithError:
+ _objc_msgSend$locationAgeMinutes
+ _objc_msgSend$locationTechnologyAvailability
+ _objc_msgSend$loiFamiliarityRank
+ _objc_msgSend$managedObjectWithSessionIdentifier:lastLockDate:lastUnlockDate:predominantModeOfTransport:currentStatus:currentStatusDate:date:shouldRetryETAQuery:numberOfETARetries:upperBoundEtaCrowFliesUpperBoundEta:upperBoundEtaMapsUpperBoundEta:roundTripReminderDate:timeToUpdateStatus:mapsExpectedTravelTime:remainingDistance:managedObjectContext:
+ _objc_msgSend$memberType
+ _objc_msgSend$members
+ _objc_msgSend$normalizedDistanceToCentroid
+ _objc_msgSend$numFamiliarLois
+ _objc_msgSend$numberOfALOIsGeneratedDuringEraseInstallInitialization
+ _objc_msgSend$numberOfVisitsRegisteredDuringEraseInstallInitialization
+ _objc_msgSend$observationInterval
+ _objc_msgSend$onBufferedDevicesReceivedNotification
+ _objc_msgSend$onCoreLocationProviderCameUpNotification
+ _objc_msgSend$onDensityUpdate:error:
+ _objc_msgSend$originLocation
+ _objc_msgSend$peopleDiscoveryRegistrar
+ _objc_msgSend$peopleDiscoveryRegistrar:didReceivePeopleDensityUpdate:error:
+ _objc_msgSend$purgeVisitLogsOnDateInterval:handler:
+ _objc_msgSend$queryMetrics
+ _objc_msgSend$rejectionReasonCode
+ _objc_msgSend$removeClient:
+ _objc_msgSend$responseValue
+ _objc_msgSend$runEraseInstallDatabaseInitialization:
+ _objc_msgSend$runningRecords
+ _objc_msgSend$serviceLevel
+ _objc_msgSend$setClientConfigurations:
+ _objc_msgSend$setCurrentConfidenceThreshold:
+ _objc_msgSend$setCurrentObservationIntervalSeconds:
+ _objc_msgSend$setCurrentStatusDate:
+ _objc_msgSend$setEraseInstallInitializationAttemptCount:
+ _objc_msgSend$setEraseInstallInitializationCompletionTimeHours:
+ _objc_msgSend$setEraseInstallRetroRegistrationStatus:
+ _objc_msgSend$setFractionOfVisitsToTopLOIWithGPS:
+ _objc_msgSend$setFractionOfVisitsToTopLOIWithWiFiHI:
+ _objc_msgSend$setIdleMaxDistanceThreshold:
+ _objc_msgSend$setIdleTimeoutThreshold:
+ _objc_msgSend$setInitializationMetrics:
+ _objc_msgSend$setIsHistoricallyALowDiversityLocation:
+ _objc_msgSend$setLocationServicesEnabled:
+ _objc_msgSend$setLocationTechnologyAvailability:
+ _objc_msgSend$setMomentsConfiguration:
+ _objc_msgSend$setNumberOfALOIsGeneratedDuringEraseInstallInitialization:
+ _objc_msgSend$setNumberOfVisitsRegisteredDuringEraseInstallInitialization:
+ _objc_msgSend$setOriginLocation:
+ _objc_msgSend$setQueryMetrics:
+ _objc_msgSend$setRank:
+ _objc_msgSend$setStartDatetime:
+ _objc_msgSend$setTrustedTimeRecentAvailability:
+ _objc_msgSend$setVisitsToTopLOIWithTechAvailabilityKnown:
+ _objc_msgSend$startDatetime
+ _objc_msgSend$startMonitoringForPeopleDiscovery:configuration:reply:
+ _objc_msgSend$startMonitoringForPeopleDiscoveryWithIdentifier:configuration:
+ _objc_msgSend$startRequestWithCompletionHandler:
+ _objc_msgSend$stopMonitoringForPeopleDiscovery
+ _objc_msgSend$stopMonitoringForPeopleDiscoveryWithReply:
+ _objc_msgSend$storageDuration
+ _objc_msgSend$technologyAvailability
+ _objc_msgSend$timeSinceDaemonStart
+ _objc_msgSend$timeSinceLastQueryMetricsSubmission
+ _objc_msgSend$timeStamp
+ _objc_msgSend$trimRunningRecordsBeforeRef:
+ _objc_msgSend$updateDateOfLastSuccessfulBiometricAuthentication
+ _objc_msgSend$updateHistogramWithAdvs:
+ _objc_msgSend$userTimeOffsetHours
+ _objc_msgSend$visitDwellMinutes
+ _objc_msgSend$visitsToTopLOIWithTechAvailabilityKnown
+ _objc_msgSend$visitsWithGPS
+ _objc_msgSend$visitsWithTechnologyAnnotation
+ _objc_msgSend$visitsWithWiFiHI
+ _objc_msgSend$wasTrustedTimeRecentlyAvailable
- +[SMTriggerDestinationStateMO managedObjectWithSessionIdentifier:lastLockDate:lastUnlockDate:predominantModeOfTransport:currentStatus:date:shouldRetryETAQuery:numberOfETARetries:upperBoundEtaCrowFliesUpperBoundEta:upperBoundEtaMapsUpperBoundEta:roundTripReminderDate:timeToUpdateStatus:mapsExpectedTravelTime:remainingDistance:managedObjectContext:]
- -[RTAddressMO debugDescription]
- -[RTAuthorizedLocation initWithLoi:dwellTime:numberOfDaysVisited:ageDaysFirstVisit:ageDaysFirstRegisteredVisit:]
- -[RTAuthorizedLocationManager _checkDefaults]
- -[RTAuthorizedLocationManager _decodeTimeSourceWithValue:isRetroRegistration:isTrusted:]
- -[RTAuthorizedLocationManager _encodeTimeSourceWithValue:isTrusted:isRetroRegistration:]
- -[RTAuthorizedLocationManager _fetchAuthorizedLocationStatus:]
- -[RTAuthorizedLocationManager _setupScheduledOneTimeRegistrationTask]
- -[RTAuthorizedLocationManager curationMetrics]
- -[RTAuthorizedLocationManager fetchAuthorizedLocationStatus:]
- -[RTAuthorizedLocationManager ignoreVisitRegistrationDate]
- -[RTAuthorizedLocationManager initWithVisitManager:locationManager:distanceCalculator:learnedLocationManager:motionActivityManager:visitLogStore:defaultsManager:xpcActivityManager:dataProtectionManager:]
- -[RTAuthorizedLocationManager isFirstRunSinceSwUpgrade]
- -[RTAuthorizedLocationManager lastMetricSubmissionDate]
- -[RTAuthorizedLocationManager queryMetrics]
- -[RTAuthorizedLocationManager retroRegistrationAttemptCount]
- -[RTAuthorizedLocationManager setCurationMetrics:]
- -[RTAuthorizedLocationManager setIgnoreVisitRegistrationDate:]
- -[RTAuthorizedLocationManager setIsFirstRunSinceSwUpgrade:]
- -[RTAuthorizedLocationManager setLastMetricSubmissionDate:]
- -[RTAuthorizedLocationManager setQueryMetrics:]
- -[RTAuthorizedLocationManager setRetroRegistrationAttemptCount:]
- -[RTAuthorizedLocationQueryMetrics convertToDictionary]
- -[RTAuthorizedLocationQueryMetrics curationMetrics]
- -[RTAuthorizedLocationQueryMetrics setCurationMetrics:]
- -[RTAuthorizedLocationQueryMetrics submitToCoreAnalytics]
- -[RTAuthorizedLocationVisitLog initWithVisitIdentifier:registrationDate:]
- -[RTMapItemMO debugDescription]
- -[RTPeopleDensityRecord _computeDensityScore:scanDuration:]
- -[RTPeopleDiscoveryProvider momentsEnabled]
- -[RTPeopleDiscoveryProvider onPeopleSwitchUpdated:]
- -[RTPeopleDiscoveryProvider safetyAlertEnabled]
- -[RTPeopleDiscoveryProvider setMomentsEnabled:]
- -[RTPeopleDiscoveryProvider setSafetyAlertEnabled:]
- -[RTVisitMO debugDescription]
- GCC_except_table112
- GCC_except_table116
- GCC_except_table143
- GCC_except_table79
- _OBJC_IVAR_$_RTAuthorizedLocationQueryMetrics._curationMetrics
- _OBJC_IVAR_$_RTPeopleDiscoveryProvider._momentsEnabled
- _OBJC_IVAR_$_RTPeopleDiscoveryProvider._safetyAlertEnabled
- ___117-[RTAuthorizedLocationManager _assertRecentMotionActivityAndLocationHistoryAreConsistentForAuthorizedLocation:visit:]_block_invoke.308
- ___25-[RTDaemonClient restore]_block_invoke.516
- ___349+[SMTriggerDestinationStateMO managedObjectWithSessionIdentifier:lastLockDate:lastUnlockDate:predominantModeOfTransport:currentStatus:date:shouldRetryETAQuery:numberOfETARetries:upperBoundEtaCrowFliesUpperBoundEta:upperBoundEtaMapsUpperBoundEta:roundTripReminderDate:timeToUpdateStatus:mapsExpectedTravelTime:remainingDistance:managedObjectContext:]_block_invoke
- ___35-[RTPeopleDiscoveryProvider _setup]_block_invoke.68
- ___35-[RTPeopleDiscoveryProvider _setup]_block_invoke.76
- ___40-[SMInitiatorService _onDeletedMessage:]_block_invoke.149
- ___43-[RTDaemonClientInternal setXpcConnection:]_block_invoke.628
- ___43-[RTPeopleDiscoveryProvider _monitorEvents]_block_invoke
- ___43-[RTPeopleDiscoveryProvider _monitorEvents]_block_invoke.84
- ___44-[RTXPCActivityManager _registerRegistrant:]_block_invoke.218
- ___45-[RTLocationManager _storeLocations:handler:]_block_invoke.153
- ___45-[RTPeopleDensityRecord _closeDensityBundle:]_block_invoke.39
- ___45-[SMInitiatorService _onDeletedConversation:]_block_invoke.152
- ___47-[RTClientListener _setupConnection:forClient:]_block_invoke.256
- ___47-[RTTrustedTimeCache machContinuousTimeSeconds]_block_invoke
- ___49-[SMInitiatorService _purgePredating:completion:]_block_invoke.117
- ___49-[SMInitiatorService _purgePredating:completion:]_block_invoke.119
- ___49-[SMInitiatorService _purgePredating:completion:]_block_invoke.121
- ___49-[SMInitiatorService _purgePredating:completion:]_block_invoke_2.118
- ___49-[SMInitiatorService _purgePredating:completion:]_block_invoke_2.120
- ___49-[SMInitiatorService _startInitializationProcess]_block_invoke.133
- ___49-[SMInitiatorService _startInitializationProcess]_block_invoke.142
- ___49-[SMInitiatorService _startInitializationProcess]_block_invoke_2.145
- ___50-[RTDaemonClient removeVisitWithIdentifier:reply:]_block_invoke.537
- ___51-[RTPeopleDiscoveryProvider onPeopleSwitchUpdated:]_block_invoke
- ___51-[RTPeopleDiscoveryProvider onPeopleSwitchUpdated:]_block_invoke.94
- ___51-[RTPeopleDiscoveryProvider onPeopleSwitchUpdated:]_block_invoke_2
- ___51-[RTPeopleDiscoveryProvider onPeopleSwitchUpdated:]_block_invoke_2.95
- ___53-[RTAuthorizedLocationManager _setupVisitLogActivity]_block_invoke.279
- ___53-[RTDaemonClient fetchStoredVisitsWithOptions:reply:]_block_invoke.459
- ___53-[RTDaemonClient fetchStoredVisitsWithOptions:reply:]_block_invoke.461
- ___53-[RTDaemonClient fetchStoredVisitsWithOptions:reply:]_block_invoke.463
- ___53-[RTDaemonClient fetchStoredVisitsWithOptions:reply:]_block_invoke_2.462
- ___53-[RTVisitMonitor fetchVisitsFromDate:toDate:handler:]_block_invoke.135
- ___54-[RTDaemonClient connection:handleInvocation:isReply:]_block_invoke.421
- ___54-[SMDaemonClient connection:handleInvocation:isReply:]_block_invoke.31
- ___55-[RTLocationManager _removeLocationsPredating:handler:]_block_invoke.208
- ___57-[RTAuthorizedLocationQueryMetrics submitToCoreAnalytics]_block_invoke
- ___57-[RTAuthorizedLocationQueryMetrics submitToCoreAnalytics]_block_invoke_2
- ___57-[SMInitiatorService _setupOncePersistenceStackAvailable]_block_invoke.94
- ___57-[SMInitiatorService _setupOncePersistenceStackAvailable]_block_invoke.96
- ___58-[SMSuggestionsManager _suppressSuggestion:context:error:]_block_invoke.188
- ___58-[SMSuggestionsManager _suppressSuggestion:context:error:]_block_invoke.195
- ___58-[SMSuggestionsManager _suppressSuggestion:context:error:]_block_invoke.200
- ___59-[SMInitiatorService _initializeSessionWithHandle:handler:]_block_invoke.193
- ___59-[SMSuggestionsManager _isFirstTimeUserOfZelkovaWithError:]_block_invoke.296
- ___61-[RTAuthorizedLocationManager fetchAuthorizedLocationStatus:]_block_invoke
- ___61-[RTLocationManager fetchCurrentLocationWithOptions:handler:]_block_invoke.166
- ___61-[RTPeopleDiscoveryProvider _fetchAndReconcileAdvertisements]_block_invoke.100
- ___61-[RTVisitMonitor _setupGeoFencesForVisit:pipelineType:error:]_block_invoke.159
- ___61-[RTVisitMonitor _setupGeoFencesForVisit:pipelineType:error:]_block_invoke_2.160
- ___62-[RTAuthorizedLocationManager _fetchAuthorizedLocationStatus:]_block_invoke
- ___62-[RTLocationManager _fetchStoredLocationsWithContext:handler:]_block_invoke.183
- ___62-[SMTriggerDestination _updateInitiatorStatusDestinationBound]_block_invoke.198
- ___64-[RTDaemonClient fetchPredictedLocationsOfInterestOnDate:reply:]_block_invoke.440
- ___65-[RTLocationManager locationManager:didDetermineState:forRegion:]_block_invoke.231
- ___65-[SMDaemonClient startMonitoringInitiatorSafetyCacheWithHandler:]_block_invoke.40
- ___66-[SMInitiatorService _fetchSessionReceiptForSessionID:completion:]_block_invoke.221
- ___67-[RTDaemonClient fetchPredictedExitDatesFromLocation:onDate:reply:]_block_invoke.508
- ___67-[RTLocationManager _fetchEstimatedLocationAtDate:options:handler:]_block_invoke.194
- ___67-[RTLocationManager locationManager:didUpdateLocations:completion:]_block_invoke.156
- ___67-[RTLocationManager locationManager:didUpdateLocations:completion:]_block_invoke.161
- ___67-[RTLocationManager locationManager:didUpdateLocations:completion:]_block_invoke_2.160
- ___67-[SMInitiatorService _startFrequentSingleShotFetchAllZonesActivity]_block_invoke.172
- ___67-[SMInitiatorService _startInfrequentPeriodicFetchAllZonesActivity]_block_invoke.180
- ___67-[SMSuggestionsManager _fetchMostLikelyReceiverHandlesWithHandler:]_block_invoke.215
- ___68-[RTAuthorizedLocationVisitLogStore _fetchVisitLogWithUUID:handler:]_block_invoke.23
- ___69-[RTAuthorizedLocationManager _curateAuthorizedLocationsWithHandler:]_block_invoke.296
- ___69-[RTAuthorizedLocationManager _curateAuthorizedLocationsWithHandler:]_block_invoke.305
- ___70-[RTDaemonClient vehicleEventRegistrar:didReceiveVehicleEvents:error:]_block_invoke.529
- ___71-[SMSuggestionsManager _fetchMostLikelySessionDestinationsWithHandler:]_block_invoke.219
- ___71-[SMSuggestionsManager _fetchMostLikelySessionDestinationsWithHandler:]_block_invoke.227
- ___71-[SMSuggestionsManager _fetchMostLikelySessionDestinationsWithHandler:]_block_invoke.234
- ___71-[SMSuggestionsManager _fetchMostLikelySessionDestinationsWithHandler:]_block_invoke.236
- ___71-[SMSuggestionsManager _fetchSuggestedSessionConfigurationWithHandler:]_block_invoke.212
- ___72-[RTAuthorizedLocationVisitLogStore _fetchVisitLogsWithOptions:handler:]_block_invoke.14
- ___72-[RTDaemonClientInternal fetchFusionCandidatesForVisitIdentifier:reply:]_block_invoke.651
- ___72-[SMSuggestionsManager _didInteractInPastWithHandle:timeInterval:error:]_block_invoke.269
- ___72-[SMSuggestionsManager _showSuggestionsDetectionUIWithSuggestion:error:]_block_invoke.182
- ___74-[SMInitiatorService _initializeAndStartSessionWithConfiguration:handler:]_block_invoke.201
- ___74-[SMInitiatorService _initializeAndStartSessionWithConfiguration:handler:]_block_invoke.205
- ___74-[SMInitiatorService _initializeAndStartSessionWithConfiguration:handler:]_block_invoke.206
- ___74-[SMInitiatorService _initializeAndStartSessionWithConfiguration:handler:]_block_invoke.209
- ___74-[SMInitiatorService _initializeAndStartSessionWithConfiguration:handler:]_block_invoke.211
- ___76-[RTDaemonClient scenarioTriggerRegistrar:didReceiveScenarioTriggers:error:]_block_invoke.503
- ___76-[RTDaemonClient scenarioTriggerRegistrar:didReceiveScenarioTriggers:error:]_block_invoke.504
- ___77-[SMSuggestionsManager _getNPLOIsWithOnlyHighConfidence:location:date:error:]_block_invoke.362
- ___79-[RTDaemonClient addLocationOfInterestOfType:mapItemStorage:customLabel:reply:]_block_invoke.533
- ___80-[RTDaemonClient fetchLocationsOfInterestVisitedBetweenStartDate:endDate:reply:]_block_invoke.492
- ___82-[RTDaemonClient fetchPredictedLocationsOfInterestBetweenStartDate:endDate:reply:]_block_invoke.511
- ___84-[SMSuggestionsMetricsManager _getNPLOIsWithOnlyHighConfidence:location:date:error:]_block_invoke.128
- ___85-[SMSuggestionsMetricsManager _getSuggestionsCountSelectedForPastDate:endDate:error:]_block_invoke.111
- ___94-[RTAuthorizedLocationManager _updateVisitLogWithTrustedTime:isRetroRegistrationTime:handler:]_block_invoke.291
- ___94-[RTAuthorizedLocationManager _updateVisitLogWithTrustedTime:isRetroRegistrationTime:handler:]_block_invoke.293
- ___94-[RTAuthorizedLocationManager _updateVisitLogWithTrustedTime:isRetroRegistrationTime:handler:]_block_invoke.294
- ___97-[RTAuthorizedLocationManager _assertRecentLocationTechnologyQualityForAuthorizedLocation:visit:]_block_invoke.309
- ___97-[RTDaemonClient fetchNextPredictedLocationsOfInterestFromLocation:startDate:timeInterval:reply:]_block_invoke.427
- ___SafetyAlertsLibraryCore_block_invoke
- ___block_descriptor_147_e8_32s40s48s56s64s72s80s88s96s104r_e5_v8?0lr104l8s32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8s96l8
- ___block_descriptor_64_e8_32s40s48bs_e48_v24?0"RTAuthorizedLocationStatus"8"NSError"16ls32l8s40l8s48l8
- ___block_descriptor_64_e8_32s40s48r56r_e33_v32?0"RTMotionActivity"8Q16^B24ls32l8r48l8r56l8s40l8
- ___block_literal_global.140
- ___block_literal_global.141
- ___block_literal_global.147
- ___block_literal_global.151
- ___block_literal_global.154
- ___block_literal_global.209
- ___block_literal_global.356
- ___block_literal_global.361
- ___block_literal_global.364
- ___block_literal_global.367
- ___block_literal_global.440
- ___block_literal_global.442
- ___block_literal_global.510
- ___block_literal_global.513
- ___block_literal_global.518
- ___block_literal_global.539
- ___block_literal_global.614
- ___block_literal_global.692
- ___block_literal_global.83
- ___block_literal_global.86
- ___block_literal_global.98
- ___getSafetyAlertsClass_block_invoke
- __unnamed_array_storage.109
- __unnamed_array_storage.122
- __unnamed_array_storage.125
- __unnamed_array_storage.197
- __unnamed_array_storage.225
- __unnamed_array_storage.230
- __unnamed_array_storage.74
- _audit_stringSafetyAlerts
- _getMOSettingsManagerClass
- _kSMSuggestionEducationalSuggestionTimeIntervalSinceSunset
- _objc_msgSend$_checkDefaults
- _objc_msgSend$_computeDensityScore:scanDuration:
- _objc_msgSend$_decodeTimeSourceWithValue:isRetroRegistration:isTrusted:
- _objc_msgSend$_encodeTimeSourceWithValue:isTrusted:isRetroRegistration:
- _objc_msgSend$_fetchAuthorizedLocationStatus:
- _objc_msgSend$_setupScheduledOneTimeRegistrationTask
- _objc_msgSend$body
- _objc_msgSend$debugDescription
- _objc_msgSend$fetchAuthorizedLocationStatus:
- _objc_msgSend$getStateForSetting:
- _objc_msgSend$initWithLoi:dwellTime:numberOfDaysVisited:ageDaysFirstVisit:ageDaysFirstRegisteredVisit:
- _objc_msgSend$initWithSessionIdentifier:currentStatus:lastLockDate:lastUnlockDate:predominantModeOfTransport:numberOfETARetries:shouldRetryETAQuery:roundTripReminderDate:timeToUpdateStatus:upperBoundEta:mapsExpectedTravelTime:remainingDistance:date:
- _objc_msgSend$initWithVisitIdentifier:registrationDate:
- _objc_msgSend$initWithVisitManager:locationManager:distanceCalculator:learnedLocationManager:motionActivityManager:visitLogStore:defaultsManager:xpcActivityManager:dataProtectionManager:
- _objc_msgSend$isSaewEnabledSync:
- _objc_msgSend$managedObjectWithSessionIdentifier:lastLockDate:lastUnlockDate:predominantModeOfTransport:currentStatus:date:shouldRetryETAQuery:numberOfETARetries:upperBoundEtaCrowFliesUpperBoundEta:upperBoundEtaMapsUpperBoundEta:roundTripReminderDate:timeToUpdateStatus:mapsExpectedTravelTime:remainingDistance:managedObjectContext:
- _objc_msgSend$momentsEnabled
- _objc_msgSend$onPeopleSwitchUpdated:
- _objc_msgSend$safetyAlertEnabled
- _objc_msgSend$setMomentsEnabled:
- _objc_msgSend$setSafetyAlertEnabled:
- _objc_msgSend$sharedInterface
CStrings:
+ "\x02\x13"
+ "\x15#"
+ "\x1d\x12!"
+ "\x1f\x01%"
+ " <%@>: %@\n"
+ "\"\x1f\x0f\f"
+ "#RTDaemonClientRegistrarPeopleDiscovery, received people density events update, count %lu"
+ "#RTPeopleDensityRecord _addressToRssiValues has nil entry at address %@"
+ "#RTPeopleDensityRecord fetchCurrentHighConfidenceBundle runningRecordsStartdatetime:%@, theoreticalObsSpanSeconds: %f, totalScanDuration: %f, currentConfidenceThreshold: %f"
+ "#RTPeopleDensityRecord trimRunningRecords count:%lu, startDatetime: %@, currentObservationInterval(s): %f"
+ "#RTPeopleDensityRecord trimRunningRecords old bundle: %@"
+ "#RTPeopleDiscoveryProvider _addClientConfiguration configuration %@ identifier %@"
+ "#RTPeopleDiscoveryProvider _removeClientConfiguration identifier %@"
+ "#RTPeopleDiscoveryProvider disabled on platforms other than iPhone"
+ "#RTPeopleDiscoveryProvider fail to retrieve initial data upon registration, error %@"
+ "#RTPeopleDiscoveryProvider is already down"
+ "#RTPeopleDiscoveryProvider is already up"
+ "#RTPeopleDiscoveryProvider r120850419 Advertising state changed to: %@"
+ "#RTPeopleDiscoveryProvider r120850419 Associated Clients: {\n"
+ "#RTPeopleDiscoveryProvider r120850419 CL Scan Level: Default"
+ "#RTPeopleDiscoveryProvider r120850419 CL Scan Level: Low"
+ "#RTPeopleDiscoveryProvider r120850419 Scanning state changed to: %@"
+ "#RTPeopleDiscoveryProvider sending initial data to client %@"
+ "#RTPeopleDiscoveryProvider short term record file does not exist"
+ "%@ %@, cannot update VisitLogDistantFutureFlag to RTEraseInstallRetroRegistrationStatusHasNotRun"
+ "%@, %@, Adult iCloud family members count, %lu"
+ "%@, %@, Sema error during iCloud family query, %@"
+ "%@, %@, bypassing preprocessor, disable: defaults delete com.apple.routined %@"
+ "%@, %@, bypassing preprocessor, effectiveLocationBundlePath, %@"
+ "%@, %@, date check failed, current date, %@, suggestion skipped because time of day is between %f AM to %f PM"
+ "%@, %@, durationOfPreviousVisit, %.2f, intervalSincePreviousVisit, %.2f, distanceFromPreviousVisit, %.2f, visits to same LOI, %@"
+ "%@, %@, failed to sanitize handle, %@"
+ "%@, %@, handle, %@, chat identifier, %@, timeIntervalSinceMessage, %f, didInteract, %@"
+ "%@, %@, handle, %@, no message date for message, %@"
+ "%@, %@, iCloud family handles count, %lu"
+ "%@, %@, iCloud family query errored, %@"
+ "%@, %@, invalid contact information, %@, handles, %@"
+ "%@, %@, services, %@, chat identifiers, %@"
+ "%@, reply to client, %@, fetchMostRecentPeopleDensity, %@, error, %@"
+ "%@:%@ BKDevice, %@, "
+ "%@:%@ BKDevice, BKDeviceDescriptor, %@, "
+ "%@:%@ BKDevice, BKDeviceDescriptor, unable to fetch trustedNow, not updating dateOfMostRecentBiometricAuthentication."
+ "%@:%@ BKDevice, BKMatchEvent, nil, error, %@, returning timeSinceLastSuccessfulBiometricAuthentication, %{public}.1f"
+ "%@:%@ BKDevice, BKMatchEvent, result %{public}d, timestamp, %{public}.1f, timeSinceLastSuccessfulBiometricAuthentication, %{public}.1f"
+ "%@:%@ BKDevice, failed to get device, error, %@, returning timeSinceLastSuccessfulBiometricAuthentication, %{public}.1f"
+ "%@:%@ Returning %zu available authorized locations."
+ "%@:%@ Setting learning data age threshold to %{public}@"
+ "%@:%@ Using defaults override for timeSinceLastSuccessfulBiometricAuthentication_s, %.3f"
+ "%@:%@ attempt count %{public}d exceeded max retry count %{public}d, disabling erase install initialization."
+ "%@:%@ changing allowUnsecureTimeFallback flag to %{public}s"
+ "%@:%@ completed successfully, disabling erase install initialization."
+ "%@:%@ feature not enabled or device not supported."
+ "%@:%@ passed 11 (%{public}08x,%{public}08x)"
+ "%@:%@ rejection 11 (%{public}08x,%{public}08x)"
+ "%@:%@, Authorized Locations: total visit dwell, %{public}.0f, number of unique days visited, %{public}ld, Authorized Location, %@."
+ "%@:%@, Detected change in XPC activity criteria for activity, %@, replacing old criteria, %@, maxAttemptCount, %{public}d, with new criteria, %@, maxAttemptCount, %{public}d."
+ "%@:%@, Loaded XPC activity criteria, %@, maxAttemptCount, %{public}d, for activity, %@"
+ "%@:%@, Registering erase-install initialization XPC activity, %@, with criteria, %@"
+ "%@:%@, _runEraseInstallDatabaseInitialization completed status: %d"
+ "%@:%@, also using visit map item (%{private}.6f, %{private}.6f)"
+ "%@:%@, appending ALOI, %@."
+ "%@:%@, applying check between lookbackStartEpoch %@,  stringentLookbackStartEpoch %@ and endTime %@."
+ "%@:%@, dateInterval %@, locationTechnologyAvailability, %{public}08x."
+ "%@:%@, decoded  trusted-time availability flag. trustedTimeWasAvailable, %d."
+ "%@:%@, device not unlocked since last boot, unable to execute retro-registration."
+ "%@:%@, erase-install initialization XPC activity due to criteria change."
+ "%@:%@, expedited sync is required, and current runnning, attempt %d."
+ "%@:%@, expedited sync not required as it has already run."
+ "%@:%@, failed to register any visits, will try again, not disabling visit retro-registration for next launch."
+ "%@:%@, fetched %{public}ld historical locations of interest between %@ and %@."
+ "%@:%@, fetched %{public}ld locations for date interval %@."
+ "%@:%@, fetched %{public}ld motion activities for date interval %@."
+ "%@:%@, fetched %{public}ld visit logs for interval: %@."
+ "%@:%@, found technology (%{public}  d): %@"
+ "%@:%@, found technology (%{public}d): %@"
+ "%@:%@, initiating first expedited sync attempt, storing start date."
+ "%@:%@, most recent location is older than %{public}.0f seconds, %@."
+ "%@:%@, motion activity, %{public}d, cumulative interval %.3f s, position uncertainty rate, %.3f."
+ "%@:%@, no motion activity, defaulting to %{public}f mps."
+ "%@:%@, processing %{public}lu visits for LOI %@."
+ "%@:%@, processing visit, isRegistered, %{public}d, dwell, %{public}.1f: %@"
+ "%@:%@, registered visit retro registration event: %@"
+ "%@:%@, setting status, %d."
+ "%@:%@, skipping ALOI, %@."
+ "%@:%@, skipping nil dateInterval, locationTechnologyAvailability, %{public}08x."
+ "%@:%@, skipping short dateInterval %@, locationTechnologyAvailability, %{public}08x."
+ "%@:%@, starting visit curation, processing %{public}lu LOIs"
+ "%@:%@, successfully fetched retro-registration flag, %@, indicating that it has already run."
+ "%@:%@, successfully fetched retro-registration flag, %@, indicating that it is running."
+ "%@:%@, successfully fetched trusted-time availability flag, %@."
+ "%@:%@, successfully fetched zero retro-registration flags, indicating that we have not already run."
+ "%@:%@, successfully fetched zero trusted-time availability flags."
+ "%@:%@, technology expectation bitset %{public}08x."
+ "%@:%@, unable to curate authorized locations with empty visit log."
+ "%@:%@, unable to fetch trustedNow, leaving _mostRecentDateAtWhichDeviceDataIsTrusted unchanged at %@"
+ "%@:%@, unable to get time since last successful biometric authentication (possibly none since last boot), not updating dateOfMostRecentBiometricAuthentication."
+ "%@:%@, unregistered erase-install initialization XPC activity due to criteria change: %@, error, %@"
+ "%@:%@, unregistered erase-install initialization XPC activity due to successful completion or max-retry limit: %@, error, %@"
+ "%@:%@, updated dateOfMostRecentBiometricAuthentication %f seconds ago, not updating now."
+ "%@:%@, updated dateOfMostRecentBiometricAuthentication to %@."
+ "%@:%@, using default position uncertainty rate, %{public}f mps."
+ "%@:%@, using weighted average position uncertainty rate from motion activity, %{public}f mps."
+ "%@:%@: Authorized Locations: %@."
+ "%@:%@: Ranked Authorized Locations: %@."
+ "%@:%@: curate authorized locations executed, created %d authorized locations, error: %@."
+ "%@:%@: feature not enabled or device not supported."
+ "%@:%@: finished, attempt count, %d, status, %d, error, %@."
+ "%@:%@: hindsight learning executed, error: %@."
+ "%@:%@: started, attempt count, %d."
+ "%@:%@: sync executed, error: %@."
+ "%@:%@: time since last authorized location curation %{public}.0f seconds, greater than threshold %{public}.0f seconds. Clearing authorized location list."
+ "%@:%@: time since last authorized location curation %{public}.0f seconds, less than threshold %{public}.0f seconds. Not regenerating authorized location list."
+ "%s, NO, has not transitioned from idle status yet, origin location, %@, last location, %@"
+ "%s, current status, %@, session configuration, %@, durationSinceLastStatusChange, %.2f"
+ "%s, delaying trigger monitoring until transition to progress state"
+ ", error %@"
+ "-[RTAuthorizedLocationBiometricsManager initWithTrustedTimeCache:defaultsManager:]"
+ "-[RTAuthorizedLocationManager _fetchAuthorizedLocationExtendedStatus:]"
+ "-[RTAuthorizedLocationManager eraseVisitLogDatabase:]"
+ "-[RTAuthorizedLocationManager fetchAuthorizedLocationExtendedStatus:]"
+ "-[RTAuthorizedLocationManager fetchVisitLogsWithOptions:handler:]"
+ "-[RTAuthorizedLocationManager initWithVisitManager:locationManager:distanceCalculator:learnedLocationManager:motionActivityManager:visitLogStore:defaultsManager:xpcActivityManager:dataProtectionManager:persistenceMirroringManager:platform:authorizationManager:]"
+ "-[RTAuthorizedLocationManager runEraseInstallDatabaseInitialization:]"
+ "-[RTAuthorizedLocationMetrics initWithDaemonStartDate:]"
+ "-[RTDaemonClientRegistrarPeopleDiscovery onPeopleDensityUpdateNotification:]_block_invoke"
+ "-[SMSuggestionsManager _getFAFamilyMembersFromAAAFamilyWithHandler:]"
+ "-[SMSuggestionsManager _getSMHandlesFromFAFamilyMembers:error:]"
+ "00001111-2222-3333-4444-555566667777"
+ "07:48:05"
+ "11112222-3333-4444-5555-666677778888"
+ "@\"<RTDaemonClientRegistrarPeopleDiscoveryProtocol>\""
+ "@\"RTAuthorizedLocationBiometricsManager\""
+ "@\"RTAuthorizedLocationDatabaseInitializationMetrics\""
+ "@\"RTAuthorizedLocationMetrics\""
+ "@\"RTDaemonClientRegistrarPeopleDiscovery\""
+ "@\"RTPeopleDensityRecordRunningRecentObservation\""
+ "@\"RTPeopleDiscoveryServiceConfiguration\""
+ "@136@0:8@16@24@32Q40Q48@56@64B72S76@80@88@96@104d112d120@128"
+ "@88@0:8@16d24q32q40q48Q56q64q72q80"
+ "Aggregated Service Configuration: %@"
+ "B24@0:8^d16"
+ "Buffered people density events failed"
+ "CLLocationManagerGathering conf %@"
+ "EraseInstallInitializationAttemptCount"
+ "EraseInstallInitializationCompletionTimeHours"
+ "FamiliarLoisGeneratedDuringEraseInstallInitialization"
+ "FractionOfVisitsToTopLOIWithGPS"
+ "FractionOfVisitsToTopLOIWithWiFiHI"
+ "HH.mm"
+ "Invalid parameter not satisfying: daemonStartDate (in %s:%d)"
+ "Invalid parameter not satisfying: databaseInitCompletionHandler (in %s:%d)"
+ "Invalid parameter not satisfying: familyMembers (in %s:%d)"
+ "Invalid parameter not satisfying: persistenceMirroringManager (in %s:%d)"
+ "Invalid parameter not satisfying: trustedTimeCache (in %s:%d)"
+ "IsLoiHistoricallyLocationStarved"
+ "LocationServicesEnabled"
+ "May  2 2024"
+ "Metric, eraseInstallInitialization, %@"
+ "Metric, query, %@"
+ "Moments"
+ "OK"
+ "RTAuthorizedLocation, rank, %ld, dwellTime_s, %f, numberOfDaysVisited, %ld, ageDaysFirstRegisteredVisit, %d, _ageDaysFirstVisit %d, locationTechnologyAvailability, %08x, visitsWithTechnologyAnnotation, %d, visitsWithGPS, %d, visitsWithWiFiHI, %d, loi, %@."
+ "RTAuthorizedLocationBiometricsManager"
+ "RTAuthorizedLocationDatabaseInitializationMetrics"
+ "RTAuthorizedLocationEraseInstallInitActivityAllowBattery"
+ "RTAuthorizedLocationEraseInstallInitActivityAttemptCount"
+ "RTAuthorizedLocationEraseInstallInitActivityDelaySeconds"
+ "RTAuthorizedLocationEraseInstallInitActivityDownloadSize"
+ "RTAuthorizedLocationEraseInstallInitActivityGracePeriodSeconds"
+ "RTAuthorizedLocationEraseInstallInitActivityInexpensiveConnectivity"
+ "RTAuthorizedLocationEraseInstallInitActivityIntervalSeconds"
+ "RTAuthorizedLocationEraseInstallInitActivityMaxAttemptCount"
+ "RTAuthorizedLocationEraseInstallInitActivityPriority"
+ "RTAuthorizedLocationEraseInstallInitActivityStartDate"
+ "RTAuthorizedLocationEraseInstallInitActivityUploadSize"
+ "RTAuthorizedLocationMetrics"
+ "RTDaemonClient fetchOngoingPeopleDensity"
+ "RTDaemonClientRegistrarPeopleDiscovery"
+ "RTDaemonClientRegistrarPeopleDiscoveryProtocol"
+ "RTDefaultsAuthorizedLocationSecondsSinceLastBiometricAuthentication"
+ "RTDefaultsLocationManagerBypassPreprocessor"
+ "RTDefaultsSMTriggerDestinationIdleMaxDistanceThresholdKey"
+ "RTDefaultsSMTriggerDestinationIdleTimeoutThresholdKey"
+ "RTPeopleDensityRecordRunningRecentObservation"
+ "RTPeopleDensityUpdateNotification"
+ "RTPurgable performPurgeOfType called"
+ "RoutineEnabled"
+ "T@\"<RTDaemonClientRegistrarPeopleDiscoveryProtocol>\",W,N,V_delegate"
+ "T@\"CLLocation\",&,N,V_originLocation"
+ "T@\"NSArray\",R,N,V_densityBundles"
+ "T@\"NSDate\",&,N,V_dateOfLastUpdate"
+ "T@\"NSDate\",&,N,V_dateOfMostRecentBiometricAuthentication"
+ "T@\"NSDate\",&,N,V_eraseInstallInitializationStartDate"
+ "T@\"NSDate\",&,N,V_lastQueryMetricSubmissionDate"
+ "T@\"NSDate\",&,N,V_mostRecentDateAtWhichDeviceDataIsTrusted"
+ "T@\"NSDate\",C,N,V_startDatetime"
+ "T@\"NSDate\",R,N,V_daemonStartDate"
+ "T@\"NSMutableArray\",&,N,V_runningAdvertisementsPerRecord"
+ "T@\"NSMutableArray\",&,N,V_runningRecords"
+ "T@\"NSMutableDictionary\",&,N,V_clientConfigurations"
+ "T@\"NSString\",R,C,N,V_clientIdentifier"
+ "T@\"RTAuthorizedLocationBiometricsManager\",R,N,V_biometricsManager"
+ "T@\"RTAuthorizedLocationDatabaseInitializationMetrics\",&,N,V_initializationMetrics"
+ "T@\"RTAuthorizedLocationMetrics\",&,N,V_metrics"
+ "T@\"RTDaemonClientRegistrarPeopleDiscovery\",&,N,V_peopleDiscoveryRegistrar"
+ "T@\"RTPeopleDensityRecordRunningRecentObservation\",&,N,V_runningRecentBundle"
+ "T@\"RTPeopleDiscoveryServiceConfiguration\",&,N,V_momentsConfiguration"
+ "T@\"RTPeopleDiscoveryServiceConfiguration\",C,N,V_configuration"
+ "T@\"RTPersistenceMirroringManager\",R,N,V_persistenceMirroringManager"
+ "T@\"RTXPCActivityCriteria\",&,N,V_eraseInstallInitializationXpcCriteria"
+ "TB,N,V_broughtUp"
+ "TB,N,V_isEraseInstallDatabaseInitializationRequired"
+ "TB,N,V_isUnlockedSinceBoot"
+ "TB,N,V_relaxTrustedTimeRequirement"
+ "TB,R,N,V_isSupportedDevice"
+ "TB,V_allowUnsecureTimeFallback"
+ "TB,V_isHistoricallyALowDiversityLocation"
+ "TB,V_locationServicesEnabled"
+ "TB,V_routineEnabled"
+ "TQ,N,V_eraseInstallDatabaseInitializationAttemptCount"
+ "TQ,N,V_eraseInstallDatabaseInitializationMaxAttemptCount"
+ "TQ,R,V_locationTechnologyAvailability"
+ "Td,N,V_idleMaxDistanceThreshold"
+ "Td,N,V_idleTimeoutThreshold"
+ "Td,V_currentObservationIntervalSeconds"
+ "Tf,V_currentConfidenceThreshold"
+ "Tf,V_fractionOfVisitsToTopLOIWithGPS"
+ "Tf,V_fractionOfVisitsToTopLOIWithWiFiHI"
+ "Ti,V_eraseInstallInitializationAttemptCount"
+ "Ti,V_eraseInstallInitializationCompletionTimeHours"
+ "Ti,V_numberOfALOIsGeneratedDuringEraseInstallInitialization"
+ "Ti,V_numberOfVisitsRegisteredDuringEraseInstallInitialization"
+ "Ti,V_visitsToTopLOIWithTechAvailabilityKnown"
+ "Time of the day logged from user context: %f"
+ "TimeSinceDaemonStartHours"
+ "TotalNumberOfVisitsToTopLOIWithKnownTechnology"
+ "Tq,D"
+ "Tq,R,V_visitsWithGPS"
+ "Tq,R,V_visitsWithTechnologyAnnotation"
+ "Tq,R,V_visitsWithWiFiHI"
+ "Tq,V_rank"
+ "Visit UUID, %s, registrationDate, %@, locationTechnologyAvailability, %ld"
+ "Visit UUID, %s, registrationDate, %@, locationTechnologyAvailability, %ld, isRetroRegistration, %d, isTrustedTime, %d"
+ "VisitsRegisteredDuringEraseInstallInitialization"
+ "_addClientConfiguration:withIdentifier:"
+ "_aggregateAndApplyConfiguration"
+ "_allowUnsecureTimeFallback"
+ "_biometricsManager"
+ "_broughtUp"
+ "_checkConfiguration"
+ "_clientConfigurations"
+ "_computeDensityScore:scanDuration:forRecords:"
+ "_computeLocationTechnologyAvailabilityForDateInterval:"
+ "_computeLocationTechnologyExpectationFromHistoricalAvailability:"
+ "_computeMeanOfRssi divide by 0: %@"
+ "_computeMeanOfRssi:"
+ "_convertObservationIntervalToDouble:"
+ "_currentConfidenceThreshold"
+ "_currentObservationIntervalSeconds"
+ "_daemonStartDate"
+ "_dateOfLastUpdate"
+ "_dateOfMostRecentBiometricAuthentication"
+ "_densityBundles"
+ "_eraseInstallDatabaseInitializationAttemptCount"
+ "_eraseInstallDatabaseInitializationMaxAttemptCount"
+ "_eraseInstallInitializationAttemptCount"
+ "_eraseInstallInitializationCompletionTimeHours"
+ "_eraseInstallInitializationStartDate"
+ "_eraseInstallInitializationXpcCriteria"
+ "_evaluateStatusUsingCurrentLocation:"
+ "_fetchAuthorizedLocationExtendedStatus:"
+ "_fetchAuthorizedLocationExtendedStatusWithMetrics:"
+ "_fractionOfVisitsToTopLOIWithGPS"
+ "_fractionOfVisitsToTopLOIWithWiFiHI"
+ "_getFAFamilyMembersFromAAAFamilyWithHandler:"
+ "_getSMHandlesFromFAFamilyMembers:error:"
+ "_getTimeSinceLastSuccessfulBiometricAuthentication:"
+ "_idleMaxDistanceThreshold"
+ "_idleTimeoutThreshold"
+ "_initializationMetrics"
+ "_isEraseInstallDatabaseInitializationRequired"
+ "_isExpeditedSyncAndLearnRequired"
+ "_isHistoricallyALowDiversityLocation"
+ "_isRoutineEnabled"
+ "_isSupportedDevice"
+ "_lastQueryMetricSubmissionDate"
+ "_loadEraseInstallInitializationXPCCriteriaFromDefaults"
+ "_locationAvailabilityFromCLLocation:"
+ "_locationServicesEnabled"
+ "_locationTechnologyAvailability"
+ "_logClientConfigurations"
+ "_momentsConfiguration"
+ "_mostRecentDateAtWhichDeviceDataIsTrusted"
+ "_numberOfALOIsGeneratedDuringEraseInstallInitialization"
+ "_numberOfVisitsRegisteredDuringEraseInstallInitialization"
+ "_onPeopleDensityUpdateNotification:"
+ "_peopleDiscoveryRegistrar"
+ "_persistenceMirroringManager"
+ "_purgeEvents"
+ "_purgeEvents purging with expirationInterval: %f before date: %@"
+ "_rank"
+ "_registerForDeviceUnlockNotification"
+ "_removeClientConfiguration:"
+ "_runEraseInstallDatabaseInitialization:"
+ "_runningAdvertisementsPerRecord"
+ "_runningRecentBundle"
+ "_runningRecords"
+ "_scanLevelFromServiceLevel:observationInterval:"
+ "_setupEraseInstallDatabaseInitializationActivity"
+ "_startDatetime"
+ "_updateMostRecentDateAtWhichDeviceDataIsTrusted"
+ "_updateVisitLogDistantFutureFlagWithStatus:TrustedTimeAvailability:isRetroRegistration:"
+ "_visitsToTopLOIWithTechAvailabilityKnown"
+ "_visitsWithGPS"
+ "_visitsWithTechnologyAnnotation"
+ "_visitsWithWiFiHI"
+ "addClient:withIdentifier:withConfiguration:"
+ "addPendingPeopleDensityUpdateBlock:failBlock:description:"
+ "allowUnsecureTimeFallback"
+ "availableDevices"
+ "b"
+ "biometricsManager"
+ "broughtUp"
+ "clearing people discovery monitoring %@"
+ "client, %@, _restorationIdentifier, %@"
+ "client, %@, not connected. buffering people density events, count %lu"
+ "clientConfigurations"
+ "com.apple.locationd.gathering.bufferedDevicesReceived"
+ "com.apple.locationd.gathering.came_up"
+ "com.apple.routined.authorizedLocation.eraseInstallInitialization"
+ "computeRssiHistogramForAdvs:"
+ "configure:withCompletionHandler:"
+ "convertMachContinuousTicksToSeconds:"
+ "currentConfidenceThreshold"
+ "currentObservationIntervalSeconds"
+ "currentStatusDate"
+ "daemonStartDate"
+ "dateOfLastUpdate"
+ "dateOfMostRecentBiometricAuthentication"
+ "decodeTimeSourceWithValue:isRetroRegistration:isTrusted:"
+ "defaultOverrideTimeSinceLastSuccessfulBiometricAuthentication:"
+ "densityCallbackConfiguration"
+ "deviceWithDescriptor:error:"
+ "done shutdown %@"
+ "encodeTimeSourceWithValue:isTrusted:isRetroRegistration:"
+ "eraseInstallDatabaseInitializationAttemptCount"
+ "eraseInstallDatabaseInitializationMaxAttemptCount"
+ "eraseInstallInitializationAttemptCount"
+ "eraseInstallInitializationCompletionTimeHours"
+ "eraseInstallInitializationStartDate"
+ "eraseInstallInitializationXpcCriteria"
+ "eraseVisitLogDatabase:"
+ "error unarchiving people discovery registrar, %@"
+ "fetchAuthorizedLocationExtendedStatus:"
+ "fetchCurrentObservationBundle"
+ "fetchMostRecentPeopleDensity:"
+ "fetchOngoingPeopleDensity:"
+ "fetchVisitLogsWithDateInterval:reply:"
+ "forceAuthorizedLocationEraseInstallInitialization:"
+ "fractionOfVisitsToTopLOIWithGPS"
+ "fractionOfVisitsToTopLOIWithWiFiHI"
+ "getEraseInstallRetroRegistrationStatus"
+ "getHistogram"
+ "i32@0:8Q16Q24"
+ "identifier, %@, name, %@, category, %@, latitude, %@, longitude, %@, uncertainty, %@, referenceFrame, %@, mapItemSource, %@, mapItemPlaceType, %@, muid, %@, resultProviderID, %@, geoMapItemHandle, %@, creationDate, %@, expirationDate, %@, displayLanguage, %@, disputed, %@, address, %@, extendedAttributesIdentifier, %@"
+ "idleMaxDistanceThreshold"
+ "idleTimeoutThreshold"
+ "initWithDaemonStartDate:"
+ "initWithLoi:dwellTime:numberOfDaysVisited:ageDaysFirstVisit:ageDaysFirstRegisteredVisit:locationTechnologyAvailability:visitsWithTechnologyAnnotation:visitsWithGPS:visitsWithWiFiHI:"
+ "initWithPeopleDensityBundles:"
+ "initWithPeopleDiscoveryProvider:queue:"
+ "initWithServiceLevel:storageDuration:observationInterval:densityCallbackConfiguration:"
+ "initWithSessionIdentifier:currentStatus:currentStatusDate:lastLockDate:lastUnlockDate:predominantModeOfTransport:numberOfETARetries:shouldRetryETAQuery:roundTripReminderDate:timeToUpdateStatus:upperBoundEta:mapsExpectedTravelTime:remainingDistance:date:"
+ "initWithTrustedTimeCache:defaultsManager:"
+ "initWithVisitIdentifier:registrationDate:locationTechnologyAvailability:"
+ "initWithVisitManager:locationManager:distanceCalculator:learnedLocationManager:motionActivityManager:visitLogStore:defaultsManager:xpcActivityManager:dataProtectionManager:persistenceMirroringManager:platform:authorizationManager:"
+ "initializationMetrics"
+ "isEraseInstallDatabaseInitializationRequired"
+ "isHistoricallyALowDiversityLocation"
+ "isSupportedDevice"
+ "lastMatchEventWithError:"
+ "lastQueryMetricSubmissionDate"
+ "locationTechnologyAvailability"
+ "managedObjectWithSessionIdentifier:lastLockDate:lastUnlockDate:predominantModeOfTransport:currentStatus:currentStatusDate:date:shouldRetryETAQuery:numberOfETARetries:upperBoundEtaCrowFliesUpperBoundEta:upperBoundEtaMapsUpperBoundEta:roundTripReminderDate:timeToUpdateStatus:mapsExpectedTravelTime:remainingDistance:managedObjectContext:"
+ "memberType"
+ "members"
+ "momentsConfiguration"
+ "mostRecentDateAtWhichDeviceDataIsTrusted"
+ "numberOfALOIsGeneratedDuringEraseInstallInitialization"
+ "numberOfVisitsRegisteredDuringEraseInstallInitialization"
+ "observationInterval"
+ "onBufferedDevicesReceivedNotification"
+ "onCoreLocationProviderCameUpNotification"
+ "onDensityUpdate:error:"
+ "onPeopleDensityUpdateNotification:"
+ "overriding idle timeout threshold"
+ "overriding idle to progress transition max distance threshold"
+ "peopleDiscoveryRegistrar"
+ "peopleDiscoveryRegistrar:didReceivePeopleDensityUpdate:error:"
+ "persistenceMirroringManager"
+ "rank"
+ "rdar122420473 identifier %@, configuration %@"
+ "received nil people density in notification, returning."
+ "received service configuration %@ for client %@ using identifier %@"
+ "removeClient:"
+ "restoring people discovery monitoring %@"
+ "runEraseInstallDatabaseInitialization:"
+ "runningAdvertisementsPerRecord"
+ "runningRecentBundle"
+ "runningRecords"
+ "sending people density events, count %lu, to client, %@"
+ "serviceLevel"
+ "setAllowUnsecureTimeFallback:"
+ "setBroughtUp:"
+ "setClientConfigurations:"
+ "setCurrentConfidenceThreshold:"
+ "setCurrentObservationIntervalSeconds:"
+ "setCurrentStatusDate:"
+ "setDateOfLastUpdate:"
+ "setDateOfMostRecentBiometricAuthentication:"
+ "setEraseInstallDatabaseInitializationAttemptCount:"
+ "setEraseInstallDatabaseInitializationMaxAttemptCount:"
+ "setEraseInstallInitializationAttemptCount:"
+ "setEraseInstallInitializationCompletionTimeHours:"
+ "setEraseInstallInitializationStartDate:"
+ "setEraseInstallInitializationXpcCriteria:"
+ "setEraseInstallRetroRegistrationStatus:"
+ "setFractionOfVisitsToTopLOIWithGPS:"
+ "setFractionOfVisitsToTopLOIWithWiFiHI:"
+ "setIdleMaxDistanceThreshold:"
+ "setIdleTimeoutThreshold:"
+ "setInitializationMetrics:"
+ "setIsEraseInstallDatabaseInitializationRequired:"
+ "setIsHistoricallyALowDiversityLocation:"
+ "setLastQueryMetricSubmissionDate:"
+ "setLocationServicesEnabled:"
+ "setLocationTechnologyAvailability:"
+ "setMomentsConfiguration:"
+ "setMostRecentDateAtWhichDeviceDataIsTrusted:"
+ "setNumberOfALOIsGeneratedDuringEraseInstallInitialization:"
+ "setNumberOfVisitsRegisteredDuringEraseInstallInitialization:"
+ "setOriginLocation:"
+ "setPeopleDiscoveryRegistrar:"
+ "setRank:"
+ "setRunningAdvertisementsPerRecord:"
+ "setRunningRecentBundle:"
+ "setRunningRecords:"
+ "setStartDatetime:"
+ "setTrustedTimeRecentAvailability:"
+ "setVisitsToTopLOIWithTechAvailabilityKnown:"
+ "startDatetime"
+ "startMonitoringForPeopleDiscovery:configuration:reply:"
+ "startMonitoringForPeopleDiscoveryWithIdentifier:configuration:"
+ "startRequestWithCompletionHandler:"
+ "stopMonitoringForPeopleDiscovery"
+ "stopMonitoringForPeopleDiscoveryWithReply:"
+ "storageDuration"
+ "timeSinceDaemonStart"
+ "timeSinceLastQueryMetricsSubmission"
+ "timeStamp"
+ "trimRunningRecordsBeforeRef:"
+ "updateConfidenceThreshold:"
+ "updateDateOfLastSuccessfulBiometricAuthentication"
+ "updateHistogramWithAdvs:"
+ "updateObservationIntervalSeconds:"
+ "v24@0:8@?<v@?@\"RTAuthorizedLocationStatus\"q@\"NSError\">16"
+ "v24@0:8@?<v@?@\"RTPeopleDensity\"@\"NSError\">16"
+ "v24@?0@\"FAFamilyCircle\"8@\"NSError\"16"
+ "v24@?0@\"RTPeopleDensity\"8@\"NSError\"16"
+ "v32@0:8@\"NSDateInterval\"16@?<v@?@\"NSArray\"@\"NSError\">24"
+ "v32@0:8q16B24B28"
+ "v32@?0@\"RTAuthorizedLocationStatus\"8q16@\"NSError\"24"
+ "v40@0:8@\"NSString\"16@\"RTPeopleDiscoveryServiceConfiguration\"24@?<v@?@\"NSError\">32"
+ "v40@0:8@\"RTDaemonClientRegistrarPeopleDiscovery\"16@\"NSArray\"24@\"NSError\"32"
+ "visitsToTopLOIWithTechAvailabilityKnown"
+ "visitsWithGPS"
+ "visitsWithTechnologyAnnotation"
+ "visitsWithWiFiHI"
+ "wasTrustedTimeRecentlyAvailable"
+ "}"
- "\x14#"
- "\x1b"
- "\x1c\x12\x11"
- "\x1f\x01"
- "\"\x1f\x0f\v"
- "#RTPeopleDiscoveryProvider file does not exist"
- "%@, %@, chat identifiers, %@"
- "%@, %@, date check failed, current date, %@, sunset date, %@, time interval since sunset, %.3f, sunrise date, %@, time interval to sunrise, %.3f, threshold, %.3f"
- "%@, %@, intervalSincePreviousVisit, %.2f, distanceFromPreviousVisit, %.2f, visits to same LOI, %@"
- "%@, %@, message body, %@, chat identifier, %@, didInteract, %@"
- "%@:%@ completed."
- "%@:%@ exceeded max retry, disabling futher retroactive registration of visits."
- "%@:%@ feature not enabled."
- "%@:%@ passed 11 (%{private}d)"
- "%@:%@ rejection 11 (%{private}d)"
- "%@:%@ returning %zu available authorized locations."
- "%@:%@, Authorized Locations: total visit dwell, %{private}.0f, number of unique days visited, %{private}ld, Authorized Location, %@."
- "%@:%@, INFO, retroactive registration of all stored visits disabled (either manually by defaults or automatically by previous launch)."
- "%@:%@, WARNING, defaults set to ignore visit registration date in computing Authorized Location list"
- "%@:%@, appending LOI, total visit dwell, %{private}.0f, threshold, %{private}.0f, number of unique days visited, %{private}ld, threshold, %{private}ld, LOI %@."
- "%@:%@, applying check between startTime %@ and endTime %@."
- "%@:%@, failed to register any visits, will try again, not setting default RTDefaultsAuthorizedLocationIsFirstRunSinceSwUpdate to NO."
- "%@:%@, fetched %{private}ld historical locations of interest between %@ and %@."
- "%@:%@, fetched %{private}ld locations for date interval %@."
- "%@:%@, fetched %{private}ld motion activities for date interval %@."
- "%@:%@, fetched %{private}ld visit logs for interval: %@."
- "%@:%@, found technology: %@"
- "%@:%@, most recent location is older than %{private}.0f seconds, %@."
- "%@:%@, motion activity, %{private}d, cumulative interval %.3f s, position uncertainty rate, %.3f."
- "%@:%@, no motion activity, defaulting to %{private}f mps."
- "%@:%@, processing %{private}lu visits for LOI %@."
- "%@:%@, processing visit, isRegistered, %{public}d, dwell, %{private}.1f: %@"
- "%@:%@, setting default RTDefaultsAuthorizedLocationIsFirstRunSinceSwUpdate to NO."
- "%@:%@, skipping LOI, total visit dwell, %{private}.0f, threshold, %{private}.0f, number of unique days visited, %{private}ld, threshold, %{private}ld, LOI %@."
- "%@:%@, starting visit curation, processing %{private}lu LOIs"
- "%@:%@, using default position uncertainty rate, %{private}f mps."
- "%@:%@, using weighted average position uncertainty rate from motion activity, %{private}f mps."
- "%@:%@: feature not enabled."
- "%@:%@: time since last authorized location curation %{private}.0f seconds, greater than threshold %{private}.0f seconds. Clearing authorized location list."
- "%@:%@: time since last authorized location curation %{private}.0f seconds, less than threshold %{private}.0f seconds. Not regenerating authorized location list."
- "%@:%@:_authorizedLocationArr Sorted Authorized Locations: total visit dwell, %{private}.0f, number of unique days visited, %{private}ld, Authorized Location, %@."
- "%s, No active session available"
- "%s, session configuration, %@, current status, %@"
- "-[RTAuthorizedLocationManager _fetchAuthorizedLocationStatus:]"
- "-[RTAuthorizedLocationManager fetchAuthorizedLocationStatus:]"
- "-[RTAuthorizedLocationManager initWithVisitManager:locationManager:distanceCalculator:learnedLocationManager:motionActivityManager:visitLogStore:defaultsManager:xpcActivityManager:dataProtectionManager:]"
- "21:00:06"
- "@128@0:8@16@24@32Q40Q48@56B64S68@72@80@88@96d104d112@120"
- "@56@0:8@16d24q32q40q48"
- "Mar 13 2024"
- "Metric, %@"
- "RTAuthorizedLocation, loi, %@, dwellTime_s, %f, numberOfDaysVisited, %ld, age first visit, %d/%d."
- "RTDefaultsAuthorizedLocationIgnoreVisitRegistrationDate"
- "RTDefaultsAuthorizedLocationIsFirstRunSinceSwUpdate"
- "RTDefaultsVisitPipelineMotionStateTrimmerDisabled"
- "SafetyAlerts"
- "T@\"NSDate\",&,N,V_lastMetricSubmissionDate"
- "T@\"NSDate\",&,V_endDate"
- "T@\"NSDate\",&,V_startDate"
- "T@\"RTAuthorizedLocationCurationMetrics\",&,V_curationMetrics"
- "TB,N,V_momentsEnabled"
- "TB,N,V_safetyAlertEnabled"
- "TB,V_ignoreVisitRegistrationDate"
- "TB,V_isFirstRunSinceSwUpgrade"
- "TB,V_isUnlockedSinceBoot"
- "TB,V_relaxTrustedTimeRequirement"
- "TQ,V_retroRegistrationAttemptCount"
- "Visit UUID, %s, registrationDate, %@"
- "_checkDefaults"
- "_computeDensityScore:scanDuration:"
- "_decodeTimeSourceWithValue:isRetroRegistration:isTrusted:"
- "_encodeTimeSourceWithValue:isTrusted:isRetroRegistration:"
- "_fetchAuthorizedLocationStatus:"
- "_ignoreVisitRegistrationDate"
- "_isFirstRunSinceSwUpgrade"
- "_lastMetricSubmissionDate"
- "_momentsEnabled"
- "_retroRegistrationAttemptCount"
- "_safetyAlertEnabled"
- "_setupScheduledOneTimeRegistrationTask"
- "body"
- "c"
- "clean up people density bundles, error %@"
- "clean up proximity events, error %@"
- "getStateForSetting:"
- "identifier, %@, name, %@, category, %@, latitude, %@, longitude, %@, uncertainty, %@, referenceFrame, %@, mapItemSource, %@, mapItemPlaceType, %@, muid, %@, resultProviderID, %@, geoMapItemHandle, %@, creationDate, %@, expirationDate, %@, displayLanguage, %@, disputed, %b, address, %@, extendedAttributesIdentifier, %@"
- "ignoreVisitRegistrationDate"
- "initWithLoi:dwellTime:numberOfDaysVisited:ageDaysFirstVisit:ageDaysFirstRegisteredVisit:"
- "initWithSessionIdentifier:currentStatus:lastLockDate:lastUnlockDate:predominantModeOfTransport:numberOfETARetries:shouldRetryETAQuery:roundTripReminderDate:timeToUpdateStatus:upperBoundEta:mapsExpectedTravelTime:remainingDistance:date:"
- "initWithVisitIdentifier:registrationDate:"
- "initWithVisitManager:locationManager:distanceCalculator:learnedLocationManager:motionActivityManager:visitLogStore:defaultsManager:xpcActivityManager:dataProtectionManager:"
- "isFirstRunSinceSwUpgrade"
- "isSaewEnabledSync:"
- "lastMetricSubmissionDate"
- "managedObjectWithSessionIdentifier:lastLockDate:lastUnlockDate:predominantModeOfTransport:currentStatus:date:shouldRetryETAQuery:numberOfETARetries:upperBoundEtaCrowFliesUpperBoundEta:upperBoundEtaMapsUpperBoundEta:roundTripReminderDate:timeToUpdateStatus:mapsExpectedTravelTime:remainingDistance:managedObjectContext:"
- "moments enabled %d, safetyAlert enabled %d"
- "momentsEnabled"
- "on state change for moments settings, state: %d, setting: %d"
- "onPeopleSwitchUpdated, enabled: %@"
- "onPeopleSwitchUpdated:"
- "people discovery is not enabled"
- "people discovery start, momentsEnabled, %d, safetyAlertEnabled, %d"
- "retroRegistrationAttemptCount"
- "safetyAlertEnabled"
- "setIgnoreVisitRegistrationDate:"
- "setIsFirstRunSinceSwUpgrade:"
- "setLastMetricSubmissionDate:"
- "setMomentsEnabled:"
- "setRetroRegistrationAttemptCount:"
- "setSafetyAlertEnabled:"
- "sharedInterface"
- "softlink:r:path:/System/Library/PrivateFrameworks/SafetyAlerts.framework/SafetyAlerts"
- "v24@?0@\"RTAuthorizedLocationStatus\"8@\"NSError\"16"

```
