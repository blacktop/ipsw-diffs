## RemoteHID

> `/System/Library/PrivateFrameworks/RemoteHID.framework/RemoteHID`

```diff

-207.0.0.0.0
-  __TEXT.__text: 0xb5d4
-  __TEXT.__auth_stubs: 0x5f0
-  __TEXT.__objc_methlist: 0x534
+207.40.2.0.0
+  __TEXT.__text: 0xb568
+  __TEXT.__auth_stubs: 0x620
+  __TEXT.__objc_methlist: 0x550
   __TEXT.__const: 0x270
-  __TEXT.__gcc_except_tab: 0x6d4
-  __TEXT.__cstring: 0x552
-  __TEXT.__oslogstring: 0xa36
-  __TEXT.__unwind_info: 0x378
-  __TEXT.__objc_classname: 0x73
-  __TEXT.__objc_methname: 0xe1a
-  __TEXT.__objc_methtype: 0x4b3
-  __TEXT.__objc_stubs: 0xee0
+  __TEXT.__gcc_except_tab: 0x684
+  __TEXT.__cstring: 0x5f8
+  __TEXT.__oslogstring: 0xa54
+  __TEXT.__unwind_info: 0x388
+  __TEXT.__objc_classname: 0x74
+  __TEXT.__objc_methname: 0xe50
+  __TEXT.__objc_methtype: 0x50a
+  __TEXT.__objc_stubs: 0xfa0
   __DATA_CONST.__got: 0x80
-  __DATA_CONST.__const: 0x318
+  __DATA_CONST.__const: 0x3a8
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x400
+  __DATA_CONST.__objc_selrefs: 0x428
   __DATA_CONST.__objc_superrefs: 0x28
-  __AUTH_CONST.__auth_got: 0x310
-  __AUTH_CONST.__const: 0x1e0
+  __AUTH_CONST.__auth_got: 0x328
+  __AUTH_CONST.__const: 0x220
   __AUTH_CONST.__cfstring: 0x2c0
-  __AUTH_CONST.__objc_const: 0x850
+  __AUTH_CONST.__objc_const: 0x8a0
   __AUTH_CONST.__objc_intobj: 0x78
   __AUTH.__objc_data: 0xf0
   __AUTH.__data: 0x10
-  __DATA.__objc_ivar: 0x7c
+  __DATA.__objc_ivar: 0x88
   __DATA.__bss: 0x18
   __DATA_DIRTY.__objc_data: 0xa0
   __DATA_DIRTY.__bss: 0x10

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 4ADF3954-44AD-3B34-964A-F209B0815F9E
-  Functions: 337
-  Symbols:   1058
-  CStrings:  402
+  UUID: D052D63C-0CB3-3169-9632-C9DCC109FC15
+  Functions: 340
+  Symbols:   1082
+  CStrings:  411
 
Symbols:
+ -[HIDRemoteDeviceServer _disconnectEndpointID:]
+ -[HIDRemoteDeviceServer disconnectEndpointID:]
+ -[HIDRemoteDeviceServer getEndpoint:]
+ -[HIDRemoteEndpoint _removeDeviceID:]
+ -[HIDRemoteEndpoint _removeDeviceID:].cold.1
+ -[HIDRemoteEndpoint logRemovedDevice:]
+ GCC_except_table1
+ GCC_except_table10
+ GCC_except_table13
+ GCC_except_table3
+ GCC_except_table66
+ GCC_except_table67
+ _OBJC_IVAR_$_HIDRemoteDeviceAACPServer._stateHandler
+ _OBJC_IVAR_$_HIDRemoteDeviceServer._lock
+ _OBJC_IVAR_$_HIDRemoteEndpoint._lock
+ ___37-[HIDRemoteDeviceAACPServer activate]_block_invoke
+ ___37-[HIDRemoteEndpoint removeAllDevices]_block_invoke_2
+ ___62-[HIDRemoteDeviceServer createRemoteDevice:deviceID:property:]_block_invoke.173
+ ___62-[HIDRemoteDeviceServer createRemoteDevice:deviceID:property:]_block_invoke.173.cold.1
+ ___62-[HIDRemoteDeviceServer createRemoteDevice:deviceID:property:]_block_invoke.173.cold.2
+ ___62-[HIDRemoteDeviceServer createRemoteDevice:deviceID:property:]_block_invoke.179
+ ___62-[HIDRemoteDeviceServer createRemoteDevice:deviceID:property:]_block_invoke.179.cold.1
+ ___62-[HIDRemoteDeviceServer createRemoteDevice:deviceID:property:]_block_invoke.179.cold.2
+ ___62-[HIDRemoteDeviceServer createRemoteDevice:deviceID:property:]_block_invoke.179.cold.3
+ ___62-[HIDRemoteDeviceServer createRemoteDevice:deviceID:property:]_block_invoke.181
+ ___block_descriptor_32_e32_v32?0"HIDRemoteDevice"8Q16^B24l
+ ___block_descriptor_32_e34_v32?0"HIDRemoteEndpoint"8Q16^B24l
+ ___block_descriptor_40_e8_32s_e34_v32?0"HIDRemoteEndpoint"8Q16^B24ls32l8
+ ___block_descriptor_40_e8_32s_e42_v32?0"NSNumber"8"HIDRemoteDevice"16^B24ls32l8
+ ___block_descriptor_40_ea8_32r_e34_v32?0"HIDRemoteEndpoint"8Q16^B24lr32l8
+ ___block_descriptor_40_ea8_32s_e103_^{os_state_data_s=I(?=b32I){os_state_data_decoder_s=[64c][64c]}[64c][0C]}16?0^{os_state_hints_s=I*II}8ls32l8
+ ___block_descriptor_40_ea8_32s_e34_v32?0"HIDRemoteEndpoint"8Q16^B24ls32l8
+ ___block_literal_global.159
+ _objc_msgSend$_disconnectEndpointID:
+ _objc_msgSend$_removeDeviceID:
+ _objc_msgSend$allValues
+ _objc_msgSend$copy
+ _objc_msgSend$disconnectEndpointID:
+ _objc_msgSend$getEndpoint:
+ _objc_msgSend$logRemovedDevice:
+ _objc_msgSend$removeObjectForKey:
+ _objc_msgSend$stateHandler:
+ _os_state_add_handler
+ _os_state_remove_handler
+ _os_unfair_recursive_lock_lock_with_options
+ _os_unfair_recursive_lock_unlock
- -[HIDAACPRemoteEndpoint removeDevice:]
- -[HIDRemoteDeviceServer disconnectEndpoint:]
- -[HIDRemoteEndpoint removeDevice:]
- -[HIDRemoteEndpoint removeDevice:].cold.1
- GCC_except_table11
- GCC_except_table2
- GCC_except_table29
- GCC_except_table60
- GCC_except_table61
- GCC_except_table64
- GCC_except_table7
- ___28-[HIDRemoteEndpoint devices]_block_invoke
- ___62-[HIDRemoteDeviceServer createRemoteDevice:deviceID:property:]_block_invoke.166
- ___62-[HIDRemoteDeviceServer createRemoteDevice:deviceID:property:]_block_invoke.166.cold.1
- ___62-[HIDRemoteDeviceServer createRemoteDevice:deviceID:property:]_block_invoke.166.cold.2
- ___62-[HIDRemoteDeviceServer createRemoteDevice:deviceID:property:]_block_invoke.167
- ___62-[HIDRemoteDeviceServer createRemoteDevice:deviceID:property:]_block_invoke.172
- ___62-[HIDRemoteDeviceServer createRemoteDevice:deviceID:property:]_block_invoke.172.cold.1
- ___62-[HIDRemoteDeviceServer createRemoteDevice:deviceID:property:]_block_invoke.172.cold.2
- ___62-[HIDRemoteDeviceServer createRemoteDevice:deviceID:property:]_block_invoke.172.cold.3
- ___block_descriptor_40_e8_32s_e15_v32?0816^B24ls32l8
- ___block_descriptor_40_ea8_32s_e15_v32?0816^B24ls32l8
- ___block_descriptor_48_ea8_32r40r_e15_v32?0816^B24lr32l8r40l8
- _objc_alloc_init
- _objc_msgSend$disconnectEndpoint:
- _objc_msgSend$removeDevice:
- _objc_msgSend$unsignedLongLongValue
CStrings:
+ "1\""
+ "Create device:%@ with id:%llu for endpoint:%@ property:%@"
+ "HID AACP device remove:0x%llx"
+ "Remove device:%@ with id:%llu for endpoint:%llu"
+ "^{os_state_data_s=I(?=b32I){os_state_data_decoder_s=[64c][64c]}[64c][0C]}16@?0^{os_state_hints_s=I*II}8"
+ "_disconnectEndpointID:"
+ "_lock"
+ "_removeDeviceID:"
+ "_stateHandler"
+ "allValues"
+ "copy"
+ "disconnectEndpointID:"
+ "getEndpoint:"
+ "logRemovedDevice:"
+ "removeObjectForKey:"
+ "v32@?0@\"HIDRemoteEndpoint\"8Q16^B24"
+ "v32@?0@\"NSNumber\"8@\"HIDRemoteDevice\"16^B24"
+ "{os_unfair_recursive_lock_s=\"ourl_lock\"{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}\"ourl_count\"I}"
- "B24@0:8@16"
- "Create device:%@ for endpoint:%@ property:%@"
- "HID AACP device remove:%p"
- "Remove device:%@ for endpoint:%llu"
- "T@\"NSMutableDictionary\",R,V_endpoints"
- "disconnectEndpoint:"
- "removeDevice:"
- "unsignedLongLongValue"
- "v32@?0@8@16^B24"

```
