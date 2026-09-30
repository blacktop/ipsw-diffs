## ASMExclaveSupport

> `/System/Library/PrivateFrameworks/ASMExclaveSupport.framework/ASMExclaveSupport`

```diff

-11.28.0.0.0
-  __TEXT.__text: 0x60c sha256:d769264e9985c310036a858baf15e97b8ccc1cb0ec93d84cd1813c4d4a7159f0
-  __TEXT.__auth_stubs: 0x80 sha256:f37627f39de92f1ac836de36dc722b3d87db14ca63bd583143cdb93d591fc4bd
-  __TEXT.__const: 0x1b2 sha256:d7a32a3ec052d5d791a401e940e3420f09db4baa9950d7fadfa62be5454fcd16
-  __TEXT.__constg_swiftt: 0x98 sha256:af504186d18d9c60b729cc28ad823053bcd1765e06c393895fe0a21b688cf874
+20.26.0.0.1
+  __TEXT.__text: 0x60c sha256:68a96434bb902a6b0ab840e159ea7e5fdbc5b27f6311b8a13459440ff8f4d176
+  __TEXT.__const: 0x1b2 sha256:99b77d08ff0514eb5a78de12ec3cf81251a00eb38a359d1e630781fe3fea1db4
+  __TEXT.__constg_swiftt: 0x98 sha256:017070760caa33539935c67458072be243854c78f7afba5155cc6986eb999fb8
   __TEXT.__swift5_typeref: 0x40 sha256:d2ebae5eed372671d2ab012a2c9811d241d40a17b38d50086dccb0d26ef33ed5
   __TEXT.__swift5_builtin: 0x14 sha256:c76c127047d78d2fb11da67cbe87eb27c7a3681e0db423877e2a0182be809750
   __TEXT.__swift5_types: 0xc sha256:f918774ff2c0e3246771f9a477f52beb5e3554a6d540c93ce44391592da88501
   __TEXT.__swift5_fieldmd: 0x30 sha256:2e3094bc201bde73877ff94f3e4d9ece5eefe32f552813adb2254f696a7e196e
   __TEXT.__swift5_proto: 0x14 sha256:2ea9fd210b35338ceec17e6e0e65b002f6a61f0d2f4aa622c06c0fb552c7252d
   __TEXT.__swift5_protos: 0x4 sha256:a40694397cbe238ae7baef064d956fb928432c8d63ce9aab0ac15cd7fd8a2868
-  __TEXT.__unwind_info: 0x98 sha256:8d2ba802bd0ff5d4166f3368976d60920c5e84965209d691877c32490d7f3d13
-  __TEXT.__eh_frame: 0x100 sha256:ed3b8abf2bb5b2c5cc7badd1ccd219982a1d0426cae319626c10d615edeb5dad
-  __DATA_CONST.__got: 0x20 sha256:66687aadf862bd776c8fc18b8e9f8e20089714856ee233b3902a591d0d5f2925
+  __TEXT.__unwind_info: 0xa0 sha256:5808973fbc4bce87e7d11b054cae9f633929d00573a65478a8a541639e214f76
+  __TEXT.__eh_frame: 0x100 sha256:55f6bfd2487723b7bc353cd57bf30d4ab99b595edbf8dcb95af363657941c2af
+  __TEXT.__auth_stubs: 0x0
   __DATA_CONST.__const: 0x38 sha256:d4817aa5497628e7c77e6b606107042bbba3130888c5f47a375e6179be789fbb
-  __DATA_CONST.__objc_imageinfo: 0x8 sha256:8c2e86a3d61473a17440ee60441113a7d285704a3b70278f03e88b3c356a5493
+  __DATA_CONST.__objc_imageinfo: 0x8 sha256:ce857dcadc2529f941104469975d60698ea3610a86c121e7b4aee224cd0c59ea
+  __DATA_CONST.__got: 0x0
+  __AUTH_CONST.__const: 0x78 sha256:e7deae156c8eb60290945656df98f14eeb9ba512d6dbff29736207e02757cdc1
   __AUTH_CONST.__auth_got: 0x40 sha256:f5a5fd42d16a20302798ef6ed309979b43003d2320d9f0e8ea9831a92759fb4b
-  __AUTH_CONST.__const: 0x78 sha256:eca4075f5bbbb0d06747915283d6e40a5d5ab002a38d9b66226718f6b4ccb436
   __DATA.__data: 0x10 sha256:374708fff7719dd5979ec875d56cd2286f6d3cf7ec317a3b25632aab28ec37bb
   __DATA.__bss: 0x200 sha256:076a27c79e5ace2a3d47f9dd2e83e4ff6ea8872b3c2218f66c92b89b55f36560
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 47F59432-B6CB-3C3A-BDFA-E8B4BC35EC8D
+  UUID: 47EB0835-CB18-36F8-8045-9545D6E9EEFC
   Functions: 15
   Symbols:   25
   CStrings:  0
Functions:
~ sub_2a944ec58 -> sub_24911cc58 : sha256 1a377b2550bc6d0d9be615ade7c70e69d2de5b5206ab9d1b0fe38f351b3d8135 -> c27023914aa9d9a4069b793737405a203effc65b43eb6ed240f696f9803a9d9a
~ sub_2a944eca8 -> sub_24911cca8 : sha256 77d1b6f4637956508dc9c4029605fa3728102ab20a35b0fdbfc7ac1a19199bde -> ad01474cb2d0994977f7681598525917c9185f1cd5ed7aa5f38cd7abde894877
~ sub_2a944ed50 -> sub_24911cd50 : sha256 fb73c5d52d630fd6749ed018c2bfb437158ccf8c3fbaae6ba212be972e95dd85 -> a8fad497fbd2760991052956a4f302eaf95aff260ce8b78695c2aaa16487321e
~ sub_2a944ee24 -> sub_24911ce24 : sha256 25610a36e797bb477f88e61a8933f2d26afd48334cecb264a8495037cc7417c7 -> c89f89e753506a0dd5861cd5752d905eef488f6b3cf62e0180cc0679697cf607
~ sub_2a944eefc -> sub_24911cefc : sha256 82715d70c05d6f0a1daf2752fa18875f7ef64c87cfefe2d51fe57e62bb308ce5 -> 9946bd8826bba9ee943152914cb5cc31181bc1dbe1dcbefc02c596dbf356693c
~ sub_2a944f06c -> sub_24911d06c : sha256 eea3a82d8d66ceddda566ba1eca885e2bb3c76beb46fc72d05434625d60ecbbc -> 3292d2cbfe498308f2ebda8177bb4cfc9db80651c4e0259f2136e66b5c6e64de
~ sub_2a944f1fc -> sub_24911d1fc : sha256 f8c68f5cb7547d5a40714cb554ec479330468af90a33d44f1cb39df09f785883 -> 27b4ead206bb412aeaeba9273ae1b7aafd98748febacb7c8df6927d00ab31a5f
~ sub_2a944f254 -> sub_24911d254 : sha256 d6f0d89ba3a38a77ae23f240af56f2c2554e8207d1b987b83a0b08cb85fba4f8 -> 5a8b2bce408f8deefc0933d60f211ae04cdd50433ff84d6cfafc36c0c68e37a8

```
