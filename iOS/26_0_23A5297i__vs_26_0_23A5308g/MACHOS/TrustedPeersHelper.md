## TrustedPeersHelper

> `/System/Library/Frameworks/Security.framework/XPCServices/TrustedPeersHelper.xpc/TrustedPeersHelper`

```diff

-61901.0.56.0.1
-  __TEXT.__text: 0x204814
+61901.0.84.0.0
+  __TEXT.__text: 0x204a9c
   __TEXT.__auth_stubs: 0x1ff0
   __TEXT.__objc_stubs: 0x2500
   __TEXT.__objc_methlist: 0x276c
-  __TEXT.__const: 0xa1f8
-  __TEXT.__cstring: 0x17b3d
-  __TEXT.__objc_methname: 0x754b
-  __TEXT.__oslogstring: 0xa72a
+  __TEXT.__const: 0xa1e0
+  __TEXT.__cstring: 0x17b7d
+  __TEXT.__objc_methname: 0x7557
+  __TEXT.__oslogstring: 0xa7aa
   __TEXT.__swift5_entry: 0x8
   __TEXT.__constg_swiftt: 0x3778
   __TEXT.__swift5_typeref: 0x380e
-  __TEXT.__swift5_fieldmd: 0x2768
-  __TEXT.__swift5_reflstr: 0x2317
+  __TEXT.__swift5_fieldmd: 0x2780
+  __TEXT.__swift5_reflstr: 0x2337
   __TEXT.__swift5_builtin: 0xb4
   __TEXT.__swift5_assocty: 0x3f0
   __TEXT.__swift5_proto: 0x8c8

   __TEXT.__unwind_info: 0x4a28
   __TEXT.__eh_frame: 0x76a8
   __DATA_CONST.__auth_got: 0x1008
-  __DATA_CONST.__got: 0x960
+  __DATA_CONST.__got: 0x938
   __DATA_CONST.__auth_ptr: 0x690
   __DATA_CONST.__const: 0x128c0
   __DATA_CONST.__cfstring: 0x1780

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x60
   __DATA_CONST.__objc_superrefs: 0xe8
-  __DATA.__objc_const: 0x68e0
-  __DATA.__objc_selrefs: 0x1cc0
+  __DATA.__objc_const: 0x6900
+  __DATA.__objc_selrefs: 0x1cc8
   __DATA.__objc_ivar: 0x1e8
   __DATA.__objc_data: 0x2a00
   __DATA.__data: 0x7a80

   - /System/Library/PrivateFrameworks/InternalSwiftProtobuf.framework/InternalSwiftProtobuf
   - /System/Library/PrivateFrameworks/KeychainCircle.framework/KeychainCircle
   - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration
+  - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
   - /System/Library/PrivateFrameworks/OctagonTrust.framework/OctagonTrust
   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/ProtocolBuffer
   - /System/Library/PrivateFrameworks/SecurityFoundation.framework/SecurityFoundation

   - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 625B0A14-5BEA-3D88-83AF-4E8CDCA23C04
+  UUID: 9547AA65-A15A-366F-8018-9D0F75296675
   Functions: 8134
-  Symbols:   517
-  CStrings:  3428
+  Symbols:   512
+  CStrings:  3435
 
Symbols:
+ _kSecurityRTCFieldIsCurrentDevice
- _kSecurityRTCFieldEgoMachineIDEvictedFromTDL
- _kSecurityRTCFieldEgoMachineIDGhosted
- _kSecurityRTCFieldEgoMachineIDUnknown
- _kSecurityRTCFieldEgoMachineIDUnknownRemovalReasonFromTDL
- _kSecurityRTCFieldEgoMachineIDUserInitiatedRemovalFromTDL
- _kSecurityRTCFieldEgoMachineIDVanishedFromTDL
CStrings:
+ "?"
+ "EscrowCheckMigration"
+ "Mismatch between configured CKContainer (accountID %{public}s and requested user (appleAccountID:%{public}s, altDSID:%{public}s"
+ "Mismatch between existing container and account, remaking container for %{public}@"
+ "accountID"
+ "initWithAccountID:"
+ "user"
- "Mismatch between configured CKContainer (altDSID %{public}s and requested user %{public}s"
- "initWithAltDSID:"

```
