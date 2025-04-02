## MediaExtension

> `/System/Library/Frameworks/MediaExtension.framework/Versions/A/MediaExtension`

```diff

-3210.19.1.5.2
-  __TEXT.__text: 0x7c28
-  __TEXT.__auth_stubs: 0x540
+3225.3.2.15.1
+  __TEXT.__text: 0x8b2c
+  __TEXT.__auth_stubs: 0x580
   __TEXT.__objc_methlist: 0xbc8
-  __TEXT.__cstring: 0x465
-  __TEXT.__const: 0xfa
+  __TEXT.__cstring: 0x6a6
+  __TEXT.__const: 0x11a
+  __TEXT.__oslogstring: 0x3c0
   __TEXT.__constg_swiftt: 0xe4
   __TEXT.__swift5_typeref: 0x3f
   __TEXT.__swift5_fieldmd: 0xbc
   __TEXT.__swift5_types: 0x18
   __TEXT.__swift5_builtin: 0x50
   __TEXT.__swift5_reflstr: 0x42
-  __TEXT.__unwind_info: 0x348
+  __TEXT.__unwind_info: 0x358
   __TEXT.__objc_classname: 0x332
   __TEXT.__objc_methname: 0x1b03
   __TEXT.__objc_methtype: 0x84f
   __TEXT.__objc_stubs: 0xa60
-  __DATA_CONST.__got: 0x128
+  __DATA_CONST.__got: 0x138
   __DATA_CONST.__const: 0x110
   __DATA_CONST.__objc_classlist: 0xa8
   __DATA_CONST.__objc_protolist: 0x28

   __DATA_CONST.__objc_selrefs: 0x5d0
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x98
-  __AUTH_CONST.__auth_got: 0x2a8
+  __AUTH_CONST.__auth_got: 0x2c8
   __AUTH_CONST.__auth_ptr: 0x20
-  __AUTH_CONST.__const: 0x460
+  __AUTH_CONST.__const: 0x440
   __AUTH_CONST.__cfstring: 0x220
   __AUTH_CONST.__objc_const: 0x2030
   __AUTH.__objc_data: 0x690
   __DATA.__objc_ivar: 0x168
   __DATA.__data: 0x250
+  __DATA.__common: 0x20
   __DATA.__bss: 0x20
   - /System/Library/Frameworks/AVFoundation.framework/Versions/A/AVFoundation
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 318
-  Symbols:   176
-  CStrings:  480
+  Functions: 326
+  Symbols:   181
+  CStrings:  509
 
Symbols:
+ _FigSignalErrorAt3
+ __os_log_send_and_compose_impl
+ __xpc_error_connection_interrupted
+ __xpc_error_connection_invalid
+ _fig_log_call_emit_and_clean_up_after_send_and_compose
+ _fig_log_emitter_get_os_log_and_send_and_compose_flags_and_os_log_type
+ _os_log_type_enabled
- _FigSignalErrorAt
- __NSConcreteGlobalBlock
CStrings:
+ "%s%s%s signalled err=%d (%s) (%s) at %s:%d"
+ "-[MEByteSource initWithRelatedFile:forByteSource:error:]"
+ "-[MEByteSource requestDirectoryFileNames]"
+ "-[MEByteSource startServiceConnection]"
+ "-[MEByteSource startServiceConnection]_block_invoke"
+ "-[MERAWProcessorPixelBufferManager setPixelBufferAttributes:]"
+ "<<< MERAWProcessorPixelBufferManager >>> %s: Pool allocation failed with error: %d"
+ "<<<< MEByteSource >>>>"
+ "<<<< MEByteSource >>>> %s: Connection to XPC service was interrupted. Should get restored when needed. error: %s"
+ "<<<< MEByteSource >>>> %s: Created connection to service %s."
+ "<<<< MEByteSource >>>> %s: Error when sending directory list message: %s"
+ "<<<< MEByteSource >>>> %s: Invalid XPC connection error for service: %s\n"
+ "<<<< MEByteSource >>>> %s: Invalid response type: %llu\n"
+ "<<<< MEByteSource >>>> %s: Operation failed for file descriptor: %d\n"
+ "<<<< MEByteSource >>>> %s: Operation invalid for file descriptor %d\n"
+ "<<<< MEByteSource >>>> %s: Received unexpected XPC error event: %s\n"
+ "<<<< MEByteSource >>>> %s: Received unexpected XPC event in hander for service %s\n"
+ "<<<< MEByteSource >>>> %s: Unable to access byte source file descriptor!"
+ "<<<< MEByteSource >>>> %s: Unable to create connection to service %s."
+ "<<<< MEByteSource >>>> %s: Unable to dispatch queue for XPC service."
+ "MEByteSource.m"
+ "MEErrorInternalFailure"
+ "MEErrorInvalidParameter"
+ "Unable to access MTPluginByteSource"
+ "Unable to access MTPluginByteSource fig byte source"
+ "Unable to access base byte source file descriptor!"
+ "Unable to start XPC service"
+ "byteSource NULL"
+ "fileName NULL"

```
