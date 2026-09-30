## MessageUI

> `/System/Library/Frameworks/MessageUI.framework/MessageUI`

```diff

-3864.300.11.2.1
-  __TEXT.__text: 0x125684
+3864.300.22.2.1
+  __TEXT.__text: 0x1257ec
   __TEXT.__auth_stubs: 0x24e0
   __TEXT.__delay_helper: 0xec
   __TEXT.__objc_methlist: 0x1260c
-  __TEXT.__gcc_except_tab: 0x2510c
+  __TEXT.__gcc_except_tab: 0x2515c
   __TEXT.__cstring: 0x9be4
   __TEXT.__const: 0x15a4
-  __TEXT.__oslogstring: 0x5533
+  __TEXT.__oslogstring: 0x5583
   __TEXT.__dlopen_cstrs: 0x40d
   __TEXT.__ustring: 0x4dc
   __TEXT.__swift5_typeref: 0x612

   __TEXT.__unwind_info: 0x9e10
   __TEXT.__eh_frame: 0x328
   __TEXT.__objc_classname: 0x2192
-  __TEXT.__objc_methname: 0x34e35
+  __TEXT.__objc_methname: 0x34e62
   __TEXT.__objc_methtype: 0xba35
-  __TEXT.__objc_stubs: 0x22f80
+  __TEXT.__objc_stubs: 0x22fc0
   __DATA_CONST.__got: 0x1c80
   __DATA_CONST.__const: 0x4708
   __DATA_CONST.__objc_classlist: 0x608
   __DATA_CONST.__objc_catlist: 0x108
   __DATA_CONST.__objc_protolist: 0x410
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xbf98
+  __DATA_CONST.__objc_selrefs: 0xbfa0
   __DATA_CONST.__objc_protorefs: 0x68
   __DATA_CONST.__objc_superrefs: 0x4a8
   __DATA_CONST.__objc_arraydata: 0x628

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 005DC4B3-1675-3415-A68C-17A9DDD7C5B3
+  UUID: 2962EC3B-12D2-35B9-9F9F-A7E19085A166
   Functions: 6187
-  Symbols:   24041
-  CStrings:  12518
+  Symbols:   24043
+  CStrings:  12520
 
Symbols:
+ ___70-[MFMailComposeController _originalContentOfMessagesInReplyToMessage:]_block_invoke.1299
+ ___70-[MFMailComposeController _originalContentOfMessagesInReplyToMessage:]_block_invoke_2.1300
+ ___70-[MFMailComposeController _originalContentOfMessagesInReplyToMessage:]_block_invoke_3.1301
+ ___block_literal_global.1083
+ ___block_literal_global.1110
+ ___block_literal_global.1298
+ _objc_msgSend$forceSaveAsDraft
+ _objc_msgSend$mailComposeControllerShouldSaveDraftOnClose:
- ___70-[MFMailComposeController _originalContentOfMessagesInReplyToMessage:]_block_invoke.1297
- ___70-[MFMailComposeController _originalContentOfMessagesInReplyToMessage:]_block_invoke_2.1298
- ___70-[MFMailComposeController _originalContentOfMessagesInReplyToMessage:]_block_invoke_3.1299
- ___block_literal_global.1081
- ___block_literal_global.1108
- ___block_literal_global.1296
Functions:
~ -[MFMailComposeController viewDidDisappear:] : 640 -> 1000
CStrings:
+ "%p: [Draft] %{public}@ on unfinished compose and delegate wants to save the draft."
+ "mailComposeControllerShouldSaveDraftOnClose:"

```
