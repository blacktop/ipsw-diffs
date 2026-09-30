## FindMyDeviceHelperXPCService

> `/System/Library/PrivateFrameworks/FindMyDevice.framework/XPCServices/FindMyDeviceHelperXPCService.xpc/FindMyDeviceHelperXPCService`

```diff

-438.35.2.11.19
-  __TEXT.__text: 0xd360
-  __TEXT.__auth_stubs: 0x600
-  __TEXT.__objc_stubs: 0x2520
-  __TEXT.__objc_methlist: 0xc84
-  __TEXT.__objc_methname: 0x2728
-  __TEXT.__cstring: 0x222f
-  __TEXT.__objc_classname: 0x1e4
-  __TEXT.__objc_methtype: 0x861
-  __TEXT.__const: 0x120
-  __TEXT.__gcc_except_tab: 0x178
-  __TEXT.__oslogstring: 0x1aca
-  __TEXT.__unwind_info: 0x2e0
-  __DATA_CONST.__auth_got: 0x310
-  __DATA_CONST.__got: 0x218
-  __DATA_CONST.__const: 0x1078
-  __DATA_CONST.__cfstring: 0x2d20
-  __DATA_CONST.__objc_classlist: 0x68
+452.30.5.13.0
+  __TEXT.__text: 0xa1ec
+  __TEXT.__auth_stubs: 0x4a0
+  __TEXT.__objc_stubs: 0x1f20
+  __TEXT.__objc_methlist: 0x98c
+  __TEXT.__const: 0x100
+  __TEXT.__gcc_except_tab: 0xb4
+  __TEXT.__objc_methname: 0x1ff7
+  __TEXT.__oslogstring: 0x112c
+  __TEXT.__cstring: 0x20cd
+  __TEXT.__objc_classname: 0x199
+  __TEXT.__objc_methtype: 0x63b
+  __TEXT.__unwind_info: 0x228
+  __DATA_CONST.__auth_got: 0x260
+  __DATA_CONST.__got: 0x210
+  __DATA_CONST.__const: 0xf28
+  __DATA_CONST.__cfstring: 0x2ca0
+  __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_catlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x48
+  __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x20
+  __DATA_CONST.__objc_superrefs: 0x10
   __DATA_CONST.__objc_arraydata: 0x130
   __DATA_CONST.__objc_arrayobj: 0x30
   __DATA_CONST.__objc_doubleobj: 0x10
   __DATA_CONST.__objc_intobj: 0x48
-  __DATA.__objc_const: 0x1e18
-  __DATA.__objc_selrefs: 0xae0
-  __DATA.__objc_ivar: 0xc0
-  __DATA.__objc_data: 0x410
-  __DATA.__data: 0x448
+  __DATA.__objc_const: 0x1990
+  __DATA.__objc_selrefs: 0x938
+  __DATA.__objc_ivar: 0x84
+  __DATA.__objc_data: 0x370
+  __DATA.__data: 0x388
   __DATA.__common: 0x8
   __DATA.__bss: 0x158
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox
+  - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreLocation.framework/CoreLocation
   - /System/Library/Frameworks/CoreMedia.framework/CoreMedia
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/BiometricKit.framework/BiometricKit
-  - /System/Library/PrivateFrameworks/BluetoothManager.framework/BluetoothManager
   - /System/Library/PrivateFrameworks/FMCore.framework/FMCore
   - /System/Library/PrivateFrameworks/FMCoreLite.framework/FMCoreLite
   - /System/Library/PrivateFrameworks/FindMyDevice.framework/FindMyDevice
   - /System/Library/PrivateFrameworks/MediaExperience.framework/MediaExperience
-  - /System/Library/PrivateFrameworks/MobileBluetooth.framework/MobileBluetooth
   - /System/Library/PrivateFrameworks/NearField.framework/NearField
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 5D73426F-E010-353B-B344-043BC3F05D97
-  Functions: 337
-  Symbols:   178
-  CStrings:  1471
+  UUID: 880699E0-148D-31CA-8216-6A3DD686D77D
+  Functions: 243
+  Symbols:   153
+  CStrings:  1297
 
Symbols:
- _BTAccessoryManagerAddCallbacks
- _BTAccessoryManagerGetControlCommand
- _BTAccessoryManagerGetDefault
- _BTAccessoryManagerRemoveCallbacks
- _BTAccessoryManagerSendControlCommand
- _BTDeviceAddressFromString
- _BTDeviceFromAddress
- _BTLocalDeviceAddCallbacks
- _BTLocalDeviceGetDefault
- _BTLocalDeviceRemoveCallbacks
- _BTServiceAddCallbacks
- _BTServiceRemoveCallbacks
- _BTSessionAttachWithQueue
- _BTSessionDetachWithQueue
- _OBJC_CLASS_$_FMDLostModeInfo
- _OBJC_CLASS_$_FMFuture
- _OBJC_METACLASS_$_FMDLostModeInfo
- __Block_object_dispose
- _dispatch_assert_queue$V2
- _dispatch_queue_create
- _dispatch_semaphore_create
- _dispatch_semaphore_signal
- _dispatch_semaphore_wait
- _dispatch_sync
- _objc_opt_respondsToSelector
CStrings:
+ "FMDAccessoryAudioController: Original state - volume: %f"
+ "X"
+ "group.com.apple.icloud.findmydeviced"
- "3"
- "@\"FMDBluetoothSessionInterface\""
- "@\"FMFuture\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@24@0:8@\"NSCoder\"16"
- "ADMobileBluetoothDeviceDataSource"
- "Already attaching to session. Ignoring new request."
- "Attaching to session..."
- "Attempting to set listening mode for accessory address: %@"
- "Callback for BTAccessoryEvent %u"
- "Callback for BTLocalDeviceStatusEvent %u"
- "Callback for BTServiceEvent %u"
- "Callback for BTSessionEvent %u"
- "Cannot get BTDevice: No session. Address: %@"
- "Detached session is not the active session. Ignoring."
- "Detaching from session %p"
- "Error in bluetooth session interface, detaching. Pending actions have been discarded. %@"
- "FMDAccessoryAudioController restoring listening mode %u for accessory %@"
- "FMDAccessoryAudioController unable to restore unknown listening mode %u for accessory %@"
- "FMDAccessoryAudioController: Original state - volume: %f listeningMode: %u"
- "FMDBluetoothSessionInterface"
- "FMDBluetoothSessionInterfaceErrorDomain"
- "FMDLostModeInfo"
- "FMDLostModeInfo(0x%lx) message - %@, phoneNum - %@, facetimeCapable - %d, footnote - %@, inLostMode - %d, disableUnlock - %d, type - %ld"
- "Failed adding callbacks to accessory manager %p from session: %p, result: %d"
- "Failed adding callbacks to local device %p from session %p. Result: %d."
- "Failed attaching to session %d"
- "Failed getting BTDevice address from address string %@ %d"
- "Failed getting BTDevice address from nil / empty address string."
- "Failed getting BTDevice from BTDeviceAddress %@ %d"
- "Failed getting default accessory manager from session: %p, result: %d"
- "Failed getting default local device from session %p. Result: %d."
- "Failed to get btdevice for listening mode using accessory address: %@"
- "Failed to get listening mode for accessory address: %@ | result: %d"
- "Failed to set listening mode for accessory address: %@ | result: %d"
- "Failed to set up accessory manager. Missing session."
- "Failed to set up local device. Missing session."
- "Failed to update btdevice listening mode on accessory address: %@"
- "Finished setup of accessory manager %p"
- "Found BTDevice at address %@"
- "Got listening mode for accessory address: %@ | mode: %u"
- "Initialized FMDBluetoothSessionInterface"
- "Local device set up."
- "NSCoding"
- "NSSecureCoding"
- "No accessory manager to tear-down."
- "No local device to tear-down."
- "Q"
- "Registered session callbacks %p"
- "Retrieving listening mode for accessory address: %@ | timeout: %f"
- "Session attached %p, result: %d."
- "Session detached %p"
- "Session failed to attach: %u"
- "Session is active. Executing client request block."
- "Session requested detach, but we had no session. Nothing to do."
- "Session started by client. [warmup complete]"
- "Session terminated %p"
- "Set listening mode for accessory address: %@ | mode: %u"
- "T@\"FMDBluetoothSessionInterface\",&,N,V_bluetoothSessionInterface"
- "T@\"FMFuture\",&,N,V_futureSession"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_bluetoothSessionQueue"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_serialQueue"
- "T@\"NSString\",&,N,V_footnoteText"
- "T@\"NSString\",&,N,V_message"
- "T@\"NSString\",&,N,V_phoneNumber"
- "TB,N,V_disableSlideToUnlock"
- "TB,N,V_facetimeCapable"
- "TB,N,V_lostModeEnabled"
- "TB,R"
- "TQ,N,V_lostModeType"
- "T^{BTAccessoryManagerImpl=},N,V_accessoryManager"
- "T^{BTLocalDeviceImpl=},N,V_localDevice"
- "T^{BTSessionImpl=},N,V_session"
- "Tear-down finished for accessory manager: %p"
- "Tear-down finished for local device: %p"
- "Terminated session is not the active session. Ignoring."
- "Ti,N,V_listeningMode"
- "Timeout getting listening mode for accessory address: %@"
- "^{BTAccessoryManagerImpl=}"
- "^{BTAccessoryManagerImpl=}16@0:8"
- "^{BTDeviceImpl=}24@0:8@16"
- "^{BTLocalDeviceImpl=}"
- "^{BTLocalDeviceImpl=}16@0:8"
- "^{BTSessionImpl=}"
- "^{BTSessionImpl=}16@0:8"
- "_accessoryManager"
- "_bluetoothSessionInterface"
- "_bluetoothSessionQueue"
- "_disableSlideToUnlock"
- "_facetimeCapable"
- "_footnoteText"
- "_futureSession"
- "_listeningMode"
- "_localDevice"
- "_lostModeEnabled"
- "_lostModeType"
- "_message"
- "_phoneNumber"
- "_serialQueue"
- "_session"
- "accessoryManager"
- "accessoryManager = %p, accessoryEvent = %d, device = %p, state = %d"
- "accessoryManager:event:device:state:"
- "addFailureBlock:"
- "addSuccessBlock:"
- "attachToSession"
- "bluetoothSessionInterface"
- "bluetoothSessionQueue"
- "bypassAllListeningModesForAccessory:"
- "com.apple.icloud.findmydeviced.FMDBluetoothSessionInterface"
- "com.apple.icloud.findmydeviced.FMDBluetoothSessionInterface.BTSession"
- "dealloc"
- "decodeObjectOfClass:forKey:"
- "detachFromSession"
- "deviceWithAddress:"
- "encodeObject:forKey:"
- "encodeWithCoder:"
- "finishWithError:"
- "finishWithNoResult"
- "futureSession"
- "i16@0:8"
- "i24@0:8@16"
- "i32@0:8@16d24"
- "initWithCoder:"
- "listeningMode"
- "listeningModeForAccessory:timeout:"
- "localDevice"
- "numberWithDouble:"
- "performWithActiveSession:"
- "restoreListeningMode:forAccessory:"
- "serialQueue"
- "session"
- "sessionAttached:result:"
- "sessionDetached:"
- "sessionTerminated:"
- "setAccessoryManager:"
- "setBluetoothSessionInterface:"
- "setBluetoothSessionQueue:"
- "setDisableSlideToUnlock:"
- "setFacetimeCapable:"
- "setFootnoteText:"
- "setFutureSession:"
- "setListeningMode:"
- "setLocalDevice:"
- "setLostModeEnabled:"
- "setLostModeType:"
- "setMessage:"
- "setPhoneNumber:"
- "setSerialQueue:"
- "setSession:"
- "setUpAccessoryManager"
- "setUpLocalDevice"
- "startSession"
- "supportsChangingListeningMode"
- "supportsSecureCoding"
- "tearDownAccessoryManager"
- "tearDownLocalDevice"
- "unsignedIntValue"
- "updateListeningMode:accessory:"
- "v16@?0@8"
- "v20@0:8i16"
- "v24@0:8@\"NSCoder\"16"
- "v24@0:8Q16"
- "v24@0:8^{BTAccessoryManagerImpl=}16"
- "v24@0:8^{BTLocalDeviceImpl=}16"
- "v24@0:8^{BTSessionImpl=}16"
- "v28@0:8^{BTSessionImpl=}16i24"
- "v28@0:8i16@20"
- "v40@0:8^{BTAccessoryManagerImpl=}16i24^{BTDeviceImpl=}28i36"

```
