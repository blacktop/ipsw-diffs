## BulletinBoard

> `/System/Library/PrivateFrameworks/BulletinBoard.framework/BulletinBoard`

```diff

-955.2.2.0.0
-  __TEXT.__text: 0x7b778
-  __TEXT.__objc_methlist: 0x87e4
+955.3.5.0.0
+  __TEXT.__text: 0x7c1bc
+  __TEXT.__objc_methlist: 0x8864
   __TEXT.__const: 0x1c0
-  __TEXT.__cstring: 0x6d92
-  __TEXT.__gcc_except_tab: 0x9b8
-  __TEXT.__oslogstring: 0x68c9
+  __TEXT.__cstring: 0x6e80
+  __TEXT.__gcc_except_tab: 0x9dc
+  __TEXT.__oslogstring: 0x6a15
   __TEXT.__dlopen_cstrs: 0x19c
-  __TEXT.__unwind_info: 0x2c38
+  __TEXT.__unwind_info: 0x2c80
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__const: 0x21a0
   __DATA_CONST.__objc_classlist: 0x280
   __DATA_CONST.__objc_catlist: 0x28
-  __DATA_CONST.__objc_protolist: 0x130
+  __DATA_CONST.__objc_protolist: 0x138
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x40f8
+  __DATA_CONST.__objc_selrefs: 0x4178
   __DATA_CONST.__objc_protorefs: 0x68
   __DATA_CONST.__objc_superrefs: 0x210
   __DATA_CONST.__objc_arraydata: 0x190
   __DATA_CONST.__got: 0x648
   __AUTH_CONST.__const: 0xb40
   __AUTH_CONST.__cfstring: 0x79e0
-  __AUTH_CONST.__objc_const: 0x10cc8
+  __AUTH_CONST.__objc_const: 0x10d70
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH_CONST.__objc_intobj: 0x108
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__auth_got: 0x0
-  __DATA.__objc_ivar: 0x8d4
-  __DATA.__data: 0xe60
+  __DATA.__objc_ivar: 0x8e0
+  __DATA.__data: 0xec0
   __DATA_DIRTY.__objc_data: 0x1900
   __DATA_DIRTY.__data: 0x14
   __DATA_DIRTY.__bss: 0x1c8

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 3416
-  Symbols:   5262
-  CStrings:  1545
+  Functions: 3430
+  Symbols:   5287
+  CStrings:  1557
 
Symbols:
+ -[BBServer _carPlayAppPolicyShowsNotificationsForSectionID:]
+ -[BBServer _isCarPlaySessionConnected]
+ -[BBServer _isV68Device]
+ -[BBServer _resumeConnectionWhenRunning:]
+ -[BBServer sessionDidConnect:]
+ -[BBServer sessionDidDisconnect:]
+ GCC_except_table179
+ GCC_except_table211
+ GCC_except_table220
+ GCC_except_table221
+ GCC_except_table360
+ GCC_except_table75
+ GCC_except_table93
+ _CarKitLibrary
+ _MGGetProductType
+ _OBJC_IVAR_$_BBServer._carPlayAppPolicyEvaluator
+ _OBJC_IVAR_$_BBServer._carPlaySessionConnected
+ _OBJC_IVAR_$_BBServer._carPlaySessionStatus
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CARSessionObserving
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CARSessionObserving
+ __OBJC_$_PROTOCOL_REFS_CARSessionObserving
+ __OBJC_LABEL_PROTOCOL_$_CARSessionObserving
+ __OBJC_PROTOCOL_$_CARSessionObserving
+ ___30-[BBServer sessionDidConnect:]_block_invoke
+ ___33-[BBServer sessionDidDisconnect:]_block_invoke
+ ___41-[BBServer _resumeConnectionWhenRunning:]_block_invoke
+ ___getCARSessionStatusClass_block_invoke
+ ___getCRCarPlayAppDeclarationClass_block_invoke
+ ___getCRCarPlayAppPolicyEvaluatorClass_block_invoke
+ _getCARSessionStatusClass.softClass
+ _getCRCarPlayAppDeclarationClass.softClass
+ _getCRCarPlayAppPolicyEvaluatorClass.softClass
- -[BBServer _addSuspendedConnection:]
- GCC_except_table161
- GCC_except_table208
- GCC_except_table213
- GCC_except_table214
- GCC_except_table91
- ___36-[BBServer _addSuspendedConnection:]_block_invoke
CStrings:
+ "BBServer: CarPlay app policy suppresses car feed for bulletin %{public}@ in section %{public}@"
+ "CARSessionStatus"
+ "CRCarPlayAppDeclaration"
+ "CRCarPlayAppPolicyEvaluator"
+ "CarPlay session did connect: %{public}@"
+ "CarPlay session did disconnect: %{public}@"
+ "Class getCARSessionStatusClass(void)_block_invoke"
+ "Class getCRCarPlayAppDeclarationClass(void)_block_invoke"
+ "Class getCRCarPlayAppPolicyEvaluatorClass(void)_block_invoke"
+ "Configured section settings for data provider %{public}@"
+ "Data provider <%{public}@> performed settings migration."
+ "[%{public}@] %{public}@: read from disk"
```
