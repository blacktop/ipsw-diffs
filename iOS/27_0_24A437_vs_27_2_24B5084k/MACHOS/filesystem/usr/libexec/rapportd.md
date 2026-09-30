## rapportd

> `/usr/libexec/rapportd`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_capture`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_protos`
- `__TEXT.__swift5_acfuncs`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__auth_got`
- `__DATA_CONST.__auth_ptr`

```diff

-751.100.2.0.0
-  __TEXT.__text: 0x18cc74
+751.200.31.0.0
+  __TEXT.__text: 0x18efe8
   __TEXT.__auth_stubs: 0x39f0
-  __TEXT.__objc_stubs: 0x13620
-  __TEXT.__objc_methlist: 0xa0d0
-  __TEXT.__const: 0x6160
-  __TEXT.__cstring: 0x36db6
-  __TEXT.__objc_classname: 0x10bf
-  __TEXT.__objc_methtype: 0x4a81
-  __TEXT.__gcc_except_tab: 0x24b0
-  __TEXT.__objc_methname: 0x1c840
-  __TEXT.__oslogstring: 0x3542
-  __TEXT.__swift5_typeref: 0x1776
+  __TEXT.__objc_stubs: 0x13740
+  __TEXT.__objc_methlist: 0xa110
+  __TEXT.__const: 0x61e0
+  __TEXT.__cstring: 0x37286
+  __TEXT.__objc_classname: 0x10cf
+  __TEXT.__objc_methtype: 0x4ab1
+  __TEXT.__gcc_except_tab: 0x24c4
+  __TEXT.__objc_methname: 0x1c980
+  __TEXT.__oslogstring: 0x3582
+  __TEXT.__swift5_typeref: 0x17ca
   __TEXT.__swift5_capture: 0xb78
   __TEXT.__swift5_reflstr: 0xfc4
   __TEXT.__swift5_assocty: 0x190
-  __TEXT.__constg_swiftt: 0xe58
+  __TEXT.__constg_swiftt: 0xe60
   __TEXT.__swift5_builtin: 0x78
   __TEXT.__swift5_fieldmd: 0xf3c
   __TEXT.__swift5_proto: 0x1cc

   __TEXT.__swift5_protos: 0x4
   __TEXT.__swift5_acfuncs: 0x104
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x73f0
+  __TEXT.__unwind_info: 0x7420
   __TEXT.__eh_frame: 0x4c4c
-  __DATA_CONST.__const: 0x8498
-  __DATA_CONST.__cfstring: 0x6600
-  __DATA_CONST.__objc_classlist: 0x3a0
+  __DATA_CONST.__const: 0x84f0
+  __DATA_CONST.__cfstring: 0x6620
+  __DATA_CONST.__objc_classlist: 0x3a8
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x178
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_dictobj: 0x50
   __DATA_CONST.__objc_doubleobj: 0x20
   __DATA_CONST.__auth_got: 0x1d08
-  __DATA_CONST.__got: 0xac8
+  __DATA_CONST.__got: 0xad8
   __DATA_CONST.__auth_ptr: 0x670
-  __DATA.__objc_const: 0x11d88
-  __DATA.__objc_selrefs: 0x5e80
+  __DATA.__objc_const: 0x11e18
+  __DATA.__objc_selrefs: 0x5ec8
   __DATA.__objc_ivar: 0x113c
-  __DATA.__objc_data: 0x2d88
-  __DATA.__data: 0x3af8
+  __DATA.__objc_data: 0x2de0
+  __DATA.__data: 0x3b18
   __DATA.__common: 0xd0
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork

   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftDistributed.dylib
+  - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 8597
-  Symbols:   1455
-  CStrings:  10854
+  Functions: 8607
+  Symbols:   1457
+  CStrings:  10887
 
Symbols:
+ _$s10Foundation4UUIDV2eeoiySbAC_ACtFZ
+ _OBJC_CLASS_$_NSScanner
+ __swift_FORCE_LOAD_$_swiftIntents
- _swift_coroFrameAlloc
CStrings:
+ "%@ RX Empty response from `%~@`: requestID=%@ appSvc=%@ error=%@\n"
+ "%@ RX Error from `%~@`: requestID=%@ appSvc=%@ error=%@\n"
+ "%@ RX RESP from '%~@': requestID=%@ appSvc=%@ response=%s serverPublicKey=%zu bytes bonjourServiceID=%@ serverPort=%u listener=%@ error=%@\n"
+ "%@ TX REQ to '%~@': requestID=%@ appSvc=%@%@\n"
+ "%@Failed to publish advertisement for service %@: %@"
+ "%@Failed to stop publishing advertisement for service %@: %@"
+ "%@Missing advertisement for service %@"
+ "%@Now %lu pending advertisements after cancelling %@"
+ "%@Now %lu pending advertisements after publishing %@"
+ "%@Pending advertisement for %@ was cancelled"
+ "%@Successfully published advertisement (%lu total) for service %@: %@"
+ "%@Successfully stopped advertisement for service: %@"
+ "%@Unpublished advertisement (%lu total) for service %@"
+ "/System/Library/PrivateFrameworks/AirPlaySupport.framework/AirPlaySupport"
+ "@48@0:8@16@24@32@?40"
+ "APSGetP2PAllow"
+ "BLE NearbyActionV2 device lost for device we were not tracking: %@\n"
+ "Failed to activate cLink %@: %@"
+ "No handler for requestID %{public}s on flags [%{public}s] (registered under: %{public}s)"
+ "RPNWTXTUtils"
+ "RX Empty response from `%~@`: requestID=%@ appSvc=%@ error=%@\n"
+ "RX Error from `%~@`: requestID=%@ appSvc=%@ error=%@\n"
+ "RX RESP from '%~@': requestID=%@ appSvc=%@ response=%s bytes listener=%@ error=%@\n"
+ "RapportDefaultPersonaID"
+ "Register eventID %{public}s registration %s persona %{public}s with handlers: %{public}s"
+ "Register requestID %{public}s registration %s persona %{public}s with handlers: %{public}s"
+ "Setting up cLink %@"
+ "TX REQ to '%~@': requestID=%@ appSvc=%@%@\n"
+ "Unable to find Service Directory request sender %@"
+ "_txtRecordForApplicationService:"
+ "initWithBytes:length:encoding:"
+ "initWithUnsignedLongLong:"
+ "registerEventID:persona:options:handler:"
+ "registerRequestID:persona:options:handler:"
+ "scanUnsignedLongLong:"
+ "statusFlagsForEndpoint:"
+ "statusFlagsForTXTRecord:"
+ "updateStatusFlags:onEndpoint:operation:"
+ "updateStatusFlags:onTXTRecord:operation:"
+ "v40@0:8Q16@24Q32"
- "Failed to activate cLink: %@"
- "No message handler registered for request ID %{public}s"
- "Register eventID %{public}s registration %s with handlers: %{public}s"
- "Register requestID %{public}s registration %s with handlers: %{public}s"
- "Setting up cLink"
- "Unable to find Service Directory sender %@"
- "txtRecordForApplicationService:"
```
