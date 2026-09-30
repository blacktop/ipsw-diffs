## date

> `/bin/date`

```diff

-319.0.1.0.0
-  __TEXT.__text: 0x1584
-  __TEXT.__auth_stubs: 0x1f0
-  __TEXT.__const: 0x7e
-  __TEXT.__cstring: 0x357
-  __TEXT.__unwind_info: 0xa0
-  __DATA_CONST.__auth_got: 0xf8
+326.0.0.0.0
+  __TEXT.__text: 0x16fc
+  __TEXT.__auth_stubs: 0x210
+  __TEXT.__const: 0x68
+  __TEXT.__cstring: 0x39d
+  __TEXT.__unwind_info: 0xa8
+  __DATA_CONST.__auth_got: 0x108
   __DATA_CONST.__got: 0x20
-  __DATA_CONST.__const: 0x40
+  __DATA_CONST.__const: 0x50
   __DATA.__data: 0x160
-  __DATA.__bss: 0x18
+  __DATA.__bss: 0x10
   - /usr/lib/libSystem.B.dylib
-  UUID: 87B2315B-231B-3BE9-A2CE-C96B753B29F2
-  Functions: 17
-  Symbols:   37
-  CStrings:  55
+  UUID: 1CB48788-E620-371D-8DF4-2D2BA79D43C6
+  Functions: 19
+  Symbols:   39
+  CStrings:  61
 
Symbols:
+ _asprintf
+ _clock_gettime
+ _clock_settime
+ _strdup
- _settimeofday
- _time
CStrings:
+ "            [ -z output_zone ] [-r filename|seconds] [-v[+|-]val[y|m|w|d|H|M|S]]"
+ "%.*s%.9ld%s"
+ ",%N"
+ "asprintf"
+ "clock_gettime"
+ "clock_settime"
+ "f:I::jnRr:uv:z:"
+ "ns"
+ "setenv(TZ)"
+ "strdup"
+ "usage: date [-jnRu] [-I[date|hours|minutes|seconds|ns]] [-f input_fmt]"
- "            [-r filename|seconds] [-v[+|-]val[y|m|w|d|H|M|S]]"
- "f:I::jnRr:uv:"
- "settimeofday (timeval)"
- "time"
- "usage: date [-jnRu] [-I[date|hours|minutes|seconds]] [-f input_fmt]"

```
