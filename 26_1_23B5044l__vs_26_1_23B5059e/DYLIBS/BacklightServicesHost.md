## BacklightServicesHost

> `/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost`

```diff

-5.1.3.0.0
-  __TEXT.__text: 0x89568
+5.1.7.0.0
+  __TEXT.__text: 0x8a184
   __TEXT.__auth_stubs: 0xb10
   __TEXT.__objc_methlist: 0x7bcc
   __TEXT.__const: 0x3b8
-  __TEXT.__gcc_except_tab: 0x1090
-  __TEXT.__cstring: 0x69fb
-  __TEXT.__oslogstring: 0xfdd7
+  __TEXT.__gcc_except_tab: 0x11dc
+  __TEXT.__cstring: 0x6a9c
+  __TEXT.__oslogstring: 0xfaca
   __TEXT.__ustring: 0x328
-  __TEXT.__unwind_info: 0x2298
+  __TEXT.__unwind_info: 0x2310
   __TEXT.__objc_classname: 0x2005
-  __TEXT.__objc_methname: 0x11d7c
+  __TEXT.__objc_methname: 0x11d9f
   __TEXT.__objc_methtype: 0x43e9
-  __TEXT.__objc_stubs: 0xa2c0
+  __TEXT.__objc_stubs: 0xa2e0
   __DATA_CONST.__got: 0x758
-  __DATA_CONST.__const: 0x2600
+  __DATA_CONST.__const: 0x27a8
   __DATA_CONST.__objc_classlist: 0x560
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x2a0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x31a8
+  __DATA_CONST.__objc_selrefs: 0x31b8
   __DATA_CONST.__objc_superrefs: 0x460
   __DATA_CONST.__objc_arraydata: 0x78
   __AUTH_CONST.__auth_got: 0x598
-  __AUTH_CONST.__const: 0xb80
-  __AUTH_CONST.__cfstring: 0x6520
+  __AUTH_CONST.__const: 0xb60
+  __AUTH_CONST.__cfstring: 0x6600
   __AUTH_CONST.__objc_const: 0x13e58
   __AUTH_CONST.__objc_intobj: 0xc0
   __AUTH_CONST.__objc_dictobj: 0x28

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
-  UUID: 2D96E732-084B-373B-8B4E-8723C82738AC
-  Functions: 3376
-  Symbols:   11677
-  CStrings:  5868
+  UUID: B573350E-95C8-3B96-909E-02A78D44000F
+  Functions: 3398
+  Symbols:   11738
+  CStrings:  5885
 
Symbols:
+ -[BLSHBacklightEnvironmentStateMachine _checkCompletedOperationsToBacklightState:transitionState:shouldCompleteTransitionState:setupWithLock:completeWithoutLock:]
+ -[BLSHBacklightEnvironmentStateMachine _descriptionOfTransitionStates:shouldFilter:countOnly:environmentFilter:filter:]
+ -[BLSHBacklightEnvironmentStateMachine _lock_allTransitionsDidBeginUpdateBacklightState:environmentFilter:]
+ -[BLSHBacklightEnvironmentStateMachine _lock_descriptionOfDateSpecifierTransitionStatesShouldFilter:countOnly:]
+ -[BLSHBacklightEnvironmentStateMachine _lock_descriptionOfUpdatingTransitionStatesToBacklightState:shouldFilter:countOnly:]
+ -[BLSHBacklightEnvironmentStateMachine _lock_etsLoggingStringForBacklightState:]
+ -[BLSHBacklightEnvironmentStateMachine _lock_numTransitionsDidNotBeginUpdateBacklightState:]
+ -[BLSHBacklightEnvironmentStateMachine _lock_transitionCompleteAfterCompletingTransitionState:]
+ -[BLSHBacklightEnvironmentStateMachine _lock_transitionStateForEnvironment:]
+ -[BLSHBacklightEnvironmentStateMachine _lock_updateHistory:backlightState:transitionState:pendingTransitionStateCount:]
+ -[BLSHBacklightEnvironmentStateMachine checkCompletedOperationsToBacklightState:visualState:transitionState:isBeginUpdate:]
+ -[BLSHBacklightEnvironmentStateMachine lock_delegate]
+ -[BLSHBacklightFBSceneHostEnvironment sceneDidInvalidate:].cold.1
+ GCC_except_table129
+ GCC_except_table130
+ GCC_except_table131
+ GCC_except_table15
+ GCC_except_table62
+ _OBJC_IVAR_$_BLSHBacklightEnvironmentStateMachine._lock_delegate
+ ___102-[BLSHBacklightEnvironmentStateMachine onMain_performEvent:withInitialSpecifier:performBacklightRamp:]_block_invoke.183
+ ___102-[BLSHBacklightEnvironmentStateMachine onMain_performEvent:withInitialSpecifier:performBacklightRamp:]_block_invoke_2
+ ___102-[BLSHBacklightEnvironmentStateMachine onMain_performEvent:withInitialSpecifier:performBacklightRamp:]_block_invoke_2.cold.1
+ ___102-[BLSHBacklightEnvironmentStateMachine onMain_performEvent:withInitialSpecifier:performBacklightRamp:]_block_invoke_2.cold.2
+ ___102-[BLSHBacklightEnvironmentStateMachine onMain_performEvent:withInitialSpecifier:performBacklightRamp:]_block_invoke_2.cold.3
+ ___119-[BLSHBacklightEnvironmentStateMachine _descriptionOfTransitionStates:shouldFilter:countOnly:environmentFilter:filter:]_block_invoke
+ ___119-[BLSHBacklightEnvironmentStateMachine _descriptionOfTransitionStates:shouldFilter:countOnly:environmentFilter:filter:]_block_invoke_2
+ ___119-[BLSHBacklightEnvironmentStateMachine _descriptionOfTransitionStates:shouldFilter:countOnly:environmentFilter:filter:]_block_invoke_3
+ ___119-[BLSHBacklightEnvironmentStateMachine _descriptionOfTransitionStates:shouldFilter:countOnly:environmentFilter:filter:]_block_invoke_4
+ ___119-[BLSHBacklightEnvironmentStateMachine _descriptionOfTransitionStates:shouldFilter:countOnly:environmentFilter:filter:]_block_invoke_5
+ ___123-[BLSHBacklightEnvironmentStateMachine _lock_descriptionOfUpdatingTransitionStatesToBacklightState:shouldFilter:countOnly:]_block_invoke
+ ___123-[BLSHBacklightEnvironmentStateMachine checkCompletedOperationsToBacklightState:visualState:transitionState:isBeginUpdate:]_block_invoke
+ ___123-[BLSHBacklightEnvironmentStateMachine checkCompletedOperationsToBacklightState:visualState:transitionState:isBeginUpdate:]_block_invoke.229
+ ___80-[BLSHBacklightEnvironmentStateMachine _lock_etsLoggingStringForBacklightState:]_block_invoke
+ ___88-[BLSHBacklightEnvironmentStateMachine onMain_setPresentation:withTargetBacklightState:]_block_invoke.158
+ ___88-[BLSHBacklightEnvironmentStateMachine onMain_setPresentation:withTargetBacklightState:]_block_invoke.164
+ ___92-[BLSHBacklightEnvironmentStateMachine _lock_numTransitionsDidNotBeginUpdateBacklightState:]_block_invoke
+ ___block_descriptor_104_e8_32s40s48s56s64r72r80r88r_e20_v28?0B8B12B16B20B24ls32l8s40l8s48l8r64l8r72l8r80l8r88l8s56l8
+ ___block_descriptor_32_e20_B28?0B8B12B16B20B24l
+ ___block_descriptor_40_e40_B16?0"BLSHEnvironmentTransitionState"8l
+ ___block_descriptor_40_e43_v16?0"<BSDescriptionStringAppendTarget>"8l
+ ___block_descriptor_40_e8_32r_e20_B28?0B8B12B16B20B24lr32l8
+ ___block_descriptor_41_e8_32s_e43_v16?0"<BSDescriptionStringAppendTarget>"8ls32l8
+ ___block_descriptor_48_e8_32r_e43_v16?0"<BSDescriptionStringAppendTarget>"8lr32l8
+ ___block_descriptor_56_e8_32r40r_e43_v16?0"<BSDescriptionStringAppendTarget>"8lr32l8r40l8
+ ___block_descriptor_58_e8_32bs40bs48bs_e5_v8?0ls32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48r_e20_v28?0B8B12B16B20B24lr48l8s32l8s40l8
+ ___block_descriptor_65_e8_32s40s48s_e20_v28?0B8B12B16B20B24ls32l8s40l8s48l8
+ ___block_descriptor_72_e8_32s40r48r56r64r_e20_B28?0B8B12B16B20B24lr40l8r48l8r56l8s32l8r64l8
+ ___block_descriptor_83_e8_32s40s48s56bs64r72r_e5_v8?0ls32l8s56l8r64l8s40l8r72l8s48l8
+ ___block_literal_global.182
+ ___block_literal_global.186
+ ___block_literal_global.231
+ _objc_msgSend$numberWithLong:
- -[BLSHBacklightEnvironmentStateMachine allTransitionsDidBeginUpdateBacklightState:]
- -[BLSHBacklightEnvironmentStateMachine delegate]
- -[BLSHBacklightEnvironmentStateMachine isSetPresentationOperationComplete:]
- -[BLSHBacklightEnvironmentStateMachine isTransitionComplete]
- -[BLSHBacklightEnvironmentStateMachine onMain_setPresentation:withTargetBacklightState:].cold.4
- -[BLSHBacklightEnvironmentStateMachine transitionCompleteAfterCompletingTransitionState:]
- -[BLSHBacklightEnvironmentStateMachine transitionState:didUpdateToDateSpecifier:].cold.1
- -[BLSHBacklightEnvironmentStateMachine withLock_allTransitionsDidBeginUpdateBacklightState:environmentFilter:]
- -[BLSHBacklightEnvironmentStateMachine withLock_numTransitionsDidNotBeginUpdateBacklightState:]
- -[BLSHBacklightEnvironmentStateMachine withLock_transitionStateForEnvironment:]
- _OBJC_IVAR_$_BLSHBacklightEnvironmentStateMachine._delegate
- ___102-[BLSHBacklightEnvironmentStateMachine transitionState:didCompleteUpdateToBacklightState:visualState:]_block_invoke
- ___102-[BLSHBacklightEnvironmentStateMachine transitionState:didCompleteUpdateToBacklightState:visualState:]_block_invoke.202
- ___95-[BLSHBacklightEnvironmentStateMachine withLock_numTransitionsDidNotBeginUpdateBacklightState:]_block_invoke
- ___block_descriptor_32_e40_16?0"BLSHEnvironmentTransitionState"8l
- ___block_descriptor_57_e8_32bs40bs48bs_e5_v8?0ls32l8s40l8s48l8
- ___block_literal_global.177
- ___block_literal_global.201
- ___block_literal_global.204
CStrings:
+ "%s%@"
+ "(%ld)"
+ "(%ld/%ld)"
+ "({%ld}%ld/%ld)"
+ "+"
+ "B16@?0@\"BLSHEnvironmentTransitionState\"8"
+ "B28@?0B8B12B16B20B24"
+ "ESM:%p %s:%{public}@ for:%{public}@ %sets:%{public}@ ∂env:%d ∂begin:%{BOOL}u/%{BOOL}u ∂end:%{BOOL}u/%{BOOL}u ∂pres:%{BOOL}u/%{BOOL}u %{public}@ stale:%{BOOL}u"
+ "ESM:%p (finishing - %s) setPresentation:%p transitionStates:%{public}@"
+ "ESM:%p (performEvent finishing - %s) performEvent:%{public}@ transitionStates:%{public}@ "
+ "ESM:%p (stale) etsUpdateTo:%{public}@ for:%{public}@ ets:%{public}@"
+ "ESM:%p etsUpdateTo:%{public}@ dateMatch:%{BOOL}u for:%{public}@ ets:%{public}@"
+ "ESM:%p finishing (immediate complete - update begin also) setPresentation:%{public}@"
+ "ESM:%p finishing (immediate complete - update end also) setPresentation:%{public}@"
+ "ESM:%p finishing (performEvent immediate begin update) performEvent:%{public}@"
+ "ESM:%p finishing (performEvent immediate complete) performEvent:%{public}@"
+ "ESM:%p finishing (performEvent immediate setPresentation complete) performEvent:%{public}@"
+ "ETS:%p: client disabled:%p, pretending state matches:%{public}@"
+ "T@\"<BLSHBacklightEnvironmentStateMachineDelegate>\",R,W,N,V_lock_delegate"
+ "completed before begun! "
+ "etsDidBeginUpdateTo"
+ "etsDidCompleteUpdateTo"
+ "ev"
+ "lock_delegate"
+ "mismatch"
+ "numberWithLong:"
+ "targ"
+ "v28@?0B8B12B16B20B24"
+ "waiting"
- " (mismatch)"
- "@16@?0@\"BLSHEnvironmentTransitionState\"8"
- "ESM:%p (%p:%{public}@ didCompleteUpdateTo:%{public}@ — %{public}@)%s, transitionStates:%{public}@, tar:%{public}@ peTar:%{public}@ pendingNB:%{BOOL}u ∂Pres:%{BOOL}u ∂:%{BOOL}u stale:%{BOOL}u"
- "ESM:%p (%p:%{public}@ didCompleteUpdateTo:%{public}@) completed before begun (only waiter - will send begun) : %{public}@"
- "ESM:%p (%p:%{public}@ didCompleteUpdateTo:%{public}@) completed before begun : %{public}@"
- "ESM:%p (%p:%{public}@ didCompleteUpdateTo:%{public}@) completed inactive transitionState : %{public}@"
- "ESM:%p (%p:%{public}@ didCompleteUpdateTo:%{public}@) still waiting transitionStates:%{public}@, addingEnvironmentsCount:%d"
- "ESM:%p (didBeginUpdateToBacklightState:%p:%{public}@) still waiting transitionStates:%{public}@, addingEnvironmentsCount:%d"
- "ESM:%p (didBeginUpdateToBacklightState:%p:%{public}@), transitionStates:%{public}@, state:%{public}@ target:%{public}@ performEventTarget:%{public}@ pendingNotifyBegan:%{BOOL}u, updatingPres:%{BOOL}u, updating:%{BOOL}u, transitionState:%{public}@, visualState:%{public}@"
- "ESM:%p (didUpdateToDateSpecifier:%p:%{public}@) still waiting transitionStates:%{public}@"
- "ESM:%p (finishing - %s) performEvent:%{public}@ transitionStates:%{public}@ "
- "ESM:%p (finishing - waiting) setPresentation:%p transitionStates:%{public}@"
- "ESM:%p didUpdateToDateSpecifier:%{public}@ expectedDate:%{BOOL}u transitionState:%{public}@"
- "ESM:%p finishing (immediate begin update) performEvent:%{public}@"
- "ESM:%p finishing (immediate complete - update also) setPresentation:%{public}@"
- "ESM:%p finishing (immediate complete) performEvent:%{public}@"
- "ESM:%p transitionComplete:%{BOOL}u for transitionStateComplete:%{public}@ "
- "ETS:%p: client is disabled for %{public}@, so considering updated to state:%{public}@"
- "T@\"<BLSHBacklightEnvironmentStateMachineDelegate>\",R,W,N,V_delegate"

```
