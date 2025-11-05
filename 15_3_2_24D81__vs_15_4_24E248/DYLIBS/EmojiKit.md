## EmojiKit

> `/System/iOSSupport/System/Library/PrivateFrameworks/EmojiKit.framework/Versions/A/EmojiKit`

```diff

 42.0.0.0.0
-  __TEXT.__text: 0xc9e8
-  __TEXT.__auth_stubs: 0x700
-  __TEXT.__objc_methlist: 0xef4
+  __TEXT.__text: 0xc9d0
+  __TEXT.__auth_stubs: 0x6f0
+  __TEXT.__objc_methlist: 0x10ac
   __TEXT.__const: 0x160
   __TEXT.__oslogstring: 0x530
   __TEXT.__cstring: 0x408
-  __TEXT.__gcc_except_tab: 0x190
+  __TEXT.__gcc_except_tab: 0x194
   __TEXT.__ustring: 0x4
   __TEXT.__unwind_info: 0x450
   __TEXT.__objc_classname: 0x217

   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xd28
+  __DATA_CONST.__objc_selrefs: 0xdc8
   __DATA_CONST.__objc_superrefs: 0x70
   __DATA_CONST.__objc_arraydata: 0x10
-  __AUTH_CONST.__auth_got: 0x390
+  __AUTH_CONST.__auth_got: 0x388
   __AUTH_CONST.__const: 0xa0
   __AUTH_CONST.__cfstring: 0x2a0
-  __AUTH_CONST.__objc_const: 0x2380
+  __AUTH_CONST.__objc_const: 0x2068
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH.__objc_data: 0x500

   - /System/iOSSupport/System/Library/Frameworks/UIKit.framework/Versions/A/UIKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 0A0A481B-0E37-3E86-9CC1-06368328C729
-  Functions: 344
-  Symbols:   1195
+  UUID: 589C164B-5901-37CA-A738-1C2A24A883F9
+  Functions: 348
+  Symbols:   1198
   CStrings:  816
 
Symbols:
+ +[_EMKTextKit2Controller log].cold.1
+ -[EMKOverlayView drawBackground:].cold.1
+ -[EMKTextEnumerator enumerateEmojiSignifiersInString:touchingRange:language:usingBlock:].cold.1
+ darkBackgroundColor.cold.1
- _objc_retain_x26
Functions:
~ -[EMKOverlayView drawBackground:] : 492 -> 476
~ -[EMKOverlayView drawForeground:] : 456 -> 448
~ _darkBackgroundColor : 84 -> 68
~ ___81-[NSTextLayoutManager(Helper) _enumerateTextLineFragmentsInTextRange:usingBlock:]_block_invoke : 744 -> 736
~ ___69-[NSTextLayoutManager(Helper) _enumerateAllTokenListsUsingBlock_emk:]_block_invoke_2 : 300 -> 296
~ ___48-[EMKTextView(Helper) _setTokenListsHidden_emk:]_block_invoke : 172 -> 176
~ -[_EMKTouchInfo tokenListRange] : 56 -> 60
~ -[_EMKTouchInfo frame] : 60 -> 64
~ +[_EMKTextKit2Controller log] : 84 -> 68
~ -[_EMKTextKit2Controller updateEmojiDisplay:] : 84 -> 88
~ -[_EMKTextKit2Controller _startOrStopAnimation] : 592 -> 588
~ -[_EMKTextKit2Controller __stopAnimation] : 256 -> 244
~ -[_EMKTextKit2Controller __startAnimation] : 568 -> 564
~ -[_EMKTextKit2Controller touchHasEmojiSignificance:] : 1264 -> 1252
~ __52-[_EMKTextKit2Controller touchHasEmojiSignificance:]_block_invoke.59 : 448 -> 452
~ -[_EMKTextKit2Controller textTapGestureRecognized:] : 708 -> 712
~ -[_EMKTextKit2Controller replaceRange:withEmojiToken:language:] : 1120 -> 1108
~ -[_EMKTextKit2Controller textContentStorage:textParagraphWithRange:] : 208 -> 216
~ -[_EMKTextLayoutFragmentView ___drawAnimatingEmojiGlyph:textPosition:glyphPosition:font:attributes:] : 528 -> 520
~ -[NSShadow(Helper) applyToGraphicsContext_emk:] : 168 -> 160
~ -[EMKTextEnumerator enumerateEmojiSignifiersInString:touchingRange:language:usingBlock:] : 456 -> 440
~ -[EMKLayoutManager startOrStopTimer] : 212 -> 220
~ -[EMKLayoutManager isEmojiAnimationActive] : 164 -> 172
~ -[EMKLayoutManager setEmojiConversionEnabled:] : 188 -> 192
~ -[EMKLayoutManager drawGlyphsForGlyphRange:atPoint:] : 116 -> 112
~ -[EMKTextView isEmojiConversionEnabled] : 104 -> 92
~ -[EMKTextView touchHasEmojiSignificance:] : 548 -> 552

```
