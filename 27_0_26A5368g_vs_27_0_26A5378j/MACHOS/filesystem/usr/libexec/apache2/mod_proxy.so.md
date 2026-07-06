## mod_proxy.so

> `/usr/libexec/apache2/mod_proxy.so`

```diff

-  __TEXT.__text: 0x281b4
+  __TEXT.__text: 0x281cc
   __TEXT.__auth_stubs: 0xe10
   __TEXT.__cstring: 0x4d42
   __TEXT.__unwind_info: 0x1b8
Sections:
~ __TEXT.__cstring : content changed
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__const : content changed
~ __DATA.__data : content changed
Functions:
~ _ap_proxy_canonenc_ex : 1024 -> 1032
~ _proxy_match_domainname : 388 -> 396
~ _ap_proxy_location_reverse_map : 1608 -> 1616
CStrings:
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.HCJruC/Sources/apache/httpd/modules/proxy/mod_proxy.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.HCJruC/Sources/apache/httpd/modules/proxy/proxy_util.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.QaP6H4/Sources/apache/httpd/modules/proxy/mod_proxy.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.QaP6H4/Sources/apache/httpd/modules/proxy/proxy_util.c"

```
