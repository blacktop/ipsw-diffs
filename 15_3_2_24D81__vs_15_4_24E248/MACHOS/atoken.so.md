## atoken.so

> `/usr/lib/sasl2/atoken.so`

```diff

 195.0.0.0.0
-  __TEXT.__text: 0x14c8
+  __TEXT.__text: 0x14b8
   __TEXT.__auth_stubs: 0xa0
   __TEXT.__cstring: 0x34c
   __TEXT.__unwind_info: 0xb0

   __DATA.__data: 0x60
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libsasl2.2.dylib
-  UUID: C6D0AF29-45E3-335C-87B1-D666B1BC529B
+  UUID: 29162C5C-4670-3AFE-95F8-B274B370FB3E
   Functions: 19
   Symbols:   31
   CStrings:  14
Functions:
~ __plug_ipfromstring : 568 -> 564
~ __plug_strdup : 224 -> 220
~ __plug_parseuser : 376 -> 372
~ _atoken_client_plug_init : 92 -> 96
~ _atoken_client_mech_step : 1132 -> 1124
CStrings:
+ "Out of Memory in /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/passwordserver_saslplugins/atoken.c near line %d"
+ "Out of Memory in /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/passwordserver_saslplugins/plugin_common.c near line %d"
+ "Parameter Error in /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/passwordserver_saslplugins/plugin_common.c near line %d"
- "Out of Memory in /AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/passwordserver_saslplugins/atoken.c near line %d"
- "Out of Memory in /AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/passwordserver_saslplugins/plugin_common.c near line %d"
- "Parameter Error in /AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/passwordserver_saslplugins/plugin_common.c near line %d"

```
