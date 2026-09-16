## AudioSession

> `/System/Library/PrivateFrameworks/AudioSession.framework/AudioSession`

```diff

-449.107.0.0.0
+449.203.0.0.0
   __TEXT.__text: 0x4e044
   __TEXT.__realtime: 0x178
   __TEXT.__objc_methlist: 0x2364
   __TEXT.__gcc_except_tab: 0x9010
   __TEXT.__cstring: 0x3a4f
   __TEXT.__const: 0x207
-  __TEXT.__oslogstring: 0x47f4
+  __TEXT.__oslogstring: 0x4878
   __TEXT.__unwind_info: 0x31c8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
CStrings:
+ "%25s:%-5d __delegate_identifier__:Performance Diagnostics__:::____message__:This method can lead to UI unresponsiveness if called on the main thread while the audio session is active."
+ "%25s:%-5d __delegate_identifier__:Performance Diagnostics__:::____message__:This method can lead to UI unresponsiveness if called on the main thread. Consider using the asynchronous activate/deactivate API instead for calls from the main thread."
- "%25s:%-5d This method can lead to UI unresponsiveness if called on the main thread while the audio session is active."
- "%25s:%-5d This method can lead to UI unresponsiveness if called on the main thread. Consider using the asynchronous activate/deactivate API instead for calls from the main thread."
```
