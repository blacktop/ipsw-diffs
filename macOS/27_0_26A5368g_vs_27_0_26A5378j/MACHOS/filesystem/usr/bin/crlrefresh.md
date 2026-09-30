## crlrefresh

> `/usr/bin/crlrefresh`

```diff

-  __TEXT.__text: 0x1058
-  __TEXT.__auth_stubs: 0x300
+  __TEXT.__text: 0x11b0
+  __TEXT.__auth_stubs: 0x310
   __TEXT.__const: 0x168
   __TEXT.__cstring: 0x285
   __TEXT.__gcc_except_tab: 0x98
   __TEXT.__oslogstring: 0xb4
   __TEXT.__dof_security_: 0x207
-  __TEXT.__unwind_info: 0xf0
-  __DATA_CONST.__const: 0x198
-  __DATA_CONST.__auth_got: 0x188
+  __TEXT.__unwind_info: 0xf8
+  __DATA_CONST.__const: 0x1c8
+  __DATA_CONST.__auth_got: 0x190
   __DATA_CONST.__got: 0x28
   __DATA.__data: 0x40
   __DATA.__bss: 0x18

   - /System/Library/Frameworks/Security.framework/Versions/A/Security
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  Functions: 36
-  Symbols:   60
+  Functions: 40
+  Symbols:   61
   CStrings:  30
 
Sections:
~ __TEXT.__dof_security_ : content changed
~ __DATA_CONST.__got : content changed
Symbols:
+ _malloc_type_calloc

```
