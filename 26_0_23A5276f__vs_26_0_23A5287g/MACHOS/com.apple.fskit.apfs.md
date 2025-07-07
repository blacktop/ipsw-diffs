## com.apple.fskit.apfs

> `/System/Library/ExtensionKit/Extensions/com.apple.fskit.apfs.appex/com.apple.fskit.apfs`

```diff

-2632.0.36.0.1
-  __TEXT.__text: 0xa7050
+2632.0.54.0.2
+  __TEXT.__text: 0xa7030
   __TEXT.__auth_stubs: 0xea0
   __TEXT.__objc_stubs: 0x5c0
   __TEXT.__objc_methlist: 0x1ec
   __TEXT.__const: 0x88f0
-  __TEXT.__cstring: 0x2de6f
+  __TEXT.__cstring: 0x2de79
   __TEXT.__gcc_except_tab: 0x78
   __TEXT.__oslogstring: 0x11b
   __TEXT.__objc_classname: 0x5b

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libutil.dylib
-  UUID: 0B2F2777-3297-3BE0-B004-B0F87D4E6463
+  UUID: C0E4D69F-411D-38E1-AB8D-22CEF14A4F9A
   Functions: 2324
   Symbols:   1192
   CStrings:  3953
Symbols:
+ _objc_retain_x26
- _objc_retain_x23
Functions:
~ sub_10002b550 : 348 -> 340
~ sub_100058760 -> sub_100058758 : 1300 -> 1268
~ _get_jobj_xfields_ptr : 208 -> 216
CStrings:
+ "(o->o_aflags >> OBJ_AFLAG_DEFERRED_LIST_UPDATE_INDEX_SHIFT) == i"
+ "2632.0.54.0.2"
+ "o->o_aflags & OBJ_AFLAG_DEFERRED_LIST_UPDATE"
- "(aflags >> OBJ_AFLAG_DEFERRED_LIST_UPDATE_INDEX_SHIFT) == i"
- "2632.0.36.0.1"
- "aflags & OBJ_AFLAG_DEFERRED_LIST_UPDATE"

```
