# 18.3.1 (22D72) .vs 18.3.2 (22D82)

## Security Content

- <https://support.apple.com/en-us/122281>

## IPSWs

- `iPhone17,1_18.3.1_22D72_Restore.ipsw`
- `iPhone17,1_18.3.2_22D82_Restore.ipsw`

## Kernel

### Version

| iOS | Version | Build | Date |
| :-- | :------ | :---- | :--- |
| 18.3.1 *(22D72)* | 24.3.0 | 11215.82.4~20 | Thu, 16Jan2025 03:00:11 PST |
| 18.3.2 *(22D82)* | 24.3.0 | 11215.82.4~20 | Thu, 16Jan2025 03:00:11 PST |

## MachO

### 🆕 NEW (7)

- `/usr/lib/libLogRedirect.dylib`
- `/usr/lib/libffi-trampolines.dylib`
- `/usr/lib/libglInterpose.dylib`
- `/usr/lib/libmobileassetd.dylib`
- `/usr/lib/libobjc-trampolines.dylib`
- `/usr/lib/libstdc++.6.0.9.dylib`
- `/usr/libexec/BatteryAlgorithms.framework/BatteryAlgorithms`

### ⬆️ Updated (5)

<details>
  <summary><i>View Updated</i></summary>

#### PasswordsSettings

>  `/System/Library/PreferenceBundles/PasswordsSettings.bundle/PasswordsSettings`

```diff

-7620.2.4.10.7
+7620.2.4.10.8
   __TEXT.__text: 0x7ce0
   __TEXT.__auth_stubs: 0x910
   __TEXT.__objc_methlist: 0x19c

   __TEXT.__eh_frame: 0x108
   __DATA_CONST.__auth_got: 0x488
   __DATA_CONST.__got: 0x1f0
-  __DATA_CONST.__auth_ptr: 0x168
+  __DATA_CONST.__auth_ptr: 0x150
   __DATA_CONST.__const: 0x238
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_protolist: 0x30

```

#### SearchIndexer

>  `/System/Library/PrivateFrameworks/Message.framework/XPCServices/SearchIndexer.xpc/SearchIndexer`

```diff

-3826.400.131.2.14
-  __TEXT.__text: 0x5de424
+3826.400.131.2.15
+  __TEXT.__text: 0x5e1c3c
   __TEXT.__auth_stubs: 0x4390
   __TEXT.__objc_stubs: 0x140
   __TEXT.__objc_methlist: 0x198
-  __TEXT.__cstring: 0x8e89
+  __TEXT.__cstring: 0x8e59
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__const: 0x42ff0
+  __TEXT.__const: 0x43040
   __TEXT.__swift5_typeref: 0xe1f9
   __TEXT.__swift5_capture: 0x7edc
-  __TEXT.__constg_swiftt: 0xb91c
+  __TEXT.__constg_swiftt: 0xb908
   __TEXT.__swift5_reflstr: 0xd5a9
   __TEXT.__swift5_fieldmd: 0x12160
   __TEXT.__swift5_proto: 0x2398
   __TEXT.__swift5_types: 0x1434
   __TEXT.__swift5_assocty: 0x1620
-  __TEXT.__oslogstring: 0xeb80
+  __TEXT.__oslogstring: 0xeb20
   __TEXT.__swift5_builtin: 0xb18
   __TEXT.__swift5_mpenum: 0x7f8
   __TEXT.__swift5_protos: 0x74

   __TEXT.__objc_methtype: 0x3e5
   __TEXT.__gcc_except_tab: 0x10c
   __TEXT.__unwind_info: 0x130a8
-  __TEXT.__eh_frame: 0x193a0
+  __TEXT.__eh_frame: 0x19368
   __DATA_CONST.__auth_got: 0x21d8
   __DATA_CONST.__got: 0xb40
-  __DATA_CONST.__auth_ptr: 0x3050
-  __DATA_CONST.__const: 0x48770
+  __DATA_CONST.__auth_ptr: 0x3058
+  __DATA_CONST.__const: 0x486e0
   __DATA_CONST.__cfstring: 0x20
-  __DATA_CONST.__objc_classlist: 0x1a0
+  __DATA_CONST.__objc_classlist: 0x198
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x100
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x80
-  __DATA.__objc_const: 0x4c20
+  __DATA.__objc_const: 0x4b90
   __DATA.__objc_selrefs: 0x798
-  __DATA.__objc_data: 0x980
-  __DATA.__data: 0x11de8
+  __DATA.__objc_data: 0x930
+  __DATA.__data: 0x11e58
   __DATA.__bss: 0x45dc0
-  __DATA.__common: 0xcf8
+  __DATA.__common: 0xce8
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/Contacts.framework/Contacts
   - /System/Library/Frameworks/CoreData.framework/CoreData

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 29355
+  Functions: 29368
   Symbols:   446
-  CStrings:  2987
+  CStrings:  2984
 
CStrings:
+ "[%.*hhx] Did mark %ld more mailboxes as sync complete."
+ "[%.*hhx] [{%.*hx}-%{sensitive,mask.mailbox}s] Did mark as sync complete."
- "[%.*hhx-%{public}s] %{sensitive,mask.mailbox}s ."
- "[%.*hhx-%{public}s] Did mark %ld more mailboxes as sync complete."
- "[%.*hhx-%{public}s] [{%.*hx}-%{sensitive,mask.mailbox}s] Did mark as sync complete."
- "_TtCV13IMAP2Behavior5State6Logger"
- "l"

```

