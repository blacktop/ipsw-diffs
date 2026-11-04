## findmylocated

> `/usr/libexec/findmylocated`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__swift5_entry`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`

```diff

-141.31.6.16.22
-  __TEXT.__text: 0x55e1f0
-  __TEXT.__auth_stubs: 0x5da0
-  __TEXT.__objc_stubs: 0x20e0
-  __TEXT.__objc_methlist: 0x1004
-  __TEXT.__const: 0x209a8
-  __TEXT.__cstring: 0xbdc2
-  __TEXT.__swift5_typeref: 0x72fa
-  __TEXT.__constg_swiftt: 0x7294
+141.32.9.13.4
+  __TEXT.__text: 0x5679c4
+  __TEXT.__auth_stubs: 0x5dd0
+  __TEXT.__objc_stubs: 0x2100
+  __TEXT.__objc_methlist: 0x1034
+  __TEXT.__const: 0x20b18
+  __TEXT.__cstring: 0xbee2
+  __TEXT.__swift5_typeref: 0x730a
+  __TEXT.__constg_swiftt: 0x72ec
   __TEXT.__swift5_builtin: 0x140
-  __TEXT.__swift5_reflstr: 0x7efd
-  __TEXT.__swift5_fieldmd: 0x9140
+  __TEXT.__swift5_reflstr: 0x7f5d
+  __TEXT.__swift5_fieldmd: 0x91d0
   __TEXT.__swift5_assocty: 0x958
-  __TEXT.__swift5_proto: 0x1790
-  __TEXT.__swift5_types: 0x800
-  __TEXT.__objc_classname: 0x1336
-  __TEXT.__objc_methname: 0x51c5
-  __TEXT.__objc_methtype: 0x13a8
-  __TEXT.__swift5_protos: 0x48
+  __TEXT.__swift5_proto: 0x178c
+  __TEXT.__swift5_types: 0x810
+  __TEXT.__objc_classname: 0x1406
+  __TEXT.__objc_methname: 0x52e5
+  __TEXT.__objc_methtype: 0x13e8
+  __TEXT.__swift5_protos: 0x44
   __TEXT.__swift5_mpenum: 0x50
-  __TEXT.__oslogstring: 0x1983c
-  __TEXT.__swift_as_entry: 0x1780
-  __TEXT.__swift_as_ret: 0x29ac
-  __TEXT.__swift_as_cont: 0x45ec
-  __TEXT.__swift5_capture: 0x4ff0
+  __TEXT.__oslogstring: 0x19f9c
+  __TEXT.__swift_as_entry: 0x17a0
+  __TEXT.__swift_as_ret: 0x2a08
+  __TEXT.__swift_as_cont: 0x4698
+  __TEXT.__swift5_capture: 0x4ff4
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__unwind_info: 0x18b68
-  __TEXT.__eh_frame: 0x4a468
-  __DATA_CONST.__const: 0x188c8
-  __DATA_CONST.__objc_classlist: 0x260
+  __TEXT.__unwind_info: 0x19210
+  __TEXT.__eh_frame: 0x4b060
+  __DATA_CONST.__const: 0x188d0
+  __DATA_CONST.__objc_classlist: 0x278
   __DATA_CONST.__objc_protolist: 0x160
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0xd0
   __DATA_CONST.__linkguard: 0x33
-  __DATA_CONST.__auth_got: 0x2ed8
-  __DATA_CONST.__got: 0x1dd8
-  __DATA_CONST.__auth_ptr: 0x1890
-  __DATA.__objc_const: 0x65a0
-  __DATA.__objc_selrefs: 0xde0
-  __DATA.__objc_data: 0x14f0
-  __DATA.__data: 0xf370
-  __DATA.__common: 0x13f0
+  __DATA_CONST.__auth_got: 0x2ef0
+  __DATA_CONST.__got: 0x1df8
+  __DATA_CONST.__auth_ptr: 0x18c0
+  __DATA.__objc_const: 0x67a8
+  __DATA.__objc_selrefs: 0xdf8
+  __DATA.__objc_data: 0x15e0
+  __DATA.__data: 0xf610
+  __DATA.__common: 0x13c8
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/AppIntents.framework/AppIntents
   - /System/Library/Frameworks/CloudKit.framework/CloudKit

   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 17836
-  Symbols:   2842
-  CStrings:  3934
+  Functions: 17959
+  Symbols:   2850
+  CStrings:  3974
 
Symbols:
+ _$s10FindMyBase14ManagedDefaultV12wrappedValuexSgvM
+ _$s10Foundation4DateV11descriptionSSvg
+ _$s12FindMyLocate15PreferenceErrorOs0E0AAMc
+ _$s12FindMyLocate18ClientSessionErrorV8CategoryO18missingEntitlementyA2EmFWC
+ _$s12FindMyLocate18FriendshipProtocolP52setPeoplePrecisionFindingLastTokenRequestAttemptDate_3fory10Foundation0N0VSg_AA6HandleVSgtYaKFTq
+ _$s12FindMyLocate18FriendshipProtocolP53getPeoplePrecisionFindingLastTokenRequestAttemptDates3forSDy10Foundation4UUIDVAF4DateVGAA6HandleVSg_tYaKFTq
+ _$s15FindMyMessaging11DestinationV9hashValueSivg
+ _$sSDyxq_G10FindMyBase17PropertyListValueABSSRszAbCR_rlMc
CStrings:
+ "%{private,mask.hash}s doesn't have people precision finding capability"
+ "%{public}f s since last attempt for %{private,mask.hash}s, threshold: %{public}f"
+ "Enqueuing people precision finding token requests if needed"
+ "Failed to request people precision finding token for %{private,mask.hash}s"
+ "FindingConfigData-"
+ "Has outgoingSharedSecret for %{private,mask.hash}s."
+ "LocationAuthorizationCache: authorization notification stream ended; status will no longer refresh"
+ "LocationAuthorizationCache: authorization status is %{public}d"
+ "Missing outgoingBaseDate for %{private,mask.hash}s."
+ "Missing outgoingSharedSecret for %{private,mask.hash}s."
+ "Missing peer ID for %{private,mask.hash}s, not removing people precision finding last token request attempt date"
+ "Missing peerID for %{private,mask.hash}s, skipping"
+ "Missing token record for %{private,mask.hash}s."
+ "NIRangingService+SessionDelegate"
+ "No followings, skipping token request date pruning"
+ "No peerID for %{private,mask.hash}s"
+ "No people precision finding token for %{private,mask.hash}s, requesting"
+ "No people precision finding token request was made"
+ "No primary account to send request from"
+ "No token request date pruning necessary"
+ "Not requesting people precision finding token; device is missing capabilities."
+ "Not requesting people precision finding token; feature disabled."
+ "People precision finding token (%{private,mask.hash}s) for handle %{private,mask.hash}s"
+ "People precision finding token exists for handle %{private,mask.hash}s"
+ "People precision finding token request completed!"
+ "Pruning %ld token request dates!"
+ "Removed people precision finding last token request attempt date for %{private,mask.hash}s"
+ "Request people precision finding token from: %{private,mask.hash}s"
+ "Requesting on-demand people precision finding token from %{private,mask.hash}s if needed"
+ "Requesting people precision finding token for %{private,mask.hash}s."
+ "Requesting periodic people precision finding token from %ld friends if needed"
+ "Requesting precision finding token from %{private,mask.hash}s over IDS."
+ "Successfully requested precision finding token from %{private,mask.hash}s"
+ "Updated %ld last token request attempt dates"
+ "_TtC13findmylocated26LocationAuthorizationCache"
+ "_TtCC13findmylocated16NIRangingService15SessionDelegate"
+ "_TtCC13findmylocated26LocationAuthorizationCacheP33_39FD8C67DF55239251B947B05BAFCCCB6Reader"
+ "authorizationStatusForBundlePath:"
+ "bundlePath"
+ "cachedStatus"
+ "com.apple.findmy.LocationAuthorizationCache.read"
+ "getPeoplePrecisionFindingLastTokenRequestAttemptDates for handle: %{private,mask.hash}s"
+ "getPeoplePrecisionFindingLastTokenRequestAttemptDates is only supported on internal builds"
+ "getPeoplePrecisionFindingLastTokenRequestAttemptDates(handle:completion:)"
+ "getPeoplePrecisionFindingLastTokenRequestAttemptDatesWithHandle:completion:"
+ "getPeoplePrecisionFindingTokenSharedSecretAndDate(handle:)"
+ "lastTokenRequestAttemptDatesByPeerID"
+ "locationAuthorizationCache"
+ "peerToken failed for %{private,mask.hash}s. error: %{public}@"
+ "peerToken succeeded for %{private,mask.hash}s, %{public}s"
+ "reader"
+ "requestPeoplePrecisionFindingTokensIfNeeded(_:)"
+ "sessionDelegate"
+ "setPeoplePrecisionFindingLastTokenRequestAttemptDate date: %{public}s for handle: %{private,mask.hash}s"
+ "setPeoplePrecisionFindingLastTokenRequestAttemptDate is only supported on internal builds"
+ "setPeoplePrecisionFindingLastTokenRequestAttemptDate(_:handle:completion:)"
+ "setPeoplePrecisionFindingLastTokenRequestAttemptDate:handle:completion:"
+ "v40@0:8@\"NSDate\"16@\"NSData\"24@?<v@?@\"NSError\">32"
- "%{public}s Missing friendSharedSecretsRecord for %{private,mask.hash}s. Requesting token..."
- "%{public}s Missing outgoingSharedSecret for %{private,mask.hash}s. Requesting token..."
- "%{public}s Missing primary account to send FindingTokenReuqest with my dsid!"
- "%{public}s No peerID for following %{private,mask.hash}s"
- "%{public}s found existing peerID: %{private,mask.hash}s for handle %{private,mask.hash}s."
- "%{public}s threshold: %f"
- "Checking if we need to request token for %{private,mask.hash}s"
- "Failed to request token from %{private,mask.hash}s error - %{public}@"
- "Missing outgoingSharedSecret for %{private,mask.hash}s!"
- "NIRangingService"
- "NIRangingService+Trampoline"
- "Requesting shared secret from %{private,mask.hash}s.\nserverId: %{private,mask.hash}s over IDS."
- "Successfully requested finding token from %{private,mask.hash}s"
- "Time since last token request attempt: %{public}f. Threshold: %{public}f. Not sending."
- "lastTokenRequestAttemptDate"
- "peerToken: %{private,mask.hash}s for handle %{private,mask.hash}s."
- "requestToken(from:)"
- "requestTokensIfNeeded(threshold:)"
```
