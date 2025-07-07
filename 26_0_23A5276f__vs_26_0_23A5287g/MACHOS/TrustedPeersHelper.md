## TrustedPeersHelper

> `/System/Library/Frameworks/Security.framework/XPCServices/TrustedPeersHelper.xpc/TrustedPeersHelper`

```diff

-61901.0.33.0.2
-  __TEXT.__text: 0x2052f8
-  __TEXT.__auth_stubs: 0x2000
+61901.0.46.502.1
+  __TEXT.__text: 0x204814
+  __TEXT.__auth_stubs: 0x1ff0
   __TEXT.__objc_stubs: 0x2500
   __TEXT.__objc_methlist: 0x276c
-  __TEXT.__const: 0xa200
-  __TEXT.__dlopen_cstrs: 0x228
-  __TEXT.__cstring: 0x17b96
-  __TEXT.__objc_methname: 0x7537
+  __TEXT.__const: 0xa1f8
+  __TEXT.__cstring: 0x17b3d
+  __TEXT.__objc_methname: 0x754b
   __TEXT.__oslogstring: 0xa72a
   __TEXT.__swift5_entry: 0x8
   __TEXT.__constg_swiftt: 0x3778
   __TEXT.__swift5_typeref: 0x380e
-  __TEXT.__swift5_fieldmd: 0x2750
-  __TEXT.__swift5_reflstr: 0x22f7
+  __TEXT.__swift5_fieldmd: 0x2768
+  __TEXT.__swift5_reflstr: 0x2317
   __TEXT.__swift5_builtin: 0xb4
   __TEXT.__swift5_assocty: 0x3f0
   __TEXT.__swift5_proto: 0x8c8
   __TEXT.__swift5_types: 0x290
   __TEXT.__objc_classname: 0x42b
-  __TEXT.__objc_methtype: 0x2196
+  __TEXT.__objc_methtype: 0x219c
   __TEXT.__swift5_mpenum: 0x18
-  __TEXT.__swift5_capture: 0x4438
-  __TEXT.__gcc_except_tab: 0x170
+  __TEXT.__swift5_capture: 0x443c
+  __TEXT.__gcc_except_tab: 0x160
+  __TEXT.__dlopen_cstrs: 0x1c2
   __TEXT.__swift5_protos: 0x18
-  __TEXT.__unwind_info: 0x4b98
-  __TEXT.__eh_frame: 0x77a8
-  __DATA_CONST.__auth_got: 0x1010
-  __DATA_CONST.__got: 0x958
+  __TEXT.__unwind_info: 0x4a28
+  __TEXT.__eh_frame: 0x76a8
+  __DATA_CONST.__auth_got: 0x1008
+  __DATA_CONST.__got: 0x960
   __DATA_CONST.__auth_ptr: 0x690
   __DATA_CONST.__const: 0x12900
-  __DATA_CONST.__cfstring: 0x17c0
+  __DATA_CONST.__cfstring: 0x1780
   __DATA_CONST.__objc_classlist: 0x250
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0xe8

   __DATA.__objc_data: 0x2a00
   __DATA.__data: 0x7a80
   __DATA.__objc_stublist: 0x98
-  __DATA.__bss: 0x115a8
+  __DATA.__bss: 0x11598
   __DATA.__common: 0x918
   - /System/Library/Frameworks/CloudKit.framework/CloudKit
   - /System/Library/Frameworks/CoreData.framework/CoreData

   - /System/Library/PrivateFrameworks/FeatureFlags.framework/FeatureFlags
   - /System/Library/PrivateFrameworks/InternalSwiftProtobuf.framework/InternalSwiftProtobuf
   - /System/Library/PrivateFrameworks/KeychainCircle.framework/KeychainCircle
+  - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration
   - /System/Library/PrivateFrameworks/OctagonTrust.framework/OctagonTrust
   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/ProtocolBuffer
   - /System/Library/PrivateFrameworks/SecurityFoundation.framework/SecurityFoundation

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 7AC2778A-965D-3B26-96DE-8CA8EFCD4B1F
+  UUID: B0FCFCB8-529D-3330-AB23-9F64130BCA98
   Functions: 8134
   Symbols:   525
-  CStrings:  3435
+  CStrings:  3428
 
Symbols:
+ _OBJC_CLASS_$_MCProfileConnection
- _objc_getClass
CStrings:
+ "SEPBasedICSCHealingEnabled"
+ "escrowCheck(passcodeGeneration:requiresEscrowCheck:knownFederations:isBackgroundCheck:flowID:deviceSessionID:reply:)"
+ "requestEscrowCheckWithSpecificUser:requiresEscrowCheck:passcodeGeneration:knownFederations:isBackgroundCheck:flowID:deviceSessionID:reply:"
+ "v72@0:8@\"TPSpecificUser\"16B24Q28@\"NSArray\"36B44@\"NSString\"48@\"NSString\"56@?<v@?@\"OTEscrowCheckCallResult\"@\"NSError\">64"
+ "v72@0:8@16B24Q28@36B44@48@56@?64"
- "Class getMCProfileConnectionClass(void)_block_invoke"
- "MCProfileConnection"
- "OTManagedConfigurationAdapter.m"
- "Unable to find class %s"
- "escrowCheck(passcodeGeneration:knownFederations:isBackgroundCheck:flowID:deviceSessionID:reply:)"
- "requestEscrowCheckWithSpecificUser:passcodeGeneration:knownFederations:isBackgroundCheck:flowID:deviceSessionID:reply:"
- "softlink:r:path:/System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration"
- "v68@0:8@\"TPSpecificUser\"16Q24@\"NSArray\"32B40@\"NSString\"44@\"NSString\"52@?<v@?@\"OTEscrowCheckCallResult\"@\"NSError\">60"
- "v68@0:8@16Q24@32B40@44@52@?60"
- "void *ManagedConfigurationLibrary(void)"

```
