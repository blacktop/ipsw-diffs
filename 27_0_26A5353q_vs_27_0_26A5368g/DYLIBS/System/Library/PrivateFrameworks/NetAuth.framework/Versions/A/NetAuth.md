## NetAuth

> `/System/Library/PrivateFrameworks/NetAuth.framework/Versions/A/NetAuth`

```diff

-190.0.0.0.0
-  __TEXT.__text: 0xb288 sha256:a92935ad091fde429274650b04a22c08f3f2147780a3484165a3e6df803481be
-  __TEXT.__cstring: 0x7d6 sha256:c32a2feca57e5522e1cc75f83a6188b85eeb2514b9c3b22ba3ae030cf6cefa22
+193.0.0.0.0
+  __TEXT.__text: 0xb4ec sha256:8004e5d98c6fce9c58fc84c88708b6413ce51620de6de606c2141328ff3f67c8
+  __TEXT.__cstring: 0x9f6 sha256:76637a7ca650237c10431958ec536900eeb141938ca8d0c368ea67aeccb3b987
   __TEXT.__const: 0x148 sha256:bcdac47d8ef81d04e39ab146ba37d928d22386ea3bc9425e01a21b7e8256eb02
-  __TEXT.__unwind_info: 0x260 sha256:c5de8ada341e4ca82d32bb2f74e9daa56008afcd0921338448bede4773789ff8
+  __TEXT.__unwind_info: 0x268 sha256:32e1b38c449f04d2d2dac7449a4751af0b3f51eea3b27a5e800af990f125a1f8
   __TEXT.__auth_stubs: 0x0
-  __DATA_CONST.__const: 0x560 sha256:a8d5c3622018af475e981aa1d1331fc885d5e05710f3cbe96bc4f3b8435eaf0d
+  __DATA_CONST.__const: 0x560 sha256:703ec0e98037fcf1b23e72945bb82bbb0e29351d2c8402349c2cdc43323ad4d7
   __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__const: 0x768 sha256:ed28204115ef72f347cae00a253582bf25e96e8e0b6da1c455d420d07a9f32a8
-  __AUTH_CONST.__cfstring: 0x760 sha256:af6bdafc730700c29f7bb179a434af7a7a1fa55079f2147db7ecca0491911527
-  __AUTH_CONST.__auth_got: 0x288 sha256:f4bd841308415de6ed2727462cd66a7333ac8155b4e8e95de0220355189c785c
-  __DATA.__bss: 0x424 sha256:d50e2d8474134908822ade46e27717d1a22aaa2d4ebd66ee14c988ecafc01461
+  __AUTH_CONST.__const: 0x768 sha256:567ba3e470edaaf723c027da1e9b4eac2d09ceff0cbcfcc38100d1318dadff35
+  __AUTH_CONST.__cfstring: 0x840 sha256:cb9fd41d3e5997218eacc7a30ef0d2d5ba3bb1f3adb77b56eaae6b4fd733557b
+  __AUTH_CONST.__auth_got: 0x2b0 sha256:334e61fade598d87a35822d34aaa6adec70d9edb5a441ea134552eeb2afd813e
+  __DATA.__bss: 0x43c sha256:45eb891154164864eaa29c5e99f304dfd3fff33db977755c5a7add6526b577a9
   __DATA.__common: 0x38 sha256:d4817aa5497628e7c77e6b606107042bbba3130888c5f47a375e6179be789fbb
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Security.framework/Versions/A/Security
   - /System/Library/PrivateFrameworks/TCC.framework/Versions/A/TCC
   - /System/Library/PrivateFrameworks/login.framework/Versions/A/Frameworks/loginsupport.framework/Versions/A/loginsupport
   - /usr/lib/libSystem.B.dylib
-  UUID: 5E8A9A24-6359-312D-8C36-DA345427830C
-  Functions: 221
-  Symbols:   447
-  CStrings:  136
+  UUID: 6A9029C3-EEFD-3F96-93BD-7C3ABEBECD6B
+  Functions: 223
+  Symbols:   454
+  CStrings:  150
 
Symbols:
+ _CFStringFindWithOptions
+ _CFStringGetCharacterAtIndex
+ _NAMountPointPathIsVolumesRoot
+ _NAMountPointPathIsVolumesRootOrDirectChild
+ _dispatch_assert_queue_not$V2
+ _getpid
+ _sandbox_check
CStrings:
+ "NARequestTCCAccessForMountPoint: FDA required and not granted - returning kNetAuthErrorFullDiskAccessRequired"
+ "NARequestTCCAccessForMountPoint: caller is root - skipping TCC pre-check"
+ "NARequestTCCAccessForMountPoint: evaluating root bypass (uid=%d)"
+ "NSAppDataUsageDescription"
+ "NSSystemAdministrationUsageDescription"
+ "_CallerHasUsageDescriptionForService: no usage-description key for service %@ - denying"
+ "_MountPointIsInCallersContainer: caller is not sandboxed - skipping container check"
+ "_MountPointIsInCallersContainer: sandbox_check returned error %d - treating as not sandboxed"
- "NSApplicationDataUsageDescription"

```
