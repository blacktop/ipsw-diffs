## applekeystored

> `/usr/libexec/applekeystored`

```diff

-2155.0.23.502.1
-  __TEXT.__text: 0x6c1cc
-  __TEXT.__auth_stubs: 0x1b10
+2155.0.28.0.1
+  __TEXT.__text: 0x6c73c
+  __TEXT.__auth_stubs: 0x1a70
   __TEXT.__objc_methlist: 0x104
-  __TEXT.__const: 0x6345
+  __TEXT.__const: 0x62b5
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__swift5_typeref: 0x1b0d
-  __TEXT.__constg_swiftt: 0x1c1c
-  __TEXT.__swift5_reflstr: 0x1650
-  __TEXT.__swift5_fieldmd: 0x215c
-  __TEXT.__oslogstring: 0x12f6
-  __TEXT.__cstring: 0x9cd4
+  __TEXT.__swift5_typeref: 0x1a1f
+  __TEXT.__constg_swiftt: 0x1c10
+  __TEXT.__swift5_reflstr: 0x16a0
+  __TEXT.__swift5_fieldmd: 0x218c
+  __TEXT.__oslogstring: 0x1596
+  __TEXT.__cstring: 0x9d1a
   __TEXT.__swift5_proto: 0x47c
   __TEXT.__swift5_types: 0x1d4
   __TEXT.__swift5_capture: 0x124

   __TEXT.__objc_classname: 0x39
   __TEXT.__objc_methname: 0x275
   __TEXT.__objc_methtype: 0xad
-  __TEXT.__swift_as_entry: 0xc4
-  __TEXT.__swift_as_ret: 0xec
+  __TEXT.__swift_as_entry: 0xc0
+  __TEXT.__swift_as_ret: 0xdc
   __TEXT.__swift5_protos: 0x10
-  __TEXT.__unwind_info: 0x1ac0
-  __TEXT.__eh_frame: 0x3a58
-  __DATA_CONST.__auth_got: 0xd88
-  __DATA_CONST.__got: 0x410
-  __DATA_CONST.__auth_ptr: 0x8d8
-  __DATA_CONST.__const: 0x8e30
+  __TEXT.__unwind_info: 0x1a10
+  __TEXT.__eh_frame: 0x37b0
+  __DATA_CONST.__auth_got: 0xd38
+  __DATA_CONST.__got: 0x408
+  __DATA_CONST.__auth_ptr: 0x8a0
+  __DATA_CONST.__const: 0x8eb0
   __DATA_CONST.__objc_classlist: 0xb8
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA.__objc_const: 0x1d80
   __DATA.__objc_selrefs: 0x100
   __DATA.__objc_data: 0x1e0
-  __DATA.__data: 0x65d0
-  __DATA.__bss: 0x8f10
-  __DATA.__common: 0x1f0
+  __DATA.__data: 0x64b0
+  __DATA.__bss: 0x8ef0
+  __DATA.__common: 0x208
   - /AppleInternal/Library/Frameworks/TapToRadarKit.framework/TapToRadarKit
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CryptoKit.framework/CryptoKit

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftObservation.dylib
   - /usr/lib/swift/libswiftSynchronization.dylib
+  - /usr/lib/swift/libswiftSystem.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: B51E8662-A80B-338E-85AE-723EE79ADB09
-  Functions: 2299
-  Symbols:   793
-  CStrings:  1818
+  UUID: 102FDA6C-3B67-3CB7-AF0D-0F082534BA7C
+  Functions: 2275
+  Symbols:   778
+  CStrings:  1830
 
Symbols:
+ _$s6System5ErrnoVMn
+ _$s6System5ErrnoVN
+ _$s6System5ErrnoVs5ErrorAAMc
- _$s9SwiftData12ModelContextC010registeredC03forxSgAA20PersistentIdentifierV_tAA0gC0RzlFTj
- _$s9SwiftData15PersistentModelPAAE010persistentD2IDAA0C10IdentifierVvg
- _$s9SwiftData6SchemaC15encodingVersionAC0E0Vvg
- _$s9SwiftData6SchemaC15encodingVersionAC0E0VvpMV
- _$s9SwiftData6SchemaC6UniqueCMn
- _$s9SwiftData6SchemaC6UniqueCyAEy_xGSays14PartialKeyPathCyxGGd_tcfc
- _$s9SwiftData6SchemaC6UniqueCy_xGAA0C8PropertyAAMc
- _$s9SwiftData6SchemaC7VersionVMn
- _$s9SwiftData6SchemaCMn
- _$sScS12ContinuationV15BufferingPolicyO9unboundedyADyx__GAFmlFWC
- _$ss14PartialKeyPathCMn
- _swift_arrayInitWithTakeBackToFront
- _swift_arrayInitWithTakeFrontToBack
- _swift_cvw_initEnumMetadataMultiPayloadWithLayoutString
- _swift_cvw_multiPayloadEnumGeneric_destructiveInjectEnumTag
- _swift_cvw_multiPayloadEnumGeneric_getEnumTag
- _swift_getEnumCaseMultiPayload
- _swift_storeEnumTagMultiPayload
CStrings:
+ "<malformed event>"
+ "EnforcementTask has malformed event: a column in this row has an invalid value."
+ "analytics reporting is disabled"
+ "cannot get protectionClass for %s: %@"
+ "com.apple.chrono.WidgetRenderer-Activities"
+ "com.apple.chrono.WidgetRenderer-WatchFaces"
+ "database has invalid column values for EnforcementTask: op(%s), pc(%s), mpc(%s), dpc(%s)"
+ "discarded duplicate event %s"
+ "enqueuing deferred enforcement event: %s retryCount=%ld"
+ "failed to check for duplicate enforcement task: %@"
+ "failed to disable kernel analytics reporting"
+ "failed to get current protection class for %s: %@"
+ "failed to get protection class for %s: %@"
+ "failed to repair %s to %{public}s: %@"
+ "file at %s deleted before it could be processed"
+ "file at %s has exception xattr from: %{public}s"
+ "getProtectionClass(for: %s) failed: errno(%@)"
+ "getProtectionClass(for: %s) skipped: file no longer exists"
+ "kernel analytics reporting is disabled"
+ "kernelAnalyticsEnabled"
+ "retry count exceeded for event %s"
+ "scheduling class D tasks"
+ "setProtectionClass(\"%s\") failed: errno(%@)"
+ "setProtectionClass(\"%s\") skipped: file no longer exists"
+ "setProtectionClass(for: %s, protection: %{public}s) returned 0, but did not actually change the effective class"
+ "setProtectionClass(for: %s, to: %s) skipped: file no longer exists"
+ "skipping repair of %s since it no longer exists"
- " taskID "
- "Failed to get protection class for %s"
- "File at %s has exception xattr from: %{public}s"
- "SwiftData.Schema.Unique"
- "_inProgress"
- "attempted to retry nonexistent enforcement task"
- "cannot get protectionClass for %s"
- "checking if %s is a symbolic link"
- "enqueuing deferred enforcement event: %s"
- "exceeded retries for enforcement task %s"
- "failed to get current protection class for %s"
- "failed to repair %s to %{public}s"
- "setProtectionClass(\"%s\") failed: errno(%d)"
- "setProtectionClass(\"%s\") failed: file not found"
- "setProtectionClassForFile(%s, protection: %{public}s) returned 0, but did not actually change the effective class"

```
