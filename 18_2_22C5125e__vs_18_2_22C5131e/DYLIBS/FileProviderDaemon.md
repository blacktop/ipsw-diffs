## FileProviderDaemon

> `/System/Library/PrivateFrameworks/FileProviderDaemon.framework/FileProviderDaemon`

```diff

-2732.60.111.0.0
-  __TEXT.__text: 0xcfd50
-  __TEXT.__auth_stubs: 0x1220
-  __TEXT.__objc_methlist: 0x5498
+2732.60.126.0.0
+  __TEXT.__text: 0xcfd60
+  __TEXT.__auth_stubs: 0x11f0
+  __TEXT.__objc_methlist: 0x5508
   __TEXT.__const: 0x1f8
-  __TEXT.__cstring: 0xd0ae
-  __TEXT.__oslogstring: 0xdf58
+  __TEXT.__cstring: 0xd072
+  __TEXT.__oslogstring: 0xe061
   __TEXT.__gcc_except_tab: 0xd4c0
   __TEXT.__ustring: 0x1922
   __TEXT.__dlopen_cstrs: 0x50
-  __TEXT.__unwind_info: 0x39f8
-  __TEXT.__objc_classname: 0xa71
-  __TEXT.__objc_methname: 0x15a0b
-  __TEXT.__objc_methtype: 0x54ac
+  __TEXT.__unwind_info: 0x39f0
+  __TEXT.__objc_classname: 0xa72
+  __TEXT.__objc_methname: 0x15d71
+  __TEXT.__objc_methtype: 0x5533
   __TEXT.__objc_stubs: 0xe340
-  __DATA_CONST.__got: 0x848
-  __DATA_CONST.__const: 0x3a50
+  __DATA_CONST.__got: 0x818
+  __DATA_CONST.__const: 0x3a30
   __DATA_CONST.__objc_classlist: 0x268
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x140
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x43e0
+  __DATA_CONST.__objc_selrefs: 0x4410
   __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__objc_superrefs: 0x208
   __DATA_CONST.__objc_arraydata: 0xc8
-  __AUTH_CONST.__auth_got: 0x920
+  __AUTH_CONST.__auth_got: 0x908
   __AUTH_CONST.__auth_ptr: 0x8
-  __AUTH_CONST.__const: 0xa60
-  __AUTH_CONST.__cfstring: 0x5ea0
-  __AUTH_CONST.__objc_const: 0x12620
+  __AUTH_CONST.__const: 0xa20
+  __AUTH_CONST.__cfstring: 0x5e80
+  __AUTH_CONST.__objc_const: 0x12790
   __AUTH_CONST.__objc_arrayobj: 0x90
   __AUTH_CONST.__objc_intobj: 0xf0
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH.__objc_data: 0x9b0
-  __DATA.__objc_ivar: 0x950
+  __DATA.__objc_ivar: 0x964
   __DATA.__data: 0xf10
-  __DATA.__bss: 0xf0
+  __DATA.__bss: 0xe0
   __DATA_DIRTY.__objc_data: 0xe60
   __DATA_DIRTY.__data: 0x8
   __DATA_DIRTY.__bss: 0x148

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libprequelite.dylib
-  Functions: 3539
-  Symbols:   4436
-  CStrings:  5995
+  Functions: 3551
+  Symbols:   4441
+  CStrings:  6014
 
Symbols:
- _CFRelease
- _CFUserNotificationCreate
- _CFUserNotificationReceiveResponse
- _kCFAllocatorDefault
- _kCFUserNotificationAlertHeaderKey
- _kCFUserNotificationAlertMessageKey
- _kCFUserNotificationAlternateButtonTitleKey
- _kCFUserNotificationDefaultButtonTitleKey
- _kCFUserNotificationOtherButtonTitleKey
CStrings:
+ "\x01\xf03q\x81"
+ "-[FPDXPCServicer triggerDiagnosticsFor:triggeringError:uiOnly:completionHandler:]"
+ "-[FPDXPCServicer triggerDiagnosticsFor:triggeringError:uiOnly:completionHandler:]_block_invoke"
+ "T@\"NSString\",R,N,V_targetedSPSErrorsPayload"
+ "Tq,R,N,V_spsFeedbackBackoffAfterOtherResponsesInSeconds"
+ "Tq,R,N,V_spsFeedbackBackoffAfterOtherResponses_MultipleAttempts_InSeconds"
+ "Tq,R,N,V_spsFeedbackBackoffAfterSayingYesInSeconds"
+ "Tq,R,N,V_spsFeedbackRequestPromptTimeoutInSeconds"
+ "[DEBUG] 🧹 No backend for sendDiagnosticsForItemIDs"
+ "[ERROR] XPCServicer triggerTTRFor, returned non-yes result"
+ "[ERROR] launchFeedbackForProvider not supported in dead end"
+ "[ERROR] launchFeedbackForProvider not supported in extension backend"
+ "[ERROR] triggerFeedbackApprovalRequest not supported in dead end backend"
+ "[ERROR] triggerFeedbackApprovalRequest not supported in extension backend"
+ "[]"
+ "_spsFeedbackBackoffAfterOtherResponsesInSeconds"
+ "_spsFeedbackBackoffAfterOtherResponses_MultipleAttempts_InSeconds"
+ "_spsFeedbackBackoffAfterSayingYesInSeconds"
+ "_spsFeedbackRequestPromptTimeoutInSeconds"
+ "_targetedSPSErrorsPayload"
+ "launchFeedbackForDomain:itemIdentifier:triggeringError:completionHandler:"
+ "sendDiagnosticsForItemIDs:"
+ "sendDiagnosticsFromFPCKForItemIDs:"
+ "spsFeedbackBackoffAfterOtherResponsesInSeconds"
+ "spsFeedbackBackoffAfterOtherResponses_MultipleAttempts_InSeconds"
+ "spsFeedbackBackoffAfterSayingYesInSeconds"
+ "spsFeedbackRequestPromptTimeoutInSeconds"
+ "targetedSPSErrorsPayload"
+ "triggerDiagnosticsFor:triggeringError:uiOnly:completionHandler:"
+ "triggerFeedbackApprovalRequestForItemURL:domain:uiOnly:completionHandler:"
+ "v44@0:8@\"NSURL\"16@\"FPDDomain\"24B32@?<v@?B>36"
+ "v44@0:8@\"NSURL\"16@\"NSError\"24B32@?<v@?@\"NSError\">36"
+ "v44@0:8@16@24B32@?36"
+ "v48@0:8@\"FPDDomain\"16@\"NSString\"24@\"NSError\"32@?<v@?@\"NSError\">40"
- "\x01\xf03q"
- "-[FPDXPCServicer triggerTTFFor:triggeringError:completionHandler:]"
- "-[FPDXPCServicer triggerTTFFor:triggeringError:completionHandler:]_block_invoke"
- "-[FPDXPCServicer triggerTTFFor:triggeringError:completionHandler:]_block_invoke_2"
- "FileProvider-Feedback-prompt"
- "TTF_PROMPT_%!@(MISSING)_%!@(MISSING)"
- "TTF_PROMPT_ALTERNATE"
- "TTF_PROMPT_DEFAULT"
- "TTF_PROMPT_ICLOUDDRIVE_%!@(MISSING)"
- "TTF_PROMPT_OTHER"
- "TTF_PROMPT_TITLE"
- "URLWithString:"
- "[DEBUG] 🧹 No backend for sendTTRForItemIDs"
- "[ERROR] Opening the app failed: %!@(MISSING)"
- "[INFO] Will spawn feedback UI with URL: %!@(MISSING)"
- "fileprovider-feedback://gather-feedback?provider=%!@(MISSING)&domain=%!@(MISSING)&itemid=%!@(MISSING)&error=%!@(MISSING):%!l(MISSING)d"
- "openURL:configuration:completionHandler:"
- "sendTTRForItemIDs:"
- "triggerTTFFor:triggeringError:completionHandler:"
- "v40@0:8@\"NSURL\"16@\"NSError\"24@?<v@?@\"NSError\">32"

```
