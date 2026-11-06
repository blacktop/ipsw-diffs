## WatchListKit

> `/System/Library/PrivateFrameworks/WatchListKit.framework/Versions/A/WatchListKit`

```diff

-952.0.1.0.0
-  __TEXT.__text: 0x650e8
-  __TEXT.__objc_methlist: 0x6d14
+952.10.8.0.0
+  __TEXT.__text: 0x66b48
+  __TEXT.__objc_methlist: 0x6d84
   __TEXT.__const: 0x19c
-  __TEXT.__cstring: 0x7506
-  __TEXT.__oslogstring: 0x5a21
+  __TEXT.__cstring: 0x7688
+  __TEXT.__oslogstring: 0x5a95
   __TEXT.__gcc_except_tab: 0xd30
-  __TEXT.__unwind_info: 0x1c08
+  __TEXT.__unwind_info: 0x1c58
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xc68
+  __DATA_CONST.__const: 0xc58
   __DATA_CONST.__objc_classlist: 0x548
   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3628
+  __DATA_CONST.__objc_selrefs: 0x36a8
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x498
   __DATA_CONST.__objc_arraydata: 0x620
   __DATA_CONST.__got: 0x818
-  __AUTH_CONST.__const: 0x2840
-  __AUTH_CONST.__cfstring: 0xa020
-  __AUTH_CONST.__objc_const: 0x11130
+  __AUTH_CONST.__const: 0x2a90
+  __AUTH_CONST.__cfstring: 0xa0c0
+  __AUTH_CONST.__objc_const: 0x111a0
   __AUTH_CONST.__objc_intobj: 0x360
   __AUTH_CONST.__objc_dictobj: 0x190
   __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x17c0
-  __DATA.__objc_ivar: 0xa14
+  __DATA.__objc_ivar: 0xa1c
   __DATA.__data: 0x618
   __DATA.__bss: 0xe8
   __DATA_DIRTY.__objc_data: 0x1d10
   __DATA_DIRTY.__data: 0x8
-  __DATA_DIRTY.__bss: 0x400
+  __DATA_DIRTY.__bss: 0x3f8
   __DATA_DIRTY.__common: 0x5
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts
   - /System/Library/Frameworks/CFNetwork.framework/Versions/A/CFNetwork

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2737
-  Symbols:   6646
-  CStrings:  1822
+  Functions: 2767
+  Symbols:   6690
+  CStrings:  1839
 
Symbols:
+ +[NSURL(WLKAdditions) _wlk_URLWithServerConfig:fullPath:endpoint:queryParameters:suppressParameterEncoding:ignoreUserLocation:]
+ +[NSURL(WLKAdditions) wlk_URLWithServerConfig:endpoint:baseURLString:queryParameters:suppressParameterEncoding:ignoreUserLocation:]
+ +[WLKConfigurationRequest _configURLStringWithCompletion:]
+ -[WLKSystemPreferencesStore alwaysShowProfileSelection]
+ -[WLKSystemPreferencesStore setAlwaysShowProfileSelection:]
+ -[WLKSystemPreferencesStore setSignLanguageCode:]
+ -[WLKSystemPreferencesStore setSignLanguageCodeDownload:]
+ -[WLKSystemPreferencesStore signLanguageCodeDownload]
+ -[WLKSystemPreferencesStore signLanguageCode]
+ -[WLKURLRequestProperties URLRequestWithConfiguration:baseURLString:]
+ OBJC_IVAR_$_WLKSystemPreferencesStore._preferencesCache
+ OBJC_IVAR_$_WLKSystemPreferencesStore._preferencesCacheLock
+ _WLKSignLanguageCodeASL
+ _WLKSignLanguageCodeBSL
+ __107+[WLKConfigurationRequest _fetchV3WithOptions:cachePolicy:sessionConfiguration:queryParameters:completion:]_block_invoke
+ __51-[WLKUTSNetworkRequestOperation prepareURLRequest:]_block_invoke
+ __55+[WLKURLBagUtilities isFullTVAppEnabledWithCompletion:]_block_invoke
+ __58+[WLKConfigurationRequest _configURLStringWithCompletion:]_block_invoke
+ __61+[WLKSettingsCloudUtilities _cloudSyncEnabledWithCompletion:]_block_invoke
+ __WLKFetchBaseURLWithCompletion_block_invoke
+ __WLKFetchNowPlayingEnabledReturningError_block_invoke
+ ___55+[WLKURLBagUtilities isFullTVAppEnabledWithCompletion:]_block_invoke_2
+ ___58+[WLKConfigurationRequest _configURLStringWithCompletion:]_block_invoke
+ ___58+[WLKConfigurationRequest _configURLStringWithCompletion:]_block_invoke_2
+ ___61+[WLKSettingsCloudUtilities _cloudSyncEnabledWithCompletion:]_block_invoke_2
+ ___61+[WLKSettingsCloudUtilities _cloudSyncEnabledWithCompletion:]_block_invoke_3
+ ___WLKFetchNowPlayingEnabledReturningError_block_invoke_2
+ ___block_descriptor_40_e8_32bs_e27_v24?0"NSURL"8"NSError"16l
+ ___block_descriptor_40_e8_32bs_e30_v24?0"NSNumber"8"NSError"16l
+ ___block_descriptor_40_e8_32bs_e30_v24?0"NSString"8"NSError"16l
+ ___block_descriptor_40_e8_32bs_e38_v32?0"NSURL"8"NSURL"16"NSNumber"24l
+ ___block_descriptor_48_e8_32bs_e37_v32?0"NSURL"8"NSURL"16"NSError"24l
+ ___block_descriptor_48_e8_32s40bs_e18_v16?0"NSString"8l
+ ___block_descriptor_48_e8_32s40bs_e30_v24?0"NSNumber"8"NSError"16l
+ ___block_descriptor_56_e8_32s40s48bs_e30_v24?0"NSString"8"NSError"16l
+ ___block_descriptor_56_e8_32s40s48bs_e8_v16?0Q8l
+ ___block_descriptor_64_e8_32s40s48bs_e30_v24?0"NSNumber"8"NSError"16l
+ ___block_descriptor_64_e8_32s40s48s56bs_e22_v16?0"NSURLRequest"8l
+ ___block_descriptor_64_e8_32s40s48s56bs_e5_v8?0l
+ ___block_descriptor_72_e8_32s40s48bs_e30_v24?0"NSString"8"NSError"16l
+ _objc_msgSend$URLRequestWithConfiguration:baseURLString:
+ _objc_msgSend$_configURLStringWithCompletion:
+ _objc_msgSend$_wlk_URLWithServerConfig:fullPath:endpoint:queryParameters:suppressParameterEncoding:ignoreUserLocation:
+ _objc_msgSend$defaultBagV3
+ _objc_msgSend$getConfigPathV3WithCompletion:
+ _objc_msgSend$getMaxLocalSettingsAgeV3WithCompletion:
+ _objc_msgSend$getNowPlayingEnabledV3WithCompletion:
+ _objc_msgSend$getUTSBaseURLV3WithCompletion:
+ _objc_msgSend$getWatchListSettingsURLsV3WithCompletion:
+ _objc_msgSend$wlk_URLWithServerConfig:endpoint:baseURLString:queryParameters:suppressParameterEncoding:ignoreUserLocation:
- GCC_except_table12
- GCC_except_table53
- _WLKFeatureEnablementAdditionalFlags_block_invoke.sparkleEnabledDefaultsValue
- ___block_descriptor_32_e8_v12?0i8l
- _objc_msgSend$URLRequestWithConfiguration:
- _objc_msgSend$_configURLString:
CStrings:
+ "%@: tricycle enabled but base URL could not be resolved from the V3 bag"
+ "-[WLKURLRequestProperties URLRequestWithConfiguration:baseURLString:]"
+ "AlwaysShowProfileSelection"
+ "NSURL-WLKAdditions: Failed to fetch baseURL"
+ "PreferredSignLanguage"
+ "PreferredSignLanguageDownload"
+ "ase"
+ "bfi"
+ "com.apple.AppleTV.signLanguageSettingDidChange"
+ "sparkle_related_v2"
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
- "sparkle"
```
