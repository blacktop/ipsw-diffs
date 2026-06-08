## DSContinuityPairing

> `/System/Library/PrivateFrameworks/DSContinuityPairing.framework/DSContinuityPairing`

```diff

-616.2.0.0.0
-  __TEXT.__text: 0x740c
-  __TEXT.__auth_stubs: 0xa00
+654.0.0.0.0
+  __TEXT.__text: 0x6d58
   __TEXT.__objc_methlist: 0x1a8
   __TEXT.__const: 0x28a
+  __TEXT.__cstring: 0x3c
   __TEXT.__swift5_typeref: 0x141
   __TEXT.__oslogstring: 0x147
   __TEXT.__constg_swiftt: 0x54
   __TEXT.__swift5_reflstr: 0x17
   __TEXT.__swift5_fieldmd: 0x38
   __TEXT.__swift5_capture: 0x9c
-  __TEXT.__cstring: 0x1c
   __TEXT.__swift5_proto: 0xc
   __TEXT.__swift5_types: 0x8
   __TEXT.__swift_as_entry: 0x1c
   __TEXT.__swift_as_ret: 0x20
-  __TEXT.__unwind_info: 0x248
+  __TEXT.__swift_as_cont: 0x30
+  __TEXT.__unwind_info: 0x200
   __TEXT.__eh_frame: 0x490
-  __TEXT.__objc_classname: 0x6d
-  __TEXT.__objc_methname: 0x4eb
-  __TEXT.__objc_methtype: 0x106
-  __TEXT.__objc_stubs: 0x260
-  __DATA_CONST.__got: 0x108
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x48
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x118
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0x508
+  __DATA_CONST.__got: 0x108
   __AUTH_CONST.__const: 0x1f8
   __AUTH_CONST.__objc_const: 0x3c0
+  __AUTH_CONST.__auth_got: 0x568
   __AUTH.__objc_data: 0x158
   __AUTH.__data: 0x28
   __DATA.__objc_ivar: 0x2c

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 61387D31-FE9B-3078-A7AB-E5E47AD75436
-  Functions: 126
-  Symbols:   250
-  CStrings:  84
+  UUID: A3404FEE-523B-3C33-B85D-F0B8F9D51589
+  Functions: 127
+  Symbols:   278
+  CStrings:  10
 
Symbols:
+ ___swift_async_cont_functlets
+ ___swift_closure_destructor
+ ___swift_closure_destructor.14
+ ___swift_closure_destructor.14Tm
+ ___swift_closure_destructor.18
+ ___swift_closure_destructor.22
+ ___swift_closure_destructor.26
+ ___swift_closure_destructor.35
+ ___swift_closure_destructor.39
+ ___swift_closure_destructor.44
+ _objc_claimAutoreleasedReturnValue
+ _objc_release_x27
+ _objc_retain_x2
+ _objc_retain_x3
+ _swift_release_x10
+ _swift_release_x19
+ _swift_release_x20
+ _swift_release_x21
+ _swift_release_x22
+ _swift_release_x25
+ _swift_release_x8
+ _swift_retain_x19
+ _swift_retain_x21
- _objc_retain_x28
- _objectdestroy.14Tm
- _swift_retain
CStrings:
- ".cxx_destruct"
- "@\"NSDate\""
- "@\"NSString\""
- "@\"NSUUID\""
- "@\"_TtC19DSContinuityPairing17ContinuityPairing\""
- "@16@0:8"
- "@48@0:8@16@24@32@40"
- "B24@0:8@16"
- "DSContinuityDevice"
- "DSContinuityPairingWrapper"
- "T@\"NSDate\",&,N,V_initialDiscoveryDate"
- "T@\"NSString\",&,N,V_formattedSessionDuration"
- "T@\"NSString\",&,N,V_formattedSessionStart"
- "T@\"NSString\",&,N,V_marketingName"
- "T@\"NSString\",&,N,V_model"
- "T@\"NSString\",&,N,V_name"
- "T@\"NSString\",&,N,V_pushToken"
- "T@\"NSString\",&,N,V_serialNumber"
- "T@\"NSUUID\",&,N,V_deviceID"
- "T@\"NSUUID\",&,N,V_relationshipID"
- "T@\"_TtC19DSContinuityPairing17ContinuityPairing\",&,N,V_continuityPairing"
- "_TtC19DSContinuityPairing17ContinuityPairing"
- "_continuityPairing"
- "_deviceID"
- "_formattedSessionDuration"
- "_formattedSessionStart"
- "_initialDiscoveryDate"
- "_marketingName"
- "_model"
- "_name"
- "_pushToken"
- "_relationshipID"
- "_serialNumber"
- "allowedUnits"
- "continuityPairing"
- "dealloc"
- "deviceID"
- "fetchContinuityDevicesWithCompletionHandler:"
- "fetchContinuityEligibleDevicesWithCompletion:"
- "formattedSessionDuration"
- "formattedSessionStart"
- "init"
- "initWithName:deviceID:relationshipID:initialDiscoveryDate:"
- "initialDiscoveryDate"
- "isEqual:"
- "manager"
- "marketingName"
- "model"
- "name"
- "pushToken"
- "relationshipID"
- "serialNumber"
- "setAllowedUnits:"
- "setContinuityPairing:"
- "setDeviceID:"
- "setFormattedSessionDuration:"
- "setFormattedSessionStart:"
- "setInitialDiscoveryDate:"
- "setMarketingName:"
- "setModel:"
- "setName:"
- "setPushToken:"
- "setRelationshipID:"
- "setSerialNumber:"
- "setUnitsStyle:"
- "stringFromDate:toDate:"
- "unpairDeviceWith:completionHandler:"
- "unpairHostWithDeviceID:completion:"
- "v16@0:8"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8@?<v@?@\"NSArray\"@\"NSError\">16"
- "v32@0:8@\"NSUUID\"16@?<v@?@\"NSError\">24"
- "v32@0:8@16@?24"

```
