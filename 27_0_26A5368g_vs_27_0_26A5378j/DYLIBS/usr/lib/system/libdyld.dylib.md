## libdyld.dylib

> `/usr/lib/system/libdyld.dylib`

```diff

-  __TEXT.__text: 0x1eb6c
+  __TEXT.__text: 0x1f1d4
   __TEXT.__const: 0x32c
-  __TEXT.__cstring: 0x4bf0
+  __TEXT.__cstring: 0x4cc5
   __TEXT.__gcc_except_tab: 0x20
-  __TEXT.__unwind_info: 0xe78
+  __TEXT.__unwind_info: 0xe70
   __TEXT.__auth_stubs: 0x0
   __DATA_CONST.__const: 0xd28
   __DATA_CONST.__helper: 0x8

   - /usr/lib/system/libsystem_pthread.dylib
   - /usr/lib/system/libunwind.dylib
   - /usr/lib/system/libxpc.dylib
-  Functions: 916
+  Functions: 915
   Symbols:   1483
-  CStrings:  537
+  CStrings:  541
 
Sections:
~ __TEXT.__const : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__helper : content changed
~ __DATA_CONST.__got : content changed
~ __AUTH_CONST.__const : content changed
~ __DATA.__data : content changed
Symbols:
+ __ZNK6mach_o6Policy26enforceSegmentSectionNamesEv
- __ZN6mach_o12read_uleb128ENSt3__14spanIKhLm18446744073709551615EEERmRb
CStrings:
+ "section '%s' has an empty segment name"
+ "section '%s' segment name '%s' does not match containing segment's name '%s'"
+ "section in segment '%s' has an empty section name"
+ "segment load command has an empty segment name"

```
