## AirPlayReceiver

> `/System/Library/PrivateFrameworks/AirPlayReceiver.framework/AirPlayReceiver`

```diff

 1005.13.1.1.0
-  __TEXT.__text: 0x1799cc
+  __TEXT.__text: 0x179b44
   __TEXT.__objc_methlist: 0xaec
   __TEXT.__const: 0x2762b
   __TEXT.__dlopen_cstrs: 0xad
   __TEXT.__gcc_except_tab: 0x890
-  __TEXT.__cstring: 0x33395
+  __TEXT.__cstring: 0x33399
   __TEXT.__oslogstring: 0x2eb
   __TEXT.__unwind_info: 0x1cc8
   __TEXT.__eh_frame: 0x128

   __DATA_CONST.__objc_arraydata: 0x10
   __DATA_CONST.__got: 0x998
   __AUTH_CONST.__const: 0x9420
-  __AUTH_CONST.__cfstring: 0xba80
+  __AUTH_CONST.__cfstring: 0xbaa0
   __AUTH_CONST.__objc_const: 0x1550
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_intobj: 0x18
-  __AUTH_CONST.__auth_got: 0x1e38
+  __AUTH_CONST.__auth_got: 0x1e58
   __AUTH.__objc_data: 0x280
   __DATA.__objc_ivar: 0x174
   __DATA.__data: 0x17c40

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 1715
-  Symbols:   3606
-  CStrings:  5207
+  Symbols:   3610
+  CStrings:  5208
 
Symbols:
+ _APSGetClusterMemberIDForSurroundRole
+ _APSGetSurroundRoleFromClusterSummary
+ _APSIsHomeTheaterSurroundEnabled
+ _APSSurroundToOdeonFallbackEnabled
Functions:
~ ____IsWiFiDECaptureAllowed_block_invoke : 36 -> 40
~ _sysInfo_updatePrefs : 5388 -> 5440
~ _sysInfo_updateAdvertiserInfo : 3668 -> 3712
~ __APAdvertiserInfoAddAirPlayData : 3516 -> 3596
~ _APAdvertiserInfoCopyAirPlayDataWithNANServiceType : 3704 -> 3804
~ _APAdvertiserInfoCopyClusterCompatibleAirPlayData : 2640 -> 2736
CStrings:
+ "pgs"
```
