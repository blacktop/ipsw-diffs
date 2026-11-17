## QuickLookUICore

> `/System/Library/PrivateFrameworks/QuickLookUICore.framework/QuickLookUICore`

```diff

-1034.2.4.0.0
-  __TEXT.__text: 0x20b28
+1034.2.6.0.0
+  __TEXT.__text: 0x234a4
   __TEXT.__delay_stubs: 0x1c0
   __TEXT.__delay_helper: 0x25c
-  __TEXT.__objc_methlist: 0x31ac
-  __TEXT.__const: 0xf0
-  __TEXT.__cstring: 0x2073
-  __TEXT.__gcc_except_tab: 0x868
-  __TEXT.__oslogstring: 0x1892
-  __TEXT.__unwind_info: 0xcb0
+  __TEXT.__objc_methlist: 0x324c
+  __TEXT.__const: 0x148
+  __TEXT.__cstring: 0x2110
+  __TEXT.__gcc_except_tab: 0x8d8
+  __TEXT.__oslogstring: 0x193f
+  __TEXT.__ustring: 0x12
+  __TEXT.__unwind_info: 0xd28
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x900
+  __DATA_CONST.__const: 0x9a0
   __DATA_CONST.__objc_classlist: 0x128
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0xa0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2138
+  __DATA_CONST.__objc_selrefs: 0x22e8
   __DATA_CONST.__objc_superrefs: 0xc8
-  __DATA_CONST.__got: 0x4e0
-  __AUTH_CONST.__const: 0x1f0
-  __AUTH_CONST.__cfstring: 0x20a0
+  __DATA_CONST.__got: 0x560
+  __AUTH_CONST.__const: 0x210
+  __AUTH_CONST.__cfstring: 0x22c0
   __AUTH_CONST.__objc_const: 0x7718
-  __AUTH_CONST.__objc_intobj: 0x138
+  __AUTH_CONST.__objc_doubleobj: 0x10
+  __AUTH_CONST.__objc_intobj: 0x150
   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x960
   __DATA.__objc_ivar: 0x3bc

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1038
-  Symbols:   2163
-  CStrings:  413
+  Functions: 1064
+  Symbols:   2212
+  CStrings:  435
 
Symbols:
+ +[QLTextItemTransformer attributedStringFromData:encoding:typeIdentifier:documentURL:error:]
+ +[QLTextItemTransformer attributesForBlock:inlineIntent:baseFont:columnWidths:]
+ +[QLTextItemTransformer cachedAttributesForBlock:inlineIntent:baseFont:columnWidths:cache:]
+ +[QLTextItemTransformer columnWidthsInParsedMarkdown:baseFont:]
+ +[QLTextItemTransformer isSafeLink:]
+ +[QLTextItemTransformer markdownFromData:encoding:]
+ +[QLTextItemTransformer markdownFromData:encoding:documentURL:]
+ +[QLTextItemTransformer markerForListItem:]
+ +[QLTextItemTransformer separatorFromBlock:toBlock:]
+ +[QLTextItemTransformer shouldRenderMarkdownSource:]
+ +[QLTextItemTransformer styledStringFromParsedMarkdown:baseFont:documentURL:]
+ +[QLTextItemTransformer takeTaskListMarker:]
+ +[QLTextItemTransformer wrapperFromData:encoding:typeIdentifier:documentURL:error:]
+ GCC_except_table24
+ _NSImageURLAttributeName
+ _NSInlinePresentationIntentAttributeName
+ _NSLinkAttributeName
+ _NSParagraphStyleAttributeName
+ _NSPresentationIntentAttributeName
+ _NSStrikethroughStyleAttributeName
+ _NSURLIsRegularFileKey
+ _OBJC_CLASS_$_NSAttributedStringMarkdownParsingOptions
+ _OBJC_CLASS_$_NSConstantDoubleNumber
+ _OBJC_CLASS_$_NSMutableAttributedString
+ _OBJC_CLASS_$_NSMutableParagraphStyle
+ _OBJC_CLASS_$_NSMutableString
+ _OBJC_CLASS_$_NSTextAttachment
+ _OBJC_CLASS_$_NSTextTab
+ _OBJC_CLASS_$_NSURLComponents
+ _QLEnclosingIntentOfKind
+ _QLEnclosingRowIntent
+ _QLIntentDepthOfKind
+ _QLMarkdownFenceRunLength
+ _QLMarkdownLineWithoutFenceIndent
+ _UIFontWeightSemibold
+ _UTTypeMarkdown
+ ___36+[QLTextItemTransformer isSafeLink:]_block_invoke
+ ___52+[QLTextItemTransformer shouldRenderMarkdownSource:]_block_invoke
+ ___63+[QLTextItemTransformer columnWidthsInParsedMarkdown:baseFont:]_block_invoke
+ ___77+[QLTextItemTransformer styledStringFromParsedMarkdown:baseFont:documentURL:]_block_invoke
+ ___block_descriptor_128_e8_32s40s48s56s64s72s80r88r96r104r112r_e41_v40?0"NSDictionary"8{_NSRange=QQ}16^B32ls32l8s40l8s48l8s56l8r80l8s64l8r88l8r96l8r104l8r112l8s72l8
+ ___block_descriptor_64_e8_32s40bs48r56r_e41_v40?0"NSDictionary"8{_NSRange=QQ}16^B32lr48l8s40l8r56l8s32l8
+ ___block_descriptor_64_e8_32s40r48r56r_e52_v56?0"NSString"8{_NSRange=QQ}16{_NSRange=QQ}32^B48lr40l8s32l8r48l8r56l8
+ ___block_descriptor_72_e8_32s40s48s56r64r_e5_v8?0lr56l8r64l8s32l8s40l8s48l8
+ _attachmentsByteLimit
+ _attachmentsTotalByteLimit
+ _attributesForBlock:inlineIntent:baseFont:columnWidths:.scales
+ _isSafeLink:.allowedSchemes
+ _isSafeLink:.onceToken
CStrings:
+ "\t"
+ "\n"
+ "\n\n"
+ "%ld.\t"
+ "%ld.%lu"
+ "/"
+ "Could not parse Markdown, showing the source instead: %@ #AnyItemViewController"
+ "Markdown beyond its size or nesting limit, showing the source instead #AnyItemViewController"
+ "["
+ "ftp"
+ "ftps"
+ "http"
+ "https"
+ "mailto"
+ "q"
+ "sms"
+ "tel"
+ "v40@?0@\"NSDictionary\"8{_NSRange=QQ}16^B32"
+ "v56@?0@\"NSString\"8{_NSRange=QQ}16{_NSRange=QQ}32^B48"
+ "•\t"
+ "☐\t"
+ "☑\t"
```
