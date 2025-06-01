## libsqlite3.dylib

> `/usr/lib/libsqlite3.dylib`

```diff

-349.1.0.0.0
-  __TEXT.__text: 0x156f50
+349.3.0.0.0
+  __TEXT.__text: 0x1570ac
   __TEXT.__auth_stubs: 0xa10
   __TEXT.__const: 0x7aa8
-  __TEXT.__cstring: 0xb9a3
-  __TEXT.__oslogstring: 0x498
-  __TEXT.__unwind_info: 0x1d58
+  __TEXT.__cstring: 0xb856
+  __TEXT.__oslogstring: 0x610
+  __TEXT.__unwind_info: 0x1d5c
   __DATA_CONST.__got: 0x68
   __DATA_CONST.__const: 0x1c38
   __AUTH_CONST.__const: 0x1100

   __DATA_DIRTY.__data: 0x2e30
   __DATA_DIRTY.__bss: 0x32e
   - /usr/lib/libSystem.B.dylib
-  UUID: 890023FA-73C5-3897-AC87-BB31EC254531
-  Functions: 2440
+  UUID: 48C19B53-12D5-3A2E-B452-7505022C1B29
+  Functions: 2443
   Symbols:   541
-  CStrings:  2128
+  CStrings:  2129
 
CStrings:
+ "Failed to open temporary file at path %s: %s"
+ "No temporary directory is accessible.  This is not a legitimate configuration.  Either the process environment or its sandbox is misconfigured.  Various library routines will error out abruptly."
+ "_CS_DARWIN_USER_TEMP_DIR was deleted out from underneath this process. This is illegal and likely to cause crashes and data corruption."
- "No temporary directory is accessible.  This is not a legitimate configuration.  Either the process environment or its sandbox is misconfigured.  Various library routines will error out abruptly.\n"
- "_CS_DARWIN_USER_TEMP_DIR was deleted out from underneath this process. This is illegal and likely to cause crashes and data corruption.\n"

```
