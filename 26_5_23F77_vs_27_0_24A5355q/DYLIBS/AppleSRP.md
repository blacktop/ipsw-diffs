## AppleSRP

> `/System/Library/PrivateFrameworks/AppleSRP.framework/AppleSRP`

```diff

-37.0.0.0.0
-  __TEXT.__text: 0x4938
-  __TEXT.__auth_stubs: 0x260
+39.0.0.0.0
+  __TEXT.__text: 0x4998
   __TEXT.__const: 0x18
   __TEXT.__cstring: 0xba
   __TEXT.__unwind_info: 0x1e8
-  __DATA_CONST.__got: 0x10
-  __AUTH_CONST.__auth_got: 0x130
+  __TEXT.__auth_stubs: 0x0
+  __DATA_CONST.__got: 0x0
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__data: 0x1c0
   __DATA.__data: 0x49
   __DATA.__bss: 0x5
   - /usr/lib/libSystem.B.dylib
-  UUID: 8C649A89-E98B-3FDB-807E-669864245CD1
+  UUID: DB1EF9E3-FA85-3D01-9D87-94EF248296FD
   Functions: 135
   Symbols:   255
   CStrings:  9
Functions:
~ _t_serveropenraw : 500 -> 508
~ _t_servergetkey : 724 -> 720
~ _srp6_client_params : 352 -> 360
~ _srp6_server_params : 364 -> 372
~ _BigIntegerToString : 340 -> 348
~ _t_sessionkey : 472 -> 488
~ _t_fromb64 : 460 -> 488
~ _t_tob64 : 300 -> 308
~ _srp2945_client_params : 352 -> 360
~ _srp2945_server_params : 364 -> 372

```
