## ActivityAchievementsDaemon

> `/System/Library/PrivateFrameworks/ActivityAchievementsDaemon.framework/ActivityAchievementsDaemon`

```diff

-2026.1.2.0.0
-  __TEXT.__text: 0x787e0
+2026.1.5.0.0
+  __TEXT.__text: 0x788cc
   __TEXT.__auth_stubs: 0x1800
   __TEXT.__objc_methlist: 0x60b4
   __TEXT.__const: 0x868
   __TEXT.__cstring: 0x6581
   __TEXT.__gcc_except_tab: 0x2450
-  __TEXT.__oslogstring: 0x905d
+  __TEXT.__oslogstring: 0x90cd
   __TEXT.__swift5_typeref: 0x2f7
   __TEXT.__swift5_capture: 0x24
   __TEXT.__constg_swiftt: 0x180

   __TEXT.__swift5_assocty: 0x30
   __TEXT.__swift5_proto: 0x68
   __TEXT.__swift5_types: 0x28
-  __TEXT.__unwind_info: 0x1f58
+  __TEXT.__unwind_info: 0x1f60
   __TEXT.__eh_frame: 0x438
   __TEXT.__objc_classname: 0xc7e
   __TEXT.__objc_methname: 0x11abe
   __TEXT.__objc_methtype: 0x2260
   __TEXT.__objc_stubs: 0xa820
   __DATA_CONST.__got: 0x758
-  __DATA_CONST.__const: 0x2718
+  __DATA_CONST.__const: 0x2720
   __DATA_CONST.__objc_classlist: 0x238
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x140

   __AUTH_CONST.__objc_intobj: 0x360
   __AUTH_CONST.__objc_arrayobj: 0x90
   __AUTH_CONST.__objc_doubleobj: 0x20
-  __AUTH.__objc_data: 0x320
+  __AUTH.__objc_data: 0x280
   __AUTH.__data: 0xc0
   __DATA.__objc_ivar: 0x720
   __DATA.__data: 0x1088
-  __DATA.__bss: 0xe20
-  __DATA_DIRTY.__objc_data: 0x13b0
+  __DATA.__bss: 0xdf0
+  __DATA_DIRTY.__objc_data: 0x1450
   __DATA_DIRTY.__data: 0x198
-  __DATA_DIRTY.__bss: 0xe8
+  __DATA_DIRTY.__bss: 0x118
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIntents.dylib

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: CF6B66B6-20C8-3AEB-815E-8A7E4DA99715
+  UUID: 4D92441D-B702-305F-80A7-D5B8D584D3DC
   Functions: 2825
-  Symbols:   9207
-  CStrings:  4188
+  Symbols:   9209
+  CStrings:  4190
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftCoreImage
+ __swift_FORCE_LOAD_$_swiftCoreImage_$_ActivityAchievementsDaemon
Functions:
~ ___91-[ACHEarnedInstanceAwardingEngine _requestHistoricalEvaluationForAllSourcesWithCompletion:]_block_invoke_2 : 864 -> 1028
~ _OUTLINED_FUNCTION_4 : 12 -> 32
~ ___50-[ACHEarnedInstanceAwardingEngine registerSource:]_block_invoke.cold.1 : 140 -> 144
~ ___52-[ACHEarnedInstanceAwardingEngine deregisterSource:]_block_invoke.cold.1 : 140 -> 144
~ ___91-[ACHEarnedInstanceAwardingEngine _requestHistoricalEvaluationForAllSourcesWithCompletion:]_block_invoke_2.cold.1 : 168 -> 172
~ ___91-[ACHEarnedInstanceAwardingEngine _requestHistoricalEvaluationForAllSourcesWithCompletion:]_block_invoke_2.cold.2 : 180 -> 204
~ ___91-[ACHEarnedInstanceAwardingEngine _requestHistoricalEvaluationForAllSourcesWithCompletion:]_block_invoke_2.cold.3 : 164 -> 180
CStrings:
+ "[%{public}@] Committing data store properties for sourceRecord.source %{public}@ to dataStore"
+ "[%{public}@] Error committing data store properties for sourceRecord %{public}@ with error %{public}@"
+ "[%{public}@] Error committing data store properties for sourceRecord.source %{public}@ with error %{public}@"
+ "[%{public}@] Now committing source record %{public}@ to data store"
+ "[%{public}@] failed historical evaluation: %{public}@"
+ "[%{public}@] succeeded historical evaluation"
+ "[%{public}@] succeeded historical evaluation, committing data to dataStore"
- "Error committing data store properties for sourceRecord %@ with error %{public}@"
- "Error committing data store properties for sourceRecord.source %@ with error %{public}@"
- "Successfully committed data store properties for sourceRecord.source %@, now committing source record %@ properties"
- "[%@] failed historical evaluation, not committing data to dataStore: %{public}@"
- "[%@] succeeded historical evaluation, committing data to dataStore"

```
