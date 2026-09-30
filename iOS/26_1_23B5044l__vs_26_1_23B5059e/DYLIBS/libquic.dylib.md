## libquic.dylib

> `/usr/lib/libquic.dylib`

```diff

-5569.40.67.0.0
-  __TEXT.__text: 0xcfb8c
+5569.40.91.0.0
+  __TEXT.__text: 0xcfd14
   __TEXT.__auth_stubs: 0x1aa0
   __TEXT.__objc_methlist: 0x244
   __TEXT.__const: 0x39d
   __TEXT.__cstring: 0x8f35
-  __TEXT.__oslogstring: 0x117d8
-  __TEXT.__unwind_info: 0xe30
+  __TEXT.__oslogstring: 0x11825
+  __TEXT.__unwind_info: 0xe28
   __TEXT.__objc_classname: 0xa
   __TEXT.__objc_methname: 0x7e6
   __TEXT.__objc_methtype: 0xd09

   __DATA.__objc_ivar: 0xc
   __DATA.__data: 0x50
   __DATA.__crash_info: 0x148
-  __DATA.__bss: 0x5a0
+  __DATA.__bss: 0x550
   __DATA_DIRTY.__data: 0x14
-  __DATA_DIRTY.__bss: 0x6e8
+  __DATA_DIRTY.__bss: 0x728
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Network.framework/Network
   - /System/Library/Frameworks/Security.framework/Security
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A3EDC5B6-81F5-364D-B3D2-699BF4B21E50
+  UUID: 0A8A8CC1-2CFD-3B89-B410-5E91D882AD6F
   Functions: 1158
   Symbols:   3181
-  CStrings:  2928
+  CStrings:  2929
 
Symbols:
+ _nw_setting_pqtls_disable_non_h3_quic
- _nw_setting_pqtls_enable_non_h3_quic
Functions:
~ _quic_conn_retire_dcid : 908 -> 1300
CStrings:
+ "%{public}s %{public}s [%{public}s-%{public}s] unable to find DCID %{public}s"

```
