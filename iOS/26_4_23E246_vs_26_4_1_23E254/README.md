# 26.4 (23E246) .vs 26.4.1 (23E254)

## Inputs

- `iPhone18,1_26.4_23E246_Restore.ipsw`
- `iPhone18,1_26.4.1_23E254_Restore.ipsw`

## Kernel

### Version

| iOS | Version | Build | Date |
| :-- | :------ | :---- | :--- |
| 26.4 *(23E246)* | 25.4.0 | 12377.102.10~3 | Thu, 05Mar2026 23:59:10 PST |
| 26.4.1 *(23E254)* | 25.4.0 | 12377.102.10~3 | Thu, 05Mar2026 23:59:10 PST |

### Kexts

### ⬆️ Updated (1)

<details>
  <summary><i>View Updated</i></summary>

#### com.apple.driver.AppleIDV

>  `com.apple.driver.AppleIDV`

```diff

-8.420.0.0.0
+8.420.1.0.0
   __TEXT.__const: 0xf8
-  __TEXT.__cstring: 0x145c
+  __TEXT.__cstring: 0x145e
   __TEXT_EXEC.__text: 0x7a98
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc4

   __DATA_CONST.__mod_term_func: 0x10
   __DATA_CONST.__const: 0xe38
   __DATA_CONST.__kalloc_type: 0x80
-  UUID: 88D54FFE-A543-3E22-A644-51C2AEAB2924
+  UUID: 3FBC7D0A-4F72-32AF-91A9-F4AF8903EB6B
   Functions: 187
   Symbols:   0
   CStrings:  126
CStrings:
+ "8.420.1"
- "8.420"

```


</details>

## MachO

### ⬆️ Updated (7)

<details>
  <summary><i>View Updated</i></summary>

#### TouchSensitiveButtonHIDService

>  `/System/Library/HIDPlugins/ServicePlugins/TouchSensitiveButtonHIDService.plugin/TouchSensitiveButtonHIDService`

```diff

-9140.3.0.0.0
-  __TEXT.__text: 0x2eb8
+9140.5.0.0.0
+  __TEXT.__text: 0x2e10
   __TEXT.__auth_stubs: 0x380
   __TEXT.__objc_stubs: 0x6c0
-  __TEXT.__objc_methlist: 0x448
+  __TEXT.__objc_methlist: 0x430
   __TEXT.__const: 0xd0
-  __TEXT.__gcc_except_tab: 0x370
-  __TEXT.__cstring: 0x306
+  __TEXT.__gcc_except_tab: 0x358
+  __TEXT.__cstring: 0x2e6
   __TEXT.__oslogstring: 0x3c2
-  __TEXT.__objc_methname: 0x8f5
+  __TEXT.__objc_methname: 0x8b1
   __TEXT.__objc_classname: 0x78
-  __TEXT.__objc_methtype: 0x53b
+  __TEXT.__objc_methtype: 0x52f
   __TEXT.__unwind_info: 0x1a8
   __DATA_CONST.__auth_got: 0x1d8
   __DATA_CONST.__got: 0x68
   __DATA_CONST.__const: 0x1f0
-  __DATA_CONST.__cfstring: 0x2a0
+  __DATA_CONST.__cfstring: 0x280
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x10
-  __DATA_CONST.__objc_intobj: 0x90
+  __DATA_CONST.__objc_intobj: 0x60
   __DATA_CONST.__objc_arraydata: 0x20
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA.__objc_const: 0x8d0
-  __DATA.__objc_selrefs: 0x300
-  __DATA.__objc_ivar: 0x34
+  __DATA.__objc_const: 0x8a0
+  __DATA.__objc_selrefs: 0x2f0
+  __DATA.__objc_ivar: 0x30
   __DATA.__objc_data: 0xa0
   __DATA.__data: 0x120
   __DATA.__bss: 0x20

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 71765B2B-71B3-3E1F-BF66-504681F580BD
-  Functions: 82
-  Symbols:   309
-  CStrings:  274
+  UUID: F38FE776-8BB6-30A6-AF45-7AD86D445E8D
+  Functions: 80
+  Symbols:   306
+  CStrings:  267
 
Symbols:
+ _objc_retain_x25
- -[TouchSensitiveButtonHIDService resetDelay]
- -[TouchSensitiveButtonHIDService setResetDelay:]
- OBJC_IVAR_$_TouchSensitiveButtonHIDService._resetDelay
- _MGGetProductType
CStrings:
- "@\"NSNumber\""
- "ResetDelayAfterScanDeactivation"
- "T@\"NSNumber\",&,N,V_resetDelay"
- "_resetDelay"
- "resetDelay"
- "setResetDelay:"

```

#### UtilityExtension

>  `/System/Library/PrivateFrameworks/AppleMediaServicesUI.framework/Extensions/UtilityExtension.appex/UtilityExtension`

```diff

-7.4.25.2.3
-  __TEXT.__text: 0x45494
+7.4.25.2.4
+  __TEXT.__text: 0x45480
   __TEXT.__auth_stubs: 0x1c30
   __TEXT.__objc_stubs: 0x1440
   __TEXT.__objc_methlist: 0xb94

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: F298DE6F-87F0-3175-944D-704257B562D2
+  UUID: 3A62D5CC-952D-3AE6-9601-1BFB000450A0
   Functions: 1676
   Symbols:   223
   CStrings:  591
Functions:
~ sub_10003b6a4 : 368 -> 348

```

#### identityservicesd

>  `/System/Library/PrivateFrameworks/IDS.framework/identityservicesd.app/identityservicesd`

```diff

-1969.500.91.2.1
-  __TEXT.__text: 0xa4ecb8
+1969.500.91.2.2
+  __TEXT.__text: 0xa4ed0c
   __TEXT.__auth_stubs: 0x6eb0
   __TEXT.__objc_stubs: 0x48fa0
   __TEXT.__objc_methlist: 0x2b3ec
   __TEXT.__const: 0x6c690
-  __TEXT.__gcc_except_tab: 0x27534
+  __TEXT.__gcc_except_tab: 0x2753c
   __TEXT.__objc_methname: 0x79495
   __TEXT.__cstring: 0x57567
   __TEXT.__oslogstring: 0x81176

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 38447CD5-4F2F-3E1B-9FF0-886BFCAFBDFF
+  UUID: CC514075-D96D-3C65-A3CE-56882B2817E4
   Functions: 29134
   Symbols:   2847
   CStrings:  42742
Functions:
~ sub_100344f64 : 332 -> 416
CStrings:
+ "17:17:47"
+ "Apr  4 2026"
- "00:00:38"
- "Mar  6 2026"

```

#### eligibilityd

>  `/usr/libexec/eligibilityd`

```diff

-319.102.1.0.0
-  __TEXT.__text: 0x3e24c
+319.102.3.0.0
+  __TEXT.__text: 0x3e8b0
   __TEXT.__auth_stubs: 0x1840
-  __TEXT.__objc_stubs: 0x2640
-  __TEXT.__objc_methlist: 0x1d84
-  __TEXT.__const: 0x2020
-  __TEXT.__cstring: 0x618d
+  __TEXT.__objc_stubs: 0x2680
+  __TEXT.__objc_methlist: 0x1d94
+  __TEXT.__const: 0x2030
+  __TEXT.__cstring: 0x61c0
   __TEXT.__swift5_typeref: 0x822
-  __TEXT.__oslogstring: 0x2382
+  __TEXT.__oslogstring: 0x24da
   __TEXT.__constg_swiftt: 0x76c
   __TEXT.__swift5_reflstr: 0x673
   __TEXT.__swift5_fieldmd: 0x678

   __TEXT.__swift5_assocty: 0xf0
   __TEXT.__swift5_proto: 0x1c4
   __TEXT.__swift5_types: 0xd4
-  __TEXT.__objc_methname: 0x2ebf
+  __TEXT.__objc_methname: 0x2eef
   __TEXT.__objc_classname: 0x55f
-  __TEXT.__objc_methtype: 0x78a
+  __TEXT.__objc_methtype: 0x798
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_protos: 0x14
   __TEXT.__swift5_capture: 0x14
   __TEXT.__gcc_except_tab: 0x378
-  __TEXT.__unwind_info: 0xcd0
+  __TEXT.__unwind_info: 0xcd8
   __TEXT.__eh_frame: 0xb20
   __DATA_CONST.__auth_got: 0xc30
   __DATA_CONST.__got: 0x370

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x40
   __DATA_CONST.__objc_superrefs: 0xc0
-  __DATA_CONST.__objc_intobj: 0x288
-  __DATA_CONST.__objc_arraydata: 0xa480
-  __DATA_CONST.__objc_arrayobj: 0x28b0
+  __DATA_CONST.__objc_intobj: 0x2b8
+  __DATA_CONST.__objc_arraydata: 0xa488
+  __DATA_CONST.__objc_arrayobj: 0x28c8
   __DATA_CONST.__objc_dictobj: 0x9470
   __DATA.__objc_const: 0x3548
-  __DATA.__objc_selrefs: 0xaf8
+  __DATA.__objc_selrefs: 0xb08
   __DATA.__objc_ivar: 0xc4
   __DATA.__objc_data: 0xd40
   __DATA.__data: 0x1188

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: C41DC9AD-0F5A-3698-8614-22B9F368E34A
-  Functions: 1248
+  UUID: A357009C-7A0A-3892-9FD1-F68A62FB5C2C
+  Functions: 1249
   Symbols:   595
-  CStrings:  2432
+  CStrings:  2439
 
Functions:
~ sub_10003c5d4 : 396 -> 428
+ sub_10003c780
CStrings:
+ "%s: Detected a China Location device incorrectly returning eligible. isGreymatter: %d, hasBillingAccount: %d, chinaBilling: %d, chinaLocation: %d"
+ "%s: Detected a ChinaSKU device incorrectly returning eligible. isGreymatter: %d, isStrontium: %d"
+ "%s: Input objects not found when checking Greymatter Billing: %@ , Region : %@ , CountryLocation :%@"
+ "-[EligibilityEngine _checkDomains:computedAnswer:]"
+ "18:26:14"
+ "319.102.3"
+ "@32@0:8@16@24"
+ "Apr  3 2026"
+ "_checkDomains:computedAnswer:"
+ "dictionary"
- "00:59:38"
- "319.102.1"
- "Feb 26 2026"

```

#### idcredd

>  `/usr/libexec/idcredd`

