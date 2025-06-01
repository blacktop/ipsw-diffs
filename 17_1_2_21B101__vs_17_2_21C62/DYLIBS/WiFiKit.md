## WiFiKit

> `/System/Library/PrivateFrameworks/WiFiKit.framework/WiFiKit`

```diff

-878.6.0.0.0
-  __TEXT.__text: 0x8f110
+878.7.0.0.0
+  __TEXT.__text: 0x8f3f8
   __TEXT.__auth_stubs: 0x14c0
-  __TEXT.__objc_methlist: 0x7e24
+  __TEXT.__objc_methlist: 0x7e2c
   __TEXT.__const: 0x188
-  __TEXT.__oslogstring: 0xa075
-  __TEXT.__cstring: 0xa50f
+  __TEXT.__oslogstring: 0xa0b2
+  __TEXT.__cstring: 0xa530
   __TEXT.__gcc_except_tab: 0x1878
   __TEXT.__dlopen_cstrs: 0xac
   __TEXT.__ustring: 0x44
   __TEXT.__unwind_info: 0x1a44
   __TEXT.__objc_classname: 0xe17
-  __TEXT.__objc_methname: 0x1456e
+  __TEXT.__objc_methname: 0x14582
   __TEXT.__objc_methtype: 0x29f5
   __TEXT.__objc_stubs: 0xdca0
   __DATA_CONST.__got: 0x550
-  __DATA_CONST.__const: 0x20b8
+  __DATA_CONST.__const: 0x2090
   __DATA_CONST.__objc_classlist: 0x338
   __DATA_CONST.__objc_catlist: 0x68
   __DATA_CONST.__objc_protolist: 0x158
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x181a0
-  __DATA_CONST.__objc_selrefs: 0x46e8
+  __DATA_CONST.__objc_selrefs: 0x46f0
   __DATA_CONST.__objc_arraydata: 0x188
   __AUTH_CONST.__objc_const: 0x2598
-  __AUTH_CONST.__cfstring: 0x69c0
+  __AUTH_CONST.__cfstring: 0x69e0
   __AUTH_CONST.__objc_intobj: 0x600
   __AUTH_CONST.__objc_arrayobj: 0x1e0
   __AUTH_CONST.__const: 0x3a0

   - /usr/lib/libSystemHealth.dylib
   - /usr/lib/libnetquality.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 72E8DF21-0219-3683-AC37-2E01D605AE2B
-  Functions: 3118
-  Symbols:   11119
-  CStrings:  7225
+  UUID: 62EEC6F0-5B91-34C9-B54A-C6505AA72127
+  Functions: 3119
+  Symbols:   11120
+  CStrings:  7229
 
Symbols:
+ -[CWFNetworkProfile(WiFiKit) hasDisabledUntilDate]
+ ___23-[WFClient setPowered:]_block_invoke.108
+ ___26-[WFClient asyncMISState:]_block_invoke.146
+ ___35-[WFClient asyncMISDiscoveryState:]_block_invoke.147
+ ___35-[WFClient asyncUserAutoJoinState:]_block_invoke.144
+ ___37-[WFClient setPoweredToggle:handler:]_block_invoke.109
+ ___56-[WFClient _startMonitoringCoreWiFiEventsWithInterface:]_block_invoke.80
+ ___56-[WFClient _startMonitoringCoreWiFiEventsWithInterface:]_block_invoke.99
+ ___block_descriptor_56_e8_32s40bs48r_e45_v24?0"CWFScanResult"8"CWFNetworkProfile"16ls32l8r48l8s40l8
+ ___block_literal_global.390
+ _objc_msgSend$hasDisabledUntilDate
- ___23-[WFClient setPowered:]_block_invoke.105
- ___26-[WFClient asyncMISState:]_block_invoke.143
- ___35-[WFClient asyncMISDiscoveryState:]_block_invoke.144
- ___35-[WFClient asyncUserAutoJoinState:]_block_invoke.141
- ___37-[WFClient setPoweredToggle:handler:]_block_invoke.106
- ___56-[WFClient _startMonitoringCoreWiFiEventsWithInterface:]_block_invoke.77
- ___56-[WFClient _startMonitoringCoreWiFiEventsWithInterface:]_block_invoke.96
- ___block_descriptor_40_e8_32bs_e23_v16?0"CWFScanResult"8ls32l8
- ___block_descriptor_56_e8_32s40bs48r_e23_v16?0"CWFScanResult"8ls32l8r48l8s40l8
- ___block_literal_global.387
- _objc_msgSend$asyncCurrentScanResult:
CStrings:
+ "%@: network %@ profile %@"
+ "%s: updating asyncCurrentNetwork on join error %@"
+ "JoinStatus"
+ "hasDisabledUntilDate"
+ "v24@?0@\"CWFScanResult\"8@\"CWFNetworkProfile\"16"
- "%@: network %@"
- "v16@?0@\"CWFScanResult\"8"

```
