## SignpostSupport

> `/System/Library/PrivateFrameworks/SignpostSupport.framework/SignpostSupport`

```diff

-173.0.0.0.0
-  __TEXT.__text: 0x48f54
+173.0.1.0.0
+  __TEXT.__text: 0x49b44
   __TEXT.__auth_stubs: 0x5b0
-  __TEXT.__objc_methlist: 0x622c
-  __TEXT.__const: 0x228
-  __TEXT.__cstring: 0x16da9
-  __TEXT.__oslogstring: 0xe6a
+  __TEXT.__objc_methlist: 0x62a4
+  __TEXT.__const: 0x238
+  __TEXT.__cstring: 0x16ef4
+  __TEXT.__oslogstring: 0xeb0
   __TEXT.__gcc_except_tab: 0x28c
   __TEXT.__ustring: 0x3e
-  __TEXT.__unwind_info: 0x11c0
+  __TEXT.__unwind_info: 0x11f0
   __TEXT.__objc_classname: 0xd2a
-  __TEXT.__objc_methname: 0xea97
-  __TEXT.__objc_methtype: 0x118e
-  __TEXT.__objc_stubs: 0x88e0
+  __TEXT.__objc_methname: 0xece9
+  __TEXT.__objc_methtype: 0x11b8
+  __TEXT.__objc_stubs: 0x89e0
   __DATA_CONST.__got: 0x300
-  __DATA_CONST.__const: 0xb78
+  __DATA_CONST.__const: 0xbc0
   __DATA_CONST.__objc_classlist: 0x2e8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2990
+  __DATA_CONST.__objc_selrefs: 0x29d8
   __DATA_CONST.__objc_superrefs: 0x260
   __DATA_CONST.__objc_arraydata: 0x5058
   __AUTH_CONST.__auth_got: 0x2e8
-  __AUTH_CONST.__const: 0xae0
-  __AUTH_CONST.__cfstring: 0x183c0
-  __AUTH_CONST.__objc_const: 0xd800
+  __AUTH_CONST.__const: 0xb40
+  __AUTH_CONST.__cfstring: 0x18400
+  __AUTH_CONST.__objc_const: 0xd850
   __AUTH_CONST.__objc_arrayobj: 0x3c0
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_intobj: 0x1b0
   __AUTH.__objc_data: 0x5f0
-  __DATA.__objc_ivar: 0x8ec
-  __DATA.__data: 0xb48
-  __DATA.__bss: 0x3a0
+  __DATA.__objc_ivar: 0x8f0
+  __DATA.__data: 0xb60
+  __DATA.__bss: 0x3b0
   __DATA_DIRTY.__objc_data: 0x1720
   __DATA_DIRTY.__bss: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: AE7CB759-1712-3EC0-B9A5-19C4B0A45990
-  Functions: 2306
-  Symbols:   7683
-  CStrings:  8985
+  UUID: 607FB286-E40B-3144-9C97-5E8280C5EBF1
+  Functions: 2324
+  Symbols:   7738
+  CStrings:  9006
 
Symbols:
+ +[SignpostAnimationInterval effectiveGlitchTimeRatioContributedVersion]
+ +[SignpostAnimationInterval effectiveGlitchTimeRatioContributedVersion].cold.1
+ +[SignpostAnimationInterval effectiveGlitchTimeRatioContributedVersion].cold.2
+ +[SignpostAnimationInterval forcedGlitchTimeRatioContributedVersion]
+ +[SignpostAnimationInterval normalizeOverrunIntervals:]
+ +[SignpostAnimationInterval setForcedGlitchTimeRatioContributedVersion:]
+ -[SignpostAnimationInterval _timeRatioForTimeIntervalArray:applyPerceptionAdjustments:].cold.1
+ -[SignpostAnimationSubInterval setStartMachContinuousTime:]
+ -[SignpostFrameLifetimeInterval _glitchIntervalBeginTime:roundingUp:previousMCT:hasLongUpdateSequence:]
+ -[SignpostFrameLifetimeInterval _glitchIntervalWithRoundingUp:previousMCT:hasLongUpdateSequence:]
+ -[SignpostFrameLifetimeInterval _inProcessGlitchIntervalBeginTime:targetMCT:previousMCT:hasLongUpdateSequence:]
+ -[SignpostFrameLifetimeInterval _inProcessGlitchIntervalBeginTime:targetMCT:previousMCT:hasLongUpdateSequence:].cold.1
+ -[SignpostFrameLifetimeInterval _inProcessGlitchIntervalWithTargetMCT:previousMCT:hasLongUpdateSequence:]
+ -[SignpostFrameLifetimeInterval isMaintaningFrameCadanceWithPreviousFrameLifetime]
+ -[SignpostFrameLifetimeInterval setIsMaintaningFrameCadanceWithPreviousFrameLifetime:]
+ -[SignpostUpdateSequenceInterval _durationRelativeToLifetimeAndPreviousUpdate]
+ _OBJC_IVAR_$_SignpostFrameLifetimeInterval._isMaintaningFrameCadanceWithPreviousFrameLifetime
+ _OUTLINED_FUNCTION_4
+ ___55+[SignpostAnimationInterval normalizeOverrunIntervals:]_block_invoke
+ ___55+[SignpostAnimationInterval normalizeOverrunIntervals:]_block_invoke_2
+ ___71+[SignpostAnimationInterval effectiveGlitchTimeRatioContributedVersion]_block_invoke
+ ___87-[SignpostAnimationInterval _timeRatioForTimeIntervalArray:applyPerceptionAdjustments:]_block_invoke_2
+ ___block_descriptor_32_e71_q24?0"SignpostFrameOverrunInterval"8"SignpostFrameOverrunInterval"16l
+ ___block_descriptor_40_e8_32s_e55_B24?0"SignpostFrameOverrunInterval"8"NSDictionary"16ls32l8
+ ___block_descriptor_48_e8_32s_e39_Q16?0"<SignpostSupportTimeInterval>"8ls32l8
+ ___block_literal_global.1043
+ ___block_literal_global.692
+ ___block_literal_global.736
+ ___block_literal_global.744
+ ___block_literal_global.747
+ ___block_literal_global.751
+ ___block_literal_global.754
+ ___block_literal_global.756
+ ___block_literal_global.758
+ ___block_literal_global.760
+ ___block_literal_global.762
+ ___block_literal_global.764
+ ___block_literal_global.858
+ __forcedGlitchTimeRatioContributedVersion
+ __timeRatioForTimeIntervalArray:applyPerceptionAdjustments:.concurrentAdjustement
+ __timeRatioForTimeIntervalArray:applyPerceptionAdjustments:.onceToken
+ _effectiveGlitchTimeRatioContributedVersion.onceToken
+ _effectiveGlitchTimeRatioContributedVersion.userDefaultsVersion
+ _objc_msgSend$_durationRelativeToLifetimeAndPreviousUpdate
+ _objc_msgSend$_glitchIntervalBeginTime:roundingUp:previousMCT:hasLongUpdateSequence:
+ _objc_msgSend$_glitchIntervalWithRoundingUp:previousMCT:hasLongUpdateSequence:
+ _objc_msgSend$_inProcessGlitchIntervalBeginTime:targetMCT:previousMCT:hasLongUpdateSequence:
+ _objc_msgSend$_inProcessGlitchIntervalWithTargetMCT:previousMCT:hasLongUpdateSequence:
+ _objc_msgSend$effectiveGlitchTimeRatioContributedVersion
+ _objc_msgSend$forcedGlitchTimeRatioContributedVersion
+ _objc_msgSend$isMaintaningFrameCadanceWithPreviousFrameLifetime
+ _objc_msgSend$normalizeOverrunIntervals:
+ _objc_msgSend$setIsMaintaningFrameCadanceWithPreviousFrameLifetime:
- -[SignpostFrameLifetimeInterval _glitchIntervalWithRoundingUp:previousMCT:]
- -[SignpostFrameLifetimeInterval _inProcessGlitchIntervalWithRoundingUp:targetMCT:previousMCT:]
- -[SignpostFrameLifetimeInterval _inProcessGlitchIntervalWithRoundingUp:targetMCT:previousMCT:].cold.1
- ___block_descriptor_40_e8_32s_e39_Q16?0"<SignpostSupportTimeInterval>"8ls32l8
- ___block_literal_global.1011
- ___block_literal_global.716
- ___block_literal_global.720
- ___block_literal_global.724
- ___block_literal_global.727
- ___block_literal_global.729
- ___block_literal_global.731
- ___block_literal_global.735
- ___block_literal_global.737
- ___block_literal_global.831
- _objc_msgSend$_glitchIntervalWithRoundingUp:previousMCT:
- _objc_msgSend$_inProcessGlitchIntervalWithRoundingUp:targetMCT:previousMCT:
CStrings:
+ "%s: Unknown GlitchTimeRatioContributedVersion %lu, - reverting to %lu"
+ "+[SignpostAnimationInterval effectiveGlitchTimeRatioContributedVersion]"
+ "@32@0:8B16Q20B28"
+ "B24@?0@\"SignpostFrameOverrunInterval\"8@\"NSDictionary\"16"
+ "B40@0:8^Q16B24Q28B36"
+ "B44@0:8^Q16Q24Q32B40"
+ "SignpostSupportOverrideDefaultGlitchTimeRatioConcurrentAdjustment"
+ "SignpostSupportOverrideDefaultGlitchTimeRatioContributedVersion"
+ "TB,N,V_isMaintaningFrameCadanceWithPreviousFrameLifetime"
+ "_durationRelativeToLifetimeAndPreviousUpdate"
+ "_glitchIntervalBeginTime:roundingUp:previousMCT:hasLongUpdateSequence:"
+ "_glitchIntervalWithRoundingUp:previousMCT:hasLongUpdateSequence:"
+ "_inProcessGlitchIntervalBeginTime:targetMCT:previousMCT:hasLongUpdateSequence:"
+ "_inProcessGlitchIntervalWithTargetMCT:previousMCT:hasLongUpdateSequence:"
+ "_isMaintaningFrameCadanceWithPreviousFrameLifetime"
+ "effectiveGlitchTimeRatioContributedVersion"
+ "forcedGlitchTimeRatioContributedVersion"
+ "isMaintaningFrameCadanceWithPreviousFrameLifetime"
+ "normalizeOverrunIntervals:"
+ "overridden"
+ "q24@?0@\"SignpostFrameOverrunInterval\"8@\"SignpostFrameOverrunInterval\"16"
+ "setForcedGlitchTimeRatioContributedVersion:"
+ "setIsMaintaningFrameCadanceWithPreviousFrameLifetime:"
- "@36@0:8B16Q20Q28"
- "Overriden"
- "_glitchIntervalWithRoundingUp:previousMCT:"
- "_inProcessGlitchIntervalWithRoundingUp:targetMCT:previousMCT:"

```
