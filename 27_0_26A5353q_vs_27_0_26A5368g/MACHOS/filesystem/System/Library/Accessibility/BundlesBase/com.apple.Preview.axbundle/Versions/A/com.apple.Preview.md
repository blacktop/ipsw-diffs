## com.apple.Preview

> `/System/Library/Accessibility/BundlesBase/com.apple.Preview.axbundle/Versions/A/com.apple.Preview`

```diff

-327.0.0.0.0
-  __TEXT.__text: 0x8b4 sha256:da31a838caa4a7fc8485c392a6bfbf0a7c822156a7cd77d811c73eb42b8fd02a
+329.0.0.0.0
+  __TEXT.__text: 0x8b0 sha256:15d316fdad2838d5f4158c741c34da58e7eeac5b3b2ac2d8b490d9a0a18e0bb2
   __TEXT.__auth_stubs: 0x100 sha256:e3f775a68ce8cee8e28e3387db63208ae0788c381acf0407a6e69c49d01b6ee9
   __TEXT.__objc_stubs: 0x2e0 sha256:99584bdd05e8c027043dd748c636c1b7009c7413bb05573d37320b6cab3844fd
-  __TEXT.__objc_methlist: 0xb0 sha256:9a395d40ff97a8696a960fb489346caa9fbf00e33681af6b77af3342629992fa
+  __TEXT.__objc_methlist: 0xb0 sha256:8c85b4cf80615521cccedb86430c809a570ef59106de3526f549590e41c1e393
   __TEXT.__cstring: 0x1cb sha256:eb10ee8acb46fafcd125c6ec7375c772c84ab044ce5250c15021ae22e5ca17cf
   __TEXT.__objc_classname: 0xc5 sha256:251065df4fe64dbd4761f36d8f2db3e431fd4c856c077bfc7a99871204e524c6
   __TEXT.__objc_methname: 0x312 sha256:03b728e34b1e5261a759187a37bc4bb9093bb3f278fb94ff95e6adaf8340ca22
   __TEXT.__objc_methtype: 0x39 sha256:d80134b9249d66e0f60f1ddf095ce60b305356e3cd906dffd7a9739bf3fcc4a6
-  __TEXT.__unwind_info: 0x90 sha256:6ad45d49e840daf234fbc7793a4f0ad4308e2544be59dc6429bd9e09317e8c27
+  __TEXT.__unwind_info: 0x90 sha256:182d35131c04da8c530c96cd94e46658093e9abc8c74e91cae8d051d146bec94
   __DATA_CONST.__const: 0xa0 sha256:64af800e98a1cf59e1658a7ed72291b3b353cdc5d17f51ec6ae866da87408d7a
   __DATA_CONST.__cfstring: 0x2a0 sha256:b9eb268312a6224ed72f54eabfd1479d20445d7f2c99e5f56aee8c8bcaeb3484
   __DATA_CONST.__objc_classlist: 0x28 sha256:d9ffa2b99c6737fa7489c9dd0146bcc12eabf4ed8b83fc4f22a7bab1aa2b00e9

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 550CF913-66B7-3FA4-A490-BCE5417C2B46
+  UUID: 74C30BE7-3BF9-3CF3-B571-4BA4F0C3BE40
   Functions: 14
   Symbols:   99
   CStrings:  86
Symbols:
+ __block_literal_global.357
+ __block_literal_global.366
- __block_literal_global.351
- __block_literal_global.360
Functions:
~ +[AXPreviewGlue accessibilityPrincipalClassInitializeBundle] : sha256 2c0287c496001b3b5163e0e9f3d7fce784a88eb8f1f26313fa5692875724513a -> 070481715242ae97ea6998fb014ae4ddbe3144570e0b24117b56d12207409e02
~ ___60+[AXPreviewGlue accessibilityPrincipalClassInitializeBundle]_block_invoke_2 : sha256 b53f06eaa6188934d2b17163f57f68e0f1396bbb6a9a4d1847e7a97aa07fdee7 -> 4af77557b36dc6cdf1d63601c1e262f68f1c8a1e5ac8e382e8e6c17573b68070
~ ___60+[AXPreviewGlue accessibilityPrincipalClassInitializeBundle]_block_invoke_3 : sha256 43f0b23eabc34954085f447b9b3da3fb7d2a01455060bba8336e507cc4552d0e -> 37e8c7b6a6a186012ae6036fb539272aeec2ce99d907e6da7113f40fa8f6bcf3
~ _accessibilityLocalizedString : sha256 888ea57a4e5ccce82c1dc2fe6e09ea8efab9d3721a1d4500e04312c7a25e2f23 -> 3e8082d2f921b55c5dba7c9af79fad696510727489a45edc1c8cd339af67fec0
~ +[PVWindowAccessibility(SafeCategory) safeCategoryBaseClass] : sha256 9db56e5e83e23bd0ee9b78ffde17b9fdfd27444d6755415da54ff1bc512023d7 -> 113918a8f8b3d3f7166080d1daac03f65d28c6d1815e76522107d116b17fe861
~ +[PVWindowAccessibility _accessibilityPerformValidations:] : sha256 8852c8aedbf24d7d0fbe2ad2d48544d36c399094d21e3fe395c8839b4a7272bf -> 3def284c64e348a9ee7adc8f9d39592b8f954782db44f06336d5e55f7bc27750
~ -[PVWindowAccessibility accessibilityHitTest:] : sha256 856aeaa42c19ffb89d678e27d0790b5001d9d09326da8f78c14643bb3f22c709 -> c0518631dd4f29939ac8b781c5eb38f611ed300f75329dc1b86671a2be76eb52
~ -[PVWindowAccessibility accessibilityFocusedUIElement] : 756 -> 752
~ +[PVFormFillingCoachingBannerViewControllerAccessibility _accessibilityPerformValidations:] : sha256 d14d2b6fc65af86badc81615bbaf1667528fd1f5d5c246dfb8c26d6608a646a5 -> d8cac35939de6b57f12b1c017130094ea72777780bcecc537eae7183440682b1
~ -[PVFormFillingCoachingBannerViewControllerAccessibility viewDidLoad] : sha256 7a820899984e391004e4aa3c0413ddbfc1ba404e7d038b005efa57658eafdd05 -> 90269573ee4a72099caee26ec4f84dc0a86b2b574993b636f607f17ad5e7c472

```
