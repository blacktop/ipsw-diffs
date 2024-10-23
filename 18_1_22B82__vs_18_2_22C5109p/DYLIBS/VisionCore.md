## VisionCore

> `/System/Library/PrivateFrameworks/VisionCore.framework/VisionCore`

```diff

-8.0.41.0.0
-  __TEXT.__text: 0x2b148
-  __TEXT.__auth_stubs: 0xe60
-  __TEXT.__objc_methlist: 0x24d4
-  __TEXT.__gcc_except_tab: 0x2524
+8.0.51.0.0
+  __TEXT.__text: 0x2d1cc
+  __TEXT.__auth_stubs: 0xeb0
+  __TEXT.__objc_methlist: 0x259c
+  __TEXT.__gcc_except_tab: 0x25e4
   __TEXT.__const: 0xf4
-  __TEXT.__cstring: 0x3251
-  __TEXT.__dlopen_cstrs: 0x130
+  __TEXT.__cstring: 0x3524
+  __TEXT.__dlopen_cstrs: 0x190
   __TEXT.__oslogstring: 0x1d5
-  __TEXT.__unwind_info: 0xed8
-  __TEXT.__objc_classname: 0xa13
-  __TEXT.__objc_methname: 0x74b4
-  __TEXT.__objc_methtype: 0x20b3
-  __TEXT.__objc_stubs: 0x3c60
-  __DATA_CONST.__got: 0x348
-  __DATA_CONST.__const: 0x638
-  __DATA_CONST.__objc_classlist: 0x1f0
+  __TEXT.__unwind_info: 0xf50
+  __TEXT.__objc_classname: 0xa5a
+  __TEXT.__objc_methname: 0x77ac
+  __TEXT.__objc_methtype: 0x212c
+  __TEXT.__objc_stubs: 0x3ec0
+  __DATA_CONST.__got: 0x358
+  __DATA_CONST.__const: 0x658
+  __DATA_CONST.__objc_classlist: 0x1f8
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1548
-  __DATA_CONST.__objc_superrefs: 0x160
-  __DATA_CONST.__objc_arraydata: 0xe0
-  __AUTH_CONST.__auth_got: 0x748
-  __AUTH_CONST.__const: 0x260
-  __AUTH_CONST.__cfstring: 0x3360
-  __AUTH_CONST.__objc_const: 0x54c0
-  __AUTH_CONST.__objc_intobj: 0x3a8
-  __AUTH_CONST.__objc_arrayobj: 0x48
+  __DATA_CONST.__objc_selrefs: 0x15e8
+  __DATA_CONST.__objc_superrefs: 0x168
+  __DATA_CONST.__objc_arraydata: 0x140
+  __AUTH_CONST.__auth_got: 0x770
+  __AUTH_CONST.__const: 0x320
+  __AUTH_CONST.__cfstring: 0x3700
+  __AUTH_CONST.__objc_const: 0x5598
+  __AUTH_CONST.__objc_intobj: 0x438
+  __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__objc_dictobj: 0x50
-  __AUTH.__objc_data: 0xf0
-  __DATA.__objc_ivar: 0x2f8
-  __DATA.__data: 0x3c0
-  __DATA.__bss: 0x110
-  __DATA_DIRTY.__objc_data: 0x1270
+  __AUTH.__objc_data: 0x190
+  __DATA.__objc_ivar: 0x2fc
+  __DATA.__data: 0x3c8
+  __DATA.__bss: 0x178
+  __DATA_DIRTY.__objc_data: 0x1220
   __DATA_DIRTY.__bss: 0x70
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/Frameworks/Metal.framework/Metal
   - /System/Library/PrivateFrameworks/Espresso.framework/Espresso
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
+  - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 887
-  Symbols:   1359
-  CStrings:  1838
+  Functions: 916
+  Symbols:   1397
+  CStrings:  1896
 
Symbols:
+ _MGGetBoolAnswer
+ _MGGetSInt64Answer
+ _MGIsQuestionValid
+ _OBJC_CLASS_$_NSUserDefaults
+ _OBJC_CLASS_$_VisionCorePersonInstanceMaskEspressoInferenceNetworkDescriptor
+ _OBJC_CLASS_$_VisionCoreSemanticSegmentationEspressoInferenceNetworkDescriptorV4
+ _OBJC_METACLASS_$_VisionCorePersonInstanceMaskEspressoInferenceNetworkDescriptor
+ _OBJC_METACLASS_$_VisionCoreSemanticSegmentationEspressoInferenceNetworkDescriptorV4
+ _VisionCoreANEArchitectureName
+ _VisionCoreANESubtype
+ _VisionCoreCurrentANEGeneration
+ _VisionCoreHasANE
+ _VisionCoreInferenceNetworkIdentifierPersonInstanceMaskEspresso
+ _VisionCoreInferenceNetworkIdentifierSemanticSegmentationEspressoV4
+ _e5rt_tensor_desc_get_size
+ _objc_retain_x5
- _OBJC_CLASS_$_VisionCoreSemanticSegmentationInferenceNetworkDescriptorV4
- _OBJC_METACLASS_$_VisionCoreSemanticSegmentationInferenceNetworkDescriptorV4
- _VisionCoreInferenceNetworkIdentifierSemanticSegmentationV4
CStrings:
+ "+N9mZUAHooNvMiQnjeTJ8g"
+ ".bundle"
+ ".espresso"
+ ".mil"
+ ".net"
+ "@36@0:8@16B24^@28"
+ "@40@0:8@16Q24^@32"
+ "@40@0:8Q16Q24^@32"
+ "@56@0:8@16Q24@32@40Q48"
+ "@68@0:8@16@24Q32q40q48B56^@60"
+ "E5RTBaseModelName:error:"
+ "E5RTURLForModelBundle:modelFileIsBaseName:error:"
+ "E5RTURLForModelNamed:error:"
+ "H"
+ "HyperDETR-u8-v1.1"
+ "HyperDETR-u8-v1.1.e5.espresso.net"
+ "NULL"
+ "Output descriptor: %!@(MISSING)"
+ "TQ,R,N,V_storageByteCount"
+ "The model is not supported on current ANE version"
+ "The model is only supported with the ANE compute device"
+ "Unexpected model version %!l(MISSING)u"
+ "Unkknown person instance model"
+ "Unkknown semantic segmentation model"
+ "Unknown format for model: %!@(MISSING)"
+ "Unknown model extension: %!@(MISSING)"
+ "Unknown model version"
+ "Unknown model version %!l(MISSING)u"
+ "Unknown person instance model"
+ "VISIONCORE_LOG_ALL_MESSAGES"
+ "VisionCoreAssert:log:"
+ "VisionCoreInferenceNetworkIdentifierPersonInstanceMaskEspresso"
+ "VisionCoreInferenceNetworkIdentifierSemanticSegmentationEspressoV4"
+ "VisionCorePersonInstanceMaskEspressoInferenceNetworkDescriptor"
+ "VisionCoreSemanticSegmentationEspressoInferenceNetworkDescriptorV4"
+ "_ANEDeviceInfo"
+ "_storageByteCount"
+ "addSuiteNamed:"
+ "aneSubType"
+ "boolForKey:"
+ "camalgoseg.flows.lowres-s2h6ysbnuy_82500"
+ "componentsSeparatedByString:"
+ "containsString:"
+ "decodeInt64ForKey:"
+ "eJGhnVvylF3dMOHBKJzeiw"
+ "encodeInt64:forKey:"
+ "initWithName:dataType:shape:strides:storageByteCount:"
+ "integerValue"
+ "lastObject"
+ "loadOrCompileProgramLibrary:modelBaseName:e5rtComputeDeviceType:supportedOnANEFrom:fullyANEResidentFrom:allowCompilation:error:"
+ "modelFileURLForModelVersion:error:"
+ "objectClassIDsToObjectClassesDetectionStatusIndexes:modelVersion:error:"
+ "objectClassNamesToObjectClassesDetectionStatusIndexes:modelVersion:error:"
+ "objectClassOutputNameForObjectClassID:modelVersion:error:"
+ "objectClassOutputNamesForObjectClassIDs:modelVersion:error:"
+ "personInstanceMaskForModelVersion:computeDeviceType:error:"
+ "person_instance_boxes:0"
+ "personsemantics-u8-v4"
+ "personsemantics-u8-v4.e5.espresso.net"
+ "semanticSegmentationForModelVersion:computeDeviceType:error:"
+ "softlink:o:path:/System/Library/PrivateFrameworks/AppleNeuralEngine.framework/AppleNeuralEngine"
+ "standardUserDefaults"
+ "uppercaseString"
+ "v28@0:8B16@20"
- "HyperDETR-u8-v1.1.espresso"
- "VisionCoreInferenceNetworkIdentifierSemanticSegmentationV4"
- "VisionCoreSemanticSegmentationInferenceNetworkDescriptorV4"
- "objectClassIDsToObjectClassesDetectionStatusIndexes:error:"
- "objectClassNamesToObjectClassesDetectionStatusIndexes:error:"
- "semanticSegmentationV6AndReturnError:"
- "stringByDeletingLastPathComponent"

```
