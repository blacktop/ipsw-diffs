# 26.5 (25F71) .vs 26.5.1 (25F80)

## Inputs

- `UniversalMac_26.5_25F71_Restore.ipsw`
- `UniversalMac_26.5.1_25F80_Restore.ipsw`

## Kernel

### Version

| iOS | Version | Build | Date |
| :-- | :------ | :---- | :--- |
| 26.5 *(25F71)* | 25.5.0 | 12377.121.6~2 | Mon Apr 27 20:41:12 PDT 2026 |
| 26.5.1 *(25F80)* | 25.5.0 | 12377.121.6~2 | Mon Apr 27 20:41:12 PDT 2026 |

## Entitlements

- No differences found

## MachO

#### ⬆️ Updated (3)

#### `/root/usr/libexec/neagent`

```diff

-2226.120.19.0.0
+2226.121.1.0.0
   __TEXT.__text: 0x1919c
   __TEXT.__auth_stubs: 0x6f0
   __TEXT.__objc_stubs: 0x1b20

   __TEXT.__cstring: 0x11b5
   __TEXT.__objc_classname: 0x341
   __TEXT.__objc_methtype: 0xefb
-  __TEXT.__info_plist: 0x41c
+  __TEXT.__info_plist: 0x421
   __TEXT.__unwind_info: 0x420
   __DATA_CONST.__auth_got: 0x388
   __DATA_CONST.__got: 0x1a0

   - /System/Library/PrivateFrameworks/CipherML.framework/Versions/A/CipherML
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 2433BD89-A48B-3F48-883E-351416C0941F
+  UUID: 7D5EDF18-9383-36A4-BAE2-2CBC54A2E8CE
   Functions: 361
   Symbols:   170
   CStrings:  0

```


#### `/root/usr/libexec/nehelper`

```diff

-2226.120.19.0.0
+2226.121.1.0.0
   __TEXT.__text: 0x24188
   __TEXT.__auth_stubs: 0xde0
   __TEXT.__delay_helper: 0xdc

   __TEXT.__oslogstring: 0x4094
   __TEXT.__objc_classname: 0x1a4
   __TEXT.__objc_methtype: 0x280
-  __TEXT.__info_plist: 0x41e
+  __TEXT.__info_plist: 0x423
   __TEXT.__unwind_info: 0x3d0
   __DATA_CONST.__auth_got: 0x700
   __DATA_CONST.__got: 0x298

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 4462DE94-79B8-34AC-8188-979A74C4C28E
+  UUID: 8ABF0388-7BA4-329C-86D6-56B7220846F6
   Functions: 244
   Symbols:   303
   CStrings:  0

```


#### `/root/usr/libexec/nesessionmanager`

```diff

-2226.120.19.0.0
+2226.121.1.0.0
   __TEXT.__text: 0xc5064
   __TEXT.__auth_stubs: 0x1be0
   __TEXT.__objc_stubs: 0x8000

   __TEXT.__cstring: 0x5211
   __TEXT.__objc_classname: 0xb31
   __TEXT.__objc_methtype: 0x1ad3
-  __TEXT.__info_plist: 0x42e
+  __TEXT.__info_plist: 0x433
   __TEXT.__unwind_info: 0x1690
   __DATA_CONST.__auth_got: 0xe00
   __DATA_CONST.__got: 0x720

   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libnetworkextension.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: DBA64C40-AA64-339F-8ECD-B827BE3F69E2
+  UUID: 0883408B-C7C8-3DAE-9800-FEF9E6BB495C
   Functions: 1951
   Symbols:   659
   CStrings:  0

```

## DSC

### WebKit

| iOS | Version |
| :-- | :------ |
| 26.5 *(25F71)* | 624.2.5.11.4 |
| 26.5 *(25F80)* | 624.2.5.11.4 |

### Dylibs

#### ⬆️ Updated (1)

#### `/System/Library/Frameworks/NetworkExtension.framework/Versions/A/NetworkExtension`

