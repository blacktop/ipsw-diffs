## watchlistd

> `/System/Library/PrivateFrameworks/WatchListKit.framework/Support/watchlistd`

```diff

-850.30.4.0.0
-  __TEXT.__text: 0x27a54
-  __TEXT.__auth_stubs: 0x940
+850.40.37.0.1
+  __TEXT.__text: 0x27928
+  __TEXT.__auth_stubs: 0x950
   __TEXT.__objc_stubs: 0x5160
-  __TEXT.__objc_methlist: 0x2238
+  __TEXT.__objc_methlist: 0x263c
   __TEXT.__cstring: 0x46e4
   __TEXT.__oslogstring: 0x2497
   __TEXT.__objc_classname: 0x497

   __TEXT.__const: 0x128
   __TEXT.__gcc_except_tab: 0xedc
   __TEXT.__dlopen_cstrs: 0x5a
-  __TEXT.__unwind_info: 0xb60
-  __DATA_CONST.__auth_got: 0x4b0
+  __TEXT.__unwind_info: 0xb48
+  __DATA_CONST.__auth_got: 0x4b8
   __DATA_CONST.__got: 0x558
-  __DATA_CONST.__const: 0x1378
+  __DATA_CONST.__const: 0x1398
   __DATA_CONST.__cfstring: 0x3bc0
   __DATA_CONST.__objc_classlist: 0x120
   __DATA_CONST.__objc_catlist: 0x10

   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0xf0
   __DATA_CONST.__objc_intobj: 0x60
-  __DATA.__objc_const: 0x5530
-  __DATA.__objc_selrefs: 0x1ae0
+  __DATA.__objc_const: 0x4de8
+  __DATA.__objc_selrefs: 0x1bb8
   __DATA.__objc_ivar: 0x27c
   __DATA.__objc_data: 0xb40
   __DATA.__data: 0x510

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 892
-  Symbols:   2679
+  Functions: 897
+  Symbols:   2694
   CStrings:  1987
 
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
+ _objc_retainAutoreleasedReturnValue

```
