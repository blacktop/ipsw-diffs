## pam_krb5.so.2

> `/usr/lib/pam/pam_krb5.so.2`

```diff

-  __TEXT.__text: 0x3018
+  __TEXT.__text: 0x2fe8
   __TEXT.__auth_stubs: 0x620
   __TEXT.__cstring: 0xe64
   __TEXT.__const: 0x1c
Sections:
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__cfstring : content changed
Functions:
~ _verify_krb_v5_tgt : 588 -> 572
~ _extract_homemount : 500 -> 468

```
