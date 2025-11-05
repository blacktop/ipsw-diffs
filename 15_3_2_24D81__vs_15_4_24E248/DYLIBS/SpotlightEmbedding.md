## SpotlightEmbedding

> `/System/Library/PrivateFrameworks/SpotlightEmbedding.framework/Versions/A/SpotlightEmbedding`

```diff

-2328.7.8.7.0
-  __TEXT.__text: 0x44c8
-  __TEXT.__auth_stubs: 0x270
-  __TEXT.__objc_methlist: 0x2d4
-  __TEXT.__const: 0xa8
-  __TEXT.__cstring: 0x304
-  __TEXT.__gcc_except_tab: 0x13c
-  __TEXT.__oslogstring: 0x49d
-  __TEXT.__unwind_info: 0x168
+2333.22.13.7.0
+  __TEXT.__text: 0x495c
+  __TEXT.__auth_stubs: 0x280
+  __TEXT.__objc_methlist: 0x2c4
+  __TEXT.__const: 0xb0
+  __TEXT.__cstring: 0x3cc
+  __TEXT.__gcc_except_tab: 0x14c
+  __TEXT.__oslogstring: 0x4a7
+  __TEXT.__unwind_info: 0x170
   __TEXT.__objc_classname: 0x4d
-  __TEXT.__objc_methname: 0xa03
-  __TEXT.__objc_methtype: 0x1c2
-  __TEXT.__objc_stubs: 0xaa0
-  __DATA_CONST.__got: 0xc0
-  __DATA_CONST.__const: 0x48
+  __TEXT.__objc_methname: 0xa2e
+  __TEXT.__objc_methtype: 0x1b2
+  __TEXT.__objc_stubs: 0xb40
+  __DATA_CONST.__got: 0xc8
+  __DATA_CONST.__const: 0x68
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x338
+  __DATA_CONST.__objc_selrefs: 0x358
   __DATA_CONST.__objc_superrefs: 0x20
-  __DATA_CONST.__objc_arraydata: 0x8
-  __AUTH_CONST.__auth_got: 0x148
+  __AUTH_CONST.__auth_got: 0x150
   __AUTH_CONST.__const: 0x2a0
-  __AUTH_CONST.__cfstring: 0x220
+  __AUTH_CONST.__cfstring: 0x360
   __AUTH_CONST.__objc_const: 0x530
   __AUTH_CONST.__objc_intobj: 0x30
-  __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0x140
   __DATA.__objc_ivar: 0x3c
   __DATA.__bss: 0x60
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreSpotlight.framework/Versions/A/CoreSpotlight
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
+  - /System/Library/PrivateFrameworks/CoreAnalytics.framework/Versions/A/CoreAnalytics
   - /System/Library/PrivateFrameworks/CoreSceneUnderstanding.framework/Versions/A/CoreSceneUnderstanding
-  - /System/Library/PrivateFrameworks/GenerativeModels.framework/Versions/A/GenerativeModels
   - /System/Library/PrivateFrameworks/MediaAnalysis.framework/Versions/A/MediaAnalysis
   - /System/Library/PrivateFrameworks/MediaAnalysisServices.framework/Versions/A/MediaAnalysisServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 521916D9-DFEC-3A15-AB2F-74A81D802364
-  Functions: 95
-  Symbols:   329
-  CStrings:  228
+  UUID: 8CF078C8-1CAD-3F14-AB13-61E1F5AA7134
+  Functions: 99
+  Symbols:   340
+  CStrings:  252
 
Symbols:
+ +[SPEmbeddingModel sharedInstance].cold.1
+ +[SPEmbeddingTokenizer sharedInstance].cold.1
+ -[SPEmbeddingModel generateEmbeddingForTextInputs:extendedContextLength:bundleID:queryID:clientBundleID:timeout:useCLIPSafety:computeThreshold:workCost:error:]
+ -[SPEmbeddingModel generateEmbeddingForTextInputs:extendedContextLength:bundleID:queryID:clientBundleID:timeout:workCost:error:]
+ -[SPEmbeddingModel generateEmbeddingForTextInputs:extendedContextLength:queryID:clientBundleID:timeout:useCLIPSafety:workCost:error:]
+ GCC_except_table38
+ _AnalyticsSendEventLazy
+ _OBJC_CLASS_$_CSGenerativeModelsAvailabilityManager
+ _OBJC_CLASS_$_NSBundle
+ __159-[SPEmbeddingModel generateEmbeddingForTextInputs:extendedContextLength:bundleID:queryID:clientBundleID:timeout:useCLIPSafety:computeThreshold:workCost:error:]_block_invoke.70
+ __49-[SPEmbeddingModel preheatWithCompletionHandler:]_block_invoke.33
+ ___159-[SPEmbeddingModel generateEmbeddingForTextInputs:extendedContextLength:bundleID:queryID:clientBundleID:timeout:useCLIPSafety:computeThreshold:workCost:error:]_block_invoke
+ ___block_descriptor_145_e8_32s40s48s56s64s72r80r88r96r_e20_v20?0i8"NSError"12l
+ ___block_descriptor_147_e8_32s40s48s56s64s72r80r88r96r104r_e5_v8?0l
+ ___block_descriptor_44_e19_"NSDictionary"8?0l
+ ___copy_helper_block_e8_32s40s48s56s64s72r80r88r96r
+ ___copy_helper_block_e8_32s40s48s56s64s72r80r88r96r104r
+ ___destroy_helper_block_e8_32s40s48s56s64s72r80r88r96r
+ ___destroy_helper_block_e8_32s40s48s56s64s72r80r88r96r104r
+ ___sendSpotlightEmbeddingAnalyticsEvent_block_invoke
+ __block_literal_global.132
+ __getDeviceSupported_block_invoke.cold.2
+ _objc_msgSend$bundleIdentifier
+ _objc_msgSend$generateEmbeddingForTextInputs:extendedContextLength:bundleID:queryID:clientBundleID:timeout:useCLIPSafety:computeThreshold:workCost:error:
+ _objc_msgSend$generateEmbeddingForTextInputs:extendedContextLength:queryID:clientBundleID:timeout:useCLIPSafety:workCost:error:
+ _objc_msgSend$hasPrefix:
+ _objc_msgSend$isEqual:
+ _objc_msgSend$isSemanticSearchAvailable
+ _objc_msgSend$mainBundle
+ _objc_msgSend$numberWithUnsignedInt:
+ _sendSpotlightEmbeddingAnalyticsEvent
- -[SPEmbeddingModel generateEmbeddingForTextInputs:extendedContextLength:bundleID:queryID:timeout:useCLIPSafety:workCost:error:]
- -[SPEmbeddingModel generateEmbeddingForTextInputs:extendedContextLength:bundleID:queryID:timeout:workCost:error:]
- -[SPEmbeddingModel generateEmbeddingForTextInputs:extendedContextLength:queryID:timeout:useCLIPSafety:workCost:error:]
- -[SPEmbeddingModel generateEmbeddingForTextInputs:extendedContextLength:queryID:timeout:workCost:error:]
- GCC_except_table39
- _OBJC_CLASS_$_GMAvailabilityWrapper
- _OBJC_CLASS_$_NSConstantArray
- __127-[SPEmbeddingModel generateEmbeddingForTextInputs:extendedContextLength:bundleID:queryID:timeout:useCLIPSafety:workCost:error:]_block_invoke.51
- __49-[SPEmbeddingModel preheatWithCompletionHandler:]_block_invoke.13
- ___127-[SPEmbeddingModel generateEmbeddingForTextInputs:extendedContextLength:bundleID:queryID:timeout:useCLIPSafety:workCost:error:]_block_invoke
- ___block_descriptor_129_e8_32s40s48s56s64r72r80r_e20_v20?0i8"NSError"12l
- ___block_descriptor_130_e8_32s40s48s56s64r72r80r88r_e5_v8?0l
- ___copy_helper_block_e8_32s40s48s56s64r72r80r
- ___copy_helper_block_e8_32s40s48s56s64r72r80r88r
- ___destroy_helper_block_e8_32s40s48s56s64r72r80r
- ___destroy_helper_block_e8_32s40s48s56s64r72r80r88r
- __block_literal_global.115
- _objc_msgSend$currentWithUseCaseIdentifiers:
- _objc_msgSend$generateEmbeddingForTextInputs:extendedContextLength:bundleID:queryID:timeout:useCLIPSafety:workCost:error:
- _objc_msgSend$generateEmbeddingForTextInputs:extendedContextLength:queryID:timeout:useCLIPSafety:workCost:error:
CStrings:
+ "@\"NSDictionary\"8@?0"
+ "@72@0:8@16B24q28@36q44B52^q56^@64"
+ "@76@0:8@16B24@28q36@44q52^q60^@68"
+ "@84@0:8@16B24@28q36@44q52B60B64^q68^@76"
+ "Device does not support embeddings"
+ "[qid=%ld] MADRequest as QOS (%d) client:%@"
+ "bundleIdentifier"
+ "caller"
+ "client"
+ "com.apple.Photos"
+ "com.apple.Spotlight"
+ "com.apple.email"
+ "com.apple.mail"
+ "com.apple.omniSearch"
+ "com.apple.spotlightembeddings.errors"
+ "com.apple.spotlightknowledged"
+ "errorCode"
+ "generateEmbeddingForTextInputs:extendedContextLength:bundleID:queryID:clientBundleID:timeout:useCLIPSafety:computeThreshold:workCost:error:"
+ "generateEmbeddingForTextInputs:extendedContextLength:bundleID:queryID:clientBundleID:timeout:workCost:error:"
+ "generateEmbeddingForTextInputs:extendedContextLength:queryID:clientBundleID:timeout:useCLIPSafety:workCost:error:"
+ "hasPrefix:"
+ "isEqual:"
+ "isSemanticSearchAvailable"
+ "mainBundle"
+ "numberWithUnsignedInt:"
- "@60@0:8@16B24q28q36^q44^@52"
- "@64@0:8@16B24q28q36B44^q48^@56"
- "@68@0:8@16B24@28q36q44^q52^@60"
- "@72@0:8@16B24@28q36q44B52^q56^@64"
- "[qid=%ld] MADRequest as QOS (%d)"
- "com.apple.spotlight.semanticSearch"
- "currentWithUseCaseIdentifiers:"
- "generateEmbeddingForTextInputs:extendedContextLength:bundleID:queryID:timeout:useCLIPSafety:workCost:error:"
- "generateEmbeddingForTextInputs:extendedContextLength:bundleID:queryID:timeout:workCost:error:"
- "generateEmbeddingForTextInputs:extendedContextLength:queryID:timeout:useCLIPSafety:workCost:error:"
- "generateEmbeddingForTextInputs:extendedContextLength:queryID:timeout:workCost:error:"

```
