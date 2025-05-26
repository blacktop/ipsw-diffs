## AutoFillUI

> `/System/Library/PrivateFrameworks/AutoFillUI.framework/AutoFillUI`

```diff

-56.150.1.1.0
-  __TEXT.__text: 0x1b05c
-  __TEXT.__auth_stubs: 0x5e0
-  __TEXT.__objc_methlist: 0x16d4
+56.210.1.0.0
+  __TEXT.__text: 0x1c3dc
+  __TEXT.__auth_stubs: 0x640
+  __TEXT.__objc_methlist: 0x17ac
   __TEXT.__const: 0xd8
-  __TEXT.__cstring: 0x155f
-  __TEXT.__gcc_except_tab: 0x4a0
+  __TEXT.__cstring: 0x1684
+  __TEXT.__gcc_except_tab: 0x4f8
   __TEXT.__ustring: 0xb0
   __TEXT.__dlopen_cstrs: 0x104
   __TEXT.__oslogstring: 0x3
-  __TEXT.__unwind_info: 0x750
-  __TEXT.__objc_classname: 0x429
-  __TEXT.__objc_methname: 0x698e
-  __TEXT.__objc_methtype: 0x19ab
-  __TEXT.__objc_stubs: 0x4f40
-  __DATA_CONST.__got: 0x238
-  __DATA_CONST.__const: 0x8c8
+  __TEXT.__unwind_info: 0x7b0
+  __TEXT.__objc_classname: 0x42c
+  __TEXT.__objc_methname: 0x6f5a
+  __TEXT.__objc_methtype: 0x1aaf
+  __TEXT.__objc_stubs: 0x5420
+  __DATA_CONST.__got: 0x258
+  __DATA_CONST.__const: 0x8a0
   __DATA_CONST.__objc_classlist: 0xb8
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x98
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x55b0
-  __DATA_CONST.__objc_selrefs: 0x1678
+  __DATA_CONST.__objc_const: 0x52b0
+  __DATA_CONST.__objc_selrefs: 0x17e8
   __DATA_CONST.__objc_arraydata: 0xc8
-  __AUTH_CONST.__cfstring: 0x1440
-  __AUTH_CONST.__objc_const: 0x970
-  __AUTH_CONST.__const: 0x3c0
+  __AUTH_CONST.__cfstring: 0x1460
+  __AUTH_CONST.__objc_const: 0x9b8
+  __AUTH_CONST.__const: 0x3e0
   __AUTH_CONST.__objc_arrayobj: 0x90
   __AUTH_CONST.__objc_intobj: 0x18
-  __AUTH_CONST.__auth_got: 0x300
+  __AUTH_CONST.__auth_got: 0x330
   __AUTH.__objc_data: 0x550
   __DATA.__objc_protorefs: 0x10
-  __DATA.__objc_classrefs: 0x298
+  __DATA.__objc_classrefs: 0x2c0
   __DATA.__objc_superrefs: 0x88
-  __DATA.__objc_ivar: 0x1c0
+  __DATA.__objc_ivar: 0x1cc
   __DATA.__data: 0x768
-  __DATA.__bss: 0xe0
+  __DATA.__bss: 0xf0
   __DATA_DIRTY.__objc_data: 0x1e0
   __DATA_DIRTY.__bss: 0xe0
   - /System/Library/Frameworks/Contacts.framework/Contacts

   - /System/Library/PrivateFrameworks/AutoFillCore.framework/AutoFillCore
   - /System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices
   - /System/Library/PrivateFrameworks/BoardServices.framework/BoardServices
+  - /System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices
   - /System/Library/PrivateFrameworks/RemoteTextInput.framework/RemoteTextInput
   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking

   - /System/Library/PrivateFrameworks/WebKitLegacy.framework/WebKitLegacy
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 674
-  Symbols:   2855
-  CStrings:  1501
+  Functions: 696
+  Symbols:   2951
+  CStrings:  1570
 
Symbols:
+ +[AFUIAutoFillCreditCardController dateStringTextContentType:date:placeholderHint:]
+ +[_AFUIQueuedOperations queuedOperationsWithSecureAppID:processID:textOperations:completionHandler:]
+ -[AFUIAutoFillPasswordController presentingViewController]
+ -[AFUIAutoFillPasswordController setPresentingViewController:]
+ -[AFUIAutoFillPopoverController _displayContextMenuForSourceRect:caretRect:]
+ -[AFUIAutoFillPopoverController _displayContextMenuWhenReady]
+ -[AFUIAutoFillPopoverController _displayContextMenu]
+ -[AFUIAutoFillPopoverController _sourceRectInApplicationCoordinates]
+ -[AFUIAutoFillPopoverController _translatedRectFromApplication:]
+ -[AFUIAutoFillPopoverController setWillPresentMenu:]
+ -[AFUIAutoFillPopoverController willPresentMenu]
+ -[AFUIAutofillContactsController _meAction]
+ -[AFUIContactsController _meContactInfosForTextContentType:meContact:]
+ -[AFUIExplicitAutoFillController authenticationDidEndForSessionUUID:completion:]
+ -[AFUIExplicitAutoFillController authenticationWillBeginForSessionUUID:completion:]
+ -[AFUIPanel _monitorDocumentProcessVisibility:]
+ -[AFUIPanel authenticationDidEndForSessionUUID:completion:]
+ -[AFUIPanel authenticationWillBeginForSessionUUID:completion:]
+ -[AFUIPanel contactsUIDidEndForSessionUUID:completion:]
+ -[AFUIPanel contactsUIWillBeginForSessionUUID:completion:]
+ -[AFUIPanel dismissMenu]
+ -[AFUIPanel initWithDocumentPid:sessionUUID:]
+ -[AFUIPanel passwordsUIDidEndForSessionUUID:completion:]
+ -[AFUIPanel processMonitor]
+ -[AFUIPanel sessionUUID]
+ -[AFUIPanel setIsMenuPresented:forSessionUUID:]
+ -[AFUIPanel setProcessMonitor:]
+ -[AFUIPanel setSessionUUID:]
+ -[AFUIServiceDelegate _performBlockOnInternalQueueForUUID:block:]
+ -[AFUIServiceDelegate _queueTextOperations:forSecureAppID:processID:completionHandler:]
+ -[AFUIServiceDelegate _queueTextOperations:forSecureAppID:processID:completionHandler:].cold.1
+ -[AFUIServiceDelegate _queueTextOperations:forSecureAppID:processID:completionHandler:].cold.2
+ -[AFUIServiceDelegate _sendAuthenticationStateOperation:sessionUUID:completion:]
+ -[AFUIServiceDelegate _sendTextOperations:toSession:completionHandler:]
+ -[AFUIServiceDelegate _sendTextOperations:toSession:completionHandler:].cold.1
+ -[AFUIServiceDelegate _sessionForUUID:]
+ -[AFUIServiceDelegate _setIsMenuPresented:forSessionUUID:]
+ -[AFUIServiceDelegate _setupPanelForSessionUUID:documentPid:]
+ -[AFUIServiceDelegate authenticatingForDocumentTraits]
+ -[AFUIServiceDelegate authenticatingForSessionId]
+ -[AFUIServiceDelegate authenticationDidEndForSessionUUID:completion:]
+ -[AFUIServiceDelegate authenticationDidEndForSessionUUID:completion:].cold.1
+ -[AFUIServiceDelegate authenticationWillBeginForSessionUUID:completion:]
+ -[AFUIServiceDelegate authenticationWillBeginForSessionUUID:completion:].cold.1
+ -[AFUIServiceDelegate contactsUIDidEndForSessionUUID:completion:]
+ -[AFUIServiceDelegate contactsUIWillBeginForSessionUUID:completion:]
+ -[AFUIServiceDelegate currentSessions]
+ -[AFUIServiceDelegate inputSystemService:inputSessionDidPause:withReason:].cold.1
+ -[AFUIServiceDelegate inputSystemService:inputSessionDidUnpause:withReason:].cold.1
+ -[AFUIServiceDelegate passwordsUIDidEndForSessionUUID:completion:]
+ -[AFUIServiceDelegate setAuthenticatingForDocumentTraits:]
+ -[AFUIServiceDelegate setAuthenticatingForSessionId:]
+ -[AFUIServiceDelegate setCurrentSessions:]
+ -[AFUIServiceDelegate setIsMenuPresented:forSessionUUID:]
+ -[_AFUIQueuedOperations completionHandler]
+ -[_AFUIQueuedOperations initWithSecureAppID:processID:textOperations:completionHandler:]
+ GCC_except_table10
+ GCC_except_table16
+ GCC_except_table25
+ GCC_except_table26
+ _AFTextContentTypeIsInBirthdaySet
+ _AFTextContentTypeIsInJobSet
+ _AFUIAutoFillPopoverControllerOSLogFacility
+ _AFUIAutoFillPopoverControllerOSLogFacility.logFacility
+ _AFUIAutoFillPopoverControllerOSLogFacility.onceToken
+ _BKSHIDServicesGetCALayerTransform
+ _CALayerGetRenderId
+ _CATransform3DIdentity
+ _CATransform3DInvert
+ _CA_CGRectApplyTransform
+ _CGRectContainsRect
+ _CNLabelURLAddressHomePage
+ _FBSSceneVisibilityEndowmentNamespace
+ _NSCalendarIdentifierGregorian
+ _OBJC_CLASS_$_RBSProcessIdentifier
+ _OBJC_CLASS_$_RBSProcessMonitor
+ _OBJC_CLASS_$_RBSProcessPredicate
+ _OBJC_CLASS_$_RBSProcessStateDescriptor
+ _OBJC_CLASS_$_UIPeripheralHost
+ _OBJC_IVAR_$_AFUIAutoFillPopoverController._willPresentMenu
+ _OBJC_IVAR_$_AFUIPanel._processMonitor
+ _OBJC_IVAR_$_AFUIPanel._sessionUUID
+ _OBJC_IVAR_$_AFUIServiceDelegate._authenticatingForDocumentTraits
+ _OBJC_IVAR_$_AFUIServiceDelegate._authenticatingForSessionId
+ _OBJC_IVAR_$_AFUIServiceDelegate._currentSessions
+ _OBJC_IVAR_$__AFUIQueuedOperations._completionHandler
+ _UIPointIsDiscrete
+ __OBJC_$_CLASS_METHODS_AFUIAutoFillCreditCardController
+ ___43-[AFUIAutofillContactsController _meAction]_block_invoke
+ ___47-[AFUIPanel _monitorDocumentProcessVisibility:]_block_invoke
+ ___47-[AFUIPanel _monitorDocumentProcessVisibility:]_block_invoke_2
+ ___47-[AFUIPanel _monitorDocumentProcessVisibility:]_block_invoke_3
+ ___54-[AFUIServiceDelegate _displayPanelForSession:traits:]_block_invoke_5
+ ___57-[AFUIServiceDelegate setIsMenuPresented:forSessionUUID:]_block_invoke
+ ___61-[AFUIAutoFillPopoverController _displayContextMenuWhenReady]_block_invoke
+ ___68-[AFUIServiceDelegate _checkAndSendQueuedTextOperationsIfNecessary:]_block_invoke
+ ___68-[AFUIServiceDelegate _checkAndSendQueuedTextOperationsIfNecessary:]_block_invoke.cold.1
+ ___70-[AFUIContactsController _meContactInfosForTextContentType:meContact:]_block_invoke
+ ___71-[AFUIServiceDelegate _sendTextOperations:toSession:completionHandler:]_block_invoke
+ ___77-[AFUIServiceDelegate inputSystemService:inputSession:performInputOperation:]_block_invoke
+ ___80-[AFUIServiceDelegate _sendAuthenticationStateOperation:sessionUUID:completion:]_block_invoke
+ ___80-[AFUIServiceDelegate _sendAuthenticationStateOperation:sessionUUID:completion:]_block_invoke_2
+ ___80-[AFUIServiceDelegate _sendAuthenticationStateOperation:sessionUUID:completion:]_block_invoke_3
+ ___AFUIAutoFillPopoverControllerOSLogFacility_block_invoke
+ ___block_descriptor_32_e26_v32?0"AFUIPanel"8Q16^B24l
+ ___block_descriptor_40_e8_32w_e74_v32?0"RBSProcessMonitor"8"RBSProcessHandle"16"RBSProcessStateUpdate"24lw32l8
+ ___block_descriptor_44_e8_32w_e40_v16?0"<RBSProcessMonitorConfiguring>"8lw32l8
+ ___block_literal_global.289
+ ___block_literal_global.298
+ ___block_literal_global.7
+ __meContactInfosForTextContentType:meContact:.onceToken
+ __meContactInfosForTextContentType:meContact:.preferredLabelOrder
+ _objc_msgSend$_contextId
+ _objc_msgSend$_displayContextMenu
+ _objc_msgSend$_displayContextMenuForSourceRect:caretRect:
+ _objc_msgSend$_displayContextMenuWhenReady
+ _objc_msgSend$_meAction
+ _objc_msgSend$_meContactInfosForTextContentType:meContact:
+ _objc_msgSend$_monitorDocumentProcessVisibility:
+ _objc_msgSend$_performBlockOnInternalQueueForUUID:block:
+ _objc_msgSend$_queueTextOperations:forSecureAppID:processID:completionHandler:
+ _objc_msgSend$_sendAuthenticationStateOperation:sessionUUID:completion:
+ _objc_msgSend$_sendTextOperations:toSession:completionHandler:
+ _objc_msgSend$_sessionForUUID:
+ _objc_msgSend$_setIsMenuPresented:forSessionUUID:
+ _objc_msgSend$_setupPanelForSessionUUID:documentPid:
+ _objc_msgSend$_sourceRectInApplicationCoordinates
+ _objc_msgSend$_translatedRectFromApplication:
+ _objc_msgSend$authenticatingForDocumentTraits
+ _objc_msgSend$authenticatingForSessionId
+ _objc_msgSend$authenticationDidEndForSessionUUID:completion:
+ _objc_msgSend$authenticationWillBeginForSessionUUID:completion:
+ _objc_msgSend$completionHandler
+ _objc_msgSend$contactsUIDidEndForSessionUUID:completion:
+ _objc_msgSend$contactsUIWillBeginForSessionUUID:completion:
+ _objc_msgSend$convertRect:fromView:
+ _objc_msgSend$currentSessions
+ _objc_msgSend$descriptor
+ _objc_msgSend$endowmentNamespaces
+ _objc_msgSend$flushOperations
+ _objc_msgSend$identifierWithPid:
+ _objc_msgSend$initWithCalendarIdentifier:
+ _objc_msgSend$initWithDocumentPid:sessionUUID:
+ _objc_msgSend$initWithSecureAppID:processID:textOperations:completionHandler:
+ _objc_msgSend$isExplicitAutoFillInvocation
+ _objc_msgSend$layerID
+ _objc_msgSend$monitorWithConfiguration:
+ _objc_msgSend$passwordsUIDidEndForSessionUUID:completion:
+ _objc_msgSend$predicateMatchingIdentifier:
+ _objc_msgSend$queuedOperationsWithSecureAppID:processID:textOperations:completionHandler:
+ _objc_msgSend$screen
+ _objc_msgSend$scrolling
+ _objc_msgSend$sessionUUID
+ _objc_msgSend$setAuthenticatingForDocumentTraits:
+ _objc_msgSend$setAuthenticatingForSessionId:
+ _objc_msgSend$setContainerView:
+ _objc_msgSend$setEndowmentNamespaces:
+ _objc_msgSend$setIsAutoFillTextOperation:
+ _objc_msgSend$setIsExplicitAutoFillInvocation:
+ _objc_msgSend$setIsMenuPresented:forSessionUUID:
+ _objc_msgSend$setPredicates:
+ _objc_msgSend$setServiceClass:
+ _objc_msgSend$setStateDescriptor:
+ _objc_msgSend$setUpdateHandler:
+ _objc_msgSend$setValues:
+ _objc_msgSend$setWillPresentMenu:
+ _objc_msgSend$visiblePeripheralFrame
+ _objc_msgSend$willPresentMenu
+ _objc_retain_x5
- +[_AFUIQueuedOperations queuedOperationsWithSecureAppID:processID:textOperations:]
- -[AFUIAutoFillCreditCardController dateStringTextContentType:date:placeholderHint:]
- -[AFUIAutofillContactsController _meActiom]
- -[AFUIExplicitAutoFillController authenticationDidEndWithCompletion:]
- -[AFUIExplicitAutoFillController authenticationWillBeginWithCompletion:]
- -[AFUIPanel authenticationDidEndWithCompletion:]
- -[AFUIPanel authenticationWillBeginWithCompletion:]
- -[AFUIPanel contactsUIDidEndWithCompletion:]
- -[AFUIPanel contactsUIWillBeginWithCompletion:]
- -[AFUIPanel init]
- -[AFUIPanel passwordsUIDidEndWithCompletion:]
- -[AFUIServiceDelegate _queueTextOperations:forSecureAppID:processID:]
- -[AFUIServiceDelegate _queueTextOperations:forSecureAppID:processID:].cold.1
- -[AFUIServiceDelegate _queueTextOperations:forSecureAppID:processID:].cold.2
- -[AFUIServiceDelegate _queuedTextOperationsForSecureAppID:processID:]
- -[AFUIServiceDelegate _sendAuthenticationStateOperation:completion:]
- -[AFUIServiceDelegate _sendTextOperations:toSession:]
- -[AFUIServiceDelegate _sendTextOperations:toSession:].cold.1
- -[AFUIServiceDelegate _setupPanelForSessionUUID:]
- -[AFUIServiceDelegate authenticationDidEndWithCompletion:]
- -[AFUIServiceDelegate authenticationWillBeginWithCompletion:]
- -[AFUIServiceDelegate contactsUIDidEndWithCompletion:]
- -[AFUIServiceDelegate contactsUIWillBeginWithCompletion:]
- -[AFUIServiceDelegate currentSessionQueue]
- -[AFUIServiceDelegate currentSession]
- -[AFUIServiceDelegate inputSystemService:inputSessionDidDie:].cold.2
- -[AFUIServiceDelegate inputSystemService:inputSessionDidEnd:options:].cold.4
- -[AFUIServiceDelegate passwordsUIDidEndWithCompletion:]
- -[AFUIServiceDelegate setCurrentSession:]
- -[AFUIServiceDelegate setCurrentSessionQueue:]
- -[AFUIServiceSession authenticationDidEndWithCompletion:]
- -[AFUIServiceSession authenticationWillBeginWithCompletion:]
- -[AFUIServiceSession contactsUIDidEndWithCompletion:]
- -[AFUIServiceSession contactsUIWillBeginWithCompletion:]
- -[AFUIServiceSession passwordsUIDidEndWithCompletion:]
- -[_AFUIQueuedOperations initWithSecureAppID:processID:textOperations:]
- GCC_except_table12
- GCC_except_table20
- GCC_except_table21
- _OBJC_IVAR_$_AFUIServiceDelegate._currentSession
- _OBJC_IVAR_$_AFUIServiceDelegate._currentSessionQueue
- _OBJC_IVAR_$_AFUIServiceDelegate._sessionIDBeforeAuthentication
- _OBJC_IVAR_$_AFUIServiceDelegate._sessionIDBeforeContactsUI
- ___43-[AFUIAutofillContactsController _meActiom]_block_invoke
- ___53-[AFUIServiceDelegate _sendTextOperations:toSession:]_block_invoke
- ___53-[AFUIServiceDelegate _sendTextOperations:toSession:]_block_invoke_2
- ___54-[AFUIServiceDelegate contactsUIDidEndWithCompletion:]_block_invoke
- ___54-[AFUIServiceDelegate contactsUIDidEndWithCompletion:]_block_invoke.cold.1
- ___55-[AFUIServiceDelegate passwordsUIDidEndWithCompletion:]_block_invoke
- ___57-[AFUIServiceDelegate contactsUIWillBeginWithCompletion:]_block_invoke
- ___57-[AFUIServiceDelegate contactsUIWillBeginWithCompletion:]_block_invoke.cold.1
- ___58-[AFUIServiceDelegate authenticationDidEndWithCompletion:]_block_invoke
- ___58-[AFUIServiceDelegate authenticationDidEndWithCompletion:]_block_invoke.cold.1
- ___59-[AFUIContactsController meContactInfosForTextContentType:]_block_invoke
- ___61-[AFUIServiceDelegate authenticationWillBeginWithCompletion:]_block_invoke
- ___61-[AFUIServiceDelegate authenticationWillBeginWithCompletion:]_block_invoke.cold.1
- ___68-[AFUIServiceDelegate _sendAuthenticationStateOperation:completion:]_block_invoke
- ___68-[AFUIServiceDelegate _sendAuthenticationStateOperation:completion:]_block_invoke_2
- ___69-[AFUIServiceDelegate _queuedTextOperationsForSecureAppID:processID:]_block_invoke
- ___69-[AFUIServiceDelegate _queuedTextOperationsForSecureAppID:processID:]_block_invoke.cold.1
- ___block_descriptor_32_e8_v16?0Q8l
- ___block_descriptor_40_e8_32bs_e5_v8?0ls32l8
- ___block_descriptor_48_e8_32s40bs_e5_v8?0ls32l8s40l8
- ___block_descriptor_56_e8_32s40bs_e5_v8?0ls32l8s40l8
- ___block_literal_global.264
- ___block_literal_global.273
- _meContactInfosForTextContentType:.onceToken
- _meContactInfosForTextContentType:.preferredLabelOrder
- _objc_msgSend$_meActiom
- _objc_msgSend$_queueTextOperations:forSecureAppID:processID:
- _objc_msgSend$_queuedTextOperationsForSecureAppID:processID:
- _objc_msgSend$_sendAuthenticationStateOperation:completion:
- _objc_msgSend$_sendTextOperations:toSession:
- _objc_msgSend$_setupPanelForSessionUUID:
- _objc_msgSend$authenticationDidEndWithCompletion:
- _objc_msgSend$authenticationWillBeginWithCompletion:
- _objc_msgSend$contactsUIDidEndWithCompletion:
- _objc_msgSend$contactsUIWillBeginWithCompletion:
- _objc_msgSend$currentSession
- _objc_msgSend$currentSessionQueue
- _objc_msgSend$initWithSecureAppID:processID:textOperations:
- _objc_msgSend$passwordsUIDidEndWithCompletion:
- _objc_msgSend$queuedOperationsWithSecureAppID:processID:textOperations:
- _objc_msgSend$setCurrentSession:
- _objc_msgSend$setCurrentSessionQueue:
- _objc_retain_x26
CStrings:
+ "\x03\x11"
+ "\a"
+ "\x111"
+ "%@ - %@"
+ "%s %@"
+ "%s %@ is for a session being targeted by AutoFill which is authenticating %@"
+ "%s _displayMenuForContentController: with invalid centerOfCaret"
+ "&"
+ "-[AFUIAutoFillPopoverController _displayContextMenuForSourceRect:caretRect:]"
+ "-[AFUIServiceDelegate _checkAndSendQueuedTextOperationsIfNecessary:]_block_invoke"
+ "-[AFUIServiceDelegate _queueTextOperations:forSecureAppID:processID:completionHandler:]"
+ "-[AFUIServiceDelegate _sendTextOperations:toSession:completionHandler:]"
+ "-[AFUIServiceDelegate authenticationDidEndForSessionUUID:completion:]"
+ "-[AFUIServiceDelegate authenticationWillBeginForSessionUUID:completion:]"
+ "-[AFUIServiceDelegate inputSystemService:inputSessionDidPause:withReason:]"
+ "-[AFUIServiceDelegate inputSystemService:inputSessionDidUnpause:withReason:]"
+ "@\"RBSProcessMonitor\""
+ "@28@0:8i16@20"
+ "@44@0:8@16i24@28@?36"
+ "R"
+ "T@\"NSMutableArray\",&,N,V_currentSessions"
+ "T@\"NSUUID\",&,N,V_sessionUUID"
+ "T@\"NSUUID\",&,V_authenticatingForSessionId"
+ "T@\"RBSProcessMonitor\",&,V_processMonitor"
+ "T@\"RTIDocumentTraits\",&,V_authenticatingForDocumentTraits"
+ "T@\"UIViewController\",W,V_presentingViewController"
+ "T@?,R,N,V_completionHandler"
+ "TB,V_willPresentMenu"
+ "_authenticatingForDocumentTraits"
+ "_authenticatingForSessionId"
+ "_completionHandler"
+ "_contextId"
+ "_currentSessions"
+ "_displayContextMenu"
+ "_displayContextMenuForSourceRect:caretRect:"
+ "_displayContextMenuWhenReady"
+ "_meAction"
+ "_meContactInfosForTextContentType:meContact:"
+ "_monitorDocumentProcessVisibility:"
+ "_performBlockOnInternalQueueForUUID:block:"
+ "_processMonitor"
+ "_queueTextOperations:forSecureAppID:processID:completionHandler:"
+ "_sendAuthenticationStateOperation:sessionUUID:completion:"
+ "_sendTextOperations:toSession:completionHandler:"
+ "_sessionForUUID:"
+ "_sessionUUID"
+ "_setIsMenuPresented:forSessionUUID:"
+ "_setupPanelForSessionUUID:documentPid:"
+ "_sourceRectInApplicationCoordinates"
+ "_translatedRectFromApplication:"
+ "_willPresentMenu"
+ "authenticatingForDocumentTraits"
+ "authenticatingForSessionId"
+ "authenticationDidEndForSessionUUID:completion:"
+ "authenticationWillBeginForSessionUUID:completion:"
+ "completionHandler"
+ "contactsUIDidEndForSessionUUID:completion:"
+ "contactsUIWillBeginForSessionUUID:completion:"
+ "convertRect:fromView:"
+ "currentSessions"
+ "descriptor"
+ "dismissAutoFillMenu"
+ "dismissAutoFillPanel"
+ "endowmentNamespaces"
+ "flushOperations"
+ "handleEventFromRemoteSource_autoFillIsMenuPresented:"
+ "identifierWithPid:"
+ "initWithCalendarIdentifier:"
+ "initWithDocumentPid:sessionUUID:"
+ "initWithSecureAppID:processID:textOperations:completionHandler:"
+ "isAutoFillTextOperation"
+ "isExplicitAutoFillInvocation"
+ "isMenuPresented"
+ "layerID"
+ "monitorWithConfiguration:"
+ "passwordsUIDidEndForSessionUUID:completion:"
+ "predicateMatchingIdentifier:"
+ "processMonitor"
+ "queuedOperationsWithSecureAppID:processID:textOperations:completionHandler:"
+ "screen"
+ "scrolling"
+ "sessionUUID"
+ "setAuthenticatingForDocumentTraits:"
+ "setAuthenticatingForSessionId:"
+ "setContainerView:"
+ "setCurrentSessions:"
+ "setEndowmentNamespaces:"
+ "setIsAutoFillTextOperation:"
+ "setIsExplicitAutoFillInvocation:"
+ "setIsMenuPresented:forSessionUUID:"
+ "setPredicates:"
+ "setProcessMonitor:"
+ "setServiceClass:"
+ "setSessionUUID:"
+ "setStateDescriptor:"
+ "setUpdateHandler:"
+ "setValues:"
+ "setWillPresentMenu:"
+ "v16@?0@\"<RBSProcessMonitorConfiguring>\"8"
+ "v20@0:8i16"
+ "v28@0:8B16@\"NSUUID\"20"
+ "v28@0:8B16@20"
+ "v32@0:8@\"NSUUID\"16@?<v@?>24"
+ "v32@?0@\"AFUIPanel\"8Q16^B24"
+ "v32@?0@\"RBSProcessMonitor\"8@\"RBSProcessHandle\"16@\"RBSProcessStateUpdate\"24"
+ "v36@0:8B16@20@?28"
+ "v44@0:8@16@24i32@?36"
+ "v80@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16{CGRect={CGPoint=dd}{CGSize=dd}}48"
+ "visiblePeripheralFrame"
+ "willPresentMenu"
+ "{CGRect={CGPoint=dd}{CGSize=dd}}16@0:8"
+ "{CGRect={CGPoint=dd}{CGSize=dd}}48@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16"
- "\x03\x12"
- "\b"
- "\x12"
- "\x14"
- "%@ %@. - %@"
- "%s %@ is ending session %@"
- "%s %@ is for session %@ that is ending for expected interruption"
- "%s %@ is for session %@ that is resuming from expected interruption"
- "-[AFUIServiceDelegate _queueTextOperations:forSecureAppID:processID:]"
- "-[AFUIServiceDelegate _queuedTextOperationsForSecureAppID:processID:]_block_invoke"
- "-[AFUIServiceDelegate _sendTextOperations:toSession:]"
- "-[AFUIServiceDelegate authenticationDidEndWithCompletion:]_block_invoke"
- "-[AFUIServiceDelegate authenticationWillBeginWithCompletion:]_block_invoke"
- "-[AFUIServiceDelegate contactsUIDidEndWithCompletion:]_block_invoke"
- "-[AFUIServiceDelegate contactsUIWillBeginWithCompletion:]_block_invoke"
- "@\"RTIInputSystemServiceSession\""
- "@36@0:8@16i24@28"
- "T@\"NSObject<OS_dispatch_queue>\",&,V_currentSessionQueue"
- "T@\"RTIInputSystemServiceSession\",&,N,V_currentSession"
- "T@\"UIViewController\",&,V_presentingViewController"
- "_currentSession"
- "_currentSessionQueue"
- "_meActiom"
- "_queueTextOperations:forSecureAppID:processID:"
- "_queuedTextOperationsForSecureAppID:processID:"
- "_sendAuthenticationStateOperation:completion:"
- "_sendTextOperations:toSession:"
- "_sessionIDBeforeAuthentication"
- "_sessionIDBeforeContactsUI"
- "_setupPanelForSessionUUID:"
- "authenticationDidEndWithCompletion:"
- "authenticationWillBeginWithCompletion:"
- "contactsUIDidEndWithCompletion:"
- "contactsUIWillBeginWithCompletion:"
- "currentSession"
- "currentSessionQueue"
- "initWithSecureAppID:processID:textOperations:"
- "passwordsUIDidEndWithCompletion:"
- "queuedOperationsWithSecureAppID:processID:textOperations:"
- "setCurrentSession:"
- "setCurrentSessionQueue:"
- "v24@0:8@?<v@?>16"
- "v28@0:8B16@?20"
- "v36@0:8@16@24i32"

```
