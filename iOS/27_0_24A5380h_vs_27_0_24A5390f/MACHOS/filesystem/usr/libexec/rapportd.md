## rapportd

> `/usr/libexec/rapportd`

### Sections with Same Size but Changed Content

- `__TEXT.__gcc_except_tab`
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
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__bss`
- `__DATA.__common`

```diff

-745.100.4.0.0
-  __TEXT.__text: 0x194e64
-  __TEXT.__auth_stubs: 0x39e0
+747.100.2.0.0
+  __TEXT.__text: 0x197b1c
+  __TEXT.__auth_stubs: 0x39f0
   __TEXT.__objc_stubs: 0x135e0
-  __TEXT.__objc_methlist: 0xa0e8
-  __TEXT.__const: 0x5fb0
-  __TEXT.__cstring: 0x36ed6
+  __TEXT.__objc_methlist: 0xa0c8
+  __TEXT.__const: 0x5fa0
+  __TEXT.__cstring: 0x36bb6
   __TEXT.__objc_classname: 0x10bf
-  __TEXT.__objc_methtype: 0x4ab1
+  __TEXT.__objc_methtype: 0x4a81
   __TEXT.__gcc_except_tab: 0x24b0
-  __TEXT.__objc_methname: 0x1c730
-  __TEXT.__oslogstring: 0x3492
-  __TEXT.__swift5_typeref: 0x1710
+  __TEXT.__objc_methname: 0x1c800
+  __TEXT.__oslogstring: 0x3542
+  __TEXT.__swift5_typeref: 0x1776
   __TEXT.__swift5_capture: 0xb78
   __TEXT.__swift5_reflstr: 0xfc4
   __TEXT.__swift5_assocty: 0x190
-  __TEXT.__constg_swiftt: 0xe50
+  __TEXT.__constg_swiftt: 0xe58
   __TEXT.__swift5_builtin: 0x78
   __TEXT.__swift5_fieldmd: 0xf3c
   __TEXT.__swift5_proto: 0x1cc

   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__unwind_info: 0x5968
   __TEXT.__eh_frame: 0x4c44
-  __DATA_CONST.__const: 0x8470
-  __DATA_CONST.__cfstring: 0x67a0
+  __DATA_CONST.__const: 0x8448
+  __DATA_CONST.__cfstring: 0x6600
   __DATA_CONST.__objc_classlist: 0x3a0
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x178
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0xc8
   __DATA_CONST.__objc_superrefs: 0x228
-  __DATA_CONST.__objc_intobj: 0x378
+  __DATA_CONST.__objc_intobj: 0x3c0
   __DATA_CONST.__objc_arraydata: 0x58
   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA_CONST.__objc_dictobj: 0x50
   __DATA_CONST.__objc_doubleobj: 0x20
-  __DATA_CONST.__auth_got: 0x1d00
-  __DATA_CONST.__got: 0xac0
+  __DATA_CONST.__auth_got: 0x1d08
+  __DATA_CONST.__got: 0xac8
   __DATA_CONST.__auth_ptr: 0x670
-  __DATA.__objc_const: 0x11cd0
-  __DATA.__objc_selrefs: 0x5e60
-  __DATA.__objc_ivar: 0x112c
-  __DATA.__objc_data: 0x2d80
-  __DATA.__data: 0x3ad8
+  __DATA.__objc_const: 0x11d88
+  __DATA.__objc_selrefs: 0x5e70
+  __DATA.__objc_ivar: 0x113c
+  __DATA.__objc_data: 0x2d88
+  __DATA.__data: 0x3af8
   __DATA.__bss: 0x4730
   __DATA.__common: 0xd0
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 8583
-  Symbols:   1453
-  CStrings:  10861
+  Functions: 8590
+  Symbols:   1455
+  CStrings:  10843
 
Symbols:
+ _$s10Foundation4UUIDVs23CustomStringConvertibleAAMc
+ _swift_coroFrameAlloc
CStrings:
+ "Deregistered eventID: %{public}s registration %s"
+ "Deregistered requestID: %{public}s registration %s"
+ "EventID: %{public}s handled by %s"
+ "No message handler registered for event ID %{public}s"
+ "No message handler registered for request ID %{public}s"
+ "Register eventID %{public}s registration %s with handlers: %{public}s"
+ "Register requestID %{public}s registration %s with handlers: %{public}s"
+ "RequestID: %{public}s handled by %s"
+ "T@\"NSMutableDictionary\",R,N,V_registeredEventRegistrationIDs"
+ "T@\"NSMutableDictionary\",R,N,V_registeredRequestRegistrationIDs"
+ "T@\"NSUUID\",&,N,V_registrationID"
+ "_registeredEventRegistrationIDs"
+ "_registeredRequestRegistrationIDs"
+ "_registrationID"
+ "deregisterEventID:registrationID:"
+ "deregisterRequestID:registrationID:"
+ "registeredEventRegistrationIDs"
+ "registeredRequestRegistrationIDs"
+ "registrationID"
+ "setRegistrationID:"
- "### RegisterEventID: a handler already exists for eventID '%{public}s'"
- "### RegisterRequestID: a handler already exists for request ID:'%{public}s'"
- "%@ Using IP transport over wireless or wired ethernet"
- "%@ Using P2P transport over BLE"
- "%@ Using P2P transport over WiFi"
- "%@ Using unknown transport"
- "%@ cnx state no transport\n"
- "%@ cnx state: %s\n"
- "%@ unable to evaluate cnx state, power info may be inaccurate\n"
- "-[RPCompanionLinkDaemon _logConnectionStateInformation:connection:]"
- "-[RPCompanionLinkXPCConnection logXPCConnectionInformation:]"
- "-[RPRemoteDisplayXPCConnection logXPCConnectionInformation:]"
- "AudioAccessory1,"
- "AudioAccessory5,"
- "AudioAccessory6,"
- "Deregistered event ID: %s"
- "Deregistered request ID: %s"
- "Ready"
- "Register event ID %{public}s with handlers: %{public}s"
- "Register request ID %{public}s with handlers: %{public}s"
- "XPC Cnx %@: not transmitting without source"
- "XPC Cnx %@: peer to peer source device %@"
- "XPC Cnx %@: transmitting"
- "XPC Cnx %@: transmitting from source %@"
- "_logConnectionStateInformation:connection:"
- "authCompletion"
- "daemonInvalidation"
- "errorFlagsChanged"
- "invalidated"
- "logConnectionInformation:options:"
- "logXPCConnectionInformation:"
- "netConnectionStart"
- "onDemandStart"
- "serviceDiscoveryClient:didRequestRemotePayloadForDevice:completion:"
- "sessionStart"
- "sessionStop"
- "stateChange"
- "v40@0:8@\"SDServiceDiscoveryClient\"16@\"NSString\"24@?<v@?@\"NSData\">32"
```
