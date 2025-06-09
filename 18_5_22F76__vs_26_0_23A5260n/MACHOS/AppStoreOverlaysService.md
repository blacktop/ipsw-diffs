## AppStoreOverlaysService

> `/System/Library/PrivateFrameworks/AppStoreOverlays.framework/PlugIns/AppStoreOverlaysService.appex/AppStoreOverlaysService`

```diff

-7.5.1.0.0
-  __TEXT.__text: 0x15aa0
-  __TEXT.__auth_stubs: 0xe60
+8.0.27.0.0
+  __TEXT.__text: 0x16150
+  __TEXT.__auth_stubs: 0xe80
   __TEXT.__objc_stubs: 0x2680
   __TEXT.__objc_methlist: 0x1164
-  __TEXT.__const: 0x5b4
-  __TEXT.__cstring: 0x11d7
+  __TEXT.__const: 0x5a4
+  __TEXT.__cstring: 0x11e7
   __TEXT.__objc_classname: 0x35b
-  __TEXT.__objc_methname: 0x31f0
+  __TEXT.__objc_methname: 0x3260
   __TEXT.__objc_methtype: 0x95c
   __TEXT.__oslogstring: 0xc9e
   __TEXT.__gcc_except_tab: 0x168
   __TEXT.__dlopen_cstrs: 0x62
   __TEXT.__constg_swiftt: 0x3a4
-  __TEXT.__swift5_typeref: 0x33a
+  __TEXT.__swift5_typeref: 0x34c
   __TEXT.__swift5_reflstr: 0x1ea
   __TEXT.__swift5_fieldmd: 0x228
   __TEXT.__swift5_builtin: 0x28

   __TEXT.__swift5_proto: 0x2c
   __TEXT.__swift5_types: 0x34
   __TEXT.__swift5_capture: 0x10
-  __TEXT.__unwind_info: 0x698
-  __TEXT.__eh_frame: 0x48
-  __DATA_CONST.__auth_got: 0x740
+  __TEXT.__unwind_info: 0x6a8
+  __DATA_CONST.__auth_got: 0x750
   __DATA_CONST.__got: 0x448
-  __DATA_CONST.__auth_ptr: 0x150
-  __DATA_CONST.__const: 0x8d0
+  __DATA_CONST.__auth_ptr: 0x160
+  __DATA_CONST.__const: 0x8a0
   __DATA_CONST.__cfstring: 0x380
   __DATA_CONST.__objc_classlist: 0xe0
   __DATA_CONST.__objc_protolist: 0x90

   __DATA_CONST.__objc_arraydata: 0x8
   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA.__objc_const: 0x2200
-  __DATA.__objc_selrefs: 0xd58
+  __DATA.__objc_selrefs: 0xd68
   __DATA.__objc_ivar: 0xc8
   __DATA.__objc_data: 0xcd0
-  __DATA.__data: 0x9d0
+  __DATA.__data: 0x9f8
   __DATA.__bss: 0x660
-  __DATA.__common: 0xc0
+  __DATA.__common: 0xa0
   - /System/Library/Frameworks/AdAttributionKit.framework/AdAttributionKit
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /System/Library/PrivateFrameworks/UIFoundation.framework/UIFoundation
-  - /System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAVFoundation.dylib

   - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
-  - /usr/lib/swift/libswiftCryptoTokenKit.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
-  - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib

   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  - /usr/lib/swift/libswift_errno.dylib
-  - /usr/lib/swift/libswift_math.dylib
-  - /usr/lib/swift/libswift_signal.dylib
-  - /usr/lib/swift/libswift_stdio.dylib
-  - /usr/lib/swift/libswift_time.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  - /usr/lib/swift/libswiftsys_time.dylib
-  - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 9E8AD2B6-8DCB-3033-B438-B952436F17FD
-  Functions: 544
-  Symbols:   301
-  CStrings:  894
+  UUID: F2CBB7F7-4C0B-38BC-BD72-153186896DE3
+  Functions: 542
+  Symbols:   298
+  CStrings:  896
 
Symbols:
+ _ASOOverlayConfigurationParameterCampaignToken
+ _ASOOverlayConfigurationParameterProviderToken
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3
+ _swift_setDeallocating
- __swift_FORCE_LOAD_$_swiftCryptoTokenKit
- __swift_FORCE_LOAD_$_swiftDataDetection
- __swift_FORCE_LOAD_$_swift_errno
- __swift_FORCE_LOAD_$_swift_math
- __swift_FORCE_LOAD_$_swift_signal
- __swift_FORCE_LOAD_$_swift_stdio
- __swift_FORCE_LOAD_$_swift_time
- __swift_FORCE_LOAD_$_swiftsys_time
- __swift_FORCE_LOAD_$_swiftunistd
CStrings:
+ "@104@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16@48@56@64@72@80@88@96"
+ "initWithFrame:lockup:metricsReporter:localizer:hostBundleIdentifier:hostSceneIdentifier:campaignToken:providerToken:"
+ "initWithFrame:request:metricsReporter:localizer:hostBundleIdentifier:hostSceneIdentifier:campaignToken:providerToken:"
+ "queryParametersForLockup:withBaseQueryParams:"
+ "setCampaignToken:"
+ "setProviderToken:"
- "@88@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16@48@56@64@72@80"
- "initWithFrame:lockup:metricsReporter:localizer:hostBundleIdentifier:hostSceneIdentifier:"
- "initWithFrame:request:metricsReporter:localizer:hostBundleIdentifier:hostSceneIdentifier:"
- "queryParametersForLockup:"

```
