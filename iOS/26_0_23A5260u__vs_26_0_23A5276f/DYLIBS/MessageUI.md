## MessageUI

> `/System/Library/Frameworks/MessageUI.framework/MessageUI`

```diff

-3853.100.6.2.6
-  __TEXT.__text: 0x124668
+3856.100.4.0.0
+  __TEXT.__text: 0x124c44
   __TEXT.__auth_stubs: 0x24d0
   __TEXT.__delay_helper: 0xec
-  __TEXT.__objc_methlist: 0x12384
-  __TEXT.__gcc_except_tab: 0x252b4
+  __TEXT.__objc_methlist: 0x123d4
+  __TEXT.__gcc_except_tab: 0x25390
   __TEXT.__cstring: 0x9a94
   __TEXT.__const: 0x1414
-  __TEXT.__oslogstring: 0x52d3
+  __TEXT.__oslogstring: 0x53b3
   __TEXT.__dlopen_cstrs: 0x406
   __TEXT.__ustring: 0x4d2
   __TEXT.__swift5_typeref: 0x612

   __TEXT.__swift5_capture: 0x6c
   __TEXT.__swift_as_entry: 0x8
   __TEXT.__swift_as_ret: 0x8
-  __TEXT.__unwind_info: 0x9d70
+  __TEXT.__unwind_info: 0x9dc0
   __TEXT.__eh_frame: 0x328
   __TEXT.__objc_classname: 0x217d
-  __TEXT.__objc_methname: 0x342be
+  __TEXT.__objc_methname: 0x3438d
   __TEXT.__objc_methtype: 0xb556
-  __TEXT.__objc_stubs: 0x22ee0
+  __TEXT.__objc_stubs: 0x22f40
   __DATA_CONST.__got: 0x1c88
-  __DATA_CONST.__const: 0x4728
+  __DATA_CONST.__const: 0x4708
   __DATA_CONST.__objc_classlist: 0x608
   __DATA_CONST.__objc_catlist: 0x108
   __DATA_CONST.__objc_protolist: 0x408
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xbda8
+  __DATA_CONST.__objc_selrefs: 0xbde0
   __DATA_CONST.__objc_protorefs: 0x68
   __DATA_CONST.__objc_superrefs: 0x4a8
   __DATA_CONST.__objc_arraydata: 0x608
   __AUTH_CONST.__auth_got: 0x1278
   __AUTH_CONST.__const: 0x1200
   __AUTH_CONST.__cfstring: 0x8ce0
-  __AUTH_CONST.__objc_const: 0x19f00
+  __AUTH_CONST.__objc_const: 0x19f40
   __AUTH_CONST.__objc_intobj: 0x1b0
   __AUTH_CONST.__objc_dictobj: 0x550
   __AUTH_CONST.__objc_arrayobj: 0x78

   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH.__objc_data: 0x2da0
   __AUTH.__data: 0x190
-  __DATA.__objc_ivar: 0x10f8
+  __DATA.__objc_ivar: 0x1100
   __DATA.__data: 0x32b4
   __DATA.__bss: 0x17c8
   __DATA.__common: 0x2f8

   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
-  - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMLCompute.dylib

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: A9576633-D406-3548-B13F-2AF0A0074521
-  Functions: 6165
-  Symbols:   23981
-  CStrings:  12420
+  UUID: 1F36F12C-528C-3778-9DF9-FAF788A6A931
+  Functions: 6171
+  Symbols:   23999
+  CStrings:  12431
 
Symbols:
+ -[MFMailComposeController _addComposeToolbarIfNeeded]
+ -[MFMailComposeController _reportUserEngagement:suggestionService:warning:]
+ -[MFMailComposeController composeRecipientViewTabPressed:]
+ -[MFMailComposeController pressesBegan:withEvent:]
+ -[MFMailComposeController pressesCancelled:withEvent:]
+ -[MFMailComposeController pressesChanged:withEvent:]
+ -[MFMailComposeController pressesEnded:withEvent:]
+ -[MFMailComposeView focusFirstResponderBeforeRecipientView:]
+ GCC_except_table501
+ GCC_except_table516
+ GCC_except_table517
+ GCC_except_table539
+ GCC_except_table541
+ GCC_except_table545
+ GCC_except_table548
+ GCC_except_table554
+ GCC_except_table555
+ GCC_except_table562
+ GCC_except_table564
+ GCC_except_table566
+ GCC_except_table568
+ GCC_except_table579
+ GCC_except_table580
+ GCC_except_table582
+ GCC_except_table586
+ GCC_except_table589
+ GCC_except_table602
+ GCC_except_table604
+ GCC_except_table605
+ GCC_except_table611
+ GCC_except_table649
+ GCC_except_table656
+ GCC_except_table668
+ GCC_except_table674
+ GCC_except_table675
+ GCC_except_table676
+ GCC_except_table677
+ GCC_except_table678
+ GCC_except_table679
+ GCC_except_table793
+ GCC_except_table797
+ GCC_except_table798
+ GCC_except_table800
+ GCC_except_table801
+ GCC_except_table802
+ OBJC_IVAR_$_MFMailComposeController._bccField
+ _OBJC_IVAR_$_MFMailComposeController._currentKeyModifierFlags
+ ___70-[MFMailComposeController _originalContentOfMessagesInReplyToMessage:]_block_invoke.1295
+ ___70-[MFMailComposeController _originalContentOfMessagesInReplyToMessage:]_block_invoke_2.1296
+ ___70-[MFMailComposeController _originalContentOfMessagesInReplyToMessage:]_block_invoke_3.1297
+ ___75-[MFMailComposeController _reportUserEngagement:suggestionService:warning:]_block_invoke
+ ___block_literal_global.1081
+ ___block_literal_global.1111
+ ___block_literal_global.1294
+ _objc_msgSend$_addComposeToolbarIfNeeded
+ _objc_msgSend$_reportUserEngagement:suggestionService:warning:
+ _objc_msgSend$focusFirstResponderBeforeRecipientView:
+ _objc_msgSend$modifierFlags
- -[MFMailComposeController _reportUserEnagagement:suggestionService:warning:]
- GCC_except_table505
- GCC_except_table520
- GCC_except_table521
- GCC_except_table544
- GCC_except_table550
- GCC_except_table551
- GCC_except_table553
- GCC_except_table559
- GCC_except_table560
- GCC_except_table571
- GCC_except_table572
- GCC_except_table574
- GCC_except_table578
- GCC_except_table584
- GCC_except_table590
- GCC_except_table591
- GCC_except_table592
- GCC_except_table599
- GCC_except_table607
- GCC_except_table609
- GCC_except_table610
- GCC_except_table616
- GCC_except_table654
- GCC_except_table661
- GCC_except_table673
- GCC_except_table787
- GCC_except_table788
- GCC_except_table791
- GCC_except_table792
- GCC_except_table795
- GCC_except_table796
- ___70-[MFMailComposeController _originalContentOfMessagesInReplyToMessage:]_block_invoke.1288
- ___70-[MFMailComposeController _originalContentOfMessagesInReplyToMessage:]_block_invoke_2.1289
- ___70-[MFMailComposeController _originalContentOfMessagesInReplyToMessage:]_block_invoke_3.1290
- ___76-[MFMailComposeController _reportUserEnagagement:suggestionService:warning:]_block_invoke
- ___block_literal_global.1083
- ___block_literal_global.1105
- ___block_literal_global.1287
- __swift_FORCE_LOAD_$_swiftDarwin
- __swift_FORCE_LOAD_$_swiftDarwin_$_MessageUI
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_MessageUI
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_MessageUI
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_MessageUI
- _objc_msgSend$_reportUserEnagagement:suggestionService:warning:
CStrings:
+ "<%{public}@: %p> [Compose Toolbar] Compose toolbar already added"
+ "<%{public}@: %p> [Compose Toolbar] Device is not eligible for compose toolbar"
+ "<%{public}@: %p> [Compose Toolbar] Failed to add compose toolbar, stillLoading=%{public}@"
+ "_addComposeToolbarIfNeeded"
+ "_currentKeyModifierFlags"
+ "_reportUserEngagement:suggestionService:warning:"
+ "focusFirstResponderBeforeRecipientView:"
+ "modifierFlags"
+ "pressesBegan:withEvent:"
+ "pressesCancelled:withEvent:"
+ "pressesChanged:withEvent:"
+ "pressesEnded:withEvent:"
- "_reportUserEnagagement:suggestionService:warning:"

```
