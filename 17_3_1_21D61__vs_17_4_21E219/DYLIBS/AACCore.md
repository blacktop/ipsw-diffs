## AACCore

> `/System/Library/PrivateFrameworks/AACCore.framework/AACCore`

```diff

-13.0.2.0.0
-  __TEXT.__text: 0xb228
+13.4.3.0.0
+  __TEXT.__text: 0xbae4
   __TEXT.__auth_stubs: 0x520
-  __TEXT.__objc_methlist: 0xe40
+  __TEXT.__objc_methlist: 0xf30
   __TEXT.__const: 0x58
-  __TEXT.__cstring: 0x8c6
+  __TEXT.__cstring: 0xa9a
   __TEXT.__oslogstring: 0x21e
   __TEXT.__gcc_except_tab: 0x9c
-  __TEXT.__unwind_info: 0x4b8
-  __TEXT.__objc_classname: 0x75e
-  __TEXT.__objc_methname: 0x1d81
+  __TEXT.__unwind_info: 0x4b4
+  __TEXT.__objc_classname: 0x760
+  __TEXT.__objc_methname: 0x21ab
   __TEXT.__objc_methtype: 0x6b1
-  __TEXT.__objc_stubs: 0x1180
+  __TEXT.__objc_stubs: 0x13c0
   __DATA_CONST.__got: 0x68
   __DATA_CONST.__const: 0x520
   __DATA_CONST.__objc_classlist: 0x178
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0xb0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x2cc0
-  __DATA_CONST.__objc_selrefs: 0x660
-  __AUTH_CONST.__cfstring: 0x920
+  __DATA_CONST.__objc_const: 0x2ea0
+  __DATA_CONST.__objc_selrefs: 0x700
+  __DATA_CONST.__objc_protorefs: 0x20
+  __DATA_CONST.__objc_classrefs: 0x1e0
+  __DATA_CONST.__objc_superrefs: 0xf8
+  __AUTH_CONST.__cfstring: 0xa40
   __AUTH_CONST.__objc_const: 0x10f8
   __AUTH_CONST.__const: 0x60
   __AUTH_CONST.__auth_got: 0x2a0
   __AUTH.__objc_data: 0xeb0
-  __DATA.__objc_protorefs: 0x20
-  __DATA.__objc_classrefs: 0x1e0
-  __DATA.__objc_superrefs: 0xf8
-  __DATA.__objc_ivar: 0x150
+  __DATA.__objc_ivar: 0x178
   __DATA.__data: 0x860
   __DATA.__bss: 0x20
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/AccessibilityUtilities.framework/AccessibilityUtilities
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 392
-  Symbols:   1624
-  CStrings:  601
+  Functions: 412
+  Symbols:   1692
+  CStrings:  652
 
Symbols:
+ -[AEAssessmentState allowsAccessibilitySpeech]
+ -[AEAssessmentState allowsActivityContinuation]
+ -[AEAssessmentState allowsAutoCorrection]
+ -[AEAssessmentState allowsContinuousPathKeyboard]
+ -[AEAssessmentState allowsDictation]
+ -[AEAssessmentState allowsKeyboardShortcuts]
+ -[AEAssessmentState allowsPasswordAutoFill]
+ -[AEAssessmentState allowsPredictiveKeyboard]
+ -[AEAssessmentState allowsSmartPunctuation]
+ -[AEAssessmentState allowsSpellCheck]
+ -[AEAssessmentState setAllowsAccessibilitySpeech:]
+ -[AEAssessmentState setAllowsActivityContinuation:]
+ -[AEAssessmentState setAllowsAutoCorrection:]
+ -[AEAssessmentState setAllowsContinuousPathKeyboard:]
+ -[AEAssessmentState setAllowsDictation:]
+ -[AEAssessmentState setAllowsKeyboardShortcuts:]
+ -[AEAssessmentState setAllowsPasswordAutoFill:]
+ -[AEAssessmentState setAllowsPredictiveKeyboard:]
+ -[AEAssessmentState setAllowsSmartPunctuation:]
+ -[AEAssessmentState setAllowsSpellCheck:]
+ _OBJC_IVAR_$_AEAssessmentState._allowsAccessibilitySpeech
+ _OBJC_IVAR_$_AEAssessmentState._allowsActivityContinuation
+ _OBJC_IVAR_$_AEAssessmentState._allowsAutoCorrection
+ _OBJC_IVAR_$_AEAssessmentState._allowsContinuousPathKeyboard
+ _OBJC_IVAR_$_AEAssessmentState._allowsDictation
+ _OBJC_IVAR_$_AEAssessmentState._allowsKeyboardShortcuts
+ _OBJC_IVAR_$_AEAssessmentState._allowsPasswordAutoFill
+ _OBJC_IVAR_$_AEAssessmentState._allowsPredictiveKeyboard
+ _OBJC_IVAR_$_AEAssessmentState._allowsSmartPunctuation
+ _OBJC_IVAR_$_AEAssessmentState._allowsSpellCheck
+ _objc_msgSend$allowsAccessibilitySpeech
+ _objc_msgSend$allowsActivityContinuation
+ _objc_msgSend$allowsAutoCorrection
+ _objc_msgSend$allowsContinuousPathKeyboard
+ _objc_msgSend$allowsDictation
+ _objc_msgSend$allowsPasswordAutoFill
+ _objc_msgSend$allowsPredictiveKeyboard
+ _objc_msgSend$allowsSmartPunctuation
+ _objc_msgSend$allowsSpellCheck
+ _objc_msgSend$setAllowsAccessibilitySpeech:
+ _objc_msgSend$setAllowsActivityContinuation:
+ _objc_msgSend$setAllowsAutoCorrection:
+ _objc_msgSend$setAllowsContinuousPathKeyboard:
+ _objc_msgSend$setAllowsDictation:
+ _objc_msgSend$setAllowsPasswordAutoFill:
+ _objc_msgSend$setAllowsPredictiveKeyboard:
+ _objc_msgSend$setAllowsSmartPunctuation:
+ _objc_msgSend$setAllowsSpellCheck:
CStrings:
+ "\""
+ "<%@: %p { isEnabled = %@, mainIndividualConfiguration = %@, configurationsByApplicationDescriptor = %@, allowsAutoCorrection = %@, allowsSmartPunctuation = %@, allowsSpellCheck = %@, allowsPredictiveKeyboard = %@, allowsActivityContinuation = %@, allowsDictation = %@, allowsAccessibilitySpeech = %@, allowsPasswordAutoFill = %@, allowsContinuousPathKeyboard = %@ }>"
+ "T@\"NSString\",?,R,C"
+ "TB,N,V_allowsAccessibilitySpeech"
+ "TB,N,V_allowsActivityContinuation"
+ "TB,N,V_allowsAutoCorrection"
+ "TB,N,V_allowsContinuousPathKeyboard"
+ "TB,N,V_allowsDictation"
+ "TB,N,V_allowsKeyboardShortcuts"
+ "TB,N,V_allowsPasswordAutoFill"
+ "TB,N,V_allowsPredictiveKeyboard"
+ "TB,N,V_allowsSmartPunctuation"
+ "TB,N,V_allowsSpellCheck"
+ "_allowsAccessibilitySpeech"
+ "_allowsActivityContinuation"
+ "_allowsAutoCorrection"
+ "_allowsContinuousPathKeyboard"
+ "_allowsDictation"
+ "_allowsKeyboardShortcuts"
+ "_allowsPasswordAutoFill"
+ "_allowsPredictiveKeyboard"
+ "_allowsSmartPunctuation"
+ "_allowsSpellCheck"
+ "allowsAccessibilitySpeech"
+ "allowsActivityContinuation"
+ "allowsAutoCorrection"
+ "allowsContinuousPathKeyboard"
+ "allowsDictation"
+ "allowsKeyboardShortcuts"
+ "allowsPasswordAutoFill"
+ "allowsPredictiveKeyboard"
+ "allowsSmartPunctuation"
+ "allowsSpellCheck"
+ "setAllowsAccessibilitySpeech:"
+ "setAllowsActivityContinuation:"
+ "setAllowsAutoCorrection:"
+ "setAllowsContinuousPathKeyboard:"
+ "setAllowsDictation:"
+ "setAllowsKeyboardShortcuts:"
+ "setAllowsPasswordAutoFill:"
+ "setAllowsPredictiveKeyboard:"
+ "setAllowsSmartPunctuation:"
+ "setAllowsSpellCheck:"
- "<%@: %p { isEnabled = %@, mainIndividualConfiguration = %@, configurationsByApplicationDescriptor = %@ }>"

```
