## SiriTurnTakingManager

> `/System/Library/PrivateFrameworks/SiriTurnTakingManager.framework/Versions/A/SiriTurnTakingManager`

```diff

-3520.27.1.0.0
-  __TEXT.__text: 0x23dfc
+3605.4.1.0.0
+  __TEXT.__text: 0x248a0
   __TEXT.__objc_methlist: 0x108
-  __TEXT.__const: 0x1374
-  __TEXT.__swift5_typeref: 0x670
-  __TEXT.__swift5_fieldmd: 0xabc
-  __TEXT.__constg_swiftt: 0xb1c
-  __TEXT.__swift5_reflstr: 0x645
-  __TEXT.__swift5_capture: 0x36c
-  __TEXT.__oslogstring: 0x1cc2
+  __TEXT.__const: 0x1404
+  __TEXT.__swift5_typeref: 0x6ee
+  __TEXT.__swift5_fieldmd: 0xb04
+  __TEXT.__constg_swiftt: 0xbac
+  __TEXT.__swift5_reflstr: 0x675
+  __TEXT.__swift5_capture: 0x384
+  __TEXT.__oslogstring: 0x1e02
   __TEXT.__cstring: 0x692
-  __TEXT.__swift5_protos: 0x1c
-  __TEXT.__swift5_proto: 0xdc
-  __TEXT.__swift5_types: 0xa4
+  __TEXT.__swift5_protos: 0x24
+  __TEXT.__swift5_proto: 0xe4
+  __TEXT.__swift5_types: 0xa8
   __TEXT.__swift5_assocty: 0x60
-  __TEXT.__unwind_info: 0x998
-  __TEXT.__eh_frame: 0x798
+  __TEXT.__unwind_info: 0x9a8
+  __TEXT.__eh_frame: 0x768
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__const: 0xf0
   __DATA_CONST.__objc_classlist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x270
+  __DATA_CONST.__objc_selrefs: 0x2b0
   __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__const: 0x21a0
-  __AUTH_CONST.__objc_const: 0x970
-  __AUTH_CONST.__auth_got: 0x830
+  __AUTH_CONST.__const: 0x2238
+  __AUTH_CONST.__objc_const: 0x9b0
+  __AUTH_CONST.__auth_got: 0x838
   __AUTH.__objc_data: 0x240
   __DATA.__data: 0x1a8
   __DATA_DIRTY.__objc_data: 0x4e0
-  __DATA_DIRTY.__data: 0xb08
+  __DATA_DIRTY.__data: 0xb38
   __DATA_DIRTY.__common: 0x60
   __DATA_DIRTY.__bss: 0x100
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /System/Library/PrivateFrameworks/AssistantServices.framework/Versions/A/AssistantServices
   - /System/Library/PrivateFrameworks/CDMFoundation.framework/Versions/A/CDMFoundation
   - /System/Library/PrivateFrameworks/CoreSpeech.framework/Versions/A/CoreSpeech
+  - /System/Library/PrivateFrameworks/CoreSpeechFoundation.framework/Versions/A/CoreSpeechFoundation
   - /System/Library/PrivateFrameworks/FeatureStore.framework/Versions/A/FeatureStore
   - /System/Library/PrivateFrameworks/InternalSwiftProtobuf.framework/Versions/A/InternalSwiftProtobuf
   - /System/Library/PrivateFrameworks/SiriAnalytics.framework/Versions/A/SiriAnalytics

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1006
-  Symbols:   608
-  CStrings:  168
+  Functions: 1019
+  Symbols:   627
+  CStrings:  171
 
Symbols:
+ _OBJC_CLASS_$_CSUtils
+ _OBJC_CLASS_$_SLNCThresholdConfiguration
+ ___swift_mutable_project_boxed_opaque_existential_1
+ __swift_closure_destructor.51Tm
+ _objc_msgSend$getCSDeviceType
+ _objc_msgSend$getMitigationAssetWithCompletion:
+ _objc_msgSend$hasThresholds
+ _objc_msgSend$initWithConfig:bnnsIrPath:ncThresholdConfiguration:error:
+ _objc_msgSend$initWithMitigationAsset:
+ _objc_msgSend$mode
+ _objc_msgSend$selfPlatform
+ _objc_msgSend$setSelfPlatform:
+ _objc_msgSend$setServingPlatform:
+ _objc_msgSend$supportsConfigurationBasedNCThresholds
+ _swift_makeBoxUnique
+ _symbolic $s21SiriTurnTakingManager15CSUtilsProviderP
+ _symbolic $s21SiriTurnTakingManager16SLUresMitigatingP
+ _symbolic So26SLNCThresholdConfigurationCSg
+ _symbolic _____ 21SiriTurnTakingManager22DefaultCSUtilsProviderV
+ _symbolic ______p 21SiriTurnTakingManager15CSUtilsProviderP
+ _symbolic ______pSg 21SiriTurnTakingManager16SLUresMitigatingP
+ _symbolic x
- _objc_msgSend$initWithConfig:bnnsIrPath:error:
- _objc_msgSend$initWithConfig:error:
- _symbolic So15SLUresMitigatorCSg
CStrings:
+ "Completion block of getMitigationAsset invoked and ncThresholdConfiguration is cached"
+ "fetching mitigation asset from MitigationAssetProvider with error: %s"
+ "processTTCandidate: usingConfigThresholds=%{bool}d, selfPlatform=%lu, mode=%lu"
+ "using config path - %s for loading NC (bnnsIrPath empty=%{bool}d, ncThresholdConfiguration=%{bool}d)"
- "using config path - %s for loading NC"
```
