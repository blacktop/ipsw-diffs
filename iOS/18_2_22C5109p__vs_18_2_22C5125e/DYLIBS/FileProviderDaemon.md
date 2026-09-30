## FileProviderDaemon

> `/System/Library/PrivateFrameworks/FileProviderDaemon.framework/FileProviderDaemon`

```diff

-2732.60.87.502.1
-  __TEXT.__text: 0xceea0
-  __TEXT.__auth_stubs: 0x11f0
-  __TEXT.__objc_methlist: 0x5488
+2732.60.111.0.0
+  __TEXT.__text: 0xcfd50
+  __TEXT.__auth_stubs: 0x1220
+  __TEXT.__objc_methlist: 0x5498
   __TEXT.__const: 0x1f8
-  __TEXT.__cstring: 0xcf6e
-  __TEXT.__oslogstring: 0xdfad
-  __TEXT.__gcc_except_tab: 0xd35c
+  __TEXT.__cstring: 0xd0ae
+  __TEXT.__oslogstring: 0xdf58
+  __TEXT.__gcc_except_tab: 0xd4c0
   __TEXT.__ustring: 0x1922
   __TEXT.__dlopen_cstrs: 0x50
-  __TEXT.__unwind_info: 0x39c0
+  __TEXT.__unwind_info: 0x39f8
   __TEXT.__objc_classname: 0xa71
-  __TEXT.__objc_methname: 0x159a2
-  __TEXT.__objc_methtype: 0x547b
-  __TEXT.__objc_stubs: 0xe300
-  __DATA_CONST.__got: 0x828
-  __DATA_CONST.__const: 0x39e0
+  __TEXT.__objc_methname: 0x15a0b
+  __TEXT.__objc_methtype: 0x54ac
+  __TEXT.__objc_stubs: 0xe340
+  __DATA_CONST.__got: 0x848
+  __DATA_CONST.__const: 0x3a50
   __DATA_CONST.__objc_classlist: 0x268
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x140
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x43c8
+  __DATA_CONST.__objc_selrefs: 0x43e0
   __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__objc_superrefs: 0x208
   __DATA_CONST.__objc_arraydata: 0xc8
-  __AUTH_CONST.__auth_got: 0x908
+  __AUTH_CONST.__auth_got: 0x920
   __AUTH_CONST.__auth_ptr: 0x8
-  __AUTH_CONST.__const: 0xa40
-  __AUTH_CONST.__cfstring: 0x5e20
-  __AUTH_CONST.__objc_const: 0x12600
+  __AUTH_CONST.__const: 0xa60
+  __AUTH_CONST.__cfstring: 0x5ea0
+  __AUTH_CONST.__objc_const: 0x12620
   __AUTH_CONST.__objc_arrayobj: 0x90
   __AUTH_CONST.__objc_intobj: 0xf0
   __AUTH_CONST.__objc_dictobj: 0x50
-  __AUTH.__objc_data: 0xa50
+  __AUTH.__objc_data: 0x9b0
   __DATA.__objc_ivar: 0x950
   __DATA.__data: 0xf10
-  __DATA.__bss: 0xe8
-  __DATA_DIRTY.__objc_data: 0xdc0
+  __DATA.__bss: 0xf0
+  __DATA_DIRTY.__objc_data: 0xe60
   __DATA_DIRTY.__data: 0x8
-  __DATA_DIRTY.__bss: 0x140
+  __DATA_DIRTY.__bss: 0x148
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CloudKit.framework/CloudKit
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libprequelite.dylib
-  Functions: 3533
-  Symbols:   4423
-  CStrings:  5983
+  Functions: 3539
+  Symbols:   4436
+  CStrings:  5995
 
Symbols:
+ _CFRelease
+ _CFUserNotificationCreate
+ _CFUserNotificationReceiveResponse
+ _fpfs_supports_tap_to_feedback
+ _kCFAllocatorDefault
+ _kCFUserNotificationAlertHeaderKey
+ _kCFUserNotificationAlertMessageKey
+ _kCFUserNotificationAlternateButtonTitleKey
+ _kCFUserNotificationDefaultButtonTitleKey
+ _kCFUserNotificationOtherButtonTitleKey
- _EXExtensionKitErrorDomain
- __dispatch_main_q
- _dispatch_after
CStrings:
+ "-[FPDXPCServicer triggerTTFFor:triggeringError:completionHandler:]"
+ "-[FPDXPCServicer triggerTTFFor:triggeringError:completionHandler:]_block_invoke"
+ "-[FPDXPCServicer triggerTTFFor:triggeringError:completionHandler:]_block_invoke_2"
+ "FileProvider-Feedback-prompt"
+ "TTF_PROMPT_%!@(MISSING)_%!@(MISSING)"
+ "TTF_PROMPT_ALTERNATE"
+ "TTF_PROMPT_DEFAULT"
+ "TTF_PROMPT_ICLOUDDRIVE_%!@(MISSING)"
+ "TTF_PROMPT_OTHER"
+ "TTF_PROMPT_TITLE"
+ "URLWithString:"
+ "[ERROR] Opening the app failed: %!@(MISSING)"
+ "[INFO] Will spawn feedback UI with URL: %!@(MISSING)"
+ "fileprovider-feedback://gather-feedback?provider=%!@(MISSING)&domain=%!@(MISSING)&itemid=%!@(MISSING)&error=%!@(MISSING):%!l(MISSING)d"
+ "openURL:configuration:completionHandler:"
+ "triggerTTFFor:triggeringError:completionHandler:"
+ "v40@0:8@\"NSURL\"16@\"NSError\"24@?<v@?@\"NSError\">32"
- "Failed to create XPC connection"
- "Failed to create new XPC connection for provider %!@(MISSING)\nError: %!@(MISSING)"
- "[ERROR] Exiting after an unrecoverable extension launch error was detected."
- "[ERROR] Exiting with delay after an unrecoverable extension launch error was detected."
- "a problem launching an extension was detected"

```
