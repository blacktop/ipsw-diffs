## Diagnostic-8276

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8276.appex/Diagnostic-8276`

```diff

-32.0.0.0.0
-  __TEXT.__text: 0x19b74
+38.0.0.0.0
+  __TEXT.__text: 0x1a214
   __TEXT.__auth_stubs: 0xab0
-  __TEXT.__objc_stubs: 0x1900
+  __TEXT.__objc_stubs: 0x1920
   __TEXT.__objc_methlist: 0x810
-  __TEXT.__gcc_except_tab: 0x2848
+  __TEXT.__gcc_except_tab: 0x291c
   __TEXT.__const: 0x154
-  __TEXT.__objc_methname: 0x2f1f
-  __TEXT.__cstring: 0x3e24
+  __TEXT.__objc_methname: 0x2f2b
+  __TEXT.__cstring: 0x3fa3
   __TEXT.__objc_classname: 0x156
-  __TEXT.__objc_methtype: 0x1590
+  __TEXT.__objc_methtype: 0x1591
   __TEXT.__oslogstring: 0x11d
-  __TEXT.__unwind_info: 0x7f4
+  __TEXT.__unwind_info: 0x7f8
   __TEXT.__eh_frame: 0x4c
   __DATA_CONST.__auth_got: 0x570
-  __DATA_CONST.__got: 0x310
+  __DATA_CONST.__got: 0x318
   __DATA_CONST.__const: 0x5a0
-  __DATA_CONST.__cfstring: 0x2f00
+  __DATA_CONST.__cfstring: 0x3080
   __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_arraydata: 0xb0
   __DATA_CONST.__objc_dictobj: 0x50
   __DATA.__objc_const: 0x2410
-  __DATA.__objc_selrefs: 0x8b0
+  __DATA.__objc_selrefs: 0x8b8
   __DATA.__objc_ivar: 0x164
   __DATA.__objc_data: 0x280
   __DATA.__data: 0x2a0

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 361
-  Symbols:   448
-  CStrings:  1166
+  Symbols:   449
+  CStrings:  1179
 
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
