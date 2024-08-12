## amfid

> `/usr/libexec/amfid`

```diff

-938.0.23.0.0
-  __TEXT.__text: 0x18dcc
-  __TEXT.__auth_stubs: 0x14c0
-  __TEXT.__objc_stubs: 0xbc0
+938.0.31.0.0
+  __TEXT.__text: 0x19604
+  __TEXT.__auth_stubs: 0x14f0
+  __TEXT.__objc_stubs: 0xc40
   __TEXT.__init_offsets: 0x8
-  __TEXT.__objc_methlist: 0x154
+  __TEXT.__objc_methlist: 0x194
   __TEXT.__const: 0xaef
-  __TEXT.__gcc_except_tab: 0x500
-  __TEXT.__oslogstring: 0x13e2
-  __TEXT.__cstring: 0x1790
+  __TEXT.__gcc_except_tab: 0x504
+  __TEXT.__oslogstring: 0x1462
+  __TEXT.__cstring: 0x1940
   __TEXT.__objc_classname: 0x57
-  __TEXT.__objc_methname: 0xacd
-  __TEXT.__objc_methtype: 0x2df
+  __TEXT.__objc_methname: 0xb69
+  __TEXT.__objc_methtype: 0x2fd
   __TEXT.__swift5_typeref: 0x461
   __TEXT.__swift5_reflstr: 0x155
   __TEXT.__swift5_assocty: 0x48
-  __TEXT.__constg_swiftt: 0x274
+  __TEXT.__constg_swiftt: 0x284
   __TEXT.__swift5_fieldmd: 0x1a4
   __TEXT.__swift5_proto: 0x3c
   __TEXT.__swift5_types: 0x18
   __TEXT.__swift5_capture: 0x1c
-  __TEXT.__unwind_info: 0x720
-  __TEXT.__eh_frame: 0x360
-  __DATA_CONST.__auth_got: 0xa78
+  __TEXT.__unwind_info: 0x740
+  __TEXT.__eh_frame: 0x3d0
+  __DATA_CONST.__auth_got: 0xa90
   __DATA_CONST.__got: 0x368
   __DATA_CONST.__auth_ptr: 0x1d8
-  __DATA_CONST.__const: 0x9f8
-  __DATA_CONST.__cfstring: 0x480
+  __DATA_CONST.__const: 0xa38
+  __DATA_CONST.__cfstring: 0x5a0
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_arraydata: 0x90
   __DATA_CONST.__objc_dictobj: 0x168
   __DATA_CONST.__objc_intobj: 0x30
-  __DATA.__objc_const: 0x8d0
-  __DATA.__objc_selrefs: 0x370
-  __DATA.__objc_ivar: 0x4
+  __DATA.__objc_const: 0x930
+  __DATA.__objc_selrefs: 0x398
+  __DATA.__objc_ivar: 0x8
   __DATA.__objc_data: 0x220
-  __DATA.__data: 0x620
+  __DATA.__data: 0x630
   __DATA.__common: 0xc8
   __DATA.__bss: 0x828
   __RESTRICT.__restrict: 0x0

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftObservation.dylib
   - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswift_errno.dylib
+  - /usr/lib/swift/libswift_math.dylib
+  - /usr/lib/swift/libswift_signal.dylib
+  - /usr/lib/swift/libswift_stdio.dylib
+  - /usr/lib/swift/libswift_time.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 517
-  Symbols:   519
-  CStrings:  514
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
+  Functions: 528
+  Symbols:   530
+  CStrings:  538
 
Symbols:
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_math
+ __swift_FORCE_LOAD_$_swift_signal
+ __swift_FORCE_LOAD_$_swift_stdio
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swiftsys_time
+ __swift_FORCE_LOAD_$_swiftunistd
+ _objc_destroyWeak
+ _objc_loadWeakRetained
+ _objc_storeWeak
CStrings:
+ "%!s(MISSING): attempting to kick-off developer-mode-daemons"
+ "%!s(MISSING): skipping developer-mode-daemons initiation"
+ "-[AMFIService initiateDeveloperModeDaemonsWithReply:]"
+ "-[AMFIService removeManagedStateWithReply:]"
+ "-[AMFIService signTeamID:withSignType:withLAContext:withReply:]"
+ "-[AMFIService verifyBoolEntitlement:]"
+ "@\"NSXPCConnection\""
+ "T@\"NSXPCConnection\",W,V_connection"
+ "[%!s(MISSING)] invalid: %!@(MISSING)"
+ "[%!s(MISSING)] missing: %!@(MISSING)"
+ "_connection"
+ "com.apple.private.amfi.commit-profile"
+ "com.apple.private.amfi.data-migration"
+ "com.apple.private.amfi.developer-mode-control"
+ "com.apple.private.amfi.remove-trust"
+ "com.apple.private.amfi.schedule-profile"
+ "com.apple.private.amfi.set-demo"
+ "com.apple.private.amfi.set-managed"
+ "com.apple.private.amfi.set-supervised"
+ "com.apple.private.amfi.set-trust"
+ "connection"
+ "initiateDeveloperModeDaemonsWithReply:"
+ "removeManagedStateWithReply:"
+ "setConnection:"
+ "signTeamID:withSignType:withLAContext:withReply:"
+ "v24@0:8@16"
+ "valueForEntitlement:"
+ "verifyBoolEntitlement:"
- "-[AMFIService removeManagedStatewithReply:]"
- "-[AMFIService signTeamId:withSignType:withLAContext:withReply:]"
- "removeManagedStatewithReply:"
- "signTeamId:withSignType:withLAContext:withReply:"

```
