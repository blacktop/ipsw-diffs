## EmbeddedOSSupportHost

> `/System/Library/PrivateFrameworks/EmbeddedOSSupportHost.framework/Versions/A/EmbeddedOSSupportHost`

```diff

 164.0.0.0.0
-  __TEXT.__text: 0x4a38
+  __TEXT.__text: 0x49c8
   __TEXT.__auth_stubs: 0x410
   __TEXT.__const: 0x70
   __TEXT.__cstring: 0x548
   __TEXT.__oslogstring: 0xc75
-  __TEXT.__unwind_info: 0x118
+  __TEXT.__unwind_info: 0x120
   __DATA_CONST.__got: 0x58
   __DATA_CONST.__const: 0x198
   __AUTH_CONST.__auth_got: 0x208

   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
-  UUID: 3A551FAD-1B67-3053-AF77-2027FABEB87B
-  Functions: 118
-  Symbols:   298
+  UUID: B0D1EE70-86D2-36AA-A936-E8D7F175E227
+  Functions: 117
+  Symbols:   313
   CStrings:  178
 
Symbols:
+ _eos_device_get_notify_state.cold.5
+ eos_device_connect.cold.2
+ eos_device_connect_with_timeout.cold.3
+ eos_device_fetch_boot_args.cold.6
+ eos_device_fetch_gestalt_keys.cold.7
+ eos_device_fetch_supported_gestalt_keys_list.cold.6
+ eos_device_force_dfu.cold.5
+ eos_device_force_reset.cold.5
+ eos_device_get_addr_in6.cold.2
+ eos_device_get_healed.cold.4
+ eos_device_get_type.cold.2
+ eos_device_init.cold.2
+ eos_device_init_sockaddr_in6.cold.2
+ eos_device_init_socket_in6.cold.2
+ eos_device_is_connected.cold.2
+ eos_device_is_supported.cold.1
+ eos_device_is_unresponsive.cold.3
+ eos_device_register_event_handler.cold.4
+ eos_device_set_healed.cold.4
+ eos_device_unregister_event_handler.cold.2
- _OUTLINED_FUNCTION_3
- _OUTLINED_FUNCTION_4

```
