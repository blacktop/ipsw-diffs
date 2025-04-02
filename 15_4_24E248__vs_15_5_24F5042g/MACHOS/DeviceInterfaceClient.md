## DeviceInterfaceClient

> `/System/Library/Templates/Data/Library/Apple/System/Library/PrivateFrameworks/DeviceInterfaceClient.framework/Versions/A/DeviceInterfaceClient`

```diff

-205.0.0.0.0
-  __TEXT.__text: 0x40f8
-  __TEXT.__auth_stubs: 0x130
-  __TEXT.__objc_methlist: 0x33c
+208.120.5.0.0
+  __TEXT.__text: 0x4d58
+  __TEXT.__auth_stubs: 0x200
+  __TEXT.__objc_methlist: 0x3b4
   __TEXT.__const: 0x40
-  __TEXT.__gcc_except_tab: 0xac
-  __TEXT.__cstring: 0x725
-  __TEXT.__oslogstring: 0x219
-  __TEXT.__unwind_info: 0xd0
-  __TEXT.__objc_classname: 0x94
-  __TEXT.__objc_methname: 0x94e
-  __TEXT.__objc_methtype: 0x4df
-  __TEXT.__objc_stubs: 0x580
-  __DATA_CONST.__got: 0x50
+  __TEXT.__gcc_except_tab: 0xc8
+  __TEXT.__cstring: 0x870
+  __TEXT.__oslogstring: 0x289
+  __TEXT.__unwind_info: 0xf0
+  __TEXT.__objc_classname: 0x95
+  __TEXT.__objc_methname: 0xba5
+  __TEXT.__objc_methtype: 0x509
+  __TEXT.__objc_stubs: 0x760
+  __DATA_CONST.__got: 0x70
   __DATA_CONST.__const: 0x60
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x260
+  __DATA_CONST.__objc_selrefs: 0x2e8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0xa8
-  __AUTH_CONST.__const: 0x220
-  __AUTH_CONST.__cfstring: 0x20
-  __AUTH_CONST.__objc_const: 0x4b0
+  __AUTH_CONST.__auth_got: 0x110
+  __AUTH_CONST.__const: 0x230
+  __AUTH_CONST.__cfstring: 0x40
+  __AUTH_CONST.__objc_const: 0x5a0
   __AUTH.__objc_data: 0xa0
-  __DATA.__objc_ivar: 0x24
-  __DATA.__data: 0x121
-  __DATA.__bss: 0x8
+  __DATA.__objc_ivar: 0x38
+  __DATA.__data: 0x120
+  __DATA.__bss: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 70
-  Symbols:   217
-  CStrings:  214
+  Functions: 85
+  Symbols:   270
+  CStrings:  251
 
Symbols:
+ -[DeviceInterfaceClientXPCClient connectionStateCallback]
+ -[DeviceInterfaceClientXPCClient controller]
+ -[DeviceInterfaceClientXPCClient deviceRemovedCallback]
+ -[DeviceInterfaceClientXPCClient handleConnectionClosed]
+ -[DeviceInterfaceClientXPCClient interfaceIDsLock]
+ -[DeviceInterfaceClientXPCClient interfaceIDs]
+ -[DeviceInterfaceClientXPCClient registerConnectionStateCallback:context:]
+ -[DeviceInterfaceClientXPCClient registerDeviceRemovedCallback:map:userClient:]
+ -[DeviceInterfaceUserClient registerConnectionStateCallback:context:]
+ -[DeviceInterfaceUserClient registerDeviceRemovedCallback:map:]
+ GCC_except_table1
+ GCC_except_table14
+ GCC_except_table27
+ OBJC_IVAR_$_DeviceInterfaceClientXPCClient._connectionStateCallback
+ OBJC_IVAR_$_DeviceInterfaceClientXPCClient._controller
+ OBJC_IVAR_$_DeviceInterfaceClientXPCClient._deviceRemovedCallback
+ OBJC_IVAR_$_DeviceInterfaceClientXPCClient._interfaceIDs
+ OBJC_IVAR_$_DeviceInterfaceClientXPCClient._interfaceIDsLock
+ _IOObjectRelease
+ _IORegistryEntryCreateCFProperty
+ _IOServiceGetMatchingService
+ _IOServiceMatching
+ _OBJC_CLASS_$_NSMutableSet
+ _OBJC_CLASS_$_NSSet
+ __62-[DeviceInterfaceClientXPCClient createConnectionToXPCService]_block_invoke.68
+ ___block_descriptor_40_e8_32w_e5_v8?0l
+ ___copy_helper_block_e8_32w
+ ___destroy_helper_block_e8_32w
+ ___os_log_helper_16_0_0
+ __block_literal_global.71
+ __os_log_debug_impl
+ _device_interface_user_client_register_connection_state_callback
+ _device_interface_user_client_register_device_removed_callback
+ _kCFAllocatorDefault
+ _kIOMainPortDefault
+ _memset
+ _objc_copyWeak
+ _objc_destroyWeak
+ _objc_enumerationMutation
+ _objc_initWeak
+ _objc_loadWeakRetained
+ _objc_msgSend$connectionStateCallback
+ _objc_msgSend$containsObject:
+ _objc_msgSend$controller
+ _objc_msgSend$countByEnumeratingWithState:objects:count:
+ _objc_msgSend$deviceRemoved:
+ _objc_msgSend$handleConnectionClosed
+ _objc_msgSend$lock
+ _objc_msgSend$map
+ _objc_msgSend$registerConnectionStateCallback:context:
+ _objc_msgSend$registerDeviceRemovedCallback:map:
+ _objc_msgSend$registerDeviceRemovedCallback:map:userClient:
+ _objc_msgSend$removeObject:
+ _objc_msgSend$set
+ _objc_msgSend$setWithSet:
+ _objc_msgSend$unlock
+ _objc_msgSend$unsignedIntValue
+ _objc_opt_class
+ _objc_opt_isKindOfClass
+ _rsm_channel_controller_version
- GCC_except_table12
- GCC_except_table25
- __62-[DeviceInterfaceClientXPCClient createConnectionToXPCService]_block_invoke.67
- ___os_log_helper_16_2_3_8_32_4_0_8_0
- __block_literal_global.69
- __block_literal_global.72
- _objc_msgSend$kisConnection
CStrings:
+ "\x01\x82"
+ "%s:%d: Device removed: %@"
+ "%s:%d: Registered connection state changed callback"
+ "%s:%d: Registered device removed callback"
+ "-[DeviceInterfaceClientXPCClient registerConnectionStateCallback:context:]"
+ "-[DeviceInterfaceClientXPCClient registerDeviceRemovedCallback:map:userClient:]"
+ "@\"NSLock\""
+ "@\"NSMutableSet\""
+ "AppleRSMChannelController"
+ "AppleRSMChannelControllerMajorVersion"
+ "RSM Channel Controller service not found!"
+ "T@\"NSLock\",R,N,V_interfaceIDsLock"
+ "T@\"NSMutableSet\",R,N,V_interfaceIDs"
+ "T^?,R,N,V_connectionStateCallback"
+ "T^?,R,N,V_deviceRemovedCallback"
+ "T^v,R,N,V_controller"
+ "_connectionStateCallback"
+ "_controller"
+ "_deviceRemovedCallback"
+ "_interfaceIDs"
+ "_interfaceIDsLock"
+ "connectionStateCallback"
+ "containsObject:"
+ "controller"
+ "countByEnumeratingWithState:objects:count:"
+ "deviceRemovedCallback"
+ "device_interface_user_client_register_connection_state_callback"
+ "device_interface_user_client_register_device_removed_callback"
+ "handleConnectionClosed"
+ "interfaceIDs"
+ "interfaceIDsLock"
+ "lock"
+ "registerConnectionStateCallback:context:"
+ "registerDeviceRemovedCallback:map:"
+ "registerDeviceRemovedCallback:map:userClient:"
+ "removeObject:"
+ "set"
+ "setWithSet:"
+ "unlock"
+ "unsignedIntValue"
+ "v32@0:8^?16^v24"
- "\x01"
- "%s:%d: interfaceID: %llx"
- "%s:%d: shouldUseKext: %x"
- "shouldUseKext"

```
