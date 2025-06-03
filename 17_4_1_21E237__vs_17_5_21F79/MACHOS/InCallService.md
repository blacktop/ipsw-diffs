## InCallService

> `/Applications/InCallService.app/InCallService`

```diff

-2869.500.151.2.3
-  __TEXT.__text: 0x177048
+2869.600.72.2.3
+  __TEXT.__text: 0x177c58
   __TEXT.__auth_stubs: 0x3db0
-  __TEXT.__objc_stubs: 0x266c0
-  __TEXT.__objc_methlist: 0x10f58
-  __TEXT.__cstring: 0xdc4d
-  __TEXT.__objc_methname: 0x398f3
+  __TEXT.__objc_stubs: 0x26800
+  __TEXT.__objc_methlist: 0x10fd8
+  __TEXT.__cstring: 0xdc7d
+  __TEXT.__objc_methname: 0x39b27
   __TEXT.__objc_classname: 0x2147
-  __TEXT.__objc_methtype: 0x7d52
+  __TEXT.__objc_methtype: 0x7da7
   __TEXT.__const: 0x3ed4
-  __TEXT.__oslogstring: 0x14425
-  __TEXT.__gcc_except_tab: 0x11c0
+  __TEXT.__oslogstring: 0x14485
+  __TEXT.__gcc_except_tab: 0x1200
   __TEXT.__ustring: 0x4
   __TEXT.__dlopen_cstrs: 0x109
   __TEXT.__constg_swiftt: 0x22d4

   __TEXT.__swift5_types: 0x1e8
   __TEXT.__swift5_mpenum: 0x10
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0x5cd0
+  __TEXT.__unwind_info: 0x5d24
   __TEXT.__eh_frame: 0x20e0
   __DATA_CONST.__auth_got: 0x1ee8
   __DATA_CONST.__got: 0xe90
   __DATA_CONST.__auth_ptr: 0x130
-  __DATA_CONST.__const: 0x7430
+  __DATA_CONST.__const: 0x7530
   __DATA_CONST.__cfstring: 0x7220
   __DATA_CONST.__objc_classlist: 0x740
   __DATA_CONST.__objc_catlist: 0x128

   __DATA_CONST.__objc_arrayobj: 0x3c0
   __DATA_CONST.__objc_floatobj: 0xc0
   __DATA_CONST.__objc_doubleobj: 0x40
-  __DATA.__objc_const: 0x219c0
-  __DATA.__objc_selrefs: 0xba00
-  __DATA.__objc_ivar: 0xfc0
+  __DATA.__objc_const: 0x21a28
+  __DATA.__objc_selrefs: 0xba60
+  __DATA.__objc_ivar: 0xfc8
   __DATA.__objc_data: 0x6a80
   __DATA.__data: 0x5a20
   __DATA.__bss: 0x4030

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 5550C51E-F0A5-3E11-9EC4-EFD8DA922C2D
-  Functions: 9660
+  UUID: 317602B9-9C18-3882-8DAC-D5D9B58E0584
+  Functions: 9679
   Symbols:   2101
-  CStrings:  13415
+  CStrings:  13438
 
CStrings:
+ "(disconnectedCall.contactIdentifiers.count: %lu && \n\n !(disconnectedCall.isOutgoing: %d && disconnectedCall.dateConnected: %@) && \n\n disconnectedCall.provider.isFaceTimeProvider: %d \n\n [[FTDeviceSupport sharedInstance] isGreenTea]) : %d"
+ "@20@0:8S16"
+ "@24@0:8S16B20"
+ "PHAudioDeviceController.serialQueue"
+ "SNAP: Adding default backgroundGradientView"
+ "SNAP: Fading out poster, but there is no contact image data either, setting up default blur background in this case"
+ "SNAP: Removing default backgroundGradientView"
+ "SNAP: update backgroundContactImageView withImage: %@"
+ "Setting preferredBannerHeight based on productType %ld"
+ "T@\"TUCallCenter\",R,N,V_fetchRoutesBackgroundCallCenter"
+ "TB,N,V_hasKeypadUpdated"
+ "_fetchRoutesBackgroundCallCenter"
+ "_hasKeypadUpdated"
+ "_pickableRoutesUsingBackgroundQueue:"
+ "_unformattedPickableRoutesForAudioSessionCategory:usingBackgroundQueue:"
+ "callForPickableRoutesUsingBackgroundQueue:"
+ "emojiViewController"
+ "fetchMenuActionsWithCompletionHandler:"
+ "fetchRoutesBackgroundCallCenter"
+ "fetchRoutesForAudioRoutingMenuController:completionHandler:"
+ "fetchRoutesWithCompletionHandler:"
+ "hasKeypadUpdated"
+ "initWithQueue:wantsCallNotifications:"
+ "menuActionsWithRoutes:"
+ "removeNameLabelForAlwaysOnDisplay"
+ "setHasKeypadUpdated:"
+ "v32@0:8@\"PHAudioRoutingMenuController\"16@?<v@?@\"NSArray\">24"
- "(disconnectedCall.contactIdentifiers.count: %lu && \n\n !(disconnectedCall.isOutgoing: %d && disconnectedCall.dateConnected: %@) && \n\n disconnectedCall.provider.isFaceTimeProvider: %d \n\n [_featureFlags callEndedUIBlockAndReportEnabled] : %d && \n\n [[FTDeviceSupport sharedInstance] isGreenTea]) : %d"
- "callEndedUIBlockAndReportEnabled"
- "callEndedUIBlockAndReportEnabled is not enabled, so we don't show the end call screen"
- "isMessagingAllowed returning false due to the call being a branded call."

```
