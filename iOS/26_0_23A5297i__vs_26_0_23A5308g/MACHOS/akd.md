## akd

> `/System/Library/PrivateFrameworks/AuthKit.framework/akd`

```diff

-518.1.0.0.0
-  __TEXT.__text: 0x1b44bc
-  __TEXT.__auth_stubs: 0x1fc0
-  __TEXT.__objc_stubs: 0x18f40
-  __TEXT.__objc_methlist: 0xb244
-  __TEXT.__const: 0x4280
-  __TEXT.__cstring: 0xc7c3
+520.0.0.0.0
+  __TEXT.__text: 0x2617b0
+  __TEXT.__auth_stubs: 0x1f60
+  __TEXT.__objc_stubs: 0x18f60
+  __TEXT.__objc_methlist: 0xb254
+  __TEXT.__const: 0x4120
+  __TEXT.__cstring: 0xc993
   __TEXT.__objc_classname: 0x19e5
   __TEXT.__objc_methtype: 0x6087
-  __TEXT.__gcc_except_tab: 0x24d4
-  __TEXT.__objc_methname: 0x23610
-  __TEXT.__oslogstring: 0x21f58
-  __TEXT.__dlopen_cstrs: 0x5a
+  __TEXT.__gcc_except_tab: 0x3d30
+  __TEXT.__objc_methname: 0x2366f
+  __TEXT.__oslogstring: 0x220c8
+  __TEXT.__dlopen_cstrs: 0x15f
   __TEXT.__swift5_typeref: 0x2363
   __TEXT.__swift5_fieldmd: 0xe04
   __TEXT.__constg_swiftt: 0x15e0

   __TEXT.__swift_as_entry: 0x390
   __TEXT.__swift_as_ret: 0x458
   __TEXT.__swift5_protos: 0x3c
-  __TEXT.__unwind_info: 0x5ef0
-  __TEXT.__eh_frame: 0x8628
-  __DATA_CONST.__auth_got: 0xff0
-  __DATA_CONST.__got: 0x17f0
+  __TEXT.__unwind_info: 0x5420
+  __TEXT.__eh_frame: 0xa030
+  __DATA_CONST.__auth_got: 0xfc0
+  __DATA_CONST.__got: 0x1808
   __DATA_CONST.__auth_ptr: 0x4d8
-  __DATA_CONST.__const: 0xeec8
-  __DATA_CONST.__cfstring: 0x77c0
+  __DATA_CONST.__const: 0x10bb8
+  __DATA_CONST.__cfstring: 0x7ba0
   __DATA_CONST.__objc_classlist: 0x768
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x318

   __DATA_CONST.__objc_dictobj: 0x140
   __DATA_CONST.__objc_arrayobj: 0x60
   __DATA_CONST.__linkguard: 0x3e
-  __DATA.__objc_const: 0x256d8
-  __DATA.__objc_selrefs: 0x79e0
+  __DATA.__objc_const: 0x256c8
+  __DATA.__objc_selrefs: 0x79f0
   __DATA.__objc_ivar: 0xa6c
   __DATA.__objc_data: 0x5730
-  __DATA.__data: 0x3c88
-  __DATA.__bss: 0x2b30
+  __DATA.__data: 0x3d18
+  __DATA.__bss: 0x2b40
   __DATA.__common: 0x111
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/Combine.framework/Combine

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 5354CBF0-09A0-3187-83DA-E73ABB0E6282
-  Functions: 7836
-  Symbols:   1426
-  CStrings:  11013
+  UUID: F03453EE-4605-39DC-988E-1C6EB108D358
+  Functions: 7216
+  Symbols:   1423
+  CStrings:  11093
 
Symbols:
+ _AKAppleAccountConsentValueKey
+ _AKAppleAccountConsentVersionKey
+ _AKAppleAccountPrivacyConsentKey
+ _memset
+ _pow
- ___exp10
- _objc_claimAutoreleasedReturnValue
- _objc_release_x2
- _objc_retain_x1
- _objc_retain_x3
- _objc_retain_x4
- _objc_retain_x5
- _objc_retain_x6
CStrings:
+ "@\"AKRemoteViewServiceConfiguration\""
+ "AKSQLStoreErrorCode"
+ "AKVMType"
+ "Attempting to generate certificate data... (%d/%lu/%d)"
+ "Email address cannot be nil"
+ "Email domain cannot be nil"
+ "Error discovering bt devices: %@"
+ "Executing signing request with QoS: original=%d, enforced=%d, request=%@"
+ "Header"
+ "IDSBAASignerErrorDomain"
+ "Privacy consent configuration info must be a dictionary: %@"
+ "Privacy consent dictionary missing required keys: %@"
+ "Privacy consent value and version are required and cannot be empty"
+ "Private Email cannot be nil"
+ "Request"
+ "Silent status check not yet supported..."
+ "URL bag cache hit for altDSID, returning immediately without async work"
+ "URL bag cache miss for altDSID, falling back to async network fetch"
+ "X-Apple-I-Accepted-Terms"
+ "X-Apple-I-MD-EUID"
+ "_baaConfigTTLInDays"
+ "_generateTTLInMins"
+ "ak_addEffectiveUserIdentifierHeader"
+ "application/x-apple-plist"
+ "baa-attestation-exclusion-vip"
+ "beneficiaryListVersion"
+ "beneficiaryUUIDs"
+ "com.apple.IDS"
+ "com.apple.iTunes"
+ "credential_state"
+ "custodianListVersion"
+ "custodianUUIDs"
+ "ichat"
+ "is missing"
+ "items_ids"
+ "setPrivacyConsentForAltDSID:client:value:version:completion:"
+ "softlink:o:fw:ApplePushService"
+ "softlink:o:fw:CoreFollowUp"
+ "softlink:o:fw:CoreLocation"
+ "softlink:o:fw:KeychainCircle"
+ "softlink:o:fw:Rapport"
+ "softlink:o:fw:SafariFoundation"
+ "softlink:o:fw:SetupAssistant"
+ "softlink:o:fw:SetupKit"
+ "softlink:r:fw:BaseBoard"
+ "softlink:r:fw:IDS"
+ "synced-time"
+ "text/plist"
+ "text/x-json"
+ "timestampOnCK"
+ "transfer_state"
+ "userType"
+ "valid"
+ "x-apple-debug-time-diff-ms"
- "Attempting to generate certificate data... (%dh/%luh/%dh)"
- "Client is not allow listed to access birthday!"
- "Executing signing request: %@; qos: %@"
- "_generateTTL"
- "com.apple.AKTester"
- "com.apple.FamilyCircle"
- "com.apple.WatchFacesWallpaperSupport.SnoopyPoster"
- "com.apple.appleaccountd"
- "com.apple.familycircled"
- "isPermittedToAccessBirthday"

```
