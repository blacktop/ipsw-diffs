# 17.6 (21G80) .vs 17.6.1 (21G93)

## IPSWs

- `iPhone16,2_17.6_21G80_Restore.ipsw`
- `iPhone16,2_17.6.1_21G93_Restore.ipsw`

## Kernel

### Version

| iOS | Version | Build | Date |
| :-- | :------ | :---- | :--- |
| 17.6 *(21G80)* | 23.6.0 | 10063.142.1~1 | Fri, 05Jul2024 18:04:28 PDT |
| 17.6.1 *(21G93)* | 23.6.0 | 10063.142.1~1 | Fri, 05Jul2024 18:04:28 PDT |

### Kexts

#### ⬆️ Updated (1)

<details>
  <summary><i>View Updated</i></summary>

>  `com.apple.driver.ASIOKit`

```diff

-11.77.0.0.0
+11.78.0.0.0
   __TEXT.__cstring: 0x1e3
   __TEXT.__const: 0x7c40
-  __TEXT_EXEC.__text: 0x33220
+  __TEXT_EXEC.__text: 0x33248
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xd8
   __DATA.__common: 0x60

```

</details>

## MachO

### ⬆️ Updated (8)

<details>
  <summary><i>View Updated</i></summary>

#### securityuploadd

>  `/usr/libexec/securityuploadd`

```diff

-61123.140.15.0.0
+61123.142.1.0.0
   __TEXT.__text: 0xc78c
   __TEXT.__auth_stubs: 0x780
   __TEXT.__objc_stubs: 0x1b60
   __TEXT.__objc_methlist: 0x644
   __TEXT.__const: 0x80
   __TEXT.__gcc_except_tab: 0x1d4
-  __TEXT.__cstring: 0xee0
+  __TEXT.__cstring: 0xedf
   __TEXT.__oslogstring: 0xe06
   __TEXT.__objc_classname: 0xd7
   __TEXT.__objc_methname: 0x1e97
CStrings:
+ "61123.142.1"
- "61123.140.15"

```

#### sharingd

>  `/usr/libexec/sharingd`

```diff

   __TEXT.__oslogstring: 0x1ebd8
   __TEXT.__objc_classname: 0x2c43
   __TEXT.__objc_methtype: 0x9955
-  __TEXT.__const: 0xc478
+  __TEXT.__const: 0xc488
   __TEXT.__gcc_except_tab: 0x55c8
   __TEXT.__dlopen_cstrs: 0x2c7
   __TEXT.__constg_swiftt: 0x6944

```

#### DailyBriefingFlowPlugin

>  `/System/Library/Assistant/FlowDelegatePlugins/DailyBriefingFlowPlugin.bundle/DailyBriefingFlowPlugin`

```diff

   __TEXT.__swift5_protos: 0x60
   __TEXT.__swift5_capture: 0x3d4
   __TEXT.__swift5_mpenum: 0x10
-  __TEXT.__unwind_info: 0x3ad4
+  __TEXT.__unwind_info: 0x3acc
   __TEXT.__eh_frame: 0x72e0
   __DATA_CONST.__auth_got: 0x15e8
   __DATA_CONST.__got: 0x640

```

#### ASIOKit

>  `/System/Library/Extensions/ASIOKit.kext/ASIOKit`

```diff

-11.77.0.0.0
+11.78.0.0.0
   __TEXT.__cstring: 0x1e3
   __TEXT.__const: 0x7c40
-  __TEXT_EXEC.__text: 0x33220
+  __TEXT_EXEC.__text: 0x33248
   __TEXT_EXEC.__auth_stubs: 0x1a0
   __DATA.__data: 0xd8
   __DATA.__common: 0x60

```

#### CDPFollowUpExtension

>  `/System/Library/PrivateFrameworks/CoreCDPUI.framework/PlugIns/CDPFollowUpExtension.appex/CDPFollowUpExtension`

```diff

-359.22.0.0.0
-  __TEXT.__text: 0x68d8
+359.23.0.0.0
+  __TEXT.__text: 0x6918
   __TEXT.__auth_stubs: 0x3f0
   __TEXT.__objc_stubs: 0x1400
   __TEXT.__objc_methlist: 0x2c0

   __TEXT.__dlopen_cstrs: 0x5a
   __TEXT.__unwind_info: 0x1c0
   __DATA_CONST.__auth_got: 0x208
-  __DATA_CONST.__got: 0xf8
+  __DATA_CONST.__got: 0x100
   __DATA_CONST.__const: 0x2e8
   __DATA_CONST.__cfstring: 0x260
   __DATA_CONST.__objc_classlist: 0x8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 146
-  Symbols:   147
+  Symbols:   148
   CStrings:  379
 
Symbols:
+ _kADPStateHealingActionContinue

```

#### appleaccountd

>  `/usr/libexec/appleaccountd`

