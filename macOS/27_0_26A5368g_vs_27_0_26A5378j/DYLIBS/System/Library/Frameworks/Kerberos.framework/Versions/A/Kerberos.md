## Kerberos

> `/System/Library/Frameworks/Kerberos.framework/Versions/A/Kerberos`

```diff

-  __TEXT.__text: 0xdcdc
+  __TEXT.__text: 0xdbe8
   __TEXT.__cstring: 0x1859
   __TEXT.__const: 0xd0
-  __TEXT.__unwind_info: 0x400
+  __TEXT.__unwind_info: 0x3f8
   __TEXT.__auth_stubs: 0x0
   __DATA_CONST.__const: 0x228
   __DATA_CONST.__got: 0x0
Sections:
~ __DATA_CONST.__const : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__cfstring : content changed
~ __AUTH.__data : content changed
~ __DATA.__data : content changed
Functions:
~ _krb5_free_authdata : 108 -> 92
~ _profile_parse_file : 1976 -> 1796
~ _profile_update_relation : 332 -> 328
~ _profile_rename_section : 312 -> 308
~ _profile_add_relation : 444 -> 420
~ _krb5_string_to_timestamp : 336 -> 320

```
