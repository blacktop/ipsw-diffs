## libcopyfile.dylib

> `/usr/lib/system/libcopyfile.dylib`

```diff

-  __TEXT.__text: 0x7e80
+  __TEXT.__text: 0x7ef8
   __TEXT.__const: 0x1c8
   __TEXT.__cstring: 0x1c51
-  __TEXT.__unwind_info: 0xf8
+  __TEXT.__unwind_info: 0x100
   __TEXT.__auth_stubs: 0x0
   __DATA_CONST.__const: 0x3b0
   __DATA_CONST.__got: 0x0
Sections:
~ __TEXT.__const : content changed
~ __TEXT.__cstring : content changed
~ __DATA_CONST.__const : content changed
~ __AUTH_CONST.__const : content changed
Functions:
~ _copyfile_internal : 7884 -> 7968
~ _nameInDefaultList : 152 -> 160
~ _xattr_intent_with_flags : 56 -> 64
~ _xattr_preserve_for_intent : 116 -> 136
CStrings:
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.bhGYBQ/Sources/copyfile/copyfile.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.eO9MVK/Sources/copyfile/copyfile.c"

```
