## MachineSettings

> `/System/Library/PrivateFrameworks/MachineSettings.framework/Versions/A/MachineSettings`

```diff

 14.0.0.0.0
-  __TEXT.__text: 0xb1c sha256:bcbd105cf29661254d68d710d91cbc977393e8909317bfeb107288a8fb402499
-  __TEXT.__objc_methlist: 0x50 sha256:bf4f685f00468b32f68e9516c0bf6d7cc23bf0f63d078220e12481aa77321d5a
-  __TEXT.__cstring: 0xa23 sha256:9260efe5b8179a1d15679c6cd29c6cb718fba0e32d8dd12e1209aabee98a43cd
+  __TEXT.__text: 0xb1c sha256:d6b9cd89dcf85741ee0d7fb4ed2b88a8833cd548d839f0a007a4217ea19308fa
+  __TEXT.__objc_methlist: 0x50 sha256:3dab7db4e1e25c3775446c2b8cbc173a14b0ba3acd0b49ff5baa801796a83663
+  __TEXT.__cstring: 0xa23 sha256:5260dfde30bc020b6ee8319c6a3309558081ddd112fa79026a513cd4ca3b3c93
   __TEXT.__unwind_info: 0x88 sha256:d21c1489982d48270bcb312c5900c6d60740fc8f0d60c0da18d5f961c3eeeb8f
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__objc_classlist: 0x8 sha256:7b5f46775b25ff79fbfdfc61f326075e47091743bdfef3bed85aaf3af61e4ce0
+  __DATA_CONST.__objc_classlist: 0x8 sha256:323c07e8d401545511f17e602d38e476774b214af04d1501b97a7d4d8dc94b0b
   __DATA_CONST.__objc_imageinfo: 0x8 sha256:59fc9e64071aa89b9247d029e0b37ebe0fe9fc5434efb8e67b0b36435fb494cf
-  __DATA_CONST.__objc_selrefs: 0x30 sha256:426e0529829d61062e1983f41e21f257e1133ad3f70c3aed0abdf484b99acd2f
+  __DATA_CONST.__objc_selrefs: 0x30 sha256:20feef88d9ca625ac5890d4bb7e8c170bb3f6873d94f5a7de6b09995e4b0da31
   __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__cfstring: 0x820 sha256:666cdd00615937f2983517e07a7fdbf1f67f6c048bf4e9f6b61a5f57cb482b94
-  __AUTH_CONST.__objc_const: 0x90 sha256:2387b3b3db9f4145d63c785311c0331f10c51e27913b473ecc4bf0532a00e1b9
+  __AUTH_CONST.__cfstring: 0x820 sha256:f79ed4b405fc26757c90218811da37e0547fd07389812648cd4119e4df275012
+  __AUTH_CONST.__objc_const: 0x90 sha256:dbb7f4e21a8943df418b416cd6cec501cc33a69b3c1b43dd901b3afaa497f235
   __AUTH_CONST.__auth_got: 0x0
-  __AUTH.__objc_data: 0x50 sha256:7614386dc04852a2193cc8aecc3b3e2c43a89e5adbe8d6e3d772c27358cafe7c
-  __DATA.__data: 0xe0 sha256:17580e8bb9cc5184bad265e9ac9169aeb83d4bbfca1ed008cb614ddf95b55990
+  __AUTH.__objc_data: 0x50 sha256:e0a8fdb0ece333ea06d0907c865fcadacd0ae621647ec02bda7f7fcdb8ffdb2b
+  __DATA.__data: 0xe0 sha256:cc5c478b42f874c42c926366e2ed2d2718e9b19dad6bd9f41f93e5aed90a3233
   __DATA.__bss: 0x4 sha256:df3f619804a92fdb4057192dc43dd748ea778adc52bc498ce80524c014b81119
   - /System/Library/Frameworks/CoreAudio.framework/Versions/A/CoreAudio
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: E405F017-3118-396E-A0D6-FFDB96609A62
+  UUID: A3B20F8A-D648-3C7D-BD15-B9D25F6C0178
   Functions: 21
   Symbols:   91
   CStrings:  137
Functions:
~ _getEVSHandle : sha256 f185c3150909d65dbd8e125d89659e25f07b898f099d3760ab102c601b99001f -> 69b82d4160154241504c8f161f6c1f871e1c738faab56ae8d61c6c6f32cb5796
~ _doubleClickThresholdLevel : sha256 5a25831486fdc5e727f2a193744983931c0a912166b9ea90d8db8cbb0c2476ff -> ee1823e213383919242ecf0132bf8e4c49782e8f1e3b4357f10aa6311b4abf86
~ _openIOConnection : sha256 067e22cb3d34a4a29e144543df3a8ae95481dfdcea6aecc21a1782a3e0f55bd4 -> b34b730a9b66f7ce051eaf9a3301b3c66abf6a23239329794c1db9e2464defb8
~ _setDoubleClickThresholdLevel : sha256 f82570026f3298fd6500ad465a4f75ac19e403d560c789b56623074cfebcd534 -> 5b5918dd4f6ea7e19ccd673e7d412b8321b57643036bb9f813cd685c5909a2af
~ _setMultitouchTrackpadBehavior : sha256 87c855bd5898f3889c641c3a252f8543669a4c900e240d5f2cbe80ab25589f72 -> e1073117cf7772eb0592e95a0c173a02d0199f28cfc5594715959041eef8679f
~ _createDictionaryForTrackpadPreferences : sha256 57087aa3d2d1b207a6fa5a85b4a4b52ad1ea7e3c3799cc5968730a776184b47f -> 2bb0a8acdaf67883769027efd26b6aad225d0d526fca1dbc7c48014600787e2f
~ _setTrackpadTapBehavior : sha256 bf84c9e2088dadeb0d876542d785a12f993f963279eda65eea2e6bda58ced9c7 -> 8c8ba3c4450ddf88f97c7e6050f73f5eb24a03c9645745cf6c11ef33fbaa7408
~ _setIgnoreTrackWhileTypingBehavior : sha256 ad142a3f0f7f9bd09e2cd525d2b3deaba5a1b52d899a73ad39f6bf2cc2ee9a2c -> 748568093475685f63d352b99e2e0f282ec86050a18c7f4933d757fcfb71622a
~ _setIgnoreTrackpadIfMousePresent : sha256 89e44cdb73771bab480e43d805c1076d7f37a8e6eb826d97ff952d9592637b75 -> e3a53412c828054933f8c812c379a9f03baa670b99a63a214733050fd2a0a580
~ _NSSetMouseButtonClickBehavior : sha256 31ec6184c9be257cb69dd16190778fd81341156d1faa52871726f58f78ec9901 -> dd52fa11e4e5a064a235e7f318d477c1e21047fe11c290cfa8b940aebaf371e6
~ _NSMouseButtonClickBehavior : sha256 11ef40bf7c3382294c60f0a811fe7fe0457a464a9b5e065753623d96805bd949 -> 41f9380793ffb87f5f355e010e89155e9d06bd0003b4019d65a86c50fd32a23c
~ _setXServeLockEnclosureState : sha256 dc1d8e6432e506672187a1c458a9e9506f5d1a97cd7eae186be170f5e93bf644 -> 4cfd874fb5bd763258b669b6c1eee3e0436273bba17f5bb07843bcc5d2e3c62f
~ _setXServeLockEnclosureStateForConnection : sha256 998babca82f96f7c52f4514432f25fbd0b83c6e250e3920a8fae8d3448c17bbd -> c3b29656d43a223033c69cbd80b6e27e4dbcc2321210a37529c429b110d2e920
~ _createKeyForKeyboard : sha256 4049eaf3770a44845a596bd8a160afab0973e93ff546bdcdf5c271243600b1dc -> d09ccddc4245b095ca398fe217ee954814638c066c443ec99619985bd004fad6
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~CRbaugABU6CbkKYnZg7yUW9aeD8jLSrV02M9ijQ/Library/Caches/com.apple.xbs/TemporaryDirectory.iKmpyy/Sources/MachineSettingsFramework/MachineSettings/InputDeviceUtilities.m"
- "/AppleInternal/Library/BuildRoots/4~CQCDugCoaFjTiLVlgtvFvDW_V3XqG3B6utBb2x0/Library/Caches/com.apple.xbs/TemporaryDirectory.HADiPM/Sources/MachineSettingsFramework/MachineSettings/InputDeviceUtilities.m"

```
