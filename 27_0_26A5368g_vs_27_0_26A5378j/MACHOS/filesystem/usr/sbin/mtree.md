## mtree

> `/usr/sbin/mtree`

```diff

-  __TEXT.__text: 0x8e50
+  __TEXT.__text: 0x8e80
   __TEXT.__auth_stubs: 0x7a0
   __TEXT.__const: 0x6f7
-  __TEXT.__cstring: 0x15bd
+  __TEXT.__cstring: 0x15bf
   __TEXT.__unwind_info: 0x198
   __DATA_CONST.__const: 0x130
   __DATA_CONST.__cfstring: 0x20

   __DATA.__common: 0x500
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /usr/lib/libSystem.B.dylib
-  Functions: 146
+  Functions: 147
   Symbols:   138
   CStrings:  274
 
Sections:
~ __TEXT.__const : content changed
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__cfstring : content changed
~ __DATA.__data : content changed
CStrings:
+ "cdef:iK:k:LNnPp:qrs:UuvwxX:m:F:t:E:SD"
+ "usage: mtree [-LPUScdeinNqruxwD] [-f spec] [-K key] [-k key] [-p path] [-s seed] [-m xml dictionary] [-t timestamp]\n\t[-X excludes]\n"
- "cdef:iK:k:LnPp:qrs:UuvwxX:m:F:t:E:SD"
- "usage: mtree [-LPUScdeinqruxwD] [-f spec] [-K key] [-k key] [-p path] [-s seed] [-m xml dictionary] [-t timestamp]\n\t[-X excludes]\n"

```
