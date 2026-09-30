## wifivelocityd

> `/usr/libexec/wifivelocityd`

```diff

-1150.53.0.0.0
-  __TEXT.__text: 0x9bcc4
-  __TEXT.__auth_stubs: 0x13d0
-  __TEXT.__objc_stubs: 0xd2a0
+1150.55.0.0.0
+  __TEXT.__text: 0x9be8c
+  __TEXT.__auth_stubs: 0x13e0
+  __TEXT.__objc_stubs: 0xd2c0
   __TEXT.__objc_methlist: 0x53ac
   __TEXT.__dlopen_cstrs: 0x31a
-  __TEXT.__const: 0x388
+  __TEXT.__const: 0x398
   __TEXT.__gcc_except_tab: 0x189c
   __TEXT.__objc_methname: 0xdd84
-  __TEXT.__oslogstring: 0xb0df
-  __TEXT.__cstring: 0xc3ca
+  __TEXT.__oslogstring: 0xb178
+  __TEXT.__cstring: 0xc426
   __TEXT.__objc_classname: 0x832
   __TEXT.__objc_methtype: 0x23e9
   __TEXT.__ustring: 0x8c
   __TEXT.__unwind_info: 0x1b30
-  __DATA_CONST.__auth_got: 0x9f8
+  __DATA_CONST.__auth_got: 0xa00
   __DATA_CONST.__got: 0x590
   __DATA_CONST.__auth_ptr: 0x10
-  __DATA_CONST.__const: 0x2918
+  __DATA_CONST.__const: 0x2940
   __DATA_CONST.__cfstring: 0xaee0
   __DATA_CONST.__objc_classlist: 0x258
   __DATA_CONST.__objc_catlist: 0x10

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libpcap.A.dylib
   - @rpath/BloodhoundKit.framework/BloodhoundKit
-  UUID: 7AF5AC90-EE3D-3041-9434-024FD1DC30CD
+  UUID: 7B4A31CF-6241-33B7-9795-46669EF1D5A1
   Functions: 2342
-  Symbols:   508
-  CStrings:  6718
+  Symbols:   509
+  CStrings:  6722
 
Symbols:
+ __os_log_fault_impl
Functions:
~ sub_10002babc : 376 -> 384
~ sub_10002bccc -> sub_10002bcd4 : 744 -> 924
~ sub_10008c374 -> sub_10008c430 : 580 -> 848
CStrings:
+ "-[NSManagedObject(WiFiVelocity) _w5DictionaryRepresentation]"
+ "NSManagedObject+WiFiVelocity.m"
+ "Unexpected non secure codeable object: %@ in results (%lu) for request: %@"
+ "[wifivelocity] %s (%s:%u) Ignoring non secure codeable object (%@) for %@: %@"

```
