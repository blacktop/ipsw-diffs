## SystemWake

> `/System/Library/PrivateFrameworks/SystemWake.framework/SystemWake`

```diff

-694.2.1.0.0
-  __TEXT.__text: 0x9e28
-  __TEXT.__auth_stubs: 0x550
-  __TEXT.__objc_methlist: 0x4c8
-  __TEXT.__const: 0xc0
-  __TEXT.__gcc_except_tab: 0x1088
-  __TEXT.__cstring: 0x9d8
-  __TEXT.__oslogstring: 0x1197
-  __TEXT.__unwind_info: 0x4a8
-  __TEXT.__objc_classname: 0x25e
-  __TEXT.__objc_methname: 0x122c
-  __TEXT.__objc_methtype: 0x58a
-  __TEXT.__objc_stubs: 0xae0
-  __DATA_CONST.__got: 0xf8
-  __DATA_CONST.__const: 0x408
-  __DATA_CONST.__objc_classlist: 0x58
-  __DATA_CONST.__objc_protolist: 0x60
+694.2.2.0.0
+  __TEXT.__text: 0xbdf0
+  __TEXT.__auth_stubs: 0x5a0
+  __TEXT.__objc_methlist: 0x5d0
+  __TEXT.__const: 0xd8
+  __TEXT.__gcc_except_tab: 0x1368
+  __TEXT.__cstring: 0xae7
+  __TEXT.__oslogstring: 0x1622
+  __TEXT.__unwind_info: 0x590
+  __TEXT.__objc_classname: 0x2ab
+  __TEXT.__objc_methname: 0x14bf
+  __TEXT.__objc_methtype: 0x5e5
+  __TEXT.__objc_stubs: 0xc20
+  __DATA_CONST.__got: 0x108
+  __DATA_CONST.__const: 0x4c0
+  __DATA_CONST.__objc_classlist: 0x60
+  __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x360
-  __DATA_CONST.__objc_superrefs: 0x48
-  __AUTH_CONST.__auth_got: 0x2b8
-  __AUTH_CONST.__const: 0xc0
-  __AUTH_CONST.__cfstring: 0x960
-  __AUTH_CONST.__objc_const: 0x1be0
-  __DATA.__objc_ivar: 0x110
-  __DATA.__data: 0x480
+  __DATA_CONST.__objc_selrefs: 0x3b8
+  __DATA_CONST.__objc_superrefs: 0x50
+  __AUTH_CONST.__auth_got: 0x2e0
+  __AUTH_CONST.__const: 0xe0
+  __AUTH_CONST.__cfstring: 0xac0
+  __AUTH_CONST.__objc_const: 0x1e80
+  __AUTH.__objc_data: 0x50
+  __DATA.__objc_ivar: 0x138
+  __DATA.__data: 0x4e0
   __DATA_DIRTY.__objc_data: 0x370
-  __DATA_DIRTY.__bss: 0x48
+  __DATA_DIRTY.__bss: 0x58
   __DATA_DIRTY.__common: 0x20
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 143
-  Symbols:   278
-  CStrings:  456
+  Functions: 174
+  Symbols:   317
+  CStrings:  504
 
Symbols:
+ _OBJC_CLASS_$_BSDescriptionStream
+ _objc_opt_new
+ _OBJC_CLASS_$_SWActiveSystemActivityRegistry
+ _OBJC_METACLASS_$_SWActiveSystemActivityRegistry
+ _BSLogAddStateCaptureBlockWithTitle
+ _NSStringForSWSystemActivityAbortSleepPhase
+ _objc_retain_x27
+ _objc_release_x28
+ _os_variant_has_internal_diagnostics
CStrings:
+ "_lock_systemActivitiesAreActive"
+ "@\"SWActiveSystemActivityRegistry\""
+ "@60@0:8@16@24B32@36@44@52"
+ "_lock_activeSystemActivitiesCount"
+ "isAwakeOrAbortingSleep"
+ "appendCollection:withName:itemBlock:"
+ "\x03"
+ "_activeSystemActivityRegistry"
+ "awakeOrAbortingSleep"
+ "aborted"
+ "TB,R,GisAwakeOrAbortingSleep"
+ "powerManagementPhase != SWSystemSleepPowerManagementPhaseInitialized"
+ "systemActivityAborting"
+ "%!p(MISSING) (zero active system activities) state:%!{(MISSING)public}@ elapsed:%!l(MISSING)fs phase:%!{(MISSING)public}@(%!u(MISSING)) elapsedPhase:%!l(MISSING)fs systemActivityAborting:%!{(MISSING)public}@->%!{(MISSING)public}@"
+ "@8@?0"
+ "_acquireWaitsToAbortSleepImminent"
+ "%!p(MISSING) state:%!{(MISSING)public}@ elapsed:%!l(MISSING)fs phase:%!{(MISSING)public}@(%!u(MISSING)) elapsedPhase:%!l(MISSING)fs systemActivityAborting:%!{(MISSING)public}@"
+ "SWSleepState"
+ "%!p(MISSING) created system activity assertion; id:%!{(MISSING)public}@ systemState:%!u(MISSING) assertionID:%!l(MISSING)u wasSleepImminent:%!{(MISSING)BOOL}u isSleepImminent:%!{(MISSING)BOOL}u hasSleepBeenRequested:%!{(MISSING)BOOL}u"
+ "systemActivityRegistryCountDidDecrementToZero:"
+ "%!p(MISSING) systemPowerChanged:%!{(MISSING)public}@(%!u(MISSING)) previous:%!{(MISSING)public}@(%!u(MISSING)) elapsedPhase:%!l(MISSING)fs state:%!{(MISSING)public}@->%!{(MISSING)public}@ elapsedState:%!l(MISSING)fs notificationID:%!l(MISSING)d systemActivityAborting:%!{(MISSING)public}@"
+ "idle"
+ "registerActiveSystemActivity:"
+ "unregisterInactiveSystemActivity:"
+ "%!p(MISSING) obsolete\u00a0request to update to state:%!{(MISSING)public}@ forID:%!l(MISSING)d elapsed:%!l(MISSING)fs – currentState:%!{(MISSING)public}@ elapsed:%!l(MISSING)fs currentID:%!l(MISSING)d systemActivityAborting:%!{(MISSING)public}@"
+ "SWActiveSystemActivityRegistryObserving"
+ "activities"
+ "initWithIdentifier:queue:allowsInvalidation:monitorProvider:sleepAssertionProvider:activeSystemActivityRegistry:"
+ "%!p(MISSING) state:%!{(MISSING)public}@->%!{(MISSING)public}@ elapsed:%!l(MISSING)fs(%!l(MISSING)fs) systemActivityAborting:%!{(MISSING)public}@"
+ "%!p(MISSING) systemPowerChanged:%!{(MISSING)public}@(%!u(MISSING)) previous:%!{(MISSING)public}@(%!u(MISSING)) elapsedPhase:%!l(MISSING)fs state:%!{(MISSING)public}@->%!{(MISSING)public}@ elapsedState:%!l(MISSING)fs notificationID:%!l(MISSING)d systemActivityAborting:%!{(MISSING)public}@->%!{(MISSING)public}@"
+ "sharedRegistry"
+ "@24@0:8Q16"
+ "_lock_activeSystemActivities"
+ "%!p(MISSING) stale request to update to state:%!{(MISSING)public}@ forID:%!l(MISSING)d elapsed:%!l(MISSING)fs – currentState:%!{(MISSING)public}@ elapsed:%!l(MISSING)fs currentID:%!l(MISSING)d systemActivityAborting:%!{(MISSING)public}@"
+ "_lock_systemActivityAbortSleepPhase"
+ "appendProem:block:"
+ "setSleepSlate:powerManagementPhase:notificationID:"
+ "SWActiveSystemActivityRegistry"
+ "systemActivityRegistryCountDidIncrementToOne:"
+ "v24@0:8@\"SWActiveSystemActivityRegistry\"16"
+ "descriptionForTimestamp:"
+ "_stateCaptureHandler"
+ "v16@?0@\"<SWActiveSystemActivityRegistryObserving>\"8"
+ "\x04\x12q"
+ "%!p(MISSING) created system activity assertion too late, will wait for next system wake, id:%!{(MISSING)public}@ err:%!l(MISSING)d wasSleepImminent:%!{(MISSING)BOOL}u isSleepImminent:%!{(MISSING)BOOL}u"
+ "aborting"
+ "pending"
+ "v16@?0@8"
+ "setAcquireWaitsToAbortSleepImminent:"
+ "%!p(MISSING) created system activity assertion after prepareForSleep, will wait for next system wake, id:%!{(MISSING)public}@ err:%!l(MISSING)d"
+ "%!p(MISSING) state:%!{(MISSING)public}@->%!{(MISSING)public}@ elapsed:%!l(MISSING)fs systemActivityAborting:%!{(MISSING)public}@->aborting"
- "%!p(MISSING) created system activity assertion; id:%!{(MISSING)public}@ systemState:%!u(MISSING) assertionID:%!l(MISSING)u wasSleepImminent:%!{(MISSING)BOOL}u"
- "%!p(MISSING) stale request to update to state:%!{(MISSING)public}@ forID:%!l(MISSING)d elapsed:%!l(MISSING)fs – currentState:%!{(MISSING)public}@ elapsed:%!l(MISSING)fs currentID:%!l(MISSING)d"
- "%!p(MISSING) state:%!{(MISSING)public}@->%!{(MISSING)public}@ elapsed:%!l(MISSING)fs(%!l(MISSING)fs)"
- "%!p(MISSING) created system activity assertion too late, will wait for next system wake, id:%!{(MISSING)public}@ err:%!l(MISSING)d wasSleepImminent:%!{(MISSING)BOOL}u"
- "initWithIdentifier:queue:allowsInvalidation:monitorProvider:sleepAssertionProvider:"
- "@52@0:8@16@24B32@36@44"

```
