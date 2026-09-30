## Nexus

> `/System/Library/PrivateFrameworks/Nexus.framework/Nexus`

```diff

-760.26.0.0.0
-  __TEXT.__text: 0xba910
+760.34.0.0.0
+  __TEXT.__text: 0xb7880
   __TEXT.__auth_stubs: 0x1e90
   __TEXT.__objc_methlist: 0x44
   __TEXT.__cstring: 0x2513
-  __TEXT.__swift5_typeref: 0x262c
-  __TEXT.__const: 0x70b4
+  __TEXT.__swift5_typeref: 0x2612
+  __TEXT.__const: 0x7114
   __TEXT.__constg_swiftt: 0x1c2c
   __TEXT.__swift5_reflstr: 0x16b9
   __TEXT.__swift5_assocty: 0x4f0
   __TEXT.__swift5_fieldmd: 0x2070
   __TEXT.__swift5_builtin: 0xf0
   __TEXT.__swift5_mpenum: 0xf4
-  __TEXT.__swift5_proto: 0x70c
+  __TEXT.__swift5_proto: 0x710
   __TEXT.__swift5_types: 0x244
   __TEXT.__swift5_protos: 0x38
   __TEXT.__oslogstring: 0x2392
-  __TEXT.__swift5_capture: 0x15fc
-  __TEXT.__unwind_info: 0x2dd0
-  __TEXT.__eh_frame: 0x45d4
+  __TEXT.__swift5_capture: 0x12b4
+  __TEXT.__unwind_info: 0x2c68
+  __TEXT.__eh_frame: 0x414c
   __TEXT.__objc_classname: 0x43
   __TEXT.__objc_methname: 0x588
   __TEXT.__objc_methtype: 0xad
   __TEXT.__objc_stubs: 0x40
-  __DATA_CONST.__got: 0x470
+  __DATA_CONST.__got: 0x480
   __DATA_CONST.__const: 0x388
   __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1f0
+  __DATA_CONST.__objc_selrefs: 0x1f8
   __DATA_CONST.__objc_protorefs: 0x20
   __AUTH_CONST.__auth_got: 0xf50
-  __AUTH_CONST.__auth_ptr: 0x5b0
-  __AUTH_CONST.__const: 0x6ba0
+  __AUTH_CONST.__auth_ptr: 0x5a8
+  __AUTH_CONST.__const: 0x6a10
   __AUTH_CONST.__objc_const: 0x17d8
   __AUTH.__objc_data: 0x200
-  __AUTH.__data: 0xd78
-  __DATA.__data: 0x12c0
-  __DATA.__bss: 0xe390
+  __AUTH.__data: 0xd68
+  __DATA.__data: 0x1200
+  __DATA.__bss: 0xe420
   __DATA.__common: 0x88
   - /System/Library/Frameworks/Combine.framework/Combine
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 3913
-  Symbols:   395
+  Functions: 3855
+  Symbols:   391
   CStrings:  655
 
CStrings:
+ "### CUMessageSession request failed: id=%!{(MISSING)public}s, error=%!@(MISSING)"
+ "### NAN publisher start failed: error=%!@(MISSING)"
+ "### NAN subscriber start failed: error=%!@(MISSING)"
+ "### connection failed: peer=%!s(MISSING), error=%!@(MISSING)"
+ "### network server create failed: error=%!@(MISSING)"
+ "### network server failed: error=%!@(MISSING)"
+ "### process header failed: data=<%!s(MISSING)>, error=%!@(MISSING)"
+ "### process message failed: type=%!h(MISSING)hu, error=%!@(MISSING)"
+ "### request failed: xid=%!s(MISSING), name=%!s(MISSING), error=%!@(MISSING)"
+ "### response received: xid=%!s(MISSING), decode error=%!@(MISSING)"
+ "### run error: state=%!s(MISSING), error=%!@(MISSING)"
+ "PairSetup failed: error=%!@(MISSING)"
+ "PairVerify failed: error=%!@(MISSING)"
+ "connection ended: during body, error=%!@(MISSING)"
+ "connection ended: during header, error=%!@(MISSING)"
+ "connection waiting: peer=%!s(MISSING), error=%!@(MISSING))"
+ "network server waiting: error=%!@(MISSING)"
+ "pairing sign failed: flags=0x%!x(MISSING), message=%!l(MISSING)d bytes, error=%!@(MISSING)"
+ "pairing verify failed: message=%!l(MISSING)d bytes, signature=%!l(MISSING)d bytes, error=%!@(MISSING)"
+ "response queue: xid=%!{(MISSING)public}s, data=%!{(MISSING)bool}d, dict=%!{(MISSING)bool}d, error=%!@(MISSING)"
+ "response received: xid=%!s(MISSING), error=%!@(MISSING)"
- "### CUMessageSession request failed: id=%!{(MISSING)public}s, error=%!s(MISSING)"
- "### NAN publisher start failed: error=%!s(MISSING)"
- "### NAN subscriber start failed: error=%!s(MISSING)"
- "### connection failed: peer=%!s(MISSING), error=%!s(MISSING)"
- "### network server create failed: error=%!s(MISSING)"
- "### network server failed: error=%!s(MISSING)"
- "### process header failed: data=<%!s(MISSING)>, error=%!s(MISSING)"
- "### process message failed: type=%!h(MISSING)hu, error=%!s(MISSING)"
- "### request failed: xid=%!s(MISSING), name=%!s(MISSING), error=%!s(MISSING)"
- "### response received: xid=%!s(MISSING), decode error=%!s(MISSING)"
- "### run error: state=%!s(MISSING), error=%!s(MISSING)"
- "PairSetup failed: error=%!s(MISSING)"
- "PairVerify failed: error=%!s(MISSING)"
- "connection ended: during body, error=%!s(MISSING)"
- "connection ended: during header, error=%!s(MISSING)"
- "connection waiting: peer=%!s(MISSING), error=%!s(MISSING))"
- "network server waiting: error=%!s(MISSING)"
- "pairing sign failed: flags=0x%!x(MISSING), message=%!l(MISSING)d bytes, error=%!s(MISSING)"
- "pairing verify failed: message=%!l(MISSING)d bytes, signature=%!l(MISSING)d bytes, error=%!s(MISSING)"
- "response queue: xid=%!{(MISSING)public}s, data=%!{(MISSING)bool}d, dict=%!{(MISSING)bool}d, error=%!s(MISSING)"
- "response received: xid=%!s(MISSING), error=%!s(MISSING)"

```
