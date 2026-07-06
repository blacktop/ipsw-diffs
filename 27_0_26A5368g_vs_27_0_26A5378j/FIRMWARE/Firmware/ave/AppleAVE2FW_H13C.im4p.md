## AppleAVE2FW_H13C.im4p

> `Firmware/ave/AppleAVE2FW_H13C.im4p`

```diff

-  __TEXT.__text: 0xfc7f0
+  __TEXT.__text: 0xfc88c
   __TEXT.__const: 0x228e4
   __TEXT.__cstring: 0x16298
   __TEXT.__init_offsets: 0x0
Sections:
~ __TEXT.__const : content changed
~ __TEXT.__cstring : content changed
~ __DATA._rtk_patchbay : content changed
~ __DATA.__data : content changed
~ __DATA._rtk_mtab : content changed
~ __DATA.__const : content changed
Functions:
~ __ZN14CAVCController14ConfigureMCPUsEPK18AVE_PICMGMT_PARAMSPK12_S_AVC_Slice : 6092 -> 6080
~ __ZN14CAVCController19GetSliceHeaderForFWEPK12_S_AVC_SliceyiPhPji : 908 -> 904
~ __ZN14CAVCController21CollectLrmeStatsMcoreEv : 584 -> 572
~ __ZN14CAVCController19CollectDataFromCpusEb : 4336 -> 4416
~ __ZN14CAVCController24CollectDataFromTranscodeEP30CAVEControllerTranscodeDoneCmd : 2040 -> 2032
~ __ZN20CAVECommonController20processLowResMeStatsEjji : 1264 -> 1244
~ __ZN15CHEVCController14ConfigureMCPUsEPK18AVE_PICMGMT_PARAMS : 26144 -> 26152
~ __ZN15CHEVCController21ProcessLRMEStatsMcoreEv : 10256 -> 10244
~ __ZN15CHEVCController28CollectDataFromCpusMultiCoreEv : 1668 -> 1672
~ __ZN17CMultiPassControl24MpFinalPassSceneBitratesEfb : 6164 -> 6168
~ __ZN17CAVEPriorityQueue16UnregisterClientEy : 612 -> 616
~ __ZNK17CAVEPriorityQueue17GetClientPriorityEyPi : 284 -> 288
~ __ZN17CAVEPriorityQueue17SetClientPriorityEyi : 296 -> 300
~ __ZN17CAVEPriorityQueue22SetClientUseFirmwareRCEyb : 300 -> 304
~ __ZN17CAVEPriorityQueue7EnqueueEyyyjPvPN10CAVEClient9FrameInfoEj : 668 -> 660
~ __ZN17CAVEPriorityQueue24GetCommandQueueToDequeueEy : 224 -> 228
~ __ZN17CAVEPriorityQueue5FlushEyyP15sCmdInformation : 756 -> 768
~ __ZN17CAVEPriorityQueue8CompleteEyj19_E_Proc_Mode_Queues : 440 -> 428
~ __ZN17CAVEPriorityQueue8ConvertPEyj19_E_Proc_Mode_Queues : 876 -> 880
~ _IOProcessorChannelCreate : 268 -> 260
~ sub_d2e28 -> sub_d2e4c : 868 -> 844
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
~ __Z20AVE_IOP_Config_pandav : 484 -> 488
~ sub_ed84c -> sub_ed8ec : 872 -> 868
~ __ZN7RTKHeap9addToPoolEPvm : 496 -> 500
~ sub_f182c -> sub_f18cc : 228 -> 244
~ sub_f19e8 -> sub_f1a98 : 168 -> 236
~ sub_f1a90 -> sub_f1b84 : 244 -> 212
~ _RTK_stack_guard_free : 168 -> 164
~ sub_f3e9c -> sub_f3f6c : 296 -> 292
~ sub_f4248 -> sub_f4314 : 412 -> 408
~ sub_f5744 -> sub_f580c : 2352 -> 2340
~ sub_f70cc -> sub_f7188 : 1884 -> 1836
~ _RTK_mbi_route_create : 612 -> 592
~ sub_fbb50 -> sub_fbbc8 : 2492 -> 2528
~ sub_fc6ac -> sub_fc748 : 324 -> 332
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
