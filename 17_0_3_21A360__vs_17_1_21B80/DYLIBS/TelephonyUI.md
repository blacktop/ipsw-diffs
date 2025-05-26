## TelephonyUI

> `/System/Library/PrivateFrameworks/TelephonyUI.framework/TelephonyUI`

```diff

-1430.100.1.2.10
-  __TEXT.__text: 0x395d4
-  __TEXT.__auth_stubs: 0x1280
-  __TEXT.__objc_methlist: 0x3350
-  __TEXT.__const: 0x11bc
-  __TEXT.__gcc_except_tab: 0x188
-  __TEXT.__cstring: 0x23f1
-  __TEXT.__dlopen_cstrs: 0x15e
+1430.200.61.0.0
+  __TEXT.__text: 0x3c63c
+  __TEXT.__auth_stubs: 0x12f0
+  __TEXT.__objc_methlist: 0x3498
+  __TEXT.__const: 0x127c
+  __TEXT.__gcc_except_tab: 0x1a0
+  __TEXT.__cstring: 0x2591
+  __TEXT.__dlopen_cstrs: 0x1a9
   __TEXT.__oslogstring: 0x62c
   __TEXT.__ustring: 0x208
-  __TEXT.__swift5_typeref: 0x4af
-  __TEXT.__constg_swiftt: 0x708
+  __TEXT.__swift5_typeref: 0x505
+  __TEXT.__constg_swiftt: 0x724
   __TEXT.__swift5_reflstr: 0x466
-  __TEXT.__swift5_fieldmd: 0x498
+  __TEXT.__swift5_fieldmd: 0x4a8
   __TEXT.__swift5_protos: 0x8
-  __TEXT.__swift5_proto: 0x6c
-  __TEXT.__swift5_types: 0x58
+  __TEXT.__swift5_proto: 0x74
+  __TEXT.__swift5_types: 0x5c
   __TEXT.__swift5_capture: 0x50
   __TEXT.__swift5_builtin: 0x28
-  __TEXT.__swift5_assocty: 0x108
-  __TEXT.__unwind_info: 0x11f8
+  __TEXT.__swift5_assocty: 0x120
+  __TEXT.__unwind_info: 0x12dc
   __TEXT.__eh_frame: 0xe0
   __TEXT.__objc_classname: 0x4f7
-  __TEXT.__objc_methname: 0xa4b3
-  __TEXT.__objc_methtype: 0x1101
-  __TEXT.__objc_stubs: 0x8160
-  __DATA_CONST.__got: 0x3c8
-  __DATA_CONST.__const: 0x7a8
+  __TEXT.__objc_methname: 0xa8f7
+  __TEXT.__objc_methtype: 0x10e0
+  __TEXT.__objc_stubs: 0x8560
+  __DATA_CONST.__got: 0x3e8
+  __DATA_CONST.__const: 0x7d0
   __DATA_CONST.__objc_classlist: 0x1c0
   __DATA_CONST.__objc_catlist: 0x68
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x53e8
-  __DATA_CONST.__objc_selrefs: 0x2b50
+  __DATA_CONST.__objc_const: 0x5448
+  __DATA_CONST.__objc_selrefs: 0x2c68
   __DATA_CONST.__objc_arraydata: 0x60
   __AUTH_CONST.__cfstring: 0x1fe0
   __AUTH_CONST.__objc_const: 0x18a0
-  __AUTH_CONST.__const: 0xa50
+  __AUTH_CONST.__const: 0xa90
   __AUTH_CONST.__objc_intobj: 0x120
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH_CONST.__objc_floatobj: 0x20
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__auth_ptr: 0x50
-  __AUTH_CONST.__auth_got: 0x950
+  __AUTH_CONST.__auth_got: 0x988
   __AUTH.__objc_data: 0x1048
   __AUTH.__data: 0x3a0
   __DATA.__objc_protorefs: 0x8
   __DATA.__objc_classrefs: 0x418
   __DATA.__objc_superrefs: 0x118
-  __DATA.__objc_ivar: 0x31c
-  __DATA.__data: 0xe88
-  __DATA.__bss: 0xae0
+  __DATA.__objc_ivar: 0x324
+  __DATA.__data: 0xfe0
+  __DATA.__bss: 0xb50
   __DATA_DIRTY.__objc_data: 0x550
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox
   - /System/Library/Frameworks/Contacts.framework/Contacts

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1896
-  Symbols:   4910
-  CStrings:  2421
+  Functions: 1988
+  Symbols:   5022
+  CStrings:  2469
 
Symbols:
+ +[TPIncomingCallMetricsProvider callDetailsButtonMaxSize]
+ +[TPIncomingCallMetricsProvider callDetailsButtonPaddingPercentTop_ForSnapshot]
+ +[TPIncomingCallMetricsProvider callDetailsButtonPaddingTopPercent_DynamicIsland]
+ +[TPIncomingCallMetricsProvider callDetailsButtonPaddingTopPercent_HomeButton]
+ +[TPIncomingCallMetricsProvider callDetailsButtonPaddingTopPercent_Notch]
+ +[TPIncomingCallMetricsProvider callDetailsButtonPaddingTop_ForSnapshot]
+ +[TPIncomingCallMetricsProvider callDetailsButtonPaddingTrailPercent_ForSnapshot]
+ +[TPIncomingCallMetricsProvider callDetailsButtonPaddingTrail_ForSnapshot]
+ +[TPIncomingCallMetricsProvider callDetailsButtonPaddingTrailingPercent_DynamicIsland]
+ +[TPIncomingCallMetricsProvider callDetailsButtonPaddingTrailingPercent_HomeButton]
+ +[TPIncomingCallMetricsProvider callDetailsButtonPaddingTrailingPercent_Notch]
+ +[TPIncomingCallMetricsProvider deviceHasHomeButton]
+ +[TPIncomingCallMetricsProvider fullDeviceBounds]
+ +[TPIncomingCallMetricsProvider fullDeviceHeight]
+ +[TPIncomingCallMetricsProvider fullDeviceWidth]
+ +[TPIncomingCallMetricsProvider incomingCallAndInCallControlsBottomPadding]
+ +[TPIncomingCallMetricsProvider nameLabelFontWithAvatar]
+ +[TPIncomingCallMetricsProvider posterBadgeMaxSize]
+ +[TPIncomingCallMetricsProvider twelvePercentOfDeviceHeight]
+ -[TPInComingCallUISnapshotViewController avatarView]
+ -[TPInComingCallUISnapshotViewController capCallDetailsViewButtonSize]
+ -[TPInComingCallUISnapshotViewController customAvatar]
+ -[TPInComingCallUISnapshotViewController initWithConfiguration:style:contact:avatarImage:]
+ -[TPInComingCallUISnapshotViewController initWithConfiguration:style:nameString:avatarImage:]
+ -[TPInComingCallUISnapshotViewController moveMobileLabelToBeYAxisCenteredWithInfoButton]
+ -[TPInComingCallUISnapshotViewController setAvatarView:]
+ -[TPInComingCallUISnapshotViewController setBackroundColor:]
+ -[TPInComingCallUISnapshotViewController setCustomAvatar:]
+ -[TPInComingCallUISnapshotViewController setLabelsColor:]
+ -[TPInComingCallUISnapshotViewController setupAvatarViewIfNeeded]
+ -[UIFont(TelephonyUI) withCaseSensitiveAttribute]
+ GCC_except_table11
+ GCC_except_table30
+ _ContactsUILibraryCore.frameworkLibrary
+ _OBJC_IVAR_$_TPInComingCallUISnapshotViewController._avatarView
+ _OBJC_IVAR_$_TPInComingCallUISnapshotViewController._customAvatar
+ _TUActionLiveVoicemailSettings
+ _TUCallScreeningDisabledUserDefault
+ _TUTipsEventCallScreened
+ _UIAccessibilityIsReduceTransparencyEnabled
+ _UIContentSizeCategorySmall
+ ___52+[TPIncomingCallMetricsProvider deviceHasHomeButton]_block_invoke
+ ___ContactsUILibraryCore_block_invoke
+ ___getCNImageDerivedColorGeneratorClass_block_invoke
+ ___getCNImageDerivedColorGeneratorClass_block_invoke.cold.1
+ ___getCNImageDerivedColorGeneratorClass_block_invoke.cold.2
+ _associated conformance 11TelephonyUI16LiveVoicemailTipV8TipsNext0E0AAs12Identifiable
+ _associated conformance 11TelephonyUI16LiveVoicemailTipVs12IdentifiableAA2IDsADP_SH
+ _audit_stringContactsUI
+ _deviceHasHomeButton.homeButtonType
+ _deviceHasHomeButton.onceToken
+ _getCNImageDerivedColorGeneratorClass.softClass
+ _objc_msgSend$_colorBlendedWithColor:
+ _objc_msgSend$_colorDifferenceFromColor:
+ _objc_msgSend$avatarView
+ _objc_msgSend$callDetailsButtonMaxSize
+ _objc_msgSend$callDetailsButtonPaddingPercentTop_ForSnapshot
+ _objc_msgSend$callDetailsButtonPaddingTopPercent_DynamicIsland
+ _objc_msgSend$callDetailsButtonPaddingTopPercent_HomeButton
+ _objc_msgSend$callDetailsButtonPaddingTop_ForSnapshot
+ _objc_msgSend$callDetailsButtonPaddingTrailPercent_ForSnapshot
+ _objc_msgSend$callDetailsButtonPaddingTrail_ForSnapshot
+ _objc_msgSend$callDetailsButtonPaddingTrailingPercent_DynamicIsland
+ _objc_msgSend$callDetailsButtonPaddingTrailingPercent_HomeButton
+ _objc_msgSend$capCallDetailsViewButtonSize
+ _objc_msgSend$colorsForImageRef:
+ _objc_msgSend$contactImageBackgroundColors
+ _objc_msgSend$customAvatar
+ _objc_msgSend$deviceHasHomeButton
+ _objc_msgSend$displayName
+ _objc_msgSend$fullDeviceBounds
+ _objc_msgSend$fullDeviceHeight
+ _objc_msgSend$fullDeviceWidth
+ _objc_msgSend$incomingCallAndInCallControlsBottomPadding
+ _objc_msgSend$initWithConfiguration:style:contact:avatarImage:
+ _objc_msgSend$initWithConfiguration:style:nameString:avatarImage:
+ _objc_msgSend$moveMobileLabelToBeYAxisCenteredWithInfoButton
+ _objc_msgSend$nameLabelFontWithAvatar
+ _objc_msgSend$setAvatarView:
+ _objc_msgSend$setBackroundColor:
+ _objc_msgSend$setCustomAvatar:
+ _objc_msgSend$setLabelsColor:
+ _objc_msgSend$setMarqueeEnabled:
+ _objc_msgSend$setMaximumContentSizeCategory:
+ _objc_msgSend$setNameLabelTextColor:
+ _objc_msgSend$setupAvatarViewIfNeeded
+ _objc_msgSend$thumbnailImageData
+ _objc_msgSend$twelvePercentOfDeviceHeight
+ _objc_msgSend$updateTraitsIfNeeded
+ _objc_msgSend$withCaseSensitiveAttribute
+ _symbolic SDy___________pG 11TelephonyUI12TPTipsHelperC5EntryV4KindO 8TipsNext3TipP
+ _symbolic _____ 11TelephonyUI16LiveVoicemailTipV
+ _symbolic ____________pt 11TelephonyUI12TPTipsHelperC5EntryV4KindO 8TipsNext3TipP
+ _symbolic ______pSg 8TipsNext3TipP
+ _symbolic _____y___________pG s18_DictionaryStorageC 11TelephonyUI12TPTipsHelperC5EntryV4KindO 8TipsNext3TipP
- +[TPIncomingCallMetricsProvider bottomBarBottomMarginForHomeButtonOffset:]
- +[TPIncomingCallMetricsProvider verticalNameHorizontalStatusLabelPositionTransform]
- -[TPInComingCallUISnapshotViewController setUpCallDetailsViewButton]
- -[UIFont(TelephonyUI) telephonyUIFontByAddingCaseSensitiveLayoutEnabledAttribute]
- GCC_except_table16
- GCC_except_table18
- GCC_except_table9
- _CGAffineTransformMakeTranslation
- ___74+[TPIncomingCallMetricsProvider bottomBarBottomMarginForHomeButtonOffset:]_block_invoke
- _bottomBarBottomMarginForHomeButtonOffset:.bottomMargin
- _bottomBarBottomMarginForHomeButtonOffset:.onceToken
- _objc_msgSend$bottomBarBottomMarginForHomeButtonOffset:
- _objc_msgSend$homeButtonOffsetForSafeAreaFrame:
- _objc_msgSend$layoutFrame
- _objc_msgSend$setUpCallDetailsViewButton
- _objc_msgSend$telephonyUIFontByAddingCaseSensitiveLayoutEnabledAttribute
- _objc_msgSend$verticalNameHorizontalStatusLabelPositionTransform
CStrings:
+ "\n\x13"
+ "CID-frequentlyfavorite-mini-tip"
+ "CID-live-voicemail-phone-mini-tip"
+ "CNImageDerivedColorGenerator"
+ "Class getCNImageDerivedColorGeneratorClass(void)_block_invoke"
+ "Manage in Settings"
+ "See a transcription of an incoming message before answering the call. Calling and data rates may apply."
+ "T@\"UIImage\",&,N,V_customAvatar"
+ "T@\"UIImageView\",&,N,V_avatarView"
+ "_avatarView"
+ "_colorBlendedWithColor:"
+ "_colorDifferenceFromColor:"
+ "_customAvatar"
+ "avatarView"
+ "callDetailsButtonMaxSize"
+ "callDetailsButtonPaddingPercentTop_ForSnapshot"
+ "callDetailsButtonPaddingTopPercent_DynamicIsland"
+ "callDetailsButtonPaddingTopPercent_HomeButton"
+ "callDetailsButtonPaddingTopPercent_Notch"
+ "callDetailsButtonPaddingTop_ForSnapshot"
+ "callDetailsButtonPaddingTrailPercent_ForSnapshot"
+ "callDetailsButtonPaddingTrail_ForSnapshot"
+ "callDetailsButtonPaddingTrailingPercent_DynamicIsland"
+ "callDetailsButtonPaddingTrailingPercent_HomeButton"
+ "callDetailsButtonPaddingTrailingPercent_Notch"
+ "callScreeningEnabled"
+ "capCallDetailsViewButtonSize"
+ "colorsForImageRef:"
+ "com.apple.facetime.opened-livevoicemail-tip"
+ "contactImageBackgroundColors"
+ "currentTip"
+ "customAvatar"
+ "deviceHasHomeButton"
+ "displayName"
+ "fullDeviceBounds"
+ "fullDeviceHeight"
+ "fullDeviceWidth"
+ "incomingCallAndInCallControlsBottomPadding"
+ "initWithConfiguration:style:contact:avatarImage:"
+ "initWithConfiguration:style:nameString:avatarImage:"
+ "moveMobileLabelToBeYAxisCenteredWithInfoButton"
+ "nameLabelFontWithAvatar"
+ "posterBadgeMaxSize"
+ "setAvatarView:"
+ "setBackroundColor:"
+ "setCustomAvatar:"
+ "setLabelsColor:"
+ "setMarqueeEnabled:"
+ "setMaximumContentSizeCategory:"
+ "setupAvatarViewIfNeeded"
+ "softlink:r:path:/System/Library/Frameworks/ContactsUI.framework/ContactsUI"
+ "thumbnailImageData"
+ "twelvePercentOfDeviceHeight"
+ "updateTraitsIfNeeded"
+ "void *ContactsUILibrary(void)"
+ "withCaseSensitiveAttribute"
- "\t\x12"
- "bottomBarBottomMarginForHomeButtonOffset:"
- "didSetup"
- "layoutFrame"
- "setUpCallDetailsViewButton"
- "telephonyUIFontByAddingCaseSensitiveLayoutEnabledAttribute"
- "verticalNameHorizontalStatusLabelPositionTransform"
- "{CGAffineTransform=dddddd}16@0:8"

```
