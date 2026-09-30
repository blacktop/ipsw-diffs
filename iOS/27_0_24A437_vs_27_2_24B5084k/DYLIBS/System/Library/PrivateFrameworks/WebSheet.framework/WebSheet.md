## WebSheet

> `/System/Library/PrivateFrameworks/WebSheet.framework/WebSheet`

```diff

-335.0.0.0.0
-  __TEXT.__text: 0x7bbc
-  __TEXT.__objc_methlist: 0xc90
+337.0.0.0.0
+  __TEXT.__text: 0x8208
+  __TEXT.__objc_methlist: 0xcd8
   __TEXT.__const: 0x60
-  __TEXT.__cstring: 0x1586
+  __TEXT.__cstring: 0x165b
   __TEXT.__gcc_except_tab: 0x2c
-  __TEXT.__unwind_info: 0x320
+  __TEXT.__unwind_info: 0x348
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x2d0
-  __DATA_CONST.__objc_classlist: 0x38
+  __DATA_CONST.__const: 0x348
+  __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xe48
-  __DATA_CONST.__objc_superrefs: 0x20
-  __DATA_CONST.__got: 0x250
+  __DATA_CONST.__objc_selrefs: 0xe70
+  __DATA_CONST.__objc_superrefs: 0x28
+  __DATA_CONST.__got: 0x258
   __AUTH_CONST.__const: 0xe0
-  __AUTH_CONST.__cfstring: 0xb00
-  __AUTH_CONST.__objc_const: 0x14e8
+  __AUTH_CONST.__cfstring: 0xb60
+  __AUTH_CONST.__objc_const: 0x15a0
   __AUTH_CONST.__auth_got: 0x0
-  __AUTH.__objc_data: 0x230
-  __DATA.__objc_ivar: 0xe8
+  __AUTH.__objc_data: 0x280
+  __DATA.__objc_ivar: 0xec
   __DATA.__data: 0x3c0
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/WebUI.framework/WebUI
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 194
-  Symbols:   848
-  CStrings:  153
+  Functions: 205
+  Symbols:   875
+  CStrings:  157
 
Symbols:
+ -[WSSchemeApprovalCompletion .cxx_destruct]
+ -[WSSchemeApprovalCompletion completeWithApproval:]
+ -[WSSchemeApprovalCompletion dealloc]
+ -[WSSchemeApprovalCompletion initWithHandler:]
+ -[WSWebSheetView _openInBrowserTabForNavigationAction:webView:decisionHandler:]
+ -[WSWebSheetView _requestUserApprovalToOpenInApp:completion:]
+ GCC_except_table130
+ _OBJC_CLASS_$_WSSchemeApprovalCompletion
+ _OBJC_IVAR_$_WSSchemeApprovalCompletion._handler
+ _OBJC_METACLASS_$_WSSchemeApprovalCompletion
+ __OBJC_$_INSTANCE_METHODS_WSSchemeApprovalCompletion
+ __OBJC_$_INSTANCE_VARIABLES_WSSchemeApprovalCompletion
+ __OBJC_CLASS_RO_$_WSSchemeApprovalCompletion
+ __OBJC_METACLASS_RO_$_WSSchemeApprovalCompletion
+ ___61-[WSWebSheetView _requestUserApprovalToOpenInApp:completion:]_block_invoke
+ ___61-[WSWebSheetView _requestUserApprovalToOpenInApp:completion:]_block_invoke_2
+ ___61-[WSWebSheetView _requestUserApprovalToOpenInApp:completion:]_block_invoke_3
+ ___74-[WSWebSheetView webView:decidePolicyForNavigationAction:decisionHandler:]_block_invoke_3
+ ___79-[WSWebSheetView _openInBrowserTabForNavigationAction:webView:decisionHandler:]_block_invoke
+ ___79-[WSWebSheetView _openInBrowserTabForNavigationAction:webView:decisionHandler:]_block_invoke_2
+ ___block_descriptor_48_e8_32s40bs_e8_v12?0B8ls32l8s40l8
+ ___block_descriptor_56_e8_32s40s48bs_e8_v12?0B8ls48l8s32l8s40l8
+ ___block_descriptor_72_e8_32s40s48s56s64bs_e8_v12?0B8ls64l8s32l8s40l8s48l8s56l8
+ _objc_msgSend$_openInBrowserTabForNavigationAction:webView:decisionHandler:
+ _objc_msgSend$_requestUserApprovalToOpenInApp:completion:
+ _objc_msgSend$completeWithApproval:
+ _objc_msgSend$initWithHandler:
+ _objc_msgSend$presentedViewController
+ _objc_msgSend$setPreferredAction:
+ _objc_retainBlock
+ _objc_retain_x28
- -[WSWebSheetView isUserAprroved:]
- GCC_except_table119
- _CFUserNotificationDisplayAlert
- _objc_msgSend$isUserAprroved:
CStrings:
+ "openURL approval alert went away without a choice, treating as not approved"
+ "presented UIAlertController asking for approval to open in \"%@\""
+ "unable to prompt for openURL approval, treating as not approved"
+ "v12@?0B8"
```
