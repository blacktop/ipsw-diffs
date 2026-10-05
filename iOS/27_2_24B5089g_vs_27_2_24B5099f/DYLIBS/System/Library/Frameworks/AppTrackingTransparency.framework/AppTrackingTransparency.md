## AppTrackingTransparency

> `/System/Library/Frameworks/AppTrackingTransparency.framework/AppTrackingTransparency`

```diff

-106.3.2.0.0
+106.3.3.0.0
   __TEXT.__text: 0x29b0
   __TEXT.__objc_methlist: 0x184
   __TEXT.__const: 0x80
   __TEXT.__gcc_except_tab: 0xe8
-  __TEXT.__cstring: 0x4cc
-  __TEXT.__oslogstring: 0x838
+  __TEXT.__cstring: 0x4e8
+  __TEXT.__oslogstring: 0x844
   __TEXT.__unwind_info: 0x160
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
Symbols:
+ +[ATTrackingManager requestTrackingAuthorizationPreferringExpandedInterface:additionalInformationAction:completionHandler:]
+ ___123+[ATTrackingManager requestTrackingAuthorizationPreferringExpandedInterface:additionalInformationAction:completionHandler:]_block_invoke
- +[ATTrackingManager requestTrackingAuthorizationPreferExpandedInterface:additionalInformationAction:completionHandler:]
- ___119+[ATTrackingManager requestTrackingAuthorizationPreferExpandedInterface:additionalInformationAction:completionHandler:]_block_invoke
CStrings:
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
- "[%@] requestTrackingAuthorizationPreferExpandedInterface API call failed due to missing completion."
- "[%@] requestTrackingAuthorizationPreferExpandedInterface API call invoked, preferExpandedInterface=%d, displayAdditionalInfo=%d."
- "[%@] requestTrackingAuthorizationPreferExpandedInterface returning - Additional Information button tapped."
- "requestTrackingAuthorizationPreferExpandedInterface returning %lu due to backgrounded app."
- "requestTrackingAuthorizationPreferExpandedInterface returning - ATT Authorized."
- "requestTrackingAuthorizationPreferExpandedInterface returning - ATT Denied due to tracking toggle."
- "requestTrackingAuthorizationPreferExpandedInterface returning - ATT Denied."
- "requestTrackingAuthorizationPreferExpandedInterface returning - ATT not determined."
- "requestTrackingAuthorizationPreferExpandedInterface returning Authorized due to consent."
- "requestTrackingAuthorizationPreferExpandedInterface returning Denied due to consent."
```
