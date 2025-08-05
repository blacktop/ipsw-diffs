## SpotlightEmbedding

> `/System/Library/PrivateFrameworks/SpotlightEmbedding.framework/SpotlightEmbedding`

```diff

-2387.1.0.0.0
-  __TEXT.__text: 0x5508
-  __TEXT.__auth_stubs: 0x460
+2391.1.0.0.0
+  __TEXT.__text: 0x5554
+  __TEXT.__auth_stubs: 0x470
   __TEXT.__objc_methlist: 0x374
   __TEXT.__const: 0xc0
-  __TEXT.__cstring: 0x512
+  __TEXT.__cstring: 0x523
   __TEXT.__gcc_except_tab: 0x240
   __TEXT.__oslogstring: 0x5be
   __TEXT.__dlopen_cstrs: 0x58

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x450
   __DATA_CONST.__objc_superrefs: 0x28
-  __DATA_CONST.__objc_arraydata: 0x10
-  __AUTH_CONST.__auth_got: 0x240
+  __AUTH_CONST.__auth_got: 0x248
   __AUTH_CONST.__const: 0x80
   __AUTH_CONST.__cfstring: 0x480
   __AUTH_CONST.__objc_const: 0x630
   __AUTH_CONST.__objc_intobj: 0x30
-  __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH_CONST.__objc_floatobj: 0x10
+  __AUTH_CONST.__objc_floatobj: 0x20
   __AUTH.__objc_data: 0x50
   __DATA.__objc_ivar: 0x48
   __DATA.__bss: 0x8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
-  UUID: 92B60D0E-6EC7-3895-9452-29DADE4CD89B
+  UUID: 7F00C781-D240-3618-9BE5-3874E21EF0D5
   Functions: 102
-  Symbols:   533
+  Symbols:   532
   CStrings:  322
 
Symbols:
+ ___159-[SPEmbeddingModel generateEmbeddingForTextInputs:extendedContextLength:bundleID:queryID:clientBundleID:timeout:useCLIPSafety:computeThreshold:workCost:error:]_block_invoke.63
+ ___49-[SPEmbeddingModel preheatWithCompletionHandler:]_block_invoke.35
+ ___block_descriptor_145_e8_32s40s48s56s64s72r80r88r96r_e20_v20?0i8"NSError"12lr72l8s32l8s40l8r80l8s48l8r88l8s56l8r96l8s64l8
+ _arc4random_uniform
- _OBJC_CLASS_$_NSConstantDictionary
- _OBJC_CLASS_$_NSConstantDoubleNumber
- ___159-[SPEmbeddingModel generateEmbeddingForTextInputs:extendedContextLength:bundleID:queryID:clientBundleID:timeout:useCLIPSafety:computeThreshold:workCost:error:]_block_invoke.64
- ___49-[SPEmbeddingModel preheatWithCompletionHandler:]_block_invoke.36
- ___block_descriptor_145_e8_32s40s48s56s64s72r80r88r96r_e20_v20?0i8"NSError"12lr72l8s32l8s40l8r80l8r88l8s48l8r96l8s56l8s64l8
Functions:
~ ___159-[SPEmbeddingModel generateEmbeddingForTextInputs:extendedContextLength:bundleID:queryID:clientBundleID:timeout:useCLIPSafety:computeThreshold:workCost:error:]_block_invoke : 1100 -> 1084
~ ___159-[SPEmbeddingModel generateEmbeddingForTextInputs:extendedContextLength:bundleID:queryID:clientBundleID:timeout:useCLIPSafety:computeThreshold:workCost:error:]_block_invoke.64 -> ___159-[SPEmbeddingModel generateEmbeddingForTextInputs:extendedContextLength:bundleID:queryID:clientBundleID:timeout:useCLIPSafety:computeThreshold:workCost:error:]_block_invoke.63 : 1956 -> 2024
~ _sendSpotlightEmbeddingAnalyticsEvent : 380 -> 404
CStrings:
+ "com.apple.MobileSMS"
- "zh"

```
