## wifip2pd

> `/usr/libexec/wifip2pd`

```diff

-826.101.0.0.0
-  __TEXT.__text: 0x464b90
-  __TEXT.__auth_stubs: 0x4550
+826.105.0.0.0
+  __TEXT.__text: 0x463ce8
+  __TEXT.__auth_stubs: 0x4570
   __TEXT.__objc_methlist: 0x1584
-  __TEXT.__const: 0x35d80
-  __TEXT.__cstring: 0xe36b
-  __TEXT.__swift5_typeref: 0xadce
+  __TEXT.__const: 0x35d20
+  __TEXT.__cstring: 0xe31b
+  __TEXT.__swift5_typeref: 0xad8a
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__oslogstring: 0x13bd3
+  __TEXT.__oslogstring: 0x13db3
   __TEXT.__objc_methname: 0x3a0a
-  __TEXT.__constg_swiftt: 0xdac4
-  __TEXT.__swift5_fieldmd: 0x13f88
-  __TEXT.__swift5_types: 0x104c
-  __TEXT.__swift5_reflstr: 0x11fc6
+  __TEXT.__constg_swiftt: 0xd9e8
+  __TEXT.__swift5_fieldmd: 0x13f2c
+  __TEXT.__swift5_types: 0x1044
+  __TEXT.__swift5_reflstr: 0x11f56
   __TEXT.__swift5_builtin: 0x1478
   __TEXT.__swift5_assocty: 0x28c8
   __TEXT.__swift5_protos: 0xe4
   __TEXT.__swift5_proto: 0x2abc
   __TEXT.__objc_classname: 0x385
   __TEXT.__objc_methtype: 0x12b1
-  __TEXT.__swift5_capture: 0x3310
+  __TEXT.__swift5_capture: 0x3318
   __TEXT.__swift5_mpenum: 0x16c
   __TEXT.__swift_as_entry: 0xc4
   __TEXT.__swift_as_ret: 0x70
-  __TEXT.__unwind_info: 0xd838
-  __TEXT.__eh_frame: 0x1792c
-  __DATA_CONST.__auth_got: 0x22a8
+  __TEXT.__unwind_info: 0xd7a0
+  __TEXT.__eh_frame: 0x1791c
+  __DATA_CONST.__auth_got: 0x22b8
   __DATA_CONST.__got: 0xef0
-  __DATA_CONST.__auth_ptr: 0x1dc0
-  __DATA_CONST.__const: 0x2aa38
+  __DATA_CONST.__auth_ptr: 0x1da8
+  __DATA_CONST.__const: 0x2a8e8
   __DATA_CONST.__cfstring: 0x20
   __DATA_CONST.__objc_classlist: 0x148
   __DATA_CONST.__objc_protolist: 0x250
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x128
-  __DATA.__objc_const: 0x8568
+  __DATA.__objc_const: 0x84c0
   __DATA.__objc_selrefs: 0xfd8
   __DATA.__objc_data: 0x1228
-  __DATA.__data: 0x10c90
-  __DATA.__common: 0xa28
+  __DATA.__data: 0x10b58
+  __DATA.__common: 0xa08
   __DATA.__bss: 0x53340
   - /System/Library/Frameworks/Combine.framework/Combine
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 512F7AD6-D53E-3F53-855A-EA02C3DBF413
-  Functions: 20356
-  Symbols:   2066
-  CStrings:  3900
+  UUID: 78FBC603-E1E2-34A9-AC6E-86E79180E431
+  Functions: 20325
+  Symbols:   2068
+  CStrings:  3909
 
Symbols:
+ _$s9WiFiAware23WABrowserAgentInterfaceO0E10ToEndpointV6decode4fromAE10Foundation4DataV_tKFZ
+ _$s9WiFiAware23WABrowserAgentInterfaceO0E10ToEndpointV6deviceAA14WAPairedDeviceVvg
CStrings:
+ "#### BrowserClient for :%@ ID: %s"
+ "#### Connection Terminated error:%ld"
+ "#### No Devices Resolve Endpoint"
+ "#### Publisher state %s"
+ "#### Terminated InBoundConnection %s error: %ld"
+ "#### Terminating BrowserClient for :%@ ID: %s"
+ "#### subscriber state %s"
+ "%@ received datapath response with status %s from responder data address: %s [NMI: %s]"
+ "?"
+ "Core analytics periodic timer fired for App datacollection : %s"
+ "Failed to fetch WABrowseResult in resolve endpoint"
+ "Ignore result: Datapath inprogress"
+ "Peer: %s [NMI: %s]"
+ "Praveen : No app usage data available. Skipping system statistics submission."
+ "Praveen : submitSystemStatistics : %s"
+ "Praveen : updateAppSessionInformation : %s"
+ "WiFiAwarePairingStoreInstance[%@] Invalidating unauthorized connection: %@"
+ "WiFiP2P-826.105 Jul 25 2025 22:07:17"
+ "[WAAnalytics] Timeout waiting for WiFi analytics query for %s"
+ "responderNMIAddress"
+ "service being monitored for: %s"
+ "xpcConnection"
- "#### BrowserClient for :%@"
- "#### Connection Terminated"
- "#### publisherRunning %{bool}d"
- "#### subscriberRunning"
- "%@ received datapath response with status %s from responder data address: %s"
- "Core analytics periodic timer fired for App datacollection"
- "Failed to retrieve core-analytics performance report"
- "No app usage data available. Skipping system statistics submission."
- "Pairing Metadat: %s"
- "WiFiP2P-826.101 Jul 12 2025 01:07:11"
- "[Datapath Performance] ID: %hhu: %s, Query samplePeerStats on init ok"
- "performanceCoreAnalytics"
- "service is already being monitored for: %s"

```
