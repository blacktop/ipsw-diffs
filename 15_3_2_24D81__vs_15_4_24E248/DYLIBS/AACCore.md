## AACCore

> `/System/Library/PrivateFrameworks/AACCore.framework/Versions/A/AACCore`

```diff

-14.2.5.0.0
-  __TEXT.__text: 0x1038c
+14.2.9.0.0
+  __TEXT.__text: 0x100bc
   __TEXT.__auth_stubs: 0x3d0
-  __TEXT.__objc_methlist: 0x1014
+  __TEXT.__objc_methlist: 0x145c
   __TEXT.__const: 0xe0
-  __TEXT.__cstring: 0xdfd
+  __TEXT.__cstring: 0xe6b
   __TEXT.__oslogstring: 0x5c3
-  __TEXT.__gcc_except_tab: 0x1b0
-  __TEXT.__unwind_info: 0x570
+  __TEXT.__gcc_except_tab: 0x1bc
+  __TEXT.__unwind_info: 0x550
   __TEXT.__objc_classname: 0x8a2
-  __TEXT.__objc_methname: 0x2669
-  __TEXT.__objc_methtype: 0x7ef
-  __TEXT.__objc_stubs: 0x1a60
+  __TEXT.__objc_methname: 0x2757
+  __TEXT.__objc_methtype: 0x7f7
+  __TEXT.__objc_stubs: 0x1b00
   __DATA_CONST.__got: 0x1d0
   __DATA_CONST.__const: 0x120
   __DATA_CONST.__objc_classlist: 0x1a8
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0xd0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x898
+  __DATA_CONST.__objc_selrefs: 0x940
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0x110
   __AUTH_CONST.__auth_got: 0x1f8
   __AUTH_CONST.__const: 0x600
-  __AUTH_CONST.__cfstring: 0xde0
-  __AUTH_CONST.__objc_const: 0x4120
+  __AUTH_CONST.__cfstring: 0xe20
+  __AUTH_CONST.__objc_const: 0x3b30
   __AUTH.__objc_data: 0x1090
-  __DATA.__objc_ivar: 0x1bc
+  __DATA.__objc_ivar: 0x1c4
   __DATA.__data: 0x9e0
   __DATA.__bss: 0x20
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 6F11F563-15B1-3CE4-9EDB-2B6D69795A1E
-  Functions: 485
-  Symbols:   1488
-  CStrings:  857
+  UUID: 0387BA07-21E1-3741-9001-6E25F9FFDF10
+  Functions: 510
+  Symbols:   1539
+  CStrings:  872
 
Symbols:
+ +[AEFileSystem assessmentAgentContainerURL].cold.1
+ -[AEActivePolicySession deactivateWithCompletion:].cold.1
+ -[AEAssessmentState allowsKeyboardMathSolving]
+ -[AEAssessmentState allowsMathPaperSolving]
+ -[AEAssessmentState setAllowsKeyboardMathSolving:]
+ -[AEAssessmentState setAllowsMathPaperSolving:]
+ -[AEConcreteProcessInfoPrimitives systemUptime]
+ -[AEPreference setPreferenceValue:].cold.1
+ AECoreErrorUserInfo.cold.1
+ AECoreLog.cold.1
+ OBJC_IVAR_$_AEAssessmentState._allowsKeyboardMathSolving
+ OBJC_IVAR_$_AEAssessmentState._allowsMathPaperSolving
+ _OUTLINED_FUNCTION_1
+ _OUTLINED_FUNCTION_2
+ _OUTLINED_FUNCTION_3
+ _OUTLINED_FUNCTION_4
+ _OUTLINED_FUNCTION_5
+ _OUTLINED_FUNCTION_6
+ _OUTLINED_FUNCTION_7
+ _OUTLINED_FUNCTION_8
+ __113-[AEPolicyBundle runWithRemainingActivations:remainingDeactivations:invalidationHandler:currentEvent:completion:]_block_invoke_4.cold.1
+ __48-[AEPolicyBundle activateSessionWithCompletion:]_block_invoke_2.cold.1
+ __48-[AEPolicyBundle activateSessionWithCompletion:]_block_invoke_2.cold.2
+ __OBJC_$_PROP_LIST_AEConcreteProcessInfoPrimitives
+ __OBJC_$_PROP_LIST_AEProcessInfoPrimitives
+ _objc_msgSend$allowsKeyboardMathSolving
+ _objc_msgSend$allowsMathPaperSolving
+ _objc_msgSend$setAllowsKeyboardMathSolving:
+ _objc_msgSend$setAllowsMathPaperSolving:
+ _objc_msgSend$systemUptime
- -[AEActiveRestrictionUUIDFetchingProxy setOfActiveRestrictionUUIDs:].cold.1
- __50-[AEActivePolicySession deactivateWithCompletion:]_block_invoke_2.cold.1
- __50-[AEActivePolicySession deactivateWithCompletion:]_block_invoke_2.cold.2
- __52-[AERecoveryPolicySession deactivateWithCompletion:]_block_invoke.5.cold.1
- __52-[AERecoveryPolicySession deactivateWithCompletion:]_block_invoke.5.cold.2
CStrings:
+ "<%@: %p { isEnabled = %@, mainIndividualConfiguration = %@, configurationsByApplicationDescriptor = %@, allowsAutoCorrection = %@, allowsSmartPunctuation = %@, allowsSpellCheck = %@, allowsPredictiveKeyboard = %@, allowsActivityContinuation = %@, allowsDictation = %@, allowsAccessibilitySpeech = %@, allowsPasswordAutoFill = %@, allowsContinuousPathKeyboard = %@, allowsKeyboardShortcuts = %@, allowsKeyboardMathSolving = %@, allowsMathPaperSolving = %@}>"
+ "TB,N,V_allowsKeyboardMathSolving"
+ "TB,N,V_allowsMathPaperSolving"
+ "Td,R"
+ "_allowsKeyboardMathSolving"
+ "_allowsMathPaperSolving"
+ "allowsKeyboardMathSolving"
+ "allowsMathPaperSolving"
+ "d16@0:8"
+ "setAllowsKeyboardMathSolving:"
+ "setAllowsMathPaperSolving:"
+ "systemUptime"
- "<%@: %p { isEnabled = %@, mainIndividualConfiguration = %@, configurationsByApplicationDescriptor = %@, allowsAutoCorrection = %@, allowsSmartPunctuation = %@, allowsSpellCheck = %@, allowsPredictiveKeyboard = %@, allowsActivityContinuation = %@, allowsDictation = %@, allowsAccessibilitySpeech = %@, allowsPasswordAutoFill = %@, allowsContinuousPathKeyboard = %@, allowsKeyboardShortcuts = %@}>"

```
