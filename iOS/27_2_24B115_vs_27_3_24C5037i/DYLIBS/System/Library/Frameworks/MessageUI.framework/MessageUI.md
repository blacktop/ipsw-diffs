## MessageUI

> `/System/Library/Frameworks/MessageUI.framework/MessageUI`

```diff

-3901.200.71.2.2
-  __TEXT.__text: 0x14baf0
+3901.300.26.0.0
+  __TEXT.__text: 0x14bdfc
   __TEXT.__delay_helper: 0x114
-  __TEXT.__objc_methlist: 0x12b44
-  __TEXT.__cstring: 0xa356
-  __TEXT.__gcc_except_tab: 0x256e4
+  __TEXT.__objc_methlist: 0x12b84
+  __TEXT.__cstring: 0xa316
+  __TEXT.__gcc_except_tab: 0x25780
   __TEXT.__const: 0x2004
   __TEXT.__ustring: 0x4dc
   __TEXT.__oslogstring: 0x647e

   __TEXT.__swift_as_entry: 0x28
   __TEXT.__swift_as_ret: 0x2c
   __TEXT.__swift_as_cont: 0x50
-  __TEXT.__unwind_info: 0xb5a0
+  __TEXT.__unwind_info: 0xb5c8
   __TEXT.__eh_frame: 0x5e8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x4a88
+  __DATA_CONST.__const: 0x4a60
   __DATA_CONST.__objc_classlist: 0x618
   __DATA_CONST.__objc_catlist: 0x108
   __DATA_CONST.__objc_protolist: 0x418
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xc360
+  __DATA_CONST.__objc_selrefs: 0xc3a0
   __DATA_CONST.__objc_protorefs: 0x68
   __DATA_CONST.__objc_superrefs: 0x4a8
   __DATA_CONST.__objc_arraydata: 0x638
-  __DATA_CONST.__got: 0x1f10
+  __DATA_CONST.__got: 0x1f08
   __AUTH_CONST.__const: 0x1cd0
   __AUTH_CONST.__cfstring: 0x8f00
-  __AUTH_CONST.__objc_const: 0x1a788
+  __AUTH_CONST.__objc_const: 0x1a758
   __AUTH_CONST.__objc_floatobj: 0x20
   __AUTH_CONST.__objc_intobj: 0x1b0
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__objc_dictobj: 0x578
-  __AUTH_CONST.__auth_got: 0x18f0
+  __AUTH_CONST.__auth_got: 0x18f8
   __AUTH.__objc_data: 0x34e8
   __AUTH.__data: 0x358
-  __DATA.__objc_ivar: 0x1154
+  __DATA.__objc_ivar: 0x114c
   __DATA.__data: 0x3870
   __DATA.__common: 0x2f8
   __DATA_DIRTY.__objc_data: 0xb90

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 6905
-  Symbols:   11676
-  CStrings:  2087
+  Functions: 6907
+  Symbols:   11687
+  CStrings:  2086
 
Symbols:
+ -[MFComposeWebView _updateComposeToolbarItems]
+ -[MFComposeWebView _updateNavigationToolbarItems:]
+ -[MFComposeWebView safeAreaInsetsDidChange]
+ -[MFComposeWebView updateObscuredInsetsForComposeToolbar]
+ -[MFMailComposeController _addsKeyboardToSafeArea]
+ -[MFMailComposeController _keyboardWillChangeFrame:]
+ -[MFMailComposeController _updateSafeAreaForKeyboard]
+ -[MFMailComposeController composeToolbarShown]
+ -[MFMailComposeController composeWebView:updateNavigationToolbarItems:]
+ -[MFMailComposeController keyboardFrameInScreen]
+ -[MFMailComposeController setComposeToolbarShown:]
+ -[MFMailComposeController setKeyboardFrameInScreen:]
+ -[MFMailComposeController viewSafeAreaInsetsDidChange]
+ -[MFMailComposeView composeWebViewSafeAreaInsetsDidChange:]
+ -[UITraitCollection(Convenience) mf_hasVerticalBarEdge]
+ GCC_except_table177
+ GCC_except_table237
+ GCC_except_table244
+ GCC_except_table249
+ GCC_except_table252
+ GCC_except_table255
+ GCC_except_table273
+ GCC_except_table677
+ GCC_except_table685
+ GCC_except_table693
+ GCC_except_table708
+ GCC_except_table714
+ GCC_except_table715
+ GCC_except_table716
+ GCC_except_table717
+ GCC_except_table718
+ GCC_except_table842
+ GCC_except_table843
+ GCC_except_table845
+ GCC_except_table847
+ GCC_except_table848
+ GCC_except_table849
+ _OBJC_IVAR_$_MFComposeWebView._composeToolbarShown
+ _OBJC_IVAR_$_MFMailComposeController._composeToolbarShown
+ _OBJC_IVAR_$_MFMailComposeController._keyboardFrameInScreen
+ _UIKeyboardWillChangeFrameNotification
+ __UIEnhancedLandscapeBarEnabled
+ ___48-[MFComposeWebView releaseFocusAfterDismissing:]_block_invoke_2
- -[MFComposeWebView _composeToolbarUsageDidChange]
- -[MFComposeWebView _setNeedsComposeToolbarUsageUpdate]
- -[MFComposeWebView _supportsComposeToolbar]
- -[MFComposeWebView _updateHingeClosed:]
- -[MFComposeWebView _updatePocketContainerInteractionVisible]
- -[MFComposeWebView composeInputAccessoryPocketContainerInteraction]
- -[MFComposeWebView composeInputAccessoryView]
- -[MFComposeWebView inputAccessoryViewHeight]
- -[MFComposeWebView inputAccessoryView]
- -[MFComposeWebView setComposeInputAccessoryPocketContainerInteraction:]
- -[MFComposeWebView setComposeInputAccessoryView:]
- GCC_except_table253
- GCC_except_table671
- GCC_except_table682
- GCC_except_table690
- GCC_except_table698
- GCC_except_table713
- GCC_except_table829
- GCC_except_table830
- GCC_except_table833
- GCC_except_table834
- GCC_except_table836
- GCC_except_table840
- _OBJC_CLASS_$__UIScrollPocketContainerInteraction
- _OBJC_IVAR_$_MFComposeWebView._composeInputAccessoryPocketContainerInteraction
- _OBJC_IVAR_$_MFComposeWebView._composeInputAccessoryView
- _OBJC_IVAR_$_MFComposeWebView._composeToolbarInUse
- _OBJC_IVAR_$_MFComposeWebView._composeToolbarUsageUpdateScheduled
- _OBJC_IVAR_$_MFComposeWebView._hingeClosed
- ___47-[MFComposeWebView initWithFrame:isQuickReply:]_block_invoke_7
- ___54-[MFComposeWebView _setNeedsComposeToolbarUsageUpdate]_block_invoke
- ___block_descriptor_40_ea8_32w_e52_v24?0"<UITraitEnvironment>"8"UITraitCollection"16lw32l8
CStrings:
- "v24@?0@\"<UITraitEnvironment>\"8@\"UITraitCollection\"16"
```
