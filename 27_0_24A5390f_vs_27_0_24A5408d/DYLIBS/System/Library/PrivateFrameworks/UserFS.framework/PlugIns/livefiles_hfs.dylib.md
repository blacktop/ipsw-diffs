## livefiles_hfs.dylib

> `/System/Library/PrivateFrameworks/UserFS.framework/PlugIns/livefiles_hfs.dylib`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__weak_got`
- `__AUTH.__data`
- `__DATA.__data`

```diff

-750.0.0.0.0
-  __TEXT.__text: 0x3d360
+751.0.0.0.0
+  __TEXT.__text: 0x3d480
   __TEXT.__const: 0x4e60
-  __TEXT.__oslogstring: 0x5ecc
-  __TEXT.__cstring: 0x26fb
+  __TEXT.__oslogstring: 0x5ed7
+  __TEXT.__cstring: 0x270a
   __TEXT.__unwind_info: 0x6d8
   __TEXT.__auth_stubs: 0x0
   __DATA_CONST.__weak_got: 0x8

   - /usr/lib/libSystem.B.dylib
   Functions: 677
   Symbols:   646
-  CStrings:  747
+  CStrings:  751
 
Functions:
~ _replay_journal : 6220 -> 6368
~ _HeadTruncateFile : 1300 -> 1440
CStrings:
+ "\n"
+ "%s"
+ "0x%.8x"
+ "HeadTruncateFile: too many tail extents, marking volume inconsistent.\n"
+ "jnl: "
- "jnl: 0x%.8x 0x%.8x 0x%.8x 0x%.8x  0x%.8x 0x%.8x 0x%.8x 0x%.8x\n"
```
