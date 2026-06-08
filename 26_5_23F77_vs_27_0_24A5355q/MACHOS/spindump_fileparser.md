## spindump_fileparser

> `/usr/libexec/spindump_fileparser`

```diff

-419.10.0.0.0
-  __TEXT.__text: 0xc5c58
-  __TEXT.__auth_stubs: 0x12d0
-  __TEXT.__objc_stubs: 0x43a0
+435.0.0.0.0
+  __TEXT.__text: 0xc0878
+  __TEXT.__auth_stubs: 0x1340
+  __TEXT.__objc_stubs: 0x4420
   __TEXT.__objc_methlist: 0x9f4
   __TEXT.__const: 0x250
-  __TEXT.__cstring: 0x15718
-  __TEXT.__oslogstring: 0x2794e
-  __TEXT.__objc_classname: 0x105
-  __TEXT.__gcc_except_tab: 0x33b4
-  __TEXT.__objc_methname: 0x4322
+  __TEXT.__cstring: 0x15cbf
+  __TEXT.__oslogstring: 0x284db
+  __TEXT.__gcc_except_tab: 0x3040
+  __TEXT.__objc_classname: 0xe2
+  __TEXT.__objc_methname: 0x4370
   __TEXT.__objc_methtype: 0x530
-  __TEXT.__unwind_info: 0xe00
-  __DATA_CONST.__auth_got: 0x978
-  __DATA_CONST.__got: 0x220
-  __DATA_CONST.__auth_ptr: 0x20
-  __DATA_CONST.__const: 0x1530
-  __DATA_CONST.__cfstring: 0x9fa0
+  __TEXT.__unwind_info: 0xce0
+  __DATA_CONST.__const: 0x1570
+  __DATA_CONST.__cfstring: 0xa200
   __DATA_CONST.__objc_classlist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x38
   __DATA_CONST.__objc_intobj: 0xf0
   __DATA_CONST.__objc_arraydata: 0x48
   __DATA_CONST.__objc_arrayobj: 0x48
+  __DATA_CONST.__auth_got: 0x9b0
+  __DATA_CONST.__got: 0x220
+  __DATA_CONST.__auth_ptr: 0x20
   __DATA.__objc_const: 0x1d68
-  __DATA.__objc_selrefs: 0x1200
+  __DATA.__objc_selrefs: 0x1220
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
-  UUID: 89B79130-4B78-33AE-B98C-43E59D6B9D90
-  Functions: 1813
-  Symbols:   380
-  CStrings:  6051
+  UUID: 16290357-52C0-305E-8B9C-8F41629069D4
+  Functions: 1820
+  Symbols:   387
+  CStrings:  6131
 
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
+ "Invalid process %s"
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
+ "Unable to format: Invalid process %s"
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
+ "lowercaseString"
+ "num_ipc_messages_queued"
+ "num_ipc_messages_queued_limit"
+ "setPidsToPrint:"
+ "setProcessNamesToPrint:"
+ "setUniquePidsToPrint:"
+ "v20@?0r*8B16"

```
