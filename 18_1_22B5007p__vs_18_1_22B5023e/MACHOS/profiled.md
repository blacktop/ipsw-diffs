## profiled

> `/usr/libexec/profiled`

```diff

-2343.0.0.0.0
-  __TEXT.__text: 0x9d380
+2349.0.0.0.0
+  __TEXT.__text: 0x9d724
   __TEXT.__auth_stubs: 0x20e0
-  __TEXT.__objc_stubs: 0xfa20
-  __TEXT.__objc_methlist: 0x4c94
+  __TEXT.__objc_stubs: 0xfa00
+  __TEXT.__objc_methlist: 0x4c84
   __TEXT.__const: 0x148
   __TEXT.__gcc_except_tab: 0x19a0
-  __TEXT.__oslogstring: 0xcac0
-  __TEXT.__cstring: 0x8ad7
-  __TEXT.__objc_methname: 0x13398
+  __TEXT.__oslogstring: 0xcaea
+  __TEXT.__cstring: 0x8b27
+  __TEXT.__objc_methname: 0x132fb
   __TEXT.__objc_classname: 0xb36
   __TEXT.__objc_methtype: 0x1ff1
   __TEXT.__info_plist: 0x61b
-  __TEXT.__unwind_info: 0x1698
+  __TEXT.__unwind_info: 0x16a0
   __DATA_CONST.__auth_got: 0x1080
-  __DATA_CONST.__got: 0x1b70
-  __DATA_CONST.__const: 0x1b28
-  __DATA_CONST.__cfstring: 0x82c0
+  __DATA_CONST.__got: 0x1b80
+  __DATA_CONST.__const: 0x1b38
+  __DATA_CONST.__cfstring: 0x8300
   __DATA_CONST.__objc_classlist: 0x2c8
   __DATA_CONST.__objc_catlist: 0x1e8
   __DATA_CONST.__objc_protolist: 0x68

   __DATA_CONST.__objc_arraydata: 0x28
   __DATA_CONST.__objc_arrayobj: 0x30
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA.__objc_const: 0x7248
-  __DATA.__objc_selrefs: 0x4348
-  __DATA.__objc_ivar: 0x1c4
+  __DATA.__objc_const: 0x7218
+  __DATA.__objc_selrefs: 0x4338
+  __DATA.__objc_ivar: 0x1c0
   __DATA.__objc_data: 0x1bd0
   __DATA.__data: 0x4ea
   __DATA.__common: 0x20

   - /usr/lib/liblockdown.dylib
   - /usr/lib/libmis.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1921
-  Symbols:   1450
+  Functions: 1920
+  Symbols:   1452
   CStrings:  4881
 
Symbols:
+ _kMCDMAirPlayAllowlistDeviceNameToPayloadUUIDDependencyKey
+ _kMCDMAirPlayAllowlistMACToPayloadUUIDDependencyKey
+ _kMCDMPayloadUUIDToAirPlayAllowlistMACDependencyKey
+ _kMCDMPayloadUUIDToDeviceNameDependencyKey
- _kMCDMAirPlayWhitelistMACToPayloadUUIDDependencyKey
- _kMCDMPayloadUUIDToAirPlayWhitelistMACDependencyKey
CStrings:
+ "Setting AirPlay allowlist to %!l(MISSING)u devices."
+ "com.apple.profiled.recomputeNagMetadata"
+ "deviceNameFilter"
+ "recompute nag metadata"
+ "scheduleRecomputeNagMetadataJob"
- "TB,N,V_memberQueueNeedToRecomputeNagMetadata"
- "_memberQueueNeedToRecomputeNagMetadata"
- "contextForPrimaryAccount"
- "memberQueueNeedToRecomputeNagMetadata"
- "setMemberQueueNeedToRecomputeNagMetadata:"

```
