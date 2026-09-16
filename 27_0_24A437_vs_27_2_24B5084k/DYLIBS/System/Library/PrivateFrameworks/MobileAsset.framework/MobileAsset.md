## MobileAsset

> `/System/Library/PrivateFrameworks/MobileAsset.framework/MobileAsset`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__objc_imageinfo`

```diff

-2215.0.20.0.0
-  __TEXT.__text: 0x8bf84
-  __TEXT.__objc_methlist: 0x6f64
-  __TEXT.__const: 0x2c4
-  __TEXT.__cstring: 0x13e91
-  __TEXT.__oslogstring: 0xbba3
-  __TEXT.__gcc_except_tab: 0x1394
-  __TEXT.__unwind_info: 0x2420
+2215.40.18.0.0
+  __TEXT.__text: 0x8c718
+  __TEXT.__objc_methlist: 0x6f6c
+  __TEXT.__const: 0x2da
+  __TEXT.__cstring: 0x13f25
+  __TEXT.__oslogstring: 0xbbb4
+  __TEXT.__gcc_except_tab: 0x13a4
+  __TEXT.__swift5_typeref: 0xa
+  __TEXT.__unwind_info: 0x2450
+  __TEXT.__eh_frame: 0x48
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x27a0
+  __DATA_CONST.__const: 0x27c8
   __DATA_CONST.__objc_classlist: 0x290
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x38a8
+  __DATA_CONST.__objc_selrefs: 0x38c8
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x258
-  __DATA_CONST.__objc_arraydata: 0x350
+  __DATA_CONST.__objc_arraydata: 0x7d0
   __DATA_CONST.__got: 0x488
-  __AUTH_CONST.__const: 0x7e0
-  __AUTH_CONST.__cfstring: 0x10120
+  __AUTH_CONST.__const: 0x860
+  __AUTH_CONST.__cfstring: 0x10180
   __AUTH_CONST.__objc_const: 0xac90
-  __AUTH_CONST.__objc_arrayobj: 0x108
+  __AUTH_CONST.__objc_arrayobj: 0x1c8
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_intobj: 0x2e8
-  __AUTH_CONST.__auth_got: 0x0
+  __AUTH_CONST.__auth_got: 0x588
   __AUTH.__objc_data: 0xbe0
   __DATA.__objc_ivar: 0x92c
-  __DATA.__data: 0x358
+  __DATA.__data: 0x360
   __DATA.__crash_info: 0x148
   __DATA_DIRTY.__objc_data: 0xdc0
   __DATA_DIRTY.__data: 0x10

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 3106
-  Symbols:   6282
-  CStrings:  2858
+  - /usr/lib/swift/libswiftCore.dylib
+  - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftDispatch.dylib
+  - /usr/lib/swift/libswiftObjectiveC.dylib
+  - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
+  Functions: 3117
+  Symbols:   6316
+  CStrings:  2861
 
Symbols:
+ -[MAAutoAssetMigrationResults migrationDate]
+ -[MAAutoAssetMigrationResults setMigrationDate:]
+ -[MADownloadOptions summary]
+ _OBJC_IVAR_$_MAAutoAssetMigrationResults._migrationDate
+ __MAClientLogDateFormatter
+ __MAClientLogDateFormatter.dateFormatter
+ __MAClientLogDateFormatter.onceToken
+ __MAClientLogSpacedDateFormatter
+ __MAClientLogSpacedDateFormatter.onceToken
+ __MAClientLogSpacedDateFormatter.spacedDateFormatter
+ ____MAClientLogDateFormatter_block_invoke
+ ____MAClientLogSpacedDateFormatter_block_invoke
+ ___block_descriptor_32_e23_v16?0"MAPushChannel"8l
+ ___swift_instantiateConcreteTypeFromMangledNameV2
+ ___swift_reflection_version
+ __swift_FORCE_LOAD_$_swiftCoreFoundation
+ __swift_FORCE_LOAD_$_swiftCoreFoundation_$_MobileAsset
+ __swift_FORCE_LOAD_$_swiftDispatch
+ __swift_FORCE_LOAD_$_swiftDispatch_$_MobileAsset
+ __swift_FORCE_LOAD_$_swiftFoundation
+ __swift_FORCE_LOAD_$_swiftFoundation_$_MobileAsset
+ __swift_FORCE_LOAD_$_swiftObjectiveC
+ __swift_FORCE_LOAD_$_swiftObjectiveC_$_MobileAsset
+ __swift_FORCE_LOAD_$_swiftXPC
+ __swift_FORCE_LOAD_$_swiftXPC_$_MobileAsset
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_Builtin_float_$_MobileAsset
+ _objc_msgSend$domain
+ _objc_msgSend$isLatestDownloadedFreshForCurrentOSWithError:
+ _objc_msgSend$migrationDate
+ _objc_msgSend$objectIsEqual:to:
+ _objc_msgSend$setConciseLoggingMessages:
+ _objc_msgSend$setDebugLoggingMessages:
+ _objc_retainAutoreleasedReturnValue
+ _swift_bridgeObjectRelease
+ _swift_getTypeByMangledNameInContext2
+ _swift_once
+ _swift_willThrow
+ _symbolic _____ySiG s11_SetStorageC
- -[MAPushNotificationController setVerboseLogging:]
- -[MAPushNotificationController verboseLogging]
- _OBJC_IVAR_$_MAPushNotificationController._verboseLogging
- ___block_descriptor_40_e8_32s_e23_v16?0"MAPushChannel"8ls32l8
- _objc_msgSend$verboseLogging
CStrings:
+ "Caching server for %{public}@ %{public}@ is enabled: %d"
+ "Decoded MAAssetDiff %0llx/%0llx = %0llx"
+ "PreinstalledMigrationFileExists"
+ "Refresh state completed with purpose:%@ result:%ld success:%@"
+ "Secure"
+ "[MigrationResults>>>\nSuccessully migrated assets:\n%@\nFailed migrated assets:\n%@\nSetupError:\n%@\nMigrationDate:\n%@\n<<<]"
+ "cellular:%@|timeout:%ld|discretionary:%@|sessionId:%@|expensive:%@|power:%@|WiFi:%@"
+ "migrationDate"
- "Refresh state completed with result:%ld success:%@"
- "Refreshing with purpose: %@"
- "SecureMA"
- "Using caching server for %{public}@ %{public}@ is enabled: %d"
- "[MigrationResults>>>\nSuccessully migrated assets:\n%@\nFailed migrated assets:\n%@\nSetupError:\n%@\n<<<]"
```
