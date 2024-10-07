## GameCenterFoundation

> `/System/Library/PrivateFrameworks/GameCenterFoundation.framework/GameCenterFoundation`

```diff

-819.1.17.0.0
-  __TEXT.__text: 0x15e0dc
+819.1.22.2.3
+  __TEXT.__text: 0x15fba8
   __TEXT.__auth_stubs: 0x2630
-  __TEXT.__objc_methlist: 0xf958
-  __TEXT.__cstring: 0x18e53
-  __TEXT.__const: 0x43a8
+  __TEXT.__objc_methlist: 0xf9b0
+  __TEXT.__cstring: 0x19033
+  __TEXT.__const: 0x4698
   __TEXT.__gcc_except_tab: 0x1418
-  __TEXT.__oslogstring: 0xcddb
+  __TEXT.__oslogstring: 0xcf4b
   __TEXT.__ustring: 0x18
   __TEXT.__dlopen_cstrs: 0xba
-  __TEXT.__swift5_typeref: 0x1b80
+  __TEXT.__swift5_typeref: 0x1c18
   __TEXT.__swift5_capture: 0x788
-  __TEXT.__swift5_fieldmd: 0x11f0
-  __TEXT.__constg_swiftt: 0x1430
-  __TEXT.__swift5_reflstr: 0xc93
+  __TEXT.__swift5_fieldmd: 0x1264
+  __TEXT.__constg_swiftt: 0x1484
+  __TEXT.__swift5_reflstr: 0xce3
   __TEXT.__swift5_builtin: 0xdc
   __TEXT.__swift5_assocty: 0x228
   __TEXT.__swift5_protos: 0x24
-  __TEXT.__swift5_proto: 0x3d4
-  __TEXT.__swift5_types: 0x16c
+  __TEXT.__swift5_proto: 0x3e8
+  __TEXT.__swift5_types: 0x174
   __TEXT.__swift5_mpenum: 0x48
-  __TEXT.__unwind_info: 0x6030
+  __TEXT.__unwind_info: 0x60a0
   __TEXT.__eh_frame: 0x4ea0
   __TEXT.__objc_classname: 0x1d75
-  __TEXT.__objc_methname: 0x24b54
+  __TEXT.__objc_methname: 0x24c1b
   __TEXT.__objc_methtype: 0x63ad
-  __TEXT.__objc_stubs: 0x149a0
-  __DATA_CONST.__got: 0x1050
-  __DATA_CONST.__const: 0x5ed8
-  __DATA_CONST.__objc_classlist: 0x7a8
+  __TEXT.__objc_stubs: 0x14a20
+  __DATA_CONST.__got: 0x1058
+  __DATA_CONST.__const: 0x5ef8
+  __DATA_CONST.__objc_classlist: 0x7b0
   __DATA_CONST.__objc_catlist: 0xe8
   __DATA_CONST.__objc_protolist: 0x218
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x7940
+  __DATA_CONST.__objc_selrefs: 0x7960
   __DATA_CONST.__objc_protorefs: 0x128
   __DATA_CONST.__objc_superrefs: 0x4d0
   __DATA_CONST.__objc_arraydata: 0x280
   __AUTH_CONST.__auth_got: 0x1328
-  __AUTH_CONST.__auth_ptr: 0x640
-  __AUTH_CONST.__const: 0x4b60
-  __AUTH_CONST.__cfstring: 0x109c0
-  __AUTH_CONST.__objc_const: 0x26448
+  __AUTH_CONST.__auth_ptr: 0x600
+  __AUTH_CONST.__const: 0x4c78
+  __AUTH_CONST.__cfstring: 0x109e0
+  __AUTH_CONST.__objc_const: 0x264a0
   __AUTH_CONST.__objc_arrayobj: 0x150
   __AUTH_CONST.__objc_intobj: 0x258
   __AUTH_CONST.__objc_dictobj: 0x140
-  __AUTH.__objc_data: 0x2dd8
-  __AUTH.__data: 0xe80
+  __AUTH.__objc_data: 0x2e48
+  __AUTH.__data: 0xea0
   __DATA.__objc_ivar: 0xefc
-  __DATA.__data: 0x3c58
-  __DATA.__bss: 0x7d90
-  __DATA.__common: 0x20
+  __DATA.__data: 0x3cc8
+  __DATA.__bss: 0x8050
+  __DATA.__common: 0x28
   __DATA_DIRTY.__objc_data: 0x24b8
   __DATA_DIRTY.__data: 0x368
   __DATA_DIRTY.__common: 0xa8
-  __DATA_DIRTY.__bss: 0x598
+  __DATA_DIRTY.__bss: 0x558
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/Combine.framework/Combine
   - /System/Library/Frameworks/Contacts.framework/Contacts

   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
+  - /usr/lib/swift/libswiftCryptoTokenKit.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIntents.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 9998
-  Symbols:   9114
-  CStrings:  10880
+  Functions: 10044
+  Symbols:   9124
+  CStrings:  10899
 
Symbols:
+ _GKFriendRequestURLRequestState
+ _GKFriendRequestURLSenderPlayerID
+ _GKFriendRequestURLVersionNumber
+ _GKFriendRequestsBannerPercentAllowed
+ _OBJC_CLASS_$_GKFriendInviteActivityEvent
+ _OBJC_METACLASS_$_GKFriendInviteActivityEvent
+ __swift_FORCE_LOAD_$_swiftCryptoTokenKit
+ _os_log_GKReactions
- _GKFriendRequestsBannerDisabled
CStrings:
+ "@32@0:8Q16@24"
+ "FriendInviteActivityEvent: Expected a hostApp as we're in a sent stage, but no hostApp was provided. Stage: %!s(MISSING)"
+ "GKAPIReporter: Recording inviteActivity stage %!@(MISSING)"
+ "GKFriendInviteActivityEvent"
+ "Reactions"
+ "TB,R,D,N,GisFriendInvitationInContacts"
+ "Unknown stage encountered when trying to build metrics fields for inviteActivity stage %!s(MISSING), bailing"
+ "_gkIsGameDaemon"
+ "_gkIsKnownFirstParty"
+ "friendInvitationInContacts"
+ "gk-friend-requests-banner-percent-allowed"
+ "isFriendInvitationInContacts"
+ "metricsFieldsForStage:hostApp:"
+ "receivedResponse"
+ "recordFriendInviteActivityEventAtStage:hostApp:"
+ "sentResponseAccepted"
+ "sentResponseIgnored"
+ "shouldShowAnyOnboardingScreen? %!@(MISSING) (Show if the user has not seen the most recent Welcome/WhatsNew copy on this device, Seen:%!@(MISSING) VS Current:%!d(MISSING))"
+ "shouldShowAnyOnboardingScreen? YES (At least one of the onboarding conditions have to be completed)"
+ "shouldShowAnyOnboardingScreen? needConsentGDPR=%!d(MISSING) || needPersonalization=%!d(MISSING) || needProfilePrivacy=%!d(MISSING) || needFriendSuggestions=%!d(MISSING) || needContactsIntegrationConsent=%!d(MISSING)"
+ "stringForStage:"
+ "topPercentageOnLeaderboard"
+ "{\n\t\tlastWelcomeWhatsNewCopyVersionDisplayed: %!@(MISSING)\n\t\tlastPrivacyNoticeVersionDisplayed: %!@(MISSING)\n\t\tlastPersonalizationVersionDisplayed: %!@(MISSING)\n\t\tlastProfilePrivacyVersionDisplayed: %!@(MISSING)\n\t\tlastFriendSuggestionsVersionDisplayed: %!@(MISSING)\n\t\tlastContactsIntegrationConsentVersionDisplayed: %!@(MISSING)\n}"
- "_gkIsDaemon"
- "_gkIsFirstParty"
- "gk-friend-requests-banner-disabled"
- "shouldShowAnyOnboardingScreen? %!@(MISSING), lastWelcomeWhatsNewCopyVersionDisplayed=%!@(MISSING) must be less than GKOnboardingWelcomeWhatsNewCopyVersion=%!d(MISSING)"
- "shouldShowAnyOnboardingScreen? %!@(MISSING), needConsentGDPR=%!d(MISSING) || needPersonalization=%!d(MISSING) ||needProfilePrivacy=%!d(MISSING) || needFriendSuggestions=%!d(MISSING) || needContactsIntegrationConsent=%!d(MISSING)"

```
