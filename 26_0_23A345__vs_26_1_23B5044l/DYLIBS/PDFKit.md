## PDFKit

> `/System/Library/Frameworks/PDFKit.framework/PDFKit`

```diff

-1449.0.1.2.0
-  __TEXT.__text: 0xba078
-  __TEXT.__auth_stubs: 0x2c60
-  __TEXT.__objc_methlist: 0xaa3c
+1451.1.3.0.0
+  __TEXT.__text: 0xba20c
+  __TEXT.__auth_stubs: 0x2c50
+  __TEXT.__objc_methlist: 0xaa4c
   __TEXT.__const: 0x954
-  __TEXT.__cstring: 0x7284
-  __TEXT.__gcc_except_tab: 0x36e0
+  __TEXT.__cstring: 0x72a4
+  __TEXT.__gcc_except_tab: 0x36f8
   __TEXT.__dlopen_cstrs: 0x201
   __TEXT.__ustring: 0xb4
   __TEXT.__oslogstring: 0x1a

   __TEXT.__swift5_assocty: 0x30
   __TEXT.__swift5_proto: 0x18
   __TEXT.__swift5_types: 0x8
-  __TEXT.__unwind_info: 0x30e8
+  __TEXT.__unwind_info: 0x30f0
   __TEXT.__eh_frame: 0xb8
-  __TEXT.__objc_classname: 0x1110
-  __TEXT.__objc_methname: 0x196f5
+  __TEXT.__objc_classname: 0x1113
+  __TEXT.__objc_methname: 0x1973c
   __TEXT.__objc_methtype: 0x6cc0
-  __TEXT.__objc_stubs: 0x15540
+  __TEXT.__objc_stubs: 0x15580
   __DATA_CONST.__got: 0xaa0
-  __DATA_CONST.__const: 0x2040
+  __DATA_CONST.__const: 0x2048
   __DATA_CONST.__objc_classlist: 0x458
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x168
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6df8
+  __DATA_CONST.__objc_selrefs: 0x6e08
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0x298
   __DATA_CONST.__objc_arraydata: 0x158
-  __AUTH_CONST.__auth_got: 0x1648
-  __AUTH_CONST.__const: 0x968
-  __AUTH_CONST.__cfstring: 0x7d20
-  __AUTH_CONST.__objc_const: 0xf1c0
+  __AUTH_CONST.__auth_got: 0x1640
+  __AUTH_CONST.__const: 0x988
+  __AUTH_CONST.__cfstring: 0x7d40
+  __AUTH_CONST.__objc_const: 0xf1e0
   __AUTH_CONST.__objc_arrayobj: 0x90
   __AUTH_CONST.__objc_intobj: 0x330
   __AUTH_CONST.__objc_dictobj: 0x168
   __AUTH_CONST.__objc_doubleobj: 0xe0
   __AUTH.__objc_data: 0x28f0
   __AUTH.__data: 0x98
-  __DATA.__objc_ivar: 0xcc8
+  __DATA.__objc_ivar: 0xccc
   __DATA.__data: 0x1190
-  __DATA.__bss: 0x770
+  __DATA.__bss: 0x780
   __DATA_DIRTY.__objc_data: 0x230
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: B39F5F67-7366-32DC-88FD-128FE04A2140
-  Functions: 3661
-  Symbols:   13885
-  CStrings:  7566
+  UUID: 4B8CC478-836E-3062-97F6-049EECBF8A26
+  Functions: 3664
+  Symbols:   13897
+  CStrings:  7571
 
Symbols:
+ +[PDFPage useLegacyImageHandling].cold.1
+ -[PDFPage _handlePageRefChangeWithOldRotation:oldMediaBox:]
+ GCC_except_table116
+ GCC_except_table123
+ GCC_except_table76
+ _OBJC_IVAR_$_PDFPage._pageLock
+ _PDFDocumentCreateAIGeneratedContentDictionary
+ ___33+[PDFPage useLegacyImageHandling]_block_invoke
+ ___59-[PDFPage _handlePageRefChangeWithOldRotation:oldMediaBox:]_block_invoke
+ ___block_literal_global.121
+ ___block_literal_global.317
+ ___block_literal_global.324
+ ___block_literal_global.366
+ _objc_msgSend$_handlePageRefChangeWithOldRotation:oldMediaBox:
+ _objc_msgSend$environment
+ _useLegacyImageHandling.onceToken
+ _useLegacyImageHandling.runningXCTest
- GCC_except_table114
- GCC_except_table121
- GCC_except_table74
- _NSVersionOfLinkTimeLibrary
- ___22-[PDFPage setPageRef:]_block_invoke
- ___block_literal_global.312
- ___block_literal_global.319
- ___block_literal_global.361
Functions:
~ +[PDFPageAnalyzerV2 isCreatedByCalendar:] : 240 -> 304
~ +[PDFAKAnnotationAdaptor _pdfAnnotationInstanceForAKAnnotation:] : 1040 -> 1072
~ -[PDFViewController editMenuInteraction:menuForConfiguration:suggestedActions:] : 908 -> 928
~ +[PDFPage useLegacyImageHandling] : 88 -> 112
+ ___33+[PDFPage useLegacyImageHandling]_block_invoke
~ -[PDFPage setPageRef:] : 616 -> 248
+ -[PDFPage _handlePageRefChangeWithOldRotation:oldMediaBox:]
~ -[PDFPage boundsForBox:] : 436 -> 424
~ -[PDFPage setBounds:forBox:] : 512 -> 528
~ -[PDFPage drawWithBox:inContext:withOptions:] : 1304 -> 1320
~ -[PDFPage _commonInit] : 384 -> 368
~ -[PDFPage drawAnnotationsWithBox:inContext:passingTest:] : 728 -> 696
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~B9_0ugBqXoro13xE6C1ykXsR_AGblqJsbJ-Z1Jg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/System/Library/Frameworks/CoreGraphics.framework/PrivateHeaders/CGBuf.h"
+ "PDFKit_RunningUnitTest"
+ "_handlePageRefChangeWithOldRotation:oldMediaBox:"
+ "_pageLock"
+ "environment"
- "/AppleInternal/Library/BuildRoots/4~B617ugCER984GBWHUCFxr-MfR611kW5uWJWc4_M/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/System/Library/Frameworks/CoreGraphics.framework/PrivateHeaders/CGBuf.h"

```