```diff

-8.420.0.0.0
-  __TEXT.__text: 0x1b294c
-  __TEXT.__auth_stubs: 0x3ed0
+8.420.1.0.0
+  __TEXT.__text: 0x1b2d00
+  __TEXT.__auth_stubs: 0x3ec0
   __TEXT.__objc_stubs: 0x2040
   __TEXT.__objc_methlist: 0x8fc
-  __TEXT.__const: 0x54e8
-  __TEXT.__constg_swiftt: 0x21d8
-  __TEXT.__swift5_typeref: 0x2724
+  __TEXT.__const: 0x54d8
+  __TEXT.__constg_swiftt: 0x21d0
+  __TEXT.__swift5_typeref: 0x272e
   __TEXT.__swift5_builtin: 0x1a4
-  __TEXT.__swift5_reflstr: 0x1677
+  __TEXT.__swift5_reflstr: 0x1697
   __TEXT.__swift5_assocty: 0x1b0
-  __TEXT.__cstring: 0xd6a9
-  __TEXT.__oslogstring: 0xa6b8
-  __TEXT.__swift5_fieldmd: 0x15d8
+  __TEXT.__cstring: 0xd6f9
+  __TEXT.__oslogstring: 0xa718
+  __TEXT.__swift5_fieldmd: 0x15f0
   __TEXT.__swift5_proto: 0x15c
   __TEXT.__swift5_types: 0x1d8
   __TEXT.__objc_classname: 0x7b4

   __TEXT.__objc_methtype: 0xf93
   __TEXT.__swift5_mpenum: 0x10
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__unwind_info: 0x5448
+  __TEXT.__unwind_info: 0x5430
   __TEXT.__eh_frame: 0x13bc8
-  __DATA_CONST.__auth_got: 0x1f70
+  __DATA_CONST.__auth_got: 0x1f68
   __DATA_CONST.__got: 0x1688
   __DATA_CONST.__auth_ptr: 0x9d8
-  __DATA_CONST.__const: 0x5a98
+  __DATA_CONST.__const: 0x5a70
   __DATA_CONST.__objc_classlist: 0x140
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA.__objc_const: 0x26d0
   __DATA.__objc_selrefs: 0xae8
   __DATA.__objc_data: 0xc78
-  __DATA.__data: 0x40e0
+  __DATA.__data: 0x40e8
   __DATA.__bss: 0x1fd0
   __DATA.__common: 0xf0
   - /AppleInternal/Library/Frameworks/TapToRadarKit.framework/TapToRadarKit

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 1FC2939E-E101-3352-98E4-C316D3F714FE
-  Functions: 4058
+  UUID: FA417BB4-DAB3-39AA-BB6D-F1779DF70C2B
+  Functions: 4060
   Symbols:   1863
-  CStrings:  2124
+  CStrings:  2125
 
Symbols:
+ _objc_retain_x11
- _objc_retain_x10
CStrings:
+ "PresentmentResponseBuilder: Using credential document type %s for known terminal issuer (%s)"
+ "buildProposal(for:documentRequest:requiredPublicKeyIdentifier:sessionReaderAuthenticationPolicy:readerAuthCertificateData:readerMetadata:readerAnalytics:knownIssuer:knownTerminalIssuers:)"
+ "findProposals(documentRequests:requiredPublicKeyIdentifier:readerAuthenticationPolicy:readerAuthCertificateData:readerMetadata:readerAnalytics:readerAuthError:knownIssuer:knownTerminalIssuers:)"
+ "preparePresentmentData(selection:proposal:knownTerminalIssuers:)"
- "buildProposal(for:documentRequest:requiredPublicKeyIdentifier:sessionReaderAuthenticationPolicy:readerAuthCertificateData:readerMetadata:readerAnalytics:knownIssuer:)"
- "findProposals(documentRequests:requiredPublicKeyIdentifier:readerAuthenticationPolicy:readerAuthCertificateData:readerMetadata:readerAnalytics:readerAuthError:knownIssuer:)"
- "preparePresentmentData(selection:proposal:)"

```

#### remindd

>  `/usr/libexec/remindd`

```diff

-3973.0.0.0.0
-  __TEXT.__text: 0x81285c
+3973.81.0.0.0
+  __TEXT.__text: 0x8127f4
   __TEXT.__auth_stubs: 0x87c0
   __TEXT.__objc_stubs: 0x1b760
   __TEXT.__objc_methlist: 0xa8e0
-  __TEXT.__const: 0x28768
+  __TEXT.__const: 0x287f8
   __TEXT.__objc_methname: 0x27a01
   __TEXT.__objc_classname: 0x60b6
   __TEXT.__objc_methtype: 0x4267
   __TEXT.__gcc_except_tab: 0x2540
   __TEXT.__cstring: 0x180b7
-  __TEXT.__oslogstring: 0x5ea40
+  __TEXT.__oslogstring: 0x5e8f0
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__swift5_typeref: 0x14048
+  __TEXT.__swift5_typeref: 0x14042
   __TEXT.__swift5_fieldmd: 0xa4e8
   __TEXT.__constg_swiftt: 0xcb94
   __TEXT.__swift5_builtin: 0x3ac

   __TEXT.__swift5_protos: 0x2d4
   __TEXT.__swift5_proto: 0x18e8
   __TEXT.__swift5_types: 0xafc
-  __TEXT.__swift_as_entry: 0x1a4
-  __TEXT.__swift_as_ret: 0x204
+  __TEXT.__swift_as_entry: 0x1a8
+  __TEXT.__swift_as_ret: 0x208
   __TEXT.__swift5_mpenum: 0xc4
-  __TEXT.__unwind_info: 0xff30
-  __TEXT.__eh_frame: 0x1f82c
+  __TEXT.__unwind_info: 0xff40
+  __TEXT.__eh_frame: 0x1f89c
   __DATA_CONST.__auth_got: 0x43f0
   __DATA_CONST.__got: 0x3418
   __DATA_CONST.__auth_ptr: 0x2820

   __DATA.__objc_selrefs: 0x7b00
   __DATA.__objc_ivar: 0x480
   __DATA.__objc_data: 0x8450
-  __DATA.__data: 0x1e590
+  __DATA.__data: 0x1e630
   __DATA.__objc_stublist: 0x38
   __DATA.__bss: 0x237f0
   __DATA.__common: 0x9f0

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 2EAB57B6-B94A-373F-BC5C-3A3854E36219
-  Functions: 22210
+  UUID: B425A9AE-385D-3C4E-AF8D-0DF01350BA56
+  Functions: 22212
   Symbols:   4183
-  CStrings:  12688
+  CStrings:  12684
 
CStrings:
+ "RDUrgentAlarmConsumer: updateLastBannerPresentationDate END {reminderID: %{public}@, lastBannerPresentationDate: %{public}s}"
+ "RDUrgentAlarmConsumer: updateLastBannerPresentationDate FAIL {reminderID: %{public}@, error: %s}"
+ "RDUrgentAlarmConsumer: updateLastBannerPresentationDate START {reminderID: %{public}@, lastBannerPresentationDate: %{public}s}"
+ "TimeDataSourceAlarms: Failed to get REMReminder, REMAlarm or triggerEvent from cdTrigger -- skipping {cdTrigger: %@}"
- "RDUrgentAlarmConsumer: updateLastBannerPresentationDates END"
- "RDUrgentAlarmConsumer: updateLastBannerPresentationDates START\n     reminderCount: %ld"
- "RDUrgentAlarmConsumer: updateLastBannerPresentationDates {reminderID: %{public}@, lastBannerPresentationDate: %{public}s}"
- "RDUrgentAlarmConsumer: updateLastBannerPresentationDates | Save failed: %{public}s}"
- "TimeDataSourceAlarms: Failed to get REMReminder, REMAlarm from cdTrigger -- skipping {cdTrigger: %{public}@}"
- "TimeDataSourceAlarms: Failed to get fireDate from trigger -- skipping {cdTrigger: %{public}@}"
- "TimeDataSourceAlarms: Failed to unwrap cdAlarm or cdReminder -- skipping {cdTrigger: %{public}@}"
- "TimeDataSourceAlarms: Finished fetching alarms\n      input: %{public}*ld\n     result: %{public}*ld\n    skipped: %{public}*ld"

```

#### seserviced

>  `/usr/libexec/seserviced`

```diff

-64.24.0.0.0
-  __TEXT.__text: 0x437d2c
+64.26.0.0.0
+  __TEXT.__text: 0x437d7c
   __TEXT.__auth_stubs: 0x4b70
   __TEXT.__delay_stubs: 0x40
   __TEXT.__delay_helper: 0x33c

   __TEXT.__const: 0x11a98
   __TEXT.__gcc_except_tab: 0x346c
   __TEXT.__objc_methname: 0x17359
-  __TEXT.__oslogstring: 0x2b7e0
+  __TEXT.__oslogstring: 0x2b7f0
   __TEXT.__cstring: 0x1e5e9
   __TEXT.__objc_classname: 0x2bba
   __TEXT.__objc_methtype: 0x765f

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 93B896C5-C7BD-3C81-BD35-A2C66E2EF8A0
+  UUID: 5B913762-3F85-3217-9BF9-AF3B3FABB787
   Functions: 11920
   Symbols:   2368
   CStrings:  11837
Functions:
~ sub_100004aa0 : 1980 -> 2052
~ sub_1000052c8 -> sub_100005310 : 8 -> 92
~ sub_1000052d0 -> sub_10000536c : 84 -> 8
CStrings:
+ "Returning occupied keySlot %u from %lu slots"
+ "Returning short lived keySlot %u from %lu slots"
+ "iOS (26.4) - SecureElementService-64.26"
- "Returning occupied keySlot %u"
- "Returning short lived keySlot %u"
- "iOS (26.4) - SecureElementService-64.24"

```


</details>

### iBoot

| iOS | Version |
| :-- | :------ |
| 26.4 *(23E246)* | mBoot-18000.102.4 |
| 26.4.1 *(23E254)* | mBoot-18000.102.4 |

## DSC

### WebKit

| iOS | Version |
| :-- | :------ |
| 26.4 *(23E246)* | 624.1.16.10.6 |
| 26.4.1 *(23E254)* | 624.1.16.10.6 |

### Dylibs

#### ⬆️ Updated (12)

<details>
  <summary><i>View Updated</i></summary>

#### AppleMediaServices

>  `/System/Library/PrivateFrameworks/AppleMediaServices.framework/AppleMediaServices`

```diff

-9.4.28.2.1
-  __TEXT.__text: 0x7df8d0
+9.4.28.2.3
+  __TEXT.__text: 0x7df9d8
   __TEXT.__auth_stubs: 0x4cd0
   __TEXT.__objc_methlist: 0x2369c
   __TEXT.__const: 0x5f1b0

   __TEXT.__swift5_capture: 0x3b90
   __TEXT.__swift5_mpenum: 0x84
   __TEXT.__swift5_protos: 0x108
-  __TEXT.__oslogstring: 0x31f68
-  __TEXT.__gcc_except_tab: 0x5ab4
+  __TEXT.__oslogstring: 0x31fd6
+  __TEXT.__gcc_except_tab: 0x5a2c
   __TEXT.__ustring: 0x1b2
-  __TEXT.__unwind_info: 0x13c10
+  __TEXT.__unwind_info: 0x13c18
   __TEXT.__eh_frame: 0x185c4
   __TEXT.__objc_classname: 0x5b69
   __TEXT.__objc_methname: 0x48705

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 954A40FE-99C9-33FD-9B19-9D09E9631E1F
-  Functions: 28741
-  Symbols:   56806
-  CStrings:  26162
+  UUID: A045B8BC-EA64-3545-B97A-B1DB1B0D0D60
+  Functions: 28742
+  Symbols:   56808
+  CStrings:  26163
 
Symbols:
+ _getSSSilentEnrollmentContextClass
Functions:
~ +[AMSCardEnrollmentPaymentSessionTask _performPaymentSessionWithBag:isForParentalVerification:] : 2724 -> 2768
+ _getSSSilentEnrollmentContextClass
CStrings:
+ "%{public}@: [%{public}@] Silent-enrollment payment session failed due to missing payment session URL bag key."

```

