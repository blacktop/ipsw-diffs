## SafetyAlerts

> `/System/Library/PrivateFrameworks/SafetyAlerts.framework/SafetyAlerts`

```diff

-67.0.4.0.0
-  __TEXT.__text: 0x8200
-  __TEXT.__auth_stubs: 0x500
-  __TEXT.__objc_methlist: 0x3d4
-  __TEXT.__const: 0xa0
-  __TEXT.__gcc_except_tab: 0xcf0
-  __TEXT.__cstring: 0xd15
-  __TEXT.__oslogstring: 0x24e3
-  __TEXT.__unwind_info: 0x3f0
-  __TEXT.__objc_classname: 0x26
-  __TEXT.__objc_methname: 0xdea
-  __TEXT.__objc_methtype: 0x108
-  __TEXT.__objc_stubs: 0xb20
-  __DATA_CONST.__got: 0xa8
-  __DATA_CONST.__const: 0x220
-  __DATA_CONST.__objc_classlist: 0x10
+70.0.15.0.0
+  __TEXT.__text: 0xb900
+  __TEXT.__objc_methlist: 0x6fc
+  __TEXT.__const: 0xa8
+  __TEXT.__gcc_except_tab: 0x11cc
+  __TEXT.__cstring: 0xf54
+  __TEXT.__oslogstring: 0x2f6c
+  __TEXT.__unwind_info: 0x540
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x248
+  __DATA_CONST.__objc_classlist: 0x30
+  __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3d8
-  __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0x290
-  __AUTH_CONST.__const: 0x40
-  __AUTH_CONST.__cfstring: 0x9e0
-  __AUTH_CONST.__objc_const: 0x368
-  __DATA.__objc_ivar: 0x30
-  __DATA.__data: 0x88
+  __DATA_CONST.__objc_selrefs: 0x5a0
+  __DATA_CONST.__objc_superrefs: 0x30
+  __DATA_CONST.__got: 0xe8
+  __AUTH_CONST.__const: 0xc0
+  __AUTH_CONST.__cfstring: 0xe80
+  __AUTH_CONST.__objc_const: 0xb68
+  __AUTH_CONST.__auth_got: 0x0
+  __AUTH.__objc_data: 0x140
+  __DATA.__objc_ivar: 0x8c
+  __DATA.__data: 0x1a8
   __DATA_DIRTY.__objc_data: 0xa0
-  __DATA_DIRTY.__common: 0x28
-  __DATA_DIRTY.__bss: 0x30
+  __DATA_DIRTY.__common: 0x20
+  __DATA_DIRTY.__bss: 0x70
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreTelephony.framework/CoreTelephony
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libTelephonyUtilDynamic.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 4F9092FB-F438-39D8-9F2C-CEFAF88A4378
-  Functions: 109
-  Symbols:   547
-  CStrings:  465
+  UUID: 741E406D-B007-3B4C-8A1C-FA46E47CFEE2
+  Functions: 168
+  Symbols:   837
+  CStrings:  402
 
Symbols:
+ +[SACircularGeofence supportsSecureCoding]
+ +[SAGeoAlertData supportsSecureCoding]
+ +[SAGeoAlertData(SafetyAlerts) createFromMergedDict:]
+ +[SAGeoAlertData(SafetyAlerts) parseCircularGeofencesFromArray:]
+ +[SAGeoAlertData(SafetyAlerts) parsePolygonalGeofencesFromArray:]
+ +[SAGeofenceCoordinate supportsSecureCoding]
+ +[SAPolygonalGeofence supportsSecureCoding]
+ +[SafetyAlerts isSupportedPlatform]
+ -[SACircularGeofence .cxx_destruct]
+ -[SACircularGeofence center]
+ -[SACircularGeofence copyWithZone:]
+ -[SACircularGeofence encodeWithCoder:]
+ -[SACircularGeofence identifier]
+ -[SACircularGeofence initWithCoder:]
+ -[SACircularGeofence initWithIdentifier:center:radius:]
+ -[SACircularGeofence radius]
+ -[SAGeoAlertData .cxx_destruct]
+ -[SAGeoAlertData alertHash]
+ -[SAGeoAlertData alertType]
+ -[SAGeoAlertData circularGeofences]
+ -[SAGeoAlertData copyWithZone:]
+ -[SAGeoAlertData deliveryTime]
+ -[SAGeoAlertData displayTime]
+ -[SAGeoAlertData displayed]
+ -[SAGeoAlertData encodeWithCoder:]
+ -[SAGeoAlertData epicenterCoordinate]
+ -[SAGeoAlertData initWithAlertHash:title:message:instructionMessage:language:safetyCategory:safetyEvent:safetyCategoryEnums:safetyEventEnums:deliveryTime:displayTime:displayed:polygonalGeofences:circularGeofences:epicenterCoordinate:alertType:]
+ -[SAGeoAlertData initWithCoder:]
+ -[SAGeoAlertData instructionMessage]
+ -[SAGeoAlertData language]
+ -[SAGeoAlertData message]
+ -[SAGeoAlertData polygonalGeofences]
+ -[SAGeoAlertData safetyCategoryEnums]
+ -[SAGeoAlertData safetyCategory]
+ -[SAGeoAlertData safetyEventEnums]
+ -[SAGeoAlertData safetyEvent]
+ -[SAGeoAlertData title]
+ -[SAGeofenceCoordinate copyWithZone:]
+ -[SAGeofenceCoordinate encodeWithCoder:]
+ -[SAGeofenceCoordinate initWithCoder:]
+ -[SAGeofenceCoordinate initWithLatitude:longitude:]
+ -[SAGeofenceCoordinate latitude]
+ -[SAGeofenceCoordinate longitude]
+ -[SAPolygonalGeofence .cxx_destruct]
+ -[SAPolygonalGeofence coordinates]
+ -[SAPolygonalGeofence copyWithZone:]
+ -[SAPolygonalGeofence encodeWithCoder:]
+ -[SAPolygonalGeofence identifier]
+ -[SAPolygonalGeofence initWithCoder:]
+ -[SAPolygonalGeofence initWithIdentifier:coordinates:]
+ -[SafetyAlerts getGeoAlertData:outError:]
+ -[SafetyAlerts parseGeoAlertDataFromReply:outError:]
+ -[SafetyAlerts(GeoAlerts) getGeoAlert:completion:]
+ -[SafetyAlerts(GeoAlerts) getGeoAlert:outError:]
+ GCC_except_table1
+ GCC_except_table19
+ GCC_except_table31
+ GCC_except_table46
+ GCC_except_table48
+ _OBJC_CLASS_$_NSMutableArray
+ _OBJC_CLASS_$_NSSet
+ _OBJC_CLASS_$_SACircularGeofence
+ _OBJC_CLASS_$_SAGeoAlertData
+ _OBJC_CLASS_$_SAGeofenceCoordinate
+ _OBJC_CLASS_$_SAPolygonalGeofence
+ _OBJC_IVAR_$_SACircularGeofence._center
+ _OBJC_IVAR_$_SACircularGeofence._identifier
+ _OBJC_IVAR_$_SACircularGeofence._radius
+ _OBJC_IVAR_$_SAGeoAlertData._alertHash
+ _OBJC_IVAR_$_SAGeoAlertData._alertType
+ _OBJC_IVAR_$_SAGeoAlertData._circularGeofences
+ _OBJC_IVAR_$_SAGeoAlertData._deliveryTime
+ _OBJC_IVAR_$_SAGeoAlertData._displayTime
+ _OBJC_IVAR_$_SAGeoAlertData._displayed
+ _OBJC_IVAR_$_SAGeoAlertData._epicenterCoordinate
+ _OBJC_IVAR_$_SAGeoAlertData._instructionMessage
+ _OBJC_IVAR_$_SAGeoAlertData._language
+ _OBJC_IVAR_$_SAGeoAlertData._message
+ _OBJC_IVAR_$_SAGeoAlertData._polygonalGeofences
+ _OBJC_IVAR_$_SAGeoAlertData._safetyCategory
+ _OBJC_IVAR_$_SAGeoAlertData._safetyCategoryEnums
+ _OBJC_IVAR_$_SAGeoAlertData._safetyEvent
+ _OBJC_IVAR_$_SAGeoAlertData._safetyEventEnums
+ _OBJC_IVAR_$_SAGeoAlertData._title
+ _OBJC_IVAR_$_SAGeofenceCoordinate._latitude
+ _OBJC_IVAR_$_SAGeofenceCoordinate._longitude
+ _OBJC_IVAR_$_SAPolygonalGeofence._coordinates
+ _OBJC_IVAR_$_SAPolygonalGeofence._identifier
+ _OBJC_METACLASS_$_SACircularGeofence
+ _OBJC_METACLASS_$_SAGeoAlertData
+ _OBJC_METACLASS_$_SAGeofenceCoordinate
+ _OBJC_METACLASS_$_SAPolygonalGeofence
+ __OBJC_$_CLASS_METHODS_SACircularGeofence
+ __OBJC_$_CLASS_METHODS_SAGeoAlertData(SafetyAlerts)
+ __OBJC_$_CLASS_METHODS_SAGeofenceCoordinate
+ __OBJC_$_CLASS_METHODS_SAPolygonalGeofence
+ __OBJC_$_CLASS_PROP_LIST_NSSecureCoding
+ __OBJC_$_CLASS_PROP_LIST_SACircularGeofence
+ __OBJC_$_CLASS_PROP_LIST_SAGeoAlertData
+ __OBJC_$_CLASS_PROP_LIST_SAGeofenceCoordinate
+ __OBJC_$_CLASS_PROP_LIST_SAPolygonalGeofence
+ __OBJC_$_INSTANCE_METHODS_SACircularGeofence
+ __OBJC_$_INSTANCE_METHODS_SAGeoAlertData
+ __OBJC_$_INSTANCE_METHODS_SAGeofenceCoordinate
+ __OBJC_$_INSTANCE_METHODS_SAPolygonalGeofence
+ __OBJC_$_INSTANCE_METHODS_SafetyAlerts(GeoAlerts)
+ __OBJC_$_INSTANCE_VARIABLES_SACircularGeofence
+ __OBJC_$_INSTANCE_VARIABLES_SAGeoAlertData
+ __OBJC_$_INSTANCE_VARIABLES_SAGeofenceCoordinate
+ __OBJC_$_INSTANCE_VARIABLES_SAPolygonalGeofence
+ __OBJC_$_PROP_LIST_SACircularGeofence
+ __OBJC_$_PROP_LIST_SAGeoAlertData
+ __OBJC_$_PROP_LIST_SAGeofenceCoordinate
+ __OBJC_$_PROP_LIST_SAPolygonalGeofence
+ __OBJC_$_PROTOCOL_CLASS_METHODS_NSSecureCoding
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCoding
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCopying
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSCoding
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSCopying
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSSecureCoding
+ __OBJC_$_PROTOCOL_REFS_NSSecureCoding
+ __OBJC_CLASS_PROTOCOLS_$_SACircularGeofence
+ __OBJC_CLASS_PROTOCOLS_$_SAGeoAlertData
+ __OBJC_CLASS_PROTOCOLS_$_SAGeofenceCoordinate
+ __OBJC_CLASS_PROTOCOLS_$_SAPolygonalGeofence
+ __OBJC_CLASS_RO_$_SACircularGeofence
+ __OBJC_CLASS_RO_$_SAGeoAlertData
+ __OBJC_CLASS_RO_$_SAGeofenceCoordinate
+ __OBJC_CLASS_RO_$_SAPolygonalGeofence
+ __OBJC_LABEL_PROTOCOL_$_NSCoding
+ __OBJC_LABEL_PROTOCOL_$_NSCopying
+ __OBJC_LABEL_PROTOCOL_$_NSSecureCoding
+ __OBJC_METACLASS_RO_$_SACircularGeofence
+ __OBJC_METACLASS_RO_$_SAGeoAlertData
+ __OBJC_METACLASS_RO_$_SAGeofenceCoordinate
+ __OBJC_METACLASS_RO_$_SAPolygonalGeofence
+ __OBJC_PROTOCOL_$_NSCoding
+ __OBJC_PROTOCOL_$_NSCopying
+ __OBJC_PROTOCOL_$_NSSecureCoding
+ ___35+[SafetyAlerts isSupportedPlatform]_block_invoke
+ ___39-[SAEDFollowUpManager _retractFollowUp]_block_invoke.98
+ ___50-[SafetyAlerts(GeoAlerts) getGeoAlert:completion:]_block_invoke
+ ___52-[SAEDFollowUpManager _evaluateFollowUpState_LOCKED]_block_invoke.53
+ ___58-[SafetyAlerts fetchAvailableAlertTypesOnQueue:withReply:]_block_invoke.80
+ ___60-[SafetyAlerts onAPSDConnectionChangeIsOverWiFi:isOverCell:]_block_invoke
+ ___NSArray0__struct
+ ____ZL16SAGetDeviceClassv_block_invoke
+ ___block_descriptor_56_ea8_32s40s48bs_e5_v8?0ls32l8s40l8s48l8
+ ___block_literal_global.265
+ ___block_literal_global.43
+ ___block_literal_global.60
+ _dispatch_get_global_queue
+ _objc_autorelease
+ _objc_claimAutoreleasedReturnValue
+ _objc_enumerationMutation
+ _objc_msgSend$addObject:
+ _objc_msgSend$alertHash
+ _objc_msgSend$alertType
+ _objc_msgSend$allocWithZone:
+ _objc_msgSend$array
+ _objc_msgSend$center
+ _objc_msgSend$circularGeofences
+ _objc_msgSend$coordinates
+ _objc_msgSend$copy
+ _objc_msgSend$count
+ _objc_msgSend$countByEnumeratingWithState:objects:count:
+ _objc_msgSend$createFromMergedDict:
+ _objc_msgSend$dateWithTimeIntervalSinceReferenceDate:
+ _objc_msgSend$decodeBoolForKey:
+ _objc_msgSend$decodeDoubleForKey:
+ _objc_msgSend$decodeIntegerForKey:
+ _objc_msgSend$decodeObjectOfClass:forKey:
+ _objc_msgSend$decodeObjectOfClasses:forKey:
+ _objc_msgSend$deliveryTime
+ _objc_msgSend$displayTime
+ _objc_msgSend$displayed
+ _objc_msgSend$encodeBool:forKey:
+ _objc_msgSend$encodeDouble:forKey:
+ _objc_msgSend$encodeInteger:forKey:
+ _objc_msgSend$encodeObject:forKey:
+ _objc_msgSend$epicenterCoordinate
+ _objc_msgSend$getGeoAlert:outError:
+ _objc_msgSend$getGeoAlertData:outError:
+ _objc_msgSend$identifier
+ _objc_msgSend$init
+ _objc_msgSend$initWithAlertHash:title:message:instructionMessage:language:safetyCategory:safetyEvent:safetyCategoryEnums:safetyEventEnums:deliveryTime:displayTime:displayed:polygonalGeofences:circularGeofences:epicenterCoordinate:alertType:
+ _objc_msgSend$initWithIdentifier:center:radius:
+ _objc_msgSend$initWithIdentifier:coordinates:
+ _objc_msgSend$initWithLatitude:longitude:
+ _objc_msgSend$instructionMessage
+ _objc_msgSend$integerValue
+ _objc_msgSend$isSupportedPlatform
+ _objc_msgSend$language
+ _objc_msgSend$latitude
+ _objc_msgSend$length
+ _objc_msgSend$longitude
+ _objc_msgSend$message
+ _objc_msgSend$parseCircularGeofencesFromArray:
+ _objc_msgSend$parseGeoAlertDataFromReply:outError:
+ _objc_msgSend$parsePolygonalGeofencesFromArray:
+ _objc_msgSend$polygonalGeofences
+ _objc_msgSend$radius
+ _objc_msgSend$safetyCategory
+ _objc_msgSend$safetyCategoryEnums
+ _objc_msgSend$safetyEvent
+ _objc_msgSend$safetyEventEnums
+ _objc_msgSend$setWithObjects:
+ _objc_msgSend$sharedInterface
+ _objc_msgSend$title
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x2
+ _objc_retain_x25
+ _objc_retain_x26
+ _objc_retain_x27
+ _objc_retain_x28
+ _os_variant_has_factory_content
- GCC_except_table60
- __OBJC_$_INSTANCE_METHODS_SafetyAlerts
- ___39-[SAEDFollowUpManager _retractFollowUp]_block_invoke.95
- ___52-[SAEDFollowUpManager _evaluateFollowUpState_LOCKED]_block_invoke.50
- ___58-[SafetyAlerts fetchAvailableAlertTypesOnQueue:withReply:]_block_invoke.68
- _objc_retainAutoreleasedReturnValue
CStrings:
+ "APSDBiomeCollectionEnabled"
+ "Alert not found"
+ "AppleTV"
+ "AudioAccessory"
+ "DualSIMActivationPolicyCapable"
+ "Failed to create GeoAlert data object"
+ "Failed to create XPC message"
+ "Invalid alert data format"
+ "Invalid alert hash"
+ "Invalid response format"
+ "Mac"
+ "No response from daemon"
+ "Unsupported platform"
+ "Watch"
+ "alertHash"
+ "alertType"
+ "center"
+ "circularGeofences"
+ "coordinates"
+ "deliveryTime"
+ "displayTime"
+ "displayed"
+ "epicenterCoordinate"
+ "geoAlertData"
+ "iPad"
+ "iPod"
+ "identifier"
+ "instructionMessage"
+ "language"
+ "latitude"
+ "longitude"
+ "polygonalGeofences"
+ "radius"
+ "saGetGeoAlert"
+ "safetyCategory"
+ "safetyCategoryEnums"
+ "safetyEvent"
+ "safetyEventEnums"
+ "title"
+ "{\"msg%{public}.0s\":\"#platformInfo\", \"deviceClass\":%{private, location:escape_only}s, \"iPhone\":%{private}hhd, \"iPod\":%{private}hhd, \"iPad\":%{private}hhd, \"watch\":%{private}hhd, \"appleTV\":%{private}hhd, \"homePod\":%{private}hhd, \"mac\":%{private}hhd, \"cellular\":%{private}hhd, \"dualSim\":%{private}hhd, \"cellularWatch\":%{private}hhd, \"wifiOnlyWatch\":%{private}hhd, \"internal\":%{private}hhd, \"supportedDevice\":%{private}hhd, \"supportedOSType\":%{private}hhd, \"supportedPlatform\":%{private}hhd, \"aop\":%{private}hhd, \"tinkerWatch\":%{private}hhd}"
+ "{\"msg%{public}.0s\":\"#saClient,fetchAvailableAlertTypes,unsupportedPlatform\"}"
+ "{\"msg%{public}.0s\":\"#saClient,fetchIsEnabled,unsupportedPlatform\"}"
+ "{\"msg%{public}.0s\":\"#saClient,fetchIsSaewEnabled,unsupportedPlatform\"}"
+ "{\"msg%{public}.0s\":\"#saClient,fetchSafetyAlertsSettingsSpecifiers,unsupportedPlatform\"}"
+ "{\"msg%{public}.0s\":\"#saClient,fetchSafetyAlertsSettingsSpecifiersSync,unsupportedPlatform\"}"
+ "{\"msg%{public}.0s\":\"#saClient,getGeoAlertData\", \"alertHash\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#saClient,getGeoAlertData,cantCreateMessage\"}"
+ "{\"msg%{public}.0s\":\"#saClient,getGeoAlertData,unsupportedPlatform\"}"
+ "{\"msg%{public}.0s\":\"#saClient,getIgneousTestStatusSync,unsupportedPlatform\"}"
+ "{\"msg%{public}.0s\":\"#saClient,notifyAlertSettingsChange,unsupportedPlatform\"}"
+ "{\"msg%{public}.0s\":\"#saClient,onAPSDConnectionChange,not collecting\"}"
+ "{\"msg%{public}.0s\":\"#saClient,onAPSDConnectionChange,sandbox\"}"
+ "{\"msg%{public}.0s\":\"#saClient,onAPSDConnectionChange,unsupportedPlatform\"}"
+ "{\"msg%{public}.0s\":\"#saClient,onEnhancedDeliveryEnabled,unsupportedPlatform\"}"
+ "{\"msg%{public}.0s\":\"#saClient,onNetworkConnectivityChanged,unsupportedPlatform\"}"
+ "{\"msg%{public}.0s\":\"#saClient,onSettingsPageVisited,unsupportedPlatform\"}"
+ "{\"msg%{public}.0s\":\"#saClient,onSignificantEventDetected,unsupportedPlatform\"}"
+ "{\"msg%{public}.0s\":\"#saClient,onTestMessage,unsupportedPlatform\"}"
+ "{\"msg%{public}.0s\":\"#saClient,onUserTappedOnUiWithInfo,unsupportedPlatform\"}"
+ "{\"msg%{public}.0s\":\"#saClient,onUserTappedOnWeaWithInfo,unsupportedPlatform\"}"
+ "{\"msg%{public}.0s\":\"#saClient,onWeaReceived,unsupportedPlatform\"}"
+ "{\"msg%{public}.0s\":\"#saClient,parseGeoAlertData,invalidDictionary\"}"
+ "{\"msg%{public}.0s\":\"#saClient,parseGeoAlertData,noGeoAlertData\"}"
+ "{\"msg%{public}.0s\":\"#saClient,parseGeoAlertData,replyIsNil\"}"
+ "{\"msg%{public}.0s\":\"#saClient,parseGeoAlertData,replyIsNotADictionary\"}"
+ "{\"msg%{public}.0s\":\"#saClient,parseGeoAlertData,success\", \"alertData\":%{private, location:escape_only}@}"
+ "{\"msg%{public}.0s\":\"#saClient,setSafetyAlertsSettingsState,unsupportedPlatform\"}"
+ "{\"msg%{public}.0s\":\"#saClient,unsupportedPlatform\", \"isSupportedDevice\":%{private}hhd, \"isSupportedOSType\":%{private}hhd}"
- ".cxx_destruct"
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSObject<OS_xpc_object>\""
- "@16@0:8"
- "@24@0:8@16"
- "@32@0:8@16@24"
- "APSDInterfaceStatus"
- "B"
- "B16@0:8"
- "B24@0:8@16"
- "B24@0:8Q16"
- "B28@0:8@16B24"
- "B32@0:8@16@24"
- "Device"
- "Q16@0:8"
- "Q32@0:8@16Q24"
- "SAIsImprovedDeliveryStateEnabled"
- "SAIsImprovedDeliveryVisible"
- "SafetyAlerts"
- "T@\"NSUserDefaults\",R,N"
- "TB,N"
- "TB,N,V_SAIsImprovedDeliveryStateEnabled"
- "TB,N,V_SAIsImprovedDeliveryVisible"
- "TB,N,V_currentLocationInCoveredRegion"
- "TB,N,V_locationServicesEnabled"
- "TQ,N"
- "Tf,N,V_uptakeCoefficient"
- "URLWithString:"
- "UTF8String"
- "Wireless"
- "_SAIsImprovedDeliveryStateEnabled"
- "_SAIsImprovedDeliveryVisible"
- "_addNotificationObservers"
- "_cfuPostInProgress"
- "_connection"
- "_ctSuppressEDFollowUpReason"
- "_currentDeviceHasEnhancedDeliverySwitch"
- "_currentLocationInCoveredRegion"
- "_currentLocationInCoveredRegion_Valid"
- "_evaluateFollowUpStateAsync"
- "_evaluateFollowUpState_LOCKED"
- "_evaluationQueue"
- "_isIgneousEnabled"
- "_locationServicesEnabled"
- "_locationServicesEnabled_Valid"
- "_onCellConfigChanged:"
- "_postFollowUp"
- "_queue"
- "_removeNotificationObservers"
- "_retractFollowUp"
- "_saSuppressEDFollowUpReason"
- "_shouldDeferFollowUpForSAReason:"
- "_shouldPostFollowUpForCTReason:"
- "_shouldPostFollowUpForSAReason:"
- "_shouldRetractFollowUpForSAReason:"
- "_uptakeCoefficient"
- "_uptakeCoefficient_Valid"
- "actionWithLabel:url:"
- "addObserver:selector:name:object:"
- "arrayWithObjects:count:"
- "boolForDefaultsKey:defaultValue:"
- "boolOverrideForDefaultsKey:defaultValue:"
- "boolValue"
- "bundleForClass:"
- "clearPendingFollowUpItemsWithUniqueIdentifiers:completion:"
- "countOfPendingFollowUpItemsWithCompletion:"
- "currentLocationInCoveredRegion"
- "date"
- "dealloc"
- "defaultCenter"
- "dictionaryWithObjects:forKeys:count:"
- "dictionaryWithObjectsAndKeys:"
- "doubleValue"
- "errorWithDomain:code:userInfo:"
- "f"
- "f16@0:8"
- "fetchAvailableAlertTypesOnQueue:withReply:"
- "fetchIsSaewEnabledOnQueue:withReply:"
- "fetchIsSafetyAlertsEnabledOnQueue:withReply:"
- "fetchSafetyAlertsSettingsSpecifiers:withReply:"
- "fetchSafetyAlertsSettingsSpecifiersSync"
- "floatValue"
- "followUpState"
- "getIgneousEnablementStateReply:stateInfo:"
- "getIgneousStatusInfoFromReply:"
- "getIgneousTestStatusSync"
- "getIsSafetyAlertsEnabledFromReply:"
- "hasNumberOverrideForDefaultsKey:"
- "hasValidCurrentLocationInCoveredRegion"
- "hasValidLocationServicesEnabled"
- "hasValidUptakeCoefficient"
- "init"
- "initWithClientIdentifier:"
- "initWithStarting:isAPSDOverWiFi:isAPSDOverCell:"
- "initWithSuiteName:"
- "intValue"
- "isEqualToString:"
- "jkr5aFPOh/d6zTzNKYthBw"
- "localizedStringForKey:value:table:"
- "locationServicesEnabled"
- "newCFUShown"
- "noteUserViewedEDSettings"
- "notifyAlertSettingsChange"
- "numberOverrideForDefaultsKey:defaultValue:"
- "numberWithBool:"
- "numberWithDouble:"
- "numberWithFloat:"
- "numberWithInt:"
- "numberWithUnsignedInteger:"
- "objectForKey:"
- "objectForKeyedSubscript:"
- "onAPSDConnectionChangeIsOverWiFi:isOverCell:"
- "onEnhancedDeliveryEnabled:"
- "onEnhancedDeliveryPageVisited"
- "onNetworkConnectivityChanged:"
- "onSettingsPageVisited"
- "onSignificantEventDetected:"
- "onTestMessage:"
- "onUserTappedOnUiWithInfo:"
- "onUserTappedOnWeaWithInfo:"
- "onWeaReceived:"
- "postFollowUpItem:completion:"
- "removeObjectForKey:"
- "removeObserver:name:object:"
- "sendEvent:"
- "setActions:"
- "setCtSuppressEDFollowUpReason:"
- "setCurrentLocationInCoveredRegion:"
- "setDisplayStyle:"
- "setFollowUpState:"
- "setGroupIdentifier:"
- "setInformativeText:"
- "setLocationServicesEnabled:"
- "setNewCFUShown:"
- "setObject:forKey:"
- "setSAEWEnabledState:"
- "setSAIsImprovedDeliveryStateEnabled:"
- "setSAIsImprovedDeliveryVisible:"
- "setSaSuppressEDFollowUpReason:"
- "setSafetyAlertsSettingsState:"
- "setTitle:"
- "setUniqueIdentifier:"
- "setUptakeCoefficient:"
- "setUserViewedEDSettings:"
- "setValue:forKey:"
- "settingsUpdate:isImprovedAlertStateEnabled:"
- "sharedInstance"
- "sharedInterface"
- "shouldShowCFUPerUptakeCoefficient"
- "source"
- "start"
- "stringForDefaultsKey:defaultValue:"
- "stringWithUTF8String:"
- "uintForDefaultsKey:defaultValue:"
- "unsignedIntegerValue"
- "uptakeCoefficient"
- "userDefaults"
- "v16@0:8"
- "v20@0:8B16"
- "v20@0:8f16"
- "v24@0:8@16"
- "v24@0:8B16B20"
- "v24@0:8Q16"
- "v32@0:8@16@?24"

```
