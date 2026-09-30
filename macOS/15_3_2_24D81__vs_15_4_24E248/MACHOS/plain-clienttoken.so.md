## plain-clienttoken.so

> `/usr/lib/sasl2/plain-clienttoken.so`

```diff

 195.0.0.0.0
-  __TEXT.__text: 0x1474
+  __TEXT.__text: 0x1460
   __TEXT.__auth_stubs: 0xa0
   __TEXT.__cstring: 0x43a
   __TEXT.__unwind_info: 0xb0

   __DATA.__data: 0x60
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libsasl2.2.dylib
-  UUID: 472D5C4B-7787-3EA9-AA75-5CB91D6552C4
+  UUID: 999D0EDC-5572-3101-B7D4-79E578F957E9
   Functions: 19
   Symbols:   31
   CStrings:  16
Functions:
~ __plug_ipfromstring : 568 -> 564
~ __plug_strdup : 224 -> 220
~ __plug_parseuser : 376 -> 372
~ _plain_clienttoken_client_plug_init : 92 -> 96
~ _plain_clienttoken_client_mech_step : 1052 -> 1040
CStrings:
+ "Out of Memory in /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/passwordserver_saslplugins/plain_clienttoken.c near line %d"
+ "Out of Memory in /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/passwordserver_saslplugins/plugin_common.c near line %d"
+ "Parameter Error in /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/passwordserver_saslplugins/plain_clienttoken.c near line %d"
+ "Parameter Error in /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/passwordserver_saslplugins/plugin_common.c near line %d"
- "Out of Memory in /AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/passwordserver_saslplugins/plain_clienttoken.c near line %d"
- "Out of Memory in /AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/passwordserver_saslplugins/plugin_common.c near line %d"
- "Parameter Error in /AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/passwordserver_saslplugins/plain_clienttoken.c near line %d"
- "Parameter Error in /AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/passwordserver_saslplugins/plugin_common.c near line %d"

```
