## amsaccountsd

> `/System/Library/PrivateFrameworks/AppleMediaServices.framework/amsaccountsd`

```diff

-9.1.20.2.1
-  __TEXT.__text: 0x2194c4
-  __TEXT.__auth_stubs: 0x3cd0
-  __TEXT.__objc_stubs: 0x9a80
-  __TEXT.__objc_methlist: 0x55c4
-  __TEXT.__const: 0x1d494
-  __TEXT.__objc_classname: 0xed7
-  __TEXT.__objc_methname: 0xec61
-  __TEXT.__oslogstring: 0xd9a1
-  __TEXT.__objc_methtype: 0x431d
-  __TEXT.__cstring: 0xaff7
+9.2.16.0.0
+  __TEXT.__text: 0x21aadc
+  __TEXT.__auth_stubs: 0x3cf0
+  __TEXT.__objc_stubs: 0x9b00
+  __TEXT.__objc_methlist: 0x5634
+  __TEXT.__const: 0x1d4a4
+  __TEXT.__objc_classname: 0xf0d
+  __TEXT.__objc_methname: 0xee66
+  __TEXT.__oslogstring: 0xda41
+  __TEXT.__objc_methtype: 0x439c
+  __TEXT.__cstring: 0xb137
   __TEXT.__gcc_except_tab: 0xe30
   __TEXT.__dlopen_cstrs: 0x34d
   __TEXT.__swift5_typeref: 0x6cc8
-  __TEXT.__swift5_fieldmd: 0x63e4
-  __TEXT.__constg_swiftt: 0x52cc
+  __TEXT.__swift5_fieldmd: 0x645c
+  __TEXT.__constg_swiftt: 0x52d4
   __TEXT.__swift5_builtin: 0x118
-  __TEXT.__swift5_reflstr: 0x465c
+  __TEXT.__swift5_reflstr: 0x471c
   __TEXT.__swift5_assocty: 0x8f8
   __TEXT.__swift5_protos: 0xa8
   __TEXT.__swift5_proto: 0x16d8
   __TEXT.__swift5_types: 0x67c
-  __TEXT.__swift5_capture: 0xa28
   __TEXT.__swift_as_entry: 0x200
-  __TEXT.__swift_as_ret: 0x2a8
   __TEXT.__swift5_mpenum: 0x78
+  __TEXT.__swift5_capture: 0xa28
+  __TEXT.__swift_as_ret: 0x2a8
   __TEXT.__swift5_types2: 0x8
-  __TEXT.__unwind_info: 0x8340
-  __TEXT.__eh_frame: 0xf71c
-  __DATA_CONST.__auth_got: 0x1e78
-  __DATA_CONST.__got: 0x1220
+  __TEXT.__unwind_info: 0x8660
+  __TEXT.__eh_frame: 0xf7dc
+  __DATA_CONST.__auth_got: 0x1e88
+  __DATA_CONST.__got: 0x1228
   __DATA_CONST.__auth_ptr: 0xcb8
-  __DATA_CONST.__const: 0x12178
-  __DATA_CONST.__cfstring: 0x3fa0
-  __DATA_CONST.__objc_classlist: 0x350
+  __DATA_CONST.__const: 0x121a8
+  __DATA_CONST.__cfstring: 0x4000
+  __DATA_CONST.__objc_classlist: 0x358
   __DATA_CONST.__objc_catlist: 0x90
-  __DATA_CONST.__objc_protolist: 0x270
+  __DATA_CONST.__objc_protolist: 0x278
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x68
   __DATA_CONST.__objc_superrefs: 0x198
   __DATA_CONST.__objc_intobj: 0xa8
   __DATA_CONST.__linkguard: 0x2c
-  __DATA.__objc_const: 0xb020
-  __DATA.__objc_selrefs: 0x3878
+  __DATA.__objc_const: 0xb158
+  __DATA.__objc_selrefs: 0x38f8
   __DATA.__objc_ivar: 0x350
-  __DATA.__objc_data: 0x23d0
-  __DATA.__data: 0xa1c0
-  __DATA.__bss: 0x2d410
+  __DATA.__objc_data: 0x2420
+  __DATA.__data: 0xa230
+  __DATA.__bss: 0x2d420
   __DATA.__common: 0x190
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CloudKit.framework/CloudKit

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: EFB8DDE6-FB6B-326C-AAA3-019AC7163C70
-  Functions: 13286
-  Symbols:   1867
-  CStrings:  5435
+  UUID: 9E138AD8-8034-3513-8CBE-436110F7A8A9
+  Functions: 13303
+  Symbols:   1870
+  CStrings:  5471
 
Symbols:
+ _OBJC_CLASS_$_AMSEligibilityResponse
+ _os_eligibility_domain_for_name
+ _os_eligibility_get_domain_answer
CStrings:
+ "%{public}@Production Push Accounts with Simple Profiles: %{public}@"
+ "%{public}@Received profileName, notification will be formatted for profile purchase."
+ "AMSDEligibilityService"
+ "AMSEligibilityServiceInterface"
+ "Expiring account data for"
+ "Failed to read eligibility"
+ "T@\"AMSDEligibilityService\",R,N"
+ "The supplied domain is not supported"
+ "[MISSING FROM DS]"
+ "_startDelegateAuthenticateWithAccount:bag:cacheKey:challenge:deviceName:profileName:"
+ "ageAreaComplianceId"
+ "ams_fetchiTunesSimpleProfileAccounts"
+ "ams_simpleProfileAccounts"
+ "getEligibilityForDomain:completion:"
+ "getEligibilityServiceProxyWithReplyHandler:"
+ "initWithAnswer:source:status:context:"
+ "isAccountEligibleForAgeAssurance"
+ "isAgeVerifiedAdult"
+ "isConnectedToAgeVerifiedAdult"
+ "methodOfVerification"
+ "profileName"
+ "setAgeAreaComplianceID:"
+ "setAllowPurchases:"
+ "setIsAccountEligibleForAgeAssurance:"
+ "setIsAgeVerifiedAdult:"
+ "setIsConnectedToAgeVerifiedAdult:"
+ "setMovieRestrictionRatingSystem:"
+ "setMovieRestrictionRatingValue:"
+ "setProfileLock:"
+ "setProfileName:"
+ "setTvRestrictionRatingSystem:"
+ "setTvRestrictionRatingValue:"
+ "v24@0:8@?<v@?@\"<AMSEligibilityServiceInterface>\"@\"NSError\">16"
+ "v32@0:8@\"NSString\"16@?<v@?@\"AMSEligibilityResponse\"@\"NSError\">24"
- "_startDelegateAuthenticateWithAccount:bag:cacheKey:challenge:deviceName:"

```
