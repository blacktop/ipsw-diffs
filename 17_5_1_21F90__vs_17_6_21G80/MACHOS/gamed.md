## gamed

> `/usr/libexec/gamed`

```diff

-818.5.11.2.2
-  __TEXT.__text: 0x1f2938
+818.6.8.0.0
+  __TEXT.__text: 0x1f38dc
   __TEXT.__auth_stubs: 0x27b0
-  __TEXT.__objc_stubs: 0x1a040
-  __TEXT.__objc_methlist: 0xb9f4
-  __TEXT.__objc_classname: 0x1e95
-  __TEXT.__oslogstring: 0x125b4
+  __TEXT.__objc_stubs: 0x1a180
+  __TEXT.__objc_methlist: 0xba7c
+  __TEXT.__objc_classname: 0x1e93
+  __TEXT.__oslogstring: 0x12810
   __TEXT.__const: 0x10c30
-  __TEXT.__gcc_except_tab: 0x2a20
-  __TEXT.__cstring: 0x1ace4
-  __TEXT.__objc_methname: 0x218bf
-  __TEXT.__objc_methtype: 0x6615
+  __TEXT.__gcc_except_tab: 0x29e4
+  __TEXT.__cstring: 0x1ad24
+  __TEXT.__objc_methname: 0x21a21
+  __TEXT.__objc_methtype: 0x6626
   __TEXT.__swift5_typeref: 0xd0e
   __TEXT.__constg_swiftt: 0xbc4
   __TEXT.__swift5_reflstr: 0x7b7

   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_assocty: 0x60
   __TEXT.__swift5_protos: 0x18
-  __TEXT.__unwind_info: 0x6d20
+  __TEXT.__unwind_info: 0x6d4c
   __TEXT.__eh_frame: 0x3a98
   __DATA_CONST.__auth_got: 0x13f0
-  __DATA_CONST.__got: 0xfd0
+  __DATA_CONST.__got: 0xfd8
   __DATA_CONST.__auth_ptr: 0xb0
-  __DATA_CONST.__const: 0x10f38
-  __DATA_CONST.__cfstring: 0xcbc0
+  __DATA_CONST.__const: 0x10fc8
+  __DATA_CONST.__cfstring: 0xcb80
   __DATA_CONST.__objc_classlist: 0x888
   __DATA_CONST.__objc_catlist: 0x118
   __DATA_CONST.__objc_protolist: 0x200
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x38
-  __DATA_CONST.__objc_classrefs: 0xf78
-  __DATA_CONST.__objc_superrefs: 0x528
-  __DATA_CONST.__objc_arraydata: 0x638
-  __DATA_CONST.__objc_dictobj: 0x2d0
-  __DATA_CONST.__objc_intobj: 0x8b8
+  __DATA_CONST.__objc_classrefs: 0xf80
+  __DATA_CONST.__objc_superrefs: 0x530
+  __DATA_CONST.__objc_arraydata: 0x618
+  __DATA_CONST.__objc_dictobj: 0x280
+  __DATA_CONST.__objc_intobj: 0x8d0
   __DATA_CONST.__objc_arrayobj: 0x288
-  __DATA.__objc_const: 0x21f60
-  __DATA.__objc_selrefs: 0x7ae8
-  __DATA.__objc_ivar: 0x7c8
+  __DATA.__objc_const: 0x21fa0
+  __DATA.__objc_selrefs: 0x7b38
+  __DATA.__objc_ivar: 0x7cc
   __DATA.__objc_data: 0x5d30
   __DATA.__data: 0x3a30
-  __DATA.__bss: 0x1968
+  __DATA.__bss: 0x1978
   __DATA.__common: 0xe0
   - /AppleInternal/Library/Frameworks/TapToRadarKit.framework/TapToRadarKit
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: B6A1BC28-7BC5-3ADB-822B-E0895FA6758A
-  Functions: 8517
-  Symbols:   1560
-  CStrings:  11925
+  UUID: 40508EDE-218E-3DAB-AAA8-EC6D180BD3D9
+  Functions: 8546
+  Symbols:   1562
+  CStrings:  11941
 
Symbols:
+ _GKNewsAppIdentifier
+ _GKNewsGameCenterTesterIdentifier
+ _OBJC_CLASS_$_GKGame
- _FBSOpenApplicationOptionKeyPayloadURL
CStrings:
+ "\x1a"
+ "-[GKAMPController createBagIfNecessary]"
+ "-[GKUtilityService viewableThresholdWithCompletion:]"
+ "B36@0:8B16@20@28"
+ "Cannot get threshold value without a bag."
+ "Cannot setup arcade subscription state without a bag."
+ "Could not create appLaunchTrampolineURL, adamID or bundleID is nil."
+ "Could not launch trampoline, action.appLaunchTrampolineURL is unexpectedly nil."
+ "Creating bag"
+ "GKBulletin handleAction:"
+ "GKBulletin launchBulletinWithCompletionHandler:"
+ "Invoking AppLaunchTrampoline with URL: %@"
+ "LaunchTrampoline"
+ "Launching News puzzles section in response to leaderboard notification action"
+ "NewsApp"
+ "Setting up metrics"
+ "T@\"NSNumber\",&,V_adamID"
+ "T@\"NSString\",&,V_bundleID"
+ "The source app %@ has been allow-listed such that this app will appear as though it were downloaded from the App Store"
+ "This app was not downloaded from the App Store."
+ "_gkAddEntriesFrom:"
+ "appLaunchTrampolineURL"
+ "arcade"
+ "bulletin handle action: %@"
+ "checkAndUpdateArcadeSubscriberStatusWithHandler: Error updating arcade subscription status: %@ "
+ "checkAndUpdateArcadeSubscriberStatusWithHandler: updating arcade subscription state with entitlement %@"
+ "com.apple.Magellan"
+ "createBagIfNecessary"
+ "getBagWithCompletion:"
+ "invokeASCAppLaunchTrampoline failed with error: %@"
+ "isFirstParty:sourceApp:allowList:"
+ "isNewsApp:"
+ "launchBulletinWithCompletionHandler:"
+ "metricsBundleID"
+ "openNewsApp"
+ "reportClickStreamEventWithHostAppBundleId:metricsFields:"
+ "reportMetricsForPresented"
+ "reportMetricsWithEventType:additionalFields:"
+ "reportMetricsWithHostAppBundleId:fields:"
+ "sourceApp"
+ "updateArcadeSubscriptionState:completionHandler:"
+ "v16@?0@\"AMSBag\"8"
- "\x1b"
- "\""
- "%@ doesn't implement %@; dropping action %@"
- "Arcade"
- "GKBulletinController launchBulletin:"
- "GKChallenge Notification: launch appStore: %@"
- "GKLaunchApplicationWithIdentifier: %@"
- "GKRealtimeMultiplayer Notification: launch appStore: %@"
- "LaunchApp"
- "LaunchURL"
- "Launching App: %@"
- "Launching Store: %@"
- "Setting up metrics, will fetch bag: %d"
- "T@\"NSURL\",&,V_storeURL"
- "_storeURL"
- "actionDetails"
- "itms-apps://itunes.apple.com/app/id%@?mt=8"
- "launchBulletin:"
- "openURL: %@"
- "setDefaultActionURL:"
- "setStoreURL:"
- "storeURL"
- "unhandled"
- "updateArcadeSubscriptionState:"

```
