## PlatformSSOCore

> `/System/Library/PrivateFrameworks/PlatformSSOCore.framework/PlatformSSOCore`

```diff

-643.0.33.0.0
-  __TEXT.__text: 0x976dc
-  __TEXT.__objc_methlist: 0x6278
+643.0.47.0.0
+  __TEXT.__text: 0x97b0c
+  __TEXT.__objc_methlist: 0x62d8
   __TEXT.__const: 0x19ac
   __TEXT.__cstring: 0xad28
   __TEXT.__oslogstring: 0x1e67

   __TEXT.__swift5_assocty: 0x30
   __TEXT.__swift5_proto: 0x1c
   __TEXT.__swift5_types: 0x30
-  __TEXT.__unwind_info: 0x2170
+  __TEXT.__unwind_info: 0x2178
   __TEXT.__eh_frame: 0x568
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x90
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2ce8
+  __DATA_CONST.__objc_selrefs: 0x2d10
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0x1e8
   __DATA_CONST.__objc_arraydata: 0x58
   __DATA_CONST.__got: 0x9b0
   __AUTH_CONST.__const: 0xc20
   __AUTH_CONST.__cfstring: 0x7b20
-  __AUTH_CONST.__objc_const: 0x14cc8
+  __AUTH_CONST.__objc_const: 0x14d28
   __AUTH_CONST.__objc_intobj: 0x228
   __AUTH_CONST.__objc_doubleobj: 0x30
   __AUTH_CONST.__objc_arrayobj: 0x78

   __AUTH_CONST.__auth_got: 0xdb8
   __AUTH.__objc_data: 0x35a0
   __AUTH.__data: 0x1a8
-  __DATA.__objc_ivar: 0x64c
+  __DATA.__objc_ivar: 0x654
   __DATA.__data: 0x1228
   __DATA.__bss: 0x771
   __DATA.__common: 0x88

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 3843
-  Symbols:   6766
+  Functions: 3850
+  Symbols:   6781
   CStrings:  1759
 
Symbols:
+ +[POAuthenticationProcess authorizationContextScopes]
+ -[POAuthenticationContext includePlatformSSOAuthorizationScopes]
+ -[POAuthenticationContext setIncludePlatformSSOAuthorizationScopes:]
+ -[POAuthenticationProcess _requestScopeForContext:]
+ -[POAuthenticationProcess _scopeByRemovingAuthorizationContextScopes:]
+ -[POLoginConfiguration includePlatformSSOAuthorizationScopes]
+ -[POLoginConfiguration setIncludePlatformSSOAuthorizationScopes:]
+ _OBJC_IVAR_$_POAuthenticationContext._includePlatformSSOAuthorizationScopes
+ _OBJC_IVAR_$_POLoginConfiguration._includePlatformSSOAuthorizationScopes
+ __OBJC_$_CLASS_METHODS_POAuthenticationProcess
+ _objc_msgSend$_requestScopeForContext:
+ _objc_msgSend$_scopeByRemovingAuthorizationContextScopes:
+ _objc_msgSend$authorizationContextScopes
+ _objc_msgSend$includePlatformSSOAuthorizationScopes
+ _objc_msgSend$setIncludePlatformSSOAuthorizationScopes:
```
