## CoreAudio

> `/System/Library/Components/CoreAudio.component/Contents/MacOS/CoreAudio`

### Sections with Same Size but Changed Content

- `__TEXT.__dof_AudioTool`
- `__TEXT.__eh_frame`
- `__DATA.__objc_selrefs`

```diff

-1633.10.0.0.0
-  __TEXT.__text: 0xd82e4
-  __TEXT.__realtime: 0x3f328
+1638.0.0.0.0
+  __TEXT.__text: 0xd8578
+  __TEXT.__realtime: 0x3f524
   __TEXT.__auth_stubs: 0x2630
   __TEXT.__objc_stubs: 0x540
   __TEXT.__const: 0xa760
-  __TEXT.__gcc_except_tab: 0x881c
-  __TEXT.__cstring: 0x8486
-  __TEXT.__oslogstring: 0x9bdc
+  __TEXT.__gcc_except_tab: 0x8848
+  __TEXT.__cstring: 0x84a6
+  __TEXT.__oslogstring: 0x9c37
   __TEXT.__dlopen_cstrs: 0x8e
   __TEXT.__objc_methname: 0x2e3
   __TEXT.__dof_AudioTool: 0x2c7
-  __TEXT.__unwind_info: 0x4958
+  __TEXT.__unwind_info: 0x4970
   __TEXT.__eh_frame: 0x108
-  __DATA_CONST.__const: 0x123b8
-  __DATA_CONST.__cfstring: 0x4620
+  __DATA_CONST.__const: 0x123c0
+  __DATA_CONST.__cfstring: 0x4640
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__auth_got: 0x1328
   __DATA_CONST.__got: 0x208
   __DATA_CONST.__auth_ptr: 0x8
   __DATA.__objc_selrefs: 0x150
-  __DATA.__data: 0xe60
+  __DATA.__data: 0xe68
   __DATA.__bss: 0xd50
   - /System/Library/Frameworks/Accelerate.framework/Versions/A/Accelerate
   - /System/Library/Frameworks/AudioToolbox.framework/Versions/A/AudioToolbox

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 4248
+  Functions: 4250
   Symbols:   834
-  CStrings:  2046
+  CStrings:  2050
 
CStrings:
+ "%25s:%-5d SetConverterChannelMap failed: err %d"
+ "AUAccessGuard<T> concurrent access at caller=%p"
+ "AUBase::ScheduleParameter: could not access parameter event list"
+ "AUConverterBase.cpp"
+ "legacy mode"
- "MatrixReverb: channelCount %u exceeds max %u (hasLFE=%d, LFEIndex=%d)"
```
