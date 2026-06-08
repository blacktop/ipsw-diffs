## InputUI

> `/Applications/InputUI.app/InputUI`

```diff

-96.5.0.0.0
-  __TEXT.__text: 0xce24
-  __TEXT.__auth_stubs: 0x5f0
-  __TEXT.__objc_stubs: 0x1f80
-  __TEXT.__objc_methlist: 0x2274
-  __TEXT.__objc_methname: 0x616b
-  __TEXT.__cstring: 0x654
-  __TEXT.__objc_classname: 0x35a
-  __TEXT.__objc_methtype: 0x29e2
+109.8.0.0.0
+  __TEXT.__text: 0xbffc
+  __TEXT.__auth_stubs: 0x600
+  __TEXT.__objc_stubs: 0x1f00
+  __TEXT.__objc_methlist: 0x22ac
+  __TEXT.__objc_methname: 0x6214
+  __TEXT.__cstring: 0x788
+  __TEXT.__objc_classname: 0x381
+  __TEXT.__objc_methtype: 0x2a4e
   __TEXT.__const: 0x88
-  __TEXT.__oslogstring: 0x131e
-  __TEXT.__gcc_except_tab: 0x1dc
-  __TEXT.__dlopen_cstrs: 0xa4
-  __TEXT.__unwind_info: 0x460
-  __DATA_CONST.__auth_got: 0x308
-  __DATA_CONST.__got: 0x140
-  __DATA_CONST.__const: 0x3e8
-  __DATA_CONST.__cfstring: 0x260
-  __DATA_CONST.__objc_classlist: 0x90
-  __DATA_CONST.__objc_protolist: 0xa8
+  __TEXT.__oslogstring: 0x138f
+  __TEXT.__gcc_except_tab: 0x1b4
+  __TEXT.__dlopen_cstrs: 0xf8
+  __TEXT.__unwind_info: 0x3d8
+  __DATA_CONST.__const: 0x3f8
+  __DATA_CONST.__cfstring: 0x2c0
+  __DATA_CONST.__objc_classlist: 0x98
+  __DATA_CONST.__objc_protolist: 0xb0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x58
-  __DATA.__objc_const: 0x5270
-  __DATA.__objc_selrefs: 0x1710
-  __DATA.__objc_ivar: 0x108
-  __DATA.__objc_data: 0x5a0
-  __DATA.__data: 0x7e0
-  __DATA.__bss: 0x80
+  __DATA_CONST.__auth_got: 0x310
+  __DATA_CONST.__got: 0x160
+  __DATA.__objc_const: 0x5650
+  __DATA.__objc_selrefs: 0x1738
+  __DATA.__objc_ivar: 0x104
+  __DATA.__objc_data: 0x5f0
+  __DATA.__data: 0x840
+  __DATA.__bss: 0xa8
   - /AppleInternal/Library/Frameworks/InputTeletypeService.framework/InputTeletypeService
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /System/Library/PrivateFrameworks/KeyboardArbiter.framework/KeyboardArbiter
   - /System/Library/PrivateFrameworks/RemoteTextInput.framework/RemoteTextInput
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
+  - /System/Library/PrivateFrameworks/SpringBoardUIServices.framework/SpringBoardUIServices
   - /System/Library/PrivateFrameworks/TextInput.framework/TextInput
+  - /System/Library/PrivateFrameworks/TextInputUI.framework/TextInputUI
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 649FE6C7-68F1-379F-8F80-0497C106EBC2
-  Functions: 338
-  Symbols:   158
-  CStrings:  1404
+  UUID: 1BE4E6CD-2750-3F14-A321-507517BF7949
+  Functions: 341
+  Symbols:   163
+  CStrings:  1429
 
Symbols:
+ _OBJC_CLASS_$_NSMutableSet
+ _OBJC_CLASS_$_SBSUIUserSwipedToKillAction
+ _OBJC_CLASS_$_TUIHostedInputCandidateContainerSceneDelegate
+ _OBJC_CLASS_$_TUIInputSessionManager
+ __UISceneSessionRoleSceneHosting
+ _objc_claimAutoreleasedReturnValue
+ _objc_opt_new
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x25
+ _objc_retain_x26
+ _objc_retain_x3
+ _objc_retain_x4
+ _objc_unsafeClaimAutoreleasedReturnValue
- _OBJC_CLASS_$_NSLock
- __os_signpost_emit_with_name_impl
- _dispatch_semaphore_create
- _dispatch_semaphore_signal
- _objc_autorelease
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x28
- _os_signpost_enabled
- _os_signpost_id_generate
CStrings:
+ "@\"AFUIServiceListener\""
+ "@\"NSSet\"32@0:8@\"NSSet\"16@\"FBSSceneTransitionContext\"24"
+ "@\"TUIInputSessionManager\""
+ "Context Menu Scene"
+ "Context menu scene requested"
+ "IUIUserSwipedToKillActionHandler"
+ "Initializing TUIInputUIInputManagerServer"
+ "InputSessionAppDelegate"
+ "InputUI scene: %@ willConnectToSession: %@"
+ "InputUI sceneDidBecomeActive: %@"
+ "InputUI sceneDidDisconnect: %@"
+ "InputUI sceneDidEnterBackground: %@"
+ "InputUI sceneWillEnterForeground: %@"
+ "InputUI sceneWillResignActive: %@"
+ "No context menu reqeuest..."
+ "No scene hosting, using setDelegateClass: %@"
+ "Q24@0:8@\"UIWindowScene\"16"
+ "Q24@0:8@16"
+ "Scene hosting required, using setDelegateClass: %@"
+ "Secure Prediction UI Scene"
+ "T@\"AFUIServiceListener\",R,N,V_autofillUIServiceListener"
+ "T@\"TUIInputSessionManager\",&,N,V_inputSessionManager"
+ "TUIContextMenuHostingOptionsWrapper"
+ "TUIContextMenuSceneDelegate"
+ "TextInputUI"
+ "UIKit"
+ "_UIApplicationBSActionHandler"
+ "_UIKeyboardArbiterInputUIHost"
+ "_inputSessionManager"
+ "_registerBSActionHandler:"
+ "_respondToApplicationActions:fromTransitionContext:"
+ "acknowledge"
+ "extractFromConnectionOptions:"
+ "inputSessionManager"
+ "inputui_candidate_generation_flow"
+ "intelligenceCursorEnabled"
+ "keyboard_candidate_disambiguation_ui"
+ "secure_input_candidate_hosting"
+ "set"
+ "setDelegateClass:"
+ "setInputSessionManager:"
+ "setIntelligenceCursorEnabled:"
+ "softlink:o:path:/System/Library/PrivateFrameworks/TextInputUI.framework/TextInputUI"
+ "supportedInterfaceOrientationsForWindowScene:"
+ "windowScene:didUpdateHostingOptions:"
- "%s  InputUI service is paused: calling end input session completion immediately"
- "@\"AFUSServiceListener\""
- "@\"NSLock\""
- "InputUI scene:%@ willConnectToSession:%@"
- "InputUI sceneDidBecomeActive:%@"
- "InputUI sceneDidDisconnect:%@"
- "InputUI sceneDidEnterBackground:%@"
- "InputUI sceneWillEnterForeground:%@"
- "InputUI sceneWillResignActive:%@"
- "T@\"AFUSServiceListener\",R,N,V_autofillUIServiceListener"
- "T@\"NSLock\",R,N,V_servicePausedLock"
- "TB,N,GisServicePaused,V_servicePaused"
- "_servicePaused"
- "_servicePausedLock"
- "isServicePaused"
- "lock"
- "pauseTextInputService"
- "resumeTextInputService"
- "servicePaused"
- "servicePausedLock"
- "setServicePaused:"
- "unlock"

```
