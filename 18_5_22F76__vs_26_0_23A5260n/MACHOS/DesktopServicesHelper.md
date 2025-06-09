## DesktopServicesHelper

> `/System/Library/PrivateFrameworks/DesktopServicesPriv.framework/DesktopServicesHelper`

```diff

-1732.6.1.0.0
-  __TEXT.__text: 0x4b7b0
-  __TEXT.__auth_stubs: 0x1600
-  __TEXT.__objc_stubs: 0x1620
+1818.0.0.0.0
+  __TEXT.__text: 0x5d490
+  __TEXT.__auth_stubs: 0x1610
+  __TEXT.__objc_stubs: 0x1b80
   __TEXT.__init_offsets: 0x4
-  __TEXT.__objc_methlist: 0x69c
-  __TEXT.__gcc_except_tab: 0x6848
-  __TEXT.__cstring: 0x122c
-  __TEXT.__const: 0x10a8
-  __TEXT.__oslogstring: 0xbeb
-  __TEXT.__objc_classname: 0xf8
+  __TEXT.__objc_methlist: 0x734
+  __TEXT.__gcc_except_tab: 0x80cc
+  __TEXT.__cstring: 0x16b2
+  __TEXT.__const: 0x12a0
+  __TEXT.__oslogstring: 0xf36
+  __TEXT.__objc_classname: 0x117
   __TEXT.__ustring: 0x4
-  __TEXT.__objc_methname: 0x15de
-  __TEXT.__objc_methtype: 0x30f
-  __TEXT.__unwind_info: 0x2360
-  __DATA_CONST.__auth_got: 0xb10
-  __DATA_CONST.__got: 0x470
-  __DATA_CONST.__const: 0x1098
-  __DATA_CONST.__cfstring: 0x780
-  __DATA_CONST.__objc_classlist: 0x30
+  __TEXT.__objc_methname: 0x1ae8
+  __TEXT.__objc_methtype: 0xe0c
+  __TEXT.__unwind_info: 0x2b30
+  __DATA_CONST.__auth_got: 0xb18
+  __DATA_CONST.__got: 0x4a0
+  __DATA_CONST.__const: 0x13c8
+  __DATA_CONST.__cfstring: 0x7c0
+  __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x28
+  __DATA_CONST.__objc_superrefs: 0x30
   __DATA_CONST.__objc_arraydata: 0x48
   __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA_CONST.__objc_intobj: 0x30
-  __DATA.__objc_const: 0xac0
-  __DATA.__objc_selrefs: 0x730
-  __DATA.__objc_ivar: 0x54
-  __DATA.__objc_data: 0x1e0
-  __DATA.__data: 0x370
-  __DATA.__common: 0x1c2
-  __DATA.__bss: 0x4a8
+  __DATA_CONST.__objc_intobj: 0x48
+  __DATA.__objc_const: 0xc58
+  __DATA.__objc_selrefs: 0x870
+  __DATA.__objc_ivar: 0x70
+  __DATA.__objc_data: 0x230
+  __DATA.__data: 0x448
+  __DATA.__common: 0x1be
+  __DATA.__bss: 0x510
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/FileProvider.framework/FileProvider

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 9DBE6AFD-5B69-36AB-B7B6-439A0DE6A615
-  Functions: 1299
-  Symbols:   511
-  CStrings:  714
+  UUID: 8811CBE0-1E7F-3163-8032-7C80FD147F32
+  Functions: 1531
+  Symbols:   517
+  CStrings:  849
 
Symbols:
+ _CFStringCreateWithBytesNoCopy
+ _OBJC_CLASS_$_NSNull
+ __ZNSt3__112bad_weak_ptrD1Ev
+ __ZNSt3__119__shared_weak_count4lockEv
+ __ZTINSt3__112bad_weak_ptrE
+ __ZTVNSt3__112bad_weak_ptrE
+ ___cxa_rethrow
+ __os_feature_enabled_impl
+ _dlopen
+ _kCFURLVolumeTypeNameKey
+ _objc_getClass
+ _objc_storeWeak
+ _printf
+ _pthread_setname_np
+ _strerror
- __Znwm
- _objc_setProperty_nonatomic_copy
- _pthread_mutex_destroy
- _pthread_mutex_init
- _pthread_mutex_lock
- _pthread_mutex_unlock
- _pthread_mutexattr_destroy
- _pthread_mutexattr_init
- _pthread_mutexattr_settype
CStrings:
+ "%{public}s, ContinuedProcessingTaskRequest:%{public}@, Title:%{public}@, Reason:%{public}@"
+ "-[DSFileService requestBGTask:]"
+ ".VolumeIcon.icns"
+ "/System/Library/Frameworks/BackgroundTasks.framework/BackgroundTasks"
+ "0"
+ "1 0"
+ "@\"NSObject<OS_dispatch_queue>\""
+ "@\"_BGContinuedProcessingTask\""
+ "@40@0:8r^v16r^v24r^v32"
+ "AppGroup"
+ "BGTaskScheduler"
+ "Cancelling progress for group %{public}@"
+ "CloudStorage"
+ "Continuous background task registration failed for id: %{public}@"
+ "Continuous background task registration succeeded for id: %{public}@"
+ "Copying files"
+ "CreateFilesOnThread"
+ "DSProgress setUpGroupForChildProgress: Added child to %{public}@ - new count: %lu"
+ "DS_TKeyValueObserverGlue"
+ "DesktopServices"
+ "Error removing checkpoint '%{public}s' for %{public}@"
+ "Error(%d) removing xattr %{public}s from %{public}@"
+ "FIOperation"
+ "Failed to submit background task request: %{public}@ for group id %{public}@"
+ "File Provider Storage"
+ "Finder"
+ "Finder.app"
+ "ForceHighThroughputSSDOptimization"
+ "FruitBasket-"
+ "GlobalCopyProgress"
+ "Got nil for path %@"
+ "Icon?"
+ "LastRoot"
+ "Main Reader thread"
+ "Main Writer thread"
+ "MaxActiveReadThreads"
+ "MaxActiveWriteThreads"
+ "MaxReadThreads"
+ "MaxWriteThreads"
+ "Mobile Documents"
+ "NO"
+ "Network"
+ "No groups awaiting tasks"
+ "Other error "
+ "Preparing..."
+ "Read Data Thread"
+ "RunCopyMoveOperation"
+ "RunSetRootMetadata"
+ "Running with QOS level %d"
+ "Shared"
+ "Submitted background task request with progress UI %@ for group id %{public}@"
+ "T@\"NSDate\",R,N,V_dateStarted"
+ "T@\"NSMutableDictionary\",R,N,V_childProgresses"
+ "T@\"NSMutableDictionary\",R,N,V_progressGroups"
+ "T@\"NSObject<OS_dispatch_queue>\",&,N,V_backgroundProcessingQueue"
+ "T@\"NSProgress\",R,N,V_progress"
+ "T@\"NSString\",R,N,V_firstChildName"
+ "T@\"NSURL\",R,N,V_publishingURL"
+ "T@\"NSUUID\",R,N,V_uuid"
+ "T@\"_BGContinuedProcessingTask\",&,V_continuedUITask"
+ "TCopyWriter::WriteDataFork dequeue aborted. status=%d"
+ "UTType is nil for identifier '%{public}@' - falling back to %{public}@"
+ "Unable to find path for key %{pubic}s"
+ "Unable to find progress group for %{public}@"
+ "Unable to publish progress to file with error=%d, id=%{public}@, %{public}@"
+ "Unknown error:"
+ "W"
+ "Write Data Thread"
+ "WriteDataForksOnThread"
+ "_BGContinuedProcessingTaskRequest"
+ "_NSBPlistMappedString"
+ "_backgroundProcessingQueue"
+ "_completedUnitCountObservers"
+ "_continuedUITask"
+ "_functor"
+ "_functorWithChange"
+ "_observedKeyPath"
+ "_observedObjects"
+ "apfs"
+ "arrayWithCapacity:"
+ "backgroundProcessingQueue"
+ "byteCompletedCount"
+ "byteTotalCount"
+ "com.apple.DocumentsApp"
+ "com.apple.desktopservices.desktopserviceshelper.progress."
+ "com.apple.desktopservices.desktopserviceshelper.progress.bgtaskschedulerqueue"
+ "completedUnitCountDidChange:forProgress:"
+ "com~apple~"
+ "continuedUITask"
+ "createNewRequestForGroupUUID:"
+ "exfat"
+ "false"
+ "groupForChildProgress:"
+ "handleContinuousProcessingTask:withGroupUUID:"
+ "hfs"
+ "iCloud~com~apple~"
+ "initCommon:observedKeyPath:"
+ "initWithFunctor:observedObjects:observedKeyPath:"
+ "initWithFunctorWithChange:observedObjects:observedKeyPath:"
+ "initWithIdentifier:iconBundleIdentifier:applicationBundleIdentifier:"
+ "isEqualToNumber:"
+ "isIndeterminate"
+ "isTornDown"
+ "kRunCopyMoveOperationMsg"
+ "kRunSetRootMetadataMsg"
+ "kind"
+ "localizedAdditionalDescription"
+ "localizedStringWithFormat:"
+ "longLongValue"
+ "msdos"
+ "numberWithLongLong:"
+ "objectForKey:"
+ "options"
+ "private"
+ "progressWithTotalUnitCount:"
+ "reason"
+ "registerChildProgress:"
+ "registerForTaskWithIdentifier:usingQueue:launchHandler:"
+ "removeObserver:forKeyPath:"
+ "removeObserver:fromObjectsAtIndexes:forKeyPath:"
+ "requestBGTask:"
+ "setBackgroundProcessingQueue:"
+ "setByteCompletedCount:"
+ "setByteTotalCount:"
+ "setCancellable:"
+ "setContinuedUITask:"
+ "setExpirationHandler:"
+ "setLocalizedAdditionalDescription:"
+ "setReason:"
+ "setTaskCompletedWithSuccess:"
+ "setTitle:"
+ "setUserInfoObject:forKey:"
+ "setting QOS level to %d"
+ "sharedScheduler"
+ "stringByAppendingString:"
+ "stringWithUTF8String:"
+ "submitTaskRequest:error:"
+ "title"
+ "typeWithIdentifier:"
+ "updateProgress:"
+ "updateTitle:withReason:"
+ "using a custom value %lld for MaxActiveReadThreads\n"
+ "using a custom value %lld for MaxActiveWriteThreads\n"
+ "using a custom value %lld for MaxReadThreads\n"
+ "using a custom value %lld for MaxWriteThreads\n"
+ "v16@?0@\"_BGContinuedProcessingTask\"8"
+ "v32@0:8@16@24"
+ "v32@0:8r^v16r^v24"
+ "{TString=\"fString\"{TRef<const __CFString *, TRetainReleasePolicy<CFStringRef>>=\"fRef\"^{__CFString}}}"
+ "{function<void ()>=\"__f_\"{__value_func<void ()>=\"__buf_\"(type=\"__data\"[24C])\"__f_\"^v}}"
+ "{function<void (NSDictionary<NSString *,NSObject *> *)>=\"__f_\"{__value_func<void (NSDictionary<NSString *,NSObject *> *)>=\"__buf_\"(type=\"__data\"[24C])\"__f_\"^v}}"
+ "{mutex=\"__m_\"{_opaque_pthread_mutex_t=\"__sig\"q\"__opaque\"[56c]}}"
+ "{optional_bool=\"\"(?=\"__null_state_\"c\"__val_\"B)\"__engaged_\"B}"
+ "{unordered_map<NSProgress *, TKeyValueObserver, std::hash<NSProgress *>, std::equal_to<NSProgress *>, std::allocator<std::pair<NSProgress *const, TKeyValueObserver>>>=\"__table_\"{__hash_table<std::__hash_value_type<NSProgress *, TKeyValueObserver>, std::__unordered_map_hasher<NSProgress *, std::__hash_value_type<NSProgress *, TKeyValueObserver>, std::hash<NSProgress *>, std::equal_to<NSProgress *>>, std::__unordered_map_equal<NSProgress *, std::__hash_value_type<NSProgress *, TKeyValueObserver>, std::equal_to<NSProgress *>, std::hash<NSProgress *>>, std::allocator<std::__hash_value_type<NSProgress *, TKeyValueObserver>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<NSProgress *, TKeyValueObserver>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<NSProgress *, TKeyValueObserver>, void *> *> *>>>=\"__ptr_\"^^v\"__deleter_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<NSProgress *, TKeyValueObserver>, void *> *> *>>=\"__size_\"Q}}\"__first_node_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<NSProgress *, TKeyValueObserver>, void *> *>=\"__next_\"^v}\"__size_\"Q\"__max_load_factor_\"f}}"
+ "{unordered_set<NSObject *__unsafe_unretained, std::hash<NSObject *__unsafe_unretained>, std::equal_to<NSObject *__unsafe_unretained>, std::allocator<NSObject *__unsafe_unretained>>=\"__table_\"{__hash_table<NSObject *__unsafe_unretained, std::hash<NSObject *__unsafe_unretained>, std::equal_to<NSObject *__unsafe_unretained>, std::allocator<NSObject *__unsafe_unretained>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<NSObject *__unsafe_unretained, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<NSObject *__unsafe_unretained, void *> *> *>>>=\"__ptr_\"^^v\"__deleter_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<NSObject *__unsafe_unretained, void *> *> *>>=\"__size_\"Q}}\"__first_node_\"{__hash_node_base<std::__hash_node<NSObject *__unsafe_unretained, void *> *>=\"__next_\"^v}\"__size_\"Q\"__hasher_\"{hash<NSObject *__unsafe_unretained>=\"fHash\"{hash<NSObject *>=}}\"__max_load_factor_\"f\"__key_eq_\"{equal_to<NSObject *__unsafe_unretained>=\"fEqual\"{equal_to<NSObject *>=}}}}"
- "CopyBasicBufferSizeKB"
- "Error removing checkpoint '%d' for %{public}@"
- "T@\"NSDate\",R,C,N,V_dateStarted"
- "T@\"NSMutableDictionary\",&,N,V_childProgresses"
- "T@\"NSMutableDictionary\",&,V_progressGroups"
- "T@\"NSProgress\",C,N,V_progress"
- "T@\"NSString\",R,C,N,V_firstChildName"
- "T@\"NSURL\",C,N,V_publishingURL"
- "T@\"NSUUID\",C,N,V_uuid"
- "TCopyWriter::WriteDataFork bad buffer item. status=%d"
- "Writer could not find cached clone. status=%d"
- "com.apple.decmpfs"
- "dictionary"
- "numberWithUnsignedInt:"
- "removeObserver:forKeyPath:context:"
- "setChildProgresses:"
- "setProgressGroups:"
- "setPublishingURL:"
- "setUuid:"
- "unsignedIntValue"
- "{TDSMutex=\"fMutex\"{_opaque_pthread_mutex_t=\"__sig\"q\"__opaque\"[56c]}}"
- "{optional<bool>=\"\"(?=\"__null_state_\"c\"__val_\"B)\"__engaged_\"B}"

```
