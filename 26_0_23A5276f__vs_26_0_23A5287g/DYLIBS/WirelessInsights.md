## WirelessInsights

> `/System/Library/Frameworks/WirelessInsights.framework/WirelessInsights`

```diff

-207.0.0.0.0
-  __TEXT.__text: 0x6b970
-  __TEXT.__auth_stubs: 0x1ac0
+211.0.0.0.0
+  __TEXT.__text: 0x6c614
+  __TEXT.__auth_stubs: 0x1ad0
   __TEXT.__objc_methlist: 0x3ec
-  __TEXT.__gcc_except_tab: 0x3c0c
-  __TEXT.__cstring: 0x1907
-  __TEXT.__const: 0x9173
-  __TEXT.__oslogstring: 0x208f
+  __TEXT.__gcc_except_tab: 0x3cfc
+  __TEXT.__cstring: 0x1927
+  __TEXT.__const: 0x91bb
+  __TEXT.__oslogstring: 0x217f
   __TEXT.__swift5_typeref: 0x18a9
-  __TEXT.__swift5_capture: 0x2a8
+  __TEXT.__swift5_capture: 0x2f8
   __TEXT.__swift5_reflstr: 0x849
   __TEXT.__swift5_assocty: 0x180
   __TEXT.__constg_swiftt: 0x1700

   __TEXT.__swift5_types: 0x230
   __TEXT.__swift_as_entry: 0x84
   __TEXT.__swift_as_ret: 0x64
-  __TEXT.__unwind_info: 0x3650
-  __TEXT.__eh_frame: 0x1f20
+  __TEXT.__unwind_info: 0x3688
+  __TEXT.__eh_frame: 0x1f48
   __TEXT.__objc_classname: 0x67
   __TEXT.__objc_methname: 0x831
   __TEXT.__objc_methtype: 0x254
   __TEXT.__objc_stubs: 0x460
   __DATA_CONST.__got: 0x348
-  __DATA_CONST.__const: 0x700
+  __DATA_CONST.__const: 0x720
   __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x2e0
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x18
-  __AUTH_CONST.__auth_got: 0xd70
-  __AUTH_CONST.__const: 0x5318
+  __AUTH_CONST.__auth_got: 0xd78
+  __AUTH_CONST.__const: 0x53d0
   __AUTH_CONST.__cfstring: 0x260
   __AUTH_CONST.__objc_const: 0x9a8
   __AUTH.__objc_data: 0x48

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 0A54D380-C761-371B-84C2-248D86A496F0
-  Functions: 3546
-  Symbols:   1598
-  CStrings:  549
+  UUID: 24EDF28C-0930-3814-AF20-09E2EAD53FB4
+  Functions: 3563
+  Symbols:   1609
+  CStrings:  553
 
Symbols:
+ __ZN3wis15WISServerFacade26registerForAnomalyInsightsEj
+ __ZN3wis15WISServerFacade31registerForAnomalyInsights_syncEj
+ __ZN3wis33WISRegisterAnomalyInsightsMessageC1ERKN3xpc4dictE
+ __ZN3wis33WISRegisterAnomalyInsightsMessageC1Ej
+ __ZN3wis33WISRegisterAnomalyInsightsMessageC2ERKN3xpc4dictE
+ __ZN3wis33WISRegisterAnomalyInsightsMessageC2Ej
+ __ZNK3wis33WISRegisterAnomalyInsightsMessage14getComponentIdEv
+ __ZNK3wis33WISRegisterAnomalyInsightsMessage16createXpcMessageEv
+ __ZTIN3wis33WISRegisterAnomalyInsightsMessageE
+ __ZTSN3wis33WISRegisterAnomalyInsightsMessageE
+ __ZTVN3wis33WISRegisterAnomalyInsightsMessageE
CStrings:
+ "WISMessageComponentIdKey"
+ "client:#E Failed to create the xpc Message for component 0x%x"
+ "client:#E xpc connection NULL while registering for Anomaly insights for component 0x%x"
+ "client:#I Sending message to register for Anomaly Insights for component 0x%x "
+ "core:#N Registering callback for Anomaly Insights"
- "core:#N Registering callback for Anomaly"

```
