## ANECompiler

> `/System/Library/PrivateFrameworks/ANECompiler.framework/ANECompiler`

```diff

-8.3.15.1.0
-  __TEXT.__text: 0x125cf70
+8.4.1.0.0
+  __TEXT.__text: 0x125dba4
   __TEXT.__auth_stubs: 0x2140
   __TEXT.__init_offsets: 0x4
-  __TEXT.__const: 0x7843c
-  __TEXT.__cstring: 0x91a8c
-  __TEXT.__gcc_except_tab: 0x6e084
+  __TEXT.__const: 0x7852c
+  __TEXT.__cstring: 0x91af7
+  __TEXT.__gcc_except_tab: 0x6e114
   __TEXT.__oslogstring: 0x161fd
-  __TEXT.__unwind_info: 0x394b8
+  __TEXT.__unwind_info: 0x394e0
   __TEXT.__eh_frame: 0x2488
   __DATA_CONST.__got: 0x1c8
   __DATA_CONST.__const: 0x3640
   __AUTH_CONST.__auth_got: 0x10a8
   __AUTH_CONST.__auth_ptr: 0x80
-  __AUTH_CONST.__const: 0x71e98
+  __AUTH_CONST.__const: 0x71ec8
   __AUTH_CONST.__cfstring: 0x7f80
   __AUTH.__data: 0x3618
   __AUTH.__thread_vars: 0xf0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libncurses.5.4.dylib
-  Functions: 72950
-  Symbols:   85416
-  CStrings:  15722
+  Functions: 72962
+  Symbols:   85427
+  CStrings:  15725
 
CStrings:
+ "Enforced per-TD latency violation on Task %zd.  Current latency: (%.0f us).  Upper bound: (%.0f us).  Related OpLayers: %s.  Compilation will FAIL.\n"
+ "It is not a qualifying attention branch"
+ "Scheduled branch must not be empty"
+ "queue must be empty"
- "Enforced per-TD latency violation.  Current latency: (%.0f us).  Upper bound: (%.0f us).  Related OpLayers: %s.  Compilation will FAIL.\n"

```
