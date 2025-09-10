## libmecabra.dylib

> `/usr/lib/libmecabra.dylib`

```diff

-1062.205.0.0.0
-  __TEXT.__text: 0x2548b0
-  __TEXT.__auth_stubs: 0x27a0
+1062.307.0.0.0
+  __TEXT.__text: 0x25d258
+  __TEXT.__auth_stubs: 0x2780
   __TEXT.__objc_methlist: 0x3d0
-  __TEXT.__const: 0x22f98
-  __TEXT.__cstring: 0x109ac
+  __TEXT.__const: 0x23007
+  __TEXT.__cstring: 0x10b4b
   __TEXT.__ustring: 0x794e
-  __TEXT.__gcc_except_tab: 0x1913c
-  __TEXT.__oslogstring: 0x3725
-  __TEXT.__dlopen_cstrs: 0x104
-  __TEXT.__unwind_info: 0xc0c4
+  __TEXT.__gcc_except_tab: 0x1940c
+  __TEXT.__oslogstring: 0x3b7f
+  __TEXT.__dlopen_cstrs: 0x152
+  __TEXT.__unwind_info: 0xc018
   __TEXT.__eh_frame: 0x38
   __TEXT.__objc_classname: 0x69
   __TEXT.__objc_methname: 0x15d4
   __TEXT.__objc_methtype: 0x14d
   __TEXT.__objc_stubs: 0x1a20
   __DATA_CONST.__got: 0x340
-  __DATA_CONST.__const: 0x8468
+  __DATA_CONST.__const: 0x85e0
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x1f0
   __DATA_CONST.__objc_selrefs: 0x758
+  __DATA_CONST.__objc_classrefs: 0xe8
+  __DATA_CONST.__objc_superrefs: 0x18
   __DATA_CONST.__objc_arraydata: 0x208
-  __AUTH_CONST.__const: 0x40278
-  __AUTH_CONST.__cfstring: 0x8cc0
+  __AUTH_CONST.__const: 0x40380
+  __AUTH_CONST.__cfstring: 0x8d60
   __AUTH_CONST.__objc_arrayobj: 0xf0
   __AUTH_CONST.__objc_const: 0x1f0
-  __AUTH_CONST.__auth_got: 0x13e8
+  __AUTH_CONST.__auth_got: 0x13d8
   __AUTH.__data: 0x1e0
   __AUTH.__objc_data: 0xf0
-  __DATA.__objc_classrefs: 0xe8
-  __DATA.__objc_superrefs: 0x18
   __DATA.__objc_ivar: 0x20
-  __DATA.__data: 0x4f58
+  __DATA.__data: 0x4f68
   __DATA.__thread_vars: 0x270
   __DATA.__thread_bss: 0xd10
   __DATA.__common: 0x940
-  __DATA.__bss: 0x25e4
+  __DATA.__bss: 0x262c
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 098B5301-EC56-3AD3-B91A-9A6481B5FA0E
-  Functions: 10188
-  Symbols:   1070
-  CStrings:  5053
+  UUID: E902030C-6728-35CF-94D2-9F30A175DE9F
+  Functions: 10277
+  Symbols:   1069
+  CStrings:  5086
 
Symbols:
+ _kMecabraCreationUseMontrealLanguageModelKey
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC1ERKS5_
- __ZNSt3__115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEE3strERKNS_12basic_stringIcS2_S4_EE
CStrings:
+ "CFArrayGetCount(other) == otherExpectedSize"
+ "Feature flag activate: useMontreal_KO = 1"
+ "Feature flag activate: useMontreal_TH = 1"
+ "Feature flag activated: useMontreal_JA = true"
+ "Feature flag detected: useMontreal_JA"
+ "Feature flag detected: useMontreal_KO"
+ "Feature flag detected: useMontreal_TH"
+ "Feature flag is not activate: useMontreal_KO = 0"
+ "Feature flag is not activate: useMontreal_TH = 0"
+ "Feature flag is not enabled: useMontreal_JA = false"
+ "JapaneseRNNLMPredictor.h"
+ "MRLNeuralNetworkCopyStates"
+ "MRLNeuralNetworkCreate"
+ "MRLNeuralNetworkGetOutput"
+ "MRLNeuralNetworkPredict"
+ "MRLNeuralNetworkSetInput"
+ "Montreal assets are not reachable: %@"
+ "Montreal model creation by MRLNeuralNetworkCreate caught an error: %@"
+ "MontrealLanguageModel.cpp"
+ "[Inference Engine: %s]"
+ "[MontrealLanguageModel::isModelAvaiable] model for batched joint probability isn't avaiable. Does the bundle contain function name '%s'?"
+ "[MontrealLanguageModel::isModelAvaiable] model for batched prediction isn't avaiable. Does the bundle contain function name '%s'?"
+ "[MontrealLanguageModel::isModelAvaiable] model for joint probability isn't avaiable. Does the bundle contain function name '%s'?"
+ "[MontrealLanguageModel::isModelAvaiable] model for prediction isn't avaiable."
+ "[MontrealLanguageModel::jointProbabilityBatchedInference]"
+ "[MontrealLanguageModel::jointProbabilitySingleInference]"
+ "batch32"
+ "extendStates"
+ "kMRLNeuralNetworkModelTypeE5RT"
+ "kMRLNeuralNetworkOptionModelTypeKey"
+ "kMRLNeuralNetworkOptionModelURLKey"
+ "label"
+ "lm->type() != NeuralLanguageModelEngineType::None"
+ "logJointProb"
+ "logJointProb_batch32"
+ "logits"
+ "model_mil/lstm.mil"
+ "setLM"
+ "softlink:o:path:/System/Library/PrivateFrameworks/Montreal.framework/Montreal"
+ "useMontrealLM"
+ "useMontreal_JA"
+ "useMontreal_KO"
+ "useMontreal_TH"
- "ascii"
- "cp932"
- "euc"
- "euc-jp"
- "euc_jp"
- "mixed"
- "none"
- "shift-jis"
- "shift_jis"
- "single_character"
- "sjis"
- "system"
- "utf-8"
- "wakati"

```
