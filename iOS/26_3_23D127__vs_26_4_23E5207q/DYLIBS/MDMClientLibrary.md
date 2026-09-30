## MDMClientLibrary

> `/System/Library/PrivateFrameworks/MDMClientLibrary.framework/MDMClientLibrary`

```diff

-55.80.4.0.0
-  __TEXT.__text: 0x1f42c
-  __TEXT.__auth_stubs: 0x8d0
+59.100.16.0.0
+  __TEXT.__text: 0x20bf8
+  __TEXT.__auth_stubs: 0x850
   __TEXT.__objc_methlist: 0x1da4
   __TEXT.__const: 0xd1
-  __TEXT.__gcc_except_tab: 0x520
-  __TEXT.__cstring: 0x2420
-  __TEXT.__oslogstring: 0x2f1d
+  __TEXT.__gcc_except_tab: 0x564
+  __TEXT.__cstring: 0x244f
+  __TEXT.__oslogstring: 0x3082
   __TEXT.__dlopen_cstrs: 0xb7
-  __TEXT.__unwind_info: 0x838
+  __TEXT.__unwind_info: 0x950
   __TEXT.__objc_classname: 0x336
-  __TEXT.__objc_methname: 0x556f
-  __TEXT.__objc_methtype: 0xbc9
+  __TEXT.__objc_methname: 0x5585
+  __TEXT.__objc_methtype: 0xbd1
   __TEXT.__objc_stubs: 0x3920
   __DATA_CONST.__got: 0x3b0
-  __DATA_CONST.__const: 0x11b0
+  __DATA_CONST.__const: 0x11c0
   __DATA_CONST.__objc_classlist: 0xc8
   __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x13a8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x78
-  __AUTH_CONST.__auth_got: 0x478
+  __AUTH_CONST.__auth_got: 0x438
   __AUTH_CONST.__const: 0x3c0
-  __AUTH_CONST.__cfstring: 0x3300
+  __AUTH_CONST.__cfstring: 0x3340
   __AUTH_CONST.__objc_const: 0x3a10
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH.__objc_data: 0x140

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libmis.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: AB288A50-F10C-37CD-9D83-A955FB6D7465
-  Functions: 681
-  Symbols:   2935
-  CStrings:  1982
+  UUID: 8C7793CF-8416-36A1-ADDE-E9874ED1240D
+  Functions: 683
+  Symbols:   2933
+  CStrings:  1991
 
Symbols:
+ -[MDMClientCore requestReturnToServiceObliterationWithPreserveDataPlan:disallowProximitySetup:mdmProfileData:wifiProfileData:revertToSnapshotName:bootstrapToken:shouldRetryEnrollment:completionHandler:]
+ _OUTLINED_FUNCTION_0
+ ___202-[MDMClientCore requestReturnToServiceObliterationWithPreserveDataPlan:disallowProximitySetup:mdmProfileData:wifiProfileData:revertToSnapshotName:bootstrapToken:shouldRetryEnrollment:completionHandler:]_block_invoke
+ _kMDMPQueryAuthenticatedTemporarySession
+ _kMDMPQueryDirectUserSwitch
+ _objc_msgSend$requestReturnToServiceObliterationWithPreserveDataPlan:disallowProximitySetup:mdmProfileData:wifiProfileData:revertToSnapshotName:bootstrapToken:shouldRetryEnrollment:completionHandler:
+ _objc_retainAutoreleasedReturnValue
- -[MDMClientCore requestReturnToServiceObliterationWithPreserveDataPlan:disallowProximitySetup:mdmProfileData:wifiProfileData:revertToSnapshotName:bootstrapToken:completionHandler:]
- ___180-[MDMClientCore requestReturnToServiceObliterationWithPreserveDataPlan:disallowProximitySetup:mdmProfileData:wifiProfileData:revertToSnapshotName:bootstrapToken:completionHandler:]_block_invoke
- _objc_claimAutoreleasedReturnValue
- _objc_msgSend$requestReturnToServiceObliterationWithPreserveDataPlan:disallowProximitySetup:mdmProfileData:wifiProfileData:revertToSnapshotName:bootstrapToken:completionHandler:
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x3
- _objc_retain_x4
- _objc_retain_x5
- _objc_retain_x7
- _objc_retain_x8
- _objc_retain_x9
- _objc_unsafeClaimAutoreleasedReturnValue
CStrings:
+ "AuthenticatedTemporarySession"
+ "Could not deserialize JSON data for missing token: %{public}@"
+ "DirectUserSwitch"
+ "Failed to get OAuth2 bearer token invalid response: %{public}@"
+ "Failed to switch to persona %{public}@ for RM account update: %{public}@"
+ "Failed to switch to persona %{public}@ for iCloud account update: %{public}@"
+ "Failed to switch to persona %{public}@ for iTunes account update: %{public}@"
+ "Failed to switch to persona %{public}@ for token refresh: %{public}@"
+ "requestReturnToServiceObliterationWithPreserveDataPlan:disallowProximitySetup:mdmProfileData:wifiProfileData:revertToSnapshotName:bootstrapToken:shouldRetryEnrollment:completionHandler:"
+ "v24@0:8@?<v@?@\"NSData\"@\"NSData\"@\"NSData\"BB@\"NSError\">16"
+ "v68@0:8B16B20@\"NSData\"24@\"NSData\"32@\"NSString\"40@\"NSData\"48B56@?<v@?@\"NSError\">60"
+ "v68@0:8B16B20@24@32@40@48B56@?60"
- "Failed to get OAuth2 bearer token invalid response: %{public}@}"
- "requestReturnToServiceObliterationWithPreserveDataPlan:disallowProximitySetup:mdmProfileData:wifiProfileData:revertToSnapshotName:bootstrapToken:completionHandler:"
- "v24@0:8@?<v@?@\"NSData\"@\"NSData\"@\"NSData\"@\"NSError\">16"
- "v64@0:8B16B20@\"NSData\"24@\"NSData\"32@\"NSString\"40@\"NSData\"48@?<v@?@\"NSError\">56"
- "v64@0:8B16B20@24@32@40@48@?56"

```
