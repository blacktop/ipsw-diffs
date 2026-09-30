## libquic.dylib

> `/usr/lib/libquic.dylib`

```diff

-6681.0.514.0.4
-  __TEXT.__text: 0xd0850
+6681.1.1.0.0
+  __TEXT.__text: 0xd0b24
   __TEXT.__objc_methlist: 0x244
   __TEXT.__const: 0x395
-  __TEXT.__cstring: 0x87e1
-  __TEXT.__oslogstring: 0x123da
-  __TEXT.__unwind_info: 0xcc8
+  __TEXT.__cstring: 0x8823
+  __TEXT.__oslogstring: 0x12459
+  __TEXT.__unwind_info: 0xcc0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1be0
+  __DATA_CONST.__const: 0x1c00
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x1e8

   __AUTH_CONST.__const: 0x1870
   __AUTH_CONST.__cfstring: 0x1320
   __AUTH_CONST.__objc_const: 0xf8
-  __AUTH_CONST.__auth_got: 0xd48
+  __AUTH_CONST.__auth_got: 0xd50
   __AUTH.__objc_data: 0x50
   __AUTH.__data: 0x118
   __DATA.__objc_ivar: 0xc

   - /System/Library/Frameworks/Security.framework/Versions/A/Security
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1165
-  Symbols:   1715
-  CStrings:  2603
+  Functions: 1168
+  Symbols:   1719
+  CStrings:  2606
 
Symbols:
+ __quic_migration_migrate_block_invoke
+ _nw_parameters_is_fallback
+ _quic_conn_is_cellular_fallback
+ _quic_path_set_is_preferred_address
CStrings:
+ "%{public}s %{public}s [%{public}s-%{public}s] skipping probe connectivity keep-alive over companion link on non-watch platform"
+ "quic_conn_is_cellular_fallback"
+ "quic_path_set_is_preferred_address"
```
