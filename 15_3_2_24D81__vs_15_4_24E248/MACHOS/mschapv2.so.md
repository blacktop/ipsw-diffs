## mschapv2.so

> `/usr/lib/sasl2/mschapv2.so`

```diff

 195.0.0.0.0
-  __TEXT.__text: 0x24e4
+  __TEXT.__text: 0x24b4
   __TEXT.__auth_stubs: 0x1b0
   __TEXT.__const: 0xb0
   __TEXT.__cstring: 0x63a
-  __TEXT.__unwind_info: 0xe8
+  __TEXT.__unwind_info: 0xe0
   __DATA_CONST.__auth_got: 0xd8
   __DATA_CONST.__got: 0x10
   __DATA_CONST.__const: 0x18

   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/PrivateFrameworks/PasswordServer.framework/Versions/A/PasswordServer
   - /usr/lib/libSystem.B.dylib
-  UUID: 2E254DB9-B31A-34D7-A796-9A6170FD4CA7
+  UUID: 3B77898E-D2C1-3211-AF8D-B0D0D24B4B76
   Functions: 34
   Symbols:   66
   CStrings:  34
Functions:
~ _chap_server_plug_init : 92 -> 96
~ _chap_client_plug_init : 92 -> 96
~ _chap_server_mech_step : 1396 -> 1380
~ _chap_client_mech_step : 1424 -> 1412
~ _ChapMS : 200 -> 188
~ _ChapMS2 : 528 -> 524
~ __plug_ipfromstring : 568 -> 564
~ __plug_strdup : 224 -> 220
~ __plug_parseuser : 376 -> 372
CStrings:
+ "Out of Memory in /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/passwordserver_saslplugins/mschapv2.c near line %d"
+ "Out of Memory in /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/passwordserver_saslplugins/plugin_common.c near line %d"
+ "Parameter Error in /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/passwordserver_saslplugins/mschapv2.c near line %d"
+ "Parameter Error in /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/passwordserver_saslplugins/plugin_common.c near line %d"
- "Out of Memory in /AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/passwordserver_saslplugins/mschapv2.c near line %d"
- "Out of Memory in /AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/passwordserver_saslplugins/plugin_common.c near line %d"
- "Parameter Error in /AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/passwordserver_saslplugins/mschapv2.c near line %d"
- "Parameter Error in /AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/passwordserver_saslplugins/plugin_common.c near line %d"

```
