## AutoFillUI

> `/System/Library/PrivateFrameworks/AutoFillUI.framework/AutoFillUI`

```diff

-56.1.0.0.0
-  __TEXT.__text: 0x194e0
-  __TEXT.__auth_stubs: 0x5b0
-  __TEXT.__objc_methlist: 0x1528
+56.150.1.1.0
+  __TEXT.__text: 0x1b05c
+  __TEXT.__auth_stubs: 0x5e0
+  __TEXT.__objc_methlist: 0x16d4
   __TEXT.__const: 0xd8
-  __TEXT.__cstring: 0x12c9
-  __TEXT.__gcc_except_tab: 0x478
+  __TEXT.__cstring: 0x155f
+  __TEXT.__gcc_except_tab: 0x4a0
   __TEXT.__ustring: 0xb0
   __TEXT.__dlopen_cstrs: 0x104
   __TEXT.__oslogstring: 0x3
-  __TEXT.__unwind_info: 0x6dc
-  __TEXT.__objc_classname: 0x400
-  __TEXT.__objc_methname: 0x65ea
-  __TEXT.__objc_methtype: 0x1907
-  __TEXT.__objc_stubs: 0x4cc0
-  __DATA_CONST.__got: 0x230
-  __DATA_CONST.__const: 0x850
-  __DATA_CONST.__objc_classlist: 0xa8
+  __TEXT.__unwind_info: 0x750
+  __TEXT.__objc_classname: 0x429
+  __TEXT.__objc_methname: 0x698e
+  __TEXT.__objc_methtype: 0x19ab
+  __TEXT.__objc_stubs: 0x4f40
+  __DATA_CONST.__got: 0x238
+  __DATA_CONST.__const: 0x8c8
+  __DATA_CONST.__objc_classlist: 0xb8
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x98
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x5280
-  __DATA_CONST.__objc_selrefs: 0x15c8
+  __DATA_CONST.__objc_const: 0x55b0
+  __DATA_CONST.__objc_selrefs: 0x1678
   __DATA_CONST.__objc_arraydata: 0xc8
-  __AUTH_CONST.__cfstring: 0x13a0
-  __AUTH_CONST.__objc_const: 0x898
-  __AUTH_CONST.__const: 0x3a0
+  __AUTH_CONST.__cfstring: 0x1440
+  __AUTH_CONST.__objc_const: 0x970
+  __AUTH_CONST.__const: 0x3c0
   __AUTH_CONST.__objc_arrayobj: 0x90
   __AUTH_CONST.__objc_intobj: 0x18
-  __AUTH_CONST.__auth_got: 0x2e8
-  __AUTH.__objc_data: 0x4b0
+  __AUTH_CONST.__auth_got: 0x300
+  __AUTH.__objc_data: 0x550
   __DATA.__objc_protorefs: 0x10
-  __DATA.__objc_classrefs: 0x278
-  __DATA.__objc_superrefs: 0x70
-  __DATA.__objc_ivar: 0x1a0
+  __DATA.__objc_classrefs: 0x298
+  __DATA.__objc_superrefs: 0x88
+  __DATA.__objc_ivar: 0x1c0
   __DATA.__data: 0x768
-  __DATA.__bss: 0xd0
+  __DATA.__bss: 0xe0
   __DATA_DIRTY.__objc_data: 0x1e0
   __DATA_DIRTY.__bss: 0xe0
   - /System/Library/Frameworks/Contacts.framework/Contacts

   - /System/Library/PrivateFrameworks/WebKitLegacy.framework/WebKitLegacy
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F79E2120-A657-31E9-BB15-58742046A8AC
-  Functions: 624
-  Symbols:   2697
-  CStrings:  1594
+  UUID: AAEC4CE4-B3AB-3D93-9F06-19525DE6BB8D
+  Functions: 674
+  Symbols:   2855
+  CStrings:  1663
 
Symbols:
+ +[_AFUIQueuedOperations queuedOperationsWithSecureAppID:processID:textOperations:]
+ -[AFUIAutoFillPasswordController passwordsControllerDidFinish:]
+ -[AFUIExplicitAutoFillController passwordsControllerDidFinish:]
+ -[AFUIPanel _applyPanelState]
+ -[AFUIPanel _sceneWillEnterForeground:]
+ -[AFUIPanel authenticationDidEndWithCompletion:]
+ -[AFUIPanel authenticationWillBeginWithCompletion:]
+ -[AFUIPanel contactsUIDidEndWithCompletion:]
+ -[AFUIPanel contactsUIWillBeginWithCompletion:]
+ -[AFUIPanel dealloc]
+ -[AFUIPanel documentStateChanged:].cold.1
+ -[AFUIPanel init]
+ -[AFUIPanel panelState]
+ -[AFUIPanel passwordsUIDidEndWithCompletion:]
+ -[AFUIPanel setPanelState:]
+ -[AFUIPanelState .cxx_destruct]
+ -[AFUIPanelState documentState]
+ -[AFUIPanelState documentTraits]
+ -[AFUIPanelState initDisplayed:documentTraits:documentState:textOperationsHandler:]
+ -[AFUIPanelState initNotDisplayed]
+ -[AFUIPanelState isDisplayed]
+ -[AFUIPanelState textOperationsHandler]
+ -[AFUIPasswordsController passwordViewControllerDidFinish:]
+ -[AFUIServiceDelegate _checkAndSendQueuedTextOperationsIfNecessary:]
+ -[AFUIServiceDelegate _queueTextOperations:forSecureAppID:processID:]
+ -[AFUIServiceDelegate _queueTextOperations:forSecureAppID:processID:].cold.1
+ -[AFUIServiceDelegate _queueTextOperations:forSecureAppID:processID:].cold.2
+ -[AFUIServiceDelegate _queuedTextOperationsForSecureAppID:processID:]
+ -[AFUIServiceDelegate _scheduleExpirationOfQueuedOperations:]
+ -[AFUIServiceDelegate _sendOrQueueTextOperations:session:withInputIdentifier:]
+ -[AFUIServiceDelegate _tearDownPanelsExceptForSessionUUID:]
+ -[AFUIServiceDelegate inputSystemService:inputSessionDidBegin:options:].cold.5
+ -[AFUIServiceDelegate passwordsUIDidEndWithCompletion:]
+ -[AFUIServiceSession passwordsUIDidEndWithCompletion:]
+ -[_AFUIQueuedOperations .cxx_destruct]
+ -[_AFUIQueuedOperations initWithSecureAppID:processID:textOperations:]
+ -[_AFUIQueuedOperations processID]
+ -[_AFUIQueuedOperations secureAppID]
+ -[_AFUIQueuedOperations textOperations]
+ GCC_except_table12
+ GCC_except_table20
+ GCC_except_table21
+ _AFUIPanelOSLogFacility
+ _AFUIPanelOSLogFacility.logFacility
+ _AFUIPanelOSLogFacility.onceToken
+ _OBJC_CLASS_$_AFUIPanelState
+ _OBJC_CLASS_$_NSLock
+ _OBJC_CLASS_$_NSUUID
+ _OBJC_CLASS_$__AFUIQueuedOperations
+ _OBJC_IVAR_$_AFUIPanel._panelState
+ _OBJC_IVAR_$_AFUIPanelState._displayed
+ _OBJC_IVAR_$_AFUIPanelState._documentState
+ _OBJC_IVAR_$_AFUIPanelState._documentTraits
+ _OBJC_IVAR_$_AFUIPanelState._textOperationsHandler
+ _OBJC_IVAR_$_AFUIServiceDelegate._lock
+ _OBJC_IVAR_$__AFUIQueuedOperations._processID
+ _OBJC_IVAR_$__AFUIQueuedOperations._secureAppID
+ _OBJC_IVAR_$__AFUIQueuedOperations._textOperations
+ _OBJC_METACLASS_$_AFUIPanelState
+ _OBJC_METACLASS_$__AFUIQueuedOperations
+ _UISceneWillEnterForegroundNotification
+ __OBJC_$_CLASS_METHODS__AFUIQueuedOperations
+ __OBJC_$_INSTANCE_METHODS_AFUIPanelState
+ __OBJC_$_INSTANCE_METHODS__AFUIQueuedOperations
+ __OBJC_$_INSTANCE_VARIABLES_AFUIPanelState
+ __OBJC_$_INSTANCE_VARIABLES__AFUIQueuedOperations
+ __OBJC_$_PROP_LIST_AFUIPanelState
+ __OBJC_$_PROP_LIST__AFUIQueuedOperations
+ __OBJC_CLASS_RO_$_AFUIPanelState
+ __OBJC_CLASS_RO_$__AFUIQueuedOperations
+ __OBJC_METACLASS_RO_$_AFUIPanelState
+ __OBJC_METACLASS_RO_$__AFUIQueuedOperations
+ ___29-[AFUIPanel _applyPanelState]_block_invoke
+ ___29-[AFUIPanel _applyPanelState]_block_invoke.cold.1
+ ___29-[AFUIPanel _applyPanelState]_block_invoke.cold.2
+ ___55-[AFUIServiceDelegate passwordsUIDidEndWithCompletion:]_block_invoke
+ ___59-[AFUIServiceDelegate _tearDownPanelsExceptForSessionUUID:]_block_invoke
+ ___61-[AFUIServiceDelegate _scheduleExpirationOfQueuedOperations:]_block_invoke
+ ___61-[AFUIServiceDelegate _scheduleExpirationOfQueuedOperations:]_block_invoke.cold.1
+ ___69-[AFUIServiceDelegate _queuedTextOperationsForSecureAppID:processID:]_block_invoke
+ ___69-[AFUIServiceDelegate _queuedTextOperationsForSecureAppID:processID:]_block_invoke.cold.1
+ ___AFUIPanelOSLogFacility_block_invoke
+ ___block_descriptor_40_e8_32bs_e5_v8?0ls32l8
+ ___block_descriptor_52_e8_32s40r_e46_v32?0"NSUUID"8"_AFUIQueuedOperations"16^B24ls32l8r40l8
+ ___block_descriptor_64_e8_32s40s48s56s_e5_v8?0ls32l8s40l8s48l8s56l8
+ ___block_descriptor_72_e8_32s40s48s56s64w_e27_v16?0"RTITextOperations"8lw64l8s32l8s40l8s48l8s56l8
+ ___block_descriptor_88_e8_32s40s48s56s64s72s80w_e5_v8?0ls32l8s40l8s48l8s56l8s64l8w80l8s72l8
+ ___block_literal_global.264
+ ___block_literal_global.273
+ ___block_literal_global.4
+ _dispatch_after
+ _dispatch_get_global_queue
+ _dispatch_time
+ _objc_msgSend$UUID
+ _objc_msgSend$_applyPanelState
+ _objc_msgSend$_checkAndSendQueuedTextOperationsIfNecessary:
+ _objc_msgSend$_queueTextOperations:forSecureAppID:processID:
+ _objc_msgSend$_queuedTextOperationsForSecureAppID:processID:
+ _objc_msgSend$_scheduleExpirationOfQueuedOperations:
+ _objc_msgSend$_sendOrQueueTextOperations:session:withInputIdentifier:
+ _objc_msgSend$_tearDownPanelsExceptForSessionUUID:
+ _objc_msgSend$initDisplayed:documentTraits:documentState:textOperationsHandler:
+ _objc_msgSend$initNotDisplayed
+ _objc_msgSend$initWithSecureAppID:processID:textOperations:
+ _objc_msgSend$isDisplayed
+ _objc_msgSend$lock
+ _objc_msgSend$panelState
+ _objc_msgSend$passwordsControllerDidFinish:
+ _objc_msgSend$passwordsUIDidEndWithCompletion:
+ _objc_msgSend$processID
+ _objc_msgSend$queuedOperationsWithSecureAppID:processID:textOperations:
+ _objc_msgSend$removeObserver:name:object:
+ _objc_msgSend$secureAppID
+ _objc_msgSend$setPanelState:
+ _objc_msgSend$textOperationsHandler
+ _objc_msgSend$unlock
- -[AFUIServiceDelegate _checkAndSendQueuedTextOperationsIfNecessary]
- -[AFUIServiceDelegate _sendOrQueueTextOperations:withInputIdentifier:]
- -[AFUIServiceDelegate _sendOrQueueTextOperations:withInputIdentifier:].cold.1
- -[AFUIServiceDelegate _sendOrQueueTextOperations:withInputIdentifier:].cold.2
- _OBJC_IVAR_$_AFUIServiceDelegate._currentTraits
- ___block_descriptor_56_e8_32s40s48w_e27_v16?0"RTITextOperations"8lw48l8s32l8s40l8
- ___block_descriptor_80_e8_32s40s48s56s64s72w_e5_v8?0ls32l8s40l8s48l8s56l8s64l8w72l8
- ___block_literal_global.221
- ___block_literal_global.230
- _objc_msgSend$_checkAndSendQueuedTextOperationsIfNecessary
- _objc_msgSend$_sendOrQueueTextOperations:withInputIdentifier:
- _objc_msgSend$isEqualToNumber:
CStrings:
+ "\x12"
+ "\x14"
+ "%s Cannot queue textOperations: secureAppID is empty"
+ "%s Found queued textOperations for session with appId: %@ (payloadID: %@)"
+ "%s Queued operations are expiring unused for payloadID: %@"
+ "%s Queueing textOperations for session with appId: %@ (payloadID: %@)"
+ "%s action:DisplayPanel appId:%@"
+ "%s action:HidePanel appId:%@"
+ "%s appId:%@"
+ "%s sending textOperations for session %@ (appId: %@)"
+ "%s textOperations %@ for session uuid %@ (appId: %@)"
+ "-[AFUIPanel _applyPanelState]_block_invoke"
+ "-[AFUIPanel displayForDocumentTraits:documentState:textOperationsHandler:]"
+ "-[AFUIPanel documentStateChanged:]"
+ "-[AFUIPanel hide]"
+ "-[AFUIPanel transientHide]"
+ "-[AFUIPanel transientUnhide]"
+ "-[AFUIServiceDelegate _checkAndSendQueuedTextOperationsIfNecessary:]"
+ "-[AFUIServiceDelegate _queueTextOperations:forSecureAppID:processID:]"
+ "-[AFUIServiceDelegate _queuedTextOperationsForSecureAppID:processID:]_block_invoke"
+ "-[AFUIServiceDelegate _scheduleExpirationOfQueuedOperations:]_block_invoke"
+ "@\"AFUIPanelState\""
+ "@\"NSLock\""
+ "@\"RTITextOperations\""
+ "@28@0:8@16i24"
+ "@36@0:8@16i24@28"
+ "@44@0:8B16@20@28@?36"
+ "AFUIPanelState"
+ "T@\"AFUIPanelState\",&,N,V_panelState"
+ "T@\"NSString\",R,C,N,V_secureAppID"
+ "T@\"RTIDocumentState\",R,C,N,V_documentState"
+ "T@\"RTIDocumentTraits\",R,C,N,V_documentTraits"
+ "T@\"RTITextOperations\",R,N,V_textOperations"
+ "T@?,R,C,N,V_textOperationsHandler"
+ "TB,R,N,GisDisplayed,V_displayed"
+ "Ti,R,N,V_processID"
+ "UUID"
+ "_AFUIQueuedOperations"
+ "_applyPanelState"
+ "_checkAndSendQueuedTextOperationsIfNecessary:"
+ "_displayed"
+ "_lock"
+ "_panelState"
+ "_processID"
+ "_queueTextOperations:forSecureAppID:processID:"
+ "_queuedTextOperationsForSecureAppID:processID:"
+ "_sceneWillEnterForeground:"
+ "_scheduleExpirationOfQueuedOperations:"
+ "_secureAppID"
+ "_sendOrQueueTextOperations:session:withInputIdentifier:"
+ "_tearDownPanelsExceptForSessionUUID:"
+ "_textOperations"
+ "displayed"
+ "i16@0:8"
+ "initDisplayed:documentTraits:documentState:textOperationsHandler:"
+ "initNotDisplayed"
+ "initWithSecureAppID:processID:textOperations:"
+ "isDisplayed"
+ "lock"
+ "panelState"
+ "passwordsControllerDidFinish:"
+ "passwordsUIDidEndWithCompletion:"
+ "processID"
+ "queuedOperationsWithSecureAppID:processID:textOperations:"
+ "removeObserver:name:object:"
+ "secureAppID"
+ "setPanelState:"
+ "textOperationsHandler"
+ "unlock"
+ "v24@0:8@\"AFUIPasswordsController\"16"
+ "v32@?0@\"NSUUID\"8@\"_AFUIQueuedOperations\"16^B24"
+ "v36@0:8@16@24i32"
- "%s %@: queueing textOperations for session with input identifier %@"
- "%s %@: sending textOperations for session %@"
- "%s %@: textOperations %@ for session %@"
- "%s Session mismatch for autofill results. currentSession = %@"
- "-[AFUIServiceDelegate _checkAndSendQueuedTextOperationsIfNecessary]"
- "-[AFUIServiceDelegate _sendOrQueueTextOperations:withInputIdentifier:]"
- "_checkAndSendQueuedTextOperationsIfNecessary"
- "_currentTraits"
- "_sendOrQueueTextOperations:withInputIdentifier:"
- "isEqualToNumber:"

```
