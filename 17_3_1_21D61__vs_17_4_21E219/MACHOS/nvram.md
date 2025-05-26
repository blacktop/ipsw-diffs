## nvram

> `/usr/sbin/nvram`

```diff

-970.0.4.0.0
-  __TEXT.__text: 0x1f08
-  __TEXT.__auth_stubs: 0x450
-  __TEXT.__const: 0x40
-  __TEXT.__cstring: 0x80a
-  __TEXT.__unwind_info: 0xa8
-  __DATA_CONST.__auth_got: 0x228
+979.100.8.0.0
+  __TEXT.__text: 0x2184
+  __TEXT.__auth_stubs: 0x470
+  __TEXT.__const: 0x48
+  __TEXT.__cstring: 0x9cb
+  __TEXT.__unwind_info: 0xa4
+  __DATA_CONST.__auth_got: 0x238
   __DATA_CONST.__got: 0x60
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__const: 0x20
   __DATA_CONST.__cfstring: 0x20
-  __DATA.__bss: 0xf
+  __DATA.__bss: 0x13
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
-  Functions: 41
-  Symbols:   85
-  CStrings:  73
+  Functions: 43
+  Symbols:   87
+  CStrings:  82
 
Symbols:
+ _csr_check
+ _strncmp
CStrings:
+ "\t-b         set variable using binary file. invoked with the following format: nvram -b <variable name> <binary file>"
+ "\t-d         delete the named variable(does not return error code)"
+ "\t-r         delete the named variable(returns error code if any)"
+ "\t-z         use system-options node if available (internal builds only)"
+ "Couldn't open binary file - '%s'"
+ "Error deleting variable - '%s': %s (0x%08x)"
+ "IONVRAM-DELETEWRET-PROPERTY"
+ "Invalid file size %d"
+ "missing arguments"
+ "unsupported option -z"
- "\t-d         delete the named variable"

```
