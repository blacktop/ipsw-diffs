## IDSFoundation

> `/System/Library/PrivateFrameworks/IDSFoundation.framework/Versions/A/IDSFoundation`

```diff

-2000.100.2.1.1
-  __TEXT.__text: 0x4f008c
-  __TEXT.__objc_methlist: 0x1ab0c
-  __TEXT.__const: 0x3f6d0
-  __TEXT.__oslogstring: 0x28b1a
-  __TEXT.__cstring: 0x32f2d
-  __TEXT.__gcc_except_tab: 0xb1d0
+2003.100.1.0.0
+  __TEXT.__text: 0x4f1f90
+  __TEXT.__objc_methlist: 0x1ac44
+  __TEXT.__const: 0x3f740
+  __TEXT.__oslogstring: 0x28c9a
+  __TEXT.__cstring: 0x331fd
+  __TEXT.__gcc_except_tab: 0xb220
   __TEXT.__dlopen_cstrs: 0xac
-  __TEXT.__ustring: 0xc
-  __TEXT.__swift5_typeref: 0xb67e
-  __TEXT.__constg_swiftt: 0xc798
-  __TEXT.__swift5_reflstr: 0x6b36
-  __TEXT.__swift5_fieldmd: 0xb674
-  __TEXT.__swift5_builtin: 0x384
+  __TEXT.__ustring: 0x188
+  __TEXT.__swift5_typeref: 0xb6b4
+  __TEXT.__constg_swiftt: 0xc85c
+  __TEXT.__swift5_reflstr: 0x6b56
+  __TEXT.__swift5_fieldmd: 0xb6b4
+  __TEXT.__swift5_builtin: 0x398
   __TEXT.__swift5_assocty: 0x958
   __TEXT.__swift5_proto: 0x33dc
-  __TEXT.__swift5_types: 0xea8
+  __TEXT.__swift5_types: 0xeb0
   __TEXT.__swift5_capture: 0x15a4
   __TEXT.__swift_as_entry: 0x3ac
   __TEXT.__swift_as_ret: 0x330

   __TEXT.__swift5_acfuncs: 0x1cc
   __TEXT.__swift5_mpenum: 0x164
   __TEXT.__swift5_types2: 0x20
-  __TEXT.__unwind_info: 0x13fb8
+  __TEXT.__unwind_info: 0x14018
   __TEXT.__eh_frame: 0x165f4
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x5500
-  __DATA_CONST.__objc_classlist: 0x1288
+  __DATA_CONST.__const: 0x5558
+  __DATA_CONST.__objc_classlist: 0x1290
   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0x1f0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xa730
+  __DATA_CONST.__objc_selrefs: 0xa7b0
   __DATA_CONST.__objc_protorefs: 0xb0
   __DATA_CONST.__objc_superrefs: 0xaf8
   __DATA_CONST.__objc_arraydata: 0x1558
   __DATA_CONST.__got: 0x13e8
-  __AUTH_CONST.__const: 0x1bf20
-  __AUTH_CONST.__cfstring: 0x2b880
-  __AUTH_CONST.__objc_const: 0x3d188
+  __AUTH_CONST.__const: 0x1bf40
+  __AUTH_CONST.__cfstring: 0x2ba80
+  __AUTH_CONST.__objc_const: 0x3d3f0
   __AUTH_CONST.__objc_intobj: 0xba0
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__objc_arrayobj: 0x1e90
   __AUTH_CONST.__auth_got: 0x26d8
-  __AUTH.__objc_data: 0xa1d8
-  __AUTH.__data: 0xaa10
-  __DATA.__objc_ivar: 0x27ac
-  __DATA.__data: 0xed60
+  __AUTH.__objc_data: 0xa318
+  __AUTH.__data: 0xaa40
+  __DATA.__objc_ivar: 0x27c4
+  __DATA.__data: 0xedb0
   __DATA.__crash_info: 0x148
-  __DATA.__bss: 0x66080
+  __DATA.__bss: 0x66070
   __DATA.__common: 0x180
   __DATA_DIRTY.__objc_data: 0x1400
   __DATA_DIRTY.__data: 0x728

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 31403
-  Symbols:   4931
-  CStrings:  8051
+  Functions: 31461
+  Symbols:   4936
+  CStrings:  8070
 
Symbols:
+ _IDSMessageContextLocalTraceIdentifierKey
+ _IDSMessageTraceIDKey
+ _IDSRegistrationPropertySupportsDedicatedChannelBaseFilterOverrideOpportunistic
+ _OBJC_CLASS_$_IDSDeregistrationDailyMetric
+ _OBJC_METACLASS_$_IDSDeregistrationDailyMetric
CStrings:
+ "%@ (idx %u)"
+ "(none)"
+ "(unnamed)"
+ "<%@: %p verifierResult: %@, ticket: %@, accountKey: %@, queryResponseTime: %@, verificationDate: %@>, ktOptInStatus: %@"
+ "DatagramChannelHBHSecretLogging"
+ "GL getInterfaceFamily"
+ "HBH secret logging: sessionID = %@, participantID = %llu, relaySessionKey = %@, salt = %@, hbhEncKey = %@, hbhDecKey = %@"
+ "IDSFoundation.IDSDeregistrationDailyMetric"
+ "IDSMessageContextLocalTraceIdentifierKey"
+ "IDSMessageTraceID"
+ "IDSSendParametersTraceID"
+ "Remote App Intents"
+ "VerificationDate"
+ "_postProcessQUICAllocbindResponse: HBH keys already derived (in deriveAES128CTRKeys); keeping them for %@."
+ "_supportsDedicatedChannelBaseFilterOverrideOpportunistic"
+ "com.apple.private.alloy.remoteappintents"
+ "deriveAES128CTRKeys: IDSLinkHBHDeriveHKDFSha256Keys failed."
+ "filter out utun interface [if:%s family:%u subfamily:%u type:%d], useDefaultInterfaceOnly:%@"
+ "supports-dedicated-channel-base-filter-override-opportunistic"
+ "── %@ (idx %u) %@ ──\n  addr:      %@\n  netmask:   %@\n  external:  %@\n  delegated: %@\n  flags:     AWDL:%@ Cellular:%@ Temp:%@ CompanionLink:%@ Wired:%@ Expensive:%@ Constrained:%@ clat46:%@"
- "<%@: %p verifierResult: %@, ticket: %@, accountKey: %@, queryResponseTime: %@>, ktOptInStatus: %@"
```
