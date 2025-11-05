## libntlm.so

> `/usr/lib/sasl2/libntlm.so`

```diff

 215.0.0.0.0
-  __TEXT.__text: 0x3cac
+  __TEXT.__text: 0x3dd4
   __TEXT.__auth_stubs: 0x200
   __TEXT.__cstring: 0xbb4
-  __TEXT.__unwind_info: 0xe8
+  __TEXT.__unwind_info: 0xf0
   __DATA_CONST.__auth_got: 0x100
   __DATA_CONST.__got: 0x10
   __DATA_CONST.__const: 0x30
   __DATA.__data: 0xcc
   __DATA.__common: 0x500
   - /usr/lib/libSystem.B.dylib
-  UUID: 6C80E138-7D42-3897-BD46-346ECC9E5AC4
-  Functions: 41
-  Symbols:   79
+  UUID: 0E74E1A9-D707-36B5-B26F-F8E02933626C
+  Functions: 44
+  Symbols:   82
   CStrings:  82
 
Symbols:
+ _create_response
+ _smb_session_setup
+ _unload_negprot_resp
Functions:
~ __plug_ipfromstring : 568 -> 564
~ __plug_decode : 508 -> 520
~ __plug_parseuser : 376 -> 372
~ _ntlm_server_plug_init : 92 -> 96
~ _ntlm_client_plug_init : 92 -> 96
~ _ntlm_server_mech_new : 1376 -> 1384
~ _ntlm_server_mech_step : 4048 -> 3012
~ _make_netbios_name : 220 -> 224
~ _retry_writev : 312 -> 300
+ _unload_negprot_resp
~ _unload_buffer : 276 -> 288
~ _P16_nt : 212 -> 208
+ _smb_session_setup
~ _ntlm_client_mech_step : 2044 -> 1536
CStrings:
+ "Out of Memory in /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/passwordserver_sasl/cyrus_sasl/plugins/ntlm.c near line %d"
+ "Out of Memory in /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/passwordserver_sasl/cyrus_sasl/plugins/plugin_common.c near line %d"
+ "Parameter Error in /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/passwordserver_sasl/cyrus_sasl/plugins/plugin_common.c near line %d"
- "Out of Memory in /AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/passwordserver_sasl/cyrus_sasl/plugins/ntlm.c near line %d"
- "Out of Memory in /AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/passwordserver_sasl/cyrus_sasl/plugins/plugin_common.c near line %d"
- "Parameter Error in /AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/passwordserver_sasl/cyrus_sasl/plugins/plugin_common.c near line %d"

```
