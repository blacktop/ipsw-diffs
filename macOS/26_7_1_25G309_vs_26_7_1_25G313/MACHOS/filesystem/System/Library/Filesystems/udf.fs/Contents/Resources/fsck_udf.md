## fsck_udf

> `System/Library/Filesystems/udf.fs/Contents/Resources/fsck_udf`

### Sections with Same Size but Changed Content

- `__TEXT.__init_offsets`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__data`

```diff

-324.160.3.700.3
-  __TEXT.__text: 0x10ed0
+324.160.3.701.4
+  __TEXT.__text: 0x10f18
   __TEXT.__auth_stubs: 0x420
   __TEXT.__init_offsets: 0x8
-  __TEXT.__cstring: 0x34fe
+  __TEXT.__cstring: 0x35c9
   __TEXT.__const: 0x4f5d
   __TEXT.__gcc_except_tab: 0x5c0
   __TEXT.__unwind_info: 0x518

   - /usr/lib/libc++.1.dylib
   Functions: 365
   Symbols:   84
-  CStrings:  388
+  CStrings:  390
 
Functions:
~ sub_100003e8c : 484 -> 556
CStrings:
+ "VarIterator.ReadCurEntry entry length exceeds stream length: byteOffset: %lld  curEntryLength: %u"
+ "VarIterator.ReadCurEntry invalid entry: byteOffset: %lld  curEntryLength: %u"
+ "VarIterator.ReadCurEntry overflowed while calculating byte range: byteOffset: %lld, curEntryLength: %u"
- "VarIterator.ReadCurEntry invalid entry: byteOffset: %u  curEntryLength: %u"
```
