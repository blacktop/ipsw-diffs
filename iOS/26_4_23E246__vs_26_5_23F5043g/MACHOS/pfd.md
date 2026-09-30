## pfd

> `/usr/libexec/pfd`

```diff

-114.100.1.0.0
-  __TEXT.__text: 0x7284
-  __TEXT.__auth_stubs: 0x6c0
+114.120.2.0.0
+  __TEXT.__text: 0x74b8
+  __TEXT.__auth_stubs: 0x6e0
   __TEXT.__const: 0x2190
-  __TEXT.__cstring: 0x1598
+  __TEXT.__cstring: 0x164c
   __TEXT.__oslogstring: 0x1e
-  __TEXT.__unwind_info: 0x108
-  __DATA_CONST.__auth_got: 0x360
+  __TEXT.__unwind_info: 0x110
+  __DATA_CONST.__auth_got: 0x370
   __DATA_CONST.__got: 0x90
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__const: 0xe0
   __DATA_CONST.__cfstring: 0x80
-  __DATA.__data: 0x3b4
+  __DATA.__data: 0x3c4
   __DATA.__common: 0x10
   __DATA.__bss: 0x8c
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/PrivateFrameworks/PacketFilter.framework/PacketFilter
   - /usr/lib/libSystem.B.dylib
-  UUID: 3C521E15-3A12-3531-87C3-8E80C3BB9F18
-  Functions: 61
-  Symbols:   131
-  CStrings:  306
+  UUID: D4C46982-7C1E-3AEF-B615-2F72C9DE64FF
+  Functions: 63
+  Symbols:   133
+  CStrings:  314
 
Symbols:
+ ___memcpy_chk
+ _xpc_dictionary_get_data
Functions:
~ sub_100001acc : 5988 -> 6120
+ sub_1000072e8
CStrings:
+ "%s (dst): %m"
+ "%s (src): %m"
+ "delete_address"
+ "delete_af"
+ "deleting states for address %s (af=%d)"
+ "invalid address family %d"
+ "missing delete address"
+ "pf states deleted for address %s (af=%d)"

```
