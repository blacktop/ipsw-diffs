## CarKit

> `/System/Library/PrivateFrameworks/CarKit.framework/CarKit`

```diff

-746.17.0.0.0
-  __TEXT.__text: 0x58908
+746.20.0.0.0
+  __TEXT.__text: 0x58d58
   __TEXT.__auth_stubs: 0xe60
-  __TEXT.__objc_methlist: 0x5d94
-  __TEXT.__const: 0x610
-  __TEXT.__cstring: 0x56b1
-  __TEXT.__oslogstring: 0x63ea
+  __TEXT.__objc_methlist: 0x5dbc
+  __TEXT.__const: 0x620
+  __TEXT.__cstring: 0x56e1
+  __TEXT.__oslogstring: 0x647a
   __TEXT.__gcc_except_tab: 0xa48
   __TEXT.__ustring: 0x24
   __TEXT.__dlopen_cstrs: 0x15e

   __TEXT.__swift5_proto: 0x24
   __TEXT.__swift5_types: 0x1c
   __TEXT.__swift5_fieldmd: 0xac
-  __TEXT.__unwind_info: 0x18f0
-  __TEXT.__objc_classname: 0xae6
-  __TEXT.__objc_methname: 0x10693
-  __TEXT.__objc_methtype: 0x23a6
-  __TEXT.__objc_stubs: 0x9480
+  __TEXT.__unwind_info: 0x18e0
+  __TEXT.__objc_classname: 0xae7
+  __TEXT.__objc_methname: 0x107bf
+  __TEXT.__objc_methtype: 0x23bc
+  __TEXT.__objc_stubs: 0x9580
   __DATA_CONST.__got: 0x788
   __DATA_CONST.__const: 0x1ea8
   __DATA_CONST.__objc_classlist: 0x248
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x170
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3478
+  __DATA_CONST.__objc_selrefs: 0x3498
   __DATA_CONST.__objc_protorefs: 0x100
   __DATA_CONST.__objc_superrefs: 0x1e0
   __DATA_CONST.__objc_arraydata: 0x50
   __AUTH_CONST.__auth_got: 0x740
   __AUTH_CONST.__const: 0x1b50
-  __AUTH_CONST.__cfstring: 0x5920
-  __AUTH_CONST.__objc_const: 0xee08
+  __AUTH_CONST.__cfstring: 0x5960
+  __AUTH_CONST.__objc_const: 0xee98
   __AUTH_CONST.__objc_intobj: 0x108
   __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH.__objc_data: 0x10c0
   __AUTH.__data: 0x58
-  __DATA.__objc_ivar: 0x6fc
-  __DATA.__data: 0x10a8
+  __DATA.__objc_ivar: 0x708
+  __DATA.__data: 0x1098
   __DATA.__bss: 0x8d0
   __DATA.__common: 0x18
   __DATA_DIRTY.__objc_data: 0x690

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: F088E11A-62E5-378D-8C14-01D68B7B2CDD
-  Functions: 2773
-  Symbols:   9096
-  CStrings:  4990
+  UUID: 49484C43-65C8-3015-ACBF-6546031D25D0
+  Functions: 2777
+  Symbols:   9112
+  CStrings:  5007
 
Symbols:
+ -[CARSessionConfiguration supportsPinnedMessages]
+ -[CRCarPlayCapabilities pinnedMessages]
+ -[CRCarPlayCapabilities setPinnedMessages:]
+ -[CRDisplayScaleInfo _scaledToOriginalRatio]
+ -[CRDisplayScaleInfo optimizedPointScaleForMode:]
+ -[CRDisplayScaleInfo preferredPointScaleForMode:]
+ -[CRDisplayScaleInfo preferredToOriginalScaleRatioForMode:]
+ -[CRVehicle pinnedMessagesUserPreference]
+ -[CRVehicle setPinnedMessagesUserPreference:]
+ -[CRVehicle setUserVisibleBrand:]
+ -[CRVehicle userVisibleBrand]
+ GCC_except_table37
+ _OBJC_IVAR_$_CARSessionConfiguration._supportsPinnedMessages
+ _OBJC_IVAR_$_CRCarPlayCapabilities._pinnedMessages
+ _OBJC_IVAR_$_CRVehicle._pinnedMessagesUserPreference
+ _OBJC_IVAR_$_CRVehicle._userVisibleBrand
+ ___63+[CRCarPlayCapabilities waitForCarCapabilitiesValuesWithReply:]_block_invoke.163
+ ___63+[CRCarPlayCapabilities waitForCarCapabilitiesValuesWithReply:]_block_invoke.163.cold.1
+ ___block_literal_global.162
+ ___block_literal_global.230
+ ___block_literal_global.235
+ _objc_msgSend$_scaledToOriginalRatio
+ _objc_msgSend$optimizedPointScaleForMode:
+ _objc_msgSend$pinnedMessages
+ _objc_msgSend$pinnedMessagesUserPreference
+ _objc_msgSend$preferredPointScaleForMode:
+ _objc_msgSend$preferredToOriginalScaleRatioForMode:
+ _objc_msgSend$routeSharingReason
+ _objc_msgSend$setPinnedMessages:
+ _objc_msgSend$setPinnedMessagesUserPreference:
+ _objc_msgSend$setRouteSharingReason:
+ _objc_msgSend$setUserVisibleBrand:
+ _objc_msgSend$userVisibleBrand
- +[CRCarPlayPreferences _boolValueInAirPlayDomainForKey:]
- -[CRCarPlayPreferences isCarPlayRouteSharingEnabled]
- -[CRCarPlayPreferences isCarPlayRouteSharingEnabled].cold.1
- -[CRDisplayScaleInfo optimizedPointScale]
- -[CRDisplayScaleInfo preferredPointScale]
- -[CRDisplayScaleInfo preferredToOriginalScaleRatio]
- -[CRVehicle oemName]
- -[CRVehicle setOemName:]
- _CRPreferencesAirPlayDomain
- _OBJC_IVAR_$_CRVehicle._oemName
- ___63+[CRCarPlayCapabilities waitForCarCapabilitiesValuesWithReply:]_block_invoke.160
- ___63+[CRCarPlayCapabilities waitForCarCapabilitiesValuesWithReply:]_block_invoke.160.cold.1
- ___block_literal_global.159
- ___block_literal_global.232
- ___block_literal_global.243
- ___block_literal_global.248
- _objc_msgSend$_boolValueInAirPlayDomainForKey:
- _objc_msgSend$optimizedPointScale
- _objc_msgSend$preferredPointScale
- _objc_msgSend$preferredToOriginalScaleRatio
CStrings:
+ "%@ (identifier: %@, PPID: %@, pairing: %@, startSessionRequest: %@, cluster{supported: %@ id: %@ versions{ %@, %@}, enhancedIntegration: %@, routeSharing: %@, disabledFeatures: %@, isSiriBargeInDisabled: %@, supportsMixableAudio: %@, albumArtUserPreference: %@,  %@: %@, %@: %@, %@: %@, %@: %@, %@: %@, %@: %@, %@: %@, %@: %@)"
+ "CRCapabilitiesPinnedMessagesKey"
+ "Jumping to 3x scale: pixelSize:%{public}@, ratio: %{public}@"
+ "Optimal size is within 0.05 tolerance AND not equal to the original size AND it's currently ON (new connection) AND the screen is >880x528px, we compare against smaller threshold to use 3x more often"
+ "Q24@0:8q16"
+ "T@\"NSString\",C,N,V_userVisibleBrand"
+ "TB,R,N,V_supportsPinnedMessages"
+ "Tq,N,V_pinnedMessages"
+ "Tq,N,V_pinnedMessagesUserPreference"
+ "_pinnedMessages"
+ "_pinnedMessagesUserPreference"
+ "_scaledToOriginalRatio"
+ "_supportsPinnedMessages"
+ "_userVisibleBrand"
+ "brand"
+ "d24@0:8q16"
+ "optimizedPointScaleForMode:"
+ "pinnedMessages"
+ "pinnedMessagesUserPreference"
+ "preferredPointScaleForMode:"
+ "preferredToOriginalScaleRatioForMode:"
+ "setPinnedMessages:"
+ "setPinnedMessagesUserPreference:"
+ "setUserVisibleBrand:"
+ "supportsPinnedMessages"
+ "userVisibleBrand"
- "%@ (identifier: %@, PPID: %@, pairing: %@, startSessionRequest: %@, cluster{supported: %@ id: %@ versions{ %@, %@}, enhancedIntegration: %@, routeSharing: %@, disabledFeatures: %@, isSiriBargeInDisabled: %@, supportsMixableAudio: %@, albumArtUserPreference: %@, %@: %@, %@: %@, %@: %@, %@: %@, %@: %@, %@: %@, %@: %@)"
- "Jumping to 3x scale: squaredPixelSize:%{self.squaredPixelSize}@, minSize:%{public}@; ratio: %{public}@"
- "T@\"NSString\",C,N,V_oemName"
- "_boolValueInAirPlayDomainForKey:"
- "_oemName"
- "com.apple.airplay"
- "enableCarPlayRouteSharing"
- "isCarPlayRouteSharingEnabled"
- "oemName"
- "optimizedPointScale"
- "preferredPointScale"
- "preferredToOriginalScaleRatio"
- "setOemName:"

```
