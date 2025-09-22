## PasscodeAndBiometricsSettings

> `/System/Library/PrivateFrameworks/PasscodeAndBiometricsSettings.framework/PasscodeAndBiometricsSettings`

```diff

-14.0.0.0.0
-  __TEXT.__text: 0x306c4
+15.0.0.0.0
+  __TEXT.__text: 0x3081c
   __TEXT.__auth_stubs: 0xc40
   __TEXT.__delay_stubs: 0x2c
   __TEXT.__delay_helper: 0xc8

   __TEXT.__const: 0x4d4
   __TEXT.__gcc_except_tab: 0xad8
   __TEXT.__cstring: 0x319f
-  __TEXT.__oslogstring: 0x4690
+  __TEXT.__oslogstring: 0x46d8
   __TEXT.__dlopen_cstrs: 0x443
   __TEXT.__ustring: 0x4e
   __TEXT.__constg_swiftt: 0xe0

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 3107C24F-6884-3CFD-9B27-3075CBAB23BE
-  Functions: 1042
+  UUID: 00A25E3A-8DB4-3D15-A8D8-86FA5B7C7DA5
+  Functions: 1043
   Symbols:   3710
-  CStrings:  2387
+  CStrings:  2390
 
Functions:
~ ___56-[PABSPasscodeLockController updateAutoUnlockSpecifiers]_block_invoke : 164 -> 280
~ ___56-[PABSPasscodeLockController updateAutoUnlockSpecifiers]_block_invoke.864 : 164 -> 280
+ ___56-[PABSPasscodeLockController updateAutoUnlockSpecifiers]_block_invoke.864.cold.1
CStrings:
+ "Querying for visionUnlockiOS"
+ "Querying for visionUnlockiOS failed: %@"
+ "Querying for visionUnlockiOS succeeded: %@"
+ "Querying for watchUnlockiOS"
+ "Querying for watchUnlockiOS failed: %@"
+ "Querying for watchUnlockiOS succeeded: %@"
- "Error when querying autounlock devices: %@"
- "Querying candidate Vision devices for watchUnlockiOS"
- "Querying candidate watch devices for VisionUnlockiOS"

```
