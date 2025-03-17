## FindMyDeviceBluetoothExtension

> `/Applications/FindMyExtensionContainer.app/PlugIns/FindMyDeviceBluetoothExtension.appex/FindMyDeviceBluetoothExtension`

```diff

-438.34.7.11.24
-  __TEXT.__text: 0xcdc8
-  __TEXT.__auth_stubs: 0x460
-  __TEXT.__objc_stubs: 0x2600
-  __TEXT.__objc_methlist: 0x104c
-  __TEXT.__const: 0x128
-  __TEXT.__oslogstring: 0x142a
-  __TEXT.__cstring: 0x23b9
-  __TEXT.__objc_classname: 0x366
-  __TEXT.__objc_methtype: 0xa9b
-  __TEXT.__objc_methname: 0x2abe
-  __TEXT.__gcc_except_tab: 0x1a0
-  __TEXT.__unwind_info: 0x320
-  __DATA_CONST.__auth_got: 0x240
-  __DATA_CONST.__got: 0x1c0
-  __DATA_CONST.__const: 0x1160
-  __DATA_CONST.__cfstring: 0x2fe0
-  __DATA_CONST.__objc_classlist: 0x90
+438.34.7.11.27
+  __TEXT.__text: 0xfe98
+  __TEXT.__auth_stubs: 0x5f0
+  __TEXT.__objc_stubs: 0x2a20
+  __TEXT.__objc_methlist: 0x1244
+  __TEXT.__const: 0x148
+  __TEXT.__oslogstring: 0x1d88
+  __TEXT.__cstring: 0x25c2
+  __TEXT.__objc_classname: 0x386
+  __TEXT.__objc_methtype: 0xc6d
+  __TEXT.__objc_methname: 0x2f20
+  __TEXT.__gcc_except_tab: 0x2b4
+  __TEXT.__unwind_info: 0x3f8
+  __DATA_CONST.__auth_got: 0x308
+  __DATA_CONST.__got: 0x1b8
+  __DATA_CONST.__const: 0x12f8
+  __DATA_CONST.__cfstring: 0x3060
+  __DATA_CONST.__objc_classlist: 0x98
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x30
+  __DATA_CONST.__objc_superrefs: 0x38
   __DATA_CONST.__objc_arraydata: 0x30
   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA_CONST.__objc_dictobj: 0x50
   __DATA_CONST.__objc_intobj: 0x30
-  __DATA.__objc_const: 0x3340
-  __DATA.__objc_selrefs: 0xb50
-  __DATA.__objc_ivar: 0x100
-  __DATA.__objc_data: 0x5a0
+  __DATA.__objc_const: 0x3560
+  __DATA.__objc_selrefs: 0xc58
+  __DATA.__objc_ivar: 0x120
+  __DATA.__objc_data: 0x5f0
   __DATA.__data: 0x6a0
   __DATA.__common: 0x8
-  __DATA.__bss: 0x158
+  __DATA.__bss: 0x180
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox
-  - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/PrivateFrameworks/BluetoothManager.framework/BluetoothManager
   - /System/Library/PrivateFrameworks/FMCore.framework/FMCore
   - /System/Library/PrivateFrameworks/FMCoreLite.framework/FMCoreLite
   - /System/Library/PrivateFrameworks/FindMyDevice.framework/FindMyDevice
   - /System/Library/PrivateFrameworks/MediaExperience.framework/MediaExperience
+  - /System/Library/PrivateFrameworks/MobileBluetooth.framework/MobileBluetooth
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 372
-  Symbols:   138
-  CStrings:  1178
+  Functions: 457
+  Symbols:   163
+  CStrings:  1305
 
Symbols:
+ OBJC_IVAR_$_BluetoothManager._accessoryManager
+ _BTAccessoryManagerAddCallbacks
+ _BTAccessoryManagerGetControlCommand
+ _BTAccessoryManagerGetDefault
+ _BTAccessoryManagerGetDeviceColor
+ _BTAccessoryManagerRemoveCallbacks
+ _BTAccessoryManagerSendControlCommand
+ _BTDeviceAddressFromString
+ _BTDeviceFromAddress
+ _BTLocalDeviceAddCallbacks
+ _BTLocalDeviceGetDefault
+ _BTLocalDeviceRemoveCallbacks
+ _BTServiceAddCallbacks
+ _BTServiceRemoveCallbacks
+ _BTSessionAttachWithQueue
+ _BTSessionDetachWithQueue
+ _OBJC_CLASS_$_BluetoothManager
+ _OBJC_CLASS_$_FMFuture
+ _OBJC_METACLASS_$_BluetoothManager
+ __Block_object_dispose
+ _dispatch_assert_queue$V2
+ _dispatch_group_create
+ _dispatch_group_enter
+ _dispatch_group_leave
+ _dispatch_group_wait
+ _dispatch_semaphore_create
+ _dispatch_semaphore_signal
+ _dispatch_semaphore_wait
+ _dispatch_sync
+ _objc_release_x9
- _OBJC_CLASS_$_CBConnection
- _OBJC_CLASS_$_CBDiscovery
- _OBJC_CLASS_$_CBProductInfo
- __os_log_default
- _dispatch_queue_attr_make_with_autorelease_frequency
CStrings:
+ "3"
+ "@\"FMDBluetoothSessionInterface\""
+ "@\"FMFuture\""
+ "AACPVersionInfo"
+ "ADMobileBluetoothDeviceDataSource"
+ "Already attaching to session. Ignoring new request."
+ "Attaching to session..."
+ "Attempting to set listening mode for accessory address: %@"
+ "Bluetooth accessory %@ connection status = %u"
+ "BluetoothManager available after %f"
+ "Callback for BTAccessoryEvent %u"
+ "Callback for BTLocalDeviceStatusEvent %u"
+ "Callback for BTServiceEvent %u"
+ "Callback for BTSessionEvent %u"
+ "Cannot get BTDevice: No session. Address: %@"
+ "Detached session is not the active session. Ignoring."
+ "Detaching from session %p"
+ "Error in bluetooth session interface, detaching. Pending actions have been discarded. %@"
+ "FMDAccessoryAudioController restoring listening mode %u for accessory %@"
+ "FMDAccessoryAudioController unable to restore unknown listening mode %u for accessory %@"
+ "FMDAccessoryAudioController: Original state - volume: %f listeningMode: %u"
+ "FMDBluetoothSessionInterface"
+ "FMDBluetoothSessionInterfaceErrorDomain"
+ "Failed adding callbacks to accessory manager %p from session: %p, result: %d"
+ "Failed adding callbacks to local device %p from session %p. Result: %d."
+ "Failed attaching to session %d"
+ "Failed getting BTDevice address from address string %@ %d"
+ "Failed getting BTDevice address from nil / empty address string."
+ "Failed getting BTDevice from BTDeviceAddress %@ %d"
+ "Failed getting default accessory manager from session: %p, result: %d"
+ "Failed getting default local device from session %p. Result: %d."
+ "Failed to get btdevice for listening mode using accessory address: %@"
+ "Failed to get color for accessory %@ with error code %d"
+ "Failed to get listening mode for accessory address: %@ | result: %d"
+ "Failed to set listening mode for accessory address: %@ | result: %d"
+ "Failed to set up accessory manager. Missing session."
+ "Failed to set up local device. Missing session."
+ "Failed to update btdevice listening mode on accessory address: %@"
+ "Finished setup of accessory manager %p"
+ "Found BTDevice at address %@"
+ "Got listening mode for accessory address: %@ | mode: %u"
+ "Initialized FMDBluetoothSessionInterface"
+ "Local device set up."
+ "No accessory manager to tear-down."
+ "No local device to tear-down."
+ "Registered session callbacks %p"
+ "Retrieving listening mode for accessory address: %@ | timeout: %f"
+ "Session attached %p, result: %d."
+ "Session detached %p"
+ "Session failed to attach: %u"
+ "Session is active. Executing client request block."
+ "Session requested detach, but we had no session. Nothing to do."
+ "Session started by client. [warmup complete]"
+ "Session terminated %p"
+ "Set listening mode for accessory address: %@ | mode: %u"
+ "T@\"FMDBluetoothSessionInterface\",&,N,V_bluetoothSessionInterface"
+ "T@\"FMFuture\",&,N,V_futureSession"
+ "T@\"NSObject<OS_dispatch_queue>\",&,N,V_bluetoothSessionQueue"
+ "T^{BTAccessoryManagerImpl=},N,V_accessoryManager"
+ "T^{BTLocalDeviceImpl=},N,V_localDevice"
+ "T^{BTSessionImpl=},N,V_session"
+ "Tear-down finished for accessory manager: %p"
+ "Tear-down finished for local device: %p"
+ "Terminated session is not the active session. Ignoring."
+ "Ti,N,V_listeningMode"
+ "Timeout getting listening mode for accessory address: %@"
+ "X\x11"
+ "^{BTAccessoryManagerImpl=}"
+ "^{BTAccessoryManagerImpl=}16@0:8"
+ "^{BTDeviceImpl=}24@0:8@16"
+ "^{BTLocalDeviceImpl=}"
+ "^{BTLocalDeviceImpl=}16@0:8"
+ "^{BTSessionImpl=}"
+ "^{BTSessionImpl=}16@0:8"
+ "_accessoryManager"
+ "_bluetoothSessionInterface"
+ "_bluetoothSessionQueue"
+ "_futureSession"
+ "_listeningMode"
+ "_localDevice"
+ "_session"
+ "accessoryInfo"
+ "accessoryManager"
+ "accessoryManager = %p, accessoryEvent = %d, device = %p, state = %d"
+ "accessoryManager:event:device:state:"
+ "addSuccessBlock:"
+ "attachToSession"
+ "available"
+ "bluetoothDevice %@"
+ "bluetoothManagerDelegateQueue"
+ "bluetoothSessionInterface"
+ "bluetoothSessionQueue"
+ "bypassAllListeningModesForAccessory:"
+ "color"
+ "com.apple.icloud.FindMyDevice.FindMyExtensionContainer.FindMyDeviceBluetoothExtension.bluetoothManagerDelegateQueue"
+ "com.apple.icloud.FindMyDevice.FindMyExtensionContainer.FindMyDeviceBluetoothExtension.bluetoothManagerSerialQueue"
+ "com.apple.icloud.findmydeviced.FMDBluetoothSessionInterface"
+ "com.apple.icloud.findmydeviced.FMDBluetoothSessionInterface.BTSession"
+ "connectDevice:"
+ "connected"
+ "currentInstance"
+ "detachFromSession"
+ "device"
+ "deviceWithAddress:"
+ "findmybluetotthExtension invalid info. Count: %lu, Values: %@"
+ "finishWithError:"
+ "finishWithNoResult"
+ "futureSession"
+ "getAccessoryManager"
+ "i16@0:8"
+ "i24@0:8@16"
+ "i32@0:8@16d24"
+ "inEarDetectEnabled"
+ "inEarStatusPrimary:secondary:"
+ "isTemporaryPaired"
+ "length"
+ "listeningMode"
+ "listeningModeForAccessory:timeout:"
+ "localDevice"
+ "numberWithDouble:"
+ "pairedAppleAccessories"
+ "pairedDevices"
+ "performWithActiveSession:"
+ "productId"
+ "received valid AACPVersionInfo: %@"
+ "restoreListeningMode:forAccessory:"
+ "serialNumberFromVersionInfo:"
+ "session"
+ "sessionAttached:result:"
+ "sessionDetached:"
+ "sessionTerminated:"
+ "setAccessoryManager:"
+ "setBluetoothSessionInterface:"
+ "setBluetoothSessionQueue:"
+ "setFutureSession:"
+ "setListeningMode:"
+ "setLocalDevice:"
+ "setSession:"
+ "setSharedInstanceQueue:"
+ "setUpAccessoryManager"
+ "setUpLocalDevice"
+ "startSession"
+ "tearDownAccessoryManager"
+ "tearDownLocalDevice"
+ "updateDisccovery"
+ "updateListeningMode:accessory:"
+ "v16@?0@8"
+ "v20@0:8i16"
+ "v24@0:8^{BTAccessoryManagerImpl=}16"
+ "v24@0:8^{BTLocalDeviceImpl=}16"
+ "v24@0:8^{BTSessionImpl=}16"
+ "v28@0:8^{BTSessionImpl=}16i24"
+ "v28@0:8i16@20"
+ "v40@0:8^{BTAccessoryManagerImpl=}16i24^{BTDeviceImpl=}28i36"
+ "vendorId"
- "Bluetooth accessory %@ connection status = %u serviceFlags %x discoveryFlags %llx"
- "CBDiscovery returned %lu devices.\n"
- "CBDiscovery returned 0 devices. Potential error: %@\n"
- "FMDAccessoryAudioController: Original state - volume: %f"
- "Failed to activate connection with error: %@"
- "Found %@.\n"
- "Ignore %@ because it is LE paired.\n"
- "X"
- "activateWithCompletion:"
- "btAddressData"
- "classicPairedAppleAccessories"
- "colorCodeBest"
- "connectedServices"
- "deviceFlags"
- "devicesWithDiscoveryFlags:error:"
- "discoveryFlags"
- "firmwareVersion"
- "flags"
- "fm_safeSetObject:forKey:"
- "primaryPlacement"
- "productID"
- "productInfoWithProductID:"
- "secondaryPlacement"
- "serialNumberLeft"
- "serialNumberRight"
- "setPeerDevice:"
- "setServiceFlags:"
- "updateDiscovery"
- "vendorID"

```
