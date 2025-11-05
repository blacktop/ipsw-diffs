## com.apple.MailUI

> `/System/Library/Accessibility/BundlesBase/com.apple.MailUI.axbundle/Versions/A/com.apple.MailUI`

```diff

-287.6.0.0.0
-  __TEXT.__text: 0x2b0c
+287.6.4.0.0
+  __TEXT.__text: 0x2928
   __TEXT.__auth_stubs: 0x180
-  __TEXT.__objc_stubs: 0x740
+  __TEXT.__objc_stubs: 0x720
   __TEXT.__objc_methlist: 0x290
   __TEXT.__objc_classname: 0x2c2
-  __TEXT.__cstring: 0x80c
-  __TEXT.__objc_methname: 0x72a
+  __TEXT.__cstring: 0x7c8
+  __TEXT.__objc_methname: 0x70d
   __TEXT.__objc_methtype: 0x5d
   __TEXT.__const: 0x18
   __TEXT.__gcc_except_tab: 0x80

   __DATA_CONST.__auth_got: 0xd0
   __DATA_CONST.__got: 0xa0
   __DATA_CONST.__const: 0x1d0
-  __DATA_CONST.__cfstring: 0xc40
+  __DATA_CONST.__cfstring: 0xbc0
   __DATA_CONST.__objc_classlist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x28
   __DATA.__objc_const: 0x990
-  __DATA.__objc_selrefs: 0x240
+  __DATA.__objc_selrefs: 0x238
   __DATA.__objc_data: 0x550
   __DATA.__bss: 0x20
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A9B63642-E00F-360A-B3A7-8D7AF2657074
-  Functions: 66
+  UUID: 27F200C6-AF0F-3494-837E-2421CE50BCF9
+  Functions: 67
   Symbols:   280
-  CStrings:  302
+  CStrings:  293
 
Symbols:
+ -[MUIRichMessageCellBaseAccessibility _accessibilityPriorityForChild:].cold.1
- _objc_msgSend$accessibilityRoleDescription
Functions:
~ -[MUITokenAddressFieldCellAccessibility accessibilitySharedFocusElements] : 584 -> 592
~ -[MUITokenAddressFieldCellAccessibility _axcTokenAddressField] : 200 -> 208
~ -[NSTableViewCellMockElementAccessibility__MailUI__AppKit accessibilityChildrenAttribute] : 500 -> 504
~ -[NSTableViewCellMockElementAccessibility__MailUI__AppKit accessibilityChildrenInNavigationOrderAttribute] : 500 -> 504
~ -[MessageStatusStackViewAccessibility isAccessibilityElement] : 256 -> 260
~ -[MessageStatusStackViewAccessibility accessibilityLabel] : 1108 -> 556
~ -[MUIAddressTokenAttachmentCellAccessibility accessibilityIdentifier] : 144 -> 148
~ -[MUIAddressFieldAccessibility _axcAddressTokenIconsForAddress:includeExternalAddressTokenIcon:] : 400 -> 404
~ -[MUIAddressFieldAccessibility tokenField:setUpTokenAttachmentCell:forRepresentedObject:] : 792 -> 816
~ -[MUIRichMessageCellBaseAccessibility _accessibilityPriorityForChild:] : 1308 -> 1296
CStrings:
+ "Mail.messageList.cell.view.statusStack"
- "NSButtonCell"
- "ReplyButtonCell"
- "_MV_RICH_LIST_STATUS_STACK"
- "_MV_RICH_LIST_STATUS_STACK_COLUMN_LAYOUT"
- "accessibilityRoleDescription"

```
