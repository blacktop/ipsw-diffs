## netstat

> `/usr/sbin/netstat`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA.__data`

```diff

 755.0.0.0.0
-  __TEXT.__text: 0x1b054
+  __TEXT.__text: 0x1b190
   __TEXT.__auth_stubs: 0x4e0
-  __TEXT.__cstring: 0xeebc
+  __TEXT.__cstring: 0xf116
   __TEXT.__const: 0x3d8
   __TEXT.__unwind_info: 0x200
   __DATA_CONST.__const: 0x14b8

   __DATA_CONST.__got: 0x38
   __DATA_CONST.__auth_ptr: 0x10
   __DATA.__data: 0xa6c
-  __DATA.__bss: 0xabc8
+  __DATA.__bss: 0xabd8
   __DATA.__common: 0x6b0
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libpcap.A.dylib
   Functions: 124
   Symbols:   88
-  CStrings:  2353
+  CStrings:  2371
 
Functions:
~ sub_1000189b8 : 4200 -> 4308
~ sub_100019c54 -> sub_100019cc0 : 104 -> 136
~ sub_100019cbc -> sub_100019d48 : 168 -> 172
~ sub_100019dc0 -> sub_100019e50 : 4960 -> 5096
~ sub_10001b354 -> sub_10001b46c : 104 -> 136
~ sub_10001b3bc -> sub_10001b4f4 : 168 -> 172
CStrings:
+ "DROP_REASON_IP6_NDP_SELF_LLADDR"
+ "DROP_REASON_IPSEC_IN_AUTH_FAILED"
+ "DROP_REASON_IPSEC_IN_BAD_SPI"
+ "DROP_REASON_IPSEC_IN_DECRYPT_FAILED"
+ "DROP_REASON_IPSEC_IN_INVALID"
+ "DROP_REASON_IPSEC_IN_MBUF_ALLOC_FAILED"
+ "DROP_REASON_IPSEC_IN_NO_SA"
+ "DROP_REASON_IPSEC_IN_POLICY"
+ "DROP_REASON_IPSEC_IN_REPLAY"
+ "IPsec input: authentication failed"
+ "IPsec input: bad SPI"
+ "IPsec input: decryption failed"
+ "IPsec input: invalid or malformed packet"
+ "IPsec input: mbuf allocation failed"
+ "IPsec input: no security association found"
+ "IPsec input: replay check failed"
+ "IPsec input: security policy violation"
+ "IPv6 NDP option claims our own LL address"
```
