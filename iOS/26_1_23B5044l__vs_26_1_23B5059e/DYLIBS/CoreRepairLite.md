## CoreRepairLite

> `/System/Library/PrivateFrameworks/CoreRepairLite.framework/CoreRepairLite`

```diff

-921.40.47.0.0
-  __TEXT.__text: 0xb5fc
+921.40.58.0.0
+  __TEXT.__text: 0xb750
   __TEXT.__auth_stubs: 0x740
-  __TEXT.__objc_methlist: 0x320
+  __TEXT.__objc_methlist: 0x328
   __TEXT.__const: 0xc3
   __TEXT.__oslogstring: 0x17da
   __TEXT.__gcc_except_tab: 0xf8
-  __TEXT.__cstring: 0x526
-  __TEXT.__unwind_info: 0x1b8
+  __TEXT.__cstring: 0x52b
+  __TEXT.__unwind_info: 0x1c0
   __TEXT.__objc_classname: 0x49
-  __TEXT.__objc_methname: 0xb1f
+  __TEXT.__objc_methname: 0xb42
   __TEXT.__objc_methtype: 0x1d7
   __TEXT.__objc_stubs: 0xc60
   __DATA_CONST.__got: 0x100
   __DATA_CONST.__const: 0x70
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3b8
+  __DATA_CONST.__objc_selrefs: 0x3c0
   __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__objc_arraydata: 0x78
   __AUTH_CONST.__auth_got: 0x3b0
   __AUTH_CONST.__const: 0x40
-  __AUTH_CONST.__cfstring: 0x8a0
+  __AUTH_CONST.__cfstring: 0x8c0
   __AUTH_CONST.__objc_const: 0x2b0
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH.__objc_data: 0x140

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libamsupport.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 5451AFEF-F6A0-3493-9B64-AE408BDF0DF4
-  Functions: 210
-  Symbols:   763
-  CStrings:  491
+  UUID: EDF53C4E-803B-3F2D-8A1F-A21A7005F6BC
+  Functions: 212
+  Symbols:   767
+  CStrings:  494
 
Symbols:
+ +[CRFDRUtils getSealedInstancesWithClass:error:]
+ +[CRFDRUtils getSealedInstancesWithClass:error:].cold.1
Functions:
+ +[CRFDRUtils getSealedInstancesWithClass:error:]
~ +[CRFDRUtils isPrimaryDataClassSupported:] : 316 -> 332
~ _OUTLINED_FUNCTION_1 : 24 -> 16
~ _OUTLINED_FUNCTION_2 : 16 -> 20
+ +[CRFDRUtils getSealedInstancesWithClass:error:].cold.1
~ +[CRFDRUtils findUnsealedDataWithKey:error:].cold.1 : 124 -> 128
~ +[CRFDRUtils findUnsealedDataWithKey:error:].cold.2 : 124 -> 128
~ +[CRFDRUtils findUnsealedDataWithKey:error:].cold.3 : 124 -> 128
~ +[CRFDRUtils findUnsealedDataWithKey:error:].cold.4 : 124 -> 128
CStrings:
+ "getSealedInstancesWithClass:error:"
+ "vcrt"

```
