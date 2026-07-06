## libutil.dylib

> `/usr/lib/libutil.dylib`

```diff

-  __TEXT.__text: 0x2584
+  __TEXT.__text: 0x2590
   __TEXT.__const: 0x118
   __TEXT.__cstring: 0xf9
   __TEXT.__gcc_except_tab: 0x6c
Sections:
~ __TEXT.__gcc_except_tab : content changed
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__const : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__weak_auth_got : content changed
Functions:
~ __ZN13ExtentManager4InitEjjx -> _getmntopts : 104 -> 528
~ __ZN13ExtentManager19AddBlockRangeExtentExx -> _freemntopts : 376 -> 68
~ __ZN13ExtentManager22RemoveBlockRangeExtentExx -> __ZN13ExtentManager4InitEjjx : 268 -> 104
~ __ZN13ExtentManager18AddByteRangeExtentExx -> __ZN13ExtentManager19AddBlockRangeExtentExx : 36 -> 376
~ _getmntoptstr -> __ZN13ExtentManager22RemoveBlockRangeExtentExx : 152 -> 268
~ _getmntoptnum -> __ZN13ExtentManager18AddByteRangeExtentExx : 264 -> 36
~ _freemntopts -> _getmntoptstr : 68 -> 152
~ _getmntopts -> _getmntoptnum : 516 -> 264

```
