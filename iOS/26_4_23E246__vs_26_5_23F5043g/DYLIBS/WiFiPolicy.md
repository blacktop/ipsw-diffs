## WiFiPolicy

> `/System/Library/PrivateFrameworks/WiFiPolicy.framework/WiFiPolicy`

```diff

-1041.25.0.0.0
-  __TEXT.__text: 0xd7bfc
+1050.2.0.0.0
+  __TEXT.__text: 0xd7f10
   __TEXT.__auth_stubs: 0x1730
-  __TEXT.__objc_methlist: 0x12450
+  __TEXT.__objc_methlist: 0x124d0
   __TEXT.__const: 0x6e8
-  __TEXT.__cstring: 0x202cc
+  __TEXT.__cstring: 0x202c5
   __TEXT.__oslogstring: 0x4862
   __TEXT.__gcc_except_tab: 0x1920
   __TEXT.__dlopen_cstrs: 0xf3
   __TEXT.__ustring: 0x82
-  __TEXT.__unwind_info: 0x2fd0
-  __TEXT.__objc_classname: 0x14ba
-  __TEXT.__objc_methname: 0x34e6c
+  __TEXT.__unwind_info: 0x2fe0
+  __TEXT.__objc_classname: 0x14bb
+  __TEXT.__objc_methname: 0x350ec
   __TEXT.__objc_methtype: 0x3f90
-  __TEXT.__objc_stubs: 0x1a200
+  __TEXT.__objc_stubs: 0x1a220
   __DATA_CONST.__got: 0xab0
   __DATA_CONST.__const: 0x23d0
   __DATA_CONST.__objc_classlist: 0x570
   __DATA_CONST.__objc_catlist: 0x58
   __DATA_CONST.__objc_protolist: 0x108
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xa198
+  __DATA_CONST.__objc_selrefs: 0xa1f0
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x488
   __DATA_CONST.__objc_arraydata: 0xb50
   __AUTH_CONST.__auth_got: 0xbb0
   __AUTH_CONST.__const: 0x4e0
-  __AUTH_CONST.__cfstring: 0x1b280
-  __AUTH_CONST.__objc_const: 0x22e00
+  __AUTH_CONST.__cfstring: 0x1b2a0
+  __AUTH_CONST.__objc_const: 0x22ef0
   __AUTH_CONST.__objc_intobj: 0x19f8
   __AUTH_CONST.__objc_arrayobj: 0x3f0
   __AUTH_CONST.__objc_dictobj: 0x168
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH.__objc_data: 0x7f8
-  __DATA.__objc_ivar: 0x22b0
+  __DATA.__objc_ivar: 0x22c4
   __DATA.__data: 0x1c20
   __DATA.__bss: 0x78
   __DATA_DIRTY.__objc_data: 0x2e68

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 3E9D6C37-D44E-392C-8340-F5084E82A296
-  Functions: 6559
-  Symbols:   21402
-  CStrings:  17703
+  UUID: B8842D99-4496-3373-ABE5-4BBDBAFB7DB7
+  Functions: 6570
+  Symbols:   21430
+  CStrings:  17726
 
Symbols:
+ -[WiFiUsageSession assocWhenNotChargingDuration]
+ -[WiFiUsageSession assocWhenNotChargingStartTime]
+ -[WiFiUsageSession assocWhileChargingDuration]
+ -[WiFiUsageSession assocWhileChargingStartTime]
+ -[WiFiUsageSession isDeviceCharging]
+ -[WiFiUsageSession setAssocWhenNotChargingDuration:]
+ -[WiFiUsageSession setAssocWhenNotChargingStartTime:]
+ -[WiFiUsageSession setAssocWhileChargingDuration:]
+ -[WiFiUsageSession setAssocWhileChargingStartTime:]
+ -[WiFiUsageSession setIsDeviceCharging:]
+ -[WiFiUsageSession tallyAssocDurationWithChargingState]
+ GCC_except_table60
+ _OBJC_IVAR_$_WiFiUsageSession._assocWhenNotChargingDuration
+ _OBJC_IVAR_$_WiFiUsageSession._assocWhenNotChargingStartTime
+ _OBJC_IVAR_$_WiFiUsageSession._assocWhileChargingDuration
+ _OBJC_IVAR_$_WiFiUsageSession._assocWhileChargingStartTime
+ _OBJC_IVAR_$_WiFiUsageSession._isDeviceCharging
+ ___62-[WiFiUsageLinkSession performLinkTestFor:isTriggeredByFault:]_block_invoke.373
+ _objc_msgSend$tallyAssocDurationWithChargingState
- GCC_except_table58
- ___62-[WiFiUsageLinkSession performLinkTestFor:isTriggeredByFault:]_block_invoke.376
CStrings:
+ "T@\"NSDate\",&,N,V_assocWhenNotChargingStartTime"
+ "T@\"NSDate\",&,N,V_assocWhileChargingStartTime"
+ "TB,N,V_isDeviceCharging"
+ "Td,N,V_assocWhenNotChargingDuration"
+ "Td,N,V_assocWhileChargingDuration"
+ "_assocWhenNotChargingDuration"
+ "_assocWhenNotChargingStartTime"
+ "_assocWhileChargingDuration"
+ "_assocWhileChargingStartTime"
+ "_isDeviceCharging"
+ "assocWhenNotChargingDuration"
+ "assocWhenNotChargingStartTime"
+ "assocWhileChargingDuration"
+ "assocWhileChargingStartTime"
+ "isDeviceCharging"
+ "setAssocWhenNotChargingDuration:"
+ "setAssocWhenNotChargingStartTime:"
+ "setAssocWhileChargingDuration:"
+ "setAssocWhileChargingStartTime:"
+ "setIsDeviceCharging:"
+ "tallyAssocDurationWithChargingState"
- "%s Rejected due to [WiFiUsagePrivacyFilter isInternalInstall]\n"

```
