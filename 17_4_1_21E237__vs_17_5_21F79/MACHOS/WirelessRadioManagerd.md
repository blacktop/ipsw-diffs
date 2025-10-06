## WirelessRadioManagerd

> `/usr/sbin/WirelessRadioManagerd`

```diff

-1630.4.8.0.0
-  __TEXT.__text: 0x12fcf8
+1630.5.2.0.0
+  __TEXT.__text: 0x130cd8
   __TEXT.__auth_stubs: 0x1fc0
-  __TEXT.__objc_stubs: 0x1a5c0
-  __TEXT.__objc_methlist: 0xd3ac
-  __TEXT.__objc_methname: 0x28afe
-  __TEXT.__cstring: 0x43d23
+  __TEXT.__objc_stubs: 0x1a780
+  __TEXT.__objc_methlist: 0xd46c
+  __TEXT.__objc_methname: 0x28d5c
+  __TEXT.__cstring: 0x43ff9
   __TEXT.__objc_classname: 0xcf6
   __TEXT.__objc_methtype: 0x6af4
-  __TEXT.__const: 0x21098
-  __TEXT.__gcc_except_tab: 0x3698
+  __TEXT.__const: 0x210a8
+  __TEXT.__gcc_except_tab: 0x36a0
   __TEXT.__dlopen_cstrs: 0x2b4
   __TEXT.__oslogstring: 0x85
-  __TEXT.__unwind_info: 0x4064
+  __TEXT.__unwind_info: 0x41e8
   __TEXT.__eh_frame: 0x88
   __DATA_CONST.__auth_got: 0xff8
   __DATA_CONST.__got: 0x478
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x45b8
-  __DATA_CONST.__cfstring: 0x26160
+  __DATA_CONST.__const: 0x45a0
+  __DATA_CONST.__cfstring: 0x26380
   __DATA_CONST.__objc_classlist: 0x3d8
   __DATA_CONST.__objc_catlist: 0x0
   __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_classrefs: 0x520
+  __DATA_CONST.__objc_classrefs: 0x528
   __DATA_CONST.__objc_superrefs: 0x400
   __DATA_CONST.__objc_arraydata: 0xd890
   __DATA_CONST.__objc_arrayobj: 0x5e20
   __DATA_CONST.__objc_intobj: 0x30d8
   __DATA_CONST.__objc_dictobj: 0x78
   __DATA_CONST.__objc_doubleobj: 0x10
-  __DATA.__objc_const: 0x171e8
-  __DATA.__objc_selrefs: 0x79a0
-  __DATA.__objc_ivar: 0x17ac
+  __DATA.__objc_const: 0x172d0
+  __DATA.__objc_selrefs: 0x7a20
+  __DATA.__objc_ivar: 0x17c4
   __DATA.__objc_data: 0x2670
-  __DATA.__data: 0x5b8
+  __DATA.__data: 0x5c0
   __DATA.__common: 0x142
   __DATA.__bss: 0x3f0
   - /System/Library/Frameworks/CallKit.framework/CallKit

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libnetwork.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 04BB2697-D145-3E82-8939-8900931F48B4
-  Functions: 6624
-  Symbols:   732
-  CStrings:  18068
+  UUID: CC94C4B6-6705-3DE7-AFFA-72CB0BC0828C
+  Functions: 6642
+  Symbols:   733
+  CStrings:  18135
 
Symbols:
+ _OBJC_CLASS_$_NSTimer
CStrings:
+ "CFUseTddModeDuringFindMy"
+ "FindMyPencil"
+ "Handle WiFi/BT Coex change %d"
+ "Received LeScanStateChange msg"
+ "Sending response to getHomeKitBtLoad message %@"
+ "Setting TDD profile for 2.4GHz -pencilCoexActive || findMyPencilScanActive || threadActive is (%d || %d || %d)"
+ "T@\"NSTimer\",&,N,V_homeKitReportingTimer"
+ "TB,R,N,V_findMyPencilScanActive"
+ "TDD_FINDMY"
+ "UCMClientManager: Rcvd WRMHomeKit controller event %p"
+ "WRMHomeKit"
+ "_findMyPencilScanActive"
+ "_homeKitReportingTimer"
+ "addTimer:forMode:"
+ "antenna_block_policy_mav_dummy"
+ "enableHomeKitTimer"
+ "enableHomeKitTimer:"
+ "findMyPencilScanActive"
+ "getHomeKitBtLoad"
+ "getHomeKitBtLoad xpc_reply is NULL"
+ "getHomeKitBtLoad:"
+ "getLeDiscoveryScanState"
+ "getLeDiscoveryScanUseCase"
+ "handleBTLeDiscoveryScanStateChange"
+ "handleBTLeDiscoveryScanStateChange - Scan %s, Use Case %s"
+ "handleLeDiscoveryScanStateChange:"
+ "homeKitReportingTimer"
+ "kWCMBTLeDiscoveryScan_State"
+ "kWCMBTLeDiscoveryScan_UseCase"
+ "kWRMHomeKitBtLoad"
+ "kWRMHomeKitDuration"
+ "kWRMHomeKitEnable"
+ "mCurrentBtLoad"
+ "mLeDiscoveryScanState"
+ "mLeDiscoveryScanUseCase"
+ "mMaximumBtLoad"
+ "scheduledTimerWithTimeInterval:target:selector:userInfo:repeats:"
+ "sendWirelessBtLoad Load:%u"
+ "sendWirelessBtLoad:"
+ "setHomeKitReportingTimer:"
+ "startHomeKitTimer"
+ "startHomeKitTimer:"
+ "stopHomeKitTimer"
+ "timerHandler"
+ "timerHandler:"
+ "updateControllerSession:remove context for WRMHomeKit from UCMClientManager"
+ "updateWirelessBtLoad load: %u"
+ "updateWirelessBtLoad:"
- "Setting TDD profile for 2.4GHz -pencilCoexActive || threadActive is (%d || %d)"

```
