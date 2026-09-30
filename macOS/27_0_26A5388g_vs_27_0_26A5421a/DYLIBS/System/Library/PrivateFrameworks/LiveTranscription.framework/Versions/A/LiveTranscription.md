## LiveTranscription

> `/System/Library/PrivateFrameworks/LiveTranscription.framework/Versions/A/LiveTranscription`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`

```diff

-584.0.0.0.0
-  __TEXT.__text: 0x310e4
-  __TEXT.__objc_methlist: 0x16a4
-  __TEXT.__const: 0x968
+587.0.0.0.0
+  __TEXT.__text: 0x32318
+  __TEXT.__objc_methlist: 0x16d4
+  __TEXT.__const: 0x980
   __TEXT.__dlopen_cstrs: 0x6a
   __TEXT.__swift5_typeref: 0x454
   __TEXT.__cstring: 0x8cc

   __TEXT.__constg_swiftt: 0x528
   __TEXT.__swift5_builtin: 0x50
   __TEXT.__swift5_fieldmd: 0x244
-  __TEXT.__oslogstring: 0x2478
+  __TEXT.__oslogstring: 0x2627
   __TEXT.__swift5_proto: 0x30
   __TEXT.__swift5_types: 0x2c
   __TEXT.__swift5_capture: 0x378
   __TEXT.__swift_as_entry: 0x70
   __TEXT.__swift_as_ret: 0x78
   __TEXT.__swift_as_cont: 0x78
-  __TEXT.__gcc_except_tab: 0x8c
-  __TEXT.__unwind_info: 0xa58
+  __TEXT.__gcc_except_tab: 0xf8
+  __TEXT.__unwind_info: 0xa78
   __TEXT.__eh_frame: 0xb80
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xe78
+  __DATA_CONST.__objc_selrefs: 0xe98
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x68
   __DATA_CONST.__got: 0x3a0
-  __AUTH_CONST.__const: 0xf10
+  __AUTH_CONST.__const: 0xfd0
   __AUTH_CONST.__cfstring: 0x6a0
-  __AUTH_CONST.__objc_const: 0x2ab0
+  __AUTH_CONST.__objc_const: 0x2ae0
   __AUTH_CONST.__objc_doubleobj: 0x20
-  __AUTH_CONST.__auth_got: 0x788
+  __AUTH_CONST.__auth_got: 0x798
   __AUTH.__objc_data: 0x48
-  __DATA.__objc_ivar: 0x188
+  __DATA.__objc_ivar: 0x18c
   __DATA.__data: 0x6b8
   __DATA.__bss: 0x6c8
   __DATA.__common: 0x18

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1004
-  Symbols:   1436
-  CStrings:  263
+  Functions: 1014
+  Symbols:   1454
+  CStrings:  269
 
Symbols:
+ -[AXLTAudioOutManager _removeRunningStateListenerForTranscriber:]
+ -[AXLTAudioOutManager handleAudioQueueStoppedForTranscriber:]
+ -[AXLTAudioOutManager lastTapRebuildDates]
+ -[AXLTAudioOutManager setLastTapRebuildDates:]
+ GCC_except_table356
+ GCC_except_table368
+ OBJC_IVAR_$_AXLTAudioOutManager._lastTapRebuildDates
+ _AudioQueueAddPropertyListener
+ _AudioQueueRemovePropertyListener
+ ___61-[AXLTAudioOutManager handleAudioQueueStoppedForTranscriber:]_block_invoke
+ ___61-[AXLTAudioOutManager handleAudioQueueStoppedForTranscriber:]_block_invoke_2
+ ___block_descriptor_60_e8_32s40s48r_e5_v8?0l
+ ___block_descriptor_68_e8_32s40s48s56s_e5_v8?0l
+ ___copy_helper_block_e8_32s40s48r
+ ___destroy_helper_block_e8_32s40s48r
+ _handleAudioQueueRunningStateChanged
+ _objc_msgSend$_removeRunningStateListenerForTranscriber:
+ _objc_msgSend$handleAudioQueueStoppedForTranscriber:
+ _objc_msgSend$lastTapRebuildDates
- GCC_except_table359
CStrings:
+ "5"
+ "AudioManager: Audio queue stopped again for pid %d %.1fs after rebuild, not retrying"
+ "AudioManager: Audio queue stopped unexpectedly for app: %@, pid: %d, rebuilding tap"
+ "AudioManager: Failed to add running-state listener for pid %@: %d"
+ "AudioManager: Failed to rebuild tap for app: %@, pid: %d, error: %@"
+ "TranscriberV2: %s %s: %s"
+ "TranscriberV2: found default is %s locale with removed region from supported locales: %s"
+ "TranscriberV2: removed region from %s locale identifier: %s"
- "4"
- "TranscriberV2: found %s locale identifier with no region: %s"
```
