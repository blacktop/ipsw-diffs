## HMAssistant

> `/System/Library/Assistant/Plugins/HMAssistant.assistantBundle/HMAssistant`

```diff

-1418.6.20.0.0
-  __TEXT.__text: 0x1b24
-  __TEXT.__auth_stubs: 0x3b0
+1468.5.0.0.6
+  __TEXT.__text: 0x1d80
   __TEXT.__objc_methlist: 0x33c
-  __TEXT.__const: 0x30
-  __TEXT.__gcc_except_tab: 0xc0
-  __TEXT.__cstring: 0x86
-  __TEXT.__oslogstring: 0x3fa
-  __TEXT.__unwind_info: 0xd8
-  __TEXT.__objc_classname: 0x4f
-  __TEXT.__objc_methname: 0x7ec
-  __TEXT.__objc_methtype: 0x3fd
-  __TEXT.__objc_stubs: 0x620
-  __DATA_CONST.__got: 0x60
+  __TEXT.__const: 0x58
+  __TEXT.__gcc_except_tab: 0x8c
+  __TEXT.__cstring: 0x89
+  __TEXT.__oslogstring: 0x784
+  __TEXT.__unwind_info: 0xa8
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x98
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x2c0
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x1e8
+  __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x20
   __AUTH_CONST.__cfstring: 0xa0
   __AUTH_CONST.__objc_const: 0x440
+  __AUTH_CONST.__auth_got: 0x0
   __DATA.__objc_ivar: 0x20
   __DATA.__data: 0x180
+  __DATA.__bss: 0x10
   __DATA_DIRTY.__objc_data: 0x50
-  __DATA_DIRTY.__bss: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/HomeKit.framework/HomeKit

   - /System/Library/PrivateFrameworks/SAObjects.framework/SAObjects
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B863DCB8-493A-364E-AA30-56460F871C3B
+  UUID: C40A0B9B-606B-330E-9709-36784AAF6FF2
   Functions: 31
-  Symbols:   78
-  CStrings:  185
+  Symbols:   79
+  CStrings:  44
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x26
- _objc_autoreleaseReturnValue
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x25
- _objc_retain_x28
CStrings:
+ "Failed to retrieve Siri sync data - error %@"
+ "Finished sync data retrieval refresh in %llu milliseconds - dropping home names from sync data %@"
+ "Home manager did update homes in %llu milliseconds"
+ "Incoming key '%@' does not match plug-in key '%@'"
+ "Indicating syncDidEnd from dealloc"
+ "Leaving the dispatch group as it did not time out."
+ "No accessories configured - skipping sync request from Siri client..."
+ "No sync entities from homed"
+ "Siri: entity: %@"
+ "Started initialization of home manager with configuration %@"
+ "Timed out waiting for homed"
+ "[%{public}@] Failed to retrieve Siri sync data - error %@"
+ "[%{public}@] Finished sync data retrieval refresh in %llu milliseconds - dropping home names from sync data %@"
+ "[%{public}@] Home manager did update homes in %llu milliseconds"
+ "[%{public}@] Incoming key '%@' does not match plug-in key '%@'"
+ "[%{public}@] Indicating syncDidEnd from dealloc"
+ "[%{public}@] Leaving the dispatch group as it did not time out."
+ "[%{public}@] No accessories configured - skipping sync request from Siri client..."
+ "[%{public}@] No sync entities from homed"
+ "[%{public}@] Siri: entity: %@"
+ "[%{public}@] Started initialization of home manager with configuration %@"
+ "[%{public}@] Timed out waiting for homed"
+ "[%{public}@] finalAnchor is %@"
+ "[%{public}@] homed did not respond"
+ "[%{public}@] lastSyncValidity '%@' different from assistantConfigurationSnapshot %@ - reset all data so that full sync attempted next time"
+ "[%{public}@] lastSyncedSnapshot %@ at same as assistantConfigurationSnapshot %@ - skipping sync..."
+ "[%{public}@] lastSyncedVersion %@  beginAnchor is %@  validity %@  key %@  count %tu"
+ "finalAnchor is %@"
+ "homed did not respond"
+ "lastSyncValidity '%@' different from assistantConfigurationSnapshot %@ - reset all data so that full sync attempted next time"
+ "lastSyncedSnapshot %@ at same as assistantConfigurationSnapshot %@ - skipping sync..."
+ "lastSyncedVersion %@  beginAnchor is %@  validity %@  key %@  count %tu"
- "#16@0:8"
- "%{public}@Failed to retrieve Siri sync data - error %@"
- "%{public}@Finished sync data retrieval refresh in %llu milliseconds - dropping home names from sync data %@"
- "%{public}@Home manager did update homes in %llu milliseconds"
- "%{public}@Incoming key '%@' does not match plug-in key '%@'"
- "%{public}@Indicating syncDidEnd from dealloc"
- "%{public}@Leaving the dispatch group as it did not time out."
- "%{public}@No accessories configured - skipping sync request from Siri client..."
- "%{public}@No sync entities from homed"
- "%{public}@Siri: entity: %@"
- "%{public}@Started initialization of home manager with configuration %@"
- "%{public}@Timed out waiting for homed"
- "%{public}@finalAnchor is %@"
- "%{public}@homed did not respond"
- "%{public}@lastSyncValidity '%@' different from assistantConfigurationSnapshot %@ - reset all data so that full sync attempted next time"
- "%{public}@lastSyncedSnapshot %@ at same as assistantConfigurationSnapshot %@ - skipping sync..."
- "%{public}@lastSyncedVersion %@  beginAnchor is %@  validity %@  key %@  count %tu"
- ".cxx_destruct"
- "@\"AFSyncSnapshot\"16@0:8"
- "@\"AFSyncSnapshot\"24@0:8@\"NSString\"16"
- "@\"HMHomeManager\""
- "@\"NSArray\""
- "@\"NSObject\"16@0:8"
- "@\"NSObject<OS_dispatch_group>\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"NSString\"24@0:8@\"NSString\"16"
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@16"
- "@32@0:8:16@24"
- "@40@0:8:16@24@32"
- "AFSyncHandler"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "HMAssistantSyncHome"
- "HMFLogging"
- "HMHomeManagerDelegate"
- "NSObject"
- "Q"
- "Q16@0:8"
- "T#,R"
- "T@\"HMHomeManager\",&,N,V_homeManager"
- "T@\"NSArray\",&,N,V_anchors"
- "T@\"NSArray\",&,N,V_entities"
- "T@\"NSObject<OS_dispatch_group>\",&,N,V_waitGroup"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_queue"
- "T@\"NSString\",&,N,V_finalAnchor"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "TB,N,V_done"
- "TQ,N,V_fetchHomeConfigurationStartTime"
- "TQ,R"
- "UTF8String"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_anchors"
- "_done"
- "_entities"
- "_fetchHomeConfigurationStartTime"
- "_finalAnchor"
- "_homeManager"
- "_queue"
- "_waitGroup"
- "addObject:"
- "anchors"
- "areAnyAccessoriesConfigured"
- "array"
- "autorelease"
- "beginSyncWithAnchor:validity:count:forKey:beginInfo:"
- "beginSyncWithAnchor:validity:count:forKey:beginInfo:configuration:"
- "beginSyncWithAnchor:validity:forKey:beginInfo:"
- "beginSyncWithInfo:configuration:"
- "boolValue"
- "class"
- "conformsToProtocol:"
- "copy"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "currentSyncSnapshot"
- "dealloc"
- "debugDescription"
- "defaultPrivateConfiguration"
- "description"
- "done"
- "entities"
- "entityType"
- "fetchHomeConfigurationStartTime"
- "finalAnchor"
- "getChangeAfterAnchor:changeInfo:"
- "hash"
- "hm_shortDescription"
- "hmf_arrayForKey:"
- "homeManager"
- "homeManager:didAddHome:"
- "homeManager:didReceiveAddAccessoryRequest:"
- "homeManager:didRemoveHome:"
- "homeManager:didUpdateAuthorizationStatus:"
- "homeManagerDidUpdateHomes:"
- "homeManagerDidUpdatePrimaryHome:"
- "indexOfObject:"
- "init"
- "initWithConfiguration:"
- "initWithDictionary:"
- "initWithNoValidation"
- "isEqual:"
- "isEqualToString:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "logCategory"
- "logIdentifier"
- "objectAtIndex:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "preferenceForKey:"
- "queue"
- "release"
- "requestSiriSyncDataWithValidity:completion:"
- "resetWithValidity:"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "self"
- "setAnchors:"
- "setCachePolicy:"
- "setDefaultValue:forPreferenceKey:"
- "setDelegate:"
- "setDone:"
- "setEntities:"
- "setFetchHomeConfigurationStartTime:"
- "setFinalAnchor:"
- "setHome:"
- "setHomeManager:"
- "setName:"
- "setObject:"
- "setOptions:"
- "setPostAnchor:"
- "setQueue:"
- "setWaitGroup:"
- "sharedPreferences"
- "shouldSyncForAnchor:"
- "stringWithFormat:"
- "superclass"
- "syncDidEnd"
- "syncSnapshotForKey:"
- "syncVerificationKeyForKey:"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@\"HMHomeManager\"16"
- "v24@0:8@16"
- "v24@0:8Q16"
- "v32@0:8@\"<AFSyncBeginInfo>\"16@\"<AFSyncConfiguration>\"24"
- "v32@0:8@\"HMHomeManager\"16@\"HMAddAccessoryRequest\"24"
- "v32@0:8@\"HMHomeManager\"16@\"HMHome\"24"
- "v32@0:8@\"HMHomeManager\"16Q24"
- "v32@0:8@\"NSString\"16@\"<AFSyncChangeInfo>\"24"
- "v32@0:8@16@24"
- "v32@0:8@16Q24"
- "v48@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32@\"<AFSyncBeginInfo>\"40"
- "v48@0:8@16@24@32@40"
- "v56@0:8@\"NSString\"16@\"NSString\"24q32@\"NSString\"40@\"<AFSyncBeginInfo>\"48"
- "v56@0:8@16@24q32@40@48"
- "v64@0:8@\"NSString\"16@\"NSString\"24q32@\"NSString\"40@\"<AFSyncBeginInfo>\"48@\"<AFSyncConfiguration>\"56"
- "v64@0:8@16@24q32@40@48@56"
- "waitGroup"
- "zone"

```
