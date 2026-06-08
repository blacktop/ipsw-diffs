## CommonAuth

> `/System/Library/PrivateFrameworks/CommonAuth.framework/CommonAuth`

```diff

-710.100.4.0.0
-  __TEXT.__text: 0x65ac
-  __TEXT.__auth_stubs: 0x2d0
-  __TEXT.__const: 0x15c
+720.0.0.0.0
+  __TEXT.__text: 0x65f0
+  __TEXT.__const: 0x154
   __TEXT.__cstring: 0x76f
   __TEXT.__unwind_info: 0x1f8
-  __DATA_CONST.__got: 0x10
-  __AUTH_CONST.__auth_got: 0x168
+  __TEXT.__auth_stubs: 0x0
+  __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0xb0
+  __AUTH_CONST.__auth_got: 0x0
   __DATA.__data: 0x77a
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libheimdal-asn1.dylib
   - /usr/lib/libicucore.A.dylib
-  UUID: F24737AE-EBFF-3557-943B-427228A3F69C
+  UUID: 9B6D6EAE-4F2A-34F0-85BA-3ED36E961E17
   Functions: 146
   Symbols:   301
   CStrings:  124
Functions:
~ _ret_string : 352 -> 356
~ _ascii2ucs2le : 396 -> 400
~ _verify_ntlm2 : 736 -> 740
~ _heim_cram_md5_export : 396 -> 404
~ _parse_values : 576 -> 580
~ __krb5_put_int : 40 -> 44
~ _encode_hex : 164 -> 168
~ _wind_ucs2read : 224 -> 260
~ _wind_utf8ucs2 : 184 -> 188
~ _wind_ucs2utf8 : 180 -> 176

```
