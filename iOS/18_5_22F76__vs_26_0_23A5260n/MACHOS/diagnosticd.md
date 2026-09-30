## diagnosticd

> `/usr/libexec/diagnosticd`

```diff

-1643.120.5.0.0
-  __TEXT.__text: 0x7c94
-  __TEXT.__auth_stubs: 0xf40
+1815.0.0.0.0
+  __TEXT.__text: 0x7f08
+  __TEXT.__auth_stubs: 0xf50
   __TEXT.__objc_stubs: 0x460
   __TEXT.__objc_methlist: 0x50
-  __TEXT.__const: 0x458
-  __TEXT.__cstring: 0x17e9
+  __TEXT.__const: 0x468
+  __TEXT.__cstring: 0x197c
   __TEXT.__objc_methname: 0x33c
   __TEXT.__objc_classname: 0x11
   __TEXT.__objc_methtype: 0x50
   __TEXT.__unwind_info: 0x1a8
-  __DATA_CONST.__auth_got: 0x7a8
+  __DATA_CONST.__auth_got: 0x7b0
   __DATA_CONST.__got: 0x128
   __DATA_CONST.__auth_ptr: 0x18
-  __DATA_CONST.__const: 0x800
+  __DATA_CONST.__const: 0x7d8
   __DATA_CONST.__cfstring: 0x940
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA.__objc_data: 0x50
   __DATA.__os_assumes_log: 0x8
   __DATA.__data: 0x1a4
-  __DATA.__crash_info: 0x40
+  __DATA.__crash_info: 0x148
   __DATA.__bss: 0x1d0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/liblockdown.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 5181640E-490A-300B-952D-05A8DFDAB9B8
+  UUID: DC8EC3B1-33A9-33DE-A22D-6B84DE4DB29C
   Functions: 91
-  Symbols:   292
-  CStrings:  331
+  Symbols:   293
+  CStrings:  334
 
Symbols:
+ __os_activity_stream_entry_get_version
+ __os_trace_calloc_typed
- __os_trace_calloc
Functions:
~ sub_100000e7c -> sub_100000ecc : 416 -> 432
~ sub_1000010f8 -> sub_100001158 : 1452 -> 1292
~ sub_10000198c -> sub_10000194c : 336 -> 368
~ sub_1000028f8 -> sub_1000028d8 : 1240 -> 1248
~ sub_100003870 -> sub_100003858 : 2076 -> 2104
~ sub_100004830 -> sub_100004834 : 2280 -> 2672
~ sub_100006044 -> sub_1000061d0 : 484 -> 500
~ sub_100006228 -> sub_1000063c4 : 248 -> 264
~ sub_100006918 -> sub_100006ac4 : 976 -> 968
~ sub_100007040 -> sub_1000071e4 : 904 -> 1040
~ sub_100007eb4 -> sub_1000080e0 : 1588 -> 1604
~ sub_100008758 -> sub_100008994 : 548 -> 104
~ sub_10000897c -> sub_1000089fc : 160 -> 604
~ sub_100008a1c -> sub_100008c58 : 24 -> 160
CStrings:
+ "BUG IN LIBTRACE: Nope. Invalid stream object version"
+ "OSLogDarwin_C.c"
+ "entryData"

```
