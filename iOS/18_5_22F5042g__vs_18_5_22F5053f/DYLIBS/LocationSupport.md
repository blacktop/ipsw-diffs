## LocationSupport

> `/System/Library/PrivateFrameworks/LocationSupport.framework/LocationSupport`

```diff

-2960.0.60.0.0
-  __TEXT.__text: 0x24544
+2964.0.3.0.0
+  __TEXT.__text: 0x247fc
   __TEXT.__auth_stubs: 0xf40
   __TEXT.__objc_methlist: 0x1764
   __TEXT.__const: 0x285
-  __TEXT.__cstring: 0x1b25
+  __TEXT.__cstring: 0x1b2d
   __TEXT.__gcc_except_tab: 0x1660
-  __TEXT.__oslogstring: 0x60e2
-  __TEXT.__unwind_info: 0xbf0
+  __TEXT.__oslogstring: 0x62b0
+  __TEXT.__unwind_info: 0xbe8
   __TEXT.__objc_classname: 0x412
-  __TEXT.__objc_methname: 0x2950
+  __TEXT.__objc_methname: 0x2965
   __TEXT.__objc_methtype: 0x858
-  __TEXT.__objc_stubs: 0x24c0
+  __TEXT.__objc_stubs: 0x24e0
   __DATA_CONST.__got: 0x2a8
   __DATA_CONST.__const: 0x570
   __DATA_CONST.__objc_classlist: 0x110
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xcb0
+  __DATA_CONST.__objc_selrefs: 0xcb8
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0xd0
   __DATA_CONST.__objc_arraydata: 0x8

   - /usr/lib/libobjc.A.dylib
   Functions: 729
   Symbols:   484
-  CStrings:  1210
+  CStrings:  1216
 
CStrings:
+ "#LogEncryption Can't create the new encryption key dir"
+ "#LogEncryption Can't persist the new log encryption key"
+ "%04d_%03d"
+ "CLLogKeyStorePath == nullptr && __c11_atomic_compare_exchange_strong(&CLLogAtomicKeyUpdateInProgress, &expected, true, 5, 5) && __c11_atomic_load(&CLLogAtomicKeyCreationTime, 5) == 0"
+ "localizedDescription"
+ "{\"msg%{public}.0s\":\"#LogEncryption Can't create the new encryption key dir\", \"directory\":%{public, location:escape_only}s, \"error\":%{public, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#LogEncryption Can't persist the new log encryption key\", \"fileName\":%{public, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#LogEncryption New log encryption key created\", \"fileName\":%{public, location:escape_only}s}"
- "#LogEncryption New log encryption key created: %@"
- "CLLogKeyStorePath == nullptr && __c11_atomic_compare_exchange_strong(&CLLogAtomicKeyUpdateInProgress, &expected, true, 5, 5) && __c11_atomic_load(&CLLogAtomicKeyExpirationTime, 5) == 0"

```
