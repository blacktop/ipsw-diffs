## libMainThreadChecker.dylib

> `/usr/lib/libMainThreadChecker.dylib`

```diff

-64575.39.1.0.0
-  __TEXT.__text: 0x41fa8
+64578.47.1.0.0
+  __TEXT.__text: 0x41f90
   __TEXT.__auth_stubs: 0x4d0
   __TEXT.__init_offsets: 0x4
   __TEXT.__const: 0xd8
   __TEXT.__cstring: 0x9ee
   __TEXT.__oslogstring: 0x3
-  __TEXT.__unwind_info: 0xd8
+  __TEXT.__unwind_info: 0xe8
+  __DATA_CONST.__const: 0x118
+  __DATA_CONST.__cfstring: 0x20
   __DATA_CONST.__auth_got: 0x268
   __DATA_CONST.__got: 0x30
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x118
-  __DATA_CONST.__cfstring: 0x20
   __DATA.__data: 0x10
   __DATA.__bss: 0x1000e0
   __DATA.__common: 0x20

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 27639B66-7CA1-3F32-854B-4A2753182C9D
+  UUID: 05C22B9D-C3AF-360C-8F9A-0391FED91F5D
   Functions: 32
   Symbols:   158
   CStrings:  121
Functions:
~ _resetDyldInsertLibraries : 432 -> 436
~ ___ASSERT_API_MUST_BE_CALLED_FROM_MAIN_THREAD_FAILED__ : 1040 -> 1048
~ ___library_initializer : 2348 -> 2352
~ _SwizzleClasses : 1396 -> 1400
~ __ASSERT_API_MUST_BE_CALLED_FROM_MAIN_THREAD_FAILED__.cold.2 : 120 -> 76

```
