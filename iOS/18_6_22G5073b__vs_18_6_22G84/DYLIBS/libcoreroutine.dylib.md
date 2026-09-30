## libcoreroutine.dylib

> `/usr/lib/libcoreroutine.dylib`

```diff

-990.0.10.0.0
-  __TEXT.__text: 0x4d55f4
+990.0.10.0.1
+  __TEXT.__text: 0x4d4d00
   __TEXT.__auth_stubs: 0x1d10
-  __TEXT.__objc_methlist: 0x28e94
+  __TEXT.__objc_methlist: 0x28e6c
   __TEXT.__const: 0x1c78
   __TEXT.__dlopen_cstrs: 0x1d2
-  __TEXT.__cstring: 0x3a42b
-  __TEXT.__oslogstring: 0x5e78e
+  __TEXT.__cstring: 0x3a36f
+  __TEXT.__oslogstring: 0x5e739
   __TEXT.__swift5_typeref: 0x73
   __TEXT.__swift5_capture: 0x20
   __TEXT.__constg_swiftt: 0x88

   __TEXT.__swift5_types: 0x4
   __TEXT.__gcc_except_tab: 0x20a48
   __TEXT.__ustring: 0x16
-  __TEXT.__unwind_info: 0xb720
+  __TEXT.__unwind_info: 0xb710
   __TEXT.__eh_frame: 0x60
-  __TEXT.__objc_classname: 0x4ada
-  __TEXT.__objc_methname: 0x76d4d
-  __TEXT.__objc_methtype: 0xb3f8
-  __TEXT.__objc_stubs: 0x46b20
+  __TEXT.__objc_classname: 0x4ad9
+  __TEXT.__objc_methname: 0x76cb6
+  __TEXT.__objc_methtype: 0xb3e4
+  __TEXT.__objc_stubs: 0x46ac0
   __DATA_CONST.__got: 0x29b0
-  __DATA_CONST.__const: 0xcf98
+  __DATA_CONST.__const: 0xcf90
   __DATA_CONST.__objc_classlist: 0x11c0
   __DATA_CONST.__objc_catlist: 0x2e8
   __DATA_CONST.__objc_protolist: 0x308
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x14f40
+  __DATA_CONST.__objc_selrefs: 0x14f28
   __DATA_CONST.__objc_protorefs: 0x120
   __DATA_CONST.__objc_superrefs: 0xf08
   __DATA_CONST.__objc_arraydata: 0x2750
   __AUTH_CONST.__auth_got: 0xe98
   __AUTH_CONST.__const: 0x29f0
-  __AUTH_CONST.__cfstring: 0x21a60
-  __AUTH_CONST.__objc_const: 0x42a78
-  __AUTH_CONST.__objc_intobj: 0x35b8
+  __AUTH_CONST.__cfstring: 0x21a40
+  __AUTH_CONST.__objc_const: 0x42a48
+  __AUTH_CONST.__objc_intobj: 0x35d0
   __AUTH_CONST.__objc_arrayobj: 0xcc0
   __AUTH_CONST.__objc_doubleobj: 0x950
   __AUTH_CONST.__objc_dictobj: 0xf0
   __AUTH_CONST.__objc_floatobj: 0x10
   __AUTH.__objc_data: 0x1dc8
   __AUTH.__data: 0x28
-  __DATA.__objc_ivar: 0x1ed8
+  __DATA.__objc_ivar: 0x1ed4
   __DATA.__data: 0x27f0
   __DATA.__bss: 0x80
   __DATA.__common: 0x8

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: F828E729-D9CB-3ED8-BD87-7BDCDE0FD7ED
-  Functions: 16739
-  Symbols:   54291
-  CStrings:  33179
+  UUID: 5FD174E0-FF49-3167-A529-17FD2352C187
+  Functions: 16736
+  Symbols:   54279
+  CStrings:  33166
 
Symbols:
- -[RTPersistenceMigrator __executeVacuumStepWithStore:coordinator:delegate:vacuumDate:]
- -[RTPersistenceMigrator didVacuumStore]
- -[RTPersistenceStore performVacuumWithCoordinator:error:]
- _OBJC_IVAR_$_RTPersistenceMigrator._didVacuumStore
- _RTPersistentStoreMetadataLastVacuumDateKey
- _kRTPersistentStoreVacuumTimeInterval
- _objc_msgSend$__executeVacuumStepWithStore:coordinator:delegate:vacuumDate:
- _objc_msgSend$didVacuumStore
- _objc_msgSend$performVacuumWithCoordinator:error:
Functions:
~ -[RTPersistenceMigrator initWithStore:modelProvider:delegate:] : 408 -> 404
~ -[RTPersistenceMigrator _executeVacuumStep] : 1844 -> 1312
- -[RTPersistenceMigrator __executeVacuumStepWithStore:coordinator:delegate:vacuumDate:]
~ -[RTPersistenceMigrator _executeRecreateStep] : 1052 -> 1004
- -[RTPersistenceMigrator didVacuumStore]
~ -[RTPersistenceDriver(Metrics) persistenceDriver:persistenceMigrator:didFinishMigratingStore:withModelProvider:] : 912 -> 856
- -[RTPersistenceStore performVacuumWithCoordinator:error:]
CStrings:
+ "22:48:18"
+ "3"
+ "Jul 15 2025"
- "-[RTPersistenceMigrator __executeVacuumStepWithStore:coordinator:delegate:vacuumDate:]"
- "-[RTPersistenceStore performVacuumWithCoordinator:error:]"
- "13:58:58"
- "Invalid parameter not satisfying: vacuumDate"
- "Jun  3 2025"
- "Q48@0:8@16@24@32@40"
- "RTPersistentStoreMetadataLastVacuumDateKey"
- "TB,R,V_didVacuumStore"
- "__executeVacuumStepWithStore:coordinator:delegate:vacuumDate:"
- "_didVacuumStore"
- "didVacuumStore"
- "performVacuumWithCoordinator:error:"
- "vacuum duration, %lf"
- "vacuuming store %@"

```
