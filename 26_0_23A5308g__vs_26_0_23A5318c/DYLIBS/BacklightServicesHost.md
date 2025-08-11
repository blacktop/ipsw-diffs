## BacklightServicesHost

> `/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost`

```diff

-5.0.62.0.0
-  __TEXT.__text: 0x88d04
+5.0.66.0.0
+  __TEXT.__text: 0x892f0
   __TEXT.__auth_stubs: 0xb10
   __TEXT.__objc_methlist: 0x7bcc
   __TEXT.__const: 0x3b8
   __TEXT.__gcc_except_tab: 0x1090
-  __TEXT.__cstring: 0x69db
-  __TEXT.__oslogstring: 0xfc1f
+  __TEXT.__cstring: 0x69f2
+  __TEXT.__oslogstring: 0xfd87
   __TEXT.__ustring: 0x328
-  __TEXT.__unwind_info: 0x2280
-  __TEXT.__objc_classname: 0x2004
-  __TEXT.__objc_methname: 0x11d05
+  __TEXT.__unwind_info: 0x2290
+  __TEXT.__objc_classname: 0x2005
+  __TEXT.__objc_methname: 0x11d6e
   __TEXT.__objc_methtype: 0x43e9
   __TEXT.__objc_stubs: 0xa2a0
   __DATA_CONST.__got: 0x758
-  __DATA_CONST.__const: 0x25c8
+  __DATA_CONST.__const: 0x2600
   __DATA_CONST.__objc_classlist: 0x560
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x2a0

   __DATA_CONST.__objc_superrefs: 0x460
   __DATA_CONST.__objc_arraydata: 0x78
   __AUTH_CONST.__auth_got: 0x598
-  __AUTH_CONST.__const: 0xba0
+  __AUTH_CONST.__const: 0xb80
   __AUTH_CONST.__cfstring: 0x6520
-  __AUTH_CONST.__objc_const: 0x13d38
+  __AUTH_CONST.__objc_const: 0x13e58
   __AUTH_CONST.__objc_intobj: 0xc0
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_floatobj: 0x10
   __AUTH.__objc_data: 0xeb0
-  __DATA.__objc_ivar: 0xe60
+  __DATA.__objc_ivar: 0xe84
   __DATA.__data: 0x1f80
   __DATA.__bss: 0x98
   __DATA_DIRTY.__objc_data: 0x2710

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
-  UUID: 808106BC-7779-3707-9626-4A845636A0A7
-  Functions: 3354
-  Symbols:   11629
-  CStrings:  5856
+  UUID: 42AF9684-885A-3208-A20A-94C0C82BB65B
+  Functions: 3375
+  Symbols:   11674
+  CStrings:  5865
 
Symbols:
+ -[BLSHBacklightFBSceneHostEnvironment copyRenderSeedToSettings:]
+ -[BLSHBacklightFBSceneHostEnvironment incrementRenderSeed]
+ -[BLSHBacklightFBSceneHostEnvironment setAlwaysOnEnabledForEnvironment:].cold.1
+ -[BLSHBacklightFBSceneHostEnvironment setAlwaysOnEnabledForEnvironment:forwardedToSettings:]
+ -[BLSHBacklightFBSceneHostEnvironment setClientActive:forwardedToSettings:]
+ -[BLSHBacklightFBSceneHostEnvironment setLiveUpdating:].cold.1
+ -[BLSHBacklightFBSceneHostEnvironment setLiveUpdating:forwardedToSettings:]
+ -[BLSHBacklightFBSceneHostEnvironment setPresentationDate:forwardedToSettings:]
+ -[BLSHBacklightFBSceneHostEnvironment setUnrestrictedFramerateUpdates:].cold.1
+ -[BLSHBacklightFBSceneHostEnvironment setUnrestrictedFramerateUpdates:forwardedToSettings:]
+ -[BLSHBacklightFBSceneHostEnvironment setVisualState:forwardedToSettings:]
+ -[BLSHBacklightFBSceneHostEnvironment update1HzFlipbookForClientSettingChange]
+ -[BLSHBacklightFBSceneHostEnvironment updateClientHasDelegateFromClientSettings]
+ -[BLSHBacklightFBSceneHostEnvironment updateClientSupportsAlwaysOnFromClientSettings]
+ GCC_except_table75
+ _OBJC_IVAR_$_BLSHBacklightFBSceneHostEnvironment._lock_alwaysOnEnabledForEnvironment
+ _OBJC_IVAR_$_BLSHBacklightFBSceneHostEnvironment._lock_clientActive
+ _OBJC_IVAR_$_BLSHBacklightFBSceneHostEnvironment._lock_clientAlwaysOnContentIs1hz
+ _OBJC_IVAR_$_BLSHBacklightFBSceneHostEnvironment._lock_clientHasDelegate
+ _OBJC_IVAR_$_BLSHBacklightFBSceneHostEnvironment._lock_clientSupportsAlwaysOn
+ _OBJC_IVAR_$_BLSHBacklightFBSceneHostEnvironment._lock_liveUpdating
+ _OBJC_IVAR_$_BLSHBacklightFBSceneHostEnvironment._lock_presentationDate
+ _OBJC_IVAR_$_BLSHBacklightFBSceneHostEnvironment._lock_unrestrictedFramerateUpdates
+ _OBJC_IVAR_$_BLSHBacklightFBSceneHostEnvironment._lock_visualState
+ ___102-[BLSHBacklightEnvironmentStateMachine transitionState:didCompleteUpdateToBacklightState:visualState:]_block_invoke.199
+ ___124-[BLSHBacklightFBSceneHostEnvironment requestDateSpecifiersForDateInterval:previousPresentationDate:shouldReset:completion:]_block_invoke.90
+ ___124-[BLSHBacklightFBSceneHostEnvironment requestDateSpecifiersForDateInterval:previousPresentationDate:shouldReset:completion:]_block_invoke.93
+ ___183-[BLSHBacklightFBSceneHostEnvironment updateToVisualState:presentationDateSpecifier:animated:triggerEvent:touchTargetable:sceneContentsUpdated:performBacklightRamp:animationComplete:]_block_invoke.66
+ ___183-[BLSHBacklightFBSceneHostEnvironment updateToVisualState:presentationDateSpecifier:animated:triggerEvent:touchTargetable:sceneContentsUpdated:performBacklightRamp:animationComplete:]_block_invoke.75
+ ___183-[BLSHBacklightFBSceneHostEnvironment updateToVisualState:presentationDateSpecifier:animated:triggerEvent:touchTargetable:sceneContentsUpdated:performBacklightRamp:animationComplete:]_block_invoke.75.cold.1
+ ___183-[BLSHBacklightFBSceneHostEnvironment updateToVisualState:presentationDateSpecifier:animated:triggerEvent:touchTargetable:sceneContentsUpdated:performBacklightRamp:animationComplete:]_block_invoke.79
+ ___183-[BLSHBacklightFBSceneHostEnvironment updateToVisualState:presentationDateSpecifier:animated:triggerEvent:touchTargetable:sceneContentsUpdated:performBacklightRamp:animationComplete:]_block_invoke.79.cold.1
+ ___183-[BLSHBacklightFBSceneHostEnvironment updateToVisualState:presentationDateSpecifier:animated:triggerEvent:touchTargetable:sceneContentsUpdated:performBacklightRamp:animationComplete:]_block_invoke.83
+ ___183-[BLSHBacklightFBSceneHostEnvironment updateToVisualState:presentationDateSpecifier:animated:triggerEvent:touchTargetable:sceneContentsUpdated:performBacklightRamp:animationComplete:]_block_invoke.83.cold.1
+ ___82-[BLSHBacklightFBSceneHostEnvironment updateToDateSpecifier:sceneContentsUpdated:]_block_invoke.104
+ ___82-[BLSHBacklightFBSceneHostEnvironment updateToDateSpecifier:sceneContentsUpdated:]_block_invoke.104.cold.1
+ ___block_descriptor_40_e8_32s_e33_v16?0"FBSMutableSceneSettings"8ls32l8
+ ___block_descriptor_41_e8_32s_e33_v16?0"FBSMutableSceneSettings"8ls32l8
+ ___block_descriptor_56_e8_32s40s48s_e33_v16?0"FBSMutableSceneSettings"8ls32l8s40l8s48l8
+ ___block_descriptor_72_e8_32s40s48s56s64bs_e60_"FBSSceneTransitionContext"16?0"FBSMutableSceneSettings"8ls32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_98_e8_32s40s48s56s64s72bs80bs88bs_e60_"FBSSceneTransitionContext"16?0"FBSMutableSceneSettings"8ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8
+ ___block_literal_global.176
+ ___block_literal_global.180
+ ___block_literal_global.198
+ ___block_literal_global.201
+ ___block_literal_global.96
- -[BLSHBacklightFBSceneHostEnvironment update1HzFlipbookForSettingChange]
- GCC_except_table65
- ___102-[BLSHBacklightEnvironmentStateMachine transitionState:didCompleteUpdateToBacklightState:visualState:]_block_invoke.198
- ___124-[BLSHBacklightFBSceneHostEnvironment requestDateSpecifiersForDateInterval:previousPresentationDate:shouldReset:completion:]_block_invoke.92
- ___124-[BLSHBacklightFBSceneHostEnvironment requestDateSpecifiersForDateInterval:previousPresentationDate:shouldReset:completion:]_block_invoke.95
- ___179-[BLSHBacklightEnvironmentStateMachine updateTransitionStatesForEnvironments:toBacklightState:forEvent:withInitialSpecifier:forReason:performBacklightRamp:environmentTransformer:]_block_invoke.cold.1
- ___183-[BLSHBacklightFBSceneHostEnvironment updateToVisualState:presentationDateSpecifier:animated:triggerEvent:touchTargetable:sceneContentsUpdated:performBacklightRamp:animationComplete:]_block_invoke.68
- ___183-[BLSHBacklightFBSceneHostEnvironment updateToVisualState:presentationDateSpecifier:animated:triggerEvent:touchTargetable:sceneContentsUpdated:performBacklightRamp:animationComplete:]_block_invoke.68.cold.1
- ___183-[BLSHBacklightFBSceneHostEnvironment updateToVisualState:presentationDateSpecifier:animated:triggerEvent:touchTargetable:sceneContentsUpdated:performBacklightRamp:animationComplete:]_block_invoke.77
- ___183-[BLSHBacklightFBSceneHostEnvironment updateToVisualState:presentationDateSpecifier:animated:triggerEvent:touchTargetable:sceneContentsUpdated:performBacklightRamp:animationComplete:]_block_invoke.77.cold.1
- ___183-[BLSHBacklightFBSceneHostEnvironment updateToVisualState:presentationDateSpecifier:animated:triggerEvent:touchTargetable:sceneContentsUpdated:performBacklightRamp:animationComplete:]_block_invoke.81
- ___183-[BLSHBacklightFBSceneHostEnvironment updateToVisualState:presentationDateSpecifier:animated:triggerEvent:touchTargetable:sceneContentsUpdated:performBacklightRamp:animationComplete:]_block_invoke.81.cold.1
- ___183-[BLSHBacklightFBSceneHostEnvironment updateToVisualState:presentationDateSpecifier:animated:triggerEvent:touchTargetable:sceneContentsUpdated:performBacklightRamp:animationComplete:]_block_invoke.85
- ___183-[BLSHBacklightFBSceneHostEnvironment updateToVisualState:presentationDateSpecifier:animated:triggerEvent:touchTargetable:sceneContentsUpdated:performBacklightRamp:animationComplete:]_block_invoke.85.cold.1
- ___60-[BLSHBacklightFBSceneHostEnvironment clearPresentationDate]_block_invoke.cold.1
- ___82-[BLSHBacklightFBSceneHostEnvironment updateToDateSpecifier:sceneContentsUpdated:]_block_invoke.106
- ___82-[BLSHBacklightFBSceneHostEnvironment updateToDateSpecifier:sceneContentsUpdated:]_block_invoke.106.cold.1
- ___82-[BLSHBacklightFBSceneHostEnvironment updateToDateSpecifier:sceneContentsUpdated:]_block_invoke.cold.1
- ___block_descriptor_106_e8_32s40s48s56s64s72bs80bs88bs_e60_"FBSSceneTransitionContext"16?0"FBSMutableSceneSettings"8ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8
- ___block_descriptor_32_e33_v16?0"FBSMutableSceneSettings"8l
- ___block_descriptor_33_e33_v16?0"FBSMutableSceneSettings"8l
- ___block_descriptor_80_e8_32s40s48s56s64bs_e60_"FBSSceneTransitionContext"16?0"FBSMutableSceneSettings"8ls32l8s40l8s48l8s56l8s64l8
- ___block_literal_global.174
- ___block_literal_global.178
- ___block_literal_global.197
- ___block_literal_global.200
- ___block_literal_global.98
CStrings:
+ "%p:%{public}@ scene nil, will not setAlwaysOnEnabledForEnvironment:%{BOOL}u"
+ "%p:%{public}@ scene nil, will not setLiveUpdating:%{BOOL}u"
+ "%p:%{public}@ scene nil, will not setUnrestrictedFramerateUpdates:%{BOOL}u"
+ "(OBSOLETE - ignoring) "
+ "ESM: %supdateTransitionStatesForEnvironments: -> %@ environment %@: %@"
+ "OSIP:%p disableSuppression set to YES - use 'login -f mobile defaults delete com.apple.BacklightServices disableSuppression' to remove"
+ "OSIP:%p startup cbDisplayMode:%{public}@ dsao:%{BOOL}u dsaof:%{BOOL}u dscs:%{BOOL}u sup:%{BOOL}u"
+ "_lock_clientActive"
+ "_lock_clientAlwaysOnContentIs1hz"
+ "_lock_clientHasDelegate"
+ "_lock_clientSupportsAlwaysOn"
- "ESM: updateTransitionStatesForEnvironments: -> %@ environment %@: %@"
- "OSIP:%p startup cbDisplayMode:%{public}@ dsao:%{BOOL}u dsaof:%{BOOL}u dscs:%{BOOL}u"

```
