## watchlistd

> `/System/Library/PrivateFrameworks/WatchListKit.framework/Support/watchlistd`

```diff

-850.30.4.0.0
-  __TEXT.__text: 0x29350
+850.40.40.0.0
+  __TEXT.__text: 0x29240
   __TEXT.__auth_stubs: 0x780
   __TEXT.__objc_stubs: 0x4ce0
-  __TEXT.__objc_methlist: 0x2138
+  __TEXT.__objc_methlist: 0x252c
   __TEXT.__cstring: 0x413d
   __TEXT.__oslogstring: 0x229e
   __TEXT.__objc_classname: 0x429
-  __TEXT.__objc_methtype: 0xf14
-  __TEXT.__objc_methname: 0x5ad4
+  __TEXT.__objc_methtype: 0xf4a
+  __TEXT.__objc_methname: 0x5af7
   __TEXT.__const: 0x110
-  __TEXT.__gcc_except_tab: 0xdfc
-  __TEXT.__unwind_info: 0xb08
+  __TEXT.__gcc_except_tab: 0xdf4
+  __TEXT.__unwind_info: 0xaf8
   __DATA_CONST.__auth_got: 0x3d0
   __DATA_CONST.__got: 0x4b0
-  __DATA_CONST.__const: 0x13e8
+  __DATA_CONST.__const: 0x1408
   __DATA_CONST.__cfstring: 0x3840
   __DATA_CONST.__objc_classlist: 0x110
   __DATA_CONST.__objc_catlist: 0x10

   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0xe0
   __DATA_CONST.__objc_intobj: 0x48
-  __DATA.__objc_const: 0x4fc0
-  __DATA.__objc_selrefs: 0x19b8
+  __DATA.__objc_const: 0x48b8
+  __DATA.__objc_selrefs: 0x1aa0
   __DATA.__objc_ivar: 0x26c
   __DATA.__objc_data: 0xaa0
   __DATA.__data: 0x4b0

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 4D76F5B3-EF28-3952-A737-2F11B91E1902
-  Functions: 909
-  Symbols:   2567
-  CStrings:  2351
+  UUID: E74359F8-487E-354E-970B-EEFFE9A4B297
+  Functions: 914
+  Symbols:   2581
+  CStrings:  2353
 
Symbols:
+ +[WLDAMSBagObserver sharedObserver].cold.1
+ +[WLDAppVisibilityManager sharedManager].cold.1
+ +[WLDChannelManager defaultChannelManager].cold.1
+ +[WLDFederatedPunchoutReporter sharedFederatedPunchoutReporter].cold.1
+ +[WLDFullTVAppMonitor sharedInstance].cold.1
+ +[WLDPlaybackManager sharedManager].cold.1
+ +[WLDPlaybackReporter _cachedMetadataByIdentifier].cold.1
+ +[WLDPlaybackReporter _cachedNotFoundIdentifiers].cold.1
+ +[WLDServer server].cold.1
+ +[WLDSubscriptionStore sharedInstance].cold.1
+ -[WLDPlaybackNowPlayingObserver _unsupportedMediaTypes].cold.1
+ WLDDispatchQueue.cold.1
+ WLDOperationQueue.cold.1
+ _BagObserverLog.cold.1
CStrings:
+ "@\"NSDictionary\"32@0:8@\"AMSPushPayload\"16@\"NSString\"24"
+ "pushPayload:metricsOverlayForType:"

```
