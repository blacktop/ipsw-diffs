## SensitiveContentAnalysisML

> `/System/Library/PrivateFrameworks/SensitiveContentAnalysisML.framework/SensitiveContentAnalysisML`

```diff

 165.5.0.0.0
-  __TEXT.__text: 0xf0cb0
-  __TEXT.__objc_methlist: 0x1ef4
-  __TEXT.__const: 0x1157c
-  __TEXT.__gcc_except_tab: 0x453c
-  __TEXT.__cstring: 0x3ea6
-  __TEXT.__oslogstring: 0x1fd3
+  __TEXT.__text: 0xf652c
+  __TEXT.__objc_methlist: 0x1fcc
+  __TEXT.__const: 0x1191c
+  __TEXT.__gcc_except_tab: 0x4614
+  __TEXT.__cstring: 0x3fc6
+  __TEXT.__oslogstring: 0x2193
   __TEXT.__dlopen_cstrs: 0xb0
-  __TEXT.__swift5_typeref: 0x29cd
-  __TEXT.__swift5_fieldmd: 0x2588
-  __TEXT.__constg_swiftt: 0x2bbc
-  __TEXT.__swift5_reflstr: 0x1169
-  __TEXT.__swift5_builtin: 0xb4
+  __TEXT.__swift5_typeref: 0x2a81
+  __TEXT.__swift5_fieldmd: 0x2698
+  __TEXT.__constg_swiftt: 0x2da4
+  __TEXT.__swift5_reflstr: 0x1259
+  __TEXT.__swift5_builtin: 0xdc
   __TEXT.__swift5_assocty: 0x4c8
-  __TEXT.__swift5_protos: 0x20
-  __TEXT.__swift5_proto: 0x1010
-  __TEXT.__swift5_types: 0x420
-  __TEXT.__swift_as_entry: 0x190
-  __TEXT.__swift_as_ret: 0x228
-  __TEXT.__swift_as_cont: 0x574
-  __TEXT.__swift5_capture: 0x43c
+  __TEXT.__swift5_protos: 0x24
+  __TEXT.__swift5_proto: 0x101c
+  __TEXT.__swift5_types: 0x444
+  __TEXT.__swift_as_entry: 0x1b8
+  __TEXT.__swift_as_ret: 0x250
+  __TEXT.__swift_as_cont: 0x5ac
+  __TEXT.__swift5_capture: 0x4cc
   __TEXT.__swift5_mpenum: 0x10
-  __TEXT.__unwind_info: 0x64c0
-  __TEXT.__eh_frame: 0x8d40
+  __TEXT.__unwind_info: 0x6718
+  __TEXT.__eh_frame: 0x9358
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x7c8
-  __DATA_CONST.__objc_classlist: 0x260
+  __DATA_CONST.__const: 0x8d0
+  __DATA_CONST.__objc_classlist: 0x288
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x10
-  __DATA_CONST.__objc_selrefs: 0x11a0
+  __DATA_CONST.__objc_selrefs: 0x11e8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x128
   __DATA_CONST.__objc_arraydata: 0x1f8
-  __DATA_CONST.__got: 0x8e8
-  __AUTH_CONST.__const: 0xa5c0
-  __AUTH_CONST.__cfstring: 0x1b00
-  __AUTH_CONST.__objc_const: 0x57d8
+  __DATA_CONST.__got: 0x950
+  __AUTH_CONST.__const: 0xa840
+  __AUTH_CONST.__cfstring: 0x1b20
+  __AUTH_CONST.__objc_const: 0x5b28
   __AUTH_CONST.__weak_auth_got: 0x28
   __AUTH_CONST.__objc_intobj: 0x138
   __AUTH_CONST.__objc_arrayobj: 0xf0
-  __AUTH_CONST.__auth_got: 0x19e8
-  __DATA.__objc_ivar: 0x308
-  __DATA.__data: 0x24e0
+  __AUTH_CONST.__auth_got: 0x1aa0
+  __DATA.__objc_ivar: 0x31c
+  __DATA.__data: 0x2530
   __DATA.__common: 0x98
-  __DATA_DIRTY.__objc_data: 0x1a60
-  __DATA_DIRTY.__data: 0x2710
+  __DATA_DIRTY.__objc_data: 0x1d40
+  __DATA_DIRTY.__data: 0x29b8
   __DATA_DIRTY.__bss: 0x16f0
   __DATA_DIRTY.__common: 0xb0
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /System/Library/PrivateFrameworks/ModelCatalog.framework/ModelCatalog
   - /System/Library/PrivateFrameworks/ModelManagerServices.framework/ModelManagerServices
   - /System/Library/PrivateFrameworks/PromptKit.framework/PromptKit
+  - /System/Library/PrivateFrameworks/RegionalSafetyAnalysis.framework/RegionalSafetyAnalysis
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /System/Library/PrivateFrameworks/TokenGeneration.framework/TokenGeneration
   - /System/Library/PrivateFrameworks/TokenGenerationCore.framework/TokenGenerationCore

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 6271
-  Symbols:   3912
-  CStrings:  804
+  Functions: 6398
+  Symbols:   3998
+  CStrings:  822
 
Symbols:
+ -[SCMLImageSanitizationSignal isChinaPolicySignal]
+ -[SCMLImageSanitizationSignal setIsChinaPolicySignal:]
+ -[SCMLImageSanitizerConfiguration regionalSafetyImplFactory]
+ -[SCMLImageSanitizerConfiguration setRegionalSafetyImplFactory:]
+ -[SCMLTextSanitizerConfiguration regionalSafetyImplFactory]
+ -[SCMLTextSanitizerConfiguration setRegionalSafetyImplFactory:]
+ GCC_except_table117
+ GCC_except_table118
+ GCC_except_table119
+ GCC_except_table56
+ GCC_except_table75
+ GCC_except_table76
+ GCC_except_table77
+ GCC_except_table89
+ GCC_except_table94
+ _OBJC_CLASS_$__TtC26SensitiveContentAnalysisML18BiomeEventsDonator
+ _OBJC_CLASS_$__TtC26SensitiveContentAnalysisML24SCMLRegionalErrorUtility
+ _OBJC_CLASS_$__TtC26SensitiveContentAnalysisML29SCMLRegionalSafetyImplFactory
+ _OBJC_IVAR_$_SCMLImageSanitizationSignal._isChinaPolicySignal
+ _OBJC_IVAR_$_SCMLImageSanitizer._biomeEventsDonator
+ _OBJC_IVAR_$_SCMLImageSanitizerConfiguration._regionalSafetyImplFactory
+ _OBJC_IVAR_$_SCMLTextSanitizer._biomeEventsDonator
+ _OBJC_IVAR_$_SCMLTextSanitizerConfiguration._regionalSafetyImplFactory
+ _OBJC_METACLASS_$__TtC26SensitiveContentAnalysisML18BiomeEventsDonator
+ _OBJC_METACLASS_$__TtC26SensitiveContentAnalysisML24SCMLRegionalErrorUtility
+ _OBJC_METACLASS_$__TtC26SensitiveContentAnalysisML29SCMLRegionalSafetyImplFactory
+ __CLASS_METHODS__TtC26SensitiveContentAnalysisML24SCMLRegionalErrorUtility
+ __DATA__TtC26SensitiveContentAnalysisML18BiomeEventsDonator
+ __DATA__TtC26SensitiveContentAnalysisML21RegionalTextSanitizer
+ __DATA__TtC26SensitiveContentAnalysisML22RegionalImageSanitizer
+ __DATA__TtC26SensitiveContentAnalysisML24SCMLRegionalErrorUtility
+ __DATA__TtC26SensitiveContentAnalysisML29SCMLRegionalSafetyImplFactory
+ __INSTANCE_METHODS__TtC26SensitiveContentAnalysisML18BiomeEventsDonator
+ __INSTANCE_METHODS__TtC26SensitiveContentAnalysisML24SCMLRegionalErrorUtility
+ __INSTANCE_METHODS__TtC26SensitiveContentAnalysisML29SCMLRegionalSafetyImplFactory
+ __IVARS__TtC26SensitiveContentAnalysisML18BiomeEventsDonator
+ __IVARS__TtC26SensitiveContentAnalysisML21RegionalTextSanitizer
+ __IVARS__TtC26SensitiveContentAnalysisML22RegionalImageSanitizer
+ __METACLASS_DATA__TtC26SensitiveContentAnalysisML18BiomeEventsDonator
+ __METACLASS_DATA__TtC26SensitiveContentAnalysisML21RegionalTextSanitizer
+ __METACLASS_DATA__TtC26SensitiveContentAnalysisML22RegionalImageSanitizer
+ __METACLASS_DATA__TtC26SensitiveContentAnalysisML24SCMLRegionalErrorUtility
+ __METACLASS_DATA__TtC26SensitiveContentAnalysisML29SCMLRegionalSafetyImplFactory
+ __ZNKSt3__110__function6__funcIZ49-[SCMLTextSanitizer initWithConfiguration:error:]E3$_1FvvEE11target_typeEv
+ __ZNKSt3__110__function6__funcIZ49-[SCMLTextSanitizer initWithConfiguration:error:]E3$_1FvvEE6targetERKSt9type_info
+ __ZNKSt3__110__function6__funcIZ49-[SCMLTextSanitizer initWithConfiguration:error:]E3$_1FvvEE7__cloneEPNS0_6__baseIS3_EE
+ __ZNKSt3__110__function6__funcIZ49-[SCMLTextSanitizer initWithConfiguration:error:]E3$_1FvvEE7__cloneEv
+ __ZNKSt3__110__function6__funcIZZ69-[SCMLTextSanitizer sanitizeRequestAsynchronously:completionHandler:]EUb_E3$_2FvvEE11target_typeEv
+ __ZNKSt3__110__function6__funcIZZ69-[SCMLTextSanitizer sanitizeRequestAsynchronously:completionHandler:]EUb_E3$_2FvvEE6targetERKSt9type_info
+ __ZNKSt3__110__function6__funcIZZ69-[SCMLTextSanitizer sanitizeRequestAsynchronously:completionHandler:]EUb_E3$_2FvvEE7__cloneEPNS0_6__baseIS3_EE
+ __ZNKSt3__110__function6__funcIZZ69-[SCMLTextSanitizer sanitizeRequestAsynchronously:completionHandler:]EUb_E3$_2FvvEE7__cloneEv
+ __ZNSt3__110__function6__funcIZ49-[SCMLTextSanitizer initWithConfiguration:error:]E3$_1FvvEE18destroy_deallocateEv
+ __ZNSt3__110__function6__funcIZ49-[SCMLTextSanitizer initWithConfiguration:error:]E3$_1FvvEE7destroyEv
+ __ZNSt3__110__function6__funcIZ49-[SCMLTextSanitizer initWithConfiguration:error:]E3$_1FvvEED0Ev
+ __ZNSt3__110__function6__funcIZ49-[SCMLTextSanitizer initWithConfiguration:error:]E3$_1FvvEED1Ev
+ __ZNSt3__110__function6__funcIZ49-[SCMLTextSanitizer initWithConfiguration:error:]E3$_1FvvEEclEv
+ __ZNSt3__110__function6__funcIZZ69-[SCMLTextSanitizer sanitizeRequestAsynchronously:completionHandler:]EUb_E3$_2FvvEE18destroy_deallocateEv
+ __ZNSt3__110__function6__funcIZZ69-[SCMLTextSanitizer sanitizeRequestAsynchronously:completionHandler:]EUb_E3$_2FvvEE7destroyEv
+ __ZNSt3__110__function6__funcIZZ69-[SCMLTextSanitizer sanitizeRequestAsynchronously:completionHandler:]EUb_E3$_2FvvEED0Ev
+ __ZNSt3__110__function6__funcIZZ69-[SCMLTextSanitizer sanitizeRequestAsynchronously:completionHandler:]EUb_E3$_2FvvEED1Ev
+ __ZNSt3__110__function6__funcIZZ69-[SCMLTextSanitizer sanitizeRequestAsynchronously:completionHandler:]EUb_E3$_2FvvEEclEv
+ __ZTINSt3__110__function6__funcIZ49-[SCMLTextSanitizer initWithConfiguration:error:]E3$_1FvvEEE
+ __ZTINSt3__110__function6__funcIZZ69-[SCMLTextSanitizer sanitizeRequestAsynchronously:completionHandler:]EUb_E3$_2FvvEEE
+ __ZTIZ49-[SCMLTextSanitizer initWithConfiguration:error:]E3$_1
+ __ZTIZZ69-[SCMLTextSanitizer sanitizeRequestAsynchronously:completionHandler:]EUb_E3$_2
+ __ZTSNSt3__110__function6__funcIZ49-[SCMLTextSanitizer initWithConfiguration:error:]E3$_1FvvEEE
+ __ZTSNSt3__110__function6__funcIZZ69-[SCMLTextSanitizer sanitizeRequestAsynchronously:completionHandler:]EUb_E3$_2FvvEEE
+ __ZTSZ49-[SCMLTextSanitizer initWithConfiguration:error:]E3$_1
+ __ZTSZZ69-[SCMLTextSanitizer sanitizeRequestAsynchronously:completionHandler:]EUb_E3$_2
+ __ZTVNSt3__110__function6__funcIZ49-[SCMLTextSanitizer initWithConfiguration:error:]E3$_1FvvEEE
+ __ZTVNSt3__110__function6__funcIZZ69-[SCMLTextSanitizer sanitizeRequestAsynchronously:completionHandler:]EUb_E3$_2FvvEEE
+ ___69-[SCMLTextSanitizer sanitizeRequestAsynchronously:completionHandler:]_block_invoke_2
+ ___70-[SCMLImageSanitizer sanitizeRequestAsynchronously:completionHandler:]_block_invoke_2
+ ___block_descriptor_56_ea8_32s40s48bs_e17_v16?0"NSError"8ls48l8s32l8s40l8
+ ___block_descriptor_56_ea8_32s40s48bs_e42_v24?0"SCMLTextSanitization"8"NSError"16ls32l8s40l8s48l8
+ ___block_descriptor_56_ea8_32s40s48bs_e43_v24?0"SCMLImageSanitization"8"NSError"16ls32l8s40l8s48l8
+ ___swift_assignWithCopy_strong
+ ___swift_assignWithTake_strong
+ ___swift_closure_destructorTm
+ ___swift_destroy_strong
+ ___swift_initWithCopy_strong
+ _kSCMLImageSanitizationSignalChinaSanitizer
+ _kSCMLTextSanitizationSignalChinaSanitizer
+ _swift_release_x9
+ _symbolic $s26SensitiveContentAnalysisML18RegionalSafetyImplP
+ _symbolic So6NSUUIDCSg
+ _symbolic _____ 10ObjectiveC8ObjCBoolV
+ _symbolic _____ 12ModelCatalog0B6ClientC
+ _symbolic _____ 22RegionalSafetyAnalysis0abC14SendableClientC
+ _symbolic _____ 22RegionalSafetyAnalysis8SeverityO
+ _symbolic _____ 26SensitiveContentAnalysisML018SCMLRegionalSafetyC8ResponseV
+ _symbolic _____ 26SensitiveContentAnalysisML18BiomeEventsDonatorC
+ _symbolic _____ 26SensitiveContentAnalysisML21RegionalTextSanitizerC
+ _symbolic _____ 26SensitiveContentAnalysisML22RealRegionalSafetyImplV
+ _symbolic _____ 26SensitiveContentAnalysisML22RegionalImageSanitizerC
+ _symbolic _____ 26SensitiveContentAnalysisML24SCMLRegionalErrorUtilityC
+ _symbolic _____ 26SensitiveContentAnalysisML29SCMLRegionalSafetyImplFactoryC
+ _symbolic _____ So26SCMLTextSanitizerTextStyleV
+ _symbolic _____ So28SCMLImageSanitizerImageStyleV
+ _symbolic _____Sg 10Foundation4UUIDV
+ _symbolic _____Sg 22RegionalSafetyAnalysis0abC14SendableClientC0E5ErrorO
+ _symbolic _____Sg_ABt 22RegionalSafetyAnalysis0abC14SendableClientC0E5ErrorO
+ _symbolic ______p 26SensitiveContentAnalysisML18RegionalSafetyImplP
+ _type_layout_string 26SensitiveContentAnalysisML22RealRegionalSafetyImplV
- GCC_except_table113
- GCC_except_table49
- GCC_except_table51
- GCC_except_table73
- __ZNKSt3__110__function6__funcIZZ69-[SCMLTextSanitizer sanitizeRequestAsynchronously:completionHandler:]EUb_E3$_1FvvEE11target_typeEv
- __ZNKSt3__110__function6__funcIZZ69-[SCMLTextSanitizer sanitizeRequestAsynchronously:completionHandler:]EUb_E3$_1FvvEE6targetERKSt9type_info
- __ZNKSt3__110__function6__funcIZZ69-[SCMLTextSanitizer sanitizeRequestAsynchronously:completionHandler:]EUb_E3$_1FvvEE7__cloneEPNS0_6__baseIS3_EE
- __ZNKSt3__110__function6__funcIZZ69-[SCMLTextSanitizer sanitizeRequestAsynchronously:completionHandler:]EUb_E3$_1FvvEE7__cloneEv
- __ZNSt3__110__function6__funcIZZ69-[SCMLTextSanitizer sanitizeRequestAsynchronously:completionHandler:]EUb_E3$_1FvvEE18destroy_deallocateEv
- __ZNSt3__110__function6__funcIZZ69-[SCMLTextSanitizer sanitizeRequestAsynchronously:completionHandler:]EUb_E3$_1FvvEE7destroyEv
- __ZNSt3__110__function6__funcIZZ69-[SCMLTextSanitizer sanitizeRequestAsynchronously:completionHandler:]EUb_E3$_1FvvEED0Ev
- __ZNSt3__110__function6__funcIZZ69-[SCMLTextSanitizer sanitizeRequestAsynchronously:completionHandler:]EUb_E3$_1FvvEED1Ev
- __ZNSt3__110__function6__funcIZZ69-[SCMLTextSanitizer sanitizeRequestAsynchronously:completionHandler:]EUb_E3$_1FvvEEclEv
- __ZTINSt3__110__function6__funcIZZ69-[SCMLTextSanitizer sanitizeRequestAsynchronously:completionHandler:]EUb_E3$_1FvvEEE
- __ZTIZZ69-[SCMLTextSanitizer sanitizeRequestAsynchronously:completionHandler:]EUb_E3$_1
- __ZTSNSt3__110__function6__funcIZZ69-[SCMLTextSanitizer sanitizeRequestAsynchronously:completionHandler:]EUb_E3$_1FvvEEE
- __ZTSZZ69-[SCMLTextSanitizer sanitizeRequestAsynchronously:completionHandler:]EUb_E3$_1
- __ZTVNSt3__110__function6__funcIZZ69-[SCMLTextSanitizer sanitizeRequestAsynchronously:completionHandler:]EUb_E3$_1FvvEEE
CStrings:
+ "B"
+ "Begin RegionalTextSanitizer.sanitize override = %{bool}d"
+ "End RegionalImageSanitizer.sanitize"
+ "End RegionalTextSanitizer.sanitize"
+ "End RegionalTextSanitizer.sanitize result has been overridden to safe=%{bool}d sensitive=%{bool}d, severity=%s"
+ "RegionalImageSanitizer %s"
+ "RegionalTextSanitizer %s"
+ "Request style: %u"
+ "SCMLTextSanitizer.init.regional"
+ "SensitiveContentAnalysisML.BiomeEventsDonator"
+ "dijob.tbojujafs"
+ "failed to donate 1P guardrail result: %@"
+ "init(configuration:)"
+ "regionalImageAnalyzer"
+ "regionalTextAnalyzer"
+ "regionalsafety.text.override"
+ "regionalsafety.text.safe"
+ "regionalsafety.text.sensitive"
+ "regionalsafety.text.severity"
- "A"
```
