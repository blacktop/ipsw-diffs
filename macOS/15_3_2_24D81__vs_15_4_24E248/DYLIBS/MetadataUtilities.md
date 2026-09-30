## MetadataUtilities

> `/System/Library/PrivateFrameworks/MetadataUtilities.framework/Versions/A/MetadataUtilities`

```diff

-2328.7.8.7.0
-  __TEXT.__text: 0x4f020
-  __TEXT.__auth_stubs: 0x17e0
+2333.22.13.7.0
+  __TEXT.__text: 0x4fed8
+  __TEXT.__auth_stubs: 0x1850
   __TEXT.__objc_methlist: 0x45c
-  __TEXT.__const: 0x3cde
-  __TEXT.__cstring: 0x685d
-  __TEXT.__oslogstring: 0xc4e
+  __TEXT.__const: 0x3cbe
+  __TEXT.__cstring: 0x6a2a
+  __TEXT.__oslogstring: 0xc82
   __TEXT.__dlopen_cstrs: 0x54
   __TEXT.__ustring: 0x9a
-  __TEXT.__unwind_info: 0x978
+  __TEXT.__unwind_info: 0x958
   __TEXT.__objc_classname: 0xcc
-  __TEXT.__objc_methname: 0xf76
-  __TEXT.__objc_methtype: 0x64d
+  __TEXT.__objc_methname: 0xf6c
+  __TEXT.__objc_methtype: 0x63f
   __TEXT.__objc_stubs: 0x860
-  __DATA_CONST.__got: 0x130
-  __DATA_CONST.__const: 0x10c0
+  __DATA_CONST.__got: 0x138
+  __DATA_CONST.__const: 0x1180
   __DATA_CONST.__objc_classlist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x3b0
   __DATA_CONST.__objc_superrefs: 0x50
   __DATA_CONST.__objc_arraydata: 0x280
-  __AUTH_CONST.__auth_got: 0xbf8
-  __AUTH_CONST.__const: 0xd78
-  __AUTH_CONST.__cfstring: 0x45e0
-  __AUTH_CONST.__objc_const: 0x1080
+  __AUTH_CONST.__auth_got: 0xc30
+  __AUTH_CONST.__const: 0xe18
+  __AUTH_CONST.__cfstring: 0x4720
+  __AUTH_CONST.__objc_const: 0x1060
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__objc_dictobj: 0xf0
   __AUTH.__objc_data: 0x190
-  __AUTH.__data: 0x28
+  __AUTH.__data: 0x50
   __AUTH.__thread_vars: 0x18
   __AUTH.__thread_bss: 0x28
-  __DATA.__objc_ivar: 0x13c
-  __DATA.__data: 0x1d24c
-  __DATA.__bss: 0x3b8
+  __DATA.__objc_ivar: 0x138
+  __DATA.__data: 0x1d25c
+  __DATA.__bss: 0x3d8
   __DATA.__common: 0x908
   __DATA_DIRTY.__objc_data: 0x190
   __DATA_DIRTY.__data: 0x68
-  __DATA_DIRTY.__bss: 0x150
+  __DATA_DIRTY.__bss: 0x168
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/PrivateFrameworks/CoreNLP.framework/Versions/A/CoreNLP

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: E758C584-F7F6-3484-AF84-06E9DFCA1D21
-  Functions: 1146
-  Symbols:   2144
-  CStrings:  1953
+  UUID: A92F910C-359D-3CE8-92CD-CF2B8E62FF78
+  Functions: 1191
+  Symbols:   2260
+  CStrings:  1977
 
Symbols:
+ +[_MDPlistBytes emptyArrayPlistBytes].cold.1
+ +[_MDPlistBytes emptyDictionaryPlistBytes].cold.1
+ +[_MDPlistBytes enumerateObjectsFromPlistBytes:count:shouldDeallocate:usingBlock:].cold.1
+ +[_MDPlistBytes nullObjectPlistBytes].cold.1
+ -[MDPathFilter iCloudPath:updateFilter:].cold.1
+ -[SITracingObjcLifetimeSpan dealloc].cold.1
+ -[SITracingObjcLifetimeSpan init:kind:what:].cold.1
+ -[_MDPlistBytes _cfTypeID].cold.1
+ -[_MDPlistBytes initWithByteVector:count:trusted:deallocator:].cold.1
+ -[_MDPlistBytes isEqual:].cold.1
+ MDCopyBestAvailableLanguage.cold.1
+ MDExtendedAttributeBlockList.cold.1
+ MDExtendedAttributeBlockList.onceToken
+ MDExtendedAttributeBlockList.sBlockList
+ MDGetBestAvailableLanguage.cold.1
+ MDRetrieveBestAvailableLanguage.cold.1
+ SpotlightCacheAttributes.cold.1
+ SpotlightCacheDeleteEntry.cold.1
+ SpotlightCacheInsertEntry.cold.1
+ _MDBundleUtilsCopyLocalizedApplicationCategories.cold.1
+ _MDBundleUtilsCopyLocalizedDescriptionDictionary.cold.1
+ _MDBundleUtilsCopyLocalizedDescriptionDictionary.cold.2
+ _MDBundleUtilsCopyLocalizedDescriptionDictionary.cold.3
+ _MDExtendedAttributeBlockList
+ _MDIsAppleInternal.cold.1
+ _MDLogForCategoryDefault.cold.1
+ _MDPerf_IndexingLog.cold.1
+ _MDPerf_LifeCycleLog.cold.1
+ _MDPerf_QueryLog.cold.1
+ _MDPerf_SignpostLog.cold.1
+ _MDPlistBytesCopyPlistAtIndexWithCallbacksAndAllocator.cold.3
+ _MDPlistBytesCopyPlistBytesAtIndex.cold.1
+ _MDPlistBytesCopyPlistBytesAtIndex.cold.2
+ _MDPlistBytesCreate.cold.1
+ _MDPlistBytesCreateTrusted.cold.1
+ _MDPlistBytesCreateTrustedWithDeallocator.cold.1
+ _MDPlistBytesCreateWithDeallocator.cold.1
+ _MDPlistBytesGetTypeID.cold.1
+ _MDPlistContainerCreateCommon.cold.3
+ _MDPlistContainerCreateCommon.cold.4
+ _MDPlistContainerGetTypeID.cold.1
+ _MDStringCopyAbbreviations.cold.1
+ _OUTLINED_FUNCTION_7
+ _OUTLINED_FUNCTION_8
+ _PBCopyCopyObjectCustomReleaseCallback
+ _PBCopyCopyObjectCustomRetainCallback
+ __MDCopyTokensFromString.cold.1
+ __MDPlistBytesAddObject.cold.2
+ __MDQueryCreateQueryDictionaryWithOptionsDict.cold.1
+ __MDStoreOIDArrayIsMutable
+ __ZSt28__throw_bad_array_new_lengthB8nn190102v
+ ___MDBundleUtilsCopyLocalizedApplicationCategories_block_invoke.cold.1
+ ___MDBundleUtilsCopyLocalizedApplicationCategories_block_invoke.cold.2
+ ___MDExtendedAttributeBlockList_block_invoke
+ ____MDPlistBytesAddObject_block_invoke.cold.1
+ ____MDPlistBytesCopyPlistAtIndexWithCallbacksAndAllocator_block_invoke
+ ___getClientBundleIdentifier_block_invoke
+ ___isSearchToolClientBundleIdentifier_block_invoke
+ __block_descriptor_tmp.187
+ __block_descriptor_tmp.193
+ __block_descriptor_tmp.196
+ __block_descriptor_tmp.197
+ __block_descriptor_tmp.529
+ __block_descriptor_tmp.534
+ __block_descriptor_tmp.536
+ __block_descriptor_tmp.540
+ __block_descriptor_tmp.601
+ __block_descriptor_tmp.610
+ __block_descriptor_tmp.611
+ __block_descriptor_tmp.615
+ __block_descriptor_tmp.633
+ __block_descriptor_tmp.637
+ __block_descriptor_tmp.641
+ __block_descriptor_tmp.645
+ __block_descriptor_tmp.649
+ __block_descriptor_tmp.653
+ __block_descriptor_tmp.657
+ __block_descriptor_tmp.661
+ __block_descriptor_tmp.665
+ __block_descriptor_tmp.669
+ __block_descriptor_tmp.682
+ __block_descriptor_tmp.686
+ __block_descriptor_tmp.690
+ __block_literal_global.18
+ __block_literal_global.199
+ __block_literal_global.603
+ __block_literal_global.613
+ __block_literal_global.617
+ __block_literal_global.620
+ __get_proximities_block_invoke.188
+ __isSearchToolClientBundleIdentifier_block_invoke.cold.1
+ __rescheduleAutomaticCooldown_Locked_block_invoke.614
+ __rescheduleAutomaticCooldown_Locked_block_invoke.cold.1
+ _fd_acquire_fd.cold.3
+ _kCopyArrayArrayCallbacks
+ _moveWindowsInner.cold.1
+ _moveWindowsInner.cold.2
+ _pthread_cond_broadcast
+ _pthread_cond_destroy
+ _pthread_cond_init
+ _pthread_getspecific
+ _pthread_key_create
+ _pthread_mutex_destroy
+ _pthread_mutex_init
+ _pthread_setspecific
+ _qpUpdateParserOptions.cold.2
+ _si_create_queue
+ _si_dequeue_locked
+ _si_destroy_queue
+ _si_enqueue_locked
+ _si_simplequeue_count_locked
+ copyAppCategoryMap.cold.2
+ copyObject.cold.20
+ copyObject.cold.21
+ copyObject.cold.22
+ copyObject.cold.23
+ fd_create_protected.cold.1
+ fuzzy_matches.cold.1
+ fuzzy_matches.cold.2
+ fuzzy_matches.cold.3
+ fuzzy_matches.cold.4
+ fuzzy_matches.cold.5
+ fuzzy_matches.cold.6
+ getClientBundleIdentifier.identifier
+ getClientBundleIdentifier.once
+ isSearchToolClientBundleIdentifier.isSearchTool
+ isSearchToolClientBundleIdentifier.onceToken
+ preprocessStringKey.cold.1
+ rescheduleAutomaticCooldown_Locked.automaticCooldownEnabled
+ rescheduleAutomaticCooldown_Locked.automaticCooldownEnabledOnceToken
+ rescheduleAutomaticCooldown_Locked.cold.1
+ si_enqueue_locked.cold.1
+ si_enqueue_locked.cold.2
+ si_enqueue_locked.cold.3
+ si_enqueue_locked.cold.4
+ si_simplequeue_count_locked.cold.1
+ si_simplequeue_count_locked.cold.2
+ si_tracing_log_span_begin.cold.1
+ si_tracing_log_span_end.cold.1
+ si_tracing_log_span_event.cold.1
- OBJC_IVAR_$__MDPlistBytes._rleQueue
- _MDPlistBytesCopyPlistAtIndexWithCallbacksAndAllocator.lock
- __ZSt28__throw_bad_array_new_lengthB8nn180100v
- __block_descriptor_tmp.180
- __block_descriptor_tmp.182
- __block_descriptor_tmp.186
- __block_descriptor_tmp.190
- __block_descriptor_tmp.532
- __block_descriptor_tmp.537
- __block_descriptor_tmp.539
- __block_descriptor_tmp.543
- __block_descriptor_tmp.607
- __block_descriptor_tmp.608
- __block_descriptor_tmp.614
- __block_descriptor_tmp.622
- __block_descriptor_tmp.626
- __block_descriptor_tmp.630
- __block_descriptor_tmp.634
- __block_descriptor_tmp.638
- __block_descriptor_tmp.642
- __block_descriptor_tmp.646
- __block_descriptor_tmp.650
- __block_descriptor_tmp.663
- __block_descriptor_tmp.667
- __block_descriptor_tmp.671
- __block_literal_global.192
- __block_literal_global.610
- __get_proximities_block_invoke.181
- _fmod
- _icu_get_char_category_mask
- _identifier
- _utf8_encodelen
- _windowsResolvePtr.cold.1
- _windowsResolvePtr.cold.2
- _windowsResolvePtr.cold.3
- bit_vector_set.cold.2
CStrings:
+ "(window->mappedStart==0||window->mappedStart==mapStart)&&window->mappedMemory==((void*)0)"
+ "/AppleInternal/Library/BuildRoots/0e5e56ba-061f-11f0-a913-122ba06eff56/Library/Caches/com.apple.xbs/Sources/SpotlightCore/spotlight/MetadataUtilities/MDPathFilter.m"
+ "/AppleInternal/Library/BuildRoots/0e5e56ba-061f-11f0-a913-122ba06eff56/Library/Caches/com.apple.xbs/Sources/SpotlightCore/spotlight/MetadataUtilities/MDPathFilterGenerator.m"
+ "/AppleInternal/Library/BuildRoots/0e5e56ba-061f-11f0-a913-122ba06eff56/Library/Caches/com.apple.xbs/Sources/SpotlightCore/spotlight/MetadataUtilities/_MDPlistBytes.c"
+ "CFTypeRef copyObject(_MDPlistBytesDeserializationContext *, int *, _Bool, unsigned int, copy_object_behavior_t)"
+ "SISimpleQueue.c"
+ "[automatic cooldown] automatic cooldown enabled: %d"
+ "_kMDItemMediaEmbeddingVersion"
+ "_kMDItemPrimaryTextEmbedding"
+ "_kMDItemTextChunkTokenLength"
+ "addedPlistObject == ((void*)0)"
+ "com.apple.intelligenceflow"
+ "com.apple.omniSearch"
+ "com.apple.ondeviceeval"
+ "destroyed simple queue"
+ "kMDItemEmbeddingVersion"
+ "kMDItemKeyphraseLabels"
+ "kMDItemKeyphraseVersion"
+ "kMDItemTextContentLanguage"
+ "queue->end == (queue->end&(queue->size-1))"
+ "queue->start == (queue->start&(queue->size-1))"
+ "si_enqueue_locked"
+ "si_simplequeue_count_locked"
+ "simple queue"
- "(window->mappedStart==0||window->mappedStart==mapStart)&&window->mappedMemory==((void *)0)"
- "/AppleInternal/Library/BuildRoots/cf117d38-cf63-11ef-b315-aabfac210453/Library/Caches/com.apple.xbs/Sources/SpotlightCore/spotlight/MetadataUtilities/MDPathFilter.m"
- "/AppleInternal/Library/BuildRoots/cf117d38-cf63-11ef-b315-aabfac210453/Library/Caches/com.apple.xbs/Sources/SpotlightCore/spotlight/MetadataUtilities/MDPathFilterGenerator.m"
- "/AppleInternal/Library/BuildRoots/cf117d38-cf63-11ef-b315-aabfac210453/Library/Caches/com.apple.xbs/Sources/SpotlightCore/spotlight/MetadataUtilities/_MDPlistBytes.c"
- "CFTypeRef copyObject(_MDPlistBytesDeserializationContext *, int *, _Bool, unsigned int)"
- "\\U"
- "\\u"
- "^{__CFArray=}"
- "_rleQueue"
- "addedPlistObject == ((void *)0)"

```
