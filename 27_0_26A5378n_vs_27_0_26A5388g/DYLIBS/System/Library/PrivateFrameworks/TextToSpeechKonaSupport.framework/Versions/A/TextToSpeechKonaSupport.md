## TextToSpeechKonaSupport

> `/System/Library/PrivateFrameworks/TextToSpeechKonaSupport.framework/Versions/A/TextToSpeechKonaSupport`

### Sections with Same Size but Changed Content

- `__TEXT.__init_offsets`
- `__TEXT.__swift5_assocty`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__swift_as_entry`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH.__data`
- `__DATA.__objc_stublist`
- `__DATA_DIRTY.__objc_data`

```diff

-678.0.0.0.0
-  __TEXT.__text: 0x11ce0
+680.0.0.0.0
+  __TEXT.__text: 0x11a3c
   __TEXT.__init_offsets: 0x4
-  __TEXT.__objc_methlist: 0x778
-  __TEXT.__const: 0x6b8
-  __TEXT.__oslogstring: 0x423
-  __TEXT.__swift5_typeref: 0x1e2
-  __TEXT.__swift5_capture: 0x98
+  __TEXT.__objc_methlist: 0x788
+  __TEXT.__const: 0x6d8
+  __TEXT.__oslogstring: 0x333
+  __TEXT.__swift5_typeref: 0x1ee
+  __TEXT.__swift5_capture: 0xe0
   __TEXT.__swift5_reflstr: 0x2a3
   __TEXT.__swift5_assocty: 0x30
   __TEXT.__constg_swiftt: 0x2e8
   __TEXT.__swift5_fieldmd: 0x1f4
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__cstring: 0x958
+  __TEXT.__cstring: 0x967
   __TEXT.__swift5_proto: 0x24
   __TEXT.__swift5_types: 0x14
   __TEXT.__swift_as_entry: 0x34
-  __TEXT.__swift_as_ret: 0x24
-  __TEXT.__swift_as_cont: 0x60
-  __TEXT.__gcc_except_tab: 0xddc
-  __TEXT.__unwind_info: 0x570
-  __TEXT.__eh_frame: 0x7d8
+  __TEXT.__swift_as_ret: 0x20
+  __TEXT.__swift_as_cont: 0x44
+  __TEXT.__gcc_except_tab: 0xcf4
+  __TEXT.__unwind_info: 0x598
+  __TEXT.__eh_frame: 0x6f8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xe0
-  __DATA_CONST.__objc_classlist: 0x40
+  __DATA_CONST.__const: 0xc0
+  __DATA_CONST.__objc_classlist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x690
-  __DATA_CONST.__objc_superrefs: 0x18
+  __DATA_CONST.__objc_selrefs: 0x668
+  __DATA_CONST.__objc_superrefs: 0x20
   __DATA_CONST.__objc_arraydata: 0xb8
   __DATA_CONST.__got: 0x200
-  __AUTH_CONST.__const: 0x3e0
+  __AUTH_CONST.__const: 0x5b8
   __AUTH_CONST.__cfstring: 0x11a0
-  __AUTH_CONST.__objc_const: 0x12a0
+  __AUTH_CONST.__objc_const: 0x1390
   __AUTH_CONST.__objc_intobj: 0x258
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH_CONST.__auth_got: 0x648
-  __AUTH.__objc_data: 0x220
+  __AUTH_CONST.__auth_got: 0x660
+  __AUTH.__objc_data: 0x270
   __AUTH.__data: 0x170
-  __DATA.__objc_ivar: 0xf8
+  __DATA.__objc_ivar: 0x104
   __DATA.__data: 0x1c8
   __DATA.__objc_stublist: 0x8
   __DATA.__bss: 0x4d0

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 388
-  Symbols:   806
-  CStrings:  191
+  Functions: 415
+  Symbols:   831
+  CStrings:  187
 
Symbols:
+ -[AXKonaSpeechEngine _applyParametersOnQueue:]
+ -[AXKonaSpeechEngine _cancelInFlightJob]
+ -[AXKonaSpeechEngine _resetEngineForVoiceOnQueue:]
+ -[AXKonaSpeechEngine _scheduleResetPreservingParams]
+ -[AXKonaSpeechEngine setWorkQueue:]
+ -[AXKonaSpeechEngine synthesizeText:bufferHandler:completion:]
+ -[AXKonaSpeechEngine workQueue]
+ -[AXKonaSynthesisJob .cxx_destruct]
+ -[AXKonaSynthesisJob bufferHandler]
+ -[AXKonaSynthesisJob cancel]
+ -[AXKonaSynthesisJob completion]
+ -[AXKonaSynthesisJob deliverCompletionWithCanceled:]
+ -[AXKonaSynthesisJob init]
+ -[AXKonaSynthesisJob isCanceled]
+ -[AXKonaSynthesisJob setBufferHandler:]
+ -[AXKonaSynthesisJob setCancelListener:]
+ -[AXKonaSynthesisJob setCompletion:]
+ GCC_except_table110
+ GCC_except_table117
+ GCC_except_table119
+ GCC_except_table120
+ GCC_except_table121
+ GCC_except_table136
+ GCC_except_table137
+ GCC_except_table142
+ GCC_except_table145
+ GCC_except_table153
+ GCC_except_table154
+ GCC_except_table157
+ GCC_except_table159
+ GCC_except_table162
+ GCC_except_table166
+ GCC_except_table171
+ GCC_except_table176
+ GCC_except_table177
+ GCC_except_table178
+ OBJC_IVAR_$_AXKonaSpeechEngine._currentJob
+ OBJC_IVAR_$_AXKonaSpeechEngine._intendedJob
+ OBJC_IVAR_$_AXKonaSpeechEngine._workQueue
+ OBJC_IVAR_$_AXKonaSynthesisJob._bufferHandler
+ OBJC_IVAR_$_AXKonaSynthesisJob._cancelListener
+ OBJC_IVAR_$_AXKonaSynthesisJob._canceled
+ OBJC_IVAR_$_AXKonaSynthesisJob._completed
+ OBJC_IVAR_$_AXKonaSynthesisJob._completion
+ OBJC_IVAR_$_AXKonaSynthesisJob._lock
+ _OBJC_CLASS_$_AXKonaSynthesisJob
+ _OBJC_METACLASS_$_AXKonaSynthesisJob
+ __54-[AXKonaSpeechEngine eciCallback:iParam:instanceData:]_block_invoke
+ __62-[AXKonaSpeechEngine synthesizeText:bufferHandler:completion:]_block_invoke
+ __Block_copy
+ __Block_release
+ __OBJC_$_INSTANCE_METHODS_AXKonaSynthesisJob
+ __OBJC_$_INSTANCE_VARIABLES_AXKonaSynthesisJob
+ __OBJC_$_PROP_LIST_AXKonaSynthesisJob
+ __OBJC_CLASS_RO_$_AXKonaSynthesisJob
+ __OBJC_METACLASS_RO_$_AXKonaSynthesisJob
+ ___31-[AXKonaSpeechEngine setVoice:]_block_invoke
+ ___36-[AXKonaSpeechEngine setParameters:]_block_invoke
+ ___52-[AXKonaSpeechEngine _scheduleResetPreservingParams]_block_invoke
+ ___62-[AXKonaSpeechEngine synthesizeText:bufferHandler:completion:]_block_invoke
+ ___62-[AXKonaSpeechEngine synthesizeText:bufferHandler:completion:]_block_invoke_2
+ ___block_descriptor_40_ea8_32bs_e5_v8?0l
+ ___block_descriptor_40_ea8_32s_e14_v16?0?<v?>8l
+ ___block_descriptor_48_ea8_32s40s_e5_v8?0l
+ ___block_descriptor_48_ea8_32s40w_e14_v16?0?<v?>8l
+ ___block_descriptor_56_ea8_32s40s48s_e5_v8?0l
+ ___copy_helper_block_ea8_32b
+ ___copy_helper_block_ea8_32s40s
+ ___copy_helper_block_ea8_32s40s48s
+ ___copy_helper_block_ea8_32s40w
+ ___destroy_helper_block_ea8_32s40s
+ ___destroy_helper_block_ea8_32s40s48s
+ ___destroy_helper_block_ea8_32s40w
+ _block_copy_helper
+ _block_descriptor
+ _block_destroy_helper
+ _dispatch_semaphore_create
+ _objc_copyWeak
+ _objc_destroyWeak
+ _objc_initWeak
+ _objc_loadWeakRetained
+ _objc_msgSend$_applyParametersOnQueue:
+ _objc_msgSend$_cancelInFlightJob
+ _objc_msgSend$_resetEngineForVoiceOnQueue:
+ _objc_msgSend$_scheduleResetPreservingParams
+ _objc_msgSend$bufferHandler
+ _objc_msgSend$cancel
+ _objc_msgSend$completion
+ _objc_msgSend$deliverCompletionWithCanceled:
+ _objc_msgSend$isCanceled
+ _objc_msgSend$setBufferHandler:
+ _objc_msgSend$setCancelListener:
+ _objc_msgSend$setCompletion:
+ _objc_msgSend$synthesizeText:bufferHandler:completion:
+ _objc_msgSend$workQueue
+ _objc_retainBlock
+ _os_unfair_lock_lock
+ _os_unfair_lock_unlock
+ _symbolic Ieg_SgIegg_
+ _symbolic IeyB_IeyBy_
+ _symbolic IeyB_SgIeyBy_
+ _symbolic So21OS_dispatch_semaphoreC
+ _symbolic _____ 12TextToSpeech15SynthesisBufferV
+ block_copy_helper
+ block_descriptor
+ block_destroy_helper
- -[AXKonaSpeechEngine _cancelSynthesis]
- -[AXKonaSpeechEngine _enqueueBuffer:]
- -[AXKonaSpeechEngine _resetEnginePreservingParams]
- -[AXKonaSpeechEngine cancelSynthesis]
- -[AXKonaSpeechEngine consumedBuffers]
- -[AXKonaSpeechEngine nextBuffer]
- -[AXKonaSpeechEngine producedBuffers]
- -[AXKonaSpeechEngine queuedBuffers]
- -[AXKonaSpeechEngine setConsumedBuffers:]
- -[AXKonaSpeechEngine setProducedBuffers:]
- -[AXKonaSpeechEngine setQueuedBuffers:]
- -[AXKonaSpeechEngine setSynthState:]
- -[AXKonaSpeechEngine setSynthesizerSyncQueue:]
- -[AXKonaSpeechEngine synthState]
- -[AXKonaSpeechEngine synthesizeText:]
- -[AXKonaSpeechEngine synthesizerSyncQueue]
- GCC_except_table125
- GCC_except_table126
- GCC_except_table127
- GCC_except_table128
- GCC_except_table129
- GCC_except_table131
- GCC_except_table132
- GCC_except_table133
- GCC_except_table134
- GCC_except_table135
- GCC_except_table140
- GCC_except_table144
- GCC_except_table147
- GCC_except_table148
- GCC_except_table150
- GCC_except_table151
- GCC_except_table152
- GCC_except_table160
- GCC_except_table163
- OBJC_IVAR_$_AXKonaSpeechEngine._bufferLock
- OBJC_IVAR_$_AXKonaSpeechEngine._consumedBuffers
- OBJC_IVAR_$_AXKonaSpeechEngine._producedBuffers
- OBJC_IVAR_$_AXKonaSpeechEngine._queuedBuffers
- OBJC_IVAR_$_AXKonaSpeechEngine._synthState
- OBJC_IVAR_$_AXKonaSpeechEngine._synthesizerSyncQueue
- _AX_PERFORM_WITH_LOCK
- _OBJC_CLASS_$_NSCondition
- __NSConcreteGlobalBlock
- ___32-[AXKonaSpeechEngine nextBuffer]_block_invoke
- ___37-[AXKonaSpeechEngine _enqueueBuffer:]_block_invoke
- ___37-[AXKonaSpeechEngine cancelSynthesis]_block_invoke
- ___37-[AXKonaSpeechEngine synthesizeText:]_block_invoke
- ___38-[AXKonaSpeechEngine _cancelSynthesis]_block_invoke
- ___block_descriptor_32_e5_v8?0l
- ___block_descriptor_48_ea8_32s40r_e5_v8?0l
- ___block_descriptor_56_ea8_32s40s48r_e5_v8?0l
- ___block_literal_global
- ___copy_helper_block_ea8_32s40s48r
- ___destroy_helper_block_ea8_32s40s48r
- ___swift__destructor
- _dispatch_sync
- _objc_msgSend$_cancelSynthesis
- _objc_msgSend$_enqueueBuffer:
- _objc_msgSend$_resetEnginePreservingParams
- _objc_msgSend$broadcast
- _objc_msgSend$cancelSynthesis
- _objc_msgSend$consumedBuffers
- _objc_msgSend$nextBuffer
- _objc_msgSend$producedBuffers
- _objc_msgSend$queuedBuffers
- _objc_msgSend$removeObjectAtIndex:
- _objc_msgSend$setQueuedBuffers:
- _objc_msgSend$setSynthState:
- _objc_msgSend$signal
- _objc_msgSend$synthState
- _objc_msgSend$synthesizeText:
- _objc_msgSend$synthesizerSyncQueue
- _objc_msgSend$wait
- _swift_errorRetain
- _swift_getErrorValue
- _swift_unknownObjectWeakDestroy
- _swift_unknownObjectWeakInit
- _swift_unknownObjectWeakLoadStrong
- _symbolic So18AXKonaSpeechEngineCSgXw
- _symbolic So18AXKonaSpeechEngineCSgXwz_Xx
CStrings:
+ "konaSpeechWorkQueue"
+ "v16@?0@?<v@?>8"
+ "\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\x82',"
- "Buffer processing completed"
- "Cancelled any previous synthesis"
- "Failed to send buffer: %s"
- "No more buffers available, synthesis complete"
- "Starting buffer processing"
- "Synthesis cancelled, stopping buffer processing"
- "konaSpeechSyncQueue"
```
