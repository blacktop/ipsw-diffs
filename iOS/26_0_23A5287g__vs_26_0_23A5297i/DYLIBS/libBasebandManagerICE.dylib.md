## libBasebandManagerICE.dylib

> `/usr/lib/libBasebandManagerICE.dylib`

```diff

-1380.0.0.0.0
-  __TEXT.__text: 0x21f560
-  __TEXT.__auth_stubs: 0x3240
-  __TEXT.__init_offsets: 0x15c
+1384.1.0.0.0
+  __TEXT.__text: 0x21f860
+  __TEXT.__auth_stubs: 0x3250
+  __TEXT.__init_offsets: 0x160
   __TEXT.__objc_methlist: 0x46c
   __TEXT.__const: 0xf4aa
-  __TEXT.__gcc_except_tab: 0x347fc
-  __TEXT.__oslogstring: 0xb903
-  __TEXT.__cstring: 0x7ad0
-  __TEXT.__unwind_info: 0xa128
+  __TEXT.__gcc_except_tab: 0x3485c
+  __TEXT.__oslogstring: 0xb933
+  __TEXT.__cstring: 0x7ad8
+  __TEXT.__unwind_info: 0xa140
   __TEXT.__objc_classname: 0x10d
   __TEXT.__objc_methname: 0x13e7
   __TEXT.__objc_methtype: 0x10f0
   __TEXT.__objc_stubs: 0x1100
-  __DATA_CONST.__got: 0x2218
+  __DATA_CONST.__got: 0x2220
   __DATA_CONST.__const: 0x1d18
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x5b8
   __DATA_CONST.__objc_superrefs: 0x20
-  __AUTH_CONST.__auth_got: 0x1930
-  __AUTH_CONST.__const: 0xea38
+  __AUTH_CONST.__auth_got: 0x1938
+  __AUTH_CONST.__const: 0xea68
   __AUTH_CONST.__cfstring: 0x940
   __AUTH_CONST.__objc_const: 0x918
   __AUTH_CONST.__objc_intobj: 0x18

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libprotobuf-lite.dylib
   - /usr/lib/libprotobuf.dylib
-  UUID: 78FF766D-0FCE-3AFF-960F-A740CC1FEC38
-  Functions: 6026
-  Symbols:   18433
+  UUID: 37C69A71-12F9-30F9-A040-AAB8A950F5AA
+  Functions: 6029
+  Symbols:   18442
   CStrings:  2725
 
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
