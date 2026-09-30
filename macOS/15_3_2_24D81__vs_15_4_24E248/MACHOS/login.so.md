## login.so

> `/usr/lib/sasl2/login.so`

```diff

 215.0.0.0.0
-  __TEXT.__text: 0x1a68
+  __TEXT.__text: 0x1a78
   __TEXT.__auth_stubs: 0xe0
   __TEXT.__cstring: 0x538
   __TEXT.__unwind_info: 0xc0

   __DATA_CONST.__got: 0x8
   __DATA.__data: 0xc8
   - /usr/lib/libSystem.B.dylib
-  UUID: E97C77F0-C0B8-3341-969E-907C29D827E2
+  UUID: 22D808C5-1F7E-377E-B2A4-76DFD88BD1A8
   Functions: 29
   Symbols:   46
   CStrings:  25
Functions:
~ _login_server_plug_init : 92 -> 96
~ _login_client_plug_init : 92 -> 96
~ _login_server_mech_step : 620 -> 624
~ __plug_ipfromstring : 568 -> 564
~ __plug_decode : 508 -> 520
~ __plug_parseuser : 376 -> 372
CStrings:
+ "Out of Memory in /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/passwordserver_sasl/cyrus_sasl/plugins/login.c near line %d"
+ "Out of Memory in /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/passwordserver_sasl/cyrus_sasl/plugins/plugin_common.c near line %d"
+ "Parameter Error in /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/passwordserver_sasl/cyrus_sasl/plugins/login.c near line %d"
+ "Parameter Error in /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/passwordserver_sasl/cyrus_sasl/plugins/plugin_common.c near line %d"
- "Out of Memory in /AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/passwordserver_sasl/cyrus_sasl/plugins/login.c near line %d"
- "Out of Memory in /AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/passwordserver_sasl/cyrus_sasl/plugins/plugin_common.c near line %d"
- "Parameter Error in /AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/passwordserver_sasl/cyrus_sasl/plugins/login.c near line %d"
- "Parameter Error in /AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/passwordserver_sasl/cyrus_sasl/plugins/plugin_common.c near line %d"

```
