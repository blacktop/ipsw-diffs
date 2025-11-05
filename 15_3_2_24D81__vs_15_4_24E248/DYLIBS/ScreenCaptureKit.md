## ScreenCaptureKit

> `/System/iOSSupport/System/Library/Frameworks/ScreenCaptureKit.framework/Versions/A/ScreenCaptureKit`

```diff

-595.11.1.0.0
-  __TEXT.__text: 0x35cf8
+610.5.1.5.1
+  __TEXT.__text: 0x361b0
   __TEXT.__auth_stubs: 0xcd0
-  __TEXT.__objc_methlist: 0x28f8
+  __TEXT.__objc_methlist: 0x2cfc
   __TEXT.__const: 0x17e
-  __TEXT.__oslogstring: 0x3393
-  __TEXT.__cstring: 0x53f2
+  __TEXT.__oslogstring: 0x33e6
+  __TEXT.__cstring: 0x541f
   __TEXT.__gcc_except_tab: 0x6e0
   __TEXT.__constg_swiftt: 0x54
   __TEXT.__swift5_typeref: 0x2e

   __TEXT.__swift5_fieldmd: 0x5c
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_types: 0x8
-  __TEXT.__unwind_info: 0xb80
+  __TEXT.__unwind_info: 0xbd0
   __TEXT.__objc_classname: 0x662
-  __TEXT.__objc_methname: 0x7ca5
+  __TEXT.__objc_methname: 0x7ce8
   __TEXT.__objc_methtype: 0x108b
-  __TEXT.__objc_stubs: 0x4f60
-  __DATA_CONST.__got: 0x388
-  __DATA_CONST.__const: 0xce8
+  __TEXT.__objc_stubs: 0x4fa0
+  __DATA_CONST.__got: 0x390
+  __DATA_CONST.__const: 0xcf0
   __DATA_CONST.__objc_classlist: 0x160
   __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1a78
+  __DATA_CONST.__objc_selrefs: 0x1b08
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x128
   __DATA_CONST.__objc_arraydata: 0x10
   __AUTH_CONST.__auth_got: 0x678
   __AUTH_CONST.__const: 0x230
   __AUTH_CONST.__cfstring: 0x1f00
-  __AUTH_CONST.__objc_const: 0x73d8
+  __AUTH_CONST.__objc_const: 0x6cc0
   __AUTH_CONST.__objc_intobj: 0x180
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH.__objc_data: 0xdc0

   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
+  - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIOKit.dylib
   - /usr/lib/swift/libswiftMetal.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: BA1A0E37-B816-3130-9B70-91D42BD7BFF5
-  Functions: 1260
-  Symbols:   3099
-  CStrings:  2556
+  UUID: 977E154A-247A-35FE-9600-8698B30B3D06
+  Functions: 1259
+  Symbols:   3101
+  CStrings:  2560
 
Symbols:
+ +[RPFeatureFlagUtility sharedInstance].cold.1
+ +[SCContentSharingSessionManager shared].cold.1
+ -[SCControlCenterManager getCameraIDforPID:].cold.1
+ RP_Micro.cold.1
+ _CMCaptureFrameSenderEndpointTypeInputVideo
+ __MergedGlobals
+ __swift_FORCE_LOAD_$_swiftDataDetection
+ __swift_FORCE_LOAD_$_swiftDataDetection_$_ScreenCaptureKit
+ _objc_msgSend$endpointType
+ _objc_msgSend$pickerDidUpdate:withFilter:preservedFilter:forStream:
- RP_MachTimeScale.did_init
- RP_MachTimeScale.timeScale
- _OUTLINED_FUNCTION_11
CStrings:
+ " [ERROR] %{public}s:%d did not have an endpoint with type InputVideo, endpoints=%@"
+ "-[SCControlCenterManager getCameraIDforPID:]"
+ "endpointType"
+ "pickerDidUpdate:withFilter:preservedFilter:forStream:"

```
