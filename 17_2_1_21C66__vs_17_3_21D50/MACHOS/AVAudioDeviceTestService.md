## AVAudioDeviceTestService

> `/System/Library/Frameworks/AVFAudio.framework/XPCServices/AVAudioDeviceTestService.xpc/AVAudioDeviceTestService`

```diff

-629.3.4.0.0
-  __TEXT.__text: 0xdce4
-  __TEXT.__auth_stubs: 0x630
+629.3.5.0.0
+  __TEXT.__text: 0xdfc0
+  __TEXT.__auth_stubs: 0x620
   __TEXT.__objc_stubs: 0x1ac0
   __TEXT.__objc_methlist: 0x784
   __TEXT.__const: 0xe0
-  __TEXT.__gcc_except_tab: 0x1a4c
+  __TEXT.__gcc_except_tab: 0x1ad0
   __TEXT.__cstring: 0x567
-  __TEXT.__oslogstring: 0xebe
+  __TEXT.__oslogstring: 0xfcb
   __TEXT.__objc_methname: 0x1f00
   __TEXT.__objc_classname: 0x10f
   __TEXT.__objc_methtype: 0x4ae
   __TEXT.__unwind_info: 0x3b4
   __TEXT.__eh_frame: 0x38
-  __DATA_CONST.__auth_got: 0x330
+  __DATA_CONST.__auth_got: 0x328
   __DATA_CONST.__got: 0xc8
   __DATA_CONST.__const: 0x458
   __DATA_CONST.__cfstring: 0x6a0

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 195
-  Symbols:   169
-  CStrings:  621
+  Symbols:   168
+  CStrings:  624
 
Symbols:
- _objc_retain_x27
CStrings:
+ "%25s:%-5d Invalid mic channel name. { providedName=%{public}@ }"
+ "%25s:%-5d Invalid setup, cannot provide multichannel playback file without specifying mic channel."
+ "%25s:%-5d Multichannel file provided, will split into single channel buffers. { requestedMic=%{public}@ }"

```