```diff

-2226.120.19.0.0
-  __TEXT.__text: 0x22e704
+2226.121.1.0.0
+  __TEXT.__text: 0x22e46c
   __TEXT.__auth_stubs: 0x4510
   __TEXT.__objc_methlist: 0xf178
-  __TEXT.__const: 0x34c0
+  __TEXT.__const: 0x34b0
   __TEXT.__cstring: 0x18cf8
   __TEXT.__constg_swiftt: 0xc1c
   __TEXT.__swift5_typeref: 0xdd3

   __TEXT.__swift5_proto: 0x60
   __TEXT.__swift5_types: 0x90
   __TEXT.__swift5_capture: 0xd58
-  __TEXT.__oslogstring: 0x25a62
+  __TEXT.__oslogstring: 0x259b3
   __TEXT.__swift_as_entry: 0xe4
   __TEXT.__swift_as_ret: 0x104
   __TEXT.__swift5_protos: 0x14

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 5ABB3BC5-BBAD-36DD-98EE-43FD291643A3
+  UUID: 8618B266-AF27-3652-8E9A-7CCC336C9DA5
   Functions: 8022
   Symbols:   16956
   CStrings:  0
Symbols:
+ __Block_byref_object_copy_.12830
+ __Block_byref_object_copy_.15324
+ __Block_byref_object_copy_.17818
+ __Block_byref_object_copy_.20928
+ __Block_byref_object_copy_.22248
+ __Block_byref_object_copy_.23311
+ __Block_byref_object_copy_.24539
+ __Block_byref_object_copy_.25222
+ __Block_byref_object_copy_.27888
+ __Block_byref_object_copy_.29044
+ __Block_byref_object_copy_.7228
+ __Block_byref_object_copy_.9746
+ __Block_byref_object_dispose_.12831
+ __Block_byref_object_dispose_.15325
+ __Block_byref_object_dispose_.17819
+ __Block_byref_object_dispose_.20929
+ __Block_byref_object_dispose_.22249
+ __Block_byref_object_dispose_.23312
+ __Block_byref_object_dispose_.24540
+ __Block_byref_object_dispose_.25223
+ __Block_byref_object_dispose_.27889
+ __Block_byref_object_dispose_.29045
+ __Block_byref_object_dispose_.7229
+ __Block_byref_object_dispose_.9747
+ __block_descriptor_tmp.20126
+ __block_descriptor_tmp.24012
+ __block_descriptor_tmp.26098
+ __block_descriptor_tmp.26715
+ __block_literal_global.10.15873
+ __block_literal_global.10.9391
+ __block_literal_global.10350
+ __block_literal_global.13129
+ __block_literal_global.13496
+ __block_literal_global.14.22773
+ __block_literal_global.14.26328
+ __block_literal_global.14451
+ __block_literal_global.14630
+ __block_literal_global.15326
+ __block_literal_global.15875
+ __block_literal_global.16467
+ __block_literal_global.16709
+ __block_literal_global.17395
+ __block_literal_global.17826
+ __block_literal_global.18278
+ __block_literal_global.18415
+ __block_literal_global.18726
+ __block_literal_global.19.14464
+ __block_literal_global.19.18406
+ __block_literal_global.20035
+ __block_literal_global.20713
+ __block_literal_global.21235
+ __block_literal_global.22.14465
+ __block_literal_global.22.18412
+ __block_literal_global.22343
+ __block_literal_global.22778
+ __block_literal_global.23176
+ __block_literal_global.23925
+ __block_literal_global.24010
+ __block_literal_global.24473
+ __block_literal_global.24624
+ __block_literal_global.24733
+ __block_literal_global.24779
+ __block_literal_global.24973
+ __block_literal_global.26046
+ __block_literal_global.26096
+ __block_literal_global.26332
+ __block_literal_global.26438
+ __block_literal_global.26821
+ __block_literal_global.27378
+ __block_literal_global.27466
+ __block_literal_global.27615
+ __block_literal_global.27854
+ __block_literal_global.28.27892
+ __block_literal_global.28.5705
+ __block_literal_global.28406
+ __block_literal_global.29097
+ __block_literal_global.4.14454
+ __block_literal_global.5726
+ __block_literal_global.63.20708
+ __block_literal_global.7.26036
+ __block_literal_global.7258
+ __block_literal_global.73.26433
+ __block_literal_global.7482
+ __block_literal_global.7666
+ __block_literal_global.8067
+ __block_literal_global.9389
+ _extensionAuxiliaryHostProtocol.protocol.20709
+ _extensionAuxiliaryHostProtocol.protocol.24780
+ _extensionAuxiliaryHostProtocol.protocol.26434
+ _extensionAuxiliaryHostProtocol.protocolInit.20707
+ _extensionAuxiliaryHostProtocol.protocolInit.24778
+ _extensionAuxiliaryHostProtocol.protocolInit.26432
+ _extensionAuxiliaryVendorProtocol.protocol.20714
+ _extensionAuxiliaryVendorProtocol.protocol.26439
+ _extensionAuxiliaryVendorProtocol.protocolInit.20712
+ _extensionAuxiliaryVendorProtocol.protocolInit.26437
+ convert_error_to_string.25215
+ driverInterface.driverInterface.10347
+ driverInterface.driverInterface.17396
+ driverInterface.driverInterface.21232
+ driverInterface.driverInterface.22774
+ driverInterface.driverInterface.7660
+ driverInterface.onceToken.10346
+ driverInterface.onceToken.17394
+ driverInterface.onceToken.21231
+ driverInterface.onceToken.22772
+ driverInterface.onceToken.7659
+ g_noAppFilter.29018
+ globalConfigurationManager.gChangeQueue.18410
+ globalConfigurationManager.gChangeQueue.5724
+ globalConfigurationManager.gConfigurationManager.18407
+ globalConfigurationManager.gConfigurationManager.5722
+ globalConfigurationManager.onceToken.18405
+ globalConfigurationManager.onceToken.5721
+ initGlobals.onceToken.16708
+ loadedManagers.loadedManagers.27852
+ loadedManagers.loadedManagers.29021
+ loadedManagers.managers_init.27851
+ loadedManagers.managers_init.29020
+ managerInterface.managerInterface.10351
+ managerInterface.managerInterface.21236
+ managerInterface.managerInterface.22779
+ managerInterface.onceToken.10349
+ managerInterface.onceToken.21234
+ managerInterface.onceToken.22777
+ sharedManager.g_manager.27467
+ sharedManager.g_manager.7483
+ sharedManager.g_manager.8068
+ sharedManager.init_manager.7481
+ sharedManager.init_manager.8066
+ sharedManager.onceToken.18414
+ sharedManager.onceToken.27465
+ sharedManager.onceToken.29096
+ sharedManager.onceToken.5725
- __Block_byref_object_copy_.12834
- __Block_byref_object_copy_.15328
- __Block_byref_object_copy_.17822
- __Block_byref_object_copy_.20932
- __Block_byref_object_copy_.22252
- __Block_byref_object_copy_.23315
- __Block_byref_object_copy_.24543
- __Block_byref_object_copy_.25226
- __Block_byref_object_copy_.27892
- __Block_byref_object_copy_.29048
- __Block_byref_object_copy_.7232
- __Block_byref_object_copy_.9750
- __Block_byref_object_dispose_.12835
- __Block_byref_object_dispose_.15329
- __Block_byref_object_dispose_.17823
- __Block_byref_object_dispose_.20933
- __Block_byref_object_dispose_.22253
- __Block_byref_object_dispose_.23316
- __Block_byref_object_dispose_.24544
- __Block_byref_object_dispose_.25227
- __Block_byref_object_dispose_.27893
- __Block_byref_object_dispose_.29049
- __Block_byref_object_dispose_.7233
- __Block_byref_object_dispose_.9751
- __block_descriptor_tmp.20130
- __block_descriptor_tmp.24016
- __block_descriptor_tmp.26102
- __block_descriptor_tmp.26719
- __block_literal_global.10.15877
- __block_literal_global.10.9395
- __block_literal_global.10354
- __block_literal_global.13133
- __block_literal_global.13500
- __block_literal_global.14.22777
- __block_literal_global.14.26332
- __block_literal_global.14455
- __block_literal_global.14634
- __block_literal_global.15330
- __block_literal_global.15879
- __block_literal_global.16471
- __block_literal_global.16713
- __block_literal_global.17399
- __block_literal_global.17830
- __block_literal_global.18282
- __block_literal_global.18419
- __block_literal_global.18730
- __block_literal_global.19.14468
- __block_literal_global.19.18410
- __block_literal_global.20039
- __block_literal_global.20717
- __block_literal_global.21239
- __block_literal_global.22.14469
- __block_literal_global.22.18416
- __block_literal_global.22347
- __block_literal_global.22782
- __block_literal_global.23180
- __block_literal_global.23929
- __block_literal_global.24014
- __block_literal_global.24477
- __block_literal_global.24628
- __block_literal_global.24737
- __block_literal_global.24783
- __block_literal_global.24977
- __block_literal_global.26050
- __block_literal_global.26100
- __block_literal_global.26336
- __block_literal_global.26442
- __block_literal_global.26825
- __block_literal_global.27382
- __block_literal_global.27470
- __block_literal_global.27619
- __block_literal_global.27858
- __block_literal_global.28.27896
- __block_literal_global.28.5709
- __block_literal_global.28410
- __block_literal_global.29101
- __block_literal_global.4.14458
- __block_literal_global.5730
- __block_literal_global.63.20712
- __block_literal_global.7.26040
- __block_literal_global.7262
- __block_literal_global.73.26437
- __block_literal_global.7486
- __block_literal_global.7670
- __block_literal_global.8071
- __block_literal_global.9393
- _extensionAuxiliaryHostProtocol.protocol.20713
- _extensionAuxiliaryHostProtocol.protocol.24784
- _extensionAuxiliaryHostProtocol.protocol.26438
- _extensionAuxiliaryHostProtocol.protocolInit.20711
- _extensionAuxiliaryHostProtocol.protocolInit.24782
- _extensionAuxiliaryHostProtocol.protocolInit.26436
- _extensionAuxiliaryVendorProtocol.protocol.20718
- _extensionAuxiliaryVendorProtocol.protocol.26443
- _extensionAuxiliaryVendorProtocol.protocolInit.20716
- _extensionAuxiliaryVendorProtocol.protocolInit.26441
- convert_error_to_string.25219
- driverInterface.driverInterface.10351
- driverInterface.driverInterface.17400
- driverInterface.driverInterface.21236
- driverInterface.driverInterface.22778
- driverInterface.driverInterface.7664
- driverInterface.onceToken.10350
- driverInterface.onceToken.17398
- driverInterface.onceToken.21235
- driverInterface.onceToken.22776
- driverInterface.onceToken.7663
- g_noAppFilter.29022
- globalConfigurationManager.gChangeQueue.18414
- globalConfigurationManager.gChangeQueue.5728
- globalConfigurationManager.gConfigurationManager.18411
- globalConfigurationManager.gConfigurationManager.5726
- globalConfigurationManager.onceToken.18409
- globalConfigurationManager.onceToken.5725
- initGlobals.onceToken.16712
- loadedManagers.loadedManagers.27856
- loadedManagers.loadedManagers.29025
- loadedManagers.managers_init.27855
- loadedManagers.managers_init.29024
- managerInterface.managerInterface.10355
- managerInterface.managerInterface.21240
- managerInterface.managerInterface.22783
- managerInterface.onceToken.10353
- managerInterface.onceToken.21238
- managerInterface.onceToken.22781
- sharedManager.g_manager.27471
- sharedManager.g_manager.7487
- sharedManager.g_manager.8072
- sharedManager.init_manager.7485
- sharedManager.init_manager.8070
- sharedManager.onceToken.18418
- sharedManager.onceToken.27469
- sharedManager.onceToken.29100
- sharedManager.onceToken.5729

```

## EOF
