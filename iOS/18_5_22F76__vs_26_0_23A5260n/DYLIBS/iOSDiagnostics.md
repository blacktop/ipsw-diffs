## iOSDiagnostics

> `/System/Library/PrivateFrameworks/iOSDiagnostics.framework/iOSDiagnostics`

```diff

-820.122.1.0.0
-  __TEXT.__text: 0x3c5c
+1053.0.0.0.0
+  __TEXT.__text: 0x4c7c
   __TEXT.__auth_stubs: 0x380
-  __TEXT.__objc_methlist: 0x824
+  __TEXT.__objc_methlist: 0x8a4
   __TEXT.__const: 0x88
-  __TEXT.__cstring: 0x5d9
-  __TEXT.__gcc_except_tab: 0x110
-  __TEXT.__oslogstring: 0x1e6
-  __TEXT.__unwind_info: 0x1d8
-  __TEXT.__objc_classname: 0x1c9
-  __TEXT.__objc_methname: 0x11bf
-  __TEXT.__objc_methtype: 0x512
-  __TEXT.__objc_stubs: 0xca0
-  __DATA_CONST.__got: 0xf8
-  __DATA_CONST.__const: 0x2d0
-  __DATA_CONST.__objc_classlist: 0x30
-  __DATA_CONST.__objc_protolist: 0x58
+  __TEXT.__cstring: 0xa30
+  __TEXT.__oslogstring: 0x33b
+  __TEXT.__gcc_except_tab: 0xd4
+  __TEXT.__unwind_info: 0x1c8
+  __TEXT.__objc_classname: 0x267
+  __TEXT.__objc_methname: 0x155a
+  __TEXT.__objc_methtype: 0x553
+  __TEXT.__objc_stubs: 0x1180
+  __DATA_CONST.__got: 0x130
+  __DATA_CONST.__const: 0x340
+  __DATA_CONST.__objc_classlist: 0x40
+  __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4d8
+  __DATA_CONST.__objc_selrefs: 0x608
   __DATA_CONST.__objc_protorefs: 0x30
-  __DATA_CONST.__objc_superrefs: 0x28
+  __DATA_CONST.__objc_superrefs: 0x20
   __DATA_CONST.__objc_arraydata: 0x8
   __AUTH_CONST.__auth_got: 0x1d0
-  __AUTH_CONST.__const: 0x20
-  __AUTH_CONST.__cfstring: 0x2a0
-  __AUTH_CONST.__objc_const: 0x12c0
+  __AUTH_CONST.__const: 0x40
+  __AUTH_CONST.__cfstring: 0x520
+  __AUTH_CONST.__objc_const: 0x19b8
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH.__objc_data: 0x1e0
+  __AUTH.__objc_data: 0x280
   __DATA.__objc_ivar: 0x5c
-  __DATA.__data: 0x420
-  __DATA.__bss: 0x1
+  __DATA.__data: 0x4e0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices
+  - /System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard
   - /System/Library/PrivateFrameworks/CheckerBoardServices.framework/CheckerBoardServices
   - /System/Library/PrivateFrameworks/DiagnosticsKit.framework/DiagnosticsKit
   - /System/Library/PrivateFrameworks/DiagnosticsSupport.framework/DiagnosticsSupport

   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: EA48A608-F1B0-322C-9614-96BA20C122F3
-  Functions: 147
-  Symbols:   661
-  CStrings:  345
+  UUID: 42EF47A9-F274-3C2C-BCB2-5D98E543E328
+  Functions: 154
+  Symbols:   755
+  CStrings:  440
 
Symbols:
+ +[DADiagnosticFlow supportsBSXPCSecureCoding]
+ +[DADiagnosticsRemoteViewController requestViewControllerWithHostBundleID:handler:]
+ +[DADiagnosticsRemoteViewControllerHostToServiceAction actionToString:]
+ +[DADiagnosticsRemoteViewControllerHostToServiceAction actionWithType:object:]
+ +[DADiagnosticsRemoteViewControllerServiceToHostAction actionToString:]
+ +[DADiagnosticsRemoteViewControllerServiceToHostAction actionWithType:object:]
+ -[DADiagnosticFlow encodeWithBSXPCCoder:]
+ -[DADiagnosticFlow initWithBSXPCCoder:]
+ -[DADiagnosticsRemoteHostViewController finished]
+ -[DADiagnosticsRemoteHostViewController setFinished:]
+ -[DADiagnosticsRemoteViewController clientIsReady]
+ -[DADiagnosticsRemoteViewController hostApplicationBundleIdentifier]
+ -[DADiagnosticsRemoteViewController hostingController]
+ -[DADiagnosticsRemoteViewController prefersStatusBarHidden]
+ -[DADiagnosticsRemoteViewController requestViewControllerWithHostBundleID:handler:]
+ -[DADiagnosticsRemoteViewController setHostApplicationBundleIdentifier:]
+ -[DADiagnosticsRemoteViewController setHostingController:]
+ -[DADiagnosticsRemoteViewControllerHostToServiceAction performActionForHostedWindowScene:]
+ -[DADiagnosticsRemoteViewControllerHostToServiceAction performActionForHostedWindowScene:].cold.1
+ -[DADiagnosticsRemoteViewControllerHostToServiceAction performActionForHostedWindowScene:].cold.2
+ -[DADiagnosticsRemoteViewControllerHostToServiceAction performActionForHostedWindowScene:].cold.3
+ -[DADiagnosticsRemoteViewControllerHostToServiceAction performActionForHostedWindowScene:].cold.4
+ -[DADiagnosticsRemoteViewControllerHostToServiceAction performActionForHostedWindowScene:].cold.5
+ -[DADiagnosticsRemoteViewControllerServiceToHostAction performActionForSceneController:]
+ -[DADiagnosticsRemoteViewControllerServiceToHostAction performActionForSceneController:].cold.1
+ -[DADiagnosticsRemoteViewControllerServiceToHostAction performActionForSceneController:].cold.2
+ -[DADiagnosticsRemoteViewControllerServiceToHostAction performActionForSceneController:].cold.3
+ -[DADiagnosticsRemoteViewControllerServiceToHostAction performActionForSceneController:].cold.4
+ -[DADiagnosticsRemoteViewControllerServiceToHostAction performActionForSceneController:].cold.5
+ _OBJC_CLASS_$_BSMutableSettings
+ _OBJC_CLASS_$_DADiagnosticsRemoteViewControllerHostToServiceAction
+ _OBJC_CLASS_$_DADiagnosticsRemoteViewControllerServiceToHostAction
+ _OBJC_CLASS_$_NSLayoutConstraint
+ _OBJC_CLASS_$_RBSProcessIdentity
+ _OBJC_CLASS_$_UIViewController
+ _OBJC_CLASS_$__UISceneHostingActionClientToHost
+ _OBJC_CLASS_$__UISceneHostingActionHostToClient
+ _OBJC_CLASS_$__UISceneHostingController
+ _OBJC_CLASS_$__UISceneHostingSceneSpecification
+ _OBJC_IVAR_$_DADiagnosticsRemoteHostViewController._finished
+ _OBJC_IVAR_$_DADiagnosticsRemoteViewController._hostApplicationBundleIdentifier
+ _OBJC_IVAR_$_DADiagnosticsRemoteViewController._hostingController
+ _OBJC_METACLASS_$_DADiagnosticsRemoteViewControllerHostToServiceAction
+ _OBJC_METACLASS_$_DADiagnosticsRemoteViewControllerServiceToHostAction
+ _OBJC_METACLASS_$_UIViewController
+ _OBJC_METACLASS_$__UISceneHostingActionClientToHost
+ _OBJC_METACLASS_$__UISceneHostingActionHostToClient
+ _OUTLINED_FUNCTION_2
+ __OBJC_$_CLASS_METHODS_DADiagnosticsRemoteViewControllerHostToServiceAction
+ __OBJC_$_CLASS_METHODS_DADiagnosticsRemoteViewControllerServiceToHostAction
+ __OBJC_$_INSTANCE_METHODS_DADiagnosticsRemoteViewControllerHostToServiceAction
+ __OBJC_$_INSTANCE_METHODS_DADiagnosticsRemoteViewControllerServiceToHostAction
+ __OBJC_$_PROTOCOL_CLASS_METHODS_BSXPCSecureCoding
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_BSXPCSecureCoding
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT__UISceneHostingControllerDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_BSXPCSecureCoding
+ __OBJC_$_PROTOCOL_METHOD_TYPES__UISceneHostingControllerDelegate
+ __OBJC_$_PROTOCOL_REFS_BSXPCSecureCoding
+ __OBJC_$_PROTOCOL_REFS__UISceneHostingControllerDelegate
+ __OBJC_CLASS_RO_$_DADiagnosticsRemoteViewControllerHostToServiceAction
+ __OBJC_CLASS_RO_$_DADiagnosticsRemoteViewControllerServiceToHostAction
+ __OBJC_LABEL_PROTOCOL_$_BSXPCSecureCoding
+ __OBJC_LABEL_PROTOCOL_$__UISceneHostingControllerDelegate
+ __OBJC_METACLASS_RO_$_DADiagnosticsRemoteViewControllerHostToServiceAction
+ __OBJC_METACLASS_RO_$_DADiagnosticsRemoteViewControllerServiceToHostAction
+ __OBJC_PROTOCOL_$_BSXPCSecureCoding
+ __OBJC_PROTOCOL_$__UISceneHostingControllerDelegate
+ ___83-[DADiagnosticsRemoteViewController requestViewControllerWithHostBundleID:handler:]_block_invoke
+ ___block_descriptor_32_e8_B12?0B8l
+ ___block_literal_global.23
+ _objc_msgSend$_beginDelayingPresentation:cancellationHandler:
+ _objc_msgSend$_endDelayingPresentation
+ _objc_msgSend$actionToString:
+ _objc_msgSend$actionWithType:object:
+ _objc_msgSend$activateConstraints:
+ _objc_msgSend$addChildViewController:
+ _objc_msgSend$addSubview:
+ _objc_msgSend$boolValue
+ _objc_msgSend$bottomAnchor
+ _objc_msgSend$conformsToProtocol:
+ _objc_msgSend$constraintEqualToAnchor:
+ _objc_msgSend$decodeInt64ForKey:
+ _objc_msgSend$didMoveToParentViewController:
+ _objc_msgSend$encodeInt64:forKey:
+ _objc_msgSend$floatValue
+ _objc_msgSend$hostingController
+ _objc_msgSend$identityForEmbeddedApplicationIdentifier:
+ _objc_msgSend$info
+ _objc_msgSend$initWithInfo:responder:
+ _objc_msgSend$initWithProcessIdentity:sceneSpecification:
+ _objc_msgSend$integerValue
+ _objc_msgSend$leadingAnchor
+ _objc_msgSend$numberWithInteger:
+ _objc_msgSend$objectForKeyedSubscript:
+ _objc_msgSend$objectForSetting:
+ _objc_msgSend$prefersStatusBarHidden
+ _objc_msgSend$remoteViewControllerDidSetHostBundleIdentifier:
+ _objc_msgSend$requestViewControllerWithHostBundleID:handler:
+ _objc_msgSend$sceneViewController
+ _objc_msgSend$sendAction:
+ _objc_msgSend$setHostApplicationBundleIdentifier:
+ _objc_msgSend$setHostingController:
+ _objc_msgSend$setObject:forSetting:
+ _objc_msgSend$setTranslatesAutoresizingMaskIntoConstraints:
+ _objc_msgSend$specification
+ _objc_msgSend$topAnchor
+ _objc_msgSend$trailingAnchor
+ _objc_msgSend$view
+ _objc_msgSend$viewServiceDidEnableVolumeHUD:
+ _objc_msgSend$viewServiceDidFinishWithReason:
+ _objc_msgSend$viewServiceDidSetScreenToBrightness:animate:
+ _objc_msgSend$viewServiceDidSuspend
+ _objc_release_x26
+ _objc_release_x27
+ _objc_release_x28
+ _objc_retain_x3
- +[DADiagnosticsRemoteHostViewController exportedInterface]
- +[DADiagnosticsRemoteHostViewController serviceViewControllerInterface]
- +[DADiagnosticsRemoteViewController exportedInterface]
- +[DADiagnosticsRemoteViewController serviceViewControllerInterface]
- -[DADiagnosticsRemoteHostViewController .cxx_destruct]
- -[DADiagnosticsRemoteHostViewController _viewServiceInterface]
- -[DADiagnosticsRemoteHostViewController delegate]
- -[DADiagnosticsRemoteHostViewController originalScreenBrightness]
- -[DADiagnosticsRemoteHostViewController responder]
- -[DADiagnosticsRemoteHostViewController setDelegate:]
- -[DADiagnosticsRemoteHostViewController setOriginalScreenBrightness:]
- -[DADiagnosticsRemoteHostViewController setResponder:]
- -[DADiagnosticsRemoteHostViewController viewDidDisappear:]
- -[DADiagnosticsRemoteHostViewController viewDidLoad]
- -[DADiagnosticsRemoteHostViewController viewServiceDidEnableVolumeHUD:]
- -[DADiagnosticsRemoteHostViewController viewServiceDidSetScreenToBrightness:animate:]
- -[DADiagnosticsRemoteHostViewController viewServiceDidTerminateWithError:]
- -[DADiagnosticsRemoteViewController _viewServiceInterface]
- -[DADiagnosticsRemoteViewController viewServiceDidTerminateWithError:]
- -[DADiagnosticsRemoteViewController viewServiceDidTerminateWithError:].cold.1
- GCC_except_table10
- GCC_except_table11
- _OBJC_CLASS_$__UIRemoteViewController
- _OBJC_IVAR_$_DADiagnosticsRemoteHostViewController._delegate
- _OBJC_IVAR_$_DADiagnosticsRemoteHostViewController._originalScreenBrightness
- _OBJC_IVAR_$_DADiagnosticsRemoteHostViewController._responder
- _OBJC_METACLASS_$__UIRemoteViewController
- __OBJC_CLASS_PROTOCOLS_$_DADiagnosticsRemoteHostViewController
- ___101+[DADiagnosticsRemoteHostViewController requestDiagnosticsRemoteViewControllerWithConnectionHandler:]_block_invoke
- ___71-[DADiagnosticsRemoteHostViewController viewServiceDidEnableVolumeHUD:]_block_invoke
- ___85-[DADiagnosticsRemoteHostViewController viewServiceDidSetScreenToBrightness:animate:]_block_invoke
- ___block_descriptor_40_e8_32bs_e45_v24?0"_UIRemoteViewController"8"NSError"16ls32l8
- _objc_msgSend$_viewServiceInterface
- _objc_msgSend$requestViewController:fromServiceWithBundleIdentifier:connectionHandler:
- _objc_msgSend$serviceViewControllerProxy
- _objc_retainBlock
- _objc_sync_enter
- _objc_sync_exit
- _objc_unsafeClaimAutoreleasedReturnValue
- _requestDiagnosticsRemoteViewControllerWithConnectionHandler:.alreadyRequestingController
CStrings:
+ ""
+ "$"
+ "%s Action object animate type is incorrect, received: %@, expected: %@. Ignoring action"
+ "%s Action object brightness type is incorrect, received: %@, expected: %@. Ignoring action"
+ "%s Action object type is incorrect, received: %@, expected: %@. Ignoring action"
+ "%s Created %@ action with object %@"
+ "%s Received %@ action"
+ "%s Received %@ action with object %@"
+ "+[DADiagnosticsRemoteViewControllerHostToServiceAction actionWithType:object:]"
+ "+[DADiagnosticsRemoteViewControllerServiceToHostAction actionWithType:object:]"
+ "-[DADiagnosticsRemoteViewControllerHostToServiceAction performActionForHostedWindowScene:]"
+ "-[DADiagnosticsRemoteViewControllerServiceToHostAction performActionForSceneController:]"
+ "@\"_UISceneHostingController\""
+ "@24@0:8@\"<BSXPCDecoding>\"16"
+ "@24@0:8q16"
+ "@32@0:8q16@24"
+ "B12@?0B8"
+ "BSXPCSecureCoding"
+ "DADiagnosticsRemoteViewControllerFinishReasonCompleted"
+ "DADiagnosticsRemoteViewControllerFinishReasonExceededRetryLimit"
+ "DADiagnosticsRemoteViewControllerFinishReasonFailed"
+ "DADiagnosticsRemoteViewControllerFinishReasonUserSelectedCompleteInStore"
+ "DADiagnosticsRemoteViewControllerFinishReasonWatchLocked"
+ "DADiagnosticsRemoteViewControllerFinishReasonWatchNotConnected"
+ "DADiagnosticsRemoteViewControllerFinishReasonWatchNotPaired"
+ "DADiagnosticsRemoteViewControllerHostToServiceAction"
+ "DADiagnosticsRemoteViewControllerServiceToHostAction"
+ "HostToServiceActionTypeRemoteViewControllerDidDisappear"
+ "HostToServiceActionTypeSetHostBundleIdentifier"
+ "HostToServiceActionTypeSetRequiredSerialNumbers"
+ "HostToServiceActionTypeSetSelectableSerialNumbers"
+ "HostToServiceActionTypeSetSessionToken"
+ "HostToServiceActionTypeSetStartingFlow"
+ "ServiceToHostActionTypeDidEnableVolumeHUD"
+ "ServiceToHostActionTypeDidFinish"
+ "ServiceToHostActionTypeDidSetScreenToBrightness"
+ "ServiceToHostActionTypeDidSuspend"
+ "T@\"NSString\",&,N,V_hostApplicationBundleIdentifier"
+ "T@\"_UISceneHostingController\",&,N,V_hostingController"
+ "TB,V_finished"
+ "_UISceneHostingControllerDelegate"
+ "_beginDelayingPresentation:cancellationHandler:"
+ "_endDelayingPresentation"
+ "_hostApplicationBundleIdentifier"
+ "_hostingController"
+ "actionToString:"
+ "actionWithType:object:"
+ "activateConstraints:"
+ "addChildViewController:"
+ "addSubview:"
+ "animate"
+ "boolValue"
+ "bottomAnchor"
+ "brightness"
+ "clientIsReady"
+ "com.apple.purplebuddy"
+ "constraintEqualToAnchor:"
+ "decodeInt64ForKey:"
+ "didMoveToParentViewController:"
+ "encodeInt64:forKey:"
+ "encodeWithBSXPCCoder:"
+ "floatValue"
+ "hostApplicationBundleIdentifier"
+ "hostingController"
+ "identityForEmbeddedApplicationIdentifier:"
+ "info"
+ "initWithBSXPCCoder:"
+ "initWithInfo:responder:"
+ "initWithProcessIdentity:sceneSpecification:"
+ "integerValue"
+ "leadingAnchor"
+ "numberWithInteger:"
+ "objectForKeyedSubscript:"
+ "objectForSetting:"
+ "performActionForHostedWindowScene:"
+ "performActionForSceneController:"
+ "prefersStatusBarHidden"
+ "remoteViewControllerDidSetHostBundleIdentifier:"
+ "requestViewControllerWithHostBundleID:handler:"
+ "sceneViewController"
+ "sendAction:"
+ "setHostApplicationBundleIdentifier:"
+ "setHostingController:"
+ "setObject:forSetting:"
+ "setTranslatesAutoresizingMaskIntoConstraints:"
+ "specification"
+ "supportsBSXPCSecureCoding"
+ "topAnchor"
+ "trailingAnchor"
+ "v24@0:8@\"<BSXPCEncoding>\"16"
+ "view"
- "\""
- "%s error: %@"
- "-[DADiagnosticsRemoteViewController viewServiceDidTerminateWithError:]"
- "@\"<DADiagnosticsRemoteDelegate>\""
- "@24@0:8@?16"
- "DARootViewController"
- "T@\"<DADiagnosticsRemoteDelegate>\",W,N,V_delegate"
- "TB,N,V_finished"
- "_viewServiceInterface"
- "exportedInterface"
- "requestViewController:fromServiceWithBundleIdentifier:connectionHandler:"
- "serviceViewControllerInterface"
- "serviceViewControllerProxy"
- "v24@?0@\"_UIRemoteViewController\"8@\"NSError\"16"
- "viewServiceDidTerminateWithError:"

```
