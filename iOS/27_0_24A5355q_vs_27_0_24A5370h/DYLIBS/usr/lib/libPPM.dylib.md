## libPPM.dylib

> `/usr/lib/libPPM.dylib`

```diff

-1177.0.0.502.4
-  __TEXT.__text: 0x11b0 sha256:2409b01b8e26487b1ee53038e00a2680425bd1b9f263ae41e793cde41908c952
-  __TEXT.__objc_methlist: 0x184 sha256:80d95bb73f2c1494500d3d331c9da1f279d2a320de55b8e4858f274c62bd9c19
+1191.0.4.502.1
+  __TEXT.__text: 0x1198 sha256:e5661d9926edc1a5babb0be9f8f5148399f7318ab35bf7c0de204150591b6bbd
+  __TEXT.__objc_methlist: 0x184 sha256:ad074c21fa5b80788d6531b14f24366fe0befe80d063ebbef72e556bfa038d99
   __TEXT.__const: 0xb8 sha256:0b8087d674d10920af1fea11aa132da066f777487eae1e9ddb3f0d528efe229a
   __TEXT.__cstring: 0x565 sha256:0ceb21cbb140493c1f513a484c47793acf5e50b2159f919a8c8196dffba6cbf3
-  __TEXT.__unwind_info: 0xb0 sha256:83cf8c82cab93f050bde7c70cd2464a51be718d760c9ba176daa0852b99ea0b8
+  __TEXT.__unwind_info: 0xb0 sha256:faf583882bbf9aaa1003e4e4c0801cc02be58344674d34a5bb846c26799b7b48
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x60 sha256:592425672b314074502ab5061e0152b73f47d9d8f3f5709615627661f3396239
-  __DATA_CONST.__objc_classlist: 0x10 sha256:5702b484d69c8163d2821f591eb5d712e73d2deccf5103a0f361798bb9253172
+  __DATA_CONST.__const: 0x60 sha256:d185c550a0f0e1cdcb507cc0607bdf07c5977aca16aa29b5489d967a59ea5e06
+  __DATA_CONST.__objc_classlist: 0x10 sha256:5f6f52c04167623d3c4806688a4efd2d9028cd4c314c74ca398e2e8b27a78061
   __DATA_CONST.__objc_imageinfo: 0x8 sha256:59fc9e64071aa89b9247d029e0b37ebe0fe9fc5434efb8e67b0b36435fb494cf
-  __DATA_CONST.__objc_selrefs: 0x118 sha256:43293d8a23d678745f18a0e72dd6cb06dbdc421cdf3a34bd9f01ea59ed10ccce
-  __DATA_CONST.__objc_superrefs: 0x8 sha256:be4f3dd991fc77cce212d8d4c9af3373bb6aaa925d1678de70c4109fb6d1fa4e
-  __DATA_CONST.__got: 0x48 sha256:6ad400b4f208982b27be746c9a8ae4524507fa8a3b6e185f820690038afa1ca4
-  __AUTH_CONST.__cfstring: 0x420 sha256:7177937ecd3819d7707b68571ad5421f76788619e138ee25795bd2a8c132fa48
-  __AUTH_CONST.__objc_const: 0x260 sha256:da97da1169a4e6cf5d80dcc978679121799309651d22cf44667fdf43ca6c8bcd
+  __DATA_CONST.__objc_selrefs: 0x118 sha256:409fe846f9d9cb3b590cb6052e375186b45a9e2d170cf688d75405e191fc3fa4
+  __DATA_CONST.__objc_superrefs: 0x8 sha256:7d5ad4b22f27c2cb3d73ddcc38b8b3cd8f3fd8084b88309e4e7857ff0295ede0
+  __DATA_CONST.__got: 0x48 sha256:072660c9a6cce16185bbd51435f4f0bbdc81611bfe0683a7c224a04258f1d95a
+  __AUTH_CONST.__cfstring: 0x420 sha256:8de7c40b204a979366b6fab7105cf300a4d22c211d6bcece1594281df1c3137e
+  __AUTH_CONST.__objc_const: 0x260 sha256:e6fa3f38a9f415e12be3d82154eaf49f840e4928f0ae0e61d301fa463c15b426
   __AUTH_CONST.__auth_got: 0x0
   __DATA.__objc_ivar: 0x18 sha256:913850c783ba5c7fc4aa79c39e100dcf127ec84a398d649d08e50d00274f0c46
-  __DATA_DIRTY.__objc_data: 0xa0 sha256:d4afe8a73acd7a6759b2f5a42aa34013a3fbfc94a208d42c3bed3e6288e82f97
+  __DATA_DIRTY.__objc_data: 0xa0 sha256:e36307023df7e430730888a29e68a50cca3a28b55040d2a24a3122ce565a9835
   __DATA_DIRTY.__bss: 0x20 sha256:66687aadf862bd776c8fc18b8e9f8e20089714856ee233b3902a591d0d5f2925
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: D18B4F05-B86A-3721-8A00-785A8EAE9004
+  UUID: E1D5303F-B7C0-3922-90ED-FD66B03F7CD2
   Functions: 32
   Symbols:   180
   CStrings:  72
Functions:
~ -[PPMClient initWithClientIdentifier:] : sha256 1703d65dc24c12a09b157a33de04ce913ec7e9a5681a48072eab09abe2f33510 -> f33ac6c4d958edfde7bfd313c12e7038b3bdb6a55331cce243443d33977db52a
~ +[PPMClient sharedInstanceWithClientRepresentation:error:] : sha256 6f6e3196d94ba4ce6b1826b2f1e9efc64aab50bf77752d0268ef981b7e5943f5 -> 07c9ef69ebba6646c9fac738c80bdfcb5022702b4e937cfa93c30c2a4d127bc8
~ +[PPMClient sharedInstanceWithClientRepresentation:options:error:] : sha256 628e99647f83a9038b51431451d489b4571722b8add15655084667e12cf8e5df -> 0e692c1ee9b817818aba8e921ece71572b8a210ae3cc5ac4ee0de1cd7f5760e9
~ ___66+[PPMClient sharedInstanceWithClientRepresentation:options:error:]_block_invoke : sha256 0b7672e42dccab27ba0c1ae934c7fa7f43e7eeadbe7097fc50bfa8fde9951bed -> 1bd606b983db70620803a5b843fcc0153c9476255ec8734b77190adc17007259
~ -[PPMClient getClientNumber:] : sha256 2c8a75e9a78abad2264675bc5d780b5dbd7b89e020dff31234102d3b5b48ebac -> 84b34abef274443f87e5a2e0ee20feb65eec1232c7d4676755503c832733e9b5
~ -[PPMClient registerForNotificationsWithError:handler:] : sha256 cddaf667cea9dd644bfd4b0ab20d5dabc7057492e536e40a8a39bcd478cf9563 -> f9c181f28b33e9b9cdc34c95d7cf11926362f0a0e637b9cae224e4f72f1b18c7
~ _budgetNotificationCallback : sha256 1baa69f618d66bbbf54d9c0af9130fdbc97b57f2b4b72b34bd631625dc7751ab -> 16da8e8339bde6f82804bd5aeba6a7d91d79170fd295a4c6cd70876241df7649
~ -[PPMClient initWithClient:error:] : sha256 b091e1c63ed994b0cdd4e569370c9d5b21f784a4674a9f063541b9d712a3c37b -> 5dfa2eb7791184bed000e88a59ef87f2432bf9064db8ec8516118c5514799146
~ -[PPMClient setupIOKitUserClientWith:error:] : sha256 c03adc7fef05dc271e681184bdbfa8a32de924ea6dfb9126b9339e0ea9559f59 -> 276367c34d74e9e5c980921c35e40ae9e3b2ef4a84364352e98724e2a55575ae
~ -[PPMClient admissionCheckWithLevel:options:error:handler:] : sha256 c5d8e43d6dfd9f5db573d7accaead92cc2b702fbbc1c5380b04c9505c28c4ea8 -> c7b81ab86bb2f7fcd17443727bb1bb080e37bb16261e6846de81d2a39eae1c96
~ -[PPMClient activityStoppedWithLevel:options:error:] : sha256 837c23a640f1a0c90b4b3e7296ccad4699ea871e5e7de00adb9a6a26859aa5f8 -> 2f809f3b9d65a4c5128e3b71a7bccd3a973325615cb57af41c346422d41467ab
~ -[PPMClient activityStartedWithLevel:options:error:] : sha256 91caac9450058812fa3e98dc50393aaf24165aeb3664bb2927fd23b19f78ff5b -> ecc960dc58acd02b329a4a716589f31e9b30829dc9756505d8d777af1e307b44
~ -[PPMClient pushTelemetryToPPM:error:] : 980 -> 956
~ -[PPMClient userClient] : sha256 a26e6674d9b8ef474f559c591d953f4cd7f4a50713ea618d946f644177759f39 -> 54d9402b14c8fc53bfce7b808f691d0b2c73c19acde716da07cd2bff812f3857
~ -[PPMClient setUserClient:] : sha256 a1707b719ece00a899941fb22d90eabdfa6be8c321cbb1a7a79722eec7fcbb63 -> 204855d0e7869727ee6fb5263d66e134a232348f395ca46a29104fe216a91e40
~ -[PPMClient identifier] : sha256 0f3b82eedf3278cf6178321e5da3e0356413412bc0692013a2109a628ddde771 -> 0c709f5ca6a95632eeaff66129cf1a8b6f7f0b55b1f0b28fa13dccd5e35b52a2
~ -[PPMClient setIdentifier:] : sha256 cb0ae3cfa7e652d09f802550a7ba249004b8fb11068a0f93d91a10dd56aeb98c -> a9817b98c0df56724b7201b9f090174d62ada0ebec09fa2d8ab155481c7f9ffd
~ -[PPMClient .cxx_destruct] : sha256 36cf9b693ed9700edb416fb23f3aaf9b26de227d89300f9bda1886f20ad335ba -> 5705e174c0f665660dd10a87c31ccd8bdd5447ff7b7b7f4c7893034c4aa3c1d4
~ -[PPMClientUserClientInterface openPPMUserClient:clientNumber:] : sha256 66a285f2ca93370e5b85dad4ee341d24dc9055a03ce19fb2643bbafa0d99faaf -> 5a83805f2a2060b147221eb262456b42378ea7ee2cba3769af663126bc63e38d
~ -[PPMClientUserClientInterface admissionCheckOfValuePPM:clientNumber:level:result:] : sha256 7d8a39da33e579a4ada4e004d0c83f44580928e7d7c7d583d37825b53a1d82e0 -> 5f8b997756f9e621691b60d9f64106ad74207c2be46f37f79ab476fc194fa5ce
~ -[PPMClientUserClientInterface stopActivity:clientNumber:level:] : sha256 ee4a999dfc292c5bae4b3042963ca40a2f7dccb6cd37e741fdb1af972f179713 -> c17feab9c1ab5d9ed9e35d0df00741d8cb94f66a681ec6ee50732a5fe4163b58
~ -[PPMClientUserClientInterface startActivity:clientNumber:level:] : sha256 57cbb5093590a47eec02e38847c5b6ac158a453ae122a42d62ac3013025e563b -> 9d7d3867627b610aad8dd4f4b31aeae3ea85349ab397f0aaf85519f69be9c728
~ -[PPMClientUserClientInterface setBudget:clientNumber:value:] : sha256 32f0daa9703fcde7f2fb388634d9d28b9e35ee6280e6cb6be6bee3899de41eb5 -> 9ea7eb75497ca4255189d14e6760c0596c8e78806ad1d865c12c15bfce9782a6
~ -[PPMClientUserClientInterface setDebugFlag:value:] : sha256 b86def7e31cad1c932c8a919353ca9932dcda288beb8ecdfa98911046fc7c563 -> 02accf0909b2ac6e5dce8290f520ef4524ab76548c22f97e168c9a1cb9187083
~ -[PPMClientUserClientInterface pushTelemetry:userDictRef:] : sha256 bc366b266583194fa1f3761d688def650cb4d7b258be37cf5e68dc7d6f91c044 -> 9f2c5c8f30402ceaba23f4c7946aec59cfc1588f0b57135d42ec13984f624b04

```
