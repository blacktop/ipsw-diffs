## amfid

> `/usr/libexec/amfid`

```diff

-938.120.13.0.0
-  __TEXT.__text: 0x19600
-  __TEXT.__auth_stubs: 0x14c0
-  __TEXT.__objc_stubs: 0xcc0
+1045.0.1.0.1
+  __TEXT.__text: 0x19874
+  __TEXT.__auth_stubs: 0x1440
+  __TEXT.__objc_stubs: 0xd00
   __TEXT.__init_offsets: 0x8
   __TEXT.__objc_methlist: 0x35c
-  __TEXT.__const: 0xb2f
-  __TEXT.__gcc_except_tab: 0x4fc
-  __TEXT.__oslogstring: 0x15b2
-  __TEXT.__cstring: 0x1773
+  __TEXT.__const: 0xb4f
+  __TEXT.__gcc_except_tab: 0x460
+  __TEXT.__oslogstring: 0x15d2
+  __TEXT.__cstring: 0x1743
   __TEXT.__objc_classname: 0x57
-  __TEXT.__objc_methname: 0xbb2
+  __TEXT.__objc_methname: 0xbf9
   __TEXT.__objc_methtype: 0x2fd
-  __TEXT.__swift5_typeref: 0x461
+  __TEXT.__swift5_typeref: 0x49b
   __TEXT.__swift5_reflstr: 0x175
-  __TEXT.__swift5_assocty: 0x48
-  __TEXT.__constg_swiftt: 0x284
+  __TEXT.__swift5_assocty: 0x60
+  __TEXT.__constg_swiftt: 0x28c
   __TEXT.__swift5_fieldmd: 0x1b0
   __TEXT.__swift5_proto: 0x3c
   __TEXT.__swift5_types: 0x18
   __TEXT.__swift5_capture: 0x1c
-  __TEXT.__unwind_info: 0x738
+  __TEXT.__unwind_info: 0x718
   __TEXT.__eh_frame: 0x3d0
-  __DATA_CONST.__auth_got: 0xa78
-  __DATA_CONST.__got: 0x370
-  __DATA_CONST.__auth_ptr: 0x1d8
-  __DATA_CONST.__const: 0xa88
+  __DATA_CONST.__auth_got: 0xa38
+  __DATA_CONST.__got: 0x390
+  __DATA_CONST.__auth_ptr: 0x1e8
+  __DATA_CONST.__const: 0xa68
   __DATA_CONST.__cfstring: 0x5a0
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_protolist: 0x18

   __DATA_CONST.__objc_dictobj: 0x168
   __DATA_CONST.__objc_intobj: 0x30
   __DATA.__objc_const: 0x5e0
-  __DATA.__objc_selrefs: 0x450
+  __DATA.__objc_selrefs: 0x460
   __DATA.__objc_ivar: 0x8
   __DATA.__objc_data: 0x220
-  __DATA.__data: 0x630
+  __DATA.__data: 0x640
   __DATA.__common: 0xc8
   __DATA.__bss: 0x828
   __RESTRICT.__restrict: 0x0

   - /System/Library/Frameworks/LocalAuthentication.framework/LocalAuthentication
   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/Frameworks/SwiftData.framework/SwiftData
+  - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/Frameworks/UserNotifications.framework/UserNotifications
   - /System/Library/PrivateFrameworks/AppleMobileFileIntegrity.framework/AppleMobileFileIntegrity
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics

   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
   - /System/Library/PrivateFrameworks/SetupAssistant.framework/SetupAssistant
   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
-  - /System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore
   - /usr/lib/libCoreEntitlements.dylib
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib

   - /usr/lib/swift/libswiftObservation.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  - /usr/lib/swift/libswift_errno.dylib
-  - /usr/lib/swift/libswift_math.dylib
-  - /usr/lib/swift/libswift_signal.dylib
-  - /usr/lib/swift/libswift_stdio.dylib
-  - /usr/lib/swift/libswift_time.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
-  - /usr/lib/swift/libswiftsys_time.dylib
-  - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 63DFD63B-77E1-3989-B7EE-5EBCBFFA0868
-  Functions: 526
-  Symbols:   533
+  UUID: F1CBC95E-6E04-3A40-8F3B-815D2C96F421
+  Functions: 523
+  Symbols:   528
   CStrings:  586
 
Symbols:
+ _$s4Root9SwiftData15PersistentModelPTl
+ _$s9SwiftData15PersistentModelP4RootAC_AaBTn
+ _$ss11_StringGutsV16_foreignCopyUTF84intoSiSgSrys5UInt8VG_tF
+ _$ss20__StaticArrayStorageCN
+ _OBJC_CLASS_$_MISAgentClient
+ _OBJC_CLASS_$_MISProfileDBClient
+ _OBJC_CLASS_$_NSSet
+ __swiftImmortalRefCount
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3
+ _swift_coroFrameAlloc
+ _swift_setDeallocating
- _$ss11_StringGutsV8copyUTF84intoSiSgSrys5UInt8VG_tF
- _MISEnumerateInstalledProvisioningProfiles
- _MISProvisioningProfileGetDeveloperCertificates
- _MISProvisioningProfileGetUUID
- _MISRemoveProfileTrust
- _SecCertificateCopySubjectSummary
- _SecCertificateCreateWithData
- __Znwm
- __swift_FORCE_LOAD_$_swift_errno
- __swift_FORCE_LOAD_$_swift_math
- __swift_FORCE_LOAD_$_swift_signal
- __swift_FORCE_LOAD_$_swift_stdio
- __swift_FORCE_LOAD_$_swift_time
- __swift_FORCE_LOAD_$_swiftsys_time
- __swift_FORCE_LOAD_$_swiftunistd
- _objc_enumerationMutation
- _swift_bridgeObjectRelease_n
- _swift_bridgeObjectRetain_n
CStrings:
+ "%s: adding identities %@ to trustedAppSigners"
+ "-[AMFIService removeTrustforTeamID:withReply:]"
+ "-[AMFIService setTrustForTeamID:withSignature:withSignType:withReply:]"
+ "[%s] attempting to remove trust for team ID: %@"
+ "[%s] attempting to set trust for team ID: %@"
+ "[%s] failed to trust team ID %@ with signature %@: %@"
+ "[%s] failed to untrust team ID %@: %@"
+ "[%s] team ID must be provided"
+ "__trustSigningIdentities"
+ "addTrustedCodeSigningIdentities:"
+ "isSubsetOfSet:"
+ "removeTrustforTeamID:withReply:"
+ "setTrustForTeamID:withSignature:withSignType:withReply:"
+ "setWithArray:"
+ "signingIdentitiesWithProfileUUID:"
+ "signingIdentitiesWithTeamID:"
+ "trustTeamID:signature:error:"
+ "untrustTeamID:error:"
- "%s: adding identity %@ to trustedAppSigners"
- "%s: adding profile %@ to trustedAppSigners"
- "%s: unable to find %@"
- "%s: unable to iterate and select %@"
- "-[AMFIService removeTrustforUuid:withReply:]"
- "-[AMFIService setTrustForUuid:withSignature:withSignType:withReply:]"
- "B16@?0^v8"
- "[%s] attempting to remove trust for UUID: %@"
- "[%s] attempting to set trust for UUID: %@"
- "__trustProfileIdentity"
- "__trustProfileIdentity_block_invoke"
- "addObject:"
- "compare:"
- "countByEnumeratingWithState:objects:count:"
- "mutableCopy"
- "removeTrustforUuid:withReply:"
- "setTrustForUuid:withSignature:withSignType:withReply:"
- "setTrustedCodeSigningIdentities:"

```