```diff

-981.23.0.0.0
-  __TEXT.__text: 0x272f98
+981.23.1.0.0
+  __TEXT.__text: 0x275078
   __TEXT.__auth_stubs: 0x2300
   __TEXT.__objc_methlist: 0x620
-  __TEXT.__objc_methname: 0x3cfb
+  __TEXT.__objc_methname: 0x3d8a
   __TEXT.__objc_classname: 0x1e0
   __TEXT.__objc_methtype: 0x1261
-  __TEXT.__cstring: 0x1c074
-  __TEXT.__swift5_typeref: 0x5a09
+  __TEXT.__cstring: 0x1c484
+  __TEXT.__swift5_typeref: 0x5a17
   __TEXT.__swift5_entry: 0x8
   __TEXT.__const: 0xb6c0
-  __TEXT.__constg_swiftt: 0x8f24
-  __TEXT.__swift5_reflstr: 0x4914
-  __TEXT.__swift5_fieldmd: 0x4b88
+  __TEXT.__constg_swiftt: 0x8f8c
+  __TEXT.__swift5_reflstr: 0x4954
+  __TEXT.__swift5_fieldmd: 0x4ba0
   __TEXT.__swift5_builtin: 0x17c
   __TEXT.__swift5_assocty: 0x5a8
   __TEXT.__swift5_proto: 0x924
   __TEXT.__swift5_types: 0x48c
   __TEXT.__swift5_protos: 0x1b8
-  __TEXT.__swift5_capture: 0x4c4c
+  __TEXT.__swift5_capture: 0x4c98
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x5a80
+  __TEXT.__unwind_info: 0x5ab8
   __TEXT.__eh_frame: 0x5688
   __DATA_CONST.__auth_got: 0x1180
   __DATA_CONST.__got: 0x730
   __DATA_CONST.__auth_ptr: 0x430
-  __DATA_CONST.__const: 0x13490
+  __DATA_CONST.__const: 0x13568
   __DATA_CONST.__objc_classlist: 0x4b8
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x140

   __DATA_CONST.__objc_protorefs: 0xa0
   __DATA_CONST.__objc_classrefs: 0x410
   __DATA_CONST.__objc_superrefs: 0x8
-  __DATA.__objc_const: 0xc270
-  __DATA.__objc_selrefs: 0x10d8
+  __DATA.__objc_const: 0xc2b0
+  __DATA.__objc_selrefs: 0x1110
   __DATA.__objc_ivar: 0x4
   __DATA.__objc_data: 0x2418
-  __DATA.__data: 0xe958
+  __DATA.__data: 0xe9b8
   __DATA.__objc_stublist: 0x70
   __DATA.__bss: 0xe180
-  __DATA.__common: 0x398
+  __DATA.__common: 0x3b0
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CloudKit.framework/CloudKit
   - /System/Library/Frameworks/Combine.framework/Combine

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 8206
+  Functions: 8227
   Symbols:   1080
-  CStrings:  3017
+  CStrings:  3039
 
CStrings:
+ "%s - Error performing Walrus Status Mismatch Detection: %@"
+ "%s - Successfully performed Walrus Status Mismatch Detection"
+ "CombinedWalrusStatus: pcs:%lu octagon:%lu escrow:%lu"
+ "Error while fetching isWalrusStatusMismatched: %@"
+ "Found mismatch in CombinedWalrusStatus. Posting adpStateHealing CFU"
+ "Initiating combined walrus status fetch"
+ "No mismatch found in CombinedWalrusStatus. Tearing down adpStateHealing CFU, if posted already."
+ "combinedWalrusStatus:"
+ "contextForADPStateHealing"
+ "disableADPStateHealing"
+ "escrowWalrusStatus"
+ "isWalrusStatusMismatchDetectionEnabled"
+ "isWalrusStatusMismatchDetectionEnabled: %{bool}d"
+ "isWalrusStatusMismatchDetectionEnabled: Defaults are in place to prevent ADP State Healing"
+ "isWalrusStatusMismatchDetectionEnabled: Fetched new urlBag with success: %{bool}d and with error: %@"
+ "isWalrusStatusMismatchDetectionEnabled: configuration(atKey) nil"
+ "isWalrusStatusMismatchDetectionEnabled: urlBag is nil"
+ "isWalrusStatusMismatchDetectionEnabledKey"
+ "isWalrusStatusMismatched: %{bool}d"
+ "mismatchDetected"
+ "octagonWalrusStatus"
+ "pcsWalrusStatus"

```

#### asd

>  `/usr/libexec/asd`

