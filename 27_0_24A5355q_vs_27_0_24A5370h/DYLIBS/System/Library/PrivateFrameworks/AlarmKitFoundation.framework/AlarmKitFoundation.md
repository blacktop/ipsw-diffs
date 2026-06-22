## AlarmKitFoundation

> `/System/Library/PrivateFrameworks/AlarmKitFoundation.framework/AlarmKitFoundation`

```diff

-2327.0.1.0.0
-  __TEXT.__text: 0x608 sha256:6654d4aaf7cb1095b70baab805b0999ce7167af99ef2a6caa3797378962e034f
-  __TEXT.__objc_methlist: 0x1e8 sha256:41b8bd609694f413b7cb38e1f404011d8d7ef3bbb48bf743f3e3e25b8314f312
+2328.0.0.0.0
+  __TEXT.__text: 0x608 sha256:b2799c127c38f31a27679c25e1a218c2f3f879202d26c4605cd83914c8a49c1d
+  __TEXT.__objc_methlist: 0x1e8 sha256:87f4529f4bc5a578cc16bd4ee986dc5a6448863ade256d01b2c08167fa512a18
   __TEXT.__const: 0x40 sha256:fdd000a7411d1118bda81f1b4e2068223de8bbb4ab1534efbe320b690b5d0578
   __TEXT.__cstring: 0x8 sha256:9362b1c964211c18f15b662c8577c3c2a8b0d0ba27da0d8bb700ef708166e5a9
   __TEXT.__unwind_info: 0x98 sha256:184b8fba78da4cbf9939f5545440a8662a1fddf91149eebca4e4352ac03d1540

   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__objc_classlist: 0x30 sha256:3de90938069838e317e0c6ef3538197abd07ce4d848ec41f6a17e99a0f56be3e
+  __DATA_CONST.__objc_classlist: 0x30 sha256:0a88637ab4d0fe3a070b5da66584fb479572f9831cb4088dacbe3daa74679099
   __DATA_CONST.__objc_imageinfo: 0x8 sha256:59fc9e64071aa89b9247d029e0b37ebe0fe9fc5434efb8e67b0b36435fb494cf
-  __DATA_CONST.__objc_selrefs: 0x100 sha256:4a05208bb8a1aabcd37ee1e6af920d6a325d863b615077f5bb60010c55569e11
-  __DATA_CONST.__objc_superrefs: 0x30 sha256:ff99b3605f9864a69e22e9046682c5c483c00be3523a78754b6f530fab3f50c3
-  __AUTH_CONST.__objc_const: 0x7b0 sha256:0adb36a056f619db02508ea25a624c9690fa055ac6247a6a1bc2e292ffcbbf7a
+  __DATA_CONST.__objc_selrefs: 0x100 sha256:cc79abaabe8d5d245bdcdf0c0732fd32ba255369ad115ce10f111f2aaef045f7
+  __DATA_CONST.__objc_superrefs: 0x30 sha256:5ddacfe17d6f008d0252fa1d6a191d607ab7bf692a74d411685fc6e0adebea86
+  __AUTH_CONST.__objc_const: 0x7b0 sha256:5d10f8622bdcfac2313e52c61056de20c9d19201077296bf23a92588a6bab5c2
   __AUTH_CONST.__auth_got: 0x0
-  __AUTH.__objc_data: 0x140 sha256:82bd85714191a4eac3ef3ef2a180ad7eb691da1bd9ce428cfd6291e5f44aa0f2
+  __AUTH.__objc_data: 0x140 sha256:84c7547a2a8a084e11010a13c56f19da18d441c8f0a98c77ae2520260595bd03
   __DATA.__objc_ivar: 0x54 sha256:318c15bd8505efc0b9607909b672c1eec0f9daa42929096ab7fabfc7a16d671d
-  __DATA_DIRTY.__objc_data: 0xa0 sha256:2ecd8fb475fbb9c2e2ed8a5c0e8515c0f58053d21ce4ce23c66404d5c58967b8
+  __DATA_DIRTY.__objc_data: 0xa0 sha256:0c1909b825bd18e79d7f2fe97204bd4fad47527e99560dbe3ef1654b3a5d3a26
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 21D54CAD-3BA3-3B9A-B234-CD2385142C89
+  UUID: 40B1D269-CE2C-3922-9088-A0364611D606
   Functions: 36
   Symbols:   168
   CStrings:  0
Functions:
~ -[AKCAlarmSchedule initWithDays:hour:minute:repeating:] : sha256 a4c044931c44ad5b3b2cb04862ec9d34285babf4c4763bf5b2691b13f2e121ab -> e32056912f52329b79211d0d0909b304f6699cd9ee40c70367b6990ced01d61a
~ -[AKCAlertNotification initWithIdentifier:displayTitle:hasSecondaryAction:secondaryButtonLabel:stopButtonLabel:actionUrlScheme:tintColor:bundleID:localizedAppName:] : sha256 6dfd0230258edd6fb2c120b83849f9a5d13f64993c7f998943c600e73e4e8ed9 -> f612f27bfb21d27c279d1151902c541a25e702c6f9c078202d133ee6615cf5ea
~ -[AKCAlertNotification .cxx_destruct] : sha256 b1f505e37ed04b30a9fb6b65f76bc0d27f1c440bb1ec50ae8557cf5e78994029 -> 16682cc30617a24a7b77ad8296fda33822cc7d423b1e3e28abe742b42a1697bf
~ -[AKCAlarmAlertNotification initWithIdentifier:scheduledFireDate:allowsSnooze:displayTitle:hasSecondaryAction:secondaryButtonLabel:stopButtonLabel:actionUrlScheme:tintColor:bundleID:localizedAppName:] : sha256 2eb4c1b7497fc11f49596cff3c59dd64b8313ba2f389dbd888859998056bc704 -> 49bd1ccef9dbdc76fe9b2d3e4bc70be14a1cd07fa67c6f5388042572d9ad6386
~ -[AKCAlarmAlertNotification .cxx_destruct] : sha256 f00125abaac309c7c745368aa5c67636792f736125a35f73fc3606a5596b5077 -> 60c3a050d9ee71f3044f521f5ed0826f4a83374fd6f06c2a7beab733f22753b2
~ -[AKCTimerAlertNotification initWithIdentifier:displayTitle:hasSecondaryAction:secondaryButtonLabel:stopButtonLabel:actionUrlScheme:tintColor:bundleID:localizedAppName:] : sha256 6a1b9fd122121655646f9bb50d964ef3fde5ad0418fdadde228dbb5d7d8dfaac -> f7ff193b586ddff34b386c962adc6e692407091fa8f1e50f84b7733005321281
~ -[AKCAuthorization initWithBundleID:status:] : sha256 482a1c6abafa8bbb60845e8bb5cb4c39ae6f9808bdb8248ef813e82c032b0991 -> e435030146f1ed531da1eb3b6a11527229d22eb616caf9a076d0a956771f77fc
~ -[AKCAuthorization setBundleID:] : sha256 d24b6ca029722fc0ebf05244463c1fd622e1991d3415908cd1e07736a0d6298b -> fea7fcb6fc3ae80eb8522a8c42c65173949febcbebaabf5cc24a0b8a21c2a0d8
~ -[AKCAuthorization .cxx_destruct] : sha256 969296552722c86ea6ed202b47cb49914cd0ea8d257c13a6402280dc91e5f2a8 -> 4c995415bcb5bb9e5e625854827c4f2a35bb8e1793d736c89ea037b4e39e3e1e
~ -[AKCAlarm initWithIdentifier:data:attributes:] : sha256 5b9017b27eae9e1774824829c18513ebcdd3547946e59e174862ca21cc7a19da -> 0fcbb7e1f166b4d92ce9ab968056636a6e640e780ef76e3c8e9326a90f98fe64
~ -[AKCAlarm setIdentifier:] : sha256 c8646c62fbcb33b046dfc9b125dd9f1e858ae629bc03043650953377526be91a -> 113a13221c0f6e5d44f8d88dec4ee96a4a058125199e9f7f2f06adb2cd8b6f52
~ -[AKCAlarm setData:] : sha256 141cb4f3374d734f3f5dd3f3cb17572db0ad2716166e30f56c7326176dbe1cd2 -> 1ac050b9c22526158d9cb339f78b196bbeffc66b618f7c90bc280e86d0d69e52
~ -[AKCAlarm setAttributes:] : sha256 70eef8dcf87b7f4a09a5a926e536a0c1de26ecb3e0b5bededa57ad1c6d564321 -> 309c25b844f0a9e7cec4f03cb205067507deaae339c3d961cb90e9bed6186c92
~ -[AKCAlarm .cxx_destruct] : sha256 65fac0b70c74fec10a96c70d87cfa8b74bad362ea0d753c4aecb505970e90a0f -> acf568d7288497282355558be1135d8f185173e8c12add906790399616e0a43a

```
