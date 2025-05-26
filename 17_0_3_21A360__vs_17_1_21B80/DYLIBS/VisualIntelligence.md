## VisualIntelligence

> `/System/Library/PrivateFrameworks/VisualIntelligence.framework/VisualIntelligence`

```diff

-3.0.62.0.0
-  __TEXT.__text: 0x2dd4bc
-  __TEXT.__auth_stubs: 0x4240
+3.1.68.0.0
+  __TEXT.__text: 0x2df868
+  __TEXT.__auth_stubs: 0x4250
   __TEXT.__objc_methlist: 0x2194
-  __TEXT.__const: 0x13968
-  __TEXT.__cstring: 0x1b32b
+  __TEXT.__const: 0x139e8
+  __TEXT.__cstring: 0x1b31b
   __TEXT.__gcc_except_tab: 0x3e98
-  __TEXT.__constg_swiftt: 0x59c8
-  __TEXT.__swift5_typeref: 0x4d24
+  __TEXT.__constg_swiftt: 0x59ec
+  __TEXT.__swift5_typeref: 0x4d04
   __TEXT.__swift5_builtin: 0x140
   __TEXT.__swift5_reflstr: 0x52a0
   __TEXT.__swift5_fieldmd: 0x6144

   __TEXT.__swift5_protos: 0x7c
   __TEXT.__swift5_capture: 0xb50
   __TEXT.__swift5_mpenum: 0x18
-  __TEXT.__unwind_info: 0x9748
+  __TEXT.__unwind_info: 0x9790
   __TEXT.__eh_frame: 0xb160
-  __TEXT.__objc_classname: 0x941
-  __TEXT.__objc_methname: 0x69b2
+  __TEXT.__objc_classname: 0x919
+  __TEXT.__objc_methname: 0x6990
   __TEXT.__objc_methtype: 0x1fc7
   __TEXT.__objc_stubs: 0x2a00
   __DATA_CONST.__got: 0xb68
   __DATA_CONST.__const: 0x5b0
   __DATA_CONST.__objc_classlist: 0x598
   __DATA_CONST.__objc_catlist: 0x10
-  __DATA_CONST.__objc_protolist: 0xe0
+  __DATA_CONST.__objc_protolist: 0xd0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0xb6a0
-  __DATA_CONST.__objc_selrefs: 0x1320
+  __DATA_CONST.__objc_const: 0xb688
+  __DATA_CONST.__objc_selrefs: 0x1318
   __DATA_CONST.__objc_arraydata: 0x20
   __AUTH_CONST.__cfstring: 0x1aa0
-  __AUTH_CONST.__objc_const: 0x0
+  __AUTH_CONST.__objc_const: 0xd8
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH_CONST.__const: 0x4f10
-  __AUTH_CONST.__auth_ptr: 0x4b0
-  __AUTH_CONST.__auth_got: 0x20a8
-  __AUTH.__objc_data: 0x0
+  __AUTH_CONST.__const: 0x4f18
+  __AUTH_CONST.__auth_ptr: 0x4b8
+  __AUTH_CONST.__auth_got: 0x20b0
+  __AUTH.__objc_data: 0xa0
   __AUTH.__data: 0x58
   __AUTH.__got_weak: 0x90
   __DATA.__got_weak: 0x60
-  __DATA.__objc_protorefs: 0x60
+  __DATA.__objc_protorefs: 0x58
   __DATA.__objc_classrefs: 0x510
   __DATA.__objc_superrefs: 0x1d8
   __DATA.__objc_ivar: 0x3d0
-  __DATA.__data: 0x3150
+  __DATA.__data: 0x3130
   __DATA.__bss: 0x13430
   __DATA.__common: 0x3e8
-  __DATA_DIRTY.__const: 0x9338
-  __DATA_DIRTY.__objc_const: 0x20d8
-  __DATA_DIRTY.__objc_data: 0x2a18
-  __DATA_DIRTY.__data: 0xca70
+  __DATA_DIRTY.__const: 0x91a8
+  __DATA_DIRTY.__objc_const: 0x2000
+  __DATA_DIRTY.__objc_data: 0x2978
+  __DATA_DIRTY.__data: 0xcc00
   __DATA_DIRTY.__bss: 0xaf90
   __DATA_DIRTY.__common: 0x7b8
   - /System/Library/Frameworks/Accelerate.framework/Accelerate

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 13381
-  Symbols:   8564
-  CStrings:  3893
+  Functions: 13397
+  Symbols:   8561
+  CStrings:  3891
 
Symbols:
+ +[VICloudKitHandler uploadUserFeedbackToEnvironment:container:request:sfReport:intermediateResults:deviceInfo:nsfwConfidence:imageData:reportIdentifier:completionHandler:]
+ +[VINSFWModelHandler isSensitiveLabelScore:confidenceScore:classificationMode:]
+ -[VINSFWModelHandler .cxx_destruct]
+ -[VINSFWModelHandler generateClassificationScoresForPixelBuffer:]
+ -[VINSFWModelHandler initWithPreferredMetalDevice:]
+ _OBJC_CLASS_$_VICloudKitHandler
+ _OBJC_CLASS_$_VINSFWModelHandler
+ _OBJC_IVAR_$_VINSFWModelHandler._scmlHandler
+ _OBJC_METACLASS_$_VICloudKitHandler
+ _OBJC_METACLASS_$_VINSFWModelHandler
+ __OBJC_$_CLASS_METHODS_VICloudKitHandler
+ __OBJC_$_CLASS_METHODS_VINSFWModelHandler
+ __OBJC_$_INSTANCE_METHODS_VINSFWModelHandler
+ __OBJC_$_INSTANCE_VARIABLES_VINSFWModelHandler
+ __OBJC_CLASS_RO_$_VICloudKitHandler
+ __OBJC_CLASS_RO_$_VINSFWModelHandler
+ __OBJC_METACLASS_RO_$_VICloudKitHandler
+ __OBJC_METACLASS_RO_$_VINSFWModelHandler
+ ___171+[VICloudKitHandler uploadUserFeedbackToEnvironment:container:request:sfReport:intermediateResults:deviceInfo:nsfwConfidence:imageData:reportIdentifier:completionHandler:]_block_invoke
+ _symbolic _____Sg 6CoreML15MLComputeDeviceO
+ _symbolic _____ySo18VINSFWModelHandlerCG 18VisualIntelligence4LazyC
- +[VICloudKitHandlerInternal uploadUserFeedbackToEnvironment:container:request:sfReport:intermediateResults:deviceInfo:nsfwConfidence:imageData:reportIdentifier:completionHandler:]
- +[VINSFWModelHandlerInternal isSensitiveLabelScore:confidenceScore:classificationMode:]
- -[VINSFWModelHandlerInternal .cxx_destruct]
- -[VINSFWModelHandlerInternal generateClassificationScoresForPixelBuffer:]
- -[VINSFWModelHandlerInternal initWithPreferredMetalDevice:]
- _OBJC_CLASS_$_VICloudKitHandlerInternal
- _OBJC_CLASS_$_VINSFWModelHandlerInternal
- _OBJC_IVAR_$_VINSFWModelHandlerInternal._scmlHandler
- _OBJC_METACLASS_$_VICloudKitHandlerInternal
- _OBJC_METACLASS_$_VINSFWModelHandlerInternal
- __OBJC_$_CLASS_METHODS_VICloudKitHandlerInternal
- __OBJC_$_CLASS_METHODS_VINSFWModelHandlerInternal
- __OBJC_$_INSTANCE_METHODS_VINSFWModelHandlerInternal
- __OBJC_$_INSTANCE_VARIABLES_VINSFWModelHandlerInternal
- __OBJC_$_PROTOCOL_REFS_MLComputeDeviceProtocol
- __OBJC_CLASS_RO_$_VICloudKitHandlerInternal
- __OBJC_CLASS_RO_$_VINSFWModelHandlerInternal
- __OBJC_LABEL_PROTOCOL_$_MLComputeDeviceProtocol
- __OBJC_METACLASS_RO_$_VICloudKitHandlerInternal
- __OBJC_METACLASS_RO_$_VINSFWModelHandlerInternal
- __OBJC_PROTOCOL_$_MLComputeDeviceProtocol
- ___179+[VICloudKitHandlerInternal uploadUserFeedbackToEnvironment:container:request:sfReport:intermediateResults:deviceInfo:nsfwConfidence:imageData:reportIdentifier:completionHandler:]_block_invoke
- _symbolic So23MLComputeDeviceProtocol_pSg
- _symbolic _____ySo26VINSFWModelHandlerInternalCG 18VisualIntelligence4LazyC
CStrings:
+ "/Library/Caches/com.apple.xbs/Sources/VisualSearch/VisualIntelligence/VisualIntelligence/Utils/VIImageRotation.m"
+ "VICloudKitHandler"
+ "VICloudKitHandler uploading... %@ %@"
+ "VINSFWModelHandler"
- "/Library/Caches/com.apple.xbs/Sources/VisualSearch/VisualIntelligence/VisualIntelligence/Utils/VIImageRotation_Internal.m"
- "MLComputeDeviceProtocol"
- "VICloudKitHandlerInternal"
- "VICloudKitHandlerInternal uploading... %@ %@"
- "VINSFWModelHandlerInternal"
- "setComputeDevice:forComputeStage:"

```