#### MobileMail

>  `/private/var/staged_system_apps/MobileMail.app/MobileMail`

```diff

-3826.400.131.2.14
+3826.400.131.2.15
   __TEXT.__text: 0x45b5a4
   __TEXT.__auth_stubs: 0x6180
   __TEXT.__objc_stubs: 0x40600

   __TEXT.__eh_frame: 0x2910
   __DATA_CONST.__auth_got: 0x30d0
   __DATA_CONST.__got: 0x3768
-  __DATA_CONST.__auth_ptr: 0x1ed8
+  __DATA_CONST.__auth_ptr: 0x1e28
   __DATA_CONST.__const: 0x15490
   __DATA_CONST.__cfstring: 0xe4c0
   __DATA_CONST.__objc_classlist: 0xe00

```

#### SafariWidgetExtension

>  `/private/var/staged_system_apps/MobileSafari.app/PlugIns/SafariWidgetExtension.appex/SafariWidgetExtension`

```diff

-7620.2.4.10.7
+7620.2.4.10.8
   __TEXT.__text: 0x4bcac
   __TEXT.__auth_stubs: 0x1560
   __TEXT.__cstring: 0x308a

   __TEXT.__eh_frame: 0x1dac
   __DATA_CONST.__auth_got: 0xab0
   __DATA_CONST.__got: 0x548
-  __DATA_CONST.__auth_ptr: 0xc90
+  __DATA_CONST.__auth_ptr: 0xc88
   __DATA_CONST.__const: 0x1778
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8

```

#### mobileactivationd

>  `/usr/libexec/mobileactivationd`

