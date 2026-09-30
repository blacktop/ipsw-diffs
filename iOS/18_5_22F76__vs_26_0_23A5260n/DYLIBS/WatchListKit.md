## WatchListKit

> `/System/Library/PrivateFrameworks/WatchListKit.framework/WatchListKit`

```diff

-850.50.2.0.0
-  __TEXT.__text: 0x65aa4
-  __TEXT.__auth_stubs: 0x850
-  __TEXT.__objc_methlist: 0x6eac
-  __TEXT.__const: 0x1ac
-  __TEXT.__cstring: 0x7986
-  __TEXT.__oslogstring: 0x6031
-  __TEXT.__gcc_except_tab: 0x1210
-  __TEXT.__dlopen_cstrs: 0x5a
-  __TEXT.__unwind_info: 0x1e30
-  __TEXT.__objc_classname: 0x1320
-  __TEXT.__objc_methname: 0xfe4f
-  __TEXT.__objc_methtype: 0x1c59
-  __TEXT.__objc_stubs: 0x9b80
-  __DATA_CONST.__got: 0x8d8
-  __DATA_CONST.__const: 0x2780
+902.0.0.0.0
+  __TEXT.__text: 0x66b50
+  __TEXT.__auth_stubs: 0x810
+  __TEXT.__objc_methlist: 0x6fc4
+  __TEXT.__const: 0x1a4
+  __TEXT.__cstring: 0x7a5d
+  __TEXT.__oslogstring: 0x6327
+  __TEXT.__gcc_except_tab: 0x11b0
+  __TEXT.__unwind_info: 0x1dd8
+  __TEXT.__objc_classname: 0x1321
+  __TEXT.__objc_methname: 0x105c2
+  __TEXT.__objc_methtype: 0x1da5
+  __TEXT.__objc_stubs: 0x9c60
+  __DATA_CONST.__got: 0x8f8
+  __DATA_CONST.__const: 0x2760
   __DATA_CONST.__objc_classlist: 0x560
   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0x98
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3838
+  __DATA_CONST.__objc_selrefs: 0x38d0
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x4b0
-  __DATA_CONST.__objc_arraydata: 0x620
-  __AUTH_CONST.__auth_got: 0x438
-  __AUTH_CONST.__const: 0xe60
-  __AUTH_CONST.__cfstring: 0xa100
-  __AUTH_CONST.__objc_const: 0x119b8
-  __AUTH_CONST.__objc_intobj: 0x390
+  __DATA_CONST.__objc_arraydata: 0x628
+  __AUTH_CONST.__auth_got: 0x418
+  __AUTH_CONST.__const: 0xe80
+  __AUTH_CONST.__cfstring: 0xa340
+  __AUTH_CONST.__objc_const: 0x11b00
+  __AUTH_CONST.__objc_intobj: 0x378
   __AUTH_CONST.__objc_dictobj: 0x190
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH.__objc_data: 0xf0
-  __DATA.__objc_ivar: 0xa10
+  __DATA.__objc_ivar: 0xa28
   __DATA.__data: 0x7a0
-  __DATA.__bss: 0x110
+  __DATA.__bss: 0x108
   __DATA_DIRTY.__objc_data: 0x34d0
   __DATA_DIRTY.__data: 0x8
-  __DATA_DIRTY.__bss: 0x438
+  __DATA_DIRTY.__bss: 0x430
   __DATA_DIRTY.__common: 0x8
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork

   - /System/Library/Frameworks/Intents.framework/Intents
   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/Frameworks/UserNotifications.framework/UserNotifications
+  - /System/Library/Frameworks/_LocationEssentials.framework/_LocationEssentials
+  - /System/Library/PrivateFrameworks/AppStoreDaemon.framework/AppStoreDaemon
   - /System/Library/PrivateFrameworks/AppSupport.framework/AppSupport
   - /System/Library/PrivateFrameworks/AppleMediaServices.framework/AppleMediaServices
   - /System/Library/PrivateFrameworks/ChronoServices.framework/ChronoServices

   - /System/Library/PrivateFrameworks/MediaRemote.framework/MediaRemote
   - /System/Library/PrivateFrameworks/NanoPreferencesSync.framework/NanoPreferencesSync
   - /System/Library/PrivateFrameworks/ParsecSubscriptionServiceSupport.framework/ParsecSubscriptionServiceSupport
-  - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
+  - /System/Library/PrivateFrameworks/SetupAssistant.framework/SetupAssistant
   - /System/Library/PrivateFrameworks/TVAppServices.framework/TVAppServices
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 0039C21C-D07B-3141-AEFD-572E40EFFC22
-  Functions: 2715
-  Symbols:   9998
-  CStrings:  6354
+  UUID: C8C50F1C-5148-3C41-A02C-31882972814D
+  Functions: 2742
+  Symbols:   10053
+  CStrings:  6427
 
Symbols:
+ +[WLKContinueWatchingRequestOperation isHeicFormatAllowed]
+ +[WLKPlaybackSummary EBSSummaryWithBundleID:channelID:externalId:accountID:externalProfileID:timestamp:playbackState:playbackRate:currentPlaybackDate:playablePassthrough:]
+ +[WLKPlaybackSummary VODSummaryWithBundleID:channelID:contentID:accountID:externalProfileID:timestamp:duration:elapsedTime:featureDuration:featureElapsedTime:playbackState:playbackRate:contentTitle:completionState:]
+ +[WLKPlaybackSummary VODSummaryWithBundleID:channelID:contentID:accountID:externalProfileID:timestamp:duration:elapsedTime:featureDuration:featureElapsedTime:playbackState:playbackRate:playablePassthrough:contentTitle:completionState:]
+ +[WLKPlaybackSummary VODSummaryWithBundleID:channelID:contentID:accountID:externalProfileID:timestamp:duration:elapsedTime:playbackState:playbackRate:contentTitle:completionState:]
+ +[WLKPlaybackSummary VODSummaryWithBundleID:channelID:contentID:accountID:externalProfileID:timestamp:duration:elapsedTime:playbackState:playbackRate:playablePassthrough:contentTitle:completionState:]
+ +[WLKPlaybackSummary liveSummaryWithBundleID:channelID:serviceID:accountID:externalProfileID:timestamp:playbackState:playbackRate:currentPlaybackDate:playablePassthrough:]
+ -[WLKPlayActivityDecorateEBSOperation initWithChannelID:externalContentID:playablePassthrough:]
+ -[WLKPlayActivityDecorateEBSOperation initWithChannelID:externalContentID:playablePassthrough:].cold.1
+ -[WLKPlayActivityDecorateEBSOperation initWithChannelID:externalContentID:playablePassthrough:].cold.2
+ -[WLKPlayActivityDecorateEBSOperation initWithChannelID:externalContentID:playablePassthrough:].cold.3
+ -[WLKPlayActivityDecorateEBSOperation playablePassthrough]
+ -[WLKPlayActivityDecorateLiveOperation initWithChannelID:serviceID:playablePassthrough:]
+ -[WLKPlayActivityDecorateLiveOperation initWithChannelID:serviceID:playablePassthrough:].cold.1
+ -[WLKPlayActivityDecorateLiveOperation initWithChannelID:serviceID:playablePassthrough:].cold.2
+ -[WLKPlayActivityDecorateLiveOperation initWithChannelID:serviceID:playablePassthrough:].cold.3
+ -[WLKPlayActivityDecorateLiveOperation playablePassthrough]
+ -[WLKPlayActivityDecorateVODOperation initWithExternalId:brandId:hlsAssetDuration:playablePassthrough:]
+ -[WLKPlayActivityDecorateVODOperation initWithExternalId:brandId:hlsAssetDuration:playablePassthrough:].cold.1
+ -[WLKPlayActivityDecorateVODOperation initWithExternalId:brandId:hlsAssetDuration:playablePassthrough:].cold.2
+ -[WLKPlayActivityDecorateVODOperation initWithExternalId:brandId:hlsAssetDuration:playablePassthrough:].cold.3
+ -[WLKPlayActivityDecorateVODOperation initWithExternalId:brandId:hlsAssetDuration:playablePassthrough:].cold.4
+ -[WLKPlayActivityDecorateVODOperation processResponse].cold.1
+ -[WLKPlayActivityDecorateVODOperation processResponse].cold.2
+ -[WLKPlaybackSummary contentTitle]
+ -[WLKPlaybackSummary initWithBundleID:timestamp:duration:elapsedTime:featureDuration:featureElapsedTime:externalProfileID:contentID:accountID:playbackState:playbackRate:completionState:isAlwaysLive:serviceID:currentPlaybackDate:playbackType:isTimerDerived:isFromActivePlayerPath:channelID:contentTitle:]
+ -[WLKPlaybackSummary initWithBundleID:timestamp:duration:elapsedTime:featureDuration:featureElapsedTime:externalProfileID:contentID:accountID:playbackState:playbackRate:completionState:isAlwaysLive:serviceID:currentPlaybackDate:playbackType:isTimerDerived:isFromActivePlayerPath:playablePassthrough:channelID:contentTitle:]
+ -[WLKPlaybackSummary playablePassthrough]
+ -[WLKReachabilityMonitor setIsNetworkReachable:]
+ -[WLKReachabilityMonitor setIsWifiEnabled:]
+ -[WLKSystemPreferencesStore appAppearance]
+ -[WLKSystemPreferencesStore autoDownloadsEpisodeCount]
+ -[WLKSystemPreferencesStore autoDownloadsStorageLimit]
+ -[WLKSystemPreferencesStore setAppAppearance:]
+ -[WLKSystemPreferencesStore setAutoDownloadsEpisodeCount:]
+ -[WLKSystemPreferencesStore setAutoDownloadsStorageLimit:]
+ -[WLKSystemPreferencesStore setUseAutomaticDownloads:]
+ -[WLKSystemPreferencesStore useAutomaticDownloads]
+ -[WLKUTSNetworkRequestWrappingOperation amsUrlResponse]
+ GCC_except_table39
+ GCC_except_table73
+ GCC_except_table89
+ _MCFeatureMaximumAppsRating
+ _OBJC_CLASS_$_ASDPurchase
+ _OBJC_CLASS_$_ASDPurchaseManager
+ _OBJC_CLASS_$_TVAppAccountStoreObjC
+ _OBJC_IVAR_$_WLKPlayActivityDecorateEBSOperation._playablePassthrough
+ _OBJC_IVAR_$_WLKPlayActivityDecorateLiveOperation._playablePassthrough
+ _OBJC_IVAR_$_WLKPlaybackSummary._contentTitle
+ _OBJC_IVAR_$_WLKPlaybackSummary._playablePassthrough
+ _OBJC_IVAR_$_WLKReachabilityMonitor._isNetworkReachable
+ _OBJC_IVAR_$_WLKReachabilityMonitor._isWifiEnabled
+ _TVASDefaultSupportPath
+ _TVASDefaultSupportPath._path
+ _TVASDefaultSupportPath.cold.1
+ _TVASDefaultSupportPath.onceToken
+ _TVASTVAppGroupSharedContainer
+ _VideosAppAppearanceOptionDark
+ _VideosAppAppearanceOptionLight
+ _VideosAppAppearanceOptionSystem
+ _WLKRestrictionsMaximumEffectiveAppRanking
+ __OBJC_$_INSTANCE_VARIABLES_WLKReachabilityMonitor
+ ___30-[WLKOfferManager _connection]_block_invoke.76
+ ___31-[WLKOfferManager clearOffers:]_block_invoke.69
+ ___51-[WLKSportsFavoriteManager handleAccountDidChange:]_block_invoke
+ ___TVASDefaultSupportPath_block_invoke
+ ___block_literal_global.108
+ ___block_literal_global.14
+ ___block_literal_global.75
+ _kMRMediaRemoteNowPlayingInfoTitle
+ _objc_msgSend$VODSummaryWithBundleID:channelID:contentID:accountID:externalProfileID:timestamp:duration:elapsedTime:featureDuration:featureElapsedTime:playbackState:playbackRate:contentTitle:completionState:
+ _objc_msgSend$VODSummaryWithBundleID:channelID:contentID:accountID:externalProfileID:timestamp:duration:elapsedTime:featureDuration:featureElapsedTime:playbackState:playbackRate:playablePassthrough:contentTitle:completionState:
+ _objc_msgSend$VODSummaryWithBundleID:channelID:contentID:accountID:externalProfileID:timestamp:duration:elapsedTime:playbackState:playbackRate:contentTitle:completionState:
+ _objc_msgSend$accountWithDSID:
+ _objc_msgSend$activeOrLocalAccount
+ _objc_msgSend$amsUrlResponse
+ _objc_msgSend$contentTitle
+ _objc_msgSend$initWithBundleID:timestamp:duration:elapsedTime:featureDuration:featureElapsedTime:externalProfileID:contentID:accountID:playbackState:playbackRate:completionState:isAlwaysLive:serviceID:currentPlaybackDate:playbackType:isTimerDerived:isFromActivePlayerPath:channelID:contentTitle:
+ _objc_msgSend$initWithBundleID:timestamp:duration:elapsedTime:featureDuration:featureElapsedTime:externalProfileID:contentID:accountID:playbackState:playbackRate:completionState:isAlwaysLive:serviceID:currentPlaybackDate:playbackType:isTimerDerived:isFromActivePlayerPath:playablePassthrough:channelID:contentTitle:
+ _objc_msgSend$initWithDomain:code:userInfo:
+ _objc_msgSend$isFullTVAppEnabledCachedValue
+ _objc_msgSend$isHeicFormatAllowed
+ _objc_msgSend$playablePassthrough
- -[WLKPlayActivityDecorateEBSOperation initWithChannelID:externalContentID:]
- -[WLKPlayActivityDecorateEBSOperation initWithChannelID:externalContentID:].cold.1
- -[WLKPlayActivityDecorateEBSOperation initWithChannelID:externalContentID:].cold.2
- -[WLKPlayActivityDecorateLiveOperation initWithChannelID:serviceID:]
- -[WLKPlayActivityDecorateLiveOperation initWithChannelID:serviceID:].cold.1
- -[WLKPlayActivityDecorateLiveOperation initWithChannelID:serviceID:].cold.2
- -[WLKPlayActivityDecorateVODOperation initWithExternalId:brandId:hlsAssetDuration:]
- -[WLKPlayActivityDecorateVODOperation initWithExternalId:brandId:hlsAssetDuration:].cold.1
- -[WLKPlayActivityDecorateVODOperation initWithExternalId:brandId:hlsAssetDuration:].cold.2
- -[WLKPlayActivityDecorateVODOperation initWithExternalId:brandId:hlsAssetDuration:].cold.3
- -[WLKPlaybackSummary initWithBundleID:timestamp:duration:elapsedTime:featureDuration:featureElapsedTime:externalProfileID:contentID:accountID:playbackState:playbackRate:completionState:isAlwaysLive:serviceID:currentPlaybackDate:playbackType:isTimerDerived:isFromActivePlayerPath:channelID:]
- GCC_except_table38
- GCC_except_table68
- GCC_except_table72
- GCC_except_table88
- GCC_except_table90
- _AppStoreDaemonLibrary
- _AppStoreDaemonLibraryCore.frameworkLibrary
- _OBJC_CLASS_$_ACAccountStore
- ___30-[WLKOfferManager _connection]_block_invoke.75
- ___31-[WLKOfferManager clearOffers:]_block_invoke_2
- ___AppStoreDaemonLibraryCore_block_invoke
- ___block_descriptor_40_e8_32r_e5_v8?0lr32l8
- ___block_literal_global.74
- ___getASDPurchaseClass_block_invoke
- ___getASDPurchaseClass_block_invoke.cold.1
- ___getASDPurchaseManagerClass_block_invoke
- ___getASDPurchaseManagerClass_block_invoke.cold.1
- __sl_dlopen
- _abort_report_np
- _audit_stringAppStoreDaemon
- _free
- _getASDPurchaseClass.softClass
- _getASDPurchaseManagerClass.softClass
- _objc_getClass
- _objc_msgSend$VODSummaryWithBundleID:channelID:contentID:accountID:externalProfileID:timestamp:duration:elapsedTime:featureDuration:featureElapsedTime:playbackState:playbackRate:completionState:
- _objc_msgSend$ams_activeiTunesAccount
- _objc_msgSend$ams_iTunesAccountWithDSID:
- _objc_msgSend$ams_localiTunesAccount
- _objc_msgSend$ams_sharedAccountStore
- _objc_msgSend$initWithBundleID:timestamp:duration:elapsedTime:featureDuration:featureElapsedTime:externalProfileID:contentID:accountID:playbackState:playbackRate:completionState:isAlwaysLive:serviceID:currentPlaybackDate:playbackType:isTimerDerived:isFromActivePlayerPath:channelID:
CStrings:
+ "-[WLKPlayActivityDecorateEBSOperation initWithChannelID:externalContentID:playablePassthrough:]"
+ "-[WLKPlayActivityDecorateLiveOperation initWithChannelID:serviceID:playablePassthrough:]"
+ "-[WLKPlayActivityDecorateVODOperation initWithExternalId:brandId:hlsAssetDuration:playablePassthrough:]"
+ "@112@0:8@16@24@32@40@48@56@64@72q80@88@96q104"
+ "@120@0:8@16@24@32@40@48@56@64@72q80@88@96@104q112"
+ "@128@0:8@16@24@32@40@48@56@64@72@80@88q96@104@112q120"
+ "@136@0:8@16@24@32@40@48@56@64@72@80@88q96@104@112@120q128"
+ "@164@0:8@16@24@32@40@48@56@64@72@80q88@96q104B112@116@124q132B140B144@148@156"
+ "@172@0:8@16@24@32@40@48@56@64@72@80q88@96q104B112@116@124q132B140B144@148@156@164"
+ "@96@0:8@16@24@32@40@48@56q64@72@80@88"
+ "AppAppearanceOptions"
+ "AutoDownloads"
+ "AutoDownloadsEpisodeCount"
+ "AutoDownloadsStorageLimit"
+ "DarkAppearanceOption"
+ "EBSSummaryWithBundleID:channelID:externalId:accountID:externalProfileID:timestamp:playbackState:playbackRate:currentPlaybackDate:playablePassthrough:"
+ "Fetch full tv app enabled, fall back to previous cached value %@"
+ "LightAppearanceOption"
+ "SystemAppearanceOption"
+ "T@\"NSString\",R,C,N,V_playablePassthrough"
+ "T@\"NSString\",R,N,V_contentTitle"
+ "T@\"NSString\",R,N,V_playablePassthrough"
+ "TB,N,V_isNetworkReachable"
+ "TB,N,V_isWifiEnabled"
+ "VODSummaryWithBundleID:channelID:contentID:accountID:externalProfileID:timestamp:duration:elapsedTime:featureDuration:featureElapsedTime:playbackState:playbackRate:contentTitle:completionState:"
+ "VODSummaryWithBundleID:channelID:contentID:accountID:externalProfileID:timestamp:duration:elapsedTime:featureDuration:featureElapsedTime:playbackState:playbackRate:playablePassthrough:contentTitle:completionState:"
+ "VODSummaryWithBundleID:channelID:contentID:accountID:externalProfileID:timestamp:duration:elapsedTime:playbackState:playbackRate:contentTitle:completionState:"
+ "VODSummaryWithBundleID:channelID:contentID:accountID:externalProfileID:timestamp:duration:elapsedTime:playbackState:playbackRate:playablePassthrough:contentTitle:completionState:"
+ "WLKOfferManager - Error: daemon error when clearing offer: (%@)"
+ "WLKPlayActivityDecorateEBSOperation - Playable passthrough is missing for channelID - %@ and externalContentID - %@, we can still proceed with decorate call"
+ "WLKPlayActivityDecorateLiveOperation - Playable passthrough is missing for channelID - %@ and serviceID - %@, we can still proceed with decorate call"
+ "WLKPlayActivityDecorateVODOperation - CompoundId is nil. Cannot cache the metadata."
+ "WLKPlayActivityDecorateVODOperation - Playable passthrough is nil for externalID - %@ and brandID - %@, we can still proceed with decorate call"
+ "WLKPlayActivityDecorateVODOperation - WLKPlayActivityMetadata object is nil. Cannot cache it."
+ "WLKPlaybackActivity.contentTitle"
+ "WLKPlaybackActivity.playablePassthrough"
+ "_contentTitle"
+ "_isNetworkReachable"
+ "_isWifiEnabled"
+ "_playablePassthrough"
+ "accountWithDSID:"
+ "activeOrLocalAccount"
+ "appAppearance"
+ "autoDownloadsEpisodeCount"
+ "autoDownloadsStorageLimit"
+ "callas"
+ "com.apple.TV"
+ "contentTitle"
+ "group.tvappservices.container"
+ "heic"
+ "initWithBundleID:timestamp:duration:elapsedTime:featureDuration:featureElapsedTime:externalProfileID:contentID:accountID:playbackState:playbackRate:completionState:isAlwaysLive:serviceID:currentPlaybackDate:playbackType:isTimerDerived:isFromActivePlayerPath:channelID:contentTitle:"
+ "initWithBundleID:timestamp:duration:elapsedTime:featureDuration:featureElapsedTime:externalProfileID:contentID:accountID:playbackState:playbackRate:completionState:isAlwaysLive:serviceID:currentPlaybackDate:playbackType:isTimerDerived:isFromActivePlayerPath:playablePassthrough:channelID:contentTitle:"
+ "initWithChannelID:externalContentID:playablePassthrough:"
+ "initWithChannelID:serviceID:playablePassthrough:"
+ "initWithDomain:code:userInfo:"
+ "initWithExternalId:brandId:hlsAssetDuration:playablePassthrough:"
+ "isHeicFormatAllowed"
+ "jpeg"
+ "liveSummaryWithBundleID:channelID:serviceID:accountID:externalProfileID:timestamp:playbackState:playbackRate:currentPlaybackDate:playablePassthrough:"
+ "menkaure"
+ "opal"
+ "playablePassthrough"
+ "setAppAppearance:"
+ "setAutoDownloadsEpisodeCount:"
+ "setAutoDownloadsStorageLimit:"
+ "setIsNetworkReachable:"
+ "setIsWifiEnabled:"
+ "setUseAutomaticDownloads:"
+ "shelfitemimage"
+ "shelfitemimagelive"
+ "shelfitemimagepost"
+ "timbuktu"
+ "useAutomaticDownloads"
- "%s"
- "-[WLKPlayActivityDecorateEBSOperation initWithChannelID:externalContentID:]"
- "-[WLKPlayActivityDecorateLiveOperation initWithChannelID:serviceID:]"
- "-[WLKPlayActivityDecorateVODOperation initWithExternalId:brandId:hlsAssetDuration:]"
- "@156@0:8@16@24@32@40@48@56@64@72@80q88@96q104B112@116@124q132B140B144@148"
- "ASDPurchase"
- "ASDPurchaseManager"
- "Unable to find class %s"
- "WLKPlayActivityDecorateVODOperation: CompoundId is nil. Cannot cache the metadata."
- "WLKPlayActivityDecorateVODOperation: WLKPlayActivityMetadata object is nil. Cannot cache it."
- "ams_activeiTunesAccount"
- "ams_iTunesAccountWithDSID:"
- "ams_localiTunesAccount"
- "ams_sharedAccountStore"
- "fromm"
- "initWithBundleID:timestamp:duration:elapsedTime:featureDuration:featureElapsedTime:externalProfileID:contentID:accountID:playbackState:playbackRate:completionState:isAlwaysLive:serviceID:currentPlaybackDate:playbackType:isTimerDerived:isFromActivePlayerPath:channelID:"
- "initWithChannelID:externalContentID:"
- "initWithChannelID:serviceID:"
- "initWithExternalId:brandId:hlsAssetDuration:"
- "softlink:r:path:/System/Library/PrivateFrameworks/AppStoreDaemon.framework/AppStoreDaemon"

```
