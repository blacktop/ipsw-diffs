## WiFiKit

> `/System/Library/PrivateFrameworks/WiFiKit.framework/WiFiKit`

```diff

-1110.1.0.0.0
-  __TEXT.__text: 0x9704c
-  __TEXT.__auth_stubs: 0x1530
-  __TEXT.__objc_methlist: 0x9448
-  __TEXT.__const: 0x270
-  __TEXT.__oslogstring: 0xa9f3
-  __TEXT.__cstring: 0xaca5
-  __TEXT.__gcc_except_tab: 0x2b04
+1151.73.0.0.0
+  __TEXT.__text: 0x9b290
+  __TEXT.__auth_stubs: 0x15f0
+  __TEXT.__objc_methlist: 0x9628
+  __TEXT.__const: 0x283
+  __TEXT.__oslogstring: 0xaf69
+  __TEXT.__cstring: 0xb539
+  __TEXT.__gcc_except_tab: 0x2bf4
   __TEXT.__dlopen_cstrs: 0xac
   __TEXT.__ustring: 0x44
-  __TEXT.__unwind_info: 0x1be8
-  __TEXT.__objc_classname: 0xe3d
-  __TEXT.__objc_methname: 0x14f39
-  __TEXT.__objc_methtype: 0x2c3c
-  __TEXT.__objc_stubs: 0xe240
-  __DATA_CONST.__got: 0xbc8
-  __DATA_CONST.__const: 0x23e0
-  __DATA_CONST.__objc_classlist: 0x340
+  __TEXT.__unwind_info: 0x1c88
+  __TEXT.__objc_classname: 0xe54
+  __TEXT.__objc_methname: 0x15705
+  __TEXT.__objc_methtype: 0x3016
+  __TEXT.__objc_stubs: 0xe640
+  __DATA_CONST.__got: 0xbf0
+  __DATA_CONST.__const: 0x2610
+  __DATA_CONST.__objc_classlist: 0x348
   __DATA_CONST.__objc_catlist: 0x70
   __DATA_CONST.__objc_protolist: 0x158
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4b90
+  __DATA_CONST.__objc_selrefs: 0x4d00
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x290
-  __DATA_CONST.__objc_arraydata: 0x198
-  __AUTH_CONST.__auth_got: 0xaa8
-  __AUTH_CONST.__const: 0x3a0
-  __AUTH_CONST.__cfstring: 0x6e00
-  __AUTH_CONST.__objc_const: 0x18b58
-  __AUTH_CONST.__objc_intobj: 0x648
+  __DATA_CONST.__objc_superrefs: 0x298
+  __DATA_CONST.__objc_arraydata: 0x1a0
+  __AUTH_CONST.__auth_got: 0xb08
+  __AUTH_CONST.__const: 0x540
+  __AUTH_CONST.__cfstring: 0x6ee0
+  __AUTH_CONST.__objc_const: 0x18da8
+  __AUTH_CONST.__objc_intobj: 0x660
   __AUTH_CONST.__objc_arrayobj: 0x1e0
-  __AUTH.__objc_data: 0x15e0
-  __DATA.__objc_ivar: 0xb90
-  __DATA.__data: 0x1330
-  __DATA.__bss: 0xc8
+  __AUTH.__objc_data: 0x1630
+  __DATA.__objc_ivar: 0xbac
+  __DATA.__data: 0x13b8
+  __DATA.__bss: 0x108
   __DATA_DIRTY.__objc_data: 0xaa0
-  __DATA_DIRTY.__bss: 0x98
+  __DATA_DIRTY.__bss: 0x91
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/AccessorySetupKit.framework/AccessorySetupKit
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork

   - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration
   - /System/Library/PrivateFrameworks/MobileStoreDemoKit.framework/MobileStoreDemoKit
   - /System/Library/PrivateFrameworks/MobileWiFi.framework/MobileWiFi
+  - /System/Library/PrivateFrameworks/NetworkQuality.framework/NetworkQuality
   - /System/Library/PrivateFrameworks/NetworkServiceProxy.framework/NetworkServiceProxy
   - /System/Library/PrivateFrameworks/OnBoardingKit.framework/OnBoardingKit
   - /System/Library/PrivateFrameworks/Preferences.framework/Preferences

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libSystemHealth.dylib
-  - /usr/lib/libnetquality.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: CA4AC8A4-C421-3548-9B6C-80305FFEDC68
-  Functions: 3324
-  Symbols:   11751
-  CStrings:  7476
+  UUID: F34A1A4D-3DBA-3529-9669-828B39C4D547
+  Functions: 3403
+  Symbols:   12014
+  CStrings:  7663
 
Symbols:
+ +[CWFInterface(WiFiKit) nearbyCaptiveAssistRecommendationUIFeatureEnabled]
+ -[WFAssociationContextQueue _queueCount]
+ -[WFClient _updateWiFiUIFlagsState]
+ -[WFClient setWifiUIStateFlags:]
+ -[WFClient wifiUIStateFlags]
+ -[WFContentCachesContext .cxx_destruct]
+ -[WFContentCachesContext cacheLocatorSettingsInstance]
+ -[WFContentCachesContext delegate]
+ -[WFContentCachesContext init]
+ -[WFContentCachesContext numOfContentCaches]
+ -[WFContentCachesContext setCacheLocatorSettingsInstance:]
+ -[WFContentCachesContext setDelegate:]
+ -[WFContentCachesContext setNumOfContentCaches:]
+ -[WFDetailsContext contentCachesContext]
+ -[WFDetailsContext setContentCachesContext:]
+ -[WFEnterpriseJoinOperation __hasPrivateMACUserJoinFailureUIState:]
+ -[WFHealthIssueOverrides poorCoverageOverride]
+ -[WFHealthIssueOverrides setPoorCoverageOverride:]
+ -[WFHealthManager noInternetTestQueue]
+ -[WFHealthManager setNoInternetTestQueue:]
+ -[WFIPMonitor __isIPConfigurationPrimaryForProperty:]
+ -[WFIPMonitor isIPv4Primary]
+ -[WFIPMonitor isIPv6Primary]
+ -[WFInterface hasPrimaryIPConfiguration]
+ -[WFJoinOperation __hasPrivateMACUserJoinFailureUIState:]
+ -[WFNetworkListController contentCachesContext]
+ -[WFNetworkListController initWithViewController:viewProvider:client:].cold.1
+ -[WFNetworkListController setContentCachesContext:]
+ -[WFNetworkSettingsCellFactory contentCachesCellAtIndexPath:]
+ -[WFPortalContext fullPortalURLString]
+ -[WFPortalContext initWithCaptiveProfile:anqpVenueURLs:]
+ -[WFPortalContext portalHostnameForDisplay]
+ -[WFWiFiStateMonitor _wifiUIFlagsStateChanged:]
+ GCC_except_table10
+ GCC_except_table40
+ GCC_except_table48
+ GCC_except_table50
+ GCC_except_table59
+ _CWFPrivateMACAddressUserJoinFailureUIStateKey
+ _NSClassFromString
+ _OBJC_CLASS_$_NSURLComponents
+ _OBJC_CLASS_$_WFContentCachesContext
+ _OBJC_IVAR_$_WFClient._wifiUIStateFlags
+ _OBJC_IVAR_$_WFContentCachesContext._cacheLocatorSettingsInstance
+ _OBJC_IVAR_$_WFContentCachesContext._delegate
+ _OBJC_IVAR_$_WFContentCachesContext._numOfContentCaches
+ _OBJC_IVAR_$_WFDetailsContext._contentCachesContext
+ _OBJC_IVAR_$_WFHealthIssueOverrides._poorCoverageOverride
+ _OBJC_IVAR_$_WFHealthManager._noInternetTestQueue
+ _OBJC_IVAR_$_WFNetworkListController._contentCachesContext
+ _OBJC_METACLASS_$_WFContentCachesContext
+ _OUTLINED_FUNCTION_11
+ _SCDynamicStoreKeyCreateNetworkGlobalEntity
+ _WFClientWiFiUIFlagsStateChangedNotification
+ __NETRBCreateNetwork
+ __NETRBCreateNetwork.cold.1
+ __NETRBCreateNetworkConfiguration
+ __NETRBCreateNetworkConfiguration.cold.1
+ __NETRBDeserializeNetwork
+ __NETRBDeserializeNetwork.cold.1
+ __NETRBDeserializeNetworkConfig
+ __NETRBInterfaceGetMacAddr
+ __NETRBInterfaceGetMtu
+ __NETRBInterfaceGetSocketFd
+ __NETRBInterfaceGetTypeId.pred
+ __NETRBInterfaceGetUUID
+ __NETRBInterfaceTypeId
+ __NETRBNetworkAddDHCPReservation
+ __NETRBNetworkAddPortForwardingRule
+ __NETRBNetworkClient
+ __NETRBNetworkClientRefCnt
+ __NETRBNetworkCopy
+ __NETRBNetworkCopy.cold.1
+ __NETRBNetworkDisableDHCP
+ __NETRBNetworkDisableDNSProxy
+ __NETRBNetworkDisableNAT44
+ __NETRBNetworkDisableNAT66
+ __NETRBNetworkDisableRouterAdvertisement
+ __NETRBNetworkGetConfigHandle
+ __NETRBNetworkGetIPv4Subnet
+ __NETRBNetworkGetIPv6Prefix
+ __NETRBNetworkGetTypeId.pred
+ __NETRBNetworkSetExternalInterface
+ __NETRBNetworkSetFlags
+ __NETRBNetworkSetIPv4Addresses
+ __NETRBNetworkSetIPv6Prefix
+ __NETRBNetworkSetMtu
+ __NETRBNetworkStartVirtualMachineInterface
+ __NETRBNetworkStartVirtualMachineInterface.cold.1
+ __NETRBNetworkStartVirtualMachineInterface.cold.2
+ __NETRBNetworkTypeId
+ __NETRBSerializeNetwork
+ __OBJC_$_CATEGORY_CLASS_METHODS_CWFInterface_$_WiFiKit
+ __OBJC_$_INSTANCE_METHODS_WFContentCachesContext
+ __OBJC_$_INSTANCE_VARIABLES_WFContentCachesContext
+ __OBJC_$_PROP_LIST_WFContentCachesContext
+ __OBJC_CLASS_RO_$_WFContentCachesContext
+ __OBJC_METACLASS_RO_$_WFContentCachesContext
+ ___101-[WFNetworkListController networkListViewController:showSettingsForNetwork:context:scrollToCellType:]_block_invoke.335
+ ___101-[WFNetworkListController networkListViewController:showSettingsForNetwork:context:scrollToCellType:]_block_invoke.337
+ ___101-[WFNetworkListController networkListViewController:showSettingsForNetwork:context:scrollToCellType:]_block_invoke.389
+ ___101-[WFNetworkListController networkListViewController:showSettingsForNetwork:context:scrollToCellType:]_block_invoke.391
+ ___101-[WFNetworkListController networkListViewController:showSettingsForNetwork:context:scrollToCellType:]_block_invoke.392
+ ___101-[WFNetworkListController networkListViewController:showSettingsForNetwork:context:scrollToCellType:]_block_invoke.394
+ ___101-[WFNetworkListController networkListViewController:showSettingsForNetwork:context:scrollToCellType:]_block_invoke.396
+ ___101-[WFNetworkListController networkListViewController:showSettingsForNetwork:context:scrollToCellType:]_block_invoke.398
+ ___23-[WFClient setPowered:]_block_invoke.124
+ ___25-[WFClient asyncPowered:]_block_invoke.126
+ ___26-[WFClient asyncMISState:]_block_invoke.163
+ ___30-[WFContentCachesContext init]_block_invoke
+ ___30-[WFContentCachesContext init]_block_invoke_2
+ ___35-[WFClient _updateWiFiUIFlagsState]_block_invoke
+ ___35-[WFClient asyncMISDiscoveryState:]_block_invoke.164
+ ___35-[WFClient asyncUserAutoJoinState:]_block_invoke.161
+ ___35-[WFWiFiStateMonitor _updateState:]_block_invoke.43
+ ___35-[WFWiFiStateMonitor _updateState:]_block_invoke.44
+ ___37-[WFClient setPoweredToggle:handler:]_block_invoke.125
+ ___37-[WFWiFiStateMonitor startMonitoring]_block_invoke.15
+ ___41-[WFWiFiStateMonitor _updateWiFiUIState:]_block_invoke.50
+ ___41-[WFWiFiStateMonitor _updateWiFiUIState:]_block_invoke_2
+ ___43-[WFHealthManager runNoInternetDiagnostics]_block_invoke.21
+ ___44-[WFNetworkListController _updatePowerState]_block_invoke.114
+ ___44-[WFNetworkListController _updatePowerState]_block_invoke.115
+ ___53-[WFIPMonitor __isIPConfigurationPrimaryForProperty:]_block_invoke
+ ___53-[WFNetworkListController _associateToHotspotDevice:]_block_invoke.166
+ ___53-[WFNetworkListController _associateToHotspotDevice:]_block_invoke.167
+ ___53-[WFNetworkListController _associateToHotspotDevice:]_block_invoke.171
+ ___53-[WFNetworkListController _associateToHotspotDevice:]_block_invoke.172
+ ___56-[WFClient _startMonitoringCoreWiFiEventsWithInterface:]_block_invoke.115
+ ___56-[WFClient _startMonitoringCoreWiFiEventsWithInterface:]_block_invoke.78
+ ___56-[WFClient _startMonitoringCoreWiFiEventsWithInterface:]_block_invoke.84
+ ___56-[WFClient _startMonitoringCoreWiFiEventsWithInterface:]_block_invoke.88
+ ___56-[WFClient _startMonitoringCoreWiFiEventsWithInterface:]_block_invoke.89
+ ___56-[WFClient _startMonitoringCoreWiFiEventsWithInterface:]_block_invoke_2.91
+ ___56-[WFNetworkListController _updateCurrentNetworkIPState:]_block_invoke.264
+ ___57-[WFNetworkListController _canStartAssociationToNetwork:]_block_invoke.250
+ ___57-[WFNetworkListController _canStartAssociationToNetwork:]_block_invoke.251
+ ___57-[WFNetworkListController _canStartAssociationToNetwork:]_block_invoke.252
+ ___58-[WFNetworkListController _applicationDidEnterBackground:]_block_invoke.100
+ ___59-[WFNetworkListController _associateToUserSuppliedNetwork:]_block_invoke.220
+ ___59-[WFNetworkListController _associateToUserSuppliedNetwork:]_block_invoke.222
+ ___59-[WFNetworkListController _updateViewControllerScanResults]_block_invoke.130
+ ___59-[WFNetworkListController _updateViewControllerScanResults]_block_invoke.141
+ ___59-[WFNetworkListController _updateViewControllerScanResults]_block_invoke.143
+ ___60-[WFNetworkListController _updatePrivacyProxyFeatureEnabled]_block_invoke.551
+ ___60-[WFNetworkListController _updatePrivacyProxyFeatureEnabled]_block_invoke.554
+ ___60-[WFNetworkListController _updatePrivacyProxyFeatureEnabled]_block_invoke_2.552
+ ___62-[WFNetworkListController _scanNetworkForAssociation:profile:]_block_invoke.260
+ ___63-[WFNetworkListController _associationDidFinish:error:network:]_block_invoke.257
+ ___63-[WFNetworkListController _refreshKnownHiddenNetworkNamesCache]_block_invoke.561
+ ___64-[WFNetworkListController _promptCredentialsForNetwork:profile:]_block_invoke.239
+ ___64-[WFNetworkListController _promptCredentialsForNetwork:profile:]_block_invoke.246
+ ___69-[WFNetworkListController _canStartAssociationToUserSuppliedNetwork:]_block_invoke.254
+ ___71-[WFNetworkListController networkListViewControllerDidTapOtherNetwork:]_block_invoke.302
+ ___71-[WFNetworkListController networkListViewControllerDidTapOtherNetwork:]_block_invoke.303
+ ___74-[WFNetworkListController _associateToUserSuppliedNetworkHelper:networks:]_block_invoke.225
+ ___99-[WFNetworkListController _handleAssociationError:network:profile:securityMode:associationContext:]_block_invoke.228
+ ___99-[WFNetworkListController _handleAssociationError:network:profile:securityMode:associationContext:]_block_invoke.230
+ ___99-[WFNetworkListController _handleAssociationError:network:profile:securityMode:associationContext:]_block_invoke_2.229
+ ___99-[WFNetworkListController _handleAssociationError:network:profile:securityMode:associationContext:]_block_invoke_2.232
+ ___NETRBInterfaceRelease
+ ___NETRBInterfaceRelease.cold.1
+ ___NETRBNetworkCreateGlobalClient
+ ___NETRBNetworkCreateGlobalClient.cold.1
+ ___NETRBNetworkGetServiceQueue.__networkServiceQueue
+ ___NETRBNetworkGetServiceQueue.__networkServiceQueueName
+ ___NETRBNetworkGetServiceQueue.predNetworkQueue
+ ___NETRBNetworkRelease
+ ____NETRBCreateNetwork_block_invoke
+ ____NETRBCreateNetwork_block_invoke_2
+ ____NETRBInterfaceGetTypeId_block_invoke
+ ____NETRBNetworkGetTypeId_block_invoke
+ ____NETRBNetworkStartVirtualMachineInterface_block_invoke
+ ____NETRBNetworkStartVirtualMachineInterface_block_invoke_2
+ _____NETRBInterfaceRelease_block_invoke
+ _____NETRBNetworkCreateGlobalClient_block_invoke
+ _____NETRBNetworkCreateGlobalClient_block_invoke.cold.1
+ _____NETRBNetworkCreateGlobalClient_block_invoke_2
+ _____NETRBNetworkGetServiceQueue_block_invoke
+ _____NETRBNetworkReleaseGlobalClient_block_invoke
+ _____NETRBNetworkReleaseGlobalClient_block_invoke.cold.1
+ _____NETRBNetworkRelease_block_invoke
+ ___assert_rtn
+ ___block_descriptor_40_e8_32w_e60_v32?0"NSError"8"<WFDiagnosticsResultItem>"16"NSString"24lw32l8
+ ___block_descriptor_56_e8_32s40s48r_e5_v8?0lr48l8s32l8s40l8
+ ___block_descriptor_56_e8_32w40w_e5_v8?0lw32l8w40l8
+ ___block_descriptor_64_e8_32s40bs48r56r_e45_v24?0"CWFScanResult"8"CWFNetworkProfile"16ls32l8r48l8r56l8s40l8
+ ___block_descriptor_80_e8_32s40r48r56r64r_e5_v8?0lr40l8r48l8s32l8r56l8r64l8
+ ___block_descriptor_tmp.101
+ ___block_descriptor_tmp.102
+ ___block_descriptor_tmp.106
+ ___block_descriptor_tmp.111
+ ___block_descriptor_tmp.115
+ ___block_descriptor_tmp.120
+ ___block_descriptor_tmp.121
+ ___block_descriptor_tmp.124
+ ___block_descriptor_tmp.133
+ ___block_descriptor_tmp.134
+ ___block_descriptor_tmp.138
+ ___block_descriptor_tmp.144
+ ___block_descriptor_tmp.145
+ ___block_descriptor_tmp.148
+ ___block_descriptor_tmp.149
+ ___block_descriptor_tmp.160
+ ___block_descriptor_tmp.164
+ ___block_descriptor_tmp.166
+ ___block_descriptor_tmp.167
+ ___block_descriptor_tmp.168
+ ___block_descriptor_tmp.172
+ ___block_descriptor_tmp.179
+ ___block_descriptor_tmp.191
+ ___block_descriptor_tmp.192
+ ___block_descriptor_tmp.195
+ ___block_descriptor_tmp.200
+ ___block_descriptor_tmp.203
+ ___block_descriptor_tmp.207
+ ___block_descriptor_tmp.225
+ ___block_descriptor_tmp.226
+ ___block_descriptor_tmp.254
+ ___block_descriptor_tmp.255
+ ___block_descriptor_tmp.256
+ ___block_descriptor_tmp.261
+ ___block_descriptor_tmp.265
+ ___block_descriptor_tmp.269
+ ___block_descriptor_tmp.270
+ ___block_descriptor_tmp.273
+ ___block_descriptor_tmp.278
+ ___block_descriptor_tmp.281
+ ___block_descriptor_tmp.60
+ ___block_descriptor_tmp.65
+ ___block_descriptor_tmp.71
+ ___block_descriptor_tmp.75
+ ___block_descriptor_tmp.88
+ ___block_descriptor_tmp.89
+ ___block_descriptor_tmp.92
+ ___block_descriptor_tmp.95
+ ___block_literal_global.118
+ ___block_literal_global.205
+ ___block_literal_global.209
+ ___block_literal_global.235
+ ___block_literal_global.258
+ ___block_literal_global.263
+ ___block_literal_global.267
+ ___block_literal_global.272
+ ___block_literal_global.275
+ ___block_literal_global.280
+ ___block_literal_global.283
+ ___block_literal_global.323
+ ___block_literal_global.457
+ ___block_literal_global.543
+ ___block_literal_global.549
+ ___block_literal_global.77
+ ___memcpy_chk
+ ___netrb_interface_class
+ ___netrb_network_class
+ ___strlcpy_chk
+ __os_signpost_emit_with_name_impl
+ _in6addr_any
+ _kSCDynamicStorePropNetPrimaryInterface
+ _netrbClientRelayAuditToken
+ _netrbNetworkDHCPReservationIPAddr
+ _netrbNetworkDHCPReservationMacAddr
+ _netrbNetworkPortForwardingAddressFamily
+ _netrbNetworkPortForwardingExternalPort
+ _netrbNetworkPortForwardingInternalAddress
+ _netrbNetworkPortForwardingInternalPort
+ _netrbNetworkPortForwardingProtocol
+ _netrbXPCInterfaceId
+ _netrbXPCNetworkAuthorizationToken
+ _netrbXPCNetworkForceRemove
+ _netrbXPCNetworkObject
+ _netrbXPCNetworkObjects
+ _netrbXPCNetworkSerialization
+ _netrbXPCNetworkSerializationDHCPReservation
+ _netrbXPCNetworkSerializationPortForwarding
+ _netrbXPCRelayAuditToken
+ _objc_msgSend$__hasPrivateMACUserJoinFailureUIState:
+ _objc_msgSend$__isIPConfigurationPrimaryForProperty:
+ _objc_msgSend$_queueCount
+ _objc_msgSend$_updateWiFiUIFlagsState
+ _objc_msgSend$addExecutionBlock:
+ _objc_msgSend$contentCachesContext
+ _objc_msgSend$contentCachesContext:didUpdateNumOfContentCaches:
+ _objc_msgSend$deploymentIssues
+ _objc_msgSend$fullPortalURLString
+ _objc_msgSend$hasPrimaryIPConfiguration
+ _objc_msgSend$initWithCaptiveProfile:anqpVenueURLs:
+ _objc_msgSend$isCancelled
+ _objc_msgSend$isCarPlayOnly
+ _objc_msgSend$isDeviceSupervised
+ _objc_msgSend$isIPv4Primary
+ _objc_msgSend$isIPv6Primary
+ _objc_msgSend$isNetworkManagedByMDM:
+ _objc_msgSend$loadAndReturnError:
+ _objc_msgSend$networkProfile
+ _objc_msgSend$noInternetTestQueue
+ _objc_msgSend$operationCount
+ _objc_msgSend$poorCoverageOverride
+ _objc_msgSend$portalHostnameForDisplay
+ _objc_msgSend$privateMACAddressForNetworkProfile:
+ _objc_msgSend$privateMACAddressModeConfigurationProfileSetting
+ _objc_msgSend$privateMACAddressModeForNetworkProfile:
+ _objc_msgSend$scanForCachesOn:withHandler:
+ _objc_msgSend$setContentCachesContext:
+ _objc_msgSend$setNumOfContentCaches:
+ _objc_msgSend$setPrivateMACAddressMode:networkProfile:error:
+ _objc_msgSend$setPrivateMACAddressUserJoinFailureUIState:networkProfile:
+ _objc_msgSend$setVenueInfoURL:
+ _objc_msgSend$underlyingErrors
+ _objc_msgSend$venueURLList
+ _objc_msgSend$wf_popViewControllerAnimated:
+ _objc_msgSend$wf_pushViewController:animated:
+ _os_signpost_enabled
+ _sleep
+ _uuid_compare
+ _uuid_copy
+ _xpc_dictionary_get_data
+ _xpc_dictionary_set_data
- -[WFHealthManager diagnosticsQueue]
- -[WFHealthManager setDiagnosticsQueue:]
- -[WFPortalContext initWithCaptiveProfile:]
- -[WFPortalContext portalURLForDisplay]
- GCC_except_table34
- GCC_except_table42
- GCC_except_table44
- GCC_except_table57
- _OBJC_IVAR_$_WFHealthManager._diagnosticsQueue
- ___101-[WFNetworkListController networkListViewController:showSettingsForNetwork:context:scrollToCellType:]_block_invoke.327
- ___101-[WFNetworkListController networkListViewController:showSettingsForNetwork:context:scrollToCellType:]_block_invoke.329
- ___101-[WFNetworkListController networkListViewController:showSettingsForNetwork:context:scrollToCellType:]_block_invoke.380
- ___101-[WFNetworkListController networkListViewController:showSettingsForNetwork:context:scrollToCellType:]_block_invoke.381
- ___101-[WFNetworkListController networkListViewController:showSettingsForNetwork:context:scrollToCellType:]_block_invoke.382
- ___101-[WFNetworkListController networkListViewController:showSettingsForNetwork:context:scrollToCellType:]_block_invoke.383
- ___101-[WFNetworkListController networkListViewController:showSettingsForNetwork:context:scrollToCellType:]_block_invoke.384
- ___101-[WFNetworkListController networkListViewController:showSettingsForNetwork:context:scrollToCellType:]_block_invoke.386
- ___23-[WFClient setPowered:]_block_invoke.119
- ___25-[WFClient asyncPowered:]_block_invoke.121
- ___26-[WFClient asyncMISState:]_block_invoke.158
- ___35-[WFClient asyncMISDiscoveryState:]_block_invoke.159
- ___35-[WFClient asyncUserAutoJoinState:]_block_invoke.156
- ___35-[WFWiFiStateMonitor _updateState:]_block_invoke.39
- ___35-[WFWiFiStateMonitor _updateState:]_block_invoke.42
- ___37-[WFClient setPoweredToggle:handler:]_block_invoke.120
- ___37-[WFWiFiStateMonitor startMonitoring]_block_invoke.13
- ___41-[WFWiFiStateMonitor _updateWiFiUIState:]_block_invoke.45
- ___41-[WFWiFiStateMonitor _updateWiFiUIState:]_block_invoke.46
- ___43-[WFHealthManager runNoInternetDiagnostics]_block_invoke.19
- ___43-[WFHealthManager runNoInternetDiagnostics]_block_invoke.20
- ___44-[WFNetworkListController _updatePowerState]_block_invoke.111
- ___44-[WFNetworkListController _updatePowerState]_block_invoke.112
- ___53-[WFNetworkListController _associateToHotspotDevice:]_block_invoke.163
- ___53-[WFNetworkListController _associateToHotspotDevice:]_block_invoke.164
- ___53-[WFNetworkListController _associateToHotspotDevice:]_block_invoke.168
- ___53-[WFNetworkListController _associateToHotspotDevice:]_block_invoke.169
- ___56-[WFClient _startMonitoringCoreWiFiEventsWithInterface:]_block_invoke.110
- ___56-[WFClient _startMonitoringCoreWiFiEventsWithInterface:]_block_invoke.72
- ___56-[WFClient _startMonitoringCoreWiFiEventsWithInterface:]_block_invoke.85
- ___56-[WFClient _startMonitoringCoreWiFiEventsWithInterface:]_block_invoke.86
- ___56-[WFClient _startMonitoringCoreWiFiEventsWithInterface:]_block_invoke_2.81
- ___56-[WFClient _startMonitoringCoreWiFiEventsWithInterface:]_block_invoke_2.88
- ___56-[WFNetworkListController _updateCurrentNetworkIPState:]_block_invoke.258
- ___57-[WFNetworkListController _canStartAssociationToNetwork:]_block_invoke.244
- ___57-[WFNetworkListController _canStartAssociationToNetwork:]_block_invoke.245
- ___57-[WFNetworkListController _canStartAssociationToNetwork:]_block_invoke.246
- ___58-[WFNetworkListController _applicationDidEnterBackground:]_block_invoke.97
- ___59-[WFNetworkListController _associateToUserSuppliedNetwork:]_block_invoke.215
- ___59-[WFNetworkListController _associateToUserSuppliedNetwork:]_block_invoke.217
- ___59-[WFNetworkListController _updateViewControllerScanResults]_block_invoke.127
- ___59-[WFNetworkListController _updateViewControllerScanResults]_block_invoke.138
- ___59-[WFNetworkListController _updateViewControllerScanResults]_block_invoke.140
- ___60-[WFNetworkListController _updatePrivacyProxyFeatureEnabled]_block_invoke.543
- ___60-[WFNetworkListController _updatePrivacyProxyFeatureEnabled]_block_invoke.546
- ___60-[WFNetworkListController _updatePrivacyProxyFeatureEnabled]_block_invoke_2.544
- ___62-[WFNetworkListController _scanNetworkForAssociation:profile:]_block_invoke.254
- ___63-[WFNetworkListController _associationDidFinish:error:network:]_block_invoke.251
- ___63-[WFNetworkListController _refreshKnownHiddenNetworkNamesCache]_block_invoke.553
- ___64-[WFNetworkListController _promptCredentialsForNetwork:profile:]_block_invoke.233
- ___64-[WFNetworkListController _promptCredentialsForNetwork:profile:]_block_invoke.234
- ___69-[WFNetworkListController _canStartAssociationToUserSuppliedNetwork:]_block_invoke.248
- ___71-[WFNetworkListController networkListViewControllerDidTapOtherNetwork:]_block_invoke.297
- ___71-[WFNetworkListController networkListViewControllerDidTapOtherNetwork:]_block_invoke.298
- ___74-[WFNetworkListController _associateToUserSuppliedNetworkHelper:networks:]_block_invoke.220
- ___99-[WFNetworkListController _handleAssociationError:network:profile:securityMode:associationContext:]_block_invoke.222
- ___99-[WFNetworkListController _handleAssociationError:network:profile:securityMode:associationContext:]_block_invoke.224
- ___99-[WFNetworkListController _handleAssociationError:network:profile:securityMode:associationContext:]_block_invoke_2.223
- ___99-[WFNetworkListController _handleAssociationError:network:profile:securityMode:associationContext:]_block_invoke_2.226
- ___block_descriptor_48_e8_32s40w_e60_v32?0"NSError"8"<WFDiagnosticsResultItem>"16"NSString"24lw40l8s32l8
- ___block_descriptor_64_e8_32s40bs48r56r_e45_v24?0"CWFScanResult"8"CWFNetworkProfile"16ls32l8r48l8s40l8r56l8
- ___block_descriptor_tmp.103
- ___block_descriptor_tmp.104
- ___block_descriptor_tmp.108
- ___block_descriptor_tmp.113
- ___block_descriptor_tmp.117
- ___block_descriptor_tmp.126
- ___block_descriptor_tmp.129
- ___block_descriptor_tmp.130
- ___block_descriptor_tmp.136
- ___block_descriptor_tmp.140
- ___block_descriptor_tmp.141
- ___block_descriptor_tmp.151
- ___block_descriptor_tmp.152
- ___block_descriptor_tmp.154
- ___block_descriptor_tmp.155
- ___block_descriptor_tmp.157
- ___block_descriptor_tmp.158
- ___block_descriptor_tmp.159
- ___block_descriptor_tmp.162
- ___block_descriptor_tmp.165
- ___block_descriptor_tmp.169
- ___block_descriptor_tmp.197
- ___block_descriptor_tmp.222
- ___block_descriptor_tmp.223
- ___block_descriptor_tmp.52
- ___block_descriptor_tmp.57
- ___block_descriptor_tmp.58
- ___block_descriptor_tmp.62
- ___block_descriptor_tmp.67
- ___block_descriptor_tmp.80
- ___block_descriptor_tmp.81
- ___block_descriptor_tmp.84
- ___block_descriptor_tmp.87
- ___block_descriptor_tmp.94
- ___block_descriptor_tmp.98
- ___block_descriptor_tmp.99
- ___block_literal_global.115
- ___block_literal_global.176
- ___block_literal_global.180
- ___block_literal_global.229
- ___block_literal_global.318
- ___block_literal_global.449
- ___block_literal_global.535
- ___block_literal_global.541
- ___block_literal_global.74
- _insert_interface_address_params
- _objc_msgSend$initWithCaptiveProfile:
- _objc_msgSend$popViewControllerAnimated:
- _objc_msgSend$portalURLForDisplay
- _objc_msgSend$pushViewController:animated:
CStrings:
+ "%@: (sender: %@) wifi ui flags state changed"
+ "%@: current network changed from %@ to %@ (reason %lu)"
+ "%@: wifiuistateflags %lu"
+ "%s SPI doesn't support bridged mode"
+ "%s: CacheLocatorSettings class not found in content caches bundle."
+ "%s: Failed to load content caches bundle from internal path. Error: %@"
+ "%s: Failed to load content caches bundle from system path. Error: %@"
+ "%s: Loaded content caches bundle from internal path"
+ "%s: _CFRuntimeCreateInstance"
+ "%s: _NETRBClientCreate"
+ "%s: _NETRBClientNewInterface"
+ "%s: __NETRBNetworkCreateGlobalClient"
+ "%s: adding virtual interface to network %p"
+ "%s: airplaneModeEnabled set to %i"
+ "%s: anqp venueURLs='%@'"
+ "%s: failed"
+ "%s: found %d content caches"
+ "%s: interface creation failed"
+ "%s: invalid address family %u"
+ "%s: invalid network global client"
+ "%s: invalid operation mode"
+ "%s: invalid serialized network"
+ "%s: network handle mismatch"
+ "%s: network handle not returned"
+ "%s: no associated network"
+ "%s: no response from daemon"
+ "%s: queuing no internet test after %lusecs"
+ "%s: refresh current network cell when exiting edit PNL"
+ "%s: scanForCaches method not found on CacheLocatorSettings"
+ "%s: unable to create framework queue"
+ "%s: urlComponents nil for URL %@"
+ "%s: venueURL='%@' userPortalURL='%@'"
+ "%s: wifiUIStateFlags changed from %lu to %lu"
+ "-[WFClient _updateWiFiUIFlagsState]"
+ "-[WFContentCachesContext init]"
+ "-[WFContentCachesContext init]_block_invoke_2"
+ "-[WFHealthManager runNoInternetDiagnosticsAfter:]"
+ "-[WFPortalContext initWithCaptiveProfile:anqpVenueURLs:]"
+ "-[WFPortalContext portalHostnameForDisplay]"
+ "/AppleInternal/Library/PreferenceBundles/Content Caches.bundle"
+ "/System/Library/PreferenceBundles/Content Caches.bundle"
+ "@\"<ContentCachesContextDelegate>\""
+ "@\"CacheLocatorSettings\""
+ "@\"UIMenu\"40@0:8@\"UITextField\"16@\"NSArray\"24@\"NSArray\"32"
+ "@\"UIMenu\"40@0:8@\"UITextView\"16@\"NSArray\"24@\"NSArray\"32"
+ "@\"WFContentCachesContext\""
+ "@\"WFContentCachesContext\"16@0:8"
+ "B24@0:8^{__CFString=}16"
+ "B40@0:8@\"UITextField\"16@\"NSArray\"24@\"NSString\"32"
+ "B40@0:8@\"UITextView\"16@\"NSArray\"24@\"NSString\"32"
+ "B40@0:8@16@24@32"
+ "CWFEventTypeLinkQuality - event='%@'"
+ "CWFEventTypeWiFiUIStateFlagsChanged - event %@"
+ "CacheLocatorSettings"
+ "ContentCaching"
+ "Hotspot has been enabled and directed scan has been completed. Associate to hotspot."
+ "Joining a hotspot while another association is in progress"
+ "NETRB.c"
+ "NETRB_CLIENT"
+ "NETRB_INTERFACE"
+ "NETRB_NETWORK"
+ "NearbyAutoJoinAssist"
+ "NearbyCaptiveAssist"
+ "NearbyCaptiveAssistRecommendationUI"
+ "No internet warning generated becuase Velocity tests failed"
+ "Solarium"
+ "SwiftUI"
+ "T@\"<ContentCachesContextDelegate>\",W,N,V_delegate"
+ "T@\"CacheLocatorSettings\",&,N,V_cacheLocatorSettingsInstance"
+ "T@\"NSOperationQueue\",&,N,V_noInternetTestQueue"
+ "T@\"WFContentCachesContext\",&,N,V_contentCachesContext"
+ "T@\"WFContentCachesContext\",?,&,N"
+ "TQ,V_wifiUIStateFlags"
+ "Ti,N,V_numOfContentCaches"
+ "Tq,N,V_poorCoverageOverride"
+ "UnifiedPrivateMAC_ios"
+ "WFClientWiFiUIFlagsStateChangedNotification"
+ "WFContentCachesContext"
+ "Wifi-NAN"
+ "_NETRBCreateNetwork"
+ "_NETRBCreateNetworkConfiguration"
+ "_NETRBCreateNetwork_block_invoke"
+ "_NETRBCreateNetwork_block_invoke_2"
+ "_NETRBDeserializeNetwork"
+ "_NETRBDeserializeNetworkConfig"
+ "_NETRBNetworkAddPortForwardingRule"
+ "_NETRBNetworkClientRefCnt > 0"
+ "_NETRBNetworkStartVirtualMachineInterface"
+ "_NETRBNetworkStartVirtualMachineInterface_block_invoke"
+ "_NETRBNetworkStartVirtualMachineInterface_block_invoke_2"
+ "__NETRBInterfaceRelease"
+ "__NETRBNetworkCreateGlobalClient_block_invoke"
+ "__NETRBNetworkRelease"
+ "__NETRBNetworkReleaseGlobalClient_block_invoke"
+ "__hasPrivateMACUserJoinFailureUIState:"
+ "__isIPConfigurationPrimaryForProperty:"
+ "_cacheLocatorSettingsInstance"
+ "_contentCachesContext"
+ "_noInternetTestQueue"
+ "_numOfContentCaches"
+ "_poorCoverageOverride"
+ "_queueCount"
+ "_updateWiFiUIFlagsState"
+ "_wifiUIFlagsStateChanged:"
+ "_wifiUIStateFlags"
+ "addExecutionBlock:"
+ "building xpc request"
+ "cacheLocatorSettingsInstance"
+ "contentCachesCellAtIndexPath:"
+ "contentCachesContext"
+ "contentCachesContext:didUpdateNumOfContentCaches:"
+ "credentials context (%@) in progress for other network %@, reusing for association"
+ "current network='%@' kicking off internet test upon receiving valid IP configuration"
+ "dataSession:confirmedForPeerDataAddress:serviceSpecificInfo:pairingKeyStoreID:"
+ "dataSession:confirmedForPeerDataAddress:serviceSpecificInfo:pairingKeyStoreID:deviceID:"
+ "deploymentIssues"
+ "fullPortalURLString"
+ "hasPrimaryIPConfiguration"
+ "initWithCaptiveProfile:anqpVenueURLs:"
+ "initializing WFClient with callback run loop"
+ "interfaceId"
+ "isCancelled"
+ "isCarPlayOnly"
+ "isDeviceSupervised"
+ "isIPv4Primary"
+ "isIPv6Primary"
+ "isNetworkManagedByMDM:"
+ "kWFLocSettingsContentCachesButton"
+ "loadAndReturnError:"
+ "multiple associations in progress. assocationContextQueue count: %d"
+ "nearbyCaptiveAssistRecommendationUIFeatureEnabled"
+ "network is %s, has valid IP: %d, network has DHCP Lease: %d"
+ "networkAuthorizationToken"
+ "networkForceRemove"
+ "networkObject"
+ "networkObjects"
+ "networkProfile"
+ "networkSerialization"
+ "networkSerializationDHCPReservation"
+ "networkSerializationPortForwarding"
+ "network_dhcp_reservation_ip_addr"
+ "network_dhcp_reservation_mac_addr"
+ "network_port_forwarding_address_family"
+ "network_port_forwarding_external_port"
+ "network_port_forwarding_internal_address"
+ "network_port_forwarding_internal_port"
+ "network_port_forwarding_protocol"
+ "no internet test cancelled"
+ "noInternetTestQueue"
+ "not primary"
+ "numOfContentCaches"
+ "operationCount"
+ "poorCoverageOverride"
+ "portalHostnameForDisplay"
+ "primary"
+ "privateMACAddressForNetworkProfile:"
+ "privateMACAddressModeConfigurationProfileSetting"
+ "privateMACAddressModeForNetworkProfile:"
+ "publisher:dataConfirmedForHandle:localInterfaceIndex:serviceSpecificInfo:pairingKeyStoreID:"
+ "publisher:dataConfirmedForHandle:localInterfaceIndex:serviceSpecificInfo:pairingKeyStoreID:deviceID:"
+ "relay audit token"
+ "relay_audit_token"
+ "resetting current network states"
+ "scanForCachesOn:withHandler:"
+ "set currentNetworkScaledRSSI"
+ "setCacheLocatorSettingsInstance:"
+ "setContentCachesContext:"
+ "setNoInternetTestQueue:"
+ "setNumOfContentCaches:"
+ "setPoorCoverageOverride:"
+ "setPrivateMACAddressMode:networkProfile:error:"
+ "setPrivateMACAddressUserJoinFailureUIState:networkProfile:"
+ "setWifiUIStateFlags:"
+ "tap-portal-url"
+ "textField:editMenuForCharactersInRanges:suggestedActions:"
+ "textField:shouldChangeCharactersInRanges:replacementString:"
+ "textView:editMenuForTextInRanges:suggestedActions:"
+ "textView:shouldChangeTextInRanges:replacementText:"
+ "underlyingErrors"
+ "v24@0:8@\"WFContentCachesContext\"16"
+ "v48@0:8@\"WiFiAwareDataSession\"16@\"WiFiMACAddress\"24@\"WiFiAwarePublishDatapathServiceSpecificInfo\"32@\"NSUUID\"40"
+ "v48@0:8@16@24@32@40"
+ "v52@0:8@\"WiFiAwarePublisher\"16@\"WiFiAwarePublisherDataSessionHandle\"24I32@\"WiFiAwarePublishDatapathServiceSpecificInfo\"36@\"NSUUID\"44"
+ "v52@0:8@16@24I32@36@44"
+ "v56@0:8@\"WiFiAwareDataSession\"16@\"WiFiMACAddress\"24@\"WiFiAwarePublishDatapathServiceSpecificInfo\"32@\"NSUUID\"40Q48"
+ "v56@0:8@16@24@32@40Q48"
+ "v60@0:8@\"WiFiAwarePublisher\"16@\"WiFiAwarePublisherDataSessionHandle\"24I32@\"WiFiAwarePublishDatapathServiceSpecificInfo\"36@\"NSUUID\"44Q52"
+ "v60@0:8@16@24I32@36@44Q52"
+ "venueURLList"
+ "wf_popViewControllerAnimated:"
+ "wf_pushViewController:animated:"
+ "{ACTION*} no action performed, returning current state"
+ "{ACTION*} power modification is disabled"
- "%@: Current network changed, %@ (reason %lu)"
- "-[WFPortalContext initWithCaptiveProfile:]"
- "NETRB"
- "No internet warning generated becuase Velocity tests failed!"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_diagnosticsQueue"
- "_diagnosticsQueue"
- "diagnosticsQueue"
- "initWithCaptiveProfile:"
- "network has valid IP: %d, network has DHCP Lease: %d"
- "popViewControllerAnimated:"
- "portalURLForDisplay"
- "pushViewController:animated:"
- "setDiagnosticsQueue:"

```
