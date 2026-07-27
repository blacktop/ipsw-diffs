## H16ISP.mediacapture

> `/System/Library/MediaCapture/H16ISP.mediacapture`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__got`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__auth_got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_intobj`
- `__DATA.__data`
- `__DATA_DIRTY.__data`

```diff

-5.502.1.0.0
-  __TEXT.__text: 0x18b590
+5.604.0.0.0
+  __TEXT.__text: 0x18b954
   __TEXT.__auth_stubs: 0x2800
   __TEXT.__const: 0x27187
-  __TEXT.__oslogstring: 0x1848a
-  __TEXT.__cstring: 0x15268
+  __TEXT.__oslogstring: 0x1857d
+  __TEXT.__cstring: 0x15277
   __TEXT.__gcc_except_tab: 0x544c
-  __TEXT.__unwind_info: 0x2fe0
+  __TEXT.__unwind_info: 0x2fd8
   __TEXT.__objc_methname: 0x5c7
   __TEXT.__objc_stubs: 0x9c0
   __DATA_CONST.__got: 0x3130

   - /usr/lib/libz.1.dylib
   Functions: 4924
   Symbols:   7474
-  CStrings:  5445
+  CStrings:  5451
 
Functions:
~ __ZN6H16ISP16ProjectorManager14updateOnChangeEii : 216 -> 436
~ __ZL35SetInfraredLightSourceConfigurationPKvP19H16ISPCaptureStreamP18H16ISPCaptureGroupP19H16ISPCaptureDevice : 192 -> 392
~ __ZL20SetIRProjectorParamsPKvP19H16ISPCaptureStreamP18H16ISPCaptureGroupP19H16ISPCaptureDevice : 1520 -> 1724
~ __ZL23SetGenericProjectorTypePKvP19H16ISPCaptureStreamP18H16ISPCaptureGroupP19H16ISPCaptureDevice : 148 -> 336
~ __ZL27SetDepthEngineConfigurationPKvP19H16ISPCaptureStreamP18H16ISPCaptureGroupP19H16ISPCaptureDevice : 3388 -> 3540
CStrings:
+ "%s - ch=%d exposure=%d fps=%d _didDisableAE=%d\n"
+ "EnablePCEStreamingInFrameReceiver: ch=%u isIRSensor=%d type=%d\n"
+ "SetGenericProjectorType: ch=%u\n"
+ "SetIRProjectorParams: ch=%u type=%d enable=%d\n"
+ "SetInfraredLightSourceConfiguration: ch=%u type=%d\n"
+ "updateOnChange"
```
