## CommCenter

> `/System/Library/Frameworks/CoreTelephony.framework/Support/CommCenter`

### Sections with Same Size but Changed Content

- `__TEXT.__init_offsets`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-13478.2.0.0.0
-  __TEXT.__text: 0x75d01c
-  __TEXT.__auth_stubs: 0x71f0
-  __TEXT.__objc_stubs: 0xbbe0
+13482.0.0.0.0
+  __TEXT.__text: 0x761f8c
+  __TEXT.__auth_stubs: 0x7250
+  __TEXT.__objc_stubs: 0xbc20
   __TEXT.__init_offsets: 0x184
-  __TEXT.__objc_methlist: 0x6d34
-  __TEXT.__const: 0x96abc
-  __TEXT.__cstring: 0x227e1
-  __TEXT.__gcc_except_tab: 0x8b1f8
-  __TEXT.__oslogstring: 0x87744
+  __TEXT.__objc_methlist: 0x6d44
+  __TEXT.__const: 0x9696c
+  __TEXT.__cstring: 0x22817
+  __TEXT.__gcc_except_tab: 0x8b85c
+  __TEXT.__oslogstring: 0x8791a
   __TEXT.__objc_classname: 0x18a2
-  __TEXT.__objc_methname: 0x11feb
+  __TEXT.__objc_methname: 0x12040
   __TEXT.__objc_methtype: 0xe3e6
   __TEXT.__ustring: 0x3e2
-  __TEXT.__unwind_info: 0x2a2b0
-  __DATA_CONST.__const: 0x77950
-  __DATA_CONST.__cfstring: 0xbce0
+  __TEXT.__unwind_info: 0x2a5d0
+  __DATA_CONST.__const: 0x77c20
+  __DATA_CONST.__cfstring: 0xbd40
   __DATA_CONST.__objc_classlist: 0x260
   __DATA_CONST.__objc_catlist: 0x88
   __DATA_CONST.__objc_protolist: 0x310

   __DATA_CONST.__objc_dictobj: 0x50
   __DATA_CONST.__linkguard: 0x1b
   __DATA_CONST.__objc_intobj: 0x60
-  __DATA_CONST.__auth_got: 0x3910
+  __DATA_CONST.__auth_got: 0x3940
   __DATA_CONST.__got: 0x1ea8
   __DATA_CONST.__auth_ptr: 0x30
   __DATA.__objc_const: 0x8050
-  __DATA.__objc_selrefs: 0x4a00
+  __DATA.__objc_selrefs: 0x4a10
   __DATA.__objc_ivar: 0x354
   __DATA.__objc_data: 0x17c0
   __DATA.__data: 0x3498

   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libxml2.2.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 32769
-  Symbols:   2971
-  CStrings:  19583
+  Functions: 32867
+  Symbols:   2977
+  CStrings:  19601
 
