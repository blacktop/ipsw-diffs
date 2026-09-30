## perfdiagsselfenabled

> `/usr/libexec/perfdiagsselfenabled`

```diff

-380.0.0.0.0
-  __TEXT.__text: 0xc53c
-  __TEXT.__auth_stubs: 0x590
+382.0.0.0.0
+  __TEXT.__text: 0xc6b4
+  __TEXT.__auth_stubs: 0x5b0
   __TEXT.__objc_stubs: 0xe80
-  __TEXT.__objc_methlist: 0xa78
+  __TEXT.__objc_methlist: 0xa84
   __TEXT.__const: 0x108
-  __TEXT.__cstring: 0x13bf
-  __TEXT.__oslogstring: 0x1fd0
+  __TEXT.__cstring: 0x13d8
+  __TEXT.__oslogstring: 0x1ff4
   __TEXT.__objc_classname: 0xda
   __TEXT.__objc_methtype: 0x553
-  __TEXT.__objc_methname: 0x31b2
+  __TEXT.__objc_methname: 0x3205
   __TEXT.__gcc_except_tab: 0x18
-  __TEXT.__unwind_info: 0x270
-  __DATA_CONST.__auth_got: 0x2d8
+  __TEXT.__unwind_info: 0x278
+  __DATA_CONST.__auth_got: 0x2e8
   __DATA_CONST.__got: 0xb8
-  __DATA_CONST.__const: 0x658
-  __DATA_CONST.__cfstring: 0x1560
+  __DATA_CONST.__const: 0x660
+  __DATA_CONST.__cfstring: 0x1580
   __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x10
   __DATA_CONST.__objc_intobj: 0x18
-  __DATA.__objc_const: 0x1ab0
-  __DATA.__objc_selrefs: 0x720
-  __DATA.__objc_ivar: 0x1b0
+  __DATA.__objc_const: 0x1ae0
+  __DATA.__objc_selrefs: 0x728
+  __DATA.__objc_ivar: 0x1b4
   __DATA.__objc_data: 0x370
   __DATA.__data: 0x30
   __DATA.__bss: 0x60

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
-  UUID: 4D2B8090-D1DD-36E8-AA67-AEC56B5592BD
-  Functions: 306
-  Symbols:   121
-  CStrings:  985
+  UUID: DD8D77E4-44FF-3FCF-BECF-23E3CFC9B2B8
+  Functions: 308
+  Symbols:   123
+  CStrings:  991
 
Symbols:
+ _tailspin_config_copy_description
+ _tailspin_config_create_with_current_state
CStrings:
+ "Current tailspin config: %{public}@"
+ "ShouldCollectCPURoleInfo"
+ "TB,R,V_shouldCollectCPURoleInfo"
+ "_shouldCollectCPURoleInfo"
+ "shouldCollectCPURoleInfo"

```
