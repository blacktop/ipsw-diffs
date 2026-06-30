## com.apple.DriverKit-AppleUSBFTDI

> `/System/Library/DriverExtensions/com.apple.DriverKit-AppleUSBFTDI.dext/com.apple.DriverKit-AppleUSBFTDI`

```diff

-145.160.2.0.0
-  __TEXT.__text: 0x1348 sha256:93f896e7cc9a6d914a8a02dc7401e7e278ee592d06c681e5241f5853e3e96e23
+145.160.3.0.0
+  __TEXT.__text: 0x135c sha256:ac18847c5d8cc5691226db152e02e3d5a8b4be33a6d9b9cfa603112e3dd2d67f
   __TEXT.__auth_stubs: 0x1c0 sha256:013f327ebb17ef0f1fb415dca333afb4e87844ba6702785c45985e600409477a
   __TEXT.__const: 0x158 sha256:aa7b687ab7004ec500f2518d7fc736d839c473b2cd582b8c281f3839e60fc3b9
   __TEXT.__cstring: 0x23 sha256:fd203d3d7c4cee9bcbcdd28e1f799a498502453eb6238f8682982f990d36bd25
   __TEXT.__oslogstring: 0xaf sha256:95708ae076d6c799424460aab6bc7c7cc08de362e0f9ad7fc72d4f0ed373d910
   __DATA_CONST.__auth_got: 0xe0 sha256:7658954af2f3ac03e811a24d3571b50513f8add3abfd8223f562936069c0420e
   __DATA_CONST.__got: 0x10 sha256:29e90b32b1a05f55567223aafc34937e21c652990e11b5d66dfc62a8395728ac
-  __DATA_CONST.__const: 0x198 sha256:b1cbdc72f1e21c6566287a63e12df8c5f999fc23fbdd144e5acceaf717eddc6b
+  __DATA_CONST.__const: 0x198 sha256:22e83a46487292cc155f6ad601d4667047869821cb5a1da458efd0ab7e692331
   __DATA_CONST.__osclassinfo: 0x8 sha256:2a74f03864c12635328153d59b74340756a5843d0dfc16245b304b888f3c04dd
   __DATA.__common: 0x8 sha256:6eca5cc86a53c80d74e777fffd48ee46b98f06a8b448d18106af49ac0862b875
   - /System/DriverKit/System/Library/Frameworks/DriverKit.framework/DriverKit

   - /System/DriverKit/System/Library/Frameworks/USBDriverKit.framework/USBDriverKit
   - /System/DriverKit/System/Library/Frameworks/USBSerialDriverKit.framework/USBSerialDriverKit
   - /System/DriverKit/usr/lib/libc++.dylib
-  UUID: 955C90FE-307C-37B2-80F1-6DC10A489695
+  UUID: 50604258-882E-3441-8526-46120DB7B03B
   Functions: 24
   Symbols:   71
   CStrings:  5
Functions:
~ __ZN12AppleUSBFTDI4initEv : sha256 0ff04615162819f011e3632b96ce1e14f0d1245e76aebabb0dd03765a0ec718a -> 69e70dba213064116cc5420d18036912d7de73a689d8aa0c7125599f985cafb5
~ __ZN12AppleUSBFTDI4freeEv : sha256 ac8a5afbd226cc4653d7f118a550dd46f8da59b9a987016d5835fe65fb353883 -> 48483c630f692d63f0ad0da1c00978f197d1690fd25f36ddb531766713f6b2b4
~ __ZN12AppleUSBFTDI10Start_ImplEP9IOService : sha256 12acb229fa377100d77f2b0b986d770f37168f6b57c602d993c8b51bcf62087a -> 935c2e3be0986fb233c0b99e9e91860ac2b0dd6caac01f7659e10cc207ff83fd
~ __ZN12AppleUSBFTDI14handleRxPacketERPhRj : 284 -> 304
~ __ZThn64_N12AppleUSBFTDI14handleRxPacketERPhRj : sha256 134d5deb0b99f18c93afea48b2b1f3720beb47de191cdca732a034f41933a4ab -> be2aafc17f42dc6c98768c821206a710ae55c597ad6f6cb98c0ab07ccb2cff2d
~ __ZNK18AppleUSBFTDI_IVars19calculateDeviceBaudEPtS0_ : sha256 226bdb0b0fc92fc6242f6c40a7c364d870beb35c194c8c255d4393328a2e2258 -> 4bad412c0f0491300032ca72a69043aac1baadc2211a4673abbaef8ab33ebc21
~ __ZL23calculateActualBaudRatejtt : sha256 a71dac34b9a98246cf2a487cd77b47cf7e99d9896921261deb49cb1bfa5efe70 -> 69db34732c92c4e2f64cf199503835d997d4f1a0feeecc54f5d1c39fc6da9493
~ __ZN12AppleUSBFTDI9_DispatchEPS_5IORPC : sha256 5672461447adde329efee5ba44a5a02efb602ab1bcc994d5c48cacce5719cb31 -> 6c7d28042457c06fb8bdc39e617262e359cead9f61b2306d27cf56054e8e592e

```
