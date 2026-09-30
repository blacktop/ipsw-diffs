## mobileactivationd

> `/usr/libexec/mobileactivationd`

```diff

-1015.81.2.0.0
-  __TEXT.__text: 0x60294
+1017.100.16.0.0
+  __TEXT.__text: 0x5f6f0
   __TEXT.__auth_stubs: 0xfb0
-  __TEXT.__objc_stubs: 0x2140
-  __TEXT.__objc_methlist: 0x550
+  __TEXT.__objc_stubs: 0x2180
+  __TEXT.__objc_methlist: 0x84c
   __TEXT.__const: 0x9411
-  __TEXT.__gcc_except_tab: 0x1218
-  __TEXT.__objc_methname: 0x2584
+  __TEXT.__gcc_except_tab: 0x1224
+  __TEXT.__objc_methname: 0x25d2
   __TEXT.__oslogstring: 0x12cd
-  __TEXT.__cstring: 0xb240
+  __TEXT.__cstring: 0xb2c7
   __TEXT.__objc_classname: 0x10f
   __TEXT.__objc_methtype: 0x8db
   __TEXT.__ustring: 0x4
   __TEXT.__dlopen_cstrs: 0x1bf
-  __TEXT.__unwind_info: 0xc08
+  __TEXT.__unwind_info: 0xc20
   __DATA_CONST.__auth_got: 0x7e8
-  __DATA_CONST.__got: 0x418
-  __DATA_CONST.__auth_ptr: 0x38
-  __DATA_CONST.__const: 0x34f8
-  __DATA_CONST.__cfstring: 0x94e0
+  __DATA_CONST.__got: 0x400
+  __DATA_CONST.__auth_ptr: 0x58
+  __DATA_CONST.__const: 0x3500
+  __DATA_CONST.__cfstring: 0x95a0
   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x30

   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x28
   __DATA_CONST.__objc_intobj: 0x210
-  __DATA_CONST.__objc_arraydata: 0x450
+  __DATA_CONST.__objc_arraydata: 0x460
   __DATA_CONST.__objc_arrayobj: 0x78
-  __DATA.__objc_const: 0x1360
-  __DATA.__objc_selrefs: 0x958
+  __DATA.__objc_const: 0xdd0
+  __DATA.__objc_selrefs: 0xa88
   __DATA.__objc_ivar: 0x80
   __DATA.__objc_data: 0x230
   __DATA.__data: 0x3ca

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbootpolicy.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: DAEBF95A-1410-3E3B-B1D9-D4CC308E9041
-  Functions: 1049
-  Symbols:   7548
-  CStrings:  3458
+  UUID: 4127BEBC-EFFA-3048-8A21-C8BB695E0315
+  Functions: 1238
+  Symbols:   8110
+  CStrings:  3473
 
Symbols:
+ +[DeviceType sharedInstance].cold.1
+ +[GestaltHlpr getSharedInstance].cold.1
+ +[MALog getSharedInstance].cold.1
+ /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.4.Internal.sdk/usr/local/lib/amd/libDER.a(DER_Decode.o)
+ /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.4.Internal.sdk/usr/local/lib/libCoreTrust.a(CMS.o)
+ /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.4.Internal.sdk/usr/local/lib/libCoreTrust.a(CTEvaluate.o)
+ /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.4.Internal.sdk/usr/local/lib/libCoreTrust.a(CTEvaluateBAA.o)
+ /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.4.Internal.sdk/usr/local/lib/libCoreTrust.a(CryptoUtils.o)
+ /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.4.Internal.sdk/usr/local/lib/libCoreTrust.a(DERUtils.o)
+ /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.4.Internal.sdk/usr/local/lib/libCoreTrust.a(X509Certificate.o)
+ /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.4.Internal.sdk/usr/local/lib/libCoreTrust.a(X509Chain.o)
+ /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.4.Internal.sdk/usr/local/lib/libCoreTrust.a(X509Policy.o)
+ /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.4.Internal.sdk/usr/local/lib/libaks.a(acl_keys.o)
+ /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.4.Internal.sdk/usr/local/lib/libaks.a(der_utils.o)
+ /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.4.Internal.sdk/usr/local/lib/libaks.a(firebloom_hacks.o)
+ /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.4.Internal.sdk/usr/local/lib/libaks.a(libaks_client.o)
+ /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.4.Internal.sdk/usr/local/lib/libaks.a(libaks_internal.o)
+ /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.4.Internal.sdk/usr/local/lib/libaks.a(libaks_ref_key.o)
+ /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationdMacOS.build/Objects-normal/arm64e/BAAASMFiOSRootCAPEM.o
+ /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationdMacOS.build/Objects-normal/arm64e/BAAMFiRootCAPEM.o
+ /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationdMacOS.build/Objects-normal/arm64e/BAASCRTRootCAPEM.o
+ /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationdMacOS.build/Objects-normal/arm64e/BAAUCRTRootCAPEM.o
+ /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationdMacOS.build/Objects-normal/arm64e/BAAVMRootCAPEM.o
+ /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationdMacOS.build/Objects-normal/arm64e/FactoryUCRTRootCAPEM.o
+ /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationdMacOS.build/Objects-normal/arm64e/GestaltHlpr.o
+ /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationdMacOS.build/Objects-normal/arm64e/MobileActivationError.o
+ /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationdMacOS.build/Objects-normal/arm64e/MobileActivationErrorPrivate.o
+ /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationdMacOS.build/Objects-normal/arm64e/NSDateFormatter+MobileActivation.o
+ /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationdMacOS.build/Objects-normal/arm64e/NetworkProvider.o
+ /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationdMacOS.build/Objects-normal/arm64e/QABAAASMFiOSRootCAPEM.o
+ /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationdMacOS.build/Objects-normal/arm64e/QABAAMFiRootCAPEM.o
+ /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationdMacOS.build/Objects-normal/arm64e/QABAASCRTRootCAPEM.o
+ /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationdMacOS.build/Objects-normal/arm64e/QABAAUCRTRootCAPEM.o
+ /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationdMacOS.build/Objects-normal/arm64e/QABAAVMRootCAPEM.o
+ /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationdMacOS.build/Objects-normal/arm64e/QAIphoneActivationPEM.o
+ /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationdMacOS.build/Objects-normal/arm64e/QAIphoneDeviceCAPEM.o
+ /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationdMacOS.build/Objects-normal/arm64e/QAUCRTRootCAP384PEM.o
+ /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationdMacOS.build/Objects-normal/arm64e/QAUCRTRootCAPEM.o
+ /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationdMacOS.build/Objects-normal/arm64e/QAUCRTSubCAPEM.o
+ /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationdMacOS.build/Objects-normal/arm64e/RaptorActivationPEM.o
+ /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationdMacOS.build/Objects-normal/arm64e/RaptorDeviceCAPEM.o
+ /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationdMacOS.build/Objects-normal/arm64e/UCRTRootCAPEM.o
+ /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationdMacOS.build/Objects-normal/arm64e/UCRTSubCAPEM.o
+ /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationdMacOS.build/Objects-normal/arm64e/activationSupportMacOS.o
+ /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationdMacOS.build/Objects-normal/arm64e/activation_support_shared.o
+ /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationdMacOS.build/Objects-normal/arm64e/authkit.o
+ /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationdMacOS.build/Objects-normal/arm64e/baa.o
+ /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationdMacOS.build/Objects-normal/arm64e/baa_oids.o
+ /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationdMacOS.build/Objects-normal/arm64e/bridge.o
+ /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationdMacOS.build/Objects-normal/arm64e/bridge_support.o
+ /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationdMacOS.build/Objects-normal/arm64e/common.o
+ /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationdMacOS.build/Objects-normal/arm64e/coretrust.o
+ /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationdMacOS.build/Objects-normal/arm64e/crypto.o
+ /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationdMacOS.build/Objects-normal/arm64e/data_ark.o
+ /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationdMacOS.build/Objects-normal/arm64e/device_tree.o
+ /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationdMacOS.build/Objects-normal/arm64e/dsp.o
+ /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationdMacOS.build/Objects-normal/arm64e/findmy.o
+ /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationdMacOS.build/Objects-normal/arm64e/iPhoneActivationPEM.o
+ /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationdMacOS.build/Objects-normal/arm64e/iPhoneCAPEM.o
+ /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationdMacOS.build/Objects-normal/arm64e/iPhoneDeviceCAPEM.o
+ /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationdMacOS.build/Objects-normal/arm64e/identity_support.o
+ /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationdMacOS.build/Objects-normal/arm64e/keylist.o
+ /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationdMacOS.build/Objects-normal/arm64e/libaks_keymanagement.o
+ /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationdMacOS.build/Objects-normal/arm64e/log.o
+ /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationdMacOS.build/Objects-normal/arm64e/main.o
+ /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationdMacOS.build/Objects-normal/arm64e/mobileactivationdMacOS.o
+ /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationdMacOS.build/Objects-normal/arm64e/msu_data_accessor.o
+ /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationdMacOS.build/Objects-normal/arm64e/path_support_shared.o
+ /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationdMacOS.build/Objects-normal/arm64e/requests.o
+ /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationdMacOS.build/Objects-normal/arm64e/requests_network.o
+ /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationdMacOS.build/Objects-normal/arm64e/requests_support.o
+ /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationdMacOS.build/Objects-normal/arm64e/root_certificates.o
+ /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationdMacOS.build/Objects-normal/arm64e/security_keymanagement.o
+ /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationdMacOS.build/Objects-normal/arm64e/signpost.o
+ /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationdMacOS.build/Objects-normal/arm64e/splunk_logging.o
+ /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationdMacOS.build/Objects-normal/arm64e/vm_host_support.o
+ /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationdMacOS.build/Objects-normal/arm64e/vm_libavp.o
+ /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationdMacOS.build/Objects-normal/arm64e/vm_support.o
+ /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleKeyStore_libs/
+ /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/CoreTrust/Source/
+ /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/MobileActivation/certs/Activation/PROD/
+ /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/MobileActivation/certs/Activation/QA/
+ /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/MobileActivation/certs/BAA/PROD/
+ /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/MobileActivation/certs/BAA/QA/
+ /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/MobileActivation/certs/UCRT/PROD/
+ /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/MobileActivation/certs/UCRT/QA/
+ /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/MobileActivation/mobileactivationdMacOS/
+ /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/MobileActivation/shared/
+ /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/libDER/libDER/
+ ACMContextGetExternalForm.cold.1
+ _OBJC_CLASS_$_NSRegularExpression
+ _OUTLINED_FUNCTION_10
+ _OUTLINED_FUNCTION_11
+ _OUTLINED_FUNCTION_12
+ _OUTLINED_FUNCTION_13
+ _OUTLINED_FUNCTION_14
+ _OUTLINED_FUNCTION_15
+ _OUTLINED_FUNCTION_16
+ _OUTLINED_FUNCTION_17
+ _OUTLINED_FUNCTION_18
+ _OUTLINED_FUNCTION_19
+ _OUTLINED_FUNCTION_20
+ _OUTLINED_FUNCTION_21
+ _OUTLINED_FUNCTION_22
+ _OUTLINED_FUNCTION_23
+ _OUTLINED_FUNCTION_24
+ _OUTLINED_FUNCTION_25
+ _OUTLINED_FUNCTION_26
+ _OUTLINED_FUNCTION_27
+ _OUTLINED_FUNCTION_28
+ _OUTLINED_FUNCTION_29
+ _OUTLINED_FUNCTION_30
+ _OUTLINED_FUNCTION_31
+ _OUTLINED_FUNCTION_32
+ _OUTLINED_FUNCTION_33
+ _OUTLINED_FUNCTION_34
+ _OUTLINED_FUNCTION_35
+ _OUTLINED_FUNCTION_36
+ _OUTLINED_FUNCTION_37
+ _OUTLINED_FUNCTION_38
+ _OUTLINED_FUNCTION_39
+ _OUTLINED_FUNCTION_40
+ _OUTLINED_FUNCTION_41
+ _OUTLINED_FUNCTION_42
+ _OUTLINED_FUNCTION_43
+ _OUTLINED_FUNCTION_44
+ _OUTLINED_FUNCTION_45
+ _OUTLINED_FUNCTION_46
+ _OUTLINED_FUNCTION_48
+ _OUTLINED_FUNCTION_49
+ _OUTLINED_FUNCTION_54
+ _OUTLINED_FUNCTION_59
+ _OUTLINED_FUNCTION_6
+ _OUTLINED_FUNCTION_7
+ _OUTLINED_FUNCTION_8
+ _OUTLINED_FUNCTION_9
+ __61-[MobileActivationMacOSDaemon issueUCRT:withCompletionBlock:]_block_invoke_2.444
+ __61-[MobileActivationMacOSDaemon issueUCRT:withCompletionBlock:]_block_invoke_2.446
+ ___block_descriptor_119_e8_32s40s48s56s64s72s80s88s96bs104r_e5_v8?0l
+ ___copy_helper_block_e8_32s40s48s56s64s72s80s88s96b104r
+ ___destroy_helper_block_e8_32s40s48s56s64s72s80s88s96s104r
+ __block_literal_global.369
+ __block_literal_global.401
+ __block_literal_global.409
+ _clientNameSuffixIsValid
+ _createBAAClientName
+ _createUserAgentValue
+ _kMAOptionsBAAClientNameSuffix
+ _merge_dict_cb.cold.1
+ _objc_msgSend$firstMatchInString:options:range:
+ _objc_msgSend$regularExpressionWithPattern:options:error:
+ copyLoggingHandle.cold.1
+ copyMobileActivationSerialQueue.cold.1
+ copyRTCResetSerialQueue.cold.1
+ copySignpostLoggingHandle.cold.1
+ copySplunkQueue.cold.1
+ copySplunkUUIDQueue.cold.1
+ copy_data_ark_directory_path.cold.1
+ copy_dcrt_path.cold.1
+ copy_legacy_dcrt_path.cold.1
+ copy_log_directory_path.cold.1
+ copy_splunk_directory_path.cold.1
+ copy_ucrt_path.cold.1
+ der_key_validate.cold.1
+ der_key_validate.cold.2
+ get_aks_client_connection.cold.1
+ isRunningInDiagnosticsMode.cold.1
+ isRunningInRecovery.cold.1
+ isRunningInRootLaunchdContext.cold.1
+ isSupportedActivationLockClient.cold.2
+ isSupportedDeviceIdentityClient.cold.2
+ isSupportedRecoveryLogClient.cold.1
+ lockcrypto_query_certificate_properties.cold.1
+ updateLogLevelFromKext.cold.1
- /AppleInternal/Library/BuildRoots/2d1fc6ee-e34b-11ef-ba1a-122ba06eff56/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.3.Internal.sdk/usr/local/lib/amd/libDER.a(DER_Decode.o)
- /AppleInternal/Library/BuildRoots/2d1fc6ee-e34b-11ef-ba1a-122ba06eff56/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.3.Internal.sdk/usr/local/lib/libCoreTrust.a(CMS.o)
- /AppleInternal/Library/BuildRoots/2d1fc6ee-e34b-11ef-ba1a-122ba06eff56/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.3.Internal.sdk/usr/local/lib/libCoreTrust.a(CTEvaluate.o)
- /AppleInternal/Library/BuildRoots/2d1fc6ee-e34b-11ef-ba1a-122ba06eff56/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.3.Internal.sdk/usr/local/lib/libCoreTrust.a(CTEvaluateBAA.o)
- /AppleInternal/Library/BuildRoots/2d1fc6ee-e34b-11ef-ba1a-122ba06eff56/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.3.Internal.sdk/usr/local/lib/libCoreTrust.a(CryptoUtils.o)
- /AppleInternal/Library/BuildRoots/2d1fc6ee-e34b-11ef-ba1a-122ba06eff56/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.3.Internal.sdk/usr/local/lib/libCoreTrust.a(DERUtils.o)
- /AppleInternal/Library/BuildRoots/2d1fc6ee-e34b-11ef-ba1a-122ba06eff56/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.3.Internal.sdk/usr/local/lib/libCoreTrust.a(X509Certificate.o)
- /AppleInternal/Library/BuildRoots/2d1fc6ee-e34b-11ef-ba1a-122ba06eff56/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.3.Internal.sdk/usr/local/lib/libCoreTrust.a(X509Chain.o)
- /AppleInternal/Library/BuildRoots/2d1fc6ee-e34b-11ef-ba1a-122ba06eff56/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.3.Internal.sdk/usr/local/lib/libCoreTrust.a(X509Policy.o)
- /AppleInternal/Library/BuildRoots/2d1fc6ee-e34b-11ef-ba1a-122ba06eff56/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.3.Internal.sdk/usr/local/lib/libaks.a(acl_keys.o)
- /AppleInternal/Library/BuildRoots/2d1fc6ee-e34b-11ef-ba1a-122ba06eff56/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.3.Internal.sdk/usr/local/lib/libaks.a(der_utils.o)
- /AppleInternal/Library/BuildRoots/2d1fc6ee-e34b-11ef-ba1a-122ba06eff56/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.3.Internal.sdk/usr/local/lib/libaks.a(firebloom_hacks.o)
- /AppleInternal/Library/BuildRoots/2d1fc6ee-e34b-11ef-ba1a-122ba06eff56/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.3.Internal.sdk/usr/local/lib/libaks.a(libaks_client.o)
- /AppleInternal/Library/BuildRoots/2d1fc6ee-e34b-11ef-ba1a-122ba06eff56/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.3.Internal.sdk/usr/local/lib/libaks.a(libaks_internal.o)
- /AppleInternal/Library/BuildRoots/2d1fc6ee-e34b-11ef-ba1a-122ba06eff56/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.3.Internal.sdk/usr/local/lib/libaks.a(libaks_ref_key.o)
- /AppleInternal/Library/BuildRoots/2d1fc6ee-e34b-11ef-ba1a-122ba06eff56/Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationdMacOS.build/Objects-normal/arm64e/BAAASMFiOSRootCAPEM.o
- /AppleInternal/Library/BuildRoots/2d1fc6ee-e34b-11ef-ba1a-122ba06eff56/Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationdMacOS.build/Objects-normal/arm64e/BAAMFiRootCAPEM.o
- /AppleInternal/Library/BuildRoots/2d1fc6ee-e34b-11ef-ba1a-122ba06eff56/Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationdMacOS.build/Objects-normal/arm64e/BAASCRTRootCAPEM.o
- /AppleInternal/Library/BuildRoots/2d1fc6ee-e34b-11ef-ba1a-122ba06eff56/Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationdMacOS.build/Objects-normal/arm64e/BAAUCRTRootCAPEM.o
- /AppleInternal/Library/BuildRoots/2d1fc6ee-e34b-11ef-ba1a-122ba06eff56/Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationdMacOS.build/Objects-normal/arm64e/BAAVMRootCAPEM.o
- /AppleInternal/Library/BuildRoots/2d1fc6ee-e34b-11ef-ba1a-122ba06eff56/Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationdMacOS.build/Objects-normal/arm64e/FactoryUCRTRootCAPEM.o
- /AppleInternal/Library/BuildRoots/2d1fc6ee-e34b-11ef-ba1a-122ba06eff56/Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationdMacOS.build/Objects-normal/arm64e/GestaltHlpr.o
- /AppleInternal/Library/BuildRoots/2d1fc6ee-e34b-11ef-ba1a-122ba06eff56/Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationdMacOS.build/Objects-normal/arm64e/MobileActivationError.o
- /AppleInternal/Library/BuildRoots/2d1fc6ee-e34b-11ef-ba1a-122ba06eff56/Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationdMacOS.build/Objects-normal/arm64e/MobileActivationErrorPrivate.o
- /AppleInternal/Library/BuildRoots/2d1fc6ee-e34b-11ef-ba1a-122ba06eff56/Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationdMacOS.build/Objects-normal/arm64e/NSDateFormatter+MobileActivation.o
- /AppleInternal/Library/BuildRoots/2d1fc6ee-e34b-11ef-ba1a-122ba06eff56/Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationdMacOS.build/Objects-normal/arm64e/NetworkProvider.o
- /AppleInternal/Library/BuildRoots/2d1fc6ee-e34b-11ef-ba1a-122ba06eff56/Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationdMacOS.build/Objects-normal/arm64e/QABAAASMFiOSRootCAPEM.o
- /AppleInternal/Library/BuildRoots/2d1fc6ee-e34b-11ef-ba1a-122ba06eff56/Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationdMacOS.build/Objects-normal/arm64e/QABAAMFiRootCAPEM.o
- /AppleInternal/Library/BuildRoots/2d1fc6ee-e34b-11ef-ba1a-122ba06eff56/Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationdMacOS.build/Objects-normal/arm64e/QABAASCRTRootCAPEM.o
- /AppleInternal/Library/BuildRoots/2d1fc6ee-e34b-11ef-ba1a-122ba06eff56/Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationdMacOS.build/Objects-normal/arm64e/QABAAUCRTRootCAPEM.o
- /AppleInternal/Library/BuildRoots/2d1fc6ee-e34b-11ef-ba1a-122ba06eff56/Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationdMacOS.build/Objects-normal/arm64e/QABAAVMRootCAPEM.o
- /AppleInternal/Library/BuildRoots/2d1fc6ee-e34b-11ef-ba1a-122ba06eff56/Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationdMacOS.build/Objects-normal/arm64e/QAIphoneActivationPEM.o
- /AppleInternal/Library/BuildRoots/2d1fc6ee-e34b-11ef-ba1a-122ba06eff56/Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationdMacOS.build/Objects-normal/arm64e/QAIphoneDeviceCAPEM.o
- /AppleInternal/Library/BuildRoots/2d1fc6ee-e34b-11ef-ba1a-122ba06eff56/Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationdMacOS.build/Objects-normal/arm64e/QAUCRTRootCAP384PEM.o
- /AppleInternal/Library/BuildRoots/2d1fc6ee-e34b-11ef-ba1a-122ba06eff56/Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationdMacOS.build/Objects-normal/arm64e/QAUCRTRootCAPEM.o
- /AppleInternal/Library/BuildRoots/2d1fc6ee-e34b-11ef-ba1a-122ba06eff56/Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationdMacOS.build/Objects-normal/arm64e/QAUCRTSubCAPEM.o
- /AppleInternal/Library/BuildRoots/2d1fc6ee-e34b-11ef-ba1a-122ba06eff56/Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationdMacOS.build/Objects-normal/arm64e/RaptorActivationPEM.o
- /AppleInternal/Library/BuildRoots/2d1fc6ee-e34b-11ef-ba1a-122ba06eff56/Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationdMacOS.build/Objects-normal/arm64e/RaptorDeviceCAPEM.o
- /AppleInternal/Library/BuildRoots/2d1fc6ee-e34b-11ef-ba1a-122ba06eff56/Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationdMacOS.build/Objects-normal/arm64e/UCRTRootCAPEM.o
- /AppleInternal/Library/BuildRoots/2d1fc6ee-e34b-11ef-ba1a-122ba06eff56/Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationdMacOS.build/Objects-normal/arm64e/UCRTSubCAPEM.o
- /AppleInternal/Library/BuildRoots/2d1fc6ee-e34b-11ef-ba1a-122ba06eff56/Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationdMacOS.build/Objects-normal/arm64e/activationSupportMacOS.o
- /AppleInternal/Library/BuildRoots/2d1fc6ee-e34b-11ef-ba1a-122ba06eff56/Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationdMacOS.build/Objects-normal/arm64e/activation_support_shared.o
- /AppleInternal/Library/BuildRoots/2d1fc6ee-e34b-11ef-ba1a-122ba06eff56/Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationdMacOS.build/Objects-normal/arm64e/authkit.o
- /AppleInternal/Library/BuildRoots/2d1fc6ee-e34b-11ef-ba1a-122ba06eff56/Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationdMacOS.build/Objects-normal/arm64e/baa.o
- /AppleInternal/Library/BuildRoots/2d1fc6ee-e34b-11ef-ba1a-122ba06eff56/Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationdMacOS.build/Objects-normal/arm64e/baa_oids.o
- /AppleInternal/Library/BuildRoots/2d1fc6ee-e34b-11ef-ba1a-122ba06eff56/Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationdMacOS.build/Objects-normal/arm64e/bridge.o
- /AppleInternal/Library/BuildRoots/2d1fc6ee-e34b-11ef-ba1a-122ba06eff56/Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationdMacOS.build/Objects-normal/arm64e/bridge_support.o
- /AppleInternal/Library/BuildRoots/2d1fc6ee-e34b-11ef-ba1a-122ba06eff56/Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationdMacOS.build/Objects-normal/arm64e/common.o
- /AppleInternal/Library/BuildRoots/2d1fc6ee-e34b-11ef-ba1a-122ba06eff56/Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationdMacOS.build/Objects-normal/arm64e/coretrust.o
- /AppleInternal/Library/BuildRoots/2d1fc6ee-e34b-11ef-ba1a-122ba06eff56/Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationdMacOS.build/Objects-normal/arm64e/crypto.o
- /AppleInternal/Library/BuildRoots/2d1fc6ee-e34b-11ef-ba1a-122ba06eff56/Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationdMacOS.build/Objects-normal/arm64e/data_ark.o
- /AppleInternal/Library/BuildRoots/2d1fc6ee-e34b-11ef-ba1a-122ba06eff56/Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationdMacOS.build/Objects-normal/arm64e/device_tree.o
- /AppleInternal/Library/BuildRoots/2d1fc6ee-e34b-11ef-ba1a-122ba06eff56/Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationdMacOS.build/Objects-normal/arm64e/dsp.o
- /AppleInternal/Library/BuildRoots/2d1fc6ee-e34b-11ef-ba1a-122ba06eff56/Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationdMacOS.build/Objects-normal/arm64e/findmy.o
- /AppleInternal/Library/BuildRoots/2d1fc6ee-e34b-11ef-ba1a-122ba06eff56/Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationdMacOS.build/Objects-normal/arm64e/iPhoneActivationPEM.o
- /AppleInternal/Library/BuildRoots/2d1fc6ee-e34b-11ef-ba1a-122ba06eff56/Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationdMacOS.build/Objects-normal/arm64e/iPhoneCAPEM.o
- /AppleInternal/Library/BuildRoots/2d1fc6ee-e34b-11ef-ba1a-122ba06eff56/Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationdMacOS.build/Objects-normal/arm64e/iPhoneDeviceCAPEM.o
- /AppleInternal/Library/BuildRoots/2d1fc6ee-e34b-11ef-ba1a-122ba06eff56/Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationdMacOS.build/Objects-normal/arm64e/identity_support.o
- /AppleInternal/Library/BuildRoots/2d1fc6ee-e34b-11ef-ba1a-122ba06eff56/Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationdMacOS.build/Objects-normal/arm64e/keylist.o
- /AppleInternal/Library/BuildRoots/2d1fc6ee-e34b-11ef-ba1a-122ba06eff56/Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationdMacOS.build/Objects-normal/arm64e/libaks_keymanagement.o
- /AppleInternal/Library/BuildRoots/2d1fc6ee-e34b-11ef-ba1a-122ba06eff56/Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationdMacOS.build/Objects-normal/arm64e/log.o
- /AppleInternal/Library/BuildRoots/2d1fc6ee-e34b-11ef-ba1a-122ba06eff56/Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationdMacOS.build/Objects-normal/arm64e/main.o
- /AppleInternal/Library/BuildRoots/2d1fc6ee-e34b-11ef-ba1a-122ba06eff56/Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationdMacOS.build/Objects-normal/arm64e/mobileactivationdMacOS.o
- /AppleInternal/Library/BuildRoots/2d1fc6ee-e34b-11ef-ba1a-122ba06eff56/Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationdMacOS.build/Objects-normal/arm64e/msu_data_accessor.o
- /AppleInternal/Library/BuildRoots/2d1fc6ee-e34b-11ef-ba1a-122ba06eff56/Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationdMacOS.build/Objects-normal/arm64e/path_support_shared.o
- /AppleInternal/Library/BuildRoots/2d1fc6ee-e34b-11ef-ba1a-122ba06eff56/Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationdMacOS.build/Objects-normal/arm64e/requests.o
- /AppleInternal/Library/BuildRoots/2d1fc6ee-e34b-11ef-ba1a-122ba06eff56/Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationdMacOS.build/Objects-normal/arm64e/requests_network.o
- /AppleInternal/Library/BuildRoots/2d1fc6ee-e34b-11ef-ba1a-122ba06eff56/Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationdMacOS.build/Objects-normal/arm64e/requests_support.o
- /AppleInternal/Library/BuildRoots/2d1fc6ee-e34b-11ef-ba1a-122ba06eff56/Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationdMacOS.build/Objects-normal/arm64e/root_certificates.o
- /AppleInternal/Library/BuildRoots/2d1fc6ee-e34b-11ef-ba1a-122ba06eff56/Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationdMacOS.build/Objects-normal/arm64e/security_keymanagement.o
- /AppleInternal/Library/BuildRoots/2d1fc6ee-e34b-11ef-ba1a-122ba06eff56/Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationdMacOS.build/Objects-normal/arm64e/signpost.o
- /AppleInternal/Library/BuildRoots/2d1fc6ee-e34b-11ef-ba1a-122ba06eff56/Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationdMacOS.build/Objects-normal/arm64e/splunk_logging.o
- /AppleInternal/Library/BuildRoots/2d1fc6ee-e34b-11ef-ba1a-122ba06eff56/Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationdMacOS.build/Objects-normal/arm64e/vm_host_support.o
- /AppleInternal/Library/BuildRoots/2d1fc6ee-e34b-11ef-ba1a-122ba06eff56/Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationdMacOS.build/Objects-normal/arm64e/vm_libavp.o
- /AppleInternal/Library/BuildRoots/2d1fc6ee-e34b-11ef-ba1a-122ba06eff56/Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationdMacOS.build/Objects-normal/arm64e/vm_support.o
- /AppleInternal/Library/BuildRoots/2d1fc6ee-e34b-11ef-ba1a-122ba06eff56/Library/Caches/com.apple.xbs/Sources/MobileActivation/certs/Activation/PROD/
- /AppleInternal/Library/BuildRoots/2d1fc6ee-e34b-11ef-ba1a-122ba06eff56/Library/Caches/com.apple.xbs/Sources/MobileActivation/certs/Activation/QA/
- /AppleInternal/Library/BuildRoots/2d1fc6ee-e34b-11ef-ba1a-122ba06eff56/Library/Caches/com.apple.xbs/Sources/MobileActivation/certs/BAA/PROD/
- /AppleInternal/Library/BuildRoots/2d1fc6ee-e34b-11ef-ba1a-122ba06eff56/Library/Caches/com.apple.xbs/Sources/MobileActivation/certs/BAA/QA/
- /AppleInternal/Library/BuildRoots/2d1fc6ee-e34b-11ef-ba1a-122ba06eff56/Library/Caches/com.apple.xbs/Sources/MobileActivation/certs/UCRT/PROD/
- /AppleInternal/Library/BuildRoots/2d1fc6ee-e34b-11ef-ba1a-122ba06eff56/Library/Caches/com.apple.xbs/Sources/MobileActivation/certs/UCRT/QA/
- /AppleInternal/Library/BuildRoots/2d1fc6ee-e34b-11ef-ba1a-122ba06eff56/Library/Caches/com.apple.xbs/Sources/MobileActivation/mobileactivationdMacOS/
- /AppleInternal/Library/BuildRoots/2d1fc6ee-e34b-11ef-ba1a-122ba06eff56/Library/Caches/com.apple.xbs/Sources/MobileActivation/shared/
- /AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleKeyStore_libs/
- /AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/CoreTrust/Source/
- /AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/libDER/libDER/
- __61-[MobileActivationMacOSDaemon issueUCRT:withCompletionBlock:]_block_invoke_2.441
- __61-[MobileActivationMacOSDaemon issueUCRT:withCompletionBlock:]_block_invoke_2.443
- ___block_descriptor_111_e8_32s40s48s56s64s72s80s88bs96r_e5_v8?0l
- ___copy_helper_block_e8_32s40s48s56s64s72s80s88b96r
- ___destroy_helper_block_e8_32s40s48s56s64s72s80s88s96r
- __block_literal_global.366
- __block_literal_global.398
- __block_literal_global.406
- __isNullOrEqualMem2
CStrings:
+ "#%@"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/ACMLib/ACMLib.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/CommonUtil.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/LibCall.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/LibCallBlock.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/LibSerialization.c"
+ "1017.100.16"
+ "Absinthe/2.0 macOS Device Activator (MobileActivation-1017.100.16 built on Mar  7 2025 at 21:53:03)"
+ "BAAClientNameSuffix"
+ "Failed to create regex."
+ "Invalid type for option %@"
+ "^[A-Za-z0-9_-]{0,64}$"
+ "clientNameSuffixIsValid"
+ "firstMatchInString:options:range:"
+ "imagent"
+ "macOS Device Activator (MobileActivation-1017.100.16)"
+ "regularExpressionWithPattern:options:error:"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/ACMLib/ACMLib.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/CommonUtil.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/LibCall.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/LibCallBlock.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/LibSerialization.c"
- "1015.81.2"
- "Absinthe/2.0 macOS Device Activator (MobileActivation-1015.81.2 built on Mar  4 2025 at 22:54:05)"
- "macOS Device Activator (MobileActivation-1015.81.2)"

```
