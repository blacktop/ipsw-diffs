## AXRuntime

> `/System/Library/PrivateFrameworks/AXRuntime.framework/AXRuntime`

```diff

-3189.2.0.0.0
-  __TEXT.__text: 0x49e4c
+3190.5.0.0.0
+  __TEXT.__text: 0x4a280
   __TEXT.__auth_stubs: 0x14b0
-  __TEXT.__objc_methlist: 0x36c0
-  __TEXT.__const: 0x458
-  __TEXT.__cstring: 0x5c26
+  __TEXT.__objc_methlist: 0x36a4
+  __TEXT.__const: 0x468
+  __TEXT.__cstring: 0x5c35
   __TEXT.__oslogstring: 0x12c1
   __TEXT.__gcc_except_tab: 0xb38
   __TEXT.__ustring: 0x4
   __TEXT.__dlopen_cstrs: 0x31a
   __TEXT.__unwind_info: 0x13f0
   __TEXT.__objc_classname: 0x349
-  __TEXT.__objc_methname: 0x7ad6
-  __TEXT.__objc_methtype: 0x138b
+  __TEXT.__objc_methname: 0x7aeb
+  __TEXT.__objc_methtype: 0x1364
   __TEXT.__objc_stubs: 0x5d20
   __DATA_CONST.__got: 0x2d0
-  __DATA_CONST.__const: 0x12b8
+  __DATA_CONST.__const: 0x12e0
   __DATA_CONST.__objc_classlist: 0xe0
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2260
+  __DATA_CONST.__objc_selrefs: 0x2268
   __DATA_CONST.__objc_superrefs: 0xa8
   __DATA_CONST.__objc_arraydata: 0xc0
   __AUTH_CONST.__auth_got: 0xa68
   __AUTH_CONST.__const: 0xba8
   __AUTH_CONST.__cfstring: 0x4f20
-  __AUTH_CONST.__objc_const: 0x3690
+  __AUTH_CONST.__objc_const: 0x3688
   __AUTH_CONST.__objc_intobj: 0x1620
   __AUTH_CONST.__objc_arrayobj: 0x90
   __AUTH_CONST.__objc_doubleobj: 0x20

   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 685CABB6-D969-3F42-9EAF-011E170070F6
+  UUID: A0F2E00B-D659-3A7A-B752-0BD5C71C488A
   Functions: 1756
-  Symbols:   5757
-  CStrings:  3187
+  Symbols:   5759
+  CStrings:  3188
 
Symbols:
+ -[AXUIElement nextCursorRangeInDirection:unit:outputRange:currentCursorRange:outputStyleSpeakToRight:]
+ ___102-[AXUIElement nextCursorRangeInDirection:unit:outputRange:currentCursorRange:outputStyleSpeakToRight:]_block_invoke
+ ___block_descriptor_40_e8_32s_e14_B28?0q8q16S24ls32l8
+ _kAXSnapshotItemContainerTrait
+ _objc_msgSend$letterCharacterSet
+ _objc_msgSend$whitespaceCharacterSet
- -[AXUIElement nextCursorRangeInDirection:unit:outputRange:]
- -[AXUIElement nextCursorRangeInDirection:unit:outputRange:currentCursorRange:]
- _objc_msgSend$_selectedTextRange
- _objc_msgSend$nextCursorRangeInDirection:unit:outputRange:currentCursorRange:
Functions:
~ _AXConvertOutgoingValue : 5824 -> 5840
~ -[AXUIElement nextCursorRangeInDirection:unit:outputRange:] -> -[AXUIElement _lineRangeWithFaultTolerance:forward:] : 96 -> 108
~ -[AXUIElement _lineRangeWithFaultTolerance:forward:] -> -[AXUIElement nextCursorRangeInDirection:unit:outputRange:currentCursorRange:outputStyleSpeakToRight:] : 108 -> 1944
~ -[AXUIElement nextCursorRangeInDirection:unit:outputRange:currentCursorRange:] -> ___102-[AXUIElement nextCursorRangeInDirection:unit:outputRange:currentCursorRange:outputStyleSpeakToRight:]_block_invoke : 1012 -> 224
CStrings:
+ "B28@?0q8q16S24"
+ "letterCharacterSet"
+ "nextCursorRangeInDirection:unit:outputRange:currentCursorRange:outputStyleSpeakToRight:"
+ "whitespaceCharacterSet"
+ "{_NSRange=QQ}60@0:8Q16Q24^{_NSRange=QQ}32{_NSRange=QQ}40B56"
- "nextCursorRangeInDirection:unit:outputRange:"
- "nextCursorRangeInDirection:unit:outputRange:currentCursorRange:"
- "{_NSRange=QQ}40@0:8Q16Q24^{_NSRange=QQ}32"
- "{_NSRange=QQ}56@0:8Q16Q24^{_NSRange=QQ}32{_NSRange=QQ}40"

```
