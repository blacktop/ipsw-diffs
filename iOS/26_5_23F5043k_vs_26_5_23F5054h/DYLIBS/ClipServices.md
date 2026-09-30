## ClipServices

> `/System/Library/PrivateFrameworks/ClipServices.framework/ClipServices`

```diff

-1035.2.0.0.0
-  __TEXT.__text: 0x3b63c
+1036.1.0.0.0
+  __TEXT.__text: 0x3b714
   __TEXT.__auth_stubs: 0x8f0
   __TEXT.__objc_methlist: 0x322c
   __TEXT.__gcc_except_tab: 0xcc0
   __TEXT.__const: 0x110
   __TEXT.__cstring: 0x3eb2
-  __TEXT.__oslogstring: 0x47a8
+  __TEXT.__oslogstring: 0x481f
   __TEXT.__dlopen_cstrs: 0x2e4
-  __TEXT.__unwind_info: 0x1170
+  __TEXT.__unwind_info: 0x1178
   __TEXT.__objc_classname: 0x52c
   __TEXT.__objc_methname: 0xa177
   __TEXT.__objc_methtype: 0x145c

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: DBF3F15E-AFD9-32C0-A1E3-0308A27925F2
-  Functions: 1494
-  Symbols:   5318
-  CStrings:  3046
+  UUID: 315DAF65-8454-3772-8366-42646656AB65
+  Functions: 1495
+  Symbols:   5320
+  CStrings:  3048
 
Symbols:
+ -[CPSSession _retrieveInstalledApplicationIconWithAppIconURL:clipBundleID:].cold.3
Functions:
~ -[CPSSession _retrieveInstalledApplicationIconWithAppIconURL:clipBundleID:] : 576 -> 724
~ -[CPSClipMetadataRequest proxy:didRetrieveApplicationIcon:] : 156 -> 160
+ -[CPSSession _retrieveInstalledApplicationIconWithAppIconURL:clipBundleID:].cold.3
CStrings:
+ "Unable to use a valid appIconURL for image store."
+ "appIconURL is not available for %{private}@, use full App Store URL."

```
