## watchlistd

> `/System/Library/PrivateFrameworks/WatchListKit.framework/Support/watchlistd`

```diff

-850.50.2.0.0
-  __TEXT.__text: 0x27928
-  __TEXT.__auth_stubs: 0x950
-  __TEXT.__objc_stubs: 0x5160
-  __TEXT.__objc_methlist: 0x264c
-  __TEXT.__cstring: 0x46e4
-  __TEXT.__oslogstring: 0x2497
+902.0.0.0.0
+  __TEXT.__text: 0x28354
+  __TEXT.__auth_stubs: 0x920
+  __TEXT.__objc_stubs: 0x51e0
+  __TEXT.__objc_methlist: 0x265c
+  __TEXT.__cstring: 0x48bf
+  __TEXT.__oslogstring: 0x2602
   __TEXT.__objc_classname: 0x497
   __TEXT.__objc_methtype: 0xf79
-  __TEXT.__objc_methname: 0x5ecd
-  __TEXT.__const: 0x128
-  __TEXT.__gcc_except_tab: 0xedc
-  __TEXT.__dlopen_cstrs: 0x5a
-  __TEXT.__unwind_info: 0xb50
-  __DATA_CONST.__auth_got: 0x4b8
-  __DATA_CONST.__got: 0x558
-  __DATA_CONST.__const: 0x1398
-  __DATA_CONST.__cfstring: 0x3bc0
+  __TEXT.__objc_methname: 0x5f2a
+  __TEXT.__const: 0x130
+  __TEXT.__gcc_except_tab: 0xf00
+  __TEXT.__unwind_info: 0xb58
+  __DATA_CONST.__auth_got: 0x4a0
+  __DATA_CONST.__got: 0x538
+  __DATA_CONST.__const: 0x1320
+  __DATA_CONST.__cfstring: 0x3d00
   __DATA_CONST.__objc_classlist: 0x120
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x60

   __DATA_CONST.__objc_superrefs: 0xf0
   __DATA_CONST.__objc_intobj: 0x60
   __DATA.__objc_const: 0x4df0
-  __DATA.__objc_selrefs: 0x1bc0
+  __DATA.__objc_selrefs: 0x1be8
   __DATA.__objc_ivar: 0x27c
   __DATA.__objc_data: 0xb40
   __DATA.__data: 0x510
-  __DATA.__bss: 0xf8
+  __DATA.__bss: 0xe8
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /System/Library/PrivateFrameworks/PromotedContentSupport.framework/PromotedContentSupport
   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/ProtocolBuffer
   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
-  - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
+  - /System/Library/PrivateFrameworks/SetupAssistant.framework/SetupAssistant
   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
   - /System/Library/PrivateFrameworks/TVAppServices.framework/TVAppServices
   - /System/Library/PrivateFrameworks/UserManagement.framework/UserManagement

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 12BD004B-9B1C-3A01-8E84-D10E7D24C31E
-  Functions: 897
-  Symbols:   2694
-  CStrings:  2453
+  UUID: D315DB24-334F-3902-8C67-7097B03BD3D8
+  Functions: 896
+  Symbols:   2684
+  CStrings:  2479
 
Symbols:
+ -[WLDServer _supportPath]
+ _BYSetupAssistantNeedsToRun
+ _OBJC_CLASS_$_TVAppAccountStoreObjC
+ _TVASDefaultSupportPath
+ __block_literal_global.293
+ __block_literal_global.331
+ __block_literal_global.50
+ __block_literal_global.53
+ _objc_msgSend$_setError
+ _objc_msgSend$accountWithDSID:
+ _objc_msgSend$contentTitle
+ _objc_msgSend$getBytes:range:
+ _objc_msgSend$hasError
+ _objc_msgSend$initWithChannelID:externalContentID:playablePassthrough:
+ _objc_msgSend$initWithChannelID:serviceID:playablePassthrough:
+ _objc_msgSend$initWithExternalId:brandId:hlsAssetDuration:playablePassthrough:
+ _objc_msgSend$playablePassthrough
+ _objc_msgSend$position
+ _objc_msgSend$setPosition:
- OBJC_IVAR_$_PBDataReader._bytes
- OBJC_IVAR_$_PBDataReader._error
- OBJC_IVAR_$_PBDataReader._length
- OBJC_IVAR_$_PBDataReader._pos
- SetupAssistantLibraryCore.frameworkLibrary
- _OBJC_CLASS_$_ACAccountStore
- ___SetupAssistantLibraryCore_block_invoke
- ___block_descriptor_40_e5_v8?0l
- ___block_descriptor_40_e8_32r_e5_v8?0lr32l8
- ___getBYSetupAssistantNeedsToRunSymbolLoc_block_invoke
- __block_literal_global.278
- __block_literal_global.316
- __block_literal_global.44
- __block_literal_global.47
- __sl_dlopen
- _abort_report_np
- _audit_stringSetupAssistant
- _dlerror
- _dlsym
- _free
- _objc_msgSend$ams_activeiTunesAccount
- _objc_msgSend$ams_iTunesAccountWithDSID:
- _objc_msgSend$ams_sharedAccountStore
- _objc_msgSend$handleAMSDeviceOffer
- _objc_msgSend$initWithChannelID:externalContentID:
- _objc_msgSend$initWithChannelID:serviceID:
- _objc_msgSend$initWithExternalId:brandId:hlsAssetDuration:
- getBYSetupAssistantNeedsToRunSymbolLoc.ptr
CStrings:
+ "Favorite Events Changed"
+ "User did not consent to channel with ID %@"
+ "WLDPlaybackManager: Canonical id is not cached. Error:%@"
+ "WLDPlaybackManager: User did not consent to Channel with ID %@. Ignoring report."
+ "WLDPlaybackManager: _handleReporting failed with error: %@"
+ "WLDPlaybackManager: _offlineValidation failed"
+ "WLDPlaybackManager: online validation failed with error: %@"
+ "WLDPlaybackManager: retrieved (%@) decorated summaries"
+ "WLDPlaybackNowPlayingObserver - WLDPlaybackNowPlayingObserver: _fetchActivePlayerPaths filtered paths count: %lu"
+ "WLDPlaybackNowPlayingObserver - WLDPlaybackNowPlayingObserver: _nowPlayingInfoForPlayerPath invalid player path"
+ "WLDPlaybackNowPlayingObserver - WLDPlaybackNowPlayingObserver: _nowPlayingInfoForPlayerPath summary is nil, activePlayingInfo is not set."
+ "WLDServer - Error: TVASDefaultSupportPath returned nil"
+ "WLDServer - Failed to archive app library dictionary data: %@"
+ "WLDServer - Failed to write app library dictionary data."
+ "_setError"
+ "accountWithDSID:"
+ "applibrarydict"
+ "contentTitle"
+ "favoriteSportingEventsChanges"
+ "getBytes:range:"
+ "hasError"
+ "initWithChannelID:externalContentID:playablePassthrough:"
+ "initWithChannelID:serviceID:playablePassthrough:"
+ "initWithExternalId:brandId:hlsAssetDuration:playablePassthrough:"
+ "playablePassthrough"
+ "position"
+ "setPosition:"
+ "timbuktu"
- "%s"
- "BYSetupAssistantNeedsToRun"
- "WLDPlaybackManager: Canonical id is not cached"
- "WLDPlaybackManager: begin decorating (%@) summaries"
- "ams_activeiTunesAccount"
- "ams_iTunesAccountWithDSID:"
- "ams_sharedAccountStore"
- "com.apple.AppleMediaServices.deviceOffersChanged"
- "initWithChannelID:externalContentID:"
- "initWithChannelID:serviceID:"
- "initWithExternalId:brandId:hlsAssetDuration:"
- "softlink:r:path:/System/Library/PrivateFrameworks/SetupAssistant.framework/SetupAssistant"

```
