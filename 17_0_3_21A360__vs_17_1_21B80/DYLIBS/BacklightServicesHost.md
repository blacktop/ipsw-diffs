## BacklightServicesHost

> `/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost`

```diff

-3.0.103.0.0
-  __TEXT.__text: 0x765f0
+3.1.6.0.0
+  __TEXT.__text: 0x76b54
   __TEXT.__auth_stubs: 0xa60
-  __TEXT.__objc_methlist: 0x543c
+  __TEXT.__objc_methlist: 0x5454
   __TEXT.__const: 0x228
-  __TEXT.__oslogstring: 0xd441
+  __TEXT.__oslogstring: 0xd62f
   __TEXT.__cstring: 0x5938
   __TEXT.__gcc_except_tab: 0x818
   __TEXT.__ustring: 0x1f4
-  __TEXT.__unwind_info: 0x1c50
+  __TEXT.__unwind_info: 0x1c58
   __TEXT.__objc_classname: 0x1c0e
-  __TEXT.__objc_methname: 0xf80c
-  __TEXT.__objc_methtype: 0x3e6a
-  __TEXT.__objc_stubs: 0x8f00
+  __TEXT.__objc_methname: 0xf8d0
+  __TEXT.__objc_methtype: 0x3e81
+  __TEXT.__objc_stubs: 0x8f20
   __DATA_CONST.__got: 0xb8
-  __DATA_CONST.__const: 0x2020
+  __DATA_CONST.__const: 0x2048
   __DATA_CONST.__objc_classlist: 0x4a0
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x270
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0xfd60
-  __DATA_CONST.__objc_selrefs: 0x2a80
+  __DATA_CONST.__objc_const: 0xfdc0
+  __DATA_CONST.__objc_selrefs: 0x2a88
   __DATA_CONST.__objc_arraydata: 0x78
   __AUTH_CONST.__objc_const: 0x39c0
   __AUTH_CONST.__cfstring: 0x5860

   __AUTH.__objc_data: 0x1540
   __DATA.__objc_classrefs: 0x7d0
   __DATA.__objc_superrefs: 0x3d0
-  __DATA.__objc_ivar: 0xc2c
+  __DATA.__objc_ivar: 0xc34
   __DATA.__data: 0x1d40
   __DATA.__bss: 0x90
   __DATA_DIRTY.__objc_data: 0x1900

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
-  Functions: 2897
-  Symbols:   9930
-  CStrings:  4460
+  Functions: 2899
+  Symbols:   9938
+  CStrings:  4469
 
Symbols:
+ -[BLSHEnvironmentTransitionStateTarget backlightRampBlock]
+ -[BLSHEnvironmentTransitionStateTarget initWithSequenceID:backlightState:triggerEvent:backlightRampBlock:]
+ -[BLSHEnvironmentTransitionStateTarget initWithSequenceID:backlightState:visualState:presentationDate:triggerEvent:backlightRampBlock:]
+ -[BLSHEnvironmentTransitionStateTarget triggerEvent]
+ _OBJC_IVAR_$_BLSHEnvironmentTransitionStateTarget._backlightRampBlock
+ _OBJC_IVAR_$_BLSHEnvironmentTransitionStateTarget._triggerEvent
+ ___76-[BLSHLocalHostSceneEnvironment updateToDateSpecifier:sceneContentsUpdated:]_block_invoke
+ ___block_descriptor_72_e8_32s40s48s56s_e5_v8?0ls32l8s40l8s48l8s56l8
+ _objc_msgSend$backlightRampBlock
+ _objc_msgSend$initWithSequenceID:backlightState:triggerEvent:backlightRampBlock:
+ _objc_msgSend$initWithSequenceID:backlightState:visualState:presentationDate:triggerEvent:backlightRampBlock:
- -[BLSHEnvironmentTransitionStateTarget initWithSequenceID:backlightState:]
- -[BLSHEnvironmentTransitionStateTarget initWithSequenceID:backlightState:visualState:presentationDate:]
- -[BLSHLocalHostSceneEnvironment updateToDateSpecifier:sceneContentsUpdated:].cold.6
- _objc_msgSend$initWithSequenceID:backlightState:
- _objc_msgSend$initWithSequenceID:backlightState:visualState:presentationDate:
CStrings:
+ "@48@0:8Q16q24@32@?40"
+ "@64@0:8Q16q24@32@40@48@?56"
+ "@?16@0:8"
+ "ETS:%p:%{public}@ (now obsolete - will not call backlight ramp or animation completion) redundant update to target:%{public}@ wasUpdating:%{BOOL}u animated:%{BOOL}u hasBacklightRamp:%{BOOL}u event:%{public}@ touchTarget:%{BOOL}u oldInProgress:%{public}@ currentInProgress:%{public}@"
+ "ETS:%p:%{public}@ redundant update to target:%{public}@ wasUpdating:%{BOOL}u animated:%{BOOL}u hasBacklightRamp:%{BOOL}u event:%{public}@ touchTarget:%{BOOL}u existingInProgress:%{public}@"
+ "ETS:%p:%{public}@ update to state:%{public}@ – inheriting old backlight ramp existingInProgress:%{public}@ –\u00a0event:%{public}@"
+ "ETS:%p:%{public}@ update to state:%{public}@ – inheriting old triggerEvent existingInProgress:%{public}@ –\u00a0event:%{public}@"
+ "ETS:%p:%{public}@ will skip update to oldTarget:%{public}@ was replaced with newPartialTarget:%{public}@ hadBacklightRamp:%{BOOL}u oldEvent:%{public}@ wouldTransitionHaveBeenNeeded:%{BOOL}U"
+ "ETS:%p:%{public}@ will update to target:%{public}@ wasUpdating:%{BOOL}u animated:%{BOOL}u hasBacklightRamp:%{BOOL}u event:%{public}@ touchTarget:%{BOOL}u"
+ "T@\"BLSBacklightChangeEvent\",R,N,V_triggerEvent"
+ "T@?,R,C,N,V_backlightRampBlock"
+ "_backlightRampBlock"
+ "_triggerEvent"
+ "backlightRampBlock"
+ "hostSceneVisualState != clientEnvVisualState. visualState:%{public}@ clientEnvironment:%{public}@ clientEnvVisualState:%{public}@"
+ "initWithSequenceID:backlightState:triggerEvent:backlightRampBlock:"
+ "initWithSequenceID:backlightState:visualState:presentationDate:triggerEvent:backlightRampBlock:"
+ "visualState:%@ clientEnvironment:%@ clientEnvVisualState:%@"
- "@32@0:8Q16q24"
- "@48@0:8Q16q24@32@40"
- "ETS:%p:%{public}@ (now obsolete - will not call backlight ramp or animation completion) redundant update to target:%{public}@ wasUpdating:%{BOOL}u animated:%{BOOL}u event:%{public}@ touchTarget:%{BOOL}u oldInProgress:%{public}@ currentInProgress:%{public}@"
- "ETS:%p:%{public}@ redundant update to target:%{public}@ wasUpdating:%{BOOL}u animated:%{BOOL}u event:%{public}@ touchTarget:%{BOOL}u existingInProgress:%{public}@"
- "ETS:%p:%{public}@ will skip update to oldTarget:%{public}@ was replaced with newPartialTarget:%{public}@ oldEvent:%{public}@ wouldTransitionHaveBeenNeeded:%{BOOL}U"
- "ETS:%p:%{public}@ will update to target:%{public}@ wasUpdating:%{BOOL}u animated:%{BOOL}u event:%{public}@ touchTarget:%{BOOL}u"
- "[_lock_visualState isEqual:[clientEnvironment visualState]]"
- "initWithSequenceID:backlightState:"
- "initWithSequenceID:backlightState:visualState:presentationDate:"

```
