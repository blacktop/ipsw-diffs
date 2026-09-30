## CoreRepairLite

> `/System/Library/PrivateFrameworks/CoreRepairLite.framework/CoreRepairLite`

```diff

-921.0.34.0.0
-  __TEXT.__text: 0xb75c
+921.0.65.0.0
+  __TEXT.__text: 0xb8c8
   __TEXT.__auth_stubs: 0x750
-  __TEXT.__objc_methlist: 0x320
+  __TEXT.__objc_methlist: 0x328
   __TEXT.__const: 0xc3
-  __TEXT.__oslogstring: 0x17d6
+  __TEXT.__oslogstring: 0x17c0
   __TEXT.__gcc_except_tab: 0xf8
-  __TEXT.__cstring: 0x535
+  __TEXT.__cstring: 0x562
   __TEXT.__unwind_info: 0x1c8
   __TEXT.__objc_classname: 0x49
-  __TEXT.__objc_methname: 0xb17
+  __TEXT.__objc_methname: 0xb36
   __TEXT.__objc_methtype: 0x1d7
   __TEXT.__objc_stubs: 0xc80
   __DATA_CONST.__got: 0x100
   __DATA_CONST.__const: 0x70
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3b8
+  __DATA_CONST.__objc_selrefs: 0x3c0
   __DATA_CONST.__objc_superrefs: 0x8
-  __DATA_CONST.__objc_arraydata: 0xa0
+  __DATA_CONST.__objc_arraydata: 0x78
   __AUTH_CONST.__auth_got: 0x3b8
   __AUTH_CONST.__const: 0x40
-  __AUTH_CONST.__cfstring: 0x800
+  __AUTH_CONST.__cfstring: 0x920
   __AUTH_CONST.__objc_const: 0x2b0
-  __AUTH_CONST.__objc_arrayobj: 0x60
+  __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH.__objc_data: 0x140
   __DATA.__objc_ivar: 0xc
   __DATA.__bss: 0x50

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libamsupport.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 62B6DC43-E883-399A-9B6D-C07D4B8EFFC0
-  Functions: 206
-  Symbols:   757
-  CStrings:  481
+  UUID: E7879FD9-5AA2-3943-A760-DD45FDCDF7C1
+  Functions: 209
+  Symbols:   763
+  CStrings:  500
 
Symbols:
+ +[CRFDRUtils isPrimaryDataClassSupported:]
+ +[CRFDRUtils isRepairASIDSupported]
+ +[CRFDRUtils isRepairASIDSupported].cold.1
+ +[CRFDRUtils isRepairASIDSupported].cold.2
+ +[CRFDRUtils isRepairASIDSupported].cold.3
- +[CRFDRUtils hasMesaUnsealedData]
- +[CRFDRUtils hasMesaUnsealedData].cold.1
CStrings:
+ "CmCl"
+ "Failed to get 'supm' property"
+ "LCfg"
+ "NBCl"
+ "PlCl"
+ "bcrt"
+ "dCfg"
+ "isPrimaryDataClassSupported:"
+ "isRepairASIDSupported"
+ "prpc"
+ "supm"
+ "supm: %@"
+ "tcrt"
- "Failed to get delta components: %@"
- "No delta components found"
- "hasMesaUnsealedData"

```
