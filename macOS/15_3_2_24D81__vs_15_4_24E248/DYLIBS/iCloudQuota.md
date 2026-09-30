## iCloudQuota

> `/System/Library/PrivateFrameworks/iCloudQuota.framework/Versions/A/iCloudQuota`

```diff

-301.22.3.0.0
-  __TEXT.__text: 0x75988
-  __TEXT.__auth_stubs: 0x13f0
-  __TEXT.__objc_methlist: 0x4e00
-  __TEXT.__const: 0xdb8
-  __TEXT.__cstring: 0x50c0
+301.22.4.7.0
+  __TEXT.__text: 0x740c8
+  __TEXT.__auth_stubs: 0x13a0
+  __TEXT.__objc_methlist: 0x5014
+  __TEXT.__const: 0xe08
+  __TEXT.__cstring: 0x4e80
   __TEXT.__gcc_except_tab: 0x664
-  __TEXT.__oslogstring: 0x6d4e
+  __TEXT.__oslogstring: 0x6d0e
   __TEXT.__dlopen_cstrs: 0x235
   __TEXT.__ustring: 0x4
-  __TEXT.__swift5_typeref: 0x6e0
+  __TEXT.__swift5_typeref: 0x704
   __TEXT.__swift5_capture: 0x29c
   __TEXT.__swift5_reflstr: 0x2ad
-  __TEXT.__swift5_assocty: 0x78
-  __TEXT.__constg_swiftt: 0x674
+  __TEXT.__swift5_assocty: 0x90
+  __TEXT.__constg_swiftt: 0x694
   __TEXT.__swift5_fieldmd: 0x32c
-  __TEXT.__swift5_proto: 0x90
-  __TEXT.__swift5_types: 0x48
+  __TEXT.__swift5_proto: 0x94
+  __TEXT.__swift5_types: 0x4c
+  __TEXT.__swift_as_entry: 0x60
+  __TEXT.__swift_as_ret: 0x68
+  __TEXT.__swift5_builtin: 0x28
   __TEXT.__swift5_protos: 0x14
-  __TEXT.__swift5_builtin: 0x14
-  __TEXT.__unwind_info: 0x1a78
-  __TEXT.__eh_frame: 0x1148
+  __TEXT.__unwind_info: 0x1a98
+  __TEXT.__eh_frame: 0x11d8
   __TEXT.__objc_classname: 0x8b8
   __TEXT.__objc_methname: 0xbad1
   __TEXT.__objc_methtype: 0xe12
-  __TEXT.__objc_stubs: 0x7da0
+  __TEXT.__objc_stubs: 0x7d80
   __DATA_CONST.__got: 0x6d8
-  __DATA_CONST.__const: 0x9a8
+  __DATA_CONST.__const: 0x978
   __DATA_CONST.__objc_classlist: 0x320
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2960
+  __DATA_CONST.__objc_selrefs: 0x2a50
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x250
-  __DATA_CONST.__objc_arraydata: 0x6d8
-  __AUTH_CONST.__auth_got: 0xa08
-  __AUTH_CONST.__const: 0x2050
-  __AUTH_CONST.__cfstring: 0x5ca0
-  __AUTH_CONST.__objc_const: 0xa038
+  __DATA_CONST.__objc_arraydata: 0x6f8
+  __AUTH_CONST.__auth_got: 0x9e0
+  __AUTH_CONST.__const: 0x20c0
+  __AUTH_CONST.__cfstring: 0x5ce0
+  __AUTH_CONST.__objc_const: 0x9c70
   __AUTH_CONST.__objc_dictobj: 0x190
   __AUTH_CONST.__objc_arrayobj: 0x90
-  __AUTH_CONST.__objc_intobj: 0x900
+  __AUTH_CONST.__objc_intobj: 0x930
   __AUTH.__objc_data: 0x2120
-  __AUTH.__data: 0x678
+  __AUTH.__data: 0x670
   __DATA.__objc_ivar: 0x5e0
-  __DATA.__data: 0x6d8
-  __DATA.__bss: 0x1430
+  __DATA.__data: 0x6e8
+  __DATA.__bss: 0x14a0
   __DATA.__common: 0x10
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts
   - /System/Library/Frameworks/Combine.framework/Versions/A/Combine

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 547C3590-FAA9-3CE1-9501-BEBF31C7D36F
-  Functions: 2696
-  Symbols:   5219
-  CStrings:  4471
+  UUID: 2E89174C-07AD-3C63-B93B-70212F205DBA
+  Functions: 2711
+  Symbols:   5261
+  CStrings:  4460
 
Symbols:
+ +[AMSBag(Quota) quotaBag].cold.1
+ +[ICQAppCloudStorageCache sharedInstance].cold.1
+ +[ICQAppsSyncingToDriveCache sharedInstance].cold.1
+ +[ICQCloudStorageDataController _requestQueue].cold.1
+ +[ICQCloudStorageSummaryCache sharedInstance].cold.1
+ +[ICQDaemonAlert dismissAlertsWithNotificationID:].cold.1
+ +[ICQDaemonOffer(Internal) defaultPlaceholderKeys].cold.1
+ +[ICQDaemonOfferManager getCkBackupDeviceIDWithCompletionHandler:].cold.1
+ +[ICQInlineTip downwardArrowConfigurationStrings].cold.1
+ +[ICQInlineTip upwardArrowConfigurationStrings].cold.1
+ +[ICQOfferManager defaultBundleIdentifier].cold.1
+ +[ICQRequestProvider _keyIsEligibleForURLStringReplacement:].cold.1
+ +[ICQRequestProvider _newAccountBagKeyForOldKey:].cold.1
+ +[ICQStoragePlanRecommendation _requestQueue].cold.1
+ +[ICQStoragePlanRecommendationCache sharedInstance].cold.1
+ +[_ICQFollowupSpecification sharedFollowUpController].cold.1
+ +[_ICQHelperFunctions _remoteBackupSizeOperationQueue].cold.1
+ +[_ICQPhotosInfo _photosShutdownQueue].cold.1
+ -[ICQDaemonAlert dismissAlert].cold.1
+ -[ICQDaemonOfferRequestBuilder requestWithQuotaKey:reason:offerStub:notificationID:contextDictionary:mlDaemonExtraFields:sourceIsServerSample:].cold.3
+ _ICQActionForServerActionString.cold.1
+ _ICQActionForString.cold.2
+ _ICQBannerLogSystem.cold.1
+ _ICQBooleanForServerObjectDefault.cold.1
+ _ICQBundleIDForKnownContainerID.cold.1
+ _ICQContainerIDForKnownBundleID.cold.1
+ _ICQGetLogSystem.cold.1
+ _ICQLevelForString.cold.1
+ _ICQOfferTypeForServerString.cold.1
+ _ICQOfferTypeForString.cold.1
+ _ICQSignpostGetNanoseconds.cold.1
+ _ICQSignpostLogSystem.cold.1
+ ___swift_async_entry_functlets
+ ___swift_async_ret_functlets
+ ___swift_destroy_boxed_opaque_existential_0Tm
+ __block_literal_global.268
+ _symbolic SccySo9ACAccountCSg______pG s5ErrorP
+ _symbolic Sccy___________pG So30ACAccountCredentialRenewResultV s5ErrorP
+ _symbolic _____ So30ACAccountCredentialRenewResultV
- _OUTLINED_FUNCTION_7
- _OUTLINED_FUNCTION_8
- __block_literal_global.263
- _objc_msgSend$defaultLink
- _symbolic So9ACAccountCSg
CStrings:
+ "DRIVE_ALLOW_UNLIMITED_CELLULAR"
+ "ICQActionDriveAllowUnlimitedCellular"
- "Fatal error"
- "Insufficient space allocated to copy string contents"
- "Swift/ContiguousArrayBuffer.swift"
- "Swift/StringTesting.swift"
- "Swift/StringUTF8View.swift"
- "Swift/UnsafeBufferPointer.swift"
- "Swift/UnsafePointer.swift"
- "Swift/UnsafeRawPointer.swift"
- "Unexpectedly found nil while unwrapping an Optional value"
- "UnsafeMutableBufferPointer with negative count"
- "UnsafeMutablePointer.initialize overlapping range"
- "UnsafeMutablePointer.moveInitialize with negative count"
- "UnsafeMutableRawPointer.initializeMemory overlapping range"
- "icqLinkForContext: Did not find a specific action for context: %@"
- "invalid Collection: less than 'count' elements in collection"

```
