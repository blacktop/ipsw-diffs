## TextInputSourceUAU

> `/System/Library/CoreServices/UAUPlugins/TextInputSourceUAU.bundle/Contents/MacOS/TextInputSourceUAU`

```diff

-138.100.0.0.0
-  __TEXT.__text: 0x2c00 sha256:b0b7e201848bab9adf41bc46a7a8117f972326e473c65fc069001e662722dc13
+139.0.0.0.0
+  __TEXT.__text: 0x2c04 sha256:7433a81c12a4ea63a582ae92c853a45e134ec16a9f2785c0219126a0e21da8f2
   __TEXT.__auth_stubs: 0x320 sha256:a0fd9fa4b291972c00d659b8baee9d0cae03c0acefd00cd208848297c78a9ba4
   __TEXT.__objc_stubs: 0x560 sha256:43e2fd58f3353da5c1e7c310d862fa3890c9e05d248d73ce6a54f310138dcdc9
-  __TEXT.__objc_methlist: 0x1dc sha256:9fd21fd7757b93b2847a5c6bd07942aec4505165de60e9ee9ed1e2238f13cdc8
+  __TEXT.__objc_methlist: 0x1dc sha256:f222c45030f0e77e524ebc0cd81f448216939de13b87f68205b0ec3c510c9ef2
   __TEXT.__const: 0x30 sha256:a0020dda8be85e4aaf1c782a5566edda7426ce8acd7b0b219edb869513d1d864
   __TEXT.__cstring: 0x5ba sha256:62b3fa194bdea279a53d73effd26694c06a05931b8800fb3a68f2bf18bf12ba8
   __TEXT.__oslogstring: 0x719 sha256:cfa3f7b5dcf88b45da9fba7e543978f55b51d3eeefc3869691a7d5bb789853c8
   __TEXT.__objc_classname: 0x37 sha256:5420bb998e008ac37ebc74075282f51960e9c857e4a9f10ba72042c854cc0cd6
   __TEXT.__objc_methname: 0x5b4 sha256:c8548a941b6e38b44b045c8db63f06d7f180ece14c3da71dd1c06ac6466c5747
   __TEXT.__objc_methtype: 0x112 sha256:24c39fd265eaf5ed311fc5a9f40146ce60707f117b41e05e16e34e9e7846f612
-  __TEXT.__unwind_info: 0x98 sha256:7c53491a4a7b8f60af34c80d2f99f672ccb6e611de2f4cd32df7042490cb8dcc
+  __TEXT.__unwind_info: 0x98 sha256:24742254027743f5b1ffb9c0a4c3048a671df3e672ae86ea0e36a64995e6a4de
   __DATA_CONST.__const: 0x10 sha256:24dea3ec66c551b7ef7ede3b4e8bf74afd8bfb47fef80280d3315e5a508c6851
   __DATA_CONST.__cfstring: 0x820 sha256:4ec9cf6ea9b9b4b4c7f26bb0072d7a8d5ccad52d962ad3d5a3c8db388f51cd58
   __DATA_CONST.__objc_classlist: 0x8 sha256:ff2a9bf15582784a6462318817604b6eee5ed58fcbe8166ea3945dee9577ff18

   - /System/Library/PrivateFrameworks/UAUPlugin.framework/Versions/A/UAUPlugin
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 18BA3911-AF63-32B9-BD7D-9E2CF4111EA6
+  UUID: BE22974E-8776-3430-9925-76F4C62958F6
   Functions: 23
   Symbols:   101
   CStrings:  259
Functions:
~ _MigrateAppleEnabledHandwritingLanguages : sha256 4a042037d387bebdadd97111e8f32563bebcc8eec19540f68a5bfa87a9956343 -> c8a35cb4eda6defcb8fb31d9f0c93a756afcec8532cb252f88bc005cc76c49e2
~ _MigrateHandwriting_zh_to_yue_for_HK_MO : sha256 acbf81e7a071a8faa9a38635e2af69afb77e4b3f59cc47a4830d52648241c4cc -> ae62fd2d1163f0e4f79c21f3abec32707b53b05c52cddb92a8118827f5362fb8
~ _RemoveKeyboardViewerFromAppleEnabledInputSources : sha256 44987d054f9fb3a428579e08fb1569ea3d136254bf30692df19730d7036d5c1e -> 3dc3981e38b04a78210877c8d99608e8c25679ada4c9b08aa2ed2329710a6a8b
~ _UpdateInputSourceSwitchingHotKeysOverridedByUserTemplate : 1528 -> 1520
~ _MigrateJapaneseIMToRomajiIMOrKanaIM : sha256 1d75e36f9c47297610b6f37a5a004db2a00428dcd86d95b3146871e5d8c8566a -> 0167040b0b2a24d4e471dc07c0a36307b072df8f0a07e788a5169df7e99deaf8
~ _MigrateThirdPartyInputSourcesToNewDomain : sha256 850c5dc21d23cea47cdf6ecef5fc9b852eaee8eee46a2eea6b4ff1dc9ba5f688 -> e717da231ef0ea54b86aa171128de36eefc5818c7371dd3bbd3c182362438fe0
~ __IsInputSourceEnabledToUser : sha256 bb66c6f6048fe5e67a11120093fe545f4ef69f00e5f302d4b746c5dca8c2aa71 -> 8aca99fdf16d6b1a8d47c7551c355f89cf21072bb6df3b95fee81ae461f1b7d6
~ _MigrateShortcutsForNewCzechAndSlovakLayouts : 1488 -> 1504
~ _MigrateHindiIMToTransliterationIM : sha256 1c0e105904bed36ee511117396bcee69c49e9a3777ab54aef6d475afb1c16aab -> f01aebc2c433df5bbeaabd78225b1f8b88d765893e5c40650292124104d165bb
~ _GetKeyboardID : sha256 807a965b8497fda311261f1cea9d3babc634014f4641fb91774447db73c9359c -> 5a120f3610fa95a6f1d97a5c88443ec60aa1c58081e53c08db00456e2fe9c123
~ _MigrateDictationDoubleTapHotKey : 1836 -> 1832
~ sub_3588 -> sub_358c : sha256 2922ebeb1ec273c811d392ecb07650714e7e2dc3b505f8e0a5db5b1726662725 -> 168030d87cd2684c19abc01f7eeb955b060c7452e83a4f69b2736c527b26b0a6
~ sub_35a4 -> sub_35a8 : sha256 3f545a62833194874ce60712bf36c7a5f4f484f350d98c6412e4d922d5b4c187 -> 5928916dab17c8c332e89493ab2fd9589055a5c7702af61525ad57446cf90767
~ sub_3704 -> sub_3708 : sha256 a65673d58a312696b925ae10cef75294a66be18e289e99a7afcd1f2ca7a18948 -> e72bf1caf1c8c29689cb0faba02eb56c0c611af2945eb102b702a25b724c6779
~ sub_3820 -> sub_3824 : sha256 4a5fce39c1cefe6219f36f369bb1bfc1d408439cab381d05f59bfc7a5a0d6109 -> 4f3f69b1efee0de8ce77763208e2926d35e55b750b234e6d6b0d84254f394f00
~ sub_38fc -> sub_3900 : sha256 232276c7d1931535a65a9da1819eaa2eb89c6aab15a8179b635fd1fd233d96b6 -> 73a24926ebd5301967429aabe470b133d1cd9746bda50f9e14ae0be829ad36fb

```
