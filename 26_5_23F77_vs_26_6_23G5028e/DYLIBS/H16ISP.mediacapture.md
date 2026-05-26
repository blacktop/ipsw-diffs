## H16ISP.mediacapture

> `/System/Library/MediaCapture/H16ISP.mediacapture`

```diff

-5.504.0.0.0
-  __TEXT.__text: 0x1cf414
+5.601.0.0.0
+  __TEXT.__text: 0x1cf850
   __TEXT.__auth_stubs: 0x32a0
   __TEXT.__objc_methlist: 0x268
   __TEXT.__const: 0x2864f
-  __TEXT.__oslogstring: 0x1dcf9
-  __TEXT.__cstring: 0x19862
+  __TEXT.__oslogstring: 0x1de57
+  __TEXT.__cstring: 0x19871
   __TEXT.__gcc_except_tab: 0x72a4
-  __TEXT.__unwind_info: 0x3f98
+  __TEXT.__unwind_info: 0x3f90
   __TEXT.__objc_classname: 0x89
   __TEXT.__objc_methname: 0x1dc8
   __TEXT.__objc_methtype: 0x10b3

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 5DD2467F-DAB6-329D-905C-9AD8D3682657
+  UUID: EB732313-8316-343F-A200-FD9736CCE48A
   Functions: 5932
   Symbols:   15287
-  CStrings:  8033
+  CStrings:  8040
 
Functions:
~ __ZL32H16ISPCaptureStreamStartInternalP22OpaqueFigCaptureStream : 26348 -> 26528
~ __ZL33EnablePCEStreamingInFrameReceiverP19H16ISPCaptureDeviceP19H16ISPCaptureStream : 916 -> 1008
~ __ZN6H16ISP16ProjectorManager14updateOnChangeEii : 216 -> 436
~ __ZL35SetInfraredLightSourceConfigurationPKvP19H16ISPCaptureStreamP18H16ISPCaptureGroupP19H16ISPCaptureDevice : 168 -> 368
~ __ZL20SetIRProjectorParamsPKvP19H16ISPCaptureStreamP18H16ISPCaptureGroupP19H16ISPCaptureDevice : 1500 -> 1704
~ __ZL23SetGenericProjectorTypePKvP19H16ISPCaptureStreamP18H16ISPCaptureGroupP19H16ISPCaptureDevice : 148 -> 336
CStrings:
+ "%s - ch=%d exposure=%d fps=%d _didDisableAE=%d\n"
+ "EnablePCEStreamingInFrameReceiver: ch=%u isIRSensor=%d type=%d\n"
+ "H16ISPCaptureStreamStart: ch=%u isIRSensor=%d irProjectorType=%d pdeStreamingFlags=%u projectorAllowed=%d\n"
+ "SetGenericProjectorType: ch=%u\n"
+ "SetIRProjectorParams: ch=%u type=%d enable=%d\n"
+ "SetInfraredLightSourceConfiguration: ch=%u type=%d\n"
+ "updateOnChange"

```
