## AmbientUIKit

> `/System/Library/PrivateFrameworks/AmbientUIKit.framework/AmbientUIKit`

```diff

-101.0.100.0.0
-  __TEXT.__text: 0x754 sha256:92728dbcae5a8e7b224139fd581e621c5d5d5eb17ef93cfa632a9eb87216c718
-  __TEXT.__objc_methlist: 0x38 sha256:e69ce561764c4f712df4d80162f50862fa59e8f07121073a1987c70a6ffa73fd
+104.0.0.0.0
+  __TEXT.__text: 0x754 sha256:c8d2846df0f9c4e59f372082fc81be22fe3c17797a898284ee5f052c47820c06
+  __TEXT.__objc_methlist: 0x38 sha256:8837fb825706b1b802896130cfd221c96f8f055f133eba1f4648653a49ed5977
   __TEXT.__const: 0x60 sha256:e20ed59f9f10f9fc5e2e0aee424bb1d3200a3e7a0ffcf3694b30912e8871a7fe
   __TEXT.__cstring: 0x3d sha256:782ca2f5edcb0c211ce29e9cb5834c1c30ee8c39495b2cbbf067333dffd002bd
   __TEXT.__unwind_info: 0x80 sha256:ff62d6cae686cc1732b8868fbe0d1b0d2558ec5efbe5236a794afbd9d0f58fcd

   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x50 sha256:e2dd6396b9ff91e23daaebb13e27148d903b8c6d326064c9c9744fbf1ee9324e
-  __DATA_CONST.__objc_catlist: 0x8 sha256:eda9fdd374707fb824bd06fc9c3993baa1be9d35a2c05316a188d0b126d9e9ae
+  __DATA_CONST.__const: 0x50 sha256:cbe5f4fc817c4784799e28215a3ead6d5c2a9afcca262ec5654c265f5d71af59
+  __DATA_CONST.__objc_catlist: 0x8 sha256:8a5c97d357848bd2313a86ce84ba753336d23d321b6bd22d47d97cc86dd515ac
   __DATA_CONST.__objc_imageinfo: 0x8 sha256:59fc9e64071aa89b9247d029e0b37ebe0fe9fc5434efb8e67b0b36435fb494cf
-  __DATA_CONST.__objc_selrefs: 0xa8 sha256:6896114c7fa0fb527a18c53a851fa10698be843cbfac6663414a2a979e83af7f
+  __DATA_CONST.__objc_selrefs: 0xa8 sha256:a209f6d1bc98ce5ec69c19bf5e149173adcd3aa89969c898ae4b5d7c9c8bb813
   __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__cfstring: 0x60 sha256:8cdb2e819dd21204436a1c29e92cc1bcc2a234fdb6f2ea04d29a408a084af025
-  __AUTH_CONST.__objc_const: 0x40 sha256:94edd403014868505626e36cf3c52cecea6d7ad8a1140b2cf2d09bed91c2b234
+  __AUTH_CONST.__cfstring: 0x60 sha256:ab6d7f0a27b37fc0b764bdf5158b32c1d279016190ec85577e291e9963fb2a75
+  __AUTH_CONST.__objc_const: 0x40 sha256:a955e8739956019842c27d2d83c8698d9c39c2992e69ebbc64743b1eeb84025f
   __AUTH_CONST.__auth_got: 0x0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 3FA7DEC3-3447-3D74-91A6-5587284E4A4C
+  UUID: E30D5909-8254-3EDF-A687-85401E7BAF49
   Functions: 9
   Symbols:   81
   CStrings:  7
Functions:
~ _AMUIRedModeAnimationSettings : sha256 0ca76649ef1429ba92b34c496938640ba6aae2855b9246256c2086ae7664ee55 -> f5cbed03b97290bdfb124ab6056f3cc164ac55876518814bda52aac3fbde8b78
~ -[UIView(AmbientUI) amui_applyRedModeFilterAnimated:withCompletion:] : sha256 95908eae8f06004b8f9aadcea3fd8df873a007485843077ef18783b601f17a18 -> 15962025f4b046dbfe874668da466a9e6968522b0b96c71b00bb8d93415fdc9e
~ -[UIView(AmbientUI) amui_applyRedModeFilterAnimated:withCoordinatedAnimationBlock:completion:] : sha256 da288d0d192156746934ad764ad936fc1cab04abd3130fe4b274e07e17ad7b07 -> c1f8da35bcedc66fc80984f1c3076cb90d53c43b91f110bb1fddae77c3fdeed1
~ ___94-[UIView(AmbientUI) amui_applyRedModeFilterAnimated:withCoordinatedAnimationBlock:completion:]_block_invoke : sha256 b6eed2fdc4ba7fc348af1bf0c285c00f2e99f54d74b624ff173112c30afaf7b7 -> 314fd9d20963332193a8bba2dd2bb1c67a2ca17cfe749947af514d08fb9bf474
~ -[UIView(AmbientUI) amui_clearRedModeFilterAnimated:withCompletion:] : sha256 8670742b90311ff56158d3618b5090e0bf0f330c9fa35fbb97561c0e1181cfdb -> a4e56972b92a3f5e1461619e2efd6a42a605078db0d93da3467cd1ec931f7cd2
~ -[UIView(AmbientUI) amui_clearRedModeFilterAnimated:withCoordinatedAnimationBlock:completion:] : sha256 77dd762110a14190e933aaa1cdaec6470e2afdd1a1029a4f85d6faafac86458a -> 02a2386a3954aa2ab5252297a19b29df212f35cae13e8d8f25a149c3be268c2d
~ ___94-[UIView(AmbientUI) amui_clearRedModeFilterAnimated:withCoordinatedAnimationBlock:completion:]_block_invoke : sha256 6d34541795222c58b6fbf465626c12052ba236c5b6cd10337b0bdf006e15b68b -> 73f258e42f4a323c7ed38ad893c389b54bb3f147807095c9c79507dc943d3b39

```
