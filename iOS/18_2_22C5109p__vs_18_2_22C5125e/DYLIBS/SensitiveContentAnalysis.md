## SensitiveContentAnalysis

> `/System/Library/Frameworks/SensitiveContentAnalysis.framework/SensitiveContentAnalysis`

```diff

-84.5.0.0.0
-  __TEXT.__text: 0xc8ec
-  __TEXT.__auth_stubs: 0xae0
-  __TEXT.__objc_methlist: 0x438
-  __TEXT.__const: 0xda4
-  __TEXT.__cstring: 0x760
-  __TEXT.__oslogstring: 0x456
-  __TEXT.__gcc_except_tab: 0x228
+87.0.0.0.0
+  __TEXT.__text: 0x12fdc
+  __TEXT.__auth_stubs: 0xec0
+  __TEXT.__objc_methlist: 0x55c
+  __TEXT.__const: 0x11c0
+  __TEXT.__cstring: 0x9be
+  __TEXT.__oslogstring: 0x4df
+  __TEXT.__gcc_except_tab: 0x268
   __TEXT.__dlopen_cstrs: 0xc2
-  __TEXT.__constg_swiftt: 0x208
-  __TEXT.__swift5_typeref: 0x39f
-  __TEXT.__swift5_reflstr: 0x161
-  __TEXT.__swift5_fieldmd: 0x1c8
-  __TEXT.__swift5_types: 0x34
-  __TEXT.__swift5_capture: 0x80
-  __TEXT.__swift5_assocty: 0x120
-  __TEXT.__swift5_builtin: 0x14
-  __TEXT.__swift5_proto: 0xc0
-  __TEXT.__unwind_info: 0x558
-  __TEXT.__eh_frame: 0x4f0
-  __TEXT.__objc_classname: 0x97
-  __TEXT.__objc_methname: 0xf08
-  __TEXT.__objc_methtype: 0x23e
-  __TEXT.__objc_stubs: 0xb60
-  __DATA_CONST.__got: 0x168
-  __DATA_CONST.__const: 0x318
-  __DATA_CONST.__objc_classlist: 0x50
+  __TEXT.__constg_swiftt: 0x368
+  __TEXT.__swift5_typeref: 0x6cc
+  __TEXT.__swift5_reflstr: 0x1d1
+  __TEXT.__swift5_fieldmd: 0x228
+  __TEXT.__swift5_types: 0x64
+  __TEXT.__swift5_capture: 0x158
+  __TEXT.__swift5_assocty: 0x168
+  __TEXT.__swift5_builtin: 0x3c
+  __TEXT.__swift5_proto: 0x138
+  __TEXT.__unwind_info: 0x800
+  __TEXT.__eh_frame: 0x8fc
+  __TEXT.__objc_classname: 0xaf
+  __TEXT.__objc_methname: 0x1199
+  __TEXT.__objc_methtype: 0x28d
+  __TEXT.__objc_stubs: 0xba0
+  __DATA_CONST.__got: 0x218
+  __DATA_CONST.__const: 0x368
+  __DATA_CONST.__objc_classlist: 0x60
+  __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3c8
+  __DATA_CONST.__objc_selrefs: 0x490
+  __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x20
-  __AUTH_CONST.__auth_got: 0x580
-  __AUTH_CONST.__auth_ptr: 0x268
-  __AUTH_CONST.__const: 0x560
+  __AUTH_CONST.__auth_got: 0x770
+  __AUTH_CONST.__auth_ptr: 0x360
+  __AUTH_CONST.__const: 0x840
   __AUTH_CONST.__cfstring: 0x160
-  __AUTH_CONST.__objc_const: 0x828
-  __AUTH.__objc_data: 0x48
-  __AUTH.__data: 0xc0
+  __AUTH_CONST.__objc_const: 0xba0
+  __AUTH.__objc_data: 0xb8
+  __AUTH.__data: 0x1a0
   __DATA.__objc_ivar: 0x20
-  __DATA.__data: 0x200
-  __DATA.__bss: 0x1940
-  __DATA.__common: 0x10
+  __DATA.__data: 0x4d8
+  __DATA.__bss: 0x1f50
+  __DATA.__common: 0x28
   __DATA_DIRTY.__objc_data: 0x2a8
-  __DATA_DIRTY.__data: 0xd8
+  __DATA_DIRTY.__data: 0xe0
   __DATA_DIRTY.__bss: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
+  - /System/Library/Frameworks/CoreVideo.framework/CoreVideo
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Security.framework/Security
+  - /System/Library/Frameworks/VideoToolbox.framework/VideoToolbox
   - /System/Library/PrivateFrameworks/BiomeLibrary.framework/BiomeLibrary
   - /System/Library/PrivateFrameworks/ManagedSettingsObjC.framework/ManagedSettingsObjC
+  - /System/Library/PrivateFrameworks/SensitiveContentAnalysisML.framework/SensitiveContentAnalysisML
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftCore.dylib
+  - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftCoreImage.dylib
+  - /usr/lib/swift/libswiftCoreMedia.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
+  - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
+  - /usr/lib/swift/libswiftVideoToolbox.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 459
-  Symbols:   338
-  CStrings:  272
+  Functions: 670
+  Symbols:   391
+  CStrings:  337
 
Symbols:
+ _CFAbsoluteTimeGetCurrent
+ _CVBufferPropagateAttachments
+ _CVPixelBufferPoolCreate
+ _CVPixelBufferPoolCreatePixelBuffer
+ _CVPixelBufferPoolFlush
+ _NSOSStatusErrorDomain
+ _OBJC_CLASS_$_NSNumber
+ _OBJC_CLASS_$_SCVideoStreamAnalyzer
+ _OBJC_METACLASS_$_SCVideoStreamAnalyzer
+ _SCMLImageSensitivity
+ _VTPixelTransferSessionCreate
+ _VTPixelTransferSessionInvalidate
+ _VTPixelTransferSessionTransferImage
+ __swiftEmptyDictionarySingleton
+ __swift_FORCE_LOAD_$_swiftCoreAudio
+ __swift_FORCE_LOAD_$_swiftCoreImage
+ __swift_FORCE_LOAD_$_swiftCoreMedia
+ __swift_FORCE_LOAD_$_swiftMetal
+ __swift_FORCE_LOAD_$_swiftVideoToolbox
+ __swift_stdlib_bridgeErrorToNSError
+ _kCVPixelBufferHeightKey
+ _kCVPixelBufferIOSurfacePropertiesKey
+ _kCVPixelBufferPixelFormatTypeKey
+ _kCVPixelBufferPoolAllocationThresholdKey
+ _kCVPixelBufferPoolMaximumBufferAgeKey
+ _kCVPixelBufferPoolMinimumBufferCountKey
+ _kCVPixelBufferWidthKey
+ _memcpy
+ _objc_release_x26
+ _objc_retain_x25
+ _objc_retain_x26
+ _objc_retain_x27
+ _objc_retain_x28
+ _os_unfair_lock_lock
+ _os_unfair_lock_unlock
+ _swift_arrayDestroy
+ _swift_dynamicCast
+ _swift_getObjCClassFromObject
+ _swift_initStackObject
+ _swift_slowAlloc
+ _swift_slowDealloc
+ _swift_willThrowTypedImpl
CStrings:
+ "@24@0:8@\"NSCoder\"16"
+ "@32@0:8q16^@24"
+ "@?16@0:8"
+ "Analysis failed with error: %!@(MISSING)"
+ "MAD request(%!d(MISSING)) returned the following results: (%!d(MISSING), '%!@(MISSING)')"
+ "MAD request(%!d(MISSING)) with CVPixelBuffer has started"
+ "Messages"
+ "NSCoding"
+ "NSSecureCoding"
+ "Photos"
+ "Private"
+ "SCVideoStreamAnalyzer"
+ "SensitiveContentAnalysis_Private.SCVideoStreamAnalyzer"
+ "T@\"SCSensitivityAnalysis\",N,R"
+ "T@?,N,C"
+ "TB,R"
+ "VideoStreamAnalysis"
+ "_TtC24SensitiveContentAnalysis11PolicyCache"
+ "_TtCE24SensitiveContentAnalysisCSo21SCVideoStreamAnalyzerP33_E52FA56DEBAFC8D53EB6FBB0D64E15B215PixelBufferPool"
+ "_currentPolicy"
+ "analysis"
+ "analysisChanged"
+ "analyzePixelBuffer:"
+ "analyzePixelBuffer:orientation:completionHandler:"
+ "boolValue"
+ "bufferPool"
+ "changesSource"
+ "com.apple.SensitiveContentAnalysisUI"
+ "decodeObjectForKey:"
+ "encodeObject:forKey:"
+ "encodeWithCoder:"
+ "initMigratingFromNudityDetectionValue:"
+ "initWithAnalysisResult:error:"
+ "initWithCoder:"
+ "initWithOptions:error:"
+ "initWithPixelBufferClassificationDictionary:error:"
+ "isContentPreviewable"
+ "isContentShareable"
+ "isEqual:"
+ "isSensitivePixelBuffer:withOrientation:completionHandler:"
+ "lastAnalysisTime"
+ "options"
+ "performRequests:onPixelBuffer:withOrientation:andIdentifier:completionHandler:"
+ "pool"
+ "prefetchSensitiveContentPolicy:"
+ "setAnalysisChanged:"
+ "shouldObscureVideo"
+ "shouldStore"
+ "supportsSecureCoding"
+ "transferSession"
+ "transferringStateFromAnalysis:"
+ "v24@0:8@\"NSCoder\"16"
+ "v24@0:8@?<v@?@\"NSError\">16"
+ "v24@0:8^{__CVBuffer=}16"
+ "v36@0:8^{__CVBuffer=}16I24@?28"
- "Failed to encode analysis"
- "SensitiveContentAnalysis/SCSensitivityAnalysis+Implementation.swift"
- "_TtC24SensitiveContentAnalysisP33_4D89A8A00028CF3643711B7990FDFFDA31PolicyCachingSequenceDispatcher"
- "currentPolicy"

```
