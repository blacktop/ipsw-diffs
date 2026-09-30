## AppTrackingTransparency

> `/System/Library/Frameworks/AppTrackingTransparency.framework/AppTrackingTransparency`

```diff

-104.0.0.0.0
-  __TEXT.__text: 0x1d38
-  __TEXT.__auth_stubs: 0x310
-  __TEXT.__objc_methlist: 0x13c
-  __TEXT.__const: 0x78
-  __TEXT.__gcc_except_tab: 0x16c
+106.1.1.0.0
+  __TEXT.__text: 0x21fc
+  __TEXT.__auth_stubs: 0x320
+  __TEXT.__objc_methlist: 0x144
+  __TEXT.__const: 0x80
+  __TEXT.__gcc_except_tab: 0x1b0
   __TEXT.__cstring: 0x1aa
-  __TEXT.__oslogstring: 0x33e
-  __TEXT.__unwind_info: 0xf0
-  __TEXT.__objc_classname: 0x4d
-  __TEXT.__objc_methname: 0x480
-  __TEXT.__objc_methtype: 0x7e
+  __TEXT.__oslogstring: 0x6f6
+  __TEXT.__unwind_info: 0x100
+  __TEXT.__objc_classname: 0x4c
+  __TEXT.__objc_methname: 0x496
+  __TEXT.__objc_methtype: 0x86
   __TEXT.__objc_stubs: 0x4a0
   __DATA_CONST.__got: 0x70
-  __DATA_CONST.__const: 0x128
+  __DATA_CONST.__const: 0x160
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x188
   __DATA_CONST.__objc_protorefs: 0x8
-  __AUTH_CONST.__auth_got: 0x198
+  __AUTH_CONST.__auth_got: 0x1a0
   __AUTH_CONST.__const: 0x60
   __AUTH_CONST.__cfstring: 0x160
   __AUTH_CONST.__objc_const: 0x188

   - /System/Library/PrivateFrameworks/UserManagement.framework/UserManagement
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 34C83D65-36F2-300E-9D02-4BF1C49AEB3A
-  Functions: 37
-  Symbols:   234
-  CStrings:  108
+  UUID: 35D823C4-01F0-3C9E-8776-574DB5193D87
+  Functions: 40
+  Symbols:   243
+  CStrings:  120
 
Symbols:
+ +[ATTrackingEnforcementManager _refreshEnforcementStatusInBackground]
+ ___69+[ATTrackingEnforcementManager _refreshEnforcementStatusInBackground]_block_invoke
+ ___69+[ATTrackingEnforcementManager _refreshEnforcementStatusInBackground]_block_invoke.4
+ ___69+[ATTrackingEnforcementManager _refreshEnforcementStatusInBackground]_block_invoke.5
+ ___69+[ATTrackingEnforcementManager _refreshEnforcementStatusInBackground]_block_invoke.5.cold.1
+ ___69+[ATTrackingEnforcementManager _refreshEnforcementStatusInBackground]_block_invoke.7
+ ___69+[ATTrackingEnforcementManager _refreshEnforcementStatusInBackground]_block_invoke_2
+ ___block_descriptor_48_e8_32bs_e17_v16?0"NSError"8ls32l8
+ ___block_descriptor_48_e8_32bs_e5_v8?0ls32l8
+ ___block_descriptor_48_e8_32s_e14_v24?0B8q12B20ls32l8
+ ___block_descriptor_48_e8_32s_e5_v8?0ls32l8
+ __os_log_error_impl
+ _objc_msgSend$_refreshEnforcementStatusInBackground
+ _objc_msgSend$remoteObjectProxyWithErrorHandler:
+ _objc_release_x9
+ _objc_retain_x8
- GCC_except_table8
- ___68+[ATTrackingEnforcementManager shouldEnforceTrackingWithReasonCode:]_block_invoke
- ___68+[ATTrackingEnforcementManager shouldEnforceTrackingWithReasonCode:]_block_invoke.10
- ___68+[ATTrackingEnforcementManager shouldEnforceTrackingWithReasonCode:]_block_invoke.6
- ___68+[ATTrackingEnforcementManager shouldEnforceTrackingWithReasonCode:]_block_invoke.7
- ___block_descriptor_40_e17_v16?0"NSError"8l
- ___block_descriptor_40_e5_v8?0l
- ___block_descriptor_88_e8_32s40r48r56r64r_e14_v24?0B8q12B20lr40l8r48l8s32l8r56l8r64l8
- _objc_msgSend$code
- _objc_msgSend$synchronousRemoteObjectProxyWithErrorHandler:
- _objc_retain_x22
- _objc_retain_x23
CStrings:
+ "[%@] Background refresh completed. enforced: %d, reason: %ld"
+ "[%@] Background refresh failed with error: %@"
+ "[%@] Cache is stale. Triggering background refresh."
+ "[%@] Call to requestTrackingAuthorizationWithCompletionHandler eligible for rate limiting. Returning %lu"
+ "[%@] Call to trackingAuthorizationStatus eligible for rate limiting. Returning %lu"
+ "[%@] Returning from trackingAuthorizationStatus - %lu"
+ "[%@] requestTrackingAuthorizationWithCompletionHandler API call failed due to missing completion."
+ "[%@] requestTrackingAuthorizationWithCompletionHandler returning %lu due to backgrounded app."
+ "[%@] requestTrackingAuthorizationWithCompletionHandler returning - ATT Authorized."
+ "[%@] requestTrackingAuthorizationWithCompletionHandler returning - ATT Denied due to consent."
+ "[%@] requestTrackingAuthorizationWithCompletionHandler returning - ATT Denied due to tracking toggle."
+ "[%@] requestTrackingAuthorizationWithCompletionHandler returning - ATT not determined."
+ "[%@] requestTrackingAuthorizationWithCompletionHandler returning - Restricted due to permission."
+ "[%@] requestTrackingAuthorizationWithCompletionHandler returning - Restricted due to profile."
+ "[%@] requestTrackingAuthorizationWithCompletionHandler returning - Restricted."
+ "[%@] requestTrackingAuthorizationWithCompletionHandler returning Authorized due to consent."
+ "[%@] requestTrackingAuthorizationWithCompletionHandler returning Denied due to consent."
+ "_refreshEnforcementStatusInBackground"
+ "remoteObjectProxyWithErrorHandler:"
+ "v16@0:8"
- "[%@] Call to requestTrackingAuthorizationWithCompletionHandler eligible for rate limiting"
- "[%@] Call to trackingAuthorizationStatus eligible for rate limiting"
- "[%@] EnforcementService call completed successfully: enforced: %d reason code: %ld."
- "[%@] Failed to create connection to EnforcementService. Using default values."
- "[%@] Received error code %ld from remote call to EnforcementService: %@"
- "[%@] Returned from synchronous remote call to EnforcementService"
- "code"
- "synchronousRemoteObjectProxyWithErrorHandler:"

```
