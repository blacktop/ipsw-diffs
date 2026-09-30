## mod_xml2enc.so

> `/usr/libexec/apache2/mod_xml2enc.so`

```diff

-879.0.0.0.0
-  __TEXT.__text: 0x58f4
+880.0.0.0.0
+  __TEXT.__text: 0x5248
   __TEXT.__auth_stubs: 0x2e0
   __TEXT.__cstring: 0x682
-  __TEXT.__unwind_info: 0x60
+  __TEXT.__unwind_info: 0x70
   __DATA_CONST.__auth_got: 0x170
   __DATA_CONST.__got: 0x20
   __DATA_CONST.__auth_ptr: 0x8

   - /usr/lib/libcrypto.46.dylib
   - /usr/lib/libssl.48.dylib
   - /usr/lib/libxml2.2.dylib
-  UUID: 92CDB4CB-7377-384B-97D9-A16EF7BAC0AF
+  UUID: 13FF1A6E-D495-3110-96A1-6F23490ACD51
   Functions: 13
   Symbols:   67
   CStrings:  50
Functions:
~ _xml2enc_config : 80 -> 76
~ _xml2enc_merge : 304 -> 268
~ _xml2enc_hooks : 248 -> 240
~ _xml2enc_run_preprocess : 272 -> 244
~ _set_default : 172 -> 156
~ _set_alias : 152 -> 132
~ _set_skipto : 144 -> 132
~ _xml2enc_ffunc : 12064 -> 11244
~ _xml2enc_filter_init : 216 -> 196
~ _xml2enc_filter : 696 -> 648
~ _xml2enc_charset : 236 -> 208
~ _sniff_encoding : 6432 -> 5912
~ _fix_skipto : 1756 -> 1608
CStrings:
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/filters/mod_xml2enc.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/filters/mod_xml2enc.c"

```
