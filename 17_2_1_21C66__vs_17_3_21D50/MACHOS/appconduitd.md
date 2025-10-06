## appconduitd

> `/System/Library/PrivateFrameworks/AppConduit.framework/Support/appconduitd`

```diff

-356.60.2.0.0
-  __TEXT.__text: 0x55398
+356.80.2.0.0
+  __TEXT.__text: 0x58f68
   __TEXT.__auth_stubs: 0xa00
-  __TEXT.__objc_stubs: 0x79c0
-  __TEXT.__objc_methlist: 0x302c
+  __TEXT.__objc_stubs: 0x7e20
+  __TEXT.__objc_methlist: 0x32ec
   __TEXT.__const: 0xb8
-  __TEXT.__gcc_except_tab: 0x9b0
-  __TEXT.__objc_methname: 0xb3c3
-  __TEXT.__cstring: 0x13552
-  __TEXT.__objc_classname: 0x572
-  __TEXT.__objc_methtype: 0x1c92
+  __TEXT.__gcc_except_tab: 0x9e4
+  __TEXT.__objc_methname: 0xbb95
+  __TEXT.__cstring: 0x1451c
+  __TEXT.__objc_classname: 0x5da
+  __TEXT.__objc_methtype: 0x1d2d
   __TEXT.__oslogstring: 0x1a0
-  __TEXT.__unwind_info: 0x112c
+  __TEXT.__unwind_info: 0x120c
   __DATA_CONST.__auth_got: 0x510
-  __DATA_CONST.__got: 0x230
+  __DATA_CONST.__got: 0x258
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x1810
-  __DATA_CONST.__cfstring: 0x89c0
-  __DATA_CONST.__objc_classlist: 0x120
+  __DATA_CONST.__const: 0x18f0
+  __DATA_CONST.__cfstring: 0x8ea0
+  __DATA_CONST.__objc_classlist: 0x130
   __DATA_CONST.__objc_catlist: 0x18
-  __DATA_CONST.__objc_protolist: 0x98
+  __DATA_CONST.__objc_protolist: 0xa0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_intobj: 0x390
-  __DATA_CONST.__objc_arraydata: 0xf0
-  __DATA_CONST.__objc_dictobj: 0x118
+  __DATA_CONST.__objc_intobj: 0x3d8
+  __DATA_CONST.__objc_arraydata: 0x100
+  __DATA_CONST.__objc_dictobj: 0x140
   __DATA_CONST.__objc_doubleobj: 0x10
-  __DATA.__objc_const: 0x9560
-  __DATA.__objc_selrefs: 0x2168
-  __DATA.__objc_classrefs: 0x2a8
-  __DATA.__objc_superrefs: 0x110
-  __DATA.__objc_ivar: 0x3b4
-  __DATA.__objc_data: 0xb40
-  __DATA.__data: 0x760
-  __DATA.__bss: 0x128
+  __DATA.__objc_const: 0x9a88
+  __DATA.__objc_selrefs: 0x22a0
+  __DATA.__objc_classrefs: 0x2b8
+  __DATA.__objc_superrefs: 0x120
+  __DATA.__objc_ivar: 0x3e8
+  __DATA.__objc_data: 0xbe0
+  __DATA.__data: 0x7c0
+  __DATA.__bss: 0x148
   __DATA.__common: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libmis.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: D4BA55A8-7891-383B-B1DB-E48BF42DC147
-  Functions: 1509
-  Symbols:   294
-  CStrings:  4610
+  UUID: 5077E565-58F5-326C-8654-7A7985254239
+  Functions: 1592
+  Symbols:   299
+  CStrings:  4775
 
Symbols:
+ _IXAppRemovabilityChangedNotificationName
+ _IXNotificationPayloadRemovabilityStoreClockKey
+ _IXNotificationPayloadRemovabilityValueKey
+ _kIXNotificationPayloadDataStoreClockGUIDKey
+ _kIXNotificationPayloadDataStoreClockSequenceNumberKey
CStrings:
+ "\x02\""
+ "\x19"
+ "%@ requested for app removability for device pairing ID: %@"
+ "+[ACXRemoteAppRemovabilityManager remoteRemovabilityManagerForStorageBaseURL:delegate:queue:]"
+ "-[ACXCompanionSyncConnection _onQueue_configureRemoteRemovabilityManagerAndFetchRemoteRemovabilityStatus]"
+ "-[ACXCompanionSyncConnection _onQueue_fetchRemovabilityForRemoteAppsWithRetryCount:]_block_invoke"
+ "-[ACXCompanionSyncConnection _onQueue_fetchRemovabilityForRemoteApps]"
+ "-[ACXCompanionSyncConnection _onQueue_handleAppRemovabilityUpdatedMessage:]"
+ "-[ACXCompanionSyncConnection _onQueue_handleRemoteRemovabilityFetchResponse:]"
+ "-[ACXCompanionSyncConnection applicationsRemovabilityUpdated:]"
+ "-[ACXCompanionSyncConnection fetchRemovabilityForRemoteApps]"
+ "-[ACXDeviceConnectionClient applicationRemovabilityOnDeviceWithPairingID:completion:]"
+ "-[ACXLocalAppRemovabilityManager _onQueue_handleRemovabilityChangedNotification:]"
+ "-[ACXLocalAppRemovabilityManager _onQueue_updateRemovabilityInfoAndReturnRemovabilityMap]"
+ "-[ACXLocalAppRemovabilityManager init]_block_invoke"
+ "-[ACXRemoteAppRemovabilityManager _onQueue_hasRemoteChangeClockUpdatedForUUID:sequenceNumber:]"
+ "-[ACXRemoteAppRemovabilityManager _onQueue_saveData]"
+ "-[ACXRemoteAppRemovabilityManager initWithCoder:]"
+ "-[ACXRemoteAppRemovabilityManager removabilityUpdatedForApp:removability:dbUUID:sequenceNumber:]_block_invoke"
+ "-[ACXRemoteAppRemovabilityManager setRemoteRemovabilityData:withDBUUID:sequenceNumber:]_block_invoke"
+ "1"
+ "10.3"
+ "@\"<ACXRemoteRemovabilityCommunications>\""
+ "@\"ACXRemoteAppRemovabilityManager\""
+ "@\"IXDataStoreClock\""
+ "ACXLocalAppRemovabilityManager"
+ "ACXRemoteAppRemovabilityManager"
+ "ACXRemoteRemovability.plist"
+ "ACXRemoteRemovabilityCommunications"
+ "B32@0:8@16Q24"
+ "Calling all removability changed observers"
+ "Creating new remote removability list"
+ "Dec 20 2023"
+ "Failed to deserialize remote removability list"
+ "Failed to fetch local removability info. Skipping requesting remote removability."
+ "Failed to get app removability list encoded data from %@ : %@"
+ "Failed to initialize remote apps removability manager for pairing store %@"
+ "Failed to retrieve app removability data: %@"
+ "Got app removability updated message without a bundle ID: %@"
+ "Got app removability updated message without db uuid for change clock: %@"
+ "Got app removability updated message without removability value: %@"
+ "Got app removability updated message without sequence number for change clock: %@"
+ "Got error when sending remote removability query message to %@ : %@"
+ "Got remote removability fetch response but it didn't contain removability list : %@"
+ "Ignoring remote removability fetch request for %@ because already one is going on."
+ "Ignoring remote removability fetch request for %@ because it is not reachable."
+ "RA"
+ "RS"
+ "RU"
+ "Received app removability updated message for bundleID: %@ removability: %@ dbUUID: %@ sequenceNo: %@"
+ "Received delayed removability changed notification for %@ : %lu. Remote clock sequence no: %lu. Synced remote clock sequence number: %lu. Ignoring it."
+ "Received notification for change in removability: %@"
+ "Received removability info: %@ with associated remote clock %@ : %@"
+ "Received spurious removability changed notification for %@ : %lu. Local removability value: %@. Remote clocks is in sync. Ignoring it"
+ "Remote change clock uuid has changed from %@ to %@. This is very odd."
+ "Remote removability change clock has advanced by more than 1: %lu"
+ "Remote removability clock has gone backwards. Remote clock sequence no: %lu. Synced remote clock sequence number: %lu. Remote removability map: %@. Local removability map: %@. Ignoring it."
+ "Remote removability fetch called on a device not supporting removability"
+ "Remote removability fetch message was not successfully sent after 5 tries."
+ "RemoteRemovabilityVersion"
+ "Removability store at init, apps marked with removability values: %@ changeClock: %@"
+ "Retrying remote removability fetch in 5 seconds..."
+ "Sending removability changed notification: %@"
+ "T@\"<ACXRemoteRemovabilityCommunications>\",W,N,V_delegate"
+ "T@\"ACXRemoteAppRemovabilityManager\",&,N,V_remoteRemovabilityManager"
+ "T@\"IXDataStoreClock\",&,N,V_removabilityChangeClock"
+ "T@\"NSDictionary\",&,N,V_appRemovabilityMap"
+ "T@\"NSObject<OS_dispatch_queue>\",R,N,V_observerQueue"
+ "T@\"NSUUID\",&,N,V_currentClockUUID"
+ "TB,N,V_remoteRemovabilityFetchRunning"
+ "TB,R,N,V_supportsTrackingAppRemovability"
+ "This device does not support tracking app removability: %@"
+ "_appRemovabilityMap"
+ "_currentClockUUID"
+ "_observerQueue"
+ "_onQueue_configureRemoteRemovabilityManagerAndFetchRemoteRemovabilityStatus"
+ "_onQueue_fetchRemovabilityForRemoteApps"
+ "_onQueue_fetchRemovabilityForRemoteAppsWithRetryCount:"
+ "_onQueue_handleAppRemovabilityUpdatedMessage:"
+ "_onQueue_handleRemoteRemovabilityFetchResponse:"
+ "_onQueue_handleRemovabilityChangedNotification:"
+ "_onQueue_hasRemoteChangeClockUpdatedForUUID:sequenceNumber:"
+ "_onQueue_updateRemovabilityInfoAndReturnRemovabilityMap"
+ "_remoteRemovabilityFetchRunning"
+ "_remoteRemovabilityManager"
+ "_removabilityChangeClock"
+ "_supportsTrackingAppRemovability"
+ "addObserver:selector:name:object:"
+ "appRemovabilityMap"
+ "applicationRemovabilityOnDeviceWithPairingID:completion:"
+ "applicationsRemovabilityUpdated:"
+ "com.apple.AppConduit.ACXRemoteRemovabilityManager"
+ "com.apple.appconduit.ACXLocalRemovabilityObserver"
+ "com.apple.appconduit.removabilitySyncManagerQueue"
+ "com.apple.appconduitd.RetryRemovabilityForRemoteAppsFetch"
+ "currentClockUUID"
+ "fetchCurrentRemovabilityStoreUUID:sequenceNumber:"
+ "fetchRemovabilityForRemoteApps"
+ "getRemovabilityForAllAppsWithStoreUUID:sequenceNumber:"
+ "guid"
+ "isEqualToNumber:"
+ "noteRemovabilityUpdated:forApp:dataStoreUUID:sequenceNumber:"
+ "observerQueue"
+ "remote removability fetch"
+ "remoteRemovabilityFetchRunning"
+ "remoteRemovabilityManager"
+ "remoteRemovabilityManagerForStorageBaseURL:delegate:queue:"
+ "removability"
+ "removabilityChangeClock"
+ "removabilityDataWithChangeClock:error:"
+ "removabilityForRemoteApps"
+ "removabilityUpdatedForApp:removability:dbUUID:sequenceNumber:"
+ "removeDelegate:"
+ "reportRemoteRemovabilityDBUUID:sequenceNumber:"
+ "setAppRemovabilityMap:"
+ "setCurrentClockUUID:"
+ "setRemoteRemovabilityData:withDBUUID:sequenceNumber:"
+ "setRemoteRemovabilityFetchRunning:"
+ "setRemoteRemovabilityManager:"
+ "setRemovabilityChangeClock:"
+ "supportsTrackingAppRemovability"
+ "updateRemovabilityInfoAndReturnRemovabilityMap:"
+ "v24@0:8@\"NSDictionary\"16"
+ "v32@?0@\"IXApplicationIdentity\"8@\"IXAppRemovabilityMetadata\"16^B24"
+ "v48@0:8@16Q24@32Q40"
+ "valueForKey:"
- "\x18"
- "Nov 12 2023"

```
