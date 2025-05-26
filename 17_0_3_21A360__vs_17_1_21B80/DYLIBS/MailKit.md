## MailKit

> `/System/Library/PrivateFrameworks/MailKit.framework/MailKit`

```diff

-3774.100.2.2.5
-  __TEXT.__text: 0x14900
+3774.200.91.2.1
+  __TEXT.__text: 0x14e44
   __TEXT.__auth_stubs: 0x520
-  __TEXT.__objc_methlist: 0x1768
-  __TEXT.__gcc_except_tab: 0x2818
-  __TEXT.__cstring: 0x115d
+  __TEXT.__objc_methlist: 0x17c0
+  __TEXT.__gcc_except_tab: 0x28b8
+  __TEXT.__cstring: 0x118c
   __TEXT.__const: 0x10
   __TEXT.__oslogstring: 0xb31
   __TEXT.__ustring: 0x3c6
-  __TEXT.__unwind_info: 0xea0
-  __TEXT.__objc_classname: 0x524
-  __TEXT.__objc_methname: 0x423b
-  __TEXT.__objc_methtype: 0xafc
-  __TEXT.__objc_stubs: 0x29c0
+  __TEXT.__unwind_info: 0xed0
+  __TEXT.__objc_classname: 0x526
+  __TEXT.__objc_methname: 0x444f
+  __TEXT.__objc_methtype: 0xb5a
+  __TEXT.__objc_stubs: 0x2a00
   __DATA_CONST.__got: 0x158
   __DATA_CONST.__const: 0x668
   __DATA_CONST.__objc_classlist: 0xf8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0xc0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x2c80
-  __DATA_CONST.__objc_selrefs: 0xe48
+  __DATA_CONST.__objc_const: 0x2d70
+  __DATA_CONST.__objc_selrefs: 0xe78
   __DATA_CONST.__objc_arraydata: 0x20
-  __AUTH_CONST.__cfstring: 0x1140
+  __AUTH_CONST.__cfstring: 0x1160
   __AUTH_CONST.__objc_const: 0x90
   __AUTH_CONST.__const: 0x40
   __AUTH_CONST.__objc_intobj: 0x60

   __DATA.__objc_protorefs: 0x18
   __DATA.__objc_classrefs: 0x1d0
   __DATA.__objc_superrefs: 0xd8
-  __DATA.__objc_ivar: 0x1e8
+  __DATA.__objc_ivar: 0x1f8
   __DATA.__data: 0x900
   __DATA.__bss: 0x88
   __DATA_DIRTY.__const: 0x220

   - /System/Library/PrivateFrameworks/PlugInKit.framework/PlugInKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 557
-  Symbols:   2518
-  CStrings:  1095
+  Functions: 565
+  Symbols:   2544
+  CStrings:  1111
 
Symbols:
+ -[MEAppExtensionsController hasSecurityExtensionsEnabled]
+ -[MEComposeExtensionsHelper shouldPerformSendValidation]
+ -[MEMessageSecurityInformation disallowUsersToLoadRemoteContent]
+ -[MEMessageSecurityInformation initWithSigners:isEncrypted:signingError:encryptionError:shouldBlockRemoteContent:disallowUsersToLoadRemoteContent:localizedRemoteContentBlockingReason:]
+ -[MEOutgoingMessageEncodingStatus initWithCanSign:canEncrypt:shouldSign:shouldEncrypt:securityError:addressesFailingEncryption:]
+ -[MEOutgoingMessageEncodingStatus shouldEncrypt]
+ -[MEOutgoingMessageEncodingStatus shouldSign]
+ -[MERemoteExtensionContext session:hasSendMessageCheckWithCompletion:]
+ _OBJC_IVAR_$_MEComposeExtensionsHelper._shouldPerformSendValidationMap
+ _OBJC_IVAR_$_MEMessageSecurityInformation._disallowUsersToLoadRemoteContent
+ _OBJC_IVAR_$_MEOutgoingMessageEncodingStatus._shouldEncrypt
+ _OBJC_IVAR_$_MEOutgoingMessageEncodingStatus._shouldSign
+ ___78-[MEComposeExtensionsHelper _dispatchMailComposeSessionDidBeginForExtensions:]_block_invoke.15
+ ___78-[MEComposeExtensionsHelper _dispatchMailComposeSessionDidBeginForExtensions:]_block_invoke.15.cold.1
+ ___86-[MEComposeExtensionsHelper initWithComposeSession:extensionsController:iconReloader:]_block_invoke.9
+ ___block_literal_global.104
+ _objc_msgSend$disallowUsersToLoadRemoteContent
+ _objc_msgSend$initWithCanSign:canEncrypt:shouldSign:shouldEncrypt:securityError:addressesFailingEncryption:
+ _objc_msgSend$initWithSigners:isEncrypted:signingError:encryptionError:shouldBlockRemoteContent:disallowUsersToLoadRemoteContent:localizedRemoteContentBlockingReason:
- ___78-[MEComposeExtensionsHelper _dispatchMailComposeSessionDidBeginForExtensions:]_block_invoke.14
- ___78-[MEComposeExtensionsHelper _dispatchMailComposeSessionDidBeginForExtensions:]_block_invoke.14.cold.1
- ___86-[MEComposeExtensionsHelper initWithComposeSession:extensionsController:iconReloader:]_block_invoke.8
- ___block_literal_global.102
- _objc_msgSend$initWithCanSign:canEncrypt:securityError:addressesFailingEncryption:
CStrings:
+ "\x06"
+ "@48@0:8B16B20B24B28@32@40"
+ "@60@0:8@16B24@28@36B44B48@52"
+ "EFPropertyKey_disallowUsersToLoadRemoteContent"
+ "TB,R,N,V_disallowUsersToLoadRemoteContent"
+ "TB,R,N,V_shouldEncrypt"
+ "TB,R,N,V_shouldSign"
+ "_disallowUsersToLoadRemoteContent"
+ "_shouldPerformSendValidationMap"
+ "a"
+ "disallowUsersToLoadRemoteContent"
+ "hasSecurityExtensionsEnabled"
+ "initWithCanSign:canEncrypt:shouldSign:shouldEncrypt:securityError:addressesFailingEncryption:"
+ "initWithSigners:isEncrypted:signingError:encryptionError:shouldBlockRemoteContent:disallowUsersToLoadRemoteContent:localizedRemoteContentBlockingReason:"
+ "session:hasSendMessageCheckWithCompletion:"
+ "shouldPerformSendValidation"
+ "v32@0:8@\"MEComposeSession\"16@?<v@?B>24"

```
