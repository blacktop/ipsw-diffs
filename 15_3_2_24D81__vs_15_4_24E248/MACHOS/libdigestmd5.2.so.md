## libdigestmd5.2.so

> `/usr/lib/sasl2/libdigestmd5.2.so`

```diff

 215.0.0.0.0
-  __TEXT.__text: 0x7098
+  __TEXT.__text: 0x6ff8
   __TEXT.__auth_stubs: 0x1a0
   __TEXT.__const: 0xf8
   __TEXT.__cstring: 0x1330

   __DATA.__data: 0x1c8
   __DATA.__bss: 0x10
   - /usr/lib/libSystem.B.dylib
-  UUID: 56ED4CD5-8814-3636-8D28-5BA7236803E3
+  UUID: D2BEA401-726D-3299-841C-9894DBB4E2A2
   Functions: 56
   Symbols:   94
   CStrings:  158
Functions:
~ _digestmd5_server_mech_step : 1864 -> 1884
~ _digestmd5_server_mech_step2 : 5288 -> 5192
~ _digestmd5_encode : 536 -> 532
~ _create_layer_keys : 584 -> 580
~ _MD5_UTF8_8859_1 : 284 -> 276
~ _digestmd5_client_mech_step : 4064 -> 4000
~ _make_client_response : 2388 -> 2380
~ __plug_ipfromstring : 568 -> 564
~ __plug_decode : 508 -> 520
~ __plug_parseuser : 376 -> 372
CStrings:
+ "Out of Memory in /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/passwordserver_sasl/cyrus_sasl/plugins/plugin_common.c near line %d"
+ "Parameter Error in /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/passwordserver_sasl/cyrus_sasl/plugins/digestmd5.c near line %d"
+ "Parameter Error in /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/passwordserver_sasl/cyrus_sasl/plugins/plugin_common.c near line %d"
- "Out of Memory in /AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/passwordserver_sasl/cyrus_sasl/plugins/plugin_common.c near line %d"
- "Parameter Error in /AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/passwordserver_sasl/cyrus_sasl/plugins/digestmd5.c near line %d"
- "Parameter Error in /AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/passwordserver_sasl/cyrus_sasl/plugins/plugin_common.c near line %d"

```
