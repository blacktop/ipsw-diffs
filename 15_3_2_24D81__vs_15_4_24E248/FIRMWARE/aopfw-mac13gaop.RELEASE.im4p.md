## aopfw-mac13gaop.RELEASE.im4p

> `aopfw-mac13gaop.RELEASE.im4p`

```diff

 
-  __TEXT.__text: 0x78238
-  __TEXT.__const: 0x4168
-  __TEXT.__cstring: 0x13a5a
-  __TEXT.__chain_starts: 0x40
+  __TEXT.__text: 0x77e74
+  __TEXT.__const: 0x4198
+  __TEXT.__cstring: 0x13d0f
+  __TEXT.__chain_starts: 0x44
   __DATA._rtk_boot: 0x3000
   __DATA._rtk_page_tables: 0x5000
   __DATA._spu_stack: 0x1000

   __DATA._rtk_ext_stack: 0x1800
   __DATA._rtk_heap: 0x11b68
   __DATA.__const: 0x7450
-  __DATA.__data: 0x8668
+  __DATA.__data: 0x8780
   __DATA._spu_service: 0x210
   __DATA._spu_endpoint: 0x30
-  __DATA._rtk_patchbay: 0x306
+  __DATA._rtk_patchbay: 0x326
   __DATA._rtk_power: 0x3b8
   __DATA._rtk_tunables: 0x1e8
   __DATA._rtk_data_uuid: 0x0
   __DATA._rtk_threads: 0x0
   __DATA.__gxf_data: 0x10
-  __DATA.__mod_init_func: 0xb0
+  __DATA.__mod_init_func: 0xa8
   __DATA.__version: 0x8
   __DATA.__constructor: 0x0
   __DATA._rtk_mtab: 0x5f8
-  __DATA.__zerofill: 0x5ab70
+  __DATA.__zerofill: 0x5aa70
   __ETEXT.__eh_frame: 0x40
-  __ETEXT.__text: 0xc4c8
-  __ETEXT.__StaticInit: 0x8b0c
+  __ETEXT.__text: 0xc53c
+  __ETEXT.__StaticInit: 0x8800
   __ETEXT.__const: 0x15a
   __OS_LOG.__string: 0x537
   __MISC.__apf_list: 0x90
-  UUID: EAC9270B-6AD6-346D-BB07-90B3BCBE0464
-  Functions: 1726
+  UUID: 93489B48-7421-36E0-BBA3-FF1235056BF1
+  Functions: 1846
   Symbols:   0
-  CStrings:  1712
+  CStrings:  1727
 
CStrings:
+ "!(inArgs->payloadBytes > (inBufferSize - sizeof(struct Interface::SetNodePropertyInputSubPacket)))"
+ "!(sizeof(RegisterAccess::PacketHeader) + packet->header.addressWidth > inBufferSize)"
+ "!instance->ap_mbox & !instance->external & instance->is_inbox"
+ "!instance->ap_mbox & instance->external & instance->is_inbox"
+ "+ %s::%s(%d %s)"
+ "- %s::%s(kEndpointWillPowerOff)"
+ "- %s::%s(kEndpointWillPowerOffNoWake)"
+ "18:48:52"
+ "???"
+ "AppleSPUFirmware-2001.100.83~151"
+ "Cntl"
+ "Mar  7 2025"
+ "RTKitAudioFramework v440.12 (built %s %s) ready!! {%zu nodes}"
+ "Resume"
+ "WillHibernate"
+ "handleHibernationNotification"
+ "instance->ap_mbox & !instance->external & !instance->is_inbox"
+ "instance->ap_mbox & !instance->external & instance->is_inbox"
+ "instance->ap_mbox & instance->external & !instance->is_inbox"
+ "instance->ap_mbox & instance->external & instance->is_inbox"
- "17:46:18"
- "AppleSPUFirmware-2001.80.4~53"
- "Dec 13 2024"
- "RTKitAudioFramework v420.10 (built %s %s) ready!! {%zu nodes}"
- "reqPtr"

```
