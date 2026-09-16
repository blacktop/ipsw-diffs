## AppSSO

> `/System/Library/PrivateFrameworks/AppSSO.framework/AppSSO`

```diff

-643.0.47.0.0
-  __TEXT.__text: 0x2b2f4
+643.40.23.0.0
+  __TEXT.__text: 0x2b5e0
   __TEXT.__objc_methlist: 0x1c54
   __TEXT.__const: 0x158
-  __TEXT.__gcc_except_tab: 0x195c
-  __TEXT.__oslogstring: 0x4c95
-  __TEXT.__cstring: 0x3806
+  __TEXT.__gcc_except_tab: 0x19a4
+  __TEXT.__oslogstring: 0x4ce8
+  __TEXT.__cstring: 0x383c
   __TEXT.__dlopen_cstrs: 0x6dc
-  __TEXT.__unwind_info: 0x12d0
+  __TEXT.__unwind_info: 0x12d8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_arraydata: 0x28
   __DATA_CONST.__got: 0x240
   __AUTH_CONST.__const: 0x3e0
-  __AUTH_CONST.__cfstring: 0x1320
+  __AUTH_CONST.__cfstring: 0x1340
   __AUTH_CONST.__objc_const: 0x4900
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__objc_arrayobj: 0x18

   __DATA.__objc_ivar: 0x174
   __DATA.__data: 0x6d0
   __DATA_DIRTY.__objc_data: 0x6e0
-  __DATA_DIRTY.__bss: 0x1d0
+  __DATA_DIRTY.__bss: 0x1d8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1065
+  Functions: 1068
   Symbols:   1988
-  CStrings:  733
+  CStrings:  735
 
Functions:
~ _AppSSOCoreLibrary : 256 -> 252
~ _AppSSOCoreLibrary : 80 -> 256
~ _AppSSOCoreLibrary : 252 -> 80
~ _AppSSOCoreLibrary : 92 -> 252
+ _AppSSOCoreLibrary
~ -[SODDMConfigurationHost applyConfiguration:replaceKey:error:] : 1140 -> 1724
~ ___getSOErrorHelperClass_block_invoke : 324 -> 88
+ ___getSOFullProfileClass_block_invoke
+ -[SODDMConfigurationHost loadDDMConfigurationsWithError:].cold.1
+ ___getSOAuthorizationResultCoreClass_block_invoke.cold.1
- ___getSOFullProfileClass_block_invoke.cold.1
CStrings:
+ "Only a single Platform SSO configuration is supported"
+ "Rejecting configuration: more than one Platform SSO configuration is not supported"
```
