## CoreCDP

> `/System/Library/PrivateFrameworks/CoreCDP.framework/CoreCDP`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
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
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-444.0.0.0.0
-  __TEXT.__text: 0x4f4c8
+445.0.0.0.0
+  __TEXT.__text: 0x4f648
   __TEXT.__objc_methlist: 0x3a74
-  __TEXT.__const: 0x1424
+  __TEXT.__const: 0x147c
   __TEXT.__gcc_except_tab: 0x1114
   __TEXT.__oslogstring: 0x91af
-  __TEXT.__cstring: 0x65a4
+  __TEXT.__cstring: 0x65c2
   __TEXT.__dlopen_cstrs: 0xca
   __TEXT.__ustring: 0x28
   __TEXT.__unwind_info: 0x1658

   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__auth_got: 0x878
   __DATA.__objc_ivar: 0x300
-  __DATA.__data: 0x1150
+  __DATA.__data: 0x1178
   __DATA.__bss: 0x141
   __DATA.__common: 0x20
   __DATA_DIRTY.__objc_data: 0x1090

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2398
-  Symbols:   4515
-  CStrings:  1638
+  Functions: 2401
+  Symbols:   4527
+  CStrings:  1639
 
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
CStrings:
+ "aks_get_convenience_bio_state"
```
