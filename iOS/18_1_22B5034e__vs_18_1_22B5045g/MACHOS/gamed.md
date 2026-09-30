## gamed

> `/usr/libexec/gamed`

```diff

-819.1.7.0.0
-  __TEXT.__text: 0x23f1e0
+819.1.12.0.0
+  __TEXT.__text: 0x24031c
   __TEXT.__auth_stubs: 0x2f00
-  __TEXT.__objc_stubs: 0x1b640
-  __TEXT.__objc_methlist: 0xc534
+  __TEXT.__objc_stubs: 0x1b6c0
+  __TEXT.__objc_methlist: 0xc564
   __TEXT.__const: 0x123a0
-  __TEXT.__objc_classname: 0x1eae
-  __TEXT.__oslogstring: 0x15cfb
-  __TEXT.__objc_methname: 0x23d35
-  __TEXT.__cstring: 0x1b86a
-  __TEXT.__objc_methtype: 0x6a5e
+  __TEXT.__objc_classname: 0x1eac
+  __TEXT.__oslogstring: 0x15edb
+  __TEXT.__objc_methname: 0x23e5b
+  __TEXT.__cstring: 0x1b91a
+  __TEXT.__objc_methtype: 0x6a51
   __TEXT.__gcc_except_tab: 0x3368
   __TEXT.__swift5_typeref: 0x1a62
-  __TEXT.__constg_swiftt: 0x1540
+  __TEXT.__constg_swiftt: 0x1550
   __TEXT.__swift5_reflstr: 0xc9a
   __TEXT.__swift5_fieldmd: 0x1184
   __TEXT.__swift5_builtin: 0x64

   __TEXT.__swift5_proto: 0x1f0
   __TEXT.__swift5_assocty: 0x60
   __TEXT.__swift5_mpenum: 0x1c
-  __TEXT.__unwind_info: 0x7770
+  __TEXT.__unwind_info: 0x7788
   __TEXT.__eh_frame: 0x6758
   __DATA_CONST.__auth_got: 0x1798
-  __DATA_CONST.__got: 0x1b00
-  __DATA_CONST.__auth_ptr: 0x6a0
-  __DATA_CONST.__const: 0x121c8
+  __DATA_CONST.__got: 0x1b08
+  __DATA_CONST.__auth_ptr: 0x680
+  __DATA_CONST.__const: 0x121f8
   __DATA_CONST.__cfstring: 0xcee0
   __DATA_CONST.__objc_classlist: 0x930
   __DATA_CONST.__objc_catlist: 0x138

   __DATA_CONST.__objc_arraydata: 0x478
   __DATA_CONST.__objc_dictobj: 0x280
   __DATA_CONST.__objc_arrayobj: 0x1b0
-  __DATA.__objc_const: 0x24190
-  __DATA.__objc_selrefs: 0x8240
-  __DATA.__objc_ivar: 0x808
-  __DATA.__objc_data: 0x68e0
+  __DATA.__objc_const: 0x241c0
+  __DATA.__objc_selrefs: 0x8278
+  __DATA.__objc_ivar: 0x80c
+  __DATA.__objc_data: 0x68f0
   __DATA.__data: 0x4b98
   __DATA.__bss: 0x3e88
   __DATA.__common: 0xe4

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 9993
-  Symbols:   1811
-  CStrings:  10941
+  Functions: 10002
+  Symbols:   1812
+  CStrings:  10958
 
Symbols:
+ _OBJC_CLASS_$_GKDaemonProxy
+ _$s20GameCenterFoundation02InA10BannerDataV0E4TypeOMa
+ _$s20GameCenterFoundation02InA10BannerDataV4type5title4body5imageA2C0E4TypeO_S2SSg0C00F0VSgtcfC
+ _$sSS10describingSSx_tclufC
+ _$s20GameCenterFoundation5GKLogO9friending2os6LoggerVvgZ
+ _$s20GameCenterFoundation02InA10BannerDataV4typeAC0E4TypeOvg
+ _$s20GameCenterFoundation02InA10BannerDataVMa
+ _$s20GameCenterFoundation02InA10BannerDataV6encode06bannerF00C00F0VSgAC_tFZ
+ _$s24GameCenterOverlayService20DashboardClientProxyC06showInA6Banner4data15sceneIdentifiery10Foundation4DataV_SSSgtF
+ _$s20GameCenterFoundation02InA10BannerDataV0E4TypeO18youBeatFriendScoreyAESS_SaySSGtcAEmFWC
+ _$s20GameCenterFoundation02InA10BannerDataV0E4TypeO7generalyA2EmFWC
- _$s24GameCenterOverlayService20DashboardClientProxyC18AccessPointUseCaseO02inA6BanneryA2EmFWC
- _$s20GameCenterFoundation21LeaderboardBannerDataV4typeAC0E4TypeOvg
- _$s24GameCenterOverlayService20DashboardClientProxyC06showInA6Banner7useCase5title7message9imageData10identifier15sceneIdentifieryAC014AccessPointUseL0O_S2SSg10Foundation0P0VSgA2MtF
- _$s20GameCenterFoundation21LeaderboardBannerDataV4type5title4body13leaderboardID9playerIDsA2C0E4TypeO_S3SSaySSGtcfC
- _$s24GameCenterOverlayService20DashboardClientProxyC18AccessPointUseCaseOMa
- _$s20GameCenterFoundation21LeaderboardBannerDataV0E4TypeO18youBeatFriendScoreyA2EmFWC
- _$s20GameCenterFoundation21LeaderboardBannerDataV6encode06bannerF00C00F0VSgAC_tFZ
- _$s20GameCenterFoundation21LeaderboardBannerDataV0E4TypeO8rawValueSSvg
- _$s20GameCenterFoundation21LeaderboardBannerDataVMa
- _$s20GameCenterFoundation21LeaderboardBannerDataV0E4TypeOMa
CStrings:
+ "FriendBulletin ignoreFriendRequest playerID not found"
+ "settings-navigation://com.apple.Settings.GameCenter/ALL_FRIENDS?id="
+ "friendServicePrivate"
+ "Vv32@0:8q16@?<v@?@\"NSArray\"@\"NSError\">24"
+ "sortDescriptorWithKey:ascending:selector:"
+ "T@\"NSString\",&,V_playerID"
+ "getNicknameSuggestions - server returned zero nickname suggestions"
+ "Failed to fetch profile with caid with error: %!@(MISSING)"
+ "caseInsensitiveCompare:"
+ "FriendBulletin ignoreFriendInvitation call to daemon failed with error: %!@(MISSING)"
+ "-[GKProfileServicePrivate getProfilesForPlayerIDs:playerIdToContactAssociationIdMap:handler:]"
+ "getNicknameSuggestions - server error: %!@(MISSING)"
+ "FriendBulletin acceptFriendInvitation call to daemon failed with error: %!@(MISSING)"
+ "isAddingFriendsRestricted"
+ "FriendBulletin acceptFriendRequest playerID not found"
+ "getProfilesForPlayerIDs:playerIdToContactAssociationIdMap:handler:"
+ "-[GKProfileServicePrivate getNicknameSuggestions:handler:]"
+ "LeaderboardBeatFriendScoreBulletin: InGameBannerData could not be encoded"
+ "proxyForLocalPlayer"
+ "issuing-player-caid"
+ "getNicknameSuggestions:handler:"
+ "emitMultiplayerEvent: InGameBannerData could not be encoded"
+ "populateContactInfoForProfiles:playerIdToContactAssociationIdMap:withContext:"
+ "_playerID"
+ "settings-navigation://com.apple.Settings.GameCenter/FRIEND_REQUESTS?id="
- "settings-navigation://com.apple.Settings.GameCenter/ALL_FRIENDS"
- "$"
- "getSuggestionsForNickname - server error: %!@(MISSING)"
- "getSuggestionsForNickname - server returned zero nickname suggestions"
- "Vv40@0:8@\"NSString\"16q24@?<v@?@\"NSArray\"@\"NSError\">32"
- "Skeezix"
- "getSuggestionsForNickname:suggestionsCount:handler:"
- "-[GKProfileServicePrivate getSuggestionsForNickname:suggestionsCount:handler:]"

```
