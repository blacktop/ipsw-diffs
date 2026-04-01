## UserActivity

> `/System/Library/PrivateFrameworks/UserActivity.framework/UserActivity`

```diff

-594.0.0.0.0
-  __TEXT.__text: 0x4202c
+594.1.2.0.0
+  __TEXT.__text: 0x4227c
   __TEXT.__auth_stubs: 0x9d0
   __TEXT.__objc_methlist: 0x2b38
-  __TEXT.__const: 0x1c0
+  __TEXT.__const: 0x1c8
   __TEXT.__cstring: 0x2914
-  __TEXT.__oslogstring: 0x4e14
+  __TEXT.__oslogstring: 0x4f5b
   __TEXT.__gcc_except_tab: 0x534c
   __TEXT.__dof_UA: 0x1c51
   __TEXT.__unwind_info: 0x14f0

   __TEXT.__objc_methname: 0x7b5d
   __TEXT.__objc_methtype: 0x1174
   __TEXT.__objc_stubs: 0x58c0
-  __DATA_CONST.__got: 0x2b0
+  __DATA_CONST.__got: 0x2b8
   __DATA_CONST.__const: 0x1150
   __DATA_CONST.__objc_classlist: 0xc0
   __DATA_CONST.__objc_catlist: 0x8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 67638098-8F50-3E63-97E7-5FB91906DD63
+  UUID: A51F7B1C-95F2-373C-8288-16459CAD023F
   Functions: 1294
-  Symbols:   4812
-  CStrings:  2544
+  Symbols:   4813
+  CStrings:  2548
 
Symbols:
+ _NSURLIsSymbolicLinkKey
Functions:
~ -[UAPasteboardFileItemProvider accessFileAtURLWithCompletion:] : 656 -> 1248
CStrings:
+ "Could not check symlink status for URL %{private}@: %@"
+ "Security: Rejecting symlink access for pasteboard URL: %{private}@"
+ "accessFileAtURLWithCompletion: Accessing file at URL: %{private}@"
+ "accessFileAtURLWithCompletion: Symlink check passed, proceeding with file access"
+ "accessFileAtURLWithCompletion: isSymbolicLink check result: %d for URL: %{private}@"
- "Accessing file at URL: %@"

```
