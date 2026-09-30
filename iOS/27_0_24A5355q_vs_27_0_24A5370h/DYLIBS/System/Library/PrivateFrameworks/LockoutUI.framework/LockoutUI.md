## LockoutUI

> `/System/Library/PrivateFrameworks/LockoutUI.framework/LockoutUI`

```diff

 1.0.11.0.0
-  __TEXT.__text: 0xf8 sha256:bcf8029fb0f94549cd4efccb8199a86e5d6a1fbcdd890bba31e7cd67c99bcf5d
-  __TEXT.__objc_methlist: 0x1b4 sha256:2cffe011b95cc1f9cbbd5deec63a699bf4f51a8c4dabe4c6f7aa484011fdbca7
+  __TEXT.__text: 0xf8 sha256:d663828de7e4b8e57299e41c64ea2b5b4f9cc0790048826a6a5c05bdaa4ae045
+  __TEXT.__objc_methlist: 0x1b4 sha256:87b00328deccbc42707680dc6310af5726033030519f833e4d3ec3473c058acc
   __TEXT.__const: 0x38 sha256:3b90dea808d008454d3d08d29a60630397797c74ddc8ac142581e172b5fc755a
   __TEXT.__cstring: 0x42 sha256:729f6ede41a4cb3b582d235d5a5ce2c705743982383458e2ee54188468fe2eb0
   __TEXT.__unwind_info: 0x68 sha256:6849932754ebc63c99f6e81488fd4ee5369c49e55d7d34226881c2747c166ed2

   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x18 sha256:31bf6a4c1c8ac82c66474e9b00702389dbc0847d45150761c02cb061e816743f
-  __DATA_CONST.__objc_classlist: 0x8 sha256:ee639226dcd1a8cb78241eaa5af4368374ae273365a143fa1596f748cdbb6bed
-  __DATA_CONST.__objc_catlist: 0x8 sha256:11f468a1b86676f80fd2c187e9edf6df0078375cf20d296586fd417ab29a76a1
-  __DATA_CONST.__objc_protolist: 0x10 sha256:a356f3a1560d6345c0cec009e73c36f1effdcdbd8756fa8931404945e2e5e4ed
+  __DATA_CONST.__const: 0x18 sha256:eb5a3f8cc67936853a12036102d8ecb3481cedba6fe3b9eb08ef826053f9844a
+  __DATA_CONST.__objc_classlist: 0x8 sha256:a4ae52bfbbd10f34a3e3479277012725dd24f7249cb5bb99e294a582af29a6ba
+  __DATA_CONST.__objc_catlist: 0x8 sha256:daa71068cebcc21654063fc3e24edfc5d68bc7b5ec918aaabb98b7bc44667811
+  __DATA_CONST.__objc_protolist: 0x10 sha256:ed5c016eeaa352a79a0e2b1aaa789bc9633b5600b1d582db0bfbac045247d984
   __DATA_CONST.__objc_imageinfo: 0x8 sha256:59fc9e64071aa89b9247d029e0b37ebe0fe9fc5434efb8e67b0b36435fb494cf
-  __DATA_CONST.__objc_selrefs: 0x100 sha256:981999d77ae6aa66f11164bd623ff70fb6a55874964f4ebcb64c037eef8a4dec
+  __DATA_CONST.__objc_selrefs: 0x100 sha256:c031c30d81123e4294e204c895cf07fe6f0dc09c9280ff218eceb0ff1333e4e8
   __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__cfstring: 0x60 sha256:b368432829b0253b8df9da1f4bc014a96182e9b36a0f208c53b42fa3ddcffaa1
-  __AUTH_CONST.__objc_const: 0x2f0 sha256:e58ae4fbe8700bba481fbe8368927d5955f0fc9cebaede19bc7fe8f26b79c9d1
+  __AUTH_CONST.__cfstring: 0x60 sha256:f9c600f0672c9c029c5c7e04a7331cd1a8127c61f1d8cf73964f0bd410889327
+  __AUTH_CONST.__objc_const: 0x2f0 sha256:339265e36dd5deb85370906af611559c948b6e46f6ef91f4b9e5a9af42c19bf7
   __AUTH_CONST.__auth_got: 0x0
-  __AUTH.__objc_data: 0x50 sha256:dc8cec0835e32a5a0febe5b70e344744ec64ce412c94db42c1d1ae4e17b993e5
-  __DATA.__data: 0xc0 sha256:95bb6030149a24157cb670544e2e7473d9d31bcb549f723dc5149da9a641a307
+  __AUTH.__objc_data: 0x50 sha256:edfa96a1ab0cc60473c863f964bb87eaefe70c7841b3eb5491695678782e49d6
+  __DATA.__data: 0xc0 sha256:a1e6dff4156f52b72016e307669bbf0084e184c0a768e116f478effd257e0796
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/UIKit.framework/UIKit

   - /System/Library/PrivateFrameworks/ScreenTimeUI.framework/ScreenTimeUI
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 350B190B-7E94-34AB-9EDD-A38DFB441AA5
+  UUID: D95F0C49-333E-3877-A449-D29D1B2EE8EC
   Functions: 5
   Symbols:   55
   CStrings:  6
Functions:
~ +[LOViewController lockoutViewControllerWithBundleIdentifier:] : sha256 97dc0ae706e78094ffe311c81857b1a93c179f3808abc7e246bce8bbca51d0eb -> a8728443687506c8493661f26ab594bf2b9f604f0968763be65bf7eb9a86815b
~ -[LOViewController initWithBundleIdentifier:] : sha256 ae3855b6da3416062e54231621b0fe7d3a3e1ba18fc270e4cbd78c37276936dc -> 5ffab6e32834b73d69d975b32a6dfa561719dd068f1293ced7a015791cad0504
~ +[LOViewController messageForApplicationName:style:] : sha256 ee5668a7c93b9c57c7b6872689dd89af082415e5ac014da8bf590e9745eb4bb6 -> e5e109b24054db4efd7f92b67c38157b2f6bbd62383a94545f498f3c237b571e
~ +[LOViewController messageForBundleIdentifier:style:] : sha256 978396f95f4a237ee7d5c9bec936f77217dae3848b5b736cbd8086dde8caf10e -> 923b256e9c6151fc9078d2a2011ff44276f7cdc184c83d10a55691a65c01c014
~ +[LOViewController messageForWebsiteURL:] : sha256 38e5557fc24bbff8f0c6ed5d8e528cc1b57f49ec43074d46d6f290a4c3ce9c03 -> 94349e5aa9120631795268f6c42005e58bb8ce16e4f65195c1f31e9406924d58

```
