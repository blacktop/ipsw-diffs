## libCommCenterMCommandDrivers.dylib

> `/System/Library/Frameworks/CoreTelephony.framework/Support/libCommCenterMCommandDrivers.dylib`

```diff

-13169.2.1.2.0
-  __TEXT.__text: 0x219b2c
-  __TEXT.__auth_stubs: 0x2c90
+13171.6.0.0.0
+  __TEXT.__text: 0x21a40c
+  __TEXT.__auth_stubs: 0x2cb0
   __TEXT.__init_offsets: 0x8
-  __TEXT.__const: 0x26080
-  __TEXT.__cstring: 0xc050
-  __TEXT.__gcc_except_tab: 0x1e470
-  __TEXT.__oslogstring: 0x19b5f
-  __TEXT.__unwind_info: 0xeb28
+  __TEXT.__const: 0x26090
+  __TEXT.__cstring: 0xc058
+  __TEXT.__gcc_except_tab: 0x1e4ec
+  __TEXT.__oslogstring: 0x19c32
+  __TEXT.__unwind_info: 0xeb58
   __DATA_CONST.__got: 0x4e0
-  __DATA_CONST.__const: 0xb358
-  __AUTH_CONST.__auth_got: 0x1650
+  __DATA_CONST.__const: 0xb380
+  __AUTH_CONST.__auth_got: 0x1660
   __AUTH_CONST.__const: 0x21238
   __AUTH_CONST.__cfstring: 0x220
   __DATA.__data: 0x28

   - /usr/lib/libTelephonyCapabilities.dylib
   - /usr/lib/libTelephonyUtilDynamic.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: 90C630D3-C3A8-36ED-BC3B-2A8E1B9F713E
-  Functions: 12393
-  Symbols:   37779
-  CStrings:  4259
+  UUID: 36C7701B-EBC6-3555-A953-D93264B860E4
+  Functions: 12398
+  Symbols:   37795
+  CStrings:  4266
 
Symbols:
+ GCC_except_table149
+ GCC_except_table173
+ GCC_except_table379
+ GCC_except_table438
+ __ZN22QMIStewieCommandDriver23getFringeCoverageStatusEONSt3__18functionIFvbNS0_8optionalIbEEEEE
+ __ZN3tlv6parseVIN3sft3tlv14FringeCoverageEEET_RPKhi
+ __ZN9DataUtils20coalescePortInfoListERNSt3__16vectorI26DataDownlinkFilterPortInfoNS0_9allocatorIS2_EEEEm
+ __ZNK3ctu20SharedSynchronizableI22QMIStewieCommandDriverE7executeIZNS1_23getFringeCoverageStatusEONSt3__18functionIFvbNS4_8optionalIbEEEEEE3$_0EEvOT_
+ __ZNSt3__110__function12__value_funcIFvbNS_8optionalIbEEEEC2B9nqe210106EOS5_
+ __ZNSt3__110__function12__value_funcIFvbNS_8optionalIbEEEED2B9nqe210106Ev
+ __ZNSt3__110unique_ptrIZN22QMIStewieCommandDriver23getFringeCoverageStatusEONS_8functionIFvbNS_8optionalIbEEEEEE3$_0NS_14default_deleteIS8_EEED1B9nqe210106Ev
+ __ZNSt3__110unique_ptrIZNK3ctu20SharedSynchronizableI22QMIStewieCommandDriverE15execute_wrappedIZNS3_23getFringeCoverageStatusEONS_8functionIFvbNS_8optionalIbEEEEEE3$_0EEvOT_EUlvE_NS_14default_deleteISF_EEED1B9nqe210106Ev
+ __ZNSt3__120__shared_ptr_emplaceIZN22QMIStewieCommandDriver23getFringeCoverageStatusEONS_8functionIFvbNS_8optionalIbEEEEEE3$_1NS_9allocatorIS8_EEE16__on_zero_sharedEv
+ __ZNSt3__120__shared_ptr_emplaceIZN22QMIStewieCommandDriver23getFringeCoverageStatusEONS_8functionIFvbNS_8optionalIbEEEEEE3$_1NS_9allocatorIS8_EEE21__on_zero_shared_weakEv
+ __ZNSt3__120__shared_ptr_emplaceIZN22QMIStewieCommandDriver23getFringeCoverageStatusEONS_8functionIFvbNS_8optionalIbEEEEEE3$_1NS_9allocatorIS8_EEED0Ev
+ __ZNSt3__120__shared_ptr_emplaceIZN22QMIStewieCommandDriver23getFringeCoverageStatusEONS_8functionIFvbNS_8optionalIbEEEEEE3$_1NS_9allocatorIS8_EEED1Ev
+ __ZNSt3__16__sortIRNS_6__lessIttEEPtEEvT0_S5_T_
+ __ZNSt3__16vectorI26DataDownlinkFilterPortInfoNS_9allocatorIS1_EEE20__throw_length_errorB9nqe210106Ev
+ __ZTINSt3__120__shared_ptr_emplaceIZN22QMIStewieCommandDriver23getFringeCoverageStatusEONS_8functionIFvbNS_8optionalIbEEEEEE3$_1NS_9allocatorIS8_EEEE
+ __ZTSNSt3__120__shared_ptr_emplaceIZN22QMIStewieCommandDriver23getFringeCoverageStatusEONS_8functionIFvbNS_8optionalIbEEEEEE3$_1NS_9allocatorIS8_EEEE
+ __ZTVNSt3__120__shared_ptr_emplaceIZN22QMIStewieCommandDriver23getFringeCoverageStatusEONS_8functionIFvbNS_8optionalIbEEEEEE3$_1NS_9allocatorIS8_EEEE
+ __ZZN8dispatch5asyncIZNK3ctu20SharedSynchronizableI22QMIStewieCommandDriverE15execute_wrappedIZNS3_23getFringeCoverageStatusEONSt3__18functionIFvbNS6_8optionalIbEEEEEE3$_0EEvOT_EUlvE_EEvP16dispatch_queue_sNS6_10unique_ptrISE_NS6_14default_deleteISE_EEEEENUlPvE_8__invokeESN_
+ ____ZN22QMIStewieCommandDriver4sendIN3sft23GetFringeCoverageStatus7RequestEZNS_23getFringeCoverageStatusEONSt3__18functionIFvbNS4_8optionalIbEEEEEE3$_1EEvRKT_OT0__block_invoke
+ ____ZNO3qmi6Client9SendProxy8callbackIRKN3sft23GetFringeCoverageStatus8ResponseEEEOS1_U13block_pointerFvT_E_block_invoke
+ ___copy_helper_block_e8_32c119_ZTSNSt3__110shared_ptrIZN22QMIStewieCommandDriver23getFringeCoverageStatusEONS_8functionIFvbNS_8optionalIbEEEEEE3$_1EE
+ ___destroy_helper_block_e8_32c119_ZTSNSt3__110shared_ptrIZN22QMIStewieCommandDriver23getFringeCoverageStatusEONS_8functionIFvbNS_8optionalIbEEEEEE3$_1EE
- GCC_except_table182
- GCC_except_table272
- GCC_except_table317
- GCC_except_table358
- GCC_except_table374
- __ZN22QMIStewieCommandDriver23triggerFringeMitigationEONSt3__18functionIFvbEEE
- __ZNK3ctu20SharedSynchronizableI22QMIStewieCommandDriverE7executeIZNS1_23triggerFringeMitigationEONSt3__18functionIFvbEEEE3$_0EEvOT_
- __ZNSt3__110unique_ptrIZN22QMIStewieCommandDriver23triggerFringeMitigationEONS_8functionIFvbEEEE3$_0NS_14default_deleteIS6_EEED1B9nqe210106Ev
- __ZNSt3__110unique_ptrIZNK3ctu20SharedSynchronizableI22QMIStewieCommandDriverE15execute_wrappedIZNS3_23triggerFringeMitigationEONS_8functionIFvbEEEE3$_0EEvOT_EUlvE_NS_14default_deleteISD_EEED1B9nqe210106Ev
- __ZNSt3__120__shared_ptr_emplaceIZN22QMIStewieCommandDriver23triggerFringeMitigationEONS_8functionIFvbEEEE3$_1NS_9allocatorIS6_EEE16__on_zero_sharedEv
- __ZNSt3__120__shared_ptr_emplaceIZN22QMIStewieCommandDriver23triggerFringeMitigationEONS_8functionIFvbEEEE3$_1NS_9allocatorIS6_EEE21__on_zero_shared_weakEv
- __ZNSt3__120__shared_ptr_emplaceIZN22QMIStewieCommandDriver23triggerFringeMitigationEONS_8functionIFvbEEEE3$_1NS_9allocatorIS6_EEED0Ev
- __ZNSt3__120__shared_ptr_emplaceIZN22QMIStewieCommandDriver23triggerFringeMitigationEONS_8functionIFvbEEEE3$_1NS_9allocatorIS6_EEED1Ev
- __ZTINSt3__120__shared_ptr_emplaceIZN22QMIStewieCommandDriver23triggerFringeMitigationEONS_8functionIFvbEEEE3$_1NS_9allocatorIS6_EEEE
- __ZTSNSt3__120__shared_ptr_emplaceIZN22QMIStewieCommandDriver23triggerFringeMitigationEONS_8functionIFvbEEEE3$_1NS_9allocatorIS6_EEEE
- __ZTVNSt3__120__shared_ptr_emplaceIZN22QMIStewieCommandDriver23triggerFringeMitigationEONS_8functionIFvbEEEE3$_1NS_9allocatorIS6_EEEE
- __ZZN8dispatch5asyncIZNK3ctu20SharedSynchronizableI22QMIStewieCommandDriverE15execute_wrappedIZNS3_23triggerFringeMitigationEONSt3__18functionIFvbEEEE3$_0EEvOT_EUlvE_EEvP16dispatch_queue_sNS6_10unique_ptrISC_NS6_14default_deleteISC_EEEEENUlPvE_8__invokeESL_
- ____ZN22QMIStewieCommandDriver4sendIN3sft23TriggerFringeMitigation7RequestEZNS_23triggerFringeMitigationEONSt3__18functionIFvbEEEE3$_1EEvRKT_OT0__block_invoke
- ___copy_helper_block_e8_32c103_ZTSNSt3__110shared_ptrIZN22QMIStewieCommandDriver23triggerFringeMitigationEONS_8functionIFvbEEEE3$_1EE
- ___destroy_helper_block_e8_32c103_ZTSNSt3__110shared_ptrIZN22QMIStewieCommandDriver23triggerFringeMitigationEONS_8functionIFvbEEEE3$_1EE
CStrings:
+ "#D Sending GetFringeCoverageStatus"
+ "#D ranged port[%zu].port=%u, range=%u"
+ "#I %s portListNumber=%zu"
+ "#I Coalesced Internet portInfoList from size:%zu to size:%zu"
+ "#I Downlink %s filter Rule #%d port=%d, range=%d, totalNum %d"
+ "#I GetFringeCoverageStatus request succeeded"
+ "#I getOpenPortsExt failed on pdpId %d, fIpFamily %d protocol %s"
+ "#I original port[%zu]=%u"
+ "#I ranged portInfoList size=%zu"
+ "/Library/Caches/com.apple.xbs/19355516-4B0F-496A-B40B-C52CFE6DFD57/TemporaryDirectory.B6Zc89/Sources/CoreTelephony/CSI/Modules/CallModule/EurekaC2KCallFormatter.cpp"
+ "/Library/Caches/com.apple.xbs/19355516-4B0F-496A-B40B-C52CFE6DFD57/TemporaryDirectory.B6Zc89/Sources/CoreTelephony/CommCenter/CommCenterCommandDrivers/AQM/QMIAQMCommandDriver.cpp"
+ "/Library/Caches/com.apple.xbs/19355516-4B0F-496A-B40B-C52CFE6DFD57/TemporaryDirectory.B6Zc89/Sources/CoreTelephony/CommCenter/CommCenterCommandDrivers/Activation/QMIActivationCommandDriver.cpp"
+ "/Library/Caches/com.apple.xbs/19355516-4B0F-496A-B40B-C52CFE6DFD57/TemporaryDirectory.B6Zc89/Sources/CoreTelephony/CommCenter/CommCenterCommandDrivers/Awd/QMIAwdCommandDriver.cpp"
+ "/Library/Caches/com.apple.xbs/19355516-4B0F-496A-B40B-C52CFE6DFD57/TemporaryDirectory.B6Zc89/Sources/CoreTelephony/CommCenter/CommCenterCommandDrivers/Data/QMI/Context/QMIDataContextDriver.cpp"
+ "/Library/Caches/com.apple.xbs/19355516-4B0F-496A-B40B-C52CFE6DFD57/TemporaryDirectory.B6Zc89/Sources/CoreTelephony/CommCenter/CommCenterCommandDrivers/Data/QMI/Context/QMIDataContextIP.cpp"
+ "/Library/Caches/com.apple.xbs/19355516-4B0F-496A-B40B-C52CFE6DFD57/TemporaryDirectory.B6Zc89/Sources/CoreTelephony/CommCenter/CommCenterCommandDrivers/Data/QMI/Context/QMIDataContextIPAggregator.cpp"
+ "/Library/Caches/com.apple.xbs/19355516-4B0F-496A-B40B-C52CFE6DFD57/TemporaryDirectory.B6Zc89/Sources/CoreTelephony/CommCenter/CommCenterCommandDrivers/Data/QMI/Context/QMIDataContextIPBase.cpp"
+ "/Library/Caches/com.apple.xbs/19355516-4B0F-496A-B40B-C52CFE6DFD57/TemporaryDirectory.B6Zc89/Sources/CoreTelephony/CommCenter/CommCenterCommandDrivers/Data/QMI/Context/QMIQOSClientIP.cpp"
+ "/Library/Caches/com.apple.xbs/19355516-4B0F-496A-B40B-C52CFE6DFD57/TemporaryDirectory.B6Zc89/Sources/CoreTelephony/CommCenter/CommCenterCommandDrivers/DataSubscription/QMIDataSubscriptionCommandDriver.cpp"
+ "/Library/Caches/com.apple.xbs/19355516-4B0F-496A-B40B-C52CFE6DFD57/TemporaryDirectory.B6Zc89/Sources/CoreTelephony/CommCenter/CommCenterCommandDrivers/Dormancy/QMIDormancyCommandDriver.cpp"
+ "/Library/Caches/com.apple.xbs/19355516-4B0F-496A-B40B-C52CFE6DFD57/TemporaryDirectory.B6Zc89/Sources/CoreTelephony/CommCenter/CommCenterCommandDrivers/MavCommandDriversFactory.cpp"
+ "/Library/Caches/com.apple.xbs/19355516-4B0F-496A-B40B-C52CFE6DFD57/TemporaryDirectory.B6Zc89/Sources/CoreTelephony/CommCenter/CommCenterCommandDrivers/QMIClientPool.cpp"
+ "/Library/Caches/com.apple.xbs/19355516-4B0F-496A-B40B-C52CFE6DFD57/TemporaryDirectory.B6Zc89/Sources/CoreTelephony/CommCenter/CommCenterCommandDrivers/QMIClientPool.h"
+ "/Library/Caches/com.apple.xbs/19355516-4B0F-496A-B40B-C52CFE6DFD57/TemporaryDirectory.B6Zc89/Sources/CoreTelephony/CommCenter/CommCenterCommandDrivers/STK/QMI_STK_Helper.cpp"
+ "/Library/Caches/com.apple.xbs/19355516-4B0F-496A-B40B-C52CFE6DFD57/TemporaryDirectory.B6Zc89/Sources/CoreTelephony/CommCenter/CommCenterCommandDrivers/SignalStrength/QMISignalStrengthCommandDriver.cpp"
+ "/Library/Caches/com.apple.xbs/19355516-4B0F-496A-B40B-C52CFE6DFD57/TemporaryDirectory.B6Zc89/Sources/CoreTelephony/CommCenter/CommCenterCommandDrivers/Sim/EURSubscriberSimCommandDriver.cpp"
+ "/Library/Caches/com.apple.xbs/19355516-4B0F-496A-B40B-C52CFE6DFD57/TemporaryDirectory.B6Zc89/Sources/CoreTelephony/CommCenter/CommCenterCommandDrivers/Stewie/QMI/QMIStewieCommandDriver.cpp"
+ "Failed to execute GetFringeCoverageStatus. Client is not ready"
+ "Failed to execute GetFringeCoverageStatus. Error code:0x%x (%s)"
+ "TCP"
+ "UDP"
- "#I Downlink IP filter Rule #%d port=%d, totalNum %d"
- "#I TriggerFringeMitigation succeeded"
- "#I getOpenPortsExt failed on pdpId %d, fIpFamily %d protocol %d"
- "#I portListNumber = %d"
- "/Library/Caches/com.apple.xbs/045E7A93-F69E-4EC4-8115-7DC73E453BCA/TemporaryDirectory.2ssem7/Sources/CoreTelephony/CSI/Modules/CallModule/EurekaC2KCallFormatter.cpp"
- "/Library/Caches/com.apple.xbs/045E7A93-F69E-4EC4-8115-7DC73E453BCA/TemporaryDirectory.2ssem7/Sources/CoreTelephony/CommCenter/CommCenterCommandDrivers/AQM/QMIAQMCommandDriver.cpp"
- "/Library/Caches/com.apple.xbs/045E7A93-F69E-4EC4-8115-7DC73E453BCA/TemporaryDirectory.2ssem7/Sources/CoreTelephony/CommCenter/CommCenterCommandDrivers/Activation/QMIActivationCommandDriver.cpp"
- "/Library/Caches/com.apple.xbs/045E7A93-F69E-4EC4-8115-7DC73E453BCA/TemporaryDirectory.2ssem7/Sources/CoreTelephony/CommCenter/CommCenterCommandDrivers/Awd/QMIAwdCommandDriver.cpp"
- "/Library/Caches/com.apple.xbs/045E7A93-F69E-4EC4-8115-7DC73E453BCA/TemporaryDirectory.2ssem7/Sources/CoreTelephony/CommCenter/CommCenterCommandDrivers/Data/QMI/Context/QMIDataContextDriver.cpp"
- "/Library/Caches/com.apple.xbs/045E7A93-F69E-4EC4-8115-7DC73E453BCA/TemporaryDirectory.2ssem7/Sources/CoreTelephony/CommCenter/CommCenterCommandDrivers/Data/QMI/Context/QMIDataContextIP.cpp"
- "/Library/Caches/com.apple.xbs/045E7A93-F69E-4EC4-8115-7DC73E453BCA/TemporaryDirectory.2ssem7/Sources/CoreTelephony/CommCenter/CommCenterCommandDrivers/Data/QMI/Context/QMIDataContextIPAggregator.cpp"
- "/Library/Caches/com.apple.xbs/045E7A93-F69E-4EC4-8115-7DC73E453BCA/TemporaryDirectory.2ssem7/Sources/CoreTelephony/CommCenter/CommCenterCommandDrivers/Data/QMI/Context/QMIDataContextIPBase.cpp"
- "/Library/Caches/com.apple.xbs/045E7A93-F69E-4EC4-8115-7DC73E453BCA/TemporaryDirectory.2ssem7/Sources/CoreTelephony/CommCenter/CommCenterCommandDrivers/Data/QMI/Context/QMIQOSClientIP.cpp"
- "/Library/Caches/com.apple.xbs/045E7A93-F69E-4EC4-8115-7DC73E453BCA/TemporaryDirectory.2ssem7/Sources/CoreTelephony/CommCenter/CommCenterCommandDrivers/DataSubscription/QMIDataSubscriptionCommandDriver.cpp"
- "/Library/Caches/com.apple.xbs/045E7A93-F69E-4EC4-8115-7DC73E453BCA/TemporaryDirectory.2ssem7/Sources/CoreTelephony/CommCenter/CommCenterCommandDrivers/Dormancy/QMIDormancyCommandDriver.cpp"
- "/Library/Caches/com.apple.xbs/045E7A93-F69E-4EC4-8115-7DC73E453BCA/TemporaryDirectory.2ssem7/Sources/CoreTelephony/CommCenter/CommCenterCommandDrivers/MavCommandDriversFactory.cpp"
- "/Library/Caches/com.apple.xbs/045E7A93-F69E-4EC4-8115-7DC73E453BCA/TemporaryDirectory.2ssem7/Sources/CoreTelephony/CommCenter/CommCenterCommandDrivers/QMIClientPool.cpp"
- "/Library/Caches/com.apple.xbs/045E7A93-F69E-4EC4-8115-7DC73E453BCA/TemporaryDirectory.2ssem7/Sources/CoreTelephony/CommCenter/CommCenterCommandDrivers/QMIClientPool.h"
- "/Library/Caches/com.apple.xbs/045E7A93-F69E-4EC4-8115-7DC73E453BCA/TemporaryDirectory.2ssem7/Sources/CoreTelephony/CommCenter/CommCenterCommandDrivers/STK/QMI_STK_Helper.cpp"
- "/Library/Caches/com.apple.xbs/045E7A93-F69E-4EC4-8115-7DC73E453BCA/TemporaryDirectory.2ssem7/Sources/CoreTelephony/CommCenter/CommCenterCommandDrivers/SignalStrength/QMISignalStrengthCommandDriver.cpp"
- "/Library/Caches/com.apple.xbs/045E7A93-F69E-4EC4-8115-7DC73E453BCA/TemporaryDirectory.2ssem7/Sources/CoreTelephony/CommCenter/CommCenterCommandDrivers/Sim/EURSubscriberSimCommandDriver.cpp"
- "/Library/Caches/com.apple.xbs/045E7A93-F69E-4EC4-8115-7DC73E453BCA/TemporaryDirectory.2ssem7/Sources/CoreTelephony/CommCenter/CommCenterCommandDrivers/Stewie/QMI/QMIStewieCommandDriver.cpp"
- "Failed to execute TriggerFringeMitigation. Client is not ready"
- "Failed to execute TriggerFringeMitigation. Error code:0x%x (%s)"

```
