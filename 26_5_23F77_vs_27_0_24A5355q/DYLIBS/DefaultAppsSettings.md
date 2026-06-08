## DefaultAppsSettings

> `/System/Library/PrivateFrameworks/DefaultAppsSettings.framework/DefaultAppsSettings`

```diff

-14.4.1.0.0
-  __TEXT.__text: 0x270 sha256:51116dda01ac1b3bde5d9ef0d02d4665816ef059abcd56d09a647c74bbf7f841
-  __TEXT.__auth_stubs: 0x10 sha256:ba3ff2641e2c0af26d5a4001fd15b21d5c7ea7a00c74fa16b107ff0adcd855f0
-  __TEXT.__const: 0xa6 sha256:f0ebecb4506fe368715856ba949c265352a5ed6c26e2b22b5613aee95b81b150
+17.0.0.0.0
+  __TEXT.__text: 0x28c sha256:135b37d5bc1ae50c14f66efbc733b8f5e299235d461ff13b40ef3fa316cdb067
+  __TEXT.__const: 0xa6 sha256:fbd3dd973507b5b36a6181139f45d5972e3545d8a76cd48332e38c02a5d0f0d5
   __TEXT.__swift5_typeref: 0x38 sha256:522e3693a9911fa01748591b0e2bfd6c2931e36488680ce116e3e1ee67f97e72
   __TEXT.__swift5_fieldmd: 0x10 sha256:ec0bf2fc5f0e1e5434ffe897e18d521fd4c8b4372cb65dd4a57a08f2c4cb6f6c
-  __TEXT.__constg_swiftt: 0x94 sha256:f6d1fcf6508f62f7aaf2ad1923e6b2f397292c5220a8e4ca682a8270f7d0e5e9
+  __TEXT.__constg_swiftt: 0x94 sha256:677fa508caaa47b86d3d591efa68394ea409e3d08b5f0781e1445d88f9d82c9e
   __TEXT.__swift5_protos: 0x4 sha256:89a0c13e25d82b47262267b8d29e81b65518c03f1b240eba820097c03c12d982
-  __TEXT.__cstring: 0x204 sha256:a45029e65e8c4fa42697c82bf1629e852019f34b60daf7e3cc35725847a6bc3f
-  __TEXT.__unwind_info: 0x68 sha256:aef4074c061466703c0f9bf1e5e419414660e8fe564373be82d75a3f8a0e41bb
+  __TEXT.__cstring: 0x239 sha256:f8e8bab91e90cc50db5e7d1432eb2b60d9dc5144c50e24e23dca1f7e6e8f98a1
+  __TEXT.__unwind_info: 0x98 sha256:07da0872cb1955c94fe6765834cb2c60e71ff6db89f28f1c02b03b500a612750
+  __TEXT.__auth_stubs: 0x0
   __DATA_CONST.__const: 0x88 sha256:b707241545a346265aab1ffb32ff64b55bf8f8dc1b56a46ef33ce3d15db11d33
-  __DATA_CONST.__objc_imageinfo: 0x8 sha256:8c2e86a3d61473a17440ee60441113a7d285704a3b70278f03e88b3c356a5493
+  __DATA_CONST.__objc_imageinfo: 0x8 sha256:ce857dcadc2529f941104469975d60698ea3610a86c121e7b4aee224cd0c59ea
   __AUTH_CONST.__auth_got: 0x8 sha256:af5570f5a1810b7af78caf4bc70a660f0df51e42baf91d4de5b2328de0e83dfc
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/SwiftUI.framework/SwiftUI

   - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
-  - /usr/lib/swift/libswiftCoreMedia.dylib
+  - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: C3EF5A9D-2000-38F6-9E87-D6091DF12EFB
-  Functions: 26
+  UUID: 142F49C1-9E38-360B-982D-09D0B147DBD2
+  Functions: 27
   Symbols:   41
-  CStrings:  11
+  CStrings:  12
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftCoreLocation
+ __swift_FORCE_LOAD_$_swiftCoreLocation_$_DefaultAppsSettings
- __swift_FORCE_LOAD_$_swiftCoreMedia
- __swift_FORCE_LOAD_$_swiftCoreMedia_$_DefaultAppsSettings
Functions:
~ sub_250141ce0 -> sub_257fb8ce0 : sha256 e2cf09fd83db99dc0c6582655b34d3e1ce7f52a6764942339a04111c8ef5c8d0 -> 75733d77ef35b7d9842956b133bce1c453cf4780c8d47d6a2d56208074b6dc5e
~ sub_250141de4 -> sub_257fb8de4 : sha256 c88d68f04d9c54c0a57e00364a49c21316c920b1fd99d5be587c9cfa8083c26f -> 8b88a9e893723e5d119e22bfa18b764dfb3bcd01993e19cf621121febc5da18a
~ sub_250141e00 -> sub_257fb8e00 : sha256 dfd81280e441824fca60b4003751b242c871e66f393be4b331b8ad91ec784e21 -> 2b8440d37e179b47cccf00b641a3ce9e7a966987d7ea5c84a12a8cb9f5a54332
~ sub_250141e1c -> sub_257fb8e1c : sha256 4eb24faf7331c53ebcdfb7285b26e5ed0a83d6a252e7e9215bebaae1405fc029 -> 0ec69de3e4d09c32dc126f9e5bdb56d4132a5c37dbba3686f9de14637c6f8dbb
~ sub_250141e38 -> sub_257fb8e38 : sha256 1cf1311f398ac359a9d4350b9ad07b4f63f8c8829fb0f4db8cbfa1d6a7c704bd -> 78726545a7c2d544e23b7e04149da6440386cf12fe1932dcfadea3450ff59f93
~ sub_250141e54 -> sub_257fb8e54 : sha256 a49d07428d89252f72703ebc57904e18e1294ddfd1961b85664b833a046a5d30 -> 5c6570035b91eb54710bdab2f51da0ed7a5eaaeb0a40928fa444cd628a871583
~ sub_250141e70 -> sub_257fb8e70 : sha256 7243f0758ee0de31d7cc1b9b9e78cb0a8e32343022c0e584c09ca30dce55a230 -> 813b61100e4210cdffcce0d3216385d51c7650273c76d5da1171bd758bd32b07
~ sub_250141e8c -> sub_257fb8e8c : sha256 eb7d30846b04333690b0b426cdb68bb0e85e8ff2ffe0f2dfcc14903defd25d3b -> ab405e045e854f03c6fd3236276a66d7ae4ca72bf7c053525236127239126ada
~ sub_250141ea8 -> sub_257fb8ea8 : sha256 6f0001aadf49075f8d0afa18657e368a8d721d7ce8e27a383cf883c5500590cd -> 7c59308d784540fd9f99b390c706f3c715dacf070d9f898a1c2bd88376174b19
~ sub_250141ec4 -> sub_257fb8ec4 : sha256 f10417221d64503a68af5e9ce101fffae703e3c09666e01ed2bdad8e77bcf55b -> 9c035af49ec8017c59910e4fec738fc022418f89a81ba3178f73bfd9aac52964
~ sub_250141ee0 -> sub_257fb8ee0 : sha256 7e7b1fe054d006cf5ee20cc9c7d8a9ef635f6cc7dbeb13191e95e520a040168f -> bddd6d5647ff123a6df05dc5864dabc36dcbd8b8a1b8f661429eb095ee604853
~ sub_250141efc -> sub_257fb8efc : sha256 482a1da92d04644cf8a070cfcd4debfb028374b61b976658359af733fe67b3cd -> a41fe4a2a23749d3dceb07f697c341cffcc638a6e264941e7a5f020dd3ea01b7
CStrings:
+ "com.apple.settings.MediaDeviceExtensions"

```
