## mod_proxy_ftp.so

> `/usr/libexec/apache2/mod_proxy_ftp.so`

```diff

-  __TEXT.__text: 0xac18
+  __TEXT.__text: 0xac40
   __TEXT.__auth_stubs: 0x610
   __TEXT.__cstring: 0xefb
   __TEXT.__unwind_info: 0x88
Sections:
~ __TEXT.__cstring : content changed
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__const : content changed
~ __DATA.__data : content changed
Functions:
~ _proxy_send_dir_filter : 5780 -> 5796
~ _ftp_check_string : 284 -> 292
~ _decodeenc : 308 -> 316
~ _ftp_getrc_msg : 1016 -> 1024
CStrings:
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.HCJruC/Sources/apache/httpd/modules/proxy/mod_proxy_ftp.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.QaP6H4/Sources/apache/httpd/modules/proxy/mod_proxy_ftp.c"

```
