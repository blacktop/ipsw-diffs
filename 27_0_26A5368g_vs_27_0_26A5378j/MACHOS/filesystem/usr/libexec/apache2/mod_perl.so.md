## mod_perl.so

> `/usr/libexec/apache2/mod_perl.so`

```diff

-  __TEXT.__text: 0x1a810
+  __TEXT.__text: 0x1a7b4
   __TEXT.__auth_stubs: 0x11a0
   __TEXT.__cstring: 0x3a5b
   __TEXT.__const: 0x51
Sections:
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__const : content changed
~ __DATA.__data : content changed
Functions:
~ _modperl_callback_run_handlers : 1148 -> 1168
~ _modperl_handler_anon_next : 1052 -> 1060
~ _modperl_str_toupper : 64 -> 56
~ sub_8e78 -> sub_8e8c : 156 -> 148
~ _modperl_file2package : 404 -> 396
~ _modperl_mgv_compile : 480 -> 416
~ _modperl_env_hash_keys : 1160 -> 1168
~ _modperl_env_default_populate : 236 -> 220
~ _modperl_cgi_header_parse : 352 -> 340
~ _modperl_modglobal_hash_keys : 1164 -> 1172
~ _modperl_modglobal_lookup : 100 -> 80

```
