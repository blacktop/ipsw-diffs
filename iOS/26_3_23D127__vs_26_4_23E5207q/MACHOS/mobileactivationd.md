## mobileactivationd

> `/usr/libexec/mobileactivationd`

```diff

-1068.80.3.0.0
-  __TEXT.__text: 0x355590
-  __TEXT.__auth_stubs: 0x1140
-  __TEXT.__objc_stubs: 0x3040
+1076.100.26.0.0
+  __TEXT.__text: 0x35d608
+  __TEXT.__auth_stubs: 0x1160
+  __TEXT.__objc_stubs: 0x30e0
   __TEXT.__objc_methlist: 0x10b4
-  __TEXT.__const: 0x5c6a8
-  __TEXT.__cstring: 0xe44f
-  __TEXT.__objc_methname: 0x3e92
-  __TEXT.__oslogstring: 0xee1
+  __TEXT.__const: 0x5c348
+  __TEXT.__cstring: 0xe8a4
+  __TEXT.__objc_methname: 0x3eea
+  __TEXT.__oslogstring: 0xf38
   __TEXT.__objc_classname: 0x1b4
   __TEXT.__objc_methtype: 0x102a
-  __TEXT.__gcc_except_tab: 0x1b00
+  __TEXT.__gcc_except_tab: 0x1c3c
   __TEXT.__dlopen_cstrs: 0x294
   __TEXT.__ustring: 0x4
-  __TEXT.__unwind_info: 0x1130
+  __TEXT.__unwind_info: 0x1190
   __TEXT.__eh_frame: 0xa0
-  __DATA_CONST.__auth_got: 0x8b0
-  __DATA_CONST.__got: 0x470
+  __DATA_CONST.__auth_got: 0x8c0
+  __DATA_CONST.__got: 0x488
   __DATA_CONST.__auth_ptr: 0x78
-  __DATA_CONST.__const: 0x1e858
-  __DATA_CONST.__cfstring: 0xc9c0
+  __DATA_CONST.__const: 0x1e9c8
+  __DATA_CONST.__cfstring: 0xcea0
   __DATA_CONST.__objc_classlist: 0x50
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x40
-  __DATA_CONST.__objc_intobj: 0x258
-  __DATA_CONST.__objc_arraydata: 0x4b0
+  __DATA_CONST.__objc_intobj: 0x270
+  __DATA_CONST.__objc_arraydata: 0x4f0
   __DATA_CONST.__objc_arrayobj: 0x90
   __DATA.__objc_const: 0x1888
-  __DATA.__objc_selrefs: 0x1030
+  __DATA.__objc_selrefs: 0x1058
   __DATA.__objc_ivar: 0xf8
   __DATA.__objc_data: 0x320
-  __DATA.__data: 0x1528
-  __DATA.__bss: 0x53c
-  __DATA.__common: 0xab0
+  __DATA.__data: 0x1b38
+  __DATA.__bss: 0x54c
+  __DATA.__common: 0xb30
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreTelephony.framework/CoreTelephony

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/liblockdown.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 16562CDD-6290-3B4B-8ADE-BF40E1456428
-  Functions: 1544
-  Symbols:   10489
-  CStrings:  4546
+  UUID: 205AD0C4-C45C-357C-AA48-09FA3E641005
+  Functions: 1598
+  Symbols:   10803
+  CStrings:  4639
 
Symbols:
+ -[MobileActivationDaemon getUCRTSalvageStateWithCompletionBlock:]
+ /AppleInternal/Library/BuildRoots/4~CIVAugADxzDny4-IaryLNZqAxdcRE1l7PqMx9Ac/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/local/lib/amd/libDER.a(DER_Decode.o)
+ /AppleInternal/Library/BuildRoots/4~CIVAugADxzDny4-IaryLNZqAxdcRE1l7PqMx9Ac/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/local/lib/libCoreTrust.a(AppleAnchors.o)
+ /AppleInternal/Library/BuildRoots/4~CIVAugADxzDny4-IaryLNZqAxdcRE1l7PqMx9Ac/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/local/lib/libCoreTrust.a(CMS.o)
+ /AppleInternal/Library/BuildRoots/4~CIVAugADxzDny4-IaryLNZqAxdcRE1l7PqMx9Ac/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/local/lib/libCoreTrust.a(CTEvaluate.o)
+ /AppleInternal/Library/BuildRoots/4~CIVAugADxzDny4-IaryLNZqAxdcRE1l7PqMx9Ac/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/local/lib/libCoreTrust.a(CTEvaluateBAA.o)
+ /AppleInternal/Library/BuildRoots/4~CIVAugADxzDny4-IaryLNZqAxdcRE1l7PqMx9Ac/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/local/lib/libCoreTrust.a(CryptoUtils.o)
+ /AppleInternal/Library/BuildRoots/4~CIVAugADxzDny4-IaryLNZqAxdcRE1l7PqMx9Ac/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/local/lib/libCoreTrust.a(DERUtils.o)
+ /AppleInternal/Library/BuildRoots/4~CIVAugADxzDny4-IaryLNZqAxdcRE1l7PqMx9Ac/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/local/lib/libCoreTrust.a(X509Certificate.o)
+ /AppleInternal/Library/BuildRoots/4~CIVAugADxzDny4-IaryLNZqAxdcRE1l7PqMx9Ac/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/local/lib/libCoreTrust.a(X509Chain.o)
+ /AppleInternal/Library/BuildRoots/4~CIVAugADxzDny4-IaryLNZqAxdcRE1l7PqMx9Ac/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/local/lib/libCoreTrust.a(X509Policy.o)
+ /AppleInternal/Library/BuildRoots/4~CIVAugADxzDny4-IaryLNZqAxdcRE1l7PqMx9Ac/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/local/lib/libCoreTrust.a(iCDPAnchors.o)
+ /AppleInternal/Library/BuildRoots/4~CIVAugADxzDny4-IaryLNZqAxdcRE1l7PqMx9Ac/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/local/lib/libaks.a(acl_keys.o)
+ /AppleInternal/Library/BuildRoots/4~CIVAugADxzDny4-IaryLNZqAxdcRE1l7PqMx9Ac/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/local/lib/libaks.a(aks_pack.o)
+ /AppleInternal/Library/BuildRoots/4~CIVAugADxzDny4-IaryLNZqAxdcRE1l7PqMx9Ac/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/local/lib/libaks.a(der_utils.o)
+ /AppleInternal/Library/BuildRoots/4~CIVAugADxzDny4-IaryLNZqAxdcRE1l7PqMx9Ac/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/local/lib/libaks.a(firebloom_hacks.o)
+ /AppleInternal/Library/BuildRoots/4~CIVAugADxzDny4-IaryLNZqAxdcRE1l7PqMx9Ac/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/local/lib/libaks.a(libaks_client.o)
+ /AppleInternal/Library/BuildRoots/4~CIVAugADxzDny4-IaryLNZqAxdcRE1l7PqMx9Ac/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/local/lib/libaks.a(libaks_internal.o)
+ /AppleInternal/Library/BuildRoots/4~CIVAugADxzDny4-IaryLNZqAxdcRE1l7PqMx9Ac/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/local/lib/libaks.a(libaks_ref_key.o)
+ /Library/Caches/com.apple.xbs/5E3D7A20-2586-48C9-BDE8-85166E801D6C/TemporaryDirectory.sOvK8S/Sources/CoreTrust/Source/
+ /Library/Caches/com.apple.xbs/6D4D3654-5503-43C3-A5E9-B1A70297643B/TemporaryDirectory.DGwI0F/Sources/libDER/libDER/
+ /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/BAAASMFiOSRootCAPEM.o
+ /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/BAAMFiRootCAPEM.o
+ /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/BAASCRTRootCAPEM.o
+ /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/BAAUCRTRootCAPEM.o
+ /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/BAAVMRootCAPEM.o
+ /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/FactoryUCRTRootCAPEM.o
+ /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/GestaltHlpr.o
+ /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/MACollectionInterface.o
+ /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/MATelephonyInfo.o
+ /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/MobileActivationError.o
+ /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/MobileActivationErrorPrivate.o
+ /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/MobileRecertifyEngine.o
+ /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/NSData+MobileActivation.o
+ /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/NSDateFormatter+MobileActivation.o
+ /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/NSDictionary+MobileActivation.o
+ /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/NetworkProvider.o
+ /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/QABAAASMFiOSRootCAPEM.o
+ /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/QABAAMFiRootCAPEM.o
+ /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/QABAASCRTRootCAPEM.o
+ /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/QABAAUCRTRootCAPEM.o
+ /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/QABAAVMRootCAPEM.o
+ /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/QAIphoneActivationPEM.o
+ /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/QAIphoneDeviceCAPEM.o
+ /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/QAUCRTRootCAP384PEM.o
+ /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/QAUCRTRootCAPEM.o
+ /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/QAUCRTSubCAPEM.o
+ /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/RaptorActivationPEM.o
+ /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/RaptorDeviceCAPEM.o
+ /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/UCRTRootCAPEM.o
+ /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/UCRTSubCAPEM.o
+ /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/activation_support.o
+ /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/activation_support_shared.o
+ /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/authkit.o
+ /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/baa.o
+ /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/baa_oids.o
+ /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/battery_management.o
+ /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/bridge.o
+ /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/bridge_support.o
+ /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/common.o
+ /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/coretrust.o
+ /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/crypto.o
+ /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/data_ark.o
+ /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/data_migration_support.o
+ /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/device_tree.o
+ /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/dsp.o
+ /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/findmy.o
+ /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/host.o
+ /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/iPhoneActivationPEM.o
+ /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/iPhoneCAPEM.o
+ /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/iPhoneDeviceCAPEM.o
+ /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/identity_support.o
+ /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/keylist.o
+ /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/libaks_keymanagement.o
+ /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/log.o
+ /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/main.o
+ /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/mobileactivationd.o
+ /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/msu_data_accessor.o
+ /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/path_support_shared.o
+ /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/regioncode.o
+ /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/requests.o
+ /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/requests_network.o
+ /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/requests_support.o
+ /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/reverseproxy.o
+ /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/root_certificates.o
+ /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/security_keymanagement.o
+ /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/signpost.o
+ /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/splunk_logging.o
+ /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/support.o
+ /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/trial.o
+ /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/vm_host_support.o
+ /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/vm_libavp.o
+ /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/vm_support.o
+ /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Sources/MobileActivation/certs/Activation/PROD/
+ /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Sources/MobileActivation/certs/Activation/QA/
+ /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Sources/MobileActivation/certs/BAA/PROD/
+ /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Sources/MobileActivation/certs/BAA/QA/
+ /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Sources/MobileActivation/certs/UCRT/PROD/
+ /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Sources/MobileActivation/certs/UCRT/QA/
+ /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Sources/MobileActivation/mobileactivationd/
+ /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Sources/MobileActivation/shared/
+ /Library/Caches/com.apple.xbs/BED3B4D7-0AE0-4137-801C-27DCB7197E88/TemporaryDirectory.lcvZrq/Sources/AppleKeyStore_libs/
+ GCC_except_table114
+ GCC_except_table32
+ GCC_except_table69
+ GCC_except_table80
+ GCC_except_table87
+ GCC_except_table94
+ _CFPreferencesSynchronize
+ _CMSAttributeParseAppleHashAgilityV2
+ _CMSGetCertificateUsingIssuerSerialNumber
+ _CMSParseEncapsulatedContent
+ _CMSParseSignedData
+ _CTConvertAsciiHexToUint64
+ _EIqMKHg4gO6i
+ _OBJC_CLASS_$_NSLocale
+ _OUTLINED_FUNCTION_15
+ _OUTLINED_FUNCTION_20
+ _OUTLINED_FUNCTION_21
+ _OUTLINED_FUNCTION_34
+ _OUTLINED_FUNCTION_35
+ _OUTLINED_FUNCTION_36
+ _OUTLINED_FUNCTION_37
+ _OUTLINED_FUNCTION_39
+ _OUTLINED_FUNCTION_47
+ _OUTLINED_FUNCTION_52
+ _OUTLINED_FUNCTION_53
+ _OUTLINED_FUNCTION_56
+ _OUTLINED_FUNCTION_57
+ _OUTLINED_FUNCTION_58
+ _OUTLINED_FUNCTION_62
+ _OUTLINED_FUNCTION_63
+ _OUTLINED_FUNCTION_68
+ _SALVAGE_STATE_KBB_SHARED_SERIAL
+ _SALVAGE_STATE_KBB_UNIQUE_SERIAL
+ __107-[MobileActivationDaemon updateBasebandTicket:baaCertData:baaIntermediateCert:options:withCompletionBlock:]_block_invoke.408
+ __107-[MobileActivationDaemon updateBasebandTicket:baaCertData:baaIntermediateCert:options:withCompletionBlock:]_block_invoke.408.cold.1
+ __107-[MobileActivationDaemon updateBasebandTicket:baaCertData:baaIntermediateCert:options:withCompletionBlock:]_block_invoke.408.cold.2
+ __107-[MobileActivationDaemon updateBasebandTicket:baaCertData:baaIntermediateCert:options:withCompletionBlock:]_block_invoke.408.cold.3
+ __107-[MobileActivationDaemon updateBasebandTicket:baaCertData:baaIntermediateCert:options:withCompletionBlock:]_block_invoke.408.cold.4
+ __61-[MobileActivationDaemon recertifyDeviceWithCompletionBlock:]_block_invoke.336
+ __62-[MobileActivationDaemon issueCollection:withCompletionBlock:]_block_invoke.484
+ __70-[MobileActivationDaemon copyLegacyDeviceIdentityWithCompletionBlock:]_block_invoke.487
+ __75-[MobileActivationDaemon issueClientCertificateLegacy:WithCompletionBlock:]_block_invoke.358
+ __90-[MobileActivationDaemon copyAttestationDictionaryWithCompletionBlock:options:completion:]_block_invoke.389
+ __94-[MobileActivationDaemon handleActivationInfoWithSession:activationSignature:completionBlock:]_block_invoke.351
+ ___65-[MobileActivationDaemon getUCRTSalvageStateWithCompletionBlock:]_block_invoke
+ ___block_descriptor_119_e8_32s40s48s56s64s72s80bs88r96r104r_e5_v8?0l
+ ___block_descriptor_136_e8_32s40s48s56s64s72s80s88s96bs104r112r120r_e5_v8?0l
+ ___copy_device_region_info_path_block_invoke
+ ___copy_helper_block_e8_32s40s48s56s64s72s80s88s96b104r112r120r
+ ___destroy_helper_block_e8_32s40s48s56s64s72s80s88s96s104r112r120r
+ __block_descriptor_tmp.181
+ __block_literal_global.183
+ __block_literal_global.207
+ __block_literal_global.313
+ __block_literal_global.351
+ __block_literal_global.354
+ __block_literal_global.4
+ __block_literal_global.413
+ __block_literal_global.445
+ __block_literal_global.453
+ __block_literal_global.486
+ __block_literal_global.552
+ __block_literal_global.561
+ __block_literal_global.569
+ __block_literal_global.572
+ __block_literal_global.577
+ __block_literal_global.67
+ __block_literal_global.89
+ __collection_activity_handler_block_invoke.556
+ __collection_activity_handler_block_invoke.559
+ __collection_activity_handler_block_invoke_2.557
+ __dcrt_oob_activity_handler_block_invoke.543
+ __dcrt_oob_activity_handler_block_invoke.545
+ __dcrt_oob_activity_handler_block_invoke.546
+ __dcrt_oob_activity_handler_block_invoke.547
+ __dcrt_oob_activity_handler_block_invoke.550
+ __dcrt_oob_activity_handler_block_invoke_2.548
+ __dcrt_oob_load_spreading_activity_handler_block_invoke.538
+ __issueClientCertificateWithReferenceKey_block_invoke.311
+ __register_xpc_activities_block_invoke.796
+ __register_xpc_activities_block_invoke.796.cold.1
+ __register_xpc_activities_block_invoke.797
+ __register_xpc_activities_block_invoke.797.cold.1
+ __register_xpc_activities_block_invoke.798
+ __register_xpc_activities_block_invoke.798.cold.1
+ __register_xpc_activities_block_invoke.799
+ __register_xpc_activities_block_invoke.799.cold.1
+ __register_xpc_activities_block_invoke.800
+ __register_xpc_activities_block_invoke.800.cold.1
+ __register_xpc_activities_block_invoke.801
+ __register_xpc_activities_block_invoke.801.cold.1
+ __register_xpc_activities_block_invoke.802
+ __register_xpc_activities_block_invoke.802.cold.1
+ __register_xpc_activities_block_invoke.803
+ __register_xpc_activities_block_invoke.803.cold.1
+ __register_xpc_activities_block_invoke.804
+ __register_xpc_activities_block_invoke.804.cold.1
+ __scheduleXPCActivity_block_invoke.24
+ __scheduleXPCActivity_block_invoke.24.cold.1
+ __ucrt_oob_activity_handler_block_invoke.570
+ __ucrt_oob_activity_handler_block_invoke.573
+ __ucrt_oob_activity_handler_block_invoke.575
+ __ucrt_oob_activity_handler_block_invoke_2.574
+ _abort
+ _copySalvageState
+ _copy_device_region_info_from_activation_record
+ _copy_device_region_info_path
+ _deactivationRequiredForSalavagedDevice
+ _geteuid
+ _isRunningAsRoot
+ _kCFPreferencesAnyUser
+ _kCFPreferencesCurrentHost
+ _kMACertifySBOverrideURL
+ _kMACertifySessionOverrideURL
+ _kMADeviceRegionCountryCode
+ _kMADeviceRegionRegionInfo
+ _kMADeviceRegionSoftwareBehaviors
+ _kMAIsInPalletUpdateModeOverride
+ _kMAOptionsBAAMatterSubjectDN
+ _kMAOptionsBAAMatterSubjectDNAppleHome
+ _kMAOptionsBAAMatterSubjectDNAppleKeychain
+ _kMAOptionsBAAOIDMatterSubjectDN
+ _kMAOptionsRebootAfterDeactivation
+ _kMAShiptoCountryCode
+ _kMAUCRTSLVGDate
+ _kMAUCRTSLVGState
+ _kMAUCRTSLVGStateKBBSharedSerial
+ _kMAUCRTSLVGStateKBBUniqueSerial
+ _kMAUCRTSLVGStateKGB
+ _kMAUCRTSLVGStateUnavailable
+ _mmap
+ _munmap
+ _objc_initWeak
+ _objc_msgSend$dictionary
+ _objc_msgSend$initWithSuiteName:
+ _objc_msgSend$localeWithLocaleIdentifier:
+ _objc_msgSend$setLocale:
+ _objc_msgSend$writeToFile:atomically:
+ _readUserDefaults
+ _removeUserDefaults
+ _salvagedFlagSetInCertificate
+ _sched_yield
+ _store_device_region_info
+ _synchronizeUserDefaults
+ _sysconf
+ _writeUserDefaults
+ copy_device_region_info_path.cold.1
+ copy_device_region_info_path.onceToken
+ copy_device_region_info_path.retval
- -[MobileActivationDaemon copyRegionDataForGestaltWithCompletionBlock:]
- /AppleInternal/Library/BuildRoots/4~CHKyugCWzTCwGAL76-AW157dWDISyL5VurfRuho/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/lib/amd/libDER.a(DER_Decode.o)
- /AppleInternal/Library/BuildRoots/4~CHKyugCWzTCwGAL76-AW157dWDISyL5VurfRuho/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/lib/libCoreTrust.a(AppleAnchors.o)
- /AppleInternal/Library/BuildRoots/4~CHKyugCWzTCwGAL76-AW157dWDISyL5VurfRuho/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/lib/libCoreTrust.a(CMS.o)
- /AppleInternal/Library/BuildRoots/4~CHKyugCWzTCwGAL76-AW157dWDISyL5VurfRuho/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/lib/libCoreTrust.a(CTEvaluate.o)
- /AppleInternal/Library/BuildRoots/4~CHKyugCWzTCwGAL76-AW157dWDISyL5VurfRuho/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/lib/libCoreTrust.a(CTEvaluateBAA.o)
- /AppleInternal/Library/BuildRoots/4~CHKyugCWzTCwGAL76-AW157dWDISyL5VurfRuho/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/lib/libCoreTrust.a(CryptoUtils.o)
- /AppleInternal/Library/BuildRoots/4~CHKyugCWzTCwGAL76-AW157dWDISyL5VurfRuho/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/lib/libCoreTrust.a(DERUtils.o)
- /AppleInternal/Library/BuildRoots/4~CHKyugCWzTCwGAL76-AW157dWDISyL5VurfRuho/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/lib/libCoreTrust.a(X509Certificate.o)
- /AppleInternal/Library/BuildRoots/4~CHKyugCWzTCwGAL76-AW157dWDISyL5VurfRuho/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/lib/libCoreTrust.a(X509Chain.o)
- /AppleInternal/Library/BuildRoots/4~CHKyugCWzTCwGAL76-AW157dWDISyL5VurfRuho/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/lib/libCoreTrust.a(X509Policy.o)
- /AppleInternal/Library/BuildRoots/4~CHKyugCWzTCwGAL76-AW157dWDISyL5VurfRuho/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/lib/libCoreTrust.a(iCDPAnchors.o)
- /AppleInternal/Library/BuildRoots/4~CHKyugCWzTCwGAL76-AW157dWDISyL5VurfRuho/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/lib/libaks.a(acl_keys.o)
- /AppleInternal/Library/BuildRoots/4~CHKyugCWzTCwGAL76-AW157dWDISyL5VurfRuho/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/lib/libaks.a(aks_pack.o)
- /AppleInternal/Library/BuildRoots/4~CHKyugCWzTCwGAL76-AW157dWDISyL5VurfRuho/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/lib/libaks.a(der_utils.o)
- /AppleInternal/Library/BuildRoots/4~CHKyugCWzTCwGAL76-AW157dWDISyL5VurfRuho/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/lib/libaks.a(firebloom_hacks.o)
- /AppleInternal/Library/BuildRoots/4~CHKyugCWzTCwGAL76-AW157dWDISyL5VurfRuho/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/lib/libaks.a(libaks_client.o)
- /AppleInternal/Library/BuildRoots/4~CHKyugCWzTCwGAL76-AW157dWDISyL5VurfRuho/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/lib/libaks.a(libaks_internal.o)
- /AppleInternal/Library/BuildRoots/4~CHKyugCWzTCwGAL76-AW157dWDISyL5VurfRuho/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/lib/libaks.a(libaks_ref_key.o)
- /Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/BAAASMFiOSRootCAPEM.o
- /Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/BAAMFiRootCAPEM.o
- /Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/BAASCRTRootCAPEM.o
- /Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/BAAUCRTRootCAPEM.o
- /Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/BAAVMRootCAPEM.o
- /Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/FactoryUCRTRootCAPEM.o
- /Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/GestaltHlpr.o
- /Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/MACollectionInterface.o
- /Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/MATelephonyInfo.o
- /Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/MobileActivationError.o
- /Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/MobileActivationErrorPrivate.o
- /Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/MobileRecertifyEngine.o
- /Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/NSData+MobileActivation.o
- /Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/NSDateFormatter+MobileActivation.o
- /Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/NSDictionary+MobileActivation.o
- /Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/NetworkProvider.o
- /Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/QABAAASMFiOSRootCAPEM.o
- /Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/QABAAMFiRootCAPEM.o
- /Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/QABAASCRTRootCAPEM.o
- /Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/QABAAUCRTRootCAPEM.o
- /Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/QABAAVMRootCAPEM.o
- /Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/QAIphoneActivationPEM.o
- /Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/QAIphoneDeviceCAPEM.o
- /Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/QAUCRTRootCAP384PEM.o
- /Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/QAUCRTRootCAPEM.o
- /Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/QAUCRTSubCAPEM.o
- /Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/RaptorActivationPEM.o
- /Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/RaptorDeviceCAPEM.o
- /Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/UCRTRootCAPEM.o
- /Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/UCRTSubCAPEM.o
- /Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/activation_support.o
- /Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/activation_support_shared.o
- /Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/authkit.o
- /Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/baa.o
- /Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/baa_oids.o
- /Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/battery_management.o
- /Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/bridge.o
- /Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/bridge_support.o
- /Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/common.o
- /Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/coretrust.o
- /Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/crypto.o
- /Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/data_ark.o
- /Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/data_migration_support.o
- /Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/device_tree.o
- /Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/dsp.o
- /Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/findmy.o
- /Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/host.o
- /Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/iPhoneActivationPEM.o
- /Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/iPhoneCAPEM.o
- /Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/iPhoneDeviceCAPEM.o
- /Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/identity_support.o
- /Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/keylist.o
- /Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/libaks_keymanagement.o
- /Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/log.o
- /Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/main.o
- /Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/mobileactivationd.o
- /Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/msu_data_accessor.o
- /Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/path_support_shared.o
- /Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/regioncode.o
- /Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/requests.o
- /Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/requests_network.o
- /Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/requests_support.o
- /Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/reverseproxy.o
- /Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/root_certificates.o
- /Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/security_keymanagement.o
- /Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/signpost.o
- /Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/splunk_logging.o
- /Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/support.o
- /Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/trial.o
- /Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/vm_host_support.o
- /Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/vm_libavp.o
- /Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/vm_support.o
- /Library/Caches/com.apple.xbs/Sources/AppleKeyStore_libs/
- /Library/Caches/com.apple.xbs/Sources/CoreTrust/Source/
- /Library/Caches/com.apple.xbs/Sources/MobileActivation/certs/Activation/PROD/
- /Library/Caches/com.apple.xbs/Sources/MobileActivation/certs/Activation/QA/
- /Library/Caches/com.apple.xbs/Sources/MobileActivation/certs/BAA/PROD/
- /Library/Caches/com.apple.xbs/Sources/MobileActivation/certs/BAA/QA/
- /Library/Caches/com.apple.xbs/Sources/MobileActivation/certs/UCRT/PROD/
- /Library/Caches/com.apple.xbs/Sources/MobileActivation/certs/UCRT/QA/
- /Library/Caches/com.apple.xbs/Sources/MobileActivation/mobileactivationd/
- /Library/Caches/com.apple.xbs/Sources/MobileActivation/shared/
- /Library/Caches/com.apple.xbs/Sources/libDER/libDER/
- GCC_except_table115
- GCC_except_table30
- GCC_except_table5
- GCC_except_table70
- GCC_except_table81
- GCC_except_table88
- GCC_except_table95
- _OUTLINED_FUNCTION_12
- _OUTLINED_FUNCTION_40
- _OUTLINED_FUNCTION_41
- _OUTLINED_FUNCTION_42
- _OUTLINED_FUNCTION_44
- _OUTLINED_FUNCTION_45
- _OUTLINED_FUNCTION_46
- __107-[MobileActivationDaemon updateBasebandTicket:baaCertData:baaIntermediateCert:options:withCompletionBlock:]_block_invoke.411
- __107-[MobileActivationDaemon updateBasebandTicket:baaCertData:baaIntermediateCert:options:withCompletionBlock:]_block_invoke.411.cold.1
- __107-[MobileActivationDaemon updateBasebandTicket:baaCertData:baaIntermediateCert:options:withCompletionBlock:]_block_invoke.411.cold.2
- __107-[MobileActivationDaemon updateBasebandTicket:baaCertData:baaIntermediateCert:options:withCompletionBlock:]_block_invoke.411.cold.3
- __107-[MobileActivationDaemon updateBasebandTicket:baaCertData:baaIntermediateCert:options:withCompletionBlock:]_block_invoke.411.cold.4
- __61-[MobileActivationDaemon recertifyDeviceWithCompletionBlock:]_block_invoke.339
- __62-[MobileActivationDaemon issueCollection:withCompletionBlock:]_block_invoke.487
- __70-[MobileActivationDaemon copyLegacyDeviceIdentityWithCompletionBlock:]_block_invoke.490
- __75-[MobileActivationDaemon issueClientCertificateLegacy:WithCompletionBlock:]_block_invoke.361
- __90-[MobileActivationDaemon copyAttestationDictionaryWithCompletionBlock:options:completion:]_block_invoke.392
- __94-[MobileActivationDaemon handleActivationInfoWithSession:activationSignature:completionBlock:]_block_invoke.354
- ___block_descriptor_111_e8_32s40s48s56s64s72s80bs88r96r_e5_v8?0l
- ___block_descriptor_128_e8_32s40s48s56s64s72s80s88s96bs104r112r_e5_v8?0l
- ___copy_helper_block_e8_32s40s48s56s64s72s80s88s96b104r112r
- ___destroy_helper_block_e8_32s40s48s56s64s72s80s88s96s104r112r
- __block_descriptor_tmp.170
- __block_literal_global.172
- __block_literal_global.204
- __block_literal_global.310
- __block_literal_global.348
- __block_literal_global.357
- __block_literal_global.389
- __block_literal_global.421
- __block_literal_global.429
- __block_literal_global.489
- __block_literal_global.546
- __block_literal_global.549
- __block_literal_global.557
- __block_literal_global.560
- __block_literal_global.571
- __block_literal_global.64
- __collection_activity_handler_block_invoke.547
- __collection_activity_handler_block_invoke.550
- __collection_activity_handler_block_invoke_2.551
- __dcrt_oob_activity_handler_block_invoke.535
- __dcrt_oob_activity_handler_block_invoke.537
- __dcrt_oob_activity_handler_block_invoke.538
- __dcrt_oob_activity_handler_block_invoke.539
- __dcrt_oob_activity_handler_block_invoke.540
- __dcrt_oob_activity_handler_block_invoke_2.542
- __dcrt_oob_load_spreading_activity_handler_block_invoke.532
- __issueClientCertificateWithReferenceKey_block_invoke.308
- __register_xpc_activities_block_invoke.781
- __register_xpc_activities_block_invoke.781.cold.1
- __register_xpc_activities_block_invoke.782
- __register_xpc_activities_block_invoke.782.cold.1
- __register_xpc_activities_block_invoke.783
- __register_xpc_activities_block_invoke.783.cold.1
- __register_xpc_activities_block_invoke.784
- __register_xpc_activities_block_invoke.784.cold.1
- __register_xpc_activities_block_invoke.785
- __register_xpc_activities_block_invoke.785.cold.1
- __register_xpc_activities_block_invoke.786
- __register_xpc_activities_block_invoke.786.cold.1
- __register_xpc_activities_block_invoke.787
- __register_xpc_activities_block_invoke.787.cold.1
- __register_xpc_activities_block_invoke.788
- __register_xpc_activities_block_invoke.788.cold.1
- __register_xpc_activities_block_invoke.789
- __register_xpc_activities_block_invoke.789.cold.1
- __scheduleXPCActivity_block_invoke.21
- __scheduleXPCActivity_block_invoke.21.cold.1
- __ucrt_oob_activity_handler_block_invoke.558
- __ucrt_oob_activity_handler_block_invoke.561
- __ucrt_oob_activity_handler_block_invoke.569
- __ucrt_oob_activity_handler_block_invoke_2.568
- _create_region_data_for_gestalt
- _kMAManufacturingData
- _kMAManufacturingDataCountryCode
- _kMARegionDataForGestaltCountryCode
- _kMARegionDataForGestaltRegionInfo
- _kMARegionDataForGestaltSotwareBehaviors
- _objc_retainAutoreleaseReturnValue
CStrings:
+ "-[MobileActivationDaemon getUCRTSalvageStateWithCompletionBlock:]"
+ "1.3.6.1.4.1.37244.1.7"
+ "1076.100.26"
+ "Absinthe/2.0 iOS Device Activator (MobileActivation-1076.100.26 built on Feb  5 2026 at 00:05:09)"
+ "Activation record does not contain expected key: %@"
+ "BE/A"
+ "BR"
+ "CH"
+ "CertifySBOverrideURL"
+ "CertifySessionOverrideURL"
+ "CopySalvageStateXPC"
+ "Deactivating device: %@"
+ "DeviceRegionCountryCode"
+ "DeviceRegionRegionInfo"
+ "DeviceRegionSoftwareBehaviors"
+ "Devices"
+ "ES"
+ "FR"
+ "Failed to copy salvage state from certificate."
+ "Failed to create the device region file."
+ "Failed to decode regulatory info."
+ "Failed to override the device region info file: %@"
+ "Failed to query certificate device identifiers."
+ "Failed to read salvage date: %@"
+ "Failed to retrieve the device region file path."
+ "Failed to retrieve the device region path."
+ "Failed to store device region info."
+ "GB"
+ "Library/region_info"
+ "MatterSubjectDN"
+ "Missing salvage date."
+ "OVERRIDE: Overriding the device region info file"
+ "QL/A"
+ "RebootAfterDeactivation"
+ "Regulatory info is missing expected key: %@"
+ "SCARemoteView Appex"
+ "SLVG"
+ "Salvaged device (deactivation required)."
+ "ShiptoCountryCode"
+ "UCRT salvage state requested by %{public}@"
+ "UCRTSLVGDate"
+ "UCRTSLVGState"
+ "UCRTSLVGStateKBBSharedSerial"
+ "UCRTSLVGStateKBBUniqueSerial"
+ "UCRTSLVGStateKGB"
+ "UCRTSLVGStateUnavailable"
+ "Unrecognized Salvage state: %d"
+ "ZD/A"
+ "anomalydetectiond"
+ "com.apple.MobileAsset.DownloadService.Backported"
+ "com.apple.MobileAsset.DownloadService.Builtin"
+ "copySalvageState"
+ "copy_device_region_info_from_activation_record"
+ "dictionary"
+ "en_US_POSIX"
+ "fmdautomationtool"
+ "getUCRTSalvageStateWithCompletionBlock:"
+ "iOS Device Activator (MobileActivation-1076.100.26)"
+ "initWithSuiteName:"
+ "kMAIsInPalletUpdateModeOverride"
+ "localeWithLocaleIdentifier:"
+ "perform_luck_data_migration_tasks"
+ "recert_session_request.txt"
+ "recert_session_response.txt"
+ "region_info.plist"
+ "setLocale:"
+ "slvd"
+ "store_device_region_info"
+ "triald"
+ "triald_system"
+ "writeToFile:atomically:"
+ "yyyyMMddHHmmss'Z'"
- "-[MobileActivationDaemon copyRegionDataForGestaltWithCompletionBlock:]"
- "1068.80.3"
- "Absinthe/2.0 iOS Device Activator (MobileActivation-1068.80.3 built on Jan 20 2026 at 04:04:45)"
- "CountryCode"
- "Failed to allocate dictionary"
- "Failed to create region data."
- "Manufacturing data is missing expected key: %@"
- "ManufacturingData"
- "RegionDataForGestaltCountryCode"
- "RegionDataForGestaltRegionInfo"
- "RegionDataForGestaltSotwareBehaviors"
- "TestCountry1"
- "TestCountry1RegionCode"
- "TestCountry2"
- "TestCountry2RegionCode"
- "copyRegionDataForGestaltWithCompletionBlock:"
- "create_region_data_for_gestalt"
- "iOS Device Activator (MobileActivation-1068.80.3)"

```
