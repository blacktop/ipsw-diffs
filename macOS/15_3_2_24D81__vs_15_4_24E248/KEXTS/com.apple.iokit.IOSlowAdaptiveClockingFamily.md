## com.apple.iokit.IOSlowAdaptiveClockingFamily

> `com.apple.iokit.IOSlowAdaptiveClockingFamily`

```diff

-30.0.0.0.0
-  __TEXT.__const: 0x10
-  __TEXT.__cstring: 0x37d
+31.0.0.0.0
+  __TEXT.__const: 0x20
+  __TEXT.__cstring: 0x3a0
   __TEXT.__os_log: 0x2c8
-  __TEXT_EXEC.__text: 0x3028
+  __TEXT_EXEC.__text: 0x312c
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x60
-  __DATA_CONST.__auth_got: 0xd0
+  __DATA_CONST.__auth_got: 0xd8
   __DATA_CONST.__got: 0x38
   __DATA_CONST.__mod_init_func: 0x10
   __DATA_CONST.__mod_term_func: 0x10
   __DATA_CONST.__const: 0xcf8
   __DATA_CONST.__kalloc_type: 0x80
-  UUID: F27DBCB0-C08E-3E2B-93A4-8FDE413408DB
+  __DATA_CONST.__kalloc_var: 0x140
+  UUID: 1B9ECD50-3595-3434-B5C2-8FFE0C2E49A7
   Functions: 76
-  Symbols:   422
-  CStrings:  37
+  Symbols:   427
+  CStrings:  40
 
Symbols:
+ _IOFreeTypeVarImpl
+ _IOMallocTypeVarImpl
+ __ZZN28IOSlowAdaptiveClockingDomain16_allocateVictimsEvE20kalloc_type_view_373
+ __ZZN28IOSlowAdaptiveClockingDomain16_allocateVictimsEvE20kalloc_type_view_382
+ __ZZN28IOSlowAdaptiveClockingDomain4freeEvE19kalloc_type_view_69
+ __ZZN28IOSlowAdaptiveClockingDomain4freeEvE19kalloc_type_view_71
- _IOMallocZeroData
Functions:
~ __ZN28IOSlowAdaptiveClockingDomain4freeEv : 260 -> 368
~ __ZN28IOSlowAdaptiveClockingDomain12clearVictimsEv : 252 -> 316
~ __ZN28IOSlowAdaptiveClockingDomain17initWithAggressorEPvRK21IOSACActionCallback_tjPyPj : 960 -> 972
~ __ZN28IOSlowAdaptiveClockingDomain14_maskFindFirstEPj : 72 -> 76
~ __ZN28IOSlowAdaptiveClockingDomain16_allocateVictimsEv : 216 -> 276
~ __ZN28IOSlowAdaptiveClockingDomain13_removeVictimEy : 928 -> 924
~ __ZN29IOSlowAdaptiveClockingManager5startEP9IOService : 980 -> 972
~ __ZN29IOSlowAdaptiveClockingManager4freeEv : 216 -> 220
~ __ZN29IOSlowAdaptiveClockingManager10addVictimsEjPjjP20IOSACVictimFrequency : 572 -> 592
CStrings:
+ "2211"
+ "site.IOSACVictim"
+ "site.UInt32"

```
