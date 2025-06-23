## OnBoardingKit

> `/System/Library/PrivateFrameworks/OnBoardingKit.framework/OnBoardingKit`

```diff

-3962.0.0.0.0
-  __TEXT.__text: 0x3c514
+3965.0.0.0.0
+  __TEXT.__text: 0x3d80c
   __TEXT.__auth_stubs: 0x8c0
-  __TEXT.__objc_methlist: 0x577c
+  __TEXT.__objc_methlist: 0x586c
   __TEXT.__const: 0x3b6
-  __TEXT.__cstring: 0x18dd
+  __TEXT.__cstring: 0x193d
   __TEXT.__oslogstring: 0xe63
   __TEXT.__ustring: 0x4
   __TEXT.__gcc_except_tab: 0x74

   __TEXT.__constg_swiftt: 0x50
   __TEXT.__swift5_fieldmd: 0x10
   __TEXT.__swift5_types: 0x4
-  __TEXT.__unwind_info: 0xe40
-  __TEXT.__objc_classname: 0xb0a
-  __TEXT.__objc_methname: 0xef93
-  __TEXT.__objc_methtype: 0x1e14
-  __TEXT.__objc_stubs: 0xa640
-  __DATA_CONST.__got: 0x498
-  __DATA_CONST.__const: 0x6a8
+  __TEXT.__unwind_info: 0xe58
+  __TEXT.__objc_classname: 0xb40
+  __TEXT.__objc_methname: 0xf3ba
+  __TEXT.__objc_methtype: 0x1e17
+  __TEXT.__objc_stubs: 0xa920
+  __DATA_CONST.__got: 0x4a8
+  __DATA_CONST.__const: 0x688
   __DATA_CONST.__objc_classlist: 0x2d8
-  __DATA_CONST.__objc_catlist: 0x30
+  __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x98
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3790
+  __DATA_CONST.__objc_selrefs: 0x3868
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x288
   __DATA_CONST.__objc_arraydata: 0x90
   __AUTH_CONST.__auth_got: 0x470
   __AUTH_CONST.__const: 0x1e0
-  __AUTH_CONST.__cfstring: 0x2020
-  __AUTH_CONST.__objc_const: 0xcec8
+  __AUTH_CONST.__cfstring: 0x2080
+  __AUTH_CONST.__objc_const: 0xd048
   __AUTH_CONST.__objc_intobj: 0x1f8
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH.__objc_data: 0x1158
   __AUTH.__data: 0x98
-  __DATA.__objc_ivar: 0x578
+  __DATA.__objc_ivar: 0x594
   __DATA.__data: 0x728
   __DATA.__bss: 0x70
   __DATA.__common: 0x60

   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
-  - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: EB5D5B91-2C12-3A95-800D-B20A92F2953D
-  Functions: 1650
-  Symbols:   6234
-  CStrings:  3373
+  UUID: F7C72EEE-C28C-30EC-9709-BFE0EB1AEEAF
+  Functions: 1669
+  Symbols:   6298
+  CStrings:  3421
 
Symbols:
+ -[NSMutableAttributedString(ParagraphSpacing) compressDoubleSpacingBy:]
+ -[OBBulletedListItem leadingMargin]
+ -[OBBulletedListItem topMargin]
+ -[OBBulletedListItem trailingMargin]
+ -[OBButtonTray(OBButtonTrayScrollPocketInteraction) addScrollPocketToScrollView:]
+ -[OBButtonTray(OBButtonTrayScrollPocketInteraction) removeScrollPocket]
+ -[OBHeaderView appNameLabel]
+ -[OBHeaderView badgeLabel]
+ -[OBHeaderView headerLeftEdgeConstraint]
+ -[OBHeaderView headerRightEdgeConstraint]
+ -[OBHeaderView setAppNameForIntroScreen:]
+ -[OBHeaderView setAppNameLabel:]
+ -[OBHeaderView setBadgeLabel:]
+ -[OBHeaderView setBadgeText:]
+ -[OBHeaderView setHeaderLeftEdgeConstraint:]
+ -[OBHeaderView setHeaderRightEdgeConstraint:]
+ -[OBHeaderView setUseIntroScreenLayout:]
+ -[OBHeaderView useIntroScreenLayout]
+ -[OBPrivacyFlow localizedButtonCaptionSymbolNameForLanguage:preferredDeviceType:]
+ -[OBPrivacyLinkButton captionAttachmentImage]
+ -[OBPrivacyLinkButton initWithCaption:captionAttachmentImage:buttonText:image:imageSize:useLargeIcon:displayLanguage:]
+ -[OBTextBulletedListItem leadingMargin]
+ -[OBTextBulletedListItem topMargin]
+ -[OBTextBulletedListItem trailingMargin]
+ -[OBWelcomeController applicationDidBecomeActive:]
+ -[OBWelcomeController initForIntroScreenWithTitle:appName:detailText:icon:]
+ _OBJC_CLASS_$_NSTextEncapsulation
+ _OBJC_IVAR_$_OBHeaderView._appNameLabel
+ _OBJC_IVAR_$_OBHeaderView._badgeLabel
+ _OBJC_IVAR_$_OBHeaderView._headerLeftEdgeConstraint
+ _OBJC_IVAR_$_OBHeaderView._headerRightEdgeConstraint
+ _OBJC_IVAR_$_OBHeaderView._useIntroScreenLayout
+ _OBJC_IVAR_$_OBPrivacyLinkButton._captionAttachmentImage
+ _OBJC_IVAR_$_OBWelcomeController._symbolNeedsAnimation
+ _UIApplicationDidBecomeActiveNotification
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_NSMutableAttributedString_$_ParagraphSpacing
+ __OBJC_$_CATEGORY_NSMutableAttributedString_$_ParagraphSpacing
+ __OBJC_$_INSTANCE_METHODS_OBButtonTray(OBButtonTrayScrollPocketInteraction)
+ ___block_literal_global.100
+ _objc_msgSend$_setTextEncapsulation:
+ _objc_msgSend$appNameLabel
+ _objc_msgSend$applicationState
+ _objc_msgSend$badgeLabel
+ _objc_msgSend$compressDoubleSpacingBy:
+ _objc_msgSend$configurationWithPointSize:weight:scale:
+ _objc_msgSend$configurationWithWeight:
+ _objc_msgSend$constraintGreaterThanOrEqualToConstant:
+ _objc_msgSend$headerLeftEdgeConstraint
+ _objc_msgSend$headerRightEdgeConstraint
+ _objc_msgSend$initWithCaption:captionAttachmentImage:buttonText:image:imageSize:useLargeIcon:displayLanguage:
+ _objc_msgSend$leadingMargin
+ _objc_msgSend$localizedButtonCaptionSymbolNameForLanguage:preferredDeviceType:
+ _objc_msgSend$rangeOfString:options:range:
+ _objc_msgSend$setAppNameForIntroScreen:
+ _objc_msgSend$setAppNameLabel:
+ _objc_msgSend$setBadgeLabel:
+ _objc_msgSend$setHeaderLeftEdgeConstraint:
+ _objc_msgSend$setHeaderRightEdgeConstraint:
+ _objc_msgSend$setPlatterSize:
+ _objc_msgSend$setShape:
+ _objc_msgSend$setUseIntroScreenLayout:
+ _objc_msgSend$textAttachmentWithImage:
+ _objc_msgSend$topMargin
+ _objc_msgSend$trailingMargin
+ _objc_msgSend$useIntroScreenLayout
+ _objc_msgSend$whiteColor
- -[OBBulletedListItem leadingMargins]
- -[OBBulletedListItem trailingMargins]
- -[OBButtonTray addScrollPocketToScrollView:]
- -[OBButtonTray removeScrollPocket]
- -[OBPrivacyLinkButton initWithCaption:buttonText:image:imageSize:useLargeIcon:displayLanguage:]
- -[OBTextBulletedListItem leadingMargins]
- -[OBTextBulletedListItem trailingMargins]
- __OBJC_$_INSTANCE_METHODS_OBButtonTray
- ___block_literal_global.96
- __swift_FORCE_LOAD_$_swiftDarwin
- __swift_FORCE_LOAD_$_swiftDarwin_$_OnBoardingKit
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_OnBoardingKit
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_OnBoardingKit
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_OnBoardingKit
- _objc_msgSend$configurationPreferringMonochrome
- _objc_msgSend$initWithCaption:buttonText:image:imageSize:useLargeIcon:displayLanguage:
- _objc_msgSend$leadingMargins
- _objc_msgSend$trailingMargins
CStrings:
+ " do not localize"
+ "@76@0:8@16@24@32@40{CGSize=dd}48B64@68"
+ "BUTTON_CAPTION_SYMBOL_NAME"
+ "BUTTON_SPACE_BETWEEN_BUTTON_CAPTION_ATTACHMENT_IMAGE_AND_TEXT"
+ "OBButtonTrayScrollPocketInteraction"
+ "ParagraphSpacing"
+ "T@\"NSLayoutConstraint\",&,N,V_headerLeftEdgeConstraint"
+ "T@\"NSLayoutConstraint\",&,N,V_headerRightEdgeConstraint"
+ "T@\"UIImage\",R,V_captionAttachmentImage"
+ "T@\"UILabel\",&,N,V_appNameLabel"
+ "T@\"UILabel\",&,N,V_badgeLabel"
+ "TB,N,V_useIntroScreenLayout"
+ "_appNameLabel"
+ "_badgeLabel"
+ "_captionAttachmentImage"
+ "_headerLeftEdgeConstraint"
+ "_headerRightEdgeConstraint"
+ "_setTextEncapsulation:"
+ "_symbolNeedsAnimation"
+ "_useIntroScreenLayout"
+ "appNameLabel"
+ "applicationDidBecomeActive:"
+ "applicationState"
+ "badgeLabel"
+ "captionAttachmentImage"
+ "compressDoubleSpacingBy:"
+ "configurationWithPointSize:weight:scale:"
+ "configurationWithWeight:"
+ "constraintGreaterThanOrEqualToConstant:"
+ "headerLeftEdgeConstraint"
+ "headerRightEdgeConstraint"
+ "initForIntroScreenWithTitle:appName:detailText:icon:"
+ "initWithCaption:captionAttachmentImage:buttonText:image:imageSize:useLargeIcon:displayLanguage:"
+ "leadingMargin"
+ "localizedButtonCaptionSymbolNameForLanguage:preferredDeviceType:"
+ "rangeOfString:options:range:"
+ "setAppNameForIntroScreen:"
+ "setAppNameLabel:"
+ "setBadgeLabel:"
+ "setBadgeText:"
+ "setHeaderLeftEdgeConstraint:"
+ "setHeaderRightEdgeConstraint:"
+ "setPlatterSize:"
+ "setShape:"
+ "setUseIntroScreenLayout:"
+ "textAttachmentWithImage:"
+ "topMargin"
+ "trailingMargin"
+ "useIntroScreenLayout"
+ "whiteColor"
- "@68@0:8@16@24@32{CGSize=dd}40B56@60"
- "configurationPreferringMonochrome"
- "initWithCaption:buttonText:image:imageSize:useLargeIcon:displayLanguage:"
- "leadingMargins"
- "trailingMargins"

```
