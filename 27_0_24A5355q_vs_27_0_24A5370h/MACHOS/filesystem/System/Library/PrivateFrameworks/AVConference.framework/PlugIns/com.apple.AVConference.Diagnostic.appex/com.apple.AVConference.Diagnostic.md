## com.apple.AVConference.Diagnostic

> `/System/Library/PrivateFrameworks/AVConference.framework/PlugIns/com.apple.AVConference.Diagnostic.appex/com.apple.AVConference.Diagnostic`

```diff

-2235.48.1.0.0
-  __TEXT.__text: 0x104c sha256:b39ca4efd01731e1a3750767633311fe46a82c91704dbe1b1e264f94ea462f0e
+2235.52.1.11.1
+  __TEXT.__text: 0x1048 sha256:02692933db5ba3991629ceeb24f0eafcd0dc5533a1ac3298740d739d04f65bac
   __TEXT.__auth_stubs: 0x210 sha256:4dbe994e1f9c8af807cec7259d34e668aecbe5a4d092c102a0667ebd4797ca93
   __TEXT.__objc_stubs: 0x4e0 sha256:63be20fa2eb627b8a6a4717b3469df9d7ae37d9f89d6f7960b6cc49803b2d702
-  __TEXT.__objc_methlist: 0xb0 sha256:b85ba027dcc75013b8192ebbf125f9144b8188efcb0bc1720997139efb347468
+  __TEXT.__objc_methlist: 0xb0 sha256:05728319c61e8523f20b6db3ddb5a20cdd43850c62adff468ae35159b8fdaf9a
   __TEXT.__const: 0x88 sha256:a9f50d82ac9235f5936120a703f7c51188b92bd09410284ceacdd071ffa8be96
   __TEXT.__cstring: 0x270 sha256:b0b24ad54dbd3a9095ac06254f4e1bece4ec8938dcbb768513718cf008e7f2fa
   __TEXT.__oslogstring: 0x3c1 sha256:d3fa08ea911f4530afedd7b1de8a6af26ba2a2b5d7821e8558d2e65b50829c0a
   __TEXT.__objc_classname: 0x2b sha256:551da86c59a296cc2d976c5e05c316ab5a478e67d161f7c2962b6a36e7cf535f
   __TEXT.__objc_methname: 0x408 sha256:13d0ccaed7724dcb83e2f859c7e0019f11b3ade0fdd1078825e88d0b802d795d
   __TEXT.__objc_methtype: 0x55 sha256:70ad46dac6564f96d61257800567ad352cb61756b33bd0d33395513437d38990
-  __TEXT.__unwind_info: 0x90 sha256:86787a5a9b0ca2df5427d5d95b174e2ee274f7ceb348f8cea8bb789cb43f05aa
-  __DATA_CONST.__const: 0x40 sha256:ea7b43ad92545bc437a5720d1d4703da6b2a381af03ac99b3bece75a10ee4d6e
+  __TEXT.__unwind_info: 0x90 sha256:ac5e4bac408874282e86bf06299e26912b38c454d2792003143aed6c700cc5b1
+  __DATA_CONST.__const: 0x40 sha256:1e856a6d8cbb3a5955c356a6b37438c559ff2eb58d55f2b6b18ad019e2467215
   __DATA_CONST.__cfstring: 0x320 sha256:fe5170ee2a767db7642476766383a7d525d7ff6aa5215b7647c4ec0afa445047
   __DATA_CONST.__objc_classlist: 0x8 sha256:545ddab617b008ce2c06c146627b6de588af51267d4f3565c761357c4053f975
   __DATA_CONST.__objc_imageinfo: 0x8 sha256:1fa65ffcccc24c72d5d7f804a2be05ae57dfbb8769ffb33c4272ed6795b7e61c

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: D666E3B2-9582-3EB3-A6BB-2603F0C85A00
+  UUID: 6BB0116D-D05F-3EE6-AB6A-103B4D28D517
   Functions: 20
   Symbols:   127
   CStrings:  116
Functions:
~ +[com_apple_AVConference_DiagnosticExtension realHomeDirectory] : sha256 e2e1392f36e054d86e7d058fa9a7a3b7ebad5ed75ae608a60e1b986046e21ec8 -> acc5d4ff8f1dd81329ae6f1db7a26dab30fb0e1ccd0a03294715c1ec01528656
~ -[com_apple_AVConference_DiagnosticExtension copyDirectory:withPredicate:toSubDirectory:] : 872 -> 868
~ -[com_apple_AVConference_DiagnosticExtension copyFile:withPredicate:toSaveDirectory:] : sha256 3ed8d937b13fa8a05d7c8f8ac36d428204d34dd83902d23b1b325a0951f01834 -> 4b28d7a21aff00dacf66736451c5813a370664243b93423b37fdd802f81c991f
~ -[com_apple_AVConference_DiagnosticExtension copyStackshotsAndCrashes] : sha256 d33d7734d086e3e319aaacab03783c68d5cdb8ac035baa4b0e550018b4713ada -> 685d79dd478acea89ccf5bbb3aadfe4c65ff39c2868a3732533ebe66060723d8
~ -[com_apple_AVConference_DiagnosticExtension copySpindumps] : sha256 b8cc90e3f593256a5b5afebf0499777d864eb7f0494b6cc72a8757cb0c74a4b1 -> f2453fef4278900b7c0db5923551ca038d3de8c97a26efbb670e9647edc60a34
~ -[com_apple_AVConference_DiagnosticExtension copyDumps] : sha256 7fe8fc4987967e3e34ea1f0840bb08102b4ead680f8e85a9f2351b62a7ab4f67 -> 04c49a92ae04e8844785e1105970c3b2ad188a931934fc6f77297ad7c443a050
~ -[com_apple_AVConference_DiagnosticExtension copyRTCReporting] : sha256 4da9e9f05e16bf4bf7698c56283b8ebb0e5533f38ae41082d14122fe25695820 -> b84fb3afafb68ab79e10ee6787394caf6f032a3e886d4e5f3e83cfdb4d31e7e9
~ -[com_apple_AVConference_DiagnosticExtension attachmentsForParameters:withProgressHandler:] : sha256 d3e5f0d4c86296093a039041b44212df90d4e6195eed6f98907c21f16ed6ae67 -> 03df94baafef35dc438c06dcdd00e08d7fc3ed57009c8b35a26b868cfbc64088
~ __89-[com_apple_AVConference_DiagnosticExtension copyDirectory:withPredicate:toSubDirectory:]_block_invoke.cold.1 : sha256 a95822fc2c53c373eadb8704a5e8eebfb52be47f6fe254614da30b58974fe426 -> 0d3db28eca698701fa91e6a75b66c223e63617ec973f54822ae80236401c4fec
~ -[com_apple_AVConference_DiagnosticExtension copyFile:withPredicate:toSaveDirectory:].cold.1 : sha256 20323668e568cbbf57d70cdc741ec078748aa2b49343d27c969254a60d996f7a -> a7ea894193ae688a7f4c7d71b38cf9249b061cb785b58973a571decd7c08f606

```
