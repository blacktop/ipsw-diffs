## APFS

> `/System/Library/PrivateFrameworks/APFS.framework/APFS`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__DATA.__data`
- `__DATA_DIRTY.__data`

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
   Symbols:   1103
-  CStrings:  1388
+  CStrings:  1391
 
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
