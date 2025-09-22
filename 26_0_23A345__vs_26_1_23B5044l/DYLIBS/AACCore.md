## AACCore

> `/System/Library/PrivateFrameworks/AACCore.framework/AACCore`

```diff

-19.0.0.0.0
-  __TEXT.__text: 0xe7c8
+23.0.0.0.0
+  __TEXT.__text: 0xef60
   __TEXT.__auth_stubs: 0x580
-  __TEXT.__objc_methlist: 0x150c
+  __TEXT.__objc_methlist: 0x15ac
   __TEXT.__const: 0xd8
-  __TEXT.__cstring: 0x1009
+  __TEXT.__cstring: 0x1066
   __TEXT.__oslogstring: 0x5c3
   __TEXT.__gcc_except_tab: 0x1b8
-  __TEXT.__unwind_info: 0x548
-  __TEXT.__objc_classname: 0x8ea
-  __TEXT.__objc_methname: 0x28f3
-  __TEXT.__objc_methtype: 0x848
-  __TEXT.__objc_stubs: 0x1c00
+  __TEXT.__unwind_info: 0x578
+  __TEXT.__objc_classname: 0x90b
+  __TEXT.__objc_methname: 0x2aa9
+  __TEXT.__objc_methtype: 0x85d
+  __TEXT.__objc_stubs: 0x1ce0
   __DATA_CONST.__got: 0x1d8
   __DATA_CONST.__const: 0x628
-  __DATA_CONST.__objc_classlist: 0x1b0
+  __DATA_CONST.__objc_classlist: 0x1b8
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0xd8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x980
+  __DATA_CONST.__objc_selrefs: 0x9c8
   __DATA_CONST.__objc_protorefs: 0x30
-  __DATA_CONST.__objc_superrefs: 0x110
+  __DATA_CONST.__objc_superrefs: 0x118
   __AUTH_CONST.__auth_got: 0x2d0
   __AUTH_CONST.__const: 0x60
-  __AUTH_CONST.__cfstring: 0xf80
-  __AUTH_CONST.__objc_const: 0x3ce8
-  __AUTH.__objc_data: 0xd70
-  __DATA.__objc_ivar: 0x1d4
+  __AUTH_CONST.__cfstring: 0x1000
+  __AUTH_CONST.__objc_const: 0x3e60
+  __AUTH.__objc_data: 0xdc0
+  __DATA.__objc_ivar: 0x1e4
   __DATA.__data: 0xa50
   __DATA.__bss: 0x20
   __DATA_DIRTY.__objc_data: 0x370

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: D3FCAC28-A6A2-34C7-B959-0DDA8F524EBD
-  Functions: 489
-  Symbols:   2059
-  CStrings:  916
+  UUID: A868020F-8372-3849-8F98-1622A1F9D1C1
+  Functions: 509
+  Symbols:   2118
+  CStrings:  939
 
Symbols:
+ -[AEAssessmentState allowsScreenshots]
+ -[AEAssessmentState setAllowsScreenshots:]
+ -[AECompositeAssessmentStateReader .cxx_destruct]
+ -[AECompositeAssessmentStateReader dealloc]
+ -[AECompositeAssessmentStateReader initWithFileBackedReader:accessibilityServerReader:]
+ -[AECompositeAssessmentStateReader isActive]
+ -[AECompositeAssessmentStateReader observeValueForKeyPath:ofObject:change:context:]
+ -[AECompositeAssessmentStateReader setActive:]
+ -[AELifecycleEventHandlingProxy _handleEventWantsStartWindowContentCaptureWithCompletion:]
+ -[AELifecycleEventHandlingProxy _handleEventWantsStopWindowContentCaptureWithCompletion:]
+ -[AELifecycleEventHandlingProxy handleEventWantsStartWindowContentCaptureWithCompletion:]
+ -[AELifecycleEventHandlingProxy handleEventWantsStopWindowContentCaptureWithCompletion:]
+ -[AEPreferences disableSystemHotKeys]
+ _OBJC_CLASS_$_AECompositeAssessmentStateReader
+ _OBJC_IVAR_$_AEAssessmentState._allowsScreenshots
+ _OBJC_IVAR_$_AECompositeAssessmentStateReader._accessibilityServerReader
+ _OBJC_IVAR_$_AECompositeAssessmentStateReader._active
+ _OBJC_IVAR_$_AECompositeAssessmentStateReader._fileBackedReader
+ _OBJC_METACLASS_$_AECompositeAssessmentStateReader
+ _OUTLINED_FUNCTION_7
+ __OBJC_$_INSTANCE_METHODS_AECompositeAssessmentStateReader
+ __OBJC_$_INSTANCE_VARIABLES_AECompositeAssessmentStateReader
+ __OBJC_$_PROP_LIST_AECompositeAssessmentStateReader
+ __OBJC_CLASS_PROTOCOLS_$_AECompositeAssessmentStateReader
+ __OBJC_CLASS_RO_$_AECompositeAssessmentStateReader
+ __OBJC_METACLASS_RO_$_AECompositeAssessmentStateReader
+ ___88-[AELifecycleEventHandlingProxy handleEventWantsStopWindowContentCaptureWithCompletion:]_block_invoke
+ ___88-[AELifecycleEventHandlingProxy handleEventWantsStopWindowContentCaptureWithCompletion:]_block_invoke_2
+ ___89-[AELifecycleEventHandlingProxy _handleEventWantsStopWindowContentCaptureWithCompletion:]_block_invoke
+ ___89-[AELifecycleEventHandlingProxy handleEventWantsStartWindowContentCaptureWithCompletion:]_block_invoke
+ ___89-[AELifecycleEventHandlingProxy handleEventWantsStartWindowContentCaptureWithCompletion:]_block_invoke_2
+ ___90-[AELifecycleEventHandlingProxy _handleEventWantsStartWindowContentCaptureWithCompletion:]_block_invoke
+ _objc_msgSend$addObserver:forKeyPath:options:context:
+ _objc_msgSend$allowsScreenshots
+ _objc_msgSend$handleEventWantsStartWindowContentCaptureWithCompletion:
+ _objc_msgSend$handleEventWantsStopWindowContentCaptureWithCompletion:
+ _objc_msgSend$initWithFileBackedReader:accessibilityServerReader:
+ _objc_msgSend$removeObserver:forKeyPath:context:
+ _objc_msgSend$setAllowsScreenshots:
CStrings:
+ "2"
+ "<%@: %p { isEnabled = %@, mainIndividualConfiguration = %@, configurationsByApplicationDescriptor = %@, allowsAutoCorrection = %@, allowsSmartPunctuation = %@, allowsSpellCheck = %@, allowsPredictiveKeyboard = %@, allowsActivityContinuation = %@, allowsDictation = %@, allowsAccessibilitySpeech = %@, allowsAccessibilityTypingFeedback = %@, allowsPasswordAutoFill = %@, allowsContinuousPathKeyboard = %@, allowsKeyboardShortcuts = %@, allowsKeyboardMathSolving = %@, allowsMathPaperSolving = %@, allowsScreenshots = %@, _allowsNetworkAccess = %@, _allowsContentCapture = %@}>"
+ "AECompositeAssessmentStateReader"
+ "CompositeReaderContext"
+ "DisableSystemHotKeys"
+ "TB,N,V_allowsScreenshots"
+ "_accessibilityServerReader"
+ "_allowsScreenshots"
+ "_fileBackedReader"
+ "addObserver:forKeyPath:options:context:"
+ "allowsScreenshots"
+ "disableSystemHotKeys"
+ "handleEventWantsStartWindowContentCaptureWithCompletion:"
+ "handleEventWantsStopWindowContentCaptureWithCompletion:"
+ "initWithFileBackedReader:accessibilityServerReader:"
+ "observeValueForKeyPath:ofObject:change:context:"
+ "removeObserver:forKeyPath:context:"
+ "setAllowsScreenshots:"
+ "v48@0:8@16@24@32^v40"
- "\""
- "<%@: %p { isEnabled = %@, mainIndividualConfiguration = %@, configurationsByApplicationDescriptor = %@, allowsAutoCorrection = %@, allowsSmartPunctuation = %@, allowsSpellCheck = %@, allowsPredictiveKeyboard = %@, allowsActivityContinuation = %@, allowsDictation = %@, allowsAccessibilitySpeech = %@, allowsAccessibilityTypingFeedback = %@, allowsPasswordAutoFill = %@, allowsContinuousPathKeyboard = %@, allowsKeyboardShortcuts = %@, allowsKeyboardMathSolving = %@, allowsMathPaperSolving = %@, _allowsNetworkAccess = %@, _allowsContentCapture = %@}>"

```