Symbols:
+ __ZN10subscriber8asStringENS_15HardwareSimSlotE
+ __ZN12capabilities2ct25supportsBacklightServicesEv
+ __ZNK8CallInfo12uuidAsStringEv
+ _nw_parameters_set_prohibited_interface_subtypes
+ _xpc_array_create_empty
+ _xpc_array_set_uint64
CStrings:
+ " qs-properties: "
+ " qs: "
+ "%s%s%s%sinvalid sms-mode received - %d, ignored"
+ ", sms-mode:"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.m4D9TN/Sources/CoreTelephony/CSI/Modules/CallModule/CallStateModel.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.m4D9TN/Sources/CoreTelephony/CSI/Modules/Data/Source/APNStorage.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.m4D9TN/Sources/CoreTelephony/CSI/Modules/Data/Source/DataAPNSettings.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.m4D9TN/Sources/CoreTelephony/CSI/Modules/Data/Source/DataCollocationCommon.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.m4D9TN/Sources/CoreTelephony/CSI/Modules/Data/Source/DataConnectionAgent.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.m4D9TN/Sources/CoreTelephony/CSI/Modules/Data/Source/DataConnectionIMS.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.m4D9TN/Sources/CoreTelephony/CSI/Modules/Data/Source/DataConnectionInterface.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.m4D9TN/Sources/CoreTelephony/CSI/Modules/Data/Source/DataPDPActivator.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.m4D9TN/Sources/CoreTelephony/CSI/Modules/Data/Source/DataServiceController.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.m4D9TN/Sources/CoreTelephony/CSI/Modules/Data/Source/DataiRatControlleriOSBase.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.m4D9TN/Sources/CoreTelephony/CSI/Modules/Data/Source/IPCU_CellProfile.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.m4D9TN/Sources/CoreTelephony/CSI/Modules/Data/Source/IWLANDataContext.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.m4D9TN/Sources/CoreTelephony/CSI/Modules/SystemObserver/PowerObserver.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.m4D9TN/Sources/CoreTelephony/CSI/Source/Common/CSIPersistentProperties.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.m4D9TN/Sources/CoreTelephony/CSI/Source/PlatformSpecific/CSIFlatFileNvpStore.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.m4D9TN/Sources/CoreTelephony/CommCenter/Location/CTLocationBasedCountryDetermination.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.m4D9TN/Sources/CoreTelephony/CommCenter/Source/CSI/DarwinPDPConfig.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.m4D9TN/Sources/CoreTelephony/CommCenter/Source/DarwinPDPManager.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.m4D9TN/Sources/CoreTelephony/CommCenter/Source/Startup/StartupActions.cpp"
+ "13482"
+ "13482~72"
+ "Bundle ID %@ is not registered for state events, skipping initial push"
+ "Client %@ registered for quickSwitchStateDidChange, pushing current state"
+ "Could not register for display status updates"
+ "DATA::  \t\tCTDataPathEvaluatorHolder: id=%u, i=%{public}s, d=%{public}s, a=%{public}s, pe=%{bool}d, watch=%{bool}d observers vector size = %lu"
+ "Disconnected: No call found for uuid %{public,uuid_t}.16P. Trying to send STOP"
+ "Display is now %s"
+ "Failed to push initial state: %@"
+ "Getting the display status: %{bool}d"
+ "IPv6ServiceHandover: already exists"
+ "Null IMS call command driver"
+ "Proceeding dropped: IMSDialBBCallResponse but no queued STK-dialed IMS call"
+ "QuickSwitchStateController not available to push initial state"
+ "SendBBIMSCallStatusResponse dropped: null IMS driver for STK call %{public,uuid_t}.16P"
+ "SendBBIMSCallStatusResponse: StartMO failed for STK call %{public,uuid_t}.16P, ending on IpT"
+ "TextStreamDetected: declining RTT upgrade — Carrier does not support TTY over IMS"
+ "TextStreamDetected: failed to decline RTT upgrade: No IMS call object found for uuid %{public,uuid_t}.16P"
+ "fanoutWithMessageReference"
+ "fanoutWithoutMessageReference"
+ "handleQuickSwitchSelectorRegistration:connection:"
+ "is-service-included"
+ "is-service-included:"
+ "isBundleIDRegisteredForStateEvents called on macOS - returning false"
+ "isServiceIncluded"
+ "isServiceIncluded:"
+ "qs-properties"
+ "qsProperties"
+ "remoteObjectProxyWithErrorHandler:"
+ "selectiveDelivery"
+ "sms-mode"
+ "smsMode"
+ "smsMode:"
- "%s%s%s: VinylCapability==kUnknown on China SKU with 2P+2E mode support. Hack cannot distinguish 4FF & eSIM - suppress slot info completely"
- "%s%sExpel 4FF SIM %s from completely hidden %s"
- "%s%sfPhySlot is outside of HardwareSimSlot range!!!"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.iqTMSA/Sources/CoreTelephony/CSI/Modules/CallModule/CallStateModel.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.iqTMSA/Sources/CoreTelephony/CSI/Modules/Data/Source/APNStorage.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.iqTMSA/Sources/CoreTelephony/CSI/Modules/Data/Source/DataAPNSettings.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.iqTMSA/Sources/CoreTelephony/CSI/Modules/Data/Source/DataCollocationCommon.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.iqTMSA/Sources/CoreTelephony/CSI/Modules/Data/Source/DataConnectionAgent.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.iqTMSA/Sources/CoreTelephony/CSI/Modules/Data/Source/DataConnectionIMS.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.iqTMSA/Sources/CoreTelephony/CSI/Modules/Data/Source/DataConnectionInterface.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.iqTMSA/Sources/CoreTelephony/CSI/Modules/Data/Source/DataPDPActivator.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.iqTMSA/Sources/CoreTelephony/CSI/Modules/Data/Source/DataServiceController.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.iqTMSA/Sources/CoreTelephony/CSI/Modules/Data/Source/DataiRatControlleriOSBase.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.iqTMSA/Sources/CoreTelephony/CSI/Modules/Data/Source/IPCU_CellProfile.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.iqTMSA/Sources/CoreTelephony/CSI/Modules/Data/Source/IWLANDataContext.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.iqTMSA/Sources/CoreTelephony/CSI/Modules/SystemObserver/PowerObserver.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.iqTMSA/Sources/CoreTelephony/CSI/Source/Common/CSIPersistentProperties.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.iqTMSA/Sources/CoreTelephony/CSI/Source/PlatformSpecific/CSIFlatFileNvpStore.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.iqTMSA/Sources/CoreTelephony/CommCenter/Location/CTLocationBasedCountryDetermination.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.iqTMSA/Sources/CoreTelephony/CommCenter/Source/CSI/DarwinPDPConfig.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.iqTMSA/Sources/CoreTelephony/CommCenter/Source/DarwinPDPManager.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.iqTMSA/Sources/CoreTelephony/CommCenter/Source/Startup/StartupActions.cpp"
- "/cc/events/wifi_availability_info"
- "13478.2"
- "13478.2~176"
- "Could not register for screen blank notification"
- "DATA::  \t\tCTDataPathEvaluatorHolder: id=%u, i=%{public}s, d=%{public}s, a=%{public}s, pe=%{bool}d, observers vector size = %lu"
- "Disconnected dropped: No call found for uuid %{public,uuid_t}.16P. Trying to send STOP"
- "Getting the display status: %llu"
- "Proceeding dropped: IMSDialBBCallResponse but BBDialed call queue is empty"
- "RealHwdSimSlot::kFour"
- "RealHwdSimSlot::kOne"
- "RealHwdSimSlot::kThree"
- "RealHwdSimSlot::kTwo"
- "RealHwdSimSlot::kUnknown"
- "TextStreamDetected dropped: Carrier does not support TTY over IMS"
- "WiFi status (default route) changed: %s -> %s"
- "com.apple.springboard.hasBlankedScreen"
```
