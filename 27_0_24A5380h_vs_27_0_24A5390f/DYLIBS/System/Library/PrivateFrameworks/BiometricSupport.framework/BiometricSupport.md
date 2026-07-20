## BiometricSupport

> `/System/Library/PrivateFrameworks/BiometricSupport.framework/BiometricSupport`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH.__objc_data`
- `__DATA_DIRTY.__objc_data`

```diff

-575.0.0.0.0
-  __TEXT.__text: 0x4ea48
+576.0.0.0.0
+  __TEXT.__text: 0x4ebc8
   __TEXT.__objc_methlist: 0x291c
-  __TEXT.__const: 0x1394
-  __TEXT.__cstring: 0x6fb1
-  __TEXT.__oslogstring: 0x3733
+  __TEXT.__const: 0x13ec
+  __TEXT.__cstring: 0x6fcf
+  __TEXT.__oslogstring: 0x3734
   __TEXT.__gcc_except_tab: 0x1048
   __TEXT.__unwind_info: 0x1058
   __TEXT.__objc_stubs: 0x0

   __AUTH_CONST.__auth_got: 0x830
   __AUTH.__objc_data: 0xf0
   __DATA.__objc_ivar: 0x288
-  __DATA.__data: 0xc08
+  __DATA.__data: 0xc30
   __DATA.__common: 0x28
   __DATA.__bss: 0x51
   __DATA_DIRTY.__objc_data: 0x820

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2015
-  Symbols:   3371
-  CStrings:  1234
+  Functions: 2018
+  Symbols:   3383
+  CStrings:  1235
 
Symbols:
+ ___der_key_last_mesa_auth
+ ___der_key_last_mesa_unlock
+ ___der_key_last_passcode_auth
+ ___der_key_last_passcode_unlock
+ ___der_key_sks_heap_stats
+ _aks_get_convenience_bio_state
+ _aks_get_sks_heap_stats
+ _der_key_last_mesa_auth
+ _der_key_last_mesa_unlock
+ _der_key_last_passcode_auth
+ _der_key_last_passcode_unlock
+ _der_key_sks_heap_stats
Functions:
~ _OUTLINED_FUNCTION_43 : 16 -> 24
~ _OUTLINED_FUNCTION_24 : 28 -> 12
~ _OUTLINED_FUNCTION_24 : 28 -> 12
+ _OUTLINED_FUNCTION_24
~ _OUTLINED_FUNCTION_22 : 12 -> 20
~ _OUTLINED_FUNCTION_22 : 8 -> 56
~ _OUTLINED_FUNCTION_40 : 24 -> 12
+ _OUTLINED_FUNCTION_42
~ _OUTLINED_FUNCTION_19 : 36 -> 16
~ _OUTLINED_FUNCTION_20 : 12 -> 36
~ _OUTLINED_FUNCTION_21 : 56 -> 12
~ _OUTLINED_FUNCTION_23 : 12 -> 8
~ _OUTLINED_FUNCTION_26 : 20 -> 28
~ _OUTLINED_FUNCTION_27 : 28 -> 20
~ _OUTLINED_FUNCTION_28 : 12 -> 28
~ _OUTLINED_FUNCTION_31 : 32 -> 12
~ _OUTLINED_FUNCTION_33 : 36 -> 32
~ _OUTLINED_FUNCTION_34 : 16 -> 36
~ _OUTLINED_FUNCTION_35 : 36 -> 16
~ _OUTLINED_FUNCTION_36 : 12 -> 36
~ _OUTLINED_FUNCTION_37 : 20 -> 12
~ _OUTLINED_FUNCTION_38 : 28 -> 20
~ _OUTLINED_FUNCTION_39 : 12 -> 28
- _OUTLINED_FUNCTION_42
~ _aks_kext_get_options : 204 -> 188
~ _aks_get_internal_info_for_key : 384 -> 376
+ _aks_get_convenience_bio_state
+ _aks_get_sks_heap_stats
CStrings:
+ "AssertMacros: %s (value = 0x%lx), version: BiometricKit-576~458, %s file: %s, line: %d\n\n"
+ "aks_get_convenience_bio_state"
- "AssertMacros: %s (value = 0x%lx), version: BiometricKit-575~90, %s file: %s, line: %d\n\n"
```
