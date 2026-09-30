## SampleAnalysis

> `/System/Library/PrivateFrameworks/SampleAnalysis.framework/SampleAnalysis`

```diff

 439.0.0.0.0
-  __TEXT.__text: 0x105ecc
+  __TEXT.__text: 0x105f14
   __TEXT.__objc_methlist: 0x5dbc
   __TEXT.__const: 0x2f8
   __TEXT.__dlopen_cstrs: 0x108
   __TEXT.__cstring: 0x18c31
   __TEXT.__oslogstring: 0xc4ac
-  __TEXT.__gcc_except_tab: 0x20600
+  __TEXT.__gcc_except_tab: 0x20604
   __TEXT.__unwind_info: 0x3cc0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
Functions:
~ _print_io_histograms : 968 -> 976
~ -[SASampleStore _parseKCDataTaskContainer:timestampOfSample:sampleIndex:sharedCaches:frameIterator:primaryDataIsKPerf:addStaticInfoOnly:kperfState:ktraceDataUnavailable:taskUniquePidsInThisSample:taskPidsInThisSample:importanceDonations:rPidForJetsamCoalitionId:port_label_info_array:vmrls:exclaveInfo:] : 18152 -> 18200
~ -[SAModel(Serialization) addSelfToBuffer:bufferLength:withCompletedSerializationDictionary:] : 1492 -> 1496
~ -[SATask(Serialization) populateReferencesUsingBuffer:bufferLength:andDeserializationDictionary:andDataBufferDictionary:] : 5104 -> 5116
```
