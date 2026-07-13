## apfs_vol_converter

> `/System/Library/Filesystems/apfs.fs/apfs_vol_converter`

```diff

-  __TEXT.__text: 0x59ad4
+  __TEXT.__text: 0x59c98
   __TEXT.__auth_stubs: 0xa10
   __TEXT.__init_offsets: 0x4
   __TEXT.__const: 0xbf0
-  __TEXT.__cstring: 0x11f3e
+  __TEXT.__cstring: 0x1201d
   __TEXT.__gcc_except_tab: 0x680
   __TEXT.__unwind_info: 0xc48
   __DATA_CONST.__auth_got: 0x510

   - /usr/lib/libutil.dylib
   Functions: 884
   Symbols:   187
-  CStrings:  1700
+  CStrings:  1703
 
Sections:
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__cfstring : content changed
~ __DATA.__data : content changed
Functions:
~ sub_10003dc90 : 1192 -> 1632
~ sub_10004032c -> sub_1000404e4 : 12056 -> 12064
~ sub_100049448 -> sub_100049608 : 632 -> 636
CStrings:
+ "%s:%d: %s Invalid reap list free entry %d\n"
+ "%s:%d: %s reap list object 0x%llx first index %u larger than max index %u\n"
+ "%s:%d: %s reap list object 0x%llx free index %u larger than max index %u\n"
+ "%s:%d: %s reap list object 0x%llx last index %u larger than max index %u\n"
+ "%s:%d: %s reap list object expected %u entries, max %u, but we walked %u\n"
+ "%s:%d: %s reap list object expected %u entries, max %u, but we walked %u + %u = %u\n"
+ "2811.160.7.0.4"
- "%s:%d: %s reap list object 0x%llx first index %u larger than max %u\n"
- "%s:%d: %s reap list object 0x%llx free index %u larger than max %u\n"
- "%s:%d: %s reap list object 0x%llx last index %u larger than max %u\n"
- "2811.160.7"

```
