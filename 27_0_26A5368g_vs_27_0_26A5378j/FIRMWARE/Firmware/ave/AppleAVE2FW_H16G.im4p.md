## AppleAVE2FW_H16G.im4p

> `Firmware/ave/AppleAVE2FW_H16G.im4p`

```diff

-  __TEXT.__text: 0x11113c
+  __TEXT.__text: 0x1111b8
   __TEXT.__const: 0x258b4
   __TEXT.__cstring: 0x17b74
   __TEXT.__init_offsets: 0x0
Sections:
~ __TEXT.__const : content changed
~ __TEXT.__cstring : content changed
~ __DATA._rtk_patchbay : content changed
~ __DATA.__data : content changed
~ __DATA._rtk_mtab : content changed
~ __DATA.__const : content changed
Functions:
~ __ZN14CAVCController14ConfigureMCPUsEPK18AVE_PICMGMT_PARAMSPK12_S_AVC_Slice : 6108 -> 6096
~ __ZN14CAVCController19GetSliceHeaderForFWEPK12_S_AVC_SliceyiPhPji : 908 -> 904
~ __ZN14CAVCController21CollectLrmeStatsMcoreEv : 584 -> 572
~ __ZN14CAVCController19CollectDataFromCpusEb : 4336 -> 4416
~ __ZN14CAVCController24CollectDataFromTranscodeEP30CAVEControllerTranscodeDoneCmd : 2040 -> 2032
~ __ZN20CAVECommonController20processLowResMeStatsEjji : 1264 -> 1244
~ __ZN15CHEVCController14ConfigureMCPUsEPK18AVE_PICMGMT_PARAMS : 21624 -> 21632
~ __ZN15CHEVCController21ProcessLRMEStatsMcoreEv : 10256 -> 10244
~ __ZN15CHEVCController28CollectDataFromCpusMultiCoreEv : 1668 -> 1672
~ __ZN17CMultiPassControl24MpFinalPassSceneBitratesEfb : 6164 -> 6168
~ __ZN17CAVEPriorityQueue16UnregisterClientEy : 612 -> 616
~ __ZNK17CAVEPriorityQueue17GetClientPriorityEyPi : 284 -> 288
~ __ZN17CAVEPriorityQueue17SetClientPriorityEyi : 296 -> 300
~ __ZN17CAVEPriorityQueue22SetClientUseFirmwareRCEyb : 300 -> 304
~ __ZN17CAVEPriorityQueue19SetClientMCTFEncodeEyb : 280 -> 284
~ __ZN17CAVEPriorityQueue24GetCommandQueueToDequeueEy : 224 -> 228
~ __ZN17CAVEPriorityQueue5FlushEyyP15sCmdInformation : 756 -> 768
~ __ZN17CAVEPriorityQueue8CompleteEyj19_E_Proc_Mode_Queues : 440 -> 428
~ __ZN17CAVEPriorityQueue8ConvertPEyj19_E_Proc_Mode_Queues : 880 -> 884
~ _IOProcessorChannelCreate : 268 -> 260
~ sub_e6aa4 -> sub_e6ad4 : 868 -> 844
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
~ _exp2f : 168 -> 176
~ sub_1014a4 -> sub_101554 : 104 -> 88
~ sub_10150c -> sub_1015ac : 468 -> 452
~ sub_1016e0 -> sub_101770 : 764 -> 740
~ sub_1019dc -> sub_101a54 : 84 -> 68
~ sub_101a30 -> sub_101a98 : 248 -> 244
~ sub_1020d4 -> sub_102138 : 876 -> 872
~ sub_10404c -> sub_1040ac : 176 -> 180
~ __ZN7RTKHeap9addToPoolEPvm : 496 -> 500
~ sub_1060bc -> sub_106124 : 228 -> 244
~ sub_106278 -> sub_1062f0 : 168 -> 236
~ sub_106320 -> sub_1063dc : 244 -> 212
~ _RTK_stack_guard_free : 168 -> 164
~ sub_10872c -> sub_1087c4 : 296 -> 292
~ sub_108ac8 -> sub_108b5c : 412 -> 408
~ sub_109fc4 -> sub_10a054 : 2356 -> 2344
~ sub_10b95c -> sub_10b9e0 : 1884 -> 1836
~ sub_10c40c -> sub_10c460 : 452 -> 456
~ sub_10d0b8 -> sub_10d110 : 172 -> 168
~ _RTK_mbi_route_create : 612 -> 592
~ sub_110438 -> sub_110478 : 2592 -> 2652
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
