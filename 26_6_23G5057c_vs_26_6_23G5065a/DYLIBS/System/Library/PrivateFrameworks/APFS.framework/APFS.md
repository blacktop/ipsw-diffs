## APFS

> `/System/Library/PrivateFrameworks/APFS.framework/APFS`

```diff

-  __TEXT.__text: 0x532a0
+  __TEXT.__text: 0x53464
   __TEXT.__auth_stubs: 0xc40
   __TEXT.__const: 0x8540
-  __TEXT.__cstring: 0xe59e
+  __TEXT.__cstring: 0xe67d
   __TEXT.__oslogstring: 0x11b8
   __TEXT.__gcc_except_tab: 0x1c
   __TEXT.__unwind_info: 0x958

   - /usr/lib/libutil.dylib
   Functions: 881
   Symbols:   1934
-  CStrings:  1535
+  CStrings:  1538
 
Sections:
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__const : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__cfstring : content changed
~ __DATA.__data : content changed
~ __DATA_DIRTY.__data : content changed
Functions:
~ _omap_get : 628 -> 632
~ _nx_check : 12092 -> 12100
~ _nx_reaper_checkpoint_traverse : 1188 -> 1628
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
