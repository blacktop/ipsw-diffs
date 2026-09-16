## DeviceSelectionEmergencyFlow

> `/System/Library/PrivateFrameworks/DeviceSelectionEmergencyFlow.framework/DeviceSelectionEmergencyFlow`

```diff

-3600.49.15.0.0
-  __TEXT.__text: 0x1721c
-  __TEXT.__objc_methlist: 0x374
+3605.22.1.0.0
+  __TEXT.__text: 0x17768
+  __TEXT.__objc_methlist: 0x38c
   __TEXT.__dlopen_cstrs: 0x60
   __TEXT.__const: 0x1208
   __TEXT.__swift5_typeref: 0x5a0

   __TEXT.__swift5_reflstr: 0x6bc
   __TEXT.__swift5_assocty: 0x30
   __TEXT.__swift5_capture: 0x264
-  __TEXT.__cstring: 0x4c2
+  __TEXT.__cstring: 0x4ed
   __TEXT.__oslogstring: 0x7e9
   __TEXT.__swift5_protos: 0x20
   __TEXT.__swift5_proto: 0xc8

   __TEXT.__swift_as_entry: 0xc0
   __TEXT.__swift_as_ret: 0xb8
   __TEXT.__swift_as_cont: 0x160
-  __TEXT.__gcc_except_tab: 0x30
-  __TEXT.__unwind_info: 0xba8
+  __TEXT.__gcc_except_tab: 0x38
+  __TEXT.__unwind_info: 0xbd8
   __TEXT.__eh_frame: 0x178c
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_classlist: 0x70
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x290
+  __DATA_CONST.__objc_selrefs: 0x2b8
   __DATA_CONST.__objc_superrefs: 0x20
-  __DATA_CONST.__got: 0x168
+  __DATA_CONST.__got: 0x178
   __AUTH_CONST.__const: 0x14a8
-  __AUTH_CONST.__objc_const: 0x1078
-  __AUTH_CONST.__auth_got: 0x688
+  __AUTH_CONST.__objc_const: 0x10a8
+  __AUTH_CONST.__auth_got: 0x6b8
   __AUTH.__data: 0xa0
-  __DATA.__objc_ivar: 0x38
+  __DATA.__objc_ivar: 0x3c
   __DATA.__data: 0x2a8
   __DATA_DIRTY.__objc_data: 0x190
   __DATA_DIRTY.__data: 0x7c8

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 928
-  Symbols:   586
-  CStrings:  74
+  Functions: 937
+  Symbols:   611
+  CStrings:  76
 
Symbols:
+ -[WiProxDeviceInfo idsDeviceID]
+ -[WiProxDeviceInfo initWithDeviceUUID:deviceAddress:idsDeviceID:heySiriPerceptualHash:heySiriSNR:heySiriConfidence:heySiriDeviceGroup:heySiriDeviceClass:heySiriRandom:heySiriProductType:]
+ -[WiProxDiscoveryAdapter startScanningAndAdvertisingWithPhash:snr:random:confidence:]
+ GCC_except_table30
+ GCC_except_table31
+ GCC_except_table42
+ _MakeHeySiriPayload
+ _OBJC_CLASS_$_NSString
+ _OBJC_IVAR_$_WiProxDeviceInfo._idsDeviceID
+ _WirelessProximityLibrary
+ ___85-[WiProxDiscoveryAdapter startScanningAndAdvertisingWithPhash:snr:random:confidence:]_block_invoke
+ ___getWPHeySiriNeedsIdentitySymbolLoc_block_invoke
+ ___getWPHeySiriRPIdentitySymbolLoc_block_invoke
+ ___kCFBooleanTrue
+ _getWPHeySiriAdvertisingData
+ _getWPHeySiriNeedsIdentity
+ _getWPHeySiriNeedsIdentitySymbolLoc.ptr
+ _getWPHeySiriRPIdentitySymbolLoc.ptr
+ _objc_autoreleaseReturnValue
+ _objc_msgSend$copy
+ _objc_msgSend$initWithDeviceUUID:deviceAddress:idsDeviceID:heySiriPerceptualHash:heySiriSNR:heySiriConfidence:heySiriDeviceGroup:heySiriDeviceClass:heySiriRandom:heySiriProductType:
+ _objc_msgSend$setObject:forKey:
+ _objc_msgSend$startScanningAndAdvertisingWithData:
+ _objc_opt_class
+ _objc_opt_isKindOfClass
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x21
+ _objc_retain_x24
+ _objc_retain_x27
- -[WiProxDeviceInfo initWithDeviceUUID:deviceAddress:heySiriPerceptualHash:heySiriSNR:heySiriConfidence:heySiriDeviceGroup:heySiriDeviceClass:heySiriRandom:heySiriProductType:]
- GCC_except_table27
- _objc_msgSend$initWithDeviceUUID:deviceAddress:heySiriPerceptualHash:heySiriSNR:heySiriConfidence:heySiriDeviceGroup:heySiriDeviceClass:heySiriRandom:heySiriProductType:
- _objc_retain_x25
CStrings:
+ "WPHeySiriNeedsIdentity"
+ "WPHeySiriRPIdentity"
```
