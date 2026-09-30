## VoiceTrigger

> `/System/Library/PrivateFrameworks/VoiceTrigger.framework/VoiceTrigger`

```diff

 3520.16.1.0.0
-  __TEXT.__text: 0xdac38
+  __TEXT.__text: 0xdac28
   __TEXT.__auth_stubs: 0x1550
   __TEXT.__objc_methlist: 0x3b54
   __TEXT.__const: 0x1496

   __AUTH.__data: 0x120
   __DATA.__objc_ivar: 0x570
   __DATA.__data: 0xa7a8
-  __DATA.__bss: 0x5e0
+  __DATA.__bss: 0x5d8
   __DATA.__common: 0x40
   __DATA_DIRTY.__objc_data: 0x780
   __DATA_DIRTY.__bss: 0xd8

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 2C903811-8B3D-3C16-BBC4-4C5B28155326
+  UUID: 2ED2E51D-545E-33A3-9EAC-9BCD1F2FD5A3
   Functions: 3039
   Symbols:   8448
   CStrings:  4566
Symbols:
+ ___27-[VTPhraseSpotter analyze:]_block_invoke.560
+ ___27-[VTPhraseSpotter analyze:]_block_invoke.561
+ ___34-[VTPhraseSpotter _analyzeEvents:]_block_invoke.601
+ ___44-[VTAssetManager _runAssetQuery:completion:]_block_invoke.359
+ ___46-[VTAssetManager _downloadAsset:withComplete:]_block_invoke.365
+ ___53-[VTPhraseSpotter _handleAssetChangeForLanguageCode:]_block_invoke.718
+ ___55-[VTPhraseSpotter prepareWithProperty:readyCompletion:]_block_invoke.535
+ ___Block_byref_object_copy_.3543
+ ___Block_byref_object_copy_.6585
+ ___Block_byref_object_dispose_.3544
+ ___Block_byref_object_dispose_.6586
+ ___block_literal_global.11.5786
+ ___block_literal_global.12.6416
+ ___block_literal_global.14.5787
+ ___block_literal_global.17.5788
+ ___block_literal_global.23.6405
+ ___block_literal_global.3367
+ ___block_literal_global.3483
+ ___block_literal_global.351
+ ___block_literal_global.3559
+ ___block_literal_global.364
+ ___block_literal_global.3752
+ ___block_literal_global.3917
+ ___block_literal_global.4400
+ ___block_literal_global.4505
+ ___block_literal_global.4579
+ ___block_literal_global.4635
+ ___block_literal_global.4769
+ ___block_literal_global.511
+ ___block_literal_global.5121
+ ___block_literal_global.5174
+ ___block_literal_global.524
+ ___block_literal_global.5689
+ ___block_literal_global.5770
+ ___block_literal_global.5785
+ ___block_literal_global.594
+ ___block_literal_global.61.3830
+ ___block_literal_global.622
+ ___block_literal_global.6303
+ ___block_literal_global.6422
+ ___block_literal_global.6599
+ ___block_literal_global.6643
+ ___block_literal_global.6761
+ ___block_literal_global.7.5109
+ _sharedInstance._sharedInstance.3368
+ _sharedInstance._sharedInstance.3484
+ _sharedInstance._sharedInstance.3918
+ _sharedInstance._sharedInstance.4636
+ _sharedInstance._sharedInstance.4770
+ _sharedInstance._sharedInstance.5771
+ _sharedInstance._sharedInstance.6304
+ _sharedInstance.onceToken.3366
+ _sharedInstance.onceToken.3482
+ _sharedInstance.onceToken.3916
+ _sharedInstance.onceToken.4578
+ _sharedInstance.onceToken.4634
+ _sharedInstance.onceToken.4768
+ _sharedInstance.onceToken.5173
+ _sharedInstance.onceToken.5769
+ _sharedInstance.onceToken.6302
+ _sharedInstance.onceToken.6760
- ___27-[VTPhraseSpotter analyze:]_block_invoke.521
- ___27-[VTPhraseSpotter analyze:]_block_invoke.522
- ___34-[VTPhraseSpotter _analyzeEvents:]_block_invoke.562
- ___44-[VTAssetManager _runAssetQuery:completion:]_block_invoke.320
- ___46-[VTAssetManager _downloadAsset:withComplete:]_block_invoke.326
- ___53-[VTPhraseSpotter _handleAssetChangeForLanguageCode:]_block_invoke.679
- ___55-[VTPhraseSpotter prepareWithProperty:readyCompletion:]_block_invoke.496
- ___Block_byref_object_copy_.3545
- ___Block_byref_object_copy_.6588
- ___Block_byref_object_dispose_.3546
- ___Block_byref_object_dispose_.6589
- ___block_literal_global.11.5787
- ___block_literal_global.12.6417
- ___block_literal_global.14.5788
- ___block_literal_global.17.5789
- ___block_literal_global.23.6406
- ___block_literal_global.312
- ___block_literal_global.325
- ___block_literal_global.3369
- ___block_literal_global.3485
- ___block_literal_global.3561
- ___block_literal_global.3754
- ___block_literal_global.3919
- ___block_literal_global.4402
- ___block_literal_global.4507
- ___block_literal_global.4580
- ___block_literal_global.4636
- ___block_literal_global.472
- ___block_literal_global.4770
- ___block_literal_global.485
- ___block_literal_global.5122
- ___block_literal_global.5175
- ___block_literal_global.555
- ___block_literal_global.5690
- ___block_literal_global.5771
- ___block_literal_global.5786
- ___block_literal_global.583
- ___block_literal_global.61.3832
- ___block_literal_global.6304
- ___block_literal_global.6423
- ___block_literal_global.6602
- ___block_literal_global.6646
- ___block_literal_global.6764
- ___block_literal_global.7.5110
- _sharedInstance._sharedInstance.3370
- _sharedInstance._sharedInstance.3486
- _sharedInstance._sharedInstance.3920
- _sharedInstance._sharedInstance.4637
- _sharedInstance._sharedInstance.4771
- _sharedInstance._sharedInstance.5772
- _sharedInstance._sharedInstance.6305
- _sharedInstance.onceToken.3368
- _sharedInstance.onceToken.3484
- _sharedInstance.onceToken.3918
- _sharedInstance.onceToken.4579
- _sharedInstance.onceToken.4635
- _sharedInstance.onceToken.4769
- _sharedInstance.onceToken.5174
- _sharedInstance.onceToken.5770
- _sharedInstance.onceToken.6303
- _sharedInstance.onceToken.6763
Functions:
~ sub_22ab74f44 -> sub_22abe6f44 : 1072 -> 1056
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~CJIsugBphfHCrEdtGlG7P3oX_bpmt1Vpz1gPKug/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CJIsugBphfHCrEdtGlG7P3oX_bpmt1Vpz1gPKug/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:410: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CJIsugBphfHCrEdtGlG7P3oX_bpmt1Vpz1gPKug/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string_view:341: libc++ Hardening assertion (__end - __begin) >= 0 failed: std::string_view::string_view(iterator, sentinel) received invalid range\n"
+ "Apple clang version 21.0.0 (clang-2100.0.122.2) [+internal-os]"
+ "Mon Feb 16 00:45:11 2026"
+ "Mon Feb 16 00:45:11 PST 2026"
+ "Novalib gitrelno_unavailable Release Mon Feb 16 00:45:11 2026"
- "/AppleInternal/Library/BuildRoots/4~CHwHugA0Sz63hnNyUivNiahdOSZJw8hYhUtwz5k/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CHwHugA0Sz63hnNyUivNiahdOSZJw8hYhUtwz5k/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:410: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CHwHugA0Sz63hnNyUivNiahdOSZJw8hYhUtwz5k/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string_view:341: libc++ Hardening assertion (__end - __begin) >= 0 failed: std::string_view::string_view(iterator, sentinel) received invalid range\n"
- "Apple clang version 21.0.0 (clang-2100.0.119.1) [+internal-os]"
- "Novalib gitrelno_unavailable Release Wed Jan 28 03:12:57 2026"
- "Wed Jan 28 03:12:57 2026"
- "Wed Jan 28 03:12:57 PST 2026"

```
