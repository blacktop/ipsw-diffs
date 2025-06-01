## AudioServerDriverTransports_IOA2

> `/System/Library/PrivateFrameworks/AudioServerDriverTransports_IOA2.framework/AudioServerDriverTransports_IOA2`

```diff

-140.55.0.0.0
-  __TEXT.__text: 0x30f74
-  __TEXT.__auth_stubs: 0xfc0
+150.2.0.0.0
+  __TEXT.__text: 0x31024
+  __TEXT.__auth_stubs: 0xfe0
   __TEXT.__objc_methlist: 0x1410
-  __TEXT.__gcc_except_tab: 0x4764
+  __TEXT.__gcc_except_tab: 0x4798
   __TEXT.__cstring: 0xf9a
   __TEXT.__oslogstring: 0x2dda
   __TEXT.__const: 0x670
-  __TEXT.__unwind_info: 0x1cb0
+  __TEXT.__unwind_info: 0x1cc0
   __TEXT.__eh_frame: 0x38
   __TEXT.__objc_classname: 0x2f5
-  __TEXT.__objc_methname: 0x23b3
+  __TEXT.__objc_methname: 0x23e5
   __TEXT.__objc_methtype: 0x1bbd
-  __TEXT.__objc_stubs: 0x1fe0
+  __TEXT.__objc_stubs: 0x2060
   __DATA_CONST.__got: 0x138
   __DATA_CONST.__const: 0x200
   __DATA_CONST.__objc_classlist: 0xe0

   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x1ad8
-  __DATA_CONST.__objc_selrefs: 0xa80
+  __DATA_CONST.__objc_selrefs: 0xaa0
   __DATA_CONST.__objc_classrefs: 0x118
   __DATA_CONST.__objc_superrefs: 0xc0
   __AUTH_CONST.__const: 0x858
   __AUTH_CONST.__cfstring: 0xbe0
   __AUTH_CONST.__objc_const: 0xaf0
   __AUTH_CONST.__objc_intobj: 0x30
-  __AUTH_CONST.__auth_got: 0x7f0
+  __AUTH_CONST.__auth_got: 0x800
   __AUTH.__objc_data: 0x8c0
   __DATA.__got_weak: 0x20
   __DATA.__objc_ivar: 0x150

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 2D22FBAE-BA81-366C-8235-22B65FFF73DE
+  UUID: 02346E41-08BD-31A3-B5B7-C4E245694298
   Functions: 1291
-  Symbols:   3644
-  CStrings:  1077
+  Symbols:   3652
+  CStrings:  1081
 
Symbols:
+ GCC_except_table107
+ __ZN4ASDT12IOUserClient33SetTerminationNotificationEnabledEb
+ ___39-[ASDTIOA2Device handleMachPortMessage]_block_invoke
+ _asdtPowerStateCompare
+ _objc_msgSend$pmSequencer
+ _objc_msgSend$pmSerialQueue
+ _objc_msgSend$powerState
+ _objc_msgSend$terminated
- -[ASDTIOA2Device ioRequestBegin].cold.2
- GCC_except_table106
- GCC_except_table112
- GCC_except_table155
CStrings:
+ "pmSequencer"
+ "pmSerialQueue"
+ "powerState"
+ "terminated"

```
