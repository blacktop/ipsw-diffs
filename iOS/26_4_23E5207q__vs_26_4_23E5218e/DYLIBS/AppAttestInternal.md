## AppAttestInternal

> `/System/Library/PrivateFrameworks/AppAttestInternal.framework/AppAttestInternal`

```diff

-132.1.0.0.0
-  __TEXT.__text: 0x690fc
+132.2.0.0.0
+  __TEXT.__text: 0x69178
   __TEXT.__auth_stubs: 0x1620
   __TEXT.__objc_methlist: 0x6c4
   __TEXT.__const: 0x3700

   __TEXT.__objc_methtype: 0x399
   __TEXT.__objc_stubs: 0x1660
   __DATA_CONST.__got: 0x4b8
-  __DATA_CONST.__const: 0x300
+  __DATA_CONST.__const: 0x308
   __DATA_CONST.__objc_classlist: 0xe0
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8

   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib
+  - /usr/lib/swift/libswiftSpatial.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 81FD014E-74B2-3682-9E6D-A168B07850CB
+  UUID: C8AE54DB-FC53-31CD-A35B-CCDBCB0CF9F2
   Functions: 1371
-  Symbols:   2009
+  Symbols:   2011
   CStrings:  1357
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftSpatial
+ __swift_FORCE_LOAD_$_swiftSpatial_$_AppAttestInternal
Functions:
~ sub_22d370dbc -> sub_22d3f2e04 : 396 -> 528
~ sub_22d37dadc -> sub_22d3ffba8 : 500 -> 492
CStrings:
+ "/Library/Caches/com.apple.xbs/C5BC7708-B121-4112-889F-6D423A57FFBB/TemporaryDirectory.nPBkjT/Sources/TwoBit/AppAttestInternal/Source/Core/AppAttestEligibilityManager.m"
+ "/Library/Caches/com.apple.xbs/C5BC7708-B121-4112-889F-6D423A57FFBB/TemporaryDirectory.nPBkjT/Sources/TwoBit/AppAttestInternal/Source/Core/AppAttestHandler.swift"
+ "/Library/Caches/com.apple.xbs/C5BC7708-B121-4112-889F-6D423A57FFBB/TemporaryDirectory.nPBkjT/Sources/TwoBit/AppAttestInternal/Source/Core/Controllers/BundleRecordController.swift"
+ "/Library/Caches/com.apple.xbs/C5BC7708-B121-4112-889F-6D423A57FFBB/TemporaryDirectory.nPBkjT/Sources/TwoBit/AppAttestInternal/Source/Core/Controllers/KeychainController.swift"
+ "/Library/Caches/com.apple.xbs/C5BC7708-B121-4112-889F-6D423A57FFBB/TemporaryDirectory.nPBkjT/Sources/TwoBit/AppAttestInternal/Source/Core/Controllers/SecurityController.swift"
+ "/Library/Caches/com.apple.xbs/C5BC7708-B121-4112-889F-6D423A57FFBB/TemporaryDirectory.nPBkjT/Sources/TwoBit/AppAttestInternal/Source/Core/DeviceAttestHandler.swift"
+ "/Library/Caches/com.apple.xbs/C5BC7708-B121-4112-889F-6D423A57FFBB/TemporaryDirectory.nPBkjT/Sources/TwoBit/AppAttestInternal/Source/Core/Managers/AppUUIDDataManager.swift"
+ "/Library/Caches/com.apple.xbs/C5BC7708-B121-4112-889F-6D423A57FFBB/TemporaryDirectory.nPBkjT/Sources/TwoBit/AppAttestInternal/Source/Core/Managers/AssertionCBORManager.swift"
+ "/Library/Caches/com.apple.xbs/C5BC7708-B121-4112-889F-6D423A57FFBB/TemporaryDirectory.nPBkjT/Sources/TwoBit/AppAttestInternal/Source/Core/Managers/AssertionDataManager.swift"
+ "/Library/Caches/com.apple.xbs/C5BC7708-B121-4112-889F-6D423A57FFBB/TemporaryDirectory.nPBkjT/Sources/TwoBit/AppAttestInternal/Source/Core/Managers/AttestationCBORManager.swift"
+ "/Library/Caches/com.apple.xbs/C5BC7708-B121-4112-889F-6D423A57FFBB/TemporaryDirectory.nPBkjT/Sources/TwoBit/AppAttestInternal/Source/Core/Managers/AttestationManager.swift"
+ "/Library/Caches/com.apple.xbs/C5BC7708-B121-4112-889F-6D423A57FFBB/TemporaryDirectory.nPBkjT/Sources/TwoBit/AppAttestInternal/Source/Core/Managers/AuthenticationManager.swift"
+ "/Library/Caches/com.apple.xbs/C5BC7708-B121-4112-889F-6D423A57FFBB/TemporaryDirectory.nPBkjT/Sources/TwoBit/AppAttestInternal/Source/Core/Managers/EligibilityManager.swift"
+ "/Library/Caches/com.apple.xbs/C5BC7708-B121-4112-889F-6D423A57FFBB/TemporaryDirectory.nPBkjT/Sources/TwoBit/AppAttestInternal/Source/Core/Managers/IdentityManager.swift"
+ "/Library/Caches/com.apple.xbs/C5BC7708-B121-4112-889F-6D423A57FFBB/TemporaryDirectory.nPBkjT/Sources/TwoBit/AppAttestInternal/Source/Core/Managers/KeyDataManager.swift"
+ "/Library/Caches/com.apple.xbs/C5BC7708-B121-4112-889F-6D423A57FFBB/TemporaryDirectory.nPBkjT/Sources/TwoBit/AppAttestInternal/Source/Core/Utility/KeyUtility.swift"
+ "/Library/Caches/com.apple.xbs/C5BC7708-B121-4112-889F-6D423A57FFBB/TemporaryDirectory.nPBkjT/Sources/TwoBit/AppAttestInternal/Source/Core/support/AnonymousAttestation.m"
+ "/Library/Caches/com.apple.xbs/C5BC7708-B121-4112-889F-6D423A57FFBB/TemporaryDirectory.nPBkjT/Sources/TwoBit/AppAttestInternal/Source/Core/support/AppAttestation.m"
+ "/Library/Caches/com.apple.xbs/C5BC7708-B121-4112-889F-6D423A57FFBB/TemporaryDirectory.nPBkjT/Sources/TwoBit/AppAttestInternal/Source/Interfaces/AppAttestAppAttestation.m"
+ "/Library/Caches/com.apple.xbs/C5BC7708-B121-4112-889F-6D423A57FFBB/TemporaryDirectory.nPBkjT/Sources/TwoBit/AppAttestInternal/Source/Interfaces/AppAttestDeviceAttestation.m"
+ "/Library/Caches/com.apple.xbs/C5BC7708-B121-4112-889F-6D423A57FFBB/TemporaryDirectory.nPBkjT/Sources/TwoBit/AppAttestInternal/Source/Interfaces/AppAttestTaskCreator.m"
+ "/Library/Caches/com.apple.xbs/C5BC7708-B121-4112-889F-6D423A57FFBB/TemporaryDirectory.nPBkjT/Sources/TwoBit/AppAttestInternal/Source/Interfaces/AppAttestUtils.m"
+ "/Library/Caches/com.apple.xbs/C5BC7708-B121-4112-889F-6D423A57FFBB/TemporaryDirectory.nPBkjT/Sources/TwoBit/AppAttestInternal/Source/Interfaces/AppAttestWebAuthentication.m"
+ "/Library/Caches/com.apple.xbs/C5BC7708-B121-4112-889F-6D423A57FFBB/TemporaryDirectory.nPBkjT/Sources/TwoBit/FeatureFlags/DeviceCheck.swift"
+ "/Library/Caches/com.apple.xbs/C5BC7708-B121-4112-889F-6D423A57FFBB/TemporaryDirectory.nPBkjT/Sources/TwoBit/FeatureFlags/FeatureFlagsManager.m"
+ "AppAttest (%@-132.2) - %@"
- "/Library/Caches/com.apple.xbs/B05BC02D-BD92-442D-B28C-8A501BBB4521/TemporaryDirectory.IO0WlM/Sources/TwoBit/AppAttestInternal/Source/Core/AppAttestEligibilityManager.m"
- "/Library/Caches/com.apple.xbs/B05BC02D-BD92-442D-B28C-8A501BBB4521/TemporaryDirectory.IO0WlM/Sources/TwoBit/AppAttestInternal/Source/Core/AppAttestHandler.swift"
- "/Library/Caches/com.apple.xbs/B05BC02D-BD92-442D-B28C-8A501BBB4521/TemporaryDirectory.IO0WlM/Sources/TwoBit/AppAttestInternal/Source/Core/Controllers/BundleRecordController.swift"
- "/Library/Caches/com.apple.xbs/B05BC02D-BD92-442D-B28C-8A501BBB4521/TemporaryDirectory.IO0WlM/Sources/TwoBit/AppAttestInternal/Source/Core/Controllers/KeychainController.swift"
- "/Library/Caches/com.apple.xbs/B05BC02D-BD92-442D-B28C-8A501BBB4521/TemporaryDirectory.IO0WlM/Sources/TwoBit/AppAttestInternal/Source/Core/Controllers/SecurityController.swift"
- "/Library/Caches/com.apple.xbs/B05BC02D-BD92-442D-B28C-8A501BBB4521/TemporaryDirectory.IO0WlM/Sources/TwoBit/AppAttestInternal/Source/Core/DeviceAttestHandler.swift"
- "/Library/Caches/com.apple.xbs/B05BC02D-BD92-442D-B28C-8A501BBB4521/TemporaryDirectory.IO0WlM/Sources/TwoBit/AppAttestInternal/Source/Core/Managers/AppUUIDDataManager.swift"
- "/Library/Caches/com.apple.xbs/B05BC02D-BD92-442D-B28C-8A501BBB4521/TemporaryDirectory.IO0WlM/Sources/TwoBit/AppAttestInternal/Source/Core/Managers/AssertionCBORManager.swift"
- "/Library/Caches/com.apple.xbs/B05BC02D-BD92-442D-B28C-8A501BBB4521/TemporaryDirectory.IO0WlM/Sources/TwoBit/AppAttestInternal/Source/Core/Managers/AssertionDataManager.swift"
- "/Library/Caches/com.apple.xbs/B05BC02D-BD92-442D-B28C-8A501BBB4521/TemporaryDirectory.IO0WlM/Sources/TwoBit/AppAttestInternal/Source/Core/Managers/AttestationCBORManager.swift"
- "/Library/Caches/com.apple.xbs/B05BC02D-BD92-442D-B28C-8A501BBB4521/TemporaryDirectory.IO0WlM/Sources/TwoBit/AppAttestInternal/Source/Core/Managers/AttestationManager.swift"
- "/Library/Caches/com.apple.xbs/B05BC02D-BD92-442D-B28C-8A501BBB4521/TemporaryDirectory.IO0WlM/Sources/TwoBit/AppAttestInternal/Source/Core/Managers/AuthenticationManager.swift"
- "/Library/Caches/com.apple.xbs/B05BC02D-BD92-442D-B28C-8A501BBB4521/TemporaryDirectory.IO0WlM/Sources/TwoBit/AppAttestInternal/Source/Core/Managers/EligibilityManager.swift"
- "/Library/Caches/com.apple.xbs/B05BC02D-BD92-442D-B28C-8A501BBB4521/TemporaryDirectory.IO0WlM/Sources/TwoBit/AppAttestInternal/Source/Core/Managers/IdentityManager.swift"
- "/Library/Caches/com.apple.xbs/B05BC02D-BD92-442D-B28C-8A501BBB4521/TemporaryDirectory.IO0WlM/Sources/TwoBit/AppAttestInternal/Source/Core/Managers/KeyDataManager.swift"
- "/Library/Caches/com.apple.xbs/B05BC02D-BD92-442D-B28C-8A501BBB4521/TemporaryDirectory.IO0WlM/Sources/TwoBit/AppAttestInternal/Source/Core/Utility/KeyUtility.swift"
- "/Library/Caches/com.apple.xbs/B05BC02D-BD92-442D-B28C-8A501BBB4521/TemporaryDirectory.IO0WlM/Sources/TwoBit/AppAttestInternal/Source/Core/support/AnonymousAttestation.m"
- "/Library/Caches/com.apple.xbs/B05BC02D-BD92-442D-B28C-8A501BBB4521/TemporaryDirectory.IO0WlM/Sources/TwoBit/AppAttestInternal/Source/Core/support/AppAttestation.m"
- "/Library/Caches/com.apple.xbs/B05BC02D-BD92-442D-B28C-8A501BBB4521/TemporaryDirectory.IO0WlM/Sources/TwoBit/AppAttestInternal/Source/Interfaces/AppAttestAppAttestation.m"
- "/Library/Caches/com.apple.xbs/B05BC02D-BD92-442D-B28C-8A501BBB4521/TemporaryDirectory.IO0WlM/Sources/TwoBit/AppAttestInternal/Source/Interfaces/AppAttestDeviceAttestation.m"
- "/Library/Caches/com.apple.xbs/B05BC02D-BD92-442D-B28C-8A501BBB4521/TemporaryDirectory.IO0WlM/Sources/TwoBit/AppAttestInternal/Source/Interfaces/AppAttestTaskCreator.m"
- "/Library/Caches/com.apple.xbs/B05BC02D-BD92-442D-B28C-8A501BBB4521/TemporaryDirectory.IO0WlM/Sources/TwoBit/AppAttestInternal/Source/Interfaces/AppAttestUtils.m"
- "/Library/Caches/com.apple.xbs/B05BC02D-BD92-442D-B28C-8A501BBB4521/TemporaryDirectory.IO0WlM/Sources/TwoBit/AppAttestInternal/Source/Interfaces/AppAttestWebAuthentication.m"
- "/Library/Caches/com.apple.xbs/B05BC02D-BD92-442D-B28C-8A501BBB4521/TemporaryDirectory.IO0WlM/Sources/TwoBit/FeatureFlags/DeviceCheck.swift"
- "/Library/Caches/com.apple.xbs/B05BC02D-BD92-442D-B28C-8A501BBB4521/TemporaryDirectory.IO0WlM/Sources/TwoBit/FeatureFlags/FeatureFlagsManager.m"
- "AppAttest (%@-132.1) - %@"

```
