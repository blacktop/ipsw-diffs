## libbsm.0.dylib

> `/usr/lib/libbsm.0.dylib`

```diff

 90.0.0.0.0
-  __TEXT.__text: 0xe884
-  __TEXT.__auth_stubs: 0x3c0
+  __TEXT.__text: 0xe8ec
   __TEXT.__const: 0x3d0
   __TEXT.__cstring: 0x188b
-  __TEXT.__unwind_info: 0x2b8
-  __DATA_CONST.__got: 0x18
+  __TEXT.__unwind_info: 0x2d8
+  __TEXT.__auth_stubs: 0x0
   __DATA_CONST.__const: 0xb20
-  __AUTH_CONST.__auth_got: 0x1e0
+  __DATA_CONST.__got: 0x0
+  __AUTH_CONST.__auth_got: 0x0
   __DATA.__data: 0x180
   __DATA.__bss: 0x8a0
   __DATA_DIRTY.__bss: 0x4
   - /usr/lib/libSystem.B.dylib
-  UUID: FF317F86-6ABD-3096-A10E-8661322CC700
+  UUID: 72CCB76E-08B1-38F6-9F47-A3F61406EBD1
   Functions: 245
   Symbols:   427
   CStrings:  415
Functions:
~ _audit_token_to_au32 -> _audit_token_to_pid : 140 -> 8
~ _audit_token_to_euid -> _audit_token_to_au32 : 8 -> 140
~ _au_assemble : 456 -> 460
~ _getauditflagschar : 280 -> 284
~ _fetch_execenv_tok : 152 -> 156
~ _fetch_inaddr_ex_tok : 160 -> 164
~ _fetch_subject32ex_tok : 384 -> 388
~ _fetch_arb_tok : 144 -> 148
~ _fetch_krb5_principal_tok : 152 -> 156
~ _au_print_flags_tok : 17700 -> 17768
~ _print_string : 288 -> 292
~ _au_to_strings : 312 -> 316

```
