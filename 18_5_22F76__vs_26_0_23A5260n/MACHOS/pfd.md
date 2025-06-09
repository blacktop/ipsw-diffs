## pfd

> `/usr/libexec/pfd`

```diff

-111.0.0.0.0
-  __TEXT.__text: 0x6b04
-  __TEXT.__auth_stubs: 0x6a0
-  __TEXT.__const: 0x2180
-  __TEXT.__cstring: 0x14e9
+112.0.0.0.0
+  __TEXT.__text: 0x72c8
+  __TEXT.__auth_stubs: 0x6d0
+  __TEXT.__const: 0x2190
+  __TEXT.__cstring: 0x1598
   __TEXT.__oslogstring: 0x1e
-  __TEXT.__unwind_info: 0x100
-  __DATA_CONST.__auth_got: 0x350
+  __TEXT.__unwind_info: 0x108
+  __DATA_CONST.__auth_got: 0x368
   __DATA_CONST.__got: 0x90
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__const: 0xe0
   __DATA_CONST.__cfstring: 0x80
-  __DATA.__data: 0x394
+  __DATA.__data: 0x3b4
   __DATA.__common: 0x10
   __DATA.__bss: 0x8c
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/PrivateFrameworks/PacketFilter.framework/PacketFilter
   - /usr/lib/libSystem.B.dylib
-  UUID: 4E66CD4F-FCD6-3A59-8BC9-DFA4D8ED17A9
-  Functions: 53
-  Symbols:   129
-  CStrings:  297
+  UUID: 5F39BAC0-5070-31B5-AD6B-97C95F826ED6
+  Functions: 56
+  Symbols:   132
+  CStrings:  306
 
Symbols:
+ ___strcpy_chk
+ _xpc_array_get_string
+ _xpc_string_get_string_ptr
CStrings:
+ "%s: %s"
+ "Invalid table name"
+ "address-table"
+ "cannot parse addr %s, errno %s"
+ "com.apple.%s/%s"
+ "network_isolation"
+ "table name %s too long, max size is %u"
+ "table_address_array"
+ "table_name"

```
