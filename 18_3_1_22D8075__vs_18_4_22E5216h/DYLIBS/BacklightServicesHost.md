## BacklightServicesHost

> `/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost`

```diff

-4.2.19.2.0
-  __TEXT.__text: 0x863b0
-  __TEXT.__auth_stubs: 0xa80
-  __TEXT.__objc_methlist: 0x60b8
-  __TEXT.__const: 0x398
-  __TEXT.__gcc_except_tab: 0xff4
-  __TEXT.__cstring: 0x6539
-  __TEXT.__oslogstring: 0xf0b9
+4.4.30.0.0
+  __TEXT.__text: 0x86158
+  __TEXT.__auth_stubs: 0xa90
+  __TEXT.__objc_methlist: 0x798c
+  __TEXT.__const: 0x3b8
+  __TEXT.__gcc_except_tab: 0x10ac
+  __TEXT.__cstring: 0x66c7
+  __TEXT.__oslogstring: 0xf51b
   __TEXT.__ustring: 0x2fe
-  __TEXT.__unwind_info: 0x2168
-  __TEXT.__objc_classname: 0x1f66
-  __TEXT.__objc_methname: 0x11229
-  __TEXT.__objc_methtype: 0x41fd
-  __TEXT.__objc_stubs: 0x9d20
-  __DATA_CONST.__got: 0x760
-  __DATA_CONST.__const: 0x2440
-  __DATA_CONST.__objc_classlist: 0x540
+  __TEXT.__unwind_info: 0x21a8
+  __TEXT.__objc_classname: 0x1fc5
+  __TEXT.__objc_methname: 0x11518
+  __TEXT.__objc_methtype: 0x42c5
+  __TEXT.__objc_stubs: 0x9f40
+  __DATA_CONST.__got: 0x768
+  __DATA_CONST.__const: 0x2500
+  __DATA_CONST.__objc_classlist: 0x550
   __DATA_CONST.__objc_catlist: 0x30
-  __DATA_CONST.__objc_protolist: 0x298
+  __DATA_CONST.__objc_protolist: 0x2a0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2ef0
-  __DATA_CONST.__objc_superrefs: 0x448
+  __DATA_CONST.__objc_selrefs: 0x3090
+  __DATA_CONST.__objc_superrefs: 0x458
   __DATA_CONST.__objc_arraydata: 0x78
-  __AUTH_CONST.__auth_got: 0x550
+  __AUTH_CONST.__auth_got: 0x558
   __AUTH_CONST.__const: 0xb40
-  __AUTH_CONST.__cfstring: 0x60c0
-  __AUTH_CONST.__objc_const: 0x15e40
+  __AUTH_CONST.__cfstring: 0x62e0
+  __AUTH_CONST.__objc_const: 0x138c8
   __AUTH_CONST.__objc_intobj: 0xc0
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_floatobj: 0x10
   __AUTH.__objc_data: 0xf0
-  __DATA.__objc_ivar: 0xddc
-  __DATA.__data: 0x1f20
+  __DATA.__objc_ivar: 0xe20
+  __DATA.__data: 0x1f80
   __DATA.__bss: 0x90
-  __DATA_DIRTY.__objc_data: 0x3390
+  __DATA_DIRTY.__objc_data: 0x3430
   __DATA_DIRTY.__bss: 0xf8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreMotion.framework/CoreMotion

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
-  Functions: 3136
-  Symbols:   3822
-  CStrings:  4923
+  Functions: 3275
+  Symbols:   3928
+  CStrings:  4988
 
Symbols:
+ _OBJC_CLASS_$_BLSHEngineEnvironmentObserverHelper
+ _OBJC_METACLASS_$_BLSHEngineEnvironmentObserverHelper
+ _objc_retainAutoreleasedReturnValue
CStrings:
+ "\x04\x12"
+ "\x06\x14R"
+ "\a\x12\x11"
+ "\x13\x12\x11Q"
+ "\x1f\f"
+ "%@ for <%@: %p>"
+ "%p -[CAFlipBook cancel] error:%{public}@ (took %.5fs.)"
+ "%p -[CAFlipBook cancel] took %.5fs. Dupe of rdar://78634442?"
+ "%p device does not support flipbook"
+ "%p no environment found for sceneToken:%{public}@ handler:%{public}@ will not activate for:%{public}@"
+ "%p no environment found for sceneToken:%{public}@ handler:%{public}@ will not deactivate for:%{public}@"
+ "%p updates(%d) (%d limit reached - stopping) previous:%{public}@ earliest:%@ latest:%@ valid:(%{public}@->%{public}@) (initial:%{BOOL}u) startingAtDate:%{public}@ gapDuration:%1.3lg"
+ "%p updates(%d) (invalid - stopping) valid:(%{public}@->%{public}@) earliestDate:%{public}@"
+ "%p updates(%d) startDate->lastValidDate interval too small (<%.lfs) startDate:%{public}@ lastValidDate:%{public}@"
+ "%p will reset all budgets for reason:%{public}@"
+ "%p:%{public}@ invalidated content will not invalidate flipbook (not in presentation) for source:%{public}@ reason:%{public}@ environment:%{public}@"
+ "%p:%{public}@ will clear %d specifiers from interval:%{public}@ (%{public}@)"
+ "@\"<BLSHBacklightSceneHostEnvironmentObserver>\""
+ "@\"<BLSHRenderedFlipbookFrame>\"24@0:8^@16"
+ "@\"BLSHEngineEnvironmentObserverHelper\""
+ "@24@0:8^@16"
+ "@40@0:8@16d24@32"
+ "A"
+ "BLSHDateSpecifierModelObserving"
+ "BLSHEngineEnvironmentObserverHelper"
+ "BLSHEngineEnvironmentObserverHelper.m"
+ "BLSHLocalHostSceneEnvironmentUpdaterBudget"
+ "BLSHLongHeldAssertion"
+ "BLSHServiceBudget"
+ "BacklightEvent"
+ "RequestDates"
+ "T@\"BLSHDateSpecifierModel\",&,N"
+ "TB,?,GisHighLuminanceAlwaysOn,V_lock_highLuminanceAlwaysOn"
+ "Td,R,V_activeDuration"
+ "[self identifier]"
+ "_activeDuration"
+ "_description"
+ "_engine"
+ "_environmentObserverHelper"
+ "_lock_flipbookPowerSavingAssertion"
+ "_lock_longHeldAssertionHistory"
+ "_lock_modelEnvironments"
+ "_timeReleased"
+ "alwaysOnEnabled:%u"
+ "bls_isOnOrAfter:"
+ "bls_isOnOrBefore:"
+ "cancelAllFrames error:%{public}@ [[CAFlipbook activeFrames] count] should be zero (not %d) after cancelAllFrames lastFrame:%{public}@ – did backboardd die?)"
+ "cancelAllFramesWithError:"
+ "cancelWithError:"
+ "dateSpecifierModel:didAddEnvironment:"
+ "dateSpecifierModel:didRemoveEnvironment:"
+ "didUpdateToPresentation:"
+ "disableClientInvalidationBudget"
+ "disableHostInvalidationBudget"
+ "disabled"
+ "disabling client side invalidation budget because default is set"
+ "disabling host side invalidation budget because default is set"
+ "enabled"
+ "enabling client side invalidation budget."
+ "enabling host side invalidation budget."
+ "error != nil"
+ "hostEnvironment:hostDidSetHighLuminanceAlwaysOn:"
+ "initWithEngine:"
+ "initWithEventID:state:previousState:wasTransitioning:changeRequest:"
+ "isEmpty"
+ "lock_setFlipbookPredictiveRenderType"
+ "longHeldAssertionWithDescription:activeDuration:timeReleased:"
+ "longHeldAssertions"
+ "model:%@ should be empty, was just added to helper"
+ "must have valid flipbook to set flipbook mode"
+ "presentationDatesModel"
+ "purge stale"
+ "released"
+ "resetAllBudgetsForReason:"
+ "resetAllLocalHostBudgetsForReason:"
+ "resetBudgetForEnvironment:reason:"
+ "setDateSpecifier:"
+ "setPresentationDate:"
+ "setPresentationDatesModel:"
+ "setVisualState:presentationDate:"
+ "unrestrictedFramerate"
+ "v16@?0@\"<BLSHDateSpecifierModelObserving>\"8"
+ "v25@0:8{?=b1b1b1b1b1}16@\"BLSBacklightSceneUpdate\"17"
+ "v25@0:8{?=b1b1b1b1b1}16@17"
+ "v32@0:8@\"BLSHDateSpecifierModel\"16@\"<BLSHBacklightSceneHostEnvironment>\"24"
+ "wasTransitioning"
+ "withLock:"
+ "\xf1"
- "\x05\x14R"
- "\x06\x12\x11"
- "\x12\x12\x11Q"
- "\x1f\v"
- "%p -[CAFlipBook cancel] took %.5fs. Likely dupe of rdar://78634442"
- "%p updates(%d) (invalid - stopping) valid:(%{public}@->%{public}@)"
- "%p:%{public}@ will ignore invalidate flipbook (not in presentation) for source:%{public}@ reason:%{public}@ environment:%{public}@"
- "BLSHBacklightEnvironmentStateMachineAbortPayload.m"
- "Can't handle index %u"
- "TB,GisDisplayBlanked"
- "TB,GisDisplayBlanked,V_displayBlanked"
- "T{os_unfair_lock_s=I},R,N,V_lock"
- "_displayBlanked"
- "bls_isBlanked"
- "bls_setBlanked:"
- "cancelAllFrames"
- "displayBlanked"
- "isDisplayBlanked"
- "lock"
- "setDisplayBlanked:"
- "v25@0:8{?=b1b1b1b1b1b1}16@\"BLSBacklightSceneUpdate\"17"
- "v25@0:8{?=b1b1b1b1b1b1}16@17"
- "{os_unfair_lock_s=I}16@0:8"
- "\xe1"

```
