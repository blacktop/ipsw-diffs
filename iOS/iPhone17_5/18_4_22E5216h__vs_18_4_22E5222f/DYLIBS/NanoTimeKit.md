## NanoTimeKit

> `/System/Library/PrivateFrameworks/NanoTimeKit.framework/NanoTimeKit`

```diff

-2483.147.62.2.0
-  __TEXT.__text: 0x2c3440
-  __TEXT.__auth_stubs: 0x3800
-  __TEXT.__objc_methlist: 0x2e674
+2483.147.66.0.0
+  __TEXT.__text: 0x2c3ef4
+  __TEXT.__auth_stubs: 0x3810
+  __TEXT.__objc_methlist: 0x2e6ac
   __TEXT.__const: 0x3744
   __TEXT.__gcc_except_tab: 0x6480
-  __TEXT.__cstring: 0x1c75b
-  __TEXT.__oslogstring: 0x1468e
+  __TEXT.__cstring: 0x1c7cb
+  __TEXT.__oslogstring: 0x147fe
   __TEXT.__ustring: 0x456
   __TEXT.__dlopen_cstrs: 0x1ad
   __TEXT.__constg_swiftt: 0x454

   __TEXT.__swift5_reflstr: 0x161
   __TEXT.__swift5_assocty: 0x120
   __TEXT.__swift5_proto: 0x4c
-  __TEXT.__unwind_info: 0xc390
+  __TEXT.__unwind_info: 0xc3b8
   __TEXT.__eh_frame: 0x778
   __TEXT.__objc_classname: 0x82e3
-  __TEXT.__objc_methname: 0x5e83d
+  __TEXT.__objc_methname: 0x5e97b
   __TEXT.__objc_methtype: 0xc88a
-  __TEXT.__objc_stubs: 0x3f380
-  __DATA_CONST.__got: 0x2ff0
-  __DATA_CONST.__const: 0xb790
+  __TEXT.__objc_stubs: 0x3f4c0
+  __DATA_CONST.__got: 0x2ff8
+  __DATA_CONST.__const: 0xb808
   __DATA_CONST.__objc_classlist: 0x1af0
   __DATA_CONST.__objc_catlist: 0xc0
   __DATA_CONST.__objc_protolist: 0x620
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x145e8
+  __DATA_CONST.__objc_selrefs: 0x14638
   __DATA_CONST.__objc_protorefs: 0xc8
-  __DATA_CONST.__objc_superrefs: 0x1500
+  __DATA_CONST.__objc_superrefs: 0x1508
   __DATA_CONST.__objc_arraydata: 0x2bf8
-  __AUTH_CONST.__auth_got: 0x1c18
+  __AUTH_CONST.__auth_got: 0x1c20
   __AUTH_CONST.__auth_ptr: 0x2a0
   __AUTH_CONST.__const: 0x4430
   __AUTH_CONST.__cfstring: 0x20a40
-  __AUTH_CONST.__objc_const: 0x83c60
+  __AUTH_CONST.__objc_const: 0x83c80
   __AUTH_CONST.__objc_intobj: 0x5208
   __AUTH_CONST.__objc_doubleobj: 0x3380
   __AUTH_CONST.__objc_dictobj: 0x410

   __AUTH_CONST.__objc_floatobj: 0x10
   __AUTH.__objc_data: 0xeb88
   __AUTH.__data: 0x2a8
-  __DATA.__objc_ivar: 0x38c0
+  __DATA.__objc_ivar: 0x38c4
   __DATA.__data: 0x4e98
   __DATA.__bss: 0x5600
   __DATA.__common: 0x40

   - /System/Library/PrivateFrameworks/IMFoundation.framework/IMFoundation
   - /System/Library/PrivateFrameworks/IntlPreferences.framework/IntlPreferences
   - /System/Library/PrivateFrameworks/MediaPlaybackCore.framework/MediaPlaybackCore
+  - /System/Library/PrivateFrameworks/MediaRemote.framework/MediaRemote
   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
   - /System/Library/PrivateFrameworks/MobileTimer.framework/MobileTimer
   - /System/Library/PrivateFrameworks/NanoHomeIntents.framework/NanoHomeIntents

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 18411
-  Symbols:   22863
-  CStrings:  23705
+  Functions: 18426
+  Symbols:   22881
+  CStrings:  23726
 
Symbols:
+ _MRMediaRemoteGetProactiveRecommendedPlayer
+ _MRMediaRemoteProactiveRecommendedPlayerDidChangeNotification
CStrings:
+ "%@ Complication does not support current proactiveRecommended '%@', falling back to local"
+ "%@ Complication supports proactiveRecommended '%@'"
+ "%@ Got nil playerPath"
+ "%@ Setting player path to %@"
+ "%@ launchURL (currently playing item) url=%@"
+ "%@ launchURL (no currently playing items) scheme=%@"
+ "%@ proactiveRecommendedPlayerPath nil or unresolved, defaulting to system route"
+ "NTKMediaController (%@):"
+ "_handlePlayerDidChange:"
+ "_loggingPrefix"
+ "_refreshPlayerNotificationName"
+ "_refreshPlayerRequest"
+ "_resolveIntentionalRoutingPlayerPathWithQueue:completion:"
+ "_resolveLegacyPlayerPathWithQueue:completion:"
+ "_resolvePlayerPathWithQueue:completion:"
+ "client"
+ "controller:complicationSupportsPlayer:"
+ "description=NanoTimeKit-2483.147.66"
+ "getProactiveRecommendedRouteWithCompletion:"
+ "isResolved"
+ "setZeroPadTimeSubstringToSeparatorText:"
+ "systemRoute"
+ "v16@?0@\"MPCPlayerPath\"8"
+ "v24@?0@\"MRPlayerPath\"8@\"NSString\"16"
+ "watch_intentional_routing"
- "%02ld"
- "_handleRoutingControllerActiveSystemRouteDidChange:"
- "_updateActiveRoute"
- "description=NanoTimeKit-2483.147.62.2"

```
