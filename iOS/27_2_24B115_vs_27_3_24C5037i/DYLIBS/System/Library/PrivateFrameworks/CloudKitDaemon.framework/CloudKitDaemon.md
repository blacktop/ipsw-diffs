## CloudKitDaemon

> `/System/Library/PrivateFrameworks/CloudKitDaemon.framework/CloudKitDaemon`

```diff

-2720.17.6.0.0
-  __TEXT.__text: 0x3db844
-  __TEXT.__objc_methlist: 0x3186c
+2730.18.0.0.0
+  __TEXT.__text: 0x3e0da8
+  __TEXT.__objc_methlist: 0x31bb4
   __TEXT.__const: 0x4e10
   __TEXT.__swift5_typeref: 0x21a1
-  __TEXT.__oslogstring: 0x332aa
+  __TEXT.__oslogstring: 0x33abc
   __TEXT.__swift5_capture: 0x918
   __TEXT.__constg_swiftt: 0x1ac0
   __TEXT.__swift5_reflstr: 0x1136

   __TEXT.__swift_as_ret: 0x16c
   __TEXT.__swift_as_cont: 0x23c
   __TEXT.__swift5_protos: 0x38
-  __TEXT.__cstring: 0x2b413
+  __TEXT.__cstring: 0x2bbc2
   __TEXT.__swift5_mpenum: 0x1c
-  __TEXT.__gcc_except_tab: 0xca44
+  __TEXT.__gcc_except_tab: 0xcb84
   __TEXT.__ustring: 0x2c
-  __TEXT.__unwind_info: 0xed38
+  __TEXT.__unwind_info: 0xee70
   __TEXT.__eh_frame: 0x3ba8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x9ab8
-  __DATA_CONST.__objc_classlist: 0x14f0
+  __DATA_CONST.__const: 0x9b58
+  __DATA_CONST.__objc_classlist: 0x1518
   __DATA_CONST.__objc_catlist: 0x148
   __DATA_CONST.__objc_protolist: 0x220
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x131b0
+  __DATA_CONST.__objc_selrefs: 0x132c8
   __DATA_CONST.__objc_protorefs: 0xa0
-  __DATA_CONST.__objc_superrefs: 0x13c8
+  __DATA_CONST.__objc_superrefs: 0x13e0
   __DATA_CONST.__objc_arraydata: 0x1558
-  __DATA_CONST.__got: 0x2090
+  __DATA_CONST.__got: 0x20c0
   __AUTH_CONST.__const: 0x5388
-  __AUTH_CONST.__cfstring: 0x23a60
-  __AUTH_CONST.__objc_const: 0x4af20
-  __AUTH_CONST.__objc_intobj: 0xcd8
+  __AUTH_CONST.__cfstring: 0x23f40
+  __AUTH_CONST.__objc_const: 0x4b470
+  __AUTH_CONST.__objc_intobj: 0xcf0
   __AUTH_CONST.__objc_arrayobj: 0x390
   __AUTH_CONST.__objc_dictobj: 0xbe0
-  __AUTH_CONST.__auth_got: 0x2310
-  __AUTH.__objc_data: 0x5258
+  __AUTH_CONST.__auth_got: 0x2328
+  __AUTH.__objc_data: 0x53e8
   __AUTH.__data: 0x5b0
-  __DATA.__objc_ivar: 0x1a94
+  __DATA.__objc_ivar: 0x1a9c
   __DATA.__data: 0x1ee0
   __DATA.__common: 0xa0
-  __DATA_DIRTY.__objc_ivar: 0x1984
+  __DATA_DIRTY.__objc_ivar: 0x19ac
   __DATA_DIRTY.__objc_data: 0x8580
   __DATA_DIRTY.__data: 0x2288
   __DATA_DIRTY.__bss: 0x3900

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 21004
-  Symbols:   3030
-  CStrings:  8534
+  Functions: 21084
+  Symbols:   3043
+  CStrings:  8608
 
Symbols:
+ _CKTestDeviceOptionSelfAddedPCSV2Upgrade
+ _OBJC_CLASS_$_CKDFetchScreeningKeyOperation
+ _OBJC_CLASS_$_CKDFetchScreeningKeyOperationInfo
+ _OBJC_CLASS_$_CKDScreeningEligibilityEvaluator
+ _OBJC_CLASS_$_CKDSelfAddedPCSUpgrader
+ _OBJC_METACLASS_$_CKDFetchScreeningKeyOperation
+ _OBJC_METACLASS_$_CKDFetchScreeningKeyOperationInfo
+ _OBJC_METACLASS_$_CKDScreeningEligibilityEvaluator
+ _OBJC_METACLASS_$_CKDSelfAddedPCSUpgrader
+ _SecKeyCopyExternalRepresentation
+ _SecKeyCopyPublicKey
+ _SecKeyCreateRandomKey
+ _kSecAttrKeySizeInBits
CStrings:
+ "Adding screening identity to selfAddedPCS for share %@"
+ "CKDFetchScreeningKeyURLRequest.m"
+ "Can't upgrade a share PCS that is not read-write"
+ "Cannot verify screening key: containerScopedUserID unavailable for share %@"
+ "Couldn't copy a private key into the v2 share PCS"
+ "Couldn't copy a sharee into the v2 share PCS"
+ "Couldn't create a v2 share PCS"
+ "Couldn't set the current private key of the v2 share PCS"
+ "Couldn't strip screening identity from public PCS for share at URL %@: %@"
+ "Couldn't upgrade selfAddedPCS to v2 for share %@; saving with the existing selfAddedPCS: %@"
+ "Couldn't upgrade share PCS to v2: %@"
+ "Error fetching screening key for share %@"
+ "Error fetching signing certificates for screening key: %@"
+ "Error upgrading selfAddedPCS %@ to v2: %@"
+ "Failed to add screening identity to selfAddedPCS for share %@"
+ "Failed to create screening PCS identity for share %@"
+ "Failed to create test screening PCS identity for share %@"
+ "Failed to generate test screening key for share %@: %@"
+ "Failed to parse screening key signature envelope for share %@"
+ "Failed to remove stale screening identity from selfAddedPCS for share %@: %@"
+ "Failed to resolve server environment for screening key certificate fetch: %@"
+ "Failed to serialize publicProtectionData for share %@ under test hook: %@"
+ "Fetch screening key request failed: %@"
+ "Fetching Screening Key"
+ "Fetching Signing Certificates"
+ "Forced screening key fetch error for share %@"
+ "Forced selfAddedPCS upgrade failure for testing"
+ "Missing shareRecordID for screening key fetch"
+ "New share %@ is eligible for screening"
+ "No share PCS to upgrade to v2"
+ "No valid signing certificates available to verify screening key for share %@"
+ "No valid signing certificates found for screening key verification"
+ "Public PCS doesn't contain screening key after add attempt for share %@"
+ "Removed stale screening identity from selfAddedPCS for share %@; share is no longer eligible for screening"
+ "ReportSharePCSPrepFailure"
+ "Saving participant is not the share owner for share %@"
+ "Saving participant may not modify the PCS chain for share %@"
+ "Screening identity already present in selfAddedPCS for share %@; skipping fetch and add"
+ "Screening key response is missing required publicKey or signature for share %@"
+ "Screening key signature is not trusted: no pinned certificate verified the signature for share %@"
+ "Screening public key length %lu does not match reported key type %ld (expected %lu bytes) for share %@"
+ "Server rejected the screening key request for share %@; saving without adding screening key to the share: %@"
+ "Share %@ is being made public and is eligible for screening"
+ "Share %@ is not eligible for screening"
+ "Share %@ was last saved with public permission %ld; keeping its existing screening state"
+ "Share PCS version %ld %{public}@ an upgrade to v2"
+ "Share screening feature not enabled"
+ "Stripped screening identity from PPPCS during participant vetting for URL %@"
+ "Stripped screening identity from PPPCS during public share acceptance for URL %@"
+ "TestForceDuplicateScreeningIdentity"
+ "TestForceScreeningKeyFetchErrorCode"
+ "TestForceSelfAddedPCSUpgradeFailure"
+ "TestForceSerializePublicProtectionData"
+ "TestSkipAddScreeningKeyToSelfAddedPCS"
+ "TestSkipRemoveStaleScreeningKeyFromSelfAddedPCS"
+ "The upgraded share PCS has a different current private key"
+ "The upgraded share PCS has different private keys"
+ "The upgraded share PCS has different sharees or sharee flags"
+ "The upgraded share PCS is not v2"
+ "Upgraded selfAddedPCS %@ to v2 PCS %@"
+ "Upgraded selfAddedPCS to v2 for share %@"
+ "Upgraded share PCS to v2 with %lu private keys and %lu sharees"
+ "Upgrading selfAddedPCS %@ to v2"
+ "Upgrading share PCS from version %ld to v2"
+ "daemon/fetch-screening-key"
+ "does not need"
+ "https://gateway.icloud.com/config-qa/server-signature-verification.plist"
+ "missingScreeningKeyInSelfAddedPcs"
+ "needs"
+ "screening"
+ "selfAddedPCS for share %@ contains %lu screening keys; expected at most one"
+ "selfAddedPCS v2 upgrade %{public}@ by behavior option for share %@"
+ "selfAddedPCS v2 upgrade %{public}@ by test device option for share %@"
+ "v44@?0@\"NSData\"8q16i24@\"NSData\"28@\"CKDPResponseOperationResult\"36"
```
