## SystemOverride

> `/System/Library/PrivateFrameworks/SystemOverride.framework/Versions/A/SystemOverride`

```diff

-87.0.0.0.0
-  __TEXT.__text: 0x664 sha256:12dad4e2ec162d43bd69d9f349fba1e3f4d41ceddc7d4af6632af9e54a5c9cae
-  __TEXT.__objc_methlist: 0x5c sha256:a2bdf573cfd52f7256c2e0dc1c585db9bb9690a1b9f91874778cc1fb2a9b0a39
+87.0.2.0.0
+  __TEXT.__text: 0x660 sha256:9b09fb6e87445a93e24838617fc1a1fb7667fcfd70e7d97adb2fca2ccdc8ca63
+  __TEXT.__objc_methlist: 0x5c sha256:050397ad2a09b6cfaf6f4b36583d18b4afe545a090f03d407ca0c1e08b744ed1
   __TEXT.__const: 0x50 sha256:ef54e17f7bcdc20738aab1b590f702205a0b425074d892c000ef972a9ce57512
   __TEXT.__cstring: 0xb0 sha256:7f4cd2f8c48b0af2a6b08262d5612bf5f133bc4c7db568c32d5c9d220206726d
-  __TEXT.__unwind_info: 0x78 sha256:b0042e7215b0207b7a93909fd444d58b8527603fd5a16709a23304fb0e636210
+  __TEXT.__unwind_info: 0x78 sha256:98558078c20331fa0ac275352c94ca78b22899a837d850e8caa4602df08bebdf
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x10 sha256:96c4408e5471fd06302c9c5cfeb05b8bb146f23439fe30c4f0c1becbcca29e88
-  __DATA_CONST.__objc_classlist: 0x8 sha256:18b907106e1b06187dfd407a817885da8f76bf818856bb030d29b149467b33dd
+  __DATA_CONST.__const: 0x10 sha256:e26c1a721ff595108a6ad48f732aa958d4dee030d371fcfc6d05e89d8e1a8635
+  __DATA_CONST.__objc_classlist: 0x8 sha256:d0ee2c20b9ea2d41ebaddc387f4771a523225f4725dfd744ada111c496cded20
   __DATA_CONST.__objc_imageinfo: 0x8 sha256:59fc9e64071aa89b9247d029e0b37ebe0fe9fc5434efb8e67b0b36435fb494cf
-  __DATA_CONST.__objc_selrefs: 0xa8 sha256:87a0b6746d7bc9d2bf4bdc59464c74a3cef62f8fd42545768f9dd79b2ce3fac4
-  __DATA_CONST.__got: 0x48 sha256:f7cd473f38ec0b0c3f60de50172857931bfa42b0b161a954a22789882edd2407
-  __AUTH_CONST.__cfstring: 0xa0 sha256:279d1b6a9d646adcb28172514801e18d09921c8f8ba8d47dcb762e09323cb576
-  __AUTH_CONST.__objc_const: 0x90 sha256:6719a2324468b30cc95a634b1beb1a6e7b67c87f872c985c2bd20cdaf2d32744
+  __DATA_CONST.__objc_selrefs: 0xa8 sha256:536f5dc0ee33407422bdfe4ef08b135228d5bfa0e38417c33549e74f4c3ba4fb
+  __DATA_CONST.__got: 0x48 sha256:3a7e0fa282f31d85ef3b0d9b0f2c28fb1258ccb223e5f2c5d2f702440936c017
+  __AUTH_CONST.__cfstring: 0xa0 sha256:1f7abe32d359b1ff507cdb61246a40226101c52954a561c1865335ec2d821761
+  __AUTH_CONST.__objc_const: 0x90 sha256:bf75eeb7cec4432eddf7db2e3f002fafcc4694297fb5269fd9795b545698af70
   __AUTH_CONST.__auth_got: 0x0
-  __DATA_DIRTY.__objc_data: 0x50 sha256:93880498b4efbeb740782003f989fd276ae5e2a0aa97cb88d77340e9de2f26a1
+  __DATA_DIRTY.__objc_data: 0x50 sha256:1a14e5500451dc44bf4597caf86c2214440099465cdcd99f5f7c90cb541b21b5
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: D070638B-C1E9-3EF7-B0DE-9A2842795D92
+  UUID: CBF404A8-878A-3177-963A-6A738AD90422
   Functions: 10
   Symbols:   57
   CStrings:  10
Functions:
~ +[SystemOverride getSystemOverrideForKey:mountPoint:] : sha256 9be4b77967b3d5b3da143011cd0007fda7c662f9d6b9a729a4d286580f5e6eaf -> 59ed5f92b824ad0fda880cbbbd7a1840737f0087f38dd111e9fd8be73bef1682
~ _assert_valid_key : sha256 4bb9dfcaa6ab73891c1ee3f41be3090e996807c4a4f9d199cee6c487d1927985 -> e58ded5af446c20b3a25ea2967b65c544f84f5fdc17ad288413c1921cb6ff6dc
~ _get_system_overrides : sha256 080707d87795cafdaf58f94c60c3ff73498d49fbb1a7726a4e92a8e81c000909 -> 7eea2ef5ebd77ccacfea49a207dee02baf77037c14f0d7aa44865efd0f72b35e
~ +[SystemOverride getSystemOverrideForKey:] : sha256 322f8396723a28a93d85b79877b08357deb17eac9dde9884d6a392c220f931ce -> 9c6fdcc9806cda86bfbd609944369ca4160ed8c5c663f03d6ed53d6a43debe0d
~ +[SystemOverride setSystemOverrideValue:forKey:mountPoint:] : sha256 8d56cb3908bbd37fc97e31d453f1c030d93e04469e7805f965b7c922031610ed -> 593abf3cb1edf2501c74f85be9eecfab22bfb168dbf439153adfda9150da4b20
~ _set_system_overrides : sha256 6f7618f278aa14e5ee35c4e33c12c7b99e21fca7f2f048c9d616405679ef26bd -> e5ddb21133adfb19f88334653bcc0ae0b45c58f249d761058a7b98c8eedfdf07
~ +[SystemOverride setSystemOverrideValue:forKey:] : sha256 dfa683fb05a4a35702a6db477637d6b6c6b3af66ab559f383d30734b38502a1f -> 1719cffca5e0c9ef81e27b483254ad3202125589db4c4403a52fbf3957678fae
~ +[SystemOverride validSystemOverrideKeys] : sha256 4f04251144775d06be2e397c435aca8235bafffaf04d4818b5159c8eacfe8afb -> cd02b5216c8f012089b279f55e93b157532044e3a58dee068ddec8858e200321
~ +[SystemOverride resetSystemOverridesForMountPoint:] : 360 -> 356
~ +[SystemOverride resetSystemOverrides] : sha256 9edaa6c805e2a68e933b80bddcaff415d1bccf04519ebad7d13bbe2f1f7ca617 -> 8c74bceedcf95325cdcc7e8a0cece209bd631266ae24758a6ec031c4088b708f

```
