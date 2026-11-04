## HealthDaemonFoundation

> `/System/Library/PrivateFrameworks/HealthDaemonFoundation.framework/HealthDaemonFoundation`

```diff

-7027.1.56.2.9
-  __TEXT.__text: 0x743c4
-  __TEXT.__objc_methlist: 0x3e34
+7027.2.13.0.0
+  __TEXT.__text: 0x74574
+  __TEXT.__objc_methlist: 0x3e64
   __TEXT.__const: 0x23a2
-  __TEXT.__cstring: 0x4b6b
+  __TEXT.__cstring: 0x4b7b
   __TEXT.__oslogstring: 0x37e5
-  __TEXT.__gcc_except_tab: 0x3118
+  __TEXT.__gcc_except_tab: 0x3124
   __TEXT.__swift5_typeref: 0xd2c
   __TEXT.__swift5_reflstr: 0x90b
   __TEXT.__swift5_assocty: 0xa8

   __TEXT.__swift5_protos: 0x38
   __TEXT.__swift5_mpenum: 0x24
   __TEXT.__swift5_types2: 0xc
-  __TEXT.__unwind_info: 0x31b8
+  __TEXT.__unwind_info: 0x31c8
   __TEXT.__eh_frame: 0x1548
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_protolist: 0x100
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0x21f8
+  __DATA_CONST.__objc_selrefs: 0x2218
   __DATA_CONST.__objc_protorefs: 0x78
   __DATA_CONST.__objc_superrefs: 0x1e0
   __DATA_CONST.__objc_arraydata: 0x18
   __DATA_CONST.__got: 0x6f0
   __AUTH_CONST.__const: 0x2a60
-  __AUTH_CONST.__cfstring: 0x4140
-  __AUTH_CONST.__objc_const: 0x8988
+  __AUTH_CONST.__cfstring: 0x4160
+  __AUTH_CONST.__objc_const: 0x89e8
   __AUTH_CONST.__weak_auth_got: 0x18
   __AUTH_CONST.__objc_intobj: 0x78
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH_CONST.__auth_got: 0x1128
+  __AUTH_CONST.__auth_got: 0x1130
   __AUTH.__objc_data: 0xb20
   __AUTH.__data: 0x2d0
-  __DATA.__objc_ivar: 0x56c
+  __DATA.__objc_ivar: 0x574
   __DATA.__data: 0xbf0
   __DATA_DIRTY.__objc_data: 0x16d8
   __DATA_DIRTY.__data: 0xb38

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 3144
-  Symbols:   4016
-  CStrings:  916
+  Functions: 3151
+  Symbols:   4024
+  CStrings:  917
 
Symbols:
+ -[HDDatabaseConnectionPool createdConnectionCount]
+ -[HDDatabaseConnectionPool trimCachedConnectionsToCount:]
+ -[HDSQLiteConnectionHandle interruptRequested]
+ -[HDSQLiteConnectionHandle setInterruptRequested:]
+ _HDSQLiteInterruptProgressHandler
+ _OBJC_IVAR_$_HDDatabaseConnectionPool._createdConnectionCount
+ _OBJC_IVAR_$_HDSQLiteConnectionHandle._interruptRequested
+ _sqlite3_progress_handler
CStrings:
+ "count >= 0"
+ "\xd1"
- "\xc1"
```
