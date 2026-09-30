## AppleAOPAudioPlugin

> `/System/Library/Audio/Plug-Ins/HAL/AppleAOPAudioPlugin.driver/AppleAOPAudioPlugin`

```diff

-420.1.0.0.0
-  __TEXT.__text: 0x186d4
-  __TEXT.__auth_stubs: 0xd60
+500.1.0.0.0
+  __TEXT.__text: 0x18aa0
+  __TEXT.__auth_stubs: 0xd50
   __TEXT.__objc_stubs: 0xca0
   __TEXT.__init_offsets: 0x4
   __TEXT.__objc_methlist: 0x350
-  __TEXT.__gcc_except_tab: 0x15cc
+  __TEXT.__gcc_except_tab: 0x15c8
   __TEXT.__const: 0x300
   __TEXT.__oslogstring: 0x1875
   __TEXT.__cstring: 0x306b
   __TEXT.__objc_methname: 0xc2f
   __TEXT.__objc_classname: 0x41
-  __TEXT.__objc_methtype: 0x71b
-  __TEXT.__unwind_info: 0xb38
-  __DATA_CONST.__auth_got: 0x6c0
-  __DATA_CONST.__got: 0x128
+  __TEXT.__objc_methtype: 0x5a7
+  __TEXT.__unwind_info: 0xb50
+  __DATA_CONST.__auth_got: 0x6b8
+  __DATA_CONST.__got: 0x130
   __DATA_CONST.__const: 0x528
   __DATA_CONST.__cfstring: 0x4a0
   __DATA_CONST.__objc_classlist: 0x18

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B8B07D7C-1771-329F-89E8-DB5981C4CF5D
-  Functions: 666
+  UUID: 56B4A28F-276B-3928-A240-35E55ABB5429
+  Functions: 672
   Symbols:   699
   CStrings:  604
 
Symbols:
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6resizeEmc
+ __ZNSt3__16localeC1Ev
+ __ZTVNSt3__115basic_streambufIcNS_11char_traitsIcEEEE
- __ZNSt3__115basic_streambufIcNS_11char_traitsIcEEEC2Ev
- __ZNSt3__115basic_streambufIcNS_11char_traitsIcEEED2Ev
- __Znwm
CStrings:
+ "00:14:32"
+ "500.1"
+ "May 19 2025"
+ "{DeviceInfo=\"mDeviceObjectID\"I\"mInterestNotificationList\"{vector<unsigned int, std::allocator<unsigned int>>=\"__begin_\"^I\"__end_\"^I\"__cap_\"^I}}"
+ "{basic_string<char, std::char_traits<char>, std::allocator<char>>=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}16@0:8"
+ "{unique_ptr<CADeprecated::CADispatchQueue, std::default_delete<CADeprecated::CADispatchQueue>>=\"__ptr_\"^{CADispatchQueue}}"
+ "{unique_ptr<CADeprecated::CAMutex, std::default_delete<CADeprecated::CAMutex>>=\"__ptr_\"^{CAMutex}}"
- "01:30:19"
- "420.1"
- "Apr 19 2025"
- "{DeviceInfo=\"mDeviceObjectID\"I\"mInterestNotificationList\"{vector<unsigned int, std::allocator<unsigned int>>=\"__begin_\"^I\"__end_\"^I\"__end_cap_\"{__compressed_pair<unsigned int *, std::allocator<unsigned int>>=\"__value_\"^I}}}"
- "{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>=(__rep={__short=[23c][0C]b7b1}{__long=*Qb63b1})}}16@0:8"
- "{unique_ptr<CADeprecated::CADispatchQueue, std::default_delete<CADeprecated::CADispatchQueue>>=\"__ptr_\"{__compressed_pair<CADeprecated::CADispatchQueue *, std::default_delete<CADeprecated::CADispatchQueue>>=\"__value_\"^{CADispatchQueue}}}"
- "{unique_ptr<CADeprecated::CAMutex, std::default_delete<CADeprecated::CAMutex>>=\"__ptr_\"{__compressed_pair<CADeprecated::CAMutex *, std::default_delete<CADeprecated::CAMutex>>=\"__value_\"^{CAMutex}}}"

```
