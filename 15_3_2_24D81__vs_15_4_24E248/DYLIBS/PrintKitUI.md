## PrintKitUI

> `/System/iOSSupport/System/Library/PrivateFrameworks/PrintKitUI.framework/Versions/A/PrintKitUI`

```diff

-16.5.0.0.0
-  __TEXT.__text: 0x1c938
-  __TEXT.__auth_stubs: 0xc00
-  __TEXT.__objc_methlist: 0x1e38
-  __TEXT.__const: 0x1e8
-  __TEXT.__cstring: 0x10fc
-  __TEXT.__gcc_except_tab: 0x5dc
-  __TEXT.__dlopen_cstrs: 0x186
-  __TEXT.__unwind_info: 0x878
-  __TEXT.__objc_classname: 0x371
-  __TEXT.__objc_methname: 0x5786
-  __TEXT.__objc_methtype: 0xa6a
-  __TEXT.__objc_stubs: 0x44c0
-  __DATA_CONST.__got: 0x330
-  __DATA_CONST.__const: 0x680
+50.3.0.0.0
+  __TEXT.__text: 0x1b7e0
+  __TEXT.__auth_stubs: 0xc90
+  __TEXT.__objc_methlist: 0x210c
+  __TEXT.__const: 0x240
+  __TEXT.__cstring: 0xebe
+  __TEXT.__gcc_except_tab: 0x3f0
+  __TEXT.__ustring: 0x8
+  __TEXT.__unwind_info: 0x710
+  __TEXT.__objc_classname: 0x356
+  __TEXT.__objc_methname: 0x5b90
+  __TEXT.__objc_methtype: 0xac9
+  __TEXT.__objc_stubs: 0x4940
+  __DATA_CONST.__got: 0x460
+  __DATA_CONST.__const: 0x648
   __DATA_CONST.__objc_classlist: 0xd8
   __DATA_CONST.__objc_catlist: 0x20
-  __DATA_CONST.__objc_protolist: 0x40
+  __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1880
+  __DATA_CONST.__objc_selrefs: 0x1a20
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x90
   __DATA_CONST.__objc_arraydata: 0x60
-  __AUTH_CONST.__auth_got: 0x610
-  __AUTH_CONST.__const: 0xb0
-  __AUTH_CONST.__cfstring: 0x1220
-  __AUTH_CONST.__objc_const: 0x36c0
+  __AUTH_CONST.__auth_got: 0x658
+  __AUTH_CONST.__const: 0x70
+  __AUTH_CONST.__cfstring: 0x12e0
+  __AUTH_CONST.__objc_const: 0x3438
   __AUTH_CONST.__objc_intobj: 0xd8
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH.__objc_data: 0x870
-  __DATA.__objc_ivar: 0x250
-  __DATA.__data: 0x308
-  __DATA.__bss: 0x200
+  __DATA.__objc_ivar: 0x260
+  __DATA.__data: 0x2a8
+  __DATA.__bss: 0x48
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/Versions/A/CoreGraphics
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/Frameworks/ImageIO.framework/Versions/A/ImageIO
+  - /System/Library/Frameworks/QuartzCore.framework/Versions/A/QuartzCore
   - /System/Library/Frameworks/UniformTypeIdentifiers.framework/Versions/A/UniformTypeIdentifiers
   - /System/Library/PrivateFrameworks/PrintKit.framework/Versions/A/PrintKit
   - /System/Library/PrivateFrameworks/SoftLinking.framework/Versions/A/SoftLinking

   - /System/iOSSupport/System/Library/PrivateFrameworks/UIKitCore.framework/Versions/A/UIKitCore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: E28CD323-D021-3547-B66D-EA772065621B
-  Functions: 778
-  Symbols:   2275
-  CStrings:  1599
+  UUID: 08A04AF1-E5E7-3014-B66D-34499314E77A
+  Functions: 718
+  Symbols:   2160
+  CStrings:  1617
 
Symbols:
+ +[UIPrinterInfoRequest requestInfoForPrinter:]
+ -[UIPrintInteractionController _addPDFWithData:toContext:addAllPages:]
+ -[UIPrintInteractionController _canPreviewContent]
+ -[UIPrintInteractionController _createDocInfoDict]
+ -[UIPrintInteractionController _drawPrintItem:toContext:printAllPages:]
+ -[UIPrintInteractionController _printItemContentSize:]
+ -[UIPrintInteractionController _printPageWithRenderer:]
+ -[UIPrintInteractionController _setPrinterInfoState:]
+ -[UIPrintInteractionController appOptionsViewController]
+ -[UIPrintInteractionController createWebKitPDFForAllPages]
+ -[UIPrintInteractionController drawImage:toContext:sheetSize:]
+ -[UIPrintInteractionController drawImageForPageNum:toContext:sheetSize:]
+ -[UIPrintInteractionController drawPagesWithPreviewState:]
+ -[UIPrintInteractionController paperSizeForPageNum:]
+ -[UIPrintInteractionController preventPDFCreation]
+ -[UIPrintInteractionController printerInfoState]
+ -[UIPrintInteractionController recalculateWebKitPageCount]
+ -[UIPrintInteractionController setPreventPDFCreation:]
+ -[UIPrintInteractionController setPrinterInfoState:]
+ -[UIPrintInteractionController setUsingWebKitFormatter:]
+ -[UIPrintInteractionController setWebKitFormatterMutex:]
+ -[UIPrintInteractionController updatePrintingItems]
+ -[UIPrintInteractionController usingWebKitFormatter]
+ -[UIPrintInteractionController webKitFormatterMutex]
+ -[UIPrintInteractionController(UIPrintInteractionController_Private) dismissAnimated:completionHandler:]
+ -[UIPrintMessageAndSpinnerView .cxx_destruct]
+ -[UIPrintMessageAndSpinnerView currentHorizontalConstraints]
+ -[UIPrintMessageAndSpinnerView initWithFrame:]
+ -[UIPrintMessageAndSpinnerView label]
+ -[UIPrintMessageAndSpinnerView messageText]
+ -[UIPrintMessageAndSpinnerView setCurrentHorizontalConstraints:]
+ -[UIPrintMessageAndSpinnerView setLabel:]
+ -[UIPrintMessageAndSpinnerView setMessageText:]
+ -[UIPrintMessageAndSpinnerView setSpinSpinner:]
+ -[UIPrintMessageAndSpinnerView setSpinner:]
+ -[UIPrintMessageAndSpinnerView setSpinnerHidden:]
+ -[UIPrintMessageAndSpinnerView spinSpinner]
+ -[UIPrintMessageAndSpinnerView spinnerHidden]
+ -[UIPrintMessageAndSpinnerView spinner]
+ -[UIPrintMessageAndSpinnerView updateConstraints]
+ -[UIPrintMessageAndSpinnerView updateFont]
+ -[UIPrintPageRenderer _drawPage:withScale:drawingToPDF:]
+ -[UIPrintPageRenderer _endPrintJobContext]
+ -[UIPrintPageRenderer _startPrintJobContext:]
+ -[UIPrintPageRenderer _startPrintJobContext:printInfo:printSettings:]
+ -[UIPrintPanelViewController dismissAnimated:completionHandler:]
+ -[UIPrintPaper mediaType]
+ -[UIPrintServiceExtension _apOp:reply:]
+ -[UIPrintServiceExtension _authenticatedRequestForRequest:challengeResponse:reply:]
+ -[UIPrintServiceExtensionContext _apOp:reply:]
+ -[UIPrintServiceExtensionContext _authenticatedRequestForRequest:challengeResponse:reply:]
+ -[UIPrinterInfoRequest .cxx_destruct]
+ -[UIPrinterInfoRequest completionHandler]
+ -[UIPrinterInfoRequest printerInfo]
+ -[UIPrinterInfoRequest requestPrinterInfo]
+ -[UIPrinterInfoRequest requestState]
+ -[UIPrinterInfoRequest setCompletionHandler:]
+ -[UIPrinterInfoRequest setPrinterInfo:]
+ -[UIPrinterInfoRequest setRequestState:]
+ -[UITallPDFPrintFormatter initWithPDFData:pdfPassword:]
+ -[UITallPDFPrintFormatter initWithPDFURL:pdfPassword:]
+ -[UITextViewPrintFormatter adjustedPageBottom:]
+ -[UITextViewPrintFormatter calculatingUsedRects]
+ -[UITextViewPrintFormatter initializedUsedRects]
+ -[UITextViewPrintFormatter pageData]
+ -[UITextViewPrintFormatter setCalculatingUsedRects:]
+ -[UITextViewPrintFormatter setInitializedUsedRects:]
+ -[UITextViewPrintFormatter setPageData:]
+ GCC_except_table120
+ GCC_except_table50
+ GCC_except_table53
+ GCC_except_table61
+ GCC_except_table67
+ GCC_except_table72
+ GCC_except_table74
+ GCC_except_table8
+ OBJC_IVAR_$_UIPrintInteractionController._alertWindow
+ OBJC_IVAR_$_UIPrintInteractionController._preventPDFCreation
+ OBJC_IVAR_$_UIPrintInteractionController._printerInfoState
+ OBJC_IVAR_$_UIPrintInteractionController._usingWebKitFormatter
+ OBJC_IVAR_$_UIPrintInteractionController._webKitFormatterMutex
+ OBJC_IVAR_$_UIPrintMessageAndSpinnerView._currentHorizontalConstraints
+ OBJC_IVAR_$_UIPrintMessageAndSpinnerView._label
+ OBJC_IVAR_$_UIPrintMessageAndSpinnerView._spinner
+ OBJC_IVAR_$_UIPrintPageRenderer._usingPrintJobContext
+ OBJC_IVAR_$_UIPrinterInfoRequest._completionHandler
+ OBJC_IVAR_$_UIPrinterInfoRequest._printer
+ OBJC_IVAR_$_UIPrinterInfoRequest._printerInfo
+ OBJC_IVAR_$_UIPrinterInfoRequest._requestState
+ OBJC_IVAR_$_UITextViewPrintFormatter._calculatingUsedRects
+ OBJC_IVAR_$_UITextViewPrintFormatter._initializedUsedRects
+ _CFStringGetLength
+ _CGAffineTransformConcat
+ _CGAffineTransformIdentity
+ _CGAffineTransformMakeRotation
+ _CGBitmapContextGetColorSpace
+ _CGBitmapContextGetHeight
+ _CGBitmapContextGetWidth
+ _CGColorSpaceGetModel
+ _CGContextDrawImage
+ _CGContextFillRect
+ _CGContextSetCMYKFillColor
+ _CGContextSetCTM
+ _CGContextSetGrayFillColor
+ _CGContextSetRGBFillColor
+ _CGRectApplyAffineTransform
+ _CGRectGetWidth
+ _CGRectIntersectsRect
+ _GetAppName
+ _LocalizedInteger
+ _LocalizedUnsignedInteger
+ _NSIntersectsRange
+ _OBJC_CLASS_$_NSNumberFormatter
+ _OBJC_CLASS_$_NSThread
+ _OBJC_CLASS_$_PKDefaults
+ _OBJC_CLASS_$_PKPrintSettings
+ _OBJC_CLASS_$_UIPrintMessageAndSpinnerView
+ _OBJC_CLASS_$_UIPrinterInfoRequest
+ _OBJC_CLASS_$_UTType
+ _OBJC_METACLASS_$_UIPrintMessageAndSpinnerView
+ _OBJC_METACLASS_$_UIPrinterInfoRequest
+ _PDFHasAnnotations
+ _PKAnnotationsImagedKey
+ _PKCopiesKey
+ _PKDocumentPasswordKey
+ _PKDrawImageToSheet
+ _PKDuplexKey
+ _PKDuplexLandscape
+ _PKDuplexNone
+ _PKDuplexPortrait
+ _PKFileTypePDF
+ _PKFinishingTemplateKey
+ _PKFinishingsKey
+ _PKInputSlotKey
+ _PKJobAccountIDKey
+ _PKJobNameKey
+ _PKJobPresetFinishingsKey
+ _PKJobPresetKey
+ _PKJobPresetMediaSourceKey
+ _PKJobPresetMediaTypeKey
+ _PKJobPresetOptionKey
+ _PKMediaTypeKey
+ _PKOrientationKey
+ _PKOrientationLandscape
+ _PKOrientationPortrait
+ _PKOrientationReverseLandscape
+ _PKOutputBinKey
+ _PKOutputModeColor
+ _PKOutputModeGray
+ _PKOutputModeKey
+ _PKPageStackOrderKey
+ _PKPrinterLastUsedSize
+ _PKPrinterNameKey
+ _PKQualityHigh
+ _PKQualityKey
+ _PKQualityNormal
+ _PKUIPageCountKeyPath
+ _PMAppendToSummaryString
+ __OBJC_$_CLASS_METHODS_UIPrinterInfoRequest
+ __OBJC_$_INSTANCE_METHODS_UIPrintMessageAndSpinnerView
+ __OBJC_$_INSTANCE_METHODS_UIPrinterInfoRequest
+ __OBJC_$_INSTANCE_VARIABLES_UIPrintMessageAndSpinnerView
+ __OBJC_$_INSTANCE_VARIABLES_UIPrinterInfoRequest
+ __OBJC_$_PROP_LIST_UIPrintMessageAndSpinnerView
+ __OBJC_$_PROP_LIST_UIPrinterInfoRequest
+ __OBJC_$_PROP_LIST_UITextViewPrintFormatter
+ __OBJC_CLASS_RO_$_UIPrintMessageAndSpinnerView
+ __OBJC_CLASS_RO_$_UIPrinterInfoRequest
+ __OBJC_METACLASS_RO_$_UIPrintMessageAndSpinnerView
+ __OBJC_METACLASS_RO_$_UIPrinterInfoRequest
+ __UIPrinterInfoCancelRequest
+ __UIPrinterInfoCancelRequests
+ __UIPrinterInfoGetState
+ __UIPrinterInfoHasInfo
+ __UIPrinterInfoStartRequest
+ ___36-[UITextViewPrintFormatter pageData]_block_invoke
+ ___42-[UIPrinterInfoRequest requestPrinterInfo]_block_invoke
+ ___42-[UIPrinterInfoRequest requestPrinterInfo]_block_invoke_2
+ ___54-[UITextViewPrintFormatter drawInRect:forPageAtIndex:]_block_invoke_2
+ ___54-[UITextViewPrintFormatter drawInRect:forPageAtIndex:]_block_invoke_3
+ ___80-[UIPrintInteractionController _presentAnimated:hostingScene:completionHandler:]_block_invoke_2
+ ____UIPrinterInfoCancelRequests_block_invoke
+ ___block_descriptor_112_e8_32s40s_e25_v16?0"NSLayoutManager"8ls32l8s40l8
+ ___block_descriptor_40_e8_32w_e5_v8?0lw32l8
+ ___block_descriptor_48_e8_32s40s_e23_v16?0"UIAlertAction"8ls32l8s40l8
+ ___block_descriptor_48_e8_32s40w_e5_v8?0lw40l8s32l8
+ ___block_descriptor_72_e8_32s_e25_v16?0"NSLayoutManager"8ls32l8
+ ___block_descriptor_96_e8_32r_e35_v32?0"NSTextLineFragment"8Q16^B24lr32l8
+ ___block_descriptor_96_e8_32s40r48r_e30_B16?0"NSTextLayoutFragment"8ls32l8r40l8r48l8
+ ___printerInfoRequests
+ __cgImageToPaperTransform
+ __imageRotationTransfrom
+ _drawCGImageToCGContext
+ _drawPDFPageToCGContext
+ _eraseCGBitmapContext
+ _kCGPDFContextOwnerPassword
+ _kCGPDFContextUserPassword
+ _objc_msgSend$_addPDFWithData:toContext:addAllPages:
+ _objc_msgSend$_apOp:reply:
+ _objc_msgSend$_authenticatedRequestForRequest:challengeResponse:reply:
+ _objc_msgSend$_canPreviewContent
+ _objc_msgSend$_createDocInfoDict
+ _objc_msgSend$_drawPage:withScale:drawingToPDF:
+ _objc_msgSend$_drawPrintItem:toContext:printAllPages:
+ _objc_msgSend$_endPrintJobContext
+ _objc_msgSend$_printItemContentSize:
+ _objc_msgSend$_setPrinterInfoState:
+ _objc_msgSend$_startPrintJobContext:
+ _objc_msgSend$_startPrintJobContext:printInfo:printSettings:
+ _objc_msgSend$addPrinterToiCloud:displayName:location:
+ _objc_msgSend$adjustedPageBottom:
+ _objc_msgSend$appendString:
+ _objc_msgSend$calculatingUsedRects
+ _objc_msgSend$currentThread
+ _objc_msgSend$delegate
+ _objc_msgSend$description
+ _objc_msgSend$dismissAnimated:completionHandler:
+ _objc_msgSend$documentRange
+ _objc_msgSend$drawAtPoint:inContext:
+ _objc_msgSend$drawImage:toContext:sheetSize:
+ _objc_msgSend$drawPagesWithPreviewState:
+ _objc_msgSend$ensureLayoutForRange:
+ _objc_msgSend$enumerateTextLayoutFragmentsFromLocation:options:usingBlock:
+ _objc_msgSend$hasPrefix:
+ _objc_msgSend$initWithPDFData:pdfPassword:
+ _objc_msgSend$initWithPDFURL:pdfPassword:
+ _objc_msgSend$initializedUsedRects
+ _objc_msgSend$isCancelled
+ _objc_msgSend$lastPathComponent
+ _objc_msgSend$layoutFragmentFrame
+ _objc_msgSend$localizedStringFromNumber:numberStyle:
+ _objc_msgSend$mediaInfo
+ _objc_msgSend$numberWithUnsignedInteger:
+ _objc_msgSend$pageData
+ _objc_msgSend$paperSizeForPageNum:
+ _objc_msgSend$pathExtension
+ _objc_msgSend$performSelector:
+ _objc_msgSend$printPanelViewController
+ _objc_msgSend$printerInfo
+ _objc_msgSend$printingItem
+ _objc_msgSend$printingItems
+ _objc_msgSend$removeObjectsInArray:
+ _objc_msgSend$requestPrinterInfo
+ _objc_msgSend$setCalculatingUsedRects:
+ _objc_msgSend$setInitializedUsedRects:
+ _objc_msgSend$setJobName:
+ _objc_msgSend$setPrinterInfo:
+ _objc_msgSend$setUsingWebKitFormatter:
+ _objc_msgSend$stringByDeletingPathExtension
+ _objc_msgSend$textContainerOrigin
+ _objc_msgSend$textContentManager
+ _objc_msgSend$textLayoutFragmentForPosition:
+ _objc_msgSend$textLayoutManager
+ _objc_msgSend$textLineFragmentForVerticalOffset:requiresExactMatch:
+ _objc_msgSend$textLineFragments
+ _objc_msgSend$typeWithFilenameExtension:
+ _objc_msgSend$typographicBounds
+ _objc_msgSend$updatePrintingItems
+ _objc_msgSend$usageBoundsForTextContainer
+ _objc_msgSend$usingWebKitFormatter
+ _objc_msgSend$webKitFormatterMutex
+ _pdfPageToPaperTransform
+ _pdfPageToPaperTransformFilter
+ _startPrintJobContext:printInfo:printSettings:.__consumerCallbacks
+ drawImage:toContext:sheetSize:._UIImageOrientationToEXIFOrientationMapping
+ printableRect.0
+ printableRect.1
+ printableRect.2
+ printableRect.3
- +[UIPrintInfoRequest requestInfoForPrinter:]
- -[UIPrintInfo _createPrintSettingsForPrinter:].cold.1
- -[UIPrintInfo _createPrintSettingsForPrinter:].cold.2
- -[UIPrintInfo _createPrintSettingsForPrinter:].cold.3
- -[UIPrintInfo _createPrintSettingsForPrinter:].cold.4
- -[UIPrintInfo _createPrintSettingsForPrinter:].cold.5
- -[UIPrintInfo _createPrintSettingsForPrinter:].cold.6
- -[UIPrintInfo _createPrintSettingsForPrinter:].cold.7
- -[UIPrintInfo _createPrintSettingsForPrinter:].cold.8
- -[UIPrintInfo _createPrintSettingsForPrinter:].cold.9
- -[UIPrintInfoRequest .cxx_destruct]
- -[UIPrintInfoRequest completionHandler]
- -[UIPrintInfoRequest requestPrintInfo]
- -[UIPrintInfoRequest requestState]
- -[UIPrintInfoRequest setCompletionHandler:]
- -[UIPrintInfoRequest setRequestState:]
- -[UIPrintInteractionController _addPDFWithData:toContext:]
- -[UIPrintInteractionController _drawPageWithItem:toContext:]
- -[UIPrintInteractionController _generatePDFForQuickLookCompletion:]
- -[UIPrintInteractionController _preparePrintInfo].cold.1
- -[UIPrintInteractionController _preparePrintInfo].cold.2
- -[UIPrintInteractionController _preparePrintInfo].cold.3
- -[UIPrintInteractionController _printPageRenderer:]
- -[UIPrintInteractionController _setPrintInfoState:]
- -[UIPrintInteractionController drawAllPagesWithPreviewState:]
- -[UIPrintInteractionController drawThumbnailImageForPageNum:toContext:sheetSize:]
- -[UIPrintInteractionController paper].cold.1
- -[UIPrintInteractionController paper].cold.2
- -[UIPrintInteractionController printInfoState]
- -[UIPrintInteractionController setPrintInfoState:]
- -[UIPrintInteractionController thumbnailSizeForPageNum:]
- -[UIPrintPageRenderer _drawPage:]
- -[UIPrintPageRenderer _endPrintContext:success:]
- -[UIPrintPageRenderer _startPrintContext:printSettings:]
- -[UIPrintPageRenderer _startPrintContext:printSettings:].cold.1
- -[UIPrintPanelViewController appPrintExtensionController]
- -[UIPrintPanelViewController setAppPrintExtensionController:]
- -[UIPrintServiceExtension .cxx_destruct]
- -[UIPrintServiceExtension _respondWithResults:]
- -[UIPrintServiceExtension beginRequestWithExtensionContext:]
- -[UIPrintServiceExtension extensionContext]
- -[UIPrintServiceExtension setExtensionContext:]
- -[UIPrinter finishingTemplates].cold.1
- -[UIPrinter outputBins].cold.1
- -[UIPrinter printerFinishingOptions].cold.1
- -[UIPrinter supportedMediaTypes].cold.1
- -[UIPrinter supportedPresets].cold.1
- -[UIPrinter supportedQualities].cold.1
- -[UIPrinter supportedTrays].cold.1
- -[UITallPDFPrintFormatter initWithPDFData:]
- -[UITallPDFPrintFormatter initWithPDFURL:]
- -[UITextViewPrintFormatter _pageData]
- -[_UIPrintMessageAndSpinnerView .cxx_destruct]
- -[_UIPrintMessageAndSpinnerView currentHorizontalConstraints]
- -[_UIPrintMessageAndSpinnerView initWithFrame:]
- -[_UIPrintMessageAndSpinnerView label]
- -[_UIPrintMessageAndSpinnerView messageText]
- -[_UIPrintMessageAndSpinnerView setCurrentHorizontalConstraints:]
- -[_UIPrintMessageAndSpinnerView setLabel:]
- -[_UIPrintMessageAndSpinnerView setMessageText:]
- -[_UIPrintMessageAndSpinnerView setSpinSpinner:]
- -[_UIPrintMessageAndSpinnerView setSpinner:]
- -[_UIPrintMessageAndSpinnerView setSpinnerHidden:]
- -[_UIPrintMessageAndSpinnerView spinSpinner]
- -[_UIPrintMessageAndSpinnerView spinnerHidden]
- -[_UIPrintMessageAndSpinnerView spinner]
- -[_UIPrintMessageAndSpinnerView updateConstraints]
- -[_UIPrintMessageAndSpinnerView updateFont]
- GCC_except_table12
- GCC_except_table13
- GCC_except_table134
- GCC_except_table14
- GCC_except_table16
- GCC_except_table17
- GCC_except_table18
- GCC_except_table20
- GCC_except_table22
- GCC_except_table23
- GCC_except_table24
- GCC_except_table25
- GCC_except_table26
- GCC_except_table27
- GCC_except_table28
- GCC_except_table30
- GCC_except_table31
- GCC_except_table32
- GCC_except_table33
- GCC_except_table34
- GCC_except_table35
- GCC_except_table36
- GCC_except_table37
- GCC_except_table38
- GCC_except_table45
- GCC_except_table46
- GCC_except_table49
- GCC_except_table52
- GCC_except_table60
- GCC_except_table69
- GCC_except_table92
- GCC_except_table93
- ImageableArea.0
- ImageableArea.1
- ImageableArea.2
- ImageableArea.3
- OBJC_IVAR_$_UIPrintInfoRequest._completionHandler
- OBJC_IVAR_$_UIPrintInfoRequest._printer
- OBJC_IVAR_$_UIPrintInfoRequest._requestState
- OBJC_IVAR_$_UIPrintInteractionController._passwordAlertWindow
- OBJC_IVAR_$_UIPrintInteractionController._printInfoState
- OBJC_IVAR_$_UIPrintPanelViewController._appPrintExtensionController
- OBJC_IVAR_$_UIPrintServiceExtension._extensionContext
- OBJC_IVAR_$_UITextViewPrintFormatter._textViewPrintFormatterFlags
- OBJC_IVAR_$__UIPrintMessageAndSpinnerView._currentHorizontalConstraints
- OBJC_IVAR_$__UIPrintMessageAndSpinnerView._label
- OBJC_IVAR_$__UIPrintMessageAndSpinnerView._spinner
- PrintKitLibraryCore.frameworkLibrary
- _CFNumberCreate
- _OBJC_CLASS_$_NSExtensionItem
- _OBJC_CLASS_$_NSItemProvider
- _OBJC_CLASS_$_UIPrintInfoRequest
- _OBJC_CLASS_$__UIPrintMessageAndSpinnerView
- _OBJC_EHTYPE_$_NSException
- _OBJC_METACLASS_$_UIPrintInfoRequest
- _OBJC_METACLASS_$__UIPrintMessageAndSpinnerView
- _PrintKitLibrary
- _UTTypePropertyList
- __OBJC_$_CLASS_METHODS_UIPrintInfoRequest
- __OBJC_$_INSTANCE_METHODS_UIPrintInfoRequest
- __OBJC_$_INSTANCE_METHODS__UIPrintMessageAndSpinnerView
- __OBJC_$_INSTANCE_VARIABLES_UIPrintInfoRequest
- __OBJC_$_INSTANCE_VARIABLES_UIPrintServiceExtension
- __OBJC_$_INSTANCE_VARIABLES__UIPrintMessageAndSpinnerView
- __OBJC_$_PROP_LIST_UIPrintInfoRequest
- __OBJC_$_PROP_LIST_UIPrintServiceExtension
- __OBJC_$_PROP_LIST__UIPrintMessageAndSpinnerView
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSExtensionRequestHandling
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSExtensionRequestHandling
- __OBJC_$_PROTOCOL_REFS_NSExtensionRequestHandling
- __OBJC_CLASS_PROTOCOLS_$_UIPrintServiceExtension
- __OBJC_CLASS_RO_$_UIPrintInfoRequest
- __OBJC_CLASS_RO_$__UIPrintMessageAndSpinnerView
- __OBJC_LABEL_PROTOCOL_$_NSExtensionRequestHandling
- __OBJC_METACLASS_RO_$_UIPrintInfoRequest
- __OBJC_METACLASS_RO_$__UIPrintMessageAndSpinnerView
- __OBJC_PROTOCOL_$_NSExtensionRequestHandling
- __PKDrawImageToSheet.cold.1
- __UIPrintInfoCancelRequest
- __UIPrintInfoCancelRequests
- __UIPrintInfoGetState
- __UIPrintInfoStartRequest
- __UIPrinterGetDescription
- ___37-[UITextViewPrintFormatter _pageData]_block_invoke
- ___38-[UIPrintInfoRequest requestPrintInfo]_block_invoke
- ___38-[UIPrintInfoRequest requestPrintInfo]_block_invoke_2
- ___47-[UIPrintServiceExtension _respondWithResults:]_block_invoke
- ___47-[UIPrintServiceExtension _respondWithResults:]_block_invoke_2
- ___47-[UIPrintServiceExtension _respondWithResults:]_block_invoke_3
- ___60-[UIPrintServiceExtension beginRequestWithExtensionContext:]_block_invoke
- ___67-[UIPrintInteractionController _generatePDFForQuickLookCompletion:]_block_invoke
- ___PKDrawImageToSheet
- ___PrintKitLibraryCore_block_invoke
- ____UIPrintInfoCancelRequests_block_invoke
- ___block_descriptor_152_e8_32s40s48s_e25_v16?0"NSLayoutManager"8ls32l8s40l8s48l8
- ___block_descriptor_40_e5_v8?0l
- ___block_descriptor_40_e8_32bs_e21_v24?0"NSURL"8B16B20ls32l8
- ___block_descriptor_40_e8_32r_e5_v8?0lr32l8
- ___block_descriptor_40_e8_32s_e34_v24?0"NSDictionary"8"NSError"16ls32l8
- ___block_descriptor_48_e8_32s40s_e5_v8?0ls32l8s40l8
- ___block_descriptor_80_e8_32s40s_e25_v16?0"NSLayoutManager"8ls32l8s40l8
- ___getPKAnnotationsImagedKeySymbolLoc_block_invoke
- ___getPKCopiesKeySymbolLoc_block_invoke
- ___getPKDefaultsClass_block_invoke
- ___getPKDocumentPasswordKeySymbolLoc_block_invoke
- ___getPKDrawImageToSheetSymbolLoc_block_invoke
- ___getPKDuplexKeySymbolLoc_block_invoke
- ___getPKDuplexLandscapeSymbolLoc_block_invoke
- ___getPKDuplexNoneSymbolLoc_block_invoke
- ___getPKDuplexPortraitSymbolLoc_block_invoke
- ___getPKFileTypePDFSymbolLoc_block_invoke
- ___getPKFinishingTemplateKeySymbolLoc_block_invoke
- ___getPKFinishingsKeySymbolLoc_block_invoke
- ___getPKInputSlotKeySymbolLoc_block_invoke
- ___getPKJobAccountIDKeySymbolLoc_block_invoke
- ___getPKJobNameKeySymbolLoc_block_invoke
- ___getPKJobPresetFinishingsKeySymbolLoc_block_invoke
- ___getPKJobPresetKeySymbolLoc_block_invoke
- ___getPKJobPresetMediaSourceKeySymbolLoc_block_invoke
- ___getPKJobPresetMediaTypeKeySymbolLoc_block_invoke
- ___getPKJobPresetOptionKeySymbolLoc_block_invoke
- ___getPKMediaTypeKeySymbolLoc_block_invoke
- ___getPKOrientationKeySymbolLoc_block_invoke
- ___getPKOrientationLandscapeSymbolLoc_block_invoke
- ___getPKOrientationPortraitSymbolLoc_block_invoke
- ___getPKOrientationReverseLandscapeSymbolLoc_block_invoke
- ___getPKOutputBinKeySymbolLoc_block_invoke
- ___getPKOutputModeColorSymbolLoc_block_invoke
- ___getPKOutputModeGraySymbolLoc_block_invoke
- ___getPKOutputModeKeySymbolLoc_block_invoke
- ___getPKPageStackOrderKeySymbolLoc_block_invoke
- ___getPKPaperClass_block_invoke
- ___getPKPrintSettingsClass_block_invoke
- ___getPKPrinterClass_block_invoke
- ___getPKPrinterLastUsedSizeSymbolLoc_block_invoke
- ___getPKPrinterNameKeySymbolLoc_block_invoke
- ___getPKQualityHighSymbolLoc_block_invoke
- ___getPKQualityKeySymbolLoc_block_invoke
- ___getPKQualityNormalSymbolLoc_block_invoke
- ___printInfoRequests
- __block_literal_global.55
- __getPKDefaultsClass_block_invoke.cold.1
- __getPKPaperClass_block_invoke.cold.1
- __getPKPrintSettingsClass_block_invoke.cold.1
- __getPKPrinterClass_block_invoke.cold.1
- __sl_dlopen
- _abort_report_np
- _audit_stringPrintKit
- _dlerror
- _dlsym
- _getPKCopiesKey
- _getPKDefaultsClass
- _getPKDuplexKey
- _getPKDuplexLandscape
- _getPKDuplexNone
- _getPKDuplexPortrait
- _getPKFinishingsKey
- _getPKJobNameKey
- _getPKJobPresetFinishingsKey
- _getPKJobPresetMediaSourceKey
- _getPKJobPresetMediaTypeKey
- _getPKJobPresetOptionKey
- _getPKOrientationKey
- _getPKOrientationLandscape
- _getPKOrientationPortrait
- _getPKOrientationReverseLandscape
- _getPKOutputModeColor
- _getPKOutputModeGray
- _getPKOutputModeKey
- _getPKPaperClass
- _getPKQualityHigh
- _getPKQualityKey
- _getPKQualityNormal
- _objc_begin_catch
- _objc_end_catch
- _objc_getClass
- _objc_msgSend$_addPDFWithData:toContext:
- _objc_msgSend$_canShowPreview
- _objc_msgSend$_drawPage:
- _objc_msgSend$_drawPageWithItem:toContext:
- _objc_msgSend$_endPrintContext:success:
- _objc_msgSend$_pageData
- _objc_msgSend$_respondWithResults:
- _objc_msgSend$_setPrintInfoState:
- _objc_msgSend$_startPrintContext:printSettings:
- _objc_msgSend$attachments
- _objc_msgSend$completeRequestReturningItems:completionHandler:
- _objc_msgSend$dismissAnimated:
- _objc_msgSend$drawAllPagesWithPreviewState:
- _objc_msgSend$extensionContext
- _objc_msgSend$hasItemConformingToTypeIdentifier:
- _objc_msgSend$initWithItem:typeIdentifier:
- _objc_msgSend$initWithPDFData:
- _objc_msgSend$initWithPDFURL:
- _objc_msgSend$inputItems
- _objc_msgSend$loadItemForTypeIdentifier:options:completionHandler:
- _objc_msgSend$presentAnimated:completionHandler:
- _objc_msgSend$rangeOfString:
- _objc_msgSend$requestPrintInfo
- _objc_msgSend$setAttachments:
- _objc_msgSend$setExtensionContext:
- _objc_msgSend$substringFromIndex:
- _objc_msgSend$substringToIndex:
- _objc_msgSend$thumbnailSizeForPageNum:
- _startPrintContext:printSettings:.__consumerCallbacks
- getPKAnnotationsImagedKeySymbolLoc.ptr
- getPKCopiesKey.cold.1
- getPKCopiesKeySymbolLoc.ptr
- getPKDefaultsClass.softClass
- getPKDocumentPasswordKeySymbolLoc.ptr
- getPKDrawImageToSheetSymbolLoc.ptr
- getPKDuplexKey.cold.1
- getPKDuplexKeySymbolLoc.ptr
- getPKDuplexLandscape.cold.1
- getPKDuplexLandscapeSymbolLoc.ptr
- getPKDuplexNone.cold.1
- getPKDuplexNoneSymbolLoc.ptr
- getPKDuplexPortrait.cold.1
- getPKDuplexPortraitSymbolLoc.ptr
- getPKFileTypePDFSymbolLoc.ptr
- getPKFinishingTemplateKeySymbolLoc.ptr
- getPKFinishingsKey.cold.1
- getPKFinishingsKeySymbolLoc.ptr
- getPKInputSlotKeySymbolLoc.ptr
- getPKJobAccountIDKeySymbolLoc.ptr
- getPKJobNameKey.cold.1
- getPKJobNameKeySymbolLoc.ptr
- getPKJobPresetFinishingsKey.cold.1
- getPKJobPresetFinishingsKeySymbolLoc.ptr
- getPKJobPresetKeySymbolLoc.ptr
- getPKJobPresetMediaSourceKey.cold.1
- getPKJobPresetMediaSourceKeySymbolLoc.ptr
- getPKJobPresetMediaTypeKey.cold.1
- getPKJobPresetMediaTypeKeySymbolLoc.ptr
- getPKJobPresetOptionKey.cold.1
- getPKJobPresetOptionKeySymbolLoc.ptr
- getPKMediaTypeKeySymbolLoc.ptr
- getPKOrientationKey.cold.1
- getPKOrientationKeySymbolLoc.ptr
- getPKOrientationLandscape.cold.1
- getPKOrientationLandscapeSymbolLoc.ptr
- getPKOrientationPortrait.cold.1
- getPKOrientationPortraitSymbolLoc.ptr
- getPKOrientationReverseLandscape.cold.1
- getPKOrientationReverseLandscapeSymbolLoc.ptr
- getPKOutputBinKeySymbolLoc.ptr
- getPKOutputModeColor.cold.1
- getPKOutputModeColorSymbolLoc.ptr
- getPKOutputModeGray.cold.1
- getPKOutputModeGraySymbolLoc.ptr
- getPKOutputModeKey.cold.1
- getPKOutputModeKeySymbolLoc.ptr
- getPKPageStackOrderKeySymbolLoc.ptr
- getPKPaperClass.softClass
- getPKPrintSettingsClass.softClass
- getPKPrinterClass.softClass
- getPKPrinterLastUsedSizeSymbolLoc.ptr
- getPKPrinterNameKeySymbolLoc.ptr
- getPKQualityHigh.cold.1
- getPKQualityHighSymbolLoc.ptr
- getPKQualityKey.cold.1
- getPKQualityKeySymbolLoc.ptr
- getPKQualityNormal.cold.1
- getPKQualityNormalSymbolLoc.ptr
CStrings:
+ " "
+ "@\"NSURL\"16@0:8"
+ "B16@?0@\"NSTextLayoutFragment\"8"
+ "B40@0:8@16@24@32"
+ "Protected PDF files can only be printed separately."
+ "T@\"NSArray\",&,N,V_pageData"
+ "T@\"NSArray\",&,V_pageRanges"
+ "T@\"NSDictionary\",&,V_printerInfo"
+ "T@\"NSObject\",&,V_webKitFormatterMutex"
+ "TB,N,V_calculatingUsedRects"
+ "TB,N,V_initializedUsedRects"
+ "TB,N,V_preventPDFCreation"
+ "TB,V_usingWebKitFormatter"
+ "Ti,V_printerInfoState"
+ "Tq,V_pageCount"
+ "UIPrintMessageAndSpinnerView"
+ "UIPrinterInfoRequest"
+ "_WKWebViewPrintFormatter"
+ "_addPDFWithData:toContext:addAllPages:"
+ "_alertWindow"
+ "_apOp:reply:"
+ "_authenticatedRequestForRequest:challengeResponse:reply:"
+ "_calculatingUsedRects"
+ "_canPreviewContent"
+ "_createDocInfoDict"
+ "_drawPage:withScale:drawingToPDF:"
+ "_drawPrintItem:toContext:printAllPages:"
+ "_endPrintJobContext"
+ "_initializedUsedRects"
+ "_preventPDFCreation"
+ "_printItemContentSize:"
+ "_printPageWithRenderer:"
+ "_printerInfoState"
+ "_setPrinterInfoState:"
+ "_startPrintJobContext:"
+ "_startPrintJobContext:printInfo:printSettings:"
+ "_usingPrintJobContext"
+ "_usingWebKitFormatter"
+ "_webKitFormatterMutex"
+ "addPrinterToiCloud:displayName:location:"
+ "adjustedPageBottom:"
+ "appOptionsViewController"
+ "appendString:"
+ "calculatingUsedRects"
+ "com.apple.iwork"
+ "createWebKitPDFForAllPages"
+ "currentThread"
+ "d24@0:8d16"
+ "dismissAnimated:completionHandler:"
+ "documentRange"
+ "drawAtPoint:inContext:"
+ "drawImage:toContext:sheetSize:"
+ "drawImageForPageNum:toContext:sheetSize:"
+ "drawPagesWithPreviewState:"
+ "ensureLayoutForRange:"
+ "enumerateTextLayoutFragmentsFromLocation:options:usingBlock:"
+ "glossy"
+ "hasPrefix:"
+ "initWithPDFData:pdfPassword:"
+ "initWithPDFURL:pdfPassword:"
+ "initializedUsedRects"
+ "isCancelled"
+ "lastPathComponent"
+ "layoutFragmentFrame"
+ "localizedStringFromNumber:numberStyle:"
+ "matte"
+ "media-type"
+ "mediaInfo"
+ "numberWithUnsignedInteger:"
+ "pageData"
+ "paperSizeForPageNum:"
+ "pathExtension"
+ "preventPDFCreation"
+ "printerInfo"
+ "printerInfoState"
+ "recalculateWebKitPageCount"
+ "removeObjectsInArray:"
+ "requestPrinterInfo"
+ "setCalculatingUsedRects:"
+ "setInitializedUsedRects:"
+ "setPageData:"
+ "setPreventPDFCreation:"
+ "setPrinterInfo:"
+ "setPrinterInfoState:"
+ "setUsingWebKitFormatter:"
+ "setWebKitFormatterMutex:"
+ "stationery"
+ "stringByDeletingPathExtension"
+ "textContainerOrigin"
+ "textContentManager"
+ "textLayoutFragmentForPosition:"
+ "textLayoutManager"
+ "textLineFragmentForVerticalOffset:requiresExactMatch:"
+ "textLineFragments"
+ "typeWithFilenameExtension:"
+ "typographicBounds"
+ "updatePrintingItems"
+ "usageBoundsForTextContainer"
+ "usingWebKitFormatter"
+ "v32@0:8@\"NSDictionary\"16@?<v@?@\"NSDictionary\">24"
+ "v32@?0@\"NSTextLineFragment\"8Q16^B24"
+ "v36@0:8@16^{CGContext=}24B32"
+ "v36@0:8q16d24B32"
+ "v40@0:8@\"NSURLRequest\"16@\"NSHTTPURLResponse\"24@?<v@?@\"NSURLRequest\">32"
+ "v40@0:8@16@24@?32"
+ "v48@0:8@16^{CGContext=}24{CGSize=dd}32"
+ "webKitFormatterMutex"
+ "\xf1\xf0Q"
- " @ "
- "%s"
- "@\"NSExtensionContext\""
- "@\"UIViewController<UIPrintAppExtensionProtocol>\""
- "B32@0:8@16@24"
- "NSExtensionRequestHandling"
- "PKAnnotationsImagedKey"
- "PKCopiesKey"
- "PKDefaults"
- "PKDocumentPasswordKey"
- "PKDrawImageToSheet"
- "PKDuplexKey"
- "PKDuplexLandscape"
- "PKDuplexNone"
- "PKDuplexPortrait"
- "PKFileTypePDF"
- "PKFinishingTemplateKey"
- "PKFinishingsKey"
- "PKInputSlotKey"
- "PKJobAccountIDKey"
- "PKJobNameKey"
- "PKJobPresetFinishingsKey"
- "PKJobPresetKey"
- "PKJobPresetMediaSourceKey"
- "PKJobPresetMediaTypeKey"
- "PKJobPresetOptionKey"
- "PKMediaTypeKey"
- "PKOrientationKey"
- "PKOrientationLandscape"
- "PKOrientationPortrait"
- "PKOrientationReverseLandscape"
- "PKOutputBinKey"
- "PKOutputModeColor"
- "PKOutputModeGray"
- "PKOutputModeKey"
- "PKPageStackOrderKey"
- "PKPaper"
- "PKPrintSettings"
- "PKPrinter"
- "PKPrinterLastUsedSize"
- "PKPrinterNameKey"
- "PKQualityHigh"
- "PKQualityKey"
- "PKQualityNormal"
- "Rotate"
- "T@\"NSExtensionContext\",&,N,V_extensionContext"
- "T@\"UIViewController<UIPrintAppExtensionProtocol>\",&,N,V_appPrintExtensionController"
- "Ti,V_printInfoState"
- "UIPrintInfoRequest"
- "Unable to find class %s"
- "Wireless Printing"
- "_UIPrintMessageAndSpinnerView"
- "_addPDFWithData:toContext:"
- "_appPrintExtensionController"
- "_drawPage:"
- "_drawPageWithItem:toContext:"
- "_endPrintContext:success:"
- "_extensionContext"
- "_generatePDFForQuickLookCompletion:"
- "_passwordAlertWindow"
- "_printInfoState"
- "_printPageRenderer:"
- "_respondWithResults:"
- "_setPrintInfoState:"
- "_startPrintContext:printSettings:"
- "_textViewPrintFormatterFlags"
- "appPrintExtensionController"
- "attachments"
- "beginRequestWithExtensionContext:"
- "completeRequestReturningItems:completionHandler:"
- "drawAllPagesWithPreviewState:"
- "drawThumbnailImageForPageNum:toContext:sheetSize:"
- "extensionContext"
- "hasItemConformingToTypeIdentifier:"
- "initWithItem:typeIdentifier:"
- "initWithPDFData:"
- "initWithPDFURL:"
- "inputItems"
- "loadItemForTypeIdentifier:options:completionHandler:"
- "printInfoState"
- "rangeOfString:"
- "requestPrintInfo"
- "setAppPrintExtensionController:"
- "setAttachments:"
- "setExtensionContext:"
- "setPrintInfoState:"
- "softlink:r:path:/System/Library/PrivateFrameworks/PrintKit.framework/PrintKit"
- "substringFromIndex:"
- "substringToIndex:"
- "thumbnailSizeForPageNum:"
- "v24@0:8@\"NSExtensionContext\"16"
- "v24@?0@\"NSDictionary\"8@\"NSError\"16"
- "v24@?0@\"NSURL\"8B16B20"
- "v32@0:8@16^{CGContext=}24"
- "{?=\"initializedUsedRects\"b1}"
- "\xf1\xf0A"

```
