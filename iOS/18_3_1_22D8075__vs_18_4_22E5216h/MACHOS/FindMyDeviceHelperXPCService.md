## FindMyDeviceHelperXPCService

> `/System/Library/PrivateFrameworks/FindMyDevice.framework/XPCServices/FindMyDeviceHelperXPCService.xpc/FindMyDeviceHelperXPCService`

```diff

-438.33.10.29.2
-  __TEXT.__text: 0xd288
-  __TEXT.__auth_stubs: 0x600
-  __TEXT.__objc_stubs: 0x2520
-  __TEXT.__objc_methlist: 0x9c0
-  __TEXT.__objc_methname: 0x2728
-  __TEXT.__cstring: 0x21d4
-  __TEXT.__objc_classname: 0x1e4
-  __TEXT.__objc_methtype: 0x861
-  __TEXT.__const: 0x120
-  __TEXT.__gcc_except_tab: 0x178
-  __TEXT.__oslogstring: 0x1aca
-  __TEXT.__unwind_info: 0x2c8
-  __DATA_CONST.__auth_got: 0x310
-  __DATA_CONST.__got: 0x218
-  __DATA_CONST.__const: 0x1048
-  __DATA_CONST.__cfstring: 0x2ce0
-  __DATA_CONST.__objc_classlist: 0x68
+438.34.7.11.22
+  __TEXT.__text: 0xa6fc
+  __TEXT.__auth_stubs: 0x4a0
+  __TEXT.__objc_stubs: 0x2040
+  __TEXT.__objc_methlist: 0xacc
+  __TEXT.__objc_methname: 0x220b
+  __TEXT.__cstring: 0x20ff
+  __TEXT.__objc_classname: 0x1c4
+  __TEXT.__objc_methtype: 0x670
+  __TEXT.__const: 0x100
+  __TEXT.__gcc_except_tab: 0xb4
+  __TEXT.__oslogstring: 0x112c
+  __TEXT.__unwind_info: 0x240
+  __DATA_CONST.__auth_got: 0x260
+  __DATA_CONST.__got: 0x210
+  __DATA_CONST.__const: 0xef0
+  __DATA_CONST.__cfstring: 0x2cc0
+  __DATA_CONST.__objc_classlist: 0x60
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x20
+  __DATA_CONST.__objc_superrefs: 0x18
   __DATA_CONST.__objc_arraydata: 0x130
   __DATA_CONST.__objc_arrayobj: 0x30
   __DATA_CONST.__objc_doubleobj: 0x10
   __DATA_CONST.__objc_intobj: 0x48
-  __DATA.__objc_const: 0x2318
-  __DATA.__objc_selrefs: 0xa50
-  __DATA.__objc_ivar: 0xc0
-  __DATA.__objc_data: 0x410
+  __DATA.__objc_const: 0x1bf8
+  __DATA.__objc_selrefs: 0x9a0
+  __DATA.__objc_ivar: 0xa0
+  __DATA.__objc_data: 0x3c0
   __DATA.__data: 0x448
   __DATA.__common: 0x8
   __DATA.__bss: 0x148
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
-  Functions: 318
-  Symbols:   178
-  CStrings:  1113
+  Functions: 260
+  Symbols:   155
+  CStrings:  980
 
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
- _OBJC_CLASS_$_FMFuture
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
- "3"
- "@\"FMDBluetoothSessionInterface\""
- "@\"FMFuture\""
- "@\"NSObject<OS_dispatch_queue>\""
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
- "No accessory manager to tear-down."
- "No local device to tear-down."
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
- "T^{BTAccessoryManagerImpl=},N,V_accessoryManager"
- "T^{BTLocalDeviceImpl=},N,V_localDevice"
- "T^{BTSessionImpl=},N,V_session"
- "Tear-down finished for accessory manager: %p"
- "Tear-down finished for local device: %p"
- "Terminated session is not the active session. Ignoring."
- "Ti,N,V_listeningMode"
- "Timeout getting listening mode for accessory address: %@"
- "X\x11"
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
- "_futureSession"
- "_listeningMode"
- "_localDevice"
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
- "detachFromSession"
- "deviceWithAddress:"
- "finishWithError:"
- "finishWithNoResult"
- "futureSession"
- "i16@0:8"
- "i24@0:8@16"
- "i32@0:8@16d24"
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
- "setFutureSession:"
- "setListeningMode:"
- "setLocalDevice:"
- "setSerialQueue:"
- "setSession:"
- "setUpAccessoryManager"
- "setUpLocalDevice"
- "startSession"
- "supportsChangingListeningMode"
- "tearDownAccessoryManager"
- "tearDownLocalDevice"
- "unsignedIntValue"
- "updateListeningMode:accessory:"
- "v16@?0@8"
- "v20@0:8i16"
- "v24@0:8^{BTAccessoryManagerImpl=}16"
- "v24@0:8^{BTLocalDeviceImpl=}16"
- "v24@0:8^{BTSessionImpl=}16"
- "v28@0:8^{BTSessionImpl=}16i24"
- "v28@0:8i16@20"
- "v40@0:8^{BTAccessoryManagerImpl=}16i24^{BTDeviceImpl=}28i36"

```