#### AppleMediaServicesUI

>  `/System/Library/PrivateFrameworks/AppleMediaServicesUI.framework/AppleMediaServicesUI`

```diff

-7.4.25.2.3
-  __TEXT.__text: 0x1e702c
-  __TEXT.__auth_stubs: 0x4640
-  __TEXT.__objc_methlist: 0x10844
-  __TEXT.__const: 0xcdb4
+7.4.25.2.4
+  __TEXT.__text: 0x1ede2c
+  __TEXT.__auth_stubs: 0x47f0
+  __TEXT.__objc_methlist: 0x10994
+  __TEXT.__const: 0xd394
   __TEXT.__gcc_except_tab: 0x1a08
-  __TEXT.__oslogstring: 0xa1db
-  __TEXT.__cstring: 0xd09d
+  __TEXT.__oslogstring: 0xa2ab
+  __TEXT.__cstring: 0xd3dd
   __TEXT.__dlopen_cstrs: 0xe35
   __TEXT.__ustring: 0x13a
-  __TEXT.__swift5_typeref: 0xf2fc
-  __TEXT.__constg_swiftt: 0x4ff0
-  __TEXT.__swift5_reflstr: 0x2655
-  __TEXT.__swift5_assocty: 0x1048
-  __TEXT.__swift5_fieldmd: 0x2b14
+  __TEXT.__swift5_typeref: 0xfb22
+  __TEXT.__constg_swiftt: 0x52bc
+  __TEXT.__swift5_reflstr: 0x27c5
+  __TEXT.__swift5_assocty: 0x10e0
+  __TEXT.__swift5_fieldmd: 0x2d00
   __TEXT.__swift5_builtin: 0x1b8
-  __TEXT.__swift5_capture: 0x133c
-  __TEXT.__swift5_proto: 0x4e0
-  __TEXT.__swift5_types: 0x3ac
-  __TEXT.__swift5_protos: 0x2c
+  __TEXT.__swift5_capture: 0x13e0
+  __TEXT.__swift5_proto: 0x500
+  __TEXT.__swift5_types: 0x3cc
+  __TEXT.__swift5_protos: 0x30
   __TEXT.__swift_as_entry: 0x194
   __TEXT.__swift_as_ret: 0x1d4
   __TEXT.__swift5_mpenum: 0x40
-  __TEXT.__unwind_info: 0x8c68
-  __TEXT.__eh_frame: 0x5de0
-  __TEXT.__objc_classname: 0x36e4
-  __TEXT.__objc_methname: 0x2707f
-  __TEXT.__objc_methtype: 0x8221
-  __TEXT.__objc_stubs: 0x1bd60
-  __DATA_CONST.__got: 0x1a70
-  __DATA_CONST.__const: 0x3d38
-  __DATA_CONST.__objc_classlist: 0xa08
+  __TEXT.__unwind_info: 0x8e00
+  __TEXT.__eh_frame: 0x5e40
+  __TEXT.__objc_classname: 0x3814
+  __TEXT.__objc_methname: 0x2768f
+  __TEXT.__objc_methtype: 0x8521
+  __TEXT.__objc_stubs: 0x1c0e0
+  __DATA_CONST.__got: 0x1ae8
+  __DATA_CONST.__const: 0x3db0
+  __DATA_CONST.__objc_classlist: 0xa20
   __DATA_CONST.__objc_catlist: 0xa0
-  __DATA_CONST.__objc_protolist: 0x390
+  __DATA_CONST.__objc_protolist: 0x3a8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x8ce0
-  __DATA_CONST.__objc_protorefs: 0x100
+  __DATA_CONST.__objc_selrefs: 0x8e18
+  __DATA_CONST.__objc_protorefs: 0x110
   __DATA_CONST.__objc_superrefs: 0x680
   __DATA_CONST.__objc_arraydata: 0x330
-  __AUTH_CONST.__auth_got: 0x2330
-  __AUTH_CONST.__const: 0x7fb0
-  __AUTH_CONST.__cfstring: 0xb020
-  __AUTH_CONST.__objc_const: 0x1fe58
+  __AUTH_CONST.__auth_got: 0x2408
+  __AUTH_CONST.__const: 0x83a0
+  __AUTH_CONST.__cfstring: 0xb080
+  __AUTH_CONST.__objc_const: 0x20288
   __AUTH_CONST.__objc_intobj: 0x420
   __AUTH_CONST.__objc_dictobj: 0x230
   __AUTH_CONST.__objc_doubleobj: 0x60
   __AUTH_CONST.__objc_arrayobj: 0x108
-  __AUTH.__objc_data: 0x7210
-  __AUTH.__data: 0x4f08
-  __DATA.__objc_ivar: 0x10e0
-  __DATA.__data: 0x63c0
-  __DATA.__objc_stublist: 0x8
-  __DATA.__bss: 0xa440
-  __DATA.__common: 0x248
+  __AUTH.__objc_data: 0x75a0
+  __AUTH.__data: 0x4fc8
+  __DATA.__objc_ivar: 0x10ec
+  __DATA.__data: 0x6620
+  __DATA.__objc_stublist: 0x10
+  __DATA.__bss: 0xa7e0
+  __DATA.__common: 0x258
   __DATA_DIRTY.__objc_data: 0xea8
   __DATA_DIRTY.__data: 0x88
   __DATA_DIRTY.__bss: 0x48

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: B33C9D2F-4CDC-38E8-85B2-994FC127DCA9
-  Functions: 13518
-  Symbols:   25974
-  CStrings:  11440
+  UUID: 06E19747-3F5B-37CC-BF11-686B381FCF89
+  Functions: 13697
+  Symbols:   26203
+  CStrings:  11532
 
Symbols:
+ -[AMSUIWebCameraReaderPageModel ctaButtons]
+ -[AMSUIWebCameraReaderPageModel manualCaptureImagePadding]
+ -[AMSUIWebCameraReaderPageModel outputImageWidth]
+ -[AMSUIWebCameraReaderPageModel setCtaButtons:]
+ -[AMSUIWebCameraReaderPageModel setManualCaptureImagePadding:]
+ -[AMSUIWebCameraReaderPageModel setOutputImageWidth:]
+ _AVCaptureSessionPresetPhoto
+ _AVLayerVideoGravityResizeAspectFill
+ _CGImageGetHeight
+ _CGImageGetWidth
+ _OBJC_CLASS_$_AMSUIWebAgeVerificationInfoViewControllerProvider
+ _OBJC_CLASS_$_AMSUIWebManualCaptureViewControllerProvider
+ _OBJC_CLASS_$_AVCaptureDeviceInput
+ _OBJC_CLASS_$_AVCaptureDeviceRotationCoordinator
+ _OBJC_CLASS_$_AVCapturePhotoOutput
+ _OBJC_CLASS_$_AVCapturePhotoSettings
+ _OBJC_CLASS_$_AVCaptureSession
+ _OBJC_CLASS_$_AVCaptureVideoPreviewLayer
+ _OBJC_CLASS_$__TtC20AppleMediaServicesUI23PhotoCaptureCoordinator
+ _OBJC_IVAR_$_AMSUIWebCameraReaderPageModel._ctaButtons
+ _OBJC_IVAR_$_AMSUIWebCameraReaderPageModel._manualCaptureImagePadding
+ _OBJC_IVAR_$_AMSUIWebCameraReaderPageModel._outputImageWidth
+ _OBJC_METACLASS_$_AMSUIWebAgeVerificationInfoViewControllerProvider
+ _OBJC_METACLASS_$_AMSUIWebManualCaptureViewControllerProvider
+ _OBJC_METACLASS_$__TtC20AppleMediaServicesUI23PhotoCaptureCoordinator
+ _OBJC_METACLASS_$__TtC20AppleMediaServicesUI30ManualCaptureHostingController
+ _OBJC_METACLASS_$__TtCV20AppleMediaServicesUIP33_EAEACBFDC3A9AAA71A62BB0B70D2DDF630CameraPreviewViewRepresentable17CameraPreviewView
+ __CLASS_METHODS_AMSUIWebAgeVerificationInfoViewControllerProvider
+ __CLASS_METHODS_AMSUIWebManualCaptureViewControllerProvider
+ __DATA_AMSUIWebAgeVerificationInfoViewControllerProvider
+ __DATA_AMSUIWebManualCaptureViewControllerProvider
+ __DATA__TtC20AppleMediaServicesUI23PhotoCaptureCoordinator
+ __DATA__TtC20AppleMediaServicesUI30ManualCaptureHostingController
+ __DATA__TtCV20AppleMediaServicesUIP33_EAEACBFDC3A9AAA71A62BB0B70D2DDF630CameraPreviewViewRepresentable17CameraPreviewView
+ __INSTANCE_METHODS_AMSUIWebAgeVerificationInfoViewControllerProvider
+ __INSTANCE_METHODS_AMSUIWebManualCaptureViewControllerProvider
+ __INSTANCE_METHODS__TtC20AppleMediaServicesUI23PhotoCaptureCoordinator
+ __INSTANCE_METHODS__TtC20AppleMediaServicesUI30ManualCaptureHostingController
+ __INSTANCE_METHODS__TtCV20AppleMediaServicesUIP33_EAEACBFDC3A9AAA71A62BB0B70D2DDF630CameraPreviewViewRepresentable17CameraPreviewView
+ __IVARS__TtC20AppleMediaServicesUI23PhotoCaptureCoordinator
+ __IVARS__TtC20AppleMediaServicesUI30ManualCaptureHostingController
+ __IVARS__TtCV20AppleMediaServicesUIP33_EAEACBFDC3A9AAA71A62BB0B70D2DDF630CameraPreviewViewRepresentable17CameraPreviewView
+ __METACLASS_DATA_AMSUIWebAgeVerificationInfoViewControllerProvider
+ __METACLASS_DATA_AMSUIWebManualCaptureViewControllerProvider
+ __METACLASS_DATA__TtC20AppleMediaServicesUI23PhotoCaptureCoordinator
+ __METACLASS_DATA__TtC20AppleMediaServicesUI30ManualCaptureHostingController
+ __METACLASS_DATA__TtCV20AppleMediaServicesUIP33_EAEACBFDC3A9AAA71A62BB0B70D2DDF630CameraPreviewViewRepresentable17CameraPreviewView
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_AVCapturePhotoCaptureDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_AVCapturePhotoCaptureDelegate
+ __OBJC_$_PROTOCOL_REFS_AVCapturePhotoCaptureDelegate
+ __OBJC_LABEL_PROTOCOL_$_AVCapturePhotoCaptureDelegate
+ __OBJC_PROTOCOL_$_AVCapturePhotoCaptureDelegate
+ __PROTOCOLS__TtC20AppleMediaServicesUI23PhotoCaptureCoordinator
+ __PROTOCOLS__TtC20AppleMediaServicesUI23PhotoCaptureCoordinator.7
+ __PROTOCOLS__TtC20AppleMediaServicesUI30ManualCaptureHostingController
+ __PROTOCOLS__TtC20AppleMediaServicesUI30ManualCaptureHostingController.19
+ ___110-[AMSUIParentalVerificationApplePayTask _promiseToRequestWalletDataUsingSession:bag:accountParameters:bundle:]_block_invoke
+ ___41-[AMSUIWebCameraReaderPageModel loadPage]_block_invoke
+ ___41-[AMSUIWebCameraReaderPageModel loadPage]_block_invoke.61
+ ___52-[AMSUIParentalVerificationApplePayTask performTask]_block_invoke_2
+ ___52-[AMSUIWebCameraReaderViewController _setupInfoView]_block_invoke
+ ___block_descriptor_40_e8_32s_e48_"AMSBinaryPromise"24?0"NSNumber"8"NSError"16ls32l8
+ ___block_descriptor_40_e8_32s_e55_v24?0"AMSPaymentVerificationTokenResult"8"NSError"16ls32l8
+ ___block_descriptor_48_e8_32s40s_e48_"AMSBinaryPromise"24?0"NSNumber"8"NSError"16ls32l8s40l8
+ ___block_descriptor_80_e8_32s40s48s56s64s72s_e30_"AMSPromise"16?0"NSString"8ls32l8s40l8s48l8s56l8s64l8s72l8
+ _associated conformance 20AppleMediaServicesUI17ManualCaptureViewV05SwiftD00G0AA4BodyAdEP_AdE
+ _associated conformance 20AppleMediaServicesUI18CornerBracketShape33_EAEACBFDC3A9AAA71A62BB0B70D2DDF6LLV05SwiftD00G0AaE10Animatable
+ _associated conformance 20AppleMediaServicesUI18CornerBracketShape33_EAEACBFDC3A9AAA71A62BB0B70D2DDF6LLV05SwiftD00G0AaE4View
+ _associated conformance 20AppleMediaServicesUI18CornerBracketShape33_EAEACBFDC3A9AAA71A62BB0B70D2DDF6LLV05SwiftD010AnimatableAA0Q4DataAeFP_AE16VectorArithmetic
+ _associated conformance 20AppleMediaServicesUI18CornerBracketShape33_EAEACBFDC3A9AAA71A62BB0B70D2DDF6LLV05SwiftD04ViewAA4BodyAeFP_AeF
+ _associated conformance 20AppleMediaServicesUI29AgeVerificationInfoViewButtonVs12IdentifiableAA2IDsADP_SH
+ _associated conformance 20AppleMediaServicesUI30CameraPreviewViewRepresentable33_EAEACBFDC3A9AAA71A62BB0B70D2DDF6LLV05SwiftD006UIViewH0AaE0G0
+ _associated conformance 20AppleMediaServicesUI30CameraPreviewViewRepresentable33_EAEACBFDC3A9AAA71A62BB0B70D2DDF6LLV05SwiftD00G0AA4BodyAeFP_AeF
+ _get_enum_tag_for_layout_string Ieg_Sg
+ _get_witness_table 7SwiftUI14GeometryReaderVyAA6VStackVyAA9TupleViewVyAA15ModifiedContentVyAIyAIy018AppleMediaServicesB0013CameraPreviewG13Representable33_EAEACBFDC3A9AAA71A62BB0B70D2DDF6LLVAA30_SafeAreaRegionsIgnoringLayoutVGAA12_FrameLayoutVGAA16_OverlayModifierVyAIyAIyAIyAA011StrokeShapeG0VyAJ18CornerBracketShapeALLLVAA5ColorVAA05EmptyG0VGAA14_PaddingLayoutVGA4_GA4_GGG_AJ019AgeVerificationInfoG0VtGGGAA0G0HPyHC.50
+ _get_witness_table qd0__7SwiftUI4ViewHD3_AaBPAAE11safeAreaBar4edge9alignment7spacing7contentQrAA12VerticalEdgeO_AA19HorizontalAlignmentV12CoreGraphics7CGFloatVSgqd__yXEtAaBRd__lFQOyAA15ModifiedContentVyARyAcAE20scrollBounceBehavior_4axesQrAA06ScrolluV0V_AA4AxisO3SetVtFQOyAA0xC0VyARyAA6VStackVyAA05TupleC0VyARyAA4TextVAA16_FixedSizeLayoutVG_A9_AA6ButtonVyA6_GSgAA6SpacerVtGGAA14_PaddingLayoutVGG_Qo_AA16_FlexFrameLayoutVGAA24_BackgroundStyleModifierVyAA5ColorVGG_ARyA2_yAA7ForEachVySay018AppleMediaServicesB0019AgeVerificationInfoC6ButtonVGSiAA012_ConditionalS0VyAcAE11buttonStyleyQrqd__AA20PrimitiveButtonStyleRd__lFQOyARyA11_yARyA6_AA12_FrameLayoutVGGAA30_EnvironmentKeyWritingModifierVyAA17ButtonBorderShapeVGG_AA25GlassProminentButtonStyleVQo_AcAEA40_yQrqd__AAA41_Rd__lFQOyA51__AA16GlassButtonStyleVQo_GGGA19_GSgQo_HO.22
+ _keypath_get_selector_videoRotationAngleForHorizonLevelPreview
+ _objc_msgSend$CGImageRepresentation
+ _objc_msgSend$addInput:
+ _objc_msgSend$addOutput:
+ _objc_msgSend$canAddInput:
+ _objc_msgSend$canAddOutput:
+ _objc_msgSend$capturePhotoWithSettings:delegate:
+ _objc_msgSend$connection
+ _objc_msgSend$createControllerWithModel:context:
+ _objc_msgSend$createControllerWithPrimaryLabel:secondaryLabel:linkTitle:linkAction:ctaButtons:context:
+ _objc_msgSend$ctaButtons
+ _objc_msgSend$defaultDeviceWithMediaType:
+ _objc_msgSend$drawInRect:
+ _objc_msgSend$initWithCGImage:scale:orientation:
+ _objc_msgSend$initWithDevice:error:
+ _objc_msgSend$initWithDevice:previewLayer:
+ _objc_msgSend$initWithSession:
+ _objc_msgSend$isVideoRotationAngleSupported:
+ _objc_msgSend$manualCaptureImagePadding
+ _objc_msgSend$metadataOutputRectOfInterestForRect:
+ _objc_msgSend$outputImageWidth
+ _objc_msgSend$setFlashMode:
+ _objc_msgSend$setLivePhotoCaptureEnabled:
+ _objc_msgSend$setManualCaptureImagePadding:
+ _objc_msgSend$setOutputImageWidth:
+ _objc_msgSend$setSessionPreset:
+ _objc_msgSend$setVideoGravity:
+ _objc_msgSend$setVideoRotationAngle:
+ _objc_msgSend$startRunning
+ _objc_msgSend$stopRunning
+ _objc_msgSend$videoRotationAngleForHorizonLevelPreview
+ _objectdestroy.13Tm
+ _swift_arrayDestroy
+ _symbolic $s20AppleMediaServicesUI23PhotoCaptureCoordinatorC8DelegateP
+ _symbolic IeyB_
+ _symbolic Say_____G 20AppleMediaServicesUI29AgeVerificationInfoViewButtonV
+ _symbolic Say_____GSg 20AppleMediaServicesUI29AgeVerificationInfoViewButtonV
+ _symbolic So15AVCaptureDeviceCSg
+ _symbolic So16AVCaptureSessionC
+ _symbolic So20AVCapturePhotoOutputC
+ _symbolic So21AMSUIWebClientContextC
+ _symbolic So26AVCaptureVideoPreviewLayerCSgXw
+ _symbolic So34AVCaptureDeviceRotationCoordinatorC
+ _symbolic So34AVCaptureDeviceRotationCoordinatorCSg
+ _symbolic So34AVCaptureDeviceRotationCoordinatorCSgz_Xx
+ _symbolic SuSg
+ _symbolic _____ 20AppleMediaServicesUI17ManualCaptureViewV
+ _symbolic _____ 20AppleMediaServicesUI18CornerBracketShape33_EAEACBFDC3A9AAA71A62BB0B70D2DDF6LLV
+ _symbolic _____ 20AppleMediaServicesUI23PhotoCaptureCoordinatorC
+ _symbolic _____ 20AppleMediaServicesUI29AgeVerificationInfoViewButtonV
+ _symbolic _____ 20AppleMediaServicesUI30CameraPreviewViewRepresentable33_EAEACBFDC3A9AAA71A62BB0B70D2DDF6LLV
+ _symbolic _____ 20AppleMediaServicesUI30CameraPreviewViewRepresentable33_EAEACBFDC3A9AAA71A62BB0B70D2DDF6LLV0efG0C
+ _symbolic _____ 20AppleMediaServicesUI30ManualCaptureHostingControllerC
+ _symbolic _____ 20AppleMediaServicesUI35ManualCaptureViewControllerProviderC
+ _symbolic _____ 7SwiftUI17ButtonBorderShapeV
+ _symbolic _____SgXw 20AppleMediaServicesUI30ManualCaptureHostingControllerC
+ _symbolic ______pSgXw 20AppleMediaServicesUI23PhotoCaptureCoordinatorC8DelegateP
+ _symbolic _____yAAyAAy__________G_____G_____yAAyAAyAAy_____y_______________G_____GAMGAMGGG 7SwiftUI15ModifiedContentV 018AppleMediaServicesB030CameraPreviewViewRepresentable33_EAEACBFDC3A9AAA71A62BB0B70D2DDF6LLV AA30_SafeAreaRegionsIgnoringLayoutV AA06_FrameX0V AA16_OverlayModifierV AA011StrokeShapeJ0V AD18CornerBracketShapeAFLLV AA5ColorV AA05EmptyJ0V AA08_PaddingX0V
+ _symbolic _____yAAyAAy_____y_______________G_____GAGGAGG 7SwiftUI15ModifiedContentV AA15StrokeShapeViewV 018AppleMediaServicesB0013CornerBracketF033_EAEACBFDC3A9AAA71A62BB0B70D2DDF6LLV AA5ColorV AA05EmptyG0V AA14_PaddingLayoutV
+ _symbolic _____yAAy_____y_______________G_____GAGG 7SwiftUI15ModifiedContentV AA15StrokeShapeViewV 018AppleMediaServicesB0013CornerBracketF033_EAEACBFDC3A9AAA71A62BB0B70D2DDF6LLV AA5ColorV AA05EmptyG0V AA14_PaddingLayoutV
+ _symbolic _____yAAy_____y_____yAAy_____y_____yAAy__________G_AG_____yAEGSg_____tGG_____GG_Qo______G_____y_____GG 7SwiftUI15ModifiedContentV AA4ViewPAAE20scrollBounceBehavior_4axesQrAA06ScrollgH0V_AA4AxisO3SetVtFQO AA0jE0V AA6VStackV AA05TupleE0V AA4TextV AA16_FixedSizeLayoutV AA6ButtonV AA6SpacerV AA08_PaddingR0V AA010_FlexFrameR0V AA24_BackgroundStyleModifierV AA5ColorV
+ _symbolic _____y_____G 10Foundation24NSKeyValueObservedChangeV 12CoreGraphics7CGFloatV
+ _symbolic _____y_____G 7SwiftUI19UIHostingControllerC 018AppleMediaServicesB017ManualCaptureViewV
+ _symbolic _____y_____G 7SwiftUI30_EnvironmentKeyWritingModifierV AA17ButtonBorderShapeV
+ _symbolic _____y_____G s23_ContiguousArrayStorageC 20AppleMediaServicesUI29AgeVerificationInfoViewButtonV
+ _symbolic _____y__________G 7SwiftUI10_ShapeViewV 018AppleMediaServicesB0013CornerBracketC033_EAEACBFDC3A9AAA71A62BB0B70D2DDF6LLV AA15ForegroundStyleV
+ _symbolic _____y__________G 7SwiftUI15ModifiedContentV AA4TextV AA12_FrameLayoutV
+ _symbolic _____y_______________G 7SwiftUI15StrokeShapeViewV 018AppleMediaServicesB0013CornerBracketD033_EAEACBFDC3A9AAA71A62BB0B70D2DDF6LLV AA5ColorV AA05EmptyE0V
+ _symbolic _____y___________ySay_____GSi_____y_____y_____y_____yAGy__________GG_____y_____GG______Qo______yAP______Qo_GGG 7SwiftUI13_VariadicViewO4TreeV AA13_VStackLayoutV AA7ForEachV 018AppleMediaServicesB0019AgeVerificationInfoD6ButtonV AA19_ConditionalContentV AA0D0PAAE11buttonStyleyQrqd__AA09PrimitivepT0Rd__lFQO AA08ModifiedR0V AA0P0V AA4TextV AA06_FrameG0V AA30_EnvironmentKeyWritingModifierV AA0P11BorderShapeV AA014GlassProminentpT0V ApAEAQyQrqd__AaRRd__lFQO AA05GlasspT0V
+ _symbolic _____y_____yAAy__________GG_____y_____GG 7SwiftUI15ModifiedContentV AA6ButtonV AA4TextV AA12_FrameLayoutV AA30_EnvironmentKeyWritingModifierV AA0E11BorderShapeV
+ _symbolic _____y_____yAAy_____y_____yAAy_____y_____yAAy__________G_AG_____yAEGSg_____tGG_____GG_Qo______G_____y_____GG_AAyACy_____ySay_____GSi_____y_____yAAyAHyAAyAE_____GG_____y_____GG______Qo______yA6_______Qo_GGGANGSgQo_ 7SwiftUI4ViewPAAE11safeAreaBar4edge9alignment7spacing7contentQrAA12VerticalEdgeO_AA19HorizontalAlignmentV12CoreGraphics7CGFloatVSgqd__yXEtAaBRd__lFQO AA15ModifiedContentV AcAE20scrollBounceBehavior_4axesQrAA06ScrolluV0V_AA4AxisO3SetVtFQO AA0xC0V AA6VStackV AA05TupleC0V AA4TextV AA16_FixedSizeLayoutV AA6ButtonV AA6SpacerV AA14_PaddingLayoutV AA16_FlexFrameLayoutV AA24_BackgroundStyleModifierV AA5ColorV AA7ForEachV 018AppleMediaServicesB0019AgeVerificationInfoC6ButtonV AA012_ConditionalS0V AcAE11buttonStyleyQrqd__AA20PrimitiveButtonStyleRd__lFQO AA12_FrameLayoutV AA30_EnvironmentKeyWritingModifierV AA17ButtonBorderShapeV AA25GlassProminentButtonStyleV AcAEA28_yQrqd__AAA29_Rd__lFQO AA16GlassButtonStyleV
+ _symbolic _____y_____yAByABy_____y_______________G_____GAHGAHGG 7SwiftUI16_OverlayModifierV AA15ModifiedContentV AA15StrokeShapeViewV 018AppleMediaServicesB0013CornerBracketH033_EAEACBFDC3A9AAA71A62BB0B70D2DDF6LLV AA5ColorV AA05EmptyI0V AA14_PaddingLayoutV
+ _symbolic _____y_____ySay_____GSi_____y_____y_____y_____yAFy__________GG_____y_____GG______Qo______yAO______Qo_GGG 7SwiftUI6VStackV AA7ForEachV 018AppleMediaServicesB029AgeVerificationInfoViewButtonV AA19_ConditionalContentV AA0L0PAAE11buttonStyleyQrqd__AA09PrimitivemQ0Rd__lFQO AA08ModifiedO0V AA0M0V AA4TextV AA12_FrameLayoutV AA30_EnvironmentKeyWritingModifierV AA0M11BorderShapeV AA014GlassProminentmQ0V AlAEAMyQrqd__AaNRd__lFQO AA05GlassmQ0V
+ _symbolic _____y_____y__________GG 7SwiftUI6ButtonV AA15ModifiedContentV AA4TextV AA12_FrameLayoutV
+ _symbolic _____y_____y_______________G_____G 7SwiftUI15ModifiedContentV AA15StrokeShapeViewV 018AppleMediaServicesB0013CornerBracketF033_EAEACBFDC3A9AAA71A62BB0B70D2DDF6LLV AA5ColorV AA05EmptyG0V AA14_PaddingLayoutV
+ _symbolic _____y_____y_____yAAy__________GG_____y_____GG______Qo_ 7SwiftUI4ViewPAAE11buttonStyleyQrqd__AA015PrimitiveButtonE0Rd__lFQO AA15ModifiedContentV AA0G0V AA4TextV AA12_FrameLayoutV AA30_EnvironmentKeyWritingModifierV AA0G11BorderShapeV AA014GlassProminentgE0V
+ _symbolic _____y_____y_____yAAy__________GG_____y_____GG______Qo_ 7SwiftUI4ViewPAAE11buttonStyleyQrqd__AA015PrimitiveButtonE0Rd__lFQO AA15ModifiedContentV AA0G0V AA4TextV AA12_FrameLayoutV AA30_EnvironmentKeyWritingModifierV AA0G11BorderShapeV AA05GlassgE0V
+ _symbolic _____y_____y_____yAAy__________G_AF_____yADGSg_____tGG_____G 7SwiftUI15ModifiedContentV AA6VStackV AA9TupleViewV AA4TextV AA16_FixedSizeLayoutV AA6ButtonV AA6SpacerV AA08_PaddingK0V
+ _symbolic _____y_____y_____yAAy_____y_____yAAy__________G_AG_____yAEGSg_____tGG_____GG_Qo______G 7SwiftUI15ModifiedContentV AA4ViewPAAE20scrollBounceBehavior_4axesQrAA06ScrollgH0V_AA4AxisO3SetVtFQO AA0jE0V AA6VStackV AA05TupleE0V AA4TextV AA16_FixedSizeLayoutV AA6ButtonV AA6SpacerV AA08_PaddingR0V AA010_FlexFrameR0V
+ _symbolic _____y_____y_____ySay_____GSi_____y_____yAAy_____yAAy__________GG_____y_____GG______Qo______yAO______Qo_GGG_____G 7SwiftUI15ModifiedContentV AA6VStackV AA7ForEachV 018AppleMediaServicesB029AgeVerificationInfoViewButtonV AA012_ConditionalD0V AA0N0PAAE11buttonStyleyQrqd__AA09PrimitiveoR0Rd__lFQO AA0O0V AA4TextV AA12_FrameLayoutV AA30_EnvironmentKeyWritingModifierV AA0O11BorderShapeV AA014GlassProminentoR0V AnAEAOyQrqd__AaPRd__lFQO AA05GlassoR0V AA08_PaddingV0V
+ _symbolic _____y_____y_____ySay_____GSi_____y_____yAAy_____yAAy__________GG_____y_____GG______Qo______yAO______Qo_GGG_____GSg 7SwiftUI15ModifiedContentV AA6VStackV AA7ForEachV 018AppleMediaServicesB029AgeVerificationInfoViewButtonV AA012_ConditionalD0V AA0N0PAAE11buttonStyleyQrqd__AA09PrimitiveoR0Rd__lFQO AA0O0V AA4TextV AA12_FrameLayoutV AA30_EnvironmentKeyWritingModifierV AA0O11BorderShapeV AA014GlassProminentoR0V AnAEAOyQrqd__AaPRd__lFQO AA05GlassoR0V AA08_PaddingV0V
+ _symbolic _____y_____y_____y_____yABy__________GG_____y_____GG______Qo______yAK______Qo_G 7SwiftUI19_ConditionalContentV AA4ViewPAAE11buttonStyleyQrqd__AA015PrimitiveButtonG0Rd__lFQO AA08ModifiedD0V AA0I0V AA4TextV AA12_FrameLayoutV AA30_EnvironmentKeyWritingModifierV AA0I11BorderShapeV AA014GlassProminentiG0V AeAEAFyQrqd__AaGRd__lFQO AA0tiG0V
+ _symbolic _____y_____y_____y_____yABy__________GG_____y_____GG______Qo______yAK______Qo__G 7SwiftUI19_ConditionalContentV7StorageO AA4ViewPAAE11buttonStyleyQrqd__AA015PrimitiveButtonH0Rd__lFQO AA08ModifiedD0V AA0J0V AA4TextV AA12_FrameLayoutV AA30_EnvironmentKeyWritingModifierV AA0J11BorderShapeV AA014GlassProminentjH0V AgAEAHyQrqd__AaIRd__lFQO AA0ujH0V
+ _symbolic _____y_____y_____y_____yABy__________G_AG_____yAEGSg_____tGG_____GG 7SwiftUI10ScrollViewV AA15ModifiedContentV AA6VStackV AA05TupleD0V AA4TextV AA16_FixedSizeLayoutV AA6ButtonV AA6SpacerV AA08_PaddingL0V
+ _symbolic _____y_____y_____y_____yADyADy__________G_____G_____yADyADyADy_____y_______________G_____GAPGAPGGG______tGGG 7SwiftUI14GeometryReaderV AA6VStackV AA9TupleViewV AA15ModifiedContentV 018AppleMediaServicesB0013CameraPreviewG13Representable33_EAEACBFDC3A9AAA71A62BB0B70D2DDF6LLV AA30_SafeAreaRegionsIgnoringLayoutV AA12_FrameLayoutV AA16_OverlayModifierV AA011StrokeShapeG0V AJ18CornerBracketShapeALLLV AA5ColorV AA05EmptyG0V AA14_PaddingLayoutV AJ019AgeVerificationInfoG0V
+ _type_layout_string 20AppleMediaServicesUI17ManualCaptureViewV
+ _type_layout_string 20AppleMediaServicesUI18CornerBracketShape33_EAEACBFDC3A9AAA71A62BB0B70D2DDF6LLV
+ _type_layout_string 20AppleMediaServicesUI29AgeVerificationInfoViewButtonV
+ _type_layout_string 20AppleMediaServicesUI30CameraPreviewViewRepresentable33_EAEACBFDC3A9AAA71A62BB0B70D2DDF6LLV
- -[AMSUIWebCameraReaderViewController _setupImageWidthForIDCardInReader:]
- GCC_except_table24
- GCC_except_table26
- _OBJC_CLASS_$__TtC20AppleMediaServicesUI41AgeVerificationInfoViewControllerProvider
- _OBJC_METACLASS_$__TtC20AppleMediaServicesUI41AgeVerificationInfoViewControllerProvider
- __CLASS_METHODS__TtC20AppleMediaServicesUI41AgeVerificationInfoViewControllerProvider
- __DATA__TtC20AppleMediaServicesUI41AgeVerificationInfoViewControllerProvider
- __INSTANCE_METHODS__TtC20AppleMediaServicesUI41AgeVerificationInfoViewControllerProvider
- __METACLASS_DATA__TtC20AppleMediaServicesUI41AgeVerificationInfoViewControllerProvider
- ___72-[AMSUIWebCameraReaderViewController _setupImageWidthForIDCardInReader:]_block_invoke
- ___72-[AMSUIWebCameraReaderViewController _setupImageWidthForIDCardInReader:]_block_invoke.98
- ___block_descriptor_48_e8_32s40s_e33_v28?0"NSNumber"8B16"NSError"20ls32l8s40l8
- _get_witness_table 7SwiftUI15ModifiedContentVyACyACyAA6VStackVyAA9TupleViewVyACyAA4TextVAA16_FixedSizeLayoutVG_AlA6ButtonVyAIGSgAA6SpacerVtGGAA010_FlexFrameK0VGAA24_BackgroundStyleModifierVyAA5ColorVGGAA08_PaddingK0VGAA0G0HPA1_AAA5_HPAwAA5_HPAtAA5_HPyHC_AvA0gR0HPyHCHC_A0_AAA6_HPyHCHC_A3_AAA6_HPyHCHC.3
- _objc_msgSend$_setupImageWidthForIDCardInReader:
- _objc_msgSend$createControllerWithPrimaryLabel:secondaryLabel:linkTitle:linkAction:
- _symbolic ______pSg So22AMSUIWebActionRunnableP
- _symbolic _____yAAyAAy_____y_____yAAy__________G_AF_____yADGSg_____tGG_____G_____y_____GG_____G 7SwiftUI15ModifiedContentV AA6VStackV AA9TupleViewV AA4TextV AA16_FixedSizeLayoutV AA6ButtonV AA6SpacerV AA010_FlexFrameK0V AA24_BackgroundStyleModifierV AA5ColorV AA08_PaddingK0V
- _symbolic _____yAAy_____y_____yAAy__________G_AF_____yADGSg_____tGG_____G_____y_____GG 7SwiftUI15ModifiedContentV AA6VStackV AA9TupleViewV AA4TextV AA16_FixedSizeLayoutV AA6ButtonV AA6SpacerV AA010_FlexFrameK0V AA24_BackgroundStyleModifierV AA5ColorV
- _symbolic _____y_____y_____yAAy__________G_AF_____yADGSg_____tGG_____G 7SwiftUI15ModifiedContentV AA6VStackV AA9TupleViewV AA4TextV AA16_FixedSizeLayoutV AA6ButtonV AA6SpacerV AA010_FlexFrameK0V
CStrings:
+ "%{public}@: [%{public}@] Task finished successfully"
+ "%{public}@: [%{public}@] Task finished with error: %{public}@"
+ "%{public}@Bag does not contain image padding"
+ "%{public}@Could not read padding from bag. Error: %{public}@"
+ "%{public}@Got padding: %f"
+ "@\"AMSBinaryPromise\"24@?0@\"NSNumber\"8@\"NSError\"16"
+ "@64@0:8@16@24@32@?40@48@56"
+ "AMSUIWebAgeVerificationInfoViewControllerProvider"
+ "AMSUIWebManualCaptureViewControllerProvider"
+ "AVCapturePhotoCaptureDelegate"
+ "AppleMediaServicesUI.CameraPreviewView"
+ "AppleMediaServicesUI.ManualCaptureHostingController"
+ "AppleMediaServicesUI.PhotoCaptureCoordinator"
+ "AppleMediaServicesUI/AMSUIWebManualCaptureView.swift"
+ "CGImageRepresentation"
+ "Could not crop image because preview layer was nil. Will continue uncropped."
+ "Could not encode image as HEIC"
+ "Could not get CGImage representation"
+ "Could not resize image"
+ "Could not setup capture session. Error: "
+ "Delegate was nil"
+ "Failed to crop image"
+ "Finishing with error: "
+ "Finishing with image data"
+ "Finishing without error or result"
+ "No suitable card in wallet"
+ "Received delegate callback from photo capture"
+ "T@\"NSArray\",&,N,V_ctaButtons"
+ "T@\"NSNumber\",&,N,V_manualCaptureImagePadding"
+ "T@\"NSNumber\",&,N,V_outputImageWidth"
+ "Video device was not available."
+ "_TtC20AppleMediaServicesUI23PhotoCaptureCoordinator"
+ "_TtC20AppleMediaServicesUI30ManualCaptureHostingController"
+ "_TtCV20AppleMediaServicesUIP33_EAEACBFDC3A9AAA71A62BB0B70D2DDF630CameraPreviewViewRepresentable17CameraPreviewView"
+ "_ctaButtons"
+ "_manualCaptureImagePadding"
+ "_outputImageWidth"
+ "addInput:"
+ "addOutput:"
+ "age-assurance-id-image-padding-manual"
+ "age-assurance-id-image-width-manual"
+ "canAddInput:"
+ "canAddOutput:"
+ "captureCoordinator"
+ "captureOutput:didCapturePhotoForResolvedSettings:"
+ "captureOutput:didFinishCaptureForResolvedSettings:error:"
+ "captureOutput:didFinishCapturingDeferredPhotoProxy:error:"
+ "captureOutput:didFinishProcessingLivePhotoToMovieFileAtURL:duration:photoDisplayTime:resolvedSettings:error:"
+ "captureOutput:didFinishProcessingPhoto:error:"
+ "captureOutput:didFinishProcessingPhotoSampleBuffer:previewPhotoSampleBuffer:resolvedSettings:bracketSettings:error:"
+ "captureOutput:didFinishProcessingRawPhotoSampleBuffer:previewPhotoSampleBuffer:resolvedSettings:bracketSettings:error:"
+ "captureOutput:didFinishRecordingLivePhotoMovieForEventualFileAtURL:resolvedSettings:"
+ "captureOutput:willBeginCaptureForResolvedSettings:"
+ "captureOutput:willCapturePhotoForResolvedSettings:"
+ "capturePhotoWithSettings:delegate:"
+ "createControllerWithModel:context:"
+ "createControllerWithPrimaryLabel:secondaryLabel:linkTitle:linkAction:ctaButtons:context:"
+ "ctaButtons"
+ "defaultDeviceWithMediaType:"
+ "drawInRect:"
+ "initWithCGImage:scale:orientation:"
+ "initWithDevice:error:"
+ "initWithDevice:previewLayer:"
+ "initWithSession:"
+ "isVideoRotationAngleSupported:"
+ "manualCaptureImagePadding"
+ "metadataOutputRectOfInterestForRect:"
+ "outputImageWidth"
+ "outputWidth"
+ "previewLayer"
+ "rotationAngle"
+ "rotationCoordinator"
+ "rotationObservation"
+ "setCtaButtons:"
+ "setFlashMode:"
+ "setLivePhotoCaptureEnabled:"
+ "setManualCaptureImagePadding:"
+ "setOutputImageWidth:"
+ "setSessionPreset:"
+ "setVideoGravity:"
+ "setVideoRotationAngle:"
+ "startRunning"
+ "stopRunning"
+ "v32@0:8@\"AVCapturePhotoOutput\"16@\"AVCaptureResolvedPhotoSettings\"24"
+ "v40@0:8@\"AVCapturePhotoOutput\"16@\"AVCaptureDeferredPhotoProxy\"24@\"NSError\"32"
+ "v40@0:8@\"AVCapturePhotoOutput\"16@\"AVCapturePhoto\"24@\"NSError\"32"
+ "v40@0:8@\"AVCapturePhotoOutput\"16@\"AVCaptureResolvedPhotoSettings\"24@\"NSError\"32"
+ "v40@0:8@\"AVCapturePhotoOutput\"16@\"NSURL\"24@\"AVCaptureResolvedPhotoSettings\"32"
+ "v64@0:8@\"AVCapturePhotoOutput\"16^{opaqueCMSampleBuffer=}24^{opaqueCMSampleBuffer=}32@\"AVCaptureResolvedPhotoSettings\"40@\"AVCaptureBracketedStillImageSettings\"48@\"NSError\"56"
+ "v64@0:8@16^{opaqueCMSampleBuffer=}24^{opaqueCMSampleBuffer=}32@40@48@56"
+ "v96@0:8@\"AVCapturePhotoOutput\"16@\"NSURL\"24{?=qiIq}32{?=qiIq}56@\"AVCaptureResolvedPhotoSettings\"80@\"NSError\"88"
+ "v96@0:8@16@24{?=qiIq}32{?=qiIq}56@80@88"
+ "videoRotationAngleForHorizonLevelPreview"
+ "\xf0!"
- "%{public}@Setting width %lu on reader"
- "Can not continue with payment request"
- "_TtC20AppleMediaServicesUI41AgeVerificationInfoViewControllerProvider"
- "_setupImageWidthForIDCardInReader:"
- "createControllerWithPrimaryLabel:secondaryLabel:linkTitle:linkAction:"
- "\xe1"

```

