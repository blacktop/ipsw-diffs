## AUHostingServiceXPC_arrow

> `/System/Library/Frameworks/AudioToolbox.framework/XPCServices/AUHostingServiceXPC_arrow.xpc/AUHostingServiceXPC_arrow`

```diff

-1456.607.0.0.0
-  __TEXT.__text: 0x6018
+1534.2.30.1.0
+  __TEXT.__text: 0x6028
   __TEXT.__auth_stubs: 0x840
   __TEXT.__objc_stubs: 0xa80
   __TEXT.__objc_methlist: 0x6ac

   __TEXT.__cstring: 0x928
   __TEXT.__objc_methname: 0x1209
   __TEXT.__objc_classname: 0x14c
-  __TEXT.__objc_methtype: 0xdcb
+  __TEXT.__objc_methtype: 0xd69
   __TEXT.__oslogstring: 0x231
   __TEXT.__dof_AUHosting: 0x4a9
   __TEXT.__unwind_info: 0x328

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/PrivateFrameworks/AudioToolboxCore.framework/AudioToolboxCore
+  - /System/Library/PrivateFrameworks/caulk.framework/caulk
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 83FEA222-1F0A-342C-8FD0-2FAE70E91086
+  UUID: 32F77616-12FE-324F-9582-953100EFAF92
   Functions: 124
   Symbols:   174
   CStrings:  418
Symbols:
+ __ZnwmSt19__type_descriptor_t
- __Znwm
Functions:
~ sub_100005be0 -> sub_100005c38 : 56 -> 72
CStrings:
+ "{basic_string<char, std::char_traits<char>, std::allocator<char>>=\"__rep_\"(__rep=\"__s\"{__short=\"__data_\"[23c]\"__size_\"b7\"__is_long_\"b1}\"__l\"{__long=\"__data_\"*\"__size_\"Q\"__cap_\"b63\"__is_long_\"b1})}"
- "{basic_string<char, std::char_traits<char>, std::allocator<char>>=\"__r_\"{__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>=\"__value_\"(__rep=\"__s\"{__short=\"__data_\"[23c]\"__padding_\"[0C]\"__size_\"b7\"__is_long_\"b1}\"__l\"{__long=\"__data_\"*\"__size_\"Q\"__cap_\"b63\"__is_long_\"b1})}}"

```
