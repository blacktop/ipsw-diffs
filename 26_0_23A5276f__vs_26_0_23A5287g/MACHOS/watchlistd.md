## watchlistd

> `/System/Library/PrivateFrameworks/WatchListKit.framework/Support/watchlistd`

```diff

-903.0.0.0.0
-  __TEXT.__text: 0x28658
-  __TEXT.__auth_stubs: 0x920
-  __TEXT.__objc_stubs: 0x52e0
-  __TEXT.__objc_methlist: 0x2664
-  __TEXT.__cstring: 0x48c7
-  __TEXT.__oslogstring: 0x26c9
+905.0.0.0.0
+  __TEXT.__text: 0x28e64
+  __TEXT.__auth_stubs: 0x930
+  __TEXT.__objc_stubs: 0x5360
+  __TEXT.__objc_methlist: 0x268c
+  __TEXT.__cstring: 0x484b
+  __TEXT.__oslogstring: 0x2970
   __TEXT.__objc_classname: 0x497
-  __TEXT.__objc_methtype: 0xf79
-  __TEXT.__objc_methname: 0x5fb5
+  __TEXT.__objc_methtype: 0xf98
+  __TEXT.__objc_methname: 0x6060
   __TEXT.__const: 0x130
   __TEXT.__gcc_except_tab: 0xf00
   __TEXT.__unwind_info: 0xb58
-  __DATA_CONST.__auth_got: 0x4a0
+  __DATA_CONST.__auth_got: 0x4a8
   __DATA_CONST.__got: 0x540
-  __DATA_CONST.__const: 0x1320
-  __DATA_CONST.__cfstring: 0x3d00
+  __DATA_CONST.__const: 0x1348
+  __DATA_CONST.__cfstring: 0x3cc0
   __DATA_CONST.__objc_classlist: 0x120
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x60

   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0xf0
   __DATA_CONST.__objc_intobj: 0x60
-  __DATA.__objc_const: 0x4df0
-  __DATA.__objc_selrefs: 0x1c28
+  __DATA.__objc_const: 0x4df8
+  __DATA.__objc_selrefs: 0x1c48
   __DATA.__objc_ivar: 0x27c
   __DATA.__objc_data: 0xb40
   __DATA.__data: 0x510

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 08D8EE05-94A5-3D0C-A8F6-CC8FB5B209E0
-  Functions: 897
-  Symbols:   2694
-  CStrings:  2490
+  UUID: 76BC8A94-F9F6-384C-A09B-260825B4E9B2
+  Functions: 904
+  Symbols:   2707
+  CStrings:  2499
 
Symbols:
+ -[WLDSportsLiveActivityPushHandler handleGameStartNotification:completion:]
+ -[WLDSportsLiveActivityPushHandler handleSentimentNotification:completion:]
+ -[WLDSportsLiveActivityPushHandler shouldSuppressNotificationForCanonicalId:comletion:]
+ _IsSentiment
+ _IsSession
+ __46-[WLDSportsLiveActivityPushHandler connection]_block_invoke.63
+ __98-[WLDSportsLiveActivityPushHandler createLiveActivityForCanonicalId:supplementaryData:completion:]_block_invoke.10
+ ___75-[WLDSportsLiveActivityPushHandler handleGameStartNotification:completion:]_block_invoke
+ ___87-[WLDSportsLiveActivityPushHandler shouldSuppressNotificationForCanonicalId:comletion:]_block_invoke
+ ___block_descriptor_48_e8_32s40bs_e17_v16?0"NSError"8ls32l8s40l8
+ ___block_descriptor_56_e8_32s40r48w_e8_v12?0B8lw48l8s32l8r40l8
+ __block_literal_global.287
+ __block_literal_global.325
+ _objc_msgSend$handleGameStartNotification:completion:
+ _objc_msgSend$handleSentimentNotification:completion:
+ _objc_msgSend$shouldSuppressNotification:completion:
+ _objc_msgSend$shouldSuppressNotificationForCanonicalId:comletion:
+ _objc_retain_x27
- __46-[WLDSportsLiveActivityPushHandler connection]_block_invoke.59
- ___98-[WLDSportsLiveActivityPushHandler createLiveActivityForCanonicalId:supplementaryData:completion:]_block_invoke_2
- ___block_descriptor_56_e8_32s40r48w_e17_v16?0"NSError"8lw48l8s32l8r40l8
- __block_literal_global.293
- __block_literal_global.331
CStrings:
+ "WLDMercuryPushHandler - Ignore Mercury silent push since Badged UM is enabled."
+ "WLDSportsLiveActivityPushHandler - Error creating live activity for canonicalId %@: %@"
+ "WLDSportsLiveActivityPushHandler - Error in XPC connection when creating live activity: %@"
+ "WLDSportsLiveActivityPushHandler - Error in shouldSuppressNotificationForCanonicalId: %@"
+ "WLDSportsLiveActivityPushHandler - Failed to handle game start notification for canonicalID %@: %@"
+ "WLDSportsLiveActivityPushHandler - Sport cannot handle unsupported notification type"
+ "WLDSportsLiveActivityPushHandler - Sports handling Game Start notification"
+ "WLDSportsLiveActivityPushHandler - Sports handling Sentiment notification"
+ "handleGameStartNotification:completion:"
+ "handleSentimentNotification:completion:"
+ "shouldSuppressNotification:completion:"
+ "shouldSuppressNotificationForCanonicalId:comletion:"
+ "v32@0:8@\"NSString\"16@?<v@?B>24"
- "User did not consent to channel with ID %@"
- "WLDPlaybackManager: User did not consent to Channel with ID %@. Ignoring report."

```
