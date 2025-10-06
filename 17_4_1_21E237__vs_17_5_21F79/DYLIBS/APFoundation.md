## APFoundation

> `/System/Library/PrivateFrameworks/APFoundation.framework/APFoundation`

```diff

-510.12.0.0.0
-  __TEXT.__text: 0xd1520
-  __TEXT.__auth_stubs: 0x15e0
-  __TEXT.__objc_methlist: 0x3820
+511.16.0.0.0
+  __TEXT.__text: 0xd1d34
+  __TEXT.__auth_stubs: 0x1610
+  __TEXT.__objc_methlist: 0x3810
   __TEXT.__const: 0x5320
-  __TEXT.__cstring: 0x3634
-  __TEXT.__oslogstring: 0x3ee1
-  __TEXT.__gcc_except_tab: 0x680
+  __TEXT.__cstring: 0x3674
+  __TEXT.__oslogstring: 0x3f73
+  __TEXT.__gcc_except_tab: 0x6a0
   __TEXT.__ustring: 0x4
   __TEXT.__constg_swiftt: 0x7f4
   __TEXT.__swift5_typeref: 0x526

   __TEXT.__swift5_proto: 0x5c
   __TEXT.__swift5_capture: 0xd8
   __TEXT.__swift5_protos: 0x20
-  __TEXT.__unwind_info: 0x1610
+  __TEXT.__unwind_info: 0x1708
   __TEXT.__eh_frame: 0x470
   __TEXT.__objc_classname: 0x8ab
-  __TEXT.__objc_methname: 0x87bf
-  __TEXT.__objc_methtype: 0x1953
-  __TEXT.__objc_stubs: 0x6ce0
+  __TEXT.__objc_methname: 0x87db
+  __TEXT.__objc_methtype: 0x193e
+  __TEXT.__objc_stubs: 0x6d00
   __DATA_CONST.__got: 0x2c0
-  __DATA_CONST.__const: 0xf08
+  __DATA_CONST.__const: 0xf28
   __DATA_CONST.__objc_classlist: 0x278
   __DATA_CONST.__objc_catlist: 0x80
   __DATA_CONST.__objc_protolist: 0x108
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x65b8
-  __DATA_CONST.__objc_selrefs: 0x2318
+  __DATA_CONST.__objc_const: 0x6598
+  __DATA_CONST.__objc_selrefs: 0x2328
   __DATA_CONST.__objc_protorefs: 0x50
   __DATA_CONST.__objc_classrefs: 0x390
   __DATA_CONST.__objc_superrefs: 0x178
   __DATA_CONST.__objc_arraydata: 0x78
-  __AUTH_CONST.__cfstring: 0x2d40
+  __AUTH_CONST.__cfstring: 0x2d80
   __AUTH_CONST.__objc_const: 0xb40
   __AUTH_CONST.__const: 0x5b80
   __AUTH_CONST.__objc_intobj: 0x90
   __AUTH_CONST.__objc_doubleobj: 0xb0
   __AUTH_CONST.__objc_arrayobj: 0x30
-  __AUTH_CONST.__auth_got: 0xb00
+  __AUTH_CONST.__auth_got: 0xb18
   __AUTH.__objc_data: 0x320
   __AUTH.__data: 0xb18
-  __DATA.__objc_ivar: 0x378
-  __DATA.__data: 0xe28
-  __DATA.__bss: 0x7d0
-  __DATA.__common: 0xdc
+  __DATA.__objc_ivar: 0x374
+  __DATA.__data: 0xf48
+  __DATA.__bss: 0x520
+  __DATA.__common: 0xcc
   __DATA_DIRTY.__const: 0x2e0
   __DATA_DIRTY.__objc_const: 0x1330
   __DATA_DIRTY.__objc_data: 0x1370
   __DATA_DIRTY.__data: 0x190
-  __DATA_DIRTY.__bss: 0x350
+  __DATA_DIRTY.__bss: 0x4f0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreLocation.framework/CoreLocation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 01B0CD09-B60A-328C-A41C-18DCEAA0A125
-  Functions: 1686
-  Symbols:   660
-  CStrings:  3200
+  UUID: E064EFE4-7159-3EF3-BFDF-7CE782583AA7
+  Functions: 1685
+  Symbols:   666
+  CStrings:  3216
 
Symbols:
+ __os_signpost_emit_with_name_impl
+ _kAPOriginalContentIdentifier
+ _kAPServerUnfilledReason
+ _kAPSupplementalContext
+ _os_signpost_enabled
+ _os_signpost_id_generate
CStrings:
+ " enableTelemetry=YES "
+ "Attempt to send network request of type %{public}ld."
+ "CacheReadTime"
+ "Clearing all contexts for pool '%@'"
+ "ContextCreate"
+ "ContextInit"
+ "ContextSetup"
+ "FPDI server request type %ld received %ld response code."
+ "Response error %ld for request type %ld: %@"
+ "Signing Authority %p finished creating context"
+ "Signing Authority %p finished handling init response"
+ "Signing Authority %p finished setup response"
+ "Signing Authority %p finished with setup request"
+ "Signing Authority %p received init response"
+ "Signing Authority %p verified context"
+ "SigningAuthority %p state %@ -> %@"
+ "T@\"APClientInfo\",R,N"
+ "TQ,N,V_signpostID"
+ "TotalSetupTime"
+ "VerifyCachedContext"
+ "VerifyNewContext"
+ "_clearStashedContextsIfIndicated"
+ "_signpostID"
+ "clearStashedContexts"
+ "original_content_identifier"
+ "sendRequest:requestType:completionHandler:"
+ "server_unfilled_reason"
+ "setSignpostID:"
+ "signpostID"
+ "supplemental_context"
- "Attempt to send network request of type %{public}ld, at retry %{public}ld"
- "Signing Authority %p finished creating context (%.6f) (%.6f)"
- "Signing Authority %p finished handling init response (%.6f) (%.6f)"
- "Signing Authority %p finished setup response (%.6f) (%.6f)"
- "Signing Authority %p finished with setup request (%.6f) (%.6f)"
- "Signing Authority %p received init response (%.6f) (%.6f)"
- "Signing Authority %p verified context (%.6f) (%.6f)"
- "SigningAuthority %p state %@ -> %@ (%.6f) (%.6f)"
- "T@\"APClientInfo\",&,N"
- "Td,N,V_setupStartTime"
- "_setupStartTime"
- "numRetry"
- "sendRequest:requestType:numRetry:completionHandler:"
- "setSetupStartTime:"
- "setupStartTime"
- "v48@0:8@16q24q32@?40"

```
