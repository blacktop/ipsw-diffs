## libramrod.dylib

> `/usr/lib/libramrod.dylib`

```diff

-3476.82.1.0.0
-  __TEXT.__text: 0xdce98
-  __TEXT.__auth_stubs: 0x28f0
+3476.100.140.0.0
+  __TEXT.__text: 0xdbe8c
+  __TEXT.__auth_stubs: 0x2920
   __TEXT.__objc_methlist: 0x117c
-  __TEXT.__cstring: 0x28a97
-  __TEXT.__const: 0x94948
-  __TEXT.__gcc_except_tab: 0xbc4
+  __TEXT.__cstring: 0x28fd1
+  __TEXT.__const: 0x94ec8
+  __TEXT.__gcc_except_tab: 0xba4
   __TEXT.__oslogstring: 0xab4
-  __TEXT.__unwind_info: 0x1d28
-  __TEXT.__eh_frame: 0x3c0
+  __TEXT.__unwind_info: 0x1d98
+  __TEXT.__eh_frame: 0x370
   __TEXT.__objc_classname: 0x195
   __TEXT.__objc_methname: 0x29a2
   __TEXT.__objc_methtype: 0xb65
   __TEXT.__objc_stubs: 0x28c0
   __DATA_CONST.__got: 0x2d0
-  __DATA_CONST.__const: 0x1f80
+  __DATA_CONST.__const: 0x1f98
   __DATA_CONST.__objc_classlist: 0x90
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0xcb8
-  __AUTH_CONST.__auth_got: 0x1490
+  __AUTH_CONST.__auth_got: 0x14a8
   __AUTH_CONST.__const: 0x2020
-  __AUTH_CONST.__cfstring: 0xba60
+  __AUTH_CONST.__cfstring: 0xbaa0
   __AUTH_CONST.__objc_const: 0x1ad0
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH.__objc_data: 0x5a0

   __DATA.__objc_classrefs: 0x128
   __DATA.__objc_superrefs: 0x80
   __DATA.__objc_ivar: 0x138
-  __DATA.__data: 0x2198
-  __DATA.__bss: 0x868
+  __DATA.__data: 0x2598
+  __DATA.__bss: 0x878
   __DATA.__common: 0x38
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libutil.dylib
   - /usr/lib/libz.1.dylib
   - /usr/lib/updaters/libAppleTypeCRetimerUpdater.dylib
-  UUID: C2F5E6A0-43BB-3FFA-A4C6-AC830FE0CDD0
-  Functions: 2662
-  Symbols:   1821
-  CStrings:  7456
+  UUID: FFED8012-8225-30E9-B8CD-6865C5BD8159
+  Functions: 2757
+  Symbols:   1829
+  CStrings:  7471
 
Symbols:
+ _IOMobileFramebufferGetServiceObject
+ _IOMobileFramebufferSwapSetBrightness
+ _MGGetBoolAnswer
+ _dispatch_async_and_wait
+ _kImg4TagStr_eurm
+ _ramrod_display_power_cycle
+ _ramrod_display_set_brightness_nits
+ _ramrod_register_for_button_event_with_first_event_handler
+ _ramrod_split_data_volume_with_migrator_status
- _dispatch_retain
CStrings:
+ "%s: Failed to set brightness property: %d\n"
+ "%s: No current display\n"
+ "%s: No framebuffer service.\n"
+ "%s: SwapSetBrightness failed %d\n"
+ "%s: nits value too large\n"
+ "%s: nits=%d, iomfb_swap_set_brightness_supported=%d\n"
+ "%s: powered on after %d polls\n"
+ "%s: timed out waiting for display power on\n"
+ "-A"
+ "/Library/Caches/com.apple.xbs/05BC2D32-1B21-4498-8369-DABC4A1C2388/TemporaryDirectory.TPxQAa/Sources/Pearl_Kernel/PearlFactoryLib/PearlFactoryLib.m"
+ "/Library/Caches/com.apple.xbs/B65DF3A4-AF11-4BE0-AF07-2DC2EF4DDBAA/TemporaryDirectory.dwsI1I/Sources/ParallelCompression/Common/IOBasicStreams.c"
+ "/Library/Caches/com.apple.xbs/B65DF3A4-AF11-4BE0-AF07-2DC2EF4DDBAA/TemporaryDirectory.dwsI1I/Sources/ParallelCompression/Common/IOBuffers.c"
+ "/Library/Caches/com.apple.xbs/B65DF3A4-AF11-4BE0-AF07-2DC2EF4DDBAA/TemporaryDirectory.dwsI1I/Sources/ParallelCompression/Common/IOCompressedStreams.c"
+ "/Library/Caches/com.apple.xbs/B65DF3A4-AF11-4BE0-AF07-2DC2EF4DDBAA/TemporaryDirectory.dwsI1I/Sources/ParallelCompression/Common/ParallelCompressionAFSCStream.c"
+ "/Library/Caches/com.apple.xbs/B65DF3A4-AF11-4BE0-AF07-2DC2EF4DDBAA/TemporaryDirectory.dwsI1I/Sources/ParallelCompression/Common/SharedArray.h"
+ "/Library/Caches/com.apple.xbs/B65DF3A4-AF11-4BE0-AF07-2DC2EF4DDBAA/TemporaryDirectory.dwsI1I/Sources/ParallelCompression/Common/SharedBuffer.c"
+ "/Library/Caches/com.apple.xbs/B65DF3A4-AF11-4BE0-AF07-2DC2EF4DDBAA/TemporaryDirectory.dwsI1I/Sources/ParallelCompression/Common/ThreadPipeline.c"
+ "/Library/Caches/com.apple.xbs/B65DF3A4-AF11-4BE0-AF07-2DC2EF4DDBAA/TemporaryDirectory.dwsI1I/Sources/ParallelCompression/Common/Threads.c"
+ "/Library/Caches/com.apple.xbs/B65DF3A4-AF11-4BE0-AF07-2DC2EF4DDBAA/TemporaryDirectory.dwsI1I/Sources/ParallelCompression/Common/Utils.c"
+ "/Library/Caches/com.apple.xbs/B65DF3A4-AF11-4BE0-AF07-2DC2EF4DDBAA/TemporaryDirectory.dwsI1I/Sources/ParallelCompression/ParallelArchive/../ParallelCompression/../Common/SharedArray.h"
+ "/Library/Caches/com.apple.xbs/B65DF3A4-AF11-4BE0-AF07-2DC2EF4DDBAA/TemporaryDirectory.dwsI1I/Sources/ParallelCompression/ParallelArchive/Extract.c"
+ "/Library/Caches/com.apple.xbs/B65DF3A4-AF11-4BE0-AF07-2DC2EF4DDBAA/TemporaryDirectory.dwsI1I/Sources/ParallelCompression/ParallelArchive/Read.c"
+ "/Library/Caches/com.apple.xbs/B65DF3A4-AF11-4BE0-AF07-2DC2EF4DDBAA/TemporaryDirectory.dwsI1I/Sources/ParallelCompression/ParallelArchive/YAACommon.c"
+ "/Library/Caches/com.apple.xbs/B65DF3A4-AF11-4BE0-AF07-2DC2EF4DDBAA/TemporaryDirectory.dwsI1I/Sources/ParallelCompression/ParallelCompression/Filter.c"
+ "DeviceSupportsFrameSynchronousBrightness"
+ "Display power off failed: %d\n"
+ "Display power on failed: %d\n"
+ "IOMFBBrightnessLevel"
+ "concatExtractPathEx"
+ "display_update"
+ "mammoth"
+ "power cycling display %s\n"
+ "ramrod_clear_updating_text_block_invoke"
+ "ramrod_display_power_cycle"
+ "ramrod_display_set_brightness_nits"
+ "ramrod_set_updating_text_block_invoke"
+ "ramrod_split_data_volume_with_migrator_status"
+ "skipping display port power on since this is a VM\n"
- "\nUNIT TEST(%s) : %s SUCCESS (expected failure [exit status])\n"
- "/Library/Caches/com.apple.xbs/Sources/ParallelCompression/Common/IOBasicStreams.c"
- "/Library/Caches/com.apple.xbs/Sources/ParallelCompression/Common/IOBuffers.c"
- "/Library/Caches/com.apple.xbs/Sources/ParallelCompression/Common/IOCompressedStreams.c"
- "/Library/Caches/com.apple.xbs/Sources/ParallelCompression/Common/ParallelCompressionAFSCStream.c"
- "/Library/Caches/com.apple.xbs/Sources/ParallelCompression/Common/SharedArray.h"
- "/Library/Caches/com.apple.xbs/Sources/ParallelCompression/Common/SharedBuffer.c"
- "/Library/Caches/com.apple.xbs/Sources/ParallelCompression/Common/ThreadPipeline.c"
- "/Library/Caches/com.apple.xbs/Sources/ParallelCompression/Common/Threads.c"
- "/Library/Caches/com.apple.xbs/Sources/ParallelCompression/Common/Utils.c"
- "/Library/Caches/com.apple.xbs/Sources/ParallelCompression/ParallelArchive/../ParallelCompression/../Common/SharedArray.h"
- "/Library/Caches/com.apple.xbs/Sources/ParallelCompression/ParallelArchive/Extract.c"
- "/Library/Caches/com.apple.xbs/Sources/ParallelCompression/ParallelArchive/Read.c"
- "/Library/Caches/com.apple.xbs/Sources/ParallelCompression/ParallelArchive/YAACommon.c"
- "/Library/Caches/com.apple.xbs/Sources/ParallelCompression/ParallelCompression/Filter.c"
- "/Library/Caches/com.apple.xbs/Sources/Pearl_Kernel/PearlFactoryLib/PearlFactoryLib.m"
- "Invalid block size in read"
- "can't load nil pointer with NVRAM value\n"
- "checkpoint_nvram_store_set_string"
- "concatExtractPath"
- "dest == NULL"
- "outData is NULL.\n"
- "ramrod_clear_updating_text_block_invoke_2"
- "ramrod_set_updating_text_block_invoke_2"
- "ramrod_split_data_volume"

```
