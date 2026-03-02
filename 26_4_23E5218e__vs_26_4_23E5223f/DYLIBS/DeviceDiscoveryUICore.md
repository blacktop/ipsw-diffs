## DeviceDiscoveryUICore

> `/System/Library/PrivateFrameworks/DeviceDiscoveryUICore.framework/DeviceDiscoveryUICore`

```diff

-2094.51.11.0.0
-  __TEXT.__text: 0x41628
+2094.51.25.0.0
+  __TEXT.__text: 0x41504
   __TEXT.__auth_stubs: 0x1920
-  __TEXT.__objc_methlist: 0x15c4
+  __TEXT.__objc_methlist: 0x15ac
   __TEXT.__const: 0x2bd0
   __TEXT.__cstring: 0x1767
   __TEXT.__oslogstring: 0x3050

   __TEXT.__swift5_acfuncs: 0x28
   __TEXT.__swift5_protos: 0x8
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x12f0
+  __TEXT.__unwind_info: 0x12e8
   __TEXT.__eh_frame: 0x1ae8
   __TEXT.__objc_classname: 0x83a
-  __TEXT.__objc_methname: 0x44d5
-  __TEXT.__objc_methtype: 0x1122
-  __TEXT.__objc_stubs: 0x3240
+  __TEXT.__objc_methname: 0x4455
+  __TEXT.__objc_methtype: 0x1112
+  __TEXT.__objc_stubs: 0x3220
   __DATA_CONST.__got: 0x530
   __DATA_CONST.__const: 0x990
   __DATA_CONST.__objc_classlist: 0x108
   __DATA_CONST.__objc_protolist: 0x130
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1030
+  __DATA_CONST.__objc_selrefs: 0x1028
   __DATA_CONST.__objc_protorefs: 0x70
   __DATA_CONST.__objc_superrefs: 0x68
   __AUTH_CONST.__auth_got: 0xca0
   __AUTH_CONST.__const: 0x1910
   __AUTH_CONST.__cfstring: 0x12a0
-  __AUTH_CONST.__objc_const: 0x2e18
+  __AUTH_CONST.__objc_const: 0x2de8
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH.__objc_data: 0xc20
   __AUTH.__data: 0x890
-  __DATA.__objc_ivar: 0x144
+  __DATA.__objc_ivar: 0x140
   __DATA.__data: 0x1230
   __DATA.__objc_stublist: 0x8
   __DATA.__bss: 0x42b0

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 29E0E628-FC59-3112-9074-27C38305B469
-  Functions: 1490
-  Symbols:   2605
-  CStrings:  1496
+  UUID: 46E661B4-0C2B-3636-AAEA-391CFEE4F2D7
+  Functions: 1488
+  Symbols:   2599
+  CStrings:  1492
 
Symbols:
+ -[_DDUIRemoteDisplaySessionHandler canEnterSession]
+ -[_DDUIRemoteDisplaySessionHandler isContinuityCaptureUserPreferenceEnabled]
+ -[_DDUIRemoteDisplaySessionHandler shouldAutoAcceptCCConfirmation]
+ -[_DDUIRemoteDisplaySessionHandler shouldByPassConfirmationForRemoteDeviceID:]
+ _objc_msgSend$canEnterSession
+ _objc_msgSend$isContinuityCaptureUserPreferenceEnabled
+ _objc_msgSend$shouldAutoAcceptCCConfirmation
+ _objc_msgSend$shouldByPassConfirmationForRemoteDeviceID:
- -[_DDUIRemoteDisplaySessionHandler canEnterSessionWithDevice:]
- -[_DDUIRemoteDisplaySessionHandler isContinuityCaptureUserPreferenceEnabledOrSkippedForDevice:]
- -[_DDUIRemoteDisplaySessionHandler shouldAutoAcceptCCConfirmationForRemoteDevice:]
- -[_DDUIRemoteDisplaySessionHandler shouldByPassConfirmationForRemoteDevice:]
- -[_DDUIiOSPresentedNotification remoteDevice]
- -[_DDUIiOSPresentedNotification setRemoteDevice:]
- _OBJC_IVAR_$__DDUIiOSPresentedNotification._remoteDevice
- _objc_msgSend$canEnterSessionWithDevice:
- _objc_msgSend$isContinuityCaptureUserPreferenceEnabledOrSkippedForDevice:
- _objc_msgSend$setRemoteDevice:
- _objc_msgSend$shouldAutoAcceptCCConfirmationForRemoteDevice:
- _objc_msgSend$shouldByPassConfirmationForRemoteDevice:
CStrings:
+ "canEnterSession"
+ "isContinuityCaptureUserPreferenceEnabled"
+ "shouldAutoAcceptCCConfirmation"
+ "shouldByPassConfirmationForRemoteDeviceID:"
- "@\"<DDUIDevice>\""
- "T@\"<DDUIDevice>\",&,N,V_remoteDevice"
- "_remoteDevice"
- "canEnterSessionWithDevice:"
- "isContinuityCaptureUserPreferenceEnabledOrSkippedForDevice:"
- "setRemoteDevice:"
- "shouldAutoAcceptCCConfirmationForRemoteDevice:"
- "shouldByPassConfirmationForRemoteDevice:"

```
