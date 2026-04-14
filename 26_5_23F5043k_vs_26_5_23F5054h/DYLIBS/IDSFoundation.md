## IDSFoundation

> `/System/Library/PrivateFrameworks/IDSFoundation.framework/IDSFoundation`

```diff

-1969.600.2.0.0
-  __TEXT.__text: 0x4f80b8
-  __TEXT.__auth_stubs: 0x5060
-  __TEXT.__objc_methlist: 0x1b00c
-  __TEXT.__const: 0x3bb60
-  __TEXT.__oslogstring: 0x28509
-  __TEXT.__cstring: 0x32fd1
-  __TEXT.__gcc_except_tab: 0xc4ac
+1969.600.31.0.0
+  __TEXT.__text: 0x501bf4
+  __TEXT.__auth_stubs: 0x5080
+  __TEXT.__objc_methlist: 0x1b0d4
+  __TEXT.__const: 0x3bea0
+  __TEXT.__oslogstring: 0x28829
+  __TEXT.__cstring: 0x33081
+  __TEXT.__gcc_except_tab: 0xc4ec
   __TEXT.__ustring: 0xc
   __TEXT.__dlopen_cstrs: 0xac
-  __TEXT.__swift5_typeref: 0xa925
-  __TEXT.__swift5_fieldmd: 0xac18
-  __TEXT.__constg_swiftt: 0xa83c
+  __TEXT.__swift5_typeref: 0xaceb
+  __TEXT.__swift5_fieldmd: 0xace8
+  __TEXT.__constg_swiftt: 0xa8ec
   __TEXT.__swift5_builtin: 0x35c
-  __TEXT.__swift5_reflstr: 0x65b0
+  __TEXT.__swift5_reflstr: 0x6610
   __TEXT.__swift5_assocty: 0x860
   __TEXT.__swift5_protos: 0x90
-  __TEXT.__swift5_proto: 0x30b0
-  __TEXT.__swift5_types: 0xda4
-  __TEXT.__swift5_capture: 0x11e0
+  __TEXT.__swift5_proto: 0x30c0
+  __TEXT.__swift5_types: 0xdb4
+  __TEXT.__swift5_capture: 0x1260
   __TEXT.__swift_as_entry: 0x364
   __TEXT.__swift_as_ret: 0x2f4
   __TEXT.__swift5_mpenum: 0x148
-  __TEXT.__swift5_acfuncs: 0x17c
   __TEXT.__swift5_types2: 0x24
-  __TEXT.__unwind_info: 0x140e8
-  __TEXT.__eh_frame: 0x15988
-  __TEXT.__objc_classname: 0x52b7
-  __TEXT.__objc_methname: 0x38c77
+  __TEXT.__swift5_acfuncs: 0x17c
+  __TEXT.__unwind_info: 0x142a0
+  __TEXT.__eh_frame: 0x15a8c
+  __TEXT.__objc_classname: 0x5327
+  __TEXT.__objc_methname: 0x38dc7
   __TEXT.__objc_methtype: 0x84ac
-  __TEXT.__objc_stubs: 0x1b920
+  __TEXT.__objc_stubs: 0x1ba40
   __DATA_CONST.__got: 0x1500
-  __DATA_CONST.__const: 0x7340
-  __DATA_CONST.__objc_classlist: 0x1250
+  __DATA_CONST.__const: 0x7350
+  __DATA_CONST.__objc_classlist: 0x1260
   __DATA_CONST.__objc_catlist: 0x68
   __DATA_CONST.__objc_protolist: 0x210
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xabf0
+  __DATA_CONST.__objc_selrefs: 0xac38
   __DATA_CONST.__objc_protorefs: 0x80
   __DATA_CONST.__objc_superrefs: 0xaf8
   __DATA_CONST.__objc_arraydata: 0x1530
-  __AUTH_CONST.__auth_got: 0x2840
-  __AUTH_CONST.__const: 0x17e20
-  __AUTH_CONST.__cfstring: 0x2b680
-  __AUTH_CONST.__objc_const: 0x3d1d0
+  __AUTH_CONST.__auth_got: 0x2850
+  __AUTH_CONST.__const: 0x180c0
+  __AUTH_CONST.__cfstring: 0x2b800
+  __AUTH_CONST.__objc_const: 0x3d430
   __AUTH_CONST.__objc_intobj: 0xbd0
   __AUTH_CONST.__objc_arrayobj: 0x1e90
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH.__objc_data: 0x9ed0
-  __AUTH.__data: 0xad38
+  __AUTH.__data: 0xaeb0
   __DATA.__objc_ivar: 0x27d4
-  __DATA.__data: 0xe0f8
+  __DATA.__data: 0xe228
   __DATA.__crash_info: 0x148
   __DATA.__bss: 0x5fe10
   __DATA.__common: 0x1d0

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: DD05401C-9093-38E2-AC48-8EBD1204A6CC
-  Functions: 30299
-  Symbols:   4966
-  CStrings:  25701
+  UUID: CBD5E89C-870D-3753-A8AB-1340F775548E
+  Functions: 30431
+  Symbols:   4968
+  CStrings:  25755
 
Symbols:
+ _GLUtilInterfaceTypeStringFromRAT
+ _GLUtilLinkProtocolMetricStringFromAWDType
CStrings:
+ "%s: %s -> connecting (retry plugin)"
+ "%s: healthy retry (was connected for %s, threshold: %s)"
+ "%s: initialized with protocol delays: %s"
+ "%s: inserting %s delay before first link containing %s (on %s)"
+ "%s: registering with ConnectFirstController %s"
+ "%s: skipping ConnectFirstController %s (missing required tag)"
+ "Healthy Link Retry"
+ "Healthy retry: enabled=%{bool}d (defaults: %s, experiments: %s), duration=%lds (defaults: %s, experiments: %s), active=%{bool}d"
+ "IDSGLLinkEngine: TwoWay per-protocol fallback delays: %s"
+ "IDSGLLinkEngine: experiment override for fallback delay before %s: %lds"
+ "IDSGLLinkEngine: ignoring experiment %s: value %ld outside valid range 1-10"
+ "IDSGLLinkEngine: ignoring experiment %s: value is not an integer"
+ "_TtC13IDSFoundation22HealthyLinkRetryPlugin"
+ "_TtC13IDSFoundation28IDSTwoWayFallbackDelayPlugin"
+ "_buildQrExperiments: qr experiments: %@"
+ "_reportLinkFailureMetricForCandidatePair:"
+ "cell"
+ "cl-%@-%@"
+ "discard"
+ "fail-%@-%@"
+ "fallbackDelaysHook"
+ "globalLinkSessionTypeShared"
+ "globalLinkSessionTypeTwoway"
+ "idsQRHealthyRetryDuration"
+ "idsQRHealthyRetryEnabled"
+ "internal"
+ "linkConnectedOnInterfaceType:usingProtocol:"
+ "linkFailedOnInterfaceType:usingProtocol:"
+ "linkRetryOnInterfaceType:usingProtocol:"
+ "minimumConnectedDuration"
+ "protocolDelays"
+ "quic"
+ "retry-%@-%@"
+ "setIsInternalServer:"
+ "setIsTwoWay:"
+ "shared"
+ "shouldRetryHook"
+ "tls"
+ "twoway"
+ "wifi"

```
