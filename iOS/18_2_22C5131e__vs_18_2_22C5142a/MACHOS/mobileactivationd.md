## mobileactivationd

> `/usr/libexec/mobileactivationd`

```diff

 1015.60.1.0.0
-  __TEXT.__text: 0x1fe144
+  __TEXT.__text: 0x1fdb78
   __TEXT.__auth_stubs: 0x10a0
   __TEXT.__objc_stubs: 0x2ec0
   __TEXT.__objc_methlist: 0xa80
-  __TEXT.__const: 0x46181
+  __TEXT.__const: 0x46351
   __TEXT.__cstring: 0xd7fb
   __TEXT.__objc_methname: 0x3ce7
   __TEXT.__oslogstring: 0xe5a

   __DATA_CONST.__auth_got: 0x860
   __DATA_CONST.__got: 0x488
   __DATA_CONST.__auth_ptr: 0x40
-  __DATA_CONST.__const: 0xdc38
+  __DATA_CONST.__const: 0xdf30
   __DATA_CONST.__cfstring: 0xc020
   __DATA_CONST.__objc_classlist: 0x50
   __DATA_CONST.__objc_catlist: 0x18

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/liblockdown.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1298
-  Symbols:   9132
+  Functions: 1297
+  Symbols:   9161
   CStrings:  2804
 
Symbols:
+ /AppleInternal/Library/BuildRoots/c293e576-9dba-11ef-b7d9-de9f3dcc796f/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.2.Internal.sdk/usr/local/lib/amd/libDER.a(DER_Decode.o)
+ /AppleInternal/Library/BuildRoots/c293e576-9dba-11ef-b7d9-de9f3dcc796f/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.2.Internal.sdk/usr/local/lib/libCoreTrust.a(CMS.o)
+ /AppleInternal/Library/BuildRoots/c293e576-9dba-11ef-b7d9-de9f3dcc796f/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.2.Internal.sdk/usr/local/lib/libCoreTrust.a(CTEvaluate.o)
+ /AppleInternal/Library/BuildRoots/c293e576-9dba-11ef-b7d9-de9f3dcc796f/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.2.Internal.sdk/usr/local/lib/libCoreTrust.a(CTEvaluateBAA.o)
+ /AppleInternal/Library/BuildRoots/c293e576-9dba-11ef-b7d9-de9f3dcc796f/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.2.Internal.sdk/usr/local/lib/libCoreTrust.a(CryptoUtils.o)
+ /AppleInternal/Library/BuildRoots/c293e576-9dba-11ef-b7d9-de9f3dcc796f/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.2.Internal.sdk/usr/local/lib/libCoreTrust.a(DERUtils.o)
+ /AppleInternal/Library/BuildRoots/c293e576-9dba-11ef-b7d9-de9f3dcc796f/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.2.Internal.sdk/usr/local/lib/libCoreTrust.a(X509Certificate.o)
+ /AppleInternal/Library/BuildRoots/c293e576-9dba-11ef-b7d9-de9f3dcc796f/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.2.Internal.sdk/usr/local/lib/libCoreTrust.a(X509Chain.o)
+ /AppleInternal/Library/BuildRoots/c293e576-9dba-11ef-b7d9-de9f3dcc796f/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.2.Internal.sdk/usr/local/lib/libCoreTrust.a(X509Policy.o)
+ /AppleInternal/Library/BuildRoots/c293e576-9dba-11ef-b7d9-de9f3dcc796f/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.2.Internal.sdk/usr/local/lib/libaks.a(acl_keys.o)
+ /AppleInternal/Library/BuildRoots/c293e576-9dba-11ef-b7d9-de9f3dcc796f/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.2.Internal.sdk/usr/local/lib/libaks.a(aks_pack.o)
+ /AppleInternal/Library/BuildRoots/c293e576-9dba-11ef-b7d9-de9f3dcc796f/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.2.Internal.sdk/usr/local/lib/libaks.a(der_utils.o)
+ /AppleInternal/Library/BuildRoots/c293e576-9dba-11ef-b7d9-de9f3dcc796f/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.2.Internal.sdk/usr/local/lib/libaks.a(firebloom_hacks.o)
+ /AppleInternal/Library/BuildRoots/c293e576-9dba-11ef-b7d9-de9f3dcc796f/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.2.Internal.sdk/usr/local/lib/libaks.a(libaks_client.o)
+ /AppleInternal/Library/BuildRoots/c293e576-9dba-11ef-b7d9-de9f3dcc796f/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.2.Internal.sdk/usr/local/lib/libaks.a(libaks_internal.o)
+ /AppleInternal/Library/BuildRoots/c293e576-9dba-11ef-b7d9-de9f3dcc796f/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.2.Internal.sdk/usr/local/lib/libaks.a(libaks_ref_key.o)
+ CTEvaluateBAA.c
+ _CTEvaluateSEK
+ _CTGetSEKType
+ _SEKProdRoot
+ _SEKProdRootPublicKey
+ _SEKProdRootSKID
+ _SEKProdRootSPKI
+ _SEKTestRoot
+ _SEKTestRootPublicKey
+ _SEKTestRootSKID
+ _SEKTestRootSPKI
+ _X509PolicySEK
+ __sek_prod_root_public_key
+ __sek_prod_root_skid
+ __sek_prod_root_spki
+ __sek_test_root_public_key
+ __sek_test_root_skid
+ __sek_test_root_spki
- /AppleInternal/Library/BuildRoots/fb221e8a-99d7-11ef-987f-0e2f5cba2fa5/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.2.Internal.sdk/usr/local/lib/amd/libDER.a(DER_Decode.o)
- /AppleInternal/Library/BuildRoots/fb221e8a-99d7-11ef-987f-0e2f5cba2fa5/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.2.Internal.sdk/usr/local/lib/libCoreTrust.a(CMS.o)
- /AppleInternal/Library/BuildRoots/fb221e8a-99d7-11ef-987f-0e2f5cba2fa5/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.2.Internal.sdk/usr/local/lib/libCoreTrust.a(CTEvaluate.o)
- /AppleInternal/Library/BuildRoots/fb221e8a-99d7-11ef-987f-0e2f5cba2fa5/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.2.Internal.sdk/usr/local/lib/libCoreTrust.a(CryptoUtils.o)
- /AppleInternal/Library/BuildRoots/fb221e8a-99d7-11ef-987f-0e2f5cba2fa5/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.2.Internal.sdk/usr/local/lib/libCoreTrust.a(DERUtils.o)
- /AppleInternal/Library/BuildRoots/fb221e8a-99d7-11ef-987f-0e2f5cba2fa5/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.2.Internal.sdk/usr/local/lib/libCoreTrust.a(X509Certificate.o)
- /AppleInternal/Library/BuildRoots/fb221e8a-99d7-11ef-987f-0e2f5cba2fa5/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.2.Internal.sdk/usr/local/lib/libCoreTrust.a(X509Chain.o)
- /AppleInternal/Library/BuildRoots/fb221e8a-99d7-11ef-987f-0e2f5cba2fa5/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.2.Internal.sdk/usr/local/lib/libCoreTrust.a(X509Policy.o)
- /AppleInternal/Library/BuildRoots/fb221e8a-99d7-11ef-987f-0e2f5cba2fa5/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.2.Internal.sdk/usr/local/lib/libaks.a(acl_keys.o)
- /AppleInternal/Library/BuildRoots/fb221e8a-99d7-11ef-987f-0e2f5cba2fa5/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.2.Internal.sdk/usr/local/lib/libaks.a(aks_pack.o)
- /AppleInternal/Library/BuildRoots/fb221e8a-99d7-11ef-987f-0e2f5cba2fa5/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.2.Internal.sdk/usr/local/lib/libaks.a(der_utils.o)
- /AppleInternal/Library/BuildRoots/fb221e8a-99d7-11ef-987f-0e2f5cba2fa5/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.2.Internal.sdk/usr/local/lib/libaks.a(firebloom_hacks.o)
- /AppleInternal/Library/BuildRoots/fb221e8a-99d7-11ef-987f-0e2f5cba2fa5/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.2.Internal.sdk/usr/local/lib/libaks.a(libaks_client.o)
- /AppleInternal/Library/BuildRoots/fb221e8a-99d7-11ef-987f-0e2f5cba2fa5/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.2.Internal.sdk/usr/local/lib/libaks.a(libaks_internal.o)
- /AppleInternal/Library/BuildRoots/fb221e8a-99d7-11ef-987f-0e2f5cba2fa5/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.2.Internal.sdk/usr/local/lib/libaks.a(libaks_ref_key.o)
- _CTEvaluateAccessoryCert
- _CTParseAccessoryCerts
- _CTParseFlagsForAccessoryCerts
CStrings:
+ "Absinthe/2.0 iOS Device Activator (MobileActivation-1015.60.1 built on Nov 11 2024 at 00:18:42)"
- "Absinthe/2.0 iOS Device Activator (MobileActivation-1015.60.1 built on Nov  3 2024 at 23:02:20)"

```
