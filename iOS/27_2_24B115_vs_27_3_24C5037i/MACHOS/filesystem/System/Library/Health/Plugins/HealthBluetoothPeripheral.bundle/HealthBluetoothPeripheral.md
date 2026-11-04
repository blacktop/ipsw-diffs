## HealthBluetoothPeripheral

> `/System/Library/Health/Plugins/HealthBluetoothPeripheral.bundle/HealthBluetoothPeripheral`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-7027.1.56.2.9
-  __TEXT.__text: 0x3df3c
+7027.2.13.0.0
+  __TEXT.__text: 0x3f3c0
   __TEXT.__auth_stubs: 0x850
-  __TEXT.__objc_stubs: 0x62a0
-  __TEXT.__objc_methlist: 0x3ee4
+  __TEXT.__objc_stubs: 0x63c0
+  __TEXT.__objc_methlist: 0x3f84
   __TEXT.__const: 0x1a8
-  __TEXT.__cstring: 0x26b5
-  __TEXT.__oslogstring: 0x5952
+  __TEXT.__cstring: 0x2745
+  __TEXT.__oslogstring: 0x5b07
   __TEXT.__objc_classname: 0xb5f
-  __TEXT.__objc_methname: 0x9ccd
+  __TEXT.__objc_methname: 0x9fea
   __TEXT.__objc_methtype: 0x2e98
-  __TEXT.__gcc_except_tab: 0xb10
-  __TEXT.__unwind_info: 0x1528
-  __DATA_CONST.__const: 0x12e8
-  __DATA_CONST.__cfstring: 0x22e0
+  __TEXT.__gcc_except_tab: 0xb40
+  __TEXT.__unwind_info: 0x15b8
+  __DATA_CONST.__const: 0x13b8
+  __DATA_CONST.__cfstring: 0x2340
   __DATA_CONST.__objc_classlist: 0x1b8
   __DATA_CONST.__objc_protolist: 0x188
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA_CONST.__auth_got: 0x438
   __DATA_CONST.__got: 0x460
-  __DATA.__objc_const: 0x7830
-  __DATA.__objc_selrefs: 0x2288
-  __DATA.__objc_ivar: 0x5a8
+  __DATA.__objc_const: 0x78d8
+  __DATA.__objc_selrefs: 0x2318
+  __DATA.__objc_ivar: 0x5bc
   __DATA.__objc_data: 0x1130
   __DATA.__data: 0x1280
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth

   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1717
+  Functions: 1753
   Symbols:   433
-  CStrings:  2666
+  CStrings:  2700
 
CStrings:
+ "%{public}@: Alert activation pending, chaining the handler"
+ "%{public}@: Alert already active, continuing with the handler"
+ "%{public}@: Removing user notification to launch app"
+ "%{public}@: Workout app was not opened to continue paired handoff, cancelling handoff"
+ "%{public}@: dequeuing remote pairing payload"
+ "%{public}@: enqueuing remote pairing payload while waiting for app launch"
+ "%{public}@: ignoring remote error for a different session"
+ "HBPGymKitRemotePairingNFCSessionID"
+ "Paired Handoff App Launch"
+ "Workout app was not opened to continue paired handoff"
+ "_pairedHandoffAppLaunchTimer"
+ "_queue_alertLaunchedForCurrentPairing"
+ "_queue_appLaunchNotificationIdentifier"
+ "_queue_queuedRemotePayloads"
+ "_queue_resumingPairingAfterAppLaunch"
+ "a\xd1"
+ "beginPairedHandoffAppLaunchTimeout"
+ "cancelPairedHandoffAppLaunchTimeout"
+ "errorWithDomain:code:userInfo:"
+ "isEqualToData:"
+ "isPairedHandoffAppLaunchTimerValid"
+ "removeDeliveredNotificationsWithIdentifiers:"
+ "removePendingNotificationsWithIdentifiers:"
+ "stateTimersPairedHandoffAppLaunchTimeout:"
+ "unitTest_appLaunchNotificationIdentifier"
+ "unitTest_firePairedHandoffAppLaunchTimeout"
+ "unitTest_isWaitingForAppLaunch"
+ "unitTest_nfcSessionIDData"
+ "unitTest_queuedRemotePayloads"
+ "unitTest_receiveRemotePairingError:"
+ "unitTest_receiveRemotePairingPayload:"
+ "unitTest_seedPairedHandoffTagSessionWaitingForAppLaunchWithOOBInfo:"
+ "unitTest_waitForQueue"
+ "userInfo"
+ "v24@?0@\"NSData\"8@\"NSError\"16"
- "a\xb1"
```
