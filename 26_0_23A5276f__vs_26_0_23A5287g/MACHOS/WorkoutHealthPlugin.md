## WorkoutHealthPlugin

> `/System/Library/Health/Plugins/WorkoutHealthPlugin.bundle/WorkoutHealthPlugin`

```diff

-1074.0.0.0.0
-  __TEXT.__text: 0x115a0
-  __TEXT.__auth_stubs: 0x380
-  __TEXT.__objc_stubs: 0x1800
-  __TEXT.__objc_methlist: 0xc9c
+1081.0.0.0.0
+  __TEXT.__text: 0x12b3c
+  __TEXT.__auth_stubs: 0x390
+  __TEXT.__objc_stubs: 0x18e0
+  __TEXT.__objc_methlist: 0xcbc
   __TEXT.__cstring: 0x2174
   __TEXT.__objc_classname: 0x20e
-  __TEXT.__objc_methname: 0x21cb
+  __TEXT.__objc_methname: 0x22f7
   __TEXT.__objc_methtype: 0x947
-  __TEXT.__oslogstring: 0xe30
-  __TEXT.__gcc_except_tab: 0x30c
-  __TEXT.__unwind_info: 0x268
-  __DATA_CONST.__auth_got: 0x1d0
-  __DATA_CONST.__got: 0x188
+  __TEXT.__oslogstring: 0xfea
+  __TEXT.__gcc_except_tab: 0x41c
+  __TEXT.__unwind_info: 0x278
+  __DATA_CONST.__auth_got: 0x1d8
+  __DATA_CONST.__got: 0x198
   __DATA_CONST.__const: 0xb10
   __DATA_CONST.__cfstring: 0x8a0
   __DATA_CONST.__objc_classlist: 0x50

   __DATA_CONST.__objc_arraydata: 0x88
   __DATA_CONST.__objc_arrayobj: 0x60
   __DATA_CONST.__objc_intobj: 0x60
-  __DATA.__objc_const: 0xdd8
-  __DATA.__objc_selrefs: 0x978
+  __DATA.__objc_const: 0xde0
+  __DATA.__objc_selrefs: 0x9b8
   __DATA.__objc_ivar: 0x18
   __DATA.__objc_data: 0x320
   __DATA.__data: 0x420

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: AABD2111-F39C-340A-A604-46E5185AE45E
-  Functions: 206
-  Symbols:   1721
-  CStrings:  636
+  UUID: 6D0BA22A-235D-3855-8AA1-0B61B11EEF44
+  Functions: 211
+  Symbols:   1756
+  CStrings:  650
 
Symbols:
+ +[WOWorkoutEntity queryLimit]
+ GCC_except_table15
+ GCC_except_table27
+ GCC_except_table35
+ GCC_except_table43
+ GCC_except_table52
+ _NSStringForWOPersistenceObjectState
+ _OBJC_CLASS_$_HDSQLiteNullPredicate
+ _OBJC_CLASS_$_HDSQLiteOrderingTerm
+ __80-[WOWorkoutQueryServer _deleteExternalProvidersWithSourceIdentifier:completion:]_block_invoke.388
+ ___block_descriptor_104_e8_32s40s48s56r64r_e35_B24?0"HDDatabaseTransaction"8^16ls32l8r56l8s40l8s48l8r64l8
+ ___block_descriptor_72_e8_32s40s48r_e35_B24?0"HDDatabaseTransaction"8^16lu56l8s32l8s40l8r48l8
+ ___block_descriptor_80_e8_32s40s48s56s_e35_B24?0"HDDatabaseTransaction"8^16ls32l8s40l8s48l8u64l8s56l8
+ ___block_descriptor_80_e8_32s40s_e35_B24?0"HDDatabaseTransaction"8^16ls32l8u48l8s40l8
+ ___block_descriptor_88_e8_32s40s48r_e35_B24?0"HDDatabaseTransaction"8^16lu56l8s32l8s40l8r48l8
+ ___block_descriptor_88_e8_32s40s48s56s64r_e51_B64?08"NSArray"16^{HDSQLiteRow=}24q32Q40^B48^56ls32l8s40l8s48l8r64l8s56l8
+ ___os_log_helper_16_2_2_4_0_8_66
+ ___os_log_helper_16_2_3_8_66_8_66_8_0
+ ___os_log_helper_16_2_4_8_66_8_66_8_0_8_66
+ ___os_log_helper_16_2_5_8_66_8_2_8_64_8_2_8_2
+ _objc_msgSend$encodedByteCount
+ _objc_msgSend$enumerateProperties:withPredicate:orderingTerms:groupBy:limit:healthDatabase:error:enumerationHandler:
+ _objc_msgSend$isNotNullPredicateWithProperty:
+ _objc_msgSend$maxEncodedBytesPerCodableChangeForSyncEntityClass:
+ _objc_msgSend$orderingTermWithProperty:entityClass:ascending:
+ _objc_msgSend$persistences
+ _objc_msgSend$queryLimit
- GCC_except_table13
- GCC_except_table26
- GCC_except_table34
- GCC_except_table38
- GCC_except_table48
- __80-[WOWorkoutQueryServer _deleteExternalProvidersWithSourceIdentifier:completion:]_block_invoke.335
- ___block_descriptor_64_e8_32s40s48r_e35_B24?0"HDDatabaseTransaction"8^16lu56l8s32l8s40l8r48l8
- ___block_descriptor_64_e8_32s40s48s_e51_B64?08"NSArray"16^{HDSQLiteRow=}24q32Q40^B48^56ls32l8s40l8s48l8
- ___block_descriptor_64_e8_32s40s_e35_B24?0"HDDatabaseTransaction"8^16ls32l8u48l8s40l8
- ___block_descriptor_72_e8_32s40s48s56s_e35_B24?0"HDDatabaseTransaction"8^16ls32l8s40l8s48l8u64l8s56l8
- ___block_descriptor_80_e8_32s40s48r_e35_B24?0"HDDatabaseTransaction"8^16lu56l8s32l8s40l8r48l8
- ___block_descriptor_88_e8_32s40s48s56r_e35_B24?0"HDDatabaseTransaction"8^16ls32l8r56l8s40l8s48l8
CStrings:
+ "[WOSync] %{public}@ limit syncing to %{public}lu objects for session (%@). accumulatedBytes=%{public}lu, maxBytes=%{public}lu"
+ "[WOSync] %{public}@ sync generated %{public}lu objects for sync"
+ "[WorkoutQueryServer] fetched %d %{public}@"
+ "[WorkoutQueryServer] fetched %lu %{public}@"
+ "[WorkoutQueryServer] fetching %{public}@ of state %{public}@ (limit=%lu)"
+ "[WorkoutQueryServer] fetching %{public}@ of state %{public}@ (limit=%lu) for id: %{public}@"
+ "encodedByteCount"
+ "enumerateProperties:withPredicate:orderingTerms:groupBy:limit:healthDatabase:error:enumerationHandler:"
+ "isNotNullPredicateWithProperty:"
+ "maxEncodedBytesPerCodableChangeForSyncEntityClass:"
+ "orderingTermWithProperty:entityClass:ascending:"
+ "persistences"
+ "queryLimit"
+ "startSyncAnchorForEntity"

```
