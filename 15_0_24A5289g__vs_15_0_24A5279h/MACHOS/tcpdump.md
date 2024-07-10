## tcpdump

> `/usr/sbin/tcpdump`

```diff

-141.0.0.0.0
-  __TEXT.__text: 0x97c50
-  __TEXT.__auth_stubs: 0xca0
-  __TEXT.__const: 0xc41
+140.0.0.0.0
+  __TEXT.__text: 0x97a74
+  __TEXT.__auth_stubs: 0xc80
+  __TEXT.__const: 0xc29
   __TEXT.__cstring: 0x36f04
-  __TEXT.__oslogstring: 0xa8
   __TEXT.__unwind_info: 0xc50
-  __DATA_CONST.__auth_got: 0x650
-  __DATA_CONST.__got: 0x40
+  __DATA_CONST.__auth_got: 0x640
+  __DATA_CONST.__got: 0x38
   __DATA_CONST.__const: 0x228f8
   __DATA.__data: 0x3890
   __DATA.__bss: 0x161b29

   - /usr/lib/libpcap.A.dylib
   - /usr/lib/libssl.48.dylib
   Functions: 1030
-  Symbols:   2541
+  Symbols:   2538
   CStrings:  12216
 
Symbols:
- __os_log_default
- __os_log_impl
- _os_log_type_enabled

```