```diff

 0.0.0.0.0
-  __TEXT.__text: 0x3776a0
-  __TEXT.__auth_stubs: 0x23a0
-  __TEXT.__objc_stubs: 0x4e80
+  __TEXT.__text: 0x3779e4
+  __TEXT.__auth_stubs: 0x2380
+  __TEXT.__objc_stubs: 0x4e40
   __TEXT.__objc_methlist: 0x17f0
-  __TEXT.__cstring: 0x4cdb
+  __TEXT.__cstring: 0x4c7b
   __TEXT.__objc_classname: 0x45e
-  __TEXT.__objc_methname: 0x7061
+  __TEXT.__objc_methname: 0x7019
   __TEXT.__objc_methtype: 0x8853
-  __TEXT.__const: 0xa3730
+  __TEXT.__const: 0xa3720
   __TEXT.__gcc_except_tab: 0x1924
   __TEXT.__ustring: 0x30
   __TEXT.__constg_swiftt: 0x14d8

   __TEXT.__swift5_protos: 0x54
   __TEXT.__swift5_proto: 0x318
   __TEXT.__swift5_mpenum: 0x18
-  __TEXT.__unwind_info: 0x3824
-  __TEXT.__eh_frame: 0x4890
-  __TEXT.__oslogstring: 0x10f0
-  __DATA_CONST.__auth_got: 0x11e0
-  __DATA_CONST.__got: 0x760
+  __TEXT.__unwind_info: 0x37dc
+  __TEXT.__eh_frame: 0x4858
+  __TEXT.__oslogstring: 0xff3
+  __DATA_CONST.__auth_got: 0x11d0
+  __DATA_CONST.__got: 0x740
   __DATA_CONST.__auth_ptr: 0xe0
-  __DATA_CONST.__const: 0x2b998
-  __DATA_CONST.__cfstring: 0x1ac0
+  __DATA_CONST.__const: 0x2b8f8
+  __DATA_CONST.__cfstring: 0x1a00
   __DATA_CONST.__objc_classlist: 0x200
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0xa8

   __DATA_CONST.__objc_protorefs: 0x40
   __DATA_CONST.__objc_classrefs: 0x468
   __DATA_CONST.__objc_superrefs: 0xb0
-  __DATA_CONST.__objc_intobj: 0x360
+  __DATA_CONST.__objc_intobj: 0x318
   __DATA_CONST.__objc_doubleobj: 0x20
-  __DATA_CONST.__objc_arraydata: 0x188
-  __DATA_CONST.__objc_dictobj: 0xf0
+  __DATA_CONST.__objc_arraydata: 0x148
+  __DATA_CONST.__objc_dictobj: 0xa0
   __DATA_CONST.__objc_arrayobj: 0xf0
   __DATA.__objc_const: 0x50d8
-  __DATA.__objc_selrefs: 0x1870
+  __DATA.__objc_selrefs: 0x1860
   __DATA.__objc_ivar: 0x150
   __DATA.__objc_data: 0x1730
-  __DATA.__data: 0xd5b8
+  __DATA.__data: 0xd5f8
   __DATA.__bss: 0x5880
   __DATA.__common: 0x1ec
   SMOOTH.SMOOTH: 0x60

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 4443
-  Symbols:   1335
-  CStrings:  2089
+  Functions: 4437
+  Symbols:   1329
+  CStrings:  2068
 
Symbols:
- _MGGetBoolAnswer
- _SecCertificateNotValidAfter
- _kSecAttrAccessGroup
- _kSecAttrService
- _kSecClassGenericPassword
- _kSecReturnData
CStrings:
+ "BEDTime check is disabled."
- "0dnM19zBqLw5ZPhIo4GEkg"
- "ASBAA-ucrt"
- "BAAExpDate"
- "BAASigKey"
- "BED Date %@, TimeInterval %f"
- "BED Error : %@"
- "BED Error ret=%d (0x%lx)"
- "BED Finished"
- "BED Trigger"
- "BEDTime"
- "Can't query info"
- "Converted BEDTime %@"
- "Ignoring ERROR querying objects %@"
- "Pulled Expiry date"
- "Pulling Expiry date"
- "Retrieved BEDTime %@"
- "USERDEFAULTS: Date = %@"
- "USERDEFAULTS: Date = nil"
- "ber"
- "com.apple.applesse"
- "dateWithTimeInterval:sinceDate:"
- "dateWithTimeIntervalSinceReferenceDate:"

```

#### security-sysdiagnose

>  `/usr/libexec/security-sysdiagnose`

```diff

-61123.140.15.0.0
+61123.142.1.0.0
   __TEXT.__text: 0x2cdc
   __TEXT.__auth_stubs: 0x710
   __TEXT.__objc_stubs: 0x360
   __TEXT.__objc_methlist: 0x50
-  __TEXT.__const: 0x68
+  __TEXT.__const: 0x60
   __TEXT.__gcc_except_tab: 0x114
   __TEXT.__objc_classname: 0x2f
   __TEXT.__objc_methname: 0x2ae

```


</details>

## DSC

### WebKit

| iOS | Version |
| :-- | :------ |
| 17.6 *(21G80)* | 618.3.11.10.5 |
| 17.6.1 *(21G93)* | 618.3.11.10.5 |

