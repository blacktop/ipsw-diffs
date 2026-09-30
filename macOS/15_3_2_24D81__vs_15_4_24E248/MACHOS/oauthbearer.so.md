## oauthbearer.so

> `/usr/lib/sasl2/oauthbearer.so`

```diff

 195.0.0.0.0
-  __TEXT.__text: 0x162c
+  __TEXT.__text: 0x1624
   __TEXT.__auth_stubs: 0xf0
   __TEXT.__cstring: 0x4c9
   __TEXT.__unwind_info: 0xb0

   __DATA.__data: 0xc0
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libsasl2.2.dylib
-  UUID: 01986BAB-059B-30B5-AD93-5C48AFB995AD
+  UUID: 1A8685A6-6913-3100-B154-AA86F00162F2
   Functions: 20
   Symbols:   37
   CStrings:  22
Functions:
~ __plug_ipfromstring : 568 -> 564
~ __plug_strdup : 224 -> 220
~ __plug_parseuser : 376 -> 372
~ _oauthbearer_client_plug_init : 92 -> 96
CStrings:
+ "Out of Memory in /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/passwordserver_saslplugins/oauthbearer.c near line %d"
+ "Out of Memory in /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/passwordserver_saslplugins/plugin_common.c near line %d"
+ "Parameter Error in /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/passwordserver_saslplugins/plugin_common.c near line %d"
- "Out of Memory in /AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/passwordserver_saslplugins/oauthbearer.c near line %d"
- "Out of Memory in /AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/passwordserver_saslplugins/plugin_common.c near line %d"
- "Parameter Error in /AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/passwordserver_saslplugins/plugin_common.c near line %d"

```
