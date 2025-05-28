## nehelper

> `/usr/libexec/nehelper`

```diff

-1838.102.2.0.0
-  __TEXT.__text: 0x21a74
-  __TEXT.__auth_stubs: 0x10d0
-  __TEXT.__objc_stubs: 0x24c0
+1838.122.1.0.0
+  __TEXT.__text: 0x21e08
+  __TEXT.__auth_stubs: 0x10e0
+  __TEXT.__objc_stubs: 0x2520
   __TEXT.__objc_methlist: 0x30c
   __TEXT.__const: 0x4c
   __TEXT.__gcc_except_tab: 0x32c
-  __TEXT.__objc_methname: 0x1c8b
-  __TEXT.__oslogstring: 0x4377
+  __TEXT.__objc_methname: 0x1cbd
+  __TEXT.__oslogstring: 0x4432
   __TEXT.__cstring: 0x57b1
   __TEXT.__objc_classname: 0x1a5
   __TEXT.__objc_methtype: 0x251
-  __TEXT.__unwind_info: 0x400
-  __DATA_CONST.__auth_got: 0x878
-  __DATA_CONST.__got: 0x158
+  __TEXT.__unwind_info: 0x3fc
+  __DATA_CONST.__auth_got: 0x880
+  __DATA_CONST.__got: 0x160
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__const: 0xc30
   __DATA_CONST.__cfstring: 0x4be0

   __DATA_CONST.__objc_arrayobj: 0x30
   __DATA_CONST.__objc_dictobj: 0x50
   __DATA.__objc_const: 0x19a8
-  __DATA.__objc_selrefs: 0x950
+  __DATA.__objc_selrefs: 0x968
   __DATA.__objc_ivar: 0xd4
   __DATA.__objc_data: 0x500
   __DATA.__data: 0xc8
-  __DATA.__bss: 0x290
+  __DATA.__bss: 0x288
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreLocation.framework/CoreLocation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/libnetwork.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 242
-  Symbols:   373
-  CStrings:  1570
+  Symbols:   375
+  CStrings:  1578
 
Symbols:
+ _SecIdentityCreate
+ _kSecClassKey
CStrings:
+ "%@ SecItemCopyMatching for cert failed %d"
+ "%@ SecItemCopyMatching for identity failed %d"
+ "%@ SecItemCopyMatching for key failed %d"
+ "Created new key proxy"
+ "Failed to create identity reference"
+ "identity"
+ "isModernSystem"
+ "keyPersistentReference"

```
