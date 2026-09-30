## OnBoardingKit

> `/System/iOSSupport/System/Library/PrivateFrameworks/OnBoardingKit.framework/Versions/A/OnBoardingKit`

```diff

-3977.0.23.0.0
-  __TEXT.__text: 0x37188
-  __TEXT.__objc_methlist: 0x50ec
-  __TEXT.__cstring: 0x18a9
-  __TEXT.__const: 0x4e4
-  __TEXT.__oslogstring: 0xc5d
+3977.1.3.1.0
+  __TEXT.__text: 0x379f4
+  __TEXT.__objc_methlist: 0x515c
+  __TEXT.__cstring: 0x1919
+  __TEXT.__const: 0x4f4
+  __TEXT.__oslogstring: 0xd72
   __TEXT.__ustring: 0x4
-  __TEXT.__gcc_except_tab: 0xa4
+  __TEXT.__gcc_except_tab: 0xdc
   __TEXT.__swift5_typeref: 0xe
   __TEXT.__constg_swiftt: 0x50
   __TEXT.__swift5_fieldmd: 0x10
   __TEXT.__swift5_types: 0x4
-  __TEXT.__unwind_info: 0x1070
+  __TEXT.__unwind_info: 0x10b0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x638
-  __DATA_CONST.__objc_classlist: 0x288
+  __DATA_CONST.__objc_classlist: 0x290
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x35e0
+  __DATA_CONST.__objc_selrefs: 0x3628
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x240
+  __DATA_CONST.__objc_superrefs: 0x248
   __DATA_CONST.__objc_arraydata: 0x90
-  __DATA_CONST.__got: 0x458
+  __DATA_CONST.__got: 0x468
   __AUTH_CONST.__const: 0x180
-  __AUTH_CONST.__cfstring: 0x1fe0
-  __AUTH_CONST.__objc_const: 0xa778
+  __AUTH_CONST.__cfstring: 0x2040
+  __AUTH_CONST.__objc_const: 0xa858
   __AUTH_CONST.__objc_intobj: 0x1b0
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_arrayobj: 0x30
-  __AUTH_CONST.__auth_got: 0x450
-  __AUTH.__objc_data: 0xb40
+  __AUTH_CONST.__auth_got: 0x460
+  __AUTH.__objc_data: 0xb90
   __AUTH.__data: 0x98
-  __DATA.__objc_ivar: 0x594
+  __DATA.__objc_ivar: 0x59c
   __DATA.__data: 0x5a0
   __DATA.__common: 0x60
   __DATA_DIRTY.__objc_data: 0xdc0

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1582
-  Symbols:   4287
-  CStrings:  341
+  Functions: 1593
+  Symbols:   4315
+  CStrings:  347
 
Symbols:
+ -[OBBaseWelcomeController _allowApplicationTerminationWhileModal]
+ -[OBHeaderBadgeLabel intrinsicContentSize]
+ -[OBPrivacyLinkButton _isLaidOutEdgeToEdgeWithWindow]
+ -[OBPrivacyLinkButton _setSafeAreaAnchoringTrustedForContentGutter:]
+ -[OBPrivacyLinkButton _textLeadingContainerConstraintForTesting]
+ -[OBTextAccessoryButton intrinsicContentSize]
+ -[OBTextAccessoryButton lastIntrinsicContentSizeWidth]
+ -[OBTextAccessoryButton layoutSubviews]
+ -[OBTextAccessoryButton setLastIntrinsicContentSizeWidth:]
+ -[OBTextBulletedListItem dotSize]
+ GCC_except_table20
+ OBJC_IVAR_$_OBPrivacyLinkButton._safeAreaAnchoringTrustedForContentGutter
+ OBJC_IVAR_$_OBTextAccessoryButton._lastIntrinsicContentSizeWidth
+ _OBJC_CLASS_$_OBHeaderBadgeLabel
+ _OBJC_EHTYPE_$_NSException
+ _OBJC_METACLASS_$_OBHeaderBadgeLabel
+ _OBRectIsFlushHorizontally
+ __OBJC_$_INSTANCE_METHODS_OBHeaderBadgeLabel
+ __OBJC_CLASS_RO_$_OBHeaderBadgeLabel
+ __OBJC_METACLASS_RO_$_OBHeaderBadgeLabel
+ ___kCFBooleanFalse
+ _objc_begin_catch
+ _objc_end_catch
+ _objc_msgSend$_allowApplicationTerminationWhileModal
+ _objc_msgSend$_isLaidOutEdgeToEdgeWithWindow
+ _objc_msgSend$contentInsets
+ _objc_msgSend$convertRect:toView:
+ _objc_msgSend$dotSize
+ _objc_msgSend$lastIntrinsicContentSizeWidth
+ _objc_msgSend$layoutFrame
+ _objc_msgSend$setLastIntrinsicContentSizeWidth:
+ _objc_msgSend$setValue:forKeyPath:
- -[OBPrivacyLinkButton _isLaidOutEdgeToEdgeWithSuperview]
- -[OBTableWelcomeController _setAdditionalTopInsetForColumnLayout]
- _objc_msgSend$_isLaidOutEdgeToEdgeWithSuperview
- _objc_msgSend$_setAdditionalTopInsetForColumnLayout
CStrings:
+ "-seed"
+ "A presented form sheet has no window scene; the app may not be quittable until this sheet is dismissed"
+ "Could not allow application termination while modal; the app may not be quittable until this sheet is dismissed: %{public}@"
+ "HideFromCombinedListForGMECHINA"
+ "HideFromCombinedListForGMECHINA must be a boolean"
+ "_UINSWindowProxy.attachedWindow.preventsApplicationTerminationWhenModal"
```
