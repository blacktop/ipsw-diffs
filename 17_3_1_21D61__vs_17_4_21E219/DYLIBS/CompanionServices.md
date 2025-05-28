## CompanionServices

> `/System/Library/PrivateFrameworks/CompanionServices.framework/CompanionServices`

```diff

-46.20.1.0.0
-  __TEXT.__text: 0xa3bc
-  __TEXT.__auth_stubs: 0x440
-  __TEXT.__objc_methlist: 0xe08
+46.40.11.0.0
+  __TEXT.__text: 0xaaf0
+  __TEXT.__auth_stubs: 0x450
+  __TEXT.__objc_methlist: 0xe80
   __TEXT.__const: 0xe8
-  __TEXT.__cstring: 0x1168
+  __TEXT.__cstring: 0x11d5
   __TEXT.__oslogstring: 0x1b3
   __TEXT.__gcc_except_tab: 0x13c
   __TEXT.__dlopen_cstrs: 0x63
-  __TEXT.__unwind_info: 0x418
-  __TEXT.__objc_classname: 0x388
-  __TEXT.__objc_methname: 0x246d
-  __TEXT.__objc_methtype: 0x64e
-  __TEXT.__objc_stubs: 0xb60
+  __TEXT.__unwind_info: 0x428
+  __TEXT.__objc_classname: 0x39d
+  __TEXT.__objc_methname: 0x262d
+  __TEXT.__objc_methtype: 0x685
+  __TEXT.__objc_stubs: 0xbc0
   __DATA_CONST.__got: 0x50
-  __DATA_CONST.__const: 0x340
-  __DATA_CONST.__objc_classlist: 0xd0
+  __DATA_CONST.__const: 0x390
+  __DATA_CONST.__objc_classlist: 0xd8
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x3e70
-  __DATA_CONST.__objc_selrefs: 0x778
-  __AUTH_CONST.__objc_const: 0xc18
-  __AUTH_CONST.__cfstring: 0x1060
+  __DATA_CONST.__objc_const: 0x3fe0
+  __DATA_CONST.__objc_selrefs: 0x7b8
+  __DATA_CONST.__objc_protorefs: 0x28
+  __DATA_CONST.__objc_classrefs: 0x160
+  __DATA_CONST.__objc_superrefs: 0xa8
+  __AUTH_CONST.__objc_const: 0xca8
+  __AUTH_CONST.__cfstring: 0x10e0
   __AUTH_CONST.__const: 0x130
-  __AUTH_CONST.__auth_got: 0x230
-  __AUTH.__objc_data: 0x820
-  __DATA.__objc_protorefs: 0x28
-  __DATA.__objc_classrefs: 0x158
-  __DATA.__objc_superrefs: 0xa0
-  __DATA.__objc_ivar: 0x114
+  __AUTH_CONST.__auth_got: 0x238
+  __AUTH.__objc_data: 0x870
+  __DATA.__objc_ivar: 0x120
   __DATA.__data: 0x3d0
   __DATA.__bss: 0x108
   - /System/Library/Frameworks/Accounts.framework/Accounts
+  - /System/Library/Frameworks/AuthenticationServices.framework/AuthenticationServices
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/AuthKit.framework/AuthKit

   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 387
-  Symbols:   1542
-  CStrings:  714
+  Functions: 405
+  Symbols:   1602
+  CStrings:  737
 
Symbols:
+ +[CPSLearnMoreResponse supportsSecureCoding]
+ -[CPSAppSignInRequest isWebAuthRequest]
+ -[CPSLearnMoreResponse encodeWithCoder:]
+ -[CPSLearnMoreResponse initWithCoder:]
+ -[CPSViewServicePresentationContext proxiedAppDomains]
+ -[CPSViewServicePresentationContext setProxiedAppDomains:]
+ -[CPSWebRequest additionalHeaderFields]
+ -[CPSWebRequest callback]
+ -[CPSWebRequest initWithURL:callback:additionalHeaderFields:]
+ -[CPSWebRequest initWithURL:callback:additionalHeaderFields:].cold.1
+ -[CPSWebRequest initWithURL:callback:additionalHeaderFields:].cold.2
+ -[CPSWebRequest initWithURL:callbackScheme:additionalHeaderFields:]
+ -[CPSWebRequest initWithURL:callbackScheme:additionalHeaderFields:].cold.1
+ -[CPSWebRequest initWithURL:callbackScheme:additionalHeaderFields:].cold.2
+ GCC_except_table29
+ _OBJC_CLASS_$_ASWebAuthenticationSessionCallback
+ _OBJC_CLASS_$_CPSLearnMoreResponse
+ _OBJC_IVAR_$_CPSViewServicePresentationContext._proxiedAppDomains
+ _OBJC_IVAR_$_CPSWebRequest._additionalHeaderFields
+ _OBJC_IVAR_$_CPSWebRequest._callback
+ _OBJC_METACLASS_$_CPSLearnMoreResponse
+ __OBJC_$_CLASS_METHODS_CPSLearnMoreResponse
+ __OBJC_$_CLASS_PROP_LIST_CPSLearnMoreResponse
+ __OBJC_$_INSTANCE_METHODS_CPSLearnMoreResponse
+ __OBJC_CLASS_PROTOCOLS_$_CPSLearnMoreResponse
+ __OBJC_CLASS_RO_$_CPSLearnMoreResponse
+ __OBJC_METACLASS_RO_$_CPSLearnMoreResponse
+ ___25-[CPSWebRequest isEqual:]_block_invoke_3
+ ___25-[CPSWebRequest isEqual:]_block_invoke_4
+ ___block_descriptor_40_e8_32s_e19_"NSDictionary"8?0ls32l8
+ ___block_descriptor_40_e8_32s_e41_"ASWebAuthenticationSessionCallback"8?0ls32l8
+ _objc_msgSend$decodeDictionaryWithKeysOfClass:objectsOfClass:forKey:
+ _objc_msgSend$decodeObjectOfClasses:forKey:
+ _objc_msgSend$initWithURL:callback:additionalHeaderFields:
+ _objc_msgSend$initWithURL:callbackScheme:additionalHeaderFields:
+ _objc_retain_x25
- -[CPSWebRequest initWithURL:callbackScheme:]
- -[CPSWebRequest initWithURL:callbackScheme:].cold.1
- -[CPSWebRequest initWithURL:callbackScheme:].cold.2
- _objc_msgSend$initWithURL:callbackScheme:
CStrings:
+ "\r"
+ "@\"ASWebAuthenticationSessionCallback\""
+ "@\"ASWebAuthenticationSessionCallback\"8@?0"
+ "@40@0:8@16@24@32"
+ "CPSLearnMoreResponse"
+ "Failed to decode CPSWebRequest: missing callback value"
+ "T@\"ASWebAuthenticationSessionCallback\",R,N,V_callback"
+ "T@\"NSArray\",&,N,V_proxiedAppDomains"
+ "T@\"NSDictionary\",R,N,V_additionalHeaderFields"
+ "T@\"NSString\",?,R,C"
+ "_additionalHeaderFields"
+ "_callback"
+ "_proxiedAppDomains"
+ "additionalHeaderFields"
+ "callback"
+ "callback != ((void *)0)"
+ "decodeDictionaryWithKeysOfClass:objectsOfClass:forKey:"
+ "decodeObjectOfClasses:forKey:"
+ "initWithURL:callback:additionalHeaderFields:"
+ "initWithURL:callbackScheme:additionalHeaderFields:"
+ "isWebAuthRequest"
+ "proxiedAppDomains"
+ "setProxiedAppDomains:"
- "\f"
- "Failed to decode CPSWebRequest: missing callback scheme value"
- "initWithURL:callbackScheme:"

```
