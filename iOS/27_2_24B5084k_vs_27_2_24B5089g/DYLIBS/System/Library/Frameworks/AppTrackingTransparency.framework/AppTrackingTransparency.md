## AppTrackingTransparency

> `/System/Library/Frameworks/AppTrackingTransparency.framework/AppTrackingTransparency`

```diff

-106.3.1.0.0
+106.3.2.0.0
   __TEXT.__text: 0x29b0
   __TEXT.__objc_methlist: 0x184
   __TEXT.__const: 0x80
   __TEXT.__gcc_except_tab: 0xe8
-  __TEXT.__cstring: 0x4c5
-  __TEXT.__oslogstring: 0x835
+  __TEXT.__cstring: 0x4cc
+  __TEXT.__oslogstring: 0x838
   __TEXT.__unwind_info: 0x160
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
Symbols:
+ +[ATTrackingManager _performTCCAccessRequestPreferExpandedInterface:displayAdditionalInfo:completion:]
+ +[ATTrackingManager requestTrackingAuthorizationPreferExpandedInterface:additionalInformationAction:completionHandler:]
+ ___102+[ATTrackingManager _performTCCAccessRequestPreferExpandedInterface:displayAdditionalInfo:completion:]_block_invoke
+ ___119+[ATTrackingManager requestTrackingAuthorizationPreferExpandedInterface:additionalInformationAction:completionHandler:]_block_invoke
+ _objc_msgSend$_performTCCAccessRequestPreferExpandedInterface:displayAdditionalInfo:completion:
- +[ATTrackingManager _performTCCAccessRequestUsingExpandedInterface:displayAdditionalInfo:completion:]
- +[ATTrackingManager requestTrackingAuthorizationUsingExpandedInterface:additionalInformationAction:completionHandler:]
- ___101+[ATTrackingManager _performTCCAccessRequestUsingExpandedInterface:displayAdditionalInfo:completion:]_block_invoke
- ___118+[ATTrackingManager requestTrackingAuthorizationUsingExpandedInterface:additionalInformationAction:completionHandler:]_block_invoke
- _objc_msgSend$_performTCCAccessRequestUsingExpandedInterface:displayAdditionalInfo:completion:
CStrings:
+ "[%@] requestTrackingAuthorizationPreferExpandedInterface API call failed due to missing completion."
+ "[%@] requestTrackingAuthorizationPreferExpandedInterface API call invoked, preferExpandedInterface=%d, displayAdditionalInfo=%d."
+ "[%@] requestTrackingAuthorizationPreferExpandedInterface returning - Additional Information button tapped."
+ "requestTrackingAuthorizationPreferExpandedInterface returning %lu due to backgrounded app."
+ "requestTrackingAuthorizationPreferExpandedInterface returning - ATT Authorized."
+ "requestTrackingAuthorizationPreferExpandedInterface returning - ATT Denied due to tracking toggle."
+ "requestTrackingAuthorizationPreferExpandedInterface returning - ATT Denied."
+ "requestTrackingAuthorizationPreferExpandedInterface returning - ATT not determined."
+ "requestTrackingAuthorizationPreferExpandedInterface returning Authorized due to consent."
+ "requestTrackingAuthorizationPreferExpandedInterface returning Denied due to consent."
- "[%@] requestTrackingAuthorizationUsingExpandedInterface API call failed due to missing completion."
- "[%@] requestTrackingAuthorizationUsingExpandedInterface API call invoked, preferExpandedInterface=%d, displayAdditionalInfo=%d."
- "[%@] requestTrackingAuthorizationUsingExpandedInterface returning - Additional Information button tapped."
- "requestTrackingAuthorizationUsingExpandedInterface returning %lu due to backgrounded app."
- "requestTrackingAuthorizationUsingExpandedInterface returning - ATT Authorized."
- "requestTrackingAuthorizationUsingExpandedInterface returning - ATT Denied due to tracking toggle."
- "requestTrackingAuthorizationUsingExpandedInterface returning - ATT Denied."
- "requestTrackingAuthorizationUsingExpandedInterface returning - ATT not determined."
- "requestTrackingAuthorizationUsingExpandedInterface returning Authorized due to consent."
- "requestTrackingAuthorizationUsingExpandedInterface returning Denied due to consent."
```
