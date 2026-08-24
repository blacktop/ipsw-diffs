## OSInstaller

> `/System/Library/PrivateFrameworks/OSInstaller.framework/Versions/A/OSInstaller`

```diff

-1638.0.0.0.0
-  __TEXT.__text: 0x5a568
+1639.0.1.0.0
+  __TEXT.__text: 0x5a654
   __TEXT.__objc_methlist: 0x3694
-  __TEXT.__cstring: 0x10345
+  __TEXT.__cstring: 0x1035b
   __TEXT.__gcc_except_tab: 0x2308
   __TEXT.__ustring: 0x34
   __TEXT.__const: 0x178
-  __TEXT.__oslogstring: 0xe14
+  __TEXT.__oslogstring: 0xe2a
   __TEXT.__unwind_info: 0xcb8
   __TEXT.__eh_frame: 0x7c
   __TEXT.__objc_stubs: 0x0

   - /usr/lib/libimage4.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libpartition2_dynamic.dylib
-  Functions: 1418
-  Symbols:   3789
-  CStrings:  1834
+  Functions: 1419
+  Symbols:   3791
+  CStrings:  1835
 
Symbols:
+ _disk_is_virtual
+ disk_is_virtual
Functions:
~ _bless2_summarize : 2592 -> 2596
~ _bless2_os_preboot : 48 -> 56
+ _disk_is_virtual
- bless2_summarize.cold.3
+ disk_is_virtual.cold.1
CStrings:
+ "disk is vitual ?: %d\n"
```
