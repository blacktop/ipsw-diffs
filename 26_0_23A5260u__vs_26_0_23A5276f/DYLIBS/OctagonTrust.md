## OctagonTrust

> `/System/Library/PrivateFrameworks/OctagonTrust.framework/OctagonTrust`

```diff

-61901.0.9.0.1
-  __TEXT.__text: 0x22a64
+61901.0.33.0.2
+  __TEXT.__text: 0x22a60
   __TEXT.__auth_stubs: 0x6e0
-  __TEXT.__objc_methlist: 0x193c
+  __TEXT.__objc_methlist: 0x194c
   __TEXT.__const: 0x100
   __TEXT.__gcc_except_tab: 0xb74
-  __TEXT.__cstring: 0x165c
+  __TEXT.__cstring: 0x167f
   __TEXT.__dlopen_cstrs: 0xb0
   __TEXT.__oslogstring: 0x293e
   __TEXT.__unwind_info: 0x750
   __TEXT.__objc_classname: 0x203
-  __TEXT.__objc_methname: 0x3f0b
-  __TEXT.__objc_methtype: 0x5ca
-  __TEXT.__objc_stubs: 0x2840
+  __TEXT.__objc_methname: 0x3f00
+  __TEXT.__objc_methtype: 0x5b3
+  __TEXT.__objc_stubs: 0x2860
   __DATA_CONST.__got: 0x208
   __DATA_CONST.__const: 0x2a8
   __DATA_CONST.__objc_classlist: 0x90
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xf20
+  __DATA_CONST.__objc_selrefs: 0xf28
   __DATA_CONST.__objc_superrefs: 0x88
   __AUTH_CONST.__auth_got: 0x380
-  __AUTH_CONST.__cfstring: 0x13c0
-  __AUTH_CONST.__objc_const: 0x2418
+  __AUTH_CONST.__cfstring: 0x13e0
+  __AUTH_CONST.__objc_const: 0x2448
   __AUTH.__objc_data: 0x50
-  __DATA.__objc_ivar: 0x180
+  __DATA.__objc_ivar: 0x184
   __DATA.__data: 0x138
   __DATA.__bss: 0x168
   __DATA_DIRTY.__objc_data: 0x550

   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 3412BF02-1B26-39AD-8116-BFA931399908
-  Functions: 636
-  Symbols:   2141
-  CStrings:  1322
+  UUID: 49C68E24-F8B9-3AFF-95CC-5FB18BD0E5B5
+  Functions: 637
+  Symbols:   2145
+  CStrings:  1326
 
Symbols:
+ -[OTEscrowCheckCallResult repairDisabled]
+ -[OTEscrowCheckCallResult setRepairDisabled:]
+ GCC_except_table380
+ GCC_except_table385
+ GCC_except_table391
+ GCC_except_table393
+ GCC_except_table395
+ GCC_except_table397
+ GCC_except_table399
+ GCC_except_table401
+ GCC_except_table403
+ GCC_except_table405
+ GCC_except_table407
+ GCC_except_table409
+ GCC_except_table411
+ GCC_except_table413
+ GCC_except_table415
+ GCC_except_table420
+ GCC_except_table425
+ GCC_except_table427
+ GCC_except_table430
+ GCC_except_table433
+ GCC_except_table439
+ GCC_except_table441
+ GCC_except_table443
+ GCC_except_table446
+ GCC_except_table449
+ _CloudServicesLibrary.736
+ _CloudServicesLibraryCore.frameworkLibrary.737
+ _OBJC_IVAR_$_OTEscrowCheckCallResult._repairDisabled
+ ___CloudServicesLibraryCore_block_invoke.738
+ ___getkSecureBackupRecordIDKeySymbolLoc_block_invoke.758
+ ___getkSecureBackupRecordLabelKeySymbolLoc_block_invoke.756
+ _audit_stringCloudServices.739
+ _getkSecureBackupRecordIDKeySymbolLoc.ptr.757
+ _getkSecureBackupRecordLabelKeySymbolLoc.ptr.755
+ _objc_msgSend$repairDisabled
- -[OTEscrowCheckCallResult initWithNeedsReenroll:octagonTrusted:secureTermsNeeded:moveRequest:repairReason:]
- GCC_except_table379
- GCC_except_table384
- GCC_except_table390
- GCC_except_table392
- GCC_except_table394
- GCC_except_table396
- GCC_except_table398
- GCC_except_table400
- GCC_except_table402
- GCC_except_table404
- GCC_except_table406
- GCC_except_table408
- GCC_except_table410
- GCC_except_table412
- GCC_except_table414
- GCC_except_table419
- GCC_except_table424
- GCC_except_table426
- GCC_except_table429
- GCC_except_table432
- GCC_except_table438
- GCC_except_table440
- GCC_except_table442
- GCC_except_table445
- GCC_except_table448
- _CloudServicesLibrary.730
- _CloudServicesLibraryCore.frameworkLibrary.731
- ___CloudServicesLibraryCore_block_invoke.732
- ___getkSecureBackupRecordIDKeySymbolLoc_block_invoke.752
- ___getkSecureBackupRecordLabelKeySymbolLoc_block_invoke.750
- _audit_stringCloudServices.733
- _getkSecureBackupRecordIDKeySymbolLoc.ptr.751
- _getkSecureBackupRecordLabelKeySymbolLoc.ptr.749
Functions:
+ -[OTEscrowCheckCallResult moveRequest]
+ -[OTEscrowCheckCallResult setSecureTermsNeeded:]
~ -[OTEscrowCheckCallResult dictionaryRepresentation] : 392 -> 448
~ -[OTEscrowCheckCallResult encodeWithCoder:] : 220 -> 248
~ -[OTEscrowCheckCallResult initWithCoder:] : 220 -> 240
~ -[OTEscrowCheckCallResult description] : 208 -> 244
- -[OTEscrowCheckCallResult initWithNeedsReenroll:octagonTrusted:secureTermsNeeded:moveRequest:repairReason:]
CStrings:
+ "<OTEscrowCheckCallResult: needsReenroll: %@, octagonTrusted: %@, moveRequest? %@, secureTermsNeeded? %@, repairReason: %ld, repairDisabled: %@>"
+ "TB,V_repairDisabled"
+ "_repairDisabled"
+ "repairDisabled"
+ "setRepairDisabled:"
- "<OTEscrowCheckCallResult: needsReenroll: %@, octagonTrusted: %@, moveRequest? %@, secureTermsNeeded? %@, repairReason: %ld,"
- "@44@0:8B16B20B24@28q36"
- "initWithNeedsReenroll:octagonTrusted:secureTermsNeeded:moveRequest:repairReason:"

```
