## PDFKit

> `/System/Library/Frameworks/PDFKit.framework/PDFKit`

```diff

-1451.1.8.0.0
-  __TEXT.__text: 0xba28c
+1451.2.2.0.0
+  __TEXT.__text: 0xba364
   __TEXT.__auth_stubs: 0x2c60
-  __TEXT.__objc_methlist: 0xaa4c
+  __TEXT.__objc_methlist: 0xaa54
   __TEXT.__const: 0x9a4
   __TEXT.__cstring: 0x72a4
-  __TEXT.__gcc_except_tab: 0x36e8
+  __TEXT.__gcc_except_tab: 0x36d0
   __TEXT.__dlopen_cstrs: 0x201
   __TEXT.__ustring: 0xb4
   __TEXT.__oslogstring: 0x1a

   __TEXT.__unwind_info: 0x30f0
   __TEXT.__eh_frame: 0xb8
   __TEXT.__objc_classname: 0x1113
-  __TEXT.__objc_methname: 0x1973c
-  __TEXT.__objc_methtype: 0x6cc0
-  __TEXT.__objc_stubs: 0x15580
+  __TEXT.__objc_methname: 0x19770
+  __TEXT.__objc_methtype: 0x6cd4
+  __TEXT.__objc_stubs: 0x155c0
   __DATA_CONST.__got: 0xaa0
   __DATA_CONST.__const: 0x2048
   __DATA_CONST.__objc_classlist: 0x458
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x168
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6e08
+  __DATA_CONST.__objc_selrefs: 0x6e18
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0x298
   __DATA_CONST.__objc_arraydata: 0x158

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: A2604CCC-205C-3E3B-AA98-2A04FA7F6138
-  Functions: 3665
-  Symbols:   13900
-  CStrings:  7571
+  UUID: C7DADFC2-2A5D-3156-B070-2316EAA486EE
+  Functions: 3666
+  Symbols:   13904
+  CStrings:  7573
 
Symbols:
+ -[PDFDocument updateUserNameFromAKControllerforAnnotation:]
+ GCC_except_table105
+ GCC_except_table118
+ GCC_except_table155
+ GCC_except_table157
+ GCC_except_table168
+ GCC_except_table176
+ GCC_except_table45
+ GCC_except_table95
+ GCC_except_table99
+ _objc_msgSend$author
+ _objc_msgSend$updateUserNameFromAKControllerforAnnotation:
- GCC_except_table100
- GCC_except_table115
- GCC_except_table117
- GCC_except_table140
- GCC_except_table154
- GCC_except_table156
- GCC_except_table167
- GCC_except_table173
- GCC_except_table175
- GCC_except_table70
- GCC_except_table94
- GCC_except_table98
Functions:
~ +[PDFPageAnalyzerV2 addTablesFromVisionDocument:documentImage:toPage:withBox:] : 2364 -> 2348
~ -[PDFPageViewAnnotationController addMarkupWithStyle:forIndexSet:] : 2164 -> 2192
~ +[PDFAnnotation createDetectedTextFieldWithBounds:font:textContentType:page:] : 356 -> 408
~ -[PDFAnnotation setTextContentType:] : 272 -> 260
~ -[PDFPageAnalyzer _addTableFromAnalysis:bounds:toPDFPage:] : 1484 -> 1468
~ __ZNSt3__16__treeINS_12__value_typeIdU8__strongP13PDFAnnotationEENS_19__map_value_compareIdS5_NS_4lessIdEELb1EEENS_9allocatorIS5_EEE25__emplace_unique_key_argsIdJRKNS_21piecewise_construct_tENS_5tupleIJRKdEEENSH_IJEEEEEENS_4pairINS_15__tree_iteratorIS5_PNS_11__tree_nodeIS5_PvEElEEbEERKT_DpOT0_ : 240 -> 248
~ ___71-[PDFDetectedForm _collectGlyphEntriesInDisplayList:medianGlyphHeight:]_block_invoke : 764 -> 768
~ __ZNSt3__16vectorIPK18CGDisplayListEntryNS_9allocatorIS3_EEE11__vallocateB8ne200100Em : 60 -> 64
~ __ZNSt3__16vectorI18PDFDetectedFormRowNS_9allocatorIS1_EEE26__swap_out_circular_bufferERNS_14__split_bufferIS1_RS3_EEPS1_ : 188 -> 192
~ __ZNSt3__16vectorIU8__strongP20PDFDetectedFormFieldNS_9allocatorIS3_EEE11__vallocateB8ne200100Em : 60 -> 64
+ -[PDFDocument updateUserNameFromAKControllerforAnnotation:]
~ -[PDFView areaOfInterestForPoint:] : 1020 -> 1028
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~CAw-ugACXP9VzbY1YunXuPxbdlynV0TOOoKjc5c/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/System/Library/Frameworks/CoreGraphics.framework/PrivateHeaders/CGBuf.h"
+ "updateUserNameFromAKControllerforAnnotation:"
+ "{vector<CGRect, std::allocator<CGRect>>=\"__begin_\"^{CGRect}\"__end_\"^{CGRect}\"\"{?=\"__cap_\"^{CGRect}}}"
+ "{vector<PDFDetectedFormRow, std::allocator<PDFDetectedFormRow>>=\"__begin_\"^{PDFDetectedFormRow}\"__end_\"^{PDFDetectedFormRow}\"\"{?=\"__cap_\"^{PDFDetectedFormRow}}}"
+ "{vector<const CGDisplayListEntry *, std::allocator<const CGDisplayListEntry *>>=^^{CGDisplayListEntry}^^{CGDisplayListEntry}{?=^^{CGDisplayListEntry}}}32@0:8^{CGDisplayList=}16^d24"
+ "{vector<unsigned char, std::allocator<unsigned char>>=**{?=*}}24@0:8^{CGImage=}16"
- "/AppleInternal/Library/BuildRoots/4~B_wcugDCwP2N8FmKCJK0XLv253-cge_2Fx5tw6Q/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/System/Library/Frameworks/CoreGraphics.framework/PrivateHeaders/CGBuf.h"
- "{vector<CGRect, std::allocator<CGRect>>=\"__begin_\"^{CGRect}\"__end_\"^{CGRect}\"__cap_\"^{CGRect}}"
- "{vector<PDFDetectedFormRow, std::allocator<PDFDetectedFormRow>>=\"__begin_\"^{PDFDetectedFormRow}\"__end_\"^{PDFDetectedFormRow}\"__cap_\"^{PDFDetectedFormRow}}"
- "{vector<const CGDisplayListEntry *, std::allocator<const CGDisplayListEntry *>>=^^{CGDisplayListEntry}^^{CGDisplayListEntry}^^{CGDisplayListEntry}}32@0:8^{CGDisplayList=}16^d24"
- "{vector<unsigned char, std::allocator<unsigned char>>=***}24@0:8^{CGImage=}16"

```
