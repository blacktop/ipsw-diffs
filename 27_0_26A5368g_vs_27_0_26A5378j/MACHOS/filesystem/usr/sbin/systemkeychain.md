## systemkeychain

> `/usr/sbin/systemkeychain`

```diff

-  __TEXT.__text: 0xe744
-  __TEXT.__auth_stubs: 0xae0
+  __TEXT.__text: 0xe9f0
+  __TEXT.__auth_stubs: 0xaf0
   __TEXT.__const: 0xe28
   __TEXT.__gcc_except_tab: 0x125c
   __TEXT.__cstring: 0x626
   __TEXT.__oslogstring: 0x168
   __TEXT.__dof_security_: 0x33c
-  __TEXT.__unwind_info: 0x850
-  __DATA_CONST.__const: 0x2888
-  __DATA_CONST.__auth_got: 0x578
+  __TEXT.__unwind_info: 0x858
+  __DATA_CONST.__const: 0x28b8
+  __DATA_CONST.__auth_got: 0x580
   __DATA_CONST.__got: 0xb8
   __DATA.__data: 0x8
   __DATA.__thread_vars: 0x18

   - /System/Library/Frameworks/Security.framework/Versions/A/Security
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  Functions: 361
-  Symbols:   205
+  Functions: 365
+  Symbols:   206
   CStrings:  75
 
Sections:
~ __TEXT.__gcc_except_tab : content changed
~ __TEXT.__dof_security_ : content changed
~ __DATA_CONST.__got : content changed
~ __DATA.__data : content changed
~ __DATA.__thread_vars : content changed
Symbols:
+ _malloc_type_calloc

```