#### AppleMediaServicesUIDynamic

>  `/System/Library/PrivateFrameworks/AppleMediaServicesUIDynamic.framework/AppleMediaServicesUIDynamic`

```diff

-7.4.25.2.3
-  __TEXT.__text: 0xb5e4c
+7.4.25.2.4
+  __TEXT.__text: 0xb5e38
   __TEXT.__auth_stubs: 0x2e60
   __TEXT.__objc_methlist: 0x19a4
   __TEXT.__const: 0x91a0

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 31C18A90-0993-32DA-80F3-63D74351EFE4
+  UUID: 04BC3444-5DD2-3D93-9BF2-DA02940D3012
   Functions: 5939
   Symbols:   5687
   CStrings:  2076
Functions:
~ sub_1cc622e78 -> sub_1cc62ae78 : 368 -> 348

```

#### CallHistory

>  `/System/Library/PrivateFrameworks/CallHistory.framework/CallHistory`

```diff

   __TEXT.__auth_stubs: 0x2420
   __TEXT.__objc_methlist: 0x3a0c
   __TEXT.__const: 0x1e578
-  __TEXT.__cstring: 0x4064
+  __TEXT.__cstring: 0x4074
   __TEXT.__oslogstring: 0x5e19
   __TEXT.__gcc_except_tab: 0x854
   __TEXT.__dlopen_cstrs: 0x147

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 803D489B-79C0-3321-B24A-1BA8DF415313
+  UUID: E2BC0E7F-FE24-317C-AFA9-404821244807
   Functions: 12301
   Symbols:   7862
   CStrings:  3485
CStrings:
+ "106.500.211.2.12~32"
- "106.500.211.2.12~1"

```

