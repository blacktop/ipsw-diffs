## libsystem_eligibility.dylib

> `/usr/lib/system/libsystem_eligibility.dylib`

```diff

-286.40.9.0.1
-  __TEXT.__text: 0x30d4
+286.60.18.502.1
+  __TEXT.__text: 0x3360
   __TEXT.__auth_stubs: 0x290
-  __TEXT.__const: 0x4a8
-  __TEXT.__cstring: 0x2f68
+  __TEXT.__const: 0x558
+  __TEXT.__cstring: 0x3d72
   __TEXT.__oslogstring: 0x2eb
-  __TEXT.__unwind_info: 0xb8
+  __TEXT.__unwind_info: 0xc0
   __DATA_CONST.__got: 0x28
-  __DATA_CONST.__const: 0x8b8
+  __DATA_CONST.__const: 0xa88
   __AUTH_CONST.__auth_got: 0x148
   __AUTH_CONST.__const: 0x40
   __DATA_DIRTY.__bss: 0x10

   - /usr/lib/system/libsystem_malloc.dylib
   - /usr/lib/system/libsystem_trace.dylib
   - /usr/lib/system/libxpc.dylib
-  UUID: 1A982915-D27A-3792-9AFD-CF0D3C2435FE
-  Functions: 23
-  Symbols:   85
-  CStrings:  341
+  UUID: 9DEE1995-C220-382A-AA57-084C69A90F44
+  Functions: 25
+  Symbols:   87
+  CStrings:  396
 
Symbols:
+ ___block_descriptor_tmp.369
+ _os_eligibility_fetch_newest_policies
+ _os_eligibility_get_error_description
- ___block_descriptor_tmp.227
Functions:
+ _os_eligibility_fetch_newest_policies
+ _os_eligibility_get_error_description
~ _os_eligibility_domain_for_name : 3788 -> 4376
CStrings:
+ "An internal error occured while processing the eligibility request"
+ "Connection reset by peer"
+ "Failed to initialize the input with the provided data"
+ "Forcing eligibility answers is not supported on this device"
+ "OS_ELIGIBILITY_DOMAIN_ADULT_AGE_VERIFICATION_REQUIRED"
+ "OS_ELIGIBILITY_DOMAIN_ADULT_AGE_VERIFICATION_REQUIRED_MINI_BUDDY"
+ "OS_ELIGIBILITY_DOMAIN_APP_STORE_LAUNCH_AGE_VERIFICATION"
+ "OS_ELIGIBILITY_DOMAIN_BLOCK_ASK_TO_BUY_DISABLE"
+ "OS_ELIGIBILITY_DOMAIN_CHILD_AND_TEEN_RESTRICTION_REQUIRED"
+ "OS_ELIGIBILITY_DOMAIN_COMM_SAFETY_FORCE_ON"
+ "OS_ELIGIBILITY_DOMAIN_DECLARED_AGE_RANGE_API_ALWAYS_SHARE_REQUIRED"
+ "OS_ELIGIBILITY_DOMAIN_DECLARED_AGE_RANGE_API_NOTIFY_FOR_SIGNIFICANT_APP_CHANGE"
+ "OS_ELIGIBILITY_DOMAIN_DECLARED_AGE_RANGE_API_VEND_GEO_SPECIFIC_AGE_RANGES"
+ "OS_ELIGIBILITY_DOMAIN_DECLARED_AGE_RANGE_API_VEND_GEO_SPECIFIC_AGE_RANGES_SANDBOX"
+ "OS_ELIGIBILITY_DOMAIN_DECLARED_AGE_RANGE_API_VEND_VERIFICATION_REQUIRED"
+ "OS_ELIGIBILITY_DOMAIN_DECLARED_AGE_RANGE_API_VEND_VERIFICATION_REQUIRED_SANDBOX"
+ "OS_ELIGIBILITY_DOMAIN_FORCE_ASK_TO_BUY_ON"
+ "OS_ELIGIBILITY_DOMAIN_GUARDIAN_AGE_VERIFICATION_REQUIRED"
+ "OS_ELIGIBILITY_DOMAIN_GUARDIAN_AGE_VERIFICATION_REQUIRED_MINI_BUDDY"
+ "OS_ELIGIBILITY_DOMAIN_PERMISSIONKIT_SIGNIFICANT_APP_CHANGE_REQUEST"
+ "OS_ELIGIBILITY_DOMAIN_PERMISSIONKIT_SIGNIFICANT_APP_CHANGE_REQUEST_SANDBOX"
+ "OS_ELIGIBILITY_DOMAIN_SIGNIFICANT_APP_UPDATE_RESTRICTED"
+ "OS_ELIGIBILITY_DOMAIN_TEEN_ATTACHED_TO_FAMILY_REQUIRED"
+ "OS_ELIGIBILITY_DOMAIN_UNVERIFIED_ADULT_RESTRICTION_REQUIRED"
+ "OS_ELIGIBILITY_DOMAIN_WEB_CONTENT_FILTER_FORCE_ON"
+ "The provided context data is malformed"
+ "The provided input status is not settable"
+ "The specified answer type is invalid"
+ "The specified directory path is invalid or inaccessible"
+ "The specified domain set is invalid or not recognized"
+ "The specified eligibility domain is invalid or not recognized"
+ "The specified eligibility input type is not supported or recognized"
+ "The specified input status is invalid"
+ "Unknown Error Number"
+ "com.apple.os-eligibility-domain.change.adult-age-verification-required"
+ "com.apple.os-eligibility-domain.change.adult-age-verification-required-mini-buddy"
+ "com.apple.os-eligibility-domain.change.app-store-launch-age-verification"
+ "com.apple.os-eligibility-domain.change.block-ask-to-buy-disable"
+ "com.apple.os-eligibility-domain.change.child-and-teen-restriction-required"
+ "com.apple.os-eligibility-domain.change.comm-safety-force-on"
+ "com.apple.os-eligibility-domain.change.declared-age-range-api-always-share-required"
+ "com.apple.os-eligibility-domain.change.declared-age-range-api-notify-for-significant-app-change"
+ "com.apple.os-eligibility-domain.change.declared-age-range-api-vend-geo-specific-age-ranges"
+ "com.apple.os-eligibility-domain.change.declared-age-range-api-vend-geo-specific-age-ranges-sandbox"
+ "com.apple.os-eligibility-domain.change.declared-age-range-api-vend-verification-required"
+ "com.apple.os-eligibility-domain.change.declared-age-range-api-vend-verification-required-sandbox"
+ "com.apple.os-eligibility-domain.change.force-ask-to-buy-on"
+ "com.apple.os-eligibility-domain.change.guardian-age-verification-required"
+ "com.apple.os-eligibility-domain.change.guardian-age-verification-required-mini-buddy"
+ "com.apple.os-eligibility-domain.change.permissionkit-significant-app-change-request"
+ "com.apple.os-eligibility-domain.change.permissionkit-significant-app-change-request-sandbox"
+ "com.apple.os-eligibility-domain.change.significant-app-update-restricted"
+ "com.apple.os-eligibility-domain.change.teen-attached-to-family-required"
+ "com.apple.os-eligibility-domain.change.unverified-adult-restriction-required"
+ "com.apple.os-eligibility-domain.change.web-content-filter-force-on"

```
