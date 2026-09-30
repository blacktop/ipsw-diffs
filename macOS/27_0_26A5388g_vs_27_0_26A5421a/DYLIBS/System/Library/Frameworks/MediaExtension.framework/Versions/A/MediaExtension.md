## MediaExtension

> `/System/Library/Frameworks/MediaExtension.framework/Versions/A/MediaExtension`

```diff

-3350.71.2.0.0
-  __TEXT.__text: 0x8d74
+3350.77.5.6.0
+  __TEXT.__text: 0x8084
   __TEXT.__objc_methlist: 0xc00
-  __TEXT.__cstring: 0x6bf
-  __TEXT.__const: 0xaa
-  __TEXT.__oslogstring: 0x3c0
+  __TEXT.__cstring: 0x4c6
+  __TEXT.__const: 0x8a
   __TEXT.__constg_swiftt: 0x28
   __TEXT.__swift5_typeref: 0x15
   __TEXT.__swift5_fieldmd: 0x10
   __TEXT.__swift5_types: 0x4
-  __TEXT.__unwind_info: 0x358
+  __TEXT.__unwind_info: 0x348
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_selrefs: 0x608
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x98
-  __DATA_CONST.__got: 0x148
-  __AUTH_CONST.__const: 0x2d0
+  __DATA_CONST.__got: 0x138
+  __AUTH_CONST.__const: 0x2f0
   __AUTH_CONST.__cfstring: 0x240
   __AUTH_CONST.__objc_const: 0x2090
-  __AUTH_CONST.__auth_got: 0x2c0
+  __AUTH_CONST.__auth_got: 0x2a8
   __AUTH.__objc_data: 0x690
   __DATA.__objc_ivar: 0x170
   __DATA.__data: 0x228
-  __DATA.__common: 0x20
   - /System/Library/Frameworks/AVFoundation.framework/Versions/A/AVFoundation
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/Versions/A/CoreGraphics

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 333
-  Symbols:   169
-  CStrings:  65
+  Functions: 324
+  Symbols:   165
+  CStrings:  39
 
Symbols:
+ _FigSignalErrorAtGM
+ __NSConcreteGlobalBlock
+ _fig_log_get_emitter
- _FigSignalErrorAt3
- __os_log_send_and_compose_impl
- __xpc_error_connection_interrupted
- __xpc_error_connection_invalid
- _fig_log_call_emit_and_clean_up_after_send_and_compose
- _fig_log_emitter_get_os_log_and_send_and_compose_flags_and_os_log_type
- _os_log_type_enabled
CStrings:
+ "%s signalled err=%d at <>:%d"
+ "com.apple.coremedia"
- "%s%s%s signalled err=%d (%s) (%s) at %s:%d"
- "-[MEByteSource initWithRelatedFile:forByteSource:error:]"
- "-[MEByteSource requestDirectoryFileNames]"
- "-[MEByteSource startServiceConnection]"
- "-[MEByteSource startServiceConnection]_block_invoke"
- "-[MERAWProcessorPixelBufferManager setPixelBufferAttributes:]"
- "<<< MERAWProcessorPixelBufferManager >>> %s: Pool allocation failed with error: %d"
- "<<<< MEByteSource >>>> %s: Connection to XPC service was interrupted. Should get restored when needed. error: %s"
- "<<<< MEByteSource >>>> %s: Created connection to service %s."
- "<<<< MEByteSource >>>> %s: Error when sending directory list message: %s"
- "<<<< MEByteSource >>>> %s: Invalid XPC connection error for service: %s\n"
- "<<<< MEByteSource >>>> %s: Invalid response type: %llu\n"
- "<<<< MEByteSource >>>> %s: Operation failed for file descriptor: %d\n"
- "<<<< MEByteSource >>>> %s: Operation invalid for file descriptor %d\n"
- "<<<< MEByteSource >>>> %s: Received unexpected XPC error event: %s\n"
- "<<<< MEByteSource >>>> %s: Received unexpected XPC event in hander for service %s\n"
- "<<<< MEByteSource >>>> %s: Unable to access byte source file descriptor!"
- "<<<< MEByteSource >>>> %s: Unable to create connection to service %s."
- "<<<< MEByteSource >>>> %s: Unable to dispatch queue for XPC service."
- "MEByteSource.m"
- "MEErrorInternalFailure"
- "MEErrorInvalidParameter"
- "Unable to access MTPluginByteSource"
- "Unable to access MTPluginByteSource fig byte source"
- "Unable to access base byte source file descriptor!"
- "Unable to start XPC service"
- "byteSource NULL"
- "fileName NULL"
```
