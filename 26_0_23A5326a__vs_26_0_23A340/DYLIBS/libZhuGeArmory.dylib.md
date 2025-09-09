## libZhuGeArmory.dylib

> `/System/Library/PrivateFrameworks/AppleDeviceQuerySupport.framework/libZhuGeArmory.dylib`

```diff

 396.0.9.0.0
-  __TEXT.__text: 0x22a60
-  __TEXT.__auth_stubs: 0x9a0
-  __TEXT.__objc_methlist: 0x81c
+  __TEXT.__text: 0x2350c
+  __TEXT.__auth_stubs: 0x9c0
+  __TEXT.__objc_methlist: 0x824
   __TEXT.__const: 0x4b8
-  __TEXT.__cstring: 0xa01c
+  __TEXT.__cstring: 0xa1ef
   __TEXT.__gcc_except_tab: 0x18c
   __TEXT.__oslogstring: 0x1af
-  __TEXT.__unwind_info: 0x3d8
+  __TEXT.__unwind_info: 0x3e0
   __TEXT.__objc_classname: 0x181
-  __TEXT.__objc_methname: 0x1cd2
+  __TEXT.__objc_methname: 0x1cf0
   __TEXT.__objc_methtype: 0x32c
   __TEXT.__objc_stubs: 0x1bc0
   __DATA_CONST.__got: 0x198

   __DATA_CONST.__objc_classlist: 0x70
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x850
+  __DATA_CONST.__objc_selrefs: 0x858
   __DATA_CONST.__objc_superrefs: 0x10
-  __DATA_CONST.__objc_arraydata: 0x748
-  __AUTH_CONST.__auth_got: 0x4e0
+  __DATA_CONST.__objc_arraydata: 0x7f8
+  __AUTH_CONST.__auth_got: 0x4f0
   __AUTH_CONST.__const: 0x300
-  __AUTH_CONST.__cfstring: 0x7fc0
+  __AUTH_CONST.__cfstring: 0x8140
   __AUTH_CONST.__objc_const: 0xe68
   __AUTH_CONST.__objc_intobj: 0x1f8
-  __AUTH_CONST.__objc_dictobj: 0x758
-  __AUTH_CONST.__objc_arrayobj: 0x7f8
+  __AUTH_CONST.__objc_dictobj: 0x848
+  __AUTH_CONST.__objc_arrayobj: 0x840
   __AUTH.__objc_data: 0x190
   __DATA.__objc_ivar: 0x60
   __DATA.__data: 0xa24

   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/PrivateFrameworks/BiometricKit.framework/BiometricKit
+  - /System/Library/PrivateFrameworks/Centauri.framework/Centauri
   - /System/Library/PrivateFrameworks/MSUDataAccessor.framework/MSUDataAccessor
   - /System/Library/PrivateFrameworks/NearField.framework/NearField
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libnfrestore.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 3289452F-40B7-397B-9E4F-969049395F69
-  Functions: 335
-  Symbols:   1402
-  CStrings:  2610
+  - /usr/lib/updaters/libCentauriUpdater.dylib
+  UUID: CFD6625F-02E4-3873-987B-D9C485EC39C4
+  Functions: 337
+  Symbols:   1408
+  CStrings:  2637
 
Symbols:
+ +[ZhuGeKeysActionArmory queryCentauriSikPubWithError:]
+ GCC_except_table21
+ GCC_except_table44
+ GCC_except_table53
+ _CENGetSiKPublicKey
+ _CentauriUpdaterCopySiKPublicKey
+ _logCallbackForSyslogWithContextBuffer
- GCC_except_table20
- GCC_except_table40
- GCC_except_table45
Functions:
+ _logCallbackForSyslogWithContextBuffer
+ +[ZhuGeKeysActionArmory queryCentauriSikPubWithError:]
~ ___getConfigDict_block_invoke : 33120 -> 35380
CStrings:
+ "+[ZhuGeKeysActionArmory queryCentauriSikPubWithError:]"
+ "CENGetSiKPublicKey is not supported!"
+ "CentauriUpdaterCopySiKPublicKey is not supported!"
+ "ChipID"
+ "ECID"
+ "Failed to query Centauri Sik Pub!"
+ "centauri"
+ "kUmcdgObIa1Tmrury+vs80E+P7feurT7fjeBoSNzOjBrM"
+ "logCallbackForSyslogWithContextBuffer"
+ "qcLoMoHuqwN9l2o0uaPaq0FGgheBaItLe5TCoQ5VCxqiw"
+ "qjRH5QM3m6nH/auYOa6eC0D5vPWulgi0+VLCngICk+c2w"
+ "queryCentauriSikPubWithError:"
+ "tritium-mando-uid"
+ "yTyKhgkJ+N+ZMHJDz95Gb0BK1bLAMFxFm3aqAYh69bBo8"

```
