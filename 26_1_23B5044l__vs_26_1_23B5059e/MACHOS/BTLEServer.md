## BTLEServer

> `/usr/sbin/BTLEServer`

```diff

-351.1.0.0.0
-  __TEXT.__text: 0x7b284
+351.2.0.0.0
+  __TEXT.__text: 0x7b3c8
   __TEXT.__auth_stubs: 0x10b0
   __TEXT.__objc_stubs: 0xc880
   __TEXT.__objc_methlist: 0x74dc
   __TEXT.__const: 0x598
-  __TEXT.__cstring: 0x344b
+  __TEXT.__cstring: 0x3462
   __TEXT.__objc_methname: 0x126f4
-  __TEXT.__oslogstring: 0xc3fa
+  __TEXT.__oslogstring: 0xc467
   __TEXT.__objc_classname: 0x8bc
   __TEXT.__objc_methtype: 0x306d
   __TEXT.__gcc_except_tab: 0xf10

   __DATA_CONST.__got: 0x940
   __DATA_CONST.__auth_ptr: 0x18
   __DATA_CONST.__const: 0x1660
-  __DATA_CONST.__cfstring: 0x4ae0
+  __DATA_CONST.__cfstring: 0x4b00
   __DATA_CONST.__objc_classlist: 0x298
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0xc8

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: C4C36DA0-9C07-3A27-B459-C394138CB115
+  UUID: BC406224-EE7F-3754-BEDE-A1D237D33EBD
   Functions: 2891
   Symbols:   566
-  CStrings:  5641
+  CStrings:  5645
 
Functions:
~ sub_100036760 : 1756 -> 1932
~ sub_1000374ec -> sub_10003759c : 944 -> 1092
CStrings:
+ "Creating accessory connection without auth for %@ as it previously passed auth"
+ "Untagging %@ due to auth fail"
+ "pencilMFiAuth4.0Passed"

```
