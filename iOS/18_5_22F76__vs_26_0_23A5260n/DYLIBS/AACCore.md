## AACCore

> `/System/Library/PrivateFrameworks/AACCore.framework/AACCore`

```diff

-14.2.9.0.0
-  __TEXT.__text: 0xe3a8
+16.0.0.0.0
+  __TEXT.__text: 0xe6c4
   __TEXT.__auth_stubs: 0x580
-  __TEXT.__objc_methlist: 0x149c
+  __TEXT.__objc_methlist: 0x14e4
   __TEXT.__const: 0xd8
-  __TEXT.__cstring: 0xe46
+  __TEXT.__cstring: 0xfa6
   __TEXT.__oslogstring: 0x5c3
   __TEXT.__gcc_except_tab: 0x1b8
   __TEXT.__unwind_info: 0x548
   __TEXT.__objc_classname: 0x8ea
-  __TEXT.__objc_methname: 0x2750
+  __TEXT.__objc_methname: 0x2846
   __TEXT.__objc_methtype: 0x848
-  __TEXT.__objc_stubs: 0x1b00
+  __TEXT.__objc_stubs: 0x1bc0
   __DATA_CONST.__got: 0x1d8
-  __DATA_CONST.__const: 0x620
+  __DATA_CONST.__const: 0x628
   __DATA_CONST.__objc_classlist: 0x1b0
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0xd8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x938
+  __DATA_CONST.__objc_selrefs: 0x968
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0x110
   __AUTH_CONST.__auth_got: 0x2d0
   __AUTH_CONST.__const: 0x60
-  __AUTH_CONST.__cfstring: 0xe40
-  __AUTH_CONST.__objc_const: 0x3c18
+  __AUTH_CONST.__cfstring: 0xf40
+  __AUTH_CONST.__objc_const: 0x3ca8
   __AUTH.__objc_data: 0xd70
-  __DATA.__objc_ivar: 0x1c4
-  __DATA.__data: 0xa40
+  __DATA.__objc_ivar: 0x1d0
+  __DATA.__data: 0xa50
   __DATA.__bss: 0x20
   __DATA_DIRTY.__objc_data: 0x370
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 4384F349-BEEF-32B9-B561-98A36AF84322
-  Functions: 480
-  Symbols:   2042
-  CStrings:  879
+  UUID: E680A516-5EFF-3F42-A3A1-701F15DAEC42
+  Functions: 486
+  Symbols:   2050
+  CStrings:  907
 
Symbols:
+ -[AEAssessmentIndividualConfiguration isRequired]
+ -[AEAssessmentIndividualConfiguration setRequired:]
+ -[AEAssessmentState _allowsContentCapture]
+ -[AEAssessmentState _allowsNetworkAccess]
+ -[AEAssessmentState set_allowsContentCapture:]
+ -[AEAssessmentState set_allowsNetworkAccess:]
+ _AEAssessmentModePrivateConfigurationSPIEntitlement
+ _AECoreNotInstalledParticipantsKey
+ _AECoreRestrictedSystemParticipantsKey
+ _OBJC_IVAR_$_AEAssessmentIndividualConfiguration._required
+ _OBJC_IVAR_$_AEAssessmentState.__allowsContentCapture
+ _OBJC_IVAR_$_AEAssessmentState.__allowsNetworkAccess
+ _objc_msgSend$_allowsContentCapture
+ _objc_msgSend$_allowsNetworkAccess
+ _objc_msgSend$isRequired
+ _objc_msgSend$setRequired:
+ _objc_msgSend$set_allowsContentCapture:
+ _objc_msgSend$set_allowsNetworkAccess:
CStrings:
+ "<%@: %p { allowsNetworkAccess = %@, required = %@, configurationInfo = %@ }>"
+ "<%@: %p { isEnabled = %@, mainIndividualConfiguration = %@, configurationsByApplicationDescriptor = %@, allowsAutoCorrection = %@, allowsSmartPunctuation = %@, allowsSpellCheck = %@, allowsPredictiveKeyboard = %@, allowsActivityContinuation = %@, allowsDictation = %@, allowsAccessibilitySpeech = %@, allowsPasswordAutoFill = %@, allowsContinuousPathKeyboard = %@, allowsKeyboardShortcuts = %@, allowsKeyboardMathSolving = %@, allowsMathPaperSolving = %@, _allowsNetworkAccess = %@, _allowsContentCapture = %@}>"
+ "AENotInstalledParticipants"
+ "AERestrictedSystemParticipants"
+ "Required participants are not available on this device."
+ "TB,N,GisRequired,V_required"
+ "TB,N,V__allowsContentCapture"
+ "TB,N,V__allowsNetworkAccess"
+ "The Policy Session is not entitled to use private configuration SPI."
+ "__allowsContentCapture"
+ "__allowsNetworkAccess"
+ "_allowsContentCapture"
+ "_required"
+ "com.apple.assessmentmode.private-configuration"
+ "isRequired"
+ "required"
+ "setRequired:"
+ "set_allowsContentCapture:"
+ "set_allowsNetworkAccess:"
- "<%@: %p { allowsNetworkAccess = %@, configurationInfo = %@ }>"
- "<%@: %p { isEnabled = %@, mainIndividualConfiguration = %@, configurationsByApplicationDescriptor = %@, allowsAutoCorrection = %@, allowsSmartPunctuation = %@, allowsSpellCheck = %@, allowsPredictiveKeyboard = %@, allowsActivityContinuation = %@, allowsDictation = %@, allowsAccessibilitySpeech = %@, allowsPasswordAutoFill = %@, allowsContinuousPathKeyboard = %@, allowsKeyboardShortcuts = %@, allowsKeyboardMathSolving = %@, allowsMathPaperSolving = %@}>"

```
