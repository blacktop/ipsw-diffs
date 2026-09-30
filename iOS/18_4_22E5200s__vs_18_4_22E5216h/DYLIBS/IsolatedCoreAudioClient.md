## IsolatedCoreAudioClient

> `/System/Library/PrivateFrameworks/IsolatedCoreAudioClient.framework/IsolatedCoreAudioClient`

```diff

-5.512.0.0.0
-  __TEXT.__text: 0x1a0a4
+5.514.0.0.0
+  __TEXT.__text: 0x1a714
   __TEXT.__auth_stubs: 0xa30
   __TEXT.__objc_methlist: 0x85c
   __TEXT.__const: 0x27a6
-  __TEXT.__gcc_except_tab: 0x1c88
-  __TEXT.__cstring: 0x86a
-  __TEXT.__oslogstring: 0x2442
-  __TEXT.__unwind_info: 0xf08
+  __TEXT.__gcc_except_tab: 0x1d00
+  __TEXT.__cstring: 0x87a
+  __TEXT.__oslogstring: 0x282d
+  __TEXT.__unwind_info: 0xf30
   __TEXT.__objc_classname: 0x211
   __TEXT.__objc_methname: 0x1030
   __TEXT.__objc_methtype: 0xc5a

   __AUTH.__objc_data: 0x190
   __DATA.__objc_ivar: 0x60
   __DATA.__data: 0x360
-  __DATA.__bss: 0x208
+  __DATA.__bss: 0x218
   __DATA_DIRTY.__objc_data: 0x140
   __DATA_DIRTY.__bss: 0x10
   - /System/Library/Frameworks/CoreAudio.framework/CoreAudio

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 867
-  Symbols:   1086
-  CStrings:  492
+  Functions: 868
+  Symbols:   1087
+  CStrings:  504
 
CStrings:
+ "%25s:%-5d AudioClient::start - The client has tried to start IO, but IO is already being started or stopped by the client."
+ "%25s:%-5d AudioClient::start - The client has tried to start IO, but client IO is already running."
+ "%25s:%-5d AudioClient::start - There was an error trying to start IO."
+ "%25s:%-5d AudioClient::start - Unknown exception caught."
+ "%25s:%-5d AudioClient::startAtTime - The client has tried to start IO, but IO is already being started or stopped by the client."
+ "%25s:%-5d AudioClient::startAtTime - The client has tried to start IO, but client IO is already running."
+ "%25s:%-5d AudioClient::startAtTime - There was an error trying to start IO at the given time."
+ "%25s:%-5d AudioClient::startAtTime - Unknown exception caught."
+ "%25s:%-5d AudioClient::stop - The client has tried to stop IO, but IO is already being started or stopped by the client."
+ "%25s:%-5d AudioClient::stop - The client has tried to stop IO, but IO is not running."
+ "%25s:%-5d AudioClient::stop - Unknown exception caught."
+ "AudioClient.cpp"

```