```diff

-1015.60.1.0.0
-  __TEXT.__text: 0x1fdb78
+1015.82.2.0.0
+  __TEXT.__text: 0x1fdedc
   __TEXT.__auth_stubs: 0x10a0
   __TEXT.__objc_stubs: 0x2ec0
   __TEXT.__objc_methlist: 0xa80
   __TEXT.__const: 0x46351
-  __TEXT.__cstring: 0xd7fb
+  __TEXT.__cstring: 0xd8b7
   __TEXT.__objc_methname: 0x3ce7
   __TEXT.__oslogstring: 0xe5a
   __TEXT.__objc_classname: 0x1b4

   __TEXT.__gcc_except_tab: 0x198c
   __TEXT.__dlopen_cstrs: 0x24c
   __TEXT.__ustring: 0x4
-  __TEXT.__unwind_info: 0x1118
+  __TEXT.__unwind_info: 0x1120
   __TEXT.__eh_frame: 0x1108
   __DATA_CONST.__auth_got: 0x860
   __DATA_CONST.__got: 0x488
   __DATA_CONST.__auth_ptr: 0x40
   __DATA_CONST.__const: 0xdf30
-  __DATA_CONST.__cfstring: 0xc020
+  __DATA_CONST.__cfstring: 0xc0e0
   __DATA_CONST.__objc_classlist: 0x50
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x48

   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x40
   __DATA_CONST.__objc_intobj: 0x258
-  __DATA_CONST.__objc_arraydata: 0x450
+  __DATA_CONST.__objc_arraydata: 0x458
   __DATA_CONST.__objc_arrayobj: 0x90
   __DATA.__objc_const: 0x23c8
   __DATA.__objc_selrefs: 0xd50

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/liblockdown.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1297
-  Symbols:   9161
-  CStrings:  2804
+  Functions: 1300
+  Symbols:   9176
+  CStrings:  2813
 
Symbols:
+ /AppleInternal/Library/BuildRoots/ab3efd37-e438-11ef-ae41-de23e2c06a38/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/lib/amd/libDER.a(DER_Decode.o)
+ /AppleInternal/Library/BuildRoots/ab3efd37-e438-11ef-ae41-de23e2c06a38/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/lib/libCoreTrust.a(CMS.o)
+ /AppleInternal/Library/BuildRoots/ab3efd37-e438-11ef-ae41-de23e2c06a38/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/lib/libCoreTrust.a(CTEvaluate.o)
+ /AppleInternal/Library/BuildRoots/ab3efd37-e438-11ef-ae41-de23e2c06a38/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/lib/libCoreTrust.a(CTEvaluateBAA.o)
+ /AppleInternal/Library/BuildRoots/ab3efd37-e438-11ef-ae41-de23e2c06a38/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/lib/libCoreTrust.a(CryptoUtils.o)
+ /AppleInternal/Library/BuildRoots/ab3efd37-e438-11ef-ae41-de23e2c06a38/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/lib/libCoreTrust.a(DERUtils.o)
+ /AppleInternal/Library/BuildRoots/ab3efd37-e438-11ef-ae41-de23e2c06a38/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/lib/libCoreTrust.a(X509Certificate.o)
+ /AppleInternal/Library/BuildRoots/ab3efd37-e438-11ef-ae41-de23e2c06a38/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/lib/libCoreTrust.a(X509Chain.o)
+ /AppleInternal/Library/BuildRoots/ab3efd37-e438-11ef-ae41-de23e2c06a38/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/lib/libCoreTrust.a(X509Policy.o)
+ /AppleInternal/Library/BuildRoots/ab3efd37-e438-11ef-ae41-de23e2c06a38/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/lib/libaks.a(acl_keys.o)
+ /AppleInternal/Library/BuildRoots/ab3efd37-e438-11ef-ae41-de23e2c06a38/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/lib/libaks.a(aks_pack.o)
+ /AppleInternal/Library/BuildRoots/ab3efd37-e438-11ef-ae41-de23e2c06a38/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/lib/libaks.a(der_utils.o)
+ /AppleInternal/Library/BuildRoots/ab3efd37-e438-11ef-ae41-de23e2c06a38/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/lib/libaks.a(firebloom_hacks.o)
+ /AppleInternal/Library/BuildRoots/ab3efd37-e438-11ef-ae41-de23e2c06a38/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/lib/libaks.a(libaks_client.o)
+ /AppleInternal/Library/BuildRoots/ab3efd37-e438-11ef-ae41-de23e2c06a38/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/lib/libaks.a(libaks_internal.o)
+ /AppleInternal/Library/BuildRoots/ab3efd37-e438-11ef-ae41-de23e2c06a38/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/lib/libaks.a(libaks_ref_key.o)
+ GCC_except_table25
+ __block_literal_global.203
+ _validateCertificateOID
+ _validateCertificateOIDArray
+ _validateOIDKeyUsageProperties
- /AppleInternal/Library/BuildRoots/774ff07e-d344-11ef-9a16-36218cb420d5/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/lib/amd/libDER.a(DER_Decode.o)
- /AppleInternal/Library/BuildRoots/774ff07e-d344-11ef-9a16-36218cb420d5/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/lib/libCoreTrust.a(CMS.o)
- /AppleInternal/Library/BuildRoots/774ff07e-d344-11ef-9a16-36218cb420d5/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/lib/libCoreTrust.a(CTEvaluate.o)
- /AppleInternal/Library/BuildRoots/774ff07e-d344-11ef-9a16-36218cb420d5/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/lib/libCoreTrust.a(CTEvaluateBAA.o)
- /AppleInternal/Library/BuildRoots/774ff07e-d344-11ef-9a16-36218cb420d5/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/lib/libCoreTrust.a(CryptoUtils.o)
- /AppleInternal/Library/BuildRoots/774ff07e-d344-11ef-9a16-36218cb420d5/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/lib/libCoreTrust.a(DERUtils.o)
- /AppleInternal/Library/BuildRoots/774ff07e-d344-11ef-9a16-36218cb420d5/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/lib/libCoreTrust.a(X509Certificate.o)
- /AppleInternal/Library/BuildRoots/774ff07e-d344-11ef-9a16-36218cb420d5/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/lib/libCoreTrust.a(X509Chain.o)
- /AppleInternal/Library/BuildRoots/774ff07e-d344-11ef-9a16-36218cb420d5/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/lib/libCoreTrust.a(X509Policy.o)
- /AppleInternal/Library/BuildRoots/774ff07e-d344-11ef-9a16-36218cb420d5/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/lib/libaks.a(acl_keys.o)
- /AppleInternal/Library/BuildRoots/774ff07e-d344-11ef-9a16-36218cb420d5/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/lib/libaks.a(aks_pack.o)
- /AppleInternal/Library/BuildRoots/774ff07e-d344-11ef-9a16-36218cb420d5/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/lib/libaks.a(der_utils.o)
- /AppleInternal/Library/BuildRoots/774ff07e-d344-11ef-9a16-36218cb420d5/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/lib/libaks.a(firebloom_hacks.o)
- /AppleInternal/Library/BuildRoots/774ff07e-d344-11ef-9a16-36218cb420d5/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/lib/libaks.a(libaks_client.o)
- /AppleInternal/Library/BuildRoots/774ff07e-d344-11ef-9a16-36218cb420d5/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/lib/libaks.a(libaks_internal.o)
- /AppleInternal/Library/BuildRoots/774ff07e-d344-11ef-9a16-36218cb420d5/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/lib/libaks.a(libaks_ref_key.o)
- GCC_except_table22
- __block_literal_global.185
CStrings:
+ "1015.82.2"
+ "5"
+ "Absinthe/2.0 iOS Device Activator (MobileActivation-1015.82.2 built on Mar  5 2025 at 03:06:41)"
+ "Empty OID list."
+ "Failed to query OID %@."
+ "Failed to validate %@."
+ "Failed to validate OID %@."
+ "Failed to validate OID(s): %@"
+ "Missing 'sepClient' property."
+ "iOS Device Activator (MobileActivation-1015.82.2)"
+ "validateCertificateOID"
+ "validateCertificateOIDArray"
+ "validateOIDKeyUsageProperties"
- "1015.60.1"
- "Absinthe/2.0 iOS Device Activator (MobileActivation-1015.60.1 built on Jan 16 2025 at 03:56:05)"
- "Existing %@ is missing required OID(s) (%@)."
- "iOS Device Activator (MobileActivation-1015.60.1)"

```


