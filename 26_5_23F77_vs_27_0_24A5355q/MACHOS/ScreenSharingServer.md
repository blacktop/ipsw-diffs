## ScreenSharingServer

> `/System/Library/CoreServices/ScreenSharingServer.app/ScreenSharingServer`

```diff

-144.1.0.0.0
-  __TEXT.__text: 0x44308
-  __TEXT.__auth_stubs: 0xe00
-  __TEXT.__objc_stubs: 0x45e0
-  __TEXT.__objc_methlist: 0x1cfc
+166.10.0.0.0
+  __TEXT.__text: 0x3f8e0
+  __TEXT.__auth_stubs: 0xe40
+  __TEXT.__objc_stubs: 0x4760
+  __TEXT.__objc_methlist: 0x1d94
   __TEXT.__const: 0xf2
-  __TEXT.__objc_methname: 0x5f28
-  __TEXT.__cstring: 0xb64e
-  __TEXT.__oslogstring: 0x7495
-  __TEXT.__objc_classname: 0x2c8
-  __TEXT.__objc_methtype: 0x3183
-  __TEXT.__gcc_except_tab: 0x3e0
-  __TEXT.__unwind_info: 0x5a8
-  __DATA_CONST.__auth_got: 0x710
-  __DATA_CONST.__got: 0x3f0
-  __DATA_CONST.__const: 0x678
-  __DATA_CONST.__cfstring: 0x1d80
+  __TEXT.__objc_methname: 0x6160
+  __TEXT.__cstring: 0xb69e
+  __TEXT.__oslogstring: 0x7539
+  __TEXT.__objc_classname: 0x2a7
+  __TEXT.__objc_methtype: 0x322c
+  __TEXT.__gcc_except_tab: 0x3c4
+  __TEXT.__unwind_info: 0x560
+  __DATA_CONST.__const: 0x610
+  __DATA_CONST.__cfstring: 0x1d60
   __DATA_CONST.__objc_classlist: 0x68
   __DATA_CONST.__objc_catlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x70
+  __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x58
   __DATA_CONST.__objc_arraydata: 0x148
   __DATA_CONST.__objc_arrayobj: 0x48
   __DATA_CONST.__objc_intobj: 0x60
   __DATA_CONST.__objc_dictobj: 0x78
-  __DATA.__objc_const: 0x2680
-  __DATA.__objc_selrefs: 0x1698
-  __DATA.__objc_ivar: 0x1fc
+  __DATA_CONST.__auth_got: 0x730
+  __DATA_CONST.__got: 0x3f0
+  __DATA.__objc_const: 0x2740
+  __DATA.__objc_selrefs: 0x1718
+  __DATA.__objc_ivar: 0x200
   __DATA.__objc_data: 0x410
-  __DATA.__data: 0x590
+  __DATA.__data: 0x5f0
   __DATA.__bss: 0x338
   __DATA.__common: 0x19
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration
   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
   - /System/Library/PrivateFrameworks/MobileWiFi.framework/MobileWiFi
+  - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
   - /System/Library/PrivateFrameworks/SettingsCellular.framework/SettingsCellular
   - /System/Library/PrivateFrameworks/SettingsCellularUI.framework/SettingsCellularUI
   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 44F8D221-5667-3DAC-A528-1236F930E5D7
-  Functions: 616
-  Symbols:   365
-  CStrings:  3569
+  UUID: 84E1CBC0-6929-30D5-A351-E27CAAFF968D
+  Functions: 619
+  Symbols:   369
+  CStrings:  3591
 
Symbols:
+ _OBJC_CLASS_$_RBSProcessIdentity
+ _OBJC_CLASS_$_SBSRemoteAlertActivationContext
+ _OBJC_CLASS_$_SBSRemoteAlertConfigurationContext
+ _OBJC_CLASS_$_SBSRemoteAlertDefinition
+ _OBJC_CLASS_$_SBSRemoteAlertHandle
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x3
+ _objc_retain_x4
+ _objc_retain_x5
- _SBSUIActivateRemoteAlertWithLifecycleNotifications
- _SBSUIRemoteAlertOptionDisableFadeInAnimation
- _SBSUIRemoteAlertOptionDismissWithHomeButton
- _SBSUIRemoteAlertOptionStatusBarStyle
- _SBSUIRemoteAlertOptionUserInfo
- _SBSUIRemoteAlertOptionViewControllerClass
- _objc_retainAutoreleasedReturnValue
CStrings:
+ "-[IDSServiceEmbeddedController terminateViewServiceProcess]"
+ "-[IDSSessionEmbeddedControllerAppleCare handleRemoteAlertTermination]"
+ "-[IDSSessionEmbeddedControllerAppleCare remoteAlertHandle:didInvalidateWithError:]"
+ "-[IDSSessionEmbeddedControllerAppleCare remoteAlertHandleDidDeactivate:]"
+ "@\"SBSRemoteAlertHandle\""
+ "Activated SwiftUI TermsAndConditionsViewService using SBSRemoteAlertHandle"
+ "Remote alert handle did deactivate for session %s"
+ "Remote alert handle did invalidate for session %s, error: %s"
+ "Remote alert terminated"
+ "SBSRemoteAlertHandleObserver"
+ "T@\"SBSRemoteAlertHandle\",&,N,V_remoteAlertHandle"
+ "ViewService not active"
+ "[%s:%d] Activated SwiftUI TermsAndConditionsViewService using SBSRemoteAlertHandle"
+ "[%s:%d] Remote alert handle did deactivate for session %s"
+ "[%s:%d] Remote alert handle did invalidate for session %s, error: %s"
+ "[%s:%d] Remote alert terminated"
+ "[%s:%d] ViewService not active"
+ "[%s:%d] kill ViewService process %d"
+ "_remoteAlertHandle"
+ "activateWithContext:"
+ "cleanUpRemoteAlertIfNecessary"
+ "com.apple.screensharing.TermsAndConditionsViewService"
+ "handleRemoteAlertTermination"
+ "identityForApplicationJobLabel:"
+ "initWithSceneProvidingProcess:configurationIdentifier:"
+ "kill ViewService process %d"
+ "newHandleWithDefinition:configurationContext:"
+ "registerObserver:"
+ "remoteAlertHandle"
+ "remoteAlertHandle:didInvalidateWithError:"
+ "remoteAlertHandleDidActivate:"
+ "remoteAlertHandleDidDeactivate:"
+ "screenCapture:didUpdateProtectionOptions:success:error:"
+ "sendSessionInfoToClientIfNeeded"
+ "setRemoteAlertHandle:"
+ "setUserInfo:"
+ "terminateViewServiceProcess"
+ "unregisterObserver:"
+ "v24@0:8@\"SBSRemoteAlertHandle\"16"
+ "v32@0:8@\"SBSRemoteAlertHandle\"16@\"NSError\"24"
+ "v44@0:8@\"AVCScreenCapture\"16Q24B32@\"NSError\"36"
+ "v44@0:8@16Q24B32@36"
- "-[IDSSessionEmbeddedControllerAppleCare showUserTermsAndConditions]_block_invoke"
- "-[IDSSessionEmbeddedControllerAppleCare showUserTermsAndConditions]_block_invoke_2"
- "-[IDSSessionEmbeddedControllerShareSettings showUserTermsAndConditions]"
- "-[IDSSessionEmbeddedControllerShareSettings showUserTermsAndConditions]_block_invoke"
- "-[IDSSessionEmbeddedControllerShareSettings showUserTermsAndConditions]_block_invoke_2"
- "RemoteAlert: %d"
- "TermsConditionsViewController"
- "[%s:%d] RemoteAlert: %d"
- "[%s:%d] activated:%d"
- "[%s:%d] deactivated:%d"
- "[%s:%d] show share settings terms and conditions"
- "[%s:%d] terms were accepted"
- "activated:%d"
- "com.apple.ScreenSharingViewService"
- "deactivated:%d"
- "sendSessionInfoToClient"
- "show share settings terms and conditions"
- "terms were accepted"

```
