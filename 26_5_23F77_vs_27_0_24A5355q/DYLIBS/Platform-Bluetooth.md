## Platform-Bluetooth

> `/System/Library/CoreAccessories/PlugIns/Platform/Platform-Bluetooth.platform/Platform-Bluetooth`

```diff

-1147.120.2.0.0
-  __TEXT.__text: 0x4418
-  __TEXT.__auth_stubs: 0x3e0
+1176.0.26.502.1
+  __TEXT.__text: 0x3ec0
   __TEXT.__objc_methlist: 0x3fc
   __TEXT.__const: 0x40
-  __TEXT.__cstring: 0x2e3
+  __TEXT.__cstring: 0x2e9
   __TEXT.__oslogstring: 0x86d
-  __TEXT.__unwind_info: 0x118
-  __TEXT.__objc_classname: 0xf7
-  __TEXT.__objc_methname: 0x828
-  __TEXT.__objc_methtype: 0x35d
-  __TEXT.__objc_stubs: 0x520
-  __DATA_CONST.__got: 0x60
-  __DATA_CONST.__const: 0x150
+  __TEXT.__unwind_info: 0x120
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x170
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x278
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0x1f8
+  __DATA_CONST.__got: 0x60
+  __AUTH_CONST.__const: 0x20
   __AUTH_CONST.__cfstring: 0x1a0
   __AUTH_CONST.__objc_const: 0x6d0
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0xa0
   __DATA.__objc_ivar: 0x38
   __DATA.__data: 0x1e0
-  __DATA.__bss: 0x8
+  __DATA.__bss: 0x10
   __DATA_DIRTY.__objc_data: 0x50
   __DATA_DIRTY.__data: 0x38
   __DATA_DIRTY.__common: 0x20

   - /System/Library/PrivateFrameworks/MobileBluetooth.framework/MobileBluetooth
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 69EB51DD-F12F-33AB-901E-D0A22937CE82
-  Functions: 74
-  Symbols:   435
-  CStrings:  250
+  UUID: 75075170-431A-3AAD-97D2-3D9819B167C6
+  Functions: 75
+  Symbols:   446
+  CStrings:  89
 
Symbols:
+ __NSConcreteGlobalBlock
+ ___block_descriptor_32_e5_v8?0l
+ ___block_literal_global
+ ___logObjectForModule_block_invoke
+ ___logObjectForModule_block_invoke.cold.1
+ _logObjectForModule.onceToken
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x2
+ _objc_retain_x3
+ _objc_retain_x5
+ _objc_retain_x8
- _OUTLINED_FUNCTION_2
- _objc_release
- _objc_retainAutoreleasedReturnValue
CStrings:
- "#16@0:8"
- ".cxx_destruct"
- "@\"ACCPlatformBluetoothStatusAccessory\"24@0:8@\"NSString\"16"
- "@\"NSData\""
- "@\"NSMutableDictionary\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"NSString\"24@0:8@\"NSString\"16"
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@16"
- "@32@0:8:16@24"
- "@40@0:8:16@24@32"
- "@48@0:8@16@24@32@40"
- "ACCPlatformBluetoothAccessoryInformationPluginProtocol"
- "ACCPlatformBluetoothStatusAccessory"
- "ACCPlatformBluetoothStatusPluginProtocol"
- "ACCPlatformPluginBluetooth"
- "ACCPlatformPluginProtocol"
- "ACCPluginProtocol"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "NSObject"
- "Q16@0:8"
- "T#,R"
- "T@\"NSData\",R,N,V_macAddr"
- "T@\"NSMutableDictionary\",&,N,V_accessoryList"
- "T@\"NSMutableDictionary\",R,N,V_componentList"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_btEventQueue"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "T@\"NSString\",R,N"
- "T@\"NSString\",R,N,V_accessoryUID"
- "T@\"NSString\",R,N,V_componentUID"
- "T@\"NSString\",R,N,V_name"
- "TB,N,V_btUpdatesStarted"
- "TB,N,V_isRunning"
- "TB,N,V_needToUnplugBTDevice"
- "TB,R,N"
- "TQ,R"
- "T^{BTAccessoryManagerImpl=},N,V_btAccessoryManager"
- "T^{BTDeviceImpl=},N,V_btDevice"
- "T^{BTSessionImpl=},N,V_btSession"
- "UTF8String"
- "Vv16@0:8"
- "^{BTAccessoryManagerImpl=}"
- "^{BTAccessoryManagerImpl=}16@0:8"
- "^{BTDeviceImpl=}"
- "^{BTDeviceImpl=}16@0:8"
- "^{BTSessionImpl=}"
- "^{BTSessionImpl=}16@0:8"
- "^{_NSZone=}16@0:8"
- "_ACCBluetoothStatusComponent"
- "_accessoryList"
- "_accessoryUID"
- "_btAccessoryManager"
- "_btDevice"
- "_btEventQueue"
- "_btSession"
- "_btUpdatesStarted"
- "_componentList"
- "_componentUID"
- "_isRunning"
- "_macAddr"
- "_name"
- "_needToUnplugBTDevice"
- "accessoryAttached:"
- "accessoryDetached:"
- "accessoryList"
- "accessoryUID"
- "addObject:"
- "allValues"
- "autorelease"
- "btAccessoryManager"
- "btDevice"
- "btEventQueue"
- "btSession"
- "btUpdatesStarted"
- "cStringUsingEncoding:"
- "class"
- "componentList"
- "componentUID"
- "conformsToProtocol:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "createComponentFromDict:"
- "dataWithBytes:length:"
- "debugDescription"
- "defaultCenter"
- "description"
- "getAccessoryList"
- "getBytes:length:"
- "hash"
- "i36@0:8@\"NSDictionary\"16@\"NSString\"24B32"
- "i36@0:8@16@24B32"
- "init"
- "initPlugin"
- "initWithUID:"
- "initWithUID:macAddr:name:forAccessoryUID:"
- "isEqual:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "isRunning"
- "iterateRegisteredComponentsForKnownAddresses:allOFF:"
- "macAddr"
- "member:"
- "name"
- "nameForMacAddress:"
- "needToUnplugBTDevice"
- "numberWithInt:"
- "objectForKey:"
- "performInit"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "pluginBTDevice:btAccessoryManager:btDevice:"
- "pluginName"
- "postNotificationName:object:userInfo:"
- "release"
- "removeObjectForKey:"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "self"
- "setAccessoryList:"
- "setBtAccessoryManager:"
- "setBtDevice:"
- "setBtEventQueue:"
- "setBtSession:"
- "setBtUpdatesStarted:"
- "setIsRunning:"
- "setNeedToUnplugBTDevice:"
- "setObject:forKey:"
- "setWithObject:"
- "startCheckingForUpdates:forAccessory:"
- "startPlugin"
- "stopCheckingForUpdates:forAccessory:"
- "stopPlugin"
- "stringWithFormat:"
- "stringWithUTF8String:"
- "superclass"
- "unplugBTDevice:btAccessoryManager:btDevice:"
- "updateBTComponent:forAccessory:withEnabledState:"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@\"ACCPlatformBluetoothStatusAccessory\"16"
- "v24@0:8@16"
- "v24@0:8^{BTAccessoryManagerImpl=}16"
- "v24@0:8^{BTDeviceImpl=}16"
- "v24@0:8^{BTSessionImpl=}16"
- "v28@0:8@16B24"
- "v32@0:8@\"NSDictionary\"16@\"NSString\"24"
- "v32@0:8@16@24"
- "v40@0:8@16^{BTAccessoryManagerImpl=}24^{BTDeviceImpl=}32"
- "zone"

```
