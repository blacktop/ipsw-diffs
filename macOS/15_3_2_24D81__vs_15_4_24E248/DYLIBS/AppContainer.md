## AppContainer

> `/System/Library/PrivateFrameworks/AppContainer.framework/Versions/A/AppContainer`

```diff

-738.60.3.0.0
-  __TEXT.__text: 0x10a28
+738.100.25.0.0
+  __TEXT.__text: 0x10a20
   __TEXT.__auth_stubs: 0x690
-  __TEXT.__objc_methlist: 0x820
-  __TEXT.__const: 0xa8
+  __TEXT.__objc_methlist: 0x834
+  __TEXT.__const: 0xb0
   __TEXT.__gcc_except_tab: 0xf0
   __TEXT.__cstring: 0x1045
   __TEXT.__oslogstring: 0x7ca
-  __TEXT.__unwind_info: 0x358
+  __TEXT.__unwind_info: 0x368
   __TEXT.__objc_classname: 0x14d
   __TEXT.__objc_methname: 0x1ee9
   __TEXT.__objc_methtype: 0x3a0

   __AUTH_CONST.__auth_got: 0x358
   __AUTH_CONST.__const: 0x720
   __AUTH_CONST.__cfstring: 0x1340
-  __AUTH_CONST.__objc_const: 0xba0
+  __AUTH_CONST.__objc_const: 0xb80
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH.__objc_data: 0x370
   __DATA.__objc_ivar: 0x6c

   - /System/Library/PrivateFrameworks/SecCodeWrapper.framework/Versions/A/SecCodeWrapper
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: D431BC40-3089-3058-86B7-95DF28156191
-  Functions: 299
-  Symbols:   850
+  UUID: 7419B3C9-5E8F-36A0-AD62-B276615256A3
+  Functions: 305
+  Symbols:   856
   CStrings:  710
 
Symbols:
+ +[ASBContainer containerIdentifierForAppSigningId:].cold.1
+ +[ASBMutableContainerSynchronization synchronizationForSigningId:].cold.1
+ -[ASBMutableContainer initWithHomeDirectory:andContainerPath:error:].cold.1
+ -[ASBMutableContainer preferenceDomain:requiresMigration:error:].cold.1
+ ASBBundleIdPassesSanityCheck.cold.1
+ AppSandboxUtilRealPathForPath.cold.1
+ makedir.cold.1
- _OUTLINED_FUNCTION_4

```
