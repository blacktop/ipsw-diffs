## SBRendererService

> `/System/Library/PrivateFrameworks/PaperBoardUI.framework/XPCServices/SBRendererService.xpc/SBRendererService`

```diff

-227.2.0.0.0
-  __TEXT.__text: 0x23e8
-  __TEXT.__auth_stubs: 0x400
-  __TEXT.__objc_stubs: 0x8e0
-  __TEXT.__objc_methlist: 0x1d4
-  __TEXT.__cstring: 0x457
-  __TEXT.__objc_classname: 0xd1
-  __TEXT.__objc_methname: 0x9d2
-  __TEXT.__objc_methtype: 0x2ea
-  __TEXT.__const: 0x40
-  __TEXT.__oslogstring: 0x306
-  __TEXT.__gcc_except_tab: 0x54
-  __TEXT.__unwind_info: 0x128
-  __DATA_CONST.__auth_got: 0x210
-  __DATA_CONST.__got: 0xf0
-  __DATA_CONST.__const: 0x1c0
-  __DATA_CONST.__cfstring: 0x240
-  __DATA_CONST.__objc_classlist: 0x18
+228.1.4.1.0
+  __TEXT.__text: 0x5394
+  __TEXT.__auth_stubs: 0x510
+  __TEXT.__objc_stubs: 0x10c0
+  __TEXT.__objc_methlist: 0x364
+  __TEXT.__cstring: 0x732
+  __TEXT.__objc_classname: 0x157
+  __TEXT.__objc_methname: 0xfe6
+  __TEXT.__objc_methtype: 0x4e2
+  __TEXT.__const: 0x48
+  __TEXT.__gcc_except_tab: 0x380
+  __TEXT.__oslogstring: 0x3da
+  __TEXT.__dlopen_cstrs: 0xac
+  __TEXT.__unwind_info: 0x220
+  __DATA_CONST.__auth_got: 0x298
+  __DATA_CONST.__got: 0x148
+  __DATA_CONST.__const: 0x478
+  __DATA_CONST.__cfstring: 0x420
+  __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_catlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x28
+  __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x10
-  __DATA.__objc_const: 0x890
-  __DATA.__objc_selrefs: 0x288
-  __DATA.__objc_ivar: 0x1c
-  __DATA.__objc_data: 0xf0
-  __DATA.__data: 0x1e0
-  __DATA.__bss: 0x30
+  __DATA_CONST.__objc_superrefs: 0x28
+  __DATA.__objc_const: 0x1768
+  __DATA.__objc_selrefs: 0x488
+  __DATA.__objc_ivar: 0x4c
+  __DATA.__objc_data: 0x1e0
+  __DATA.__data: 0x300
+  __DATA.__bss: 0x90
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
+  - /System/Library/Frameworks/CoreImage.framework/CoreImage
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/QuartzCore.framework/QuartzCore
   - /System/Library/Frameworks/UIKit.framework/UIKit

   - /System/Library/PrivateFrameworks/PosterFoundation.framework/PosterFoundation
   - /System/Library/PrivateFrameworks/PosterKit.framework/PosterKit
   - /System/Library/PrivateFrameworks/PosterUIFoundation.framework/PosterUIFoundation
+  - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 63
-  Symbols:   117
-  CStrings:  208
+  Functions: 129
+  Symbols:   154
+  CStrings:  351
 
Symbols:
+ _SBRSLogImageAnalysis
+ _objc_sync_enter
+ _objc_retain
+ _PRUISAnalysisDetermineProminentColor
+ _abort_report_np
+ _objc_release_x9
+ _OBJC_CLASS_$_UIColor
+ _OBJC_METACLASS_$_SBImageAnalysisServer
+ _OBJC_CLASS_$_PRUISAnalysisService
+ _OBJC_METACLASS_$_SBImageAnalyzerOperation
+ _free
+ _os_transaction_create
+ _objc_sync_exit
+ _OBJC_CLASS_$_SBImageAnalyzer
+ _objc_retain_x25
+ _OBJC_CLASS_$_NSOperationQueue
+ _objc_release_x27
+ _NSMultipleUnderlyingErrorsKey
+ _objc_getClass
+ _OBJC_CLASS_$_CIImage
+ _OBJC_CLASS_$_NSArray
+ _OBJC_METACLASS_$_SBImageAnalyzer
+ _OBJC_CLASS_$_SBImageAnalyzerOperation
+ _OBJC_METACLASS_$_NSBlockOperation
+ _OBJC_CLASS_$_NSProgress
+ _OBJC_CLASS_$_SBImageAnalysisServer
+ __sl_dlopen
+ _objc_retain_x24
+ _OBJC_CLASS_$_PRUISAnalysisServiceResponse
+ _OBJC_CLASS_$_NSBlockOperation
+ _objc_getProperty
+ _OBJC_CLASS_$_NSMutableArray
+ _OBJC_CLASS_$_NSDictionary
+ __os_log_fault_impl
+ _dispatch_time
+ _objc_autorelease
+ _objc_retain_x27
CStrings:
+ "\x01"
+ "PRUISAnalyzer"
+ "dominantColors"
+ "T@\"PRUISAnalysisServiceResponse\",R,N,V_response"
+ "@\"SBImageAnalyzer\""
+ "@40@0:8@16@24@32"
+ "PISchema"
+ "T@\"PRUISAnalysisServiceRequest\",R,N,V_request"
+ "no results were returned"
+ "PRUISAnalysisServiceInterface"
+ "_self_invalidate"
+ "dictionaryWithObjects:forKeys:count:"
+ "%!s(MISSING)"
+ "@\"PRUISAnalysisServiceRequest\""
+ "NSProgressReporting"
+ "NUSource"
+ "@\"PRUISAnalysisServiceResponse\"32@0:8@\"PRUISAnalysisServiceRequest\"16o^@24"
+ "arrayWithObjects:count:"
+ "\t"
+ "initWithIdentifier:"
+ "_request"
+ "analysisServer"
+ "bs_filter:"
+ "NURenderContext"
+ "addOperations:waitUntilFinished:"
+ "imageByColorMatchingWorkingSpaceToColorSpace:"
+ "PhotoImaging did not return any colors."
+ "SBImageAnalyzer"
+ "executeAnalysisRequest:completion:"
+ "pui_hsbValues"
+ "setMaxDominantColors:"
+ "T@\"SBImageAnalysisServer\",R,N,V_analysisServer"
+ "registerPhotosSchema"
+ "unknown error"
+ "initWithRequest:completion:"
+ "@16@?0@\"PFParallaxColor\"8"
+ "PhotoImaging did not return a result."
+ "_operationQueue"
+ "cancelRequest:"
+ "initWithComposition:"
+ "BSInvalidatable"
+ "SBImageAnalysisServer"
+ "_determineProminentColor failed to run w/ error: %!{(MISSING)public}@"
+ "initWithPurpose:"
+ "source"
+ "T@\"NSError\",R,N,V_error"
+ "error"
+ "secureCodableResponseClasses"
+ "setAnalyzeBackground:"
+ "setSegmentationMatte:"
+ "initWithCIImage:orientation:"
+ "q24@?0@\"UIColor\"8@\"UIColor\"16"
+ "setCompletionBlock:"
+ "@32@0:8@16@?24"
+ "isEqualToString:"
+ "v24@?0@\"UIColor\"8@\"NSError\"16"
+ "determineProminentColorWithCompletion finished"
+ "requestIdentifier"
+ "@\"NSProgress\""
+ "Unable to find class %!s(MISSING)"
+ "setDefinition:"
+ "CGColor"
+ "_determineProminentColor"
+ "cancel"
+ "pui_hslValues"
+ "_accumulatedErrors"
+ "colorWithCGColor:"
+ "initWithRenderService:snapshotServer:analysisServer:"
+ "v24@?0@\"NSString\"8^B16"
+ "addExecutionBlock:"
+ "determineProminentColorWithCompletion elapsed 20 second timer."
+ "@\"NSOperationQueue\""
+ "Timed out."
+ "_progress"
+ "bs_mapNoNulls:"
+ "@\"BSAtomicSignal\""
+ "_firedCompletionSignal"
+ "NUCIImageSourceDefinition"
+ "response"
+ "setAssetIdentifier:"
+ "_analyzer"
+ "progress"
+ "NUGenericComposition"
+ "invalidated"
+ "_analysisServer"
+ "softlink:r:path:/System/Library/PrivateFrameworks/PhotoImaging.framework/PhotoImaging"
+ "@\"NSError\""
+ "@\"NSProgress\"16@0:8"
+ "sortedArrayUsingComparator:"
+ "UUID"
+ "_prominentColor"
+ "operations"
+ "luminance"
+ "result:"
+ "v24@0:8@\"PRUISAnalysisServiceRequest\"16"
+ "@\"UIColor\""
+ "PIParallaxColorAnalysisRequest"
+ "PhotosImaging was unable to register schema information."
+ "firstObject"
+ "progressWithTotalUnitCount:"
+ "addOperation:"
+ "request"
+ "setCancellationHandler:"
+ "submit:"
+ "T@\"NSProgress\",R"
+ "_error"
+ "_hasError"
+ "enumerateObjectsUsingBlock:"
+ "setRenderContext:"
+ "v16@?0@\"NUResponse\"8"
+ "executeAnalysisRequest:reply:"
+ "cancelled."
+ "setName:"
+ "@\"NSProgress\"32@0:8@\"PRUISAnalysisServiceRequest\"16@?<v@?@\"PRUISAnalysisServiceResponse\"@\"NSError\">24"
+ "@\"SBImageAnalysisServer\""
+ "@32@0:8@16o^@24"
+ "SBImageAnalyzerOperation"
+ "_determineProminentColor ran successfully"
+ "saturation"
+ "image"
+ "softlink:r:path:/System/Library/PrivateFrameworks/NeutrinoCore.framework/NeutrinoCore"
+ "executeAnalysisRequest:error:"
+ "@\"PRUISAnalysisServiceResponse\""
+ "CGImage"
+ "_completionBlock"
+ "B16@?0@\"UIColor\"8"
+ "T@\"NSProgress\",R,V_progress"
+ "_setupAnalysisOperations"
+ "@\"NSObject<OS_os_transaction>\""
+ "SBImageAnalyzerOperation servicing request %!@(MISSING)"
+ "multiple crippling failures were experienced"
+ "_osTransaction"
+ "com.apple.PaperBoardUI"
+ "requestedAnalyses"
+ "ImageAnalysis"
+ "_response"
+ "count"
+ "source image deallocated before prominent color analysis could be run."
+ "@?"
+ "addBarrierBlock:"
+ "initWithRequestIdentifier:reports:"
+ "@\"NSMutableArray\""
+ "_fireCompletionWithError:"
+ "initWithCGImage:"
- "initWithRenderService:snapshotServer:"
- "@32@0:8@16@24"

```
