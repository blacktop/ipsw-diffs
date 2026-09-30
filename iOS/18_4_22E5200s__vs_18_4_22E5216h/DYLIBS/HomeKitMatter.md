## HomeKitMatter

> `/System/Library/PrivateFrameworks/HomeKitMatter.framework/HomeKitMatter`

```diff

-1277.0.0.1.2
-  __TEXT.__text: 0x12e81c
-  __TEXT.__auth_stubs: 0xa10
-  __TEXT.__objc_methlist: 0x9a94
+1278.5.8.2.0
+  __TEXT.__text: 0x12fe2c
+  __TEXT.__auth_stubs: 0xa40
+  __TEXT.__objc_methlist: 0x9b0c
   __TEXT.__const: 0x158
   __TEXT.__dlopen_cstrs: 0x58
-  __TEXT.__gcc_except_tab: 0x2a60
-  __TEXT.__cstring: 0x6158
-  __TEXT.__oslogstring: 0x250d5
+  __TEXT.__gcc_except_tab: 0x2abc
+  __TEXT.__cstring: 0x61b7
+  __TEXT.__oslogstring: 0x253b0
   __TEXT.__ustring: 0x68
-  __TEXT.__unwind_info: 0x2c00
-  __TEXT.__objc_classname: 0x1338
-  __TEXT.__objc_methname: 0x2340f
-  __TEXT.__objc_methtype: 0x3789
-  __TEXT.__objc_stubs: 0x15180
+  __TEXT.__unwind_info: 0x2c40
+  __TEXT.__objc_classname: 0x1337
+  __TEXT.__objc_methname: 0x23578
+  __TEXT.__objc_methtype: 0x3782
+  __TEXT.__objc_stubs: 0x152a0
   __DATA_CONST.__got: 0x990
-  __DATA_CONST.__const: 0x4308
+  __DATA_CONST.__const: 0x4368
   __DATA_CONST.__objc_classlist: 0x3e8
   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0x120
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x65d0
+  __DATA_CONST.__objc_selrefs: 0x6630
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x2c8
   __DATA_CONST.__objc_arraydata: 0x228
-  __AUTH_CONST.__auth_got: 0x518
-  __AUTH_CONST.__const: 0xe80
-  __AUTH_CONST.__cfstring: 0x6600
-  __AUTH_CONST.__objc_const: 0xe938
+  __AUTH_CONST.__auth_got: 0x530
+  __AUTH_CONST.__const: 0xf20
+  __AUTH_CONST.__cfstring: 0x6620
+  __AUTH_CONST.__objc_const: 0xe918
   __AUTH_CONST.__objc_intobj: 0x15d8
   __AUTH_CONST.__objc_arrayobj: 0x180
   __AUTH_CONST.__objc_doubleobj: 0x20

   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/HomeKit.framework/HomeKit
   - /System/Library/Frameworks/Matter.framework/Matter
   - /System/Library/Frameworks/MatterSupport.framework/MatterSupport
   - /System/Library/Frameworks/Network.framework/Network

   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 4026
-  Symbols:   4782
-  CStrings:  8153
+  Functions: 4045
+  Symbols:   4804
+  CStrings:  8176
 
Symbols:
+ _objc_retain_x7
+ _objc_sync_enter
+ _objc_sync_exit
CStrings:
+ "\x01\x16!\x119\x15\x11\x16\x1e"
+ "%{public}@Handling remove from browser"
+ "%{public}@Overriding linkLayerType unknown -> thread for nodeID %@"
+ "%{public}@Removing active clients fabricUUIDs: %@"
+ "%{public}@Removing fabrics with secondary clients fabricUUIDs: %@"
+ "%{public}@Retrieved controller %@ for fabric UUID %@ upon setting the startup parameters"
+ "%{public}@Stopping thread due to user logout"
+ "%{public}@[Flow: %@] Existing guest with schedule already exists on the lock, just return the user response"
+ "%{public}@[Flow: %@] Found user on index verify userUniqueID %@"
+ "%{public}@_handleThreadRadioStateChanged - requiresThreadRouter = %@ (isWED = %@, isControllerInSleepyRouterState = %@)"
+ "%{public}@configureDefaultRequiresThreadRouter - accessory requires thread router = %@ (isAccessoryServerThreadCapable = %@, isDeviceThreadCapable = %@, isWEDDevice = %@"
+ "%{public}@deviceActivityState change - goOffline=%@, reason=%ld, current active fabric %@"
+ "%{public}@handleThreadDirectConnectionSleepyTypeChange - requiresThreadRouter = %@ for accessory with nodeID %@ (isWED = %@, isSleepyLink = %@)"
+ "%{public}@isReadyToEstablishWEDConnection - Thread is not active"
+ "%{public}@isReadyToTransitionToFullRouterModeForFirmwareUpdate - Thread is not active"
+ "%{public}@isThreadNetworkConnected - Thread is not active"
+ "%{public}@stopping thread even though preventDisconnect is true due to logout"
+ "@44@0:8q16B24@28@36"
+ "@52@0:8@16@24@32B40@44"
+ "@72@0:8@16q24q32@40@48@56@64"
+ "B16@?0@\"HAPService\"8"
+ "B32@?0@\"HMMTRControllerWrapperRevokeHandlerInfo\"8Q16^B24"
+ "__getUserAtIndex:includeAliroCredentials:temporaryCachedAliroCredentials:flow:"
+ "_handleLogoutNotification"
+ "_removeOrSuspendAllActiveClientsWithCurrentFabricUUID:reason:"
+ "_resumeSuspendedActiveClients"
+ "_suspendedActiveClientFabricUUID"
+ "_suspendedActiveSecondaryClientFabricUUIDs"
+ "addSuspendedActiveSecondaryClientFabricUUIDs:"
+ "aliroCredentials"
+ "clearSuspendedActiveSecondaryClientFabricUUIDs"
+ "configureDefaultRequiresThreadRouter"
+ "deregisterRevokeHandlersWithQueue:"
+ "findAllUsersWithCreatorFabricIndex:indexStartingAtSlot:assumingTotalNumberOfSlots:users:temporaryCachedAliroCredentials:flow:"
+ "findHomeUserWithUniqueID:indexStartingAtSlot:assumingTotalNumberOfSlots:availableSlots:currentFabricIndex:temporaryCachedAliroCredentials:flow:"
+ "findOrAddUserWithUniqueID:withWeekDaySchedules:andYearDaySchedules:requireFullScheduleAudit:flow:"
+ "getUserWithParams:includeAliroCredentials:temporaryCachedAliroCredentials:flow:completion:"
+ "handleRemoveFromBrowser"
+ "hapErrorWithCode:marker:"
+ "indexesOfObjectsPassingTest:"
+ "removeObjectsAtIndexes:"
+ "setSuspendedActiveClientFabricUUID:"
+ "stopThreadOnUserLogout"
+ "supportedLinkLayerTypesContainsEthernet:"
+ "supportedLinkLayerTypesContainsThread:"
+ "supportedLinkLayerTypesContainsWiFi:"
+ "suspendedActiveClientFabricUUID"
+ "suspendedActiveSecondaryClientFabricUUIDs"
+ "updateAccessory:withServices:"
+ "v52@0:8@16B24@28@36@?44"
+ "\x91\xf1Q"
- "\x01\x14!\x11I\x15\x11\x16\x1e"
- "%{public}@Per-controller storage is not enabled to configure controller for fabric ID %@ upfront"
- "%{public}@Removing fabric %@ from active clients and aborting operations"
- "%{public}@Thread is not active"
- "%{public}@_handleThreadRadioStateChanged - requiresThreadRouter = %@ (isWED = %@, isControllerInSleepyRouterState = %@, primaryReachableAndThreadCapable = %@)"
- "%{public}@configuring controller for fabric %@ with fabric ID %@"
- "%{public}@handleThreadDirectConnectionSleepyTypeChange - requiresThreadRouter = %@ for accessory with nodeID %@ (isWED = %@, isSleepyLink = %@, primaryReachableAndThreadCapable = %@)"
- "@44@0:8q16B24^@28@36"
- "@64@0:8@16q24q32@40^@48@56"
- "@72@0:8@16q24q32@40@48^@56@64"
- "TB,V_lockStateKBNotificationRegistered"
- "Ti,V_lockStateKBNotificationRegistrationToken"
- "__getUserAtIndex:includeAliroCredentials:aliroCredentials:flow:"
- "_lockStateKBNotificationRegistered"
- "_lockStateKBNotificationRegistrationToken"
- "configureControllerForFabric:"
- "findAllUsersWithCreatorFabricIndex:indexStartingAtSlot:assumingTotalNumberOfSlots:users:aliroCredentials:flow:"
- "findHomeUserWithUniqueID:indexStartingAtSlot:assumingTotalNumberOfSlots:availableSlots:currentFabricIndex:aliroCredentials:flow:"
- "findOrAddUserWithUniqueID:withWeekDaySchedules:andYearDaySchedules:flow:"
- "getUserWithParams:includeAliroCredentials:aliroCredentials:flow:completion:"
- "isCurrentDeviceMobileAndResidentReachableAndThreadCapableForFabric:"
- "isPrimaryResidentNodeReachableAndThreadCapable"
- "lockStateKBNotificationRegistered"
- "lockStateKBNotificationRegistrationToken"
- "q\xf0\x11Q"
- "setLockStateKBNotificationRegistered:"
- "setLockStateKBNotificationRegistrationToken:"
- "v52@0:8@16B24^@28@36@?44"

```