</details>

### 🔑 Entitlements

- [Entitlements DIFF](Entitlements.md)

## DSC

### WebKit

| iOS | Version |
| :-- | :------ |
| 18.3.1 *(22D72)* | 620.2.4.10.7 |
| 18.3.2 *(22D82)* | 620.2.4.10.8 |

### Dylibs

#### ⬆️ Updated (7)

<details>
  <summary><i>View Updated</i></summary>

#### _AuthenticationServices_SwiftUI

>  `/System/Library/Frameworks/_AuthenticationServices_SwiftUI.framework/_AuthenticationServices_SwiftUI`

```diff

-620.2.4.10.7
+620.2.4.10.8
   __TEXT.__text: 0xd95c
   __TEXT.__auth_stubs: 0xa30
   __TEXT.__objc_methlist: 0x190

   __DATA_CONST.__objc_selrefs: 0xf8
   __DATA_CONST.__objc_protorefs: 0x40
   __AUTH_CONST.__auth_got: 0x518
-  __AUTH_CONST.__auth_ptr: 0x408
+  __AUTH_CONST.__auth_ptr: 0x410
   __AUTH_CONST.__const: 0xbb8
   __AUTH_CONST.__objc_const: 0x958
   __AUTH.__objc_data: 0x478

```

#### AuthenticationServicesCore

>  `/System/Library/PrivateFrameworks/AuthenticationServicesCore.framework/AuthenticationServicesCore`

```diff

-620.2.4.10.7
+620.2.4.10.8
   __TEXT.__text: 0xb990c
   __TEXT.__auth_stubs: 0x21e0
   __TEXT.__objc_methlist: 0x2758

   __DATA_CONST.__objc_superrefs: 0xf0
   __DATA_CONST.__objc_arraydata: 0x10
   __AUTH_CONST.__auth_got: 0x1100
-  __AUTH_CONST.__auth_ptr: 0x6d8
+  __AUTH_CONST.__auth_ptr: 0x6f8
   __AUTH_CONST.__const: 0x56c0
   __AUTH_CONST.__cfstring: 0x1e40
   __AUTH_CONST.__objc_const: 0x7c08

```

#### DeviceIdentity

>  `/System/Library/PrivateFrameworks/DeviceIdentity.framework/DeviceIdentity`

```diff

-1015.60.1.0.0
+1015.82.2.0.0
   __TEXT.__text: 0x1b4ec
   __TEXT.__auth_stubs: 0x880
   __TEXT.__objc_methlist: 0x1f4

   __DATA_CONST.__objc_selrefs: 0x490
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
-  __DATA_CONST.__objc_arraydata: 0x448
+  __DATA_CONST.__objc_arraydata: 0x450
   __AUTH_CONST.__auth_got: 0x450
   __AUTH_CONST.__auth_ptr: 0x10
   __AUTH_CONST.__const: 0x100
CStrings:
+ "iOS Device Activator (MobileActivation-1015.82.2)"
- "iOS Device Activator (MobileActivation-1015.60.1)"

```

