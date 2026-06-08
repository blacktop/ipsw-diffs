## libgermantok.dylib

> `/usr/lib/libgermantok.dylib`

```diff

 31.0.0.0.0
-  __TEXT.__text: 0x1a18
-  __TEXT.__auth_stubs: 0x190
+  __TEXT.__text: 0x1a58
   __TEXT.__const: 0x7b
   __TEXT.__cstring: 0x4f
   __TEXT.__unwind_info: 0x70
-  __DATA_CONST.__got: 0x8
+  __TEXT.__auth_stubs: 0x0
+  __DATA_CONST.__got: 0x0
   __AUTH_CONST.__auth_got: 0xc8
   __DATA_DIRTY.__data: 0x40
   __DATA_DIRTY.__bss: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libicucore.A.dylib
-  UUID: F17C1DD4-962F-3DB2-B911-0591C5F1EB86
+  UUID: 4C0435E9-C072-3694-AFE3-F7762E5B0DE2
   Functions: 6
   Symbols:   43
   CStrings:  10
Functions:
~ ___btrie_find_common_prefix -> ___gt_getWordData : 600 -> 472
~ _germantok_tokenize : 3436 -> 3444
~ ___gt_getWordData -> ___btrie_find_common_prefix : 472 -> 604
~ ___gt_findSubstrings : 516 -> 532
~ ___gt_tokenizeHelper : 1628 -> 1664

```
