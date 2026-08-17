## DataRelay_Private

> `/System/Library/PrivateFrameworks/DataRelay_Private.framework/Versions/A/DataRelay_Private`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_classname`

```diff

 35.14.0.0.0
-  __TEXT.__text: 0x107a0
+  __TEXT.__text: 0x111a0
   __TEXT.__auth_stubs: 0x2b0
-  __TEXT.__objc_methlist: 0xbb0
+  __TEXT.__objc_methlist: 0xbe8
   __TEXT.__const: 0x58
-  __TEXT.__gcc_except_tab: 0x65c
-  __TEXT.__cstring: 0x23f9
-  __TEXT.__unwind_info: 0x678
+  __TEXT.__gcc_except_tab: 0x6dc
+  __TEXT.__cstring: 0x24aa
+  __TEXT.__unwind_info: 0x6c0
   __TEXT.__objc_classname: 0xdc
-  __TEXT.__objc_methname: 0x1e05
-  __TEXT.__objc_methtype: 0x2e3
-  __TEXT.__objc_stubs: 0x18e0
-  __DATA_CONST.__got: 0x120
+  __TEXT.__objc_methname: 0x1e9a
+  __TEXT.__objc_methtype: 0x301
+  __TEXT.__objc_stubs: 0x1980
+  __DATA_CONST.__got: 0x130
   __DATA_CONST.__const: 0xb8
   __DATA_CONST.__objc_classlist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x7e0
+  __DATA_CONST.__objc_selrefs: 0x808
   __DATA_CONST.__objc_superrefs: 0x68
   __DATA_CONST.__objc_arraydata: 0x130
   __AUTH_CONST.__auth_got: 0x168
-  __AUTH_CONST.__const: 0x8c0
-  __AUTH_CONST.__cfstring: 0x920
-  __AUTH_CONST.__objc_const: 0x12f8
-  __AUTH_CONST.__objc_intobj: 0x138
+  __AUTH_CONST.__const: 0x920
+  __AUTH_CONST.__cfstring: 0x940
+  __AUTH_CONST.__objc_const: 0x1358
+  __AUTH_CONST.__objc_intobj: 0x150
   __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH.__objc_data: 0x370
-  __DATA.__objc_ivar: 0xe4
+  __DATA.__objc_ivar: 0xec
   __DATA.__data: 0x548
   __DATA_DIRTY.__objc_data: 0xf0
   __DATA_DIRTY.__data: 0xe0

   - /System/Library/PrivateFrameworks/Rapport.framework/Versions/A/Rapport
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 475
-  Symbols:   903
-  CStrings:  670
+  Functions: 488
+  Symbols:   924
+  CStrings:  686
 
Symbols:
+ -[DRClient resetSPDServer]
+ -[DRClient setSpdServer:]
+ -[DRClient spdServer]
+ -[DRServer setSpdClient:]
+ -[DRServer spdClient]
+ GCC_except_table19
+ GCC_except_table23
+ GCC_except_table34
+ GCC_except_table38
+ OBJC_IVAR_$_DRClient._spdServer
+ OBJC_IVAR_$_DRServer._spdClient
+ _OUTLINED_FUNCTION_10
+ __45-[DRServer addRequestedDataTypes:completion:]_block_invoke_2
+ __45-[DRServer addRequestedDataTypes:completion:]_block_invoke_4
+ ___26-[DRClient resetSPDServer]_block_invoke
+ ___45-[DRServer addRequestedDataTypes:completion:]_block_invoke_4
+ ___block_descriptor_40_e8_32w_e29_v16?0"NSMutableDictionary"8l
+ ___block_descriptor_56_e8_32s40bs_e51_v32?0"NSDictionary"8"NSDictionary"16"NSError"24l
+ ___block_descriptor_64_e8_32s40bs48w_e51_v32?0"NSDictionary"8"NSDictionary"16"NSError"24l
+ _objc_msgSend$handleEvent:
+ _objc_msgSend$handleRequest:
+ _objc_msgSend$resetSPDServer
+ _objc_msgSend$setRequestHandler:
+ _objc_msgSend$spdClient
- GCC_except_table21
- GCC_except_table32
- ___block_descriptor_56_e8_32s40bs48w_e51_v32?0"NSDictionary"8"NSDictionary"16"NSError"24l
CStrings:
+ "-[DRClient resetSPDServer]"
+ "-[DRServer addRequestedDataTypes:completion:]_block_invoke_2"
+ "@\"DRSPDClient\""
+ "@\"DRSPDServer\""
+ "BBInference"
+ "T@\"DRSPDClient\",&,N,V_spdClient"
+ "T@\"DRSPDServer\",&,N,V_spdServer"
+ "_spdClient"
+ "_spdServer"
+ "resetSPDServer"
+ "sending request for dataType %@"
+ "setSpdClient:"
+ "setSpdServer:"
+ "spdClient"
+ "spdServer"
+ "v16@?0@\"NSMutableDictionary\"8"
```
