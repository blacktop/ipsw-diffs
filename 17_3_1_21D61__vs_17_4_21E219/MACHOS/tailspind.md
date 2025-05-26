## tailspind

> `/usr/libexec/tailspind`

```diff

-162.3.0.0.0
-  __TEXT.__text: 0x92d0
-  __TEXT.__auth_stubs: 0xbf0
-  __TEXT.__objc_stubs: 0x740
+176.0.0.0.0
+  __TEXT.__text: 0x9f0c
+  __TEXT.__auth_stubs: 0xc60
+  __TEXT.__objc_stubs: 0x780
   __TEXT.__const: 0x64
-  __TEXT.__cstring: 0x726
+  __TEXT.__cstring: 0x854
   __TEXT.__gcc_except_tab: 0x170
-  __TEXT.__oslogstring: 0x2442
-  __TEXT.__objc_methname: 0x536
-  __TEXT.__unwind_info: 0x178
-  __DATA_CONST.__auth_got: 0x608
-  __DATA_CONST.__got: 0x108
+  __TEXT.__oslogstring: 0x269d
+  __TEXT.__objc_methname: 0x55e
+  __TEXT.__unwind_info: 0x190
+  __DATA_CONST.__auth_got: 0x640
+  __DATA_CONST.__got: 0x110
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x388
-  __DATA_CONST.__cfstring: 0x320
+  __DATA_CONST.__const: 0x3b0
+  __DATA_CONST.__cfstring: 0x440
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__objc_classrefs: 0xa0
   __DATA_CONST.__objc_intobj: 0x18
-  __DATA.__objc_selrefs: 0x1d0
-  __DATA.__objc_classrefs: 0xa0
-  __DATA.__data: 0x2188
+  __DATA.__objc_selrefs: 0x1e0
+  __DATA.__data: 0x21b8
   __DATA.__crash_info: 0x40
   __DATA.__bss: 0x478
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libdscsym.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
-  Functions: 168
-  Symbols:   251
-  CStrings:  283
+  Functions: 176
+  Symbols:   259
+  CStrings:  305
 
Symbols:
+ _TSPDumpOptions_CollectTrials
+ __os_signpost_emit_with_name_impl
+ _kperf_kdebug_filter_add_debugid
+ _objc_retain_x28
+ _os_signpost_enabled
+ _tailspin_sampling_option_get
+ _tailspin_sampling_options_get_default
+ _xpc_connection_get_context
CStrings:
+ "%{public}s requested to change tailspin sampling modifers to 0x%x, overriding previous request from %{public}s to change tailspin sampling modifiers to 0x%x"
+ "%{public}s requested to change tailspin sampling modifiers to %x from default %x"
+ "Bad file descriptor %d"
+ "Can't parse client dump output options"
+ "DumpRequest"
+ "FAILED due to reason: %{public}@"
+ "Failed to deserialize dump options due to %@"
+ "File descriptor is not read-write %d"
+ "New connection for client %{public}s [%d]"
+ "NewClientConnection"
+ "Request from %{public}s [%d]"
+ "Resulting trace would be shorter than desired duration"
+ "Reverted previous request by %{public}s to change tailspin sampling options to %x to default %x"
+ "SUCCEEDED"
+ "SaveResultEnum"
+ "Successfully got oldest kdebug time (%llu, %.2fs ago)"
+ "Unable to get oldest kdebug time: %{errno}d"
+ "Unable to save tailspin for %{public}s [%d]: Can't parse client dump output options"
+ "Unable to save tailspin for %{public}s [%d]: Failed to deserialize dump options due to %s"
+ "Unable to save tailspin for %{public}s [%d]: bad file descriptor %d"
+ "Unable to save tailspin for %{public}s [%d]: file descriptor is not read-write %d"
+ "Unable to save tailspin for %{public}s [%d]: tailspin currently disabled"
+ "com.apple.tailspin.saveresult.v1"
+ "com.apple.tailspind.saveresult.v1"
+ "initWithFormat:"
+ "numberWithUnsignedInt:"
+ "tailspin is disabled"
+ "v12@?0i8"
- "Unable to save tailspin for %{public}s: Can't parse client dump output options"
- "Unable to save tailspin for %{public}s: Failed to deserialize dump options due to %s"
- "Unable to save tailspin for %{public}s: bad file descriptor %d"
- "Unable to save tailspin for %{public}s: file descriptor is not read-write %d"
- "Unable to save tailspin for %{public}s: tailspin currently disabled"
- "v12@?0B8"

```
