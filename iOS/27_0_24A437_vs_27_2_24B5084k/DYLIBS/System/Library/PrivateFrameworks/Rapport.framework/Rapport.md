## Rapport

> `/System/Library/PrivateFrameworks/Rapport.framework/Rapport`

```diff

-751.100.2.0.0
-  __TEXT.__text: 0xd4324
-  __TEXT.__objc_methlist: 0x9f48
-  __TEXT.__cstring: 0x144ac
-  __TEXT.__const: 0x3f68
-  __TEXT.__gcc_except_tab: 0x14c4
-  __TEXT.__oslogstring: 0x242d
-  __TEXT.__swift5_typeref: 0xbd5
-  __TEXT.__swift5_capture: 0x890
-  __TEXT.__swift5_fieldmd: 0xb28
-  __TEXT.__constg_swiftt: 0xd94
-  __TEXT.__swift5_reflstr: 0x91c
+751.200.31.0.0
+  __TEXT.__text: 0xd8a60
+  __TEXT.__objc_methlist: 0x9fe0
+  __TEXT.__cstring: 0x145fc
+  __TEXT.__const: 0x41b8
+  __TEXT.__gcc_except_tab: 0x14d8
+  __TEXT.__oslogstring: 0x26fd
+  __TEXT.__swift5_typeref: 0xc4f
+  __TEXT.__swift5_capture: 0x950
+  __TEXT.__swift5_fieldmd: 0xb34
+  __TEXT.__constg_swiftt: 0xdbc
+  __TEXT.__swift5_reflstr: 0x93c
   __TEXT.__swift5_proto: 0x144
   __TEXT.__swift5_types: 0xb0
   __TEXT.__swift_as_entry: 0x14

   __TEXT.__swift5_builtin: 0x50
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0x3af0
+  __TEXT.__unwind_info: 0x3b50
   __TEXT.__eh_frame: 0x960
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x27e8
-  __DATA_CONST.__objc_classlist: 0x2c8
+  __DATA_CONST.__const: 0x2810
+  __DATA_CONST.__objc_classlist: 0x2d0
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x150
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x44e0
+  __DATA_CONST.__objc_selrefs: 0x4558
   __DATA_CONST.__objc_protorefs: 0xe0
   __DATA_CONST.__objc_superrefs: 0x1f0
   __DATA_CONST.__objc_arraydata: 0xb0
-  __DATA_CONST.__got: 0x4d0
-  __AUTH_CONST.__const: 0x2658
-  __AUTH_CONST.__cfstring: 0x60a0
-  __AUTH_CONST.__objc_const: 0x112f8
-  __AUTH_CONST.__objc_intobj: 0x240
+  __DATA_CONST.__got: 0x4e0
+  __AUTH_CONST.__const: 0x27c0
+  __AUTH_CONST.__cfstring: 0x6100
+  __AUTH_CONST.__objc_const: 0x113e8
+  __AUTH_CONST.__objc_intobj: 0x258
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_dictobj: 0x78
-  __AUTH_CONST.__auth_got: 0x1140
-  __AUTH.__objc_data: 0x1280
+  __AUTH_CONST.__auth_got: 0x1178
+  __AUTH.__objc_data: 0x1300
   __AUTH.__data: 0x538
-  __DATA.__objc_ivar: 0x10f4
-  __DATA.__data: 0x20d8
+  __DATA.__objc_ivar: 0x10f8
+  __DATA.__data: 0x20e8
   __DATA.__common: 0x68
   __DATA_DIRTY.__objc_data: 0x1318
   __DATA_DIRTY.__data: 0x588

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 5746
-  Symbols:   8214
-  CStrings:  3009
+  Functions: 5785
+  Symbols:   8255
+  CStrings:  3030
 
Symbols:
+ +[RPNWTXTUtils statusFlagsForEndpoint:]
+ +[RPNWTXTUtils statusFlagsForTXTRecord:]
+ +[RPNWTXTUtils updateStatusFlags:onEndpoint:operation:]
+ +[RPNWTXTUtils updateStatusFlags:onTXTRecord:operation:]
+ -[RPClient endpointContextForService:trustCircles:completion:]
+ -[RPClient updateEndpointAttributes:forService:usingContext:completion:]
+ -[RPConnection _identityDaemonGetPairingIdentityFromHomeWithAccessory:completion:]
+ -[RPConnection _requestIDIsHighVolume:messageIsChatty:]
+ -[RPSiriSession _triggerInfoRequest]
+ -[RPSiriSession setTriggerDurationMs:]
+ -[RPSiriSession setTwoShotFeedbackDelaySec:]
+ -[RPSiriSession triggerDurationMs]
+ -[RPSiriSession twoShotFeedbackDelaySec]
+ GCC_except_table280
+ GCC_except_table73
+ GCC_except_table92
+ _OBJC_CLASS_$_NSScanner
+ _OBJC_CLASS_$_RPNWTXTUtils
+ _OBJC_IVAR_$_RPSiriSession._triggerDurationMs
+ _OBJC_IVAR_$_RPSiriSession._twoShotFeedbackDelaySec
+ _OBJC_METACLASS_$_RPNWTXTUtils
+ __OBJC_$_CLASS_METHODS_RPNWTXTUtils
+ __OBJC_CLASS_RO_$_RPNWTXTUtils
+ __OBJC_METACLASS_RO_$_RPNWTXTUtils
+ ___40+[RPNWTXTUtils statusFlagsForTXTRecord:]_block_invoke
+ ___62-[RPClient endpointContextForService:trustCircles:completion:]_block_invoke
+ ___72-[RPClient updateEndpointAttributes:forService:usingContext:completion:]_block_invoke
+ ___block_descriptor_40_e8_32r_e19_B36?0r*8i16r*20Q28lr32l8
+ ___swift_closure_destructor.142Tm
+ ___swift_closure_destructor.154Tm
+ ___swift_closure_destructor.186Tm
+ ___swift_closure_destructor.253Tm
+ _nw_endpoint_copy_txt_record
+ _nw_endpoint_set_txt_record
+ _nw_txt_record_access_key
+ _nw_txt_record_create_dictionary
+ _nw_txt_record_set_key
+ _objc_msgSend$_identityDaemonGetPairingIdentityFromHomeWithAccessory:completion:
+ _objc_msgSend$_requestIDIsHighVolume:messageIsChatty:
+ _objc_msgSend$_triggerInfoRequest
+ _objc_msgSend$cStringUsingEncoding:
+ _objc_msgSend$identityResolved
+ _objc_msgSend$identityVerified
+ _objc_msgSend$scanUnsignedLongLong:
+ _objc_msgSend$statusFlagsForTXTRecord:
+ _objc_msgSend$stringValue
+ _objc_msgSend$updateStatusFlags:onTXTRecord:operation:
+ _swift_deletedMethodError
+ _swift_retain_x28
+ _symbolic So10RPIdentityC
+ _symbolic So10RPIdentityCSgIeghg_
+ _symbolic So16CUPairingSessionCSgXw
+ _symbolic So16CUPairingSessionCSgXwz_Xx
+ _symbolic yySo10RPIdentityCSgYbccSg
- -[RPConnection _requestIDLogLevel:chatty:]
- GCC_except_table278
- GCC_except_table39
- GCC_except_table68
- GCC_except_table70
- GCC_except_table72
- GCC_except_table91
- _OBJC_IVAR_$_RPConnection._identityVerified
- ___swift_closure_destructor.143Tm
- ___swift_closure_destructor.175Tm
- ___swift_closure_destructor.242Tm
- ___swift_closure_destructor.250Tm
- _objc_msgSend$_requestIDLogLevel:chatty:
CStrings:
+ "-[RPClient endpointContextForService:trustCircles:completion:]"
+ "-[RPClient updateEndpointAttributes:forService:usingContext:completion:]"
+ "B36@?0r*8i16r*20Q28"
+ "Failed to resolve client HomeKit pairing identity for %s: %@"
+ "Identity daemon not available"
+ "PairVerify activate client"
+ "PairVerify activate client: session no longer current, ignoring"
+ "PairVerify client identity resolution result nil, will use default"
+ "PairVerify client identity resolution: session no longer current, ignoring"
+ "PairVerify client ignoring resolved identity %@, handler already set"
+ "PairVerify client will use resolved identity %@"
+ "PairVerify prepare client: AT %{public}s, CF %{public}s, FL %{public}s, PWT %{public}s"
+ "PairVerify will resolve client identity before activation"
+ "Requesting endpoint context for %@ with %#ll{flags}\n"
+ "Resolving client HomeKit pairing identity for %s"
+ "StatusFlags"
+ "Successfully resolved client HomeKit pairing identity for %s to %@"
+ "Unable to resolve client HomeKit pairing identity for %s"
+ "Updating endpoint %@ for %@ with context (%lu bytes)\n"
+ "_vtDurMs"
+ "_vtTwoShotSec"
+ "tutool"
- "PairVerify start client: AT %{public}s, CF %{public}s, FL %{public}s, PWT %{public}s"
```
