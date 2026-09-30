## TelephonyPreferences

> `/System/Library/PrivateFrameworks/TelephonyPreferences.framework/TelephonyPreferences`

```diff

-383.200.41.0.0
-  __TEXT.__text: 0x32fd4
+383.300.1.0.0
+  __TEXT.__text: 0x33448
   __TEXT.__auth_stubs: 0xf70
   __TEXT.__objc_methlist: 0x3f48
   __TEXT.__const: 0x696
   __TEXT.__cstring: 0x2183
-  __TEXT.__oslogstring: 0x243e
+  __TEXT.__oslogstring: 0x2511
   __TEXT.__gcc_except_tab: 0x324
   __TEXT.__dlopen_cstrs: 0x114
   __TEXT.__ustring: 0x9e

   __TEXT.__swift5_protos: 0x8
   __TEXT.__swift5_proto: 0x20
   __TEXT.__swift5_assocty: 0x80
-  __TEXT.__unwind_info: 0xfd0
+  __TEXT.__unwind_info: 0xfe0
   __TEXT.__eh_frame: 0x2c8
   __TEXT.__objc_classname: 0xc74
   __TEXT.__objc_methname: 0x9f13

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 9C3102A9-D997-3239-A566-7A7D32CEF2B6
-  Functions: 1455
-  Symbols:   4773
-  CStrings:  2494
+  UUID: C76BBC1D-3FEF-3735-B95E-7A25DB3A3F9B
+  Functions: 1459
+  Symbols:   4781
+  CStrings:  2497
 
Symbols:
+ -[TPSCallForwardingRequestController suppServicesEvent:event:settingsType:data:].cold.4
+ -[TPSCallWaitingRequestController suppServicesEvent:event:settingsType:data:].cold.4
+ -[TPSCallingLineIdRestrictionRequestController suppServicesEvent:event:settingsType:data:].cold.4
CStrings:
+ "Request type %@ is not the expected: \"TPSSetCallForwardingRequest\""
+ "Request type %@ is not the expected: \"TPSSetCallWaitingRequest\""
+ "Request type %@ is not the expected: \"TPSSetCallingLineIdRestrictionSetRequest\""

```
