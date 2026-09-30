## CoreTelephony

> `/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`

```diff

-13077.0.0.0.0
-  __TEXT.__text: 0x18d588
-  __TEXT.__auth_stubs: 0x1980
-  __TEXT.__objc_methlist: 0x1b29c
-  __TEXT.__const: 0x100a
-  __TEXT.__gcc_except_tab: 0x1dc8c
-  __TEXT.__cstring: 0x1f745
+13080.2.0.0.0
+  __TEXT.__text: 0x18e930
+  __TEXT.__auth_stubs: 0x1990
+  __TEXT.__objc_methlist: 0x1b42c
+  __TEXT.__const: 0x1002
+  __TEXT.__gcc_except_tab: 0x1def0
+  __TEXT.__cstring: 0x1f7e5
   __TEXT.__oslogstring: 0x4368
   __TEXT.__swift5_typeref: 0x17
-  __TEXT.__unwind_info: 0xd0f8
-  __TEXT.__objc_classname: 0x58f3
-  __TEXT.__objc_methname: 0x22aeb
-  __TEXT.__objc_methtype: 0x7286
-  __TEXT.__objc_stubs: 0x16ba0
-  __DATA_CONST.__got: 0xaf0
-  __DATA_CONST.__const: 0x74b0
-  __DATA_CONST.__objc_classlist: 0x1520
+  __TEXT.__unwind_info: 0xd1d0
+  __TEXT.__objc_classname: 0x5928
+  __TEXT.__objc_methname: 0x22c57
+  __TEXT.__objc_methtype: 0x72e4
+  __TEXT.__objc_stubs: 0x16ce0
+  __DATA_CONST.__got: 0xb00
+  __DATA_CONST.__const: 0x7388
+  __DATA_CONST.__objc_classlist: 0x1530
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x250
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x7798
+  __DATA_CONST.__objc_selrefs: 0x77e8
   __DATA_CONST.__objc_protorefs: 0x48
-  __DATA_CONST.__objc_superrefs: 0x1790
+  __DATA_CONST.__objc_superrefs: 0x17a0
   __DATA_CONST.__objc_arraydata: 0x20
-  __AUTH_CONST.__auth_got: 0xcd8
-  __AUTH_CONST.__const: 0x1ec0
-  __AUTH_CONST.__cfstring: 0x1d980
-  __AUTH_CONST.__objc_const: 0x2f658
+  __AUTH_CONST.__auth_got: 0xce0
+  __AUTH_CONST.__const: 0x2080
+  __AUTH_CONST.__cfstring: 0x1da80
+  __AUTH_CONST.__objc_const: 0x2f928
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH_CONST.__objc_arrayobj: 0x30
-  __AUTH.__objc_data: 0xa8c0
-  __DATA.__objc_ivar: 0x1420
+  __AUTH.__objc_data: 0xa960
+  __DATA.__objc_ivar: 0x1438
   __DATA.__data: 0x1f88
   __DATA.__bss: 0x198
   __DATA.__common: 0x10

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  UUID: E3301E91-CFE9-3F2C-B5D6-DF45CA005A9D
-  Functions: 11239
-  Symbols:   38133
-  CStrings:  17063
+  UUID: E9A51677-1082-3A76-B5EF-E9C2542F5304
+  Functions: 11280
+  Symbols:   38265
+  CStrings:  17103
 
Symbols:
+ +[CTLazuliOriginalMessageID supportsSecureCoding]
+ +[CTLazuliSecureGroupVersion supportsSecureCoding]
+ -[CTLazuliMessageID originalId]
+ -[CTLazuliMessageID secureGroupVersion]
+ -[CTLazuliMessageID setOriginalId:]
+ -[CTLazuliMessageID setSecureGroupVersion:]
+ -[CTLazuliOriginalMessageID .cxx_destruct]
+ -[CTLazuliOriginalMessageID copyWithZone:]
+ -[CTLazuliOriginalMessageID description]
+ -[CTLazuliOriginalMessageID encodeWithCoder:]
+ -[CTLazuliOriginalMessageID initWithCoder:]
+ -[CTLazuliOriginalMessageID initWithReflection:]
+ -[CTLazuliOriginalMessageID isEqual:]
+ -[CTLazuliOriginalMessageID isEqualToCTLazuliOriginalMessageID:]
+ -[CTLazuliOriginalMessageID secureGroupVersion]
+ -[CTLazuliOriginalMessageID setSecureGroupVersion:]
+ -[CTLazuliOriginalMessageID setUuid:]
+ -[CTLazuliOriginalMessageID uuid]
+ -[CTLazuliSecureGroupVersion .cxx_destruct]
+ -[CTLazuliSecureGroupVersion copyWithZone:]
+ -[CTLazuliSecureGroupVersion description]
+ -[CTLazuliSecureGroupVersion encodeWithCoder:]
+ -[CTLazuliSecureGroupVersion epoch]
+ -[CTLazuliSecureGroupVersion era]
+ -[CTLazuliSecureGroupVersion initWithCoder:]
+ -[CTLazuliSecureGroupVersion initWithReflection:]
+ -[CTLazuliSecureGroupVersion isEqual:]
+ -[CTLazuliSecureGroupVersion isEqualToCTLazuliSecureGroupVersion:]
+ -[CTLazuliSecureGroupVersion setEpoch:]
+ -[CTLazuliSecureGroupVersion setEra:]
+ GCC_except_table393
+ GCC_except_table394
+ GCC_except_table434
+ GCC_except_table469
+ GCC_except_table492
+ GCC_except_table497
+ GCC_except_table501
+ GCC_except_table504
+ GCC_except_table512
+ GCC_except_table516
+ GCC_except_table568
+ GCC_except_table595
+ GCC_except_table610
+ GCC_except_table632
+ GCC_except_table635
+ GCC_except_table643
+ GCC_except_table644
+ GCC_except_table647
+ GCC_except_table658
+ GCC_except_table669
+ GCC_except_table679
+ GCC_except_table681
+ GCC_except_table682
+ GCC_except_table683
+ GCC_except_table684
+ GCC_except_table685
+ GCC_except_table706
+ GCC_except_table710
+ GCC_except_table756
+ GCC_except_table758
+ GCC_except_table762
+ GCC_except_table766
+ GCC_except_table794
+ GCC_except_table795
+ GCC_except_table798
+ GCC_except_table799
+ GCC_except_table800
+ GCC_except_table801
+ GCC_except_table805
+ GCC_except_table807
+ GCC_except_table808
+ GCC_except_table809
+ GCC_except_table810
+ GCC_except_table812
+ GCC_except_table813
+ GCC_except_table815
+ GCC_except_table817
+ GCC_except_table822
+ GCC_except_table823
+ GCC_except_table827
+ _OBJC_CLASS_$_CTLazuliOriginalMessageID
+ _OBJC_CLASS_$_CTLazuliSecureGroupVersion
+ _OBJC_IVAR_$_CTLazuliMessageID._originalId
+ _OBJC_IVAR_$_CTLazuliMessageID._secureGroupVersion
+ _OBJC_IVAR_$_CTLazuliOriginalMessageID._secureGroupVersion
+ _OBJC_IVAR_$_CTLazuliOriginalMessageID._uuid
+ _OBJC_IVAR_$_CTLazuliSecureGroupVersion._epoch
+ _OBJC_IVAR_$_CTLazuliSecureGroupVersion._era
+ _OBJC_METACLASS_$_CTLazuliOriginalMessageID
+ _OBJC_METACLASS_$_CTLazuliSecureGroupVersion
+ __OBJC_$_CLASS_METHODS_CTLazuliOriginalMessageID
+ __OBJC_$_CLASS_METHODS_CTLazuliSecureGroupVersion
+ __OBJC_$_CLASS_PROP_LIST_CTLazuliOriginalMessageID
+ __OBJC_$_CLASS_PROP_LIST_CTLazuliSecureGroupVersion
+ __OBJC_$_INSTANCE_METHODS_CTLazuliOriginalMessageID
+ __OBJC_$_INSTANCE_METHODS_CTLazuliSecureGroupVersion
+ __OBJC_$_INSTANCE_VARIABLES_CTLazuliOriginalMessageID
+ __OBJC_$_INSTANCE_VARIABLES_CTLazuliSecureGroupVersion
+ __OBJC_$_PROP_LIST_CTLazuliOriginalMessageID
+ __OBJC_$_PROP_LIST_CTLazuliSecureGroupVersion
+ __OBJC_CLASS_PROTOCOLS_$_CTLazuliOriginalMessageID
+ __OBJC_CLASS_PROTOCOLS_$_CTLazuliSecureGroupVersion
+ __OBJC_CLASS_RO_$_CTLazuliOriginalMessageID
+ __OBJC_CLASS_RO_$_CTLazuliSecureGroupVersion
+ __OBJC_METACLASS_RO_$_CTLazuliOriginalMessageID
+ __OBJC_METACLASS_RO_$_CTLazuliSecureGroupVersion
+ __Z21_CTHandleNotificationN3ctu2cf11CFSharedRefI20__CTServerConnectionEE7CTEventPxm11CFUUIDBytesPhS7_S7_
+ __ZL48_RegisterForLocalDaemonReadyNotificationIfNeededP20__CTServerConnection
+ __ZN14CSIPhoneNumber23setEmergencyCategoryURNERKNSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE
+ __ZNK14CSIPhoneNumber23getEmergencyCategoryURNEv
+ ____Z21_CTHandleNotificationN3ctu2cf11CFSharedRefI20__CTServerConnectionEE7CTEventPxm11CFUUIDBytesPhS7_S7__block_invoke
+ ____ZL19sHandleNotificationP13CTServerStateN3xpc4dictE_block_invoke.99
+ ___block_descriptor_tmp.100
+ ___block_descriptor_tmp.120
+ ___block_descriptor_tmp.131
+ ___block_descriptor_tmp.135
+ ___block_descriptor_tmp.44
+ ___block_descriptor_tmp.45
+ ___block_descriptor_tmp.73
+ ___block_descriptor_tmp.74
+ ___block_descriptor_tmp.80
+ ___block_descriptor_tmp.83
+ ___copy_helper_block_8_32c50_ZTSN3ctu2cf11CFSharedRefI20__CTServerConnectionEE
+ ___copy_helper_block_8_32c50_ZTSN3ctu2cf11CFSharedRefI20__CTServerConnectionEE48c21_ZTSN8dispatch5queueE
+ ___copy_helper_block_8_32c50_ZTSN3ctu2cf11CFSharedRefI20__CTServerConnectionEE48c41_ZTSN3ctu2cf11CFSharedRefIK10__CFStringEE56c45_ZTSN3ctu2cf11CFSharedRefIK14__CFDictionaryEE
+ ___copy_helper_block_8_32c50_ZTSN3ctu2cf11CFSharedRefI20__CTServerConnectionEE56c15_ZTSN3xpc4dictE
+ ___copy_helper_block_8_40c50_ZTSN3ctu2cf11CFSharedRefI20__CTServerConnectionEE
+ ___copy_helper_block_8_64c50_ZTSN3ctu2cf11CFSharedRefI20__CTServerConnectionEE
+ ___destroy_helper_block_8_32c50_ZTSN3ctu2cf11CFSharedRefI20__CTServerConnectionEE
+ ___destroy_helper_block_8_32c50_ZTSN3ctu2cf11CFSharedRefI20__CTServerConnectionEE48c21_ZTSN8dispatch5queueE
+ ___destroy_helper_block_8_32c50_ZTSN3ctu2cf11CFSharedRefI20__CTServerConnectionEE48c41_ZTSN3ctu2cf11CFSharedRefIK10__CFStringEE56c45_ZTSN3ctu2cf11CFSharedRefIK14__CFDictionaryEE
+ ___destroy_helper_block_8_32c50_ZTSN3ctu2cf11CFSharedRefI20__CTServerConnectionEE56c15_ZTSN3xpc4dictE
+ ___destroy_helper_block_8_40c50_ZTSN3ctu2cf11CFSharedRefI20__CTServerConnectionEE
+ ___destroy_helper_block_8_64c50_ZTSN3ctu2cf11CFSharedRefI20__CTServerConnectionEE
+ _nw_parameters_set_no_proxy
+ _objc_msgSend$epoch
+ _objc_msgSend$era
+ _objc_msgSend$isEqualToCTLazuliOriginalMessageID:
+ _objc_msgSend$isEqualToCTLazuliSecureGroupVersion:
+ _objc_msgSend$originalId
+ _objc_msgSend$secureGroupVersion
+ _objc_msgSend$setEpoch:
+ _objc_msgSend$setEra:
+ _objc_msgSend$setOriginalId:
+ _objc_msgSend$setSecureGroupVersion:
- GCC_except_table363
- GCC_except_table461
- GCC_except_table464
- GCC_except_table465
- GCC_except_table473
- GCC_except_table477
- GCC_except_table522
- GCC_except_table523
- GCC_except_table534
- GCC_except_table538
- GCC_except_table578
- GCC_except_table579
- GCC_except_table584
- GCC_except_table606
- GCC_except_table625
- GCC_except_table628
- GCC_except_table629
- GCC_except_table640
- GCC_except_table650
- GCC_except_table651
- GCC_except_table676
- GCC_except_table726
- GCC_except_table728
- GCC_except_table732
- GCC_except_table735
- GCC_except_table736
- GCC_except_table741
- GCC_except_table748
- GCC_except_table750
- GCC_except_table752
- GCC_except_table764
- GCC_except_table767
- GCC_except_table768
- GCC_except_table769
- GCC_except_table770
- GCC_except_table775
- GCC_except_table777
- GCC_except_table779
- GCC_except_table783
- GCC_except_table785
- GCC_except_table787
- GCC_except_table792
- GCC_except_table793
- __Z21_CTHandleNotificationP20__CTServerConnection7CTEventPxm11CFUUIDBytesPhS4_S4_
- ____Z21_CTHandleNotificationP20__CTServerConnection7CTEventPxm11CFUUIDBytesPhS4_S4__block_invoke
- ____ZL19sHandleNotificationP13CTServerStateN3xpc4dictE_block_invoke.95
- ___block_descriptor_tmp.103
- ___block_descriptor_tmp.112
- ___block_descriptor_tmp.119
- ___block_descriptor_tmp.43
- ___block_descriptor_tmp.79
- ___block_descriptor_tmp.96
- ___copy_helper_block_8_40c21_ZTSN8dispatch5queueE
- ___copy_helper_block_8_40c41_ZTSN3ctu2cf11CFSharedRefIK10__CFStringEE48c45_ZTSN3ctu2cf11CFSharedRefIK14__CFDictionaryEE
- ___destroy_helper_block_8_40c21_ZTSN8dispatch5queueE
- ___destroy_helper_block_8_40c41_ZTSN3ctu2cf11CFSharedRefIK10__CFStringEE48c45_ZTSN3ctu2cf11CFSharedRefIK14__CFDictionaryEE
CStrings:
+ ", epoch = %@"
+ ", era = %@"
+ ", originalId = %@"
+ ", secureGroupVersion = %@"
+ "13080.2"
+ "13080.2~1"
+ "@\"CTLazuliOriginalMessageID\""
+ "@\"CTLazuliSecureGroupVersion\""
+ "@24@0:8r^{SecureGroupVersion=QQ}16"
+ "CTLazuliOriginalMessageID"
+ "CTLazuliSecureGroupVersion"
+ "NegativeDeliveryFailureToDecrypt"
+ "T@\"CTLazuliOriginalMessageID\",C,N,V_originalId"
+ "T@\"CTLazuliSecureGroupVersion\",C,N,V_secureGroupVersion"
+ "T@\"NSNumber\",C,N,V_epoch"
+ "T@\"NSNumber\",C,N,V_era"
+ "_epoch"
+ "_era"
+ "_originalId"
+ "_secureGroupVersion"
+ "epoch"
+ "era"
+ "isEqualToCTLazuliOriginalMessageID:"
+ "isEqualToCTLazuliSecureGroupVersion:"
+ "kEpochKey"
+ "kEraKey"
+ "kOriginalIdKey"
+ "kSecureGroupVersionKey"
+ "originalId"
+ "secureGroupVersion"
+ "setEpoch:"
+ "setEra:"
+ "setOriginalId:"
+ "setSecureGroupVersion:"
- "13077"
- "13077~26"

```
