## PosterBoardUIServices

> `/System/Library/PrivateFrameworks/PosterBoardUIServices.framework/PosterBoardUIServices`

```diff

-228.1.7.0.0
-  __TEXT.__text: 0x27c14
-  __TEXT.__auth_stubs: 0x7c0
-  __TEXT.__objc_methlist: 0x2c80
-  __TEXT.__const: 0x170
-  __TEXT.__cstring: 0x1a0f
-  __TEXT.__gcc_except_tab: 0x630
-  __TEXT.__oslogstring: 0x187d
-  __TEXT.__unwind_info: 0xc40
-  __TEXT.__objc_classname: 0xd42
-  __TEXT.__objc_methname: 0x9584
-  __TEXT.__objc_methtype: 0x1cc2
-  __TEXT.__objc_stubs: 0x6a80
-  __DATA_CONST.__got: 0x660
-  __DATA_CONST.__const: 0xed0
-  __DATA_CONST.__objc_classlist: 0x208
+228.1.7.100.0
+  __TEXT.__text: 0x28a10
+  __TEXT.__auth_stubs: 0x870
+  __TEXT.__objc_methlist: 0x2bd0
+  __TEXT.__const: 0x188
+  __TEXT.__cstring: 0x1df3
+  __TEXT.__gcc_except_tab: 0x63c
+  __TEXT.__oslogstring: 0x19ac
+  __TEXT.__dlopen_cstrs: 0xac
+  __TEXT.__unwind_info: 0xc80
+  __TEXT.__objc_classname: 0xcc1
+  __TEXT.__objc_methname: 0x96da
+  __TEXT.__objc_methtype: 0x1ac3
+  __TEXT.__objc_stubs: 0x6d20
+  __DATA_CONST.__got: 0x650
+  __DATA_CONST.__const: 0x1048
+  __DATA_CONST.__objc_classlist: 0x1f8
   __DATA_CONST.__objc_catlist: 0x40
-  __DATA_CONST.__objc_protolist: 0x110
+  __DATA_CONST.__objc_protolist: 0x100
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2108
-  __DATA_CONST.__objc_protorefs: 0x38
-  __DATA_CONST.__objc_superrefs: 0x180
-  __AUTH_CONST.__auth_got: 0x3f0
-  __AUTH_CONST.__const: 0x640
-  __AUTH_CONST.__cfstring: 0x1940
-  __AUTH_CONST.__objc_const: 0xad38
+  __DATA_CONST.__objc_selrefs: 0x21b0
+  __DATA_CONST.__objc_protorefs: 0x28
+  __DATA_CONST.__objc_superrefs: 0x170
+  __AUTH_CONST.__auth_got: 0x448
+  __AUTH_CONST.__const: 0x700
+  __AUTH_CONST.__cfstring: 0x1a20
+  __AUTH_CONST.__objc_const: 0xa700
   __AUTH_CONST.__objc_intobj: 0x48
-  __AUTH.__objc_data: 0xb90
-  __DATA.__objc_ivar: 0x360
-  __DATA.__data: 0xd08
-  __DATA.__bss: 0xc0
+  __AUTH.__objc_data: 0xaf0
+  __DATA.__objc_ivar: 0x344
+  __DATA.__data: 0xc48
+  __DATA.__bss: 0x138
   __DATA_DIRTY.__objc_data: 0x8c0
   __DATA_DIRTY.__bss: 0xc8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
+  - /System/Library/Frameworks/CoreImage.framework/CoreImage
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/ExtensionFoundation.framework/ExtensionFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/PosterKit.framework/PosterKit
   - /System/Library/PrivateFrameworks/PosterUIFoundation.framework/PosterUIFoundation
   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
+  - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1182
-  Symbols:   1689
-  CStrings:  2162
+  Functions: 1196
+  Symbols:   1709
+  CStrings:  2202
 
Symbols:
+ _BSDispatchQueueCreateSerial
+ _CGColorSpaceCreateWithName
+ _CGColorSpaceRelease
+ _OBJC_CLASS_$_CIImage
+ _OBJC_CLASS_$_PBUIRemoteRendererXPCConnection
+ _OBJC_CLASS_$_PFOSTransactionQueue
+ _PRUISExecuteProminentColorAnalysisOnImage
+ _PRUISLogAnalysis
+ __os_signpost_emit_with_name_impl
+ __sl_dlopen
+ _dispatch_group_wait
+ _free
+ _kCGColorSpaceSRGB
+ _objc_autoreleasePoolPop
+ _objc_autoreleasePoolPush
+ _objc_getClass
+ _objc_retain_x27
+ _os_signpost_enabled
+ _os_signpost_id_generate
- _NSLocalizedFailureErrorKey
- _NSPOSIXErrorDomain
- _OBJC_CLASS_$_NSXPCConnection
- _OBJC_CLASS_$_NSXPCInterface
- _OBJC_CLASS_$_SBSnapshotServiceXPCConnection
- _OBJC_CLASS_$__PRUISAnalysisServiceXPCConnection
- _OBJC_METACLASS_$_SBSnapshotServiceXPCConnection
- _OBJC_METACLASS_$__PRUISAnalysisServiceXPCConnection
- _os_unfair_recursive_lock_lock_with_options
- _os_unfair_recursive_lock_unlock
CStrings:
+ "%!s(MISSING)"
+ "(%!d(MISSING)) end %!{(MISSING)public}s; completed in %!f(MISSING) / %!{(MISSING)public}@"
+ "(%!d(MISSING)) start %!{(MISSING)public}s"
+ "@\"PBUIRemoteRendererXPCConnection\""
+ "@16@?0@\"PFParallaxColor\"8"
+ "Analysis"
+ "B16@?0@\"UIColor\"8"
+ "BOOL PRUISExecuteProminentColorAnalysisOnImage(CGImageRef _Nonnull, void (^__strong _Nonnull)(UIColor *__strong, NSError *__strong))"
+ "BOOL PRUISExecuteProminentColorAnalysisOnImage(CGImageRef _Nonnull, void (^__strong _Nonnull)(UIColor *__strong, NSError *__strong))_block_invoke"
+ "CGColor"
+ "Class getNUCIImageSourceDefinitionClass(void)_block_invoke"
+ "Class getNUGenericCompositionClass(void)_block_invoke"
+ "Class getNURenderContextClass(void)_block_invoke"
+ "Class getNUSourceClass(void)_block_invoke"
+ "Class getPIParallaxColorAnalysisRequestClass(void)_block_invoke"
+ "Class getPISchemaClass(void)_block_invoke"
+ "NUCIImageSourceDefinition"
+ "NUGenericComposition"
+ "NURenderContext"
+ "NUSource"
+ "PIParallaxColorAnalysisRequest"
+ "PISchema"
+ "PRUISAnalyses.m"
+ "PhotoImaging did not return a result."
+ "PhotoImaging did not return any colors."
+ "PhotosImaging was unable to register schema information."
+ "ProminentColor"
+ "Timed out."
+ "Unable to find class %!s(MISSING)"
+ "_copyIOSurface"
+ "_determineProminentColor failed to run w/ error: %!{(MISSING)public}@"
+ "_determineProminentColor ran successfully"
+ "_timeoutQueue"
+ "cancelAllRequests"
+ "colorWithCGColor:"
+ "com.apple.PosterBoardUIServices.analysisService"
+ "determineProminentColorWithCompletion elapsed 20 second timer."
+ "determineProminentColorWithCompletion finished"
+ "dispatchAsync:"
+ "dominantColors"
+ "handleFailureInFunction:file:lineNumber:description:"
+ "imageByColorMatchingWorkingSpaceToColorSpace:"
+ "initWithCGImage:"
+ "initWithCIImage:orientation:"
+ "initWithComposition:"
+ "initWithIOSurface:scale:error:"
+ "initWithPurpose:"
+ "initWithTransactionName:"
+ "initWithUnderlyingConnection:"
+ "luminance"
+ "nil input image"
+ "prominent color"
+ "prominent color was nil"
+ "pui_hsbValues"
+ "pui_hslValues"
+ "q24@?0@\"UIColor\"8@\"UIColor\"16"
+ "registerPhotosSchema"
+ "result:"
+ "saturation"
+ "setAnalyzeBackground:"
+ "setAssetIdentifier:"
+ "setMaxDominantColors:"
+ "setRenderContext:"
+ "setSegmentationMatte:"
+ "softlink:r:path:/System/Library/PrivateFrameworks/NeutrinoCore.framework/NeutrinoCore"
+ "softlink:r:path:/System/Library/PrivateFrameworks/PhotoImaging.framework/PhotoImaging"
+ "sortedArrayUsingComparator:"
+ "source"
+ "source image deallocated before prominent color analysis could be run."
+ "stringWithUTF8String:"
+ "submit:"
+ "v16@?0@\"NUResponse\"8"
+ "v24@?0@\"UIColor\"8@\"NSError\"16"
+ "void *NeutrinoCoreLibrary(void)"
+ "void *PhotoImagingLibrary(void)"
- "\x02\x11"
- "@\"NSProgress\"32@0:8@\"PRUISAnalysisServiceRequest\"16@?<v@?@\"PRUISAnalysisServiceResponse\"@\"NSError\">24"
- "@\"NSXPCConnection\""
- "@\"NSXPCListenerEndpoint\""
- "@\"PRUISAnalysisServiceResponse\"32@0:8@\"PRUISAnalysisServiceRequest\"16o^@24"
- "@\"SBSnapshotServiceXPCConnection\""
- "@\"_PRUISAnalysisServiceXPCConnection\""
- "@24@0:8@?16"
- "@24@0:8o^@16"
- "Connection to service (%!@(MISSING)) refused on activation."
- "Ensure this process has the correct sandbox for connection and that the service is not crashing or failing to load."
- "PRUISAnalysisService.m"
- "PRUISAnalysisServiceInterface"
- "PRUISSnapshotService.m"
- "PRUISSnapshotServiceInterface"
- "SBSnapshotServiceXPCConnection"
- "_connectionLock"
- "_endpoint"
- "_lock_connection"
- "_serviceName"
- "com.apple.springboard.SBRendererService"
- "connectionActivateIfNeededWithError:"
- "initToEndpoint:"
- "initToServiceName:"
- "initWithListenerEndpoint:"
- "initWithServiceName:"
- "interfaceWithProtocol:"
- "serviceName"
- "setClasses:forSelector:argumentIndex:ofReply:"
- "setRemoteObjectInterface:"
- "v24@0:8@\"PRUISAnalysisServiceRequest\"16"
- "v32@0:8@\"PRUISSnapshotServiceRequest\"16@?<v@?@\"PRUISSnapshotServiceResponse\"@\"NSError\">24"
- "{os_unfair_recursive_lock_s=\"ourl_lock\"{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}\"ourl_count\"I}"

```
