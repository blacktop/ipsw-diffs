## AXContainerServices

> `/System/Library/PrivateFrameworks/AXContainerServices.framework/AXContainerServices`

```diff

-3229.1.6.0.0
-  __TEXT.__text: 0x848 sha256:ab4b45d20f8958447373ecd0afd6f942f24ab9e6baa9d3411444ca0164c24956
-  __TEXT.__objc_methlist: 0x68 sha256:9e17b17429607671a12382fdd101682bbf8023725f702692d5ceaf6fceb8a1ee
+3232.3.0.0.0
+  __TEXT.__text: 0x848 sha256:ae763e8faea8101264800d4b91951cbf35603d89afd5bcdc9e619830c335547b
+  __TEXT.__objc_methlist: 0x68 sha256:f2fef4792ce8fb7198690b420f523ea143a4f24c5264633672b29584efa4f40a
   __TEXT.__const: 0x8 sha256:61ea6d291f51bed018bdd7fb80d20685e7773ed7872222c6648a8ecfbe680f88
   __TEXT.__cstring: 0x6d sha256:a76b1f931e6375d37b2a95ecdd089343c0c86a3165a6b46950308eebeb0b7771
   __TEXT.__unwind_info: 0x88 sha256:c2140911929a5fcd763aed978680842bf91d66ca2f98d17d5adb9e8b1956b553

   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x48 sha256:64256a3d93211cf7576395c98284db4cf6e0a4e224722b192fc2c0f39f882250
-  __DATA_CONST.__objc_classlist: 0x8 sha256:7d028711f7db04f07df949f123f368bdb96052e7ae7efd2b8238747593f01141
+  __DATA_CONST.__const: 0x48 sha256:2736dfb90aaab68692a6373893ff019e411b682fe8350258bf6b18cf9ebb80b8
+  __DATA_CONST.__objc_classlist: 0x8 sha256:66494677ca3647b0eeff78f6072e00a2089bb473824beb8bbe6dcf5fd7cbd7c6
   __DATA_CONST.__objc_imageinfo: 0x8 sha256:59fc9e64071aa89b9247d029e0b37ebe0fe9fc5434efb8e67b0b36435fb494cf
-  __DATA_CONST.__objc_selrefs: 0x70 sha256:4e32a933451260400ac407c8ee132cb3e2c53d3e5f437832f19a526b3da87d36
-  __DATA_CONST.__got: 0x60 sha256:6d67f477bdfd39068ac718338240ef92787d5697313ffa3a0235ab88c3c84b68
-  __AUTH_CONST.__const: 0x20 sha256:8f89c23c46e38607b77f69242e872066297aebe903393b426cd884bddbf95af2
-  __AUTH_CONST.__cfstring: 0x60 sha256:83462a29d8db072e11c1dcf7639e2bfb351cef2f2a8a6edf5c9deab7ca7caae4
-  __AUTH_CONST.__objc_const: 0xd0 sha256:31f1991daddb1e3ba02ee40bda3f49d74b548f9c0d83721d547d40f6b52abe13
+  __DATA_CONST.__objc_selrefs: 0x70 sha256:2cef6a0cd9d152a299cc289aa3699c6a1b6c001170fac7335f5a32ea4f1363d5
+  __DATA_CONST.__got: 0x60 sha256:69c077a100a925ddfddecf5f9fed9bfd08047c062fdf39d5b239d917b24bdf0d
+  __AUTH_CONST.__const: 0x20 sha256:38b296afc8a1654d4eaf16db48da6b27d49901c9e5e6e9dbde619ef2afaeaf1b
+  __AUTH_CONST.__cfstring: 0x60 sha256:fcc38289d5ecafda62cd00caa9fef3511393a7dc10c98f98e6917ad2e0da2ccf
+  __AUTH_CONST.__objc_const: 0xd0 sha256:24b76dac1f3ac22e473fb3c930b25f96ddf5de4e5cb1fee21824a707d2fb1d73
   __AUTH_CONST.__auth_got: 0x0
-  __AUTH.__objc_data: 0x50 sha256:6ba7ab014b4005479d3f693f90d86f9733099069438a972fbbb7a033277d16ed
+  __AUTH.__objc_data: 0x50 sha256:113af1f0d11bb51e57d7c2d00ba0f3315db124ab2f49ef2b98f13c3868bf41c7
   __DATA.__objc_ivar: 0x4 sha256:dc765660b06ee03dd16fd7ca5b957e8c805161ac2c4af28c5a100ab2ab432ca1
   __DATA.__bss: 0x10 sha256:374708fff7719dd5979ec875d56cd2286f6d3cf7ec317a3b25632aab28ec37bb
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/AccessibilityUtilities.framework/AccessibilityUtilities
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F07A872F-4A45-32E1-B160-25F4D2E8E998
+  UUID: 7BFBAF27-252A-3D56-9E57-DF629AA2E740
   Functions: 12
   Symbols:   90
   CStrings:  8
Functions:
~ -[AXContainerManager containerServerClient] : sha256 1cef56df9a29fd83414962f6248dff062ddfc7c887b55379252c4043c3ac4050 -> 9df4f8031c1ba889ed04bf2a1d0b9b2d95e3d127a98035b2cb2dadcabaeda0cd
~ +[AXContainerManager sharedManager] : sha256 44ee7422ccf2ce328a066b57eb0859c22992775df29ea04591a48c758852d27d -> c6c5c1bdb4e457ba74a01ad98b886a095142f6f8b1003d723e4b3ebde653442a
~ ___35+[AXContainerManager sharedManager]_block_invoke : sha256 5a7d4e396b235cc75fefce6b5dfd80949f51e73b1d9a0be9cbafe0dca100d122 -> 4fec484d8dfaf19a6bee8553673d95d65c41b2d587f62264f26d751919a7fbe9
~ -[AXContainerManager readDataForFileAtAccessibilityContainerPath:completion:] : sha256 5639b741400ace35da66cbd6cccae5c999081796948466fd916d995eb27def36 -> 8f290cca5ae25ed39d087ee47be034eebec1007050b37ab6c16e530cc34f8554
~ ___77-[AXContainerManager readDataForFileAtAccessibilityContainerPath:completion:]_block_invoke : sha256 903dd912a69b0f3baa021c812bdd71fffad94602e3057ce041686e1d9857bb4e -> 32fe098d7e9a7cb61c87a3010bfe24736bcb337b5e81fb9858b9ab532e0c8430
~ _getErrorCascading : sha256 c81f2035768735558430fe39a9f722e41f952128e721f3ab7e35d36ffdf1a64d -> 0362896f910fbf9fc5996558dacdb541b1fec822ed66a77233025234d092799d
~ -[AXContainerManager writeData:toFileAtAccessibilityContainerPath:completion:] : sha256 848d28b5c791dbcbd48adc9c7f1f53052448687bf365a79593912163bf19a1e6 -> ae696626adcfb8083eaae959649321a50664567e94dab8686fa38a1168af9867
~ ___78-[AXContainerManager writeData:toFileAtAccessibilityContainerPath:completion:]_block_invoke : sha256 32233ba5afae4d3311e232cd1520bff4b1677b88c0f79d08eb62bdfff7e3dc7a -> 7b96fabed64152b72f9eb1d6b602c225e6e0f77fb4ba2c3e03eddb2f53bcc915
~ -[AXContainerManager deleteFileAtAccessibilityContainerPath:completion:] : sha256 7f8ca65d0a8bcd0d0bc072ffe3b74d20d6c766d52a4564bfcb1f8469a03f10d2 -> 7eab6fd26b0d4bfe6a13c3ddfa70aa4a7722fa4c6c666b2119132dd299f4eac0
~ ___72-[AXContainerManager deleteFileAtAccessibilityContainerPath:completion:]_block_invoke : sha256 b15a3167d63911745b9b9880a5e05855a2768d3e139851d52f49f473baeadc74 -> 3926097e4c9aa0ad0ee14033643ff30f6748a4c40c0ea70b751f2383f424c1ea
~ -[AXContainerManager setContainerServerClient:] : sha256 0ef09e48fe31763a43bf262833c2d4f95d8181c2d4da0223cfb2810fbf52c840 -> 5d616be6d050dbb11324b70c1062d54a71728a76774e01e267d40553bd40278e
~ -[AXContainerManager .cxx_destruct] : sha256 d65777be2473100b20198c5dd6b3ea8f38387a7d01238b5019493ad2ed60878d -> fc61b3e291220963b3cf7b167afb5b8536f159e64ea688a3a980160d65d3c1b2

```
