## watchlistd

> `/System/Library/PrivateFrameworks/WatchListKit.framework/Support/watchlistd`

```diff

-800.10.14.0.0
-  __TEXT.__text: 0x26eb4
-  __TEXT.__auth_stubs: 0x960
-  __TEXT.__objc_stubs: 0x5020
+800.20.10.0.0
+  __TEXT.__text: 0x271e0
+  __TEXT.__auth_stubs: 0x940
+  __TEXT.__objc_stubs: 0x5060
   __TEXT.__objc_methlist: 0x21f4
-  __TEXT.__cstring: 0x44f2
+  __TEXT.__cstring: 0x4575
   __TEXT.__oslogstring: 0x2434
   __TEXT.__objc_classname: 0x486
-  __TEXT.__objc_methname: 0x5e95
-  __TEXT.__objc_methtype: 0xf44
-  __TEXT.__const: 0x68
-  __TEXT.__gcc_except_tab: 0xba0
+  __TEXT.__objc_methname: 0x5ec7
+  __TEXT.__objc_methtype: 0xf2c
+  __TEXT.__const: 0xf0
+  __TEXT.__gcc_except_tab: 0xbac
   __TEXT.__dlopen_cstrs: 0x5a
-  __TEXT.__unwind_info: 0xb10
-  __DATA_CONST.__auth_got: 0x4c0
+  __TEXT.__unwind_info: 0xb24
+  __DATA_CONST.__auth_got: 0x4b0
   __DATA_CONST.__got: 0x258
-  __DATA_CONST.__const: 0x1308
-  __DATA_CONST.__cfstring: 0x3a00
+  __DATA_CONST.__const: 0x1360
+  __DATA_CONST.__cfstring: 0x3a80
   __DATA_CONST.__objc_classlist: 0x118
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_intobj: 0x60
   __DATA.__objc_const: 0x54d0
-  __DATA.__objc_selrefs: 0x1a98
+  __DATA.__objc_selrefs: 0x1aa8
   __DATA.__objc_protorefs: 0x10
-  __DATA.__objc_classrefs: 0x3d0
+  __DATA.__objc_classrefs: 0x3d8
   __DATA.__objc_superrefs: 0xf0
   __DATA.__objc_ivar: 0x284
   __DATA.__objc_data: 0xaf0

   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
+  - /System/Library/PrivateFrameworks/TVAppServices.framework/TVAppServices
   - /System/Library/PrivateFrameworks/UserManagement.framework/UserManagement
   - /System/Library/PrivateFrameworks/WatchListKit.framework/WatchListKit
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 69679E25-2B50-37FE-99FC-1EE2E4013B26
-  Functions: 883
-  Symbols:   2649
-  CStrings:  2427
+  UUID: 49FFAA71-632F-3A8A-A08B-28C84081F786
+  Functions: 888
+  Symbols:   2654
+  CStrings:  2436
 
Symbols:
+ -[WLDPlaybackManager _promptForBundleID:completionHandler:]
+ GCC_except_table47
+ GCC_except_table60
+ _OBJC_CLASS_$_SportsFavoriteServiceObjC
+ __46-[WLDSportsLiveActivityPushHandler connection]_block_invoke.57
+ __66-[WLDPushNotificationController _loadURLBagWithCompletionHandler:]_block_invoke.192
+ ___59-[WLDPlaybackManager _promptForBundleID:completionHandler:]_block_invoke
+ ___66-[WLDPlaybackManager _enqueuePlaybackSummary:sessionID:serialize:]_block_invoke_5
+ ___block_descriptor_56_e8_32s40s48s_e8_v12?0B8ls32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48s56bs_e5_v8?0ls32l8s40l8s48l8s56l8
+ ___block_descriptor_80_e8_32s40s48s56s64s72w_e20_v20?0B8"NSError"12lw72l8s32l8s40l8s48l8s56l8s64l8
+ __block_literal_global.44
+ __block_literal_global.47
+ _objc_msgSend$_promptForBundleID:completionHandler:
+ _objc_msgSend$createActivityWithCanonicalId:supplementaryData:completion:
+ _objc_msgSend$markCacheTopicDirty:
+ _objc_msgSend$refreshWithCompletion:
- -[WLDPlaybackManager _promptForBundleID:]
- GCC_except_table56
- _CFNumberGetTypeID
- _CFNumberGetValue
- __46-[WLDSportsLiveActivityPushHandler connection]_block_invoke.54
- __66-[WLDPushNotificationController _loadURLBagWithCompletionHandler:]_block_invoke.186
- ___block_descriptor_72_e8_32s40s48s56s64w_e20_v20?0B8"NSError"12lw64l8s32l8s40l8s48l8s56l8
- __block_literal_global.37
- __block_literal_global.40
- _objc_msgSend$_promptForBundleID:
- _objc_msgSend$createActivityWithCanonicalId:supplementaryData:userInitiated:completion:
CStrings:
+ "Favorite Leagues Changed"
+ "Favorite Syncing User Consent Changed"
+ "Favorite Teams Changed"
+ "LiveActivityAutostart"
+ "_promptForBundleID:completionHandler:"
+ "actionId"
+ "createActivityWithCanonicalId:supplementaryData:completion:"
+ "favoriteLeaguesChanges"
+ "gameStartWithScore"
+ "id"
+ "liveActivityAutostart"
+ "liveActivityAutostartAction"
+ "liveActivityAutostartEnabled"
+ "markCacheTopicDirty:"
+ "refreshWithCompletion:"
+ "sports_live_activities_autostart"
+ "v40@0:8@\"NSString\"16@\"NSDictionary\"24@?<v@?@\"NSError\">32"
- "BatteryCurrentCapacity"
- "Favorite Sync Setting"
- "Favorite Teams"
- "_promptForBundleID:"
- "createActivityWithCanonicalId:supplementaryData:userInitiated:completion:"
- "editorial"
- "excitingGame"
- "notificationText"
- "overtimeGame"
- "sports_auto_liveactivities_v3"
- "v44@0:8@\"NSString\"16@\"NSDictionary\"24B32@?<v@?@\"NSError\">36"
- "v44@0:8@16@24B32@?36"

```
