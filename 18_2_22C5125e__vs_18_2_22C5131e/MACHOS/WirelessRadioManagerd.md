## WirelessRadioManagerd

> `/usr/sbin/WirelessRadioManagerd`

```diff

-1740.2.7.2.0
-  __TEXT.__text: 0x137398
+1740.2.8.1.0
+  __TEXT.__text: 0x13753c
   __TEXT.__auth_stubs: 0x2170
-  __TEXT.__objc_stubs: 0x1bf80
+  __TEXT.__objc_stubs: 0x1bf40
   __TEXT.__init_offsets: 0x4
-  __TEXT.__objc_methlist: 0xe29c
-  __TEXT.__objc_methname: 0x2b51d
-  __TEXT.__cstring: 0x48a95
+  __TEXT.__objc_methlist: 0xe25c
+  __TEXT.__objc_methname: 0x2b359
+  __TEXT.__cstring: 0x48aea
   __TEXT.__objc_classname: 0xddc
   __TEXT.__objc_methtype: 0x751c
-  __TEXT.__gcc_except_tab: 0x4310
-  __TEXT.__const: 0x1fa08
+  __TEXT.__gcc_except_tab: 0x436c
+  __TEXT.__const: 0x1fa18
   __TEXT.__dlopen_cstrs: 0x376
   __TEXT.__oslogstring: 0x90
-  __TEXT.__unwind_info: 0x40c0
+  __TEXT.__unwind_info: 0x40d0
   __DATA_CONST.__auth_got: 0x10d0
   __DATA_CONST.__got: 0x6e8
   __DATA_CONST.__auth_ptr: 0x10
   __DATA_CONST.__const: 0x4800
-  __DATA_CONST.__cfstring: 0x28ce0
+  __DATA_CONST.__cfstring: 0x28d00
   __DATA_CONST.__objc_classlist: 0x410
   __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_arrayobj: 0x6c18
   __DATA_CONST.__objc_dictobj: 0x208
   __DATA_CONST.__objc_doubleobj: 0x10
-  __DATA.__objc_const: 0x18668
-  __DATA.__objc_selrefs: 0x8160
-  __DATA.__objc_ivar: 0x1908
+  __DATA.__objc_const: 0x18548
+  __DATA.__objc_selrefs: 0x8138
+  __DATA.__objc_ivar: 0x18f0
   __DATA.__objc_data: 0x28a0
   __DATA.__data: 0x5c8
   __DATA.__common: 0x168

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libnetwork.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 6536
+  Functions: 6532
   Symbols:   762
-  CStrings:  14022
+  CStrings:  14006
 
CStrings:
+ "Cellular/WiFi TimeSharing:  Configure WiFi channel for TimeSharing: %!@(MISSING)"
+ "Cellular/WiFi TimeSharing:  triggered by WRM_B40B_COEX"
+ "Cellular/WiFi TimeSharing:  triggered by WRM_B41A1+A2_Coex"
+ "Cellular/WiFi TimeSharing: Configured to BB (subId = %!l(MISSING)lu, CoexTech = 0x%!X(MISSING), centerFreq = %!l(MISSING)lu,  bandwidth = %!l(MISSING)lu, )"
+ "Cellular/WiFi TimeSharing: Enabled for freq %!l(MISSING)lu and bw %!l(MISSING)lu"
+ "Coex ARI driver(SubId %!u(MISSING)): Set Timesharing Config - BandInfo[0] , frequency=%!l(MISSING)ldKHz, BW=%!l(MISSING)ldKHz"
+ "setStaticTimesharingConfig:"
- "Configure Timesharing: Invalid active SubId %!l(MISSING)lu"
- "TB,R,N,V_timesharingEnabled_subId0"
- "TB,R,N,V_timesharingEnabled_subId1"
- "TQ,R,N,V_timesharingBw_subId0"
- "TQ,R,N,V_timesharingBw_subId1"
- "TQ,R,N,V_timesharingFreq_subId0"
- "TQ,R,N,V_timesharingFreq_subId1"
- "Time Sharing triggered by WRM_B40B_COEX"
- "Time Sharing triggered by WRM_B41A1+A2_Coex"
- "Time Sharing will be configured for central freq %!l(MISSING)lu and bw %!l(MISSING)lu"
- "_timesharingBw_subId0"
- "_timesharingBw_subId1"
- "_timesharingEnabled_subId0"
- "_timesharingEnabled_subId1"
- "_timesharingFreq_subId0"
- "_timesharingFreq_subId1"
- "configureCellularTimeShareConfigReqParamsWithInstance is called. BB side timesharing will be configured. (centerFreq = %!l(MISSING)lu, CoexTech = 0x%!X(MISSING), bandwidth = %!l(MISSING)lu, subId = %!l(MISSING)lu)"
- "timesharingBw_subId0"
- "timesharingBw_subId1"
- "timesharingEnabled_subId0"
- "timesharingEnabled_subId1"
- "timesharingFreq_subId0"
- "timesharingFreq_subId1"

```
