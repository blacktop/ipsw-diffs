## TVRemoteCore

> `/System/Library/PrivateFrameworks/TVRemoteCore.framework/Versions/A/TVRemoteCore`

```diff

-496.40.31.0.0
-  __TEXT.__text: 0x611b8
+496.50.5.0.0
+  __TEXT.__text: 0x61308
   __TEXT.__auth_stubs: 0x860
   __TEXT.__objc_methlist: 0x7fe0
   __TEXT.__const: 0x200
   __TEXT.__gcc_except_tab: 0xb30
-  __TEXT.__cstring: 0x4c62
-  __TEXT.__oslogstring: 0x63ae
+  __TEXT.__cstring: 0x4cb9
+  __TEXT.__oslogstring: 0x63a1
   __TEXT.__unwind_info: 0x1578
   __TEXT.__objc_classname: 0xca5
-  __TEXT.__objc_methname: 0xecf9
+  __TEXT.__objc_methname: 0xed0b
   __TEXT.__objc_methtype: 0x2923
-  __TEXT.__objc_stubs: 0x9280
+  __TEXT.__objc_stubs: 0x92a0
   __DATA_CONST.__got: 0x510
   __DATA_CONST.__const: 0x808
   __DATA_CONST.__objc_classlist: 0x360
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0xe0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x38d0
+  __DATA_CONST.__objc_selrefs: 0x38d8
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x2c0
   __DATA_CONST.__objc_arraydata: 0xb8

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2683
-  Symbols:   5973
-  CStrings:  4592
+  Functions: 2686
+  Symbols:   5977
+  CStrings:  4595
 
Symbols:
+ -[TVRCRPCompanionLinkClientWrapper sourceVersion].cold.1
+ -[TVRCRPCompanionLinkClientWrapper sourceVersion].cold.2
+ -[TVRCRapportDeviceQuery _removeAllDevices]
+ _OUTLINED_FUNCTION_6
+ _objc_msgSend$_removeAllDevices
- -[TVRCRapportDeviceQuery _disconnectAllDevices]
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
- "Found existing device = [%{public}@] for device = [%{public}@]"
- "Rapport discovery companionLinkClient connection invalidated, disconnecting all devices"
- "Waiting for volume or siri settings before notifying client of updated supproted buttons. receivedSiriSettings:%d, receivedVolumeSettings:%d"

```
