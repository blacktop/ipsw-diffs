## libnfrestore.dylib

> `/usr/lib/libnfrestore.dylib`

```diff

-365.3.1.0.0
-  __TEXT.__text: 0xd5c4
-  __TEXT.__auth_stubs: 0x950
-  __TEXT.__const: 0x88
-  __TEXT.__cstring: 0x21c4
-  __TEXT.__oslogstring: 0x18fe
-  __TEXT.__unwind_info: 0x118
-  __DATA_CONST.__got: 0x78
+370.33.1.0.0
+  __TEXT.__text: 0xceac
+  __TEXT.__const: 0x80
+  __TEXT.__cstring: 0x2181
+  __TEXT.__oslogstring: 0x18cb
+  __TEXT.__unwind_info: 0x120
+  __TEXT.__auth_stubs: 0x0
   __DATA_CONST.__const: 0x30
-  __AUTH_CONST.__auth_got: 0x4a8
+  __DATA_CONST.__got: 0x0
   __AUTH_CONST.__cfstring: 0x6c0
+  __AUTH_CONST.__auth_got: 0x4b8
   __DATA.__bss: 0x18
   __DATA.__common: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libPN548_API.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libnfshared.dylib
-  UUID: 3B1D4501-CD84-34CF-A58E-C8482FC01A95
+  UUID: B33C1C66-0C9D-363D-A5C3-598D30970E39
   Functions: 53
-  Symbols:   184
-  CStrings:  551
+  Symbols:   186
+  CStrings:  546
 
Symbols:
+ _NFDriverUnloadStack
+ __NFLogFormattedData
+ __NFLogFormattedDataAlt
- _NFDriverUnloadStackAndLeaveHWEnabled
CStrings:
+ "SE310S_FW_A0_01_01_41_rev172736.bin"
+ "SN200V_FURY_FW_B1_02_01_AE_rev170322.bin"
+ "SN300V_FW_B0_02_01_88_rev172757.bin"
+ "SN300V_FW_B0_02_01_C9_rev170948.bin"
+ "[Hex dump: length=%lu bytes] (%s:%i %s)"
+ "[Hex dump: length=%lu bytes] (%{public}s:%i %{public}s)"
- "%04lX: "
- "%s:%i %s %lu bytes :"
- "%s:%i %{public}s %lu bytes"
- "%s:%i Trying to restore unsupported HW. Bailing with success"
- "%{public}s"
- "%{public}s:%i Trying to restore unsupported HW. Bailing with success"
- "0123456789ABCDEF"
- "SE310S_FW_A0_01_01_37_rev170509.bin"
- "SN200V_FURY_FW_B1_02_01_AF_rev171073.bin"
- "SN300V_FW_B0_02_01_7E_rev171089.bin"
- "SN300V_FW_B0_02_01_FC_rev167600.bin"

```
