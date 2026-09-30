## AppleCameraISPExclaveKitServices

> `/System/Library/PrivateFrameworks/AppleCameraISPExclaveKitServices.framework/AppleCameraISPExclaveKitServices`

### Sections with Same Size but Changed Content

- `__TEXT.__gcc_except_tab`
- `__TEXT.__cstring`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__weak_got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__weak_auth_got`
- `__AUTH.__data`
- `__DATA.__data`

```diff

-20.55.3.0.0
-  __TEXT.__text: 0x30b60
+20.57.3.0.0
+  __TEXT.__text: 0x30c0c
   __TEXT.__const: 0x2ea
   __TEXT.__gcc_except_tab: 0x8c8
   __TEXT.__oslogstring: 0x431e

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 1174
+  Functions: 1175
   Symbols:   772
   CStrings:  802
 
Functions:
~ __ZN28ISPExclaveKitHostMetaManager19parseHostMetaSensorEPhP18HostMetaSensorInfo : 128 -> 140
~ __ZN28ISPExclaveKitHostMetaManager26readNextAndParseSensorMetaEP18HostMetaSensorInfoPm : 464 -> 480
~ __Z29ispExclaveKitCommandChInfoSetP20sExclaveKitIspCmdHdr : 2292 -> 2348
~ __Z34ispExclaveKitCommandChSendMetadataP20sExclaveKitIspCmdHdr : 1176 -> 1172
~ __ZL48_convertFrameworkSensorMetaToTightbeamSensorMetaPKN25ISPExclaveKitAutoExposure31sExclaveKitIspCmdChSendMetadataEP57applecamera_ispexclavekitshared_ekchannelsensormetadata_s : 364 -> 368
~ _applecamera_ispexclavekitshared_ekispmanager_channelsensormetadataset : 1088 -> 1100
+ __Z29ispExclaveKitCommandChInfoSetP20sExclaveKitIspCmdHdr.cold.16
```
