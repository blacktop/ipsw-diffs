## AppleAVE2FW_H18.im4p

> `Firmware/ave/AppleAVE2FW_H18.im4p`

```diff

-  __TEXT.__text: 0x1136cc
-  __TEXT.__const: 0x2004c
+  __TEXT.__text: 0x1138d8
+  __TEXT.__const: 0x20044
   __TEXT.__cstring: 0x1948d
   __TEXT.__init_offsets: 0x0
   __TEXT.__chain_starts: 0x18
Sections:
~ __TEXT.__cstring : content changed
~ __DATA._rtk_patchbay : content changed
~ __DATA.__data : content changed
~ __DATA._rtk_mtab : content changed
~ __DATA.__const : content changed
Functions:
~ __ZN14CAVCController19CollectDataFromCpusEb : 1396 -> 1508
~ __ZN14CAVCController24CollectDataFromTranscodeEP30CAVEControllerTranscodeDoneCmd : 1872 -> 1864
~ __ZN14CAVCController19GetSliceHeaderForFWEPK12_S_AVC_SliceyiPhPji : 908 -> 904
~ sub_136e8 -> sub_1374c : 8300 -> 8264
~ __ZN15CHEVCController19CollectDataFromCpusEb : 1704 -> 1832
~ __ZN14CAVCController14ConfigureMCPUsEPK18AVE_PICMGMT_PARAMSPK12_S_AVC_Slice : 6464 -> 6472
~ __ZN14CAVCController16ProcessHMESCDoneEv : 984 -> 988
~ __ZN15CHEVCController16ProcessHMESCDoneEv : 1028 -> 1032
~ __ZN14CGGMController14ConfigureMCPUsEPK18AVE_PICMGMT_PARAMS : 592 -> 588
~ __ZN17CMultiPassControl32CollectMultiPassStats_MCPUs_HEVCEP13sCommonParamsjjjjPv : 924 -> 1044
~ __ZN17CMultiPassControl31CollectMultiPassStats_MCPUs_AVCEP13sCommonParamsjjPv : 896 -> 1036
~ __ZN17CMultiPassControl24MpFinalPassSceneBitratesEfb : 6164 -> 6168
~ __ZN17CAVEPriorityQueue16UnregisterClientEy : 612 -> 616
~ __ZNK17CAVEPriorityQueue17GetClientPriorityEyPi : 284 -> 288
~ __ZN17CAVEPriorityQueue17SetClientPriorityEyi : 296 -> 300
~ __ZN17CAVEPriorityQueue22SetClientUseFirmwareRCEyb : 296 -> 300
~ __ZN17CAVEPriorityQueue19SetClientMCTFEncodeEyb : 280 -> 284
~ __ZN17CAVEPriorityQueue5FlushEyyP15sCmdInformation : 756 -> 768
~ __ZN17CAVEPriorityQueue8CompleteEyj19_E_Proc_Mode_Queues : 440 -> 428
~ __ZN17CAVEPriorityQueue8ConvertPEyj19_E_Proc_Mode_Queues : 468 -> 472
~ _IOProcessorChannelCreate : 268 -> 260
~ sub_ea270 -> sub_ea454 : 868 -> 844
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
~ __Z20AVE_IOP_Config_pandav : 348 -> 352
~ _pow : 1216 -> 1184
~ sub_103a34 -> sub_103c74 : 104 -> 88
~ sub_103a9c -> sub_103ccc : 468 -> 452
~ sub_103c70 -> sub_103e90 : 764 -> 740
~ sub_103f6c -> sub_104174 : 84 -> 68
~ sub_103fc0 -> sub_1041b8 : 248 -> 244
~ sub_104664 -> sub_104858 : 876 -> 872
~ sub_1065dc -> sub_1067cc : 176 -> 180
~ __ZN7RTKHeap9addToPoolEPvm : 496 -> 500
~ sub_10864c -> sub_108844 : 228 -> 244
~ sub_108808 -> sub_108a10 : 168 -> 236
~ sub_1088b0 -> sub_108afc : 244 -> 212
~ _RTK_stack_guard_free : 168 -> 164
~ sub_10acbc -> sub_10aee4 : 296 -> 292
~ sub_10b058 -> sub_10b27c : 412 -> 408
~ sub_10c554 -> sub_10c774 : 2356 -> 2344
~ sub_10deec -> sub_10e100 : 1884 -> 1836
~ sub_10e99c -> sub_10eb80 : 452 -> 456
~ sub_10f648 -> sub_10f830 : 172 -> 168
~ _RTK_mbi_route_create : 612 -> 592
~ sub_1129c8 -> sub_112b98 : 2592 -> 2652

```
