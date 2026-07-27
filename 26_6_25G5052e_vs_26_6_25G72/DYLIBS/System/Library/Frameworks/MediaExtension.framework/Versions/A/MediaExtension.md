## MediaExtension

> `/System/Library/Frameworks/MediaExtension.framework/Versions/A/MediaExtension`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__AUTH.__objc_data`
- `__DATA.__data`

```diff

-3330.10.1.0.0
-  __TEXT.__text: 0x9050
-  __TEXT.__auth_stubs: 0x560
+3330.13.2.0.0
+  __TEXT.__text: 0x8354
+  __TEXT.__auth_stubs: 0x530
   __TEXT.__objc_methlist: 0xbe8
-  __TEXT.__cstring: 0x6a8
-  __TEXT.__const: 0x19a
-  __TEXT.__oslogstring: 0x3c0
+  __TEXT.__cstring: 0x4af
+  __TEXT.__const: 0x17a
   __TEXT.__constg_swiftt: 0xe4
   __TEXT.__swift5_typeref: 0x3f
   __TEXT.__swift5_fieldmd: 0xbc
   __TEXT.__swift5_types: 0x18
   __TEXT.__swift5_builtin: 0x50
   __TEXT.__swift5_reflstr: 0x42
-  __TEXT.__unwind_info: 0x330
+  __TEXT.__unwind_info: 0x320
   __TEXT.__objc_classname: 0x335
   __TEXT.__objc_methname: 0x1b54
   __TEXT.__objc_methtype: 0x84f
   __TEXT.__objc_stubs: 0xc60
-  __DATA_CONST.__got: 0x138
+  __DATA_CONST.__got: 0x128
   __DATA_CONST.__const: 0xe0
   __DATA_CONST.__objc_classlist: 0xa8
   __DATA_CONST.__objc_protolist: 0x28

   __DATA_CONST.__objc_selrefs: 0x5e0
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x98
-  __AUTH_CONST.__auth_got: 0x2b8
-  __AUTH_CONST.__const: 0x4b0
+  __AUTH_CONST.__auth_got: 0x2a0
+  __AUTH_CONST.__const: 0x4d0
   __AUTH_CONST.__cfstring: 0x240
   __AUTH_CONST.__objc_const: 0x2060
   __AUTH.__objc_data: 0x690
   __DATA.__objc_ivar: 0x16c
   __DATA.__data: 0x230
-  __DATA.__common: 0x20
   __DATA.__bss: 0x20
   - /System/Library/Frameworks/AVFoundation.framework/Versions/A/AVFoundation
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 335
-  Symbols:   169
-  CStrings:  510
+  Functions: 333
+  Symbols:   165
+  CStrings:  484
 
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