### Dylibs

#### ⬆️ Updated (10)

<details>
  <summary><i>View Updated</i></summary>

#### HealthRecordsUI

>  `/System/Library/PrivateFrameworks/HealthRecordsUI.framework/HealthRecordsUI`

```diff

   __TEXT.__swift5_capture: 0x36d8
   __TEXT.__swift5_protos: 0x114
   __TEXT.__swift5_mpenum: 0x88
-  __TEXT.__unwind_info: 0xe9f0
+  __TEXT.__unwind_info: 0xe9f4
   __TEXT.__eh_frame: 0xa740
   __TEXT.__objc_classname: 0x101d
   __TEXT.__objc_methname: 0x18f52

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 22805
+  Functions: 22806
   Symbols:   3939
   CStrings:  7635
 

```

#### CDPAccountNotificationPlugin_IOS

>  `/System/Library/Accounts/Notification/CDPAccountNotificationPlugin_IOS.bundle/CDPAccountNotificationPlugin_IOS`

```diff

-359.22.0.0.0
-  __TEXT.__text: 0x884
+359.23.0.0.0
+  __TEXT.__text: 0x8a8
   __TEXT.__auth_stubs: 0x140
   __TEXT.__objc_methlist: 0x44
   __TEXT.__const: 0x50

   __TEXT.__oslogstring: 0x1fa
   __TEXT.__unwind_info: 0x70
   __TEXT.__objc_classname: 0x43
-  __TEXT.__objc_methname: 0x54b
+  __TEXT.__objc_methname: 0x565
   __TEXT.__objc_methtype: 0x209
-  __TEXT.__objc_stubs: 0x380
+  __TEXT.__objc_stubs: 0x3a0
   __DATA_CONST.__got: 0x38
   __DATA_CONST.__const: 0x28
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x4a0
-  __DATA_CONST.__objc_selrefs: 0xe8
+  __DATA_CONST.__objc_selrefs: 0xf0
   __DATA_CONST.__objc_classrefs: 0x38
   __AUTH_CONST.__cfstring: 0x20
   __AUTH_CONST.__const: 0x20

   - /usr/lib/libobjc.A.dylib
   Functions: 9
   Symbols:   45
-  CStrings:  98
+  CStrings:  99
 
CStrings:
+ "contextForADPStateHealing"

```

#### AppleAccount

>  `/System/Library/PrivateFrameworks/AppleAccount.framework/AppleAccount`

```diff

-981.23.0.0.0
-  __TEXT.__text: 0xb87e4
+981.23.1.0.0
+  __TEXT.__text: 0xb88d0
   __TEXT.__auth_stubs: 0xac0
-  __TEXT.__objc_methlist: 0x8e3c
+  __TEXT.__objc_methlist: 0x8e54
   __TEXT.__const: 0x1610
-  __TEXT.__cstring: 0xb770
+  __TEXT.__cstring: 0xb79c
   __TEXT.__oslogstring: 0xd3a6
   __TEXT.__gcc_except_tab: 0x1710
   __TEXT.__dlopen_cstrs: 0x241
   __TEXT.__unwind_info: 0x2454
   __TEXT.__objc_classname: 0x1c08
-  __TEXT.__objc_methname: 0x133e7
+  __TEXT.__objc_methname: 0x13419
   __TEXT.__objc_methtype: 0x2a17
   __TEXT.__objc_stubs: 0xad40
   __DATA_CONST.__got: 0x510

   __DATA_CONST.__objc_protolist: 0x150
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x1b028
-  __DATA_CONST.__objc_selrefs: 0x4418
+  __DATA_CONST.__objc_selrefs: 0x4428
   __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__objc_classrefs: 0x720
   __DATA_CONST.__objc_superrefs: 0x510
   __DATA_CONST.__objc_arraydata: 0xc0
-  __AUTH_CONST.__cfstring: 0xae60
+  __AUTH_CONST.__cfstring: 0xae80
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_const: 0x238
   __AUTH_CONST.__objc_intobj: 0xd8

   - /usr/lib/libcompression.dylib
   - /usr/lib/liblockdown.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 3901
-  Symbols:   5391
-  CStrings:  6414
+  Functions: 3903
+  Symbols:   5394
+  CStrings:  6417
 
Symbols:
+ _kAAProtocolPrefDisableADPStateHealingKey
CStrings:
+ "disableADPStateHealing"
+ "disableWalrusStatusMismatchDetectionEnabled"
+ "setDisableADPStateHealing:"

```

#### CoreCDP

>  `/System/Library/PrivateFrameworks/CoreCDP.framework/CoreCDP`

