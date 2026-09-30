## coreautha

> `/System/Library/Frameworks/LocalAuthentication.framework/Support/coreautha.bundle/Contents/MacOS/coreautha`

```diff

-1656.80.6.0.0
-  __TEXT.__text: 0x12ff4
-  __TEXT.__auth_stubs: 0x4c0
-  __TEXT.__objc_stubs: 0x2f00
-  __TEXT.__objc_methlist: 0x102c
-  __TEXT.__const: 0x118
-  __TEXT.__objc_methname: 0x3508
-  __TEXT.__objc_classname: 0x355
-  __TEXT.__objc_methtype: 0xde7
-  __TEXT.__gcc_except_tab: 0xcc
-  __TEXT.__oslogstring: 0xf27
-  __TEXT.__cstring: 0x16c5
-  __TEXT.__unwind_info: 0x498
-  __DATA_CONST.__auth_got: 0x270
-  __DATA_CONST.__got: 0x220
-  __DATA_CONST.__const: 0x4d0
-  __DATA_CONST.__cfstring: 0xdc0
+1656.100.223.0.0
+  __TEXT.__text: 0x156c4
+  __TEXT.__auth_stubs: 0x4b0
+  __TEXT.__objc_stubs: 0x31a0
+  __TEXT.__objc_methlist: 0x1a5c
+  __TEXT.__const: 0x120
+  __TEXT.__objc_methname: 0x37f9
+  __TEXT.__objc_classname: 0x390
+  __TEXT.__objc_methtype: 0xeee
+  __TEXT.__gcc_except_tab: 0x230
+  __TEXT.__oslogstring: 0x114d
+  __TEXT.__cstring: 0x1885
+  __TEXT.__unwind_info: 0x548
+  __DATA_CONST.__auth_got: 0x268
+  __DATA_CONST.__got: 0x2a8
+  __DATA_CONST.__const: 0x5c0
+  __DATA_CONST.__cfstring: 0xde0
   __DATA_CONST.__objc_classlist: 0xb8
   __DATA_CONST.__objc_catlist: 0x10
-  __DATA_CONST.__objc_protolist: 0x90
+  __DATA_CONST.__objc_protolist: 0xa0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x20
-  __DATA_CONST.__objc_superrefs: 0x88
-  __DATA_CONST.__objc_intobj: 0x300
-  __DATA.__objc_const: 0x5978
-  __DATA.__objc_selrefs: 0xdb8
-  __DATA.__objc_ivar: 0x194
+  __DATA_CONST.__objc_superrefs: 0x90
+  __DATA_CONST.__objc_intobj: 0x120
+  __DATA.__objc_const: 0x4c10
+  __DATA.__objc_selrefs: 0x10b8
+  __DATA.__objc_ivar: 0x1b0
   __DATA.__objc_data: 0x730
-  __DATA.__data: 0x6c0
+  __DATA.__data: 0x780
   __DATA.__bss: 0x108
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /System/Library/PrivateFrameworks/login.framework/Versions/A/login
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 96B85AB5-F14E-3DD5-94C6-59890B333224
-  Functions: 457
-  Symbols:   165
-  CStrings:  1259
+  UUID: 1DDB8D68-B446-3576-9CE4-B57BF844DD0A
+  Functions: 508
+  Symbols:   183
+  CStrings:  1321
 
Symbols:
+ _LACPolicyDeviceAdminAuthentication
+ _LACPolicyOptionAuthenticationReason
+ _LACPolicyOptionAuthenticationTitle
+ _LACPolicyOptionBodyText
+ _LACPolicyOptionCallerIconPath
+ _LACPolicyOptionCancelVisible
+ _LACPolicyOptionFallbackVisible
+ _LACPolicyOptionPINLabel
+ _LACPolicyOptionPINMaxLength
+ _LACPolicyOptionPINMinLength
+ _LACPolicyOptionPasswordAuthenticationReason
+ _LACPolicyOptionTKAuthOperationError
+ _LACPolicyOptionUseUnmanagedSpace
+ _LACPolicyOptionUserCancel
+ _LACPolicyOptionUserFallback
+ _LACResultEnteredPassphrase
+ _LACResultEnteredPassword
+ _OBJC_CLASS_$_LACCachedExternalizedContext
+ _OBJC_CLASS_$_LACConcurrentIdleUIListenerProvider
+ _OBJC_CLASS_$_LACInstalledAppsCache
+ _OBJC_CLASS_$_LACStringHelper
- _OBJC_CLASS_$_InstalledAppsCache
- _OBJC_CLASS_$_LACachedExternalizedContext
- _objc_setProperty_nonatomic_copy
CStrings:
+ "%@ immediately falls back to password after reconnection"
+ "%@ no idle UI handler"
+ "%@ not a key window"
+ "%@ will set up evaluation connection"
+ "%@ will set up idle connection"
+ "%s %{public}@, %{public}@, state: %@ on %@"
+ "%s Release window: %d on %@"
+ "%s State: %@ on %@"
+ "%s UI controller unregistered mechanism: %@ on %@"
+ "%s options: %{public}@, endpoint: %@, rid: %@ on %@"
+ "-[LAAuthDialogController closeDialogReleaseWindow:]"
+ "-[LAAuthDialogController initWithInternalInfo:parent:window:]"
+ "-[LAAuthDialogController openDialogAtPosition:shouldUsePosition:]"
+ "-[LAAuthMechanismUI _configureDialogAtPosition:shouldUsePosition:]"
+ "-[LAAuthMechanismUI _createControlForController:internalInfo:window:]"
+ "-[LAAuthMechanismUI _informHandlerAboutFocusIfNeeded]"
+ "-[LAAuthMechanismUI _invalidateEvaluationConnection]"
+ "-[LAAuthMechanismUI _invalidateIdleConnection]"
+ "-[LAAuthMechanismUI destroyIfNeeded]"
+ "-[LAAuthMechanismUI dismissRemoteUIWithIdleEndpoint:wasInvalidated:completionHandler:]"
+ "-[LAAuthMechanismUI initWithOptions:]"
+ "-[LAUIController mechanismFinished:]"
+ "@\"<LAAuthMechanismUIDelegate>\""
+ "@\"<LACBackoffCounter>\""
+ "@\"<LACBackoffCounter>\"16@0:8"
+ "@\"<LACConcurrentIdleUIHandling>\""
+ "@\"<LACConcurrentIdleUIHandling>\"16@0:8"
+ "@\"<LACRemoteUIHost>\""
+ "@\"<LACRemoteUIHost>\"16@0:8"
+ "@\"<LACUIMechanism>\""
+ "@\"<LACUIMechanism>\"16@0:8"
+ "@\"<NSObject>\""
+ "@\"LACCachedExternalizedContext\""
+ "@\"LACCachedExternalizedContext\"16@0:8"
+ "@\"NSNumber\""
+ "@32@0:8q16@24"
+ "@40@0:8@16@24@32"
+ "Evaluation connection was interrupted"
+ "Evaluation connection was invalidated"
+ "Executing completion with invalidation"
+ "Idle connection was interrupted"
+ "Idle connection was invalidated"
+ "LAAuthMechanismUIDelegate"
+ "LACConcurrentIdleUIPresenting"
+ "LACContextExternalizing"
+ "LACRemoteUI"
+ "LACRemoteUIHost"
+ "LACUIMechanism"
+ "LACUITransition"
+ "RequestId"
+ "T@\"<LAAuthMechanismUIDelegate>\",W,N,V_delegate"
+ "T@\"<LACBackoffCounter>\",?,&,N"
+ "T@\"<LACBackoffCounter>\",?,&,N,V_backoffCounter"
+ "T@\"<LACConcurrentIdleUIHandling>\",?,R,N"
+ "T@\"<LACConcurrentIdleUIHandling>\",?,R,N,V_idleUIHandler"
+ "T@\"<LACRemoteUIHost>\",?,R,N"
+ "T@\"<LACRemoteUIHost>\",?,R,N,V_remoteUIHost"
+ "T@\"<LACUIMechanism>\",?,R,N"
+ "T@\"<LACUIMechanism>\",?,R,N,V_mechanism"
+ "T@\"LACCachedExternalizedContext\",?,R,N"
+ "T@\"LACCachedExternalizedContext\",?,R,N,V_cachedExternalizedContext"
+ "UI controller registered mechanism: %@"
+ "Will invalidate evaluation connection %@"
+ "Will invalidate idle connection %@"
+ "XPC error connecting to idleUIHandler: %{public}@"
+ "_configureDialogAtPosition:shouldUsePosition:"
+ "_createControlForController:internalInfo:window:"
+ "_didBecomeKeyObservation"
+ "_didResignKeyObservation"
+ "_dismissUICompletionBlock"
+ "_evaluationConnection"
+ "_idleConnection"
+ "_idleUIHandler"
+ "_informHandlerAboutFocusIfNeeded"
+ "_invalidateConnections"
+ "_invalidateEvaluationConnection"
+ "_invalidateIdleConnection"
+ "_mechanisms"
+ "_requestId"
+ "_setupIdleUIConnectionWithEndpoint:"
+ "_showUICompletionBlock"
+ "_state"
+ "addObserverForName:object:queue:usingBlock:"
+ "checkHasPendingUIRequestsWithCompletion:"
+ "closeDialogReleaseWindow:"
+ "connectIdleUI:identifier:completion:"
+ "connectRemoteUI:requestID:reply:"
+ "copy"
+ "destroyIdleUI"
+ "destroyIfNeeded"
+ "dismissRemoteUIWithIdleEndpoint:wasInvalidated:completionHandler:"
+ "dismissing"
+ "displayName"
+ "expectReconnectionOfIdleUI"
+ "idleUIGotFocus:identifier:completion:"
+ "idleUIHandler"
+ "idleUIXPCInterface"
+ "infoForPid:"
+ "initWithInternalInfo:parent:window:"
+ "initWithOptions:"
+ "initWithStyle:window:"
+ "isKeyWindow"
+ "mechanismFinished:"
+ "openDialogAtPosition:shouldUsePosition:"
+ "setContentViewController:"
+ "setDismissing:"
+ "setFrameOrigin:"
+ "setInternalInfo:"
+ "setupConnectionWithOptions:endpoint:"
+ "v16@?0@\"NSNotification\"8"
+ "v24@0:8@\"<LACBackoffCounter>\"16"
+ "v24@0:8@\"LAAuthMechanismUI\"16"
+ "v24@0:8@?<v@?@\"NSArray\">16"
+ "v24@?0@\"<LACConcurrentIdleUIHandling>\"8@\"NSError\"16"
+ "v32@?0@\"<LACUIMechanism>\"8@\"<LACBackoffCounter>\"16@\"NSError\"24"
+ "v36@0:8@\"NSXPCListenerEndpoint\"16B24@?<v@?>28"
+ "v36@0:8@16B24@?28"
+ "v36@0:8{CGPoint=dd}16B32"
+ "v40@0:8@\"<LACRemoteUI>\"16@\"NSNumber\"24@?<v@?@\"<LACUIMechanism>\"@\"<LACBackoffCounter>\"@\"NSError\">32"
+ "v40@0:8q16@24@32"
+ "\xe1"
- "%s options: %{public}@, endpoint: %@ on %@"
- "-[LAAuthDialogController closeDialog]"
- "-[LAAuthDialogController initWithInternalInfo:parent:]"
- "-[LAAuthDialogController openDialog]"
- "-[LAAuthMechanismUI _createDialog]"
- "-[LAAuthMechanismUI destroy]"
- "-[LAAuthMechanismUI dismissRemoteUIWasInvalidated:completionHandler:]"
- "-[LAAuthMechanismUI initWithOptions:endpoint:]"
- "@\"<LABackoffCounter>\""
- "@\"<LABackoffCounter>\"16@0:8"
- "@\"<LARemoteUIHost>\""
- "@\"<LARemoteUIHost>\"16@0:8"
- "@\"<LAUIMechanism>\""
- "@\"<LAUIMechanism>\"16@0:8"
- "@\"LACachedExternalizedContext\""
- "@\"LACachedExternalizedContext\"16@0:8"
- "@?<v@?>16@0:8"
- "Connection was interrupted unexpectedly"
- "Connection was invalidated unexpectedly"
- "LAContextExternalizationProt"
- "LARemoteUI"
- "LARemoteUIHost"
- "LAUIMechanism"
- "LAUITransition"
- "T@\"<LABackoffCounter>\",?,&,N"
- "T@\"<LABackoffCounter>\",?,&,N,V_backoffCounter"
- "T@\"<LARemoteUIHost>\",?,R,N"
- "T@\"<LARemoteUIHost>\",?,R,N,V_remoteUIHost"
- "T@\"<LAUIMechanism>\",?,R,N"
- "T@\"<LAUIMechanism>\",?,R,N,V_mechanism"
- "T@\"LACachedExternalizedContext\",?,R,N"
- "T@\"LACachedExternalizedContext\",?,R,N,V_cachedExternalizedContext"
- "T@?,?,C,N"
- "T@?,?,C,N,V_appearedNotification"
- "T@?,?,C,N,V_disappearedNotification"
- "Will invalidate connection %@"
- "_appearedNotification"
- "_closedControllers"
- "_connection"
- "_createDialog"
- "_disappearedNotification"
- "_setupConnectionWithOptions:endpoint:"
- "appNameForPid:bundleId:"
- "appearedNotification"
- "checkClearForIdleExitWithCompletion:"
- "closeDialog"
- "connectRemoteUI:reply:"
- "destroy"
- "disappearedNotification"
- "dismissRemoteUIWasInvalidated:completionHandler:"
- "initWithOptions:endpoint:"
- "openDialog"
- "setAppearedNotification:"
- "setDisappearedNotification:"
- "v24@0:8@\"<LABackoffCounter>\"16"
- "v24@0:8@?<v@?@\"NSDate\"@\"NSError\">16"
- "v28@0:8B16@?20"
- "v28@0:8B16@?<v@?>20"
- "v32@0:8@\"<LARemoteUI>\"16@?<v@?@\"<LAUIMechanism>\"@\"<LABackoffCounter>\"@\"NSError\">24"
- "v32@?0@\"<LAUIMechanism>\"8@\"<LABackoffCounter>\"16@\"NSError\"24"

```
