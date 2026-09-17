## VideoIntelligence

> `/System/Library/PrivateFrameworks/VideoIntelligence.framework/Versions/A/VideoIntelligence`

```diff

-32.3.0.0.0
-  __TEXT.__text: 0x124fc4
+33.12.0.0.0
+  __TEXT.__text: 0x17d9bc
   __TEXT.__objc_methlist: 0x3e4
-  __TEXT.__const: 0xc840
-  __TEXT.__swift5_typeref: 0x3e26
-  __TEXT.__cstring: 0x3886
-  __TEXT.__constg_swiftt: 0x31e4
-  __TEXT.__swift5_reflstr: 0x21a2
-  __TEXT.__swift5_fieldmd: 0x28dc
+  __TEXT.__const: 0xf938
+  __TEXT.__swift5_typeref: 0x4ec4
+  __TEXT.__cstring: 0x3d06
+  __TEXT.__constg_swiftt: 0x42bc
+  __TEXT.__swift5_reflstr: 0x2a52
+  __TEXT.__swift5_fieldmd: 0x346c
   __TEXT.__swift5_builtin: 0x1a4
-  __TEXT.__swift5_capture: 0xc70
-  __TEXT.__swift5_assocty: 0x940
-  __TEXT.__swift5_protos: 0x88
-  __TEXT.__swift5_proto: 0xaec
-  __TEXT.__swift5_types: 0x378
-  __TEXT.__swift_as_entry: 0x1d0
-  __TEXT.__swift_as_ret: 0x244
-  __TEXT.__swift_as_cont: 0x494
-  __TEXT.__swift5_mpenum: 0x64
-  __TEXT.__swift5_types2: 0x4
-  __TEXT.__oslogstring: 0x2fde
+  __TEXT.__swift5_capture: 0x11c8
+  __TEXT.__swift5_assocty: 0xfc0
+  __TEXT.__swift5_protos: 0xc0
+  __TEXT.__swift5_proto: 0xe04
+  __TEXT.__swift5_types: 0x490
+  __TEXT.__swift_as_entry: 0x294
+  __TEXT.__swift_as_ret: 0x31c
+  __TEXT.__swift_as_cont: 0x60c
+  __TEXT.__oslogstring: 0x48f4
+  __TEXT.__swift5_mpenum: 0x50
+  __TEXT.__swift5_types2: 0x8
   __TEXT.__gcc_except_tab: 0xca8
-  __TEXT.__unwind_info: 0x3ca8
-  __TEXT.__eh_frame: 0x69c0
+  __TEXT.__unwind_info: 0x4e88
+  __TEXT.__eh_frame: 0x88c8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x3c0
-  __DATA_CONST.__objc_classlist: 0xa0
+  __DATA_CONST.__const: 0x3d0
+  __DATA_CONST.__objc_classlist: 0xe0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x378
+  __DATA_CONST.__objc_selrefs: 0x398
   __DATA_CONST.__objc_superrefs: 0x28
-  __DATA_CONST.__got: 0x658
-  __AUTH_CONST.__const: 0x6b38
+  __DATA_CONST.__got: 0x720
+  __AUTH_CONST.__const: 0x99c0
   __AUTH_CONST.__cfstring: 0x360
-  __AUTH_CONST.__objc_const: 0x1b20
-  __AUTH_CONST.__auth_got: 0x1098
-  __AUTH.__objc_data: 0x3b0
-  __AUTH.__data: 0x1ea0
+  __AUTH_CONST.__objc_const: 0x23d8
+  __AUTH_CONST.__auth_got: 0x1218
+  __AUTH.__objc_data: 0x400
+  __AUTH.__data: 0x2f20
   __DATA.__objc_ivar: 0x4c
-  __DATA.__data: 0x2818
-  __DATA.__common: 0x72
+  __DATA.__data: 0x3610
+  __DATA.__common: 0xe2
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/Versions/A/CoreGraphics
   - /System/Library/Frameworks/CoreVideo.framework/Versions/A/CoreVideo

   - /System/Library/PrivateFrameworks/MobileAsset.framework/Versions/A/MobileAsset
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
+  - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 4103
-  Symbols:   353
-  CStrings:  512
+  Functions: 5393
+  Symbols:   375
+  CStrings:  635
 
Symbols:
+ _OBJC_CLASS_$_NSUserDefaults
+ _OBJC_CLASS_$_OS_dispatch_queue_serial
+ __swift_FORCE_LOAD_$_swiftAccelerate
+ _dispatch_activate
+ _dispatch_async
+ _dispatch_barrier_async
+ _dispatch_block_create_with_voucher
+ _dispatch_block_create_with_voucher_and_qos_class
+ _dispatch_workloop_create_inactive
+ _dispatch_workloop_set_os_workgroup
+ _dispatch_workloop_set_qos_class_floor
+ _notify_cancel
+ _notify_register_dispatch
+ _pthread_get_qos_class_np
+ _pthread_mach_thread_np
+ _pthread_self
+ _pthread_threadid_np
+ _swift_copyPOD
+ _swift_deletedAsyncMethodErrorTu
+ _swift_initStructMetadata
+ _swift_task_future_wait_throwing
+ _swift_unknownObjectRelease_n
+ _swift_unknownObjectRetain_n
+ _voucher_copy
- _OBJC_CLASS_$_OS_dispatch_queue_concurrent
- _OBJC_CLASS_$_OS_dispatch_workloop
CStrings:
+ " has unknown QoS"
+ ") with relative priority "
+ "1.0"
+ "11.0"
+ "3.0"
+ "3.3"
+ "5.0"
+ "6.0"
+ "7.0"
+ "AssetRegistry %s abandoning the resolution of %s: a result has already been delivered"
+ "AssetRegistry %s discarding cached resolutions: a source changed what it can serve (was %{public}s, now %{public}s)"
+ "AssetRegistry %s discarding the failure of an abandoned resolution of %s: %@"
+ "AssetRegistry %s joining an in-flight assets resolution of %s"
+ "AssetRegistry %s joining an in-flight resolution of %s"
+ "AssetRegistry %s: %s contributes no key: %@"
+ "AssetRegistry %s: %s has lost its owning registry"
+ "AssetRegistry %s: no source served %s, reporting %@ after skipping %s"
+ "AssetRegistry %s: not caching %s, resolved before a provider refresh"
+ "AssetRegistry %s: not caching the assets for %s, %s"
+ "AssetRegistry %s: skipping %s, resolving error: %@"
+ "AssetRegistry %s: timed out waiting for the %s provider to finish resolving %s"
+ "I/O bindings have been previously committed, decommitting before binding"
+ "MobileAssetSupport"
+ "MobileAsset_WorkRateMETs"
+ "ModelAvailability(introduced: "
+ "Mulberry"
+ "Mulberry.WorkRateMETs"
+ "QoS"
+ "Threading"
+ "TransientError"
+ "Unexpected model: "
+ "VINDispatchAsync: failed to create block with QoS class 0x%x and relative priority %d"
+ "VideoIntelligence.VFM.Mulberry.OverriddenAdapters"
+ "VideoIntelligence.VFM.Mulberry.OverriddenFunctionName"
+ "VideoIntelligence.VFM.Mulberry.OverriddenModelPath"
+ "VideoIntelligence/MulberryInferenceProvider.swift"
+ "VideoIntelligence/MulberryModel.swift"
+ "WorkAttribution(0x"
+ "[AssetRegistrySource] [MA] [Catalog] starting download, QoS %{public}s, %{public}s"
+ "[AssetRegistrySource] [MA] [Download] startDownload, QoS %{public}s, %{public}s"
+ "[AssetRegistrySource] [MA] [Query] issuing query, QoS %{public}s, %{public}s"
+ "[AssetRegistrySource] [MA] _downloadAsset(), QoS %{public}s, %{public}s"
+ "[AssetRegistrySource] [MA] _ensureMetadataAssetDownloaded(), QoS %{public}s, %{public}s"
+ "[AssetRegistrySource] [MA] _findAssetAndRetry(), QoS %{public}s, %{public}s"
+ "[AssetRegistrySource] [MA] joining in-flight fetch, QoS %{public}s, effective QoS %{public}s"
+ "[AssetRegistrySource] [MA] joining in-flight resolution, QoS %{public}s, effective QoS %{public}s"
+ "[AssetRegistry] AssetRegistry %s resolve(), QoS %{public}s, %{public}s"
+ "[AssetRegistry] AssetRegistry %s resolveAssets(for:), QoS %{public}s, %{public}s"
+ "[MA] [Catalog] catalog change announces a download of ours, left for it to count"
+ "[MA] [Catalog] catalog change arrived after the source went away"
+ "[MA] [Catalog] could not observe catalog changes: notify status %u"
+ "[MA] [Catalog] could not stop observing catalog changes: notify status %u"
+ "[MA] [Catalog] counting the catalog change claimed by a download that failed, now generation %{public}s"
+ "[MA] [Catalog] mobileassetd replaced the catalog, now generation %{public}s"
+ "[MA] [Catalog] observing %{public}s"
+ "[MA] [Catalog] stopped observing catalog changes, token %d"
+ "[MA] [Download] cancelled before reaching MobileAsset: %s"
+ "[MA] [Download] cancelled downloading asset: %@"
+ "[MA] [Download] downloaded %s in %fs"
+ "[MA] [Download] downloaded but not refreshable: %s"
+ "[MA] [Download] downloading %s, progress: %@"
+ "[MA] [Download] failed to cancel: %@, %ld"
+ "[MA] [Download] failed: %@, %ld, %s"
+ "[MA] [Download] installed but refresh failed: %s"
+ "[MA] [Download] not starting, its client cancelled: %s"
+ "[MA] [Download] succeeded with an error attached: %@: %@"
+ "[MA] [Fetch] %s lost the publish race %ld times, giving up on this attempt"
+ "[MA] [Fetch] %s not local, state: %ld"
+ "[MA] [Metadata] %s: %@, reporting %@"
+ "[MA] [Metadata] %s: query %@, reporting %@"
+ "[MA] [Metadata] already downloaded: %s"
+ "[MA] [Metadata] asset download already in progress, consolidating..."
+ "[MA] [Metadata] asset is not local after download: %s, state: %ld"
+ "[MA] [Metadata] discarding assets found under catalog generation %{public}s, now %{public}s"
+ "[MA] [Metadata] no catalog refresh landed, querying installed assets instead: %@"
+ "[MA] [Metadata] not caching an asset found before a catalog refresh: %s"
+ "[MA] [Metadata] prior asset download completed, retrying..."
+ "[MA] [Query] a catalog landed while resolving an asset this device has not installed, asking again"
+ "[MA] [Query] a catalog landed while this query ran, leaving its freshness alone and keeping the wind-back"
+ "[MA] [Query] failed: result %ld, error: %@"
+ "[MA] [Query] failed: succeeded but reported an error: %@"
+ "[MA] [Query] found %s %s/%s in %fs"
+ "[MA] [Query] matched within allowed differences"
+ "[MA] [Query] no catalog landed for the retry, not asking the daemon again"
+ "[MA] [Query] no installed asset to prefer over the listed one, keeping %s"
+ "[MA] [Query] no locally installed asset among the results"
+ "[MA] [Query] no usable catalog, considering only locally installed assets"
+ "[MA] [Query] skipping asset missing AssetVersionInfo: %s"
+ "[MA] [Query] skipping asset missing BuildVersionTuple: %s"
+ "[MA] [Query] skipping asset missing BundleVersionTuple: %s"
+ "[MA] [Query] the catalog could not be refreshed, preferring the installed %s over the listed %s"
+ "[MA] [Query] the wind-back is already spent, leaving the freshness window to govern the next attempt"
+ "[MA] discarding assets built under catalog generation %{public}s, now %{public}s"
+ "[MA] ignoring a second completion for an already-retired operation"
+ "[MA] sharing an asset whose work is still in flight: %s"
+ "[Mulberry] MulberryInferenceProvider.prepare() called, %{public}s"
+ "[Mulberry] MulberryInferenceProvider.prepare(), QoS %{public}s, %{public}s"
+ "[Mulberry] MulberryInferenceProvider.run() called, %{public}s"
+ "[Mulberry] MulberryModel.fetching() task started, %{public}s"
+ "[Mulberry] MulberryModel.fetching(), QoS %{public}s, %{public}s"
+ "[Mulberry] MulberryModel.resolvingState() task started, %{public}s"
+ "[Mulberry] MulberryModel.resolvingState(), QoS %{public}s, %{public}s"
+ "[OVERRIDING] Ignoring inaccessible Mulberry adapter: %s: %s"
+ "[OVERRIDING] Ignoring inaccessible Mulberry model path: %s"
+ "[OVERRIDING] Mulberry adapter: %s: %s"
+ "[OVERRIDING] Mulberry function name: %s"
+ "[OVERRIDING] Mulberry model has been overridden via UserDefaults"
+ "[OVERRIDING] Mulberry model path: %s"
+ "[wrMETs] MA FF is disabled."
+ "[wrMETs] MA FF is enabled."
+ "abandoned the resolution of requirement: %s"
+ "angular_uncertainty"
+ "assetMetadata(for:compatibilityVersion:escalating:)"
+ "boosted work in progress, %{public}s"
+ "clamping out-of-range relative priority %{public}d to %{public}d"
+ "com.apple.MobileAsset.VideoIntelligence.ma.cached-metadata-updated"
+ "com.apple.VideoIntelligence."
+ "decommitting I/O bindings"
+ "dev_placeholder_out"
+ "discarding cached metadata: the source changed what it can serve (was %{public}s, now %{public}s)"
+ "done decommitting I/O bindings"
+ "dropping relative priority %{public}d attached to an unspecified QoS class"
+ "error decommitting I/O bindings"
+ "fetching(escalating:)"
+ "fetching(scheduling:)"
+ "has uncommitted I/O bindings"
+ "ignoring unsupported QoS class 0x%{public}x"
+ "invalidationKey: requires concrete implementation"
+ "joints_uncertainty"
+ "metadata is already being loaded with requirement: %s, joining the load in progress"
+ "not caching a metadata load failure answered before a provider refresh, %s: %@"
+ "not caching a resolution failure answered before a provider refresh, %s: %@"
+ "not caching a transient metadata load failure for requirement: %s, error: %@"
+ "not caching a transient resolution failure for requirement: %s, error: %@"
+ "not caching metadata loaded before a provider refresh, %s"
+ "pthread_get_qos_class_np(0x%{public}lx) failed: %d"
+ "pthread_threadid_np(0x%{public}lx) failed: %d"
+ "requirement depends on itself: %s, recursive requirement detected"
+ "resolution of requirement: %s was cancelled"
+ "resolvingState(escalating:)"
+ "resolvingState(scheduling:)"
+ "startResolving(requirement:escalating:completionHandler:): requires concrete implementation"
+ "unclassified error answered as transient; add a `TransientError` conformance to have it decided: %@"
+ "user-interactive"
+ "uvd_joints_variance"
- "AssetRegistry %s: all sources not available"
- "AssetRegistry %s: skipping mobile asset provider %s, due to resolving error %@"
- "AssetRegistry %s: timed out waiting for %s to finish resolving %s"
- "I/O bindings have been previously committed, decommiting before binding"
- "VideoIntelligence/AssetMetadataProviding.swift"
- "[MA] [Download] asset successfully downloaded: %s, elapsed time: %f"
- "[MA] [Download] cancelled downloading asset: %s"
- "[MA] [Download] downloading asset: %s, progress: %@"
- "[MA] [Download] failed to cancel downloading asset: %s, result: %ld"
- "[MA] [Download] failed to download asset: %s, error: %@"
- "[MA] [Metadata] asset already downloaded: %s"
- "[MA] [Query] failed: %@"
- "[MA] [Query] found asset: %@, bundle version: %s, build version: %s, elapsed time: %f"
- "[MA] [Query] skipping asset missing AssetVersionInfo: %@"
- "[MA] [Query] skipping asset missing BuildVersionTuple: %@"
- "[MA] [Query] skipping asset missing BundleVersionTuple: %@"
- "decommiting I/O bindings"
- "done decommiting I/O bindings"
- "error decommiting I/O bindings"
- "has uncommited I/O bindings"
- "ongoing resolution for requirement: %s, recursive requirement detected"
- "resolve(requirement:completionHandler:): requires concrete implementation"
```
