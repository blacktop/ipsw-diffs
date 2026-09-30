## PacketFilter

> `/System/Library/PrivateFrameworks/PacketFilter.framework/PacketFilter`

```diff

-114.100.1.0.0
-  __TEXT.__text: 0x8264
+114.120.2.0.0
+  __TEXT.__text: 0x8648
   __TEXT.__auth_stubs: 0x580
   __TEXT.__const: 0x50
-  __TEXT.__cstring: 0x233c
+  __TEXT.__cstring: 0x23d0
   __TEXT.__oslogstring: 0x1e
-  __TEXT.__unwind_info: 0x1d0
+  __TEXT.__unwind_info: 0x1e0
   __DATA_CONST.__got: 0x78
-  __DATA_CONST.__const: 0x718
+  __DATA_CONST.__const: 0x790
   __AUTH_CONST.__auth_got: 0x2c0
   __AUTH_CONST.__const: 0x168
   __AUTH_CONST.__cfstring: 0x20
-  __DATA.__data: 0x3c8
+  __DATA.__data: 0x3d8
   __DATA.__bss: 0x20
   __DATA_DIRTY.__data: 0x40
   __DATA_DIRTY.__bss: 0x40

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Security.framework/Security
   - /usr/lib/libSystem.B.dylib
-  UUID: A46B1699-A2B9-3C49-8B56-7D685C5CDB24
-  Functions: 131
-  Symbols:   513
-  CStrings:  361
+  UUID: 8CA7B514-4FCE-3A78-B4DD-2A805AB7F8A2
+  Functions: 135
+  Symbols:   525
+  CStrings:  367
 
Symbols:
+ _PFUserDeleteStates
+ ___PFUserDeleteStates_block_invoke
+ ___PFUserDeleteStates_block_invoke_2
+ _____PFUserXPCDeleteStatesResponseHandler_block_invoke
+ ___block_descriptor_tmp.101
+ ___block_descriptor_tmp.103
+ ___block_descriptor_tmp.110
+ ___block_descriptor_tmp.112
+ ___block_descriptor_tmp.114
+ ___block_descriptor_tmp.116
+ ___block_descriptor_tmp.118
+ ___block_descriptor_tmp.120
+ ___block_descriptor_tmp.127
+ ___block_descriptor_tmp.73
+ ___block_descriptor_tmp.77
+ ___block_descriptor_tmp.79
+ ___block_descriptor_tmp.80
+ ___block_descriptor_tmp.81
+ ___block_descriptor_tmp.95
+ _pfXPCKeyDeleteAF
+ _pfXPCKeyDeleteAddress
- ___block_descriptor_tmp.100
- ___block_descriptor_tmp.102
- ___block_descriptor_tmp.109
- ___block_descriptor_tmp.111
- ___block_descriptor_tmp.113
- ___block_descriptor_tmp.125
- ___block_descriptor_tmp.69
- ___block_descriptor_tmp.75
- ___block_descriptor_tmp.76
- ___block_descriptor_tmp.90
- ___block_descriptor_tmp.96
- ___block_descriptor_tmp.98
CStrings:
+ "delete_address"
+ "delete_af"
+ "invalid parameters"
+ "user %p xpc response -> delete states %s"
+ "user %p xpc send -> delete states"
+ "xpc_dictionary_create failed"

```
