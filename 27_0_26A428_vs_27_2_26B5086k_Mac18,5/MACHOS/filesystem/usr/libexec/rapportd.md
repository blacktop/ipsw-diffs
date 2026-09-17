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

-751.100.1.0.0
-  __TEXT.__text: 0x1784b4
+751.200.31.0.0
+  __TEXT.__text: 0x17a84c
   __TEXT.__auth_stubs: 0x3500
-  __TEXT.__objc_stubs: 0x119c0
-  __TEXT.__objc_methlist: 0x8f88
-  __TEXT.__const: 0x6110
-  __TEXT.__cstring: 0x2fa46
-  __TEXT.__objc_classname: 0xf4f
-  __TEXT.__objc_methtype: 0x4491
-  __TEXT.__gcc_except_tab: 0x2348
-  __TEXT.__objc_methname: 0x19b40
-  __TEXT.__oslogstring: 0x31e2
-  __TEXT.__swift5_typeref: 0x173a
+  __TEXT.__objc_stubs: 0x11b00
+  __TEXT.__objc_methlist: 0x8fc8
+  __TEXT.__const: 0x6180
+  __TEXT.__cstring: 0x2fe26
+  __TEXT.__objc_classname: 0xf5f
+  __TEXT.__objc_methtype: 0x44b1
+  __TEXT.__gcc_except_tab: 0x235c
+  __TEXT.__objc_methname: 0x19c80
+  __TEXT.__oslogstring: 0x3222
+  __TEXT.__swift5_typeref: 0x178e
   __TEXT.__swift5_capture: 0xb38
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
-  __TEXT.__unwind_info: 0x6a38
+  __TEXT.__unwind_info: 0x6a68
   __TEXT.__eh_frame: 0x4bbc
-  __DATA_CONST.__const: 0x8068
-  __DATA_CONST.__cfstring: 0x5f60
-  __DATA_CONST.__objc_classlist: 0x368
+  __DATA_CONST.__const: 0x80c8
+  __DATA_CONST.__cfstring: 0x5f80
+  __DATA_CONST.__objc_classlist: 0x370
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x148
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_dictobj: 0x50
   __DATA_CONST.__objc_doubleobj: 0x10
   __DATA_CONST.__auth_got: 0x1a90
-  __DATA_CONST.__got: 0xa20
+  __DATA_CONST.__got: 0xa30
   __DATA_CONST.__auth_ptr: 0x660
-  __DATA.__objc_const: 0x10738
-  __DATA.__objc_selrefs: 0x5658
+  __DATA.__objc_const: 0x107c8
+  __DATA.__objc_selrefs: 0x56a8
   __DATA.__objc_ivar: 0xfd4
-  __DATA.__objc_data: 0x2b58
-  __DATA.__data: 0x35a8
+  __DATA.__objc_data: 0x2bb0
+  __DATA.__data: 0x35c8
   __DATA.__common: 0xd0
   - /System/Library/Frameworks/AVFoundation.framework/Versions/A/AVFoundation
   - /System/Library/Frameworks/CFNetwork.framework/Versions/A/CFNetwork

   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftDistributed.dylib
   - /usr/lib/swift/libswiftIOKit.dylib
+  - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 7834
-  Symbols:   1357
-  CStrings:  9880
+  Functions: 7844
+  Symbols:   1359
+  CStrings:  9910
 
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
+ "RapportDefaultPersonaID"
+ "Register eventID %{public}s registration %s persona %{public}s with handlers: %{public}s"
+ "Register requestID %{public}s registration %s persona %{public}s with handlers: %{public}s"
+ "Setting up cLink %@"
+ "Unable to find Service Directory request sender %@"
+ "_txtRecordForApplicationService:"
+ "initWithBytes:length:encoding:"
+ "initWithString:"
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
