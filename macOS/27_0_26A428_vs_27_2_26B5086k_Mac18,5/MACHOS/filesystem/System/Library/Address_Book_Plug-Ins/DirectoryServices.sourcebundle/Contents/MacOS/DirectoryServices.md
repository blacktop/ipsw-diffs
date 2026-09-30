## DirectoryServices

> `/System/Library/Address Book Plug-Ins/DirectoryServices.sourcebundle/Contents/MacOS/DirectoryServices`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__cstring`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__got`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-2765.100.1.1.1
-  __TEXT.__text: 0x2a60
-  __TEXT.__auth_stubs: 0x1e0
-  __TEXT.__objc_stubs: 0xd80
+2768.200.41.0.0
+  __TEXT.__text: 0x2a74
+  __TEXT.__auth_stubs: 0x210
+  __TEXT.__objc_stubs: 0xda0
   __TEXT.__objc_methlist: 0x354
+  __TEXT.__gcc_except_tab: 0x30
   __TEXT.__const: 0x20
   __TEXT.__cstring: 0x4b3
-  __TEXT.__objc_methname: 0xbe4
-  __TEXT.__oslogstring: 0x11d
+  __TEXT.__objc_methname: 0xc10
+  __TEXT.__oslogstring: 0xfd
   __TEXT.__objc_classname: 0x76
-  __TEXT.__objc_methtype: 0x1a5
-  __TEXT.__gcc_except_tab: 0x18
+  __TEXT.__objc_methtype: 0x1b2
   __TEXT.__dlopen_cstrs: 0x43
-  __TEXT.__unwind_info: 0x180
+  __TEXT.__unwind_info: 0x190
   __DATA_CONST.__const: 0xd8
   __DATA_CONST.__cfstring: 0x5c0
   __DATA_CONST.__objc_classlist: 0x18

   __DATA_CONST.__objc_superrefs: 0x18
   __DATA_CONST.__objc_arraydata: 0xb0
   __DATA_CONST.__objc_arrayobj: 0x48
-  __DATA_CONST.__auth_got: 0x100
+  __DATA_CONST.__auth_got: 0x118
   __DATA_CONST.__got: 0x128
-  __DATA.__objc_const: 0x410
-  __DATA.__objc_selrefs: 0x488
-  __DATA.__objc_ivar: 0x1c
+  __DATA.__objc_const: 0x430
+  __DATA.__objc_selrefs: 0x490
+  __DATA.__objc_ivar: 0x20
   __DATA.__objc_data: 0xf0
   __DATA.__data: 0xc0
   - /System/Library/Frameworks/CoreData.framework/Versions/A/CoreData

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 74
-  Symbols:   93
-  CStrings:  261
+  Symbols:   97
+  CStrings:  264
 
Symbols:
+ OBJC_IVAR_$_ABDirectoryServicesSearchOperation._searchRunLoop
+ _CFRunLoopStop
+ _objc_sync_enter
+ _objc_sync_exit
Functions:
~ sub_10d8 : 688 -> 752
~ sub_1b64 -> sub_1ba4 : 124 -> 60
~ sub_1be0 : 152 -> 200
~ sub_1c78 -> sub_1ca8 : 72 -> 92
~ sub_3820 -> sub_3864 : 92 -> 44
CStrings:
+ "@\"NSRunLoop\""
+ "Cancelled."
+ "_searchRunLoop"
+ "dateWithTimeIntervalSinceNow:"
+ "getCFRunLoop"
- "Cancelled. Removing query from runloop: %@"
- "distantFuture"
```
