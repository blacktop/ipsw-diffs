## BiometricSupport

> `/System/Library/PrivateFrameworks/BiometricSupport.framework/BiometricSupport`

```diff

-577.0.0.0.0
-  __TEXT.__text: 0x4e2e0
-  __TEXT.__objc_methlist: 0x291c
-  __TEXT.__const: 0x13ec
-  __TEXT.__cstring: 0x6fdc
-  __TEXT.__oslogstring: 0x3735
-  __TEXT.__gcc_except_tab: 0x1060
-  __TEXT.__unwind_info: 0x19c8
+578.40.6.0.0
+  __TEXT.__text: 0x4e384
+  __TEXT.__objc_methlist: 0x294c
+  __TEXT.__const: 0x1444
+  __TEXT.__cstring: 0x7043
+  __TEXT.__oslogstring: 0x377a
+  __TEXT.__gcc_except_tab: 0x105c
+  __TEXT.__unwind_info: 0x19e8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_classlist: 0xe8
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1ba0
+  __DATA_CONST.__objc_selrefs: 0x1bb8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0xb8
   __DATA_CONST.__objc_arraydata: 0x20
   __DATA_CONST.__got: 0x338
   __AUTH_CONST.__const: 0x1b0
   __AUTH_CONST.__cfstring: 0x2200
-  __AUTH_CONST.__objc_const: 0x3f48
+  __AUTH_CONST.__objc_const: 0x3f70
   __AUTH_CONST.__objc_intobj: 0xcd8
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__auth_got: 0x830
   __AUTH.__objc_data: 0xf0
   __DATA.__objc_ivar: 0x288
-  __DATA.__data: 0xc30
+  __DATA.__data: 0xc58
   __DATA.__common: 0x28
   __DATA_DIRTY.__objc_data: 0x820
   __DATA_DIRTY.__data: 0x8

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2020
-  Symbols:   3386
-  CStrings:  1236
+  Functions: 2033
+  Symbols:   3402
+  CStrings:  1240
 
Symbols:
+ -[BiometricKitXPCExportedObject getDeviceProperties:replyBlock:]
+ -[BiometricKitXPCServer addDeviceSpecificProperties:]
+ -[BiometricKitXPCServer getDeviceProperties:withClient:]
+ GCC_except_table188
+ GCC_except_table194
+ GCC_except_table196
+ GCC_except_table203
+ GCC_except_table208
+ GCC_except_table213
+ GCC_except_table221
+ GCC_except_table227
+ GCC_except_table230
+ GCC_except_table238
+ GCC_except_table248
+ GCC_except_table253
+ __MergedGlobals
+ ___der_key_state_abs_last_mesa_auth
+ ___der_key_state_abs_last_mesa_unlock
+ ___der_key_state_abs_last_passcode_auth
+ ___der_key_state_abs_last_passcode_unlock
+ ___der_key_state_abs_lock_time
+ _der_key_state_abs_last_mesa_auth
+ _der_key_state_abs_last_mesa_unlock
+ _der_key_state_abs_last_passcode_auth
+ _der_key_state_abs_last_passcode_unlock
+ _der_key_state_abs_lock_time
+ _objc_msgSend$addDeviceSpecificProperties:
+ _objc_msgSend$getDeviceProperties:withClient:
- GCC_except_table186
- GCC_except_table193
- GCC_except_table195
- GCC_except_table202
- GCC_except_table204
- GCC_except_table209
- GCC_except_table219
- GCC_except_table226
- GCC_except_table228
- GCC_except_table235
- GCC_except_table246
- GCC_except_table251
CStrings:
+ "-[BiometricKitXPCExportedObject getDeviceProperties:replyBlock:]"
+ "AssertMacros: %s (value = 0x%lx), version: BiometricKit-578.40.6~32, %s file: %s, line: %d\n\n"
+ "deviceProperties"
+ "devicePropertiesDict"
+ "getDeviceProperties: (client:%@) -> err:0x%x deviceProperties:%@\n"
- "AssertMacros: %s (value = 0x%lx), version: BiometricKit-577~3209, %s file: %s, line: %d\n\n"
```
