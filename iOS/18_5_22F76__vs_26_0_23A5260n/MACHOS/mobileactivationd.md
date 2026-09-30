## mobileactivationd

> `/usr/libexec/mobileactivationd`

```diff

-1017.120.3.0.0
-  __TEXT.__text: 0x1fdd74
-  __TEXT.__auth_stubs: 0x10a0
+1055.0.0.0.0
+  __TEXT.__text: 0x2c17fc
+  __TEXT.__auth_stubs: 0x10f0
   __TEXT.__objc_stubs: 0x2f20
-  __TEXT.__objc_methlist: 0x1084
-  __TEXT.__const: 0x468c1
-  __TEXT.__cstring: 0xd93b
-  __TEXT.__objc_methname: 0x3d4e
-  __TEXT.__oslogstring: 0xe5a
+  __TEXT.__objc_methlist: 0x109c
+  __TEXT.__const: 0x5f120
+  __TEXT.__cstring: 0xdd69
+  __TEXT.__objc_methname: 0x3d7b
+  __TEXT.__oslogstring: 0xed6
   __TEXT.__objc_classname: 0x1b4
   __TEXT.__objc_methtype: 0x102a
   __TEXT.__gcc_except_tab: 0x1998
   __TEXT.__dlopen_cstrs: 0x24c
   __TEXT.__ustring: 0x4
-  __TEXT.__unwind_info: 0x1170
-  __TEXT.__eh_frame: 0x10f0
-  __DATA_CONST.__auth_got: 0x860
-  __DATA_CONST.__got: 0x460
+  __TEXT.__unwind_info: 0x1028
+  __TEXT.__eh_frame: 0xa0
+  __DATA_CONST.__auth_got: 0x888
+  __DATA_CONST.__got: 0x468
   __DATA_CONST.__auth_ptr: 0x70
-  __DATA_CONST.__const: 0xe470
-  __DATA_CONST.__cfstring: 0xc1a0
+  __DATA_CONST.__const: 0x19e28
+  __DATA_CONST.__cfstring: 0xc420
   __DATA_CONST.__objc_classlist: 0x50
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x48

   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x40
   __DATA_CONST.__objc_intobj: 0x258
-  __DATA_CONST.__objc_arraydata: 0x468
+  __DATA_CONST.__objc_arraydata: 0x4a0
   __DATA_CONST.__objc_arrayobj: 0x90
-  __DATA.__objc_const: 0x1850
-  __DATA.__objc_selrefs: 0xfe0
+  __DATA.__objc_const: 0x1858
+  __DATA.__objc_selrefs: 0xfe8
   __DATA.__objc_ivar: 0xf4
   __DATA.__objc_data: 0x320
-  __DATA.__data: 0x1210
-  __DATA.__bss: 0x510
-  __DATA.__common: 0xa10
+  __DATA.__data: 0x1348
+  __DATA.__bss: 0x524
+  __DATA.__common: 0xa40
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreTelephony.framework/CoreTelephony

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/liblockdown.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 99FA35E5-EB2C-3234-A572-1E63DC01E528
-  Functions: 1389
-  Symbols:   9660
-  CStrings:  4366
+  UUID: BAEE9858-7165-3962-8F7E-8497DD987A19
+  Functions: 1477
+  Symbols:   10283
+  CStrings:  4429
 
Symbols:
+ -[MobileActivationDaemon copyRegionDataForGestaltWithCompletionBlock:]
+ /AppleInternal/Library/BuildRoots/4~B2AEugAUGjMlI6UqkPScJY2sX7EGK06TFUnw4eU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/lib/amd/libDER.a(DER_Decode.o)
+ /AppleInternal/Library/BuildRoots/4~B2AEugAUGjMlI6UqkPScJY2sX7EGK06TFUnw4eU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/lib/libCoreTrust.a(AppleAnchors.o)
+ /AppleInternal/Library/BuildRoots/4~B2AEugAUGjMlI6UqkPScJY2sX7EGK06TFUnw4eU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/lib/libCoreTrust.a(CMS.o)
+ /AppleInternal/Library/BuildRoots/4~B2AEugAUGjMlI6UqkPScJY2sX7EGK06TFUnw4eU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/lib/libCoreTrust.a(CTEvaluate.o)
+ /AppleInternal/Library/BuildRoots/4~B2AEugAUGjMlI6UqkPScJY2sX7EGK06TFUnw4eU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/lib/libCoreTrust.a(CTEvaluateBAA.o)
+ /AppleInternal/Library/BuildRoots/4~B2AEugAUGjMlI6UqkPScJY2sX7EGK06TFUnw4eU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/lib/libCoreTrust.a(CryptoUtils.o)
+ /AppleInternal/Library/BuildRoots/4~B2AEugAUGjMlI6UqkPScJY2sX7EGK06TFUnw4eU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/lib/libCoreTrust.a(DERUtils.o)
+ /AppleInternal/Library/BuildRoots/4~B2AEugAUGjMlI6UqkPScJY2sX7EGK06TFUnw4eU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/lib/libCoreTrust.a(X509Certificate.o)
+ /AppleInternal/Library/BuildRoots/4~B2AEugAUGjMlI6UqkPScJY2sX7EGK06TFUnw4eU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/lib/libCoreTrust.a(X509Chain.o)
+ /AppleInternal/Library/BuildRoots/4~B2AEugAUGjMlI6UqkPScJY2sX7EGK06TFUnw4eU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/lib/libCoreTrust.a(X509Policy.o)
+ /AppleInternal/Library/BuildRoots/4~B2AEugAUGjMlI6UqkPScJY2sX7EGK06TFUnw4eU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/lib/libCoreTrust.a(iCDPAnchors.o)
+ /AppleInternal/Library/BuildRoots/4~B2AEugAUGjMlI6UqkPScJY2sX7EGK06TFUnw4eU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/lib/libaks.a(acl_keys.o)
+ /AppleInternal/Library/BuildRoots/4~B2AEugAUGjMlI6UqkPScJY2sX7EGK06TFUnw4eU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/lib/libaks.a(aks_pack.o)
+ /AppleInternal/Library/BuildRoots/4~B2AEugAUGjMlI6UqkPScJY2sX7EGK06TFUnw4eU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/lib/libaks.a(der_utils.o)
+ /AppleInternal/Library/BuildRoots/4~B2AEugAUGjMlI6UqkPScJY2sX7EGK06TFUnw4eU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/lib/libaks.a(firebloom_hacks.o)
+ /AppleInternal/Library/BuildRoots/4~B2AEugAUGjMlI6UqkPScJY2sX7EGK06TFUnw4eU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/lib/libaks.a(libaks_client.o)
+ /AppleInternal/Library/BuildRoots/4~B2AEugAUGjMlI6UqkPScJY2sX7EGK06TFUnw4eU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/lib/libaks.a(libaks_internal.o)
+ /AppleInternal/Library/BuildRoots/4~B2AEugAUGjMlI6UqkPScJY2sX7EGK06TFUnw4eU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/lib/libaks.a(libaks_ref_key.o)
+ /Library/Caches/com.apple.xbs/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationd.build/Objects-normal/arm64e/regioncode.o
+ AppleAnchors.c
+ GCC_except_table115
+ GCC_except_table70
+ GCC_except_table81
+ GCC_except_table88
+ GCC_except_table95
+ _ACRTRoot_public_key
+ _AohBfJYWOS6
+ _ApplePlatformBackportECCRootCAG1
+ _ApplePlatformBackportECCRootCAG1PublicKey
+ _ApplePlatformBackportECCRootCAG1SKID
+ _ApplePlatformBackportECCRootCAG1SPKI
+ _ApplePlatformBackportECCRootCAG1_public_key
+ _ApplePlatformBackportECCRootCAG1_skid
+ _ApplePlatformBackportECCRootCAG1_spki
+ _ApplePlatformBackportRSARootCAG1
+ _ApplePlatformBackportRSARootCAG1PublicKey
+ _ApplePlatformBackportRSARootCAG1SKID
+ _ApplePlatformBackportRSARootCAG1SPKI
+ _ApplePlatformBackportRSARootCAG1_public_key
+ _ApplePlatformBackportRSARootCAG1_skid
+ _ApplePlatformBackportRSARootCAG1_spki
+ _ApplePlatformBootstrapECCRootCAG1
+ _ApplePlatformBootstrapECCRootCAG1PublicKey
+ _ApplePlatformBootstrapECCRootCAG1SKID
+ _ApplePlatformBootstrapECCRootCAG1SPKI
+ _ApplePlatformBootstrapECCRootCAG1_public_key
+ _ApplePlatformBootstrapECCRootCAG1_skid
+ _ApplePlatformBootstrapECCRootCAG1_spki
+ _ApplePlatformCodeSigningECCRootCAG1
+ _ApplePlatformCodeSigningECCRootCAG1PublicKey
+ _ApplePlatformCodeSigningECCRootCAG1SKID
+ _ApplePlatformCodeSigningECCRootCAG1SPKI
+ _ApplePlatformCodeSigningECCRootCAG1_public_key
+ _ApplePlatformCodeSigningECCRootCAG1_skid
+ _ApplePlatformCodeSigningECCRootCAG1_spki
+ _ApplePlatformCodeSigningRSARootCAG1
+ _ApplePlatformCodeSigningRSARootCAG1PublicKey
+ _ApplePlatformCodeSigningRSARootCAG1SKID
+ _ApplePlatformCodeSigningRSARootCAG1SPKI
+ _ApplePlatformCodeSigningRSARootCAG1_public_key
+ _ApplePlatformCodeSigningRSARootCAG1_skid
+ _ApplePlatformCodeSigningRSARootCAG1_spki
+ _ApplePlatformDeveloperECCRootCAG1
+ _ApplePlatformDeveloperECCRootCAG1PublicKey
+ _ApplePlatformDeveloperECCRootCAG1SKID
+ _ApplePlatformDeveloperECCRootCAG1SPKI
+ _ApplePlatformDeveloperECCRootCAG1_public_key
+ _ApplePlatformDeveloperECCRootCAG1_skid
+ _ApplePlatformDeveloperECCRootCAG1_spki
+ _ApplePlatformDeveloperRSARootCAG1
+ _ApplePlatformDeveloperRSARootCAG1PublicKey
+ _ApplePlatformDeveloperRSARootCAG1SKID
+ _ApplePlatformDeveloperRSARootCAG1SPKI
+ _ApplePlatformDeveloperRSARootCAG1_public_key
+ _ApplePlatformDeveloperRSARootCAG1_skid
+ _ApplePlatformDeveloperRSARootCAG1_spki
+ _ApplePlatformECCRootCAG1
+ _ApplePlatformECCRootCAG1PublicKey
+ _ApplePlatformECCRootCAG1SKID
+ _ApplePlatformECCRootCAG1SPKI
+ _ApplePlatformECCRootCAG1_public_key
+ _ApplePlatformECCRootCAG1_skid
+ _ApplePlatformECCRootCAG1_spki
+ _ApplePlatformMultipurposeECCRootCAG1
+ _ApplePlatformMultipurposeECCRootCAG1PublicKey
+ _ApplePlatformMultipurposeECCRootCAG1SKID
+ _ApplePlatformMultipurposeECCRootCAG1SPKI
+ _ApplePlatformMultipurposeECCRootCAG1_public_key
+ _ApplePlatformMultipurposeECCRootCAG1_skid
+ _ApplePlatformMultipurposeECCRootCAG1_spki
+ _ApplePlatformMultipurposeRSARootCAG1
+ _ApplePlatformMultipurposeRSARootCAG1PublicKey
+ _ApplePlatformMultipurposeRSARootCAG1SKID
+ _ApplePlatformMultipurposeRSARootCAG1SPKI
+ _ApplePlatformMultipurposeRSARootCAG1_public_key
+ _ApplePlatformMultipurposeRSARootCAG1_skid
+ _ApplePlatformMultipurposeRSARootCAG1_spki
+ _ApplePlatformRSARootCAG1
+ _ApplePlatformRSARootCAG1PublicKey
+ _ApplePlatformRSARootCAG1SKID
+ _ApplePlatformRSARootCAG1SPKI
+ _ApplePlatformRSARootCAG1_public_key
+ _ApplePlatformRSARootCAG1_skid
+ _ApplePlatformRSARootCAG1_spki
+ _ApplePlatformTLSECCRootCAG1
+ _ApplePlatformTLSECCRootCAG1PublicKey
+ _ApplePlatformTLSECCRootCAG1SKID
+ _ApplePlatformTLSECCRootCAG1SPKI
+ _ApplePlatformTLSECCRootCAG1_public_key
+ _ApplePlatformTLSECCRootCAG1_skid
+ _ApplePlatformTLSECCRootCAG1_spki
+ _ApplePlatformTLSRSARootCAG1
+ _ApplePlatformTLSRSARootCAG1PublicKey
+ _ApplePlatformTLSRSARootCAG1SKID
+ _ApplePlatformTLSRSARootCAG1SPKI
+ _ApplePlatformTLSRSARootCAG1_public_key
+ _ApplePlatformTLSRSARootCAG1_skid
+ _ApplePlatformTLSRSARootCAG1_spki
+ _AppleRootCAG2SPKI
+ _AppleRootCAG2_skid
+ _AppleRootCAG2_spki
+ _AppleRootCAG3SPKI
+ _AppleRootCAG3_skid
+ _AppleRootCAG3_spki
+ _AppleRootCA_skid
+ _AppleRootCA_spki
+ _AppleRootFlags
+ _AppleRootSPKIs
+ _BASepAppRoot_public_key
+ _BASepAppRoot_skid
+ _BASepAppRoot_spki
+ _BASystemRoot_public_key
+ _BASystemRoot_skid
+ _BASystemRoot_spki
+ _BAUserRoot_public_key
+ _BAUserRoot_skid
+ _BAUserRoot_spki
+ _BlockedYonkers_spki
+ _CFUnnB0JdUjJ5CNJMkDS
+ _COUNTRY_TO_REGION
+ _CTEvaluateICDPFederation
+ _CTGetICDPFederationType
+ _CdfajkOy32ff
+ _CjHbHx
+ _DERParseInteger64Signed
+ _DERParseIntegerSigned
+ _DeKxOzK1QT
+ _DevICDPFederationRoot152PublicKey
+ _DevICDPFederationRoot152SKID
+ _DevICDPFederationRoot152_public_key
+ _DevICDPFederationRoot152_skid
+ _DevICDPFederationRoot4PublicKey
+ _DevICDPFederationRoot4SKID
+ _DevICDPFederationRoot4_public_key
+ _DevICDPFederationRoot4_skid
+ _DnfHbSOPOb3
+ _Ehn34khqq1jgEJw
+ _F21B5Tc5GK6
+ _FIUPqPyosF
+ _FKsdr5
+ _Fc3vhtJDvr
+ _Fhjfdethrte87erhy4
+ _G7b066W
+ _HN0R
+ _Hbz0lOyjnO0
+ _Hz73b
+ _ICDPFederationRoot101PublicKey
+ _ICDPFederationRoot101SKID
+ _ICDPFederationRoot101_public_key
+ _ICDPFederationRoot101_skid
+ _ICDPFederationRoot102PublicKey
+ _ICDPFederationRoot102SKID
+ _ICDPFederationRoot102_public_key
+ _ICDPFederationRoot102_skid
+ _ICDPFederationRoot103PublicKey
+ _ICDPFederationRoot103SKID
+ _ICDPFederationRoot103_public_key
+ _ICDPFederationRoot103_skid
+ _ICDPFederationRoot310PublicKey
+ _ICDPFederationRoot310SKID
+ _ICDPFederationRoot310_public_key
+ _ICDPFederationRoot310_skid
+ _ICDPFederationRoot500PublicKey
+ _ICDPFederationRoot500SKID
+ _ICDPFederationRoot500_public_key
+ _ICDPFederationRoot500_skid
+ _IPaI1oem5iL
+ _ImNUOAOCCj1zIAp6X14h
+ _J3NocDTIn
+ _JRiKWV
+ _LGokLiStr
+ _LLb3qVEd
+ _LainiFYJT9auDqhZYWzW
+ _LxkN2VWE1TGfu
+ _MAyZqXcneaiE3LtQUHx
+ _MFi4RootSPKI
+ _MFi4Root_public_key
+ _MFi4Root_skid
+ _MFi4Root_spki
+ _MaYVT0G
+ _Mib5yocT
+ _MpmZulZW
+ _Mt76Vq80ux
+ _MyFblh3Z
+ _NOAHabXy
+ _NQ7ggq70Owbvqj8qbExsJ5Hw
+ _NROcmM
+ _NY6eB6
+ _NjiEJ7prRY3
+ _NnzznRTkqBtQzU
+ _NuRl2rYpg6zLtnsguhi3
+ _OUTLINED_FUNCTION_18
+ _OUTLINED_FUNCTION_31
+ _OUTLINED_FUNCTION_32
+ _OUTLINED_FUNCTION_33
+ _OUTLINED_FUNCTION_41
+ _OflR7BMjGok3A7mYQFt9
+ _OlrF
+ _OowSGu
+ _PIc2v4FsmbHb6FcVO9Fu
+ _PhUojZmspd
+ _PjPfaWZz
+ _Pwjgsa92as0
+ _QgPp5PNq
+ _RbFpir
+ _RpUSQN
+ _S12yWPyxCU
+ _SEKProdRoot_public_key
+ _SEKProdRoot_skid
+ _SEKTestRoot_public_key
+ _SEKTestRoot_skid
+ _T40gmCiYgO7uIqkoes4oO6isuYo
+ _TBGzuU3p5n1n
+ _TestApplePlatformBackportECCRootCAG1
+ _TestApplePlatformBackportECCRootCAG1PublicKey
+ _TestApplePlatformBackportECCRootCAG1SKID
+ _TestApplePlatformBackportECCRootCAG1SPKI
+ _TestApplePlatformBackportECCRootCAG1_public_key
+ _TestApplePlatformBackportECCRootCAG1_skid
+ _TestApplePlatformBackportECCRootCAG1_spki
+ _TestApplePlatformBackportRSARootCAG1
+ _TestApplePlatformBackportRSARootCAG1PublicKey
+ _TestApplePlatformBackportRSARootCAG1SKID
+ _TestApplePlatformBackportRSARootCAG1SPKI
+ _TestApplePlatformBackportRSARootCAG1_public_key
+ _TestApplePlatformBackportRSARootCAG1_skid
+ _TestApplePlatformBackportRSARootCAG1_spki
+ _TestApplePlatformBootstrapECCRootCAG1
+ _TestApplePlatformBootstrapECCRootCAG1PublicKey
+ _TestApplePlatformBootstrapECCRootCAG1SKID
+ _TestApplePlatformBootstrapECCRootCAG1SPKI
+ _TestApplePlatformBootstrapECCRootCAG1_public_key
+ _TestApplePlatformBootstrapECCRootCAG1_skid
+ _TestApplePlatformBootstrapECCRootCAG1_spki
+ _TestApplePlatformCodeSigningECCRootCAG1
+ _TestApplePlatformCodeSigningECCRootCAG1PublicKey
+ _TestApplePlatformCodeSigningECCRootCAG1SKID
+ _TestApplePlatformCodeSigningECCRootCAG1SPKI
+ _TestApplePlatformCodeSigningECCRootCAG1_public_key
+ _TestApplePlatformCodeSigningECCRootCAG1_skid
+ _TestApplePlatformCodeSigningECCRootCAG1_spki
+ _TestApplePlatformCodeSigningRSARootCAG1
+ _TestApplePlatformCodeSigningRSARootCAG1PublicKey
+ _TestApplePlatformCodeSigningRSARootCAG1SKID
+ _TestApplePlatformCodeSigningRSARootCAG1SPKI
+ _TestApplePlatformCodeSigningRSARootCAG1_public_key
+ _TestApplePlatformCodeSigningRSARootCAG1_skid
+ _TestApplePlatformCodeSigningRSARootCAG1_spki
+ _TestApplePlatformDeveloperECCRootCAG1
+ _TestApplePlatformDeveloperECCRootCAG1PublicKey
+ _TestApplePlatformDeveloperECCRootCAG1SKID
+ _TestApplePlatformDeveloperECCRootCAG1SPKI
+ _TestApplePlatformDeveloperECCRootCAG1_public_key
+ _TestApplePlatformDeveloperECCRootCAG1_skid
+ _TestApplePlatformDeveloperECCRootCAG1_spki
+ _TestApplePlatformDeveloperRSARootCAG1
+ _TestApplePlatformDeveloperRSARootCAG1PublicKey
+ _TestApplePlatformDeveloperRSARootCAG1SKID
+ _TestApplePlatformDeveloperRSARootCAG1SPKI
+ _TestApplePlatformDeveloperRSARootCAG1_public_key
+ _TestApplePlatformDeveloperRSARootCAG1_skid
+ _TestApplePlatformDeveloperRSARootCAG1_spki
+ _TestApplePlatformECCRootCAG1
+ _TestApplePlatformECCRootCAG1PublicKey
+ _TestApplePlatformECCRootCAG1SKID
+ _TestApplePlatformECCRootCAG1SPKI
+ _TestApplePlatformECCRootCAG1_public_key
+ _TestApplePlatformECCRootCAG1_skid
+ _TestApplePlatformECCRootCAG1_spki
+ _TestApplePlatformMultipurposeECCRootCAG1
+ _TestApplePlatformMultipurposeECCRootCAG1PublicKey
+ _TestApplePlatformMultipurposeECCRootCAG1SKID
+ _TestApplePlatformMultipurposeECCRootCAG1SPKI
+ _TestApplePlatformMultipurposeECCRootCAG1_public_key
+ _TestApplePlatformMultipurposeECCRootCAG1_skid
+ _TestApplePlatformMultipurposeECCRootCAG1_spki
+ _TestApplePlatformMultipurposeRSARootCAG1
+ _TestApplePlatformMultipurposeRSARootCAG1PublicKey
+ _TestApplePlatformMultipurposeRSARootCAG1SKID
+ _TestApplePlatformMultipurposeRSARootCAG1SPKI
+ _TestApplePlatformMultipurposeRSARootCAG1_public_key
+ _TestApplePlatformMultipurposeRSARootCAG1_skid
+ _TestApplePlatformMultipurposeRSARootCAG1_spki
+ _TestApplePlatformRSARootCAG1
+ _TestApplePlatformRSARootCAG1PublicKey
+ _TestApplePlatformRSARootCAG1SKID
+ _TestApplePlatformRSARootCAG1SPKI
+ _TestApplePlatformRSARootCAG1_public_key
+ _TestApplePlatformRSARootCAG1_skid
+ _TestApplePlatformRSARootCAG1_spki
+ _TestApplePlatformTLSECCRootCAG1
+ _TestApplePlatformTLSECCRootCAG1PublicKey
+ _TestApplePlatformTLSECCRootCAG1SKID
+ _TestApplePlatformTLSECCRootCAG1SPKI
+ _TestApplePlatformTLSECCRootCAG1_public_key
+ _TestApplePlatformTLSECCRootCAG1_skid
+ _TestApplePlatformTLSECCRootCAG1_spki
+ _TestApplePlatformTLSRSARootCAG1
+ _TestApplePlatformTLSRSARootCAG1PublicKey
+ _TestApplePlatformTLSRSARootCAG1SKID
+ _TestApplePlatformTLSRSARootCAG1SPKI
+ _TestApplePlatformTLSRSARootCAG1_public_key
+ _TestApplePlatformTLSRSARootCAG1_skid
+ _TestApplePlatformTLSRSARootCAG1_spki
+ _TestAppleRootCAG2
+ _TestAppleRootCAG2SPKI
+ _TestAppleRootCAG2_skid
+ _TestAppleRootCAG2_spki
+ _TestAppleRootCAG3
+ _TestAppleRootCAG3SPKI
+ _TestAppleRootCAG3_skid
+ _TestAppleRootCAG3_spki
+ _TestAppleRootCA_skid
+ _TestAppleRootCA_spki
+ _TestAppleRootECC_skid
+ _TestAppleRootECC_spki
+ _TmMyt2B0
+ _TsbHVdUOnzCHizuzrAdwYFpb
+ _U4HBs
+ _UNKNOWN_REGION_CODE
+ _UcrtRootSPKI
+ _UcrtRoot_public_key
+ _UcrtRoot_spki
+ _V0YaM92nP0Xx19HNvczPJ
+ _V3lNO
+ _VONlh32NYbFTEnv
+ _VVaAJGMXS456O5KIXfqv
+ _W85xZa
+ _WGrQCCz7
+ _WJF2uJCSo
+ _X509PolicyICDPFederation
+ _X5EvIJWqdcALcjaxX6Pl
+ _Xr9TNsiQ
+ _Y2Zxt
+ _YHrWZQ6wU
+ _YMQGEcsGvUj
+ __107-[MobileActivationDaemon updateBasebandTicket:baaCertData:baaIntermediateCert:options:withCompletionBlock:]_block_invoke.411
+ __107-[MobileActivationDaemon updateBasebandTicket:baaCertData:baaIntermediateCert:options:withCompletionBlock:]_block_invoke.411.cold.1
+ __107-[MobileActivationDaemon updateBasebandTicket:baaCertData:baaIntermediateCert:options:withCompletionBlock:]_block_invoke.411.cold.2
+ __107-[MobileActivationDaemon updateBasebandTicket:baaCertData:baaIntermediateCert:options:withCompletionBlock:]_block_invoke.411.cold.3
+ __107-[MobileActivationDaemon updateBasebandTicket:baaCertData:baaIntermediateCert:options:withCompletionBlock:]_block_invoke.411.cold.4
+ __58-[MobileActivationDaemon handleSessionResponse:withError:]_block_invoke.150
+ __61-[MobileActivationDaemon recertifyDeviceWithCompletionBlock:]_block_invoke.339
+ __62-[MobileActivationDaemon issueCollection:withCompletionBlock:]_block_invoke.487
+ __66-[MobileActivationDaemon createActivationInfoWithCompletionBlock:]_block_invoke.274
+ __70-[MobileActivationDaemon copyLegacyDeviceIdentityWithCompletionBlock:]_block_invoke.490
+ __70-[MobileActivationDaemon createTunnel1SessionInfoWithCompletionBlock:]_block_invoke.237
+ __75-[MobileActivationDaemon issueClientCertificateLegacy:WithCompletionBlock:]_block_invoke.361
+ __82-[MobileActivationDaemon createTunnel1ActivationInfo:options:withCompletionBlock:]_block_invoke.199
+ __90-[MobileActivationDaemon copyAttestationDictionaryWithCompletionBlock:options:completion:]_block_invoke.392
+ __94-[MobileActivationDaemon handleActivationInfoWithSession:activationSignature:completionBlock:]_block_invoke.354
+ ___copyNotificationSerialQueue_block_invoke
+ ___handle_eligibility_domain_input_needed_notification_block_invoke
+ ___handle_eligibility_domain_input_needed_notification_block_invoke_2
+ ___register_for_darwin_notifications_block_invoke
+ __block_descriptor_tmp.169
+ __block_literal_global.171
+ __block_literal_global.357
+ __block_literal_global.383
+ __block_literal_global.415
+ __block_literal_global.423
+ __block_literal_global.489
+ __block_literal_global.526
+ __block_literal_global.532
+ __block_literal_global.543
+ __block_literal_global.548
+ __collection_activity_handler_block_invoke.530
+ __collection_activity_handler_block_invoke_2.528
+ __dcrt_oob_activity_handler_block_invoke.513
+ __dcrt_oob_activity_handler_block_invoke.514
+ __dcrt_oob_activity_handler_block_invoke.518
+ __dcrt_oob_activity_handler_block_invoke_2.516
+ __dcrt_oob_load_spreading_activity_handler_block_invoke.506
+ __handle_eligibility_domain_input_needed_notification_block_invoke_2.cold.1
+ __register_xpc_activities_block_invoke.764
+ __register_xpc_activities_block_invoke.764.cold.1
+ __register_xpc_activities_block_invoke.765
+ __register_xpc_activities_block_invoke.765.cold.1
+ __register_xpc_activities_block_invoke.766
+ __register_xpc_activities_block_invoke.766.cold.1
+ __ucrt_oob_activity_handler_block_invoke.544
+ __ucrt_oob_activity_handler_block_invoke.546
+ __ucrt_oob_activity_handler_block_invoke_2.545
+ __xpc_event_key_name
+ __xpc_type_int64
+ _aC4q7GWh
+ _aeD9m
+ _bcn5Uck5
+ _cEG4ZMc
+ _cp2g1b9ro
+ _create_eligibility_input_for_country
+ _create_region_data_for_gestalt
+ _d040f74D
+ _device_supports_missing_emac
+ _g9eargdzvoj3
+ _gDmCYFQnze
+ _gLg1CWr7p
+ _h5eRUOOOhxuaBmELCqQZZEcx
+ _hZZRqgZwI
+ _ha0dkchaters6
+ _hqRB2RyoIJ
+ _hwgAS7
+ _i1IfStf2DSO
+ _iA9rX60D0o2A
+ _icdpFederationAnchors
+ _ioXEmDKsuxLeg
+ _jEGq2i0LF
+ _jfkdDAjba3jd
+ _jmoibFLZ
+ _jr3lMuU8uaAR
+ _jumT7rcoieclCtxS2rgJ
+ _kMAManufacturingData
+ _kMAManufacturingDataCountryCode
+ _kMAManufacturingDataOverride
+ _kMARegionDataForGestaltCountryCode
+ _kMARegionDataForGestaltRegionInfo
+ _kMARegionDataForGestaltSotwareBehaviors
+ _kmezkLiKJOhcpyl
+ _knAHxS
+ _l0934SD
+ _lCUad
+ _lpo7y56t5h
+ _merge_dict_cb.cold.2
+ _mm0Euuzhc
+ _myda13fYo
+ _nXJ7Amk1zyK93
+ _numICDPRoots
+ _os_eligibility_set_input
+ _pDCGH0ta
+ _pggRSNuJfiTW0g
+ _producttype_supports_missing_emac
+ _pwqRYgp9824hrj2Enl
+ _qdrn6
+ _qk82YWRPNDt4yUtuP3cY
+ _region_code_compat_for_country
+ _rpY4QOlsWsxk0fLzfV8h
+ _set_eligibility_input
+ _set_eligibility_input_for_country
+ _strnlen
+ _sv65rt7ugf9si4
+ _t6uy9jukl3
+ _tTA34a4tbgsKsWljx9Ip
+ _u8tyhm3ety
+ _uhO2GULXwfgKwPcp4YR2
+ _wmhYOjgJkR
+ _woqRTqq9PL5McfBs891
+ _xpc_connection_activate
+ _xpc_connection_create_mach_service
+ _xpc_connection_send_message_with_reply_sync
+ _xpc_connection_set_event_handler
+ _xpc_dictionary_create_empty
+ _xpc_dictionary_get_data
+ _xpc_dictionary_get_string
+ _xpc_dictionary_set_data
+ _xpc_int64_get_value
+ _xpc_release
+ _xpc_set_event_stream_handler
+ _ysE4jN2LzGiDiW
+ _zLTj
+ copyNotificationSerialQueue.onceToken
+ copyNotificationSerialQueue.queue
+ iCDPAnchors.c
+ main.cold.13
+ regioncode.m
- /AppleInternal/Library/BuildRoots/6ea8983d-1d96-11f0-ab86-ae4c1e672297/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/usr/local/lib/amd/libDER.a(DER_Decode.o)
- /AppleInternal/Library/BuildRoots/6ea8983d-1d96-11f0-ab86-ae4c1e672297/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/usr/local/lib/libCoreTrust.a(CMS.o)
- /AppleInternal/Library/BuildRoots/6ea8983d-1d96-11f0-ab86-ae4c1e672297/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/usr/local/lib/libCoreTrust.a(CTEvaluate.o)
- /AppleInternal/Library/BuildRoots/6ea8983d-1d96-11f0-ab86-ae4c1e672297/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/usr/local/lib/libCoreTrust.a(CTEvaluateBAA.o)
- /AppleInternal/Library/BuildRoots/6ea8983d-1d96-11f0-ab86-ae4c1e672297/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/usr/local/lib/libCoreTrust.a(CryptoUtils.o)
- /AppleInternal/Library/BuildRoots/6ea8983d-1d96-11f0-ab86-ae4c1e672297/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/usr/local/lib/libCoreTrust.a(DERUtils.o)
- /AppleInternal/Library/BuildRoots/6ea8983d-1d96-11f0-ab86-ae4c1e672297/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/usr/local/lib/libCoreTrust.a(X509Certificate.o)
- /AppleInternal/Library/BuildRoots/6ea8983d-1d96-11f0-ab86-ae4c1e672297/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/usr/local/lib/libCoreTrust.a(X509Chain.o)
- /AppleInternal/Library/BuildRoots/6ea8983d-1d96-11f0-ab86-ae4c1e672297/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/usr/local/lib/libCoreTrust.a(X509Policy.o)
- /AppleInternal/Library/BuildRoots/6ea8983d-1d96-11f0-ab86-ae4c1e672297/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/usr/local/lib/libaks.a(acl_keys.o)
- /AppleInternal/Library/BuildRoots/6ea8983d-1d96-11f0-ab86-ae4c1e672297/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/usr/local/lib/libaks.a(aks_pack.o)
- /AppleInternal/Library/BuildRoots/6ea8983d-1d96-11f0-ab86-ae4c1e672297/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/usr/local/lib/libaks.a(der_utils.o)
- /AppleInternal/Library/BuildRoots/6ea8983d-1d96-11f0-ab86-ae4c1e672297/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/usr/local/lib/libaks.a(firebloom_hacks.o)
- /AppleInternal/Library/BuildRoots/6ea8983d-1d96-11f0-ab86-ae4c1e672297/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/usr/local/lib/libaks.a(libaks_client.o)
- /AppleInternal/Library/BuildRoots/6ea8983d-1d96-11f0-ab86-ae4c1e672297/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/usr/local/lib/libaks.a(libaks_internal.o)
- /AppleInternal/Library/BuildRoots/6ea8983d-1d96-11f0-ab86-ae4c1e672297/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/usr/local/lib/libaks.a(libaks_ref_key.o)
- GCC_except_table114
- GCC_except_table69
- GCC_except_table87
- GCC_except_table94
- _ApplePlatformBackportECCRootG1
- _ApplePlatformBackportECCRootG1PublicKey
- _ApplePlatformBackportECCRootG1SKID
- _ApplePlatformBackportECCRootG1SPKI
- _ApplePlatformBackportRSARootG1
- _ApplePlatformBackportRSARootG1PublicKey
- _ApplePlatformBackportRSARootG1SKID
- _ApplePlatformBackportRSARootG1SPKI
- _AppleRootCAPublicKey
- _AppleRootCASKID
- _AppleRootG2PublicKey
- _AppleRootG2SKID
- _AppleRootG2SPKI
- _AppleRootG3PublicKey
- _AppleRootG3SKID
- _AppleRootG3SPKI
- _BlockedYonkersPublicKey
- _MFi4RootSpki
- _OUTLINED_FUNCTION_15
- _OUTLINED_FUNCTION_21
- _OUTLINED_FUNCTION_66
- _OUTLINED_FUNCTION_68
- _SEKProdRoot
- _SEKProdRootSPKI
- _SEKTestRoot
- _SEKTestRootSPKI
- _TestApplePlatformBackportECCRootG1
- _TestApplePlatformBackportECCRootG1PublicKey
- _TestApplePlatformBackportECCRootG1SKID
- _TestApplePlatformBackportECCRootG1SPKI
- _TestApplePlatformBackportRSARootG1
- _TestApplePlatformBackportRSARootG1PublicKey
- _TestApplePlatformBackportRSARootG1SKID
- _TestApplePlatformBackportRSARootG1SPKI
- _TestAppleRootCAPublicKey
- _TestAppleRootCASKID
- _TestAppleRootECCPublicKey
- _TestAppleRootECCSKID
- _TestAppleRootG2
- _TestAppleRootG2PublicKey
- _TestAppleRootG2SKID
- _TestAppleRootG2SPKI
- _TestAppleRootG3
- _TestAppleRootG3PublicKey
- _TestAppleRootG3SKID
- _TestAppleRootG3SPKI
- _UcrtRootSpki
- __107-[MobileActivationDaemon updateBasebandTicket:baaCertData:baaIntermediateCert:options:withCompletionBlock:]_block_invoke.407
- __107-[MobileActivationDaemon updateBasebandTicket:baaCertData:baaIntermediateCert:options:withCompletionBlock:]_block_invoke.407.cold.1
- __107-[MobileActivationDaemon updateBasebandTicket:baaCertData:baaIntermediateCert:options:withCompletionBlock:]_block_invoke.407.cold.2
- __107-[MobileActivationDaemon updateBasebandTicket:baaCertData:baaIntermediateCert:options:withCompletionBlock:]_block_invoke.407.cold.3
- __107-[MobileActivationDaemon updateBasebandTicket:baaCertData:baaIntermediateCert:options:withCompletionBlock:]_block_invoke.407.cold.4
- __58-[MobileActivationDaemon handleSessionResponse:withError:]_block_invoke.149
- __61-[MobileActivationDaemon recertifyDeviceWithCompletionBlock:]_block_invoke.335
- __62-[MobileActivationDaemon issueCollection:withCompletionBlock:]_block_invoke.483
- __66-[MobileActivationDaemon createActivationInfoWithCompletionBlock:]_block_invoke.273
- __70-[MobileActivationDaemon copyLegacyDeviceIdentityWithCompletionBlock:]_block_invoke.486
- __70-[MobileActivationDaemon createTunnel1SessionInfoWithCompletionBlock:]_block_invoke.236
- __75-[MobileActivationDaemon issueClientCertificateLegacy:WithCompletionBlock:]_block_invoke.357
- __82-[MobileActivationDaemon createTunnel1ActivationInfo:options:withCompletionBlock:]_block_invoke.198
- __90-[MobileActivationDaemon copyAttestationDictionaryWithCompletionBlock:options:completion:]_block_invoke.388
- __94-[MobileActivationDaemon handleActivationInfoWithSession:activationSignature:completionBlock:]_block_invoke.350
- __acrt_root_public_key
- __baa_sep_app_root_public_key
- __baa_sep_app_root_skid
- __baa_sep_app_root_spki
- __baa_system_root_public_key
- __baa_system_root_skid
- __baa_system_root_spki
- __baa_user_root_public_key
- __baa_user_root_skid
- __baa_user_root_spki
- __block_descriptor_tmp.171
- __block_literal_global.173
- __block_literal_global.353
- __block_literal_global.362
- __block_literal_global.394
- __block_literal_global.402
- __block_literal_global.485
- __block_literal_global.520
- __block_literal_global.529
- __block_literal_global.531
- __block_literal_global.545
- __collection_activity_handler_block_invoke.521
- __collection_activity_handler_block_invoke_2.525
- __dcrt_oob_activity_handler_block_invoke.506
- __dcrt_oob_activity_handler_block_invoke.508
- __dcrt_oob_activity_handler_block_invoke.510
- __dcrt_oob_activity_handler_block_invoke_2.513
- __dcrt_oob_load_spreading_activity_handler_block_invoke.503
- __mfi4_root_pub_key
- __mfi4_root_skid
- __mfi4_root_spki
- __register_xpc_activities_block_invoke.755
- __register_xpc_activities_block_invoke.755.cold.1
- __register_xpc_activities_block_invoke.756
- __register_xpc_activities_block_invoke.756.cold.1
- __register_xpc_activities_block_invoke.757
- __register_xpc_activities_block_invoke.757.cold.1
- __sek_prod_root_public_key
- __sek_prod_root_skid
- __sek_prod_root_spki
- __sek_test_root_public_key
- __sek_test_root_skid
- __sek_test_root_spki
- __ucrt_oob_activity_handler_block_invoke.532
- __ucrt_oob_activity_handler_block_invoke.543
- __ucrt_oob_activity_handler_block_invoke_2.542
- __ucrt_root_pub_key
- __ucrt_root_spki
- _der_key_validate
- _kMAOptionsAllowInvalidNetworkCertificates
- der_key_validate.cold.1
- der_key_validate.cold.2
CStrings:
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s aks connection failed%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s bad 1%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s fail%s\n"
+ "-[MobileActivationDaemon copyRegionDataForGestaltWithCompletionBlock:]"
+ "0x%x"
+ "1055"
+ "Absinthe/2.0 iOS Device Activator (MobileActivation-1055 built on May 30 2025 at 19:36:32)"
+ "Activation record is missing expected key: %@"
+ "CountryCode"
+ "DemoLoop"
+ "Failed to allocate dictionary"
+ "Failed to create eligibility input."
+ "Failed to create region code mapping for %@"
+ "Failed to create region data."
+ "Failed to set eligibility input."
+ "Failed to set eligibility input: %@"
+ "Failed to set eligibility input: %d (%s)"
+ "FeatureAccessAgent"
+ "J/A"
+ "JP"
+ "KH/A"
+ "KR"
+ "LL/A"
+ "Manufacturing data is missing expected key: %@"
+ "ManufacturingData"
+ "ManufacturingDataOverride"
+ "OS_ELIGIBILITY_INPUT_SHIPTO_LOCATION_KEY_COUNTRY_CODE"
+ "OS_ELIGIBILITY_INPUT_SHIPTO_LOCATION_KEY_LEGACY_REGION_INFO"
+ "OS_ELIGIBILITY_INPUT_SHIPTO_LOCATION_KEY_LEGACY_SOFTWARE_BEHAVIORS"
+ "Processing eligibility notification..."
+ "RegionDataForGestaltCountryCode"
+ "RegionDataForGestaltRegionInfo"
+ "RegionDataForGestaltSotwareBehaviors"
+ "RepairApp"
+ "Successfully processed eligibility notification."
+ "SupportFlow"
+ "TestCountry1"
+ "TestCountry1RegionCode"
+ "TestCountry2"
+ "TestCountry2RegionCode"
+ "com.apple.mobileactivationd.notifications"
+ "com.apple.notifyd.matching"
+ "com.apple.os-eligibility-domain.input-needed"
+ "copyRegionDataForGestaltWithCompletionBlock:"
+ "create_region_data_for_gestalt"
+ "failed to open connection to %s: %d\n"
+ "failed to open userclient via %s: %d\n"
+ "featureaccessd"
+ "frauddefensed"
+ "iOS Device Activator (MobileActivation-1055)"
+ "managedassetsd"
+ "set_eligibility_input"
+ "set_eligibility_input_for_country"
- "%s%s:%s%s%s%s%u:%s%u:%s aks connection failed%s\n"
- "%s%s:%s%s%s%s%u:%s%u:%s bad 1%s\n"
- "%s%s:%s%s%s%s%u:%s%u:%s bad 2%s\n"
- "%s%s:%s%s%s%s%u:%s%u:%s fail%s\n"
- "1017.120.3"
- "Absinthe/2.0 iOS Device Activator (MobileActivation-1017.120.3 built on Apr 20 2025 at 21:21:07)"
- "AllowInvalidNetworkCertificates"
- "der_key_validate"
- "failed to open connection to %s\n"
- "iOS Device Activator (MobileActivation-1017.120.3)"

```
