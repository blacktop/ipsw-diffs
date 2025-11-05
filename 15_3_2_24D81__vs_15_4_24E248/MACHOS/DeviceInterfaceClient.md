## DeviceInterfaceClient

> `/System/Library/Templates/Data/Library/Apple/System/Library/PrivateFrameworks/DeviceInterfaceClient.framework/Versions/A/DeviceInterfaceClient`

```diff

-178.60.8.0.0
-  __TEXT.__text: 0x2d5c
-  __TEXT.__auth_stubs: 0x150
-  __TEXT.__objc_methlist: 0x1a8
-  __TEXT.__const: 0x68
-  __TEXT.__gcc_except_tab: 0x30
-  __TEXT.__cstring: 0x732
+205.0.0.0.0
+  __TEXT.__text: 0x40f8
+  __TEXT.__auth_stubs: 0x130
+  __TEXT.__objc_methlist: 0x33c
+  __TEXT.__const: 0x40
+  __TEXT.__gcc_except_tab: 0xac
+  __TEXT.__cstring: 0x725
   __TEXT.__oslogstring: 0x219
-  __TEXT.__unwind_info: 0x110
+  __TEXT.__unwind_info: 0xd0
   __TEXT.__objc_classname: 0x94
   __TEXT.__objc_methname: 0x94e
   __TEXT.__objc_methtype: 0x4df
   __TEXT.__objc_stubs: 0x580
-  __DATA_CONST.__got: 0x40
+  __DATA_CONST.__got: 0x50
   __DATA_CONST.__const: 0x60
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1c0
+  __DATA_CONST.__objc_selrefs: 0x260
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0xb8
-  __AUTH_CONST.__const: 0x210
+  __AUTH_CONST.__auth_got: 0xa8
+  __AUTH_CONST.__const: 0x220
   __AUTH_CONST.__cfstring: 0x20
-  __AUTH_CONST.__objc_const: 0x7a0
+  __AUTH_CONST.__objc_const: 0x4b0
   __AUTH.__objc_data: 0xa0
   __DATA.__objc_ivar: 0x24
-  __DATA.__data: 0x120
-  __DATA.__bss: 0x10
+  __DATA.__data: 0x121
+  __DATA.__bss: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
-  - /System/Library/Frameworks/DriverKit.framework/Versions/A/DriverKit
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B8AB0979-2207-3950-8E64-8D7471839AB9
-  Functions: 89
-  Symbols:   235
+  UUID: 82551206-7D2A-3F9B-B2E4-DF4D1CE27AAF
+  Functions: 70
+  Symbols:   217
   CStrings:  214
 
Symbols:
+ GCC_except_table12
+ GCC_except_table25
+ ___block_descriptor_40_e8_32r_e8_v12?0B8l
+ ___memcpy_chk
+ ___os_log_helper_16_2_2_8_32_4_0
+ ___os_log_helper_16_2_3_8_32_4_0_4_0
+ ___os_log_helper_16_2_3_8_32_4_0_8_0
+ ___os_log_helper_16_2_3_8_32_4_0_8_64
+ ___os_log_helper_16_2_4_8_32_4_0_8_0_8_64
+ _shouldUseKext
- -[DeviceInterfaceUserClient testPing].cold.1
- GCC_except_table9
- _OUTLINED_FUNCTION_0
- _OUTLINED_FUNCTION_1
- _OUTLINED_FUNCTION_2
- __130-[DeviceInterfaceClientXPCClient transferData:inputCount:inputStruct:inputStructCount:outputStruct:outputStructCount:interfaceID:]_block_invoke.cold.1
- __44-[DeviceInterfaceClientXPCClient pingServer]_block_invoke.cold.1
- __56-[DeviceInterfaceClientXPCClient stmDestroyDockChannel:]_block_invoke.cold.1
- __59-[DeviceInterfaceClientXPCClient updatePortalAvailability:]_block_invoke.cold.1
- __62-[DeviceInterfaceClientXPCClient exclusiveAccess:interfaceID:]_block_invoke.cold.1
- __64-[DeviceInterfaceClientXPCClient portalTransaction:interfaceID:]_block_invoke.cold.1
- __85-[DeviceInterfaceClientXPCClient stmCreateDockChannel:suffix:suffixSize:interfaceID:]_block_invoke.cold.1
- __block_literal_global.95
- __shouldUseKext_block_invoke.cold.1
- _memcpy
- device_interface_user_client_create_dock_channel.cold.1
- device_interface_user_client_create_dock_channel.cold.2
- device_interface_user_client_destroy_dock_channel.cold.1
- device_interface_user_client_exclusive_access.cold.1
- device_interface_user_client_ping.cold.1
- device_interface_user_client_portal_availability.cold.1
- device_interface_user_client_portal_transaction.cold.1
- device_interface_user_client_register_device_added_callback.cold.1
- device_interface_user_client_transfer_data.cold.1
- device_interface_user_client_transfer_data.cold.2
- device_interface_user_client_transfer_data.cold.3
CStrings:
+ "B32@0:8^Q16Q24"
+ "shouldUseKext"
- "shouldUseKext_block_invoke"
- "v32@0:8^Q16Q24"

```
