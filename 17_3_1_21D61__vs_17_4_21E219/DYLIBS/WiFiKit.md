## WiFiKit

> `/System/Library/PrivateFrameworks/WiFiKit.framework/WiFiKit`

```diff

-878.7.0.0.0
-  __TEXT.__text: 0x8f3f8
+885.19.0.0.0
+  __TEXT.__text: 0x8f840
   __TEXT.__auth_stubs: 0x14c0
-  __TEXT.__objc_methlist: 0x7e2c
+  __TEXT.__objc_methlist: 0x7e44
   __TEXT.__const: 0x188
-  __TEXT.__oslogstring: 0xa0b2
-  __TEXT.__cstring: 0xa530
+  __TEXT.__oslogstring: 0xa132
+  __TEXT.__cstring: 0xa5d8
   __TEXT.__gcc_except_tab: 0x1878
   __TEXT.__dlopen_cstrs: 0xac
   __TEXT.__ustring: 0x44
-  __TEXT.__unwind_info: 0x1a44
+  __TEXT.__unwind_info: 0x1a48
   __TEXT.__objc_classname: 0xe17
-  __TEXT.__objc_methname: 0x14582
+  __TEXT.__objc_methname: 0x1466e
   __TEXT.__objc_methtype: 0x29f5
   __TEXT.__objc_stubs: 0xdca0
   __DATA_CONST.__got: 0x550

   __DATA_CONST.__objc_catlist: 0x68
   __DATA_CONST.__objc_protolist: 0x158
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x181a0
-  __DATA_CONST.__objc_selrefs: 0x46f0
+  __DATA_CONST.__objc_const: 0x181d0
+  __DATA_CONST.__objc_selrefs: 0x4700
+  __DATA_CONST.__objc_protorefs: 0x18
+  __DATA_CONST.__objc_classrefs: 0x658
+  __DATA_CONST.__objc_superrefs: 0x288
   __DATA_CONST.__objc_arraydata: 0x188
   __AUTH_CONST.__objc_const: 0x2598
   __AUTH_CONST.__cfstring: 0x69e0

   __AUTH_CONST.__const: 0x3a0
   __AUTH_CONST.__auth_got: 0xa70
   __AUTH.__objc_data: 0x15e0
-  __DATA.__objc_protorefs: 0x18
-  __DATA.__objc_classrefs: 0x658
-  __DATA.__objc_superrefs: 0x288
-  __DATA.__objc_ivar: 0xb70
+  __DATA.__objc_ivar: 0xb74
   __DATA.__data: 0x1290
   __DATA.__bss: 0xc8
   __DATA_DIRTY.__objc_data: 0xa50

   - /usr/lib/libSystemHealth.dylib
   - /usr/lib/libnetquality.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 18AF7C5F-DFA1-328F-949A-A1D597F4705C
-  Functions: 3119
-  Symbols:   11120
-  CStrings:  7229
+  UUID: 2CF56623-3380-3935-8E12-B5600378F623
+  Functions: 3121
+  Symbols:   11125
+  CStrings:  7248
 
Symbols:
+ -[WFClient setStateMonitorQueue:]
+ -[WFClient stateMonitorQueue]
+ _OBJC_IVAR_$_WFClient._stateMonitorQueue
+ ___23-[WFClient setPowered:]_block_invoke.109
+ ___25-[WFClient asyncPowered:]_block_invoke.111
+ ___26-[WFClient asyncMISState:]_block_invoke.148
+ ___35-[WFClient asyncMISDiscoveryState:]_block_invoke.149
+ ___35-[WFClient asyncUserAutoJoinState:]_block_invoke.146
+ ___37-[WFClient setPoweredToggle:handler:]_block_invoke.110
+ ___56-[WFClient _startMonitoringCoreWiFiEventsWithInterface:]_block_invoke.100
+ ___56-[WFClient _startMonitoringCoreWiFiEventsWithInterface:]_block_invoke.77
+ ___56-[WFClient _startMonitoringCoreWiFiEventsWithInterface:]_block_invoke.81
+ ___60-[WFNetworkListController _updatePrivacyProxyFeatureEnabled]_block_invoke.497
+ ___60-[WFNetworkListController _updatePrivacyProxyFeatureEnabled]_block_invoke.500
+ ___60-[WFNetworkListController _updatePrivacyProxyFeatureEnabled]_block_invoke_2.498
+ ___63-[WFNetworkListController _refreshKnownHiddenNetworkNamesCache]_block_invoke.507
+ ___84-[WFNetworkListController networkListViewController:showSettingsForNetwork:context:]_block_invoke.370
+ ___84-[WFNetworkListController networkListViewController:showSettingsForNetwork:context:]_block_invoke.372
+ ___84-[WFNetworkListController networkListViewController:showSettingsForNetwork:context:]_block_invoke.374
+ ___84-[WFNetworkListController networkListViewController:showSettingsForNetwork:context:]_block_invoke.376
+ ___block_literal_global.397
+ ___block_literal_global.435
+ ___block_literal_global.489
+ ___block_literal_global.495
- ___23-[WFClient setPowered:]_block_invoke.108
- ___25-[WFClient asyncPowered:]_block_invoke_2
- ___26-[WFClient asyncMISState:]_block_invoke.146
- ___35-[WFClient asyncMISDiscoveryState:]_block_invoke.147
- ___35-[WFClient asyncUserAutoJoinState:]_block_invoke.144
- ___37-[WFClient setPoweredToggle:handler:]_block_invoke.109
- ___56-[WFClient _startMonitoringCoreWiFiEventsWithInterface:]_block_invoke.76
- ___56-[WFClient _startMonitoringCoreWiFiEventsWithInterface:]_block_invoke.80
- ___56-[WFClient _startMonitoringCoreWiFiEventsWithInterface:]_block_invoke.99
- ___60-[WFNetworkListController _updatePrivacyProxyFeatureEnabled]_block_invoke.496
- ___60-[WFNetworkListController _updatePrivacyProxyFeatureEnabled]_block_invoke.499
- ___60-[WFNetworkListController _updatePrivacyProxyFeatureEnabled]_block_invoke_2.497
- ___63-[WFNetworkListController _refreshKnownHiddenNetworkNamesCache]_block_invoke.506
- ___84-[WFNetworkListController networkListViewController:showSettingsForNetwork:context:]_block_invoke.365
- ___84-[WFNetworkListController networkListViewController:showSettingsForNetwork:context:]_block_invoke.371
- ___84-[WFNetworkListController networkListViewController:showSettingsForNetwork:context:]_block_invoke.373
- ___84-[WFNetworkListController networkListViewController:showSettingsForNetwork:context:]_block_invoke.375
- ___block_literal_global.390
- ___block_literal_global.434
- ___block_literal_global.488
- ___block_literal_global.494
CStrings:
+ "%s: Entering WFClient stateMonitorQueue"
+ "%s: querying current network's IP from en0."
+ "%s: querying current network's IP from ir0."
+ "-[WFClient _startMonitoringCoreWiFiEventsWithInterface:]_block_invoke_2"
+ "-[WFClient asyncPowered:]_block_invoke"
+ "-[WFInterface _currentInterface]"
+ "A\"\x14"
+ "T@\"NSObject<OS_dispatch_queue>\",&,N,V_stateMonitorQueue"
+ "T@\"NSString\",?,C,N"
+ "T@\"NSString\",?,N"
+ "T@\"NSString\",?,R,C"
+ "T@\"NSString\",?,R,C,N"
+ "T@,?,R,N"
+ "T@?,?,C,N"
+ "T@?,?,C,N,V_credentialsTappedHandler"
+ "TB,?,N"
+ "TB,?,N,GisJoinable"
+ "TB,?,N,GisJoinable,V_joinable"
+ "TB,?,R,N"
+ "TB,?,R,N,GisCredentialsVisible"
+ "TB,?,R,N,GisWifiModeConfigurable"
+ "TB,?,R,N,VwantsModalPresentation"
+ "TQ,?,R,N"
+ "Tq,?,R,N"
+ "WFWiFiStateMonitorQueue"
+ "_stateMonitorQueue"
+ "setStateMonitorQueue:"
+ "stateMonitorQueue"
- "A\"\x13"
- "T@\"NSString\",N"
- "T@,R,N"
- "T@?,C,N,V_credentialsTappedHandler"
- "TB,N,GisJoinable"
- "TB,N,GisJoinable,V_joinable"
- "TB,R,N,GisCredentialsVisible"
- "TB,R,N,GisWifiModeConfigurable"
- "TB,R,N,VwantsModalPresentation"

```
