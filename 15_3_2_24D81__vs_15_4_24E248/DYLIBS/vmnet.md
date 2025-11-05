## vmnet

> `/System/Library/Frameworks/vmnet.framework/Versions/A/vmnet`

```diff

-315.60.1.0.0
-  __TEXT.__text: 0x32a8
-  __TEXT.__auth_stubs: 0x4b0
+315.100.4.0.0
+  __TEXT.__text: 0x32f8
+  __TEXT.__auth_stubs: 0x4a0
   __TEXT.__const: 0x60
-  __TEXT.__cstring: 0xb79
+  __TEXT.__cstring: 0xbab
   __TEXT.__oslogstring: 0x1e
   __TEXT.__unwind_info: 0x108
-  __DATA_CONST.__got: 0xf0
+  __DATA_CONST.__got: 0xf8
   __DATA_CONST.__const: 0xb8
-  __AUTH_CONST.__auth_got: 0x258
+  __AUTH_CONST.__auth_got: 0x250
   __AUTH_CONST.__const: 0x4b0
-  __DATA.__data: 0xb8
+  __DATA.__data: 0xc0
   __DATA.__bss: 0x40
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/SystemConfiguration.framework/Versions/A/SystemConfiguration
   - /System/Library/PrivateFrameworks/Netrb.framework/Versions/A/Netrb
   - /usr/lib/libSystem.B.dylib
-  UUID: 95FB6C33-2F3F-30F2-856D-1E347FA5E0CD
-  Functions: 59
-  Symbols:   229
+  UUID: 67CCD6A4-D9E1-32BC-AED4-296E8A94D64F
+  Functions: 62
+  Symbols:   238
   CStrings:  107
 
Symbols:
+ ____vmnet_interface_release_block_invoke.148
+ __block_descriptor_tmp.102
+ __block_descriptor_tmp.105
+ __block_descriptor_tmp.109
+ __block_descriptor_tmp.112
+ __block_descriptor_tmp.115
+ __block_descriptor_tmp.119
+ __block_descriptor_tmp.123
+ __block_descriptor_tmp.126
+ __block_descriptor_tmp.130
+ __block_descriptor_tmp.131
+ __block_descriptor_tmp.134
+ __block_descriptor_tmp.138
+ __block_descriptor_tmp.146
+ __block_descriptor_tmp.149
+ __block_descriptor_tmp.157
+ __block_descriptor_tmp.57
+ __block_descriptor_tmp.61
+ __block_descriptor_tmp.67
+ __block_descriptor_tmp.70
+ __block_descriptor_tmp.73
+ __block_descriptor_tmp.82
+ __block_descriptor_tmp.83
+ __block_descriptor_tmp.86
+ __block_descriptor_tmp.93
+ __block_descriptor_tmp.96
+ __block_literal_global.136
+ __block_literal_global.140
+ __vmnet_interface_add_ip_port_forwarding_rule_block_invoke.106
+ __vmnet_interface_get_ip_port_forwarding_rules_block_invoke.127
+ __vmnet_interface_release.cold.2
+ __vmnet_interface_remove_ip_port_forwarding_rule_block_invoke.116
+ __vmnet_start_interface_block_invoke.50
+ __vmnet_start_interface_block_invoke.64
+ _netrbClientEnableVirtIOHeader
+ _vmnet_enable_virtio_header_key
+ vmnet_interface_add_ip_port_forwarding_rule.cold.1
+ vmnet_interface_get_ip_port_forwarding_rules.cold.1
+ vmnet_interface_remove_ip_port_forwarding_rule.cold.1
+ vmnet_interface_set_event_callback.cold.1
+ vmnet_start_interface.cold.1
+ vmnet_start_interface.cold.2
+ vmnet_start_interface.cold.3
+ vmnet_stop_interface.cold.1
- ____vmnet_interface_release_block_invoke.146
- __block_descriptor_tmp.100
- __block_descriptor_tmp.103
- __block_descriptor_tmp.107
- __block_descriptor_tmp.110
- __block_descriptor_tmp.113
- __block_descriptor_tmp.117
- __block_descriptor_tmp.121
- __block_descriptor_tmp.124
- __block_descriptor_tmp.128
- __block_descriptor_tmp.129
- __block_descriptor_tmp.132
- __block_descriptor_tmp.136
- __block_descriptor_tmp.144
- __block_descriptor_tmp.147
- __block_descriptor_tmp.155
- __block_descriptor_tmp.55
- __block_descriptor_tmp.59
- __block_descriptor_tmp.65
- __block_descriptor_tmp.68
- __block_descriptor_tmp.71
- __block_descriptor_tmp.80
- __block_descriptor_tmp.81
- __block_descriptor_tmp.84
- __block_descriptor_tmp.91
- __block_descriptor_tmp.94
- __block_literal_global.134
- __block_literal_global.138
- __vmnet_interface_add_ip_port_forwarding_rule_block_invoke.104
- __vmnet_interface_get_ip_port_forwarding_rules_block_invoke.125
- __vmnet_interface_remove_ip_port_forwarding_rule_block_invoke.114
- __vmnet_start_interface_block_invoke.48
- __vmnet_start_interface_block_invoke.62
- _insert_address_info
- _strncmp
CStrings:
+ "'%s' and '%s' can't both be enabled"
+ "vmnet_enable_virtio_header"
- "<unknown>"
- "en"

```