#### Message

>  `/System/Library/PrivateFrameworks/Message.framework/Message`

```diff

-3826.400.131.2.14
-  __TEXT.__text: 0xb7c39c
+3826.400.131.2.15
+  __TEXT.__text: 0xb7fda8
   __TEXT.__auth_stubs: 0x7df0
   __TEXT.__objc_methlist: 0x11ab4
   __TEXT.__gcc_except_tab: 0x386e8
-  __TEXT.__const: 0x4ac40
-  __TEXT.__cstring: 0x3016e
-  __TEXT.__oslogstring: 0x24300
+  __TEXT.__const: 0x4ac90
+  __TEXT.__cstring: 0x3012e
+  __TEXT.__oslogstring: 0x242a0
   __TEXT.__ustring: 0x23ca
   __TEXT.__swift5_typeref: 0x12311
   __TEXT.__swift5_capture: 0x31370
-  __TEXT.__constg_swiftt: 0xd6f8
+  __TEXT.__constg_swiftt: 0xd6e4
   __TEXT.__swift5_builtin: 0xdac
   __TEXT.__swift5_reflstr: 0xea79
   __TEXT.__swift5_fieldmd: 0x14888

   __TEXT.__swift5_protos: 0x74
   __TEXT.__swift5_mpenum: 0x7f0
   __TEXT.__unwind_info: 0x23e10
-  __TEXT.__eh_frame: 0x1e560
+  __TEXT.__eh_frame: 0x1e528
   __TEXT.__objc_classname: 0x2a4e
   __TEXT.__objc_methname: 0x2e581
   __TEXT.__objc_methtype: 0x67df
   __TEXT.__objc_stubs: 0x24660
   __DATA_CONST.__got: 0x2c80
   __DATA_CONST.__const: 0x15600
-  __DATA_CONST.__objc_classlist: 0xb38
+  __DATA_CONST.__objc_classlist: 0xb30
   __DATA_CONST.__objc_catlist: 0x68
   __DATA_CONST.__objc_protolist: 0x550
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_superrefs: 0x680
   __DATA_CONST.__objc_arraydata: 0xf58
   __AUTH_CONST.__auth_got: 0x3f10
-  __AUTH_CONST.__auth_ptr: 0x3170
-  __AUTH_CONST.__const: 0xa5e88
+  __AUTH_CONST.__auth_ptr: 0x3168
+  __AUTH_CONST.__const: 0xa5df8
   __AUTH_CONST.__cfstring: 0x184a0
-  __AUTH_CONST.__objc_const: 0x26ec0
+  __AUTH_CONST.__objc_const: 0x26e30
   __AUTH_CONST.__objc_arrayobj: 0xb88
   __AUTH_CONST.__objc_intobj: 0xa08
   __AUTH_CONST.__objc_dictobj: 0x78
-  __AUTH.__objc_data: 0x5298
-  __AUTH.__data: 0xaf60
+  __AUTH.__objc_data: 0x5248
+  __AUTH.__data: 0xafc0
   __DATA.__objc_ivar: 0x13a4
-  __DATA.__data: 0xe920
+  __DATA.__data: 0xe930
   __DATA.__crash_info: 0x40
   __DATA.__bss: 0x4e518
-  __DATA.__common: 0xf48
+  __DATA.__common: 0xf38
   __DATA_DIRTY.__objc_data: 0x1900
   __DATA_DIRTY.__data: 0x18
   __DATA_DIRTY.__bss: 0x410

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 54937
-  Symbols:   13902
-  CStrings:  17267
+  Functions: 54952
+  Symbols:   13901
+  CStrings:  17264
 
CStrings:
+ "[%.*hhx] Did mark %ld more mailboxes as sync complete."
+ "[%.*hhx] [{%.*hx}-%{sensitive,mask.mailbox}s] Did mark as sync complete."
- "[%.*hhx-%{public}s] %{sensitive,mask.mailbox}s ."
- "[%.*hhx-%{public}s] Did mark %ld more mailboxes as sync complete."
- "[%.*hhx-%{public}s] [{%.*hx}-%{sensitive,mask.mailbox}s] Did mark as sync complete."
- "_TtCV13IMAP2Behavior5State6Logger"
- "l"

```

#### MobileSafari

>  `/System/Library/PrivateFrameworks/MobileSafari.framework/MobileSafari`

