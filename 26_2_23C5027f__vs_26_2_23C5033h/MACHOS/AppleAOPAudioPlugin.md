## AppleAOPAudioPlugin

> `/System/Library/Audio/Plug-Ins/HAL/AppleAOPAudioPlugin.driver/AppleAOPAudioPlugin`

```diff

 500.1.0.0.0
-  __TEXT.__text: 0x18aa0
+  __TEXT.__text: 0x18ab0
   __TEXT.__auth_stubs: 0xd50
   __TEXT.__objc_stubs: 0xca0
   __TEXT.__init_offsets: 0x4

   __TEXT.__cstring: 0x306b
   __TEXT.__objc_methname: 0xc2f
   __TEXT.__objc_classname: 0x41
-  __TEXT.__objc_methtype: 0x5a7
+  __TEXT.__objc_methtype: 0x5bd
   __TEXT.__unwind_info: 0xb98
   __DATA_CONST.__auth_got: 0x6b8
   __DATA_CONST.__got: 0x130

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: EB3FE1C3-275B-3AA3-AC9F-CD75839589CC
+  UUID: 6E22F2FC-7F8A-38EF-AB78-77657C17E8A6
   Functions: 672
   Symbols:   699
   CStrings:  604
Functions:
~ sub_8340 : 60 -> 64
~ sub_8518 -> sub_851c : 60 -> 64
~ sub_12848 -> sub_12850 : 280 -> 284
~ sub_14bd4 -> sub_14be0 : 60 -> 64
CStrings:
+ "01:14:42"
+ "Nov  1 2025"
+ "{DeviceInfo=\"mDeviceObjectID\"I\"mInterestNotificationList\"{vector<unsigned int, std::allocator<unsigned int>>=\"__begin_\"^I\"__end_\"^I\"\"{?=\"__cap_\"^I}}}"
+ "{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}16@0:8"
+ "{unique_ptr<CADeprecated::CADispatchQueue, std::default_delete<CADeprecated::CADispatchQueue>>=\"\"{?=\"__ptr_\"^{CADispatchQueue}}}"
+ "{unique_ptr<CADeprecated::CAMutex, std::default_delete<CADeprecated::CAMutex>>=\"\"{?=\"__ptr_\"^{CAMutex}}}"
- "09:22:49"
- "Oct 18 2025"
- "{DeviceInfo=\"mDeviceObjectID\"I\"mInterestNotificationList\"{vector<unsigned int, std::allocator<unsigned int>>=\"__begin_\"^I\"__end_\"^I\"__cap_\"^I}}"
- "{basic_string<char, std::char_traits<char>, std::allocator<char>>=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}16@0:8"
- "{unique_ptr<CADeprecated::CADispatchQueue, std::default_delete<CADeprecated::CADispatchQueue>>=\"__ptr_\"^{CADispatchQueue}}"
- "{unique_ptr<CADeprecated::CAMutex, std::default_delete<CADeprecated::CAMutex>>=\"__ptr_\"^{CAMutex}}"

```
