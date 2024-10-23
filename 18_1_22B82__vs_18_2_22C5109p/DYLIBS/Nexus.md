## Nexus

> `/System/Library/PrivateFrameworks/Nexus.framework/Nexus`

```diff

-752.1.0.0.0
-  __TEXT.__text: 0x99830
-  __TEXT.__auth_stubs: 0x1880
+760.26.0.0.0
+  __TEXT.__text: 0xba910
+  __TEXT.__auth_stubs: 0x1e90
   __TEXT.__objc_methlist: 0x44
-  __TEXT.__cstring: 0x21b3
-  __TEXT.__swift5_typeref: 0x2340
-  __TEXT.__const: 0x6754
-  __TEXT.__swift5_reflstr: 0x1419
-  __TEXT.__swift5_assocty: 0x460
-  __TEXT.__constg_swiftt: 0x1a3c
-  __TEXT.__swift5_fieldmd: 0x1d24
+  __TEXT.__cstring: 0x2513
+  __TEXT.__swift5_typeref: 0x262c
+  __TEXT.__const: 0x70b4
+  __TEXT.__constg_swiftt: 0x1c2c
+  __TEXT.__swift5_reflstr: 0x16b9
+  __TEXT.__swift5_assocty: 0x4f0
+  __TEXT.__swift5_fieldmd: 0x2070
   __TEXT.__swift5_builtin: 0xf0
-  __TEXT.__swift5_mpenum: 0x108
-  __TEXT.__swift5_proto: 0x678
-  __TEXT.__swift5_types: 0x218
-  __TEXT.__swift5_capture: 0x144c
+  __TEXT.__swift5_mpenum: 0xf4
+  __TEXT.__swift5_proto: 0x70c
+  __TEXT.__swift5_types: 0x244
   __TEXT.__swift5_protos: 0x38
-  __TEXT.__oslogstring: 0x1e92
-  __TEXT.__unwind_info: 0x28f0
-  __TEXT.__eh_frame: 0x4204
-  __TEXT.__objc_classname: 0x17
-  __TEXT.__objc_methname: 0x4aa
+  __TEXT.__oslogstring: 0x2392
+  __TEXT.__swift5_capture: 0x15fc
+  __TEXT.__unwind_info: 0x2dd0
+  __TEXT.__eh_frame: 0x45d4
+  __TEXT.__objc_classname: 0x43
+  __TEXT.__objc_methname: 0x588
   __TEXT.__objc_methtype: 0xad
-  __DATA_CONST.__got: 0x340
-  __DATA_CONST.__const: 0x2e8
+  __TEXT.__objc_stubs: 0x40
+  __DATA_CONST.__got: 0x470
+  __DATA_CONST.__const: 0x388
   __DATA_CONST.__objc_classlist: 0x40
-  __DATA_CONST.__objc_protolist: 0x20
+  __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x178
-  __DATA_CONST.__objc_protorefs: 0x10
-  __AUTH_CONST.__auth_got: 0xc40
-  __AUTH_CONST.__auth_ptr: 0x4f0
-  __AUTH_CONST.__const: 0x66b0
-  __AUTH_CONST.__objc_const: 0x1740
-  __AUTH.__objc_data: 0x110
-  __AUTH.__data: 0xa90
-  __DATA.__data: 0xf60
-  __DATA.__bss: 0xce40
-  __DATA.__common: 0x8
+  __DATA_CONST.__objc_selrefs: 0x1f0
+  __DATA_CONST.__objc_protorefs: 0x20
+  __AUTH_CONST.__auth_got: 0xf50
+  __AUTH_CONST.__auth_ptr: 0x5b0
+  __AUTH_CONST.__const: 0x6ba0
+  __AUTH_CONST.__objc_const: 0x17d8
+  __AUTH.__objc_data: 0x200
+  __AUTH.__data: 0xd78
+  __DATA.__data: 0x12c0
+  __DATA.__bss: 0xe390
+  __DATA.__common: 0x88
   - /System/Library/Frameworks/Combine.framework/Combine
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 3499
-  Symbols:   376
-  CStrings:  586
+  Functions: 3913
+  Symbols:   395
+  CStrings:  655
 
Symbols:
+ _CUGestaltDeviceClassToString
+ _CUNextID32
+ _OBJC_CLASS_$_NSString
+ _OBJC_CLASS_$_OS_dispatch_queue_serial_executor
+ _OBJC_CLASS_$_OS_dispatch_source
+ _nw_endpoint_copy_address_string
+ _nw_endpoint_get_bonjour_service_name
+ _nw_endpoint_get_hostname
+ _nw_endpoint_get_url
+ _objc_alloc
+ _swift_getKeyPath
+ _swift_getTupleTypeLayout2
+ _swift_initStackObject
+ _swift_setAtWritableKeyPath
+ _xpc_dictionary_set_bool
- _swift_weakAssign
CStrings:
+ "### request send failed: xid=%!{(MISSING)public}s, cid=%!u(MISSING), %!l(MISSING)d/%!l(MISSING)d, error=%!@(MISSING)"
+ "### request send start failed: xid=%!{(MISSING)public}s, cid=%!u(MISSING), %!l(MISSING)d/%!l(MISSING)d, error=%!@(MISSING)"
+ "### response received: unencrypted, xid=%!s(MISSING)"
+ "### response send encode failed: xid=%!{(MISSING)public}s, error=%!@(MISSING)"
+ "### response send failed: xid=%!{(MISSING)public}s, cid=%!u(MISSING), %!l(MISSING)d/%!l(MISSING)d, error=%!@(MISSING)"
+ "### response send start failed: xid=%!{(MISSING)public}s, cid=%!u(MISSING), %!l(MISSING)d/%!l(MISSING)d, error=%!@(MISSING)"
+ ", fixedPassword="
+ ", peerDeviceClass="
+ "Case 'nw' cannot be encoded because it is not defined in CodingKeys."
+ "Connection deinit"
+ "Endpoint without Bonjour type"
+ "NAN data session stop"
+ "NAN discover match setupID: nanEndpoint=%!@(MISSING), nxEndpoint=%!s(MISSING)"
+ "NAN discover mismatch: nanEndpoint=%!@(MISSING), nxEndpoint=%!s(MISSING)"
+ "NAN discover stop"
+ "NAN publisher update textInfo: [%!s(MISSING)]"
+ "NXEndpoint.nw is not supported over XPC"
+ "Nexus/NXConnection.swift"
+ "OS_dispatch_source"
+ "OS_dispatch_source_timer"
+ "Request timeout ("
+ "_authenticationConfiguration"
+ "_bonjourBrowser"
+ "_bonjourEndpoint"
+ "_cuEnvironment"
+ "_hasCUEnvironment"
+ "_pauseBeforePairing"
+ "_requestHistory"
+ "authenticationConfiguration"
+ "authenticationConfiguration={"
+ "bad expectedSetupID="
+ "bad foundSetupID="
+ "bluetoothSetupID"
+ "bluetoothSetupID="
+ "bonjour discover cancelled"
+ "bonjour discover failed: error=%!@(MISSING)"
+ "bonjour discover ignore: endpoint=%!s(MISSING), metadata=%!s(MISSING), reason=%!s(MISSING)"
+ "bonjour discover match: nwEndpoint=%!s(MISSING), nxEndpoint=%!s(MISSING)"
+ "bonjour discover mismatch: found=0x%!l(MISSING)x, expected=0x%!l(MISSING)x"
+ "bonjour discover ready"
+ "bonjour discover start: type=%!s(MISSING)"
+ "bonjour discover stop"
+ "bonjour discover unknown state"
+ "bonjour discover waiting: error=%!@(MISSING)"
+ "bonjourServiceType"
+ "bonjourServiceType="
+ "btAddressData"
+ "connectionID"
+ "identifier"
+ "initWithUTF8String:"
+ "languageCode"
+ "localeIdentifier"
+ "nearbyActionExtraData"
+ "needsNetwork"
+ "network client connection ended: cid=%!u(MISSING), endpoint=%!s(MISSING), error=%!@(MISSING)"
+ "network client connection start: cid=%!u(MISSING), endpoint=%!s(MISSING)"
+ "network server bonjour remove"
+ "network server bonjour update: name=%!s(MISSING), type=%!s(MISSING), txt=%!s(MISSING)"
+ "network server connection accepted: cid=%!u(MISSING), peer=%!s(MISSING)"
+ "network server connection ended: cid=%!u(MISSING), peer=%!s(MISSING), error=%!@(MISSING)"
+ "network server start: name=%!s(MISSING), type=%!s(MISSING), port=%!h(MISSING)u"
+ "pairPause"
+ "pairing sign failed: flags=0x%!x(MISSING), message=%!l(MISSING)d bytes, error=%!s(MISSING)"
+ "pairing verify failed: message=%!l(MISSING)d bytes, signature=%!l(MISSING)d bytes, error=%!s(MISSING)"
+ "pairingPauseConfigure"
+ "pairingPauseConfigure: pause="
+ "peerDeviceClass"
+ "request queue: xid=%!{(MISSING)public}s, name=%!{(MISSING)public}s, %!s(MISSING)"
+ "request received: xid=%!s(MISSING), name=%!s(MISSING)%!s(MISSING)"
+ "request send: xid=%!{(MISSING)public}s, cid=%!u(MISSING), %!l(MISSING)d/%!l(MISSING)d"
+ "request timeout: xid=%!{(MISSING)public}s, name=%!{(MISSING)public}s"
+ "response send: xid=%!{(MISSING)public}s, cid=%!u(MISSING), %!l(MISSING)d/%!l(MISSING)d, error=%!@(MISSING)"
+ "serviceType"
+ "setAcl:"
+ "setEndpointChangedHandler:"
+ "setFixedPIN:"
+ "setLocalize:"
+ "setNearbyActionExtraData:"
+ "setTextInfo:"
+ "si"
+ "textInfo"
+ "timeoutTimer"
+ "v20@?0@\"CUNANEndpoint\"8I16"
- "### pairing sign failed: flags=0x%!x(MISSING), message=%!l(MISSING)d bytes, error=%!s(MISSING)"
- "### pairing verify failed: message=%!l(MISSING)d bytes, signature=%!l(MISSING)d bytes, error=%!s(MISSING)"
- "### response send failed: xid=%!{(MISSING)public}s, error=%!s(MISSING)"
- ", nanTrafficFlags="
- "_bestConnection"
- "_passwordType"
- "network client connection ended: endpoint=%!s(MISSING), best=%!{(MISSING)bool}d, error=%!s(MISSING)"
- "network client connection start: endpoint=%!s(MISSING)"
- "network server connection accepted: peer=%!s(MISSING)"
- "network server connection ended: peer=%!s(MISSING), best=%!{(MISSING)bool}d, error=%!s(MISSING)"
- "network server start: port=%!h(MISSING)u"
- "request queue: xid=%!{(MISSING)public}s, name=%!{(MISSING)public}s"
- "request received: xid=%!s(MISSING), name=%!s(MISSING)"
- "request send: xid=%!{(MISSING)public}s"
- "response send: xid=%!{(MISSING)public}s, error=%!s(MISSING)"

```
