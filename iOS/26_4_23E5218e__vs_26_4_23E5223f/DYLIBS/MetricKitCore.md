## MetricKitCore

> `/System/Library/PrivateFrameworks/MetricKitCore.framework/MetricKitCore`

```diff

-297.100.10.0.0
-  __TEXT.__text: 0x181a4
-  __TEXT.__auth_stubs: 0x7b0
+297.100.11.0.0
+  __TEXT.__text: 0x18234
+  __TEXT.__auth_stubs: 0x7d0
   __TEXT.__objc_methlist: 0x19bc
   __TEXT.__const: 0x26a
   __TEXT.__oslogstring: 0x1c96
-  __TEXT.__cstring: 0x8f1
+  __TEXT.__cstring: 0x941
   __TEXT.__gcc_except_tab: 0x14
   __TEXT.__swift5_typeref: 0x4f
   __TEXT.__swift5_reflstr: 0x9

   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_proto: 0xc
   __TEXT.__swift5_types: 0x8
-  __TEXT.__unwind_info: 0x5e8
+  __TEXT.__unwind_info: 0x5d8
   __TEXT.__objc_classname: 0x2e5
   __TEXT.__objc_methname: 0x4923
   __TEXT.__objc_methtype: 0x9e8

   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x80
   __DATA_CONST.__objc_arraydata: 0x598
-  __AUTH_CONST.__auth_got: 0x3e8
+  __AUTH_CONST.__auth_got: 0x3f8
   __AUTH_CONST.__const: 0x40
   __AUTH_CONST.__cfstring: 0x860
   __AUTH_CONST.__objc_const: 0x2b48

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  UUID: 9356E8C4-1D1A-392B-8566-2A78414352A1
+  UUID: 9C5D637F-C79E-30F9-81D8-39619E7381E3
   Functions: 679
-  Symbols:   2413
-  CStrings:  1103
+  Symbols:   2415
+  CStrings:  1105
 
Symbols:
+ _dispatch_queue_attr_make_with_autorelease_frequency
+ _os_transaction_create
Functions:
~ -[MXSource _initQueue] : 176 -> 232
~ -[MXSource writeMetricDataWithPayload:] : 232 -> 264
~ ___39-[MXSource writeMetricDataWithPayload:]_block_invoke : 88 -> 100
~ -[MXSource writeDiagnosticDataWithPayload:] : 232 -> 264
~ ___43-[MXSource writeDiagnosticDataWithPayload:]_block_invoke : 88 -> 100
CStrings:
+ "com.apple.metrickitd.diagnostic-processing"
+ "com.apple.metrickitd.metric-processing"

```
