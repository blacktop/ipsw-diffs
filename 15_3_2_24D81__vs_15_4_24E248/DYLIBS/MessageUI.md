## MessageUI

> `/System/iOSSupport/System/Library/Frameworks/MessageUI.framework/Versions/A/MessageUI`

```diff

-3826.400.131.1.6
-  __TEXT.__text: 0x45b70
+3826.500.181.1.5
+  __TEXT.__text: 0x458b0
   __TEXT.__auth_stubs: 0xc50
-  __TEXT.__objc_methlist: 0x452c
-  __TEXT.__gcc_except_tab: 0x8448
-  __TEXT.__cstring: 0x29f8
-  __TEXT.__const: 0x394
-  __TEXT.__oslogstring: 0x32d
+  __TEXT.__objc_methlist: 0x5d34
+  __TEXT.__gcc_except_tab: 0x8468
+  __TEXT.__cstring: 0x29d8
+  __TEXT.__const: 0x3d4
+  __TEXT.__oslogstring: 0x374
   __TEXT.__ustring: 0x10
   __TEXT.__swift5_typeref: 0x7c
   __TEXT.__constg_swiftt: 0x154
   __TEXT.__swift5_reflstr: 0x4d
   __TEXT.__swift5_fieldmd: 0x88
   __TEXT.__swift5_types: 0x10
-  __TEXT.__unwind_info: 0x2900
+  __TEXT.__unwind_info: 0x2918
   __TEXT.__eh_frame: 0x178
   __TEXT.__objc_classname: 0x98c
-  __TEXT.__objc_methname: 0x110a8
-  __TEXT.__objc_methtype: 0x350e
+  __TEXT.__objc_methname: 0x11215
+  __TEXT.__objc_methtype: 0x365b
   __TEXT.__objc_stubs: 0xae60
-  __DATA_CONST.__got: 0x7b8
-  __DATA_CONST.__const: 0x17d0
+  __DATA_CONST.__got: 0x7c8
+  __DATA_CONST.__const: 0x1770
   __DATA_CONST.__objc_classlist: 0x230
   __DATA_CONST.__objc_catlist: 0x80
   __DATA_CONST.__objc_protolist: 0xd0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3830
+  __DATA_CONST.__objc_selrefs: 0x4458
   __DATA_CONST.__objc_superrefs: 0x1a0
   __AUTH_CONST.__auth_got: 0x638
   __AUTH_CONST.__const: 0x360
-  __AUTH_CONST.__cfstring: 0x2640
-  __AUTH_CONST.__objc_const: 0xbcd8
+  __AUTH_CONST.__cfstring: 0x2600
+  __AUTH_CONST.__objc_const: 0x8fa8
   __AUTH_CONST.__objc_intobj: 0xa8
   __AUTH.__objc_data: 0x1748
   __AUTH.__data: 0x128

   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
-  - /usr/lib/swift/libswiftFileProvider.dylib
   - /usr/lib/swift/libswiftIOKit.dylib
   - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMetal.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 32AC9EFD-9F7D-33F1-BB07-C04D87CC4C35
-  Functions: 1759
-  Symbols:   5521
-  CStrings:  4053
+  UUID: A2C35174-3C9B-3003-B43A-BBCFF02BE75D
+  Functions: 1774
+  Symbols:   5536
+  CStrings:  4070
 
Symbols:
+ +[EFScheduler(MessageUI) __mui_nextRunLoopMainThreadScheduler].cold.1
+ +[MFContactsManager isAuthorizedToUseContacts].cold.1
+ +[MFContactsManager sharedManager].cold.1
+ +[MFFontMetricCache sharedFontMetricCache].cold.1
+ +[MFRecipientTableViewCell _deviceSpecificLayoutMargin].cold.1
+ +[MFRecipientTableViewCell _realDetailButtonAccessoryMargin].cold.1
+ +[_MFMessageObserver sharedObserver].cold.1
+ -[MFAtomTextView actionDelegate]
+ -[MFAtomTextView paragraphStyle].cold.1
+ -[MFAtomTextView setActionDelegate:]
+ -[MFMailComposeViewController insertCollaborationItemProvider:completionHandler:]
+ -[MFMailComposeViewController insertCollaborationItemProvider:completionHandler:].cold.1
+ -[MFModernAtomView _chevronTextAttachment].cold.1
+ GCC_except_table107
+ GCC_except_table152
+ GCC_except_table156
+ GCC_except_table157
+ GCC_except_table163
+ GCC_except_table189
+ GCC_except_table210
+ GCC_except_table211
+ GCC_except_table215
+ GCC_except_table221
+ GCC_except_table225
+ GCC_except_table226
+ GCC_except_table65
+ GCC_except_table73
+ MFLocalizedAddressSeparator.cold.1
+ initIMMessageSentDistributedNotification.cold.1
+ initIMMessageSentDistributedNotificationUserInfoMessageGUIDKey.cold.1
+ initIMMessageSentDistributedNotificationUserInfoSucessKey.cold.1
- GCC_except_table150
- GCC_except_table153
- GCC_except_table154
- GCC_except_table161
- GCC_except_table196
- GCC_except_table213
- GCC_except_table219
- GCC_except_table223
- GCC_except_table224
- _MFImageGlyphClose
- __swift_FORCE_LOAD_$_swiftFileProvider
- __swift_FORCE_LOAD_$_swiftFileProvider_$_MessageUI
CStrings:
+ "@\"UIConversationContext\"16@0:8"
+ "T@\"UIConversationContext\",?,&,N"
+ "_convertPointToRenderSpace:textPosition:"
+ "_insertAttributedText:withAnimation:completion:"
+ "_replaceRange:withAttributedText:usingAnimation:completion:"
+ "actionDelegate"
+ "conversationContext"
+ "insertCollaborationItemProvider is only available on the iOS platform."
+ "insertCollaborationItemProvider:completionHandler:"
+ "insertInputSuggestion:"
+ "setActionDelegate:"
+ "setConversationContext:"
+ "textView:insertInputSuggestion:"
+ "v24@0:8@\"UIConversationContext\"16"
+ "v24@0:8@\"UIInputSuggestion\"16"
+ "v32@0:8@\"UITextView\"16@\"UIInputSuggestion\"24"
+ "v40@0:8@\"NSAttributedString\"16q24@?<v@?>32"
+ "v40@0:8@16q24@?32"
+ "v48@0:8@\"UITextRange\"16@\"NSAttributedString\"24q32@?<v@?>40"
+ "v48@0:8@16@24q32@?40"
+ "{CGPoint=dd}40@0:8{CGPoint=dd}16@\"UITextPosition\"32"
- "person.slash.fill"
- "xmark.circle.fill"

```
