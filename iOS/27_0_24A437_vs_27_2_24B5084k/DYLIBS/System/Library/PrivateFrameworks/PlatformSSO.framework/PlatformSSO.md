## PlatformSSO

> `/System/Library/PrivateFrameworks/PlatformSSO.framework/PlatformSSO`

```diff

-643.0.47.0.0
-  __TEXT.__text: 0x59f34
-  __TEXT.__objc_methlist: 0x358c
+643.40.23.0.0
+  __TEXT.__text: 0x5a3d8
+  __TEXT.__objc_methlist: 0x35bc
   __TEXT.__const: 0x322
-  __TEXT.__cstring: 0x8296
-  __TEXT.__oslogstring: 0x28f1
-  __TEXT.__gcc_except_tab: 0x1448
+  __TEXT.__cstring: 0x82e6
+  __TEXT.__oslogstring: 0x2961
+  __TEXT.__gcc_except_tab: 0x1454
   __TEXT.__dlopen_cstrs: 0x162
   __TEXT.__swift5_typeref: 0xd9
   __TEXT.__swift5_capture: 0x14c

   __TEXT.__swift_as_entry: 0x30
   __TEXT.__swift_as_ret: 0x54
   __TEXT.__swift_as_cont: 0x58
-  __TEXT.__unwind_info: 0x1e18
+  __TEXT.__unwind_info: 0x1e28
   __TEXT.__eh_frame: 0x628
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2400
+  __DATA_CONST.__objc_selrefs: 0x2428
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0xc8
   __DATA_CONST.__objc_arraydata: 0x10
-  __DATA_CONST.__got: 0x440
+  __DATA_CONST.__got: 0x458
   __AUTH_CONST.__const: 0xc80
-  __AUTH_CONST.__cfstring: 0x3a40
-  __AUTH_CONST.__objc_const: 0x8640
+  __AUTH_CONST.__cfstring: 0x3a80
+  __AUTH_CONST.__objc_const: 0x8670
   __AUTH_CONST.__objc_intobj: 0xc0
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH_CONST.__auth_got: 0x758
+  __AUTH_CONST.__auth_got: 0x760
   __AUTH.__objc_data: 0xa00
-  __DATA.__objc_ivar: 0x390
+  __DATA.__objc_ivar: 0x394
   __DATA.__data: 0x600
   __DATA_DIRTY.__objc_data: 0x50
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 2146
-  Symbols:   3624
-  CStrings:  1050
+  Functions: 2154
+  Symbols:   3638
+  CStrings:  1053
 
Symbols:
+ -[POAgentAuthenticationProcess postAuthenticationNotificationForEvaluationError:]
+ -[PODaemonConnection resetTempSessionAccountWithCompletion:]
+ -[POProfile alwaysUseLoginUI]
+ -[POProfile setAlwaysUseLoginUI:]
+ GCC_except_table115
+ GCC_except_table123
+ GCC_except_table130
+ GCC_except_table178
+ GCC_except_table36
+ GCC_except_table89
+ _LAErrorDomain
+ _OBJC_IVAR_$_POProfile._alwaysUseLoginUI
+ _POExtensionNormalizedTeamIdentifier
+ ___60-[PODaemonConnection resetTempSessionAccountWithCompletion:]_block_invoke
+ _krb5_get_init_creds_opt_set_tkt_life
+ _objc_msgSend$alwaysUseLoginUI
+ _objc_msgSend$domain
+ _objc_msgSend$postAuthenticationNotificationForEvaluationError:
+ _objc_msgSend$resetTempSessionAccountWithCompletion:
+ _objc_msgSend$setAlwaysUseLoginUI:
- GCC_except_table114
- GCC_except_table117
- GCC_except_table121
- GCC_except_table128
- GCC_except_table177
- GCC_except_table5
CStrings:
+ "AlwaysUseLoginUI"
+ "Auth rights already checked for this build"
+ "Auth rights check failed, screen unlock may not use Platform SSO: %{public}@"
+ "Auth rights checked successfully"
+ "The federationUserPreauthenticationURL is missing for dynamic OpenID."
- "Rule already checked"
- "Rule successfully checked"
```
