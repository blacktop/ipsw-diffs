## SleepHealthDaemon

> `/System/Library/PrivateFrameworks/SleepHealthDaemon.framework/SleepHealthDaemon`

```diff

-7027.1.45.2.4
-  __TEXT.__text: 0xc6ec
-  __TEXT.__objc_methlist: 0xb7c
-  __TEXT.__const: 0x298
-  __TEXT.__constg_swiftt: 0x2c
-  __TEXT.__swift5_typeref: 0x51
+7027.1.54.2.3
+  __TEXT.__text: 0xf4dc
+  __TEXT.__objc_methlist: 0xbdc
+  __TEXT.__const: 0x570
+  __TEXT.__constg_swiftt: 0x134
+  __TEXT.__swift5_typeref: 0x157
   __TEXT.__swift5_builtin: 0x14
-  __TEXT.__swift5_reflstr: 0x23
-  __TEXT.__swift5_fieldmd: 0x1c
-  __TEXT.__swift5_assocty: 0x30
-  __TEXT.__swift5_proto: 0x18
-  __TEXT.__swift5_types: 0x4
-  __TEXT.__cstring: 0x633
-  __TEXT.__oslogstring: 0x1bef
-  __TEXT.__gcc_except_tab: 0x184
-  __TEXT.__unwind_info: 0x398
+  __TEXT.__swift5_reflstr: 0x75
+  __TEXT.__swift5_fieldmd: 0xb4
+  __TEXT.__swift5_assocty: 0x68
+  __TEXT.__swift5_proto: 0x30
+  __TEXT.__swift5_types: 0x14
+  __TEXT.__swift5_protos: 0x4
+  __TEXT.__swift5_capture: 0x10
+  __TEXT.__cstring: 0x64b
+  __TEXT.__oslogstring: 0x1c14
+  __TEXT.__gcc_except_tab: 0x100
+  __TEXT.__unwind_info: 0x4e8
   __TEXT.__eh_frame: 0x48
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x278
-  __DATA_CONST.__objc_classlist: 0x58
+  __DATA_CONST.__const: 0x250
+  __DATA_CONST.__objc_classlist: 0x78
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0xe0
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0x50
   __DATA_CONST.__objc_arraydata: 0x48
-  __DATA_CONST.__got: 0x3b8
-  __AUTH_CONST.__const: 0x88
+  __DATA_CONST.__got: 0x4c8
+  __AUTH_CONST.__const: 0xe8
   __AUTH_CONST.__cfstring: 0x4a0
-  __AUTH_CONST.__objc_const: 0x15f0
+  __AUTH_CONST.__objc_const: 0x1880
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH_CONST.__objc_intobj: 0xa8
-  __AUTH_CONST.__auth_got: 0x438
-  __AUTH.__objc_data: 0xf0
-  __DATA.__objc_ivar: 0xc0
-  __DATA.__data: 0x880
+  __AUTH_CONST.__auth_got: 0x668
+  __AUTH.__objc_data: 0x2a8
+  __AUTH.__data: 0x1a8
+  __DATA.__objc_ivar: 0xc4
+  __DATA.__data: 0x988
+  __DATA.__common: 0x28
   __DATA_DIRTY.__objc_data: 0x280
-  __DATA_DIRTY.__data: 0xa8
+  __DATA_DIRTY.__data: 0x98
   __DATA_DIRTY.__bss: 0x100
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/HealthKit.framework/HealthKit
   - /System/Library/Frameworks/UserNotifications.framework/UserNotifications
   - /System/Library/PrivateFrameworks/BreathingAlgorithms.framework/BreathingAlgorithms
+  - /System/Library/PrivateFrameworks/FeatureFlags.framework/FeatureFlags
   - /System/Library/PrivateFrameworks/HealthDaemon.framework/HealthDaemon
   - /System/Library/PrivateFrameworks/HealthDaemonFoundation.framework/HealthDaemonFoundation
   - /System/Library/PrivateFrameworks/HealthFeatures.framework/HealthFeatures
+  - /System/Library/PrivateFrameworks/HealthKitOrchestrationAdditions.framework/HealthKitOrchestrationAdditions
+  - /System/Library/PrivateFrameworks/HealthOrchestration.framework/HealthOrchestration
+  - /System/Library/PrivateFrameworks/HealthUtilities.framework/HealthUtilities
   - /System/Library/PrivateFrameworks/NanoRegistry.framework/NanoRegistry
   - /System/Library/PrivateFrameworks/Sleep.framework/Sleep
   - /System/Library/PrivateFrameworks/SleepHealth.framework/SleepHealth

   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib
+  - /usr/lib/swift/libswiftSynchronization.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 197
-  Symbols:   697
-  CStrings:  163
+  Functions: 286
+  Symbols:   770
+  CStrings:  165
 
Symbols:
+ -[HDSHProfileExtension dealloc]
+ -[HDSHProfileExtension samplesAdded:anchor:]
+ -[HDSHProfileExtension widgetReloader]
+ _OBJC_CLASS_$_HDSHOrchestrationFeatureFlag
+ _OBJC_CLASS_$_HDSHSleepWidgetReloader
+ _OBJC_CLASS_$__TtCs12_SwiftObject
+ _OBJC_IVAR_$_HDSHProfileExtension._widgetReloader
+ _OBJC_METACLASS_$_HDSHOrchestrationFeatureFlag
+ _OBJC_METACLASS_$_HDSHSleepWidgetReloader
+ _OBJC_METACLASS_$__TtCs12_SwiftObject
+ __CLASS_METHODS_HDSHOrchestrationFeatureFlag
+ __CLASS_PROPERTIES_HDSHOrchestrationFeatureFlag
+ __DATA_HDSHOrchestrationFeatureFlag
+ __DATA_HDSHSleepWidgetReloader
+ __DATA__TtC17SleepHealthDaemon25SleepWidgetReloadExecutor
+ __DATA__TtCC17SleepHealthDaemon25SleepWidgetReloadExecutor7Planner
+ __INSTANCE_METHODS_HDSHOrchestrationFeatureFlag
+ __INSTANCE_METHODS_HDSHSleepWidgetReloader
+ __IVARS_HDSHSleepWidgetReloader
+ __IVARS__TtC17SleepHealthDaemon25SleepWidgetReloadExecutor
+ __IVARS__TtCC17SleepHealthDaemon25SleepWidgetReloadExecutor7Planner
+ __METACLASS_DATA_HDSHOrchestrationFeatureFlag
+ __METACLASS_DATA_HDSHSleepWidgetReloader
+ __METACLASS_DATA__TtC17SleepHealthDaemon25SleepWidgetReloadExecutor
+ __METACLASS_DATA__TtCC17SleepHealthDaemon25SleepWidgetReloadExecutor7Planner
+ ___chkstk_darwin
+ ___swift_allocate_boxed_opaque_existential_1
+ ___swift_allocate_value_buffer
+ ___swift_closure_destructor
+ ___swift_destroy_boxed_opaque_existential_0Tm
+ ___swift_destroy_boxed_opaque_existential_1
+ ___swift_mutable_project_boxed_opaque_existential_1
+ ___swift_project_boxed_opaque_existential_1
+ ___swift_project_value_buffer
+ __swiftImmortalRefCount
+ __swift_stdlib_malloc_size
+ _associated conformance 17SleepHealthDaemon0A20WidgetReloadExecutorC0B13Orchestration0F0AA7PlannerAdEP_AdF
+ _associated conformance 17SleepHealthDaemon0A20WidgetReloadExecutorC7PlannerC0B13OrchestrationAdA8WorkPlanAfDP_AfG
+ _associated conformance 17SleepHealthDaemon0A20WidgetReloadExecutorC7PlannerC0bC00bc6PluginG0AA0B13OrchestrationAD
+ _malloc_size
+ _memcpy
+ _memmove
+ _swift_allocBox
+ _swift_arrayInitWithTakeBackToFront
+ _swift_arrayInitWithTakeFrontToBack
+ _swift_conformsToProtocol2
+ _swift_deallocClassInstance
+ _swift_deallocObject
+ _swift_deletedMethodError
+ _swift_dynamicCast
+ _swift_getObjectType
+ _swift_getSingletonMetadata
+ _swift_isUniquelyReferenced_nonNull_native
+ _swift_makeBoxUnique
+ _swift_once
+ _swift_release
+ _swift_release_x27
+ _swift_release_x8
+ _swift_retain_x19
+ _swift_slowAlloc
+ _swift_slowDealloc
+ _swift_updateClassMetadata2
+ _symbolic $s17SleepHealthDaemon0A14WidgetReloaderP
+ _symbolic $s19HealthOrchestration7PlannerP
+ _symbolic $s19HealthOrchestration8ExecutorP
+ _symbolic Sb
+ _symbolic So8NSObjectC
+ _symbolic _____ 17SleepHealthDaemon0A19StoreWidgetReloaderC
+ _symbolic _____ 17SleepHealthDaemon0A20WidgetReloadExecutorC
+ _symbolic _____ 17SleepHealthDaemon0A20WidgetReloadExecutorC7PlannerC
+ _symbolic _____ 17SleepHealthDaemon28HDSHOrchestrationFeatureFlagC
+ _symbolic _____ 19HealthOrchestration14InputSignalSetV
+ _symbolic _____ 19HealthOrchestration14SimpleWorkPlanV
+ _symbolic ______p 17SleepHealthDaemon0A14WidgetReloaderP
+ _symbolic ______p 19HealthOrchestration11WorkContextP
+ _symbolic _____ySo14HKSPSleepStoreCSgG 15Synchronization5MutexVAARi_zrlE
+ _symbolic _____yyt______pGIeghn_ s6ResultOsRi_zRi0_zrlE s5ErrorP
+ _symbolic yt
- +[HDSHWidgetSchedulingManager _logSleepSampleStatistics:]
- GCC_except_table16
- __OBJC_$_CLASS_METHODS_HDSHWidgetSchedulingManager
- ___57+[HDSHWidgetSchedulingManager _logSleepSampleStatistics:]_block_invoke
- ___block_descriptor_64_e8_32r40r48r56r_e26_v16?0"HKCategorySample"8lr32l8r40l8r48l8r56l8
CStrings:
+ "[%{public}s] Reloading sleep widgets"
+ "sleep-widget-reload"
+ "widgetReloadExecutor"
- "v16@?0@\"HKCategorySample\"8"
```