#### CoreIDCred

>  `/System/Library/PrivateFrameworks/CoreIDCred.framework/CoreIDCred`

```diff

-8.420.0.0.0
+8.420.1.0.0
   __TEXT.__text: 0x3e9b4
   __TEXT.__auth_stubs: 0xbf0
   __TEXT.__objc_methlist: 0x21c4
-  __TEXT.__const: 0x3650
+  __TEXT.__const: 0x3660
   __TEXT.__cstring: 0x1a4b
   __TEXT.__oslogstring: 0x3e6c
   __TEXT.__gcc_except_tab: 0x14

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 192923A3-D238-3E2A-BE78-7D966EA8F1B7
+  UUID: A1E3564D-8141-37DC-BAE2-DF1C554525FB
   Functions: 2144
   Symbols:   3399
   CStrings:  1490

```

#### GenerativeFunctionsFoundation

>  `/System/Library/PrivateFrameworks/GenerativeFunctionsFoundation.framework/GenerativeFunctionsFoundation`

```diff

-222.35.5.0.0
-  __TEXT.__text: 0x6da40
-  __TEXT.__auth_stubs: 0x1680
+222.35.7.0.0
+  __TEXT.__text: 0x6ddac
+  __TEXT.__auth_stubs: 0x16a0
   __TEXT.__const: 0x10960
   __TEXT.__swift5_typeref: 0x3952
-  __TEXT.__cstring: 0x254d
+  __TEXT.__cstring: 0x257d
   __TEXT.__constg_swiftt: 0x2e28
   __TEXT.__swift5_reflstr: 0x1063
   __TEXT.__swift5_fieldmd: 0x2cdc

   __TEXT.__swift_as_entry: 0x28
   __TEXT.__swift_as_ret: 0x24
   __TEXT.__swift5_capture: 0x58
-  __TEXT.__unwind_info: 0x2a00
+  __TEXT.__unwind_info: 0x2a08
   __TEXT.__eh_frame: 0x348c
   __TEXT.__objc_methname: 0xa7
   __TEXT.__objc_stubs: 0x120

   __DATA_CONST.__const: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x48
-  __AUTH_CONST.__auth_got: 0xb48
+  __AUTH_CONST.__auth_got: 0xb58
   __AUTH_CONST.__const: 0x7bb0
   __AUTH.__data: 0x458
   __DATA.__data: 0x2908

   - /System/Library/PrivateFrameworks/AppleIntelligenceReporting.framework/AppleIntelligenceReporting
   - /System/Library/PrivateFrameworks/FeatureFlags.framework/FeatureFlags
   - /System/Library/PrivateFrameworks/PromptKit.framework/PromptKit
+  - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftCore.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: C77EC6A2-5D66-3728-A4B5-ACD327D93818
-  Functions: 4852
-  Symbols:   119
-  CStrings:  215
+  UUID: 5660DC24-C2ED-3881-9A22-7EC6C4C7D5F8
+  Functions: 4859
+  Symbols:   121
+  CStrings:  216
 
Symbols:
+ _MobileGestalt_copy_regionCode_obj
+ _MobileGestalt_get_current_device
CStrings:
+ "OS_ELIGIBILITY_CONTEXT_COUNTRY_POLICY"

```

