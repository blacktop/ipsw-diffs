## libdispatch.dylib

> `/usr/lib/system/libdispatch.dylib`

```diff

-1605.60.4.0.0
-  __TEXT.__text: 0x3c52c
+1605.60.5.0.0
+  __TEXT.__text: 0x3c648
   __TEXT.__objc_methlist: 0x684
   __TEXT.__const: 0x750
   __TEXT.__cstring: 0x61a0
-  __TEXT.__unwind_info: 0x1158
+  __TEXT.__unwind_info: 0x1160
   __TEXT.__eh_frame: 0xb8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   - /usr/lib/system/libsystem_platform.dylib
   - /usr/lib/system/libsystem_pthread.dylib
   - /usr/lib/system/libunwind.dylib
-  Functions: 1381
+  Functions: 1383
   Symbols:   1789
   CStrings:  512
 
Functions:
~ _dispatch_data_create_with_transform : 220 -> 232
~ ____dispatch_transform_from_base32_with_table_block_invoke : 572 -> 588
~ ____dispatch_transform_from_base64_block_invoke : 480 -> 496
~ ____dispatch_transform_from_utf16_block_invoke : 876 -> 988
~ __dispatch_transform_buffer_new : 256 -> 180
~ ____dispatch_transform_to_utf16_block_invoke : 788 -> 792
~ _OUTLINED_FUNCTION_0 : 44 -> 28
+ _OUTLINED_FUNCTION_1
~ ____dispatch_transform_from_utf16_block_invoke.cold.1 : 72 -> 108
~ ____dispatch_transform_from_utf16_block_invoke.cold.2 : 40 -> 112
~ ____dispatch_transform_from_utf16_block_invoke.cold.3 : 132 -> 108
+ __dispatch_transform_buffer_new.cold.1
```
