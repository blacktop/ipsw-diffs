## AudioSessionServer

> `/System/Library/PrivateFrameworks/AudioSessionServer.framework/AudioSessionServer`

```diff

-321.112.0.0.0
-  __TEXT.__text: 0x5b1b0
-  __TEXT.__auth_stubs: 0x10a0
+321.115.0.0.0
+  __TEXT.__text: 0x5b5fc
+  __TEXT.__auth_stubs: 0x10d0
   __TEXT.__objc_methlist: 0x6d0
   __TEXT.__const: 0xb79
-  __TEXT.__gcc_except_tab: 0x864c
-  __TEXT.__cstring: 0x40a3
+  __TEXT.__gcc_except_tab: 0x86b0
+  __TEXT.__cstring: 0x428d
   __TEXT.__oslogstring: 0x3874
   __TEXT.__dlopen_cstrs: 0x5a
-  __TEXT.__unwind_info: 0x2650
+  __TEXT.__unwind_info: 0x2678
   __TEXT.__objc_classname: 0x13a
-  __TEXT.__objc_methname: 0x1930
-  __TEXT.__objc_methtype: 0x2833
-  __TEXT.__objc_stubs: 0xe20
+  __TEXT.__objc_methname: 0x192a
+  __TEXT.__objc_methtype: 0x288a
+  __TEXT.__objc_stubs: 0xe00
   __DATA_CONST.__got: 0x400
-  __DATA_CONST.__const: 0x418
+  __DATA_CONST.__const: 0x468
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x648
   __DATA_CONST.__objc_superrefs: 0x28
-  __AUTH_CONST.__auth_got: 0x860
+  __AUTH_CONST.__auth_got: 0x878
   __AUTH_CONST.__const: 0x9f8
   __AUTH_CONST.__cfstring: 0xbc0
   __AUTH_CONST.__objc_const: 0x1488
   __AUTH_CONST.__objc_intobj: 0x78
   __DATA.__objc_ivar: 0x60
   __DATA.__data: 0x249
-  __DATA.__bss: 0xa8
+  __DATA.__bss: 0x50
   __DATA.__common: 0x1
   __DATA_DIRTY.__objc_data: 0x1e0
   __DATA_DIRTY.__data: 0x30
-  __DATA_DIRTY.__bss: 0x248
+  __DATA_DIRTY.__bss: 0x2a0
   __DATA_DIRTY.__common: 0x8
   - /System/Library/Frameworks/CoreAudio.framework/CoreAudio
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1414
-  Symbols:   2090
-  CStrings:  1235
+  Functions: 1417
+  Symbols:   2098
+  CStrings:  1241
 
Symbols:
+ __ZN2as12WorkloopPool13dispatchAsyncEU13block_pointerFvvE
+ __ZN2as12WorkloopPool6CreateEm
+ _objc_release_x1
+ _objc_retain_x26
- _dispatch_sync
CStrings:
+ "\x03B"
+ "-[AVAudioSessionRemoteXPCClient getMXPropertyGenericPipe:propertyName:reply:]_block_invoke"
+ "-[AVAudioSessionRemoteXPCClient getProperties:properties:reply:]_block_invoke"
+ "-[AVAudioSessionRemoteXPCClient getProperty:propertyName:MXProperty:reply:]_block_invoke"
+ "-[AVAudioSessionRemoteXPCClient setProperties:values:MXProperties:batchStrategy:genericMXPipe:reply:]_block_invoke"
+ "-[AVAudioSessionRemoteXPCClient setProperties:values:MXProperties:batchStrategy:genericMXPipe:reply:]_block_invoke_2"
+ "_workloopPool"
+ "{shared_ptr<as::WorkloopPool>=\"__ptr_\"^{WorkloopPool}\"__cntrl_\"^{__shared_weak_count}}"
- "\x032"
- "_clientDeathPromise"

```
