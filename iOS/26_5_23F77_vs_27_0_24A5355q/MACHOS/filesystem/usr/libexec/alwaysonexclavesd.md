## alwaysonexclavesd

> `/usr/libexec/alwaysonexclavesd`

```diff

-40.100.10.0.0
-  __TEXT.__text: 0x70 sha256:5a925749b851aaec9e62e4267643b66e733563a943c901d2ad4c3224cd6c975f
-  __TEXT.__auth_stubs: 0x50 sha256:83f3889bd9c58f1912d0e9c6e7f09ca8a93629f0d7517c03e6a073a38a706b57
-  __TEXT.__const: 0x52 sha256:307bb8b7498a57c78be32f01a3391155f2c466ca4ea54d5b229f25b6d976ae16
-  __TEXT.__cstring: 0x3b sha256:450839123a1994ba903d7d1e661db9e17a2bc8fd2179440d667c919f8c1fd92a
-  __TEXT.__swift5_entry: 0x8 sha256:4f21d891525a7c028a2696c8b11aad26afff6362e5867c8e3838005f4925bb99
-  __TEXT.__unwind_info: 0x58 sha256:616eadf918912fa336ed0a55949213bb8541a4229ab6f6095cd46b60a6a8d6a0
-  __DATA_CONST.__auth_got: 0x28 sha256:2b562e0c5d98e3f426fec6485d45f8f78ef02f706019712f97d8b7deac86b17e
+60.0.0.0.1
+  __TEXT.__text: 0x164 sha256:aaa21878b35be2607e9bca9f402aea601d92c7c294630e10d0bceebdb440c9fe
+  __TEXT.__auth_stubs: 0x80 sha256:c8f7bc52abb614065c2fd1a776fbf5367eadd7c25090cc969d9424c241e29241
+  __TEXT.__const: 0x5a sha256:2d424ff06a1cf84a4df86d69ec4b1f2893d545bb09afa0df71f19053e500dbaf
+  __TEXT.__cstring: 0xa8 sha256:bfec437fd1b997a9acf5f4e2522f51e789bbeeb5f6e0cff6dbf0dae6585cd7c4
+  __TEXT.__swift5_typeref: 0x8 sha256:41c579813372e3f260b52ff24c3c9f355c9fc1362244ea26e25f4755937e341e
+  __TEXT.__swift5_entry: 0x8 sha256:7f28d9bea29a018690174e122efa5026b3f8c199d2a083e5e73461488ce2aff2
+  __TEXT.__unwind_info: 0x60 sha256:87541061f7a01f4ae09cb48358d087cff06843191fe7ae0290cedb633c901dd3
   __DATA_CONST.__const: 0x40 sha256:f5a5fd42d16a20302798ef6ed309979b43003d2320d9f0e8ea9831a92759fb4b
-  __DATA_CONST.__objc_imageinfo: 0x8 sha256:234cedc7009d98da03ca2a7ff525d0db26b82bff0e6046456f4eda918f734526
+  __DATA_CONST.__objc_imageinfo: 0x8 sha256:885ce8037a15de89b0ceb0054c31fc3de725513307f685be388961916dadcdb0
+  __DATA_CONST.__auth_got: 0x40 sha256:0bb886e6694b925c22435e12adf7d549092a575160bb8b47fc79004fa926779b
+  __DATA_CONST.__got: 0x10 sha256:b7201f46a2a43537a73c24cd1dcba9695aea9587eb8464eb2cfa7409a4563911
+  __DATA_CONST.__auth_ptr: 0x8 sha256:db7b82219e5862d1899518b91154a698ffe338574094f66f7be342783a934a14
+  __DATA.__data: 0x8 sha256:af5570f5a1810b7af78caf4bc70a660f0df51e42baf91d4de5b2328de0e83dfc
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/AlwaysOnExclavesDaemon.framework/AlwaysOnExclavesDaemon
   - /usr/lib/libSystem.B.dylib

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 49AFE876-061D-3CC3-88D9-6527D4FB0053
-  Functions: 1
-  Symbols:   15
-  CStrings:  2
+  UUID: 21EBFF42-AA43-3779-B6F0-83361AF35ADD
+  Functions: 2
+  Symbols:   21
+  CStrings:  5
 
Symbols:
+ _$s22AlwaysOnExclavesDaemon0D0C5start5label12mach_serviceySS_SStKFZ
+ _$sSS6appendyySSF
+ _$ss11_StringGutsV4growyySiF
+ _$ss15_print_unlockedyyx_q_zts16TextOutputStreamR_r0_lF
+ _$ss17_assertionFailure__4file4line5flagss5NeverOs12StaticStringV_SSAHSus6UInt32VtF
+ _$ss26DefaultStringInterpolationVN
+ _$ss26DefaultStringInterpolationVs16TextOutputStreamsWP
+ _$ss5ErrorMp
+ _swift_getTypeByMangledNameInContext2
- _$s22AlwaysOnExclavesDaemon0D0C5label12mach_serviceACSS_SStcfc
- _$s22AlwaysOnExclavesDaemon0D0C5startyyFTj
- _swift_allocObject
CStrings:
+ " could not start AlwaysOnExclavesDaemon"
+ "Fatal error"
+ "alwaysonexclavesd/alwaysonexclavesd.swift"

```
