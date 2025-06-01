## CoreRoutine

> `/System/Library/PrivateFrameworks/CoreRoutine.framework/CoreRoutine`

```diff

-900.0.12.0.0
-  __TEXT.__text: 0x3c370
+900.0.25.0.0
+  __TEXT.__text: 0x3e348
   __TEXT.__auth_stubs: 0x680
-  __TEXT.__objc_methlist: 0x45ac
+  __TEXT.__objc_methlist: 0x47ec
   __TEXT.__const: 0x190
-  __TEXT.__oslogstring: 0x2167
-  __TEXT.__cstring: 0x3bc9
+  __TEXT.__oslogstring: 0x2358
+  __TEXT.__cstring: 0x3ddc
   __TEXT.__gcc_except_tab: 0x280
-  __TEXT.__unwind_info: 0x1100
-  __TEXT.__objc_classname: 0x856
-  __TEXT.__objc_methname: 0x9170
-  __TEXT.__objc_methtype: 0x1b0e
-  __TEXT.__objc_stubs: 0x50e0
+  __TEXT.__unwind_info: 0x1158
+  __TEXT.__objc_classname: 0x8cd
+  __TEXT.__objc_methname: 0x974e
+  __TEXT.__objc_methtype: 0x1c31
+  __TEXT.__objc_stubs: 0x5380
   __DATA_CONST.__got: 0x58
-  __DATA_CONST.__const: 0xb68
-  __DATA_CONST.__objc_classlist: 0x290
+  __DATA_CONST.__const: 0xc40
+  __DATA_CONST.__objc_classlist: 0x2a8
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x63d8
-  __DATA_CONST.__objc_selrefs: 0x1be8
+  __DATA_CONST.__objc_const: 0x67a0
+  __DATA_CONST.__objc_selrefs: 0x1cb0
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_classrefs: 0x2d0
-  __DATA_CONST.__objc_superrefs: 0x260
+  __DATA_CONST.__objc_classrefs: 0x2e8
+  __DATA_CONST.__objc_superrefs: 0x278
   __DATA_CONST.__objc_arraydata: 0x90
-  __AUTH_CONST.__cfstring: 0x3900
-  __AUTH_CONST.__objc_const: 0x2b20
+  __AUTH_CONST.__cfstring: 0x3b60
+  __AUTH_CONST.__objc_const: 0x2c88
   __AUTH_CONST.__const: 0x380
   __AUTH_CONST.__objc_intobj: 0xa8
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__auth_got: 0x350
-  __AUTH.__objc_data: 0x640
-  __DATA.__objc_ivar: 0x4b0
+  __AUTH.__objc_data: 0x730
+  __DATA.__objc_ivar: 0x4d4
   __DATA.__data: 0x2c0
-  __DATA_DIRTY.__objc_ivar: 0x98
+  __DATA_DIRTY.__objc_ivar: 0xa8
   __DATA_DIRTY.__objc_data: 0x1360
   __DATA_DIRTY.__data: 0x30
   __DATA_DIRTY.__bss: 0x40

   - /System/Library/PrivateFrameworks/GeoServices.framework/GeoServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 1243C020-A0C9-3E06-A569-06303F66D33D
-  Functions: 1654
-  Symbols:   5326
-  CStrings:  2916
+  UUID: E2990DFA-7DED-3628-99BF-082A85AC477B
+  Functions: 1707
+  Symbols:   5497
+  CStrings:  3024
 
Symbols:
+ +[RTPeopleDensityCallbackConfiguration supportsSecureCoding]
+ +[RTPeopleDiscoveryServiceConfiguration supportsSecureCoding]
+ -[RTPeopleDensityCallbackConfiguration .cxx_destruct]
+ -[RTPeopleDensityCallbackConfiguration copyWithZone:]
+ -[RTPeopleDensityCallbackConfiguration densityUpdateHandler]
+ -[RTPeopleDensityCallbackConfiguration descriptionDictionary]
+ -[RTPeopleDensityCallbackConfiguration description]
+ -[RTPeopleDensityCallbackConfiguration encodeWithCoder:]
+ -[RTPeopleDensityCallbackConfiguration initWithCoder:]
+ -[RTPeopleDensityCallbackConfiguration initWithPeriodicReportInterval:magnitude:densityUpdateHandler:]
+ -[RTPeopleDensityCallbackConfiguration init]
+ -[RTPeopleDensityCallbackConfiguration isEqual:]
+ -[RTPeopleDensityCallbackConfiguration magnitude]
+ -[RTPeopleDensityCallbackConfiguration periodicReportInterval]
+ -[RTPeopleDiscoveryServiceConfiguration .cxx_destruct]
+ -[RTPeopleDiscoveryServiceConfiguration copyWithZone:]
+ -[RTPeopleDiscoveryServiceConfiguration densityCallbackConfiguration]
+ -[RTPeopleDiscoveryServiceConfiguration descriptionDictionary]
+ -[RTPeopleDiscoveryServiceConfiguration description]
+ -[RTPeopleDiscoveryServiceConfiguration encodeWithCoder:]
+ -[RTPeopleDiscoveryServiceConfiguration initWithCoder:]
+ -[RTPeopleDiscoveryServiceConfiguration initWithServiceLevel:storageDuration:observationInterval:densityCallbackConfiguration:]
+ -[RTPeopleDiscoveryServiceConfiguration init]
+ -[RTPeopleDiscoveryServiceConfiguration isEqual:]
+ -[RTPeopleDiscoveryServiceConfiguration observationInterval]
+ -[RTPeopleDiscoveryServiceConfiguration serviceLevel]
+ -[RTPeopleDiscoveryServiceConfiguration storageDuration]
+ -[RTRoutineManager fetchCurrentPeopleDensity:]
+ -[RTRoutineManager onDensityUpdate:error:]
+ -[RTRoutineManager peopleDiscoveryErrorHandler]
+ -[RTRoutineManager peopleDiscoveryRegistrant]
+ -[RTRoutineManager setPeopleDiscoveryErrorHandler:]
+ -[RTRoutineManager setPeopleDiscoveryRegistrant:]
+ -[RTRoutineManager startMonitoringForPeopleDiscovery:handler:]
+ -[RTRoutineManager stopMonitoringForPeopleDiscoveryWithHandler:]
+ -[RTRoutineManagerExportedObject onDensityUpdate:error:]
+ -[RTRoutineManagerRegistrantPeopleDiscovery .cxx_destruct]
+ -[RTRoutineManagerRegistrantPeopleDiscovery configurationIdentifier]
+ -[RTRoutineManagerRegistrantPeopleDiscovery configuration]
+ -[RTRoutineManagerRegistrantPeopleDiscovery initWithConfigurationIdentifier:]
+ -[RTRoutineManagerRegistrantPeopleDiscovery onDensityUpdate:error:]
+ -[RTRoutineManagerRegistrantPeopleDiscovery registered]
+ -[RTRoutineManagerRegistrantPeopleDiscovery startMonitoringForPeopleDiscovery:]
+ -[RTRoutineManagerRegistrantPeopleDiscovery stopMonitoringForPeopleDiscovery]
+ GCC_except_table100
+ GCC_except_table93
+ _OBJC_CLASS_$_RTPeopleDensityCallbackConfiguration
+ _OBJC_CLASS_$_RTPeopleDiscoveryServiceConfiguration
+ _OBJC_CLASS_$_RTRoutineManagerRegistrantPeopleDiscovery
+ _OBJC_IVAR_$_RTPeopleDensityCallbackConfiguration._densityUpdateHandler
+ _OBJC_IVAR_$_RTPeopleDensityCallbackConfiguration._magnitude
+ _OBJC_IVAR_$_RTPeopleDensityCallbackConfiguration._periodicReportInterval
+ _OBJC_IVAR_$_RTPeopleDiscoveryServiceConfiguration._densityCallbackConfiguration
+ _OBJC_IVAR_$_RTPeopleDiscoveryServiceConfiguration._observationInterval
+ _OBJC_IVAR_$_RTPeopleDiscoveryServiceConfiguration._serviceLevel
+ _OBJC_IVAR_$_RTPeopleDiscoveryServiceConfiguration._storageDuration
+ _OBJC_IVAR_$_RTRoutineManager._peopleDiscoveryErrorHandler
+ _OBJC_IVAR_$_RTRoutineManager._peopleDiscoveryRegistrant
+ _OBJC_METACLASS_$_RTPeopleDensityCallbackConfiguration
+ _OBJC_METACLASS_$_RTPeopleDiscoveryServiceConfiguration
+ _OBJC_METACLASS_$_RTRoutineManagerRegistrantPeopleDiscovery
+ _ObservationIntervalDescriptor
+ _PeriodicReportIntervalDescriptor
+ _ServiceLevelDescriptor
+ _StorageDurationDescriptor
+ _UpdateMagnitudeDescriptor
+ __OBJC_$_CLASS_METHODS_RTPeopleDensityCallbackConfiguration
+ __OBJC_$_CLASS_METHODS_RTPeopleDiscoveryServiceConfiguration
+ __OBJC_$_CLASS_PROP_LIST_RTPeopleDensityCallbackConfiguration
+ __OBJC_$_CLASS_PROP_LIST_RTPeopleDiscoveryServiceConfiguration
+ __OBJC_$_INSTANCE_METHODS_RTPeopleDensityCallbackConfiguration
+ __OBJC_$_INSTANCE_METHODS_RTPeopleDiscoveryServiceConfiguration
+ __OBJC_$_INSTANCE_METHODS_RTRoutineManagerRegistrantPeopleDiscovery
+ __OBJC_$_INSTANCE_VARIABLES_RTPeopleDensityCallbackConfiguration
+ __OBJC_$_INSTANCE_VARIABLES_RTPeopleDiscoveryServiceConfiguration
+ __OBJC_$_INSTANCE_VARIABLES_RTRoutineManagerRegistrantPeopleDiscovery
+ __OBJC_$_PROP_LIST_RTPeopleDensityCallbackConfiguration
+ __OBJC_$_PROP_LIST_RTPeopleDiscoveryServiceConfiguration
+ __OBJC_$_PROP_LIST_RTRoutineManagerRegistrantPeopleDiscovery
+ __OBJC_CLASS_PROTOCOLS_$_RTPeopleDensityCallbackConfiguration
+ __OBJC_CLASS_PROTOCOLS_$_RTPeopleDiscoveryServiceConfiguration
+ __OBJC_CLASS_RO_$_RTPeopleDensityCallbackConfiguration
+ __OBJC_CLASS_RO_$_RTPeopleDiscoveryServiceConfiguration
+ __OBJC_CLASS_RO_$_RTRoutineManagerRegistrantPeopleDiscovery
+ __OBJC_METACLASS_RO_$_RTPeopleDensityCallbackConfiguration
+ __OBJC_METACLASS_RO_$_RTPeopleDiscoveryServiceConfiguration
+ __OBJC_METACLASS_RO_$_RTRoutineManagerRegistrantPeopleDiscovery
+ ___37-[RTRoutineManager _createConnection]_block_invoke.353
+ ___38-[RTRoutineManager stopLeechingVisits]_block_invoke.403
+ ___40-[RTRoutineManager stopMonitoringVisits]_block_invoke.402
+ ___42-[RTRoutineManager addElevations:handler:]_block_invoke.471
+ ___46-[RTRoutineManager fetchCurrentPeopleDensity:]_block_invoke
+ ___46-[RTRoutineManager fetchCurrentPeopleDensity:]_block_invoke_2
+ ___46-[RTRoutineManager fetchCurrentPeopleDensity:]_block_invoke_3
+ ___49-[RTRoutineManager fetchRoutineStateWithHandler:]_block_invoke.379
+ ___51-[RTRoutineManager fetchRoutineEnabledWithHandler:]_block_invoke.376
+ ___51-[RTRoutineManager fetchRoutineEnabledWithHandler:]_block_invoke_2.378
+ ___51-[RTRoutineManager stopLeechingLowConfidenceVisits]_block_invoke.404
+ ___53-[RTRoutineManager clearAllVehicleEventsWithHandler:]_block_invoke.433
+ ___53-[RTRoutineManager fetchElevationsWithOptions:reply:]_block_invoke.472
+ ___56-[RTRoutineManager stopMonitoringScenarioTriggerOfType:]_block_invoke.408
+ ___59-[RTRoutineManager enumerateObjectsWithOptions:usingBlock:]_block_invoke.391
+ ___62-[RTRoutineManager startMonitoringForPeopleDiscovery:handler:]_block_invoke
+ ___62-[RTRoutineManager startMonitoringForPeopleDiscovery:handler:]_block_invoke.462
+ ___62-[RTRoutineManager startMonitoringForPeopleDiscovery:handler:]_block_invoke_2
+ ___64-[RTRoutineManager stopMonitoringForPeopleDiscoveryWithHandler:]_block_invoke
+ ___64-[RTRoutineManager stopMonitoringForPeopleDiscoveryWithHandler:]_block_invoke.463
+ ___64-[RTRoutineManager stopMonitoringForPeopleDiscoveryWithHandler:]_block_invoke.464
+ ___68-[RTRoutineManager _enumerateStoredLocationsWithOptions:usingBlock:]_block_invoke.399
+ ___68-[RTRoutineManager _enumerateStoredLocationsWithOptions:usingBlock:]_block_invoke.400
+ ___68-[RTRoutineManager fetchPeopleCountEventsHistory:completionHandler:]_block_invoke.468
+ ___71-[RTRoutineManager fetchContactScoresFromContactIDs:completionHandler:]_block_invoke.470
+ ___72-[RTRoutineManager fetchProximityHistoryFromEventIDs:completionHandler:]_block_invoke.467
+ ___81-[RTRoutineManager fetchProximityHistoryFromStartDate:endDate:completionHandler:]_block_invoke.466
+ ___85-[RTRoutineManager fetchPeopleDensityHistoryFromStartDate:endDate:completionHandler:]_block_invoke.469
+ ___block_descriptor_40_e8_32bs_e37_v24?0"RTPeopleDensity"8"NSError"16ls32l8
+ ___block_descriptor_64_e8_32s40s48bs_e5_v8?0ls32l8s40l8s48l8
+ ___block_literal_global.407
+ ___block_literal_global.410
+ ___block_literal_global.435
+ ___block_literal_global.437
+ ___block_literal_global.439
+ ___block_literal_global.441
+ ___block_literal_global.443
+ ___block_literal_global.445
+ ___block_literal_global.447
+ ___block_literal_global.449
+ ___block_literal_global.451
+ ___block_literal_global.453
+ ___block_literal_global.455
+ ___block_literal_global.457
+ ___block_literal_global.459
+ ___block_literal_global.461
+ ___block_literal_global.665
+ _objc_msgSend$configuration
+ _objc_msgSend$configurationIdentifier
+ _objc_msgSend$densityCallbackConfiguration
+ _objc_msgSend$densityUpdateHandler
+ _objc_msgSend$fetchOngoingPeopleDensity:
+ _objc_msgSend$initWithConfigurationIdentifier:
+ _objc_msgSend$initWithPeriodicReportInterval:magnitude:densityUpdateHandler:
+ _objc_msgSend$initWithServiceLevel:storageDuration:observationInterval:densityCallbackConfiguration:
+ _objc_msgSend$magnitude
+ _objc_msgSend$observationInterval
+ _objc_msgSend$onDensityUpdate:error:
+ _objc_msgSend$peopleDiscoveryErrorHandler
+ _objc_msgSend$periodicReportInterval
+ _objc_msgSend$serviceLevel
+ _objc_msgSend$setPeopleDiscoveryErrorHandler:
+ _objc_msgSend$startMonitoringForPeopleDiscovery:
+ _objc_msgSend$startMonitoringForPeopleDiscovery:configuration:reply:
+ _objc_msgSend$startMonitoringForPeopleDiscovery:handler:
+ _objc_msgSend$stopMonitoringForPeopleDiscovery
+ _objc_msgSend$stopMonitoringForPeopleDiscoveryWithReply:
+ _objc_msgSend$storageDuration
- GCC_except_table91
- GCC_except_table99
- ___37-[RTRoutineManager _createConnection]_block_invoke.342
- ___38-[RTRoutineManager stopLeechingVisits]_block_invoke.392
- ___40-[RTRoutineManager stopMonitoringVisits]_block_invoke.391
- ___42-[RTRoutineManager addElevations:handler:]_block_invoke.456
- ___49-[RTRoutineManager fetchRoutineStateWithHandler:]_block_invoke.368
- ___51-[RTRoutineManager fetchRoutineEnabledWithHandler:]_block_invoke.365
- ___51-[RTRoutineManager fetchRoutineEnabledWithHandler:]_block_invoke_2.367
- ___51-[RTRoutineManager stopLeechingLowConfidenceVisits]_block_invoke.393
- ___53-[RTRoutineManager clearAllVehicleEventsWithHandler:]_block_invoke.422
- ___53-[RTRoutineManager fetchElevationsWithOptions:reply:]_block_invoke.457
- ___56-[RTRoutineManager stopMonitoringScenarioTriggerOfType:]_block_invoke.397
- ___59-[RTRoutineManager enumerateObjectsWithOptions:usingBlock:]_block_invoke.380
- ___68-[RTRoutineManager _enumerateStoredLocationsWithOptions:usingBlock:]_block_invoke.388
- ___68-[RTRoutineManager _enumerateStoredLocationsWithOptions:usingBlock:]_block_invoke.389
- ___68-[RTRoutineManager fetchPeopleCountEventsHistory:completionHandler:]_block_invoke.453
- ___71-[RTRoutineManager fetchContactScoresFromContactIDs:completionHandler:]_block_invoke.455
- ___72-[RTRoutineManager fetchProximityHistoryFromEventIDs:completionHandler:]_block_invoke.452
- ___81-[RTRoutineManager fetchProximityHistoryFromStartDate:endDate:completionHandler:]_block_invoke.451
- ___85-[RTRoutineManager fetchPeopleDensityHistoryFromStartDate:endDate:completionHandler:]_block_invoke.454
- ___block_literal_global.396
- ___block_literal_global.399
- ___block_literal_global.424
- ___block_literal_global.426
- ___block_literal_global.428
- ___block_literal_global.430
- ___block_literal_global.432
- ___block_literal_global.434
- ___block_literal_global.436
- ___block_literal_global.438
- ___block_literal_global.440
- ___block_literal_global.442
- ___block_literal_global.444
- ___block_literal_global.446
- ___block_literal_global.448
- ___block_literal_global.450
- ___block_literal_global.636
CStrings:
+ "\x1d"
+ "%@, registered, %@, monitoredConfig, %@, densityBundles count, %lu, error, %@"
+ "-[RTRoutineManager fetchCurrentPeopleDensity:]"
+ "-[RTRoutineManager startMonitoringForPeopleDiscovery:handler:]"
+ "-[RTRoutineManager stopMonitoringForPeopleDiscoveryWithHandler:]"
+ "1"
+ "15Min"
+ "1Day"
+ "1Hour"
+ "4Weeks"
+ "5Min"
+ "@\"RTPeopleDensityCallbackConfiguration\""
+ "@\"RTPeopleDiscoveryServiceConfiguration\""
+ "@\"RTRoutineManagerRegistrantPeopleDiscovery\""
+ "@40@0:8Q16Q24@?32"
+ "@48@0:8Q16Q24Q32@40"
+ "Best"
+ "DensityCallbackConfig"
+ "Encountered error while starting monitoring for people discovery service, error, %@"
+ "Encountered error while stopping monitoring for people discovery service, error, %@"
+ "Good"
+ "Invalid configuration to register for people discovery service.  Requires non-nil value."
+ "Invalid parameter not satisfying: completionHandler (in %s:%d)"
+ "Invalid parameter not satisfying: configuration (in %s:%d)"
+ "Invalid parameter value for density update handler.  Requires non-nil value."
+ "Large"
+ "Long"
+ "ObservationInterval"
+ "RTPeopleDensityCallbackConfiguration"
+ "RTPeopleDiscoveryServiceConfiguration"
+ "RTRoutineManagerRegistrantPeopleDiscovery"
+ "ServiceLevel"
+ "Short"
+ "Small"
+ "StorageDuration"
+ "T@\"NSString\",R,N,V_configurationIdentifier"
+ "T@\"RTPeopleDensityCallbackConfiguration\",R,N,V_densityCallbackConfiguration"
+ "T@\"RTPeopleDiscoveryServiceConfiguration\",R,N,V_configuration"
+ "T@\"RTRoutineManagerRegistrantPeopleDiscovery\",&,N,V_peopleDiscoveryRegistrant"
+ "T@?,C,N,V_peopleDiscoveryErrorHandler"
+ "T@?,R,N,V_densityUpdateHandler"
+ "TQ,R,N,V_magnitude"
+ "TQ,R,N,V_observationInterval"
+ "TQ,R,N,V_periodicReportInterval"
+ "TQ,R,N,V_serviceLevel"
+ "TQ,R,N,V_storageDuration"
+ "_configuration"
+ "_configurationIdentifier"
+ "_densityCallbackConfiguration"
+ "_densityHandler"
+ "_densityUpdateHandler"
+ "_magnitude"
+ "_observationInterval"
+ "_peopleDiscoveryErrorHandler"
+ "_peopleDiscoveryRegistrant"
+ "_periodicReportInterval"
+ "_serviceLevel"
+ "_storageDuration"
+ "configuration"
+ "configurationIdentifier"
+ "densityCallbackConfiguration"
+ "densityUpdateHandler"
+ "fetchCurrentPeopleDensity:"
+ "fetchOngoingPeopleDensity:"
+ "initWithConfigurationIdentifier:"
+ "initWithPeriodicReportInterval:magnitude:densityUpdateHandler:"
+ "initWithServiceLevel:storageDuration:observationInterval:densityCallbackConfiguration:"
+ "interval"
+ "magnitude"
+ "observationInterval"
+ "onDensityUpdate:error:"
+ "peopleDiscoveryErrorHandler"
+ "peopleDiscoveryRegistrant"
+ "periodicReportInterval"
+ "rdar122420473 _peopleDiscoveryRegistrant %@"
+ "rdar122420473 creating _peopleDiscoveryRegistrant initWithConfigurationIdentifier %@"
+ "serviceLevel"
+ "setPeopleDiscoveryErrorHandler:"
+ "setPeopleDiscoveryRegistrant:"
+ "startMonitoringForPeopleDiscovery:"
+ "startMonitoringForPeopleDiscovery:configuration:reply:"
+ "startMonitoringForPeopleDiscovery:handler:"
+ "stopMonitoringForPeopleDiscovery"
+ "stopMonitoringForPeopleDiscoveryWithHandler:"
+ "stopMonitoringForPeopleDiscoveryWithReply:"
+ "storageDuration"
+ "v24@0:8@?<v@?@\"RTPeopleDensity\"@\"NSError\">16"
+ "v24@?0@\"RTPeopleDensity\"8@\"NSError\"16"
+ "v40@0:8@\"NSString\"16@\"RTPeopleDiscoveryServiceConfiguration\"24@?<v@?@\"NSError\">32"
- "\x1b"

```
