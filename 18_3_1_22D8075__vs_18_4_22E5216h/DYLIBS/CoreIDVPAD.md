## CoreIDVPAD

> `/System/Library/PrivateFrameworks/CoreIDVPAD.framework/CoreIDVPAD`

```diff

-2.8.0.0.0
-  __TEXT.__text: 0x4a3d4
-  __TEXT.__auth_stubs: 0x16a0
-  __TEXT.__objc_methlist: 0xc14
-  __TEXT.__const: 0x22a6
-  __TEXT.__gcc_except_tab: 0xa60
-  __TEXT.__cstring: 0x220e
-  __TEXT.__oslogstring: 0x1888
-  __TEXT.__constg_swiftt: 0x1a74
-  __TEXT.__swift5_typeref: 0xc5e
+2.9.1.0.0
+  __TEXT.__text: 0x4493c
+  __TEXT.__auth_stubs: 0x1630
+  __TEXT.__objc_methlist: 0xe68
+  __TEXT.__const: 0x2382
+  __TEXT.__gcc_except_tab: 0xa74
+  __TEXT.__cstring: 0x1ce9
+  __TEXT.__oslogstring: 0x19c8
+  __TEXT.__constg_swiftt: 0x1894
+  __TEXT.__swift5_typeref: 0xc60
   __TEXT.__swift5_builtin: 0x118
-  __TEXT.__swift5_reflstr: 0xd26
-  __TEXT.__swift5_fieldmd: 0x10f4
+  __TEXT.__swift5_reflstr: 0xce1
+  __TEXT.__swift5_fieldmd: 0x1078
   __TEXT.__swift5_assocty: 0x150
   __TEXT.__swift5_proto: 0x174
-  __TEXT.__swift5_types: 0x100
+  __TEXT.__swift5_types: 0xf0
   __TEXT.__swift5_protos: 0x20
+  __TEXT.__swift_as_entry: 0x20
+  __TEXT.__swift_as_ret: 0x24
   __TEXT.__swift5_capture: 0x21c
-  __TEXT.__unwind_info: 0xf78
-  __TEXT.__eh_frame: 0x1020
+  __TEXT.__unwind_info: 0xe38
+  __TEXT.__eh_frame: 0xe98
   __TEXT.__objc_classname: 0x1db
-  __TEXT.__objc_methname: 0x226e
+  __TEXT.__objc_methname: 0x21b9
   __TEXT.__objc_methtype: 0x971
   __TEXT.__objc_stubs: 0xe80
   __DATA_CONST.__got: 0x3f0
-  __DATA_CONST.__const: 0x2c8
-  __DATA_CONST.__objc_classlist: 0x160
+  __DATA_CONST.__const: 0x2b0
+  __DATA_CONST.__objc_classlist: 0x140
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x8b0
+  __DATA_CONST.__objc_selrefs: 0x940
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x38
-  __AUTH_CONST.__auth_got: 0xb68
-  __AUTH_CONST.__auth_ptr: 0x450
-  __AUTH_CONST.__const: 0x1730
+  __AUTH_CONST.__auth_got: 0xb30
+  __AUTH_CONST.__auth_ptr: 0x4f0
+  __AUTH_CONST.__const: 0x1758
   __AUTH_CONST.__cfstring: 0x820
-  __AUTH_CONST.__objc_const: 0x3ab8
+  __AUTH_CONST.__objc_const: 0x3288
   __AUTH_CONST.__objc_intobj: 0x48
   __AUTH.__objc_data: 0xde0
-  __AUTH.__data: 0x1f78
+  __AUTH.__data: 0x1bf8
   __DATA.__objc_ivar: 0x120
-  __DATA.__data: 0xb58
+  __DATA.__data: 0xb28
   __DATA.__bss: 0x2b20
-  __DATA.__common: 0x10
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 1389
-  Symbols:   740
-  CStrings:  927
+  Functions: 1310
+  Symbols:   749
+  CStrings:  902
 
Symbols:
+ _swift_cvw_assignWithCopy
+ _swift_cvw_assignWithTake
+ _swift_cvw_destroy
+ _swift_cvw_initWithCopy
+ _swift_cvw_initializeBufferWithCopyOfBuffer
- _objc_release_x10
- _swift_setDeallocating
CStrings:
+ "PADInternalClassifier:cancelWithCompletion(), set PADSWClassifier to nil"
+ "PADInternalClassifier:init(), PADSWClassifier loaded"
+ "PADInternalClassifier:padClassifierDidCancelWithError(), set PADSWClassifier to nil"
+ "PADInternalClassifier:padClassifierDidCompleteAssessment(), set PADSWClassifier to nil"
+ "Successfully loaded FacePose v%s"
- "Attempted to run PRD on frame with no faces detected."
- "Can't construct Array with count < 0"
- "Insufficient space allocated to copy string contents"
- "PRD model was unable to generate a PRD assessment for frame."
- "Successfully loaded FacePose v%s, PrintReplay v%s"
- "Swift/Array.swift"
- "Swift/ContiguousArrayBuffer.swift"
- "Swift/StringTesting.swift"
- "Swift/StringUTF8View.swift"
- "Swift/UnsafeBufferPointer.swift"
- "Swift/UnsafePointer.swift"
- "Swift/UnsafeRawPointer.swift"
- "Unable to create cropped buffer for PRD model."
- "Unable to extract frame's VNImageBuffer for PRD processing."
- "Unable to load PRD model."
- "Unexpectedly found nil while unwrapping an Optional value"
- "UnsafeMutableBufferPointer with negative count"
- "UnsafeMutablePointer.initialize overlapping range"
- "UnsafeMutablePointer.initialize with negative count"
- "UnsafeMutablePointer.moveInitialize with negative count"
- "UnsafeMutableRawPointer.initializeMemory overlapping range"
- "_TtC10CoreIDVPAD21PADPrintReplayS2Model"
- "_TtC10CoreIDVPAD26PADPrintReplayModelManager"
- "_TtC10CoreIDVPAD26PADPrintReplayS2ModelInput"
- "_TtC10CoreIDVPAD27PADPrintReplayS2ModelOutput"
- "cropAndScaleBufferWithWidth:height:cropRect:format:imageCropAndScaleOption:options:error:calculatedNormalizedOriginOffset:calculatedScaleX:calculatedScaleY:pixelBufferRepsCacheKey:"
- "image"
- "invalid Collection: less than 'count' elements in collection"
- "prdModel"
- "printReplayModelManager"

```
