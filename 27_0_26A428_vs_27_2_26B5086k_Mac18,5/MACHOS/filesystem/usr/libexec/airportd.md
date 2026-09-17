## airportd

> `/usr/libexec/airportd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__gcc_except_tab`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-19175.65.0.0.0
-  __TEXT.__text: 0xdda64
-  __TEXT.__auth_stubs: 0x1fe0
-  __TEXT.__objc_stubs: 0x102e0
+19177.1.0.0.0
+  __TEXT.__text: 0xddc30
+  __TEXT.__auth_stubs: 0x1ff0
+  __TEXT.__objc_stubs: 0x10300
   __TEXT.__objc_methlist: 0x5680
   __TEXT.__const: 0xb28
-  __TEXT.__objc_methname: 0x14a73
+  __TEXT.__objc_methname: 0x14a91
   __TEXT.__objc_classname: 0x3be
   __TEXT.__objc_methtype: 0x3400
   __TEXT.__gcc_except_tab: 0x2114
-  __TEXT.__cstring: 0x2dfba
-  __TEXT.__oslogstring: 0x14c4
-  __TEXT.__unwind_info: 0x2d78
+  __TEXT.__cstring: 0x2e092
+  __TEXT.__oslogstring: 0x151d
+  __TEXT.__unwind_info: 0x2d80
   __DATA_CONST.__const: 0x3270
   __DATA_CONST.__cfstring: 0x9b00
   __DATA_CONST.__objc_classlist: 0x128

   __DATA_CONST.__objc_arraydata: 0x2a0
   __DATA_CONST.__objc_dictobj: 0x168
   __DATA_CONST.__objc_arrayobj: 0x78
-  __DATA_CONST.__auth_got: 0x1008
+  __DATA_CONST.__auth_got: 0x1010
   __DATA_CONST.__got: 0x940
   __DATA_CONST.__auth_ptr: 0x28
   __DATA.__objc_const: 0x6938
-  __DATA.__objc_selrefs: 0x4940
+  __DATA.__objc_selrefs: 0x4948
   __DATA.__objc_ivar: 0x728
   __DATA.__objc_data: 0xb90
   __DATA.__data: 0x424

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libpcap.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 2825
-  Symbols:   831
-  CStrings:  7559
+  Functions: 2826
+  Symbols:   832
+  CStrings:  7564
 
Symbols:
+ _securityTypeForLegacySecurityTypeNoTranslate
CStrings:
+ "-[CWXPCConnection queryAllWiFiProfilesAndReply:]"
+ "<%s[%d]> %s: QUERY ALL WIFI NETWORKS: location services not authorized for pid %ld (%@), profiles will be redacted unless exempt\n"
+ "<%{public}s:%u> xpcConnection is NULL, returning configuration with empty known networks"
+ "CWXCopyConfigurationForXPCConnection"
+ "setPrivateMacNetworkTypeHome:"
```
