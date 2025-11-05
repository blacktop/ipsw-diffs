## TVIdleServices

> `/System/Library/PrivateFrameworks/TVIdleServices.framework/Versions/A/TVIdleServices`

```diff

-511.30.12.0.0
-  __TEXT.__text: 0x7986c
-  __TEXT.__auth_stubs: 0xc90
-  __TEXT.__objc_methlist: 0x2ff8
-  __TEXT.__const: 0xda
-  __TEXT.__gcc_except_tab: 0x2030
-  __TEXT.__cstring: 0x677c
-  __TEXT.__oslogstring: 0x3ac6
+511.40.53.0.0
+  __TEXT.__text: 0x7c070
+  __TEXT.__auth_stubs: 0xcc0
+  __TEXT.__objc_methlist: 0x3624
+  __TEXT.__const: 0xca
+  __TEXT.__gcc_except_tab: 0x2028
+  __TEXT.__cstring: 0x6aed
+  __TEXT.__oslogstring: 0x3b06
   __TEXT.__swift5_typeref: 0x135
   __TEXT.__swift5_capture: 0x1b8
   __TEXT.__constg_swiftt: 0x5c
   __TEXT.__swift5_reflstr: 0x7
   __TEXT.__swift5_fieldmd: 0x1c
   __TEXT.__swift5_types: 0x4
-  __TEXT.__unwind_info: 0xea8
+  __TEXT.__swift_as_entry: 0x8
+  __TEXT.__swift_as_ret: 0xc
+  __TEXT.__unwind_info: 0xe88
   __TEXT.__eh_frame: 0x1a0
   __TEXT.__objc_classname: 0x8f8
-  __TEXT.__objc_methname: 0x86a0
+  __TEXT.__objc_methname: 0x86ec
   __TEXT.__objc_methtype: 0x1526
-  __TEXT.__objc_stubs: 0x6a60
-  __DATA_CONST.__got: 0x458
+  __TEXT.__objc_stubs: 0x6a80
+  __DATA_CONST.__got: 0x468
   __DATA_CONST.__const: 0x13c0
   __DATA_CONST.__objc_classlist: 0x210
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0xc0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1f20
+  __DATA_CONST.__objc_selrefs: 0x2038
   __DATA_CONST.__objc_protorefs: 0x40
   __DATA_CONST.__objc_superrefs: 0x170
   __DATA_CONST.__objc_arraydata: 0x68
-  __AUTH_CONST.__auth_got: 0x658
+  __AUTH_CONST.__auth_got: 0x670
   __AUTH_CONST.__const: 0x21f0
-  __AUTH_CONST.__cfstring: 0x2b00
-  __AUTH_CONST.__objc_const: 0xb180
+  __AUTH_CONST.__cfstring: 0x2b20
+  __AUTH_CONST.__objc_const: 0xa6c8
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__objc_arrayobj: 0xc0
   __AUTH.__objc_data: 0x1520
   __AUTH.__data: 0x28
-  __DATA.__objc_ivar: 0x2e8
+  __DATA.__objc_ivar: 0x2ec
   __DATA.__data: 0x970
   __DATA.__bss: 0x388
   __DATA.__common: 0x20

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 87E71F68-40D2-3C37-8E17-17C89A4BE5BD
-  Functions: 1631
-  Symbols:   4589
-  CStrings:  2979
+  UUID: E9F36011-EA0C-3ABE-8243-D201FAEAC722
+  Functions: 1626
+  Symbols:   4596
+  CStrings:  3000
 
Symbols:
+ -[TVISEvolutionServiceUpdate canAccessNetworkQueue]
+ OBJC_IVAR_$_TVISEvolutionServiceUpdate._canAccessNetworkQueue
+ _CacheDeleteCacheable
+ __55-[TVISAerialEvolutionService executeUpdate:completion:]_block_invoke.23
+ __62-[TVISAerialEvolutionService _batchDownloadAssets:completion:]_block_invoke.75
+ __62-[TVISAerialEvolutionService _batchDownloadAssets:completion:]_block_invoke.77
+ __67-[TVISAerialEvolutionService _batchDownloadPreviewsWithCompletion:]_block_invoke.55
+ __72-[TVISAerialEvolutionService _downloadAssetWithID:remoteURL:completion:]_block_invoke.66
+ __72-[TVISAerialEvolutionService _downloadAssetWithID:remoteURL:completion:]_block_invoke.68
+ __72-[TVISAerialEvolutionService _downloadAssetWithID:remoteURL:completion:]_block_invoke.71
+ __76-[TVISAerialEvolutionService _downloadAssetsIfNeededWithContext:completion:]_block_invoke.79
+ __76-[TVISAerialEvolutionService _downloadAssetsIfNeededWithContext:completion:]_block_invoke.83
+ __76-[TVISAerialEvolutionService _downloadAssetsIfNeededWithContext:completion:]_block_invoke.88
+ ___os_log_helper_16_2_5_8_32_8_0_8_0_8_0_8_0
+ ___swift_async_entry_functlets
+ ___swift_async_ret_functlets
+ __block_literal_global.257
+ _objc_msgSend$canAccessNetworkQueue
- __62-[TVISAerialEvolutionService _batchDownloadAssets:completion:]_block_invoke.74
- __62-[TVISAerialEvolutionService _batchDownloadAssets:completion:]_block_invoke.76
- __67-[TVISAerialEvolutionService _batchDownloadPreviewsWithCompletion:]_block_invoke.54
- __72-[TVISAerialEvolutionService _downloadAssetWithID:remoteURL:completion:]_block_invoke.64
- __72-[TVISAerialEvolutionService _downloadAssetWithID:remoteURL:completion:]_block_invoke.67
- __72-[TVISAerialEvolutionService _downloadAssetWithID:remoteURL:completion:]_block_invoke.70
- __76-[TVISAerialEvolutionService _downloadAssetsIfNeededWithContext:completion:]_block_invoke.78
- __76-[TVISAerialEvolutionService _downloadAssetsIfNeededWithContext:completion:]_block_invoke.82
- __76-[TVISAerialEvolutionService _downloadAssetsIfNeededWithContext:completion:]_block_invoke.87
- ___55-[TVISAerialEvolutionService executeUpdate:completion:]_block_invoke_2
- __block_literal_global.252
CStrings:
+ "%s - Attempting asset download - limit=%lu (minimum=%lu, existing=%lu, total=%lu)"
+ "%s - Completed with purged amount: %{public}ld, urgency: %{public}ld, volume: %@"
+ "%s - Skipped downloading; network queue inaccessible"
+ "-[TVISAerialEvolutionService executeUpdate:completion:]_block_invoke"
+ "B32@0:8@16^^{archive_entry}24"
+ "Error writing archive header. Couldn't set file destination path."
+ "Insufficient space allocated to copy string contents"
+ "String index is out of bounds"
+ "Swift/ContiguousArrayBuffer.swift"
+ "Swift/StringTesting.swift"
+ "Swift/StringUTF8View.swift"
+ "Swift/UnsafeRawPointer.swift"
+ "TB,R,N,V_canAccessNetworkQueue"
+ "UnsafeMutableBufferPointer with negative count"
+ "UnsafeMutablePointer.initialize overlapping range"
+ "UnsafeMutablePointer.initialize with negative count"
+ "UnsafeMutablePointer.moveInitialize with negative count"
+ "UnsafeMutableRawPointer.initializeMemory overlapping range"
+ "UnsafeMutableRawPointer.initializeMemory with negative count"
+ "_canAccessNetworkQueue"
+ "canAccessNetworkQueue"
+ "invalid Collection: less than 'count' elements in collection"
+ "invalid Collection: more than 'count' elements in collection"
- "%s - Attempting asset download - limit=%lu (minimum=%lu, existing=%lu)"
- "%s - Completed with remaining amount: %{public}ld, urgency: %{public}ld, volume: %@"
- "v32@0:8@16^^{archive_entry}24"

```
