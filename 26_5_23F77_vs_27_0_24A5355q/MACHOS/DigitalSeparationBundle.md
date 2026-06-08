## DigitalSeparationBundle

> `/System/Library/DigitalSeparation/SharingSources/DigitalSeparationBundle.bundle/DigitalSeparationBundle`

```diff

-1418.6.20.0.0
-  __TEXT.__text: 0x59b0
-  __TEXT.__auth_stubs: 0x300
+1468.5.0.0.6
+  __TEXT.__text: 0x5eb0
+  __TEXT.__auth_stubs: 0x350
   __TEXT.__objc_stubs: 0xd40
   __TEXT.__objc_methlist: 0x73c
-  __TEXT.__const: 0x20
+  __TEXT.__const: 0x30
   __TEXT.__objc_methname: 0x1266
-  __TEXT.__objc_classname: 0xf7
+  __TEXT.__objc_classname: 0xeb
   __TEXT.__objc_methtype: 0x5f4
-  __TEXT.__cstring: 0x2bb
-  __TEXT.__oslogstring: 0x8eb
-  __TEXT.__unwind_info: 0x188
-  __DATA_CONST.__auth_got: 0x188
-  __DATA_CONST.__got: 0x90
+  __TEXT.__cstring: 0x2c7
+  __TEXT.__oslogstring: 0x10f6
+  __TEXT.__unwind_info: 0x190
   __DATA_CONST.__const: 0x4f0
   __DATA_CONST.__cfstring: 0x160
   __DATA_CONST.__objc_classlist: 0x38

   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x30
+  __DATA_CONST.__auth_got: 0x1b0
+  __DATA_CONST.__got: 0x90
   __DATA.__objc_const: 0xf18
   __DATA.__objc_selrefs: 0x4e0
   __DATA.__objc_ivar: 0x50

   - /System/Library/Frameworks/HomeKit.framework/HomeKit
   - /System/Library/PrivateFrameworks/DigitalSeparation.framework/DigitalSeparation
   - /System/Library/PrivateFrameworks/HMFoundation.framework/HMFoundation
-  - /System/Library/PrivateFrameworks/MobileStoreDemoKit.framework/MobileStoreDemoKit
   - /System/Library/PrivateFrameworks/NetAppsUtilities.framework/NetAppsUtilities
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 8D13D838-9EC4-38A9-9E49-95CCDCD5802B
+  UUID: 55B8A96D-423F-30D8-86EA-D4611718BC28
   Functions: 108
-  Symbols:   76
-  CStrings:  361
+  Symbols:   81
+  CStrings:  393
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x28
+ _objc_retain_x3
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x26
CStrings:
+ "Calling completion after fetching shared resources: %@, with error: %@"
+ "Calling completion after stopping all sharing with error: %@"
+ "Calling completion after stopping sharing resource: %@ with error: %@"
+ "Calling completion after stopping sharing with participant: %@ with error: %@"
+ "Calling completion with DSSourceErroriCloudDisabled error because Home iCloud switch is disabled. Status: %@, DataSyncState: %@"
+ "Calling completion with empty array because home manager is not ready, but it is not clear that we are in an error state. Status: %@, DataSyncState: %@"
+ "Calling completion with error because home manager is not ready. Status: %@, DataSyncState: %@"
+ "Calling completion with error because we failed to refresh the home manager with error: %@"
+ "Cannot remove participant object: %@"
+ "Creating shared resource for home: %@"
+ "Failed to remove access code: %@"
+ "Fetching shared resources"
+ "Found homes: %@"
+ "Found participant in home but cannot remove them because we do not have sufficient privileges. Home: %@, participantObject: %@"
+ "Home has participants: %@, accessCodes: %@"
+ "Invalid identity on participant: %@"
+ "Invalid shared resource: %@"
+ "Participant home no longer exists with homeUniqueIdentifier: %@"
+ "Participant is not in home: %@ participant: %@"
+ "Participant object has all nil properties: %@"
+ "Received did update homes callback"
+ "Removing access code participant from home: %@, participantObject: %@"
+ "Removing all participants that we have authority to remove from home: %@"
+ "Removing outgoing invitation participant from home: %@, participantObject: %@"
+ "Removing user participant from home: %@, participantObject: %@"
+ "Stopping all sharing"
+ "Stopping sharing resource: %@"
+ "Stopping sharing with participant: %@"
+ "There are no users we can remove, so not creating a shared resource for home: %@"
+ "Unrecognized participant: %@"
+ "We do not have admin privileges, so not creating a shared resource for home: %@"
+ "We do not have admin privileges, so we cannot remove anyone from the home: %@"
+ "[%{public}@] Calling completion after fetching shared resources: %@, with error: %@"
+ "[%{public}@] Calling completion after stopping all sharing with error: %@"
+ "[%{public}@] Calling completion after stopping sharing resource: %@ with error: %@"
+ "[%{public}@] Calling completion after stopping sharing with participant: %@ with error: %@"
+ "[%{public}@] Calling completion with DSSourceErroriCloudDisabled error because Home iCloud switch is disabled. Status: %@, DataSyncState: %@"
+ "[%{public}@] Calling completion with empty array because home manager is not ready, but it is not clear that we are in an error state. Status: %@, DataSyncState: %@"
+ "[%{public}@] Calling completion with error because home manager is not ready. Status: %@, DataSyncState: %@"
+ "[%{public}@] Calling completion with error because we failed to refresh the home manager with error: %@"
+ "[%{public}@] Cannot remove participant object: %@"
+ "[%{public}@] Creating shared resource for home: %@"
+ "[%{public}@] Failed to remove access code: %@"
+ "[%{public}@] Fetching shared resources"
+ "[%{public}@] Found homes: %@"
+ "[%{public}@] Found participant in home but cannot remove them because we do not have sufficient privileges. Home: %@, participantObject: %@"
+ "[%{public}@] Home has participants: %@, accessCodes: %@"
+ "[%{public}@] Invalid identity on participant: %@"
+ "[%{public}@] Invalid shared resource: %@"
+ "[%{public}@] Participant home no longer exists with homeUniqueIdentifier: %@"
+ "[%{public}@] Participant is not in home: %@ participant: %@"
+ "[%{public}@] Participant object has all nil properties: %@"
+ "[%{public}@] Received did update homes callback"
+ "[%{public}@] Removing access code participant from home: %@, participantObject: %@"
+ "[%{public}@] Removing all participants that we have authority to remove from home: %@"
+ "[%{public}@] Removing outgoing invitation participant from home: %@, participantObject: %@"
+ "[%{public}@] Removing user participant from home: %@, participantObject: %@"
+ "[%{public}@] Stopping all sharing"
+ "[%{public}@] Stopping sharing resource: %@"
+ "[%{public}@] Stopping sharing with participant: %@"
+ "[%{public}@] There are no users we can remove, so not creating a shared resource for home: %@"
+ "[%{public}@] Unrecognized participant: %@"
+ "[%{public}@] We do not have admin privileges, so not creating a shared resource for home: %@"
+ "[%{public}@] We do not have admin privileges, so we cannot remove anyone from the home: %@"
- "%{public}@Calling completion after fetching shared resources: %@, with error: %@"
- "%{public}@Calling completion after stopping all sharing with error: %@"
- "%{public}@Calling completion after stopping sharing resource: %@ with error: %@"
- "%{public}@Calling completion after stopping sharing with participant: %@ with error: %@"
- "%{public}@Calling completion with DSSourceErroriCloudDisabled error because Home iCloud switch is disabled. Status: %@, DataSyncState: %@"
- "%{public}@Calling completion with empty array because home manager is not ready, but it is not clear that we are in an error state. Status: %@, DataSyncState: %@"
- "%{public}@Calling completion with error because home manager is not ready. Status: %@, DataSyncState: %@"
- "%{public}@Calling completion with error because we failed to refresh the home manager with error: %@"
- "%{public}@Cannot remove participant object: %@"
- "%{public}@Creating shared resource for home: %@"
- "%{public}@Failed to remove access code: %@"
- "%{public}@Fetching shared resources"
- "%{public}@Found homes: %@"
- "%{public}@Found participant in home but cannot remove them because we do not have sufficient privileges. Home: %@, participantObject: %@"
- "%{public}@Home has participants: %@, accessCodes: %@"
- "%{public}@Invalid identity on participant: %@"
- "%{public}@Invalid shared resource: %@"
- "%{public}@Participant home no longer exists with homeUniqueIdentifier: %@"
- "%{public}@Participant is not in home: %@ participant: %@"
- "%{public}@Participant object has all nil properties: %@"
- "%{public}@Received did update homes callback"
- "%{public}@Removing access code participant from home: %@, participantObject: %@"
- "%{public}@Removing all participants that we have authority to remove from home: %@"
- "%{public}@Removing outgoing invitation participant from home: %@, participantObject: %@"
- "%{public}@Removing user participant from home: %@, participantObject: %@"
- "%{public}@Stopping all sharing"
- "%{public}@Stopping sharing resource: %@"
- "%{public}@Stopping sharing with participant: %@"
- "%{public}@There are no users we can remove, so not creating a shared resource for home: %@"
- "%{public}@Unrecognized participant: %@"
- "%{public}@We do not have admin privileges, so not creating a shared resource for home: %@"
- "%{public}@We do not have admin privileges, so we cannot remove anyone from the home: %@"

```
