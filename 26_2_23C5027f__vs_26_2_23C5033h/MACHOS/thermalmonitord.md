## thermalmonitord

> `/usr/libexec/thermalmonitord`

```diff

 2048.0.0.0.0
-  __TEXT.__text: 0x5a114
+  __TEXT.__text: 0x5a124
   __TEXT.__auth_stubs: 0x13b0
   __TEXT.__objc_stubs: 0x4f40
   __TEXT.__objc_methlist: 0x4104

   __TEXT.__objc_classname: 0x12e1
   __TEXT.__objc_methtype: 0x1ab8
   __TEXT.__objc_methname: 0x82f4
-  __TEXT.__cstring: 0x4a91
+  __TEXT.__cstring: 0x4a9d
   __TEXT.__gcc_except_tab: 0x3bc
   __TEXT.__oslogstring: 0x991b
   __TEXT.__unwind_info: 0x11f8
   __DATA_CONST.__auth_got: 0x9f0
   __DATA_CONST.__got: 0x5d0
-  __DATA_CONST.__auth_ptr: 0x8
+  __DATA_CONST.__auth_ptr: 0x10
   __DATA_CONST.__const: 0x13b0
   __DATA_CONST.__cfstring: 0x6200
   __DATA_CONST.__objc_classlist: 0x518

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 85DB7810-0582-3A49-8FD4-90CC8EEA6787
+  UUID: 8035A178-C5A2-30DE-BECB-4F6A717227A0
   Functions: 2015
-  Symbols:   407
+  Symbols:   408
   CStrings:  4487
 
Symbols:
+ ___chkstk_darwin
Functions:
~ sub_100029324 : 60 -> 64
~ sub_10004830c -> sub_100048310 : 6164 -> 6184
~ sub_1000532c0 -> sub_1000532d8 : 224 -> 220
~ sub_100059774 -> sub_100059788 : 120 -> 116
CStrings:
+ "v36@?0B8{vector<abm::BasebandThermalID, std::allocator<abm::BasebandThermalID>>=^C^C{?=^C}}12"
+ "v36@?0B8{vector<abm::ThermalSensorData, std::allocator<abm::ThermalSensorData>>=^{ThermalSensorData}^{ThermalSensorData}{?=^{ThermalSensorData}}}12"
+ "v48@?0{Result=i{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}}8^v40"
- "v36@?0B8{vector<abm::BasebandThermalID, std::allocator<abm::BasebandThermalID>>=^C^C^C}12"
- "v36@?0B8{vector<abm::ThermalSensorData, std::allocator<abm::ThermalSensorData>>=^{ThermalSensorData}^{ThermalSensorData}^{ThermalSensorData}}12"
- "v48@?0{Result=i{basic_string<char, std::char_traits<char>, std::allocator<char>>=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}8^v40"

```
