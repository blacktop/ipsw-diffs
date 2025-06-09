## useractivityd

> `/System/Library/PrivateFrameworks/UserActivity.framework/Agents/useractivityd`

```diff

-594.0.0.0.0
-  __TEXT.__text: 0x7ab10
-  __TEXT.__auth_stubs: 0xf40
-  __TEXT.__objc_stubs: 0xc0a0
-  __TEXT.__objc_methlist: 0x684c
-  __TEXT.__const: 0x338
-  __TEXT.__cstring: 0x4720
-  __TEXT.__objc_classname: 0xc74
-  __TEXT.__objc_methname: 0xf6f9
-  __TEXT.__objc_methtype: 0x2155
-  __TEXT.__gcc_except_tab: 0xae6c
-  __TEXT.__oslogstring: 0xdf10
+602.0.0.0.0
+  __TEXT.__text: 0x7a37c
+  __TEXT.__auth_stubs: 0xed0
+  __TEXT.__objc_stubs: 0xc040
+  __TEXT.__objc_methlist: 0x68a4
+  __TEXT.__const: 0x328
+  __TEXT.__cstring: 0x470b
+  __TEXT.__objc_classname: 0xc8d
+  __TEXT.__objc_methname: 0xf864
+  __TEXT.__objc_methtype: 0x2244
+  __TEXT.__gcc_except_tab: 0xadac
+  __TEXT.__oslogstring: 0xdc59
   __TEXT.__dof_UA: 0xfad
-  __TEXT.__unwind_info: 0x2430
-  __DATA_CONST.__auth_got: 0x7b8
-  __DATA_CONST.__got: 0x4c8
+  __TEXT.__unwind_info: 0x23f0
+  __DATA_CONST.__auth_got: 0x780
+  __DATA_CONST.__got: 0x4d0
   __DATA_CONST.__auth_ptr: 0x18
   __DATA_CONST.__const: 0x1868
   __DATA_CONST.__cfstring: 0x5840
   __DATA_CONST.__objc_classlist: 0x2c0
   __DATA_CONST.__objc_catlist: 0x8
-  __DATA_CONST.__objc_protolist: 0xf8
+  __DATA_CONST.__objc_protolist: 0x100
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x58
   __DATA_CONST.__objc_superrefs: 0x218

   __DATA_CONST.__objc_intobj: 0x180
   __DATA_CONST.__objc_doubleobj: 0xd0
   __DATA_CONST.__objc_arrayobj: 0x30
-  __DATA.__objc_const: 0xee70
-  __DATA.__objc_selrefs: 0x38e8
-  __DATA.__objc_ivar: 0x8f0
+  __DATA.__objc_const: 0xf1e0
+  __DATA.__objc_selrefs: 0x3918
+  __DATA.__objc_ivar: 0x8e8
   __DATA.__objc_data: 0x1b80
-  __DATA.__data: 0xbf8
+  __DATA.__data: 0xc58
   __DATA.__bss: 0x238
   __DATA.__common: 0x1
+  - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/Frameworks/UniformTypeIdentifiers.framework/UniformTypeIdentifiers
   - /System/Library/PrivateFrameworks/AggregateDictionary.framework/AggregateDictionary
   - /System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices
-  - /System/Library/PrivateFrameworks/BluetoothManager.framework/BluetoothManager
   - /System/Library/PrivateFrameworks/CarPlayServices.framework/CarPlayServices
   - /System/Library/PrivateFrameworks/CloudDocs.framework/CloudDocs
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics

   - /usr/lib/libbz2.1.0.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 7959466B-AE65-362F-A989-00A88A17FDCF
-  Functions: 2343
-  Symbols:   414
-  CStrings:  5560
+  UUID: 205E556A-F654-3077-AFF3-E15AD7DF63DF
+  Functions: 2338
+  Symbols:   408
+  CStrings:  5561
 
Symbols:
+ _OBJC_CLASS_$_CBCentralManager
- _BTLocalDeviceAddCallbacks
- _BTLocalDeviceGetDefault
- _BTLocalDeviceGetModulePower
- _BTLocalDeviceMaskCallbacks
- _BTLocalDeviceRemoveCallbacks
- _BTSessionAttachWithQueue
- _BTSessionDetachWithQueue
CStrings:
+ "01:54:25"
+ "01:54:48"
+ "@\"CBCentralManager\""
+ "BLUETOOTH: Detached from bluetooth session."
+ "BLUETOOTH: Setting powered status to OFF"
+ "BLUETOOTH: Setting powered status to ON"
+ "BLUETOOTH: Setting powered status to resetting"
+ "BLUETOOTH: Setting powered status to unauthorized"
+ "BLUETOOTH: Setting powered status to unknown"
+ "BLUETOOTH: Setting powered status to unsupported"
+ "CBCentralManagerDelegate"
+ "May 19 2025"
+ "[CODERV2] Got extension data: %{private}@ for path %{private}@"
+ "[FILE MANAGER] Created file by writing blank data to path: %@"
+ "_cbManager"
+ "cbManager"
+ "centralManager:connectionEventDidOccur:forPeripheral:"
+ "centralManager:didConnectPeripheral:"
+ "centralManager:didDisconnectPeripheral:error:"
+ "centralManager:didDisconnectPeripheral:timestamp:isReconnecting:error:"
+ "centralManager:didDiscoverPeripheral:advertisementData:RSSI:"
+ "centralManager:didFailToConnectPeripheral:error:"
+ "centralManager:didUpdateANCSAuthorizationForPeripheral:"
+ "centralManager:willRestoreState:"
+ "centralManagerDidUpdateState:"
+ "initWithDelegate:queue:options:"
+ "v24@0:8@\"CBCentralManager\"16"
+ "v32@0:8@\"CBCentralManager\"16@\"CBPeripheral\"24"
+ "v32@0:8@\"CBCentralManager\"16@\"NSDictionary\"24"
+ "v40@0:8@\"CBCentralManager\"16@\"CBPeripheral\"24@\"NSError\"32"
+ "v40@0:8@\"CBCentralManager\"16q24@\"CBPeripheral\"32"
+ "v40@0:8@16q24@32"
+ "v48@0:8@\"CBCentralManager\"16@\"CBPeripheral\"24@\"NSDictionary\"32@\"NSNumber\"40"
+ "v52@0:8@\"CBCentralManager\"16@\"CBPeripheral\"24d32B40@\"NSError\"44"
+ "v52@0:8@16@24d32B40@44"
+ "writeToFile:atomically:"
+ "zOrderIndex"
- "05:20:48"
- "05:21:08"
- "Apr 19 2025"
- "BLUETOOTH: Attached to BTSession %{public}p"
- "BLUETOOTH: Detached from BTSession %{public}p localDevice=%{public}p"
- "BLUETOOTH: Detached from BTSession, result=%{public}d, setting attached to NO."
- "BLUETOOTH: Error %{public}d removing device callbacks, device=%{public}p"
- "BLUETOOTH: Failed to add callbacks for local device %{public}p from BTSession %{public}p, result=%{public}d."
- "BLUETOOTH: Failed to attach to BTSession, result=%{public}d"
- "BLUETOOTH: Failed to get device powered status, for local device %{public}p from BTSession %{public}p, result=%{public}d."
- "BLUETOOTH: Failed to get local device for session %{public}p, result=%{public}d"
- "BLUETOOTH: Local device %{public}p from BTSession %{public}p, result=%{public}d."
- "BLUETOOTH: Returning NO for .poweredOn because our session has been terminated."
- "BLUETOOTH: Setting powered status for device %{public}p to %{BOOL}d"
- "BLUETOOTH: Setting powered-status-validity for device %{public}p to NO"
- "BLUETOOTH: Terminated from BTSession %{public}p localDevice=%{public}p"
- "BLUETOOTH: Unexpected error %{public}d, so ignoring it."
- "[CODERV2] Got extension data: %@"
- "[FILE MANAGER] Created file at path: %@"
- "^{BTLocalDeviceImpl=}"
- "^{BTLocalDeviceImpl=}16@0:8"
- "^{BTSessionImpl=}"
- "^{BTSessionImpl=}16@0:8"
- "_localDevice"
- "_session"
- "attachSession:"
- "detachSession:"
- "handleLocalDeviceCallback:event:result:"
- "handleSessionEvent:event:result:"
- "localDevice"
- "session"
- "terminateSession:"
- "userActivityBTStatus"
- "v24@0:8^{BTSessionImpl=}16"
- "v32@0:8^{BTLocalDeviceImpl=}16i24i28"
- "v32@0:8^{BTSessionImpl=}16i24i28"

```
