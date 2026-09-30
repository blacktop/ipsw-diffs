## ARKit

> `/System/Library/Frameworks/ARKit.framework/ARKit`

```diff

-746.100.4.0.0
-  __TEXT.__text: 0xb54 sha256:d02c7faecacdc8c18b6df344e084b21864abbd58a8272410e9e52db1d4e6d3ab
-  __TEXT.__auth_stubs: 0x1a0 sha256:89fe3f07387bdedb8e9f957375934b60e250c2b2a1c6ac76a9907cc07951949f
-  __TEXT.__const: 0x40 sha256:f1e94f5e5d0e542edfeb8d0818d2a67d5742a028176a59f78fd10b3f69c8b5ca
+779.0.0.0.5
+  __TEXT.__text: 0xab0 sha256:eb8906786d9412d93a7e5cf41b253a1ae546c63a2e23a353a0e84e87c96c9aa5
+  __TEXT.__const: 0x40 sha256:95015faa9b9bad9c0cb5f244130bac2c79aa12fe5732f0e16079f452d62cc377
   __TEXT.__cstring: 0x111 sha256:2b95afe41fa9cd23f73c353f2c1be7a45ec104812243524cb37b9eb7695f0149
   __TEXT.__oslogstring: 0xb sha256:8f07885ef5796a973d8f6b2156e6f9ccb7542fd099242e8a12e80b0e1b6730c6
   __TEXT.__ustring: 0x5a sha256:09538d5328a2261bd4ab9d67a478d2e638f5612284f6cd7919c13ea565b2cc36
-  __TEXT.__unwind_info: 0xb0 sha256:4ecbb0a0a07234afc8736dc835d79c9f6c62a5306c24781a745d1693584eb147
-  __TEXT.__objc_methname: 0xd2 sha256:61ff8912794d44910ab4b5aacc5dd35ea2f1a0e303c52255dddc62c67d0b985f
-  __TEXT.__objc_stubs: 0x160 sha256:f6a7338b137318b67827bd18b7be457963a43486a3ed57037c284e50a315a7a7
-  __DATA_CONST.__got: 0x30 sha256:17b0761f87b081d5cf10757ccc89f12be355c70e2e29df288b65b30710dcbcd1
-  __DATA_CONST.__const: 0x68 sha256:acf62ccada1f84f8584276a0eec0690be5c85dbb949a384ff4cc21cf9ab93e00
+  __TEXT.__unwind_info: 0xb0 sha256:ad204b1373708a5e684e55457093b66a7984fb633739b105e97a31b89b06e6e4
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_methname: 0x0
+  __DATA_CONST.__const: 0x68 sha256:8e383807e8747e9a97484493e8790f49eda5c6409569b3b53261cb4c75aa8fb1
   __DATA_CONST.__objc_imageinfo: 0x8 sha256:59fc9e64071aa89b9247d029e0b37ebe0fe9fc5434efb8e67b0b36435fb494cf
-  __DATA_CONST.__objc_selrefs: 0x58 sha256:5f39244a9881cb33a468f396a5d6d15f42b91a5bc1e890377a19081629cba49f
-  __AUTH_CONST.__auth_got: 0xd8 sha256:a5645e7a3fa0866cde8842c4dab96567507c3d1a3c028b816bc63f6966367b70
-  __AUTH_CONST.__const: 0x40 sha256:0595aaea096609211c44e9417e6c322c75edea7c31bcc83f8399a9db8a02ae70
-  __AUTH_CONST.__cfstring: 0x260 sha256:2da4862cbfb572dfe61b365b516fdc2407463761a866b67f8ed802ef1fbdc287
+  __DATA_CONST.__objc_selrefs: 0x58 sha256:c19d3599d685305d5c0a65d47579e745728631cb13f15727d2ef767e03b69599
+  __DATA_CONST.__got: 0x0
+  __AUTH_CONST.__const: 0x40 sha256:d684ed00909b06db17bf2fe90a44d9573008693f2d581004cde2bf6f2e62bc81
+  __AUTH_CONST.__cfstring: 0x260 sha256:8692d25ddb7de9463ff6c1f1b565366ad80915452ee998ebd1cd1b6262de33a7
+  __AUTH_CONST.__auth_got: 0x0
   __DATA.__bss: 0x20 sha256:66687aadf862bd776c8fc18b8e9f8e20089714856ee233b3902a591d0d5f2925
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
-  - /System/Library/PrivateFrameworks/ARKitCore.framework/ARKitCore
-  - /System/Library/PrivateFrameworks/ARKitFoundation.framework/ARKitFoundation
-  - /System/Library/PrivateFrameworks/ARKitUI.framework/ARKitUI
+  - /System/Library/SubFrameworks/ARKitCore.framework/ARKitCore
+  - /System/Library/SubFrameworks/ARKitFoundation.framework/ARKitFoundation
+  - /System/Library/SubFrameworks/ARKitUI.framework/ARKitUI
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 5135DD85-BA18-3CD0-9E84-42A2E1BB0D4A
+  UUID: 214BD0A5-832B-3342-B326-2BB897164631
   Functions: 26
-  Symbols:   95
-  CStrings:  43
+  Symbols:   94
+  CStrings:  32
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
- ___stack_chk_fail
- ___stack_chk_guard
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x19
- _objc_retain_x21
Functions:
~ _ARFileDescriptorIsTTY : sha256 6544db2f191435e6fffea072a9ffd447da08f43de52832b8489e2f87f2ed716a -> 9a2e079a5d270684a29756a8cb569f5ef95ce7227999755e8b048346a52a92c3
~ ___ARFileDescriptorIsTTY_block_invoke : 140 -> 128
~ __printFormat : 260 -> 212
~ __ARLogGeneral : 84 -> 68
~ __printMessageWithColor : 332 -> 288
~ _printMessage : sha256 320919e9faf36e5d6f2d71f5c4bfc7203aa429a750764d462eef411cc2c32cc9 -> afdee1c87cb9694d942670777d45083d506ece28d723625e90f282d8caf79c3c
~ __printMessage : sha256 ad9718da243c9e9bec49a15de4c320327661495cf7bd2f4db9c8ad3d3569c50f -> ea17c7ee224e21a0b2659cab7dc7495cccec50cf2d9d2855b4f3b08293b64f2e
~ _printVector3 : sha256 fda2963fb46c002ffb16a44d362ed6685e3be19c92a3b7e876837287974bbb62 -> 4a30e3b3f42157b5f8c764d1cfdd257b5032ee82e4a6aaa337e203a33a7129d1
~ __printError : 232 -> 224
~ __printInfo : 232 -> 224
~ __printWarning : 232 -> 224
~ __printColoredMessage : sha256 0ca7d8dc52a32b9db11046cf9ac9095b4e7b780aeb712df854ceef0ce69bebcb -> 990a5acc4457a3dd4d8e749a5da30645cc9a7ff7e5363c6553e4f53cd6fe52a9
~ _ARPrintUsageStrings : sha256 bf47578f53517f76beee92297c51412d5c32db8792f05b943398819dfa3fb4c4 -> 3d284c136ab4170f0082d32482ba65f59dda31d865494bb93b267ed82bf3d6b5
~ _ARPrintToiTerm : 140 -> 132
~ _ARPrintEscapeEnableAlternativeBuffer : sha256 c7d146550b5f02061196cfb971aef7253b26e36f4b89e3a2280c084539bec123 -> 1dc10cacc31c83340baf7852ec2a4740c5ebe5e7bd5289a268ec38fff8862421
~ _ARPrintEscapeDisableAlternativeBuffer : sha256 600bd8acb08028c1d44b8387953fda1eec9d11b5982703dc02fe8d1e2dfc7d15 -> dd130a9c2814b6b01ff52f7d78f91973363ae64b7d64a3c1d12ef8297e0ef3a7
~ _ARPrintEscapeEraseScreen : sha256 ff8767c51f5f93e968d74b9251831356e4e13d8090e92ea66ba5a17b0ea68b0f -> 2f65e4dbd592a8e83b8a6f794fdccfb71544768ca67c8e3c784590b021409785
~ _ARPrintEscapeMoveToLocation : sha256 8abcc1acb77df116e50feb023fbd59d6cf908f1bfbabc66fb1cf96b3842575de -> 4fa92437ff76d1a338a81e99d8fad3cd21aebe802e45330af9e5c0ae990ee31c
~ ____ARLogGeneral_block_invoke : sha256 fb7916aa6a679a8f3003a023b00787fca626eb75c035cf6f4d9b5592836d7827 -> 6b327f0dcea78e29af8f1b90c8572c3051cf240b0e4a80d240fdb276a7fef5c0
~ _ARKitBuildVersionString : 144 -> 132
~ _ARFileDescriptorIsTTY.cold.1 : sha256 b2692cf802a0f44b3140ba72e810785273226b38e95992c69ba56f89f24f2705 -> 5544c1b3b84145044dc1f217ea27c460ab96b2b6f9d4b693f788b8b59f779cfb
~ __ARLogGeneral.cold.1 : sha256 a8acda8cb14c6492e638cea3741481e3942914eb3c0062c31091713da0dce25a -> c13bd2f08f7eca2f43e409752ae8c59de34f6f85a8aa21138fa8ba1f62d590be
CStrings:
- "UTF8String"
- "_bundleWithIdentifier:andLibraryName:"
- "base64EncodedStringWithOptions:"
- "environment"
- "infoDictionary"
- "initWithFormat:arguments:"
- "length"
- "objectForKey:"
- "objectForKeyedSubscript:"
- "processInfo"
- "stringWithFormat:"

```
