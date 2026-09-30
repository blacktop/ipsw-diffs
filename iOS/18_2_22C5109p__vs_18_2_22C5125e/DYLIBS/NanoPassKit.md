## NanoPassKit

> `/System/Library/PrivateFrameworks/NanoPassKit.framework/NanoPassKit`

```diff

-1216.1.0.0.0
-  __TEXT.__text: 0x241b70
+1216.6.1.0.0
+  __TEXT.__text: 0x2423d4
   __TEXT.__auth_stubs: 0x1d70
-  __TEXT.__objc_methlist: 0x22a94
-  __TEXT.__cstring: 0x177e2
+  __TEXT.__objc_methlist: 0x22ad4
+  __TEXT.__cstring: 0x17982
   __TEXT.__const: 0x71c
-  __TEXT.__oslogstring: 0x2b80c
-  __TEXT.__gcc_except_tab: 0x6acc
+  __TEXT.__oslogstring: 0x2b95c
+  __TEXT.__gcc_except_tab: 0x6ad0
   __TEXT.__dlopen_cstrs: 0x2eb
   __TEXT.__ustring: 0x160
   __TEXT.__constg_swiftt: 0x1c0

   __TEXT.__swift5_proto: 0x24
   __TEXT.__swift5_assocty: 0x30
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0x8c70
+  __TEXT.__unwind_info: 0x8c98
   __TEXT.__eh_frame: 0x310
-  __TEXT.__objc_classname: 0x6ba6
-  __TEXT.__objc_methname: 0x3f1de
-  __TEXT.__objc_methtype: 0xa29a
-  __TEXT.__objc_stubs: 0x21d00
+  __TEXT.__objc_classname: 0x6ba9
+  __TEXT.__objc_methname: 0x3f422
+  __TEXT.__objc_methtype: 0xa33f
+  __TEXT.__objc_stubs: 0x21d80
   __DATA_CONST.__got: 0x1e68
-  __DATA_CONST.__const: 0x6d50
+  __DATA_CONST.__const: 0x6d70
   __DATA_CONST.__objc_classlist: 0x11d8
   __DATA_CONST.__objc_catlist: 0xe8
   __DATA_CONST.__objc_protolist: 0x278
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xbfb0
+  __DATA_CONST.__objc_selrefs: 0xbfe8
   __DATA_CONST.__objc_protorefs: 0x90
   __DATA_CONST.__objc_superrefs: 0x1108
   __DATA_CONST.__objc_arraydata: 0x88
   __AUTH_CONST.__auth_got: 0xec8
   __AUTH_CONST.__auth_ptr: 0xc8
   __AUTH_CONST.__const: 0x1218
-  __AUTH_CONST.__cfstring: 0xeb00
-  __AUTH_CONST.__objc_const: 0x4a100
+  __AUTH_CONST.__cfstring: 0xebe0
+  __AUTH_CONST.__objc_const: 0x4a1a8
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH_CONST.__objc_intobj: 0x1f8
   __AUTH_CONST.__objc_doubleobj: 0x70
   __AUTH_CONST.__objc_dictobj: 0xc8
   __AUTH.__objc_data: 0xb1d0
   __AUTH.__data: 0x180
-  __DATA.__objc_ivar: 0x1c40
+  __DATA.__objc_ivar: 0x1c48
   __DATA.__data: 0x1ef0
   __DATA.__bss: 0x898
   __DATA.__common: 0x98

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 14217
-  Symbols:   16302
-  CStrings:  15098
+  Functions: 14227
+  Symbols:   16310
+  CStrings:  15123
 
CStrings:
+ "\x11\x11"
+ "-[NPKPaymentWebServiceCompanionTargetDevice _paymentWebService:presentStandaloneTransaction:forPassUniqueIdentifier:terminalReaderIdentifier:validUntilDate:completion:]"
+ "Error: [NanoPassdXPC] Handling legacy express mode enabled codepath for pass unique ID: %!@(MISSING)"
+ "HOME_KEY_BOTH_EXPRESS_ENABLED_OPT_OUT_NOTIFICATION_MESSAGE_WATCH"
+ "HOME_KEY_UWB_EXPRESS_ENABLED_OPT_OUT_NOTIFICATION_MESSAGE_WATCH"
+ "HOME_KEY_UWB_EXPRESS_ENABLED_OPT_OUT_NOTIFICATION_TITLE_WATCH"
+ "NPKNanoPassbookUserNotificationTypeNFCExpressModeEnabled"
+ "NPKNanoPassbookUserNotificationTypeNfcAndUwbExpressModeEnabled"
+ "NPKNanoPassbookUserNotificationTypeUWBExpressModeEnabled"
+ "Notice: NPKCompanionAgentConnection (%!@(MISSING)): Present standalone transaction of type %!l(MISSING)d for pass %!@(MISSING) readerID %!@(MISSING) completion %!@(MISSING)"
+ "Notice: Target device (%!@(MISSING)) - present standalone transaction %!l(MISSING)u for pass unique ID %!@(MISSING) reader ID %!@(MISSING) with completion %!@(MISSING)"
+ "Notice: [NanoPassdXPC] Connection finished addUserNotificationForEnabledExpressMode: %!l(MISSING)u, passUniqueID: %!@(MISSING), error?: %!@(MISSING)"
+ "Notice: [NanoPassdXPC] Connection finished addUserNotificationOfType: %!l(MISSING)u, passUniqueID: %!@(MISSING), error?: %!@(MISSING)"
+ "Notice: [NanoPassdXPC] Connection started addUserNotificationForEnabledExpressMode: %!l(MISSING)u, pass unique ID: %!@(MISSING)"
+ "Notice: [NanoPassdXPC] Request to add user notification of type: %!@(MISSING) for passUniqueID: %!@(MISSING)"
+ "T@\"NSString\",&,N,V_terminalReaderIdentifier"
+ "_addLegacyExpressModeEnabledUserNotificationForPassUniqueID:completion:"
+ "_expressNotificationType"
+ "_paymentWebService:presentStandaloneTransaction:forPassUniqueIdentifier:terminalReaderIdentifier:validUntilDate:completion:"
+ "_terminalReaderIdentifier"
+ "addUserNotificationForEnabledExpressMode:passUniqueID:completion:"
+ "hasTerminalReaderIdentifier"
+ "initWithPass:expressNotificationType:"
+ "paymentAuthorizationController:didRequestMerchantSessionWithURL:merchantSessionUpdate:"
+ "paymentWebService:presentStandaloneTransaction:forPassUniqueIdentifier:terminalReaderIdentifier:completion:"
+ "presentStandaloneTransaction:forPassUniqueIdentifier:terminalReaderIdentifier:completion:"
+ "setTerminalReaderIdentifier:"
+ "terminalReaderIdentifier"
+ "v40@0:8@\"PKPaymentAuthorizationController\"16@\"NSURL\"24@?<v@?@\"PKPaymentRequestMerchantSessionUpdate\">32"
+ "v48@0:8q16@\"NSString\"24@\"NSString\"32@?<v@?B>40"
+ "v48@0:8q16@24@32@?40"
+ "v64@0:8@16q24@32@40@48@?56"
- "-[NPKPaymentWebServiceCompanionTargetDevice _paymentWebService:presentStandaloneTransaction:forPassUniqueIdentifier:validUntilDate:completion:]"
- "Notice: NPKCompanionAgentConnection (%!@(MISSING)): Present standalone transaction of type %!l(MISSING)d for pass %!@(MISSING) with completion %!@(MISSING)"
- "Notice: Target device (%!@(MISSING)) - present standalone transaction %!l(MISSING)u for pass unique ID %!@(MISSING) with completion %!@(MISSING)"
- "Notice: [NanoPassdXPC] Connection finished addUserNotificationOfType: %!@(MISSING), passUniqueID: %!@(MISSING), error?: %!@(MISSING)"
- "Notice: [NanoPassdXPC] Connection started addUserNotificationOfType: %!@(MISSING), pass unique ID: %!@(MISSING)"
- "_paymentWebService:presentStandaloneTransaction:forPassUniqueIdentifier:validUntilDate:completion:"
- "paymentWebService:presentStandaloneTransaction:forPassUniqueIdentifier:completion:"
- "v40@0:8q16@\"NSString\"24@?<v@?B>32"

```