#### Message

>  `/System/Library/PrivateFrameworks/Message.framework/Message`

```diff

-3864.500.181.2.2
-  __TEXT.__text: 0xacc6d4
+3864.500.181.2.3
+  __TEXT.__text: 0xacc754
   __TEXT.__auth_stubs: 0x7d80
   __TEXT.__objc_methlist: 0x140ec
-  __TEXT.__gcc_except_tab: 0x393c4
+  __TEXT.__gcc_except_tab: 0x393e0
   __TEXT.__const: 0x69bcc
   __TEXT.__cstring: 0x2e414
-  __TEXT.__oslogstring: 0x26ed0
+  __TEXT.__oslogstring: 0x26f10
   __TEXT.__ustring: 0x23ca
   __TEXT.__dlopen_cstrs: 0xae
   __TEXT.__swift5_typeref: 0x1018c

   __TEXT.__objc_classname: 0x3b2a
   __TEXT.__objc_methname: 0x30805
   __TEXT.__objc_methtype: 0x710a
-  __TEXT.__objc_stubs: 0x262e0
+  __TEXT.__objc_stubs: 0x26300
   __DATA_CONST.__got: 0x2e80
   __DATA_CONST.__const: 0x152e0
   __DATA_CONST.__objc_classlist: 0xb38

   - /usr/lib/swift/libswift_DarwinFoundation2.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 76B13C9C-582E-3C4E-9026-949CF0A96C78
+  UUID: B65C3CE8-7520-33DC-AE8C-C228C40E664E
   Functions: 46126
-  Symbols:   38571
-  CStrings:  20532
+  Symbols:   38572
+  CStrings:  20533
 
Symbols:
+ _objc_msgSend$persistenceDidAddNewMessages:
Functions:
~ _insertDAMessages : 3016 -> 3144
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~CMaougCYr__TwaUffOdSIAuGLdqeHasfZnZfCBA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/System/Library/PrivateFrameworks/EmailCore.framework/Headers/ECFlagChangeMessageActionResults.h"
+ "/AppleInternal/Library/BuildRoots/4~CMaougCYr__TwaUffOdSIAuGLdqeHasfZnZfCBA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/System/Library/PrivateFrameworks/EmailCore.framework/Headers/ECTransferMessageAction.h"
+ "/AppleInternal/Library/BuildRoots/4~CMaougCYr__TwaUffOdSIAuGLdqeHasfZnZfCBA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/System/Library/PrivateFrameworks/EmailCore.framework/Headers/ECTransferMessageActionResults.h"
+ "Dispatching persistenceDidAddNewMessages for %lu Exchange messages"
- "/AppleInternal/Library/BuildRoots/4~CKTdugCGgDo_KERRVhMPCB84ve-so6GiD_-mxBE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/System/Library/PrivateFrameworks/EmailCore.framework/Headers/ECFlagChangeMessageActionResults.h"
- "/AppleInternal/Library/BuildRoots/4~CKTdugCGgDo_KERRVhMPCB84ve-so6GiD_-mxBE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/System/Library/PrivateFrameworks/EmailCore.framework/Headers/ECTransferMessageAction.h"
- "/AppleInternal/Library/BuildRoots/4~CKTdugCGgDo_KERRVhMPCB84ve-so6GiD_-mxBE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/System/Library/PrivateFrameworks/EmailCore.framework/Headers/ECTransferMessageActionResults.h"

```

