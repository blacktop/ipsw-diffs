## VisualLookUp

> `/System/Library/PrivateFrameworks/VisualLookUp.framework/VisualLookUp`

```diff

-5.0.41.0.0
-  __TEXT.__text: 0x30d3e8
-  __TEXT.__auth_stubs: 0x5180
-  __TEXT.__objc_methlist: 0x4534
-  __TEXT.__const: 0x1a464
-  __TEXT.__cstring: 0x14ba0
-  __TEXT.__oslogstring: 0x6fb4
+5.0.46.0.0
+  __TEXT.__text: 0x305078
+  __TEXT.__auth_stubs: 0x5170
+  __TEXT.__objc_methlist: 0x4474
+  __TEXT.__const: 0x1a474
+  __TEXT.__cstring: 0x14b30
+  __TEXT.__oslogstring: 0x71d4
   __TEXT.__gcc_except_tab: 0x3e90
-  __TEXT.__constg_swiftt: 0x7680
+  __TEXT.__constg_swiftt: 0x7648
   __TEXT.__swift5_typeref: 0x6249
-  __TEXT.__swift5_reflstr: 0x6fb8
-  __TEXT.__swift5_fieldmd: 0x7e20
+  __TEXT.__swift5_reflstr: 0x6fe8
+  __TEXT.__swift5_fieldmd: 0x7e2c
   __TEXT.__swift5_builtin: 0x140
   __TEXT.__swift5_assocty: 0x730
-  __TEXT.__swift5_capture: 0x2074
+  __TEXT.__swift5_capture: 0x1d6c
   __TEXT.__swift5_proto: 0x1604
   __TEXT.__swift5_types: 0x85c
   __TEXT.__swift5_protos: 0x88
   __TEXT.__swift5_mpenum: 0x20
   __TEXT.__swift_as_entry: 0x24
   __TEXT.__swift_as_ret: 0x24
-  __TEXT.__unwind_info: 0x9070
-  __TEXT.__eh_frame: 0xd6b8
+  __TEXT.__unwind_info: 0x9020
+  __TEXT.__eh_frame: 0xd5f0
   __TEXT.__objc_classname: 0x84a
-  __TEXT.__objc_methname: 0xa29e
-  __TEXT.__objc_methtype: 0x264f
-  __TEXT.__objc_stubs: 0x41a0
-  __DATA_CONST.__got: 0x12b0
-  __DATA_CONST.__const: 0x640
+  __TEXT.__objc_methname: 0x9f5a
+  __TEXT.__objc_methtype: 0x2612
+  __TEXT.__objc_stubs: 0x40a0
+  __DATA_CONST.__got: 0x12a8
+  __DATA_CONST.__const: 0x620
   __DATA_CONST.__objc_classlist: 0x680
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x130
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1fc0
+  __DATA_CONST.__objc_selrefs: 0x1f48
   __DATA_CONST.__objc_protorefs: 0x58
   __DATA_CONST.__objc_superrefs: 0x258
   __DATA_CONST.__objc_arraydata: 0x20
-  __AUTH_CONST.__auth_got: 0x28d8
-  __AUTH_CONST.__const: 0x11da0
+  __AUTH_CONST.__auth_got: 0x28d0
+  __AUTH_CONST.__const: 0x11830
   __AUTH_CONST.__cfstring: 0x2000
   __AUTH_CONST.__objc_const: 0x10870
   __AUTH_CONST.__objc_intobj: 0x18

   __DATA.__data: 0x39e0
   __DATA.__bss: 0x1c6b0
   __DATA.__common: 0x738
-  __DATA_DIRTY.__objc_data: 0x17c0
-  __DATA_DIRTY.__data: 0xbd98
+  __DATA_DIRTY.__objc_data: 0x1780
+  __DATA_DIRTY.__data: 0xbdb8
   __DATA_DIRTY.__bss: 0xbf90
   __DATA_DIRTY.__common: 0x848
   - /System/Library/Frameworks/Accelerate.framework/Accelerate

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: BF18B7DD-311F-339C-9DD3-D7C047CC4102
-  Functions: 12280
-  Symbols:   10802
-  CStrings:  5127
+  UUID: C25B38E0-0425-3664-A54F-561916949C82
+  Functions: 12213
+  Symbols:   10729
+  CStrings:  5121
 
Symbols:
+ _block_copy_helper.104
+ _block_copy_helper.120
+ _block_copy_helper.129
+ _block_copy_helper.130
+ _block_copy_helper.143
+ _block_copy_helper.160
+ _block_copy_helper.30
+ _block_copy_helper.71
+ _block_copy_helper.92
+ _block_copy_helper.96
+ _block_descriptor.106
+ _block_descriptor.122
+ _block_descriptor.131
+ _block_descriptor.132
+ _block_descriptor.145
+ _block_descriptor.162
+ _block_descriptor.32
+ _block_descriptor.73
+ _block_descriptor.94
+ _block_descriptor.98
+ _block_destroy_helper.105
+ _block_destroy_helper.121
+ _block_destroy_helper.130
+ _block_destroy_helper.131
+ _block_destroy_helper.144
+ _block_destroy_helper.161
+ _block_destroy_helper.31
+ _block_destroy_helper.72
+ _block_destroy_helper.93
+ _block_destroy_helper.97
+ _objc_msgSend$shouldLogInternalVerboseMessage
+ _objc_retain_x10
+ _objectdestroy.118Tm
+ _objectdestroy.127Tm
+ _objectdestroy.18Tm
+ _objectdestroy.62Tm
+ _objectdestroy.88Tm
- -[VIService detectorModelDescriptions]
- -[VIService encryptedSearchWithParsedVisualQuery:completion:]
- -[VIService experimentalSearchWithParsedVisualQuery:completion:]
- -[VIService generateCachedResultsWithDetectorOutputs:imageSize:orientation:normalizedRegionOfInterest:]
- -[VIService isEligibleForEncryptedSearchWithCachedResults:]
- -[VIService parseCameraFrameWithVisualQuery:cachedResults:completion:]
- -[VIService parseCameraFrameWithVisualQuery:completion:]
- -[VIService searchCameraFrameWithParsedVisualQuery:completion:]
- ___56-[VIService parseCameraFrameWithVisualQuery:completion:]_block_invoke
- ___70-[VIService parseCameraFrameWithVisualQuery:cachedResults:completion:]_block_invoke
- __swift_FORCE_LOAD_$_swiftDarwin
- __swift_FORCE_LOAD_$_swiftDarwin_$_VisualLookUp
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_VisualLookUp
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_VisualLookUp
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_VisualLookUp
- _block_copy_helper.109
- _block_copy_helper.122
- _block_copy_helper.128
- _block_copy_helper.133
- _block_copy_helper.142
- _block_copy_helper.154
- _block_copy_helper.159
- _block_copy_helper.171
- _block_copy_helper.183
- _block_copy_helper.199
- _block_copy_helper.211
- _block_copy_helper.26
- _block_copy_helper.36
- _block_copy_helper.47
- _block_copy_helper.58
- _block_copy_helper.69
- _block_copy_helper.80
- _block_copy_helper.83
- _block_copy_helper.95
- _block_copy_helper.99
- _block_descriptor.101
- _block_descriptor.111
- _block_descriptor.124
- _block_descriptor.130
- _block_descriptor.135
- _block_descriptor.144
- _block_descriptor.156
- _block_descriptor.161
- _block_descriptor.173
- _block_descriptor.185
- _block_descriptor.201
- _block_descriptor.213
- _block_descriptor.28
- _block_descriptor.38
- _block_descriptor.49
- _block_descriptor.60
- _block_descriptor.71
- _block_descriptor.82
- _block_descriptor.85
- _block_descriptor.97
- _block_destroy_helper.100
- _block_destroy_helper.110
- _block_destroy_helper.123
- _block_destroy_helper.129
- _block_destroy_helper.134
- _block_destroy_helper.143
- _block_destroy_helper.155
- _block_destroy_helper.160
- _block_destroy_helper.172
- _block_destroy_helper.184
- _block_destroy_helper.200
- _block_destroy_helper.212
- _block_destroy_helper.27
- _block_destroy_helper.37
- _block_destroy_helper.48
- _block_destroy_helper.59
- _block_destroy_helper.70
- _block_destroy_helper.81
- _block_destroy_helper.84
- _block_destroy_helper.96
- _objc_msgSend$detectorModelDescriptions
- _objc_msgSend$encryptedSearchWithImage:visualUnderstanding:queryContext:completion:
- _objc_msgSend$experimentalSearchWithImage:visualUnderstanding:queryContext:completion:
- _objc_msgSend$generateCachedResultsWithDetectorOutputs:imageSize:imageOrientation:normalizedRegionOfInterest:
- _objc_msgSend$isEligibleForEncryptedSearchWithCachedResults:
- _objc_msgSend$parseCameraFrameCachedWithVisualQuery:cachedResults:completion:
- _objc_msgSend$parseCameraFrameWithVisualQuery:completion:
- _objc_msgSend$searchCameraFrameWithImage:visualUnderstanding:queryContext:completion:
- _objc_msgSend$shouldLogVerboseMessage
- _objectdestroy.126Tm
- _objectdestroy.24Tm
- _objectdestroy.97Tm
CStrings:
+ " region(s) with assigned domains"
+ "Enabled %ld domains in locale: %s"
+ "Enabled domains: %s"
+ "Evaluating lazy PIRClient failed with error: %@"
+ "VisualIntelligenceService.init()"
+ "encryptedSearch(): no imageRegion matching domain %s"
+ "encryptedSearch(): unsupported domain %s"
+ "encryptedSearchPEC(): canceled"
+ "encryptedSearchPIR(): canceled"
+ "parse(): failed with error: %s"
+ "parse(): successful %s"
+ "parseCameraFrame with groundingDetections"
+ "parseCameraFrame with input image"
+ "performEncryptedPegasusRequestForPEC(): %@"
+ "performEncryptedPegasusRequestForPEC(): processingConfigError %@"
+ "performEncryptedPegasusRequestForPIR(): %@"
+ "performEncryptedPegasusRequestForPIR(): processingConfigError %@"
+ "performRunArgos2D() with domain: %s"
+ "runArgos2DV2(): %s"
+ "runArgos2DV2(): successful"
+ "search(): %s"
+ "search(): error =%@"
+ "search(): failure"
+ "searchCameraFrame"
+ "searchCameraFrame with searchHistoryEntries"
+ "shouldLogInternalVerboseMessage"
- "@76@0:8@16{CGSize=dd}24I40{CGRect={CGPoint=dd}{CGSize=dd}}44"
- "Camera enabled domains: input domain count %ld, domains: %s for locale: %s"
- "Invalid boxOutput"
- "Invalid confidenceOutput"
- "Invalid model info or outputs or modelURL"
- "__swift_objectForKeyedSubscript:"
- "detectorModelDescriptions"
- "encryptedSearchWithImage:visualUnderstanding:queryContext:completion:"
- "encryptedSearchWithParsedVisualQuery:completion:"
- "experimentalSearch(): canceled"
- "experimentalSearch(): no imageRegion matching domain %s"
- "experimentalSearch(): unsupported domain %s"
- "experimentalSearchWithImage:visualUnderstanding:queryContext:completion:"
- "experimentalSearchWithParsedVisualQuery:completion:"
- "generateCachedResultsWithDetectorOutputs:imageSize:imageOrientation:normalizedRegionOfInterest:"
- "generateCachedResultsWithDetectorOutputs:imageSize:orientation:normalizedRegionOfInterest:"
- "initWithLongLong:"
- "isEligibleForEncryptedSearchWithCachedResults:"
- "parse(): %s"
- "parse(): successful"
- "parseCameraFrameCachedWithVisualQuery:cachedResults:completion:"
- "parseCameraFrameWithVisualQuery:cachedResults:completion:"
- "parseCameraFrameWithVisualQuery:completion:"
- "performEncryptedPegasusRequest(): %@"
- "performEncryptedPegasusRequest(): processingConfigError %@"
- "performExperimentalPegasusRequest(): %@"
- "performExperimentalPegasusRequest(): processingConfigError %@"
- "searchCameraFrameWithImage:visualUnderstanding:queryContext:completion:"
- "searchCameraFrameWithParsedVisualQuery:completion:"
- "shouldLogVerboseMessage"

```
