## configd

> `/usr/libexec/configd`

```diff

-1296.40.6.0.0
-  __TEXT.__text: 0x610d8
+1296.60.3.0.0
+  __TEXT.__text: 0x61838
   __TEXT.__auth_stubs: 0x23c0
   __TEXT.__objc_stubs: 0x1460
   __TEXT.__objc_methlist: 0x854
   __TEXT.__const: 0x130
-  __TEXT.__cstring: 0x2ccc
-  __TEXT.__oslogstring: 0x4e65
+  __TEXT.__cstring: 0x2cfd
+  __TEXT.__oslogstring: 0x4ec0
   __TEXT.__objc_methname: 0x19eb
   __TEXT.__objc_classname: 0x5d
   __TEXT.__objc_methtype: 0x4ef
   __TEXT.__gcc_except_tab: 0x8c
-  __TEXT.__unwind_info: 0x97c
+  __TEXT.__unwind_info: 0x9a8
   __DATA_CONST.__auth_got: 0x11f0
   __DATA_CONST.__got: 0x5c8
-  __DATA_CONST.__auth_ptr: 0xf0
+  __DATA_CONST.__auth_ptr: 0xf8
   __DATA_CONST.__const: 0x18a0
   __DATA_CONST.__cfstring: 0x24a0
   __DATA_CONST.__objc_classlist: 0x28

   __DATA.__objc_superrefs: 0x28
   __DATA.__objc_ivar: 0x90
   __DATA.__objc_data: 0x190
-  __DATA.__data: 0x84
+  __DATA.__data: 0xdc
   __DATA.__common: 0x80
-  __DATA.__bss: 0x5e8
+  __DATA.__bss: 0x5f0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/liblockdown.dylib
   - /usr/lib/libnetwork.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 873
+  Functions: 886
   Symbols:   788
-  CStrings:  1576
+  CStrings:  1582
 
CStrings:
+ "%s: %s (%d): effective %s (%d)"
+ "%s: count %lu"
+ "%s: failed to convert %@ to string\n"
+ "%s: trying again excluding %d"
+ "RouteListFinalize"
+ "effective_ifindex_free"
+ "effective_ifindex_get"
+ "elect_ip"
- "%s: %@ effective %@"
- "copy_effective_if_name"

```