```diff

-359.22.0.0.0
-  __TEXT.__text: 0x316f0
+359.23.0.0.0
+  __TEXT.__text: 0x324a8
   __TEXT.__auth_stubs: 0x9a0
-  __TEXT.__objc_methlist: 0x2814
+  __TEXT.__objc_methlist: 0x284c
   __TEXT.__const: 0xe0
-  __TEXT.__gcc_except_tab: 0xe28
-  __TEXT.__oslogstring: 0x7506
-  __TEXT.__cstring: 0x29dd
+  __TEXT.__gcc_except_tab: 0xe68
+  __TEXT.__oslogstring: 0x76c1
+  __TEXT.__cstring: 0x2a41
   __TEXT.__dlopen_cstrs: 0x68
   __TEXT.__ustring: 0x28
-  __TEXT.__unwind_info: 0xddc
+  __TEXT.__unwind_info: 0xe0c
   __TEXT.__objc_classname: 0x6b6
-  __TEXT.__objc_methname: 0x76f9
-  __TEXT.__objc_methtype: 0x1861
-  __TEXT.__objc_stubs: 0x4420
+  __TEXT.__objc_methname: 0x7815
+  __TEXT.__objc_methtype: 0x1900
+  __TEXT.__objc_stubs: 0x44c0
   __DATA_CONST.__got: 0x188
-  __DATA_CONST.__const: 0x1308
+  __DATA_CONST.__const: 0x1360
   __DATA_CONST.__objc_classlist: 0x190
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0xa0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x76d8
-  __DATA_CONST.__objc_selrefs: 0x1b68
+  __DATA_CONST.__objc_const: 0x7748
+  __DATA_CONST.__objc_selrefs: 0x1bb8
   __DATA_CONST.__objc_protorefs: 0x30
-  __DATA_CONST.__objc_classrefs: 0x288
+  __DATA_CONST.__objc_classrefs: 0x290
   __DATA_CONST.__objc_superrefs: 0xd8
   __DATA_CONST.__objc_arraydata: 0x90
   __AUTH_CONST.__objc_const: 0x14f0
-  __AUTH_CONST.__cfstring: 0x2c40
+  __AUTH_CONST.__cfstring: 0x2ca0
   __AUTH_CONST.__const: 0x3c0
   __AUTH_CONST.__objc_intobj: 0x48
   __AUTH_CONST.__objc_dictobj: 0x28

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1451
-  Symbols:   2013
-  CStrings:  2414
+  Functions: 1474
+  Symbols:   2038
+  CStrings:  2438
 
Symbols:
+ _CDP_FOLLOWUP_ADP_STATE_HEALING
+ _OBJC_CLASS_$_AKURLBag
CStrings:
+ "\"Creating context for ADP State healing CFU\""
+ "\"Error %@ getting isWalrusStatusMismatchDetectionEnabled from URLBag, returning false\""
+ "\"Failed to fetch walrus combined status with error: %@\""
+ "\"Received isWalrusStatusMismatchDetectionEnabled = %d\""
+ "\"Walrus combined status %@\""
+ "\"XPC Error while fetching walrus combined status: %{public}@\""
+ "\"isWalrusStatusMismatchDetectionEnabled has overrider set, returning false\""
+ "@\"CDPCombinedWalrusStatus\"24@0:8^@16"
+ "Vv32@0:8@\"CDPContext\"16@?<v@?@\"CDPCombinedWalrusStatus\"@\"NSError\">24"
+ "Walrus: Fetching combined status."
+ "combinedWalrusStatus:"
+ "combinedWalrusStatusWithCompletion:"
+ "combinedWalrusStatusWithContext:completion:"
+ "configurationAtKey:"
+ "contextForADPStateHealing"
+ "disableWalrusStatusMismatchDetectionEnabled"
+ "intValue"
+ "isWalrusStatusMismatchDetectionEnabled"
+ "isWalrusStatusMismatchDetectionEnabledWithCompletion:"
+ "kADPStateHealing"
+ "mismatchDetected"
+ "requestNewURLBagIfNecessaryWithCompletion:"
+ "sharedBag"
+ "v24@0:8@?<v@?@\"CDPCombinedWalrusStatus\"@\"NSError\">16"

```

#### CoreCDPInternal

>  `/System/Library/PrivateFrameworks/CoreCDPInternal.framework/CoreCDPInternal`

