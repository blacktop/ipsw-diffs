## LoginKit

> `/System/Library/PrivateFrameworks/LoginKit.framework/LoginKit`

```diff

-3019.0.0.0.0
-  __TEXT.__text: 0xfa1c
-  __TEXT.__auth_stubs: 0x6d0
-  __TEXT.__objc_methlist: 0x14f4
-  __TEXT.__cstring: 0x1071
+3024.0.0.0.0
+  __TEXT.__text: 0x10698
+  __TEXT.__auth_stubs: 0x660
+  __TEXT.__objc_methlist: 0x1524
+  __TEXT.__cstring: 0x102c
   __TEXT.__const: 0x80
   __TEXT.__gcc_except_tab: 0x84
   __TEXT.__oslogstring: 0x96e
   __TEXT.__ustring: 0xb8
-  __TEXT.__unwind_info: 0x458
+  __TEXT.__unwind_info: 0x590
   __TEXT.__objc_classname: 0x2bd
-  __TEXT.__objc_methname: 0x3d06
+  __TEXT.__objc_methname: 0x3d99
   __TEXT.__objc_methtype: 0x77a
-  __TEXT.__objc_stubs: 0x2da0
+  __TEXT.__objc_stubs: 0x2dc0
   __DATA_CONST.__got: 0x218
-  __DATA_CONST.__const: 0x630
+  __DATA_CONST.__const: 0x728
   __DATA_CONST.__objc_classlist: 0xd8
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xf50
+  __DATA_CONST.__objc_selrefs: 0xf68
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0xa0
   __DATA_CONST.__objc_arraydata: 0x8
-  __AUTH_CONST.__auth_got: 0x378
+  __AUTH_CONST.__auth_got: 0x340
   __AUTH_CONST.__const: 0x100
-  __AUTH_CONST.__cfstring: 0x1520
-  __AUTH_CONST.__objc_const: 0x3060
+  __AUTH_CONST.__cfstring: 0x1500
+  __AUTH_CONST.__objc_const: 0x3098
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0x820
-  __DATA.__objc_ivar: 0x178
+  __DATA.__objc_ivar: 0x17c
   __DATA.__data: 0x3d4
   __DATA.__bss: 0x98
   __DATA.__common: 0x18

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 284AD075-4B3B-3335-8563-2C23989DBCC2
-  Functions: 454
-  Symbols:   1957
-  CStrings:  1232
+  UUID: 89EFE7CD-EA97-35F8-90BA-7D22EF2E81D7
+  Functions: 466
+  Symbols:   1982
+  CStrings:  1231
 
Symbols:
+ -[LKLoginController triggerDirectTemporarySessionSwitchLoginWithCompletionHandler:]
+ -[LKLogoutSupport logoutTask]
+ -[LKLogoutSupport setLogoutTask:]
+ _OBJC_IVAR_$_LKLogoutSupport._logoutTask
+ _OUTLINED_FUNCTION_2
+ _OUTLINED_FUNCTION_3
+ ___43-[LKLogoutSupport _syncPreferencesIfNeeded]_block_invoke.10
+ ___83-[LKLoginController triggerDirectTemporarySessionSwitchLoginWithCompletionHandler:]_block_invoke
+ _objc_msgSend$triggerDirectTemporarySessionSwitchLoginWithCompletionHandler:
+ _objc_retain_x28
- ___43-[LKLogoutSupport _syncPreferencesIfNeeded]_block_invoke.12
- __os_feature_enabled_impl
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x25
- _objc_retain_x27
- _objc_retain_x4
- _objc_retain_x5
- _objc_retain_x8
CStrings:
+ "T@\"UMUserSwitchBlockingTask\",&,N,V_logoutTask"
+ "This Apple Account cannot be used on this device"
+ "_logoutTask"
+ "logoutTask"
+ "setLogoutTask:"
+ "triggerDirectTemporarySessionSwitchLoginWithCompletionHandler:"
- "AABranding"
- "AppleAccount"
- "Not a managed Apple ID"
- "SharediPad"
- "This Apple ID cannot be used on this device"
- "idMSPreferences"

```
