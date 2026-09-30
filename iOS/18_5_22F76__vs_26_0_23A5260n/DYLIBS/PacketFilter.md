## PacketFilter

> `/System/Library/PrivateFrameworks/PacketFilter.framework/PacketFilter`

```diff

-111.0.0.0.0
-  __TEXT.__text: 0x7214
-  __TEXT.__auth_stubs: 0x560
+112.0.0.0.0
+  __TEXT.__text: 0x8290
+  __TEXT.__auth_stubs: 0x580
   __TEXT.__const: 0x50
-  __TEXT.__cstring: 0x21f2
+  __TEXT.__cstring: 0x233c
   __TEXT.__oslogstring: 0x1e
-  __TEXT.__unwind_info: 0x1a0
+  __TEXT.__unwind_info: 0x1d0
   __DATA_CONST.__got: 0x78
-  __DATA_CONST.__const: 0x588
-  __AUTH_CONST.__auth_got: 0x2b0
-  __AUTH_CONST.__const: 0x108
+  __DATA_CONST.__const: 0x718
+  __AUTH_CONST.__auth_got: 0x2c0
+  __AUTH_CONST.__const: 0x168
   __AUTH_CONST.__cfstring: 0x20
-  __DATA.__data: 0x398
-  __DATA.__bss: 0x18
+  __DATA.__data: 0x3c8
+  __DATA.__bss: 0x20
   __DATA_DIRTY.__data: 0x40
   __DATA_DIRTY.__bss: 0x40
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Security.framework/Security
   - /usr/lib/libSystem.B.dylib
-  UUID: FB98FB4B-DC43-38FD-A70D-C8B67D4237D4
-  Functions: 113
-  Symbols:   464
-  CStrings:  347
+  UUID: 4C4D111F-27E9-3798-9DBA-D0F83BB77C8B
+  Functions: 131
+  Symbols:   513
+  CStrings:  361
 
Symbols:
+ _PFTableAddAddress
+ _PFTableBegin
+ _PFTableClear
+ _PFTableCommit
+ _PFTableCreate
+ _PFTableDelete
+ ___PFTableAddAddress_block_invoke
+ ___PFTableBegin_block_invoke
+ ___PFTableClass
+ ___PFTableClear_block_invoke
+ ___PFTableCommit_block_invoke
+ ___PFTableCommit_block_invoke_2
+ ___PFTableCreate_block_invoke
+ ___PFTableDelete_block_invoke
+ ___PFTableDelete_block_invoke_2
+ ___PFTableRegister
+ ___PFTableRelease
+ _____PFUserXPCCommitTableResponseHandler_block_invoke
+ _____PFUserXPCDeleteTableResponseHandler_block_invoke
+ ___block_descriptor_tmp.100
+ ___block_descriptor_tmp.102
+ ___block_descriptor_tmp.105
+ ___block_descriptor_tmp.107
+ ___block_descriptor_tmp.109
+ ___block_descriptor_tmp.111
+ ___block_descriptor_tmp.113
+ ___block_descriptor_tmp.125
+ ___block_descriptor_tmp.42
+ ___block_descriptor_tmp.49
+ ___block_descriptor_tmp.50
+ ___block_descriptor_tmp.51
+ ___block_descriptor_tmp.55
+ ___block_descriptor_tmp.58
+ ___block_descriptor_tmp.62
+ ___block_descriptor_tmp.63
+ ___block_descriptor_tmp.67
+ ___block_descriptor_tmp.68
+ ___block_descriptor_tmp.69
+ ___block_descriptor_tmp.72
+ ___block_descriptor_tmp.74
+ ___block_descriptor_tmp.76
+ ___block_descriptor_tmp.90
+ ___block_descriptor_tmp.96
+ ___block_descriptor_tmp.98
+ ___pfTableTypeID
+ ___pfTableTypeInit
+ _kPFNetworkIsolation
+ _kPFSubTable
+ _pfXPCKeyTableAddressArray
+ _pfXPCKeyTableName
+ _xpc_dictionary_get_array
+ _xpc_string_create
- ___block_descriptor_tmp.121
- ___block_descriptor_tmp.43
- ___block_descriptor_tmp.44
- ___block_descriptor_tmp.48
- ___block_descriptor_tmp.52
- ___block_descriptor_tmp.53
- ___block_descriptor_tmp.57
- ___block_descriptor_tmp.61
- ___block_descriptor_tmp.81
- ___block_descriptor_tmp.83
- ___block_descriptor_tmp.85
- ___block_descriptor_tmp.87
- ___block_descriptor_tmp.89
- ___block_descriptor_tmp.91
- ___block_descriptor_tmp.93
CStrings:
+ "PFTable"
+ "addr missing"
+ "address-table"
+ "network_isolation"
+ "rule is not a xpc string"
+ "table %p xpc response -> commit %s"
+ "table %p xpc response -> delete %s"
+ "table %p xpc send -> commit table %p"
+ "table %s xpc send -> delete table"
+ "table is NULL"
+ "table_address_array"
+ "table_name"
+ "unable to create table name xpc str"
+ "unable to get framework queue"

```
