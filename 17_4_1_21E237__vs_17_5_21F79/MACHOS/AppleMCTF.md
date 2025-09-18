## AppleMCTF

> `/System/Library/Video/Plug-Ins/AppleMCTF.bundle/AppleMCTF`

```diff

-760.23.1.0.0
-  __TEXT.__text: 0xea9f0
+760.30.1.0.0
+  __TEXT.__text: 0xebab4
   __TEXT.__auth_stubs: 0xeb0
   __TEXT.__init_offsets: 0x8
-  __TEXT.__cstring: 0x647d0
+  __TEXT.__cstring: 0x656b1
   __TEXT.__const: 0x107a8
   __TEXT.__gcc_except_tab: 0x1fc
   __TEXT.__unwind_info: 0x790
   __TEXT.__eh_frame: 0x38
   __DATA_CONST.__auth_got: 0x760
-  __DATA_CONST.__got: 0x8b0
+  __DATA_CONST.__got: 0x8b8
   __DATA_CONST.__auth_ptr: 0x30
   __DATA_CONST.__const: 0x2300
   __DATA_CONST.__cfstring: 0x23e0

   - /System/Library/PrivateFrameworks/OpticalFlowFramework.framework/OpticalFlowFramework
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: 64CDC7D0-762A-3357-8426-BE0FAD6DE3D8
+  UUID: AEFA6154-E695-3A45-BD3E-42B71CB53371
   Functions: 629
-  Symbols:   562
-  CStrings:  6582
+  Symbols:   563
+  CStrings:  6607
 
Symbols:
+ _kVTCompressionPropertyKey_AllowOpenGOP
CStrings:
+ "AVE_AddSupportedProperty(PropertyDictionary, kVTPropertyType_Boolean, ((CFStringRef) __builtin___CFStringMakeConstantString (\"\" \"EnableCrcQpModMode\" \"\")), false)"
+ "AVE_AddSupportedProperty(PropertyDictionary, kVTPropertyType_Boolean, ((CFStringRef) __builtin___CFStringMakeConstantString (\"\" \"EnableSEITagInsertion\" \"\")), false)"
+ "AVE_AddSupportedProperty(PropertyDictionary, kVTPropertyType_Boolean, ((CFStringRef) __builtin___CFStringMakeConstantString (\"\" \"EnableSliceEncodingMode\" \"\")), false)"
+ "AVE_AddSupportedProperty(PropertyDictionary, kVTPropertyType_Boolean, ((CFStringRef) __builtin___CFStringMakeConstantString (\"\" \"LrmePipeSyncMode\" \"\")), false)"
+ "AVE_AddSupportedProperty(PropertyDictionary, kVTPropertyType_Boolean, ((CFStringRef) __builtin___CFStringMakeConstantString (\"\" \"RCMode\" \"\")), false)"
+ "AVE_AddSupportedProperty(PropertyDictionary, kVTPropertyType_Number, ((CFStringRef) __builtin___CFStringMakeConstantString (\"\" \"EnableMultipleScalingMatrices\" \"\")), false)"
+ "AVE_AddSupportedProperty(PropertyDictionary, kVTPropertyType_Number, ((CFStringRef) __builtin___CFStringMakeConstantString (\"\" \"SVENum\" \"\")), false)"
+ "AVE_AddSupportedProperty(PropertyDictionaryHEIF, kVTPropertyType_Boolean, ((CFStringRef) __builtin___CFStringMakeConstantString (\"\" \"EnableAdaptB\" \"\")), false)"
+ "AVE_AddSupportedProperty(PropertyDictionaryHEIF, kVTPropertyType_Boolean, ((CFStringRef) __builtin___CFStringMakeConstantString (\"\" \"EnableVarianceQPMod\" \"\")), false)"
+ "AVE_AddSupportedProperty(PropertyDictionaryHEIF, kVTPropertyType_Boolean, ((CFStringRef) __builtin___CFStringMakeConstantString (\"\" \"FlatAreaLowQp\" \"\")), false)"
+ "AVE_AddSupportedProperty(PropertyDictionaryHEIF, kVTPropertyType_Boolean, ((CFStringRef) __builtin___CFStringMakeConstantString (\"\" \"RCMode\" \"\")), false)"
+ "AVE_AddSupportedProperty(PropertyDictionaryHEIF, kVTPropertyType_Boolean, ((CFStringRef) __builtin___CFStringMakeConstantString (\"\" \"UseAsyncFWScheduling\" \"\")), false)"
+ "AVE_AddSupportedProperty(PropertyDictionaryHEIF, kVTPropertyType_Boolean, kVTCompressionPropertyKey_AllowFrameReordering, false)"
+ "AVE_AddSupportedProperty(PropertyDictionaryHEIF, kVTPropertyType_Boolean, kVTCompressionPropertyKey_AllowOpenGOP, false)"
+ "AVE_AddSupportedProperty(PropertyDictionaryHEIF, kVTPropertyType_Boolean, kVTCompressionPropertyKey_PerceptualQualityOptimization, false)"
+ "AVE_AddSupportedProperty(PropertyDictionaryHEIF, kVTPropertyType_Number, ((CFStringRef) __builtin___CFStringMakeConstantString (\"\" \"BPictures\" \"\")), false)"
+ "AVE_AddSupportedProperty(PropertyDictionaryHEIF, kVTPropertyType_Number, ((CFStringRef) __builtin___CFStringMakeConstantString (\"\" \"EdgeReplication\" \"\")), false)"
+ "AVE_AddSupportedProperty(PropertyDictionaryHEIF, kVTPropertyType_Number, ((CFStringRef) __builtin___CFStringMakeConstantString (\"\" \"EnableAdaptB\" \"\")), false)"
+ "AVE_AddSupportedProperty(PropertyDictionaryHEIF, kVTPropertyType_Number, ((CFStringRef) __builtin___CFStringMakeConstantString (\"\" \"EnableStaticAreasLowQP\" \"\")), false)"
+ "AVE_AddSupportedProperty(PropertyDictionaryHEIF, kVTPropertyType_Number, ((CFStringRef) __builtin___CFStringMakeConstantString (\"\" \"EnableStatsCollect\" \"\")), false)"
+ "AVE_AddSupportedProperty(PropertyDictionaryHEIF, kVTPropertyType_Number, ((CFStringRef) __builtin___CFStringMakeConstantString (\"\" \"RCMode\" \"\")), false)"
+ "AVE_AddSupportedProperty(PropertyDictionaryHEIF, kVTPropertyType_Number, ((CFStringRef) __builtin___CFStringMakeConstantString (\"\" \"SVENum\" \"\")), false)"
+ "AVE_AddSupportedProperty(PropertyDictionaryHEIF, kVTPropertyType_Number, kVTCompressionPropertyKey_AverageBitRate, false)"
+ "AVE_AddSupportedProperty(PropertyDictionaryHEIF, kVTPropertyType_Number, kVTCompressionPropertyKey_ExpectedFrameRate, false)"
+ "AVE_AddSupportedProperty(PropertyDictionaryHEIF, kVTPropertyType_Number, kVTCompressionPropertyKey_NumberOfSlices, false)"

```
