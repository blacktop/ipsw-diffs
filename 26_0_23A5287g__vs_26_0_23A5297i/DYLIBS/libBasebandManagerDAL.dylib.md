## libBasebandManagerDAL.dylib

> `/usr/lib/libBasebandManagerDAL.dylib`

```diff

-1380.0.0.0.0
-  __TEXT.__text: 0x188624
-  __TEXT.__auth_stubs: 0x28e0
-  __TEXT.__init_offsets: 0x100
+1384.1.0.0.0
+  __TEXT.__text: 0x188924
+  __TEXT.__auth_stubs: 0x28f0
+  __TEXT.__init_offsets: 0x104
   __TEXT.__objc_methlist: 0x314
   __TEXT.__const: 0xa4a3
-  __TEXT.__gcc_except_tab: 0x2394c
-  __TEXT.__oslogstring: 0x88b1
-  __TEXT.__cstring: 0x4b0f
-  __TEXT.__unwind_info: 0x7328
+  __TEXT.__gcc_except_tab: 0x239ac
+  __TEXT.__oslogstring: 0x88e1
+  __TEXT.__cstring: 0x4b13
+  __TEXT.__unwind_info: 0x7338
   __TEXT.__objc_classname: 0xd3
   __TEXT.__objc_methname: 0xc99
   __TEXT.__objc_methtype: 0xe03
   __TEXT.__objc_stubs: 0xc40
-  __DATA_CONST.__got: 0x1670
+  __DATA_CONST.__got: 0x1678
   __DATA_CONST.__const: 0x1550
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x3f0
   __DATA_CONST.__objc_superrefs: 0x18
-  __AUTH_CONST.__auth_got: 0x1480
-  __AUTH_CONST.__const: 0x9e38
+  __AUTH_CONST.__auth_got: 0x1488
+  __AUTH_CONST.__const: 0x9e68
   __AUTH_CONST.__cfstring: 0x480
   __AUTH_CONST.__objc_const: 0x6e8
   __AUTH.__objc_data: 0x190

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libprotobuf-lite.dylib
   - /usr/lib/libprotobuf.dylib
-  UUID: 9CC5DC65-0A49-3135-9598-93D74C900F0A
-  Functions: 4327
-  Symbols:   13110
+  UUID: ACD7BD80-F70D-3C98-B755-D360F82BDE1C
+  Functions: 4330
+  Symbols:   13119
   CStrings:  1915
 
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
