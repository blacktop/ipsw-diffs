## libBasebandManager.dylib

> `/usr/lib/libBasebandManager.dylib`

```diff

-1380.0.0.0.0
-  __TEXT.__text: 0x224a14
-  __TEXT.__auth_stubs: 0x3200
-  __TEXT.__init_offsets: 0x150
+1384.1.0.0.0
+  __TEXT.__text: 0x224d14
+  __TEXT.__auth_stubs: 0x3210
+  __TEXT.__init_offsets: 0x154
   __TEXT.__objc_methlist: 0x46c
   __TEXT.__const: 0xf128
-  __TEXT.__gcc_except_tab: 0x34a34
-  __TEXT.__cstring: 0x7d0f
-  __TEXT.__oslogstring: 0xb991
-  __TEXT.__unwind_info: 0xa0e0
+  __TEXT.__gcc_except_tab: 0x34a94
+  __TEXT.__cstring: 0x7d13
+  __TEXT.__oslogstring: 0xb9c1
+  __TEXT.__unwind_info: 0xa0f8
   __TEXT.__objc_classname: 0x10d
   __TEXT.__objc_methname: 0x13e7
   __TEXT.__objc_methtype: 0x10f0
   __TEXT.__objc_stubs: 0x1100
-  __DATA_CONST.__got: 0x21d8
+  __DATA_CONST.__got: 0x21e0
   __DATA_CONST.__const: 0x2040
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x5b8
   __DATA_CONST.__objc_superrefs: 0x20
-  __AUTH_CONST.__auth_got: 0x1910
-  __AUTH_CONST.__const: 0xe780
+  __AUTH_CONST.__auth_got: 0x1918
+  __AUTH_CONST.__const: 0xe7b0
   __AUTH_CONST.__cfstring: 0x860
   __AUTH_CONST.__objc_const: 0x918
   __AUTH_CONST.__objc_intobj: 0x18

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libprotobuf-lite.dylib
   - /usr/lib/libprotobuf.dylib
-  UUID: 682FF84D-0FE1-3829-88CB-9BC4158480F3
-  Functions: 6029
-  Symbols:   18448
+  UUID: F91B27D3-1F43-3D4E-89DC-9CB1DDA04409
+  Functions: 6032
+  Symbols:   18457
   CStrings:  2770
 
Symbols:
+ __ZN15AnalyticsHelper11submitEventENSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEERNS0_3mapIS6_N3xpc4dictENS0_4lessIS6_EENS4_INS0_4pairIKS6_S9_EEEEEEb
+ __ZN3abm26kKeyHasRepeatedIntegerTypeE
+ __ZN6metric22sendCoreAnalyticsEventENSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEEN3xpc4dictEb
+ __ZN9Timestamp12timediffUSecERKS_S1_
+ ____ZN6metric22sendCoreAnalyticsEventENSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEEN3xpc4dictEb_block_invoke
+ ____ZN6metric22sendCoreAnalyticsEventENSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEEN3xpc4dictEb_block_invoke.2
+ ___block_literal_global.57
+ ___cxx_global_var_init.50
+ _analytics_send_exploding_event_lazy
- __ZN15AnalyticsHelper11submitEventENSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEERNS0_3mapIS6_N3xpc4dictENS0_4lessIS6_EENS4_INS0_4pairIKS6_S9_EEEEEE
- __ZN6metric22sendCoreAnalyticsEventENSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEEN3xpc4dictE
- ____ZN6metric22sendCoreAnalyticsEventENSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEEN3xpc4dictE_block_invoke
- ___block_literal_global.56
CStrings:
+ "#D Submitting CoreAnalytics event[%s], hasRepeatedInt[%d] - %s"
+ "AppleBasebandManager-AppleBasebandServices_Manager-1384.1"
+ "AppleBasebandServices_Manager-1384.1"
+ "Sending CoreAnalytics event: %s (repeated integer type: %d)"
- "#D Submitting CoreAnalytics event[%s] - %s"
- "AppleBasebandManager-AppleBasebandServices_Manager-1380"
- "AppleBasebandServices_Manager-1380"
- "Sending CoreAnalytics event: %s"

```
