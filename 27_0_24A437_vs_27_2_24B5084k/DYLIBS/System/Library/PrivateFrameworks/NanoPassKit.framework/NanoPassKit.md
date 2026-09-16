## NanoPassKit

> `/System/Library/PrivateFrameworks/NanoPassKit.framework/NanoPassKit`

```diff

-1347.0.0.0.0
-  __TEXT.__text: 0x1e26fc
-  __TEXT.__objc_methlist: 0x1ffa8
-  __TEXT.__cstring: 0x12cd4
+1353.0.0.0.0
+  __TEXT.__text: 0x1e342c
+  __TEXT.__objc_methlist: 0x20098
+  __TEXT.__cstring: 0x12d24
   __TEXT.__const: 0x300
-  __TEXT.__gcc_except_tab: 0x3808
-  __TEXT.__oslogstring: 0x22879
+  __TEXT.__gcc_except_tab: 0x3820
+  __TEXT.__oslogstring: 0x22b0f
   __TEXT.__dlopen_cstrs: 0x1ba
   __TEXT.__ustring: 0x168
   __TEXT.__constg_swiftt: 0x28

   __TEXT.__swift5_reflstr: 0x17
   __TEXT.__swift5_fieldmd: 0x28
   __TEXT.__swift5_types: 0x4
-  __TEXT.__unwind_info: 0x8b48
+  __TEXT.__unwind_info: 0x8b78
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x4020
-  __DATA_CONST.__objc_classlist: 0xf78
+  __DATA_CONST.__objc_classlist: 0xf88
   __DATA_CONST.__objc_catlist: 0xf8
   __DATA_CONST.__objc_protolist: 0x168
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x8f00
+  __DATA_CONST.__objc_selrefs: 0x8f78
   __DATA_CONST.__objc_protorefs: 0x50
-  __DATA_CONST.__objc_superrefs: 0xf20
+  __DATA_CONST.__objc_superrefs: 0xf28
   __DATA_CONST.__objc_arraydata: 0x28
   __DATA_CONST.__got: 0x1620
   __AUTH_CONST.__const: 0x720
   __AUTH_CONST.__cfstring: 0xaa00
-  __AUTH_CONST.__objc_const: 0x36f20
+  __AUTH_CONST.__objc_const: 0x37168
   __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH_CONST.__objc_intobj: 0xa8
   __AUTH_CONST.__objc_doubleobj: 0x70
   __AUTH_CONST.__auth_got: 0x0
-  __AUTH.__objc_data: 0x8d90
-  __DATA.__objc_ivar: 0x16b8
+  __AUTH.__objc_data: 0x8e30
+  __DATA.__objc_ivar: 0x16d0
   __DATA.__data: 0x1120
   __DATA_DIRTY.__objc_data: 0xd20
   __DATA_DIRTY.__bss: 0xa8

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 11919
-  Symbols:   21460
-  CStrings:  3754
+  Functions: 11947
+  Symbols:   21517
+  CStrings:  3762
 
Symbols:
+ +[NPKPassLibrarySyncState _shouldAddPass:withDeviceIsTinker:supportHealthPass:stateVersion:hasValidSignature:]
+ -[NPKPassLibrarySyncState initWithPasses:device:signatureValidationCache:]
+ -[NPKPassSignatureValidationCache .cxx_destruct]
+ -[NPKPassSignatureValidationCache hasValidSignatureForPass:manifestHash:]
+ -[NPKPassSignatureValidationCache init]
+ -[NPKPassSignatureValidationCache invalidatePassWithUniqueID:]
+ -[NPKPassSignatureValidationCacheEntry .cxx_destruct]
+ -[NPKPassSignatureValidationCacheEntry contentToken]
+ -[NPKPassSignatureValidationCacheEntry hasValidSignature]
+ -[NPKPassSignatureValidationCacheEntry setContentToken:]
+ -[NPKPassSignatureValidationCacheEntry setHasValidSignature:]
+ -[NPKPassSyncService initWithPassSyncEngineRole:pairedDevice:]
+ -[NPKPassSyncService pairedDevice]
+ -[NPKPassSyncService passSyncEngineArchivePath]
+ -[NPKPassSyncService setPassSyncEngineArchivePath:]
+ -[NPKPassSyncStateItem isValidForSync]
+ -[NPKPassSyncStateItem syncValidationDescription]
+ GCC_except_table163
+ GCC_except_table164
+ GCC_except_table166
+ GCC_except_table167
+ GCC_except_table207
+ GCC_except_table234
+ GCC_except_table84
+ _NPKHomeDirectorySubpath
+ _NPKHomeDirectorySubpathForDevice
+ _NPKPassHasValidSignatureForStandaloneSync
+ _NPKPassNeedsSignatureValidationForStandaloneSync
+ _NPKPassSyncEngineArchivePathForDevice
+ _NPKPaymentWebServiceBackgroundContextPathForDevice
+ _NPKPeerPaymentAccountPathForDevice
+ _NPKPeerPaymentWebServiceContextPathForDevice
+ _NPKShouldUseStandaloneSyncForPassWithDeviceAndSignatureValidity
+ _NPKStorePathForPaymentPassWithUniqueIDForDevice
+ _NPKStorePathForPaymentPassWithUniqueIDInDirectory
+ _NPKValidatePassSignatureForStandaloneSync
+ _OBJC_CLASS_$_NPKPassSignatureValidationCache
+ _OBJC_CLASS_$_NPKPassSignatureValidationCacheEntry
+ _OBJC_IVAR_$_NPKPassSignatureValidationCache._entriesByUniqueID
+ _OBJC_IVAR_$_NPKPassSignatureValidationCache._lock
+ _OBJC_IVAR_$_NPKPassSignatureValidationCacheEntry._contentToken
+ _OBJC_IVAR_$_NPKPassSignatureValidationCacheEntry._hasValidSignature
+ _OBJC_IVAR_$_NPKPassSyncService._pairedDevice
+ _OBJC_IVAR_$_NPKPassSyncService._passSyncEngineArchivePath
+ _OBJC_METACLASS_$_NPKPassSignatureValidationCache
+ _OBJC_METACLASS_$_NPKPassSignatureValidationCacheEntry
+ __OBJC_$_INSTANCE_METHODS_NPKPassSignatureValidationCache
+ __OBJC_$_INSTANCE_METHODS_NPKPassSignatureValidationCacheEntry
+ __OBJC_$_INSTANCE_VARIABLES_NPKPassSignatureValidationCache
+ __OBJC_$_INSTANCE_VARIABLES_NPKPassSignatureValidationCacheEntry
+ __OBJC_$_PROP_LIST_NPKPassSignatureValidationCacheEntry
+ __OBJC_CLASS_RO_$_NPKPassSignatureValidationCache
+ __OBJC_CLASS_RO_$_NPKPassSignatureValidationCacheEntry
+ __OBJC_METACLASS_RO_$_NPKPassSignatureValidationCache
+ __OBJC_METACLASS_RO_$_NPKPassSignatureValidationCacheEntry
+ ___34-[NPKPassSyncState initWithCoder:]_block_invoke
+ ___62-[NPKPassSyncService initWithPassSyncEngineRole:pairedDevice:]_block_invoke
+ ___74-[NPKPassLibrarySyncState initWithPasses:device:signatureValidationCache:]_block_invoke
+ ___74-[NPKPassLibrarySyncState initWithPasses:device:signatureValidationCache:]_block_invoke_2
+ ___74-[NPKPassLibrarySyncState initWithPasses:device:signatureValidationCache:]_block_invoke_3
+ ___block_descriptor_66_e8_32s40s48s56s_e20_v24?0"PKPass"8^B16ls32l8s40l8s48l8s56l8
+ ___block_descriptor_80_e8_32s40s48s56s64s72bs_e47_v24?0"NPKIDVRemoteDeviceSession"8"NSError"16ls32l8s72l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_90_e8_32s40s48s56s64s72r80r_e25_v32?0"NSNumber"8Q16^B24ls32l8r72l8s40l8r80l8s48l8s56l8s64l8
+ _objc_msgSend$_shouldAddPass:withDeviceIsTinker:supportHealthPass:stateVersion:hasValidSignature:
+ _objc_msgSend$contentToken
+ _objc_msgSend$hasValidSignature
+ _objc_msgSend$hasValidSignatureForPass:manifestHash:
+ _objc_msgSend$initWithPassSyncEngineRole:pairedDevice:
+ _objc_msgSend$initWithPasses:device:signatureValidationCache:
+ _objc_msgSend$isValidForSync
+ _objc_msgSend$passSyncEngineArchivePath
+ _objc_msgSend$setContentToken:
+ _objc_msgSend$setHasValidSignature:
+ _objc_msgSend$syncValidationDescription
- +[NPKPassLibrarySyncState _shouldAddPass:withDeviceIsTinker:supportHealthPass:stateVersion:]
- GCC_except_table157
- GCC_except_table158
- GCC_except_table159
- GCC_except_table160
- GCC_except_table195
- GCC_except_table225
- GCC_except_table227
- _NPKRasterizedPassCachePath
- ___49-[NPKPassLibrarySyncState initWithPasses:device:]_block_invoke
- ___49-[NPKPassLibrarySyncState initWithPasses:device:]_block_invoke_2
- ___49-[NPKPassLibrarySyncState initWithPasses:device:]_block_invoke_3
- ___49-[NPKPassSyncService initWithPassSyncEngineRole:]_block_invoke
- ___block_descriptor_58_e8_32s40s48s_e20_v24?0"PKPass"8^B16ls32l8s40l8s48l8
- ___block_descriptor_66_e8_32s40s48s56s_e25_v32?0"NSNumber"8Q16^B24ls32l8s40l8s48l8s56l8
- ___block_descriptor_72_e8_32s40s48s56s64bs_e47_v24?0"NPKIDVRemoteDeviceSession"8"NSError"16ls32l8s40l8s48l8s56l8s64l8
- _objc_msgSend$_shouldAddPass:withDeviceIsTinker:supportHealthPass:stateVersion:
CStrings:
+ "Error: %s failed to obtain a session for the target device with identifier %@, error:%@"
+ "Error: Dropping archived sync state item with incomplete fields (%@)"
+ "Error: Not adding or updating sync state item with incomplete fields (%@)"
+ "Error: Skipping pass with incomplete sync fields (%@)"
+ "Error: Skipping proto conversion for sync state item with nil required field (%@)"
+ "NPKPassNeedsSignatureValidationForStandaloneSync"
+ "NPKShouldUseStandaloneSyncForPassWithDeviceAndSignatureValidity"
+ "Notice: No store path for pass with unique ID %@ (no active paired device); skipping data accessor setup."
+ "Notice: No store path for pass: %@ (no active paired device); skipping data accessor update."
+ "Notice: Not opening pass database: no home directory (no current paired device)"
+ "Notice: Updated home directory: %{private}@ for pairing ID: %{private}@"
+ "passTypeIdentifier: %@, serialNumber: %@, manifestHash: %@"
- "IdentityStreamlinedPresentment"
- "NPKShouldUseStandaloneSyncForPassWithDevice"
- "Notice: Updated Home directory:%@ for deviceParingID:%@"
- "RasterizedPasses"
```
