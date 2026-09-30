## AccelerateGPU

> `/System/Library/PrivateFrameworks/AccelerateGPU.framework/Versions/A/AccelerateGPU`

```diff

 35.0.0.0.0
-  __TEXT.__text: 0x4614 sha256:643522c2a78ac9b6cfa2ab2df8afcaea9b1422058dcdf9b4548bacede7f73930
-  __TEXT.__auth_stubs: 0xf0 sha256:eb07eae70e057e54a64a7c95199be6c380d2f7788e22c9d06bac77e8345fc1d9
+  __TEXT.__text: 0x4614 sha256:21689cb0399ddcdaaae9b3f944c7887c517b7d87e750e658366da589071b5288
+  __TEXT.__auth_stubs: 0xf0 sha256:ce0a9f01014cc1bf13837ba53f438b244f5771a6e5510c688f654a32264d69c9
   __TEXT.__gcc_except_tab: 0x900 sha256:87625c7a88aa0f7b885223707dbdbdadded551e1404e3cec3763a336cd7817f3
   __TEXT.__const: 0x58 sha256:6e8ee4de7b1b70cfe9cc6df44d09ca2720c4a53b2d74e4873c15be0b642e7d55
   __TEXT.__cstring: 0x82f sha256:2297cf122e213c0a4269ee528d5d2becefd1fe1cd3a08285e80900205b8132fc
-  __TEXT.__unwind_info: 0x190 sha256:2d7b5579268ecf250d2a2601576b3dcc5ac58d55a116f5eb9a07fd406d8e498e
+  __TEXT.__unwind_info: 0x190 sha256:8bde042a3c1fe1fd1cb7d5ee864f436da55456ce835df3d398e7c2a9059223a5
   __TEXT.__objc_methname: 0x402 sha256:391b085358607751215536b6ef92a61960704f5920afe2fb286547df0884de03
-  __TEXT.__objc_stubs: 0x4a0 sha256:8290101037dc6fc2dd0dc1367b7ebe2cf0cc20b1917053b42ab02144db1d942c
+  __TEXT.__objc_stubs: 0x4a0 sha256:845b22defe88b862f8f3496ec3393c216504b0a4813bb744c04b2a3c0072c777
   __DATA_CONST.__got: 0x28 sha256:2c34ce1df23b838c5abf2a7f6437cca3d3067ed509ff25f11df6b11b582b51eb
   __DATA_CONST.__objc_imageinfo: 0x8 sha256:59fc9e64071aa89b9247d029e0b37ebe0fe9fc5434efb8e67b0b36435fb494cf
-  __DATA_CONST.__objc_selrefs: 0x128 sha256:764abb76e24def631c4ba5cfba76697832d4a492ba61e86a911aaf8df9382bf9
+  __DATA_CONST.__objc_selrefs: 0x128 sha256:6cdbefd34090dd93b0596340fc60f14fcbab16a6c8e7c7c9232bc0308db56477
   __AUTH_CONST.__auth_got: 0x88 sha256:b707241545a346265aab1ffb32ff64b55bf8f8dc1b56a46ef33ce3d15db11d33
-  __AUTH_CONST.__const: 0x30 sha256:e6f9b8ab9f9ee5104626f4bdc93f4f5aa0c16d61870edf8275c976eaef12c68a
-  __AUTH_CONST.__cfstring: 0x6e0 sha256:e28314a2175fa3c05fdb689d52b790e18fd78291b1b0fd4ee7d32e9e01120098
+  __AUTH_CONST.__const: 0x30 sha256:e3d39f5b432acb3e0472df15c1c88a811e0aaa08fff3a6fc976eb869304cdc45
+  __AUTH_CONST.__cfstring: 0x6e0 sha256:0e16efc92d8bbf1f7cb7322bcc6732c25b93fbf065f554cca67be5e1478a3ec5
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/Frameworks/Metal.framework/Versions/A/Metal
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 33C8D51D-6DBE-3E23-A403-73D73E89BD90
+  UUID: 2AF185DA-D715-3891-8BB8-A7C6B389DFD0
   Functions: 41
   Symbols:   120
   CStrings:  148
Functions:
~ _gpuCreateSession : sha256 a5d392ddd4520cfa49011e94dacaaab7dac1cb5136fc804b4c4bdbc95c7dd1b4 -> 41ba93d7ce0e8a4b77e45583b8bcc1b74654f5309da3ebdc774d7de701205cc4
~ _gpuExecuteBlockEndWithCompletionHandler : sha256 3af17a427c585bdc384b206681c5b6cec2c9babbaf2699dab01c71d5965af982 -> b7a2f2b1b934fb36fb92cfac17bf290bff1c01126b851c5b5c0bab1062076ca8
~ _gpuImageHistogramCalculation_ARGB8888 : sha256 ff7b3b26844cd0da2e86b628ec9d61ed75438c50cdbd39ebf0cfb733187025c9 -> d5feea46b796d3196e3553b3de8a0adcc3152fb8a831240804712190d1e137f7
~ _gpuGetLibrary : sha256 c120faccd91a39e8e3992b608f7768c1e24a39ae9aeffae95ec0f1567f96c0db -> 75e9cacdef42d6c937e681543199468ea34aba10502248166d66a87f8bb9dad9
~ _gpuImageConvolution_ARGB8888 : sha256 53457a158667a292c70f291b5c4eafd2de724edb1a0379fda0621ba7934688c8 -> 8ea07d8a056b433a66f556dc980bf6da96bad790566b42b6ef05acb04360ffc0
~ _gpuImageSeparableConvolution_ARGB8888 : sha256 5c2b85a4cdf24350ab1e5fdab7b765586137eb5f2fc2c9285f648c6999440afa -> 359fcb083a169c12005dc7e272000190ad67db9fc24b3b19d265cffc323af5db
~ _gpuImageBoxConvolve_ARGB8888 : sha256 7931d839b82c5490f510b66c55dd6655add1c7a80717501a3115e7290378b417 -> da3e9c23b579da02a8fcb37b78a7e1829947fb2570dbfd2d39d940aace0f2012

```
