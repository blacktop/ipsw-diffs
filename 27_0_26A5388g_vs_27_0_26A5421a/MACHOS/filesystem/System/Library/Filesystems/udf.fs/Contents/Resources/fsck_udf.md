## fsck_udf

> `/System/Library/Filesystems/udf.fs/Contents/Resources/fsck_udf`

### Sections with Same Size but Changed Content

- `__TEXT.__init_offsets`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__data`

```diff

-329.0.0.0.0
-  __TEXT.__text: 0x10dbc
+331.0.0.0.0
+  __TEXT.__text: 0x10e04
   __TEXT.__auth_stubs: 0x420
   __TEXT.__init_offsets: 0x8
   __TEXT.__gcc_except_tab: 0x604
-  __TEXT.__cstring: 0x34fe
+  __TEXT.__cstring: 0x35c9
   __TEXT.__const: 0x4f5c
   __TEXT.__unwind_info: 0x538
   __DATA_CONST.__const: 0x348

   - /usr/lib/libc++.1.dylib
   Functions: 366
   Symbols:   84
-  CStrings:  388
+  CStrings:  390
 
Functions:
~ sub_100003eec : 484 -> 556
CStrings:
+ "VarIterator.ReadCurEntry entry length exceeds stream length: byteOffset: %lld  curEntryLength: %u"
+ "VarIterator.ReadCurEntry invalid entry: byteOffset: %lld  curEntryLength: %u"
+ "VarIterator.ReadCurEntry overflowed while calculating byte range: byteOffset: %lld, curEntryLength: %u"
- "VarIterator.ReadCurEntry invalid entry: byteOffset: %u  curEntryLength: %u"
```
