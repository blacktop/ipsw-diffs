## RemoteHID

> `/System/Library/PrivateFrameworks/RemoteHID.framework/Versions/A/RemoteHID`

```diff

-192.0.1.0.0
-  __TEXT.__text: 0x9e88
-  __TEXT.__auth_stubs: 0x3d0
-  __TEXT.__objc_methlist: 0x3d8
+192.100.4.0.0
+  __TEXT.__text: 0xa0dc
+  __TEXT.__auth_stubs: 0x3f0
+  __TEXT.__objc_methlist: 0x400
   __TEXT.__const: 0x244
-  __TEXT.__gcc_except_tab: 0x174
-  __TEXT.__cstring: 0x43c
-  __TEXT.__oslogstring: 0x89e
-  __TEXT.__unwind_info: 0x1e0
+  __TEXT.__gcc_except_tab: 0x18c
+  __TEXT.__cstring: 0x445
+  __TEXT.__oslogstring: 0x8ce
+  __TEXT.__unwind_info: 0x1f8
   __TEXT.__objc_classname: 0x5a
-  __TEXT.__objc_methname: 0xabf
+  __TEXT.__objc_methname: 0xb16
   __TEXT.__objc_methtype: 0x3fc
-  __TEXT.__objc_stubs: 0xb80
+  __TEXT.__objc_stubs: 0xc00
   __DATA_CONST.__got: 0x78
   __DATA_CONST.__const: 0x108
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x308
+  __DATA_CONST.__objc_selrefs: 0x328
   __DATA_CONST.__objc_superrefs: 0x20
-  __AUTH_CONST.__auth_got: 0x1f8
-  __AUTH_CONST.__const: 0x278
-  __AUTH_CONST.__cfstring: 0x1e0
-  __AUTH_CONST.__objc_const: 0x630
-  __AUTH_CONST.__objc_intobj: 0x48
+  __AUTH_CONST.__auth_got: 0x208
+  __AUTH_CONST.__const: 0x2c8
+  __AUTH_CONST.__cfstring: 0x200
+  __AUTH_CONST.__objc_const: 0x660
+  __AUTH_CONST.__objc_intobj: 0x60
   __AUTH.__objc_data: 0x140
   __AUTH.__data: 0x10
-  __DATA.__objc_ivar: 0x58
+  __DATA.__objc_ivar: 0x5c
   __DATA.__bss: 0x28
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation

   - /System/Library/PrivateFrameworks/MobileBluetooth.framework/Versions/A/MobileBluetooth
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 3699CE8B-E116-3F61-B536-85B466704D6D
-  Functions: 267
-  Symbols:   543
-  CStrings:  320
+  UUID: 45DABD26-EB2F-38DF-A688-EBB8BCB983DC
+  Functions: 292
+  Symbols:   576
+  CStrings:  329
 
Symbols:
+ -[HIDRemoteDevice cancelled]
+ -[HIDRemoteDevice setCancelled:]
+ -[HIDRemoteDeviceAACPServer removeAllBTDevices]
+ GCC_except_table27
+ GCC_except_table48
+ GCC_except_table49
+ GCC_except_table52
+ OBJC_IVAR_$_HIDRemoteDevice._cancelled
+ RemoteHIDLog.cold.1
+ RemoteHIDLogPackets.cold.1
+ _OUTLINED_FUNCTION_10
+ _OUTLINED_FUNCTION_9
+ __62-[HIDRemoteDeviceServer createRemoteDevice:deviceID:property:]_block_invoke.134
+ __62-[HIDRemoteDeviceServer createRemoteDevice:deviceID:property:]_block_invoke.134.cold.1
+ __62-[HIDRemoteDeviceServer createRemoteDevice:deviceID:property:]_block_invoke.134.cold.2
+ __62-[HIDRemoteDeviceServer createRemoteDevice:deviceID:property:]_block_invoke.140
+ __62-[HIDRemoteDeviceServer createRemoteDevice:deviceID:property:]_block_invoke.140.cold.1
+ __62-[HIDRemoteDeviceServer createRemoteDevice:deviceID:property:]_block_invoke.140.cold.2
+ __62-[HIDRemoteDeviceServer createRemoteDevice:deviceID:property:]_block_invoke.140.cold.3
+ __62-[HIDRemoteDeviceServer createRemoteDevice:deviceID:property:]_block_invoke.144
+ __64-[HIDRemoteDeviceAACPServer btSessionEventHandler:event:result:]_block_invoke.7
+ ___47-[HIDRemoteDeviceAACPServer removeAllBTDevices]_block_invoke
+ ___64-[HIDRemoteDeviceAACPServer btSessionEventHandler:event:result:]_block_invoke_2
+ ___block_descriptor_40_e8_32w_e5_v8?0l
+ ___copy_helper_block_e8_32w
+ ___destroy_helper_block_e8_32w
+ _bzero
+ _dispatch_async_and_wait
+ _objc_msgSend$cancelled
+ _objc_msgSend$removeAllBTDevices
+ _objc_msgSend$setCancelHandler:
+ _objc_msgSend$setCancelled:
- GCC_except_table25
- GCC_except_table46
- GCC_except_table47
- GCC_except_table50
- __62-[HIDRemoteDeviceServer createRemoteDevice:deviceID:property:]_block_invoke.129
- __62-[HIDRemoteDeviceServer createRemoteDevice:deviceID:property:]_block_invoke.129.cold.1
- __62-[HIDRemoteDeviceServer createRemoteDevice:deviceID:property:]_block_invoke.130
- __62-[HIDRemoteDeviceServer createRemoteDevice:deviceID:property:]_block_invoke.135.cold.1
- __62-[HIDRemoteDeviceServer createRemoteDevice:deviceID:property:]_block_invoke.135.cold.2
- __62-[HIDRemoteDeviceServer createRemoteDevice:deviceID:property:]_block_invoke.135.cold.3
- __64-[HIDRemoteDeviceAACPServer btSessionEventHandler:event:result:]_block_invoke.10
- ___35-[HIDRemoteDeviceAACPServer cancel]_block_invoke
CStrings:
+ "TB,V_cancelled"
+ "VendorID"
+ "[device:%d] remoteDeviceSetReport:0x%x, bailing"
+ "_cancelled"
+ "cancelled"
+ "removeAllBTDevices"
+ "setCancelHandler:"
+ "setCancelled:"

```
