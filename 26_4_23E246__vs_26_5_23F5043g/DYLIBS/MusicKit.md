## MusicKit

> `/System/Library/Frameworks/MusicKit.framework/MusicKit`

```diff

-4025.510.2.0.0
-  __TEXT.__text: 0x5612bc
-  __TEXT.__auth_stubs: 0x2f50
-  __TEXT.__objc_methlist: 0x2234
-  __TEXT.__const: 0x50dc4
-  __TEXT.__gcc_except_tab: 0x2028
-  __TEXT.__cstring: 0x10b42
-  __TEXT.__dlopen_cstrs: 0xa7a
+4025.600.3.0.0
+  __TEXT.__text: 0x561e64
+  __TEXT.__auth_stubs: 0x2fc0
+  __TEXT.__objc_methlist: 0x224c
+  __TEXT.__const: 0x50e54
+  __TEXT.__gcc_except_tab: 0x1ff4
+  __TEXT.__cstring: 0x10b92
+  __TEXT.__dlopen_cstrs: 0xa32
   __TEXT.__oslogstring: 0x1892
   __TEXT.__swift5_typeref: 0x119de
   __TEXT.__swift5_reflstr: 0xbbdb

   __TEXT.__unwind_info: 0x171b8
   __TEXT.__eh_frame: 0x25e7c
   __TEXT.__objc_classname: 0x1487
-  __TEXT.__objc_methname: 0x7d43
-  __TEXT.__objc_methtype: 0x13ac
-  __TEXT.__objc_stubs: 0x5f00
-  __DATA_CONST.__got: 0x940
-  __DATA_CONST.__const: 0x1688
+  __TEXT.__objc_methname: 0x7d73
+  __TEXT.__objc_methtype: 0x147c
+  __TEXT.__objc_stubs: 0x5ec0
+  __DATA_CONST.__got: 0x958
+  __DATA_CONST.__const: 0x16c0
   __DATA_CONST.__objc_classlist: 0x308
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1b20
+  __DATA_CONST.__objc_selrefs: 0x1b10
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x168
   __DATA_CONST.__objc_arraydata: 0x168
-  __AUTH_CONST.__auth_got: 0x17b8
+  __AUTH_CONST.__auth_got: 0x17f0
   __AUTH_CONST.__const: 0x29250
-  __AUTH_CONST.__cfstring: 0xdc0
+  __AUTH_CONST.__cfstring: 0xe40
   __AUTH_CONST.__objc_const: 0x6e40
   __AUTH_CONST.__objc_doubleobj: 0x90
   __AUTH_CONST.__objc_arrayobj: 0x108

   __AUTH.__data: 0x3960
   __DATA.__objc_ivar: 0x160
   __DATA.__data: 0xa198
-  __DATA.__bss: 0x616e0
+  __DATA.__bss: 0x616c0
   __DATA.__common: 0x138
   __DATA_DIRTY.__objc_data: 0xd88
   __DATA_DIRTY.__data: 0xaa68

   - /System/Library/Frameworks/Combine.framework/Combine
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
+  - /System/Library/Frameworks/CoreText.framework/CoreText
   - /System/Library/Frameworks/CryptoKit.framework/CryptoKit
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Network.framework/Network

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: E6645A42-DAFE-39D4-862E-477BDC925881
-  Functions: 43602
-  Symbols:   44666
-  CStrings:  3284
+  UUID: 97195D30-C485-3D7D-B88A-68A04E427103
+  Functions: 43607
+  Symbols:   44677
+  CStrings:  3288
 
Symbols:
+ -[MusicKit_SoftLinking_CoverArtworkDataSource _drawText:withFrame:attributedString:renderingHeight:]
+ -[MusicKit_SoftLinking_CoverArtworkDataSource _generatePortraitRadialBurstImageWithImageRenderer:backgroundColor:primaryColor:secondaryColor:tertiaryColor:bundle:rect:size:andSpace:]
+ -[MusicKit_SoftLinking_CoverArtworkDataSource _generateTextGradient:withFrame:attributedString:font:textColor:renderingHeight:]
+ _CFRelease
+ _CGPathCreateWithRect
+ _CGPathRelease
+ _CTFrameDraw
+ _CTFramesetterCreateFrame
+ _CTFramesetterCreateWithAttributedString
+ _OBJC_CLASS_$_NSAttributedString
+ ___127-[MusicKit_SoftLinking_CoverArtworkDataSource _generateTextGradient:withFrame:attributedString:font:textColor:renderingHeight:]_block_invoke
+ ___127-[MusicKit_SoftLinking_CoverArtworkDataSource _generateTextGradient:withFrame:attributedString:font:textColor:renderingHeight:]_block_invoke_2
+ ___182-[MusicKit_SoftLinking_CoverArtworkDataSource _generatePortraitRadialBurstImageWithImageRenderer:backgroundColor:primaryColor:secondaryColor:tertiaryColor:bundle:rect:size:andSpace:]_block_invoke
+ ___182-[MusicKit_SoftLinking_CoverArtworkDataSource _generatePortraitRadialBurstImageWithImageRenderer:backgroundColor:primaryColor:secondaryColor:tertiaryColor:bundle:rect:size:andSpace:]_block_invoke_2
+ ___182-[MusicKit_SoftLinking_CoverArtworkDataSource _generatePortraitRadialBurstImageWithImageRenderer:backgroundColor:primaryColor:secondaryColor:tertiaryColor:bundle:rect:size:andSpace:]_block_invoke_3
+ ___182-[MusicKit_SoftLinking_CoverArtworkDataSource _generatePortraitRadialBurstImageWithImageRenderer:backgroundColor:primaryColor:secondaryColor:tertiaryColor:bundle:rect:size:andSpace:]_block_invoke_4
+ ___182-[MusicKit_SoftLinking_CoverArtworkDataSource _generatePortraitRadialBurstImageWithImageRenderer:backgroundColor:primaryColor:secondaryColor:tertiaryColor:bundle:rect:size:andSpace:]_block_invoke_5
+ ___block_descriptor_104_e8_32s40s48s_e40_v16?0"UIGraphicsImageRendererContext"8ls32l8s40l8s48l8
+ ___block_descriptor_136_e8_32s40s_e40_v16?0"UIGraphicsImageRendererContext"8ls32l8s40l8
+ ___kCFBooleanFalse
+ _hypotf
+ _kCTFrameIntegerLineMetricsAttributeName
+ _objc_msgSend$_drawText:withFrame:attributedString:renderingHeight:
+ _objc_msgSend$_generatePortraitRadialBurstImageWithImageRenderer:backgroundColor:primaryColor:secondaryColor:tertiaryColor:bundle:rect:size:andSpace:
+ _objc_msgSend$_generateTextGradient:withFrame:attributedString:font:textColor:renderingHeight:
+ _objc_msgSend$initWithString:attributes:
- -[MusicKit_SoftLinking_CoverArtworkDataSource _generateTextGradient:withFrame:attributedString:font:textColor:]
- _JetUILibraryCore.frameworkLibrary
- ___109-[MusicKit_SoftLinking_CoverArtworkDataSource _coverArtworkImageWithSize:destinationScale:coverArtworkToken:]_block_invoke.cold.6
- ___111-[MusicKit_SoftLinking_CoverArtworkDataSource _generateTextGradient:withFrame:attributedString:font:textColor:]_block_invoke
- ___111-[MusicKit_SoftLinking_CoverArtworkDataSource _generateTextGradient:withFrame:attributedString:font:textColor:]_block_invoke_2
- ___JetUILibraryCore_block_invoke
- ___getJULanguageAwareStringClass_block_invoke
- ___getJULanguageAwareStringClass_block_invoke.cold.1
- ___getNSMutableParagraphStyleClass_block_invoke
- ___getNSMutableParagraphStyleClass_block_invoke.cold.1
- ___getNSParagraphStyleAttributeNameSymbolLoc_block_invoke
- _audit_stringJetUI
- _getJULanguageAwareStringClass.softClass
- _getNSMutableParagraphStyleClass.softClass
- _getNSParagraphStyleAttributeNameSymbolLoc.ptr
- _objc_msgSend$_generateTextGradient:withFrame:attributedString:font:textColor:
- _objc_msgSend$attributedString
- _objc_msgSend$drawWithRect:options:context:
- _objc_msgSend$initWithString:attributes:baseParagraphStyle:keepStatisticsOnLanguageComponents:
- _objc_msgSend$setMaximumLineHeight:
- _objc_msgSend$setMinimumLineHeight:
CStrings:
+ "@120@0:8@16^{CGColor=}24^{CGColor=}32^{CGColor=}40^{CGColor=}48@56{CGRect={CGPoint=dd}{CGSize=dd}}64{CGSize=dd}96^{CGColorSpace=}112"
+ "_drawText:withFrame:attributedString:renderingHeight:"
+ "_generatePortraitRadialBurstImageWithImageRenderer:backgroundColor:primaryColor:secondaryColor:tertiaryColor:bundle:rect:size:andSpace:"
+ "_generateTextGradient:withFrame:attributedString:font:textColor:renderingHeight:"
+ "initWithString:attributes:"
+ "portrait_car_expression_9_burst_mask_1"
+ "portrait_car_expression_9_burst_mask_2"
+ "portrait_car_expression_9_burst_mask_3"
+ "portrait_car_expression_9_top_mask"
+ "v72@0:8^{CGContext=}16{CGRect={CGPoint=dd}{CGSize=dd}}24@56d64"
+ "v88@0:8^{CGContext=}16{CGRect={CGPoint=dd}{CGSize=dd}}24@56@64@72d80"
- "JULanguageAwareString"
- "NSMutableParagraphStyle"
- "NSParagraphStyleAttributeName"
- "_generateTextGradient:withFrame:attributedString:font:textColor:"
- "attributedString"
- "drawWithRect:options:context:"
- "initWithString:attributes:baseParagraphStyle:keepStatisticsOnLanguageComponents:"
- "setMaximumLineHeight:"
- "setMinimumLineHeight:"
- "softlink:r:path:/System/Library/PrivateFrameworks/JetUI.framework/JetUI"
- "v80@0:8^{CGContext=}16{CGRect={CGPoint=dd}{CGSize=dd}}24@56@64@72"

```
