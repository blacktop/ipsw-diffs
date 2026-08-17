## mDNSResponder

> `usr/sbin/mDNSResponder`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_intobj`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__data`

```diff

-2881.160.4.0.0
-  __TEXT.__text: 0x103d2c
+2881.160.4.700.1
+  __TEXT.__text: 0x103dd8
   __TEXT.__auth_stubs: 0x2f20
   __TEXT.__objc_stubs: 0xe60
   __TEXT.__objc_methlist: 0x2a4
-  __TEXT.__const: 0x1218
-  __TEXT.__cstring: 0x189d8
+  __TEXT.__const: 0x1220
+  __TEXT.__cstring: 0x189ab
   __TEXT.__gcc_except_tab: 0x370
   __TEXT.__oslogstring: 0x1e454
   __TEXT.__objc_classname: 0x5ff

   - /usr/lib/libxml2.2.dylib
   Functions: 1774
   Symbols:   3805
-  CStrings:  4557
+  CStrings:  4556
 
Symbols:
+ _FormatKeepaliveRData
- _UpdateKeepaliveRData
Functions:
~ _UpdateKeepaliveRData -> _FormatKeepaliveRData : 1208 -> 780
~ _mDNSPlatformGetRemoteMacAddr : 636 -> 1004
~ _GetProxyRecords : 924 -> 1156
CStrings:
+ "FormatKeepaliveRData: InterfaceID mismatch mti.IntfId = %p InterfaceID = %p"
+ "FormatKeepaliveRData: mDNSPlatformRetrieveTCPInfo failed %d"
+ "FormatKeepaliveRData: not a valid record %s for keepalive %#a:%d %#a:%d"
+ "UpdateKeepaliveRDataWithMAC: Freed allocated memory for keep alive packet: %s "
+ "UpdateKeepaliveRDataWithMAC: successfully updated the record %s"
+ "mDNSResponder-2881.160.4.700.1"
- "UpdateKeepaliveRData: Freed allocated memory for keep alive packet: %s "
- "UpdateKeepaliveRData: could not allocate memory %s"
- "UpdateKeepaliveRData: not a valid record %s for keepalive %#a:%d %#a:%d"
- "UpdateKeepaliveRData: successfully updated the record %s"
- "mDNSPlatformRetrieveTCPInfo: InterfaceID mismatch mti.IntfId = %p InterfaceID = %p"
- "mDNSPlatformRetrieveTCPInfo: mDNSPlatformRetrieveTCPInfo failed %d"
- "mDNSResponder-2881.160.4"
```