#### MetricMeasurement

>  `/System/Library/PrivateFrameworks/MetricMeasurement.framework/MetricMeasurement`

```diff

-297.100.11.0.0
-  __TEXT.__text: 0x1e538
+297.102.1.0.0
+  __TEXT.__text: 0x1e520
   __TEXT.__auth_stubs: 0x850
   __TEXT.__objc_methlist: 0x28bc
   __TEXT.__const: 0x268

   __TEXT.__gcc_except_tab: 0x6f4
   __TEXT.__oslogstring: 0x9d5
   __TEXT.__ustring: 0x34
-  __TEXT.__unwind_info: 0x9c8
+  __TEXT.__unwind_info: 0x9c0
   __TEXT.__objc_classname: 0x5c5
   __TEXT.__objc_methname: 0x4b7a
-  __TEXT.__objc_methtype: 0x10f2
+  __TEXT.__objc_methtype: 0x10e7
   __TEXT.__objc_stubs: 0x4200
   __DATA_CONST.__got: 0x288
   __DATA_CONST.__const: 0x6a0

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libpmsample.dylib
   - /usr/lib/libsysmon.dylib
-  UUID: 9B8AD42D-E52F-3476-B622-736BF847A16D
+  UUID: 96B0BD67-8740-3ACA-9DEF-818D424696BB
   Functions: 870
   Symbols:   3257
   CStrings:  1889
Functions:
~ -[MXMSystemProbe _pollSystemLoadInformationWithData:] : 136 -> 112
CStrings:
+ "v40@0:8@16Q24^{vm_statistics64=IIIIQQQQQQQQQIIQQQQIIIIQQ}32"
- "v40@0:8@16Q24^{vm_statistics64=IIIIQQQQQQQQQIIQQQQIIIIQQQQQQQQQQQQQ}32"

```

#### TextInputUI

>  `/System/Library/PrivateFrameworks/TextInputUI.framework/TextInputUI`

