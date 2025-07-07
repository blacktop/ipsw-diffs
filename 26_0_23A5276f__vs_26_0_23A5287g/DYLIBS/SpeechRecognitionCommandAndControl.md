## SpeechRecognitionCommandAndControl

> `/System/Library/PrivateFrameworks/SpeechRecognitionCommandAndControl.framework/SpeechRecognitionCommandAndControl`

```diff

-138.0.0.0.0
-  __TEXT.__text: 0x9ecb8
+140.0.0.0.0
+  __TEXT.__text: 0x9f06c
   __TEXT.__auth_stubs: 0x2090
-  __TEXT.__objc_methlist: 0xab1c
+  __TEXT.__objc_methlist: 0xab34
   __TEXT.__const: 0xbf4
-  __TEXT.__oslogstring: 0x28f5
-  __TEXT.__cstring: 0x6f37
-  __TEXT.__gcc_except_tab: 0x1fa0
+  __TEXT.__oslogstring: 0x2935
+  __TEXT.__cstring: 0x6f67
+  __TEXT.__gcc_except_tab: 0x1f5c
   __TEXT.__ustring: 0x3a
   __TEXT.__constg_swiftt: 0x2dc
   __TEXT.__swift5_typeref: 0xd3e

   __TEXT.__swift5_types: 0x24
   __TEXT.__swift5_fieldmd: 0x134
   __TEXT.__swift5_capture: 0x10
-  __TEXT.__unwind_info: 0x28f0
+  __TEXT.__unwind_info: 0x2900
   __TEXT.__eh_frame: 0x218
   __TEXT.__objc_classname: 0x164e
-  __TEXT.__objc_methname: 0x1e1cd
+  __TEXT.__objc_methname: 0x1e272
   __TEXT.__objc_methtype: 0x3f3b
-  __TEXT.__objc_stubs: 0x138a0
-  __DATA_CONST.__got: 0xe80
+  __TEXT.__objc_stubs: 0x13980
+  __DATA_CONST.__got: 0xe98
   __DATA_CONST.__const: 0x1a30
   __DATA_CONST.__objc_classlist: 0x428
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x1a8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6fc0
+  __DATA_CONST.__objc_selrefs: 0x7000
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x2a0
   __DATA_CONST.__objc_arraydata: 0x858
   __AUTH_CONST.__auth_got: 0x1058
-  __AUTH_CONST.__const: 0x1880
-  __AUTH_CONST.__cfstring: 0x88c0
+  __AUTH_CONST.__const: 0x1860
+  __AUTH_CONST.__cfstring: 0x88e0
   __AUTH_CONST.__objc_const: 0xeec0
   __AUTH_CONST.__objc_intobj: 0x348
   __AUTH_CONST.__objc_doubleobj: 0x50

   - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration
   - /System/Library/PrivateFrameworks/MediaExperience.framework/MediaExperience
   - /System/Library/PrivateFrameworks/OnBoardingKit.framework/OnBoardingKit
+  - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
   - /System/Library/PrivateFrameworks/SpeakThisServices.framework/SpeakThisServices
   - /System/Library/PrivateFrameworks/SpeechRecognitionCommandServices.framework/SpeechRecognitionCommandServices
   - /System/Library/PrivateFrameworks/SpeechRecognitionCore.framework/SpeechRecognitionCore

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: D9ED9DD2-B02D-354C-9437-3D639247F990
-  Functions: 4228
-  Symbols:   14771
-  CStrings:  7972
+  UUID: EA1EBF47-64BC-3140-AE53-ECD0E51190E4
+  Functions: 4230
+  Symbols:   14783
+  CStrings:  7983
 
Symbols:
+ -[CACSpokenCommand(CACSpokenCommandGestures) systemPressKeySpace]
+ -[CACSpokenCommand(CACSpokenCommandHardware) activateTypeToSiri]
+ _OBJC_CLASS_$_RBSProcessPredicate
+ _OBJC_CLASS_$_RBSTerminateContext
+ _OBJC_CLASS_$_RBSTerminateRequest
+ ___35-[CACSpokenCommand searchSpotlight]_block_invoke.720
+ ___35-[CACSpokenCommand searchSpotlight]_block_invoke.720.cold.1
+ ___41-[CACSpokenCommand closeFrontApplication]_block_invoke
+ ___62+[CACApplicationUtilities terminateApplicationWithIdentifier:]_block_invoke.cold.1
+ ___block_descriptor_40_e8_32s_e25_v32?0"NSString"816^B24ls32l8
+ ___block_literal_global.307
+ ___block_literal_global.614
+ ___block_literal_global.636
+ ___block_literal_global.643
+ ___block_literal_global.692
+ ___block_literal_global.694
+ ___block_literal_global.704
+ ___block_literal_global.719
+ _objc_msgSend$activateTypeToSiri
+ _objc_msgSend$execute:
+ _objc_msgSend$initWithExplanation:
+ _objc_msgSend$initWithPredicate:context:
+ _objc_msgSend$isSiriVisible
+ _objc_msgSend$isTypeToSiriVisible
+ _objc_msgSend$predicateMatchingBundleIdentifier:
- ___35-[CACSpokenCommand searchSpotlight]_block_invoke.719
- ___35-[CACSpokenCommand searchSpotlight]_block_invoke.719.cold.1
- ___block_descriptor_40_e8_32r_e25_v32?0"NSString"816^B24lr32l8
- ___block_literal_global.101
- ___block_literal_global.299
- ___block_literal_global.613
- ___block_literal_global.635
- ___block_literal_global.642
- ___block_literal_global.673
- ___block_literal_global.691
- ___block_literal_global.693
- ___block_literal_global.695
- ___block_literal_global.703
- ___block_literal_global.718
CStrings:
+ "Failed to terminate existing instance of bundle identifier '%@'"
+ "Voice Control user requesting app termination"
+ "activateTypeToSiri"
+ "execute:"
+ "initWithExplanation:"
+ "initWithPredicate:context:"
+ "isSiriVisible"
+ "isTypeToSiriVisible"
+ "predicateMatchingBundleIdentifier:"
+ "systemPressKeySpace"

```
