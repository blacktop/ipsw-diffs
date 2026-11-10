## mobileactivationd

> `/usr/libexec/mobileactivationd`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-1145.0.2.0.0
-  __TEXT.__text: 0x65574
-  __TEXT.__auth_stubs: 0x1190
-  __TEXT.__objc_stubs: 0x24c0
-  __TEXT.__objc_methlist: 0x8ec
+1145.40.5.0.4
+  __TEXT.__text: 0x65904
+  __TEXT.__auth_stubs: 0x11b0
+  __TEXT.__objc_stubs: 0x24e0
+  __TEXT.__objc_methlist: 0x8fc
   __TEXT.__const: 0x18be3
   __TEXT.__gcc_except_tab: 0x12c0
-  __TEXT.__objc_methname: 0x2879
+  __TEXT.__objc_methname: 0x28b9
   __TEXT.__oslogstring: 0x143f
-  __TEXT.__cstring: 0xc567
+  __TEXT.__cstring: 0xc6b2
   __TEXT.__objc_classname: 0x104
   __TEXT.__objc_methtype: 0x908
   __TEXT.__ustring: 0x4
   __TEXT.__dlopen_cstrs: 0x267
-  __TEXT.__unwind_info: 0x1390
+  __TEXT.__unwind_info: 0x1398
   __DATA_CONST.__const: 0x6670
-  __DATA_CONST.__cfstring: 0xa4e0
+  __DATA_CONST.__cfstring: 0xa620
   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x30

   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x28
   __DATA_CONST.__objc_intobj: 0x2e8
-  __DATA_CONST.__objc_arraydata: 0x5f8
+  __DATA_CONST.__objc_arraydata: 0x600
   __DATA_CONST.__objc_arrayobj: 0x90
-  __DATA_CONST.__auth_got: 0x8d8
+  __DATA_CONST.__auth_got: 0x8e8
   __DATA_CONST.__got: 0x448
   __DATA_CONST.__auth_ptr: 0x60
-  __DATA.__objc_const: 0xeb8
-  __DATA.__objc_selrefs: 0xb68
-  __DATA.__objc_ivar: 0x88
+  __DATA.__objc_const: 0xee8
+  __DATA.__objc_selrefs: 0xb70
+  __DATA.__objc_ivar: 0x8c
   __DATA.__objc_data: 0x230
   __DATA.__data: 0x46a
   __DATA.__bss: 0x278

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbootpolicy.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1447
-  Symbols:   3558
-  CStrings:  2498
+  Functions: 1450
+  Symbols:   3567
+  CStrings:  2514
 
