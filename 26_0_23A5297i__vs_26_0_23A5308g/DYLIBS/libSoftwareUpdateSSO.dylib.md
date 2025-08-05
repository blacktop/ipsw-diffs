## libSoftwareUpdateSSO.dylib

> `/usr/lib/libSoftwareUpdateSSO.dylib`

```diff

-1837.0.31.0.1
-  __TEXT.__text: 0x2ef4
+1837.0.53.0.0
+  __TEXT.__text: 0x2e64
   __TEXT.__auth_stubs: 0x3d0
   __TEXT.__objc_methlist: 0x3b8
-  __TEXT.__const: 0x88
+  __TEXT.__const: 0x80
   __TEXT.__cstring: 0x2df
-  __TEXT.__oslogstring: 0x819
+  __TEXT.__oslogstring: 0x7b9
   __TEXT.__unwind_info: 0xd8
   __TEXT.__objc_classname: 0x9d
-  __TEXT.__objc_methname: 0xb5e
-  __TEXT.__objc_methtype: 0x2e6
-  __TEXT.__objc_stubs: 0xa60
+  __TEXT.__objc_methname: 0xb17
+  __TEXT.__objc_methtype: 0x2e8
+  __TEXT.__objc_stubs: 0xaa0
   __DATA_CONST.__got: 0xc0
   __DATA_CONST.__const: 0x100
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x378
+  __DATA_CONST.__objc_selrefs: 0x388
   __DATA_CONST.__objc_superrefs: 0x8
   __AUTH_CONST.__auth_got: 0x1f0
-  __AUTH_CONST.__const: 0x60
+  __AUTH_CONST.__const: 0x40
   __AUTH_CONST.__cfstring: 0x500
-  __AUTH_CONST.__objc_const: 0x650
+  __AUTH_CONST.__objc_const: 0x640
   __AUTH.__objc_data: 0xa0
   __DATA.__objc_ivar: 0x44
   __DATA.__data: 0x120
-  __DATA.__bss: 0x20
+  __DATA.__bss: 0x10
   - /System/Library/Frameworks/AuthenticationServices.framework/AuthenticationServices
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/SoftwareUpdateCoreSupport.framework/SoftwareUpdateCoreSupport
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 5CC533DC-B021-3BA0-86B3-A8A2A5EC60A7
-  Functions: 64
-  Symbols:   367
-  CStrings:  313
+  UUID: 1CEBB077-FD2D-37E7-9E0B-C1B50098D940
+  Functions: 62
+  Symbols:   362
+  CStrings:  312
 
Symbols:
+ -[SoftwareUpdateSSO _completionDeadline]
+ -[SoftwareUpdateSSO invalidate]
+ _OBJC_IVAR_$_SoftwareUpdateSSO.ssoControllerQueue
+ _objc_msgSend$_completionDeadline
+ _objc_msgSend$cancel
+ _objc_msgSend$integerValue
+ _objc_msgSend$invalidate
- -[SoftwareUpdateExtensibleSSOAuthenticator authenticationController]
- -[SoftwareUpdateExtensibleSSOAuthenticator setAuthenticationController:]
- -[SoftwareUpdateSSO initWithOptions:].cold.1
- _OBJC_IVAR_$_SoftwareUpdateExtensibleSSOAuthenticator._authenticationController
- ___37-[SoftwareUpdateSSO initWithOptions:]_block_invoke
- _objc_msgSend$authenticationController
- _objc_msgSend$setAuthenticationController:
- _ssoControllerQueue
- _ssoControllerQueueOnce
CStrings:
+ "\v"
+ "@\"NSObject<OS_dispatch_queue>\""
+ "ExtensibleSSOAuthenticator: Authentication completed successfully\n"
+ "_completionDeadline"
+ "cancel"
+ "getDawToken called in unsupported environment\n"
+ "integerValue"
+ "invalidate"
+ "ssoControllerQueue"
- "\n"
- "@\"ASAuthorizationController\""
- "GenerateDawToken called in unsupported environment\n"
- "INFO: ExtensibleSSOAuthenticator: Authentication completed successfully\n"
- "T@\"ASAuthorizationController\",&,N,V_authenticationController"
- "Unable to allocate AuthenticationController object\n"
- "Unable to create request object\n"
- "_authenticationController"
- "authenticationController"
- "setAuthenticationController:"

```
