## TVRemoteCore

> `/System/Library/PrivateFrameworks/TVRemoteCore.framework/TVRemoteCore`

```diff

-496.41.1.0.0
-  __TEXT.__text: 0xbad10
+496.50.5.0.0
+  __TEXT.__text: 0xbaef4
   __TEXT.__auth_stubs: 0xce0
   __TEXT.__objc_methlist: 0xa160
   __TEXT.__const: 0x23c40
   __TEXT.__gcc_except_tab: 0xf68
-  __TEXT.__cstring: 0x58aa
-  __TEXT.__oslogstring: 0x8813
-  __TEXT.__unwind_info: 0x1d80
+  __TEXT.__cstring: 0x5901
+  __TEXT.__oslogstring: 0x8845
+  __TEXT.__unwind_info: 0x1d88
   __TEXT.__eh_frame: 0x7f8
   __TEXT.__objc_classname: 0x1105
-  __TEXT.__objc_methname: 0x12b01
+  __TEXT.__objc_methname: 0x12b13
   __TEXT.__objc_methtype: 0x3e4f
-  __TEXT.__objc_stubs: 0xc020
+  __TEXT.__objc_stubs: 0xc040
   __DATA_CONST.__got: 0x7d0
   __DATA_CONST.__const: 0x1bb0
   __DATA_CONST.__objc_classlist: 0x440
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x170
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4560
+  __DATA_CONST.__objc_selrefs: 0x4568
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x370
   __DATA_CONST.__objc_arraydata: 0xe0

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 3360
-  Symbols:   4122
-  CStrings:  5685
+  Functions: 3363
+  Symbols:   4125
+  CStrings:  5689
 
CStrings:
+ "-[TVRCRapportDeviceQuery _removeAllDevices]"
+ "-[TVRCXPCClient deviceQueryUpdatedDiscoveredDevices:]"
+ "-[TVRCXPCClient deviceUpdatedState:]"
+ "Device was lost, wait to see if it returns, timeout=%f, deviceWrapper=%{public}@, device=%{public}@"
+ "Informing delegate to remove device=%{public}@"
+ "Rapport discovery companionLinkClient connection invalidated. Removing all devices"
+ "Waiting for volume or siri settings before notifying client of supported buttons. receivedSiriSettings:%d, receivedVolumeSettings:%d"
+ "_removeAllDevices"
- "-[TVRCRapportDeviceQuery _disconnectAllDevices]"
- "Device was lost, wait to see if it returns, timeout=%f, deviceWrapper=%@, device=%@"
- "Rapport discovery companionLinkClient connection invalidated, disconnecting all devices"
- "Waiting for volume or siri settings before notifying client of updated supproted buttons. receivedSiriSettings:%d, receivedVolumeSettings:%d"

```
