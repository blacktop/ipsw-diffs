## PassKitCore

> `/System/Library/PrivateFrameworks/PassKitCore.framework/PassKitCore`

```diff

-1642.5.18.0.0
-  __TEXT.__text: 0x8419bc
+1642.6.1.0.0
+  __TEXT.__text: 0x841f00
   __TEXT.__auth_stubs: 0x4a60
-  __TEXT.__objc_methlist: 0x6e824
+  __TEXT.__objc_methlist: 0x6e854
   __TEXT.__const: 0x251a8
   __TEXT.__swift5_typeref: 0x637c
-  __TEXT.__cstring: 0x689b5
-  __TEXT.__constg_swiftt: 0x53c8
-  __TEXT.__swift5_reflstr: 0x466d
-  __TEXT.__swift5_fieldmd: 0x55d8
+  __TEXT.__cstring: 0x68a37
+  __TEXT.__constg_swiftt: 0x53e0
+  __TEXT.__swift5_reflstr: 0x468d
+  __TEXT.__swift5_fieldmd: 0x55e4
   __TEXT.__swift5_builtin: 0x3e8
   __TEXT.__swift5_assocty: 0x978
   __TEXT.__swift5_proto: 0xcb8

   __TEXT.__swift5_types2: 0x4
   __TEXT.__gcc_except_tab: 0x7780
   __TEXT.__ustring: 0x1e7a
-  __TEXT.__unwind_info: 0x1f140
+  __TEXT.__unwind_info: 0x1f158
   __TEXT.__eh_frame: 0x4ba0
   __TEXT.__objc_classname: 0x1109d
-  __TEXT.__objc_methname: 0xd0ffd
-  __TEXT.__objc_methtype: 0x190d3
-  __TEXT.__objc_stubs: 0x5d680
+  __TEXT.__objc_methname: 0xd10cd
+  __TEXT.__objc_methtype: 0x190f3
+  __TEXT.__objc_stubs: 0x5d6a0
   __DATA_CONST.__got: 0x4b18
-  __DATA_CONST.__const: 0x21a68
+  __DATA_CONST.__const: 0x21a80
   __DATA_CONST.__objc_classlist: 0x3c00
   __DATA_CONST.__objc_catlist: 0x110
   __DATA_CONST.__objc_protolist: 0x590
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x23cc0
+  __DATA_CONST.__objc_selrefs: 0x23ce0
   __DATA_CONST.__objc_protorefs: 0x250
   __DATA_CONST.__objc_superrefs: 0x3020
   __DATA_CONST.__objc_arraydata: 0x28e8
   __AUTH_CONST.__auth_got: 0x2540
   __AUTH_CONST.__const: 0x1ecd8
-  __AUTH_CONST.__cfstring: 0x73820
-  __AUTH_CONST.__objc_const: 0xc7ee0
+  __AUTH_CONST.__cfstring: 0x73880
+  __AUTH_CONST.__objc_const: 0xc7f40
   __AUTH_CONST.__objc_arrayobj: 0xd68
   __AUTH_CONST.__objc_intobj: 0x1080
   __AUTH_CONST.__objc_dictobj: 0x15b8
   __AUTH_CONST.__objc_doubleobj: 0x2b0
-  __AUTH.__objc_data: 0x20f40
+  __AUTH.__objc_data: 0x20f60
   __AUTH.__data: 0x3eb0
   __AUTH.__thread_vars: 0x18
   __AUTH.__thread_bss: 0x8
-  __DATA.__objc_ivar: 0x6ea8
-  __DATA.__data: 0x8068
+  __DATA.__objc_ivar: 0x6eac
+  __DATA.__data: 0x8098
   __DATA.__bss: 0x18400
   __DATA.__common: 0xc00
   __DATA_DIRTY.__objc_ivar: 0x1e34

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: D2CCA039-1648-3EAD-9087-B73D6DA6123A
-  Functions: 50573
-  Symbols:   131422
-  CStrings:  68748
+  UUID: 2C10E246-57CF-39C8-8375-1FD15A960E5A
+  Functions: 50583
+  Symbols:   131442
+  CStrings:  68762
 
Symbols:
+ -[PKInAppPaymentService paymentServicesMerchantURLForAPIType:isDelegated:completion:]
+ -[PKPaymentSetupFieldsModel disableCVVPrefill]
+ -[PKPaymentSetupFieldsModel setDisableCVVPrefill:]
+ GCC_except_table220
+ GCC_except_table458
+ GCC_except_table675
+ GCC_except_table718
+ GCC_except_table726
+ _.str.273
+ _.str.287
+ _.str.293
+ _.str.301
+ _.str.315
+ _.str.899
+ _OBJC_IVAR_$_PKPaymentSetupFieldsModel._disableCVVPrefill
+ _PKCashCIPReloadEnabled
+ _PKPeerPaymentDismissedPeerPaymentCompleteVerification
+ _PKPeerPaymentDismissedPeerPaymentIDVOffer
+ _PKPeerPaymentHasDismissedPeerPaymentCompleteVerification
+ _PKPeerPaymentHasDismissedPeerPaymentIDVOffer
+ _PKPeerPaymentSetHasDismissedPeerPaymentCompleteVerification
+ _PKPeerPaymentSetHasDismissedPeerPaymentIDVOffer
+ __OBJC_$_PROP_LIST_PKPaymentSetupFieldsModel
+ ___59-[PKInAppPaymentService secureElementStatusWithCompletion:]_block_invoke.41
+ ___66-[PKInAppPaymentService paymentHardwareStatusWithType:completion:]_block_invoke.43
+ ___72-[PKInAppPaymentService cardsAvailableForAMPWithCountryCode:completion:]_block_invoke.44
+ ___78-[PKInAppPaymentService cardDataForMerchantIdentifier:countryCode:completion:]_block_invoke.46
+ ___84-[PKInAppPaymentService validatePayLaterMerchandisingConfiguration:type:completion:]_block_invoke.50
+ ___85-[PKInAppPaymentService paymentServicesMerchantURLForAPIType:isDelegated:completion:]_block_invoke
+ ___85-[PKInAppPaymentService paymentServicesMerchantURLForAPIType:isDelegated:completion:]_block_invoke.39
+ ___90-[PKInAppPaymentService enrollPaymentPassWithUniqueIdentifier:merchantSession:completion:]_block_invoke.48
+ ___93-[PKInAppPaymentService registerInterfaceAvailableForAdditionalPaymentRequestWithCompletion:]_block_invoke.52
+ ___95-[PKInAppPaymentService unregisterInterfaceAvailableForAdditionalPaymentRequestWithCompletion:]_block_invoke.53
+ ___PKPeerPaymentRemoveRecurringPaymentRecentMemoIcon_block_invoke.1137
+ ___PKRequestContactAccessWithCompletion_block_invoke.324
+ ___block_literal_global.1009
+ ___block_literal_global.1011
+ ___block_literal_global.1026
+ ___block_literal_global.1039
+ ___block_literal_global.1043
+ ___block_literal_global.1048
+ ___block_literal_global.1059
+ ___block_literal_global.1062
+ ___block_literal_global.1090
+ ___block_literal_global.1095
+ ___block_literal_global.1097
+ ___block_literal_global.1102
+ ___block_literal_global.1107
+ ___block_literal_global.1112
+ ___block_literal_global.1117
+ ___block_literal_global.1122
+ ___block_literal_global.1127
+ ___block_literal_global.1132
+ ___block_literal_global.1137
+ ___block_literal_global.1139
+ ___block_literal_global.1147
+ ___block_literal_global.1183
+ ___block_literal_global.1185
+ ___block_literal_global.1262
+ ___block_literal_global.1267
+ ___block_literal_global.1271
+ ___block_literal_global.1277
+ ___block_literal_global.1286
+ ___block_literal_global.1300
+ ___block_literal_global.1458
+ ___block_literal_global.1460
+ ___block_literal_global.1463
+ ___block_literal_global.1699
+ ___block_literal_global.1701
+ ___block_literal_global.1706
+ ___block_literal_global.1710
+ ___block_literal_global.1724
+ ___block_literal_global.1726
+ ___block_literal_global.1731
+ ___block_literal_global.1745
+ ___block_literal_global.1751
+ ___block_literal_global.1754
+ ___block_literal_global.1756
+ ___block_literal_global.1758
+ ___block_literal_global.1760
+ ___block_literal_global.1762
+ ___block_literal_global.1765
+ ___block_literal_global.310
+ ___block_literal_global.330
+ ___block_literal_global.335
+ ___block_literal_global.340
+ ___block_literal_global.432
+ ___block_literal_global.440
+ ___block_literal_global.703
+ ___block_literal_global.708
+ ___block_literal_global.714
+ ___block_literal_global.719
+ ___block_literal_global.724
+ ___block_literal_global.729
+ ___block_literal_global.734
+ ___block_literal_global.739
+ ___block_literal_global.749
+ ___block_literal_global.751
+ ___block_literal_global.789
+ ___block_literal_global.792
+ ___block_literal_global.794
+ ___block_literal_global.952
+ ___block_literal_global.967
+ ___block_literal_global.974
+ ___block_literal_global.980
+ ___block_literal_global.982
+ ___block_literal_global.984
+ _block_copy_helper.117
+ _block_copy_helper.84
+ _block_descriptor.119
+ _block_descriptor.86
+ _block_destroy_helper.118
+ _block_destroy_helper.85
+ _objc_msgSend$paymentServicesMerchantURLForAPIType:isDelegated:completion:
+ _objc_msgSend$paymentServicesMerchantURLForAPIType:isDelegated:handler:
- GCC_except_table219
- GCC_except_table457
- GCC_except_table674
- GCC_except_table717
- GCC_except_table725
- _.str.270
- _.str.284
- _.str.290
- _.str.299
- _.str.313
- _.str.898
- ___59-[PKInAppPaymentService secureElementStatusWithCompletion:]_block_invoke.40
- ___66-[PKInAppPaymentService paymentHardwareStatusWithType:completion:]_block_invoke.42
- ___72-[PKInAppPaymentService cardsAvailableForAMPWithCountryCode:completion:]_block_invoke.43
- ___78-[PKInAppPaymentService cardDataForMerchantIdentifier:countryCode:completion:]_block_invoke.45
- ___84-[PKInAppPaymentService validatePayLaterMerchandisingConfiguration:type:completion:]_block_invoke.49
- ___90-[PKInAppPaymentService enrollPaymentPassWithUniqueIdentifier:merchantSession:completion:]_block_invoke.47
- ___93-[PKInAppPaymentService registerInterfaceAvailableForAdditionalPaymentRequestWithCompletion:]_block_invoke.51
- ___95-[PKInAppPaymentService unregisterInterfaceAvailableForAdditionalPaymentRequestWithCompletion:]_block_invoke.52
- ___PKPeerPaymentRemoveRecurringPaymentRecentMemoIcon_block_invoke.1131
- ___PKRequestContactAccessWithCompletion_block_invoke.323
- ___block_literal_global.1008
- ___block_literal_global.1010
- ___block_literal_global.1016
- ___block_literal_global.1025
- ___block_literal_global.1038
- ___block_literal_global.1040
- ___block_literal_global.1042
- ___block_literal_global.1058
- ___block_literal_global.1061
- ___block_literal_global.1089
- ___block_literal_global.1094
- ___block_literal_global.1096
- ___block_literal_global.1101
- ___block_literal_global.1106
- ___block_literal_global.1111
- ___block_literal_global.1116
- ___block_literal_global.1126
- ___block_literal_global.1131
- ___block_literal_global.1138
- ___block_literal_global.1146
- ___block_literal_global.1179
- ___block_literal_global.1182
- ___block_literal_global.1261
- ___block_literal_global.1266
- ___block_literal_global.1270
- ___block_literal_global.1273
- ___block_literal_global.1276
- ___block_literal_global.1285
- ___block_literal_global.1299
- ___block_literal_global.1457
- ___block_literal_global.1459
- ___block_literal_global.1462
- ___block_literal_global.1698
- ___block_literal_global.1700
- ___block_literal_global.1705
- ___block_literal_global.1709
- ___block_literal_global.1723
- ___block_literal_global.1725
- ___block_literal_global.1730
- ___block_literal_global.1744
- ___block_literal_global.1750
- ___block_literal_global.1753
- ___block_literal_global.1755
- ___block_literal_global.1757
- ___block_literal_global.1759
- ___block_literal_global.1761
- ___block_literal_global.1764
- ___block_literal_global.307
- ___block_literal_global.309
- ___block_literal_global.329
- ___block_literal_global.334
- ___block_literal_global.339
- ___block_literal_global.395
- ___block_literal_global.431
- ___block_literal_global.436
- ___block_literal_global.439
- ___block_literal_global.702
- ___block_literal_global.707
- ___block_literal_global.713
- ___block_literal_global.718
- ___block_literal_global.723
- ___block_literal_global.728
- ___block_literal_global.733
- ___block_literal_global.738
- ___block_literal_global.743
- ___block_literal_global.748
- ___block_literal_global.750
- ___block_literal_global.788
- ___block_literal_global.791
- ___block_literal_global.793
- ___block_literal_global.95
- ___block_literal_global.951
- ___block_literal_global.966
- ___block_literal_global.968
- ___block_literal_global.971
- ___block_literal_global.973
- ___block_literal_global.975
- ___block_literal_global.977
- ___block_literal_global.979
- ___block_literal_global.981
- ___block_literal_global.983
- _block_copy_helper.110
- _block_copy_helper.114
- _block_copy_helper.73
- _block_descriptor.112
- _block_descriptor.116
- _block_descriptor.75
- _block_destroy_helper.111
- _block_destroy_helper.115
- _block_destroy_helper.74
- _objc_msgSend$paymentServicesMerchantURLForAPIType:completion:
CStrings:
+ "AppleCashCIPReload"
+ "PKPeerPaymentDismissedPeerPaymentCompleteVerification"
+ "PKPeerPaymentDismissedPeerPaymentIDVOffer"
+ "TB,N,V_disableCVVPrefill"
+ "_disableCVVPrefill"
+ "cardActivation"
+ "disableCVVPrefill"
+ "paymentServicesMerchantURLForAPIType:isDelegated:completion:"
+ "paymentServicesMerchantURLForAPIType:isDelegated:handler:"
+ "setDisableCVVPrefill:"
+ "v36@0:8q16B24@?<v@?B@\"NSURL\">28"

```
