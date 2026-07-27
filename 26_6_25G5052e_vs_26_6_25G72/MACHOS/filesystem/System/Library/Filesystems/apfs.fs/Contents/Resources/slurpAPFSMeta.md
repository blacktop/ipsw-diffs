## slurpAPFSMeta

> `/System/Library/Filesystems/apfs.fs/Contents/Resources/slurpAPFSMeta`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__data`

```diff

-2811.160.6.0.0
-  __TEXT.__text: 0x36430
+2811.160.7.0.4
+  __TEXT.__text: 0x365f8
   __TEXT.__auth_stubs: 0x830
-  __TEXT.__cstring: 0x8aa5
+  __TEXT.__cstring: 0x8b6e
   __TEXT.__const: 0x1e0
   __TEXT.__unwind_info: 0x680
   __DATA_CONST.__auth_got: 0x418

   - /usr/lib/libSystem.B.dylib
   Functions: 520
   Symbols:   144
-  CStrings:  752
+  CStrings:  755
 
Functions:
~ sub_10001949c : 632 -> 636
~ sub_1000256c8 -> sub_1000256cc : 168 -> 180
~ sub_1000313c0 -> sub_1000313d0 : 1192 -> 1632
CStrings:
+ "%s:%d: %s Invalid reap list free entry %d\n"
+ "%s:%d: %s reap list object expected %u entries, max %u, but we walked %u\n"
+ "%s:%d: %s reap list object expected %u entries, max %u, but we walked %u + %u = %u\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Yjd3GC/Sources/apfs_executables/nx/obj.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7XiiiP/Sources/apfs_executables/nx/obj.c"
```