```diff

-9126.4.27.0.0
-  __TEXT.__text: 0xe9dfc
+9126.4.27.1.107
+  __TEXT.__text: 0xe9e0c
   __TEXT.__auth_stubs: 0x2b60
   __TEXT.__objc_methlist: 0xc62c
   __TEXT.__const: 0x2170

   __TEXT.__swift5_typeref: 0xe12
   __TEXT.__oslogstring: 0x2dce
   __TEXT.__swift5_capture: 0x2a0
-  __TEXT.__cstring: 0x97fd
+  __TEXT.__cstring: 0x9b98
   __TEXT.__constg_swiftt: 0xb44
   __TEXT.__swift5_reflstr: 0x468
   __TEXT.__swift5_fieldmd: 0x4cc

   __DATA_CONST.__objc_selrefs: 0x8770
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x360
-  __DATA_CONST.__objc_arraydata: 0x588
+  __DATA_CONST.__objc_arraydata: 0x708
   __AUTH_CONST.__auth_got: 0x15b8
   __AUTH_CONST.__const: 0x1628
-  __AUTH_CONST.__cfstring: 0xb6e0
+  __AUTH_CONST.__cfstring: 0xbce0
   __AUTH_CONST.__objc_const: 0x13938
   __AUTH_CONST.__objc_intobj: 0x360
-  __AUTH_CONST.__objc_arrayobj: 0x1f8
+  __AUTH_CONST.__objc_arrayobj: 0x210
   __AUTH_CONST.__objc_doubleobj: 0x170
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_floatobj: 0xe0

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 1730A9C3-BE2C-34BA-8CF3-F1A07B666B81
+  UUID: 379058DE-6B6B-313B-9189-775E1AAF521C
   Functions: 4902
   Symbols:   16361
-  CStrings:  10177
+  CStrings:  10273
 
Symbols:
+ __TUIKeyboardTrackingLogger.8619
+ __TUIKeyboardTrackingLogger.log.8625
+ __TUIKeyboardTrackingLogger.onceToken.8623
+ ___Block_byref_object_copy_.12898
+ ___Block_byref_object_copy_.5607
+ ___Block_byref_object_copy_.5951
+ ___Block_byref_object_copy_.8360
+ ___Block_byref_object_copy_.9981
+ ___Block_byref_object_dispose_.12899
+ ___Block_byref_object_dispose_.5608
+ ___Block_byref_object_dispose_.5952
+ ___Block_byref_object_dispose_.8361
+ ___Block_byref_object_dispose_.9982
+ ____TUIKeyboardTrackingLogger_block_invoke.8628
+ ___block_literal_global.10.10940
+ ___block_literal_global.10083
+ ___block_literal_global.10617
+ ___block_literal_global.10945
+ ___block_literal_global.11130
+ ___block_literal_global.11471
+ ___block_literal_global.11628
+ ___block_literal_global.11904
+ ___block_literal_global.12908
+ ___block_literal_global.13148
+ ___block_literal_global.13646
+ ___block_literal_global.18.8415
+ ___block_literal_global.20.10080
+ ___block_literal_global.20.9543
+ ___block_literal_global.22.9545
+ ___block_literal_global.4.13171
+ ___block_literal_global.5430
+ ___block_literal_global.5640
+ ___block_literal_global.6.11132
+ ___block_literal_global.6061
+ ___block_literal_global.61.13146
+ ___block_literal_global.633
+ ___block_literal_global.644
+ ___block_literal_global.6748
+ ___block_literal_global.6870
+ ___block_literal_global.7133
+ ___block_literal_global.7403
+ ___block_literal_global.7800
+ ___block_literal_global.7971
+ ___block_literal_global.8419
+ ___block_literal_global.8624
+ ___block_literal_global.8826
+ ___block_literal_global.9269
+ ___block_literal_global.9456
+ ___block_literal_global.9536
+ ___block_literal_global.9618
+ ___block_literal_global.9990
+ _sharedInstance.__instance.10941
+ _sharedInstance.onceToken.10079
+ _sharedInstance.onceToken.10939
+ _sharedInstance.onceToken.6869
+ _shouldGenerateCandidateForContext:.onceToken.9996
- __TUIKeyboardTrackingLogger.8550
- __TUIKeyboardTrackingLogger.log.8556
- __TUIKeyboardTrackingLogger.onceToken.8554
- ___Block_byref_object_copy_.12836
- ___Block_byref_object_copy_.5547
- ___Block_byref_object_copy_.5882
- ___Block_byref_object_copy_.8291
- ___Block_byref_object_copy_.9919
- ___Block_byref_object_dispose_.12837
- ___Block_byref_object_dispose_.5548
- ___Block_byref_object_dispose_.5883
- ___Block_byref_object_dispose_.8292
- ___Block_byref_object_dispose_.9920
- ____TUIKeyboardTrackingLogger_block_invoke.8559
- ___block_literal_global.10.10878
- ___block_literal_global.10021
- ___block_literal_global.10555
- ___block_literal_global.10883
- ___block_literal_global.11068
- ___block_literal_global.11409
- ___block_literal_global.11566
- ___block_literal_global.11842
- ___block_literal_global.12846
- ___block_literal_global.13086
- ___block_literal_global.13601
- ___block_literal_global.18.8346
- ___block_literal_global.20.10018
- ___block_literal_global.20.9481
- ___block_literal_global.22.9483
- ___block_literal_global.4.13109
- ___block_literal_global.486
- ___block_literal_global.497
- ___block_literal_global.5370
- ___block_literal_global.5580
- ___block_literal_global.5992
- ___block_literal_global.6.11070
- ___block_literal_global.61.13084
- ___block_literal_global.6679
- ___block_literal_global.6801
- ___block_literal_global.7064
- ___block_literal_global.7334
- ___block_literal_global.7731
- ___block_literal_global.7902
- ___block_literal_global.8350
- ___block_literal_global.8555
- ___block_literal_global.8757
- ___block_literal_global.9207
- ___block_literal_global.9394
- ___block_literal_global.9474
- ___block_literal_global.9556
- ___block_literal_global.9928
- _sharedInstance.__instance.10879
- _sharedInstance.onceToken.10017
- _sharedInstance.onceToken.10877
- _sharedInstance.onceToken.6800
- _shouldGenerateCandidateForContext:.onceToken.9934
Functions:
~ +[TUIKeyboardLayoutFactory crescendoLayouts] : 796 -> 812
CStrings:
+ "DecimalPad-Arabic"
+ "DecimalPad-Bengali"
+ "DecimalPad-Devanagari-Hindi"
+ "DecimalPad-Devanagari-Marathi"
+ "DecimalPad-Gujarati"
+ "DecimalPad-Jawi"
+ "DecimalPad-Kannada"
+ "DecimalPad-Kurdish-Sorani"
+ "DecimalPad-Oriya"
+ "DecimalPad-Pashto"
+ "DecimalPad-Persian"
+ "DecimalPad-Punjabi"
+ "DecimalPad-Sindhi"
+ "DecimalPad-Tibetan"
+ "DecimalPad-Urdu"
+ "NamePhonePad-Arabic"
+ "NamePhonePad-Bengali"
+ "NamePhonePad-Tibetan"
+ "NumberPad-Arabic"
+ "NumberPad-Bengali"
+ "NumberPad-Devanagari-Hindi"
+ "NumberPad-Devanagari-Marathi"
+ "NumberPad-Gujarati"
+ "NumberPad-Jawi"
+ "NumberPad-Kannada"
+ "NumberPad-Kurdish-Sorani"
+ "NumberPad-Oriya"
+ "NumberPad-Pashto"
+ "NumberPad-Persian"
+ "NumberPad-Punjabi"
+ "NumberPad-Sindhi"
+ "NumberPad-Tibetan"
+ "NumberPad-Urdu"
+ "PhonePad-Arabic"
+ "PhonePad-Bengali"
+ "PhonePad-Devanagari-Hindi"
+ "PhonePad-Devanagari-Marathi"
+ "PhonePad-Gujarati"
+ "PhonePad-Jawi"
+ "PhonePad-Kannada"
+ "PhonePad-Kurdish-Sorani"
+ "PhonePad-Oriya"
+ "PhonePad-Pashto"
+ "PhonePad-Persian"
+ "PhonePad-Punjabi"
+ "PhonePad-Sindhi"
+ "PhonePad-Tibetan"
+ "PhonePad-Urdu"

```

#### UIKitCore

>  `/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`

```diff

-9126.4.27.1.105
-  __TEXT.__text: 0x1b509b0
+9126.4.27.1.107
+  __TEXT.__text: 0x1b50a04
   __TEXT.__auth_stubs: 0xdb50
   __TEXT.__delay_helper: 0x1bc
   __TEXT.__init_offsets: 0x4

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: D80F437F-0293-33B6-B76B-5F2A74B11CDA
+  UUID: 32C1B300-A601-3E14-8B53-3419A2D2F234
   Functions: 173471
   Symbols:   437740
   CStrings:  181156
Symbols:
+ ___block_literal_global.394
+ ___block_literal_global.498
- ___block_literal_global.478
- ___block_literal_global.483
Functions:
~ -[UIKeyboardImpl canPresentNumberpadPopover] : 500 -> 516
~ -[UIKeyboardInputModeController _trackInputModeIfNecessary:] : 964 -> 940
~ _UIKeyboardGetKBStarName : 2684 -> 2676
~ -[UIKeyboardPreferencesController currentInputModeSupportsCrescendo] : 404 -> 360
~ _UIKeyboardGetDerivedKeyboardForSpecificOrientation : 4052 -> 4064
~ -[UIKeyboardPreferencesController inputModeSupportsCrescendo:screenTraits:keyboardType:] : 152 -> 284

```

#### UserNotificationsCore

>  `/System/Library/PrivateFrameworks/UserNotificationsCore.framework/UserNotificationsCore`

```diff

-640.4.40.102.0
-  __TEXT.__text: 0x1ed1c8
+640.4.40.103.0
+  __TEXT.__text: 0x1ed32c
   __TEXT.__auth_stubs: 0x3a40
-  __TEXT.__objc_methlist: 0x7ae4
+  __TEXT.__objc_methlist: 0x7af4
   __TEXT.__cstring: 0xa693
   __TEXT.__const: 0x10188
   __TEXT.__gcc_except_tab: 0x710
-  __TEXT.__oslogstring: 0xe627
+  __TEXT.__oslogstring: 0xe7b7
   __TEXT.__dlopen_cstrs: 0xf4
   __TEXT.__constg_swiftt: 0x67b0
   __TEXT.__swift5_typeref: 0x5fac

   __TEXT.__unwind_info: 0x5e20
   __TEXT.__eh_frame: 0x7328
   __TEXT.__objc_classname: 0x36a6
-  __TEXT.__objc_methname: 0x18f55
+  __TEXT.__objc_methname: 0x18f85
   __TEXT.__objc_methtype: 0x39bf
-  __TEXT.__objc_stubs: 0xf8a0
+  __TEXT.__objc_stubs: 0xf8c0
   __DATA_CONST.__got: 0x1560
   __DATA_CONST.__const: 0x1598
   __DATA_CONST.__objc_classlist: 0x6a0
   __DATA_CONST.__objc_catlist: 0x80
   __DATA_CONST.__objc_protolist: 0x2e0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x48d8
+  __DATA_CONST.__objc_selrefs: 0x48e0
   __DATA_CONST.__objc_protorefs: 0x170
   __DATA_CONST.__objc_superrefs: 0x200
   __AUTH_CONST.__auth_got: 0x1d30

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 464F21BA-D8AD-3EAB-B26F-DC2031A2D4CE
-  Functions: 9000
-  Symbols:   13203
-  CStrings:  7290
+  UUID: E008E957-0EB2-3896-B0AA-0804B71054CA
+  Functions: 9001
+  Symbols:   13206
+  CStrings:  7294
 
Symbols:
+ -[UNCRemoteNotificationServer _queue_topicIsExemptFromTokenValidation:]
+ _objc_msgSend$_queue_topicIsExemptFromTokenValidation:
Functions:
~ -[UNCRemoteNotificationServer _queue_messageIsValidForDelivery:] : 520 -> 844
+ -[UNCRemoteNotificationServer _queue_topicIsExemptFromTokenValidation:]
CStrings:
+ "Received remote notification on topic %{public}@ for bundleIdentifier %{public}@ for unknown token, dropping."
+ "Received remote notification on topic %{public}@ for bundleIdentifier %{public}@, hasPerAppToken: %{BOOL}d, pushType: %{public}@"
+ "Received remote notification on topic %{public}@ for unknown token, allowing exempt CloudKit topic for bundleIdentifier %{public}@."
+ "Received remote notification on topic %{public}@ for unknown token, allowing exempt bundleIdentifier %{public}@."
+ "_queue_topicIsExemptFromTokenValidation:"
- "Received remote notification on topic %{public}@ for unknown token, dropping."

```

#### libswiftPrespecialized.dylib

>  `/usr/lib/libswiftPrespecialized.dylib`

```diff

 0.0.0.0.0
   __TEXT.__text: 0x0
   __TEXT.__lldb_no_nlist: 0x0
-  __DATA_CONST.__const: 0x301f60
+  __DATA_CONST.__const: 0x301fb0
   __DATA_CONST.__ptrhashtab: 0x171d8
   __DATA_CONST.__ptrhashtabkey: 0x25f80
   __AUTH_CONST.__const: 0x4fa68
   __AUTH.__data: 0xcbe30
   - /usr/lib/libSystem.B.dylib
-  UUID: 47E1B48C-778B-3424-B569-21CCBA603CC9
+  UUID: 0641CC8A-BE8A-3D2E-B71B-B24E21A97887
   Functions: 0
-  Symbols:   151432
+  Symbols:   151430
   CStrings:  0
 
Symbols:
- _$s20AppleMediaServicesUI41AgeVerificationInfoViewControllerProviderC06createI012primaryLabel09secondaryM09linkTitle0O6ActionSo06UIViewI0CSS_S2SSgypSgtFZTq
- _$s20AppleMediaServicesUI41AgeVerificationInfoViewControllerProviderCMn

```


</details>

## EOF
