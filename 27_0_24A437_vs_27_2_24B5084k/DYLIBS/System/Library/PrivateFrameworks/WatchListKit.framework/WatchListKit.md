## WatchListKit

> `/System/Library/PrivateFrameworks/WatchListKit.framework/WatchListKit`

```diff

-952.0.1.0.0
-  __TEXT.__text: 0x646ec
-  __TEXT.__objc_methlist: 0x7174
+952.10.6.0.0
+  __TEXT.__text: 0x65e5c
+  __TEXT.__objc_methlist: 0x71d4
   __TEXT.__const: 0x1a4
-  __TEXT.__cstring: 0x7dfa
-  __TEXT.__oslogstring: 0x6492
+  __TEXT.__cstring: 0x7f44
+  __TEXT.__oslogstring: 0x6506
   __TEXT.__gcc_except_tab: 0xf44
-  __TEXT.__unwind_info: 0x2568
+  __TEXT.__unwind_info: 0x25d0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x27a0
+  __DATA_CONST.__const: 0x29a8
   __DATA_CONST.__objc_classlist: 0x560
   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0x98
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3a20
+  __DATA_CONST.__objc_selrefs: 0x3aa0
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x4b0
   __DATA_CONST.__objc_arraydata: 0x628
   __DATA_CONST.__got: 0x908
   __AUTH_CONST.__const: 0xea0
-  __AUTH_CONST.__cfstring: 0xa6c0
-  __AUTH_CONST.__objc_const: 0x11ce8
+  __AUTH_CONST.__cfstring: 0xa720
+  __AUTH_CONST.__objc_const: 0x11d50
   __AUTH_CONST.__objc_intobj: 0x378
   __AUTH_CONST.__objc_dictobj: 0x190
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x1810
-  __DATA.__objc_ivar: 0xa4c
+  __DATA.__objc_ivar: 0xa54
   __DATA.__data: 0x7a0
   __DATA_DIRTY.__objc_data: 0x1db0
   __DATA_DIRTY.__data: 0x8

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2784
-  Symbols:   6889
-  CStrings:  1927
+  Functions: 2812
+  Symbols:   6931
+  CStrings:  1943
 
Symbols:
+ +[NSURL(WLKAdditions) _wlk_URLWithServerConfig:fullPath:endpoint:queryParameters:suppressParameterEncoding:ignoreUserLocation:]
+ +[NSURL(WLKAdditions) wlk_URLWithServerConfig:endpoint:baseURLString:queryParameters:suppressParameterEncoding:ignoreUserLocation:]
+ +[WLKConfigurationRequest _configURLStringWithCompletion:]
+ -[WLKSystemPreferencesStore alwaysShowProfileSelection]
+ -[WLKSystemPreferencesStore setAlwaysShowProfileSelection:]
+ -[WLKSystemPreferencesStore setSignLanguageEnabled:]
+ -[WLKSystemPreferencesStore signLanguageEnabled]
+ -[WLKURLRequestProperties URLRequestWithConfiguration:baseURLString:]
+ GCC_except_table44
+ _OBJC_IVAR_$_WLKSystemPreferencesStore._preferencesCache
+ _OBJC_IVAR_$_WLKSystemPreferencesStore._preferencesCacheLock
+ ___51-[WLKUTSNetworkRequestOperation prepareURLRequest:]_block_invoke_2
+ ___55+[WLKURLBagUtilities isFullTVAppEnabledWithCompletion:]_block_invoke_2
+ ___58+[WLKConfigurationRequest _configURLStringWithCompletion:]_block_invoke
+ ___58+[WLKConfigurationRequest _configURLStringWithCompletion:]_block_invoke_2
+ ___58+[WLKConfigurationRequest _configURLStringWithCompletion:]_block_invoke_3
+ ___58+[WLKConfigurationRequest _configURLStringWithCompletion:]_block_invoke_4
+ ___61+[WLKSettingsCloudUtilities _cloudSyncEnabledWithCompletion:]_block_invoke_2
+ ___61+[WLKSettingsCloudUtilities _cloudSyncEnabledWithCompletion:]_block_invoke_3
+ ___61+[WLKSettingsCloudUtilities _cloudSyncEnabledWithCompletion:]_block_invoke_4
+ ___WLKFetchBaseURLWithCompletion_block_invoke_2
+ ___WLKFetchNowPlayingEnabledReturningError_block_invoke_2
+ ___block_descriptor_40_e8_32bs_e27_v24?0"NSURL"8"NSError"16ls32l8
+ ___block_descriptor_40_e8_32bs_e30_v24?0"NSNumber"8"NSError"16ls32l8
+ ___block_descriptor_40_e8_32bs_e30_v24?0"NSString"8"NSError"16ls32l8
+ ___block_descriptor_40_e8_32bs_e38_v32?0"NSURL"8"NSURL"16"NSNumber"24ls32l8
+ ___block_descriptor_48_e8_32bs_e37_v32?0"NSURL"8"NSURL"16"NSError"24ls32l8
+ ___block_descriptor_48_e8_32s40bs_e18_v16?0"NSString"8ls40l8s32l8
+ ___block_descriptor_48_e8_32s40bs_e30_v24?0"NSNumber"8"NSError"16ls32l8s40l8
+ ___block_descriptor_56_e8_32s40s48bs_e30_v24?0"NSString"8"NSError"16ls48l8s32l8s40l8
+ ___block_descriptor_56_e8_32s40s48bs_e8_v16?0Q8ls32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48bs_e30_v24?0"NSNumber"8"NSError"16ls48l8s32l8s40l8
+ ___block_descriptor_64_e8_32s40s48s56bs_e22_v16?0"NSURLRequest"8ls32l8s40l8s56l8s48l8
+ ___block_descriptor_64_e8_32s40s48s56bs_e5_v8?0ls56l8s32l8s40l8s48l8
+ ___block_descriptor_72_e8_32s40s48bs_e30_v24?0"NSString"8"NSError"16ls48l8s32l8s40l8
+ _objc_msgSend$URLRequestWithConfiguration:baseURLString:
+ _objc_msgSend$_configURLStringWithCompletion:
+ _objc_msgSend$_wlk_URLWithServerConfig:fullPath:endpoint:queryParameters:suppressParameterEncoding:ignoreUserLocation:
+ _objc_msgSend$defaultBagV3
+ _objc_msgSend$getConfigPathV3WithCompletion:
+ _objc_msgSend$getMaxLocalSettingsAgeV3WithCompletion:
+ _objc_msgSend$getNowPlayingEnabledV3WithCompletion:
+ _objc_msgSend$getUTSBaseURLV3WithCompletion:
+ _objc_msgSend$getWatchListSettingsURLsV3WithCompletion:
+ _objc_msgSend$isSimpleProfile
+ _objc_msgSend$wlk_URLWithServerConfig:endpoint:baseURLString:queryParameters:suppressParameterEncoding:ignoreUserLocation:
- GCC_except_table36
- GCC_except_table41
- _objc_msgSend$URLRequestWithConfiguration:
- _objc_msgSend$_configURLString:
CStrings:
+ "%@: tricycle enabled but base URL could not be resolved from the V3 bag"
+ "-[WLKURLRequestProperties URLRequestWithConfiguration:baseURLString:]"
+ "AlwaysShowProfileSelection"
+ "NSURL-WLKAdditions: Failed to fetch baseURL"
+ "SignLanguageEnabled"
+ "sp_personal"
+ "sparkle_related_v2"
+ "sparkle_v2"
+ "tricycle"
+ "v16@?0@\"NSString\"8"
+ "v16@?0@\"NSURLRequest\"8"
+ "v16@?0Q8"
+ "v24@?0@\"NSNumber\"8@\"NSError\"16"
+ "v24@?0@\"NSString\"8@\"NSError\"16"
+ "v24@?0@\"NSURL\"8@\"NSError\"16"
+ "v32@?0@\"NSURL\"8@\"NSURL\"16@\"NSError\"24"
+ "v32@?0@\"NSURL\"8@\"NSURL\"16@\"NSNumber\"24"
- "-[WLKURLRequestProperties URLRequestWithConfiguration:]"
```
