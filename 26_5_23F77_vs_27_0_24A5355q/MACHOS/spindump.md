## spindump

> `/usr/sbin/spindump`

```diff

-419.10.0.0.0
-  __TEXT.__text: 0xbcc70
-  __TEXT.__auth_stubs: 0x1270
+435.0.0.0.0
+  __TEXT.__text: 0xb7584
+  __TEXT.__auth_stubs: 0x12e0
   __TEXT.__objc_stubs: 0x4180
   __TEXT.__objc_methlist: 0x9f4
   __TEXT.__const: 0x240
-  __TEXT.__cstring: 0x14b90
-  __TEXT.__oslogstring: 0x25e2a
-  __TEXT.__objc_classname: 0x105
-  __TEXT.__gcc_except_tab: 0x32b4
+  __TEXT.__cstring: 0x15117
+  __TEXT.__oslogstring: 0x2697f
+  __TEXT.__gcc_except_tab: 0x2f20
+  __TEXT.__objc_classname: 0xe2
   __TEXT.__objc_methname: 0x4257
   __TEXT.__objc_methtype: 0x530
-  __TEXT.__unwind_info: 0xdf0
-  __DATA_CONST.__auth_got: 0x948
-  __DATA_CONST.__got: 0x218
-  __DATA_CONST.__auth_ptr: 0x18
-  __DATA_CONST.__const: 0x1508
-  __DATA_CONST.__cfstring: 0x99a0
+  __TEXT.__unwind_info: 0xcc8
+  __DATA_CONST.__const: 0x1520
+  __DATA_CONST.__cfstring: 0x9be0
   __DATA_CONST.__objc_classlist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x38
   __DATA_CONST.__objc_intobj: 0xa8
   __DATA_CONST.__objc_arraydata: 0x18
   __DATA_CONST.__objc_arrayobj: 0x18
+  __DATA_CONST.__auth_got: 0x980
+  __DATA_CONST.__got: 0x218
+  __DATA_CONST.__auth_ptr: 0x18
   __DATA.__objc_const: 0x1d68
   __DATA.__objc_selrefs: 0x11b8
   __DATA.__objc_ivar: 0x214
   __DATA.__objc_data: 0x410
   __DATA.__data: 0x20
   __DATA.__crash_info: 0x148
-  __DATA.__bss: 0x800
+  __DATA.__bss: 0x808
   __DATA.__common: 0x60
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/libsystemstats.dylib
   - /usr/lib/libtailspin.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 4782B0C2-D93C-375E-8EA1-4A6B015210FC
-  Functions: 1804
-  Symbols:   373
-  CStrings:  5863
+  UUID: EE45C441-959D-33F8-B864-9B59D3DD52F9
+  Functions: 1808
+  Symbols:   380
+  CStrings:  5934
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x10
+ _objc_retain_x11
+ _objc_retain_x5
+ _pthread_setname_np
CStrings:
+ "%s [%d]: ipc messages queued exhaustion: %llu ipc messages queued with flags %#llx"
+ "%s [%d]: ipc messages queued exhaustion: deallocating fatal port, allowing process to exit due to fatal resource exhaustion"
+ "%s [%d]: ipc messages queued exhaustion: fatal, %llu ipc messages queued with flags %#llx"
+ "%s [%d]: ipc messages queued exhaustion: not monitoring due to conditions %#llx"
+ "%s [%d]: ipc messages queued exhaustion: not monitoring due to suppression cookie file"
+ "%s is not a valid type"
+ "%{public}s [%d]: ipc messages queued exhaustion: %llu ipc messages queued with flags %#llx"
+ "%{public}s [%d]: ipc messages queued exhaustion: deallocating fatal port, allowing process to exit due to fatal resource exhaustion"
+ "%{public}s [%d]: ipc messages queued exhaustion: fatal, %llu ipc messages queued with flags %#llx"
+ "%{public}s [%d]: ipc messages queued exhaustion: not monitoring due to conditions %#llx"
+ "%{public}s [%d]: ipc messages queued exhaustion: not monitoring due to suppression cookie file"
+ "BundleIdOverride=%{public, signpost.description:attribute}@ cid=%{public,name=cid}llu pid=%{public,name=pid}u numIPCMessagesQueued=%{public,name=numIPCMessagesQueued}llu numIPCMessagesQueuedLimit=%{public,name=numIPCMessagesQueuedLimit}llu conditionsPreventingSubmission=%{public,name=conditionsPreventingSubmission}#llx otherConditions=%{public,name=otherConditions}#llx enableTelemetry=YES "
+ "Error reporting ipc messages queued exhaustion: no num ipc messages queued provided"
+ "Error reporting ipc messages queued exhaustion: no pid provided"
+ "ExhaustionFatal_IPCMessagesQueued"
+ "Exhaustion_IPCMessagesQueued"
+ "IPCMessagesQueuedExhaustion"
+ "NumIPCMessagesQueued"
+ "NumIPCMessagesQueuedLimit"
+ "Stackshot sampling"
+ "Unable to format: %s [%d]: ipc messages queued exhaustion: %llu ipc messages queued with flags %#llx"
+ "Unable to format: %s [%d]: ipc messages queued exhaustion: deallocating fatal port, allowing process to exit due to fatal resource exhaustion"
+ "Unable to format: %s [%d]: ipc messages queued exhaustion: fatal, %llu ipc messages queued with flags %#llx"
+ "Unable to format: %s [%d]: ipc messages queued exhaustion: not monitoring due to conditions %#llx"
+ "Unable to format: %s [%d]: ipc messages queued exhaustion: not monitoring due to suppression cookie file"
+ "Unable to format: %s is not a valid type"
+ "Unable to format: Error reporting ipc messages queued exhaustion: no num ipc messages queued provided"
+ "Unable to format: Error reporting ipc messages queued exhaustion: no pid provided"
+ "Unable to format: WR: %@: Using provided incident UUID %@"
+ "Unable to format: ipc messages queued exhaustion: %llu ipc messages queued with flags %#llx"
+ "Unable to format: ipc messages queued exhaustion: deallocating fatal port, allowing process to exit due to fatal resource exhaustion"
+ "Unable to format: ipc messages queued exhaustion: fatal, %llu ipc messages queued with flags %#llx"
+ "Unable to format: ipc messages queued exhaustion: not monitoring due to conditions %#llx"
+ "Unable to format: ipc messages queued exhaustion: not monitoring due to suppression cookie file"
+ "WR: %@: Using provided incident UUID %@"
+ "com.apple.spindump.ipcmessagesqueuedexhaustion"
+ "ipc messages queued exhaustion"
+ "ipc messages queued exhaustion: %llu ipc messages queued with flags %#llx"
+ "ipc messages queued exhaustion: deallocating fatal port, allowing process to exit due to fatal resource exhaustion"
+ "ipc messages queued exhaustion: fatal, %llu ipc messages queued with flags %#llx"
+ "ipc messages queued exhaustion: not monitoring due to conditions %#llx"
+ "ipc messages queued exhaustion: not monitoring due to suppression cookie file"
+ "num_ipc_messages_queued"
+ "num_ipc_messages_queued_limit"

```
