## SBRendererService

> `/System/Library/PrivateFrameworks/PaperBoardUI.framework/XPCServices/SBRendererService.xpc/SBRendererService`

```diff

-228.1.7.0.0
-  __TEXT.__text: 0x52fc
-  __TEXT.__auth_stubs: 0x520
-  __TEXT.__objc_stubs: 0x10c0
+228.1.7.100.0
+  __TEXT.__text: 0x4464
+  __TEXT.__auth_stubs: 0x4c0
+  __TEXT.__objc_stubs: 0xd20
   __TEXT.__objc_methlist: 0x364
-  __TEXT.__cstring: 0x732
-  __TEXT.__objc_classname: 0x157
-  __TEXT.__objc_methname: 0xfe6
+  __TEXT.__cstring: 0x665
+  __TEXT.__const: 0x50
+  __TEXT.__gcc_except_tab: 0x20c
+  __TEXT.__objc_methname: 0xe03
+  __TEXT.__objc_classname: 0x156
   __TEXT.__objc_methtype: 0x4e2
-  __TEXT.__const: 0x48
-  __TEXT.__gcc_except_tab: 0x324
-  __TEXT.__oslogstring: 0x3da
-  __TEXT.__dlopen_cstrs: 0xac
+  __TEXT.__oslogstring: 0x351
   __TEXT.__unwind_info: 0x228
-  __DATA_CONST.__auth_got: 0x2a0
-  __DATA_CONST.__got: 0x148
-  __DATA_CONST.__const: 0x478
-  __DATA_CONST.__cfstring: 0x420
+  __DATA_CONST.__auth_got: 0x270
+  __DATA_CONST.__got: 0x120
+  __DATA_CONST.__const: 0x2f8
+  __DATA_CONST.__cfstring: 0x340
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x40

   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x28
   __DATA.__objc_const: 0x1768
-  __DATA.__objc_selrefs: 0x488
+  __DATA.__objc_selrefs: 0x3a0
   __DATA.__objc_ivar: 0x4c
   __DATA.__objc_data: 0x1e0
   __DATA.__data: 0x300
-  __DATA.__bss: 0x90
+  __DATA.__bss: 0x4c
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/CoreImage.framework/CoreImage

   - /System/Library/PrivateFrameworks/PosterFoundation.framework/PosterFoundation
   - /System/Library/PrivateFrameworks/PosterKit.framework/PosterKit
   - /System/Library/PrivateFrameworks/PosterUIFoundation.framework/PosterUIFoundation
-  - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 128
-  Symbols:   155
-  CStrings:  351
+  Functions: 113
+  Symbols:   144
+  CStrings:  305
 
Symbols:
+ _CFAbsoluteTimeGetCurrent
+ _PRUISExecuteProminentColorAnalysisOnImage
- _OBJC_CLASS_$_CIImage
- _OBJC_CLASS_$_NSDate
- _OBJC_CLASS_$_NSRunLoop
- _OBJC_CLASS_$_UIColor
- __dispatch_main_q
- __os_log_fault_impl
- __sl_dlopen
- _abort_report_np
- _free
- _objc_getClass
- _objc_release_x27
- _objc_retain_x25
- _objc_retain_x27
CStrings:
+ "(%!d(MISSING)) end %!{(MISSING)public}s (serviced in %!f(MISSING) s)"
+ "(%!d(MISSING)) start %!s(MISSING)"
+ "(%!d(MISSING)) start %!{(MISSING)public}s"
+ "-[SBRendererServiceConnection cancelRequest:]"
+ "-[SBRendererServiceConnection executeAnalysisRequest:error:]"
+ "-[SBRendererServiceConnection executeAnalysisRequest:reply:]"
+ "-[SBRendererServiceConnection executeAnalysisRequest:reply:]_block_invoke"
+ "serviceListener"
+ "setMaxConcurrentOperationCount:"
+ "v24@?0@\"PRUISAnalysisServiceResponse\"8@\"NSError\"16"
- "%!s(MISSING)"
- "@16@?0@\"PFParallaxColor\"8"
- "B16@?0@\"UIColor\"8"
- "CGColor"
- "NUCIImageSourceDefinition"
- "NUGenericComposition"
- "NURenderContext"
- "NUSource"
- "PIParallaxColorAnalysisRequest"
- "PISchema"
- "PhotoImaging did not return a result."
- "PhotoImaging did not return any colors."
- "PhotosImaging was unable to register schema information."
- "Timed out."
- "UUID"
- "Unable to find class %!s(MISSING)"
- "_determineProminentColor failed to run w/ error: %!{(MISSING)public}@"
- "_determineProminentColor ran successfully"
- "_setQueue:"
- "bs_filter:"
- "bs_mapNoNulls:"
- "colorWithCGColor:"
- "com.apple.springboard.SBRendererService"
- "determineProminentColorWithCompletion elapsed 20 second timer."
- "determineProminentColorWithCompletion finished"
- "distantFuture"
- "dominantColors"
- "imageByColorMatchingWorkingSpaceToColorSpace:"
- "initWithCGImage:"
- "initWithCIImage:orientation:"
- "initWithComposition:"
- "initWithIdentifier:"
- "initWithMachServiceName:"
- "initWithPurpose:"
- "luminance"
- "mainRunLoop"
- "pui_hsbValues"
- "pui_hslValues"
- "q24@?0@\"UIColor\"8@\"UIColor\"16"
- "registerPhotosSchema"
- "result:"
- "runUntilDate:"
- "saturation"
- "setAnalyzeBackground:"
- "setAssetIdentifier:"
- "setDefinition:"
- "setMaxDominantColors:"
- "setRenderContext:"
- "setSegmentationMatte:"
- "softlink:r:path:/System/Library/PrivateFrameworks/NeutrinoCore.framework/NeutrinoCore"
- "softlink:r:path:/System/Library/PrivateFrameworks/PhotoImaging.framework/PhotoImaging"
- "sortedArrayUsingComparator:"
- "source"
- "source image deallocated before prominent color analysis could be run."
- "submit:"
- "v16@?0@\"NUResponse\"8"

```
