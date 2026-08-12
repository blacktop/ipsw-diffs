## IDSFoundation

> `/System/Library/PrivateFrameworks/IDSFoundation.framework/IDSFoundation`

```diff

-2000.100.2.2.1
-  __TEXT.__text: 0x4ebbf4
-  __TEXT.__objc_methlist: 0x1ba8c
-  __TEXT.__const: 0x3f720
-  __TEXT.__cstring: 0x3499d
-  __TEXT.__oslogstring: 0x2b92a
-  __TEXT.__gcc_except_tab: 0xbb14
+2003.100.1.0.0
+  __TEXT.__text: 0x4ed8f4
+  __TEXT.__objc_methlist: 0x1bbc4
+  __TEXT.__const: 0x3f790
+  __TEXT.__cstring: 0x34c6d
+  __TEXT.__oslogstring: 0x2ba9a
+  __TEXT.__gcc_except_tab: 0xbb58
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
-  __TEXT.__unwind_info: 0x14360
+  __TEXT.__unwind_info: 0x143c8
   __TEXT.__eh_frame: 0x164a4
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x75c8
-  __DATA_CONST.__objc_classlist: 0x12b0
+  __DATA_CONST.__const: 0x7620
+  __DATA_CONST.__objc_classlist: 0x12b8
   __DATA_CONST.__objc_catlist: 0x68
   __DATA_CONST.__objc_protolist: 0x250
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xb0a0
+  __DATA_CONST.__objc_selrefs: 0xb120
   __DATA_CONST.__objc_protorefs: 0xb0
   __DATA_CONST.__objc_superrefs: 0xb30
   __DATA_CONST.__objc_arraydata: 0x1558
   __DATA_CONST.__got: 0x1500
-  __AUTH_CONST.__const: 0x1a0a0
-  __AUTH_CONST.__cfstring: 0x2cb80
-  __AUTH_CONST.__objc_const: 0x3ea40
+  __AUTH_CONST.__const: 0x1a0c0
+  __AUTH_CONST.__cfstring: 0x2cd80
+  __AUTH_CONST.__objc_const: 0x3eca8
   __AUTH_CONST.__objc_intobj: 0xc30
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__objc_arrayobj: 0x1e90
   __AUTH_CONST.__auth_got: 0x2a28
-  __AUTH.__objc_data: 0xa598
-  __AUTH.__data: 0xb0a8
-  __DATA.__objc_ivar: 0x28a0
-  __DATA.__data: 0xf258
+  __AUTH.__objc_data: 0xa6d8
+  __AUTH.__data: 0xb0d8
+  __DATA.__objc_ivar: 0x28b8
+  __DATA.__data: 0xf2e8
   __DATA.__crash_info: 0x148
   __DATA.__bss: 0x66270
   __DATA.__common: 0x1b0

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 31643
-  Symbols:   5088
-  CStrings:  8370
+  Functions: 31703
+  Symbols:   5093
+  CStrings:  8389
 
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
