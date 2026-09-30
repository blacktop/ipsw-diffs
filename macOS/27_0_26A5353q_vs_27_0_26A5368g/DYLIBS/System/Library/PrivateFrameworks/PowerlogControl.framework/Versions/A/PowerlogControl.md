## PowerlogControl

> `/System/Library/PrivateFrameworks/PowerlogControl.framework/Versions/A/PowerlogControl`

```diff

-3468.0.0.0.0
-  __TEXT.__text: 0x730 sha256:8d644d09c5ccce1acdce60ab9388f1b7bf453ee5006e2cc800624bad871819a2
-  __TEXT.__const: 0x48 sha256:6b44380a71e1e89fe660ee4a4a4cee8074abddee76a21d457f011e33da97d81d
+3486.0.21.501.2
+  __TEXT.__text: 0x730 sha256:03a91e04e28e2558eda5023288c1d9d6f71dc15b18194ebb6351d73bec3da446
+  __TEXT.__const: 0x50 sha256:9f81ee3ca31c3aa7dc4829a0027a1a81663efcfa063ad332ee64a26280a0724b
   __TEXT.__cstring: 0x88 sha256:f3a2cd99a15a7149d224998bee144757539e6e60c482f87f253ae32169b79a85
   __TEXT.__oslogstring: 0xdd sha256:6d7e3e4d3223f63bfee3c0332bcb08c12daf970f8762e0f7442ff55fa5cd30ca
   __TEXT.__unwind_info: 0x80 sha256:7d10173e698f425639db263ba11d67fe33f9b50a7f1eefdadfd297f46c361777
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_methname: 0x0
-  __DATA_CONST.__const: 0x40 sha256:6158aa67afafaf3992fb914e5692fb8cb8ded6dea5f74edfecd9154fbdbf60b2
+  __DATA_CONST.__const: 0x40 sha256:c497be8037f3590ac3d58db65c98fb1f7636ac86fb80e5ef6242dbbf476c3600
   __DATA_CONST.__objc_imageinfo: 0x8 sha256:59fc9e64071aa89b9247d029e0b37ebe0fe9fc5434efb8e67b0b36435fb494cf
-  __DATA_CONST.__objc_selrefs: 0x40 sha256:b9a4924cd85b5114be0ccf06ba7ccba56526f57f6948afd00c97f273269fed48
+  __DATA_CONST.__objc_selrefs: 0x40 sha256:66cf5818977ad688a6897adf5f3acf7cdb40caee4986dddffbb21f56b8735ced
   __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__const: 0x20 sha256:d0a1738c033a548b933f372ee4636adf16cadb116c27cbe11e086f63827f33ac
-  __AUTH_CONST.__cfstring: 0xc0 sha256:f810525aea3506496d8dbbeca42c44ce96c9238e351b2de4056646207ab89aac
+  __AUTH_CONST.__const: 0x20 sha256:89e933067c0fdddc52d79b4a7a2cd27476f558de99fe8ea7530194f6faef4a89
+  __AUTH_CONST.__cfstring: 0xc0 sha256:97aec2a5e3bc7dbc8114657a630d15a53f9dcab316b84167d6585d3e20c19189
   __AUTH_CONST.__auth_got: 0x0
   __DATA.__bss: 0x10 sha256:374708fff7719dd5979ec875d56cd2286f6d3cf7ec317a3b25632aab28ec37bb
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: D4F18F04-3208-3AF6-A48C-E9F848F03EFF
+  UUID: D162C59F-0222-30D1-B6E1-2D68C8D264EC
   Functions: 14
   Symbols:   57
   CStrings:  22
Functions:
~ _PowerlogControlLog : sha256 d03689a99f2623104441c21a76b7f24195cfaf79115d086a87f5c064f047c415 -> c7bade1ec077be935e080acff248dbada95d81e723c1b0ed4e839d596f37ec36
~ ___PowerlogControlLog_block_invoke : sha256 60ef9e410aaf8ac589612b810e345e955964b4e3ca8c244362fe57bbb1dea5b4 -> d7215e61ee6bdf199c64de6997f8e62bf10c892a1b7374119ca8bb1af41220d2
~ _containerPath : sha256 e7a7fa731084db70e166bea87fb4e38a28fe93212c445ca76f217ea2602af3ff -> fb8e5f2b7eb56ec711d04baf84c9d909865a7ffd551915ab53a5e7b30c2e5b84
~ _allowModeTransition : sha256 399529945edb8762a8481c624345f23f58ec689b6c27eab7375aa85a394652ad -> aca57d05e88462082f27e0eab29d10ae3acfa043fe8c317b78829f818dbac52b
~ _validValue : sha256 5791e2c47cbd3cf57614def8fcf4ba88924680a4ce23481e33920acf0b156813 -> 67d982bc9f8670b3c28aaf57d15e79f580ab9f50a82182db516ba94657d1f9cc
~ _PowerlogControlReadMode : sha256 0fd0ca41d78f8f30c00b867b7da7de9f779871936ec2e7e49799ea9d1cd35ceb -> 572f037c802e6c5102d51ac80a63af243033e39c7b5433637db3adfd8397883b
~ _PowerlogControlDefaultsChanged : sha256 eafaf08a21818c4876738fed7af8d8187d29b909386a01e3971aec4e56fe4649 -> c02bab6c50532a8f955c0e6bd513418a7f4f17141ab490872e7a75840e0ff65d
~ _PowerlogControlSwitchMode : sha256 e8e0b147e85606c93b5ed10f32a07cd819ad72c1ba6aa002a5c7be10971589ee -> 894a9384f6f415929a4d04912d21afea7e5542a3a44dfa549e46b9fc206bce60
~ PowerlogControlLog.cold.1 : sha256 89c5c6c1a98ad9ef1de927a9632dceb958acafc9784892146d10b69c55c5acfa -> 41414685d4bd034704842e85b0b3f1baa82f6a1063f2864da589452fb9a748ed
~ allowModeTransition.cold.1 : sha256 28c549a36b3e8c3a84c3721e58db055415c1ceed105c4073ca84916ffe60e1ef -> 7b0da14c737caa8c2e45ad19f6f689f196cb458d213e9b9faf6ae27127e098db
~ PowerlogControlReadMode.cold.1 : sha256 3fde3592c82ac791071d318d30f509e147955f4e24fb75286731cf98f6995370 -> 23b38242bf4ccd8c30b74f3620b9c609aea8793f3107be76ebabdec8fe209ea5
~ PowerlogControlSwitchMode.cold.1 : sha256 b5d33c65aaf382624edd439d428e1b4a1404eef7a2e58dce81282b2876a96e81 -> e5207d066c61c9b452965e52169879220a8bf96d65eb9f4759f82f069f6ef91e
~ PowerlogControlSwitchMode.cold.2 : sha256 a5224d11c6219e2dfdb79a419c167282ed83543ee140fc639df777a6fcc63fff -> 5bc444b4a635548c3f258051df96bdca9a0e2da529e9b04bcd6f6014f1ae77a0

```
