## UserActivity

> `/System/Library/PrivateFrameworks/UserActivity.framework/UserActivity`

```diff

-606.4.2.0.0
-  __TEXT.__text: 0x45950
+606.4.3.0.0
+  __TEXT.__text: 0x45bac
   __TEXT.__auth_stubs: 0x950
   __TEXT.__objc_methlist: 0x2b28
-  __TEXT.__const: 0x1c0
+  __TEXT.__const: 0x1c8
   __TEXT.__cstring: 0x2947
-  __TEXT.__oslogstring: 0x4e14
+  __TEXT.__oslogstring: 0x4f5b
   __TEXT.__gcc_except_tab: 0x6464
   __TEXT.__dof_UA: 0x1c51
   __TEXT.__unwind_info: 0x17c0

   __TEXT.__objc_methname: 0x7b41
   __TEXT.__objc_methtype: 0x1174
   __TEXT.__objc_stubs: 0x58c0
-  __DATA_CONST.__got: 0x2b0
+  __DATA_CONST.__got: 0x2b8
   __DATA_CONST.__const: 0x1100
   __DATA_CONST.__objc_classlist: 0xc0
   __DATA_CONST.__objc_catlist: 0x8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 780A71DA-9221-3FED-A4A5-7115BED7BB0F
+  UUID: 123723D9-B5F2-32FB-80D2-A0860D0EF278
   Functions: 1295
-  Symbols:   4862
-  CStrings:  2544
+  Symbols:   4863
+  CStrings:  2548
 
Symbols:
+ _NSURLIsSymbolicLinkKey
Functions:
~ -[UAPasteboardFileItemProvider accessFileAtURLWithCompletion:] : 772 -> 1376
CStrings:
+ "Could not check symlink status for URL %{private}@: %@"
+ "Security: Rejecting symlink access for pasteboard URL: %{private}@"
+ "accessFileAtURLWithCompletion: Accessing file at URL: %{private}@"
+ "accessFileAtURLWithCompletion: Symlink check passed, proceeding with file access"
+ "accessFileAtURLWithCompletion: isSymbolicLink check result: %d for URL: %{private}@"
- "Accessing file at URL: %@"

```
