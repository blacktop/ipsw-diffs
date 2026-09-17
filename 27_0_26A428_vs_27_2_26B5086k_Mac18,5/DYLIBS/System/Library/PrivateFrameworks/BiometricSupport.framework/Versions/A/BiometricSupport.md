## BiometricSupport

> `/System/Library/PrivateFrameworks/BiometricSupport.framework/Versions/A/BiometricSupport`

```diff

-577.0.0.0.0
-  __TEXT.__text: 0x3d55c
-  __TEXT.__objc_methlist: 0x284c
-  __TEXT.__const: 0x13ec
+578.40.6.0.0
+  __TEXT.__text: 0x3d5e8
+  __TEXT.__objc_methlist: 0x287c
+  __TEXT.__const: 0x1444
   __TEXT.__gcc_except_tab: 0x112c
-  __TEXT.__cstring: 0x56de
-  __TEXT.__oslogstring: 0x34fe
-  __TEXT.__unwind_info: 0x1250
+  __TEXT.__cstring: 0x571f
+  __TEXT.__oslogstring: 0x3540
+  __TEXT.__unwind_info: 0x1260
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_classlist: 0xe8
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1ac8
+  __DATA_CONST.__objc_selrefs: 0x1ae0
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0xb8
   __DATA_CONST.__objc_arraydata: 0x8
   __DATA_CONST.__got: 0x2f0
   __AUTH_CONST.__const: 0x5c0
   __AUTH_CONST.__cfstring: 0x1f40
-  __AUTH_CONST.__objc_const: 0x3df0
+  __AUTH_CONST.__objc_const: 0x3e18
   __AUTH_CONST.__objc_intobj: 0xcd8
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__auth_got: 0x748
   __AUTH.__objc_data: 0xf0
   __DATA.__objc_ivar: 0x26c
-  __DATA.__data: 0xb70
+  __DATA.__data: 0xb98
   __DATA.__common: 0x28
   __DATA_DIRTY.__objc_data: 0x820
   __DATA_DIRTY.__common: 0x30
-  __DATA_DIRTY.__bss: 0x90
+  __DATA_DIRTY.__bss: 0xa0
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/Versions/A/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1597
-  Symbols:   3385
-  CStrings:  1015
+  Functions: 1605
+  Symbols:   3400
+  CStrings:  1017
 
Symbols:
+ -[BiometricKitXPCExportedObject getDeviceProperties:replyBlock:]
+ -[BiometricKitXPCServer addDeviceSpecificProperties:]
+ -[BiometricKitXPCServer getDeviceProperties:withClient:]
+ GCC_except_table182
+ GCC_except_table188
+ GCC_except_table190
+ GCC_except_table197
+ GCC_except_table202
+ GCC_except_table207
+ GCC_except_table215
+ GCC_except_table223
+ GCC_except_table225
+ GCC_except_table228
+ GCC_except_table236
+ GCC_except_table245
+ GCC_except_table252
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
- GCC_except_table180
- GCC_except_table187
- GCC_except_table189
- GCC_except_table196
- GCC_except_table198
- GCC_except_table203
- GCC_except_table213
- GCC_except_table220
- GCC_except_table224
- GCC_except_table226
- GCC_except_table233
- GCC_except_table243
- GCC_except_table250
CStrings:
+ "-[BiometricKitXPCExportedObject getDeviceProperties:replyBlock:]"
+ "getDeviceProperties: (client:%@) -> err:0x%x deviceProperties:%@\n"
```
