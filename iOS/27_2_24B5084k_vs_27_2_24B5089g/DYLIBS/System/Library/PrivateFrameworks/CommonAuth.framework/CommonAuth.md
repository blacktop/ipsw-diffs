## CommonAuth

> `/System/Library/PrivateFrameworks/CommonAuth.framework/CommonAuth`

```diff

   __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0xb0
   __AUTH_CONST.__auth_got: 0x0
-  __DATA.__data: 0x77a
+  __DATA.__data: 0x2a
+  __DATA_DIRTY.__data: 0x750
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libheimdal-asn1.dylib
   - /usr/lib/libicucore.A.dylib
Functions:
~ _heim_ntlm_free_buf -> _heim_ntlm_unparse_flags : 48 -> 44
~ _heim_ntlm_free_targetinfo -> _heim_ntlm_free_buf : 108 -> 48
~ _heim_ntlm_encode_targetinfo -> _heim_ntlm_free_targetinfo : 536 -> 108
~ _encode_ti_string -> _heim_ntlm_encode_targetinfo : 120 -> 536
~ _heim_ntlm_decode_targetinfo -> _encode_ti_string : 496 -> 120
~ sub_259c2abd0 -> _heim_ntlm_decode_targetinfo : 44 -> 496
```
