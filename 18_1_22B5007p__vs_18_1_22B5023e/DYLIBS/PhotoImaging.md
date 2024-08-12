## PhotoImaging

> `/System/Library/PrivateFrameworks/PhotoImaging.framework/PhotoImaging`

```diff

-710.1.103.0.0
-  __TEXT.__text: 0x13e898
-  __TEXT.__auth_stubs: 0x1870
-  __TEXT.__objc_methlist: 0xd1ac
-  __TEXT.__const: 0x7dfc
-  __TEXT.__gcc_except_tab: 0x3dec
-  __TEXT.__cstring: 0x27845
-  __TEXT.__oslogstring: 0x405e
+710.7.140.0.0
+  __TEXT.__text: 0x141984
+  __TEXT.__auth_stubs: 0x18b0
+  __TEXT.__delay_helper: 0x110
+  __TEXT.__objc_methlist: 0xd554
+  __TEXT.__const: 0x7e0c
+  __TEXT.__gcc_except_tab: 0x3e54
+  __TEXT.__cstring: 0x27d0a
+  __TEXT.__oslogstring: 0x4061
   __TEXT.__dlopen_cstrs: 0x1d8
-  __TEXT.__unwind_info: 0x31e0
-  __TEXT.__objc_classname: 0x244f
-  __TEXT.__objc_methname: 0x1f1e5
-  __TEXT.__objc_methtype: 0x360f
-  __TEXT.__objc_stubs: 0x17b40
-  __DATA_CONST.__got: 0x17e0
-  __DATA_CONST.__const: 0x2268
-  __DATA_CONST.__objc_classlist: 0x9c8
+  __TEXT.__unwind_info: 0x32b8
+  __TEXT.__objc_classname: 0x2509
+  __TEXT.__objc_methname: 0x1f921
+  __TEXT.__objc_methtype: 0x3697
+  __TEXT.__objc_stubs: 0x180a0
+  __DATA_CONST.__got: 0x1828
+  __DATA_CONST.__const: 0x2410
+  __DATA_CONST.__objc_classlist: 0x9f0
   __DATA_CONST.__objc_catlist: 0x38
-  __DATA_CONST.__objc_protolist: 0x138
+  __DATA_CONST.__objc_protolist: 0x140
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x7500
+  __DATA_CONST.__objc_selrefs: 0x76a8
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x418
+  __DATA_CONST.__objc_superrefs: 0x438
   __DATA_CONST.__objc_arraydata: 0x6520
-  __AUTH_CONST.__auth_got: 0xc50
+  __AUTH_CONST.__auth_got: 0xc70
   __AUTH_CONST.__auth_ptr: 0x8
-  __AUTH_CONST.__const: 0x3378
-  __AUTH_CONST.__cfstring: 0x11600
-  __AUTH_CONST.__objc_const: 0x1ad90
+  __AUTH_CONST.__const: 0x3418
+  __AUTH_CONST.__cfstring: 0x11820
+  __AUTH_CONST.__objc_const: 0x1b590
   __AUTH_CONST.__objc_intobj: 0x930
   __AUTH_CONST.__objc_doubleobj: 0x8c0
   __AUTH_CONST.__objc_arrayobj: 0x228
   __AUTH_CONST.__objc_dictobj: 0x3b60
   __AUTH_CONST.__objc_floatobj: 0x70
-  __AUTH.__objc_data: 0x280
-  __DATA.__objc_ivar: 0xf30
-  __DATA.__data: 0xfbc
+  __AUTH.__objc_data: 0x410
+  __DATA.__objc_ivar: 0xf88
+  __DATA.__data: 0x1024
   __DATA.__bss: 0x5d0
   __DATA_DIRTY.__objc_data: 0x5f50
   __DATA_DIRTY.__bss: 0x1e0

   - /System/Library/PrivateFrameworks/PhotosFormats.framework/PhotosFormats
   - /System/Library/PrivateFrameworks/Portrait.framework/Portrait
   - /System/Library/PrivateFrameworks/PowerLog.framework/PowerLog
+  - /System/Library/PrivateFrameworks/SensitiveContentAnalysisML.framework/SensitiveContentAnalysisML
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 5168
-  Symbols:   7001
-  CStrings:  9465
+  Functions: 5263
+  Symbols:   7115
+  CStrings:  9588
 
Symbols:
+ _CGImageCreateFromIOSurface
+ _CVPixelBufferGetIOSurface
+ _OBJC_CLASS_$_NUScaledSourceDefinition
+ _OBJC_CLASS_$_PISensitiveContentAnalysisJob
+ _OBJC_CLASS_$_PISensitiveContentAnalysisRequest
+ _OBJC_CLASS_$_PIThumbnailGenerator
+ _OBJC_CLASS_$_SCMLImageLabelCoder
+ _OBJC_CLASS_$_SCMLImageSanitizer
+ _OBJC_CLASS_$_SCMLImageSanitizerConfiguration
+ _OBJC_CLASS_$__PISensitiveContentAnalysisResult
+ _OBJC_CLASS_$__PIThumbnailGeneratorSnapshot
+ _OBJC_METACLASS_$_PISensitiveContentAnalysisJob
+ _OBJC_METACLASS_$_PISensitiveContentAnalysisRequest
+ _OBJC_METACLASS_$_PIThumbnailGenerator
+ _OBJC_METACLASS_$__PISensitiveContentAnalysisResult
+ _OBJC_METACLASS_$__PIThumbnailGeneratorSnapshot
+ __dispatch_main_q
+ _atan2
+ _dlopen
+ _log10
- _cosf
CStrings:
+ "\t"
+ "\n        %!@(MISSING): %!@(MISSING) (%!f(MISSING))"
+ "\n   isSafe: %!@(MISSING)"
+ "-[PISensitiveContentAnalysisJob render:]"
+ "-[PISensitiveContentAnalysisJob renderInputBuffer:]"
+ "-[PIThumbnailGenerator generateThumbnailsWithCompletion:]"
+ "-[PIThumbnailGenerator setThumbnailTimes:]"
+ "-[_PISensitiveContentAnalysisResult sensitivityScore]"
+ "/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Autocalculators/PISensitiveContentAnalysisRequest.m"
+ "/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/PhotoImaging/Util/PIThumbnailGenerator.m"
+ "/System/Library/PrivateFrameworks/SensitiveContentAnalysisML.framework/SensitiveContentAnalysisML"
+ "@\"NUImageBufferRenderRequest\""
+ "@\"PIThumbnailGenerator\""
+ "@\"SCMLImageSanitization\""
+ "@\"_PIThumbnailGeneratorSnapshot\""
+ "@56@0:8{?=qiIq}16@40@48"
+ "B32@?0@\"NSValue\"8Q16^B24"
+ "CMTimeValue"
+ "Couldn't create SCMLImageSanitizer"
+ "Did not get the expected signal: %!@(MISSING)"
+ "Failed to render adjusted thumbnail"
+ "Failed to render unadjusted image at time"
+ "Failed to run SCMLImageSanitizer"
+ "Missing tumbnail times"
+ "PISensitiveContentAnalysisJob"
+ "PISensitiveContentAnalysisRequest"
+ "PISensitiveContentAnalysisResult"
+ "PIThumbnailGenerator"
+ "PIThumbnailGenerator"
+ "PIThumbnailGenerator-AdjustedThumbnail"
+ "PIThumbnailGenerator-UnadjustedThumbnail"
+ "PI_FORCE_SAFETY_CHECK_FAIL"
+ "T@\"<NUScalePolicy>\",&,N,V_thumbnailScalePolicy"
+ "T@\"NSArray\",C,N,V_thumbnailTimes"
+ "T@\"NSArray\",C,N,V_unadjustedThumbnails"
+ "T@\"NSObject<OS_dispatch_queue>\",&,N,V_resultQueue"
+ "T@\"NUComposition\",C,N,V_composition"
+ "T@\"NUImageBufferRenderRequest\",&,N,V_request"
+ "T@\"PIThumbnailGenerator\",W,N,V_generator"
+ "T@\"SCMLImageSanitization\",&,N,V_sanitization"
+ "T@\"_PIThumbnailGeneratorSnapshot\",&,N,V_pendingSnapshot"
+ "T@?,C,N,V_completionHandler"
+ "T@?,C,N,V_partialResultHandler"
+ "T{?=qiIq},N,V_referenceTime"
+ "UNSAFE"
+ "Unable to generate unadjusted thumbnail"
+ "_PISensitiveContentAnalysisResult"
+ "_PIThumbnailGeneratorSnapshot"
+ "_completionHandler"
+ "_currentSnapshot"
+ "_generateAdjustedThumbnailsWithSnapshot:"
+ "_generateThumbnailsWithPendingSnapshot:"
+ "_generateThumbnailsWithSnapshot:"
+ "_generateUnadjustedThumbnailsWithSnapshot:completion:"
+ "_generator"
+ "_partialResultHandler"
+ "_pendingSnapshot"
+ "_referenceTime"
+ "_renderRequest"
+ "_resultQueue"
+ "_sanitization"
+ "_sourceFromResult:"
+ "_thumbnailScalePolicy"
+ "_thumbnailTimes"
+ "_unadjustedThumbnails"
+ "absoluteSensitivityThreshold"
+ "cancelThumbnailGeneration"
+ "ciImageTiled:closed:pressureMode:"
+ "completionHandler"
+ "decodeFromP1:"
+ "encodeToP1:"
+ "generateThumbnailsWithCompletion:"
+ "generateThumbnailsWithPendingSnapshot:"
+ "generator"
+ "initWithConfiguration:error:"
+ "initWithGenerator:"
+ "initWithSanitization:"
+ "initWithScale:"
+ "initWithSourceDefinition:sourceSize:fullSize:"
+ "instance"
+ "isSafe"
+ "ivs.nsfw_any"
+ "no input image"
+ "partialResultHandler"
+ "pendingSnapshot"
+ "pipelineFiltersForAdjustedThumbnailRenderWithSource:"
+ "pipelineFiltersForUnadjustedThumbnail"
+ "pre-SmartTone"
+ "q24@?0@\"NSString\"8@\"NSString\"16"
+ "referenceSourceForTime:thumbnailTimes:unadjustedSources:"
+ "referenceTime"
+ "referenceTimeForTimes:"
+ "relativeSensitivityThreshold"
+ "renderInputBuffer:"
+ "resultQueue"
+ "safe"
+ "safe"
+ "sanitization"
+ "sanitizePixelBuffer:error:"
+ "sensitivityScore"
+ "setBackends:"
+ "setCompletionHandler:"
+ "setGenerator:"
+ "setGranularity:"
+ "setMode:"
+ "setPartialResultHandler:"
+ "setPendingSnapshot:"
+ "setReferenceTime:"
+ "setResultQueue:"
+ "setSanitization:"
+ "setThumbnailScalePolicy:"
+ "setThumbnailTimes:"
+ "setUnadjustedThumbnails:"
+ "signals"
+ "thumbnailScalePolicy"
+ "thumbnailTimes"
+ "times != nil"
+ "unadjustedThumbnails"
+ "v32@?0@\"NSString\"8@\"SCMLImageSanitizationSignal\"16^B24"
+ "v32@?0@\"NSValue\"8Q16^B24"
+ "v32@?0@\"NUSource\"8Q16^B24"
+ "\x81"
- "ciImageTiled:closed:pressureMode:alwaysUseCG:"

```
