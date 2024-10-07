## gamed

> `/usr/libexec/gamed`

```diff

-819.1.17.0.0
-  __TEXT.__text: 0x240f1c
+819.1.22.2.3
+  __TEXT.__text: 0x242070
   __TEXT.__auth_stubs: 0x2f00
-  __TEXT.__objc_stubs: 0x1b6e0
-  __TEXT.__objc_methlist: 0xc56c
+  __TEXT.__objc_stubs: 0x1b7c0
+  __TEXT.__objc_methlist: 0xc594
   __TEXT.__const: 0x123a0
   __TEXT.__objc_classname: 0x1eac
-  __TEXT.__oslogstring: 0x1606b
-  __TEXT.__objc_methname: 0x23ea2
+  __TEXT.__oslogstring: 0x1638b
+  __TEXT.__objc_methname: 0x2404c
   __TEXT.__cstring: 0x1b93a
   __TEXT.__objc_methtype: 0x6a51
   __TEXT.__gcc_except_tab: 0x33b0

   __TEXT.__swift5_proto: 0x1f0
   __TEXT.__swift5_assocty: 0x60
   __TEXT.__swift5_mpenum: 0x1c
-  __TEXT.__unwind_info: 0x77a8
+  __TEXT.__unwind_info: 0x77b8
   __TEXT.__eh_frame: 0x6758
   __DATA_CONST.__auth_got: 0x1798
-  __DATA_CONST.__got: 0x1b08
-  __DATA_CONST.__auth_ptr: 0x6a0
-  __DATA_CONST.__const: 0x12218
-  __DATA_CONST.__cfstring: 0xcf00
+  __DATA_CONST.__got: 0x1b20
+  __DATA_CONST.__auth_ptr: 0x698
+  __DATA_CONST.__const: 0x12298
+  __DATA_CONST.__cfstring: 0xcf20
   __DATA_CONST.__objc_classlist: 0x930
   __DATA_CONST.__objc_catlist: 0x138
   __DATA_CONST.__objc_protolist: 0x228

   __DATA_CONST.__objc_protorefs: 0x60
   __DATA_CONST.__objc_superrefs: 0x528
   __DATA_CONST.__objc_intobj: 0x9f0
-  __DATA_CONST.__objc_arraydata: 0x478
+  __DATA_CONST.__objc_arraydata: 0x3f0
   __DATA_CONST.__objc_dictobj: 0x280
-  __DATA_CONST.__objc_arrayobj: 0x1b0
-  __DATA.__objc_const: 0x241e0
-  __DATA.__objc_selrefs: 0x8288
-  __DATA.__objc_ivar: 0x80c
+  __DATA_CONST.__objc_arrayobj: 0x198
+  __DATA.__objc_const: 0x24230
+  __DATA.__objc_selrefs: 0x82d0
+  __DATA.__objc_ivar: 0x810
   __DATA.__objc_data: 0x68f0
   __DATA.__data: 0x4b98
   __DATA.__bss: 0x3e88

   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
+  - /usr/lib/swift/libswiftCryptoTokenKit.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 10005
-  Symbols:   1812
-  CStrings:  10968
+  Functions: 10018
+  Symbols:   1816
+  CStrings:  10998
 
Symbols:
+ _$s20GameCenterFoundation02InA10BannerDataV0E4TypeO26topPercentageOnLeaderboardyAESS_tcAEmFWC
+ _GKFriendRequestURLSenderPlayerID
+ _GKFriendRequestsBannerPercentAllowed
+ _OBJC_CLASS_$_GKFriendInviteActivityEvent
+ __swift_FORCE_LOAD_$_swiftCryptoTokenKit
- _GKFriendRequestsBannerDisabled
CStrings:
+ "B16@?0@\"GKLocalPlayer\"8"
+ "Failed to accept a friend invitation: %!@(MISSING)"
+ "Failed to ignore a friend invitation: %!@(MISSING)"
+ "Failed to preemptively flush friend invitation mailbox, error: %!@(MISSING)"
+ "Failed while sending friend invitation via push: %!@(MISSING)"
+ "Fetching primary player."
+ "Friend requests banner dice roll: %!@(MISSING), bag value: %!@(MISSING)"
+ "GKAMPController: Reporting inviteActivity stage %!@(MISSING)"
+ "Not displaying notification because notifications are not authorized"
+ "T@\"NSString\",R,N,GgetRelationshipPlayerImage"
+ "T@\"NSString\",R,N,GgetRelationshipPlayerName"
+ "TB,R,N,V_supportsNearbyAdvertising"
+ "[%!@(MISSING)]Current game not supporting nearby advertising."
+ "[%!@(MISSING)]Current game supports nearby advertising."
+ "_gkIsKnownFirstParty"
+ "_gkIsPreferences"
+ "_supportsNearbyAdvertising"
+ "authorizationStatus"
+ "avatarUrl"
+ "getRelationshipPlayerImage"
+ "getRelationshipPlayerName"
+ "metricsFieldsForStage:hostApp:"
+ "notificationSettings"
+ "relationshipPlayerImage"
+ "relationshipPlayerName"
+ "reportFriendInviteActivityEventAtStage:hostApp:"
+ "setLastPrivacyNoticeVersionDisplayedForSignedInPlayer: Skipped because the current value has been overridden for testing."
+ "setLastPrivacyNoticeVersionDisplayedForSignedInPlayer: Skipped because the values of current and new are the same."
+ "setLastPrivacyNoticeVersionDisplayedForSignedInPlayer: The value is set to %!@(MISSING)"
+ "stringForStage:"
+ "supportsNearbyAdvertising"
+ "updatedNotificationCategoriesOrNil:"
+ "|"
- "currentGameSupportsMultiplayer"
- "gk-get-friend-invitation-mailbox"
- "updateNotificationCategories:"

```
