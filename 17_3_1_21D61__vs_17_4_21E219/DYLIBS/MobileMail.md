## MobileMail

> `/System/Library/AccessibilityBundles/MobileMail.axbundle/MobileMail`

```diff

-2909.1.4.18.0
-  __TEXT.__text: 0x11ff4
-  __TEXT.__auth_stubs: 0x6a0
+2909.23.0.0.0
+  __TEXT.__text: 0x12144
+  __TEXT.__auth_stubs: 0x690
   __TEXT.__objc_methlist: 0x1768
   __TEXT.__const: 0x20
-  __TEXT.__cstring: 0x3395
+  __TEXT.__cstring: 0x33e5
   __TEXT.__oslogstring: 0x5a
-  __TEXT.__gcc_except_tab: 0x284
+  __TEXT.__gcc_except_tab: 0x294
   __TEXT.__ustring: 0xa
-  __TEXT.__unwind_info: 0x6d4
+  __TEXT.__unwind_info: 0x6e0
   __TEXT.__objc_classname: 0x12c5
-  __TEXT.__objc_methname: 0x2d40
-  __TEXT.__objc_methtype: 0x23c
-  __TEXT.__objc_stubs: 0x2740
+  __TEXT.__objc_methname: 0x2d48
+  __TEXT.__objc_methtype: 0x22b
+  __TEXT.__objc_stubs: 0x2760
   __DATA_CONST.__got: 0x98
   __DATA_CONST.__const: 0x660
   __DATA_CONST.__objc_classlist: 0x380
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x2008
-  __DATA_CONST.__objc_selrefs: 0xd08
+  __DATA_CONST.__objc_selrefs: 0xd10
+  __DATA_CONST.__objc_classrefs: 0x198
+  __DATA_CONST.__objc_superrefs: 0x148
   __DATA_CONST.__objc_arraydata: 0x10
-  __AUTH_CONST.__cfstring: 0x4500
+  __AUTH_CONST.__cfstring: 0x4540
   __AUTH_CONST.__const: 0x500
   __AUTH_CONST.__objc_const: 0x1f78
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH_CONST.__auth_got: 0x360
+  __AUTH_CONST.__auth_got: 0x358
   __AUTH.__objc_data: 0x140
-  __DATA.__objc_classrefs: 0x198
-  __DATA.__objc_superrefs: 0x148
   __DATA.__objc_ivar: 0x4
   __DATA.__bss: 0x6
   __DATA_DIRTY.__objc_data: 0x21c0

   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 512
-  Symbols:   2199
-  CStrings:  1166
+  Functions: 515
+  Symbols:   2206
+  CStrings:  1168
 
Symbols:
+ -[MessageStatusIndicatorManagerAccessibility _accessibilitySetImageNameForImage:options:]
+ -[MessageStatusIndicatorManagerAccessibility _axValueForMask:]
+ -[MessageStatusIndicatorManagerAccessibility statusIndicatorImageWithOptionsMask:]
+ GCC_except_table4
+ ___49+[AXMobileMailGlue accessibilityInitializeBundle]_block_invoke.493
+ ___50-[MailActionCellAccessibility accessibilityTraits]_block_invoke.274
+ ___62-[MessageStatusIndicatorManagerAccessibility _axValueForMask:]_block_invoke
+ ___69-[MFConversationViewCellAccessibility _accessibilityMailSwipeActions]_block_invoke.292
+ ___accessibilityApproximateVisibleSummaryText_block_invoke.296
+ ___block_literal_global.255
+ ___block_literal_global.257
+ ___block_literal_global.262
+ ___block_literal_global.309
+ ___block_literal_global.321
+ ___block_literal_global.343
+ ___block_literal_global.476
+ ___block_literal_global.487
+ ___block_literal_global.496
+ ___block_literal_global.517
+ ___block_literal_global.519
+ ___block_literal_global.528
+ ___block_literal_global.531
+ ___block_literal_global.532
+ ___block_literal_global.536
+ ___block_literal_global.554
+ ___block_literal_global.556
+ ___block_literal_global.563
+ ___block_literal_global.646
+ ___block_literal_global.652
+ ___block_literal_global.681
+ __unnamed_array_storage.272
+ _objc_msgSend$_accessibilitySetImageNameForImage:options:
+ _objc_msgSend$_axValueForMask:
+ _objc_msgSend$statusIndicatorColorWithOptionsMask:
- -[MessageStatusIndicatorManagerAccessibility _accessibilitySetImageNameForImage:options:flagColor:]
- -[MessageStatusIndicatorManagerAccessibility _axValueForMask:flagColor:]
- -[MessageStatusIndicatorManagerAccessibility statusIndicatorImageWithOptionsMask:flagColor:]
- ___49+[AXMobileMailGlue accessibilityInitializeBundle]_block_invoke.469
- ___50-[MailActionCellAccessibility accessibilityTraits]_block_invoke.250
- ___69-[MFConversationViewCellAccessibility _accessibilityMailSwipeActions]_block_invoke.268
- ___accessibilityApproximateVisibleSummaryText_block_invoke.272
- ___block_literal_global.231
- ___block_literal_global.233
- ___block_literal_global.238
- ___block_literal_global.285
- ___block_literal_global.297
- ___block_literal_global.319
- ___block_literal_global.452
- ___block_literal_global.463
- ___block_literal_global.472
- ___block_literal_global.485
- ___block_literal_global.490
- ___block_literal_global.492
- ___block_literal_global.495
- ___block_literal_global.501
- ___block_literal_global.505
- ___block_literal_global.507
- ___block_literal_global.529
- ___block_literal_global.530
- ___block_literal_global.539
- ___block_literal_global.622
- ___block_literal_global.628
- ___block_literal_global.657
- __unnamed_array_storage.248
- _objc_msgSend$_accessibilitySetImageNameForImage:options:flagColor:
- _objc_msgSend$_axValueForMask:flagColor:
- _objc_retain_x4
CStrings:
+ "_accessibilitySetImageNameForImage:options:"
+ "_axValueForMask:"
+ "displayMessageItemID"
+ "referenceMessageListItem"
+ "referenceMessageListItem.displayMessageItemID"
+ "statusIndicatorColorWithOptionsMask:"
+ "statusIndicatorImageWithOptionsMask:"
+ "v32@0:8@16Q24"
- "@32@0:8Q16@24"
- "_accessibilitySetImageNameForImage:options:flagColor:"
- "_axValueForMask:flagColor:"
- "_referenceDisplayMessage.itemID"
- "itemID"
- "statusIndicatorImageWithOptionsMask:flagColor:"
- "v40@0:8@16Q24@32"

```
