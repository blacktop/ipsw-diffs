## Diagnostic-6002

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-6002.appex/Diagnostic-6002`

```diff

-32.0.0.0.0
-  __TEXT.__text: 0x1a1e4
+38.0.0.0.0
+  __TEXT.__text: 0x1a890
   __TEXT.__auth_stubs: 0xac0
-  __TEXT.__objc_stubs: 0x1a80
+  __TEXT.__objc_stubs: 0x1aa0
   __TEXT.__objc_methlist: 0x84c
-  __TEXT.__gcc_except_tab: 0x28f4
+  __TEXT.__gcc_except_tab: 0x29c8
   __TEXT.__const: 0x154
-  __TEXT.__objc_methname: 0x306d
-  __TEXT.__cstring: 0x3f78
+  __TEXT.__objc_methname: 0x3079
+  __TEXT.__cstring: 0x40f7
   __TEXT.__objc_classname: 0x14c
-  __TEXT.__objc_methtype: 0x15ff
+  __TEXT.__objc_methtype: 0x1600
   __TEXT.__oslogstring: 0xec
-  __TEXT.__unwind_info: 0x818
+  __TEXT.__unwind_info: 0x81c
   __TEXT.__eh_frame: 0x4c
   __DATA_CONST.__auth_got: 0x578
-  __DATA_CONST.__got: 0x310
+  __DATA_CONST.__got: 0x318
   __DATA_CONST.__const: 0x5a0
-  __DATA_CONST.__cfstring: 0x2fc0
+  __DATA_CONST.__cfstring: 0x3140
   __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_arraydata: 0xb0
   __DATA_CONST.__objc_dictobj: 0x50
   __DATA.__objc_const: 0x2440
-  __DATA.__objc_selrefs: 0x910
+  __DATA.__objc_selrefs: 0x918
   __DATA.__objc_ivar: 0x168
   __DATA.__objc_data: 0x280
   __DATA.__data: 0x2a0

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 366
-  Symbols:   451
-  CStrings:  1191
+  Symbols:   452
+  CStrings:  1204
 
Symbols:
+ __ZN17DeviceCMInterface23requestControlOfStreamsEbj
+ __ZN28HxISPCaptureDeviceController14RequestStreamsEPK9__CFArrayPK14__CFDictionary
+ _kFigCaptureDeviceRequestControlOfStreamsOptionsKey_ClientPriority
- __ZN17DeviceCMInterface23requestControlOfStreamsEv
- __ZN28HxISPCaptureDeviceController14RequestStreamsEPK9__CFArray
CStrings:
+ "FW VALIDATION FAIL INFO"
+ "J717"
+ "J718"
+ "J720"
+ "J721"
+ "^{DeviceCMInterface=i^{StreamingClient}^{HxISPCaptureDeviceController}{StreamIdsInfo=iiiiii}{PearlConfiguration=BBBii@}{JasperConfiguration=BBBBi}iBBBB}"
+ "cmsetcurrentformat 2 %d, setPearlFormatIndex(m_streamIdsInfo.rgbPearlStreamId, %d) ret = %d"
+ "config pearl device failed to read projector version"
+ "dictionary"
+ "done waiting"
+ "projector version %d"
+ "request control on high priority"
+ "requestControlOfStreamscontrol - controlled by another client. %d/%d"
+ "waiting for preempted client to terminate for %.2f sec..."
- "^{DeviceCMInterface=i^{StreamingClient}^{HxISPCaptureDeviceController}{StreamIdsInfo=iiiiii}{PearlConfiguration=BBBii}{JasperConfiguration=BBBBi}iBBBB}"

```
