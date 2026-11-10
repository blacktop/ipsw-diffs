## AudioSession

> `/System/Library/PrivateFrameworks/AudioSession.framework/Versions/A/AudioSession`

```diff

-449.108.0.0.0
-  __TEXT.__text: 0x4eb20
+449.205.0.0.0
+  __TEXT.__text: 0x4ebe8
   __TEXT.__realtime: 0x1748
-  __TEXT.__objc_methlist: 0x201c
+  __TEXT.__objc_methlist: 0x2024
   __TEXT.__cstring: 0x4e90
   __TEXT.__const: 0x271a
-  __TEXT.__gcc_except_tab: 0x77d0
-  __TEXT.__oslogstring: 0x5d31
+  __TEXT.__gcc_except_tab: 0x77f8
+  __TEXT.__oslogstring: 0x5db5
   __TEXT.__dlopen_cstrs: 0xaf
   __TEXT.__unwind_info: 0x2b88
   __TEXT.__objc_stubs: 0x0

   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x10
-  __DATA_CONST.__objc_selrefs: 0x1568
+  __DATA_CONST.__objc_selrefs: 0x1570
   __DATA_CONST.__objc_superrefs: 0xe0
   __DATA_CONST.__objc_arraydata: 0x10
   __DATA_CONST.__got: 0x738

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1984
+  Functions: 1985
   Symbols:   3998
   CStrings:  1001
 
Symbols:
+ +[AVAudioApplication(SPI) homeAccessorySupportsEnhanceDialogue]
+ GCC_except_table104
+ GCC_except_table197
+ _objc_msgSend$homeAccessorySupportsEnhanceDialogue
- GCC_except_table103
- GCC_except_table180
- GCC_except_table192
- GCC_except_table196
CStrings:
+ "%25s:%-5d __delegate_identifier__:Performance Diagnostics__:::____message__:This method can lead to UI unresponsiveness if called on the main thread while the audio session is active."
+ "%25s:%-5d __delegate_identifier__:Performance Diagnostics__:::____message__:This method can lead to UI unresponsiveness if called on the main thread. Consider using the asynchronous activate/deactivate API instead for calls from the main thread."
- "%25s:%-5d This method can lead to UI unresponsiveness if called on the main thread while the audio session is active."
- "%25s:%-5d This method can lead to UI unresponsiveness if called on the main thread. Consider using the asynchronous activate/deactivate API instead for calls from the main thread."
```
