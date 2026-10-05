## HealthOntologyDaemon

> `/System/Library/PrivateFrameworks/HealthOntologyDaemon.framework/HealthOntologyDaemon`

```diff

-7027.1.45.2.4
-  __TEXT.__text: 0x2e56c
-  __TEXT.__objc_methlist: 0x226c
+7027.1.54.2.3
+  __TEXT.__text: 0x2e710
+  __TEXT.__objc_methlist: 0x2254
   __TEXT.__const: 0x282
   __TEXT.__gcc_except_tab: 0x6e8
-  __TEXT.__cstring: 0x34ec
-  __TEXT.__oslogstring: 0x208a
+  __TEXT.__cstring: 0x354c
+  __TEXT.__oslogstring: 0x212a
   __TEXT.__swift5_proto: 0x8
   __TEXT.__swift5_typeref: 0xb1
   __TEXT.__swift5_fieldmd: 0x40

   __DATA_CONST.__objc_catlist: 0x58
   __DATA_CONST.__objc_protolist: 0x120
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x18e8
+  __DATA_CONST.__objc_selrefs: 0x18d8
   __DATA_CONST.__objc_protorefs: 0x48
   __DATA_CONST.__objc_superrefs: 0xf8
   __DATA_CONST.__objc_arraydata: 0x2b0
   __DATA_CONST.__got: 0x428
   __AUTH_CONST.__const: 0x381
-  __AUTH_CONST.__cfstring: 0x2420
-  __AUTH_CONST.__objc_const: 0x4010
+  __AUTH_CONST.__cfstring: 0x2440
+  __AUTH_CONST.__objc_const: 0x4050
   __AUTH_CONST.__objc_arrayobj: 0x150
   __AUTH_CONST.__objc_intobj: 0x1f8
   __AUTH_CONST.__auth_got: 0x4b8
   __AUTH.__objc_data: 0xf0
-  __DATA.__objc_ivar: 0x1f4
+  __DATA.__objc_ivar: 0x1fc
   __DATA.__data: 0xc90
   __DATA_DIRTY.__objc_data: 0xcd0
   __DATA_DIRTY.__data: 0x10

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1138
-  Symbols:   2196
-  CStrings:  476
+  Functions: 1137
+  Symbols:   2198
+  CStrings:  479
 
Symbols:
+ -[HDOntologyUpdateCoordinator _callWillTriggerGatedActivityTestHookWithMaximumDelay:gatedTask:]
+ -[HDOntologyUpdateCoordinator _configureBackgroundTasksInProfile:]
+ GCC_except_table48
+ GCC_except_table70
+ GCC_except_table83
+ _OBJC_IVAR_$_HDOntologyUpdateCoordinator._lock_didConfigureBackgroundTasks
+ _OBJC_IVAR_$_HDOntologyUpdateCoordinator._lock_invalidated
- -[HDOntologyUpdateCoordinator _callWillTriggerGatedActivityTestHookWithMaximumDelay:]
- -[HDOntologyUpdateCoordinator initWithDaemon:scheduler:]
- -[HDOntologyUpdateCoordinator initWithDaemon:scheduler:medicalHistoryDefaults:]
- GCC_except_table71
- GCC_except_table84
CStrings:
+ "%{public}@: No fallback background task available (primary profile not ready, or coordinator invalidated)"
+ "%{public}@: Unable to trigger gated update: %{public}@"
+ "No gated ontology background task available (primary profile not ready, or coordinator invalidated)"
```