```diff

-359.22.0.0.0
-  __TEXT.__text: 0x68130
+359.23.0.0.0
+  __TEXT.__text: 0x692cc
   __TEXT.__auth_stubs: 0xac0
-  __TEXT.__objc_methlist: 0x3b30
+  __TEXT.__objc_methlist: 0x3b98
   __TEXT.__const: 0x90
-  __TEXT.__oslogstring: 0xfcd2
-  __TEXT.__cstring: 0x4be6
+  __TEXT.__oslogstring: 0xffd6
+  __TEXT.__cstring: 0x4ce8
   __TEXT.__gcc_except_tab: 0x78c
-  __TEXT.__unwind_info: 0x1484
+  __TEXT.__unwind_info: 0x14a8
   __TEXT.__objc_classname: 0xb75
-  __TEXT.__objc_methname: 0xc670
-  __TEXT.__objc_methtype: 0x22b3
-  __TEXT.__objc_stubs: 0xa440
-  __DATA_CONST.__got: 0x8d0
-  __DATA_CONST.__const: 0x1af0
+  __TEXT.__objc_methname: 0xc7fe
+  __TEXT.__objc_methtype: 0x22f8
+  __TEXT.__objc_stubs: 0xa5a0
+  __DATA_CONST.__got: 0x8e0
+  __DATA_CONST.__const: 0x1b08
   __DATA_CONST.__objc_classlist: 0x248
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x110
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0xd8a8
-  __DATA_CONST.__objc_selrefs: 0x2d38
+  __DATA_CONST.__objc_const: 0xd8c8
+  __DATA_CONST.__objc_selrefs: 0x2d90
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_classrefs: 0x4a8
   __DATA_CONST.__objc_superrefs: 0x150
-  __DATA_CONST.__objc_arraydata: 0x68
+  __DATA_CONST.__objc_arraydata: 0x70
   __AUTH_CONST.__objc_const: 0x1a38
-  __AUTH_CONST.__cfstring: 0x3ca0
+  __AUTH_CONST.__cfstring: 0x3d80
   __AUTH_CONST.__const: 0x380
   __AUTH_CONST.__objc_intobj: 0x138
   __AUTH_CONST.__auth_ptr: 0x8

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2391
-  Symbols:   3162
-  CStrings:  3870
+  Functions: 2415
+  Symbols:   3191
+  CStrings:  3903
 
Symbols:
+ _CDP_FOLLOWUP_ADP_STATE_HEALING
+ _FLNotificationOptionBannerAlert
+ _kADPDeepLinkUrl
+ _kADPStateHealingActionContinue
+ _kADPStateHealingItemIdentifier
CStrings:
+ "\"Account not eligible, cannot fetch walrus matched status: %@\""
+ "\"Did Clear Pending ADPStateHealing CFU? %d with error: %@\""
+ "\"Failed to fetch any pending CFUs, error: %{public}@\""
+ "\"Failed to fetch walrus combined status with error code: %zd, error: %@\""
+ "\"Found CFU with uniqueIdentifier %@\""
+ "\"No Pending ADPStateHealing CFU found. Continuing to Return combined walrus status\""
+ "\"No eligible primary account found, cannot fetch walrus matched status: %@\""
+ "\"Pending ADPStateHealing CFU found. Dismissing...\""
+ "\"Walrus combined status %@ status fetched successfully.\""
+ "\"Walrus octagon state error: %@\""
+ "\"Walrus state mismatch NOT detected. Checking if there is a pending ADPStateHealing CFU posted...\""
+ "\"Walrus state mismatch detected\""
+ "\"Walrus state: %@\""
+ "\"Walrus stingray state error: %@\""
+ "ADP_STATE_HEALING_CFU_TEXT"
+ "ADP_STATE_HEALING_CFU_TITLE"
+ "ADP_STATE_HEALING_NOTIFICATION_TEXT"
+ "CONTINUE"
+ "Vv32@0:8@\"CDPContext\"16@?<v@?@\"CDPCombinedWalrusStatus\"@\"NSError\">24"
+ "_adpStateHealingFollowUpAction"
+ "_combinedWalrusStatusForPrimaryAccountWithError:"
+ "_combinedWalrusStatusWithContext:error:"
+ "_combinedWalrusStatusWithOptions:context:error:"
+ "_followUpForADPStateHealingWithContext:"
+ "com.apple.CDPFollowUpIdentifier.adpStateHealing"
+ "com.apple.cdp.adpStateHealing.continue"
+ "combinedWalrusStatusWithContext:completion:"
+ "combinedWalrusStatusWithContext:error:"
+ "contextForADPStateHealing"
+ "hasPendingFollowUpWithUniqueIdentifier:"
+ "mismatchDetected"
+ "pendingFollowUpItems:"
+ "prefs:root=APPLE_ACCOUNT&path=ICLOUD_SERVICE/ICLOUD_ADP_SPECIFIER_NAME"

```

#### CoreCDPUI

>  `/System/Library/PrivateFrameworks/CoreCDPUI.framework/CoreCDPUI`

