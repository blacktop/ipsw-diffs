## AppAttestInternal

> `/System/Library/PrivateFrameworks/AppAttestInternal.framework/Versions/A/AppAttestInternal`

```diff

-108.2.0.0.0
-  __TEXT.__text: 0x6b0f4
-  __TEXT.__auth_stubs: 0x1350
-  __TEXT.__objc_methlist: 0x63c
+109.3.0.0.0
+  __TEXT.__text: 0x6bd48
+  __TEXT.__auth_stubs: 0x1380
+  __TEXT.__objc_methlist: 0x68c
   __TEXT.__const: 0x24f0
-  __TEXT.__cstring: 0x5bb8
-  __TEXT.__oslogstring: 0x302a
-  __TEXT.__gcc_except_tab: 0x690
+  __TEXT.__cstring: 0x5cb8
+  __TEXT.__oslogstring: 0x310a
+  __TEXT.__gcc_except_tab: 0x6e4
   __TEXT.__swift5_typeref: 0x940
   __TEXT.__swift5_reflstr: 0xdd3
   __TEXT.__swift5_assocty: 0x180

   __TEXT.__swift5_mpenum: 0x18
   __TEXT.__swift5_capture: 0x23c
   __TEXT.__swift_as_ret: 0x4
-  __TEXT.__unwind_info: 0xf58
+  __TEXT.__unwind_info: 0xf78
   __TEXT.__eh_frame: 0xb50
-  __TEXT.__objc_classname: 0xd0
-  __TEXT.__objc_methname: 0x1185
-  __TEXT.__objc_methtype: 0x29b
-  __TEXT.__objc_stubs: 0x1200
-  __DATA_CONST.__got: 0x488
+  __TEXT.__objc_classname: 0xe2
+  __TEXT.__objc_methname: 0x11ed
+  __TEXT.__objc_methtype: 0x2b6
+  __TEXT.__objc_stubs: 0x12a0
+  __DATA_CONST.__got: 0x490
   __DATA_CONST.__const: 0x258
-  __DATA_CONST.__objc_classlist: 0xc8
+  __DATA_CONST.__objc_classlist: 0xd0
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x648
+  __DATA_CONST.__objc_selrefs: 0x670
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x40
+  __DATA_CONST.__objc_superrefs: 0x48
   __DATA_CONST.__objc_arraydata: 0xc8
-  __AUTH_CONST.__auth_got: 0x9b8
-  __AUTH_CONST.__auth_ptr: 0x450
-  __AUTH_CONST.__const: 0x23f0
-  __AUTH_CONST.__cfstring: 0x1920
-  __AUTH_CONST.__objc_const: 0x1668
+  __AUTH_CONST.__auth_got: 0x9d0
+  __AUTH_CONST.__auth_ptr: 0x460
+  __AUTH_CONST.__const: 0x2410
+  __AUTH_CONST.__cfstring: 0x19e0
+  __AUTH_CONST.__objc_const: 0x1768
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__objc_arrayobj: 0x78
-  __AUTH.__objc_data: 0xae8
+  __AUTH.__objc_data: 0xb38
   __AUTH.__data: 0x920
-  __DATA.__objc_ivar: 0x34
+  __DATA.__objc_ivar: 0x3c
   __DATA.__data: 0x628
-  __DATA.__bss: 0x3e70
+  __DATA.__bss: 0x3e80
   __DATA.__common: 0x158
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /System/Library/PrivateFrameworks/RemoteServiceDiscovery.framework/Versions/A/RemoteServiceDiscovery
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
+  - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 1336
-  Symbols:   1328
-  CStrings:  1039
+  Functions: 1348
+  Symbols:   1365
+  CStrings:  1063
 
Symbols:
+ -[AppAttestCDHash .cxx_destruct]
+ -[AppAttestCDHash cdHash]
+ -[AppAttestCDHash initWithHash:andType:]
+ -[AppAttestCDHash setCdHash:]
+ -[AppAttestCDHash setType:]
+ -[AppAttestCDHash type]
+ GCC_except_table0
+ OBJC_IVAR_$_AppAttestCDHash._cdHash
+ OBJC_IVAR_$_AppAttestCDHash._type
+ _OBJC_CLASS_$_AppAttestCDHash
+ _OBJC_METACLASS_$_AppAttestCDHash
+ __OBJC_$_INSTANCE_METHODS_AppAttestCDHash
+ __OBJC_$_INSTANCE_VARIABLES_AppAttestCDHash
+ __OBJC_$_PROP_LIST_AppAttestCDHash
+ __OBJC_CLASS_RO_$_AppAttestCDHash
+ __OBJC_METACLASS_RO_$_AppAttestCDHash
+ ___block_descriptor_140_e8_32s40s48s56s64s72s80s88s96bs_e34_v24?0"NSDictionary"8"NSError"16l
+ ___fetchOptInEntitlements_block_invoke
+ ___fetchOptInEntitlements_block_invoke_2
+ __block_literal_global.126
+ __block_literal_global.129
+ __block_literal_global.137
+ __fetchPublicKey_block_invoke.133
+ __removeAllKeychainItemsForMissingApps_block_invoke.123
+ __removeAllKeychainItemsForMissingApps_block_invoke.123.cold.1
+ __removeAllKeychainItemsForMissingApps_block_invoke.123.cold.2
+ __removeAllKeychainItemsForMissingApps_block_invoke.127
+ __removeAllKeychainItemsForMissingApps_block_invoke.127.cold.1
+ __removeAllKeychainItemsForMissingApps_block_invoke.127.cold.2
+ _audit_token_to_pid
+ _csops
+ _fetchCdHash
+ _fetchOptInEntitlements
+ _objc_msgSend$cdHash
+ _objc_msgSend$initWithHash:andType:
+ _objc_msgSend$setCdHash:
+ _objc_msgSend$setType:
+ _objc_msgSend$type
+ _strerror
+ fetchCdHash.cold.1
+ fetchOptInEntitlements.cold.1
+ fetchOptInEntitlements.cold.2
+ fetchOptInEntitlements.cold.3
+ generateAttestationObject.cold.4
- ___block_descriptor_108_e8_32s40s48s56s64s72s80s88s96bs_e34_v24?0"NSDictionary"8"NSError"16l
- __block_literal_global.117
- __block_literal_global.120
- __block_literal_global.128
- __fetchPublicKey_block_invoke.124
- __removeAllKeychainItemsForMissingApps_block_invoke.114
- __removeAllKeychainItemsForMissingApps_block_invoke.114.cold.1
- __removeAllKeychainItemsForMissingApps_block_invoke.114.cold.2
- __removeAllKeychainItemsForMissingApps_block_invoke.118
- __removeAllKeychainItemsForMissingApps_block_invoke.118.cold.1
- __removeAllKeychainItemsForMissingApps_block_invoke.118.cold.2
CStrings:
+ "\x11"
+ "%25s:%-5d Adding CD Hash data to attestation object CBOR."
+ "%25s:%-5d Failed to fetch CD hash. { error=%s }"
+ "%25s:%-5d Fetched opt-in entitlement values. { values=%@ }"
+ "%25s:%-5d No values for opt-in entitlement found."
+ "/AppleInternal/Library/BuildRoots/fa4539c7-059d-11f0-b0c1-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/TwoBit/AppAttestInternal/Source/Core/AppAttestEligibilityManager.m"
+ "/AppleInternal/Library/BuildRoots/fa4539c7-059d-11f0-b0c1-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/TwoBit/AppAttestInternal/Source/Core/AppAttestHandler.swift"
+ "/AppleInternal/Library/BuildRoots/fa4539c7-059d-11f0-b0c1-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/TwoBit/AppAttestInternal/Source/Core/Controllers/BundleRecordController.swift"
+ "/AppleInternal/Library/BuildRoots/fa4539c7-059d-11f0-b0c1-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/TwoBit/AppAttestInternal/Source/Core/Controllers/KeychainController.swift"
+ "/AppleInternal/Library/BuildRoots/fa4539c7-059d-11f0-b0c1-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/TwoBit/AppAttestInternal/Source/Core/Controllers/SecurityController.swift"
+ "/AppleInternal/Library/BuildRoots/fa4539c7-059d-11f0-b0c1-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/TwoBit/AppAttestInternal/Source/Core/DeviceAttestHandler.swift"
+ "/AppleInternal/Library/BuildRoots/fa4539c7-059d-11f0-b0c1-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/TwoBit/AppAttestInternal/Source/Core/Managers/AppUUIDDataManager.swift"
+ "/AppleInternal/Library/BuildRoots/fa4539c7-059d-11f0-b0c1-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/TwoBit/AppAttestInternal/Source/Core/Managers/AssertionDataManager.swift"
+ "/AppleInternal/Library/BuildRoots/fa4539c7-059d-11f0-b0c1-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/TwoBit/AppAttestInternal/Source/Core/Managers/AttestationManager.swift"
+ "/AppleInternal/Library/BuildRoots/fa4539c7-059d-11f0-b0c1-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/TwoBit/AppAttestInternal/Source/Core/Managers/AuthenticationManager.swift"
+ "/AppleInternal/Library/BuildRoots/fa4539c7-059d-11f0-b0c1-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/TwoBit/AppAttestInternal/Source/Core/Managers/EligibilityManager.swift"
+ "/AppleInternal/Library/BuildRoots/fa4539c7-059d-11f0-b0c1-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/TwoBit/AppAttestInternal/Source/Core/Managers/IdentityManager.swift"
+ "/AppleInternal/Library/BuildRoots/fa4539c7-059d-11f0-b0c1-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/TwoBit/AppAttestInternal/Source/Core/Managers/KeyDataManager.swift"
+ "/AppleInternal/Library/BuildRoots/fa4539c7-059d-11f0-b0c1-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/TwoBit/AppAttestInternal/Source/Core/Utility/KeyUtility.swift"
+ "/AppleInternal/Library/BuildRoots/fa4539c7-059d-11f0-b0c1-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/TwoBit/AppAttestInternal/Source/Core/support/AnonymousAttestation.m"
+ "/AppleInternal/Library/BuildRoots/fa4539c7-059d-11f0-b0c1-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/TwoBit/AppAttestInternal/Source/Core/support/AppAttestation.m"
+ "/AppleInternal/Library/BuildRoots/fa4539c7-059d-11f0-b0c1-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/TwoBit/AppAttestInternal/Source/Interfaces/AppAttestAppAttestation.m"
+ "/AppleInternal/Library/BuildRoots/fa4539c7-059d-11f0-b0c1-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/TwoBit/AppAttestInternal/Source/Interfaces/AppAttestDeviceAttestation.m"
+ "/AppleInternal/Library/BuildRoots/fa4539c7-059d-11f0-b0c1-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/TwoBit/AppAttestInternal/Source/Interfaces/AppAttestTaskCreator.m"
+ "/AppleInternal/Library/BuildRoots/fa4539c7-059d-11f0-b0c1-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/TwoBit/AppAttestInternal/Source/Interfaces/AppAttestUtils.m"
+ "/AppleInternal/Library/BuildRoots/fa4539c7-059d-11f0-b0c1-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/TwoBit/AppAttestInternal/Source/Interfaces/AppAttestWebAuthentication.m"
+ "/AppleInternal/Library/BuildRoots/fa4539c7-059d-11f0-b0c1-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/TwoBit/FeatureFlags/FeatureFlagsManager.m"
+ "@28@0:8@16C24"
+ "AppAttest (%@-109.3) - %@"
+ "AppAttestCDHash"
+ "C"
+ "T@\"NSData\",&,N,V_cdHash"
+ "TC,N,V_type"
+ "_cdHash"
+ "_type"
+ "addCdHash"
+ "cdHash"
+ "com.apple.DeviceCheckTests"
+ "com.apple.developer.devicecheck.app-attest-optin"
+ "initWithHash:andType:"
+ "setCdHash:"
+ "setType:"
+ "v20@0:8C16"
- "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/TwoBit/AppAttestInternal/Source/Core/AppAttestEligibilityManager.m"
- "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/TwoBit/AppAttestInternal/Source/Core/AppAttestHandler.swift"
- "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/TwoBit/AppAttestInternal/Source/Core/Controllers/BundleRecordController.swift"
- "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/TwoBit/AppAttestInternal/Source/Core/Controllers/KeychainController.swift"
- "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/TwoBit/AppAttestInternal/Source/Core/Controllers/SecurityController.swift"
- "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/TwoBit/AppAttestInternal/Source/Core/DeviceAttestHandler.swift"
- "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/TwoBit/AppAttestInternal/Source/Core/Managers/AppUUIDDataManager.swift"
- "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/TwoBit/AppAttestInternal/Source/Core/Managers/AssertionDataManager.swift"
- "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/TwoBit/AppAttestInternal/Source/Core/Managers/AttestationManager.swift"
- "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/TwoBit/AppAttestInternal/Source/Core/Managers/AuthenticationManager.swift"
- "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/TwoBit/AppAttestInternal/Source/Core/Managers/EligibilityManager.swift"
- "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/TwoBit/AppAttestInternal/Source/Core/Managers/IdentityManager.swift"
- "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/TwoBit/AppAttestInternal/Source/Core/Managers/KeyDataManager.swift"
- "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/TwoBit/AppAttestInternal/Source/Core/Utility/KeyUtility.swift"
- "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/TwoBit/AppAttestInternal/Source/Core/support/AnonymousAttestation.m"
- "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/TwoBit/AppAttestInternal/Source/Core/support/AppAttestation.m"
- "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/TwoBit/AppAttestInternal/Source/Interfaces/AppAttestAppAttestation.m"
- "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/TwoBit/AppAttestInternal/Source/Interfaces/AppAttestDeviceAttestation.m"
- "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/TwoBit/AppAttestInternal/Source/Interfaces/AppAttestTaskCreator.m"
- "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/TwoBit/AppAttestInternal/Source/Interfaces/AppAttestWebAuthentication.m"
- "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/TwoBit/FeatureFlags/FeatureFlagsManager.m"
- "AppAttest (%@-108.2) - %@"

```
