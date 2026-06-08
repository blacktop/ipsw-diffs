## ifconfig

> `/sbin/ifconfig`

```diff

-741.100.2.0.0
-  __TEXT.__text: 0xbbd4
+754.0.0.0.0
+  __TEXT.__text: 0xbbf4
   __TEXT.__auth_stubs: 0x4a0
   __TEXT.__init_offsets: 0x2c
   __TEXT.__const: 0x1f0
-  __TEXT.__cstring: 0x3a08
+  __TEXT.__cstring: 0x3a2e
   __TEXT.__unwind_info: 0x218
+  __DATA_CONST.__const: 0x280
   __DATA_CONST.__auth_got: 0x250
   __DATA_CONST.__got: 0x38
-  __DATA_CONST.__const: 0x280
   __DATA.__data: 0x2dd8
   __DATA.__common: 0x7c
   __DATA.__bss: 0x1260
   - /usr/lib/libSystem.B.dylib
-  UUID: 18A7B5EA-FA65-3CEC-98DC-A01559AC60CB
+  UUID: 05FC0C84-0943-3DE4-8922-C52513861F3D
   Functions: 254
   Symbols:   443
   CStrings:  841
Functions:
~ _bond_status : 740 -> 744
~ _main : 8296 -> 8308
~ _bridge_status : 3352 -> 3368
CStrings:
+ "\tforwarded pkts: %llu\n"
- "sysctl IFDATA_SUPPLEMENTAL"

```
