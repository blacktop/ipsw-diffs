## WatchListKit

> `/System/Library/PrivateFrameworks/WatchListKit.framework/WatchListKit`

```diff

-800.20.10.0.0
-  __TEXT.__text: 0x5aabc
-  __TEXT.__auth_stubs: 0x840
-  __TEXT.__objc_methlist: 0x5ce8
+800.40.27.0.0
+  __TEXT.__text: 0x5a94c
+  __TEXT.__auth_stubs: 0x820
+  __TEXT.__objc_methlist: 0x5d48
   __TEXT.__const: 0x12c
-  __TEXT.__cstring: 0x6b8b
+  __TEXT.__cstring: 0x6cae
   __TEXT.__oslogstring: 0x4b7c
   __TEXT.__gcc_except_tab: 0xb74
   __TEXT.__dlopen_cstrs: 0x5a
-  __TEXT.__unwind_info: 0x1984
-  __TEXT.__objc_classname: 0x11d8
-  __TEXT.__objc_methname: 0xe1da
+  __TEXT.__unwind_info: 0x1974
+  __TEXT.__objc_classname: 0x11e9
+  __TEXT.__objc_methname: 0xe308
   __TEXT.__objc_methtype: 0x1ade
-  __TEXT.__objc_stubs: 0x8c60
-  __DATA_CONST.__got: 0x1f0
-  __DATA_CONST.__const: 0x2168
-  __DATA_CONST.__objc_classlist: 0x500
-  __DATA_CONST.__objc_catlist: 0x58
+  __TEXT.__objc_stubs: 0x8c00
+  __DATA_CONST.__got: 0x1e0
+  __DATA_CONST.__const: 0x2150
+  __DATA_CONST.__objc_classlist: 0x508
+  __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0x98
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0xd580
-  __DATA_CONST.__objc_selrefs: 0x3060
+  __DATA_CONST.__objc_const: 0xd6a8
+  __DATA_CONST.__objc_selrefs: 0x3078
+  __DATA_CONST.__objc_protorefs: 0x20
+  __DATA_CONST.__objc_classrefs: 0x690
+  __DATA_CONST.__objc_superrefs: 0x470
   __DATA_CONST.__objc_arraydata: 0x198
-  __AUTH_CONST.__cfstring: 0x8260
+  __AUTH_CONST.__cfstring: 0x83a0
   __AUTH_CONST.__objc_intobj: 0x378
-  __AUTH_CONST.__objc_const: 0x4208
+  __AUTH_CONST.__objc_const: 0x4210
   __AUTH_CONST.__const: 0xd20
   __AUTH_CONST.__objc_dictobj: 0x140
   __AUTH_CONST.__objc_arrayobj: 0x60
-  __AUTH_CONST.__auth_got: 0x430
-  __AUTH.__objc_data: 0x18b0
-  __DATA.__objc_protorefs: 0x20
-  __DATA.__objc_classrefs: 0x688
-  __DATA.__objc_superrefs: 0x468
-  __DATA.__objc_ivar: 0x974
+  __AUTH_CONST.__auth_got: 0x420
+  __AUTH.__objc_data: 0x1900
+  __DATA.__objc_ivar: 0x984
   __DATA.__data: 0x7a0
   __DATA.__bss: 0x110
   __DATA_DIRTY.__objc_data: 0x1950

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A8A2FBE4-3288-3078-AF77-E80668D2B33C
-  Functions: 2382
-  Symbols:   8933
-  CStrings:  5527
+  UUID: 15E08C5D-C60D-34CA-B8D9-C89C4F5FCD6F
+  Functions: 2383
+  Symbols:   8939
+  CStrings:  5560
 
Symbols:
+ -[WLKAMSMediaProxy .cxx_destruct]
+ -[WLKAMSMediaProxy _initializeProperties:]
+ -[WLKAMSMediaProxy buyParameters]
+ -[WLKAMSMediaProxy contentRatingsBySystemDictionary]
+ -[WLKAMSMediaProxy hasInAppPurchases]
+ -[WLKAMSMediaProxy initWithDictionary:]
+ -[WLKAMSMediaProxy setHasInAppPurchases:]
+ -[WLKAMSMediaProxy subtitle]
+ -[WLKSettingsStore postPlayAutoPlayNextVideo]
+ -[WLKSettingsStore setPostPlayAutoPlayNextVideo:]
+ -[_WLKAppInstallSession _doPurchaseWithAppAdamID:offerBuyParams:]
+ GCC_except_table101
+ GCC_except_table105
+ GCC_except_table107
+ GCC_except_table116
+ GCC_except_table63
+ GCC_except_table78
+ GCC_except_table79
+ GCC_except_table83
+ GCC_except_table92
+ GCC_except_table99
+ _OBJC_CLASS_$_AMSMediaTask
+ _OBJC_CLASS_$_WLKAMSMediaProxy
+ _OBJC_IVAR_$_WLKAMSMediaProxy._buyParameters
+ _OBJC_IVAR_$_WLKAMSMediaProxy._contentRatingsBySystemDictionary
+ _OBJC_IVAR_$_WLKAMSMediaProxy._hasInAppPurchases
+ _OBJC_IVAR_$_WLKAMSMediaProxy._subtitle
+ _OBJC_METACLASS_$_WLKAMSMediaProxy
+ _WLKMediaAPIClientIdentifier
+ _WLKMediaAPIClientVersion
+ __OBJC_$_INSTANCE_METHODS_WLKAMSMediaProxy
+ __OBJC_$_INSTANCE_VARIABLES_WLKAMSMediaProxy
+ __OBJC_$_PROP_LIST_WLKAMSMediaProxy
+ __OBJC_CLASS_RO_$_WLKAMSMediaProxy
+ __OBJC_METACLASS_RO_$_WLKAMSMediaProxy
+ ___132-[WLKSportsFavoriteManager watchlistd_performUserSettingsAction:setFavoritesSyncEnabled:caller:overrideLastModifiedDate:completion:]_block_invoke.189
+ ___39-[WLKSportsFavoriteManager _connection]_block_invoke.169
+ ___40-[WLKSportsFavoriteManager isOnboarded:]_block_invoke.176
+ ___40-[WLKSportsFavoriteManager isOnboarded:]_block_invoke_2.177
+ ___42-[WLKSportsFavoriteManager initWithCache:]_block_invoke.150
+ ___42-[WLKSportsFavoriteManager initWithCache:]_block_invoke.156
+ ___49-[WLKSettingsStore setPostPlayAutoPlayNextVideo:]_block_invoke
+ ___65-[_WLKAppInstallSession _doPurchaseWithAppAdamID:offerBuyParams:]_block_invoke
+ ___69-[WLKSportsFavoriteManager _performAction:withIDs:caller:completion:]_block_invoke.180
+ ___69-[WLKSportsFavoriteManager _performAction:withIDs:caller:completion:]_block_invoke.182
+ ___97-[WLKSportsFavoriteManager _performUserSettingsAction:setFavoritesSyncEnabled:caller:completion:]_block_invoke.184
+ ___block_descriptor_48_e8_32s40s_e36_v24?0"AMSMediaResult"8"NSError"16ls32l8s40l8
+ ___block_literal_global.111
+ ___block_literal_global.120
+ ___block_literal_global.168
+ ___block_literal_global.171
+ ___block_literal_global.174
+ ___block_literal_global.198
+ ___block_literal_global.86
+ _objc_msgSend$_doPurchaseWithAppAdamID:offerBuyParams:
+ _objc_msgSend$_initializeProperties:
+ _objc_msgSend$booleanForKey:
+ _objc_msgSend$cachedBooleanForKey:
+ _objc_msgSend$initWithType:clientIdentifier:clientVersion:bag:
+ _objc_msgSend$perform
+ _objc_msgSend$setItemIdentifiers:
+ _objc_msgSend$urlForKey:
- -[AMSBagValue(WLKAdditions) wlk_quietValueWithCompletion:]
- -[AMSBagValue(WLKAdditions) wlk_quietValueWithError:]
- -[_WLKAppInstallSession _doPurchaseWithAppAdamID:offer:]
- GCC_except_table102
- GCC_except_table104
- GCC_except_table113
- GCC_except_table60
- GCC_except_table76
- GCC_except_table80
- GCC_except_table89
- GCC_except_table96
- GCC_except_table98
- _AMSErrorIsEqual
- _AMSLookupKeyProfileLockup
- _OBJC_CLASS_$_AMSBagValue
- _OBJC_CLASS_$_AMSLookup
- _WLKshouldRetryError
- __OBJC_$_CATEGORY_AMSBagValue_$_WLKAdditions
- __OBJC_$_INSTANCE_METHODS_AMSBagValue(WLKAdditions)
- __SanitizedAMSError
- ___132-[WLKSportsFavoriteManager watchlistd_performUserSettingsAction:setFavoritesSyncEnabled:caller:overrideLastModifiedDate:completion:]_block_invoke.188
- ___39-[WLKSportsFavoriteManager _connection]_block_invoke.168
- ___40-[WLKSportsFavoriteManager isOnboarded:]_block_invoke.175
- ___40-[WLKSportsFavoriteManager isOnboarded:]_block_invoke_2.176
- ___42-[WLKSportsFavoriteManager initWithCache:]_block_invoke.149
- ___42-[WLKSportsFavoriteManager initWithCache:]_block_invoke.154
- ___55+[WLKURLBagUtilities isFullTVAppEnabledWithCompletion:]_block_invoke
- ___56-[_WLKAppInstallSession _doPurchaseWithAppAdamID:offer:]_block_invoke
- ___58-[AMSBagValue(WLKAdditions) wlk_quietValueWithCompletion:]_block_invoke
- ___69-[WLKSportsFavoriteManager _performAction:withIDs:caller:completion:]_block_invoke.179
- ___69-[WLKSportsFavoriteManager _performAction:withIDs:caller:completion:]_block_invoke.181
- ___97-[WLKSportsFavoriteManager _performUserSettingsAction:setFavoritesSyncEnabled:caller:completion:]_block_invoke.182
- ___WLKFetchBaseURLWithCompletion_block_invoke
- ___WLKFetchNotificationCategories_block_invoke
- ___WLKFetchNowPlayingEnabledReturningError_block_invoke
- ___WLKFetchPrivacyAcknowledgementURLWithCompletionHandler_block_invoke
- ___block_descriptor_40_e8_32bs_e23_v28?08B16"NSError"20ls32l8
- ___block_descriptor_48_e8_32s40s_e37_v24?0"AMSLookupResult"8"NSError"16ls32l8s40l8
- ___block_literal_global.102
- ___block_literal_global.119
- ___block_literal_global.167
- ___block_literal_global.170
- ___block_literal_global.173
- ___block_literal_global.193
- ___block_literal_global.83
- __kCFStreamErrorCodeKey
- _objc_msgSend$URLForKey:
- _objc_msgSend$_doPurchaseWithAppAdamID:offer:
- _objc_msgSend$allItems
- _objc_msgSend$bagSubProfile
- _objc_msgSend$bagSubProfileVersion
- _objc_msgSend$initWithBag:caller:keyProfile:
- _objc_msgSend$performLookupWithBundleIdentifiers:itemIdentifiers:
- _objc_msgSend$valueWithCompletion:
- _objc_msgSend$valueWithError:
- _objc_msgSend$wlk_quietValueWithCompletion:
- _objc_msgSend$wlk_quietValueWithError:
- _objc_release_x2
CStrings:
+ "PostPlayAutoPlayNextVideo"
+ "T@\"NSArray\",R,N,V_buyParameters"
+ "T@\"NSDictionary\",R,N,V_contentRatingsBySystemDictionary"
+ "T@\"NSString\",?,R,C"
+ "T@\"NSString\",R,N,V_subtitle"
+ "TB,?,R,N"
+ "TB,N,V_hasInAppPurchases"
+ "WLKAMSMediaProxy"
+ "WLKAMSMediaProxy: properties are: _contentRatingsBySystemDictionary:%@,_hasInAppPurchases:%d,_substitle:%@,_buyParameters: %@"
+ "WLKAppInstaller - Lookup succeeded."
+ "_contentRatingsBySystemDictionary"
+ "_doPurchaseWithAppAdamID:offerBuyParams:"
+ "_hasInAppPurchases"
+ "_initializeProperties:"
+ "_subtitle"
+ "appletvos"
+ "attributes"
+ "booleanForKey:"
+ "cachedBooleanForKey:"
+ "com.tv.videosui"
+ "contentRatingsBySystem"
+ "contentRatingsBySystemDictionary"
+ "dictionary response is invalid and does not have valid node."
+ "hasInAppPurchases"
+ "initWithType:clientIdentifier:clientVersion:bag:"
+ "perform"
+ "platformAttributes"
+ "postPlayAutoPlayNextVideo"
+ "setHasInAppPurchases:"
+ "setItemIdentifiers:"
+ "setPostPlayAutoPlayNextVideo:"
+ "subtitle"
+ "topaz"
+ "urlForKey:"
+ "v24@?0@\"AMSMediaResult\"8@\"NSError\"16"
- "URLForKey:"
- "WLKBaseURLReturningError - Retry - Error: %@"
- "_doPurchaseWithAppAdamID:offer:"
- "allItems"
- "bagSubProfile"
- "bagSubProfileVersion"
- "initWithBag:caller:keyProfile:"
- "performLookupWithBundleIdentifiers:itemIdentifiers:"
- "v24@?0@\"AMSLookupResult\"8@\"NSError\"16"
- "v28@?0@8B16@\"NSError\"20"
- "valueWithCompletion:"
- "valueWithError:"
- "wlk_quietValueWithCompletion:"
- "wlk_quietValueWithError:"

```
