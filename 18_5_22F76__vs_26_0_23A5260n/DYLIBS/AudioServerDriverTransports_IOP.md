## AudioServerDriverTransports_IOP

> `/System/Library/PrivateFrameworks/AudioServerDriverTransports_IOP.framework/AudioServerDriverTransports_IOP`

```diff

-250.3.0.0.0
-  __TEXT.__text: 0xe9b4
-  __TEXT.__auth_stubs: 0x6f0
-  __TEXT.__objc_methlist: 0xc2c
+300.65.0.0.0
+  __TEXT.__text: 0xe910
+  __TEXT.__auth_stubs: 0x6b0
+  __TEXT.__objc_methlist: 0xc3c
   __TEXT.__gcc_except_tab: 0x138c
   __TEXT.__const: 0x148
-  __TEXT.__oslogstring: 0xe95
-  __TEXT.__cstring: 0xe6e
+  __TEXT.__oslogstring: 0xe68
+  __TEXT.__cstring: 0xe61
   __TEXT.__unwind_info: 0x788
   __TEXT.__objc_classname: 0x359
-  __TEXT.__objc_methname: 0x134d
-  __TEXT.__objc_methtype: 0xb25
-  __TEXT.__objc_stubs: 0x1300
-  __DATA_CONST.__got: 0x170
+  __TEXT.__objc_methname: 0x1370
+  __TEXT.__objc_methtype: 0x811
+  __TEXT.__objc_stubs: 0x12e0
+  __DATA_CONST.__got: 0x158
   __DATA_CONST.__const: 0x100
   __DATA_CONST.__objc_classlist: 0xc0
   __DATA_CONST.__objc_catlist: 0x8

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x678
   __DATA_CONST.__objc_superrefs: 0x90
-  __AUTH_CONST.__auth_got: 0x390
+  __AUTH_CONST.__auth_got: 0x370
   __AUTH_CONST.__const: 0x228
   __AUTH_CONST.__cfstring: 0x300
   __AUTH_CONST.__objc_const: 0x1748
-  __AUTH_CONST.__objc_intobj: 0x168
+  __AUTH_CONST.__objc_intobj: 0x180
   __AUTH.__objc_data: 0x1e0
   __DATA.__objc_ivar: 0x64
   __DATA.__data: 0x188

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 75845EB1-1F48-35BF-9894-DAA93FCB01F6
-  Functions: 436
-  Symbols:   1537
-  CStrings:  578
+  UUID: CD147DE9-611C-3CB1-93EE-1743CAD94B60
+  Functions: 434
+  Symbols:   1526
+  CStrings:  576
 
Symbols:
+ +[ASDTIOPAudioLPMicDevice enableListeningOnGesturePropertyForService:]
+ GCC_except_table18
+ GCC_except_table25
+ GCC_except_table27
+ __ZN10applesauce2CF13DictionaryRefD2Ev
+ __ZN10applesauce2CF7TypeRefD2Ev
+ __ZN10applesauce2CF9ObjectRefIPK10__CFStringED2Ev
+ __ZN10applesauce2CF9ObjectRefIPK14__CFDictionaryED2Ev
+ __ZNSt3__111shared_lockINS_12shared_mutexEED2B8ne200100Ev
+ __ZNSt3__111unique_lockINS_12shared_mutexEED2B8ne200100Ev
- GCC_except_table13
- GCC_except_table24
- GCC_except_table34
- __ZN10applesauce2CF13DictionaryRef8from_getEPK14__CFDictionary
- __ZN10applesauce2CF9ObjectRefIPK10__CFStringED1Ev
- __ZN10applesauce2CF9ObjectRefIPK14__CFDictionaryED1Ev
- __ZNKSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB8ne190102Ev
- __ZNSt11logic_errorC2EPKc
- __ZNSt12length_errorC1B8ne190102EPKc
- __ZNSt12length_errorD1Ev
- __ZNSt3__111shared_lockINS_12shared_mutexEED2B8ne190102Ev
- __ZNSt3__111unique_lockINS_12shared_mutexEED2B8ne190102Ev
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B8ne190102ILi0EEEPKc
- __ZNSt3__120__throw_length_errorB8ne190102EPKc
- __ZTISt12length_error
- __ZTVSt12length_error
- __Znwm
- _memmove
- _objc_msgSend$isActive
- _strlen
CStrings:
+ "enableListeningOnGesturePropertyForService:"
+ "{unique_ptr<ASDT::Exclaves::StatusTracker, std::default_delete<ASDT::Exclaves::StatusTracker>>=\"__ptr_\"^{StatusTracker}}"
+ "{unique_ptr<ASDT::IOPAudio::ClientManager::UserClient, std::default_delete<ASDT::IOPAudio::ClientManager::UserClient>>=\"__ptr_\"^{UserClient}}"
+ "{unique_ptr<ASDT::IOPAudio::IOBuffer::UserClient, std::default_delete<ASDT::IOPAudio::IOBuffer::UserClient>>=\"__ptr_\"^{UserClient}}"
+ "{unique_ptr<ASDT::IOPAudio::IsolatedIOBuffer::UserClient, std::default_delete<ASDT::IOPAudio::IsolatedIOBuffer::UserClient>>=\"__ptr_\"^{UserClient}}"
+ "{unique_ptr<ASDT::IOPAudio::LPMic::UserClient, std::default_delete<ASDT::IOPAudio::LPMic::UserClient>>=\"__ptr_\"^{UserClient}}"
+ "{unique_ptr<ASDT::IOPAudio::VoiceTrigger::UserClient, std::default_delete<ASDT::IOPAudio::VoiceTrigger::UserClient>>=\"__ptr_\"^{UserClient}}"
- "%@:%@: Stream not active for ioThread start."
- "basic_string"
- "isActive"
- "{unique_ptr<ASDT::Exclaves::StatusTracker, std::default_delete<ASDT::Exclaves::StatusTracker>>=\"__ptr_\"{__compressed_pair<ASDT::Exclaves::StatusTracker *, std::default_delete<ASDT::Exclaves::StatusTracker>>=\"__value_\"^{StatusTracker}}}"
- "{unique_ptr<ASDT::IOPAudio::ClientManager::UserClient, std::default_delete<ASDT::IOPAudio::ClientManager::UserClient>>=\"__ptr_\"{__compressed_pair<ASDT::IOPAudio::ClientManager::UserClient *, std::default_delete<ASDT::IOPAudio::ClientManager::UserClient>>=\"__value_\"^{UserClient}}}"
- "{unique_ptr<ASDT::IOPAudio::IOBuffer::UserClient, std::default_delete<ASDT::IOPAudio::IOBuffer::UserClient>>=\"__ptr_\"{__compressed_pair<ASDT::IOPAudio::IOBuffer::UserClient *, std::default_delete<ASDT::IOPAudio::IOBuffer::UserClient>>=\"__value_\"^{UserClient}}}"
- "{unique_ptr<ASDT::IOPAudio::IsolatedIOBuffer::UserClient, std::default_delete<ASDT::IOPAudio::IsolatedIOBuffer::UserClient>>=\"__ptr_\"{__compressed_pair<ASDT::IOPAudio::IsolatedIOBuffer::UserClient *, std::default_delete<ASDT::IOPAudio::IsolatedIOBuffer::UserClient>>=\"__value_\"^{UserClient}}}"
- "{unique_ptr<ASDT::IOPAudio::LPMic::UserClient, std::default_delete<ASDT::IOPAudio::LPMic::UserClient>>=\"__ptr_\"{__compressed_pair<ASDT::IOPAudio::LPMic::UserClient *, std::default_delete<ASDT::IOPAudio::LPMic::UserClient>>=\"__value_\"^{UserClient}}}"
- "{unique_ptr<ASDT::IOPAudio::VoiceTrigger::UserClient, std::default_delete<ASDT::IOPAudio::VoiceTrigger::UserClient>>=\"__ptr_\"{__compressed_pair<ASDT::IOPAudio::VoiceTrigger::UserClient *, std::default_delete<ASDT::IOPAudio::VoiceTrigger::UserClient>>=\"__value_\"^{UserClient}}}"

```
