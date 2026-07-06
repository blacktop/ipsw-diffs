## mod_autoindex.so

> `/usr/libexec/apache2/mod_autoindex.so`

```diff

-  __TEXT.__text: 0x6570
+  __TEXT.__text: 0x65e0
   __TEXT.__auth_stubs: 0x4f0
   __TEXT.__cstring: 0xf5f
   __TEXT.__unwind_info: 0x80
Sections:
~ __TEXT.__cstring : content changed
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__const : content changed
~ __DATA.__data : content changed
Functions:
~ _index_directory : 3180 -> 3212
~ _output_directories : 7328 -> 7376
~ _find_title : 820 -> 844
~ _terminate_description : 600 -> 608
CStrings:
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.HCJruC/Sources/apache/httpd/modules/generators/mod_autoindex.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.QaP6H4/Sources/apache/httpd/modules/generators/mod_autoindex.c"

```
