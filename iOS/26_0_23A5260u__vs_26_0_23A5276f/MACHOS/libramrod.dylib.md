## libramrod.dylib

> `/usr/lib/libramrod.dylib`

```diff

-3476.0.6.0.1
-  __TEXT.__text: 0xd7b64
-  __TEXT.__auth_stubs: 0x2800
-  __TEXT.__objc_methlist: 0x106c
-  __TEXT.__cstring: 0x28348
-  __TEXT.__const: 0x94860
-  __TEXT.__gcc_except_tab: 0xb60
+3476.0.29.0.0
+  __TEXT.__text: 0xd8ec0
+  __TEXT.__auth_stubs: 0x2820
+  __TEXT.__objc_methlist: 0x1164
+  __TEXT.__cstring: 0x2857f
+  __TEXT.__const: 0x94960
+  __TEXT.__gcc_except_tab: 0xbb4
   __TEXT.__oslogstring: 0x9e5
-  __TEXT.__unwind_info: 0x1c10
+  __TEXT.__unwind_info: 0x1c70
   __TEXT.__eh_frame: 0x3c0
-  __TEXT.__objc_classname: 0x17d
-  __TEXT.__objc_methname: 0x272d
-  __TEXT.__objc_methtype: 0xb47
-  __TEXT.__objc_stubs: 0x2720
+  __TEXT.__objc_classname: 0x195
+  __TEXT.__objc_methname: 0x28ee
+  __TEXT.__objc_methtype: 0xb70
+  __TEXT.__objc_stubs: 0x2820
   __DATA_CONST.__got: 0x2c8
-  __DATA_CONST.__const: 0x1f78
-  __DATA_CONST.__objc_classlist: 0x88
+  __DATA_CONST.__const: 0x1f80
+  __DATA_CONST.__objc_classlist: 0x90
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xc10
-  __AUTH_CONST.__auth_got: 0x1418
+  __DATA_CONST.__objc_selrefs: 0xc88
+  __AUTH_CONST.__auth_got: 0x1428
   __AUTH_CONST.__const: 0x1fd0
-  __AUTH_CONST.__cfstring: 0xb420
-  __AUTH_CONST.__objc_const: 0x18f0
+  __AUTH_CONST.__cfstring: 0xb4c0
+  __AUTH_CONST.__objc_const: 0x1aa0
   __AUTH_CONST.__objc_intobj: 0x30
-  __AUTH.__objc_data: 0x550
+  __AUTH.__objc_data: 0x5a0
   __AUTH.__data: 0x2b8
-  __DATA.__objc_classrefs: 0x118
-  __DATA.__objc_superrefs: 0x78
-  __DATA.__objc_ivar: 0x11c
+  __DATA.__objc_classrefs: 0x128
+  __DATA.__objc_superrefs: 0x80
+  __DATA.__objc_ivar: 0x134
   __DATA.__data: 0x2198
   __DATA.__bss: 0x828
   __DATA.__common: 0x38

   - /usr/lib/libpartition2_dynamic.dylib
   - /usr/lib/libutil.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 9D3E096C-839F-303B-B6AF-779B951AE1EF
-  Functions: 2549
-  Symbols:   1776
-  CStrings:  7274
+  UUID: 803E8E6C-B2B4-3E37-8A8A-62FC774FA6AF
+  Functions: 2585
+  Symbols:   1789
+  CStrings:  7327
 
Symbols:
+ _OBJC_CLASS_$_NSOutputStream
+ _OBJC_CLASS_$_NSPropertyListSerialization
+ _OBJC_METACLASS_$_NSOutputStream
+ _checkpoint_closure_context_set_encountered_async_error
+ _checkpoint_error_copy_canceled_error
+ _kCheckpointEngineErrorDomain
+ _objc_sync_enter
+ _objc_sync_exit
+ _ramrod_clear_apt_carvout
+ _ramrod_message_plist_create
+ _ramrod_message_plist_send
+ _ramrod_recv_bytes
+ _ramrod_send_bytes
CStrings:
+ "@32@0:8@16^@24"
+ "AppleProcessorTraceNub"
+ "CheckpointEngineErrorDomain"
+ "Couldn't read a kCFNumberIntType out of the feature flags"
+ "Device had no AppleProcessorTraceNub entry"
+ "Device had no DeviceCapabilities dictionary?"
+ "DeviceCapabilities"
+ "Entering %s\n"
+ "Feature flags (%d) & 4 == 4. Clearing `apt-carveout-size-mb`"
+ "Feature flags were NULL. No need to clear apt carvout"
+ "FeatureFlags"
+ "RamrodOSMessagePlist"
+ "T@\"NSArray\",R,C,V_chunks"
+ "TB,V_isCanceled"
+ "TQ,R,V_length"
+ "T^v,N,V_awaitDescription"
+ "T^v,N,V_stepDescription"
+ "_awaitDescription"
+ "_chunks"
+ "_isCanceled"
+ "_length"
+ "_stepDescription"
+ "_streamError"
+ "apt-carveout-size-mb"
+ "awaitDescription"
+ "cancel"
+ "chassis->lastUniqueEngineID < INT_MAX"
+ "checkpoint_chassis_set_global_async_error"
+ "checkpoint_engine_free_no_lock"
+ "checkpoint_engine_set_async_error"
+ "chip-epoch"
+ "chunks"
+ "failingStep"
+ "hasSpaceAvailable"
+ "i20@0:8i16"
+ "initWithPropertyList:error:"
+ "isCanceled"
+ "q32@0:8r*16Q24"
+ "ramrod_checkpoint.c"
+ "ramrod_clear_apt_carvout"
+ "removeAllObjects"
+ "sendToSocket:"
+ "setAwaitDescription:"
+ "setIsCanceled:"
+ "setStepDescription:"
+ "sock %3d: CFPropertyListCreateData: %s"
+ "stepDescription"
+ "streamError"
+ "write:maxLength:"
+ "writePropertyList:toStream:format:options:error:"
- "checkpoint_engine_free"
- "sock %3d: CFPropertyListCreateData: %s\n"

```
