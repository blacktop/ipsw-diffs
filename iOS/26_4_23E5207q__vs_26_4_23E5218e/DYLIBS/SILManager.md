## SILManager

> `/System/Library/PrivateFrameworks/SILManager.framework/SILManager`

```diff

 53.19.0.0.0
-  __TEXT.__text: 0x575ac
-  __TEXT.__auth_stubs: 0x17f0
+  __TEXT.__text: 0x574e4
+  __TEXT.__auth_stubs: 0x17e0
   __TEXT.__objc_methlist: 0x6f0
   __TEXT.__const: 0x481c
   __TEXT.__oslogstring: 0x1a54

   __DATA_CONST.__objc_classlist: 0xc0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x440
-  __AUTH_CONST.__auth_got: 0xc08
+  __AUTH_CONST.__auth_got: 0xc00
   __AUTH_CONST.__const: 0x1f20
   __AUTH_CONST.__cfstring: 0xa0
   __AUTH_CONST.__objc_const: 0x2008

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: AC47F2F8-23F4-3007-BA9F-8423EB2213EA
+  UUID: 107291D9-3ABD-35BE-95F6-62F10F296118
   Functions: 1595
-  Symbols:   5579
+  Symbols:   5578
   CStrings:  767
 
Symbols:
- _objc_retain_x11
Functions:
~ _$s10SILManager12SILValidatorC22checkFallbackIndicator6states8rendererAC16FBITriggeredTypeOAC0E6StatesV_AA11SILRendererCtF : 4212 -> 4192
~ _$s10SILManager24SILDebugAnimationTrackerC15printAnimations14animationDequey19CollectionsInternal0H0VyAC14AnimPropertiesVG_tF : 2152 -> 2120
~ _$s10SILManager16SILFlipBookStateC_4name11transitionsACSayAA9FrameDescCG_SSSDySSSDySSSaySiGGGtKcfc : 3436 -> 3384
~ _$s10SILManager15SILFlipBookDescCyACSayAA05FrameD0CG_SDySSSDySSSDySSSaySiGGGGtKcfc : 844 -> 824
~ _$s10SILManager11SILManifestC8manifestACSgvpZfiAEyXEfU_ : 604 -> 596
~ _$s10SILManager11SILManifestC027constraintFileFromIndicatorD010deviceType09indicatorD4Name0C5FilesAA14SILConstraintsCSS_SSSayAA13SILFileHandle_pGtKFZTf4nnnd_n : 2664 -> 2748
~ _$s10SILManager11SILManifestC8findBlob33_1A38F4C2AD7451B3FA5C586DAE7EC27DLL4from10blobSuffixySayAA12SILAssetDescCG_SStFTf4nnd_n : 1320 -> 1376
~ _$s10SILManager11SILManifestC18manifestFromPlists6plists12enableCursorACSgSayAA13SILFileHandle_pG_SbtFZTf4nnd_n : 5596 -> 5632
~ _$s10SILManager11SILRendererC9swapBegins6UInt64VyKF : 3360 -> 3340
~ _$s10SILManager11SILRendererC4swap9region_id13indicator_idx8position9zRotation12frame_number7opacity10glyphScales6UInt64VSi_SiSo7CGPointVAA0I0Os6UInt16VS2ftKF : 17180 -> 17164
~ _$s10SILManager11SILRendererC7swapEnd16presentationTime9syncToTsqys6UInt64V_SbtKF : 2420 -> 2356
~ _$s10SILManager11SILRendererC11dumpSwapEnd33_218A6A42BD54406E011163ED9EC808F6LLyys6UInt64V_SbtFTf4ddn_n : 7248 -> 7104
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~CJImugC-AVS6upfdOQEzxB4gHXEx4SP8vLuBZPE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__format/formatter_output.h:237: libc++ Hardening assertion __first <= __last failed: Not a valid range\n"
+ "/AppleInternal/Library/BuildRoots/4~CJImugC-AVS6upfdOQEzxB4gHXEx4SP8vLuBZPE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__format/formatter_output.h:250: libc++ Hardening assertion __first <= __last failed: Not a valid range\n"
+ "/AppleInternal/Library/BuildRoots/4~CJImugC-AVS6upfdOQEzxB4gHXEx4SP8vLuBZPE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__format/formatter_output.h:264: libc++ Hardening assertion __first <= __last failed: Not a valid range\n"
+ "/AppleInternal/Library/BuildRoots/4~CJImugC-AVS6upfdOQEzxB4gHXEx4SP8vLuBZPE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__format/parser_std_format_spec.h:594: libc++ Hardening assertion __begin != __end failed: when called with an empty input the function will cause undefined behavior by evaluating data not in the input\n"
+ "/AppleInternal/Library/BuildRoots/4~CJImugC-AVS6upfdOQEzxB4gHXEx4SP8vLuBZPE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/optional:811: libc++ Hardening assertion this->has_value() failed: optional operator* called on a disengaged value\n"
+ "/AppleInternal/Library/BuildRoots/4~CJImugC-AVS6upfdOQEzxB4gHXEx4SP8vLuBZPE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string_view:329: libc++ Hardening assertion __len <= static_cast<size_type>(numeric_limits<difference_type>::max()) failed: string_view::string_view(_CharT *, size_t): length does not fit in difference_type\n"
+ "/AppleInternal/Library/BuildRoots/4~CJImugC-AVS6upfdOQEzxB4gHXEx4SP8vLuBZPE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string_view:341: libc++ Hardening assertion (__end - __begin) >= 0 failed: std::string_view::string_view(iterator, sentinel) received invalid range\n"
+ "/Library/Caches/com.apple.xbs/677207E6-4462-42E0-A456-BBD7B5DBE71A/TemporaryDirectory.9NJ0j7/Binaries/SILManager/install/TempContent/Objects/SILManager.build/SILManager.build/DerivedSources/SILManager_C.c"
- "/AppleInternal/Library/BuildRoots/4~CH80ugDuRUKx_1j7xNzoqFEOTNcg8BQwSM1-5_s/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__format/formatter_output.h:237: libc++ Hardening assertion __first <= __last failed: Not a valid range\n"
- "/AppleInternal/Library/BuildRoots/4~CH80ugDuRUKx_1j7xNzoqFEOTNcg8BQwSM1-5_s/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__format/formatter_output.h:250: libc++ Hardening assertion __first <= __last failed: Not a valid range\n"
- "/AppleInternal/Library/BuildRoots/4~CH80ugDuRUKx_1j7xNzoqFEOTNcg8BQwSM1-5_s/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__format/formatter_output.h:264: libc++ Hardening assertion __first <= __last failed: Not a valid range\n"
- "/AppleInternal/Library/BuildRoots/4~CH80ugDuRUKx_1j7xNzoqFEOTNcg8BQwSM1-5_s/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__format/parser_std_format_spec.h:594: libc++ Hardening assertion __begin != __end failed: when called with an empty input the function will cause undefined behavior by evaluating data not in the input\n"
- "/AppleInternal/Library/BuildRoots/4~CH80ugDuRUKx_1j7xNzoqFEOTNcg8BQwSM1-5_s/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/optional:811: libc++ Hardening assertion this->has_value() failed: optional operator* called on a disengaged value\n"
- "/AppleInternal/Library/BuildRoots/4~CH80ugDuRUKx_1j7xNzoqFEOTNcg8BQwSM1-5_s/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string_view:329: libc++ Hardening assertion __len <= static_cast<size_type>(numeric_limits<difference_type>::max()) failed: string_view::string_view(_CharT *, size_t): length does not fit in difference_type\n"
- "/AppleInternal/Library/BuildRoots/4~CH80ugDuRUKx_1j7xNzoqFEOTNcg8BQwSM1-5_s/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string_view:341: libc++ Hardening assertion (__end - __begin) >= 0 failed: std::string_view::string_view(iterator, sentinel) received invalid range\n"
- "/Library/Caches/com.apple.xbs/6282C671-789D-4467-A777-514CF7205168/TemporaryDirectory.NoEtM5/Binaries/SILManager/install/TempContent/Objects/SILManager.build/SILManager.build/DerivedSources/SILManager_C.c"

```
