## BridgeOSInstall

> `/System/Library/PrivateFrameworks/BridgeOSInstall.framework/Versions/A/BridgeOSInstall`

```diff

 92.0.0.0.0
-  __TEXT.__text: 0x334 sha256:7d629ffe7837b77c8f46c59db4e3eb82635e5c3e90c008c0fa819a904127a109
-  __TEXT.__objc_methlist: 0x19c sha256:d2f62684957c99a97073b913a465dbb00bfd2d5bbb89f9aedb4933f09479b30b
+  __TEXT.__text: 0x334 sha256:96db8fc439f5ed9c6d1701105be0def66041d1245b239d8ee2e3f79e5f582c67
+  __TEXT.__objc_methlist: 0x19c sha256:8d0509d16dfd783c35daed50c22645a0183acea1116d12f4205ed296961243b0
   __TEXT.__const: 0x48 sha256:986c38f5a08ee57213713edbc46c034766d32fc6fd5eeb10f85ea25764ffbf89
   __TEXT.__cstring: 0x183 sha256:65bc265a2b1ad8ed864325087fbbb731d974e56491a752b9f1e19e02c3a7a404
   __TEXT.__unwind_info: 0x78 sha256:208126ce75bcfd975feb6312b41e4a94d3d837f4e23fbfd2a429d1cb34e84636

   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xa8 sha256:cac0882d8119017f049b351f7a578c8fc7033a94f67b9c0d4d60655ebc954707
-  __DATA_CONST.__objc_classlist: 0x10 sha256:51c04a7c8f795a87c6f2c1c18cf3c33d9df6f0bd5b4ffc9a318d277048bd97f8
+  __DATA_CONST.__const: 0xa8 sha256:13a31ada76248ffe6efdae518b3a82aed67092586cccde4df2ade2fb541a7d2e
+  __DATA_CONST.__objc_classlist: 0x10 sha256:d8970c48eae30882711f9c94ff70139735d2ef04fff96305756d1162342ae922
   __DATA_CONST.__objc_imageinfo: 0x8 sha256:59fc9e64071aa89b9247d029e0b37ebe0fe9fc5434efb8e67b0b36435fb494cf
-  __DATA_CONST.__objc_selrefs: 0x110 sha256:2c96b2006542855a1e9a212ab9d2b63247c5071a61efd14a499d3a68e5a7a351
-  __DATA_CONST.__objc_superrefs: 0x8 sha256:205b963a01e31cca3aa23c49530616853cf008eaee904642378b662d7e385de4
+  __DATA_CONST.__objc_selrefs: 0x110 sha256:d69bfc31668c772ec506a3bb9eeaa09a957e0bf9881a8a75a19275e3c84334d2
+  __DATA_CONST.__objc_superrefs: 0x8 sha256:2a869fbeae6f99a58de58b0d5af475795318a1ef89deefdab5167c537d37aa50
   __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__cfstring: 0x2c0 sha256:a44beb12b5f6790cb5a291faf12987de310f2573e41ebb249375896b704dc1a3
-  __AUTH_CONST.__objc_const: 0x1d8 sha256:7d8cdeda4bfcc3f71c74aacfdfaeef220fdbcd4cdf6945707c1e38e816809331
+  __AUTH_CONST.__cfstring: 0x2c0 sha256:4438648138b95f2d529d14f3bda001250a05634c329bb544a4179b446dc05c74
+  __AUTH_CONST.__objc_const: 0x1d8 sha256:281b1997b4858905394df22ee6aeed3f9b0f34dda7926f984cf30c6c1ed1385b
   __AUTH_CONST.__auth_got: 0x0
-  __AUTH.__objc_data: 0xa0 sha256:58cebcaa8d44393769f8062b129e6e198b51bccd7a8a8ff0dc6ce05b4f5f918d
+  __AUTH.__objc_data: 0xa0 sha256:8746186934d0a52746f76058af47e6ca7aca89620b94a0a1ae5b44b7a4d1cde8
   __DATA.__objc_ivar: 0x4 sha256:dc765660b06ee03dd16fd7ca5b957e8c805161ac2c4af28c5a100ab2ab432ca1
-  __DATA.__data: 0x8 sha256:f3228114f92cc4ba8503df88a1a90667b554906b28ea363d8e7d2462b660eed9
+  __DATA.__data: 0x8 sha256:b3d075a57ac0252f2a5f7eea3c584439bf420249498d24043f7fe7b322d108a1
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 04998075-319A-3B9F-85A6-35DCD0F70325
+  UUID: C70EF9B7-72F4-36F1-B0C3-B3EC7441538C
   Functions: 35
   Symbols:   89
   CStrings:  44
Functions:
~ -[BridgeOSInstallController initWithClient:] : sha256 dba82f2d97e0665cd5c23cb2558535643466725b8abef9edf95584b8b9865f62 -> 09d97edae91f6ea96314d44286dc87bf606e455e9c5263ac4106b43450a04199
~ -[BridgeOSInstallController prepareUpdateWithPackageSpecifiers:apply:options:progressHandler:completionHandler:] : sha256 2214f89914d29233d9638948c10457251f699d6b42e12ea43a8dc1d37b3751f5 -> 818bf85fc55069499503d768142a5c9cb79e84197f4ca6514bd0583eba051bdd
~ -[BridgeOSInstallController cancelPendingUpdate] : sha256 02321184aab35a3695ee0221fc7b6775097991eb5c0ecaa536b29b61e787cf3f -> c9f2d641504f695f9b1ffd5dbb91b14bd23e52fc3c014beda273303779ee75a0
~ -[BridgeOSInstallController client] : sha256 f9ebd8259a77c6108389443be1fbb2347f558a2d7977593b29cdaf97dd1d2587 -> 032ed4e787af8a46afeea14b9597f2f10eac8444124d2b0cc27d78790e15f77d
~ -[BridgeOSInstallController setClient:] : sha256 501a33800447e30a4b0b1c45fefa6bbc0d6003f198b78cb03284fba9688fe85a -> 0041997903a1f62a9f2b1de13fac303868369d9c674f60bfcbf958f74d8dc01d
~ -[BridgeOSInstallController .cxx_destruct] : sha256 4a14ed86c3c611844996b3737f6894b79b5fc65745d7cffccc2db789795d8afe -> 4e0af8112408c7414c51910192ff4f19cfd9676a594add4a8e290d5bce079325
~ -[BridgeOSInstallDownloader remotePackageSpecifiers] : sha256 512d4ef3c26e1932e6031d4c9bf768c16bc5397f75dd29b27a4d0ea6aa81a184 -> a1a06cefdee4fe68a2d373a2bfccbb6ad9d11a3a285355e42fa6a224b2b1ee71
~ -[BridgeOSInstallDownloader findProductWithOptions:completionHandler:] : sha256 ace84327ed04b81ba53a66eab70e1976c575f06ab8af70d6ed45b43c57db4539 -> 2d631d63bf2136927a383910c0e4e909b7ca26b91ec0a6f9e0765698ae11a221
~ -[BridgeOSInstallDownloader downloadProductToDirectory:progressHandler:completionHandler:] : sha256 d28a27bd3722f56a97e531a98f1b1edffd3b1262d8f2264280618c3ea2999303 -> c041873e312c975bcb3223943ceaf157c41bce0b1fdfd6bc9c1657a0024c6de8

```
