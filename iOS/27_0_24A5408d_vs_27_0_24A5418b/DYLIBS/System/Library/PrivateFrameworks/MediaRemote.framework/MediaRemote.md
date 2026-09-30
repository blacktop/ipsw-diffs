## MediaRemote

> `/System/Library/PrivateFrameworks/MediaRemote.framework/MediaRemote`

```diff

-4026.110.83.1.0
-  __TEXT.__text: 0x317068
-  __TEXT.__objc_methlist: 0x2c788
+4026.110.4.0.0
+  __TEXT.__text: 0x317a24
+  __TEXT.__objc_methlist: 0x2c818
   __TEXT.__const: 0x6b0
-  __TEXT.__cstring: 0x2de92
-  __TEXT.__oslogstring: 0xea48
+  __TEXT.__cstring: 0x2df00
+  __TEXT.__oslogstring: 0xeaed
   __TEXT.__gcc_except_tab: 0x6368
   __TEXT.__dlopen_cstrs: 0x777
   __TEXT.__ustring: 0x7b8
-  __TEXT.__unwind_info: 0xbe10
+  __TEXT.__unwind_info: 0xbe18
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xbb08
+  __DATA_CONST.__const: 0xbb58
   __DATA_CONST.__objc_classlist: 0x1210
   __DATA_CONST.__objc_catlist: 0x78
   __DATA_CONST.__objc_protolist: 0x260
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xf930
+  __DATA_CONST.__objc_selrefs: 0xf978
   __DATA_CONST.__objc_protorefs: 0x88
   __DATA_CONST.__objc_superrefs: 0x1038
   __DATA_CONST.__objc_arraydata: 0x260
   __DATA_CONST.__got: 0x14d0
   __AUTH_CONST.__const: 0x3440
-  __AUTH_CONST.__cfstring: 0x24a20
-  __AUTH_CONST.__objc_const: 0x47e80
+  __AUTH_CONST.__cfstring: 0x24a80
+  __AUTH_CONST.__objc_const: 0x47f48
   __AUTH_CONST.__objc_arrayobj: 0x180
   __AUTH_CONST.__objc_intobj: 0x4f8
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__auth_got: 0xbc0
   __AUTH.__objc_data: 0x8700
-  __DATA.__objc_ivar: 0x33e4
+  __DATA.__objc_ivar: 0x33ec
   __DATA.__data: 0x1ca8
-  __DATA.__bss: 0x998
+  __DATA.__bss: 0x9b8
   __DATA.__common: 0x8
   __DATA_DIRTY.__objc_data: 0x2da0
   __DATA_DIRTY.__data: 0x88

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 21013
-  Symbols:   35571
-  CStrings:  6771
+  Functions: 21030
+  Symbols:   35599
+  CStrings:  6776
 
Symbols:
+ -[MRAVLightweightReconnaissanceSession searchOutputDevices:protocolUID:appVended:timeout:details:queue:completion:]
+ -[MRIRRoute appVendedContainerBundleID]
+ -[MRIRRoute appVended]
+ -[MRIRRoute setAppVendedContainerBundleID:]
+ -[MRNowPlayingAudioFormatController ignoreList]
+ -[MRNowPlayingAudioFormatController isBundleIDAllowed:]
+ -[MRNowPlayingAudioFormatController setIgnoreList:]
+ -[MRUserSettings appVendedRouteRecommendationsEnabled]
+ -[MRUserSettings disableRemoteMediaExtensionNetworkPolicies]
+ GCC_except_table73
+ _OBJC_IVAR_$_MRIRRoute._appVendedContainerBundleID
+ _OBJC_IVAR_$_MRNowPlayingAudioFormatController._ignoreList
+ ___115-[MRAVLightweightReconnaissanceSession searchOutputDevices:protocolUID:appVended:timeout:details:queue:completion:]_block_invoke
+ ___115-[MRAVLightweightReconnaissanceSession searchOutputDevices:protocolUID:appVended:timeout:details:queue:completion:]_block_invoke_2
+ ___115-[MRAVLightweightReconnaissanceSession searchOutputDevices:protocolUID:appVended:timeout:details:queue:completion:]_block_invoke_3
+ ___115-[MRAVLightweightReconnaissanceSession searchOutputDevices:protocolUID:appVended:timeout:details:queue:completion:]_block_invoke_4
+ ___115-[MRAVLightweightReconnaissanceSession searchOutputDevices:protocolUID:appVended:timeout:details:queue:completion:]_block_invoke_5
+ ___51-[MRNowPlayingAudioFormatController setIgnoreList:]_block_invoke
+ ___54-[MRUserSettings appVendedRouteRecommendationsEnabled]_block_invoke
+ ___59-[MRNowPlayingAudioFormatController audioFormatApplication]_block_invoke
+ ___59-[MRNowPlayingAudioFormatController audioFormatContentInfo]_block_invoke
+ ___60-[MRUserSettings disableRemoteMediaExtensionNetworkPolicies]_block_invoke
+ ___block_descriptor_56_e8_32s40s48w_e5_v8?0lw48l8s32l8s40l8
+ ___block_descriptor_72_e8_32s40s48s56bs64bs_e58_v40?0"NSArray"8"NSArray"16"MRAVEndpoint"24"NSError"32ls32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_72_e8_32s40s48s56bs_e5_v8?0ls32l8s40l8s48l8s56l8
+ _appVendedRouteRecommendationsEnabled.__value
+ _appVendedRouteRecommendationsEnabled.onceToken
+ _disableRemoteMediaExtensionNetworkPolicies.onceToken
+ _disableRemoteMediaExtensionNetworkPolicies.result
+ _objc_msgSend$appVendedContainerBundleID
+ _objc_msgSend$ignoreList
+ _objc_msgSend$isBundleIDAllowed:
+ _objc_msgSend$searchOutputDevices:protocolUID:appVended:timeout:details:queue:completion:
+ _objc_msgSend$setAppVendedContainerBundleID:
- ___105-[MRAVLightweightReconnaissanceSession searchOutputDevices:protocolUID:timeout:details:queue:completion:]_block_invoke
- ___105-[MRAVLightweightReconnaissanceSession searchOutputDevices:protocolUID:timeout:details:queue:completion:]_block_invoke_2
- ___105-[MRAVLightweightReconnaissanceSession searchOutputDevices:protocolUID:timeout:details:queue:completion:]_block_invoke_3
- ___105-[MRAVLightweightReconnaissanceSession searchOutputDevices:protocolUID:timeout:details:queue:completion:]_block_invoke_4
- ___105-[MRAVLightweightReconnaissanceSession searchOutputDevices:protocolUID:timeout:details:queue:completion:]_block_invoke_5
- ___block_descriptor_96_e8_32s40s48s56s64s72s80bs_e58_v40?0"NSArray"8"NSArray"16"MRAVEndpoint"24"NSError"32ls32l8s40l8s48l8s80l8s56l8s64l8s72l8
CStrings:
+ "%{public}@ ignoring the following bundle ids: %{public}@"
+ "AppVendedRouteRecommendationsEnabled"
+ "Update: %{public}@<%{public}@> app-vended route: skipping audio discovery, searching RemoteControl directly"
+ "appVendedContainerBundleID"
+ "disableRemoteMediaExtensionNetworkPolicies"
```
