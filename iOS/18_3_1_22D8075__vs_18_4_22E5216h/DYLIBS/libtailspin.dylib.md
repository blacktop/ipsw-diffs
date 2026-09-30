## libtailspin.dylib

> `/usr/lib/libtailspin.dylib`

```diff

-200.2.0.0.0
-  __TEXT.__text: 0x1e04c
-  __TEXT.__auth_stubs: 0xfe0
-  __TEXT.__objc_methlist: 0x14c
-  __TEXT.__const: 0x171
-  __TEXT.__cstring: 0x1a43
-  __TEXT.__oslogstring: 0x2239
-  __TEXT.__gcc_except_tab: 0x12e4
+218.1.0.0.0
+  __TEXT.__text: 0x1eb34
+  __TEXT.__auth_stubs: 0x1060
+  __TEXT.__objc_methlist: 0x1c4
+  __TEXT.__const: 0x189
+  __TEXT.__cstring: 0x1ae6
+  __TEXT.__oslogstring: 0x2433
+  __TEXT.__gcc_except_tab: 0x1274
   __TEXT.__ustring: 0x6
   __TEXT.__dlopen_cstrs: 0x48
-  __TEXT.__unwind_info: 0x6d8
-  __TEXT.__objc_classname: 0x17
-  __TEXT.__objc_methname: 0xe61
-  __TEXT.__objc_methtype: 0xe5
-  __TEXT.__objc_stubs: 0x1040
-  __DATA_CONST.__got: 0x1a8
-  __DATA_CONST.__const: 0x938
+  __TEXT.__unwind_info: 0x790
+  __TEXT.__objc_classname: 0x18
+  __TEXT.__objc_methname: 0x108d
+  __TEXT.__objc_methtype: 0xfb
+  __TEXT.__objc_stubs: 0x10e0
+  __DATA_CONST.__got: 0x1b0
+  __DATA_CONST.__const: 0x958
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x478
+  __DATA_CONST.__objc_selrefs: 0x4c8
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x808
+  __AUTH_CONST.__auth_got: 0x848
   __AUTH_CONST.__auth_ptr: 0x10
   __AUTH_CONST.__const: 0x280
-  __AUTH_CONST.__cfstring: 0x19a0
-  __AUTH_CONST.__objc_const: 0x210
-  __DATA.__objc_ivar: 0x20
+  __AUTH_CONST.__cfstring: 0x1a40
+  __AUTH_CONST.__objc_const: 0x2a0
+  __DATA.__objc_ivar: 0x2c
   __DATA.__data: 0x10
   __DATA.__crash_info: 0x40
   __DATA.__bss: 0x4a8

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libdscsym.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 482
-  Symbols:   506
-  CStrings:  639
+  Functions: 504
+  Symbols:   519
+  CStrings:  676
 
Symbols:
+ _TSPDumpOptions_EndTimestamp
+ _TSPMetadata_SharedCacheInfo
+ _TSPMetadata_SharedCacheResidentSize
+ _TSPMetadata_SharedCacheVirtualSize
+ _dyld_process_create_for_current_task
+ _dyld_process_dispose
+ _dyld_process_snapshot_create_for_process
+ _dyld_process_snapshot_dispose
+ _dyld_process_snapshot_get_shared_cache
+ _dyld_shared_cache_for_each_file
+ _mach_error_string
+ _mincore
+ _mmap
+ _munmap
+ _objc_retain_x24
+ _vm_page_size
- _dispatch_queue_create_with_target$V2
- _objc_retain_x28
- _strdup
CStrings:
+ "%{public, signpost.description:begin_time}llu %{public, signpost.description:end_time}llu numEvents=%{public,name=numEvents}llu requestID=0x%llx enableTelemetry=YES "
+ "11"
+ "@\"NSString\""
+ "B"
+ "B16@0:8"
+ "Ended read session: %{public}@ [%d], original fd: %d, duped fd: %d"
+ "MAX_CHUNK_SIZE 0x%x isn't a page multiple 0x%lx"
+ "PostProcessing_Libktrace"
+ "PostProcessing_Tailspin"
+ "Saved %{bytes}lld tailspin on behalf of %{public}@ [%d]"
+ "Saved %{bytes}lld tailspin on behalf of %{public}@ [%d] (augment failed)"
+ "SharedCacheInfo"
+ "SharedCacheSizeResident"
+ "SharedCacheSizeVirtual"
+ "Started read session: %{public}@ [%d], original fd: %d, duped fd: %d, size: %{bytes}lld"
+ "T@\"NSString\",&,N,V_prevExecName"
+ "TB,N,V_didClientRequestEndTimestamp"
+ "TB,N,V_didPrevClientSaveOverlapWithEndTimestamp"
+ "Unable to create read session for original fd %d (duped fd %d) from client %{public}@ [%d].: %{errno}d"
+ "Unable to fstat %{public}@'s saved tailspin file: %{errno}d"
+ "Unable to get ktfile for original fd %d (duped fd %d) from client %{public}@ [%d].: %{errno}d"
+ "Unable to start read session for original fd %d (duped fd %d) from client %{public}@ [%d].: %{errno}d"
+ "_didClientRequestEndTimestamp"
+ "_didPrevClientSaveOverlapWithEndTimestamp"
+ "_prevExecName"
+ "didClientRequestEndTimestamp"
+ "didPrevClientSaveOverlapWithEndTimestamp"
+ "failed to create dyld process:%d (%s)"
+ "failed to create snapshot of the process:%d (%s)"
+ "failed to fstat shared cache file %s: %{errno}d"
+ "failed to get shared cache"
+ "failed to open shared cache file %s: %{errno}d"
+ "mincore of 0x%llx,0x%llx of shared cache file %s failed: %{errno}d"
+ "mmap of 0x%llx,0x%llx of shared cache file %s failed: %{errno}d"
+ "munmap of 0x%llx,0x%llx of shared cache file %s failed: %{errno}d"
+ "native shared cache has %llu/%llu pages resident"
+ "prevExecName"
+ "setDidClientRequestEndTimestamp:"
+ "setDidPrevClientSaveOverlapWithEndTimestamp:"
+ "setPrevExecName:"
+ "shared cache file %s has %llu/%llu pages resident"
+ "startRecordingTimeForLibktracePostProcessing"
+ "startRecordingTimeForTailspinPostProcessing"
+ "stopRecordingTimeForLibktracePostProcessing"
+ "stopRecordingTimeForTailspinPostProcessing"
+ "tailspin_dump_option_end_timestamp"
+ "v16@?0r*8"
- "!"
- "%{public, signpost.description:begin_time}llu %{public, signpost.description:end_time}llu numEvents=%{public,name=numEvents}llu enableTelemetry=YES "
- "Ended read session: %{public}s [%d], original fd: %d, duped fd: %d"
- "Ended writing fd: %{public}s [%d], original fd: %d, duped fd: %d"
- "Saved %{bytes}lld tailspin on behalf of %{public}s [%d]"
- "Saved %{bytes}lld tailspin on behalf of %{public}s [%d] (augment failed)"
- "Started read session: %{public}s [%d], original fd: %d, duped fd: %d, size: %{bytes}lld"
- "Unable to create read session for original fd %d (duped fd %d) from client %{public}s [%d].: %{errno}d"
- "Unable to fstat %{public}s's saved tailspin file: %{errno}d"
- "Unable to get ktfile for original fd %d (duped fd %d) from client %{public}s [%d].: %{errno}d"
- "Unable to start read session for original fd %d (duped fd %d) from client %{public}s [%d].: %{errno}d"
- "com.apple.tailspind.post-processing-queue"

```
