## sharingd

> `filesystem/usr/libexec/sharingd`

```diff

-2094.60.3.2.1
-  __TEXT.__text: 0x7a2144
+2094.60.32.0.0
+  __TEXT.__text: 0x7a42d0
   __TEXT.__auth_stubs: 0x9e30
-  __TEXT.__objc_stubs: 0x38960
-  __TEXT.__objc_methlist: 0x201c4
-  __TEXT.__cstring: 0x42813
-  __TEXT.__objc_methname: 0x509e5
+  __TEXT.__objc_stubs: 0x389a0
+  __TEXT.__objc_methlist: 0x201cc
+  __TEXT.__cstring: 0x42853
+  __TEXT.__objc_methname: 0x50a45
   __TEXT.__objc_classname: 0x65e7
   __TEXT.__objc_methtype: 0xbc4a
-  __TEXT.__const: 0x1d600
-  __TEXT.__gcc_except_tab: 0x6de8
-  __TEXT.__oslogstring: 0x408a3
+  __TEXT.__const: 0x1d5d0
+  __TEXT.__gcc_except_tab: 0x6dfc
+  __TEXT.__oslogstring: 0x40b73
   __TEXT.__ustring: 0x94
   __TEXT.__dlopen_cstrs: 0x438
-  __TEXT.__swift5_typeref: 0xa970
+  __TEXT.__swift5_typeref: 0xa990
   __TEXT.__swift5_fieldmd: 0x9488
   __TEXT.__constg_swiftt: 0xb968
   __TEXT.__swift5_builtin: 0x370

   __TEXT.__swift5_proto: 0x16dc
   __TEXT.__swift5_types: 0x98c
   __TEXT.__swift_as_entry: 0x1028
-  __TEXT.__swift5_capture: 0x533c
-  __TEXT.__swift_as_ret: 0x104c
+  __TEXT.__swift5_capture: 0x5328
+  __TEXT.__swift_as_ret: 0x1058
   __TEXT.__swift5_mpenum: 0x1c
-  __TEXT.__unwind_info: 0x179f8
-  __TEXT.__eh_frame: 0x29ce4
+  __TEXT.__unwind_info: 0x17a40
+  __TEXT.__eh_frame: 0x29e54
   __DATA_CONST.__auth_got: 0x4f28
   __DATA_CONST.__got: 0x3608
-  __DATA_CONST.__auth_ptr: 0x1a40
-  __DATA_CONST.__const: 0x229e8
-  __DATA_CONST.__cfstring: 0x19ec0
+  __DATA_CONST.__auth_ptr: 0x1a48
+  __DATA_CONST.__const: 0x22998
+  __DATA_CONST.__cfstring: 0x19ee0
   __DATA_CONST.__objc_classlist: 0xf98
   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0x738

   __DATA_CONST.__objc_protorefs: 0x288
   __DATA_CONST.__objc_classrefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x7b8
-  __DATA_CONST.__objc_intobj: 0xd50
+  __DATA_CONST.__objc_intobj: 0xd68
   __DATA_CONST.__objc_arraydata: 0x22e8
   __DATA_CONST.__objc_dictobj: 0x16f8
   __DATA_CONST.__objc_arrayobj: 0x720
   __DATA_CONST.__objc_doubleobj: 0x20
-  __DATA.__objc_const: 0x3d3c0
-  __DATA.__objc_selrefs: 0x11678
-  __DATA.__objc_ivar: 0x2b64
+  __DATA.__objc_const: 0x3d3e0
+  __DATA.__objc_selrefs: 0x11680
+  __DATA.__objc_ivar: 0x2b68
   __DATA.__objc_data: 0xb8a0
-  __DATA.__data: 0x1af50
+  __DATA.__data: 0x1af40
   __DATA.__bss: 0x17dc0
   __DATA.__common: 0xb48
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: A2798C4D-FCE6-3D52-9B60-83F76D67DC85
-  Functions: 29402
-  Symbols:   4559
-  CStrings:  32343
+  UUID: 664D74D1-2F92-3316-8B52-649A3BF49B1F
+  Functions: 29409
+  Symbols:   4560
+  CStrings:  32355
 
Symbols:
+ _$s7Sharing15DeviceLockStateOMn
+ _OBJC_CLASS_$_DADaemonSession
- _OBJC_CLASS_$_DASession
CStrings:
+ "@\"DADaemonSession\""
+ "Pin Pairing initial resolve callback {resolverStatus: %u, hasEndpoints: %{bool}d}"
+ "Pin Pairing resolve callback -- already handled {resolverStatus: %u, retryCount: %ld}"
+ "Pin Pairing resolve callback -- no endpoints returned {resolverStatus: %u, retryCount: %ld}"
+ "Pin Pairing resolve callback -- no handled AppSvcPairingResult {endpointCount: %ld, retryCount: %ld}"
+ "Pin Pairing resolve callback received {resolverStatus: %u, endpointCount: %ld, retryCount: %ld}"
+ "Pin Pairing resolve endpoint {index: %ld, AppSvcPairingResult: %s, retryCount: %ld}"
+ "Pin Pairing resolve with PIN failed {retryCount: %ld}"
+ "Pin Pairing resolve with PIN succeeded {retryCount: %ld}"
+ "Recreated PIN events stream (cleared buffered events)"
+ "Update from DAAuthorizationChangeNotification"
+ "_daAuthorizationToken"
+ "_synchronousRemoteObjectProxyForConnection:"
+ "_teardownDAAuthorizationMonitor"
+ "com.apple.private.sharing.activity-advertiser"
+ "process %d tried to connect to the handoff advertising server, but it was not entitled!"
+ "vicinity"
- "@\"DASession\""
- "Pin Pairing resolve with PIN failed (retryCount: %ld)"
- "Pin Pairing resolve with PIN succeeded"
- "Resolve Completed"
- "Triggered from DAAuthorizationChangeNotification"
- "_daAuthorizationChanged:"

```
