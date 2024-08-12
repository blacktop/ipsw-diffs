## iCloudQuota

> `/System/Library/PrivateFrameworks/iCloudQuota.framework/iCloudQuota`

```diff

-301.22.0.32.0
-  __TEXT.__text: 0x7d5a8
-  __TEXT.__auth_stubs: 0x1670
-  __TEXT.__objc_methlist: 0x54c4
-  __TEXT.__const: 0xe20
-  __TEXT.__cstring: 0x6691
-  __TEXT.__oslogstring: 0x7c24
+301.22.0.33.0
+  __TEXT.__text: 0x831e0
+  __TEXT.__auth_stubs: 0x1720
+  __TEXT.__objc_methlist: 0x5558
+  __TEXT.__const: 0xf90
+  __TEXT.__cstring: 0x6911
+  __TEXT.__oslogstring: 0x8069
   __TEXT.__gcc_except_tab: 0x6d0
   __TEXT.__dlopen_cstrs: 0x35f
   __TEXT.__ustring: 0x136
-  __TEXT.__swift5_typeref: 0x9f4
-  __TEXT.__swift5_capture: 0x4f0
-  __TEXT.__swift5_reflstr: 0x2e1
-  __TEXT.__swift5_assocty: 0x60
-  __TEXT.__constg_swiftt: 0x844
-  __TEXT.__swift5_fieldmd: 0x3bc
-  __TEXT.__swift5_proto: 0x90
-  __TEXT.__swift5_types: 0x54
+  __TEXT.__swift5_typeref: 0xa36
+  __TEXT.__swift5_capture: 0x50c
+  __TEXT.__swift5_reflstr: 0x3a1
+  __TEXT.__swift5_assocty: 0x78
+  __TEXT.__constg_swiftt: 0x8cc
+  __TEXT.__swift5_fieldmd: 0x43c
+  __TEXT.__swift5_proto: 0xa4
+  __TEXT.__swift5_types: 0x5c
   __TEXT.__swift5_protos: 0x14
   __TEXT.__swift5_builtin: 0x14
-  __TEXT.__unwind_info: 0x2010
-  __TEXT.__eh_frame: 0x1de8
-  __TEXT.__objc_classname: 0xa33
-  __TEXT.__objc_methname: 0xcf3b
-  __TEXT.__objc_methtype: 0xc4e
-  __TEXT.__objc_stubs: 0x8d00
-  __DATA_CONST.__got: 0x810
+  __TEXT.__unwind_info: 0x2100
+  __TEXT.__eh_frame: 0x1e30
+  __TEXT.__objc_classname: 0xa61
+  __TEXT.__objc_methname: 0xd363
+  __TEXT.__objc_methtype: 0x1009
+  __TEXT.__objc_stubs: 0x8de0
+  __DATA_CONST.__got: 0x820
   __DATA_CONST.__const: 0x1e38
-  __DATA_CONST.__objc_classlist: 0x390
+  __DATA_CONST.__objc_classlist: 0x398
   __DATA_CONST.__objc_catlist: 0x28
-  __DATA_CONST.__objc_protolist: 0x28
+  __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2db8
+  __DATA_CONST.__objc_selrefs: 0x2e08
+  __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x280
   __DATA_CONST.__objc_arraydata: 0x2090
-  __AUTH_CONST.__auth_got: 0xb48
-  __AUTH_CONST.__auth_ptr: 0x2b0
-  __AUTH_CONST.__const: 0x1360
+  __AUTH_CONST.__auth_got: 0xba0
+  __AUTH_CONST.__auth_ptr: 0x2b8
+  __AUTH_CONST.__const: 0x14b0
   __AUTH_CONST.__cfstring: 0x7140
-  __AUTH_CONST.__objc_const: 0xaf38
+  __AUTH_CONST.__objc_const: 0xb548
   __AUTH_CONST.__objc_intobj: 0xab0
   __AUTH_CONST.__objc_dictobj: 0x1478
   __AUTH_CONST.__objc_arrayobj: 0x528
-  __AUTH.__objc_data: 0x15a0
-  __AUTH.__data: 0x708
+  __AUTH.__objc_data: 0x16b8
+  __AUTH.__data: 0x730
   __DATA.__objc_ivar: 0x66c
-  __DATA.__data: 0x778
-  __DATA.__bss: 0x1380
+  __DATA.__data: 0x8a8
+  __DATA.__bss: 0x1640
   __DATA.__common: 0x10
   __DATA_DIRTY.__objc_data: 0xf60
   __DATA_DIRTY.__data: 0x248

   - /System/Library/PrivateFrameworks/CacheDelete.framework/CacheDelete
   - /System/Library/PrivateFrameworks/CloudRecommendation.framework/CloudRecommendation
   - /System/Library/PrivateFrameworks/CloudSubscriptionFeatures.framework/CloudSubscriptionFeatures
+  - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/CoreFollowUp.framework/CoreFollowUp
   - /System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices
   - /System/Library/PrivateFrameworks/MobileBackup.framework/MobileBackup

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 3018
-  Symbols:   2944
-  CStrings:  4199
+  Functions: 3103
+  Symbols:   2956
+  CStrings:  4274
 
Symbols:
+ _AnalyticsSendEventLazy
+ _OBJC_CLASS_$_ICQBubbleBannerTracker
+ _OBJC_METACLASS_$_ICQBubbleBannerTracker
+ __ICQBannerLogSystem
+ __swiftImmortalRefCount
CStrings:
+ "%!s(MISSING) Banner was dismissed in the same session returning false"
+ "%!s(MISSING) Checking Banner decay threshold lastDisplayed: %!s(MISSING) decayUntil: %!f(MISSING) current: %!s(MISSING) end: %!s(MISSING)"
+ "%!s(MISSING) Checking Banner supression threshold lastDismissed: %!s(MISSING) supressUntil: %!f(MISSING) current: %!s(MISSING)"
+ "%!s(MISSING) Decay threshold not passed. We will let the banner decay."
+ "%!s(MISSING) Decay threshold passed. Displaying banner at the top of the stack."
+ "%!s(MISSING) No cached event found for, possibly first display of the banner %!s(MISSING) returning true"
+ "%!s(MISSING) No cached events found, ignoring decay thresholds and displaying banner at the top."
+ "%!s(MISSING) Supression threshold not passed. Supressing banner"
+ "%!s(MISSING) Supression threshold passed. Displaying banner"
+ "%!s(MISSING) Unable to compute endate from given info."
+ "@\"NSDictionary\"8@?0"
+ "@32@0:8@16d24"
+ "@40@0:8@16@24d32"
+ "B44@0:8@16@24B32d36"
+ "B52@0:8@16@24@32B40d44"
+ "BubbleBannerDismissed"
+ "BubbleBannerDisplayed"
+ "Failed to copy %!s(MISSING). Skipping adding headers"
+ "ICQBubbleBannerTracker"
+ "ICQLiftUIDataSource handling redirect, re-adding headers"
+ "NSURLSessionDelegate"
+ "NSURLSessionTaskDelegate"
+ "Providing last updated for Photos Bubble Banner - Reason: %!@(MISSING) Decay: %!f(MISSING) lastUpdated: %!@(MISSING)"
+ "T@\"ICQBubbleBannerTracker\",N,R"
+ "Tracking event %!s(MISSING) for key %!s(MISSING)"
+ "URLSession:didBecomeInvalidWithError:"
+ "URLSession:didCreateTask:"
+ "URLSession:didReceiveChallenge:completionHandler:"
+ "URLSession:task:didCompleteWithError:"
+ "URLSession:task:didFinishCollectingMetrics:"
+ "URLSession:task:didReceiveChallenge:completionHandler:"
+ "URLSession:task:didReceiveInformationalResponse:"
+ "URLSession:task:didSendBodyData:totalBytesSent:totalBytesExpectedToSend:"
+ "URLSession:task:needNewBodyStream:"
+ "URLSession:task:needNewBodyStreamFromOffset:completionHandler:"
+ "URLSession:task:willBeginDelayedRequest:completionHandler:"
+ "URLSession:task:willPerformHTTPRedirection:newRequest:completionHandler:"
+ "URLSession:taskIsWaitingForConnectivity:"
+ "URLSessionDidFinishEventsForBackgroundURLSession:"
+ "We do not have a recommendation banner spec. In this case sending the current timestamp."
+ "account:lastUpdated:decayUntil:"
+ "account:shouldDisplay:forReason:dismissedInSession:supressUntil:"
+ "banner"
+ "bubbleBannerTrackLastDismissed:forReason:"
+ "com.apple.iCloudPhotosBanner"
+ "decayUntilInMS"
+ "iCloudQuota.BubbleBannerTracker"
+ "invalidateAndCancel"
+ "kAlmostFullReason"
+ "kBubbleBannerCAEventKey"
+ "kBubbleBannerDismissedKey"
+ "kBubbleBannerDisplayedKey"
+ "kFullReason"
+ "lastUpdated(_:reason:decayUntil:)"
+ "lastUpdatedForReason:decayUntil:"
+ "sessionWithConfiguration:delegate:delegateQueue:"
+ "shouldDisplay(_:date:for:dismissedInSession:supressUntil:)"
+ "shouldDisplay:forReason:dismissedInSession:supressUntil:"
+ "suppressUntilInMS"
+ "trackLastDismissed:date:reason:"
+ "trackLastDisplayedAtTheTop:date:reason:"
+ "v24@0:8@\"NSURLSession\"16"
+ "v32@0:8@\"NSURLSession\"16@\"NSError\"24"
+ "v32@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24"
+ "v40@0:8@\"NSURLSession\"16@\"NSURLAuthenticationChallenge\"24@?<v@?q@\"NSURLCredential\">32"
+ "v40@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24@\"NSError\"32"
+ "v40@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24@\"NSHTTPURLResponse\"32"
+ "v40@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24@\"NSURLSessionTaskMetrics\"32"
+ "v40@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24@?<v@?@\"NSInputStream\">32"
+ "v48@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24@\"NSURLAuthenticationChallenge\"32@?<v@?q@\"NSURLCredential\">40"
+ "v48@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24@\"NSURLRequest\"32@?<v@?q@\"NSURLRequest\">40"
+ "v48@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24q32@?<v@?@\"NSInputStream\">40"
+ "v56@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24@\"NSHTTPURLResponse\"32@\"NSURLRequest\"40@?<v@?@\"NSURLRequest\">48"
+ "v56@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24q32q40q48"
+ "v56@0:8@16@24q32q40q48"

```
