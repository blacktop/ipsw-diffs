## MediaControls

> `/System/Library/PrivateFrameworks/MediaControls.framework/MediaControls`

```diff

-4026.100.79.0.0
-  __TEXT.__text: 0x21fbec
-  __TEXT.__objc_methlist: 0x15b94
-  __TEXT.__cstring: 0x6f44
-  __TEXT.__ustring: 0x22
-  __TEXT.__const: 0xb844
-  __TEXT.__gcc_except_tab: 0x1598
-  __TEXT.__oslogstring: 0x8799
+4026.110.83.1.0
+  __TEXT.__text: 0x222bdc
+  __TEXT.__objc_methlist: 0x15bd4
+  __TEXT.__cstring: 0x6f74
+  __TEXT.__ustring: 0x28
+  __TEXT.__const: 0xba64
+  __TEXT.__gcc_except_tab: 0x1548
+  __TEXT.__oslogstring: 0x86d9
   __TEXT.__dlopen_cstrs: 0x64
-  __TEXT.__constg_swiftt: 0x7740
-  __TEXT.__swift5_typeref: 0x3398
-  __TEXT.__swift5_reflstr: 0x4a03
-  __TEXT.__swift5_fieldmd: 0x4b08
-  __TEXT.__swift5_types: 0x604
-  __TEXT.__swift5_capture: 0x13d8
+  __TEXT.__constg_swiftt: 0x7778
+  __TEXT.__swift5_typeref: 0x3368
+  __TEXT.__swift5_reflstr: 0x4b33
+  __TEXT.__swift5_fieldmd: 0x4b8c
+  __TEXT.__swift5_types: 0x608
+  __TEXT.__swift5_capture: 0x13f8
   __TEXT.__swift5_protos: 0xb8
-  __TEXT.__swift5_proto: 0x5e8
+  __TEXT.__swift5_proto: 0x5ec
   __TEXT.__swift5_builtin: 0x334
-  __TEXT.__swift5_mpenum: 0x50
+  __TEXT.__swift5_mpenum: 0x5c
   __TEXT.__swift_as_entry: 0x3c
   __TEXT.__swift_as_ret: 0x34
   __TEXT.__swift_as_cont: 0x6c
   __TEXT.__swift5_assocty: 0x348
-  __TEXT.__unwind_info: 0x88c8
-  __TEXT.__eh_frame: 0x1900
+  __TEXT.__unwind_info: 0x88e8
+  __TEXT.__eh_frame: 0x18a8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x30a8
+  __DATA_CONST.__const: 0x3080
   __DATA_CONST.__objc_classlist: 0x9b8
   __DATA_CONST.__objc_catlist: 0xa8
   __DATA_CONST.__objc_protolist: 0x470
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xa6d8
+  __DATA_CONST.__objc_selrefs: 0xa6f0
   __DATA_CONST.__objc_protorefs: 0xa0
   __DATA_CONST.__objc_superrefs: 0x608
   __DATA_CONST.__objc_arraydata: 0x1e8
   __DATA_CONST.__got: 0x1898
-  __AUTH_CONST.__const: 0xa7f0
-  __AUTH_CONST.__cfstring: 0x51a0
-  __AUTH_CONST.__objc_const: 0x439e0
+  __AUTH_CONST.__const: 0xaa08
+  __AUTH_CONST.__cfstring: 0x51e0
+  __AUTH_CONST.__objc_const: 0x43a18
   __AUTH_CONST.__objc_intobj: 0x2b8
   __AUTH_CONST.__objc_arrayobj: 0x138
   __AUTH_CONST.__objc_doubleobj: 0xf0
   __AUTH_CONST.__objc_dictobj: 0x140
-  __AUTH_CONST.__auth_got: 0x2010
-  __AUTH.__objc_data: 0x3828
+  __AUTH_CONST.__auth_got: 0x2008
+  __AUTH.__objc_data: 0x3880
   __AUTH.__data: 0x1238
-  __DATA.__objc_ivar: 0x18d0
-  __DATA.__data: 0x4128
-  __DATA.__bss: 0x8898
-  __DATA.__common: 0x720
+  __DATA.__objc_ivar: 0x18cc
+  __DATA.__data: 0x4138
+  __DATA.__bss: 0x8928
+  __DATA.__common: 0x8b0
   __DATA_DIRTY.__objc_data: 0x7270
   __DATA_DIRTY.__data: 0x3378
   __DATA_DIRTY.__bss: 0x28a0

   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/CoreHaptics.framework/CoreHaptics
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
+  - /System/Library/Frameworks/CoreText.framework/CoreText
   - /System/Library/Frameworks/DeveloperToolsSupport.framework/DeveloperToolsSupport
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/HomeKit.framework/HomeKit

   - /System/Library/PrivateFrameworks/MediaRemote.framework/MediaRemote
   - /System/Library/PrivateFrameworks/MediaServices.framework/MediaServices
   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
+  - /System/Library/PrivateFrameworks/ProductKit.framework/ProductKit
   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
   - /System/Library/PrivateFrameworks/Sharing.framework/Sharing
   - /System/Library/PrivateFrameworks/SharingUI.framework/SharingUI

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 14347
-  Symbols:   17593
-  CStrings:  1625
+  Functions: 14388
+  Symbols:   17609
+  CStrings:  1624
 
Symbols:
+ -[MRUMarqueeLabel updateDimmed]
+ -[MRUMarqueeLabel updateMarquee]
+ -[MRUNowPlayingTimeControlsView sliderTouchChanged:]
+ -[MRURouteRecommendationPlatterViewController updateArtwork:]
+ -[MRURouteRecommendationPlatterViewController updateEndpointRoute:]
+ -[MRURouteRecommendationPlatterViewController updateNowPlayingInfo:]
+ -[MRURouteRecommendationPlatterViewController updateShowTVRemote:]
+ -[MRUVolumeViewController audioModuleController:listeningModeController:didChangePrimaryListeningModeConfigs:listeningMode:autoANCCapability:autoANCStrength:]
+ -[NSString(MRUTextSize) mru_containsExcessiveHeightCharacters]
+ GCC_except_table28
+ _CTFontCopySystemUIFontExcessiveLineHeightCharacterSet
+ _CTFontGetLanguageAwareOutsets
+ _MSVGetDeviceProductType
+ __OBJC_$_PROP_LIST_NSString_$_MRUTextSize
+ ___62-[NSString(MRUTextSize) mru_containsExcessiveHeightCharacters]_block_invoke
+ ___64-[MRUVolumeViewController updateEnvironmentSliderValueAnimated:]_block_invoke
+ ___64-[MRUVolumeViewController updateEnvironmentSliderValueAnimated:]_block_invoke_2
+ ___66-[MRUVolumeViewController updatePrimarySliderVolumeValueAnimated:]_block_invoke
+ ___66-[MRUVolumeViewController updatePrimarySliderVolumeValueAnimated:]_block_invoke_2
+ ___67-[MRURouteRecommendationPlatterViewController updateEndpointRoute:]_block_invoke
+ ___68-[MRUVolumeViewController updateSecondarySliderVolumeValueAnimated:]_block_invoke
+ ___68-[MRUVolumeViewController updateSecondarySliderVolumeValueAnimated:]_block_invoke_2
+ ___block_descriptor_64_e8_32s40s48s56bs_e5_v8?0ls32l8s56l8s40l8s48l8
+ ___swift_memcpy177_8
+ _get_enum_tag_for_layout_string 13MediaControls17MultiOptionButtonC0D0V5AssetO
+ _mru_containsExcessiveHeightCharacters.onceToken
+ _mru_containsExcessiveHeightCharacters.sExcessiveHeightCharacters
+ _objc_msgSend$imageForModelIdentifier:color:timeout:completion:
+ _objc_msgSend$isMarqueeEnabled
+ _objc_msgSend$mru_containsExcessiveHeightCharacters
+ _objc_msgSend$rangeOfCharacterFromSet:
+ _objc_msgSend$removeCharactersInString:
+ _objc_msgSend$updateArtwork:
+ _objc_msgSend$updateEndpointRoute:
+ _objc_msgSend$updateNowPlayingInfo:
+ _objc_msgSend$updateShowTVRemote:
+ _symbolic _____ 13MediaControls17MultiOptionButtonC0D0V5AssetO
+ _symbolic _____Sg 10ProductKit14iosmacHardwareV5ModelO
+ _symbolic _____Sg 13MediaControls17MultiOptionButtonC0D0V5AssetO
+ _symbolic _____Sg_ABt 13MediaControls17MultiOptionButtonC0D0V5AssetO
+ _type_layout_string 13MediaControls17MultiOptionButtonC0D0V5AssetO
- -[MRUAssetManager productKitImageForModelIdentifier:color:allowFallback:timeout:completion:]
- -[MRUAssetManager shouldUseProductKitFor:]
- -[MRURouteRecommendationPlatterViewController updateActionType]
- -[MRUVolumeViewController audioModuleController:listeningModeController:didChangePrimaryListeningMode:]
- GCC_except_table29
- _OBJC_IVAR_$_MRUMetadataController._dataSourceLock
- ___102-[MRURouteRecommendationPlatterViewController nowPlayingController:endpointController:didChangeRoute:]_block_invoke
- ___52-[MRUNowPlayingController imageForRoute:completion:]_block_invoke_4
- ___92-[MRUAssetManager productKitImageForModelIdentifier:color:allowFallback:timeout:completion:]_block_invoke
- ___block_descriptor_48_e8_32s40bs_e29_v24?0"UIImage"8"NSError"16ls32l8s40l8
- ___block_descriptor_48_e8_32s40r_e8_v12?0B8lr40l8s32l8
- _dispatch_semaphore_create
- _dispatch_semaphore_signal
- _dispatch_semaphore_wait
- _objc_msgSend$assetHardwareModel:color:allowFallback:timeout:completion:
- _objc_msgSend$availableFor:
- _objc_msgSend$imageNamed:inBundle:compatibleWithTraitCollection:
- _objc_msgSend$productKitImageForModelIdentifier:color:allowFallback:timeout:completion:
- _objc_msgSend$shouldUseProductKitFor:
- _objc_msgSend$updateActionType
- _symbolic SS8fileName_So8NSBundleC6bundlet
- _symbolic Si4code_t
- _symbolic _____ 13MediaControls17ProductKitWrapperC5asset3for5color13allowFallback7timeout10completionySS_SSSbSdySo7UIImageCSg_s5Error_pSgtctFZ15CompletionValueL_O
- _symbolic ______p5error_t s5ErrorP
- _symbolic _____y_____G s11_SetStorageC 13MediaControls17MultiOptionButtonC0F4ViewC
CStrings:
+ "AudioAccessory"
+ "SpatialMultichannelHeadTracked"
+ "SpatialMultichannelOff"
+ "SpatialMultichannelOn"
+ "SpatialStereoHeadTracked"
+ "SpatialStereoOff"
+ "SpatialStereoOn"
+ "[MRPKW] No ProductKit image for %@"
+ "çÇ"
- "[AssetManager] PK request<%@> for model: %@, color: %@, allow fallback? %{BOOL}u, timeout: %f"
- "[AssetManager] PK response<%@> Asset found: %@"
- "[AssetManager] PK response<%@> Failed to obtain asset: %@"
- "[MRPKW] failed to get image; fileName: %@, bundle: %@"
- "[MRPKW] got image: %@"
- "person.and.sparkles.fill"
- "person.closed.fill"
- "person.open.fill"
- "person.spatialaudio.fill"
- "person.spatialaudio.stereo.fill"
```
