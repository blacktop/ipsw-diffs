## Nexus

> `/System/Library/PrivateFrameworks/Nexus.framework/Nexus`

```diff

-760.34.0.0.0
-  __TEXT.__text: 0xb7880
-  __TEXT.__auth_stubs: 0x1e90
+760.36.0.0.0
+  __TEXT.__text: 0xba3c8
+  __TEXT.__auth_stubs: 0x1f80
   __TEXT.__objc_methlist: 0x44
-  __TEXT.__cstring: 0x2513
-  __TEXT.__swift5_typeref: 0x2612
-  __TEXT.__const: 0x7114
-  __TEXT.__constg_swiftt: 0x1c2c
-  __TEXT.__swift5_reflstr: 0x16b9
+  __TEXT.__const: 0x72a4
+  __TEXT.__cstring: 0x26c3
+  __TEXT.__swift5_typeref: 0x263a
+  __TEXT.__oslogstring: 0x2452
+  __TEXT.__constg_swiftt: 0x1c94
+  __TEXT.__swift5_reflstr: 0x17a9
   __TEXT.__swift5_assocty: 0x4f0
-  __TEXT.__swift5_fieldmd: 0x2070
+  __TEXT.__swift5_fieldmd: 0x2104
   __TEXT.__swift5_builtin: 0xf0
   __TEXT.__swift5_mpenum: 0xf4
   __TEXT.__swift5_proto: 0x710
-  __TEXT.__swift5_types: 0x244
+  __TEXT.__swift5_types: 0x248
   __TEXT.__swift5_protos: 0x38
-  __TEXT.__oslogstring: 0x2392
   __TEXT.__swift5_capture: 0x12b4
-  __TEXT.__unwind_info: 0x2c68
-  __TEXT.__eh_frame: 0x414c
+  __TEXT.__unwind_info: 0x2c98
+  __TEXT.__eh_frame: 0x4194
   __TEXT.__objc_classname: 0x43
   __TEXT.__objc_methname: 0x588
   __TEXT.__objc_methtype: 0xad
   __TEXT.__objc_stubs: 0x40
-  __DATA_CONST.__got: 0x480
+  __DATA_CONST.__got: 0x488
   __DATA_CONST.__const: 0x388
-  __DATA_CONST.__objc_classlist: 0x40
+  __DATA_CONST.__objc_classlist: 0x48
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x1f8
   __DATA_CONST.__objc_protorefs: 0x20
-  __AUTH_CONST.__auth_got: 0xf50
-  __AUTH_CONST.__auth_ptr: 0x5a8
+  __AUTH_CONST.__auth_got: 0xfc8
+  __AUTH_CONST.__auth_ptr: 0x5d0
   __AUTH_CONST.__const: 0x6a10
-  __AUTH_CONST.__objc_const: 0x17d8
-  __AUTH.__objc_data: 0x200
-  __AUTH.__data: 0xd68
+  __AUTH_CONST.__objc_const: 0x1988
+  __AUTH.__objc_data: 0x250
+  __AUTH.__data: 0xe78
   __DATA.__data: 0x1200
-  __DATA.__bss: 0xe420
+  __DATA.__bss: 0xe4a0
   __DATA.__common: 0x88
   - /System/Library/Frameworks/Combine.framework/Combine
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 3855
-  Symbols:   391
-  CStrings:  655
+  Functions: 3865
+  Symbols:   393
+  CStrings:  680
 
Symbols:
+ __os_signpost_emit_with_name_impl
CStrings:
+ "### ignoring pairing start received on client"
+ "%!s(MISSING)"
+ "[Error] Interval already ended"
+ "_TtC5Nexus23NXOSSignpostTransaction"
+ "_name"
+ "_signpostBonjourDiscover"
+ "_signpostID"
+ "_signpostIPConnect"
+ "_signpostNANDiscover"
+ "_signpostNANSessionStart"
+ "_signpostPairSetup"
+ "_signpostPairVerify"
+ "_signpostStart"
+ "_signposter"
+ "bonjourDiscover"
+ "completed-unexpected"
+ "connect"
+ "ipConnect"
+ "nanSessionStart"
+ "pairSetup"
+ "pairVerify"
+ "pairing completed: pairSetup, duration=%!l(MISSING)lu ms"
+ "pairing completed: pairVerify, duration=%!l(MISSING)lu ms"
+ "pairing received: pairSetup, start=%!{(MISSING)bool}d, data=%!l(MISSING)d bytes"
+ "pairing received: pairVerify, start=%!{(MISSING)bool}d, data=%!l(MISSING)d bytes"
+ "pairing send: pairSetup, start=%!{(MISSING)bool}d, data=%!l(MISSING)d bytes"
+ "pairing send: pairVerify, start=%!{(MISSING)bool}d, data=%!l(MISSING)d bytes"
+ "pairing start: pairSetup"
+ "pairing start: pairVerify"
+ "ready-unexpected"
+ "state changed: %!s(MISSING) -> %!s(MISSING)"
- "### ignoring Pairing start received on client"
- "pairing completed: setup=%!{(MISSING)bool}d, duration=%!l(MISSING)lu ms"
- "pairing received: setup=%!{(MISSING)bool}d, start=%!{(MISSING)bool}d, data=%!l(MISSING)d bytes"
- "pairing send: setup=%!{(MISSING)bool}d, start=%!{(MISSING)bool}d, data=%!l(MISSING)d bytes"
- "pairing start: setup=%!{(MISSING)bool}d"
- "state changed: old=%!s(MISSING), new=%!s(MISSING)"

```