```diff

-620.2.4.10.7
+620.2.4.10.8
   __TEXT.__text: 0x3a2418
   __TEXT.__auth_stubs: 0x4b50
   __TEXT.__objc_methlist: 0x12388

   __DATA_CONST.__objc_superrefs: 0x6a0
   __DATA_CONST.__objc_arraydata: 0x258
   __AUTH_CONST.__auth_got: 0x25c0
-  __AUTH_CONST.__auth_ptr: 0x2050
+  __AUTH_CONST.__auth_ptr: 0x1dd8
   __AUTH_CONST.__const: 0x13270
   __AUTH_CONST.__cfstring: 0x86e0
   __AUTH_CONST.__objc_const: 0x330d8

```

#### PasswordManagerUI

>  `/System/Library/PrivateFrameworks/PasswordManagerUI.framework/PasswordManagerUI`

```diff

-7620.2.4.10.7
+7620.2.4.10.8
   __TEXT.__text: 0x46129c
   __TEXT.__auth_stubs: 0x5e70
   __TEXT.__objc_methlist: 0x1508

   __DATA_CONST.__objc_protorefs: 0x100
   __DATA_CONST.__objc_superrefs: 0x20
   __AUTH_CONST.__auth_got: 0x2f48
-  __AUTH_CONST.__auth_ptr: 0x4418
+  __AUTH_CONST.__auth_ptr: 0x4000
   __AUTH_CONST.__const: 0x14508
   __AUTH_CONST.__cfstring: 0x4c0
   __AUTH_CONST.__objc_const: 0xa468

```

#### WebCore

>  `/System/Library/PrivateFrameworks/WebCore.framework/WebCore`

