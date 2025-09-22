## MobileAsset

> `/System/Library/PrivateFrameworks/MobileAsset.framework/MobileAsset`

```diff

-936.80.3.0.0
-  __TEXT.__text: 0x6cb4c
-  __TEXT.__auth_stubs: 0x8e0
-  __TEXT.__objc_methlist: 0x54a0
-  __TEXT.__const: 0x1b8
-  __TEXT.__gcc_except_tab: 0x76c
-  __TEXT.__cstring: 0x12a07
-  __TEXT.__oslogstring: 0x4132
-  __TEXT.__unwind_info: 0x1764
-  __TEXT.__objc_classname: 0x5f1
-  __TEXT.__objc_methname: 0x1032f
-  __TEXT.__objc_methtype: 0x10a3
-  __TEXT.__objc_stubs: 0x6ca0
+1022.102.3.0.0
+  __TEXT.__text: 0x71348
+  __TEXT.__auth_stubs: 0x920
+  __TEXT.__objc_methlist: 0x5658
+  __TEXT.__const: 0x1c8
+  __TEXT.__gcc_except_tab: 0x778
+  __TEXT.__cstring: 0x1347a
+  __TEXT.__oslogstring: 0x512a
+  __TEXT.__unwind_info: 0x1814
+  __TEXT.__objc_classname: 0x62e
+  __TEXT.__objc_methname: 0x10bf7
+  __TEXT.__objc_methtype: 0x1155
+  __TEXT.__objc_stubs: 0x7060
   __DATA_CONST.__got: 0x90
-  __DATA_CONST.__const: 0x1c00
-  __DATA_CONST.__objc_classlist: 0x1e8
+  __DATA_CONST.__const: 0x1c80
+  __DATA_CONST.__objc_classlist: 0x1f8
   __DATA_CONST.__objc_catlist: 0x0
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x6bc0
-  __DATA_CONST.__objc_selrefs: 0x2840
-  __DATA_CONST.__objc_arraydata: 0x250
-  __AUTH_CONST.__cfstring: 0xd640
-  __AUTH_CONST.__const: 0x5e0
-  __AUTH_CONST.__objc_const: 0x2010
+  __DATA_CONST.__objc_const: 0x6db0
+  __DATA_CONST.__objc_selrefs: 0x2958
+  __DATA_CONST.__objc_protorefs: 0x10
+  __DATA_CONST.__objc_classrefs: 0x2f0
+  __DATA_CONST.__objc_superrefs: 0x1d8
+  __DATA_CONST.__objc_arraydata: 0x240
+  __AUTH_CONST.__cfstring: 0xdd60
+  __AUTH_CONST.__const: 0x640
+  __AUTH_CONST.__objc_const: 0x20a0
   __AUTH_CONST.__objc_arrayobj: 0x90
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_intobj: 0x18
-  __AUTH_CONST.__auth_got: 0x480
-  __AUTH.__objc_data: 0x870
-  __DATA.__objc_protorefs: 0x10
-  __DATA.__objc_classrefs: 0x2d8
-  __DATA.__objc_superrefs: 0x1d0
-  __DATA.__objc_ivar: 0x754
-  __DATA.__data: 0x420
-  __DATA.__bss: 0x123
-  __DATA_DIRTY.__objc_data: 0xaa0
-  __DATA_DIRTY.__bss: 0x90
+  __AUTH_CONST.__auth_got: 0x4a0
+  __AUTH.__objc_data: 0x8c0
+  __DATA.__objc_ivar: 0x770
+  __DATA.__data: 0x3c8
+  __DATA.__bss: 0xd8
+  __DATA_DIRTY.__objc_data: 0xaf0
+  __DATA_DIRTY.__data: 0x8
+  __DATA_DIRTY.__bss: 0x160
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/AppSupport.framework/AppSupport

   - /System/Library/PrivateFrameworks/StreamingZip.framework/StreamingZip
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: E2C3EE84-75E6-345D-9AB9-0EE68678BD7C
-  Functions: 2595
-  Symbols:   7596
-  CStrings:  6155
+  UUID: F5356497-F3C6-3154-9A2C-9F28969939D6
+  Functions: 2665
+  Symbols:   7798
+  CStrings:  6355
 
Symbols:
+ +[MAAutoAsset logMAAutoAssetVersion]
+ +[MAAutoAssetAuthorizationPolicy _existingSandboxExtensions]
+ +[MAAutoAssetAuthorizationPolicy consumeSandboxExtension:forPath:]
+ +[MAAutoAssetAuthorizationPolicy consumeSandboxExtension:forPath:].cold.1
+ +[MAAutoAssetAuthorizationPolicy consumeSandboxExtension:forPath:].cold.2
+ +[MAAutoAssetSet eliminateAtomic:usingClientDomain:forAssetSetIdentifier:awaitingUnlocked:completion:]
+ +[MAAutoAssetSet eliminateAtomic:usingClientDomain:forAssetSetIdentifier:awaitingUnlocked:completion:].cold.1
+ +[MAAutoAssetSet eliminateAtomicSync:usingClientDomain:forAssetSetIdentifier:awaitingUnlocked:]
+ +[MAAutoAssetSetStatus _shortTermLockFilenameNormalizedComponent:]
+ +[MAAutoAssetSetStatus shortTermLockFilename:forAssetSetIdentifier:forSetAtomicInstance:]
+ -[MAAutoAsset _successLockContent:dueToDesire:sandboxExtension:sandboxExtensionPath:completion:]
+ -[MAAutoAssetSet _closeAndRemoveShortTermLock:forShortTermLock:]
+ -[MAAutoAssetSet _closeAndRemoveShortTermLock:forShortTermLock:].cold.1
+ -[MAAutoAssetSet _closeAndRemoveShortTermLock:forShortTermLock:].cold.2
+ -[MAAutoAssetSet _closeAndRemoveShortTermLock:forShortTermLock:].cold.3
+ -[MAAutoAssetSet _eliminateAtomic:awaitingUnlocked:completion:]
+ -[MAAutoAssetSet _eliminateAtomic:awaitingUnlocked:completion:].cold.1
+ -[MAAutoAssetSet _eliminateAtomicSync:awaitingUnlocked:]
+ -[MAAutoAssetSet _readLockedSetStatusFromSharedLockFile:error:]
+ -[MAAutoAssetSet _shortTermCurrentSetStatus:]
+ -[MAAutoAssetSet _shortTermCurrentSetStatusSync:]
+ -[MAAutoAssetSet _shortTermEndAtomicLock:ofAtomicInstance:completion:]
+ -[MAAutoAssetSet _shortTermEndAtomicLockSync:ofAtomicInstance:]
+ -[MAAutoAssetSet _shortTermLockAtomic:forAtomicInstance:completion:]
+ -[MAAutoAssetSet _shortTermLockAtomicSync:forAtomicInstance:error:]
+ -[MAAutoAssetSet _shortTermLockForAtomicInstance:locking:withLockedFileDescriptor:forLockReason:justCreated:error:]
+ -[MAAutoAssetSet _shortTermLockForAtomicInstance:locking:withLockedFileDescriptor:forLockReason:justCreated:error:].cold.1
+ -[MAAutoAssetSet _shortTermLockForAtomicInstance:locking:withLockedFileDescriptor:forLockReason:justCreated:error:].cold.2
+ -[MAAutoAssetSet _shortTermLogResult:forLockReason:forAtomicInstance:atomicInstanceFilename:forShortTermLock:withSetStatus:returningError:]
+ -[MAAutoAssetSet _successLockAtomic:forAssetSetIdentifier:lockedAtomicInstance:lockedAtomicEntries:sandboxExtension:sandboxExtensionPath:completion:]
+ -[MAAutoAssetSet _successLockAtomic:forAssetSetIdentifier:lockedAtomicInstance:lockedAtomicEntries:sandboxExtension:sandboxExtensionPath:completion:].cold.1
+ -[MAAutoAssetSet initLockerUsingClientDomain:forAssetSetIdentifier:error:]
+ -[MAAutoAssetSet initLockerUsingClientDomain:forAssetSetIdentifier:usingDesiredPolicyCategory:completingFromQueue:error:]
+ -[MAAutoAssetSet initUsingClientDomain:forClientName:forAssetSetIdentifier:asShortTermLocker:comprisedOfEntries:usingDesiredPolicyCategory:completingFromQueue:error:]
+ -[MAAutoAssetSet lockAtomic:forAtomicInstance:completion:]
+ -[MAAutoAssetSet lockAtomic:forAtomicInstance:completion:].cold.1
+ -[MAAutoAssetSet lockAtomicSync:forAtomicInstance:error:]
+ -[MAAutoAssetSet shortTermLocker]
+ -[MAAutoAssetSetPolicy setSupportingShortTermLocks:]
+ -[MAAutoAssetSetPolicy supportingShortTermLocks]
+ -[MAAutoAssetSetShortTermLock .cxx_destruct]
+ -[MAAutoAssetSetShortTermLock assetSetAtomicInstance]
+ -[MAAutoAssetSetShortTermLock description]
+ -[MAAutoAssetSetShortTermLock initForAssetSetAtomicInstance:withLockedFilename:withLockedFileDescriptor:forFirstLockReason:]
+ -[MAAutoAssetSetShortTermLock lockCountByReason]
+ -[MAAutoAssetSetShortTermLock lockedFileDescriptor]
+ -[MAAutoAssetSetShortTermLock lockedFilename]
+ -[MAAutoAssetSetShortTermLock setLockCountByReason:]
+ -[MAAutoAssetSetShortTermLock setLockedFileDescriptor:]
+ -[MAAutoAssetSetShortTermLock setTotalLockCount:]
+ -[MAAutoAssetSetShortTermLock summary]
+ -[MAAutoAssetSetShortTermLock totalLockCount]
+ GCC_except_table127
+ GCC_except_table140
+ GCC_except_table144
+ GCC_except_table146
+ GCC_except_table46
+ GCC_except_table58
+ GCC_except_table63
+ GCC_except_table67
+ GCC_except_table84
+ GCC_except_table91
+ GCC_except_table98
+ _MAGetPallasUrl
+ _MAGetPallasUrlForType
+ _OBJC_CLASS_$_MAAutoAssetAuthorizationPolicy
+ _OBJC_CLASS_$_MAAutoAssetSetShortTermLock
+ _OBJC_CLASS_$_SUCorePersistedState
+ _OBJC_IVAR_$_MAAutoAssetSet._shortTermLocker
+ _OBJC_IVAR_$_MAAutoAssetSetPolicy._supportingShortTermLocks
+ _OBJC_IVAR_$_MAAutoAssetSetShortTermLock._assetSetAtomicInstance
+ _OBJC_IVAR_$_MAAutoAssetSetShortTermLock._lockCountByReason
+ _OBJC_IVAR_$_MAAutoAssetSetShortTermLock._lockedFileDescriptor
+ _OBJC_IVAR_$_MAAutoAssetSetShortTermLock._lockedFilename
+ _OBJC_IVAR_$_MAAutoAssetSetShortTermLock._totalLockCount
+ _OBJC_METACLASS_$_MAAutoAssetAuthorizationPolicy
+ _OBJC_METACLASS_$_MAAutoAssetSetShortTermLock
+ _OUTLINED_FUNCTION_11
+ _OUTLINED_FUNCTION_12
+ _OUTLINED_FUNCTION_13
+ _OUTLINED_FUNCTION_14
+ _OUTLINED_FUNCTION_15
+ _OUTLINED_FUNCTION_16
+ __MAsendGetPallasUrl
+ __MAsendGetPallasUrlForType
+ __OBJC_$_CLASS_METHODS_MAAutoAssetAuthorizationPolicy
+ __OBJC_$_INSTANCE_METHODS_MAAutoAssetSetShortTermLock
+ __OBJC_$_INSTANCE_VARIABLES_MAAutoAssetSetShortTermLock
+ __OBJC_$_PROP_LIST_MAAutoAssetSetShortTermLock
+ __OBJC_CLASS_RO_$_MAAutoAssetAuthorizationPolicy
+ __OBJC_CLASS_RO_$_MAAutoAssetSetShortTermLock
+ __OBJC_METACLASS_RO_$_MAAutoAssetAuthorizationPolicy
+ __OBJC_METACLASS_RO_$_MAAutoAssetSetShortTermLock
+ ___102+[MAAutoAssetSet eliminateAtomic:usingClientDomain:forAssetSetIdentifier:awaitingUnlocked:completion:]_block_invoke
+ ___102+[MAAutoAssetSet eliminateAtomic:usingClientDomain:forAssetSetIdentifier:awaitingUnlocked:completion:]_block_invoke_2
+ ___149-[MAAutoAssetSet _successLockAtomic:forAssetSetIdentifier:lockedAtomicInstance:lockedAtomicEntries:sandboxExtension:sandboxExtensionPath:completion:]_block_invoke
+ ___166-[MAAutoAssetSet initUsingClientDomain:forClientName:forAssetSetIdentifier:asShortTermLocker:comprisedOfEntries:usingDesiredPolicyCategory:completingFromQueue:error:]_block_invoke
+ ___33-[MAAutoAsset _successEliminate:]_block_invoke.596
+ ___36+[MAAutoAsset logMAAutoAssetVersion]_block_invoke
+ ___38-[MAAutoAsset _successCancelActivity:]_block_invoke.589
+ ___45-[MAAutoAssetSet _shortTermCurrentSetStatus:]_block_invoke
+ ___47-[MAAutoAsset _successEndLockUsage:completion:]_block_invoke.585
+ ___49-[MAAutoAssetSet _shortTermCurrentSetStatusSync:]_block_invoke
+ ___49-[MAAutoAssetSet _shortTermCurrentSetStatusSync:]_block_invoke.cold.1
+ ___56-[MAAutoAssetSet _eliminateAtomicSync:awaitingUnlocked:]_block_invoke
+ ___56-[MAAutoAssetSet _eliminateAtomicSync:awaitingUnlocked:]_block_invoke_2
+ ___56-[MAAutoAssetSet _eliminateAtomicSync:awaitingUnlocked:]_block_invoke_3
+ ___58-[MAAutoAssetSet lockAtomic:forAtomicInstance:completion:]_block_invoke
+ ___60+[MAAutoAssetAuthorizationPolicy _existingSandboxExtensions]_block_invoke
+ ___60-[MAAutoAssetSet endAtomicLock:ofAtomicInstance:completion:]_block_invoke_3
+ ___63-[MAAutoAssetSet _eliminateAtomic:awaitingUnlocked:completion:]_block_invoke
+ ___63-[MAAutoAssetSet _eliminateAtomic:awaitingUnlocked:completion:]_block_invoke_2
+ ___63-[MAAutoAssetSet _shortTermEndAtomicLockSync:ofAtomicInstance:]_block_invoke
+ ___63-[MAAutoAssetSet _shortTermEndAtomicLockSync:ofAtomicInstance:]_block_invoke.cold.1
+ ___63-[MAAutoAssetSet _shortTermEndAtomicLockSync:ofAtomicInstance:]_block_invoke.cold.2
+ ___63-[MAAutoAssetSet _shortTermEndAtomicLockSync:ofAtomicInstance:]_block_invoke.cold.3
+ ___63-[MAAutoAssetSet _shortTermEndAtomicLockSync:ofAtomicInstance:]_block_invoke.cold.4
+ ___67-[MAAutoAssetSet _shortTermLockAtomicSync:forAtomicInstance:error:]_block_invoke
+ ___68-[MAAutoAssetSet _shortTermLockAtomic:forAtomicInstance:completion:]_block_invoke
+ ___70-[MAAutoAssetSet _shortTermEndAtomicLock:ofAtomicInstance:completion:]_block_invoke
+ ___96-[MAAutoAsset _successLockContent:dueToDesire:sandboxExtension:sandboxExtensionPath:completion:]_block_invoke
+ ___96-[MAAutoAsset _successLockContent:dueToDesire:sandboxExtension:sandboxExtensionPath:completion:]_block_invoke.578
+ ___96-[MAAutoAsset _successLockContent:dueToDesire:sandboxExtension:sandboxExtensionPath:completion:]_block_invoke.cold.1
+ ___Block_byref_object_copy_.555
+ ___Block_byref_object_copy_.642
+ ___Block_byref_object_copy_.960
+ ___Block_byref_object_dispose_.556
+ ___Block_byref_object_dispose_.643
+ ___Block_byref_object_dispose_.961
+ ___block_descriptor_56_e8_32s40r48r_e5_v8?0ls32l8r40l8r48l8
+ ___block_descriptor_64_e8_32s40s48s56r_e5_v8?0ls32l8s40l8s48l8r56l8
+ ___block_descriptor_72_e8_32s40s48s56r64r_e5_v8?0ls32l8s40l8r56l8r64l8s48l8
+ ___block_descriptor_80_e8_32s40s48s56s64s72bs_e5_v8?0ls32l8s40l8s48l8s72l8s56l8s64l8
+ ___block_literal_global.1079
+ ___block_literal_global.2274
+ ___block_literal_global.2276
+ ___block_literal_global.2278
+ ___block_literal_global.2280
+ ___block_literal_global.233
+ ___block_literal_global.236
+ ___block_literal_global.239
+ ___block_literal_global.400
+ ___block_literal_global.447
+ ___block_literal_global.453
+ ___block_literal_global.455
+ ___block_literal_global.633
+ ___block_literal_global.639
+ ___block_literal_global.641
+ ___block_literal_global.658
+ ___block_literal_global.660
+ ___block_literal_global.666
+ ___block_literal_global.668
+ ___block_literal_global.669
+ ___block_literal_global.670
+ ___block_literal_global.710
+ ___block_literal_global.720
+ ___block_literal_global.725
+ ___block_literal_global.813
+ ___block_literal_global.815
+ ___block_literal_global.818
+ ___block_literal_global.838
+ ___error
+ ___maAutoAssetLogVersionDispatchOnce
+ ___maAutoAssetSetSharedProcessByClientDomainName
+ ___maAutoAssetSetShortTermLockerDispatchQueue
+ ___maAutoAssetSetShortTermLockerOnce
+ __existingSandboxExtensions.activeExtensions
+ __existingSandboxExtensions.existingSandboxExtensionsOnceToken
+ __unnamed_array_storage.746
+ __unnamed_array_storage.747
+ __unnamed_array_storage.763
+ __unnamed_array_storage.966
+ __unnamed_array_storage.974
+ __unnamed_array_storage.989
+ _close
+ _objc_msgSend$_closeAndRemoveShortTermLock:forShortTermLock:
+ _objc_msgSend$_eliminateAtomic:awaitingUnlocked:completion:
+ _objc_msgSend$_eliminateAtomicSync:awaitingUnlocked:
+ _objc_msgSend$_existingSandboxExtensions
+ _objc_msgSend$_readLockedSetStatusFromSharedLockFile:error:
+ _objc_msgSend$_shortTermCurrentSetStatus:
+ _objc_msgSend$_shortTermCurrentSetStatusSync:
+ _objc_msgSend$_shortTermEndAtomicLockSync:ofAtomicInstance:
+ _objc_msgSend$_shortTermLockAtomic:forAtomicInstance:completion:
+ _objc_msgSend$_shortTermLockAtomicSync:forAtomicInstance:error:
+ _objc_msgSend$_shortTermLockFilenameNormalizedComponent:
+ _objc_msgSend$_shortTermLockForAtomicInstance:locking:withLockedFileDescriptor:forLockReason:justCreated:error:
+ _objc_msgSend$_shortTermLogResult:forLockReason:forAtomicInstance:atomicInstanceFilename:forShortTermLock:withSetStatus:returningError:
+ _objc_msgSend$_successLockAtomic:forAssetSetIdentifier:lockedAtomicInstance:lockedAtomicEntries:sandboxExtension:sandboxExtensionPath:completion:
+ _objc_msgSend$_successLockContent:dueToDesire:sandboxExtension:sandboxExtensionPath:completion:
+ _objc_msgSend$assetSetAtomicInstance
+ _objc_msgSend$checkedDescription
+ _objc_msgSend$consumeSandboxExtension:forPath:
+ _objc_msgSend$eliminateAtomic:usingClientDomain:forAssetSetIdentifier:awaitingUnlocked:completion:
+ _objc_msgSend$eliminateAtomicSync:usingClientDomain:forAssetSetIdentifier:awaitingUnlocked:
+ _objc_msgSend$initForAssetSetAtomicInstance:withLockedFilename:withLockedFileDescriptor:forFirstLockReason:
+ _objc_msgSend$initUsingClientDomain:forClientName:forAssetSetIdentifier:asShortTermLocker:comprisedOfEntries:usingDesiredPolicyCategory:completingFromQueue:error:
+ _objc_msgSend$initWithDispatchQueue:withPersistencePath:forPolicyVersion:
+ _objc_msgSend$initWithDispatchQueue:withPersistencePath:forPolicyVersion:issuingDefaultLevelLogging:
+ _objc_msgSend$initWithInteger:
+ _objc_msgSend$loadPersistedState
+ _objc_msgSend$lockCountByReason
+ _objc_msgSend$lockedFileDescriptor
+ _objc_msgSend$lockedFilename
+ _objc_msgSend$logMAAutoAssetVersion
+ _objc_msgSend$secureCodedObjectForKey:ofClass:
+ _objc_msgSend$setLockCountByReason:
+ _objc_msgSend$setLockedFileDescriptor:
+ _objc_msgSend$shortTermLockFilename:forAssetSetIdentifier:forSetAtomicInstance:
+ _objc_msgSend$shortTermLocker
+ _objc_msgSend$supportingShortTermLocks
+ _open
+ _strerror
- +[MAAutoAssetSet eliminateAtomic:usingClientDomain:forAssetSetIdentifier:completion:].cold.1
- -[MAAutoAsset _successLockContent:dueToDesire:completion:]
- -[MAAutoAssetLockReason initFromClientLockReasonKey:]
- -[MAAutoAssetSet _eliminateAtomic:completion:]
- -[MAAutoAssetSet _eliminateAtomic:completion:].cold.1
- -[MAAutoAssetSet _eliminateAtomicSync:]
- -[MAAutoAssetSet _successLockAtomic:forAssetSetIdentifier:lockedAtomicInstance:lockedAtomicEntries:completion:]
- -[MAAutoAssetSet _successLockAtomic:forAssetSetIdentifier:lockedAtomicInstance:lockedAtomicEntries:completion:].cold.1
- GCC_except_table103
- GCC_except_table114
- GCC_except_table118
- GCC_except_table120
- GCC_except_table53
- GCC_except_table56
- GCC_except_table60
- GCC_except_table61
- GCC_except_table69
- GCC_except_table83
- GCC_except_table90
- ___111-[MAAutoAssetSet _successLockAtomic:forAssetSetIdentifier:lockedAtomicInstance:lockedAtomicEntries:completion:]_block_invoke
- ___33-[MAAutoAsset _successEliminate:]_block_invoke.568
- ___38-[MAAutoAsset _successCancelActivity:]_block_invoke.561
- ___39-[MAAutoAssetSet _eliminateAtomicSync:]_block_invoke
- ___39-[MAAutoAssetSet _eliminateAtomicSync:]_block_invoke_2
- ___39-[MAAutoAssetSet _eliminateAtomicSync:]_block_invoke_3
- ___46-[MAAutoAssetSet _eliminateAtomic:completion:]_block_invoke
- ___46-[MAAutoAssetSet _eliminateAtomic:completion:]_block_invoke_2
- ___47-[MAAutoAsset _successEndLockUsage:completion:]_block_invoke.557
- ___58-[MAAutoAsset _successLockContent:dueToDesire:completion:]_block_invoke
- ___58-[MAAutoAsset _successLockContent:dueToDesire:completion:]_block_invoke.550
- ___58-[MAAutoAsset _successLockContent:dueToDesire:completion:]_block_invoke.cold.1
- ___85+[MAAutoAssetSet eliminateAtomic:usingClientDomain:forAssetSetIdentifier:completion:]_block_invoke
- ___85+[MAAutoAssetSet eliminateAtomic:usingClientDomain:forAssetSetIdentifier:completion:]_block_invoke_2
- ___Block_byref_object_copy_.494
- ___Block_byref_object_copy_.528
- ___Block_byref_object_copy_.933
- ___Block_byref_object_dispose_.495
- ___Block_byref_object_dispose_.529
- ___Block_byref_object_dispose_.934
- ___block_descriptor_64_e8_32s40s48s56bs_e5_v8?0ls32l8s40l8s48l8s56l8
- ___block_literal_global.1052
- ___block_literal_global.209
- ___block_literal_global.212
- ___block_literal_global.215
- ___block_literal_global.2250
- ___block_literal_global.2252
- ___block_literal_global.2254
- ___block_literal_global.2256
- ___block_literal_global.376
- ___block_literal_global.423
- ___block_literal_global.429
- ___block_literal_global.431
- ___block_literal_global.515
- ___block_literal_global.517
- ___block_literal_global.519
- ___block_literal_global.609
- ___block_literal_global.615
- ___block_literal_global.617
- ___block_literal_global.634
- ___block_literal_global.645
- ___block_literal_global.683
- ___block_literal_global.686
- ___block_literal_global.689
- ___block_literal_global.699
- ___block_literal_global.783
- ___block_literal_global.785
- ___block_literal_global.787
- __unnamed_array_storage.725
- __unnamed_array_storage.726
- __unnamed_array_storage.742
- __unnamed_array_storage.945
- __unnamed_array_storage.953
- __unnamed_array_storage.968
- _objc_msgSend$_eliminateAtomic:completion:
- _objc_msgSend$_eliminateAtomicSync:
- _objc_msgSend$_successLockAtomic:forAssetSetIdentifier:lockedAtomicInstance:lockedAtomicEntries:completion:
- _objc_msgSend$_successLockContent:dueToDesire:completion:
- _objc_msgSend$rangeOfString:
- _objc_msgSend$substringWithRange:
CStrings:
+ "\x16"
+ "%@/%@/%@/%@/%@_%@.%@"
+ "(NO_TARGETS_DEFINED)"
+ "/private/var/MobileAsset/AssetsV2/locks"
+ "1.0"
+ "2.1.2"
+ ":;,/\\?~%*|\"<>[](){}"
+ "@44@0:8@16@24i32@36"
+ "@56@0:8@16B24i28@32^B40^@48"
+ "@76@0:8@16@24@32B40@44@52@60^@68"
+ "B32@0:8@16@24"
+ "Cannot end SHORT-TERM locks of specific reason without specifying an atomic-instance | endLockReason:%@"
+ "FailedSharedLockPreparation"
+ "InvalidForLockerMode"
+ "MA-auto(FRAMEWORK_VERSION:%{public}@) | build environment:%{public}@"
+ "MA-auto-set[AUTO-SHORT-TERM][FRAMEWORK]{%{public}@:_closeAndRemoveShortTermLock} | WARNING | failed close of shared lock file | errno:%d | shortTermLock:%{public}@"
+ "MA-auto-set[AUTO-SHORT-TERM][FRAMEWORK]{%{public}@:_closeAndRemoveShortTermLock} | WARNING | invalid lockedFileDesciptor | shortTermLock:%{public}@"
+ "MA-auto-set[AUTO-SHORT-TERM][FRAMEWORK]{%{public}@:_closeAndRemoveShortTermLock} | WARNING | unable to locate byAssetSetIdentifier when ending SHORT-TERM lock | shortTermLock:%{public}@"
+ "MA-auto-set[AUTO-SHORT-TERM][FRAMEWORK]{%{public}@:_closeAndRemoveShortTermLock} | WARNING | unable to locate byAtomicInstance when ending SHORT-TERM lock | shortTermLock:%{public}@"
+ "MA-auto-set[AUTO-SHORT-TERM][FRAMEWORK]{%{public}@:_closeAndRemoveShortTermLock} | released shared lock | shortTermLock:%{public}@"
+ "MA-auto-set[AUTO-SHORT-TERM][FRAMEWORK]{%{public}@} %{public}@ ERROR | lockReason:%{public}@ | forAtomicInstance:%{public}@ | atomicInstanceFilename:%{public}@ | setStatus:%{public}@ | error:%{public}@"
+ "MA-auto-set[AUTO-SHORT-TERM][FRAMEWORK]{%{public}@} %{public}@ ERROR | lockReason:%{public}@ | shortTermLock:%{public}@  | setStatus:%{public}@ | error:%{public}@"
+ "MA-auto-set[AUTO-SHORT-TERM][FRAMEWORK]{%{public}@} %{public}@ SUCCESS | lockReason:%{public}@ | forAtomicInstance:%{public}@ | atomicInstanceFilename:%{public}@ | setStatus:%{public}@"
+ "MA-auto-set[AUTO-SHORT-TERM][FRAMEWORK]{%{public}@} %{public}@ SUCCESS | lockReason:%{public}@ | shortTermLock:%{public}@ | setStatus:%{public}@"
+ "MA-auto-set[AUTO-SHORT-TERM][FRAMEWORK]{_shortTermCurrentSetStatusSync} | WARNING | failed close of shared lock file | latestAtomicInstanceFilename:%{public}@ | errno:%d"
+ "MA-auto-set[AUTO-SHORT-TERM][FRAMEWORK]{_shortTermEndAtomicLockSync}(%{public}@) | WARNING | inconsistent totalLockCount (ending last lock) | shortTermLock:%@"
+ "MA-auto-set[AUTO-SHORT-TERM][FRAMEWORK]{_shortTermEndAtomicLockSync}(%{public}@) | WARNING | inconsistent totalLockCount (not last lock) | shortTermLock:%@"
+ "MA-auto-set[AUTO-SHORT-TERM][FRAMEWORK]{_shortTermEndAtomicLockSync}(%{public}@) | WARNING | unable to locate byAssetSetIdentifier when ending SHORT-TERM locks for all lock reasons | shortTermLock:%@"
+ "MA-auto-set[AUTO-SHORT-TERM][FRAMEWORK]{_shortTermEndAtomicLockSync}(%{public}@) | WARNING | unable to locate byAtomicInstance when ending SHORT-TERM locks for all lock reasons | shortTermLock:%@"
+ "MA-auto-set[AUTO-SHORT-TERM][FRAMEWORK]{_shortTermLockAtomicSync}(%{public}@) | WARNING | failed close of extra lock, errno:%d | lockReason:%{public}@"
+ "MA-auto-set[AUTO-SHORT-TERM][FRAMEWORK]{_shortTermLockAtomicSync}(%{public}@) | WARNING | failed close of symlink lock, errno:%d | lockReason:%{public}@"
+ "MA-auto-set[AUTO-SHORT-TERM][FRAMEWORK]{_shortTermLockAtomicSync}(%{public}@) | additional (locally tracked usage) of shared lock | shortTermLock:%{public}@"
+ "MA-auto-set[AUTO-SHORT-TERM][FRAMEWORK]{_shortTermLockAtomicSync}(%{public}@) | holding shared lock | shortTermLock:%{public}@"
+ "MA-auto-set[AUTO-SHORT-TERM][FRAMEWORK]{_shortTermLockForAtomicInstance} | WARNING | failed close of validation lock file | atomicInstanceFilename:%{public}@ | errno:%d"
+ "MA-auto-set[AUTO-SHORT-TERM][FRAMEWORK]{_shortTermLockForAtomicInstance} | WARNING | unable to allocate MAAutoAssetSetShortTermLock (when already locked) | atomicInstanceFilename:%{public}@"
+ "MA-auto-set[AUTO-SHORT-TERM][FRAMEWORK]{_shortTermLockForAtomicInstance}(%{public}@) | holding shared lock | shortTermLock:%{public}@"
+ "MAAutoAssetAuthorizationPolicy"
+ "MAAutoAssetSetShortTermLock"
+ "MAGetPallasUrl"
+ "MA_END_ATOMIC_LOCKS_ALL_INSTANCES is specified but endLockCount is not MA_END_ATOMIC_LOCKS_COUNT_ALL"
+ "MA_END_ATOMIC_LOCKS_ALL_INSTANCES is specified but endLockReason is not nil"
+ "MA_GET_PALLAS_URL"
+ "No current SHORT-TERM lock (by assetSetIdentifier) | assetSetAtomicInstance:%@"
+ "No current SHORT-TERM lock (by atomicInstance) | assetSetAtomicInstance:%@"
+ "No current SHORT-TERM lock (by clientDomainName) | assetSetAtomicInstance:%@"
+ "No latestDownloadedAtomicInstance in locked set-status from shared lock on %@"
+ "NoSharedLock"
+ "RestrictedToLockerMode"
+ "SHORT-TERM lock is not currently locked for reason to end-lock for | shortTermLock:%@ | endLockReason:%@"
+ "SHORT-TERM lock lockCountForReason has invalid lock count | shortTermLock:%@ | endLockReason:%@ | lockCount:%d"
+ "SHORT_TERM_LOCKER"
+ "ShortTermLocked"
+ "T@\"NSMutableDictionary\",&,N,V_lockCountByReason"
+ "T@\"NSString\",?,R,C"
+ "T@\"NSString\",R,&,N,V_assetSetAtomicInstance"
+ "T@\"NSString\",R,&,N,V_lockedFilename"
+ "TB,N,V_supportingShortTermLocks"
+ "TB,R,N,V_shortTermLocker"
+ "Ti,N,V_lockedFileDescriptor"
+ "Unable to allociate SHORT-TERM lock tracking atomicInstanceFilename:%@"
+ "Unable to create persisted-state for shared lock file | sharedLockFilename:%@"
+ "Unable to load persisted-state for shared lock file | sharedLockFilename:%@"
+ "Unable to obtain shared lock (validation lock) on %@ | errno:%d"
+ "Unable to obtain shared lock on %@ | errno:%d"
+ "Unable to read auto-asset-set-status from shared lock on %@"
+ "Unable to read set-status from persisted-state for shared lock file | sharedLockFilename:%@"
+ "_MAsendGetPallasUrlForType"
+ "_assetSetAtomicInstance"
+ "_closeAndRemoveShortTermLock:forShortTermLock:"
+ "_eliminateAtomic:awaitingUnlocked:completion:"
+ "_eliminateAtomicSync:awaitingUnlocked:"
+ "_existingSandboxExtensions"
+ "_lockCountByReason"
+ "_lockedFileDescriptor"
+ "_lockedFilename"
+ "_readLockedSetStatusFromSharedLockFile:error:"
+ "_shortTermCurrentSetStatus:"
+ "_shortTermCurrentSetStatusSync"
+ "_shortTermCurrentSetStatusSync:"
+ "_shortTermEndAtomicLock:ofAtomicInstance:completion:"
+ "_shortTermEndAtomicLockSync"
+ "_shortTermEndAtomicLockSync(ending all locks of atomic-instances and lock-reasons)"
+ "_shortTermEndAtomicLockSync(ending specific atomic-instance lock)"
+ "_shortTermEndAtomicLockSync(ending specific atomic-instance locks - all lock-reasons)"
+ "_shortTermEndAtomicLockSync:ofAtomicInstance:"
+ "_shortTermLockAtomic:forAtomicInstance:completion:"
+ "_shortTermLockAtomicSync"
+ "_shortTermLockAtomicSync:forAtomicInstance:error:"
+ "_shortTermLockFilenameNormalizedComponent:"
+ "_shortTermLockForAtomicInstance:locking:withLockedFileDescriptor:forLockReason:justCreated:error:"
+ "_shortTermLocker"
+ "_shortTermLogResult:forLockReason:forAtomicInstance:atomicInstanceFilename:forShortTermLock:withSetStatus:returningError:"
+ "_successLockAtomic:forAssetSetIdentifier:lockedAtomicInstance:lockedAtomicEntries:sandboxExtension:sandboxExtensionPath:completion:"
+ "_successLockContent:dueToDesire:sandboxExtension:sandboxExtensionPath:completion:"
+ "_supportingShortTermLocks"
+ "assetSetAtomicInstance"
+ "assetSetAtomicInstance:%@|lockedFilename:%@|lockedFileDescriptor:%d|lockCountByReason:%@|totalLockCount:%ld"
+ "atomic_instance"
+ "auto-set(_readLockedSetStatusFromSharedLockFile)"
+ "auto-set(_shortTermCurrentSetStatusSync)"
+ "auto-set(_shortTermEndAtomicLockSync)"
+ "auto-set(_shortTermLockAtomicSync)"
+ "auto-set(_shortTermLockForAtomicInstance)"
+ "auto-set(lockAtomic)"
+ "autoAssetSetClientName:%@|assetSetIdentifier:%@|shortTermLocker:%@|autoAssetEntries:%@"
+ "checkedDescription"
+ "consumeSandboxExtension:forPath:"
+ "eliminateAtomic:usingClientDomain:forAssetSetIdentifier:awaitingUnlocked:completion:"
+ "eliminateAtomicSync:usingClientDomain:forAssetSetIdentifier:awaitingUnlocked:"
+ "endLockReason is nil but endLockCount is not MA_END_ATOMIC_LOCKS_COUNT_ALL"
+ "initForAssetSetAtomicInstance:withLockedFilename:withLockedFileDescriptor:forFirstLockReason:"
+ "initLockerUsingClientDomain:forAssetSetIdentifier:error:"
+ "initLockerUsingClientDomain:forAssetSetIdentifier:usingDesiredPolicyCategory:completingFromQueue:error:"
+ "initUsingClientDomain:forClientName:forAssetSetIdentifier:asShortTermLocker:comprisedOfEntries:usingDesiredPolicyCategory:completingFromQueue:error:"
+ "initWithDispatchQueue:withPersistencePath:forPolicyVersion:"
+ "initWithDispatchQueue:withPersistencePath:forPolicyVersion:issuingDefaultLevelLogging:"
+ "initWithInteger:"
+ "latest"
+ "loadPersistedState"
+ "lockAtomic:forAtomicInstance:completion:"
+ "lockAtomicSync:forAtomicInstance:error:"
+ "lockCountByReason"
+ "lockedFileDescriptor"
+ "lockedFilename"
+ "locker"
+ "logMAAutoAssetVersion"
+ "no SHORT-TERM lock tracking dictionary"
+ "no SHORT-TERM locker dispatch queue"
+ "not supported for SHORT-TERM locker instance"
+ "process.MobileAssetFramework.shortTermLocker"
+ "restricted to SHORT-TERM locker instance"
+ "sandboxExtensionPathKey"
+ "secureCodedObjectForKey:ofClass:"
+ "setLockCountByReason:"
+ "setLockedFileDescriptor:"
+ "setSupportingShortTermLocks:"
+ "sharedLockSetStatus"
+ "shared_locks"
+ "shortTermLockFilename:forAssetSetIdentifier:forSetAtomicInstance:"
+ "shortTermLocker"
+ "specific"
+ "supportingShortTermLocks"
+ "v52@0:8@16@24@32B40@?44"
+ "v72@0:8@16@24@32@40@48@56@64"
+ "v72@0:8@16@24@32@40@48@56@?64"
+ "{MAAutoAssetAuthorizationPolicy}(consumeSandboxExtensionFromMessage) consumed sandbox extension for path %{public}@"
+ "{MAAutoAssetAuthorizationPolicy}(consumeSandboxExtensionFromMessage) found existing consumed sandbox extension for path %{public}@"
+ "{MAAutoAssetAuthorizationPolicy}(consumeSandboxExtensionFromMessage) unable to consume sandbox extension as there is no extension available for path %{public}@"
+ "{MAAutoAssetAuthorizationPolicy}(consumeSandboxExtensionFromMessage) unable to consume sandbox extension with errno %s (%d) for path %{public}@"
+ "|"
+ "|TARGET_OS_IPHONE"
+ "|TARGET_OS_MAC"
+ "|lockInhibitsRemoval:%@|supportingShortTermLocks:%@|allowCheckDownload(OnBattery:%@,WhenBatteryLow:%@,WhenCPUHigh:%@,OverExpensive:%@,OverCellular:%@)|blockCheckDownload:%@|"
- "_eliminateAtomic:completion:"
- "_eliminateAtomicSync:"
- "_successLockAtomic:forAssetSetIdentifier:lockedAtomicInstance:lockedAtomicEntries:completion:"
- "_successLockContent:dueToDesire:completion:"
- "autoAssetSetClientName:%@|assetSetIdentifier:%@|autoAssetEntries:%@"
- "client:"
- "com.apple.MobileAsset.RegulatoryCertification"
- "initFromClientLockReasonKey:"
- "rangeOfString:"
- "substringWithRange:"
- "|lockInhibitsRemoval:%@|allowCheckDownload(OnBattery:%@,WhenBatteryLow:%@,WhenCPUHigh:%@,OverExpensive:%@,OverCellular:%@)|blockCheckDownload:%@"
- "|reason:"

```
