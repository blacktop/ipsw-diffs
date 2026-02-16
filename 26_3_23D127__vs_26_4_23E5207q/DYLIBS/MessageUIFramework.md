## MessageUIFramework

> `/System/Library/AccessibilityBundles/MessageUIFramework.axbundle/MessageUIFramework`

```diff

-3005.4.19.0.0
-  __TEXT.__text: 0x76e4
-  __TEXT.__auth_stubs: 0x490
+3005.16.0.0.0
+  __TEXT.__text: 0x7b88
+  __TEXT.__auth_stubs: 0x450
   __TEXT.__objc_methlist: 0xe34
   __TEXT.__cstring: 0x190e
   __TEXT.__oslogstring: 0x3d

   __TEXT.__gcc_except_tab: 0x108
   __TEXT.__unwind_info: 0x358
   __TEXT.__objc_classname: 0xcab
-  __TEXT.__objc_methname: 0x1225
+  __TEXT.__objc_methname: 0x1238
   __TEXT.__objc_methtype: 0x16e
-  __TEXT.__objc_stubs: 0x1120
+  __TEXT.__objc_stubs: 0x1140
   __DATA_CONST.__got: 0x128
   __DATA_CONST.__const: 0x228
   __DATA_CONST.__objc_classlist: 0x268
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5d0
+  __DATA_CONST.__objc_selrefs: 0x5d8
   __DATA_CONST.__objc_superrefs: 0xc0
-  __AUTH_CONST.__auth_got: 0x258
+  __AUTH_CONST.__auth_got: 0x238
   __AUTH_CONST.__const: 0x200
   __AUTH_CONST.__cfstring: 0x22a0
   __AUTH_CONST.__objc_const: 0x2b50
   __AUTH.__objc_data: 0x140
-  __DATA.__bss: 0x38
+  __DATA.__bss: 0x30
   __DATA_DIRTY.__objc_data: 0x16d0
   __DATA_DIRTY.__common: 0x8
   __DATA_DIRTY.__bss: 0x8

   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F552CF8D-9C9B-374F-BE89-4322C71DB778
+  UUID: D80FCDF1-9216-3B39-A5C4-32F65D99A0CB
   Functions: 277
-  Symbols:   1238
-  CStrings:  865
+  Symbols:   1235
+  CStrings:  866
 
Symbols:
+ _objc_msgSend$axSafelyAddObject:
+ _objc_retain_x25
+ _objc_retain_x26
- _objc_claimAutoreleasedReturnValue
- _objc_retain_x1
- _objc_retain_x2
- _objc_retain_x23
- _objc_retain_x3
- _objc_retain_x8
Functions:
~ +[AXMessageUIFrameworkGlue accessibilityInitializeBundle] : 280 -> 288
~ ___57+[AXMessageUIFrameworkGlue accessibilityInitializeBundle]_block_invoke : 1056 -> 1060
~ ___57+[AXMessageUIFrameworkGlue accessibilityInitializeBundle]_block_invoke_2 : 84 -> 88
~ ___57+[AXMessageUIFrameworkGlue accessibilityInitializeBundle]_block_invoke_3 : 792 -> 800
~ +[AXMessageUIFrameworkGlue _webKitInitialized] : 156 -> 160
~ ___46+[AXMessageUIFrameworkGlue _webKitInitialized]_block_invoke_2 : 100 -> 104
~ ___46+[AXMessageUIFrameworkGlue _webKitInitialized]_block_invoke_4 : 84 -> 88
~ -[WKContentViewAccessibility__MessageUI__WebKit _accessibilityLoadAccessibilityInformation] : 264 -> 268
~ ___91-[WKContentViewAccessibility__MessageUI__WebKit _accessibilityLoadAccessibilityInformation]_block_invoke : 268 -> 276
~ -[WKContentViewAccessibility__MessageUI__WebKit _axRepostFirstResponderWhenReady] : 304 -> 316
~ -[WKContentViewAccessibility__MessageUI__WebKit dealloc] : 108 -> 112
~ +[MFAtomTextViewAccessibility _accessibilityPerformValidations:] : 176 -> 188
~ -[MFAtomTextViewAccessibility _accessibilityLoadAccessibilityInformation] : 176 -> 188
~ -[MFAttachmentAccessibility markupStringForDisplayWithData:allowAttachmentElement:] : 168 -> 172
~ +[MFCaptionLabelAccessibility _accessibilityPerformValidations:] : 120 -> 128
~ -[MFCaptionLabelAccessibility accessibilityLabel] : 424 -> 440
~ ___49-[MFCaptionLabelAccessibility accessibilityLabel]_block_invoke : 76 -> 80
~ +[MFComposeActionCardTitleViewAccessibility _accessibilityPerformValidations:] : 180 -> 192
~ -[MFComposeActionCardTitleViewAccessibility _accessibilityLoadAccessibilityInformation] : 744 -> 768
~ +[MFComposeFromViewAccessibility _accessibilityPerformValidations:] : 128 -> 140
~ -[MFComposeFromViewAccessibility accessibilityValue] : 84 -> 92
~ -[MFComposeImageSizeViewAccessibility setSizeDescription:forScale:] : 564 -> 580
~ ___67-[MFComposeImageSizeViewAccessibility setSizeDescription:forScale:]_block_invoke : 468 -> 504
~ ___67-[MFComposeImageSizeViewAccessibility setSizeDescription:forScale:]_block_invoke.317 : 116 -> 120
~ -[MFComposeImageSizeViewAccessibility accessibilityElementsHidden] : 72 -> 76
~ -[MFComposeInputAccessoryViewAccessibility accessibilityElements] : 392 -> 420
~ +[MFComposeRecipientTextViewAccessibility _accessibilityPerformValidations:] : 348 -> 356
~ -[MFComposeRecipientTextViewAccessibility _accessibilityLoadAccessibilityInformation] : 108 -> 112
~ -[MFComposeRecipientTextViewAccessibility _updateInactiveTextView] : 104 -> 108
~ -[MFComposeRecipientTextViewAccessibility _didRemoveRecipient:] : 268 -> 284
~ +[MFComposeStyleSelectorButtonAccessibility _accessibilityPerformValidations:] : 100 -> 112
~ -[MFComposeStyleSelectorButtonAccessibility accessibilityLabel] : 372 -> 380
~ +[MFComposeStyleSelectorViewControllerAccessibility _accessibilityPerformValidations:] : 140 -> 148
~ ___74-[MFComposeStyleSelectorViewControllerAccessibility changeFontSizeAction:]_block_invoke : 132 -> 136
~ +[MFComposeSubjectViewAccessibility _accessibilityPerformValidations:] : 220 -> 228
~ -[MFComposeSubjectViewAccessibility _accessibilityLoadAccessibilityInformation] : 216 -> 232
~ -[MFComposeSubjectViewAccessibility setNotifyOptionSelected:] : 148 -> 152
~ -[MFComposeTextColorButtonAccessibility accessibilityValue] : 184 -> 196
~ +[MFComposeWebViewAccessibility _accessibilityPerformValidations:] : 268 -> 276
~ -[MFComposeWebViewAccessibility _accessibilityLoadAccessibilityInformation] : 1216 -> 1252
~ -[MFHeaderLabelViewAccessibility isAccessibilityElement] : 76 -> 80
~ -[MFHeaderLabelViewAccessibility accessibilityRespondsToUserInteraction] : 116 -> 120
~ -[MFHeaderLabelViewAccessibility accessibilityHint] : 112 -> 120
~ -[MFComposeRecipientViewAccessibility _reflowAnimated:] : 132 -> 140
~ -[MFComposeRecipientViewAccessibility removeRecipient:] : 212 -> 224
~ +[MFMailComposeViewAccessibility _accessibilityPerformValidations:] : 864 -> 872
~ -[MFMailComposeViewAccessibility _accessibilityLoadAccessibilityInformation] : 552 -> 584
~ -[MFMailComposeViewAccessibility _accessibilityCompareElement:toElement:] : 592 -> 600
~ -[MFMailComposeViewAccessibility _accessibilityComposeElementsForSorting] : 484 -> 536
~ -[MFMailComposeViewAccessibility _searchResultsTable] : 104 -> 108
~ -[MFMailComposeViewAccessibility dragSource:draggableItemsAtPoint:] : 236 -> 244
~ -[MFMailComposeViewAccessibility dropTarget:dragEnteredAtPoint:] : 504 -> 544
~ -[MFMailComposeViewAccessibility dropTarget:dragDidMoveToPoint:] : 1016 -> 1052
~ -[MFMailComposeViewAccessibility _axIndexOfRecipient:inArray:] : 304 -> 300
~ ___62-[MFMailComposeViewAccessibility _axIndexOfRecipient:inArray:]_block_invoke : 200 -> 216
~ +[MFModernAddressAtomAccessibility _accessibilityPerformValidations:] : 224 -> 232
~ -[MFModernAddressAtomAccessibility accessibilityLabel] : 156 -> 172
~ -[MFModernAddressAtomAccessibility accessibilityHint] : 116 -> 124
~ -[MFModernAtomViewAccessibility accessibilityLabel] : 272 -> 296
~ +[MFModernComposeRecipientAtomAccessibility _accessibilityPerformValidations:] : 264 -> 272
~ -[MFModernComposeRecipientAtomAccessibility accessibilityHint] : 100 -> 104
~ -[MFModernComposeRecipientAtomAccessibility accessibilityLabel] : 404 -> 444
~ -[MFModernComposeRecipientAtomAccessibility _axMFAddressIsSafeDomain] : 180 -> 200
~ +[MFModernLabelledAtomListAccessibility _accessibilityPerformValidations:] : 156 -> 168
~ -[MFModernLabelledAtomListAccessibility _accessibilitySpeakThisString] : 232 -> 252
~ -[MFModernLabelledAtomListAccessibility accessibilityElements] : 236 -> 248
~ +[MFPhotoPickerControllerAccessibility _accessibilityPerformValidations:] : 236 -> 244
~ -[MFPhotoPickerControllerAccessibility _accessibilityLoadAccessibilityInformation] : 256 -> 280
~ -[MFPhotoPickerControllerAccessibility collectionView:cellForItemAtIndexPath:] : 336 -> 356
~ -[MFPhotoPickerControllerAccessibility viewDidLoad] : 200 -> 212
~ -[MFRecipientTableViewCellAccessibility accessibilityLabel] : 496 -> 512
~ ___59-[MFRecipientTableViewCellAccessibility accessibilityLabel]_block_invoke : 184 -> 196
~ -[UIViewAccessibility__MessageUI__UIKit _accessibilityOverridesInvisibility] : 212 -> 216
~ +[UITableViewAccessibility__MessageUI__UIKit _accessibilityPerformValidations:] : 136 -> 144
~ -[UITableViewAccessibility__MessageUI__UIKit accessibilityViewIsModal] : 120 -> 124
~ -[UITableViewAccessibility__MessageUI__UIKit _accessibilityObscuredScreenAllowedViews] : 292 -> 320
~ _accessibilityLocalizedString : 156 -> 164
~ -[WebAccessibilityObjectWrapperAccessibility__MessageUI__WebCore _axIsAttachmentType] : 104 -> 108
~ -[WebAccessibilityObjectWrapperAccessibility__MessageUI__WebCore accessibilityLabel] : 148 -> 160
~ -[WebAccessibilityObjectWrapperAccessibility__MessageUI__WebCore accessibilityValue] : 148 -> 160
~ -[WebAccessibilityObjectWrapperAccessibility__MessageUI__WebCore accessibilityHint] : 148 -> 160
~ -[UIDimmingViewAccessibility__MessageUI__UIKit passthroughViews] : 196 -> 212
~ ___64-[UIDimmingViewAccessibility__MessageUI__UIKit passthroughViews]_block_invoke : 128 -> 132
~ -[UITextViewAccessibility__MessageUI__UIKit accessibilityLabel] : 252 -> 272
~ -[UITextViewAccessibility__MessageUI__UIKit accessibilityFrame] : 312 -> 324
~ +[_MFAtomFieldEditorAccessibility _accessibilityPerformValidations:] : 168 -> 176
~ -[_MFAtomFieldEditorAccessibility _axAtomTextViewAncestor] : 148 -> 156
~ -[_MFAtomFieldEditorAccessibility accessibilityTraits] : 128 -> 132
~ -[_MFAtomFieldEditorAccessibility accessibilityPlaceholderValue] : 196 -> 212
~ -[_MFAtomFieldEditorAccessibility _accessibilityCanBeFirstResponder] : 208 -> 216
~ -[_MFAtomTextViewAccessibility accessibilityLabel] : 352 -> 376
~ -[_MFAtomTextViewAccessibility accessibilityValue] : 548 -> 580
~ ___50-[_MFAtomTextViewAccessibility accessibilityValue]_block_invoke : 96 -> 100
~ +[MFMailComposeControllerAccessibility _accessibilityPerformValidations:] : 220 -> 228
~ -[MFMailComposeControllerAccessibility _accessibilityLoadAccessibilityInformation] : 204 -> 220
~ ___60-[MFMailComposeControllerAccessibility _composeViewDidDraw:]_block_invoke : 104 -> 108
CStrings:
+ "axSafelyAddObject:"

```
