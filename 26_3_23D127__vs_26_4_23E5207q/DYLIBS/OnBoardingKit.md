## OnBoardingKit

> `/System/Library/PrivateFrameworks/OnBoardingKit.framework/OnBoardingKit`

```diff

-3976.2.1.0.0
-  __TEXT.__text: 0x3e554
-  __TEXT.__auth_stubs: 0x870
-  __TEXT.__objc_methlist: 0x5924
-  __TEXT.__const: 0x3c4
-  __TEXT.__cstring: 0x191d
-  __TEXT.__oslogstring: 0xef5
+3976.4.6.3.0
+  __TEXT.__text: 0x45f98
+  __TEXT.__auth_stubs: 0x810
+  __TEXT.__objc_methlist: 0x5a4c
+  __TEXT.__const: 0x3d4
+  __TEXT.__cstring: 0x1879
+  __TEXT.__oslogstring: 0xfab
   __TEXT.__ustring: 0x4
   __TEXT.__gcc_except_tab: 0x74
   __TEXT.__swift5_typeref: 0xe
   __TEXT.__constg_swiftt: 0x50
   __TEXT.__swift5_fieldmd: 0x10
   __TEXT.__swift5_types: 0x4
-  __TEXT.__unwind_info: 0xe80
-  __TEXT.__objc_classname: 0xb26
-  __TEXT.__objc_methname: 0xf548
-  __TEXT.__objc_methtype: 0x1e0a
-  __TEXT.__objc_stubs: 0xaa60
+  __TEXT.__unwind_info: 0x1330
+  __TEXT.__objc_classname: 0xb8d
+  __TEXT.__objc_methname: 0xfa0e
+  __TEXT.__objc_methtype: 0x1e33
+  __TEXT.__objc_stubs: 0xae40
   __DATA_CONST.__got: 0x4a0
-  __DATA_CONST.__const: 0x688
+  __DATA_CONST.__const: 0x680
   __DATA_CONST.__objc_classlist: 0x2d0
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x98
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x38c8
+  __DATA_CONST.__objc_selrefs: 0x39d0
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x280
   __DATA_CONST.__objc_arraydata: 0x90
-  __AUTH_CONST.__auth_got: 0x448
+  __AUTH_CONST.__auth_got: 0x418
   __AUTH_CONST.__const: 0x1e0
   __AUTH_CONST.__cfstring: 0x2060
-  __AUTH_CONST.__objc_const: 0xd098
+  __AUTH_CONST.__objc_const: 0xd188
   __AUTH_CONST.__objc_intobj: 0x1f8
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH.__objc_data: 0x11d0
   __AUTH.__data: 0x98
-  __DATA.__objc_ivar: 0x5a4
+  __DATA.__objc_ivar: 0x5b8
   __DATA.__data: 0x728
-  __DATA.__bss: 0x68
+  __DATA.__bss: 0x70
   __DATA.__common: 0x60
   __DATA_DIRTY.__objc_data: 0xa00
-  __DATA_DIRTY.__bss: 0x48
+  __DATA_DIRTY.__bss: 0x40
+  - /System/Library/Frameworks/Accessibility.framework/Accessibility
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 08DB0203-4FE2-3A76-A307-DB931DDBF0A7
-  Functions: 1685
-  Symbols:   6334
-  CStrings:  3440
+  UUID: 01E49503-9031-3629-A0C6-79D33B8A7C24
+  Functions: 1717
+  Symbols:   6426
+  CStrings:  3483
 
Symbols:
+ +[OBPrivacyFlow _splashPlistFromBundle:forResource:]
+ -[OBBulletedList addItemWithTitle:attributedString:image:showsBackground:]
+ -[OBBulletedListItem _commonInitWithAccessoryButton:]
+ -[OBBulletedListItem _createDescriptionLabelWithTintColor:]
+ -[OBBulletedListItem _createImageViewWithImage:tintColor:]
+ -[OBBulletedListItem _createTitleLabelWithTitle:]
+ -[OBBulletedListItem _updateStackViewLayout]
+ -[OBBulletedListItem initWithTitle:attributedString:image:showsBackground:]
+ -[OBBulletedListItem setShowsBackground:]
+ -[OBBulletedListItem setStackViewTrailingConstraint:]
+ -[OBBulletedListItem setUsesAttributedString:]
+ -[OBBulletedListItem showsBackground]
+ -[OBBulletedListItem stackViewTrailingConstraint]
+ -[OBBulletedListItem usesAttributedString]
+ -[OBHeaderView additionalSymbolConfiguration]
+ -[OBHeaderView applySymbolConfiguration:]
+ -[OBHeaderView customIconContainerHeight]
+ -[OBHeaderView setAdditionalSymbolConfiguration:]
+ -[OBHeaderView setCustomIconContainerHeight:]
+ -[OBHeaderView updateImageView]
+ -[OBSetupAssistantPasscodeViewController _ensureContentVisibleAboveKeyboard]
+ -[OBSetupAssistantPasscodeViewController _keyboardWillShow:]
+ -[OBSetupAssistantPasscodeViewController dealloc]
+ -[OBWelcomeController(BulletedList) addBulletedListItemWithTitle:attributedString:image:showsBackground:]
+ -[OBWelcomeController(BulletedList) commonInit]
+ _AXShowBordersEnabled
+ _OBBulletedListItemPaddingWhenShowingBackground
+ _OBJC_IVAR_$_OBBulletedListItem._showsBackground
+ _OBJC_IVAR_$_OBBulletedListItem._stackViewTrailingConstraint
+ _OBJC_IVAR_$_OBBulletedListItem._usesAttributedString
+ _OBJC_IVAR_$_OBHeaderView._additionalSymbolConfiguration
+ _OBJC_IVAR_$_OBHeaderView._customIconContainerHeight
+ _OUTLINED_FUNCTION_1
+ _OUTLINED_FUNCTION_2
+ ___60-[OBSetupAssistantPasscodeViewController _keyboardWillShow:]_block_invoke
+ ___block_literal_global.99
+ _objc_msgSend$URLForResource:withExtension:
+ _objc_msgSend$_commonInitWithAccessoryButton:
+ _objc_msgSend$_createDescriptionLabelWithTintColor:
+ _objc_msgSend$_createImageViewWithImage:tintColor:
+ _objc_msgSend$_createTitleLabelWithTitle:
+ _objc_msgSend$_ensureContentVisibleAboveKeyboard
+ _objc_msgSend$_splashPlistFromBundle:forResource:
+ _objc_msgSend$_updateStackViewLayout
+ _objc_msgSend$addItemWithTitle:attributedString:image:showsBackground:
+ _objc_msgSend$additionalSymbolConfiguration
+ _objc_msgSend$adjustedContentInset
+ _objc_msgSend$commonInit
+ _objc_msgSend$configurationWithHierarchicalColor:
+ _objc_msgSend$convertRect:toView:
+ _objc_msgSend$customIconContainerHeight
+ _objc_msgSend$dictionaryWithContentsOfURL:error:
+ _objc_msgSend$imageWithSymbolConfiguration:
+ _objc_msgSend$initWithTitle:attributedString:image:showsBackground:
+ _objc_msgSend$localizedDescription
+ _objc_msgSend$removeObserver:
+ _objc_msgSend$setAdditionalSymbolConfiguration:
+ _objc_msgSend$setScrollingDisabled:
+ _objc_msgSend$setShowsBackground:
+ _objc_msgSend$setStackViewTrailingConstraint:
+ _objc_msgSend$setTag:
+ _objc_msgSend$setUsesAttributedString:
+ _objc_msgSend$showsBackground
+ _objc_msgSend$stackViewTrailingConstraint
+ _objc_msgSend$tag
+ _objc_msgSend$tertiarySystemFillColor
+ _objc_msgSend$updateImageView
+ _objc_msgSend$usesAttributedString
+ _objc_msgSend$visibleSize
+ _objc_retain_x26
+ _objc_retain_x28
- _NSLog
- _UIAccessibilityButtonShapesEnabled
- ___block_literal_global.100
- __swift_FORCE_LOAD_$_swiftAccelerate
- __swift_FORCE_LOAD_$_swiftAccelerate_$_OnBoardingKit
- _objc_claimAutoreleasedReturnValue
- _objc_msgSend$dictionaryWithContentsOfFile:
- _objc_msgSend$pathForResource:ofType:
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x4
- _objc_retain_x5
- _objc_retain_x6
CStrings:
+ "-seed"
+ "@\"UIImageSymbolConfiguration\""
+ "Failed to generate URL for splash file with content name '%@' in bundle %@"
+ "Failed to load splash plist at %@: %@"
+ "Failed to load splash plist at %@: file exists but its contents are not a valid dictionary representation."
+ "T@\"NSLayoutConstraint\",&,N,V_stackViewTrailingConstraint"
+ "T@\"UIImageSymbolConfiguration\",&,N,V_additionalSymbolConfiguration"
+ "TB,N,V_showsBackground"
+ "TB,N,V_usesAttributedString"
+ "Td,N,V_customIconContainerHeight"
+ "URLForResource:withExtension:"
+ "_additionalSymbolConfiguration"
+ "_commonInitWithAccessoryButton:"
+ "_createDescriptionLabelWithTintColor:"
+ "_createImageViewWithImage:tintColor:"
+ "_createTitleLabelWithTitle:"
+ "_customIconContainerHeight"
+ "_ensureContentVisibleAboveKeyboard"
+ "_keyboardWillShow:"
+ "_showsBackground"
+ "_splashPlistFromBundle:forResource:"
+ "_stackViewTrailingConstraint"
+ "_updateStackViewLayout"
+ "_usesAttributedString"
+ "addBulletedListItemWithTitle:attributedString:image:showsBackground:"
+ "addItemWithTitle:attributedString:image:showsBackground:"
+ "additionalSymbolConfiguration"
+ "adjustedContentInset"
+ "applySymbolConfiguration:"
+ "commonInit"
+ "convertRect:toView:"
+ "customIconContainerHeight"
+ "dealloc"
+ "dictionaryWithContentsOfURL:error:"
+ "initWithTitle:attributedString:image:showsBackground:"
+ "localizedDescription"
+ "removeObserver:"
+ "setAdditionalSymbolConfiguration:"
+ "setCustomIconContainerHeight:"
+ "setShowsBackground:"
+ "setStackViewTrailingConstraint:"
+ "setTag:"
+ "setUsesAttributedString:"
+ "showsBackground"
+ "stackViewTrailingConstraint"
+ "tag"
+ "tertiarySystemFillColor"
+ "updateImageView"
+ "usesAttributedString"
+ "visibleSize"
- "\r"
- "No splash found in bundle at path: %@"
- "Warning: Attempted to add a nil constraint!"
- "dictionaryWithContentsOfFile:"
- "pathForResource:ofType:"

```
