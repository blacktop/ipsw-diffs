## zipsplit

> `/usr/bin/zipsplit`

```diff

-  __TEXT.__text: 0x9020
+  __TEXT.__text: 0x906c
   __TEXT.__auth_stubs: 0x370
   __TEXT.__cstring: 0x28eb
   __TEXT.__const: 0x110
Sections:
~ __TEXT.__cstring : content changed
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__const : content changed
~ __DATA.__data : content changed
~ __DATA.__common : content changed
~ __DATA.__bss : content changed
Functions:
~ sub_100000a2c : 3836 -> 3824
~ sub_100006edc -> sub_100006ed0 : 2180 -> 2188
~ sub_100007760 -> sub_10000775c : 1224 -> 1232
~ sub_100008078 -> sub_10000807c : 2776 -> 2804
~ sub_100008b50 -> sub_100008b70 : 1044 -> 1088
CStrings:
+ " on Jun 22 2026"
+ "gcc Apple LLVM 21.0.0 (clang-2100.3.25.1) [+internal-os]"
- " on Jun  9 2026"
- "gcc Apple LLVM 21.0.0 (clang-2100.3.23.3) [+internal-os]"

```
