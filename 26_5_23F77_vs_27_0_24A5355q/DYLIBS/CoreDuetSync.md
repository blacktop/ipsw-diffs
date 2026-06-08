## CoreDuetSync

> `/System/Library/PrivateFrameworks/CoreDuetSync.framework/CoreDuetSync`

```diff

-1933.11.0.0.0
-  __TEXT.__text: 0x6c80
-  __TEXT.__auth_stubs: 0x320
+1956.0.1.0.0
+  __TEXT.__text: 0x6300
   __TEXT.__objc_methlist: 0x2b4
   __TEXT.__const: 0x50
-  __TEXT.__gcc_except_tab: 0x198
-  __TEXT.__cstring: 0xed
+  __TEXT.__gcc_except_tab: 0x178
+  __TEXT.__cstring: 0xef
   __TEXT.__oslogstring: 0x1354
-  __TEXT.__unwind_info: 0x1a8
-  __TEXT.__objc_classname: 0xae
-  __TEXT.__objc_methname: 0xe45
-  __TEXT.__objc_methtype: 0x34d
-  __TEXT.__objc_stubs: 0xb80
-  __DATA_CONST.__got: 0xf8
+  __TEXT.__unwind_info: 0x190
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x1d8
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x30

   __DATA_CONST.__objc_selrefs: 0x3a0
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x1a0
+  __DATA_CONST.__got: 0xf8
   __AUTH_CONST.__const: 0x20
   __AUTH_CONST.__cfstring: 0x120
   __AUTH_CONST.__objc_const: 0x2a8
+  __AUTH_CONST.__auth_got: 0x0
   __DATA.__objc_ivar: 0xc
   __DATA.__data: 0x240
   __DATA_DIRTY.__objc_data: 0xa0

   - /System/Library/PrivateFrameworks/NanoRegistry.framework/NanoRegistry
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 6CD0D70B-4BD4-3D84-A696-CCB5592A3C79
-  Functions: 111
-  Symbols:   477
-  CStrings:  236
+  UUID: C3FC2897-8E93-3808-8DE5-81314B4B3301
+  Functions: 108
+  Symbols:   473
+  CStrings:  74
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain
+ _objc_retain_x1
+ _objc_retain_x3
+ _objc_retain_x4
- GCC_except_table60
- GCC_except_table81
- _OUTLINED_FUNCTION_28
- _OUTLINED_FUNCTION_29
- _objc_release
- _objc_retain_x24
- _objc_retain_x25
CStrings:
- ".cxx_destruct"
- "@\"<_DKSyncRemoteContextStorage>\""
- "@\"NSDictionary\"32@0:8@\"<_DKSyncRemoteContextStorage>\"16@\"NSArray\"24"
- "@\"NSObject<OS_os_transaction>\""
- "@\"NSUUID\"16@0:8"
- "@16@0:8"
- "@24@0:8@\"NSCoder\"16"
- "@24@0:8@16"
- "@24@0:8^{_NSZone=}16"
- "@32@0:8@16@24"
- "B16@0:8"
- "B32@0:8@\"<_DKSyncRemoteContextStorage>\"16@\"NSString\"24"
- "B32@0:8@16@24"
- "B32@0:8Q16^@24"
- "B40@0:8@16@24^@32"
- "NSCoding"
- "NSCopying"
- "NSSecureCoding"
- "Q"
- "T@\"<_DKSyncRemoteContextStorage>\",&,N,V_transportMDCSRapport"
- "T@\"NSUUID\",R,N"
- "TB,R"
- "_CDRemoteUserContextServer"
- "_DKSync3Coordinator"
- "_DKSyncCoordinatorFactory"
- "_DKSyncRemoteContextStorageDelegate"
- "_DKSyncRemoteStorageDelegate"
- "_fetchPropertiesOfRemoteKeyPaths:handler:"
- "_requestActivateDevicesWithHandler:"
- "_syncDisabledToggle"
- "_syncEnabledToggle"
- "_transportMDCSRapport"
- "_watchingDeviceTypes"
- "_watchingDevicesTransaction"
- "activateDevices:remoteUserContextProxySourceDeviceUUID:"
- "activeTransportsForPeer:"
- "addObject:"
- "addObserverForName:object:queue:usingBlock:"
- "allKeys"
- "allObjects"
- "archivedDataWithRootObject:requiringSecureCoding:error:"
- "archivedObjectsForKeyPaths:"
- "arrayWithCapacity:"
- "arrayWithObjects:count:"
- "code"
- "conformsToProtocol:"
- "copyWithZone:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "deactivateDevices:remoteUserContextProxySourceDeviceUUID:"
- "dealloc"
- "defaultCenter"
- "deregisterCallback:"
- "description"
- "deviceUUID"
- "dictionaryWithCapacity:"
- "domain"
- "doubleValue"
- "encodeWithCoder:"
- "existingPeerWithSourceDeviceID:"
- "fetchContextValuesFromPeer:forKeyPaths:highPriority:completion:"
- "fetchPropertiesOfRemoteKeyPaths:handler:"
- "firstObject"
- "handleContextChangedNotification:"
- "handleStatusChangeForPeer:previousTransports:"
- "hasKnowledgeOfContextualKeyPath:"
- "identifier"
- "initWithCoder:"
- "initWithContext:"
- "initWithName:deviceID:model:companion:"
- "initWithPlistDictionary:"
- "invalidData"
- "isCompanion"
- "isMultiDeviceRegistration"
- "keyPathWithKey:"
- "keyPaths"
- "keyPathsByDeviceIDFromRemoteKeyPaths:"
- "lastModifiedDateForContextualKeyPath:"
- "me"
- "model"
- "multiDeviceContextStoreDevices"
- "mutableCopy"
- "numberWithUnsignedInteger:"
- "objectForContextualKeyPath:"
- "objectForKeyedSubscript:"
- "operationQueue"
- "peersForContextStoreDeviceIDs:"
- "peersWithActiveTransports:"
- "performAsyncBlock:"
- "performSyncBlock:"
- "plistDictionary"
- "policyForSyncTransportType:"
- "predicate"
- "rapportSyncDisabled"
- "registerCallback:"
- "registrationIdentifierForPeer:remoteRegistrationIdentifier:"
- "registrationWithIdentifier:contextualPredicate:dismissalPolicy:deviceSet:clientIdentifier:mustWake:callback:"
- "remoteContextStorage:archivedObjectsForKeyPaths:"
- "remoteContextStorage:hasKnowledgeOfKeyPath:"
- "remoteContextStorage:registrationIdentifier:setArchivedObjects:peer:"
- "remoteContextStorage:subscribeToChangesWithPeer:registrationIdentifier:predicate:"
- "remoteContextStorage:unsubscribeFromChangesWithPeer:registrationIdentifier:predicate:"
- "remoteKeyPathForKeyPath:forDeviceID:"
- "removeObject:"
- "removeObserver:name:object:"
- "requestActivateDevicesWithHandler:"
- "sendContextValuesToPeer:registrationIdentifier:archivedObjects:highPriority:completion:"
- "sendContextValuesToPeer:registrationIdentifier:keyPaths:"
- "setArchivedObjects:peer:"
- "setDelegate:"
- "setObject:forKeyedSubscript:"
- "setObject:lastModifiedDate:forContextualKeyPath:"
- "setRemoteUserContextProxy:"
- "setTransportMDCSRapport:"
- "setWithArray:"
- "setWithCapacity:"
- "setupStorage"
- "sharedInstance"
- "sourceDeviceID"
- "sourceDeviceUUID"
- "start"
- "stringWithFormat:"
- "subscribeToContextValueChangeNotificationsFromPeer:registrationIdentifier:predicate:highPriority:completion:"
- "subscribeToContextValueChangeNotificationsWithRegistration:deviceIDs:error:"
- "subscribeToContextValueChangeNotificationsWithRegistration:deviceIDs:handler:"
- "subscribeToDeviceStatusChangeNotificationsForDeviceTypes:error:"
- "subscribeToDeviceStatusChangeNotificationsForDeviceTypes:handler:"
- "supportedContextValueClasses"
- "supportsSecureCoding"
- "syncChannel"
- "syncCoordinatorWithContext:"
- "syncDisabled"
- "transportMDCSRapport"
- "unarchivedObjectOfClasses:fromData:error:"
- "underlyingQueue"
- "unsubscribeFromContextValueChangeNotificationsFromPeer:registrationIdentifier:predicate:highPriority:completion:"
- "unsubscribeFromContextValueChangeNotificationsWithRegistration:deviceIDs:error:"
- "unsubscribeFromContextValueChangeNotificationsWithRegistration:deviceIDs:handler:"
- "userContext"
- "userInfo"
- "v16@0:8"
- "v24@0:8@\"NSCoder\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8@?<v@?@\"NSError\">16"
- "v32@0:8@\"NSArray\"16@?<v@?@\"NSError\">24"
- "v32@0:8@16@24"
- "v32@0:8@16@?24"
- "v32@0:8@16q24"
- "v32@0:8Q16@?24"
- "v32@0:8Q16@?<v@?@\"NSError\">24"
- "v40@0:8@\"_CDContextualChangeRegistration\"16@\"NSArray\"24@?<v@?@\"NSError\">32"
- "v40@0:8@16@24@32"
- "v40@0:8@16@24@?32"
- "v48@0:8@\"<_DKSyncRemoteContextStorage>\"16@\"NSString\"24@\"NSDictionary\"32@\"_DKSyncPeer\"40"
- "v48@0:8@\"<_DKSyncRemoteContextStorage>\"16@\"_DKSyncPeer\"24@\"NSString\"32@\"NSDictionary\"40"
- "v48@0:8@16@24@32@40"
- "valueForKey:"
- "valueForKeyPath:"
- "version"

```
