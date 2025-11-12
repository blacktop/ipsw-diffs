## CoreAudioOrchestration

> `/System/Library/PrivateFrameworks/CoreAudioOrchestration.framework/CoreAudioOrchestration`

```diff

 50.202.0.0.0
-  __TEXT.__text: 0x54d78
+  __TEXT.__text: 0x54d8c
   __TEXT.__auth_stubs: 0x1440
   __TEXT.__objc_methlist: 0x76c
   __TEXT.__const: 0xaaa4

   __TEXT.__eh_frame: 0x2bd4
   __TEXT.__objc_classname: 0x194
   __TEXT.__objc_methname: 0xb71
-  __TEXT.__objc_methtype: 0xe10
+  __TEXT.__objc_methtype: 0xe3a
   __TEXT.__objc_stubs: 0x4e0
   __DATA_CONST.__got: 0x260
   __DATA_CONST.__const: 0x58

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 6AEAE99E-E608-3491-A1B5-DDF36D4D672E
+  UUID: 788EC5A9-D35F-3568-B1F3-F4580F4EC1F0
   Functions: 2598
   Symbols:   1901
   CStrings:  589
Functions:
~ __ZNSt3__16vectorImNS_9allocatorImEEE11__vallocateB8ne200100Em : 60 -> 64
~ __ZNSt3__16vectorIN4AMCP11Proc_StreamENS_9allocatorIS2_EEE11__vallocateB8ne200100Em : 76 -> 80
~ __ZNSt3__16vectorI15AudioBufferListNS_9allocatorIS1_EEE11__vallocateB8ne200100Em : 76 -> 80
~ __ZNSt3__16vectorI17ExADUseCaseFormatNS_9allocatorIS1_EEE11__vallocateB8ne200100Em : 60 -> 64
~ __ZNSt3__16vectorINS_4pairI26AudioObjectPropertyAddressPFijjPKS2_PvEEENS_9allocatorIS8_EEE11__vallocateB8ne200100Em : 76 -> 80
CStrings:
+ "{IOProcBrain=\"_vptr$IOProcCallable\"^^?\"_vptr$ADMIOConfigurable\"^^?\"mClientIOProc\"{ClientIOProc=\"mProvidedCallback\"^?\"mProvidedClientData\"^v}\"admIOProc\"{ADMIO=\"_vptr$IOProcCallable\"^^?\"_vptr$ADMIOConfigurable\"^^?\"ioInfo\"{ADMIOConfiguration=\"contextID\"I\"frameBufferSize\"Q\"admCallback\"{function<void (unsigned int, const AMCP::Proc_Cycle_Info &, unsigned long, AMCP::Proc_Stream *, unsigned long, AMCP::Proc_Stream *)>=\"__f_\"{__value_func<void (unsigned int, const AMCP::Proc_Cycle_Info &, unsigned long, AMCP::Proc_Stream *, unsigned long, AMCP::Proc_Stream *)>=\"__buf_\"(type=\"__data\"[24C])\"__f_\"^v}}\"inputStreamIndicesInIOProc\"{vector<unsigned long, std::allocator<unsigned long>>=\"__begin_\"^Q\"__end_\"^Q\"\"{?=\"__cap_\"^Q}}\"outputStreamIndicesInIOProc\"{vector<unsigned long, std::allocator<unsigned long>>=\"__begin_\"^Q\"__end_\"^Q\"\"{?=\"__cap_\"^Q}}}\"admInputs\"{ADMStreamsAndABLs=\"streams\"{vector<AMCP::Proc_Stream, std::allocator<AMCP::Proc_Stream>>=\"__begin_\"^{Proc_Stream}\"__end_\"^{Proc_Stream}\"\"{?=\"__cap_\"^{Proc_Stream}}}\"abls\"{vector<AudioBufferList, std::allocator<AudioBufferList>>=\"__begin_\"^{AudioBufferList}\"__end_\"^{AudioBufferList}\"\"{?=\"__cap_\"^{AudioBufferList}}}}\"admOutputs\"{ADMStreamsAndABLs=\"streams\"{vector<AMCP::Proc_Stream, std::allocator<AMCP::Proc_Stream>>=\"__begin_\"^{Proc_Stream}\"__end_\"^{Proc_Stream}\"\"{?=\"__cap_\"^{Proc_Stream}}}\"abls\"{vector<AudioBufferList, std::allocator<AudioBufferList>>=\"__begin_\"^{AudioBufferList}\"__end_\"^{AudioBufferList}\"\"{?=\"__cap_\"^{AudioBufferList}}}}}}"
+ "{unique_ptr<IOLapseHandler, std::default_delete<IOLapseHandler>>=\"\"{?=\"__ptr_\"^{IOLapseHandler}}}"
- "{IOProcBrain=\"_vptr$IOProcCallable\"^^?\"_vptr$ADMIOConfigurable\"^^?\"mClientIOProc\"{ClientIOProc=\"mProvidedCallback\"^?\"mProvidedClientData\"^v}\"admIOProc\"{ADMIO=\"_vptr$IOProcCallable\"^^?\"_vptr$ADMIOConfigurable\"^^?\"ioInfo\"{ADMIOConfiguration=\"contextID\"I\"frameBufferSize\"Q\"admCallback\"{function<void (unsigned int, const AMCP::Proc_Cycle_Info &, unsigned long, AMCP::Proc_Stream *, unsigned long, AMCP::Proc_Stream *)>=\"__f_\"{__value_func<void (unsigned int, const AMCP::Proc_Cycle_Info &, unsigned long, AMCP::Proc_Stream *, unsigned long, AMCP::Proc_Stream *)>=\"__buf_\"(type=\"__data\"[24C])\"__f_\"^v}}\"inputStreamIndicesInIOProc\"{vector<unsigned long, std::allocator<unsigned long>>=\"__begin_\"^Q\"__end_\"^Q\"__cap_\"^Q}\"outputStreamIndicesInIOProc\"{vector<unsigned long, std::allocator<unsigned long>>=\"__begin_\"^Q\"__end_\"^Q\"__cap_\"^Q}}\"admInputs\"{ADMStreamsAndABLs=\"streams\"{vector<AMCP::Proc_Stream, std::allocator<AMCP::Proc_Stream>>=\"__begin_\"^{Proc_Stream}\"__end_\"^{Proc_Stream}\"__cap_\"^{Proc_Stream}}\"abls\"{vector<AudioBufferList, std::allocator<AudioBufferList>>=\"__begin_\"^{AudioBufferList}\"__end_\"^{AudioBufferList}\"__cap_\"^{AudioBufferList}}}\"admOutputs\"{ADMStreamsAndABLs=\"streams\"{vector<AMCP::Proc_Stream, std::allocator<AMCP::Proc_Stream>>=\"__begin_\"^{Proc_Stream}\"__end_\"^{Proc_Stream}\"__cap_\"^{Proc_Stream}}\"abls\"{vector<AudioBufferList, std::allocator<AudioBufferList>>=\"__begin_\"^{AudioBufferList}\"__end_\"^{AudioBufferList}\"__cap_\"^{AudioBufferList}}}}}"
- "{unique_ptr<IOLapseHandler, std::default_delete<IOLapseHandler>>=\"__ptr_\"^{IOLapseHandler}}"

```
