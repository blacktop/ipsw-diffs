## KRExperiments

> `/System/Library/PrivateFrameworks/KRExperiments.framework/Versions/A/KRExperiments`

```diff

-158.80.2.0.0
-  __TEXT.__text: 0xb24
-  __TEXT.__auth_stubs: 0x120
-  __TEXT.__const: 0x70
-  __TEXT.__cstring: 0xc4
-  __TEXT.__oslogstring: 0x157
-  __TEXT.__unwind_info: 0x70
-  __TEXT.__objc_methname: 0x208
-  __TEXT.__objc_stubs: 0x320
-  __DATA_CONST.__got: 0x18
+158.100.15.0.0
+  __TEXT.__text: 0x1318
+  __TEXT.__auth_stubs: 0x130
+  __TEXT.__const: 0x78
+  __TEXT.__cstring: 0x159
+  __TEXT.__oslogstring: 0x26e
+  __TEXT.__unwind_info: 0x80
+  __TEXT.__objc_methname: 0x2a0
+  __TEXT.__objc_stubs: 0x440
+  __DATA_CONST.__got: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xc8
-  __AUTH_CONST.__auth_got: 0x98
-  __AUTH_CONST.__cfstring: 0x100
+  __DATA_CONST.__objc_selrefs: 0x110
+  __AUTH_CONST.__auth_got: 0xa0
+  __AUTH_CONST.__const: 0x30
+  __AUTH_CONST.__cfstring: 0x1a0
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/PrivateFrameworks/Trial.framework/Versions/A/Trial
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: C6018E26-AAED-3885-B9F9-7152668B3EAB
-  Functions: 7
-  Symbols:   63
-  CStrings:  56
+  UUID: 7CE743D4-CD46-3293-B21F-F11D92288E2F
+  Functions: 11
+  Symbols:   77
+  CStrings:  86
 
Symbols:
+ _OBJC_CLASS_$_NSUserDefaults
+ _PrewarmingExperimentUpdated
+ __NSConcreteStackBlock
+ ___PrewarmingExperimentUpdated_block_invoke
+ ___block_descriptor_40_e8_32s_e24_v16?0"TRIFactorLevel"8l
+ ___copy_helper_block_e8_32s
+ ___destroy_helper_block_e8_32s
+ _objc_alloc
+ _objc_msgSend$boolForKey:
+ _objc_msgSend$initWithSuiteName:
+ _objc_msgSend$integerForKey:
+ _objc_msgSend$isEqual:
+ _objc_msgSend$removeObjectForKey:
+ _objc_msgSend$setBool:forKey:
+ _objc_msgSend$setInteger:forKey:
+ _objc_msgSend$synchronize
+ _objc_msgSend$treatmentIdWithNamespaceName:
- KRExperimentsUpdateExperimentState.cold.6
- KRExperimentsUpdateExperimentState.cold.7
- KRExperimentsUpdateExperimentState.cold.8
CStrings:
+ "(%@) WARNING -- UNKNOWN factor %@ !"
+ "(%@) discovered factor '%@'"
+ "Beginning to refresh Prewarming experiment state"
+ "COREOS_FAST_PREWARMING"
+ "Executed 'defaults delete %@ %@'"
+ "Executed 'defaults write %@ %@ %d'"
+ "PrewarmingExperimentUpdated: checking factors..."
+ "PrewarmingExperimentUpdated: no active treatment"
+ "boolForKey:"
+ "com.apple.coreos.fast"
+ "initWithSuiteName:"
+ "integerForKey:"
+ "isEqual:"
+ "null"
+ "off"
+ "on"
+ "prewarming_enable"
+ "prewarming_enable_2"
+ "prewarming_previous_enable_2"
+ "removeObjectForKey:"
+ "setBool:forKey:"
+ "setInteger:forKey:"
+ "synchronize"
+ "treatmentIdWithNamespaceName:"
+ "v16@?0@\"TRIFactorLevel\"8"

```
