## Diagnostic-8288

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8288.appex/Diagnostic-8288`

```diff

-32.0.0.0.0
-  __TEXT.__text: 0xce20
-  __TEXT.__auth_stubs: 0x610
+38.0.0.0.0
+  __TEXT.__text: 0xd458
+  __TEXT.__auth_stubs: 0x620
   __TEXT.__objc_stubs: 0x380
   __TEXT.__objc_methlist: 0x50
-  __TEXT.__cstring: 0x2d6d
-  __TEXT.__gcc_except_tab: 0x13d8
-  __TEXT.__const: 0x8
+  __TEXT.__cstring: 0x2ec0
+  __TEXT.__gcc_except_tab: 0x1490
+  __TEXT.__const: 0x10
   __TEXT.__oslogstring: 0x1d
   __TEXT.__objc_classname: 0x1a
   __TEXT.__objc_methname: 0x20d
-  __TEXT.__objc_methtype: 0xd1
-  __TEXT.__unwind_info: 0x410
+  __TEXT.__objc_methtype: 0xd2
+  __TEXT.__unwind_info: 0x40c
   __TEXT.__eh_frame: 0x4c
-  __DATA_CONST.__auth_got: 0x318
-  __DATA_CONST.__got: 0x2b8
+  __DATA_CONST.__auth_got: 0x320
+  __DATA_CONST.__got: 0x2c0
   __DATA_CONST.__const: 0x480
-  __DATA_CONST.__cfstring: 0x1ea0
+  __DATA_CONST.__cfstring: 0x1f80
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_classrefs: 0x38

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: BA58B653-FD27-38F5-801B-1F3E42410244
+  UUID: D6D85D09-71FD-3D29-8C75-F0B6D3A110BC
   Functions: 148
-  Symbols:   311
-  CStrings:  593
+  Symbols:   313
+  CStrings:  607
 
Symbols:
+ __ZN17DeviceCMInterface23requestControlOfStreamsEbj
+ __ZN28HxISPCaptureDeviceController14RequestStreamsEPK9__CFArrayPK14__CFDictionary
+ _kFigCaptureDeviceRequestControlOfStreamsOptionsKey_ClientPriority
+ _objc_release_x28
- __ZN17DeviceCMInterface23requestControlOfStreamsEv
- __ZN28HxISPCaptureDeviceController14RequestStreamsEPK9__CFArray
CStrings:
+ "^{DeviceCMInterface=i^{StreamingClient}^{HxISPCaptureDeviceController}{StreamIdsInfo=iiiiii}{PearlConfiguration=BBBii@}{JasperConfiguration=BBBBi}iBBBB}"
+ "cmsetcurrentformat 2 %d, setPearlFormatIndex(m_streamIdsInfo.rgbPearlStreamId, %d) ret = %d"
+ "config pearl device failed to read projector version"
+ "done waiting"
+ "projector version %d"
+ "request control on high priority"
+ "requestControlOfStreamscontrol - controlled by another client. %d/%d"
+ "waiting for preempted client to terminate for %.2f sec..."
- "^{DeviceCMInterface=i^{StreamingClient}^{HxISPCaptureDeviceController}{StreamIdsInfo=iiiiii}{PearlConfiguration=BBBii}{JasperConfiguration=BBBBi}iBBBB}"

```
