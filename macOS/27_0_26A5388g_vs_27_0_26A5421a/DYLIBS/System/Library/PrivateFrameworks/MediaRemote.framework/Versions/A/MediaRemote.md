## MediaRemote

> `/System/Library/PrivateFrameworks/MediaRemote.framework/Versions/A/MediaRemote`

```diff

-4026.100.79.0.0
-  __TEXT.__text: 0x31f104
-  __TEXT.__objc_methlist: 0x2b7fc
-  __TEXT.__const: 0x5c8
-  __TEXT.__cstring: 0x2c4da
-  __TEXT.__oslogstring: 0xd2bc
+4026.140.2.0.0
+  __TEXT.__text: 0x320194
+  __TEXT.__objc_methlist: 0x2b8bc
+  __TEXT.__const: 0x5d8
+  __TEXT.__cstring: 0x2c5ce
+  __TEXT.__oslogstring: 0xd361
   __TEXT.__gcc_except_tab: 0x5898
   __TEXT.__dlopen_cstrs: 0x40b
   __TEXT.__ustring: 0x7b8
-  __TEXT.__unwind_info: 0xb1a0
+  __TEXT.__unwind_info: 0xb1c8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x4b70
+  __DATA_CONST.__const: 0x4b80
   __DATA_CONST.__objc_classlist: 0x11c0
   __DATA_CONST.__objc_catlist: 0x68
   __DATA_CONST.__objc_protolist: 0x228
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xf0c0
+  __DATA_CONST.__objc_selrefs: 0xf130
   __DATA_CONST.__objc_protorefs: 0x80
   __DATA_CONST.__objc_superrefs: 0xff0
   __DATA_CONST.__objc_arraydata: 0x260
   __DATA_CONST.__got: 0x1420
-  __AUTH_CONST.__const: 0xa410
-  __AUTH_CONST.__cfstring: 0x23d80
-  __AUTH_CONST.__objc_const: 0x46578
+  __AUTH_CONST.__const: 0xa420
+  __AUTH_CONST.__cfstring: 0x23e40
+  __AUTH_CONST.__objc_const: 0x46660
   __AUTH_CONST.__objc_arrayobj: 0x180
   __AUTH_CONST.__objc_intobj: 0x4c8
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__auth_got: 0xa90
   __AUTH.__objc_data: 0x8430
-  __DATA.__objc_ivar: 0x32e8
+  __DATA.__objc_ivar: 0x32f0
   __DATA.__data: 0x1a08
-  __DATA.__bss: 0x888
+  __DATA.__bss: 0x8a8
   __DATA.__common: 0x8
   __DATA_DIRTY.__objc_data: 0x2d50
   __DATA_DIRTY.__data: 0x88

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 20578
-  Symbols:   35122
-  CStrings:  6503
+  Functions: 20601
+  Symbols:   35160
+  CStrings:  6512
 
Symbols:
+ -[MRAVLightweightReconnaissanceSession searchOutputDevices:protocolUID:appVended:timeout:details:queue:completion:]
+ -[MRAudioIntentDetails dictionaryRepresentation]
+ -[MRAudioIntentDetails initWithDictionaryRepresentation:]
+ -[MRIRRoute appVendedContainerBundleID]
+ -[MRIRRoute appVended]
+ -[MRIRRoute setAppVendedContainerBundleID:]
+ -[MRMediaRemoteService triggerClusterErrorDialogForRouteUID:status:completion:]
+ -[MRNowPlayingAudioFormatController ignoreList]
+ -[MRNowPlayingAudioFormatController isBundleIDAllowed:]
+ -[MRNowPlayingAudioFormatController setIgnoreList:]
+ -[MRUserSettings appVendedRouteRecommendationsEnabled]
+ -[MRUserSettings clearClusterConnectionThrottleOnNetworkChange]
+ -[MRUserSettings disableRemoteMediaExtensionNetworkPolicies]
+ GCC_except_table114
+ GCC_except_table127
+ GCC_except_table137
+ GCC_except_table160
+ GCC_except_table364
+ OBJC_IVAR_$_MRIRRoute._appVendedContainerBundleID
+ OBJC_IVAR_$_MRNowPlayingAudioFormatController._ignoreList
+ _MRCreateUUIDv5
+ _MRNowPlayingCreateDerivedIdentifier
+ _MRNowPlayingGetArtworkSize
+ __115-[MRAVLightweightReconnaissanceSession searchOutputDevices:protocolUID:appVended:timeout:details:queue:completion:]_block_invoke
+ __115-[MRAVLightweightReconnaissanceSession searchOutputDevices:protocolUID:appVended:timeout:details:queue:completion:]_block_invoke_2
+ ___115-[MRAVLightweightReconnaissanceSession searchOutputDevices:protocolUID:appVended:timeout:details:queue:completion:]_block_invoke
+ ___115-[MRAVLightweightReconnaissanceSession searchOutputDevices:protocolUID:appVended:timeout:details:queue:completion:]_block_invoke_2
+ ___115-[MRAVLightweightReconnaissanceSession searchOutputDevices:protocolUID:appVended:timeout:details:queue:completion:]_block_invoke_3
+ ___115-[MRAVLightweightReconnaissanceSession searchOutputDevices:protocolUID:appVended:timeout:details:queue:completion:]_block_invoke_4
+ ___51-[MRNowPlayingAudioFormatController setIgnoreList:]_block_invoke
+ ___54-[MRUserSettings appVendedRouteRecommendationsEnabled]_block_invoke
+ ___59-[MRNowPlayingAudioFormatController audioFormatApplication]_block_invoke
+ ___59-[MRNowPlayingAudioFormatController audioFormatContentInfo]_block_invoke
+ ___60-[MRUserSettings disableRemoteMediaExtensionNetworkPolicies]_block_invoke
+ ___79-[MRMediaRemoteService triggerClusterErrorDialogForRouteUID:status:completion:]_block_invoke
+ ___block_descriptor_56_e8_32s40s48w_e5_v8?0l
+ ___block_descriptor_72_e8_32s40s48s56bs64bs_e58_v40?0"NSArray"8"NSArray"16"MRAVEndpoint"24"NSError"32l
+ _kMRNowPlayingRootNamespace
+ _objc_msgSend$appVendedContainerBundleID
+ _objc_msgSend$getUUIDBytes:
+ _objc_msgSend$ignoreList
+ _objc_msgSend$initWithOutputDeviceUIDs:startDate:
+ _objc_msgSend$initWithUUIDBytes:
+ _objc_msgSend$isBundleIDAllowed:
+ _objc_msgSend$searchOutputDevices:protocolUID:appVended:timeout:details:queue:completion:
+ _objc_msgSend$setAppVendedContainerBundleID:
+ appVendedRouteRecommendationsEnabled.__value
+ appVendedRouteRecommendationsEnabled.onceToken
+ currentDeviceRoutingSymbolName.lock
+ disableRemoteMediaExtensionNetworkPolicies.onceToken
+ disableRemoteMediaExtensionNetworkPolicies.result
- GCC_except_table113
- GCC_except_table130
- GCC_except_table362
- GCC_except_table77
- __105-[MRAVLightweightReconnaissanceSession searchOutputDevices:protocolUID:timeout:details:queue:completion:]_block_invoke
- __66+[MRDeviceIdentifierSymbolProvider currentDeviceRoutingSymbolName]_block_invoke
- ___105-[MRAVLightweightReconnaissanceSession searchOutputDevices:protocolUID:timeout:details:queue:completion:]_block_invoke
- ___105-[MRAVLightweightReconnaissanceSession searchOutputDevices:protocolUID:timeout:details:queue:completion:]_block_invoke_2
- ___105-[MRAVLightweightReconnaissanceSession searchOutputDevices:protocolUID:timeout:details:queue:completion:]_block_invoke_3
- ___105-[MRAVLightweightReconnaissanceSession searchOutputDevices:protocolUID:timeout:details:queue:completion:]_block_invoke_4
- ___66+[MRDeviceIdentifierSymbolProvider currentDeviceRoutingSymbolName]_block_invoke
- ___block_descriptor_96_e8_32s40s48s56s64s72s80bs_e58_v40?0"NSArray"8"NSArray"16"MRAVEndpoint"24"NSError"32l
- currentDeviceRoutingSymbolName.onceToken
CStrings:
+ "%{public}@ ignoring the following bundle ids: %{public}@"
+ "AppVendedRouteRecommendationsEnabled"
+ "Infra6GSteerNoCandidate"
+ "MRXPC_ROUTE_STATUS_KEY"
+ "UnsupportedProtocolRequiredRevertToLocal"
+ "Update: %{public}@<%{public}@> app-vended route: skipping audio discovery, searching RemoteControl directly"
+ "appVendedContainerBundleID"
+ "clearClusterConnectionThrottleOnNetworkChange"
+ "disableRemoteMediaExtensionNetworkPolicies"
```
