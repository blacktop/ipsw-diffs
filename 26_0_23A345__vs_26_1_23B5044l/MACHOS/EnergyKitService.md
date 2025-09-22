## EnergyKitService

> `/System/Library/PrivateFrameworks/EnergyKitInternal.framework/XPCServices/EnergyKitService.xpc/EnergyKitService`

```diff

-356.1.3.1.1
-  __TEXT.__text: 0x736ec
-  __TEXT.__auth_stubs: 0x2200
-  __TEXT.__objc_methlist: 0x9d8
-  __TEXT.__cstring: 0x19fd
-  __TEXT.__objc_methname: 0x1ddc
-  __TEXT.__oslogstring: 0x1806
+375.0.0.0.0
+  __TEXT.__text: 0x9804c
+  __TEXT.__auth_stubs: 0x2530
+  __TEXT.__objc_methlist: 0xb80
+  __TEXT.__cstring: 0x21b2
+  __TEXT.__objc_methname: 0x1e44
+  __TEXT.__oslogstring: 0x1f16
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__const: 0x1128
-  __TEXT.__constg_swiftt: 0xaf8
-  __TEXT.__swift5_types: 0x78
-  __TEXT.__swift5_typeref: 0x7cb
-  __TEXT.__swift_as_entry: 0x1a8
-  __TEXT.__swift5_reflstr: 0x4a2
-  __TEXT.__swift5_fieldmd: 0x51c
-  __TEXT.__swift5_proto: 0x44
-  __TEXT.__swift5_capture: 0x9c8
+  __TEXT.__const: 0x1448
+  __TEXT.__constg_swiftt: 0xd74
+  __TEXT.__swift5_types: 0x90
+  __TEXT.__swift5_typeref: 0xa05
+  __TEXT.__swift_as_entry: 0x220
+  __TEXT.__swift5_reflstr: 0x562
+  __TEXT.__swift5_fieldmd: 0x684
+  __TEXT.__swift5_proto: 0x4c
+  __TEXT.__swift5_capture: 0xd4c
   __TEXT.__objc_classname: 0x89
   __TEXT.__objc_methtype: 0x695
-  __TEXT.__swift_as_ret: 0x2d8
+  __TEXT.__swift_as_ret: 0x37c
   __TEXT.__swift5_assocty: 0x18
-  __TEXT.__unwind_info: 0x1ce8
-  __TEXT.__eh_frame: 0x6018
-  __DATA_CONST.__auth_got: 0x1100
-  __DATA_CONST.__got: 0x5a8
-  __DATA_CONST.__auth_ptr: 0x2e0
-  __DATA_CONST.__const: 0x1a40
-  __DATA_CONST.__objc_classlist: 0xd8
+  __TEXT.__unwind_info: 0x23a8
+  __TEXT.__eh_frame: 0x7620
+  __DATA_CONST.__auth_got: 0x1298
+  __DATA_CONST.__got: 0x638
+  __DATA_CONST.__auth_ptr: 0x328
+  __DATA_CONST.__const: 0x28f0
+  __DATA_CONST.__objc_classlist: 0xf8
   __DATA_CONST.__objc_protolist: 0x90
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x58
-  __DATA.__objc_const: 0x2310
-  __DATA.__objc_selrefs: 0x838
-  __DATA.__objc_data: 0x368
-  __DATA.__data: 0x1bb8
-  __DATA.__common: 0xe8
-  __DATA.__bss: 0x880
+  __DATA.__objc_const: 0x2708
+  __DATA.__objc_selrefs: 0x8b0
+  __DATA.__objc_data: 0x570
+  __DATA.__data: 0x2050
+  __DATA.__common: 0x120
+  __DATA.__bss: 0x980
   - /System/Library/Frameworks/CoreData.framework/CoreData
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreLocation.framework/CoreLocation

   - /System/Library/PrivateFrameworks/HomeServices.framework/HomeServices
   - /System/Library/PrivateFrameworks/HomeUtilityServices.framework/HomeUtilityServices
   - /System/Library/PrivateFrameworks/InternalSwiftProtobuf.framework/InternalSwiftProtobuf
+  - /System/Library/PrivateFrameworks/TCC.framework/TCC
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 151B6E64-BAED-3DF5-BC5A-35466A0A024D
-  Functions: 1361
-  Symbols:   195
-  CStrings:  622
+  UUID: F6DD4A38-7A96-36B5-864C-027B10D0A383
+  Functions: 1850
+  Symbols:   202
+  CStrings:  708
 
Symbols:
+ _TCCAccessCheckAuditToken
+ _kTCCServiceEnergyKitGuidance
+ _pow
+ _swift_bridgeObjectRelease_n
+ _swift_cvw_initStructMetadataWithLayoutString
+ _swift_cvw_initWithTake
+ _swift_getEnumTagSinglePayloadGeneric
+ _swift_storeEnumTagSinglePayloadGeneric
- _swift_bridgeObjectRetain_n
CStrings:
+ "/System/Library/PrivateFrameworks/HomeKitDaemon.framework"
+ "EnergyKitService.TCCValidatingProxy"
+ "Failed to decode data"
+ "Failed to fetch latest hist guidance entry for %{private}s"
+ "Failed to refresh historical guidance: %@"
+ "[AuditTokenValidator] Failed to extract audit token"
+ "[AuditTokenValidator] No XPC connection provided"
+ "[AuditTokenValidator] TCC access denied for connection"
+ "[AuditTokenValidator] TCC access validated for connection"
+ "[EKSHomeManagerActor] Setting up location services"
+ "[EKSHomeManager] Location services authorized for HomeKit"
+ "[EKSHomeManager] Location services not authorized for HomeKit"
+ "[EKSHomeManager] Location services not determined. Authorizing"
+ "[LoadEventsQueryEngine] Core Data error detected, stopping processing"
+ "[LoadEventsQueryEngine] Error detected %@"
+ "[LoadEventsQueryEngine] Error processing rack %s: %@"
+ "[LoadEventsQueryEngine] Final yield of %ld records"
+ "[LoadEventsQueryEngine] Next rack: %s"
+ "[LoadEventsQueryEngine] No %s digest data found for query range"
+ "[LoadEventsQueryEngine] No hourly blocks found for query range"
+ "[LoadEventsQueryEngine] Processing complete. Total records: %ld"
+ "[LoadEventsQueryEngine] Query Range: %s"
+ "[LoadEventsQueryEngine] Yielding %ld records"
+ "[SiteOperations] Found confident gridID based on decay scores: %s"
+ "[SiteOperations] Using confident gridID from decay scores: %s"
+ "[TCC-Delegate] Accepted connection from PID: %d with universal TCC proxy"
+ "[TCC-Delegate] Connection interrupted for PID: %d"
+ "[TCC-Delegate] Connection invalidated for PID: %d"
+ "[TCC-Delegate] Connection rejected - PID %d missing entitlements"
+ "[TCC-Delegate] New connection from PID: %d"
+ "[TCC-Proxy] Method '%s' BLOCKED - audit token TCC validation failed"
+ "[TCC-Proxy] Method '%s' authorized - forwarding"
+ "[TCC-Proxy] Method '%s' is TCC-exempt - forwarding"
+ "[VenueOperations] No XPC connection available for TCC validation"
+ "_TtC16EnergyKitService14DeviceInsights"
+ "_TtC16EnergyKitService19AuditTokenValidator"
+ "_TtC16EnergyKitService21LoadEventsQueryEngine"
+ "_TtC16EnergyKitServiceP33_2D2DC1C7D933FC71CE72A1C07FFB3AED18TCCValidatingProxy"
+ "appID"
+ "batchedDeviceInsights"
+ "batchedDeviceInsightsWithRequest:endpoint:ekSandboxExtension:completion:"
+ "batchedWholeHomeInsights"
+ "batchedWholeHomeInsightsWithRequest:endpoint:ekSandboxExtension:wholeHomeOptimization:completion:"
+ "blockData"
+ "blockEnd"
+ "blockStart"
+ "code"
+ "configureCostInclusionForGuidance"
+ "configureCostInclusionForGuidanceWithIsIncluded:for:reply:"
+ "connection"
+ "decoder"
+ "deleteGridIDAppTracking"
+ "deleteGridIDAppTrackingFor:reply:"
+ "deviceID"
+ "digestConsumptionData"
+ "digestProductionData"
+ "electricityGuidance(query:)"
+ "electricityGuidance(venue:)"
+ "electricityGuidanceWithQuery:gridID:reply:"
+ "electricityGuidanceWithVenue:query:gridID:reply:"
+ "endDate"
+ "energyVenue(for:)"
+ "energyVenue(homeID:)"
+ "energyVenueFor:reply:"
+ "energyVenueWithHomeID:reply:"
+ "energyVenuesWithReply:"
+ "exemptMethods"
+ "gridID(location:)"
+ "gridID(location:async)"
+ "gridIDWithLocation:sandboxExtension:reply:"
+ "gridIDWithVenue:sandboxExtension:reply:"
+ "guidance(query:)"
+ "hasAnyHomesWithReply:"
+ "intervalEnd"
+ "isCostInclusionConfiguredForGuidance"
+ "isCostInclusionConfiguredForGuidanceFor:reply:"
+ "lastUpdated"
+ "loadType"
+ "processIdentifier"
+ "setLastUpdated:"
+ "setUpSandboxWithSandboxExtension:reply:"
+ "siteIdentifier = %@ AND sourceIdentifier = %@ AND deviceIdentifier = %@ AND blockStart >= %@ AND blockEnd <= %@ AND isConsumptionBlock = %@"
+ "siteIdentifier = %@ AND sourceIdentifier = %@ AND deviceIdentifier = %@ AND startDate >= %@ AND endDate <= %@"
+ "startDate"
+ "submitLoadEvents"
+ "submitLoadEventsWithEvents:sandboxExtension:reply:"
+ "target"
+ "v12@?0B8"
+ "v16@?0@\"NSArray\"8"
+ "v16@?0@\"NSDictionary\"8"
+ "v16@?0@\"NSString\"8"
+ "v16@?0q8"
+ "v20@?0B8@\"NSError\"12"
+ "v24@0:8@?<v@?@\"_TtC9EnergyKit24XPCEnergyVenuesContainer\"@\"NSError\">16"
+ "v24@0:8@?<v@?B>16"
+ "v24@?0@\"NSString\"8@\"NSError\"16"
+ "v24@?0@\"_TtC17EnergyKitInternal20XPCGuidanceContainer\"8@\"NSError\"16"
+ "v24@?0@\"_TtC19EnergyKitFoundation12EKEnergySite\"8@\"NSError\"16"
+ "v24@?0@\"_TtC9EnergyKit23XPCEnergyVenueContainer\"8@\"NSError\"16"
+ "v24@?0@\"_TtC9EnergyKit24XPCEnergyVenuesContainer\"8@\"NSError\"16"
+ "v24@?0@\"_TtC9EnergyKit31XPCElectricityGuidanceContainer\"8@\"NSError\"16"
+ "v24@?0q8@\"NSError\"16"
+ "v32@0:8@\"NSUUID\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@\"NSUUID\"16@?<v@?@\"_TtC9EnergyKit23XPCEnergyVenueContainer\"@\"NSError\">24"
+ "v32@0:8@\"NSUUID\"16@?<v@?B@\"NSError\">24"
+ "v36@0:8B16@\"NSUUID\"20@?<v@?@\"NSError\">28"
+ "v40@0:8@\"CLLocation\"16@\"_TtC9EnergyKit28XPCSandboxExtensionContainer\"24@?<v@?@\"NSString\"@\"NSError\">32"
+ "v40@0:8@\"NSUUID\"16@\"_TtC9EnergyKit28XPCSandboxExtensionContainer\"24@?<v@?@\"NSString\"@\"NSError\">32"
+ "v40@0:8@\"_TtC9EnergyKit31XPCElectricalLoadEventContainer\"16@\"_TtC9EnergyKit28XPCSandboxExtensionContainer\"24@?<v@?q@\"NSError\">32"
+ "v48@0:8@\"_TtC9EnergyKit19InsightQueryRequest\"16@\"NSXPCListenerEndpoint\"24@\"_TtC9EnergyKit28XPCSandboxExtensionContainer\"32@?<v@?>40"
+ "validateTCCAccess"
+ "validateTCCAccessWithReply:"
- "Listener connection interrupted"
- "Listener connection invalidated"
- "[SiteOperations] Found majority gridID with count %ld: %s"
- "[SiteOperations] Found majority gridID with count > 20: %s"
- "batchedInsightsWithRequest:endpoint:ekSandboxExtension:wholeHomeOptimization:completion:"
- "configureCostInclusionForGuidanceWithIsIncluded:for:completionHandler:"
- "deleteGridIDAppTrackingFor:completionHandler:"
- "electricityGuidanceWithQuery:gridID:completionHandler:"
- "electricityGuidanceWithVenue:query:gridID:completionHandler:"
- "energyVenueFor:completionHandler:"
- "energyVenueWithHomeID:completionHandler:"
- "energyVenuesWithCompletionHandler:"
- "energyVenuesWithNear:radius:completionHandler:"
- "gridIDWithLocation:sandboxExtension:completionHandler:"
- "gridIDWithVenue:sandboxExtension:completionHandler:"
- "isCostInclusionConfiguredForGuidanceFor:completionHandler:"
- "setUpSandboxWithSandboxExtension:completionHandler:"
- "submitLoadEventsWithEvents:sandboxExtension:completionHandler:"
- "v24@0:8@?<v@?@\"_TtC9EnergyKit24XPCEnergyVenuesContainer\">16"
- "v32@0:8@\"NSUUID\"16@?<v@?>24"
- "v32@0:8@\"NSUUID\"16@?<v@?@\"_TtC9EnergyKit23XPCEnergyVenueContainer\">24"
- "v32@0:8@\"NSUUID\"16@?<v@?B>24"
- "v36@0:8B16@\"NSUUID\"20@?<v@?>28"
- "v40@0:8@\"CLLocation\"16@\"_TtC9EnergyKit28XPCSandboxExtensionContainer\"24@?<v@?@\"NSString\">32"
- "v40@0:8@\"CLLocation\"16d24@?<v@?@\"_TtC9EnergyKit24XPCEnergyVenuesContainer\">32"
- "v40@0:8@\"NSUUID\"16@\"_TtC9EnergyKit28XPCSandboxExtensionContainer\"24@?<v@?@\"NSString\">32"
- "v40@0:8@\"_TtC9EnergyKit31XPCElectricalLoadEventContainer\"16@\"_TtC9EnergyKit28XPCSandboxExtensionContainer\"24@?<v@?q>32"

```