Symbols:
+ -[DeviceType is_home_accessory]
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.2.Internal.sdk/usr/local/lib/amd/libDER.a(DER_Decode.o)
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.2.Internal.sdk/usr/local/lib/libCoreTrust.a(AppleAnchors.o)
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.2.Internal.sdk/usr/local/lib/libCoreTrust.a(CMS.o)
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.2.Internal.sdk/usr/local/lib/libCoreTrust.a(CTEvaluate.o)
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.2.Internal.sdk/usr/local/lib/libCoreTrust.a(CTEvaluateBAA.o)
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.2.Internal.sdk/usr/local/lib/libCoreTrust.a(CryptoUtils.o)
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.2.Internal.sdk/usr/local/lib/libCoreTrust.a(DERUtils.o)
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.2.Internal.sdk/usr/local/lib/libCoreTrust.a(X509Certificate.o)
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.2.Internal.sdk/usr/local/lib/libCoreTrust.a(X509Chain.o)
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.2.Internal.sdk/usr/local/lib/libCoreTrust.a(X509Policy.o)
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.2.Internal.sdk/usr/local/lib/libCoreTrust.a(iCDPAnchors.o)
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.2.Internal.sdk/usr/local/lib/libaks.a(der_utils.o)
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.2.Internal.sdk/usr/local/lib/libaks.a(firebloom_hacks.o)
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.2.Internal.sdk/usr/local/lib/libaks.a(libaks_client.o)
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.2.Internal.sdk/usr/local/lib/libaks.a(libaks_internal.o)
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.2.Internal.sdk/usr/local/lib/libaks.a(libaks_ref_key.o)
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/mobileactivationdMacOS.build/Objects-normal/arm64e/battery_management.o
+ OBJC_IVAR_$_DeviceType._is_home_accessory
+ _IOPSSetBatteryDateOfFirstUseWithPackDetails
+ __os_feature_enabled_impl
+ _is_home_accessory
+ _objc_msgSend$is_home_accessory
+ _setBatteryDateOfFirtUse
+ battery_management.m
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.0.Internal.sdk/usr/local/lib/amd/libDER.a(DER_Decode.o)
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.0.Internal.sdk/usr/local/lib/libCoreTrust.a(AppleAnchors.o)
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.0.Internal.sdk/usr/local/lib/libCoreTrust.a(CMS.o)
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.0.Internal.sdk/usr/local/lib/libCoreTrust.a(CTEvaluate.o)
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.0.Internal.sdk/usr/local/lib/libCoreTrust.a(CTEvaluateBAA.o)
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.0.Internal.sdk/usr/local/lib/libCoreTrust.a(CryptoUtils.o)
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.0.Internal.sdk/usr/local/lib/libCoreTrust.a(DERUtils.o)
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.0.Internal.sdk/usr/local/lib/libCoreTrust.a(X509Certificate.o)
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.0.Internal.sdk/usr/local/lib/libCoreTrust.a(X509Chain.o)
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.0.Internal.sdk/usr/local/lib/libCoreTrust.a(X509Policy.o)
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.0.Internal.sdk/usr/local/lib/libCoreTrust.a(iCDPAnchors.o)
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.0.Internal.sdk/usr/local/lib/libaks.a(der_utils.o)
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.0.Internal.sdk/usr/local/lib/libaks.a(firebloom_hacks.o)
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.0.Internal.sdk/usr/local/lib/libaks.a(libaks_client.o)
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.0.Internal.sdk/usr/local/lib/libaks.a(libaks_internal.o)
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.0.Internal.sdk/usr/local/lib/libaks.a(libaks_ref_key.o)
Functions:
~ -[DeviceType init] : 2236 -> 2256
+ -[DeviceType ucrt_enforced]
+ _has_internal_diagnostics
~ _producttype_supports_missing_emac : 8 -> 128
~ _device_supports_missing_emac : 40 -> 64
+ _setBatteryDateOfFirtUse
~ _storeUCRT : 3092 -> 3496
~ _OUTLINED_FUNCTION_15 : 48 -> 20
+ _OUTLINED_FUNCTION_17
- _OUTLINED_FUNCTION_18
~ _X509ExtensionParseBasicConstraints : 208 -> 204
~ _X509ChainBuildPathPartial : 484 -> 496
CStrings:
+ "1145.40.5.0.4"
+ "ACCHWComponentAuthService"
+ "Absinthe/2.0 macOS Device Activator (MobileActivation-1145.40.5.0.4 built on Oct  3 2026 at 16:08:30)"
+ "AudioAccessory11,1"
+ "DeviceSupportsBatteryInformation"
+ "Failed to copy UCRT validity date."
+ "Failed to retrieve '%@'."
+ "Failed to set battery date of first use."
+ "Failed to set battery date of first use: 0x%08x"
+ "HomeAccessory"
+ "HomeAccessory17,1"
+ "HomeAccessory17,2"
+ "TB,R,N,V_is_home_accessory"
+ "_is_home_accessory"
+ "dossier"
+ "is_home_accessory"
+ "macOS Device Activator (MobileActivation-1145.40.5.0.4)"
+ "powerd"
+ "setBatteryDateOfFirtUse"
- "1145.0.2"
- "Absinthe/2.0 macOS Device Activator (MobileActivation-1145.0.2 built on Aug  8 2026 at 15:54:48)"
- "macOS Device Activator (MobileActivation-1145.0.2)"
```
