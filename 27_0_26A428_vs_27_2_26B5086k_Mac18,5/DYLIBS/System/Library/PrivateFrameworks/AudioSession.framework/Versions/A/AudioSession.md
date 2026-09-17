## AudioSession

> `/System/Library/PrivateFrameworks/AudioSession.framework/Versions/A/AudioSession`

```diff

-449.108.0.0.0
+449.203.0.0.0
   __TEXT.__text: 0x4d7c0
   __TEXT.__realtime: 0x1718
   __TEXT.__objc_methlist: 0x201c
   __TEXT.__cstring: 0x4e90
   __TEXT.__const: 0x271a
   __TEXT.__gcc_except_tab: 0x77d0
-  __TEXT.__oslogstring: 0x5d31
+  __TEXT.__oslogstring: 0x5db5
   __TEXT.__dlopen_cstrs: 0xaf
   __TEXT.__unwind_info: 0x2f80
   __TEXT.__objc_stubs: 0x0
CStrings:
+ "%25s:%-5d __delegate_identifier__:Performance Diagnostics__:::____message__:This method can lead to UI unresponsiveness if called on the main thread while the audio session is active."
+ "%25s:%-5d __delegate_identifier__:Performance Diagnostics__:::____message__:This method can lead to UI unresponsiveness if called on the main thread. Consider using the asynchronous activate/deactivate API instead for calls from the main thread."
- "%25s:%-5d This method can lead to UI unresponsiveness if called on the main thread while the audio session is active."
- "%25s:%-5d This method can lead to UI unresponsiveness if called on the main thread. Consider using the asynchronous activate/deactivate API instead for calls from the main thread."
```
