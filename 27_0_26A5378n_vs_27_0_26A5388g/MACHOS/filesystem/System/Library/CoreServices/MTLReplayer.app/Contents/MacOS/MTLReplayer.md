## MTLReplayer

> `/System/Library/CoreServices/MTLReplayer.app/Contents/MacOS/MTLReplayer`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__cfstring`
- `__DATA.__objc_const`
- `__DATA.__data`

```diff

-2027.0.33.0.0
-  __TEXT.__text: 0xb188
+2027.0.35.0.0
+  __TEXT.__text: 0xb16c
   __TEXT.__auth_stubs: 0x590
   __TEXT.__objc_stubs: 0x1d00
   __TEXT.__objc_methlist: 0x5fc
   __TEXT.__const: 0x17c
   __TEXT.__objc_methname: 0x1ca2
   __TEXT.__oslogstring: 0x3ee
-  __TEXT.__cstring: 0x189d
+  __TEXT.__cstring: 0x187a
   __TEXT.__gcc_except_tab: 0x7c
   __TEXT.__objc_classname: 0xa9
   __TEXT.__objc_methtype: 0xeea
   __TEXT.__unwind_info: 0x228
-  __DATA_CONST.__const: 0x9b0
+  __DATA_CONST.__const: 0x988
   __DATA_CONST.__cfstring: 0xb20
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_protolist: 0x28

   - /usr/lib/libz.1.dylib
   Functions: 135
   Symbols:   160
-  CStrings:  629
+  CStrings:  627
 
Functions:
~ sub_10000168c : 1864 -> 1840
~ sub_10000c1b8 -> sub_10000c1a0 : 212 -> 208
CStrings:
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XWjPwT/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/apr/apr_thread_mutex.c:50"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XWjPwT/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/replayer/GTMTLReplay_mainCLI.m"
- "-collectRawCounters"
- "-testProfiling"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.THTUEH/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/apr/apr_thread_mutex.c:50"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.THTUEH/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/replayer/GTMTLReplay_mainCLI.m"
```
