## IOGPU

> `/System/Library/PrivateFrameworks/IOGPU.framework/IOGPU`

```diff

-128.1.0.0.0
-  __TEXT.__text: 0x28bdc
+128.3.0.0.0
+  __TEXT.__text: 0x28c00
   __TEXT.__auth_stubs: 0xd70
-  __TEXT.__objc_methlist: 0x4cd4
+  __TEXT.__objc_methlist: 0x4cdc
   __TEXT.__cstring: 0x5f8c
   __TEXT.__const: 0x208
   __TEXT.__gcc_except_tab: 0x428
   __TEXT.__oslogstring: 0x8ae
   __TEXT.__unwind_info: 0xcc8
   __TEXT.__objc_classname: 0x635
-  __TEXT.__objc_methname: 0xb4dc
+  __TEXT.__objc_methname: 0xb4f1
   __TEXT.__objc_methtype: 0x6aec
   __TEXT.__objc_stubs: 0x2fe0
   __DATA_CONST.__got: 0x418

   __AUTH_CONST.__auth_got: 0x6d0
   __AUTH_CONST.__const: 0x3f0
   __AUTH_CONST.__cfstring: 0x1300
-  __AUTH_CONST.__objc_const: 0x7ce8
+  __AUTH_CONST.__objc_const: 0x7d08
   __AUTH.__objc_data: 0x6e0
-  __DATA.__objc_ivar: 0x390
+  __DATA.__objc_ivar: 0x394
   __DATA.__data: 0x7e0
   __DATA.__bss: 0x18
   __DATA_DIRTY.__objc_data: 0x780

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: FFB1B817-D108-3408-A034-358127BFEF95
-  Functions: 1421
-  Symbols:   4249
-  CStrings:  2937
+  UUID: 6D5F0F76-1433-3814-A652-48F4AD20AEAC
+  Functions: 1422
+  Symbols:   4252
+  CStrings:  2938
 
Symbols:
+ -[IOGPUMetalTensor allocatedSize]
+ _OBJC_IVAR_$_IOGPUMetalTensor._allocatedSize
Functions:
~ -[IOGPUMetalTensor initWithBuffer:] : 96 -> 116
+ -[IOGPUMetalTensor allocatedSize]
CStrings:
+ "TQ,R,V_allocatedSize"

```
