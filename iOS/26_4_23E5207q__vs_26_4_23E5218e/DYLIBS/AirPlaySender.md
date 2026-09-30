## AirPlaySender

> `/System/Library/PrivateFrameworks/AirPlaySender.framework/AirPlaySender`

```diff

-940.19.1.0.0
-  __TEXT.__text: 0x2149b4
-  __TEXT.__auth_stubs: 0x5700
+940.21.1.0.0
+  __TEXT.__text: 0x20f84c
+  __TEXT.__auth_stubs: 0x5710
   __TEXT.__objc_methlist: 0x7d4
-  __TEXT.__cstring: 0x84cc6
-  __TEXT.__const: 0x10110
-  __TEXT.__gcc_except_tab: 0x9c0
+  __TEXT.__cstring: 0x850ae
+  __TEXT.__const: 0x101e0
+  __TEXT.__gcc_except_tab: 0x9f8
   __TEXT.__dlopen_cstrs: 0x671
   __TEXT.__oslogstring: 0x7c5
-  __TEXT.__unwind_info: 0x52d0
+  __TEXT.__unwind_info: 0x52e0
   __TEXT.__eh_frame: 0x48
   __TEXT.__objc_classname: 0x1c5
-  __TEXT.__objc_methname: 0x216a
+  __TEXT.__objc_methname: 0x2220
   __TEXT.__objc_methtype: 0xd78
-  __TEXT.__objc_stubs: 0x1dc0
-  __DATA_CONST.__got: 0x1fd0
-  __DATA_CONST.__const: 0x6e50
+  __TEXT.__objc_stubs: 0x1f20
+  __DATA_CONST.__got: 0x1ff0
+  __DATA_CONST.__const: 0x6e98
   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x9c0
+  __DATA_CONST.__objc_selrefs: 0xa18
   __DATA_CONST.__objc_superrefs: 0x38
-  __DATA_CONST.__objc_arraydata: 0x88
-  __AUTH_CONST.__auth_got: 0x2b90
-  __AUTH_CONST.__const: 0x8388
-  __AUTH_CONST.__cfstring: 0x12da0
+  __DATA_CONST.__objc_arraydata: 0x170
+  __AUTH_CONST.__auth_got: 0x2b98
+  __AUTH_CONST.__const: 0x72a8
+  __AUTH_CONST.__cfstring: 0x12ee0
   __AUTH_CONST.__objc_const: 0xec8
-  __AUTH_CONST.__objc_dictobj: 0xa0
-  __AUTH_CONST.__objc_intobj: 0x48
-  __AUTH_CONST.__objc_arrayobj: 0x48
+  __AUTH_CONST.__objc_dictobj: 0x1b8
+  __AUTH_CONST.__objc_intobj: 0x138
+  __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH.__objc_data: 0x190
   __AUTH.__data: 0x7b0
   __DATA.__objc_ivar: 0x88
-  __DATA.__data: 0x188a8
-  __DATA.__bss: 0xa90
+  __DATA.__data: 0x18888
+  __DATA.__bss: 0xa98
   __DATA.__common: 0xa04
   __DATA_DIRTY.__objc_data: 0xa0
   __DATA_DIRTY.__data: 0xcc8

   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/CoreMedia.framework/CoreMedia
+  - /System/Library/Frameworks/CoreMotion.framework/CoreMotion
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/Frameworks/MediaToolbox.framework/MediaToolbox

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 0C92D9C0-5BB9-3D5E-9B6E-4BA86BAA2793
-  Functions: 10620
-  Symbols:   26530
-  CStrings:  13693
+  UUID: 27E016E9-D1AA-3C83-8130-96B42D8E503A
+  Functions: 10639
+  Symbols:   26595
+  CStrings:  13742
 
Symbols:
+ GCC_except_table14
+ _APDemoEndpointUIEventChannelClear
+ _APDemoEndpointUIEventChannelClear.cold.1
+ _APDemoEndpointUIEventChannelInit.cold.7
+ _IOHIDEventGetChildren
+ _IOHIDEventSystemClientSetMatchingMultiple
+ _NSRunLoopCommonModes
+ _OBJC_CLASS_$_CMMotionManager
+ _OBJC_CLASS_$_NSRunLoop
+ _OBJC_CLASS_$_NSTimer
+ ___APCarPlay_CRFetchStopSessionReasonsList_block_invoke
+ ___APCarPlay_CRFetchStopSessionReasonsList_block_invoke.cold.1
+ ___APCarPlay_CRFetchStopSessionReasonsList_block_invoke.cold.2
+ ___APCarPlay_CRFetchStopSessionReasonsList_block_invoke.cold.3
+ ___APHIDClientCreate_block_invoke.cold.7
+ ___block_descriptor_32_e17_v16?0"NSTimer"8l
+ ___block_descriptor_72_e8_32r40r48r56r_e29_v24?0"NSArray"8"NSError"16lr32l8r40l8r48l8r56l8
+ ___block_literal_global.238
+ ___block_literal_global.92
+ ___carManager_updateCurrentEndpoint_block_invoke.258
+ ___demoHIDClientInit_block_invoke
+ ___demoHIDClientInit_block_invoke.cold.1
+ ___demoHIDClientInit_block_invoke.cold.2
+ ___demoHIDClientInit_block_invoke.cold.3
+ ___getCRFetchStopSessionReasonsListSymbolLoc_block_invoke
+ _demoCreateBoolDataToSend
+ _demoCreateBoolDataToSend.cold.1
+ _demoUIEventChannelSendData
+ _demoUIEventChannelSendData.cold.1
+ _demoUIEventChannelSendData.cold.2
+ _demoUIEventChannelSendData.cold.3
+ _demoUIEventChannelSendData.cold.4
+ _demoUIEventChannelSendData.cold.5
+ _getCRFetchStopSessionReasonsListSymbolLoc.ptr
+ _jitterBuffer_Finalize.cold.1
+ _jitterBuffer_Finalize.cold.2
+ _objc_msgSend$addTimer:forMode:
+ _objc_msgSend$attitude
+ _objc_msgSend$deviceMotion
+ _objc_msgSend$isDeviceMotionAvailable
+ _objc_msgSend$mainRunLoop
+ _objc_msgSend$numberWithFloat:
+ _objc_msgSend$pitch
+ _objc_msgSend$roll
+ _objc_msgSend$setDeviceMotionUpdateInterval:
+ _objc_msgSend$startDeviceMotionUpdates
+ _objc_msgSend$timerWithTimeInterval:repeats:block:
+ _objc_msgSend$yaw
- _APCarPlay_CRFetchStopSessionReasonsList.cold.1
- _APCarPlay_CRFetchStopSessionReasonsList.cold.2
- _APCarPlay_CRFetchStopSessionReasonsList.cold.3
- _IOHIDEventSystemClientSetMatching
- ___block_literal_global.241
- ___carManager_updateCurrentEndpoint_block_invoke.261
- _demoHIDEventCallback.cold.5
- _demoHIDEventCallback.cold.6
- _demoHIDEventCallback.cold.7
- _objc_msgSend$numberWithInteger:
CStrings:
+ "%s enter: object=%p, resumed=%d, buffer=%p\n"
+ "%s exit: object=%p\n"
+ "940.21.1"
+ "CRFetchStopSessionReasonsList"
+ "CRFetchStopSessionReasonsList completion handler successful, took %lu ms\n"
+ "CameraBtnPress"
+ "Capturing motion data for demo data channel"
+ "Error in fetching stop session reasons: %@\n"
+ "Fetch stop session reasons list timeout\n"
+ "Fetching Stop Session reasons list: %@\n"
+ "MotionData"
+ "MotionDataPitch"
+ "MotionDataRoll"
+ "MotionDataYaw"
+ "NSData *demoCreateDictionaryDataToSend(NSString *, NSDictionary *, NSError **)"
+ "OSStatus APCarPlay_CRFetchStopSessionReasonsList(CFArrayRef *)_block_invoke"
+ "PowerBtnPress"
+ "PrimaryUsage"
+ "Returned from CRFetchStopSessionReasonsList\n"
+ "Unable to create NSData from demo motion: %@"
+ "VolDownBtnPress"
+ "VolUpBtnPress"
+ "[%{ptr}] DisplayUUID is empty, will not add to HID Device creation properties\n"
+ "addTimer:forMode:"
+ "attitude"
+ "demoCaptureMotionData"
+ "demoHIDupdateMotionData"
+ "deviceMotion"
+ "isDeviceMotionAvailable"
+ "jitterBuffer_Finalize"
+ "mainRunLoop"
+ "numberWithFloat:"
+ "pitch"
+ "roll"
+ "setDeviceMotionUpdateInterval:"
+ "startDeviceMotionUpdates"
+ "timerWithTimeInterval:repeats:block:"
+ "v16@?0@\"NSTimer\"8"
+ "void demoHIDupdateMotionData(void)"
+ "void jitterBuffer_Finalize(CMBaseObjectRef)"
+ "void soft_CRFetchStopSessionReasonsList(void (^)(NSArray<NSNumber *> *, NSError *))"
+ "yaw"
- "940.19.1"
- "Setting StopSession reasons list: %@\n"
- "numberWithInteger:"

```
