## smb_ntlmv2.so

> `/usr/lib/sasl2/smb_ntlmv2.so`

```diff

 195.0.0.0.0
-  __TEXT.__text: 0x2078
+  __TEXT.__text: 0x2098
   __TEXT.__auth_stubs: 0x190
   __TEXT.__cstring: 0x67f
   __TEXT.__unwind_info: 0xc0

   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/PrivateFrameworks/PasswordServer.framework/Versions/A/PasswordServer
   - /usr/lib/libSystem.B.dylib
-  UUID: 8FDD0D94-E3D3-3301-968A-AABF3C3BF494
+  UUID: 3A37A1A0-D63B-3631-B64C-7F010D936037
   Functions: 27
   Symbols:   57
   CStrings:  37
Functions:
~ _V2 : 516 -> 512
~ _ntlmv2_server_plug_init : 92 -> 96
~ _ntlmv2_client_plug_init : 92 -> 96
~ _ntlmv2_server_mech_step : 1744 -> 1792
~ _ntlmv2_client_mech_step : 1396 -> 1388
~ __plug_ipfromstring : 568 -> 564
~ __plug_strdup : 224 -> 220
~ __plug_parseuser : 376 -> 372
CStrings:
+ "Out of Memory in /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/passwordserver_saslplugins/ntlmv2.c near line %d"
+ "Out of Memory in /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/passwordserver_saslplugins/plugin_common.c near line %d"
+ "Parameter Error in /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/passwordserver_saslplugins/ntlmv2.c near line %d"
+ "Parameter Error in /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/passwordserver_saslplugins/plugin_common.c near line %d"
- "Out of Memory in /AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/passwordserver_saslplugins/ntlmv2.c near line %d"
- "Out of Memory in /AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/passwordserver_saslplugins/plugin_common.c near line %d"
- "Parameter Error in /AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/passwordserver_saslplugins/ntlmv2.c near line %d"
- "Parameter Error in /AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/passwordserver_saslplugins/plugin_common.c near line %d"

```
