## LiveTranscription

> `/System/Library/PrivateFrameworks/LiveTranscription.framework/LiveTranscription`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_typeref`
- `__TEXT.__cstring`
- `__TEXT.__swift5_assocty`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__swift5_capture`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH.__objc_data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-584.0.0.0.0
-  __TEXT.__text: 0x30a5c
-  __TEXT.__objc_methlist: 0x16ec
-  __TEXT.__const: 0x978
+587.0.0.0.0
+  __TEXT.__text: 0x31b5c
+  __TEXT.__objc_methlist: 0x171c
+  __TEXT.__const: 0x990
   __TEXT.__dlopen_cstrs: 0x6a
   __TEXT.__swift5_typeref: 0x418
   __TEXT.__cstring: 0x982

   __TEXT.__constg_swiftt: 0x528
   __TEXT.__swift5_builtin: 0x50
   __TEXT.__swift5_fieldmd: 0x244
-  __TEXT.__oslogstring: 0x2a0e
+  __TEXT.__oslogstring: 0x2bbd
   __TEXT.__swift5_proto: 0x30
   __TEXT.__swift5_types: 0x2c
   __TEXT.__swift5_capture: 0x378
   __TEXT.__swift_as_entry: 0x70
   __TEXT.__swift_as_ret: 0x78
   __TEXT.__swift_as_cont: 0x78
-  __TEXT.__gcc_except_tab: 0x88
-  __TEXT.__unwind_info: 0xa50
+  __TEXT.__gcc_except_tab: 0xf4
+  __TEXT.__unwind_info: 0xa70
   __TEXT.__eh_frame: 0xb80
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x610
+  __DATA_CONST.__const: 0x660
   __DATA_CONST.__objc_classlist: 0xb0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xf00
+  __DATA_CONST.__objc_selrefs: 0xf20
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x68
-  __DATA_CONST.__got: 0x3d8
-  __AUTH_CONST.__const: 0xb50
+  __DATA_CONST.__got: 0x3e0
+  __AUTH_CONST.__const: 0xbb0
   __AUTH_CONST.__cfstring: 0x760
-  __AUTH_CONST.__objc_const: 0x2ae0
+  __AUTH_CONST.__objc_const: 0x2b10
   __AUTH_CONST.__objc_doubleobj: 0x20
-  __AUTH_CONST.__auth_got: 0x8f8
+  __AUTH_CONST.__auth_got: 0x908
   __AUTH.__objc_data: 0x48
-  __DATA.__objc_ivar: 0x18c
+  __DATA.__objc_ivar: 0x190
   __DATA.__data: 0x688
   __DATA.__bss: 0x6c8
   __DATA.__common: 0x18

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1000
-  Symbols:   1513
-  CStrings:  295
+  Functions: 1008
+  Symbols:   1530
+  CStrings:  301
 
Symbols:
+ -[AXLTAudioOutManager _removeRunningStateListenerForTranscriber:]
+ -[AXLTAudioOutManager handleAudioQueueStoppedForTranscriber:]
+ -[AXLTAudioOutManager lastTapRebuildDates]
+ -[AXLTAudioOutManager setLastTapRebuildDates:]
+ GCC_except_table339
+ GCC_except_table349
+ _AVSystemController_CallIsActiveDidChangeNotification
+ _AudioQueueAddPropertyListener
+ _AudioQueueRemovePropertyListener
+ _OBJC_IVAR_$_AXLTAudioOutManager._lastTapRebuildDates
+ ___61-[AXLTAudioOutManager handleAudioQueueStoppedForTranscriber:]_block_invoke
+ ___61-[AXLTAudioOutManager handleAudioQueueStoppedForTranscriber:]_block_invoke_2
+ ___block_descriptor_60_e8_32s40s48r_e5_v8?0lr48l8s32l8s40l8
+ ___block_descriptor_68_e8_32s40s48s56s_e5_v8?0ls32l8s40l8s48l8s56l8
+ _handleAudioQueueRunningStateChanged
+ _objc_msgSend$_removeRunningStateListenerForTranscriber:
+ _objc_msgSend$handleAudioQueueStoppedForTranscriber:
+ _objc_msgSend$lastTapRebuildDates
- GCC_except_table342
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
