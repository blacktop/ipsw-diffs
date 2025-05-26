## PDFKit

> `/System/Library/Frameworks/PDFKit.framework/PDFKit`

```diff

-1266.1.9.0.0
-  __TEXT.__text: 0xac4b4
-  __TEXT.__auth_stubs: 0x2620
-  __TEXT.__objc_methlist: 0x89f4
-  __TEXT.__const: 0x6d0
-  __TEXT.__cstring: 0x68e0
-  __TEXT.__gcc_except_tab: 0x1ac0
-  __TEXT.__dlopen_cstrs: 0x10c
+1266.2.7.0.0
+  __TEXT.__text: 0xac820
+  __TEXT.__auth_stubs: 0x2670
+  __TEXT.__objc_methlist: 0x8a4c
+  __TEXT.__const: 0x6e0
+  __TEXT.__cstring: 0x6a4a
+  __TEXT.__gcc_except_tab: 0x1ae4
+  __TEXT.__dlopen_cstrs: 0x162
   __TEXT.__ustring: 0xb4
   __TEXT.__oslogstring: 0x1a
-  __TEXT.__unwind_info: 0x2ba8
+  __TEXT.__unwind_info: 0x2bc0
   __TEXT.__eh_frame: 0x38
-  __TEXT.__objc_classname: 0x1120
-  __TEXT.__objc_methname: 0x1721b
-  __TEXT.__objc_methtype: 0x63fa
-  __TEXT.__objc_stubs: 0x143e0
-  __DATA_CONST.__got: 0x558
-  __DATA_CONST.__const: 0x1d48
-  __DATA_CONST.__objc_classlist: 0x458
+  __TEXT.__objc_classname: 0x1101
+  __TEXT.__objc_methname: 0x173c3
+  __TEXT.__objc_methtype: 0x6436
+  __TEXT.__objc_stubs: 0x14460
+  __DATA_CONST.__got: 0x4f0
+  __DATA_CONST.__const: 0x1d80
+  __DATA_CONST.__objc_classlist: 0x450
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x160
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0xe088
-  __DATA_CONST.__objc_selrefs: 0x60a0
+  __DATA_CONST.__objc_const: 0xe058
+  __DATA_CONST.__objc_selrefs: 0x6100
   __DATA_CONST.__objc_arraydata: 0x148
-  __AUTH_CONST.__cfstring: 0x75a0
-  __AUTH_CONST.__objc_const: 0x2da8
+  __AUTH_CONST.__cfstring: 0x7660
+  __AUTH_CONST.__objc_const: 0x2d60
   __AUTH_CONST.__const: 0x8b8
   __AUTH_CONST.__objc_intobj: 0x318
   __AUTH_CONST.__objc_dictobj: 0x168
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__auth_ptr: 0x8
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH_CONST.__auth_got: 0x1328
-  __AUTH.__objc_data: 0x2990
+  __AUTH_CONST.__auth_got: 0x1350
+  __AUTH.__objc_data: 0x2940
   __DATA.__got_weak: 0x8
   __DATA.__objc_protorefs: 0x30
-  __DATA.__objc_classrefs: 0x838
+  __DATA.__objc_classrefs: 0x830
   __DATA.__objc_superrefs: 0x268
   __DATA.__objc_ivar: 0xc30
-  __DATA.__data: 0x1198
-  __DATA.__bss: 0x2f0
+  __DATA.__data: 0x11a0
+  __DATA.__bss: 0x300
   __DATA_DIRTY.__objc_data: 0x1e0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 3348
-  Symbols:   12832
-  CStrings:  6051
+  Functions: 3362
+  Symbols:   12860
+  CStrings:  6072
 
Symbols:
+ +[PDFAnnotation createDetectedTextFieldWithBounds:font:textContentType:page:]
+ +[PDFAnnotationDrawing textInset]
+ +[PDFPageAnalyzer _normalizedToPageTransformForPageWithBounds:]
+ -[PDFAnnotation autofillEntryType]
+ -[PDFAnnotation isAppearanceStreamEmpty]
+ -[PDFAnnotation setAutofillEntryType:]
+ -[PDFAnnotation setShouldReportAnalytics:]
+ -[PDFAnnotation shouldReportAnalytics]
+ -[PDFAnnotation suppressAppearanceStreamText]
+ -[PDFKitTextView autoFillDidInsertWithExplicitInvocationMode:]
+ -[PDFPageAnalyzer proposedFormFieldBoundsNearestPoint:onPage:completionBlock:]
+ -[PDFTextWidgetTextView autoFillDidInsertWithExplicitInvocationMode:]
+ -[PDFView insertFormFieldAtBestLocationNearPoint:onPage:]
+ -[PDFView insertFormFieldWithBounds:onPage:]
+ -[PDFViewController activateAnotation:]
+ -[PDFViewController addDetectedAnnotation:toPage:]
+ GCC_except_table22
+ GCC_except_table237
+ GCC_except_table311
+ GCC_except_table317
+ GCC_except_table32
+ GCC_except_table33
+ GCC_except_table34
+ GCC_except_table48
+ _AutoFillCoreLibraryCore.frameworkLibrary
+ _CGContextGetProperty
+ _CGContextSetProperty
+ _CGPDFDocumentGetEncryptMetadata
+ _CGPDFDrawingContextDrawWithContentTypes
+ _NSStringFromPoint
+ _NSStringFromRect
+ _OBJC_IVAR_$_PDFAnnotationPrivateVars.autofillEntryType
+ _OBJC_IVAR_$_PDFAnnotationPrivateVars.shouldReportAnalytics
+ _OBJC_IVAR_$_PDFAnnotationPrivateVars.suppressAppearanceStreamText
+ _PDFActionAddNote
+ _PDFActionHighlight
+ _PDFActionRemoveMarkup
+ _PDFActionRemoveNote
+ _PDFKitContextIsAnnotationLayerEffect
+ __OBJC_$_CLASS_PROP_LIST_PDFAnnotationDrawing
+ ___57-[PDFView insertFormFieldAtBestLocationNearPoint:onPage:]_block_invoke
+ ___78-[PDFPageAnalyzer proposedFormFieldBoundsNearestPoint:onPage:completionBlock:]_block_invoke
+ ___78-[PDFPageAnalyzer proposedFormFieldBoundsNearestPoint:onPage:completionBlock:]_block_invoke_2
+ ___83-[PDFViewController _findNextActivatableAnnotationOnPage:fromAnnotation:direction:]_block_invoke.112
+ ___AutoFillCoreLibraryCore_block_invoke
+ ___block_descriptor_144_ea8_32s40s48s56s_e38_"PDFAnnotation"16?0"VKCFormRegion"8ls32l8s40l8s48l8s56l8
+ ___block_descriptor_48_e8_32s40s_e39_v40?0{CGRect={CGPoint=dd}{CGSize=dd}}8ls32l8s40l8
+ ___block_descriptor_48_ea8_32bs40r_e5_v8?0ls32l8r40l8
+ ___block_descriptor_80_ea8_32s40s48bs56r_e38_v24?0"VKCImageAnalysis"8"NSError"16ls32l8s40l8r56l8s48l8
+ ___block_literal_global.210
+ ___block_literal_global.516
+ ___block_literal_global.557
+ ___block_literal_global.891
+ ___block_literal_global.893
+ ___block_literal_global.895
+ ___block_literal_global.903
+ ___block_literal_global.905
+ ___block_literal_global.907
+ ___block_literal_global.915
+ ___block_literal_global.945
+ ___block_literal_global.947
+ ___block_literal_global.949
+ ___block_literal_global.953
+ ___block_literal_global.955
+ ___block_literal_global.975
+ ___block_literal_global.977
+ ___block_literal_global.989
+ ___getAFInsertionManagerClass_block_invoke
+ ___getAFInsertionManagerClass_block_invoke.cold.1
+ __unnamed_array_storage.734
+ __unnamed_array_storage.987
+ _audit_stringAutoFillCore
+ _getAFInsertionManagerClass.softClass
+ _kCGPDFContextEncryptMetadata
+ _objc_msgSend$_normalizedToPageTransformForPageWithBounds:
+ _objc_msgSend$activateAnotation:
+ _objc_msgSend$addDetectedAnnotation:toPage:
+ _objc_msgSend$autoFillDidInsertWithExplicitInvocationMode:
+ _objc_msgSend$boundingRectWithSize:options:attributes:context:
+ _objc_msgSend$boundingRectWithSize:options:context:
+ _objc_msgSend$createDetectedTextFieldWithBounds:font:textContentType:page:
+ _objc_msgSend$drawWithRect:options:context:
+ _objc_msgSend$insertFormFieldAtBestLocationNearPoint:onPage:
+ _objc_msgSend$insertFormFieldWithBounds:onPage:
+ _objc_msgSend$isAppearanceStreamEmpty
+ _objc_msgSend$preferredInsertionOrder
+ _objc_msgSend$proposedFormFieldBoundsNearestPoint:onPage:completionBlock:
+ _objc_msgSend$proposedFormRegionForPoint:existingFields:formSize:
+ _objc_msgSend$setAutofillEntryType:
+ _objc_msgSend$textInset
- +[PDFKitTextContentTypeHelpers preferredAutofillInsertionOrder]
- -[PDFAnnotation setTextInsets:]
- -[PDFAnnotation textInsets]
- -[PDFPageAnalyzer _createFreeTextAnnotationWithBounds:font:textContentType:page:]
- -[PDFView insertFormFieldAtPoint:onPage:]
- -[PDFViewController _activateAnotation:]
- -[PDFViewController addAnnotationForDetectedFormField:onPage:activate:]
- GCC_except_table220
- GCC_except_table239
- GCC_except_table306
- GCC_except_table312
- _CGPDFDrawingContextDraw
- _OBJC_CLASS_$_PDFKitTextContentTypeHelpers
- _OBJC_IVAR_$_PDFAnnotationPrivateVars.layoutManager
- _OBJC_IVAR_$_PDFAnnotationPrivateVars.textInsets
- _OBJC_IVAR_$_PDFAnnotationPrivateVars.textStorage
- _OBJC_METACLASS_$_PDFKitTextContentTypeHelpers
- _UITextContentTypeBirthdate
- _UITextContentTypeBirthdateDay
- _UITextContentTypeBirthdateMonth
- _UITextContentTypeBirthdateYear
- _UITextContentTypeCreditCardExpiration
- _UITextContentTypeCreditCardExpirationMonth
- _UITextContentTypeCreditCardExpirationYear
- _UITextContentTypeCreditCardFamilyName
- _UITextContentTypeCreditCardGivenName
- _UITextContentTypeCreditCardMiddleName
- _UITextContentTypeCreditCardName
- _UITextContentTypeCreditCardSecurityCode
- _UITextContentTypeNewPassword
- _UITextContentTypeOneTimeCode
- __OBJC_$_CLASS_METHODS_PDFKitTextContentTypeHelpers
- __OBJC_CLASS_RO_$_PDFKitTextContentTypeHelpers
- __OBJC_METACLASS_RO_$_PDFKitTextContentTypeHelpers
- ___41-[PDFView insertFormFieldAtPoint:onPage:]_block_invoke
- ___41-[PDFView insertFormFieldAtPoint:onPage:]_block_invoke_2
- ___41-[PDFView insertFormFieldAtPoint:onPage:]_block_invoke_3
- ___83-[PDFViewController _findNextActivatableAnnotationOnPage:fromAnnotation:direction:]_block_invoke.100
- ___block_descriptor_152_ea8_32s40s48s56s64s_e38_"PDFAnnotation"16?0"VKCFormRegion"8ls32l8s40l8s48l8s56l8s64l8
- ___block_descriptor_56_e8_32r_e30_v32?0"PDFAnnotation"8Q16^B24lr32l8
- ___block_descriptor_64_e8_32s40s_e17_v16?0"NSArray"8ls32l8s40l8
- ___block_descriptor_64_e8_32s40s_e5_v8?0ls32l8s40l8
- ___block_literal_global.204
- ___block_literal_global.519
- ___block_literal_global.560
- ___block_literal_global.894
- ___block_literal_global.896
- ___block_literal_global.898
- ___block_literal_global.906
- ___block_literal_global.908
- ___block_literal_global.910
- ___block_literal_global.918
- ___block_literal_global.948
- ___block_literal_global.950
- ___block_literal_global.952
- ___block_literal_global.956
- ___block_literal_global.958
- ___block_literal_global.978
- ___block_literal_global.983
- ___block_literal_global.992
- __unnamed_array_storage.737
- __unnamed_array_storage.990
- _objc_msgSend$_activateAnotation:
- _objc_msgSend$_createFreeTextAnnotationWithBounds:font:textContentType:page:
- _objc_msgSend$addAnnotationForDetectedFormField:onPage:activate:
- _objc_msgSend$addedAnnotation:forFormField:
- _objc_msgSend$detectedFormFieldNearestPoint:
- _objc_msgSend$insertFormFieldAtPoint:onPage:
- _objc_msgSend$preferredAutofillInsertionOrder
- _objc_msgSend$segmentWidth
- _objc_msgSend$setDetectedForm:
- _objc_msgSend$setTextInsets:
- _objc_msgSend$textContainerInset
- _objc_msgSend$textInsets
CStrings:
+ "\x11\xf01q\xd1"
+ "/AppleInternal/Library/BuildRoots/529cd1b6-810a-11ee-9ed3-8e1462286c80/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.2.Internal.sdk/System/Library/Frameworks/CoreGraphics.framework/PrivateHeaders/CGBuf.h"
+ "A\x13q\x11!1\x11!\x91B"
+ "AFInsertionManager"
+ "PDFKitContextIsAnnotationLayerEffect"
+ "Td,R"
+ "Wj"
+ "_normalizedToPageTransformForPageWithBounds:"
+ "activateAnotation:"
+ "addDetectedAnnotation:toPage:"
+ "analyzePageBlock: (page #%lu) Minimal analysis COMPLETED (+%g secs)"
+ "autoFillDidInsertWithExplicitInvocationMode:"
+ "autofillEntryType"
+ "boundingRectWithSize:options:attributes:context:"
+ "boundingRectWithSize:options:context:"
+ "com.apple.pdfkit.action.addNote"
+ "com.apple.pdfkit.action.highlight"
+ "com.apple.pdfkit.action.removeMarkup"
+ "com.apple.pdfkit.action.removeNote"
+ "createDetectedTextFieldWithBounds:font:textContentType:page:"
+ "drawWithRect:options:context:"
+ "insertFormFieldAtBestLocationNearPoint:onPage:"
+ "insertFormFieldWithBounds:onPage:"
+ "isAppearanceStreamEmpty"
+ "preferredInsertionOrder"
+ "proposedFormField: formRegion bounds: %@"
+ "proposedFormField: pagePoint = %@, normalizedPoint = %@"
+ "proposedFormFieldBoundsNearestPoint:onPage:completionBlock:"
+ "proposedFormRegionForPoint:existingFields:formSize:"
+ "setAutofillEntryType:"
+ "setShouldReportAnalytics:"
+ "shouldReportAnalytics"
+ "softlink:r:path:/System/Library/PrivateFrameworks/AutoFillCore.framework/AutoFillCore"
+ "suppressAppearanceStreamText"
+ "textInset"
+ "v48@0:8{CGPoint=dd}16@32@?40"
+ "{CGAffineTransform=dddddd}48@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16"
- "\x11\xf01q\xf01"
- "/AppleInternal/Library/BuildRoots/b5ebca3a-5f05-11ee-949e-926038f30c31/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.1.Internal.sdk/System/Library/Frameworks/CoreGraphics.framework/PrivateHeaders/CGBuf.h"
- "@\"NSLayoutManager\""
- "@36@0:8@16@24B32"
- "A\x13q\x11!1\x11\"A\x81B"
- "PDFKitTextContentTypeHelpers"
- "_activateAnotation:"
- "_createFreeTextAnnotationWithBounds:font:textContentType:page:"
- "addAnnotationForDetectedFormField:onPage:activate:"
- "insertFormFieldAtPoint:onPage:"
- "layoutManager"
- "preferredAutofillInsertionOrder"
- "setTextInsets:"
- "textContainerInset"
- "textInsets"
- "textStorage"

```
