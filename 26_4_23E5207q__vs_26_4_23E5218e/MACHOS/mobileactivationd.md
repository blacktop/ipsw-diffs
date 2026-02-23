## mobileactivationd

> `/usr/libexec/mobileactivationd`

```diff

-1076.100.26.0.0
-  __TEXT.__text: 0x35d608
-  __TEXT.__auth_stubs: 0x1160
-  __TEXT.__objc_stubs: 0x30e0
-  __TEXT.__objc_methlist: 0x10b4
-  __TEXT.__const: 0x5c348
-  __TEXT.__cstring: 0xe8a4
-  __TEXT.__objc_methname: 0x3eea
+1076.100.28.0.0
+  __TEXT.__text: 0x321b48
+  __TEXT.__auth_stubs: 0x1190
+  __TEXT.__objc_stubs: 0x31c0
+  __TEXT.__objc_methlist: 0x1104
+  __TEXT.__const: 0x5c398
+  __TEXT.__cstring: 0xe987
+  __TEXT.__objc_methname: 0x3fab
   __TEXT.__oslogstring: 0xf38
   __TEXT.__objc_classname: 0x1b4
-  __TEXT.__objc_methtype: 0x102a
+  __TEXT.__objc_methtype: 0x1048
   __TEXT.__gcc_except_tab: 0x1c3c
   __TEXT.__dlopen_cstrs: 0x294
   __TEXT.__ustring: 0x4
-  __TEXT.__unwind_info: 0x1190
+  __TEXT.__unwind_info: 0x11b0
   __TEXT.__eh_frame: 0xa0
-  __DATA_CONST.__auth_got: 0x8c0
-  __DATA_CONST.__got: 0x488
+  __DATA_CONST.__auth_got: 0x8d8
+  __DATA_CONST.__got: 0x498
   __DATA_CONST.__auth_ptr: 0x78
-  __DATA_CONST.__const: 0x1e9c8
-  __DATA_CONST.__cfstring: 0xcea0
+  __DATA_CONST.__const: 0x1b7e8
+  __DATA_CONST.__cfstring: 0xcfe0
   __DATA_CONST.__objc_classlist: 0x50
-  __DATA_CONST.__objc_catlist: 0x18
+  __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x40
   __DATA_CONST.__objc_intobj: 0x270
-  __DATA_CONST.__objc_arraydata: 0x4f0
+  __DATA_CONST.__objc_arraydata: 0x4f8
   __DATA_CONST.__objc_arrayobj: 0x90
-  __DATA.__objc_const: 0x1888
-  __DATA.__objc_selrefs: 0x1058
-  __DATA.__objc_ivar: 0xf8
+  __DATA.__objc_const: 0x18f8
+  __DATA.__objc_selrefs: 0x1098
+  __DATA.__objc_ivar: 0xfc
   __DATA.__objc_data: 0x320
-  __DATA.__data: 0x1b38
+  __DATA.__data: 0x1b50
   __DATA.__bss: 0x54c
-  __DATA.__common: 0xb30
+  __DATA.__common: 0xb28
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreTelephony.framework/CoreTelephony

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/liblockdown.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 205AD0C4-C45C-357C-AA48-09FA3E641005
-  Functions: 1598
-  Symbols:   10803
-  CStrings:  4639
+  UUID: B669B8C3-0A0D-323E-9322-6F5F379D0F65
+  Functions: 1612
+  Symbols:   10924
+  CStrings:  4672
 
Symbols:
+ +[NSString(MobileActivation) stringWithUTF8StringData:]
+ -[DeviceType is_factory_restored]
+ -[NSData(MobileActivation) lastByteEqualTo:]
+ -[NSData(MobileActivation) lastByte]
+ -[NSString(MobileActivation) dataFromHexString:]
+ /AppleInternal/Library/BuildRoots/4~CJIfugBJ64sWmafN_hS9uC68vNYwwvqi98IqO6c/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/local/lib/amd/libDER.a(DER_Decode.o)
+ /AppleInternal/Library/BuildRoots/4~CJIfugBJ64sWmafN_hS9uC68vNYwwvqi98IqO6c/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/local/lib/libCoreTrust.a(AppleAnchors.o)
+ /AppleInternal/Library/BuildRoots/4~CJIfugBJ64sWmafN_hS9uC68vNYwwvqi98IqO6c/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/local/lib/libCoreTrust.a(CMS.o)
+ /AppleInternal/Library/BuildRoots/4~CJIfugBJ64sWmafN_hS9uC68vNYwwvqi98IqO6c/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/local/lib/libCoreTrust.a(CTEvaluate.o)
+ /AppleInternal/Library/BuildRoots/4~CJIfugBJ64sWmafN_hS9uC68vNYwwvqi98IqO6c/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/local/lib/libCoreTrust.a(CTEvaluateBAA.o)
+ /AppleInternal/Library/BuildRoots/4~CJIfugBJ64sWmafN_hS9uC68vNYwwvqi98IqO6c/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/local/lib/libCoreTrust.a(CryptoUtils.o)
+ /AppleInternal/Library/BuildRoots/4~CJIfugBJ64sWmafN_hS9uC68vNYwwvqi98IqO6c/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/local/lib/libCoreTrust.a(DERUtils.o)
+ /AppleInternal/Library/BuildRoots/4~CJIfugBJ64sWmafN_hS9uC68vNYwwvqi98IqO6c/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/local/lib/libCoreTrust.a(X509Certificate.o)
+ /AppleInternal/Library/BuildRoots/4~CJIfugBJ64sWmafN_hS9uC68vNYwwvqi98IqO6c/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/local/lib/libCoreTrust.a(X509Chain.o)
+ /AppleInternal/Library/BuildRoots/4~CJIfugBJ64sWmafN_hS9uC68vNYwwvqi98IqO6c/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/local/lib/libCoreTrust.a(X509Policy.o)
+ /AppleInternal/Library/BuildRoots/4~CJIfugBJ64sWmafN_hS9uC68vNYwwvqi98IqO6c/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/local/lib/libCoreTrust.a(iCDPAnchors.o)
+ /AppleInternal/Library/BuildRoots/4~CJIfugBJ64sWmafN_hS9uC68vNYwwvqi98IqO6c/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/local/lib/libaks.a(acl_keys.o)
+ /AppleInternal/Library/BuildRoots/4~CJIfugBJ64sWmafN_hS9uC68vNYwwvqi98IqO6c/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/local/lib/libaks.a(aks_pack.o)
+ /AppleInternal/Library/BuildRoots/4~CJIfugBJ64sWmafN_hS9uC68vNYwwvqi98IqO6c/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/local/lib/libaks.a(der_utils.o)
+ /AppleInternal/Library/BuildRoots/4~CJIfugBJ64sWmafN_hS9uC68vNYwwvqi98IqO6c/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/local/lib/libaks.a(firebloom_hacks.o)
+ /AppleInternal/Library/BuildRoots/4~CJIfugBJ64sWmafN_hS9uC68vNYwwvqi98IqO6c/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/local/lib/libaks.a(libaks_client.o)
+ /AppleInternal/Library/BuildRoots/4~CJIfugBJ64sWmafN_hS9uC68vNYwwvqi98IqO6c/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/local/lib/libaks.a(libaks_internal.o)
+ /AppleInternal/Library/BuildRoots/4~CJIfugBJ64sWmafN_hS9uC68vNYwwvqi98IqO6c/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/local/lib/libaks.a(libaks_ref_key.o)
+ /Library/Caches/com.apple.xbs/3E1C2549-D599-419B-94EF-96E573A9FDDB/TemporaryDirectory.y0UDhv/Sources/CoreTrust/Source/
+ /Library/Caches/com.apple.xbs/53DD53B8-F12F-4B74-9B41-3805AB4ED204/TemporaryDirectory.LZ2YvF/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/BAAASMFiOSRootCAPEM.o
+ /Library/Caches/com.apple.xbs/53DD53B8-F12F-4B74-9B41-3805AB4ED204/TemporaryDirectory.LZ2YvF/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/BAAMFiRootCAPEM.o
+ /Library/Caches/com.apple.xbs/53DD53B8-F12F-4B74-9B41-3805AB4ED204/TemporaryDirectory.LZ2YvF/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/BAASCRTRootCAPEM.o
+ /Library/Caches/com.apple.xbs/53DD53B8-F12F-4B74-9B41-3805AB4ED204/TemporaryDirectory.LZ2YvF/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/BAAUCRTRootCAPEM.o
+ /Library/Caches/com.apple.xbs/53DD53B8-F12F-4B74-9B41-3805AB4ED204/TemporaryDirectory.LZ2YvF/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/BAAVMRootCAPEM.o
+ /Library/Caches/com.apple.xbs/53DD53B8-F12F-4B74-9B41-3805AB4ED204/TemporaryDirectory.LZ2YvF/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/FactoryUCRTRootCAPEM.o
+ /Library/Caches/com.apple.xbs/53DD53B8-F12F-4B74-9B41-3805AB4ED204/TemporaryDirectory.LZ2YvF/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/GestaltHlpr.o
+ /Library/Caches/com.apple.xbs/53DD53B8-F12F-4B74-9B41-3805AB4ED204/TemporaryDirectory.LZ2YvF/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/MACollectionInterface.o
+ /Library/Caches/com.apple.xbs/53DD53B8-F12F-4B74-9B41-3805AB4ED204/TemporaryDirectory.LZ2YvF/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/MATelephonyInfo.o
+ /Library/Caches/com.apple.xbs/53DD53B8-F12F-4B74-9B41-3805AB4ED204/TemporaryDirectory.LZ2YvF/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/MobileActivationError.o
+ /Library/Caches/com.apple.xbs/53DD53B8-F12F-4B74-9B41-3805AB4ED204/TemporaryDirectory.LZ2YvF/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/MobileActivationErrorPrivate.o
+ /Library/Caches/com.apple.xbs/53DD53B8-F12F-4B74-9B41-3805AB4ED204/TemporaryDirectory.LZ2YvF/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/MobileRecertifyEngine.o
+ /Library/Caches/com.apple.xbs/53DD53B8-F12F-4B74-9B41-3805AB4ED204/TemporaryDirectory.LZ2YvF/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/NSData+MobileActivation.o
+ /Library/Caches/com.apple.xbs/53DD53B8-F12F-4B74-9B41-3805AB4ED204/TemporaryDirectory.LZ2YvF/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/NSDateFormatter+MobileActivation.o
+ /Library/Caches/com.apple.xbs/53DD53B8-F12F-4B74-9B41-3805AB4ED204/TemporaryDirectory.LZ2YvF/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/NSDictionary+MobileActivation.o
+ /Library/Caches/com.apple.xbs/53DD53B8-F12F-4B74-9B41-3805AB4ED204/TemporaryDirectory.LZ2YvF/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/NSString+MobileActivation.o
+ /Library/Caches/com.apple.xbs/53DD53B8-F12F-4B74-9B41-3805AB4ED204/TemporaryDirectory.LZ2YvF/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/NetworkProvider.o
+ /Library/Caches/com.apple.xbs/53DD53B8-F12F-4B74-9B41-3805AB4ED204/TemporaryDirectory.LZ2YvF/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/QABAAASMFiOSRootCAPEM.o
+ /Library/Caches/com.apple.xbs/53DD53B8-F12F-4B74-9B41-3805AB4ED204/TemporaryDirectory.LZ2YvF/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/QABAAMFiRootCAPEM.o
+ /Library/Caches/com.apple.xbs/53DD53B8-F12F-4B74-9B41-3805AB4ED204/TemporaryDirectory.LZ2YvF/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/QABAASCRTRootCAPEM.o
+ /Library/Caches/com.apple.xbs/53DD53B8-F12F-4B74-9B41-3805AB4ED204/TemporaryDirectory.LZ2YvF/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/QABAAUCRTRootCAPEM.o
+ /Library/Caches/com.apple.xbs/53DD53B8-F12F-4B74-9B41-3805AB4ED204/TemporaryDirectory.LZ2YvF/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/QABAAVMRootCAPEM.o
+ /Library/Caches/com.apple.xbs/53DD53B8-F12F-4B74-9B41-3805AB4ED204/TemporaryDirectory.LZ2YvF/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/QAIphoneActivationPEM.o
+ /Library/Caches/com.apple.xbs/53DD53B8-F12F-4B74-9B41-3805AB4ED204/TemporaryDirectory.LZ2YvF/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/QAIphoneDeviceCAPEM.o
+ /Library/Caches/com.apple.xbs/53DD53B8-F12F-4B74-9B41-3805AB4ED204/TemporaryDirectory.LZ2YvF/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/QAUCRTRootCAP384PEM.o
+ /Library/Caches/com.apple.xbs/53DD53B8-F12F-4B74-9B41-3805AB4ED204/TemporaryDirectory.LZ2YvF/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/QAUCRTRootCAPEM.o
+ /Library/Caches/com.apple.xbs/53DD53B8-F12F-4B74-9B41-3805AB4ED204/TemporaryDirectory.LZ2YvF/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/QAUCRTSubCAPEM.o
+ /Library/Caches/com.apple.xbs/53DD53B8-F12F-4B74-9B41-3805AB4ED204/TemporaryDirectory.LZ2YvF/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/RaptorActivationPEM.o
+ /Library/Caches/com.apple.xbs/53DD53B8-F12F-4B74-9B41-3805AB4ED204/TemporaryDirectory.LZ2YvF/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/RaptorDeviceCAPEM.o
+ /Library/Caches/com.apple.xbs/53DD53B8-F12F-4B74-9B41-3805AB4ED204/TemporaryDirectory.LZ2YvF/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/UCRTRootCAPEM.o
+ /Library/Caches/com.apple.xbs/53DD53B8-F12F-4B74-9B41-3805AB4ED204/TemporaryDirectory.LZ2YvF/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/UCRTSubCAPEM.o
+ /Library/Caches/com.apple.xbs/53DD53B8-F12F-4B74-9B41-3805AB4ED204/TemporaryDirectory.LZ2YvF/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/activation_support.o
+ /Library/Caches/com.apple.xbs/53DD53B8-F12F-4B74-9B41-3805AB4ED204/TemporaryDirectory.LZ2YvF/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/activation_support_shared.o
+ /Library/Caches/com.apple.xbs/53DD53B8-F12F-4B74-9B41-3805AB4ED204/TemporaryDirectory.LZ2YvF/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/authkit.o
+ /Library/Caches/com.apple.xbs/53DD53B8-F12F-4B74-9B41-3805AB4ED204/TemporaryDirectory.LZ2YvF/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/baa.o
+ /Library/Caches/com.apple.xbs/53DD53B8-F12F-4B74-9B41-3805AB4ED204/TemporaryDirectory.LZ2YvF/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/baa_oids.o
+ /Library/Caches/com.apple.xbs/53DD53B8-F12F-4B74-9B41-3805AB4ED204/TemporaryDirectory.LZ2YvF/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/battery_management.o
+ /Library/Caches/com.apple.xbs/53DD53B8-F12F-4B74-9B41-3805AB4ED204/TemporaryDirectory.LZ2YvF/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/bridge.o
+ /Library/Caches/com.apple.xbs/53DD53B8-F12F-4B74-9B41-3805AB4ED204/TemporaryDirectory.LZ2YvF/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/bridge_support.o
+ /Library/Caches/com.apple.xbs/53DD53B8-F12F-4B74-9B41-3805AB4ED204/TemporaryDirectory.LZ2YvF/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/common.o
+ /Library/Caches/com.apple.xbs/53DD53B8-F12F-4B74-9B41-3805AB4ED204/TemporaryDirectory.LZ2YvF/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/coretrust.o
+ /Library/Caches/com.apple.xbs/53DD53B8-F12F-4B74-9B41-3805AB4ED204/TemporaryDirectory.LZ2YvF/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/crypto.o
+ /Library/Caches/com.apple.xbs/53DD53B8-F12F-4B74-9B41-3805AB4ED204/TemporaryDirectory.LZ2YvF/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/data_ark.o
+ /Library/Caches/com.apple.xbs/53DD53B8-F12F-4B74-9B41-3805AB4ED204/TemporaryDirectory.LZ2YvF/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/data_migration_support.o
+ /Library/Caches/com.apple.xbs/53DD53B8-F12F-4B74-9B41-3805AB4ED204/TemporaryDirectory.LZ2YvF/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/device_tree.o
+ /Library/Caches/com.apple.xbs/53DD53B8-F12F-4B74-9B41-3805AB4ED204/TemporaryDirectory.LZ2YvF/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/dsp.o
+ /Library/Caches/com.apple.xbs/53DD53B8-F12F-4B74-9B41-3805AB4ED204/TemporaryDirectory.LZ2YvF/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/env.o
+ /Library/Caches/com.apple.xbs/53DD53B8-F12F-4B74-9B41-3805AB4ED204/TemporaryDirectory.LZ2YvF/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/env_darwin.o
+ /Library/Caches/com.apple.xbs/53DD53B8-F12F-4B74-9B41-3805AB4ED204/TemporaryDirectory.LZ2YvF/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/findmy.o
+ /Library/Caches/com.apple.xbs/53DD53B8-F12F-4B74-9B41-3805AB4ED204/TemporaryDirectory.LZ2YvF/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/host.o
+ /Library/Caches/com.apple.xbs/53DD53B8-F12F-4B74-9B41-3805AB4ED204/TemporaryDirectory.LZ2YvF/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/iPhoneActivationPEM.o
+ /Library/Caches/com.apple.xbs/53DD53B8-F12F-4B74-9B41-3805AB4ED204/TemporaryDirectory.LZ2YvF/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/iPhoneCAPEM.o
+ /Library/Caches/com.apple.xbs/53DD53B8-F12F-4B74-9B41-3805AB4ED204/TemporaryDirectory.LZ2YvF/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/iPhoneDeviceCAPEM.o
+ /Library/Caches/com.apple.xbs/53DD53B8-F12F-4B74-9B41-3805AB4ED204/TemporaryDirectory.LZ2YvF/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/identity_support.o
+ /Library/Caches/com.apple.xbs/53DD53B8-F12F-4B74-9B41-3805AB4ED204/TemporaryDirectory.LZ2YvF/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/keylist.o
+ /Library/Caches/com.apple.xbs/53DD53B8-F12F-4B74-9B41-3805AB4ED204/TemporaryDirectory.LZ2YvF/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/libaks_keymanagement.o
+ /Library/Caches/com.apple.xbs/53DD53B8-F12F-4B74-9B41-3805AB4ED204/TemporaryDirectory.LZ2YvF/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/log.o
+ /Library/Caches/com.apple.xbs/53DD53B8-F12F-4B74-9B41-3805AB4ED204/TemporaryDirectory.LZ2YvF/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/main.o
+ /Library/Caches/com.apple.xbs/53DD53B8-F12F-4B74-9B41-3805AB4ED204/TemporaryDirectory.LZ2YvF/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/mobileactivationd.o
+ /Library/Caches/com.apple.xbs/53DD53B8-F12F-4B74-9B41-3805AB4ED204/TemporaryDirectory.LZ2YvF/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/msu_data_accessor.o
+ /Library/Caches/com.apple.xbs/53DD53B8-F12F-4B74-9B41-3805AB4ED204/TemporaryDirectory.LZ2YvF/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/path_support_shared.o
+ /Library/Caches/com.apple.xbs/53DD53B8-F12F-4B74-9B41-3805AB4ED204/TemporaryDirectory.LZ2YvF/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/regioncode.o
+ /Library/Caches/com.apple.xbs/53DD53B8-F12F-4B74-9B41-3805AB4ED204/TemporaryDirectory.LZ2YvF/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/requests.o
+ /Library/Caches/com.apple.xbs/53DD53B8-F12F-4B74-9B41-3805AB4ED204/TemporaryDirectory.LZ2YvF/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/requests_network.o
+ /Library/Caches/com.apple.xbs/53DD53B8-F12F-4B74-9B41-3805AB4ED204/TemporaryDirectory.LZ2YvF/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/requests_support.o
+ /Library/Caches/com.apple.xbs/53DD53B8-F12F-4B74-9B41-3805AB4ED204/TemporaryDirectory.LZ2YvF/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/reverseproxy.o
+ /Library/Caches/com.apple.xbs/53DD53B8-F12F-4B74-9B41-3805AB4ED204/TemporaryDirectory.LZ2YvF/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/root_certificates.o
+ /Library/Caches/com.apple.xbs/53DD53B8-F12F-4B74-9B41-3805AB4ED204/TemporaryDirectory.LZ2YvF/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/runtime_environment.o
+ /Library/Caches/com.apple.xbs/53DD53B8-F12F-4B74-9B41-3805AB4ED204/TemporaryDirectory.LZ2YvF/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/security_keymanagement.o
+ /Library/Caches/com.apple.xbs/53DD53B8-F12F-4B74-9B41-3805AB4ED204/TemporaryDirectory.LZ2YvF/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/signpost.o
+ /Library/Caches/com.apple.xbs/53DD53B8-F12F-4B74-9B41-3805AB4ED204/TemporaryDirectory.LZ2YvF/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/splunk_logging.o
+ /Library/Caches/com.apple.xbs/53DD53B8-F12F-4B74-9B41-3805AB4ED204/TemporaryDirectory.LZ2YvF/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/support.o
+ /Library/Caches/com.apple.xbs/53DD53B8-F12F-4B74-9B41-3805AB4ED204/TemporaryDirectory.LZ2YvF/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/sysctl_.o
+ /Library/Caches/com.apple.xbs/53DD53B8-F12F-4B74-9B41-3805AB4ED204/TemporaryDirectory.LZ2YvF/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/sysctl__darwin.o
+ /Library/Caches/com.apple.xbs/53DD53B8-F12F-4B74-9B41-3805AB4ED204/TemporaryDirectory.LZ2YvF/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/trial.o
+ /Library/Caches/com.apple.xbs/53DD53B8-F12F-4B74-9B41-3805AB4ED204/TemporaryDirectory.LZ2YvF/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/vm_host_support.o
+ /Library/Caches/com.apple.xbs/53DD53B8-F12F-4B74-9B41-3805AB4ED204/TemporaryDirectory.LZ2YvF/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/vm_libavp.o
+ /Library/Caches/com.apple.xbs/53DD53B8-F12F-4B74-9B41-3805AB4ED204/TemporaryDirectory.LZ2YvF/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/vm_support.o
+ /Library/Caches/com.apple.xbs/53DD53B8-F12F-4B74-9B41-3805AB4ED204/TemporaryDirectory.LZ2YvF/Sources/MobileActivation/certs/Activation/PROD/
+ /Library/Caches/com.apple.xbs/53DD53B8-F12F-4B74-9B41-3805AB4ED204/TemporaryDirectory.LZ2YvF/Sources/MobileActivation/certs/Activation/QA/
+ /Library/Caches/com.apple.xbs/53DD53B8-F12F-4B74-9B41-3805AB4ED204/TemporaryDirectory.LZ2YvF/Sources/MobileActivation/certs/BAA/PROD/
+ /Library/Caches/com.apple.xbs/53DD53B8-F12F-4B74-9B41-3805AB4ED204/TemporaryDirectory.LZ2YvF/Sources/MobileActivation/certs/BAA/QA/
+ /Library/Caches/com.apple.xbs/53DD53B8-F12F-4B74-9B41-3805AB4ED204/TemporaryDirectory.LZ2YvF/Sources/MobileActivation/certs/UCRT/PROD/
+ /Library/Caches/com.apple.xbs/53DD53B8-F12F-4B74-9B41-3805AB4ED204/TemporaryDirectory.LZ2YvF/Sources/MobileActivation/certs/UCRT/QA/
+ /Library/Caches/com.apple.xbs/53DD53B8-F12F-4B74-9B41-3805AB4ED204/TemporaryDirectory.LZ2YvF/Sources/MobileActivation/mobileactivationd/
+ /Library/Caches/com.apple.xbs/53DD53B8-F12F-4B74-9B41-3805AB4ED204/TemporaryDirectory.LZ2YvF/Sources/MobileActivation/shared/
+ /Library/Caches/com.apple.xbs/8DBCB280-65FC-48A7-8C4C-074DDE7917BC/TemporaryDirectory.mATUM2/Sources/AppleKeyStore_libs/
+ /Library/Caches/com.apple.xbs/C1ED07BF-9AFB-4089-A6F4-1CA673B102C4/TemporaryDirectory.N67hKV/Sources/libDER/libDER/
+ NSString+MobileActivation.m
+ OBJC_IVAR_$_DeviceType._is_factory_restored
+ _NSRangeException
+ _OBJC_CLASS_$_NSException
+ __107-[MobileActivationDaemon updateBasebandTicket:baaCertData:baaIntermediateCert:options:withCompletionBlock:]_block_invoke.411
+ __107-[MobileActivationDaemon updateBasebandTicket:baaCertData:baaIntermediateCert:options:withCompletionBlock:]_block_invoke.411.cold.1
+ __107-[MobileActivationDaemon updateBasebandTicket:baaCertData:baaIntermediateCert:options:withCompletionBlock:]_block_invoke.411.cold.2
+ __107-[MobileActivationDaemon updateBasebandTicket:baaCertData:baaIntermediateCert:options:withCompletionBlock:]_block_invoke.411.cold.3
+ __107-[MobileActivationDaemon updateBasebandTicket:baaCertData:baaIntermediateCert:options:withCompletionBlock:]_block_invoke.411.cold.4
+ __61-[MobileActivationDaemon recertifyDeviceWithCompletionBlock:]_block_invoke.339
+ __62-[MobileActivationDaemon issueCollection:withCompletionBlock:]_block_invoke.487
+ __70-[MobileActivationDaemon copyLegacyDeviceIdentityWithCompletionBlock:]_block_invoke.490
+ __75-[MobileActivationDaemon issueClientCertificateLegacy:WithCompletionBlock:]_block_invoke.361
+ __90-[MobileActivationDaemon copyAttestationDictionaryWithCompletionBlock:options:completion:]_block_invoke.392
+ __94-[MobileActivationDaemon handleActivationInfoWithSession:activationSignature:completionBlock:]_block_invoke.354
+ __OBJC_$_CATEGORY_CLASS_METHODS_NSString_$_MobileActivation
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_NSString_$_MobileActivation
+ __OBJC_$_CATEGORY_NSString_$_MobileActivation
+ __block_literal_global.357
+ __block_literal_global.416
+ __block_literal_global.448
+ __block_literal_global.456
+ __block_literal_global.489
+ _envCopyString
+ _envCopyStringDarwin
+ _envSetGlobalInterface
+ _gEnvInterface
+ _gSysctlInterface
+ _isRunningInRecoveryFromEnv
+ _isRunningInRecoveryFromSysctl
+ _is_factory_restored
+ _kMAIsFactoryRestoredOverride
+ _kMARuntimeEnvironmentOSEnvironmentRecoveryValue
+ _kMARuntimeEnvironmentOSEnvironmentSysctlKey
+ _objc_msgSend$appendBytes:length:
+ _objc_msgSend$dataWithCapacity:
+ _objc_msgSend$is_factory_restored
+ _objc_msgSend$lastByte
+ _objc_msgSend$lastByteEqualTo:
+ _objc_msgSend$raise:format:
+ _objc_msgSend$stringWithUTF8StringData:
+ _os_unfair_lock_lock
+ _os_unfair_lock_unlock
+ _strtoul
+ _sysctlCopyData
+ _sysctlCopyDataDarwin
+ _sysctlSetGlobalInterface
+ env.m
+ env_darwin.m
+ runtime_environment.m
+ sysctl_.m
+ sysctl__darwin.m
- /AppleInternal/Library/BuildRoots/4~CIVAugADxzDny4-IaryLNZqAxdcRE1l7PqMx9Ac/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/local/lib/amd/libDER.a(DER_Decode.o)
- /AppleInternal/Library/BuildRoots/4~CIVAugADxzDny4-IaryLNZqAxdcRE1l7PqMx9Ac/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/local/lib/libCoreTrust.a(AppleAnchors.o)
- /AppleInternal/Library/BuildRoots/4~CIVAugADxzDny4-IaryLNZqAxdcRE1l7PqMx9Ac/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/local/lib/libCoreTrust.a(CMS.o)
- /AppleInternal/Library/BuildRoots/4~CIVAugADxzDny4-IaryLNZqAxdcRE1l7PqMx9Ac/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/local/lib/libCoreTrust.a(CTEvaluate.o)
- /AppleInternal/Library/BuildRoots/4~CIVAugADxzDny4-IaryLNZqAxdcRE1l7PqMx9Ac/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/local/lib/libCoreTrust.a(CTEvaluateBAA.o)
- /AppleInternal/Library/BuildRoots/4~CIVAugADxzDny4-IaryLNZqAxdcRE1l7PqMx9Ac/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/local/lib/libCoreTrust.a(CryptoUtils.o)
- /AppleInternal/Library/BuildRoots/4~CIVAugADxzDny4-IaryLNZqAxdcRE1l7PqMx9Ac/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/local/lib/libCoreTrust.a(DERUtils.o)
- /AppleInternal/Library/BuildRoots/4~CIVAugADxzDny4-IaryLNZqAxdcRE1l7PqMx9Ac/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/local/lib/libCoreTrust.a(X509Certificate.o)
- /AppleInternal/Library/BuildRoots/4~CIVAugADxzDny4-IaryLNZqAxdcRE1l7PqMx9Ac/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/local/lib/libCoreTrust.a(X509Chain.o)
- /AppleInternal/Library/BuildRoots/4~CIVAugADxzDny4-IaryLNZqAxdcRE1l7PqMx9Ac/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/local/lib/libCoreTrust.a(X509Policy.o)
- /AppleInternal/Library/BuildRoots/4~CIVAugADxzDny4-IaryLNZqAxdcRE1l7PqMx9Ac/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/local/lib/libCoreTrust.a(iCDPAnchors.o)
- /AppleInternal/Library/BuildRoots/4~CIVAugADxzDny4-IaryLNZqAxdcRE1l7PqMx9Ac/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/local/lib/libaks.a(acl_keys.o)
- /AppleInternal/Library/BuildRoots/4~CIVAugADxzDny4-IaryLNZqAxdcRE1l7PqMx9Ac/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/local/lib/libaks.a(aks_pack.o)
- /AppleInternal/Library/BuildRoots/4~CIVAugADxzDny4-IaryLNZqAxdcRE1l7PqMx9Ac/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/local/lib/libaks.a(der_utils.o)
- /AppleInternal/Library/BuildRoots/4~CIVAugADxzDny4-IaryLNZqAxdcRE1l7PqMx9Ac/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/local/lib/libaks.a(firebloom_hacks.o)
- /AppleInternal/Library/BuildRoots/4~CIVAugADxzDny4-IaryLNZqAxdcRE1l7PqMx9Ac/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/local/lib/libaks.a(libaks_client.o)
- /AppleInternal/Library/BuildRoots/4~CIVAugADxzDny4-IaryLNZqAxdcRE1l7PqMx9Ac/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/local/lib/libaks.a(libaks_internal.o)
- /AppleInternal/Library/BuildRoots/4~CIVAugADxzDny4-IaryLNZqAxdcRE1l7PqMx9Ac/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/local/lib/libaks.a(libaks_ref_key.o)
- /Library/Caches/com.apple.xbs/5E3D7A20-2586-48C9-BDE8-85166E801D6C/TemporaryDirectory.sOvK8S/Sources/CoreTrust/Source/
- /Library/Caches/com.apple.xbs/6D4D3654-5503-43C3-A5E9-B1A70297643B/TemporaryDirectory.DGwI0F/Sources/libDER/libDER/
- /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/BAAASMFiOSRootCAPEM.o
- /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/BAAMFiRootCAPEM.o
- /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/BAASCRTRootCAPEM.o
- /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/BAAUCRTRootCAPEM.o
- /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/BAAVMRootCAPEM.o
- /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/FactoryUCRTRootCAPEM.o
- /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/GestaltHlpr.o
- /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/MACollectionInterface.o
- /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/MATelephonyInfo.o
- /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/MobileActivationError.o
- /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/MobileActivationErrorPrivate.o
- /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/MobileRecertifyEngine.o
- /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/NSData+MobileActivation.o
- /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/NSDateFormatter+MobileActivation.o
- /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/NSDictionary+MobileActivation.o
- /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/NetworkProvider.o
- /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/QABAAASMFiOSRootCAPEM.o
- /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/QABAAMFiRootCAPEM.o
- /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/QABAASCRTRootCAPEM.o
- /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/QABAAUCRTRootCAPEM.o
- /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/QABAAVMRootCAPEM.o
- /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/QAIphoneActivationPEM.o
- /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/QAIphoneDeviceCAPEM.o
- /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/QAUCRTRootCAP384PEM.o
- /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/QAUCRTRootCAPEM.o
- /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/QAUCRTSubCAPEM.o
- /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/RaptorActivationPEM.o
- /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/RaptorDeviceCAPEM.o
- /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/UCRTRootCAPEM.o
- /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/UCRTSubCAPEM.o
- /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/activation_support.o
- /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/activation_support_shared.o
- /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/authkit.o
- /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/baa.o
- /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/baa_oids.o
- /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/battery_management.o
- /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/bridge.o
- /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/bridge_support.o
- /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/common.o
- /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/coretrust.o
- /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/crypto.o
- /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/data_ark.o
- /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/data_migration_support.o
- /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/device_tree.o
- /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/dsp.o
- /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/findmy.o
- /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/host.o
- /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/iPhoneActivationPEM.o
- /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/iPhoneCAPEM.o
- /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/iPhoneDeviceCAPEM.o
- /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/identity_support.o
- /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/keylist.o
- /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/libaks_keymanagement.o
- /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/log.o
- /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/main.o
- /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/mobileactivationd.o
- /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/msu_data_accessor.o
- /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/path_support_shared.o
- /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/regioncode.o
- /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/requests.o
- /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/requests_network.o
- /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/requests_support.o
- /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/reverseproxy.o
- /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/root_certificates.o
- /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/security_keymanagement.o
- /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/signpost.o
- /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/splunk_logging.o
- /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/support.o
- /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/trial.o
- /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/vm_host_support.o
- /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/vm_libavp.o
- /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/vm_support.o
- /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Sources/MobileActivation/certs/Activation/PROD/
- /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Sources/MobileActivation/certs/Activation/QA/
- /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Sources/MobileActivation/certs/BAA/PROD/
- /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Sources/MobileActivation/certs/BAA/QA/
- /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Sources/MobileActivation/certs/UCRT/PROD/
- /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Sources/MobileActivation/certs/UCRT/QA/
- /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Sources/MobileActivation/mobileactivationd/
- /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Sources/MobileActivation/shared/
- /Library/Caches/com.apple.xbs/BED3B4D7-0AE0-4137-801C-27DCB7197E88/TemporaryDirectory.lcvZrq/Sources/AppleKeyStore_libs/
- __107-[MobileActivationDaemon updateBasebandTicket:baaCertData:baaIntermediateCert:options:withCompletionBlock:]_block_invoke.408
- __107-[MobileActivationDaemon updateBasebandTicket:baaCertData:baaIntermediateCert:options:withCompletionBlock:]_block_invoke.408.cold.1
- __107-[MobileActivationDaemon updateBasebandTicket:baaCertData:baaIntermediateCert:options:withCompletionBlock:]_block_invoke.408.cold.2
- __107-[MobileActivationDaemon updateBasebandTicket:baaCertData:baaIntermediateCert:options:withCompletionBlock:]_block_invoke.408.cold.3
- __107-[MobileActivationDaemon updateBasebandTicket:baaCertData:baaIntermediateCert:options:withCompletionBlock:]_block_invoke.408.cold.4
- __61-[MobileActivationDaemon recertifyDeviceWithCompletionBlock:]_block_invoke.336
- __62-[MobileActivationDaemon issueCollection:withCompletionBlock:]_block_invoke.484
- __70-[MobileActivationDaemon copyLegacyDeviceIdentityWithCompletionBlock:]_block_invoke.487
- __75-[MobileActivationDaemon issueClientCertificateLegacy:WithCompletionBlock:]_block_invoke.358
- __90-[MobileActivationDaemon copyAttestationDictionaryWithCompletionBlock:options:completion:]_block_invoke.389
- __94-[MobileActivationDaemon handleActivationInfoWithSession:activationSignature:completionBlock:]_block_invoke.351
- __block_literal_global.354
- __block_literal_global.413
- __block_literal_global.445
- __block_literal_global.453
- __block_literal_global.486
CStrings:
+ "0"
+ "0x"
+ "1076.100.28"
+ "4"
+ "@20@0:8I16"
+ "Absinthe/2.0 iOS Device Activator (MobileActivation-1076.100.28 built on Feb 15 2026 at 23:38:57)"
+ "B20@0:8C16"
+ "C16@0:8"
+ "Device is not configured for legacy activation."
+ "IsFactoryRestoredOverride"
+ "IsFactorySignedRestore"
+ "TB,R,N,V_is_factory_restored"
+ "__OSINSTALL_ENVIRONMENT"
+ "_is_factory_restored"
+ "appendBytes:length:"
+ "dataFromHexString:"
+ "dataWithCapacity:"
+ "device-recovery"
+ "hw.osenvironment"
+ "iOS Device Activator (MobileActivation-1076.100.28)"
+ "is_factory_restored"
+ "lastByte"
+ "lastByteEqualTo:"
+ "no valid last byte for data with zero length"
+ "raise:format:"
+ "stringWithUTF8StringData:"
+ "wirelesseventanalyzerd"
- "$"
- "1076.100.26"
- "Absinthe/2.0 iOS Device Activator (MobileActivation-1076.100.26 built on Feb  5 2026 at 00:05:09)"
- "iOS Device Activator (MobileActivation-1076.100.26)"

```
