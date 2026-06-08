## EXDisplayPipe

> `/System/Library/PrivateFrameworks/EXDisplayPipe.framework/EXDisplayPipe`

```diff

-8.1.12.0.0
-  __TEXT.__text: 0x8d8 sha256:5412760890ca4b533afe7abbffd834d26567282bde6825b12cdf8c00542190e7
-  __TEXT.__auth_stubs: 0xb0 sha256:9b696d03f48b1e215784b47829a7f25b5ec1d75724528f566b04f372d68878fd
+9.1.40.0.0
+  __TEXT.__text: 0xa68 sha256:bc78127d29cdc5b36610f8e3e6f5f7eae48da7ef2b2b584917ef13d996efd91b
   __TEXT.__const: 0x40 sha256:3cd4c3344b83de580fd6913858c9b98c9a5cb604525b7ab74c713eac3966cbb7
-  __TEXT.__cstring: 0x248 sha256:85821851227e4c4bee9f68888903458b3017c35dbcb6fb44a01051698e6d6aef
-  __TEXT.__unwind_info: 0x58 sha256:ff9aef36a45fc5316b1ac2d8a917f1a65b4fa1a075c3939c8e4b2a0893473c8b
-  __DATA_CONST.__got: 0x10 sha256:374708fff7719dd5979ec875d56cd2286f6d3cf7ec317a3b25632aab28ec37bb
-  __AUTH_CONST.__auth_got: 0x58 sha256:10eef285deef7a4b7c82b22aa53589b7833df29de3814649c772bbd5c832f365
+  __TEXT.__cstring: 0x2a1 sha256:6d10b7da83207eb59aeff0e4b486ed64c17af19af33808c8a97c02e0db9e9028
+  __TEXT.__unwind_info: 0x68 sha256:d31201bb41888d50d1a126f753cf95b4e5767cb907aaf9f771069006bea756ce
+  __TEXT.__auth_stubs: 0x0
+  __DATA_CONST.__got: 0x0
+  __AUTH_CONST.__cfstring: 0x20 sha256:df6644f5f3cc745b217b517a41c827d8f454aa491f82f194d689e4716f0aa4d5
+  __AUTH_CONST.__auth_got: 0x0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
-  UUID: 7B7611A7-DA6D-3B28-8FBD-83BA0B957C75
-  Functions: 14
-  Symbols:   29
-  CStrings:  20
+  UUID: 1E384FA1-9885-342D-BAF4-46F60AB180F5
+  Functions: 16
+  Symbols:   38
+  CStrings:  25
 
Symbols:
+ _CFNumberGetValue
+ _CFRelease
+ _EXDisplayPipeGetFrameInfo
+ _EXDisplayPipeOpenDisplay
+ _IOIteratorNext
+ _IOObjectRelease
+ _IORegistryEntrySearchCFProperty
+ _IOServiceGetMatchingServices
+ ___CFConstantStringClassReference
+ _kCFAllocatorDefault
- _IOServiceGetMatchingService
Functions:
~ _EXDisplayPipeOpen : 276 -> 12
+ _EXDisplayPipeOpenDisplay
~ _EXDisplayPipeClose : sha256 aca046a28ffd7b568c7d0489a17e4c5092f6b17afbf4525b716fd41dde093c30 -> fdcd9623e487178070f3d7528e5a1eeeadfe33e6742b7df55090359ca0192f0e
~ _EXDisplayPipeSetPower : sha256 07b33832e2a64ddb567a6b74dd6622d9fa1a71309171552b62990a82336ef8b5 -> 040e76ab2b2273926cd96492df2947a4584439d5eaaeea075e965bc1e002d4f2
~ _EXDisplayPipeShowIndicator : sha256 6da4220fa1f2122a06cdbffb0207f41903bb81230fcaf4d7b7266910e4d795a9 -> 382fc3a0289d66869c14fa718745ee2decf7fdcbfba51d8822926e37d027b2d4
~ _EXDisplayPipeHideIndicator : sha256 4d6046868643cbb353e7c08430d70f901bfa352951e1b99c21ac9e739111938d -> 95ce4d4f8c019f9ce43a1c8f18fc398eae6c8e18c8a27cdfbba8d8e0c9cdd01c
~ _EXDisplayPipeSetIndicators : sha256 ad28611d04a48956a57a5e5e625a5833c96552611267e8cef5c4bcd9a44d951b -> 4db8391edf820e64e0f0f33ca7ce8f69698dda9387dd4d48a1ec92a2921a4442
~ _EXDisplayPipeGetStatus : sha256 a74fa284288724b4ba1be8ee36e06b453f9cc73063298ad39fe89b32b8e5b902 -> a87c7f2811ced4cb420c61c5683b2ae2c9009488e8333c130462cb86532ce497
~ _EXDisplayPipeGetSecureTEStatus : sha256 6e60ea8af19ec63b526997b61e6cfbcd3d48b6cd7581655873686cdce63ab0e5 -> a120ac3d3e21836ed630524944a2b5c5a8fbfdc629f0be092980feb367484ee4
~ _EXDisplayPipeSetLogLevel : sha256 b6339b2c1c747ea3156945415dcb613ee2030d8cb6cf61cc548821dee3ae8bb9 -> 8d628202138788edea7b747ea048fb761c97648078fc05b06017b57d26c965c0
~ _EXDisplayPipeSetLogMask : sha256 38f08e2cc688832bebfe1295ea932f7d10ef63250502ee147f51f70f302a3585 -> 4f2faa60fc2eaa4fbe2fe8a564b956cf99fa2354df182218133de7a5be1ec386
~ _EXDisplayPipeSetALSSEnable : sha256 52e4ae36f0c2693fc4b04c0ccf6f7c07739adf51144432af2651a72a96a1a03c -> 0ce566e75013f2ddee3b336401d9129090521caaaaa633d4ae9a54c1fdda112f
~ _EXDisplayPipeFlushTelemetry : sha256 73cf412284a2b00d8fd84f1473d406aa55c07cab9722270be7b68ec3ad3536cd -> d8372824a5b788e3c8af16ecfdbeb98e441b021480e901d49a73c4b9d6735890
~ _EXDisplayPipeGetSCASessionHealth : sha256 3dd362b3ca4a07e593722cf9caec7c82f388bad180f8485d4a804dc2d9793705 -> 3b94f8e09ada88bf6dd2292415eba7511d134d110053df9cb8416b3aa932d1aa
~ _EXDisplayPipeGetStats : sha256 89a7b8def7d5ebcaf5174f4eb7b299c2a8596bf19300b4ccf25f15bc8506b33a -> a398cec1becc7859de56d5dff50567cf6f8be920294217f70cb4f55fe3e08ad6
CStrings:
+ "EXDisplayPipeGetFrameInfo"
+ "IOService"
+ "display-index"
+ "error: failed to get matching services"

```
