## EAP-KRB

> `/System/Library/SystemConfiguration/PPPController.bundle/Contents/PlugIns/EAP-KRB.ppp/Contents/MacOS/EAP-KRB`

```diff

-1027.0.0.0.0
-  __TEXT.__text: 0x14c8 sha256:98682db4117d6739f9f3b5b9fc007afca38c10d112e15c793da80faf227ba60f
+1029.0.0.0.0
+  __TEXT.__text: 0x14d8 sha256:f615de78c277f2aad043d57d592845c08f3e08e4cc983fc92d694fedf7482e31
   __TEXT.__auth_stubs: 0x290 sha256:423f70601770e354a838a46126f422cedeb04ad5d8382c172ac59f2da94f7ad0
   __TEXT.__cstring: 0x2f6 sha256:37f468013e8c5b10c35d183e30f63edc3e269b4254225210a81a4c020a44e6b5
   __TEXT.__const: 0x8 sha256:78bcd0fb7c3482f2c53ac2f7e93da09d7abef179ed16b9c0e4f7f5aa6a491ddb
-  __TEXT.__unwind_info: 0xa8 sha256:f1b8eac550c04037451e9c4125919bc6b57e3146ba8039cd7d8264699a69191c
-  __DATA_CONST.__cfstring: 0x40 sha256:82b92e563a0542ea347f2f142fa80b2feced2ae56d29459071bc8175348d3fde
+  __TEXT.__unwind_info: 0xa8 sha256:6c25b515e689cac23d267907a574da0a24bae6bd900e3e27cabd5b2b6bca351d
+  __DATA_CONST.__cfstring: 0x40 sha256:badfb1592cec5b2858224bdcf4ad0fee0d9dda395ee1e217d7e729ead3487299
   __DATA_CONST.__auth_got: 0x148 sha256:a16e934ef4605501b5e9a954e64d06e96acdb75a8ffdd3ab0b1bd82c44700dc2
   __DATA_CONST.__got: 0x38 sha256:e84736f16ca41d73e24bc2de62c1dc1367a2a6044f19f4926f7fe91c40777fdc
   __DATA.__data: 0x8 sha256:64ed86b909d6d0502b64b28db0ea1272ffb358e20e9b1d88b63ccb07fa900cf5

   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Kerberos.framework/Versions/A/Kerberos
   - /usr/lib/libSystem.B.dylib
-  UUID: 0B77F14B-23C1-3CEE-AB98-2B57FB52A8D5
+  UUID: 25FEC1D5-326C-39F6-811F-478E7ACA9A91
   Functions: 21
   Symbols:   72
   CStrings:  23
Functions:
~ _Client_Init : sha256 d8dea583d8460151a594bc81fae5bcbff9de1278e4bb315f1679f9bc247c41c3 -> 0400aa5b98743f4554eb1e0247e34f9f3a076e6218dc9e6f70e9bd8f0738a113
~ _Client_Dispose : sha256 19fab4edf70e6032866d8c5812afbf716e5e4ebb03ebb18af4e30485bda23b25 -> 4c11b9736287a558e68999b4bf34abaa4bf1b374b8027163c3fcee6a2501d124
~ _Client_Authenticate : sha256 e445afe8ba017b67d187cfc7a85e477753f26554e59e57edbdda30fe711406ca -> a14ce17de04ce10a81700d499c2af578571f05d4066f7ace60cb795c81966005
~ _Server_Dispose : sha256 d31a5ff832ee7e03a1cfcad0eb7221efbfed9c3358d246978e03b424156cb0d4 -> 40df7b1b5180b2c3c9a555f69ef1e95306c208c2f14e5eb3ef504f1811dc21c7
~ _Server_Authenticate : sha256 4ee72fccc3eaedef6e27f8050cdf5a00f2b6e51688303bef4bfbb62060d4e3ca -> a1c0f15a27dce6f1a7f72b793c71886534e48bc56720c8456ea8712a3e2a5fa7
~ _Server_Authorize : sha256 f09e4374bb67352981ba2e62040b821c576c4b932bfbec530a41cea657ce391a -> 671432a65b24c26df72577ab18fdc9ce9c436fb83c7f465e9aa15aa9b87bd30c
~ _eapkrb_ui_load : sha256 436f8c76427c05d71344b8dcefeee5e7583c87bc9ca846c683082fae22c5f8bc -> 91878bf243912524814631da1418ab5d130ec58a6bb3561dc43c54a320c8f552
~ _eapkrb_ui_dispose : sha256 db53e6f8ea94a13fbd5f9629275b4b654065d91ca19c63a7fbef9c57e5f0b274 -> baf624da974ffb4ea11f805619cb86e8d39abec6713ccd7e0604900f7e3c189d
~ _eapkrb_ui_tgt : sha256 bc9769e1c329e6322ce934cc06728424165ce3ea1b615ce2c06ed1b0d50f21e8 -> 357796ff040fdd938b8efef37cca1b01b7f50d3fbddf851864a363443431c58d
~ _freeToken : sha256 9c88bd5541430f41a2118f05f390d9df8f0817d42e5fcf5da2e599f190543ade -> 4d018b4c77544a8cb6b03f606373f1a3ca391f20a542410a60f2a3f5facfceff
~ _printError : sha256 fd4f61fad79034bd4e995c1b522c9b1763119dc77e570ac1d272854c10870580 -> 03d50186ff2863807d86d610ac795b1c71ae3b7dc35de5d6113643799ccf9e5c
~ _printGSSErrors : sha256 ee3d489b9ee4c68f84dbe0f8e1f01db775cf98cc0fd9c41328c92726273b512c -> d23e96dae27fd12ecdc6cc70e286054e810bf6e78a8526cc6eb964abd0fca292
~ _Init : 844 -> 860
~ _Dispose : sha256 cf0687a0fff2b6f61a63cf57230cc47d05fea4786c8896bd03777db1dce462e0 -> d8664bc884464ff073ab3bdf0800abad3201e3fefdce6076c11cd248e4229984
~ _Process : sha256 23b825f70ae98f4317c1c3a18b8a18cc31cf4a887b92a679a850e376a6b0f906 -> 510799a5562b3d46ce7d60fe319b13d32a12b45e85b5ebc9e270abe24402c0f4
~ _InteractiveUI : sha256 63bb1a1a1fa55d9d369eea6af774b34cd0fbfa0b290e64916acb748d2dcc2681 -> 7d2e5b90a897446f34e38e1f4b62765e999a88e56cb09c65f22dd946290e530a
~ sub_1ac0 -> sub_1ad0 : sha256 e45ec392818b7d2e4c028ef09aa8fd3e4a78659b8507b9d7f9f9d8afbe80ee7c -> efb19afdf952e70260eb2244428991a392653cd959b350980efe6188aba8438b

```
