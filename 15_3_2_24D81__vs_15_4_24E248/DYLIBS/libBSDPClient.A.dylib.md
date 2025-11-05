## libBSDPClient.A.dylib

> `/usr/lib/libBSDPClient.A.dylib`

```diff

-494.80.2.0.0
-  __TEXT.__text: 0x4578
-  __TEXT.__auth_stubs: 0x550
+494.101.1.0.0
+  __TEXT.__text: 0x4450
+  __TEXT.__auth_stubs: 0x530
   __TEXT.__const: 0x30
-  __TEXT.__cstring: 0x7cb
+  __TEXT.__cstring: 0x787
   __TEXT.__oslogstring: 0x133
   __TEXT.__unwind_info: 0x160
-  __DATA_CONST.__got: 0x78
-  __AUTH_CONST.__auth_got: 0x2a8
-  __AUTH_CONST.__cfstring: 0x1a0
+  __DATA_CONST.__got: 0x80
+  __AUTH_CONST.__auth_got: 0x298
+  __AUTH_CONST.__cfstring: 0x120
   __DATA.__bss: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/Frameworks/SystemConfiguration.framework/Versions/A/SystemConfiguration
   - /usr/lib/libSystem.B.dylib
-  UUID: 3F1A894F-B5D7-3C76-A2AD-2739C691600E
+  UUID: D3797AD2-1E84-38C7-885E-2F9381C960CE
   Functions: 81
-  Symbols:   113
-  CStrings:  83
+  Symbols:   112
+  CStrings:  75
 
Symbols:
+ _SCNetworkInterfaceGetInterfaceType
+ _kSCNetworkInterfaceTypeIEEE80211
- _CFDictionaryCreate
- _IORegistryEntryCreateCFProperty
- _IOServiceGetMatchingService
Functions:
~ _BSDPClientCreateWithInterfaceAndAttributes : 800 -> 824
~ sub_25ffe6eb0 -> sub_267f5dbe8 : 908 -> 896
~ sub_25ffe782c -> sub_267f5e558 : 60 -> 56
~ sub_25ffe7918 -> sub_267f5e640 : 1020 -> 1016
~ sub_25ffe7f90 -> sub_267f5ecb4 : 1012 -> 1008
~ sub_25ffe932c -> sub_267f6004c : 456 -> 448
~ sub_25ffe9574 -> sub_267f6028c : 124 -> 120
~ sub_25ffe95f0 -> sub_267f60304 : 1024 -> 1020
~ sub_25ffea0a4 -> sub_267f60db4 : 1996 -> 1692
~ sub_25ffeaa84 -> sub_267f61664 : 424 -> 440
~ sub_25ffeae7c -> sub_267f61a6c : 148 -> 156
CStrings:
- "IO80211InterfaceRole"
- "IOInterfaceName"
- "IOPropertyMatch"
- "Infrastructure"

```
