## adprivacyd

> `/usr/libexec/adprivacyd`

```diff

-637.5.1.0.0
-  __TEXT.__text: 0x48c sha256:3df4b7ae39769ee10ba8e13e32f975bfe78f79f5e57346a92ade2319ee075ac8
-  __TEXT.__auth_stubs: 0x140 sha256:65a738bf2d0edbf21c8fed12190042b3cca085153d44cfd7c7f512d76b73a245
-  __TEXT.__objc_stubs: 0x160 sha256:e2055c8f3eb5859b4d053d2b820272363cee3b696210b8f815b3fa403f0781b4
+638.0.7.0.0
+  __TEXT.__text: 0x3e8 sha256:3bae09538b704ae0871b6efda049d6ddb2f505174c24316f264521b108be7083
+  __TEXT.__auth_stubs: 0x130 sha256:cac81d65290afdb81fb01014aa798d5015e171e478249a84a05460eeb96fcb17
+  __TEXT.__objc_stubs: 0x120 sha256:2c6f885af3e8d243d0cbbb3c1a65c4eaa38f9c79310466ccb43daa50227f3fd2
   __TEXT.__const: 0x38 sha256:e6b16a115c3094d5ff8a4f2fd569c87092163ed087e7c1f68602ae7de51efeca
   __TEXT.__cstring: 0x117 sha256:6ed9621a525d0bfda716629e2e4ad57db96c6aed778e698f980fdb9f35a1dbe9
-  __TEXT.__objc_methname: 0xb3 sha256:465d504903f19dd4dd69d072276bb743735c851aac04b8b772be2f9674a951f5
-  __TEXT.__unwind_info: 0x60 sha256:dd868a0e9ecb69147b1912a9e72140453cf21249bf3ccd119df25949742272d7
-  __DATA_CONST.__auth_got: 0xa8 sha256:c805aa254f99ade0f425fcd4243ba6c6096e8e27e8934a959c7a5d77210ee5b3
-  __DATA_CONST.__got: 0x48 sha256:c95788d7305e07c7f187663ae0ffef347aadf36fb05da79c96209718bbb9a409
-  __DATA_CONST.__const: 0x60 sha256:a0a17c84e2db7a0b996c273224e04e0c1f9881f245ee13ed8a9542af85d140e3
-  __DATA_CONST.__cfstring: 0x180 sha256:c6d8ae35c2cd2747e87b6fd11f88889c3d8d75ea2f7f91bf2563bd38d20d2957
+  __TEXT.__objc_methname: 0x91 sha256:1786d5cffe5e5cc0e74f78f0f253c2f8f40313a6fa6cd21a9f14cfc4e6145ccf
+  __TEXT.__unwind_info: 0x60 sha256:184348f23756d5c00ef407216c153d0a0026fcbeaa7996437838c4f11d830755
+  __DATA_CONST.__const: 0x60 sha256:ffb5494a25f30f4a061fb31ce3ace03d799c878f161f431c3a8059ce6b2b1045
+  __DATA_CONST.__cfstring: 0x180 sha256:f5e54a72fadab87845da55f5dbf7808f354dbe73224deadb8c93d9b31e6bd403
   __DATA_CONST.__objc_imageinfo: 0x8 sha256:1fa65ffcccc24c72d5d7f804a2be05ae57dfbb8769ffb33c4272ed6795b7e61c
-  __DATA_CONST.__linkguard: 0x1e sha256:74b42adf9ad4b6b70f4ec98f334eccb36e261178337e3105b6c2ac23ea6b6486
-  __DATA.__objc_selrefs: 0x58 sha256:e57920f4f69b5d38e1d53184246f2c4a42df272691b8ef4dc0defb42a4b43d0a
+  __DATA_CONST.__linkguard: 0x1e sha256:4de8a6f909654f4e1907459b7a223670a260737eea057b5a1bbf4f0c37814e1d
+  __DATA_CONST.__auth_got: 0xa0 sha256:8b3947e7af432a59cc445b6fe6abd1b4a8258c28b0c8b140435e93471f6302ac
+  __DATA_CONST.__got: 0x38 sha256:bdb00518510234c3971c8efbc08f6fbd2f24bc25c0f461b6356284c569d3b0f8
+  __DATA.__objc_selrefs: 0x48 sha256:05d6a79b2fd8eba02882fbda470342a6c044418a8ca093a6fc21a4921f7e2fec
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/AdCore.framework/AdCore

   - /System/Library/PrivateFrameworks/AdPlatformsInternal.framework/AdPlatformsInternal
   - /System/Library/PrivateFrameworks/LimitAdTracking.framework/LimitAdTracking
   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
-  - /System/Library/PrivateFrameworks/PromotedContentPrediction.framework/PromotedContentPrediction
   - /usr/appleinternal/lib/liblinkguard.dylib
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 9CC2F977-E307-3DEF-9202-B2C0CEDD30C8
+  UUID: AB20618D-A04F-32F0-B8E8-95D2AEE3ED23
   Functions: 3
-  Symbols:   35
-  CStrings:  37
+  Symbols:   32
+  CStrings:  35
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
- _MKBDeviceUnlockedSinceBoot
- _OBJC_CLASS_$_APOdmlDatabaseConfiguration
- _OBJC_CLASS_$_APOdmlStoreServerContainer
- _objc_retainAutoreleasedReturnValue
Functions:
~ sub_100000ba0 -> sub_100000b20 : 740 -> 616
~ sub_100000e84 -> sub_100000d88 : sha256 a672172ce10f133fd664fe9bed8c7b66c003575420ac3ef5125402a7a30d28f9 -> 93e80714b9b9dc5d35e83afa94b8e92a561adbabc2e21ac49a78764196446895
~ sub_100000e98 -> sub_100000d9c : 404 -> 364
CStrings:
- "setProcessToDaemon"
- "startListening"

```
