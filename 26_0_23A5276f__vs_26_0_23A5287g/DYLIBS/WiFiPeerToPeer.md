## WiFiPeerToPeer

> `/System/Library/PrivateFrameworks/WiFiPeerToPeer.framework/WiFiPeerToPeer`

```diff

-826.93.0.0.0
-  __TEXT.__text: 0x20648
-  __TEXT.__auth_stubs: 0x660
-  __TEXT.__objc_methlist: 0x335c
+826.96.4.1.0
+  __TEXT.__text: 0x20ea8
+  __TEXT.__auth_stubs: 0x650
+  __TEXT.__objc_methlist: 0x338c
   __TEXT.__const: 0xa0
-  __TEXT.__cstring: 0x532d
+  __TEXT.__cstring: 0x5401
   __TEXT.__oslogstring: 0x7e2
-  __TEXT.__gcc_except_tab: 0x2fc
-  __TEXT.__unwind_info: 0x910
+  __TEXT.__gcc_except_tab: 0x380
+  __TEXT.__unwind_info: 0x968
   __TEXT.__objc_classname: 0x779
-  __TEXT.__objc_methname: 0x8163
-  __TEXT.__objc_methtype: 0x1c06
+  __TEXT.__objc_methname: 0x8196
+  __TEXT.__objc_methtype: 0x1bcb
   __TEXT.__objc_stubs: 0x41a0
   __DATA_CONST.__got: 0x1e0
   __DATA_CONST.__const: 0xd30
   __DATA_CONST.__objc_classlist: 0x140
   __DATA_CONST.__objc_protolist: 0xc0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1710
+  __DATA_CONST.__objc_selrefs: 0x1728
   __DATA_CONST.__objc_protorefs: 0x90
   __DATA_CONST.__objc_superrefs: 0x130
-  __AUTH_CONST.__auth_got: 0x340
+  __AUTH_CONST.__auth_got: 0x338
   __AUTH_CONST.__const: 0x320
   __AUTH_CONST.__cfstring: 0x3500
   __AUTH_CONST.__objc_const: 0x5918

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: CBCCA364-19C0-3676-8C1E-DF742B10E14D
-  Functions: 1027
-  Symbols:   3680
-  CStrings:  2422
+  UUID: C1E44C78-93D3-3F52-A62A-32F7F8988F07
+  Functions: 1035
+  Symbols:   3698
+  CStrings:  2428
 
Symbols:
+ -[WiFiAwareDevicesStore deauthorizePairedDeviceFor:withDeviceID:remove:]
+ -[WiFiAwareDevicesStore deauthorizePairedDeviceFor:withDeviceID:remove:completionHandler:]
+ -[WiFiAwareDevicesStore removeAllPairedDevices:]
+ -[WiFiAwareDevicesStore removeAllPairedDevicesFor:]
+ -[WiFiAwareDevicesStore removeAllPairedDevices]
+ GCC_except_table17
+ GCC_except_table29
+ GCC_except_table33
+ GCC_except_table37
+ GCC_except_table41
+ ___47-[WiFiAwareDevicesStore removeAllPairedDevices]_block_invoke
+ ___48-[WiFiAwareDevicesStore removeAllPairedDevices:]_block_invoke
+ ___51-[WiFiAwareDevicesStore removeAllPairedDevicesFor:]_block_invoke
+ ___72-[WiFiAwareDevicesStore deauthorizePairedDeviceFor:withDeviceID:remove:]_block_invoke
+ ___90-[WiFiAwareDevicesStore deauthorizePairedDeviceFor:withDeviceID:remove:completionHandler:]_block_invoke
+ ___block_descriptor_57_e8_32s40bs_e37_v16?0"<WiFiAwarePairedDevicesXPC>"8ls32l8s40l8
+ _objc_msgSend$deauthorizePairedDeviceFor:withDeviceID:remove:completionHandler:
+ _objc_msgSend$removeAllPairedDevices:
- -[WiFiAwareDevicesStore addPairedDeviceFor:pairedDeviceInfo:pairingKeyStoreID:completionHandler:]
- GCC_except_table13
- GCC_except_table19
- GCC_except_table23
- GCC_except_table27
- GCC_except_table31
- ___97-[WiFiAwareDevicesStore addPairedDeviceFor:pairedDeviceInfo:pairingKeyStoreID:completionHandler:]_block_invoke
- ___block_descriptor_64_e8_32s40s48s56bs_e37_v16?0"<WiFiAwarePairedDevicesXPC>"8ls32l8s40l8s48l8s56l8
- _objc_msgSend$addPairedDeviceFor:pairedDeviceInfo:pairingKeyStoreID:completionHandler:
- _objc_msgSend$removePairedDeviceFor:withDeviceID:uninstall:completionHandler:
- _protocol_isEqual
CStrings:
+ "-[WiFiAwareDevicesStore deauthorizePairedDeviceFor:withDeviceID:remove:]_block_invoke"
+ "-[WiFiAwareDevicesStore removeAllPairedDevicesFor:]_block_invoke"
+ "-[WiFiAwareDevicesStore removeAllPairedDevices]_block_invoke"
+ "@36@0:8@16Q24B32"
+ "deauthorizePairedDeviceFor:withDeviceID:remove:"
+ "deauthorizePairedDeviceFor:withDeviceID:remove:completionHandler:"
+ "removeAllPairedDevices"
+ "removeAllPairedDevices:"
+ "removeAllPairedDevicesFor:"
+ "v24@0:8@?<v@?@\"NSError\">16"
- "addPairedDeviceFor:pairedDeviceInfo:pairingKeyStoreID:completionHandler:"
- "removePairedDeviceFor:withDeviceID:uninstall:completionHandler:"
- "v48@0:8@\"NSString\"16@\"WiFiAwarePairedDeviceInfo\"24@\"NSUUID\"32@?<v@?Q@\"NSError\">40"
- "v48@0:8@16@24@32@?40"

```
