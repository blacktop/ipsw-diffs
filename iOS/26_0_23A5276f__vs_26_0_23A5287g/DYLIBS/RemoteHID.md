## RemoteHID

> `/System/Library/PrivateFrameworks/RemoteHID.framework/RemoteHID`

```diff

-206.0.0.0.0
-  __TEXT.__text: 0xada4
-  __TEXT.__auth_stubs: 0x5e0
-  __TEXT.__objc_methlist: 0x4f4
-  __TEXT.__const: 0x260
-  __TEXT.__gcc_except_tab: 0x6a4
+207.0.0.0.0
+  __TEXT.__text: 0xb5d4
+  __TEXT.__auth_stubs: 0x5f0
+  __TEXT.__objc_methlist: 0x534
+  __TEXT.__const: 0x270
+  __TEXT.__gcc_except_tab: 0x6d4
   __TEXT.__cstring: 0x552
-  __TEXT.__oslogstring: 0x98a
-  __TEXT.__unwind_info: 0x350
+  __TEXT.__oslogstring: 0xa36
+  __TEXT.__unwind_info: 0x378
   __TEXT.__objc_classname: 0x73
-  __TEXT.__objc_methname: 0xd1b
-  __TEXT.__objc_methtype: 0x480
-  __TEXT.__objc_stubs: 0xe20
+  __TEXT.__objc_methname: 0xe1a
+  __TEXT.__objc_methtype: 0x4b3
+  __TEXT.__objc_stubs: 0xee0
   __DATA_CONST.__got: 0x80
-  __DATA_CONST.__const: 0x2e8
+  __DATA_CONST.__const: 0x318
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3d0
+  __DATA_CONST.__objc_selrefs: 0x400
   __DATA_CONST.__objc_superrefs: 0x28
-  __AUTH_CONST.__auth_got: 0x308
+  __AUTH_CONST.__auth_got: 0x310
   __AUTH_CONST.__const: 0x1e0
   __AUTH_CONST.__cfstring: 0x2c0
-  __AUTH_CONST.__objc_const: 0x830
+  __AUTH_CONST.__objc_const: 0x850
   __AUTH_CONST.__objc_intobj: 0x78
   __AUTH.__objc_data: 0xf0
   __AUTH.__data: 0x10
-  __DATA.__objc_ivar: 0x78
+  __DATA.__objc_ivar: 0x7c
   __DATA.__bss: 0x18
   __DATA_DIRTY.__objc_data: 0xa0
   __DATA_DIRTY.__bss: 0x10

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 493433D7-D5EC-3E97-9B19-A4742DCD85C1
-  Functions: 326
-  Symbols:   1022
-  CStrings:  389
+  UUID: 8FBF09B5-D077-36C1-984D-1354B55B6BAB
+  Functions: 337
+  Symbols:   1058
+  CStrings:  402
 
Symbols:
+ -[HIDRemoteDeviceAACPServer remoteDeviceRefresh:deviceID:transportVersion:side:]
+ -[HIDRemoteDeviceAACPServer remoteDeviceRefresh:deviceID:transportVersion:side:].cold.1
+ -[HIDRemoteDeviceServer getRefreshCountForEndpoint:deviceID:]
+ -[HIDRemoteDeviceServer remoteDeviceConfirmConnectHandler:packet:transportVersion:side:]
+ -[HIDRemoteDeviceServer remoteDeviceConfirmConnectHandler:packet:transportVersion:side:].cold.1
+ -[HIDRemoteDeviceServer remoteDeviceConfirmConnectHandler:packet:transportVersion:side:].cold.2
+ -[HIDRemoteDeviceServer remoteDeviceRefresh:deviceID:transportVersion:side:]
+ -[HIDRemoteDeviceServer setRefreshCountForEndpoint:deviceID:count:]
+ GCC_except_table40
+ GCC_except_table42
+ GCC_except_table45
+ GCC_except_table60
+ GCC_except_table61
+ GCC_except_table65
+ GCC_except_table71
+ _HIDRTBufferDeviceConfirmConnect_field_info
+ _HIDRTBufferDeviceConfirmConnect_msg
+ _HIDRTBufferDeviceConfirmConnect_submsg_info
+ _OBJC_IVAR_$_HIDRemoteDeviceServer._refreshCounts
+ _OUTLINED_FUNCTION_11
+ __os_log_fault_impl
+ _decodeDeviceConfirmConnect
+ _encodeDeviceConfirmConnect
+ _objc_msgSend$getRefreshCountForEndpoint:deviceID:
+ _objc_msgSend$numberWithUnsignedInteger:
+ _objc_msgSend$remoteDeviceConfirmConnectHandler:packet:transportVersion:side:
+ _objc_msgSend$remoteDeviceRefresh:deviceID:transportVersion:side:
+ _objc_msgSend$setRefreshCountForEndpoint:deviceID:count:
+ _objc_msgSend$unsignedIntValue
- GCC_except_table41
- GCC_except_table44
- GCC_except_table58
- GCC_except_table62
- GCC_except_table69
CStrings:
+ "Q32@0:8@16Q24"
+ "_refreshCounts"
+ "getRefreshCountForEndpoint:deviceID:"
+ "numberWithUnsignedInteger:"
+ "received confirm connect for missing device id:%d, refreshing"
+ "received confirm connect for missing device id:%d, retry limit exceeded"
+ "remoteDeviceConfirmConnectHandler:packet:transportVersion:side:"
+ "remoteDeviceRefresh id:%llu result:%d"
+ "remoteDeviceRefresh:deviceID:transportVersion:side:"
+ "setRefreshCountForEndpoint:deviceID:count:"
+ "unsignedIntValue"
+ "v40@0:8@16Q24C32C36"
+ "v40@0:8@16Q24Q32"

```
