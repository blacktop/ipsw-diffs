## AppleAVE2FW_H14G.im4p

> `Firmware/ave/AppleAVE2FW_H14G.im4p`

```diff

-  __TEXT.__text: 0xe1e80
+  __TEXT.__text: 0xe1eac
   __TEXT.__const: 0x1f014
   __TEXT.__cstring: 0x14b47
   __TEXT.__init_offsets: 0x0
Sections:
~ __TEXT.__const : content changed
~ __TEXT.__cstring : content changed
~ __DATA._rtk_patchbay : content changed
~ __DATA.__data : content changed
~ __DATA._rtk_mtab : content changed
~ __DATA.__const : content changed
Functions:
~ __ZN14CAVCController14ConfigureMCPUsEPK18AVE_PICMGMT_PARAMSPK12_S_AVC_Slice : 5972 -> 5956
~ __ZN14CAVCController19GetSliceHeaderForFWEPK12_S_AVC_SliceyiPhPji : 908 -> 904
~ __ZN14CAVCController19CollectDataFromCpusEb : 4060 -> 4108
~ __ZN14CAVCController24CollectDataFromTranscodeEP30CAVEControllerTranscodeDoneCmd : 2008 -> 2000
~ __ZN20CAVECommonController20processLowResMeStatsEjji : 1264 -> 1244
~ __ZN15CHEVCController19CollectDataFromCpusEb : 3336 -> 3320
~ __ZN15CHEVCController14ConfigureMCPUsEPK18AVE_PICMGMT_PARAMS : 21312 -> 21328
~ __ZN17CMultiPassControl24MpFinalPassSceneBitratesEfb : 6164 -> 6168
~ __ZN17CAVEPriorityQueue16UnregisterClientEy : 612 -> 616
~ __ZNK17CAVEPriorityQueue17GetClientPriorityEyPi : 284 -> 288
~ __ZN17CAVEPriorityQueue17SetClientPriorityEyi : 296 -> 300
~ __ZN17CAVEPriorityQueue22SetClientUseFirmwareRCEyb : 296 -> 300
~ __ZN17CAVEPriorityQueue7EnqueueEyyyjPvPN10CAVEClient9FrameInfoEj : 668 -> 660
~ __ZN17CAVEPriorityQueue5FlushEyyP15sCmdInformation : 756 -> 768
~ __ZN17CAVEPriorityQueue8CompleteEyj19_E_Proc_Mode_Queues : 440 -> 428
~ __ZN17CAVEPriorityQueue8ConvertPEyj19_E_Proc_Mode_Queues : 464 -> 468
~ _IOProcessorChannelCreate : 268 -> 260
~ sub_b8c84 -> sub_b8c8c : 868 -> 844
~ __ZN4CFSM12PostCallbackEPviPFvS0_iE : 804 -> 816
~ __ZN9CTaskPool17TerminateCallbackEmPv : 392 -> 404
~ __ZN9CTaskPool9TerminateEP11_rtk_thread : 304 -> 308
~ __ZN9CTaskPool8runUntilEv : 156 -> 164
~ __ZNK9CTaskPool4InfoEv : 416 -> 400
~ __ZN9CIOObject4TaskEv : 1328 -> 1336
~ __ZN15CChannelManager10UnregisterEPv : 392 -> 404
~ __Z17FakeChannelCreateP7CObjectiii : 3412 -> 3420
~ __Z27FakeChannelManagerTargetGetPKc : 132 -> 152
~ __Z25FakeChannelIndexTargetGetPKc : 132 -> 152
~ __Z25FakeChannelManagerHostGetPKc : 132 -> 152
~ __Z23FakeChannelIndexHostGetPKc : 132 -> 152
~ __Z17RealChannelCreateP7CObjectmP23ffwIOPChannelDescriptorbi : 2208 -> 2216
~ __Z14RealChannelGetPKcPP15CChannelManagerPm : 176 -> 184
~ sub_d23c4 -> sub_d2444 : 104 -> 88
~ sub_d242c -> sub_d249c : 468 -> 452
~ sub_d2600 -> sub_d2660 : 764 -> 740
~ sub_d28fc -> sub_d2944 : 84 -> 68
~ sub_d2950 -> sub_d2988 : 248 -> 244
~ sub_d2ff4 -> sub_d3028 : 876 -> 872
~ sub_d4f68 -> sub_d4f98 : 176 -> 180
~ sub_d664c -> sub_d6680 : 280 -> 284
~ __ZN7RTKHeap9addToPoolEPvm : 496 -> 500
~ sub_d6fe0 -> sub_d701c : 228 -> 244
~ sub_d719c -> sub_d71e8 : 168 -> 236
~ sub_d7244 -> sub_d72d4 : 244 -> 212
~ _RTK_stack_guard_free : 168 -> 164
~ sub_d9774 -> sub_d97e0 : 240 -> 244
~ sub_d99e8 -> sub_d9a58 : 412 -> 408
~ sub_daee4 -> sub_daf50 : 2784 -> 2740
~ sub_dc674 -> sub_dc6b4 : 432 -> 436
~ sub_dca14 -> sub_dca58 : 1884 -> 1836
~ sub_dd4c4 -> sub_dd4d8 : 552 -> 556
~ sub_de1d4 -> sub_de1ec : 172 -> 168
~ sub_e1198 -> sub_e11ac : 2564 -> 2588
~ sub_e1d3c -> sub_e1d68 : 324 -> 332
CStrings:
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.VBnlrw/Sources/AppleAVE2FW/External/Algorithm/RateControl.cpp"
+ "Caller is /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.VBnlrw/Sources/AppleAVE2FW/External/Algorithm/RateControl.cpp:855"
+ "Caller is /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.VBnlrw/Sources/AppleAVE2FW/External/Algorithm/RateControl.cpp:860"
+ "Caller is /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.VBnlrw/Sources/AppleAVE2FW/External/Algorithm/RateControl.cpp:901"
+ "Caller is /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.VBnlrw/Sources/AppleAVE2FW/External/Algorithm/RateControl.cpp:913"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.jAk0EN/Sources/AppleAVE2FW/External/Algorithm/RateControl.cpp"
- "Caller is /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.jAk0EN/Sources/AppleAVE2FW/External/Algorithm/RateControl.cpp:855"
- "Caller is /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.jAk0EN/Sources/AppleAVE2FW/External/Algorithm/RateControl.cpp:860"
- "Caller is /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.jAk0EN/Sources/AppleAVE2FW/External/Algorithm/RateControl.cpp:901"
- "Caller is /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.jAk0EN/Sources/AppleAVE2FW/External/Algorithm/RateControl.cpp:913"

```