```diff

-359.22.0.0.0
-  __TEXT.__text: 0x4ded8
-  __TEXT.__auth_stubs: 0x1670
+359.23.0.0.0
+  __TEXT.__text: 0x51d3c
+  __TEXT.__auth_stubs: 0x16b0
   __TEXT.__objc_methlist: 0x2c5c
-  __TEXT.__const: 0x1824
-  __TEXT.__cstring: 0x42c8
-  __TEXT.__oslogstring: 0x2610
+  __TEXT.__const: 0x18b4
+  __TEXT.__cstring: 0x4568
+  __TEXT.__oslogstring: 0x262c
   __TEXT.__gcc_except_tab: 0x82c
   __TEXT.__dlopen_cstrs: 0x230
-  __TEXT.__constg_swiftt: 0xae0
-  __TEXT.__swift5_typeref: 0x50f2
+  __TEXT.__constg_swiftt: 0xb40
+  __TEXT.__swift5_typeref: 0x636e
   __TEXT.__swift5_builtin: 0x28
-  __TEXT.__swift5_reflstr: 0x610
-  __TEXT.__swift5_fieldmd: 0x5a0
+  __TEXT.__swift5_reflstr: 0x640
+  __TEXT.__swift5_fieldmd: 0x5ac
   __TEXT.__swift5_assocty: 0x138
   __TEXT.__swift5_proto: 0x64
   __TEXT.__swift5_types: 0x70
-  __TEXT.__swift5_capture: 0x290
+  __TEXT.__swift5_capture: 0x340
   __TEXT.__swift5_protos: 0xc
-  __TEXT.__unwind_info: 0x15cc
+  __TEXT.__unwind_info: 0x1620
   __TEXT.__eh_frame: 0x98
   __TEXT.__objc_classname: 0xc0b
-  __TEXT.__objc_methname: 0xa8d1
+  __TEXT.__objc_methname: 0xa951
   __TEXT.__objc_methtype: 0x294b
-  __TEXT.__objc_stubs: 0x7a40
+  __TEXT.__objc_stubs: 0x7aa0
   __DATA_CONST.__got: 0x640
-  __DATA_CONST.__const: 0x1180
+  __DATA_CONST.__const: 0x1160
   __DATA_CONST.__objc_classlist: 0x230
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x160
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0xe868
-  __DATA_CONST.__objc_selrefs: 0x2440
+  __DATA_CONST.__objc_const: 0xe888
+  __DATA_CONST.__objc_selrefs: 0x2460
   __DATA_CONST.__objc_protorefs: 0x50
   __DATA_CONST.__objc_classrefs: 0x4f0
   __DATA_CONST.__objc_superrefs: 0x130
   __DATA_CONST.__objc_catlist2: 0x10
   __AUTH_CONST.__cfstring: 0x2460
   __AUTH_CONST.__objc_const: 0x1410
-  __AUTH_CONST.__const: 0x1960
+  __AUTH_CONST.__const: 0x1b58
   __AUTH_CONST.__auth_ptr: 0x88
-  __AUTH_CONST.__auth_got: 0xb48
-  __AUTH.__objc_data: 0x1cb0
+  __AUTH_CONST.__auth_got: 0xb68
+  __AUTH.__objc_data: 0x1d50
   __AUTH.__data: 0x690
   __DATA.__objc_ivar: 0x350
-  __DATA.__data: 0x1ba8
+  __DATA.__data: 0x1c98
   __DATA.__objc_stublist: 0x10
-  __DATA.__bss: 0xc60
-  __DATA.__common: 0xb8
+  __DATA.__bss: 0xc80
+  __DATA.__common: 0xd0
   __DATA_DIRTY.__objc_data: 0xa0
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 2074
-  Symbols:   1869
-  CStrings:  2721
+  Functions: 2138
+  Symbols:   1877
+  CStrings:  2738
 
CStrings:
+ "\"%@: target state %ld, needs change: %{BOOL}d, mismatchDetected: %{BOOL}d\""
+ "ADP Status Healing flow cancelled nil url, walrus enabled: %{bool}d"
+ "ADP_STATUS_HEALING_BODY_TEXT"
+ "ADP_STATUS_HEALING_PRIMARY_BUTTON_TEXT"
+ "ADP_STATUS_HEALING_SECONDARY_BUTTON_TEXT"
+ "ADP_STATUS_HEALING_TITLE_TEXT"
+ "Beginning ADP Status Healing flow with URL: %s"
+ "Could not fetch WalrusStatusMismatchDetectionEnabled configuration. Error: %s"
+ "WalrusStatusMismatchDetectionEnabled feature disabled through server config"
+ "[%s %s]"
+ "[%s %s]: Error while fetching combined walrus status: %@"
+ "_walrusStatusMismatchDetected"
+ "combinedWalrusStatusWithCompletion:"
+ "isWalrusStatusMismatchDetectionEnabledWithCompletion:"
+ "isWalrusStatusMismatched(completion:)"
+ "mismatchDetected"
+ "octagonWalrusStatus"
+ "v24@?0@\"CDPCombinedWalrusStatus\"8@\"NSError\"16"
- "\"%@: target state %ld, needs change: %{BOOL}d\""

```

#### CoreCDPUIInternal

>  `/System/Library/PrivateFrameworks/CoreCDPUIInternal.framework/CoreCDPUIInternal`

