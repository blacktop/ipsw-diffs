## LighthouseBitacoraFramework

> `/System/Library/PrivateFrameworks/LighthouseBitacoraFramework.framework/LighthouseBitacoraFramework`

```diff

-2.1.6.0.0
-  __TEXT.__text: 0x3d18c
-  __TEXT.__auth_stubs: 0x9e0
-  __TEXT.__objc_methlist: 0x20ec
-  __TEXT.__const: 0x146a
-  __TEXT.__cstring: 0x284b
-  __TEXT.__oslogstring: 0x1706
-  __TEXT.__gcc_except_tab: 0x64
+2.3.3.0.0
+  __TEXT.__text: 0x3e070
+  __TEXT.__auth_stubs: 0xa10
+  __TEXT.__objc_methlist: 0x2124
+  __TEXT.__const: 0x147a
+  __TEXT.__cstring: 0x298b
+  __TEXT.__oslogstring: 0x18e6
+  __TEXT.__gcc_except_tab: 0x7c
+  __TEXT.__dlopen_cstrs: 0x6e
   __TEXT.__constg_swiftt: 0x5b0
   __TEXT.__swift5_typeref: 0x334
   __TEXT.__swift5_reflstr: 0x40c

   __TEXT.__swift5_assocty: 0x60
   __TEXT.__swift5_proto: 0x120
   __TEXT.__swift5_types: 0x3c
-  __TEXT.__unwind_info: 0x1924
+  __TEXT.__unwind_info: 0x1950
   __TEXT.__eh_frame: 0xd90
-  __TEXT.__objc_classname: 0x3ac
-  __TEXT.__objc_methname: 0x6ab5
-  __TEXT.__objc_methtype: 0x682
-  __TEXT.__objc_stubs: 0x2e00
+  __TEXT.__objc_classname: 0x3ab
+  __TEXT.__objc_methname: 0x6bcb
+  __TEXT.__objc_methtype: 0x69c
+  __TEXT.__objc_stubs: 0x2ec0
   __DATA_CONST.__got: 0x80
-  __DATA_CONST.__const: 0x3e8
+  __DATA_CONST.__const: 0x470
   __DATA_CONST.__objc_classlist: 0x118
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x3b50
-  __DATA_CONST.__objc_selrefs: 0x1260
-  __DATA_CONST.__objc_arraydata: 0xe8
-  __AUTH_CONST.__cfstring: 0x2120
+  __DATA_CONST.__objc_const: 0x3bb0
+  __DATA_CONST.__objc_selrefs: 0x1290
+  __DATA_CONST.__objc_arraydata: 0xa40
+  __AUTH_CONST.__cfstring: 0x22c0
   __AUTH_CONST.__objc_const: 0xa20
   __AUTH_CONST.__objc_intobj: 0x4f8
-  __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH_CONST.__objc_arrayobj: 0x90
-  __AUTH_CONST.__const: 0x360
+  __AUTH_CONST.__objc_dictobj: 0x578
+  __AUTH_CONST.__objc_arrayobj: 0x378
+  __AUTH_CONST.__objc_doubleobj: 0xf0
+  __AUTH_CONST.__const: 0x340
   __AUTH_CONST.__auth_ptr: 0x10
-  __AUTH_CONST.__auth_got: 0x500
+  __AUTH_CONST.__auth_got: 0x518
   __AUTH.__objc_data: 0x188
   __AUTH.__data: 0xa90
-  __DATA.__objc_classrefs: 0x1e0
+  __DATA.__objc_classrefs: 0x1e8
   __DATA.__objc_superrefs: 0xd8
-  __DATA.__objc_ivar: 0x368
+  __DATA.__objc_ivar: 0x370
   __DATA.__data: 0x5d8
+  __DATA.__bss: 0x2410
   __DATA.__common: 0x130
-  __DATA.__bss: 0x2400
   __DATA_DIRTY.__objc_data: 0x9c8
   __DATA_DIRTY.__data: 0x28
   __DATA_DIRTY.__bss: 0x28

   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/InternalSwiftProtobuf.framework/InternalSwiftProtobuf
   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/ProtocolBuffer
+  - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftCore.dylib

   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
-  Functions: 1406
-  Symbols:   344
-  CStrings:  1554
+  Functions: 1427
+  Symbols:   349
+  CStrings:  1592
 
Symbols:
+ _OBJC_CLASS_$_NSConstantDoubleNumber
+ _OBJC_CLASS_$_NSSet
+ __sl_dlopen
+ _objc_getClass
+ _os_variant_has_internal_content
CStrings:
+ "%@ - Test Case #%d - Exp ID: %@ - Dep ID: %@"
+ "@\"NSSet\""
+ "@32@0:8B16@20B28"
+ "Adding %@ to usePrivateUpload."
+ "BucketedType"
+ "CombinationType"
+ "Completed with %ld events."
+ "DeDisco Upload: %@"
+ "Dedisco CA Input Dictionary: %@"
+ "Error During FedStats DPrivacyD data upload. Code: %ld, Domain: %@"
+ "Error During FedStats Stack Success data upload. Code: %ld, Domain: %@"
+ "Error During FedStats Stack Time data upload. Code: %ld, Domain: %@"
+ "Error linking FedStats library."
+ "FedStatsDataEncoder"
+ "NO"
+ "No experiment identifiers in state info."
+ "Stack Success Upload: %@"
+ "Stack Time Upload: %@"
+ "T@\"NSNumber\",R,N,V_usePrivateUpload"
+ "T@\"NSSet\",R,N,V_usePrivateUpload"
+ "Uploaded to Fedstats."
+ "Uploading to Fedstats."
+ "YES"
+ "_usePrivateUpload"
+ "bucketBoundaries"
+ "counts"
+ "dataType"
+ "encodeDataAndRecord:dataTypeContent:baseKey:errorOut:"
+ "fedstats:com.apple.insights.telemetry:dprivacyd:%@:%@:%@"
+ "fedstats:com.apple.insights.telemetry:plugin_success:%@:%@:%@"
+ "fedstats:com.apple.insights.telemetry:plugin_success_time_deltas:%@:%@:%@"
+ "initWithPerformTrialTaskStatus:error:usePrivateUpload:"
+ "initWithTrialIdentifiers:contextID:timestamp:usePrivateUpload:performTaskStatus:performTrialTaskStatus:stop:"
+ "isInternal"
+ "setByAddingObject:"
+ "softlink:o:path:/System/Library/PrivateFrameworks/PrivateFederatedLearning.framework/PrivateFederatedLearning"
+ "structure"
+ "times"
+ "uploadToDedisco"
+ "usePrivateUpload"
- "\x14"
- "%@ - Test Case #%d - Exp ID %@ - Dep ID %@"
- "initWithTrialIdentifiers:contextID:timestamp:performTaskStatus:performTrialTaskStatus:stop:"

```
