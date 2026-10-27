## AppTrackingTransparency

> `/System/Library/Frameworks/AppTrackingTransparency.framework/Versions/A/AppTrackingTransparency`

```diff

-106.2.2.0.0
-  __TEXT.__text: 0x12a8
-  __TEXT.__objc_methlist: 0xc8
-  __TEXT.__const: 0x68
-  __TEXT.__gcc_except_tab: 0x54
-  __TEXT.__cstring: 0x179
-  __TEXT.__oslogstring: 0x456
-  __TEXT.__unwind_info: 0xd8
+106.3.3.0.0
+  __TEXT.__text: 0x1e74
+  __TEXT.__objc_methlist: 0x104
+  __TEXT.__const: 0x70
+  __TEXT.__gcc_except_tab: 0x80
+  __TEXT.__cstring: 0x4c0
+  __TEXT.__oslogstring: 0x5a4
+  __TEXT.__unwind_info: 0x108
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__const: 0x20
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xb8
+  __DATA_CONST.__objc_selrefs: 0xe8
   __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__const: 0xf0
-  __AUTH_CONST.__cfstring: 0x180
+  __AUTH_CONST.__const: 0x150
+  __AUTH_CONST.__cfstring: 0x2c0
   __AUTH_CONST.__objc_const: 0x138
   __AUTH_CONST.__auth_got: 0x0
   __DATA.__bss: 0x30

   - /System/Library/PrivateFrameworks/TCC.framework/Versions/A/TCC
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 28
-  Symbols:   121
-  CStrings:  29
+  Functions: 39
+  Symbols:   150
+  CStrings:  45
 
Symbols:
+ +[ATTrackingManager _isRepromptEligible]
+ +[ATTrackingManager _performTCCAccessRequestPreferExpandedInterface:displayAdditionalInfo:completion:]
+ +[ATTrackingManager _preRequestChecksWithCompletion:]
+ +[ATTrackingManager _recordRequestOutcome:prompted:deniedReason:log:]
+ +[ATTrackingManager requestTrackingAuthorizationPreferringExpandedInterface:additionalInformationAction:completionHandler:]
+ GCC_except_table19
+ GCC_except_table23
+ GCC_except_table24
+ GCC_except_table30
+ _OBJC_CLASS_$_NSString
+ __123+[ATTrackingManager requestTrackingAuthorizationPreferringExpandedInterface:additionalInformationAction:completionHandler:]_block_invoke
+ ___102+[ATTrackingManager _performTCCAccessRequestPreferExpandedInterface:displayAdditionalInfo:completion:]_block_invoke
+ ___123+[ATTrackingManager requestTrackingAuthorizationPreferringExpandedInterface:additionalInformationAction:completionHandler:]_block_invoke
+ ___40+[ATTrackingManager _isRepromptEligible]_block_invoke
+ ___block_descriptor_48_e8_32bs40bs_e5_v8?0l
+ ___block_descriptor_56_e8_32bs40bs_e8_v16?0Q8l
+ ___copy_helper_block_e8_32b40b
+ ___destroy_helper_block_e8_32s40s
+ __dispatch_main_q
+ _dispatch_async
+ _objc_msgSend$_isCrossAppTrackingAllowed
+ _objc_msgSend$_isRepromptEligible
+ _objc_msgSend$_performTCCAccessRequestPreferExpandedInterface:displayAdditionalInfo:completion:
+ _objc_msgSend$_performTCCPreflightRequest
+ _objc_msgSend$_preRequestChecksWithCompletion:
+ _objc_msgSend$_recordRequestOutcome:prompted:deniedReason:log:
+ _objc_msgSend$applicationStateActive
+ _objc_msgSend$isApplicationExtension
+ _objc_msgSend$stringWithFormat:
+ _tcc_authorization_record_get_eligible_for_reprompt
+ _tcc_message_options_set_learn_more_link
- GCC_except_table17
- GCC_except_table18
CStrings:
+ "Tracking authorization request returning - Restricted due to permission."
+ "Tracking authorization request returning - Restricted due to profile."
+ "Tracking authorization request returning - Restricted."
+ "[%@] %{public}@"
+ "[%@] Call to requesting tracking authorization eligible for rate limiting. Returning %lu"
+ "[%@] Performing TCC Access Request (preferExpandedInterface=%d, displayAdditionalInfo=%d)."
+ "[%@] Performing TCC reprompt eligibility request."
+ "[%@] Received error invoking TCC access request with sheet."
+ "[%@] Received error querying TCC reprompt eligibility."
+ "[%@] requestTrackingAuthorizationPreferringExpandedInterface API call failed due to missing completion."
+ "[%@] requestTrackingAuthorizationPreferringExpandedInterface API call invoked, preferExpandedInterface=%d, displayAdditionalInfo=%d."
+ "[%@] requestTrackingAuthorizationPreferringExpandedInterface returning - Additional Information button tapped."
+ "requestTrackingAuthorizationPreferringExpandedInterface returning %lu due to backgrounded app."
+ "requestTrackingAuthorizationPreferringExpandedInterface returning - ATT Authorized."
+ "requestTrackingAuthorizationPreferringExpandedInterface returning - ATT Denied due to tracking toggle."
+ "requestTrackingAuthorizationPreferringExpandedInterface returning - ATT Denied."
+ "requestTrackingAuthorizationPreferringExpandedInterface returning - ATT not determined."
+ "requestTrackingAuthorizationPreferringExpandedInterface returning Authorized due to consent."
+ "requestTrackingAuthorizationPreferringExpandedInterface returning Denied due to consent."
+ "v16@?0Q8"
- "[%@] Call to requestTrackingAuthorizationWithCompletionHandler eligible for rate limiting. Returning %lu"
- "[%@] requestTrackingAuthorizationWithCompletionHandler returning - Restricted due to permission."
- "[%@] requestTrackingAuthorizationWithCompletionHandler returning - Restricted due to profile."
- "[%@] requestTrackingAuthorizationWithCompletionHandler returning - Restricted."
```
