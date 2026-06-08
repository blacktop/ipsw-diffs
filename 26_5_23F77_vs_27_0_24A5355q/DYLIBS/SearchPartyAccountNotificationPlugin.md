## SearchPartyAccountNotificationPlugin

> `/System/Library/Accounts/Notification/SearchPartyAccountNotificationPlugin.bundle/SearchPartyAccountNotificationPlugin`

```diff

-423.35.2.23.4
-  __TEXT.__text: 0x16e4
-  __TEXT.__auth_stubs: 0x2f0
+446.30.5.17.5
+  __TEXT.__text: 0x1458
   __TEXT.__objc_methlist: 0x4b8
   __TEXT.__const: 0x38
   __TEXT.__gcc_except_tab: 0x28
-  __TEXT.__cstring: 0xbb
+  __TEXT.__cstring: 0xbd
   __TEXT.__oslogstring: 0x25b
-  __TEXT.__unwind_info: 0xd8
-  __TEXT.__objc_classname: 0x88
-  __TEXT.__objc_methname: 0xe26
-  __TEXT.__objc_methtype: 0xa33
-  __TEXT.__objc_stubs: 0x3e0
-  __DATA_CONST.__got: 0x60
+  __TEXT.__unwind_info: 0xc0
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0xe8
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x20

   __DATA_CONST.__objc_selrefs: 0x380
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x188
+  __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x40
   __AUTH_CONST.__cfstring: 0xa0
   __AUTH_CONST.__objc_const: 0x4c0
+  __AUTH_CONST.__auth_got: 0x0
   __DATA.__objc_ivar: 0x10
   __DATA.__data: 0x180
   __DATA_DIRTY.__objc_data: 0x50

   - /System/Library/PrivateFrameworks/SPOwner.framework/SPOwner
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 9AE8B186-51C9-32C1-9350-58C789300F94
-  Functions: 33
-  Symbols:   66
-  CStrings:  246
+  UUID: B2F114C0-5FB3-3437-B04A-7A74D36C9D7C
+  Functions: 31
+  Symbols:   69
+  CStrings:  29
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x8
- _objc_retainAutoreleasedReturnValue
CStrings:
- "#16@0:8"
- ".cxx_destruct"
- "@\"AKAccountManager\""
- "@\"FMXPCServiceDescription\""
- "@\"FMXPCSession\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSString\"16@0:8"
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@16"
- "@24@0:8@?16"
- "@32@0:8:16@24"
- "@40@0:8:16@24@32"
- "ACDAccountNotificationPlugin"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B32@0:8@\"ACAccount\"16@\"ACDAccountStore\"24"
- "B32@0:8@16@24"
- "B40@0:8@\"ACAccount\"16@\"ACDAccountStore\"24^@32"
- "B40@0:8@16@24^@32"
- "B44@0:8@\"ACAccount\"16i24@\"ACDAccountStore\"28@\"ACAccount\"36"
- "B44@0:8@16i24@28@36"
- "NSObject"
- "Q16@0:8"
- "SPBeaconManagerXPCProtocol"
- "SPLocalBeaconManagerXPCProtocol"
- "SearchPartyAccountNotificationPlugin"
- "T#,R"
- "T@\"FMXPCServiceDescription\",&,N,V_serviceDescription"
- "T@\"FMXPCSession\",&,N,V_session"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_serialQueue"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "TQ,R"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_akAccountManager"
- "_extractPhoneNumberFrom:"
- "_serialQueue"
- "_serviceDescription"
- "_session"
- "aa_isAccountClass:"
- "account:didChangeWithType:inStore:oldAccount:"
- "account:didPerformActionsForDataclasses:"
- "account:willChangeWithType:inStore:oldAccount:"
- "account:willPerformActionsForDataclasses:"
- "accountType"
- "additionalInfoForAccount:"
- "allBeaconingKeysForUUID:dateInterval:forceGenerate:completion:"
- "allBeaconsOfTypes:includeDupes:includeHidden:completion:"
- "allBeaconsWithCompletion:"
- "allDuriansWithCompletion:"
- "autorelease"
- "beaconForUUID:completion:"
- "beaconingKeysForUUID:dateInterval:completion:"
- "beaconingKeysOfType:withCompletion:"
- "beaconingStateWithCompletion:"
- "beaconsInFirmwareUpdateState:dateInterval:completion:"
- "bluetoothPowerStateUpdated:"
- "canRemoveAccount:inStore:"
- "canRemoveAccount:inStore:error:"
- "canSaveAccount:inStore:"
- "canSaveAccount:inStore:error:"
- "cancel"
- "class"
- "commandKeysForUUID:withCriteria:completion:"
- "commandKeysForUUIDs:completion:"
- "commandKeysForUUIDs:dateInterval:completion:"
- "conformsToProtocol:"
- "connectedToBeacon:withIndex:completion:"
- "countByEnumeratingWithState:objects:count:"
- "createDuplicateBeaconsForBeacon:skipGroupIdentifier:count:completion:"
- "createOwnedDeviceKeyRecordForUUID:completion:"
- "debugDescription"
- "description"
- "fetchAllKeyMapFileDescriptorsWithCompletion:"
- "fetchFirmwareVersionForBeacon:completion:"
- "fetchUserStatsForBeacon:completion:"
- "firmwareUpdateCandidateBeaconsWithCompletion:"
- "firmwareUpdateStateForBeaconUUID:completion:"
- "getMacBeaconConfigWithCompletion:"
- "hash"
- "identifier"
- "init"
- "initWithMachServiceName:options:remoteObjectInterface:interruptionHandler:invalidationHandler:"
- "initWithQueue:timeout:completion:"
- "initWithServiceDescription:"
- "initiateFirmwareUpdateForAllEligibleBeaconsWithCompletion:"
- "interfaceWithProtocol:"
- "invalidate"
- "isEqual:"
- "isEqualToString:"
- "isKindOfClass:"
- "isLPEMModeSupportedWithCompletion:"
- "isMemberOfClass:"
- "isProxy"
- "keySyncMetadataWithcompletion:"
- "machService"
- "nearOwnerCommandKeysWithCompletion:"
- "notificationBeaconForSubscriptionId:completion:"
- "objectForKeyedSubscript:"
- "offlineAdvertisingKeysForReason:completion:"
- "ownedDeviceKeyRecordsForUUID:completion:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "poisonBeaconIdentifier:completion:"
- "postedLocalNotifyWhenFoundNotificationForUUID:completion:"
- "proxy"
- "purgeOwnedDeviceKeyRecordsForUUID:completion:"
- "release"
- "removeDuplicateBeaconsWithCompletion:"
- "removeLocalAccountDataWithCompletion:"
- "repairDataStore:"
- "respondsToSelector:"
- "resume"
- "retain"
- "retainCount"
- "roleCategoriesWithCompletion:"
- "securityLevelForAccount:"
- "self"
- "serialQueue"
- "serviceDescription"
- "session"
- "setAlignmentUncertainty:atIndex:date:forBeacon:completion:"
- "setCurrentWildKeyIndex:forBeacon:completion:"
- "setKeyRollInterval:forBeacon:completion:"
- "setRole:beaconId:completion:"
- "setSerialQueue:"
- "setServiceDescription:"
- "setServiceState:completion:"
- "setSession:"
- "setSuppressLPEMBeaconing:completion:"
- "setUserHasAcknowledgedFindMy:completion:"
- "setWildKeyBase:interval:fallback:forBeacon:completion:"
- "sharedInstance"
- "start"
- "startUpdatingSimpleBeaconsWithContext:completion:"
- "submitDeviceEvent:source:attachedTo:completion:"
- "superclass"
- "syncProxyWithErrorHandler:"
- "synchronousProxyWithErrorHandler:"
- "unacceptedBeaconsWithCompletion:"
- "updateBeacon:updates:completion:"
- "updateBeaconUUID:firmwareUpdateState:systemVersion:error:completion:"
- "updateObfuscatedIdentifierWithCompletion:"
- "userAgentProxy"
- "userAgentSynchronousProxyWithErrorHandler:"
- "userHasAcknowledgeFindMyWithCompletion:"
- "v16@0:8"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8@?<v@?>16"
- "v24@0:8@?<v@?@\"NSArray\">16"
- "v24@0:8@?<v@?@\"NSArray\"@\"NSError\">16"
- "v24@0:8@?<v@?@\"NSData\"@\"NSError\">16"
- "v24@0:8@?<v@?@\"NSDictionary\"@\"NSError\">16"
- "v24@0:8@?<v@?@\"NSError\">16"
- "v24@0:8@?<v@?@\"NSSet\">16"
- "v24@0:8@?<v@?@\"SPMacBeaconConfig\"@\"NSError\">16"
- "v24@0:8@?<v@?B>16"
- "v24@0:8@?<v@?q>16"
- "v24@0:8q16"
- "v28@0:8B16@?20"
- "v28@0:8B16@?<v@?>20"
- "v32@0:8@\"ACAccount\"16@\"NSArray\"24"
- "v32@0:8@\"NSArray\"16@?<v@?@\"NSDictionary\">24"
- "v32@0:8@\"NSString\"16@?<v@?@\"NSError\">24"
- "v32@0:8@\"NSUUID\"16@?<v@?>24"
- "v32@0:8@\"NSUUID\"16@?<v@?@\"NSArray\">24"
- "v32@0:8@\"NSUUID\"16@?<v@?@\"NSArray\"@\"NSError\">24"
- "v32@0:8@\"NSUUID\"16@?<v@?@\"NSData\">24"
- "v32@0:8@\"NSUUID\"16@?<v@?@\"SPBeacon\">24"
- "v32@0:8@\"NSUUID\"16@?<v@?@\"SPBeacon\"@\"SPBeaconGroup\">24"
- "v32@0:8@\"NSUUID\"16@?<v@?@\"SPFirmwareUpdateStateResult\">24"
- "v32@0:8@\"NSUUID\"16@?<v@?@\"SPOwnedDeviceKeyRecord\"@\"NSError\">24"
- "v32@0:8@\"NSUUID\"16@?<v@?@\"SPTagUserStats\">24"
- "v32@0:8@\"NSUUID\"16@?<v@?B>24"
- "v32@0:8@\"SPSimpleBeaconContext\"16@?<v@?B@\"NSError\">24"
- "v32@0:8@16@24"
- "v32@0:8@16@?24"
- "v32@0:8q16@?24"
- "v32@0:8q16@?<v@?@\"NSArray\">24"
- "v40@0:8@\"NSArray\"16@\"NSDateInterval\"24@?<v@?@\"NSDictionary\">32"
- "v40@0:8@\"NSSet\"16B24B28@?<v@?@\"NSSet\">32"
- "v40@0:8@\"NSUUID\"16@\"NSDateInterval\"24@?<v@?@\"NSArray\">32"
- "v40@0:8@\"NSUUID\"16@\"SPBeaconUpdates\"24@?<v@?B>32"
- "v40@0:8@\"NSUUID\"16@\"SPCommandKeysCriteria\"24@?<v@?@\"NSArray\">32"
- "v40@0:8@\"NSUUID\"16Q24@?<v@?B>32"
- "v40@0:8@16@24@?32"
- "v40@0:8@16B24B28@?32"
- "v40@0:8@16Q24@?32"
- "v40@0:8Q16@\"NSUUID\"24@?<v@?B>32"
- "v40@0:8Q16@24@?32"
- "v40@0:8q16@\"NSDateInterval\"24@?<v@?@\"NSArray\">32"
- "v40@0:8q16@\"NSUUID\"24@?<v@?@\"SPBeacon\">32"
- "v40@0:8q16@\"NSUUID\"24@?<v@?B>32"
- "v40@0:8q16@24@?32"
- "v44@0:8@\"ACAccount\"16i24@\"ACDAccountStore\"28@\"ACAccount\"36"
- "v44@0:8@\"NSUUID\"16@\"NSDateInterval\"24B32@?<v@?@\"NSArray\">36"
- "v44@0:8@\"NSUUID\"16B24q28@?<v@?@\"NSError\">36"
- "v44@0:8@\"NSUUID\"16I24@\"NSUUID\"28@?<v@?@\"NSError\">36"
- "v44@0:8@16@24B32@?36"
- "v44@0:8@16B24q28@?36"
- "v44@0:8@16I24@28@?36"
- "v44@0:8@16i24@28@36"
- "v56@0:8@\"NSUUID\"16q24@\"NSString\"32@\"NSError\"40@?<v@?B>48"
- "v56@0:8@16q24@32@40@?48"
- "v56@0:8Q16Q24Q32@\"NSUUID\"40@?<v@?B>48"
- "v56@0:8Q16Q24Q32@40@?48"
- "v56@0:8d16Q24@\"NSDate\"32@\"NSUUID\"40@?<v@?B>48"
- "v56@0:8d16Q24@32@40@?48"
- "zone"

```
