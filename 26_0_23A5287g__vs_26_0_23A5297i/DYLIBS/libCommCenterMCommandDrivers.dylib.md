## libCommCenterMCommandDrivers.dylib

> `/System/Library/Frameworks/CoreTelephony.framework/Support/libCommCenterMCommandDrivers.dylib`

```diff

-13080.2.0.0.0
-  __TEXT.__text: 0x21d820
+13085.1.0.0.0
+  __TEXT.__text: 0x21d4d0
   __TEXT.__auth_stubs: 0x2c70
   __TEXT.__init_offsets: 0x8
   __TEXT.__const: 0x269a0
-  __TEXT.__cstring: 0xbb87
-  __TEXT.__gcc_except_tab: 0x1e54c
-  __TEXT.__oslogstring: 0x197bf
+  __TEXT.__cstring: 0xbb82
+  __TEXT.__gcc_except_tab: 0x1e50c
+  __TEXT.__oslogstring: 0x19772
   __TEXT.__unwind_info: 0xeba8
   __DATA_CONST.__got: 0x4e0
   __DATA_CONST.__const: 0xb230

   - /usr/lib/libTelephonyCapabilities.dylib
   - /usr/lib/libTelephonyUtilDynamic.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: 7645D209-8DCA-35D9-9A98-3E155BD3EC9B
+  UUID: 13FAD1A5-934C-3D4F-8FEB-4BD641FDAEC8
   Functions: 12348
   Symbols:   37642
-  CStrings:  4239
+  CStrings:  4235
 
Symbols:
+ ____ZN18QMIATCommandDriver26sendPMCommandResponse_syncEjNSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE_block_invoke.16
- ____ZN18QMIATCommandDriver26sendPMCommandResponse_syncEjNSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE_block_invoke.18
Functions:
~ ____ZN18QMIATCommandDriver14bootstrap_syncEN8dispatch13group_sessionE_block_invoke : 5364 -> 4536
~ __ZN10subscriber19EURSimCommandDriver10setSimInfoERNS_13SimDriverInfoERKN3uim3tlv4SlotERKNSt3__16vectorINS4_8AppIndexENS8_9allocatorISA_EEEESF_ : 3908 -> 3888
CStrings:
- "#D Help AT command received: %s"
- "#D Profile Managment AT command received: %s"
- "="
- "=?"

```
