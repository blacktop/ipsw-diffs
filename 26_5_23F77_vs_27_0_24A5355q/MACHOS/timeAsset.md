## timeAsset

> `/System/Library/PrivateFrameworks/CoreTime.framework/TimeSources/timeAsset.bundle/timeAsset`

```diff

-1.0.0.0.0
-  __TEXT.__text: 0x17a0
-  __TEXT.__auth_stubs: 0x150
-  __TEXT.__objc_stubs: 0x5c0
-  __TEXT.__objc_methlist: 0x2c4
-  __TEXT.__objc_methname: 0x811
-  __TEXT.__cstring: 0x11d
+2.0.0.0.0
+  __TEXT.__text: 0x193c
+  __TEXT.__auth_stubs: 0x180
+  __TEXT.__objc_stubs: 0x620
+  __TEXT.__objc_methlist: 0x2dc
+  __TEXT.__objc_methname: 0x994
+  __TEXT.__cstring: 0x164
   __TEXT.__objc_classname: 0x43
-  __TEXT.__objc_methtype: 0x269
-  __TEXT.__oslogstring: 0x455
-  __TEXT.__const: 0x20
-  __TEXT.__unwind_info: 0xc8
-  __DATA_CONST.__auth_got: 0xb0
-  __DATA_CONST.__got: 0x50
-  __DATA_CONST.__const: 0xc8
-  __DATA_CONST.__cfstring: 0x160
+  __TEXT.__objc_methtype: 0x284
+  __TEXT.__oslogstring: 0x515
+  __TEXT.__const: 0x50
+  __TEXT.__unwind_info: 0xd0
+  __DATA_CONST.__const: 0x130
+  __DATA_CONST.__cfstring: 0x1c0
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x18
-  __DATA.__objc_const: 0x570
-  __DATA.__objc_selrefs: 0x270
-  __DATA.__objc_ivar: 0x30
+  __DATA_CONST.__auth_got: 0xc8
+  __DATA_CONST.__got: 0x50
+  __DATA.__objc_const: 0x5c8
+  __DATA.__objc_selrefs: 0x2a8
+  __DATA.__objc_ivar: 0x38
   __DATA.__objc_data: 0xf0
   __DATA.__data: 0xc0
-  __DATA.__bss: 0x8
+  __DATA.__common: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/CoreTime.framework/CoreTime
   - /System/Library/PrivateFrameworks/MobileAsset.framework/MobileAsset
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: CCBA7E22-FEF4-378E-9914-6E8625D5608E
+  UUID: 7880A8A1-13F5-3B18-86D1-8A0A086917B2
   Functions: 43
-  Symbols:   48
-  CStrings:  187
+  Symbols:   53
+  CStrings:  211
 
Symbols:
+ _OBJC_CLASS_$_MAAutoAssetSet
+ _OBJC_CLASS_$_MAAutoAssetSetEntry
+ _OBJC_CLASS_$_MAAutoAssetSetNotifications
+ _OBJC_CLASS_$_MAAutoAssetSetPolicy
+ _OBJC_CLASS_$_NSArray
+ _OTAAssetInterestReasonGeneral
+ _TMAS_FACILITY
+ __NSConcreteGlobalBlock
+ _objc_release
+ _objc_release_x22
+ _objc_retain_x21
+ _objc_retain_x8
- _OBJC_CLASS_$_MAAutoAsset
- _OBJC_CLASS_$_MAAutoAssetNotifications
- _OBJC_CLASS_$_MAAutoAssetSelector
- _OBJC_CLASS_$_NSMutableDictionary
- _OBJC_CLASS_$_NSNumber
- _OTAAssetInteresetReasonGeneral
- _objc_release_x21
CStrings:
+ "@\"MAAutoAssetSet\""
+ "ALL_INSTANCES"
+ "ATOMIC_INSTANCE_DOWNLOADED"
+ "CoreTime"
+ "TimezoneData"
+ "_assetManager"
+ "_coreTZRules"
+ "arrayWithObjects:count:"
+ "asset"
+ "asset processing failed, will retry after %f seconds"
+ "assetSet"
+ "begin handling atomic instance download for asset: %@"
+ "cleared previous locks for asset set: %@"
+ "code"
+ "copy failed for asset: %@ specifier: %@ source: %@ dest: %@"
+ "copy success for asset: %@ specifier: %@"
+ "copying a file at location %@ failed: %@ (domain: %@ code: %ld)"
+ "count"
+ "didFinishSetupWithCompletionHandler:"
+ "domain"
+ "downloadNotificationToken"
+ "endAtomicLock:ofAtomicInstance:completion:"
+ "endAtomicLocks:usingClientDomain:forClientName:forAssetSetIdentifier:ofAtomicInstance:removingLockCount:completion:"
+ "error creating MAAutoAssetSet: %@ (domain: %@ code: %ld)"
+ "error creating MAAutoAssetSetEntry for type: %@ specifier: %@"
+ "error ending previous locks for %@: %@ (domain: %@ code: %ld)"
+ "error expressing need for asset set %@: %@ (domain: %@ code: %ld)"
+ "expressNeedWithReason:"
+ "failed to lock atomic instance: %@ (domain: %@ code: %ld)"
+ "failed to register for atomic instance notification: %@"
+ "failed to unlock atomic instance %@: %@ (domain: %@ code: %ld)"
+ "fullAssetSelector"
+ "handleAtomicInstanceDownloadedForAsset:"
+ "i"
+ "initUsingClientDomain:forClientName:forAssetSetIdentifier:comprisedOfEntries:error:"
+ "initialized MAAutoAssetSet with identifier: %@"
+ "isEqualToString:"
+ "isFileURL"
+ "localizedDescription"
+ "lockAtomic:forAtomicInstance:withNeedPolicy:withTimeout:reportingProgress:completion:"
+ "locked atomic instance: %@ with %lu entries"
+ "lockedInstanceID"
+ "managedAsset"
+ "needForAtomic:withNeedPolicy:completion:"
+ "notifyRegistrationName:forAssetSetIdentifier:"
+ "path"
+ "received atomic instance downloaded notification for set: %@"
+ "registerForNotificationsForAsset:"
+ "registered for atomic instance notification, token: %d"
+ "replacing a file at location %@ failed: %@ (domain: %@ code: %ld)"
+ "scheduleRetryForAsset:afterInterval:"
+ "scheduling retry after %.0f seconds for asset: %@"
+ "setAllowCheckDownloadOnBattery:"
+ "setAllowCheckDownloadOverCellular:"
+ "setAllowCheckDownloadOverExpensive:"
+ "setUserInitiated:"
+ "startPeerSyncClientWithCompletionHandler:"
+ "startPeerSyncServerWithCompletionHandler:"
+ "success expressing need for asset set: %@"
+ "successfully unlocked atomic instance: %@"
+ "timezone-rules-usage"
+ "unlockAtomicInstance"
+ "unlocking atomic instance: %@"
+ "v24@0:8@?16"
+ "v24@0:8@?<v@?@\"NSError\">16"
+ "v24@?0@\"NSString\"8@\"NSError\"16"
+ "v32@0:8@16d24"
+ "v32@?0@\"NSString\"8@\"NSArray\"16@\"NSError\"24"
- "@\"NSMutableDictionary\""
- "@\"NSObject<OS_os_log>\""
- "ASSET_VERSION_DOWNLOADED"
- "MAAutoAsset not locked: %@"
- "MAAutoAsset not unlocked: %@"
- "absoluteString"
- "adding registration for assetHandle %@ token: %d"
- "allKeys"
- "assetManager"
- "assetSelector"
- "begin handler execution for asset: %@ specifier: %@"
- "containsObject:"
- "copy attempt success for asset: %@ specifier: %@"
- "copying a file at location %@ failed. Error %@"
- "coreTZRules"
- "endAllPreviousLocksOfSelector:forClientName:completion:"
- "endLockUsageSync:"
- "error creating MAAutoAsset object for type: %@ specifier %@ in response to monitor change notification: %@"
- "error creating MAAutoAssetSelector for MAAutoAsset type: %@ specifier: %@"
- "error ending previous locks for MAAutoAsset type: %@ specifier: %@: %@"
- "error expressing interest in assetType: %@ with specifier: %@: %@"
- "error processing asset with type: %@ specifier: %@, will try again after %f seconds"
- "expressInterestForSelector:withInterestReason:"
- "failed to register for new asset notification: %@"
- "handleAssetAvailable:fromAsset:"
- "initForClientName:selectingAsset:error:"
- "intValue"
- "interestInContent:forAssetSelector:completion:"
- "lock attempt success for asset: %@ specifier: %@"
- "lockAsset:"
- "lockContentSync:withTimeout:lockedAssetSelector:newerInProgress:error:"
- "logs"
- "moving asset"
- "notifyRegistrationName:forAssetType:forAssetSpecifier:"
- "numberWithInt:"
- "objectForKeyedSubscript:"
- "processAutoAsset:fromAsset:"
- "registerForChangedNotificationsForAsset:selector:"
- "registration already present for this assetHandle: %@ token: %d"
- "registrations"
- "replacing a file at location %@ failed. Error %@"
- "setValue:forKey:"
- "success expressing interest in assetType: %@ with specifier: %@"
- "unlock attempt success for asset: %@ specifier: %@"
- "unlockAsset:"
- "v24@?0@\"MAAutoAssetSelector\"8@\"NSError\"16"

```
