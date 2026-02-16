## Navigation-iOS

> `/System/Library/CoreAccessories/PlugIns/Features/Navigation-iOS.feature/Navigation-iOS`

```diff

-1139.82.1.0.0
-  __TEXT.__text: 0x4748
-  __TEXT.__auth_stubs: 0x480
+1147.100.12.0.0
+  __TEXT.__text: 0x4714
+  __TEXT.__auth_stubs: 0x430
   __TEXT.__objc_methlist: 0x4b4
   __TEXT.__const: 0x158
   __TEXT.__cstring: 0x315
   __TEXT.__oslogstring: 0xa80
-  __TEXT.__unwind_info: 0x138
+  __TEXT.__unwind_info: 0x160
   __TEXT.__objc_classname: 0xd6
   __TEXT.__objc_methname: 0xd59
   __TEXT.__objc_methtype: 0x3e2

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x410
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0x248
+  __AUTH_CONST.__auth_got: 0x220
   __AUTH_CONST.__const: 0x20
   __AUTH_CONST.__cfstring: 0x1a0
   __AUTH_CONST.__objc_const: 0x668

   - /System/Library/PrivateFrameworks/IAP.framework/IAP
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 756BB5BE-F806-3C6D-93F9-CD4B3165DD86
-  Functions: 88
-  Symbols:   497
+  UUID: 2FD2F898-6850-343C-8873-0948F50477E6
+  Functions: 90
+  Symbols:   496
   CStrings:  296
 
Symbols:
+ _OUTLINED_FUNCTION_4
+ _objc_retainAutoreleasedReturnValue
- _objc_claimAutoreleasedReturnValue
- _objc_release_x28
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x2
- _objc_retain_x24
- _objc_retain_x8
Functions:
~ -[ACCNavigationShimAccessory setIap2ShimAccessory:] : 12 -> 64
~ -[ACCNavigationShimAccessory setNavigationAccessory:] : 12 -> 64
~ -[ACCNavigationShim initWithDelegate:] : 156 -> 164
~ -[ACCNavigationShim description] : 120 -> 124
~ -[ACCNavigationShim accessoryAttached:] : 288 -> 280
~ -[ACCNavigationShim accessoryDetached:] : 288 -> 280
~ -[ACCNavigationShim accessoryStartRouteGuidance:componentList:] : 324 -> 304
~ -[ACCNavigationShim accessoryStopRouteGuidance:componentList:] : 324 -> 304
~ -[ACCNavigationShim accessoryNavigation:updateRouteGuidanceInfo:] : 460 -> 452
~ -[ACCNavigationShim accessoryNavigation:updateManeuverInfo:] : 460 -> 452
~ -[ACCNavigationShim convertIAP2ACCRouteGuidanceInfo:forAccessory:] : 352 -> 360
~ -[ACCNavigationShim convertIAP2ACCManeuverInfo:forAccessory:] : 352 -> 360
~ -[ACCNavigationShim getUID] : 8 -> 56
~ -[ACCNavigationShim tryProcessXPCMessage:connection:server:] : 2012 -> 1968
~ _OUTLINED_FUNCTION_0 : 24 -> 72
~ _OUTLINED_FUNCTION_1 : 28 -> 24
~ _OUTLINED_FUNCTION_2 : 28 -> 20
~ _OUTLINED_FUNCTION_3 : 12 -> 20
+ _OUTLINED_FUNCTION_4
~ -[ACCNavigationFeaturePlugin description] : 168 -> 176
~ -[ACCNavigationFeaturePlugin startPlugin] : 816 -> 768
~ -[ACCNavigationFeaturePlugin stopPlugin] : 460 -> 432
~ -[ACCNavigationFeaturePlugin navigation:accessoryAttached:] : 440 -> 416
~ ___59-[ACCNavigationFeaturePlugin navigation:accessoryAttached:]_block_invoke : 872 -> 844
~ -[ACCNavigationFeaturePlugin navigation:accessoryDetached:] : 440 -> 416
~ ___59-[ACCNavigationFeaturePlugin navigation:accessoryDetached:]_block_invoke : 588 -> 592
~ -[ACCNavigationFeaturePlugin navigation:startRouteGuidance:componentList:] : 484 -> 460
~ -[ACCNavigationFeaturePlugin navigation:stopRouteGuidance:componentList:] : 484 -> 460
~ -[ACCNavigationFeaturePlugin navigationShimAccessoryForConnectionID:] : 244 -> 240
~ ___69-[ACCNavigationFeaturePlugin navigationShimAccessoryForConnectionID:]_block_invoke : 80 -> 84
~ -[ACCNavigationFeaturePlugin navigationShimAccessoryList] : 52 -> 56
~ -[ACCNavigationFeaturePlugin updateRouteGuidanceInfo:componentIdList:accessory:] : 492 -> 464
~ ___80-[ACCNavigationFeaturePlugin updateRouteGuidanceInfo:componentIdList:accessory:]_block_invoke : 452 -> 444
~ -[ACCNavigationFeaturePlugin updateManeuverInfo:componentIdList:accessory:] : 492 -> 464
~ ___75-[ACCNavigationFeaturePlugin updateManeuverInfo:componentIdList:accessory:]_block_invoke : 452 -> 444
~ -[ACCNavigationFeaturePlugin notifyNavigationAccessoryClientsOfStateChange] : 108 -> 112
~ -[ACCNavigationFeaturePlugin _navigationShimAccessoryForConnectionIDNoLock:] : 100 -> 108
~ -[ACCNavigationFeaturePlugin setIap2server:] : 12 -> 64
~ -[ACCNavigationFeaturePlugin setNavigationProvider:] : 12 -> 64
~ -[ACCNavigationFeaturePlugin setNavigationQueue:] : 12 -> 64
~ -[ACCNavigationFeaturePlugin setNavigationShim:] : 12 -> 64
~ -[ACCNavigationFeaturePlugin setNavigationShimAccessoryList:] : 12 -> 64
+ _OUTLINED_FUNCTION_3
~ ___80-[ACCNavigationFeaturePlugin updateRouteGuidanceInfo:componentIdList:accessory:]_block_invoke.cold.1 : 112 -> 56
~ -[ACCNavigationShimAccessory create_xpc_representation].cold.2 : 64 -> 56
~ -[ACCNavigationShim tryProcessXPCMessage:connection:server:].cold.3 : 120 -> 92
~ -[ACCNavigationShim tryProcessXPCMessage:connection:server:].cold.5 : 52 -> 44
~ -[ACCNavigationShim tryProcessXPCMessage:connection:server:].cold.7 : 52 -> 44
~ -[ACCNavigationShim tryProcessXPCMessage:connection:server:].cold.9 : 52 -> 44
~ -[ACCNavigationShim tryProcessXPCMessage:connection:server:].cold.11 : 140 -> 112
~ ___59-[ACCNavigationFeaturePlugin navigation:accessoryAttached:]_block_invoke.cold.2 : 124 -> 84
~ ___59-[ACCNavigationFeaturePlugin navigation:accessoryAttached:]_block_invoke.cold.4 : 124 -> 84

```
