## InputMethodKit

> `/System/Library/Frameworks/InputMethodKit.framework/Versions/A/InputMethodKit`

```diff

 549.200.0.0.0
-  __TEXT.__text: 0xfa9d4
+  __TEXT.__text: 0xf9f80
   __TEXT.__auth_stubs: 0xd90
-  __TEXT.__objc_methlist: 0xf734
-  __TEXT.__const: 0x988
+  __TEXT.__objc_methlist: 0x11090
+  __TEXT.__const: 0x9a8
   __TEXT.__oslogstring: 0x2faf
   __TEXT.__cstring: 0xaff6
   __TEXT.__ustring: 0x28
-  __TEXT.__gcc_except_tab: 0x3f8c
-  __TEXT.__unwind_info: 0x39c0
+  __TEXT.__gcc_except_tab: 0x3fac
+  __TEXT.__unwind_info: 0x3a20
   __TEXT.__objc_classname: 0x1cec
   __TEXT.__objc_methname: 0x1d504
   __TEXT.__objc_methtype: 0x4785

   __DATA_CONST.__objc_catlist: 0x58
   __DATA_CONST.__objc_protolist: 0x1e0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x69c8
+  __DATA_CONST.__objc_selrefs: 0x6cd0
   __DATA_CONST.__objc_protorefs: 0x68
   __DATA_CONST.__objc_superrefs: 0x4c8
   __DATA_CONST.__objc_arraydata: 0x2d0
   __AUTH_CONST.__auth_got: 0x6d8
   __AUTH_CONST.__const: 0x2050
   __AUTH_CONST.__cfstring: 0x62a0
-  __AUTH_CONST.__objc_const: 0x19758
+  __AUTH_CONST.__objc_const: 0x167d8
   __AUTH_CONST.__objc_intobj: 0x348
   __AUTH_CONST.__objc_arrayobj: 0x1b0
   __AUTH_CONST.__objc_doubleobj: 0x40

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: E7C26538-B290-3FAF-A506-A0CD98C0C684
-  Functions: 5961
-  Symbols:   12762
+  UUID: 7D401AF5-9E0B-38C7-9281-90E1BD704CA6
+  Functions: 6008
+  Symbols:   12924
   CStrings:  7887
 
Symbols:
+ +[IMKCandidateController defaultSelectionKeyTitles].cold.1
+ +[IMKCandidateController sharedCandidateController].cold.1
+ +[IMKCandidateController sharedFunctionRowCandidateController].cold.1
+ +[IMKCandidateDefinitionUnit(Drawing) sharedTextStorage].cold.1
+ +[IMKCandidateUIStringSizeCache sharedCache].cold.1
+ +[IMKDebugging isSendingDebugInformation].cold.1
+ +[IMKDoubleSpaceEventHandler sharedHandler].cold.1
+ +[IMKExtensionHostContext _extensionAuxiliaryHostProtocol].cold.1
+ +[IMKExtensionHostContext _extensionAuxiliaryVendorProtocol].cold.1
+ +[IMKExtensionIM extensionDelegate].cold.1
+ +[IMKExtensionServiceContext _extensionAuxiliaryHostProtocol].cold.1
+ +[IMKExtensionServiceContext _extensionAuxiliaryVendorProtocol].cold.1
+ +[IMKNSXPCListener listener].cold.1
+ +[IMKPerformanceTimer performanceTimerDictionary].cold.1
+ +[IMKServer allocWithZone:].cold.1
+ +[IMKServer isValidBundleIdentifier:].cold.1
+ +[IMKSimulatorController sharedController].cold.1
+ +[IMKSimulatorInputModeSelector sharedInputModeSelector].cold.1
+ +[IMKSimulatorKeyboardInterpreter sharedKeyboardInterpreter].cold.1
+ +[IMKTextDocumentTextInputAdaptor appsWithUnreliableTextInputImplementation].cold.1
+ +[IMKUICandidate sharedTextStorage].cold.1
+ +[IMKUICandidateTouchBarOnScreenBridge sharedBridge].cold.1
+ +[IMKUIInformation isAppleInternal].cold.1
+ +[IMKUIInformation sharedInformation].cold.1
+ +[IMKUIWindowBasedCandidateController defaultSelectionKeyTitles].cold.1
+ +[IMKXPCServiceInfoDictionary singleton].cold.1
+ +[NSAttributedString(IMKAdditions) dictionarySignForFontSize:UIType:].cold.1
+ +[NSAttributedString(IMKAdditions) noteMarkForFontSize:UIType:].cold.1
+ +[_IMKServerLegacy initialize].cold.1
+ +[_IMKServerLegacy privateRunLoopMode].cold.1
+ +[_IMKServerLegacy sendsTouchBarCandidatesToApp].cold.1
+ +[_IMKServerModern initialize].cold.1
+ +[_IMKServerModern privateRunLoopMode].cold.1
+ +[_IMKServerModern sendsTouchBarCandidatesToApp].cold.1
+ +[_IPMDServerClientWrapperLegacy clientWrapperWithClientDOProxy:].cold.1
+ +[_IPMDServerClientWrapperModern clientWrapperWithClientDOProxy:].cold.1
+ -[IMKTextDocument deleteCharacters:afterCursorPosition:].cold.1
+ -[_IMKServerLegacy activateServerWithReply:].cold.1
+ -[_IMKServerLegacy activateServer].cold.1
+ -[_IMKServerLegacy commitCompositionWithDiscardMarkedTextFlag:].cold.1
+ -[_IMKServerLegacy commitCompositionWithReply:].cold.1
+ -[_IMKServerLegacy deactivateServerWithReply:].cold.1
+ -[_IMKServerLegacy deactivateServer].cold.1
+ -[_IMKServerLegacy didCommandBySelector:reply:].cold.1
+ -[_IMKServerLegacy doCommandBySelector:commandDictionary:].cold.1
+ -[_IMKServerLegacy doCommandBySelector:commandDictionary:reply:].cold.1
+ -[_IMKServerLegacy handleEvent:characterIndex:edge:asyncClient:reply:].cold.1
+ -[_IMKServerLegacy hidePalettes].cold.1
+ -[_IMKServerLegacy invalidateClientGeometry].cold.1
+ -[_IMKServerLegacy ironwoodPlaceholderWasInvalidated:].cold.1
+ -[_IMKServerLegacy ironwoodTextWasCorrected:].cold.1
+ -[_IMKServerLegacy menusDictionaryWithClientAsync:reply:].cold.1
+ -[_IMKServerLegacy modesWithClientAsync:reply:].cold.1
+ -[_IMKServerLegacy recognizedEventsWithClientAsync:reply:].cold.1
+ -[_IMKServerLegacy sendInputSessionSessAction:].cold.1
+ -[_IMKServerLegacy sendInputSessionSessAction:timestamp:withInfo:].cold.1
+ -[_IMKServerLegacy sessionFinished].cold.1
+ -[_IMKServerLegacy setValue:forTag:].cold.1
+ -[_IMKServerLegacy setValue:forTag:reply:].cold.1
+ -[_IMKServerLegacy valueForTag:asyncClient:reply:].cold.1
+ -[_IMKServerLegacy viewServiceEndpointWithClientAsync:reply:].cold.1
+ -[_IMKServerModern activateServerWithReply:].cold.1
+ -[_IMKServerModern activateServer].cold.1
+ -[_IMKServerModern commitCompositionWithDiscardMarkedTextFlag:].cold.1
+ -[_IMKServerModern commitCompositionWithReply:].cold.1
+ -[_IMKServerModern deactivateServerWithReply:].cold.1
+ -[_IMKServerModern deactivateServer].cold.1
+ -[_IMKServerModern didCommandBySelector:reply:].cold.1
+ -[_IMKServerModern doCommandBySelector:commandDictionary:].cold.1
+ -[_IMKServerModern doCommandBySelector:commandDictionary:reply:].cold.1
+ -[_IMKServerModern handleEvent:characterIndex:edge:asyncClient:reply:].cold.1
+ -[_IMKServerModern hidePalettes].cold.1
+ -[_IMKServerModern invalidateClientGeometry].cold.1
+ -[_IMKServerModern ironwoodPlaceholderWasInvalidated:].cold.1
+ -[_IMKServerModern ironwoodTextWasCorrected:].cold.1
+ -[_IMKServerModern menusDictionaryWithClientAsync:reply:].cold.1
+ -[_IMKServerModern modesWithClientAsync:reply:].cold.1
+ -[_IMKServerModern recognizedEventsWithClientAsync:reply:].cold.1
+ -[_IMKServerModern sendInputSessionSessAction:].cold.1
+ -[_IMKServerModern sendInputSessionSessAction:timestamp:withInfo:].cold.1
+ -[_IMKServerModern sessionFinished].cold.1
+ -[_IMKServerModern setValue:forTag:].cold.1
+ -[_IMKServerModern setValue:forTag:reply:].cold.1
+ -[_IMKServerModern valueForTag:asyncClient:reply:].cold.1
+ -[_IMKServerModern viewServiceEndpointWithClientAsync:reply:].cold.1
+ -[_IMKServerXPCInvocationLegacy dealloc].cold.1
+ -[_IMKServerXPCInvocationLegacy dealloc].cold.2
+ -[_IMKServerXPCInvocationLegacy invocationAwaitXPCReply].cold.1
+ -[_IMKServerXPCInvocationLegacy invocationAwaitXPCReply].cold.2
+ -[_IMKServerXPCInvocationLegacy invocationAwaitXPCReply].cold.3
+ -[_IMKServerXPCInvocationLegacy invocationAwaitXPCReply].cold.4
+ -[_IMKServerXPCInvocationLegacy invocationAwaitXPCReply].cold.5
+ -[_IMKServerXPCInvocationLegacy invocationAwaitXPCReply].cold.6
+ -[_IMKServerXPCInvocationLegacy invocationInterruptXPCReply].cold.1
+ -[_IMKServerXPCInvocationModern initWithClientWrapper:selector:].cold.1
+ -[_IPMDServerClientWrapperLegacy attributesForCharacterIndex_Cache:].cold.1
+ -[_IPMDServerClientWrapperLegacy bundleIdentifier_Cache].cold.1
+ -[_IPMDServerClientWrapperLegacy invalidateAttributesCacheForAllIndex:].cold.1
+ -[_IPMDServerClientWrapperLegacy setAttributes_Cache:forIndex:].cold.1
+ -[_IPMDServerClientWrapperLegacy setBundleIdentifier_Cache:].cold.1
+ -[_IPMDServerClientWrapperLegacy setMarkedText:selectionRange:replacementRange:].cold.1
+ -[_IPMDServerClientWrapperLegacy setTouchBarAvailableFrame:].cold.1
+ -[_IPMDServerClientWrapperLegacy setViewEffectiveAppearance_Cache:].cold.1
+ -[_IPMDServerClientWrapperLegacy setWindowLevel_Cache:].cold.1
+ -[_IPMDServerClientWrapperLegacy touchBarAvailableFrame].cold.1
+ -[_IPMDServerClientWrapperLegacy touchBarTotalWidth].cold.1
+ -[_IPMDServerClientWrapperLegacy viewEffectiveAppearance_Cache].cold.1
+ -[_IPMDServerClientWrapperLegacy windowLevel_Cache].cold.1
+ -[_IPMDServerClientWrapperLegacy wouldHandleEvent:].cold.1
+ -[_IPMDServerClientWrapperModern attributesForCharacterIndex_Cache:].cold.1
+ -[_IPMDServerClientWrapperModern bundleIdentifier_Cache].cold.1
+ -[_IPMDServerClientWrapperModern invalidateAttributesCacheForAllIndex:].cold.1
+ -[_IPMDServerClientWrapperModern setAttributes_Cache:forIndex:].cold.1
+ -[_IPMDServerClientWrapperModern setBundleIdentifier_Cache:].cold.1
+ -[_IPMDServerClientWrapperModern setMarkedText:selectionRange:replacementRange:].cold.1
+ -[_IPMDServerClientWrapperModern setTouchBarAvailableFrame:].cold.1
+ -[_IPMDServerClientWrapperModern setViewEffectiveAppearance_Cache:].cold.1
+ -[_IPMDServerClientWrapperModern setWindowLevel_Cache:].cold.1
+ -[_IPMDServerClientWrapperModern touchBarAvailableFrame].cold.1
+ -[_IPMDServerClientWrapperModern touchBarTotalWidth].cold.1
+ -[_IPMDServerClientWrapperModern viewEffectiveAppearance_Cache].cold.1
+ -[_IPMDServerClientWrapperModern windowLevel_Cache].cold.1
+ -[_IPMDServerClientWrapperModern wouldHandleEvent:].cold.1
+ GCC_except_table554
+ GCC_except_table583
+ IMKRunLoopPerformBlockReliable.cold.1
+ IMKRunLoopPerformBlockReliable.cold.2
+ IMKRunLoopWakeUpReliable.cold.2
+ IMKServerRunLoopModern.cold.1
+ IMKXPCPerformBlockOnMainThread.cold.1
+ IMKXPCPerformBlockOnMainThread.cold.2
+ IMKXPCRequestRunLoopModes.cold.1
+ __21+[IMKServer subclass]_block_invoke.cold.1
+ __51-[_IPMDServerClientWrapperLegacy windowLevel_Cache]_block_invoke.cold.1
+ __51-[_IPMDServerClientWrapperModern windowLevel_Cache]_block_invoke.cold.1
+ __56-[_IMKServerXPCInvocationLegacy invocationAwaitXPCReply]_block_invoke.91.cold.1
+ __56-[_IMKServerXPCInvocationLegacy invocationAwaitXPCReply]_block_invoke.91.cold.2
+ __56-[_IPMDServerClientWrapperLegacy bundleIdentifier_Cache]_block_invoke.cold.1
+ __56-[_IPMDServerClientWrapperModern bundleIdentifier_Cache]_block_invoke.cold.1
+ __63-[_IPMDServerClientWrapperLegacy viewEffectiveAppearance_Cache]_block_invoke.cold.1
+ __63-[_IPMDServerClientWrapperModern viewEffectiveAppearance_Cache]_block_invoke.cold.1
+ __68-[_IPMDServerClientWrapperLegacy attributesForCharacterIndex_Cache:]_block_invoke.cold.1
+ __68-[_IPMDServerClientWrapperModern attributesForCharacterIndex_Cache:]_block_invoke.cold.1
+ __IMKRunLoopWakeUpReliable_block_invoke.cold.2
+ __IMKServerRunLoopModern_block_invoke.cold.1
+ __IMKServerRunLoopModern_block_invoke.cold.2
+ __IMKXPCPerformBlockOnMainThread_block_invoke.cold.1
+ __MergedGlobals
+ adaptor_log.cold.1
+ candidate_log.cold.1
+ candidate_ui_log.cold.1
+ document_log.cold.1
+ input_controller_log.cold.1
+ input_log.cold.1
+ inputmethod_log.cold.1
+ perf_log.cold.1
+ server_log.cold.1
+ text_log.cold.1
+ textinput_log.cold.1
+ touchbar_log.cold.1
- -[_IPMDServerClientWrapperLegacy presentFunctionRowItemTextInputView].cold.1
- -[_IPMDServerClientWrapperLegacy presentFunctionRowItemTextInputView].cold.2
- -[_IPMDServerClientWrapperModern presentFunctionRowItemTextInputView].cold.1
- -[_IPMDServerClientWrapperModern presentFunctionRowItemTextInputView].cold.2
- _OUTLINED_FUNCTION_14
- _OUTLINED_FUNCTION_15
- _OUTLINED_FUNCTION_16

```