```diff

-620.2.4.10.7
-  __TEXT.__text: 0x2b2a44c
+620.2.4.10.8
+  __TEXT.__text: 0x2b2a48c
   __TEXT.__auth_stubs: 0xcfb0
   __TEXT.__objc_methlist: 0x49c4
   __TEXT.__gcc_except_tab: 0x21980
CStrings:
+ "/AppleInternal/Library/BuildRoots/bec4bd69-fa04-11ef-b2a1-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/ARM64Assembler.h"
+ "/AppleInternal/Library/BuildRoots/bec4bd69-fa04-11ef-b2a1-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/AbstractSlotVisitorInlines.h"
+ "/AppleInternal/Library/BuildRoots/bec4bd69-fa04-11ef-b2a1-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/ArgList.h"
+ "/AppleInternal/Library/BuildRoots/bec4bd69-fa04-11ef-b2a1-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/ArrayBuffer.h"
+ "/AppleInternal/Library/BuildRoots/bec4bd69-fa04-11ef-b2a1-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/ArrayBufferView.h"
+ "/AppleInternal/Library/BuildRoots/bec4bd69-fa04-11ef-b2a1-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/DataView.h"
+ "/AppleInternal/Library/BuildRoots/bec4bd69-fa04-11ef-b2a1-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/DisallowVMEntry.h"
+ "/AppleInternal/Library/BuildRoots/bec4bd69-fa04-11ef-b2a1-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/ExceptionScope.h"
+ "/AppleInternal/Library/BuildRoots/bec4bd69-fa04-11ef-b2a1-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/ExecutableAllocator.h"
+ "/AppleInternal/Library/BuildRoots/bec4bd69-fa04-11ef-b2a1-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/GenericTypedArrayViewInlines.h"
+ "/AppleInternal/Library/BuildRoots/bec4bd69-fa04-11ef-b2a1-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/IndexingHeader.h"
+ "/AppleInternal/Library/BuildRoots/bec4bd69-fa04-11ef-b2a1-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/JSArray.h"
+ "/AppleInternal/Library/BuildRoots/bec4bd69-fa04-11ef-b2a1-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/JSArrayBufferViewInlines.h"
+ "/AppleInternal/Library/BuildRoots/bec4bd69-fa04-11ef-b2a1-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/JSCPtrTag.h"
+ "/AppleInternal/Library/BuildRoots/bec4bd69-fa04-11ef-b2a1-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/JSCast.h"
+ "/AppleInternal/Library/BuildRoots/bec4bd69-fa04-11ef-b2a1-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/JSObject.h"
+ "/AppleInternal/Library/BuildRoots/bec4bd69-fa04-11ef-b2a1-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/JSObjectInlines.h"
+ "/AppleInternal/Library/BuildRoots/bec4bd69-fa04-11ef-b2a1-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/MacroAssemblerARM64.h"
+ "/AppleInternal/Library/BuildRoots/bec4bd69-fa04-11ef-b2a1-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/SecureARM64EHashPinsInlines.h"
+ "/AppleInternal/Library/BuildRoots/bec4bd69-fa04-11ef-b2a1-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/include/WebKitAdditions/EventHandlerIOSTouch.cpp"
+ "/AppleInternal/Library/BuildRoots/bec4bd69-fa04-11ef-b2a1-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/include/wtf/CheckedRef.h"
+ "/AppleInternal/Library/BuildRoots/bec4bd69-fa04-11ef-b2a1-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/include/wtf/CompletionHandler.h"
+ "/AppleInternal/Library/BuildRoots/bec4bd69-fa04-11ef-b2a1-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/include/wtf/ConcurrentPtrHashSet.h"
+ "/AppleInternal/Library/BuildRoots/bec4bd69-fa04-11ef-b2a1-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/include/wtf/Deque.h"
+ "/AppleInternal/Library/BuildRoots/bec4bd69-fa04-11ef-b2a1-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/include/wtf/JSONValues.h"
+ "/AppleInternal/Library/BuildRoots/bec4bd69-fa04-11ef-b2a1-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/include/wtf/Markable.h"
+ "/AppleInternal/Library/BuildRoots/bec4bd69-fa04-11ef-b2a1-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/include/wtf/ObjectIdentifier.h"
+ "/AppleInternal/Library/BuildRoots/bec4bd69-fa04-11ef-b2a1-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/include/wtf/Ref.h"
+ "/AppleInternal/Library/BuildRoots/bec4bd69-fa04-11ef-b2a1-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/include/wtf/RefPtr.h"
+ "/AppleInternal/Library/BuildRoots/bec4bd69-fa04-11ef-b2a1-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/include/wtf/StdLibExtras.h"
+ "/AppleInternal/Library/BuildRoots/bec4bd69-fa04-11ef-b2a1-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/include/wtf/ThreadSafeWeakHashSet.h"
+ "/AppleInternal/Library/BuildRoots/bec4bd69-fa04-11ef-b2a1-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/include/wtf/ThreadSpecific.h"
+ "/AppleInternal/Library/BuildRoots/bec4bd69-fa04-11ef-b2a1-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/include/wtf/TrailingArray.h"
+ "/AppleInternal/Library/BuildRoots/bec4bd69-fa04-11ef-b2a1-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/include/wtf/TypeCasts.h"
+ "/AppleInternal/Library/BuildRoots/bec4bd69-fa04-11ef-b2a1-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/include/wtf/cf/TypeCastsCF.h"
+ "/AppleInternal/Library/BuildRoots/bec4bd69-fa04-11ef-b2a1-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/include/wtf/text/StringBuilder.h"
+ "/AppleInternal/Library/BuildRoots/bec4bd69-fa04-11ef-b2a1-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/include/wtf/text/StringConcatenate.h"
+ "/AppleInternal/Library/BuildRoots/bec4bd69-fa04-11ef-b2a1-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/include/wtf/text/StringImpl.h"
+ "void JSC::SecureARM64EHashPins::forEachPage(Function) [Function = (lambda at /AppleInternal/Library/BuildRoots/bec4bd69-fa04-11ef-b2a1-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/SecureARM64EHashPinsInlines.h:65:17)]"
- "/AppleInternal/Library/BuildRoots/774ff07e-d344-11ef-9a16-36218cb420d5/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/ARM64Assembler.h"
- "/AppleInternal/Library/BuildRoots/774ff07e-d344-11ef-9a16-36218cb420d5/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/AbstractSlotVisitorInlines.h"
- "/AppleInternal/Library/BuildRoots/774ff07e-d344-11ef-9a16-36218cb420d5/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/ArgList.h"
- "/AppleInternal/Library/BuildRoots/774ff07e-d344-11ef-9a16-36218cb420d5/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/ArrayBuffer.h"
- "/AppleInternal/Library/BuildRoots/774ff07e-d344-11ef-9a16-36218cb420d5/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/ArrayBufferView.h"
- "/AppleInternal/Library/BuildRoots/774ff07e-d344-11ef-9a16-36218cb420d5/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/DataView.h"
- "/AppleInternal/Library/BuildRoots/774ff07e-d344-11ef-9a16-36218cb420d5/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/DisallowVMEntry.h"
- "/AppleInternal/Library/BuildRoots/774ff07e-d344-11ef-9a16-36218cb420d5/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/ExceptionScope.h"
- "/AppleInternal/Library/BuildRoots/774ff07e-d344-11ef-9a16-36218cb420d5/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/ExecutableAllocator.h"
- "/AppleInternal/Library/BuildRoots/774ff07e-d344-11ef-9a16-36218cb420d5/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/GenericTypedArrayViewInlines.h"
- "/AppleInternal/Library/BuildRoots/774ff07e-d344-11ef-9a16-36218cb420d5/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/IndexingHeader.h"
- "/AppleInternal/Library/BuildRoots/774ff07e-d344-11ef-9a16-36218cb420d5/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/JSArray.h"
- "/AppleInternal/Library/BuildRoots/774ff07e-d344-11ef-9a16-36218cb420d5/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/JSArrayBufferViewInlines.h"
- "/AppleInternal/Library/BuildRoots/774ff07e-d344-11ef-9a16-36218cb420d5/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/JSCPtrTag.h"
- "/AppleInternal/Library/BuildRoots/774ff07e-d344-11ef-9a16-36218cb420d5/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/JSCast.h"
- "/AppleInternal/Library/BuildRoots/774ff07e-d344-11ef-9a16-36218cb420d5/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/JSObject.h"
- "/AppleInternal/Library/BuildRoots/774ff07e-d344-11ef-9a16-36218cb420d5/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/JSObjectInlines.h"
- "/AppleInternal/Library/BuildRoots/774ff07e-d344-11ef-9a16-36218cb420d5/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/MacroAssemblerARM64.h"
- "/AppleInternal/Library/BuildRoots/774ff07e-d344-11ef-9a16-36218cb420d5/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/SecureARM64EHashPinsInlines.h"
- "/AppleInternal/Library/BuildRoots/774ff07e-d344-11ef-9a16-36218cb420d5/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/include/WebKitAdditions/EventHandlerIOSTouch.cpp"
- "/AppleInternal/Library/BuildRoots/774ff07e-d344-11ef-9a16-36218cb420d5/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/include/wtf/CheckedRef.h"
- "/AppleInternal/Library/BuildRoots/774ff07e-d344-11ef-9a16-36218cb420d5/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/include/wtf/CompletionHandler.h"
- "/AppleInternal/Library/BuildRoots/774ff07e-d344-11ef-9a16-36218cb420d5/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/include/wtf/ConcurrentPtrHashSet.h"
- "/AppleInternal/Library/BuildRoots/774ff07e-d344-11ef-9a16-36218cb420d5/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/include/wtf/Deque.h"
- "/AppleInternal/Library/BuildRoots/774ff07e-d344-11ef-9a16-36218cb420d5/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/include/wtf/JSONValues.h"
- "/AppleInternal/Library/BuildRoots/774ff07e-d344-11ef-9a16-36218cb420d5/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/include/wtf/Markable.h"
- "/AppleInternal/Library/BuildRoots/774ff07e-d344-11ef-9a16-36218cb420d5/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/include/wtf/ObjectIdentifier.h"
- "/AppleInternal/Library/BuildRoots/774ff07e-d344-11ef-9a16-36218cb420d5/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/include/wtf/Ref.h"
- "/AppleInternal/Library/BuildRoots/774ff07e-d344-11ef-9a16-36218cb420d5/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/include/wtf/RefPtr.h"
- "/AppleInternal/Library/BuildRoots/774ff07e-d344-11ef-9a16-36218cb420d5/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/include/wtf/StdLibExtras.h"
- "/AppleInternal/Library/BuildRoots/774ff07e-d344-11ef-9a16-36218cb420d5/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/include/wtf/ThreadSafeWeakHashSet.h"
- "/AppleInternal/Library/BuildRoots/774ff07e-d344-11ef-9a16-36218cb420d5/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/include/wtf/ThreadSpecific.h"
- "/AppleInternal/Library/BuildRoots/774ff07e-d344-11ef-9a16-36218cb420d5/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/include/wtf/TrailingArray.h"
- "/AppleInternal/Library/BuildRoots/774ff07e-d344-11ef-9a16-36218cb420d5/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/include/wtf/TypeCasts.h"
- "/AppleInternal/Library/BuildRoots/774ff07e-d344-11ef-9a16-36218cb420d5/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/include/wtf/cf/TypeCastsCF.h"
- "/AppleInternal/Library/BuildRoots/774ff07e-d344-11ef-9a16-36218cb420d5/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/include/wtf/text/StringBuilder.h"
- "/AppleInternal/Library/BuildRoots/774ff07e-d344-11ef-9a16-36218cb420d5/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/include/wtf/text/StringConcatenate.h"
- "/AppleInternal/Library/BuildRoots/774ff07e-d344-11ef-9a16-36218cb420d5/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/include/wtf/text/StringImpl.h"
- "void JSC::SecureARM64EHashPins::forEachPage(Function) [Function = (lambda at /AppleInternal/Library/BuildRoots/774ff07e-d344-11ef-9a16-36218cb420d5/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/System/Library/PrivateFrameworks/JavaScriptCore.framework/PrivateHeaders/SecureARM64EHashPinsInlines.h:65:17)]"

```


</details>

## EOF
