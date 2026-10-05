## EmojiKit

> `/System/Library/PrivateFrameworks/EmojiKit.framework/EmojiKit`

```diff

-43.0.0.0.0
-  __TEXT.__text: 0xc5a4
-  __TEXT.__objc_methlist: 0x10ac
+44.0.0.0.0
+  __TEXT.__text: 0xc79c
+  __TEXT.__objc_methlist: 0x10ec
   __TEXT.__const: 0x160
   __TEXT.__oslogstring: 0x530
-  __TEXT.__cstring: 0x427
-  __TEXT.__gcc_except_tab: 0x150
+  __TEXT.__cstring: 0x488
+  __TEXT.__gcc_except_tab: 0x15c
   __TEXT.__ustring: 0x4
-  __TEXT.__unwind_info: 0x500
+  __TEXT.__unwind_info: 0x510
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x520
-  __DATA_CONST.__objc_classlist: 0x80
+  __DATA_CONST.__const: 0x540
+  __DATA_CONST.__objc_classlist: 0x88
   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xdc8
+  __DATA_CONST.__objc_selrefs: 0xdf8
   __DATA_CONST.__objc_superrefs: 0x70
   __DATA_CONST.__objc_arraydata: 0x10
-  __DATA_CONST.__got: 0x1a8
-  __AUTH_CONST.__const: 0xa0
-  __AUTH_CONST.__cfstring: 0x2a0
-  __AUTH_CONST.__objc_const: 0x2068
+  __DATA_CONST.__got: 0x1e0
+  __AUTH_CONST.__const: 0xc0
+  __AUTH_CONST.__cfstring: 0x320
+  __AUTH_CONST.__objc_const: 0x20f8
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__auth_got: 0x390
-  __AUTH.__objc_data: 0x320
+  __AUTH.__objc_data: 0x370
   __DATA.__objc_ivar: 0x16c
   __DATA.__data: 0x1e0
   __DATA_DIRTY.__objc_data: 0x1e0

   - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/PrivateFrameworks/CoreEmoji.framework/CoreEmoji
   - /System/Library/PrivateFrameworks/EmojiFoundation.framework/EmojiFoundation
+  - /System/Library/PrivateFrameworks/InputAnalytics.framework/InputAnalytics
   - /System/Library/PrivateFrameworks/UIFoundation.framework/UIFoundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 348
-  Symbols:   826
-  CStrings:  76
+  Functions: 354
+  Symbols:   845
+  CStrings:  80
 
Symbols:
+ +[EMKInputAnalyticsHelper _reportUsageType:]
+ +[EMKInputAnalyticsHelper reportAccepted]
+ +[EMKInputAnalyticsHelper reportHighlightShown]
+ +[EMKInputAnalyticsHelper reportSuggestionShown]
+ -[_EMKTextKit2Controller _reportHighlightsShown]
+ GCC_except_table38
+ GCC_except_table45
+ _IAChannelGenmoji
+ _IAPayloadKeyGenmojiImageType
+ _IAPayloadKeyGenmojiUsageSource
+ _IAPayloadKeyGenmojiUsageType
+ _IAPayloadValueGenmojiImageTypeEmoji
+ _IASignalGenmojiUsage
+ _OBJC_CLASS_$_EMKInputAnalyticsHelper
+ _OBJC_CLASS_$_IASignalAnalytics
+ _OBJC_METACLASS_$_EMKInputAnalyticsHelper
+ __OBJC_$_CLASS_METHODS_EMKInputAnalyticsHelper
+ __OBJC_CLASS_RO_$_EMKInputAnalyticsHelper
+ __OBJC_METACLASS_RO_$_EMKInputAnalyticsHelper
+ ___48-[_EMKTextKit2Controller _reportHighlightsShown]_block_invoke
+ ___block_descriptor_32_e42_B32?0"EMKEmojiTokenList"8{_NSRange=QQ}16l
- GCC_except_table36
- GCC_except_table43
CStrings:
+ "FindAndReplace"
+ "FindAndReplaceAccepted"
+ "FindAndReplaceHighlightShown"
+ "FindAndReplaceSuggestionShown"
```
