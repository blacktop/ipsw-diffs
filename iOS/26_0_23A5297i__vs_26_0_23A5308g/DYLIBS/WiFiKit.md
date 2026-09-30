## WiFiKit

> `/System/Library/PrivateFrameworks/WiFiKit.framework/WiFiKit`

```diff

-1151.89.0.0.0
-  __TEXT.__text: 0x9bb68
-  __TEXT.__auth_stubs: 0x1600
-  __TEXT.__objc_methlist: 0x9670
+1151.93.0.0.0
+  __TEXT.__text: 0x9be5c
+  __TEXT.__auth_stubs: 0x1610
+  __TEXT.__objc_methlist: 0x96e0
   __TEXT.__const: 0x283
-  __TEXT.__oslogstring: 0xb0ae
-  __TEXT.__cstring: 0xb55d
-  __TEXT.__gcc_except_tab: 0x2c60
+  __TEXT.__oslogstring: 0xb0f1
+  __TEXT.__cstring: 0xb599
+  __TEXT.__gcc_except_tab: 0x2c74
   __TEXT.__dlopen_cstrs: 0xac
   __TEXT.__ustring: 0x44
-  __TEXT.__unwind_info: 0x1c90
+  __TEXT.__unwind_info: 0x1ca8
   __TEXT.__objc_classname: 0xe54
-  __TEXT.__objc_methname: 0x158cc
+  __TEXT.__objc_methname: 0x159ed
   __TEXT.__objc_methtype: 0x3053
   __TEXT.__objc_stubs: 0xe780
   __DATA_CONST.__got: 0xbf8

   __DATA_CONST.__objc_catlist: 0x70
   __DATA_CONST.__objc_protolist: 0x158
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4d58
+  __DATA_CONST.__objc_selrefs: 0x4d90
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x298
   __DATA_CONST.__objc_arraydata: 0x1a0
-  __AUTH_CONST.__auth_got: 0xb10
+  __AUTH_CONST.__auth_got: 0xb18
   __AUTH_CONST.__const: 0x540
   __AUTH_CONST.__cfstring: 0x6f00
-  __AUTH_CONST.__objc_const: 0x18dd8
+  __AUTH_CONST.__objc_const: 0x18e78
   __AUTH_CONST.__objc_intobj: 0x660
   __AUTH_CONST.__objc_arrayobj: 0x1e0
   __AUTH.__objc_data: 0x1630
-  __DATA.__objc_ivar: 0xbb0
+  __DATA.__objc_ivar: 0xbbc
   __DATA.__data: 0x13c0
   __DATA.__bss: 0x108
   __DATA_DIRTY.__objc_data: 0xaa0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libSystemHealth.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 90AF84B0-A4DA-3CE5-82CB-3A44F9CC01B0
-  Functions: 3411
-  Symbols:   12044
-  CStrings:  7689
+  UUID: B24DF558-EFAD-3A6D-A42D-28A8E46856BF
+  Functions: 3423
+  Symbols:   12071
+  CStrings:  7705
 
Symbols:
+ -[WFControlCenterStateMonitor .cxx_destruct]
+ -[WFControlCenterStateMonitor _getSatelliteAlert:]
+ -[WFControlCenterStateMonitor chinaDevice]
+ -[WFControlCenterStateMonitor performActionFrom:withCompletion:]
+ -[WFControlCenterStateMonitor presenter]
+ -[WFControlCenterStateMonitor satelliteAlertCompletion]
+ -[WFControlCenterStateMonitor setChinaDevice:]
+ -[WFControlCenterStateMonitor setPresenter:]
+ -[WFControlCenterStateMonitor setSatelliteAlertCompletion:]
+ GCC_except_table14
+ GCC_except_table20
+ _OBJC_IVAR_$_WFControlCenterStateMonitor._chinaDevice
+ _OBJC_IVAR_$_WFControlCenterStateMonitor._presenter
+ _OBJC_IVAR_$_WFControlCenterStateMonitor._satelliteAlertCompletion
+ __NETRBEtherAton
+ __NETRBEtherNtoa
+ __NETRBInterfaceIsMacAddrValid
+ __OBJC_$_INSTANCE_VARIABLES_WFControlCenterStateMonitor
+ __OBJC_$_PROP_LIST_WFControlCenterStateMonitor
+ ___53-[WFNetworkListController _associateToHotspotDevice:]_block_invoke.168
+ ___53-[WFNetworkListController _associateToHotspotDevice:]_block_invoke.173
+ ___56-[WFNetworkListController _updateCurrentNetworkIPState:]_block_invoke.265
+ ___57-[WFNetworkListController _canStartAssociationToNetwork:]_block_invoke.253
+ ___59-[WFNetworkListController _associateToUserSuppliedNetwork:]_block_invoke.221
+ ___59-[WFNetworkListController _associateToUserSuppliedNetwork:]_block_invoke.223
+ ___59-[WFNetworkListController _updateViewControllerScanResults]_block_invoke.131
+ ___59-[WFNetworkListController _updateViewControllerScanResults]_block_invoke.142
+ ___59-[WFNetworkListController _updateViewControllerScanResults]_block_invoke.144
+ ___62-[WFNetworkListController _scanNetworkForAssociation:profile:]_block_invoke.261
+ ___63-[WFNetworkListController _associationDidFinish:error:network:]_block_invoke.258
+ ___64-[WFNetworkListController _promptCredentialsForNetwork:profile:]_block_invoke.241
+ ___64-[WFNetworkListController _promptCredentialsForNetwork:profile:]_block_invoke.247
+ ___69-[WFNetworkListController _canStartAssociationToUserSuppliedNetwork:]_block_invoke.255
+ ___74-[WFNetworkListController _associateToUserSuppliedNetworkHelper:networks:]_block_invoke.226
+ ___99-[WFNetworkListController _handleAssociationError:network:profile:securityMode:associationContext:]_block_invoke.229
+ ___99-[WFNetworkListController _handleAssociationError:network:profile:securityMode:associationContext:]_block_invoke.231
+ ___99-[WFNetworkListController _handleAssociationError:network:profile:securityMode:associationContext:]_block_invoke_2.230
+ ___99-[WFNetworkListController _handleAssociationError:network:profile:securityMode:associationContext:]_block_invoke_2.233
+ ___block_descriptor_tmp.202
+ ___block_descriptor_tmp.205
+ ___block_descriptor_tmp.209
+ ___block_descriptor_tmp.227
+ ___block_descriptor_tmp.228
+ ___block_descriptor_tmp.257
+ ___block_descriptor_tmp.258
+ ___block_descriptor_tmp.263
+ ___block_descriptor_tmp.267
+ ___block_descriptor_tmp.271
+ ___block_descriptor_tmp.272
+ ___block_descriptor_tmp.275
+ ___block_descriptor_tmp.280
+ ___block_descriptor_tmp.283
+ ___block_literal_global.207
+ ___block_literal_global.211
+ ___block_literal_global.236
+ ___block_literal_global.260
+ ___block_literal_global.265
+ ___block_literal_global.269
+ ___block_literal_global.274
+ ___block_literal_global.277
+ ___block_literal_global.282
+ ___block_literal_global.285
+ _objc_msgSend$setPresenter:
+ _sscanf
- ___53-[WFNetworkListController _associateToHotspotDevice:]_block_invoke.166
- ___53-[WFNetworkListController _associateToHotspotDevice:]_block_invoke.171
- ___56-[WFNetworkListController _updateCurrentNetworkIPState:]_block_invoke.264
- ___57-[WFNetworkListController _canStartAssociationToNetwork:]_block_invoke.250
- ___59-[WFNetworkListController _associateToUserSuppliedNetwork:]_block_invoke.220
- ___59-[WFNetworkListController _associateToUserSuppliedNetwork:]_block_invoke.222
- ___59-[WFNetworkListController _updateViewControllerScanResults]_block_invoke.130
- ___59-[WFNetworkListController _updateViewControllerScanResults]_block_invoke.141
- ___59-[WFNetworkListController _updateViewControllerScanResults]_block_invoke.143
- ___62-[WFNetworkListController _scanNetworkForAssociation:profile:]_block_invoke.260
- ___63-[WFNetworkListController _associationDidFinish:error:network:]_block_invoke.257
- ___64-[WFNetworkListController _promptCredentialsForNetwork:profile:]_block_invoke.239
- ___64-[WFNetworkListController _promptCredentialsForNetwork:profile:]_block_invoke.246
- ___69-[WFNetworkListController _canStartAssociationToUserSuppliedNetwork:]_block_invoke.254
- ___74-[WFNetworkListController _associateToUserSuppliedNetworkHelper:networks:]_block_invoke.225
- ___99-[WFNetworkListController _handleAssociationError:network:profile:securityMode:associationContext:]_block_invoke.228
- ___99-[WFNetworkListController _handleAssociationError:network:profile:securityMode:associationContext:]_block_invoke.230
- ___99-[WFNetworkListController _handleAssociationError:network:profile:securityMode:associationContext:]_block_invoke_2.229
- ___99-[WFNetworkListController _handleAssociationError:network:profile:securityMode:associationContext:]_block_invoke_2.232
- ___block_descriptor_tmp.200
- ___block_descriptor_tmp.203
- ___block_descriptor_tmp.207
- ___block_descriptor_tmp.225
- ___block_descriptor_tmp.226
- ___block_descriptor_tmp.254
- ___block_descriptor_tmp.255
- ___block_descriptor_tmp.261
- ___block_descriptor_tmp.265
- ___block_descriptor_tmp.269
- ___block_descriptor_tmp.270
- ___block_descriptor_tmp.273
- ___block_descriptor_tmp.278
- ___block_descriptor_tmp.281
- ___block_literal_global.205
- ___block_literal_global.209
- ___block_literal_global.235
- ___block_literal_global.258
- ___block_literal_global.263
- ___block_literal_global.267
- ___block_literal_global.272
- ___block_literal_global.275
- ___block_literal_global.280
- ___block_literal_global.283
- _objc_msgSend$setWithSet:
CStrings:
+ "%02x:%02x:%02x:%02x:%02x:%02x"
+ "%hhx:%hhx:%hhx:%hhx:%hhx:%hhx"
+ "T@\"UIViewController\",&,N,V_presenter"
+ "T@?,C,N,V_satelliteAlertCompletion"
+ "TB,N,V_chinaDevice"
+ "_chinaDevice"
+ "_getSatelliteAlert:"
+ "_presenter"
+ "_satelliteAlertCompletion"
+ "chinaDevice"
+ "initializing WFControlCenterStateMonitor with presenter for alerts"
+ "performActionFrom:withCompletion:"
+ "presenter"
+ "satelliteAlertCompletion"
+ "setChinaDevice:"
+ "setPresenter:"
+ "setSatelliteAlertCompletion:"
- "setWithSet:"

```
