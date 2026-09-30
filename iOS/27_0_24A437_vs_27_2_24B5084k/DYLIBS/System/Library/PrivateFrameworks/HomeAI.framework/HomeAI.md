## HomeAI

> `/System/Library/PrivateFrameworks/HomeAI.framework/HomeAI`

```diff

-378.0.0.0.0
-  __TEXT.__text: 0x176c70
+381.0.0.0.0
+  __TEXT.__text: 0x17a9e4
   __TEXT.__init_offsets: 0x10
-  __TEXT.__objc_methlist: 0xa25c
-  __TEXT.__const: 0x495d
-  __TEXT.__cstring: 0xd9f1
+  __TEXT.__objc_methlist: 0xa67c
+  __TEXT.__const: 0x497d
+  __TEXT.__cstring: 0xda5c
   __TEXT.__gcc_except_tab: 0xc210
-  __TEXT.__oslogstring: 0xe4cc
+  __TEXT.__oslogstring: 0xe87d
   __TEXT.__dlopen_cstrs: 0x16e
   __TEXT.__swift5_typeref: 0x21
   __TEXT.__constg_swiftt: 0x28
   __TEXT.__swift5_reflstr: 0x74
   __TEXT.__swift5_fieldmd: 0x4c
   __TEXT.__swift5_types: 0x4
-  __TEXT.__unwind_info: 0x5ae0
+  __TEXT.__unwind_info: 0x5b70
   __TEXT.__eh_frame: 0x50
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x3998
-  __DATA_CONST.__objc_classlist: 0x700
+  __DATA_CONST.__objc_classlist: 0x718
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x110
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x10
-  __DATA_CONST.__objc_selrefs: 0x4800
+  __DATA_CONST.__objc_selrefs: 0x4820
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x5f8
-  __DATA_CONST.__objc_arraydata: 0x618
+  __DATA_CONST.__objc_superrefs: 0x610
+  __DATA_CONST.__objc_arraydata: 0x6e8
   __DATA_CONST.__got: 0xc48
   __AUTH_CONST.__const: 0x48b0
-  __AUTH_CONST.__cfstring: 0x8a60
-  __AUTH_CONST.__objc_const: 0x15ce0
+  __AUTH_CONST.__cfstring: 0x8ae0
+  __AUTH_CONST.__objc_const: 0x16420
   __AUTH_CONST.__weak_auth_got: 0x28
   __AUTH_CONST.__objc_intobj: 0x588
-  __AUTH_CONST.__objc_arrayobj: 0x360
-  __AUTH_CONST.__objc_doubleobj: 0x1b0
+  __AUTH_CONST.__objc_arrayobj: 0x390
+  __AUTH_CONST.__objc_doubleobj: 0x180
   __AUTH_CONST.__objc_dictobj: 0x1b8
   __AUTH_CONST.__objc_floatobj: 0x70
-  __AUTH_CONST.__auth_got: 0xe90
-  __AUTH.__objc_data: 0x41f0
+  __AUTH_CONST.__auth_got: 0xe98
+  __AUTH.__objc_data: 0x42e0
   __AUTH.__data: 0x350
-  __DATA.__objc_ivar: 0xcf8
+  __DATA.__objc_ivar: 0xd64
   __DATA.__data: 0xd3c
   __DATA_DIRTY.__objc_data: 0x410
   __DATA_DIRTY.__bss: 0x2d8

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 5428
-  Symbols:   12051
-  CStrings:  3199
+  Functions: 5516
+  Symbols:   12195
+  CStrings:  3222
 
Symbols:
+ +[NSError(HMIError) hmiPrivateErrorWithCode:reason:]
+ +[SignificantActivityYolo URLOfModelInThisBundle]
+ +[SignificantActivityYolo loadContentsOfURL:configuration:completionHandler:]
+ +[SignificantActivityYolo loadWithConfiguration:completionHandler:]
+ -[HMIDataReader canReadLength:]
+ -[HMIDataReader failReadOfLength:]
+ -[HMIDataReader remainingLength]
+ -[SignificantActivityYolo .cxx_destruct]
+ -[SignificantActivityYolo initWithConfiguration:error:]
+ -[SignificantActivityYolo initWithContentsOfURL:configuration:error:]
+ -[SignificantActivityYolo initWithContentsOfURL:error:]
+ -[SignificantActivityYolo initWithMLModel:]
+ -[SignificantActivityYolo init]
+ -[SignificantActivityYolo model]
+ -[SignificantActivityYolo predictionFromFeatures:completionHandler:]
+ -[SignificantActivityYolo predictionFromFeatures:error:]
+ -[SignificantActivityYolo predictionFromFeatures:options:completionHandler:]
+ -[SignificantActivityYolo predictionFromFeatures:options:error:]
+ -[SignificantActivityYolo predictionFromImage_Placeholder:error:]
+ -[SignificantActivityYolo predictionsFromInputs:options:error:]
+ -[SignificantActivityYoloInput dealloc]
+ -[SignificantActivityYoloInput featureNames]
+ -[SignificantActivityYoloInput featureValueForName:]
+ -[SignificantActivityYoloInput image_Placeholder]
+ -[SignificantActivityYoloInput initWithImage_Placeholder:]
+ -[SignificantActivityYoloInput initWithImage_PlaceholderAtURL:error:]
+ -[SignificantActivityYoloInput initWithImage_PlaceholderFromCGImage:error:]
+ -[SignificantActivityYoloInput setImage_Placeholder:]
+ -[SignificantActivityYoloInput setImage_PlaceholderWithCGImage:error:]
+ -[SignificantActivityYoloInput setImage_PlaceholderWithURL:error:]
+ -[SignificantActivityYoloOutput .cxx_destruct]
+ -[SignificantActivityYoloOutput HomeSSD_box0_offset0]
+ -[SignificantActivityYoloOutput HomeSSD_box0_offset1]
+ -[SignificantActivityYoloOutput HomeSSD_box0_offset2]
+ -[SignificantActivityYoloOutput HomeSSD_box0_offset3]
+ -[SignificantActivityYoloOutput HomeSSD_box0_offset4]
+ -[SignificantActivityYoloOutput HomeSSD_box1_offset0]
+ -[SignificantActivityYoloOutput HomeSSD_box1_offset1]
+ -[SignificantActivityYoloOutput HomeSSD_box1_offset2]
+ -[SignificantActivityYoloOutput HomeSSD_box1_offset3]
+ -[SignificantActivityYoloOutput HomeSSD_box1_offset4]
+ -[SignificantActivityYoloOutput HomeSSD_class_prob0]
+ -[SignificantActivityYoloOutput HomeSSD_class_prob1]
+ -[SignificantActivityYoloOutput HomeSSD_class_prob2]
+ -[SignificantActivityYoloOutput HomeSSD_class_prob3]
+ -[SignificantActivityYoloOutput HomeSSD_class_prob4]
+ -[SignificantActivityYoloOutput HomeSSD_object_roll0]
+ -[SignificantActivityYoloOutput HomeSSD_object_roll1]
+ -[SignificantActivityYoloOutput HomeSSD_object_roll2]
+ -[SignificantActivityYoloOutput HomeSSD_object_roll3]
+ -[SignificantActivityYoloOutput HomeSSD_object_roll4]
+ -[SignificantActivityYoloOutput HomeSSD_object_yaw0]
+ -[SignificantActivityYoloOutput HomeSSD_object_yaw1]
+ -[SignificantActivityYoloOutput HomeSSD_object_yaw2]
+ -[SignificantActivityYoloOutput HomeSSD_object_yaw3]
+ -[SignificantActivityYoloOutput HomeSSD_object_yaw4]
+ -[SignificantActivityYoloOutput featureNames]
+ -[SignificantActivityYoloOutput featureValueForName:]
+ -[SignificantActivityYoloOutput initWithHomeSSD_class_prob0:HomeSSD_box0_offset0:HomeSSD_box1_offset0:HomeSSD_object_roll0:HomeSSD_object_yaw0:HomeSSD_class_prob1:HomeSSD_box0_offset1:HomeSSD_box1_offset1:HomeSSD_object_roll1:HomeSSD_object_yaw1:HomeSSD_class_prob2:HomeSSD_box0_offset2:HomeSSD_box1_offset2:HomeSSD_object_roll2:HomeSSD_object_yaw2:HomeSSD_class_prob3:HomeSSD_box0_offset3:HomeSSD_box1_offset3:HomeSSD_object_roll3:HomeSSD_object_yaw3:HomeSSD_class_prob4:HomeSSD_box0_offset4:HomeSSD_box1_offset4:HomeSSD_object_roll4:HomeSSD_object_yaw4:]
+ -[SignificantActivityYoloOutput setHomeSSD_box0_offset0:]
+ -[SignificantActivityYoloOutput setHomeSSD_box0_offset1:]
+ -[SignificantActivityYoloOutput setHomeSSD_box0_offset2:]
+ -[SignificantActivityYoloOutput setHomeSSD_box0_offset3:]
+ -[SignificantActivityYoloOutput setHomeSSD_box0_offset4:]
+ -[SignificantActivityYoloOutput setHomeSSD_box1_offset0:]
+ -[SignificantActivityYoloOutput setHomeSSD_box1_offset1:]
+ -[SignificantActivityYoloOutput setHomeSSD_box1_offset2:]
+ -[SignificantActivityYoloOutput setHomeSSD_box1_offset3:]
+ -[SignificantActivityYoloOutput setHomeSSD_box1_offset4:]
+ -[SignificantActivityYoloOutput setHomeSSD_class_prob0:]
+ -[SignificantActivityYoloOutput setHomeSSD_class_prob1:]
+ -[SignificantActivityYoloOutput setHomeSSD_class_prob2:]
+ -[SignificantActivityYoloOutput setHomeSSD_class_prob3:]
+ -[SignificantActivityYoloOutput setHomeSSD_class_prob4:]
+ -[SignificantActivityYoloOutput setHomeSSD_object_roll0:]
+ -[SignificantActivityYoloOutput setHomeSSD_object_roll1:]
+ -[SignificantActivityYoloOutput setHomeSSD_object_roll2:]
+ -[SignificantActivityYoloOutput setHomeSSD_object_roll3:]
+ -[SignificantActivityYoloOutput setHomeSSD_object_roll4:]
+ -[SignificantActivityYoloOutput setHomeSSD_object_yaw0:]
+ -[SignificantActivityYoloOutput setHomeSSD_object_yaw1:]
+ -[SignificantActivityYoloOutput setHomeSSD_object_yaw2:]
+ -[SignificantActivityYoloOutput setHomeSSD_object_yaw3:]
+ -[SignificantActivityYoloOutput setHomeSSD_object_yaw4:]
+ GCC_except_table82
+ _OBJC_CLASS_$_SignificantActivityYolo
+ _OBJC_CLASS_$_SignificantActivityYoloInput
+ _OBJC_CLASS_$_SignificantActivityYoloOutput
+ _OBJC_IVAR_$_SignificantActivityYolo._model
+ _OBJC_IVAR_$_SignificantActivityYoloInput._image_Placeholder
+ _OBJC_IVAR_$_SignificantActivityYoloOutput._HomeSSD_box0_offset0
+ _OBJC_IVAR_$_SignificantActivityYoloOutput._HomeSSD_box0_offset1
+ _OBJC_IVAR_$_SignificantActivityYoloOutput._HomeSSD_box0_offset2
+ _OBJC_IVAR_$_SignificantActivityYoloOutput._HomeSSD_box0_offset3
+ _OBJC_IVAR_$_SignificantActivityYoloOutput._HomeSSD_box0_offset4
+ _OBJC_IVAR_$_SignificantActivityYoloOutput._HomeSSD_box1_offset0
+ _OBJC_IVAR_$_SignificantActivityYoloOutput._HomeSSD_box1_offset1
+ _OBJC_IVAR_$_SignificantActivityYoloOutput._HomeSSD_box1_offset2
+ _OBJC_IVAR_$_SignificantActivityYoloOutput._HomeSSD_box1_offset3
+ _OBJC_IVAR_$_SignificantActivityYoloOutput._HomeSSD_box1_offset4
+ _OBJC_IVAR_$_SignificantActivityYoloOutput._HomeSSD_class_prob0
+ _OBJC_IVAR_$_SignificantActivityYoloOutput._HomeSSD_class_prob1
+ _OBJC_IVAR_$_SignificantActivityYoloOutput._HomeSSD_class_prob2
+ _OBJC_IVAR_$_SignificantActivityYoloOutput._HomeSSD_class_prob3
+ _OBJC_IVAR_$_SignificantActivityYoloOutput._HomeSSD_class_prob4
+ _OBJC_IVAR_$_SignificantActivityYoloOutput._HomeSSD_object_roll0
+ _OBJC_IVAR_$_SignificantActivityYoloOutput._HomeSSD_object_roll1
+ _OBJC_IVAR_$_SignificantActivityYoloOutput._HomeSSD_object_roll2
+ _OBJC_IVAR_$_SignificantActivityYoloOutput._HomeSSD_object_roll3
+ _OBJC_IVAR_$_SignificantActivityYoloOutput._HomeSSD_object_roll4
+ _OBJC_IVAR_$_SignificantActivityYoloOutput._HomeSSD_object_yaw0
+ _OBJC_IVAR_$_SignificantActivityYoloOutput._HomeSSD_object_yaw1
+ _OBJC_IVAR_$_SignificantActivityYoloOutput._HomeSSD_object_yaw2
+ _OBJC_IVAR_$_SignificantActivityYoloOutput._HomeSSD_object_yaw3
+ _OBJC_IVAR_$_SignificantActivityYoloOutput._HomeSSD_object_yaw4
+ _OBJC_METACLASS_$_SignificantActivityYolo
+ _OBJC_METACLASS_$_SignificantActivityYoloInput
+ _OBJC_METACLASS_$_SignificantActivityYoloOutput
+ __OBJC_$_CLASS_METHODS_SignificantActivityYolo
+ __OBJC_$_INSTANCE_METHODS_SignificantActivityYolo
+ __OBJC_$_INSTANCE_METHODS_SignificantActivityYoloInput
+ __OBJC_$_INSTANCE_METHODS_SignificantActivityYoloOutput
+ __OBJC_$_INSTANCE_VARIABLES_SignificantActivityYolo
+ __OBJC_$_INSTANCE_VARIABLES_SignificantActivityYoloInput
+ __OBJC_$_INSTANCE_VARIABLES_SignificantActivityYoloOutput
+ __OBJC_$_PROP_LIST_SignificantActivityYolo
+ __OBJC_$_PROP_LIST_SignificantActivityYoloInput
+ __OBJC_$_PROP_LIST_SignificantActivityYoloOutput
+ __OBJC_CLASS_PROTOCOLS_$_SignificantActivityYoloInput
+ __OBJC_CLASS_PROTOCOLS_$_SignificantActivityYoloOutput
+ __OBJC_CLASS_RO_$_SignificantActivityYolo
+ __OBJC_CLASS_RO_$_SignificantActivityYoloInput
+ __OBJC_CLASS_RO_$_SignificantActivityYoloOutput
+ __OBJC_METACLASS_RO_$_SignificantActivityYolo
+ __OBJC_METACLASS_RO_$_SignificantActivityYoloInput
+ __OBJC_METACLASS_RO_$_SignificantActivityYoloOutput
+ ___68-[SignificantActivityYolo predictionFromFeatures:completionHandler:]_block_invoke
+ ___76-[SignificantActivityYolo predictionFromFeatures:options:completionHandler:]_block_invoke
+ ___77+[SignificantActivityYolo loadContentsOfURL:configuration:completionHandler:]_block_invoke
+ __os_feature_enabled_impl
+ _objc_msgSend$canReadLength:
+ _objc_msgSend$failReadOfLength:
+ _objc_msgSend$hmiPrivateErrorWithCode:reason:
+ _objc_msgSend$remainingLength
CStrings:
+ "CameraSignificantActivityModelV2"
+ "Could not load SignificantActivityYolo.mlmodelc in the bundle resource"
+ "Home"
+ "No activity"
+ "Refusing to read %llu bytes at position %llu, only %llu bytes remain."
+ "Refusing to seek to %llu, data is only %lu bytes long."
+ "Sensitive content"
+ "SignificantActivityYolo"
+ "Truncated atom header at offset %llu."
+ "Truncated atom header, expected an mfhd atom."
+ "Truncated extended size field for atom at offset %llu."
+ "Truncated mfhd atom."
+ "Unexpected %@ atom, expected an mfhd atom."
+ "Unexpected sequence number %u, expected greater than %u."
+ "Unsafe content"
+ "[%{public}@] Refusing to read %llu bytes at position %llu, only %llu bytes remain."
+ "[%{public}@] Refusing to seek to %llu, data is only %lu bytes long."
+ "[%{public}@] Truncated atom header at offset %llu."
+ "[%{public}@] Truncated atom header, expected an mfhd atom."
+ "[%{public}@] Truncated extended size field for atom at offset %llu."
+ "[%{public}@] Truncated mfhd atom."
+ "[%{public}@] Unexpected %@ atom, expected an mfhd atom."
+ "[%{public}@] Unexpected sequence number %u, expected greater than %u."
```
