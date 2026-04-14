## MobileActivationMigrator

> `filesystem/System/Library/DataClassMigrators/MobileActivationMigrator.migrator/MobileActivationMigrator`

```diff

-1076.120.9.0.0
-  __TEXT.__text: 0x2a60
-  __TEXT.__auth_stubs: 0x270
-  __TEXT.__objc_stubs: 0x800
+1076.120.11.0.0
+  __TEXT.__text: 0x2bdc
+  __TEXT.__auth_stubs: 0x2b0
+  __TEXT.__objc_stubs: 0x820
   __TEXT.__objc_methlist: 0x334
-  __TEXT.__cstring: 0x333b
+  __TEXT.__cstring: 0x338e
   __TEXT.__objc_classname: 0x47
-  __TEXT.__objc_methname: 0xc6d
+  __TEXT.__objc_methname: 0xc82
   __TEXT.__objc_methtype: 0x2da
   __TEXT.__const: 0x38
-  __TEXT.__oslogstring: 0x28
+  __TEXT.__oslogstring: 0x53
   __TEXT.__gcc_except_tab: 0x40
   __TEXT.__unwind_info: 0x140
-  __DATA_CONST.__auth_got: 0x148
-  __DATA_CONST.__got: 0xd0
+  __DATA_CONST.__auth_got: 0x168
+  __DATA_CONST.__got: 0xd8
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x1028
-  __DATA_CONST.__cfstring: 0x5060
+  __DATA_CONST.__const: 0x1030
+  __DATA_CONST.__cfstring: 0x50a0
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_arraydata: 0x4d8
   __DATA_CONST.__objc_arrayobj: 0x60
   __DATA.__objc_const: 0x330
-  __DATA.__objc_selrefs: 0x3c8
+  __DATA.__objc_selrefs: 0x3d0
   __DATA.__objc_data: 0xa0
   __DATA.__data: 0xc0
   __DATA.__bss: 0x64
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/PrivateFrameworks/DataMigration.framework/DataMigration
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 94F5C599-8CFE-3DA3-B7C6-1EAA12C79135
-  Functions: 67
-  Symbols:   1557
-  CStrings:  1459
+  UUID: 6695063B-8AAD-33FE-9526-F713FA1EE4F7
+  Functions: 68
+  Symbols:   1570
+  CStrings:  1465
 
Symbols:
+ /Library/Caches/com.apple.xbs/FD5D62B7-94DF-4974-B2E9-E5DB8AD203E8/TemporaryDirectory.NanY7v/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/MobileActivationMigrator.build/Objects-normal/arm64e/GestaltHlpr.o
+ /Library/Caches/com.apple.xbs/FD5D62B7-94DF-4974-B2E9-E5DB8AD203E8/TemporaryDirectory.NanY7v/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/MobileActivationMigrator.build/Objects-normal/arm64e/MobileActivationError.o
+ /Library/Caches/com.apple.xbs/FD5D62B7-94DF-4974-B2E9-E5DB8AD203E8/TemporaryDirectory.NanY7v/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/MobileActivationMigrator.build/Objects-normal/arm64e/MobileActivationErrorPrivate.o
+ /Library/Caches/com.apple.xbs/FD5D62B7-94DF-4974-B2E9-E5DB8AD203E8/TemporaryDirectory.NanY7v/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/MobileActivationMigrator.build/Objects-normal/arm64e/MobileActivationMigrator.o
+ /Library/Caches/com.apple.xbs/FD5D62B7-94DF-4974-B2E9-E5DB8AD203E8/TemporaryDirectory.NanY7v/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/MobileActivationMigrator.build/Objects-normal/arm64e/common.o
+ /Library/Caches/com.apple.xbs/FD5D62B7-94DF-4974-B2E9-E5DB8AD203E8/TemporaryDirectory.NanY7v/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/MobileActivationMigrator.build/Objects-normal/arm64e/data_migration_support.o
+ /Library/Caches/com.apple.xbs/FD5D62B7-94DF-4974-B2E9-E5DB8AD203E8/TemporaryDirectory.NanY7v/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/MobileActivationMigrator.build/Objects-normal/arm64e/keylist.o
+ /Library/Caches/com.apple.xbs/FD5D62B7-94DF-4974-B2E9-E5DB8AD203E8/TemporaryDirectory.NanY7v/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/MobileActivationMigrator.build/Objects-normal/arm64e/vm_support.o
+ /Library/Caches/com.apple.xbs/FD5D62B7-94DF-4974-B2E9-E5DB8AD203E8/TemporaryDirectory.NanY7v/Sources/MobileActivation/MobileActivationMigrator/
+ /Library/Caches/com.apple.xbs/FD5D62B7-94DF-4974-B2E9-E5DB8AD203E8/TemporaryDirectory.NanY7v/Sources/MobileActivation/shared/
+ _CFRelease
+ _SecTaskCopyValueForEntitlement
+ _SecTaskCreateFromSelf
+ __block_literal_global.419
+ __block_literal_global.451
+ __block_literal_global.459
+ __block_literal_global.6
+ __os_log_debug_impl
+ _kCFAllocatorDefault
+ _kMASplunkStatsUCRTEnforcementEnabled
+ _objc_msgSend$valueForEntitlement:
+ isSupportedDeviceIdentityClient.cold.3
- /Library/Caches/com.apple.xbs/2A0FC19B-D1FC-4C6C-9B39-48455A4D4B38/TemporaryDirectory.hehvrP/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/MobileActivationMigrator.build/Objects-normal/arm64e/GestaltHlpr.o
- /Library/Caches/com.apple.xbs/2A0FC19B-D1FC-4C6C-9B39-48455A4D4B38/TemporaryDirectory.hehvrP/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/MobileActivationMigrator.build/Objects-normal/arm64e/MobileActivationError.o
- /Library/Caches/com.apple.xbs/2A0FC19B-D1FC-4C6C-9B39-48455A4D4B38/TemporaryDirectory.hehvrP/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/MobileActivationMigrator.build/Objects-normal/arm64e/MobileActivationErrorPrivate.o
- /Library/Caches/com.apple.xbs/2A0FC19B-D1FC-4C6C-9B39-48455A4D4B38/TemporaryDirectory.hehvrP/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/MobileActivationMigrator.build/Objects-normal/arm64e/MobileActivationMigrator.o
- /Library/Caches/com.apple.xbs/2A0FC19B-D1FC-4C6C-9B39-48455A4D4B38/TemporaryDirectory.hehvrP/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/MobileActivationMigrator.build/Objects-normal/arm64e/common.o
- /Library/Caches/com.apple.xbs/2A0FC19B-D1FC-4C6C-9B39-48455A4D4B38/TemporaryDirectory.hehvrP/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/MobileActivationMigrator.build/Objects-normal/arm64e/data_migration_support.o
- /Library/Caches/com.apple.xbs/2A0FC19B-D1FC-4C6C-9B39-48455A4D4B38/TemporaryDirectory.hehvrP/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/MobileActivationMigrator.build/Objects-normal/arm64e/keylist.o
- /Library/Caches/com.apple.xbs/2A0FC19B-D1FC-4C6C-9B39-48455A4D4B38/TemporaryDirectory.hehvrP/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/MobileActivationMigrator.build/Objects-normal/arm64e/vm_support.o
- /Library/Caches/com.apple.xbs/2A0FC19B-D1FC-4C6C-9B39-48455A4D4B38/TemporaryDirectory.hehvrP/Sources/MobileActivation/MobileActivationMigrator/
- /Library/Caches/com.apple.xbs/2A0FC19B-D1FC-4C6C-9B39-48455A4D4B38/TemporaryDirectory.hehvrP/Sources/MobileActivation/shared/
- __block_literal_global.3
- __block_literal_global.416
- __block_literal_global.448
- __block_literal_global.456
Functions:
~ _isSupportedDeviceIdentityClient : 392 -> 684
~ _OUTLINED_FUNCTION_1 : 24 -> 20
~ _OUTLINED_FUNCTION_2 : 20 -> 16
~ isSupportedDeviceIdentityClient.cold.2 : 112 -> 88
+ isSupportedDeviceIdentityClient.cold.3
CStrings:
+ "Allowlist bypassed for %@ via entitlement."
+ "com.apple.mobileactivationd.deviceidentity-allowlist-exempt"
+ "ucrtEnforcementEnabled"
+ "valueForEntitlement:"

```
