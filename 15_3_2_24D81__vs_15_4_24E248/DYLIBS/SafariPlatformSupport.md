## SafariPlatformSupport

> `/System/Library/PrivateFrameworks/SafariPlatformSupport.framework/Versions/A/SafariPlatformSupport`

```diff

-620.2.4.11.6
-  __TEXT.__text: 0x6600
+621.1.15.11.10
+  __TEXT.__text: 0x6a58
   __TEXT.__auth_stubs: 0x230
-  __TEXT.__objc_methlist: 0x524
-  __TEXT.__cstring: 0x401
+  __TEXT.__objc_methlist: 0x900
+  __TEXT.__cstring: 0x442
   __TEXT.__const: 0x50
   __TEXT.__gcc_except_tab: 0xd0
-  __TEXT.__oslogstring: 0x27a
-  __TEXT.__unwind_info: 0x220
+  __TEXT.__oslogstring: 0x346
+  __TEXT.__unwind_info: 0x238
   __TEXT.__objc_classname: 0x3b6
-  __TEXT.__objc_methname: 0x17c0
-  __TEXT.__objc_methtype: 0x65f
-  __TEXT.__objc_stubs: 0x1320
-  __DATA_CONST.__got: 0xe0
+  __TEXT.__objc_methname: 0x18fc
+  __TEXT.__objc_methtype: 0x6a4
+  __TEXT.__objc_stubs: 0x1480
+  __DATA_CONST.__got: 0xf0
   __DATA_CONST.__const: 0x48
   __DATA_CONST.__objc_classlist: 0x48
   __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x580
+  __DATA_CONST.__objc_selrefs: 0x678
   __DATA_CONST.__objc_protorefs: 0x60
-  __DATA_CONST.__objc_superrefs: 0x18
+  __DATA_CONST.__objc_superrefs: 0x20
+  __DATA_CONST.__objc_arraydata: 0x10
   __AUTH_CONST.__auth_got: 0x128
-  __AUTH_CONST.__const: 0x490
-  __AUTH_CONST.__cfstring: 0x280
-  __AUTH_CONST.__objc_const: 0x12a0
+  __AUTH_CONST.__const: 0x4c0
+  __AUTH_CONST.__cfstring: 0x2e0
+  __AUTH_CONST.__objc_const: 0xc48
+  __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0x280
   __DATA.__objc_ivar: 0x74
   __DATA.__data: 0x548

   - /System/Library/PrivateFrameworks/ViewBridge.framework/Versions/A/ViewBridge
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: D988C1DF-8DC7-32D8-BA63-DBC7DEA2CF48
-  Functions: 167
-  Symbols:   612
-  CStrings:  380
+  UUID: CB33DD47-4506-3152-B232-C024BB3D0307
+  Functions: 184
+  Symbols:   645
+  CStrings:  402
 
Symbols:
+ +[SPSafariPlatformSupport sharedPlatformSupport].cold.1
+ -[SPAutoFillAuthorizationRemoteViewController exportedInterface].cold.1
+ -[SPAutoFillAuthorizationRemoteViewController serviceViewControllerInterface].cold.1
+ -[SPCompletionListRemoteViewController exportedInterface].cold.1
+ -[SPCompletionListRemoteViewController serviceViewControllerInterface].cold.1
+ -[SPCompletionListRemoteViewController viewServiceDidTerminateWithError:]
+ -[SPOtherPasswordsRemoteViewController exportedInterface].cold.1
+ -[SPOtherPasswordsRemoteViewController serviceViewControllerInterface].cold.1
+ -[SPSafariPlatformSupport _appCanSupportOneTimeCodeModeDeliveredCodesOnly]
+ -[SPSafariPlatformSupport _observeNotificationsForTextField:keyWindow:isForOneTimeCode:]
+ -[SPSafariPlatformSupport dismissAutoFill]
+ -[SPSafariPlatformSupport displayOTPAutoFillRelativeToRect:ofView:oneTimeCodeMode:completionHandler:]
+ -[SPSafariPlatformSupport displayOTPAutoFillRelativeToRect:ofView:oneTimeCodeMode:completionHandler:].cold.1
+ -[SPSafariPlatformSupport displayOTPAutoFillRelativeToRect:ofView:oneTimeCodeMode:completionHandler:].cold.2
+ -[SPSafariPlatformSupport viewServiceDidTerminateWithError:]
+ -[SPSafariPlatformSupport viewServiceDidTerminateWithError:].cold.1
+ -[SPSystemAutoFillRemoteViewController exportedInterface].cold.1
+ -[SPSystemAutoFillRemoteViewController serviceViewControllerInterface].cold.1
+ GCC_except_table34
+ SPOSLogSafariPlatformSupport.cold.1
+ _OBJC_CLASS_$_NSBundle
+ _OBJC_CLASS_$_NSConstantArray
+ _OBJC_CLASS_$_NSSet
+ _OUTLINED_FUNCTION_2
+ __54-[SPSafariPlatformSupport showOtherPasswordsSelected:]_block_invoke.52
+ __68-[SPSafariPlatformSupport showExternalCredentialListWithIdentifier:]_block_invoke.67
+ __78-[SPSafariPlatformSupport showExternalCredentialAuthenticationWithIdentifier:]_block_invoke.79
+ __88-[SPSafariPlatformSupport _observeNotificationsForTextField:keyWindow:isForOneTimeCode:]_block_invoke.40
+ __88-[SPSafariPlatformSupport _observeNotificationsForTextField:keyWindow:isForOneTimeCode:]_block_invoke.45
+ ___101-[SPSafariPlatformSupport displayOTPAutoFillRelativeToRect:ofView:oneTimeCodeMode:completionHandler:]_block_invoke
+ ___88-[SPSafariPlatformSupport _observeNotificationsForTextField:keyWindow:isForOneTimeCode:]_block_invoke
+ ___88-[SPSafariPlatformSupport _observeNotificationsForTextField:keyWindow:isForOneTimeCode:]_block_invoke_2
+ ___block_descriptor_49_e8_32w40w_e24_v16?0"NSNotification"8l
+ ___block_descriptor_96_e8_32s40s_e32_v16?0"NSRemoteViewController"8l
+ __block_literal_global.186
+ _objc_msgSend$_appCanSupportOneTimeCodeModeDeliveredCodesOnly
+ _objc_msgSend$_observeNotificationsForTextField:keyWindow:isForOneTimeCode:
+ _objc_msgSend$bundleIdentifier
+ _objc_msgSend$containsObject:
+ _objc_msgSend$didFocusOtherTextField
+ _objc_msgSend$dismissAutoFill
+ _objc_msgSend$displayOTPAutoFillRelativeToRect:ofView:oneTimeCodeMode:completionHandler:
+ _objc_msgSend$hasPrefix:
+ _objc_msgSend$mainBundle
+ _objc_msgSend$safari_stringByTrimmingWhitespace
+ _objc_msgSend$setWithArray:
+ _objc_msgSend$viewServiceDidTerminateWithError:
+ safeUITextField.cold.1
- -[SPSafariPlatformSupport _observeNotificationsForTextField:keyWindow:]
- -[SPSafariPlatformSupport displayOTPAutoFillRelativeToRect:ofView:completionHandler:].cold.1
- -[SPSafariPlatformSupport displayOTPAutoFillRelativeToRect:ofView:completionHandler:].cold.2
- GCC_except_table33
- __54-[SPSafariPlatformSupport showOtherPasswordsSelected:]_block_invoke.50
- __68-[SPSafariPlatformSupport showExternalCredentialListWithIdentifier:]_block_invoke.65
- __71-[SPSafariPlatformSupport _observeNotificationsForTextField:keyWindow:]_block_invoke.40
- __71-[SPSafariPlatformSupport _observeNotificationsForTextField:keyWindow:]_block_invoke.45
- __78-[SPSafariPlatformSupport showExternalCredentialAuthenticationWithIdentifier:]_block_invoke.77
- ___71-[SPSafariPlatformSupport _observeNotificationsForTextField:keyWindow:]_block_invoke
- ___71-[SPSafariPlatformSupport _observeNotificationsForTextField:keyWindow:]_block_invoke_2
- ___85-[SPSafariPlatformSupport displayOTPAutoFillRelativeToRect:ofView:completionHandler:]_block_invoke
- ___block_descriptor_88_e8_32s40s_e32_v16?0"NSRemoteViewController"8l
- __block_literal_global.167
- _objc_msgSend$_observeNotificationsForTextField:keyWindow:
CStrings:
+ "-[SPSafariPlatformSupport completionListPreferredContentSizeDidUpdate] with size %{public}@"
+ "App does not support One-Time Code AutoFill for Delivered Codes Only."
+ "View service did terminate with error: %@"
+ "_appCanSupportOneTimeCodeModeDeliveredCodesOnly"
+ "_observeNotificationsForTextField:keyWindow:isForOneTimeCode:"
+ "bundleIdentifier"
+ "com.apple."
+ "com.apple.CaptiveNetworkAssistant"
+ "com.apple.shortcuts"
+ "containsObject:"
+ "didFocusOtherTextField"
+ "dismissAutoFill"
+ "displayOTPAutoFillRelativeToRect:ofView:oneTimeCodeMode:completionHandler:"
+ "hasPrefix:"
+ "mainBundle"
+ "safari_stringByTrimmingWhitespace"
+ "setWithArray:"
+ "v36@0:8@16@24B32"
+ "v72@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16@48Q56@?64"
+ "viewServiceDidTerminateWithError:"
- "_observeNotificationsForTextField:keyWindow:"

```
