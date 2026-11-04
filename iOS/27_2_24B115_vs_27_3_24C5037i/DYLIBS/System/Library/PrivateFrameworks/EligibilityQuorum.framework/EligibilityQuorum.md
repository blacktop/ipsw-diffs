## EligibilityQuorum

> `/System/Library/PrivateFrameworks/EligibilityQuorum.framework/EligibilityQuorum`

```diff

-248.1.0.0.0
-  __TEXT.__text: 0x3fe58
+257.1.0.0.0
+  __TEXT.__text: 0x48f98
   __TEXT.__objc_methlist: 0x29c
-  __TEXT.__const: 0x3af4
-  __TEXT.__swift5_typeref: 0xf90
-  __TEXT.__swift5_capture: 0x5b0
-  __TEXT.__cstring: 0x992
-  __TEXT.__oslogstring: 0x6a2
-  __TEXT.__constg_swiftt: 0x1254
-  __TEXT.__swift5_reflstr: 0x766
-  __TEXT.__swift5_fieldmd: 0xc20
+  __TEXT.__const: 0x3b64
+  __TEXT.__swift5_typeref: 0x1022
+  __TEXT.__swift5_capture: 0x5c8
+  __TEXT.__cstring: 0xb92
+  __TEXT.__oslogstring: 0x9b8
+  __TEXT.__constg_swiftt: 0x12c0
+  __TEXT.__swift5_reflstr: 0x7e6
+  __TEXT.__swift5_fieldmd: 0xc50
   __TEXT.__swift5_assocty: 0x1e8
   __TEXT.__swift5_builtin: 0x28
   __TEXT.__swift5_proto: 0x2b0
   __TEXT.__swift5_types: 0x114
-  __TEXT.__swift_as_entry: 0x10c
-  __TEXT.__swift_as_ret: 0xe0
-  __TEXT.__swift_as_cont: 0x220
+  __TEXT.__swift_as_entry: 0x110
+  __TEXT.__swift_as_ret: 0xf0
+  __TEXT.__swift_as_cont: 0x230
   __TEXT.__swift5_protos: 0x20
   __TEXT.__swift5_mpenum: 0x10
-  __TEXT.__unwind_info: 0x1648
-  __TEXT.__eh_frame: 0x2e08
+  __TEXT.__unwind_info: 0x1738
+  __TEXT.__eh_frame: 0x3110
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x1e8
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__got: 0x240
-  __AUTH_CONST.__const: 0x2688
-  __AUTH_CONST.__objc_const: 0x1260
-  __AUTH_CONST.__auth_got: 0xa98
-  __AUTH.__objc_data: 0x1d0
+  __DATA_CONST.__got: 0x298
+  __AUTH_CONST.__const: 0x2728
+  __AUTH_CONST.__objc_const: 0x1298
+  __AUTH_CONST.__auth_got: 0xb08
+  __AUTH.__objc_data: 0x220
   __AUTH.__data: 0x6f0
-  __DATA.__data: 0x800
+  __DATA.__data: 0x8c0
   __DATA.__common: 0x60
   __DATA_DIRTY.__objc_data: 0xf0
-  __DATA_DIRTY.__data: 0xd88
+  __DATA_DIRTY.__data: 0xde0
   __DATA_DIRTY.__common: 0x38
   __DATA_DIRTY.__bss: 0xb00
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 1400
-  Symbols:   667
-  CStrings:  97
+  Functions: 1447
+  Symbols:   680
+  CStrings:  122
 
Symbols:
+ _OBJC_CLASS_$_NSDate
+ ___swift_assign_boxed_opaque_existential_0
+ ___swift_closure_destructor.58Tm
+ _objc_release_x1
+ _objc_retain_x21
+ _objc_retain_x24
+ _objc_retain_x26
+ _symbolic $s17EligibilityQuorum06RemoteA13SyncProvidingP
+ _symbolic SDySSSo6NSDataCG
+ _symbolic SS3key_yp5valuet
+ _symbolic SayScTyyt_____GG s5NeverO
+ _symbolic Say______pG 17EligibilityQuorum06RemoteA13SyncProvidingP
+ _symbolic _____3key______5valuet 13OSEligibility0A5InputO AA0aB6StatusO
+ _symbolic _____Sg 10Foundation4DateV
+ _symbolic _____Sg 13OSEligibility0A5InputO
+ _symbolic _____Sg 17EligibilityQuorum0A6RemedyV
+ _symbolic _____Sg_ABt 10Foundation4DateV
+ _symbolic _____Sg_ABt 13OSEligibility0A5InputO
+ _symbolic ______p 17EligibilityQuorum06RemoteA13SyncProvidingP
+ _symbolic _____ySSSo6NSDataCG s18_DictionaryStorageC
+ _symbolic _____ySS_____G s18_DictionaryStorageC 17EligibilityQuorum0C6ResultO
+ _symbolic _____ySS_____G s18_DictionaryStorageC 17EligibilityQuorum20IneligibilityReasonsV
+ _symbolic _____y__________G s18_DictionaryStorageC 13OSEligibility0C5InputO AC0cD6StatusO
+ _symbolic _____y______pG s23_ContiguousArrayStorageC 17EligibilityQuorum06RemoteD13SyncProvidingP
- ___swift_closure_destructor.59Tm
- _objc_retain_x19
- _swift_isUniquelyReferenced_nonNull_bridgeObject
- _symbolic $s17EligibilityQuorum06RemoteA12SyncProviderP
- _symbolic Say______pG 17EligibilityQuorum06RemoteA12SyncProviderP
- _symbolic ______p 17EligibilityQuorum06RemoteA12SyncProviderP
- _symbolic _____y______pG s23_ContiguousArrayStorageC 17EligibilityQuorum06RemoteD12SyncProviderP
- _symbolic _____yxxQp_QPG 17EligibilityQuorum17FeatureInputFuserC
- _symbolic _____yxxQp_QP_G 17EligibilityQuorum17FeatureInputFuserC0D5State33_9F744EBC820384D1DA02E4C29D8B2B01LLC
- _symbolic _____yyXlG s23_ContiguousArrayStorageC
- _symbolic xxQp_QP
CStrings:
+ "%{public}s; rechecking eligibility sync"
+ "Asking peer to resend its eligibility"
+ "Couldn't initialize accessor for saving last definite remote eligibility"
+ "Couldn't observe %{public}s"
+ "Dropped result from unregistered input for feature [%{private}s]"
+ "Failed to repair local reasons."
+ "Local eligibility missing from NPS; republishing %{public}s"
+ "No local eligibility to republish yet for %{public}s"
+ "Peer answered resend request"
+ "Peer is pending for %{public}s; using %{public}s: %{public}s"
+ "Published local eligibility for %{public}s: %{public}s"
+ "REMEDY_ALERT_MESSAGE_ICLOUD_TERMS"
+ "REMEDY_ALERT_TITLE_ICLOUD_TERMS"
+ "REMEDY_CONFIRM_ICLOUD_TERMS"
+ "REMEDY_TITLE_ICLOUD_TERMS"
+ "Remote provider reported .pending for %{public}s; treating as cannotCommunicateWithPeer"
+ "Resending local eligibility at peer's request"
+ "Stopped peer data retry loop"
+ "com.apple.account.needsToVerifyTerms"
+ "com.apple.intelligence.unableToFetchAvailability"
+ "com.apple.nanoregistry.pairedSync.initialSyncDidComplete"
+ "com.apple.nanoregistry.pairedSync.migrationSyncDidComplete"
+ "com.apple.nanoregistry.watchdidbecomeactive"
+ "lastDefiniteRemoteEligibility"
+ "needsToVerifyTerms"
```
