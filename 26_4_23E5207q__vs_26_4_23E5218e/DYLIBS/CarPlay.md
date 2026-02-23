## CarPlay

> `/System/Library/Frameworks/CarPlay.framework/CarPlay`

```diff

-515.10.1.0.0
-  __TEXT.__text: 0x68a6c
-  __TEXT.__auth_stubs: 0xc20
-  __TEXT.__objc_methlist: 0x8980
+515.14.1.0.0
+  __TEXT.__text: 0x68be0
+  __TEXT.__auth_stubs: 0xc30
+  __TEXT.__objc_methlist: 0x89a0
   __TEXT.__const: 0x532
   __TEXT.__cstring: 0x4ee6
   __TEXT.__oslogstring: 0x2dab

   __TEXT.__swift5_fieldmd: 0x7c
   __TEXT.__unwind_info: 0x1f30
   __TEXT.__objc_classname: 0x127b
-  __TEXT.__objc_methname: 0x11eeb
-  __TEXT.__objc_methtype: 0x2c87
-  __TEXT.__objc_stubs: 0xaee0
+  __TEXT.__objc_methname: 0x11f8b
+  __TEXT.__objc_methtype: 0x2d49
+  __TEXT.__objc_stubs: 0xaf20
   __DATA_CONST.__got: 0x7f0
-  __DATA_CONST.__const: 0x1de8
+  __DATA_CONST.__const: 0x1df0
   __DATA_CONST.__objc_classlist: 0x390
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x2d8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3bb8
+  __DATA_CONST.__objc_selrefs: 0x3bd8
   __DATA_CONST.__objc_protorefs: 0x158
   __DATA_CONST.__objc_superrefs: 0x2e8
-  __AUTH_CONST.__auth_got: 0x620
+  __AUTH_CONST.__auth_got: 0x628
   __AUTH_CONST.__const: 0xae8
-  __AUTH_CONST.__cfstring: 0x4c00
-  __AUTH_CONST.__objc_const: 0x1ec28
+  __AUTH_CONST.__cfstring: 0x4be0
+  __AUTH_CONST.__objc_const: 0x1ec48
   __AUTH_CONST.__objc_intobj: 0xd8
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH.__objc_data: 0x1ce0

   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib
+  - /usr/lib/swift/libswiftSpatial.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 42F93BA0-3B04-32A7-A44E-4E360956AA6B
-  Functions: 3012
-  Symbols:   11218
-  CStrings:  5028
+  UUID: 556EE648-153E-308E-95F2-AB48493D7144
+  Functions: 3013
+  Symbols:   11225
+  CStrings:  5035
 
Symbols:
+ +[CPListTemplateDetailsHeader maximumActionButtonCount]
+ _CMTimeMakeWithSeconds
+ __swift_FORCE_LOAD_$_swiftSpatial
+ __swift_FORCE_LOAD_$_swiftSpatial_$_CarPlay
+ _objc_msgSend$layoutDirection
+ _objc_msgSend$setLayoutDirection:
Functions:
~ -[CPNavigationManager _showRouteSharingPopoverIfNecessaryForVehicle:] : 580 -> 640
+ +[CPListTemplateDetailsHeader maximumActionButtonCount]
~ ___53-[CPTemplateApplicationScene _refreshTraitCollection]_block_invoke : 180 -> 240
~ -[CPPlaybackConfiguration initWithPreferredPresentation:playbackState:progress:duration:] : 192 -> 228
~ -[CPPlaybackConfiguration initWithPreferredPresentation:playbackState:elapsedTime:duration:] : 260 -> 300
~ -[CPPlaybackConfiguration initWithPreferredPresentation:playbackAction:elapsedTime:duration:] : 252 -> 316
~ -[CPPlaybackConfiguration encodeWithCoder:] : 240 -> 232
~ -[CPPlaybackConfiguration copyWithZone:] : 144 -> 152
~ -[CPPlaybackConfiguration isEqual:] : 252 -> 308
~ -[CPPlaybackConfiguration hash] : 92 -> 112
~ -[CPPlaybackConfiguration duration] : 8 -> 20
~ _$s7CarPlay17RouteSharingStateC14ownsNavigationSbvW : 672 -> 676
~ _$s7CarPlay17RouteSharingStateC20currentLegIdentifier10Foundation4UUIDVSgvW : 1296 -> 1276
~ _$sSo21CPVehicleStateManagerC7CarPlayE30willReleaseNavigationOwnership9lastOwnerySb_tF : 616 -> 608
~ _$sSo21CPVehicleStateManagerC7CarPlayE28didUpdateNavigationOwnershipyyF : 1428 -> 1440
~ _$sSo21CPVehicleStateManagerC7CarPlayE4send9routeLineySo013CPBridgeRouteH0_pSg_tF : 7120 -> 7124
~ _$sSo21CPVehicleStateManagerC7CarPlayE17sendRoutingStates33_8CF23B4C98753B3B7E23CE4A41E0DBB4LLyyF : 2060 -> 2064
~ _$sSo21CPVehicleStateManagerC7CarPlayE23carDidUpdateAccessoriesyySo6CAFCarCF : 1208 -> 1224
CStrings:
+ "@80@0:8q16q24{?=qiIq}32{?=qiIq}56"
+ "T{?=qiIq},R,N,V_duration"
+ "carDidNotify:accessory:service:control:withValue:"
+ "layoutDirection"
+ "serviceDidNotify:control:withValue:"
+ "setLayoutDirection:"
+ "v40@0:8@\"CAFService\"16@\"CAFControl\"24@\"NSDictionary\"32"
+ "v56@0:8@\"CAFCar\"16@\"CAFAccessory\"24@\"CAFService\"32@\"CAFControl\"40@\"NSDictionary\"48"
+ "v56@0:8@16@24@32@40@48"
- "0"

```