```diff

-359.22.0.0.0
+359.23.0.0.0
   __TEXT.__text: 0x5598
   __TEXT.__auth_stubs: 0x2f0
   __TEXT.__objc_methlist: 0x41c

   __TEXT.__gcc_except_tab: 0x60
   __TEXT.__unwind_info: 0x180
   __TEXT.__objc_classname: 0x157
-  __TEXT.__objc_methname: 0x171a
-  __TEXT.__objc_methtype: 0x381
+  __TEXT.__objc_methname: 0x1754
+  __TEXT.__objc_methtype: 0x3e7
   __TEXT.__objc_stubs: 0x1300
   __DATA_CONST.__got: 0xa8
   __DATA_CONST.__const: 0x288
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0xce0
+  __DATA_CONST.__objc_const: 0xd20
   __DATA_CONST.__objc_selrefs: 0x648
   __DATA_CONST.__objc_classrefs: 0x138
   __DATA_CONST.__objc_superrefs: 0x20

   - /usr/lib/libobjc.A.dylib
   Functions: 124
   Symbols:   252
-  CStrings:  415
+  CStrings:  420
 
CStrings:
+ "@\"CDPCombinedWalrusStatus\"24@0:8^@16"
+ "@24@0:8^@16"
+ "combinedWalrusStatus:"
+ "combinedWalrusStatusWithCompletion:"
+ "v24@0:8@?<v@?@\"CDPCombinedWalrusStatus\"@\"NSError\">16"

```

#### FocusSettingsUI

>  `/System/Library/PrivateFrameworks/FocusSettingsUI.framework/FocusSettingsUI`

```diff

   __TEXT.__swift5_types: 0x42c
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0x6ae4
+  __TEXT.__unwind_info: 0x6ae0
   __TEXT.__eh_frame: 0x2a78
   __TEXT.__objc_classname: 0x273
   __TEXT.__objc_methname: 0x5315

```

#### SettingsFoundation

>  `/System/Library/PrivateFrameworks/SettingsFoundation.framework/SettingsFoundation`

```diff

-1062.2.0.0.0
-  __TEXT.__text: 0x1005c
+1062.3.0.0.0
+  __TEXT.__text: 0x10260
   __TEXT.__auth_stubs: 0x6d0
   __TEXT.__objc_methlist: 0x5f8
-  __TEXT.__const: 0x6f4
+  __TEXT.__const: 0x794
   __TEXT.__cstring: 0x1730
   __TEXT.__oslogstring: 0x14d5
   __TEXT.__ustring: 0x588

   __AUTH_CONST.__cfstring: 0x1fc0
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__objc_const: 0x0
+  __AUTH_CONST.__const: 0x100
   __AUTH_CONST.__objc_arrayobj: 0xa8
-  __AUTH_CONST.__const: 0xa0
   __AUTH_CONST.__auth_got: 0x370
   __DATA.__objc_ivar: 0x2c
   __DATA.__data: 0x28
   __DATA.__bss: 0xc8
-  __DATA_DIRTY.__const: 0x360
+  __DATA_DIRTY.__const: 0x300
   __DATA_DIRTY.__objc_const: 0x358
   __DATA_DIRTY.__objc_data: 0x320
   __DATA_DIRTY.__bss: 0x168

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 277
-  Symbols:   497
+  Functions: 278
+  Symbols:   498
   CStrings:  701
 

```

#### IntelligencePlatformCore

>  `/System/Library/PrivateFrameworks/IntelligencePlatformCore.framework/IntelligencePlatformCore`

```diff

 75.16.0.0.0
-  __TEXT.__text: 0xad5590
+  __TEXT.__text: 0xad4c60
   __TEXT.__auth_stubs: 0x9170
   __TEXT.__objc_methlist: 0x154c
-  __TEXT.__const: 0x5a1b9
-  __TEXT.__cstring: 0x54dea
+  __TEXT.__const: 0x5a1c9
+  __TEXT.__cstring: 0x54dca
   __TEXT.__swift5_typeref: 0x19ab0
   __TEXT.__constg_swiftt: 0x1e8d0
-  __TEXT.__swift5_reflstr: 0x23f7c
+  __TEXT.__swift5_reflstr: 0x23f6c
   __TEXT.__swift5_fieldmd: 0x1eac8
   __TEXT.__swift5_builtin: 0x438
   __TEXT.__swift5_mpenum: 0xf8

   __TEXT.__oslogstring: 0x385
   __TEXT.__dlopen_cstrs: 0xc0
   __TEXT.__unwind_info: 0x29064
-  __TEXT.__eh_frame: 0x55fb4
+  __TEXT.__eh_frame: 0x55fac
   __TEXT.__objc_classname: 0x488
   __TEXT.__objc_methname: 0x8baf
   __TEXT.__objc_methtype: 0x2093

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 71504
+  Functions: 71498
   Symbols:   771
   CStrings:  8750
 

```


</details>

## EOF
